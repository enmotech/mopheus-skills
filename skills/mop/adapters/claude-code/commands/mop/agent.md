---
description: Inspect, configure, update system prompts, and manage skills for Mopheus agents using mop CLI
---

# /mop:agent Command

Execute or guide Mopheus agent operations via `mop agent` CLI based on user input: `$ARGUMENTS`.

- If `$ARGUMENTS` is empty:
  Run `mop agent list` to display all active agents, their roles, models, and providers in the active workspace.
- If `$ARGUMENTS` is `get <name-or-id>` or natural language (e.g. `查看代码审查员的配置`):
  Find agent ID and run `mop agent get <id>` to inspect its prompt instructions, model, and assigned skills.
- If `$ARGUMENTS` is `skills [list/add/remove]`:
  Manage agent skills (e.g. `mop agent skills add <agent-id> --skill <skill-id>`).
- If `$ARGUMENTS` is `tasks <agent-id>`:
  Run `mop agent tasks <agent-id>` to list recent tasks executed by this agent.
- If updating system prompt/instructions:
  Use `--instructions-file <file>` per `mop` safety rules.
