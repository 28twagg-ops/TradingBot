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

## Run 20260722T133035Z

- UTC timestamp: `20260722T133035Z`
- GitHub run: [#4684](https://github.com/28twagg-ops/TradingBot/actions/runs/29924155391)
- Run id: `29924155391`
- Live bot: exit=`0`, duration=`214s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-22T09:25:44.966471-04:00","date":"2026-07-22","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.7,"phases_s":{"reconcile":1.39},"signals":0,"placed":0,"equity":130535.33,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4683","github_run_id":"29923786253","status":"ok"}
```

### Live bot full output

```text
13:30:36  INFO      Mode: morning_prep
13:30:37  INFO        [prep_positions] 4/4 (4 valid)
13:30:37  INFO      Fetching tickers (universe=both)...
13:30:38  INFO        S&P 500: 503
13:30:38  INFO        MidCap 400: 400
13:30:38  INFO        Total: 903 tickers
13:30:39  INFO        [prep_universe] 40/899 (40 valid)
13:30:41  INFO        [prep_universe] 80/899 (80 valid)
13:30:43  INFO        [prep_universe] 120/899 (120 valid)
13:30:44  INFO        [prep_universe] 160/899 (160 valid)
13:30:46  INFO        [prep_universe] 200/899 (199 valid)
13:30:53  INFO        [prep_universe] 240/899 (238 valid)
13:31:04  INFO        [prep_universe] 280/899 (278 valid)
13:31:15  INFO        [prep_universe] 320/899 (318 valid)
13:31:29  INFO        [prep_universe] 360/899 (358 valid)
13:31:39  INFO        [prep_universe] 400/899 (397 valid)
13:31:52  INFO        [prep_universe] 440/899 (437 valid)
13:32:03  INFO        [prep_universe] 480/899 (477 valid)
13:32:16  INFO        [prep_universe] 520/899 (517 valid)
13:32:29  INFO        [prep_universe] 560/899 (556 valid)
13:32:39  INFO        [prep_universe] 600/899 (596 valid)
13:32:52  INFO        [prep_universe] 640/899 (636 valid)
13:33:05  INFO        [prep_universe] 680/899 (676 valid)
13:33:15  INFO        [prep_universe] 720/899 (715 valid)
13:33:28  INFO        [prep_universe] 760/899 (755 valid)
13:33:38  INFO        [prep_universe] 800/899 (795 valid)
13:33:51  INFO        [prep_universe] 840/899 (834 valid)
13:34:04  INFO        [prep_universe] 880/899 (874 valid)
13:34:08  INFO        [prep_universe] 899/899 (893 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:30 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $481.26|
+========================================================================+

+========================================================================+
|                              MORNING PREP                              |
+========================================================================+
|  Goal                   Precompute exits/signals for next execution run|
|  Plan file                                 logs/plans/morning_plan.json|
|  Regime                                                            BULL|
+========================================================================+

+========================================================================+
|                       OPEN POSITION P&L SNAPSHOT                       |
+========================================================================+
|  Open positions                                                       4|
|  Invested                                                       $361.20|
|  Open P&L                                                        $+2.54|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  BIIB     Pullback50      $96.86     $201.84  $203.23  +0.7%   $+0.66  |
|  C        Pullback50      $69.92     $132.61  $132.72  +0.1%   $+0.06  |
|  DUK      Pullback50      $97.52     $125.11  $126.77  +1.3%   $+1.27  |
|  TPR      Pullback50      $96.90     $140.84  $141.64  +0.6%   $+0.55  |
+========================================================================+

+========================================================================+
|                            OPEN SELL ORDERS                            |
+========================================================================+
|  Count                                                                0|
|                                                                        |
|  No open sell orders.                                                  |
|                                                                        |
+========================================================================+

+========================================================================+
|                              PREP SUMMARY                              |
+========================================================================+
|  Saved                                                              yes|
|  Exit candidates                                                      0|
|  Signal candidates                                                   25|
|  Universe scanned                                                   899|
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
=== options_morning_bot (PAPER) 2026-07-22T09:34:10.769448-04:00 ===

[Run context]
Paper auth OK — equity $131665.29, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 299 signal(s); top: ['S165:AMD', 'S165:APH', 'S165:AMAT', 'S165:CB', 'S165:CIEN', 'S165:COHR', 'S165:COIN', 'S165:FIX']
Paper lab: $131735 broker equity -> 140 bucket(s) ($500 virtual each, unlimited paper)
```

---

## Run 20260722T133556Z

- UTC timestamp: `20260722T133556Z`
- GitHub run: [#4685](https://github.com/28twagg-ops/TradingBot/actions/runs/29924542274)
- Run id: `29924542274`
- Live bot: exit=`0`, duration=`226s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-22T09:25:44.966471-04:00","date":"2026-07-22","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.7,"phases_s":{"reconcile":1.39},"signals":0,"placed":0,"equity":130535.33,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4683","github_run_id":"29923786253","status":"ok"}
```

### Live bot full output

```text
13:35:57  INFO      Mode: morning_prep
13:35:58  INFO        [prep_positions] 4/4 (4 valid)
13:35:58  INFO      Fetching tickers (universe=both)...
13:35:58  INFO        S&P 500: 503
13:35:58  INFO        MidCap 400: 400
13:35:58  INFO        Total: 903 tickers
13:35:59  INFO        [prep_universe] 40/899 (40 valid)
13:36:01  INFO        [prep_universe] 80/899 (80 valid)
13:36:02  INFO        [prep_universe] 120/899 (120 valid)
13:36:03  INFO        [prep_universe] 160/899 (160 valid)
13:36:11  INFO        [prep_universe] 200/899 (199 valid)
13:36:24  INFO        [prep_universe] 240/899 (238 valid)
13:36:35  INFO        [prep_universe] 280/899 (278 valid)
13:36:47  INFO        [prep_universe] 320/899 (318 valid)
13:37:00  INFO        [prep_universe] 360/899 (358 valid)
13:37:10  INFO        [prep_universe] 400/899 (397 valid)
13:37:23  INFO        [prep_universe] 440/899 (437 valid)
13:37:37  INFO        [prep_universe] 480/899 (477 valid)
13:37:47  INFO        [prep_universe] 520/899 (517 valid)
13:38:00  INFO        [prep_universe] 560/899 (556 valid)
13:38:12  INFO        [prep_universe] 600/899 (596 valid)
13:38:22  INFO        [prep_universe] 640/899 (636 valid)
13:38:35  INFO        [prep_universe] 680/899 (676 valid)
13:38:48  INFO        [prep_universe] 720/899 (715 valid)
13:38:58  INFO        [prep_universe] 760/899 (755 valid)
13:39:11  INFO        [prep_universe] 800/899 (795 valid)
13:39:24  INFO        [prep_universe] 840/899 (834 valid)
13:39:37  INFO        [prep_universe] 880/899 (874 valid)
13:39:41  INFO        [prep_universe] 899/899 (893 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:35 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $481.64|
+========================================================================+

+========================================================================+
|                              MORNING PREP                              |
+========================================================================+
|  Goal                   Precompute exits/signals for next execution run|
|  Plan file                                 logs/plans/morning_plan.json|
|  Regime                                                            BULL|
+========================================================================+

+========================================================================+
|                       OPEN POSITION P&L SNAPSHOT                       |
+========================================================================+
|  Open positions                                                       4|
|  Invested                                                       $361.58|
|  Open P&L                                                        $+2.92|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  BIIB     Pullback50      $96.89     $201.84  $203.28  +0.7%   $+0.69  |
|  C        Pullback50      $70.21     $132.61  $133.26  +0.5%   $+0.35  |
|  DUK      Pullback50      $97.60     $125.11  $126.87  +1.4%   $+1.35  |
|  TPR      Pullback50      $96.89     $140.84  $141.62  +0.6%   $+0.54  |
+========================================================================+

+========================================================================+
|                            OPEN SELL ORDERS                            |
+========================================================================+
|  Count                                                                0|
|                                                                        |
|  No open sell orders.                                                  |
|                                                                        |
+========================================================================+

+========================================================================+
|                              PREP SUMMARY                              |
+========================================================================+
|  Saved                                                              yes|
|  Exit candidates                                                      1|
|  Signal candidates                                                   27|
|  Universe scanned                                                   899|
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=0 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=3
  zombies_flagged=0
options_reconcile: done
Layout: controlled:140:c000_s173_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:140:c000_s173_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      140
=== options_morning_bot (PAPER) 2026-07-22T09:39:43.788770-04:00 ===

[Run context]
Paper auth OK — equity $132481.29, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163] …
```

---

## Run 20260722T134105Z

- UTC timestamp: `20260722T134105Z`
- GitHub run: [#4686](https://github.com/28twagg-ops/TradingBot/actions/runs/29924922368)
- Run id: `29924922368`
- Live bot: exit=`0`, duration=`215s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-22T09:25:44.966471-04:00","date":"2026-07-22","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.7,"phases_s":{"reconcile":1.39},"signals":0,"placed":0,"equity":130535.33,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4683","github_run_id":"29923786253","status":"ok"}
```

### Live bot full output

```text
13:41:05  INFO      Mode: morning_prep
13:41:07  INFO        [prep_positions] 4/4 (4 valid)
13:41:07  INFO        Universe cache hit: 903 tickers (tickers_2026-07-22.json)
13:41:08  INFO        [prep_universe] 40/899 (40 valid)
13:41:09  INFO        [prep_universe] 80/899 (80 valid)
13:41:10  INFO        [prep_universe] 120/899 (120 valid)
13:41:11  INFO        [prep_universe] 160/899 (160 valid)
13:41:12  INFO        [prep_universe] 200/899 (199 valid)
13:41:22  INFO        [prep_universe] 240/899 (238 valid)
13:41:32  INFO        [prep_universe] 280/899 (278 valid)
13:41:45  INFO        [prep_universe] 320/899 (318 valid)
13:41:58  INFO        [prep_universe] 360/899 (358 valid)
13:42:08  INFO        [prep_universe] 400/899 (397 valid)
13:42:21  INFO        [prep_universe] 440/899 (437 valid)
13:42:31  INFO        [prep_universe] 480/899 (477 valid)
13:42:45  INFO        [prep_universe] 520/899 (517 valid)
13:42:58  INFO        [prep_universe] 560/899 (556 valid)
13:43:08  INFO        [prep_universe] 600/899 (596 valid)
13:43:21  INFO        [prep_universe] 640/899 (636 valid)
13:43:34  INFO        [prep_universe] 680/899 (676 valid)
13:43:43  INFO        [prep_universe] 720/899 (715 valid)
13:43:56  INFO        [prep_universe] 760/899 (755 valid)
13:44:09  INFO        [prep_universe] 800/899 (795 valid)
13:44:19  INFO        [prep_universe] 840/899 (834 valid)
13:44:33  INFO        [prep_universe] 880/899 (874 valid)
13:44:39  INFO        [prep_universe] 899/899 (893 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.92|
+========================================================================+

+========================================================================+
|                              MORNING PREP                              |
+========================================================================+
|  Goal                   Precompute exits/signals for next execution run|
|  Plan file                                 logs/plans/morning_plan.json|
|  Regime                                                            BULL|
+========================================================================+

+========================================================================+
|                       OPEN POSITION P&L SNAPSHOT                       |
+========================================================================+
|  Open positions                                                       4|
|  Invested                                                       $362.86|
|  Open P&L                                                        $+4.20|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  BIIB     Pullback50      $97.37     $201.84  $204.31  +1.2%   $+1.17  |
|  C        Pullback50      $69.99     $132.61  $132.85  +0.2%   $+0.13  |
|  DUK      Pullback50      $97.55     $125.11  $126.80  +1.3%   $+1.30  |
|  TPR      Pullback50      $97.95     $140.84  $143.18  +1.7%   $+1.60  |
+========================================================================+

+========================================================================+
|                            OPEN SELL ORDERS                            |
+========================================================================+
|  Count                                                                0|
|                                                                        |
|  No open sell orders.                                                  |
|                                                                        |
+========================================================================+

+========================================================================+
|                              PREP SUMMARY                              |
+========================================================================+
|  Saved                                                              yes|
|  Exit candidates                                                      2|
|  Signal candidates                                                   38|
|  Universe scanned                                                   899|
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=0 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=3
  zombies_flagged=0
options_reconcile: done
Layout: controlled:140:c000_s173_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:140:c000_s173_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      140
=== options_morning_bot (PAPER) 2026-07-22T09:44:41.464308-04:00 ===

[Run context]
Paper auth OK — equity $132731.29, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163] …
```

---

## Run 20260722T134601Z

- UTC timestamp: `20260722T134601Z`
- GitHub run: [#4687](https://github.com/28twagg-ops/TradingBot/actions/runs/29925314245)
- Run id: `29925314245`
- Live bot: exit=`0`, duration=`228s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-22T09:25:44.966471-04:00","date":"2026-07-22","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.7,"phases_s":{"reconcile":1.39},"signals":0,"placed":0,"equity":130535.33,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4683","github_run_id":"29923786253","status":"ok"}
```

### Live bot full output

```text
13:46:02  INFO      Mode: morning_scan
13:46:03  INFO        [positions] 4/4 (4 valid)
13:46:03  INFO        Universe cache hit: 903 tickers (tickers_2026-07-22.json)
13:46:04  INFO        [universe] 40/899 (40 valid)
13:46:06  INFO        [universe] 80/899 (80 valid)
13:46:07  INFO        [universe] 120/899 (120 valid)
13:46:08  INFO        [universe] 160/899 (160 valid)
13:46:10  INFO        [universe] 200/899 (199 valid)
13:46:17  INFO        [universe] 240/899 (238 valid)
13:46:30  INFO        [universe] 280/899 (278 valid)
13:46:43  INFO        [universe] 320/899 (318 valid)
13:46:53  INFO        [universe] 360/899 (358 valid)
13:47:06  INFO        [universe] 400/899 (397 valid)
13:47:19  INFO        [universe] 440/899 (437 valid)
13:47:30  INFO        [universe] 480/899 (477 valid)
13:47:43  INFO        [universe] 520/899 (517 valid)
13:47:52  INFO        [universe] 560/899 (556 valid)
13:48:06  INFO        [universe] 600/899 (596 valid)
13:48:18  INFO        [universe] 640/899 (636 valid)
13:48:29  INFO        [universe] 680/899 (676 valid)
13:48:42  INFO        [universe] 720/899 (715 valid)
13:48:55  INFO        [universe] 760/899 (755 valid)
13:49:05  INFO        [universe] 800/899 (795 valid)
13:49:18  INFO        [universe] 840/899 (834 valid)
13:49:31  INFO        [universe] 880/899 (874 valid)
13:49:35  INFO        [universe] 899/899 (893 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_SCAN|
|  Time                                                         13:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $481.85|
+========================================================================+

+========================================================================+
|                   RUBBER BAND BOT v8  --  DAILY SCAN                   |
+========================================================================+
|  Mode                                                      *** LIVE ***|
|  Date                                                        2026-07-22|
|  Universe                                                          both|
|  Mon~  Jul: 52wkLow + Pullback50 (display only — schedule not enforced)|
|  Disabled                GapDown, VolumeSpike (see DISABLED_STRATEGIES)|
|  Regime                                                            BULL|
|  Exit                                      midline / stop-0.5% / 3d max|
+========================================================================+

+========================================================================+
|                                ACCOUNT                                 |
+========================================================================+
|  Equity                                                         $481.85|
|  Cash                                                           $120.06|
|  Reserve                                          $24.09  (always kept)|
|  Available                                     $95.97  (for new trades)|
|  Trade size             $96.37  (20% per signal — all strategies equal)|
+========================================================================+

+========================================================================+
|                           HOLDINGS  (4 open)                           |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  BIIB     Pullback50      $96.67     $201.84  $202.82  +0.5%   $+0.47  |
|  C        Pullback50      $70.05     $132.61  $132.96  +0.3%   $+0.19  |
|  DUK      Pullback50      $97.33     $125.11  $126.51  +1.1%   $+1.08  |
|  TPR      Pullback50      $97.75     $140.84  $142.88  +1.5%   $+1.40  |
|                                                                        |
|  Total invested                                                 $361.79|
|  Total open P&L                                                  $+3.13|
|  Buys today: 0  |  entry cap: 1  |  max open: 5                        |
+========================================================================+

+========================================================================+
|                               PLAN CACHE                               |
+========================================================================+
|  Mode                                                           morning|
|  File                                      logs/plans/morning_plan.json|
|  Use cached plan                                  no (stale (18720.6m))|
+========================================================================+

+========================================================================+
|          EXIT EVALUATION  (EOD -- midline + stop + max-hold)           |
+========================================================================+
|  C  P&L +0.3%  $+0.19                                              HOLD|
|  BIIB  P&L +0.5%  $+0.47                                           HOLD|
|  DUK  P&L +1.1%  $+1.08                                            HOLD|
|  TPR  P&L +1.5%  $+1.40                                            HOLD|
+========================================================================+

+========================================================================+
|                           EXIT EVAL SUMMARY                            |
+========================================================================+
|  Exit eval    attempted 0 | filled 0 | partial 0 | pending 0 | failed 0|
|  Other skips     already logged today 0  |  no price data 0  |  holds 4|
|  Stop-loss breaches                                                none|
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+

+========================================================================+
|                             DATA DOWNLOAD                              |
+========================================================================+
|  Universe: both  |  Alpaca primary / yfinance fallback                 |
+========================================================================+

+========================================================================+
|                              SIGNAL SCAN                               |
+========================================================================+
|  Month: Jul  |  Regime: BULL                                           |
|  Primary: 52wkLow  |  Secondary: Pullback50 (display only — schedule n~|
|  Source                                                       live scan|
+========================================================================+

+========================================================================+
|                         SIGNALS FOUND  --  32                          |
+========================================================================+
|  TICKER   STRATEGY        TIER   PRICE    RSI    VOL_Z   TRIGGER       |
+------------------------------------------------------------------------+
|  BRK-B    Pullback50      eq     $491.68  41.2   -2.73   50MA bounce (+|
|  CARR     Pullback50      eq     $67.83   36.1   -2.89   50MA bounce (-|
|  CHD      Pullback50      eq     $96.72   48.7   -3.11   50MA bounce (+|
|  EMR      Pullback50      eq     $140.53  52.0   -2.15   50MA bounce (+|
|  EXR      Pullback50      eq     $145.66  46.9   -2.51   50MA bounce (+|
|  FAST     Pullback50      eq     $45.31   36.9   -2.17   50MA bounce (-|
|  FCX      Pullback50      eq     $64.00   58.4   -2.76   50MA bounce (+|
|  FTV      Pullback50      eq     $60.70   45.0   -2.91   50MA bounce (+|
|  IFF      Pullback50      eq     $77.19   39.1   -2.56   50MA bounce (+|
|  IRM      Pullback50      eq     $125.84  59.6   -3.05   50MA bounce (+|
|  JCI      Pullback50      eq     $142.41  44.7   -1.88   50MA bounce (+|
|  LYB      Pullback50      eq     $63.02   89.0   -2.97   50MA bounce (+|
|  MAA      Pullback50      eq     $132.86  35.0   -3.09   50MA bounce (-|
|  NUE      Pullback50      eq     $237.69  71.7   -2.38   50MA bounce (-|
|  PSA      Pullback50      eq     $311.13  40.4   -1.49   50MA bounce (-|
|  RCL      Pullback50      eq     $286.51  34.9   -1.64   50MA bounce (-|
|  TXT      Pullback50      eq     $91.79   49.5   -2.55   50MA bounce (+|
|  TT       Pullback50      eq     $469.96  37.7   -1.89   50MA bounce (+|
|  AAL      Pullback50      eq     $15.11   17.8   -3.02   50MA bounce (-|
|  CAR      Pullback50      eq     $165.64  66.1   -1.22   50MA bounce (-|
|  EVR      Pullback50      eq     $342.33  50.6   -3.38   50MA bounce (-|
|  HGV      Pullback50      eq     $49.70   43.9   -2.19   50MA bounce (-|
|  GNTX     Pullback50      eq     $24.23   45.7   -2.30   50MA bounce (-|
|  IRT      Pullback50      eq     $16.57   39.4   -1.57   50MA bounce (-|
|  ITT      Pullback50      eq     $192.83  56.7   -2.69   50MA bounce (-|
|  KNF      Pullback50      eq     $80.77   46.1   -1.50   50MA bounce (+|13:49:36  ERROR       BUY FAILED BRK-B: {"code":42210000,"message":"asset \"BRK-B\" not found"}
13:49:36  INFO        BUY  CARR  $95.97  [Pullback50]  id=f5aa690d-146c-4d92-824d-f12b17c9b1bc
13:49:49  INFO        place_all_stops: checking 5 positions...
13:49:49  INFO        STOP skipped BIIB: fractional (0.4766 shares) — software exit will handle it
13:49:49  INFO        STOP skipped C: fractional (0.5268 shares) — software exit will handle it
13:49:49  INFO        STOP-MARKET placed CARR  qty=1 (pos=1.4154)  stop=$67.46  id=b01d2495-1153-49fe-a9ab-14852f163839
13:49:49  INFO        STOP skipped DUK: fractional (0.7693 shares) — software exit will handle it
13:49:49  INFO        STOP skipped TPR: fractional (0.6841 shares) — software exit will handle it
13:49:49  INFO        Daily log -> logs/daily/2026-07-22.md
13:49:49  INFO        Dashboard written → logs/dashboard.md

|  ONTO     Pullback50      eq     $295.00  36.6   -2.27   50MA bounce (+|
|  PVH      Pullback50      eq     $80.84   63.6   -2.86   50MA bounce (-|
|  RRX      Pullback50      eq     $211.44  34.2   -1.98   50MA bounce (+|
|  RS       Pullback50      eq     $387.56  64.4   -1.78   50MA bounce (+|
|  TLN      Pullback50      eq     $374.42  55.5   -1.98   50MA bounce (-|
|  TREX     Pullback50      eq     $43.40   30.1   -1.96   50MA bounce (-|
|                                                                        |
+========================================================================+

+========================================================================+
|                              ENTRY ORDERS                              |
+========================================================================+
|    ENTER [eq] BRK-B  Pullback50                                  $95.97|
|    ENTER [eq] CARR  Pullback50                                   $95.97|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    SKIP [eq] CHD  Pullback50                                      cap 5|
|    SKIP [eq] EMR  Pullback50                                      cap 5|
|    SKIP [eq] EXR  Pullback50                                      cap 5|
|    SKIP [eq] FAST  Pullback50                                     cap 5|
|    SKIP [eq] FCX  Pullback50                                      cap 5|
|    SKIP [eq] FTV  Pullback50                                      cap 5|
|    SKIP [eq] IFF  Pullback50                                      cap 5|
|    SKIP [eq] IRM  Pullback50                                      cap 5|
|    SKIP [eq] JCI  Pullback50                                      cap 5|
|    SKIP [eq] LYB  Pullback50                                      cap 5|
|    SKIP [eq] MAA  Pullback50                                      cap 5|
|    SKIP [eq] NUE  Pullback50                                      cap 5|
|    SKIP [eq] PSA  Pullback50                                      cap 5|
|    SKIP [eq] RCL  Pullback50                                      cap 5|
|    SKIP [eq] TXT  Pullback50                                      cap 5|
|    SKIP [eq] TT  Pullback50                                       cap 5|
|    SKIP [eq] AAL  Pullback50                                      cap 5|
|    SKIP [eq] CAR  Pullback50                                      cap 5|
|    SKIP [eq] EVR  Pullback50                                      cap 5|
|    SKIP [eq] HGV  Pullback50                                      cap 5|
|    SKIP [eq] GNTX  Pullback50                                     cap 5|
|    SKIP [eq] IRT  Pullback50                                      cap 5|
|    SKIP [eq] ITT  Pullback50                                      cap 5|
|    SKIP [eq] KNF  Pullback50                                      cap 5|
|    SKIP [eq] ONTO  Pullback50                                     cap 5|
|    SKIP [eq] PVH  Pullback50                                      cap 5|
|    SKIP [eq] RRX  Pullback50                                      cap 5|
|    SKIP [eq] RS  Pullback50                                       cap 5|
|    SKIP [eq] TLN  Pullback50                                      cap 5|
|    SKIP [eq] TREX  Pullback50                                     cap 5|

+========================================================================+
|                         BUY FILL CONFIRMATION                          |
+========================================================================+
|  Pending submits                                                      1|
+------------------------------------------------------------------------+
|  CARR                                                 still unconfirmed|
+========================================================================+
+========================================================================+

+========================================================================+
|                           GTC STOP PLACEMENT                           |
+========================================================================+
|  Waiting 5s for 1 buy submit(s) to settle...                           |
+========================================================================+

+========================================================================+
|                            SESSION SUMMARY                             |
+========================================================================+
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Strategy   52wkLow + Pullback50 (display only — schedule not enforced)|
|  Scanned                                                            893|
|  Signals                                                             32|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  1 unconfirmed|
|  Exits                                                                0|
|  Open pos                                                             5|
|  Equity                                                         $481.65|
|  Cash                                                            $24.09|
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=2 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=3
  zombies_flagged=2
  FLAG b48|S164|43984859 zombie age_min=830 notional=$58.00 occ=AMD260722C00575000 action=submitted:830eee3d-dc54-43ae-b0f6-ba44fcb2a0c2
  FLAG b20|S164|9fc607f2 zombie age_min=830 notional=$58.00 occ=AMD260722C00575000 action=submitted:ceaf0697-a83b-45d5-9357-d50124494f13
options_reconcile: done
Layout: controlled:140:c000_s173_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:140:c000_s173_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      140
=== options_morning_bot (PAPER) 2026-07-22T09:49:51.883273-04:00 ===

[Run context]
Paper auth OK — equity $132205.25, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163] …
```

---

## Run 20260722T135105Z

- UTC timestamp: `20260722T135105Z`
- GitHub run: [#4688](https://github.com/28twagg-ops/TradingBot/actions/runs/29925697379)
- Run id: `29925697379`
- Live bot: exit=`0`, duration=`0s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-22T09:25:44.966471-04:00","date":"2026-07-22","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.7,"phases_s":{"reconcile":1.39},"signals":0,"placed":0,"equity":130535.33,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4683","github_run_id":"29923786253","status":"ok"}
```

### Live bot full output

```text
13:51:06  INFO      Mode: morning_scan
13:51:07  INFO        [positions] 5/5 (5 valid)
13:51:07  INFO        SELL LIMIT DUK  qty=0.769322995  limit=$126.70  id=cc17ebae-bc3d-4409-85fc-2d9f22f8a722
13:51:37  INFO        SELL LIMIT filled DUK (confirmed by position check)
13:51:37  INFO        TX logged: SELL DUK  P&L 1.47%
13:51:37  INFO        Universe cache hit: 903 tickers (tickers_2026-07-22.json)
13:51:38  INFO        [universe] 40/899 (40 valid)
13:51:40  INFO        [universe] 80/899 (80 valid)
13:51:41  INFO        [universe] 120/899 (120 valid)
13:51:42  INFO        [universe] 160/899 (160 valid)
13:51:43  INFO        [universe] 200/899 (199 valid)
13:51:51  INFO        [universe] 240/899 (238 valid)
13:52:04  INFO        [universe] 280/899 (278 valid)
13:52:14  INFO        [universe] 320/899 (318 valid)
13:52:28  INFO        [universe] 360/899 (358 valid)
13:52:38  INFO        [universe] 400/899 (397 valid)
13:52:51  INFO        [universe] 440/899 (437 valid)
13:53:01  INFO        [universe] 480/899 (477 valid)
13:53:14  INFO        [universe] 520/899 (517 valid)
13:53:27  INFO        [universe] 560/899 (556 valid)
13:53:38  INFO        [universe] 600/899 (596 valid)
```

### Options bot full output

```text

## Run 20260722T135427Z

- UTC timestamp: `20260722T135427Z`
- GitHub run: [#4689](https://github.com/28twagg-ops/TradingBot/actions/runs/29925968832)
- Run id: `29925968832`
- Live bot: exit=`0`, duration=`0s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-22T09:25:44.966471-04:00","date":"2026-07-22","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.7,"phases_s":{"reconcile":1.39},"signals":0,"placed":0,"equity":130535.33,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4683","github_run_id":"29923786253","status":"ok"}
```

### Live bot full output

```text
13:54:28  INFO      Mode: morning_scan
13:54:28  INFO        [positions] 4/4 (4 valid)
13:54:28  INFO        Universe cache hit: 903 tickers (tickers_2026-07-22.json)
13:54:29  INFO        [universe] 40/899 (40 valid)
13:54:31  INFO        [universe] 80/899 (80 valid)
13:54:32  INFO        [universe] 120/899 (120 valid)
13:54:42  INFO        [universe] 160/899 (160 valid)
13:54:54  INFO        [universe] 200/899 (199 valid)
13:55:07  INFO        [universe] 240/899 (238 valid)
```

### Options bot full output

```text

## Run 20260722T135607Z

- UTC timestamp: `20260722T135607Z`
- GitHub run: [#4690](https://github.com/28twagg-ops/TradingBot/actions/runs/29926085199)
- Run id: `29926085199`
- Live bot: exit=`0`, duration=`242s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-22T09:25:44.966471-04:00","date":"2026-07-22","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.7,"phases_s":{"reconcile":1.39},"signals":0,"placed":0,"equity":130535.33,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4683","github_run_id":"29923786253","status":"ok"}
```

### Live bot full output

```text
13:56:08  INFO      Mode: morning_scan
13:56:10  INFO        [positions] 4/4 (4 valid)
13:56:10  INFO        Universe cache hit: 903 tickers (tickers_2026-07-22.json)
13:56:11  INFO        [universe] 40/899 (40 valid)
13:56:12  INFO        [universe] 80/899 (80 valid)
13:56:14  INFO        [universe] 120/899 (120 valid)
13:56:15  INFO        [universe] 160/899 (160 valid)
13:56:25  INFO        [universe] 200/899 (199 valid)
13:56:35  INFO        [universe] 240/899 (238 valid)
13:56:49  INFO        [universe] 280/899 (278 valid)
13:56:59  INFO        [universe] 320/899 (318 valid)
13:57:12  INFO        [universe] 360/899 (358 valid)
13:57:23  INFO        [universe] 400/899 (397 valid)
13:57:36  INFO        [universe] 440/899 (437 valid)
13:57:49  INFO        [universe] 480/899 (477 valid)
13:58:00  INFO        [universe] 520/899 (517 valid)
13:58:13  INFO        [universe] 560/899 (556 valid)
13:58:23  INFO        [universe] 600/899 (596 valid)
13:58:37  INFO        [universe] 640/899 (636 valid)
13:58:47  INFO        [universe] 680/899 (676 valid)
13:59:00  INFO        [universe] 720/899 (715 valid)
13:59:14  INFO        [universe] 760/899 (755 valid)
13:59:24  INFO        [universe] 800/899 (795 valid)
13:59:37  INFO        [universe] 840/899 (834 valid)
13:59:47  INFO        [universe] 880/899 (874 valid)
13:59:54  INFO        [universe] 899/899 (893 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_SCAN|
|  Time                                                         13:56 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $481.99|
+========================================================================+

+========================================================================+
|                   RUBBER BAND BOT v8  --  DAILY SCAN                   |
+========================================================================+
|  Mode                                                      *** LIVE ***|
|  Date                                                        2026-07-22|
|  Universe                                                          both|
|  Mon~  Jul: 52wkLow + Pullback50 (display only — schedule not enforced)|
|  Disabled                GapDown, VolumeSpike (see DISABLED_STRATEGIES)|
|  Regime                                                            BULL|
|  Exit                                      midline / stop-0.5% / 3d max|
+========================================================================+

+========================================================================+
|                                ACCOUNT                                 |
+========================================================================+
|  Equity                                                         $481.99|
|  Cash                                                           $121.71|
|  Reserve                                          $24.10  (always kept)|
|  Available                                     $97.61  (for new trades)|
|  Trade size             $96.40  (20% per signal — all strategies equal)|
+========================================================================+

+========================================================================+
|                           HOLDINGS  (4 open)                           |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  BIIB     Pullback50      $96.32     $201.84  $202.09  +0.1%   $+0.12  |
|  C        Pullback50      $70.00     $132.61  $132.87  +0.2%   $+0.14  |
|  CARR     Pullback50      $96.53     $67.80   $68.20   +0.6%   $+0.57  |
|  TPR      Pullback50      $97.44     $140.84  $142.42  +1.1%   $+1.09  |
|                                                                        |
|  Total invested                                                 $360.28|
|  Total open P&L                                                  $+1.91|
|  Buys today: 0  |  entry cap: 1  |  max open: 5                        |
+========================================================================+

+========================================================================+
|                               PLAN CACHE                               |
+========================================================================+
|  Mode                                                           morning|
|  File                                      logs/plans/morning_plan.json|
|  Use cached plan                                  no (stale (18730.7m))|
+========================================================================+

+========================================================================+
|          EXIT EVALUATION  (EOD -- midline + stop + max-hold)           |
+========================================================================+
|  BIIB  P&L +0.1%  $+0.12                                           HOLD|
|  C  P&L +0.2%  $+0.14                                              HOLD|
|  CARR  P&L +0.6%  $+0.57                                           HOLD|
|  TPR  P&L +1.1%  $+1.09                                            HOLD|
+========================================================================+

+========================================================================+
|                           EXIT EVAL SUMMARY                            |
+========================================================================+
|  Exit eval    attempted 0 | filled 0 | partial 0 | pending 0 | failed 0|
|  Other skips     already logged today 0  |  no price data 0  |  holds 4|
|  Stop-loss breaches                                                none|
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+

+========================================================================+
|                             DATA DOWNLOAD                              |
+========================================================================+
|  Universe: both  |  Alpaca primary / yfinance fallback                 |
+========================================================================+

+========================================================================+
|                              SIGNAL SCAN                               |
+========================================================================+
|  Month: Jul  |  Regime: BULL                                           |
|  Primary: 52wkLow  |  Secondary: Pullback50 (display only — schedule n~|
|  Source                                                       live scan|
+========================================================================+

+========================================================================+
|                         SIGNALS FOUND  --  37                          |
+========================================================================+
|  TICKER   STRATEGY        TIER   PRICE    RSI    VOL_Z   TRIGGER       |
+------------------------------------------------------------------------+
|  AEP      Pullback50      eq     $131.75  42.0   -2.26   50MA bounce (+|
|  CNP      Pullback50      eq     $43.22   46.4   -2.74   50MA bounce (+|
|  DOV      Pullback50      eq     $214.51  45.9   -2.45   50MA bounce (-|
|  DTE      Pullback50      eq     $146.65  42.4   -2.93   50MA bounce (-|
|  EMR      Pullback50      eq     $140.75  52.4   -2.14   50MA bounce (+|
|  FAST     Pullback50      eq     $45.51   38.2   -2.16   50MA bounce (-|
|  FCX      Pullback50      eq     $64.22   58.8   -2.70   50MA bounce (+|
|  FTV      Pullback50      eq     $60.69   44.9   -2.89   50MA bounce (+|
|  GRMN     Pullback50      eq     $239.04  51.5   -1.92   50MA bounce (+|
|  IFF      Pullback50      eq     $77.18   39.1   -2.56   50MA bounce (+|
|  JCI      Pullback50      eq     $143.26  46.7   -1.86   50MA bounce (+|
|  LYB      Pullback50      eq     $62.94   88.9   -2.95   50MA bounce (-|
|  NUE      Pullback50      eq     $238.35  72.1   -2.34   50MA bounce (-|
|  NVDA     Pullback50      eq     $207.97  59.8   -3.39   50MA bounce (-|
|  SRE      Pullback50      eq     $92.30   53.9   -2.17   50MA bounce (+|
|  TJX      Pullback50      eq     $156.13  61.3   -1.98   50MA bounce (-|
|  TT       Pullback50      eq     $472.69  40.5   -1.87   50MA bounce (+|
|  WEC      Pullback50      eq     $113.01  41.0   -2.85   50MA bounce (-|
|  WDC      Pullback50      eq     $557.24  45.0   -1.70   50MA bounce (-|
|  WMB      Pullback50      eq     $73.94   55.2   -2.29   50MA bounce (-|
|  XEL      Pullback50      eq     $79.53   49.3   -2.97   50MA bounce (+|
|  AAL      Pullback50      eq     $15.10   17.8   -3.01   50MA bounce (-|
|  AGCO     Pullback50      eq     $114.78  44.5   -2.96   50MA bounce (+|
|  BHF      Pullback50      eq     $63.94   50.4   -1.96   50MA bounce (+|
|  CAR      Pullback50      eq     $165.48  66.0   -1.21   50MA bounce (-|
|  EVR      Pullback50      eq     $342.54  50.7   -3.36   50MA bounce (-|13:59:55  INFO        BUY  AEP  $96.40  [Pullback50]  id=e0043dc6-d861-4cb8-a53f-bf981ecd6d15
14:00:09  INFO        place_all_stops: checking 5 positions...
14:00:09  INFO        STOP skipped AEP: fractional (0.7305 shares) — software exit will handle it
14:00:09  INFO        STOP skipped BIIB: fractional (0.4766 shares) — software exit will handle it
14:00:09  INFO        STOP skipped C: fractional (0.5268 shares) — software exit will handle it
14:00:09  INFO        STOP already live CARR @ $67.46
14:00:09  INFO        STOP skipped TPR: fractional (0.6841 shares) — software exit will handle it
14:00:09  INFO        Daily log -> logs/daily/2026-07-22.md
14:00:09  INFO        Dashboard written → logs/dashboard.md

|  GNTX     Pullback50      eq     $24.23   45.7   -2.29   50MA bounce (-|
|  HGV      Pullback50      eq     $49.97   44.9   -2.18   50MA bounce (-|
|  IRT      Pullback50      eq     $16.54   38.7   -1.56   50MA bounce (-|
|  ITT      Pullback50      eq     $194.00  58.3   -2.68   50MA bounce (+|
|  KNF      Pullback50      eq     $80.78   46.1   -1.49   50MA bounce (+|
|  MKSI     Pullback50      eq     $345.13  30.0   -2.23   50MA bounce (-|
|  PVH      Pullback50      eq     $80.65   63.3   -2.82   50MA bounce (-|
|  RS       Pullback50      eq     $386.62  63.8   -1.75   50MA bounce (+|
|  RRX      Pullback50      eq     $213.26  35.4   -1.93   50MA bounce (+|
|  TLN      Pullback50      eq     $374.99  55.7   -1.96   50MA bounce (-|
|  TREX     Pullback50      eq     $43.34   29.8   -1.94   50MA bounce (-|
|                                                                        |
+========================================================================+

+========================================================================+
|                              ENTRY ORDERS                              |
+========================================================================+
|    ENTER [eq] AEP  Pullback50                                    $96.40|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    SKIP [eq] CNP  Pullback50                                      cap 5|
|    SKIP [eq] DOV  Pullback50                                      cap 5|
|    SKIP [eq] DTE  Pullback50                                      cap 5|
|    SKIP [eq] EMR  Pullback50                                      cap 5|
|    SKIP [eq] FAST  Pullback50                                     cap 5|
|    SKIP [eq] FCX  Pullback50                                      cap 5|
|    SKIP [eq] FTV  Pullback50                                      cap 5|
|    SKIP [eq] GRMN  Pullback50                                     cap 5|
|    SKIP [eq] IFF  Pullback50                                      cap 5|
|    SKIP [eq] JCI  Pullback50                                      cap 5|
|    SKIP [eq] LYB  Pullback50                                      cap 5|
|    SKIP [eq] NUE  Pullback50                                      cap 5|
|    SKIP [eq] NVDA  Pullback50                                     cap 5|
|    SKIP [eq] SRE  Pullback50                                      cap 5|
|    SKIP [eq] TJX  Pullback50                                      cap 5|
|    SKIP [eq] TT  Pullback50                                       cap 5|
|    SKIP [eq] WEC  Pullback50                                      cap 5|
|    SKIP [eq] WDC  Pullback50                                      cap 5|
|    SKIP [eq] WMB  Pullback50                                      cap 5|
|    SKIP [eq] XEL  Pullback50                                      cap 5|
|    SKIP [eq] AAL  Pullback50                                      cap 5|
|    SKIP [eq] AGCO  Pullback50                                     cap 5|
|    SKIP [eq] BHF  Pullback50                                      cap 5|
|    SKIP [eq] CAR  Pullback50                                      cap 5|
|    SKIP [eq] EVR  Pullback50                                      cap 5|
|    SKIP [eq] GNTX  Pullback50                                     cap 5|
|    SKIP [eq] HGV  Pullback50                                      cap 5|
|    SKIP [eq] IRT  Pullback50                                      cap 5|
|    SKIP [eq] ITT  Pullback50                                      cap 5|
|    SKIP [eq] KNF  Pullback50                                      cap 5|
|    SKIP [eq] MKSI  Pullback50                                     cap 5|
|    SKIP [eq] PVH  Pullback50                                      cap 5|
|    SKIP [eq] RS  Pullback50                                       cap 5|
|    SKIP [eq] RRX  Pullback50                                      cap 5|
|    SKIP [eq] TLN  Pullback50                                      cap 5|
|    SKIP [eq] TREX  Pullback50                                     cap 5|

+========================================================================+
|                         BUY FILL CONFIRMATION                          |
+========================================================================+
|  Pending submits                                                      1|
+------------------------------------------------------------------------+
|  AEP                                                  still unconfirmed|
+========================================================================+
+========================================================================+

+========================================================================+
|                           GTC STOP PLACEMENT                           |
+========================================================================+
|  Waiting 5s for 1 buy submit(s) to settle...                           |
+========================================================================+

+========================================================================+
|                            SESSION SUMMARY                             |
+========================================================================+
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Strategy   52wkLow + Pullback50 (display only — schedule not enforced)|
|  Scanned                                                            893|
|  Signals                                                             37|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  1 unconfirmed|
|  Exits                                                                0|
|  Open pos                                                             5|
|  Equity                                                         $482.09|
|  Cash                                                            $25.32|
+========================================================================+
```

### Options bot full output

```text

## Run 20260722T140052Z

- UTC timestamp: `20260722T140052Z`
- GitHub run: [#4691](https://github.com/28twagg-ops/TradingBot/actions/runs/29926472499)
- Run id: `29926472499`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-22T09:25:44.966471-04:00","date":"2026-07-22","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.7,"phases_s":{"reconcile":1.39},"signals":0,"placed":0,"equity":130535.33,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4683","github_run_id":"29923786253","status":"ok"}
```

### Live bot full output

```text
14:00:53  INFO      Mode: exits
14:00:54  INFO        Daily log -> logs/daily/2026-07-22.md
14:00:54  INFO        Daily log reconciled -> logs/daily/2026-07-22.md (1 ledger rows)
14:00:54  INFO        place_all_stops: checking 5 positions...
14:00:54  INFO        STOP skipped AEP: fractional (0.7305 shares) — software exit will handle it
14:00:54  INFO        STOP skipped BIIB: fractional (0.4766 shares) — software exit will handle it
14:00:54  INFO        STOP skipped C: fractional (0.5268 shares) — software exit will handle it
14:00:54  INFO        STOP already live CARR @ $67.46
14:00:54  INFO        STOP skipped TPR: fractional (0.6841 shares) — software exit will handle it
14:00:54  INFO        [positions] 5/5 (5 valid)
14:00:55  INFO        Daily log -> logs/daily/2026-07-22.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:00 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.11|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AEP  P&L -0.0%  $-0.04                                            HOLD|
|  C  P&L +0.2%  $+0.14                                              HOLD|
|  BIIB  P&L +0.3%  $+0.29                                           HOLD|
|  CARR  P&L +0.3%  $+0.31                                           HOLD|
|  TPR  P&L +1.4%  $+1.32                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           5|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                5|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
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
=== options_morning_bot (PAPER) 2026-07-22T10:00:56.559306-04:00 ===

[Run context]
Paper auth OK — equity $132545.25, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 299 signal(s); top: ['S165:AMD', 'S165:APH', 'S165:AMAT', 'S165:CB', 'S165:CIEN', 'S165:COHR', 'S165:COIN', 'S165:FIX']
Paper lab: $132270 broker equity -> 140 bucket(s) ($500 virtual each, unlimited paper)
```

---

## Run 20260722T140603Z

- UTC timestamp: `20260722T140603Z`
- GitHub run: [#4692](https://github.com/28twagg-ops/TradingBot/actions/runs/29926866122)
- Run id: `29926866122`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-22T09:25:44.966471-04:00","date":"2026-07-22","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.7,"phases_s":{"reconcile":1.39},"signals":0,"placed":0,"equity":130535.33,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4683","github_run_id":"29923786253","status":"ok"}
```

### Live bot full output

```text
14:06:04  INFO      Mode: exits
14:06:05  INFO        Daily log -> logs/daily/2026-07-22.md
14:06:05  INFO        Daily log reconciled -> logs/daily/2026-07-22.md (1 ledger rows)
14:06:05  INFO        place_all_stops: checking 5 positions...
14:06:05  INFO        STOP skipped AEP: fractional (0.7305 shares) — software exit will handle it
14:06:05  INFO        STOP skipped BIIB: fractional (0.4766 shares) — software exit will handle it
14:06:05  INFO        STOP skipped C: fractional (0.5268 shares) — software exit will handle it
14:06:05  INFO        STOP already live CARR @ $67.46
14:06:05  INFO        STOP skipped TPR: fractional (0.6841 shares) — software exit will handle it
14:06:06  INFO        [positions] 5/5 (5 valid)
14:06:06  INFO        Daily log -> logs/daily/2026-07-22.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.80|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  C  P&L +0.1%  $+0.05                                              HOLD|
|  AEP  P&L +0.2%  $+0.18                                            HOLD|
|  CARR  P&L +0.4%  $+0.37                                           HOLD|
|  BIIB  P&L +0.6%  $+0.54                                           HOLD|
|  TPR  P&L +1.6%  $+1.58                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           5|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                5|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=2 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=3
  zombies_flagged=2
  FLAG b48|S164|4b941fe5 zombie age_min=846 notional=$58.00 occ=AMD260722C00575000 action=no_broker_position
  FLAG b20|S164|3fbbe0c3 zombie age_min=846 notional=$58.00 occ=AMD260722C00575000 action=no_broker_position
options_reconcile: done
Layout: controlled:140:c000_s173_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:140:c000_s173_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      140
=== options_morning_bot (PAPER) 2026-07-22T10:06:08.009966-04:00 ===

[Run context]
Paper auth OK — equity $132110.71, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-07-22 10:06:11,779 INFO   EXIT [b132|c132_s164_w1_0928_1005_r5|S164] stop_loss (-53.6%) SELL 1 AMD260722C00570000 @<= 0.23

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 299 signal(s); top: ['S165:AMD', 'S165:APH', 'S165:AMAT', 'S165:CB', 'S165:CIEN', 'S165:COHR', 'S165:COIN', 'S165:FIX']
Paper lab: $131923 broker equity -> 140 bucket(s) ($500 virtual each, unlimited paper)
```

---

## Run 20260722T141106Z

- UTC timestamp: `20260722T141106Z`
- GitHub run: [#4693](https://github.com/28twagg-ops/TradingBot/actions/runs/29927263033)
- Run id: `29927263033`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-22T09:25:44.966471-04:00","date":"2026-07-22","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.7,"phases_s":{"reconcile":1.39},"signals":0,"placed":0,"equity":130535.33,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4683","github_run_id":"29923786253","status":"ok"}
```

### Live bot full output

```text
14:11:07  INFO      Mode: exits
14:11:08  INFO        Daily log -> logs/daily/2026-07-22.md
14:11:08  INFO        Daily log reconciled -> logs/daily/2026-07-22.md (1 ledger rows)
14:11:08  INFO        place_all_stops: checking 5 positions...
14:11:08  INFO        STOP skipped AEP: fractional (0.7305 shares) — software exit will handle it
14:11:08  INFO        STOP skipped BIIB: fractional (0.4766 shares) — software exit will handle it
14:11:08  INFO        STOP skipped C: fractional (0.5268 shares) — software exit will handle it
14:11:08  INFO        STOP already live CARR @ $67.46
14:11:08  INFO        STOP skipped TPR: fractional (0.6841 shares) — software exit will handle it
14:11:09  INFO        [positions] 5/5 (5 valid)
14:11:09  INFO        Daily log -> logs/daily/2026-07-22.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.82|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  C  P&L -0.1%  $-0.10                                              HOLD|
|  AEP  P&L +0.4%  $+0.34                                            HOLD|
|  CARR  P&L +0.4%  $+0.37                                           HOLD|
|  BIIB  P&L +0.8%  $+0.79                                           HOLD|
|  TPR  P&L +1.4%  $+1.39                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           5|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                5|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=0 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=3
  zombies_flagged=0
options_reconcile: done
Layout: controlled:140:c000_s173_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:140:c000_s173_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      140
=== options_morning_bot (PAPER) 2026-07-22T10:11:11.169129-04:00 ===

[Run context]
Paper auth OK — equity $132365.13, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 299 signal(s); top: ['S165:AMD', 'S165:APH', 'S165:AMAT', 'S165:CB', 'S165:CIEN', 'S165:COHR', 'S165:COIN', 'S165:FIX']
Paper lab: $132467 broker equity -> 140 bucket(s) ($500 virtual each, unlimited paper)
```

---

## Run 20260722T141605Z

- UTC timestamp: `20260722T141605Z`
- GitHub run: [#4694](https://github.com/28twagg-ops/TradingBot/actions/runs/29927671524)
- Run id: `29927671524`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-22T09:25:44.966471-04:00","date":"2026-07-22","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.7,"phases_s":{"reconcile":1.39},"signals":0,"placed":0,"equity":130535.33,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4683","github_run_id":"29923786253","status":"ok"}
```

### Live bot full output

```text
14:16:06  INFO      Mode: exits
14:16:06  INFO        Daily log -> logs/daily/2026-07-22.md
14:16:06  INFO        Daily log reconciled -> logs/daily/2026-07-22.md (1 ledger rows)
14:16:06  INFO        place_all_stops: checking 5 positions...
14:16:06  INFO        STOP skipped AEP: fractional (0.7305 shares) — software exit will handle it
14:16:06  INFO        STOP skipped BIIB: fractional (0.4766 shares) — software exit will handle it
14:16:06  INFO        STOP skipped C: fractional (0.5268 shares) — software exit will handle it
14:16:06  INFO        STOP already live CARR @ $67.46
14:16:06  INFO        STOP skipped TPR: fractional (0.6841 shares) — software exit will handle it
14:16:07  INFO        [positions] 5/5 (5 valid)
14:16:07  INFO        Daily log -> logs/daily/2026-07-22.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.66|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  C  P&L -0.3%  $-0.24                                              HOLD|
|  CARR  P&L +0.1%  $+0.07                                           HOLD|
|  BIIB  P&L +0.6%  $+0.57                                           HOLD|
|  AEP  P&L +0.7%  $+0.63                                            HOLD|
|  TPR  P&L +1.6%  $+1.54                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           5|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                5|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=5 pending_exits=1 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=3
  zombies_flagged=0
options_reconcile: done
Layout: controlled:140:c000_s173_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:140:c000_s173_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      140
=== options_morning_bot (PAPER) 2026-07-22T10:16:09.315436-04:00 ===

[Run context]
Paper auth OK — equity $132075.13, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 299 signal(s); top: ['S165:AMD', 'S165:APH', 'S165:AMAT', 'S165:CB', 'S165:CIEN', 'S165:COHR', 'S165:COIN', 'S165:FIX']
Paper lab: $132171 broker equity -> 140 bucket(s) ($500 virtual each, unlimited paper)
```

---

## Run 20260722T142059Z

- UTC timestamp: `20260722T142059Z`
- GitHub run: [#4695](https://github.com/28twagg-ops/TradingBot/actions/runs/29928077910)
- Run id: `29928077910`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-22T09:25:44.966471-04:00","date":"2026-07-22","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.7,"phases_s":{"reconcile":1.39},"signals":0,"placed":0,"equity":130535.33,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4683","github_run_id":"29923786253","status":"ok"}
```

### Live bot full output

```text
14:21:00  INFO      Mode: exits
14:21:01  INFO        Daily log -> logs/daily/2026-07-22.md
14:21:01  INFO        Daily log reconciled -> logs/daily/2026-07-22.md (1 ledger rows)
14:21:01  INFO        place_all_stops: checking 5 positions...
14:21:01  INFO        STOP skipped AEP: fractional (0.7305 shares) — software exit will handle it
14:21:01  INFO        STOP skipped BIIB: fractional (0.4766 shares) — software exit will handle it
14:21:01  INFO        STOP skipped C: fractional (0.5268 shares) — software exit will handle it
14:21:01  INFO        STOP already live CARR @ $67.46
14:21:01  INFO        STOP skipped TPR: fractional (0.6841 shares) — software exit will handle it
14:21:02  INFO        [positions] 5/5 (5 valid)
14:21:02  INFO        Daily log -> logs/daily/2026-07-22.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.93|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  C  P&L -0.2%  $-0.15                                              HOLD|
|  BIIB  P&L +0.3%  $+0.27                                           HOLD|
|  CARR  P&L +0.4%  $+0.36                                           HOLD|
|  AEP  P&L +0.6%  $+0.61                                            HOLD|
|  TPR  P&L +1.7%  $+1.63                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           5|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                5|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=4 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=3
  zombies_flagged=4
  FLAG b104|S164|c6095e4d zombie age_min=861 notional=$56.00 occ=AMD260722C00570000 action=submitted:c340336b-0f14-42fc-baef-ec48b136fd17
  FLAG b76|S164|4cedf2ab zombie age_min=861 notional=$56.00 occ=AMD260722C00570000 action=submitted:abb19633-abd3-4b70-950d-2f7e32cd2ac7
  FLAG b48|S164|3e37f4df zombie age_min=861 notional=$56.00 occ=AMD260722C00570000 action=submitted:8235a47c-0d0b-4661-8bd1-a7e90af5f71f
  FLAG b20|S164|3738ecb7 zombie age_min=861 notional=$56.00 occ=AMD260722C00570000 action=submitted:3e2f51d5-4a54-46de-a822-ae20fc6d57d3
options_reconcile: done
Layout: controlled:140:c000_s173_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:140:c000_s173_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      140
=== options_morning_bot (PAPER) 2026-07-22T10:21:04.750937-04:00 ===

[Run context]
Paper auth OK — equity $132597.05, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 299 signal(s); top: ['S165:AMD', 'S165:APH', 'S165:AMAT', 'S165:CB', 'S165:CIEN', 'S165:COHR', 'S165:COIN', 'S165:FIX']
Paper lab: $132608 broker equity -> 140 bucket(s) ($500 virtual each, unlimited paper)
```

---

## Run 20260722T142603Z

- UTC timestamp: `20260722T142603Z`
- GitHub run: [#4696](https://github.com/28twagg-ops/TradingBot/actions/runs/29928481864)
- Run id: `29928481864`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-22T09:25:44.966471-04:00","date":"2026-07-22","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.7,"phases_s":{"reconcile":1.39},"signals":0,"placed":0,"equity":130535.33,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4683","github_run_id":"29923786253","status":"ok"}
```

### Live bot full output

```text
14:26:04  INFO      Mode: exits
14:26:04  INFO        Daily log -> logs/daily/2026-07-22.md
14:26:04  INFO        Daily log reconciled -> logs/daily/2026-07-22.md (1 ledger rows)
14:26:04  INFO        place_all_stops: checking 5 positions...
14:26:04  INFO        STOP skipped AEP: fractional (0.7305 shares) — software exit will handle it
14:26:04  INFO        STOP skipped BIIB: fractional (0.4766 shares) — software exit will handle it
14:26:04  INFO        STOP skipped C: fractional (0.5268 shares) — software exit will handle it
14:26:04  INFO        STOP already live CARR @ $67.46
14:26:04  INFO        STOP skipped TPR: fractional (0.6841 shares) — software exit will handle it
14:26:05  INFO        [positions] 5/5 (5 valid)
14:26:05  INFO        Daily log -> logs/daily/2026-07-22.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.11|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  C  P&L -0.0%  $-0.01                                              HOLD|
|  BIIB  P&L +0.1%  $+0.06                                           HOLD|
|  CARR  P&L +0.1%  $+0.07                                           HOLD|
|  AEP  P&L +0.6%  $+0.56                                            HOLD|
|  TPR  P&L +1.4%  $+1.34                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           5|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                5|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=4 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=2
  zombies_flagged=4
  FLAG b76|S164|b1836055 zombie age_min=866 notional=$56.00 occ=AMD260722C00570000 action=no_broker_position
  FLAG b48|S164|91d9aa59 zombie age_min=866 notional=$56.00 occ=AMD260722C00570000 action=no_broker_position
  FLAG b20|S164|de3c09ec zombie age_min=866 notional=$56.00 occ=AMD260722C00570000 action=no_broker_position
  FLAG b132|S164|2686c253 zombie age_min=866 notional=$56.00 occ=AMD260722C00570000 action=no_broker_position
options_reconcile: done
Layout: controlled:140:c000_s173_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:140:c000_s173_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      140
=== options_morning_bot (PAPER) 2026-07-22T10:26:06.849603-04:00 ===

[Run context]
Paper auth OK — equity $132574.13, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 299 signal(s); top: ['S165:AMD', 'S165:APH', 'S165:AMAT', 'S165:CB', 'S165:CIEN', 'S165:COHR', 'S165:COIN', 'S165:FIX']
Paper lab: $132491 broker equity -> 140 bucket(s) ($500 virtual each, unlimited paper)
```

---

## Run 20260722T143116Z

- UTC timestamp: `20260722T143116Z`
- GitHub run: [#4697](https://github.com/28twagg-ops/TradingBot/actions/runs/29928879510)
- Run id: `29928879510`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-22T09:25:44.966471-04:00","date":"2026-07-22","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.7,"phases_s":{"reconcile":1.39},"signals":0,"placed":0,"equity":130535.33,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4683","github_run_id":"29923786253","status":"ok"}
```

### Live bot full output

```text
14:31:18  INFO      Mode: exits
14:31:18  INFO        Daily log -> logs/daily/2026-07-22.md
14:31:18  INFO        Daily log reconciled -> logs/daily/2026-07-22.md (1 ledger rows)
14:31:18  INFO        place_all_stops: checking 5 positions...
14:31:18  INFO        STOP skipped AEP: fractional (0.7305 shares) — software exit will handle it
14:31:18  INFO        STOP skipped BIIB: fractional (0.4766 shares) — software exit will handle it
14:31:18  INFO        STOP skipped C: fractional (0.5268 shares) — software exit will handle it
14:31:18  INFO        STOP already live CARR @ $67.46
14:31:18  INFO        STOP skipped TPR: fractional (0.6841 shares) — software exit will handle it
14:31:19  INFO        [positions] 5/5 (5 valid)
14:31:19  INFO        Daily log -> logs/daily/2026-07-22.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $481.47|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CARR  P&L -0.2%  $-0.16                                           HOLD|
|  BIIB  P&L +0.0%  $+0.04                                           HOLD|
|  C  P&L +0.1%  $+0.05                                              HOLD|
|  AEP  P&L +0.5%  $+0.44                                            HOLD|
|  TPR  P&L +1.1%  $+1.05                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           5|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                5|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
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
=== options_morning_bot (PAPER) 2026-07-22T10:31:21.822369-04:00 ===

[Run context]
Paper auth OK — equity $132401.05, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 299 signal(s); top: ['S165:AMD', 'S165:APH', 'S165:AMAT', 'S165:CB', 'S165:CIEN', 'S165:COHR', 'S165:COIN', 'S165:FIX']
Paper lab: $132491 broker equity -> 140 bucket(s) ($500 virtual each, unlimited paper)
```

---

## Run 20260722T143611Z

- UTC timestamp: `20260722T143611Z`
- GitHub run: [#4698](https://github.com/28twagg-ops/TradingBot/actions/runs/29929289019)
- Run id: `29929289019`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-22T09:25:44.966471-04:00","date":"2026-07-22","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.7,"phases_s":{"reconcile":1.39},"signals":0,"placed":0,"equity":130535.33,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4683","github_run_id":"29923786253","status":"ok"}
```

### Live bot full output

```text
14:36:13  INFO      Mode: exits
14:36:13  INFO        Daily log -> logs/daily/2026-07-22.md
14:36:13  INFO        Daily log reconciled -> logs/daily/2026-07-22.md (1 ledger rows)
14:36:13  INFO        place_all_stops: checking 5 positions...
14:36:13  INFO        STOP skipped AEP: fractional (0.7305 shares) — software exit will handle it
14:36:13  INFO        STOP skipped BIIB: fractional (0.4766 shares) — software exit will handle it
14:36:13  INFO        STOP skipped C: fractional (0.5268 shares) — software exit will handle it
14:36:13  INFO        STOP already live CARR @ $67.46
14:36:13  INFO        STOP skipped TPR: fractional (0.6841 shares) — software exit will handle it
14:36:14  INFO        [positions] 5/5 (5 valid)
14:36:14  INFO        Daily log -> logs/daily/2026-07-22.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $481.76|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CARR  P&L -0.1%  $-0.07                                           HOLD|
|  C  P&L +0.0%  $+0.02                                              HOLD|
|  BIIB  P&L +0.2%  $+0.18                                           HOLD|
|  AEP  P&L +0.5%  $+0.49                                            HOLD|
|  TPR  P&L +1.1%  $+1.06                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           5|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                5|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
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
=== options_morning_bot (PAPER) 2026-07-22T10:36:15.510534-04:00 ===

[Run context]
Paper auth OK — equity $132607.05, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 299 signal(s); top: ['S165:AMD', 'S165:APH', 'S165:AMAT', 'S165:CB', 'S165:CIEN', 'S165:COHR', 'S165:COIN', 'S165:FIX']
Paper lab: $132745 broker equity -> 140 bucket(s) ($500 virtual each, unlimited paper)
```

---

## Run 20260722T144108Z

- UTC timestamp: `20260722T144108Z`
- GitHub run: [#4699](https://github.com/28twagg-ops/TradingBot/actions/runs/29929682991)
- Run id: `29929682991`
- Live bot: exit=`0`, duration=`5s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-22T10:41:14.708714-04:00","date":"2026-07-22","mode":"entry+manage","header":"entry+manage (15 new)","elapsed_s":237.3,"phases_s":{"reconcile":2.3,"cancel":0.12,"manage":0.12,"scan":36.17,"entries":196.43,"reconcile2":1.53},"signals":299,"placed":15,"equity":133001.73,"open_positions":1,"pending_orders":0,"open_lots":15,"submitted_today":20,"filled_today":22,"unattributed_contracts":0,"top_signals":["S165:AMD","S165:APH","S165:AMAT","S165:CB","S165:CIEN","S165:COHR","S165:COIN","S165:FIX"],"github_run":"4699","github_run_id":"29929682991","status":"ok"}
```

### Live bot full output

```text
14:41:11  INFO      Mode: exits
14:41:12  INFO        Daily log -> logs/daily/2026-07-22.md
14:41:12  INFO        Daily log reconciled -> logs/daily/2026-07-22.md (1 ledger rows)
14:41:12  INFO        place_all_stops: checking 5 positions...
14:41:12  INFO        STOP skipped AEP: fractional (0.7305 shares) — software exit will handle it
14:41:12  INFO        STOP skipped BIIB: fractional (0.4766 shares) — software exit will handle it
14:41:12  INFO        STOP skipped C: fractional (0.5268 shares) — software exit will handle it
14:41:12  INFO        STOP already live CARR @ $67.46
14:41:12  INFO        STOP skipped TPR: fractional (0.6841 shares) — software exit will handle it
14:41:12  INFO        [positions] 5/5 (5 valid)
14:41:12  INFO        Daily log -> logs/daily/2026-07-22.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.26|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CARR  P&L -0.0%  $-0.02                                           HOLD|
|  BIIB  P&L +0.1%  $+0.06                                           HOLD|
|  C  P&L +0.1%  $+0.08                                              HOLD|
|  AEP  P&L +0.6%  $+0.57                                            HOLD|
|  TPR  P&L +1.6%  $+1.50                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           5|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                5|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
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
=== options_morning_bot (PAPER) 2026-07-22T10:41:14.708714-04:00 ===

[Run context]
Paper auth OK — equity $133001.73, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 299 signal(s); top: ['S165:AMD', 'S165:APH', 'S165:AMAT', 'S165:CB', 'S165:CIEN', 'S165:COHR', 'S165:COIN', 'S165:FIX']
Paper lab: $132863 broker equity -> 140 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 525 no tradeable call, 265 open order exists, 690 pending order
Placed 15 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $133,001.73                             |
|  Signals this run              299                                     |
|  Orders submitted (session)    20                                      |
|  Orders filled today (ledger)  22                                      |
|  Entries placed this run       15                                      |
|  Open virtual lots             15                                      |
|  Broker option positions       1                                       |
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
|  OPEN OPTIONS (1)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  COIN260724C00187500          15    -19.5%   $   -185.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-22.log
elapsed=237.3s reconcile=2.3s cancel=0.12s manage=0.12s scan=36.17s entries=196.43s
STATUS: options_morning_bot run complete (PAPER) elapsed=237.3s. run=#4699 https://github.com/28twagg-ops/TradingBot/actions/runs/29929682991
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 2.9% (22/762)
# Options signal frequency

_Generated 2026-07-22T10:45:14.656256_

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
| 2026-07-22 |    1 |    0 |    1 |    0 |    1 |    0 |    0 |    0 |     3 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 2 | 2 | 1.0 | ~38 active signal-days |
| S164 | 2 | 1 | 2.0 | ~19 active signal-days |
| S165 | 16 | 9 | 1.8 | ~22 active signal-days |
| S166 | 1 | 1 | 1.0 | ~38 active signal-days |
| S167 | 3 | 2 | 1.5 | ~25 active signal-days |
| S168 | 2 | 1 | 2.0 | ~19 active signal-days |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 55 | 2 |
| S164 | 62 | 2 |
| S165 | 1498 | 16 |
| S166 | 45 | 1 |
| S167 | 65 | 3 |
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
| 2026-07-22 |   25 |   27 |   76 |   15 |   30 |   20 |   77 |    0 |   270 |

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
| Total open lots             |    15 | INFO |
| Total closed lots           |   297 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   616 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=482.27 router=CONFIRMED leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---

## Run 20260722T144556Z

- UTC timestamp: `20260722T144556Z`
- GitHub run: [#4700](https://github.com/28twagg-ops/TradingBot/actions/runs/29930083332)
- Run id: `29930083332`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`185s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-22T10:46:01.007982-04:00","date":"2026-07-22","mode":"entry+manage","header":"entry+manage (20 new)","elapsed_s":180.3,"phases_s":{"reconcile":1.52,"cancel":0.09,"manage":0.81,"scan":55.42,"entries":120.45,"reconcile2":1.52},"signals":299,"placed":20,"equity":133449.75,"open_positions":2,"pending_orders":10,"open_lots":30,"submitted_today":25,"filled_today":37,"unattributed_contracts":0,"top_signals":["S165:AMD","S165:APH","S165:AMAT","S165:CB","S165:CIEN","S165:COHR","S165:COIN","S165:FIX"],"github_run":"4700","github_run_id":"29930083332","status":"ok"}
```

### Live bot full output

```text
14:45:58  INFO      Mode: exits
14:45:58  INFO        Daily log -> logs/daily/2026-07-22.md
14:45:58  INFO        Daily log reconciled -> logs/daily/2026-07-22.md (1 ledger rows)
14:45:58  INFO        place_all_stops: checking 5 positions...
14:45:58  INFO        STOP skipped AEP: fractional (0.7305 shares) — software exit will handle it
14:45:58  INFO        STOP skipped BIIB: fractional (0.4766 shares) — software exit will handle it
14:45:58  INFO        STOP skipped C: fractional (0.5268 shares) — software exit will handle it
14:45:58  INFO        STOP already live CARR @ $67.46
14:45:58  INFO        STOP skipped TPR: fractional (0.6841 shares) — software exit will handle it
14:45:59  INFO        [positions] 5/5 (5 valid)
14:45:59  INFO        Daily log -> logs/daily/2026-07-22.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:45 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.51|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CARR  P&L +0.1%  $+0.07                                           HOLD|
|  BIIB  P&L +0.1%  $+0.09                                           HOLD|
|  C  P&L +0.5%  $+0.32                                              HOLD|
|  AEP  P&L +0.6%  $+0.54                                            HOLD|
|  TPR  P&L +1.5%  $+1.41                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           5|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                5|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=0 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=3
  zombies_flagged=0
options_reconcile: done
Layout: controlled:140:c000_s173_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:140:c000_s173_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      140
=== options_morning_bot (PAPER) 2026-07-22T10:46:01.007982-04:00 ===

[Run context]
Paper auth OK — equity $133449.75, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 299 signal(s); top: ['S165:AMD', 'S165:APH', 'S165:AMAT', 'S165:CB', 'S165:CIEN', 'S165:COHR', 'S165:COIN', 'S165:FIX']
Paper lab: $133610 broker equity -> 140 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 525 no tradeable call, 950 pending order
Placed 20 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $133,449.75                             |
|  Signals this run              299                                     |
|  Orders submitted (session)    25                                      |
|  Orders filled today (ledger)  37                                      |
|  Entries placed this run       20                                      |
|  Open virtual lots             30                                      |
|  Broker option positions       2                                       |
|  Pending orders                10                                      |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=259  buckets=23  win=32%                             |
|  Returns   avg=-1.9%  med=-35.3%  p10=-65.1%  p90=+83.9%               |
|  Realized  $+4,787.13                                                  |
|  Raw incl dropped  trades=763  real=$+1,942.58                         |
|  Today     trades=1  avg=-53.6%  med=-53.6%  real=$-30.00              |
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
|  ... 15 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b9   c009_s165_w2_1005_  6   0% -76.2 -78.1 -92.7 $   -261       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (10)                                                   |
+------------------------------------------------------------------------+
|  Top groups                    S164:AMD(5), S163:COIN(5)               |
+------------------------------------------------------------------------+
|  b21  S164 AMD      limit=0.60                                         |
|  b49  S164 AMD      limit=0.60                                         |
|  b77  S164 AMD      limit=0.60                                         |
|  b105 S164 AMD      limit=0.60                                         |
|  b133 S164 AMD      limit=0.60                                         |
|  ... 5 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (2)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  COIN260724C00187500          25    -18.8%   $   -295.00               |
|  AMD260722C00570000            5     -2.2%   $     -5.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-22.log
elapsed=180.3s reconcile=1.52s cancel=0.09s manage=0.81s scan=55.42s entries=120.45s
STATUS: options_morning_bot run complete (PAPER) elapsed=180.3s. run=#4700 https://github.com/28twagg-ops/TradingBot/actions/runs/29930083332
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_buckets.csv
Summary: 1 buckets closed trades, $-30.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 2.9% (22/763)
# Options signal frequency

_Generated 2026-07-22T10:49:04.291040_

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
| 2026-07-22 |    1 |    1 |    1 |    0 |    1 |    0 |    0 |    0 |     4 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 2 | 2 | 1.0 | ~38 active signal-days |
| S164 | 3 | 2 | 1.5 | ~25 active signal-days |
| S165 | 16 | 9 | 1.8 | ~22 active signal-days |
| S166 | 1 | 1 | 1.0 | ~38 active signal-days |
| S167 | 3 | 2 | 1.5 | ~25 active signal-days |
| S168 | 2 | 1 | 2.0 | ~19 active signal-days |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 55 | 2 |
| S164 | 72 | 3 |
| S165 | 1503 | 16 |
| S166 | 45 | 1 |
| S167 | 70 | 3 |
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
| 2026-07-22 |   25 |   37 |   81 |   15 |   35 |   20 |   77 |    0 |   290 |

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
| State/ledger mismatches     |     5 | WARN | <<<
| Total open lots             |    30 | INFO |
| Total closed lots           |   298 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   616 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=482.51 router=CONFIRMED leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---

## Run 20260722T145040Z

- UTC timestamp: `20260722T145040Z`
- GitHub run: [#4701](https://github.com/28twagg-ops/TradingBot/actions/runs/29930484421)
- Run id: `29930484421`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`146s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-22T10:50:48.292974-04:00","date":"2026-07-22","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":136.8,"phases_s":{"reconcile":2.16,"cancel":0.15,"manage":1.09,"scan":45.04,"entries":85.88,"reconcile2":1.81},"signals":299,"placed":0,"equity":133080.75,"open_positions":1,"pending_orders":5,"open_lots":5,"submitted_today":25,"filled_today":42,"unattributed_contracts":0,"top_signals":["S165:AMD","S165:APH","S165:AMAT","S165:CB","S165:CIEN","S165:COHR","S165:COIN","S165:FIX"],"github_run":"4701","github_run_id":"29930484421","status":"ok"}
```

### Live bot full output

```text
14:50:42  INFO      Mode: exits
14:50:42  INFO        Daily log -> logs/daily/2026-07-22.md
14:50:42  INFO        Daily log reconciled -> logs/daily/2026-07-22.md (1 ledger rows)
14:50:42  INFO        place_all_stops: checking 5 positions...
14:50:42  INFO        STOP skipped AEP: fractional (0.7305 shares) — software exit will handle it
14:50:42  INFO        STOP skipped BIIB: fractional (0.4766 shares) — software exit will handle it
14:50:42  INFO        STOP skipped C: fractional (0.5268 shares) — software exit will handle it
14:50:43  INFO        STOP already live CARR @ $67.46
14:50:43  INFO        STOP skipped TPR: fractional (0.6841 shares) — software exit will handle it
14:50:43  INFO        [positions] 5/5 (5 valid)
14:50:43  INFO        Daily log -> logs/daily/2026-07-22.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:50 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.34|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CARR  P&L -0.1%  $-0.07                                           HOLD|
|  BIIB  P&L -0.0%  $-0.02                                           HOLD|
|  C  P&L +0.4%  $+0.30                                              HOLD|
|  AEP  P&L +0.5%  $+0.51                                            HOLD|
|  TPR  P&L +1.6%  $+1.54                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           5|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                5|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=30 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=4
  zombies_flagged=30
  FLAG b129|S163|a871e928 zombie age_min=891 notional=$64.00 occ=COIN260724C00187500 action=submitted:4c1020c7-9798-497f-a2d9-02ade1ce0668
  FLAG b101|S163|f67c8c4c zombie age_min=891 notional=$64.00 occ=COIN260724C00187500 action=submitted:d45b8322-a98f-4fbe-be0f-10025aa54c28
  FLAG b73|S163|80be3ac0 zombie age_min=891 notional=$64.00 occ=COIN260724C00187500 action=submitted:d848432b-67fa-4240-afe1-7bd1c4ea8f64
  FLAG b45|S163|9fdb7901 zombie age_min=891 notional=$64.00 occ=COIN260724C00187500 action=submitted:4c2a7d05-98f3-48b0-82fb-09f6763c4d4e
  FLAG b17|S163|d790ac76 zombie age_min=891 notional=$64.00 occ=COIN260724C00187500 action=submitted:47d4ad7b-e0f3-4c7a-80de-1283ecba7994
  FLAG b117|S167|2fd729a4 zombie age_min=891 notional=$63.00 occ=COIN260724C00187500 action=submitted:a569d347-bd08-46bb-ac18-dcd93d003e68
  FLAG b89|S167|6663aecd zombie age_min=891 notional=$63.00 occ=COIN260724C00187500 action=submitted:3939c53a-ab07-4a43-af20-6a1ff7a08c08
  FLAG b61|S167|a6493b0d zombie age_min=891 notional=$63.00 occ=COIN260724C00187500 action=submitted:30bdfcb3-f564-4dba-9c6f-bbc8d4ac68af
  FLAG b33|S167|3ef2e261 zombie age_min=891 notional=$63.00 occ=COIN260724C00187500 action=submitted:f4511869-de8c-4e3a-8304-6aec5d2a370f
  FLAG b5|S167|68f94c22 zombie age_min=891 notional=$63.00 occ=COIN260724C00187500 action=submitted:731453dd-f3ea-413e-9baf-da1f097c078c
  FLAG b121|S165|2b6785e3 zombie age_min=891 notional=$63.00 occ=COIN260724C00187500 action=submitted:6cf2a5c8-e430-488b-8fbb-f5e69a0d2adb
  FLAG b93|S165|20e3f58a zombie age_min=891 notional=$63.00 occ=COIN260724C00187500 action=submitted:4e7a0f4a-0a5a-4c65-b5fe-2638f551ec86
  FLAG b65|S165|9da2c3b1 zombie age_min=891 notional=$63.00 occ=COIN260724C00187500 action=submitted:317d573c-8749-4897-984f-553ddeefdce6
  FLAG b37|S165|dcb1d0b2 zombie age_min=891 notional=$63.00 occ=COIN260724C00187500 action=submitted:88a1076c-39e2-408a-ae1b-edde3c38bb13
  FLAG b9|S165|9cd1ea35 zombie age_min=891 notional=$63.00 occ=COIN260724C00187500 action=submitted:dfb5c51a-d9d7-427d-abdd-13f9ea10d573
  FLAG b118|S167|b2256497 zombie age_min=891 notional=$60.00 occ=COIN260724C00187500 action=submitted:ccee8f97-c2a7-4d05-acde-39d620ab1c9e
  FLAG b90|S167|383a0b7d zombie age_min=891 notional=$60.00 occ=COIN260724C00187500 action=submitted:d786a3cf-499a-49af-ae16-e8f671eb70c5
  FLAG b62|S167|d4e6be56 zombie age_min=891 notional=$60.00 occ=COIN260724C00187500 action=submitted:7fc67b05-f3d7-41a8-a30e-883ed9f587e7
  FLAG b34|S167|30844db4 zombie age_min=891 notional=$60.00 occ=COIN260724C00187500 action=submitted:5b65e9f2-773d-4b3c-aa42-341a3d85c9d3
  FLAG b6|S167|ac46e445 zombie age_min=891 notional=$60.00 occ=COIN260724C00187500 action=submitted:57c9e68a-34c0-4182-b6e9-e2239bc96334
  FLAG b122|S165|55d4d7c2 zombie age_min=891 notional=$64.00 occ=COIN260724C00187500 action=submitted:fe121d20-378b-453b-8f0d-369c9f6959ee
  FLAG b94|S165|7c5f28ad zombie age_min=891 notional=$64.00 occ=COIN260724C00187500 action=submitted:588a09f9-98b7-4a0f-8134-fed4f3c7fbd3
  FLAG b66|S165|3affabc6 zombie age_min=891 notional=$64.00 occ=COIN260724C00187500 action=submitted:25adf8bc-5de8-4301-9cab-c72bb3ee0643
  FLAG b38|S165|b4db1400 zombie age_min=891 notional=$64.00 occ=COIN260724C00187500 action=submitted:2bdaea19-d2db-400d-b7df-dd7edb8d544c
  FLAG b10|S165|5299e16d zombie age_min=891 notional=$64.00 occ=COIN260724C00187500 action=submitted:daaf3a1a-da7a-4e63-8edc-ac46cb58c251
  FLAG b132|S164|3cd585c6 zombie age_min=891 notional=$56.00 occ=AMD260722C00570000 action=submitted:a162b6dc-c1e9-4cd5-9056-e0a6cf431ddb
  FLAG b104|S164|f1a9abda zombie age_min=891 notional=$56.00 occ=AMD260722C00570000 action=submitted:bfad8fbc-7669-491f-be6d-0d8f80fecbb5
  FLAG b76|S164|63ea6570 zombie age_min=891 notional=$56.00 occ=AMD260722C00570000 action=submitted:13189681-441b-465a-8f7a-bd4d88a7f18a
  FLAG b48|S164|28146b6a zombie age_min=891 notional=$56.00 occ=AMD260722C00570000 action=submitted:62a9c43b-2512-4388-a72c-caf794eae26c
  FLAG b20|S164|298f4d11 zombie age_min=891 notional=$56.00 occ=AMD260722C00570000 action=submitted:2587909e-79fc-4a80-9bc8-74e13995e668
options_reconcile: done
Layout: controlled:140:c000_s173_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:140:c000_s173_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      140
=== options_morning_bot (PAPER) 2026-07-22T10:50:48.292974-04:00 ===

[Run context]
Paper auth OK — equity $133080.75, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 299 signal(s); top: ['S165:AMD', 'S165:APH', 'S165:AMAT', 'S165:CB', 'S165:CIEN', 'S165:COHR', 'S165:COIN', 'S165:FIX']
Paper lab: $132911 broker equity -> 140 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 435 no tradeable call, 795 already attempted today
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $133,080.75                             |
|  Signals this run              299                                     |
|  Orders submitted (session)    25                                      |
|  Orders filled today (ledger)  42                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             5                                       |
|  Broker option positions       1                                       |
|  Pending orders                5                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=263  buckets=23  win=32%                             |
|  Returns   avg=-2.8%  med=-38.2%  p10=-64.9%  p90=+83.4%               |
|  Realized  $+4,654.13                                                  |
|  Raw incl dropped  trades=773  real=$+1,841.58                         |
|  Today     trades=1  avg=-53.6%  med=-53.6%  real=$-30.00              |
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
|  ... 15 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b9   c009_s165_w2_1005_  7   0% -74.4 -66.2 -92.7 $   -301       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (5)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S164:AMD(5)                             |
+------------------------------------------------------------------------+
|  b21  S164 AMD      limit=0.60                                         |
|  b49  S164 AMD      limit=0.60                                         |
|  b77  S164 AMD      limit=0.60                                         |
|  b105 S164 AMD      limit=0.60                                         |
|  b133 S164 AMD      limit=0.60                                         |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (1)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  COIN260724C00187500           5    -25.4%   $    -78.33               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-22.log
elapsed=136.8s reconcile=2.16s cancel=0.15s manage=1.09s scan=45.04s entries=85.88s
STATUS: options_morning_bot run complete (PAPER) elapsed=136.8s. run=#4701 https://github.com/28twagg-ops/TradingBot/actions/runs/29930484421
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_buckets.csv
Summary: 1 buckets closed trades, $-30.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 2.9% (22/773)
# Options signal frequency

_Generated 2026-07-22T10:53:08.552691_

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
| 2026-07-22 |    1 |    1 |    1 |    0 |    1 |    0 |    0 |    0 |     4 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 2 | 2 | 1.0 | ~38 active signal-days |
| S164 | 3 | 2 | 1.5 | ~25 active signal-days |
| S165 | 16 | 9 | 1.8 | ~22 active signal-days |
| S166 | 1 | 1 | 1.0 | ~38 active signal-days |
| S167 | 3 | 2 | 1.5 | ~25 active signal-days |
| S168 | 2 | 1 | 2.0 | ~19 active signal-days |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 60 | 2 |
| S164 | 72 | 3 |
| S165 | 1503 | 16 |
| S166 | 45 | 1 |
| S167 | 70 | 3 |
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
| 2026-07-22 |   30 |   37 |   81 |   15 |   35 |   20 |   77 |    0 |   295 |

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
| State/ledger mismatches     |     5 | WARN | <<<
| Total open lots             |     5 | INFO |
| Total closed lots           |   304 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   616 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=482.34 router=CONFIRMED leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---

## Run 20260722T145536Z

- UTC timestamp: `20260722T145536Z`
- GitHub run: [#4702](https://github.com/28twagg-ops/TradingBot/actions/runs/29930886501)
- Run id: `29930886501`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`132s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-22T10:55:39.207580-04:00","date":"2026-07-22","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":126.5,"phases_s":{"reconcile":1.61,"cancel":0.02,"manage":0.03,"scan":42.81,"entries":77.14,"reconcile2":4.61},"signals":299,"placed":0,"equity":133324.65,"open_positions":0,"pending_orders":5,"open_lots":0,"submitted_today":25,"filled_today":42,"unattributed_contracts":0,"top_signals":["S165:AMD","S165:APH","S165:AMAT","S165:CB","S165:CIEN","S165:COHR","S165:COIN","S165:FIX"],"github_run":"4702","github_run_id":"29930886501","status":"ok"}
```

### Live bot full output

```text
14:55:37  INFO      Mode: exits
14:55:37  INFO        Daily log -> logs/daily/2026-07-22.md
14:55:37  INFO        Daily log reconciled -> logs/daily/2026-07-22.md (1 ledger rows)
14:55:37  INFO        place_all_stops: checking 5 positions...
14:55:37  INFO        STOP skipped AEP: fractional (0.7305 shares) — software exit will handle it
14:55:37  INFO        STOP skipped BIIB: fractional (0.4766 shares) — software exit will handle it
14:55:37  INFO        STOP skipped C: fractional (0.5268 shares) — software exit will handle it
14:55:37  INFO        STOP already live CARR @ $67.46
14:55:37  INFO        STOP skipped TPR: fractional (0.6841 shares) — software exit will handle it
14:55:37  INFO        [positions] 5/5 (5 valid)
14:55:37  INFO        Daily log -> logs/daily/2026-07-22.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:55 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.12|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CARR  P&L -0.2%  $-0.15                                           HOLD|
|  BIIB  P&L +0.0%  $+0.01                                           HOLD|
|  C  P&L +0.3%  $+0.19                                              HOLD|
|  AEP  P&L +0.6%  $+0.55                                            HOLD|
|  TPR  P&L +1.5%  $+1.43                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           5|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                5|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=5 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=3
  zombies_flagged=5
  FLAG b121|S165|93809c4d zombie age_min=896 notional=$63.00 occ=COIN260724C00187500 action=submitted:801e1b54-f271-4229-86a2-dd57da61ab83
  FLAG b93|S165|e1da6de9 zombie age_min=896 notional=$63.00 occ=COIN260724C00187500 action=submitted:a36c90bf-4b02-4413-ab58-17e49fd8f8c7
  FLAG b65|S165|bd6d8dc5 zombie age_min=896 notional=$63.00 occ=COIN260724C00187500 action=submitted:da4f54b4-897b-4b1c-8821-a51d6a534d40
  FLAG b37|S165|cac17e59 zombie age_min=896 notional=$63.00 occ=COIN260724C00187500 action=submitted:3c960380-2a3a-465d-9d49-3df00610dbfa
  FLAG b9|S165|54f829e7 zombie age_min=896 notional=$63.00 occ=COIN260724C00187500 action=submitted:c3b36bb0-a060-4c3d-87f3-f78df6603eee
options_reconcile: done
Layout: controlled:140:c000_s173_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:140:c000_s173_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      140
=== options_morning_bot (PAPER) 2026-07-22T10:55:39.207580-04:00 ===

[Run context]
Paper auth OK — equity $133324.65, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 299 signal(s); top: ['S165:AMD', 'S165:APH', 'S165:AMAT', 'S165:CB', 'S165:CIEN', 'S165:COHR', 'S165:COIN', 'S165:FIX']
Paper lab: $133234 broker equity -> 140 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 435 no tradeable call, 1060 already attempted today
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $133,324.65                             |
|  Signals this run              299                                     |
|  Orders submitted (session)    25                                      |
|  Orders filled today (ledger)  42                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                5                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=263  buckets=23  win=32%                             |
|  Returns   avg=-2.8%  med=-38.2%  p10=-64.9%  p90=+83.4%               |
|  Realized  $+4,654.13                                                  |
|  Raw incl dropped  trades=774  real=$+1,863.58                         |
|  Today     trades=1  avg=-53.6%  med=-53.6%  real=$-30.00              |
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
|  ... 15 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b9   c009_s165_w2_1005_  7   0% -74.4 -66.2 -92.7 $   -301       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (5)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S164:AMD(5)                             |
+------------------------------------------------------------------------+
|  b21  S164 AMD      limit=0.60                                         |
|  b49  S164 AMD      limit=0.60                                         |
|  b77  S164 AMD      limit=0.60                                         |
|  b105 S164 AMD      limit=0.60                                         |
|  b133 S164 AMD      limit=0.60                                         |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-22.log
elapsed=126.5s reconcile=1.61s cancel=0.02s manage=0.03s scan=42.81s entries=77.14s
STATUS: options_morning_bot run complete (PAPER) elapsed=126.5s. run=#4702 https://github.com/28twagg-ops/TradingBot/actions/runs/29930886501
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_buckets.csv
Summary: 1 buckets closed trades, $-30.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 2.8% (22/774)
# Options signal frequency

_Generated 2026-07-22T10:57:49.021979_

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
| 2026-07-22 |    1 |    1 |    1 |    0 |    1 |    0 |    0 |    0 |     4 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 2 | 2 | 1.0 | ~38 active signal-days |
| S164 | 3 | 2 | 1.5 | ~25 active signal-days |
| S165 | 16 | 9 | 1.8 | ~22 active signal-days |
| S166 | 1 | 1 | 1.0 | ~38 active signal-days |
| S167 | 3 | 2 | 1.5 | ~25 active signal-days |
| S168 | 2 | 1 | 2.0 | ~19 active signal-days |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 60 | 2 |
| S164 | 72 | 3 |
| S165 | 1503 | 16 |
| S166 | 45 | 1 |
| S167 | 70 | 3 |
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
| 2026-07-22 |   30 |   37 |   81 |   15 |   35 |   20 |   77 |    0 |   295 |

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
| Total closed lots           |   304 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   616 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=482.12 router=CONFIRMED leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---

## Run 20260722T150041Z

- UTC timestamp: `20260722T150041Z`
- GitHub run: [#4703](https://github.com/28twagg-ops/TradingBot/actions/runs/29931281068)
- Run id: `29931281068`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`167s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-22T11:00:44.957158-04:00","date":"2026-07-22","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":161.2,"phases_s":{"reconcile":1.43,"cancel":0.02,"manage":0.04,"scan":79.62,"entries":78.29,"reconcile2":1.48},"signals":299,"placed":0,"equity":133490.65,"open_positions":0,"pending_orders":5,"open_lots":0,"submitted_today":25,"filled_today":42,"unattributed_contracts":0,"top_signals":["S165:AMD","S165:APH","S165:AMAT","S165:CB","S165:CIEN","S165:COHR","S165:COIN","S165:FIX"],"github_run":"4703","github_run_id":"29931281068","status":"ok"}
```

### Live bot full output

```text
15:00:42  INFO      Mode: exits
15:00:42  INFO        Daily log -> logs/daily/2026-07-22.md
15:00:42  INFO        Daily log reconciled -> logs/daily/2026-07-22.md (1 ledger rows)
15:00:42  INFO        place_all_stops: checking 5 positions...
15:00:42  INFO        STOP skipped AEP: fractional (0.7305 shares) — software exit will handle it
15:00:42  INFO        STOP skipped BIIB: fractional (0.4766 shares) — software exit will handle it
15:00:42  INFO        STOP skipped C: fractional (0.5268 shares) — software exit will handle it
15:00:42  INFO        STOP already live CARR @ $67.46
15:00:42  INFO        STOP skipped TPR: fractional (0.6841 shares) — software exit will handle it
15:00:43  INFO        [positions] 5/5 (5 valid)
15:00:43  INFO        Daily log -> logs/daily/2026-07-22.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:00 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $481.91|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  BIIB  P&L -0.1%  $-0.13                                           HOLD|
|  CARR  P&L -0.1%  $-0.12                                           HOLD|
|  C  P&L +0.3%  $+0.23                                              HOLD|
|  AEP  P&L +0.5%  $+0.48                                            HOLD|
|  TPR  P&L +1.4%  $+1.37                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           5|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                5|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
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
=== options_morning_bot (PAPER) 2026-07-22T11:00:44.957158-04:00 ===

[Run context]
Paper auth OK — equity $133490.65, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 299 signal(s); top: ['S165:AMD', 'S165:APH', 'S165:AMAT', 'S165:CB', 'S165:CIEN', 'S165:COHR', 'S165:COIN', 'S165:FIX']
Paper lab: $133353 broker equity -> 140 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 435 no tradeable call, 1060 already attempted today
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $133,490.65                             |
|  Signals this run              299                                     |
|  Orders submitted (session)    25                                      |
|  Orders filled today (ledger)  42                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                5                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=263  buckets=23  win=32%                             |
|  Returns   avg=-2.8%  med=-38.2%  p10=-64.9%  p90=+83.4%               |
|  Realized  $+4,654.13                                                  |
|  Raw incl dropped  trades=774  real=$+1,863.58                         |
|  Today     trades=1  avg=-53.6%  med=-53.6%  real=$-30.00              |
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
|  ... 15 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b9   c009_s165_w2_1005_  7   0% -74.4 -66.2 -92.7 $   -301       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (5)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S164:AMD(5)                             |
+------------------------------------------------------------------------+
|  b21  S164 AMD      limit=0.60                                         |
|  b49  S164 AMD      limit=0.60                                         |
|  b77  S164 AMD      limit=0.60                                         |
|  b105 S164 AMD      limit=0.60                                         |
|  b133 S164 AMD      limit=0.60                                         |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-22.log
elapsed=161.2s reconcile=1.43s cancel=0.02s manage=0.04s scan=79.62s entries=78.29s
STATUS: options_morning_bot run complete (PAPER) elapsed=161.2s. run=#4703 https://github.com/28twagg-ops/TradingBot/actions/runs/29931281068
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_buckets.csv
Summary: 1 buckets closed trades, $-30.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 2.8% (22/774)
# Options signal frequency

_Generated 2026-07-22T11:03:29.685300_

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
| 2026-07-22 |    1 |    1 |    1 |    0 |    1 |    0 |    0 |    0 |     4 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 2 | 2 | 1.0 | ~38 active signal-days |
| S164 | 3 | 2 | 1.5 | ~25 active signal-days |
| S165 | 16 | 9 | 1.8 | ~22 active signal-days |
| S166 | 1 | 1 | 1.0 | ~38 active signal-days |
| S167 | 3 | 2 | 1.5 | ~25 active signal-days |
| S168 | 2 | 1 | 2.0 | ~19 active signal-days |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 60 | 2 |
| S164 | 72 | 3 |
| S165 | 1503 | 16 |
| S166 | 45 | 1 |
| S167 | 70 | 3 |
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
| 2026-07-22 |   30 |   37 |   81 |   15 |   35 |   20 |   77 |    0 |   295 |

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
| Total closed lots           |   304 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   616 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=481.91 router=CONFIRMED leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---

## Run 20260722T150540Z

- UTC timestamp: `20260722T150540Z`
- GitHub run: [#4704](https://github.com/28twagg-ops/TradingBot/actions/runs/29931677442)
- Run id: `29931677442`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`159s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-22T11:05:45.504879-04:00","date":"2026-07-22","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":152.5,"phases_s":{"reconcile":1.69,"cancel":0.15,"manage":0.16,"scan":63.71,"entries":84.14,"reconcile2":1.74},"signals":299,"placed":0,"equity":134264.65,"open_positions":0,"pending_orders":5,"open_lots":0,"submitted_today":25,"filled_today":42,"unattributed_contracts":0,"top_signals":["S165:AMD","S165:APH","S165:AMAT","S165:CB","S165:CIEN","S165:COHR","S165:COIN","S165:FIX"],"github_run":"4704","github_run_id":"29931677442","status":"ok"}
```

### Live bot full output

```text
15:05:41  INFO      Mode: exits
15:05:42  INFO        Daily log -> logs/daily/2026-07-22.md
15:05:42  INFO        Daily log reconciled -> logs/daily/2026-07-22.md (1 ledger rows)
15:05:42  INFO        place_all_stops: checking 5 positions...
15:05:42  INFO        STOP skipped AEP: fractional (0.7305 shares) — software exit will handle it
15:05:42  INFO        STOP skipped BIIB: fractional (0.4766 shares) — software exit will handle it
15:05:42  INFO        STOP skipped C: fractional (0.5268 shares) — software exit will handle it
15:05:42  INFO        STOP already live CARR @ $67.46
15:05:42  INFO        STOP skipped TPR: fractional (0.6841 shares) — software exit will handle it
15:05:43  INFO        [positions] 5/5 (5 valid)
15:05:43  INFO        Daily log -> logs/daily/2026-07-22.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:05 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $481.37|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CARR  P&L -0.3%  $-0.28                                           HOLD|
|  BIIB  P&L -0.2%  $-0.18                                           HOLD|
|  AEP  P&L +0.3%  $+0.32                                            HOLD|
|  C  P&L +0.4%  $+0.29                                              HOLD|
|  TPR  P&L +1.2%  $+1.15                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           5|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                5|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
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
=== options_morning_bot (PAPER) 2026-07-22T11:05:45.504879-04:00 ===

[Run context]
Paper auth OK — equity $134264.65, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 299 signal(s); top: ['S165:AMD', 'S165:APH', 'S165:AMAT', 'S165:CB', 'S165:CIEN', 'S165:COHR', 'S165:COIN', 'S165:FIX']
Paper lab: $134366 broker equity -> 140 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 435 no tradeable call, 1060 already attempted today
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $134,264.65                             |
|  Signals this run              299                                     |
|  Orders submitted (session)    25                                      |
|  Orders filled today (ledger)  42                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                5                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=263  buckets=23  win=32%                             |
|  Returns   avg=-2.8%  med=-38.2%  p10=-64.9%  p90=+83.4%               |
|  Realized  $+4,654.13                                                  |
|  Raw incl dropped  trades=774  real=$+1,863.58                         |
|  Today     trades=1  avg=-53.6%  med=-53.6%  real=$-30.00              |
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
|  ... 15 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b9   c009_s165_w2_1005_  7   0% -74.4 -66.2 -92.7 $   -301       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (5)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S164:AMD(5)                             |
+------------------------------------------------------------------------+
|  b21  S164 AMD      limit=0.60                                         |
|  b49  S164 AMD      limit=0.60                                         |
|  b77  S164 AMD      limit=0.60                                         |
|  b105 S164 AMD      limit=0.60                                         |
|  b133 S164 AMD      limit=0.60                                         |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-22.log
elapsed=152.5s reconcile=1.69s cancel=0.15s manage=0.16s scan=63.71s entries=84.14s
STATUS: options_morning_bot run complete (PAPER) elapsed=152.5s. run=#4704 https://github.com/28twagg-ops/TradingBot/actions/runs/29931677442
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_buckets.csv
Summary: 1 buckets closed trades, $-30.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 2.8% (22/774)
# Options signal frequency

_Generated 2026-07-22T11:08:21.547889_

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
| 2026-07-22 |    1 |    1 |    1 |    0 |    1 |    0 |    0 |    0 |     4 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 2 | 2 | 1.0 | ~38 active signal-days |
| S164 | 3 | 2 | 1.5 | ~25 active signal-days |
| S165 | 16 | 9 | 1.8 | ~22 active signal-days |
| S166 | 1 | 1 | 1.0 | ~38 active signal-days |
| S167 | 3 | 2 | 1.5 | ~25 active signal-days |
| S168 | 2 | 1 | 2.0 | ~19 active signal-days |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 60 | 2 |
| S164 | 72 | 3 |
| S165 | 1503 | 16 |
| S166 | 45 | 1 |
| S167 | 70 | 3 |
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
| 2026-07-22 |   30 |   37 |   81 |   15 |   35 |   20 |   77 |    0 |   295 |

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
| Total closed lots           |   304 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   616 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=481.37 router=CONFIRMED leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---

## Run 20260722T151039Z

- UTC timestamp: `20260722T151039Z`
- GitHub run: [#4705](https://github.com/28twagg-ops/TradingBot/actions/runs/29932066233)
- Run id: `29932066233`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`143s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-22T11:10:43.458856-04:00","date":"2026-07-22","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":138.3,"phases_s":{"reconcile":1.41,"cancel":0.02,"manage":0.02,"scan":57.26,"entries":77.83,"reconcile2":1.45},"signals":299,"placed":0,"equity":134600.33,"open_positions":0,"pending_orders":5,"open_lots":0,"submitted_today":25,"filled_today":42,"unattributed_contracts":0,"top_signals":["S165:AMD","S165:APH","S165:AMAT","S165:CB","S165:CIEN","S165:COHR","S165:COIN","S165:FIX"],"github_run":"4705","github_run_id":"29932066233","status":"ok"}
```

### Live bot full output

```text
15:10:40  INFO      Mode: exits
15:10:41  INFO        Daily log -> logs/daily/2026-07-22.md
15:10:41  INFO        Daily log reconciled -> logs/daily/2026-07-22.md (1 ledger rows)
15:10:41  INFO        place_all_stops: checking 5 positions...
15:10:41  INFO        STOP skipped AEP: fractional (0.7305 shares) — software exit will handle it
15:10:41  INFO        STOP skipped BIIB: fractional (0.4766 shares) — software exit will handle it
15:10:41  INFO        STOP skipped C: fractional (0.5268 shares) — software exit will handle it
15:10:41  INFO        STOP already live CARR @ $67.46
15:10:41  INFO        STOP skipped TPR: fractional (0.6841 shares) — software exit will handle it
15:10:41  INFO        [positions] 5/5 (5 valid)
15:10:41  INFO        Daily log -> logs/daily/2026-07-22.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $481.15|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  BIIB  P&L -0.4%  $-0.41                                           HOLD|
|  CARR  P&L -0.3%  $-0.25                                           HOLD|
|  AEP  P&L +0.3%  $+0.29                                            HOLD|
|  C  P&L +0.4%  $+0.31                                              HOLD|
|  TPR  P&L +1.2%  $+1.13                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           5|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                5|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
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
=== options_morning_bot (PAPER) 2026-07-22T11:10:43.458856-04:00 ===

[Run context]
Paper auth OK — equity $134600.33, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 299 signal(s); top: ['S165:AMD', 'S165:APH', 'S165:AMAT', 'S165:CB', 'S165:CIEN', 'S165:COHR', 'S165:COIN', 'S165:FIX']
Paper lab: $134613 broker equity -> 140 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 435 no tradeable call, 1060 already attempted today
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $134,600.33                             |
|  Signals this run              299                                     |
|  Orders submitted (session)    25                                      |
|  Orders filled today (ledger)  42                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                5                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=263  buckets=23  win=32%                             |
|  Returns   avg=-2.8%  med=-38.2%  p10=-64.9%  p90=+83.4%               |
|  Realized  $+4,654.13                                                  |
|  Raw incl dropped  trades=774  real=$+1,863.58                         |
|  Today     trades=1  avg=-53.6%  med=-53.6%  real=$-30.00              |
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
|  ... 15 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b9   c009_s165_w2_1005_  7   0% -74.4 -66.2 -92.7 $   -301       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (5)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S164:AMD(5)                             |
+------------------------------------------------------------------------+
|  b21  S164 AMD      limit=0.60                                         |
|  b49  S164 AMD      limit=0.60                                         |
|  b77  S164 AMD      limit=0.60                                         |
|  b105 S164 AMD      limit=0.60                                         |
|  b133 S164 AMD      limit=0.60                                         |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-22.log
elapsed=138.3s reconcile=1.41s cancel=0.02s manage=0.02s scan=57.26s entries=77.83s
STATUS: options_morning_bot run complete (PAPER) elapsed=138.3s. run=#4705 https://github.com/28twagg-ops/TradingBot/actions/runs/29932066233
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_buckets.csv
Summary: 1 buckets closed trades, $-30.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 2.8% (22/774)
# Options signal frequency

_Generated 2026-07-22T11:13:05.150354_

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
| 2026-07-22 |    1 |    1 |    1 |    0 |    1 |    0 |    0 |    0 |     4 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 2 | 2 | 1.0 | ~38 active signal-days |
| S164 | 3 | 2 | 1.5 | ~25 active signal-days |
| S165 | 16 | 9 | 1.8 | ~22 active signal-days |
| S166 | 1 | 1 | 1.0 | ~38 active signal-days |
| S167 | 3 | 2 | 1.5 | ~25 active signal-days |
| S168 | 2 | 1 | 2.0 | ~19 active signal-days |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 60 | 2 |
| S164 | 72 | 3 |
| S165 | 1503 | 16 |
| S166 | 45 | 1 |
| S167 | 70 | 3 |
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
| 2026-07-22 |   30 |   37 |   81 |   15 |   35 |   20 |   77 |    0 |   295 |

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
| Total closed lots           |   304 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   616 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=481.15 router=CONFIRMED leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---

## Run 20260722T151545Z

- UTC timestamp: `20260722T151545Z`
- GitHub run: [#4706](https://github.com/28twagg-ops/TradingBot/actions/runs/29932461891)
- Run id: `29932461891`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`167s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-22T11:15:50.430555-04:00","date":"2026-07-22","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":160.7,"phases_s":{"reconcile":2.49,"cancel":0.05,"manage":0.04,"scan":77.3,"entries":79.0,"reconcile2":1.48},"signals":299,"placed":0,"equity":134712.65,"open_positions":0,"pending_orders":5,"open_lots":0,"submitted_today":25,"filled_today":42,"unattributed_contracts":0,"top_signals":["S165:AMD","S165:APH","S165:AMAT","S165:CB","S165:CIEN","S165:COHR","S165:COIN","S165:FIX"],"github_run":"4706","github_run_id":"29932461891","status":"ok"}
```

### Live bot full output

```text
15:15:46  INFO      Mode: exits
15:15:47  INFO        Daily log -> logs/daily/2026-07-22.md
15:15:47  INFO        Daily log reconciled -> logs/daily/2026-07-22.md (1 ledger rows)
15:15:47  INFO        place_all_stops: checking 5 positions...
15:15:47  INFO        STOP skipped AEP: fractional (0.7305 shares) — software exit will handle it
15:15:47  INFO        STOP skipped BIIB: fractional (0.4766 shares) — software exit will handle it
15:15:47  INFO        STOP skipped C: fractional (0.5268 shares) — software exit will handle it
15:15:47  INFO        STOP already live CARR @ $67.46
15:15:47  INFO        STOP skipped TPR: fractional (0.6841 shares) — software exit will handle it
15:15:48  INFO        [positions] 5/5 (5 valid)
15:15:48  INFO        Daily log -> logs/daily/2026-07-22.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:15 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $481.40|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  BIIB  P&L -0.3%  $-0.27                                           HOLD|
|  CARR  P&L -0.2%  $-0.16                                           HOLD|
|  AEP  P&L +0.3%  $+0.28                                            HOLD|
|  C  P&L +0.5%  $+0.35                                              HOLD|
|  TPR  P&L +1.2%  $+1.11                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           5|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                5|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
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
=== options_morning_bot (PAPER) 2026-07-22T11:15:50.430555-04:00 ===

[Run context]
Paper auth OK — equity $134712.65, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 299 signal(s); top: ['S165:AMD', 'S165:APH', 'S165:AMAT', 'S165:CB', 'S165:CIEN', 'S165:COHR', 'S165:COIN', 'S165:FIX']
Paper lab: $134585 broker equity -> 140 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 435 no tradeable call, 1060 already attempted today
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $134,712.65                             |
|  Signals this run              299                                     |
|  Orders submitted (session)    25                                      |
|  Orders filled today (ledger)  42                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                5                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=263  buckets=23  win=32%                             |
|  Returns   avg=-2.8%  med=-38.2%  p10=-64.9%  p90=+83.4%               |
|  Realized  $+4,654.13                                                  |
|  Raw incl dropped  trades=774  real=$+1,863.58                         |
|  Today     trades=1  avg=-53.6%  med=-53.6%  real=$-30.00              |
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
|  ... 15 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b9   c009_s165_w2_1005_  7   0% -74.4 -66.2 -92.7 $   -301       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (5)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S164:AMD(5)                             |
+------------------------------------------------------------------------+
|  b21  S164 AMD      limit=0.60                                         |
|  b49  S164 AMD      limit=0.60                                         |
|  b77  S164 AMD      limit=0.60                                         |
|  b105 S164 AMD      limit=0.60                                         |
|  b133 S164 AMD      limit=0.60                                         |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-22.log
elapsed=160.7s reconcile=2.49s cancel=0.05s manage=0.04s scan=77.3s entries=79.0s
STATUS: options_morning_bot run complete (PAPER) elapsed=160.7s. run=#4706 https://github.com/28twagg-ops/TradingBot/actions/runs/29932461891
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_buckets.csv
Summary: 1 buckets closed trades, $-30.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 2.8% (22/774)
# Options signal frequency

_Generated 2026-07-22T11:18:34.590277_

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
| 2026-07-22 |    1 |    1 |    1 |    0 |    1 |    0 |    0 |    0 |     4 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 2 | 2 | 1.0 | ~38 active signal-days |
| S164 | 3 | 2 | 1.5 | ~25 active signal-days |
| S165 | 16 | 9 | 1.8 | ~22 active signal-days |
| S166 | 1 | 1 | 1.0 | ~38 active signal-days |
| S167 | 3 | 2 | 1.5 | ~25 active signal-days |
| S168 | 2 | 1 | 2.0 | ~19 active signal-days |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 60 | 2 |
| S164 | 72 | 3 |
| S165 | 1503 | 16 |
| S166 | 45 | 1 |
| S167 | 70 | 3 |
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
| 2026-07-22 |   30 |   37 |   81 |   15 |   35 |   20 |   77 |    0 |   295 |

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
| Total closed lots           |   304 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   616 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=481.4 router=CONFIRMED leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---

## Run 20260722T152040Z

- UTC timestamp: `20260722T152040Z`
- GitHub run: [#4707](https://github.com/28twagg-ops/TradingBot/actions/runs/29932859246)
- Run id: `29932859246`
- Live bot: exit=`0`, duration=`4s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-22T11:15:50.430555-04:00","date":"2026-07-22","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":160.7,"phases_s":{"reconcile":2.49,"cancel":0.05,"manage":0.04,"scan":77.3,"entries":79.0,"reconcile2":1.48},"signals":299,"placed":0,"equity":134712.65,"open_positions":0,"pending_orders":5,"open_lots":0,"submitted_today":25,"filled_today":42,"unattributed_contracts":0,"top_signals":["S165:AMD","S165:APH","S165:AMAT","S165:CB","S165:CIEN","S165:COHR","S165:COIN","S165:FIX"],"github_run":"4706","github_run_id":"29932461891","status":"ok"}
```

### Live bot full output

```text
15:20:41  INFO      Mode: exits
15:20:42  INFO        Daily log -> logs/daily/2026-07-22.md
15:20:42  INFO        Daily log reconciled -> logs/daily/2026-07-22.md (1 ledger rows)
15:20:43  INFO        place_all_stops: checking 5 positions...
15:20:43  INFO        STOP skipped AEP: fractional (0.7305 shares) — software exit will handle it
15:20:43  INFO        STOP skipped BIIB: fractional (0.4766 shares) — software exit will handle it
15:20:43  INFO        STOP skipped C: fractional (0.5268 shares) — software exit will handle it
15:20:43  INFO        STOP already live CARR @ $67.46
15:20:43  INFO        STOP skipped TPR: fractional (0.6841 shares) — software exit will handle it
15:20:43  INFO        [positions] 5/5 (5 valid)
15:20:43  INFO        Daily log -> logs/daily/2026-07-22.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $481.51|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  BIIB  P&L -0.4%  $-0.40                                           HOLD|
|  CARR  P&L -0.1%  $-0.12                                           HOLD|
|  AEP  P&L +0.2%  $+0.23                                            HOLD|
|  C  P&L +0.7%  $+0.50                                              HOLD|
|  TPR  P&L +1.3%  $+1.23                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           5|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                5|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
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
=== options_morning_bot (PAPER) 2026-07-22T11:20:45.756959-04:00 ===

[Run context]
Paper auth OK — equity $134676.61, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 299 signal(s); top: ['S165:AMD', 'S165:APH', 'S165:AMAT', 'S165:CB', 'S165:CIEN', 'S165:COHR', 'S165:COIN', 'S165:FIX']
Paper lab: $134389 broker equity -> 140 bucket(s) ($500 virtual each, unlimited paper)
```

---

## Run 20260722T152606Z

- UTC timestamp: `20260722T152606Z`
- GitHub run: [#4708](https://github.com/28twagg-ops/TradingBot/actions/runs/29933262864)
- Run id: `29933262864`
- Live bot: exit=`0`, duration=`5s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-22T11:15:50.430555-04:00","date":"2026-07-22","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":160.7,"phases_s":{"reconcile":2.49,"cancel":0.05,"manage":0.04,"scan":77.3,"entries":79.0,"reconcile2":1.48},"signals":299,"placed":0,"equity":134712.65,"open_positions":0,"pending_orders":5,"open_lots":0,"submitted_today":25,"filled_today":42,"unattributed_contracts":0,"top_signals":["S165:AMD","S165:APH","S165:AMAT","S165:CB","S165:CIEN","S165:COHR","S165:COIN","S165:FIX"],"github_run":"4706","github_run_id":"29932461891","status":"ok"}
```

### Live bot full output

```text
15:26:08  INFO      Mode: exits
15:26:08  INFO        Daily log -> logs/daily/2026-07-22.md
15:26:08  INFO        Daily log reconciled -> logs/daily/2026-07-22.md (1 ledger rows)
15:26:08  INFO        place_all_stops: checking 5 positions...
15:26:08  INFO        STOP skipped AEP: fractional (0.7305 shares) — software exit will handle it
15:26:08  INFO        STOP skipped BIIB: fractional (0.4766 shares) — software exit will handle it
15:26:08  INFO        STOP skipped C: fractional (0.5268 shares) — software exit will handle it
15:26:08  INFO        STOP already live CARR @ $67.46
15:26:08  INFO        STOP skipped TPR: fractional (0.6841 shares) — software exit will handle it
15:26:08  INFO        [positions] 5/5 (5 valid)
15:26:08  INFO        SELL MARKET [urgent] BIIB closed
15:26:10  INFO        TX logged: SELL BIIB  P&L -0.51%
15:26:10  INFO        Daily log -> logs/daily/2026-07-22.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $481.81|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  BIIB  P&L -0.5%  $-0.49                        EXIT: stop_loss (-0.5%)|
|  CARR  P&L +0.0%  $+0.00                                           HOLD|
|  AEP  P&L +0.3%  $+0.29                                            HOLD|
|  C  P&L +0.8%  $+0.58                                              HOLD|
|  TPR  P&L +1.4%  $+1.35                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           5|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  1 attempted  |  1 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                4|
|  Logged exits                                                         1|
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  BIIB                                        -0.51%  (threshold -0.50%)|
|  Count                                                                1|
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=0 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=3
  zombies_flagged=0
options_reconcile: done
Layout: controlled:140:c000_s173_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:140:c000_s173_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      140
=== options_morning_bot (PAPER) 2026-07-22T11:26:12.457214-04:00 ===

[Run context]
Paper auth OK — equity $134401.55, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 299 signal(s); top: ['S165:AMD', 'S165:APH', 'S165:AMAT', 'S165:CB', 'S165:CIEN', 'S165:COHR', 'S165:COIN', 'S165:FIX']
Paper lab: $134516 broker equity -> 140 bucket(s) ($500 virtual each, unlimited paper)
```

---

## Run 20260722T153118Z

- UTC timestamp: `20260722T153118Z`
- GitHub run: [#4709](https://github.com/28twagg-ops/TradingBot/actions/runs/29933657422)
- Run id: `29933657422`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`200s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-22T11:31:23.135657-04:00","date":"2026-07-22","mode":"entry+manage","header":"entry+manage (5 new)","elapsed_s":194.3,"phases_s":{"reconcile":1.9,"cancel":0.14,"manage":2.21,"scan":78.08,"entries":109.37,"reconcile2":1.83},"signals":299,"placed":5,"equity":134339.25,"open_positions":2,"pending_orders":10,"open_lots":20,"submitted_today":45,"filled_today":62,"unattributed_contracts":0,"top_signals":["S165:AMD","S165:APH","S165:AMAT","S165:CB","S165:CIEN","S165:COHR","S165:COIN","S165:FIX"],"github_run":"4709","github_run_id":"29933657422","status":"ok"}
```

### Live bot full output

```text
15:31:19  INFO      Mode: exits
15:31:20  INFO        Daily log -> logs/daily/2026-07-22.md
15:31:20  INFO        Daily log reconciled -> logs/daily/2026-07-22.md (1 ledger rows)
15:31:20  INFO        place_all_stops: checking 4 positions...
15:31:20  INFO        STOP skipped AEP: fractional (0.7305 shares) — software exit will handle it
15:31:20  INFO        STOP skipped C: fractional (0.5268 shares) — software exit will handle it
15:31:20  INFO        STOP already live CARR @ $67.46
15:31:20  INFO        STOP skipped TPR: fractional (0.6841 shares) — software exit will handle it
15:31:21  INFO        [positions] 4/4 (4 valid)
15:31:21  INFO        Daily log -> logs/daily/2026-07-22.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $481.80|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CARR  P&L +0.0%  $+0.05                                           HOLD|
|  AEP  P&L +0.3%  $+0.25                                            HOLD|
|  C  P&L +0.8%  $+0.57                                              HOLD|
|  TPR  P&L +1.3%  $+1.27                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           4|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                4|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=0 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=4
  zombies_flagged=0
options_reconcile: done
Layout: controlled:140:c000_s173_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:140:c000_s173_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      140
=== options_morning_bot (PAPER) 2026-07-22T11:31:23.135657-04:00 ===

[Run context]
Paper auth OK — equity $134339.25, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 299 signal(s); top: ['S165:AMD', 'S165:APH', 'S165:AMAT', 'S165:CB', 'S165:CIEN', 'S165:COHR', 'S165:COIN', 'S165:FIX']
Paper lab: $134079 broker equity -> 140 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 465 no tradeable call, 742 already attempted today, 53 open order exists, 230 pending order
Placed 5 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $134,339.25                             |
|  Signals this run              299                                     |
|  Orders submitted (session)    45                                      |
|  Orders filled today (ledger)  62                                      |
|  Entries placed this run       5                                       |
|  Open virtual lots             20                                      |
|  Broker option positions       2                                       |
|  Pending orders                10                                      |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=263  buckets=23  win=32%                             |
|  Returns   avg=-2.8%  med=-38.2%  p10=-64.9%  p90=+83.4%               |
|  Realized  $+4,654.13                                                  |
|  Raw incl dropped  trades=774  real=$+1,863.58                         |
|  Today     trades=1  avg=-53.6%  med=-53.6%  real=$-30.00              |
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
|  ... 15 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b9   c009_s165_w2_1005_  7   0% -74.4 -66.2 -92.7 $   -301       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (10)                                                   |
+------------------------------------------------------------------------+
|  Top groups                    S164:AMD(5), S163:COIN(5)               |
+------------------------------------------------------------------------+
|  b21  S164 AMD      limit=0.60                                         |
|  b49  S164 AMD      limit=0.60                                         |
|  b77  S164 AMD      limit=0.60                                         |
|  b105 S164 AMD      limit=0.60                                         |
|  b133 S164 AMD      limit=0.60                                         |
|  ... 5 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (2)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMD260722C00570000           10    -34.5%   $   -195.00               |
|  COIN260724C00187500          10    -10.7%   $    -60.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-22.log
elapsed=194.3s reconcile=1.9s cancel=0.14s manage=2.21s scan=78.08s entries=109.37s
STATUS: options_morning_bot run complete (PAPER) elapsed=194.3s. run=#4709 https://github.com/28twagg-ops/TradingBot/actions/runs/29933657422
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_buckets.csv
Summary: 1 buckets closed trades, $-30.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 2.8% (22/774)
# Options signal frequency

_Generated 2026-07-22T11:34:40.793323_

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
| 2026-07-22 |    1 |    1 |    1 |    0 |    1 |    0 |    0 |    0 |     4 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 2 | 2 | 1.0 | ~38 active signal-days |
| S164 | 3 | 2 | 1.5 | ~25 active signal-days |
| S165 | 16 | 9 | 1.8 | ~22 active signal-days |
| S166 | 1 | 1 | 1.0 | ~38 active signal-days |
| S167 | 3 | 2 | 1.5 | ~25 active signal-days |
| S168 | 2 | 1 | 2.0 | ~19 active signal-days |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 65 | 2 |
| S164 | 82 | 3 |
| S165 | 1508 | 16 |
| S166 | 45 | 1 |
| S167 | 75 | 3 |
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
| 2026-07-22 |   35 |   47 |   86 |   15 |   40 |   20 |   77 |    0 |   320 |

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
| State/ledger mismatches     |    20 | WARN | <<<
| Total open lots             |    20 | INFO |
| Total closed lots           |   304 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   616 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=481.7 router=CONFIRMED leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---
