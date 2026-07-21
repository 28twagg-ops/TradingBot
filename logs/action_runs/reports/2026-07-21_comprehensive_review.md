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
