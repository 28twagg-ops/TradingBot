# Daily Comprehensive Action Review — 2026-07-16

_Auto-generated from GitHub Actions run output. This document appends every run for the day._

## Run 20260716T012002Z

- UTC timestamp: `20260716T012002Z`
- GitHub run: [#4101](https://github.com/28twagg-ops/TradingBot/actions/runs/29463829648)
- Run id: `29463829648`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`5s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-15T21:20:05.859352-04:00","date":"2026-07-15","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":3.8,"phases_s":{"reconcile":3.4},"signals":0,"placed":0,"equity":132394.68,"open_positions":3,"pending_orders":0,"open_lots":14,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4101","github_run_id":"29463829648","status":"ok"}
```

### Live bot full output

```text
01:20:03  INFO      Mode: summary
01:20:04  INFO        Daily log -> logs/daily/2026-07-16.md
01:20:04  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         01:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $481.08|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $481.08|
|  Cash                                                           $196.11|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $284.97|
|  Open P&L                                                        $+4.08|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (3 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CHH      Pullback50      $96.23     $108.43  $109.10  +0.6%   $+0.59  |
|  EVR      Pullback50      $97.48     $346.97  $353.65  +1.9%   $+1.84  |
|  HST      Pullback50      $91.26     $23.37   $23.80   +1.8%   $+1.65  |
|                                                                        |
|  Total invested                                                 $284.97|
|  Total open P&L                                                  $+4.08|
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
|  2026-07-14  SELL  PLD  Pullback50  $95.64  P&L $+0.01                 |
|  2026-07-14  SELL  NEE  Pullback50  $89.54  P&L $-0.09                 |
|  2026-07-14  SELL  KMI  Pullback50  $89.48  P&L $-0.10                 |
|  2026-07-14  SELL  NI  Pullback50  $44.05  P&L $-0.23                  |
|  2026-07-14  SELL  HON  Pullback50  $95.44  P&L $-0.58                 |
|  2026-07-14  SELL  NDSN  Pullback50  $90.78  P&L $-0.53                |
+========================================================================+
```

### Options bot full output

```text
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-15T21:20:05.859352-04:00 ===

[Run context]
After hours (21:20 ET) — exit summary only.
Paper auth OK — equity $132394.68, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $132,394.68                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             14                                      |
|  Broker option positions       3                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=176  buckets=43  win=46%                             |
|  Returns   avg=+30.7%  med=-2.7%  p10=-77.0%  p90=+98.3%               |
|  Realized  $+6,235.77                                                  |
|  Raw incl dropped  trades=273  real=$+5,326.58                         |
|  Today     trades=4  avg=-64.7%  med=-72.7%  real=$-105.00             |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b62  c062_s173_w3_1045_  5  60% +628.8 +1100.0 +1100.0 $   +116       |
|  b89  c089_s165_w2_1005_  2 100% +425.9 +425.9 +790.0 $   +113         |
|  b28  c028_s165_w1_0928_  4 100% +91.7 +95.1 +102.0 $   +187           |
|  b69  c069_s165_w2_1005_  2  50% +83.2 +83.2 +210.0 $     -3           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 35 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_  7   0% -54.4 -74.0 -77.0 $   -243       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (3)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  ADBE260717C00240000           9    -68.2%   $   -270.00               |
|  C260717C00148000              2    -98.5%   $   -127.33               |
|  BSX260717C00045500            3    -50.0%   $    -15.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-15.log
elapsed=3.8s reconcile=3.4s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=3.8s. run=#4101 https://github.com/28twagg-ops/TradingBot/actions/runs/29463829648
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-15_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-15_buckets.csv
Summary: 4 buckets closed trades, $-105.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-15_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-15_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
```

---

## Run 20260716T014836Z

- UTC timestamp: `20260716T014836Z`
- GitHub run: [#4102](https://github.com/28twagg-ops/TradingBot/actions/runs/29465021606)
- Run id: `29465021606`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`4s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-15T21:48:39.213795-04:00","date":"2026-07-15","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":2.9,"phases_s":{"reconcile":2.76},"signals":0,"placed":0,"equity":132362.68,"open_positions":3,"pending_orders":0,"open_lots":14,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4102","github_run_id":"29465021606","status":"ok"}
```

### Live bot full output

```text
01:48:38  INFO      Mode: summary
01:48:38  INFO        Daily log -> logs/daily/2026-07-16.md
01:48:38  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         01:48 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $481.08|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $481.08|
|  Cash                                                           $196.11|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $284.97|
|  Open P&L                                                        $+4.08|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (3 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CHH      Pullback50      $96.23     $108.43  $109.10  +0.6%   $+0.59  |
|  EVR      Pullback50      $97.48     $346.97  $353.65  +1.9%   $+1.84  |
|  HST      Pullback50      $91.26     $23.37   $23.80   +1.8%   $+1.65  |
|                                                                        |
|  Total invested                                                 $284.97|
|  Total open P&L                                                  $+4.08|
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
|  2026-07-14  SELL  PLD  Pullback50  $95.64  P&L $+0.01                 |
|  2026-07-14  SELL  NEE  Pullback50  $89.54  P&L $-0.09                 |
|  2026-07-14  SELL  KMI  Pullback50  $89.48  P&L $-0.10                 |
|  2026-07-14  SELL  NI  Pullback50  $44.05  P&L $-0.23                  |
|  2026-07-14  SELL  HON  Pullback50  $95.44  P&L $-0.58                 |
|  2026-07-14  SELL  NDSN  Pullback50  $90.78  P&L $-0.53                |
+========================================================================+
```

### Options bot full output

```text
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-15T21:48:39.213795-04:00 ===

[Run context]
After hours (21:48 ET) — exit summary only.
Paper auth OK — equity $132362.68, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $132,362.68                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             14                                      |
|  Broker option positions       3                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=176  buckets=43  win=46%                             |
|  Returns   avg=+30.7%  med=-2.7%  p10=-77.0%  p90=+98.3%               |
|  Realized  $+6,235.77                                                  |
|  Raw incl dropped  trades=273  real=$+5,326.58                         |
|  Today     trades=4  avg=-64.7%  med=-72.7%  real=$-105.00             |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b62  c062_s173_w3_1045_  5  60% +628.8 +1100.0 +1100.0 $   +116       |
|  b89  c089_s165_w2_1005_  2 100% +425.9 +425.9 +790.0 $   +113         |
|  b28  c028_s165_w1_0928_  4 100% +91.7 +95.1 +102.0 $   +187           |
|  b69  c069_s165_w2_1005_  2  50% +83.2 +83.2 +210.0 $     -3           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 35 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_  7   0% -54.4 -74.0 -77.0 $   -243       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (3)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  ADBE260717C00240000           9    -68.2%   $   -270.00               |
|  C260717C00148000              2    -98.5%   $   -127.33               |
|  BSX260717C00045500            3    -50.0%   $    -15.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-15.log
elapsed=2.9s reconcile=2.76s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=2.9s. run=#4102 https://github.com/28twagg-ops/TradingBot/actions/runs/29465021606
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-15_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-15_buckets.csv
Summary: 4 buckets closed trades, $-105.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-15_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-15_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
```

---

## Run 20260716T044523Z

- UTC timestamp: `20260716T044523Z`
- GitHub run: [#4103](https://github.com/28twagg-ops/TradingBot/actions/runs/29472109404)
- Run id: `29472109404`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`5s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T00:45:25.949912-04:00","date":"2026-07-16","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":4.1,"phases_s":{"reconcile":3.27},"signals":0,"placed":0,"equity":133326.68,"open_positions":3,"pending_orders":0,"open_lots":14,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4103","github_run_id":"29472109404","status":"ok"}
```

### Live bot full output

```text
04:45:24  INFO      Mode: summary
04:45:25  INFO        Daily log -> logs/daily/2026-07-16.md
04:45:25  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         04:45 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $481.08|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $481.08|
|  Cash                                                           $196.11|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $284.97|
|  Open P&L                                                        $+4.08|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (3 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CHH      Pullback50      $96.23     $108.43  $109.10  +0.6%   $+0.59  |
|  EVR      Pullback50      $97.48     $346.97  $353.65  +1.9%   $+1.84  |
|  HST      Pullback50      $91.26     $23.37   $23.80   +1.8%   $+1.65  |
|                                                                        |
|  Total invested                                                 $284.97|
|  Total open P&L                                                  $+4.08|
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
|  2026-07-14  SELL  PLD  Pullback50  $95.64  P&L $+0.01                 |
|  2026-07-14  SELL  NEE  Pullback50  $89.54  P&L $-0.09                 |
|  2026-07-14  SELL  KMI  Pullback50  $89.48  P&L $-0.10                 |
|  2026-07-14  SELL  NI  Pullback50  $44.05  P&L $-0.23                  |
|  2026-07-14  SELL  HON  Pullback50  $95.44  P&L $-0.58                 |
|  2026-07-14  SELL  NDSN  Pullback50  $90.78  P&L $-0.53                |
+========================================================================+
```

### Options bot full output

```text
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-16T00:45:25.949912-04:00 ===

[Run context]
After hours (00:45 ET) — exit summary only.
Paper auth OK — equity $133326.68, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $133,326.68                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             14                                      |
|  Broker option positions       3                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=176  buckets=43  win=46%                             |
|  Returns   avg=+30.7%  med=-2.7%  p10=-77.0%  p90=+98.3%               |
|  Realized  $+6,235.77                                                  |
|  Raw incl dropped  trades=273  real=$+5,326.58                         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b62  c062_s173_w3_1045_  5  60% +628.8 +1100.0 +1100.0 $   +116       |
|  b89  c089_s165_w2_1005_  2 100% +425.9 +425.9 +790.0 $   +113         |
|  b28  c028_s165_w1_0928_  4 100% +91.7 +95.1 +102.0 $   +187           |
|  b69  c069_s165_w2_1005_  2  50% +83.2 +83.2 +210.0 $     -3           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 35 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_  7   0% -54.4 -74.0 -77.0 $   -243       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (3)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  ADBE260717C00240000           9    -68.2%   $   -270.00               |
|  C260717C00148000              2    -98.5%   $   -127.33               |
|  BSX260717C00045500            3    -50.0%   $    -15.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=4.1s reconcile=3.27s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=4.1s. run=#4103 https://github.com/28twagg-ops/TradingBot/actions/runs/29472109404
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
```

---

## Run 20260716T115128Z

- UTC timestamp: `20260716T115128Z`
- GitHub run: [#4104](https://github.com/28twagg-ops/TradingBot/actions/runs/29495912126)
- Run id: `29495912126`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`5s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T07:51:31.217122-04:00","date":"2026-07-16","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":3.2,"phases_s":{"reconcile":2.94},"signals":0,"placed":0,"equity":129570.59,"open_positions":3,"pending_orders":0,"open_lots":14,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4104","github_run_id":"29495912126","status":"ok"}
```

### Live bot full output

```text
11:51:29  INFO      Mode: summary
11:51:30  INFO        Daily log -> logs/daily/2026-07-16.md
11:51:30  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         11:51 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $481.31|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $481.31|
|  Cash                                                           $196.11|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $285.20|
|  Open P&L                                                        $+4.31|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (3 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CHH      Pullback50      $96.23     $108.43  $109.10  +0.6%   $+0.59  |
|  EVR      Pullback50      $97.48     $346.97  $353.65  +1.9%   $+1.84  |
|  HST      Pullback50      $91.49     $23.37   $23.86   +2.1%   $+1.88  |
|                                                                        |
|  Total invested                                                 $285.20|
|  Total open P&L                                                  $+4.31|
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
|  2026-07-14  SELL  PLD  Pullback50  $95.64  P&L $+0.01                 |
|  2026-07-14  SELL  NEE  Pullback50  $89.54  P&L $-0.09                 |
|  2026-07-14  SELL  KMI  Pullback50  $89.48  P&L $-0.10                 |
|  2026-07-14  SELL  NI  Pullback50  $44.05  P&L $-0.23                  |
|  2026-07-14  SELL  HON  Pullback50  $95.44  P&L $-0.58                 |
|  2026-07-14  SELL  NDSN  Pullback50  $90.78  P&L $-0.53                |
+========================================================================+
```

### Options bot full output

```text
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-16T07:51:31.217122-04:00 ===

[Run context]
After hours (07:51 ET) — exit summary only.
Paper auth OK — equity $129570.59, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $129,570.59                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             14                                      |
|  Broker option positions       3                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=176  buckets=43  win=46%                             |
|  Returns   avg=+30.7%  med=-2.7%  p10=-77.0%  p90=+98.3%               |
|  Realized  $+6,235.77                                                  |
|  Raw incl dropped  trades=273  real=$+5,326.58                         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b62  c062_s173_w3_1045_  5  60% +628.8 +1100.0 +1100.0 $   +116       |
|  b89  c089_s165_w2_1005_  2 100% +425.9 +425.9 +790.0 $   +113         |
|  b28  c028_s165_w1_0928_  4 100% +91.7 +95.1 +102.0 $   +187           |
|  b69  c069_s165_w2_1005_  2  50% +83.2 +83.2 +210.0 $     -3           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 35 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_  7   0% -54.4 -74.0 -77.0 $   -243       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (3)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  ADBE260717C00240000           9    -68.2%   $   -270.00               |
|  C260717C00148000              2    -98.5%   $   -127.33               |
|  BSX260717C00045500            3    -50.0%   $    -15.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=3.2s reconcile=2.94s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=3.2s. run=#4104 https://github.com/28twagg-ops/TradingBot/actions/runs/29495912126
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
```

---

## Run 20260716T130057Z

- UTC timestamp: `20260716T130057Z`
- GitHub run: [#4105](https://github.com/28twagg-ops/TradingBot/actions/runs/29500380338)
- Run id: `29500380338`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`5s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T09:01:01.587295-04:00","date":"2026-07-16","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":3.7,"phases_s":{"reconcile":3.27},"signals":0,"placed":0,"equity":130688.59,"open_positions":3,"pending_orders":0,"open_lots":14,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4105","github_run_id":"29500380338","status":"ok"}
```

### Live bot full output

```text
13:00:58  INFO      Mode: summary
13:01:00  INFO        Daily log -> logs/daily/2026-07-16.md
13:01:00  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $481.22|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $481.22|
|  Cash                                                           $196.11|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $285.11|
|  Open P&L                                                        $+4.23|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (3 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CHH      Pullback50      $96.37     $108.43  $109.26  +0.8%   $+0.73  |
|  EVR      Pullback50      $97.48     $346.97  $353.65  +1.9%   $+1.84  |
|  HST      Pullback50      $91.26     $23.37   $23.80   +1.8%   $+1.65  |
|                                                                        |
|  Total invested                                                 $285.11|
|  Total open P&L                                                  $+4.23|
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
|  2026-07-14  SELL  PLD  Pullback50  $95.64  P&L $+0.01                 |
|  2026-07-14  SELL  NEE  Pullback50  $89.54  P&L $-0.09                 |
|  2026-07-14  SELL  KMI  Pullback50  $89.48  P&L $-0.10                 |
|  2026-07-14  SELL  NI  Pullback50  $44.05  P&L $-0.23                  |
|  2026-07-14  SELL  HON  Pullback50  $95.44  P&L $-0.58                 |
|  2026-07-14  SELL  NDSN  Pullback50  $90.78  P&L $-0.53                |
+========================================================================+
```

### Options bot full output

```text
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-16T09:01:01.587295-04:00 ===

[Run context]
After hours (09:01 ET) — exit summary only.
Paper auth OK — equity $130688.59, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $130,688.59                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             14                                      |
|  Broker option positions       3                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=176  buckets=43  win=46%                             |
|  Returns   avg=+30.7%  med=-2.7%  p10=-77.0%  p90=+98.3%               |
|  Realized  $+6,235.77                                                  |
|  Raw incl dropped  trades=273  real=$+5,326.58                         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b62  c062_s173_w3_1045_  5  60% +628.8 +1100.0 +1100.0 $   +116       |
|  b89  c089_s165_w2_1005_  2 100% +425.9 +425.9 +790.0 $   +113         |
|  b28  c028_s165_w1_0928_  4 100% +91.7 +95.1 +102.0 $   +187           |
|  b69  c069_s165_w2_1005_  2  50% +83.2 +83.2 +210.0 $     -3           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 35 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_  7   0% -54.4 -74.0 -77.0 $   -243       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (3)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  ADBE260717C00240000           9    -68.2%   $   -270.00               |
|  C260717C00148000              2    -98.5%   $   -127.33               |
|  BSX260717C00045500            3    -50.0%   $    -15.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=3.7s reconcile=3.27s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=3.7s. run=#4105 https://github.com/28twagg-ops/TradingBot/actions/runs/29500380338
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 8.1% (22/273)
```

---

## Run 20260716T130532Z

- UTC timestamp: `20260716T130532Z`
- GitHub run: [#4106](https://github.com/28twagg-ops/TradingBot/actions/runs/29500714743)
- Run id: `29500714743`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`5s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T09:05:34.765158-04:00","date":"2026-07-16","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":3.0,"phases_s":{"reconcile":2.76},"signals":0,"placed":0,"equity":130490.59,"open_positions":3,"pending_orders":0,"open_lots":14,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4106","github_run_id":"29500714743","status":"ok"}
```

### Live bot full output

```text
13:05:33  INFO      Mode: summary
13:05:33  INFO        Daily log -> logs/daily/2026-07-16.md
13:05:33  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:05 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $481.22|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $481.22|
|  Cash                                                           $196.11|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $285.11|
|  Open P&L                                                        $+4.23|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (3 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CHH      Pullback50      $96.37     $108.43  $109.26  +0.8%   $+0.73  |
|  EVR      Pullback50      $97.48     $346.97  $353.65  +1.9%   $+1.84  |
|  HST      Pullback50      $91.26     $23.37   $23.80   +1.8%   $+1.65  |
|                                                                        |
|  Total invested                                                 $285.11|
|  Total open P&L                                                  $+4.23|
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
|  2026-07-14  SELL  PLD  Pullback50  $95.64  P&L $+0.01                 |
|  2026-07-14  SELL  NEE  Pullback50  $89.54  P&L $-0.09                 |
|  2026-07-14  SELL  KMI  Pullback50  $89.48  P&L $-0.10                 |
|  2026-07-14  SELL  NI  Pullback50  $44.05  P&L $-0.23                  |
|  2026-07-14  SELL  HON  Pullback50  $95.44  P&L $-0.58                 |
|  2026-07-14  SELL  NDSN  Pullback50  $90.78  P&L $-0.53                |
+========================================================================+
```

### Options bot full output

```text
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-16T09:05:34.765158-04:00 ===

[Run context]
After hours (09:05 ET) — exit summary only.
Paper auth OK — equity $130490.59, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $130,490.59                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             14                                      |
|  Broker option positions       3                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=176  buckets=43  win=46%                             |
|  Returns   avg=+30.7%  med=-2.7%  p10=-77.0%  p90=+98.3%               |
|  Realized  $+6,235.77                                                  |
|  Raw incl dropped  trades=273  real=$+5,326.58                         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b62  c062_s173_w3_1045_  5  60% +628.8 +1100.0 +1100.0 $   +116       |
|  b89  c089_s165_w2_1005_  2 100% +425.9 +425.9 +790.0 $   +113         |
|  b28  c028_s165_w1_0928_  4 100% +91.7 +95.1 +102.0 $   +187           |
|  b69  c069_s165_w2_1005_  2  50% +83.2 +83.2 +210.0 $     -3           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 35 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_  7   0% -54.4 -74.0 -77.0 $   -243       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (3)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  ADBE260717C00240000           9    -68.2%   $   -270.00               |
|  C260717C00148000              2    -98.5%   $   -127.33               |
|  BSX260717C00045500            3    -50.0%   $    -15.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=3.0s reconcile=2.76s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=3.0s. run=#4106 https://github.com/28twagg-ops/TradingBot/actions/runs/29500714743
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 8.1% (22/273)
```

---

## Run 20260716T131102Z

- UTC timestamp: `20260716T131102Z`
- GitHub run: [#4107](https://github.com/28twagg-ops/TradingBot/actions/runs/29501064548)
- Run id: `29501064548`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`5s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T09:11:05.718041-04:00","date":"2026-07-16","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":4.1,"phases_s":{"reconcile":3.78},"signals":0,"placed":0,"equity":130690.59,"open_positions":3,"pending_orders":0,"open_lots":14,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4107","github_run_id":"29501064548","status":"ok"}
```

### Live bot full output

```text
13:11:04  INFO      Mode: summary
13:11:04  INFO        Daily log -> logs/daily/2026-07-16.md
13:11:04  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $481.22|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $481.22|
|  Cash                                                           $196.11|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $285.11|
|  Open P&L                                                        $+4.23|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (3 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CHH      Pullback50      $96.37     $108.43  $109.26  +0.8%   $+0.73  |
|  EVR      Pullback50      $97.48     $346.97  $353.65  +1.9%   $+1.84  |
|  HST      Pullback50      $91.26     $23.37   $23.80   +1.8%   $+1.65  |
|                                                                        |
|  Total invested                                                 $285.11|
|  Total open P&L                                                  $+4.23|
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
|  2026-07-14  SELL  PLD  Pullback50  $95.64  P&L $+0.01                 |
|  2026-07-14  SELL  NEE  Pullback50  $89.54  P&L $-0.09                 |
|  2026-07-14  SELL  KMI  Pullback50  $89.48  P&L $-0.10                 |
|  2026-07-14  SELL  NI  Pullback50  $44.05  P&L $-0.23                  |
|  2026-07-14  SELL  HON  Pullback50  $95.44  P&L $-0.58                 |
|  2026-07-14  SELL  NDSN  Pullback50  $90.78  P&L $-0.53                |
+========================================================================+
```

### Options bot full output

```text
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-16T09:11:05.718041-04:00 ===

[Run context]
After hours (09:11 ET) — exit summary only.
Paper auth OK — equity $130690.59, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $130,690.59                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             14                                      |
|  Broker option positions       3                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=176  buckets=43  win=46%                             |
|  Returns   avg=+30.7%  med=-2.7%  p10=-77.0%  p90=+98.3%               |
|  Realized  $+6,235.77                                                  |
|  Raw incl dropped  trades=273  real=$+5,326.58                         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b62  c062_s173_w3_1045_  5  60% +628.8 +1100.0 +1100.0 $   +116       |
|  b89  c089_s165_w2_1005_  2 100% +425.9 +425.9 +790.0 $   +113         |
|  b28  c028_s165_w1_0928_  4 100% +91.7 +95.1 +102.0 $   +187           |
|  b69  c069_s165_w2_1005_  2  50% +83.2 +83.2 +210.0 $     -3           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 35 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_  7   0% -54.4 -74.0 -77.0 $   -243       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (3)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  ADBE260717C00240000           9    -68.2%   $   -270.00               |
|  C260717C00148000              2    -98.5%   $   -127.33               |
|  BSX260717C00045500            3    -50.0%   $    -15.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=4.1s reconcile=3.78s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=4.1s. run=#4107 https://github.com/28twagg-ops/TradingBot/actions/runs/29501064548
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 8.1% (22/273)
```

---

## Run 20260716T131536Z

- UTC timestamp: `20260716T131536Z`
- GitHub run: [#4108](https://github.com/28twagg-ops/TradingBot/actions/runs/29501406148)
- Run id: `29501406148`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`4s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T09:15:38.932447-04:00","date":"2026-07-16","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":3.3,"phases_s":{"reconcile":3.08},"signals":0,"placed":0,"equity":130768.11,"open_positions":3,"pending_orders":0,"open_lots":14,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4108","github_run_id":"29501406148","status":"ok"}
```

### Live bot full output

```text
13:15:37  INFO      Mode: summary
13:15:38  INFO        Daily log -> logs/daily/2026-07-16.md
13:15:38  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:15 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $481.02|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $481.02|
|  Cash                                                           $196.11|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $284.91|
|  Open P&L                                                        $+4.02|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (3 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CHH      Pullback50      $96.17     $108.43  $109.03  +0.6%   $+0.53  |
|  EVR      Pullback50      $97.48     $346.97  $353.65  +1.9%   $+1.84  |
|  HST      Pullback50      $91.26     $23.37   $23.80   +1.8%   $+1.65  |
|                                                                        |
|  Total invested                                                 $284.91|
|  Total open P&L                                                  $+4.02|
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
|  2026-07-14  SELL  PLD  Pullback50  $95.64  P&L $+0.01                 |
|  2026-07-14  SELL  NEE  Pullback50  $89.54  P&L $-0.09                 |
|  2026-07-14  SELL  KMI  Pullback50  $89.48  P&L $-0.10                 |
|  2026-07-14  SELL  NI  Pullback50  $44.05  P&L $-0.23                  |
|  2026-07-14  SELL  HON  Pullback50  $95.44  P&L $-0.58                 |
|  2026-07-14  SELL  NDSN  Pullback50  $90.78  P&L $-0.53                |
+========================================================================+
```

### Options bot full output

```text
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-16T09:15:38.932447-04:00 ===

[Run context]
After hours (09:15 ET) — exit summary only.
Paper auth OK — equity $130768.11, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $130,768.11                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             14                                      |
|  Broker option positions       3                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=176  buckets=43  win=46%                             |
|  Returns   avg=+30.7%  med=-2.7%  p10=-77.0%  p90=+98.3%               |
|  Realized  $+6,235.77                                                  |
|  Raw incl dropped  trades=273  real=$+5,326.58                         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b62  c062_s173_w3_1045_  5  60% +628.8 +1100.0 +1100.0 $   +116       |
|  b89  c089_s165_w2_1005_  2 100% +425.9 +425.9 +790.0 $   +113         |
|  b28  c028_s165_w1_0928_  4 100% +91.7 +95.1 +102.0 $   +187           |
|  b69  c069_s165_w2_1005_  2  50% +83.2 +83.2 +210.0 $     -3           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 35 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_  7   0% -54.4 -74.0 -77.0 $   -243       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (3)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  ADBE260717C00240000           9    -68.2%   $   -270.00               |
|  C260717C00148000              2    -98.5%   $   -127.33               |
|  BSX260717C00045500            3    -50.0%   $    -15.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=3.3s reconcile=3.08s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=3.3s. run=#4108 https://github.com/28twagg-ops/TradingBot/actions/runs/29501406148
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 8.1% (22/273)
```

---
