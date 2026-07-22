# Ledger health — 2026-07-22

_Generated 2026-07-22T11:34:40.901299_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-15** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |     7 | WARN |
| Missing exit records (post) |     7 | WARN |
| State/ledger mismatches     |    20 | WARN |
| Total open lots             |    20 | INFO |
| Total closed lots           |   304 | INFO |
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

## State/ledger mismatches

- `12951408fb24`
- `37625fdb7b95`
- `49abe66a7026`
- `50abf3bc7f57`
- `5ebb2f85cc60`
- `5ef30e8b670e`
- `6a85684977e4`
- `789360672f36`
- `99deb44db07f`
- `9f213e62eec7`
- `b6844940316c`
- `b7c015c58bbc`
- `bcd8912433cc`
- `cb23a55bb2e0`
- `cb4c4c1e54ce`
- `d36c0edea0f6`
- `ef45afeb2753`
- `f3df553cc57f`
- `f785a375a4ef`
- `f88888cf0de4`
