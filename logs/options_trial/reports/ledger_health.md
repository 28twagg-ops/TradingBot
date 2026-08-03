# Ledger health — 2026-08-03

_Generated 2026-08-03T19:40:50.526692_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-21** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   327 | WARN |
| Missing exit records (post) |   327 | WARN |
| State/ledger mismatches     |     6 | WARN |
| Total open lots             |   123 | INFO |
| Total closed lots           |   497 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Notes:
- **Current stuck** = open in `lab_state.json` and older than stuck threshold (actionable).
- **Post-stable orphaned / missing exits** = actionable WARN (entry_date > 2026-07-21).
- **Pre-cutoff debt** = entry_date < 2026-07-06 (INFO).
- **Transition debt** = 2026-07-06..2026-07-21 lot_id churn after attribution fix (INFO, not WARN).

_Orphaned ledger detail omitted (327 rows) — see note above on historical lot_id churn._

## State/ledger mismatches

- `0770a14994f9`
- `6bf6903202cc`
- `8a36990fcb80`
- `8b5eee0f63fc`
- `8ba4640b8e94`
- `b199916177cf`
