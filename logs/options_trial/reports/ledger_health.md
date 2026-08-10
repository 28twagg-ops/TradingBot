# Ledger health — 2026-08-10

_Generated 2026-08-10T11:23:24.261878_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-21** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    10 | WARN |
| Orphaned lots (post-stable) |   569 | WARN |
| Missing exit records (post) |   559 | WARN |
| State/ledger mismatches     |    20 | WARN |
| Total open lots             |   166 | INFO |
| Total closed lots           |  1473 | INFO |
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
| 20cb3e46cf8a | S365 | NKE | 2026-08-04 | 6 |
| ddd8a7b0c2ac | S365 | NKE | 2026-08-04 | 6 |
| 7113a543a163 | S356 | NKE | 2026-08-04 | 6 |
| 2720cc0bbaf5 | S356 | NKE | 2026-08-04 | 6 |

_Orphaned ledger detail omitted (569 rows) — see note above on historical lot_id churn._

## State/ledger mismatches

- `045821cefc9e`
- `11b2d3e05ae0`
- `133f7a951bf3`
- `1ede6b0ddf78`
- `22f0a2fb2b22`
- `259dce6a6fd1`
- `29ad3249f505`
- `2f9855601404`
- `5171a3761c24`
- `63e0e4b32e9d`
- `658b6521d947`
- `6c27d15a6175`
- `8049c5bdf7c2`
- `90b59a5f364d`
- `bd8fa24261f2`
- `cc4b55253a19`
- `dcb872b623c3`
- `e8e2edd91d31`
- `eba395769bf8`
- `eeeb7d626317`
