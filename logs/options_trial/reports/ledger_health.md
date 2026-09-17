# Ledger health — 2026-09-17

_Generated 2026-09-17T13:56:26.715632_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-21** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     6 | WARN |
| Orphaned lots (post-stable) |  1371 | WARN |
| Missing exit records (post) |  1365 | WARN |
| State/ledger mismatches     |     3 | WARN |
| Total open lots             |    87 | INFO |
| Total closed lots           |  2320 | INFO |
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
| c749b9facdbb | S366 | MARA | 2026-09-04 | 13 |
| 53ee58608a69 | S366 | MARA | 2026-09-04 | 13 |
| 01aab77eeb4e | S366 | MARA | 2026-09-04 | 13 |
| 7772468d72fe | S163 | MARA | 2026-09-10 | 7 |
| b7a0810f1625 | S168 | MARA | 2026-09-10 | 7 |
| af2fd15cfdcf | S168 | MARA | 2026-09-10 | 7 |

_Orphaned ledger detail omitted (1371 rows) — see note above on historical lot_id churn._

## State/ledger mismatches

- `1d79395b7a8c`
- `4ad03a11d251`
- `92d6ead45f7f`
