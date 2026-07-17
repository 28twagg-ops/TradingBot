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

## Run 20260717T140102Z

- UTC timestamp: `20260717T140102Z`
- GitHub run: [#4262](https://github.com/28twagg-ops/TradingBot/actions/runs/29586166991)
- Run id: `29586166991`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`58s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T10:01:05.316773-04:00","date":"2026-07-17","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":56.5,"phases_s":{"reconcile":2.16,"cancel":0.03,"manage":3.51,"scan":50.5,"entries":0.07},"signals":205,"placed":0,"equity":122094.25,"open_positions":2,"pending_orders":0,"open_lots":9,"submitted_today":10,"filled_today":10,"unattributed_contracts":0,"top_signals":["S173:AMD","S173:AKAM","S173:ALB","S173:GOOGL","S173:GOOG","S173:AMZN","S173:AMP","S173:AME"],"github_run":"4262","github_run_id":"29586166991","status":"ok"}
```

### Live bot full output

```text
14:01:03  INFO      Mode: exits
14:01:03  INFO        Daily log -> logs/daily/2026-07-17.md
14:01:03  INFO        Daily log reconciled -> logs/daily/2026-07-17.md (1 ledger rows)
14:01:03  INFO        place_all_stops: checking 4 positions...
14:01:03  INFO        STOP already live CARR @ $67.55
14:01:03  INFO        STOP already live CMS @ $73.98
14:01:03  INFO        STOP skipped DOV: fractional (0.3763 shares) — software exit will handle it
14:01:03  INFO        STOP skipped DRI: fractional (0.4807 shares) — software exit will handle it
14:01:04  INFO        [positions] 4/4 (4 valid)
14:01:04  INFO        Daily log -> logs/daily/2026-07-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $487.46|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  DRI  P&L -0.1%  $-0.11                                            HOLD|
|  DOV  P&L +0.1%  $+0.12                                            HOLD|
|  CMS  P&L +1.1%  $+1.11                                            HOLD|
|  CARR  P&L +1.8%  $+1.54                                           HOLD|
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
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T10:01:05.316773-04:00 ===

[Run context]
Paper auth OK — equity $122094.25, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-17 10:01:11,106 INFO   EXIT [b20|c020_s173_w1_0928_1005_r2|S173] take_profit (+64.0%) SELL 1 AMZN260717C00250000 @<= 0.77

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 205 signal(s); top: ['S173:AMD', 'S173:AKAM', 'S173:ALB', 'S173:GOOGL', 'S173:GOOG', 'S173:AMZN', 'S173:AMP', 'S173:AME']
Paper lab: $122113 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  All bucket slots blocked or closed for today's signals — skip entry loop.
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $122,094.25                             |
|  Signals this run              205                                     |
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
|  Today     trades=5  avg=-59.9%  med=-93.8%  real=$-199.00             |
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
|  b20  S173 AMZN260717C00250000 x1 take_profit (+64.0%)                 |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (2)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260717C00250000           3    +72.1%   $   +106.80               |
|  GOOGL260720C00360000          5    -21.8%   $    -60.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=56.5s reconcile=2.16s cancel=0.03s manage=3.51s scan=50.5s entries=0.07s
STATUS: options_morning_bot run complete (PAPER) elapsed=56.5s. run=#4262 https://github.com/28twagg-ops/TradingBot/actions/runs/29586166991
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 3 buckets closed trades, $-199.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 5.0% (22/440)
```

---

## Run 20260717T140540Z

- UTC timestamp: `20260717T140540Z`
- GitHub run: [#4263](https://github.com/28twagg-ops/TradingBot/actions/runs/29586513937)
- Run id: `29586513937`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`65s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T10:05:43.695398-04:00","date":"2026-07-17","mode":"entry+manage","header":"entry+manage (10 new)","elapsed_s":64.0,"phases_s":{"reconcile":6.68,"cancel":0.08,"manage":1.73,"scan":45.18,"entries":4.72,"reconcile2":4.91},"signals":203,"placed":10,"equity":122926.31,"open_positions":2,"pending_orders":10,"open_lots":7,"submitted_today":20,"filled_today":10,"unattributed_contracts":0,"top_signals":["S173:AMD","S173:AKAM","S173:ALB","S173:GOOGL","S173:GOOG","S173:AMZN","S173:AMP","S173:AME"],"github_run":"4263","github_run_id":"29586513937","status":"ok"}
```

### Live bot full output

```text
14:05:41  INFO      Mode: exits
14:05:42  INFO        Daily log -> logs/daily/2026-07-17.md
14:05:42  INFO        Daily log reconciled -> logs/daily/2026-07-17.md (2 ledger rows)
14:05:42  INFO        place_all_stops: checking 4 positions...
14:05:42  INFO        STOP already live CARR @ $67.55
14:05:42  INFO        STOP already live CMS @ $73.98
14:05:42  INFO        STOP skipped DOV: fractional (0.3763 shares) — software exit will handle it
14:05:42  INFO        STOP skipped DRI: fractional (0.4807 shares) — software exit will handle it
14:05:42  INFO        [positions] 4/4 (4 valid)
14:05:42  INFO        Daily log -> logs/daily/2026-07-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:05 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $487.51|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  DRI  P&L -0.4%  $-0.37                                            HOLD|
|  DOV  P&L +0.3%  $+0.27                                            HOLD|
|  CMS  P&L +1.1%  $+1.11                                            HOLD|
|  CARR  P&L +2.0%  $+1.70                                           HOLD|
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
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T10:05:43.695398-04:00 ===

[Run context]
Paper auth OK — equity $122926.31, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-17 10:05:51,799 INFO   EXIT [b0|c000_s173_w1_0928_1005_r1|S173] take_profit (+88.3%) SELL 1 AMZN260717C00250000 @<= 0.94

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 203 signal(s); top: ['S173:AMD', 'S173:AKAM', 'S173:ALB', 'S173:GOOGL', 'S173:GOOG', 'S173:AMZN', 'S173:AMP', 'S173:AME']
Paper lab: $123268 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 30 no tradeable call, 378 already attempted today, 975 pending order
Placed 10 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $122,926.31                             |
|  Signals this run              203                                     |
|  Orders submitted (session)    20                                      |
|  Orders filled today (ledger)  10                                      |
|  Entries placed this run       10                                      |
|  Open virtual lots             7                                       |
|  Broker option positions       2                                       |
|  Pending orders                10                                      |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=334  buckets=46  win=36%                             |
|  Returns   avg=+10.4%  med=-22.9%  p10=-78.3%  p90=+90.9%              |
|  Realized  $+3,751.77                                                  |
|  Raw incl dropped  trades=442  real=$+2,467.58                         |
|  Today     trades=7  avg=-20.4%  med=-93.2%  real=$-123.00             |
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
|  PENDING ORDERS (10)                                                   |
+------------------------------------------------------------------------+
|  Top groups                    S173:AMD(5), S165:META(5)               |
+------------------------------------------------------------------------+
|  b1   S173 AMD      limit=0.68                                         |
|  b21  S173 AMD      limit=0.68                                         |
|  b41  S173 AMD      limit=0.68                                         |
|  b61  S173 AMD      limit=0.68                                         |
|  b81  S173 AMD      limit=0.68                                         |
|  ... 5 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (2)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260717C00250000           2    +74.1%   $    +73.20               |
|  GOOGL260720C00360000          5    -21.8%   $    -60.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=64.0s reconcile=6.68s cancel=0.08s manage=1.73s scan=45.18s entries=4.72s
STATUS: options_morning_bot run complete (PAPER) elapsed=64.0s. run=#4263 https://github.com/28twagg-ops/TradingBot/actions/runs/29586513937
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 4 buckets closed trades, $-123.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 5.0% (22/442)
```

---

## Run 20260717T141035Z

- UTC timestamp: `20260717T141035Z`
- GitHub run: [#4264](https://github.com/28twagg-ops/TradingBot/actions/runs/29586856458)
- Run id: `29586856458`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`51s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T10:10:37.657472-04:00","date":"2026-07-17","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":49.0,"phases_s":{"reconcile":2.18,"cancel":0.05,"manage":4.32,"scan":42.0,"entries":0.1},"signals":205,"placed":0,"equity":124189.09,"open_positions":4,"pending_orders":0,"open_lots":17,"submitted_today":20,"filled_today":20,"unattributed_contracts":0,"top_signals":["S173:AMD","S173:AKAM","S173:ALB","S173:GOOGL","S173:GOOG","S173:AMZN","S173:AMP","S173:AME"],"github_run":"4264","github_run_id":"29586856458","status":"ok"}
```

### Live bot full output

```text
14:10:36  INFO      Mode: exits
14:10:36  INFO        Daily log -> logs/daily/2026-07-17.md
14:10:36  INFO        Daily log reconciled -> logs/daily/2026-07-17.md (2 ledger rows)
14:10:36  INFO        place_all_stops: checking 4 positions...
14:10:36  INFO        STOP already live CARR @ $67.55
14:10:36  INFO        STOP already live CMS @ $73.98
14:10:36  INFO        STOP skipped DOV: fractional (0.3763 shares) — software exit will handle it
14:10:36  INFO        STOP skipped DRI: fractional (0.4807 shares) — software exit will handle it
14:10:36  INFO        [positions] 4/4 (4 valid)
14:10:36  INFO        Daily log -> logs/daily/2026-07-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $487.55|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  DRI  P&L -0.4%  $-0.41                                            HOLD|
|  DOV  P&L +0.3%  $+0.25                                            HOLD|
|  CMS  P&L +1.1%  $+1.11                                            HOLD|
|  CARR  P&L +2.1%  $+1.80                                           HOLD|
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
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T10:10:37.657472-04:00 ===

[Run context]
Paper auth OK — equity $124189.09, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-17 10:10:43,194 INFO   EXIT [b81|c081_s173_w2_1005_1045_r5|S173] take_profit (+56.1%) SELL 1 AMD260717C00512500 @<= 1.01

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 205 signal(s); top: ['S173:AMD', 'S173:AKAM', 'S173:ALB', 'S173:GOOGL', 'S173:GOOG', 'S173:AMZN', 'S173:AMP', 'S173:AME']
Paper lab: $124512 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  All bucket slots blocked or closed for today's signals — skip entry loop.
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $124,189.09                             |
|  Signals this run              205                                     |
|  Orders submitted (session)    20                                      |
|  Orders filled today (ledger)  20                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             17                                      |
|  Broker option positions       4                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=335  buckets=46  win=36%                             |
|  Returns   avg=+10.2%  med=-22.9%  p10=-78.3%  p90=+90.9%              |
|  Realized  $+3,706.77                                                  |
|  Raw incl dropped  trades=443  real=$+2,422.58                         |
|  Today     trades=7  avg=-20.4%  med=-93.2%  real=$-123.00             |
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
|  b81  S173 AMD260717C00512500 x1 take_profit (+56.1%)                  |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (4)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMD260717C00512500            4    +60.6%   $   +160.00               |
|  GOOGL260720C00360000          5    -34.5%   $    -95.00               |
|  META260720C00675000           5    -26.5%   $    -90.00               |
|  AMZN260717C00250000           2     -0.8%   $     -0.80               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=49.0s reconcile=2.18s cancel=0.05s manage=4.32s scan=42.0s entries=0.1s
STATUS: options_morning_bot run complete (PAPER) elapsed=49.0s. run=#4264 https://github.com/28twagg-ops/TradingBot/actions/runs/29586856458
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 4 buckets closed trades, $-123.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 5.0% (22/443)
```

---

## Run 20260717T141535Z

- UTC timestamp: `20260717T141535Z`
- GitHub run: [#4265](https://github.com/28twagg-ops/TradingBot/actions/runs/29587204470)
- Run id: `29587204470`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`61s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T10:15:38.926238-04:00","date":"2026-07-17","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":59.7,"phases_s":{"reconcile":2.33,"cancel":0.13,"manage":10.59,"scan":45.97,"entries":0.17},"signals":206,"placed":0,"equity":123966.07,"open_positions":4,"pending_orders":0,"open_lots":16,"submitted_today":20,"filled_today":20,"unattributed_contracts":0,"top_signals":["S173:AMD","S173:AKAM","S173:ALB","S173:GOOGL","S173:GOOG","S173:AMZN","S173:AMP","S173:AME"],"github_run":"4265","github_run_id":"29587204470","status":"ok"}
```

### Live bot full output

```text
14:15:36  INFO      Mode: exits
14:15:36  INFO        Daily log -> logs/daily/2026-07-17.md
14:15:36  INFO        Daily log reconciled -> logs/daily/2026-07-17.md (2 ledger rows)
14:15:37  INFO        place_all_stops: checking 4 positions...
14:15:37  INFO        STOP already live CARR @ $67.55
14:15:37  INFO        STOP already live CMS @ $73.98
14:15:37  INFO        STOP skipped DOV: fractional (0.3763 shares) — software exit will handle it
14:15:37  INFO        STOP skipped DRI: fractional (0.4807 shares) — software exit will handle it
14:15:37  INFO        [positions] 4/4 (4 valid)
14:15:37  INFO        Daily log -> logs/daily/2026-07-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:15 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $486.96|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  DRI  P&L -0.3%  $-0.31                                            HOLD|
|  DOV  P&L +0.2%  $+0.13                                            HOLD|
|  CMS  P&L +1.0%  $+1.01                                            HOLD|
|  CARR  P&L +1.5%  $+1.32                                           HOLD|
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
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T10:15:38.926238-04:00 ===

[Run context]
Paper auth OK — equity $123966.07, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-17 10:15:47,055 INFO   EXIT [b0|c000_s173_w1_0928_1005_r1|S173] take_profit (+64.0%) SELL 1 AMZN260717C00250000 @<= 0.75

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 206 signal(s); top: ['S173:AMD', 'S173:AKAM', 'S173:ALB', 'S173:GOOGL', 'S173:GOOG', 'S173:AMZN', 'S173:AMP', 'S173:AME']
Paper lab: $124139 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  All bucket slots blocked or closed for today's signals — skip entry loop.
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $123,966.07                             |
|  Signals this run              206                                     |
|  Orders submitted (session)    20                                      |
|  Orders filled today (ledger)  20                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             16                                      |
|  Broker option positions       4                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=336  buckets=46  win=36%                             |
|  Returns   avg=+10.4%  med=-22.9%  p10=-78.2%  p90=+90.9%              |
|  Realized  $+3,748.77                                                  |
|  Raw incl dropped  trades=444  real=$+2,464.58                         |
|  Today     trades=8  avg=-9.9%  med=-18.1%  real=$-81.00               |
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
|  b0   S173 AMZN260717C00250000 x1 take_profit (+64.0%)                 |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (4)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  GOOGL260720C00360000          5    -41.8%   $   -115.00               |
|  META260720C00675000           5    -32.4%   $   -110.00               |
|  AMD260717C00512500            4    +10.6%   $    +28.00               |
|  AMZN260717C00250000           1    +19.4%   $     +9.60               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=59.7s reconcile=2.33s cancel=0.13s manage=10.59s scan=45.97s entries=0.17s
STATUS: options_morning_bot run complete (PAPER) elapsed=59.7s. run=#4265 https://github.com/28twagg-ops/TradingBot/actions/runs/29587204470
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 5 buckets closed trades, $-81.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 5.0% (22/444)
```

---

## Run 20260717T142039Z

- UTC timestamp: `20260717T142039Z`
- GitHub run: [#4266](https://github.com/28twagg-ops/TradingBot/actions/runs/29587552207)
- Run id: `29587552207`
- Live bot: exit=`0`, duration=`5s`
- Options bot: exit=`0`, duration=`47s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T10:20:45.019585-04:00","date":"2026-07-17","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":45.6,"phases_s":{"reconcile":2.18,"cancel":0.06,"manage":6.06,"scan":36.86,"entries":0.09},"signals":207,"placed":0,"equity":124031.05,"open_positions":4,"pending_orders":0,"open_lots":15,"submitted_today":20,"filled_today":20,"unattributed_contracts":0,"top_signals":["S173:AMD","S173:AKAM","S173:ALB","S173:AMZN","S173:AMP","S173:AME","S173:APH","S173:ADI"],"github_run":"4266","github_run_id":"29587552207","status":"ok"}
```

### Live bot full output

```text
14:20:40  INFO      Mode: exits
14:20:41  INFO        Daily log -> logs/daily/2026-07-17.md
14:20:41  INFO        Daily log reconciled -> logs/daily/2026-07-17.md (2 ledger rows)
14:20:41  INFO        place_all_stops: checking 4 positions...
14:20:41  INFO        STOP already live CARR @ $67.55
14:20:41  INFO        STOP already live CMS @ $73.98
14:20:41  INFO        STOP skipped DOV: fractional (0.3763 shares) — software exit will handle it
14:20:41  INFO        STOP skipped DRI: fractional (0.4807 shares) — software exit will handle it
14:20:41  INFO        [positions] 4/4 (4 valid)
14:20:41  INFO        SELL MARKET [urgent] DRI closed
14:20:44  INFO        TX logged: SELL DRI  P&L -0.92%
14:20:44  INFO        Daily log -> logs/daily/2026-07-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $486.10|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  DRI  P&L -0.9%  $-0.89                         EXIT: stop_loss (-0.9%)|
|  DOV  P&L +0.2%  $+0.13                                            HOLD|
|  CMS  P&L +0.6%  $+0.61                                            HOLD|
|  CARR  P&L +1.7%  $+1.44                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           4|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  1 attempted  |  1 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
|  Logged exits                                                         1|
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  DRI                                         -0.92%  (threshold -0.50%)|
|  Count                                                                1|
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Options bot full output

```text
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T10:20:45.019585-04:00 ===

[Run context]
Paper auth OK — equity $124031.05, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 207 signal(s); top: ['S173:AMD', 'S173:AKAM', 'S173:ALB', 'S173:AMZN', 'S173:AMP', 'S173:AME', 'S173:APH', 'S173:ADI']
Paper lab: $123797 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  All bucket slots blocked or closed for today's signals — skip entry loop.
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $124,031.05                             |
|  Signals this run              207                                     |
|  Orders submitted (session)    20                                      |
|  Orders filled today (ledger)  20                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             15                                      |
|  Broker option positions       4                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=349  buckets=46  win=36%                             |
|  Returns   avg=+9.2%  med=-24.1%  p10=-77.2%  p90=+90.9%               |
|  Realized  $+3,527.77                                                  |
|  Raw incl dropped  trades=458  real=$+2,190.58                         |
|  Today     trades=9  avg=-1.2%  med=+56.9%  real=$-49.00               |
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
|  b80  c080_s173_w1_0928_ 35  74% +58.0 +62.9 +177.3 $   +403           |
|  ... 38 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 16   0% -63.1 -73.0 -98.5 $   -675       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (4)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  GOOGL260720C00360000          5    -49.1%   $   -135.00               |
|  META260720C00675000           5    -32.4%   $   -110.00               |
|  AMD260717C00512500            4     -9.1%   $    -24.00               |
|  AMZN260717C00250000           1    +41.7%   $    +20.60               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=45.6s reconcile=2.18s cancel=0.06s manage=6.06s scan=36.86s entries=0.09s
STATUS: options_morning_bot run complete (PAPER) elapsed=45.6s. run=#4266 https://github.com/28twagg-ops/TradingBot/actions/runs/29587552207
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 5 buckets closed trades, $-49.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 4.8% (22/458)
```

---

## Run 20260717T142533Z

- UTC timestamp: `20260717T142533Z`
- GitHub run: [#4267](https://github.com/28twagg-ops/TradingBot/actions/runs/29587896801)
- Run id: `29587896801`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`37s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T10:25:36.156708-04:00","date":"2026-07-17","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":35.8,"phases_s":{"reconcile":2.0,"cancel":0.03,"manage":2.97,"scan":30.05,"entries":0.06},"signals":206,"placed":0,"equity":123645.05,"open_positions":3,"pending_orders":0,"open_lots":15,"submitted_today":20,"filled_today":20,"unattributed_contracts":0,"top_signals":["S173:AMD","S173:AKAM","S173:ALB","S173:GOOGL","S173:GOOG","S173:AMZN","S173:AMP","S173:AME"],"github_run":"4267","github_run_id":"29587896801","status":"ok"}
```

### Live bot full output

```text
14:25:34  INFO      Mode: exits
14:25:35  INFO        Daily log -> logs/daily/2026-07-17.md
14:25:35  INFO        Daily log reconciled -> logs/daily/2026-07-17.md (3 ledger rows)
14:25:35  INFO        place_all_stops: checking 3 positions...
14:25:35  INFO        STOP already live CARR @ $67.55
14:25:35  INFO        STOP already live CMS @ $73.98
14:25:35  INFO        STOP skipped DOV: fractional (0.3763 shares) — software exit will handle it
14:25:35  INFO        [positions] 3/3 (3 valid)
14:25:35  INFO        Daily log -> logs/daily/2026-07-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:25 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $486.53|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  DOV  P&L +0.2%  $+0.16                                            HOLD|
|  CMS  P&L +0.7%  $+0.67                                            HOLD|
|  CARR  P&L +2.0%  $+1.76                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T10:25:36.156708-04:00 ===

[Run context]
Paper auth OK — equity $123645.05, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-17 10:25:41,694 INFO   EXIT [b20|c020_s173_w1_0928_1005_r2|S173] take_profit (+61.9%) SELL 1 AMZN260717C00250000 @<= 0.81

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 206 signal(s); top: ['S173:AMD', 'S173:AKAM', 'S173:ALB', 'S173:GOOGL', 'S173:GOOG', 'S173:AMZN', 'S173:AMP', 'S173:AME']
Paper lab: $123526 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  All bucket slots blocked or closed for today's signals — skip entry loop.
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $123,645.05                             |
|  Signals this run              206                                     |
|  Orders submitted (session)    20                                      |
|  Orders filled today (ledger)  20                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             15                                      |
|  Broker option positions       3                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=352  buckets=46  win=36%                             |
|  Returns   avg=+8.6%  med=-25.2%  p10=-77.0%  p90=+90.6%               |
|  Realized  $+3,417.77                                                  |
|  Raw incl dropped  trades=461  real=$+2,080.58                         |
|  Today     trades=9  avg=-1.2%  med=+56.9%  real=$-49.00               |
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
|  b80  c080_s173_w1_0928_ 35  74% +58.0 +62.9 +177.3 $   +403           |
|  ... 38 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 17   0% -62.7 -72.1 -98.5 $   -712       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b20  S173 AMZN260717C00250000 x1 take_profit (+61.9%)                 |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (3)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  GOOGL260720C00360000          5    -38.2%   $   -105.00               |
|  META260720C00675000           5    -23.5%   $    -80.00               |
|  AMD260717C00512500            4    -16.7%   $    -44.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=35.8s reconcile=2.0s cancel=0.03s manage=2.97s scan=30.05s entries=0.06s
STATUS: options_morning_bot run complete (PAPER) elapsed=35.8s. run=#4267 https://github.com/28twagg-ops/TradingBot/actions/runs/29587896801
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 5 buckets closed trades, $-49.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 4.8% (22/461)
```

---

## Run 20260717T143034Z

- UTC timestamp: `20260717T143034Z`
- GitHub run: [#4268](https://github.com/28twagg-ops/TradingBot/actions/runs/29588238675)
- Run id: `29588238675`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`64s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T10:30:37.245520-04:00","date":"2026-07-17","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":62.3,"phases_s":{"reconcile":1.97,"cancel":0.01,"manage":9.19,"scan":50.82,"entries":0.05},"signals":207,"placed":0,"equity":123181.03,"open_positions":3,"pending_orders":0,"open_lots":14,"submitted_today":20,"filled_today":20,"unattributed_contracts":0,"top_signals":["S173:AMD","S173:AKAM","S173:ALB","S173:AMZN","S173:AMP","S173:AME","S173:APH","S173:ADI"],"github_run":"4268","github_run_id":"29588238675","status":"ok"}
```

### Live bot full output

```text
14:30:35  INFO      Mode: exits
14:30:35  INFO        Daily log -> logs/daily/2026-07-17.md
14:30:35  INFO        Daily log reconciled -> logs/daily/2026-07-17.md (3 ledger rows)
14:30:35  INFO        place_all_stops: checking 3 positions...
14:30:35  INFO        STOP already live CARR @ $67.55
14:30:35  INFO        STOP already live CMS @ $73.98
14:30:35  INFO        STOP skipped DOV: fractional (0.3763 shares) — software exit will handle it
14:30:36  INFO        [positions] 3/3 (3 valid)
14:30:36  INFO        Daily log -> logs/daily/2026-07-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:30 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $486.40|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  DOV  P&L +0.1%  $+0.09                                            HOLD|
|  CMS  P&L +0.7%  $+0.71                                            HOLD|
|  CARR  P&L +1.9%  $+1.66                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T10:30:37.245520-04:00 ===

[Run context]
Paper auth OK — equity $123181.03, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 207 signal(s); top: ['S173:AMD', 'S173:AKAM', 'S173:ALB', 'S173:AMZN', 'S173:AMP', 'S173:AME', 'S173:APH', 'S173:ADI']
Paper lab: $123428 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  All bucket slots blocked or closed for today's signals — skip entry loop.
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $123,181.03                             |
|  Signals this run              207                                     |
|  Orders submitted (session)    20                                      |
|  Orders filled today (ledger)  20                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             14                                      |
|  Broker option positions       3                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=353  buckets=46  win=36%                             |
|  Returns   avg=+8.8%  med=-24.2%  p10=-77.0%  p90=+90.2%               |
|  Realized  $+3,447.77                                                  |
|  Raw incl dropped  trades=462  real=$+2,110.58                         |
|  Today     trades=10  avg=+4.8%  med=+57.8%  real=$-19.00              |
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
|  b80  c080_s173_w1_0928_ 35  74% +58.0 +62.9 +177.3 $   +403           |
|  ... 38 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 17   0% -62.7 -72.1 -98.5 $   -712       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (3)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  GOOGL260720C00360000          5    -52.7%   $   -145.00               |
|  AMD260717C00512500            4    -47.0%   $   -124.00               |
|  META260720C00675000           5    -29.4%   $   -100.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=62.3s reconcile=1.97s cancel=0.01s manage=9.19s scan=50.82s entries=0.05s
STATUS: options_morning_bot run complete (PAPER) elapsed=62.3s. run=#4268 https://github.com/28twagg-ops/TradingBot/actions/runs/29588238675
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 5 buckets closed trades, $-19.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 4.8% (22/462)
```

---

## Run 20260717T143533Z

- UTC timestamp: `20260717T143533Z`
- GitHub run: [#4269](https://github.com/28twagg-ops/TradingBot/actions/runs/29588584546)
- Run id: `29588584546`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`44s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T10:35:36.589332-04:00","date":"2026-07-17","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":42.6,"phases_s":{"reconcile":2.08,"cancel":0.02,"manage":2.51,"scan":37.66,"entries":0.11},"signals":206,"placed":0,"equity":123640.03,"open_positions":3,"pending_orders":0,"open_lots":14,"submitted_today":20,"filled_today":20,"unattributed_contracts":0,"top_signals":["S173:AMD","S173:AKAM","S173:ALB","S173:AMZN","S173:AMP","S173:AME","S173:APH","S173:ADI"],"github_run":"4269","github_run_id":"29588584546","status":"ok"}
```

### Live bot full output

```text
14:35:34  INFO      Mode: exits
14:35:35  INFO        Daily log -> logs/daily/2026-07-17.md
14:35:35  INFO        Daily log reconciled -> logs/daily/2026-07-17.md (3 ledger rows)
14:35:35  INFO        place_all_stops: checking 3 positions...
14:35:35  INFO        STOP already live CARR @ $67.55
14:35:35  INFO        STOP already live CMS @ $73.98
14:35:35  INFO        STOP skipped DOV: fractional (0.3763 shares) — software exit will handle it
14:35:35  INFO        [positions] 3/3 (3 valid)
14:35:35  INFO        Daily log -> logs/daily/2026-07-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:35 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $486.15|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  DOV  P&L +0.0%  $+0.02                                            HOLD|
|  CMS  P&L +0.6%  $+0.60                                            HOLD|
|  CARR  P&L +1.8%  $+1.59                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T10:35:36.589332-04:00 ===

[Run context]
Paper auth OK — equity $123640.03, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-17 10:35:39,397 INFO   EXIT [b28|c028_s165_w1_0928_1005_r2|S165] stop_loss (-50.9%) SELL 1 GOOGL260720C00360000 @<= 0.28

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 206 signal(s); top: ['S173:AMD', 'S173:AKAM', 'S173:ALB', 'S173:AMZN', 'S173:AMP', 'S173:AME', 'S173:APH', 'S173:ADI']
Paper lab: $123912 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  All bucket slots blocked or closed for today's signals — skip entry loop.
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $123,640.03                             |
|  Signals this run              206                                     |
|  Orders submitted (session)    20                                      |
|  Orders filled today (ledger)  20                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             14                                      |
|  Broker option positions       3                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=353  buckets=46  win=36%                             |
|  Returns   avg=+8.8%  med=-24.2%  p10=-77.0%  p90=+90.2%               |
|  Realized  $+3,447.77                                                  |
|  Raw incl dropped  trades=462  real=$+2,110.58                         |
|  Today     trades=10  avg=+4.8%  med=+57.8%  real=$-19.00              |
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
|  b80  c080_s173_w1_0928_ 35  74% +58.0 +62.9 +177.3 $   +403           |
|  ... 38 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 17   0% -62.7 -72.1 -98.5 $   -712       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b28  S165 GOOGL260720C00360000 x1 stop_loss (-50.9%)                  |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (3)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  GOOGL260720C00360000          5    -50.9%   $   -140.00               |
|  META260720C00675000           5    -33.8%   $   -115.00               |
|  AMD260717C00512500            4    -33.3%   $    -88.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=42.6s reconcile=2.08s cancel=0.02s manage=2.51s scan=37.66s entries=0.11s
STATUS: options_morning_bot run complete (PAPER) elapsed=42.6s. run=#4269 https://github.com/28twagg-ops/TradingBot/actions/runs/29588584546
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 5 buckets closed trades, $-19.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 4.8% (22/462)
```

---

## Run 20260717T144037Z

- UTC timestamp: `20260717T144037Z`
- GitHub run: [#4270](https://github.com/28twagg-ops/TradingBot/actions/runs/29588926464)
- Run id: `29588926464`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`48s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T10:40:40.421585-04:00","date":"2026-07-17","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":46.8,"phases_s":{"reconcile":2.32,"cancel":0.15,"manage":4.49,"scan":39.09,"entries":0.19},"signals":206,"placed":0,"equity":124087.01,"open_positions":3,"pending_orders":0,"open_lots":13,"submitted_today":20,"filled_today":20,"unattributed_contracts":0,"top_signals":["S173:AMD","S173:AKAM","S173:ALB","S173:GOOGL","S173:GOOG","S173:AMZN","S173:AMP","S173:AME"],"github_run":"4270","github_run_id":"29588926464","status":"ok"}
```

### Live bot full output

```text
14:40:37  INFO      Mode: exits
14:40:38  INFO        Daily log -> logs/daily/2026-07-17.md
14:40:38  INFO        Daily log reconciled -> logs/daily/2026-07-17.md (3 ledger rows)
14:40:38  INFO        place_all_stops: checking 3 positions...
14:40:38  INFO        STOP already live CARR @ $67.55
14:40:38  INFO        STOP already live CMS @ $73.98
14:40:38  INFO        STOP skipped DOV: fractional (0.3763 shares) — software exit will handle it
14:40:39  INFO        [positions] 3/3 (3 valid)
14:40:39  INFO        Daily log -> logs/daily/2026-07-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:40 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $486.11|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  DOV  P&L -0.0%  $-0.02                                            HOLD|
|  CMS  P&L +0.5%  $+0.52                                            HOLD|
|  CARR  P&L +1.9%  $+1.67                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T10:40:40.421585-04:00 ===

[Run context]
Paper auth OK — equity $124107.01, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 206 signal(s); top: ['S173:AMD', 'S173:AKAM', 'S173:ALB', 'S173:GOOGL', 'S173:GOOG', 'S173:AMZN', 'S173:AMP', 'S173:AME']
Paper lab: $123979 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  All bucket slots blocked or closed for today's signals — skip entry loop.
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $124,087.01                             |
|  Signals this run              206                                     |
|  Orders submitted (session)    20                                      |
|  Orders filled today (ledger)  20                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             13                                      |
|  Broker option positions       3                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=354  buckets=46  win=36%                             |
|  Returns   avg=+8.6%  med=-25.2%  p10=-77.0%  p90=+89.9%               |
|  Realized  $+3,422.77                                                  |
|  Raw incl dropped  trades=463  real=$+2,085.58                         |
|  Today     trades=11  avg=+0.2%  med=+56.9%  real=$-44.00              |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b28  c028_s165_w1_0928_ 11  82% +58.3 +80.0 +102.0 $   +338           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b99  c099_s163_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b80  c080_s173_w1_0928_ 35  74% +58.0 +62.9 +177.3 $   +403           |
|  ... 38 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 17   0% -62.7 -72.1 -98.5 $   -712       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (3)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMD260717C00512500            4    -39.4%   $   -104.00               |
|  GOOGL260720C00360000          4    -47.3%   $   -104.00               |
|  META260720C00675000           5    -27.9%   $    -95.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=46.8s reconcile=2.32s cancel=0.15s manage=4.49s scan=39.09s entries=0.19s
STATUS: options_morning_bot run complete (PAPER) elapsed=46.8s. run=#4270 https://github.com/28twagg-ops/TradingBot/actions/runs/29588926464
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 6 buckets closed trades, $-44.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 4.8% (22/463)
```

---

## Run 20260717T144534Z

- UTC timestamp: `20260717T144534Z`
- GitHub run: [#4271](https://github.com/28twagg-ops/TradingBot/actions/runs/29589265370)
- Run id: `29589265370`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`66s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T10:45:38.083658-04:00","date":"2026-07-17","mode":"entry+manage","header":"entry+manage (10 new)","elapsed_s":64.8,"phases_s":{"reconcile":2.32,"cancel":0.16,"manage":8.13,"scan":45.38,"entries":5.8,"reconcile2":2.45},"signals":204,"placed":10,"equity":123282.01,"open_positions":4,"pending_orders":5,"open_lots":17,"submitted_today":30,"filled_today":25,"unattributed_contracts":0,"top_signals":["S173:AMD","S173:AKAM","S173:ALB","S173:GOOGL","S173:GOOG","S173:AMZN","S173:AMP","S173:AME"],"github_run":"4271","github_run_id":"29589265370","status":"ok"}
```

### Live bot full output

```text
14:45:35  INFO      Mode: exits
14:45:36  INFO        Daily log -> logs/daily/2026-07-17.md
14:45:36  INFO        Daily log reconciled -> logs/daily/2026-07-17.md (3 ledger rows)
14:45:36  INFO        place_all_stops: checking 3 positions...
14:45:36  INFO        STOP already live CARR @ $67.55
14:45:36  INFO        STOP already live CMS @ $73.98
14:45:36  INFO        STOP skipped DOV: fractional (0.3763 shares) — software exit will handle it
14:45:37  INFO        [positions] 3/3 (3 valid)
14:45:37  INFO        Daily log -> logs/daily/2026-07-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:45 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $486.20|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  DOV  P&L -0.2%  $-0.13                                            HOLD|
|  CMS  P&L +0.8%  $+0.74                                            HOLD|
|  CARR  P&L +1.9%  $+1.64                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T10:45:38.083658-04:00 ===

[Run context]
Paper auth OK — equity $123282.01, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-17 10:45:49,016 INFO   EXIT [b21|c021_s173_w2_1005_1045_r2|S173] stop_loss (-60.6%) SELL 1 AMD260717C00512500 @<= 0.22

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 204 signal(s); top: ['S173:AMD', 'S173:AKAM', 'S173:ALB', 'S173:GOOGL', 'S173:GOOG', 'S173:AMZN', 'S173:AMP', 'S173:AME']
Paper lab: $122830 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 20 no tradeable call, 191 already attempted today, 990 pending order
Placed 10 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $123,282.01                             |
|  Signals this run              204                                     |
|  Orders submitted (session)    30                                      |
|  Orders filled today (ledger)  25                                      |
|  Entries placed this run       10                                      |
|  Open virtual lots             17                                      |
|  Broker option positions       4                                       |
|  Pending orders                5                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=360  buckets=46  win=35%                             |
|  Returns   avg=+7.7%  med=-28.8%  p10=-77.0%  p90=+87.8%               |
|  Realized  $+3,240.77                                                  |
|  Raw incl dropped  trades=469  real=$+1,903.58                         |
|  Today     trades=12  avg=-5.0%  med=+5.7%  real=$-85.00               |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b28  c028_s165_w1_0928_ 11  82% +58.3 +80.0 +102.0 $   +338           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b99  c099_s163_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b80  c080_s173_w1_0928_ 35  74% +58.0 +62.9 +177.3 $   +403           |
|  ... 38 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b83  c083_s173_w4_1120_ 13   8% -60.9 -69.2 -87.7 $   -459       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (5)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S165:META(5)                            |
+------------------------------------------------------------------------+
|  b10  S165 META     limit=0.74                                         |
|  b30  S165 META     limit=0.74                                         |
|  b50  S165 META     limit=0.74                                         |
|  b70  S165 META     limit=0.74                                         |
|  b90  S165 META     limit=0.74                                         |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (4)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMD260717C00512500            3    -71.2%   $   -141.00               |
|  META260720C00675000           5    -30.9%   $   -105.00               |
|  GOOGL260720C00360000          4    -34.5%   $    -76.00               |
|  AMD260717C00505000            5    -13.4%   $    -45.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=64.8s reconcile=2.32s cancel=0.16s manage=8.13s scan=45.38s entries=5.8s
STATUS: options_morning_bot run complete (PAPER) elapsed=64.8s. run=#4271 https://github.com/28twagg-ops/TradingBot/actions/runs/29589265370
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 7 buckets closed trades, $-85.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 4.7% (22/469)
```

---

## Run 20260717T145040Z

- UTC timestamp: `20260717T145040Z`
- GitHub run: [#4272](https://github.com/28twagg-ops/TradingBot/actions/runs/29589611334)
- Run id: `29589611334`
- Live bot: exit=`0`, duration=`4s`
- Options bot: exit=`0`, duration=`47s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T10:50:45.522316-04:00","date":"2026-07-17","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":44.9,"phases_s":{"reconcile":2.37,"cancel":0.16,"manage":6.59,"scan":34.93,"entries":0.21},"signals":205,"placed":0,"equity":123765.79,"open_positions":5,"pending_orders":0,"open_lots":22,"submitted_today":30,"filled_today":30,"unattributed_contracts":0,"top_signals":["S173:AMD","S173:AKAM","S173:ALB","S173:GOOGL","S173:GOOG","S173:AMZN","S173:AMP","S173:AME"],"github_run":"4272","github_run_id":"29589611334","status":"ok"}
```

### Live bot full output

```text
14:50:42  INFO      Mode: exits
14:50:43  INFO        Daily log -> logs/daily/2026-07-17.md
14:50:43  INFO        Daily log reconciled -> logs/daily/2026-07-17.md (3 ledger rows)
14:50:43  INFO        place_all_stops: checking 3 positions...
14:50:43  INFO        STOP already live CARR @ $67.55
14:50:43  INFO        STOP already live CMS @ $73.98
14:50:43  INFO        STOP skipped DOV: fractional (0.3763 shares) — software exit will handle it
14:50:44  INFO        [positions] 3/3 (3 valid)
14:50:44  INFO        Daily log -> logs/daily/2026-07-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:50 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $486.26|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  DOV  P&L -0.2%  $-0.15                                            HOLD|
|  CMS  P&L +0.8%  $+0.73                                            HOLD|
|  CARR  P&L +2.0%  $+1.73                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T10:50:45.522316-04:00 ===

[Run context]
Paper auth OK — equity $123765.79, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-17 10:50:50,303 INFO   EXIT [b82|c082_s173_w3_1045_1120_r5|S173] take_profit (+79.1%) SELL 1 AMD260717C00505000 @<= 1.21

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 205 signal(s); top: ['S173:AMD', 'S173:AKAM', 'S173:ALB', 'S173:GOOGL', 'S173:GOOG', 'S173:AMZN', 'S173:AMP', 'S173:AME']
Paper lab: $123481 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  All bucket slots blocked or closed for today's signals — skip entry loop.
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $123,765.79                             |
|  Signals this run              205                                     |
|  Orders submitted (session)    30                                      |
|  Orders filled today (ledger)  30                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             22                                      |
|  Broker option positions       5                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=367  buckets=46  win=35%                             |
|  Returns   avg=+6.4%  med=-31.5%  p10=-77.0%  p90=+87.4%               |
|  Realized  $+2,934.77                                                  |
|  Raw incl dropped  trades=476  real=$+1,597.58                         |
|  Today     trades=12  avg=-5.0%  med=+5.7%  real=$-85.00               |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b28  c028_s165_w1_0928_ 11  82% +58.3 +80.0 +102.0 $   +338           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b99  c099_s163_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b80  c080_s173_w1_0928_ 35  74% +58.0 +62.9 +177.3 $   +403           |
|  ... 38 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b83  c083_s173_w4_1120_ 13   8% -60.9 -69.2 -87.7 $   -459       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b82  S173 AMD260717C00505000 x1 take_profit (+79.1%)                  |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (5)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  META260720C00675000           5    -48.5%   $   -165.00               |
|  AMD260717C00505000            4    +58.2%   $   +156.00               |
|  META260720C00670000           5    -32.4%   $   -120.00               |
|  AMD260717C00512500            3    -43.9%   $    -87.00               |
|  GOOGL260720C00360000          4    -36.4%   $    -80.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=44.9s reconcile=2.37s cancel=0.16s manage=6.59s scan=34.93s entries=0.21s
STATUS: options_morning_bot run complete (PAPER) elapsed=44.9s. run=#4272 https://github.com/28twagg-ops/TradingBot/actions/runs/29589611334
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 7 buckets closed trades, $-85.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 4.6% (22/476)
```

---

## Run 20260717T145536Z

- UTC timestamp: `20260717T145536Z`
- GitHub run: [#4273](https://github.com/28twagg-ops/TradingBot/actions/runs/29589954387)
- Run id: `29589954387`
- Live bot: exit=`0`, duration=`4s`
- Options bot: exit=`0`, duration=`50s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T10:55:40.962763-04:00","date":"2026-07-17","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":48.5,"phases_s":{"reconcile":2.24,"cancel":0.15,"manage":6.27,"scan":38.93,"entries":0.18},"signals":205,"placed":0,"equity":123070.97,"open_positions":5,"pending_orders":0,"open_lots":21,"submitted_today":30,"filled_today":30,"unattributed_contracts":0,"top_signals":["S173:AMD","S173:AKAM","S173:ALB","S173:GOOGL","S173:GOOG","S173:AMZN","S173:AMP","S173:AME"],"github_run":"4273","github_run_id":"29589954387","status":"ok"}
```

### Live bot full output

```text
14:55:38  INFO      Mode: exits
14:55:38  INFO        Daily log -> logs/daily/2026-07-17.md
14:55:38  INFO        Daily log reconciled -> logs/daily/2026-07-17.md (3 ledger rows)
14:55:39  INFO        place_all_stops: checking 3 positions...
14:55:39  INFO        STOP already live CARR @ $67.55
14:55:39  INFO        STOP already live CMS @ $73.98
14:55:39  INFO        STOP skipped DOV: fractional (0.3763 shares) — software exit will handle it
14:55:39  INFO        [positions] 3/3 (3 valid)
14:55:40  INFO        Daily log -> logs/daily/2026-07-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:55 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $486.52|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  DOV  P&L -0.0%  $-0.03                                            HOLD|
|  CMS  P&L +0.8%  $+0.79                                            HOLD|
|  CARR  P&L +2.1%  $+1.82                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T10:55:40.962763-04:00 ===

[Run context]
Paper auth OK — equity $123061.77, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-17 10:55:45,702 INFO   EXIT [b29|c029_s165_w2_1005_1045_r2|S165] stop_loss (-51.5%) SELL 1 META260720C00675000 @<= 0.30
2026-07-17 10:55:46,914 INFO   EXIT [b61|c061_s173_w2_1005_1045_r4|S173] stop_loss (-54.5%) SELL 1 AMD260717C00512500 @<= 0.27

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 205 signal(s); top: ['S173:AMD', 'S173:AKAM', 'S173:ALB', 'S173:GOOGL', 'S173:GOOG', 'S173:AMZN', 'S173:AMP', 'S173:AME']
Paper lab: $123018 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  All bucket slots blocked or closed for today's signals — skip entry loop.
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $123,070.97                             |
|  Signals this run              205                                     |
|  Orders submitted (session)    30                                      |
|  Orders filled today (ledger)  30                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             21                                      |
|  Broker option positions       5                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=368  buckets=46  win=35%                             |
|  Returns   avg=+6.6%  med=-31.5%  p10=-77.0%  p90=+87.3%               |
|  Realized  $+2,992.77                                                  |
|  Raw incl dropped  trades=477  real=$+1,655.58                         |
|  Today     trades=13  avg=+2.1%  med=+56.9%  real=$-27.00              |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b28  c028_s165_w1_0928_ 11  82% +58.3 +80.0 +102.0 $   +338           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b99  c099_s163_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b80  c080_s173_w1_0928_ 35  74% +58.0 +62.9 +177.3 $   +403           |
|  ... 38 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b83  c083_s173_w4_1120_ 13   8% -60.9 -69.2 -87.7 $   -459       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b29  S165 META260720C00675000 x1 stop_loss (-51.5%)                   |
|  b61  S173 AMD260717C00512500 x1 stop_loss (-54.5%)                    |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (5)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  META260720C00675000           4    -52.9%   $   -144.00               |
|  META260720C00670000           5    -37.8%   $   -140.00               |
|  GOOGL260720C00360000          4    -47.3%   $   -104.00               |
|  AMD260717C00512500            2    -57.6%   $    -76.00               |
|  AMD260717C00505000            4    +17.9%   $    +48.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=48.5s reconcile=2.24s cancel=0.15s manage=6.27s scan=38.93s entries=0.18s
STATUS: options_morning_bot run complete (PAPER) elapsed=48.5s. run=#4273 https://github.com/28twagg-ops/TradingBot/actions/runs/29589954387
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 8 buckets closed trades, $-27.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 4.6% (22/477)
```

---

## Run 20260717T150005Z

- UTC timestamp: `20260717T150005Z`
- GitHub run: [#4274](https://github.com/28twagg-ops/TradingBot/actions/runs/29590245348)
- Run id: `29590245348`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T10:55:40.962763-04:00","date":"2026-07-17","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":48.5,"phases_s":{"reconcile":2.24,"cancel":0.15,"manage":6.27,"scan":38.93,"entries":0.18},"signals":205,"placed":0,"equity":123070.97,"open_positions":5,"pending_orders":0,"open_lots":21,"submitted_today":30,"filled_today":30,"unattributed_contracts":0,"top_signals":["S173:AMD","S173:AKAM","S173:ALB","S173:GOOGL","S173:GOOG","S173:AMZN","S173:AMP","S173:AME"],"github_run":"4273","github_run_id":"29589954387","status":"ok"}
```

### Live bot full output

```text
15:00:06  INFO      Mode: exits
15:00:07  INFO        Daily log -> logs/daily/2026-07-17.md
15:00:07  INFO        Daily log reconciled -> logs/daily/2026-07-17.md (3 ledger rows)
15:00:07  INFO        place_all_stops: checking 3 positions...
15:00:07  INFO        STOP already live CARR @ $67.55
15:00:07  INFO        STOP already live CMS @ $73.98
15:00:07  INFO        STOP skipped DOV: fractional (0.3763 shares) — software exit will handle it
15:00:07  INFO        [positions] 3/3 (3 valid)
15:00:07  INFO        Daily log -> logs/daily/2026-07-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:00 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $486.89|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  DOV  P&L +0.0%  $+0.01                                            HOLD|
|  CMS  P&L +1.0%  $+0.95                                            HOLD|
|  CARR  P&L +2.3%  $+2.00                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T11:00:08.694325-04:00 ===

[Run context]
Paper auth OK — equity $122485.73, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
```

---

## Run 20260717T150103Z

- UTC timestamp: `20260717T150103Z`
- GitHub run: [#4275](https://github.com/28twagg-ops/TradingBot/actions/runs/29590294722)
- Run id: `29590294722`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`75s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T11:01:07.158587-04:00","date":"2026-07-17","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":73.5,"phases_s":{"reconcile":2.25,"cancel":0.15,"manage":12.71,"scan":57.4,"entries":0.2},"signals":204,"placed":0,"equity":122338.71,"open_positions":4,"pending_orders":0,"open_lots":18,"submitted_today":30,"filled_today":30,"unattributed_contracts":0,"top_signals":["S173:AMD","S173:AKAM","S173:ALB","S173:AMZN","S173:AMP","S173:AME","S173:APH","S173:ADI"],"github_run":"4275","github_run_id":"29590294722","status":"ok"}
```

### Live bot full output

```text
15:01:04  INFO      Mode: exits
15:01:05  INFO        Daily log -> logs/daily/2026-07-17.md
15:01:05  INFO        Daily log reconciled -> logs/daily/2026-07-17.md (3 ledger rows)
15:01:05  INFO        place_all_stops: checking 3 positions...
15:01:05  INFO        STOP already live CARR @ $67.55
15:01:05  INFO        STOP already live CMS @ $73.98
15:01:05  INFO        STOP skipped DOV: fractional (0.3763 shares) — software exit will handle it
15:01:06  INFO        [positions] 3/3 (3 valid)
15:01:06  INFO        Daily log -> logs/daily/2026-07-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $486.91|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  DOV  P&L +0.0%  $+0.01                                            HOLD|
|  CMS  P&L +1.0%  $+1.00                                            HOLD|
|  CARR  P&L +2.3%  $+1.96                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T11:01:07.158587-04:00 ===

[Run context]
Paper auth OK — equity $122338.71, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-17 11:01:16,968 INFO   EXIT [b89|c089_s165_w2_1005_1045_r5|S165] stop_loss (-55.9%) SELL 1 META260720C00675000 @<= 0.27
2026-07-17 11:01:20,112 INFO   EXIT [b1|c001_s173_w2_1005_1045_r1|S173] stop_loss (-69.7%) SELL 1 AMD260717C00512500 @<= 0.17

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 204 signal(s); top: ['S173:AMD', 'S173:AKAM', 'S173:ALB', 'S173:AMZN', 'S173:AMP', 'S173:AME', 'S173:APH', 'S173:ADI']
Paper lab: $122603 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  All bucket slots blocked or closed for today's signals — skip entry loop.
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $122,338.71                             |
|  Signals this run              204                                     |
|  Orders submitted (session)    30                                      |
|  Orders filled today (ledger)  30                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             18                                      |
|  Broker option positions       4                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=370  buckets=46  win=35%                             |
|  Returns   avg=+6.3%  med=-32.4%  p10=-77.0%  p90=+87.3%               |
|  Realized  $+2,910.77                                                  |
|  Raw incl dropped  trades=479  real=$+1,573.58                         |
|  Today     trades=15  avg=-6.4%  med=-45.5%  real=$-109.00             |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b28  c028_s165_w1_0928_ 11  82% +58.3 +80.0 +102.0 $   +338           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b99  c099_s163_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b80  c080_s173_w1_0928_ 35  74% +58.0 +62.9 +177.3 $   +403           |
|  ... 38 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b83  c083_s173_w4_1120_ 13   8% -60.9 -69.2 -87.7 $   -459       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b89  S165 META260720C00675000 x1 stop_loss (-55.9%)                   |
|  b1   S173 AMD260717C00512500 x1 stop_loss (-69.7%)                    |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (4)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  META260720C00670000           5    -36.5%   $   -135.00               |
|  GOOGL260720C00360000          4    -58.2%   $   -128.00               |
|  META260720C00675000           3    -48.5%   $    -99.00               |
|  AMD260717C00505000            4     -4.5%   $    -12.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=73.5s reconcile=2.25s cancel=0.15s manage=12.71s scan=57.4s entries=0.2s
STATUS: options_morning_bot run complete (PAPER) elapsed=73.5s. run=#4275 https://github.com/28twagg-ops/TradingBot/actions/runs/29590294722
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 10 buckets closed trades, $-109.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 4.6% (22/479)
```

---

## Run 20260717T150539Z

- UTC timestamp: `20260717T150539Z`
- GitHub run: [#4276](https://github.com/28twagg-ops/TradingBot/actions/runs/29590645097)
- Run id: `29590645097`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`55s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T11:05:43.182754-04:00","date":"2026-07-17","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":53.3,"phases_s":{"reconcile":3.06,"cancel":0.07,"manage":4.68,"scan":44.96,"entries":0.14},"signals":205,"placed":0,"equity":121933.65,"open_positions":4,"pending_orders":0,"open_lots":15,"submitted_today":30,"filled_today":30,"unattributed_contracts":0,"top_signals":["S173:AMD","S173:AKAM","S173:ALB","S173:AMZN","S173:AMP","S173:AME","S173:APH","S173:ADI"],"github_run":"4276","github_run_id":"29590645097","status":"ok"}
```

### Live bot full output

```text
15:05:40  INFO      Mode: exits
15:05:41  INFO        Daily log -> logs/daily/2026-07-17.md
15:05:41  INFO        Daily log reconciled -> logs/daily/2026-07-17.md (3 ledger rows)
15:05:41  INFO        place_all_stops: checking 3 positions...
15:05:41  INFO        STOP already live CARR @ $67.55
15:05:41  INFO        STOP already live CMS @ $73.98
15:05:41  INFO        STOP skipped DOV: fractional (0.3763 shares) — software exit will handle it
15:05:42  INFO        [positions] 3/3 (3 valid)
15:05:42  INFO        Daily log -> logs/daily/2026-07-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:05 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $486.63|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  DOV  P&L -0.0%  $-0.02                                            HOLD|
|  CMS  P&L +0.8%  $+0.81                                            HOLD|
|  CARR  P&L +2.2%  $+1.90                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T11:05:43.182754-04:00 ===

[Run context]
Paper auth OK — equity $121934.41, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-17 11:05:47,630 INFO   EXIT [b28|c028_s165_w1_0928_1005_r2|S165] stop_loss (-61.8%) SELL 1 GOOGL260720C00360000 @<= 0.22
2026-07-17 11:05:48,914 INFO   EXIT [b29|c029_s165_w2_1005_1045_r2|S165] stop_loss (-52.9%) SELL 1 META260720C00675000 @<= 0.33

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 205 signal(s); top: ['S173:AMD', 'S173:AKAM', 'S173:ALB', 'S173:AMZN', 'S173:AMP', 'S173:AME', 'S173:APH', 'S173:ADI']
Paper lab: $121829 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  All bucket slots blocked or closed for today's signals — skip entry loop.
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $121,933.65                             |
|  Signals this run              205                                     |
|  Orders submitted (session)    30                                      |
|  Orders filled today (ledger)  30                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             15                                      |
|  Broker option positions       4                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=373  buckets=46  win=34%                             |
|  Returns   avg=+5.7%  med=-33.3%  p10=-76.4%  p90=+87.1%               |
|  Realized  $+2,795.77                                                  |
|  Raw incl dropped  trades=482  real=$+1,458.58                         |
|  Today     trades=18  avg=-15.4%  med=-53.7%  real=$-224.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b28  c028_s165_w1_0928_ 11  82% +58.3 +80.0 +102.0 $   +338           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b99  c099_s163_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b80  c080_s173_w1_0928_ 35  74% +58.0 +62.9 +177.3 $   +403           |
|  ... 38 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b83  c083_s173_w4_1120_ 13   8% -60.9 -69.2 -87.7 $   -459       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b28  S165 GOOGL260720C00360000 x1 stop_loss (-61.8%)                  |
|  b29  S165 META260720C00675000 x1 stop_loss (-52.9%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (4)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  META260720C00670000           5    -33.8%   $   -125.00               |
|  AMD260717C00505000            4    -43.3%   $   -116.00               |
|  META260720C00675000           3    -52.9%   $   -108.00               |
|  GOOGL260720C00360000          3    -61.8%   $   -102.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=53.3s reconcile=3.06s cancel=0.07s manage=4.68s scan=44.96s entries=0.14s
STATUS: options_morning_bot run complete (PAPER) elapsed=53.3s. run=#4276 https://github.com/28twagg-ops/TradingBot/actions/runs/29590645097
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 13 buckets closed trades, $-224.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 4.6% (22/482)
```

---

## Run 20260717T151037Z

- UTC timestamp: `20260717T151037Z`
- GitHub run: [#4277](https://github.com/28twagg-ops/TradingBot/actions/runs/29590989896)
- Run id: `29590989896`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`47s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T11:10:40.246254-04:00","date":"2026-07-17","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":45.5,"phases_s":{"reconcile":2.0,"cancel":0.04,"manage":4.74,"scan":38.21,"entries":0.14},"signals":205,"placed":0,"equity":122349.49,"open_positions":4,"pending_orders":0,"open_lots":13,"submitted_today":30,"filled_today":30,"unattributed_contracts":0,"top_signals":["S173:AMD","S173:AKAM","S173:ALB","S173:GOOGL","S173:GOOG","S173:AMZN","S173:AMP","S173:AME"],"github_run":"4277","github_run_id":"29590989896","status":"ok"}
```

### Live bot full output

```text
15:10:38  INFO      Mode: exits
15:10:38  INFO        Daily log -> logs/daily/2026-07-17.md
15:10:38  INFO        Daily log reconciled -> logs/daily/2026-07-17.md (3 ledger rows)
15:10:38  INFO        place_all_stops: checking 3 positions...
15:10:38  INFO        STOP already live CARR @ $67.55
15:10:38  INFO        STOP already live CMS @ $73.98
15:10:38  INFO        STOP skipped DOV: fractional (0.3763 shares) — software exit will handle it
15:10:39  INFO        [positions] 3/3 (3 valid)
15:10:39  INFO        Daily log -> logs/daily/2026-07-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $486.42|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  DOV  P&L -0.0%  $-0.03                                            HOLD|
|  CMS  P&L +0.8%  $+0.74                                            HOLD|
|  CARR  P&L +2.1%  $+1.77                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T11:10:40.246254-04:00 ===

[Run context]
Paper auth OK — equity $122349.49, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-17 11:10:43,868 INFO   EXIT [b49|c049_s165_w2_1005_1045_r3|S165] stop_loss (-50.0%) SELL 1 META260720C00675000 @<= 0.31
2026-07-17 11:10:47,159 INFO   EXIT [b48|c048_s165_w1_0928_1005_r3|S165] stop_loss (-54.5%) SELL 1 GOOGL260720C00360000 @<= 0.26

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 205 signal(s); top: ['S173:AMD', 'S173:AKAM', 'S173:ALB', 'S173:GOOGL', 'S173:GOOG', 'S173:AMZN', 'S173:AMP', 'S173:AME']
Paper lab: $122223 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  All bucket slots blocked or closed for today's signals — skip entry loop.
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $122,349.49                             |
|  Signals this run              205                                     |
|  Orders submitted (session)    30                                      |
|  Orders filled today (ledger)  30                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             13                                      |
|  Broker option positions       4                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=375  buckets=46  win=34%                             |
|  Returns   avg=+5.4%  med=-33.8%  p10=-75.8%  p90=+87.0%               |
|  Realized  $+2,729.77                                                  |
|  Raw incl dropped  trades=484  real=$+1,392.58                         |
|  Today     trades=20  avg=-19.3%  med=-53.7%  real=$-290.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b28  c028_s165_w1_0928_ 12  75% +48.6 +77.3 +102.0 $   +306           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b99  c099_s163_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b80  c080_s173_w1_0928_ 35  74% +58.0 +62.9 +177.3 $   +403           |
|  ... 38 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b83  c083_s173_w4_1120_ 13   8% -60.9 -69.2 -87.7 $   -459       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b49  S165 META260720C00675000 x1 stop_loss (-50.0%)                   |
|  b48  S165 GOOGL260720C00360000 x1 stop_loss (-54.5%)                  |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (4)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  META260720C00670000           5    -37.8%   $   -140.00               |
|  AMD260717C00505000            4    -49.3%   $   -132.00               |
|  GOOGL260720C00360000          2    -54.5%   $    -60.00               |
|  META260720C00675000           1    -51.5%   $    -35.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=45.5s reconcile=2.0s cancel=0.04s manage=4.74s scan=38.21s entries=0.14s
STATUS: options_morning_bot run complete (PAPER) elapsed=45.5s. run=#4277 https://github.com/28twagg-ops/TradingBot/actions/runs/29590989896
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 13 buckets closed trades, $-290.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 4.5% (22/484)
```

---

## Run 20260717T151538Z

- UTC timestamp: `20260717T151538Z`
- GitHub run: [#4278](https://github.com/28twagg-ops/TradingBot/actions/runs/29591333369)
- Run id: `29591333369`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`60s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T11:15:42.131366-04:00","date":"2026-07-17","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":58.3,"phases_s":{"reconcile":2.09,"cancel":0.11,"manage":6.2,"scan":49.26,"entries":0.14},"signals":203,"placed":0,"equity":122112.57,"open_positions":3,"pending_orders":0,"open_lots":11,"submitted_today":30,"filled_today":30,"unattributed_contracts":0,"top_signals":["S173:AMD","S173:AKAM","S173:ALB","S173:GOOGL","S173:AMZN","S173:AMP","S173:AME","S173:APH"],"github_run":"4278","github_run_id":"29591333369","status":"ok"}
```

### Live bot full output

```text
15:15:39  INFO      Mode: exits
15:15:40  INFO        Daily log -> logs/daily/2026-07-17.md
15:15:40  INFO        Daily log reconciled -> logs/daily/2026-07-17.md (3 ledger rows)
15:15:40  INFO        place_all_stops: checking 3 positions...
15:15:40  INFO        STOP already live CARR @ $67.55
15:15:40  INFO        STOP already live CMS @ $73.98
15:15:40  INFO        STOP skipped DOV: fractional (0.3763 shares) — software exit will handle it
15:15:41  INFO        [positions] 3/3 (3 valid)
15:15:41  INFO        Daily log -> logs/daily/2026-07-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:15 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $486.05|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  DOV  P&L -0.2%  $-0.17                                            HOLD|
|  CMS  P&L +0.6%  $+0.61                                            HOLD|
|  CARR  P&L +1.9%  $+1.67                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T11:15:42.131366-04:00 ===

[Run context]
Paper auth OK — equity $122112.57, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-17 11:15:50,823 INFO   EXIT [b8|c008_s165_w1_0928_1005_r1|S165] stop_loss (-54.5%) SELL 1 GOOGL260720C00360000 @<= 0.26

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 203 signal(s); top: ['S173:AMD', 'S173:AKAM', 'S173:ALB', 'S173:GOOGL', 'S173:AMZN', 'S173:AMP', 'S173:AME', 'S173:APH']
Paper lab: $122190 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  All bucket slots blocked or closed for today's signals — skip entry loop.
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $122,112.57                             |
|  Signals this run              203                                     |
|  Orders submitted (session)    30                                      |
|  Orders filled today (ledger)  30                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             11                                      |
|  Broker option positions       3                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=377  buckets=46  win=34%                             |
|  Returns   avg=+5.1%  med=-33.9%  p10=-75.2%  p90=+86.8%               |
|  Realized  $+2,667.77                                                  |
|  Raw incl dropped  trades=486  real=$+1,330.58                         |
|  Today     trades=22  avg=-22.1%  med=-51.2%  real=$-352.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b28  c028_s165_w1_0928_ 12  75% +48.6 +77.3 +102.0 $   +306           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b99  c099_s163_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b80  c080_s173_w1_0928_ 35  74% +58.0 +62.9 +177.3 $   +403           |
|  ... 38 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b83  c083_s173_w4_1120_ 13   8% -60.9 -69.2 -87.7 $   -459       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b8   S165 GOOGL260720C00360000 x1 stop_loss (-54.5%)                  |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (3)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  META260720C00670000           5    -39.2%   $   -145.00               |
|  AMD260717C00505000            4    -46.3%   $   -124.00               |
|  META260720C00675000           1    -50.0%   $    -34.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=58.3s reconcile=2.09s cancel=0.11s manage=6.2s scan=49.26s entries=0.14s
STATUS: options_morning_bot run complete (PAPER) elapsed=58.3s. run=#4278 https://github.com/28twagg-ops/TradingBot/actions/runs/29591333369
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 14 buckets closed trades, $-352.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 4.5% (22/486)
```

---

## Run 20260717T152040Z

- UTC timestamp: `20260717T152040Z`
- GitHub run: [#4279](https://github.com/28twagg-ops/TradingBot/actions/runs/29591672032)
- Run id: `29591672032`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`60s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T11:20:45.635036-04:00","date":"2026-07-17","mode":"entry+manage","header":"entry+manage (10 new)","elapsed_s":58.1,"phases_s":{"reconcile":2.15,"cancel":0.15,"manage":4.83,"scan":42.02,"entries":6.2,"reconcile2":2.19},"signals":200,"placed":10,"equity":122297.55,"open_positions":3,"pending_orders":0,"open_lots":19,"submitted_today":40,"filled_today":40,"unattributed_contracts":0,"top_signals":["S173:AMD","S173:AKAM","S173:ALB","S173:GOOGL","S173:GOOG","S173:AMZN","S173:AMP","S173:AME"],"github_run":"4279","github_run_id":"29591672032","status":"ok"}
```

### Live bot full output

```text
15:20:42  INFO      Mode: exits
15:20:43  INFO        Daily log -> logs/daily/2026-07-17.md
15:20:43  INFO        Daily log reconciled -> logs/daily/2026-07-17.md (3 ledger rows)
15:20:43  INFO        place_all_stops: checking 3 positions...
15:20:44  INFO        STOP already live CARR @ $67.55
15:20:44  INFO        STOP already live CMS @ $73.98
15:20:44  INFO        STOP skipped DOV: fractional (0.3763 shares) — software exit will handle it
15:20:44  INFO        [positions] 3/3 (3 valid)
15:20:44  INFO        Daily log -> logs/daily/2026-07-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $485.87|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  DOV  P&L -0.3%  $-0.27                                            HOLD|
|  CMS  P&L +0.6%  $+0.58                                            HOLD|
|  CARR  P&L +1.9%  $+1.62                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T11:20:45.635036-04:00 ===

[Run context]
Paper auth OK — equity $122297.55, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-17 11:20:51,708 INFO   EXIT [b29|c029_s165_w2_1005_1045_r2|S165] stop_loss (-50.0%) SELL 1 META260720C00675000 @<= 0.31

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 200 signal(s); top: ['S173:AMD', 'S173:AKAM', 'S173:ALB', 'S173:GOOGL', 'S173:GOOG', 'S173:AMZN', 'S173:AMP', 'S173:AME']
Paper lab: $122561 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 30 no tradeable call, 179 already attempted today, 960 pending order
Placed 10 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $122,297.55                             |
|  Signals this run              200                                     |
|  Orders submitted (session)    40                                      |
|  Orders filled today (ledger)  40                                      |
|  Entries placed this run       10                                      |
|  Open virtual lots             19                                      |
|  Broker option positions       3                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=383  buckets=47  win=33%                             |
|  Returns   avg=+4.1%  med=-35.3%  p10=-73.9%  p90=+86.5%               |
|  Realized  $+2,483.77                                                  |
|  Raw incl dropped  trades=492  real=$+1,146.58                         |
|  Today     trades=24  avg=-24.6%  med=-51.2%  real=$-415.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b28  c028_s165_w1_0928_ 12  75% +48.6 +77.3 +102.0 $   +306           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b99  c099_s163_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b80  c080_s173_w1_0928_ 35  74% +58.0 +62.9 +177.3 $   +403           |
|  ... 39 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b83  c083_s173_w4_1120_ 13   8% -60.9 -69.2 -87.7 $   -459       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (3)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  META260720C00670000           5    -37.8%   $   -140.00               |
|  AMD260717C00505000            9    -19.9%   $   -105.00               |
|  META260720C00667500           5    -15.2%   $    -50.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=58.1s reconcile=2.15s cancel=0.15s manage=4.83s scan=42.02s entries=6.2s
STATUS: options_morning_bot run complete (PAPER) elapsed=58.1s. run=#4279 https://github.com/28twagg-ops/TradingBot/actions/runs/29591672032
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 15 buckets closed trades, $-415.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 4.5% (22/492)
```

---

## Run 20260717T152537Z

- UTC timestamp: `20260717T152537Z`
- GitHub run: [#4280](https://github.com/28twagg-ops/TradingBot/actions/runs/29592011819)
- Run id: `29592011819`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`49s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T11:25:40.222573-04:00","date":"2026-07-17","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":47.4,"phases_s":{"reconcile":1.51,"cancel":0.14,"manage":3.68,"scan":41.55,"entries":0.11},"signals":201,"placed":0,"equity":122064.33,"open_positions":3,"pending_orders":0,"open_lots":19,"submitted_today":40,"filled_today":40,"unattributed_contracts":0,"top_signals":["S173:AMD","S173:AKAM","S173:ALB","S173:GOOGL","S173:GOOG","S173:AMZN","S173:AMP","S173:AME"],"github_run":"4280","github_run_id":"29592011819","status":"ok"}
```

### Live bot full output

```text
15:25:38  INFO      Mode: exits
15:25:39  INFO        Daily log -> logs/daily/2026-07-17.md
15:25:39  INFO        Daily log reconciled -> logs/daily/2026-07-17.md (3 ledger rows)
15:25:39  INFO        place_all_stops: checking 3 positions...
15:25:39  INFO        STOP already live CARR @ $67.55
15:25:39  INFO        STOP already live CMS @ $73.98
15:25:39  INFO        STOP skipped DOV: fractional (0.3763 shares) — software exit will handle it
15:25:39  INFO        [positions] 3/3 (3 valid)
15:25:39  INFO        Daily log -> logs/daily/2026-07-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:25 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $486.00|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  DOV  P&L -0.4%  $-0.33                                            HOLD|
|  CMS  P&L +0.8%  $+0.73                                            HOLD|
|  CARR  P&L +1.9%  $+1.66                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T11:25:40.222573-04:00 ===

[Run context]
Paper auth OK — equity $122064.33, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 201 signal(s); top: ['S173:AMD', 'S173:AKAM', 'S173:ALB', 'S173:GOOGL', 'S173:GOOG', 'S173:AMZN', 'S173:AMP', 'S173:AME']
Paper lab: $121991 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  All bucket slots blocked or closed for today's signals — skip entry loop.
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $122,064.33                             |
|  Signals this run              201                                     |
|  Orders submitted (session)    40                                      |
|  Orders filled today (ledger)  40                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             19                                      |
|  Broker option positions       3                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=383  buckets=47  win=33%                             |
|  Returns   avg=+4.1%  med=-35.3%  p10=-73.9%  p90=+86.5%               |
|  Realized  $+2,483.77                                                  |
|  Raw incl dropped  trades=492  real=$+1,146.58                         |
|  Today     trades=24  avg=-24.6%  med=-51.2%  real=$-415.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b28  c028_s165_w1_0928_ 12  75% +48.6 +77.3 +102.0 $   +306           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b99  c099_s163_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b80  c080_s173_w1_0928_ 35  74% +58.0 +62.9 +177.3 $   +403           |
|  ... 39 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b83  c083_s173_w4_1120_ 13   8% -60.9 -69.2 -87.7 $   -459       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (3)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMD260717C00505000            9    -43.8%   $   -231.00               |
|  META260720C00670000           5    -44.6%   $   -165.00               |
|  META260720C00667500           5    -19.7%   $    -65.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=47.4s reconcile=1.51s cancel=0.14s manage=3.68s scan=41.55s entries=0.11s
STATUS: options_morning_bot run complete (PAPER) elapsed=47.4s. run=#4280 https://github.com/28twagg-ops/TradingBot/actions/runs/29592011819
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 15 buckets closed trades, $-415.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 4.5% (22/492)
```

---

## Run 20260717T153057Z

- UTC timestamp: `20260717T153057Z`
- GitHub run: [#4281](https://github.com/28twagg-ops/TradingBot/actions/runs/29592362413)
- Run id: `29592362413`
- Live bot: exit=`0`, duration=`4s`
- Options bot: exit=`0`, duration=`66s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T11:31:01.804092-04:00","date":"2026-07-17","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":65.1,"phases_s":{"reconcile":2.15,"cancel":0.15,"manage":10.6,"scan":51.38,"entries":0.18},"signals":204,"placed":0,"equity":122390.33,"open_positions":3,"pending_orders":0,"open_lots":19,"submitted_today":40,"filled_today":40,"unattributed_contracts":0,"top_signals":["S173:AMD","S173:AKAM","S173:ALB","S173:GOOGL","S173:GOOG","S173:AMZN","S173:AMP","S173:AME"],"github_run":"4281","github_run_id":"29592362413","status":"ok"}
```

### Live bot full output

```text
15:30:58  INFO      Mode: exits
15:30:59  INFO        Daily log -> logs/daily/2026-07-17.md
15:30:59  INFO        Daily log reconciled -> logs/daily/2026-07-17.md (3 ledger rows)
15:30:59  INFO        place_all_stops: checking 3 positions...
15:30:59  INFO        STOP already live CARR @ $67.55
15:30:59  INFO        STOP already live CMS @ $73.98
15:30:59  INFO        STOP skipped DOV: fractional (0.3763 shares) — software exit will handle it
15:31:00  INFO        [positions] 3/3 (3 valid)
15:31:00  INFO        Daily log -> logs/daily/2026-07-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:30 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $486.23|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  DOV  P&L -0.3%  $-0.27                                            HOLD|
|  CMS  P&L +0.7%  $+0.69                                            HOLD|
|  CARR  P&L +2.2%  $+1.87                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T11:31:01.804092-04:00 ===

[Run context]
Paper auth OK — equity $122390.33, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 204 signal(s); top: ['S173:AMD', 'S173:AKAM', 'S173:ALB', 'S173:GOOGL', 'S173:GOOG', 'S173:AMZN', 'S173:AMP', 'S173:AME']
Paper lab: $122204 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  All bucket slots blocked or closed for today's signals — skip entry loop.
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $122,390.33                             |
|  Signals this run              204                                     |
|  Orders submitted (session)    40                                      |
|  Orders filled today (ledger)  40                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             19                                      |
|  Broker option positions       3                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=383  buckets=47  win=33%                             |
|  Returns   avg=+4.1%  med=-35.3%  p10=-73.9%  p90=+86.5%               |
|  Realized  $+2,483.77                                                  |
|  Raw incl dropped  trades=492  real=$+1,146.58                         |
|  Today     trades=24  avg=-24.6%  med=-51.2%  real=$-415.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b28  c028_s165_w1_0928_ 12  75% +48.6 +77.3 +102.0 $   +306           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b99  c099_s163_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b80  c080_s173_w1_0928_ 35  74% +58.0 +62.9 +177.3 $   +403           |
|  ... 39 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b83  c083_s173_w4_1120_ 13   8% -60.9 -69.2 -87.7 $   -459       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (3)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMD260717C00505000            9    -35.2%   $   -186.00               |
|  META260720C00670000           5    -36.5%   $   -135.00               |
|  META260720C00667500           5    -12.1%   $    -40.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=65.1s reconcile=2.15s cancel=0.15s manage=10.6s scan=51.38s entries=0.18s
STATUS: options_morning_bot run complete (PAPER) elapsed=65.1s. run=#4281 https://github.com/28twagg-ops/TradingBot/actions/runs/29592362413
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 15 buckets closed trades, $-415.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 4.5% (22/492)
```

---

## Run 20260717T153538Z

- UTC timestamp: `20260717T153538Z`
- GitHub run: [#4282](https://github.com/28twagg-ops/TradingBot/actions/runs/29592712670)
- Run id: `29592712670`
- Live bot: exit=`0`, duration=`5s`
- Options bot: exit=`0`, duration=`48s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T11:35:43.867818-04:00","date":"2026-07-17","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":47.3,"phases_s":{"reconcile":1.85,"cancel":0.12,"manage":4.24,"scan":40.45,"entries":0.15},"signals":199,"placed":0,"equity":122227.33,"open_positions":3,"pending_orders":0,"open_lots":19,"submitted_today":40,"filled_today":40,"unattributed_contracts":0,"top_signals":["S173:AMD","S173:AKAM","S173:ALB","S173:GOOGL","S173:GOOG","S173:AMZN","S173:AMP","S173:AME"],"github_run":"4282","github_run_id":"29592712670","status":"ok"}
```

### Live bot full output

```text
15:35:39  INFO      Mode: exits
15:35:39  INFO        Daily log -> logs/daily/2026-07-17.md
15:35:39  INFO        Daily log reconciled -> logs/daily/2026-07-17.md (3 ledger rows)
15:35:39  INFO        place_all_stops: checking 3 positions...
15:35:40  INFO        STOP already live CARR @ $67.55
15:35:40  INFO        STOP already live CMS @ $73.98
15:35:40  INFO        STOP skipped DOV: fractional (0.3763 shares) — software exit will handle it
15:35:40  INFO        [positions] 3/3 (3 valid)
15:35:40  INFO        SELL MARKET [urgent] DOV closed
15:35:42  INFO        TX logged: SELL DOV  P&L -0.61%
15:35:43  INFO        Daily log -> logs/daily/2026-07-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:35 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $485.59|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  DOV  P&L -0.6%  $-0.50                         EXIT: stop_loss (-0.6%)|
|  CMS  P&L +0.7%  $+0.65                                            HOLD|
|  CARR  P&L +1.8%  $+1.51                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  1 attempted  |  1 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                2|
|  Logged exits                                                         1|
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  DOV                                         -0.61%  (threshold -0.50%)|
|  Count                                                                1|
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Options bot full output

```text
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T11:35:43.867818-04:00 ===

[Run context]
Paper auth OK — equity $122227.33, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 199 signal(s); top: ['S173:AMD', 'S173:AKAM', 'S173:ALB', 'S173:GOOGL', 'S173:GOOG', 'S173:AMZN', 'S173:AMP', 'S173:AME']
Paper lab: $122772 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  All bucket slots blocked or closed for today's signals — skip entry loop.
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $122,227.33                             |
|  Signals this run              199                                     |
|  Orders submitted (session)    40                                      |
|  Orders filled today (ledger)  40                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             19                                      |
|  Broker option positions       3                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=383  buckets=47  win=33%                             |
|  Returns   avg=+4.1%  med=-35.3%  p10=-73.9%  p90=+86.5%               |
|  Realized  $+2,483.77                                                  |
|  Raw incl dropped  trades=492  real=$+1,146.58                         |
|  Today     trades=24  avg=-24.6%  med=-51.2%  real=$-415.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b28  c028_s165_w1_0928_ 12  75% +48.6 +77.3 +102.0 $   +306           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b99  c099_s163_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b80  c080_s173_w1_0928_ 35  74% +58.0 +62.9 +177.3 $   +403           |
|  ... 39 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b83  c083_s173_w4_1120_ 13   8% -60.9 -69.2 -87.7 $   -459       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (3)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  META260720C00670000           5    -41.9%   $   -155.00               |
|  AMD260717C00505000            9    +22.7%   $   +120.00               |
|  META260720C00667500           5    -24.2%   $    -80.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=47.3s reconcile=1.85s cancel=0.12s manage=4.24s scan=40.45s entries=0.15s
STATUS: options_morning_bot run complete (PAPER) elapsed=47.3s. run=#4282 https://github.com/28twagg-ops/TradingBot/actions/runs/29592712670
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 15 buckets closed trades, $-415.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 4.5% (22/492)
```

---

## Run 20260717T154034Z

- UTC timestamp: `20260717T154034Z`
- GitHub run: [#4283](https://github.com/28twagg-ops/TradingBot/actions/runs/29593056562)
- Run id: `29593056562`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`8s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T11:40:37.390336-04:00","date":"2026-07-17","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":6.5,"phases_s":{"reconcile":1.89,"cancel":0.08,"manage":3.88},"signals":0,"placed":0,"equity":123268.33,"open_positions":3,"pending_orders":0,"open_lots":19,"submitted_today":40,"filled_today":40,"unattributed_contracts":0,"top_signals":[],"github_run":"4283","github_run_id":"29593056562","status":"ok"}
```

### Live bot full output

```text
15:40:35  INFO      Mode: exits
15:40:36  INFO        Daily log -> logs/daily/2026-07-17.md
15:40:36  INFO        Daily log reconciled -> logs/daily/2026-07-17.md (4 ledger rows)
15:40:36  INFO        place_all_stops: checking 2 positions...
15:40:36  INFO        STOP already live CARR @ $67.55
15:40:36  INFO        STOP already live CMS @ $73.98
15:40:36  INFO        [positions] 2/2 (2 valid)
15:40:36  INFO        Daily log -> logs/daily/2026-07-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:40 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $485.49|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CMS  P&L +0.5%  $+0.47                                            HOLD|
|  CARR  P&L +2.0%  $+1.68                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                2|
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
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T11:40:37.390336-04:00 ===

[Run context]
Paper auth OK — equity $123318.33, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-17 11:40:43,708 INFO   EXIT [b83|c083_s173_w4_1120_1135_r5|S173] take_profit (+70.5%) SELL 1 AMD260717C00505000 @<= 1.01

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $123,268.33                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    40                                      |
|  Orders filled today (ledger)  40                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             19                                      |
|  Broker option positions       3                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=383  buckets=47  win=33%                             |
|  Returns   avg=+4.1%  med=-35.3%  p10=-73.9%  p90=+86.5%               |
|  Realized  $+2,483.77                                                  |
|  Raw incl dropped  trades=492  real=$+1,146.58                         |
|  Today     trades=24  avg=-24.6%  med=-51.2%  real=$-415.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b28  c028_s165_w1_0928_ 12  75% +48.6 +77.3 +102.0 $   +306           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b99  c099_s163_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b80  c080_s173_w1_0928_ 35  74% +58.0 +62.9 +177.3 $   +403           |
|  ... 39 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b83  c083_s173_w4_1120_ 13   8% -60.9 -69.2 -87.7 $   -459       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b83  S173 AMD260717C00505000 x1 take_profit (+70.5%)                  |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (3)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMD260717C00505000            9    +70.5%   $   +372.00               |
|  META260720C00670000           5    -41.9%   $   -155.00               |
|  META260720C00667500           5    -16.7%   $    -55.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=6.5s reconcile=1.89s cancel=0.08s manage=3.88s
STATUS: options_morning_bot run complete (PAPER) elapsed=6.5s. run=#4283 https://github.com/28twagg-ops/TradingBot/actions/runs/29593056562
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 15 buckets closed trades, $-415.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 4.5% (22/492)
```

---

## Run 20260717T154535Z

- UTC timestamp: `20260717T154535Z`
- GitHub run: [#4284](https://github.com/28twagg-ops/TradingBot/actions/runs/29593389560)
- Run id: `29593389560`
- Live bot: exit=`0`, duration=`4s`
- Options bot: exit=`0`, duration=`10s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T11:45:40.278440-04:00","date":"2026-07-17","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":8.5,"phases_s":{"reconcile":2.21,"cancel":0.22,"manage":5.15},"signals":0,"placed":0,"equity":123213.31,"open_positions":3,"pending_orders":0,"open_lots":18,"submitted_today":40,"filled_today":40,"unattributed_contracts":0,"top_signals":[],"github_run":"4284","github_run_id":"29593389560","status":"ok"}
```

### Live bot full output

```text
15:45:36  INFO      Mode: exits
15:45:38  INFO        Daily log -> logs/daily/2026-07-17.md
15:45:38  INFO        Daily log reconciled -> logs/daily/2026-07-17.md (4 ledger rows)
15:45:38  INFO        place_all_stops: checking 2 positions...
15:45:38  INFO        STOP already live CARR @ $67.55
15:45:38  INFO        STOP already live CMS @ $73.98
15:45:39  INFO        [positions] 2/2 (2 valid)
15:45:39  INFO        Daily log -> logs/daily/2026-07-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:45 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $485.60|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CMS  P&L +0.5%  $+0.48                                            HOLD|
|  CARR  P&L +2.1%  $+1.76                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                2|
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
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T11:45:40.278440-04:00 ===

[Run context]
Paper auth OK — equity $123213.31, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-17 11:45:47,184 INFO   EXIT [b43|c043_s173_w4_1120_1135_r3|S173] take_profit (+53.4%) SELL 1 AMD260717C00505000 @<= 0.86

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $123,213.31                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    40                                      |
|  Orders filled today (ledger)  40                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             18                                      |
|  Broker option positions       3                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=384  buckets=47  win=34%                             |
|  Returns   avg=+4.4%  med=-34.6%  p10=-73.8%  p90=+87.1%               |
|  Realized  $+2,532.77                                                  |
|  Raw incl dropped  trades=493  real=$+1,195.58                         |
|  Today     trades=25  avg=-19.8%  med=-50.9%  real=$-366.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b28  c028_s165_w1_0928_ 12  75% +48.6 +77.3 +102.0 $   +306           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b99  c099_s163_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b80  c080_s173_w1_0928_ 35  74% +58.0 +62.9 +177.3 $   +403           |
|  ... 39 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b83  c083_s173_w4_1120_ 14  14% -49.9 -68.7 -87.7 $   -410       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b43  S173 AMD260717C00505000 x1 take_profit (+53.4%)                  |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (3)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMD260717C00505000            7    +50.0%   $   +205.33               |
|  META260720C00670000           5    -41.9%   $   -155.00               |
|  META260720C00667500           5    -16.7%   $    -55.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=8.5s reconcile=2.21s cancel=0.22s manage=5.15s
STATUS: options_morning_bot run complete (PAPER) elapsed=8.5s. run=#4284 https://github.com/28twagg-ops/TradingBot/actions/runs/29593389560
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 16 buckets closed trades, $-366.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 4.5% (22/493)
```

---

## Run 20260717T155032Z

- UTC timestamp: `20260717T155032Z`
- GitHub run: [#4285](https://github.com/28twagg-ops/TradingBot/actions/runs/29593726299)
- Run id: `29593726299`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`6s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T11:50:34.873872-04:00","date":"2026-07-17","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":4.9,"phases_s":{"reconcile":1.5,"cancel":0.08,"manage":3.06},"signals":0,"placed":0,"equity":123323.29,"open_positions":3,"pending_orders":0,"open_lots":17,"submitted_today":40,"filled_today":40,"unattributed_contracts":0,"top_signals":[],"github_run":"4285","github_run_id":"29593726299","status":"ok"}
```

### Live bot full output

```text
15:50:33  INFO      Mode: exits
15:50:33  INFO        Daily log -> logs/daily/2026-07-17.md
15:50:33  INFO        Daily log reconciled -> logs/daily/2026-07-17.md (4 ledger rows)
15:50:33  INFO        place_all_stops: checking 2 positions...
15:50:33  INFO        STOP already live CARR @ $67.55
15:50:33  INFO        STOP already live CMS @ $73.98
15:50:34  INFO        [positions] 2/2 (2 valid)
15:50:34  INFO        Daily log -> logs/daily/2026-07-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:50 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $485.36|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CMS  P&L +0.3%  $+0.30                                            HOLD|
|  CARR  P&L +2.0%  $+1.72                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                2|
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
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T11:50:34.873872-04:00 ===

[Run context]
Paper auth OK — equity $123323.29, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-17 11:50:37,629 INFO   EXIT [b22|c022_s173_w3_1045_1120_r2|S173] take_profit (+60.2%) SELL 1 AMD260717C00505000 @<= 0.91

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $123,323.29                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    40                                      |
|  Orders filled today (ledger)  40                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             17                                      |
|  Broker option positions       3                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=385  buckets=47  win=34%                             |
|  Returns   avg=+4.5%  med=-33.9%  p10=-73.8%  p90=+87.0%               |
|  Realized  $+2,568.77                                                  |
|  Raw incl dropped  trades=494  real=$+1,231.58                         |
|  Today     trades=26  avg=-16.4%  med=-50.5%  real=$-330.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b28  c028_s165_w1_0928_ 12  75% +48.6 +77.3 +102.0 $   +306           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b99  c099_s163_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b80  c080_s173_w1_0928_ 35  74% +58.0 +62.9 +177.3 $   +403           |
|  ... 39 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b83  c083_s173_w4_1120_ 14  14% -49.9 -68.7 -87.7 $   -410       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b22  S173 AMD260717C00505000 x1 take_profit (+60.2%)                  |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (3)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMD260717C00505000            6    +70.5%   $   +248.00               |
|  META260720C00670000           5    -40.5%   $   -150.00               |
|  META260720C00667500           5    -18.2%   $    -60.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=4.9s reconcile=1.5s cancel=0.08s manage=3.06s
STATUS: options_morning_bot run complete (PAPER) elapsed=4.9s. run=#4285 https://github.com/28twagg-ops/TradingBot/actions/runs/29593726299
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 17 buckets closed trades, $-330.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 4.5% (22/494)
```

---

## Run 20260717T155533Z

- UTC timestamp: `20260717T155533Z`
- GitHub run: [#4286](https://github.com/28twagg-ops/TradingBot/actions/runs/29594064198)
- Run id: `29594064198`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`11s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T11:55:36.108462-04:00","date":"2026-07-17","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":10.1,"phases_s":{"reconcile":5.44,"cancel":0.19,"manage":4.0},"signals":0,"placed":0,"equity":124659.27,"open_positions":3,"pending_orders":0,"open_lots":16,"submitted_today":40,"filled_today":40,"unattributed_contracts":0,"top_signals":[],"github_run":"4286","github_run_id":"29594064198","status":"ok"}
```

### Live bot full output

```text
15:55:33  INFO      Mode: exits
15:55:34  INFO        Daily log -> logs/daily/2026-07-17.md
15:55:34  INFO        Daily log reconciled -> logs/daily/2026-07-17.md (4 ledger rows)
15:55:34  INFO        place_all_stops: checking 2 positions...
15:55:34  INFO        STOP already live CARR @ $67.55
15:55:34  INFO        STOP already live CMS @ $73.98
15:55:35  INFO        [positions] 2/2 (2 valid)
15:55:35  INFO        Daily log -> logs/daily/2026-07-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:55 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $485.37|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CMS  P&L +0.2%  $+0.20                                            HOLD|
|  CARR  P&L +2.1%  $+1.83                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                2|
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
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T11:55:36.108462-04:00 ===

[Run context]
Paper auth OK — equity $124683.27, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-17 11:55:46,019 INFO   EXIT [b43|c043_s173_w4_1120_1135_r3|S173] take_profit (+230.7%) SELL 1 AMD260717C00505000 @<= 2.01

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $124,659.27                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    40                                      |
|  Orders filled today (ledger)  40                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             16                                      |
|  Broker option positions       3                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=386  buckets=47  win=34%                             |
|  Returns   avg=+4.7%  med=-33.9%  p10=-73.8%  p90=+86.9%               |
|  Realized  $+2,601.77                                                  |
|  Raw incl dropped  trades=495  real=$+1,264.58                         |
|  Today     trades=27  avg=-14.0%  med=-50.0%  real=$-297.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b28  c028_s165_w1_0928_ 12  75% +48.6 +77.3 +102.0 $   +306           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b99  c099_s163_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b80  c080_s173_w1_0928_ 35  74% +58.0 +62.9 +177.3 $   +403           |
|  ... 39 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b83  c083_s173_w4_1120_ 14  14% -49.9 -68.7 -87.7 $   -410       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b43  S173 AMD260717C00505000 x1 take_profit (+230.7%                  |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (3)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMD260717C00505000            5   +242.6%   $   +711.67               |
|  META260720C00670000           5    -40.5%   $   -150.00               |
|  META260720C00667500           5    -18.2%   $    -60.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=10.1s reconcile=5.44s cancel=0.19s manage=4.0s
STATUS: options_morning_bot run complete (PAPER) elapsed=10.1s. run=#4286 https://github.com/28twagg-ops/TradingBot/actions/runs/29594064198
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 18 buckets closed trades, $-297.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 4.4% (22/495)
```

---

## Run 20260717T160038Z

- UTC timestamp: `20260717T160038Z`
- GitHub run: [#4287](https://github.com/28twagg-ops/TradingBot/actions/runs/29594397755)
- Run id: `29594397755`
- Live bot: exit=`0`, duration=`4s`
- Options bot: exit=`0`, duration=`18s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T12:00:43.428085-04:00","date":"2026-07-17","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":16.9,"phases_s":{"reconcile":2.06,"cancel":0.2,"manage":14.1},"signals":0,"placed":0,"equity":125586.25,"open_positions":3,"pending_orders":0,"open_lots":15,"submitted_today":40,"filled_today":40,"unattributed_contracts":0,"top_signals":[],"github_run":"4287","github_run_id":"29594397755","status":"ok"}
```

### Live bot full output

```text
16:00:40  INFO      Mode: exits
16:00:41  INFO        Daily log -> logs/daily/2026-07-17.md
16:00:41  INFO        Daily log reconciled -> logs/daily/2026-07-17.md (4 ledger rows)
16:00:41  INFO        place_all_stops: checking 2 positions...
16:00:41  INFO        STOP already live CARR @ $67.55
16:00:41  INFO        STOP already live CMS @ $73.98
16:00:42  INFO        [positions] 2/2 (2 valid)
16:00:42  INFO        Daily log -> logs/daily/2026-07-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:00 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $485.51|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CMS  P&L +0.2%  $+0.20                                            HOLD|
|  CARR  P&L +2.3%  $+1.97                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                2|
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
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T12:00:43.428085-04:00 ===

[Run context]
Paper auth OK — equity $125586.25, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-17 12:01:00,076 INFO   EXIT [b83|c083_s173_w4_1120_1135_r5|S173] take_profit (+445.5%) SELL 1 AMD260717C00505000 @<= 3.12

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $125,586.25                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    40                                      |
|  Orders filled today (ledger)  40                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             15                                      |
|  Broker option positions       3                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=387  buckets=47  win=34%                             |
|  Returns   avg=+5.4%  med=-33.9%  p10=-73.7%  p90=+87.4%               |
|  Realized  $+2,750.77                                                  |
|  Raw incl dropped  trades=496  real=$+1,413.58                         |
|  Today     trades=28  avg=-3.2%  med=-50.0%  real=$-148.00             |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b28  c028_s165_w1_0928_ 12  75% +48.6 +77.3 +102.0 $   +306           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b99  c099_s163_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b43  c043_s173_w4_1120_  5  60% +64.1 +69.2 +286.5 $   +153           |
|  ... 39 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b83  c083_s173_w4_1120_ 14  14% -49.9 -68.7 -87.7 $   -410       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b83  S173 AMD260717C00505000 x1 take_profit (+445.5%                  |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (3)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMD260717C00505000            5   +428.4%   $ +1,256.67               |
|  META260720C00670000           5    -28.4%   $   -105.00               |
|  META260720C00667500           5     -6.1%   $    -20.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=16.9s reconcile=2.06s cancel=0.2s manage=14.1s
STATUS: options_morning_bot run complete (PAPER) elapsed=16.9s. run=#4287 https://github.com/28twagg-ops/TradingBot/actions/runs/29594397755
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 18 buckets closed trades, $-148.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 4.4% (22/496)
```

---

## Run 20260717T160533Z

- UTC timestamp: `20260717T160533Z`
- GitHub run: [#4288](https://github.com/28twagg-ops/TradingBot/actions/runs/29594750052)
- Run id: `29594750052`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`6s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T12:05:35.969545-04:00","date":"2026-07-17","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":5.1,"phases_s":{"reconcile":1.84,"cancel":0.07,"manage":2.85},"signals":0,"placed":0,"equity":124695.99,"open_positions":3,"pending_orders":0,"open_lots":14,"submitted_today":40,"filled_today":40,"unattributed_contracts":0,"top_signals":[],"github_run":"4288","github_run_id":"29594750052","status":"ok"}
```

### Live bot full output

```text
16:05:34  INFO      Mode: exits
16:05:34  INFO        Daily log -> logs/daily/2026-07-17.md
16:05:34  INFO        Daily log reconciled -> logs/daily/2026-07-17.md (4 ledger rows)
16:05:34  INFO        place_all_stops: checking 2 positions...
16:05:34  INFO        STOP already live CARR @ $67.55
16:05:34  INFO        STOP already live CMS @ $73.98
16:05:35  INFO        [positions] 2/2 (2 valid)
16:05:35  INFO        Daily log -> logs/daily/2026-07-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:05 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $485.34|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CMS  P&L +0.3%  $+0.25                                            HOLD|
|  CARR  P&L +2.0%  $+1.75                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                2|
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
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T12:05:35.969545-04:00 ===

[Run context]
Paper auth OK — equity $124695.99, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-17 12:05:40,916 INFO   EXIT [b3|c003_s173_w4_1120_1135_r1|S173] take_profit (+368.8%) SELL 1 AMD260717C00505000 @<= 2.72

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $124,695.99                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    40                                      |
|  Orders filled today (ledger)  40                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             14                                      |
|  Broker option positions       3                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=388  buckets=47  win=34%                             |
|  Returns   avg=+6.7%  med=-33.9%  p10=-73.7%  p90=+88.5%               |
|  Realized  $+3,013.77                                                  |
|  Raw incl dropped  trades=497  real=$+1,676.58                         |
|  Today     trades=29  avg=+14.3%  med=-50.0%  real=$+115.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b28  c028_s165_w1_0928_ 12  75% +48.6 +77.3 +102.0 $   +306           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b99  c099_s163_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b43  c043_s173_w4_1120_  5  60% +64.1 +69.2 +286.5 $   +153           |
|  ... 39 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b83  c083_s173_w4_1120_ 15  20% -12.8 -68.2 -87.7 $   -147       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b3   S173 AMD260717C00505000 x1 take_profit (+368.8%                  |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (3)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMD260717C00505000            4   +368.8%   $   +865.33               |
|  META260720C00670000           5    -39.2%   $   -145.00               |
|  META260720C00667500           5    -25.8%   $    -85.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=5.1s reconcile=1.84s cancel=0.07s manage=2.85s
STATUS: options_morning_bot run complete (PAPER) elapsed=5.1s. run=#4288 https://github.com/28twagg-ops/TradingBot/actions/runs/29594750052
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 18 buckets closed trades, $+115.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 4.4% (22/497)
```

---

## Run 20260717T161038Z

- UTC timestamp: `20260717T161038Z`
- GitHub run: [#4289](https://github.com/28twagg-ops/TradingBot/actions/runs/29595089824)
- Run id: `29595089824`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`8s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T12:10:41.945740-04:00","date":"2026-07-17","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":7.3,"phases_s":{"reconcile":2.05,"cancel":0.19,"manage":4.45},"signals":0,"placed":0,"equity":125341.21,"open_positions":3,"pending_orders":0,"open_lots":13,"submitted_today":40,"filled_today":40,"unattributed_contracts":0,"top_signals":[],"github_run":"4289","github_run_id":"29595089824","status":"ok"}
```

### Live bot full output

```text
16:10:39  INFO      Mode: exits
16:10:40  INFO        Daily log -> logs/daily/2026-07-17.md
16:10:40  INFO        Daily log reconciled -> logs/daily/2026-07-17.md (4 ledger rows)
16:10:40  INFO        place_all_stops: checking 2 positions...
16:10:40  INFO        STOP already live CARR @ $67.55
16:10:40  INFO        STOP already live CMS @ $73.98
16:10:40  INFO        [positions] 2/2 (2 valid)
16:10:41  INFO        Daily log -> logs/daily/2026-07-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $485.14|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CMS  P&L +0.0%  $+0.02                                            HOLD|
|  CARR  P&L +2.1%  $+1.78                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                2|
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
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T12:10:41.945740-04:00 ===

[Run context]
Paper auth OK — equity $125341.21, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-17 12:10:46,525 INFO   EXIT [b3|c003_s173_w4_1120_1135_r1|S173] take_profit (+522.2%) SELL 1 AMD260717C00505000 @<= 3.60

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $125,341.21                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    40                                      |
|  Orders filled today (ledger)  40                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             13                                      |
|  Broker option positions       3                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=389  buckets=47  win=34%                             |
|  Returns   avg=+7.8%  med=-33.9%  p10=-73.6%  p90=+90.9%               |
|  Realized  $+3,236.77                                                  |
|  Raw incl dropped  trades=498  real=$+1,899.58                         |
|  Today     trades=30  avg=+28.1%  med=-50.0%  real=$+338.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b28  c028_s165_w1_0928_ 12  75% +48.6 +77.3 +102.0 $   +306           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b99  c099_s163_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b43  c043_s173_w4_1120_  5  60% +64.1 +69.2 +286.5 $   +153           |
|  ... 39 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b83  c083_s173_w4_1120_ 15  20% -12.8 -68.2 -87.7 $   -147       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b3   S173 AMD260717C00505000 x1 take_profit (+522.2%                  |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (3)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMD260717C00505000            2   +530.7%   $   +622.67               |
|  META260720C00670000           5    -25.7%   $    -95.00               |
|  META260720C00667500           5     -3.0%   $    -10.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=7.3s reconcile=2.05s cancel=0.19s manage=4.45s
STATUS: options_morning_bot run complete (PAPER) elapsed=7.3s. run=#4289 https://github.com/28twagg-ops/TradingBot/actions/runs/29595089824
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 19 buckets closed trades, $+338.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 4.4% (22/498)
```

---

## Run 20260717T161537Z

- UTC timestamp: `20260717T161537Z`
- GitHub run: [#4290](https://github.com/28twagg-ops/TradingBot/actions/runs/29595417920)
- Run id: `29595417920`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`7s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T12:15:40.824193-04:00","date":"2026-07-17","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":5.9,"phases_s":{"reconcile":2.82,"cancel":0.03,"manage":2.84},"signals":0,"placed":0,"equity":125525.19,"open_positions":3,"pending_orders":0,"open_lots":12,"submitted_today":40,"filled_today":40,"unattributed_contracts":0,"top_signals":[],"github_run":"4290","github_run_id":"29595417920","status":"ok"}
```

### Live bot full output

```text
16:15:38  INFO      Mode: exits
16:15:39  INFO        Daily log -> logs/daily/2026-07-17.md
16:15:39  INFO        Daily log reconciled -> logs/daily/2026-07-17.md (4 ledger rows)
16:15:39  INFO        place_all_stops: checking 2 positions...
16:15:39  INFO        STOP already live CARR @ $67.55
16:15:39  INFO        STOP already live CMS @ $73.98
16:15:39  INFO        [positions] 2/2 (2 valid)
16:15:40  INFO        Daily log -> logs/daily/2026-07-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:15 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $485.08|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CMS  P&L -0.0%  $-0.02                                            HOLD|
|  CARR  P&L +2.0%  $+1.76                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                2|
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
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T12:15:40.824193-04:00 ===

[Run context]
Paper auth OK — equity $125525.19, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-17 12:15:45,722 INFO   EXIT [b42|c042_s173_w3_1045_1120_r3|S173] take_profit (+488.1%) SELL 1 AMD260717C00505000 @<= 3.36

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $125,525.19                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    40                                      |
|  Orders filled today (ledger)  40                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             12                                      |
|  Broker option positions       3                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=390  buckets=47  win=35%                             |
|  Returns   avg=+9.3%  med=-33.8%  p10=-73.6%  p90=+90.9%               |
|  Realized  $+3,549.77                                                  |
|  Raw incl dropped  trades=499  real=$+2,212.58                         |
|  Today     trades=31  avg=+46.7%  med=-50.0%  real=$+651.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b28  c028_s165_w1_0928_ 12  75% +48.6 +77.3 +102.0 $   +306           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b99  c099_s163_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b43  c043_s173_w4_1120_  5  60% +64.1 +69.2 +286.5 $   +153           |
|  ... 39 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b83  c083_s173_w4_1120_ 15  20% -12.8 -68.2 -87.7 $   -147       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b42  S173 AMD260717C00505000 x1 take_profit (+488.1%                  |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (3)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMD260717C00505000            1   +505.1%   $   +296.33               |
|  META260720C00670000           5    -25.7%   $    -95.00               |
|  META260720C00667500           5     -4.5%   $    -15.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=5.9s reconcile=2.82s cancel=0.03s manage=2.84s
STATUS: options_morning_bot run complete (PAPER) elapsed=5.9s. run=#4290 https://github.com/28twagg-ops/TradingBot/actions/runs/29595417920
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 19 buckets closed trades, $+651.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 4.4% (22/499)
```

---

## Run 20260717T162037Z

- UTC timestamp: `20260717T162037Z`
- GitHub run: [#4291](https://github.com/28twagg-ops/TradingBot/actions/runs/29595745700)
- Run id: `29595745700`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`5s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T12:20:40.059523-04:00","date":"2026-07-17","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":4.3,"phases_s":{"reconcile":1.76,"cancel":0.03,"manage":2.24},"signals":0,"placed":0,"equity":127021.17,"open_positions":3,"pending_orders":0,"open_lots":11,"submitted_today":40,"filled_today":40,"unattributed_contracts":0,"top_signals":[],"github_run":"4291","github_run_id":"29595745700","status":"ok"}
```

### Live bot full output

```text
16:20:38  INFO      Mode: exits
16:20:39  INFO        Daily log -> logs/daily/2026-07-17.md
16:20:39  INFO        Daily log reconciled -> logs/daily/2026-07-17.md (4 ledger rows)
16:20:39  INFO        place_all_stops: checking 2 positions...
16:20:39  INFO        STOP already live CARR @ $67.55
16:20:39  INFO        STOP already live CMS @ $73.98
16:20:39  INFO        [positions] 2/2 (2 valid)
16:20:39  INFO        Daily log -> logs/daily/2026-07-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $484.95|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CMS  P&L -0.1%  $-0.07                                            HOLD|
|  CARR  P&L +1.9%  $+1.68                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                2|
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
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T12:20:40.059523-04:00 ===

[Run context]
Paper auth OK — equity $127021.17, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-17 12:20:42,625 INFO   EXIT [b91|c091_s165_w4_1120_1135_r5|S165] take_profit (+247.0%) SELL 1 META260720C00667500 @<= 2.23
2026-07-17 12:20:43,417 INFO   EXIT [b30|c030_s165_w3_1045_1120_r2|S165] take_profit (+167.6%) SELL 1 META260720C00670000 @<= 1.96
2026-07-17 12:20:44,145 INFO   EXIT [b2|c002_s173_w3_1045_1120_r1|S173] take_profit (+419.9%) SELL 1 AMD260717C00505000 @<= 3.02

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $127,021.17                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    40                                      |
|  Orders filled today (ledger)  40                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             11                                      |
|  Broker option positions       3                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=391  buckets=47  win=35%                             |
|  Returns   avg=+10.4%  med=-33.8%  p10=-73.5%  p90=+90.9%              |
|  Realized  $+3,837.77                                                  |
|  Raw incl dropped  trades=500  real=$+2,500.58                         |
|  Today     trades=32  avg=+58.6%  med=-47.7%  real=$+939.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b28  c028_s165_w1_0928_ 12  75% +48.6 +77.3 +102.0 $   +306           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b99  c099_s163_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b43  c043_s173_w4_1120_  5  60% +64.1 +69.2 +286.5 $   +153           |
|  ... 39 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b83  c083_s173_w4_1120_ 15  20% -12.8 -68.2 -87.7 $   -147       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (3)                                                     |
+------------------------------------------------------------------------+
|  b91  S165 META260720C00667500 x1 take_profit (+247.0%                 |
|  b30  S165 META260720C00670000 x1 take_profit (+167.6%                 |
|  b2   S173 AMD260717C00505000 x1 take_profit (+419.9%                  |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (3)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  META260720C00667500           4   +248.5%   $   +656.00               |
|  META260720C00670000           4   +170.3%   $   +504.00               |
|  AMD260717C00505000            1   +419.9%   $   +246.33               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=4.3s reconcile=1.76s cancel=0.03s manage=2.24s
STATUS: options_morning_bot run complete (PAPER) elapsed=4.3s. run=#4291 https://github.com/28twagg-ops/TradingBot/actions/runs/29595745700
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 20 buckets closed trades, $+939.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 4.4% (22/500)
```

---

## Run 20260717T162238Z

- UTC timestamp: `20260717T162238Z`
- GitHub run: [#4292](https://github.com/28twagg-ops/TradingBot/actions/runs/29595878988)
- Run id: `29595878988`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`6s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T12:22:42.412088-04:00","date":"2026-07-17","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":4.6,"phases_s":{"reconcile":1.82,"cancel":0.11,"manage":2.27},"signals":0,"placed":0,"equity":126493.11,"open_positions":2,"pending_orders":0,"open_lots":8,"submitted_today":40,"filled_today":40,"unattributed_contracts":0,"top_signals":[],"github_run":"4292","github_run_id":"29595878988","status":"ok"}
```

### Live bot full output

```text
16:22:40  INFO      Mode: exits
16:22:41  INFO        Daily log -> logs/daily/2026-07-17.md
16:22:41  INFO        Daily log reconciled -> logs/daily/2026-07-17.md (4 ledger rows)
16:22:41  INFO        place_all_stops: checking 2 positions...
16:22:41  INFO        STOP already live CARR @ $67.55
16:22:41  INFO        STOP already live CMS @ $73.98
16:22:41  INFO        [positions] 2/2 (2 valid)
16:22:41  INFO        Daily log -> logs/daily/2026-07-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:22 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $485.05|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CMS  P&L +0.1%  $+0.12                                            HOLD|
|  CARR  P&L +1.9%  $+1.59                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                2|
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
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T12:22:42.412088-04:00 ===

[Run context]
Paper auth OK — equity $126493.11, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-17 12:22:45,699 INFO   EXIT [b51|c051_s165_w4_1120_1135_r3|S165] take_profit (+260.6%) SELL 1 META260720C00667500 @<= 2.39
2026-07-17 12:22:46,763 INFO   EXIT [b70|c070_s165_w3_1045_1120_r4|S165] take_profit (+185.1%) SELL 1 META260720C00670000 @<= 2.06

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $126,493.11                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    40                                      |
|  Orders filled today (ledger)  40                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             8                                       |
|  Broker option positions       2                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=394  buckets=47  win=35%                             |
|  Returns   avg=+12.2%  med=-33.3%  p10=-73.1%  p90=+94.2%              |
|  Realized  $+4,363.77                                                  |
|  Raw incl dropped  trades=503  real=$+3,026.58                         |
|  Today     trades=35  avg=+75.6%  med=+49.2%  real=$+1,465.00          |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b91  c091_s165_w4_1120_  2  50% +115.5 +115.5 +247.0 $   +152         |
|  b28  c028_s165_w1_0928_ 12  75% +48.6 +77.3 +102.0 $   +306           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b99  c099_s163_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 39 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b83  c083_s173_w4_1120_ 15  20% -12.8 -68.2 -87.7 $   -147       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b51  S165 META260720C00667500 x1 take_profit (+260.6%                 |
|  b70  S165 META260720C00670000 x1 take_profit (+185.1%                 |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (2)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  META260720C00670000           4   +185.1%   $   +548.00               |
|  META260720C00667500           3   +263.6%   $   +522.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=4.6s reconcile=1.82s cancel=0.11s manage=2.27s
STATUS: options_morning_bot run complete (PAPER) elapsed=4.6s. run=#4292 https://github.com/28twagg-ops/TradingBot/actions/runs/29595878988
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 23 buckets closed trades, $+1,465.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 4.4% (22/503)
```

---

## Run 20260717T162535Z

- UTC timestamp: `20260717T162535Z`
- GitHub run: [#4293](https://github.com/28twagg-ops/TradingBot/actions/runs/29596072339)
- Run id: `29596072339`
- Live bot: exit=`0`, duration=`4s`
- Options bot: exit=`0`, duration=`8s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T12:25:40.134332-04:00","date":"2026-07-17","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":6.4,"phases_s":{"reconcile":2.9,"cancel":0.18,"manage":2.88},"signals":0,"placed":0,"equity":126518.19,"open_positions":2,"pending_orders":0,"open_lots":6,"submitted_today":40,"filled_today":40,"unattributed_contracts":0,"top_signals":[],"github_run":"4293","github_run_id":"29596072339","status":"ok"}
```

### Live bot full output

```text
16:25:37  INFO      Mode: exits
16:25:38  INFO        Daily log -> logs/daily/2026-07-17.md
16:25:38  INFO        Daily log reconciled -> logs/daily/2026-07-17.md (4 ledger rows)
16:25:38  INFO        place_all_stops: checking 2 positions...
16:25:38  INFO        STOP already live CARR @ $67.55
16:25:38  INFO        STOP already live CMS @ $73.98
16:25:39  INFO        [positions] 2/2 (2 valid)
16:25:39  INFO        Daily log -> logs/daily/2026-07-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:25 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $484.84|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CMS  P&L +0.0%  $+0.04                                            HOLD|
|  CARR  P&L +1.7%  $+1.47                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                2|
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
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T12:25:40.134332-04:00 ===

[Run context]
Paper auth OK — equity $126509.19, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-17 12:25:45,150 INFO   EXIT [b30|c030_s165_w3_1045_1120_r2|S165] take_profit (+131.1%) SELL 1 META260720C00670000 @<= 1.68
2026-07-17 12:25:46,348 INFO   EXIT [b91|c091_s165_w4_1120_1135_r5|S165] take_profit (+197.0%) SELL 1 META260720C00667500 @<= 1.93

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $126,518.19                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    40                                      |
|  Orders filled today (ledger)  40                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             6                                       |
|  Broker option positions       2                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=396  buckets=48  win=36%                             |
|  Returns   avg=+13.3%  med=-32.4%  p10=-72.8%  p90=+96.4%              |
|  Realized  $+4,674.77                                                  |
|  Raw incl dropped  trades=505  real=$+3,337.58                         |
|  Today     trades=37  avg=+83.7%  med=+56.9%  real=$+1,776.00          |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b51  c051_s165_w4_1120_  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  c091_s165_w4_1120_  2  50% +115.5 +115.5 +247.0 $   +152         |
|  b28  c028_s165_w1_0928_ 12  75% +48.6 +77.3 +102.0 $   +306           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 40 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b83  c083_s173_w4_1120_ 15  20% -12.8 -68.2 -87.7 $   -147       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b30  S165 META260720C00670000 x1 take_profit (+131.1%                 |
|  b91  S165 META260720C00667500 x1 take_profit (+197.0%                 |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (2)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  META260720C00667500           2   +197.0%   $   +260.00               |
|  META260720C00670000           2   +131.1%   $   +194.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=6.4s reconcile=2.9s cancel=0.18s manage=2.88s
STATUS: options_morning_bot run complete (PAPER) elapsed=6.4s. run=#4293 https://github.com/28twagg-ops/TradingBot/actions/runs/29596072339
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 25 buckets closed trades, $+1,776.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 4.4% (22/505)
```

---

## Run 20260717T163045Z

- UTC timestamp: `20260717T163045Z`
- GitHub run: [#4294](https://github.com/28twagg-ops/TradingBot/actions/runs/29596398397)
- Run id: `29596398397`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`8s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T12:30:48.815985-04:00","date":"2026-07-17","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":5.4,"phases_s":{"reconcile":1.85,"cancel":0.02,"manage":3.28},"signals":0,"placed":0,"equity":126523.03,"open_positions":2,"pending_orders":0,"open_lots":4,"submitted_today":40,"filled_today":40,"unattributed_contracts":0,"top_signals":[],"github_run":"4294","github_run_id":"29596398397","status":"ok"}
```

### Live bot full output

```text
16:30:46  INFO      Mode: exits
16:30:47  INFO        Daily log -> logs/daily/2026-07-17.md
16:30:47  INFO        Daily log reconciled -> logs/daily/2026-07-17.md (4 ledger rows)
16:30:47  INFO        place_all_stops: checking 2 positions...
16:30:47  INFO        STOP already live CARR @ $67.55
16:30:47  INFO        STOP already live CMS @ $73.98
16:30:47  INFO        [positions] 2/2 (2 valid)
16:30:47  INFO        Daily log -> logs/daily/2026-07-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:30 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $484.79|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CMS  P&L -0.1%  $-0.08                                            HOLD|
|  CARR  P&L +1.8%  $+1.53                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                2|
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
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T12:30:48.815985-04:00 ===

[Run context]
Paper auth OK — equity $126523.03, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-17 12:30:52,365 INFO   EXIT [b30|c030_s165_w3_1045_1120_r2|S165] take_profit (+83.8%) SELL 1 META260720C00670000 @<= 1.33
2026-07-17 12:30:54,058 INFO   EXIT [b31|c031_s165_w4_1120_1135_r2|S165] take_profit (+113.6%) SELL 1 META260720C00667500 @<= 1.42

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $126,523.03                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    40                                      |
|  Orders filled today (ledger)  40                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             4                                       |
|  Broker option positions       2                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=398  buckets=48  win=36%                             |
|  Returns   avg=+14.1%  med=-31.5%  p10=-72.5%  p90=+100.0%             |
|  Realized  $+4,901.77                                                  |
|  Raw incl dropped  trades=507  real=$+3,564.58                         |
|  Today     trades=39  avg=+87.8%  med=+58.8%  real=$+2,003.00          |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b51  c051_s165_w4_1120_  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  c091_s165_w4_1120_  3  67% +142.7 +197.0 +247.0 $   +282         |
|  b28  c028_s165_w1_0928_ 12  75% +48.6 +77.3 +102.0 $   +306           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 40 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b83  c083_s173_w4_1120_ 15  20% -12.8 -68.2 -87.7 $   -147       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b30  S165 META260720C00670000 x1 take_profit (+83.8%)                 |
|  b31  S165 META260720C00667500 x1 take_profit (+113.6%                 |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (2)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  META260720C00667500           2   +113.6%   $   +150.00               |
|  META260720C00670000           1    +89.2%   $    +66.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=5.4s reconcile=1.85s cancel=0.02s manage=3.28s
STATUS: options_morning_bot run complete (PAPER) elapsed=5.4s. run=#4294 https://github.com/28twagg-ops/TradingBot/actions/runs/29596398397
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 25 buckets closed trades, $+2,003.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 4.3% (22/507)
```

---

## Run 20260717T163534Z

- UTC timestamp: `20260717T163534Z`
- GitHub run: [#4295](https://github.com/28twagg-ops/TradingBot/actions/runs/29596726526)
- Run id: `29596726526`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`7s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T12:35:36.815306-04:00","date":"2026-07-17","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":5.7,"phases_s":{"reconcile":2.52,"cancel":0.03,"manage":2.87},"signals":0,"placed":0,"equity":126973.95,"open_positions":1,"pending_orders":0,"open_lots":2,"submitted_today":40,"filled_today":50,"unattributed_contracts":0,"top_signals":[],"github_run":"4295","github_run_id":"29596726526","status":"ok"}
```

### Live bot full output

```text
16:35:35  INFO      Mode: exits
16:35:35  INFO        Daily log -> logs/daily/2026-07-17.md
16:35:35  INFO        Daily log reconciled -> logs/daily/2026-07-17.md (4 ledger rows)
16:35:35  INFO        place_all_stops: checking 2 positions...
16:35:35  INFO        STOP already live CARR @ $67.55
16:35:35  INFO        STOP already live CMS @ $73.98
16:35:35  INFO        [positions] 2/2 (2 valid)
16:35:36  INFO        Daily log -> logs/daily/2026-07-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:35 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $484.69|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CMS  P&L -0.1%  $-0.11                                            HOLD|
|  CARR  P&L +1.7%  $+1.46                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                2|
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
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T12:35:36.815306-04:00 ===

[Run context]
Paper auth OK — equity $126973.95, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-17 12:35:40,923 INFO   EXIT [b90|c090_s165_w3_1045_1120_r5|S165] take_profit (+109.5%) SELL 1 META260720C00670000 @<= 1.56
2026-07-17 12:35:42,315 INFO   EXIT [b31|c031_s165_w4_1120_1135_r2|S165] take_profit (+172.7%) SELL 1 META260720C00667500 @<= 1.82

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $126,973.95                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    40                                      |
|  Orders filled today (ledger)  50                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             2                                       |
|  Broker option positions       1                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=447  buckets=49  win=34%                             |
|  Returns   avg=+8.9%  med=-33.8%  p10=-77.0%  p90=+94.2%               |
|  Realized  $+3,922.77                                                  |
|  Raw incl dropped  trades=556  real=$+2,585.58                         |
|  Today     trades=43  avg=+80.0%  med=+58.8%  real=$+2,048.00          |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b51  c051_s165_w4_1120_  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  c091_s165_w4_1120_  3  67% +142.7 +197.0 +247.0 $   +282         |
|  b31  c031_s165_w4_1120_  1 100% +115.2 +115.2 +115.2 $    +76         |
|  b28  c028_s165_w1_0928_ 14  71% +43.7 +77.3 +102.0 $   +322           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 41 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b9   c009_s165_w2_1005_  4   0% -74.7 -78.1 -92.7 $   -158       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b90  S165 META260720C00670000 x1 take_profit (+109.5%                 |
|  b31  S165 META260720C00667500 x1 take_profit (+172.7%                 |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (1)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  META260720C00667500           1   +175.8%   $   +116.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=5.7s reconcile=2.52s cancel=0.03s manage=2.87s
STATUS: options_morning_bot run complete (PAPER) elapsed=5.7s. run=#4295 https://github.com/28twagg-ops/TradingBot/actions/runs/29596726526
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 26 buckets closed trades, $+2,048.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 4.0% (22/556)
```

---

## Run 20260717T164037Z

- UTC timestamp: `20260717T164037Z`
- GitHub run: [#4296](https://github.com/28twagg-ops/TradingBot/actions/runs/29597052584)
- Run id: `29597052584`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`4s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T12:40:40.668207-04:00","date":"2026-07-17","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":2.5,"phases_s":{"reconcile":1.9,"cancel":0.14,"manage":0.1},"signals":0,"placed":0,"equity":126834.95,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":40,"filled_today":50,"unattributed_contracts":0,"top_signals":[],"github_run":"4296","github_run_id":"29597052584","status":"ok"}
```

### Live bot full output

```text
16:40:38  INFO      Mode: exits
16:40:39  INFO        Daily log -> logs/daily/2026-07-17.md
16:40:39  INFO        Daily log reconciled -> logs/daily/2026-07-17.md (4 ledger rows)
16:40:39  INFO        place_all_stops: checking 2 positions...
16:40:39  INFO        STOP already live CARR @ $67.55
16:40:39  INFO        STOP already live CMS @ $73.98
16:40:39  INFO        [positions] 2/2 (2 valid)
16:40:39  INFO        Daily log -> logs/daily/2026-07-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:40 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $484.65|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CMS  P&L -0.1%  $-0.10                                            HOLD|
|  CARR  P&L +1.6%  $+1.40                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                2|
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
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T12:40:40.668207-04:00 ===

[Run context]
Paper auth OK — equity $126834.95, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $126,834.95                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    40                                      |
|  Orders filled today (ledger)  50                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=482  buckets=49  win=34%                             |
|  Returns   avg=+7.7%  med=-33.8%  p10=-77.0%  p90=+94.2%               |
|  Realized  $+3,660.77                                                  |
|  Raw incl dropped  trades=593  real=$+2,268.58                         |
|  Today     trades=46  avg=+78.9%  med=+61.2%  real=$+2,200.00          |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b51  c051_s165_w4_1120_  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  c091_s165_w4_1120_  3  67% +142.7 +197.0 +247.0 $   +282         |
|  b31  c031_s165_w4_1120_  2 100% +145.5 +145.5 +175.8 $   +192         |
|  b28  c028_s165_w1_0928_ 16  75% +48.7 +80.0 +102.0 $   +414           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 41 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b9   c009_s165_w2_1005_  4   0% -74.7 -78.1 -92.7 $   -158       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=2.5s reconcile=1.9s cancel=0.14s manage=0.1s
STATUS: options_morning_bot run complete (PAPER) elapsed=2.5s. run=#4296 https://github.com/28twagg-ops/TradingBot/actions/runs/29597052584
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 27 buckets closed trades, $+2,200.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 3.7% (22/593)
```

---

## Run 20260717T164534Z

- UTC timestamp: `20260717T164534Z`
- GitHub run: [#4297](https://github.com/28twagg-ops/TradingBot/actions/runs/29597380463)
- Run id: `29597380463`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`5s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T12:45:37.954919-04:00","date":"2026-07-17","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":3.3,"phases_s":{"reconcile":2.34,"cancel":0.23,"manage":0.17},"signals":0,"placed":0,"equity":127384.95,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":40,"filled_today":50,"unattributed_contracts":0,"top_signals":[],"github_run":"4297","github_run_id":"29597380463","status":"ok"}
```

### Live bot full output

```text
16:45:34  INFO      Mode: exits
16:45:35  INFO        Daily log -> logs/daily/2026-07-17.md
16:45:35  INFO        Daily log reconciled -> logs/daily/2026-07-17.md (4 ledger rows)
16:45:35  INFO        place_all_stops: checking 2 positions...
16:45:36  INFO        STOP already live CARR @ $67.55
16:45:36  INFO        STOP already live CMS @ $73.98
16:45:36  INFO        [positions] 2/2 (2 valid)
16:45:37  INFO        Daily log -> logs/daily/2026-07-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:45 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $484.70|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CMS  P&L -0.2%  $-0.22                                            HOLD|
|  CARR  P&L +1.8%  $+1.58                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                2|
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
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T12:45:37.954919-04:00 ===

[Run context]
Paper auth OK — equity $127384.95, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $127,384.95                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    40                                      |
|  Orders filled today (ledger)  50                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=486  buckets=49  win=34%                             |
|  Returns   avg=+7.9%  med=-33.6%  p10=-77.0%  p90=+94.2%               |
|  Realized  $+3,691.77                                                  |
|  Raw incl dropped  trades=599  real=$+2,247.58                         |
|  Today     trades=46  avg=+78.9%  med=+61.2%  real=$+2,200.00          |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b51  c051_s165_w4_1120_  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  c091_s165_w4_1120_  3  67% +142.7 +197.0 +247.0 $   +282         |
|  b31  c031_s165_w4_1120_  2 100% +145.5 +145.5 +175.8 $   +192         |
|  b28  c028_s165_w1_0928_ 17  76% +49.5 +80.0 +102.0 $   +448           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 41 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b9   c009_s165_w2_1005_  4   0% -74.7 -78.1 -92.7 $   -158       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=3.3s reconcile=2.34s cancel=0.23s manage=0.17s
STATUS: options_morning_bot run complete (PAPER) elapsed=3.3s. run=#4297 https://github.com/28twagg-ops/TradingBot/actions/runs/29597380463
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 27 buckets closed trades, $+2,200.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 3.7% (22/599)
```

---

## Run 20260717T165035Z

- UTC timestamp: `20260717T165035Z`
- GitHub run: [#4298](https://github.com/28twagg-ops/TradingBot/actions/runs/29597704470)
- Run id: `29597704470`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`4s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T12:50:37.047746-04:00","date":"2026-07-17","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":2.9,"phases_s":{"reconcile":2.65,"cancel":0.03,"manage":0.02},"signals":0,"placed":0,"equity":127568.43,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":40,"filled_today":60,"unattributed_contracts":0,"top_signals":[],"github_run":"4298","github_run_id":"29597704470","status":"ok"}
```

### Live bot full output

```text
16:50:35  INFO      Mode: exits
16:50:36  INFO        Daily log -> logs/daily/2026-07-17.md
16:50:36  INFO        Daily log reconciled -> logs/daily/2026-07-17.md (4 ledger rows)
16:50:36  INFO        place_all_stops: checking 2 positions...
16:50:36  INFO        STOP already live CARR @ $67.55
16:50:36  INFO        STOP already live CMS @ $73.98
16:50:36  INFO        [positions] 2/2 (2 valid)
16:50:36  INFO        Daily log -> logs/daily/2026-07-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:50 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $484.68|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CMS  P&L -0.3%  $-0.31                                            HOLD|
|  CARR  P&L +1.9%  $+1.65                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                2|
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
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T12:50:37.047746-04:00 ===

[Run context]
Paper auth OK — equity $127568.43, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $127,568.43                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    40                                      |
|  Orders filled today (ledger)  60                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=490  buckets=49  win=34%                             |
|  Returns   avg=+7.4%  med=-33.9%  p10=-77.0%  p90=+94.1%               |
|  Realized  $+3,553.77                                                  |
|  Raw incl dropped  trades=604  real=$+2,055.58                         |
|  Today     trades=46  avg=+78.9%  med=+61.2%  real=$+2,200.00          |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b51  c051_s165_w4_1120_  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  c091_s165_w4_1120_  3  67% +142.7 +197.0 +247.0 $   +282         |
|  b31  c031_s165_w4_1120_  2 100% +145.5 +145.5 +175.8 $   +192         |
|  b28  c028_s165_w1_0928_ 17  76% +49.5 +80.0 +102.0 $   +448           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 41 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 22   0% -64.0 -72.1 -98.5 $   -942       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=2.9s reconcile=2.65s cancel=0.03s manage=0.02s
STATUS: options_morning_bot run complete (PAPER) elapsed=2.9s. run=#4298 https://github.com/28twagg-ops/TradingBot/actions/runs/29597704470
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 27 buckets closed trades, $+2,200.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 3.6% (22/604)
```

---

## Run 20260717T165537Z

- UTC timestamp: `20260717T165537Z`
- GitHub run: [#4299](https://github.com/28twagg-ops/TradingBot/actions/runs/29598026907)
- Run id: `29598026907`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`4s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T12:55:39.580443-04:00","date":"2026-07-17","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":2.0,"phases_s":{"reconcile":1.64,"cancel":0.04,"manage":0.02},"signals":0,"placed":0,"equity":127886.95,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":40,"filled_today":60,"unattributed_contracts":0,"top_signals":[],"github_run":"4299","github_run_id":"29598026907","status":"ok"}
```

### Live bot full output

```text
16:55:38  INFO      Mode: exits
16:55:38  INFO        Daily log -> logs/daily/2026-07-17.md
16:55:38  INFO        Daily log reconciled -> logs/daily/2026-07-17.md (4 ledger rows)
16:55:38  INFO        place_all_stops: checking 2 positions...
16:55:38  INFO        STOP already live CARR @ $67.55
16:55:38  INFO        STOP already live CMS @ $73.98
16:55:38  INFO        [positions] 2/2 (2 valid)
16:55:38  INFO        Daily log -> logs/daily/2026-07-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:55 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $484.46|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CMS  P&L -0.4%  $-0.39                                            HOLD|
|  CARR  P&L +1.8%  $+1.51                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                2|
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
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T12:55:39.580443-04:00 ===

[Run context]
Paper auth OK — equity $127886.95, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $127,886.95                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    40                                      |
|  Orders filled today (ledger)  60                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=490  buckets=49  win=34%                             |
|  Returns   avg=+7.4%  med=-33.9%  p10=-77.0%  p90=+94.1%               |
|  Realized  $+3,553.77                                                  |
|  Raw incl dropped  trades=604  real=$+2,055.58                         |
|  Today     trades=46  avg=+78.9%  med=+61.2%  real=$+2,200.00          |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b51  c051_s165_w4_1120_  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  c091_s165_w4_1120_  3  67% +142.7 +197.0 +247.0 $   +282         |
|  b31  c031_s165_w4_1120_  2 100% +145.5 +145.5 +175.8 $   +192         |
|  b28  c028_s165_w1_0928_ 17  76% +49.5 +80.0 +102.0 $   +448           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 41 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 22   0% -64.0 -72.1 -98.5 $   -942       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=2.0s reconcile=1.64s cancel=0.04s manage=0.02s
STATUS: options_morning_bot run complete (PAPER) elapsed=2.0s. run=#4299 https://github.com/28twagg-ops/TradingBot/actions/runs/29598026907
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 27 buckets closed trades, $+2,200.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 3.6% (22/604)
```

---

## Run 20260717T170039Z

- UTC timestamp: `20260717T170039Z`
- GitHub run: [#4300](https://github.com/28twagg-ops/TradingBot/actions/runs/29598346813)
- Run id: `29598346813`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`4s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T13:00:43.084202-04:00","date":"2026-07-17","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":2.4,"phases_s":{"reconcile":1.8,"cancel":0.13,"manage":0.08},"signals":0,"placed":0,"equity":127928.95,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":40,"filled_today":60,"unattributed_contracts":0,"top_signals":[],"github_run":"4300","github_run_id":"29598346813","status":"ok"}
```

### Live bot full output

```text
17:00:40  INFO      Mode: exits
17:00:41  INFO        Daily log -> logs/daily/2026-07-17.md
17:00:41  INFO        Daily log reconciled -> logs/daily/2026-07-17.md (4 ledger rows)
17:00:41  INFO        place_all_stops: checking 2 positions...
17:00:41  INFO        STOP already live CARR @ $67.55
17:00:41  INFO        STOP already live CMS @ $73.98
17:00:42  INFO        [positions] 2/2 (2 valid)
17:00:42  INFO        Daily log -> logs/daily/2026-07-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:00 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $484.48|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CMS  P&L -0.4%  $-0.41                                            HOLD|
|  CARR  P&L +1.8%  $+1.55                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                2|
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
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T13:00:43.084202-04:00 ===

[Run context]
Paper auth OK — equity $127928.95, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $127,928.95                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    40                                      |
|  Orders filled today (ledger)  60                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=490  buckets=49  win=34%                             |
|  Returns   avg=+7.4%  med=-33.9%  p10=-77.0%  p90=+94.1%               |
|  Realized  $+3,553.77                                                  |
|  Raw incl dropped  trades=604  real=$+2,055.58                         |
|  Today     trades=46  avg=+78.9%  med=+61.2%  real=$+2,200.00          |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b51  c051_s165_w4_1120_  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  c091_s165_w4_1120_  3  67% +142.7 +197.0 +247.0 $   +282         |
|  b31  c031_s165_w4_1120_  2 100% +145.5 +145.5 +175.8 $   +192         |
|  b28  c028_s165_w1_0928_ 17  76% +49.5 +80.0 +102.0 $   +448           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 41 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 22   0% -64.0 -72.1 -98.5 $   -942       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=2.4s reconcile=1.8s cancel=0.13s manage=0.08s
STATUS: options_morning_bot run complete (PAPER) elapsed=2.4s. run=#4300 https://github.com/28twagg-ops/TradingBot/actions/runs/29598346813
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 27 buckets closed trades, $+2,200.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 3.6% (22/604)
```

---

## Run 20260717T170537Z

- UTC timestamp: `20260717T170537Z`
- GitHub run: [#4301](https://github.com/28twagg-ops/TradingBot/actions/runs/29598674860)
- Run id: `29598674860`
- Live bot: exit=`0`, duration=`4s`
- Options bot: exit=`0`, duration=`3s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T13:05:42.308519-04:00","date":"2026-07-17","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":1.9,"phases_s":{"reconcile":1.62,"cancel":0.03,"manage":0.03},"signals":0,"placed":0,"equity":128176.95,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":40,"filled_today":60,"unattributed_contracts":0,"top_signals":[],"github_run":"4301","github_run_id":"29598674860","status":"ok"}
```

### Live bot full output

```text
17:05:38  INFO      Mode: exits
17:05:39  INFO        Daily log -> logs/daily/2026-07-17.md
17:05:39  INFO        Daily log reconciled -> logs/daily/2026-07-17.md (4 ledger rows)
17:05:39  INFO        place_all_stops: checking 2 positions...
17:05:39  INFO        STOP already live CARR @ $67.55
17:05:39  INFO        STOP skipped CMS: fractional (0.3017 shares) — software exit will handle it
17:05:39  INFO        [positions] 2/2 (2 valid)
17:05:39  INFO        SELL MARKET [urgent] CMS closed
17:05:41  INFO        TX logged: SELL CMS  P&L -0.64%
17:05:41  INFO        Daily log -> logs/daily/2026-07-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:05 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $484.41|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CMS  P&L -0.6%  $-0.14                         EXIT: stop_loss (-0.6%)|
|  CARR  P&L +1.9%  $+1.61                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  1 attempted  |  1 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
|  Logged exits                                                         1|
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  CMS                                         -0.64%  (threshold -0.50%)|
|  Count                                                                1|
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Options bot full output

```text
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T13:05:42.308519-04:00 ===

[Run context]
Paper auth OK — equity $128176.95, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $128,176.95                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    40                                      |
|  Orders filled today (ledger)  60                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=490  buckets=49  win=34%                             |
|  Returns   avg=+7.4%  med=-33.9%  p10=-77.0%  p90=+94.1%               |
|  Realized  $+3,553.77                                                  |
|  Raw incl dropped  trades=604  real=$+2,055.58                         |
|  Today     trades=46  avg=+78.9%  med=+61.2%  real=$+2,200.00          |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b51  c051_s165_w4_1120_  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  c091_s165_w4_1120_  3  67% +142.7 +197.0 +247.0 $   +282         |
|  b31  c031_s165_w4_1120_  2 100% +145.5 +145.5 +175.8 $   +192         |
|  b28  c028_s165_w1_0928_ 17  76% +49.5 +80.0 +102.0 $   +448           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 41 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 22   0% -64.0 -72.1 -98.5 $   -942       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=1.9s reconcile=1.62s cancel=0.03s manage=0.03s
STATUS: options_morning_bot run complete (PAPER) elapsed=1.9s. run=#4301 https://github.com/28twagg-ops/TradingBot/actions/runs/29598674860
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 27 buckets closed trades, $+2,200.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 3.6% (22/604)
```

---

## Run 20260717T171041Z

- UTC timestamp: `20260717T171041Z`
- GitHub run: [#4302](https://github.com/28twagg-ops/TradingBot/actions/runs/29598987899)
- Run id: `29598987899`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`4s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T13:10:45.100954-04:00","date":"2026-07-17","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":3.0,"phases_s":{"reconcile":2.01,"cancel":0.23,"manage":0.16},"signals":0,"placed":0,"equity":128358.67,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":40,"filled_today":60,"unattributed_contracts":0,"top_signals":[],"github_run":"4302","github_run_id":"29598987899","status":"ok"}
```

### Live bot full output

```text
17:10:42  INFO      Mode: exits
17:10:43  INFO        Daily log -> logs/daily/2026-07-17.md
17:10:43  INFO        Daily log reconciled -> logs/daily/2026-07-17.md (5 ledger rows)
17:10:43  INFO        place_all_stops: checking 1 positions...
17:10:43  INFO        STOP already live CARR @ $67.55
17:10:43  INFO        [positions] 1/1 (1 valid)
17:10:43  INFO        Daily log -> logs/daily/2026-07-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $484.57|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CARR  P&L +2.0%  $+1.76                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T13:10:45.100954-04:00 ===

[Run context]
Paper auth OK — equity $128356.95, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $128,358.67                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    40                                      |
|  Orders filled today (ledger)  60                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=490  buckets=49  win=34%                             |
|  Returns   avg=+7.4%  med=-33.9%  p10=-77.0%  p90=+94.1%               |
|  Realized  $+3,553.77                                                  |
|  Raw incl dropped  trades=604  real=$+2,055.58                         |
|  Today     trades=46  avg=+78.9%  med=+61.2%  real=$+2,200.00          |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b51  c051_s165_w4_1120_  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  c091_s165_w4_1120_  3  67% +142.7 +197.0 +247.0 $   +282         |
|  b31  c031_s165_w4_1120_  2 100% +145.5 +145.5 +175.8 $   +192         |
|  b28  c028_s165_w1_0928_ 17  76% +49.5 +80.0 +102.0 $   +448           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 41 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 22   0% -64.0 -72.1 -98.5 $   -942       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=3.0s reconcile=2.01s cancel=0.23s manage=0.16s
STATUS: options_morning_bot run complete (PAPER) elapsed=3.0s. run=#4302 https://github.com/28twagg-ops/TradingBot/actions/runs/29598987899
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 27 buckets closed trades, $+2,200.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 3.6% (22/604)
```

---

## Run 20260717T171647Z

- UTC timestamp: `20260717T171647Z`
- GitHub run: [#4303](https://github.com/28twagg-ops/TradingBot/actions/runs/29599309187)
- Run id: `29599309187`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`4s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T13:16:50.916217-04:00","date":"2026-07-17","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":2.7,"phases_s":{"reconcile":1.9,"cancel":0.18,"manage":0.15},"signals":0,"placed":0,"equity":128148.95,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":40,"filled_today":60,"unattributed_contracts":0,"top_signals":[],"github_run":"4303","github_run_id":"29599309187","status":"ok"}
```

### Live bot full output

```text
17:16:48  INFO      Mode: exits
17:16:49  INFO        Daily log -> logs/daily/2026-07-17.md
17:16:49  INFO        Daily log reconciled -> logs/daily/2026-07-17.md (5 ledger rows)
17:16:49  INFO        place_all_stops: checking 1 positions...
17:16:49  INFO        STOP already live CARR @ $67.55
17:16:49  INFO        [positions] 1/1 (1 valid)
17:16:50  INFO        Daily log -> logs/daily/2026-07-17.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $484.53|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CARR  P&L +2.0%  $+1.72                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T13:16:50.916217-04:00 ===

[Run context]
Paper auth OK — equity $128148.95, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $128,148.95                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    40                                      |
|  Orders filled today (ledger)  60                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=490  buckets=49  win=34%                             |
|  Returns   avg=+7.4%  med=-33.9%  p10=-77.0%  p90=+94.1%               |
|  Realized  $+3,553.77                                                  |
|  Raw incl dropped  trades=604  real=$+2,055.58                         |
|  Today     trades=46  avg=+78.9%  med=+61.2%  real=$+2,200.00          |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b51  c051_s165_w4_1120_  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  c091_s165_w4_1120_  3  67% +142.7 +197.0 +247.0 $   +282         |
|  b31  c031_s165_w4_1120_  2 100% +145.5 +145.5 +175.8 $   +192         |
|  b28  c028_s165_w1_0928_ 17  76% +49.5 +80.0 +102.0 $   +448           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 41 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 22   0% -64.0 -72.1 -98.5 $   -942       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-17.log
elapsed=2.7s reconcile=1.9s cancel=0.18s manage=0.15s
STATUS: options_morning_bot run complete (PAPER) elapsed=2.7s. run=#4303 https://github.com/28twagg-ops/TradingBot/actions/runs/29599309187
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 27 buckets closed trades, $+2,200.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 3.6% (22/604)
```

---
