# Ledger health — 2026-08-05

_Generated 2026-08-05T11:17:13.528441_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-21** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   398 | WARN |
| Missing exit records (post) |   398 | WARN |
| State/ledger mismatches     |    22 | WARN |
| Total open lots             |   200 | INFO |
| Total closed lots           |   928 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Notes:
- **Current stuck** = open in `lab_state.json` and older than stuck threshold (actionable).
- **Post-stable orphaned / missing exits** = actionable WARN (entry_date > 2026-07-21).
- **Pre-cutoff debt** = entry_date < 2026-07-06 (INFO).
- **Transition debt** = 2026-07-06..2026-07-21 lot_id churn after attribution fix (INFO, not WARN).

_Orphaned ledger detail omitted (398 rows) — see note above on historical lot_id churn._

## State/ledger mismatches

- `0102b4dca14c`
- `02e57b73f915`
- `0adb674f0c2e`
- `2d532049644b`
- `35401108af20`
- `4a3ae8885cf7`
- `559312936171`
- `5a08097f184a`
- `60eed4f3f8b3`
- `6f4e3a71d5ba`
- `98c373defc46`
- `9f4d46aee31c`
- `a683fbfa29fd`
- `aeb8367af49e`
- `aebe2c4bfaab`
- `b71c12996f02`
- `b7fd1c304233`
- `c551f66c55fd`
- `d54e7ee8857a`
- `dac2b7ad39e8`
- `f13086768076`
- `fb7736922ef3`
