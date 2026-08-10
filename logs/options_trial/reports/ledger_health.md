# Ledger health — 2026-08-10

_Generated 2026-08-10T11:56:42.724108_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-21** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     9 | WARN |
| Orphaned lots (post-stable) |   568 | WARN |
| Missing exit records (post) |   559 | WARN |
| State/ledger mismatches     |    21 | WARN |
| Total open lots             |   173 | INFO |
| Total closed lots           |  1503 | INFO |
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
| 471621ef50e0 | S356 | NKE | 2026-08-04 | 6 |
| bbf9db0f84e1 | S365 | NKE | 2026-08-04 | 6 |
| a1ce26a89873 | S365 | NKE | 2026-08-04 | 6 |
| 865b546efdca | S356 | NKE | 2026-08-04 | 6 |
| b8376153a452 | S356 | NKE | 2026-08-04 | 6 |
| 20cb3e46cf8a | S365 | NKE | 2026-08-04 | 6 |
| ddd8a7b0c2ac | S365 | NKE | 2026-08-04 | 6 |
| 7113a543a163 | S356 | NKE | 2026-08-04 | 6 |
| 2720cc0bbaf5 | S356 | NKE | 2026-08-04 | 6 |

_Orphaned ledger detail omitted (568 rows) — see note above on historical lot_id churn._

## State/ledger mismatches

- `045821cefc9e`
- `20addddd5b5b`
- `2a95b347a326`
- `2f9855601404`
- `30e1a418b4d0`
- `386e50011c4e`
- `3e0808dbfba9`
- `5a7ea7321ee6`
- `691e2fc7cf96`
- `6aad0d189f53`
- `793e32a81719`
- `81dff7a0cdaa`
- `91db69b8d92a`
- `9d259cddf764`
- `a2fa8f3b4dd3`
- `c4f90da7a9e6`
- `d99d441afdf1`
- `e4b3d8271b9e`
- `ee5d5b326132`
- `eeeb7d626317`
- `f54dcd5bc3db`
