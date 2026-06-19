# PDT Schedule Simulation Report

Generated: 2026-06-17T14:49:58
Universe: S&P 500 (495 tickers with data)
Starting equity: $500
Stop: -0.5% | Max hold: 3d | Reserve: 5%

## Executive summary

- Overnight schedule **beats** intraday full on total return (+158.1% vs +157.1%).

## Full 8-year comparison (2018–2025)

| Mode | Return | CAGR | Max DD | Sharpe | Trades | Win% | Stop avg | Overshoot | Day trades | OOS avg |
|------|--------|------|--------|--------|--------|------|----------|-----------|------------|---------|
| intraday_cap3 | +183.7% | +14.0% | -33.2% | 0.77 | 10735 | 52.8% | -1.99% | -1.49% | 5366 | +38.4% |
| overnight_pdt | +158.1% | +12.6% | -32.1% | 0.62 | 74527 | 54.4% | -1.99% | -1.49% | 0 | +52.3% |
| intraday_full | +157.1% | +12.6% | -41.5% | 0.73 | 149042 | 52.7% | -2.02% | -1.52% | 74520 | +46.5% |
| overnight_cap3 | +131.6% | +11.1% | -26.9% | 0.55 | 5369 | 55.2% | -1.86% | -1.36% | 0 | +38.6% |
| overnight_broker_stop | +114.7% | +10.1% | -32.1% | 0.53 | 74537 | 53.1% | -1.81% | -1.31% | 0 | +45.9% |
| strict_pdt | +103.4% | +9.3% | -41.5% | 0.53 | 121373 | 53.2% | -2.29% | -1.79% | 0 | +34.3% |

## By stress period

| period     |   intraday_cap3 |   intraday_full |   overnight_broker_stop |   overnight_cap3 |   overnight_pdt |   strict_pdt |
|:-----------|----------------:|----------------:|------------------------:|-----------------:|----------------:|-------------:|
| bear_2022  |         10.6364 |         3.49661 |                 6.76222 |          7.10819 |         6.15805 |     -4.89161 |
| bull_2024  |         44.0874 |        22.0106  |                17.6444  |         18.1797  |        19.2661  |     21.272   |
| full_8yr   |        183.694  |       157.061   |               114.7     |        131.594   |       158.055   |    103.391   |
| recent_3yr |         81.4451 |        54.9787  |                24.6388  |         35.2368  |        27.7425  |     47.5138  |

## Stop overshoot by period (avg % worse than -0.5%)

| period     |   intraday_cap3 |   intraday_full |   overnight_broker_stop |   overnight_cap3 |   overnight_pdt |   strict_pdt |
|:-----------|----------------:|----------------:|------------------------:|-----------------:|----------------:|-------------:|
| bear_2022  |        -1.45627 |        -1.32733 |               -0.963885 |         -1.02561 |        -1.00097 |     -1.53715 |
| bull_2024  |        -1.35396 |        -1.1268  |               -1.02491  |         -1.49358 |        -1.10233 |     -1.31284 |
| full_8yr   |        -1.48932 |        -1.52466 |               -1.31115  |         -1.36464 |        -1.49409 |     -1.78504 |
| recent_3yr |        -1.30545 |        -1.26485 |               -1.08594  |         -1.26478 |        -1.14635 |     -1.49771 |

## Mode definitions

- **intraday_full**: Morning + afternoon entries; intraday stop checks; same-day stops allowed; EOD midline.
- **strict_pdt**: Same entries; no same-day sells (old live guard); intraday stops after overnight only.
- **overnight_pdt**: Afternoon entries only; morning exits only (your proposal).
- **overnight_cap3**: Overnight schedule + max 3 new positions per day.
- **intraday_cap3**: Intraday full + max 3 entries/day.
- **overnight_broker_stop**: Overnight schedule + GTC stop on whole-share lots.

## Interpretation for $500 account

1. **PDT constraint**: overnight modes use **0 same-day round trips** for exits; intraday modes generate day trades.
2. **Stop overshoot**: strict PDT (hold losers overnight) usually worsens stop fills; overnight morning exit is a middle ground.
3. **Cap 3 entries**: concentrates capital (~$100+/position) — compare overnight_cap3 vs intraday_cap3.
4. Daily-bar sim approximates 15-min cron; real slippage may differ.

Runtime: 72846.8s

## Files

- `pdt_schedule_sim_summary.csv`
- `pdt_schedule_sim_by_period.csv`
- `pdt_schedule_sim_rolling_oos.csv`