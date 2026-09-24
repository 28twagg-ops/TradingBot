# Ledger health — 2026-09-24

_Generated 2026-09-24T10:13:27.391617_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-21** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN |
| Orphaned lots (post-stable) |  1580 | WARN |
| Missing exit records (post) |  1578 | WARN |
| State/ledger mismatches     |     5 | WARN |
| Total open lots             |   113 | INFO |
| Total closed lots           |  2435 | INFO |
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
| 53ee58608a69 | S366 | MARA | 2026-09-04 | 20 |
| 01aab77eeb4e | S366 | MARA | 2026-09-04 | 20 |

_Orphaned ledger detail omitted (1580 rows) — see note above on historical lot_id churn._

## State/ledger mismatches

- `33540ce5b718`
- `46533a25f6fc`
- `90ceb5261d18`
- `b5676237bf5c`
- `ca4efb952018`
