---
description: Manage scheduled jobs, view run history, and configure event triggers using mop CLI
---

# /mop:job Command

Execute or guide Mopheus job and trigger operations via `mop job` CLI based on user input: `$ARGUMENTS`.

- If `$ARGUMENTS` is empty:
  Run `mop job list` to show active workspace jobs, their trigger types (schedule/event/webhook), and status.
- If `$ARGUMENTS` is `runs <job-id>`:
  Run `mop job runs <job-id> --limit 10` to inspect recent execution history and status.
- If `$ARGUMENTS` is `trigger <job-id>`:
  Manually trigger a job run.
- If `$ARGUMENTS` is `event-schema [type]` or configures event triggers:
  Check capability `job.event_filters` via `python <skill-dir>/scripts/check_version.py --check job.event_filters`. Use `--event-filter-file` for JSON filters per `references/event_jobs.md`.
