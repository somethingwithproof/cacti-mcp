"""Bounded HTTP access to the Cacti MCP plugin's v2 API, independent of MCP."""

import asyncio
import http.cookiejar
import json
import re
from types import TracebackType
from typing import Any, Self
from urllib.parse import urlsplit

import httpx

MAX_RESPONSE_BYTES = 1_100_000
MAX_REQUEST_BYTES = 16_384
MAX_ABILITIES = 256
PAGE_SIZE = 100
MAX_PAGES = 20
ENDPOINT_SUFFIX = '/plugins/mcp/api.php'
TOKEN_PATTERN = re.compile(r'cmcp_pat_[a-f0-9]{64}')
# plugin_mcp lib/registry.php ID_PATTERN (and its 64 character limit).
ID_PATTERN = re.compile(r'[a-z][a-z0-9]*(-[a-z0-9]+){1,7}')
NAME_PREFIX = 'abilities/'
ANNOTATIONS = {'readOnly': True, 'destructive': False, 'idempotent': True}
STATUS_PATTERN = re.compile(r'[A-Z_]{1,32}')
REASON_PATTERN = re.compile(r'[A-Z][A-Z0-9_]{0,63}')


def ability_id(name: str) -> str:
    """The id for a descriptor name such as abilities/cacti-list-devices."""
    return name.removeprefix(NAME_PREFIX)


def _valid_id(value: object) -> bool:
    return (
        isinstance(value, str)
        and len(value) <= 64
        and ID_PATTERN.fullmatch(value) is not None
    )


def _error_summary(value: Any) -> str:
    """The AIP-193 status and ErrorInfo reason only, never the message."""
    try:
        error = value['error']
        status = error['status']
        reason = error['details'][0]['reason']
    except (KeyError, IndexError, TypeError):
        return ''
    if (
        isinstance(status, str)
        and STATUS_PATTERN.fullmatch(status)
        and isinstance(reason, str)
        and REASON_PATTERN.fullmatch(reason)
    ):
        return f' ({status}, {reason})'
    return ''


class AbilitiesError(Exception):
    """A safe, credential-free error suitable for an MCP tool response."""


class AbilitiesClient:
    """Bearer-only client for the plugin's AIP-style v2 HTTP API.

    The server authorizes every request, so there are no cookies and no CSRF
    step. Construct one client per MCP session.
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
            or not url.path.endswith(ENDPOINT_SUFFIX)
        ):
            raise ValueError('Endpoint must be an HTTPS Cacti MCP plugin URL')
        if not TOKEN_PATTERN.fullmatch(token):
            raise ValueError(
                'Token must look like cmcp_pat_ plus 64 hex digits'
            )
        self._endpoint = endpoint.rstrip('/')
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
        # Bearer-only: never store or replay a server-set cookie.
        self._http.cookies.jar.set_policy(
            http.cookiejar.DefaultCookiePolicy(allowed_domains=[])
        )

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        await self._http.aclose()

    async def _request(
        self,
        method: str,
        path: str,
        params: dict[str, str] | None = None,
        payload: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        try:
            # A wall-clock budget also bounds a peer that trickles bytes.
            async with asyncio.timeout(35):
                async with self._http.stream(
                    method,
                    self._endpoint + path,
                    params=params,
                    json=payload,
                ) as response:
                    ok = response.status_code == 200
                    encoding = response.headers.get('content-encoding', '')
                    if ok and encoding not in {'', 'identity'}:
                        raise AbilitiesError(
                            'Abilities API must return uncompressed JSON'
                        )
                    media = response.headers.get('content-type', '')
                    is_json = media.split(';')[0].strip() == 'application/json'
                    if ok and not is_json:
                        raise AbilitiesError(
                            'Abilities API did not return JSON'
                        )
                    compressed = encoding not in {'', 'identity'}
                    if compressed:
                        # Never decompress: report only the status.
                        raise AbilitiesError(
                            'Abilities API returned HTTP '
                            f'{response.status_code}'
                        )
                    body = bytearray()
                    async for chunk in response.aiter_bytes():
                        body.extend(chunk)
                        if len(body) > MAX_RESPONSE_BYTES:
                            raise AbilitiesError(
                                'Abilities API response exceeded limit'
                            )
                    if not ok:
                        detail = ''
                        if is_json:
                            try:
                                detail = _error_summary(json.loads(body))
                            except (ValueError, RecursionError):
                                pass
                        raise AbilitiesError(
                            'Abilities API returned HTTP '
                            f'{response.status_code}{detail}'
                        )
                    value = json.loads(body)
        except (httpx.HTTPError, TimeoutError):
            raise AbilitiesError('Abilities API connection failed') from None
        except (ValueError, RecursionError):
            raise AbilitiesError(
                'Abilities API returned invalid JSON'
            ) from None
        if not isinstance(value, dict):
            raise AbilitiesError('Abilities API returned invalid data')
        return value

    @staticmethod
    def _check_descriptor(item: Any) -> None:
        if (
            not isinstance(item, dict)
            or not isinstance(item.get('name'), str)
            or not item['name'].startswith(NAME_PREFIX)
            or not _valid_id(ability_id(item['name']))
            or not isinstance(item.get('displayName'), str)
            or not item['displayName']
            or not isinstance(item.get('description'), str)
            or not isinstance(item.get('inputSchema'), dict)
            or item['inputSchema'].get('type') != 'object'
            or not isinstance(item.get('outputSchema'), dict)
            or item.get('annotations') != ANNOTATIONS
        ):
            raise AbilitiesError('Invalid ability descriptor')

    async def discover(self) -> list[dict[str, Any]]:
        async with self._lock:
            abilities: list[dict[str, Any]] = []
            names: set[str] = set()
            tokens: set[str] = set()
            token = ''
            for _ in range(MAX_PAGES):
                params = {'pageSize': str(PAGE_SIZE)}
                if token:
                    params['pageToken'] = token
                page = await self._request('GET', '/v1/abilities', params)
                items = page.get('abilities')
                token = page.get('nextPageToken')
                if token is None:
                    token = ''
                if not isinstance(items, list) or not isinstance(token, str):
                    raise AbilitiesError('Unsupported abilities API response')
                for item in items:
                    self._check_descriptor(item)
                    if item['name'] in names:
                        raise AbilitiesError('Invalid ability descriptor')
                    names.add(item['name'])
                    abilities.append(item)
                if len(abilities) >= MAX_ABILITIES:
                    return abilities[:MAX_ABILITIES]
                if not token:
                    return abilities
                if token in tokens:
                    raise AbilitiesError('Abilities API repeated a page token')
                tokens.add(token)
            raise AbilitiesError('Abilities API returned too many pages')

    async def execute(
        self, name: str, arguments: dict[str, Any]
    ) -> dict[str, Any]:
        """Run the ability with this id and return its result object."""
        if not _valid_id(name) or not isinstance(arguments, dict):
            raise AbilitiesError('Invalid ability call')
        payload = {'arguments': arguments}
        try:
            request = json.dumps(payload, allow_nan=False)
        except (TypeError, ValueError, RecursionError):
            raise AbilitiesError('Invalid ability arguments') from None
        if len(request.encode()) > MAX_REQUEST_BYTES:
            raise AbilitiesError('Ability arguments exceeded limit')
        async with self._lock:
            response = await self._request(
                'POST', f'/v1/abilities/{name}:execute', payload=payload
            )
        result = response.get('result')
        request_id = response.get('requestId')
        if (
            not isinstance(result, dict)
            or not isinstance(request_id, str)
            or not re.fullmatch(r'[a-f0-9]{32}', request_id)
        ):
            raise AbilitiesError('Invalid ability result')
        return result
