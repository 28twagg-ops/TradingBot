# Failed Run Diagnosis (Jun 11–13 gap)

Generated during pipeline hardening implementation.

## Evidence

| Signal | Finding |
|--------|---------|
| Last `runs.csv` entry | `2026-06-10 23:45:27` (ext_exits) |
| No transactions after | No rows in `transactions.csv` after 2026-06-10 |
| No daily logs after | No `logs/daily/2026-06-11.md` etc. |
| Dashboard stale | `dashboard.md` still shows 2026-06-09 last run |

## Likely root causes (ranked)

1. **GitHub Actions run did not complete or did not push logs** — bot may have run locally/cron but commit step failed (concurrency queue, push conflict, or timeout).
2. **Scan runtime > 15 min** — workflow comment documents 20–30 min scans; with `cancel-in-progress: false`, runs queue and may overlap cron windows.
3. **Workflow dispatch only** — `run_bot.yml` uses `workflow_dispatch`; if cron-job.org webhook failed, no run triggered Thu/Fri.
4. **`gh` CLI unavailable** in local environment — could not pull Actions logs from this machine; check GitHub Actions UI for failed runs on Jun 11–12.

## Fixes applied

- Job `timeout-minutes: 25` with explicit failure
- `workflow_dispatch` `mode` input for manual recovery
- Git push retry on rebase conflict
- `BOT_MODE` env override
- Run duration + cache_hit in `runs.csv`
- Prep/execute split to keep execute runs under 15 min

## Manual recovery

Trigger workflow with mode `exits` or `morning_scan` / `scan` after market open, or set `BOT_MODE=summary` to verify connectivity.
