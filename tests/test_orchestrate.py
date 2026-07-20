"""Tests for orchestrate spawner."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

from coder_waifu.orchestrate.spawner import select_roles_for_task
from coder_waifu.roles.loader import Role


@pytest.fixture(autouse=True)
def _block_hermes_import(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setitem(sys.modules, "hermes_tools", None)


class FakeRole(Role):
    def __init__(self) -> None:
        self.path = Path(".")


def test_select_roles_for_task_frontend() -> None:
    results = select_roles_for_task("Build a React UI")
    assert "frontend_engineer" in results
    assert "frontend_designer" in results


def test_select_roles_for_task_backend() -> None:
    results = select_roles_for_task("Design the API and database schema")
    assert "backend_engineer" in results


def test_select_roles_for_task_default() -> None:
    results = select_roles_for_task("Write a blog post")
    assert results == ["backend_engineer", "frontend_engineer"]


def test_select_roles_dedupes() -> None:
    results = select_roles_for_task("frontend + UI + css React")
    assert len(results) == len(dict.fromkeys(results))
