"""Tests for coder-waifu scaffold command."""

from __future__ import annotations

from pathlib import Path

import pytest

from coder_waifu.scaffold import scaffold_project


def test_scaffold_creates_expected_files(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    target = tmp_path / "my-project"
    monkeypatch.chdir(tmp_path)
    code = scaffold_project("my-project")
    assert code == 0
    assert target.exists()
    assert (target / "README.md").exists()
    assert (target / ".coder-waifu" / "variables").exists()
    assert (target / ".agent" / "contract.json").exists()


def test_scaffold_refuses_overwrite(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    (tmp_path / "existing").mkdir()
    monkeypatch.chdir(tmp_path)
    code = scaffold_project("existing")
    assert code != 0
