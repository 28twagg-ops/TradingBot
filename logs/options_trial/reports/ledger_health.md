# Ledger health — 2026-08-04

_Generated 2026-08-04T10:15:21.485832_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-21** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   398 | WARN |
| Missing exit records (post) |   398 | WARN |
| State/ledger mismatches     |    14 | WARN |
| Total open lots             |   106 | INFO |
| Total closed lots           |   607 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Notes:
- **Current stuck** = open in `lab_state.json` and older than stuck threshold (actionable).
- **Post-stable orphaned / missing exits** = actionable WARN (entry_date > 2026-07-21).
- **Pre-cutoff debt** = entry_date < 2026-07-06 (INFO).
- **Transition debt** = 2026-07-06..2026-07-21 lot_id churn after attribution fix (INFO, not WARN).

_Orphaned ledger detail omitted (398 rows) — see note above on historical lot_id churn._

## State/ledger mismatches

- `08e61418ce64`
- `0a19d46b078c`
- `109f59686947`
- `17c66c638f44`
- `192f392808ef`
- `20dd2a3b2261`
- `28928379934a`
- `34348a5389a5`
- `3d7465f2cd3f`
- `5af5b331b1b5`
- `69daa7dd0ec8`
- `726d445aef1a`
- `8e018ae87e2e`
- `ab41ae7b235b`
