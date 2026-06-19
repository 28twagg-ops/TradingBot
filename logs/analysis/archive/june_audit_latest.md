# June Daily Audit

Generated: 2026-06-13 22:06 UTC

## Performance Snapshot

| Window | Sells | Win Rate | P&L$ | Avg P&L% |
|---|---:|---:|---:|---:|
| 2026-06 (to date) | 130 | 35.38% | $-4.56 | -0.28% |
| 2026-05 baseline | 69 | 34.78% | $-5.18 | -0.35% |

## Execution Quality Checks

- Stop-loss overshoots (<= -3.0%) in June: **12** (15.38% of June stop-loss sells)
- Stop-loss overshoots (<= -3.0%) in May baseline: **6** (16.22% of May stop-loss sells)
- Duplicate same-day sells in June: **0**
- Daily markdown mismatches ("No trades today" but tx rows exist): **0**
- Run/tx exit-count mismatches in June dates: **0**

## Broker Fill Reconciliation

- Broker CSV not provided (phantom-sell check skipped).

## Go/No-Go Snapshot

- Execution gate: **PASS**
- Broker reconciliation gate: **PENDING**
- Strategy gate: **FAIL**

### Gate Rules

- Execution gate PASS requires: duplicate sells=0, daily-log mismatch=0, run-vs-tx mismatch=0, and June overshoot rate <= May rate.
- Broker gate PASS requires broker CSV provided and no unmatched June sell rows.
- Strategy gate PASS requires June sells >= 20, win rate >= 45.0%, and avg pnl per sell >= -0.10%.

### Execution Gate Check Detail

- duplicate_sells: PASS (0)
- daily_log_mismatch: PASS (0)
- run_tx_mismatch: PASS (0)
- overshoot_rate_not_worse_than_may: PASS (June 15.38% vs May 16.22%)
