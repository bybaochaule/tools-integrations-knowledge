# Integration Action Plan Template

## Goal

Describe the business outcome.

## Systems involved

- Source system:
- Destination system:
- Runtime tools actually available:
- Requested tools not yet available:

## Trigger

- Manual request:
- Schedule:
- Webhook/event:
- Record/message/row change:

## Action boundary

- Read-only:
- Draft-only:
- User-approved write:
- Autonomous write:
- Destructive action:

## Permissions and authentication

- Auth type:
- Required scopes:
- Least-privilege rationale:
- User consent status:
- Secret-management path:

## Data mapping

| Source field | Destination field | Required? | Validation rule | Notes |
|---|---|---:|---|---|
|  |  |  |  |  |

## Action schema

```json
{
  "action_name": "",
  "description": "",
  "inputs": {},
  "outputs": {},
  "approval_required": true,
  "dry_run_supported": true,
  "idempotency_key": "",
  "rollback_plan": ""
}
```

## Dry-run test

- Sample payload:
- Expected response:
- Validation checks:
- Failure behavior:

## Approval checkpoint

- Reviewer:
- Review items:
- Approval phrase or mechanism:

## Logging and rollback

- Audit log fields:
- Records affected:
- Rollback steps:

## Risks and mitigations

- Risk:
- Mitigation:
