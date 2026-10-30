# HISTORY_INDEX — where records live

Active bots still write under **`logs/`** (and collectors under **`data/`**).  
`records/` holds indexes, manifests, research copies, and safe archives. Nothing here replaces a live ledger.

## Active ledgers (authoritative, not moved)

| Artifact | Path | Owner |
|---|---|---|
| Options paper trial | `logs/options_trial/` (`_ledger/`, `_state/`, `reports/`, `runs/`, `buckets/`) | options-paper |
| Options live micro | `logs/options_live_micro/` | options-micro |
| Rubber Band daily/weekly | `logs/daily/`, `logs/weekly/` | rubber-band |
| Rubber Band transactions/runs | `logs/transactions.csv`, `logs/runs.csv`, `logs/execution_audit.csv` | rubber-band |
| GHA action runs | `logs/action_runs/` | shared / GHA |
| Paper misc | `logs/paper/` | paper |
| Minute / first-hour data | `data/stocks_1min/`, `data/options_1min/`, `data/first_hour/`, `data/quality/` | collectors |

## Research & archives under records/

| Artifact | Path |
|---|---|
| File checksum manifest | [`MANIFEST.csv`](MANIFEST.csv) |
| Latest results pointer | [`current/latest-results.md`](current/latest-results.md) |
| Market-research outputs (copy) | `records/research/` (from `logs/research/`) |
| Session / transfer docs (copy) | `records/archive/2026/` |
| Offline backtest results | `research/options-strategies/backtests/results/` (code+results co-located) |
| Myers backtest outputs | `research/myers-stock-investor/outputs/` |

## Pointer dirs (no ledger merge)

- `records/live/` — see README there; points at RB + micro active paths
- `records/paper/options/` — points at `logs/options_trial/`

## Regeneration

```bash
python records/regenerate_latest_results.py
python docs/_reorg/build_records_manifest.py
```
