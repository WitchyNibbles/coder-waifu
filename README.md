# coder-waifu

Autonomous engineering orchestrator for [Hermes Agent](https://github.com/NousResearch/hermes-agent).

`coder-waifu` takes a task description, asks clarifying questions with selectable options plus freeform input, performs lightweight domain research, drafts a contract for your approval, and then spawns adversarial role-based agent pairs inside Hermes to execute and review the work. It checkpoints state automatically so long-running runs are resumable.

## Install

```bash
pip install coder-waifu
```

## Usage

```bash
coder-waifu --help
coder-waifu init my-project
coder-waifu run "add a FastAPI auth service"
coder-waifu status
coder-waifu resume
```

## Discovery phase

`coder-waifu run` asks targeted clarifying questions before spawning agents. Questions present curated selectable options and always include an **Other** freeform choice, so you can answer quickly or describe your intent exactly.

After discovery, a draft contract is written to `.agent/contract.json` and shown to you for approval. No agents are spawned until you approve.

## Roles

Each role spawns **2 collaborating agents**: one implementation pass and one adversarial review.

Built-in roles:

- `cto` — technical vision, trade-off analysis, risk assessment
- `product_manager` — requirements, user stories, scope definition
- `software_architect` — system design, interfaces, failure modes, observability
- `backend_engineer` — API design, database schemas, business logic, auth
- `frontend_engineer` — UI components, routing, state management, accessibility
- `frontend_designer` — visual design, user flows, design systems, accessibility audits
- `fullstack_engineer` — end-to-end features, API + UI integration
- `devops_engineer` — CI/CD, infrastructure as code, deployment pipelines
- `sre` — reliability, SLAs, error budgets, incident response, observability
- `security_engineer` — threat modeling, dependency audits, secrets management
- `qa_engineer` — test strategy, test automation, edge cases, quality gates
- `data_engineer` — ETL, schema design, data quality, analytics infrastructure
- `dba` — schema design, query optimization, migrations, backup/restore
- `it_architect` — network topology, identity management, enterprise policies
- `it_admin` — system provisioning, access control, monitoring, incident triage
- `mobile_engineer` — mobile UI, platform APIs, app distribution, offline behavior
- `ml_engineer` — training pipelines, inference serving, experiment tracking
- `technical_writer` — API docs, runbooks, architecture diagrams
- `performance_engineer` — load testing, profiling, latency optimization
- `accessibility_specialist` — WCAG compliance, keyboard navigation, ARIA

## Context and checkpoints

`coder-waifu` checkpoints run state to `.coder-waifu/checkpoints/` at task boundaries and before long agent work. Use `coder-waifu resume` to restart from the last checkpoint without losing progress.

## License

MIT
