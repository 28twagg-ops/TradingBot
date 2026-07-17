# Daily Comprehensive Action Review — 2026-07-17

_Auto-generated from GitHub Actions run output. This document appends every run for the day._

## Run 20260717T010718Z

- UTC timestamp: `20260717T010718Z`
- GitHub run: [#4246](https://github.com/28twagg-ops/TradingBot/actions/runs/29546593338)
- Run id: `29546593338`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`4s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T21:07:22.236284-04:00","date":"2026-07-16","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":3.1,"phases_s":{"reconcile":2.69},"signals":0,"placed":0,"equity":125155.99,"open_positions":2,"pending_orders":0,"open_lots":4,"submitted_today":32,"filled_today":55,"unattributed_contracts":0,"top_signals":[],"github_run":"4246","github_run_id":"29546593338","status":"ok"}
```

### Live bot full output

```text
01:07:19  INFO      Mode: summary
01:07:21  INFO        Daily log -> logs/daily/2026-07-17.md
01:07:21  INFO        Daily log reconciled -> logs/daily/2026-07-17.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         01:07 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $484.75|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $484.75|
|  Cash                                                            $24.24|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $460.51|
|  Open P&L                                                        $+2.20|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (5 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CARR     Pullback50      $87.85     $67.89   $69.34   +2.1%   $+1.83  |
|  CMS      Pullback50      $96.83     $74.35   $74.39   +0.1%   $+0.05  |
|  CNP      Pullback50      $97.26     $43.13   $43.34   +0.5%   $+0.48  |
|  DOV      Pullback50      $81.85     $217.58  $217.51  -0.0%   $-0.03  |
|  DRI      Pullback50      $96.72     $201.51  $201.21  -0.1%   $-0.14  |
|                                                                        |
|  Total invested                                                 $460.51|
|  Total open P&L                                                  $+2.20|
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
|  2026-07-16  SELL  MO  Pullback50  $24.34  P&L $-0.14                  |
|  2026-07-16  SELL  CASY  Pullback50  $96.04  P&L $-0.71                |
|  2026-07-16  SELL  CHH  Pullback50  $98.47  P&L $+2.83                 |
|  2026-07-16  SELL  HST  Pullback50  $92.15  P&L $+2.55                 |
|  2026-07-16  SELL  EVR  Pullback50  $96.47  P&L $+0.83                 |
|  2026-07-14  SELL  PLD  Pullback50  $95.64  P&L $+0.01                 |
+========================================================================+
```

### Options bot full output

```text
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-16T21:07:22.236284-04:00 ===

[Run context]
After hours (21:07 ET) — exit summary only.
Paper auth OK — equity $125155.99, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $125,155.99                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    32                                      |
|  Orders filled today (ledger)  55                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             4                                       |
|  Broker option positions       2                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=292  buckets=46  win=36%                             |
|  Returns   avg=+14.5%  med=-20.0%  p10=-77.0%  p90=+92.9%              |
|  Realized  $+4,345.77                                                  |
|  Raw incl dropped  trades=395  real=$+3,222.58                         |
|  Today     trades=47  avg=-33.4%  med=-56.0%  real=$-1,132.00          |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b28  c028_s165_w1_0928_  8 100% +84.7 +84.5 +102.0 $   +358           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b99  c099_s163_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b89  c089_s165_w2_1005_  4  75% +220.0 +69.9 +790.0 $   +127          |
|  ... 38 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 14   0% -62.5 -73.0 -98.5 $   -585       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b48  S165 AVGO260717C00400000 x1 EOD                                  |
|  b0   S173 UAL260717C00122000 x1 EOD                                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (2)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  UAL260717C00122000            3    -46.2%   $    -90.00               |
|  AVGO260717C00400000           1    -75.9%   $    -47.17               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=3.1s reconcile=2.69s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=3.1s. run=#4246 https://github.com/28twagg-ops/TradingBot/actions/runs/29546593338
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 26 buckets closed trades, $-1,132.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 5.6% (22/395)
```

---

## Run 20260717T015206Z

- UTC timestamp: `20260717T015206Z`
- GitHub run: [#4247](https://github.com/28twagg-ops/TradingBot/actions/runs/29548498703)
- Run id: `29548498703`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`6s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T21:52:09.717729-04:00","date":"2026-07-16","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":4.1,"phases_s":{"reconcile":3.73},"signals":0,"placed":0,"equity":124071.99,"open_positions":2,"pending_orders":0,"open_lots":4,"submitted_today":32,"filled_today":55,"unattributed_contracts":0,"top_signals":[],"github_run":"4247","github_run_id":"29548498703","status":"ok"}
```

### Live bot full output

```text
01:52:07  INFO      Mode: summary
01:52:08  INFO        Daily log -> logs/daily/2026-07-17.md
01:52:08  INFO        Daily log reconciled -> logs/daily/2026-07-17.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         01:52 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $484.75|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $484.75|
|  Cash                                                            $24.24|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $460.51|
|  Open P&L                                                        $+2.20|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (5 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CARR     Pullback50      $87.85     $67.89   $69.34   +2.1%   $+1.83  |
|  CMS      Pullback50      $96.83     $74.35   $74.39   +0.1%   $+0.05  |
|  CNP      Pullback50      $97.26     $43.13   $43.34   +0.5%   $+0.48  |
|  DOV      Pullback50      $81.85     $217.58  $217.51  -0.0%   $-0.03  |
|  DRI      Pullback50      $96.72     $201.51  $201.21  -0.1%   $-0.14  |
|                                                                        |
|  Total invested                                                 $460.51|
|  Total open P&L                                                  $+2.20|
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
|  2026-07-16  SELL  MO  Pullback50  $24.34  P&L $-0.14                  |
|  2026-07-16  SELL  CASY  Pullback50  $96.04  P&L $-0.71                |
|  2026-07-16  SELL  CHH  Pullback50  $98.47  P&L $+2.83                 |
|  2026-07-16  SELL  HST  Pullback50  $92.15  P&L $+2.55                 |
|  2026-07-16  SELL  EVR  Pullback50  $96.47  P&L $+0.83                 |
|  2026-07-14  SELL  PLD  Pullback50  $95.64  P&L $+0.01                 |
+========================================================================+
```

### Options bot full output

```text
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-16T21:52:09.717729-04:00 ===

[Run context]
After hours (21:52 ET) — exit summary only.
Paper auth OK — equity $124071.99, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $124,071.99                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    32                                      |
|  Orders filled today (ledger)  55                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             4                                       |
|  Broker option positions       2                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=292  buckets=46  win=36%                             |
|  Returns   avg=+14.5%  med=-20.0%  p10=-77.0%  p90=+92.9%              |
|  Realized  $+4,345.77                                                  |
|  Raw incl dropped  trades=395  real=$+3,222.58                         |
|  Today     trades=47  avg=-33.4%  med=-56.0%  real=$-1,132.00          |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b28  c028_s165_w1_0928_  8 100% +84.7 +84.5 +102.0 $   +358           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b99  c099_s163_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b89  c089_s165_w2_1005_  4  75% +220.0 +69.9 +790.0 $   +127          |
|  ... 38 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 14   0% -62.5 -73.0 -98.5 $   -585       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b48  S165 AVGO260717C00400000 x1 EOD                                  |
|  b0   S173 UAL260717C00122000 x1 EOD                                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (2)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  UAL260717C00122000            3    -46.2%   $    -90.00               |
|  AVGO260717C00400000           1    -75.9%   $    -47.17               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=4.1s reconcile=3.73s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=4.1s. run=#4247 https://github.com/28twagg-ops/TradingBot/actions/runs/29548498703
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 26 buckets closed trades, $-1,132.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 5.6% (22/395)
```

---

## Run 20260717T044842Z

- UTC timestamp: `20260717T044842Z`
- GitHub run: [#4248](https://github.com/28twagg-ops/TradingBot/actions/runs/29555732790)
- Run id: `29555732790`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`3s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T00:48:44.732908-04:00","date":"2026-07-17","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":2.4,"phases_s":{"reconcile":2.17},"signals":0,"placed":0,"equity":122587.99,"open_positions":2,"pending_orders":0,"open_lots":4,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4248","github_run_id":"29555732790","status":"ok"}
```

### Live bot full output

```text
04:48:43  INFO      Mode: summary
04:48:43  INFO        Daily log -> logs/daily/2026-07-17.md
04:48:43  INFO        Daily log reconciled -> logs/daily/2026-07-17.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         04:48 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $484.75|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $484.75|
|  Cash                                                            $24.24|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $460.51|
|  Open P&L                                                        $+2.20|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (5 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CARR     Pullback50      $87.85     $67.89   $69.34   +2.1%   $+1.83  |
|  CMS      Pullback50      $96.83     $74.35   $74.39   +0.1%   $+0.05  |
|  CNP      Pullback50      $97.26     $43.13   $43.34   +0.5%   $+0.48  |
|  DOV      Pullback50      $81.85     $217.58  $217.51  -0.0%   $-0.03  |
|  DRI      Pullback50      $96.72     $201.51  $201.21  -0.1%   $-0.14  |
|                                                                        |
|  Total invested                                                 $460.51|
|  Total open P&L                                                  $+2.20|
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
|  2026-07-16  SELL  MO  Pullback50  $24.34  P&L $-0.14                  |
|  2026-07-16  SELL  CASY  Pullback50  $96.04  P&L $-0.71                |
|  2026-07-16  SELL  CHH  Pullback50  $98.47  P&L $+2.83                 |
|  2026-07-16  SELL  HST  Pullback50  $92.15  P&L $+2.55                 |
|  2026-07-16  SELL  EVR  Pullback50  $96.47  P&L $+0.83                 |
|  2026-07-14  SELL  PLD  Pullback50  $95.64  P&L $+0.01                 |
+========================================================================+
```

### Options bot full output

```text
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T00:48:44.732908-04:00 ===

[Run context]
After hours (00:48 ET) — exit summary only.
Paper auth OK — equity $122587.99, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $122,587.99                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             4                                       |
|  Broker option positions       2                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=292  buckets=46  win=36%                             |
|  Returns   avg=+14.5%  med=-20.0%  p10=-77.0%  p90=+92.9%              |
|  Realized  $+4,345.77                                                  |
|  Raw incl dropped  trades=395  real=$+3,222.58                         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b28  c028_s165_w1_0928_  8 100% +84.7 +84.5 +102.0 $   +358           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b99  c099_s163_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b89  c089_s165_w2_1005_  4  75% +220.0 +69.9 +790.0 $   +127          |
|  ... 38 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 14   0% -62.5 -73.0 -98.5 $   -585       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b48  S165 AVGO260717C00400000 x1 EOD                                  |
|  b0   S173 UAL260717C00122000 x1 EOD                                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (2)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  UAL260717C00122000            3    -46.2%   $    -90.00               |
|  AVGO260717C00400000           1    -75.9%   $    -47.17               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=2.4s reconcile=2.17s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=2.4s. run=#4248 https://github.com/28twagg-ops/TradingBot/actions/runs/29555732790
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 5.6% (22/395)
```

---

## Run 20260717T130042Z

- UTC timestamp: `20260717T130042Z`
- GitHub run: [#4249](https://github.com/28twagg-ops/TradingBot/actions/runs/29582295718)
- Run id: `29582295718`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`4s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T09:00:44.454803-04:00","date":"2026-07-17","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":2.4,"phases_s":{"reconcile":2.17},"signals":0,"placed":0,"equity":121538.03,"open_positions":2,"pending_orders":0,"open_lots":4,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4249","github_run_id":"29582295718","status":"ok"}
```

### Live bot full output

```text
13:00:43  INFO      Mode: summary
13:00:43  INFO        Daily log -> logs/daily/2026-07-17.md
13:00:43  INFO        Daily log reconciled -> logs/daily/2026-07-17.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:00 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $485.23|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $485.23|
|  Cash                                                            $24.24|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $460.99|
|  Open P&L                                                        $+2.67|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (5 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CARR     Pullback50      $87.89     $67.89   $69.37   +2.2%   $+1.87  |
|  CMS      Pullback50      $96.91     $74.35   $74.45   +0.1%   $+0.13  |
|  CNP      Pullback50      $97.61     $43.13   $43.50   +0.9%   $+0.84  |
|  DOV      Pullback50      $81.85     $217.58  $217.51  -0.0%   $-0.03  |
|  DRI      Pullback50      $96.72     $201.51  $201.21  -0.1%   $-0.14  |
|                                                                        |
|  Total invested                                                 $460.99|
|  Total open P&L                                                  $+2.67|
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
|  2026-07-16  SELL  MO  Pullback50  $24.34  P&L $-0.14                  |
|  2026-07-16  SELL  CASY  Pullback50  $96.04  P&L $-0.71                |
|  2026-07-16  SELL  CHH  Pullback50  $98.47  P&L $+2.83                 |
|  2026-07-16  SELL  HST  Pullback50  $92.15  P&L $+2.55                 |
|  2026-07-16  SELL  EVR  Pullback50  $96.47  P&L $+0.83                 |
|  2026-07-14  SELL  PLD  Pullback50  $95.64  P&L $+0.01                 |
+========================================================================+
```

### Options bot full output

```text
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T09:00:44.454803-04:00 ===

[Run context]
After hours (09:00 ET) — exit summary only.
Paper auth OK — equity $121538.03, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $121,538.03                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             4                                       |
|  Broker option positions       2                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=292  buckets=46  win=36%                             |
|  Returns   avg=+14.5%  med=-20.0%  p10=-77.0%  p90=+92.9%              |
|  Realized  $+4,345.77                                                  |
|  Raw incl dropped  trades=395  real=$+3,222.58                         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b28  c028_s165_w1_0928_  8 100% +84.7 +84.5 +102.0 $   +358           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b99  c099_s163_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b89  c089_s165_w2_1005_  4  75% +220.0 +69.9 +790.0 $   +127          |
|  ... 38 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 14   0% -62.5 -73.0 -98.5 $   -585       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b48  S165 AVGO260717C00400000 x1 EOD                                  |
|  b0   S173 UAL260717C00122000 x1 EOD                                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (2)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  UAL260717C00122000            3    -46.2%   $    -90.00               |
|  AVGO260717C00400000           1    -75.9%   $    -47.17               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=2.4s reconcile=2.17s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=2.4s. run=#4249 https://github.com/28twagg-ops/TradingBot/actions/runs/29582295718
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 5.6% (22/395)
```

---

## Run 20260717T130533Z

- UTC timestamp: `20260717T130533Z`
- GitHub run: [#4250](https://github.com/28twagg-ops/TradingBot/actions/runs/29582609258)
- Run id: `29582609258`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`4s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T09:05:35.405079-04:00","date":"2026-07-17","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":2.7,"phases_s":{"reconcile":2.52},"signals":0,"placed":0,"equity":121578.63,"open_positions":2,"pending_orders":0,"open_lots":4,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4250","github_run_id":"29582609258","status":"ok"}
```

### Live bot full output

```text
13:05:34  INFO      Mode: summary
13:05:34  INFO        Daily log -> logs/daily/2026-07-17.md
13:05:34  INFO        Daily log reconciled -> logs/daily/2026-07-17.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:05 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $485.13|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $485.13|
|  Cash                                                            $24.24|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $460.89|
|  Open P&L                                                        $+2.57|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (5 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CARR     Pullback50      $87.79     $67.89   $69.29   +2.1%   $+1.77  |
|  CMS      Pullback50      $96.91     $74.35   $74.45   +0.1%   $+0.13  |
|  CNP      Pullback50      $97.61     $43.13   $43.50   +0.9%   $+0.84  |
|  DOV      Pullback50      $81.85     $217.58  $217.51  -0.0%   $-0.03  |
|  DRI      Pullback50      $96.72     $201.51  $201.21  -0.1%   $-0.14  |
|                                                                        |
|  Total invested                                                 $460.89|
|  Total open P&L                                                  $+2.57|
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
|  2026-07-16  SELL  MO  Pullback50  $24.34  P&L $-0.14                  |
|  2026-07-16  SELL  CASY  Pullback50  $96.04  P&L $-0.71                |
|  2026-07-16  SELL  CHH  Pullback50  $98.47  P&L $+2.83                 |
|  2026-07-16  SELL  HST  Pullback50  $92.15  P&L $+2.55                 |
|  2026-07-16  SELL  EVR  Pullback50  $96.47  P&L $+0.83                 |
|  2026-07-14  SELL  PLD  Pullback50  $95.64  P&L $+0.01                 |
+========================================================================+
```

### Options bot full output

```text
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T09:05:35.405079-04:00 ===

[Run context]
After hours (09:05 ET) — exit summary only.
Paper auth OK — equity $121578.63, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $121,578.63                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             4                                       |
|  Broker option positions       2                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=292  buckets=46  win=36%                             |
|  Returns   avg=+14.5%  med=-20.0%  p10=-77.0%  p90=+92.9%              |
|  Realized  $+4,345.77                                                  |
|  Raw incl dropped  trades=395  real=$+3,222.58                         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b28  c028_s165_w1_0928_  8 100% +84.7 +84.5 +102.0 $   +358           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b99  c099_s163_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b89  c089_s165_w2_1005_  4  75% +220.0 +69.9 +790.0 $   +127          |
|  ... 38 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 14   0% -62.5 -73.0 -98.5 $   -585       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b48  S165 AVGO260717C00400000 x1 EOD                                  |
|  b0   S173 UAL260717C00122000 x1 EOD                                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (2)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  UAL260717C00122000            3    -46.2%   $    -90.00               |
|  AVGO260717C00400000           1    -75.9%   $    -47.17               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=2.7s reconcile=2.52s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=2.7s. run=#4250 https://github.com/28twagg-ops/TradingBot/actions/runs/29582609258
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 5.6% (22/395)
```

---

## Run 20260717T131034Z

- UTC timestamp: `20260717T131034Z`
- GitHub run: [#4251](https://github.com/28twagg-ops/TradingBot/actions/runs/29582918009)
- Run id: `29582918009`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`4s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T09:10:37.354342-04:00","date":"2026-07-17","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":2.4,"phases_s":{"reconcile":2.03},"signals":0,"placed":0,"equity":121362.63,"open_positions":2,"pending_orders":0,"open_lots":4,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4251","github_run_id":"29582918009","status":"ok"}
```

### Live bot full output

```text
13:10:35  INFO      Mode: summary
13:10:36  INFO        Daily log -> logs/daily/2026-07-17.md
13:10:36  INFO        Daily log reconciled -> logs/daily/2026-07-17.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $484.43|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $484.43|
|  Cash                                                            $24.24|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $460.19|
|  Open P&L                                                        $+1.88|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (5 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CARR     Pullback50      $87.09     $67.89   $68.74   +1.2%   $+1.07  |
|  CMS      Pullback50      $96.91     $74.35   $74.45   +0.1%   $+0.13  |
|  CNP      Pullback50      $97.61     $43.13   $43.50   +0.9%   $+0.84  |
|  DOV      Pullback50      $81.85     $217.58  $217.51  -0.0%   $-0.03  |
|  DRI      Pullback50      $96.72     $201.51  $201.21  -0.1%   $-0.14  |
|                                                                        |
|  Total invested                                                 $460.19|
|  Total open P&L                                                  $+1.88|
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
|  2026-07-16  SELL  MO  Pullback50  $24.34  P&L $-0.14                  |
|  2026-07-16  SELL  CASY  Pullback50  $96.04  P&L $-0.71                |
|  2026-07-16  SELL  CHH  Pullback50  $98.47  P&L $+2.83                 |
|  2026-07-16  SELL  HST  Pullback50  $92.15  P&L $+2.55                 |
|  2026-07-16  SELL  EVR  Pullback50  $96.47  P&L $+0.83                 |
|  2026-07-14  SELL  PLD  Pullback50  $95.64  P&L $+0.01                 |
+========================================================================+
```

### Options bot full output

```text
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T09:10:37.354342-04:00 ===

[Run context]
After hours (09:10 ET) — exit summary only.
Paper auth OK — equity $121362.63, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $121,362.63                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             4                                       |
|  Broker option positions       2                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=292  buckets=46  win=36%                             |
|  Returns   avg=+14.5%  med=-20.0%  p10=-77.0%  p90=+92.9%              |
|  Realized  $+4,345.77                                                  |
|  Raw incl dropped  trades=395  real=$+3,222.58                         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b28  c028_s165_w1_0928_  8 100% +84.7 +84.5 +102.0 $   +358           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b99  c099_s163_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b89  c089_s165_w2_1005_  4  75% +220.0 +69.9 +790.0 $   +127          |
|  ... 38 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 14   0% -62.5 -73.0 -98.5 $   -585       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b48  S165 AVGO260717C00400000 x1 EOD                                  |
|  b0   S173 UAL260717C00122000 x1 EOD                                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (2)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  UAL260717C00122000            3    -46.2%   $    -90.00               |
|  AVGO260717C00400000           1    -75.9%   $    -47.17               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=2.4s reconcile=2.03s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=2.4s. run=#4251 https://github.com/28twagg-ops/TradingBot/actions/runs/29582918009
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 5.6% (22/395)
```

---

## Run 20260717T131536Z

- UTC timestamp: `20260717T131536Z`
- GitHub run: [#4252](https://github.com/28twagg-ops/TradingBot/actions/runs/29583232816)
- Run id: `29583232816`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`5s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T09:15:39.838699-04:00","date":"2026-07-17","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":4.3,"phases_s":{"reconcile":3.81},"signals":0,"placed":0,"equity":121246.63,"open_positions":2,"pending_orders":0,"open_lots":4,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4252","github_run_id":"29583232816","status":"ok"}
```

### Live bot full output

```text
13:15:37  INFO      Mode: summary
13:15:38  INFO        Daily log -> logs/daily/2026-07-17.md
13:15:38  INFO        Daily log reconciled -> logs/daily/2026-07-17.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:15 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $483.31|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $483.31|
|  Cash                                                            $24.24|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $459.07|
|  Open P&L                                                        $+0.75|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (5 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CARR     Pullback50      $86.79     $67.89   $68.50   +0.9%   $+0.77  |
|  CMS      Pullback50      $96.09     $74.35   $73.82   -0.7%   $-0.69  |
|  CNP      Pullback50      $97.61     $43.13   $43.50   +0.9%   $+0.84  |
|  DOV      Pullback50      $81.85     $217.58  $217.51  -0.0%   $-0.03  |
|  DRI      Pullback50      $96.72     $201.51  $201.21  -0.1%   $-0.14  |
|                                                                        |
|  Total invested                                                 $459.07|
|  Total open P&L                                                  $+0.75|
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
|  2026-07-16  SELL  MO  Pullback50  $24.34  P&L $-0.14                  |
|  2026-07-16  SELL  CASY  Pullback50  $96.04  P&L $-0.71                |
|  2026-07-16  SELL  CHH  Pullback50  $98.47  P&L $+2.83                 |
|  2026-07-16  SELL  HST  Pullback50  $92.15  P&L $+2.55                 |
|  2026-07-16  SELL  EVR  Pullback50  $96.47  P&L $+0.83                 |
|  2026-07-14  SELL  PLD  Pullback50  $95.64  P&L $+0.01                 |
+========================================================================+
```

### Options bot full output

```text
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T09:15:39.838699-04:00 ===

[Run context]
After hours (09:15 ET) — exit summary only.
Paper auth OK — equity $121246.63, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $121,246.63                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             4                                       |
|  Broker option positions       2                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=292  buckets=46  win=36%                             |
|  Returns   avg=+14.5%  med=-20.0%  p10=-77.0%  p90=+92.9%              |
|  Realized  $+4,345.77                                                  |
|  Raw incl dropped  trades=395  real=$+3,222.58                         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b28  c028_s165_w1_0928_  8 100% +84.7 +84.5 +102.0 $   +358           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b99  c099_s163_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b89  c089_s165_w2_1005_  4  75% +220.0 +69.9 +790.0 $   +127          |
|  ... 38 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 14   0% -62.5 -73.0 -98.5 $   -585       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b48  S165 AVGO260717C00400000 x1 EOD                                  |
|  b0   S173 UAL260717C00122000 x1 EOD                                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (2)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  UAL260717C00122000            3    -46.2%   $    -90.00               |
|  AVGO260717C00400000           1    -75.9%   $    -47.17               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=4.3s reconcile=3.81s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=4.3s. run=#4252 https://github.com/28twagg-ops/TradingBot/actions/runs/29583232816
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 5.6% (22/395)
```

---

## Run 20260717T132039Z

- UTC timestamp: `20260717T132039Z`
- GitHub run: [#4253](https://github.com/28twagg-ops/TradingBot/actions/runs/29583549886)
- Run id: `29583549886`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`5s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T09:20:42.715016-04:00","date":"2026-07-17","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":3.0,"phases_s":{"reconcile":2.65},"signals":0,"placed":0,"equity":121250.63,"open_positions":2,"pending_orders":0,"open_lots":4,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4253","github_run_id":"29583549886","status":"ok"}
```

### Live bot full output

```text
13:20:40  INFO      Mode: summary
13:20:41  INFO        Daily log -> logs/daily/2026-07-17.md
13:20:41  INFO        Daily log reconciled -> logs/daily/2026-07-17.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $483.31|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $483.31|
|  Cash                                                            $24.24|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $459.07|
|  Open P&L                                                        $+0.75|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (5 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CARR     Pullback50      $86.79     $67.89   $68.50   +0.9%   $+0.77  |
|  CMS      Pullback50      $96.09     $74.35   $73.82   -0.7%   $-0.69  |
|  CNP      Pullback50      $97.61     $43.13   $43.50   +0.9%   $+0.84  |
|  DOV      Pullback50      $81.85     $217.58  $217.51  -0.0%   $-0.03  |
|  DRI      Pullback50      $96.72     $201.51  $201.21  -0.1%   $-0.14  |
|                                                                        |
|  Total invested                                                 $459.07|
|  Total open P&L                                                  $+0.75|
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
|  2026-07-16  SELL  MO  Pullback50  $24.34  P&L $-0.14                  |
|  2026-07-16  SELL  CASY  Pullback50  $96.04  P&L $-0.71                |
|  2026-07-16  SELL  CHH  Pullback50  $98.47  P&L $+2.83                 |
|  2026-07-16  SELL  HST  Pullback50  $92.15  P&L $+2.55                 |
|  2026-07-16  SELL  EVR  Pullback50  $96.47  P&L $+0.83                 |
|  2026-07-14  SELL  PLD  Pullback50  $95.64  P&L $+0.01                 |
+========================================================================+
```

### Options bot full output

```text
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T09:20:42.715016-04:00 ===

[Run context]
After hours (09:20 ET) — exit summary only.
Paper auth OK — equity $121250.63, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $121,250.63                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             4                                       |
|  Broker option positions       2                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=292  buckets=46  win=36%                             |
|  Returns   avg=+14.5%  med=-20.0%  p10=-77.0%  p90=+92.9%              |
|  Realized  $+4,345.77                                                  |
|  Raw incl dropped  trades=395  real=$+3,222.58                         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b28  c028_s165_w1_0928_  8 100% +84.7 +84.5 +102.0 $   +358           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b99  c099_s163_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b89  c089_s165_w2_1005_  4  75% +220.0 +69.9 +790.0 $   +127          |
|  ... 38 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 14   0% -62.5 -73.0 -98.5 $   -585       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b48  S165 AVGO260717C00400000 x1 EOD                                  |
|  b0   S173 UAL260717C00122000 x1 EOD                                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (2)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  UAL260717C00122000            3    -46.2%   $    -90.00               |
|  AVGO260717C00400000           1    -75.9%   $    -47.17               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=3.0s reconcile=2.65s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=3.0s. run=#4253 https://github.com/28twagg-ops/TradingBot/actions/runs/29583549886
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 5.6% (22/395)
```

---

## Run 20260717T132539Z

- UTC timestamp: `20260717T132539Z`
- GitHub run: [#4254](https://github.com/28twagg-ops/TradingBot/actions/runs/29583870266)
- Run id: `29583870266`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`4s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T09:25:42.343477-04:00","date":"2026-07-17","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":2.4,"phases_s":{"reconcile":2.14},"signals":0,"placed":0,"equity":121590.59,"open_positions":2,"pending_orders":0,"open_lots":4,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4254","github_run_id":"29583870266","status":"ok"}
```

### Live bot full output

```text
13:25:41  INFO      Mode: summary
13:25:41  INFO        Daily log -> logs/daily/2026-07-17.md
13:25:41  INFO        Daily log reconciled -> logs/daily/2026-07-17.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:25 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $483.88|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $483.88|
|  Cash                                                            $24.24|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $459.64|
|  Open P&L                                                        $+1.32|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (5 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CARR     Pullback50      $87.36     $67.89   $68.95   +1.6%   $+1.34  |
|  CMS      Pullback50      $96.09     $74.35   $73.82   -0.7%   $-0.69  |
|  CNP      Pullback50      $97.61     $43.13   $43.50   +0.9%   $+0.84  |
|  DOV      Pullback50      $81.85     $217.58  $217.51  -0.0%   $-0.03  |
|  DRI      Pullback50      $96.72     $201.51  $201.21  -0.1%   $-0.14  |
|                                                                        |
|  Total invested                                                 $459.64|
|  Total open P&L                                                  $+1.32|
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
|  2026-07-16  SELL  MO  Pullback50  $24.34  P&L $-0.14                  |
|  2026-07-16  SELL  CASY  Pullback50  $96.04  P&L $-0.71                |
|  2026-07-16  SELL  CHH  Pullback50  $98.47  P&L $+2.83                 |
|  2026-07-16  SELL  HST  Pullback50  $92.15  P&L $+2.55                 |
|  2026-07-16  SELL  EVR  Pullback50  $96.47  P&L $+0.83                 |
|  2026-07-14  SELL  PLD  Pullback50  $95.64  P&L $+0.01                 |
+========================================================================+
```

### Options bot full output

```text
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T09:25:42.343477-04:00 ===

[Run context]
After hours (09:25 ET) — exit summary only.
Paper auth OK — equity $121590.59, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $121,590.59                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             4                                       |
|  Broker option positions       2                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=292  buckets=46  win=36%                             |
|  Returns   avg=+14.5%  med=-20.0%  p10=-77.0%  p90=+92.9%              |
|  Realized  $+4,345.77                                                  |
|  Raw incl dropped  trades=395  real=$+3,222.58                         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b28  c028_s165_w1_0928_  8 100% +84.7 +84.5 +102.0 $   +358           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b99  c099_s163_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b89  c089_s165_w2_1005_  4  75% +220.0 +69.9 +790.0 $   +127          |
|  ... 38 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 14   0% -62.5 -73.0 -98.5 $   -585       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b48  S165 AVGO260717C00400000 x1 EOD                                  |
|  b0   S173 UAL260717C00122000 x1 EOD                                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (2)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  UAL260717C00122000            3    -46.2%   $    -90.00               |
|  AVGO260717C00400000           1    -75.9%   $    -47.17               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=2.4s reconcile=2.14s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=2.4s. run=#4254 https://github.com/28twagg-ops/TradingBot/actions/runs/29583870266
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 5.6% (22/395)
```

---

## Run 20260717T132905Z

- UTC timestamp: `20260717T132905Z`
- GitHub run: [#4255](https://github.com/28twagg-ops/TradingBot/actions/runs/29584093670)
- Run id: `29584093670`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`12s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T09:29:07.852270-04:00","date":"2026-07-17","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":10.5,"phases_s":{"reconcile":2.19,"cancel":0.04,"manage":0.04,"scan":7.18,"entries":0.1},"signals":0,"placed":0,"equity":121738.63,"open_positions":2,"pending_orders":0,"open_lots":4,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4255","github_run_id":"29584093670","status":"ok"}
```

### Live bot full output

```text
13:29:06  INFO      Mode: summary
13:29:06  INFO        Daily log -> logs/daily/2026-07-17.md
13:29:06  INFO        Daily log reconciled -> logs/daily/2026-07-17.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:29 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $483.88|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $483.88|
|  Cash                                                            $24.24|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $459.64|
|  Open P&L                                                        $+1.32|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (5 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CARR     Pullback50      $87.36     $67.89   $68.95   +1.6%   $+1.34  |
|  CMS      Pullback50      $96.09     $74.35   $73.82   -0.7%   $-0.69  |
|  CNP      Pullback50      $97.61     $43.13   $43.50   +0.9%   $+0.84  |
|  DOV      Pullback50      $81.85     $217.58  $217.51  -0.0%   $-0.03  |
|  DRI      Pullback50      $96.72     $201.51  $201.21  -0.1%   $-0.14  |
|                                                                        |
|  Total invested                                                 $459.64|
|  Total open P&L                                                  $+1.32|
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
|  2026-07-16  SELL  MO  Pullback50  $24.34  P&L $-0.14                  |
|  2026-07-16  SELL  CASY  Pullback50  $96.04  P&L $-0.71                |
|  2026-07-16  SELL  CHH  Pullback50  $98.47  P&L $+2.83                 |
|  2026-07-16  SELL  HST  Pullback50  $92.15  P&L $+2.55                 |
|  2026-07-16  SELL  EVR  Pullback50  $96.47  P&L $+0.83                 |
|  2026-07-14  SELL  PLD  Pullback50  $95.64  P&L $+0.01                 |
+========================================================================+
```

### Options bot full output

```text
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T09:29:07.852270-04:00 ===

[Run context]
Paper auth OK — equity $121738.63, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Scan + entries]
2026-07-17 09:29:10,246 INFO Fetching universe from Wikipedia (S&P 500 + S&P 400) …
2026-07-17 09:29:10,622 INFO   S&P 500: 503 tickers
2026-07-17 09:29:10,967 INFO   S&P 400 MidCap: 400 tickers
2026-07-17 09:29:10,967 INFO   Universe total: 903 tickers
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 0 signals across top-5 strategies
Paper lab: $121719 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  All bucket slots blocked or closed for today's signals — skip entry loop.
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $121,738.63                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             4                                       |
|  Broker option positions       2                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=292  buckets=46  win=36%                             |
|  Returns   avg=+14.5%  med=-20.0%  p10=-77.0%  p90=+92.9%              |
|  Realized  $+4,345.77                                                  |
|  Raw incl dropped  trades=395  real=$+3,222.58                         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b28  c028_s165_w1_0928_  8 100% +84.7 +84.5 +102.0 $   +358           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b99  c099_s163_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b89  c089_s165_w2_1005_  4  75% +220.0 +69.9 +790.0 $   +127          |
|  ... 38 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 14   0% -62.5 -73.0 -98.5 $   -585       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b48  S165 AVGO260717C00400000 x1 EOD                                  |
|  b0   S173 UAL260717C00122000 x1 EOD                                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (2)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  UAL260717C00122000            3    -46.2%   $    -90.00               |
|  AVGO260717C00400000           1    -75.9%   $    -47.17               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=10.5s reconcile=2.19s cancel=0.04s manage=0.04s scan=7.18s entries=0.1s
STATUS: options_morning_bot run complete (PAPER) elapsed=10.5s. run=#4255 https://github.com/28twagg-ops/TradingBot/actions/runs/29584093670
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 5.6% (22/395)
```

---

## Run 20260717T133035Z

- UTC timestamp: `20260717T133035Z`
- GitHub run: [#4256](https://github.com/28twagg-ops/TradingBot/actions/runs/29584185897)
- Run id: `29584185897`
- Live bot: exit=`0`, duration=`215s`
- Options bot: exit=`0`, duration=`34s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T09:34:11.667221-04:00","date":"2026-07-17","mode":"entry+manage","header":"entry+manage (8 new)","elapsed_s":31.9,"phases_s":{"reconcile":2.12,"cancel":0.03,"manage":0.27,"scan":26.02,"entries":1.05,"reconcile2":2.14},"signals":179,"placed":8,"equity":120427.59,"open_positions":2,"pending_orders":5,"open_lots":5,"submitted_today":8,"filled_today":3,"unattributed_contracts":0,"top_signals":["S173:AKAM","S173:ALB","S173:AMZN","S173:AMP","S173:AME","S173:APP","S173:ARES","S173:AXON"],"github_run":"4256","github_run_id":"29584185897","status":"ok"}
```

### Live bot full output

```text
13:30:36  INFO      Mode: morning_prep
13:30:37  INFO        [prep_positions] 5/5 (5 valid)
13:30:37  INFO        Universe cache hit: 903 tickers (tickers_2026-07-17.json)
13:30:38  INFO        [prep_universe] 40/898 (40 valid)
13:30:39  INFO        [prep_universe] 80/898 (80 valid)
13:30:41  INFO        [prep_universe] 120/898 (120 valid)
13:30:42  INFO        [prep_universe] 160/898 (160 valid)
13:30:43  INFO        [prep_universe] 200/898 (199 valid)
13:30:51  INFO        [prep_universe] 240/898 (238 valid)
13:31:04  INFO        [prep_universe] 280/898 (278 valid)
13:31:17  INFO        [prep_universe] 320/898 (318 valid)
13:31:27  INFO        [prep_universe] 360/898 (358 valid)
13:31:41  INFO        [prep_universe] 400/898 (397 valid)
13:31:51  INFO        [prep_universe] 440/898 (437 valid)
13:32:04  INFO        [prep_universe] 480/898 (477 valid)
13:32:17  INFO        [prep_universe] 520/898 (517 valid)
13:32:27  INFO        [prep_universe] 560/898 (556 valid)
13:32:40  INFO        [prep_universe] 600/898 (596 valid)
13:32:50  INFO        [prep_universe] 640/898 (636 valid)
13:33:03  INFO        [prep_universe] 680/898 (676 valid)
13:33:16  INFO        [prep_universe] 720/898 (716 valid)
13:33:27  INFO        [prep_universe] 760/898 (756 valid)
13:33:40  INFO        [prep_universe] 800/898 (796 valid)
13:33:53  INFO        [prep_universe] 840/898 (835 valid)
13:34:03  INFO        [prep_universe] 880/898 (875 valid)
13:34:09  INFO        [prep_universe] 898/898 (893 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:30 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $484.43|
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
|  Invested                                                       $460.35|
|  Open P&L                                                        $+2.03|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CARR     Pullback50      $85.95     $67.89   $67.84   -0.1%   $-0.07  |
|  CMS      Pullback50      $97.90     $74.35   $75.21   +1.2%   $+1.12  |
|  CNP      Pullback50      $98.29     $43.13   $43.80   +1.6%   $+1.51  |
|  DOV      Pullback50      $80.63     $217.58  $214.26  -1.5%   $-1.25  |
|  DRI      Pullback50      $97.58     $201.51  $203.00  +0.7%   $+0.72  |
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
|  Signal candidates                                                   61|
|  Universe scanned                                                   898|
+========================================================================+
```

### Options bot full output

```text
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T09:34:11.667221-04:00 ===

[Run context]
Paper auth OK — equity $120427.59, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-17 09:34:14,175 INFO   EXIT [b40|c040_s173_w1_0928_1005_r3|S173] stop_loss (-100.0%) SELL 1 UAL260717C00122000 @<= 0.01

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 179 signal(s); top: ['S173:AKAM', 'S173:ALB', 'S173:AMZN', 'S173:AMP', 'S173:AME', 'S173:APP', 'S173:ARES', 'S173:AXON']
Paper lab: $120346 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 11 no tradeable call, 670 pending order
Placed 8 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $120,427.59                             |
|  Signals this run              179                                     |
|  Orders submitted (session)    8                                       |
|  Orders filled today (ledger)  3                                       |
|  Entries placed this run       8                                       |
|  Open virtual lots             5                                       |
|  Broker option positions       2                                       |
|  Pending orders                5                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=294  buckets=46  win=36%                             |
|  Returns   avg=+13.7%  med=-21.4%  p10=-77.7%  p90=+92.4%              |
|  Realized  $+4,216.77                                                  |
|  Raw incl dropped  trades=397  real=$+3,093.58                         |
|  Today     trades=2  avg=-93.5%  med=-93.5%  real=$-129.00             |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b28  c028_s165_w1_0928_  8 100% +84.7 +84.5 +102.0 $   +358           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b99  c099_s163_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b89  c089_s165_w2_1005_  4  75% +220.0 +69.9 +790.0 $   +127          |
|  ... 38 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 14   0% -62.5 -73.0 -98.5 $   -585       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (5)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S165:GOOGL(5)                           |
+------------------------------------------------------------------------+
|  b8   S165 GOOGL    limit=0.55                                         |
|  b28  S165 GOOGL    limit=0.55                                         |
|  b48  S165 GOOGL    limit=0.55                                         |
|  b68  S165 GOOGL    limit=0.55                                         |
|  b88  S165 GOOGL    limit=0.55                                         |
+========================================================================+
+========================================================================+
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b40  S173 UAL260717C00122000 x1 stop_loss (-100.0%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (2)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  UAL260717C00122000            2   -100.0%   $   -130.00               |
|  AMZN260717C00250000           3     -2.0%   $     -3.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=31.9s reconcile=2.12s cancel=0.03s manage=0.27s scan=26.02s entries=1.05s
STATUS: options_morning_bot run complete (PAPER) elapsed=31.9s. run=#4256 https://github.com/28twagg-ops/TradingBot/actions/runs/29584185897
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 2 buckets closed trades, $-129.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 5.5% (22/397)
```

---

## Run 20260717T133535Z

- UTC timestamp: `20260717T133535Z`
- GitHub run: [#4257](https://github.com/28twagg-ops/TradingBot/actions/runs/29584515655)
- Run id: `29584515655`
- Live bot: exit=`0`, duration=`214s`
- Options bot: exit=`0`, duration=`23s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T09:39:10.710820-04:00","date":"2026-07-17","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":21.6,"phases_s":{"reconcile":2.21,"cancel":0.02,"manage":0.91,"scan":18.22,"entries":0.05},"signals":178,"placed":0,"equity":119880.39,"open_positions":3,"pending_orders":0,"open_lots":10,"submitted_today":8,"filled_today":8,"unattributed_contracts":0,"top_signals":["S173:ALB","S173:AMZN","S173:AMP","S173:AME","S173:APP","S173:ARES","S173:BLK","S173:BX"],"github_run":"4257","github_run_id":"29584515655","status":"ok"}
```

### Live bot full output

```text
13:35:36  INFO      Mode: morning_prep
13:35:37  INFO        [prep_positions] 5/5 (5 valid)
13:35:37  INFO        Universe cache hit: 903 tickers (tickers_2026-07-17.json)
13:35:38  INFO        [prep_universe] 40/898 (40 valid)
13:35:39  INFO        [prep_universe] 80/898 (80 valid)
13:35:41  INFO        [prep_universe] 120/898 (120 valid)
13:35:42  INFO        [prep_universe] 160/898 (160 valid)
13:35:43  INFO        [prep_universe] 200/898 (199 valid)
13:35:53  INFO        [prep_universe] 240/898 (238 valid)
13:36:03  INFO        [prep_universe] 280/898 (278 valid)
13:36:15  INFO        [prep_universe] 320/898 (318 valid)
13:36:28  INFO        [prep_universe] 360/898 (358 valid)
13:36:41  INFO        [prep_universe] 400/898 (397 valid)
13:36:51  INFO        [prep_universe] 440/898 (437 valid)
13:37:04  INFO        [prep_universe] 480/898 (477 valid)
13:37:17  INFO        [prep_universe] 520/898 (517 valid)
13:37:27  INFO        [prep_universe] 560/898 (556 valid)
13:37:40  INFO        [prep_universe] 600/898 (596 valid)
13:37:53  INFO        [prep_universe] 640/898 (636 valid)
13:38:03  INFO        [prep_universe] 680/898 (676 valid)
13:38:16  INFO        [prep_universe] 720/898 (716 valid)
13:38:29  INFO        [prep_universe] 760/898 (756 valid)
13:38:39  INFO        [prep_universe] 800/898 (796 valid)
13:38:52  INFO        [prep_universe] 840/898 (835 valid)
13:39:05  INFO        [prep_universe] 880/898 (875 valid)
13:39:08  INFO        [prep_universe] 898/898 (893 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:35 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $484.49|
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
|  Invested                                                       $460.25|
|  Open P&L                                                        $+1.94|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CARR     Pullback50      $85.75     $67.89   $67.68   -0.3%   $-0.27  |
|  CMS      Pullback50      $98.07     $74.35   $75.34   +1.3%   $+1.29  |
|  CNP      Pullback50      $98.66     $43.13   $43.97   +1.9%   $+1.88  |
|  DOV      Pullback50      $80.80     $217.58  $214.71  -1.3%   $-1.08  |
|  DRI      Pullback50      $96.97     $201.51  $201.74  +0.1%   $+0.11  |
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
|  Signal candidates                                                   37|
|  Universe scanned                                                   898|
+========================================================================+
```

### Options bot full output

```text
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T09:39:10.710820-04:00 ===

[Run context]
Paper auth OK — equity $119880.39, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 178 signal(s); top: ['S173:ALB', 'S173:AMZN', 'S173:AMP', 'S173:AME', 'S173:APP', 'S173:ARES', 'S173:BLK', 'S173:BX']
Paper lab: $119583 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  All bucket slots blocked or closed for today's signals — skip entry loop.
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $119,880.39                             |
|  Signals this run              178                                     |
|  Orders submitted (session)    8                                       |
|  Orders filled today (ledger)  8                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             10                                      |
|  Broker option positions       3                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=296  buckets=46  win=35%                             |
|  Returns   avg=+13.3%  med=-22.9%  p10=-77.5%  p90=+92.0%              |
|  Realized  $+4,158.77                                                  |
|  Raw incl dropped  trades=399  real=$+3,035.58                         |
|  Today     trades=2  avg=-93.5%  med=-93.5%  real=$-129.00             |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b28  c028_s165_w1_0928_  9  89% +69.4 +81.8 +102.0 $   +329           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b99  c099_s163_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b89  c089_s165_w2_1005_  4  75% +220.0 +69.9 +790.0 $   +127          |
|  ... 38 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 14   0% -62.5 -73.0 -98.5 $   -585       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b40  S173 UAL260717C00122000 x1 stop_loss (-100.0%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (3)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  UAL260717C00122000            2   -100.0%   $   -130.00               |
|  GOOGL260720C00360000          5    -36.4%   $   -100.00               |
|  AMZN260717C00250000           3    +39.2%   $    +60.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=21.6s reconcile=2.21s cancel=0.02s manage=0.91s scan=18.22s entries=0.05s
STATUS: options_morning_bot run complete (PAPER) elapsed=21.6s. run=#4257 https://github.com/28twagg-ops/TradingBot/actions/runs/29584515655
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 2 buckets closed trades, $-129.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 5.5% (22/399)
```

---

## Run 20260717T134039Z

- UTC timestamp: `20260717T134039Z`
- GitHub run: [#4258](https://github.com/28twagg-ops/TradingBot/actions/runs/29584840531)
- Run id: `29584840531`
- Live bot: exit=`0`, duration=`215s`
- Options bot: exit=`0`, duration=`31s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T09:44:15.358451-04:00","date":"2026-07-17","mode":"entry+manage","header":"entry+manage (2 new)","elapsed_s":29.1,"phases_s":{"reconcile":2.37,"cancel":0.12,"manage":1.55,"scan":20.58,"entries":1.39,"reconcile2":2.61},"signals":188,"placed":2,"equity":118502.43,"open_positions":3,"pending_orders":0,"open_lots":12,"submitted_today":10,"filled_today":10,"unattributed_contracts":0,"top_signals":["S173:AKAM","S173:ALB","S173:AMZN","S173:AMP","S173:AME","S173:ARES","S173:BLK","S173:BX"],"github_run":"4258","github_run_id":"29584840531","status":"ok"}
```

### Live bot full output

```text
13:40:40  INFO      Mode: morning_prep
13:40:41  INFO        [prep_positions] 5/5 (5 valid)
13:40:41  INFO        Universe cache hit: 903 tickers (tickers_2026-07-17.json)
13:40:42  INFO        [prep_universe] 40/898 (40 valid)
13:40:44  INFO        [prep_universe] 80/898 (80 valid)
13:40:45  INFO        [prep_universe] 120/898 (120 valid)
13:40:47  INFO        [prep_universe] 160/898 (160 valid)
13:40:48  INFO        [prep_universe] 200/898 (199 valid)
13:40:56  INFO        [prep_universe] 240/898 (238 valid)
13:41:09  INFO        [prep_universe] 280/898 (278 valid)
13:41:20  INFO        [prep_universe] 320/898 (318 valid)
13:41:33  INFO        [prep_universe] 360/898 (358 valid)
13:41:43  INFO        [prep_universe] 400/898 (397 valid)
13:41:57  INFO        [prep_universe] 440/898 (437 valid)
13:42:07  INFO        [prep_universe] 480/898 (477 valid)
13:42:20  INFO        [prep_universe] 520/898 (517 valid)
13:42:31  INFO        [prep_universe] 560/898 (556 valid)
13:42:44  INFO        [prep_universe] 600/898 (596 valid)
13:42:57  INFO        [prep_universe] 640/898 (636 valid)
13:43:08  INFO        [prep_universe] 680/898 (676 valid)
13:43:21  INFO        [prep_universe] 720/898 (716 valid)
13:43:32  INFO        [prep_universe] 760/898 (756 valid)
13:43:45  INFO        [prep_universe] 800/898 (796 valid)
13:43:55  INFO        [prep_universe] 840/898 (835 valid)
13:44:09  INFO        [prep_universe] 880/898 (875 valid)
13:44:12  INFO        [prep_universe] 898/898 (893 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:40 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $487.02|
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
|  Invested                                                       $462.78|
|  Open P&L                                                        $+4.46|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CARR     Pullback50      $86.70     $67.89   $68.43   +0.8%   $+0.68  |
|  CMS      Pullback50      $98.55     $74.35   $75.71   +1.8%   $+1.77  |
|  CNP      Pullback50      $99.16     $43.13   $44.19   +2.5%   $+2.39  |
|  DOV      Pullback50      $81.13     $217.58  $215.58  -0.9%   $-0.75  |
|  DRI      Pullback50      $97.23     $201.51  $202.28  +0.4%   $+0.37  |
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
|  Universe scanned                                                   898|
+========================================================================+
```

### Options bot full output

```text
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T09:44:15.358451-04:00 ===

[Run context]
Paper auth OK — equity $118502.43, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 188 signal(s); top: ['S173:AKAM', 'S173:ALB', 'S173:AMZN', 'S173:AMP', 'S173:AME', 'S173:ARES', 'S173:BLK', 'S173:BX']
Paper lab: $118771 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 4 no tradeable call, 178 pending order
Placed 2 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $118,502.43                             |
|  Signals this run              188                                     |
|  Orders submitted (session)    10                                      |
|  Orders filled today (ledger)  10                                      |
|  Entries placed this run       2                                       |
|  Open virtual lots             12                                      |
|  Broker option positions       3                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=326  buckets=46  win=36%                             |
|  Returns   avg=+10.4%  med=-23.0%  p10=-77.5%  p90=+89.2%              |
|  Realized  $+3,748.77                                                  |
|  Raw incl dropped  trades=431  real=$+2,570.58                         |
|  Today     trades=2  avg=-93.5%  med=-93.5%  real=$-129.00             |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b28  c028_s165_w1_0928_ 10  90% +68.7 +80.9 +102.0 $   +363           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b99  c099_s163_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b89  c089_s165_w2_1005_  4  75% +220.0 +69.9 +790.0 $   +127          |
|  ... 38 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 15   0% -63.6 -74.0 -98.5 $   -639       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b40  S173 UAL260717C00122000 x1 stop_loss (-100.0%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (3)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  GOOGL260720C00360000          5    -49.1%   $   -135.00               |
|  UAL260717C00122000            2   -100.0%   $   -130.00               |
|  AMZN260717C00250000           5    -10.9%   $    -27.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=29.1s reconcile=2.37s cancel=0.12s manage=1.55s scan=20.58s entries=1.39s
STATUS: options_morning_bot run complete (PAPER) elapsed=29.1s. run=#4258 https://github.com/28twagg-ops/TradingBot/actions/runs/29584840531
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 2 buckets closed trades, $-129.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 5.1% (22/431)
```

---

## Run 20260717T134532Z

- UTC timestamp: `20260717T134532Z`
- GitHub run: [#4259](https://github.com/28twagg-ops/TradingBot/actions/runs/29585168628)
- Run id: `29585168628`
- Live bot: exit=`0`, duration=`244s`
- Options bot: exit=`0`, duration=`30s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T09:49:37.485578-04:00","date":"2026-07-17","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":28.4,"phases_s":{"reconcile":2.07,"cancel":0.02,"manage":1.29,"scan":24.65,"entries":0.11},"signals":199,"placed":0,"equity":119372.39,"open_positions":3,"pending_orders":0,"open_lots":12,"submitted_today":10,"filled_today":10,"unattributed_contracts":0,"top_signals":["S173:AKAM","S173:ALB","S173:AMZN","S173:AMP","S173:AME","S173:ADI","S173:APTV","S173:ARES"],"github_run":"4259","github_run_id":"29585168628","status":"ok"}
```

### Live bot full output

```text
13:45:32  INFO      Mode: morning_scan
13:45:34  INFO        [positions] 5/5 (5 valid)
13:45:34  INFO        SELL LIMIT CNP  qty=2.244011816  limit=$44.16  id=23df6c61-8b34-436f-ac75-da3cad722d54
13:46:04  INFO        SELL LIMIT filled CNP (confirmed by position check)
13:46:04  INFO        TX logged: SELL CNP  P&L 2.44%
13:46:04  INFO        Universe cache hit: 903 tickers (tickers_2026-07-17.json)
13:46:05  INFO        [universe] 40/899 (40 valid)
13:46:07  INFO        [universe] 80/899 (80 valid)
13:46:12  INFO        [universe] 120/899 (120 valid)
13:46:13  INFO        [universe] 160/899 (160 valid)
13:46:15  INFO        [universe] 200/899 (199 valid)
13:46:19  INFO        [universe] 240/899 (238 valid)
13:46:29  INFO        [universe] 280/899 (278 valid)
13:46:42  INFO        [universe] 320/899 (318 valid)
13:46:52  INFO        [universe] 360/899 (358 valid)
13:47:05  INFO        [universe] 400/899 (397 valid)
13:47:18  INFO        [universe] 440/899 (437 valid)
13:47:31  INFO        [universe] 480/899 (477 valid)
13:47:41  INFO        [universe] 520/899 (517 valid)
13:47:54  INFO        [universe] 560/899 (556 valid)
13:48:06  INFO        [universe] 600/899 (596 valid)
13:48:16  INFO        [universe] 640/899 (636 valid)
13:48:29  INFO        [universe] 680/899 (676 valid)
13:48:42  INFO        [universe] 720/899 (716 valid)
13:48:52  INFO        [universe] 760/899 (756 valid)
13:49:05  INFO        [universe] 800/899 (796 valid)
13:49:18  INFO        [universe] 840/899 (835 valid)
13:49:31  INFO        [universe] 880/899 (875 valid)
13:49:35  INFO        [universe] 899/899 (894 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_SCAN|
|  Time                                                         13:45 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $487.94|
+========================================================================+

+========================================================================+
|                   RUBBER BAND BOT v8  --  DAILY SCAN                   |
+========================================================================+
|  Mode                                                      *** LIVE ***|
|  Date                                                        2026-07-17|
|  Universe                                                          both|
|  Month                                        Jul: 52wkLow + Pullback50|
|  Regime                                                            BULL|
|  Exit                                      midline / stop-0.5% / 3d max|
+========================================================================+

+========================================================================+
|                                ACCOUNT                                 |
+========================================================================+
|  Equity                                                         $487.94|
|  Cash                                                            $24.24|
|  Reserve                                          $24.40  (always kept)|
|  Available                                      $0.00  (for new trades)|
|  Seasonal trade                   $97.59  (20% -- scheduled strategies)|
|  Off-sched trade                      $97.59  (20% -- other strategies)|
+========================================================================+

+========================================================================+
|                           HOLDINGS  (5 open)                           |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CARR     Pullback50      $87.51     $67.89   $69.07   +1.7%   $+1.49  |
|  CMS      Pullback50      $98.51     $74.35   $75.68   +1.8%   $+1.73  |
|  CNP      Pullback50      $99.14     $43.13   $44.18   +2.4%   $+2.36  |
|  DOV      Pullback50      $81.77     $217.58  $217.29  -0.1%   $-0.11  |
|  DRI      Pullback50      $96.76     $201.51  $201.31  -0.1%   $-0.10  |
|                                                                        |
|  Total invested                                                 $463.70|
|  Total open P&L                                                  $+5.38|
|  Buys today: 0  |  entry cap: 0  |  max open: 5                        |
+========================================================================+

+========================================================================+
|                               PLAN CACHE                               |
+========================================================================+
|  Mode                                                           morning|
|  File                                      logs/plans/morning_plan.json|
|  Use cached plan                                  no (stale (11520.1m))|
+========================================================================+

+========================================================================+
|          EXIT EVALUATION  (EOD -- midline + stop + max-hold)           |
+========================================================================+
|  DOV  P&L -0.1%  $-0.11                                            HOLD|
|  DRI  P&L -0.1%  $-0.10                                            HOLD|
|  CARR  P&L +1.7%  $+1.49                                           HOLD|
|  CMS  P&L +1.8%  $+1.73                                            HOLD|
|  CNP  P&L +2.4%  $+2.36                           EXIT: midline (+2.4%)|
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
|  Primary: 52wkLow  |  Secondary: Pullback50                            |
|  Source                                                       live scan|
+========================================================================+

+========================================================================+
|                         SIGNALS FOUND  --  42                          |
+========================================================================+
|  TICKER   STRATEGY        TIER   PRICE    RSI    VOL_Z   TRIGGER       |
+------------------------------------------------------------------------+
|  AME      Pullback50      SEAS   $233.41  44.1   -1.96   50MA bounce (+|
|  BG       Pullback50      SEAS   $118.83  65.8   -2.14   50MA bounce (-|
|  CCL      GapDown         off    $26.34   27.5   -2.10   gap -3.2% reco|
|  CAT      GapDown         off    $848.36  28.4   -1.23   gap -4.0% reco|
|  CI       Pullback50      SEAS   $289.13  54.3   -1.85   50MA bounce (+|
|  EMR      Pullback50      SEAS   $139.45  41.1   -2.06   50MA bounce (-|
|  F        Pullback50      SEAS   $14.27   52.7   -2.87   50MA bounce (+|
|  HST      Pullback50      SEAS   $23.66   32.1   -2.35   50MA bounce (+|
|  MAR      Pullback50      SEAS   $371.89  45.3   -2.59   50MA bounce (-|
|  NFLX     GapDown         off    $66.36   33.7   -1.14   gap -11.9% rec|
|  NI       Pullback50      SEAS   $46.84   36.2   -2.64   50MA bounce (-|
|  NXPI     GapDown         off    $262.25  41.4   -2.25   gap -3.9% reco|
|  OXY      Pullback50      SEAS   $54.94   67.5   -2.20   50MA bounce (+|
|  ROK      Pullback50      SEAS   $456.96  42.2   -1.02   50MA bounce (-|
|  ROK      GapDown         off    $456.96  42.2   -1.02   gap -3.0% reco|
|  TDY      Pullback50      SEAS   $626.43  51.0   -2.46   50MA bounce (+|
|  TJX      Pullback50      SEAS   $157.56  54.2   -1.99   50MA bounce (+|
|  TT       Pullback50      SEAS   $466.93  43.0   -1.89   50MA bounce (-|
|  VRSN     Pullback50      SEAS   $277.07  83.0   -1.92   50MA bounce (-|
|  WAB      Pullback50      SEAS   $262.64  36.0   -2.06   50MA bounce (-|
|  ALGM     GapDown         off    $44.75   37.7   -1.50   gap -6.0% reco|
|  ALV      GapDown         off    $119.96  51.4   -1.63   gap -4.5% reco|
|  BDC      GapDown         off    $100.02  18.8   -1.85   gap -3.0% reco|
|  DOCN     GapDown         off    $112.52  35.1   -1.22   gap -4.1% reco|13:49:36  INFO        place_all_stops: checking 4 positions...
13:49:36  INFO        STOP-MARKET placed CARR  qty=1 (pos=1.2670)  stop=$67.55  id=e3b06fff-6c14-4de5-95e1-cb325b0d5d06
13:49:36  INFO        STOP-MARKET placed CMS  qty=1 (pos=1.3017)  stop=$73.98  id=53c83293-ab31-4e91-8843-f9f8c878f3ba
13:49:36  INFO        STOP skipped DOV: fractional (0.3763 shares) — software exit will handle it
13:49:36  INFO        STOP skipped DRI: fractional (0.4807 shares) — software exit will handle it
13:49:36  INFO        Daily log -> logs/daily/2026-07-17.md
13:49:36  INFO        Dashboard written → logs/dashboard.md

|  DKS      Pullback50      SEAS   $222.14  37.4   -2.77   50MA bounce (-|
|  ENS      GapDown         off    $189.00  32.3   -1.13   gap -3.5% reco|
|  EXP      Pullback50      SEAS   $215.40  32.8   -2.21   50MA bounce (+|
|  ENTG     GapDown         off    $130.35  34.3   -2.05   gap -5.1% reco|
|  FIVE     Pullback50      SEAS   $201.81  64.4   -3.13   50MA bounce (+|
|  FLR      Pullback50      SEAS   $48.70   34.9   -1.38   50MA bounce (-|
|  FNB      GapDown         off    $19.12   48.2   -1.96   gap -3.5% reco|
|  FOUR     GapDown         off    $50.78   60.3   -1.79   gap -3.3% reco|
|  HIMS     GapDown         off    $32.51   46.1   -1.92   gap -4.8% reco|
|  IDCC     GapDown         off    $257.95  33.0   -1.64   gap -3.4% reco|
|  NOVT     GapDown         off    $146.19  39.4   -2.00   gap -3.3% reco|
|  P        GapDown         off    $67.76   48.3   -1.78   gap -3.6% reco|
|  RRX      GapDown         off    $204.49  39.9   -1.95   gap -5.3% reco|
|  SLAB     Pullback50      SEAS   $218.03  46.0   -1.01   50MA bounce (-|
|  SYNA     GapDown         off    $111.68  42.8   -0.83   gap -4.5% reco|
|  VIAV     GapDown         off    $35.63   22.5   -0.66   gap -4.2% reco|
|  VNOM     Pullback50      SEAS   $44.66   61.2   -1.97   50MA bounce (-|
|  WWD      Pullback50      SEAS   $390.11  24.2   -1.40   50MA bounce (+|
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
|  Strategy                                          52wkLow + Pullback50|
|  Scanned                                                            894|
|  Signals                                                             42|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  0 unconfirmed|
|  Exits                                                                1|
|  Open pos                                                             4|
|  Equity                                                         $488.93|
|  Cash                                                           $123.33|
+========================================================================+
```

### Options bot full output

```text
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T09:49:37.485578-04:00 ===

[Run context]
Paper auth OK — equity $119372.39, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 199 signal(s); top: ['S173:AKAM', 'S173:ALB', 'S173:AMZN', 'S173:AMP', 'S173:AME', 'S173:ADI', 'S173:APTV', 'S173:ARES']
Paper lab: $119372 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  All bucket slots blocked or closed for today's signals — skip entry loop.
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $119,372.39                             |
|  Signals this run              199                                     |
|  Orders submitted (session)    10                                      |
|  Orders filled today (ledger)  10                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             12                                      |
|  Broker option positions       3                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=329  buckets=46  win=36%                             |
|  Returns   avg=+10.5%  med=-22.9%  p10=-77.2%  p90=+90.9%              |
|  Realized  $+3,745.77                                                  |
|  Raw incl dropped  trades=436  real=$+2,515.58                         |
|  Today     trades=2  avg=-93.5%  med=-93.5%  real=$-129.00             |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b28  c028_s165_w1_0928_ 10  90% +68.7 +80.9 +102.0 $   +363           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b99  c099_s163_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b89  c089_s165_w2_1005_  4  75% +220.0 +69.9 +790.0 $   +127          |
|  ... 38 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 15   0% -63.6 -74.0 -98.5 $   -639       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b40  S173 UAL260717C00122000 x1 stop_loss (-100.0%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (3)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  GOOGL260720C00360000          5    -45.5%   $   -125.00               |
|  UAL260717C00122000            1    -98.5%   $    -64.00               |
|  AMZN260717C00250000           5    -23.1%   $    -57.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=28.4s reconcile=2.07s cancel=0.02s manage=1.29s scan=24.65s entries=0.11s
STATUS: options_morning_bot run complete (PAPER) elapsed=28.4s. run=#4259 https://github.com/28twagg-ops/TradingBot/actions/runs/29585168628
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 2 buckets closed trades, $-129.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 5.1% (22/436)
```

---

## Run 20260717T135043Z

- UTC timestamp: `20260717T135043Z`
- GitHub run: [#4260](https://github.com/28twagg-ops/TradingBot/actions/runs/29585494915)
- Run id: `29585494915`
- Live bot: exit=`0`, duration=`231s`
- Options bot: exit=`0`, duration=`23s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T09:54:34.766295-04:00","date":"2026-07-17","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":22.2,"phases_s":{"reconcile":2.29,"cancel":0.06,"manage":1.58,"scan":17.92,"entries":0.08},"signals":199,"placed":0,"equity":120455.37,"open_positions":3,"pending_orders":0,"open_lots":11,"submitted_today":10,"filled_today":10,"unattributed_contracts":0,"top_signals":["S173:AKAM","S173:ALB","S173:AMZN","S173:AMP","S173:AME","S173:ADI","S173:APTV","S173:ARES"],"github_run":"4260","github_run_id":"29585494915","status":"ok"}
```

### Live bot full output

```text
13:50:45  INFO      Mode: morning_scan
13:50:45  INFO        [positions] 4/4 (4 valid)
13:50:45  INFO        Universe cache hit: 903 tickers (tickers_2026-07-17.json)
13:50:46  INFO        [universe] 40/899 (40 valid)
13:50:48  INFO        [universe] 80/899 (80 valid)
13:50:49  INFO        [universe] 120/899 (120 valid)
13:50:50  INFO        [universe] 160/899 (160 valid)
13:50:51  INFO        [universe] 200/899 (199 valid)
13:51:01  INFO        [universe] 240/899 (238 valid)
13:51:11  INFO        [universe] 280/899 (278 valid)
13:51:24  INFO        [universe] 320/899 (318 valid)
13:51:37  INFO        [universe] 360/899 (358 valid)
13:51:47  INFO        [universe] 400/899 (397 valid)
13:52:00  INFO        [universe] 440/899 (437 valid)
13:52:14  INFO        [universe] 480/899 (477 valid)
13:52:24  INFO        [universe] 520/899 (517 valid)
13:52:37  INFO        [universe] 560/899 (556 valid)
13:52:47  INFO        [universe] 600/899 (596 valid)
13:53:00  INFO        [universe] 640/899 (636 valid)
13:53:13  INFO        [universe] 680/899 (676 valid)
13:53:23  INFO        [universe] 720/899 (716 valid)
13:53:36  INFO        [universe] 760/899 (756 valid)
13:53:49  INFO        [universe] 800/899 (796 valid)
13:53:59  INFO        [universe] 840/899 (835 valid)
13:54:12  INFO        [universe] 880/899 (875 valid)
13:54:19  INFO        [universe] 899/899 (894 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_SCAN|
|  Time                                                         13:50 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $488.68|
+========================================================================+

+========================================================================+
|                   RUBBER BAND BOT v8  --  DAILY SCAN                   |
+========================================================================+
|  Mode                                                      *** LIVE ***|
|  Date                                                        2026-07-17|
|  Universe                                                          both|
|  Month                                        Jul: 52wkLow + Pullback50|
|  Regime                                                            BULL|
|  Exit                                      midline / stop-0.5% / 3d max|
+========================================================================+

+========================================================================+
|                                ACCOUNT                                 |
+========================================================================+
|  Equity                                                         $488.68|
|  Cash                                                           $123.33|
|  Reserve                                          $24.43  (always kept)|
|  Available                                     $98.90  (for new trades)|
|  Seasonal trade                   $97.74  (20% -- scheduled strategies)|
|  Off-sched trade                      $97.74  (20% -- other strategies)|
+========================================================================+

+========================================================================+
|                           HOLDINGS  (4 open)                           |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CARR     Pullback50      $87.72     $67.89   $69.23   +2.0%   $+1.70  |
|  CMS      Pullback50      $98.12     $74.35   $75.38   +1.4%   $+1.34  |
|  DOV      Pullback50      $82.27     $217.58  $218.61  +0.5%   $+0.39  |
|  DRI      Pullback50      $97.23     $201.51  $202.29  +0.4%   $+0.37  |
|                                                                        |
|  Total invested                                                 $365.35|
|  Total open P&L                                                  $+3.81|
|  Buys today: 0  |  entry cap: 1  |  max open: 5                        |
+========================================================================+

+========================================================================+
|                               PLAN CACHE                               |
+========================================================================+
|  Mode                                                           morning|
|  File                                      logs/plans/morning_plan.json|
|  Use cached plan                                  no (stale (11525.3m))|
+========================================================================+

+========================================================================+
|          EXIT EVALUATION  (EOD -- midline + stop + max-hold)           |
+========================================================================+
|  DRI  P&L +0.4%  $+0.37                                            HOLD|
|  DOV  P&L +0.5%  $+0.39                                            HOLD|
|  CMS  P&L +1.4%  $+1.34                                            HOLD|
|  CARR  P&L +2.0%  $+1.70                                           HOLD|
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
|  Primary: 52wkLow  |  Secondary: Pullback50                            |
|  Source                                                       live scan|
+========================================================================+

+========================================================================+
|                         SIGNALS FOUND  --  57                          |
+========================================================================+
|  TICKER   STRATEGY        TIER   PRICE    RSI    VOL_Z   TRIGGER       |
+------------------------------------------------------------------------+
|  BG       Pullback50      SEAS   $119.19  66.3   -2.13   50MA bounce (-|
|  CCL      GapDown         off    $26.46   28.1   -2.08   gap -3.2% reco|
|  CAT      GapDown         off    $859.87  29.3   -1.17   gap -4.0% reco|
|  CI       Pullback50      SEAS   $287.66  53.4   -1.44   50MA bounce (+|
|  COIN     GapDown         off    $157.09  56.3   -2.48   gap -4.4% reco|
|  FIX      GapDown         off    $1583.~  35.1   -1.50   gap -6.2% reco|
|  DELL     GapDown         off    $377.00  45.7   -2.13   gap -3.7% reco|
|  EMR      Pullback50      SEAS   $141.08  45.0   -2.05   50MA bounce (+|
|  FCX      GapDown         off    $57.26   37.4   -2.75   gap -3.2% reco|
|  GEV      GapDown         off    $1017.~  47.0   -2.57   gap -4.0% reco|
|  IBKR     Pullback50      SEAS   $89.69   49.8   -2.11   50MA bounce (+|
|  ISRG     GapDown         off    $365.97  37.7   -0.62   gap -9.3% reco|
|  JCI      Pullback50      SEAS   $140.80  54.5   -2.05   50MA bounce (-|
|  MAR      Pullback50      SEAS   $371.44  44.9   -2.55   50MA bounce (-|
|  MCHP     GapDown         off    $78.98   37.6   -1.84   gap -3.3% reco|
|  MU       GapDown         off    $827.20  23.1   -2.23   gap -3.6% reco|
|  MPWR     GapDown         off    $1253.~  45.7   -1.54   gap -4.6% reco|
|  NFLX     GapDown         off    $65.79   32.9   -0.89   gap -11.9% rec|
|  NI       Pullback50      SEAS   $46.86   36.3   -2.62   50MA bounce (-|
|  OXY      Pullback50      SEAS   $55.00   67.6   -2.17   50MA bounce (+|
|  ON       GapDown         off    $85.52   44.2   -1.42   gap -4.2% reco|
|  NXPI     GapDown         off    $263.14  41.9   -2.22   gap -3.9% reco|
|  ROK      Pullback50      SEAS   $462.47  44.1   -1.01   50MA bounce (+|
|  ROK      GapDown         off    $462.47  44.1   -1.01   gap -3.0% reco|
|  TJX      Pullback50      SEAS   $156.84  52.9   -1.91   50MA bounce (+|
|  TDY      Pullback50      SEAS   $629.67  52.5   -2.46   50MA bounce (+|13:54:20  INFO        BUY  BG  $97.74  [Pullback50]  id=308eb28e-96bf-4df5-bfae-d9ec82bd5381
13:54:33  INFO        place_all_stops: checking 5 positions...
13:54:33  INFO        STOP skipped BG: fractional (0.8240 shares) — software exit will handle it
13:54:33  INFO        STOP already live CARR @ $67.55
13:54:33  INFO        STOP already live CMS @ $73.98
13:54:33  INFO        STOP skipped DOV: fractional (0.3763 shares) — software exit will handle it
13:54:33  INFO        STOP skipped DRI: fractional (0.4807 shares) — software exit will handle it

|  TT       Pullback50      SEAS   $469.05  44.2   -1.86   50MA bounce (-|
|  VRSN     Pullback50      SEAS   $278.70  83.8   -1.91   50MA bounce (-|
|  WAB      Pullback50      SEAS   $263.97  38.1   -2.04   50MA bounce (-|
|  YUM      Pullback50      SEAS   $154.74  47.3   -2.05   50MA bounce (+|
|  ALGM     GapDown         off    $44.41   37.5   -1.50   gap -6.0% reco|
|  ALSN     Pullback50      SEAS   $115.67  41.8   -0.59   50MA bounce (-|
|  ALV      Pullback50      SEAS   $120.88  53.1   -1.48   50MA bounce (-|
|  ALV      GapDown         off    $120.88  53.1   -1.48   gap -4.5% reco|
|  AVAV     GapDown         off    $147.00  53.9   -1.24   gap -3.0% reco|
|  BDC      GapDown         off    $100.42  19.1   -1.84   gap -3.0% reco|
|  DOCN     GapDown         off    $113.90  35.6   -1.20   gap -4.1% reco|
|  DKS      Pullback50      SEAS   $221.83  37.2   -2.76   50MA bounce (-|
|  ENS      GapDown         off    $190.19  32.7   -1.13   gap -3.5% reco|
|  ENTG     GapDown         off    $131.82  34.8   -2.03   gap -5.1% reco|
|  FIVE     Pullback50      SEAS   $202.57  65.0   -3.11   50MA bounce (+|
|  FNB      GapDown         off    $19.12   48.2   -1.92   gap -3.5% reco|
|  FLR      Pullback50      SEAS   $48.92   35.4   -1.37   50MA bounce (-|
|  FOUR     GapDown         off    $51.12   61.7   -1.79   gap -3.3% reco|
|  HIMS     GapDown         off    $32.84   46.9   -1.90   gap -4.8% reco|
|  IDCC     GapDown         off    $261.00  35.1   -1.62   gap -3.4% reco|
|  ITT      Pullback50      SEAS   $194.00  51.1   -2.39   50MA bounce (-|
|  NVT      GapDown         off    $149.31  38.5   -2.20   gap -3.1% reco|
|  NOVT     GapDown         off    $148.33  41.1   -1.99   gap -3.3% reco|
|  MUR      Pullback50      SEAS   $36.72   59.3   -1.83   50MA bounce (+|
|  P        GapDown         off    $67.90   48.5   -1.76   gap -3.6% reco|
|  RRX      GapDown         off    $207.16  41.4   -1.92   gap -5.3% reco|
|  SLAB     Pullback50      SEAS   $218.02  45.9   -1.01   50MA bounce (-|
|  SYNA     GapDown         off    $112.89  43.6   -0.83   gap -4.5% reco|
|  VIAV     GapDown         off    $36.02   22.9   -0.66   gap -4.2% reco|
|  VICR     GapDown         off    $217.09  30.7   -0.93   gap -6.6% reco|
|  VNOM     Pullback50      SEAS   $44.52   60.6   -1.96   50MA bounce (-|
|                                                                        |
+========================================================================+

+========================================================================+
|                              ENTRY ORDERS                              |
+========================================================================+
|    ENTER [S] BG  Pullback50                                      $97.74|
|    BUY SUBMITTED [S~  fill pending — batched confirmation after entries|
|    SKIP [S] CI  Pullback50                                        cap 5|
|    SKIP [S] EMR  Pullback50                                       cap 5|
|    SKIP [S] IBKR  Pullback50                                      cap 5|
|    SKIP [S] JCI  Pullback50                                       cap 5|
|    SKIP [S] MAR  Pullback50                                       cap 5|
|    SKIP [S] NI  Pullback50                                        cap 5|
|    SKIP [S] OXY  Pullback50                                       cap 5|
|    SKIP [S] ROK  Pullback50                                       cap 5|
|    SKIP [S] TJX  Pullback50                                       cap 5|
|    SKIP [S] TDY  Pullback50                                       cap 5|
|    SKIP [S] TT  Pullback50                                        cap 5|
|    SKIP [S] VRSN  Pullback50                                      cap 5|
|    SKIP [S] WAB  Pullback50                                       cap 5|
|    SKIP [S] YUM  Pullback50                                       cap 5|
|    SKIP [S] ALSN  Pullback50                                      cap 5|
|    SKIP [S] ALV  Pullback50                                       cap 5|
|    SKIP [S] DKS  Pullback50                                       cap 5|
|    SKIP [S] FIVE  Pullback50                                      cap 5|
|    SKIP [S] FLR  Pullback50                                       cap 5|
|    SKIP [S] ITT  Pullback50                                       cap 5|
|    SKIP [S] MUR  Pullback50                                       cap 5|
|    SKIP [S] SLAB  Pullback50                                      cap 5|
|    SKIP [S] VNOM  Pullback50                                      cap 5|
|    SKIP [o] CCL  GapDown                                          cap 5|
|    SKIP [o] CAT  GapDown                                          cap 5|
|    SKIP [o] COIN  GapDown                                         cap 5|
|    SKIP [o] FIX  GapDown                                          cap 5|
|    SKIP [o] DELL  GapDown                                         cap 5|
|    SKIP [o] FCX  GapDown                                          cap 5|
|    SKIP [o] GEV  GapDown                                          cap 5|
|    SKIP [o] ISRG  GapDown                                         cap 5|
|    SKIP [o] MCHP  GapDown                                         cap 5|
|    SKIP [o] MU  GapDown                                           cap 5|
|    SKIP [o] MPWR  GapDown                                         cap 5|
|    SKIP [o] NFLX  GapDown                                         cap 5|
|    SKIP [o] ON  GapDown                                           cap 5|
|    SKIP [o] NXPI  GapDown                                         cap 5|
|    SKIP [o] ROK  GapDown                                          cap 5|
|    SKIP [o] ALGM  GapDown                                         cap 5|
|    SKIP [o] ALV  GapDown                                          cap 5|
|    SKIP [o] AVAV  GapDown                                         cap 5|
|    SKIP [o] BDC  GapDown                                          cap 5|
|    SKIP [o] DOCN  GapDown                                         cap 5|
|    SKIP [o] ENS  GapDown                                          cap 5|
|    SKIP [o] ENTG  GapDown                                         cap 5|
|    SKIP [o] FNB  GapDown                                          cap 5|
|    SKIP [o] FOUR  GapDown                                         cap 5|
|    SKIP [o] HIMS  GapDown                                         cap 5|
|    SKIP [o] IDCC  GapDown                                         cap 5|
|    SKIP [o] NVT  GapDown                                          cap 5|
|    SKIP [o] NOVT  GapDown                                         cap 5|
|    SKIP [o] P  GapDown                                            cap 5|
|    SKIP [o] RRX  GapDown                                          cap 5|
|    SKIP [o] SYNA  GapDown                                         cap 5|
|    SKIP [o] VIAV  GapDown                                         cap 5|
|    SKIP [o] VICR  GapDown                                         cap 5|

+========================================================================+
|                         BUY FILL CONFIRMATION                          |
+========================================================================+
|  Pending submits                                                      1|
+------------------------------------------------------------------------+
|  BG                                                   still unconfirmed|
+========================================================================+
+========================================================================+

+========================================================================+
|                           GTC STOP PLACEMENT                           |
+========================================================================+
|  Waiting 5s for 1 buy submit(s) to settle...                           |
+========================================================================+

+========================================================================+
|                            SESSION SUMMARY                             |
+========================================================================+13:54:33  INFO        Daily log -> logs/daily/2026-07-17.md
13:54:34  INFO        Dashboard written → logs/dashboard.md

|  Regime                                                            BULL|
|  Universe                                                          both|
|  Strategy                                          52wkLow + Pullback50|
|  Scanned                                                            894|
|  Signals                                                             57|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  1 unconfirmed|
|  Exits                                                                0|
|  Open pos                                                             5|
|  Equity                                                         $488.38|
|  Cash                                                            $25.60|
+========================================================================+
```

### Options bot full output

```text
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T09:54:34.766295-04:00 ===

[Run context]
Paper auth OK — equity $120455.37, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-17 09:54:38,497 INFO   EXIT [b40|c040_s173_w1_0928_1005_r3|S173] stop_loss (-98.5%) SELL 1 UAL260717C00122000 @<= 0.02
2026-07-17 09:54:38,855 INFO   EXIT [b0|c000_s173_w1_0928_1005_r1|S173] take_profit (+68.0%) SELL 1 AMZN260717C00250000 @<= 0.80

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 199 signal(s); top: ['S173:AKAM', 'S173:ALB', 'S173:AMZN', 'S173:AMP', 'S173:AME', 'S173:ADI', 'S173:APTV', 'S173:ARES']
Paper lab: $120569 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  All bucket slots blocked or closed for today's signals — skip entry loop.
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $120,455.37                             |
|  Signals this run              199                                     |
|  Orders submitted (session)    10                                      |
|  Orders filled today (ledger)  10                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             11                                      |
|  Broker option positions       3                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=330  buckets=46  win=36%                             |
|  Returns   avg=+10.1%  med=-23.0%  p10=-78.0%  p90=+90.9%              |
|  Realized  $+3,699.77                                                  |
|  Raw incl dropped  trades=437  real=$+2,469.58                         |
|  Today     trades=3  avg=-95.0%  med=-93.8%  real=$-175.00             |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b28  c028_s165_w1_0928_ 10  90% +68.7 +80.9 +102.0 $   +363           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b99  c099_s163_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b89  c089_s165_w2_1005_  4  75% +220.0 +69.9 +790.0 $   +127          |
|  ... 38 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 15   0% -63.6 -74.0 -98.5 $   -639       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b40  S173 UAL260717C00122000 x1 stop_loss (-98.5%)                    |
|  b0   S173 AMZN260717C00250000 x1 take_profit (+68.0%)                 |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (3)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  GOOGL260720C00360000          5    -40.0%   $   -110.00               |
|  AMZN260717C00250000           4    +53.8%   $   +106.40               |
|  UAL260717C00122000            1    -98.5%   $    -64.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=22.2s reconcile=2.29s cancel=0.06s manage=1.58s scan=17.92s entries=0.08s
STATUS: options_morning_bot run complete (PAPER) elapsed=22.2s. run=#4260 https://github.com/28twagg-ops/TradingBot/actions/runs/29585494915
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 3 buckets closed trades, $-175.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 5.0% (22/437)
```

---

## Run 20260717T135534Z

- UTC timestamp: `20260717T135534Z`
- GitHub run: [#4261](https://github.com/28twagg-ops/TradingBot/actions/runs/29585826733)
- Run id: `29585826733`
- Live bot: exit=`0`, duration=`246s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T09:59:40.695668-04:00","date":"2026-07-17","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":39.2,"phases_s":{"reconcile":2.86,"cancel":0.14,"manage":1.88,"scan":33.57,"entries":0.19},"signals":201,"placed":0,"equity":121324.33,"open_positions":2,"pending_orders":0,"open_lots":9,"submitted_today":10,"filled_today":10,"unattributed_contracts":0,"top_signals":["S173:AKAM","S173:ALB","S173:AMZN","S173:AMP","S173:AME","S173:ADI","S173:APTV","S173:ARES"],"github_run":"4261","github_run_id":"29585826733","status":"ok"}
```

### Live bot full output

```text
13:55:35  INFO      Mode: morning_scan
13:55:36  INFO        [positions] 5/5 (5 valid)
13:55:37  INFO        SELL LIMIT BG  qty=0.823974774  limit=$118.27  id=d3e2045f-9881-4595-ab5b-78184d558f0d
13:56:07  INFO        SELL LIMIT filled BG (confirmed by position check)
13:56:07  INFO        TX logged: SELL BG  P&L -0.09%
13:56:07  INFO        Universe cache hit: 903 tickers (tickers_2026-07-17.json)
13:56:09  INFO        [universe] 40/899 (40 valid)
13:56:10  INFO        [universe] 80/899 (80 valid)
13:56:11  INFO        [universe] 120/899 (120 valid)
13:56:12  INFO        [universe] 160/899 (160 valid)
13:56:14  INFO        [universe] 200/899 (199 valid)
13:56:21  INFO        [universe] 240/899 (238 valid)
13:56:33  INFO        [universe] 280/899 (278 valid)
13:56:46  INFO        [universe] 320/899 (318 valid)
13:56:56  INFO        [universe] 360/899 (358 valid)
13:57:10  INFO        [universe] 400/899 (397 valid)
13:57:20  INFO        [universe] 440/899 (437 valid)
13:57:33  INFO        [universe] 480/899 (477 valid)
13:57:44  INFO        [universe] 520/899 (517 valid)
13:57:57  INFO        [universe] 560/899 (556 valid)
13:58:11  INFO        [universe] 600/899 (596 valid)
13:58:21  INFO        [universe] 640/899 (636 valid)
13:58:35  INFO        [universe] 680/899 (676 valid)
13:58:45  INFO        [universe] 720/899 (716 valid)
13:58:56  INFO        [universe] 760/899 (756 valid)
13:59:09  INFO        [universe] 800/899 (796 valid)
13:59:23  INFO        [universe] 840/899 (835 valid)
13:59:34  INFO        [universe] 880/899 (875 valid)
13:59:37  INFO        [universe] 899/899 (894 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_SCAN|
|  Time                                                         13:55 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $488.50|
+========================================================================+

+========================================================================+
|                   RUBBER BAND BOT v8  --  DAILY SCAN                   |
+========================================================================+
|  Mode                                                      *** LIVE ***|
|  Date                                                        2026-07-17|
|  Universe                                                          both|
|  Month                                        Jul: 52wkLow + Pullback50|
|  Regime                                                            BULL|
|  Exit                                      midline / stop-0.5% / 3d max|
+========================================================================+

+========================================================================+
|                                ACCOUNT                                 |
+========================================================================+
|  Equity                                                         $488.50|
|  Cash                                                            $25.60|
|  Reserve                                          $24.43  (always kept)|
|  Available                                      $1.18  (for new trades)|
|  Seasonal trade                   $97.70  (20% -- scheduled strategies)|
|  Off-sched trade                      $97.70  (20% -- other strategies)|
+========================================================================+

+========================================================================+
|                           HOLDINGS  (5 open)                           |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  BG       Pullback50      $97.65     $118.61  $118.50  -0.1%   $-0.08  |
|  CARR     Pullback50      $87.66     $67.89   $69.19   +1.9%   $+1.64  |
|  CMS      Pullback50      $98.10     $74.35   $75.36   +1.4%   $+1.32  |
|  DOV      Pullback50      $82.25     $217.58  $218.56  +0.5%   $+0.37  |
|  DRI      Pullback50      $97.24     $201.51  $202.30  +0.4%   $+0.38  |
|                                                                        |
|  Total invested                                                 $462.90|
|  Total open P&L                                                  $+3.63|
|  Buys today: 0  |  entry cap: 0  |  max open: 5                        |
+========================================================================+

+========================================================================+
|                               PLAN CACHE                               |
+========================================================================+
|  Mode                                                           morning|
|  File                                      logs/plans/morning_plan.json|
|  Use cached plan                                  no (stale (11530.1m))|
+========================================================================+

+========================================================================+
|          EXIT EVALUATION  (EOD -- midline + stop + max-hold)           |
+========================================================================+
|  BG  P&L -0.1%  $-0.08                            EXIT: midline (-0.1%)|
|  DRI  P&L +0.4%  $+0.38                                            HOLD|
|  DOV  P&L +0.5%  $+0.37                                            HOLD|
|  CMS  P&L +1.4%  $+1.32                                            HOLD|
|  CARR  P&L +1.9%  $+1.64                                           HOLD|
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
|  Primary: 52wkLow  |  Secondary: Pullback50                            |
|  Source                                                       live scan|
+========================================================================+

+========================================================================+
|                         SIGNALS FOUND  --  66                          |
+========================================================================+
|  TICKER   STRATEGY        TIER   PRICE    RSI    VOL_Z   TRIGGER       |
+------------------------------------------------------------------------+
|  BG       Pullback50      SEAS   $118.64  65.6   -2.12   50MA bounce (-|
|  CCL      GapDown         off    $26.39   27.7   -2.05   gap -3.2% reco|
|  CAT      GapDown         off    $859.25  29.3   -1.15   gap -4.0% reco|
|  CIEN     GapDown         off    $372.49  28.0   -0.94   gap -4.6% reco|
|  COHR     GapDown         off    $266.14  18.2   -2.07   gap -4.4% reco|
|  COIN     GapDown         off    $157.07  56.3   -2.43   gap -4.4% reco|
|  FIX      GapDown         off    $1588.~  35.3   -1.46   gap -6.2% reco|
|  DELL     GapDown         off    $382.16  46.6   -2.09   gap -3.7% reco|
|  EMR      Pullback50      SEAS   $141.09  45.1   -1.99   50MA bounce (+|
|  FCX      GapDown         off    $57.50   37.9   -2.69   gap -3.2% reco|
|  GEV      GapDown         off    $1021.~  47.4   -2.52   gap -4.0% reco|
|  INTC     GapDown         off    $92.20   26.3   -2.24   gap -5.0% reco|
|  KLAC     GapDown         off    $209.40  39.8   -2.06   gap -5.0% reco|
|  LRCX     GapDown         off    $306.34  36.4   -2.29   gap -5.3% reco|
|  LITE     GapDown         off    $683.06  37.2   -2.10   gap -3.9% reco|
|  MRVL     GapDown         off    $182.77  27.8   -0.71   gap -3.2% reco|
|  MCHP     GapDown         off    $79.11   37.7   -1.82   gap -3.3% reco|
|  MU       GapDown         off    $837.32  23.5   -2.18   gap -3.6% reco|
|  MPWR     GapDown         off    $1272.~  47.0   -1.50   gap -4.6% reco|
|  NFLX     GapDown         off    $66.36   33.7   -0.71   gap -11.9% rec|
|  NI       Pullback50      SEAS   $46.97   37.1   -2.60   50MA bounce (-|
|  ON       GapDown         off    $85.37   44.1   -1.39   gap -4.2% reco|
|  NXPI     GapDown         off    $263.80  42.2   -2.21   gap -3.9% reco|
|  OXY      Pullback50      SEAS   $54.69   66.9   -2.15   50MA bounce (-|13:59:39  INFO        place_all_stops: checking 4 positions...
13:59:39  INFO        STOP already live CARR @ $67.55
13:59:39  INFO        STOP already live CMS @ $73.98
13:59:39  INFO        STOP skipped DOV: fractional (0.3763 shares) — software exit will handle it
13:59:39  INFO        STOP skipped DRI: fractional (0.4807 shares) — software exit will handle it
13:59:39  INFO        Daily log -> logs/daily/2026-07-17.md
13:59:39  INFO        Dashboard written → logs/dashboard.md

|  ROK      Pullback50      SEAS   $460.55  43.5   -1.01   50MA bounce (+|
|  ROK      GapDown         off    $460.55  43.5   -1.01   gap -3.0% reco|
|  SNDK     GapDown         off    $1378.~  31.5   -2.35   gap -3.3% reco|
|  STX      GapDown         off    $725.51  35.7   -2.20   gap -3.3% reco|
|  TDY      Pullback50      SEAS   $629.13  52.2   -2.45   50MA bounce (+|
|  TER      GapDown         off    $307.15  28.9   -1.22   gap -5.1% reco|
|  TJX      Pullback50      SEAS   $156.12  51.5   -1.90   50MA bounce (-|
|  TT       Pullback50      SEAS   $467.96  43.6   -1.84   50MA bounce (-|
|  VRSN     Pullback50      SEAS   $277.35  83.2   -1.90   50MA bounce (-|
|  VRT      GapDown         off    $279.33  42.3   -1.18   gap -5.1% reco|
|  WAB      Pullback50      SEAS   $263.44  37.2   -2.03   50MA bounce (-|
|  YUM      Pullback50      SEAS   $154.90  47.6   -2.03   50MA bounce (+|
|  AEIS     GapDown         off    $272.82  29.2   -0.75   gap -4.8% reco|
|  ALGM     GapDown         off    $44.85   37.8   -1.49   gap -6.0% reco|
|  ALV      Pullback50      SEAS   $120.86  53.1   -1.37   50MA bounce (-|
|  ALV      GapDown         off    $120.86  53.1   -1.37   gap -4.5% reco|
|  AVAV     GapDown         off    $146.96  53.9   -1.24   gap -3.0% reco|
|  BDC      GapDown         off    $99.95   18.8   -1.84   gap -3.0% reco|
|  DKS      Pullback50      SEAS   $221.57  36.9   -2.74   50MA bounce (-|
|  DOCN     GapDown         off    $114.79  36.0   -1.19   gap -4.1% reco|
|  ENS      GapDown         off    $190.73  32.9   -1.12   gap -3.5% reco|
|  ENTG     GapDown         off    $132.47  35.0   -2.01   gap -5.1% reco|
|  FLR      Pullback50      SEAS   $48.85   35.3   -1.36   50MA bounce (-|
|  FOUR     GapDown         off    $50.77   60.3   -1.78   gap -3.3% reco|
|  FNB      GapDown         off    $18.99   46.3   -1.87   gap -3.5% reco|
|  HIMS     GapDown         off    $33.19   47.9   -1.88   gap -4.8% reco|
|  ITT      Pullback50      SEAS   $193.78  50.8   -2.38   50MA bounce (-|
|  IDCC     GapDown         off    $259.56  34.1   -1.61   gap -3.4% reco|
|  JEF      Pullback50      SEAS   $54.98   65.4   -1.38   50MA bounce (+|
|  MUR      Pullback50      SEAS   $36.85   59.8   -1.82   50MA bounce (+|
|  NVT      GapDown         off    $150.28  39.1   -2.16   gap -3.1% reco|
|  NOVT     GapDown         off    $147.99  40.8   -1.99   gap -3.3% reco|
|  P        GapDown         off    $68.34   49.0   -1.73   gap -3.6% reco|
|  RMBS     GapDown         off    $95.95   37.7   -0.93   gap -6.0% reco|
|  RRX      GapDown         off    $206.67  41.1   -1.88   gap -5.3% reco|
|  SLAB     Pullback50      SEAS   $217.95  45.2   -1.00   50MA bounce (-|
|  SITM     GapDown         off    $541.75  35.8   -0.69   gap -4.3% reco|
|  SMTC     GapDown         off    $119.68  35.3   -0.80   gap -7.1% reco|
|  SYNA     GapDown         off    $113.31  43.9   -0.78   gap -4.5% reco|
|  VNOM     Pullback50      SEAS   $44.56   60.8   -1.95   50MA bounce (-|
|  VICR     GapDown         off    $222.01  31.3   -0.91   gap -6.6% reco|
|  VIAV     GapDown         off    $36.52   23.4   -0.65   gap -4.2% reco|
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
|  Strategy                                          52wkLow + Pullback50|
|  Scanned                                                            894|
|  Signals                                                             66|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  0 unconfirmed|
|  Exits                                                                1|
|  Open pos                                                             4|
|  Equity                                                         $487.35|
|  Cash                                                           $123.27|
+========================================================================+
```

### Options bot full output

```text
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T09:59:40.695668-04:00 ===

[Run context]
Paper auth OK — equity $121324.33, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 201 signal(s); top: ['S173:AKAM', 'S173:ALB', 'S173:AMZN', 'S173:AMP', 'S173:AME', 'S173:ADI', 'S173:APTV', 'S173:ARES']
Paper lab: $121559 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  All bucket slots blocked or closed for today's signals — skip entry loop.
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $121,324.33                             |
|  Signals this run              201                                     |
|  Orders submitted (session)    10                                      |
|  Orders filled today (ledger)  10                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             9                                       |
|  Broker option positions       2                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=332  buckets=46  win=36%                             |
|  Returns   avg=+10.0%  med=-23.0%  p10=-78.4%  p90=+90.6%              |
|  Realized  $+3,675.77                                                  |
|  Raw incl dropped  trades=440  real=$+2,391.58                         |
|  Today     trades=5  avg=-59.6%  med=-93.6%  real=$-199.00             |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b28  c028_s165_w1_0928_ 10  90% +68.7 +80.9 +102.0 $   +363           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b99  c099_s163_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b89  c089_s165_w2_1005_  4  75% +220.0 +69.9 +790.0 $   +127          |
|  ... 38 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 15   0% -63.6 -74.0 -98.5 $   -639       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (2)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260717C00250000           4    +64.0%   $   +126.40               |
|  GOOGL260720C00360000          5    -18.2%   $    -50.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=39.2s reconcile=2.86s cancel=0.14s manage=1.88s scan=33.57s entries=0.19s
STATUS: options_morning_bot run complete (PAPER) elapsed=39.2s. run=#4261 https://github.com/28twagg-ops/TradingBot/actions/runs/29585826733
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 3 buckets closed trades, $-199.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 5.0% (22/440)
```

---
