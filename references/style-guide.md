# Tools & Integrations Knowledge Style Guide

## Voice

- Be practical, concrete, and safety-aware.
- Separate planning, setup, dry-run, and live execution.
- Say exactly what tool access exists and what is only proposed.
- Prefer simple implementation steps over broad automation claims.

## Terminology

- **Tool**: a runtime capability the agent can call directly.
- **Connector**: an authenticated integration to an external system.
- **Action**: an operation that performs work, such as read, create, update, send, post, append, or delete.
- **Read action**: retrieves data without changing external systems.
- **Write action**: changes data, sends content, posts messages, opens tickets, creates records, or calls non-idempotent APIs.
- **Dry run**: validates the request without changing production systems.
- **Idempotency key**: a stable key used to prevent duplicate writes.
- **Least privilege**: the minimum permission needed to complete the task.

## Response patterns

### Integration plan

Use this structure when designing an integration:

1. Goal
2. Systems involved
3. Available tools versus requested tools
4. Trigger and action boundary
5. Permissions and authentication
6. Data mapping
7. Action schema or API outline
8. Approval and dry-run plan
9. Logging, monitoring, and rollback
10. Risks and next safe step

### Tool execution note

When a tool is actually used, state:

- Tool called
- Inputs used
- Records or messages affected
- Whether anything was sent, posted, updated, or only drafted
- Errors and skipped items
- Follow-up needed

### Connector setup note

When a requested connector is not available, state:

- The connector is not available in the current runtime.
- The safest setup path or schema to create it.
- Required scopes and why each one is needed.
- A dry-run test the user can perform after connecting it.

## Examples

### Gmail send workflow

Preferred framing: "I can draft the message and show the recipient, subject, body, and attachments for approval before sending."

Avoid: "I will send this to everyone now" unless a send-capable tool is available and the user has explicitly authorized sending.

### Slack posting workflow

Preferred framing: "Confirm the workspace, channel, and visibility, then post after approval or provide a draft."

Avoid posting confidential content into broad channels or tagging users without a clear reason.

### Sheets update workflow

Preferred framing: "Validate headers, identify rows by stable keys, write only the approved columns, and provide rollback values."

Avoid overwriting formulas, formatting, or entire sheets unless specifically requested and backed up.

### CRM update workflow

Preferred framing: "Match records by stable IDs or deduplication keys, preview field changes, and log the update."

Avoid ambiguous updates such as "update all leads" without filters, counts, samples, and approval.

### API connector workflow

Preferred framing: "Define request and response schemas, auth method, rate limits, retries, idempotency, and error states before execution."

Avoid calling undocumented write endpoints without a sandbox test or rollback plan.

## Edge cases

- For bulk actions, require filters, counts, samples, rate limits, unsubscribe or opt-out handling if messaging is involved, and approval.
- For personal data, minimize copied fields and avoid exposing data in logs.
- For destructive actions, provide a safer alternative such as archive, draft, mark for review, or export a deletion candidate list.
- For cross-system syncs, choose a source of truth and conflict-resolution rule.
- For webhooks, verify event authenticity, retries, duplicate delivery behavior, and replay protection.
- For rate limits, specify batching, backoff, retry windows, and failure queues.
