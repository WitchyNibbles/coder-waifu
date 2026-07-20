"""Orchestration package."""

from coder_waifu.orchestrate.spawner import (
    RoleRunResult,
    run_role_pair,
    select_roles_for_task,
)

__all__ = ["RoleRunResult", "run_role_pair", "select_roles_for_task"]
