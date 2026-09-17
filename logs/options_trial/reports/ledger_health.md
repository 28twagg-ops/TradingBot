# Ledger health — 2026-09-17

_Generated 2026-09-17T12:01:34.720972_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-21** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    16 | WARN |
| Orphaned lots (post-stable) |  1381 | WARN |
| Missing exit records (post) |  1365 | WARN |
| State/ledger mismatches     |     5 | WARN |
| Total open lots             |   104 | INFO |
| Total closed lots           |  2306 | INFO |
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
| c749b9facdbb | S366 | MARA | 2026-09-04 | 13 |
| 53ee58608a69 | S366 | MARA | 2026-09-04 | 13 |
| 01aab77eeb4e | S366 | MARA | 2026-09-04 | 13 |
| 1d35d0a01344 | S168 | MARA | 2026-09-10 | 7 |
| e73eb3e30d6b | S364 | MARA | 2026-09-10 | 7 |
| c1a721f76ba9 | S364 | MARA | 2026-09-10 | 7 |
| feea057e1edc | S363 | MARA | 2026-09-10 | 7 |
| 9156fd2e7a3e | S363 | MARA | 2026-09-10 | 7 |
| ba53ee1b2b17 | S355 | MARA | 2026-09-10 | 7 |
| 5bb5c291f4c5 | S355 | MARA | 2026-09-10 | 7 |
| 2f8f3b3c1da0 | S354 | MARA | 2026-09-10 | 7 |
| aede53d9d451 | S354 | MARA | 2026-09-10 | 7 |
| b7f46a6ed532 | S163 | MARA | 2026-09-10 | 7 |
| 7772468d72fe | S163 | MARA | 2026-09-10 | 7 |
| b7a0810f1625 | S168 | MARA | 2026-09-10 | 7 |
| af2fd15cfdcf | S168 | MARA | 2026-09-10 | 7 |

_Orphaned ledger detail omitted (1381 rows) — see note above on historical lot_id churn._

## State/ledger mismatches

- `1d79395b7a8c`
- `4ad03a11d251`
- `92d6ead45f7f`
- `b9db7b073077`
- `f27a6711e93e`
