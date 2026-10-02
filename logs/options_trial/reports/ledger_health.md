# Ledger health — 2026-10-02

_Generated 2026-10-02T19:36:38.203244_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-21** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     6 | WARN |
| Orphaned lots (post-stable) |  1838 | WARN |
| Missing exit records (post) |  1832 | WARN |
| State/ledger mismatches     |     0 | OK |
| Total open lots             |    16 | INFO |
| Total closed lots           |  2679 | INFO |
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
| 18d8a9cd291d | S406 | NKE | 2026-09-25 | 7 |
| 89c3ca3043ba | S406 | NKE | 2026-09-25 | 7 |
| 6aff5a6b90ac | S406 | NKE | 2026-09-25 | 7 |
| 6b5580213d99 | S406 | NKE | 2026-09-25 | 7 |
| d722d11d533a | S399 | NKE | 2026-09-25 | 7 |
| de5f6ea50825 | S399 | NKE | 2026-09-25 | 7 |

_Orphaned ledger detail omitted (1838 rows) — see note above on historical lot_id churn._
