# Ledger health — 2026-08-13

_Generated 2026-08-13T10:22:43.570190_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-21** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   678 | WARN |
| Missing exit records (post) |   678 | WARN |
| State/ledger mismatches     |    12 | WARN |
| Total open lots             |    46 | INFO |
| Total closed lots           |  1722 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Notes:
- **Current stuck** = open in `lab_state.json` and older than stuck threshold (actionable).
- **Post-stable orphaned / missing exits** = actionable WARN (entry_date > 2026-07-21).
- **Pre-cutoff debt** = entry_date < 2026-07-06 (INFO).
- **Transition debt** = 2026-07-06..2026-07-21 lot_id churn after attribution fix (INFO, not WARN).

_Orphaned ledger detail omitted (678 rows) — see note above on historical lot_id churn._

## State/ledger mismatches

- `01168fbc0684`
- `1831a297dc54`
- `55847465121c`
- `8a83de94d864`
- `9095bc323183`
- `9290a2eb6691`
- `a36e55628cd8`
- `a6e4228a9ab5`
- `b66f72cd77c7`
- `cf24d5485a11`
- `de4d441c0162`
- `e80fc83a43e3`
