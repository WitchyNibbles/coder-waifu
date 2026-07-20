"""Discovery question engine with selectable options and freeform Other."""

from __future__ import annotations

from typing import Any


class Question:
    def __init__(
        self,
        key: str,
        prompt: str,
        options: list[str] | None = None,
        freeform: bool = True,
    ) -> None:
        self.key = key
        self.prompt = prompt
        self.options = list(options or [])
        self.freeform = freeform
        if freeform and "Other" not in self.options:
            self.options.append("Other")

    def render(self) -> str:
        lines = [self.prompt]
        for index, option in enumerate(self.options, start=1):
            lines.append(f"  {index}) {option}")
        if self.freeform:
            lines.append("  Or type a custom answer.")
        return "\n".join(lines)

    def capture(self, raw: str) -> dict[str, Any]:
        selected = raw if self.freeform and raw in self.options else None
        return {
            "key": self.key,
            "value": raw,
            "selected_option": selected,
            "source": "option" if selected is not None else "freeform",
        }


class QuestionEngine:
    def __init__(self, questions: list[Question]) -> None:
        self.questions = questions

    def render_question(self, question: Question) -> str:
        return question.render()

    def capture_answer(self, question: Question, raw: str) -> dict[str, Any]:
        return question.capture(raw)
