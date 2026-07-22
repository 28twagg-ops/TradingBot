# Daily Comprehensive Action Review — 2026-07-22

_Auto-generated from GitHub Actions run output. This document appends every run for the day._

## Run 20260722T001033Z

- UTC timestamp: `20260722T001033Z`
- GitHub run: [#4675](https://github.com/28twagg-ops/TradingBot/actions/runs/29879424953)
- Run id: `29879424953`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`7s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-21T20:10:37.274057-04:00","date":"2026-07-21","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":2.1,"phases_s":{"reconcile":1.73},"signals":0,"placed":0,"equity":131690.73,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":90,"filled_today":105,"unattributed_contracts":0,"top_signals":[],"github_run":"4675","github_run_id":"29879424953","status":"ok"}
```

### Live bot full output

```text
00:10:35  INFO      Mode: summary
00:10:35  INFO        Daily log -> logs/daily/2026-07-22.md
00:10:35  INFO        Daily log reconciled -> logs/daily/2026-07-22.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         00:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $481.00|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $481.00|
|  Cash                                                           $120.06|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $360.94|
|  Open P&L                                                        $+2.28|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (4 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  BIIB     Pullback50      $96.83     $201.84  $203.16  +0.7%   $+0.63  |
|  C        Pullback50      $69.99     $132.61  $132.86  +0.2%   $+0.13  |
|  DUK      Pullback50      $96.87     $125.11  $125.91  +0.6%   $+0.62  |
|  TPR      Pullback50      $97.26     $140.84  $142.16  +0.9%   $+0.91  |
|                                                                        |
|  Total invested                                                 $360.94|
|  Total open P&L                                                  $+2.28|
+========================================================================+

+========================================================================+
|                        EXIT LOGIC ACTIVE  (v8)                         |
+========================================================================+
|  Profit target                              price > 20-day MA (midline)|
|  Stop loss                                             -0.5% from entry|
|  Time stop                                          max 3 calendar days|
+========================================================================+

+========================================================================+
|                          RECENT TRANSACTIONS                           |
+========================================================================+
|  2026-07-21  SELL  APA  Pullback50  $96.03  P&L $-0.00                 |
|  2026-07-21  SELL  BEN  Pullback50  $5.47  P&L $-0.09                  |
|  2026-07-21  SELL  CNP  Pullback50  $10.28  P&L $-0.06                 |
|  2026-07-21  SELL  CI  Pullback50  $95.97  P&L $-0.17                  |
|  2026-07-21  SELL  IEX  Pullback50  $70.78  P&L $-0.49                 |
|  2026-07-21  SELL  MAA  Pullback50  $95.80  P&L $-0.55                 |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=0 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=2
  zombies_flagged=0
options_reconcile: done
Layout: controlled:140:c000_s173_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:140:c000_s173_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      140
=== options_morning_bot (PAPER) 2026-07-21T20:10:37.274057-04:00 ===

[Run context]
After hours (20:10 ET) — exit summary only.
Paper auth OK — equity $131690.73, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $131,690.73                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    90                                      |
|  Orders filled today (ledger)  105                                     |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=258  buckets=22  win=32%                             |
|  Returns   avg=-1.7%  med=-35.3%  p10=-65.3%  p90=+83.9%               |
|  Realized  $+4,817.13                                                  |
|  Raw incl dropped  trades=762  real=$+1,972.58                         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b51  c051_s164_w4_1120_  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  c091_s167_w4_1120_  2 100% +222.0 +222.0 +247.0 $   +293         |
|  b31  c031_s173_w4_1120_  2 100% +145.5 +145.5 +175.8 $   +192         |
|  b28  c028_s173_w1_0928_ 22  77% +50.0 +80.0 +102.0 $   +590           |
|  b58  c058_s173_w3_1045_  1 100% +59.1 +59.1 +59.1 $    +25            |
|  b56  c056_s173_w1_0928_  1 100% +47.7 +47.7 +47.7 $    +21            |
|  b57  c057_s173_w2_1005_  1 100% +47.7 +47.7 +47.7 $    +21            |
|  b89  c089_s167_w2_1005_  9  56% +84.4 +30.9 +790.0 $    +45           |
|  ... 14 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b9   c009_s165_w2_1005_  6   0% -76.2 -78.1 -92.7 $   -261       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-21.log
elapsed=2.1s reconcile=1.73s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=2.1s. run=#4675 https://github.com/28twagg-ops/TradingBot/actions/runs/29879424953
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 2.9% (22/762)
# Options signal frequency

_Generated 2026-07-21T20:10:42.018525_

Headline counts are **unique (strategy, underlying, date)** from `ENTRY` lines in `logs/options_trial/runs/*.log`.
Raw log-line counts (multi-bucket duplicates) are shown below for debug.

### Unique underlying symbols per day (headline)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-08 |    0 |    0 |    3 |    0 |    0 |    0 |    2 |    1 |     6 |
| 2026-07-09 |    0 |    0 |    1 |    0 |    0 |    0 |    2 |    3 |     6 |
| 2026-07-10 |    0 |    0 |    1 |    0 |    0 |    0 |    1 |    1 |     3 |
| 2026-07-13 |    0 |    0 |    2 |    0 |    0 |    0 |    3 |    2 |     7 |
| 2026-07-14 |    0 |    0 |    3 |    0 |    0 |    0 |    2 |    0 |     5 |
| 2026-07-16 |    0 |    0 |    2 |    0 |    0 |    0 |    3 |    0 |     5 |
| 2026-07-17 |    0 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |     4 |
| 2026-07-20 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-21 |    1 |    2 |    1 |    1 |    2 |    2 |    0 |    0 |     9 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 1 | 1 | 1.0 | ~38 active signal-days |
| S164 | 2 | 1 | 2.0 | ~19 active signal-days |
| S165 | 15 | 8 | 1.9 | ~20 active signal-days |
| S166 | 1 | 1 | 1.0 | ~38 active signal-days |
| S167 | 2 | 1 | 2.0 | ~19 active signal-days |
| S168 | 2 | 1 | 2.0 | ~19 active signal-days |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 30 | 1 |
| S164 | 35 | 2 |
| S165 | 1422 | 15 |
| S166 | 30 | 1 |
| S167 | 35 | 2 |
| S168 | 35 | 2 |
| S173 | 1754 | 17 |
| S174 | 891 | 7 |

### Raw log lines per day (debug / multi-bucket)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |    0 |   100 |
| 2026-07-08 |    0 |    0 |  100 |    0 |    0 |    0 |  100 |  100 |   300 |
| 2026-07-09 |    0 |    0 |   24 |    0 |    0 |    0 |  100 |   15 |   139 |
| 2026-07-10 |    0 |    0 |  242 |    0 |    0 |    0 |  230 |  202 |   674 |
| 2026-07-13 |    0 |    0 |  190 |    0 |    0 |    0 |  212 |  188 |   590 |
| 2026-07-14 |    0 |    0 |  194 |    0 |    0 |    0 |  185 |  106 |   485 |
| 2026-07-15 |    0 |    0 |  146 |    0 |    0 |    0 |  154 |   58 |   358 |
| 2026-07-16 |    0 |    0 |  179 |    0 |    0 |    0 |  205 |   58 |   442 |
| 2026-07-17 |    0 |    0 |  127 |    0 |    0 |    0 |  207 |   58 |   392 |
| 2026-07-20 |    0 |    0 |  107 |    0 |    0 |    0 |  143 |   58 |   308 |
| 2026-07-21 |   30 |   35 |  113 |   30 |   35 |   35 |  118 |   48 |   444 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-07-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |    27 | WARN | <<<
| Missing exit records (post) |    27 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |   297 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=481.0 router=CONFIRMED leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---

## Run 20260722T014930Z

- UTC timestamp: `20260722T014930Z`
- GitHub run: [#4676](https://github.com/28twagg-ops/TradingBot/actions/runs/29884121126)
- Run id: `29884121126`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`8s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-21T21:49:35.437938-04:00","date":"2026-07-21","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":2.3,"phases_s":{"reconcile":1.86},"signals":0,"placed":0,"equity":131686.85,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":90,"filled_today":105,"unattributed_contracts":0,"top_signals":[],"github_run":"4676","github_run_id":"29884121126","status":"ok"}
```

### Live bot full output

```text
01:49:31  INFO      Mode: summary
01:49:33  INFO        Daily log -> logs/daily/2026-07-22.md
01:49:33  INFO        Daily log reconciled -> logs/daily/2026-07-22.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         01:49 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $481.00|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $481.00|
|  Cash                                                           $120.06|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $360.94|
|  Open P&L                                                        $+2.28|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (4 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  BIIB     Pullback50      $96.83     $201.84  $203.16  +0.7%   $+0.63  |
|  C        Pullback50      $69.99     $132.61  $132.86  +0.2%   $+0.13  |
|  DUK      Pullback50      $96.87     $125.11  $125.91  +0.6%   $+0.62  |
|  TPR      Pullback50      $97.26     $140.84  $142.16  +0.9%   $+0.91  |
|                                                                        |
|  Total invested                                                 $360.94|
|  Total open P&L                                                  $+2.28|
+========================================================================+

+========================================================================+
|                        EXIT LOGIC ACTIVE  (v8)                         |
+========================================================================+
|  Profit target                              price > 20-day MA (midline)|
|  Stop loss                                             -0.5% from entry|
|  Time stop                                          max 3 calendar days|
+========================================================================+

+========================================================================+
|                          RECENT TRANSACTIONS                           |
+========================================================================+
|  2026-07-21  SELL  APA  Pullback50  $96.03  P&L $-0.00                 |
|  2026-07-21  SELL  BEN  Pullback50  $5.47  P&L $-0.09                  |
|  2026-07-21  SELL  CNP  Pullback50  $10.28  P&L $-0.06                 |
|  2026-07-21  SELL  CI  Pullback50  $95.97  P&L $-0.17                  |
|  2026-07-21  SELL  IEX  Pullback50  $70.78  P&L $-0.49                 |
|  2026-07-21  SELL  MAA  Pullback50  $95.80  P&L $-0.55                 |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=0 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=2
  zombies_flagged=0
options_reconcile: done
Layout: controlled:140:c000_s173_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:140:c000_s173_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      140
=== options_morning_bot (PAPER) 2026-07-21T21:49:35.437938-04:00 ===

[Run context]
After hours (21:49 ET) — exit summary only.
Paper auth OK — equity $131686.85, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $131,686.85                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    90                                      |
|  Orders filled today (ledger)  105                                     |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=258  buckets=22  win=32%                             |
|  Returns   avg=-1.7%  med=-35.3%  p10=-65.3%  p90=+83.9%               |
|  Realized  $+4,817.13                                                  |
|  Raw incl dropped  trades=762  real=$+1,972.58                         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b51  c051_s164_w4_1120_  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  c091_s167_w4_1120_  2 100% +222.0 +222.0 +247.0 $   +293         |
|  b31  c031_s173_w4_1120_  2 100% +145.5 +145.5 +175.8 $   +192         |
|  b28  c028_s173_w1_0928_ 22  77% +50.0 +80.0 +102.0 $   +590           |
|  b58  c058_s173_w3_1045_  1 100% +59.1 +59.1 +59.1 $    +25            |
|  b56  c056_s173_w1_0928_  1 100% +47.7 +47.7 +47.7 $    +21            |
|  b57  c057_s173_w2_1005_  1 100% +47.7 +47.7 +47.7 $    +21            |
|  b89  c089_s167_w2_1005_  9  56% +84.4 +30.9 +790.0 $    +45           |
|  ... 14 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b9   c009_s165_w2_1005_  6   0% -76.2 -78.1 -92.7 $   -261       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-21.log
elapsed=2.3s reconcile=1.86s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=2.3s. run=#4676 https://github.com/28twagg-ops/TradingBot/actions/runs/29884121126
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 2.9% (22/762)
# Options signal frequency

_Generated 2026-07-21T21:49:41.128065_

Headline counts are **unique (strategy, underlying, date)** from `ENTRY` lines in `logs/options_trial/runs/*.log`.
Raw log-line counts (multi-bucket duplicates) are shown below for debug.

### Unique underlying symbols per day (headline)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-08 |    0 |    0 |    3 |    0 |    0 |    0 |    2 |    1 |     6 |
| 2026-07-09 |    0 |    0 |    1 |    0 |    0 |    0 |    2 |    3 |     6 |
| 2026-07-10 |    0 |    0 |    1 |    0 |    0 |    0 |    1 |    1 |     3 |
| 2026-07-13 |    0 |    0 |    2 |    0 |    0 |    0 |    3 |    2 |     7 |
| 2026-07-14 |    0 |    0 |    3 |    0 |    0 |    0 |    2 |    0 |     5 |
| 2026-07-16 |    0 |    0 |    2 |    0 |    0 |    0 |    3 |    0 |     5 |
| 2026-07-17 |    0 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |     4 |
| 2026-07-20 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-21 |    1 |    2 |    1 |    1 |    2 |    2 |    0 |    0 |     9 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 1 | 1 | 1.0 | ~38 active signal-days |
| S164 | 2 | 1 | 2.0 | ~19 active signal-days |
| S165 | 15 | 8 | 1.9 | ~20 active signal-days |
| S166 | 1 | 1 | 1.0 | ~38 active signal-days |
| S167 | 2 | 1 | 2.0 | ~19 active signal-days |
| S168 | 2 | 1 | 2.0 | ~19 active signal-days |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 30 | 1 |
| S164 | 35 | 2 |
| S165 | 1422 | 15 |
| S166 | 30 | 1 |
| S167 | 35 | 2 |
| S168 | 35 | 2 |
| S173 | 1754 | 17 |
| S174 | 891 | 7 |

### Raw log lines per day (debug / multi-bucket)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |    0 |   100 |
| 2026-07-08 |    0 |    0 |  100 |    0 |    0 |    0 |  100 |  100 |   300 |
| 2026-07-09 |    0 |    0 |   24 |    0 |    0 |    0 |  100 |   15 |   139 |
| 2026-07-10 |    0 |    0 |  242 |    0 |    0 |    0 |  230 |  202 |   674 |
| 2026-07-13 |    0 |    0 |  190 |    0 |    0 |    0 |  212 |  188 |   590 |
| 2026-07-14 |    0 |    0 |  194 |    0 |    0 |    0 |  185 |  106 |   485 |
| 2026-07-15 |    0 |    0 |  146 |    0 |    0 |    0 |  154 |   58 |   358 |
| 2026-07-16 |    0 |    0 |  179 |    0 |    0 |    0 |  205 |   58 |   442 |
| 2026-07-17 |    0 |    0 |  127 |    0 |    0 |    0 |  207 |   58 |   392 |
| 2026-07-20 |    0 |    0 |  107 |    0 |    0 |    0 |  143 |   58 |   308 |
| 2026-07-21 |   30 |   35 |  113 |   30 |   35 |   35 |  118 |   48 |   444 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-07-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |    27 | WARN | <<<
| Missing exit records (post) |    27 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |   297 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=481.0 router=CONFIRMED leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---

## Run 20260722T045320Z

- UTC timestamp: `20260722T045320Z`
- GitHub run: [#4677](https://github.com/28twagg-ops/TradingBot/actions/runs/29892217686)
- Run id: `29892217686`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`7s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-22T00:53:23.284680-04:00","date":"2026-07-22","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.6,"phases_s":{"reconcile":1.35},"signals":0,"placed":0,"equity":130878.85,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4677","github_run_id":"29892217686","status":"ok"}
```

### Live bot full output

```text
04:53:21  INFO      Mode: summary
04:53:21  INFO        Daily log -> logs/daily/2026-07-22.md
04:53:21  INFO        Daily log reconciled -> logs/daily/2026-07-22.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         04:53 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $481.00|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $481.00|
|  Cash                                                           $120.06|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $360.94|
|  Open P&L                                                        $+2.28|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (4 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  BIIB     Pullback50      $96.83     $201.84  $203.16  +0.7%   $+0.63  |
|  C        Pullback50      $69.99     $132.61  $132.86  +0.2%   $+0.13  |
|  DUK      Pullback50      $96.87     $125.11  $125.91  +0.6%   $+0.62  |
|  TPR      Pullback50      $97.26     $140.84  $142.16  +0.9%   $+0.91  |
|                                                                        |
|  Total invested                                                 $360.94|
|  Total open P&L                                                  $+2.28|
+========================================================================+

+========================================================================+
|                        EXIT LOGIC ACTIVE  (v8)                         |
+========================================================================+
|  Profit target                              price > 20-day MA (midline)|
|  Stop loss                                             -0.5% from entry|
|  Time stop                                          max 3 calendar days|
+========================================================================+

+========================================================================+
|                          RECENT TRANSACTIONS                           |
+========================================================================+
|  2026-07-21  SELL  APA  Pullback50  $96.03  P&L $-0.00                 |
|  2026-07-21  SELL  BEN  Pullback50  $5.47  P&L $-0.09                  |
|  2026-07-21  SELL  CNP  Pullback50  $10.28  P&L $-0.06                 |
|  2026-07-21  SELL  CI  Pullback50  $95.97  P&L $-0.17                  |
|  2026-07-21  SELL  IEX  Pullback50  $70.78  P&L $-0.49                 |
|  2026-07-21  SELL  MAA  Pullback50  $95.80  P&L $-0.55                 |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=0 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=2
  zombies_flagged=0
options_reconcile: done
Layout: controlled:140:c000_s173_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:140:c000_s173_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      140
=== options_morning_bot (PAPER) 2026-07-22T00:53:23.284680-04:00 ===

[Run context]
After hours (00:53 ET) — exit summary only.
Paper auth OK — equity $130878.85, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $130,878.85                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=258  buckets=22  win=32%                             |
|  Returns   avg=-1.7%  med=-35.3%  p10=-65.3%  p90=+83.9%               |
|  Realized  $+4,817.13                                                  |
|  Raw incl dropped  trades=762  real=$+1,972.58                         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b51  c051_s164_w4_1120_  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  c091_s167_w4_1120_  2 100% +222.0 +222.0 +247.0 $   +293         |
|  b31  c031_s173_w4_1120_  2 100% +145.5 +145.5 +175.8 $   +192         |
|  b28  c028_s173_w1_0928_ 22  77% +50.0 +80.0 +102.0 $   +590           |
|  b58  c058_s173_w3_1045_  1 100% +59.1 +59.1 +59.1 $    +25            |
|  b56  c056_s173_w1_0928_  1 100% +47.7 +47.7 +47.7 $    +21            |
|  b57  c057_s173_w2_1005_  1 100% +47.7 +47.7 +47.7 $    +21            |
|  b89  c089_s167_w2_1005_  9  56% +84.4 +30.9 +790.0 $    +45           |
|  ... 14 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b9   c009_s165_w2_1005_  6   0% -76.2 -78.1 -92.7 $   -261       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-22.log
elapsed=1.6s reconcile=1.35s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.6s. run=#4677 https://github.com/28twagg-ops/TradingBot/actions/runs/29892217686
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 2.9% (22/762)
# Options signal frequency

_Generated 2026-07-22T00:53:28.231518_

Headline counts are **unique (strategy, underlying, date)** from `ENTRY` lines in `logs/options_trial/runs/*.log`.
Raw log-line counts (multi-bucket duplicates) are shown below for debug.

### Unique underlying symbols per day (headline)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-08 |    0 |    0 |    3 |    0 |    0 |    0 |    2 |    1 |     6 |
| 2026-07-09 |    0 |    0 |    1 |    0 |    0 |    0 |    2 |    3 |     6 |
| 2026-07-10 |    0 |    0 |    1 |    0 |    0 |    0 |    1 |    1 |     3 |
| 2026-07-13 |    0 |    0 |    2 |    0 |    0 |    0 |    3 |    2 |     7 |
| 2026-07-14 |    0 |    0 |    3 |    0 |    0 |    0 |    2 |    0 |     5 |
| 2026-07-16 |    0 |    0 |    2 |    0 |    0 |    0 |    3 |    0 |     5 |
| 2026-07-17 |    0 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |     4 |
| 2026-07-20 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-21 |    1 |    2 |    1 |    1 |    2 |    2 |    0 |    0 |     9 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 1 | 1 | 1.0 | ~38 active signal-days |
| S164 | 2 | 1 | 2.0 | ~19 active signal-days |
| S165 | 15 | 8 | 1.9 | ~20 active signal-days |
| S166 | 1 | 1 | 1.0 | ~38 active signal-days |
| S167 | 2 | 1 | 2.0 | ~19 active signal-days |
| S168 | 2 | 1 | 2.0 | ~19 active signal-days |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 45 | 1 |
| S164 | 55 | 2 |
| S165 | 1488 | 15 |
| S166 | 45 | 1 |
| S167 | 55 | 2 |
| S168 | 55 | 2 |
| S173 | 1831 | 17 |
| S174 | 891 | 7 |

### Raw log lines per day (debug / multi-bucket)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |    0 |   100 |
| 2026-07-08 |    0 |    0 |  100 |    0 |    0 |    0 |  100 |  100 |   300 |
| 2026-07-09 |    0 |    0 |   24 |    0 |    0 |    0 |  100 |   15 |   139 |
| 2026-07-10 |    0 |    0 |  242 |    0 |    0 |    0 |  230 |  202 |   674 |
| 2026-07-13 |    0 |    0 |  190 |    0 |    0 |    0 |  212 |  188 |   590 |
| 2026-07-14 |    0 |    0 |  194 |    0 |    0 |    0 |  185 |  106 |   485 |
| 2026-07-15 |    0 |    0 |  146 |    0 |    0 |    0 |  154 |   58 |   358 |
| 2026-07-16 |    0 |    0 |  179 |    0 |    0 |    0 |  205 |   58 |   442 |
| 2026-07-17 |    0 |    0 |  127 |    0 |    0 |    0 |  207 |   58 |   392 |
| 2026-07-20 |    0 |    0 |  107 |    0 |    0 |    0 |  143 |   58 |   308 |
| 2026-07-21 |   30 |   35 |  113 |   30 |   35 |   35 |  118 |   48 |   444 |
| 2026-07-22 |   15 |   20 |   66 |   15 |   20 |   20 |   77 |    0 |   233 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-07-22
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |     7 | WARN | <<<
| Missing exit records (post) |     7 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |   297 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   616 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=481.0 router=CONFIRMED leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---

## Run 20260722T130046Z

- UTC timestamp: `20260722T130046Z`
- GitHub run: [#4678](https://github.com/28twagg-ops/TradingBot/actions/runs/29921975375)
- Run id: `29921975375`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`9s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-22T09:00:52.027573-04:00","date":"2026-07-22","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":2.7,"phases_s":{"reconcile":2.27},"signals":0,"placed":0,"equity":129871.33,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4678","github_run_id":"29921975375","status":"ok"}
```

### Live bot full output

```text
13:00:47  INFO      Mode: summary
13:00:49  INFO        Daily log -> logs/daily/2026-07-22.md
13:00:49  INFO        Daily log reconciled -> logs/daily/2026-07-22.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:00 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $480.62|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $480.62|
|  Cash                                                           $120.06|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $360.56|
|  Open P&L                                                        $+1.90|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (4 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  BIIB     Pullback50      $96.83     $201.84  $203.16  +0.7%   $+0.63  |
|  C        Pullback50      $70.07     $132.61  $133.00  +0.3%   $+0.21  |
|  DUK      Pullback50      $96.87     $125.11  $125.91  +0.6%   $+0.62  |
|  TPR      Pullback50      $96.80     $140.84  $141.50  +0.5%   $+0.45  |
|                                                                        |
|  Total invested                                                 $360.56|
|  Total open P&L                                                  $+1.90|
+========================================================================+

+========================================================================+
|                        EXIT LOGIC ACTIVE  (v8)                         |
+========================================================================+
|  Profit target                              price > 20-day MA (midline)|
|  Stop loss                                             -0.5% from entry|
|  Time stop                                          max 3 calendar days|
+========================================================================+

+========================================================================+
|                          RECENT TRANSACTIONS                           |
+========================================================================+
|  2026-07-21  SELL  APA  Pullback50  $96.03  P&L $-0.00                 |
|  2026-07-21  SELL  BEN  Pullback50  $5.47  P&L $-0.09                  |
|  2026-07-21  SELL  CNP  Pullback50  $10.28  P&L $-0.06                 |
|  2026-07-21  SELL  CI  Pullback50  $95.97  P&L $-0.17                  |
|  2026-07-21  SELL  IEX  Pullback50  $70.78  P&L $-0.49                 |
|  2026-07-21  SELL  MAA  Pullback50  $95.80  P&L $-0.55                 |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=0 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=2
  zombies_flagged=0
options_reconcile: done
Layout: controlled:140:c000_s173_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:140:c000_s173_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      140
=== options_morning_bot (PAPER) 2026-07-22T09:00:52.027573-04:00 ===

[Run context]
After hours (09:00 ET) — exit summary only.
Paper auth OK — equity $129871.33, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $129,871.33                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=258  buckets=22  win=32%                             |
|  Returns   avg=-1.7%  med=-35.3%  p10=-65.3%  p90=+83.9%               |
|  Realized  $+4,817.13                                                  |
|  Raw incl dropped  trades=762  real=$+1,972.58                         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b51  c051_s164_w4_1120_  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  c091_s167_w4_1120_  2 100% +222.0 +222.0 +247.0 $   +293         |
|  b31  c031_s173_w4_1120_  2 100% +145.5 +145.5 +175.8 $   +192         |
|  b28  c028_s173_w1_0928_ 22  77% +50.0 +80.0 +102.0 $   +590           |
|  b58  c058_s173_w3_1045_  1 100% +59.1 +59.1 +59.1 $    +25            |
|  b56  c056_s173_w1_0928_  1 100% +47.7 +47.7 +47.7 $    +21            |
|  b57  c057_s173_w2_1005_  1 100% +47.7 +47.7 +47.7 $    +21            |
|  b89  c089_s167_w2_1005_  9  56% +84.4 +30.9 +790.0 $    +45           |
|  ... 14 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b9   c009_s165_w2_1005_  6   0% -76.2 -78.1 -92.7 $   -261       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-22.log
elapsed=2.7s reconcile=2.27s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=2.7s. run=#4678 https://github.com/28twagg-ops/TradingBot/actions/runs/29921975375
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 2.9% (22/762)
# Options signal frequency

_Generated 2026-07-22T09:00:57.948814_

Headline counts are **unique (strategy, underlying, date)** from `ENTRY` lines in `logs/options_trial/runs/*.log`.
Raw log-line counts (multi-bucket duplicates) are shown below for debug.

### Unique underlying symbols per day (headline)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-08 |    0 |    0 |    3 |    0 |    0 |    0 |    2 |    1 |     6 |
| 2026-07-09 |    0 |    0 |    1 |    0 |    0 |    0 |    2 |    3 |     6 |
| 2026-07-10 |    0 |    0 |    1 |    0 |    0 |    0 |    1 |    1 |     3 |
| 2026-07-13 |    0 |    0 |    2 |    0 |    0 |    0 |    3 |    2 |     7 |
| 2026-07-14 |    0 |    0 |    3 |    0 |    0 |    0 |    2 |    0 |     5 |
| 2026-07-16 |    0 |    0 |    2 |    0 |    0 |    0 |    3 |    0 |     5 |
| 2026-07-17 |    0 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |     4 |
| 2026-07-20 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-21 |    1 |    2 |    1 |    1 |    2 |    2 |    0 |    0 |     9 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 1 | 1 | 1.0 | ~38 active signal-days |
| S164 | 2 | 1 | 2.0 | ~19 active signal-days |
| S165 | 15 | 8 | 1.9 | ~20 active signal-days |
| S166 | 1 | 1 | 1.0 | ~38 active signal-days |
| S167 | 2 | 1 | 2.0 | ~19 active signal-days |
| S168 | 2 | 1 | 2.0 | ~19 active signal-days |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 45 | 1 |
| S164 | 55 | 2 |
| S165 | 1488 | 15 |
| S166 | 45 | 1 |
| S167 | 55 | 2 |
| S168 | 55 | 2 |
| S173 | 1831 | 17 |
| S174 | 891 | 7 |

### Raw log lines per day (debug / multi-bucket)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |    0 |   100 |
| 2026-07-08 |    0 |    0 |  100 |    0 |    0 |    0 |  100 |  100 |   300 |
| 2026-07-09 |    0 |    0 |   24 |    0 |    0 |    0 |  100 |   15 |   139 |
| 2026-07-10 |    0 |    0 |  242 |    0 |    0 |    0 |  230 |  202 |   674 |
| 2026-07-13 |    0 |    0 |  190 |    0 |    0 |    0 |  212 |  188 |   590 |
| 2026-07-14 |    0 |    0 |  194 |    0 |    0 |    0 |  185 |  106 |   485 |
| 2026-07-15 |    0 |    0 |  146 |    0 |    0 |    0 |  154 |   58 |   358 |
| 2026-07-16 |    0 |    0 |  179 |    0 |    0 |    0 |  205 |   58 |   442 |
| 2026-07-17 |    0 |    0 |  127 |    0 |    0 |    0 |  207 |   58 |   392 |
| 2026-07-20 |    0 |    0 |  107 |    0 |    0 |    0 |  143 |   58 |   308 |
| 2026-07-21 |   30 |   35 |  113 |   30 |   35 |   35 |  118 |   48 |   444 |
| 2026-07-22 |   15 |   20 |   66 |   15 |   20 |   20 |   77 |    0 |   233 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-07-22
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |     7 | WARN | <<<
| Missing exit records (post) |     7 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |   297 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   616 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=480.62 router=CONFIRMED leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---

## Run 20260722T130536Z

- UTC timestamp: `20260722T130536Z`
- GitHub run: [#4679](https://github.com/28twagg-ops/TradingBot/actions/runs/29922340326)
- Run id: `29922340326`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`7s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-22T09:05:39.369260-04:00","date":"2026-07-22","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.8,"phases_s":{"reconcile":1.45},"signals":0,"placed":0,"equity":129979.33,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4679","github_run_id":"29922340326","status":"ok"}
```

### Live bot full output

```text
13:05:37  INFO      Mode: summary
13:05:37  INFO        Daily log -> logs/daily/2026-07-22.md
13:05:37  INFO        Daily log reconciled -> logs/daily/2026-07-22.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:05 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $480.62|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $480.62|
|  Cash                                                           $120.06|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $360.56|
|  Open P&L                                                        $+1.90|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (4 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  BIIB     Pullback50      $96.83     $201.84  $203.16  +0.7%   $+0.63  |
|  C        Pullback50      $70.07     $132.61  $133.00  +0.3%   $+0.21  |
|  DUK      Pullback50      $96.87     $125.11  $125.91  +0.6%   $+0.62  |
|  TPR      Pullback50      $96.80     $140.84  $141.50  +0.5%   $+0.45  |
|                                                                        |
|  Total invested                                                 $360.56|
|  Total open P&L                                                  $+1.90|
+========================================================================+

+========================================================================+
|                        EXIT LOGIC ACTIVE  (v8)                         |
+========================================================================+
|  Profit target                              price > 20-day MA (midline)|
|  Stop loss                                             -0.5% from entry|
|  Time stop                                          max 3 calendar days|
+========================================================================+

+========================================================================+
|                          RECENT TRANSACTIONS                           |
+========================================================================+
|  2026-07-21  SELL  APA  Pullback50  $96.03  P&L $-0.00                 |
|  2026-07-21  SELL  BEN  Pullback50  $5.47  P&L $-0.09                  |
|  2026-07-21  SELL  CNP  Pullback50  $10.28  P&L $-0.06                 |
|  2026-07-21  SELL  CI  Pullback50  $95.97  P&L $-0.17                  |
|  2026-07-21  SELL  IEX  Pullback50  $70.78  P&L $-0.49                 |
|  2026-07-21  SELL  MAA  Pullback50  $95.80  P&L $-0.55                 |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=0 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=2
  zombies_flagged=0
options_reconcile: done
Layout: controlled:140:c000_s173_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:140:c000_s173_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      140
=== options_morning_bot (PAPER) 2026-07-22T09:05:39.369260-04:00 ===

[Run context]
After hours (09:05 ET) — exit summary only.
Paper auth OK — equity $129979.33, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $129,979.33                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=258  buckets=22  win=32%                             |
|  Returns   avg=-1.7%  med=-35.3%  p10=-65.3%  p90=+83.9%               |
|  Realized  $+4,817.13                                                  |
|  Raw incl dropped  trades=762  real=$+1,972.58                         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b51  c051_s164_w4_1120_  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  c091_s167_w4_1120_  2 100% +222.0 +222.0 +247.0 $   +293         |
|  b31  c031_s173_w4_1120_  2 100% +145.5 +145.5 +175.8 $   +192         |
|  b28  c028_s173_w1_0928_ 22  77% +50.0 +80.0 +102.0 $   +590           |
|  b58  c058_s173_w3_1045_  1 100% +59.1 +59.1 +59.1 $    +25            |
|  b56  c056_s173_w1_0928_  1 100% +47.7 +47.7 +47.7 $    +21            |
|  b57  c057_s173_w2_1005_  1 100% +47.7 +47.7 +47.7 $    +21            |
|  b89  c089_s167_w2_1005_  9  56% +84.4 +30.9 +790.0 $    +45           |
|  ... 14 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b9   c009_s165_w2_1005_  6   0% -76.2 -78.1 -92.7 $   -261       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-22.log
elapsed=1.8s reconcile=1.45s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.8s. run=#4679 https://github.com/28twagg-ops/TradingBot/actions/runs/29922340326
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 2.9% (22/762)
# Options signal frequency

_Generated 2026-07-22T09:05:44.144154_

Headline counts are **unique (strategy, underlying, date)** from `ENTRY` lines in `logs/options_trial/runs/*.log`.
Raw log-line counts (multi-bucket duplicates) are shown below for debug.

### Unique underlying symbols per day (headline)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-08 |    0 |    0 |    3 |    0 |    0 |    0 |    2 |    1 |     6 |
| 2026-07-09 |    0 |    0 |    1 |    0 |    0 |    0 |    2 |    3 |     6 |
| 2026-07-10 |    0 |    0 |    1 |    0 |    0 |    0 |    1 |    1 |     3 |
| 2026-07-13 |    0 |    0 |    2 |    0 |    0 |    0 |    3 |    2 |     7 |
| 2026-07-14 |    0 |    0 |    3 |    0 |    0 |    0 |    2 |    0 |     5 |
| 2026-07-16 |    0 |    0 |    2 |    0 |    0 |    0 |    3 |    0 |     5 |
| 2026-07-17 |    0 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |     4 |
| 2026-07-20 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-21 |    1 |    2 |    1 |    1 |    2 |    2 |    0 |    0 |     9 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 1 | 1 | 1.0 | ~38 active signal-days |
| S164 | 2 | 1 | 2.0 | ~19 active signal-days |
| S165 | 15 | 8 | 1.9 | ~20 active signal-days |
| S166 | 1 | 1 | 1.0 | ~38 active signal-days |
| S167 | 2 | 1 | 2.0 | ~19 active signal-days |
| S168 | 2 | 1 | 2.0 | ~19 active signal-days |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 45 | 1 |
| S164 | 55 | 2 |
| S165 | 1488 | 15 |
| S166 | 45 | 1 |
| S167 | 55 | 2 |
| S168 | 55 | 2 |
| S173 | 1831 | 17 |
| S174 | 891 | 7 |

### Raw log lines per day (debug / multi-bucket)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |    0 |   100 |
| 2026-07-08 |    0 |    0 |  100 |    0 |    0 |    0 |  100 |  100 |   300 |
| 2026-07-09 |    0 |    0 |   24 |    0 |    0 |    0 |  100 |   15 |   139 |
| 2026-07-10 |    0 |    0 |  242 |    0 |    0 |    0 |  230 |  202 |   674 |
| 2026-07-13 |    0 |    0 |  190 |    0 |    0 |    0 |  212 |  188 |   590 |
| 2026-07-14 |    0 |    0 |  194 |    0 |    0 |    0 |  185 |  106 |   485 |
| 2026-07-15 |    0 |    0 |  146 |    0 |    0 |    0 |  154 |   58 |   358 |
| 2026-07-16 |    0 |    0 |  179 |    0 |    0 |    0 |  205 |   58 |   442 |
| 2026-07-17 |    0 |    0 |  127 |    0 |    0 |    0 |  207 |   58 |   392 |
| 2026-07-20 |    0 |    0 |  107 |    0 |    0 |    0 |  143 |   58 |   308 |
| 2026-07-21 |   30 |   35 |  113 |   30 |   35 |   35 |  118 |   48 |   444 |
| 2026-07-22 |   15 |   20 |   66 |   15 |   20 |   20 |   77 |    0 |   233 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-07-22
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |     7 | WARN | <<<
| Missing exit records (post) |     7 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |   297 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   616 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=480.62 router=CONFIRMED leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---

## Run 20260722T131043Z

- UTC timestamp: `20260722T131043Z`
- GitHub run: [#4680](https://github.com/28twagg-ops/TradingBot/actions/runs/29922697035)
- Run id: `29922697035`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`7s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-22T09:10:46.735632-04:00","date":"2026-07-22","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":2.2,"phases_s":{"reconcile":1.99},"signals":0,"placed":0,"equity":130187.33,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4680","github_run_id":"29922697035","status":"ok"}
```

### Live bot full output

```text
13:10:44  INFO      Mode: summary
13:10:45  INFO        Daily log -> logs/daily/2026-07-22.md
13:10:45  INFO        Daily log reconciled -> logs/daily/2026-07-22.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $480.62|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $480.62|
|  Cash                                                           $120.06|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $360.56|
|  Open P&L                                                        $+1.90|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (4 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  BIIB     Pullback50      $96.83     $201.84  $203.16  +0.7%   $+0.63  |
|  C        Pullback50      $70.07     $132.61  $133.00  +0.3%   $+0.21  |
|  DUK      Pullback50      $96.87     $125.11  $125.91  +0.6%   $+0.62  |
|  TPR      Pullback50      $96.80     $140.84  $141.50  +0.5%   $+0.45  |
|                                                                        |
|  Total invested                                                 $360.56|
|  Total open P&L                                                  $+1.90|
+========================================================================+

+========================================================================+
|                        EXIT LOGIC ACTIVE  (v8)                         |
+========================================================================+
|  Profit target                              price > 20-day MA (midline)|
|  Stop loss                                             -0.5% from entry|
|  Time stop                                          max 3 calendar days|
+========================================================================+

+========================================================================+
|                          RECENT TRANSACTIONS                           |
+========================================================================+
|  2026-07-21  SELL  APA  Pullback50  $96.03  P&L $-0.00                 |
|  2026-07-21  SELL  BEN  Pullback50  $5.47  P&L $-0.09                  |
|  2026-07-21  SELL  CNP  Pullback50  $10.28  P&L $-0.06                 |
|  2026-07-21  SELL  CI  Pullback50  $95.97  P&L $-0.17                  |
|  2026-07-21  SELL  IEX  Pullback50  $70.78  P&L $-0.49                 |
|  2026-07-21  SELL  MAA  Pullback50  $95.80  P&L $-0.55                 |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=0 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=2
  zombies_flagged=0
options_reconcile: done
Layout: controlled:140:c000_s173_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:140:c000_s173_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      140
=== options_morning_bot (PAPER) 2026-07-22T09:10:46.735632-04:00 ===

[Run context]
After hours (09:10 ET) — exit summary only.
Paper auth OK — equity $130187.33, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $130,187.33                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=258  buckets=22  win=32%                             |
|  Returns   avg=-1.7%  med=-35.3%  p10=-65.3%  p90=+83.9%               |
|  Realized  $+4,817.13                                                  |
|  Raw incl dropped  trades=762  real=$+1,972.58                         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b51  c051_s164_w4_1120_  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  c091_s167_w4_1120_  2 100% +222.0 +222.0 +247.0 $   +293         |
|  b31  c031_s173_w4_1120_  2 100% +145.5 +145.5 +175.8 $   +192         |
|  b28  c028_s173_w1_0928_ 22  77% +50.0 +80.0 +102.0 $   +590           |
|  b58  c058_s173_w3_1045_  1 100% +59.1 +59.1 +59.1 $    +25            |
|  b56  c056_s173_w1_0928_  1 100% +47.7 +47.7 +47.7 $    +21            |
|  b57  c057_s173_w2_1005_  1 100% +47.7 +47.7 +47.7 $    +21            |
|  b89  c089_s167_w2_1005_  9  56% +84.4 +30.9 +790.0 $    +45           |
|  ... 14 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b9   c009_s165_w2_1005_  6   0% -76.2 -78.1 -92.7 $   -261       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-22.log
elapsed=2.2s reconcile=1.99s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=2.2s. run=#4680 https://github.com/28twagg-ops/TradingBot/actions/runs/29922697035
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 2.9% (22/762)
# Options signal frequency

_Generated 2026-07-22T09:10:52.030617_

Headline counts are **unique (strategy, underlying, date)** from `ENTRY` lines in `logs/options_trial/runs/*.log`.
Raw log-line counts (multi-bucket duplicates) are shown below for debug.

### Unique underlying symbols per day (headline)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-08 |    0 |    0 |    3 |    0 |    0 |    0 |    2 |    1 |     6 |
| 2026-07-09 |    0 |    0 |    1 |    0 |    0 |    0 |    2 |    3 |     6 |
| 2026-07-10 |    0 |    0 |    1 |    0 |    0 |    0 |    1 |    1 |     3 |
| 2026-07-13 |    0 |    0 |    2 |    0 |    0 |    0 |    3 |    2 |     7 |
| 2026-07-14 |    0 |    0 |    3 |    0 |    0 |    0 |    2 |    0 |     5 |
| 2026-07-16 |    0 |    0 |    2 |    0 |    0 |    0 |    3 |    0 |     5 |
| 2026-07-17 |    0 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |     4 |
| 2026-07-20 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-21 |    1 |    2 |    1 |    1 |    2 |    2 |    0 |    0 |     9 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 1 | 1 | 1.0 | ~38 active signal-days |
| S164 | 2 | 1 | 2.0 | ~19 active signal-days |
| S165 | 15 | 8 | 1.9 | ~20 active signal-days |
| S166 | 1 | 1 | 1.0 | ~38 active signal-days |
| S167 | 2 | 1 | 2.0 | ~19 active signal-days |
| S168 | 2 | 1 | 2.0 | ~19 active signal-days |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 45 | 1 |
| S164 | 55 | 2 |
| S165 | 1488 | 15 |
| S166 | 45 | 1 |
| S167 | 55 | 2 |
| S168 | 55 | 2 |
| S173 | 1831 | 17 |
| S174 | 891 | 7 |

### Raw log lines per day (debug / multi-bucket)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |    0 |   100 |
| 2026-07-08 |    0 |    0 |  100 |    0 |    0 |    0 |  100 |  100 |   300 |
| 2026-07-09 |    0 |    0 |   24 |    0 |    0 |    0 |  100 |   15 |   139 |
| 2026-07-10 |    0 |    0 |  242 |    0 |    0 |    0 |  230 |  202 |   674 |
| 2026-07-13 |    0 |    0 |  190 |    0 |    0 |    0 |  212 |  188 |   590 |
| 2026-07-14 |    0 |    0 |  194 |    0 |    0 |    0 |  185 |  106 |   485 |
| 2026-07-15 |    0 |    0 |  146 |    0 |    0 |    0 |  154 |   58 |   358 |
| 2026-07-16 |    0 |    0 |  179 |    0 |    0 |    0 |  205 |   58 |   442 |
| 2026-07-17 |    0 |    0 |  127 |    0 |    0 |    0 |  207 |   58 |   392 |
| 2026-07-20 |    0 |    0 |  107 |    0 |    0 |    0 |  143 |   58 |   308 |
| 2026-07-21 |   30 |   35 |  113 |   30 |   35 |   35 |  118 |   48 |   444 |
| 2026-07-22 |   15 |   20 |   66 |   15 |   20 |   20 |   77 |    0 |   233 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-07-22
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |     7 | WARN | <<<
| Missing exit records (post) |     7 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |   297 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   616 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=480.62 router=CONFIRMED leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---

## Run 20260722T131535Z

- UTC timestamp: `20260722T131535Z`
- GitHub run: [#4681](https://github.com/28twagg-ops/TradingBot/actions/runs/29923063426)
- Run id: `29923063426`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`6s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-22T09:15:38.379712-04:00","date":"2026-07-22","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.7,"phases_s":{"reconcile":1.43},"signals":0,"placed":0,"equity":130167.33,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4681","github_run_id":"29923063426","status":"ok"}
```

### Live bot full output

```text
13:15:36  INFO      Mode: summary
13:15:36  INFO        Daily log -> logs/daily/2026-07-22.md
13:15:36  INFO        Daily log reconciled -> logs/daily/2026-07-22.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:15 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $480.70|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $480.70|
|  Cash                                                           $120.06|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $360.64|
|  Open P&L                                                        $+1.98|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (4 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  BIIB     Pullback50      $96.83     $201.84  $203.16  +0.7%   $+0.63  |
|  C        Pullback50      $70.07     $132.61  $133.00  +0.3%   $+0.21  |
|  DUK      Pullback50      $96.94     $125.11  $126.01  +0.7%   $+0.69  |
|  TPR      Pullback50      $96.80     $140.84  $141.50  +0.5%   $+0.45  |
|                                                                        |
|  Total invested                                                 $360.64|
|  Total open P&L                                                  $+1.98|
+========================================================================+

+========================================================================+
|                        EXIT LOGIC ACTIVE  (v8)                         |
+========================================================================+
|  Profit target                              price > 20-day MA (midline)|
|  Stop loss                                             -0.5% from entry|
|  Time stop                                          max 3 calendar days|
+========================================================================+

+========================================================================+
|                          RECENT TRANSACTIONS                           |
+========================================================================+
|  2026-07-21  SELL  APA  Pullback50  $96.03  P&L $-0.00                 |
|  2026-07-21  SELL  BEN  Pullback50  $5.47  P&L $-0.09                  |
|  2026-07-21  SELL  CNP  Pullback50  $10.28  P&L $-0.06                 |
|  2026-07-21  SELL  CI  Pullback50  $95.97  P&L $-0.17                  |
|  2026-07-21  SELL  IEX  Pullback50  $70.78  P&L $-0.49                 |
|  2026-07-21  SELL  MAA  Pullback50  $95.80  P&L $-0.55                 |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=0 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=2
  zombies_flagged=0
options_reconcile: done
Layout: controlled:140:c000_s173_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:140:c000_s173_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      140
=== options_morning_bot (PAPER) 2026-07-22T09:15:38.379712-04:00 ===

[Run context]
After hours (09:15 ET) — exit summary only.
Paper auth OK — equity $130167.33, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $130,167.33                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=258  buckets=22  win=32%                             |
|  Returns   avg=-1.7%  med=-35.3%  p10=-65.3%  p90=+83.9%               |
|  Realized  $+4,817.13                                                  |
|  Raw incl dropped  trades=762  real=$+1,972.58                         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b51  c051_s164_w4_1120_  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  c091_s167_w4_1120_  2 100% +222.0 +222.0 +247.0 $   +293         |
|  b31  c031_s173_w4_1120_  2 100% +145.5 +145.5 +175.8 $   +192         |
|  b28  c028_s173_w1_0928_ 22  77% +50.0 +80.0 +102.0 $   +590           |
|  b58  c058_s173_w3_1045_  1 100% +59.1 +59.1 +59.1 $    +25            |
|  b56  c056_s173_w1_0928_  1 100% +47.7 +47.7 +47.7 $    +21            |
|  b57  c057_s173_w2_1005_  1 100% +47.7 +47.7 +47.7 $    +21            |
|  b89  c089_s167_w2_1005_  9  56% +84.4 +30.9 +790.0 $    +45           |
|  ... 14 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b9   c009_s165_w2_1005_  6   0% -76.2 -78.1 -92.7 $   -261       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-22.log
elapsed=1.7s reconcile=1.43s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.7s. run=#4681 https://github.com/28twagg-ops/TradingBot/actions/runs/29923063426
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 2.9% (22/762)
# Options signal frequency

_Generated 2026-07-22T09:15:43.448640_

Headline counts are **unique (strategy, underlying, date)** from `ENTRY` lines in `logs/options_trial/runs/*.log`.
Raw log-line counts (multi-bucket duplicates) are shown below for debug.

### Unique underlying symbols per day (headline)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-08 |    0 |    0 |    3 |    0 |    0 |    0 |    2 |    1 |     6 |
| 2026-07-09 |    0 |    0 |    1 |    0 |    0 |    0 |    2 |    3 |     6 |
| 2026-07-10 |    0 |    0 |    1 |    0 |    0 |    0 |    1 |    1 |     3 |
| 2026-07-13 |    0 |    0 |    2 |    0 |    0 |    0 |    3 |    2 |     7 |
| 2026-07-14 |    0 |    0 |    3 |    0 |    0 |    0 |    2 |    0 |     5 |
| 2026-07-16 |    0 |    0 |    2 |    0 |    0 |    0 |    3 |    0 |     5 |
| 2026-07-17 |    0 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |     4 |
| 2026-07-20 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-21 |    1 |    2 |    1 |    1 |    2 |    2 |    0 |    0 |     9 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 1 | 1 | 1.0 | ~38 active signal-days |
| S164 | 2 | 1 | 2.0 | ~19 active signal-days |
| S165 | 15 | 8 | 1.9 | ~20 active signal-days |
| S166 | 1 | 1 | 1.0 | ~38 active signal-days |
| S167 | 2 | 1 | 2.0 | ~19 active signal-days |
| S168 | 2 | 1 | 2.0 | ~19 active signal-days |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 45 | 1 |
| S164 | 55 | 2 |
| S165 | 1488 | 15 |
| S166 | 45 | 1 |
| S167 | 55 | 2 |
| S168 | 55 | 2 |
| S173 | 1831 | 17 |
| S174 | 891 | 7 |

### Raw log lines per day (debug / multi-bucket)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |    0 |   100 |
| 2026-07-08 |    0 |    0 |  100 |    0 |    0 |    0 |  100 |  100 |   300 |
| 2026-07-09 |    0 |    0 |   24 |    0 |    0 |    0 |  100 |   15 |   139 |
| 2026-07-10 |    0 |    0 |  242 |    0 |    0 |    0 |  230 |  202 |   674 |
| 2026-07-13 |    0 |    0 |  190 |    0 |    0 |    0 |  212 |  188 |   590 |
| 2026-07-14 |    0 |    0 |  194 |    0 |    0 |    0 |  185 |  106 |   485 |
| 2026-07-15 |    0 |    0 |  146 |    0 |    0 |    0 |  154 |   58 |   358 |
| 2026-07-16 |    0 |    0 |  179 |    0 |    0 |    0 |  205 |   58 |   442 |
| 2026-07-17 |    0 |    0 |  127 |    0 |    0 |    0 |  207 |   58 |   392 |
| 2026-07-20 |    0 |    0 |  107 |    0 |    0 |    0 |  143 |   58 |   308 |
| 2026-07-21 |   30 |   35 |  113 |   30 |   35 |   35 |  118 |   48 |   444 |
| 2026-07-22 |   15 |   20 |   66 |   15 |   20 |   20 |   77 |    0 |   233 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-07-22
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |     7 | WARN | <<<
| Missing exit records (post) |     7 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |   297 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   616 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=480.7 router=CONFIRMED leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---

## Run 20260722T132039Z

- UTC timestamp: `20260722T132039Z`
- GitHub run: [#4682](https://github.com/28twagg-ops/TradingBot/actions/runs/29923420825)
- Run id: `29923420825`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`8s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-22T09:20:43.198988-04:00","date":"2026-07-22","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":2.3,"phases_s":{"reconcile":1.84},"signals":0,"placed":0,"equity":130435.33,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4682","github_run_id":"29923420825","status":"ok"}
```

### Live bot full output

```text
13:20:40  INFO      Mode: summary
13:20:41  INFO        Daily log -> logs/daily/2026-07-22.md
13:20:41  INFO        Daily log reconciled -> logs/daily/2026-07-22.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $480.70|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $480.70|
|  Cash                                                           $120.06|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $360.64|
|  Open P&L                                                        $+1.98|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (4 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  BIIB     Pullback50      $96.83     $201.84  $203.16  +0.7%   $+0.63  |
|  C        Pullback50      $70.07     $132.61  $133.00  +0.3%   $+0.21  |
|  DUK      Pullback50      $96.94     $125.11  $126.01  +0.7%   $+0.69  |
|  TPR      Pullback50      $96.80     $140.84  $141.50  +0.5%   $+0.45  |
|                                                                        |
|  Total invested                                                 $360.64|
|  Total open P&L                                                  $+1.98|
+========================================================================+

+========================================================================+
|                        EXIT LOGIC ACTIVE  (v8)                         |
+========================================================================+
|  Profit target                              price > 20-day MA (midline)|
|  Stop loss                                             -0.5% from entry|
|  Time stop                                          max 3 calendar days|
+========================================================================+

+========================================================================+
|                          RECENT TRANSACTIONS                           |
+========================================================================+
|  2026-07-21  SELL  APA  Pullback50  $96.03  P&L $-0.00                 |
|  2026-07-21  SELL  BEN  Pullback50  $5.47  P&L $-0.09                  |
|  2026-07-21  SELL  CNP  Pullback50  $10.28  P&L $-0.06                 |
|  2026-07-21  SELL  CI  Pullback50  $95.97  P&L $-0.17                  |
|  2026-07-21  SELL  IEX  Pullback50  $70.78  P&L $-0.49                 |
|  2026-07-21  SELL  MAA  Pullback50  $95.80  P&L $-0.55                 |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=0 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=2
  zombies_flagged=0
options_reconcile: done
Layout: controlled:140:c000_s173_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:140:c000_s173_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      140
=== options_morning_bot (PAPER) 2026-07-22T09:20:43.198988-04:00 ===

[Run context]
After hours (09:20 ET) — exit summary only.
Paper auth OK — equity $130435.33, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $130,435.33                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=258  buckets=22  win=32%                             |
|  Returns   avg=-1.7%  med=-35.3%  p10=-65.3%  p90=+83.9%               |
|  Realized  $+4,817.13                                                  |
|  Raw incl dropped  trades=762  real=$+1,972.58                         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b51  c051_s164_w4_1120_  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  c091_s167_w4_1120_  2 100% +222.0 +222.0 +247.0 $   +293         |
|  b31  c031_s173_w4_1120_  2 100% +145.5 +145.5 +175.8 $   +192         |
|  b28  c028_s173_w1_0928_ 22  77% +50.0 +80.0 +102.0 $   +590           |
|  b58  c058_s173_w3_1045_  1 100% +59.1 +59.1 +59.1 $    +25            |
|  b56  c056_s173_w1_0928_  1 100% +47.7 +47.7 +47.7 $    +21            |
|  b57  c057_s173_w2_1005_  1 100% +47.7 +47.7 +47.7 $    +21            |
|  b89  c089_s167_w2_1005_  9  56% +84.4 +30.9 +790.0 $    +45           |
|  ... 14 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b9   c009_s165_w2_1005_  6   0% -76.2 -78.1 -92.7 $   -261       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-22.log
elapsed=2.3s reconcile=1.84s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=2.3s. run=#4682 https://github.com/28twagg-ops/TradingBot/actions/runs/29923420825
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 2.9% (22/762)
# Options signal frequency

_Generated 2026-07-22T09:20:48.940638_

Headline counts are **unique (strategy, underlying, date)** from `ENTRY` lines in `logs/options_trial/runs/*.log`.
Raw log-line counts (multi-bucket duplicates) are shown below for debug.

### Unique underlying symbols per day (headline)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-08 |    0 |    0 |    3 |    0 |    0 |    0 |    2 |    1 |     6 |
| 2026-07-09 |    0 |    0 |    1 |    0 |    0 |    0 |    2 |    3 |     6 |
| 2026-07-10 |    0 |    0 |    1 |    0 |    0 |    0 |    1 |    1 |     3 |
| 2026-07-13 |    0 |    0 |    2 |    0 |    0 |    0 |    3 |    2 |     7 |
| 2026-07-14 |    0 |    0 |    3 |    0 |    0 |    0 |    2 |    0 |     5 |
| 2026-07-16 |    0 |    0 |    2 |    0 |    0 |    0 |    3 |    0 |     5 |
| 2026-07-17 |    0 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |     4 |
| 2026-07-20 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-21 |    1 |    2 |    1 |    1 |    2 |    2 |    0 |    0 |     9 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 1 | 1 | 1.0 | ~38 active signal-days |
| S164 | 2 | 1 | 2.0 | ~19 active signal-days |
| S165 | 15 | 8 | 1.9 | ~20 active signal-days |
| S166 | 1 | 1 | 1.0 | ~38 active signal-days |
| S167 | 2 | 1 | 2.0 | ~19 active signal-days |
| S168 | 2 | 1 | 2.0 | ~19 active signal-days |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 45 | 1 |
| S164 | 55 | 2 |
| S165 | 1488 | 15 |
| S166 | 45 | 1 |
| S167 | 55 | 2 |
| S168 | 55 | 2 |
| S173 | 1831 | 17 |
| S174 | 891 | 7 |

### Raw log lines per day (debug / multi-bucket)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |    0 |   100 |
| 2026-07-08 |    0 |    0 |  100 |    0 |    0 |    0 |  100 |  100 |   300 |
| 2026-07-09 |    0 |    0 |   24 |    0 |    0 |    0 |  100 |   15 |   139 |
| 2026-07-10 |    0 |    0 |  242 |    0 |    0 |    0 |  230 |  202 |   674 |
| 2026-07-13 |    0 |    0 |  190 |    0 |    0 |    0 |  212 |  188 |   590 |
| 2026-07-14 |    0 |    0 |  194 |    0 |    0 |    0 |  185 |  106 |   485 |
| 2026-07-15 |    0 |    0 |  146 |    0 |    0 |    0 |  154 |   58 |   358 |
| 2026-07-16 |    0 |    0 |  179 |    0 |    0 |    0 |  205 |   58 |   442 |
| 2026-07-17 |    0 |    0 |  127 |    0 |    0 |    0 |  207 |   58 |   392 |
| 2026-07-20 |    0 |    0 |  107 |    0 |    0 |    0 |  143 |   58 |   308 |
| 2026-07-21 |   30 |   35 |  113 |   30 |   35 |   35 |  118 |   48 |   444 |
| 2026-07-22 |   15 |   20 |   66 |   15 |   20 |   20 |   77 |    0 |   233 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-07-22
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |     7 | WARN | <<<
| Missing exit records (post) |     7 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |   297 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   616 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=480.7 router=CONFIRMED leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---

## Run 20260722T132540Z

- UTC timestamp: `20260722T132540Z`
- GitHub run: [#4683](https://github.com/28twagg-ops/TradingBot/actions/runs/29923786253)
- Run id: `29923786253`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`7s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-22T09:25:44.966471-04:00","date":"2026-07-22","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.7,"phases_s":{"reconcile":1.39},"signals":0,"placed":0,"equity":130535.33,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4683","github_run_id":"29923786253","status":"ok"}
```

### Live bot full output

```text
13:25:42  INFO      Mode: summary
13:25:42  INFO        Daily log -> logs/daily/2026-07-22.md
13:25:42  INFO        Daily log reconciled -> logs/daily/2026-07-22.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:25 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $480.85|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $480.85|
|  Cash                                                           $120.06|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $360.79|
|  Open P&L                                                        $+2.13|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (4 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  BIIB     Pullback50      $96.83     $201.84  $203.16  +0.7%   $+0.63  |
|  C        Pullback50      $70.21     $132.61  $133.28  +0.5%   $+0.35  |
|  DUK      Pullback50      $96.94     $125.11  $126.01  +0.7%   $+0.69  |
|  TPR      Pullback50      $96.80     $140.84  $141.50  +0.5%   $+0.45  |
|                                                                        |
|  Total invested                                                 $360.79|
|  Total open P&L                                                  $+2.13|
+========================================================================+

+========================================================================+
|                        EXIT LOGIC ACTIVE  (v8)                         |
+========================================================================+
|  Profit target                              price > 20-day MA (midline)|
|  Stop loss                                             -0.5% from entry|
|  Time stop                                          max 3 calendar days|
+========================================================================+

+========================================================================+
|                          RECENT TRANSACTIONS                           |
+========================================================================+
|  2026-07-21  SELL  APA  Pullback50  $96.03  P&L $-0.00                 |
|  2026-07-21  SELL  BEN  Pullback50  $5.47  P&L $-0.09                  |
|  2026-07-21  SELL  CNP  Pullback50  $10.28  P&L $-0.06                 |
|  2026-07-21  SELL  CI  Pullback50  $95.97  P&L $-0.17                  |
|  2026-07-21  SELL  IEX  Pullback50  $70.78  P&L $-0.49                 |
|  2026-07-21  SELL  MAA  Pullback50  $95.80  P&L $-0.55                 |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=0 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=2
  zombies_flagged=0
options_reconcile: done
Layout: controlled:140:c000_s173_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:140:c000_s173_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      140
=== options_morning_bot (PAPER) 2026-07-22T09:25:44.966471-04:00 ===

[Run context]
After hours (09:25 ET) — exit summary only.
Paper auth OK — equity $130535.33, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $130,535.33                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=258  buckets=22  win=32%                             |
|  Returns   avg=-1.7%  med=-35.3%  p10=-65.3%  p90=+83.9%               |
|  Realized  $+4,817.13                                                  |
|  Raw incl dropped  trades=762  real=$+1,972.58                         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b51  c051_s164_w4_1120_  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  c091_s167_w4_1120_  2 100% +222.0 +222.0 +247.0 $   +293         |
|  b31  c031_s173_w4_1120_  2 100% +145.5 +145.5 +175.8 $   +192         |
|  b28  c028_s173_w1_0928_ 22  77% +50.0 +80.0 +102.0 $   +590           |
|  b58  c058_s173_w3_1045_  1 100% +59.1 +59.1 +59.1 $    +25            |
|  b56  c056_s173_w1_0928_  1 100% +47.7 +47.7 +47.7 $    +21            |
|  b57  c057_s173_w2_1005_  1 100% +47.7 +47.7 +47.7 $    +21            |
|  b89  c089_s167_w2_1005_  9  56% +84.4 +30.9 +790.0 $    +45           |
|  ... 14 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b9   c009_s165_w2_1005_  6   0% -76.2 -78.1 -92.7 $   -261       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-22.log
elapsed=1.7s reconcile=1.39s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.7s. run=#4683 https://github.com/28twagg-ops/TradingBot/actions/runs/29923786253
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 2.9% (22/762)
# Options signal frequency

_Generated 2026-07-22T09:25:50.004477_

Headline counts are **unique (strategy, underlying, date)** from `ENTRY` lines in `logs/options_trial/runs/*.log`.
Raw log-line counts (multi-bucket duplicates) are shown below for debug.

### Unique underlying symbols per day (headline)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-08 |    0 |    0 |    3 |    0 |    0 |    0 |    2 |    1 |     6 |
| 2026-07-09 |    0 |    0 |    1 |    0 |    0 |    0 |    2 |    3 |     6 |
| 2026-07-10 |    0 |    0 |    1 |    0 |    0 |    0 |    1 |    1 |     3 |
| 2026-07-13 |    0 |    0 |    2 |    0 |    0 |    0 |    3 |    2 |     7 |
| 2026-07-14 |    0 |    0 |    3 |    0 |    0 |    0 |    2 |    0 |     5 |
| 2026-07-16 |    0 |    0 |    2 |    0 |    0 |    0 |    3 |    0 |     5 |
| 2026-07-17 |    0 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |     4 |
| 2026-07-20 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-21 |    1 |    2 |    1 |    1 |    2 |    2 |    0 |    0 |     9 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 1 | 1 | 1.0 | ~38 active signal-days |
| S164 | 2 | 1 | 2.0 | ~19 active signal-days |
| S165 | 15 | 8 | 1.9 | ~20 active signal-days |
| S166 | 1 | 1 | 1.0 | ~38 active signal-days |
| S167 | 2 | 1 | 2.0 | ~19 active signal-days |
| S168 | 2 | 1 | 2.0 | ~19 active signal-days |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 45 | 1 |
| S164 | 55 | 2 |
| S165 | 1488 | 15 |
| S166 | 45 | 1 |
| S167 | 55 | 2 |
| S168 | 55 | 2 |
| S173 | 1831 | 17 |
| S174 | 891 | 7 |

### Raw log lines per day (debug / multi-bucket)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |    0 |   100 |
| 2026-07-08 |    0 |    0 |  100 |    0 |    0 |    0 |  100 |  100 |   300 |
| 2026-07-09 |    0 |    0 |   24 |    0 |    0 |    0 |  100 |   15 |   139 |
| 2026-07-10 |    0 |    0 |  242 |    0 |    0 |    0 |  230 |  202 |   674 |
| 2026-07-13 |    0 |    0 |  190 |    0 |    0 |    0 |  212 |  188 |   590 |
| 2026-07-14 |    0 |    0 |  194 |    0 |    0 |    0 |  185 |  106 |   485 |
| 2026-07-15 |    0 |    0 |  146 |    0 |    0 |    0 |  154 |   58 |   358 |
| 2026-07-16 |    0 |    0 |  179 |    0 |    0 |    0 |  205 |   58 |   442 |
| 2026-07-17 |    0 |    0 |  127 |    0 |    0 |    0 |  207 |   58 |   392 |
| 2026-07-20 |    0 |    0 |  107 |    0 |    0 |    0 |  143 |   58 |   308 |
| 2026-07-21 |   30 |   35 |  113 |   30 |   35 |   35 |  118 |   48 |   444 |
| 2026-07-22 |   15 |   20 |   66 |   15 |   20 |   20 |   77 |    0 |   233 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-07-22
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |     7 | WARN | <<<
| Missing exit records (post) |     7 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |   297 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   616 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=480.85 router=CONFIRMED leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---
