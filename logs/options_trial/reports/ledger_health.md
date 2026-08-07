# Ledger health — 2026-08-07

_Generated 2026-08-07T11:12:27.029920_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-21** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   438 | WARN |
| Missing exit records (post) |   436 | WARN |
| State/ledger mismatches     |    14 | WARN |
| Total open lots             |   121 | INFO |
| Total closed lots           |  1322 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Notes:
- **Current stuck** = open in `lab_state.json` and older than stuck threshold (actionable).
- **Post-stable orphaned / missing exits** = actionable WARN (entry_date > 2026-07-21).
- **Pre-cutoff debt** = entry_date < 2026-07-06 (INFO).
- **Transition debt** = 2026-07-06..2026-07-21 lot_id churn after attribution fix (INFO, not WARN).

_Orphaned ledger detail omitted (438 rows) — see note above on historical lot_id churn._

## State/ledger mismatches

- `00b293cdf648`
- `010fc7ab0949`
- `09cf69544a1d`
- `1103b26ba819`
- `127ebe228045`
- `273676403b81`
- `4a86fbdb882c`
- `68a8e08a4381`
- `7fefc4d59ab4`
- `98c85151b5d5`
- `a30cd3dd8688`
- `e431635713d5`
- `e4f72e015884`
- `f13430e1150b`
