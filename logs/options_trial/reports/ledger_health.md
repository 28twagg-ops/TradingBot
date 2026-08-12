# Ledger health — 2026-08-12

_Generated 2026-08-12T15:21:02.188658_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-21** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   650 | WARN |
| Missing exit records (post) |   650 | WARN |
| State/ledger mismatches     |    11 | WARN |
| Total open lots             |   124 | INFO |
| Total closed lots           |  1711 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Notes:
- **Current stuck** = open in `lab_state.json` and older than stuck threshold (actionable).
- **Post-stable orphaned / missing exits** = actionable WARN (entry_date > 2026-07-21).
- **Pre-cutoff debt** = entry_date < 2026-07-06 (INFO).
- **Transition debt** = 2026-07-06..2026-07-21 lot_id churn after attribution fix (INFO, not WARN).

_Orphaned ledger detail omitted (650 rows) — see note above on historical lot_id churn._

## State/ledger mismatches

- `3491e15cc0a3`
- `8060eb83a3ad`
- `8544156a0d83`
- `ae5accf579ca`
- `b41b9b407de5`
- `be7f9da2ef94`
- `beddcf955269`
- `d7264a8a0cc9`
- `dde09b7a93eb`
- `ead1bd3a4580`
- `ef98f45c6e00`
