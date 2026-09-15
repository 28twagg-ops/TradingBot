# Ledger health — 2026-09-15

_Generated 2026-09-15T11:12:41.276361_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-21** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN |
| Orphaned lots (post-stable) |  1249 | WARN |
| Missing exit records (post) |  1246 | WARN |
| State/ledger mismatches     |    10 | WARN |
| Total open lots             |   151 | INFO |
| Total closed lots           |  2212 | INFO |
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
- `22709155a481`
- `2c68a42b2e68`
- `3951f5783e17`
- `4ad03a11d251`
- `a18f3ba26839`
- `aca45f6ebd44`
- `cc7b1c7c6c24`
- `d2b945db64b7`
- `dbdd74147a7c`
