---
description: View, inspect, and switch active Mopheus workspaces using mop CLI
---

# /mop:workspace Command

Execute or guide Mopheus workspace operations via `mop workspace` CLI based on user input: `$ARGUMENTS`.

- If `$ARGUMENTS` is empty:
  Run `mop workspace list` to display all available workspaces and highlight the currently active workspace.
- If `$ARGUMENTS` is `switch <slug-or-id>` or natural language (e.g. `切到 dev-space`):
  Run `mop workspace switch <target>` and confirm the switch.
- If `$ARGUMENTS` is `get <id>` or `current`:
  Inspect the workspace details.
- Always observe `mop` safety invariants: verify target workspace exists before switching, never guess on ambiguity.
