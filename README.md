# Mopheus Agent Skills

Official AI agent skills and slash command extensions for human-agent engineering collaboration across [Mopheus](https://mopheus.ai), Claude Code, OpenAI Codex, and modern coding environments.

Integrating AI coding agents into production workflows requires more than prompt templates. In real-world engineering, agents must reliably resolve workspace boundaries, preserve multi-line Markdown specifications without shell quote corruption, and gracefully handle environment and CLI version drift.

This repository provides production-hardened skills that connect autonomous agents directly with the Mopheus platform.

---

## Quick Setup

### 1. Install the skills

<details>
<summary><strong>Claude Code (Recommended Plugin)</strong></summary>

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
<summary><strong>OpenAI Codex, Cursor & Other Agents</strong></summary>

Install via the universal [skills.sh](https://skills.sh) manager:

```bash
npx skills add enmotech/mopheus-skills
```

This interactively configures the desired skills (`mop`, `using-codegraph`) and target agents (Codex, Cursor, Windsurf, etc.), placing each skill into its designated agent directory.

To install globally without prompts:

```bash
npx skills add enmotech/mopheus-skills -g -a codex --all
```

Or manually copy the skill directory:

```bash
cp -r skills/mop ~/.codex/skills/mop
```

</details>

<details>
<summary><strong>Axon Hub (Vendor Mirror)</strong></summary>

If you manage your AI editor environment with [Axon](https://github.com/kamusis/axon-cli), add this repository as an external vendor in `~/.axon/axon.yaml`:

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

### 2. Launch with `/mop`

Type `/mop` in your chat session to start the interactive workspace assistant:

```text
/mop
```

The assistant verifies your active workspace, inspects your local environment, and presents quick actions for tickets, agents, and automation jobs. You can also give natural-language commands in English or Chinese (e.g., `/mop show open tickets assigned to me` or `/mop 查一下未完结工单`), and the skill translates them into verified CLI executions.

---

## Engineering Design & Invariants

These skills are designed around strict operational invariants to prevent common agent failure modes:

### 1. Workspace Boundary Protection (Zero Guesswork)
Agents should never guess where they are working. The `mop` skill enforces a mandatory workspace validation gate. If the target workspace cannot be unambiguously resolved from the local repository or active session, the agent halts immediately and asks for confirmation rather than writing to a guessed workspace.

### 2. Specification Preservation (File & Stdin First)
Passing complex PRDs, stack traces, or review comments through shell flags (`--description "..."`) frequently breaks newlines, backticks, and quotation marks. `mop` standardizes on `--*-file` and stdin pipelines, streaming Markdown payloads with 100% byte fidelity.

### 3. Intent Routing & Command Ergonomics
Developers should not have to memorize exhaustive CLI syntax. In conversational agents, natural-language intents are dynamically mapped to structured CLI calls. In Claude Code, granular command aliases (`/mop:ticket`, `/mop:agent`, `/mop:workspace`, etc.) provide instant autocomplete and parameter guidance.

### 4. Version Matrix & Runtime Awareness
Tool capabilities evolve across releases. The bundled, zero-dependency `check_version.py` validator probes the local CLI version against a verified capability matrix. If an operation requires a newer CLI release or a background daemon, the agent alerts you upfront and provides fallback instructions.

---

## Available Skills

| Skill | Slash Command | Description |
| :--- | :--- | :--- |
| **`mop`** | `/mop` *(plus 6 aliases)* | Canonical Mopheus workspace, ticket, agent, team, job, and transcript integration. |
| **`using-codegraph`** | `/using-codegraph` | Semantic codebase architecture analysis and code graph retrieval. |

---

## Requirements

- **Mopheus CLI (`mop` or `mopheus`)**: Version `v2.1.0` or higher (tested up to `v2.2.4+`).
- **Python 3.8+**: Standard library only (no pip dependencies required), used by helper diagnostic scripts.

## Releases

Skills in this repository are versioned and automatically synchronized on every Mopheus release.

## License

[MIT](LICENSE) © Enmotech
