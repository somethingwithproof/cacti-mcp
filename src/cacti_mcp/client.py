"""Bounded HTTP access to the abilities plugin, independent of MCP."""

import asyncio
import json
import re
from typing import Any
from urllib.parse import urlsplit

import httpx

MAX_RESPONSE_BYTES = 1_100_000
MAX_REQUEST_BYTES = 16_384


class AbilitiesError(Exception):
    """A safe, credential-free error suitable for an MCP tool response."""


class AbilitiesClient:
    """Use bearer authorization and Cacti's normal cookie/CSRF handshake.

    Construct one client per MCP session. Discovery is refreshed for every
    execution and the server must independently authorize the POST.
    """

    def __init__(
        self,
        endpoint: str,
        token: str,
        *,
        allow_loopback_http: bool = False,
        transport: httpx.AsyncBaseTransport | None = None,
    ) -> None:
        try:
            url = urlsplit(endpoint)
            valid_port = url.port is None or 0 < url.port < 65536
        except ValueError:
            raise ValueError('Invalid abilities endpoint') from None
        loopback = url.hostname in {'localhost', '127.0.0.1', '::1'}
        secure = url.scheme == 'https' or (
            url.scheme == 'http' and allow_loopback_http and loopback
        )
        if (
            not secure
            or not url.hostname
            or not valid_port
            or url.username is not None
            or url.password is not None
            or url.query
            or url.fragment
            or not url.path.endswith('/plugins/abilities/api.php')
        ):
            raise ValueError(
                'Endpoint must be an HTTPS abilities plugin URL'
            )
        if not re.fullmatch(r'[a-f0-9]{64}', token):
            raise ValueError('Token must contain 64 lowercase hex characters')
        self._endpoint = endpoint
        self._lock = asyncio.Lock()
        self._http = httpx.AsyncClient(
            headers={
                'Authorization': f'Bearer {token}',
                'Accept': 'application/json',
                'Accept-Encoding': 'identity',
            },
            timeout=httpx.Timeout(30.0, connect=5.0),
            follow_redirects=False,
            trust_env=False,
            transport=transport,
        )

    async def __aenter__(self) -> 'AbilitiesClient':
        return self

    async def __aexit__(self, *exc: object) -> None:
        await self._http.aclose()

    async def _request(
        self, method: str, data: dict[str, str] | None = None
    ) -> dict[str, Any]:
        try:
            # A wall-clock budget also bounds a peer that trickles bytes.
            async with asyncio.timeout(35):
                async with self._http.stream(
                    method, self._endpoint, data=data
                ) as response:
                    if response.status_code != 200:
                        raise AbilitiesError(
                            'Abilities API returned HTTP '
                            f'{response.status_code}'
                        )
                    encoding = response.headers.get('content-encoding', '')
                    if encoding not in {'', 'identity'}:
                        raise AbilitiesError(
                            'Abilities API must return uncompressed JSON'
                        )
                    media = response.headers.get('content-type', '')
                    if media.split(';')[0].strip() != 'application/json':
                        raise AbilitiesError(
                            'Abilities API did not return JSON'
                        )
                    body = bytearray()
                    async for chunk in response.aiter_bytes():
                        body.extend(chunk)
                        if len(body) > MAX_RESPONSE_BYTES:
                            raise AbilitiesError(
                                'Abilities API response exceeded limit'
                            )
                    value = json.loads(body)
        except (httpx.HTTPError, TimeoutError):
            raise AbilitiesError(
                'Abilities API connection failed'
            ) from None
        except (ValueError, RecursionError):
            raise AbilitiesError(
                'Abilities API returned invalid JSON'
            ) from None
        if not isinstance(value, dict):
            raise AbilitiesError('Abilities API returned invalid data')
        return value

    async def _catalog(self) -> tuple[list[dict[str, Any]], str]:
        response = await self._request('GET')
        items = response.get('abilities')
        csrf = response.get('csrfToken')
        if (
            response.get('apiVersion') != '1'
            or not isinstance(items, list)
            or len(items) > 256
            or not isinstance(csrf, str)
            or not 1 <= len(csrf) <= 4096
        ):
            raise AbilitiesError('Unsupported abilities API response')
        names: set[str] = set()
        for item in items:
            if (
                not isinstance(item, dict)
                or not isinstance(item.get('name'), str)
                or not re.fullmatch(r'[a-z][a-z0-9_.]{0,63}', item['name'])
                or item['name'] in names
                or not isinstance(item.get('description'), str)
                or not isinstance(item.get('inputSchema'), dict)
                or item['inputSchema'].get('type') != 'object'
                or item.get('readOnly') is not True
            ):
                raise AbilitiesError('Invalid ability descriptor')
            names.add(item['name'])
        return items, csrf

    async def discover(self) -> list[dict[str, Any]]:
        async with self._lock:
            items, _ = await self._catalog()
            return items

    async def execute(
        self, name: str, arguments: dict[str, Any]
    ) -> dict[str, Any]:
        if not isinstance(name, str) or not isinstance(arguments, dict):
            raise AbilitiesError('Invalid ability call')
        try:
            request = json.dumps(
                {'name': name, 'arguments': arguments}, allow_nan=False
            )
        except (TypeError, ValueError, RecursionError):
            raise AbilitiesError('Invalid ability arguments') from None
        if len(request.encode()) > MAX_REQUEST_BYTES:
            raise AbilitiesError('Ability arguments exceeded limit')
        async with self._lock:
            items, csrf = await self._catalog()
            if name not in {item['name'] for item in items}:
                raise AbilitiesError('Ability is unavailable')
            response = await self._request(
                'POST', {'__csrf_magic': csrf, 'request': request}
            )
        if (
            not isinstance(response.get('result'), dict)
            or not isinstance(response.get('requestId'), str)
            or not re.fullmatch(r'[a-f0-9]{32}', response['requestId'])
        ):
            raise AbilitiesError('Invalid ability result')
        return response
