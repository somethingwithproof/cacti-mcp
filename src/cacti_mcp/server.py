"""Tools-only MCP server using the official Python SDK's stdio transport."""

import argparse
import asyncio
import os
from typing import Any

from mcp import types
from mcp.server import Server
from mcp.server.stdio import stdio_server

from cacti_mcp import __version__
from cacti_mcp.client import AbilitiesClient, AbilitiesError


def create_server(client: AbilitiesClient) -> Server:
    server = Server('cacti-mcp', version=__version__)

    @server.list_tools()
    async def list_tools() -> list[types.Tool]:
        items = await client.discover()
        return [
            types.Tool(
                name=item['name'],
                description=item['description'],
                inputSchema=item['inputSchema'],
                annotations=types.ToolAnnotations(
                    readOnlyHint=True,
                    destructiveHint=False,
                    idempotentHint=True,
                    openWorldHint=True,
                ),
            )
            for item in items
        ]

    @server.call_tool()
    async def call_tool(
        name: str, arguments: dict[str, Any]
    ) -> dict[str, Any] | types.CallToolResult:
        try:
            return await client.execute(name, arguments)
        except AbilitiesError as error:
            return types.CallToolResult(
                isError=True,
                content=[types.TextContent(type='text', text=str(error))],
            )

    return server


async def serve(endpoint: str, token: str, allow_http: bool) -> None:
    async with AbilitiesClient(
        endpoint, token, allow_loopback_http=allow_http
    ) as client:
        server = create_server(client)
        async with stdio_server() as (reader, writer):
            await server.run(
                reader, writer, server.create_initialization_options()
            )


def main() -> None:
    parser = argparse.ArgumentParser(
        description='Serve Cacti abilities as MCP tools over stdio.'
    )
    parser.add_argument('--version', action='version', version=__version__)
    parser.add_argument(
        '--endpoint',
        default=os.environ.get('CACTI_MCP_ENDPOINT'),
        help='HTTPS URL ending in /plugins/abilities/api.php',
    )
    parser.add_argument(
        '--allow-loopback-http',
        action='store_true',
        help='Allow HTTP to loopback only, for local testing',
    )
    args = parser.parse_args()
    token = os.environ.get('CACTI_MCP_TOKEN', '')
    if not args.endpoint or not token:
        parser.error('Set CACTI_MCP_ENDPOINT and CACTI_MCP_TOKEN')
    try:
        asyncio.run(serve(args.endpoint, token, args.allow_loopback_http))
    except ValueError as error:
        parser.error(str(error))
    except KeyboardInterrupt:
        pass
