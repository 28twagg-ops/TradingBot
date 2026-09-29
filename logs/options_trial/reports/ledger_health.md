# Ledger health — 2026-09-29

_Generated 2026-09-29T09:06:41.799525_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-21** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1619 | WARN |
| Missing exit records (post) |  1619 | WARN |
| State/ledger mismatches     |     5 | WARN |
| Total open lots             |   120 | INFO |
| Total closed lots           |  2587 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Notes:
- **Current stuck** = open in `lab_state.json` and older than stuck threshold (actionable).
- **Post-stable orphaned / missing exits** = actionable WARN (entry_date > 2026-07-21).
- **Pre-cutoff debt** = entry_date < 2026-07-06 (INFO).
- **Transition debt** = 2026-07-06..2026-07-21 lot_id churn after attribution fix (INFO, not WARN).

_Orphaned ledger detail omitted (1619 rows) — see note above on historical lot_id churn._

## State/ledger mismatches

- `2a6c4c357293`
- `9f14bd1ab822`
- `af2fd2ff7b37`
- `c0a8c9e7ada3`
- `d8483095b2ce`
