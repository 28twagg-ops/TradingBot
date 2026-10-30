# Repo Reorg Migration Plan — three root folders

**Branch:** `chore/repo-reorg-three-folders`  
**Started:** 2026-10-23  
**Backup (verified):** `C:\Users\28twa\Desktop\TradingBot-reorg-backup-20261023-110514`  
**Backup manifest rows:** 261 (SHA-256)  
**Base HEAD at branch create:** `5395a181ec` (safety branch tip)

## Target roots

| Root | Purpose |
|---|---|
| `live-bots/` | Rubber Band LIVE, options paper lab, options live micro, shared helpers |
| `research/` | Myers, options strategy experiments/backtests, market studies |
| `records/` | Immutable history index, archives, research outputs; **not** GHA active ledgers |

## Absolute do-not-break

- `LIVE_OPTIONS_ENTRIES=0` and all TP/SL/sizing/RB live behavior unchanged
- Separate ledgers: RB ≠ options paper ≠ options micro ≠ Myers
- No force-push / history rewrite / destructive reset
- Prefer incomplete-but-safe over moving active GHA state

## Active paths intentionally LEFT at old locations

| Path | Why not moved |
|---|---|
| `logs/options_trial/` | Paper ledger + `_state` restored/committed by GHA every run |
| `logs/options_live_micro/` | Live micro ledger/runs; GHA dual-path restore |
| `logs/daily/`, `logs/weekly/`, `logs/transactions.csv`, `logs/runs.csv`, `logs/ab_test/`, `logs/plans/`, `logs/cache/` | Rubber Band LIVE writers use `Path("logs")` |
| `logs/action_runs/` | GHA tee + review commit path |
| `data/stocks_1min/`, `data/options_1min/`, `data/quality/`, `data/first_hour/` | Collector workflows `git add` these paths |
| `logs/` root CSVs / dashboard | Active RB truth files |

Compatibility: `logs/` remains the **live write root**. `records/` holds indexes, research copies, and safe archives. Dual-path or wrappers preferred over relocating GHA restore targets.

## Code move map (Phase C)

### live-bots/rubber-band/

- `rubber_band_bot.py` → `live-bots/rubber-band/rubber_band_bot.py`
- Root wrapper: `rubber_band_bot.py` (thin)

### live-bots/options-paper/

| Dest | Sources |
|---|---|
| `lab/` | `options_lab.py`, `options_universe.py`, `options_oi.py` |
| `strategies/` | `options_signals.py`, `options_strategy_lab.py`, `strategy_registry.json` |
| `bot/` | `options_morning_bot.py`, `options_reconcile.py`, `init_options_trial.py`, `options_paper_probe.py` |
| `reporting/` | daily/selection/DQ/ledger/dashboard/signal_frequency/lab_report/review/append/merge/rubber_band_report |

### live-bots/options-micro/

- `options_live_micro.py`, `test_options_live_micro_safety.py`

### live-bots/shared/

- Log helpers used by both bots: `merge_bot_logs.py`, `reconcile_daily_logs.py`, `daily_slippage_watch.py`, `append_action_run_review.py`
- Data collectors (GHA): `options_data_collector.py`, `first_hour_collector.py`, `data_quality_monitor.py`
- Misc probes/tests tied to runtime: `test_day_trader_data_validity.py`, `test_options_chain_cache.py`, `api_probe_options.py`, `options_microlive_sim.py`, `benchmark_run.py`, `local_docs.py`

### research/

| Dest | Sources |
|---|---|
| `myers-stock-investor/` | root `myers-stock-investor/` (untracked → tracked) |
| `options-strategies/` | `simulations/*` strategy sims + `docs/STRATEGY_RESEARCH_*` → catalog |
| `market-research/` | rainbow/midcap scripts + `logs/research` outputs (copied/moved into records + research) |
| `other-studies/` | PDT/sim helpers, stop-overshoot analysis, historical fetchers, parity checks |

### records/ (Phase D — safe only)

- `HISTORY_INDEX.md`, `MANIFEST.csv`, `current/latest-results.md`
- `research/` ← migrate `logs/research/*` (immutable study outputs)
- `archive/2026/` ← session docs copies (originals may remain under research docs pointers)
- **Do not** relocate active ledgers listed above

## Workflow policy (Phase E)

- Keep invoking `python scripts/<name>.py` and `python rubber_band_bot.py` via **compatibility wrappers**
- Annotate workflows with new canonical paths in comments
- Do not change log restore/commit/reset/rebase logic paths (`logs/…`)

## Rollback

1. Discard branch / reset to pre-reorg commit
2. Or restore from `TradingBot-reorg-backup-20261023-110514`
3. Wrappers mean old CI commands keep working if new tree is incomplete
