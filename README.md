<h1 align="center">
  <img src="images/cacti_mcp_logo.png" width="360" alt="Cacti MCP: a green cactus with linked connectors.">
</h1>

<p align="center">
  <a href="https://github.com/somethingwithproof/cacti-mcp/actions/workflows/ci.yml"><img src="https://github.com/somethingwithproof/cacti-mcp/actions/workflows/ci.yml/badge.svg?branch=develop" alt="CI"></a>
</p>

Expose Cacti abilities as MCP tools through a small Python adapter.
Cacti owns authentication, authorization, input validation, and execution.
This process translates MCP requests into the plugin's HTTP API.

The companion [Abilities plugin](https://github.com/somethingwithproof/plugin_abilities)
is required. Version 0.1 supports read-only device inventory and system version
information. Doctor diagnostics and repairs are not exposed in this version.

```text
MCP client --stdio--> cacti-mcp --HTTPS--> Cacti Abilities plugin
                                           |-- Cacti permissions
                                           |-- ability providers
                                           `-- execution audit
```

## Install and run

Requires Python 3.12 or later and [uv](https://docs.astral.sh/uv/).
From a checkout of this repository:

```sh
uv sync --locked
uv run --locked cacti-mcp --help
```

Install and enable the PHP plugin, grant its **Abilities API** realm to a
dedicated Cacti user, and provision a scoped token using the plugin's CLI.
The user's existing Cacti realms and device permissions still apply.

Provide the token through your secret manager as `CACTI_MCP_TOKEN`; never add it
to source control or command arguments. Set the endpoint separately:

```sh
export CACTI_MCP_ENDPOINT=https://cacti.example/cacti/plugins/abilities/api.php
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

## Use cases

Connect an MCP client to list the Cacti devices its dedicated user may see,
look up one permitted device, or retrieve installation versions when the user
has the required administrative realm. Names and input schemas come from
Cacti Abilities discovery, so the adapter does not duplicate each provider.
See the [plugin's use cases and WordPress Abilities API comparison](https://github.com/somethingwithproof/plugin_abilities#use-cases)
for the registration model and current limits.

## Behavior

- Uses the official [`mcp` Python SDK](https://github.com/modelcontextprotocol/python-sdk)
  for initialization, tool discovery, calls, and stdio framing.
- Exposes only abilities marked read-only by API v1. Schemas and names come
  from Cacti; the adapter contains no SQL, device credentials, or repair commands.
- Refreshes discovery and the Cacti CSRF token before every execution. The PHP
  endpoint rechecks bearer-token validity and permissions on the POST.
- Keeps session cookies in memory. Uses verified HTTPS, refuses redirects, and
  ignores proxy environment variables. HTTP requires `--allow-loopback-http`
  and a literal loopback address or `localhost`.
- Bounds API calls to 35 seconds overall, 30 seconds of network inactivity, and
  approximately 1 MB per response. Calls are serialized per client session.
- Does not retry execution automatically. HTTP error bodies and credentials
  are excluded from tool errors. Stdout is reserved for MCP messages.

The SDK version is pinned by `uv.lock`. This adapter uses its v1 tools/stdio
interface; it does not implement a remote MCP HTTP endpoint, OAuth, resources,
prompts, subscriptions, or background tasks.

See [the API contract](docs/api.md) and [implementation plan](docs/plan.md).

## Development

```sh
uv sync --locked
uv run --locked ruff check .
uv run --locked pytest
uv build
```

Tests cover HTTP validation, credential isolation, session/CSRF handling,
permission changes, and an actual SDK client/server subprocess exchange against
a fixture HTTP server. They do not require a live Cacti installation.

The repository uses `src/cacti_mcp/`, pytest, Ruff, uv, and Hatchling. CI tests
Python 3.12, 3.13, and 3.14. A separate packaging job builds the wheel
and source archive, installs the wheel outside the checkout, and smoke-tests
both entry points. Distributions and test results are workflow artifacts.

## License

GPL-2.0-or-later. See [LICENSE](LICENSE).
