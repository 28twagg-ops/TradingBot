# Ledger health — 2026-09-15

_Generated 2026-09-15T13:06:30.540755_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-21** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN |
| Orphaned lots (post-stable) |  1249 | WARN |
| Missing exit records (post) |  1246 | WARN |
| State/ledger mismatches     |     7 | WARN |
| Total open lots             |   158 | INFO |
| Total closed lots           |  2226 | INFO |
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

- `4ad03a11d251`
- `5a5c36f249e4`
- `668afe5da4c8`
- `6f7f01b37d67`
- `cc7b1c7c6c24`
- `d2b945db64b7`
- `df7e85af155e`
