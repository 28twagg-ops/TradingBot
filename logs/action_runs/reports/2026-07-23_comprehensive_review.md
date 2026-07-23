# Daily Comprehensive Action Review — 2026-07-23

_Auto-generated from GitHub Actions run output. This document appends every run for the day._

## Run 20260723T000100Z

- UTC timestamp: `20260723T000100Z`
- GitHub run: [#4818](https://github.com/28twagg-ops/TradingBot/actions/runs/29967820365)
- Run id: `29967820365`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`8s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-22T20:01:04.297368-04:00","date":"2026-07-22","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":2.3,"phases_s":{"reconcile":1.76},"signals":0,"placed":0,"equity":136493.33,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":45,"filled_today":72,"unattributed_contracts":0,"top_signals":[],"github_run":"4818","github_run_id":"29967820365","status":"ok"}
```

### Live bot full output

```text
00:01:01  INFO      Mode: summary
00:01:02  INFO        Daily log -> logs/daily/2026-07-23.md
00:01:02  INFO        Daily log reconciled -> logs/daily/2026-07-23.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         00:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.22|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $482.22|
|  Cash                                                            $25.95|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $456.27|
|  Open P&L                                                        $+1.21|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (5 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AEP      Pullback50      $97.37     $131.94  $133.29  +1.0%   $+0.98  |
|  C        Pullback50      $69.62     $132.61  $132.15  -0.3%   $-0.24  |
|  CARR     Pullback50      $96.39     $67.80   $68.10   +0.4%   $+0.43  |
|  CHD      Pullback50      $96.37     $97.17   $97.13   -0.0%   $-0.04  |
|  LNT      Pullback50      $96.51     $73.97   $74.02   +0.1%   $+0.07  |
|                                                                        |
|  Total invested                                                 $456.27|
|  Total open P&L                                                  $+1.21|
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
|  2026-07-22  SELL  AVGO  Pullback50  $96.29  P&L $-0.14                |
|  2026-07-22  SELL  TPR  Pullback50  $97.94  P&L $+1.64                 |
|  2026-07-22  SELL  BIIB  Pullback50  $95.71  P&L $-0.49                |
|  2026-07-22  SELL  DUK  Pullback50  $97.64  P&L $+1.42                 |
|  2026-07-21  SELL  APA  Pullback50  $96.03  P&L $-0.00                 |
|  2026-07-21  SELL  BEN  Pullback50  $5.47  P&L $-0.09                  |
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
=== options_morning_bot (PAPER) 2026-07-22T20:01:04.297368-04:00 ===

[Run context]
After hours (20:01 ET) — exit summary only.
Paper auth OK — equity $136493.33, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $136,493.33                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    45                                      |
|  Orders filled today (ledger)  72                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=268  buckets=23  win=31%                             |
|  Returns   avg=-3.9%  med=-39.1%  p10=-64.9%  p90=+82.4%               |
|  Realized  $+4,452.13                                                  |
|  Raw incl dropped  trades=802  real=$+2,856.58                         |
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
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-22.log
elapsed=2.3s reconcile=1.76s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=2.3s. run=#4818 https://github.com/28twagg-ops/TradingBot/actions/runs/29967820365
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_buckets.csv
Summary: 1 buckets closed trades, $-30.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 2.7% (22/802)
# Options signal frequency

_Generated 2026-07-22T20:01:10.246280_

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
| S163 | 70 | 2 |
| S164 | 82 | 3 |
| S165 | 1508 | 16 |
| S166 | 45 | 1 |
| S167 | 80 | 3 |
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
| 2026-07-22 |   40 |   47 |   86 |   15 |   45 |   20 |   77 |    0 |   330 |

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
| Total closed lots           |   313 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   616 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=482.22 router=CONFIRMED leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---

## Run 20260723T015649Z

- UTC timestamp: `20260723T015649Z`
- GitHub run: [#4819](https://github.com/28twagg-ops/TradingBot/actions/runs/29973080648)
- Run id: `29973080648`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`7s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-22T21:56:52.999228-04:00","date":"2026-07-22","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":2.0,"phases_s":{"reconcile":1.62},"signals":0,"placed":0,"equity":137209.45,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":45,"filled_today":72,"unattributed_contracts":0,"top_signals":[],"github_run":"4819","github_run_id":"29973080648","status":"ok"}
```

### Live bot full output

```text
01:56:50  INFO      Mode: summary
01:56:50  INFO        Daily log -> logs/daily/2026-07-23.md
01:56:50  INFO        Daily log reconciled -> logs/daily/2026-07-23.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         01:56 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.22|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $482.22|
|  Cash                                                            $25.95|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $456.27|
|  Open P&L                                                        $+1.21|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (5 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AEP      Pullback50      $97.37     $131.94  $133.29  +1.0%   $+0.98  |
|  C        Pullback50      $69.62     $132.61  $132.15  -0.3%   $-0.24  |
|  CARR     Pullback50      $96.39     $67.80   $68.10   +0.4%   $+0.43  |
|  CHD      Pullback50      $96.37     $97.17   $97.13   -0.0%   $-0.04  |
|  LNT      Pullback50      $96.51     $73.97   $74.02   +0.1%   $+0.07  |
|                                                                        |
|  Total invested                                                 $456.27|
|  Total open P&L                                                  $+1.21|
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
|  2026-07-22  SELL  AVGO  Pullback50  $96.29  P&L $-0.14                |
|  2026-07-22  SELL  TPR  Pullback50  $97.94  P&L $+1.64                 |
|  2026-07-22  SELL  BIIB  Pullback50  $95.71  P&L $-0.49                |
|  2026-07-22  SELL  DUK  Pullback50  $97.64  P&L $+1.42                 |
|  2026-07-21  SELL  APA  Pullback50  $96.03  P&L $-0.00                 |
|  2026-07-21  SELL  BEN  Pullback50  $5.47  P&L $-0.09                  |
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
=== options_morning_bot (PAPER) 2026-07-22T21:56:52.999228-04:00 ===

[Run context]
After hours (21:56 ET) — exit summary only.
Paper auth OK — equity $137209.45, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $137,209.45                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    45                                      |
|  Orders filled today (ledger)  72                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=268  buckets=23  win=31%                             |
|  Returns   avg=-3.9%  med=-39.1%  p10=-64.9%  p90=+82.4%               |
|  Realized  $+4,452.13                                                  |
|  Raw incl dropped  trades=802  real=$+2,856.58                         |
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
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-22.log
elapsed=2.0s reconcile=1.62s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=2.0s. run=#4819 https://github.com/28twagg-ops/TradingBot/actions/runs/29973080648
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_buckets.csv
Summary: 1 buckets closed trades, $-30.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-22_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 2.7% (22/802)
# Options signal frequency

_Generated 2026-07-22T21:56:58.238652_

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
| S163 | 70 | 2 |
| S164 | 82 | 3 |
| S165 | 1508 | 16 |
| S166 | 45 | 1 |
| S167 | 80 | 3 |
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
| 2026-07-22 |   40 |   47 |   86 |   15 |   45 |   20 |   77 |    0 |   330 |

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
| Total closed lots           |   313 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   616 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=482.22 router=CONFIRMED leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---

## Run 20260723T052032Z

- UTC timestamp: `20260723T052032Z`
- GitHub run: [#4820](https://github.com/28twagg-ops/TradingBot/actions/runs/29981859667)
- Run id: `29981859667`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`7s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-23T01:20:36.173774-04:00","date":"2026-07-23","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.9,"phases_s":{"reconcile":1.54},"signals":0,"placed":0,"equity":136321.45,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4820","github_run_id":"29981859667","status":"ok"}
```

### Live bot full output

```text
05:20:33  INFO      Mode: summary
05:20:34  INFO        Daily log -> logs/daily/2026-07-23.md
05:20:34  INFO        Daily log reconciled -> logs/daily/2026-07-23.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         05:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.22|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $482.22|
|  Cash                                                            $25.95|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $456.27|
|  Open P&L                                                        $+1.21|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (5 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AEP      Pullback50      $97.37     $131.94  $133.29  +1.0%   $+0.98  |
|  C        Pullback50      $69.62     $132.61  $132.15  -0.3%   $-0.24  |
|  CARR     Pullback50      $96.39     $67.80   $68.10   +0.4%   $+0.43  |
|  CHD      Pullback50      $96.37     $97.17   $97.13   -0.0%   $-0.04  |
|  LNT      Pullback50      $96.51     $73.97   $74.02   +0.1%   $+0.07  |
|                                                                        |
|  Total invested                                                 $456.27|
|  Total open P&L                                                  $+1.21|
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
|  2026-07-22  SELL  AVGO  Pullback50  $96.29  P&L $-0.14                |
|  2026-07-22  SELL  TPR  Pullback50  $97.94  P&L $+1.64                 |
|  2026-07-22  SELL  BIIB  Pullback50  $95.71  P&L $-0.49                |
|  2026-07-22  SELL  DUK  Pullback50  $97.64  P&L $+1.42                 |
|  2026-07-21  SELL  APA  Pullback50  $96.03  P&L $-0.00                 |
|  2026-07-21  SELL  BEN  Pullback50  $5.47  P&L $-0.09                  |
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
=== options_morning_bot (PAPER) 2026-07-23T01:20:36.173774-04:00 ===

[Run context]
After hours (01:20 ET) — exit summary only.
Paper auth OK — equity $136321.45, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $136,321.45                             |
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
|  Reflected trades=268  buckets=23  win=31%                             |
|  Returns   avg=-3.9%  med=-39.1%  p10=-64.9%  p90=+82.4%               |
|  Realized  $+4,452.13                                                  |
|  Raw incl dropped  trades=802  real=$+2,856.58                         |
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
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-23.log
elapsed=1.9s reconcile=1.54s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.9s. run=#4820 https://github.com/28twagg-ops/TradingBot/actions/runs/29981859667
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-23_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-23_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-23_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-23_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 2.7% (22/802)
# Options signal frequency

_Generated 2026-07-23T01:20:40.913820_

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
| S163 | 100 | 2 |
| S164 | 124 | 3 |
| S165 | 1558 | 16 |
| S166 | 60 | 1 |
| S167 | 120 | 3 |
| S168 | 75 | 2 |
| S173 | 1871 | 17 |
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
| 2026-07-22 |   40 |   47 |   86 |   15 |   45 |   20 |   77 |    0 |   330 |
| 2026-07-23 |   30 |   42 |   50 |   15 |   40 |   20 |   40 |    0 |   237 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-07-23
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |    18 | WARN | <<<
| Missing exit records (post) |    18 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |   313 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   616 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=482.22 router=CONFIRMED leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---

## Run 20260723T130042Z

- UTC timestamp: `20260723T130042Z`
- GitHub run: [#4821](https://github.com/28twagg-ops/TradingBot/actions/runs/30009306334)
- Run id: `30009306334`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`8s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-23T09:00:47.301194-04:00","date":"2026-07-23","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":2.3,"phases_s":{"reconcile":1.85},"signals":0,"placed":0,"equity":134193.45,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4821","github_run_id":"30009306334","status":"ok"}
```

### Live bot full output

```text
13:00:43  INFO      Mode: summary
13:00:44  INFO        Daily log -> logs/daily/2026-07-23.md
13:00:44  INFO        Daily log reconciled -> logs/daily/2026-07-23.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:00 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.76|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $482.76|
|  Cash                                                            $25.95|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $456.81|
|  Open P&L                                                        $+1.75|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (5 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AEP      Pullback50      $97.37     $131.94  $133.29  +1.0%   $+0.98  |
|  C        Pullback50      $69.33     $132.61  $131.60  -0.8%   $-0.53  |
|  CARR     Pullback50      $97.22     $67.80   $68.69   +1.3%   $+1.26  |
|  CHD      Pullback50      $96.37     $97.17   $97.13   -0.0%   $-0.04  |
|  LNT      Pullback50      $96.51     $73.97   $74.02   +0.1%   $+0.07  |
|                                                                        |
|  Total invested                                                 $456.81|
|  Total open P&L                                                  $+1.75|
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
|  2026-07-22  SELL  AVGO  Pullback50  $96.29  P&L $-0.14                |
|  2026-07-22  SELL  TPR  Pullback50  $97.94  P&L $+1.64                 |
|  2026-07-22  SELL  BIIB  Pullback50  $95.71  P&L $-0.49                |
|  2026-07-22  SELL  DUK  Pullback50  $97.64  P&L $+1.42                 |
|  2026-07-21  SELL  APA  Pullback50  $96.03  P&L $-0.00                 |
|  2026-07-21  SELL  BEN  Pullback50  $5.47  P&L $-0.09                  |
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
=== options_morning_bot (PAPER) 2026-07-23T09:00:47.301194-04:00 ===

[Run context]
After hours (09:00 ET) — exit summary only.
Paper auth OK — equity $134193.45, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $134,193.45                             |
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
|  Reflected trades=268  buckets=23  win=31%                             |
|  Returns   avg=-3.9%  med=-39.1%  p10=-64.9%  p90=+82.4%               |
|  Realized  $+4,452.13                                                  |
|  Raw incl dropped  trades=802  real=$+2,856.58                         |
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
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-23.log
elapsed=2.3s reconcile=1.85s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=2.3s. run=#4821 https://github.com/28twagg-ops/TradingBot/actions/runs/30009306334
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-23_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-23_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-23_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-23_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 2.7% (22/802)
# Options signal frequency

_Generated 2026-07-23T09:00:53.214645_

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
| S163 | 100 | 2 |
| S164 | 124 | 3 |
| S165 | 1558 | 16 |
| S166 | 60 | 1 |
| S167 | 120 | 3 |
| S168 | 75 | 2 |
| S173 | 1871 | 17 |
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
| 2026-07-22 |   40 |   47 |   86 |   15 |   45 |   20 |   77 |    0 |   330 |
| 2026-07-23 |   30 |   42 |   50 |   15 |   40 |   20 |   40 |    0 |   237 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-07-23
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |    18 | WARN | <<<
| Missing exit records (post) |    18 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |   313 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   616 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=482.76 router=CONFIRMED leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---

## Run 20260723T130538Z

- UTC timestamp: `20260723T130538Z`
- GitHub run: [#4822](https://github.com/28twagg-ops/TradingBot/actions/runs/30009669259)
- Run id: `30009669259`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`8s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-23T09:05:42.021713-04:00","date":"2026-07-23","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":2.4,"phases_s":{"reconcile":1.88},"signals":0,"placed":0,"equity":134013.45,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4822","github_run_id":"30009669259","status":"ok"}
```

### Live bot full output

```text
13:05:39  INFO      Mode: summary
13:05:40  INFO        Daily log -> logs/daily/2026-07-23.md
13:05:40  INFO        Daily log reconciled -> logs/daily/2026-07-23.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:05 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.43|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $482.43|
|  Cash                                                            $25.95|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $456.48|
|  Open P&L                                                        $+1.42|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (5 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AEP      Pullback50      $97.09     $131.94  $132.90  +0.7%   $+0.70  |
|  C        Pullback50      $69.28     $132.61  $131.51  -0.8%   $-0.58  |
|  CARR     Pullback50      $97.22     $67.80   $68.69   +1.3%   $+1.26  |
|  CHD      Pullback50      $96.37     $97.17   $97.13   -0.0%   $-0.04  |
|  LNT      Pullback50      $96.51     $73.97   $74.02   +0.1%   $+0.07  |
|                                                                        |
|  Total invested                                                 $456.48|
|  Total open P&L                                                  $+1.42|
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
|  2026-07-22  SELL  AVGO  Pullback50  $96.29  P&L $-0.14                |
|  2026-07-22  SELL  TPR  Pullback50  $97.94  P&L $+1.64                 |
|  2026-07-22  SELL  BIIB  Pullback50  $95.71  P&L $-0.49                |
|  2026-07-22  SELL  DUK  Pullback50  $97.64  P&L $+1.42                 |
|  2026-07-21  SELL  APA  Pullback50  $96.03  P&L $-0.00                 |
|  2026-07-21  SELL  BEN  Pullback50  $5.47  P&L $-0.09                  |
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
=== options_morning_bot (PAPER) 2026-07-23T09:05:42.021713-04:00 ===

[Run context]
After hours (09:05 ET) — exit summary only.
Paper auth OK — equity $134013.45, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $134,013.45                             |
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
|  Reflected trades=268  buckets=23  win=31%                             |
|  Returns   avg=-3.9%  med=-39.1%  p10=-64.9%  p90=+82.4%               |
|  Realized  $+4,452.13                                                  |
|  Raw incl dropped  trades=802  real=$+2,856.58                         |
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
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-23.log
elapsed=2.4s reconcile=1.88s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=2.4s. run=#4822 https://github.com/28twagg-ops/TradingBot/actions/runs/30009669259
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-23_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-23_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-23_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-23_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 2.7% (22/802)
# Options signal frequency

_Generated 2026-07-23T09:05:48.039932_

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
| S163 | 100 | 2 |
| S164 | 124 | 3 |
| S165 | 1558 | 16 |
| S166 | 60 | 1 |
| S167 | 120 | 3 |
| S168 | 75 | 2 |
| S173 | 1871 | 17 |
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
| 2026-07-22 |   40 |   47 |   86 |   15 |   45 |   20 |   77 |    0 |   330 |
| 2026-07-23 |   30 |   42 |   50 |   15 |   40 |   20 |   40 |    0 |   237 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-07-23
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |    18 | WARN | <<<
| Missing exit records (post) |    18 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |   313 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   616 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=482.43 router=CONFIRMED leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---

## Run 20260723T131041Z

- UTC timestamp: `20260723T131041Z`
- GitHub run: [#4823](https://github.com/28twagg-ops/TradingBot/actions/runs/30010025539)
- Run id: `30010025539`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`8s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-23T09:10:44.632083-04:00","date":"2026-07-23","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.8,"phases_s":{"reconcile":1.56},"signals":0,"placed":0,"equity":133681.09,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4823","github_run_id":"30010025539","status":"ok"}
```

### Live bot full output

```text
13:10:42  INFO      Mode: summary
13:10:42  INFO        Daily log -> logs/daily/2026-07-23.md
13:10:42  INFO        Daily log reconciled -> logs/daily/2026-07-23.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.43|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $482.43|
|  Cash                                                            $25.95|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $456.48|
|  Open P&L                                                        $+1.42|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (5 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AEP      Pullback50      $97.09     $131.94  $132.90  +0.7%   $+0.70  |
|  C        Pullback50      $69.28     $132.61  $131.51  -0.8%   $-0.58  |
|  CARR     Pullback50      $97.22     $67.80   $68.69   +1.3%   $+1.26  |
|  CHD      Pullback50      $96.37     $97.17   $97.13   -0.0%   $-0.04  |
|  LNT      Pullback50      $96.51     $73.97   $74.02   +0.1%   $+0.07  |
|                                                                        |
|  Total invested                                                 $456.48|
|  Total open P&L                                                  $+1.42|
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
|  2026-07-22  SELL  AVGO  Pullback50  $96.29  P&L $-0.14                |
|  2026-07-22  SELL  TPR  Pullback50  $97.94  P&L $+1.64                 |
|  2026-07-22  SELL  BIIB  Pullback50  $95.71  P&L $-0.49                |
|  2026-07-22  SELL  DUK  Pullback50  $97.64  P&L $+1.42                 |
|  2026-07-21  SELL  APA  Pullback50  $96.03  P&L $-0.00                 |
|  2026-07-21  SELL  BEN  Pullback50  $5.47  P&L $-0.09                  |
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
=== options_morning_bot (PAPER) 2026-07-23T09:10:44.632083-04:00 ===

[Run context]
After hours (09:10 ET) — exit summary only.
Paper auth OK — equity $133681.09, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $133,681.09                             |
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
|  Reflected trades=268  buckets=23  win=31%                             |
|  Returns   avg=-3.9%  med=-39.1%  p10=-64.9%  p90=+82.4%               |
|  Realized  $+4,452.13                                                  |
|  Raw incl dropped  trades=802  real=$+2,856.58                         |
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
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-23.log
elapsed=1.8s reconcile=1.56s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.8s. run=#4823 https://github.com/28twagg-ops/TradingBot/actions/runs/30010025539
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-23_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-23_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-23_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-23_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 2.7% (22/802)
# Options signal frequency

_Generated 2026-07-23T09:10:50.281684_

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
| S163 | 100 | 2 |
| S164 | 124 | 3 |
| S165 | 1558 | 16 |
| S166 | 60 | 1 |
| S167 | 120 | 3 |
| S168 | 75 | 2 |
| S173 | 1871 | 17 |
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
| 2026-07-22 |   40 |   47 |   86 |   15 |   45 |   20 |   77 |    0 |   330 |
| 2026-07-23 |   30 |   42 |   50 |   15 |   40 |   20 |   40 |    0 |   237 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-07-23
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |    18 | WARN | <<<
| Missing exit records (post) |    18 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |   313 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   616 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=482.43 router=CONFIRMED leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---

## Run 20260723T131534Z

- UTC timestamp: `20260723T131534Z`
- GitHub run: [#4824](https://github.com/28twagg-ops/TradingBot/actions/runs/30010386884)
- Run id: `30010386884`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`7s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-23T09:15:39.777527-04:00","date":"2026-07-23","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.8,"phases_s":{"reconcile":1.52},"signals":0,"placed":0,"equity":133577.45,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4824","github_run_id":"30010386884","status":"ok"}
```

### Live bot full output

```text
13:15:36  INFO      Mode: summary
13:15:38  INFO        Daily log -> logs/daily/2026-07-23.md
13:15:38  INFO        Daily log reconciled -> logs/daily/2026-07-23.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:15 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.30|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $482.30|
|  Cash                                                            $25.95|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $456.35|
|  Open P&L                                                        $+1.29|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (5 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AEP      Pullback50      $97.09     $131.94  $132.90  +0.7%   $+0.70  |
|  C        Pullback50      $69.15     $132.61  $131.26  -1.0%   $-0.71  |
|  CARR     Pullback50      $97.22     $67.80   $68.69   +1.3%   $+1.26  |
|  CHD      Pullback50      $96.37     $97.17   $97.13   -0.0%   $-0.04  |
|  LNT      Pullback50      $96.51     $73.97   $74.02   +0.1%   $+0.07  |
|                                                                        |
|  Total invested                                                 $456.35|
|  Total open P&L                                                  $+1.29|
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
|  2026-07-22  SELL  AVGO  Pullback50  $96.29  P&L $-0.14                |
|  2026-07-22  SELL  TPR  Pullback50  $97.94  P&L $+1.64                 |
|  2026-07-22  SELL  BIIB  Pullback50  $95.71  P&L $-0.49                |
|  2026-07-22  SELL  DUK  Pullback50  $97.64  P&L $+1.42                 |
|  2026-07-21  SELL  APA  Pullback50  $96.03  P&L $-0.00                 |
|  2026-07-21  SELL  BEN  Pullback50  $5.47  P&L $-0.09                  |
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
=== options_morning_bot (PAPER) 2026-07-23T09:15:39.777527-04:00 ===

[Run context]
After hours (09:15 ET) — exit summary only.
Paper auth OK — equity $133577.45, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $133,577.45                             |
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
|  Reflected trades=268  buckets=23  win=31%                             |
|  Returns   avg=-3.9%  med=-39.1%  p10=-64.9%  p90=+82.4%               |
|  Realized  $+4,452.13                                                  |
|  Raw incl dropped  trades=802  real=$+2,856.58                         |
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
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-23.log
elapsed=1.8s reconcile=1.52s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.8s. run=#4824 https://github.com/28twagg-ops/TradingBot/actions/runs/30010386884
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-23_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-23_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-23_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-23_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 2.7% (22/802)
# Options signal frequency

_Generated 2026-07-23T09:15:45.300089_

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
| S163 | 100 | 2 |
| S164 | 124 | 3 |
| S165 | 1558 | 16 |
| S166 | 60 | 1 |
| S167 | 120 | 3 |
| S168 | 75 | 2 |
| S173 | 1871 | 17 |
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
| 2026-07-22 |   40 |   47 |   86 |   15 |   45 |   20 |   77 |    0 |   330 |
| 2026-07-23 |   30 |   42 |   50 |   15 |   40 |   20 |   40 |    0 |   237 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-07-23
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |    18 | WARN | <<<
| Missing exit records (post) |    18 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |   313 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   616 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=482.3 router=CONFIRMED leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---

## Run 20260723T132037Z

- UTC timestamp: `20260723T132037Z`
- GitHub run: [#4825](https://github.com/28twagg-ops/TradingBot/actions/runs/30010745635)
- Run id: `30010745635`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`8s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-23T09:20:40.385319-04:00","date":"2026-07-23","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.6,"phases_s":{"reconcile":1.38},"signals":0,"placed":0,"equity":133441.45,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4825","github_run_id":"30010745635","status":"ok"}
```

### Live bot full output

```text
13:20:38  INFO      Mode: summary
13:20:38  INFO        Daily log -> logs/daily/2026-07-23.md
13:20:38  INFO        Daily log reconciled -> logs/daily/2026-07-23.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.30|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $482.30|
|  Cash                                                            $25.95|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $456.35|
|  Open P&L                                                        $+1.29|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (5 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AEP      Pullback50      $97.09     $131.94  $132.90  +0.7%   $+0.70  |
|  C        Pullback50      $69.15     $132.61  $131.26  -1.0%   $-0.71  |
|  CARR     Pullback50      $97.22     $67.80   $68.69   +1.3%   $+1.26  |
|  CHD      Pullback50      $96.37     $97.17   $97.13   -0.0%   $-0.04  |
|  LNT      Pullback50      $96.51     $73.97   $74.02   +0.1%   $+0.07  |
|                                                                        |
|  Total invested                                                 $456.35|
|  Total open P&L                                                  $+1.29|
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
|  2026-07-22  SELL  AVGO  Pullback50  $96.29  P&L $-0.14                |
|  2026-07-22  SELL  TPR  Pullback50  $97.94  P&L $+1.64                 |
|  2026-07-22  SELL  BIIB  Pullback50  $95.71  P&L $-0.49                |
|  2026-07-22  SELL  DUK  Pullback50  $97.64  P&L $+1.42                 |
|  2026-07-21  SELL  APA  Pullback50  $96.03  P&L $-0.00                 |
|  2026-07-21  SELL  BEN  Pullback50  $5.47  P&L $-0.09                  |
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
=== options_morning_bot (PAPER) 2026-07-23T09:20:40.385319-04:00 ===

[Run context]
After hours (09:20 ET) — exit summary only.
Paper auth OK — equity $133441.45, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $133,441.45                             |
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
|  Reflected trades=268  buckets=23  win=31%                             |
|  Returns   avg=-3.9%  med=-39.1%  p10=-64.9%  p90=+82.4%               |
|  Realized  $+4,452.13                                                  |
|  Raw incl dropped  trades=802  real=$+2,856.58                         |
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
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-23.log
elapsed=1.6s reconcile=1.38s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.6s. run=#4825 https://github.com/28twagg-ops/TradingBot/actions/runs/30010745635
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-23_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-23_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-23_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-23_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 2.7% (22/802)
# Options signal frequency

_Generated 2026-07-23T09:20:45.633095_

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
| S163 | 100 | 2 |
| S164 | 124 | 3 |
| S165 | 1558 | 16 |
| S166 | 60 | 1 |
| S167 | 120 | 3 |
| S168 | 75 | 2 |
| S173 | 1871 | 17 |
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
| 2026-07-22 |   40 |   47 |   86 |   15 |   45 |   20 |   77 |    0 |   330 |
| 2026-07-23 |   30 |   42 |   50 |   15 |   40 |   20 |   40 |    0 |   237 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-07-23
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |    18 | WARN | <<<
| Missing exit records (post) |    18 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |   313 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   616 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=482.3 router=CONFIRMED leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---

## Run 20260723T132551Z

- UTC timestamp: `20260723T132551Z`
- GitHub run: [#4826](https://github.com/28twagg-ops/TradingBot/actions/runs/30011102545)
- Run id: `30011102545`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`6s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-23T09:25:54.569304-04:00","date":"2026-07-23","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":2.3,"phases_s":{"reconcile":2.07},"signals":0,"placed":0,"equity":133813.45,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4826","github_run_id":"30011102545","status":"ok"}
```

### Live bot full output

```text
13:25:52  INFO      Mode: summary
13:25:53  INFO        Daily log -> logs/daily/2026-07-23.md
13:25:53  INFO        Daily log reconciled -> logs/daily/2026-07-23.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:25 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $481.85|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $481.85|
|  Cash                                                            $25.95|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $455.90|
|  Open P&L                                                        $+0.84|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (5 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AEP      Pullback50      $96.84     $131.94  $132.56  +0.5%   $+0.45  |
|  C        Pullback50      $68.95     $132.61  $130.89  -1.3%   $-0.91  |
|  CARR     Pullback50      $97.22     $67.80   $68.69   +1.3%   $+1.26  |
|  CHD      Pullback50      $96.37     $97.17   $97.13   -0.0%   $-0.04  |
|  LNT      Pullback50      $96.51     $73.97   $74.02   +0.1%   $+0.07  |
|                                                                        |
|  Total invested                                                 $455.90|
|  Total open P&L                                                  $+0.84|
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
|  2026-07-22  SELL  AVGO  Pullback50  $96.29  P&L $-0.14                |
|  2026-07-22  SELL  TPR  Pullback50  $97.94  P&L $+1.64                 |
|  2026-07-22  SELL  BIIB  Pullback50  $95.71  P&L $-0.49                |
|  2026-07-22  SELL  DUK  Pullback50  $97.64  P&L $+1.42                 |
|  2026-07-21  SELL  APA  Pullback50  $96.03  P&L $-0.00                 |
|  2026-07-21  SELL  BEN  Pullback50  $5.47  P&L $-0.09                  |
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
=== options_morning_bot (PAPER) 2026-07-23T09:25:54.569304-04:00 ===

[Run context]
After hours (09:25 ET) — exit summary only.
Paper auth OK — equity $133813.45, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $133,813.45                             |
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
|  Reflected trades=268  buckets=23  win=31%                             |
|  Returns   avg=-3.9%  med=-39.1%  p10=-64.9%  p90=+82.4%               |
|  Realized  $+4,452.13                                                  |
|  Raw incl dropped  trades=802  real=$+2,856.58                         |
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
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-23.log
elapsed=2.3s reconcile=2.07s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=2.3s. run=#4826 https://github.com/28twagg-ops/TradingBot/actions/runs/30011102545
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-23_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-23_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-23_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-23_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 2.7% (22/802)
# Options signal frequency

_Generated 2026-07-23T09:25:59.219941_

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
| S163 | 100 | 2 |
| S164 | 124 | 3 |
| S165 | 1558 | 16 |
| S166 | 60 | 1 |
| S167 | 120 | 3 |
| S168 | 75 | 2 |
| S173 | 1871 | 17 |
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
| 2026-07-22 |   40 |   47 |   86 |   15 |   45 |   20 |   77 |    0 |   330 |
| 2026-07-23 |   30 |   42 |   50 |   15 |   40 |   20 |   40 |    0 |   237 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-07-23
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |    18 | WARN | <<<
| Missing exit records (post) |    18 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |   313 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   616 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=481.85 router=CONFIRMED leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---

## Run 20260723T133040Z

- UTC timestamp: `20260723T133040Z`
- GitHub run: [#4827](https://github.com/28twagg-ops/TradingBot/actions/runs/30011465239)
- Run id: `30011465239`
- Live bot: exit=`0`, duration=`215s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-23T09:25:54.569304-04:00","date":"2026-07-23","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":2.3,"phases_s":{"reconcile":2.07},"signals":0,"placed":0,"equity":133813.45,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4826","github_run_id":"30011102545","status":"ok"}
```

### Live bot full output

```text
13:30:41  INFO      Mode: morning_prep
13:30:41  INFO        [prep_positions] 5/5 (5 valid)
13:30:41  INFO      Fetching tickers (universe=both)...
13:30:42  INFO        S&P 500: 503
13:30:42  INFO        MidCap 400: 400
13:30:42  INFO        Total: 903 tickers
13:30:43  INFO        [prep_universe] 40/898 (40 valid)
13:30:45  INFO        [prep_universe] 80/898 (80 valid)
13:30:46  INFO        [prep_universe] 120/898 (120 valid)
13:30:47  INFO        [prep_universe] 160/898 (160 valid)
13:30:49  INFO        [prep_universe] 200/898 (199 valid)
13:30:56  INFO        [prep_universe] 240/898 (238 valid)
13:31:09  INFO        [prep_universe] 280/898 (278 valid)
13:31:20  INFO        [prep_universe] 320/898 (318 valid)
13:31:33  INFO        [prep_universe] 360/898 (358 valid)
13:31:44  INFO        [prep_universe] 400/898 (397 valid)
13:31:57  INFO        [prep_universe] 440/898 (437 valid)
13:32:07  INFO        [prep_universe] 480/898 (477 valid)
13:32:21  INFO        [prep_universe] 520/898 (517 valid)
13:32:31  INFO        [prep_universe] 560/898 (557 valid)
13:32:44  INFO        [prep_universe] 600/898 (597 valid)
13:32:57  INFO        [prep_universe] 640/898 (637 valid)
13:33:07  INFO        [prep_universe] 680/898 (677 valid)
13:33:21  INFO        [prep_universe] 720/898 (717 valid)
13:33:31  INFO        [prep_universe] 760/898 (757 valid)
13:33:44  INFO        [prep_universe] 800/898 (797 valid)
13:33:57  INFO        [prep_universe] 840/898 (836 valid)
13:34:07  INFO        [prep_universe] 880/898 (876 valid)
13:34:14  INFO        [prep_universe] 898/898 (894 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:30 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $478.12|
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
|  Open positions                                                       5|
|  Invested                                                       $378.89|
|  Open P&L                                                        $-2.20|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AEP      Pullback50      $96.71     $131.94  $132.38  +0.3%   $+0.32  |
|  C        Pullback50      $68.96     $132.61  $130.90  -1.3%   $-0.90  |
|  CARR     Pullback50      $95.91     $67.80   $67.76   -0.1%   $-0.05  |
|  CHD      Pullback50      $94.96     $97.17   $95.70   -1.5%   $-1.45  |
|  LNT      Pullback50      $22.36     $73.97   $73.58   -0.5%   $-0.12  |
+========================================================================+

+========================================================================+
|                            OPEN SELL ORDERS                            |
+========================================================================+
|  Count                                                                1|
|  TICKER    TYPE              QTY       LIMIT       STOP                |
+------------------------------------------------------------------------+
|  CARR      OrderType.STOP    1         None        67.75               |
+========================================================================+

+========================================================================+
|                              PREP SUMMARY                              |
+========================================================================+
|  Saved                                                              yes|
|  Exit candidates                                                      3|
|  Signal candidates                                                   33|
|  Universe scanned                                                   898|
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
=== options_morning_bot (PAPER) 2026-07-23T09:34:16.620106-04:00 ===

[Run context]
Paper auth OK — equity $135079.45, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 425 signal(s); top: ['S165:GOOGL', 'S165:GOOG', 'S165:AMZN', 'S165:ADI', 'S165:BKNG', 'S165:BLDR', 'S165:CCL', 'S165:CNC']
Paper lab: $134723 broker equity -> 140 bucket(s) ($500 virtual each, unlimited paper)
  [b8 GOOGL] ENTRY failed: {"code":40310000,"cost_basis":"71.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b36 GOOGL] ENTRY failed: {"code":40310000,"cost_basis":"71.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b64 GOOGL] ENTRY failed: {"code":40310000,"cost_basis":"71.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b92 GOOGL] ENTRY failed: {"code":40310000,"cost_basis":"71.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b120 GOOGL] ENTRY failed: {"code":40310000,"cost_basis":"71.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b8 GOOG] ENTRY failed: {"code":40310000,"cost_basis":"63.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b36 GOOG] ENTRY failed: {"code":40310000,"cost_basis":"63.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b64 GOOG] ENTRY failed: {"code":40310000,"cost_basis":"63.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b92 GOOG] ENTRY failed: {"code":40310000,"cost_basis":"63.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b120 GOOG] ENTRY failed: {"code":40310000,"cost_basis":"63.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b8 AMZN] ENTRY failed: {"code":40310000,"cost_basis":"70.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b36 AMZN] ENTRY failed: {"code":40310000,"cost_basis":"70.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b64 AMZN] ENTRY failed: {"code":40310000,"cost_basis":"70.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b92 AMZN] ENTRY failed: {"code":40310000,"cost_basis":"70.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b120 AMZN] ENTRY failed: {"code":40310000,"cost_basis":"70.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b8 META] ENTRY failed: {"code":40310000,"cost_basis":"31.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b36 META] ENTRY failed: {"code":40310000,"cost_basis":"31.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b64 META] ENTRY failed: {"code":40310000,"cost_basis":"31.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b92 META] ENTRY failed: {"code":40310000,"cost_basis":"31.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b120 META] ENTRY failed: {"code":40310000,"cost_basis":"31.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b8 QCOM] ENTRY failed: {"code":40310000,"cost_basis":"66.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b36 QCOM] ENTRY failed: {"code":40310000,"cost_basis":"66.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b64 QCOM] ENTRY failed: {"code":40310000,"cost_basis":"66.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b92 QCOM] ENTRY failed: {"code":40310000,"cost_basis":"66.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b120 QCOM] ENTRY failed: {"code":40310000,"cost_basis":"66.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b8 HOOD] ENTRY failed: {"code":40310000,"cost_basis":"59.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b36 HOOD] ENTRY failed: {"code":40310000,"cost_basis":"59.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b64 HOOD] ENTRY failed: {"code":40310000,"cost_basis":"59.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b92 HOOD] ENTRY failed: {"code":40310000,"cost_basis":"59.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b120 HOOD] ENTRY failed: {"code":40310000,"cost_basis":"59.01","message":"insufficient options buying power","options_buying_power":"0"}
```

---

## Run 20260723T133554Z

- UTC timestamp: `20260723T133554Z`
- GitHub run: [#4828](https://github.com/28twagg-ops/TradingBot/actions/runs/30011838329)
- Run id: `30011838329`
- Live bot: exit=`0`, duration=`215s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-23T09:25:54.569304-04:00","date":"2026-07-23","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":2.3,"phases_s":{"reconcile":2.07},"signals":0,"placed":0,"equity":133813.45,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4826","github_run_id":"30011102545","status":"ok"}
```

### Live bot full output

```text
13:35:54  INFO      Mode: morning_prep
13:35:55  INFO        [prep_positions] 5/5 (5 valid)
13:35:55  INFO      Fetching tickers (universe=both)...
13:35:55  INFO        S&P 500: 503
13:35:56  INFO        MidCap 400: 400
13:35:56  INFO        Total: 903 tickers
13:35:57  INFO        [prep_universe] 40/898 (40 valid)
13:35:58  INFO        [prep_universe] 80/898 (80 valid)
13:35:59  INFO        [prep_universe] 120/898 (120 valid)
13:36:01  INFO        [prep_universe] 160/898 (160 valid)
13:36:03  INFO        [prep_universe] 200/898 (199 valid)
13:36:10  INFO        [prep_universe] 240/898 (238 valid)
13:36:23  INFO        [prep_universe] 280/898 (278 valid)
13:36:33  INFO        [prep_universe] 320/898 (318 valid)
13:36:46  INFO        [prep_universe] 360/898 (358 valid)
13:36:59  INFO        [prep_universe] 400/898 (397 valid)
13:37:09  INFO        [prep_universe] 440/898 (437 valid)
13:37:22  INFO        [prep_universe] 480/898 (477 valid)
13:37:35  INFO        [prep_universe] 520/898 (517 valid)
13:37:45  INFO        [prep_universe] 560/898 (557 valid)
13:37:58  INFO        [prep_universe] 600/898 (597 valid)
13:38:11  INFO        [prep_universe] 640/898 (637 valid)
13:38:21  INFO        [prep_universe] 680/898 (677 valid)
13:38:34  INFO        [prep_universe] 720/898 (717 valid)
13:38:47  INFO        [prep_universe] 760/898 (757 valid)
13:38:58  INFO        [prep_universe] 800/898 (797 valid)
13:39:11  INFO        [prep_universe] 840/898 (836 valid)
13:39:21  INFO        [prep_universe] 880/898 (876 valid)
13:39:27  INFO        [prep_universe] 898/898 (894 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:35 UTC|
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
|  Open positions                                                       5|
|  Invested                                                       $382.03|
|  Open P&L                                                        $+0.94|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AEP      Pullback50      $97.48     $131.94  $133.44  +1.1%   $+1.09  |
|  C        Pullback50      $69.38     $132.61  $131.71  -0.7%   $-0.48  |
|  CARR     Pullback50      $97.38     $67.80   $68.80   +1.5%   $+1.42  |
|  CHD      Pullback50      $95.26     $97.17   $96.01   -1.2%   $-1.15  |
|  LNT      Pullback50      $22.52     $73.97   $74.12   +0.2%   $+0.05  |
+========================================================================+

+========================================================================+
|                            OPEN SELL ORDERS                            |
+========================================================================+
|  Count                                                                1|
|  TICKER    TYPE              QTY       LIMIT       STOP                |
+------------------------------------------------------------------------+
|  CARR      OrderType.STOP    1         None        67.75               |
+========================================================================+

+========================================================================+
|                              PREP SUMMARY                              |
+========================================================================+
|  Saved                                                              yes|
|  Exit candidates                                                      2|
|  Signal candidates                                                   49|
|  Universe scanned                                                   898|
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
=== options_morning_bot (PAPER) 2026-07-23T09:39:30.438419-04:00 ===

[Run context]
Paper auth OK — equity $135099.45, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 430 signal(s); top: ['S165:GOOGL', 'S165:GOOG', 'S165:AMZN', 'S165:ADI', 'S165:BKNG', 'S165:BLDR', 'S165:CCL', 'S165:CNC']
Paper lab: $135343 broker equity -> 140 bucket(s) ($500 virtual each, unlimited paper)
  [b8 GOOGL] ENTRY failed: {"code":40310000,"cost_basis":"39.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b36 GOOGL] ENTRY failed: {"code":40310000,"cost_basis":"39.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b64 GOOGL] ENTRY failed: {"code":40310000,"cost_basis":"39.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b92 GOOGL] ENTRY failed: {"code":40310000,"cost_basis":"39.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b120 GOOGL] ENTRY failed: {"code":40310000,"cost_basis":"39.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b8 GOOG] ENTRY failed: {"code":40310000,"cost_basis":"65.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b36 GOOG] ENTRY failed: {"code":40310000,"cost_basis":"65.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b64 GOOG] ENTRY failed: {"code":40310000,"cost_basis":"65.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b92 GOOG] ENTRY failed: {"code":40310000,"cost_basis":"65.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b120 GOOG] ENTRY failed: {"code":40310000,"cost_basis":"65.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b8 AMZN] ENTRY failed: {"code":40310000,"cost_basis":"43.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b36 AMZN] ENTRY failed: {"code":40310000,"cost_basis":"43.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b64 AMZN] ENTRY failed: {"code":40310000,"cost_basis":"43.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b92 AMZN] ENTRY failed: {"code":40310000,"cost_basis":"43.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b120 AMZN] ENTRY failed: {"code":40310000,"cost_basis":"43.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b8 CCL] ENTRY failed: {"code":40310000,"cost_basis":"5.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b36 CCL] ENTRY failed: {"code":40310000,"cost_basis":"5.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b64 CCL] ENTRY failed: {"code":40310000,"cost_basis":"5.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b92 CCL] ENTRY failed: {"code":40310000,"cost_basis":"5.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b120 CCL] ENTRY failed: {"code":40310000,"cost_basis":"5.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b8 KR] ENTRY failed: {"code":40310000,"cost_basis":"4.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b36 KR] ENTRY failed: {"code":40310000,"cost_basis":"4.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b64 KR] ENTRY failed: {"code":40310000,"cost_basis":"4.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b92 KR] ENTRY failed: {"code":40310000,"cost_basis":"4.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b120 KR] ENTRY failed: {"code":40310000,"cost_basis":"4.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b8 META] ENTRY failed: {"code":40310000,"cost_basis":"57.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b36 META] ENTRY failed: {"code":40310000,"cost_basis":"57.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b64 META] ENTRY failed: {"code":40310000,"cost_basis":"57.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b92 META] ENTRY failed: {"code":40310000,"cost_basis":"57.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b120 META] ENTRY failed: {"code":40310000,"cost_basis":"57.01","message":"insufficient options buying power","options_buying_power":"0"}
```

---

## Run 20260723T134053Z

- UTC timestamp: `20260723T134053Z`
- GitHub run: [#4829](https://github.com/28twagg-ops/TradingBot/actions/runs/30012212125)
- Run id: `30012212125`
- Live bot: exit=`0`, duration=`215s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-23T09:25:54.569304-04:00","date":"2026-07-23","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":2.3,"phases_s":{"reconcile":2.07},"signals":0,"placed":0,"equity":133813.45,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4826","github_run_id":"30011102545","status":"ok"}
```

### Live bot full output

```text
13:40:54  INFO      Mode: morning_prep
13:40:55  INFO        [prep_positions] 5/5 (5 valid)
13:40:55  INFO        Universe cache hit: 903 tickers (tickers_2026-07-23.json)
13:40:56  INFO        [prep_universe] 40/898 (40 valid)
13:40:58  INFO        [prep_universe] 80/898 (80 valid)
13:40:59  INFO        [prep_universe] 120/898 (120 valid)
13:41:00  INFO        [prep_universe] 160/898 (160 valid)
13:41:01  INFO        [prep_universe] 200/898 (199 valid)
13:41:11  INFO        [prep_universe] 240/898 (238 valid)
13:41:22  INFO        [prep_universe] 280/898 (278 valid)
13:41:35  INFO        [prep_universe] 320/898 (318 valid)
13:41:45  INFO        [prep_universe] 360/898 (358 valid)
13:41:59  INFO        [prep_universe] 400/898 (397 valid)
13:42:09  INFO        [prep_universe] 440/898 (437 valid)
13:42:22  INFO        [prep_universe] 480/898 (477 valid)
13:42:35  INFO        [prep_universe] 520/898 (517 valid)
13:42:46  INFO        [prep_universe] 560/898 (557 valid)
13:42:58  INFO        [prep_universe] 600/898 (597 valid)
13:43:10  INFO        [prep_universe] 640/898 (637 valid)
13:43:23  INFO        [prep_universe] 680/898 (677 valid)
13:43:34  INFO        [prep_universe] 720/898 (717 valid)
13:43:47  INFO        [prep_universe] 760/898 (757 valid)
13:43:57  INFO        [prep_universe] 800/898 (797 valid)
13:44:11  INFO        [prep_universe] 840/898 (836 valid)
13:44:21  INFO        [prep_universe] 880/898 (876 valid)
13:44:28  INFO        [prep_universe] 898/898 (894 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:40 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $481.86|
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
|  Open positions                                                       5|
|  Invested                                                       $382.63|
|  Open P&L                                                        $+1.54|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AEP      Pullback50      $97.42     $131.94  $133.35  +1.1%   $+1.03  |
|  C        Pullback50      $69.31     $132.61  $131.57  -0.8%   $-0.55  |
|  CARR     Pullback50      $98.00     $67.80   $69.24   +2.1%   $+2.04  |
|  CHD      Pullback50      $95.40     $97.17   $96.15   -1.0%   $-1.01  |
|  LNT      Pullback50      $22.50     $73.97   $74.05   +0.1%   $+0.03  |
+========================================================================+

+========================================================================+
|                            OPEN SELL ORDERS                            |
+========================================================================+
|  Count                                                                1|
|  TICKER    TYPE              QTY       LIMIT       STOP                |
+------------------------------------------------------------------------+
|  CARR      OrderType.STOP    1         None        67.75               |
+========================================================================+

+========================================================================+
|                              PREP SUMMARY                              |
+========================================================================+
|  Saved                                                              yes|
|  Exit candidates                                                      2|
|  Signal candidates                                                   47|
|  Universe scanned                                                   898|
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
=== options_morning_bot (PAPER) 2026-07-23T09:44:30.178155-04:00 ===

[Run context]
Paper auth OK — equity $135933.45, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 430 signal(s); top: ['S165:GOOGL', 'S165:GOOG', 'S165:AMZN', 'S165:ADI', 'S165:BKNG', 'S165:BLDR', 'S165:CCL', 'S165:CNC']
Paper lab: $135647 broker equity -> 140 bucket(s) ($500 virtual each, unlimited paper)
  [b8 GOOGL] ENTRY failed: {"code":40310000,"cost_basis":"53.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b36 GOOGL] ENTRY failed: {"code":40310000,"cost_basis":"53.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b64 GOOGL] ENTRY failed: {"code":40310000,"cost_basis":"53.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b92 GOOGL] ENTRY failed: {"code":40310000,"cost_basis":"53.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b120 GOOGL] ENTRY failed: {"code":40310000,"cost_basis":"53.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b8 GOOG] ENTRY failed: {"code":40310000,"cost_basis":"74.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b36 GOOG] ENTRY failed: {"code":40310000,"cost_basis":"74.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b64 GOOG] ENTRY failed: {"code":40310000,"cost_basis":"74.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b92 GOOG] ENTRY failed: {"code":40310000,"cost_basis":"74.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b120 GOOG] ENTRY failed: {"code":40310000,"cost_basis":"74.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b8 AMZN] ENTRY failed: {"code":40310000,"cost_basis":"43.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b36 AMZN] ENTRY failed: {"code":40310000,"cost_basis":"43.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b64 AMZN] ENTRY failed: {"code":40310000,"cost_basis":"43.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b92 AMZN] ENTRY failed: {"code":40310000,"cost_basis":"43.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b120 AMZN] ENTRY failed: {"code":40310000,"cost_basis":"43.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b8 CCL] ENTRY failed: {"code":40310000,"cost_basis":"9.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b36 CCL] ENTRY failed: {"code":40310000,"cost_basis":"9.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b64 CCL] ENTRY failed: {"code":40310000,"cost_basis":"9.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b92 CCL] ENTRY failed: {"code":40310000,"cost_basis":"9.01","message":"insufficient options buying power","options_buying_power":"0"}
  [b120 CCL] ENTRY failed: {"code":40310000,"cost_basis":"9.01","message":"insufficient options buying power","options_buying_power":"0"}
```

---

## Run 20260723T134603Z

- UTC timestamp: `20260723T134603Z`
- GitHub run: [#4830](https://github.com/28twagg-ops/TradingBot/actions/runs/30012587925)
- Run id: `30012587925`
- Live bot: exit=`0`, duration=`222s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-23T09:25:54.569304-04:00","date":"2026-07-23","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":2.3,"phases_s":{"reconcile":2.07},"signals":0,"placed":0,"equity":133813.45,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4826","github_run_id":"30011102545","status":"ok"}
```

### Live bot full output

```text
13:46:04  INFO      Mode: morning_scan
13:46:06  INFO        [positions] 5/5 (5 valid)
13:46:06  INFO        SELL MARKET [urgent] CHD closed
13:46:08  INFO        TX logged: SELL CHD  P&L -1.23%
13:46:09  INFO        SELL MARKET [urgent] C closed
13:46:11  INFO        TX logged: SELL C  P&L -0.75%
13:46:11  INFO        Universe cache hit: 903 tickers (tickers_2026-07-23.json)
13:46:12  INFO        [universe] 40/900 (40 valid)
13:46:14  INFO        [universe] 80/900 (80 valid)
13:46:16  INFO        [universe] 120/900 (120 valid)
13:46:17  INFO        [universe] 160/900 (160 valid)
13:46:19  INFO        [universe] 200/900 (199 valid)
13:46:24  INFO        [universe] 240/900 (238 valid)
13:46:37  INFO        [universe] 280/900 (278 valid)
13:46:48  INFO        [universe] 320/900 (318 valid)
13:47:02  INFO        [universe] 360/900 (358 valid)
13:47:12  INFO        [universe] 400/900 (397 valid)
13:47:25  INFO        [universe] 440/900 (437 valid)
13:47:36  INFO        [universe] 480/900 (477 valid)
13:47:49  INFO        [universe] 520/900 (517 valid)
13:48:00  INFO        [universe] 560/900 (557 valid)
13:48:13  INFO        [universe] 600/900 (597 valid)
13:48:24  INFO        [universe] 640/900 (637 valid)
13:48:37  INFO        [universe] 680/900 (677 valid)
13:48:48  INFO        [universe] 720/900 (717 valid)
13:49:02  INFO        [universe] 760/900 (757 valid)
13:49:13  INFO        [universe] 800/900 (797 valid)
13:49:26  INFO        [universe] 840/900 (836 valid)
13:49:36  INFO        [universe] 880/900 (876 valid)
13:49:43  INFO        [universe] 900/900 (896 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_SCAN|
|  Time                                                         13:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $481.59|
+========================================================================+

+========================================================================+
|                   RUBBER BAND BOT v8  --  DAILY SCAN                   |
+========================================================================+
|  Mode                                                      *** LIVE ***|
|  Date                                                        2026-07-23|
|  Universe                                                          both|
|  Mon~  Jul: 52wkLow + Pullback50 (display only — schedule not enforced)|
|  Disabled                GapDown, VolumeSpike (see DISABLED_STRATEGIES)|
|  Regime                                                            BULL|
|  Exit                                      midline / stop-0.5% / 3d max|
+========================================================================+

+========================================================================+
|                                ACCOUNT                                 |
+========================================================================+
|  Equity                                                         $481.59|
|  Cash                                                            $99.23|
|  Reserve                                          $24.08  (always kept)|
|  Available                                     $75.15  (for new trades)|
|  Trade size             $96.32  (20% per signal — all strategies equal)|
+========================================================================+

+========================================================================+
|                           HOLDINGS  (5 open)                           |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AEP      Pullback50      $97.34     $131.94  $133.24  +1.0%   $+0.95  |
|  C        Pullback50      $69.34     $132.61  $131.62  -0.7%   $-0.52  |
|  CARR     Pullback50      $98.02     $67.80   $69.25   +2.1%   $+2.06  |
|  CHD      Pullback50      $95.22     $97.17   $95.97   -1.2%   $-1.19  |
|  LNT      Pullback50      $22.45     $73.97   $73.88   -0.1%   $-0.03  |
|                                                                        |
|  Total invested                                                 $382.36|
|  Total open P&L                                                  $+1.27|
|  Buys today: 0  |  entry cap: 0  |  max open: 5                        |
+========================================================================+

+========================================================================+
|                               PLAN CACHE                               |
+========================================================================+
|  Mode                                                           morning|
|  File                                      logs/plans/morning_plan.json|
|  Use cached plan                                  no (stale (20160.6m))|
+========================================================================+

+========================================================================+
|          EXIT EVALUATION  (EOD -- midline + stop + max-hold)           |
+========================================================================+
|  CHD  P&L -1.2%  $-1.19                         EXIT: stop_loss (-1.2%)|
|  C  P&L -0.7%  $-0.52                           EXIT: stop_loss (-0.7%)|
|  LNT  P&L -0.1%  $-0.03                                            HOLD|
|  AEP  P&L +1.0%  $+0.95                                            HOLD|
|  CARR  P&L +2.1%  $+2.06                                           HOLD|
+========================================================================+

+========================================================================+
|                           EXIT EVAL SUMMARY                            |
+========================================================================+
|  Exit eval    attempted 2 | filled 2 | partial 0 | pending 0 | failed 0|
|  Other skips     already logged today 0  |  no price data 0  |  holds 3|
|  Stop-loss breaches                                                   2|
|  CHD                                         -1.23%  (threshold -0.50%)|
|  C                                           -0.75%  (threshold -0.50%)|
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
|                         SIGNALS FOUND  --  46                          |
+========================================================================+
|  TICKER   STRATEGY        TIER   PRICE    RSI    VOL_Z   TRIGGER       |
+------------------------------------------------------------------------+
|  BIIB     Pullback50      eq     $197.49  38.2   -1.78   50MA bounce (-|
|  CL       Pullback50      eq     $90.09   38.0   -2.58   50MA bounce (-|
|  FIX      Pullback50      eq     $1854.~  58.9   -1.43   50MA bounce (+|
|  DTE      Pullback50      eq     $147.70  37.3   -2.89   50MA bounce (+|
|  EXR      Pullback50      eq     $145.52  42.3   -2.33   50MA bounce (+|
|  FAST     Pullback50      eq     $45.48   31.8   -2.15   50MA bounce (-|
|  FFIV     Pullback50      eq     $400.46  45.9   -2.59   50MA bounce (+|
|  F        Pullback50      eq     $14.21   65.8   -3.40   50MA bounce (-|
|  BEN      Pullback50      eq     $32.37   33.1   -3.26   50MA bounce (-|
|  FCX      Pullback50      eq     $63.75   56.2   -2.74   50MA bounce (-|
|  GRMN     Pullback50      eq     $239.47  49.4   -1.89   50MA bounce (+|
|  FTV      Pullback50      eq     $60.93   42.3   -2.95   50MA bounce (+|
|  IRM      Pullback50      eq     $125.38  73.6   -2.86   50MA bounce (-|
|  INVH     Pullback50      eq     $29.70   40.7   -2.08   50MA bounce (+|
|  MRNA     Pullback50      eq     $57.77   18.1   -1.71   50MA bounce (+|
|  NVDA     Pullback50      eq     $209.53  63.0   -3.41   50MA bounce (+|
|  NI       Pullback50      eq     $46.46   39.7   -2.53   50MA bounce (-|
|  PPG      Pullback50      eq     $114.90  31.7   -2.21   50MA bounce (+|
|  PSA      Pullback50      eq     $314.91  37.5   -1.42   50MA bounce (+|
|  ROK      Pullback50      eq     $458.99  43.5   -0.99   50MA bounce (-|
|  LUV      Pullback50      eq     $45.75   30.8   -2.36   50MA bounce (+|
|  TTWO     Pullback50      eq     $232.50  27.2   -1.58   50MA bounce (-|13:49:44  INFO        place_all_stops: checking 3 positions...
13:49:44  INFO        STOP skipped AEP: fractional (0.7305 shares) — software exit will handle it
13:49:45  INFO        STOP already live CARR @ $67.75
13:49:45  INFO        STOP skipped LNT: fractional (0.3038 shares) — software exit will handle it
13:49:45  INFO        Daily log -> logs/daily/2026-07-23.md
13:49:45  INFO        Dashboard written → logs/dashboard.md

|  TPR      Pullback50      eq     $142.74  47.6   -2.05   50MA bounce (+|
|  STLD     Pullback50      eq     $244.24  73.0   -2.80   50MA bounce (-|
|  WEC      Pullback50      eq     $113.28  32.6   -3.04   50MA bounce (-|
|  XEL      Pullback50      eq     $80.02   40.3   -2.96   50MA bounce (+|
|  ALGM     Pullback50      eq     $50.98   42.7   -1.22   50MA bounce (-|
|  AEIS     Pullback50      eq     $324.25  55.0   -0.78   50MA bounce (-|
|  ALLY     Pullback50      eq     $44.05   43.1   -2.18   50MA bounce (-|
|  AXTA     Pullback50      eq     $32.04   24.6   -2.40   50MA bounce (+|
|  BYD      Pullback50      eq     $85.86   42.7   -3.09   50MA bounce (+|
|  CW       Pullback50      eq     $741.10  44.5   -1.62   50MA bounce (-|
|  DTM      Pullback50      eq     $143.55  47.4   -3.34   50MA bounce (-|
|  FHI      Pullback50      eq     $56.99   51.6   -2.89   50MA bounce (-|
|  IESC     Pullback50      eq     $681.12  55.2   -0.92   50MA bounce (-|
|  ITT      Pullback50      eq     $193.98  62.4   -2.66   50MA bounce (+|
|  LSCC     Pullback50      eq     $138.05  51.5   -1.92   50MA bounce (-|
|  MKSI     Pullback50      eq     $345.50  41.7   -2.13   50MA bounce (-|
|  NWE      Pullback50      eq     $71.68   51.5   -1.18   50MA bounce (+|
|  P        Pullback50      eq     $76.26   55.4   -2.24   50MA bounce (-|
|  PEN      Pullback50      eq     $316.48  41.5   -1.88   50MA bounce (-|
|  RBC      Pullback50      eq     $596.09  45.2   -1.85   50MA bounce (-|
|  SLAB     Pullback50      eq     $217.32  40.0   -0.95   50MA bounce (-|
|  SPXC     Pullback50      eq     $221.50  44.1   -0.58   50MA bounce (-|
|  TLN      Pullback50      eq     $375.73  54.4   -2.04   50MA bounce (-|
|  TOL      Pullback50      eq     $146.50  36.0   -2.67   50MA bounce (+|
|                                                                        |
+========================================================================+

+========================================================================+
|                              ENTRY ORDERS                              |
+========================================================================+
|  Skipped                                  no entry slots (max_trades=0)|
+========================================================================+

+========================================================================+
|                            SESSION SUMMARY                             |
+========================================================================+
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Strategy   52wkLow + Pullback50 (display only — schedule not enforced)|
|  Scanned                                                            896|
|  Signals                                                             46|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  0 unconfirmed|
|  Exits                                                                2|
|  Open pos                                                             3|
|  Equity                                                         $481.25|
|  Cash                                                           $263.71|
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
=== options_morning_bot (PAPER) 2026-07-23T09:49:47.306879-04:00 ===

[Run context]
Paper auth OK — equity $135155.45, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163] …
```

---
