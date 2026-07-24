# Daily Comprehensive Action Review — 2026-07-24

_Auto-generated from GitHub Actions run output. This document appends every run for the day._

## Run 20260724T010117Z

- UTC timestamp: `20260724T010117Z`
- GitHub run: [#4961](https://github.com/28twagg-ops/TradingBot/actions/runs/30057798244)
- Run id: `30057798244`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`9s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-23T21:01:21.430720-04:00","date":"2026-07-23","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.8,"phases_s":{"reconcile":1.5},"signals":0,"placed":0,"equity":134054.43,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4961","github_run_id":"30057798244","status":"ok"}
```

### Live bot full output

```text
01:01:19  INFO      Mode: summary
01:01:19  INFO        Daily log -> logs/daily/2026-07-24.md
01:01:19  INFO        Daily log reconciled -> logs/daily/2026-07-24.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         01:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.49|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $482.49|
|  Cash                                                            $71.19|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $411.30|
|  Open P&L                                                        $+3.76|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (5 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AEP      Pullback50      $97.50     $131.94  $133.46  +1.2%   $+1.11  |
|  CARR     Pullback50      $97.87     $67.80   $69.15   +2.0%   $+1.91  |
|  CI       Pullback50      $96.80     $285.49  $286.29  +0.3%   $+0.27  |
|  DTE      Pullback50      $96.52     $147.63  $148.13  +0.3%   $+0.33  |
|  LNT      Pullback50      $22.61     $73.97   $74.42   +0.6%   $+0.14  |
|                                                                        |
|  Total invested                                                 $411.30|
|  Total open P&L                                                  $+3.76|
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
|  2026-07-23  SELL  FIX  Pullback50  $96.39  P&L $+0.32                 |
|  2026-07-23  SELL  C  Pullback50  $69.34  P&L $-0.52                   |
|  2026-07-23  SELL  CHD  Pullback50  $95.22  P&L $-1.19                 |
|  2026-07-22  SELL  AVGO  Pullback50  $96.29  P&L $-0.14                |
|  2026-07-22  SELL  TPR  Pullback50  $97.94  P&L $+1.64                 |
|  2026-07-22  SELL  BIIB  Pullback50  $95.71  P&L $-0.49                |
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
=== options_morning_bot (PAPER) 2026-07-23T21:01:21.430720-04:00 ===

[Run context]
After hours (21:01 ET) — exit summary only.
Paper auth OK — equity $134054.43, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $134,054.43                             |
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
elapsed=1.8s reconcile=1.5s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.8s. run=#4961 https://github.com/28twagg-ops/TradingBot/actions/runs/30057798244
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-23_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-23_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-23_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-23_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 2.7% (22/802)
# Options signal frequency

_Generated 2026-07-23T21:01:27.628877_

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
equity=482.49 router=CONFIRMED leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---

## Run 20260724T015229Z

- UTC timestamp: `20260724T015229Z`
- GitHub run: [#4962](https://github.com/28twagg-ops/TradingBot/actions/runs/30060104218)
- Run id: `30060104218`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`7s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-23T21:52:32.634580-04:00","date":"2026-07-23","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":2.9,"phases_s":{"reconcile":2.59},"signals":0,"placed":0,"equity":134226.43,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4962","github_run_id":"30060104218","status":"ok"}
```

### Live bot full output

```text
01:52:30  INFO      Mode: summary
01:52:31  INFO        Daily log -> logs/daily/2026-07-24.md
01:52:31  INFO        Daily log reconciled -> logs/daily/2026-07-24.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         01:52 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.49|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $482.49|
|  Cash                                                            $71.19|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $411.30|
|  Open P&L                                                        $+3.76|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (5 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AEP      Pullback50      $97.50     $131.94  $133.46  +1.2%   $+1.11  |
|  CARR     Pullback50      $97.87     $67.80   $69.15   +2.0%   $+1.91  |
|  CI       Pullback50      $96.80     $285.49  $286.29  +0.3%   $+0.27  |
|  DTE      Pullback50      $96.52     $147.63  $148.13  +0.3%   $+0.33  |
|  LNT      Pullback50      $22.61     $73.97   $74.42   +0.6%   $+0.14  |
|                                                                        |
|  Total invested                                                 $411.30|
|  Total open P&L                                                  $+3.76|
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
|  2026-07-23  SELL  FIX  Pullback50  $96.39  P&L $+0.32                 |
|  2026-07-23  SELL  C  Pullback50  $69.34  P&L $-0.52                   |
|  2026-07-23  SELL  CHD  Pullback50  $95.22  P&L $-1.19                 |
|  2026-07-22  SELL  AVGO  Pullback50  $96.29  P&L $-0.14                |
|  2026-07-22  SELL  TPR  Pullback50  $97.94  P&L $+1.64                 |
|  2026-07-22  SELL  BIIB  Pullback50  $95.71  P&L $-0.49                |
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
=== options_morning_bot (PAPER) 2026-07-23T21:52:32.634580-04:00 ===

[Run context]
After hours (21:52 ET) — exit summary only.
Paper auth OK — equity $134226.43, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $134,226.43                             |
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
elapsed=2.9s reconcile=2.59s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=2.9s. run=#4962 https://github.com/28twagg-ops/TradingBot/actions/runs/30060104218
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-23_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-23_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-23_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-23_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 2.7% (22/802)
# Options signal frequency

_Generated 2026-07-23T21:52:37.714650_

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
equity=482.49 router=CONFIRMED leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---

## Run 20260724T045525Z

- UTC timestamp: `20260724T045525Z`
- GitHub run: [#4963](https://github.com/28twagg-ops/TradingBot/actions/runs/30068016557)
- Run id: `30068016557`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`8s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-24T00:55:29.881497-04:00","date":"2026-07-24","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":2.2,"phases_s":{"reconcile":1.8},"signals":0,"placed":0,"equity":132915.03,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4963","github_run_id":"30068016557","status":"ok"}
```

### Live bot full output

```text
04:55:26  INFO      Mode: summary
04:55:27  INFO        Daily log -> logs/daily/2026-07-24.md
04:55:27  INFO        Daily log reconciled -> logs/daily/2026-07-24.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         04:55 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.49|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $482.49|
|  Cash                                                            $71.19|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $411.30|
|  Open P&L                                                        $+3.76|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (5 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AEP      Pullback50      $97.50     $131.94  $133.46  +1.2%   $+1.11  |
|  CARR     Pullback50      $97.87     $67.80   $69.15   +2.0%   $+1.91  |
|  CI       Pullback50      $96.80     $285.49  $286.29  +0.3%   $+0.27  |
|  DTE      Pullback50      $96.52     $147.63  $148.13  +0.3%   $+0.33  |
|  LNT      Pullback50      $22.61     $73.97   $74.42   +0.6%   $+0.14  |
|                                                                        |
|  Total invested                                                 $411.30|
|  Total open P&L                                                  $+3.76|
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
|  2026-07-23  SELL  FIX  Pullback50  $96.39  P&L $+0.32                 |
|  2026-07-23  SELL  C  Pullback50  $69.34  P&L $-0.52                   |
|  2026-07-23  SELL  CHD  Pullback50  $95.22  P&L $-1.19                 |
|  2026-07-22  SELL  AVGO  Pullback50  $96.29  P&L $-0.14                |
|  2026-07-22  SELL  TPR  Pullback50  $97.94  P&L $+1.64                 |
|  2026-07-22  SELL  BIIB  Pullback50  $95.71  P&L $-0.49                |
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
=== options_morning_bot (PAPER) 2026-07-24T00:55:29.881497-04:00 ===

[Run context]
After hours (00:55 ET) — exit summary only.
Paper auth OK — equity $132915.03, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $132,915.03                             |
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
Full detail: logs/options_trial/runs/2026-07-24.log
elapsed=2.2s reconcile=1.8s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=2.2s. run=#4963 https://github.com/28twagg-ops/TradingBot/actions/runs/30068016557
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-24_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-24_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-24_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-24_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 2.7% (22/802)
# Options signal frequency

_Generated 2026-07-24T00:55:36.006772_

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
| S163 | 130 | 2 |
| S164 | 166 | 3 |
| S165 | 1608 | 16 |
| S166 | 75 | 1 |
| S167 | 160 | 3 |
| S168 | 95 | 2 |
| S173 | 1911 | 17 |
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
| 2026-07-24 |   30 |   42 |   50 |   15 |   40 |   20 |   40 |    0 |   237 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-07-24
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
equity=482.49 router=CONFIRMED leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---

## Run 20260724T130051Z

- UTC timestamp: `20260724T130051Z`
- GitHub run: [#4964](https://github.com/28twagg-ops/TradingBot/actions/runs/30095157424)
- Run id: `30095157424`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`8s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-24T09:00:56.039748-04:00","date":"2026-07-24","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":3.1,"phases_s":{"reconcile":2.66},"signals":0,"placed":0,"equity":133335.55,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4964","github_run_id":"30095157424","status":"ok"}
```

### Live bot full output

```text
13:00:53  INFO      Mode: summary
13:00:54  INFO        Daily log -> logs/daily/2026-07-24.md
13:00:54  INFO        Daily log reconciled -> logs/daily/2026-07-24.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:00 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $483.00|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $483.00|
|  Cash                                                            $71.19|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $411.81|
|  Open P&L                                                        $+4.26|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (5 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AEP      Pullback50      $97.50     $131.94  $133.46  +1.2%   $+1.11  |
|  CARR     Pullback50      $98.14     $67.80   $69.34   +2.3%   $+2.18  |
|  CI       Pullback50      $97.04     $285.49  $287.00  +0.5%   $+0.51  |
|  DTE      Pullback50      $96.52     $147.63  $148.13  +0.3%   $+0.33  |
|  LNT      Pullback50      $22.61     $73.97   $74.41   +0.6%   $+0.13  |
|                                                                        |
|  Total invested                                                 $411.81|
|  Total open P&L                                                  $+4.26|
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
|  2026-07-23  SELL  FIX  Pullback50  $96.39  P&L $+0.32                 |
|  2026-07-23  SELL  C  Pullback50  $69.34  P&L $-0.52                   |
|  2026-07-23  SELL  CHD  Pullback50  $95.22  P&L $-1.19                 |
|  2026-07-22  SELL  AVGO  Pullback50  $96.29  P&L $-0.14                |
|  2026-07-22  SELL  TPR  Pullback50  $97.94  P&L $+1.64                 |
|  2026-07-22  SELL  BIIB  Pullback50  $95.71  P&L $-0.49                |
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
=== options_morning_bot (PAPER) 2026-07-24T09:00:56.039748-04:00 ===

[Run context]
After hours (09:00 ET) — exit summary only.
Paper auth OK — equity $133335.55, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $133,335.55                             |
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
Full detail: logs/options_trial/runs/2026-07-24.log
elapsed=3.1s reconcile=2.66s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=3.1s. run=#4964 https://github.com/28twagg-ops/TradingBot/actions/runs/30095157424
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-24_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-24_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-24_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-24_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 2.7% (22/802)
# Options signal frequency

_Generated 2026-07-24T09:01:02.233652_

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
| S163 | 130 | 2 |
| S164 | 166 | 3 |
| S165 | 1608 | 16 |
| S166 | 75 | 1 |
| S167 | 160 | 3 |
| S168 | 95 | 2 |
| S173 | 1911 | 17 |
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
| 2026-07-24 |   30 |   42 |   50 |   15 |   40 |   20 |   40 |    0 |   237 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-07-24
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
equity=483.0 router=CONFIRMED leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---

## Run 20260724T130538Z

- UTC timestamp: `20260724T130538Z`
- GitHub run: [#4965](https://github.com/28twagg-ops/TradingBot/actions/runs/30095489780)
- Run id: `30095489780`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`8s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-24T09:05:41.355948-04:00","date":"2026-07-24","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":2.1,"phases_s":{"reconcile":1.8},"signals":0,"placed":0,"equity":133323.03,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4965","github_run_id":"30095489780","status":"ok"}
```

### Live bot full output

```text
13:05:39  INFO      Mode: summary
13:05:39  INFO        Daily log -> logs/daily/2026-07-24.md
13:05:39  INFO        Daily log reconciled -> logs/daily/2026-07-24.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:05 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $483.00|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $483.00|
|  Cash                                                            $71.19|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $411.81|
|  Open P&L                                                        $+4.26|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (5 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AEP      Pullback50      $97.50     $131.94  $133.46  +1.2%   $+1.11  |
|  CARR     Pullback50      $98.14     $67.80   $69.34   +2.3%   $+2.18  |
|  CI       Pullback50      $97.04     $285.49  $287.00  +0.5%   $+0.51  |
|  DTE      Pullback50      $96.52     $147.63  $148.13  +0.3%   $+0.33  |
|  LNT      Pullback50      $22.61     $73.97   $74.41   +0.6%   $+0.13  |
|                                                                        |
|  Total invested                                                 $411.81|
|  Total open P&L                                                  $+4.26|
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
|  2026-07-23  SELL  FIX  Pullback50  $96.39  P&L $+0.32                 |
|  2026-07-23  SELL  C  Pullback50  $69.34  P&L $-0.52                   |
|  2026-07-23  SELL  CHD  Pullback50  $95.22  P&L $-1.19                 |
|  2026-07-22  SELL  AVGO  Pullback50  $96.29  P&L $-0.14                |
|  2026-07-22  SELL  TPR  Pullback50  $97.94  P&L $+1.64                 |
|  2026-07-22  SELL  BIIB  Pullback50  $95.71  P&L $-0.49                |
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
=== options_morning_bot (PAPER) 2026-07-24T09:05:41.355948-04:00 ===

[Run context]
After hours (09:05 ET) — exit summary only.
Paper auth OK — equity $133323.03, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $133,323.03                             |
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
Full detail: logs/options_trial/runs/2026-07-24.log
elapsed=2.1s reconcile=1.8s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=2.1s. run=#4965 https://github.com/28twagg-ops/TradingBot/actions/runs/30095489780
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-24_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-24_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-24_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-24_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 2.7% (22/802)
# Options signal frequency

_Generated 2026-07-24T09:05:47.351791_

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
| S163 | 130 | 2 |
| S164 | 166 | 3 |
| S165 | 1608 | 16 |
| S166 | 75 | 1 |
| S167 | 160 | 3 |
| S168 | 95 | 2 |
| S173 | 1911 | 17 |
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
| 2026-07-24 |   30 |   42 |   50 |   15 |   40 |   20 |   40 |    0 |   237 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-07-24
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
equity=483.0 router=CONFIRMED leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---

## Run 20260724T131036Z

- UTC timestamp: `20260724T131036Z`
- GitHub run: [#4966](https://github.com/28twagg-ops/TradingBot/actions/runs/30095814527)
- Run id: `30095814527`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`7s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-24T09:10:39.535295-04:00","date":"2026-07-24","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":2.0,"phases_s":{"reconcile":1.38},"signals":0,"placed":0,"equity":133047.03,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4966","github_run_id":"30095814527","status":"ok"}
```

### Live bot full output

```text
13:10:37  INFO      Mode: summary
13:10:37  INFO        Daily log -> logs/daily/2026-07-24.md
13:10:37  INFO        Daily log reconciled -> logs/daily/2026-07-24.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $483.00|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $483.00|
|  Cash                                                            $71.19|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $411.81|
|  Open P&L                                                        $+4.26|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (5 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AEP      Pullback50      $97.50     $131.94  $133.46  +1.2%   $+1.11  |
|  CARR     Pullback50      $98.14     $67.80   $69.34   +2.3%   $+2.18  |
|  CI       Pullback50      $97.04     $285.49  $287.00  +0.5%   $+0.51  |
|  DTE      Pullback50      $96.52     $147.63  $148.13  +0.3%   $+0.33  |
|  LNT      Pullback50      $22.61     $73.97   $74.41   +0.6%   $+0.13  |
|                                                                        |
|  Total invested                                                 $411.81|
|  Total open P&L                                                  $+4.26|
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
|  2026-07-23  SELL  FIX  Pullback50  $96.39  P&L $+0.32                 |
|  2026-07-23  SELL  C  Pullback50  $69.34  P&L $-0.52                   |
|  2026-07-23  SELL  CHD  Pullback50  $95.22  P&L $-1.19                 |
|  2026-07-22  SELL  AVGO  Pullback50  $96.29  P&L $-0.14                |
|  2026-07-22  SELL  TPR  Pullback50  $97.94  P&L $+1.64                 |
|  2026-07-22  SELL  BIIB  Pullback50  $95.71  P&L $-0.49                |
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
=== options_morning_bot (PAPER) 2026-07-24T09:10:39.535295-04:00 ===

[Run context]
After hours (09:10 ET) — exit summary only.
Paper auth OK — equity $133047.03, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $133,047.03                             |
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
Full detail: logs/options_trial/runs/2026-07-24.log
elapsed=2.0s reconcile=1.38s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=2.0s. run=#4966 https://github.com/28twagg-ops/TradingBot/actions/runs/30095814527
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-24_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-24_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-24_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-24_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 2.7% (22/802)
# Options signal frequency

_Generated 2026-07-24T09:10:45.417219_

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
| S163 | 130 | 2 |
| S164 | 166 | 3 |
| S165 | 1608 | 16 |
| S166 | 75 | 1 |
| S167 | 160 | 3 |
| S168 | 95 | 2 |
| S173 | 1911 | 17 |
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
| 2026-07-24 |   30 |   42 |   50 |   15 |   40 |   20 |   40 |    0 |   237 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-07-24
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
equity=483.0 router=CONFIRMED leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---

## Run 20260724T131537Z

- UTC timestamp: `20260724T131537Z`
- GitHub run: [#4967](https://github.com/28twagg-ops/TradingBot/actions/runs/30096141464)
- Run id: `30096141464`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`7s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-24T09:15:40.424045-04:00","date":"2026-07-24","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.6,"phases_s":{"reconcile":1.36},"signals":0,"placed":0,"equity":133191.03,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4967","github_run_id":"30096141464","status":"ok"}
```

### Live bot full output

```text
13:15:38  INFO      Mode: summary
13:15:38  INFO        Daily log -> logs/daily/2026-07-24.md
13:15:38  INFO        Daily log reconciled -> logs/daily/2026-07-24.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:15 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $483.00|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $483.00|
|  Cash                                                            $71.19|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $411.81|
|  Open P&L                                                        $+4.26|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (5 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AEP      Pullback50      $97.50     $131.94  $133.46  +1.2%   $+1.11  |
|  CARR     Pullback50      $98.14     $67.80   $69.34   +2.3%   $+2.18  |
|  CI       Pullback50      $97.04     $285.49  $287.00  +0.5%   $+0.51  |
|  DTE      Pullback50      $96.52     $147.63  $148.13  +0.3%   $+0.33  |
|  LNT      Pullback50      $22.61     $73.97   $74.41   +0.6%   $+0.13  |
|                                                                        |
|  Total invested                                                 $411.81|
|  Total open P&L                                                  $+4.26|
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
|  2026-07-23  SELL  FIX  Pullback50  $96.39  P&L $+0.32                 |
|  2026-07-23  SELL  C  Pullback50  $69.34  P&L $-0.52                   |
|  2026-07-23  SELL  CHD  Pullback50  $95.22  P&L $-1.19                 |
|  2026-07-22  SELL  AVGO  Pullback50  $96.29  P&L $-0.14                |
|  2026-07-22  SELL  TPR  Pullback50  $97.94  P&L $+1.64                 |
|  2026-07-22  SELL  BIIB  Pullback50  $95.71  P&L $-0.49                |
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
=== options_morning_bot (PAPER) 2026-07-24T09:15:40.424045-04:00 ===

[Run context]
After hours (09:15 ET) — exit summary only.
Paper auth OK — equity $133191.03, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $133,191.03                             |
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
Full detail: logs/options_trial/runs/2026-07-24.log
elapsed=1.6s reconcile=1.36s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.6s. run=#4967 https://github.com/28twagg-ops/TradingBot/actions/runs/30096141464
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-24_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-24_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-24_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-24_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 2.7% (22/802)
# Options signal frequency

_Generated 2026-07-24T09:15:45.872995_

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
| S163 | 130 | 2 |
| S164 | 166 | 3 |
| S165 | 1608 | 16 |
| S166 | 75 | 1 |
| S167 | 160 | 3 |
| S168 | 95 | 2 |
| S173 | 1911 | 17 |
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
| 2026-07-24 |   30 |   42 |   50 |   15 |   40 |   20 |   40 |    0 |   237 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-07-24
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
equity=483.0 router=CONFIRMED leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---

## Run 20260724T132038Z

- UTC timestamp: `20260724T132038Z`
- GitHub run: [#4968](https://github.com/28twagg-ops/TradingBot/actions/runs/30096461501)
- Run id: `30096461501`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`6s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-24T09:20:41.499714-04:00","date":"2026-07-24","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.9,"phases_s":{"reconcile":1.55},"signals":0,"placed":0,"equity":133287.03,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4968","github_run_id":"30096461501","status":"ok"}
```

### Live bot full output

```text
13:20:39  INFO      Mode: summary
13:20:39  INFO        Daily log -> logs/daily/2026-07-24.md
13:20:39  INFO        Daily log reconciled -> logs/daily/2026-07-24.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $483.00|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $483.00|
|  Cash                                                            $71.19|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $411.81|
|  Open P&L                                                        $+4.26|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (5 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AEP      Pullback50      $97.50     $131.94  $133.46  +1.2%   $+1.11  |
|  CARR     Pullback50      $98.14     $67.80   $69.34   +2.3%   $+2.18  |
|  CI       Pullback50      $97.04     $285.49  $287.00  +0.5%   $+0.51  |
|  DTE      Pullback50      $96.52     $147.63  $148.13  +0.3%   $+0.33  |
|  LNT      Pullback50      $22.61     $73.97   $74.41   +0.6%   $+0.13  |
|                                                                        |
|  Total invested                                                 $411.81|
|  Total open P&L                                                  $+4.26|
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
|  2026-07-23  SELL  FIX  Pullback50  $96.39  P&L $+0.32                 |
|  2026-07-23  SELL  C  Pullback50  $69.34  P&L $-0.52                   |
|  2026-07-23  SELL  CHD  Pullback50  $95.22  P&L $-1.19                 |
|  2026-07-22  SELL  AVGO  Pullback50  $96.29  P&L $-0.14                |
|  2026-07-22  SELL  TPR  Pullback50  $97.94  P&L $+1.64                 |
|  2026-07-22  SELL  BIIB  Pullback50  $95.71  P&L $-0.49                |
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
=== options_morning_bot (PAPER) 2026-07-24T09:20:41.499714-04:00 ===

[Run context]
After hours (09:20 ET) — exit summary only.
Paper auth OK — equity $133287.03, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $133,287.03                             |
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
Full detail: logs/options_trial/runs/2026-07-24.log
elapsed=1.9s reconcile=1.55s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.9s. run=#4968 https://github.com/28twagg-ops/TradingBot/actions/runs/30096461501
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-24_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-24_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-24_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-24_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 2.7% (22/802)
# Options signal frequency

_Generated 2026-07-24T09:20:46.413840_

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
| S163 | 130 | 2 |
| S164 | 166 | 3 |
| S165 | 1608 | 16 |
| S166 | 75 | 1 |
| S167 | 160 | 3 |
| S168 | 95 | 2 |
| S173 | 1911 | 17 |
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
| 2026-07-24 |   30 |   42 |   50 |   15 |   40 |   20 |   40 |    0 |   237 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-07-24
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
equity=483.0 router=CONFIRMED leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---

## Run 20260724T132535Z

- UTC timestamp: `20260724T132535Z`
- GitHub run: [#4969](https://github.com/28twagg-ops/TradingBot/actions/runs/30096786125)
- Run id: `30096786125`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`8s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-24T09:25:39.472905-04:00","date":"2026-07-24","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.8,"phases_s":{"reconcile":1.49},"signals":0,"placed":0,"equity":133270.47,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4969","github_run_id":"30096786125","status":"ok"}
```

### Live bot full output

```text
13:25:37  INFO      Mode: summary
13:25:37  INFO        Daily log -> logs/daily/2026-07-24.md
13:25:37  INFO        Daily log reconciled -> logs/daily/2026-07-24.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:25 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $483.00|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $483.00|
|  Cash                                                            $71.19|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $411.81|
|  Open P&L                                                        $+4.26|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (5 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AEP      Pullback50      $97.50     $131.94  $133.46  +1.2%   $+1.11  |
|  CARR     Pullback50      $98.14     $67.80   $69.34   +2.3%   $+2.18  |
|  CI       Pullback50      $97.04     $285.49  $287.00  +0.5%   $+0.51  |
|  DTE      Pullback50      $96.52     $147.63  $148.13  +0.3%   $+0.33  |
|  LNT      Pullback50      $22.61     $73.97   $74.41   +0.6%   $+0.13  |
|                                                                        |
|  Total invested                                                 $411.81|
|  Total open P&L                                                  $+4.26|
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
|  2026-07-23  SELL  FIX  Pullback50  $96.39  P&L $+0.32                 |
|  2026-07-23  SELL  C  Pullback50  $69.34  P&L $-0.52                   |
|  2026-07-23  SELL  CHD  Pullback50  $95.22  P&L $-1.19                 |
|  2026-07-22  SELL  AVGO  Pullback50  $96.29  P&L $-0.14                |
|  2026-07-22  SELL  TPR  Pullback50  $97.94  P&L $+1.64                 |
|  2026-07-22  SELL  BIIB  Pullback50  $95.71  P&L $-0.49                |
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
=== options_morning_bot (PAPER) 2026-07-24T09:25:39.472905-04:00 ===

[Run context]
After hours (09:25 ET) — exit summary only.
Paper auth OK — equity $133270.47, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $133,270.47                             |
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
Full detail: logs/options_trial/runs/2026-07-24.log
elapsed=1.8s reconcile=1.49s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.8s. run=#4969 https://github.com/28twagg-ops/TradingBot/actions/runs/30096786125
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-24_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-24_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-24_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-24_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 2.7% (22/802)
# Options signal frequency

_Generated 2026-07-24T09:25:45.212982_

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
| S163 | 130 | 2 |
| S164 | 166 | 3 |
| S165 | 1608 | 16 |
| S166 | 75 | 1 |
| S167 | 160 | 3 |
| S168 | 95 | 2 |
| S173 | 1911 | 17 |
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
| 2026-07-24 |   30 |   42 |   50 |   15 |   40 |   20 |   40 |    0 |   237 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-07-24
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
equity=483.0 router=CONFIRMED leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---

## Run 20260724T133039Z

- UTC timestamp: `20260724T133039Z`
- GitHub run: [#4970](https://github.com/28twagg-ops/TradingBot/actions/runs/30097110244)
- Run id: `30097110244`
- Live bot: exit=`0`, duration=`215s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-24T09:25:39.472905-04:00","date":"2026-07-24","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.8,"phases_s":{"reconcile":1.49},"signals":0,"placed":0,"equity":133270.47,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4969","github_run_id":"30096786125","status":"ok"}
```

### Live bot full output

```text
13:30:40  INFO      Mode: morning_prep
13:30:41  INFO        [prep_positions] 5/5 (5 valid)
13:30:41  INFO      Fetching tickers (universe=both)...
13:30:42  INFO        S&P 500: 503
13:30:42  INFO        MidCap 400: 400
13:30:42  INFO        Total: 903 tickers
13:30:43  INFO        [prep_universe] 40/898 (40 valid)
13:30:44  INFO        [prep_universe] 80/898 (80 valid)
13:30:46  INFO        [prep_universe] 120/898 (120 valid)
13:30:47  INFO        [prep_universe] 160/898 (160 valid)
13:30:48  INFO        [prep_universe] 200/898 (199 valid)
13:30:55  INFO        [prep_universe] 240/898 (238 valid)
13:31:08  INFO        [prep_universe] 280/898 (278 valid)
13:31:19  INFO        [prep_universe] 320/898 (318 valid)
13:31:31  INFO        [prep_universe] 360/898 (358 valid)
13:31:44  INFO        [prep_universe] 400/898 (397 valid)
13:31:54  INFO        [prep_universe] 440/898 (437 valid)
13:32:07  INFO        [prep_universe] 480/898 (477 valid)
13:32:21  INFO        [prep_universe] 520/898 (517 valid)
13:32:30  INFO        [prep_universe] 560/898 (557 valid)
13:32:43  INFO        [prep_universe] 600/898 (597 valid)
13:32:57  INFO        [prep_universe] 640/898 (637 valid)
13:33:07  INFO        [prep_universe] 680/898 (677 valid)
13:33:20  INFO        [prep_universe] 720/898 (717 valid)
13:33:30  INFO        [prep_universe] 760/898 (757 valid)
13:33:43  INFO        [prep_universe] 800/898 (797 valid)
13:33:56  INFO        [prep_universe] 840/898 (836 valid)
13:34:06  INFO        [prep_universe] 880/898 (876 valid)
13:34:13  INFO        [prep_universe] 898/898 (894 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:30 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $484.91|
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
|  Invested                                                       $413.82|
|  Open P&L                                                        $+6.28|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AEP      Pullback50      $99.02     $131.94  $135.54  +2.7%   $+2.63  |
|  CARR     Pullback50      $97.20     $67.80   $68.67   +1.3%   $+1.24  |
|  CI       Pullback50      $97.67     $285.49  $288.87  +1.2%   $+1.14  |
|  DTE      Pullback50      $97.21     $147.63  $149.19  +1.1%   $+1.02  |
|  LNT      Pullback50      $22.72     $73.97   $74.77   +1.1%   $+0.24  |
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
|  Signal candidates                                                   31|
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
=== options_morning_bot (PAPER) 2026-07-24T09:34:15.609336-04:00 ===

[Run context]
Paper auth OK — equity $133047.03, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 143 signal(s); top: ['S165:AXP', 'S165:CHRW', 'S165:CHTR', 'S165:COHR', 'S165:CMCSA', 'S165:DECK', 'S165:EBAY', 'S165:HIG']
Paper lab: $132839 broker equity -> 140 bucket(s) ($500 virtual each, unlimited paper)
```

---

## Run 20260724T133556Z

- UTC timestamp: `20260724T133556Z`
- GitHub run: [#4971](https://github.com/28twagg-ops/TradingBot/actions/runs/30097456917)
- Run id: `30097456917`
- Live bot: exit=`0`, duration=`213s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-24T09:25:39.472905-04:00","date":"2026-07-24","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.8,"phases_s":{"reconcile":1.49},"signals":0,"placed":0,"equity":133270.47,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4969","github_run_id":"30096786125","status":"ok"}
```

### Live bot full output

```text
13:35:57  INFO      Mode: morning_prep
13:35:57  INFO        [prep_positions] 5/5 (5 valid)
13:35:57  INFO      Fetching tickers (universe=both)...
13:35:57  INFO        S&P 500: 503
13:35:58  INFO        MidCap 400: 400
13:35:58  INFO        Total: 903 tickers
13:35:58  INFO        [prep_universe] 40/898 (40 valid)
13:36:00  INFO        [prep_universe] 80/898 (80 valid)
13:36:01  INFO        [prep_universe] 120/898 (120 valid)
13:36:02  INFO        [prep_universe] 160/898 (160 valid)
13:36:03  INFO        [prep_universe] 200/898 (199 valid)
13:36:13  INFO        [prep_universe] 240/898 (238 valid)
13:36:23  INFO        [prep_universe] 280/898 (278 valid)
13:36:36  INFO        [prep_universe] 320/898 (318 valid)
13:36:49  INFO        [prep_universe] 360/898 (358 valid)
13:36:59  INFO        [prep_universe] 400/898 (397 valid)
13:37:12  INFO        [prep_universe] 440/898 (437 valid)
13:37:25  INFO        [prep_universe] 480/898 (477 valid)
13:37:38  INFO        [prep_universe] 520/898 (517 valid)
13:37:48  INFO        [prep_universe] 560/898 (557 valid)
13:38:01  INFO        [prep_universe] 600/898 (597 valid)
13:38:13  INFO        [prep_universe] 640/898 (637 valid)
13:38:23  INFO        [prep_universe] 680/898 (677 valid)
13:38:36  INFO        [prep_universe] 720/898 (717 valid)
13:38:49  INFO        [prep_universe] 760/898 (757 valid)
13:38:59  INFO        [prep_universe] 800/898 (797 valid)
13:39:12  INFO        [prep_universe] 840/898 (836 valid)
13:39:25  INFO        [prep_universe] 880/898 (876 valid)
13:39:28  INFO        [prep_universe] 898/898 (894 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:35 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.41|
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
|  Invested                                                       $411.19|
|  Open P&L                                                        $+3.65|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AEP      Pullback50      $98.94     $131.94  $135.43  +2.6%   $+2.55  |
|  CARR     Pullback50      $96.10     $67.80   $67.90   +0.1%   $+0.14  |
|  CI       Pullback50      $96.73     $285.49  $286.07  +0.2%   $+0.20  |
|  DTE      Pullback50      $96.71     $147.63  $148.43  +0.5%   $+0.52  |
|  LNT      Pullback50      $22.71     $73.97   $74.74   +1.0%   $+0.24  |
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
|  Signal candidates                                                   32|
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
=== options_morning_bot (PAPER) 2026-07-24T09:39:31.292509-04:00 ===

[Run context]
Paper auth OK — equity $131269.43, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 143 signal(s); top: ['S165:AXP', 'S165:CHRW', 'S165:CHTR', 'S165:COHR', 'S165:CMCSA', 'S165:DECK', 'S165:EBAY', 'S165:HIG']
Paper lab: $131179 broker equity -> 140 bucket(s) ($500 virtual each, unlimited paper)
```

---

## Run 20260724T134602Z

- UTC timestamp: `20260724T134602Z`
- GitHub run: [#4974](https://github.com/28twagg-ops/TradingBot/actions/runs/30098142749)
- Run id: `30098142749`
- Live bot: exit=`0`, duration=`246s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-24T09:25:39.472905-04:00","date":"2026-07-24","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.8,"phases_s":{"reconcile":1.49},"signals":0,"placed":0,"equity":133270.47,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4969","github_run_id":"30096786125","status":"ok"}
```

### Live bot full output

```text
13:46:03  INFO      Mode: morning_scan
13:46:04  INFO        [positions] 5/5 (5 valid)
13:46:05  INFO        SELL LIMIT AEP  qty=0.730548271  limit=$135.72  id=2c428197-f883-4693-ac89-57c7c4a83ebc
13:46:35  INFO        SELL LIMIT filled AEP (confirmed by position check)
13:46:35  INFO        TX logged: SELL AEP  P&L 3.07%
13:46:35  INFO        Universe cache hit: 903 tickers (tickers_2026-07-24.json)
13:46:36  INFO        [universe] 40/899 (40 valid)
13:46:38  INFO        [universe] 80/899 (80 valid)
13:46:39  INFO        [universe] 120/899 (120 valid)
13:46:41  INFO        [universe] 160/899 (160 valid)
13:46:42  INFO        [universe] 200/899 (199 valid)
13:46:49  INFO        [universe] 240/899 (238 valid)
13:47:00  INFO        [universe] 280/899 (278 valid)
13:47:13  INFO        [universe] 320/899 (318 valid)
13:47:27  INFO        [universe] 360/899 (358 valid)
13:47:37  INFO        [universe] 400/899 (397 valid)
13:47:50  INFO        [universe] 440/899 (437 valid)
13:48:01  INFO        [universe] 480/899 (477 valid)
13:48:14  INFO        [universe] 520/899 (517 valid)
13:48:24  INFO        [universe] 560/899 (557 valid)
13:48:38  INFO        [universe] 600/899 (597 valid)
13:48:48  INFO        [universe] 640/899 (637 valid)
13:49:01  INFO        [universe] 680/899 (677 valid)
13:49:12  INFO        [universe] 720/899 (717 valid)
13:49:25  INFO        [universe] 760/899 (757 valid)
13:49:36  INFO        [universe] 800/899 (797 valid)
13:49:49  INFO        [universe] 840/899 (836 valid)
13:50:02  INFO        [universe] 880/899 (876 valid)
13:50:06  INFO        [universe] 899/899 (895 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_SCAN|
|  Time                                                         13:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $484.90|
+========================================================================+

+========================================================================+
|                   RUBBER BAND BOT v8  --  DAILY SCAN                   |
+========================================================================+
|  Mode                                                      *** LIVE ***|
|  Date                                                        2026-07-24|
|  Universe                                                          both|
|  Mon~  Jul: 52wkLow + Pullback50 (display only — schedule not enforced)|
|  Disabled                GapDown, VolumeSpike (see DISABLED_STRATEGIES)|
|  Regime                                                            BULL|
|  Exit                                      midline / stop-0.5% / 3d max|
+========================================================================+

+========================================================================+
|                                ACCOUNT                                 |
+========================================================================+
|  Equity                                                         $484.90|
|  Cash                                                            $71.19|
|  Reserve                                          $24.25  (always kept)|
|  Available                                     $46.94  (for new trades)|
|  Trade size             $96.98  (20% per signal — all strategies equal)|
+========================================================================+

+========================================================================+
|                           HOLDINGS  (5 open)                           |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AEP      Pullback50      $99.35     $131.94  $135.99  +3.1%   $+2.96  |
|  CARR     Pullback50      $97.22     $67.80   $68.69   +1.3%   $+1.26  |
|  CI       Pullback50      $97.06     $285.49  $287.06  +0.5%   $+0.53  |
|  DTE      Pullback50      $97.27     $147.63  $149.29  +1.1%   $+1.08  |
|  LNT      Pullback50      $22.81     $73.97   $75.07   +1.5%   $+0.34  |
|                                                                        |
|  Total invested                                                 $413.71|
|  Total open P&L                                                  $+6.17|
|  Buys today: 0  |  entry cap: 0  |  max open: 5                        |
+========================================================================+

+========================================================================+
|                               PLAN CACHE                               |
+========================================================================+
|  Mode                                                           morning|
|  File                                      logs/plans/morning_plan.json|
|  Use cached plan                                  no (stale (21600.6m))|
+========================================================================+

+========================================================================+
|          EXIT EVALUATION  (EOD -- midline + stop + max-hold)           |
+========================================================================+
|  CI  P&L +0.5%  $+0.53                                             HOLD|
|  DTE  P&L +1.1%  $+1.08                                            HOLD|
|  CARR  P&L +1.3%  $+1.26                                           HOLD|
|  LNT  P&L +1.5%  $+0.34                                            HOLD|
|  AEP  P&L +3.1%  $+2.96                           EXIT: midline (+3.1%)|
+========================================================================+

+========================================================================+
|                           EXIT EVAL SUMMARY                            |
+========================================================================+
|  Exit eval    attempted 1 | filled 1 | partial 0 | pending 0 | failed 0|
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
|                         SIGNALS FOUND  --  34                          |
+========================================================================+
|  TICKER   STRATEGY        TIER   PRICE    RSI    VOL_Z   TRIGGER       |
+------------------------------------------------------------------------+
|  ABNB     Pullback50      eq     $138.99  35.2   -2.53   50MA bounce (-|
|  MO       Pullback50      eq     $72.56   52.9   -2.36   50MA bounce (+|
|  BRK-B    Pullback50      eq     $491.76  30.2   -2.71   50MA bounce (+|
|  CHD      Pullback50      eq     $97.03   48.8   -3.09   50MA bounce (+|
|  C        Pullback50      eq     $133.18  33.1   -1.99   50MA bounce (-|
|  FIX      Pullback50      eq     $1839.~  54.1   -1.45   50MA bounce (-|
|  CL       Pullback50      eq     $90.62   43.0   -2.72   50MA bounce (+|
|  DAL      Pullback50      eq     $83.63   27.8   -2.76   50MA bounce (+|
|  F        Pullback50      eq     $14.37   60.7   -3.34   50MA bounce (-|
|  BEN      Pullback50      eq     $32.50   31.1   -3.37   50MA bounce (+|
|  GEV      Pullback50      eq     $1030.~  34.3   -2.67   50MA bounce (-|
|  INVH     Pullback50      eq     $29.66   45.6   -2.14   50MA bounce (+|
|  MGM      Pullback50      eq     $45.22   32.0   -2.13   50MA bounce (+|
|  NWSA     Pullback50      eq     $26.65   50.1   -1.47   50MA bounce (+|
|  NWS      Pullback50      eq     $30.06   50.3   -1.57   50MA bounce (-|
|  NVDA     Pullback50      eq     $207.93  60.7   -3.41   50MA bounce (-|
|  PPG      Pullback50      eq     $115.31  35.4   -1.96   50MA bounce (+|
|  PFG      Pullback50      eq     $107.67  32.6   -2.29   50MA bounce (+|
|  ROK      Pullback50      eq     $464.15  39.8   -1.03   50MA bounce (+|
|  STX      Pullback50      eq     $890.17  52.1   -2.57   50MA bounce (+|
|  VZ       Pullback50      eq     $45.01   74.5   -1.66   50MA bounce (-|
|  ALK      Pullback50      eq     $46.03   36.4   -2.22   50MA bounce (+|
|  ALLY     Pullback50      eq     $43.99   36.6   -2.19   50MA bounce (-|
|  ARW      Pullback50      eq     $214.88  67.5   -2.71   50MA bounce (-|13:50:07  INFO        place_all_stops: checking 4 positions...
13:50:08  INFO        STOP-MARKET placed CARR  qty=1 (pos=1.4154)  stop=$67.46  id=49c14145-ffef-43e7-b48f-db08a6931612
13:50:08  INFO        STOP skipped CI: fractional (0.3381 shares) — software exit will handle it
13:50:08  INFO        STOP skipped DTE: fractional (0.6516 shares) — software exit will handle it
13:50:08  INFO        STOP skipped LNT: fractional (0.3038 shares) — software exit will handle it
13:50:08  INFO        Daily log -> logs/daily/2026-07-24.md
13:50:08  INFO        Dashboard written → logs/dashboard.md

|  COKE     Pullback50      eq     $180.01  39.3   -1.84   50MA bounce (+|
|  IRT      Pullback50      eq     $16.55   38.8   -1.48   50MA bounce (-|
|  KRYS     Pullback50      eq     $328.78  29.1   -0.56   50MA bounce (-|
|  NEU      Pullback50      eq     $773.89  41.4   -2.80   50MA bounce (+|
|  RBC      Pullback50      eq     $599.10  43.9   -1.84   50MA bounce (+|
|  SPXC     Pullback50      eq     $223.15  41.0   -0.56   50MA bounce (+|
|  SSD      Pullback50      eq     $191.60  42.1   -2.09   50MA bounce (+|
|  TLN      Pullback50      eq     $379.94  51.0   -1.95   50MA bounce (+|
|  TCBI     Pullback50      eq     $100.07  38.3   -1.90   50MA bounce (-|
|  TTC      Pullback50      eq     $93.09   39.0   -2.64   50MA bounce (+|
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
|  Scanned                                                            895|
|  Signals                                                             34|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  0 unconfirmed|
|  Exits                                                                1|
|  Open pos                                                             4|
|  Equity                                                         $485.40|
|  Cash                                                           $170.49|
+========================================================================+
```

### Options bot full output

```text

## Run 20260724T135053Z

- UTC timestamp: `20260724T135053Z`
- GitHub run: [#4975](https://github.com/28twagg-ops/TradingBot/actions/runs/30098477556)
- Run id: `30098477556`
- Live bot: exit=`0`, duration=`239s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-24T09:25:39.472905-04:00","date":"2026-07-24","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.8,"phases_s":{"reconcile":1.49},"signals":0,"placed":0,"equity":133270.47,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4969","github_run_id":"30096786125","status":"ok"}
```

### Live bot full output

```text
13:50:54  INFO      Mode: morning_scan
13:50:55  INFO        [positions] 4/4 (4 valid)
13:50:55  INFO        Universe cache hit: 903 tickers (tickers_2026-07-24.json)
13:50:56  INFO        [universe] 40/899 (40 valid)
13:50:58  INFO        [universe] 80/899 (80 valid)
13:50:59  INFO        [universe] 120/899 (120 valid)
13:51:00  INFO        [universe] 160/899 (160 valid)
13:51:08  INFO        [universe] 200/899 (199 valid)
13:51:21  INFO        [universe] 240/899 (238 valid)
13:51:31  INFO        [universe] 280/899 (278 valid)
13:51:44  INFO        [universe] 320/899 (318 valid)
13:51:57  INFO        [universe] 360/899 (358 valid)
13:52:07  INFO        [universe] 400/899 (397 valid)
13:52:20  INFO        [universe] 440/899 (437 valid)
13:52:33  INFO        [universe] 480/899 (477 valid)
13:52:44  INFO        [universe] 520/899 (517 valid)
13:52:57  INFO        [universe] 560/899 (557 valid)
13:53:07  INFO        [universe] 600/899 (597 valid)
13:53:20  INFO        [universe] 640/899 (637 valid)
13:53:33  INFO        [universe] 680/899 (677 valid)
13:53:43  INFO        [universe] 720/899 (717 valid)
13:53:56  INFO        [universe] 760/899 (757 valid)
13:54:09  INFO        [universe] 800/899 (797 valid)
13:54:20  INFO        [universe] 840/899 (836 valid)
13:54:33  INFO        [universe] 880/899 (876 valid)
13:54:37  INFO        [universe] 899/899 (895 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_SCAN|
|  Time                                                         13:50 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $485.17|
+========================================================================+

+========================================================================+
|                   RUBBER BAND BOT v8  --  DAILY SCAN                   |
+========================================================================+
|  Mode                                                      *** LIVE ***|
|  Date                                                        2026-07-24|
|  Universe                                                          both|
|  Mon~  Jul: 52wkLow + Pullback50 (display only — schedule not enforced)|
|  Disabled                GapDown, VolumeSpike (see DISABLED_STRATEGIES)|
|  Regime                                                            BULL|
|  Exit                                      midline / stop-0.5% / 3d max|
+========================================================================+

+========================================================================+
|                                ACCOUNT                                 |
+========================================================================+
|  Equity                                                         $485.17|
|  Cash                                                           $170.49|
|  Reserve                                          $24.26  (always kept)|
|  Available                                    $146.23  (for new trades)|
|  Trade size             $97.03  (20% per signal — all strategies equal)|
+========================================================================+

+========================================================================+
|                           HOLDINGS  (4 open)                           |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CARR     Pullback50      $97.43     $67.80   $68.84   +1.5%   $+1.47  |
|  CI       Pullback50      $97.06     $285.49  $287.07  +0.6%   $+0.53  |
|  DTE      Pullback50      $97.35     $147.63  $149.41  +1.2%   $+1.16  |
|  LNT      Pullback50      $22.84     $73.97   $75.16   +1.6%   $+0.36  |
|                                                                        |
|  Total invested                                                 $314.68|
|  Total open P&L                                                  $+3.53|
|  Buys today: 0  |  entry cap: 1  |  max open: 5                        |
+========================================================================+

+========================================================================+
|                               PLAN CACHE                               |
+========================================================================+
|  Mode                                                           morning|
|  File                                      logs/plans/morning_plan.json|
|  Use cached plan                                  no (stale (21605.4m))|
+========================================================================+

+========================================================================+
|          EXIT EVALUATION  (EOD -- midline + stop + max-hold)           |
+========================================================================+
|  CI  P&L +0.6%  $+0.53                                             HOLD|
|  DTE  P&L +1.2%  $+1.16                                            HOLD|
|  CARR  P&L +1.5%  $+1.47                                           HOLD|
|  LNT  P&L +1.6%  $+0.36                                            HOLD|
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
|                         SIGNALS FOUND  --  29                          |
+========================================================================+
|  TICKER   STRATEGY        TIER   PRICE    RSI    VOL_Z   TRIGGER       |
+------------------------------------------------------------------------+
|  ABNB     Pullback50      eq     $139.65  36.6   -2.52   50MA bounce (+|
|  MO       Pullback50      eq     $72.51   52.6   -2.34   50MA bounce (+|
|  BRK-B    Pullback50      eq     $492.16  30.9   -2.69   50MA bounce (+|
|  CHD      Pullback50      eq     $96.92   48.5   -3.08   50MA bounce (+|
|  CL       Pullback50      eq     $90.52   42.7   -2.70   50MA bounce (-|
|  DAL      Pullback50      eq     $83.69   28.0   -2.75   50MA bounce (+|
|  F        Pullback50      eq     $14.34   60.2   -3.31   50MA bounce (-|
|  HUBB     Pullback50      eq     $489.86  46.7   -2.26   50MA bounce (+|
|  JCI      Pullback50      eq     $143.20  51.4   -1.72   50MA bounce (+|
|  INVH     Pullback50      eq     $29.70   46.1   -2.13   50MA bounce (+|
|  MGM      Pullback50      eq     $45.24   32.3   -2.12   50MA bounce (+|
|  NWSA     Pullback50      eq     $26.64   50.0   -1.47   50MA bounce (+|
|  NWS      Pullback50      eq     $30.05   50.2   -1.57   50MA bounce (-|
|  NVDA     Pullback50      eq     $207.52  60.3   -3.39   50MA bounce (-|
|  PPG      Pullback50      eq     $114.76  34.2   -1.92   50MA bounce (-|
|  STX      Pullback50      eq     $882.26  51.3   -2.55   50MA bounce (-|
|  SLB      Pullback50      eq     $51.38   78.1   -1.76   50MA bounce (-|
|  VRSN     Pullback50      eq     $277.26  67.0   -1.94   50MA bounce (-|
|  ALLY     Pullback50      eq     $43.93   36.2   -2.18   50MA bounce (-|
|  ARW      Pullback50      eq     $214.61  67.1   -2.70   50MA bounce (-|
|  CW       Pullback50      eq     $750.72  36.2   -1.65   50MA bounce (+|
|  H        Pullback50      eq     $187.05  41.3   -2.37   50MA bounce (-|
|  IRT      Pullback50      eq     $16.57   39.2   -1.48   50MA bounce (-|
|  NEU      Pullback50      eq     $772.79  40.9   -2.78   50MA bounce (+|
|  OZK      Pullback50      eq     $50.33   54.0   -2.45   50MA bounce (+|
|  RBC      Pullback50      eq     $598.44  43.4   -1.83   50MA bounce (+|13:54:38  INFO        BUY  ABNB  $97.03  [Pullback50]  id=84120657-833a-4425-819c-04657eb40acd
13:54:51  INFO        place_all_stops: checking 5 positions...
13:54:51  INFO        STOP skipped ABNB: fractional (0.6947 shares) — software exit will handle it
13:54:51  INFO        STOP already live CARR @ $67.46
13:54:51  INFO        STOP skipped CI: fractional (0.3381 shares) — software exit will handle it
13:54:51  INFO        STOP skipped DTE: fractional (0.6516 shares) — software exit will handle it
13:54:51  INFO        STOP skipped LNT: fractional (0.3038 shares) — software exit will handle it
13:54:52  INFO        Daily log -> logs/daily/2026-07-24.md
13:54:52  INFO        Dashboard written → logs/dashboard.md

|  SSD      Pullback50      eq     $190.40  40.2   -2.08   50MA bounce (-|
|  SPXC     Pullback50      eq     $221.70  39.3   -0.56   50MA bounce (-|
|  TTC      Pullback50      eq     $93.14   39.2   -2.63   50MA bounce (+|
|                                                                        |
+========================================================================+

+========================================================================+
|                              ENTRY ORDERS                              |
+========================================================================+
|    ENTER [eq] ABNB  Pullback50                                   $97.03|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    SKIP [eq] MO  Pullback50                                       cap 5|
|    SKIP [eq] BRK-B  Pullback50                                    cap 5|
|    SKIP [eq] CHD  Pullback50                                      cap 5|
|    SKIP [eq] CL  Pullback50                                       cap 5|
|    SKIP [eq] DAL  Pullback50                                      cap 5|
|    SKIP [eq] F  Pullback50                                        cap 5|
|    SKIP [eq] HUBB  Pullback50                                     cap 5|
|    SKIP [eq] JCI  Pullback50                                      cap 5|
|    SKIP [eq] INVH  Pullback50                                     cap 5|
|    SKIP [eq] MGM  Pullback50                                      cap 5|
|    SKIP [eq] NWSA  Pullback50                                     cap 5|
|    SKIP [eq] NWS  Pullback50                                      cap 5|
|    SKIP [eq] NVDA  Pullback50                                     cap 5|
|    SKIP [eq] PPG  Pullback50                                      cap 5|
|    SKIP [eq] STX  Pullback50                                      cap 5|
|    SKIP [eq] SLB  Pullback50                                      cap 5|
|    SKIP [eq] VRSN  Pullback50                                     cap 5|
|    SKIP [eq] ALLY  Pullback50                                     cap 5|
|    SKIP [eq] ARW  Pullback50                                      cap 5|
|    SKIP [eq] CW  Pullback50                                       cap 5|
|    SKIP [eq] H  Pullback50                                        cap 5|
|    SKIP [eq] IRT  Pullback50                                      cap 5|
|    SKIP [eq] NEU  Pullback50                                      cap 5|
|    SKIP [eq] OZK  Pullback50                                      cap 5|
|    SKIP [eq] RBC  Pullback50                                      cap 5|
|    SKIP [eq] SSD  Pullback50                                      cap 5|
|    SKIP [eq] SPXC  Pullback50                                     cap 5|
|    SKIP [eq] TTC  Pullback50                                      cap 5|

+========================================================================+
|                         BUY FILL CONFIRMATION                          |
+========================================================================+
|  Pending submits                                                      1|
+------------------------------------------------------------------------+
|  ABNB                                                 still unconfirmed|
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
|  Scanned                                                            895|
|  Signals                                                             29|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  1 unconfirmed|
|  Exits                                                                0|
|  Open pos                                                             5|
|  Equity                                                         $485.55|
|  Cash                                                            $73.47|
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=0 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=5
  zombies_flagged=0
options_reconcile: done
Layout: controlled:140:c000_s173_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:140:c000_s173_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      140
=== options_morning_bot (PAPER) 2026-07-24T09:54:54.005304-04:00 ===

[Run context]
Paper auth OK — equity $130399.53, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-07-24 09:54:56,813 INFO   EXIT [b132|c132_s164_w1_0928_1005_r5|S164] stop_loss (-88.9%) SELL 1 MRVL260724C00222500 @<= 0.02

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163] …
```

---
