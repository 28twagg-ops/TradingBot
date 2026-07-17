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
