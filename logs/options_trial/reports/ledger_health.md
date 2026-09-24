# Ledger health — 2026-09-24

_Generated 2026-09-24T19:46:36.384857_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-21** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1578 | WARN |
| Missing exit records (post) |  1578 | WARN |
| State/ledger mismatches     |     3 | WARN |
| Total open lots             |    55 | INFO |
| Total closed lots           |  2511 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Notes:
- **Current stuck** = open in `lab_state.json` and older than stuck threshold (actionable).
- **Post-stable orphaned / missing exits** = actionable WARN (entry_date > 2026-07-21).
- **Pre-cutoff debt** = entry_date < 2026-07-06 (INFO).
- **Transition debt** = 2026-07-06..2026-07-21 lot_id churn after attribution fix (INFO, not WARN).

_Orphaned ledger detail omitted (1578 rows) — see note above on historical lot_id churn._

## State/ledger mismatches

- `05d99f7f477c`
- `52ec4353653c`
- `b11f80ab93c8`
