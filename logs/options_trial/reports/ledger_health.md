# Ledger health — 2026-08-10

_Generated 2026-08-10T16:01:34.832144_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-21** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   560 | WARN |
| Missing exit records (post) |   560 | WARN |
| State/ledger mismatches     |    16 | WARN |
| Total open lots             |   142 | INFO |
| Total closed lots           |  1525 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Notes:
- **Current stuck** = open in `lab_state.json` and older than stuck threshold (actionable).
- **Post-stable orphaned / missing exits** = actionable WARN (entry_date > 2026-07-21).
- **Pre-cutoff debt** = entry_date < 2026-07-06 (INFO).
- **Transition debt** = 2026-07-06..2026-07-21 lot_id churn after attribution fix (INFO, not WARN).

_Orphaned ledger detail omitted (560 rows) — see note above on historical lot_id churn._

## State/ledger mismatches

- `20addddd5b5b`
- `2a95b347a326`
- `2ae58f33d7ad`
- `30e1a418b4d0`
- `3e0808dbfba9`
- `691e2fc7cf96`
- `755c5aa2f481`
- `91db69b8d92a`
- `9d259cddf764`
- `a2fa8f3b4dd3`
- `c4f90da7a9e6`
- `c87a043e6603`
- `d99d441afdf1`
- `e4b3d8271b9e`
- `ee5d5b326132`
- `faac7c12cb7a`
