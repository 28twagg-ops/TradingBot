# Ledger health — 2026-10-01

_Generated 2026-10-01T10:27:44.610358_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-21** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    21 | WARN |
| Orphaned lots (post-stable) |  1838 | WARN |
| Missing exit records (post) |  1817 | WARN |
| State/ledger mismatches     |     1 | WARN |
| Total open lots             |    29 | INFO |
| Total closed lots           |  2670 | INFO |
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
| 97e54812e581 | S412 | NKE | 2026-09-25 | 6 |
| cd504ce17d57 | S412 | NKE | 2026-09-25 | 6 |
| 18d8a9cd291d | S406 | NKE | 2026-09-25 | 6 |
| 89c3ca3043ba | S406 | NKE | 2026-09-25 | 6 |
| 2e2b7dbe88f6 | S364 | NKE | 2026-09-25 | 6 |
| 9d0435e919d4 | S364 | NKE | 2026-09-25 | 6 |
| a9ac3e75cc9c | S404 | NKE | 2026-09-25 | 6 |
| 801e26c21ddd | S398 | NKE | 2026-09-25 | 6 |
| fbdfb716ce45 | S398 | NKE | 2026-09-25 | 6 |
| 4d094b033538 | S163 | NKE | 2026-09-25 | 6 |
| 60d4b8ef839f | S163 | NKE | 2026-09-25 | 6 |
| 31e53303cac8 | S167 | NKE | 2026-09-25 | 6 |
| 74d7cb42e718 | S167 | NKE | 2026-09-25 | 6 |
| 934ce252885e | S168 | NKE | 2026-09-25 | 6 |
| 60824a4f94fb | S168 | NKE | 2026-09-25 | 6 |
| 736da7fa1059 | S165 | NKE | 2026-09-25 | 6 |
| 5aa2635aa5e0 | S165 | NKE | 2026-09-25 | 6 |
| 6aff5a6b90ac | S406 | NKE | 2026-09-25 | 6 |
| 6b5580213d99 | S406 | NKE | 2026-09-25 | 6 |
| d722d11d533a | S399 | NKE | 2026-09-25 | 6 |
| de5f6ea50825 | S399 | NKE | 2026-09-25 | 6 |

_Orphaned ledger detail omitted (1838 rows) — see note above on historical lot_id churn._

## State/ledger mismatches

- `aee8303ec6d8`
