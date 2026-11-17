import gzip
import json
from urllib.parse import parse_qs

import httpx
import pytest

from cacti_mcp.client import AbilitiesClient, AbilitiesError

ENDPOINT = 'https://cacti.example/plugins/abilities/api.php'
TOKEN = 'a' * 64  # Synthetic credential used only by the HTTP fixture.
TOOL = {
    'name': 'cacti.devices.get',
    'description': 'Read one device.',
    'inputSchema': {
        'type': 'object',
        'properties': {'id': {'type': 'integer', 'minimum': 1}},
        'required': ['id'],
        'additionalProperties': False,
    },
    'readOnly': True,
}
CATALOG = {'apiVersion': '1', 'abilities': [TOOL], 'csrfToken': 'fixture'}


@pytest.mark.anyio
async def test_cookie_csrf_handshake_and_fresh_discovery():
    methods = []

    def handler(request):
        methods.append(request.method)
        assert request.headers['authorization'] == f'Bearer {TOKEN}'
        if request.method == 'GET':
            return httpx.Response(
                200, json=CATALOG,
                headers={'set-cookie': 'Cacti=fixture; Path=/; Secure'},
            )
        assert request.headers['cookie'] == 'Cacti=fixture'
        data = parse_qs(request.content.decode())
        assert data['__csrf_magic'] == ['fixture']
        assert json.loads(data['request'][0]) == {
            'name': 'cacti.devices.get', 'arguments': {'id': 7},
        }
        return httpx.Response(
            200, json={'requestId': 'b' * 32, 'result': {'id': 7}},
        )

    async with AbilitiesClient(
        ENDPOINT, TOKEN, transport=httpx.MockTransport(handler)
    ) as client:
        assert await client.discover() == [TOOL]
        assert (await client.execute(TOOL['name'], {'id': 7}))['result'] == {
            'id': 7,
        }
        await client.execute(TOOL['name'], {'id': 7})
    assert methods == ['GET', 'GET', 'POST', 'GET', 'POST']


@pytest.mark.anyio
async def test_revoked_permission_prevents_post():
    methods = []

    def handler(request):
        methods.append(request.method)
        return httpx.Response(
            200, json={**CATALOG, 'abilities': []},
        )

    async with AbilitiesClient(
        ENDPOINT, TOKEN, transport=httpx.MockTransport(handler)
    ) as client:
        with pytest.raises(AbilitiesError, match='unavailable'):
            await client.execute(TOOL['name'], {'id': 7})
    assert methods == ['GET']


@pytest.mark.anyio
@pytest.mark.parametrize('status', [301, 302, 307, 401, 403, 429, 500])
async def test_http_errors_do_not_follow_redirects_or_expose_bodies(status):
    requests = []

    def handler(request):
        requests.append(request)
        return httpx.Response(
            status, text=TOKEN, headers={'location': 'https://other.example'},
        )

    async with AbilitiesClient(
        ENDPOINT, TOKEN, transport=httpx.MockTransport(handler)
    ) as client:
        with pytest.raises(AbilitiesError) as error:
            await client.discover()
    assert TOKEN not in str(error.value)
    assert len(requests) == 1


@pytest.mark.anyio
@pytest.mark.parametrize('payload', [
    [], {}, {**CATALOG, 'apiVersion': '2'},
    {**CATALOG, 'csrfToken': ''},
    {**CATALOG, 'abilities': [TOOL, TOOL]},
    {**CATALOG, 'abilities': [{**TOOL, 'readOnly': False}]},
    {**CATALOG, 'abilities': [{**TOOL, 'name': '../execute'}]},
])
async def test_malformed_catalog_fails_closed(payload):
    transport = httpx.MockTransport(
        lambda request: httpx.Response(200, json=payload)
    )
    async with AbilitiesClient(
        ENDPOINT, TOKEN, transport=transport
    ) as client:
        with pytest.raises(AbilitiesError):
            await client.discover()


@pytest.mark.anyio
@pytest.mark.parametrize('body, content_type', [
    (b'<html>Login required</html>', 'text/html'),
    (b'{invalid', 'application/json'),
    (b'x' * 1_100_001, 'application/json'),
])
async def test_invalid_or_oversized_response(body, content_type):
    transport = httpx.MockTransport(lambda request: httpx.Response(
        200, content=body, headers={'content-type': content_type},
    ))
    async with AbilitiesClient(
        ENDPOINT, TOKEN, transport=transport
    ) as client:
        with pytest.raises(AbilitiesError):
            await client.discover()


@pytest.mark.anyio
async def test_connection_failure_is_sanitized():
    def handler(request):
        raise httpx.ConnectError(TOKEN, request=request)

    async with AbilitiesClient(
        ENDPOINT, TOKEN, transport=httpx.MockTransport(handler)
    ) as client:
        with pytest.raises(AbilitiesError) as error:
            await client.discover()
        assert str(error.value) == 'Abilities API connection failed'


@pytest.mark.anyio
async def test_compressed_response_rejected_before_decompression():
    def handler(request):
        assert request.headers['accept-encoding'] == 'identity'
        return httpx.Response(
            200, stream=httpx.ByteStream(gzip.compress(b'x' * 100_000)),
            headers={
                'content-type': 'application/json',
                'content-encoding': 'gzip',
            },
        )

    async with AbilitiesClient(
        ENDPOINT, TOKEN, transport=httpx.MockTransport(handler)
    ) as client:
        with pytest.raises(AbilitiesError, match='uncompressed'):
            await client.discover()


@pytest.mark.parametrize('endpoint, allow', [
    ('http://cacti.example/plugins/abilities/api.php', True),
    ('http://127.0.0.1/plugins/abilities/api.php', False),
    ('https://u:p@cacti.example/plugins/abilities/api.php', False),
    (ENDPOINT + '?token=value', False),
    (ENDPOINT + '#fragment', False),
    ('https://cacti.example/other.php', False),
])
def test_unsafe_endpoints_rejected(endpoint, allow):
    with pytest.raises(ValueError):
        AbilitiesClient(endpoint, TOKEN, allow_loopback_http=allow)


@pytest.mark.anyio
async def test_oversized_arguments_never_send_a_request():
    def handler(request):
        pytest.fail('Request must not leave the process')

    async with AbilitiesClient(
        ENDPOINT, TOKEN, transport=httpx.MockTransport(handler)
    ) as client:
        with pytest.raises(AbilitiesError, match='exceeded'):
            await client.execute(TOOL['name'], {'id': 'x' * 20_000})
