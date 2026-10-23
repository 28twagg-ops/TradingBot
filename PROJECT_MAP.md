# PROJECT_MAP — TradingBot three-folder layout

Last updated: 2026-10-23 (reorg branch `chore/repo-reorg-three-folders`)

## Top level

```
TradingBot/
├── live-bots/          # runtime bots + shared collectors/helpers
├── research/           # offline studies + Myers spin-off
├── records/            # indexes, archives, research copies
├── logs/               # ACTIVE write root (GHA + bots) — not relocated
├── data/               # ACTIVE collector root — not relocated
├── scripts/            # thin compatibility wrappers → live-bots/research
├── simulations/        # thin wrappers + README → research/.../backtests
├── docs/               # handoff, protocols, reorg notes
├── .github/workflows/  # GHA (still calls wrappers + logs/ paths)
├── README.md
├── PROJECT_MAP.md
├── requirements.txt
└── rubber_band_bot.py  # wrapper → live-bots/rubber-band/
```

## live-bots/

| Path | Role |
|---|---|
| `rubber-band/rubber_band_bot.py` | Equity overnight/pullback LIVE bot |
| `options-paper/lab/` | `options_lab`, universe, OI helpers |
| `options-paper/strategies/` | signals, strategy lab, `strategy_registry.json` |
| `options-paper/bot/` | morning bot, reconcile, trial init, paper probe |
| `options-paper/reporting/` | dashboards, DQ, selection, bucket reports |
| `options-micro/` | tiny LIVE options sleeve (entries gated) |
| `shared/` | log merge/reconcile, collectors, `repo_root.py`, probes/tests |

## research/

| Path | Role |
|---|---|
| `myers-stock-investor/` | Business-acquirer research package (live disabled) |
| `options-strategies/` | Strategy catalog + `backtests/` (ex-`simulations/`) |
| `market-research/` | Rainbow BTC/ETH, midcap studies |
| `other-studies/` | PDT sims, historical runners, parity checks |

## records/

| Path | Role |
|---|---|
| `HISTORY_INDEX.md` | Where historical artifacts live |
| `MANIFEST.csv` | SHA-256 inventory of migrated/copied record files |
| `current/latest-results.md` | Regenerable pointer to newest reports |
| `research/` | Copies of study outputs (from `logs/research`) |
| `archive/2026/` | Safe document archives |
| `live/`, `paper/options/` | **Pointers only** — active ledgers remain under `logs/` |

## Active paths intentionally NOT moved

See `docs/_reorg/MIGRATION_PLAN.md`. Summary: `logs/options_trial`, `logs/options_live_micro`, RB `logs/daily|weekly|*.csv`, `logs/action_runs`, and `data/*` collector trees stay put because GHA restore/commit depends on those paths.

## Import / entry compatibility

- GHA continues to run `python rubber_band_bot.py` and `python scripts/<tool>.py`.
- Wrappers prepend package dirs onto `sys.path` and `runpy` the canonical file.
- Runtime modules resolve repo root via `live-bots/shared/repo_root.py` so `logs/` paths stay correct.
