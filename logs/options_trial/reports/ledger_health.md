# Ledger health — 2026-09-25

_Generated 2026-09-25T10:48:39.039688_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-21** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1578 | WARN |
| Missing exit records (post) |  1578 | WARN |
| State/ledger mismatches     |     8 | WARN |
| Total open lots             |    89 | INFO |
| Total closed lots           |  2527 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Notes:
- **Current stuck** = open in `lab_state.json` and older than stuck threshold (actionable).
- **Post-stable orphaned / missing exits** = actionable WARN (entry_date > 2026-07-21).
- **Pre-cutoff debt** = entry_date < 2026-07-06 (INFO).
- **Transition debt** = 2026-07-06..2026-07-21 lot_id churn after attribution fix (INFO, not WARN).

_Orphaned ledger detail omitted (1578 rows) — see note above on historical lot_id churn._

## State/ledger mismatches

- `3ec384e8a37a`
- `52ec4353653c`
- `5565e4b07070`
- `6024024bf49c`
- `7b0f4512fef7`
- `bee0378ecd6b`
- `c20ee5e2ba19`
- `f650f37b78cb`
