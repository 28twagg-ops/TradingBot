# Ledger health — 2026-09-10

_Generated 2026-09-10T13:31:47.443473_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-21** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN |
| Orphaned lots (post-stable) |  1200 | WARN |
| Missing exit records (post) |  1185 | WARN |
| State/ledger mismatches     |     4 | WARN |
| Total open lots             |   111 | INFO |
| Total closed lots           |  2157 | INFO |
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
| 361232eb5b07 | S366 | MARA | 2026-09-04 | 6 |
| c749b9facdbb | S366 | MARA | 2026-09-04 | 6 |
| 53ee58608a69 | S366 | MARA | 2026-09-04 | 6 |
| 01aab77eeb4e | S366 | MARA | 2026-09-04 | 6 |
| 4850d0ee6357 | S357 | PATH | 2026-09-04 | 6 |
| 3b55ba0967c8 | S365 | MARA | 2026-09-04 | 6 |
| d52b6db3a02a | S365 | MARA | 2026-09-04 | 6 |
| 40a2c3f0b67b | S356 | MARA | 2026-09-04 | 6 |
| 75ca2d7b5bd3 | S356 | MARA | 2026-09-04 | 6 |
| 956c4b15bfde | S357 | MARA | 2026-09-04 | 6 |
| 616989650086 | S357 | MARA | 2026-09-04 | 6 |
| 7158e568e740 | S365 | MARA | 2026-09-04 | 6 |
| a93bf29b9fc7 | S365 | MARA | 2026-09-04 | 6 |
| dc5a40562a7d | S356 | MARA | 2026-09-04 | 6 |
| 75790593d310 | S356 | MARA | 2026-09-04 | 6 |

_Orphaned ledger detail omitted (1200 rows) — see note above on historical lot_id churn._

## State/ledger mismatches

- `24a97d7db5d3`
- `a447d8346b3a`
- `dc0ed772cb1f`
- `e7586c6ae7e0`
