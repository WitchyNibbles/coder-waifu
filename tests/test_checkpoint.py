"""Tests for checkpoint store."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from coder_waifu.checkpoint.store import CheckpointStore


def test_write_and_read_roundtrip(tmp_path: Path) -> None:
    store = CheckpointStore(tmp_path / "ckpts")
    store.write("run-1", {"status": "running", "step": 1})
    run_id, state = store.latest()
    assert run_id == "run-1"
    assert state["status"] == "running"


def test_latest_raises_when_empty(tmp_path: Path) -> None:
    store = CheckpointStore(tmp_path / "ckpts")
    with pytest.raises(FileNotFoundError):
        store.latest()


def test_corrupt_json_raises_on_read(tmp_path: Path) -> None:
    store = CheckpointStore(tmp_path / "ckpts")
    path = tmp_path / "ckpts" / "run-bad.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("{not json", encoding="utf-8")
    with pytest.raises(json.JSONDecodeError):
        store.read("run-bad")


def test_read_by_id(tmp_path: Path) -> None:
    store = CheckpointStore(tmp_path / "ckpts")
    store.write("run-2", {"status": "complete"})
    assert store.read("run-2")["status"] == "complete"
