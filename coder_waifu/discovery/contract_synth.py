"""Discovery contract synthesis."""

from __future__ import annotations

import json
from pathlib import Path


def build_draft_contract(
    project: str,
    objective: str,
    answers: dict[str, object],
    assumptions: dict[str, object],
    output_path: Path,
    created_at: str | None = None,
) -> dict[str, object]:
    contract: dict[str, object] = {
        "created_at": created_at,
        "project": project,
        "status": "draft",
        "objective": objective,
        "deliverables": [],
        "constraints": [],
        "non_goals": [],
        "user_approvals_needed": [],
        "acceptance_criteria": [],
        "verification": [],
        "requires_user_approval": [],
        "assumptions": assumptions,
        "discovery_answers": answers,
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(contract, indent=2) + "\n", encoding="utf-8")
    return contract
