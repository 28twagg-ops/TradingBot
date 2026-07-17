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
