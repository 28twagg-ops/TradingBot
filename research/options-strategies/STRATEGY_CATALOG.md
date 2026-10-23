# STRATEGY_CATALOG — options paper / research

**Source of truth (mechanics):** `live-bots/options-paper/strategies/strategy_registry.json`  
**Research ranking (2026-10-23):** [`STRATEGY_RESEARCH_2026-10-23.md`](STRATEGY_RESEARCH_2026-10-23.md)  
**Profitability report:** [`PROFITABILITY_RESEARCH_REPORT.md`](PROFITABILITY_RESEARCH_REPORT.md)  
**Live gate:** entries OFF (`LIVE_OPTIONS_ENTRIES=0`). This catalog is for navigation, not promotion.

## Systems (keep separate)

| System | Ledger / outputs | Notes |
|---|---|---|
| Options paper lab | `logs/options_trial/` | Virtual buckets, cohort, twins |
| Options live micro | `logs/options_live_micro/` | Manage/orphans; $250 cap; entries gated |
| Rubber Band stocks | `logs/daily/`, `logs/transactions.csv`, … | Separate account/truth |
| Myers | `research/myers-stock-investor/outputs/` | Research only; live disabled |

## Live-allow names (paper twins exist; live entries OFF)

| ID | Name (registry) | Posture |
|---|---|---|
| S404 | GapDown_OTM2 | CONTINUE BASELINE + left-tail diagnostic |
| S406 | RubberBand_ITM3 | CONTINUE BASELINE + left-tail diagnostic |

## Day Trader Analytics (additive)

| ID | Name | Posture |
|---|---|---|
| S430 | DayTrader_ORB (opening-drive **proxy**) | DIAGNOSTIC — gather n; not classical ORB |
| S431 | DayTrader_RS | DIAGNOSTIC — often silent |
| S432 | DayTrader_ORB_RS | DIAGNOSTIC — gather n |

## Profitability experiments (paper-only, NEW IDs — awaiting forward evidence)

| ID | Name | Hypothesis |
|---|---|---|
| S440 | RubberBand_ITM3_StrongGap | Strong gap filter cuts S406 left tail |
| S441 | GapDown_OTM2_StrongGap | S404 structure + S166 gap quality |
| S442 | RubberBand_ITM3_5DTE | DTE neighbor to S362/S406 |
| S443 | TrueORB_15m | Classical ORB ≠ S430 drive proxy |

Paper buckets: `b92 s406_maxprem40`, `b93 s440_rb_stronggap`.

## Research priority labels (from 2026-10-23 report)

| Label | Examples |
|---|---|
| DEEPER EXPERIMENTATION | S406, S404, S362, S397, S167, S166, S410, true-ORB (new ID) |
| CONTINUE BASELINE | S406, S404 + promising-cohort KEEP set |
| DIAGNOSTIC | S430–S432; silent scanner zeros |
| EXCLUDED / KILL | CLEAN kill list (e.g. S212, S202, S360, S218, …) |

## Code locations

| Concern | Path |
|---|---|
| Signal definitions | `live-bots/options-paper/strategies/options_signals.py` |
| Bucket / twin lab | `live-bots/options-paper/lab/options_lab.py` |
| Registry writer / auto-kill | `live-bots/options-paper/strategies/options_strategy_lab.py` |
| Offline backtests | `research/options-strategies/backtests/` |
| Experiments folder | `research/options-strategies/experiments/` |

## How to refresh

```bash
python scripts/options_strategy_lab.py --list
python scripts/options_strategy_selection_report.py
```

Do **not** rewrite KEEP/twin arms to “make room.” New mechanics → new strategy IDs.
