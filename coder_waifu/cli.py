"""CLI entry point for coder-waifu."""

from __future__ import annotations

import argparse


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="coder-waifu",
        description="Autonomous engineering orchestrator for Hermes Agent.",
    )
    parser.add_argument("--version", action="store_true", help="Show version and exit")

    subparsers = parser.add_subparsers(dest="command")

    init_parser = subparsers.add_parser("init", help="Scaffold a new coder-waifu project")
    init_parser.add_argument("name", help="Project name / directory")

    run_parser = subparsers.add_parser("run", help="Run a task through discovery + orchestration")
    run_parser.add_argument("task", nargs="?", default="", help="Task description")

    subparsers.add_parser("status", help="Show current run state")
    subparsers.add_parser("resume", help="Resume from last checkpoint")

    args = parser.parse_args(argv)

    if args.version:
        from coder_waifu import __version__

        print(f"coder-waifu {__version__}")
        return 0

    if args.command == "init":
        from coder_waifu.scaffold import scaffold_project

        return scaffold_project(args.name)

    if args.command == "run":
        from coder_waifu.ui import ui

        ui.info("Coder-Waifu discovery/orchestration is not yet wired in this draft build, nya~")
        return 0

    if args.command == "status":
        from coder_waifu.ui import ui

        ui.info("No active run detected in this workspace yet.")
        return 0

    if args.command == "resume":
        from coder_waifu.ui import ui

        ui.info("Resume flow is not implemented yet.")
        return 0

    parser.print_help()
    return 0
