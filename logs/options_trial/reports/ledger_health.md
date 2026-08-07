# Ledger health — 2026-08-07

_Generated 2026-08-07T10:32:35.024633_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-21** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   438 | WARN |
| Missing exit records (post) |   436 | WARN |
| State/ledger mismatches     |    14 | WARN |
| Total open lots             |   112 | INFO |
| Total closed lots           |  1296 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Notes:
- **Current stuck** = open in `lab_state.json` and older than stuck threshold (actionable).
- **Post-stable orphaned / missing exits** = actionable WARN (entry_date > 2026-07-21).
- **Pre-cutoff debt** = entry_date < 2026-07-06 (INFO).
- **Transition debt** = 2026-07-06..2026-07-21 lot_id churn after attribution fix (INFO, not WARN).

_Orphaned ledger detail omitted (438 rows) — see note above on historical lot_id churn._

## State/ledger mismatches

- `000575419aa8`
- `00b293cdf648`
- `0462acb9348d`
- `1103b26ba819`
- `3624e7324a17`
- `3ebc37036f3f`
- `74f0b4f4bbf4`
- `81fef23e5e21`
- `9a4d8495dd2d`
- `a1a90a8a2dfe`
- `a30cd3dd8688`
- `da9784e57ebf`
- `e431635713d5`
- `f13430e1150b`
