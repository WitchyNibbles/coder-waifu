"""Role definition loader."""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path
from typing import Any

import yaml

BUILTINS_DIR = Path(__file__).parent / "builtins"


class Role:
    def __init__(self, path: Path) -> None:
        self.path = path
        with open(path, "r", encoding="utf-8") as fh:
            data: Mapping[str, Any] = yaml.safe_load(fh) or {}
        self.id = str(data.get("id") or path.stem)
        self.title = str(data.get("title", self.id))
        self.focus = str(data.get("focus", ""))
        self.toolsets = list(data.get("toolsets", []))
        self.system_prompt_fragment = str(data.get("system_prompt_fragment", ""))

    def as_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "title": self.title,
            "focus": self.focus,
            "toolsets": self.toolsets,
            "system_prompt_fragment": self.system_prompt_fragment,
            "source": str(self.path),
        }


REQUIRED_ROLE_FIELDS = {"id", "title", "focus", "toolsets"}


def _validate_role(data: Mapping[str, Any], path: Path) -> None:
    missing = REQUIRED_ROLE_FIELDS - data.keys()
    if missing:
        raise ValueError(f"Role {path} missing fields: {missing}")
    if not isinstance(data.get("toolsets"), list):
        raise ValueError(f"Role {path}.toolsets must be a list")


def load_builtins(builtins_dir: Path | None = None) -> dict[str, Role]:
    builtins_dir = builtins_dir or BUILTINS_DIR
    roles: dict[str, Role] = {}
    for yaml_path in sorted(builtins_dir.glob("*.yaml")):
        raw = yaml.safe_load(yaml_path.read_text(encoding="utf-8")) or {}
        _validate_role(raw, yaml_path)
        role = Role(yaml_path)
        roles[role.id] = role
    return roles


def merge_user_roles(
    user_dir: Path | None, base_roles: dict[str, Role]
) -> dict[str, Role]:
    merged = dict(base_roles)
    if not user_dir or not user_dir.exists():
        return merged
    for yaml_path in sorted(user_dir.glob("*.yaml")):
        raw = yaml.safe_load(yaml_path.read_text(encoding="utf-8")) or {}
        _validate_role(raw, yaml_path)
        role = Role(yaml_path)
        merged[role.id] = role
    return merged


def load_roles(user_dir: Path | None = None) -> dict[str, Role]:
    base = load_builtins()
    return merge_user_roles(user_dir, base) if user_dir else base
