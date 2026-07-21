# Ledger health — 2026-07-21

_Generated 2026-07-21T11:22:57.525041_

Stuck threshold: **>5** days (EXIT_DAYS_MAX=3 + buffer=2).

Baseline cutoff: **2026-07-06** (attribution fix start). WARN only after **2026-07-10** (ledger pairing stabilized); earlier unmatched entries = INFO debt.

State file: OK

| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |    27 | WARN |
| Missing exit records (post) |    27 | WARN |
| State/ledger mismatches     |    30 | WARN |
| Total open lots             |    30 | INFO |
| Total closed lots           |   297 | INFO |
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
| a8a364c27e2b | S165 | INTC | 2026-07-13 | 8 |
| fea6f59b4576 | S165 | INTC | 2026-07-13 | 8 |
| 20f6dd8f935e | S165 | INTC | 2026-07-13 | 8 |
| bffad83bd6a6 | S173 | SMCI | 2026-07-13 | 8 |
| 3f1c0275410e | S173 | SMCI | 2026-07-13 | 8 |
| 5cdaec986f88 | S173 | SMCI | 2026-07-13 | 8 |
| 993f34c7eff2 | S173 | SMCI | 2026-07-13 | 8 |
| 819501ade1ea | S173 | AMD | 2026-07-13 | 8 |
| 121a6c9d5160 | S173 | AMD | 2026-07-13 | 8 |
| 91f442f0000a | S174 | AVGO | 2026-07-13 | 8 |
| 27f8dbd57340 | S165 | HL | 2026-07-13 | 8 |
| 12d4f197f284 | S165 | HL | 2026-07-13 | 8 |
| 814f098bda69 | S173 | AMD | 2026-07-13 | 8 |
| b08fec0015fc | S173 | AMD | 2026-07-13 | 8 |
| 12d3c7762150 | S173 | AMD | 2026-07-13 | 8 |
| 4bd98a5d7c45 | S173 | AMD | 2026-07-13 | 8 |
| b1d50a632be9 | S173 | AMD | 2026-07-13 | 8 |
| 2e1bd966ddc0 | S174 | INTC | 2026-07-13 | 8 |
| d8cb3a147256 | S165 | MSFT | 2026-07-14 | 7 |
| cb00cab142e1 | S165 | MSFT | 2026-07-14 | 7 |
| 2eb176a920da | S165 | MSFT | 2026-07-14 | 7 |
| 209ba9a3f92d | S173 | C | 2026-07-14 | 7 |
| e8006feddd99 | S165 | BSX | 2026-07-14 | 7 |
| 426df5f21f1c | S173 | ADBE | 2026-07-14 | 7 |
| b61c999df2a7 | S173 | C | 2026-07-14 | 7 |
| 9603ff1aa615 | S173 | ADBE | 2026-07-14 | 7 |
| b805b2e81e9c | S173 | ADBE | 2026-07-14 | 7 |

## State/ledger mismatches

- `0b1ca7898f4d`
- `1b36f1025eda`
- `21bc664a3cef`
- `24fabf75e17d`
- `2d5ae0f52a45`
- `3db8eb2e0d5a`
- `408dcf96ee1f`
- `56d88ece4ea6`
- `5b13996d4561`
- `632e6a96619f`
- `6fce6db38ca7`
- `712ec34a8563`
- `878ce77ae95d`
- `9489dd798edc`
- `a9e3c33304a4`
- `aa8342d4d47a`
- `b70874cb82ff`
- `ba9adbcef13e`
- `bd375639011e`
- `cb99c9ccef6d`
- `cda5464e2aa0`
- `d5f57d10982a`
- `d64118920ee1`
- `dd77316e8007`
- `e0246b1d378c`
- `e22e9b63f934`
- `e8ce2a68e6c0`
- `e9d9cb7d8787`
- `f1511f386894`
- `f9eec66da4e9`
