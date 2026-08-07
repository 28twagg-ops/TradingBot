# Ledger health — 2026-08-07

_Generated 2026-08-07T09:20:50.295451_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-21** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN |
| Orphaned lots (post-stable) |   439 | WARN |
| Missing exit records (post) |   436 | WARN |
| State/ledger mismatches     |    18 | WARN |
| Total open lots             |   136 | INFO |
| Total closed lots           |  1241 | INFO |
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

- `084f8e7a1006`
- `4b71e30aa812`
- `53cf98d756f6`
- `54558629caa1`
- `61390b5f3d18`
- `66edc5e06c63`
- `6793458cc2d0`
- `6de12695f717`
- `6f0bf7f14309`
- `74f0b4f4bbf4`
- `90420ec9c86d`
- `92c6395683e2`
- `99f5a1427601`
- `9d579bc8d438`
- `9dc45701a68f`
- `a2e0625d04fc`
- `a8c739e5ce2c`
- `da9784e57ebf`
