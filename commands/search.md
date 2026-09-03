---
description: Search tickets, agents, skills, and projects across the active Mopheus workspace using mop CLI
---

# /mop:search Command

Execute workspace-wide search via `mop search` CLI based on user input: `$ARGUMENTS`.

- If `$ARGUMENTS` is empty:
  Prompt user for a search query or filter type.
- Execute:
  `mop search "$ARGUMENTS"`
- If type filter requested (e.g. only tickets or only agents):
  Add `--type ticket` or `--type agent` or `--type skill`.
