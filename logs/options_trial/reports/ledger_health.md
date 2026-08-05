# Ledger health — 2026-08-05

_Generated 2026-08-05T11:22:10.639257_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-21** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   398 | WARN |
| Missing exit records (post) |   398 | WARN |
| State/ledger mismatches     |    27 | WARN |
| Total open lots             |   214 | INFO |
| Total closed lots           |   972 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Notes:
- **Current stuck** = open in `lab_state.json` and older than stuck threshold (actionable).
- **Post-stable orphaned / missing exits** = actionable WARN (entry_date > 2026-07-21).
- **Pre-cutoff debt** = entry_date < 2026-07-06 (INFO).
- **Transition debt** = 2026-07-06..2026-07-21 lot_id churn after attribution fix (INFO, not WARN).

_Orphaned ledger detail omitted (398 rows) — see note above on historical lot_id churn._

## State/ledger mismatches

- `0adb674f0c2e`
- `26fc7a2fb9fb`
- `3f7e5b0c90d8`
- `59e18c93befa`
- `5b329fe269db`
- `5d5665f8a6e5`
- `60eed4f3f8b3`
- `6f4e3a71d5ba`
- `8b8d5e1709a5`
- `962eb7cc2d81`
- `a683fbfa29fd`
- `aebe2c4bfaab`
- `b3b3a7d5d9b9`
- `b71c12996f02`
- `c387b139cf3b`
- `c551f66c55fd`
- `cadd6ad670df`
- `cf41646da57d`
- `d54e7ee8857a`
- `d6aea67fb831`
- `dac2b7ad39e8`
- `dcfddf04605b`
- `e46b69a4b8b6`
- `ed842d376f58`
- `f13086768076`
- `f524ece89be2`
- `ffd5731b2a5e`
