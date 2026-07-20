#!/usr/bin/env bash
set -euo pipefail

TMPDIR="$(mktemp -d)"
trap 'rm -rf "$TMPDIR"' EXIT

python3 -m venv "$TMPDIR/.venv"
"$TMPDIR/.venv/bin/python" -m pip install -e "$OLDPWD[dev,roles]" -q
PATH="$TMPDIR/.venv/bin:$PATH"

coder-waifu --help >/dev/null
coder-waifu init "$TMPDIR/project" >/dev/null
test -d "$TMPDIR/project/.coder-waifu"
test -f "$TMPDIR/project/.agent/contract.json"
test -f "$TMPDIR/project/README.md"

python -m pytest -q --tb=short
ruff check .

echo "SMOKE_TEST_PASS"
