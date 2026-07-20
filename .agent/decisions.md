# Coder-Waifu Decisions

Generated: 2026-07-21

## Decisions

### D01: Use Hermes delegate_task as the primary orchestration primitive
Accepted. Evidence: official Hermes docs confirm `delegate_task` supports single and parallel batch spawns with configurable concurrency (default 3), background mode, and model/tool inheritance. Risk: subagent durability tied to parent session. Mitigated by checkpoint-based recovery and documented v2 durable-worker follow-up.

### D02: Do not use Hermes library import path for orchestration
Accepted. Evidence: Hermes docs show `delegate_task` as the in-session tool pattern; a `python-library.md` page exists suggesting `AIAgent` import, but extraction quality was low and stability across versions is unconfirmed. Decision: route through Hermes tool call surface where possible; use `terminal(background=True)` fallback for durability-critical cases rather than direct `AIAgent` import.

### D03: Accept process-local delegation limitation for v1
Accepted. Official Hermes docs explicitly state: “Not durable — top-level delegation runs in the background and posts its result back later, but it remains tied to the owning session and Hermes process.” Deferring durable workers to v2 keeps v1 honest without overpromising.

### D04: No compaction hook; use deterministic boundary checkpointing
Accepted. Extracted docs do not document a public Python API for `/compact` or auto-compaction events. Hermes hooks exist, but the lifecycle event list extracted does not include a compaction-specific hook in the rendered head+tail. Avoids a fragile coupling; checkpoint at task boundaries, before long delegations, and on explicit user /compact command detection.

### D05: Role definitions as YAML files
Accepted. Keeps role definitions editable without touching Python code. YAML is readable, versionable, and easily validated. Built-ins shipped under `coder_waifu/roles/builtins/`; user overrides in `.coder-waifu/roles/`.

### D06: Selectable options + freeform Other in discovery questions
Accepted. User explicitly requested this. The question engine always presents curated options first and an explicit Other freeform choice last, with both captured into the contract.

### D07: Hermes required at runtime
Accepted. The package targets Hermes users; optional Hermes would lead to weak failure modes. Documentation should clarify this clearly during `pip install` and `coder-waifu --help`.

### D08: Scaffold command produces literal file tree, no template engine
Accepted. Avoids pulling in Jinja2 or similar. Generate starter files with plain `write_text` calls for KISS compliance.

## Rejected findings from contrarian evidence
- Found none from the contrary-source sweep; primary evidence matched official docs shape. Counter-evidence reviews are still required after implementation completes.
