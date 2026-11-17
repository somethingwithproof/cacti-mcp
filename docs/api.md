# Abilities API v1

The endpoint is `/plugins/abilities/api.php` under the Cacti installation.
Both methods require `Authorization: Bearer <token>`. The token is a random
256-bit value encoded as 64 lowercase hexadecimal characters. Cacti stores only
its SHA-256 digest, exact ability scopes, owner, expiry, and revocation state.

Deploy over HTTPS and forward the Authorization header to PHP. Do not redirect
the endpoint to another URL. Responses use `Cache-Control: no-store`.
The adapter requests identity encoding and rejects compressed responses so its
size limit is applied before decompression.

For Apache configurations that strip Authorization, forward it in the relevant
virtual host or directory configuration, then reload Apache:

```apache
SetEnvIf Authorization "(.+)" HTTP_AUTHORIZATION=$1
```

With PHP-FPM, ensure the FastCGI configuration forwards `HTTP_AUTHORIZATION`.
An enabled plugin returning 401 for a valid token can indicate a missing header.

## Discovery

`GET` returns `apiVersion`, an authorized `abilities` array, and `csrfToken`.
Each ability has `name`, `description`, `inputSchema`, and `readOnly: true`.
Clients retain the Cacti session cookie and return the CSRF token with the next
POST. Neither the cookie nor CSRF token grants API authorization.

```json
{
  "apiVersion": "1",
  "abilities": [{
    "name": "cacti.devices.get",
    "description": "Read one permitted device. Credentials are excluded.",
    "inputSchema": {
      "type": "object",
      "properties": {"id": {"type": "integer", "minimum": 1, "maximum": 2147483647}},
      "required": ["id"],
      "additionalProperties": false
    },
    "readOnly": true
  }],
  "csrfToken": "opaque-session-token"
}
```

## Execution

`POST` uses `application/x-www-form-urlencoded` with `__csrf_magic` and `request`.
The latter contains JSON with exactly `name` and object-valued `arguments`:

```json
{"name": "cacti.devices.get", "arguments": {"id": 7}}
```

On success, the response is an object with a 32-character hexadecimal
`requestId` and object-valued `result`. This ID identifies the plugin audit row.
The adapter preserves this envelope in MCP structured content and text content.

Execution checks token state, the enabled Cacti user, the plugin realm, exact
scope, provider permissions, and schema. Permission changes since discovery take
effect at execution. Cacti authentication must be enabled. Device providers use
Cacti's allowed-device helper with the
token owner's explicit user ID. Results include only allowlisted fields.

The plugin records execution start and completion without argument or result
contents. If the start record cannot be persisted, the handler does not run.
Read-only describes domain operations; audit and session writes still occur.

## Errors and limits

Plugin errors use `{"error":{"code":"..."}}`. Common HTTP statuses are
400 for malformed input, 401 for invalid/expired/revoked tokens, 403 for denied
permissions, 404 for unavailable devices, 405 for unsupported methods, 413 for
oversized requests, 415 for unsupported content type, and 503 for unavailable
plugin/audit storage. Bootstrap or CSRF failures can instead return a Cacti
HTML response or redirect; the adapter treats either as failure.

The JSON request limit is 16,384 bytes. Form-encoded HTTP bodies are limited to
65,536 bytes. Results are limited to 1,000,000 bytes before the response envelope.
Device lists accept `limit` 1 through 100 and `offset` 0 through 1,000,000.

No implicit write, wildcard scope, arbitrary PHP dispatch, SQL, shell command,
or retry contract exists. Providers are trusted installed Cacti plugin code.
API version changes must be coordinated across both repositories.
