# Ledger health — 2026-09-04

_Generated 2026-09-04T11:13:11.916441_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-21** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   981 | WARN |
| Missing exit records (post) |   981 | WARN |
| State/ledger mismatches     |     9 | WARN |
| Total open lots             |   141 | INFO |
| Total closed lots           |  1988 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Notes:
- **Current stuck** = open in `lab_state.json` and older than stuck threshold (actionable).
- **Post-stable orphaned / missing exits** = actionable WARN (entry_date > 2026-07-21).
- **Pre-cutoff debt** = entry_date < 2026-07-06 (INFO).
- **Transition debt** = 2026-07-06..2026-07-21 lot_id churn after attribution fix (INFO, not WARN).

_Orphaned ledger detail omitted (981 rows) — see note above on historical lot_id churn._

## State/ledger mismatches

- `0951f938de5f`
- `12a1c6cdba93`
- `19cb76754714`
- `6de284dc07d0`
- `79a2ba3ef76f`
- `8dacf16c9c03`
- `916c1acd528d`
- `c5231537b23c`
- `e47d5611f499`
