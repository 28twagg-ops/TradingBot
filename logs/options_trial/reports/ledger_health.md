# Ledger health — 2026-08-04

_Generated 2026-08-04T10:18:48.167279_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-21** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   398 | WARN |
| Missing exit records (post) |   398 | WARN |
| State/ledger mismatches     |    15 | WARN |
| Total open lots             |   118 | INFO |
| Total closed lots           |   614 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Notes:
- **Current stuck** = open in `lab_state.json` and older than stuck threshold (actionable).
- **Post-stable orphaned / missing exits** = actionable WARN (entry_date > 2026-07-21).
- **Pre-cutoff debt** = entry_date < 2026-07-06 (INFO).
- **Transition debt** = 2026-07-06..2026-07-21 lot_id churn after attribution fix (INFO, not WARN).

_Orphaned ledger detail omitted (398 rows) — see note above on historical lot_id churn._

## State/ledger mismatches

- `07fa43b3866a`
- `08e61418ce64`
- `0c584fe065e9`
- `13728602d6ed`
- `19ebe810b50a`
- `26d74a34f7a0`
- `2a58900fb3d5`
- `3d7465f2cd3f`
- `561a1dd48870`
- `5af5b331b1b5`
- `66b29fe16dc9`
- `74e317c0f6d7`
- `7dc04ebf1e31`
- `91bee9a87674`
- `f39886287555`
