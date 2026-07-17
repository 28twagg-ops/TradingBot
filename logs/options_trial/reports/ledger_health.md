# Ledger health — 2026-07-17

_Generated 2026-07-17T17:16:50.420432_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

State file: OK

| Check                 | Count | Status |
|-----------------------|------:|--------|
| Current stuck (state) |     0 | OK |
| Orphaned lots (ledger)|   589 | WARN |
| State/ledger mismat   |     0 | OK |
| Missing exit records  |   589 | WARN |
| Total open lots       |     0 | INFO |
| Total closed lots     |   264 | INFO |

Notes:
- **Current stuck** = open in `lab_state.json` and older than stuck threshold (actionable).
- **Orphaned lots / missing exits** = deduped ledger entries with no matching exit (by lot_id or bucket|strategy|occ). High counts often reflect pre-2026-07-07 optimistic logging / lot_id churn — treat as audit debt, not necessarily live stuck risk, when current stuck = 0.

_Orphaned ledger detail omitted (589 rows) — see note above on historical lot_id churn._
