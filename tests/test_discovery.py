"""Tests for discovery question engine."""

from __future__ import annotations

from coder_waifu.discovery.questions import Question, QuestionEngine


def test_question_requires_options_and_freeform() -> None:
    q = Question(key="style", prompt="Preferred code style?", options=["PEP 8", "Google", "Black"])
    assert "Other" in q.options
    assert q.freeform is True


def test_render_returns_selectable_plus_other() -> None:
    engine = QuestionEngine([])
    q = Question("lang", "Language?", ["Python", "TypeScript"])
    rendered = engine.render_question(q)
    assert "Python" in rendered
    assert "TypeScript" in rendered
    assert "Other" in rendered


def test_capture_answer_accepts_freeform() -> None:
    engine = QuestionEngine([])
    q = Question("lang", "Language?", ["Python", "TypeScript"])
    answer = engine.capture_answer(q, "Rust")
    assert answer["value"] == "Rust"
    assert answer["source"] == "freeform"
