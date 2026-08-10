# Ledger health — 2026-08-10

_Generated 2026-08-10T10:38:08.597823_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-21** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    16 | WARN |
| Orphaned lots (post-stable) |   575 | WARN |
| Missing exit records (post) |   559 | WARN |
| State/ledger mismatches     |    12 | WARN |
| Total open lots             |   113 | INFO |
| Total closed lots           |  1419 | INFO |
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
| 04706b86c9c5 | S356 | NKE | 2026-08-04 | 6 |
| 471621ef50e0 | S356 | NKE | 2026-08-04 | 6 |
| bbf9db0f84e1 | S365 | NKE | 2026-08-04 | 6 |
| a1ce26a89873 | S365 | NKE | 2026-08-04 | 6 |
| 865b546efdca | S356 | NKE | 2026-08-04 | 6 |
| b8376153a452 | S356 | NKE | 2026-08-04 | 6 |
| ab30ad0b2ee8 | S366 | NKE | 2026-08-04 | 6 |
| ae42efc4cc2c | S366 | NKE | 2026-08-04 | 6 |
| 20cb3e46cf8a | S365 | NKE | 2026-08-04 | 6 |
| ddd8a7b0c2ac | S365 | NKE | 2026-08-04 | 6 |
| f8a075667cea | S366 | NKE | 2026-08-04 | 6 |
| c151a9036f99 | S366 | NKE | 2026-08-04 | 6 |
| 32967836008c | S366 | NKE | 2026-08-04 | 6 |
| 9b997fb24b3b | S366 | NKE | 2026-08-04 | 6 |
| 7113a543a163 | S356 | NKE | 2026-08-04 | 6 |
| 2720cc0bbaf5 | S356 | NKE | 2026-08-04 | 6 |

_Orphaned ledger detail omitted (575 rows) — see note above on historical lot_id churn._

## State/ledger mismatches

- `004a6cca4c14`
- `01fde3a6c073`
- `17e7b5915e92`
- `190aacc7e5f8`
- `21bb51003d84`
- `37e5dbb9d3c6`
- `592af16676b2`
- `6381ff1a2184`
- `8fe318b124a3`
- `c1e8d94fd59e`
- `c63d62d9028e`
- `f9a047cd6c58`
