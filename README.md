# mopheus-skills

Official collection of AI agent skills, plugins, and slash command extensions for [Mopheus](https://mopheus.ai), Claude Code, OpenAI Codex, and modern AI development environments.

This repository is automatically synchronized from the `skills/` directory of [enmotech/mopheus](https://github.com/enmotech/mopheus) on every release.

---

## Available Skills

### 1. `mop` (Mopheus CLI & Agent Collaboration)

The canonical skill for managing Mopheus workspaces, tickets, agents, teams, and automation triggers.

- **Universal Slash Command (`/mop`)**:
  - **Interactive Wizard**: Run `/mop` without arguments for an instant, categorized quick-action menu.
  - **Natural Language Intent**: Run `/mop find urgent tickets` or `/mop 查一下未完结工单` to automatically translate plain language into structured CLI queries.
  - **Direct CLI Execution**: Run full commands such as `mop ticket list --status open`.
- **Claude Code Pre-built Command Aliases**:
  - `/mop:ticket` — Manage, search, assign, comment, and rerun tickets.
  - `/mop:agent` — Inspect agent system instructions, configure models, and manage skill assignments.
  - `/mop:search` — Global full-text search across tickets, agents, skills, and projects.
  - `/mop:workspace` — View, inspect, and switch active workspace.
  - `/mop:job` — Manage automated jobs, execution history, and event triggers.
  - `/mop:task` — Reconstruct agent thinking steps, transcripts, and debug tool executions.
- **Safety & Performance**:
  - Zero-guesswork workspace validation gate.
  - Native `--*-file` flags for clean multi-line Markdown descriptions and comments.
  - Cross-platform capability matrix detector (`check_version.py`) with automatic fallback alerts and `mop upgrade` guidance.

### 2. `using-codegraph`

Semantic codebase exploration and architecture analysis using the Mopheus CodeGraph engine.

---

## Installation

### Option 1: Axon Skill Manager (Recommended)

If you use [Axon](https://github.com/enmotech/axon):

```bash
axon install enmotech/mopheus-skills
```

### Option 2: Claude Code

Clone into your Claude Code skills directory:

```bash
git clone https://github.com/enmotech/mopheus-skills.git ~/.claude/skills/mopheus-skills
```

To enable the granular slash commands (`/mop:ticket`, `/mop:agent`, etc.) in Claude Code:

```bash
python ~/.claude/skills/mopheus-skills/skills/mop/scripts/install_claude_commands.py
```

### Option 3: OpenAI Codex & General Agents

Clone into your Codex skills directory:

```bash
git clone https://github.com/enmotech/mopheus-skills.git ~/.codex/skills/mopheus-skills
```

---

## Releases

Skills in this repository are versioned and synchronized with `enmotech/mopheus` releases.

## License

[MIT](LICENSE) © Enmotech
