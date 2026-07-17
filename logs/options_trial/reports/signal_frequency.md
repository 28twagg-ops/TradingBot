# Options signal frequency

_Generated 2026-07-17T17:15:41.762349_

Counts are unique ENTRY events from `logs/options_trial/runs/*.log` (deduped by pending/order id when present).

| Date       | S163 | S165 | S166 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |  100 |    0 |   100 |
| 2026-07-08 |    0 |  100 |    0 |  100 |  100 |   300 |
| 2026-07-09 |    0 |   24 |    0 |  100 |   15 |   139 |
| 2026-07-10 |    0 |  242 |    0 |  230 |  202 |   674 |
| 2026-07-13 |    0 |  190 |    0 |  212 |  188 |   590 |
| 2026-07-14 |    0 |  194 |    0 |  185 |  106 |   485 |
| 2026-07-15 |    0 |  146 |    0 |  154 |   58 |   358 |
| 2026-07-16 |    0 |  179 |    0 |  205 |   58 |   442 |
| 2026-07-17 |    0 |  127 |    0 |  207 |   58 |   392 |

## Per-strategy summary

| Strategy | Total entries | Active days | Avg / active day | Est. days to n=30 exits* |
|----------|--------------:|------------:|-----------------:|--------------------------|
| S163 | 0 | 0 | 0.0 | inf (no entries yet) |
| S165 | 1202 | 8 | 150.2 | 0 (proxy already >=30 exits) |
| S166 | 0 | 0 | 0.0 | inf (no entries yet) |
| S173 | 1493 | 9 | 165.9 | 0 (proxy already >=30 exits) |
| S174 | 785 | 8 | 98.1 | 0 (proxy already >=30 exits) |

\* Proxy assumes 60% of entries become exits; target = 30 exits. Update when real exit rates are known.

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved by one-hit-per-symbol priority — expect zeros until fix is live.
- Controlled layout places one ENTRY per matching bucket×strategy, so a single gap-down symbol can produce many ENTRY rows for S165 (etc.).
