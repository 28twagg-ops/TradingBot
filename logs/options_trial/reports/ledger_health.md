# Ledger health — 2026-09-11

_Generated 2026-09-11T17:56:15.582413_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-21** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     4 | WARN |
| Orphaned lots (post-stable) |  1190 | WARN |
| Missing exit records (post) |  1186 | WARN |
| State/ledger mismatches     |     1 | WARN |
| Total open lots             |    46 | INFO |
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
| c749b9facdbb | S366 | MARA | 2026-09-04 | 7 |
| 53ee58608a69 | S366 | MARA | 2026-09-04 | 7 |
| 01aab77eeb4e | S366 | MARA | 2026-09-04 | 7 |
| 4850d0ee6357 | S357 | PATH | 2026-09-04 | 7 |

_Orphaned ledger detail omitted (1190 rows) — see note above on historical lot_id churn._

## State/ledger mismatches

- `dc0ed772cb1f`
