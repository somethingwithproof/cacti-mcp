# Implementation plan and package boundary

The first release consists of two independently installable repositories:

1. `plugin_mcp`: Cacti PHP lifecycle, token management, ability
   registry, permission checks, API v1, inventory providers, and execution audit.
2. `cacti-mcp`: Python MCP transport and HTTP adapter. Build with uv/Hatchling;
   launch through the `cacti-mcp` entry point. No PHP files ship in its wheel.

The implementation sequence is registry and authorization, API transport,
adapter, negative-path tests, Cacti integration verification, and packaging.
The API contract is the compatibility boundary; neither package imports code
from the other.

Version 0.1 is limited to system version information and permitted device
inventory. Further providers should first expose bounded read-only operations.
Doctor integration remains future work. Repairs require a separate contract for
preview identity, expiry, explicit approval, current permissions, and audit
failure handling before either package advertises write abilities.

MCP protocol revisions are handled by the official SDK. Dependency updates must
pass the subprocess tests and package build before updating the lockfile.
