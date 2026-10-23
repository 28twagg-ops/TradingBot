# TradingBot

Three-root layout for live bots, research, and historical records.

| Root | Purpose |
|---|---|
| [`live-bots/`](live-bots/) | Rubber Band LIVE, options paper lab, options live micro, shared helpers |
| [`research/`](research/) | Myers Stock Investor, options strategy studies, market research |
| [`records/`](records/) | History index, archives, research output copies (see also active `logs/`) |

**Repo:** https://github.com/28twagg-ops/TradingBot

## Standing rules

1. **Separate truths** — Rubber Band LIVE ≠ Options PAPER ≠ Options LIVE micro ≠ Myers research. Do not share ledgers.
2. **Live options entries stay OFF** unless a human explicitly re-enables them (`LIVE_OPTIONS_ENTRIES=0` in GHA).
3. Do not change TP/SL/sizing/RB live behavior as part of folder cleanup.
4. Compatibility wrappers remain at `rubber_band_bot.py` and `scripts/*.py` so GitHub Actions keeps working.

## Quick map

- Project map: [`PROJECT_MAP.md`](PROJECT_MAP.md)
- Strategy catalog: [`research/options-strategies/STRATEGY_CATALOG.md`](research/options-strategies/STRATEGY_CATALOG.md)
- History index: [`records/HISTORY_INDEX.md`](records/HISTORY_INDEX.md)
- Latest results pointer: [`records/current/latest-results.md`](records/current/latest-results.md)
- Handoff context: [`docs/HANDOFF_TRANSFER.md`](docs/HANDOFF_TRANSFER.md)
- Reorg plan: [`docs/_reorg/MIGRATION_PLAN.md`](docs/_reorg/MIGRATION_PLAN.md)

## Run (unchanged entrypoints)

```bash
# Rubber Band LIVE (GHA)
python rubber_band_bot.py

# Options paper morning bot (GHA)
python scripts/options_morning_bot.py

# Options live micro manage-only sleeve (GHA; entries gated off)
python scripts/options_live_micro.py

# Myers research (no live trading)
cd research/myers-stock-investor && python -m myers --help
```

## Setup

```bash
pip install -r requirements.txt
# Myers extras:
pip install -r research/myers-stock-investor/requirements.txt
```

## Active vs archived state

- **Active write roots (not relocated):** `logs/` (ledgers, daily/weekly RB logs, action runs) and `data/` (collectors).
- **Records:** indexes, manifests, research copies, and safe archives under `records/`.
