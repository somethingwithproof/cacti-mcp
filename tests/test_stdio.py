"""Exercise the real SDK client and server across a subprocess boundary."""

import json
import os
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs

import pytest
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from test_client import CATALOG, TOKEN, TOOL


@pytest.mark.anyio
async def test_sdk_discovery_execution_validation_and_revocation():
    state = {'revoked': False, 'calls': 0}

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *args):
            pass

        def respond(self, status, payload):
            body = json.dumps(payload).encode()
            self.send_response(status)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Content-Length', str(len(body)))
            self.send_header('Set-Cookie', 'Cacti=fixture; Path=/')
            self.end_headers()
            self.wfile.write(body)

        def do_GET(self):
            if (
                state['revoked']
                or self.headers.get('Authorization') != f'Bearer {TOKEN}'
            ):
                self.respond(401, {'error': {'code': 'invalid_token'}})
            else:
                self.respond(200, CATALOG)

        def do_POST(self):
            data = parse_qs(
                self.rfile.read(int(self.headers['Content-Length'])).decode()
            )
            if (
                data.get('__csrf_magic') != ['fixture']
                or self.headers.get('Cookie') != 'Cacti=fixture'
                or self.headers.get('Authorization') != f'Bearer {TOKEN}'
            ):
                self.respond(403, {})
                return
            state['calls'] += 1
            request = json.loads(data['request'][0])
            self.respond(
                200,
                {
                    'requestId': 'b' * 32,
                    'result': {'device': {'id': request['arguments']['id']}},
                },
            )

    http = ThreadingHTTPServer(('127.0.0.1', 0), Handler)
    thread = threading.Thread(target=http.serve_forever, daemon=True)
    thread.start()
    source = str(Path(__file__).resolve().parents[1] / 'src')
    params = StdioServerParameters(
        command=sys.executable,
        args=['-m', 'cacti_mcp', '--allow-loopback-http'],
        env={
            **os.environ,
            'PYTHONPATH': source,
            'CACTI_MCP_ENDPOINT': (
                f'http://127.0.0.1:{http.server_port}'
                '/plugins/abilities/api.php'
            ),
            'CACTI_MCP_TOKEN': TOKEN,
        },
    )
    try:
        async with stdio_client(params) as (reader, writer):
            async with ClientSession(reader, writer) as session:
                init = await session.initialize()
                assert init.serverInfo.name == 'cacti-mcp'
                tools = await session.list_tools()
                assert [tool.name for tool in tools.tools] == [TOOL['name']]
                assert tools.tools[0].annotations.readOnlyHint is True
                result = await session.call_tool(TOOL['name'], {'id': 7})
                assert not result.isError
                assert result.structuredContent['result']['device']['id'] == 7
                invalid = await session.call_tool(TOOL['name'], {'id': '7'})
                assert invalid.isError
                assert state['calls'] == 1
                state['revoked'] = True
                denied = await session.call_tool(TOOL['name'], {'id': 7})
                assert denied.isError
                assert state['calls'] == 1
                assert TOKEN not in denied.model_dump_json()
    finally:
        http.shutdown()
        http.server_close()
        thread.join(timeout=5)
