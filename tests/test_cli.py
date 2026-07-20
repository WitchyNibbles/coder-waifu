"""Tests for coder_waifu CLI."""

from __future__ import annotations

import pytest

from coder_waifu.cli import main


def test_help_system_exit_zero() -> None:
    with pytest.raises(SystemExit) as exc:
        main(["--help"])
    assert exc.value.code == 0


def test_version_exit_zero() -> None:
    assert main(["--version"]) == 0


def test_status_exit_zero() -> None:
    assert main(["status"]) == 0


def test_run_exit_zero() -> None:
    assert main(["run", "do nothing"]) == 0


def test_run_no_task_exit_zero() -> None:
    assert main(["run"]) == 0


def test_resume_exit_zero() -> None:
    assert main(["resume"]) == 0


def test_init_exits_nonzero_on_existing(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("coder_waifu.scaffold.scaffold_project", lambda name: 1)
    assert main(["init", "existing"]) == 1
