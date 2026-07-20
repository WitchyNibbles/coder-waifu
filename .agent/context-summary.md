# Coder-Waifu Architecture

## Current objective
Design a pip-installable Python package that acts as a Hermes-native autonomous engineering orchestrator.

## Approved constraints
- Python >= 3.10
- Package layout: `coder_waifu/` package
- MIT license
- Includes `coder-waifu init` scaffold command
- Discovery questions use selectable options with freeform Other always available
- Coder-Waifu persona only in user-facing CLI output
- Hermes `delegate_task` is the intended primary delegation primitive; fallback considerations documented
- Context checkpointing must be autonomous and resumable

## Important decisions
- Package layout approved as package, not flat module
- MIT license approved
- Scaffold command approved
- Selectable-option question UI is mandatory for discovery phase
- Process-local delegation is an accepted limitation for v1

## Verified completed tasks
- Contract drafted and approved in `.agent/contract.json`
- Primary and contrary research completed and persisted to `.agent/evidence.json`
- Architecture design in progress

## Current task
Write `.agent/architecture.md` and `.agent/decisions.md`, then generate `.agent/plan.json`

## Changed files
- `.agent/contract.json`
- `.agent/state.json`
- `.agent/evidence.json`

## Open reviewer findings
- None yet; specification/quality review pending after implementation begins

## Failed checks
- None

## Blockers
- Subagent delegation via `delegate_task` is currently unavailable in this runtime due to missing OpenRouter API key; architecture work proceeding directly in main session

## Next exact action
Write `.agent/architecture.md` and `.agent/decisions.md`, then create `.agent/plan.json` with dependency-aware task graph for implementation.
