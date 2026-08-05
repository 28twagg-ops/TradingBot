# Ledger health — 2026-08-05

_Generated 2026-08-05T12:26:01.669344_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-21** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   398 | WARN |
| Missing exit records (post) |   398 | WARN |
| State/ledger mismatches     |    23 | WARN |
| Total open lots             |   208 | INFO |
| Total closed lots           |   997 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Notes:
- **Current stuck** = open in `lab_state.json` and older than stuck threshold (actionable).
- **Post-stable orphaned / missing exits** = actionable WARN (entry_date > 2026-07-21).
- **Pre-cutoff debt** = entry_date < 2026-07-06 (INFO).
- **Transition debt** = 2026-07-06..2026-07-21 lot_id churn after attribution fix (INFO, not WARN).

_Orphaned ledger detail omitted (398 rows) — see note above on historical lot_id churn._

## State/ledger mismatches

- `0bc0036ed544`
- `26fc7a2fb9fb`
- `2f819c4fba81`
- `3e7dfb848853`
- `3f7e5b0c90d8`
- `59e18c93befa`
- `5b329fe269db`
- `5d5665f8a6e5`
- `6dbf70e9c876`
- `76d0456de795`
- `962eb7cc2d81`
- `9632933efada`
- `a683fbfa29fd`
- `aebe2c4bfaab`
- `b3b3a7d5d9b9`
- `bf3778e37063`
- `cc4b9f78309e`
- `ce16ef5a17e7`
- `cf41646da57d`
- `d54e7ee8857a`
- `e46b69a4b8b6`
- `e973b5f32bc2`
- `ffd5731b2a5e`
