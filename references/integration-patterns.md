# Integration Patterns

## Gmail pattern

Use cases: search email, summarize threads, draft replies, send approved messages, handle attachments.

Plan fields:

- Mailbox or account boundary
- Search query or thread ID
- Recipient list and external domain review
- Subject and body template
- Attachment rule
- Draft or send mode
- Approval checkpoint
- Audit note

Safety defaults:

- Use search and draft mode before send mode.
- Require explicit approval for external recipients, bulk sends, attachments, financial instructions, legal language, HR content, or sensitive data.
- Never ask for email passwords or OAuth secrets in chat.

## Slack pattern

Use cases: search workspace messages, summarize channels, post updates, notify owners, create escalation threads.

Plan fields:

- Workspace and channel
- Thread or top-level post
- Audience and visibility
- Mention policy
- Message payload
- Approval checkpoint
- Fallback if posting fails

Safety defaults:

- Do not post confidential data to public channels.
- Use thread replies to preserve context.
- Avoid broad mentions unless the user requests them and the channel norms support them.

## Google Sheets pattern

Use cases: read rows, append entries, update statuses, sync exports, create trackers.

Plan fields:

- Spreadsheet and sheet/tab
- Header row and required columns
- Row identifier or deduplication key
- Read columns and write columns
- Data validation
- Duplicate handling
- Rollback values

Safety defaults:

- Validate headers before writing.
- Prefer stable IDs over row numbers.
- Avoid overwriting formulas or formatting.

## CRM pattern

Use cases: lookup contacts, create leads, update opportunities, log notes, create follow-up tasks.

Plan fields:

- CRM object type
- Record ID or matching rule
- Fields to read and write
- Required fields
- Owner assignment
- Lifecycle or pipeline effects
- Duplicate handling
- Audit or rollback plan

Safety defaults:

- Treat customer records, revenue data, and notes as sensitive.
- Preview changes before writing.
- Use narrow filters for bulk updates.

## Search pattern

Use cases: web research, internal knowledge lookup, document discovery, record search before downstream action.

Plan fields:

- Query
- Source boundary
- Freshness need
- Citation requirement
- Confidence level
- Downstream action dependency

Safety defaults:

- Cite factual claims.
- Do not treat search results as permission to act in another system.
- Confirm current facts when the result could change.

## API connector pattern

Use cases: REST calls, GraphQL operations, webhooks, internal service calls, custom actions.

Plan fields:

- API host and endpoint
- Method or operation name
- Authentication type
- Required scopes
- Request schema
- Response schema
- Pagination and filtering
- Timeout and retries
- Rate limits
- Idempotency key
- Error model
- Logging and monitoring
- Approval and rollback

Safety defaults:

- Use sandbox or dry-run mode for write actions.
- Use least-privilege credentials.
- Do not expose tokens, keys, or secrets in prompts, logs, or output.
- Add idempotency for create/update operations.
