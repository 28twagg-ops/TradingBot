# Ledger health — 2026-09-14

_Generated 2026-09-14T15:16:44.079999_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-21** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     4 | WARN |
| Orphaned lots (post-stable) |  1235 | WARN |
| Missing exit records (post) |  1231 | WARN |
| State/ledger mismatches     |     1 | WARN |
| Total open lots             |    39 | INFO |
| Total closed lots           |  2193 | INFO |
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
| c749b9facdbb | S366 | MARA | 2026-09-04 | 10 |
| 53ee58608a69 | S366 | MARA | 2026-09-04 | 10 |
| 01aab77eeb4e | S366 | MARA | 2026-09-04 | 10 |
| 4850d0ee6357 | S357 | PATH | 2026-09-04 | 10 |

_Orphaned ledger detail omitted (1235 rows) — see note above on historical lot_id churn._

## State/ledger mismatches

- `dc0ed772cb1f`
