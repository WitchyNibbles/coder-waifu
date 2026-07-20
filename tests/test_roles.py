"""Tests for coder_waifu role loader."""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from coder_waifu.roles.loader import (
    Role,
    _validate_role,
    load_builtins,
    merge_user_roles,
)


def test_load_builtins_returns_twenty_roles() -> None:
    roles = load_builtins()
    assert len(roles) == 20


def test_builtin_role_keys() -> None:
    roles = load_builtins()
    for role in roles.values():
        assert role.id
        assert role.title
        assert role.focus
        assert isinstance(role.toolsets, list)


def test_merge_user_roles_overrides_builtin(tmp_path: Path) -> None:
    user_dir = tmp_path / "roles"
    user_dir.mkdir()
    payload = yaml.safe_dump(
        {
            "id": "cto",
            "title": "Chief Tea Officer",
            "focus": "tea quality",
            "toolsets": ["terminal"],
        }
    )
    (user_dir / "cto.yaml").write_text(payload, encoding="utf-8")
    base = load_builtins()
    merged = merge_user_roles(user_dir, base)
    assert merged["cto"].title == "Chief Tea Officer"
    assert merged["cto"].toolsets == ["terminal"]


def test_validate_role_rejects_missing_fields() -> None:
    with pytest.raises(ValueError):
        _validate_role({"id": "x"}, Path("x.yaml"))


def test_as_dict_contains_source() -> None:
    role = Role(Path("coder_waifu/roles/builtins/cto.yaml"))
    data = role.as_dict()
    assert data["id"] == "cto"
    assert "builtins" in data["source"]
