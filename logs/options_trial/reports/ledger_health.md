# Ledger health — 2026-08-06

_Generated 2026-08-06T13:42:02.682823_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-21** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN |
| Orphaned lots (post-stable) |   439 | WARN |
| Missing exit records (post) |   436 | WARN |
| State/ledger mismatches     |    28 | WARN |
| Total open lots             |   177 | INFO |
| Total closed lots           |  1217 | INFO |
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
| b428605e4e35 | S365 | AAPL | 2026-07-31 | 6 |

_Orphaned ledger detail omitted (439 rows) — see note above on historical lot_id churn._

## State/ledger mismatches

- `084f8e7a1006`
- `12dc9ff32024`
- `3b7ad7348e2d`
- `455af826a4e1`
- `4b71e30aa812`
- `53e410b0bd58`
- `61390b5f3d18`
- `66edc5e06c63`
- `6793458cc2d0`
- `6987e1474676`
- `6a7e0d153786`
- `6de12695f717`
- `7478afa6cf76`
- `79c3fa94dee8`
- `85a059fc6e80`
- `90420ec9c86d`
- `92c6395683e2`
- `9722ef523d65`
- `99f5a1427601`
- `9dc45701a68f`
- `a2e0625d04fc`
- `a8c739e5ce2c`
- `bc9ed069a924`
- `d465a8c7b174`
- `d4db12c7dd33`
- `d77c45e78e35`
- `f1d991055036`
- `f5363f91b2ab`
