# Ledger health — 2026-07-24

_Generated 2026-07-24T19:15:48.754253_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-18** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |     0 | OK |
| Missing exit records (post) |     0 | OK |
| State/ledger mismatches     |     1 | WARN |
| Total open lots             |     1 | INFO |
| Total closed lots           |   318 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   634 | INFO |

Notes:
- **Current stuck** = open in `lab_state.json` and older than stuck threshold (actionable).
- **Post-stable orphaned / missing exits** = actionable WARN (entry_date > 2026-07-18).
- **Pre-cutoff debt** = entry_date < 2026-07-06 (INFO).
- **Transition debt** = 2026-07-06..2026-07-18 lot_id churn after attribution fix (INFO, not WARN).

## State/ledger mismatches

- `c9de8fab1b0c`
