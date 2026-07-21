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

## Run 20260721T130534Z

- UTC timestamp: `20260721T130534Z`
- GitHub run: [#4537](https://github.com/28twagg-ops/TradingBot/actions/runs/29832858650)
- Run id: `29832858650`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`7s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-21T09:05:37.965189-04:00","date":"2026-07-21","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.8,"phases_s":{"reconcile":1.55},"signals":0,"placed":0,"equity":134259.05,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4537","github_run_id":"29832858650","status":"ok"}
```

### Live bot full output

```text
13:05:35  INFO      Mode: summary
13:05:36  INFO        Daily log -> logs/daily/2026-07-21.md
13:05:36  INFO        Daily log reconciled -> logs/daily/2026-07-21.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:05 UTC|
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
=== options_morning_bot (PAPER) 2026-07-21T09:05:37.965189-04:00 ===

[Run context]
After hours (09:05 ET) — exit summary only.
Paper auth OK — equity $134259.05, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $134,259.05                             |
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
elapsed=1.8s reconcile=1.55s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.8s. run=#4537 https://github.com/28twagg-ops/TradingBot/actions/runs/29832858650
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 3.5% (22/630)
# Options signal frequency

_Generated 2026-07-21T09:05:42.889011_

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

## Run 20260721T131040Z

- UTC timestamp: `20260721T131040Z`
- GitHub run: [#4538](https://github.com/28twagg-ops/TradingBot/actions/runs/29833220135)
- Run id: `29833220135`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`7s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-21T09:10:43.265436-04:00","date":"2026-07-21","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.9,"phases_s":{"reconcile":1.59},"signals":0,"placed":0,"equity":134459.05,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4538","github_run_id":"29833220135","status":"ok"}
```

### Live bot full output

```text
13:10:41  INFO      Mode: summary
13:10:41  INFO        Daily log -> logs/daily/2026-07-21.md
13:10:41  INFO        Daily log reconciled -> logs/daily/2026-07-21.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:10 UTC|
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
=== options_morning_bot (PAPER) 2026-07-21T09:10:43.265436-04:00 ===

[Run context]
After hours (09:10 ET) — exit summary only.
Paper auth OK — equity $134459.05, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $134,459.05                             |
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
elapsed=1.9s reconcile=1.59s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.9s. run=#4538 https://github.com/28twagg-ops/TradingBot/actions/runs/29833220135
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 3.5% (22/630)
# Options signal frequency

_Generated 2026-07-21T09:10:47.951768_

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

## Run 20260721T131538Z

- UTC timestamp: `20260721T131538Z`
- GitHub run: [#4539](https://github.com/28twagg-ops/TradingBot/actions/runs/29833589243)
- Run id: `29833589243`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`6s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-21T09:15:41.637686-04:00","date":"2026-07-21","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.8,"phases_s":{"reconcile":1.54},"signals":0,"placed":0,"equity":134113.85,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4539","github_run_id":"29833589243","status":"ok"}
```

### Live bot full output

```text
13:15:39  INFO      Mode: summary
13:15:39  INFO        Daily log -> logs/daily/2026-07-21.md
13:15:39  INFO        Daily log reconciled -> logs/daily/2026-07-21.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:15 UTC|
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
=== options_morning_bot (PAPER) 2026-07-21T09:15:41.637686-04:00 ===

[Run context]
After hours (09:15 ET) — exit summary only.
Paper auth OK — equity $134113.85, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $134,113.85                             |
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
elapsed=1.8s reconcile=1.54s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.8s. run=#4539 https://github.com/28twagg-ops/TradingBot/actions/runs/29833589243
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 3.5% (22/630)
# Options signal frequency

_Generated 2026-07-21T09:15:46.469301_

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

## Run 20260721T132038Z

- UTC timestamp: `20260721T132038Z`
- GitHub run: [#4540](https://github.com/28twagg-ops/TradingBot/actions/runs/29833954259)
- Run id: `29833954259`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`7s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-21T09:20:41.939374-04:00","date":"2026-07-21","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.8,"phases_s":{"reconcile":1.53},"signals":0,"placed":0,"equity":134380.69,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4540","github_run_id":"29833954259","status":"ok"}
```

### Live bot full output

```text
13:20:39  INFO      Mode: summary
13:20:40  INFO        Daily log -> logs/daily/2026-07-21.md
13:20:40  INFO        Daily log reconciled -> logs/daily/2026-07-21.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:20 UTC|
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
=== options_morning_bot (PAPER) 2026-07-21T09:20:41.939374-04:00 ===

[Run context]
After hours (09:20 ET) — exit summary only.
Paper auth OK — equity $134380.69, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $134,380.69                             |
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
elapsed=1.8s reconcile=1.53s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.8s. run=#4540 https://github.com/28twagg-ops/TradingBot/actions/runs/29833954259
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 3.5% (22/630)
# Options signal frequency

_Generated 2026-07-21T09:20:46.818468_

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

## Run 20260721T132540Z

- UTC timestamp: `20260721T132540Z`
- GitHub run: [#4541](https://github.com/28twagg-ops/TradingBot/actions/runs/29834325935)
- Run id: `29834325935`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`8s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-21T09:25:44.409109-04:00","date":"2026-07-21","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":2.4,"phases_s":{"reconcile":1.95},"signals":0,"placed":0,"equity":134555.05,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4541","github_run_id":"29834325935","status":"ok"}
```

### Live bot full output

```text
13:25:41  INFO      Mode: summary
13:25:41  INFO        Daily log -> logs/daily/2026-07-21.md
13:25:41  INFO        Daily log reconciled -> logs/daily/2026-07-21.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:25 UTC|
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
=== options_morning_bot (PAPER) 2026-07-21T09:25:44.409109-04:00 ===

[Run context]
After hours (09:25 ET) — exit summary only.
Paper auth OK — equity $134555.05, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $134,555.05                             |
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
elapsed=2.4s reconcile=1.95s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=2.4s. run=#4541 https://github.com/28twagg-ops/TradingBot/actions/runs/29834325935
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 3.5% (22/630)
# Options signal frequency

_Generated 2026-07-21T09:25:49.846718_

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

## Run 20260721T133039Z

- UTC timestamp: `20260721T133039Z`
- GitHub run: [#4542](https://github.com/28twagg-ops/TradingBot/actions/runs/29834702864)
- Run id: `29834702864`
- Live bot: exit=`0`, duration=`216s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-21T09:25:44.409109-04:00","date":"2026-07-21","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":2.4,"phases_s":{"reconcile":1.95},"signals":0,"placed":0,"equity":134555.05,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4541","github_run_id":"29834325935","status":"ok"}
```

### Live bot full output

```text
13:30:40  INFO      Mode: morning_prep
13:30:40  INFO        [prep_positions] 3/3 (3 valid)
13:30:40  INFO      Fetching tickers (universe=both)...
13:30:41  INFO        S&P 500: 503
13:30:41  INFO        MidCap 400: 400
13:30:41  INFO        Total: 903 tickers
13:30:42  INFO        [prep_universe] 40/900 (40 valid)
13:30:44  INFO        [prep_universe] 80/900 (80 valid)
13:30:45  INFO        [prep_universe] 120/900 (120 valid)
13:30:47  INFO        [prep_universe] 160/900 (160 valid)
13:30:48  INFO        [prep_universe] 200/900 (199 valid)
13:30:56  INFO        [prep_universe] 240/900 (238 valid)
13:31:06  INFO        [prep_universe] 280/900 (278 valid)
13:31:19  INFO        [prep_universe] 320/900 (318 valid)
13:31:29  INFO        [prep_universe] 360/900 (358 valid)
13:31:42  INFO        [prep_universe] 400/900 (397 valid)
13:31:55  INFO        [prep_universe] 440/900 (437 valid)
13:32:08  INFO        [prep_universe] 480/900 (477 valid)
13:32:18  INFO        [prep_universe] 520/900 (517 valid)
13:32:31  INFO        [prep_universe] 560/900 (556 valid)
13:32:42  INFO        [prep_universe] 600/900 (596 valid)
13:32:55  INFO        [prep_universe] 640/900 (636 valid)
13:33:08  INFO        [prep_universe] 680/900 (676 valid)
13:33:18  INFO        [prep_universe] 720/900 (715 valid)
13:33:31  INFO        [prep_universe] 760/900 (755 valid)
13:33:44  INFO        [prep_universe] 800/900 (795 valid)
13:33:54  INFO        [prep_universe] 840/900 (834 valid)
13:34:07  INFO        [prep_universe] 880/900 (874 valid)
13:34:13  INFO        [prep_universe] 900/900 (894 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:30 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $483.88|
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
|  Open positions                                                       3|
|  Invested                                                       $267.05|
|  Open P&L                                                        $+2.11|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  MAA      Pullback50      $96.41     $133.63  $133.71  +0.1%   $+0.06  |
|  TPR      Pullback50      $98.20     $140.84  $143.54  +1.9%   $+1.85  |
|  WMB      Pullback50      $72.44     $74.35   $74.56   +0.3%   $+0.20  |
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
|  Signal candidates                                                   28|
|  Universe scanned                                                   900|
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
=== options_morning_bot (PAPER) 2026-07-21T09:34:16.466759-04:00 ===

[Run context]
Paper auth OK — equity $133457.05, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 335 signal(s); top: ['S165:ACN', 'S165:ADBE', 'S165:A', 'S165:BR', 'S165:CSGP', 'S165:DHR', 'S165:EFX', 'S165:FDS']
Paper lab: $133417 broker equity -> 140 bucket(s) ($500 virtual each, unlimited paper)
```

---

## Run 20260721T133600Z

- UTC timestamp: `20260721T133600Z`
- GitHub run: [#4543](https://github.com/28twagg-ops/TradingBot/actions/runs/29835095038)
- Run id: `29835095038`
- Live bot: exit=`0`, duration=`231s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-21T09:25:44.409109-04:00","date":"2026-07-21","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":2.4,"phases_s":{"reconcile":1.95},"signals":0,"placed":0,"equity":134555.05,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4541","github_run_id":"29834325935","status":"ok"}
```

### Live bot full output

```text
13:36:01  INFO      Mode: morning_prep
13:36:03  INFO        [prep_positions] 3/3 (3 valid)
13:36:03  INFO      Fetching tickers (universe=both)...
13:36:03  INFO        S&P 500: 503
13:36:03  INFO        MidCap 400: 400
13:36:03  INFO        Total: 903 tickers
13:36:05  INFO        [prep_universe] 40/900 (40 valid)
13:36:06  INFO        [prep_universe] 80/900 (80 valid)
13:36:08  INFO        [prep_universe] 120/900 (120 valid)
13:36:10  INFO        [prep_universe] 160/900 (160 valid)
13:36:20  INFO        [prep_universe] 200/900 (199 valid)
13:36:31  INFO        [prep_universe] 240/900 (238 valid)
13:36:44  INFO        [prep_universe] 280/900 (278 valid)
13:36:55  INFO        [prep_universe] 320/900 (318 valid)
13:37:08  INFO        [prep_universe] 360/900 (358 valid)
13:37:21  INFO        [prep_universe] 400/900 (397 valid)
13:37:31  INFO        [prep_universe] 440/900 (437 valid)
13:37:45  INFO        [prep_universe] 480/900 (477 valid)
13:37:55  INFO        [prep_universe] 520/900 (517 valid)
13:38:08  INFO        [prep_universe] 560/900 (556 valid)
13:38:19  INFO        [prep_universe] 600/900 (596 valid)
13:38:32  INFO        [prep_universe] 640/900 (636 valid)
13:38:42  INFO        [prep_universe] 680/900 (676 valid)
13:38:56  INFO        [prep_universe] 720/900 (715 valid)
13:39:09  INFO        [prep_universe] 760/900 (755 valid)
13:39:19  INFO        [prep_universe] 800/900 (795 valid)
13:39:32  INFO        [prep_universe] 840/900 (834 valid)
13:39:43  INFO        [prep_universe] 880/900 (874 valid)
13:39:50  INFO        [prep_universe] 900/900 (894 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.72|
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
|  Open positions                                                       3|
|  Invested                                                       $265.89|
|  Open P&L                                                        $+0.95|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  MAA      Pullback50      $96.28     $133.63  $133.53  -0.1%   $-0.07  |
|  TPR      Pullback50      $97.73     $140.84  $142.85  +1.4%   $+1.38  |
|  WMB      Pullback50      $71.89     $74.35   $73.98   -0.5%   $-0.35  |
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
|  Signal candidates                                                   23|
|  Universe scanned                                                   900|
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
=== options_morning_bot (PAPER) 2026-07-21T09:39:52.927744-04:00 ===

[Run context]
Paper auth OK — equity $132945.05, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163] …
```

---

## Run 20260721T134101Z

- UTC timestamp: `20260721T134101Z`
- GitHub run: [#4544](https://github.com/28twagg-ops/TradingBot/actions/runs/29835479087)
- Run id: `29835479087`
- Live bot: exit=`0`, duration=`215s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-21T09:25:44.409109-04:00","date":"2026-07-21","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":2.4,"phases_s":{"reconcile":1.95},"signals":0,"placed":0,"equity":134555.05,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4541","github_run_id":"29834325935","status":"ok"}
```

### Live bot full output

```text
13:41:02  INFO      Mode: morning_prep
13:41:03  INFO        [prep_positions] 3/3 (3 valid)
13:41:03  INFO        Universe cache hit: 903 tickers (tickers_2026-07-21.json)
13:41:04  INFO        [prep_universe] 40/900 (40 valid)
13:41:06  INFO        [prep_universe] 80/900 (80 valid)
13:41:07  INFO        [prep_universe] 120/900 (120 valid)
13:41:09  INFO        [prep_universe] 160/900 (160 valid)
13:41:10  INFO        [prep_universe] 200/900 (199 valid)
13:41:17  INFO        [prep_universe] 240/900 (238 valid)
13:41:30  INFO        [prep_universe] 280/900 (278 valid)
13:41:40  INFO        [prep_universe] 320/900 (318 valid)
13:41:53  INFO        [prep_universe] 360/900 (358 valid)
13:42:06  INFO        [prep_universe] 400/900 (397 valid)
13:42:17  INFO        [prep_universe] 440/900 (437 valid)
13:42:30  INFO        [prep_universe] 480/900 (477 valid)
13:42:43  INFO        [prep_universe] 520/900 (517 valid)
13:42:53  INFO        [prep_universe] 560/900 (556 valid)
13:43:06  INFO        [prep_universe] 600/900 (596 valid)
13:43:17  INFO        [prep_universe] 640/900 (636 valid)
13:43:30  INFO        [prep_universe] 680/900 (676 valid)
13:43:42  INFO        [prep_universe] 720/900 (715 valid)
13:43:52  INFO        [prep_universe] 760/900 (755 valid)
13:44:05  INFO        [prep_universe] 800/900 (795 valid)
13:44:18  INFO        [prep_universe] 840/900 (834 valid)
13:44:31  INFO        [prep_universe] 880/900 (874 valid)
13:44:35  INFO        [prep_universe] 900/900 (894 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.12|
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
|  Open positions                                                       3|
|  Invested                                                       $265.29|
|  Open P&L                                                        $+0.35|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  MAA      Pullback50      $95.94     $133.63  $133.06  -0.4%   $-0.41  |
|  TPR      Pullback50      $97.71     $140.84  $142.82  +1.4%   $+1.36  |
|  WMB      Pullback50      $71.64     $74.35   $73.73   -0.8%   $-0.60  |
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
|  Signal candidates                                                   13|
|  Universe scanned                                                   900|
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
=== options_morning_bot (PAPER) 2026-07-21T09:44:38.062161-04:00 ===

[Run context]
Paper auth OK — equity $131747.05, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163] …
Fetched daily bars for 903/903 symbols
```

---

## Run 20260721T134559Z

- UTC timestamp: `20260721T134559Z`
- GitHub run: [#4545](https://github.com/28twagg-ops/TradingBot/actions/runs/29835867007)
- Run id: `29835867007`
- Live bot: exit=`0`, duration=`0s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-21T09:25:44.409109-04:00","date":"2026-07-21","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":2.4,"phases_s":{"reconcile":1.95},"signals":0,"placed":0,"equity":134555.05,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4541","github_run_id":"29834325935","status":"ok"}
```

### Live bot full output

```text
13:46:00  INFO      Mode: morning_scan
13:46:01  INFO        [positions] 3/3 (3 valid)
13:46:01  INFO        SELL MARKET [urgent] WMB closed
13:46:04  INFO        TX logged: SELL WMB  P&L -1.1%
13:46:04  INFO        SELL MARKET [urgent] MAA closed
13:46:06  INFO        TX logged: SELL MAA  P&L -0.57%
13:46:06  INFO        Universe cache hit: 903 tickers (tickers_2026-07-21.json)
13:46:08  INFO        [universe] 40/902 (40 valid)
13:46:09  INFO        [universe] 80/902 (80 valid)
13:46:11  INFO        [universe] 120/902 (120 valid)
13:46:12  INFO        [universe] 160/902 (160 valid)
13:46:14  INFO        [universe] 200/902 (199 valid)
13:46:19  INFO        [universe] 240/902 (238 valid)
13:46:32  INFO        [universe] 280/902 (278 valid)
13:46:46  INFO        [universe] 320/902 (318 valid)
13:46:56  INFO        [universe] 360/902 (358 valid)
13:47:07  INFO        [universe] 400/902 (397 valid)
13:47:20  INFO        [universe] 440/902 (437 valid)
13:47:31  INFO        [universe] 480/902 (477 valid)
13:47:45  INFO        [universe] 520/902 (517 valid)
13:47:55  INFO        [universe] 560/902 (556 valid)
13:48:09  INFO        [universe] 600/902 (596 valid)
13:48:19  INFO        [universe] 640/902 (636 valid)
13:48:32  INFO        [universe] 680/902 (676 valid)
13:48:43  INFO        [universe] 720/902 (715 valid)
13:48:57  INFO        [universe] 760/902 (755 valid)
13:49:07  INFO        [universe] 800/902 (795 valid)
13:49:21  INFO        [universe] 840/902 (834 valid)
13:49:31  INFO        [universe] 880/902 (874 valid)
13:49:38  INFO        [universe] 902/902 (896 valid)
13:49:40  INFO        BUY  BIIB  $96.21  [Pullback50]  id=a216be62-29d1-46b1-989d-fd807c7df127
13:49:40  INFO        BUY  CNP  $96.21  [Pullback50]  id=63e9c122-d739-4556-b38c-faf134258615
13:49:40  INFO        BUY  CI  $96.21  [Pullback50]  id=441abf71-e258-4e09-aef4-e015b16b61a1
13:49:40  INFO        BUY  IEX  $71.28  [Pullback50]  id=fb23e7d8-1e95-420c-8899-2b8e13c0e627

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_SCAN|
|  Time                                                         13:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $481.07|
+========================================================================+

+========================================================================+
|                   RUBBER BAND BOT v8  --  DAILY SCAN                   |
+========================================================================+
|  Mode                                                      *** LIVE ***|
|  Date                                                        2026-07-21|
|  Universe                                                          both|
|  Mon~  Jul: 52wkLow + Pullback50 (display only — schedule not enforced)|
|  Disabled                GapDown, VolumeSpike (see DISABLED_STRATEGIES)|
|  Regime                                                            BULL|
|  Exit                                      midline / stop-0.5% / 3d max|
+========================================================================+

+========================================================================+
|                                ACCOUNT                                 |
+========================================================================+
|  Equity                                                         $481.07|
|  Cash                                                           $216.83|
|  Reserve                                          $24.05  (always kept)|
|  Available                                    $192.78  (for new trades)|
|  Trade size             $96.21  (20% per signal — all strategies equal)|
+========================================================================+

+========================================================================+
|                           HOLDINGS  (3 open)                           |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  MAA      Pullback50      $95.80     $133.63  $132.86  -0.6%   $-0.55  |
|  TPR      Pullback50      $97.00     $140.84  $141.78  +0.7%   $+0.65  |
|  WMB      Pullback50      $71.44     $74.35   $73.53   -1.1%   $-0.80  |
|                                                                        |
|  Total invested                                                 $264.24|
|  Total open P&L                                                  $-0.70|
|  Buys today: 0  |  entry cap: 2  |  max open: 5                        |
+========================================================================+

+========================================================================+
|                               PLAN CACHE                               |
+========================================================================+
|  Mode                                                           morning|
|  File                                      logs/plans/morning_plan.json|
|  Use cached plan                                  no (stale (17280.5m))|
+========================================================================+

+========================================================================+
|          EXIT EVALUATION  (EOD -- midline + stop + max-hold)           |
+========================================================================+
|  WMB  P&L -1.1%  $-0.80                         EXIT: stop_loss (-1.1%)|
|  MAA  P&L -0.6%  $-0.55                         EXIT: stop_loss (-0.6%)|
|  TPR  P&L +0.7%  $+0.65                                            HOLD|
+========================================================================+

+========================================================================+
|                           EXIT EVAL SUMMARY                            |
+========================================================================+
|  Exit eval    attempted 2 | filled 2 | partial 0 | pending 0 | failed 0|
|  Other skips     already logged today 0  |  no price data 0  |  holds 1|
|  Stop-loss breaches                                                   2|
|  WMB                                         -1.10%  (threshold -0.50%)|
|  MAA                                         -0.57%  (threshold -0.50%)|
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
|                         SIGNALS FOUND  --  11                          |
+========================================================================+
|  TICKER   STRATEGY        TIER   PRICE    RSI    VOL_Z   TRIGGER       |
+------------------------------------------------------------------------+
|  BIIB     Pullback50      eq     $200.62  40.8   -1.90   50MA bounce (+|
|  CNP      Pullback50      eq     $42.88   41.4   -2.46   50MA bounce (-|
|  CI       Pullback50      eq     $283.99  56.3   -1.90   50MA bounce (-|
|  IEX      Pullback50      eq     $219.72  38.3   -1.95   50MA bounce (+|
|  MU       Pullback50      eq     $935.13  32.0   -2.27   50MA bounce (-|
|  AVT      Pullback50      eq     $86.90   45.5   -2.23   50MA bounce (+|
|  AXTA     Pullback50      eq     $32.09   30.9   -2.48   50MA bounce (+|
|  IRT      Pullback50      eq     $16.46   46.4   -1.61   50MA bounce (-|
|  MTDR     Pullback50      eq     $54.17   69.3   -2.70   50MA bounce (+|
|  PEN      Pullback50      eq     $317.33  55.6   -2.18   50MA bounce (-|
|  VNOM     Pullback50      eq     $44.76   62.7   -2.74   50MA bounce (+|
|                                                                        |
+========================================================================+

+========================================================================+
|                              ENTRY ORDERS                              |
+========================================================================+
|    ENTER [eq] BIIB  Pullback50                                   $96.21|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    ENTER [eq] CNP  Pullback50                                    $96.21|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    ENTER [eq] CI  Pullback50                                     $96.21|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    ENTER [eq] IEX  Pullback50                                    $71.28|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    SKIP [eq] MU  Pullback50                                       cap 5|```

### Options bot full output

```text

## Run 20260721T135046Z

- UTC timestamp: `20260721T135046Z`
- GitHub run: [#4547](https://github.com/28twagg-ops/TradingBot/actions/runs/29836254216)
- Run id: `29836254216`
- Live bot: exit=`0`, duration=`248s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-21T09:25:44.409109-04:00","date":"2026-07-21","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":2.4,"phases_s":{"reconcile":1.95},"signals":0,"placed":0,"equity":134555.05,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4541","github_run_id":"29834325935","status":"ok"}
```

### Live bot full output

```text
13:50:47  INFO      Mode: morning_scan
13:50:49  INFO        [positions] 5/5 (5 valid)
13:50:49  INFO        SELL MARKET [urgent] IEX closed
13:50:51  INFO        TX logged: SELL IEX  P&L -0.68%
13:50:51  INFO        SELL LIMIT CI  qty=0.334394683  limit=$286.59  id=99aaf9ff-d3e3-4ef9-a69a-3b52c3cbe5b7
13:51:22  INFO        SELL LIMIT filled CI (confirmed by position check)
13:51:22  INFO        TX logged: SELL CI  P&L -0.18%
13:51:22  INFO        Universe cache hit: 903 tickers (tickers_2026-07-21.json)
13:51:23  INFO        [universe] 40/900 (40 valid)
13:51:25  INFO        [universe] 80/900 (80 valid)
13:51:26  INFO        [universe] 120/900 (120 valid)
13:51:27  INFO        [universe] 160/900 (160 valid)
13:51:29  INFO        [universe] 200/900 (199 valid)
13:51:36  INFO        [universe] 240/900 (238 valid)
13:51:47  INFO        [universe] 280/900 (278 valid)
13:52:00  INFO        [universe] 320/900 (318 valid)
13:52:11  INFO        [universe] 360/900 (358 valid)
13:52:24  INFO        [universe] 400/900 (397 valid)
13:52:37  INFO        [universe] 440/900 (437 valid)
13:52:47  INFO        [universe] 480/900 (477 valid)
13:53:00  INFO        [universe] 520/900 (517 valid)
13:53:11  INFO        [universe] 560/900 (556 valid)
13:53:24  INFO        [universe] 600/900 (596 valid)
13:53:35  INFO        [universe] 640/900 (636 valid)
13:53:48  INFO        [universe] 680/900 (676 valid)
13:53:59  INFO        [universe] 720/900 (715 valid)
13:54:12  INFO        [universe] 760/900 (755 valid)
13:54:25  INFO        [universe] 800/900 (795 valid)
13:54:36  INFO        [universe] 840/900 (834 valid)
13:54:49  INFO        [universe] 880/900 (874 valid)
13:54:53  INFO        [universe] 900/900 (894 valid)
13:54:53  INFO        place_all_stops: checking 3 positions...
13:54:53  INFO        STOP skipped BIIB: fractional (0.4766 shares) — software exit will handle it
13:54:54  INFO        STOP-MARKET placed CNP  qty=2 (pos=2.2410)  stop=$42.71  id=d98c3e37-bd74-4ff1-90b6-07c4bb4a6ad8
13:54:54  INFO        STOP skipped TPR: fractional (0.6841 shares) — software exit will handle it

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_SCAN|
|  Time                                                         13:50 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $480.52|
+========================================================================+

+========================================================================+
|                   RUBBER BAND BOT v8  --  DAILY SCAN                   |
+========================================================================+
|  Mode                                                      *** LIVE ***|
|  Date                                                        2026-07-21|
|  Universe                                                          both|
|  Mon~  Jul: 52wkLow + Pullback50 (display only — schedule not enforced)|
|  Disabled                GapDown, VolumeSpike (see DISABLED_STRATEGIES)|
|  Regime                                                            BULL|
|  Exit                                      midline / stop-0.5% / 3d max|
+========================================================================+

+========================================================================+
|                                ACCOUNT                                 |
+========================================================================+
|  Equity                                                         $480.52|
|  Cash                                                            $24.11|
|  Reserve                                          $24.03  (always kept)|
|  Available                                      $0.08  (for new trades)|
|  Trade size             $96.10  (20% per signal — all strategies equal)|
+========================================================================+

+========================================================================+
|                           HOLDINGS  (5 open)                           |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  BIIB     Pullback50      $96.09     $201.84  $201.60  -0.1%   $-0.11  |
|  CI       Pullback50      $96.03     $287.68  $287.17  -0.2%   $-0.17  |
|  CNP      Pullback50      $96.08     $42.92   $42.88   -0.1%   $-0.11  |
|  IEX      Pullback50      $70.78     $220.50  $219.00  -0.7%   $-0.49  |
|  TPR      Pullback50      $97.43     $140.84  $142.42  +1.1%   $+1.08  |
|                                                                        |
|  Total invested                                                 $456.41|
|  Total open P&L                                                  $+0.20|
|  Buys today: 0  |  entry cap: 0  |  max open: 5                        |
+========================================================================+

+========================================================================+
|                               PLAN CACHE                               |
+========================================================================+
|  Mode                                                           morning|
|  File                                      logs/plans/morning_plan.json|
|  Use cached plan                                  no (stale (17285.3m))|
+========================================================================+

+========================================================================+
|          EXIT EVALUATION  (EOD -- midline + stop + max-hold)           |
+========================================================================+
|  IEX  P&L -0.7%  $-0.49                         EXIT: stop_loss (-0.7%)|
|  CI  P&L -0.2%  $-0.17                            EXIT: midline (-0.2%)|
|  BIIB  P&L -0.1%  $-0.11                                           HOLD|
|  CNP  P&L -0.1%  $-0.11                                            HOLD|
|  TPR  P&L +1.1%  $+1.08                                            HOLD|
+========================================================================+

+========================================================================+
|                           EXIT EVAL SUMMARY                            |
+========================================================================+
|  Exit eval    attempted 2 | filled 2 | partial 0 | pending 0 | failed 0|
|  Other skips     already logged today 0  |  no price data 0  |  holds 3|
|  Stop-loss breaches                                                   1|
|  IEX                                         -0.68%  (threshold -0.50%)|
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
|                         SIGNALS FOUND  --  13                          |
+========================================================================+
|  TICKER   STRATEGY        TIER   PRICE    RSI    VOL_Z   TRIGGER       |
+------------------------------------------------------------------------+
|  APA      Pullback50      eq     $35.52   65.6   -3.07   50MA bounce (-|
|  CI       Pullback50      eq     $287.17  58.3   -1.86   50MA bounce (+|
|  F        Pullback50      eq     $14.17   54.8   -3.32   50MA bounce (-|
|  BEN      Pullback50      eq     $32.51   43.2   -3.19   50MA bounce (+|
|  GM       Pullback50      eq     $78.34   54.5   -1.85   50MA bounce (-|
|  IEX      Pullback50      eq     $219.00  37.5   -1.91   50MA bounce (+|
|  IRM      Pullback50      eq     $125.36  48.0   -3.12   50MA bounce (-|
|  KDP      Pullback50      eq     $30.42   35.1   -1.47   50MA bounce (-|
|  MU       Pullback50      eq     $938.71  32.4   -2.23   50MA bounce (-|
|  MTDR     Pullback50      eq     $53.93   68.7   -2.69   50MA bounce (+|
|  PEN      Pullback50      eq     $317.44  56.0   -2.18   50MA bounce (-|
|  TWLO     Pullback50      eq     $203.17  45.6   -3.26   50MA bounce (+|
|  VNOM     Pullback50      eq     $44.55   61.8   -2.74   50MA bounce (-|
|                                                                        |
+========================================================================+

+========================================================================+
|                              ENTRY ORDERS                              |
+========================================================================+
|  Skipped                                  no entry slots (max_trades=0)|
+========================================================================+

+========================================================================+
|                            SESSION SUMMARY                             |13:54:54  INFO        Daily log -> logs/daily/2026-07-21.md
13:54:54  INFO        Dashboard written → logs/dashboard.md

+========================================================================+
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Strategy   52wkLow + Pullback50 (display only — schedule not enforced)|
|  Scanned                                                            894|
|  Signals                                                             13|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  0 unconfirmed|
|  Exits                                                                2|
|  Open pos                                                             3|
|  Equity                                                         $481.16|
|  Cash                                                           $190.93|
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
=== options_morning_bot (PAPER) 2026-07-21T09:54:56.048559-04:00 ===

[Run context]
Paper auth OK — equity $130997.05, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163] …
Fetched daily bars for 903/903 symbols
```

---

## Run 20260721T135613Z

- UTC timestamp: `20260721T135613Z`
- GitHub run: [#4548](https://github.com/28twagg-ops/TradingBot/actions/runs/29836643194)
- Run id: `29836643194`
- Live bot: exit=`0`, duration=`240s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-21T09:25:44.409109-04:00","date":"2026-07-21","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":2.4,"phases_s":{"reconcile":1.95},"signals":0,"placed":0,"equity":134555.05,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4541","github_run_id":"29834325935","status":"ok"}
```

### Live bot full output

```text
13:56:14  INFO      Mode: morning_scan
13:56:15  INFO        [positions] 3/3 (3 valid)
13:56:15  INFO        Universe cache hit: 903 tickers (tickers_2026-07-21.json)
13:56:16  INFO        [universe] 40/900 (40 valid)
13:56:18  INFO        [universe] 80/900 (80 valid)
13:56:19  INFO        [universe] 120/900 (120 valid)
13:56:21  INFO        [universe] 160/900 (160 valid)
13:56:22  INFO        [universe] 200/900 (199 valid)
13:56:30  INFO        [universe] 240/900 (238 valid)
13:56:41  INFO        [universe] 280/900 (278 valid)
13:56:54  INFO        [universe] 320/900 (318 valid)
13:57:05  INFO        [universe] 360/900 (358 valid)
13:57:18  INFO        [universe] 400/900 (397 valid)
13:57:28  INFO        [universe] 440/900 (437 valid)
13:57:42  INFO        [universe] 480/900 (477 valid)
13:57:55  INFO        [universe] 520/900 (517 valid)
13:58:05  INFO        [universe] 560/900 (556 valid)
13:58:19  INFO        [universe] 600/900 (596 valid)
13:58:29  INFO        [universe] 640/900 (636 valid)
13:58:43  INFO        [universe] 680/900 (676 valid)
13:58:53  INFO        [universe] 720/900 (715 valid)
13:59:04  INFO        [universe] 760/900 (755 valid)
13:59:18  INFO        [universe] 800/900 (795 valid)
13:59:28  INFO        [universe] 840/900 (834 valid)
13:59:42  INFO        [universe] 880/900 (874 valid)
13:59:48  INFO        [universe] 900/900 (894 valid)
13:59:50  ERROR       BUY FAILED CI: {"code":40010001,"message":"client_order_id must be unique"}
13:59:50  INFO        BUY  DUK  $96.26  [Pullback50]  id=2aa53881-8e1e-442d-92ba-bf42b6669fb4
13:59:50  INFO        BUY  BEN  $70.61  [Pullback50]  id=3be5fa63-89cf-4b0f-8110-9bd62fadcb13

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_SCAN|
|  Time                                                         13:56 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $481.29|
+========================================================================+

+========================================================================+
|                   RUBBER BAND BOT v8  --  DAILY SCAN                   |
+========================================================================+
|  Mode                                                      *** LIVE ***|
|  Date                                                        2026-07-21|
|  Universe                                                          both|
|  Mon~  Jul: 52wkLow + Pullback50 (display only — schedule not enforced)|
|  Disabled                GapDown, VolumeSpike (see DISABLED_STRATEGIES)|
|  Regime                                                            BULL|
|  Exit                                      midline / stop-0.5% / 3d max|
+========================================================================+

+========================================================================+
|                                ACCOUNT                                 |
+========================================================================+
|  Equity                                                         $481.29|
|  Cash                                                           $190.93|
|  Reserve                                          $24.06  (always kept)|
|  Available                                    $166.87  (for new trades)|
|  Trade size             $96.26  (20% per signal — all strategies equal)|
+========================================================================+

+========================================================================+
|                           HOLDINGS  (3 open)                           |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  BIIB     Pullback50      $96.73     $201.84  $202.95  +0.5%   $+0.53  |
|  CNP      Pullback50      $96.17     $42.92   $42.91   -0.0%   $-0.02  |
|  TPR      Pullback50      $97.46     $140.84  $142.46  +1.1%   $+1.11  |
|                                                                        |
|  Total invested                                                 $290.36|
|  Total open P&L                                                  $+1.61|
|  Buys today: 0  |  entry cap: 2  |  max open: 5                        |
+========================================================================+

+========================================================================+
|                               PLAN CACHE                               |
+========================================================================+
|  Mode                                                           morning|
|  File                                      logs/plans/morning_plan.json|
|  Use cached plan                                  no (stale (17290.8m))|
+========================================================================+

+========================================================================+
|          EXIT EVALUATION  (EOD -- midline + stop + max-hold)           |
+========================================================================+
|  CNP  P&L -0.0%  $-0.02                                            HOLD|
|  BIIB  P&L +0.5%  $+0.53                                           HOLD|
|  TPR  P&L +1.1%  $+1.11                                            HOLD|
+========================================================================+

+========================================================================+
|                           EXIT EVAL SUMMARY                            |
+========================================================================+
|  Exit eval    attempted 0 | filled 0 | partial 0 | pending 0 | failed 0|
|  Other skips     already logged today 0  |  no price data 0  |  holds 3|
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
|                         SIGNALS FOUND  --  16                          |
+========================================================================+
|  TICKER   STRATEGY        TIER   PRICE    RSI    VOL_Z   TRIGGER       |
+------------------------------------------------------------------------+
|  CI       Pullback50      eq     $287.15  58.3   -1.86   50MA bounce (+|
|  DUK      Pullback50      eq     $125.19  46.8   -2.75   50MA bounce (+|
|  BEN      Pullback50      eq     $32.45   42.6   -3.18   50MA bounce (+|
|  F        Pullback50      eq     $14.23   55.9   -3.31   50MA bounce (-|
|  GM       Pullback50      eq     $79.25   57.2   -1.74   50MA bounce (+|
|  IEX      Pullback50      eq     $219.07  37.6   -1.91   50MA bounce (+|
|  IRM      Pullback50      eq     $125.38  48.1   -3.11   50MA bounce (-|
|  KDP      Pullback50      eq     $30.48   35.5   -1.46   50MA bounce (-|
|  MAA      Pullback50      eq     $133.39  37.9   -3.28   50MA bounce (-|
|  NEE      Pullback50      eq     $87.84   50.3   -2.96   50MA bounce (-|
|  TXT      Pullback50      eq     $91.19   48.0   -2.61   50MA bounce (+|
|  CHRD     Pullback50      eq     $131.64  73.8   -2.76   50MA bounce (+|
|  IRT      Pullback50      eq     $16.47   46.5   -1.61   50MA bounce (-|
|  MTDR     Pullback50      eq     $53.75   68.2   -2.68   50MA bounce (+|
|  PEN      Pullback50      eq     $317.51  56.3   -2.17   50MA bounce (-|
|  TWLO     Pullback50      eq     $203.81  46.4   -3.25   50MA bounce (+|
|                                                                        |
+========================================================================+

+========================================================================+
|                              ENTRY ORDERS                              |
+========================================================================+
|    ENTER [eq] CI  Pullback50                                     $96.26|
|    ENTER [eq] DUK  Pullback50                                    $96.26|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    ENTER [eq] BEN  Pullback50                                    $70.61|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    SKIP [eq] F  Pullback50                                        cap 5|14:00:12  INFO        place_all_stops: checking 5 positions...
14:00:12  INFO        STOP-MARKET placed BEN  qty=2 (pos=2.1710)  stop=$32.36  id=650f4aac-bb50-4560-8015-a8cce3f55ac4
14:00:12  INFO        STOP skipped BIIB: fractional (0.4766 shares) — software exit will handle it
14:00:12  INFO        STOP already live CNP @ $42.71
14:00:12  INFO        STOP skipped DUK: fractional (0.7693 shares) — software exit will handle it
14:00:12  INFO        STOP skipped TPR: fractional (0.6841 shares) — software exit will handle it
14:00:13  INFO        Daily log -> logs/daily/2026-07-21.md
14:00:13  INFO        Dashboard written → logs/dashboard.md

|    SKIP [eq] GM  Pullback50                                       cap 5|
|    SKIP [eq] IEX  Pullback50                                      cap 5|
|    SKIP [eq] IRM  Pullback50                                      cap 5|
|    SKIP [eq] KDP  Pullback50                                      cap 5|
|    SKIP [eq] MAA  Pullback50                                      cap 5|
|    SKIP [eq] NEE  Pullback50                                      cap 5|
|    SKIP [eq] TXT  Pullback50                                      cap 5|
|    SKIP [eq] CHRD  Pullback50                                     cap 5|
|    SKIP [eq] IRT  Pullback50                                      cap 5|
|    SKIP [eq] MTDR  Pullback50                                     cap 5|
|    SKIP [eq] PEN  Pullback50                                      cap 5|
|    SKIP [eq] TWLO  Pullback50                                     cap 5|

+========================================================================+
|                         BUY FILL CONFIRMATION                          |
+========================================================================+
|  Pending submits                                                      2|
+------------------------------------------------------------------------+
|  DUK                                                  still unconfirmed|
|  BEN                                                  still unconfirmed|
+========================================================================+
+========================================================================+

+========================================================================+
|                           GTC STOP PLACEMENT                           |
+========================================================================+
|  Waiting 5s for 2 buy submit(s) to settle...                           |
+========================================================================+

+========================================================================+
|                            SESSION SUMMARY                             |
+========================================================================+
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Strategy   52wkLow + Pullback50 (display only — schedule not enforced)|
|  Scanned                                                            894|
|  Signals                                                             16|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  2 unconfirmed|
|  Exits                                                                0|
|  Open pos                                                             5|
|  Equity                                                         $481.18|
|  Cash                                                            $24.08|
+========================================================================+
```

### Options bot full output

```text

## Run 20260721T140054Z

- UTC timestamp: `20260721T140054Z`
- GitHub run: [#4549](https://github.com/28twagg-ops/TradingBot/actions/runs/29837035380)
- Run id: `29837035380`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-21T09:25:44.409109-04:00","date":"2026-07-21","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":2.4,"phases_s":{"reconcile":1.95},"signals":0,"placed":0,"equity":134555.05,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4541","github_run_id":"29834325935","status":"ok"}
```

### Live bot full output

```text
14:00:55  INFO      Mode: exits
14:00:55  INFO        Daily log -> logs/daily/2026-07-21.md
14:00:55  INFO        Daily log reconciled -> logs/daily/2026-07-21.md (4 ledger rows)
14:00:55  INFO        place_all_stops: checking 5 positions...
14:00:55  INFO        STOP already live BEN @ $32.36
14:00:55  INFO        STOP skipped BIIB: fractional (0.4766 shares) — software exit will handle it
14:00:55  INFO        STOP already live CNP @ $42.71
14:00:55  INFO        STOP skipped DUK: fractional (0.7693 shares) — software exit will handle it
14:00:55  INFO        STOP skipped TPR: fractional (0.6841 shares) — software exit will handle it
14:00:55  INFO        [positions] 5/5 (5 valid)
14:00:55  INFO        Daily log -> logs/daily/2026-07-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:00 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $481.00|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CNP  P&L -0.3%  $-0.25                                            HOLD|
|  BEN  P&L +0.0%  $+0.00                                            HOLD|
|  DUK  P&L +0.1%  $+0.06                                            HOLD|
|  BIIB  P&L +0.4%  $+0.43                                           HOLD|
|  TPR  P&L +1.1%  $+1.08                                            HOLD|
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
=== options_morning_bot (PAPER) 2026-07-21T10:00:57.453100-04:00 ===

[Run context]
Paper auth OK — equity $131737.05, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 335 signal(s); top: ['S165:ACN', 'S165:ADBE', 'S165:A', 'S165:BR', 'S165:CSGP', 'S165:DHR', 'S165:EFX', 'S165:FDS']
Paper lab: $131457 broker equity -> 140 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 750 no tradeable call, 900 pending order
Placed 25 new entry order(s).
```

---

## Run 20260721T140602Z

- UTC timestamp: `20260721T140602Z`
- GitHub run: [#4550](https://github.com/28twagg-ops/TradingBot/actions/runs/29837434495)
- Run id: `29837434495`
- Live bot: exit=`0`, duration=`5s`
- Options bot: exit=`0`, duration=`203s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-21T10:06:09.233997-04:00","date":"2026-07-21","mode":"entry+manage","header":"entry+manage (30 new)","elapsed_s":197.3,"phases_s":{"reconcile":1.92,"cancel":0.16,"manage":1.0,"scan":52.37,"entries":138.61,"reconcile2":2.46},"signals":335,"placed":30,"equity":131446.65,"open_positions":4,"pending_orders":15,"open_lots":40,"submitted_today":30,"filled_today":40,"unattributed_contracts":0,"top_signals":["S165:ACN","S165:ADBE","S165:A","S165:BR","S165:CSGP","S165:DHR","S165:EFX","S165:FDS"],"github_run":"4550","github_run_id":"29837434495","status":"ok"}
```

### Live bot full output

```text
14:06:03  INFO      Mode: exits
14:06:05  INFO        Daily log -> logs/daily/2026-07-21.md
14:06:05  INFO        Daily log reconciled -> logs/daily/2026-07-21.md (4 ledger rows)
14:06:05  INFO        place_all_stops: checking 5 positions...
14:06:05  INFO        STOP already live BEN @ $32.36
14:06:05  INFO        STOP skipped BIIB: fractional (0.4766 shares) — software exit will handle it
14:06:05  INFO        STOP already live CNP @ $42.71
14:06:05  INFO        STOP skipped DUK: fractional (0.7693 shares) — software exit will handle it
14:06:05  INFO        STOP skipped TPR: fractional (0.6841 shares) — software exit will handle it
14:06:06  INFO        [positions] 5/5 (5 valid)
14:06:07  INFO        Daily log -> logs/daily/2026-07-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $481.35|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CNP  P&L -0.3%  $-0.28                                            HOLD|
|  DUK  P&L +0.3%  $+0.24                                            HOLD|
|  BEN  P&L +0.3%  $+0.23                                            HOLD|
|  BIIB  P&L +0.7%  $+0.67                                           HOLD|
|  TPR  P&L +0.8%  $+0.82                                            HOLD|
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
=== options_morning_bot (PAPER) 2026-07-21T10:06:09.233997-04:00 ===

[Run context]
Paper auth OK — equity $131448.69, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 335 signal(s); top: ['S165:ACN', 'S165:ADBE', 'S165:A', 'S165:BR', 'S165:CSGP', 'S165:DHR', 'S165:EFX', 'S165:FDS']
Paper lab: $131541 broker equity -> 140 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 550 no tradeable call, 1095 pending order
Placed 30 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $131,446.65                             |
|  Signals this run              335                                     |
|  Orders submitted (session)    30                                      |
|  Orders filled today (ledger)  40                                      |
|  Entries placed this run       30                                      |
|  Open virtual lots             40                                      |
|  Broker option positions       4                                       |
|  Pending orders                15                                      |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=222  buckets=22  win=33%                             |
|  Returns   avg=-0.4%  med=-38.1%  p10=-66.0%  p90=+84.6%               |
|  Realized  $+5,148.13                                                  |
|  Raw incl dropped  trades=667  real=$+3,510.58                         |
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
|  b30  c030_s173_w3_1045_  9  33% +38.8  +0.0 +168.9 $   +260           |
|  ... 14 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b9   c009_s165_w2_1005_  5   0% -73.0 -66.2 -92.7 $   -203       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (15)                                                   |
+------------------------------------------------------------------------+
|  Top groups                    S164:LULU(5), S167:CELH(5), S163:HAL(5) |
+------------------------------------------------------------------------+
|  b21  S164 LULU     limit=0.65                                         |
|  b49  S164 LULU     limit=0.65                                         |
|  b77  S164 LULU     limit=0.65                                         |
|  b105 S164 LULU     limit=0.65                                         |
|  b133 S164 LULU     limit=0.65                                         |
|  ... 10 more pending order(s)                                          |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (4)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  HAL260724C00033000           15    -19.4%   $   -180.00               |
|  HAL260731C00033500           10    -19.1%   $   -135.00               |
|  CELH260724C00029000          10    -22.2%   $   -100.00               |
|  HAL260724C00035000            5    -25.0%   $    -10.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-21.log
elapsed=197.3s reconcile=1.92s cancel=0.16s manage=1.0s scan=52.37s entries=138.61s
STATUS: options_morning_bot run complete (PAPER) elapsed=197.3s. run=#4550 https://github.com/28twagg-ops/TradingBot/actions/runs/29837434495
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 3.3% (22/667)
# Options signal frequency

_Generated 2026-07-21T10:09:29.626911_

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
| 2026-07-21 |    1 |    1 |    1 |    1 |    1 |    1 |    0 |    0 |     6 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 1 | 1 | 1.0 | ~38 active signal-days |
| S164 | 1 | 1 | 1.0 | ~38 active signal-days |
| S165 | 15 | 8 | 1.9 | ~20 active signal-days |
| S166 | 1 | 1 | 1.0 | ~38 active signal-days |
| S167 | 1 | 1 | 1.0 | ~38 active signal-days |
| S168 | 1 | 1 | 1.0 | ~38 active signal-days |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 10 | 1 |
| S164 | 10 | 1 |
| S165 | 1407 | 15 |
| S166 | 10 | 1 |
| S167 | 10 | 1 |
| S168 | 15 | 1 |
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
| 2026-07-21 |   10 |   10 |   98 |   10 |   10 |   15 |  118 |   48 |   319 |

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
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    40 | INFO |
| Total closed lots           |   286 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=481.35 router=CONFIRMED leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---

## Run 20260721T141035Z

- UTC timestamp: `20260721T141035Z`
- GitHub run: [#4551](https://github.com/28twagg-ops/TradingBot/actions/runs/29837823135)
- Run id: `29837823135`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`55s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-21T10:10:39.976710-04:00","date":"2026-07-21","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":48.8,"phases_s":{"reconcile":1.89,"cancel":0.02,"manage":0.34,"scan":44.65,"entries":0.14,"reconcile2":1.56},"signals":335,"placed":0,"equity":130601.75,"open_positions":3,"pending_orders":10,"open_lots":25,"submitted_today":30,"filled_today":45,"unattributed_contracts":0,"top_signals":["S165:ACN","S165:ADBE","S165:A","S165:BR","S165:CSGP","S165:DHR","S165:EFX","S165:FDS"],"github_run":"4551","github_run_id":"29837823135","status":"ok"}
```

### Live bot full output

```text
14:10:36  INFO      Mode: exits
14:10:36  INFO        Daily log -> logs/daily/2026-07-21.md
14:10:36  INFO        Daily log reconciled -> logs/daily/2026-07-21.md (4 ledger rows)
14:10:36  INFO        place_all_stops: checking 5 positions...
14:10:36  INFO        STOP already live BEN @ $32.36
14:10:36  INFO        STOP skipped BIIB: fractional (0.4766 shares) — software exit will handle it
14:10:36  INFO        STOP already live CNP @ $42.71
14:10:36  INFO        STOP skipped DUK: fractional (0.7693 shares) — software exit will handle it
14:10:36  INFO        STOP skipped TPR: fractional (0.6841 shares) — software exit will handle it
14:10:37  INFO        [positions] 5/5 (5 valid)
14:10:37  INFO        Daily log -> logs/daily/2026-07-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $481.63|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CNP  P&L -0.3%  $-0.30                                            HOLD|
|  DUK  P&L +0.2%  $+0.17                                            HOLD|
|  BEN  P&L +0.5%  $+0.33                                            HOLD|
|  BIIB  P&L +0.6%  $+0.59                                           HOLD|
|  TPR  P&L +1.2%  $+1.17                                            HOLD|
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
  open_lots=40 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=7
  zombies_flagged=40
  FLAG b116|S167|8d992c06 zombie age_min=851 notional=$45.00 occ=CELH260724C00029000 action=error:{"bid":"0.37","buy_limit_price":"0.4","code":40310000,"existing_order_id":"3dc8b475-76d1-4e4f-9438-9e367f1be852","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b88|S167|35a13654 zombie age_min=851 notional=$45.00 occ=CELH260724C00029000 action=error:{"bid":"0.37","buy_limit_price":"0.4","code":40310000,"existing_order_id":"3dc8b475-76d1-4e4f-9438-9e367f1be852","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b60|S167|80cddbe2 zombie age_min=851 notional=$45.00 occ=CELH260724C00029000 action=error:{"bid":"0.37","buy_limit_price":"0.4","code":40310000,"existing_order_id":"3dc8b475-76d1-4e4f-9438-9e367f1be852","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b32|S167|c2eb5ce9 zombie age_min=851 notional=$45.00 occ=CELH260724C00029000 action=error:{"bid":"0.37","buy_limit_price":"0.4","code":40310000,"existing_order_id":"3dc8b475-76d1-4e4f-9438-9e367f1be852","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b4|S167|7789022c zombie age_min=851 notional=$45.00 occ=CELH260724C00029000 action=error:{"bid":"0.37","buy_limit_price":"0.4","code":40310000,"existing_order_id":"3dc8b475-76d1-4e4f-9438-9e367f1be852","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b120|S165|22368d8c zombie age_min=851 notional=$45.00 occ=CELH260724C00029000 action=error:{"bid":"0.37","buy_limit_price":"0.4","code":40310000,"existing_order_id":"3dc8b475-76d1-4e4f-9438-9e367f1be852","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b92|S165|822f677b zombie age_min=851 notional=$45.00 occ=CELH260724C00029000 action=error:{"bid":"0.37","buy_limit_price":"0.4","code":40310000,"existing_order_id":"3dc8b475-76d1-4e4f-9438-9e367f1be852","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b64|S165|0975fc64 zombie age_min=851 notional=$45.00 occ=CELH260724C00029000 action=error:{"bid":"0.37","buy_limit_price":"0.4","code":40310000,"existing_order_id":"3dc8b475-76d1-4e4f-9438-9e367f1be852","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b36|S165|c1d6900b zombie age_min=851 notional=$45.00 occ=CELH260724C00029000 action=error:{"bid":"0.37","buy_limit_price":"0.4","code":40310000,"existing_order_id":"3dc8b475-76d1-4e4f-9438-9e367f1be852","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b125|S166|2af958fa zombie age_min=851 notional=$67.00 occ=HAL260731C00033500 action=error:{"bid":"0.57","buy_limit_price":"0.62","code":40310000,"existing_order_id":"69d23a87-8b5f-4ca3-8462-e9cc213fde79","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b97|S166|2ec5522c zombie age_min=851 notional=$67.00 occ=HAL260731C00033500 action=error:{"bid":"0.57","buy_limit_price":"0.62","code":40310000,"existing_order_id":"69d23a87-8b5f-4ca3-8462-e9cc213fde79","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b69|S166|3d4ec554 zombie age_min=851 notional=$67.00 occ=HAL260731C00033500 action=error:{"bid":"0.57","buy_limit_price":"0.62","code":40310000,"existing_order_id":"69d23a87-8b5f-4ca3-8462-e9cc213fde79","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b41|S166|0ff072e1 zombie age_min=851 notional=$67.00 occ=HAL260731C00033500 action=error:{"bid":"0.57","buy_limit_price":"0.62","code":40310000,"existing_order_id":"69d23a87-8b5f-4ca3-8462-e9cc213fde79","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b13|S166|4c38fb81 zombie age_min=851 notional=$67.00 occ=HAL260731C00033500 action=error:{"bid":"0.57","buy_limit_price":"0.62","code":40310000,"existing_order_id":"69d23a87-8b5f-4ca3-8462-e9cc213fde79","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b137|S168|768617ba zombie age_min=851 notional=$60.00 occ=HAL260724C00033000 action=submitted:17eaf66c-2886-46df-9972-8aa2a2eb3b90
  FLAG b109|S168|66ac7429 zombie age_min=851 notional=$60.00 occ=HAL260724C00033000 action=submitted:70c2a897-d037-43e1-8f0c-16024fed4c33
  FLAG b81|S168|56591cfd zombie age_min=851 notional=$60.00 occ=HAL260724C00033000 action=submitted:34bc377a-b908-47a6-890b-575a23b035c6
  FLAG b53|S168|6c111a4a zombie age_min=851 notional=$60.00 occ=HAL260724C00033000 action=submitted:ebc8ac8b-f254-47d3-abb5-ddcba3835fa7
  FLAG b25|S168|b83eaeaf zombie age_min=851 notional=$60.00 occ=HAL260724C00033000 action=submitted:33b0f7f3-60a5-487f-903b-87d347fa7927
  FLAG b121|S165|5c9cd978 zombie age_min=851 notional=$63.00 occ=HAL260724C00033000 action=submitted:35d3eec8-033e-478a-a5a5-0cf8d4cbb534
  FLAG b93|S165|08f1e48d zombie age_min=851 notional=$63.00 occ=HAL260724C00033000 action=submitted:f8fba983-ea06-4a75-a8c7-6d4fef19f71c
  FLAG b65|S165|41deb24d zombie age_min=851 notional=$63.00 occ=HAL260724C00033000 action=submitted:60260757-a6c5-492b-b9ea-57559a225011
  FLAG b37|S165|6c2ae9a4 zombie age_min=851 notional=$63.00 occ=HAL260724C00033000 action=submitted:29988549-34e2-4933-926f-47cf82816d25
  FLAG b9|S165|9b4dbad3 zombie age_min=851 notional=$63.00 occ=HAL260724C00033000 action=submitted:13c444b2-7510-44b6-8067-ced6e1c451dd
  FLAG b128|S163|d34d81a4 zombie age_min=851 notional=$74.00 occ=HAL260731C00033500 action=error:{"bid":"0.57","buy_limit_price":"0.62","code":40310000,"existing_order_id":"69d23a87-8b5f-4ca3-8462-e9cc213fde79","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b100|S163|a18cc90d zombie age_min=851 notional=$74.00 occ=HAL260731C00033500 action=error:{"bid":"0.57","buy_limit_price":"0.62","code":40310000,"existing_order_id":"69d23a87-8b5f-4ca3-8462-e9cc213fde79","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b72|S163|0aef0dcf zombie age_min=851 notional=$74.00 occ=HAL260731C00033500 action=error:{"bid":"0.57","buy_limit_price":"0.62","code":40310000,"existing_order_id":"69d23a87-8b5f-4ca3-8462-e9cc213fde79","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b44|S163|90d927e2 zombie age_min=851 notional=$74.00 occ=HAL260731C00033500 action=error:{"bid":"0.57","buy_limit_price":"0.62","code":40310000,"existing_order_id":"69d23a87-8b5f-4ca3-8462-e9cc213fde79","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b16|S163|c4f76708 zombie age_min=851 notional=$74.00 occ=HAL260731C00033500 action=error:{"bid":"0.57","buy_limit_price":"0.62","code":40310000,"existing_order_id":"69d23a87-8b5f-4ca3-8462-e9cc213fde79","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b136|S168|9d725e90 zombie age_min=851 notional=$63.00 occ=HAL260724C00033000 action=submitted:1285ad1b-44e6-469f-9dad-1480aa88aedc
  FLAG b108|S168|ebe4dcd2 zombie age_min=851 notional=$63.00 occ=HAL260724C00033000 action=submitted:ac484f90-936e-42f3-b6df-1e9ed3f96316
  FLAG b80|S168|4e2ea213 zombie age_min=851 notional=$63.00 occ=HAL260724C00033000 action=submitted:d68acb8b-865a-490b-9ce0-5e3f76a6d36c
  FLAG b52|S168|7af94f44 zombie age_min=851 notional=$63.00 occ=HAL260724C00033000 action=submitted:3413ddc5-54f4-4965-8d3e-38a5ab47b9e3
  FLAG b24|S168|88bfd109 zombie age_min=851 notional=$63.00 occ=HAL260724C00033000 action=submitted:f309168e-f604-4c5d-bb28-996dac92117b
  FLAG b132|S164|0b52d9aa zombie age_min=851 notional=$8.00 occ=HAL260724C00035000 action=submitted:3c14972f-652e-4e53-a062-4ecb66c08e41
  FLAG b104|S164|ed121b0c zombie age_min=851 notional=$8.00 occ=HAL260724C00035000 action=submitted:e19c0cec-6235-4679-8647-89a44f3dae66
  FLAG b76|S164|52c09cd9 zombie age_min=851 notional=$8.00 occ=HAL260724C00035000 action=submitted:dfdff98a-d823-461a-8d54-570afabb3d07
  FLAG b48|S164|a439876a zombie age_min=851 notional=$8.00 occ=HAL260724C00035000 action=submitted:7affeb13-4670-43f3-9ac7-b15f070025d2
  FLAG b20|S164|1935ddaa zombie age_min=851 notional=$8.00 occ=HAL260724C00035000 action=submitted:1ba5d3d2-c47b-4eff-97b1-e740b2f569ac
  FLAG b8|S165|b5373263 zombie age_min=851 notional=$45.00 occ=CELH260724C00029000 action=error:{"bid":"0.37","buy_limit_price":"0.4","code":40310000,"existing_order_id":"3dc8b475-76d1-4e4f-9438-9e367f1be852","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
options_reconcile: done
Layout: controlled:140:c000_s173_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:140:c000_s173_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      140
=== options_morning_bot (PAPER) 2026-07-21T10:10:39.976710-04:00 ===

[Run context]
Paper auth OK — equity $130601.75, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 335 signal(s); top: ['S165:ACN', 'S165:ADBE', 'S165:A', 'S165:BR', 'S165:CSGP', 'S165:DHR', 'S165:EFX', 'S165:FDS']
Paper lab: $130540 broker equity -> 140 bucket(s) ($500 virtual each, unlimited paper)
  All bucket slots blocked or closed for today's signals — skip entry loop.
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $130,601.75                             |
|  Signals this run              335                                     |
|  Orders submitted (session)    30                                      |
|  Orders filled today (ledger)  45                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             25                                      |
|  Broker option positions       3                                       |
|  Pending orders                10                                      |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=246  buckets=22  win=32%                             |
|  Returns   avg=-1.1%  med=-35.3%  p10=-66.2%  p90=+84.5%               |
|  Realized  $+4,917.13                                                  |
|  Raw incl dropped  trades=725  real=$+2,618.58                         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b51  c051_s164_w4_1120_  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  c091_s167_w4_1120_  2 100% +222.0 +222.0 +247.0 $   +293         |
|  b31  c031_s173_w4_1120_  2 100% +145.5 +145.5 +175.8 $   +192         |
|  b28  c028_s173_w1_0928_ 21  76% +49.4 +80.0 +102.0 $   +556           |
|  b58  c058_s173_w3_1045_  1 100% +59.1 +59.1 +59.1 $    +25            |
|  b56  c056_s173_w1_0928_  1 100% +47.7 +47.7 +47.7 $    +21            |
|  b57  c057_s173_w2_1005_  1 100% +47.7 +47.7 +47.7 $    +21            |
|  b89  c089_s167_w2_1005_  9  56% +84.4 +30.9 +790.0 $    +45           |
|  ... 14 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b9   c009_s165_w2_1005_  6   0% -76.2 -78.1 -92.7 $   -261       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (10)                                                   |
+------------------------------------------------------------------------+
|  Top groups                    S167:CELH(5), S163:HAL(5)               |
+------------------------------------------------------------------------+
|  b5   S167 CELH     limit=0.40                                         |
|  b33  S167 CELH     limit=0.40                                         |
|  b61  S167 CELH     limit=0.40                                         |
|  b89  S167 CELH     limit=0.40                                         |
|  b117 S167 CELH     limit=0.40                                         |
|  ... 5 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (3)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  HAL260731C00033500           10    -19.1%   $   -135.00               |
|  CELH260724C00029000          10    -22.2%   $   -100.00               |
|  LULU260724C00121000           5    -29.2%   $    -95.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-21.log
elapsed=48.8s reconcile=1.89s cancel=0.02s manage=0.34s scan=44.65s entries=0.14s
STATUS: options_morning_bot run complete (PAPER) elapsed=48.8s. run=#4551 https://github.com/28twagg-ops/TradingBot/actions/runs/29837823135
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 3.0% (22/725)
# Options signal frequency

_Generated 2026-07-21T10:11:31.822403_

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
| 2026-07-21 |    1 |    1 |    1 |    1 |    1 |    1 |    0 |    0 |     6 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 1 | 1 | 1.0 | ~38 active signal-days |
| S164 | 1 | 1 | 1.0 | ~38 active signal-days |
| S165 | 15 | 8 | 1.9 | ~20 active signal-days |
| S166 | 1 | 1 | 1.0 | ~38 active signal-days |
| S167 | 1 | 1 | 1.0 | ~38 active signal-days |
| S168 | 1 | 1 | 1.0 | ~38 active signal-days |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 10 | 1 |
| S164 | 15 | 1 |
| S165 | 1407 | 15 |
| S166 | 10 | 1 |
| S167 | 10 | 1 |
| S168 | 15 | 1 |
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
| 2026-07-21 |   10 |   15 |   98 |   10 |   10 |   15 |  118 |   48 |   324 |

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
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    25 | INFO |
| Total closed lots           |   295 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=481.63 router=CONFIRMED leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---

## Run 20260721T141538Z

- UTC timestamp: `20260721T141538Z`
- GitHub run: [#4552](https://github.com/28twagg-ops/TradingBot/actions/runs/29838204113)
- Run id: `29838204113`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`64s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-21T10:15:42.361242-04:00","date":"2026-07-21","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":58.7,"phases_s":{"reconcile":2.21,"cancel":0.02,"manage":0.2,"scan":54.59,"entries":0.07,"reconcile2":1.38},"signals":335,"placed":0,"equity":130887.35,"open_positions":2,"pending_orders":0,"open_lots":20,"submitted_today":30,"filled_today":55,"unattributed_contracts":0,"top_signals":["S165:ACN","S165:ADBE","S165:A","S165:BR","S165:CSGP","S165:DHR","S165:EFX","S165:FDS"],"github_run":"4552","github_run_id":"29838204113","status":"ok"}
```

### Live bot full output

```text
14:15:39  INFO      Mode: exits
14:15:39  INFO        Daily log -> logs/daily/2026-07-21.md
14:15:39  INFO        Daily log reconciled -> logs/daily/2026-07-21.md (4 ledger rows)
14:15:39  INFO        place_all_stops: checking 5 positions...
14:15:39  INFO        STOP already live BEN @ $32.36
14:15:39  INFO        STOP skipped BIIB: fractional (0.4766 shares) — software exit will handle it
14:15:39  INFO        STOP already live CNP @ $42.71
14:15:39  INFO        STOP skipped DUK: fractional (0.7693 shares) — software exit will handle it
14:15:39  INFO        STOP skipped TPR: fractional (0.6841 shares) — software exit will handle it
14:15:39  INFO        [positions] 5/5 (5 valid)
14:15:39  INFO        Daily log -> logs/daily/2026-07-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:15 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $481.60|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CNP  P&L -0.3%  $-0.28                                            HOLD|
|  DUK  P&L +0.2%  $+0.20                                            HOLD|
|  BIIB  P&L +0.6%  $+0.54                                           HOLD|
|  BEN  P&L +0.6%  $+0.43                                            HOLD|
|  TPR  P&L +1.1%  $+1.03                                            HOLD|
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
  open_lots=25 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=5
  zombies_flagged=25
  FLAG b116|S167|8d992c06 zombie age_min=856 notional=$45.00 occ=CELH260724C00029000 action=error:{"bid":"0.35","buy_limit_price":"0.4","code":40310000,"existing_order_id":"3dc8b475-76d1-4e4f-9438-9e367f1be852","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b88|S167|35a13654 zombie age_min=856 notional=$45.00 occ=CELH260724C00029000 action=error:{"bid":"0.35","buy_limit_price":"0.4","code":40310000,"existing_order_id":"3dc8b475-76d1-4e4f-9438-9e367f1be852","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b60|S167|80cddbe2 zombie age_min=856 notional=$45.00 occ=CELH260724C00029000 action=error:{"bid":"0.35","buy_limit_price":"0.4","code":40310000,"existing_order_id":"3dc8b475-76d1-4e4f-9438-9e367f1be852","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b32|S167|c2eb5ce9 zombie age_min=856 notional=$45.00 occ=CELH260724C00029000 action=error:{"bid":"0.35","buy_limit_price":"0.4","code":40310000,"existing_order_id":"3dc8b475-76d1-4e4f-9438-9e367f1be852","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b4|S167|7789022c zombie age_min=856 notional=$45.00 occ=CELH260724C00029000 action=error:{"bid":"0.35","buy_limit_price":"0.4","code":40310000,"existing_order_id":"3dc8b475-76d1-4e4f-9438-9e367f1be852","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b120|S165|22368d8c zombie age_min=856 notional=$45.00 occ=CELH260724C00029000 action=error:{"bid":"0.35","buy_limit_price":"0.4","code":40310000,"existing_order_id":"3dc8b475-76d1-4e4f-9438-9e367f1be852","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b92|S165|822f677b zombie age_min=856 notional=$45.00 occ=CELH260724C00029000 action=error:{"bid":"0.35","buy_limit_price":"0.4","code":40310000,"existing_order_id":"3dc8b475-76d1-4e4f-9438-9e367f1be852","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b64|S165|0975fc64 zombie age_min=856 notional=$45.00 occ=CELH260724C00029000 action=error:{"bid":"0.35","buy_limit_price":"0.4","code":40310000,"existing_order_id":"3dc8b475-76d1-4e4f-9438-9e367f1be852","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b36|S165|c1d6900b zombie age_min=856 notional=$45.00 occ=CELH260724C00029000 action=error:{"bid":"0.35","buy_limit_price":"0.4","code":40310000,"existing_order_id":"3dc8b475-76d1-4e4f-9438-9e367f1be852","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b125|S166|2af958fa zombie age_min=856 notional=$67.00 occ=HAL260731C00033500 action=submitted:62974a10-b9ca-4279-8845-115551a86952
  FLAG b97|S166|2ec5522c zombie age_min=856 notional=$67.00 occ=HAL260731C00033500 action=submitted:cbe3a675-47e0-454f-a446-f2f7155d5154
  FLAG b69|S166|3d4ec554 zombie age_min=856 notional=$67.00 occ=HAL260731C00033500 action=submitted:d87a6782-bf4a-413c-b234-93d6d55d4e63
  FLAG b41|S166|0ff072e1 zombie age_min=856 notional=$67.00 occ=HAL260731C00033500 action=submitted:b46afa71-8193-445e-a190-130d2d5c4c2e
  FLAG b13|S166|4c38fb81 zombie age_min=856 notional=$67.00 occ=HAL260731C00033500 action=submitted:e5697184-6b23-4d9b-aa86-6844462a1f92
  FLAG b128|S163|d34d81a4 zombie age_min=856 notional=$74.00 occ=HAL260731C00033500 action=submitted:3e483ded-8cf2-4107-b90d-0e21bec164c7
  FLAG b100|S163|a18cc90d zombie age_min=856 notional=$74.00 occ=HAL260731C00033500 action=submitted:c98a0fed-e553-4150-a90d-72ae789a2b60
  FLAG b72|S163|0aef0dcf zombie age_min=856 notional=$74.00 occ=HAL260731C00033500 action=submitted:cf6d49e3-b1a2-46ba-b8d3-5d7218368faa
  FLAG b44|S163|90d927e2 zombie age_min=856 notional=$74.00 occ=HAL260731C00033500 action=submitted:ae60e971-25a8-4a8b-974e-2387b00d1d44
  FLAG b16|S163|c4f76708 zombie age_min=856 notional=$74.00 occ=HAL260731C00033500 action=submitted:4beea6be-35c5-46ec-9c73-d968158ebcc8
  FLAG b8|S165|b5373263 zombie age_min=856 notional=$45.00 occ=CELH260724C00029000 action=error:{"bid":"0.35","buy_limit_price":"0.4","code":40310000,"existing_order_id":"3dc8b475-76d1-4e4f-9438-9e367f1be852","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b133|S164|8f20b7ec zombie age_min=856 notional=$65.00 occ=LULU260724C00121000 action=submitted:9ee9e8d9-b2b3-4985-afc7-53a79bed2c05
  FLAG b105|S164|d90c7c9a zombie age_min=856 notional=$65.00 occ=LULU260724C00121000 action=submitted:1ff96ecd-7895-451d-8433-345754b40992
  FLAG b77|S164|de21e2cf zombie age_min=856 notional=$65.00 occ=LULU260724C00121000 action=submitted:8432d43e-48d0-4f5c-8f07-2e2965ac7797
  FLAG b49|S164|0445d822 zombie age_min=856 notional=$65.00 occ=LULU260724C00121000 action=submitted:86a38908-a6d6-4296-a556-5271ab8bec5d
  FLAG b21|S164|8eef877f zombie age_min=856 notional=$65.00 occ=LULU260724C00121000 action=submitted:49f2dd6a-8c32-46ec-9403-f97d9863d80b
options_reconcile: done
Layout: controlled:140:c000_s173_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:140:c000_s173_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      140
=== options_morning_bot (PAPER) 2026-07-21T10:15:42.361242-04:00 ===

[Run context]
Paper auth OK — equity $130887.35, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 335 signal(s); top: ['S165:ACN', 'S165:ADBE', 'S165:A', 'S165:BR', 'S165:CSGP', 'S165:DHR', 'S165:EFX', 'S165:FDS']
Paper lab: $130663 broker equity -> 140 bucket(s) ($500 virtual each, unlimited paper)
  All bucket slots blocked or closed for today's signals — skip entry loop.
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $130,887.35                             |
|  Signals this run              335                                     |
|  Orders submitted (session)    30                                      |
|  Orders filled today (ledger)  55                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             20                                      |
|  Broker option positions       2                                       |
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
|  OPEN OPTIONS (2)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  HAL260731C00033500            5    -26.1%   $    -88.33               |
|  CELH260724C00029000          15    -12.3%   $    -80.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-21.log
elapsed=58.7s reconcile=2.21s cancel=0.02s manage=0.2s scan=54.59s entries=0.07s
STATUS: options_morning_bot run complete (PAPER) elapsed=58.7s. run=#4552 https://github.com/28twagg-ops/TradingBot/actions/runs/29838204113
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 2.9% (22/762)
# Options signal frequency

_Generated 2026-07-21T10:16:44.225197_

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
| 2026-07-21 |    1 |    1 |    1 |    1 |    1 |    1 |    0 |    0 |     6 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 1 | 1 | 1.0 | ~38 active signal-days |
| S164 | 1 | 1 | 1.0 | ~38 active signal-days |
| S165 | 15 | 8 | 1.9 | ~20 active signal-days |
| S166 | 1 | 1 | 1.0 | ~38 active signal-days |
| S167 | 1 | 1 | 1.0 | ~38 active signal-days |
| S168 | 1 | 1 | 1.0 | ~38 active signal-days |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 15 | 1 |
| S164 | 15 | 1 |
| S165 | 1407 | 15 |
| S166 | 10 | 1 |
| S167 | 15 | 1 |
| S168 | 15 | 1 |
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
| 2026-07-21 |   15 |   15 |   98 |   10 |   15 |   15 |  118 |   48 |   334 |

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
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |    20 | INFO |
| Total closed lots           |   297 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=481.6 router=CONFIRMED leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---

## Run 20260721T142042Z

- UTC timestamp: `20260721T142042Z`
- GitHub run: [#4553](https://github.com/28twagg-ops/TradingBot/actions/runs/29838598174)
- Run id: `29838598174`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`44s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-21T10:20:47.703481-04:00","date":"2026-07-21","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":38.5,"phases_s":{"reconcile":1.29,"cancel":0.04,"manage":0.04,"scan":36.69,"entries":0.11},"signals":335,"placed":0,"equity":131188.85,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":30,"filled_today":55,"unattributed_contracts":0,"top_signals":["S165:ACN","S165:ADBE","S165:A","S165:BR","S165:CSGP","S165:DHR","S165:EFX","S165:FDS"],"github_run":"4553","github_run_id":"29838598174","status":"ok"}
```

### Live bot full output

```text
14:20:43  INFO      Mode: exits
14:20:44  INFO        Daily log -> logs/daily/2026-07-21.md
14:20:44  INFO        Daily log reconciled -> logs/daily/2026-07-21.md (4 ledger rows)
14:20:44  INFO        place_all_stops: checking 5 positions...
14:20:44  INFO        STOP already live BEN @ $32.36
14:20:44  INFO        STOP skipped BIIB: fractional (0.4766 shares) — software exit will handle it
14:20:44  INFO        STOP skipped CNP: fractional (0.2410 shares) — software exit will handle it
14:20:44  INFO        STOP skipped DUK: fractional (0.7693 shares) — software exit will handle it
14:20:44  INFO        STOP skipped TPR: fractional (0.6841 shares) — software exit will handle it
14:20:44  INFO        [positions] 5/5 (5 valid)
14:20:45  INFO        Daily log -> logs/daily/2026-07-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $480.84|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CNP  P&L -0.5%  $-0.05                                            HOLD|
|  DUK  P&L +0.0%  $+0.02                                            HOLD|
|  BEN  P&L +0.5%  $+0.33                                            HOLD|
|  BIIB  P&L +0.6%  $+0.55                                           HOLD|
|  TPR  P&L +0.8%  $+0.74                                            HOLD|
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
  open_lots=20 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=4
  zombies_flagged=20
  FLAG b116|S167|8d992c06 zombie age_min=861 notional=$45.00 occ=CELH260724C00029000 action=submitted:b141fcfa-3ce0-49f9-8d27-832821efae24
  FLAG b88|S167|35a13654 zombie age_min=861 notional=$45.00 occ=CELH260724C00029000 action=submitted:9fb07c31-d98c-40b8-8b5f-bafc174fe08a
  FLAG b60|S167|80cddbe2 zombie age_min=861 notional=$45.00 occ=CELH260724C00029000 action=submitted:26eaeb6a-17be-4546-bfa7-3749799a5165
  FLAG b32|S167|c2eb5ce9 zombie age_min=861 notional=$45.00 occ=CELH260724C00029000 action=submitted:ffb159df-84bb-41d5-bc80-8a3514b91009
  FLAG b4|S167|7789022c zombie age_min=861 notional=$45.00 occ=CELH260724C00029000 action=submitted:b8eb13d7-41ef-4f16-844f-b8c27e3e3cd7
  FLAG b120|S165|22368d8c zombie age_min=861 notional=$45.00 occ=CELH260724C00029000 action=submitted:7281d031-818e-44d4-a373-40444498c192
  FLAG b92|S165|822f677b zombie age_min=861 notional=$45.00 occ=CELH260724C00029000 action=submitted:59e2ee9e-7675-4c79-8dcc-18a16d79a5b1
  FLAG b64|S165|0975fc64 zombie age_min=861 notional=$45.00 occ=CELH260724C00029000 action=submitted:c7fded7c-5c64-451a-a369-fad2e41b92b5
  FLAG b36|S165|c1d6900b zombie age_min=861 notional=$45.00 occ=CELH260724C00029000 action=submitted:73ca0955-b3f4-409f-bd85-4fdefa75e11f
  FLAG b8|S165|4de70e59 zombie age_min=861 notional=$45.00 occ=CELH260724C00029000 action=submitted:7bba6ce6-1e80-451e-9610-db0b1f3f96d7
  FLAG b117|S167|dd7c430d zombie age_min=861 notional=$40.00 occ=CELH260724C00029000 action=submitted:c4c35bc7-da4c-4f95-8db4-2854e8e277ea
  FLAG b89|S167|0f45335a zombie age_min=861 notional=$40.00 occ=CELH260724C00029000 action=submitted:329b7811-1e98-4550-9cf9-9496c4cd7fcb
  FLAG b61|S167|a8772b50 zombie age_min=861 notional=$40.00 occ=CELH260724C00029000 action=submitted:d84e5abd-5b2e-4b8a-901a-f7784d86c0ec
  FLAG b33|S167|da2cf5b8 zombie age_min=861 notional=$40.00 occ=CELH260724C00029000 action=submitted:386e4dbc-e8d5-4588-9544-7d4ea767c193
  FLAG b5|S167|ac848a44 zombie age_min=861 notional=$40.00 occ=CELH260724C00029000 action=submitted:10a2b512-cc1c-4eb8-adf0-c3d97f69c6b1
  FLAG b128|S163|f2f0efa3 zombie age_min=861 notional=$74.00 occ=HAL260731C00033500 action=submitted:b8d21851-3e05-45d4-9422-4f5fde259778
  FLAG b100|S163|bf945669 zombie age_min=861 notional=$74.00 occ=HAL260731C00033500 action=submitted:9ae9c8a0-0cc1-41d8-8aa4-a7def65ae8be
  FLAG b72|S163|3e05dfe9 zombie age_min=861 notional=$74.00 occ=HAL260731C00033500 action=submitted:37082939-b801-484d-9b84-96cd4c91485b
  FLAG b44|S163|808ddbcc zombie age_min=861 notional=$74.00 occ=HAL260731C00033500 action=submitted:5b52d2d4-7924-4dfa-8a4e-512bab43201c
  FLAG b16|S163|5da55a21 zombie age_min=861 notional=$74.00 occ=HAL260731C00033500 action=submitted:c79eba52-699c-4f5e-970b-ae8e3a094ef1
options_reconcile: done
Layout: controlled:140:c000_s173_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:140:c000_s173_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      140
=== options_morning_bot (PAPER) 2026-07-21T10:20:47.703481-04:00 ===

[Run context]
Paper auth OK — equity $131188.85, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 335 signal(s); top: ['S165:ACN', 'S165:ADBE', 'S165:A', 'S165:BR', 'S165:CSGP', 'S165:DHR', 'S165:EFX', 'S165:FDS']
Paper lab: $131153 broker equity -> 140 bucket(s) ($500 virtual each, unlimited paper)
  All bucket slots blocked or closed for today's signals — skip entry loop.
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $131,188.85                             |
|  Signals this run              335                                     |
|  Orders submitted (session)    30                                      |
|  Orders filled today (ledger)  55                                      |
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
elapsed=38.5s reconcile=1.29s cancel=0.04s manage=0.04s scan=36.69s entries=0.11s
STATUS: options_morning_bot run complete (PAPER) elapsed=38.5s. run=#4553 https://github.com/28twagg-ops/TradingBot/actions/runs/29838598174
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 2.9% (22/762)
# Options signal frequency

_Generated 2026-07-21T10:21:29.268512_

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
| 2026-07-21 |    1 |    1 |    1 |    1 |    1 |    1 |    0 |    0 |     6 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 1 | 1 | 1.0 | ~38 active signal-days |
| S164 | 1 | 1 | 1.0 | ~38 active signal-days |
| S165 | 15 | 8 | 1.9 | ~20 active signal-days |
| S166 | 1 | 1 | 1.0 | ~38 active signal-days |
| S167 | 1 | 1 | 1.0 | ~38 active signal-days |
| S168 | 1 | 1 | 1.0 | ~38 active signal-days |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 15 | 1 |
| S164 | 15 | 1 |
| S165 | 1407 | 15 |
| S166 | 10 | 1 |
| S167 | 15 | 1 |
| S168 | 15 | 1 |
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
| 2026-07-21 |   15 |   15 |   98 |   10 |   15 |   15 |  118 |   48 |   334 |

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
equity=480.84 router=CONFIRMED leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---

## Run 20260721T142541Z

- UTC timestamp: `20260721T142541Z`
- GitHub run: [#4554](https://github.com/28twagg-ops/TradingBot/actions/runs/29838995037)
- Run id: `29838995037`
- Live bot: exit=`0`, duration=`6s`
- Options bot: exit=`0`, duration=`44s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-21T10:25:49.019390-04:00","date":"2026-07-21","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":39.1,"phases_s":{"reconcile":1.52,"cancel":0.15,"manage":0.15,"scan":36.44,"entries":0.2},"signals":335,"placed":0,"equity":131380.85,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":30,"filled_today":55,"unattributed_contracts":0,"top_signals":["S165:ACN","S165:ADBE","S165:A","S165:BR","S165:CSGP","S165:DHR","S165:EFX","S165:FDS"],"github_run":"4554","github_run_id":"29838995037","status":"ok"}
```

### Live bot full output

```text
14:25:42  INFO      Mode: exits
14:25:43  INFO        Daily log -> logs/daily/2026-07-21.md
14:25:43  INFO        Daily log reconciled -> logs/daily/2026-07-21.md (4 ledger rows)
14:25:43  INFO        place_all_stops: checking 5 positions...
14:25:43  INFO        STOP already live BEN @ $32.36
14:25:43  INFO        STOP skipped BIIB: fractional (0.4766 shares) — software exit will handle it
14:25:43  INFO        STOP skipped CNP: fractional (0.2410 shares) — software exit will handle it
14:25:43  INFO        STOP skipped DUK: fractional (0.7693 shares) — software exit will handle it
14:25:43  INFO        STOP skipped TPR: fractional (0.6841 shares) — software exit will handle it
14:25:44  INFO        [positions] 5/5 (5 valid)
14:25:44  INFO        SELL MARKET [urgent] CNP closed
14:25:46  INFO        TX logged: SELL CNP  P&L -0.59%
14:25:47  INFO        Daily log -> logs/daily/2026-07-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:25 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $480.65|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CNP  P&L -0.6%  $-0.06                         EXIT: stop_loss (-0.6%)|
|  DUK  P&L +0.0%  $+0.04                                            HOLD|
|  TPR  P&L +0.4%  $+0.40                                            HOLD|
|  BEN  P&L +0.5%  $+0.35                                            HOLD|
|  BIIB  P&L +0.7%  $+0.70                                           HOLD|
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
|  CNP                                         -0.59%  (threshold -0.50%)|
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
  alpaca open sell orders=0 positions=2
  zombies_flagged=0
options_reconcile: done
Layout: controlled:140:c000_s173_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:140:c000_s173_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      140
=== options_morning_bot (PAPER) 2026-07-21T10:25:49.019390-04:00 ===

[Run context]
Paper auth OK — equity $131380.85, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 335 signal(s); top: ['S165:ACN', 'S165:ADBE', 'S165:A', 'S165:BR', 'S165:CSGP', 'S165:DHR', 'S165:EFX', 'S165:FDS']
Paper lab: $131339 broker equity -> 140 bucket(s) ($500 virtual each, unlimited paper)
  All bucket slots blocked or closed for today's signals — skip entry loop.
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $131,380.85                             |
|  Signals this run              335                                     |
|  Orders submitted (session)    30                                      |
|  Orders filled today (ledger)  55                                      |
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
elapsed=39.1s reconcile=1.52s cancel=0.15s manage=0.15s scan=36.44s entries=0.2s
STATUS: options_morning_bot run complete (PAPER) elapsed=39.1s. run=#4554 https://github.com/28twagg-ops/TradingBot/actions/runs/29838995037
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 2.9% (22/762)
# Options signal frequency

_Generated 2026-07-21T10:26:31.133156_

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
| 2026-07-21 |    1 |    1 |    1 |    1 |    1 |    1 |    0 |    0 |     6 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 1 | 1 | 1.0 | ~38 active signal-days |
| S164 | 1 | 1 | 1.0 | ~38 active signal-days |
| S165 | 15 | 8 | 1.9 | ~20 active signal-days |
| S166 | 1 | 1 | 1.0 | ~38 active signal-days |
| S167 | 1 | 1 | 1.0 | ~38 active signal-days |
| S168 | 1 | 1 | 1.0 | ~38 active signal-days |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 15 | 1 |
| S164 | 15 | 1 |
| S165 | 1407 | 15 |
| S166 | 10 | 1 |
| S167 | 15 | 1 |
| S168 | 15 | 1 |
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
| 2026-07-21 |   15 |   15 |   98 |   10 |   15 |   15 |  118 |   48 |   334 |

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
equity=480.66 router=CONFIRMED leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---

## Run 20260721T143037Z

- UTC timestamp: `20260721T143037Z`
- GitHub run: [#4555](https://github.com/28twagg-ops/TradingBot/actions/runs/29839389486)
- Run id: `29839389486`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`63s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-21T10:30:40.678178-04:00","date":"2026-07-21","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":58.1,"phases_s":{"reconcile":1.39,"cancel":0.1,"manage":0.09,"scan":55.92,"entries":0.14},"signals":335,"placed":0,"equity":131598.85,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":30,"filled_today":55,"unattributed_contracts":0,"top_signals":["S165:ACN","S165:ADBE","S165:A","S165:BR","S165:CSGP","S165:DHR","S165:EFX","S165:FDS"],"github_run":"4555","github_run_id":"29839389486","status":"ok"}
```

### Live bot full output

```text
14:30:38  INFO      Mode: exits
14:30:38  INFO        Daily log -> logs/daily/2026-07-21.md
14:30:38  INFO        Daily log reconciled -> logs/daily/2026-07-21.md (5 ledger rows)
14:30:38  INFO        place_all_stops: checking 4 positions...
14:30:38  INFO        STOP already live BEN @ $32.36
14:30:38  INFO        STOP skipped BIIB: fractional (0.4766 shares) — software exit will handle it
14:30:38  INFO        STOP skipped DUK: fractional (0.7693 shares) — software exit will handle it
14:30:38  INFO        STOP skipped TPR: fractional (0.6841 shares) — software exit will handle it
14:30:38  INFO        [positions] 4/4 (4 valid)
14:30:39  INFO        Daily log -> logs/daily/2026-07-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:30 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $480.33|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  DUK  P&L +0.2%  $+0.18                                            HOLD|
|  TPR  P&L +0.2%  $+0.22                                            HOLD|
|  BIIB  P&L +0.3%  $+0.33                                           HOLD|
|  BEN  P&L +0.6%  $+0.41                                            HOLD|
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
  alpaca open sell orders=0 positions=2
  zombies_flagged=0
options_reconcile: done
Layout: controlled:140:c000_s173_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:140:c000_s173_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      140
=== options_morning_bot (PAPER) 2026-07-21T10:30:40.678178-04:00 ===

[Run context]
Paper auth OK — equity $131598.85, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 335 signal(s); top: ['S165:ACN', 'S165:ADBE', 'S165:A', 'S165:BR', 'S165:CSGP', 'S165:DHR', 'S165:EFX', 'S165:FDS']
Paper lab: $131555 broker equity -> 140 bucket(s) ($500 virtual each, unlimited paper)
  All bucket slots blocked or closed for today's signals — skip entry loop.
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $131,598.85                             |
|  Signals this run              335                                     |
|  Orders submitted (session)    30                                      |
|  Orders filled today (ledger)  55                                      |
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
elapsed=58.1s reconcile=1.39s cancel=0.1s manage=0.09s scan=55.92s entries=0.14s
STATUS: options_morning_bot run complete (PAPER) elapsed=58.1s. run=#4555 https://github.com/28twagg-ops/TradingBot/actions/runs/29839389486
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 2.9% (22/762)
# Options signal frequency

_Generated 2026-07-21T10:31:41.850281_

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
| 2026-07-21 |    1 |    1 |    1 |    1 |    1 |    1 |    0 |    0 |     6 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 1 | 1 | 1.0 | ~38 active signal-days |
| S164 | 1 | 1 | 1.0 | ~38 active signal-days |
| S165 | 15 | 8 | 1.9 | ~20 active signal-days |
| S166 | 1 | 1 | 1.0 | ~38 active signal-days |
| S167 | 1 | 1 | 1.0 | ~38 active signal-days |
| S168 | 1 | 1 | 1.0 | ~38 active signal-days |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 15 | 1 |
| S164 | 15 | 1 |
| S165 | 1407 | 15 |
| S166 | 10 | 1 |
| S167 | 15 | 1 |
| S168 | 15 | 1 |
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
| 2026-07-21 |   15 |   15 |   98 |   10 |   15 |   15 |  118 |   48 |   334 |

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
equity=480.33 router=CONFIRMED leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---

## Run 20260721T143538Z

- UTC timestamp: `20260721T143538Z`
- GitHub run: [#4556](https://github.com/28twagg-ops/TradingBot/actions/runs/29839787150)
- Run id: `29839787150`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`49s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-21T10:35:42.776636-04:00","date":"2026-07-21","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":43.6,"phases_s":{"reconcile":1.62,"cancel":0.15,"manage":0.15,"scan":40.76,"entries":0.24},"signals":335,"placed":0,"equity":131752.85,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":30,"filled_today":55,"unattributed_contracts":0,"top_signals":["S165:ACN","S165:ADBE","S165:A","S165:BR","S165:CSGP","S165:DHR","S165:EFX","S165:FDS"],"github_run":"4556","github_run_id":"29839787150","status":"ok"}
```

### Live bot full output

```text
14:35:39  INFO      Mode: exits
14:35:40  INFO        Daily log -> logs/daily/2026-07-21.md
14:35:40  INFO        Daily log reconciled -> logs/daily/2026-07-21.md (5 ledger rows)
14:35:40  INFO        place_all_stops: checking 4 positions...
14:35:40  INFO        STOP already live BEN @ $32.36
14:35:40  INFO        STOP skipped BIIB: fractional (0.4766 shares) — software exit will handle it
14:35:40  INFO        STOP skipped DUK: fractional (0.7693 shares) — software exit will handle it
14:35:40  INFO        STOP skipped TPR: fractional (0.6841 shares) — software exit will handle it
14:35:40  INFO        [positions] 4/4 (4 valid)
14:35:40  INFO        Daily log -> logs/daily/2026-07-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:35 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $479.84|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  DUK  P&L -0.2%  $-0.22                                            HOLD|
|  TPR  P&L +0.1%  $+0.05                                            HOLD|
|  BIIB  P&L +0.4%  $+0.36                                           HOLD|
|  BEN  P&L +0.6%  $+0.46                                            HOLD|
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
  alpaca open sell orders=0 positions=2
  zombies_flagged=0
options_reconcile: done
Layout: controlled:140:c000_s173_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:140:c000_s173_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      140
=== options_morning_bot (PAPER) 2026-07-21T10:35:42.776636-04:00 ===

[Run context]
Paper auth OK — equity $131676.85, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 335 signal(s); top: ['S165:ACN', 'S165:ADBE', 'S165:A', 'S165:BR', 'S165:CSGP', 'S165:DHR', 'S165:EFX', 'S165:FDS']
Paper lab: $131850 broker equity -> 140 bucket(s) ($500 virtual each, unlimited paper)
  All bucket slots blocked or closed for today's signals — skip entry loop.
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $131,752.85                             |
|  Signals this run              335                                     |
|  Orders submitted (session)    30                                      |
|  Orders filled today (ledger)  55                                      |
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
elapsed=43.6s reconcile=1.62s cancel=0.15s manage=0.15s scan=40.76s entries=0.24s
STATUS: options_morning_bot run complete (PAPER) elapsed=43.6s. run=#4556 https://github.com/28twagg-ops/TradingBot/actions/runs/29839787150
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 2.9% (22/762)
# Options signal frequency

_Generated 2026-07-21T10:36:29.558190_

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
| 2026-07-21 |    1 |    1 |    1 |    1 |    1 |    1 |    0 |    0 |     6 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 1 | 1 | 1.0 | ~38 active signal-days |
| S164 | 1 | 1 | 1.0 | ~38 active signal-days |
| S165 | 15 | 8 | 1.9 | ~20 active signal-days |
| S166 | 1 | 1 | 1.0 | ~38 active signal-days |
| S167 | 1 | 1 | 1.0 | ~38 active signal-days |
| S168 | 1 | 1 | 1.0 | ~38 active signal-days |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 15 | 1 |
| S164 | 15 | 1 |
| S165 | 1407 | 15 |
| S166 | 10 | 1 |
| S167 | 15 | 1 |
| S168 | 15 | 1 |
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
| 2026-07-21 |   15 |   15 |   98 |   10 |   15 |   15 |  118 |   48 |   334 |

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
equity=479.84 router=CONFIRMED leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---

## Run 20260721T144042Z

- UTC timestamp: `20260721T144042Z`
- GitHub run: [#4557](https://github.com/28twagg-ops/TradingBot/actions/runs/29840187036)
- Run id: `29840187036`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`44s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-21T10:40:46.575353-04:00","date":"2026-07-21","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":38.8,"phases_s":{"reconcile":1.28,"cancel":0.05,"manage":0.05,"scan":36.98,"entries":0.12},"signals":335,"placed":0,"equity":131902.85,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":30,"filled_today":55,"unattributed_contracts":0,"top_signals":["S165:ACN","S165:ADBE","S165:A","S165:BR","S165:CSGP","S165:DHR","S165:EFX","S165:FDS"],"github_run":"4557","github_run_id":"29840187036","status":"ok"}
```

### Live bot full output

```text
14:40:43  INFO      Mode: exits
14:40:44  INFO        Daily log -> logs/daily/2026-07-21.md
14:40:44  INFO        Daily log reconciled -> logs/daily/2026-07-21.md (5 ledger rows)
14:40:44  INFO        place_all_stops: checking 4 positions...
14:40:44  INFO        STOP already live BEN @ $32.36
14:40:44  INFO        STOP skipped BIIB: fractional (0.4766 shares) — software exit will handle it
14:40:44  INFO        STOP skipped DUK: fractional (0.7693 shares) — software exit will handle it
14:40:44  INFO        STOP skipped TPR: fractional (0.6841 shares) — software exit will handle it
14:40:44  INFO        [positions] 4/4 (4 valid)
14:40:44  INFO        Daily log -> logs/daily/2026-07-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:40 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $479.31|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  DUK  P&L -0.2%  $-0.18                                            HOLD|
|  TPR  P&L -0.1%  $-0.07                                            HOLD|
|  BIIB  P&L +0.1%  $+0.06                                           HOLD|
|  BEN  P&L +0.4%  $+0.31                                            HOLD|
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
  alpaca open sell orders=0 positions=2
  zombies_flagged=0
options_reconcile: done
Layout: controlled:140:c000_s173_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:140:c000_s173_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      140
=== options_morning_bot (PAPER) 2026-07-21T10:40:46.575353-04:00 ===

[Run context]
Paper auth OK — equity $131902.85, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 335 signal(s); top: ['S165:ACN', 'S165:ADBE', 'S165:A', 'S165:BR', 'S165:CSGP', 'S165:DHR', 'S165:EFX', 'S165:FDS']
Paper lab: $131765 broker equity -> 140 bucket(s) ($500 virtual each, unlimited paper)
  All bucket slots blocked or closed for today's signals — skip entry loop.
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $131,902.85                             |
|  Signals this run              335                                     |
|  Orders submitted (session)    30                                      |
|  Orders filled today (ledger)  55                                      |
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
elapsed=38.8s reconcile=1.28s cancel=0.05s manage=0.05s scan=36.98s entries=0.12s
STATUS: options_morning_bot run complete (PAPER) elapsed=38.8s. run=#4557 https://github.com/28twagg-ops/TradingBot/actions/runs/29840187036
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 2.9% (22/762)
# Options signal frequency

_Generated 2026-07-21T10:41:28.192929_

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
| 2026-07-21 |    1 |    1 |    1 |    1 |    1 |    1 |    0 |    0 |     6 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 1 | 1 | 1.0 | ~38 active signal-days |
| S164 | 1 | 1 | 1.0 | ~38 active signal-days |
| S165 | 15 | 8 | 1.9 | ~20 active signal-days |
| S166 | 1 | 1 | 1.0 | ~38 active signal-days |
| S167 | 1 | 1 | 1.0 | ~38 active signal-days |
| S168 | 1 | 1 | 1.0 | ~38 active signal-days |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 15 | 1 |
| S164 | 15 | 1 |
| S165 | 1407 | 15 |
| S166 | 10 | 1 |
| S167 | 15 | 1 |
| S168 | 15 | 1 |
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
| 2026-07-21 |   15 |   15 |   98 |   10 |   15 |   15 |  118 |   48 |   334 |

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
equity=479.31 router=CONFIRMED leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---

## Run 20260721T144541Z

- UTC timestamp: `20260721T144541Z`
- GitHub run: [#4558](https://github.com/28twagg-ops/TradingBot/actions/runs/29840600708)
- Run id: `29840600708`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`150s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-21T10:45:44.961103-04:00","date":"2026-07-21","mode":"entry+manage","header":"entry+manage (30 new)","elapsed_s":146.9,"phases_s":{"reconcile":1.29,"cancel":0.13,"manage":0.14,"scan":42.74,"entries":100.74,"reconcile2":1.35},"signals":335,"placed":30,"equity":132357.21,"open_positions":3,"pending_orders":19,"open_lots":11,"submitted_today":60,"filled_today":66,"unattributed_contracts":0,"top_signals":["S165:ACN","S165:ADBE","S165:A","S165:BR","S165:CSGP","S165:DHR","S165:EFX","S165:FDS"],"github_run":"4558","github_run_id":"29840600708","status":"ok"}
```

### Live bot full output

```text
14:45:42  INFO      Mode: exits
14:45:42  INFO        Daily log -> logs/daily/2026-07-21.md
14:45:42  INFO        Daily log reconciled -> logs/daily/2026-07-21.md (5 ledger rows)
14:45:42  INFO        place_all_stops: checking 4 positions...
14:45:42  INFO        STOP already live BEN @ $32.36
14:45:42  INFO        STOP skipped BIIB: fractional (0.4766 shares) — software exit will handle it
14:45:42  INFO        STOP skipped DUK: fractional (0.7693 shares) — software exit will handle it
14:45:42  INFO        STOP skipped TPR: fractional (0.6841 shares) — software exit will handle it
14:45:43  INFO        [positions] 4/4 (4 valid)
14:45:43  INFO        Daily log -> logs/daily/2026-07-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:45 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $479.45|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  DUK  P&L -0.3%  $-0.26                                            HOLD|
|  TPR  P&L +0.0%  $+0.04                                            HOLD|
|  BIIB  P&L +0.2%  $+0.16                                           HOLD|
|  BEN  P&L +0.5%  $+0.33                                            HOLD|
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
  alpaca open sell orders=0 positions=2
  zombies_flagged=0
options_reconcile: done
Layout: controlled:140:c000_s173_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:140:c000_s173_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      140
=== options_morning_bot (PAPER) 2026-07-21T10:45:44.961103-04:00 ===

[Run context]
Paper auth OK — equity $132357.21, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 335 signal(s); top: ['S165:ACN', 'S165:ADBE', 'S165:A', 'S165:BR', 'S165:CSGP', 'S165:DHR', 'S165:EFX', 'S165:FDS']
Paper lab: $132183 broker equity -> 140 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 435 no tradeable call, 1675 already attempted today, 1210 pending order
Placed 30 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $132,357.21                             |
|  Signals this run              335                                     |
|  Orders submitted (session)    60                                      |
|  Orders filled today (ledger)  66                                      |
|  Entries placed this run       30                                      |
|  Open virtual lots             11                                      |
|  Broker option positions       3                                       |
|  Pending orders                19                                      |
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
|  PENDING ORDERS (19)                                                   |
+------------------------------------------------------------------------+
|  Top groups                    S165:HAL(5), S167:LULU(5), S163:HAL(5)  |
+------------------------------------------------------------------------+
|  b10  S165 HAL      limit=0.52                                         |
|  b38  S165 HAL      limit=0.52                                         |
|  b66  S165 HAL      limit=0.52                                         |
|  b94  S165 HAL      limit=0.52                                         |
|  b122 S165 HAL      limit=0.52                                         |
|  ... 14 more pending order(s)                                          |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (3)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  HAL260731C00033500            5    -11.9%   $    -37.00               |
|  LULU260724C00120000           5     -9.0%   $    -30.00               |
|  HAL260724C00033000            1    -16.4%   $     -9.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-21.log
elapsed=146.9s reconcile=1.29s cancel=0.13s manage=0.14s scan=42.74s entries=100.74s
STATUS: options_morning_bot run complete (PAPER) elapsed=146.9s. run=#4558 https://github.com/28twagg-ops/TradingBot/actions/runs/29840600708
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 2.9% (22/762)
# Options signal frequency

_Generated 2026-07-21T10:48:13.548773_

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
| S163 | 20 | 1 |
| S164 | 21 | 2 |
| S165 | 1412 | 15 |
| S166 | 20 | 1 |
| S167 | 20 | 2 |
| S168 | 25 | 2 |
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
| 2026-07-21 |   20 |   21 |  103 |   20 |   20 |   25 |  118 |   48 |   375 |

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
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |    11 | INFO |
| Total closed lots           |   297 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=479.45 router=CONFIRMED leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---

## Run 20260721T145037Z

- UTC timestamp: `20260721T145037Z`
- GitHub run: [#4559](https://github.com/28twagg-ops/TradingBot/actions/runs/29841015729)
- Run id: `29841015729`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`48s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-21T10:50:42.301795-04:00","date":"2026-07-21","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":42.5,"phases_s":{"reconcile":1.67,"cancel":0.11,"manage":0.63,"scan":37.8,"entries":0.2,"reconcile2":1.69},"signals":335,"placed":0,"equity":131899.55,"open_positions":3,"pending_orders":15,"open_lots":15,"submitted_today":60,"filled_today":70,"unattributed_contracts":0,"top_signals":["S165:ACN","S165:ADBE","S165:A","S165:BR","S165:CSGP","S165:DHR","S165:EFX","S165:FDS"],"github_run":"4559","github_run_id":"29841015729","status":"ok"}
```

### Live bot full output

```text
14:50:38  INFO      Mode: exits
14:50:39  INFO        Daily log -> logs/daily/2026-07-21.md
14:50:39  INFO        Daily log reconciled -> logs/daily/2026-07-21.md (5 ledger rows)
14:50:39  INFO        place_all_stops: checking 4 positions...
14:50:39  INFO        STOP already live BEN @ $32.36
14:50:39  INFO        STOP skipped BIIB: fractional (0.4766 shares) — software exit will handle it
14:50:39  INFO        STOP skipped DUK: fractional (0.7693 shares) — software exit will handle it
14:50:39  INFO        STOP skipped TPR: fractional (0.6841 shares) — software exit will handle it
14:50:39  INFO        [positions] 4/4 (4 valid)
14:50:40  INFO        Daily log -> logs/daily/2026-07-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:50 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $479.27|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  DUK  P&L -0.3%  $-0.26                                            HOLD|
|  BIIB  P&L -0.1%  $-0.06                                           HOLD|
|  TPR  P&L +0.0%  $+0.03                                            HOLD|
|  BEN  P&L +0.5%  $+0.37                                            HOLD|
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
  open_lots=11 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=5
  zombies_flagged=11
  FLAG b138|S168|f0c03357 zombie age_min=891 notional=$67.00 occ=LULU260724C00120000 action=error:{"bid":"0.6","buy_limit_price":"0.64","code":40310000,"existing_order_id":"1cdce2da-8a90-42ba-aad7-6b07a5038594","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b110|S168|057cb1b4 zombie age_min=891 notional=$67.00 occ=LULU260724C00120000 action=error:{"bid":"0.6","buy_limit_price":"0.64","code":40310000,"existing_order_id":"1cdce2da-8a90-42ba-aad7-6b07a5038594","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b82|S168|62fa2554 zombie age_min=891 notional=$67.00 occ=LULU260724C00120000 action=error:{"bid":"0.6","buy_limit_price":"0.64","code":40310000,"existing_order_id":"1cdce2da-8a90-42ba-aad7-6b07a5038594","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b54|S168|727db7e6 zombie age_min=891 notional=$67.00 occ=LULU260724C00120000 action=error:{"bid":"0.6","buy_limit_price":"0.64","code":40310000,"existing_order_id":"1cdce2da-8a90-42ba-aad7-6b07a5038594","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b26|S168|b59bb7e4 zombie age_min=891 notional=$67.00 occ=LULU260724C00120000 action=error:{"bid":"0.6","buy_limit_price":"0.64","code":40310000,"existing_order_id":"1cdce2da-8a90-42ba-aad7-6b07a5038594","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b128|S163|cff92bc1 zombie age_min=891 notional=$74.00 occ=HAL260731C00033500 action=error:{"bid":"0.55","buy_limit_price":"0.58","code":40310000,"existing_order_id":"1cde3897-28bf-4dbc-bfad-b09cca33cf1e","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b100|S163|2ca8556f zombie age_min=891 notional=$74.00 occ=HAL260731C00033500 action=error:{"bid":"0.55","buy_limit_price":"0.58","code":40310000,"existing_order_id":"1cde3897-28bf-4dbc-bfad-b09cca33cf1e","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b72|S163|c2d411c4 zombie age_min=891 notional=$74.00 occ=HAL260731C00033500 action=error:{"bid":"0.55","buy_limit_price":"0.58","code":40310000,"existing_order_id":"1cde3897-28bf-4dbc-bfad-b09cca33cf1e","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b44|S163|eb68b97a zombie age_min=891 notional=$74.00 occ=HAL260731C00033500 action=error:{"bid":"0.55","buy_limit_price":"0.58","code":40310000,"existing_order_id":"1cde3897-28bf-4dbc-bfad-b09cca33cf1e","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b16|S163|b8eb90a2 zombie age_min=891 notional=$74.00 occ=HAL260731C00033500 action=error:{"bid":"0.55","buy_limit_price":"0.58","code":40310000,"existing_order_id":"1cde3897-28bf-4dbc-bfad-b09cca33cf1e","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b24|S168|7a251bc5 zombie age_min=891 notional=$63.00 occ=HAL260724C00033000 action=error:{"bid":"0.5","buy_limit_price":"0.52","code":40310000,"existing_order_id":"43580845-aebc-43b0-9c47-82b409c7295a","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
options_reconcile: done
Layout: controlled:140:c000_s173_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:140:c000_s173_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      140
=== options_morning_bot (PAPER) 2026-07-21T10:50:42.301795-04:00 ===

[Run context]
Paper auth OK — equity $131899.55, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 335 signal(s); top: ['S165:ACN', 'S165:ADBE', 'S165:A', 'S165:BR', 'S165:CSGP', 'S165:DHR', 'S165:EFX', 'S165:FDS']
Paper lab: $131874 broker equity -> 140 bucket(s) ($500 virtual each, unlimited paper)
  All bucket slots blocked or closed for today's signals — skip entry loop.
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $131,899.55                             |
|  Signals this run              335                                     |
|  Orders submitted (session)    60                                      |
|  Orders filled today (ledger)  70                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             15                                      |
|  Broker option positions       3                                       |
|  Pending orders                15                                      |
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
|  PENDING ORDERS (15)                                                   |
+------------------------------------------------------------------------+
|  Top groups                    S165:HAL(5), S167:LULU(5), S163:HAL(5)  |
+------------------------------------------------------------------------+
|  b10  S165 HAL      limit=0.52                                         |
|  b38  S165 HAL      limit=0.52                                         |
|  b66  S165 HAL      limit=0.52                                         |
|  b94  S165 HAL      limit=0.52                                         |
|  b122 S165 HAL      limit=0.52                                         |
|  ... 10 more pending order(s)                                          |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (3)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  HAL260731C00033500            5    -11.9%   $    -37.00               |
|  LULU260724C00120000           5    -10.4%   $    -35.00               |
|  HAL260724C00033000            5     -6.4%   $    -17.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-21.log
elapsed=42.5s reconcile=1.67s cancel=0.11s manage=0.63s scan=37.8s entries=0.2s
STATUS: options_morning_bot run complete (PAPER) elapsed=42.5s. run=#4559 https://github.com/28twagg-ops/TradingBot/actions/runs/29841015729
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 2.9% (22/762)
# Options signal frequency

_Generated 2026-07-21T10:51:27.929615_

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
| S163 | 20 | 1 |
| S164 | 25 | 2 |
| S165 | 1412 | 15 |
| S166 | 20 | 1 |
| S167 | 20 | 2 |
| S168 | 25 | 2 |
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
| 2026-07-21 |   20 |   25 |  103 |   20 |   20 |   25 |  118 |   48 |   379 |

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
| State/ledger mismatches     |    10 | WARN | <<<
| Total open lots             |    15 | INFO |
| Total closed lots           |   297 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=479.27 router=CONFIRMED leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---

## Run 20260721T145537Z

- UTC timestamp: `20260721T145537Z`
- GitHub run: [#4560](https://github.com/28twagg-ops/TradingBot/actions/runs/29841432289)
- Run id: `29841432289`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`36s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-21T10:55:41.020018-04:00","date":"2026-07-21","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":31.1,"phases_s":{"reconcile":1.45,"cancel":0.03,"manage":0.61,"scan":27.15,"entries":0.09,"reconcile2":1.45},"signals":335,"placed":0,"equity":131760.55,"open_positions":3,"pending_orders":15,"open_lots":15,"submitted_today":60,"filled_today":70,"unattributed_contracts":0,"top_signals":["S165:ACN","S165:ADBE","S165:A","S165:BR","S165:CSGP","S165:DHR","S165:EFX","S165:FDS"],"github_run":"4560","github_run_id":"29841432289","status":"ok"}
```

### Live bot full output

```text
14:55:38  INFO      Mode: exits
14:55:38  INFO        Daily log -> logs/daily/2026-07-21.md
14:55:38  INFO        Daily log reconciled -> logs/daily/2026-07-21.md (5 ledger rows)
14:55:38  INFO        place_all_stops: checking 4 positions...
14:55:39  INFO        STOP already live BEN @ $32.36
14:55:39  INFO        STOP skipped BIIB: fractional (0.4766 shares) — software exit will handle it
14:55:39  INFO        STOP skipped DUK: fractional (0.7693 shares) — software exit will handle it
14:55:39  INFO        STOP skipped TPR: fractional (0.6841 shares) — software exit will handle it
14:55:39  INFO        [positions] 4/4 (4 valid)
14:55:39  INFO        Daily log -> logs/daily/2026-07-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:55 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $479.05|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  BIIB  P&L -0.4%  $-0.39                                           HOLD|
|  DUK  P&L -0.3%  $-0.25                                            HOLD|
|  TPR  P&L +0.2%  $+0.19                                            HOLD|
|  BEN  P&L +0.4%  $+0.31                                            HOLD|
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
  open_lots=15 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=5
  zombies_flagged=15
  FLAG b138|S168|f0c03357 zombie age_min=896 notional=$67.00 occ=LULU260724C00120000 action=error:{"bid":"0.61","buy_limit_price":"0.64","code":40310000,"existing_order_id":"1cdce2da-8a90-42ba-aad7-6b07a5038594","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b110|S168|057cb1b4 zombie age_min=896 notional=$67.00 occ=LULU260724C00120000 action=error:{"bid":"0.61","buy_limit_price":"0.64","code":40310000,"existing_order_id":"1cdce2da-8a90-42ba-aad7-6b07a5038594","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b82|S168|62fa2554 zombie age_min=896 notional=$67.00 occ=LULU260724C00120000 action=error:{"bid":"0.61","buy_limit_price":"0.64","code":40310000,"existing_order_id":"1cdce2da-8a90-42ba-aad7-6b07a5038594","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b54|S168|727db7e6 zombie age_min=896 notional=$67.00 occ=LULU260724C00120000 action=error:{"bid":"0.61","buy_limit_price":"0.64","code":40310000,"existing_order_id":"1cdce2da-8a90-42ba-aad7-6b07a5038594","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b26|S168|b59bb7e4 zombie age_min=896 notional=$67.00 occ=LULU260724C00120000 action=error:{"bid":"0.61","buy_limit_price":"0.64","code":40310000,"existing_order_id":"1cdce2da-8a90-42ba-aad7-6b07a5038594","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b121|S165|7920fc54 zombie age_min=896 notional=$63.00 occ=HAL260724C00033000 action=error:{"bid":"0.5","buy_limit_price":"0.52","code":40310000,"existing_order_id":"43580845-aebc-43b0-9c47-82b409c7295a","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b93|S165|f7709baf zombie age_min=896 notional=$63.00 occ=HAL260724C00033000 action=error:{"bid":"0.5","buy_limit_price":"0.52","code":40310000,"existing_order_id":"43580845-aebc-43b0-9c47-82b409c7295a","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b65|S165|f3a49f5a zombie age_min=896 notional=$63.00 occ=HAL260724C00033000 action=error:{"bid":"0.5","buy_limit_price":"0.52","code":40310000,"existing_order_id":"43580845-aebc-43b0-9c47-82b409c7295a","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b37|S165|cce7018f zombie age_min=896 notional=$63.00 occ=HAL260724C00033000 action=error:{"bid":"0.5","buy_limit_price":"0.52","code":40310000,"existing_order_id":"43580845-aebc-43b0-9c47-82b409c7295a","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b128|S163|168c5f90 zombie age_min=896 notional=$74.00 occ=HAL260731C00033500 action=error:{"bid":"0.55","buy_limit_price":"0.58","code":40310000,"existing_order_id":"1cde3897-28bf-4dbc-bfad-b09cca33cf1e","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b100|S163|1065ff2d zombie age_min=896 notional=$74.00 occ=HAL260731C00033500 action=error:{"bid":"0.55","buy_limit_price":"0.58","code":40310000,"existing_order_id":"1cde3897-28bf-4dbc-bfad-b09cca33cf1e","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b72|S163|b118c489 zombie age_min=896 notional=$74.00 occ=HAL260731C00033500 action=error:{"bid":"0.55","buy_limit_price":"0.58","code":40310000,"existing_order_id":"1cde3897-28bf-4dbc-bfad-b09cca33cf1e","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b44|S163|17f8a20a zombie age_min=896 notional=$74.00 occ=HAL260731C00033500 action=error:{"bid":"0.55","buy_limit_price":"0.58","code":40310000,"existing_order_id":"1cde3897-28bf-4dbc-bfad-b09cca33cf1e","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b16|S163|062ebaab zombie age_min=896 notional=$74.00 occ=HAL260731C00033500 action=error:{"bid":"0.55","buy_limit_price":"0.58","code":40310000,"existing_order_id":"1cde3897-28bf-4dbc-bfad-b09cca33cf1e","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b24|S168|698cc30f zombie age_min=896 notional=$63.00 occ=HAL260724C00033000 action=error:{"bid":"0.5","buy_limit_price":"0.52","code":40310000,"existing_order_id":"43580845-aebc-43b0-9c47-82b409c7295a","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
options_reconcile: done
Layout: controlled:140:c000_s173_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:140:c000_s173_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      140
=== options_morning_bot (PAPER) 2026-07-21T10:55:41.020018-04:00 ===

[Run context]
Paper auth OK — equity $131760.55, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 335 signal(s); top: ['S165:ACN', 'S165:ADBE', 'S165:A', 'S165:BR', 'S165:CSGP', 'S165:DHR', 'S165:EFX', 'S165:FDS']
Paper lab: $131739 broker equity -> 140 bucket(s) ($500 virtual each, unlimited paper)
  All bucket slots blocked or closed for today's signals — skip entry loop.
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $131,760.55                             |
|  Signals this run              335                                     |
|  Orders submitted (session)    60                                      |
|  Orders filled today (ledger)  70                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             15                                      |
|  Broker option positions       3                                       |
|  Pending orders                15                                      |
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
|  PENDING ORDERS (15)                                                   |
+------------------------------------------------------------------------+
|  Top groups                    S165:HAL(5), S167:LULU(5), S163:HAL(5)  |
+------------------------------------------------------------------------+
|  b10  S165 HAL      limit=0.52                                         |
|  b38  S165 HAL      limit=0.52                                         |
|  b66  S165 HAL      limit=0.52                                         |
|  b94  S165 HAL      limit=0.52                                         |
|  b122 S165 HAL      limit=0.52                                         |
|  ... 10 more pending order(s)                                          |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (3)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  LULU260724C00120000           5     -9.0%   $    -30.00               |
|  HAL260731C00033500            5     -7.1%   $    -22.00               |
|  HAL260724C00033000            5     -6.4%   $    -17.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-21.log
elapsed=31.1s reconcile=1.45s cancel=0.03s manage=0.61s scan=27.15s entries=0.09s
STATUS: options_morning_bot run complete (PAPER) elapsed=31.1s. run=#4560 https://github.com/28twagg-ops/TradingBot/actions/runs/29841432289
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 2.9% (22/762)
# Options signal frequency

_Generated 2026-07-21T10:56:15.146964_

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
| S163 | 20 | 1 |
| S164 | 25 | 2 |
| S165 | 1412 | 15 |
| S166 | 20 | 1 |
| S167 | 20 | 2 |
| S168 | 25 | 2 |
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
| 2026-07-21 |   20 |   25 |  103 |   20 |   20 |   25 |  118 |   48 |   379 |

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
| State/ledger mismatches     |    10 | WARN | <<<
| Total open lots             |    15 | INFO |
| Total closed lots           |   297 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=479.05 router=CONFIRMED leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---

## Run 20260721T150044Z

- UTC timestamp: `20260721T150044Z`
- GitHub run: [#4561](https://github.com/28twagg-ops/TradingBot/actions/runs/29841842238)
- Run id: `29841842238`
- Live bot: exit=`0`, duration=`4s`
- Options bot: exit=`0`, duration=`71s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-21T11:00:51.552007-04:00","date":"2026-07-21","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":64.3,"phases_s":{"reconcile":1.82,"cancel":0.15,"manage":0.9,"scan":58.72,"entries":0.2,"reconcile2":1.84},"signals":335,"placed":0,"equity":131546.35,"open_positions":1,"pending_orders":15,"open_lots":5,"submitted_today":60,"filled_today":70,"unattributed_contracts":0,"top_signals":["S165:ACN","S165:ADBE","S165:A","S165:BR","S165:CSGP","S165:DHR","S165:EFX","S165:FDS"],"github_run":"4561","github_run_id":"29841842238","status":"ok"}
```

### Live bot full output

```text
15:00:45  INFO      Mode: exits
15:00:46  INFO        Daily log -> logs/daily/2026-07-21.md
15:00:46  INFO        Daily log reconciled -> logs/daily/2026-07-21.md (5 ledger rows)
15:00:46  INFO        place_all_stops: checking 4 positions...
15:00:46  INFO        STOP already live BEN @ $32.36
15:00:46  INFO        STOP skipped BIIB: fractional (0.4766 shares) — software exit will handle it
15:00:46  INFO        STOP skipped DUK: fractional (0.7693 shares) — software exit will handle it
15:00:46  INFO        STOP skipped TPR: fractional (0.6841 shares) — software exit will handle it
15:00:47  INFO        [positions] 4/4 (4 valid)
15:00:48  INFO        Daily log -> logs/daily/2026-07-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:00 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $479.05|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  BIIB  P&L -0.3%  $-0.25                                           HOLD|
|  DUK  P&L -0.2%  $-0.23                                            HOLD|
|  BEN  P&L +0.2%  $+0.11                                            HOLD|
|  TPR  P&L +0.2%  $+0.24                                            HOLD|
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
  open_lots=15 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=5
  zombies_flagged=15
  FLAG b138|S168|f0c03357 zombie age_min=901 notional=$67.00 occ=LULU260724C00120000 action=error:{"bid":"0.55","buy_limit_price":"0.64","code":40310000,"existing_order_id":"1cdce2da-8a90-42ba-aad7-6b07a5038594","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b110|S168|057cb1b4 zombie age_min=901 notional=$67.00 occ=LULU260724C00120000 action=error:{"bid":"0.55","buy_limit_price":"0.64","code":40310000,"existing_order_id":"1cdce2da-8a90-42ba-aad7-6b07a5038594","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b82|S168|62fa2554 zombie age_min=901 notional=$67.00 occ=LULU260724C00120000 action=error:{"bid":"0.55","buy_limit_price":"0.64","code":40310000,"existing_order_id":"1cdce2da-8a90-42ba-aad7-6b07a5038594","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b54|S168|727db7e6 zombie age_min=901 notional=$67.00 occ=LULU260724C00120000 action=error:{"bid":"0.55","buy_limit_price":"0.64","code":40310000,"existing_order_id":"1cdce2da-8a90-42ba-aad7-6b07a5038594","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b26|S168|b59bb7e4 zombie age_min=901 notional=$67.00 occ=LULU260724C00120000 action=error:{"bid":"0.55","buy_limit_price":"0.64","code":40310000,"existing_order_id":"1cdce2da-8a90-42ba-aad7-6b07a5038594","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b121|S165|be153918 zombie age_min=901 notional=$63.00 occ=HAL260724C00033000 action=submitted:5f122368-9a9f-4925-b482-1edc36127e78
  FLAG b93|S165|905630d6 zombie age_min=901 notional=$63.00 occ=HAL260724C00033000 action=submitted:c4525de8-d942-485c-ba75-7245a001aa87
  FLAG b65|S165|5050b1f7 zombie age_min=901 notional=$63.00 occ=HAL260724C00033000 action=submitted:63233818-e4e9-42de-86d1-544670b92ad1
  FLAG b37|S165|7a389144 zombie age_min=901 notional=$63.00 occ=HAL260724C00033000 action=submitted:864a0de3-5471-4c71-80ac-68f86fa609f2
  FLAG b128|S163|b8ac3e87 zombie age_min=901 notional=$74.00 occ=HAL260731C00033500 action=submitted:4b2bb21b-1321-4843-b13c-8097b4ebb48a
  FLAG b100|S163|344a8b1b zombie age_min=901 notional=$74.00 occ=HAL260731C00033500 action=submitted:efdffec3-e53e-414d-8e2f-02354b35ec45
  FLAG b72|S163|1dcb1f03 zombie age_min=901 notional=$74.00 occ=HAL260731C00033500 action=submitted:4f7d6840-00e8-4b5e-9139-5ef286d00e91
  FLAG b44|S163|93a886cf zombie age_min=901 notional=$74.00 occ=HAL260731C00033500 action=submitted:9dafdcc7-f5b2-452e-bd0e-07edbc452dbe
  FLAG b16|S163|d5bd0ab0 zombie age_min=901 notional=$74.00 occ=HAL260731C00033500 action=submitted:d9c74d9e-9096-4723-94f8-d1e3f1f12d74
  FLAG b24|S168|b6db1029 zombie age_min=901 notional=$63.00 occ=HAL260724C00033000 action=submitted:c6451a6e-7c36-4861-84af-f0229a73016a
options_reconcile: done
Layout: controlled:140:c000_s173_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:140:c000_s173_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      140
=== options_morning_bot (PAPER) 2026-07-21T11:00:51.552007-04:00 ===

[Run context]
Paper auth OK — equity $131544.35, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 335 signal(s); top: ['S165:ACN', 'S165:ADBE', 'S165:A', 'S165:BR', 'S165:CSGP', 'S165:DHR', 'S165:EFX', 'S165:FDS']
Paper lab: $131218 broker equity -> 140 bucket(s) ($500 virtual each, unlimited paper)
  All bucket slots blocked or closed for today's signals — skip entry loop.
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $131,546.35                             |
|  Signals this run              335                                     |
|  Orders submitted (session)    60                                      |
|  Orders filled today (ledger)  70                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             5                                       |
|  Broker option positions       1                                       |
|  Pending orders                15                                      |
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
|  PENDING ORDERS (15)                                                   |
+------------------------------------------------------------------------+
|  Top groups                    S165:HAL(5), S167:LULU(5), S163:HAL(5)  |
+------------------------------------------------------------------------+
|  b10  S165 HAL      limit=0.52                                         |
|  b38  S165 HAL      limit=0.52                                         |
|  b66  S165 HAL      limit=0.52                                         |
|  b94  S165 HAL      limit=0.52                                         |
|  b122 S165 HAL      limit=0.52                                         |
|  ... 10 more pending order(s)                                          |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (1)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  LULU260724C00120000           5    -29.9%   $   -100.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-21.log
elapsed=64.3s reconcile=1.82s cancel=0.15s manage=0.9s scan=58.72s entries=0.2s
STATUS: options_morning_bot run complete (PAPER) elapsed=64.3s. run=#4561 https://github.com/28twagg-ops/TradingBot/actions/runs/29841842238
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 2.9% (22/762)
# Options signal frequency

_Generated 2026-07-21T11:01:59.017771_

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
| S163 | 20 | 1 |
| S164 | 25 | 2 |
| S165 | 1412 | 15 |
| S166 | 20 | 1 |
| S167 | 20 | 2 |
| S168 | 25 | 2 |
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
| 2026-07-21 |   20 |   25 |  103 |   20 |   20 |   25 |  118 |   48 |   379 |

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
| Total open lots             |     5 | INFO |
| Total closed lots           |   297 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=479.05 router=CONFIRMED leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---

## Run 20260721T150536Z

- UTC timestamp: `20260721T150536Z`
- GitHub run: [#4562](https://github.com/28twagg-ops/TradingBot/actions/runs/29842261715)
- Run id: `29842261715`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`54s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-21T11:05:39.990513-04:00","date":"2026-07-21","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":48.5,"phases_s":{"reconcile":1.53,"cancel":0.02,"manage":0.29,"scan":44.58,"entries":0.08,"reconcile2":1.53},"signals":335,"placed":0,"equity":131408.15,"open_positions":1,"pending_orders":10,"open_lots":5,"submitted_today":60,"filled_today":75,"unattributed_contracts":0,"top_signals":["S165:ACN","S165:ADBE","S165:A","S165:BR","S165:CSGP","S165:DHR","S165:EFX","S165:FDS"],"github_run":"4562","github_run_id":"29842261715","status":"ok"}
```

### Live bot full output

```text
15:05:37  INFO      Mode: exits
15:05:37  INFO        Daily log -> logs/daily/2026-07-21.md
15:05:37  INFO        Daily log reconciled -> logs/daily/2026-07-21.md (5 ledger rows)
15:05:37  INFO        place_all_stops: checking 4 positions...
15:05:37  INFO        STOP already live BEN @ $32.36
15:05:37  INFO        STOP skipped BIIB: fractional (0.4766 shares) — software exit will handle it
15:05:37  INFO        STOP skipped DUK: fractional (0.7693 shares) — software exit will handle it
15:05:37  INFO        STOP skipped TPR: fractional (0.6841 shares) — software exit will handle it
15:05:37  INFO        [positions] 4/4 (4 valid)
15:05:37  INFO        Daily log -> logs/daily/2026-07-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:05 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $478.96|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  DUK  P&L -0.3%  $-0.25                                            HOLD|
|  BIIB  P&L -0.2%  $-0.22                                           HOLD|
|  BEN  P&L +0.1%  $+0.04                                            HOLD|
|  TPR  P&L +0.2%  $+0.18                                            HOLD|
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
  open_lots=5 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=3
  zombies_flagged=5
  FLAG b138|S168|f0c03357 zombie age_min=906 notional=$67.00 occ=LULU260724C00120000 action=submitted:dd9ce76e-60c8-4666-904e-41baf9c519b0
  FLAG b110|S168|057cb1b4 zombie age_min=906 notional=$67.00 occ=LULU260724C00120000 action=submitted:d786b8b1-e0d2-4f72-a04f-be4436f6288d
  FLAG b82|S168|62fa2554 zombie age_min=906 notional=$67.00 occ=LULU260724C00120000 action=submitted:27f506e5-2f2d-4479-bcaf-6407b46b566d
  FLAG b54|S168|727db7e6 zombie age_min=906 notional=$67.00 occ=LULU260724C00120000 action=submitted:6cc35c4f-e828-4778-a9ec-66cef0529752
  FLAG b26|S168|b59bb7e4 zombie age_min=906 notional=$67.00 occ=LULU260724C00120000 action=submitted:4025283a-5cb5-4c66-97a0-c876caf8d968
options_reconcile: done
Layout: controlled:140:c000_s173_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:140:c000_s173_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      140
=== options_morning_bot (PAPER) 2026-07-21T11:05:39.990513-04:00 ===

[Run context]
Paper auth OK — equity $131408.15, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 335 signal(s); top: ['S165:ACN', 'S165:ADBE', 'S165:A', 'S165:BR', 'S165:CSGP', 'S165:DHR', 'S165:EFX', 'S165:FDS']
Paper lab: $131572 broker equity -> 140 bucket(s) ($500 virtual each, unlimited paper)
  All bucket slots blocked or closed for today's signals — skip entry loop.
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $131,408.15                             |
|  Signals this run              335                                     |
|  Orders submitted (session)    60                                      |
|  Orders filled today (ledger)  75                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             5                                       |
|  Broker option positions       1                                       |
|  Pending orders                10                                      |
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
|  PENDING ORDERS (10)                                                   |
+------------------------------------------------------------------------+
|  Top groups                    S165:HAL(5), S163:HAL(5)                |
+------------------------------------------------------------------------+
|  b10  S165 HAL      limit=0.52                                         |
|  b38  S165 HAL      limit=0.52                                         |
|  b66  S165 HAL      limit=0.52                                         |
|  b94  S165 HAL      limit=0.52                                         |
|  b122 S165 HAL      limit=0.52                                         |
|  ... 5 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (1)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  LULU260724C00120000           5    -26.2%   $    -85.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-21.log
elapsed=48.5s reconcile=1.53s cancel=0.02s manage=0.29s scan=44.58s entries=0.08s
STATUS: options_morning_bot run complete (PAPER) elapsed=48.5s. run=#4562 https://github.com/28twagg-ops/TradingBot/actions/runs/29842261715
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 2.9% (22/762)
# Options signal frequency

_Generated 2026-07-21T11:06:31.690551_

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
| S163 | 20 | 1 |
| S164 | 25 | 2 |
| S165 | 1412 | 15 |
| S166 | 20 | 1 |
| S167 | 25 | 2 |
| S168 | 25 | 2 |
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
| 2026-07-21 |   20 |   25 |  103 |   20 |   25 |   25 |  118 |   48 |   384 |

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
| State/ledger mismatches     |     5 | WARN | <<<
| Total open lots             |     5 | INFO |
| Total closed lots           |   297 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=478.96 router=CONFIRMED leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---

## Run 20260721T151038Z

- UTC timestamp: `20260721T151038Z`
- GitHub run: [#4563](https://github.com/28twagg-ops/TradingBot/actions/runs/29842665630)
- Run id: `29842665630`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`53s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-21T11:10:43.401718-04:00","date":"2026-07-21","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":47.9,"phases_s":{"reconcile":2.29,"cancel":0.13,"manage":0.12,"scan":43.11,"entries":0.2,"reconcile2":1.58},"signals":335,"placed":0,"equity":132294.05,"open_positions":0,"pending_orders":10,"open_lots":0,"submitted_today":60,"filled_today":75,"unattributed_contracts":0,"top_signals":["S165:ACN","S165:ADBE","S165:A","S165:BR","S165:CSGP","S165:DHR","S165:EFX","S165:FDS"],"github_run":"4563","github_run_id":"29842665630","status":"ok"}
```

### Live bot full output

```text
15:10:40  INFO      Mode: exits
15:10:40  INFO        Daily log -> logs/daily/2026-07-21.md
15:10:40  INFO        Daily log reconciled -> logs/daily/2026-07-21.md (5 ledger rows)
15:10:40  INFO        place_all_stops: checking 4 positions...
15:10:40  INFO        STOP already live BEN @ $32.36
15:10:40  INFO        STOP skipped BIIB: fractional (0.4766 shares) — software exit will handle it
15:10:40  INFO        STOP skipped DUK: fractional (0.7693 shares) — software exit will handle it
15:10:40  INFO        STOP skipped TPR: fractional (0.6841 shares) — software exit will handle it
15:10:41  INFO        [positions] 4/4 (4 valid)
15:10:41  INFO        Daily log -> logs/daily/2026-07-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $479.15|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  DUK  P&L -0.3%  $-0.27                                            HOLD|
|  BIIB  P&L -0.2%  $-0.19                                           HOLD|
|  BEN  P&L +0.2%  $+0.13                                            HOLD|
|  TPR  P&L +0.3%  $+0.29                                            HOLD|
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
  open_lots=5 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=3
  zombies_flagged=5
  FLAG b138|S168|145ac957 zombie age_min=911 notional=$67.00 occ=LULU260724C00120000 action=submitted:eec8ae56-4541-408b-9519-388e76898a31
  FLAG b110|S168|a03899e5 zombie age_min=911 notional=$67.00 occ=LULU260724C00120000 action=submitted:974c7d36-51e8-4f47-ac9f-49cc93194237
  FLAG b82|S168|fc8cc96b zombie age_min=911 notional=$67.00 occ=LULU260724C00120000 action=submitted:47cfe320-83e3-4c6c-bea1-a1ca4647dda8
  FLAG b54|S168|eb4becbf zombie age_min=911 notional=$67.00 occ=LULU260724C00120000 action=submitted:1147b1f0-6acd-4415-a3b9-97e97f80a8b5
  FLAG b26|S168|54d48d17 zombie age_min=911 notional=$67.00 occ=LULU260724C00120000 action=submitted:be18d8aa-0e0c-456e-8a3d-893320257a2b
options_reconcile: done
Layout: controlled:140:c000_s173_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:140:c000_s173_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      140
=== options_morning_bot (PAPER) 2026-07-21T11:10:43.401718-04:00 ===

[Run context]
Paper auth OK — equity $132294.05, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 335 signal(s); top: ['S165:ACN', 'S165:ADBE', 'S165:A', 'S165:BR', 'S165:CSGP', 'S165:DHR', 'S165:EFX', 'S165:FDS']
Paper lab: $132444 broker equity -> 140 bucket(s) ($500 virtual each, unlimited paper)
  All bucket slots blocked or closed for today's signals — skip entry loop.
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $132,294.05                             |
|  Signals this run              335                                     |
|  Orders submitted (session)    60                                      |
|  Orders filled today (ledger)  75                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                10                                      |
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
|  PENDING ORDERS (10)                                                   |
+------------------------------------------------------------------------+
|  Top groups                    S165:HAL(5), S163:HAL(5)                |
+------------------------------------------------------------------------+
|  b10  S165 HAL      limit=0.52                                         |
|  b38  S165 HAL      limit=0.52                                         |
|  b66  S165 HAL      limit=0.52                                         |
|  b94  S165 HAL      limit=0.52                                         |
|  b122 S165 HAL      limit=0.52                                         |
|  ... 5 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-21.log
elapsed=47.9s reconcile=2.29s cancel=0.13s manage=0.12s scan=43.11s entries=0.2s
STATUS: options_morning_bot run complete (PAPER) elapsed=47.9s. run=#4563 https://github.com/28twagg-ops/TradingBot/actions/runs/29842665630
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 2.9% (22/762)
# Options signal frequency

_Generated 2026-07-21T11:11:33.716189_

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
| S163 | 20 | 1 |
| S164 | 25 | 2 |
| S165 | 1412 | 15 |
| S166 | 20 | 1 |
| S167 | 25 | 2 |
| S168 | 25 | 2 |
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
| 2026-07-21 |   20 |   25 |  103 |   20 |   25 |   25 |  118 |   48 |   384 |

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
equity=479.15 router=CONFIRMED leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---

## Run 20260721T151542Z

- UTC timestamp: `20260721T151542Z`
- GitHub run: [#4564](https://github.com/28twagg-ops/TradingBot/actions/runs/29843071321)
- Run id: `29843071321`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`53s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-21T11:15:46.758588-04:00","date":"2026-07-21","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":48.5,"phases_s":{"reconcile":1.61,"cancel":0.07,"manage":0.07,"scan":44.55,"entries":0.13,"reconcile2":1.58},"signals":335,"placed":0,"equity":132430.05,"open_positions":0,"pending_orders":10,"open_lots":0,"submitted_today":60,"filled_today":75,"unattributed_contracts":0,"top_signals":["S165:ACN","S165:ADBE","S165:A","S165:BR","S165:CSGP","S165:DHR","S165:EFX","S165:FDS"],"github_run":"4564","github_run_id":"29843071321","status":"ok"}
```

### Live bot full output

```text
15:15:43  INFO      Mode: exits
15:15:44  INFO        Daily log -> logs/daily/2026-07-21.md
15:15:44  INFO        Daily log reconciled -> logs/daily/2026-07-21.md (5 ledger rows)
15:15:44  INFO        place_all_stops: checking 4 positions...
15:15:44  INFO        STOP already live BEN @ $32.36
15:15:44  INFO        STOP skipped BIIB: fractional (0.4766 shares) — software exit will handle it
15:15:44  INFO        STOP skipped DUK: fractional (0.7693 shares) — software exit will handle it
15:15:44  INFO        STOP skipped TPR: fractional (0.6841 shares) — software exit will handle it
15:15:44  INFO        [positions] 4/4 (4 valid)
15:15:44  INFO        Daily log -> logs/daily/2026-07-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:15 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $479.48|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  DUK  P&L -0.2%  $-0.17                                            HOLD|
|  BIIB  P&L -0.1%  $-0.11                                           HOLD|
|  BEN  P&L +0.3%  $+0.24                                            HOLD|
|  TPR  P&L +0.3%  $+0.33                                            HOLD|
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
  alpaca open sell orders=0 positions=2
  zombies_flagged=0
options_reconcile: done
Layout: controlled:140:c000_s173_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:140:c000_s173_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      140
=== options_morning_bot (PAPER) 2026-07-21T11:15:46.758588-04:00 ===

[Run context]
Paper auth OK — equity $132430.05, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 335 signal(s); top: ['S165:ACN', 'S165:ADBE', 'S165:A', 'S165:BR', 'S165:CSGP', 'S165:DHR', 'S165:EFX', 'S165:FDS']
Paper lab: $132254 broker equity -> 140 bucket(s) ($500 virtual each, unlimited paper)
  All bucket slots blocked or closed for today's signals — skip entry loop.
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $132,430.05                             |
|  Signals this run              335                                     |
|  Orders submitted (session)    60                                      |
|  Orders filled today (ledger)  75                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                10                                      |
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
|  PENDING ORDERS (10)                                                   |
+------------------------------------------------------------------------+
|  Top groups                    S165:HAL(5), S163:HAL(5)                |
+------------------------------------------------------------------------+
|  b10  S165 HAL      limit=0.52                                         |
|  b38  S165 HAL      limit=0.52                                         |
|  b66  S165 HAL      limit=0.52                                         |
|  b94  S165 HAL      limit=0.52                                         |
|  b122 S165 HAL      limit=0.52                                         |
|  ... 5 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-21.log
elapsed=48.5s reconcile=1.61s cancel=0.07s manage=0.07s scan=44.55s entries=0.13s
STATUS: options_morning_bot run complete (PAPER) elapsed=48.5s. run=#4564 https://github.com/28twagg-ops/TradingBot/actions/runs/29843071321
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 2.9% (22/762)
# Options signal frequency

_Generated 2026-07-21T11:16:38.481562_

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
| S163 | 20 | 1 |
| S164 | 25 | 2 |
| S165 | 1412 | 15 |
| S166 | 20 | 1 |
| S167 | 25 | 2 |
| S168 | 25 | 2 |
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
| 2026-07-21 |   20 |   25 |  103 |   20 |   25 |   25 |  118 |   48 |   384 |

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
equity=479.48 router=CONFIRMED leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---

## Run 20260721T152035Z

- UTC timestamp: `20260721T152035Z`
- GitHub run: [#4565](https://github.com/28twagg-ops/TradingBot/actions/runs/29843467490)
- Run id: `29843467490`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`140s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-21T11:20:38.570876-04:00","date":"2026-07-21","mode":"entry+manage","header":"entry+manage (30 new)","elapsed_s":135.6,"phases_s":{"reconcile":1.39,"cancel":0.02,"manage":0.02,"scan":31.05,"entries":101.22,"reconcile2":1.67},"signals":335,"placed":30,"equity":131956.05,"open_positions":3,"pending_orders":10,"open_lots":30,"submitted_today":90,"filled_today":105,"unattributed_contracts":0,"top_signals":["S165:ACN","S165:ADBE","S165:A","S165:BR","S165:CSGP","S165:DHR","S165:EFX","S165:FDS"],"github_run":"4565","github_run_id":"29843467490","status":"ok"}
```

### Live bot full output

```text
15:20:36  INFO      Mode: exits
15:20:36  INFO        Daily log -> logs/daily/2026-07-21.md
15:20:36  INFO        Daily log reconciled -> logs/daily/2026-07-21.md (5 ledger rows)
15:20:36  INFO        place_all_stops: checking 4 positions...
15:20:36  INFO        STOP already live BEN @ $32.36
15:20:36  INFO        STOP skipped BIIB: fractional (0.4766 shares) — software exit will handle it
15:20:36  INFO        STOP skipped DUK: fractional (0.7693 shares) — software exit will handle it
15:20:36  INFO        STOP skipped TPR: fractional (0.6841 shares) — software exit will handle it
15:20:37  INFO        [positions] 4/4 (4 valid)
15:20:37  INFO        Daily log -> logs/daily/2026-07-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $479.69|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  BIIB  P&L -0.2%  $-0.22                                           HOLD|
|  DUK  P&L -0.1%  $-0.07                                            HOLD|
|  TPR  P&L +0.5%  $+0.44                                            HOLD|
|  BEN  P&L +0.5%  $+0.35                                            HOLD|
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
  alpaca open sell orders=0 positions=2
  zombies_flagged=0
options_reconcile: done
Layout: controlled:140:c000_s173_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:140:c000_s173_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      140
=== options_morning_bot (PAPER) 2026-07-21T11:20:38.570876-04:00 ===

[Run context]
Paper auth OK — equity $131956.05, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 335 signal(s); top: ['S165:ACN', 'S165:ADBE', 'S165:A', 'S165:BR', 'S165:CSGP', 'S165:DHR', 'S165:EFX', 'S165:FDS']
Paper lab: $131982 broker equity -> 140 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 435 no tradeable call, 1055 already attempted today, 1830 pending order
Placed 30 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $131,956.05                             |
|  Signals this run              335                                     |
|  Orders submitted (session)    90                                      |
|  Orders filled today (ledger)  105                                     |
|  Entries placed this run       30                                      |
|  Open virtual lots             30                                      |
|  Broker option positions       3                                       |
|  Pending orders                10                                      |
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
|  PENDING ORDERS (10)                                                   |
+------------------------------------------------------------------------+
|  Top groups                    S165:HAL(5), S163:HAL(5)                |
+------------------------------------------------------------------------+
|  b10  S165 HAL      limit=0.52                                         |
|  b38  S165 HAL      limit=0.52                                         |
|  b66  S165 HAL      limit=0.52                                         |
|  b94  S165 HAL      limit=0.52                                         |
|  b122 S165 HAL      limit=0.52                                         |
|  ... 5 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (3)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  HAL260731C00033500           10    -11.4%   $    -80.00               |
|  HAL260724C00033000           10    -11.3%   $    -75.00               |
|  LULU260724C00120000          10    -12.0%   $    -75.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-21.log
elapsed=135.6s reconcile=1.39s cancel=0.02s manage=0.02s scan=31.05s entries=101.22s
STATUS: options_morning_bot run complete (PAPER) elapsed=135.6s. run=#4565 https://github.com/28twagg-ops/TradingBot/actions/runs/29843467490
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 2.9% (22/762)
# Options signal frequency

_Generated 2026-07-21T11:22:57.409775_

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
| State/ledger mismatches     |    30 | WARN | <<<
| Total open lots             |    30 | INFO |
| Total closed lots           |   297 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=479.69 router=CONFIRMED leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---

## Run 20260721T152539Z

- UTC timestamp: `20260721T152539Z`
- GitHub run: [#4566](https://github.com/28twagg-ops/TradingBot/actions/runs/29843868024)
- Run id: `29843868024`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`40s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-21T11:25:43.687833-04:00","date":"2026-07-21","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":34.5,"phases_s":{"reconcile":1.86,"cancel":0.02,"manage":0.02,"scan":30.71,"entries":0.17,"reconcile2":1.42},"signals":335,"placed":0,"equity":132376.85,"open_positions":0,"pending_orders":10,"open_lots":0,"submitted_today":90,"filled_today":105,"unattributed_contracts":0,"top_signals":["S165:ACN","S165:ADBE","S165:A","S165:BR","S165:CSGP","S165:DHR","S165:EFX","S165:FDS"],"github_run":"4566","github_run_id":"29843868024","status":"ok"}
```

### Live bot full output

```text
15:25:40  INFO      Mode: exits
15:25:41  INFO        Daily log -> logs/daily/2026-07-21.md
15:25:41  INFO        Daily log reconciled -> logs/daily/2026-07-21.md (5 ledger rows)
15:25:41  INFO        place_all_stops: checking 4 positions...
15:25:41  INFO        STOP already live BEN @ $32.36
15:25:41  INFO        STOP skipped BIIB: fractional (0.4766 shares) — software exit will handle it
15:25:41  INFO        STOP skipped DUK: fractional (0.7693 shares) — software exit will handle it
15:25:41  INFO        STOP skipped TPR: fractional (0.6841 shares) — software exit will handle it
15:25:41  INFO        [positions] 4/4 (4 valid)
15:25:41  INFO        Daily log -> logs/daily/2026-07-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:25 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $479.37|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  BIIB  P&L -0.3%  $-0.33                                           HOLD|
|  DUK  P&L -0.2%  $-0.21                                            HOLD|
|  BEN  P&L +0.2%  $+0.14                                            HOLD|
|  TPR  P&L +0.6%  $+0.58                                            HOLD|
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
  open_lots=30 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=5
  zombies_flagged=30
  FLAG b118|S167|56d88ece zombie age_min=926 notional=$63.00 occ=LULU260724C00120000 action=submitted:c4bf2f59-88c0-4964-8b36-e1ecb820ce14
  FLAG b90|S167|24fabf75 zombie age_min=926 notional=$63.00 occ=LULU260724C00120000 action=submitted:4d970ea6-4d31-4d2a-8ce1-10d09b581c45
  FLAG b62|S167|9489dd79 zombie age_min=926 notional=$63.00 occ=LULU260724C00120000 action=submitted:8ec93dbe-155f-4feb-99fd-cf4fb42f823e
  FLAG b34|S167|d5f57d10 zombie age_min=926 notional=$63.00 occ=LULU260724C00120000 action=submitted:35ea0f07-e22f-40e9-9b53-d5529a2d0c56
  FLAG b6|S167|e8ce2a68 zombie age_min=926 notional=$63.00 occ=LULU260724C00120000 action=submitted:8e8e07cb-669e-4f03-a49c-c9d24b7ab22a
  FLAG b138|S168|2d5ae0f5 zombie age_min=926 notional=$67.00 occ=LULU260724C00120000 action=submitted:477afb82-71c3-4eb9-925c-ac96f4cb5397
  FLAG b110|S168|e0246b1d zombie age_min=926 notional=$67.00 occ=LULU260724C00120000 action=submitted:a2564a14-8bda-48ac-9640-920bc366d1e6
  FLAG b82|S168|878ce77a zombie age_min=926 notional=$67.00 occ=LULU260724C00120000 action=submitted:a3d704b6-109b-4d27-ad22-a6d60dfedc94
  FLAG b54|S168|712ec34a zombie age_min=926 notional=$67.00 occ=LULU260724C00120000 action=submitted:420bb1ee-cc73-4686-b4d5-62c519a61523
  FLAG b26|S168|21bc664a zombie age_min=926 notional=$67.00 occ=LULU260724C00120000 action=submitted:c14ba115-c6fa-481d-acd6-e77a72051261
  FLAG b125|S166|5b13996d zombie age_min=926 notional=$67.00 occ=HAL260731C00033500 action=submitted:d317fd78-1746-4767-82f1-e9f760c102ca
  FLAG b97|S166|632e6a96 zombie age_min=926 notional=$67.00 occ=HAL260731C00033500 action=submitted:3fd324bd-90b8-47f6-8495-cd09cd70a8a1
  FLAG b69|S166|b70874cb zombie age_min=926 notional=$67.00 occ=HAL260731C00033500 action=submitted:4eee93be-6060-4b79-8fca-d7dfc3099cd0
  FLAG b41|S166|f9eec66d zombie age_min=926 notional=$67.00 occ=HAL260731C00033500 action=submitted:3ed5161c-be3a-49d4-8b38-18af2f6777f2
  FLAG b13|S166|e9d9cb7d zombie age_min=926 notional=$67.00 occ=HAL260731C00033500 action=submitted:5a22abf6-dd44-49e3-b6db-7c107ab38085
  FLAG b121|S165|d6411892 zombie age_min=926 notional=$63.00 occ=HAL260724C00033000 action=submitted:455c5f2f-6954-4d48-8b01-0ac7a867ee05
  FLAG b93|S165|6fce6db3 zombie age_min=926 notional=$63.00 occ=HAL260724C00033000 action=submitted:131a40b0-0061-4758-8897-e20f3d5d1c45
  FLAG b65|S165|aa8342d4 zombie age_min=926 notional=$63.00 occ=HAL260724C00033000 action=submitted:f58a290a-bd9f-4d0b-9bf7-2f8ee57acb4b
  FLAG b37|S165|408dcf96 zombie age_min=926 notional=$63.00 occ=HAL260724C00033000 action=submitted:cdafc76c-55dd-4bd6-a605-e480e9b87a84
  FLAG b9|S165|cda5464e zombie age_min=926 notional=$63.00 occ=HAL260724C00033000 action=submitted:23db54dc-d1fb-41ce-a830-cda2a6ac4eda
  FLAG b128|S163|bd375639 zombie age_min=926 notional=$74.00 occ=HAL260731C00033500 action=submitted:f62b30fb-97be-4b81-baf5-4c79bf080503
  FLAG b100|S163|e22e9b63 zombie age_min=926 notional=$74.00 occ=HAL260731C00033500 action=submitted:a151af58-753a-4b88-a425-1aead0fd35fe
  FLAG b72|S163|dd77316e zombie age_min=926 notional=$74.00 occ=HAL260731C00033500 action=submitted:2b4b3a1a-6bf9-4bd8-ab40-da3401397e11
  FLAG b44|S163|cb99c9cc zombie age_min=926 notional=$74.00 occ=HAL260731C00033500 action=submitted:2c9c54ba-0e46-4cca-b265-37ec630204de
  FLAG b16|S163|f1511f38 zombie age_min=926 notional=$74.00 occ=HAL260731C00033500 action=submitted:9d8dbc8c-e8e5-40fd-9bf9-214f06a64fb7
  FLAG b136|S168|ba9adbce zombie age_min=926 notional=$63.00 occ=HAL260724C00033000 action=submitted:65538d0d-3ebc-4f34-8aac-c42d7b5607ae
  FLAG b108|S168|1b36f102 zombie age_min=926 notional=$63.00 occ=HAL260724C00033000 action=submitted:7b746de2-8a83-40c3-98ea-51d2773a63df
  FLAG b80|S168|a9e3c333 zombie age_min=926 notional=$63.00 occ=HAL260724C00033000 action=submitted:e282884c-8161-436e-a587-3a8b975ed7c1
  FLAG b52|S168|0b1ca789 zombie age_min=926 notional=$63.00 occ=HAL260724C00033000 action=submitted:ee1d570b-822d-487a-9e1a-0428dd823423
  FLAG b24|S168|3db8eb2e zombie age_min=926 notional=$63.00 occ=HAL260724C00033000 action=submitted:737f3fbd-e27a-48ab-b877-f0f128d9235d
options_reconcile: done
Layout: controlled:140:c000_s173_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:140:c000_s173_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      140
=== options_morning_bot (PAPER) 2026-07-21T11:25:43.687833-04:00 ===

[Run context]
Paper auth OK — equity $132376.85, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 335 signal(s); top: ['S165:ACN', 'S165:ADBE', 'S165:A', 'S165:BR', 'S165:CSGP', 'S165:DHR', 'S165:EFX', 'S165:FDS']
Paper lab: $132425 broker equity -> 140 bucket(s) ($500 virtual each, unlimited paper)
  All bucket slots blocked or closed for today's signals — skip entry loop.
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $132,376.85                             |
|  Signals this run              335                                     |
|  Orders submitted (session)    90                                      |
|  Orders filled today (ledger)  105                                     |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                10                                      |
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
|  PENDING ORDERS (10)                                                   |
+------------------------------------------------------------------------+
|  Top groups                    S165:HAL(5), S163:HAL(5)                |
+------------------------------------------------------------------------+
|  b10  S165 HAL      limit=0.52                                         |
|  b38  S165 HAL      limit=0.52                                         |
|  b66  S165 HAL      limit=0.52                                         |
|  b94  S165 HAL      limit=0.52                                         |
|  b122 S165 HAL      limit=0.52                                         |
|  ... 5 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-21.log
elapsed=34.5s reconcile=1.86s cancel=0.02s manage=0.02s scan=30.71s entries=0.17s
STATUS: options_morning_bot run complete (PAPER) elapsed=34.5s. run=#4566 https://github.com/28twagg-ops/TradingBot/actions/runs/29843868024
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-21_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 2.9% (22/762)
# Options signal frequency

_Generated 2026-07-21T11:26:21.275954_

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
equity=479.37 router=CONFIRMED leaderboard_rows=8
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 |
```

---
