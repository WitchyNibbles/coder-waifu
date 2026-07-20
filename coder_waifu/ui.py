"""User-facing output helper. Cute persona is confined to this module."""

from __future__ import annotations


class UI:
    def info(self, message: str) -> str:
        out = f"? {message}"
        print(out)
        return out

    def ask(self, message: str) -> str:
        out = f"?? {message}"
        print(out)
        return out

    def success(self, message: str) -> str:
        out = f"? {message}"
        print(out)
        return out

    def warn(self, message: str) -> str:
        out = f"⚠ {message}"
        print(out)
        return out

    def persona_ok(self) -> str:
        return "nya~"


ui = UI()
