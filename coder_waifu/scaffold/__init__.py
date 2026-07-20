"""Scaffold coder-waifu project layout."""

from __future__ import annotations

from pathlib import Path


def scaffold_project(name: str) -> int:
    target = Path(name).resolve()
    if target.exists():
        print(f"Refusing to overwrite existing path: {target}")
        return 1

    target.mkdir(parents=True)
    (target / ".coder-waifu" / "variables").mkdir(parents=True)
    (target / ".agent").mkdir(parents=True)

    readme = target / "README.md"
    readme.write_text(
        "\n".join(
            [
                f"# {name}",
                "",
                "Managed by coder-waifu.",
                "",
                "## Usage",
                "",
                "```",
                "coder-waifu run <task>",
                "```",
                "",
            ]
        )
        + "\n"
    )

    contract = target / ".agent" / "contract.json"
    contract.write_text('{"status":"draft","project":"' + name + '"}\n')

    print(f"Scaffolded {target}")
    return 0
