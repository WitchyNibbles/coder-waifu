"""Orchestration spawner producing adversarial role-based agent pairs."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from coder_waifu.roles.loader import Role


@dataclass(frozen=True)
class RoleRunResult:
    role_id: str
    build_summary: str | None
    review_summary: str | None
    findings: list[str] = field(default_factory=list)
    status: str = "unknown"


def _delegate_task(*args: Any, **kwargs: Any) -> Any:
    import hermes_tools  # type: ignore

    return hermes_tools.delegate_task(*args, **kwargs)


def _build_goal(role: Role, task: str) -> str:
    return (
        f"[{role.title}] Implementation pass for task: {task}\n"
        f"Focus areas: {role.focus}\n"
        "Produce a build summary including changes made, files modified, and verification evidence."
    )


def _review_goal(role: Role, task: str) -> str:
    return (
        f"[{role.title}] Adversarial review pass for task: {task}\n"
        f"Focus areas: {role.focus}\n"
        "Review the build summary and identify correctness gaps, security issues, missing edge cases, and required follow-up."
    )


def _build_context(role: Role, task: str, contract_path: str) -> str:
    return (
        f"Task: {task}\nRole: {role.id}\nFocus: {role.focus}\n"
        f"System prompt guidance: {role.system_prompt_fragment}\n"
        f"Context file: {contract_path}"
    )


def run_role_pair(
    role: Role,
    task: str,
    *,
    contract_path: str = ".agent/contract.json",
    max_iterations: int = 50,
) -> RoleRunResult:
    build_context = _build_context(role, task, contract_path)
    review_context = build_context + "\nReview the build output for gaps and failures."

    try:
        results = _delegate_task(
            tasks=[
                {
                    "goal": _build_goal(role, task),
                    "context": build_context,
                    "max_iterations": max_iterations,
                },
                {
                    "goal": _review_goal(role, task),
                    "context": review_context,
                    "max_iterations": max_iterations,
                },
            ]
        )
    except Exception as exc:  # pragma: no cover - runtime Hermes failure
        return RoleRunResult(
            role_id=role.id,
            build_summary=None,
            review_summary=None,
            findings=[f"delegation failed: {exc}"],
            status="failure",
        )

    summaries = results if isinstance(results, (list, tuple)) else []
    build_summary = summaries[0] if len(summaries) > 0 else None
    review_summary = summaries[1] if len(summaries) > 1 else None
    findings = []
    if review_summary and "issue" in review_summary.lower():
        findings.append("review reported potential issues")
    status = "complete" if build_summary and review_summary else "partial"
    return RoleRunResult(
        role_id=role.id,
        build_summary=build_summary,
        review_summary=review_summary,
        findings=findings,
        status=status,
    )


def select_roles_for_task(task: str) -> list[str]:
    lowered = task.lower()
    selected: list[str] = []
    if any(key in lowered for key in ["frontend", "ui", "ux", "css", "react", "vue"]):
        selected.append("frontend_engineer")
        selected.append("frontend_designer")
    if any(key in lowered for key in ["backend", "api", "database", "db", "auth"]):
        selected.append("backend_engineer")
    if any(key in lowered for key in ["security", "vulnerability", "secret"]):
        selected.append("security_engineer")
    if any(key in lowered for key in ["deploy", "infrastructure", "ci/cd", "k8s", "docker"]):
        selected.append("devops_engineer")
    if any(key in lowered for key in ["test", "qa", "coverage"]):
        selected.append("qa_engineer")
    if not selected:
        selected = ["backend_engineer", "frontend_engineer"]
    deduped: list[str] = []
    seen: set[str] = set()
    for role_id in selected:
        if role_id not in seen:
            deduped.append(role_id)
            seen.add(role_id)
    return deduped
