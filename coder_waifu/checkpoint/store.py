"""Checkpoint store for resumable runs."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class CheckpointStore:
    def __init__(self, checkpoints_dir: Path) -> None:
        self.checkpoints_dir = checkpoints_dir
        self.checkpoints_dir.mkdir(parents=True, exist_ok=True)

    def write(self, run_id: str, state: dict[str, Any]) -> Path:
        path = self.checkpoints_dir / f"{run_id}.json"
        path.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
        return path

    def read(self, run_id: str) -> dict[str, Any]:
        path = self.checkpoints_dir / f"{run_id}.json"
        if not path.exists():
            raise FileNotFoundError(path)
        data: dict[str, Any] = json.loads(path.read_text(encoding="utf-8"))
        return data

    def latest(self) -> tuple[str, dict[str, Any]]:
        candidates = sorted(self.checkpoints_dir.glob("*.json"))
        if not candidates:
            raise FileNotFoundError("No checkpoints found")
        path = candidates[-1]
        return path.stem, json.loads(path.read_text(encoding="utf-8"))
