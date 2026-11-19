# Cacti MCP plugin HTTP API (v2)

The adapter targets the plugin's AIP-style API at `/plugins/mcp/api.php` under
the Cacti installation. The abilities contract is version 2; its routes are under
`/v1/`. The authoritative contract is the plugin's
[openapi.json](https://github.com/somethingwithproof/plugin_mcp/blob/develop/openapi.json).
This page records what the adapter relies on.

## Authentication and transport

Every request carries `Authorization: Bearer cmcp_pat_<64 lowercase hex>`. The
token is the only credential: there are no cookies and no CSRF step, and the
adapter never stores or replays a `Set-Cookie`. Deploy over HTTPS and forward
the Authorization header to PHP. Do not redirect the endpoint. The adapter
requests identity encoding and rejects compressed responses so its size limit
applies before decompression.

For Apache configurations that strip Authorization, forward it in the relevant
virtual host or directory configuration, then reload Apache:

```apache
SetEnvIf Authorization "(.+)" HTTP_AUTHORIZATION=$1
```

With PHP-FPM, ensure the FastCGI configuration forwards `HTTP_AUTHORIZATION`.
A 401 for a valid token can indicate a missing header. Routes live in the path
after `api.php`, so nginx must also split and pass path info; a 404 `UNKNOWN_PATH`
means it did not. The plugin's README shows the configuration.

## Discovery

`GET {endpoint}/v1/abilities?pageSize=100[&pageToken=...]` returns
`{"abilities": [...], "nextPageToken": "..."|null}`. The adapter follows
`nextPageToken` until it is empty or absent, stops at 256 abilities, and fails
if the server repeats a token or returns more than 20 pages. Each ability has:

- `name`: `abilities/<id>`, where `<id>` matches
  `[a-z][a-z0-9]*(-[a-z0-9]+){1,7}` and is at most 64 characters.
- `displayName`, `description`, `category`.
- `inputSchema` (`type: object`) and `outputSchema`.
- `annotations`: exactly `readOnly: true`, `destructive: false`,
  `idempotent: true`.

A descriptor that does not fit is rejected. The MCP tool name is `<id>`, its
title is `displayName`, and `outputSchema` and the annotations map to the
tool's output schema and read-only, non-destructive, idempotent hints. The adapter
also sets the open-world hint to false, as the plugin's own MCP endpoint does.

## Execution

`POST {endpoint}/v1/abilities/<id>:execute` with `Content-Type:
application/json` and the body `{"arguments": {...}}`. The adapter rejects any
id outside the pattern above before sending. On success the response is
`{"requestId": "<32 hex>", "result": {...}}`; the adapter returns `result` as
MCP structured content and as JSON text content.

## Errors

Errors follow AIP-193: `{"error": {"code", "message", "status", "details"}}`.
The adapter reports only the HTTP status, `error.status`, and the ErrorInfo
`reason` from `details[0]`, and only when they have the expected shape. It
never shows the server's message text, response bodies, or the token.

The adapter's request body limit is 16,384 bytes and its response limit is
about 1 MB (1,100,000 bytes). Calls are not retried. Before sending, the adapter
validates arguments against the cached input schema; a mismatch or a malformed
schema is reported as a tool error and nothing is sent.
