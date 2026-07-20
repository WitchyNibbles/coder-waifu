# Coder-Waifu Architecture

Design date: 2026-07-21
Status: draft pending review

## 1. System Boundaries

Coder-waifu is a **host-side CLI wrapper**, not a replacement for Hermes. Its job is to:

- Ask the user clarifying questions in a structured discovery phase
- Synthesize a draft contract from answers + lightweight research
- Spawn and coordinate Hermes agents via `delegate_task`
- Persist checkpoint state to `.coder-waifu/checkpoints/` so runs are resumable
- Render final delivery reports to the user

It does **not**:
- Provide its own LLM inference backend
- Replace Hermes core or run independently of it
- Own or modify user project code outside the spawned agents

## 2. Components and Responsibilities

```
coder_waifu/
├── __init__.py
├── cli.py
├── discovery/
│   ├── __init__.py
│   ├── questions.py         # Selectable-option question engine
│   └── contract_synth.py    # Draft contract synthesis from answers + research
├── roles/
│   ├── __init__.py
│   ├── loader.py            # YAML-based role definition loader
│   └── builtins/            # Bundled role YAMLs
├── orchestrate/
│   ├── __init__.py
│   └── spawner.py           # Spawns 2 agents per role via Hermes delegation
├── checkpoint/
│   ├── __init__.py
│   └── store.py             # JSON checkpoint read/write + resume logic
└── scaffold/
    └── __init__.py          # coder-waifu init template generator
```

### CLI layer (`cli.py`)
- Subcommands: `init`, `run`, `status`, `resume`, `agents`
- All user-facing output routes through a single `ui.py` helper that applies the Coder-Waifu persona
- Route `init <project>` to `scaffold/`, `run <task>` to `discovery/` then `orchestrate/`

### Discovery engine (`discovery/`)
- Presents questions as HermesBot-style selectable options plus freeform Other
- Records both explicit answers and reversible assumptions
- Performs lightweight web research through Hermes web tools if available
- Emits a draft contract string to `.agent/contract.json` and surfaces it to user

### Role system (`roles/`)
- Bundled YAML definitions for 20 built-in roles
- User-supplied YAMLs in `.coder-waifu/roles/` override or extend built-ins
- Each role YAML specifies: system prompt fragment, expertise areas, review criteria, toolset preference
- Role loader validates schema before use

### Orchestration (`orchestrate/spawner.py`)
- For each selected role, dispatches `tasks=[{goal, context}, {goal, context}]`
- Each subagent receives the same underlying task but one is designated “build,” the other “review”
- Parent collects both summaries and produces a unified decision or escalation
- Failure of either subagent does not crash the workflow; it is recorded as an open finding

### Checkpoint store (`checkpoint/store.py`)
- Checkpoints written to `.coder-waifu/checkpoints/<run_id>.json`
- Each checkpoint captures: discovery answers, contract snapshot, in-flight task state, agent outputs
- Resume command reads the latest valid checkpoint and restarts orchestration from the next unverified task
- No compaction hook from Hermes is consumed; instead checkpoints are written at deterministic boundaries

### Scaffold (`scaffold/`)
- `coder-waifu init <name>` creates target dir, `.coder-waifu/variables`, optional README, and initial contract stub

## 3. Interfaces

### Public CLI interface
```
coder-waifu init <project-name>
coder-waifu run <task-description>
coder-waifu resume [run-id]
coder-waifu status
```

### Configuration interface
- `coder-waifu` reads `coder_waifu.config` from project root or `~/.coder-waifu/config.json`
- User can set default model/provider fallback, max concurrency, and checkpoint retention count

### Hermes integration interface
- Primary: `delegate_task` in-process tool call from within Hermes session
- Fallback: `terminal(background=True)` invocation of `hermes chat -q` for long-lived workers when Hermes is not embedded
- No contract-breaking guarantees if Hermes changes `delegate_task` signature in a future version

## 4. Data Flows

```
User
  → coder-waifu run
    → discovery/ (questions + research)
      → draft contract presented to user
        → user approves / Other / adjust
          → contract_synth writes .agent/contract.json
            → orchestrator selects roles
              → spawner dispatches 2x subagents per role
                → subagent summaries collected
                  → spawner produces unified state
                    → checkpoint writes to .coder-waifu/checkpoints/
                      → final report shown to user
```

## 5. State Ownership

- `.agent/*` is owned by the orchestrator session
- `.coder-waifu/` is owned by the target project
- Checkpoints are append-only WAL-style JSON; current checkpoint is a symlink or latest-valid record file
- Individual task outputs are stored inside each checkpoint as versioned blobs

## 6. Failure Modes

| Failure | Behavior |
|---------|----------|
| Subagent crashes or times out | Recorded as finding; parent continues if remaining peers succeed; task marked `failed` only if quorum is unobtainable |
| Context compaction during run | User triggers `/compact`; parent loses in-flight tool sequence. Mitigation: checkpoint at every task boundary and before long delegation calls |
| Hermes unavailable | Fallback to `terminal(background=True)` Hermes CLI spawn; graceful degradation |
| Disk full or checkpoint unreadable | Abort with explicit BLOCKED status and path to last valid checkpoint |
| User aborts mid-delegation | `/stop` can cancel children; checkpoint preserves pre-batch state for resume |

## 7. Security Implications

- No credential storage; coder-waifu uses Helmes auth provider retries
- User-typed freeform and selectable answers are written to `.agent/*` JSON; treat as non-secret but warn if unsanitized shell injection paths are introduced
- No network calls outside Hermes tool surfaces unless explicit research step requests web search
- Scaffold does not execute arbitrary code during creation

## 8. Observability

- Every delegation attempt and result is logged to `.agent/activity-log.jsonl`
- Each task has `attempts` counter; persistent findings accumulate in `.agent/review.json`
- Checkpoint timestamps in `.coder-waifu/checkpoints/` serve as durability audit trail

## 9. Testing Strategy

- **Unit**: question engine, YAML role loader, checkpoint store read/write/resume
- **Integration**: mock `delegate_task` to validate spawner behavior without real Hermes
- **CLI**: click/pytest + CliRunner for init, run --dry-run, resume commands
- **End-to-end**: scripted Hermes smoke test using `hermes chat -q` fallback
- **Failure injection**: corrupt checkpoint, missing role YAML, subagent exception

## 10. Deployment Implications

- Distributed as PyPI source/binary wheel with stdlib + Hermes as install dependencies
- Hermes is listed under `project.optional-dependencies` with a graceful warning if absent at runtime
- No system-level service or daemon
- No required config at install time; defaults to `coder-waifu init` workflow

## 11. Rejected Alternatives

| Alternative | Reason for rejection |
|-------------|----------------------|
| Custom orchestration agent runtime from scratch | Out of scope; Hermes already solves this. Reinventing it expands attack surface and maintenance. |
| Direct model provider calls | Loses Hermes memory, tool use, and existing integration ecosystem |
| Flat module layout | Would complicate role file discovery and future multi-file expansion |
| Embed role system as Hermes skill rather than package | Skills are user-local; this project is intended for `pip install` by any Hermes user, so a packaged CLI is more portable |

## 12. Explicit Trade-offs

| Trade-off | Chosen | Rationale |
|-----------|--------|-----------|
| Hermes `delegate_task` library access | Direct in-session tool call, not standalone library import | Evidence suggests `delegate_task` is primarily an in-session tool; `AIAgent` class in `run_agent.py` exists but stability across versions is unconfirmed. Using the documented tool path minimizes breakage. |
| Durable worker model | Process-local for v1 | Hermes documentation explicitly states delegated work is session-local; cronjobs or terminal background are the recommended durable path. Durable workers are deferred to v2. |
| Context hook strategy | Checkpoint at deterministic boundaries | No documented public compaction hook; boundary-based checkpointing is reliable and auditable. |
| Hermes as dependency | Required at runtime | A pip package that requires Hermes at runtime is a strict dependency. Alternative of optional Hermes lead to poor failure modes; mandatory dependency is clearer. |
