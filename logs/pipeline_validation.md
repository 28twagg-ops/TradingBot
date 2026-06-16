# Pipeline Validation Notes

Generated during implementation.

## Static checks (local)

| Check | Result |
|-------|--------|
| `python -m py_compile rubber_band_bot.py` | PASS |
| `scripts/strategy_parity_check.py` | PASS (SCHEDULE/get_signals/check_exit regions hashed) |

## Benchmark (requires Alpaca env)

`scripts/benchmark_run.py` imports the bot module which requires `ALPACA_API_KEY` / `ALPACA_SECRET_KEY`. Run in GitHub Actions or locally with keys:

```bash
python scripts/benchmark_run.py
```

Expected improvements:
- Parallel `fetch_batch` with 16 workers vs sequential ~900 fetches
- Ticker list cache skips Wikipedia on repeat runs same day
- Plan cache skips universe fetch on execute runs when prep completed

## Runtime SLA tracking

New `runs.csv` columns: `duration_s`, `cache_hit`. Monitor after deploy.

## Cron schedule (cron-job.org Chicago time)

| Cron | ET mode |
|------|---------|
| 8:30 | exits |
| 8:35 | morning_prep |
| 8:45 | morning_scan |
| 9:00–14:30 | exits every 15m |
| 14:30 | evening_prep |
| 14:45 | scan |
| 15:00+ | ext_exits |

## Live account note

`PAPER_TRADING = False` → `STRICT_SAME_DAY_EXIT = True` (same-day stop exits still deferred on live). Set `PAPER_TRADING = True` in paper env for relaxed same-day stops.
