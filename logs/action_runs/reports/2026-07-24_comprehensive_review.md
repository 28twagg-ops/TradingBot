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
