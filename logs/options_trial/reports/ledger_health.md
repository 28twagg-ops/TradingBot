# Ledger health — 2026-07-21

_Generated 2026-07-21T10:11:31.924526_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-10** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |    27 | WARN |
| Missing exit records (post) |    27 | WARN |
| State/ledger mismatches     |     1 | WARN |
| Total open lots             |    25 | INFO |
| Total closed lots           |   295 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Notes:
- **Current stuck** = open in `lab_state.json` and older than stuck threshold (actionable).
- **Post-stable orphaned / missing exits** = actionable WARN (entry_date > 2026-07-10).
- **Pre-cutoff debt** = entry_date < 2026-07-06 (INFO).
- **Transition debt** = 2026-07-06..2026-07-10 lot_id churn after attribution fix (INFO, not WARN).

## Orphaned ledger entries (detail)

| lot_id | strategy | symbol | entry_day | age_days |
|--------|----------|--------|-----------|---------:|
| 69035bbe54ed | S165 | INTC | 2026-07-13 | 8 |
| acd35e3d9d37 | S165 | INTC | 2026-07-13 | 8 |
| 7e3efbcbee4d | S165 | INTC | 2026-07-13 | 8 |
| 315408291e9d | S173 | SMCI | 2026-07-13 | 8 |
| 81cbb1d143b4 | S173 | SMCI | 2026-07-13 | 8 |
| c7c921ac55b3 | S173 | SMCI | 2026-07-13 | 8 |
| 9499278895a8 | S173 | SMCI | 2026-07-13 | 8 |
| 7a915749c7e3 | S173 | AMD | 2026-07-13 | 8 |
| e5e4a424e123 | S173 | AMD | 2026-07-13 | 8 |
| 9ab08bd47c31 | S174 | AVGO | 2026-07-13 | 8 |
| 0299cfa5bb54 | S165 | HL | 2026-07-13 | 8 |
| 5e6fb2e3314a | S165 | HL | 2026-07-13 | 8 |
| 1a9aa13a72c1 | S173 | AMD | 2026-07-13 | 8 |
| 174fad3a5c93 | S173 | AMD | 2026-07-13 | 8 |
| 82b23daf2111 | S173 | AMD | 2026-07-13 | 8 |
| 43108024132f | S173 | AMD | 2026-07-13 | 8 |
| 8e079ecd2e01 | S173 | AMD | 2026-07-13 | 8 |
| 2920355fb151 | S174 | INTC | 2026-07-13 | 8 |
| d8cb3a147256 | S165 | MSFT | 2026-07-14 | 7 |
| cb00cab142e1 | S165 | MSFT | 2026-07-14 | 7 |
| 2eb176a920da | S165 | MSFT | 2026-07-14 | 7 |
| 209ba9a3f92d | S173 | C | 2026-07-14 | 7 |
| e8006feddd99 | S165 | BSX | 2026-07-14 | 7 |
| c2de9fef4808 | S173 | ADBE | 2026-07-14 | 7 |
| b61c999df2a7 | S173 | C | 2026-07-14 | 7 |
| 9603ff1aa615 | S173 | ADBE | 2026-07-14 | 7 |
| b805b2e81e9c | S173 | ADBE | 2026-07-14 | 7 |

## State/ledger mismatches

- `b53732631165`
