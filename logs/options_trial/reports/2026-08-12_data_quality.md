# Options data quality report - 2026-08-12

Splits ledger exits into **CLEAN** (natural TP/SL/EOD, healthy runtime) vs **TAINTED** (reconcile_fill / broker-missing / known GitHub outage days).
**KEEP-only** = CLEAN exits from strategies with n>=10, med>=0%, win>=50%.

## Headline

| Slice | n | Win% | Med% | Avg% | Realized $ |
|---|---:|---:|---:|---:|---:|
| ALL | 2437 | 36.1 | -41.1 | +10.9 | $+93 |
| CLEAN (perfect running) | 764 | 42.5 | -46.9 | +12.8 | $+8,357 |
| TAINTED (errors/outages) | 1673 | 33.1 | -39.3 | +9.9 | $-8,265 |
| CLEAN since 2026-08-03 | 448 | 31.2 | -51.8 | -3.6 | $-3,942 |
| KEEP-only (CLEAN keepers) | 294 | 63.9 | +37.7 | +42.9 | $+5,741 |
| KEEP-only since 2026-08-03 | 106 | 60.4 | +50.0 | +54.7 | $+1,715 |

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
| 2026-08-10 | BUGGY | 107 | 51 | 22 | -52.4 |
| 2026-08-11 | BUGGY | 65 | 10 | 20 | -53.8 |
| 2026-08-12 | OK | 26 | 0 | 4 | -83.0 |

## CLEAN strategy kill list (n>=10, med<=-20%)

| strategy | n | win% | med% | avg% | $ |
|---|---:|---:|---:|---:|---:|
| ORPHAN | 79 | 21.5 | -66.2 | -22.2 | $+4,151 |
| S212 | 15 | 0.0 | -66.1 | -70.5 | $-561 |
| S360 | 15 | 13.3 | -62.1 | -48.1 | $-320 |
| S405 | 24 | 33.3 | -57.4 | -4.1 | $-38 |
| S407 | 10 | 40.0 | -57.0 | -5.4 | $-50 |
| S207 | 13 | 15.4 | -54.3 | -40.5 | $-341 |
| S217 | 17 | 35.3 | -52.9 | +84.9 | $+136 |
| S351 | 13 | 7.7 | -52.9 | -34.1 | $-108 |
| S355 | 24 | 33.3 | -51.5 | +15.6 | $+76 |
| S354 | 16 | 37.5 | -51.2 | +12.2 | $+46 |
| S364 | 14 | 42.9 | -50.7 | -14.7 | $-188 |
| S211 | 10 | 30.0 | -45.8 | -20.6 | $-94 |
| S408 | 16 | 31.2 | -45.6 | +32.3 | $+45 |
| S165 | 61 | 37.7 | -24.2 | +20.4 | $+507 |

## CLEAN strategy keep list (n>=10, med>=0, win>=50%)

| strategy | n | win% | med% | avg% | $ |
|---|---:|---:|---:|---:|---:|
| S404 | 12 | 100.0 | +80.1 | +79.4 | $+584 |
| S350 | 12 | 58.3 | +64.9 | +30.4 | $+85 |
| S397 | 12 | 100.0 | +64.7 | +79.5 | $+568 |
| S406 | 16 | 56.2 | +58.3 | +123.1 | $+521 |
| S210 | 14 | 71.4 | +55.4 | +36.1 | $+113 |
| S173 | 105 | 61.9 | +51.6 | +43.1 | $+2,562 |
| S218 | 17 | 52.9 | +47.8 | +67.3 | $+320 |
| S401 | 24 | 54.2 | +35.5 | +49.3 | $+334 |
| S174 | 54 | 68.5 | +30.1 | +5.5 | $+325 |
| S398 | 16 | 50.0 | +3.8 | +46.9 | $+359 |
| S403 | 12 | 50.0 | +0.8 | -3.7 | $-29 |

## Notes

- Prefer CLEAN numbers for promotion / kill decisions.
- KEEP-only is the optimistic lens (past keepers only).
- KILL/KEEP tags are advisory for now - all strategies still trade so weak names can surprise over the next ~week.
- `reconcile_fill` / outage days are TAINTED, not alpha.
- Protective broker stops (LS...) reduce damage when GitHub is down.
