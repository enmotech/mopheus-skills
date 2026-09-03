---
description: Manage, view, search, and comment on Mopheus tickets using mop CLI
---

# /mop:ticket Command

Execute or guide Mopheus ticket operations via `mop ticket` CLI based on user input: `$ARGUMENTS`.

- If `$ARGUMENTS` is empty:
  Present quick ticket actions (list open tickets, search by keyword, view details, create new ticket) and prompt user.
- If `$ARGUMENTS` is natural language (e.g. `查一下紧急工单`, `查看工单 1048`):
  Translate intent to appropriate `mop ticket` command (e.g. `mop ticket list --priority urgent` or `mop ticket get <id-or-num>`), execute with `--output json`, and display formatted summary.
- If `$ARGUMENTS` contains CLI subcommands or flags (e.g. `list --status open`, `get <id>`):
  Execute `mop ticket $ARGUMENTS` directly.
- Always observe `mop` safety invariants (verify active workspace, use `--content-file` for multi-line comments).
