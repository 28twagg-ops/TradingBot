# Ledger health — 2026-08-05

_Generated 2026-08-05T11:02:55.981851_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-21** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   398 | WARN |
| Missing exit records (post) |   398 | WARN |
| State/ledger mismatches     |    23 | WARN |
| Total open lots             |   185 | INFO |
| Total closed lots           |   905 | INFO |
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
- `2e511f3bcd0a`
- `35401108af20`
- `438388bc0279`
- `4785c9111856`
- `4a3ae8885cf7`
- `559312936171`
- `5a08097f184a`
- `673464e455cf`
- `91bf17015c5c`
- `a68521265472`
- `aeb8367af49e`
- `b7fd1c304233`
- `c551f66c55fd`
- `ccbd8e464153`
- `cfa4d292342e`
- `d1bd4bc5ed4c`
- `dfcf7d4d0605`
- `e685f68d9235`
- `eed01dfb242c`
- `fb7736922ef3`
