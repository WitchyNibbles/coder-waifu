<div align="center">
  <img src="docs/waifu-logo.png" alt="coder-waifu waifu logo" width="180">
  <br>
  <pre>
 ██████╗ ██╗ ██████╗ ███████╗██████╗  ██████╗ ████████╗██╗   ██╗███████╗
██╔════╝██║██╔═══██╗██╔════╝██╔══██╗██╔════╝ ╚══██╔══╝██║   ██║██╔════╝
██║     ██║██║   ██║███████╗██████╔╝██║         ██║   ██║   ██║█████╗  
██║     ██║██║   ██║╚════██║██╔══██╗██║         ██║   ██║   ██║██╔══╝  
███████╗██║╚██████╔╝███████║██║  ██║╚██████╗    ██║   ╚██████╔╝███████╗
╚══════╝╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝     ╚═╝    ╚═════╝ ╚══════╝
  </pre>
</div>

> *Autonomous engineering orchestrator for Hermes Agent — now with 20 built-in role pairs and mandatory discovery/intent validation before any work spawns.*

<div align="center">

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![pip](https://img.shields.io/badge/pip-installable-brightgreen)

</div>

## ? What even is this?

`coder-waifu` is a cutie-pie CLI that takes a vague engineering task, asks you clarifying questions with selectable options + freeform input so you never have to write essays, drafts a contract for your approval, and then **spawns adversarial role-based agent pairs** inside Hermes to actually execute and review the work.

Each of the 20 built-in roles gets **2 collaborating agents** — one builds, one nitpicks — until the output is actually production-grade. No more rubber-stamped garbage. We checkpoint automatically, so long-running sweeps are resumable across sessions.

## Install

```bash
pip install coder-waifu
```

## ? CLI Commands

```bash
coder-waifu --help
coder-waifu init my-project
coder-waifu run "add a FastAPI auth service"
coder-waifu status
coder-waifu resume
```

## 🔍 Discovery: "Say Less, Code More"

`coder-waifu run` is *mandatory* about one thing: **understanding what you actually want** before spawning agents.

It asks targeted clarifying questions with:
- **Curated selectable options** so you can tap-tap-tap answers fast
- **Always-available freeform "Other"** because options can’t predict everything
- **No essay-mode forced writeups** unless you choose to

After discovery, a draft contract is written to `.agent/contract.json` and shown to you for approval. **Zero agents are spawned until you say yes.** No surprises, no rogue automation.

## ? Roles (20 Built-in + Extensible)

Each role gets **2 agents**: implement + adversarial review.

| Role | Focus |
|---|---|
| `cto` | Technical vision, trade-off analysis, risk assessment |
| `product_manager` | Requirements, user stories, acceptance criteria, scope |
| `software_architect` | System design, interfaces, failure modes, observability |
| `backend_engineer` | API design, database schemas, business logic, auth |
| `frontend_engineer` | UI components, routing, state management, accessibility |
| `frontend_designer` | Visual design, user flows, design systems, accessibility audits |
| `fullstack_engineer` | End-to-end features, API + UI integration |
| `devops_engineer` | CI/CD, infrastructure as code, deployment pipelines |
| `sre` | Reliability, SLAs, error budgets, incident response, observability |
| `security_engineer` | Threat modeling, dependency audits, secrets management |
| `qa_engineer` | Test strategy, test automation, edge cases, quality gates |
| `data_engineer` | ETL, schema design, data quality, analytics infrastructure |
| `dba` | Schema design, query optimization, migrations, backup/restore |
| `it_architect` | Network topology, identity management, enterprise policies |
| `it_admin` | System provisioning, access control, monitoring, incident triage |
| `mobile_engineer` | Mobile UI, platform APIs, app distribution, offline behavior |
| `ml_engineer` | Training pipelines, inference serving, experiment tracking |
| `technical_writer` | API docs, runbooks, architecture diagrams |
| `performance_engineer` | Load testing, profiling, latency optimization |
| `accessibility_specialist` | WCAG compliance, keyboard navigation, ARIA |

Custom roles? Drop YAML files into `.coder-waifu/roles/` and they’ll be merged over built-ins automatically.

## 🧲 How it works

```
coder-waifu run "add a FastAPI auth service"
    ↓
Discovery phase (questions + freeform)
    ↓
Draft contract written to .agent/contract.json
    ↓ [YOU APPROVE]
Orchestration: 2 subagents per role × selected roles
    ↓
Adversarial review loop until production-grade
    ↓
Checkpoint saved to .coder-waifu/checkpoints/
```

## Context & Checkpoints

Long runs? No problem. `coder-waifu` checkpoints state at task boundaries and before long agent work. Drop out mid-run, run `coder-waifu resume`, and pick up right where you left off.

- Checkpoints: `.coder-waifu/checkpoints/`
- Contract: `.agent/contract.json`
- State: `.agent/state.json`

## ?? Mascot / Logo

Sixteen-oh-six waifu, encircled by a hextech frame. Chopped blue bangs, one bright magenta streak, goggles framing the face, holding the team hostage with a keyboard-fragment device. It’s the engineer mode you shouldn’t activate, but absolutely would.

Design references: Arcane/Wild Rift palette — electric blues, neon magentas, hextech glow.

<div align="center">
  <img src="docs/waifu-logo.png" alt="coder-waifu waifu logo" width="160">
</div>

## License

MIT — do whatever, just don’t be evil.

---

Made with ✨ and questionable amounts of caffeine.
