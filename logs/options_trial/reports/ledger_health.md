# Ledger health — 2026-09-22

_Generated 2026-09-22T14:36:36.680047_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-21** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN |
| Orphaned lots (post-stable) |  1485 | WARN |
| Missing exit records (post) |  1482 | WARN |
| State/ledger mismatches     |     1 | WARN |
| Total open lots             |    20 | INFO |
| Total closed lots           |  2404 | INFO |
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
| c749b9facdbb | S366 | MARA | 2026-09-04 | 18 |
| 53ee58608a69 | S366 | MARA | 2026-09-04 | 18 |
| 01aab77eeb4e | S366 | MARA | 2026-09-04 | 18 |

_Orphaned ledger detail omitted (1485 rows) — see note above on historical lot_id churn._

## State/ledger mismatches

- `70d8f5d2698f`
