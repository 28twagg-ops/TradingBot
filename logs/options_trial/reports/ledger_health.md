# Ledger health — 2026-08-12

_Generated 2026-08-12T18:31:09.043818_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-21** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   650 | WARN |
| Missing exit records (post) |   650 | WARN |
| State/ledger mismatches     |    28 | WARN |
| Total open lots             |    28 | INFO |
| Total closed lots           |  1713 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Notes:
- **Current stuck** = open in `lab_state.json` and older than stuck threshold (actionable).
- **Post-stable orphaned / missing exits** = actionable WARN (entry_date > 2026-07-21).
- **Pre-cutoff debt** = entry_date < 2026-07-06 (INFO).
- **Transition debt** = 2026-07-06..2026-07-21 lot_id churn after attribution fix (INFO, not WARN).

_Orphaned ledger detail omitted (650 rows) — see note above on historical lot_id churn._

## State/ledger mismatches

- `0f0fa5807ed9`
- `1610a4cdc0f8`
- `1831a297dc54`
- `2bf8b0ff780b`
- `2f2b17aaee89`
- `312dbb345131`
- `3136bb093710`
- `36b3780de9ce`
- `4387ab24b863`
- `4798ec8c5dee`
- `55847465121c`
- `5db59d4ad10f`
- `627a5a664b23`
- `86dc55b5e6b2`
- `8c94dd36ec8c`
- `9ba33c476e7d`
- `b66f72cd77c7`
- `bf641e7d4ac0`
- `c5d9e45968f6`
- `cd5fda708821`
- `cde751fca66a`
- `ce546f7d0974`
- `d275f8f8fa7f`
- `d9953782f360`
- `e480c540b6a2`
- `ecfa71c9e427`
- `f10eefde8e5b`
- `f1fb0156ca1f`
