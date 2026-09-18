# Ledger health — 2026-09-18

_Generated 2026-09-18T14:37:33.598447_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-21** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN |
| Orphaned lots (post-stable) |  1368 | WARN |
| Missing exit records (post) |  1365 | WARN |
| State/ledger mismatches     |     5 | WARN |
| Total open lots             |    71 | INFO |
| Total closed lots           |  2384 | INFO |
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
| c749b9facdbb | S366 | MARA | 2026-09-04 | 14 |
| 53ee58608a69 | S366 | MARA | 2026-09-04 | 14 |
| 01aab77eeb4e | S366 | MARA | 2026-09-04 | 14 |

_Orphaned ledger detail omitted (1368 rows) — see note above on historical lot_id churn._

## State/ledger mismatches

- `375229c55f38`
- `4ad03a11d251`
- `4d58aa709fac`
- `b9ef71d211aa`
- `ff6c86c178cc`
