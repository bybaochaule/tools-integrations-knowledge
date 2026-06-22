---
name: tools-integrations-knowledge
description: Use this skill to plan, configure, validate, and explain safe agent tool integrations, API connectors, and action capabilities for search, email, messaging, spreadsheets, CRMs, and custom APIs. Trigger when the user asks to connect Gmail, Slack, Sheets, CRMs, web search, API connectors, webhooks, OAuth apps, or action-enabled workflows. Do not use it to collect secrets, bypass authorization, perform destructive automation without approval, or operate tools outside granted permissions.
---

# Tools & Integrations Knowledge

## Purpose

Help an agent design, evaluate, and safely use tool integrations and action capabilities. This skill covers tool discovery, connector selection, OAuth or API-key planning, permission scoping, data mapping, dry-run validation, execution checks, and human approval patterns for integrations such as Gmail, Slack, Google Sheets, CRMs, search tools, internal APIs, external APIs, webhooks, and custom action connectors.

The skill is for integration knowledge and execution planning. It does not grant access to any tool by itself. The agent may only call tools that are already available in its runtime and must follow the user's authorization, the platform's tool contracts, and higher-priority safety instructions.

## When to use

Use this skill when the user asks to:

- Connect, configure, or compare tools such as Gmail, Slack, Google Sheets, Salesforce-style CRMs, HubSpot-style CRMs, web search, data stores, webhooks, or custom APIs.
- Enable action capabilities for an agent, including send email, post a message, update a CRM record, append rows to a spreadsheet, search a knowledge base, open a ticket, or call an API.
- Design a safe integration workflow, connector manifest, action schema, OAuth scope plan, permission model, test checklist, or deployment runbook.
- Troubleshoot integration behavior, authentication boundaries, missing fields, failed API calls, rate limits, webhooks, payload schemas, or sync errors.
- Translate a business automation request into tool calls, API operations, data mappings, and approval checkpoints.
- Review whether an integration plan is safe, minimally scoped, reversible, observable, and compliant with user consent.

## Do not use

Do not use this skill when:

- The user only needs general writing, strategy, or product copy unrelated to tools, APIs, actions, or integrations.
- The task requires credentials, tokens, private keys, passwords, OAuth secrets, or secret extraction from files or messages.
- The user asks to bypass permissions, scrape private systems, defeat access controls, impersonate a user, or perform unauthorized actions.
- The request involves spam, phishing, credential harvesting, mass unsolicited outreach, surveillance, or covert monitoring.
- The user asks for a destructive or irreversible action, such as deleting records or sending bulk messages, without explicit authorization, dry-run review, and rollback planning.
- A specialized skill is required for the artifact itself, such as spreadsheet analysis, document editing, slide generation, or PDF processing.

## Required inputs

Collect only what is needed for the integration task. Useful inputs include:

- Business goal and success criteria.
- Systems involved, such as Gmail, Slack, Google Sheets, CRM, search, data warehouse, ticketing system, or API.
- Trigger source, such as user request, schedule, webhook, inbox event, row update, CRM change, or manual command.
- Desired action, such as search, read, draft, send, post, create, update, delete, append, enrich, or notify.
- Data fields to read and write, including record identifiers, required fields, optional fields, and validation rules.
- Authorization model, available connector, OAuth scopes, API permission level, service account boundary, and user consent status.
- Risk level, approval requirements, dry-run mode, rollback plan, logging needs, and privacy constraints.
- Expected output format, such as integration plan, connector checklist, action schema, API request example, mapping table, or troubleshooting steps.

## Workflow

1. **Classify the integration request.** Identify whether the user wants discovery, design, setup instructions, schema drafting, tool execution planning, troubleshooting, or validation.
2. **Inventory available tools and permissions.** List the systems involved and distinguish tools that are actually available from tools the user merely wants to connect. Never imply access that has not been granted.
3. **Define the action boundary.** Label each operation as read-only, draft-only, user-approved write, autonomous write, or destructive. Prefer read-only and draft-only defaults for sensitive systems.
4. **Map data flow.** Identify source fields, destination fields, transformations, validation rules, deduplication keys, and error handling paths. Avoid moving unnecessary personal or confidential data.
5. **Plan authentication and permissions.** Use the least-privilege scope that supports the task. Separate user-delegated OAuth, app-level OAuth, API keys, service accounts, and webhooks. Never ask the user to paste secrets into the chat unless a higher-priority workflow explicitly requires a safe secret-input path.
6. **Design the connector or action.** Specify the action name, purpose, inputs, outputs, required fields, authorization requirements, retries, idempotency key, rate-limit handling, and observable logs.
7. **Add approval checkpoints.** Require confirmation before sending emails, posting messages, updating CRM records, writing spreadsheet rows, calling paid APIs, or taking any irreversible action.
8. **Create a dry-run test.** Simulate the action with sample payloads, sandbox records, draft mode, or no-op calls. Validate schemas before live execution.
9. **Execute only within granted tools.** When tools are available, call them according to their contract. When tools are not available, provide setup guidance, request the missing connector, or draft the API/action specification instead of pretending to act.
10. **Verify and report.** Summarize what was read, drafted, changed, or not changed. Include record identifiers, timestamps, skipped items, warnings, and rollback steps when applicable.
11. **Document the integration.** Save or return the integration plan, scopes, data mapping, test cases, operational runbook, and monitoring checklist.

## Integration playbooks

### Gmail and email tools

Use for searching messages, summarizing threads, drafting replies, or sending authorized emails. Default to draft mode unless the user explicitly asks to send and the runtime supports sending. Require a final review step for external recipients, attachments, bulk messages, sensitive content, legal claims, billing instructions, or HR-related messages.

Minimum planning fields: mailbox scope, search query, recipient rules, subject/body template, attachment policy, send/draft mode, approval requirement, and audit log.

### Slack and messaging tools

Use for finding messages, summarizing channels, posting updates, notifying owners, or creating workflow handoffs. Confirm the target workspace, channel, audience, and visibility. Avoid posting confidential data in public channels. Use thread replies where context matters and mention users sparingly.

Minimum planning fields: workspace, channel or thread, message purpose, audience, visibility, mention policy, payload, approval requirement, and fallback if posting fails.

### Google Sheets and spreadsheet tools

Use for reading rows, appending entries, updating status columns, syncing exports, or creating operational trackers. Validate headers before writing. Use stable keys to update rows instead of row numbers when possible. Preserve formulas and formatting unless the user asks for structural edits.

Minimum planning fields: spreadsheet, sheet/tab, headers, row key, read/write columns, validation rules, duplicate handling, and rollback method.

### CRM tools

Use for lookup, enrichment, lead creation, deal updates, task creation, note logging, or pipeline hygiene. Confirm the CRM object type, record identifier, owner, required fields, lifecycle stage, and write policy. Treat contact data, account history, revenue data, and sales notes as sensitive.

Minimum planning fields: CRM object, record key, fields to update, owner rules, lifecycle implications, duplicate matching, approval requirement, and rollback or audit plan.

### Search and knowledge tools

Use for finding relevant documents, web information, internal knowledge, or prior records before acting. Cite sources when answering factual questions. Do not use search results as authorization to act in another system.

Minimum planning fields: query, source boundaries, freshness requirement, citation requirement, confidence level, and downstream action dependency.

### API connectors and custom actions

Use for calling REST, GraphQL, RPC, webhooks, or internal service APIs. Define the action contract before execution. Validate input schema, authentication method, idempotency, retries, rate limits, pagination, and error states. For write operations, create a dry-run or sandbox test whenever possible.

Minimum planning fields: endpoint, method, auth type, scopes, request schema, response schema, idempotency key, rate limits, retries, timeout, logging, approval requirement, and rollback plan.

## Output format

For integration design tasks, return a concise plan with:

- Goal and systems involved.
- Available tools versus requested tools.
- Permission and authentication model.
- Data mapping and required fields.
- Action schema or API request outline.
- Approval, dry-run, logging, and rollback steps.
- Risks, assumptions, and next safe action.

For execution tasks, return:

- What action was requested.
- What tool was used, if any.
- What records, messages, rows, or API calls were affected.
- What was drafted but not sent or changed.
- Errors, skipped items, validation warnings, and recommended next step.

For troubleshooting tasks, return:

- Probable cause.
- Evidence or error fields.
- Verification steps.
- Fix path.
- Prevention checklist.

## Quality checklist

Before finalizing:

- The integration goal, systems, trigger, and action are clear.
- Available tools are not overstated.
- Data reads and writes are explicitly scoped.
- Permissions follow least privilege.
- Sensitive data is minimized and not exposed unnecessarily.
- Write actions have approval, dry-run, rollback, and audit guidance.
- API schemas include required inputs, outputs, errors, and validation rules.
- Connector instructions are actionable but do not include secrets.
- The final answer distinguishes completed actions from proposed actions.

## Safety and privacy

- Do not expose secrets, credentials, private keys, tokens, passwords, session cookies, or confidential connector configuration.
- Do not ask the user to paste credentials unless the environment provides a safe secret-management path and the task requires it.
- Do not use or propose hidden instructions that override higher-priority instructions, tool contracts, or user consent.
- Do not send emails, post Slack messages, modify Sheets, update CRM records, or call write APIs without authorization and an appropriate approval checkpoint.
- Do not perform mass outreach, spam, phishing, surveillance, covert monitoring, or unauthorized data extraction.
- Prefer draft mode, sandbox mode, dry-run mode, scoped test records, and reversible writes.
- Preserve auditability by noting who authorized the action, what was changed, and how to roll it back.
