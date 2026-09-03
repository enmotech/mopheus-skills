# Skills For Real Human-Agent Engineering

Official collection of production-grade AI agent skills, plugins, and slash command extensions for [Mopheus](https://mopheus.ai), Claude Code, OpenAI Codex, and modern AI development environments.

Developing autonomous agent workflows is hard. Most AI prompts are toy demos that fail when real engineering begins: they guess wrong workspaces, drop long Markdown specs due to shell escaping, or silently break when CLI versions drift.

These skills are engineered from real-world production experience. They enforce strict safety invariants, provide natural language intent routing, handle complex multi-line specifications natively, and keep external AI coding tools in lockstep with Mopheus.

---

## Installation (30-second setup)

### 1. Get the skills

<details>
<summary><strong>Claude Code</strong></summary>

Inside your Claude Code session:

```text
/plugin marketplace add enmotech/mopheus-skills
/plugin install mop
```

Or from your terminal:

```bash
claude plugin marketplace add enmotech/mopheus-skills
claude plugin install mop
```

Once installed, `/mop` and all namespaced slash commands (`/mop:ticket`, `/mop:agent`, `/mop:search`, `/mop:workspace`, `/mop:job`, `/mop:task`) are automatically registered and managed.

</details>

<details>
<summary><strong>OpenAI Codex & General Agents</strong></summary>

Clone into your Codex skills directory:

```bash
git clone https://github.com/enmotech/mopheus-skills.git ~/.codex/skills/mopheus-skills
```

Or copy `skills/mop` directly into your workspace's `.codex/skills/` folder.

</details>

<details>
<summary><strong>Axon Skill Hub (Vendor Mirror)</strong></summary>

If you manage your AI skills across machines via [Axon](https://github.com/kamusis/axon-cli), add this repository as a vendor source in `~/.axon/axon.yaml`:

```yaml
vendors:
  - name: mopheus-skills
    repo: https://github.com/enmotech/mopheus-skills.git
    subdir: skills
    dest: skills
    ref: main
```

Then sync to your hub:

```bash
axon vendor sync
```

</details>

### 2. Run `/mop`

In your agent chat box, simply type:

```text
/mop
```

It will instantly present an interactive quick-action guide. You can also directly ask in plain English or Chinese (e.g. `/mop check urgent tickets` or `/mop 查一下未完结工单`), and the agent will translate your request into verified CLI actions.

### 3. Bam — you're ready to collaborate.

---

## Why These Skills Exist

We built these skills to systematically eliminate the most common failure modes when using coding agents in production:

### #1: The Agent Guesses the Wrong Workspace or Project
**The Problem**: Agents love to assume. When asked to create or update a ticket, an agent might pick a random workspace or hallucinate defaults, polluting other environments or failing silently.

**The Fix**: `mop` enforces a strict **Zero-Guesswork Workspace Gate**. If the target workspace cannot be unambiguously confirmed, the agent halts immediately and presents candidates instead of guessing.

### #2: Shell Escaping Corrupts Large Markdown Specs
**The Problem**: Passing large PRD descriptions, stack traces, or review comments via CLI flags (`--description "..."`) leads to quote escaping nightmares, broken backticks, and stripped newlines.

**The Fix**: `mop` standardizes on **Native File & Stdin First** (`--description-file`, `--content-file`, `--instructions-file`). Specs and comments are passed cleanly via temporary files or streams with 100% byte fidelity.

### #3: Memorizing CLI Subcommands is Painful
**The Problem**: Developers use AI to save time, not to memorize dozens of CLI flags like `mop ticket list --priority urgent --output json`.

**The Fix**: `mop` provides **Intent Routing & Slash Aliases**. In Codex and universal tools, `/mop <natural language>` maps plain language directly to CLI calls. In Claude Code, pre-packaged aliases (`/mop:ticket`, `/mop:agent`, `/mop:workspace`, `/mop:job`, `/mop:task`, `/mop:search`) offer instant dropdown completion.

### #4: Version Drift Between Local CLI and Remote Server
**The Problem**: Different machines have different CLI versions installed. An agent might attempt a newer command flag, fail with a syntax error, and enter an infinite retry loop.

**The Fix**: A bundled, zero-dependency **Capability Matrix Detector** (`check_version.py`). When a capability is unsupported or requires a local daemon, the agent proactively alerts you, suggests the exact fallback, and provides the upgrade command.

---

## Available Skills

| Skill | Slash Command | Description |
| :--- | :--- | :--- |
| **`mop`** | `/mop` *(plus 6 aliases)* | Canonical Mopheus workspace, ticket, agent, team, job, and transcript integration. |
| **`using-codegraph`** | `/using-codegraph` | Semantic codebase architecture analysis and code graph retrieval. |

---

## Requirements

- **Mopheus CLI (`mop` or `mopheus`)**: Version `v2.1.0` or higher (tested up to `v2.2.4+`).
- **Python 3.8+**: Standard library only (no `pip install` required), used by helper utilities.

## Releases

Skills in this repository are versioned and automatically synchronized on every Mopheus release.

## License

[MIT](LICENSE) © Enmotech
