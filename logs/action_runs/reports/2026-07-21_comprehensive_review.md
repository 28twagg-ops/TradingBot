# Daily Comprehensive Action Review — 2026-07-21

_Auto-generated from GitHub Actions run output. This document appends every run for the day._

## Run 20260721T010113Z

- UTC timestamp: `20260721T010113Z`
- GitHub run: [#4533](https://github.com/28twagg-ops/TradingBot/actions/runs/29791940719)
- Run id: `29791940719`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`7s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T21:01:17.626825-04:00","date":"2026-07-20","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":2.3,"phases_s":{"reconcile":1.9},"signals":0,"placed":0,"equity":130883.73,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":20,"filled_today":20,"unattributed_contracts":0,"top_signals":[],"github_run":"4533","github_run_id":"29791940719","status":"ok"}
```

### Live bot full output

```text
01:01:14  INFO      Mode: summary
01:01:15  INFO        Daily log -> logs/daily/2026-07-21.md
01:01:15  INFO        Daily log reconciled -> logs/daily/2026-07-21.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         01:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.46|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $482.46|
|  Cash                                                           $216.83|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $265.63|
|  Open P&L                                                        $+0.69|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (3 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  MAA      Pullback50      $96.41     $133.63  $133.71  +0.1%   $+0.06  |
|  TPR      Pullback50      $96.54     $140.84  $141.12  +0.2%   $+0.19  |
|  WMB      Pullback50      $72.67     $74.35   $74.80   +0.6%   $+0.43  |
|                                                                        |
|  Total invested                                                 $265.63|
|  Total open P&L                                                  $+0.69|
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
|  2026-07-20  SELL  TJX  Pullback50  $96.31  P&L $+0.06                 |
|  2026-07-20  SELL  OXY  Pullback50  $96.34  P&L $-0.01                 |
|  2026-07-20  SELL  COP  Pullback50  $89.26  P&L $+0.88                 |
|  2026-07-20  SELL  CI  Pullback50  $87.88  P&L $-0.52                  |
|  2026-07-20  SELL  KO  Pullback50  $14.60  P&L $-0.08                  |
|  2026-07-20  SELL  CNP  Pullback50  $9.78  P&L $-0.06                  |
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
=== options_morning_bot (PAPER) 2026-07-20T21:01:17.626825-04:00 ===

[Run context]
After hours (21:01 ET) — exit summary only.
Paper auth OK — equity $130883.73, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $130,883.73                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    20                                      |
|  Orders filled today (ledger)  20                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=516  buckets=49  win=37%                             |
|  Returns   avg=+10.2%  med=-28.8%  p10=-75.5%  p90=+97.5%              |
|  Realized  $+4,588.77                                                  |
|  Raw incl dropped  trades=630  real=$+3,090.58                         |
|  Today     trades=19  avg=+81.9%  med=+82.5%  real=$+981.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b51  c051_s164_w4_1120_  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  c091_s167_w4_1120_  3  67% +142.7 +197.0 +247.0 $   +282         |
|  b31  c031_s173_w4_1120_  2 100% +145.5 +145.5 +175.8 $   +192         |
|  b28  c028_s173_w1_0928_ 17  76% +49.5 +80.0 +102.0 $   +448           |
|  b92  c092_s165_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s165_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s165_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 41 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s164_w2_1005_ 23   4% -55.2 -72.1 -98.5 $   -863       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=2.3s reconcile=1.9s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=2.3s. run=#4533 https://github.com/28twagg-ops/TradingBot/actions/runs/29791940719
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.csv
Summary: 14 buckets closed trades, $+981.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 3.5% (22/630)
# Options signal frequency

_Generated 2026-07-20T21:01:22.960612_

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

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S164 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S165 | 14 | 7 | 2.0 | ~19 active signal-days |
| S166 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S167 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S168 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 0 | 0 |
| S164 | 0 | 0 |
| S165 | 1309 | 14 |
| S166 | 0 | 0 |
| S167 | 0 | 0 |
| S168 | 0 | 0 |
| S173 | 1636 | 17 |
| S174 | 843 | 7 |

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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-07-20
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |    27 | WARN | <<<
| Missing exit records (post) |    27 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |   274 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=482.46 router=PENDING leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---

## Run 20260721T015023Z

- UTC timestamp: `20260721T015023Z`
- GitHub run: [#4534](https://github.com/28twagg-ops/TradingBot/actions/runs/29794181818)
- Run id: `29794181818`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`8s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T21:50:27.615509-04:00","date":"2026-07-20","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":2.3,"phases_s":{"reconcile":1.94},"signals":0,"placed":0,"equity":130979.73,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":20,"filled_today":20,"unattributed_contracts":0,"top_signals":[],"github_run":"4534","github_run_id":"29794181818","status":"ok"}
```

### Live bot full output

```text
01:50:24  INFO      Mode: summary
01:50:25  INFO        Daily log -> logs/daily/2026-07-21.md
01:50:25  INFO        Daily log reconciled -> logs/daily/2026-07-21.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         01:50 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.46|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $482.46|
|  Cash                                                           $216.83|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $265.63|
|  Open P&L                                                        $+0.69|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (3 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  MAA      Pullback50      $96.41     $133.63  $133.71  +0.1%   $+0.06  |
|  TPR      Pullback50      $96.54     $140.84  $141.12  +0.2%   $+0.19  |
|  WMB      Pullback50      $72.67     $74.35   $74.80   +0.6%   $+0.43  |
|                                                                        |
|  Total invested                                                 $265.63|
|  Total open P&L                                                  $+0.69|
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
|  2026-07-20  SELL  TJX  Pullback50  $96.31  P&L $+0.06                 |
|  2026-07-20  SELL  OXY  Pullback50  $96.34  P&L $-0.01                 |
|  2026-07-20  SELL  COP  Pullback50  $89.26  P&L $+0.88                 |
|  2026-07-20  SELL  CI  Pullback50  $87.88  P&L $-0.52                  |
|  2026-07-20  SELL  KO  Pullback50  $14.60  P&L $-0.08                  |
|  2026-07-20  SELL  CNP  Pullback50  $9.78  P&L $-0.06                  |
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
=== options_morning_bot (PAPER) 2026-07-20T21:50:27.615509-04:00 ===

[Run context]
After hours (21:50 ET) — exit summary only.
Paper auth OK — equity $130979.73, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $130,979.73                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    20                                      |
|  Orders filled today (ledger)  20                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=213  buckets=22  win=34%                             |
|  Returns   avg=+2.1%  med=-33.3%  p10=-64.9%  p90=+86.7%               |
|  Realized  $+5,522.13                                                  |
|  Raw incl dropped  trades=630  real=$+3,090.58                         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b51  c051_s164_w4_1120_  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  c091_s167_w4_1120_  2 100% +222.0 +222.0 +247.0 $   +293         |
|  b31  c031_s173_w4_1120_  2 100% +145.5 +145.5 +175.8 $   +192         |
|  b28  c028_s173_w1_0928_ 17  76% +49.5 +80.0 +102.0 $   +448           |
|  b58  c058_s173_w3_1045_  1 100% +59.1 +59.1 +59.1 $    +25            |
|  b56  c056_s173_w1_0928_  1 100% +47.7 +47.7 +47.7 $    +21            |
|  b57  c057_s173_w2_1005_  1 100% +47.7 +47.7 +47.7 $    +21            |
|  b89  c089_s167_w2_1005_  7  57% +113.1 +30.9 +790.0 $    +67          |
|  ... 14 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b9   c009_s165_w2_1005_  5   0% -73.0 -66.2 -92.7 $   -203       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=2.3s reconcile=1.94s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=2.3s. run=#4534 https://github.com/28twagg-ops/TradingBot/actions/runs/29794181818
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.csv
Summary: 14 buckets closed trades, $+981.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 3.5% (22/630)
# Options signal frequency

_Generated 2026-07-20T21:50:32.988679_

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

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S164 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S165 | 14 | 7 | 2.0 | ~19 active signal-days |
| S166 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S167 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S168 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 0 | 0 |
| S164 | 0 | 0 |
| S165 | 1309 | 14 |
| S166 | 0 | 0 |
| S167 | 0 | 0 |
| S168 | 0 | 0 |
| S173 | 1636 | 17 |
| S174 | 843 | 7 |

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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-07-20
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |    27 | WARN | <<<
| Missing exit records (post) |    27 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |   274 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=482.46 router=PENDING leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---

## Run 20260721T045356Z

- UTC timestamp: `20260721T045356Z`
- GitHub run: [#4535](https://github.com/28twagg-ops/TradingBot/actions/runs/29802444781)
- Run id: `29802444781`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`8s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-21T00:54:01.072770-04:00","date":"2026-07-21","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":2.4,"phases_s":{"reconcile":2.03},"signals":0,"placed":0,"equity":132131.73,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4535","github_run_id":"29802444781","status":"ok"}
```

### Live bot full output

```text
04:53:58  INFO      Mode: summary
04:53:59  INFO        Daily log -> logs/daily/2026-07-21.md
04:53:59  INFO        Daily log reconciled -> logs/daily/2026-07-21.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         04:53 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.46|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $482.46|
|  Cash                                                           $216.83|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $265.63|
|  Open P&L                                                        $+0.69|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (3 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  MAA      Pullback50      $96.41     $133.63  $133.71  +0.1%   $+0.06  |
|  TPR      Pullback50      $96.54     $140.84  $141.12  +0.2%   $+0.19  |
|  WMB      Pullback50      $72.67     $74.35   $74.80   +0.6%   $+0.43  |
|                                                                        |
|  Total invested                                                 $265.63|
|  Total open P&L                                                  $+0.69|
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
|  2026-07-20  SELL  TJX  Pullback50  $96.31  P&L $+0.06                 |
|  2026-07-20  SELL  OXY  Pullback50  $96.34  P&L $-0.01                 |
|  2026-07-20  SELL  COP  Pullback50  $89.26  P&L $+0.88                 |
|  2026-07-20  SELL  CI  Pullback50  $87.88  P&L $-0.52                  |
|  2026-07-20  SELL  KO  Pullback50  $14.60  P&L $-0.08                  |
|  2026-07-20  SELL  CNP  Pullback50  $9.78  P&L $-0.06                  |
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
=== options_morning_bot (PAPER) 2026-07-21T00:54:01.072770-04:00 ===

[Run context]
After hours (00:54 ET) — exit summary only.
Paper auth OK — equity $132131.73, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $132,131.73                             |
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
|  Reflected trades=213  buckets=22  win=34%                             |
|  Returns   avg=+2.1%  med=-33.3%  p10=-64.9%  p90=+86.7%               |
|  Realized  $+5,522.13                                                  |
|  Raw incl dropped  trades=630  real=$+3,090.58                         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b51  c051_s164_w4_1120_  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  c091_s167_w4_1120_  2 100% +222.0 +222.0 +247.0 $   +293         |
|  b31  c031_s173_w4_1120_  2 100% +145.5 +145.5 +175.8 $   +192         |
|  b28  c028_s173_w1_0928_ 17  76% +49.5 +80.0 +102.0 $   +448           |
|  b58  c058_s173_w3_1045_  1 100% +59.1 +59.1 +59.1 $    +25            |
|  b56  c056_s173_w1_0928_  1 100% +47.7 +47.7 +47.7 $    +21            |
|  b57  c057_s173_w2_1005_  1 100% +47.7 +47.7 +47.7 $    +21            |
|  b89  c089_s167_w2_1005_  7  57% +113.1 +30.9 +790.0 $    +67          |
|  ... 14 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b9   c009_s165_w2_1005_  5   0% -73.0 -66.2 -92.7 $   -203       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-21.log
elapsed=2.4s reconcile=2.03s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=2.4s. run=#4535 https://github.com/28twagg-ops/TradingBot/actions/runs/29802444781
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 3.5% (22/630)
# Options signal frequency

_Generated 2026-07-21T00:54:06.609209_

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

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S164 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S165 | 14 | 7 | 2.0 | ~19 active signal-days |
| S166 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S167 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S168 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 0 | 0 |
| S164 | 0 | 0 |
| S165 | 1392 | 14 |
| S166 | 0 | 0 |
| S167 | 0 | 0 |
| S168 | 0 | 0 |
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
| 2026-07-21 |    0 |    0 |   83 |    0 |    0 |    0 |  118 |   48 |   249 |

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
| Total closed lots           |   274 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=482.46 router=PENDING leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---

## Run 20260721T130039Z

- UTC timestamp: `20260721T130039Z`
- GitHub run: [#4536](https://github.com/28twagg-ops/TradingBot/actions/runs/29832491156)
- Run id: `29832491156`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`7s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-21T09:00:41.871548-04:00","date":"2026-07-21","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.7,"phases_s":{"reconcile":1.52},"signals":0,"placed":0,"equity":134375.05,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4536","github_run_id":"29832491156","status":"ok"}
```

### Live bot full output

```text
13:00:40  INFO      Mode: summary
13:00:40  INFO        Daily log -> logs/daily/2026-07-21.md
13:00:40  INFO        Daily log reconciled -> logs/daily/2026-07-21.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:00 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $481.73|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $481.73|
|  Cash                                                           $216.83|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $264.90|
|  Open P&L                                                        $-0.04|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (3 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  MAA      Pullback50      $96.41     $133.63  $133.71  +0.1%   $+0.06  |
|  TPR      Pullback50      $96.54     $140.84  $141.12  +0.2%   $+0.19  |
|  WMB      Pullback50      $71.95     $74.35   $74.05   -0.4%   $-0.29  |
|                                                                        |
|  Total invested                                                 $264.90|
|  Total open P&L                                                  $-0.04|
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
|  2026-07-20  SELL  TJX  Pullback50  $96.31  P&L $+0.06                 |
|  2026-07-20  SELL  OXY  Pullback50  $96.34  P&L $-0.01                 |
|  2026-07-20  SELL  COP  Pullback50  $89.26  P&L $+0.88                 |
|  2026-07-20  SELL  CI  Pullback50  $87.88  P&L $-0.52                  |
|  2026-07-20  SELL  KO  Pullback50  $14.60  P&L $-0.08                  |
|  2026-07-20  SELL  CNP  Pullback50  $9.78  P&L $-0.06                  |
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
=== options_morning_bot (PAPER) 2026-07-21T09:00:41.871548-04:00 ===

[Run context]
After hours (09:00 ET) — exit summary only.
Paper auth OK — equity $134375.05, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $134,375.05                             |
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
|  Reflected trades=213  buckets=22  win=34%                             |
|  Returns   avg=+2.1%  med=-33.3%  p10=-64.9%  p90=+86.7%               |
|  Realized  $+5,522.13                                                  |
|  Raw incl dropped  trades=630  real=$+3,090.58                         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b51  c051_s164_w4_1120_  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  c091_s167_w4_1120_  2 100% +222.0 +222.0 +247.0 $   +293         |
|  b31  c031_s173_w4_1120_  2 100% +145.5 +145.5 +175.8 $   +192         |
|  b28  c028_s173_w1_0928_ 17  76% +49.5 +80.0 +102.0 $   +448           |
|  b58  c058_s173_w3_1045_  1 100% +59.1 +59.1 +59.1 $    +25            |
|  b56  c056_s173_w1_0928_  1 100% +47.7 +47.7 +47.7 $    +21            |
|  b57  c057_s173_w2_1005_  1 100% +47.7 +47.7 +47.7 $    +21            |
|  b89  c089_s167_w2_1005_  7  57% +113.1 +30.9 +790.0 $    +67          |
|  ... 14 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b9   c009_s165_w2_1005_  5   0% -73.0 -66.2 -92.7 $   -203       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-21.log
elapsed=1.7s reconcile=1.52s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.7s. run=#4536 https://github.com/28twagg-ops/TradingBot/actions/runs/29832491156
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 3.5% (22/630)
# Options signal frequency

_Generated 2026-07-21T09:00:46.586957_

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

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S164 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S165 | 14 | 7 | 2.0 | ~19 active signal-days |
| S166 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S167 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S168 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 0 | 0 |
| S164 | 0 | 0 |
| S165 | 1392 | 14 |
| S166 | 0 | 0 |
| S167 | 0 | 0 |
| S168 | 0 | 0 |
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
| 2026-07-21 |    0 |    0 |   83 |    0 |    0 |    0 |  118 |   48 |   249 |

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
| Total closed lots           |   274 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=481.73 router=PENDING leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---
