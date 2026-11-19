<h1 align="center">
	<picture>
		<source media="(prefers-color-scheme: dark)" srcset="images/cacti_mcp_logo_dark.png">
		<img src="images/cacti_mcp_logo.png" width="360" alt="Cacti MCP: a cactus with linked connectors. Connect. Discover. Call.">
	</picture>
</h1>

<p align="center">
	<a href="https://github.com/somethingwithproof/cacti-mcp/actions/workflows/ci.yml"><img src="https://github.com/somethingwithproof/cacti-mcp/actions/workflows/ci.yml/badge.svg?branch=develop" alt="CI"></a>
	<a href="LICENSE"><img src="https://img.shields.io/badge/license-GPL--2.0--or--later-blue" alt="License: GPL-2.0-or-later"></a>
	<img src="https://img.shields.io/badge/Python-3.12%2B-3776ab?logo=python&amp;logoColor=white" alt="Python 3.12+">
	<img src="https://img.shields.io/badge/MCP-stdio-2e7d32" alt="MCP over stdio">
	<img src="https://img.shields.io/badge/MCP_plugin_API-v2-2e7d32" alt="MCP plugin API v2">
</p>

Cacti MCP is a Python adapter that exposes the abilities of the
[Cacti MCP plugin](https://github.com/somethingwithproof/plugin_mcp) as MCP
tools over stdio. The plugin already serves MCP over HTTP directly, so use
that when your client can connect to a remote server. This adapter is for
clients that only speak stdio. It uses the official Python MCP SDK and
translates tool calls into the plugin's HTTPS API (v2, bearer token only).
Cacti owns authentication, authorization, validation, and execution.

**Status: in development, before 1.0.** Version 0.1.0 supports read-only device
inventory and installation versions through the companion
[Cacti MCP plugin](https://github.com/somethingwithproof/plugin_mcp).
There is no tagged release yet. Doctor diagnostics and repairs are future work.

## What it exposes

| Operation | MCP tool supplied by the Cacti MCP plugin |
|---|---|
| List the devices the token owner may see | `cacti-list-devices` |
| Read one permitted device | `cacti-get-device` |
| Read Cacti, plugin, and API versions | `cacti-get-system-info` |

Names, descriptions, and input schemas come from Cacti's permission-filtered
discovery response. Additional permitted read-only providers can be discovered
without adding Python tool handlers.

```text
MCP client --stdio--> cacti-mcp --HTTPS--> Cacti MCP plugin
                                           |-- Cacti permissions
                                           |-- ability providers
                                           `-- execution audit
```

## Use cases

Connect an MCP client to list the Cacti devices its dedicated user may see,
look up one permitted device, or retrieve installation versions when the user
has the required administrative realm. Names and input schemas come from
the plugin's discovery response, so the adapter does not duplicate each provider.
See the [plugin's use cases](https://github.com/somethingwithproof/plugin_mcp#use-cases)
for the registration model and current limits.

## Code and test map

| Behavior | Implementation | Test evidence in this repository |
|---|---|---|
| HTTPS validation, bounds, bearer-only auth, and v2 paging | [client.py](src/cacti_mcp/client.py) | [test_client.py](tests/test_client.py) |
| MCP discovery, calls, and permission changes | [server.py](src/cacti_mcp/server.py) | [test_stdio.py](tests/test_stdio.py) |
| Command-line help, version, and missing configuration | [server.py](src/cacti_mcp/server.py), [__main__.py](src/cacti_mcp/__main__.py) | [test_cli.py](tests/test_cli.py) |

The subprocess test uses a real SDK client and server with a fixture HTTP
endpoint. It does not require or replace a live Cacti integration check.

## How it stays safe

- Uses the official [`mcp` Python SDK](https://github.com/modelcontextprotocol/python-sdk)
  for initialization, tool discovery, calls, and stdio framing.
- Exposes only abilities whose annotations are exactly read-only, non-destructive, and idempotent. Schemas and names come
  from Cacti; the adapter contains no SQL, device credentials, or repair commands.
- Sends only the bearer token: no cookies, no CSRF step. The plugin rechecks
  token validity and permissions on every POST.
- Uses verified HTTPS, never stores cookies, refuses redirects, and
  ignores proxy environment variables. HTTP requires `--allow-loopback-http`
  and a literal loopback address or `localhost`.
- Bounds API calls to 35 seconds overall, 30 seconds of network inactivity, and
  approximately 1 MB per response. Calls are serialized per client session.
- Does not retry execution automatically. Tool errors carry only the HTTP
  status, the AIP-193 `status`, and the ErrorInfo `reason`; never server
  message text, response bodies, or credentials. Stdout is reserved for MCP messages.

The SDK version is pinned by `uv.lock`. This adapter uses its v1 tools/stdio
interface; it does not implement a remote MCP HTTP endpoint, OAuth, resources,
prompts, subscriptions, or background tasks.

See [the API contract](docs/api.md) and [implementation plan](docs/plan.md).

## Installation and command line

Requires Python 3.12 or later and [uv](https://docs.astral.sh/uv/).
From a checkout of this repository:

```console
uv sync --locked
uv run --locked cacti-mcp --help
```

Install and enable the PHP plugin, grant its realm to a dedicated Cacti user,
and create a personal access token for that user (format `cmcp_pat_` followed
by 64 lowercase hex digits) in the plugin's console.
The user's existing Cacti realms and device permissions still apply.

Provide the token through your secret manager as `CACTI_MCP_TOKEN`; never add it
to source control or command arguments. Set the endpoint separately:

```console
export CACTI_MCP_ENDPOINT=https://cacti.example.com/cacti/plugins/mcp/api.php
uv run --locked cacti-mcp
```

The process waits for MCP messages on stdin. An MCP client normally launches it.
For clients accepting the common `mcpServers` configuration format:

```json
{
  "mcpServers": {
    "cacti": {
      "command": "uv",
      "args": ["run", "--locked", "--directory", "/absolute/path/cacti-mcp", "cacti-mcp"]
    }
  }
}
```

Configure the client to pass `CACTI_MCP_ENDPOINT` and `CACTI_MCP_TOKEN` to the
subprocess through its environment or secret facility. Environment inheritance
depends on the client. There is no token command-line flag.

The separately installable Python distribution supplies the `cacti-mcp` console
command. No PyPI publication is required to run the checkout. The PHP plugin has
no Python dependency.

## Releases

The distribution version is recorded in [pyproject.toml](pyproject.toml).
Until tagged releases are available, use a source checkout or the
`python-distributions` artifact from a successful
[CI run](https://github.com/somethingwithproof/cacti-mcp/actions/workflows/ci.yml).
The artifact contains a wheel and source archive. The installed package supplies
both the `cacti-mcp` command and `python -m cacti_mcp`; it does not contain the
PHP plugin.

## Development and tests

```console
uv sync --locked
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest
uv build
```

Tests cover HTTP validation, credential isolation, bearer-only requests,
paging, error redaction, and an actual SDK client/server subprocess exchange against
a fixture HTTP server. They do not require a live Cacti installation.

The repository uses `src/cacti_mcp/`, pytest, Ruff, uv, and Hatchling. CI tests
Python 3.12, 3.13, and 3.14. A separate packaging job builds the wheel
and source archive, installs the wheel outside the checkout, and smoke-tests
both entry points. Distributions and test results are workflow artifacts.

## Contributing

Pull requests go to `develop`. Keep the adapter compatible with Python 3.12,
follow the existing Ruff configuration and `src/cacti_mcp/` package layout, and
keep stdout reserved for MCP messages. Add tests for changed transport or tool
behavior, run the checks above, and sign off commits with `git commit -s`.
Coordinate API changes with the Cacti MCP plugin and update [docs/api.md](docs/api.md).

## License

Copyright (C) 2026 Thomas Vincent. Released under the GNU General Public
License, version 2 or later. See [LICENSE](LICENSE).
