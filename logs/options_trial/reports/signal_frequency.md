# Options signal frequency

_Generated 2026-07-17T17:23:02.229761_

Headline counts are **unique (strategy, underlying, date)** from `ENTRY` lines in `logs/options_trial/runs/*.log`.
Raw log-line counts (multi-bucket duplicates) are shown below for debug.

### Unique underlying symbols per day (headline)

| Date       | S163 | S165 | S166 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-08 |    0 |    3 |    0 |    2 |    1 |     6 |
| 2026-07-09 |    0 |    1 |    0 |    2 |    3 |     6 |
| 2026-07-10 |    0 |    1 |    0 |    1 |    1 |     3 |
| 2026-07-13 |    0 |    2 |    0 |    3 |    2 |     7 |
| 2026-07-14 |    0 |    3 |    0 |    2 |    0 |     5 |
| 2026-07-16 |    0 |    2 |    0 |    3 |    0 |     5 |
| 2026-07-17 |    0 |    2 |    0 |    2 |    0 |     4 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S165 | 14 | 7 | 2.0 | ~19 active signal-days |
| S166 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S173 | 16 | 8 | 2.0 | ~19 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 0 | 0 |
| S165 | 1202 | 14 |
| S166 | 0 | 0 |
| S173 | 1493 | 16 |
| S174 | 785 | 7 |

### Raw log lines per day (debug / multi-bucket)

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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.
