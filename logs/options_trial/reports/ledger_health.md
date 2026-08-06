# Ledger health — 2026-08-06

_Generated 2026-08-06T09:25:53.563781_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-21** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN |
| Orphaned lots (post-stable) |   442 | WARN |
| Missing exit records (post) |   438 | WARN |
| State/ledger mismatches     |    15 | WARN |
| Total open lots             |   156 | INFO |
| Total closed lots           |  1013 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Notes:
- **Current stuck** = open in `lab_state.json` and older than stuck threshold (actionable).
- **Post-stable orphaned / missing exits** = actionable WARN (entry_date > 2026-07-21).
- **Pre-cutoff debt** = entry_date < 2026-07-06 (INFO).
- **Transition debt** = 2026-07-06..2026-07-21 lot_id churn after attribution fix (INFO, not WARN).

## Current stuck lots

| lot_id | strategy | symbol | entry_day | age_days |
|--------|----------|--------|-----------|---------:|
| 9c83f89cabf4 | S365 | AAPL | 2026-07-31 | 6 |
| b428605e4e35 | S365 | AAPL | 2026-07-31 | 6 |

_Orphaned ledger detail omitted (442 rows) — see note above on historical lot_id churn._

## State/ledger mismatches

- `0bc0036ed544`
- `26fc7a2fb9fb`
- `3e7dfb848853`
- `3f7e5b0c90d8`
- `5d5665f8a6e5`
- `76d0456de795`
- `783d3a132699`
- `7933dacc805b`
- `9632933efada`
- `a20b38ca248c`
- `b3b3a7d5d9b9`
- `bf3778e37063`
- `d9aca5ba1264`
- `e46b69a4b8b6`
- `ffafb5bd5850`
