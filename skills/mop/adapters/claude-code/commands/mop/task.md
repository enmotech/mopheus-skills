---
description: Inspect agent tasks, stream transcripts, view tool steps, and diagnose errors using mop CLI
---

# /mop:task Command

Execute or guide Mopheus agent task diagnostics via `mop agent-task` CLI based on user input: `$ARGUMENTS`.

- If `$ARGUMENTS` is empty:
  Prompt the user for an agent task ID or offer to look up recent task IDs from recent ticket comments.
- If `$ARGUMENTS` is `get <task-id>` or natural language asking for task status:
  Run `mop agent-task get <task-id> --output json` to show status, duration, and error summary.
- If `$ARGUMENTS` is `transcript <task-id>` or asks for dialogue/tool details:
  Execute `python <skill-dir>/scripts/mop_task.py transcript <task-id>`.
- If `$ARGUMENTS` is `tools <task-id>`:
  Execute `python <skill-dir>/scripts/mop_task.py transcript <task-id> --tools-only`.
