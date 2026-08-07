# Ledger health — 2026-08-07

_Generated 2026-08-07T16:15:56.069382_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-21** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   436 | WARN |
| Missing exit records (post) |   436 | WARN |
| State/ledger mismatches     |     9 | WARN |
| Total open lots             |   103 | INFO |
| Total closed lots           |  1355 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Notes:
- **Current stuck** = open in `lab_state.json` and older than stuck threshold (actionable).
- **Post-stable orphaned / missing exits** = actionable WARN (entry_date > 2026-07-21).
- **Pre-cutoff debt** = entry_date < 2026-07-06 (INFO).
- **Transition debt** = 2026-07-06..2026-07-21 lot_id churn after attribution fix (INFO, not WARN).

_Orphaned ledger detail omitted (436 rows) — see note above on historical lot_id churn._

## State/ledger mismatches

- `142e9b02da30`
- `73c96cca589b`
- `868bc0f793a1`
- `98c85151b5d5`
- `c4246c1e298e`
- `c947ffbe44d7`
- `d9405712a08f`
- `e4f72e015884`
- `fde0a1e3bcd5`
