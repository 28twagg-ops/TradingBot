# Ledger health — 2026-09-15

_Generated 2026-09-15T10:37:44.663476_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-21** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN |
| Orphaned lots (post-stable) |  1249 | WARN |
| Missing exit records (post) |  1246 | WARN |
| State/ledger mismatches     |     7 | WARN |
| Total open lots             |   131 | INFO |
| Total closed lots           |  2202 | INFO |
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
| c749b9facdbb | S366 | MARA | 2026-09-04 | 11 |
| 53ee58608a69 | S366 | MARA | 2026-09-04 | 11 |
| 01aab77eeb4e | S366 | MARA | 2026-09-04 | 11 |

_Orphaned ledger detail omitted (1249 rows) — see note above on historical lot_id churn._

## State/ledger mismatches

- `125f2541210f`
- `1431dd8f92ab`
- `22709155a481`
- `887a398506d2`
- `aca45f6ebd44`
- `b4e39ad6e508`
- `dbdd74147a7c`
