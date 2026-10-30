# Migration report — three-folder reorg

**Branch:** `chore/repo-reorg-three-folders`  
**Date:** 2026-10-23  
**Backup:** `C:\Users\28twa\Desktop\TradingBot-reorg-backup-20261023-110514` (261 SHA-256 rows)

## Moved / created (summary)

| Area | Action |
|---|---|
| Live bot code | Relocated into `live-bots/{rubber-band,options-paper,options-micro,shared}` |
| Research code | `research/{myers-stock-investor,options-strategies,market-research,other-studies}` |
| Simulations | Moved to `research/options-strategies/backtests/` (+ thin `simulations/` wrappers) |
| Docs indexes | New root `README.md`, `PROJECT_MAP.md`, strategy/history docs |
| Records | `records/` indexes + **copies** of `logs/research` + docs archive (originals kept) |
| Wrappers | `rubber_band_bot.py`, `scripts/*.py` → canonical modules |

Approximate code moves from `scripts/` + root bot: **~50 Python modules** relocated with wrappers.  
`simulations/` contents moved into backtests. Myers tree moved under `research/`.

## Preservation

- No historical ledgers deleted.
- Active `logs/` and `data/` trees left in place.
- Research outputs copied to `records/research/` with SHA-256 in `records/MANIFEST.csv` (0 mismatches on 11-file sample vs `logs/research`).
- Session/handoff docs copied to `records/archive/2026/` (sources remain under `docs/`).

## Risks

- GHA still depends on wrappers + `logs/` paths; if wrappers break, CI fails before trading logic changes.
- Relative `Path(__file__).parent.parent` assumptions were rewritten to `find_repo_root()` for runtime writers — regression risk if a path was missed (research-only scripts lower priority).
- Local clones behind `origin/main` bot-run commits remain a separate issue (unchanged by reorg).

## Rollback

1. `git checkout fix/trading-safety-and-strategy-research` (or prior SHA) and delete this branch, **or**
2. Restore files from `TradingBot-reorg-backup-20261023-110514`, **or**
3. Revert the reorg commit(s) on this branch (no force-push / history rewrite).

## Intentionally NOT moved

| Path | Why |
|---|---|
| `logs/options_trial/` | Active paper ledger + GHA restore/commit |
| `logs/options_live_micro/` | Active micro ledger + GHA restore |
| `logs/daily|weekly|*.csv|ab_test|plans|cache|action_runs` | Rubber Band / GHA active writers |
| `data/**` collector trees | GHA `git add data/...` paths |
| Live options env / TP/SL/sizing | Untouched (`LIVE_OPTIONS_ENTRIES=0`) |

## Tests run

- YAML load: all 4 workflows OK
- Import smoke: `options_lab` TRIAL_ROOT → `logs/options_trial`
- `scripts/test_options_live_micro_safety.py`: **14 passed**
- `scripts/test_day_trader_data_validity.py`: **12 passed**
- `pytest research/myers-stock-investor/tests`: **14 passed**
- Full live GHA run / broker smoke: **not run** (no credentials / market)
