# Tools & Integrations Knowledge

## Overview

Tools & Integrations Knowledge helps an agent plan, configure, validate, and safely use tool integrations, API connectors, and action capabilities. It covers integration work involving search, Gmail, Slack, Google Sheets, CRMs, webhooks, and custom APIs.

The skill is designed for safe tool use: it separates planning from execution, distinguishes available tools from requested tools, uses least-privilege permissions, and requires approval before write actions such as sending emails, posting messages, updating CRM records, changing spreadsheets, or calling write APIs.

## When to use

Use this skill when a user asks to connect tools, enable actions, design API connectors, troubleshoot integrations, map data between systems, or create a safe automation plan for agent-driven work.

Common triggers include:

- Connect Gmail, Slack, Sheets, a CRM, search, or an internal API.
- Enable an agent to send email, post messages, update records, append rows, search knowledge bases, or call APIs.
- Draft an action schema, OAuth scope plan, webhook contract, data mapping, or integration runbook.
- Validate whether an automation is safe, reversible, logged, and permissioned.

## Contents

- `SKILL.md`: agent-facing instructions, trigger description, boundaries, workflow, output formats, and safety rules.
- `README.md`: human-readable package overview.
- `agents/openai.yaml`: display metadata, invocation policy, and file dependencies.
- `references/style-guide.md`: terminology, response patterns, examples, and edge cases for integration work.
- `references/integration-patterns.md`: reusable playbooks for Gmail, Slack, Sheets, CRMs, search, and API connectors.
- `assets/action-plan-template.md`: fill-in template for safe integration plans.
- `scripts/validate_integration_plan.py`: deterministic JSON validator for integration-plan checklists.
- `scripts/example_helper.py`: helper entry point that points to the validator.

## Package structure

```text
tools-integrations-knowledge/
|-- SKILL.md
|-- README.md
|-- agents/
|   `-- openai.yaml
|-- assets/
|   |-- .gitkeep
|   `-- action-plan-template.md
|-- references/
|   |-- style-guide.md
|   `-- integration-patterns.md
`-- scripts/
    |-- example_helper.py
    `-- validate_integration_plan.py
```

## Safe use notes

This skill does not grant connector access by itself. It helps an agent reason about connectors and use only tools that are already available in the runtime. It should never collect secrets or imply that Gmail, Slack, Sheets, CRMs, or APIs are connected unless the runtime has those tools and the user has authorized the action.
