"""Exercise the real SDK client and server across a subprocess boundary."""

import json
import os
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import pytest
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from test_client import CATALOG, TOKEN, TOOL, TOOL_ID


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
            self.end_headers()
            self.wfile.write(body)

        def do_GET(self):
            if (
                state['revoked']
                or self.headers.get('Authorization') != f'Bearer {TOKEN}'
            ):
                self.respond(401, {'error': {'code': 401}})
            elif (
                self.path.split('?')[0] != '/plugins/mcp/api.php/v1/abilities'
            ):
                self.respond(404, {})
            else:
                self.respond(200, CATALOG)

        def do_POST(self):
            body = json.loads(
                self.rfile.read(int(self.headers['Content-Length']))
            )
            if (
                state['revoked']
                or self.headers.get('Authorization') != f'Bearer {TOKEN}'
            ):
                self.respond(401, {'error': {'code': 401}})
                return
            if (
                self.path
                != f'/plugins/mcp/api.php/v1/abilities/{TOOL_ID}:execute'
            ):
                self.respond(404, {})
                return
            state['calls'] += 1
            self.respond(
                200,
                {
                    'requestId': 'b' * 32,
                    'result': {'id': body['arguments']['id']},
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
                f'http://127.0.0.1:{http.server_port}/plugins/mcp/api.php'
            ),
            'CACTI_MCP_TOKEN': TOKEN,
        },
    )
    try:
        async with stdio_client(params) as (reader, writer):
            async with ClientSession(reader, writer) as session:
                init = await session.initialize()
                assert init.server_info.name == 'cacti-mcp'
                tools = await session.list_tools()
                assert [tool.name for tool in tools.tools] == [TOOL_ID]
                tool = tools.tools[0]
                assert tool.title == TOOL['displayName']
                assert tool.output_schema == TOOL['outputSchema']
                assert tool.annotations.read_only_hint is True
                assert tool.annotations.destructive_hint is False
                assert tool.annotations.idempotent_hint is True
                result = await session.call_tool(TOOL_ID, {'id': 7})
                assert not result.is_error
                assert result.structured_content == {'id': 7}
                invalid = await session.call_tool(TOOL_ID, {'id': '7'})
                assert invalid.is_error
                assert state['calls'] == 1
                state['revoked'] = True
                denied = await session.call_tool(TOOL_ID, {'id': 7})
                assert denied.is_error
                assert state['calls'] == 1
                assert TOKEN not in denied.model_dump_json()
    finally:
        http.shutdown()
        http.server_close()
        thread.join(timeout=5)
