import gzip
import json

import httpx
import pytest

from cacti_mcp.client import AbilitiesClient, AbilitiesError

ENDPOINT = 'https://cacti.example.com/plugins/mcp/api.php'
TOKEN = 'cmcp_pat_' + 'a' * 64  # Synthetic credential for the HTTP fixture.
# Shapes below follow plugin_mcp's mcp_api_ability(), mcp_error_body() and
# tests/api.php: GET /v1/abilities returns {abilities, nextPageToken}, and
# the ability id is the name without its "abilities/" prefix.
TOOL = {
    'name': 'abilities/cacti-get-device',
    'displayName': 'Get device',
    'description': 'Read one device.',
    'category': 'inventory',
    'inputSchema': {
        'type': 'object',
        'properties': {'id': {'type': 'integer', 'minimum': 1}},
        'required': ['id'],
        'additionalProperties': False,
    },
    'outputSchema': {
        'type': 'object',
        'properties': {'id': {'type': 'integer'}},
        'required': ['id'],
        'additionalProperties': False,
    },
    'annotations': {
        'readOnly': True,
        'destructive': False,
        'idempotent': True,
    },
}
TOOL_ID = 'cacti-get-device'
OTHER = {**TOOL, 'name': 'abilities/cacti-list-devices'}
CATALOG = {'abilities': [TOOL], 'nextPageToken': None}


def error_body(status, reason, message='secret server text'):
    return {
        'error': {
            'code': 404,
            'message': message,
            'status': status,
            'details': [
                {
                    '@type': 'type.googleapis.com/google.rpc.ErrorInfo',
                    'reason': reason,
                    'domain': 'cacti.net',
                }
            ],
        }
    }


@pytest.mark.anyio
async def test_bearer_only_no_cookies():
    requests = []

    def handler(request):
        requests.append(request)
        assert request.headers['authorization'] == f'Bearer {TOKEN}'
        assert 'cookie' not in request.headers
        if request.method == 'GET':
            assert request.url.path == '/plugins/mcp/api.php/v1/abilities'
            return httpx.Response(
                200,
                json=CATALOG,
                headers={'set-cookie': 'Cacti=fixture; Path=/; Secure'},
            )
        assert request.method == 'POST'
        assert request.url.path == (
            f'/plugins/mcp/api.php/v1/abilities/{TOOL_ID}:execute'
        )
        assert json.loads(request.content) == {'arguments': {'id': 7}}
        return httpx.Response(
            200,
            json={'requestId': 'b' * 32, 'result': {'id': 7}},
            headers={'set-cookie': 'Cacti=fixture; Path=/; Secure'},
        )

    async with AbilitiesClient(
        ENDPOINT, TOKEN, transport=httpx.MockTransport(handler)
    ) as client:
        assert await client.discover() == [TOOL]
        assert await client.execute(TOOL_ID, {'id': 7}) == {'id': 7}
        await client.execute(TOOL_ID, {'id': 7})
        assert len(client._http.cookies.jar) == 0
    assert [r.method for r in requests] == ['GET', 'POST', 'POST']


@pytest.mark.anyio
async def test_discover_follows_page_tokens():
    seen = []

    def handler(request):
        token = request.url.params.get('pageToken')
        seen.append(token)
        if token is None:
            return httpx.Response(
                200, json={'abilities': [TOOL], 'nextPageToken': 'p2'}
            )
        assert token == 'p2'
        return httpx.Response(
            200, json={'abilities': [OTHER], 'nextPageToken': ''}
        )

    async with AbilitiesClient(
        ENDPOINT, TOKEN, transport=httpx.MockTransport(handler)
    ) as client:
        assert await client.discover() == [TOOL, OTHER]
    assert seen == [None, 'p2']


@pytest.mark.anyio
async def test_discover_stops_at_256_items():
    def handler(request):
        page = int(request.url.params.get('pageToken') or 0)
        items = [
            {**TOOL, 'name': f'abilities/fixture-item-{page * 100 + n}'}
            for n in range(100)
        ]
        return httpx.Response(
            200, json={'abilities': items, 'nextPageToken': str(page + 1)}
        )

    async with AbilitiesClient(
        ENDPOINT, TOKEN, transport=httpx.MockTransport(handler)
    ) as client:
        assert len(await client.discover()) == 256


@pytest.mark.anyio
async def test_repeated_page_token_is_an_error():
    transport = httpx.MockTransport(
        lambda request: httpx.Response(
            200,
            json={'abilities': [], 'nextPageToken': 'same'},
        )
    )
    async with AbilitiesClient(ENDPOINT, TOKEN, transport=transport) as client:
        with pytest.raises(AbilitiesError, match='page token'):
            await client.discover()


@pytest.mark.anyio
@pytest.mark.parametrize(
    'name',
    ['cacti.devices.get', '../execute', 'cacti-get-device:execute', 'a/b', ''],
)
async def test_rejects_dotted_ability_name(name):
    def handler(request):
        pytest.fail('Request must not leave the process')

    async with AbilitiesClient(
        ENDPOINT, TOKEN, transport=httpx.MockTransport(handler)
    ) as client:
        with pytest.raises(AbilitiesError, match='Invalid ability'):
            await client.execute(name, {})


@pytest.mark.anyio
async def test_error_message_carries_only_status_and_reason():
    def handler(request):
        return httpx.Response(
            404,
            json=error_body('NOT_FOUND', 'ABILITY_NOT_FOUND', TOKEN),
        )

    async with AbilitiesClient(
        ENDPOINT, TOKEN, transport=httpx.MockTransport(handler)
    ) as client:
        with pytest.raises(AbilitiesError) as error:
            await client.execute(TOOL_ID, {'id': 1})
    text = str(error.value)
    assert '404' in text
    assert 'NOT_FOUND' in text
    assert 'ABILITY_NOT_FOUND' in text
    assert TOKEN not in text
    assert 'secret' not in text


@pytest.mark.anyio
async def test_unsafe_error_fields_are_not_echoed():
    body = error_body('not a status\nline', 'x' * 500, 'secret')
    transport = httpx.MockTransport(
        lambda request: httpx.Response(500, json=body)
    )
    async with AbilitiesClient(ENDPOINT, TOKEN, transport=transport) as client:
        with pytest.raises(AbilitiesError) as error:
            await client.discover()
    assert str(error.value) == 'Abilities API returned HTTP 500'


@pytest.mark.anyio
async def test_server_denial_surfaces_on_execute():
    transport = httpx.MockTransport(
        lambda request: httpx.Response(
            404, json=error_body('NOT_FOUND', 'ABILITY_NOT_FOUND')
        )
    )
    async with AbilitiesClient(ENDPOINT, TOKEN, transport=transport) as client:
        with pytest.raises(AbilitiesError, match='ABILITY_NOT_FOUND'):
            await client.execute(TOOL_ID, {'id': 7})


@pytest.mark.anyio
@pytest.mark.parametrize('status', [301, 302, 307, 401, 403, 429, 500])
async def test_http_errors_do_not_follow_redirects_or_expose_bodies(status):
    requests = []

    def handler(request):
        requests.append(request)
        return httpx.Response(
            status,
            text=TOKEN,
            headers={'location': 'https://other.example'},
        )

    async with AbilitiesClient(
        ENDPOINT, TOKEN, transport=httpx.MockTransport(handler)
    ) as client:
        with pytest.raises(AbilitiesError) as error:
            await client.discover()
    assert TOKEN not in str(error.value)
    assert len(requests) == 1


@pytest.mark.anyio
@pytest.mark.parametrize(
    'payload',
    [
        [],
        {},
        {**CATALOG, 'abilities': 'x'},
        {**CATALOG, 'nextPageToken': 5},
        {**CATALOG, 'nextPageToken': 0},
        {**CATALOG, 'nextPageToken': False},
        {**CATALOG, 'abilities': [TOOL, TOOL]},
        {**CATALOG, 'abilities': [{**TOOL, 'name': '../execute'}]},
        {**CATALOG, 'abilities': [{**TOOL, 'name': 'cacti.devices.get'}]},
        {**CATALOG, 'abilities': [{**TOOL, 'name': 'abilities/one'}]},
        {**CATALOG, 'abilities': [{**TOOL, 'name': 'cacti-get-device'}]},
        {**CATALOG, 'abilities': [{**TOOL, 'displayName': ''}]},
        {**CATALOG, 'abilities': [{**TOOL, 'outputSchema': []}]},
        {
            **CATALOG,
            'abilities': [
                {
                    **TOOL,
                    'annotations': {**TOOL['annotations'], 'readOnly': False},
                }
            ],
        },
        {
            **CATALOG,
            'abilities': [
                {**TOOL, 'annotations': {**TOOL['annotations'], 'extra': True}}
            ],
        },
    ],
)
async def test_malformed_catalog_fails_closed(payload):
    transport = httpx.MockTransport(
        lambda request: httpx.Response(200, json=payload)
    )
    async with AbilitiesClient(ENDPOINT, TOKEN, transport=transport) as client:
        with pytest.raises(AbilitiesError):
            await client.discover()


@pytest.mark.anyio
@pytest.mark.parametrize(
    'body, content_type',
    [
        (b'<html>Login required</html>', 'text/html'),
        (b'{invalid', 'application/json'),
        (b'x' * 1_100_001, 'application/json'),
    ],
)
async def test_invalid_or_oversized_response(body, content_type):
    transport = httpx.MockTransport(
        lambda request: httpx.Response(
            200,
            content=body,
            headers={'content-type': content_type},
        )
    )
    async with AbilitiesClient(ENDPOINT, TOKEN, transport=transport) as client:
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
            200,
            stream=httpx.ByteStream(gzip.compress(b'x' * 100_000)),
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


@pytest.mark.parametrize(
    'endpoint, allow',
    [
        ('http://cacti.example.com/plugins/mcp/api.php', True),
        ('http://127.0.0.1/plugins/mcp/api.php', False),
        ('https://u:p@cacti.example/plugins/mcp/api.php', False),
        (ENDPOINT + '?token=value', False),
        ('https://cacti.example.com/plugins/abilities/api.php', False),
        (ENDPOINT + '#fragment', False),
        ('https://cacti.example.com/other.php', False),
    ],
)
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
            await client.execute(TOOL_ID, {'id': 'x' * 20_000})


@pytest.mark.parametrize(
    'token', ['a' * 64, 'cmcp_pat_' + 'A' * 64, 'cmcp_pat_' + 'a' * 63, '']
)
def test_malformed_token_rejected(token):
    with pytest.raises(ValueError):
        AbilitiesClient(ENDPOINT, token)


@pytest.mark.anyio
async def test_compressed_error_still_reports_status():
    transport = httpx.MockTransport(
        lambda request: httpx.Response(
            503,
            stream=httpx.ByteStream(gzip.compress(b'x' * 1000)),
            headers={
                'content-type': 'application/json',
                'content-encoding': 'gzip',
            },
        )
    )
    async with AbilitiesClient(ENDPOINT, TOKEN, transport=transport) as client:
        with pytest.raises(AbilitiesError) as error:
            await client.discover()
    assert str(error.value) == 'Abilities API returned HTTP 503'
