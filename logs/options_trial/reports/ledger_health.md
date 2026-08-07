# Ledger health — 2026-08-07

_Generated 2026-08-07T10:03:22.130502_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-21** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN |
| Orphaned lots (post-stable) |   439 | WARN |
| Missing exit records (post) |   436 | WARN |
| State/ledger mismatches     |    12 | WARN |
| Total open lots             |   107 | INFO |
| Total closed lots           |  1284 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Notes:
- **Current stuck** = open in `lab_state.json` and older than stuck threshold (actionable).
- **Post-stable orphaned / missing exits** = actionable WARN (entry_date > 2026-07-21).
- **Pre-cutoff debt** = entry_date < 2026-07-06 (INFO).
- **Transition debt** = 2026-07-06..2026-07-21 lot_id churn after attribution fix (INFO, not WARN).

## Current stuck lots

| lot_id | strategy | symbol | entry_day | age_days |
|--------|----------|--------|-----------|---------:|
| b428605e4e35 | S365 | AAPL | 2026-07-31 | 7 |

_Orphaned ledger detail omitted (439 rows) — see note above on historical lot_id churn._

## State/ledger mismatches

- `000575419aa8`
- `0462acb9348d`
- `3624e7324a17`
- `3ebc37036f3f`
- `54558629caa1`
- `572ccfa83bb5`
- `74f0b4f4bbf4`
- `9a4d8495dd2d`
- `9dc45701a68f`
- `a1a90a8a2dfe`
- `a30cd3dd8688`
- `da9784e57ebf`
