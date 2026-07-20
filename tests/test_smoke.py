"""Smoke tests for coder-waifu package."""

from coder_waifu import __version__
from coder_waifu.ui import ui


def test_version_defined():
    assert __version__ == "0.1.0"


def test_ui_outputs():
    assert ui.success("ok").startswith("?")
    assert ui.ask("question").startswith("??")
    assert ui.info("note").startswith("?")
