"""Tools-only MCP server using the official Python SDK's stdio transport."""

import argparse
import asyncio
import json
import os
from typing import Any

import jsonschema
import mcp_types as types
from mcp.server import Server, ServerRequestContext
from mcp.server.stdio import stdio_server

from cacti_mcp import __version__
from cacti_mcp.client import AbilitiesClient, AbilitiesError, ability_id


def create_server(client: AbilitiesClient) -> Server:
    # The 1.x low-level server validated arguments against the schemas from
    # the last tools/list; 2.x does not, so keep that check here.
    schemas: dict[str, dict[str, Any]] = {}

    async def refresh() -> list[dict[str, Any]]:
        items = await client.discover()
        schemas.clear()
        schemas.update(
            {ability_id(item['name']): item['inputSchema'] for item in items}
        )
        return items

    async def on_list_tools(
        ctx: ServerRequestContext, params: types.PaginatedRequestParams | None
    ) -> types.ListToolsResult:
        return types.ListToolsResult(
            tools=[
                types.Tool(
                    name=ability_id(item['name']),
                    title=item['displayName'],
                    description=item['description'],
                    input_schema=item['inputSchema'],
                    output_schema=item['outputSchema'],
                    annotations=types.ToolAnnotations(
                        read_only_hint=True,
                        destructive_hint=False,
                        idempotent_hint=True,
                        open_world_hint=False,
                    ),
                )
                for item in await refresh()
            ]
        )

    async def on_call_tool(
        ctx: ServerRequestContext, params: types.CallToolRequestParams
    ) -> types.CallToolResult:
        arguments = params.arguments or {}
        try:
            if params.name not in schemas:
                await refresh()
            # Only ids from the last verified catalog may be executed.
            schema = schemas.get(params.name)
            if schema is None:
                raise AbilitiesError('Unknown tool.')
            try:
                jsonschema.validate(arguments, schema)
            except jsonschema.ValidationError as error:
                raise AbilitiesError(
                    f'Input validation error: {error.message}'
                ) from None
            except jsonschema.SchemaError:
                # A malformed server schema is a tool error, not a crash.
                raise AbilitiesError('Invalid tool schema.') from None
            result = await client.execute(params.name, arguments)
        except AbilitiesError as error:
            return types.CallToolResult(
                is_error=True,
                content=[types.TextContent(type='text', text=str(error))],
            )
        return types.CallToolResult(
            content=[
                types.TextContent(
                    type='text', text=json.dumps(result, indent=2)
                )
            ],
            structured_content=result,
        )

    return Server(
        'cacti-mcp',
        version=__version__,
        on_list_tools=on_list_tools,
        on_call_tool=on_call_tool,
    )


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
        description='Serve Cacti MCP plugin abilities as MCP tools over stdio.'
    )
    parser.add_argument('--version', action='version', version=__version__)
    parser.add_argument(
        '--endpoint',
        default=os.environ.get('CACTI_MCP_ENDPOINT'),
        help='HTTPS URL ending in /plugins/mcp/api.php',
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
