<div align="center">
  <img src="docs/waifu-logo-jinx.png" alt="Coder-Waifu mascot logo" width="160">

  <br>

  <pre>
 ██████╗ ██████╗ ██████╗ ███████╗██████╗       ██╗    ██╗ █████╗ ██╗███████╗██╗   ██╗
██╔════╝ ██╔═══██╗██╔══██╗██╔════╝██╔══██╗      ██║    ██║██╔══██╗██║██╔════╝██║   ██║
██║      ██║   ██║██║  ██║█████╗  ██████╔╝█████╗██║ █╗ ██║███████║██║█████╗  ██║   ██║
██║      ██║   ██║██║  ██║██╔══╝  ██╔══██╗╚════╝██║███╗██║██╔══██║██║██╔══╝  ██║   ██║
╚██████╗ ╚██████╔╝██████╔╝███████╗██║  ██║      ╚███╔███╔╝██║  ██║██║██║     ╚██████╔╝
 ╚═════╝  ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝       ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝╚═╝      ╚═════╝
  </pre>

  <p><strong>Autonomous engineering orchestration for Hermes Agent</strong></p>

  <p>
    Twenty built-in engineering roles, mandatory discovery, contract approval,
    adversarial reviews, and resumable checkpoints. ✨
  </p>

  <p><em>Less vague prompting. More production-grade code. (｡•̀ᴗ-)✧</em></p>
</div>

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![pip](https://img.shields.io/badge/pip-installable-brightgreen?style=flat-square&logo=pypi&logoColor=white)

</div>

---

## 🌸 What is Coder-Waifu?

`coder-waifu` is an adorable-but-suspiciously-competent CLI that turns vague engineering requests into structured, reviewable work.

Give it a task such as:

```bash
coder-waifu run "add a FastAPI auth service"
```

Before unleashing an army of agents upon your innocent repository, Coder-Waifu:

1. Asks focused clarification questions.
2. Lets you choose from predefined answers or write your own.
3. Generates an explicit engineering contract.
4. Waits for your approval.
5. Spawns role-based agent pairs to implement and review the work.
6. Saves checkpoints so long-running tasks can be resumed later.

No essay-writing ritual. No mystery requirements. No rogue agent deciding your authentication service clearly needed blockchain. `(¬_¬")`

Each selected role receives **two collaborating agents**:

- 🛠️ **Implementation agent** — builds the solution.
- 🔍 **Adversarial reviewer** — searches for bugs, weak assumptions, missing tests, and other tiny disasters.

The result is reviewed repeatedly until it satisfies the approved contract and quality requirements.

---

## 📦 Installation

Install Coder-Waifu from PyPI:

```bash
pip install coder-waifu
```

Check that the command is available:

```bash
coder-waifu --help
```

> **Requirement:** Python 3.10 or newer.  
> Ancient Python versions have suffered enough. Please let them rest. `(´-ω-`)`

---

## 🎀 CLI Commands

```bash
# Show all available commands
coder-waifu --help

# Initialize Coder-Waifu inside a project
coder-waifu init my-project

# Start a new engineering task
coder-waifu run "add a FastAPI auth service"

# Inspect the current orchestration state
coder-waifu status

# Continue the latest interrupted run
coder-waifu resume
```

---

## 🔍 Discovery — “Say Less, Code More”

Coder-Waifu refuses to start implementation until it has a reasonable understanding of what you actually want.

This discovery phase is mandatory because:

> “Just build the feature” is not a specification, no matter how confidently someone typed it. `(￣▽￣*)ゞ`

During discovery, Coder-Waifu provides:

- 🎯 **Targeted questions** based on the task.
- 🧁 **Curated selectable options** for quick answers.
- ✍️ **An always-available `Other` option** for freeform input.
- 🚫 **No mandatory essay mode** unless additional detail is genuinely required.
- 📋 **A generated contract** containing the final scope and expectations.

The draft contract is written to:

```text
.agent/contract.json
```

Coder-Waifu then presents it for approval.

> **No agents are spawned until you approve the contract.**  
> Tiny digital engineers must obtain permission before touching the machinery. `(•̀ᴗ•́)و`

This protects the project from:

- Incorrect assumptions.
- Accidental scope expansion.
- Missing acceptance criteria.
- Unrequested architectural rewrites.
- Agents becoming creatively ambitious at your expense.

---

## 🧠 Built-in Roles

Coder-Waifu includes **20 built-in engineering roles**.

Each selected role receives:

```text
1 implementation agent + 1 adversarial review agent
```

Because one agent confidently making a mistake is merely automation. Two agents arguing about it is engineering. ✨

| Role | Focus |
|---|---|
| `cto` | Technical vision, trade-off analysis, strategic risks |
| `product_manager` | Requirements, user stories, acceptance criteria, scope |
| `software_architect` | System design, interfaces, failure modes, observability |
| `backend_engineer` | APIs, database schemas, business logic, authentication |
| `frontend_engineer` | Components, routing, state management, accessibility |
| `frontend_designer` | Visual systems, user flows, design consistency, accessibility audits |
| `fullstack_engineer` | End-to-end features and frontend/backend integration |
| `devops_engineer` | CI/CD, infrastructure as code, deployment pipelines |
| `sre` | Reliability, SLAs, error budgets, incidents, observability |
| `security_engineer` | Threat modeling, dependency audits, secrets management |
| `qa_engineer` | Test strategy, automation, edge cases, quality gates |
| `data_engineer` | ETL, schemas, data quality, analytics infrastructure |
| `dba` | Query optimization, migrations, backups, database reliability |
| `it_architect` | Network topology, identity management, enterprise policies |
| `it_admin` | Provisioning, access control, monitoring, incident triage |
| `mobile_engineer` | Mobile UI, platform APIs, distribution, offline behavior |
| `ml_engineer` | Training pipelines, inference, model serving, experiment tracking |
| `technical_writer` | API documentation, runbooks, architecture diagrams |
| `performance_engineer` | Load testing, profiling, latency and resource optimization |
| `accessibility_specialist` | WCAG compliance, keyboard navigation, ARIA |

---

## 🧩 Custom Roles

Need a role that is not included by default?

Add a YAML definition inside:

```text
.coder-waifu/roles/
```

Custom role files are automatically loaded and merged over the built-in definitions.

```text
.coder-waifu/
└── roles/
    ├── django_archaeologist.yaml
    ├── legacy_javascript_exorcist.yaml
    └── postgres_deadlock_whisperer.yaml
```

You may finally represent the highly specialized professionals demanded by modern software development. `(╥﹏╥)`

---

## 🧲 How It Works

```text
coder-waifu run "add a FastAPI auth service"
    │
    ▼
🌸 Discovery phase
   Targeted questions + selectable options + freeform input
    │
    ▼
📋 Draft contract
   Written to .agent/contract.json
    │
    ▼
✅ User approval
   No approval = no agents
    │
    ▼
🤖 Role orchestration
   Two subagents per selected role
    │
    ▼
⚔️ Adversarial review loop
   Implementation is challenged, corrected, and reviewed
    │
    ▼
💾 Checkpoint
   Progress saved to .coder-waifu/checkpoints/
```

The orchestration process continues until the produced work satisfies the approved contract or requires further user input.

---

## 💾 Context and Checkpoints

Large engineering tasks can take time. Coder-Waifu saves its state at task boundaries and before long-running agent operations.

When a run is interrupted, resume it with:

```bash
coder-waifu resume
```

Coder-Waifu stores its working data in the following locations:

| Path | Purpose |
|---|---|
| `.coder-waifu/checkpoints/` | Resumable execution checkpoints |
| `.agent/contract.json` | Approved task scope and acceptance criteria |
| `.agent/state.json` | Current orchestration state |

This allows you to close the terminal, survive a laptop reboot, reconsider your life choices, and continue later. `(づ｡◕‿‿◕｡)づ`

---

## 🛡️ Approval and Safety Model

Coder-Waifu follows a contract-first execution model:

- Discovery happens before implementation.
- Scope is written explicitly.
- The user reviews the contract.
- Agents only start after approval.
- Review agents challenge implementation decisions.
- Checkpoints preserve progress and state.

This does not guarantee perfect output—software remains software, unfortunately—but it makes assumptions visible and failures easier to detect.

---

## 🌺 Mascot and Logo

<div align="center">
  <img src="docs/waifu-logo-jinx.png" alt="Coder-Waifu mascot logo" width="180">

  <p>
    <em>Your cheerful engineering orchestrator, moments before finding seventeen missing edge cases. (◕‿◕✿)</em>
  </p>
</div>

The Coder-Waifu mascot is a circular chibi engineer badge featuring:

- 💙 Choppy electric-blue hair.
- 💗 A bright magenta streak.
- 🥽 Hextech-inspired goggles.
- 🌸 Soft sakura petals.
- ⚡ Neon technical energy.
- ✨ The unmistakable expression of someone about to reject your pull request.

The visual palette is inspired by electric blues, neon magentas, hextech glow, and sakura accents.

Cute enough for branding. Judgmental enough for code review.

---

## 🗺️ Project Philosophy

Coder-Waifu is built around a few simple ideas:

- Requirements should be clarified before implementation.
- Important assumptions should be written down.
- Generated code should be reviewed adversarially.
- Different engineering concerns deserve different specialists.
- Long-running work should be resumable.
- Automation should ask permission before redecorating the architecture.

Or, more simply:

> Plan carefully, build deliberately, review mercilessly. `(｡•̀ᴗ-)✧`

---

## 📜 License

Released under the **MIT License**.

Use it, modify it, distribute it, build something strange with it.

Just do not be evil. That paperwork is exhausting. `ಠ_ಠ`

---

<div align="center">

Made with ✨, 🌸, and deeply questionable amounts of caffeine.

`(っ˘ڡ˘ς) ☕`

</div>