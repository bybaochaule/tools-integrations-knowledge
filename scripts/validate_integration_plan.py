#!/usr/bin/env python3
"""Validate a JSON integration plan for basic safety and completeness.

Usage:
  python scripts/validate_integration_plan.py plan.json

The validator is deterministic and offline. It does not call external APIs,
read secrets, or modify any connected systems.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

REQUIRED_FIELDS = [
    "goal",
    "systems",
    "action_type",
    "auth",
    "data_read",
    "data_write",
    "approval_required",
    "dry_run",
    "rollback_plan",
]

WRITE_ACTIONS = {"send", "post", "create", "update", "append", "delete", "write", "call_write_api"}
DESTRUCTIVE_ACTIONS = {"delete", "purge", "overwrite", "drop", "destroy"}
SECRET_HINTS = {"token", "api_key", "apikey", "secret", "password", "private_key", "session_cookie"}


def flatten_values(value: Any) -> list[str]:
    if isinstance(value, dict):
        out: list[str] = []
        for key, item in value.items():
            out.append(str(key))
            out.extend(flatten_values(item))
        return out
    if isinstance(value, list):
        out = []
        for item in value:
            out.extend(flatten_values(item))
        return out
    return [str(value)]


def validate(plan: dict[str, Any]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    for field in REQUIRED_FIELDS:
        if field not in plan:
            errors.append(f"Missing required field: {field}")

    action_type = str(plan.get("action_type", "")).lower().strip()
    approval_required = bool(plan.get("approval_required", False))
    dry_run = bool(plan.get("dry_run", False))
    rollback_plan = str(plan.get("rollback_plan", "")).strip()

    if action_type in WRITE_ACTIONS and not approval_required:
        errors.append("Write action requires approval_required=true.")
    if action_type in WRITE_ACTIONS and not dry_run:
        warnings.append("Write action should include dry_run=true before live execution.")
    if action_type in DESTRUCTIVE_ACTIONS:
        errors.append("Destructive action must be replaced with a safer review workflow unless explicitly authorized outside this validator.")
    if action_type in WRITE_ACTIONS and len(rollback_plan) < 12:
        errors.append("Write action requires a concrete rollback_plan.")

    scopes = plan.get("auth", {}).get("scopes", []) if isinstance(plan.get("auth"), dict) else []
    if isinstance(scopes, str):
        scopes = [scopes]
    for scope in scopes:
        text = str(scope).lower()
        if "admin" in text or "full" in text or "*" in text:
            warnings.append(f"Scope may be overbroad: {scope}")

    all_text = "\n".join(flatten_values(plan)).lower()
    for hint in SECRET_HINTS:
        if hint in all_text:
            warnings.append(f"Plan text contains a secret-like term: {hint}. Ensure no actual secret value is present.")

    if plan.get("data_write") and not plan.get("audit_log"):
        warnings.append("Plans with data_write should include audit_log fields.")
    if plan.get("systems") and not isinstance(plan.get("systems"), list):
        warnings.append("systems should usually be a list of connected systems.")

    return errors, warnings


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_integration_plan.py plan.json", file=sys.stderr)
        return 2

    path = Path(argv[1])
    try:
        plan = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"error: cannot read JSON plan: {exc}", file=sys.stderr)
        return 2

    if not isinstance(plan, dict):
        print("error: plan must be a JSON object", file=sys.stderr)
        return 2

    errors, warnings = validate(plan)
    for warning in warnings:
        print(f"warning: {warning}")
    for error in errors:
        print(f"error: {error}")

    if errors:
        print("validation: failed")
        return 1
    print("validation: passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
