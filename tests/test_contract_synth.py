"""Tests for discovery contract synthesis."""

from __future__ import annotations

from pathlib import Path

from coder_waifu.discovery.contract_synth import build_draft_contract


def test_build_draft_contract_writes_json(tmp_path: Path) -> None:
    answers: dict[str, object] = {"primary_objective": "Build a CLI"}
    contract = build_draft_contract(
        project="demo-project",
        objective="Build a CLI",
        answers=answers,
        assumptions={},
        output_path=tmp_path / ".agent" / "contract.json",
    )
    assert contract["project"] == "demo-project"
    assert (tmp_path / ".agent" / "contract.json").exists()
