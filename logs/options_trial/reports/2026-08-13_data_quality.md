# Options data quality report - 2026-08-13

Splits ledger exits into **CLEAN** (natural TP/SL/EOD, healthy runtime) vs **TAINTED** (reconcile_fill / broker-missing / known GitHub outage days).
**KEEP-only** = CLEAN exits from strategies with n>=10, med>=0%, win>=50%.

## Headline

| Slice | n | Win% | Med% | Avg% | Realized $ |
|---|---:|---:|---:|---:|---:|
| ALL | 2517 | 35.9 | -41.1 | +10.9 | $-969 |
| CLEAN (perfect running) | 796 | 42.1 | -47.2 | +11.5 | $+7,959 |
| TAINTED (errors/outages) | 1721 | 33.1 | -38.8 | +10.6 | $-8,927 |
| CLEAN since 2026-08-03 | 480 | 31.2 | -51.8 | -4.8 | $-4,341 |
| KEEP-only (CLEAN keepers) | 302 | 63.6 | +37.7 | +42.1 | $+5,747 |
| KEEP-only since 2026-08-03 | 114 | 59.6 | +50.0 | +51.9 | $+1,721 |

## Known outage / degraded days

2026-08-01, 2026-08-06

## Daily exit health

| Day | Tag | n | reconcile-ish | Win% | Med% |
|---|---|---:|---:|---:|---:|
| 2026-07-06 | OK | 52 | 0 | 94 | +36.5 |
| 2026-07-10 | BUGGY | 163 | 123 | 32 | -21.7 |
| 2026-07-13 | BUGGY | 204 | 170 | 26 | -33.3 |
| 2026-07-14 | BUGGY | 98 | 78 | 30 | -21.8 |
| 2026-07-15 | BUGGY | 16 | 16 | 0 | -92.7 |
| 2026-07-16 | BUGGY | 156 | 120 | 13 | -57.5 |
| 2026-07-17 | BUGGY | 93 | 52 | 62 | +42.9 |
| 2026-07-20 | OK | 19 | 0 | 100 | +82.5 |
| 2026-07-22 | OK | 1 | 0 | 0 | -53.6 |
| 2026-07-24 | BUGGY | 5 | 1 | 0 | -77.8 |
| 2026-07-29 | BUGGY | 4 | 1 | 0 | -50.0 |
| 2026-07-31 | BUGGY | 145 | 79 | 76 | +63.6 |
| 2026-08-03 | BUGGY | 222 | 147 | 68 | +47.1 |
| 2026-08-04 | BUGGY | 254 | 193 | 49 | +0.0 |
| 2026-08-05 | BUGGY | 361 | 256 | 17 | -54.3 |
| 2026-08-06 | OUTAGE | 216 | 134 | 23 | -53.6 |
| 2026-08-07 | BUGGY | 230 | 160 | 28 | -59.7 |
| 2026-08-10 | BUGGY | 128 | 72 | 22 | -51.2 |
| 2026-08-11 | BUGGY | 89 | 34 | 25 | -53.0 |
| 2026-08-12 | BUGGY | 45 | 1 | 16 | -70.8 |
| 2026-08-13 | BUGGY | 16 | 2 | 38 | -60.8 |

## CLEAN strategy kill list (n>=10, med<=-20%)

| strategy | n | win% | med% | avg% | $ |
|---|---:|---:|---:|---:|---:|
| ORPHAN | 92 | 20.7 | -67.2 | -25.9 | $+3,786 |
| S212 | 17 | 5.9 | -66.1 | -64.2 | $-563 |
| S360 | 17 | 11.8 | -60.8 | -49.2 | $-371 |
| S203 | 11 | 0.0 | -58.2 | -60.9 | $-260 |
| S405 | 24 | 33.3 | -57.4 | -4.1 | $-38 |
| S407 | 10 | 40.0 | -57.0 | -5.4 | $-50 |
| S207 | 13 | 15.4 | -54.3 | -40.5 | $-341 |
| S217 | 17 | 35.3 | -52.9 | +84.9 | $+136 |
| S351 | 14 | 7.1 | -52.5 | -35.2 | $-110 |
| S355 | 24 | 33.3 | -51.5 | +15.6 | $+76 |
| S354 | 16 | 37.5 | -51.2 | +12.2 | $+46 |
| S364 | 14 | 42.9 | -50.7 | -14.7 | $-188 |
| S408 | 16 | 31.2 | -45.6 | +32.3 | $+45 |
| S211 | 11 | 36.4 | -45.5 | -12.3 | $-70 |
| S165 | 61 | 37.7 | -24.2 | +20.4 | $+507 |

## CLEAN strategy keep list (n>=10, med>=0, win>=50%)

| strategy | n | win% | med% | avg% | $ |
|---|---:|---:|---:|---:|---:|
| S404 | 12 | 100.0 | +80.1 | +79.4 | $+584 |
| S397 | 13 | 100.0 | +71.8 | +85.7 | $+638 |
| S350 | 12 | 58.3 | +64.9 | +30.4 | $+85 |
| S406 | 16 | 56.2 | +58.3 | +123.1 | $+521 |
| S210 | 17 | 64.7 | +53.6 | +27.4 | $+50 |
| S173 | 105 | 61.9 | +51.6 | +43.1 | $+2,562 |
| S403 | 13 | 53.8 | +49.1 | +0.6 | $+4 |
| S218 | 17 | 52.9 | +47.8 | +67.3 | $+320 |
| S174 | 54 | 68.5 | +30.1 | +5.5 | $+325 |
| S401 | 27 | 51.9 | +23.7 | +42.0 | $+300 |
| S398 | 16 | 50.0 | +3.8 | +46.9 | $+359 |

## Notes

- Prefer CLEAN numbers for promotion / kill decisions.
- KEEP-only is the optimistic lens (past keepers only).
- KILL/KEEP tags are advisory for now - all strategies still trade so weak names can surprise over the next ~week.
- `reconcile_fill` / outage days are TAINTED, not alpha.
- Protective broker stops (LS...) reduce damage when GitHub is down.
