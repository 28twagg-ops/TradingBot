# Ledger health — 2026-07-22

_Generated 2026-07-22T19:15:43.355339_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-15** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |     7 | WARN |
| Missing exit records (post) |     7 | WARN |
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |   313 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   616 | INFO |

Notes:
- **Current stuck** = open in `lab_state.json` and older than stuck threshold (actionable).
- **Post-stable orphaned / missing exits** = actionable WARN (entry_date > 2026-07-15).
- **Pre-cutoff debt** = entry_date < 2026-07-06 (INFO).
- **Transition debt** = 2026-07-06..2026-07-15 lot_id churn after attribution fix (INFO, not WARN).

## Orphaned ledger entries (detail)

| lot_id | strategy | symbol | entry_day | age_days |
|--------|----------|--------|-----------|---------:|
| fe6b46fa00bb | S165 | AVGO | 2026-07-16 | 6 |
| 7385dc02b472 | S173 | UAL | 2026-07-16 | 6 |
| 5b2b4313830f | S173 | UAL | 2026-07-16 | 6 |
| f09b7de85a3f | S173 | AMD | 2026-07-16 | 6 |
| 78970860d223 | S165 | AVGO | 2026-07-16 | 6 |
| cfe20e4c43c8 | S165 | AVGO | 2026-07-16 | 6 |
| 30f0bcea133d | S173 | LULU | 2026-07-16 | 6 |
