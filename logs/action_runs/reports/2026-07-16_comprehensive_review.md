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

## Run 20260716T132043Z

- UTC timestamp: `20260716T132043Z`
- GitHub run: [#4109](https://github.com/28twagg-ops/TradingBot/actions/runs/29501758141)
- Run id: `29501758141`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`5s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T09:20:45.480581-04:00","date":"2026-07-16","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":3.3,"phases_s":{"reconcile":2.8},"signals":0,"placed":0,"equity":130654.59,"open_positions":3,"pending_orders":0,"open_lots":14,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4109","github_run_id":"29501758141","status":"ok"}
```

### Live bot full output

```text
13:20:44  INFO      Mode: summary
13:20:44  INFO        Daily log -> logs/daily/2026-07-16.md
13:20:44  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:20 UTC|
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
=== options_morning_bot (PAPER) 2026-07-16T09:20:45.480581-04:00 ===

[Run context]
After hours (09:20 ET) — exit summary only.
Paper auth OK — equity $130654.59, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $130,654.59                             |
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
elapsed=3.3s reconcile=2.8s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=3.3s. run=#4109 https://github.com/28twagg-ops/TradingBot/actions/runs/29501758141
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 8.1% (22/273)
```

---

## Run 20260716T132531Z

- UTC timestamp: `20260716T132531Z`
- GitHub run: [#4110](https://github.com/28twagg-ops/TradingBot/actions/runs/29502092967)
- Run id: `29502092967`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`4s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T09:25:33.751249-04:00","date":"2026-07-16","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":3.1,"phases_s":{"reconcile":2.77},"signals":0,"placed":0,"equity":130751.07,"open_positions":3,"pending_orders":0,"open_lots":14,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4110","github_run_id":"29502092967","status":"ok"}
```

### Live bot full output

```text
13:25:32  INFO      Mode: summary
13:25:32  INFO        Daily log -> logs/daily/2026-07-16.md
13:25:32  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:25 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.67|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $482.67|
|  Cash                                                           $196.11|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $286.56|
|  Open P&L                                                        $+5.67|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (3 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CHH      Pullback50      $96.17     $108.43  $109.03  +0.6%   $+0.53  |
|  EVR      Pullback50      $97.48     $346.97  $353.65  +1.9%   $+1.84  |
|  HST      Pullback50      $92.91     $23.37   $24.23   +3.7%   $+3.30  |
|                                                                        |
|  Total invested                                                 $286.56|
|  Total open P&L                                                  $+5.67|
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
=== options_morning_bot (PAPER) 2026-07-16T09:25:33.751249-04:00 ===

[Run context]
After hours (09:25 ET) — exit summary only.
Paper auth OK — equity $130751.07, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $130,751.07                             |
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
elapsed=3.1s reconcile=2.77s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=3.1s. run=#4110 https://github.com/28twagg-ops/TradingBot/actions/runs/29502092967
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 8.1% (22/273)
```

---

## Run 20260716T133043Z

- UTC timestamp: `20260716T133043Z`
- GitHub run: [#4111](https://github.com/28twagg-ops/TradingBot/actions/runs/29502453507)
- Run id: `29502453507`
- Live bot: exit=`0`, duration=`215s`
- Options bot: exit=`0`, duration=`40s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T09:34:19.498718-04:00","date":"2026-07-16","mode":"entry+manage","header":"entry+manage (9 new)","elapsed_s":38.6,"phases_s":{"reconcile":2.65,"cancel":0.08,"manage":1.35,"scan":20.63,"entries":10.85,"reconcile2":2.69},"signals":94,"placed":9,"equity":128691.59,"open_positions":3,"pending_orders":9,"open_lots":12,"submitted_today":9,"filled_today":0,"unattributed_contracts":0,"top_signals":["S173:AMD","S173:ALB","S173:APH","S173:ADI","S173:AMAT","S173:ANET","S173:BLDR","S173:CAT"],"github_run":"4111","github_run_id":"29502453507","status":"ok"}
```

### Live bot full output

```text
13:30:44  INFO      Mode: morning_prep
13:30:45  INFO        [prep_positions] 3/3 (3 valid)
13:30:45  INFO      Fetching tickers (universe=both)...
13:30:46  INFO        S&P 500: 503
13:30:46  INFO        MidCap 400: 400
13:30:46  INFO        Total: 903 tickers
13:30:47  INFO        [prep_universe] 40/900 (40 valid)
13:30:49  INFO        [prep_universe] 80/900 (80 valid)
13:30:50  INFO        [prep_universe] 120/900 (120 valid)
13:30:51  INFO        [prep_universe] 160/900 (160 valid)
13:30:53  INFO        [prep_universe] 200/900 (199 valid)
13:31:00  INFO        [prep_universe] 240/900 (238 valid)
13:31:13  INFO        [prep_universe] 280/900 (278 valid)
13:31:23  INFO        [prep_universe] 320/900 (318 valid)
13:31:37  INFO        [prep_universe] 360/900 (358 valid)
13:31:47  INFO        [prep_universe] 400/900 (397 valid)
13:32:00  INFO        [prep_universe] 440/900 (437 valid)
13:32:13  INFO        [prep_universe] 480/900 (477 valid)
13:32:23  INFO        [prep_universe] 520/900 (517 valid)
13:32:37  INFO        [prep_universe] 560/900 (556 valid)
13:32:47  INFO        [prep_universe] 600/900 (596 valid)
13:33:01  INFO        [prep_universe] 640/900 (636 valid)
13:33:11  INFO        [prep_universe] 680/900 (676 valid)
13:33:24  INFO        [prep_universe] 720/900 (716 valid)
13:33:37  INFO        [prep_universe] 760/900 (756 valid)
13:33:47  INFO        [prep_universe] 800/900 (796 valid)
13:34:00  INFO        [prep_universe] 840/900 (835 valid)
13:34:13  INFO        [prep_universe] 880/900 (875 valid)
13:34:17  INFO        [prep_universe] 900/900 (895 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:30 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $480.84|
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
|  Invested                                                       $284.73|
|  Open P&L                                                        $+3.84|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CHH      Pullback50      $96.89     $108.43  $109.84  +1.3%   $+1.25  |
|  EVR      Pullback50      $96.51     $346.97  $350.11  +0.9%   $+0.87  |
|  HST      Pullback50      $91.34     $23.37   $23.82   +1.9%   $+1.73  |
+========================================================================+

+========================================================================+
|                            OPEN SELL ORDERS                            |
+========================================================================+
|  Count                                                                1|
|  TICKER    TYPE              QTY       LIMIT       STOP                |
+------------------------------------------------------------------------+
|  HST       OrderType.STOP    3         None        23.25               |
+========================================================================+

+========================================================================+
|                              PREP SUMMARY                              |
+========================================================================+
|  Saved                                                              yes|
|  Exit candidates                                                      1|
|  Signal candidates                                                   60|
|  Universe scanned                                                   900|
+========================================================================+
```

### Options bot full output

```text
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-16T09:34:19.498718-04:00 ===

[Run context]
Paper auth OK — equity $128691.59, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-16 09:34:23,047 INFO   EXIT [b21|c021_s173_w2_1005_1045_r2|S173] stop_loss (-98.5%) SELL 1 C260717C00148000 @<= 0.01
2026-07-16 09:34:23,250 INFO   EXIT [b9|c009_s165_w2_1005_1045_r1|S165] stop_loss (-50.0%) SELL 1 BSX260717C00045500 @<= 0.02
2026-07-16 09:34:23,768 INFO   EXIT [b62|c062_s173_w3_1045_1120_r4|S173] stop_loss (-61.4%) SELL 1 ADBE260717C00240000 @<= 0.18

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 94 signal(s); top: ['S173:AMD', 'S173:ALB', 'S173:APH', 'S173:ADI', 'S173:AMAT', 'S173:ANET', 'S173:BLDR', 'S173:CAT']
Paper lab: $128411 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 140 no tradeable call, 249 pending order
Placed 9 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $128,691.59                             |
|  Signals this run              94                                      |
|  Orders submitted (session)    9                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       9                                       |
|  Open virtual lots             12                                      |
|  Broker option positions       3                                       |
|  Pending orders                9                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=178  buckets=44  win=46%                             |
|  Returns   avg=+29.5%  med=-4.4%  p10=-77.0%  p90=+97.7%               |
|  Realized  $+6,158.77                                                  |
|  Raw incl dropped  trades=275  real=$+5,249.58                         |
|  Today     trades=2  avg=-74.3%  med=-74.3%  real=$-77.00              |
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
|  ... 36 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_  8   0% -59.9 -75.5 -98.6 $   -315       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (9)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S165:AVGO(5), S173:UAL(4)               |
+------------------------------------------------------------------------+
|  b0   S173 UAL      limit=0.67                                         |
|  b40  S173 UAL      limit=0.67                                         |
|  b60  S173 UAL      limit=0.67                                         |
|  b80  S173 UAL      limit=0.67                                         |
|  b8   S165 AVGO     limit=0.55                                         |
|  ... 4 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b62  S173 ADBE260717C00240000 x1 stop_loss (-61.4%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (3)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  ADBE260717C00240000           9    -63.6%   $   -252.00               |
|  C260717C00148000              1    -98.5%   $    -63.67               |
|  BSX260717C00045500            2   +100.0%   $    +20.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=38.6s reconcile=2.65s cancel=0.08s manage=1.35s scan=20.63s entries=10.85s
STATUS: options_morning_bot run complete (PAPER) elapsed=38.6s. run=#4111 https://github.com/28twagg-ops/TradingBot/actions/runs/29502453507
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 2 buckets closed trades, $-77.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 8.0% (22/275)
```

---

## Run 20260716T133539Z

- UTC timestamp: `20260716T133539Z`
- GitHub run: [#4112](https://github.com/28twagg-ops/TradingBot/actions/runs/29502806097)
- Run id: `29502806097`
- Live bot: exit=`0`, duration=`216s`
- Options bot: exit=`0`, duration=`26s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T09:39:15.905253-04:00","date":"2026-07-16","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":25.2,"phases_s":{"reconcile":2.8,"cancel":0.04,"manage":1.32,"scan":16.11,"entries":4.59},"signals":89,"placed":0,"equity":127451.43,"open_positions":3,"pending_orders":0,"open_lots":16,"submitted_today":0,"filled_today":5,"unattributed_contracts":0,"top_signals":["S173:AMD","S173:ALB","S173:ADI","S173:AMAT","S173:BLDR","S173:CAT","S173:FIX","S173:DELL"],"github_run":"4112","github_run_id":"29502806097","status":"ok"}
```

### Live bot full output

```text
13:35:40  INFO      Mode: morning_prep
13:35:41  INFO        [prep_positions] 3/3 (3 valid)
13:35:41  INFO      Fetching tickers (universe=both)...
13:35:41  INFO        S&P 500: 503
13:35:41  INFO        MidCap 400: 400
13:35:41  INFO        Total: 903 tickers
13:35:42  INFO        [prep_universe] 40/900 (40 valid)
13:35:44  INFO        [prep_universe] 80/900 (80 valid)
13:35:45  INFO        [prep_universe] 120/900 (120 valid)
13:35:46  INFO        [prep_universe] 160/900 (160 valid)
13:35:49  INFO        [prep_universe] 200/900 (199 valid)
13:35:54  INFO        [prep_universe] 240/900 (238 valid)
13:36:07  INFO        [prep_universe] 280/900 (278 valid)
13:36:20  INFO        [prep_universe] 320/900 (318 valid)
13:36:30  INFO        [prep_universe] 360/900 (358 valid)
13:36:43  INFO        [prep_universe] 400/900 (397 valid)
13:36:56  INFO        [prep_universe] 440/900 (437 valid)
13:37:09  INFO        [prep_universe] 480/900 (477 valid)
13:37:19  INFO        [prep_universe] 520/900 (517 valid)
13:37:32  INFO        [prep_universe] 560/900 (556 valid)
13:37:42  INFO        [prep_universe] 600/900 (596 valid)
13:37:55  INFO        [prep_universe] 640/900 (636 valid)
13:38:08  INFO        [prep_universe] 680/900 (676 valid)
13:38:18  INFO        [prep_universe] 720/900 (716 valid)
13:38:31  INFO        [prep_universe] 760/900 (756 valid)
13:38:44  INFO        [prep_universe] 800/900 (796 valid)
13:38:54  INFO        [prep_universe] 840/900 (835 valid)
13:39:07  INFO        [prep_universe] 880/900 (875 valid)
13:39:13  INFO        [prep_universe] 900/900 (895 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:35 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $481.84|
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
|  Invested                                                       $285.73|
|  Open P&L                                                        $+4.85|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CHH      Pullback50      $97.58     $108.43  $110.63  +2.0%   $+1.94  |
|  EVR      Pullback50      $96.63     $346.97  $350.54  +1.0%   $+0.99  |
|  HST      Pullback50      $91.53     $23.37   $23.87   +2.1%   $+1.92  |
+========================================================================+

+========================================================================+
|                            OPEN SELL ORDERS                            |
+========================================================================+
|  Count                                                                1|
|  TICKER    TYPE              QTY       LIMIT       STOP                |
+------------------------------------------------------------------------+
|  HST       OrderType.STOP    3         None        23.25               |
+========================================================================+

+========================================================================+
|                              PREP SUMMARY                              |
+========================================================================+
|  Saved                                                              yes|
|  Exit candidates                                                      1|
|  Signal candidates                                                   69|
|  Universe scanned                                                   900|
+========================================================================+
```

### Options bot full output

```text
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-16T09:39:15.905253-04:00 ===

[Run context]
Paper auth OK — equity $127451.43, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-16 09:39:19,359 INFO   EXIT [b83|c083_s173_w4_1120_1135_r5|S173] stop_loss (-54.5%) SELL 1 ADBE260717C00240000 @<= 0.20
2026-07-16 09:39:19,496 INFO   EXIT [b69|c069_s165_w2_1005_1045_r4|S165] take_profit (+150.0%) SELL 1 BSX260717C00045500 @<= 0.26
2026-07-16 09:39:20,205 INFO   EXIT [b20|c020_s173_w1_0928_1005_r2|S173] stop_loss (-98.5%) SELL 1 C260717C00148000 @<= 0.01

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 89 signal(s); top: ['S173:AMD', 'S173:ALB', 'S173:ADI', 'S173:AMAT', 'S173:BLDR', 'S173:CAT', 'S173:FIX', 'S173:DELL']
Paper lab: $127437 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  All bucket slots blocked or closed for today's signals — skip entry loop.
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $127,451.43                             |
|  Signals this run              89                                      |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  5                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             16                                      |
|  Broker option positions       3                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=178  buckets=44  win=46%                             |
|  Returns   avg=+29.8%  med=-4.4%  p10=-77.0%  p90=+97.7%               |
|  Realized  $+6,202.77                                                  |
|  Raw incl dropped  trades=275  real=$+5,293.58                         |
|  Today     trades=2  avg=-54.2%  med=-54.2%  real=$-33.00              |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b62  c062_s173_w3_1045_  6  50% +514.3 +520.8 +1100.0 $    +88        |
|  b89  c089_s165_w2_1005_  2 100% +425.9 +425.9 +790.0 $   +113         |
|  b28  c028_s165_w1_0928_  4 100% +91.7 +95.1 +102.0 $   +187           |
|  b69  c069_s165_w2_1005_  2  50% +83.2 +83.2 +210.0 $     -3           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 36 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_  7   0% -54.4 -74.0 -77.0 $   -243       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (3)                                                     |
+------------------------------------------------------------------------+
|  b83  S173 ADBE260717C00240000 x1 stop_loss (-54.5%)                   |
|  b69  S165 BSX260717C00045500 x1 take_profit (+150.0%                  |
|  b20  S173 C260717C00148000 x1 stop_loss (-98.5%)                      |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (3)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  ADBE260717C00240000           7    -61.4%   $   -189.00               |
|  AVGO260717C00405000           5    -45.5%   $   -125.00               |
|  BSX260717C00045500            1   +200.0%   $    +20.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=25.2s reconcile=2.8s cancel=0.04s manage=1.32s scan=16.11s entries=4.59s
STATUS: options_morning_bot run complete (PAPER) elapsed=25.2s. run=#4112 https://github.com/28twagg-ops/TradingBot/actions/runs/29502806097
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 2 buckets closed trades, $-33.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 8.0% (22/275)
```

---

## Run 20260716T134043Z

- UTC timestamp: `20260716T134043Z`
- GitHub run: [#4113](https://github.com/28twagg-ops/TradingBot/actions/runs/29503173176)
- Run id: `29503173176`
- Live bot: exit=`0`, duration=`216s`
- Options bot: exit=`0`, duration=`37s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T09:44:19.969136-04:00","date":"2026-07-16","mode":"entry+manage","header":"entry+manage (1 new)","elapsed_s":35.5,"phases_s":{"reconcile":3.1,"cancel":0.16,"manage":2.37,"scan":20.14,"entries":6.18,"reconcile2":3.02},"signals":87,"placed":1,"equity":127711.33,"open_positions":4,"pending_orders":0,"open_lots":17,"submitted_today":1,"filled_today":10,"unattributed_contracts":0,"top_signals":["S173:AMD","S173:ALB","S173:ADI","S173:AMAT","S173:BLDR","S173:CAT","S173:ETN","S173:EME"],"github_run":"4113","github_run_id":"29503173176","status":"ok"}
```

### Live bot full output

```text
13:40:44  INFO      Mode: morning_prep
13:40:46  INFO        [prep_positions] 3/3 (3 valid)
13:40:46  INFO        Universe cache hit: 903 tickers (tickers_2026-07-16.json)
13:40:47  INFO        [prep_universe] 40/900 (40 valid)
13:40:49  INFO        [prep_universe] 80/900 (80 valid)
13:40:50  INFO        [prep_universe] 120/900 (120 valid)
13:40:51  INFO        [prep_universe] 160/900 (160 valid)
13:40:53  INFO        [prep_universe] 200/900 (199 valid)
13:41:01  INFO        [prep_universe] 240/900 (238 valid)
13:41:11  INFO        [prep_universe] 280/900 (278 valid)
13:41:24  INFO        [prep_universe] 320/900 (318 valid)
13:41:38  INFO        [prep_universe] 360/900 (358 valid)
13:41:48  INFO        [prep_universe] 400/900 (397 valid)
13:42:01  INFO        [prep_universe] 440/900 (437 valid)
13:42:12  INFO        [prep_universe] 480/900 (477 valid)
13:42:25  INFO        [prep_universe] 520/900 (517 valid)
13:42:36  INFO        [prep_universe] 560/900 (556 valid)
13:42:49  INFO        [prep_universe] 600/900 (596 valid)
13:42:59  INFO        [prep_universe] 640/900 (636 valid)
13:43:13  INFO        [prep_universe] 680/900 (676 valid)
13:43:23  INFO        [prep_universe] 720/900 (716 valid)
13:43:36  INFO        [prep_universe] 760/900 (756 valid)
13:43:49  INFO        [prep_universe] 800/900 (796 valid)
13:44:00  INFO        [prep_universe] 840/900 (835 valid)
13:44:13  INFO        [prep_universe] 880/900 (875 valid)
13:44:17  INFO        [prep_universe] 900/900 (895 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:40 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $480.74|
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
|  Invested                                                       $284.63|
|  Open P&L                                                        $+3.75|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CHH      Pullback50      $97.20     $108.43  $110.20  +1.6%   $+1.56  |
|  EVR      Pullback50      $95.79     $346.97  $347.51  +0.2%   $+0.15  |
|  HST      Pullback50      $91.64     $23.37   $23.90   +2.3%   $+2.04  |
+========================================================================+

+========================================================================+
|                            OPEN SELL ORDERS                            |
+========================================================================+
|  Count                                                                1|
|  TICKER    TYPE              QTY       LIMIT       STOP                |
+------------------------------------------------------------------------+
|  HST       OrderType.STOP    3         None        23.25               |
+========================================================================+

+========================================================================+
|                              PREP SUMMARY                              |
+========================================================================+
|  Saved                                                              yes|
|  Exit candidates                                                      0|
|  Signal candidates                                                   61|
|  Universe scanned                                                   900|
+========================================================================+
```

### Options bot full output

```text
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-16T09:44:19.969136-04:00 ===

[Run context]
Paper auth OK — equity $127683.33, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-16 09:44:25,749 INFO   EXIT [b3|c003_s173_w4_1120_1135_r1|S173] stop_loss (-61.4%) SELL 1 ADBE260717C00240000 @<= 0.18
2026-07-16 09:44:25,965 INFO   EXIT [b29|c029_s165_w2_1005_1045_r2|S165] take_profit (+250.0%) SELL 1 BSX260717C00045500 @<= 0.32

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 87 signal(s); top: ['S173:AMD', 'S173:ALB', 'S173:ADI', 'S173:AMAT', 'S173:BLDR', 'S173:CAT', 'S173:ETN', 'S173:EME']
Paper lab: $127695 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 19 no tradeable call, 27 pending order
Placed 1 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $127,711.33                             |
|  Signals this run              87                                      |
|  Orders submitted (session)    1                                       |
|  Orders filled today (ledger)  10                                      |
|  Entries placed this run       1                                       |
|  Open virtual lots             17                                      |
|  Broker option positions       4                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=183  buckets=44  win=45%                             |
|  Returns   avg=+30.4%  med=-6.2%  p10=-77.0%  p90=+100.0%              |
|  Realized  $+6,151.77                                                  |
|  Raw incl dropped  trades=280  real=$+5,242.58                         |
|  Today     trades=6  avg=+32.3%  med=-50.0%  real=$-55.00              |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b62  c062_s173_w3_1045_  6  50% +514.3 +520.8 +1100.0 $    +88        |
|  b89  c089_s165_w2_1005_  2 100% +425.9 +425.9 +790.0 $   +113         |
|  b69  c069_s165_w2_1005_  3  67% +122.1 +200.0 +210.0 $    +17         |
|  b29  c029_s165_w2_1005_  2  50% +100.0 +100.0 +250.0 $    +20         |
|  b28  c028_s165_w1_0928_  4 100% +91.7 +95.1 +102.0 $   +187           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 36 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_  7   0% -54.4 -74.0 -77.0 $   -243       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b3   S173 ADBE260717C00240000 x1 stop_loss (-61.4%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (4)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  ADBE260717C00240000           7    -61.4%   $   -189.00               |
|  AVGO260717C00405000           5    -45.5%   $   -125.00               |
|  UAL260717C00122000            4    -29.2%   $    -76.00               |
|  AAL260717C00015000            1     -7.1%   $     -4.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=35.5s reconcile=3.1s cancel=0.16s manage=2.37s scan=20.14s entries=6.18s
STATUS: options_morning_bot run complete (PAPER) elapsed=35.5s. run=#4113 https://github.com/28twagg-ops/TradingBot/actions/runs/29503173176
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 6 buckets closed trades, $-55.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 7.9% (22/280)
```

---

## Run 20260716T134545Z

- UTC timestamp: `20260716T134545Z`
- GitHub run: [#4114](https://github.com/28twagg-ops/TradingBot/actions/runs/29503521622)
- Run id: `29503521622`
- Live bot: exit=`0`, duration=`238s`
- Options bot: exit=`0`, duration=`19s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T09:49:44.354542-04:00","date":"2026-07-16","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":18.0,"phases_s":{"reconcile":5.19,"cancel":0.06,"manage":1.06,"scan":11.29,"entries":0.08},"signals":85,"placed":0,"equity":127210.25,"open_positions":4,"pending_orders":0,"open_lots":17,"submitted_today":1,"filled_today":10,"unattributed_contracts":0,"top_signals":["S173:AMD","S173:ADI","S173:AMAT","S173:BLDR","S173:EME","S173:EMR","S173:GNRC","S173:HUBB"],"github_run":"4114","github_run_id":"29503521622","status":"ok"}
```

### Live bot full output

```text
13:45:46  INFO      Mode: morning_scan
13:45:47  INFO        [positions] 3/3 (3 valid)
13:45:47  INFO        Universe cache hit: 903 tickers (tickers_2026-07-16.json)
13:45:48  INFO        [universe] 40/900 (40 valid)
13:45:49  INFO        [universe] 80/900 (80 valid)
13:45:50  INFO        [universe] 120/900 (120 valid)
13:45:51  INFO        [universe] 160/900 (160 valid)
13:45:53  INFO        [universe] 200/900 (199 valid)
13:46:03  INFO        [universe] 240/900 (238 valid)
13:46:13  INFO        [universe] 280/900 (278 valid)
13:46:27  INFO        [universe] 320/900 (318 valid)
13:46:37  INFO        [universe] 360/900 (358 valid)
13:46:50  INFO        [universe] 400/900 (397 valid)
13:47:03  INFO        [universe] 440/900 (437 valid)
13:47:13  INFO        [universe] 480/900 (477 valid)
13:47:26  INFO        [universe] 520/900 (517 valid)
13:47:39  INFO        [universe] 560/900 (556 valid)
13:47:49  INFO        [universe] 600/900 (596 valid)
13:48:02  INFO        [universe] 640/900 (636 valid)
13:48:15  INFO        [universe] 680/900 (676 valid)
13:48:24  INFO        [universe] 720/900 (716 valid)
13:48:37  INFO        [universe] 760/900 (756 valid)
13:48:50  INFO        [universe] 800/900 (796 valid)
13:49:01  INFO        [universe] 840/900 (835 valid)
13:49:13  INFO        [universe] 880/900 (875 valid)
13:49:20  INFO        [universe] 900/900 (895 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_SCAN|
|  Time                                                         13:45 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $480.95|
+========================================================================+

+========================================================================+
|                   RUBBER BAND BOT v8  --  DAILY SCAN                   |
+========================================================================+
|  Mode                                                      *** LIVE ***|
|  Date                                                        2026-07-16|
|  Universe                                                          both|
|  Month                                        Jul: 52wkLow + Pullback50|
|  Regime                                                            BULL|
|  Exit                                      midline / stop-0.5% / 3d max|
+========================================================================+

+========================================================================+
|                                ACCOUNT                                 |
+========================================================================+
|  Equity                                                         $480.95|
|  Cash                                                           $196.11|
|  Reserve                                          $24.05  (always kept)|
|  Available                                    $172.06  (for new trades)|
|  Seasonal trade                   $96.19  (20% -- scheduled strategies)|
|  Off-sched trade                      $96.19  (20% -- other strategies)|
+========================================================================+

+========================================================================+
|                           HOLDINGS  (3 open)                           |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CHH      Pullback50      $97.20     $108.43  $110.20  +1.6%   $+1.56  |
|  EVR      Pullback50      $95.69     $346.97  $347.15  +0.1%   $+0.05  |
|  HST      Pullback50      $91.95     $23.37   $23.98   +2.6%   $+2.34  |
|                                                                        |
|  Total invested                                                 $284.84|
|  Total open P&L                                                  $+3.95|
|  Buys today: 0  |  entry cap: 2  |  max open: 5                        |
+========================================================================+

+========================================================================+
|                               PLAN CACHE                               |
+========================================================================+
|  Mode                                                           morning|
|  File                                      logs/plans/morning_plan.json|
|  Use cached plan                                  no (stale (10080.3m))|
+========================================================================+

+========================================================================+
|          EXIT EVALUATION  (EOD -- midline + stop + max-hold)           |
+========================================================================+
|  EVR  P&L +0.1%  $+0.05                                            HOLD|
|  CHH  P&L +1.6%  $+1.56                                            HOLD|
|  HST  P&L +2.6%  $+2.34                                            HOLD|
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
|  Primary: 52wkLow  |  Secondary: Pullback50                            |
|  Source                                                       live scan|
+========================================================================+

+========================================================================+
|                         SIGNALS FOUND  --  54                          |
+========================================================================+
|  TICKER   STRATEGY        TIER   PRICE    RSI    VOL_Z   TRIGGER       |
+------------------------------------------------------------------------+
|  AME      Pullback50      SEAS   $233.26  37.4   -2.07   50MA bounce (+|
|  CARR     Pullback50      SEAS   $68.28   24.7   -3.15   50MA bounce (+|
|  CASY     Pullback50      SEAS   $829.53  59.5   -1.90   50MA bounce (+|
|  CNP      Pullback50      SEAS   $43.19   43.5   -2.55   50MA bounce (+|
|  CVX      Pullback50      SEAS   $183.66  68.0   -2.10   50MA bounce (+|
|  DRI      Pullback50      SEAS   $200.29  33.5   -2.48   50MA bounce (-|
|  FANG     Pullback50      SEAS   $191.52  60.1   -2.35   50MA bounce (-|
|  DOV      Pullback50      SEAS   $214.62  24.2   -2.16   50MA bounce (-|
|  XOM      Pullback50      SEAS   $146.21  68.5   -1.76   50MA bounce (+|
|  GNRC     GapDown         off    $220.67  18.4   -2.21   gap -3.4% reco|
|  HLT      Pullback50      SEAS   $332.41  43.0   -0.92   50MA bounce (+|
|  HON      Pullback50      SEAS   $224.71  42.6   -1.43   50MA bounce (+|
|  IFF      Pullback50      SEAS   $75.90   52.1   -2.61   50MA bounce (-|
|  KMI      Pullback50      SEAS   $32.50   44.4   -2.06   50MA bounce (+|
|  KLAC     GapDown         off    $219.30  39.7   -2.19   gap -3.0% reco|
|  LIN      Pullback50      SEAS   $515.75  46.3   -2.23   50MA bounce (+|
|  MAR      Pullback50      SEAS   $374.43  46.4   -2.76   50MA bounce (-|
|  MAA      Pullback50      SEAS   $133.47  40.0   -3.10   50MA bounce (-|
|  MDLZ     Pullback50      SEAS   $60.53   47.9   -2.02   50MA bounce (-|
|  NUE      Pullback50      SEAS   $236.63  39.5   -1.65   50MA bounce (-|
|  RL       Pullback50      SEAS   $378.88  32.7   -2.25   50MA bounce (+|
|  ROK      Pullback50      SEAS   $458.45  40.9   -1.05   50MA bounce (-|
|  TDY      Pullback50      SEAS   $619.87  46.6   -2.56   50MA bounce (-|
|  TT       Pullback50      SEAS   $471.17  33.9   -1.92   50MA bounce (+|
|  UAL      GapDown         off    $116.84  19.7   -2.36   gap -3.6% reco|
|  WEC      Pullback50      SEAS   $114.46  42.9   -2.33   50MA bounce (+|
|  WMB      Pullback50      SEAS   $74.86   40.1   -2.12   50MA bounce (+|
|  AGCO     Pullback50      SEAS   $115.62  40.4   -3.09   50MA bounce (+|13:49:21  INFO        BUY  AME  $86.03  [Pullback50]  id=e7e8634e-d24e-46e2-b86d-7b59732cbeed
13:49:21  INFO        BUY  CARR  $86.03  [Pullback50]  id=ad79324b-ce99-4184-9e4a-d87ebb52ecba
13:49:43  INFO        place_all_stops: checking 5 positions...
13:49:43  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
13:49:43  INFO        STOP-MARKET placed CARR  qty=1 (pos=1.2670)  stop=$67.55  id=71e7744f-78e6-4897-a08d-bc2d9f0f7de2
13:49:43  INFO        STOP skipped CHH: fractional (0.8820 shares) — software exit will handle it
13:49:43  INFO        STOP skipped EVR: fractional (0.2756 shares) — software exit will handle it
13:49:43  INFO        STOP already live HST @ $23.25

|  AEIS     GapDown         off    $293.63  28.3   -0.79   gap -3.5% reco|
|  BC       Pullback50      SEAS   $81.52   34.9   -2.67   50MA bounce (+|
|  CGNX     GapDown         off    $61.52   41.0   -2.16   gap -3.1% reco|
|  CNH      Pullback50      SEAS   $10.66   44.3   -2.27   50MA bounce (+|
|  COKE     Pullback50      SEAS   $179.21  50.0   -1.91   50MA bounce (-|
|  CSL      Pullback50      SEAS   $346.67  26.2   -2.40   50MA bounce (-|
|  FHN      Pullback50      SEAS   $24.76   37.7   -1.51   50MA bounce (+|
|  FIVE     Pullback50      SEAS   $200.45  64.7   -2.95   50MA bounce (-|
|  IPGP     GapDown         off    $104.58  44.9   -1.94   gap -3.4% reco|
|  IRT      Pullback50      SEAS   $16.68   48.6   -1.75   50MA bounce (+|
|  KEX      Pullback50      SEAS   $142.12  55.8   -2.76   50MA bounce (+|
|  LSCC     GapDown         off    $128.07  38.5   -1.89   gap -3.4% reco|
|  MKSI     GapDown         off    $339.00  35.2   -2.46   gap -5.0% reco|
|  OVV      Pullback50      SEAS   $56.67   65.9   -1.92   50MA bounce (+|
|  PEN      Pullback50      SEAS   $319.30  56.8   -1.94   50MA bounce (-|
|  RMBS     GapDown         off    $99.01   35.0   -0.99   gap -3.9% reco|
|  RRX      Pullback50      SEAS   $211.29  39.6   -2.07   50MA bounce (-|
|  SBRA     Pullback50      SEAS   $19.78   58.5   -1.78   50MA bounce (+|
|  SITM     GapDown         off    $587.76  39.4   -0.85   gap -4.7% reco|
|  SLAB     Pullback50      SEAS   $218.22  52.8   -1.08   50MA bounce (+|
|  STRL     GapDown         off    $645.79  24.9   -0.84   gap -4.3% reco|
|  SSD      Pullback50      SEAS   $193.11  27.1   -2.28   50MA bounce (+|
|  TREX     Pullback50      SEAS   $43.76   18.4   -1.89   50MA bounce (+|
|  VMI      Pullback50      SEAS   $541.52  29.2   -1.66   50MA bounce (+|
|  WPC      Pullback50      SEAS   $73.22   49.4   -2.58   50MA bounce (-|
|  WSO      Pullback50      SEAS   $390.18  35.4   -2.82   50MA bounce (-|
|                                                                        |
+========================================================================+

+========================================================================+
|                              ENTRY ORDERS                              |
+========================================================================+
|  Signal scaling: 54 signals / 2 slots → sea=$86 off=$86  (max sea=$96 ~|
|    ENTER [S] AME  Pullback50                                     $86.03|
|    BUY SUBMITTED [S~  fill pending — batched confirmation after entries|
|    ENTER [S] CARR  Pullback50                                    $86.03|
|    BUY SUBMITTED [S~  fill pending — batched confirmation after entries|
|    SKIP [S] CASY  Pullback50                                      cap 5|
|    SKIP [S] CNP  Pullback50                                       cap 5|
|    SKIP [S] CVX  Pullback50                                       cap 5|
|    SKIP [S] DRI  Pullback50                                       cap 5|
|    SKIP [S] FANG  Pullback50                                      cap 5|
|    SKIP [S] DOV  Pullback50                                       cap 5|
|    SKIP [S] XOM  Pullback50                                       cap 5|
|    SKIP [S] HLT  Pullback50                                       cap 5|
|    SKIP [S] HON  Pullback50                                       cap 5|
|    SKIP [S] IFF  Pullback50                                       cap 5|
|    SKIP [S] KMI  Pullback50                                       cap 5|
|    SKIP [S] LIN  Pullback50                                       cap 5|
|    SKIP [S] MAR  Pullback50                                       cap 5|
|    SKIP [S] MAA  Pullback50                                       cap 5|
|    SKIP [S] MDLZ  Pullback50                                      cap 5|
|    SKIP [S] NUE  Pullback50                                       cap 5|
|    SKIP [S] RL  Pullback50                                        cap 5|
|    SKIP [S] ROK  Pullback50                                       cap 5|
|    SKIP [S] TDY  Pullback50                                       cap 5|
|    SKIP [S] TT  Pullback50                                        cap 5|
|    SKIP [S] WEC  Pullback50                                       cap 5|
|    SKIP [S] WMB  Pullback50                                       cap 5|
|    SKIP [S] AGCO  Pullback50                                      cap 5|
|    SKIP [S] BC  Pullback50                                        cap 5|
|    SKIP [S] CNH  Pullback50                                       cap 5|
|    SKIP [S] COKE  Pullback50                                      cap 5|
|    SKIP [S] CSL  Pullback50                                       cap 5|
|    SKIP [S] FHN  Pullback50                                       cap 5|
|    SKIP [S] FIVE  Pullback50                                      cap 5|
|    SKIP [S] IRT  Pullback50                                       cap 5|
|    SKIP [S] KEX  Pullback50                                       cap 5|
|    SKIP [S] OVV  Pullback50                                       cap 5|
|    SKIP [S] PEN  Pullback50                                       cap 5|
|    SKIP [S] RRX  Pullback50                                       cap 5|
|    SKIP [S] SBRA  Pullback50                                      cap 5|
|    SKIP [S] SLAB  Pullback50                                      cap 5|
|    SKIP [S] SSD  Pullback50                                       cap 5|
|    SKIP [S] TREX  Pullback50                                      cap 5|
|    SKIP [S] VMI  Pullback50                                       cap 5|
|    SKIP [S] WPC  Pullback50                                       cap 5|
|    SKIP [S] WSO  Pullback50                                       cap 5|
|    SKIP [o] GNRC  GapDown                                         cap 5|
|    SKIP [o] KLAC  GapDown                                         cap 5|
|    SKIP [o] UAL  GapDown                                          cap 5|
|    SKIP [o] AEIS  GapDown                                         cap 5|
|    SKIP [o] CGNX  GapDown                                         cap 5|
|    SKIP [o] IPGP  GapDown                                         cap 5|
|    SKIP [o] LSCC  GapDown                                         cap 5|
|    SKIP [o] MKSI  GapDown                                         cap 5|
|    SKIP [o] RMBS  GapDown                                         cap 5|
|    SKIP [o] SITM  GapDown                                         cap 5|
|    SKIP [o] STRL  GapDown                                         cap 5|

+========================================================================+
|                         BUY FILL CONFIRMATION                          |
+========================================================================+
|  Pending submits                                                      2|
+------------------------------------------------------------------------+
|  AME                                                  still unconfirmed|
|  CARR                                                 still unconfirmed|
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
|  Strategy                                          52wkLow + Pullback50|
|  Scanned                                                            895|
|  Signals                                                             54|13:49:43  INFO        Daily log -> logs/daily/2026-07-16.md
13:49:43  INFO        Dashboard written → logs/dashboard.md

|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  2 unconfirmed|
|  Exits                                                                0|
|  Open pos                                                             5|
|  Equity                                                         $481.89|
|  Cash                                                            $24.06|
+========================================================================+
```

### Options bot full output

```text
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-16T09:49:44.354542-04:00 ===

[Run context]
Paper auth OK — equity $127208.25, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-16 09:49:50,736 INFO   EXIT [b88|c088_s165_w1_0928_1005_r5|S165] stop_loss (-52.7%) SELL 1 AVGO260717C00405000 @<= 0.23

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 85 signal(s); top: ['S173:AMD', 'S173:ADI', 'S173:AMAT', 'S173:BLDR', 'S173:EME', 'S173:EMR', 'S173:GNRC', 'S173:HUBB']
Paper lab: $127090 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  All bucket slots blocked or closed for today's signals — skip entry loop.
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $127,210.25                             |
|  Signals this run              85                                      |
|  Orders submitted (session)    1                                       |
|  Orders filled today (ledger)  10                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             17                                      |
|  Broker option positions       4                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=183  buckets=44  win=45%                             |
|  Returns   avg=+30.4%  med=-6.2%  p10=-77.0%  p90=+100.0%              |
|  Realized  $+6,151.77                                                  |
|  Raw incl dropped  trades=280  real=$+5,242.58                         |
|  Today     trades=6  avg=+32.3%  med=-50.0%  real=$-55.00              |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b62  c062_s173_w3_1045_  6  50% +514.3 +520.8 +1100.0 $    +88        |
|  b89  c089_s165_w2_1005_  2 100% +425.9 +425.9 +790.0 $   +113         |
|  b69  c069_s165_w2_1005_  3  67% +122.1 +200.0 +210.0 $    +17         |
|  b29  c029_s165_w2_1005_  2  50% +100.0 +100.0 +250.0 $    +20         |
|  b28  c028_s165_w1_0928_  4 100% +91.7 +95.1 +102.0 $   +187           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 36 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_  7   0% -54.4 -74.0 -77.0 $   -243       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b3   S173 ADBE260717C00240000 x1 stop_loss (-61.4%)                   |
|  b88  S165 AVGO260717C00405000 x1 stop_loss (-52.7%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (4)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  ADBE260717C00240000           7    -70.5%   $   -217.00               |
|  AVGO260717C00405000           4    -52.7%   $   -116.00               |
|  UAL260717C00122000            4    -43.1%   $   -112.00               |
|  AAL260717C00015000            1    -12.5%   $     -7.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=18.0s reconcile=5.19s cancel=0.06s manage=1.06s scan=11.29s entries=0.08s
STATUS: options_morning_bot run complete (PAPER) elapsed=18.0s. run=#4114 https://github.com/28twagg-ops/TradingBot/actions/runs/29503521622
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 6 buckets closed trades, $-55.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 7.9% (22/280)
```

---

## Run 20260716T135052Z

- UTC timestamp: `20260716T135052Z`
- GitHub run: [#4116](https://github.com/28twagg-ops/TradingBot/actions/runs/29503903560)
- Run id: `29503903560`
- Live bot: exit=`0`, duration=`249s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T09:49:44.354542-04:00","date":"2026-07-16","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":18.0,"phases_s":{"reconcile":5.19,"cancel":0.06,"manage":1.06,"scan":11.29,"entries":0.08},"signals":85,"placed":0,"equity":127210.25,"open_positions":4,"pending_orders":0,"open_lots":17,"submitted_today":1,"filled_today":10,"unattributed_contracts":0,"top_signals":["S173:AMD","S173:ADI","S173:AMAT","S173:BLDR","S173:EME","S173:EMR","S173:GNRC","S173:HUBB"],"github_run":"4114","github_run_id":"29503521622","status":"ok"}
```

### Live bot full output

```text
13:50:53  INFO      Mode: morning_scan
13:50:55  INFO        [positions] 5/5 (5 valid)
13:50:56  INFO        SELL LIMIT EVR  qty=0.275643427  limit=$349.28  id=faeb061d-026b-46e5-8a96-17c0ae6ccbbb
13:51:26  INFO        SELL LIMIT not filled for EVR, falling back to market
13:51:26  INFO        SELL MARKET EVR closed
13:51:29  INFO        TX logged: SELL EVR  P&L 0.87%
13:51:29  INFO        Universe cache hit: 903 tickers (tickers_2026-07-16.json)
13:51:30  INFO        [universe] 40/899 (40 valid)
13:51:31  INFO        [universe] 80/899 (80 valid)
13:51:33  INFO        [universe] 120/899 (120 valid)
13:51:34  INFO        [universe] 160/899 (160 valid)
13:51:35  INFO        [universe] 200/899 (199 valid)
13:51:42  INFO        [universe] 240/899 (238 valid)
13:51:56  INFO        [universe] 280/899 (278 valid)
13:52:06  INFO        [universe] 320/899 (318 valid)
13:52:20  INFO        [universe] 360/899 (358 valid)
13:52:30  INFO        [universe] 400/899 (397 valid)
13:52:43  INFO        [universe] 440/899 (437 valid)
13:52:54  INFO        [universe] 480/899 (477 valid)
13:53:07  INFO        [universe] 520/899 (517 valid)
13:53:18  INFO        [universe] 560/899 (556 valid)
13:53:31  INFO        [universe] 600/899 (596 valid)
13:53:41  INFO        [universe] 640/899 (636 valid)
13:53:54  INFO        [universe] 680/899 (676 valid)
13:54:05  INFO        [universe] 720/899 (716 valid)
13:54:18  INFO        [universe] 760/899 (756 valid)
13:54:31  INFO        [universe] 800/899 (796 valid)
13:54:42  INFO        [universe] 840/899 (835 valid)
13:54:55  INFO        [universe] 880/899 (875 valid)
13:54:59  INFO        [universe] 899/899 (894 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_SCAN|
|  Time                                                         13:50 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $483.17|
+========================================================================+

+========================================================================+
|                   RUBBER BAND BOT v8  --  DAILY SCAN                   |
+========================================================================+
|  Mode                                                      *** LIVE ***|
|  Date                                                        2026-07-16|
|  Universe                                                          both|
|  Month                                        Jul: 52wkLow + Pullback50|
|  Regime                                                            BULL|
|  Exit                                      midline / stop-0.5% / 3d max|
+========================================================================+

+========================================================================+
|                                ACCOUNT                                 |
+========================================================================+
|  Equity                                                         $483.17|
|  Cash                                                            $24.06|
|  Reserve                                          $24.16  (always kept)|
|  Available                                      $0.00  (for new trades)|
|  Seasonal trade                   $96.63  (20% -- scheduled strategies)|
|  Off-sched trade                      $96.63  (20% -- other strategies)|
+========================================================================+

+========================================================================+
|                           HOLDINGS  (5 open)                           |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AME      Pullback50      $86.11     $233.41  $233.66  +0.1%   $+0.09  |
|  CARR     Pullback50      $86.41     $67.89   $68.20   +0.5%   $+0.39  |
|  CHH      Pullback50      $98.06     $108.43  $111.17  +2.5%   $+2.42  |
|  EVR      Pullback50      $96.47     $346.97  $349.98  +0.9%   $+0.83  |
|  HST      Pullback50      $92.07     $23.37   $24.01   +2.7%   $+2.46  |
|                                                                        |
|  Total invested                                                 $459.11|
|  Total open P&L                                                  $+6.18|
|  Buys today: 0  |  entry cap: 0  |  max open: 5                        |
+========================================================================+

+========================================================================+
|                               PLAN CACHE                               |
+========================================================================+
|  Mode                                                           morning|
|  File                                      logs/plans/morning_plan.json|
|  Use cached plan                                  no (stale (10085.4m))|
+========================================================================+

+========================================================================+
|          EXIT EVALUATION  (EOD -- midline + stop + max-hold)           |
+========================================================================+
|  AME  P&L +0.1%  $+0.09                                            HOLD|
|  CARR  P&L +0.5%  $+0.39                                           HOLD|
|  EVR  P&L +0.9%  $+0.83                           EXIT: midline (+0.9%)|
|  CHH  P&L +2.5%  $+2.42                                            HOLD|
|  HST  P&L +2.7%  $+2.46                                            HOLD|
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
|                         SIGNALS FOUND  --  51                          |
+========================================================================+
|  TICKER   STRATEGY        TIER   PRICE    RSI    VOL_Z   TRIGGER       |
+------------------------------------------------------------------------+
|  APD      Pullback50      SEAS   $292.84  57.6   -1.96   50MA bounce (+|
|  AMD      GapDown         off    $509.35  46.4   -2.62   gap -3.7% reco|
|  CASY     Pullback50      SEAS   $829.48  59.5   -1.89   50MA bounce (+|
|  CNP      Pullback50      SEAS   $43.18   43.5   -2.51   50MA bounce (+|
|  CVX      Pullback50      SEAS   $183.70  68.0   -2.08   50MA bounce (+|
|  FANG     Pullback50      SEAS   $191.66  60.3   -2.34   50MA bounce (-|
|  DUK      Pullback50      SEAS   $126.02  47.6   -2.15   50MA bounce (+|
|  XOM      Pullback50      SEAS   $146.27  68.6   -1.75   50MA bounce (+|
|  GNRC     GapDown         off    $220.47  18.3   -2.20   gap -3.4% reco|
|  HLT      Pullback50      SEAS   $332.93  43.5   -0.92   50MA bounce (+|
|  HON      Pullback50      SEAS   $224.93  42.9   -1.42   50MA bounce (+|
|  IFF      Pullback50      SEAS   $76.20   52.9   -2.61   50MA bounce (-|
|  KMI      Pullback50      SEAS   $32.52   44.7   -2.05   50MA bounce (+|
|  KLAC     GapDown         off    $219.72  39.8   -2.18   gap -3.0% reco|
|  LIN      Pullback50      SEAS   $514.94  45.9   -2.21   50MA bounce (+|
|  MAR      Pullback50      SEAS   $375.65  47.4   -2.74   50MA bounce (+|
|  MAA      Pullback50      SEAS   $133.95  41.2   -3.09   50MA bounce (+|
|  MDLZ     Pullback50      SEAS   $60.48   47.7   -2.00   50MA bounce (-|
|  NUE      Pullback50      SEAS   $237.25  40.0   -1.65   50MA bounce (-|
|  ROK      Pullback50      SEAS   $459.30  41.2   -1.04   50MA bounce (-|
|  TDY      Pullback50      SEAS   $624.12  48.5   -2.52   50MA bounce (-|
|  TT       Pullback50      SEAS   $472.66  34.4   -1.90   50MA bounce (+|
|  UAL      GapDown         off    $117.82  20.3   -2.32   gap -3.6% reco|
|  WEC      Pullback50      SEAS   $114.39  42.7   -2.32   50MA bounce (+|13:55:00  INFO        place_all_stops: checking 4 positions...
13:55:00  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
13:55:00  INFO        STOP already live CARR @ $67.55
13:55:00  INFO        STOP skipped CHH: fractional (0.8820 shares) — software exit will handle it
13:55:00  INFO        STOP already live HST @ $23.25
13:55:01  INFO        Daily log -> logs/daily/2026-07-16.md
13:55:01  INFO        Dashboard written → logs/dashboard.md

|  WMB      Pullback50      SEAS   $75.03   40.8   -2.11   50MA bounce (+|
|  AEIS     GapDown         off    $294.39  28.4   -0.79   gap -3.5% reco|
|  AGCO     Pullback50      SEAS   $115.68  40.6   -3.08   50MA bounce (+|
|  ALSN     Pullback50      SEAS   $115.86  35.6   -0.59   50MA bounce (-|
|  CGNX     GapDown         off    $61.83   41.4   -2.14   gap -3.1% reco|
|  COKE     Pullback50      SEAS   $181.30  52.1   -1.90   50MA bounce (+|
|  CSL      Pullback50      SEAS   $347.12  26.6   -2.39   50MA bounce (-|
|  ENTG     GapDown         off    $135.49  31.2   -2.21   gap -3.9% reco|
|  FIVE     Pullback50      SEAS   $201.97  65.8   -2.83   50MA bounce (+|
|  FHN      Pullback50      SEAS   $24.79   38.0   -1.49   50MA bounce (+|
|  ITT      Pullback50      SEAS   $193.40  43.3   -2.51   50MA bounce (-|
|  IPGP     GapDown         off    $104.64  44.9   -1.93   gap -3.4% reco|
|  IRT      Pullback50      SEAS   $16.70   49.0   -1.74   50MA bounce (+|
|  KEX      Pullback50      SEAS   $142.21  56.0   -2.72   50MA bounce (+|
|  LSCC     GapDown         off    $128.04  38.5   -1.87   gap -3.4% reco|
|  MKSI     GapDown         off    $338.23  35.0   -2.45   gap -5.0% reco|
|  OVV      Pullback50      SEAS   $56.76   66.2   -1.91   50MA bounce (+|
|  PEN      Pullback50      SEAS   $319.38  57.1   -1.93   50MA bounce (-|
|  RMBS     GapDown         off    $99.01   35.0   -0.98   gap -3.9% reco|
|  RRX      Pullback50      SEAS   $212.34  40.1   -2.06   50MA bounce (+|
|  SLAB     Pullback50      SEAS   $218.54  55.8   -1.08   50MA bounce (+|
|  SITM     GapDown         off    $585.61  39.2   -0.84   gap -4.7% reco|
|  STRL     GapDown         off    $640.50  24.6   -0.83   gap -4.3% reco|
|  SSD      Pullback50      SEAS   $193.25  27.3   -2.28   50MA bounce (+|
|  VMI      Pullback50      SEAS   $540.82  29.0   -1.65   50MA bounce (+|
|  WPC      Pullback50      SEAS   $73.35   50.0   -2.57   50MA bounce (-|
|  WSO      Pullback50      SEAS   $391.48  36.5   -2.81   50MA bounce (-|
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
|  Signals                                                             51|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  0 unconfirmed|
|  Exits                                                                1|
|  Open pos                                                             4|
|  Equity                                                         $484.03|
|  Cash                                                           $120.23|
+========================================================================+
```

### Options bot full output

```text
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-16T09:55:02.225146-04:00 ===

[Run context]
Paper auth OK — equity $127301.23, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
```

---

## Run 20260716T135556Z

- UTC timestamp: `20260716T135556Z`
- GitHub run: [#4117](https://github.com/28twagg-ops/TradingBot/actions/runs/29504251469)
- Run id: `29504251469`
- Live bot: exit=`0`, duration=`0s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T09:49:44.354542-04:00","date":"2026-07-16","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":18.0,"phases_s":{"reconcile":5.19,"cancel":0.06,"manage":1.06,"scan":11.29,"entries":0.08},"signals":85,"placed":0,"equity":127210.25,"open_positions":4,"pending_orders":0,"open_lots":17,"submitted_today":1,"filled_today":10,"unattributed_contracts":0,"top_signals":["S173:AMD","S173:ADI","S173:AMAT","S173:BLDR","S173:EME","S173:EMR","S173:GNRC","S173:HUBB"],"github_run":"4114","github_run_id":"29503521622","status":"ok"}
```

### Live bot full output

```text
13:55:57  INFO      Mode: morning_scan
13:55:58  INFO        [positions] 4/4 (4 valid)
13:55:59  INFO        SELL order cancelled HST  type=OrderType.STOP  id=eb308040-6a38-455b-9703-54d41418431b
13:55:59  INFO        SELL LIMIT HST  qty=3.834465878  limit=$24.03  id=30a587e6-977e-4eef-977f-6df778c1b628
13:56:29  INFO        SELL LIMIT filled HST (confirmed by position check)
13:56:29  INFO        TX logged: SELL HST  P&L 2.85%
13:56:30  INFO        SELL LIMIT CHH  qty=0.882043714  limit=$111.42  id=33f50d4f-4512-4b73-9cee-e0887435973d
13:57:00  INFO        SELL LIMIT not filled for CHH, falling back to market
13:57:01  INFO        SELL MARKET CHH closed
13:57:03  INFO        TX logged: SELL CHH  P&L 2.96%
13:57:03  INFO        Universe cache hit: 903 tickers (tickers_2026-07-16.json)
13:57:04  INFO        [universe] 40/901 (40 valid)
13:57:05  INFO        [universe] 80/901 (80 valid)
13:57:06  INFO        [universe] 120/901 (120 valid)
13:57:08  INFO        [universe] 160/901 (160 valid)
13:57:09  INFO        [universe] 200/901 (199 valid)
13:57:17  INFO        [universe] 240/901 (238 valid)
13:57:30  INFO        [universe] 280/901 (278 valid)
13:57:40  INFO        [universe] 320/901 (318 valid)
13:57:54  INFO        [universe] 360/901 (358 valid)
13:58:04  INFO        [universe] 400/901 (397 valid)
13:58:17  INFO        [universe] 440/901 (437 valid)
13:58:28  INFO        [universe] 480/901 (477 valid)
13:58:41  INFO        [universe] 520/901 (517 valid)
13:58:52  INFO        [universe] 560/901 (556 valid)
13:59:05  INFO        [universe] 600/901 (596 valid)
13:59:16  INFO        [universe] 640/901 (636 valid)
13:59:29  INFO        [universe] 680/901 (676 valid)
13:59:39  INFO        [universe] 720/901 (716 valid)
13:59:53  INFO        [universe] 760/901 (756 valid)
14:00:06  INFO        [universe] 800/901 (796 valid)
14:00:16  INFO        [universe] 840/901 (835 valid)
14:00:30  INFO        [universe] 880/901 (875 valid)
```

### Options bot full output

```text

## Run 20260716T140109Z

- UTC timestamp: `20260716T140109Z`
- GitHub run: [#4118](https://github.com/28twagg-ops/TradingBot/actions/runs/29504630928)
- Run id: `29504630928`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`60s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T10:01:11.831631-04:00","date":"2026-07-16","mode":"entry+manage","header":"entry+manage (1 new)","elapsed_s":59.2,"phases_s":{"reconcile":2.64,"cancel":0.02,"manage":2.19,"scan":50.51,"entries":0.49,"reconcile2":2.72},"signals":90,"placed":1,"equity":127966.23,"open_positions":4,"pending_orders":1,"open_lots":16,"submitted_today":2,"filled_today":10,"unattributed_contracts":0,"top_signals":["S173:AMD","S173:APH","S173:ADI","S173:AMAT","S173:BLDR","S173:CAT","S173:COHR","S173:ETN"],"github_run":"4118","github_run_id":"29504630928","status":"ok"}
```

### Live bot full output

```text
14:01:10  INFO      Mode: exits
14:01:10  INFO        Daily log -> logs/daily/2026-07-16.md
14:01:10  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (1 ledger rows)
14:01:10  INFO        place_all_stops: checking 4 positions...
14:01:10  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
14:01:10  INFO        STOP already live CARR @ $67.55
14:01:10  INFO        STOP skipped CASY: fractional (0.1169 shares) — software exit will handle it
14:01:10  INFO        STOP-MARKET placed MO  qty=1 (pos=1.3388)  stop=$71.90  id=56d37976-caa4-4f4e-882f-1d7a80a20c4c
14:01:10  INFO        [positions] 4/4 (4 valid)
14:01:10  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $483.44|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CASY  P&L -0.1%  $-0.10                                           HOLD|
|  MO  P&L +0.0%  $+0.05                                             HOLD|
|  AME  P&L +0.3%  $+0.28                                            HOLD|
|  CARR  P&L +0.8%  $+0.67                                           HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T10:01:11.831631-04:00 ===

[Run context]
Paper auth OK — equity $127966.23, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 90 signal(s); top: ['S173:AMD', 'S173:APH', 'S173:ADI', 'S173:AMAT', 'S173:BLDR', 'S173:CAT', 'S173:COHR', 'S173:ETN']
Paper lab: $128328 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 1 no tradeable call, 37 pending order
Placed 1 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $127,966.23                             |
|  Signals this run              90                                      |
|  Orders submitted (session)    2                                       |
|  Orders filled today (ledger)  10                                      |
|  Entries placed this run       1                                       |
|  Open virtual lots             16                                      |
|  Broker option positions       4                                       |
|  Pending orders                1                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=184  buckets=44  win=45%                             |
|  Returns   avg=+29.9%  med=-6.5%  p10=-77.0%  p90=+100.0%              |
|  Realized  $+6,122.77                                                  |
|  Raw incl dropped  trades=281  real=$+5,213.58                         |
|  Today     trades=7  avg=+20.1%  med=-50.0%  real=$-84.00              |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b62  c062_s173_w3_1045_  6  50% +514.3 +520.8 +1100.0 $    +88        |
|  b89  c089_s165_w2_1005_  2 100% +425.9 +425.9 +790.0 $   +113         |
|  b69  c069_s165_w2_1005_  3  67% +122.1 +200.0 +210.0 $    +17         |
|  b29  c029_s165_w2_1005_  2  50% +100.0 +100.0 +250.0 $    +20         |
|  b28  c028_s165_w1_0928_  4 100% +91.7 +95.1 +102.0 $   +187           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 36 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_  7   0% -54.4 -74.0 -77.0 $   -243       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (1)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S165:AVGO(1)                            |
+------------------------------------------------------------------------+
|  b48  S165 AVGO     limit=0.74                                         |
+========================================================================+
+========================================================================+
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b3   S173 ADBE260717C00240000 x1 stop_loss (-61.4%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (4)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  ADBE260717C00240000           7    -86.4%   $   -266.00               |
|  UAL260717C00122000            4    -41.5%   $   -108.00               |
|  AVGO260717C00405000           4    -38.2%   $    -84.00               |
|  AAL260717C00015000            1     +7.1%   $     +4.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=59.2s reconcile=2.64s cancel=0.02s manage=2.19s scan=50.51s entries=0.49s
STATUS: options_morning_bot run complete (PAPER) elapsed=59.2s. run=#4118 https://github.com/28twagg-ops/TradingBot/actions/runs/29504630928
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 7 buckets closed trades, $-84.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 7.8% (22/281)
```

---

## Run 20260716T140746Z

- UTC timestamp: `20260716T140746Z`
- GitHub run: [#4119](https://github.com/28twagg-ops/TradingBot/actions/runs/29504996073)
- Run id: `29504996073`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`106s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T10:07:49.457021-04:00","date":"2026-07-16","mode":"entry+manage","header":"entry+manage (5 new)","elapsed_s":104.1,"phases_s":{"reconcile":2.99,"cancel":0.07,"manage":1.03,"scan":28.89,"entries":67.89,"reconcile2":2.95},"signals":96,"placed":5,"equity":129290.23,"open_positions":4,"pending_orders":6,"open_lots":16,"submitted_today":7,"filled_today":10,"unattributed_contracts":0,"top_signals":["S173:AMD","S173:APH","S173:ADI","S173:AMAT","S173:BLDR","S173:CAT","S173:COHR","S173:DELL"],"github_run":"4119","github_run_id":"29504996073","status":"ok"}
```

### Live bot full output

```text
14:07:47  INFO      Mode: exits
14:07:47  INFO        Daily log -> logs/daily/2026-07-16.md
14:07:47  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (3 ledger rows)
14:07:47  INFO        place_all_stops: checking 4 positions...
14:07:47  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
14:07:47  INFO        STOP already live CARR @ $67.55
14:07:47  INFO        STOP skipped CASY: fractional (0.1169 shares) — software exit will handle it
14:07:47  INFO        STOP already live MO @ $71.9
14:07:48  INFO        [positions] 4/4 (4 valid)
14:07:48  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:07 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $484.11|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MO  P&L +0.2%  $+0.15                                             HOLD|
|  CASY  P&L +0.3%  $+0.27                                           HOLD|
|  AME  P&L +0.5%  $+0.46                                            HOLD|
|  CARR  P&L +0.8%  $+0.69                                           HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T10:07:49.457021-04:00 ===

[Run context]
Paper auth OK — equity $129296.23, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 96 signal(s); top: ['S173:AMD', 'S173:APH', 'S173:ADI', 'S173:AMAT', 'S173:BLDR', 'S173:CAT', 'S173:COHR', 'S173:DELL']
Paper lab: $129640 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 335 no tradeable call, 140 pending order
Placed 5 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $129,290.23                             |
|  Signals this run              96                                      |
|  Orders submitted (session)    7                                       |
|  Orders filled today (ledger)  10                                      |
|  Entries placed this run       5                                       |
|  Open virtual lots             16                                      |
|  Broker option positions       4                                       |
|  Pending orders                6                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=184  buckets=44  win=45%                             |
|  Returns   avg=+29.9%  med=-6.5%  p10=-77.0%  p90=+100.0%              |
|  Realized  $+6,122.77                                                  |
|  Raw incl dropped  trades=281  real=$+5,213.58                         |
|  Today     trades=7  avg=+20.1%  med=-50.0%  real=$-84.00              |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b62  c062_s173_w3_1045_  6  50% +514.3 +520.8 +1100.0 $    +88        |
|  b89  c089_s165_w2_1005_  2 100% +425.9 +425.9 +790.0 $   +113         |
|  b69  c069_s165_w2_1005_  3  67% +122.1 +200.0 +210.0 $    +17         |
|  b29  c029_s165_w2_1005_  2  50% +100.0 +100.0 +250.0 $    +20         |
|  b28  c028_s165_w1_0928_  4 100% +91.7 +95.1 +102.0 $   +187           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 36 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_  7   0% -54.4 -74.0 -77.0 $   -243       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (6)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S165:AVGO(6)                            |
+------------------------------------------------------------------------+
|  b48  S165 AVGO     limit=0.74                                         |
|  b9   S165 AVGO     limit=0.54                                         |
|  b29  S165 AVGO     limit=0.54                                         |
|  b49  S165 AVGO     limit=0.54                                         |
|  b69  S165 AVGO     limit=0.54                                         |
|  ... 1 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b3   S173 ADBE260717C00240000 x1 stop_loss (-61.4%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (4)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  ADBE260717C00240000           7    -84.1%   $   -259.00               |
|  UAL260717C00122000            4    -38.5%   $   -100.00               |
|  AVGO260717C00405000           4     -3.6%   $     -8.00               |
|  AAL260717C00015000            1    +12.5%   $     +7.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=104.1s reconcile=2.99s cancel=0.07s manage=1.03s scan=28.89s entries=67.89s
STATUS: options_morning_bot run complete (PAPER) elapsed=104.1s. run=#4119 https://github.com/28twagg-ops/TradingBot/actions/runs/29504996073
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 7 buckets closed trades, $-84.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 7.8% (22/281)
```

---

## Run 20260716T141041Z

- UTC timestamp: `20260716T141041Z`
- GitHub run: [#4120](https://github.com/28twagg-ops/TradingBot/actions/runs/29505371351)
- Run id: `29505371351`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`43s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T10:10:43.291419-04:00","date":"2026-07-16","mode":"entry+manage","header":"entry+manage (5 new)","elapsed_s":41.9,"phases_s":{"reconcile":2.73,"cancel":0.02,"manage":1.41,"scan":34.35,"entries":0.43,"reconcile2":2.71},"signals":97,"placed":5,"equity":129942.03,"open_positions":4,"pending_orders":6,"open_lots":21,"submitted_today":12,"filled_today":15,"unattributed_contracts":0,"top_signals":["S173:AMD","S173:ALB","S173:APH","S173:ADI","S173:AMAT","S173:AVGO","S173:BLDR","S173:CAT"],"github_run":"4120","github_run_id":"29505371351","status":"ok"}
```

### Live bot full output

```text
14:10:41  INFO      Mode: exits
14:10:42  INFO        Daily log -> logs/daily/2026-07-16.md
14:10:42  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (3 ledger rows)
14:10:42  INFO        place_all_stops: checking 4 positions...
14:10:42  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
14:10:42  INFO        STOP already live CARR @ $67.55
14:10:42  INFO        STOP skipped CASY: fractional (0.1169 shares) — software exit will handle it
14:10:42  INFO        STOP already live MO @ $71.9
14:10:42  INFO        [positions] 4/4 (4 valid)
14:10:42  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $484.84|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CASY  P&L +0.2%  $+0.17                                           HOLD|
|  MO  P&L +0.3%  $+0.28                                             HOLD|
|  CARR  P&L +1.1%  $+0.91                                           HOLD|
|  AME  P&L +1.1%  $+0.94                                            HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T10:10:43.291419-04:00 ===

[Run context]
Paper auth OK — equity $129942.03, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 97 signal(s); top: ['S173:AMD', 'S173:ALB', 'S173:APH', 'S173:ADI', 'S173:AMAT', 'S173:AVGO', 'S173:BLDR', 'S173:CAT']
Paper lab: $129383 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 480 pending order
Placed 5 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $129,942.03                             |
|  Signals this run              97                                      |
|  Orders submitted (session)    12                                      |
|  Orders filled today (ledger)  15                                      |
|  Entries placed this run       5                                       |
|  Open virtual lots             21                                      |
|  Broker option positions       4                                       |
|  Pending orders                6                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=184  buckets=44  win=45%                             |
|  Returns   avg=+29.9%  med=-6.5%  p10=-77.0%  p90=+100.0%              |
|  Realized  $+6,122.77                                                  |
|  Raw incl dropped  trades=281  real=$+5,213.58                         |
|  Today     trades=7  avg=+20.1%  med=-50.0%  real=$-84.00              |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b62  c062_s173_w3_1045_  6  50% +514.3 +520.8 +1100.0 $    +88        |
|  b89  c089_s165_w2_1005_  2 100% +425.9 +425.9 +790.0 $   +113         |
|  b69  c069_s165_w2_1005_  3  67% +122.1 +200.0 +210.0 $    +17         |
|  b29  c029_s165_w2_1005_  2  50% +100.0 +100.0 +250.0 $    +20         |
|  b28  c028_s165_w1_0928_  4 100% +91.7 +95.1 +102.0 $   +187           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 36 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_  7   0% -54.4 -74.0 -77.0 $   -243       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (6)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S173:AMD(5), S165:AVGO(1)               |
+------------------------------------------------------------------------+
|  b48  S165 AVGO     limit=0.74                                         |
|  b1   S173 AMD      limit=0.68                                         |
|  b21  S173 AMD      limit=0.68                                         |
|  b41  S173 AMD      limit=0.68                                         |
|  b61  S173 AMD      limit=0.68                                         |
|  ... 1 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b3   S173 ADBE260717C00240000 x1 stop_loss (-61.4%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (4)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  ADBE260717C00240000           7    -86.4%   $   -266.00               |
|  UAL260717C00122000            4    -49.2%   $   -128.00               |
|  AVGO260717C00405000           9     -8.1%   $    -38.00               |
|  AAL260717C00015000            1     +5.4%   $     +3.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=41.9s reconcile=2.73s cancel=0.02s manage=1.41s scan=34.35s entries=0.43s
STATUS: options_morning_bot run complete (PAPER) elapsed=41.9s. run=#4120 https://github.com/28twagg-ops/TradingBot/actions/runs/29505371351
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 7 buckets closed trades, $-84.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 7.8% (22/281)
```

---

## Run 20260716T141536Z

- UTC timestamp: `20260716T141536Z`
- GitHub run: [#4121](https://github.com/28twagg-ops/TradingBot/actions/runs/29505733273)
- Run id: `29505733273`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`47s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T10:15:39.257350-04:00","date":"2026-07-16","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":46.1,"phases_s":{"reconcile":2.95,"cancel":0.02,"manage":3.06,"scan":36.7,"entries":0.04,"reconcile2":2.68},"signals":95,"placed":0,"equity":129447.03,"open_positions":5,"pending_orders":1,"open_lots":26,"submitted_today":12,"filled_today":20,"unattributed_contracts":0,"top_signals":["S173:AMD","S173:APH","S173:ADI","S173:AMAT","S173:AVGO","S173:BLDR","S173:CAT","S173:COHR"],"github_run":"4121","github_run_id":"29505733273","status":"ok"}
```

### Live bot full output

```text
14:15:37  INFO      Mode: exits
14:15:37  INFO        Daily log -> logs/daily/2026-07-16.md
14:15:37  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (3 ledger rows)
14:15:37  INFO        place_all_stops: checking 4 positions...
14:15:37  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
14:15:37  INFO        STOP already live CARR @ $67.55
14:15:37  INFO        STOP skipped CASY: fractional (0.1169 shares) — software exit will handle it
14:15:37  INFO        STOP already live MO @ $71.9
14:15:38  INFO        [positions] 4/4 (4 valid)
14:15:38  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:15 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $483.75|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CASY  P&L -0.1%  $-0.08                                           HOLD|
|  MO  P&L +0.0%  $+0.05                                             HOLD|
|  CARR  P&L +0.5%  $+0.46                                           HOLD|
|  AME  P&L +0.9%  $+0.78                                            HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T10:15:39.257350-04:00 ===

[Run context]
Paper auth OK — equity $129447.03, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 95 signal(s); top: ['S173:AMD', 'S173:APH', 'S173:ADI', 'S173:AMAT', 'S173:AVGO', 'S173:BLDR', 'S173:CAT', 'S173:COHR']
Paper lab: $129288 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  All bucket slots blocked or closed for today's signals — skip entry loop.
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $129,447.03                             |
|  Signals this run              95                                      |
|  Orders submitted (session)    12                                      |
|  Orders filled today (ledger)  20                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             26                                      |
|  Broker option positions       5                                       |
|  Pending orders                1                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=216  buckets=44  win=42%                             |
|  Returns   avg=+28.5%  med=-8.0%  p10=-77.0%  p90=+101.0%              |
|  Realized  $+5,744.77                                                  |
|  Raw incl dropped  trades=317  real=$+4,728.58                         |
|  Today     trades=8  avg=+5.3%  med=-51.4%  real=$-151.00              |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b62  c062_s173_w3_1045_  8  50% +511.3 +520.8 +1100.0 $    +97        |
|  b89  c089_s165_w2_1005_  2 100% +425.9 +425.9 +790.0 $   +113         |
|  b69  c069_s165_w2_1005_  3  67% +122.1 +200.0 +210.0 $    +17         |
|  b29  c029_s165_w2_1005_  2  50% +100.0 +100.0 +250.0 $    +20         |
|  b28  c028_s165_w1_0928_  5 100% +85.7 +94.1 +102.0 $   +221           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 36 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_  9   0% -62.2 -77.0 -98.5 $   -369       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (1)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S165:AVGO(1)                            |
+------------------------------------------------------------------------+
|  b48  S165 AVGO     limit=0.74                                         |
+========================================================================+
+========================================================================+
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b3   S173 ADBE260717C00240000 x1 stop_loss (-61.4%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (5)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  ADBE260717C00240000           7    -86.4%   $   -266.00               |
|  UAL260717C00122000            4    -47.7%   $   -124.00               |
|  AMD260717C00567500            5    -26.5%   $    -90.00               |
|  AVGO260717C00405000           9    -15.7%   $    -74.00               |
|  AAL260717C00015000            1     +7.1%   $     +4.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=46.1s reconcile=2.95s cancel=0.02s manage=3.06s scan=36.7s entries=0.04s
STATUS: options_morning_bot run complete (PAPER) elapsed=46.1s. run=#4121 https://github.com/28twagg-ops/TradingBot/actions/runs/29505733273
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 8 buckets closed trades, $-151.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 6.9% (22/317)
```

---

## Run 20260716T142044Z

- UTC timestamp: `20260716T142044Z`
- GitHub run: [#4122](https://github.com/28twagg-ops/TradingBot/actions/runs/29506116124)
- Run id: `29506116124`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`42s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T10:20:48.438944-04:00","date":"2026-07-16","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":40.9,"phases_s":{"reconcile":3.66,"cancel":0.1,"manage":2.21,"scan":31.28,"entries":0.15,"reconcile2":2.86},"signals":95,"placed":0,"equity":128663.03,"open_positions":6,"pending_orders":0,"open_lots":26,"submitted_today":12,"filled_today":21,"unattributed_contracts":0,"top_signals":["S173:AMD","S173:APH","S173:ADI","S173:AMAT","S173:AVGO","S173:BLDR","S173:CAT","S173:COHR"],"github_run":"4122","github_run_id":"29506116124","status":"ok"}
```

### Live bot full output

```text
14:20:46  INFO      Mode: exits
14:20:46  INFO        Daily log -> logs/daily/2026-07-16.md
14:20:46  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (3 ledger rows)
14:20:46  INFO        place_all_stops: checking 4 positions...
14:20:46  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
14:20:46  INFO        STOP already live CARR @ $67.55
14:20:46  INFO        STOP skipped CASY: fractional (0.1169 shares) — software exit will handle it
14:20:46  INFO        STOP already live MO @ $71.9
14:20:47  INFO        [positions] 4/4 (4 valid)
14:20:47  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $483.73|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CASY  P&L -0.4%  $-0.35                                           HOLD|
|  MO  P&L -0.1%  $-0.07                                             HOLD|
|  CARR  P&L +0.9%  $+0.80                                           HOLD|
|  AME  P&L +1.0%  $+0.82                                            HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T10:20:48.438944-04:00 ===

[Run context]
Paper auth OK — equity $128678.03, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-16 10:20:54,847 INFO   EXIT [b61|c061_s173_w2_1005_1045_r4|S173] stop_loss (-50.0%) SELL 1 AMD260717C00567500 @<= 0.31

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 95 signal(s); top: ['S173:AMD', 'S173:APH', 'S173:ADI', 'S173:AMAT', 'S173:AVGO', 'S173:BLDR', 'S173:CAT', 'S173:COHR']
Paper lab: $128551 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  All bucket slots blocked or closed for today's signals — skip entry loop.
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $128,663.03                             |
|  Signals this run              95                                      |
|  Orders submitted (session)    12                                      |
|  Orders filled today (ledger)  21                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             26                                      |
|  Broker option positions       6                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=219  buckets=44  win=42%                             |
|  Returns   avg=+28.1%  med=-8.3%  p10=-77.0%  p90=+100.4%              |
|  Realized  $+5,700.77                                                  |
|  Raw incl dropped  trades=322  real=$+4,577.58                         |
|  Today     trades=9  avg=-0.8%  med=-50.0%  real=$-185.00              |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b62  c062_s173_w3_1045_  8  50% +511.3 +520.8 +1100.0 $    +97        |
|  b89  c089_s165_w2_1005_  2 100% +425.9 +425.9 +790.0 $   +113         |
|  b69  c069_s165_w2_1005_  3  67% +122.1 +200.0 +210.0 $    +17         |
|  b29  c029_s165_w2_1005_  2  50% +100.0 +100.0 +250.0 $    +20         |
|  b28  c028_s165_w1_0928_  5 100% +85.7 +94.1 +102.0 $   +221           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 36 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_  9   0% -62.2 -77.0 -98.5 $   -369       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b3   S173 ADBE260717C00240000 x1 stop_loss (-61.4%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (6)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  ADBE260717C00240000           7    -86.4%   $   -266.00               |
|  AVGO260717C00405000           9    -29.1%   $   -137.00               |
|  AMD260717C00567500            4    -50.0%   $   -136.00               |
|  UAL260717C00122000            4    -49.2%   $   -128.00               |
|  AAL260717C00015000            1     +7.1%   $     +4.00               |
|  AVGO260717C00400000           1     -5.5%   $     -4.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=40.9s reconcile=3.66s cancel=0.1s manage=2.21s scan=31.28s entries=0.15s
STATUS: options_morning_bot run complete (PAPER) elapsed=40.9s. run=#4122 https://github.com/28twagg-ops/TradingBot/actions/runs/29506116124
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 9 buckets closed trades, $-185.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 6.8% (22/322)
```

---

## Run 20260716T142535Z

- UTC timestamp: `20260716T142535Z`
- GitHub run: [#4123](https://github.com/28twagg-ops/TradingBot/actions/runs/29506486469)
- Run id: `29506486469`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`33s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T10:25:37.907915-04:00","date":"2026-07-16","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":31.8,"phases_s":{"reconcile":2.65,"cancel":0.02,"manage":2.99,"scan":25.83,"entries":0.05},"signals":95,"placed":0,"equity":128011.99,"open_positions":6,"pending_orders":0,"open_lots":26,"submitted_today":12,"filled_today":21,"unattributed_contracts":0,"top_signals":["S173:APH","S173:ADI","S173:AMAT","S173:BLDR","S173:CAT","S173:FIX","S173:DELL","S173:ETN"],"github_run":"4123","github_run_id":"29506486469","status":"ok"}
```

### Live bot full output

```text
14:25:36  INFO      Mode: exits
14:25:36  INFO        Daily log -> logs/daily/2026-07-16.md
14:25:36  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (3 ledger rows)
14:25:36  INFO        place_all_stops: checking 4 positions...
14:25:36  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
14:25:36  INFO        STOP already live CARR @ $67.55
14:25:36  INFO        STOP skipped CASY: fractional (0.1169 shares) — software exit will handle it
14:25:36  INFO        STOP already live MO @ $71.9
14:25:36  INFO        [positions] 4/4 (4 valid)
14:25:37  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:25 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $484.00|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CASY  P&L -0.5%  $-0.48                                           HOLD|
|  MO  P&L +0.1%  $+0.13                                             HOLD|
|  CARR  P&L +1.0%  $+0.87                                           HOLD|
|  AME  P&L +1.1%  $+0.94                                            HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T10:25:37.907915-04:00 ===

[Run context]
Paper auth OK — equity $128011.99, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-16 10:25:42,892 INFO   EXIT [b41|c041_s173_w2_1005_1045_r3|S173] stop_loss (-64.7%) SELL 1 AMD260717C00567500 @<= 0.25
2026-07-16 10:25:43,635 INFO   EXIT [b49|c049_s165_w2_1005_1045_r3|S165] stop_loss (-52.1%) SELL 1 AVGO260717C00405000 @<= 0.26

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 95 signal(s); top: ['S173:APH', 'S173:ADI', 'S173:AMAT', 'S173:BLDR', 'S173:CAT', 'S173:FIX', 'S173:DELL', 'S173:ETN']
Paper lab: $128194 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  All bucket slots blocked or closed for today's signals — skip entry loop.
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $128,011.99                             |
|  Signals this run              95                                      |
|  Orders submitted (session)    12                                      |
|  Orders filled today (ledger)  21                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             26                                      |
|  Broker option positions       6                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=219  buckets=44  win=42%                             |
|  Returns   avg=+28.1%  med=-8.3%  p10=-77.0%  p90=+100.4%              |
|  Realized  $+5,700.77                                                  |
|  Raw incl dropped  trades=322  real=$+4,577.58                         |
|  Today     trades=9  avg=-0.8%  med=-50.0%  real=$-185.00              |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b62  c062_s173_w3_1045_  8  50% +511.3 +520.8 +1100.0 $    +97        |
|  b89  c089_s165_w2_1005_  2 100% +425.9 +425.9 +790.0 $   +113         |
|  b69  c069_s165_w2_1005_  3  67% +122.1 +200.0 +210.0 $    +17         |
|  b29  c029_s165_w2_1005_  2  50% +100.0 +100.0 +250.0 $    +20         |
|  b28  c028_s165_w1_0928_  5 100% +85.7 +94.1 +102.0 $   +221           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 36 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_  9   0% -62.2 -77.0 -98.5 $   -369       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (3)                                                     |
+------------------------------------------------------------------------+
|  b3   S173 ADBE260717C00240000 x1 stop_loss (-61.4%)                   |
|  b41  S173 AMD260717C00567500 x1 stop_loss (-64.7%)                    |
|  b49  S165 AVGO260717C00405000 x1 stop_loss (-52.1%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (6)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  ADBE260717C00240000           7    -81.8%   $   -252.00               |
|  AMD260717C00567500            4    -64.7%   $   -176.00               |
|  AVGO260717C00405000           8    -40.6%   $   -169.78               |
|  UAL260717C00122000            4    -47.7%   $   -124.00               |
|  AVGO260717C00400000           1    -20.5%   $    -15.00               |
|  AAL260717C00015000            1    +12.5%   $     +7.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=31.8s reconcile=2.65s cancel=0.02s manage=2.99s scan=25.83s entries=0.05s
STATUS: options_morning_bot run complete (PAPER) elapsed=31.8s. run=#4123 https://github.com/28twagg-ops/TradingBot/actions/runs/29506486469
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 9 buckets closed trades, $-185.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 6.8% (22/322)
```

---

## Run 20260716T143049Z

- UTC timestamp: `20260716T143049Z`
- GitHub run: [#4124](https://github.com/28twagg-ops/TradingBot/actions/runs/29506876977)
- Run id: `29506876977`
- Live bot: exit=`0`, duration=`6s`
- Options bot: exit=`0`, duration=`61s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T10:30:55.977119-04:00","date":"2026-07-16","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":59.6,"phases_s":{"reconcile":2.85,"cancel":0.12,"manage":10.04,"scan":45.93,"entries":0.13},"signals":95,"placed":0,"equity":128441.95,"open_positions":6,"pending_orders":0,"open_lots":24,"submitted_today":12,"filled_today":21,"unattributed_contracts":0,"top_signals":["S173:AMD","S173:APH","S173:ADI","S173:AMAT","S173:BLDR","S173:CAT","S173:FIX","S173:DELL"],"github_run":"4124","github_run_id":"29506876977","status":"ok"}
```

### Live bot full output

```text
14:30:50  INFO      Mode: exits
14:30:51  INFO        Daily log -> logs/daily/2026-07-16.md
14:30:51  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (3 ledger rows)
14:30:51  INFO        place_all_stops: checking 4 positions...
14:30:51  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
14:30:51  INFO        STOP already live CARR @ $67.55
14:30:51  INFO        STOP skipped CASY: fractional (0.1169 shares) — software exit will handle it
14:30:51  INFO        STOP already live MO @ $71.9
14:30:52  INFO        [positions] 4/4 (4 valid)
14:30:52  INFO        SELL MARKET [urgent] CASY closed
14:30:54  INFO        TX logged: SELL CASY  P&L -0.74%
14:30:55  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:30 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $483.25|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CASY  P&L -0.7%  $-0.71                        EXIT: stop_loss (-0.7%)|
|  MO  P&L -0.4%  $-0.42                                             HOLD|
|  CARR  P&L +1.1%  $+0.92                                           HOLD|
|  AME  P&L +1.1%  $+0.93                                            HOLD|
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
|  CASY                                        -0.74%  (threshold -0.50%)|
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
=== options_morning_bot (PAPER) 2026-07-16T10:30:55.977119-04:00 ===

[Run context]
Paper auth OK — equity $128441.95, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-16 10:31:07,101 INFO   EXIT [b1|c001_s173_w2_1005_1045_r1|S173] stop_loss (-60.3%) SELL 1 AMD260717C00567500 @<= 0.28

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 95 signal(s); top: ['S173:AMD', 'S173:APH', 'S173:ADI', 'S173:AMAT', 'S173:BLDR', 'S173:CAT', 'S173:FIX', 'S173:DELL']
Paper lab: $128029 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  All bucket slots blocked or closed for today's signals — skip entry loop.
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $128,441.95                             |
|  Signals this run              95                                      |
|  Orders submitted (session)    12                                      |
|  Orders filled today (ledger)  21                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             24                                      |
|  Broker option positions       6                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=221  buckets=44  win=42%                             |
|  Returns   avg=+27.3%  med=-9.2%  p10=-77.0%  p90=+100.0%              |
|  Realized  $+5,636.77                                                  |
|  Raw incl dropped  trades=324  real=$+4,513.58                         |
|  Today     trades=11  avg=-10.4%  med=-50.0%  real=$-249.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b62  c062_s173_w3_1045_  8  50% +511.3 +520.8 +1100.0 $    +97        |
|  b89  c089_s165_w2_1005_  2 100% +425.9 +425.9 +790.0 $   +113         |
|  b69  c069_s165_w2_1005_  3  67% +122.1 +200.0 +210.0 $    +17         |
|  b29  c029_s165_w2_1005_  2  50% +100.0 +100.0 +250.0 $    +20         |
|  b28  c028_s165_w1_0928_  5 100% +85.7 +94.1 +102.0 $   +221           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 36 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_  9   0% -62.2 -77.0 -98.5 $   -369       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b3   S173 ADBE260717C00240000 x1 stop_loss (-61.4%)                   |
|  b1   S173 AMD260717C00567500 x1 stop_loss (-60.3%)                    |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (6)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  ADBE260717C00240000           7    -81.8%   $   -252.00               |
|  AVGO260717C00405000           8    -48.3%   $   -201.78               |
|  AMD260717C00567500            3    -60.3%   $   -123.00               |
|  UAL260717C00122000            4    -29.2%   $    -76.00               |
|  AVGO260717C00400000           1    -20.5%   $    -15.00               |
|  AAL260717C00015000            1    +23.2%   $    +13.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=59.6s reconcile=2.85s cancel=0.12s manage=10.04s scan=45.93s entries=0.13s
STATUS: options_morning_bot run complete (PAPER) elapsed=59.6s. run=#4124 https://github.com/28twagg-ops/TradingBot/actions/runs/29506876977
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 11 buckets closed trades, $-249.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 6.8% (22/324)
```

---

## Run 20260716T143541Z

- UTC timestamp: `20260716T143541Z`
- GitHub run: [#4125](https://github.com/28twagg-ops/TradingBot/actions/runs/29507240435)
- Run id: `29507240435`
- Live bot: exit=`0`, duration=`5s`
- Options bot: exit=`0`, duration=`30s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T10:35:47.070168-04:00","date":"2026-07-16","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":28.9,"phases_s":{"reconcile":2.58,"cancel":0.02,"manage":1.81,"scan":23.96,"entries":0.06},"signals":94,"placed":0,"equity":128625.93,"open_positions":6,"pending_orders":0,"open_lots":23,"submitted_today":12,"filled_today":21,"unattributed_contracts":0,"top_signals":["S173:AMD","S173:APH","S173:ADI","S173:AMAT","S173:BLDR","S173:CAT","S173:FIX","S173:DELL"],"github_run":"4125","github_run_id":"29507240435","status":"ok"}
```

### Live bot full output

```text
14:35:43  INFO      Mode: exits
14:35:43  INFO        Daily log -> logs/daily/2026-07-16.md
14:35:43  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (4 ledger rows)
14:35:43  INFO        place_all_stops: checking 3 positions...
14:35:43  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
14:35:43  INFO        STOP already live CARR @ $67.55
14:35:43  INFO        STOP skipped MO: fractional (0.3388 shares) — software exit will handle it
14:35:43  INFO        [positions] 3/3 (3 valid)
14:35:43  INFO        SELL MARKET [urgent] MO closed
14:35:45  INFO        TX logged: SELL MO  P&L -0.58%
14:35:46  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:35 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.79|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MO  P&L -0.6%  $-0.14                          EXIT: stop_loss (-0.6%)|
|  AME  P&L +0.8%  $+0.72                                            HOLD|
|  CARR  P&L +1.0%  $+0.85                                           HOLD|
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
|  MO                                          -0.58%  (threshold -0.50%)|
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
=== options_morning_bot (PAPER) 2026-07-16T10:35:47.070168-04:00 ===

[Run context]
Paper auth OK — equity $128625.93, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-16 10:35:51,385 INFO   EXIT [b21|c021_s173_w2_1005_1045_r2|S173] stop_loss (-57.4%) SELL 1 AMD260717C00567500 @<= 0.26

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 94 signal(s); top: ['S173:AMD', 'S173:APH', 'S173:ADI', 'S173:AMAT', 'S173:BLDR', 'S173:CAT', 'S173:FIX', 'S173:DELL']
Paper lab: $128552 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  All bucket slots blocked or closed for today's signals — skip entry loop.
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $128,625.93                             |
|  Signals this run              94                                      |
|  Orders submitted (session)    12                                      |
|  Orders filled today (ledger)  21                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             23                                      |
|  Broker option positions       6                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=222  buckets=44  win=41%                             |
|  Returns   avg=+26.9%  med=-10.9%  p10=-77.0%  p90=+100.0%             |
|  Realized  $+5,597.77                                                  |
|  Raw incl dropped  trades=325  real=$+4,474.58                         |
|  Today     trades=12  avg=-14.3%  med=-51.4%  real=$-288.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b62  c062_s173_w3_1045_  8  50% +511.3 +520.8 +1100.0 $    +97        |
|  b89  c089_s165_w2_1005_  2 100% +425.9 +425.9 +790.0 $   +113         |
|  b69  c069_s165_w2_1005_  3  67% +122.1 +200.0 +210.0 $    +17         |
|  b29  c029_s165_w2_1005_  2  50% +100.0 +100.0 +250.0 $    +20         |
|  b28  c028_s165_w1_0928_  5 100% +85.7 +94.1 +102.0 $   +221           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 36 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_  9   0% -62.2 -77.0 -98.5 $   -369       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b3   S173 ADBE260717C00240000 x1 stop_loss (-61.4%)                   |
|  b21  S173 AMD260717C00567500 x1 stop_loss (-57.4%)                    |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (6)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  ADBE260717C00240000           7    -81.8%   $   -252.00               |
|  AVGO260717C00405000           8    -44.5%   $   -185.78               |
|  AMD260717C00567500            1    -57.4%   $    -39.00               |
|  UAL260717C00122000            4     -6.2%   $    -16.00               |
|  AVGO260717C00400000           1    -19.2%   $    -14.00               |
|  AAL260717C00015000            1    +19.6%   $    +11.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=28.9s reconcile=2.58s cancel=0.02s manage=1.81s scan=23.96s entries=0.06s
STATUS: options_morning_bot run complete (PAPER) elapsed=28.9s. run=#4125 https://github.com/28twagg-ops/TradingBot/actions/runs/29507240435
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 12 buckets closed trades, $-288.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 6.8% (22/325)
```

---

## Run 20260716T144041Z

- UTC timestamp: `20260716T144041Z`
- GitHub run: [#4126](https://github.com/28twagg-ops/TradingBot/actions/runs/29507625445)
- Run id: `29507625445`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`29s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T10:40:44.595381-04:00","date":"2026-07-16","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":27.0,"phases_s":{"reconcile":2.58,"cancel":0.02,"manage":1.99,"scan":22.14,"entries":0.05},"signals":94,"placed":0,"equity":127956.19,"open_positions":6,"pending_orders":0,"open_lots":22,"submitted_today":12,"filled_today":21,"unattributed_contracts":0,"top_signals":["S173:AMD","S173:APH","S173:ADI","S173:AMAT","S173:BLDR","S173:CAT","S173:FIX","S173:DELL"],"github_run":"4126","github_run_id":"29507625445","status":"ok"}
```

### Live bot full output

```text
14:40:43  INFO      Mode: exits
14:40:43  INFO        Daily log -> logs/daily/2026-07-16.md
14:40:43  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (5 ledger rows)
14:40:43  INFO        place_all_stops: checking 2 positions...
14:40:43  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
14:40:43  INFO        STOP already live CARR @ $67.55
14:40:43  INFO        [positions] 2/2 (2 valid)
14:40:43  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:40 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.60|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L +0.7%  $+0.63                                            HOLD|
|  CARR  P&L +0.9%  $+0.76                                           HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T10:40:44.595381-04:00 ===

[Run context]
Paper auth OK — equity $127956.19, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-16 10:40:49,262 INFO   EXIT [b21|c021_s173_w2_1005_1045_r2|S173] stop_loss (-57.4%) SELL 1 AMD260717C00567500 @<= 0.30

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 94 signal(s); top: ['S173:AMD', 'S173:APH', 'S173:ADI', 'S173:AMAT', 'S173:BLDR', 'S173:CAT', 'S173:FIX', 'S173:DELL']
Paper lab: $127937 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  All bucket slots blocked or closed for today's signals — skip entry loop.
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $127,956.19                             |
|  Signals this run              94                                      |
|  Orders submitted (session)    12                                      |
|  Orders filled today (ledger)  21                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             22                                      |
|  Broker option positions       6                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=223  buckets=44  win=41%                             |
|  Returns   avg=+26.6%  med=-12.5%  p10=-77.0%  p90=+100.0%             |
|  Realized  $+5,558.77                                                  |
|  Raw incl dropped  trades=326  real=$+4,435.58                         |
|  Today     trades=13  avg=-17.6%  med=-52.7%  real=$-327.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b62  c062_s173_w3_1045_  8  50% +511.3 +520.8 +1100.0 $    +97        |
|  b89  c089_s165_w2_1005_  2 100% +425.9 +425.9 +790.0 $   +113         |
|  b69  c069_s165_w2_1005_  3  67% +122.1 +200.0 +210.0 $    +17         |
|  b29  c029_s165_w2_1005_  2  50% +100.0 +100.0 +250.0 $    +20         |
|  b28  c028_s165_w1_0928_  5 100% +85.7 +94.1 +102.0 $   +221           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 36 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 10   0% -61.7 -75.5 -98.5 $   -408       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b3   S173 ADBE260717C00240000 x1 stop_loss (-61.4%)                   |
|  b21  S173 AMD260717C00567500 x1 stop_loss (-57.4%)                    |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (6)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  ADBE260717C00240000           7    -81.8%   $   -252.00               |
|  AVGO260717C00405000           8    -44.5%   $   -185.78               |
|  UAL260717C00122000            4    -43.1%   $   -112.00               |
|  AMD260717C00567500            1    -57.4%   $    -39.00               |
|  AVGO260717C00400000           1    -24.7%   $    -18.00               |
|  AAL260717C00015000            1    +21.4%   $    +12.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=27.0s reconcile=2.58s cancel=0.02s manage=1.99s scan=22.14s entries=0.05s
STATUS: options_morning_bot run complete (PAPER) elapsed=27.0s. run=#4126 https://github.com/28twagg-ops/TradingBot/actions/runs/29507625445
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 12 buckets closed trades, $-327.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 6.8% (22/326)
```

---

## Run 20260716T144536Z

- UTC timestamp: `20260716T144536Z`
- GitHub run: [#4127](https://github.com/28twagg-ops/TradingBot/actions/runs/29508000050)
- Run id: `29508000050`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`44s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T10:45:39.814917-04:00","date":"2026-07-16","mode":"entry+manage","header":"entry+manage (6 new)","elapsed_s":43.3,"phases_s":{"reconcile":2.57,"cancel":0.03,"manage":1.23,"scan":35.73,"entries":0.66,"reconcile2":2.56},"signals":93,"placed":6,"equity":128619.95,"open_positions":6,"pending_orders":6,"open_lots":21,"submitted_today":18,"filled_today":21,"unattributed_contracts":0,"top_signals":["S173:AMD","S173:APH","S173:ADI","S173:AMAT","S173:BLDR","S173:CAT","S173:FIX","S173:DELL"],"github_run":"4127","github_run_id":"29508000050","status":"ok"}
```

### Live bot full output

```text
14:45:38  INFO      Mode: exits
14:45:38  INFO        Daily log -> logs/daily/2026-07-16.md
14:45:38  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (5 ledger rows)
14:45:38  INFO        place_all_stops: checking 2 positions...
14:45:38  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
14:45:38  INFO        STOP already live CARR @ $67.55
14:45:38  INFO        [positions] 2/2 (2 valid)
14:45:39  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:45 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.75|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L +0.7%  $+0.58                                            HOLD|
|  CARR  P&L +1.1%  $+0.96                                           HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T10:45:39.814917-04:00 ===

[Run context]
Paper auth OK — equity $128619.95, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-16 10:45:43,941 INFO   EXIT [b0|c000_s173_w1_0928_1005_r1|S173] take_profit (+84.6%) SELL 1 UAL260717C00122000 @<= 1.21

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 93 signal(s); top: ['S173:AMD', 'S173:APH', 'S173:ADI', 'S173:AMAT', 'S173:BLDR', 'S173:CAT', 'S173:FIX', 'S173:DELL']
Paper lab: $128738 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 5 no tradeable call, 296 already attempted today, 234 pending order
Placed 6 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $128,619.95                             |
|  Signals this run              93                                      |
|  Orders submitted (session)    18                                      |
|  Orders filled today (ledger)  21                                      |
|  Entries placed this run       6                                       |
|  Open virtual lots             21                                      |
|  Broker option positions       6                                       |
|  Pending orders                6                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=224  buckets=44  win=42%                             |
|  Returns   avg=+26.8%  med=-10.9%  p10=-77.0%  p90=+100.0%             |
|  Realized  $+5,614.77                                                  |
|  Raw incl dropped  trades=327  real=$+4,491.58                         |
|  Today     trades=14  avg=-10.2%  med=-51.4%  real=$-271.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b62  c062_s173_w3_1045_  8  50% +511.3 +520.8 +1100.0 $    +97        |
|  b89  c089_s165_w2_1005_  2 100% +425.9 +425.9 +790.0 $   +113         |
|  b69  c069_s165_w2_1005_  3  67% +122.1 +200.0 +210.0 $    +17         |
|  b29  c029_s165_w2_1005_  2  50% +100.0 +100.0 +250.0 $    +20         |
|  b28  c028_s165_w1_0928_  5 100% +85.7 +94.1 +102.0 $   +221           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 36 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 10   0% -61.7 -75.5 -98.5 $   -408       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (6)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S165:AVGO(5), S173:AMD(1)               |
+------------------------------------------------------------------------+
|  b22  S173 AMD      limit=0.67                                         |
|  b10  S165 AVGO     limit=0.63                                         |
|  b30  S165 AVGO     limit=0.63                                         |
|  b50  S165 AVGO     limit=0.63                                         |
|  b70  S165 AVGO     limit=0.63                                         |
|  ... 1 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b3   S173 ADBE260717C00240000 x1 stop_loss (-61.4%)                   |
|  b21  S173 AMD260717C00567500 x1 stop_loss (-57.4%)                    |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (6)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  ADBE260717C00240000           7    -77.3%   $   -238.00               |
|  AVGO260717C00405000           8    -42.6%   $   -177.78               |
|  UAL260717C00122000            3    +78.5%   $   +153.00               |
|  AMD260717C00567500            1    -57.4%   $    -39.00               |
|  AAL260717C00015000            1    +25.0%   $    +14.00               |
|  AVGO260717C00400000           1    -17.8%   $    -13.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=43.3s reconcile=2.57s cancel=0.03s manage=1.23s scan=35.73s entries=0.66s
STATUS: options_morning_bot run complete (PAPER) elapsed=43.3s. run=#4127 https://github.com/28twagg-ops/TradingBot/actions/runs/29508000050
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 13 buckets closed trades, $-271.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 6.7% (22/327)
```

---

## Run 20260716T145040Z

- UTC timestamp: `20260716T145040Z`
- GitHub run: [#4128](https://github.com/28twagg-ops/TradingBot/actions/runs/29508391242)
- Run id: `29508391242`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`35s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T10:50:42.434759-04:00","date":"2026-07-16","mode":"entry+manage","header":"entry+manage (1 new)","elapsed_s":33.7,"phases_s":{"reconcile":3.52,"cancel":0.02,"manage":1.82,"scan":25.4,"entries":0.21,"reconcile2":2.58},"signals":95,"placed":1,"equity":128278.65,"open_positions":6,"pending_orders":1,"open_lots":26,"submitted_today":19,"filled_today":27,"unattributed_contracts":0,"top_signals":["S173:AMD","S173:APH","S173:ADI","S173:AMAT","S173:BLDR","S173:CAT","S173:FIX","S173:DELL"],"github_run":"4128","github_run_id":"29508391242","status":"ok"}
```

### Live bot full output

```text
14:50:41  INFO      Mode: exits
14:50:41  INFO        Daily log -> logs/daily/2026-07-16.md
14:50:41  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (5 ledger rows)
14:50:41  INFO        place_all_stops: checking 2 positions...
14:50:41  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
14:50:41  INFO        STOP already live CARR @ $67.55
14:50:41  INFO        [positions] 2/2 (2 valid)
14:50:41  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:50 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.85|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L +0.7%  $+0.60                                            HOLD|
|  CARR  P&L +1.2%  $+1.04                                           HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T10:50:42.434759-04:00 ===

[Run context]
Paper auth OK — equity $128278.65, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-16 10:50:46,214 INFO   EXIT [b80|c080_s173_w1_0928_1005_r5|S173] take_profit (+53.8%) SELL 1 UAL260717C00122000 @<= 1.01
2026-07-16 10:50:47,433 INFO   EXIT [b20|c020_s173_w1_0928_1005_r2|S173] take_profit (+62.5%) SELL 1 AAL260717C00015000 @<= 0.88

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 95 signal(s); top: ['S173:AMD', 'S173:APH', 'S173:ADI', 'S173:AMAT', 'S173:BLDR', 'S173:CAT', 'S173:FIX', 'S173:DELL']
Paper lab: $128086 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 56 pending order
Placed 1 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $128,278.65                             |
|  Signals this run              95                                      |
|  Orders submitted (session)    19                                      |
|  Orders filled today (ledger)  27                                      |
|  Entries placed this run       1                                       |
|  Open virtual lots             26                                      |
|  Broker option positions       6                                       |
|  Pending orders                1                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=225  buckets=44  win=42%                             |
|  Returns   avg=+27.0%  med=-9.2%  p10=-77.0%  p90=+100.0%              |
|  Realized  $+5,649.77                                                  |
|  Raw incl dropped  trades=328  real=$+4,526.58                         |
|  Today     trades=15  avg=-5.4%  med=-50.0%  real=$-236.00             |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b62  c062_s173_w3_1045_  8  50% +511.3 +520.8 +1100.0 $    +97        |
|  b89  c089_s165_w2_1005_  2 100% +425.9 +425.9 +790.0 $   +113         |
|  b69  c069_s165_w2_1005_  3  67% +122.1 +200.0 +210.0 $    +17         |
|  b29  c029_s165_w2_1005_  2  50% +100.0 +100.0 +250.0 $    +20         |
|  b28  c028_s165_w1_0928_  5 100% +85.7 +94.1 +102.0 $   +221           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 36 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 10   0% -61.7 -75.5 -98.5 $   -408       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (1)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S173:AMD(1)                             |
+------------------------------------------------------------------------+
|  b2   S173 AMD      limit=0.70                                         |
+========================================================================+
+========================================================================+
|  PENDING EXITS (3)                                                     |
+------------------------------------------------------------------------+
|  b3   S173 ADBE260717C00240000 x1 stop_loss (-61.4%)                   |
|  b21  S173 AMD260717C00567500 x1 stop_loss (-57.4%)                    |
|  b80  S173 UAL260717C00122000 x1 take_profit (+53.8%)                  |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (6)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  ADBE260717C00240000           7    -79.5%   $   -245.00               |
|  AVGO260717C00405000           8    -52.1%   $   -217.78               |
|  AVGO260717C00400000           6    -19.6%   $    -73.00               |
|  UAL260717C00122000            3    +36.9%   $    +72.00               |
|  AMD260717C00567500            1    -64.7%   $    -44.00               |
|  AMD260717C00557500            1    -35.8%   $    -24.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=33.7s reconcile=3.52s cancel=0.02s manage=1.82s scan=25.4s entries=0.21s
STATUS: options_morning_bot run complete (PAPER) elapsed=33.7s. run=#4128 https://github.com/28twagg-ops/TradingBot/actions/runs/29508391242
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 13 buckets closed trades, $-236.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 6.7% (22/328)
```

---

## Run 20260716T145549Z

- UTC timestamp: `20260716T145549Z`
- GitHub run: [#4129](https://github.com/28twagg-ops/TradingBot/actions/runs/29508758964)
- Run id: `29508758964`
- Live bot: exit=`0`, duration=`4s`
- Options bot: exit=`0`, duration=`42s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T10:55:53.973106-04:00","date":"2026-07-16","mode":"entry+manage","header":"entry+manage (1 new)","elapsed_s":40.7,"phases_s":{"reconcile":4.61,"cancel":0.12,"manage":8.56,"scan":18.5,"entries":2.91,"reconcile2":5.54},"signals":91,"placed":1,"equity":127700.73,"open_positions":7,"pending_orders":1,"open_lots":27,"submitted_today":20,"filled_today":28,"unattributed_contracts":0,"top_signals":["S173:ADI","S173:AMAT","S173:BLDR","S173:EME","S173:EMR","S173:GEV","S173:GNRC","S173:HUBB"],"github_run":"4129","github_run_id":"29508758964","status":"ok"}
```

### Live bot full output

```text
14:55:51  INFO      Mode: exits
14:55:52  INFO        Daily log -> logs/daily/2026-07-16.md
14:55:52  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (5 ledger rows)
14:55:52  INFO        place_all_stops: checking 2 positions...
14:55:52  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
14:55:52  INFO        STOP already live CARR @ $67.55
14:55:53  INFO        [positions] 2/2 (2 valid)
14:55:53  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:55 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.95|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L +0.9%  $+0.73                                            HOLD|
|  CARR  P&L +1.2%  $+1.01                                           HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T10:55:53.973106-04:00 ===

[Run context]
Paper auth OK — equity $127700.73, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-16 10:56:00,978 INFO   EXIT [b69|c069_s165_w2_1005_1045_r4|S165] stop_loss (-52.1%) SELL 1 AVGO260717C00405000 @<= 0.26

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 91 signal(s); top: ['S173:ADI', 'S173:AMAT', 'S173:BLDR', 'S173:EME', 'S173:EMR', 'S173:GEV', 'S173:GNRC', 'S173:HUBB']
Paper lab: $127752 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 10 no tradeable call, 31 pending order
Placed 1 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $127,700.73                             |
|  Signals this run              91                                      |
|  Orders submitted (session)    20                                      |
|  Orders filled today (ledger)  28                                      |
|  Entries placed this run       1                                       |
|  Open virtual lots             27                                      |
|  Broker option positions       7                                       |
|  Pending orders                1                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=225  buckets=44  win=42%                             |
|  Returns   avg=+27.0%  med=-9.2%  p10=-77.0%  p90=+100.0%              |
|  Realized  $+5,649.77                                                  |
|  Raw incl dropped  trades=328  real=$+4,526.58                         |
|  Today     trades=15  avg=-5.4%  med=-50.0%  real=$-236.00             |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b62  c062_s173_w3_1045_  8  50% +511.3 +520.8 +1100.0 $    +97        |
|  b89  c089_s165_w2_1005_  2 100% +425.9 +425.9 +790.0 $   +113         |
|  b69  c069_s165_w2_1005_  3  67% +122.1 +200.0 +210.0 $    +17         |
|  b29  c029_s165_w2_1005_  2  50% +100.0 +100.0 +250.0 $    +20         |
|  b28  c028_s165_w1_0928_  5 100% +85.7 +94.1 +102.0 $   +221           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 36 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 10   0% -61.7 -75.5 -98.5 $   -408       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (1)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S173:LULU(1)                            |
+------------------------------------------------------------------------+
|  b82  S173 LULU     limit=0.47                                         |
+========================================================================+
+========================================================================+
|  PENDING EXITS (4)                                                     |
+------------------------------------------------------------------------+
|  b3   S173 ADBE260717C00240000 x1 stop_loss (-61.4%)                   |
|  b21  S173 AMD260717C00567500 x1 stop_loss (-57.4%)                    |
|  b80  S173 UAL260717C00122000 x1 take_profit (+53.8%)                  |
|  b69  S165 AVGO260717C00405000 x1 stop_loss (-52.1%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (7)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  ADBE260717C00240000           7    -79.5%   $   -245.00               |
|  AVGO260717C00405000           8    -52.1%   $   -217.78               |
|  AVGO260717C00400000           6    -21.2%   $    -79.00               |
|  AMD260717C00567500            1    -70.6%   $    -48.00               |
|  AMD260717C00557500            1    -37.3%   $    -25.00               |
|  UAL260717C00122000            3     -7.7%   $    -15.00               |
|  AMD260717C00552500            1    -12.9%   $     -9.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=40.7s reconcile=4.61s cancel=0.12s manage=8.56s scan=18.5s entries=2.91s
STATUS: options_morning_bot run complete (PAPER) elapsed=40.7s. run=#4129 https://github.com/28twagg-ops/TradingBot/actions/runs/29508758964
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 13 buckets closed trades, $-236.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 6.7% (22/328)
```

---

## Run 20260716T150053Z

- UTC timestamp: `20260716T150053Z`
- GitHub run: [#4130](https://github.com/28twagg-ops/TradingBot/actions/runs/29509141651)
- Run id: `29509141651`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`57s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T11:00:56.548698-04:00","date":"2026-07-16","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":56.6,"phases_s":{"reconcile":2.67,"cancel":0.12,"manage":10.01,"scan":43.24,"entries":0.13},"signals":95,"placed":0,"equity":128317.67,"open_positions":7,"pending_orders":0,"open_lots":26,"submitted_today":20,"filled_today":29,"unattributed_contracts":0,"top_signals":["S173:AMD","S173:APH","S173:ADI","S173:AMAT","S173:BLDR","S173:CAT","S173:FIX","S173:EME"],"github_run":"4130","github_run_id":"29509141651","status":"ok"}
```

### Live bot full output

```text
15:00:54  INFO      Mode: exits
15:00:55  INFO        Daily log -> logs/daily/2026-07-16.md
15:00:55  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (5 ledger rows)
15:00:55  INFO        place_all_stops: checking 2 positions...
15:00:55  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
15:00:55  INFO        STOP already live CARR @ $67.55
15:00:55  INFO        [positions] 2/2 (2 valid)
15:00:56  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:00 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $483.15|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L +1.0%  $+0.82                                            HOLD|
|  CARR  P&L +1.3%  $+1.12                                           HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T11:00:56.548698-04:00 ===

[Run context]
Paper auth OK — equity $128317.67, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 95 signal(s); top: ['S173:AMD', 'S173:APH', 'S173:ADI', 'S173:AMAT', 'S173:BLDR', 'S173:CAT', 'S173:FIX', 'S173:EME']
Paper lab: $128049 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  All bucket slots blocked or closed for today's signals — skip entry loop.
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $128,317.67                             |
|  Signals this run              95                                      |
|  Orders submitted (session)    20                                      |
|  Orders filled today (ledger)  29                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             26                                      |
|  Broker option positions       7                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=226  buckets=44  win=42%                             |
|  Returns   avg=+26.6%  med=-10.9%  p10=-77.0%  p90=+100.0%             |
|  Realized  $+5,611.77                                                  |
|  Raw incl dropped  trades=329  real=$+4,488.58                         |
|  Today     trades=16  avg=-8.5%  med=-51.4%  real=$-274.00             |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b62  c062_s173_w3_1045_  8  50% +511.3 +520.8 +1100.0 $    +97        |
|  b89  c089_s165_w2_1005_  2 100% +425.9 +425.9 +790.0 $   +113         |
|  b69  c069_s165_w2_1005_  3  67% +122.1 +200.0 +210.0 $    +17         |
|  b29  c029_s165_w2_1005_  2  50% +100.0 +100.0 +250.0 $    +20         |
|  b28  c028_s165_w1_0928_  5 100% +85.7 +94.1 +102.0 $   +221           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 36 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 11   0% -61.2 -74.0 -98.5 $   -446       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b3   S173 ADBE260717C00240000 x1 stop_loss (-61.4%)                   |
|  b80  S173 UAL260717C00122000 x1 take_profit (+53.8%)                  |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (7)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  ADBE260717C00240000           7    -81.8%   $   -252.00               |
|  AVGO260717C00405000           7    -48.3%   $   -176.56               |
|  AVGO260717C00400000           6    -16.4%   $    -61.00               |
|  UAL260717C00122000            3     -7.7%   $    -15.00               |
|  LULU260717C00123000           1    -27.7%   $    -13.00               |
|  AMD260717C00552500            1    +15.7%   $    +11.00               |
|  AMD260717C00557500            1    -16.4%   $    -11.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=56.6s reconcile=2.67s cancel=0.12s manage=10.01s scan=43.24s entries=0.13s
STATUS: options_morning_bot run complete (PAPER) elapsed=56.6s. run=#4130 https://github.com/28twagg-ops/TradingBot/actions/runs/29509141651
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 13 buckets closed trades, $-274.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 6.7% (22/329)
```

---

## Run 20260716T150529Z

- UTC timestamp: `20260716T150529Z`
- GitHub run: [#4131](https://github.com/28twagg-ops/TradingBot/actions/runs/29509529017)
- Run id: `29509529017`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`41s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T11:05:32.678681-04:00","date":"2026-07-16","mode":"entry+manage","header":"entry+manage (1 new)","elapsed_s":40.1,"phases_s":{"reconcile":1.7,"cancel":0.13,"manage":4.06,"scan":31.01,"entries":0.88,"reconcile2":1.82},"signals":95,"placed":1,"equity":127699.67,"open_positions":7,"pending_orders":1,"open_lots":25,"submitted_today":21,"filled_today":29,"unattributed_contracts":0,"top_signals":["S173:AMD","S173:APH","S173:ADI","S173:AMAT","S173:BLDR","S173:CAT","S173:EME","S173:EMR"],"github_run":"4131","github_run_id":"29509529017","status":"ok"}
```

### Live bot full output

```text
15:05:30  INFO      Mode: exits
15:05:31  INFO        Daily log -> logs/daily/2026-07-16.md
15:05:31  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (5 ledger rows)
15:05:31  INFO        place_all_stops: checking 2 positions...
15:05:31  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
15:05:31  INFO        STOP already live CARR @ $67.55
15:05:31  INFO        [positions] 2/2 (2 valid)
15:05:32  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:05 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.94|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L +0.9%  $+0.76                                            HOLD|
|  CARR  P&L +1.2%  $+1.01                                           HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T11:05:32.678681-04:00 ===

[Run context]
Paper auth OK — equity $127699.67, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-16 11:05:36,868 INFO   EXIT [b89|c089_s165_w2_1005_1045_r5|S165] stop_loss (-52.1%) SELL 1 AVGO260717C00405000 @<= 0.22

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 95 signal(s); top: ['S173:AMD', 'S173:APH', 'S173:ADI', 'S173:AMAT', 'S173:BLDR', 'S173:CAT', 'S173:EME', 'S173:EMR']
Paper lab: $127419 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 51 pending order
Placed 1 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $127,699.67                             |
|  Signals this run              95                                      |
|  Orders submitted (session)    21                                      |
|  Orders filled today (ledger)  29                                      |
|  Entries placed this run       1                                       |
|  Open virtual lots             25                                      |
|  Broker option positions       7                                       |
|  Pending orders                1                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=228  buckets=44  win=41%                             |
|  Returns   avg=+26.0%  med=-12.5%  p10=-77.0%  p90=+100.0%             |
|  Realized  $+5,562.77                                                  |
|  Raw incl dropped  trades=331  real=$+4,439.58                         |
|  Today     trades=18  avg=-13.0%  med=-50.0%  real=$-323.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b62  c062_s173_w3_1045_  8  50% +511.3 +520.8 +1100.0 $    +97        |
|  b29  c029_s165_w2_1005_  2  50% +100.0 +100.0 +250.0 $    +20         |
|  b28  c028_s165_w1_0928_  5 100% +85.7 +94.1 +102.0 $   +221           |
|  b69  c069_s165_w2_1005_  4  50% +79.6 +78.2 +210.0 $     -7           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 36 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 11   0% -61.2 -74.0 -98.5 $   -446       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (1)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S173:AMD(1)                             |
+------------------------------------------------------------------------+
|  b42  S173 AMD      limit=0.69                                         |
+========================================================================+
+========================================================================+
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b3   S173 ADBE260717C00240000 x1 stop_loss (-61.4%)                   |
|  b80  S173 UAL260717C00122000 x1 take_profit (+53.8%)                  |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (7)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  ADBE260717C00240000           7    -79.5%   $   -245.00               |
|  AVGO260717C00405000           6    -54.0%   $   -169.33               |
|  AVGO260717C00400000           6    -27.6%   $   -103.00               |
|  UAL260717C00122000            3     -9.2%   $    -18.00               |
|  LULU260717C00123000           1    -31.9%   $    -15.00               |
|  AMD260717C00557500            1    -19.4%   $    -13.00               |
|  AMD260717C00552500            1     +1.4%   $     +1.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=40.1s reconcile=1.7s cancel=0.13s manage=4.06s scan=31.01s entries=0.88s
STATUS: options_morning_bot run complete (PAPER) elapsed=40.1s. run=#4131 https://github.com/28twagg-ops/TradingBot/actions/runs/29509529017
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 14 buckets closed trades, $-323.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 6.7% (22/331)
```

---

## Run 20260716T151039Z

- UTC timestamp: `20260716T151039Z`
- GitHub run: [#4132](https://github.com/28twagg-ops/TradingBot/actions/runs/29509909076)
- Run id: `29509909076`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`47s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T11:10:43.132481-04:00","date":"2026-07-16","mode":"entry+manage","header":"entry+manage (1 new)","elapsed_s":45.4,"phases_s":{"reconcile":2.84,"cancel":0.15,"manage":6.21,"scan":28.34,"entries":4.24,"reconcile2":2.82},"signals":91,"placed":1,"equity":127550.63,"open_positions":9,"pending_orders":0,"open_lots":26,"submitted_today":22,"filled_today":31,"unattributed_contracts":0,"top_signals":["S173:APH","S173:ADI","S173:AMAT","S173:BLDR","S173:CAT","S173:EME","S173:EMR","S173:GEV"],"github_run":"4132","github_run_id":"29509909076","status":"ok"}
```

### Live bot full output

```text
15:10:40  INFO      Mode: exits
15:10:41  INFO        Daily log -> logs/daily/2026-07-16.md
15:10:41  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (5 ledger rows)
15:10:41  INFO        place_all_stops: checking 2 positions...
15:10:41  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
15:10:41  INFO        STOP already live CARR @ $67.55
15:10:42  INFO        [positions] 2/2 (2 valid)
15:10:42  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.82|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L +0.9%  $+0.76                                            HOLD|
|  CARR  P&L +1.0%  $+0.85                                           HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T11:10:43.132481-04:00 ===

[Run context]
Paper auth OK — equity $127550.63, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-16 11:10:48,058 INFO   EXIT [b48|c048_s165_w1_0928_1005_r3|S165] stop_loss (-54.0%) SELL 1 AVGO260717C00405000 @<= 0.21

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 91 signal(s); top: ['S173:APH', 'S173:ADI', 'S173:AMAT', 'S173:BLDR', 'S173:CAT', 'S173:EME', 'S173:EMR', 'S173:GEV']
Paper lab: $127487 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 13 no tradeable call, 30 pending order
Placed 1 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $127,550.63                             |
|  Signals this run              91                                      |
|  Orders submitted (session)    22                                      |
|  Orders filled today (ledger)  31                                      |
|  Entries placed this run       1                                       |
|  Open virtual lots             26                                      |
|  Broker option positions       9                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=229  buckets=44  win=41%                             |
|  Returns   avg=+25.6%  med=-12.5%  p10=-77.0%  p90=+100.0%             |
|  Realized  $+5,531.77                                                  |
|  Raw incl dropped  trades=332  real=$+4,408.58                         |
|  Today     trades=19  avg=-15.3%  med=-50.0%  real=$-354.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b62  c062_s173_w3_1045_  8  50% +511.3 +520.8 +1100.0 $    +97        |
|  b29  c029_s165_w2_1005_  2  50% +100.0 +100.0 +250.0 $    +20         |
|  b28  c028_s165_w1_0928_  5 100% +85.7 +94.1 +102.0 $   +221           |
|  b69  c069_s165_w2_1005_  4  50% +79.6 +78.2 +210.0 $     -7           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 36 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 11   0% -61.2 -74.0 -98.5 $   -446       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b3   S173 ADBE260717C00240000 x1 stop_loss (-61.4%)                   |
|  b80  S173 UAL260717C00122000 x1 take_profit (+53.8%)                  |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (9)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  ADBE260717C00240000           7    -79.5%   $   -245.00               |
|  AVGO260717C00405000           5    -54.0%   $   -141.11               |
|  AVGO260717C00400000           6    -26.0%   $    -97.00               |
|  UAL260717C00122000            3    -21.5%   $    -42.00               |
|  AMD260717C00557500            1    -29.9%   $    -20.00               |
|  LULU260717C00123000           1    -31.9%   $    -15.00               |
|  LULU260717C00122000           1    -22.4%   $    -13.00               |
|  AMD260717C00555000            1    -17.6%   $    -12.00               |
|  ... 1 more position(s)                                                |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=45.4s reconcile=2.84s cancel=0.15s manage=6.21s scan=28.34s entries=4.24s
STATUS: options_morning_bot run complete (PAPER) elapsed=45.4s. run=#4132 https://github.com/28twagg-ops/TradingBot/actions/runs/29509909076
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 15 buckets closed trades, $-354.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 6.6% (22/332)
```

---

## Run 20260716T151547Z

- UTC timestamp: `20260716T151547Z`
- GitHub run: [#4133](https://github.com/28twagg-ops/TradingBot/actions/runs/29510285772)
- Run id: `29510285772`
- Live bot: exit=`0`, duration=`4s`
- Options bot: exit=`0`, duration=`52s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T11:15:52.798585-04:00","date":"2026-07-16","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":50.0,"phases_s":{"reconcile":10.48,"cancel":0.13,"manage":7.46,"scan":31.31,"entries":0.13},"signals":91,"placed":0,"equity":127400.59,"open_positions":9,"pending_orders":0,"open_lots":26,"submitted_today":22,"filled_today":31,"unattributed_contracts":0,"top_signals":["S173:ADI","S173:AMAT","S173:BLDR","S173:CAT","S173:EME","S173:EMR","S173:GEV","S173:GNRC"],"github_run":"4133","github_run_id":"29510285772","status":"ok"}
```

### Live bot full output

```text
15:15:49  INFO      Mode: exits
15:15:50  INFO        Daily log -> logs/daily/2026-07-16.md
15:15:50  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (5 ledger rows)
15:15:50  INFO        place_all_stops: checking 2 positions...
15:15:50  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
15:15:50  INFO        STOP already live CARR @ $67.55
15:15:51  INFO        [positions] 2/2 (2 valid)
15:15:51  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:15 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $483.06|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L +0.9%  $+0.77                                            HOLD|
|  CARR  P&L +1.2%  $+1.05                                           HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T11:15:52.798585-04:00 ===

[Run context]
Paper auth OK — equity $127400.59, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-16 11:16:05,321 INFO   EXIT [b69|c069_s165_w2_1005_1045_r4|S165] stop_loss (-57.9%) SELL 1 AVGO260717C00405000 @<= 0.19

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 91 signal(s); top: ['S173:ADI', 'S173:AMAT', 'S173:BLDR', 'S173:CAT', 'S173:EME', 'S173:EMR', 'S173:GEV', 'S173:GNRC']
Paper lab: $127204 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  All bucket slots blocked or closed for today's signals — skip entry loop.
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $127,400.59                             |
|  Signals this run              91                                      |
|  Orders submitted (session)    22                                      |
|  Orders filled today (ledger)  31                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             26                                      |
|  Broker option positions       9                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=229  buckets=44  win=41%                             |
|  Returns   avg=+25.6%  med=-12.5%  p10=-77.0%  p90=+100.0%             |
|  Realized  $+5,531.77                                                  |
|  Raw incl dropped  trades=332  real=$+4,408.58                         |
|  Today     trades=19  avg=-15.3%  med=-50.0%  real=$-354.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b62  c062_s173_w3_1045_  8  50% +511.3 +520.8 +1100.0 $    +97        |
|  b29  c029_s165_w2_1005_  2  50% +100.0 +100.0 +250.0 $    +20         |
|  b28  c028_s165_w1_0928_  5 100% +85.7 +94.1 +102.0 $   +221           |
|  b69  c069_s165_w2_1005_  4  50% +79.6 +78.2 +210.0 $     -7           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 36 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 11   0% -61.2 -74.0 -98.5 $   -446       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (3)                                                     |
+------------------------------------------------------------------------+
|  b3   S173 ADBE260717C00240000 x1 stop_loss (-61.4%)                   |
|  b80  S173 UAL260717C00122000 x1 take_profit (+53.8%)                  |
|  b69  S165 AVGO260717C00405000 x1 stop_loss (-57.9%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (9)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  ADBE260717C00240000           7    -79.5%   $   -245.00               |
|  AVGO260717C00400000           6    -32.4%   $   -121.00               |
|  AVGO260717C00405000           4    -57.9%   $   -120.89               |
|  UAL260717C00122000            3    -18.5%   $    -36.00               |
|  AMD260717C00557500            1    -41.8%   $    -28.00               |
|  AMD260717C00555000            1    -30.9%   $    -21.00               |
|  LULU260717C00123000           1    -31.9%   $    -15.00               |
|  AMD260717C00552500            1    -18.6%   $    -13.00               |
|  ... 1 more position(s)                                                |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=50.0s reconcile=10.48s cancel=0.13s manage=7.46s scan=31.31s entries=0.13s
STATUS: options_morning_bot run complete (PAPER) elapsed=50.0s. run=#4133 https://github.com/28twagg-ops/TradingBot/actions/runs/29510285772
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 15 buckets closed trades, $-354.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 6.6% (22/332)
```

---

## Run 20260716T152033Z

- UTC timestamp: `20260716T152033Z`
- GitHub run: [#4134](https://github.com/28twagg-ops/TradingBot/actions/runs/29510663393)
- Run id: `29510663393`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`41s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T11:20:37.209205-04:00","date":"2026-07-16","mode":"entry+manage","header":"entry+manage (7 new)","elapsed_s":39.7,"phases_s":{"reconcile":4.64,"cancel":0.05,"manage":5.14,"scan":24.02,"entries":2.62,"reconcile2":2.94},"signals":92,"placed":7,"equity":127630.57,"open_positions":9,"pending_orders":5,"open_lots":27,"submitted_today":29,"filled_today":33,"unattributed_contracts":0,"top_signals":["S173:APH","S173:ADI","S173:AMAT","S173:BLDR","S173:EME","S173:EMR","S173:GEV","S173:GNRC"],"github_run":"4134","github_run_id":"29510663393","status":"ok"}
```

### Live bot full output

```text
15:20:34  INFO      Mode: exits
15:20:36  INFO        Daily log -> logs/daily/2026-07-16.md
15:20:36  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (5 ledger rows)
15:20:36  INFO        place_all_stops: checking 2 positions...
15:20:36  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
15:20:36  INFO        STOP already live CARR @ $67.55
15:20:36  INFO        [positions] 2/2 (2 valid)
15:20:36  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.83|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L +0.8%  $+0.72                                            HOLD|
|  CARR  P&L +1.0%  $+0.90                                           HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T11:20:37.209205-04:00 ===

[Run context]
Paper auth OK — equity $127630.57, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-16 11:20:45,136 INFO   EXIT [b9|c009_s165_w2_1005_1045_r1|S165] stop_loss (-57.9%) SELL 1 AVGO260717C00405000 @<= 0.23

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 92 signal(s); top: ['S173:APH', 'S173:ADI', 'S173:AMAT', 'S173:BLDR', 'S173:EME', 'S173:EMR', 'S173:GEV', 'S173:GNRC']
Paper lab: $127561 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 24 no tradeable call, 300 pending order
Placed 7 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $127,630.57                             |
|  Signals this run              92                                      |
|  Orders submitted (session)    29                                      |
|  Orders filled today (ledger)  33                                      |
|  Entries placed this run       7                                       |
|  Open virtual lots             27                                      |
|  Broker option positions       9                                       |
|  Pending orders                5                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=230  buckets=44  win=41%                             |
|  Returns   avg=+25.3%  med=-12.5%  p10=-77.0%  p90=+100.0%             |
|  Realized  $+5,503.77                                                  |
|  Raw incl dropped  trades=333  real=$+4,380.58                         |
|  Today     trades=20  avg=-17.3%  med=-51.4%  real=$-382.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b62  c062_s173_w3_1045_  8  50% +511.3 +520.8 +1100.0 $    +97        |
|  b29  c029_s165_w2_1005_  2  50% +100.0 +100.0 +250.0 $    +20         |
|  b28  c028_s165_w1_0928_  5 100% +85.7 +94.1 +102.0 $   +221           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 36 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 11   0% -61.2 -74.0 -98.5 $   -446       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (5)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S165:AMD(5)                             |
+------------------------------------------------------------------------+
|  b11  S165 AMD      limit=0.73                                         |
|  b31  S165 AMD      limit=0.73                                         |
|  b51  S165 AMD      limit=0.73                                         |
|  b71  S165 AMD      limit=0.73                                         |
|  b91  S165 AMD      limit=0.73                                         |
+========================================================================+
+========================================================================+
|  PENDING EXITS (3)                                                     |
+------------------------------------------------------------------------+
|  b3   S173 ADBE260717C00240000 x1 stop_loss (-61.4%)                   |
|  b80  S173 UAL260717C00122000 x1 take_profit (+53.8%)                  |
|  b9   S165 AVGO260717C00405000 x1 stop_loss (-57.9%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (9)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  ADBE260717C00240000           7    -72.7%   $   -224.00               |
|  AVGO260717C00405000           4    -57.9%   $   -120.89               |
|  AVGO260717C00400000           6    -30.8%   $   -115.00               |
|  UAL260717C00122000            3    -33.8%   $    -66.00               |
|  LULU260717C00122000           3    -20.1%   $    -37.00               |
|  AMD260717C00557500            1    -37.3%   $    -25.00               |
|  AMD260717C00555000            1    -29.4%   $    -20.00               |
|  LULU260717C00123000           1    -29.8%   $    -14.00               |
|  ... 1 more position(s)                                                |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=39.7s reconcile=4.64s cancel=0.05s manage=5.14s scan=24.02s entries=2.62s
STATUS: options_morning_bot run complete (PAPER) elapsed=39.7s. run=#4134 https://github.com/28twagg-ops/TradingBot/actions/runs/29510663393
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 15 buckets closed trades, $-382.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 6.6% (22/333)
```

---

## Run 20260716T152348Z

- UTC timestamp: `20260716T152348Z`
- GitHub run: [#4135](https://github.com/28twagg-ops/TradingBot/actions/runs/29510902137)
- Run id: `29510902137`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`42s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T11:23:51.622830-04:00","date":"2026-07-16","mode":"entry+manage","header":"entry+manage (2 new)","elapsed_s":40.2,"phases_s":{"reconcile":2.79,"cancel":0.12,"manage":4.55,"scan":26.01,"entries":3.4,"reconcile2":2.78},"signals":91,"placed":2,"equity":127439.53,"open_positions":9,"pending_orders":7,"open_lots":27,"submitted_today":31,"filled_today":33,"unattributed_contracts":0,"top_signals":["S173:ADI","S173:AMAT","S173:BLDR","S173:EME","S173:EMR","S173:GEV","S173:GNRC","S173:HUBB"],"github_run":"4135","github_run_id":"29510902137","status":"ok"}
```

### Live bot full output

```text
15:23:49  INFO      Mode: exits
15:23:50  INFO        Daily log -> logs/daily/2026-07-16.md
15:23:50  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (5 ledger rows)
15:23:50  INFO        place_all_stops: checking 2 positions...
15:23:50  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
15:23:50  INFO        STOP already live CARR @ $67.55
15:23:50  INFO        [positions] 2/2 (2 valid)
15:23:50  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:23 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.80|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L +0.9%  $+0.74                                            HOLD|
|  CARR  P&L +1.0%  $+0.85                                           HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T11:23:51.622830-04:00 ===

[Run context]
Paper auth OK — equity $127479.53, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 91 signal(s); top: ['S173:ADI', 'S173:AMAT', 'S173:BLDR', 'S173:EME', 'S173:EMR', 'S173:GEV', 'S173:GNRC', 'S173:HUBB']
Paper lab: $127332 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 20 no tradeable call, 313 pending order
Placed 2 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $127,439.53                             |
|  Signals this run              91                                      |
|  Orders submitted (session)    31                                      |
|  Orders filled today (ledger)  33                                      |
|  Entries placed this run       2                                       |
|  Open virtual lots             27                                      |
|  Broker option positions       9                                       |
|  Pending orders                7                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=230  buckets=44  win=41%                             |
|  Returns   avg=+25.3%  med=-12.5%  p10=-77.0%  p90=+100.0%             |
|  Realized  $+5,503.77                                                  |
|  Raw incl dropped  trades=333  real=$+4,380.58                         |
|  Today     trades=20  avg=-17.3%  med=-51.4%  real=$-382.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b62  c062_s173_w3_1045_  8  50% +511.3 +520.8 +1100.0 $    +97        |
|  b29  c029_s165_w2_1005_  2  50% +100.0 +100.0 +250.0 $    +20         |
|  b28  c028_s165_w1_0928_  5 100% +85.7 +94.1 +102.0 $   +221           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 36 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 11   0% -61.2 -74.0 -98.5 $   -446       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (7)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S165:AMD(5), S173:LULU(2)               |
+------------------------------------------------------------------------+
|  b11  S165 AMD      limit=0.73                                         |
|  b31  S165 AMD      limit=0.73                                         |
|  b51  S165 AMD      limit=0.73                                         |
|  b71  S165 AMD      limit=0.73                                         |
|  b91  S165 AMD      limit=0.73                                         |
|  ... 2 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|  PENDING EXITS (3)                                                     |
+------------------------------------------------------------------------+
|  b3   S173 ADBE260717C00240000 x1 stop_loss (-61.4%)                   |
|  b80  S173 UAL260717C00122000 x1 take_profit (+53.8%)                  |
|  b9   S165 AVGO260717C00405000 x1 stop_loss (-57.9%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (9)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  ADBE260717C00240000           7    -72.7%   $   -224.00               |
|  AVGO260717C00400000           6    -34.0%   $   -127.00               |
|  AVGO260717C00405000           4    -59.8%   $   -124.89               |
|  UAL260717C00122000            3    -32.3%   $    -63.00               |
|  LULU260717C00122000           3    -16.8%   $    -31.00               |
|  AMD260717C00557500            1    -37.3%   $    -25.00               |
|  AMD260717C00555000            1    -25.0%   $    -17.00               |
|  LULU260717C00123000           1    -27.7%   $    -13.00               |
|  ... 1 more position(s)                                                |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=40.2s reconcile=2.79s cancel=0.12s manage=4.55s scan=26.01s entries=3.4s
STATUS: options_morning_bot run complete (PAPER) elapsed=40.2s. run=#4135 https://github.com/28twagg-ops/TradingBot/actions/runs/29510902137
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 15 buckets closed trades, $-382.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 6.6% (22/333)
```

---

## Run 20260716T152534Z

- UTC timestamp: `20260716T152534Z`
- GitHub run: [#4136](https://github.com/28twagg-ops/TradingBot/actions/runs/29511037869)
- Run id: `29511037869`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`40s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T11:25:36.509199-04:00","date":"2026-07-16","mode":"entry+manage","header":"entry+manage (1 new)","elapsed_s":38.2,"phases_s":{"reconcile":3.4,"cancel":0.02,"manage":3.67,"scan":27.29,"entries":1.12,"reconcile2":2.45},"signals":91,"placed":1,"equity":127713.47,"open_positions":9,"pending_orders":6,"open_lots":27,"submitted_today":32,"filled_today":35,"unattributed_contracts":0,"top_signals":["S173:ADI","S173:AMAT","S173:BLDR","S173:CAT","S173:EME","S173:EMR","S173:GEV","S173:GNRC"],"github_run":"4136","github_run_id":"29511037869","status":"ok"}
```

### Live bot full output

```text
15:25:34  INFO      Mode: exits
15:25:35  INFO        Daily log -> logs/daily/2026-07-16.md
15:25:35  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (5 ledger rows)
15:25:35  INFO        place_all_stops: checking 2 positions...
15:25:35  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
15:25:35  INFO        STOP already live CARR @ $67.55
15:25:35  INFO        [positions] 2/2 (2 valid)
15:25:35  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:25 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $483.00|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L +0.9%  $+0.77                                            HOLD|
|  CARR  P&L +1.2%  $+1.02                                           HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T11:25:36.509199-04:00 ===

[Run context]
Paper auth OK — equity $127713.47, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-16 11:25:42,059 INFO   EXIT [b88|c088_s165_w1_0928_1005_r5|S165] stop_loss (-57.9%) SELL 1 AVGO260717C00405000 @<= 0.19

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 91 signal(s); top: ['S173:ADI', 'S173:AMAT', 'S173:BLDR', 'S173:CAT', 'S173:EME', 'S173:EMR', 'S173:GEV', 'S173:GNRC']
Paper lab: $127736 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 12 no tradeable call, 274 pending order
Placed 1 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $127,713.47                             |
|  Signals this run              91                                      |
|  Orders submitted (session)    32                                      |
|  Orders filled today (ledger)  35                                      |
|  Entries placed this run       1                                       |
|  Open virtual lots             27                                      |
|  Broker option positions       9                                       |
|  Pending orders                6                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=231  buckets=44  win=41%                             |
|  Returns   avg=+24.9%  med=-12.5%  p10=-77.0%  p90=+100.0%             |
|  Realized  $+5,470.77                                                  |
|  Raw incl dropped  trades=334  real=$+4,347.58                         |
|  Today     trades=21  avg=-19.4%  med=-52.7%  real=$-415.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b62  c062_s173_w3_1045_  8  50% +511.3 +520.8 +1100.0 $    +97        |
|  b29  c029_s165_w2_1005_  2  50% +100.0 +100.0 +250.0 $    +20         |
|  b28  c028_s165_w1_0928_  5 100% +85.7 +94.1 +102.0 $   +221           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 36 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 11   0% -61.2 -74.0 -98.5 $   -446       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (6)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S165:AMD(5), S173:LULU(1)               |
+------------------------------------------------------------------------+
|  b11  S165 AMD      limit=0.73                                         |
|  b31  S165 AMD      limit=0.73                                         |
|  b51  S165 AMD      limit=0.73                                         |
|  b71  S165 AMD      limit=0.73                                         |
|  b91  S165 AMD      limit=0.73                                         |
|  ... 1 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b3   S173 ADBE260717C00240000 x1 stop_loss (-61.4%)                   |
|  b80  S173 UAL260717C00122000 x1 take_profit (+53.8%)                  |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (9)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  ADBE260717C00240000           7    -81.8%   $   -252.00               |
|  AVGO260717C00400000           6    -30.8%   $   -115.00               |
|  LULU260717C00122000           5    -24.5%   $    -73.00               |
|  UAL260717C00122000            3    -32.3%   $    -63.00               |
|  AVGO260717C00405000           2    -57.9%   $    -60.44               |
|  AMD260717C00557500            1    -37.3%   $    -25.00               |
|  LULU260717C00123000           1    -31.9%   $    -15.00               |
|  AMD260717C00555000            1    -19.1%   $    -13.00               |
|  ... 1 more position(s)                                                |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=38.2s reconcile=3.4s cancel=0.02s manage=3.67s scan=27.29s entries=1.12s
STATUS: options_morning_bot run complete (PAPER) elapsed=38.2s. run=#4136 https://github.com/28twagg-ops/TradingBot/actions/runs/29511037869
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 15 buckets closed trades, $-415.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 6.6% (22/334)
```

---

## Run 20260716T153039Z

- UTC timestamp: `20260716T153039Z`
- GitHub run: [#4137](https://github.com/28twagg-ops/TradingBot/actions/runs/29511411937)
- Run id: `29511411937`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`68s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T11:30:42.711105-04:00","date":"2026-07-16","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":66.1,"phases_s":{"reconcile":2.6,"cancel":0.06,"manage":8.07,"scan":52.32,"entries":0.09,"reconcile2":2.6},"signals":90,"placed":0,"equity":127603.61,"open_positions":9,"pending_orders":6,"open_lots":26,"submitted_today":32,"filled_today":35,"unattributed_contracts":0,"top_signals":["S173:ADI","S173:AMAT","S173:BLDR","S173:EME","S173:EMR","S173:GNRC","S173:HUBB","S173:JCI"],"github_run":"4137","github_run_id":"29511411937","status":"ok"}
```

### Live bot full output

```text
15:30:40  INFO      Mode: exits
15:30:41  INFO        Daily log -> logs/daily/2026-07-16.md
15:30:41  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (5 ledger rows)
15:30:41  INFO        place_all_stops: checking 2 positions...
15:30:41  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
15:30:41  INFO        STOP already live CARR @ $67.55
15:30:41  INFO        [positions] 2/2 (2 valid)
15:30:41  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:30 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.90|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L +0.8%  $+0.73                                            HOLD|
|  CARR  P&L +1.1%  $+0.96                                           HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T11:30:42.711105-04:00 ===

[Run context]
Paper auth OK — equity $127603.61, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-16 11:30:50,178 INFO   EXIT [b68|c068_s165_w1_0928_1005_r4|S165] stop_loss (-57.9%) SELL 1 AVGO260717C00405000 @<= 0.19
2026-07-16 11:30:52,158 INFO   EXIT [b82|c082_s173_w3_1045_1120_r5|S173] stop_loss (-51.1%) SELL 1 LULU260717C00123000 @<= 0.24

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 90 signal(s); top: ['S173:ADI', 'S173:AMAT', 'S173:BLDR', 'S173:EME', 'S173:EMR', 'S173:GNRC', 'S173:HUBB', 'S173:JCI']
Paper lab: $127882 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  All bucket slots blocked or closed for today's signals — skip entry loop.
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $127,603.61                             |
|  Signals this run              90                                      |
|  Orders submitted (session)    32                                      |
|  Orders filled today (ledger)  35                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             26                                      |
|  Broker option positions       9                                       |
|  Pending orders                6                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=232  buckets=44  win=41%                             |
|  Returns   avg=+24.5%  med=-13.1%  p10=-76.7%  p90=+99.7%              |
|  Realized  $+5,437.77                                                  |
|  Raw incl dropped  trades=335  real=$+4,314.58                         |
|  Today     trades=22  avg=-21.2%  med=-54.3%  real=$-448.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b62  c062_s173_w3_1045_  8  50% +511.3 +520.8 +1100.0 $    +97        |
|  b29  c029_s165_w2_1005_  2  50% +100.0 +100.0 +250.0 $    +20         |
|  b28  c028_s165_w1_0928_  5 100% +85.7 +94.1 +102.0 $   +221           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 36 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 11   0% -61.2 -74.0 -98.5 $   -446       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (6)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S165:AMD(5), S173:LULU(1)               |
+------------------------------------------------------------------------+
|  b11  S165 AMD      limit=0.73                                         |
|  b31  S165 AMD      limit=0.73                                         |
|  b51  S165 AMD      limit=0.73                                         |
|  b71  S165 AMD      limit=0.73                                         |
|  b91  S165 AMD      limit=0.73                                         |
|  ... 1 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|  PENDING EXITS (3)                                                     |
+------------------------------------------------------------------------+
|  b3   S173 ADBE260717C00240000 x1 stop_loss (-61.4%)                   |
|  b80  S173 UAL260717C00122000 x1 take_profit (+53.8%)                  |
|  b82  S173 LULU260717C00123000 x1 stop_loss (-51.1%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (9)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  ADBE260717C00240000           7    -81.8%   $   -252.00               |
|  AVGO260717C00400000           6    -29.2%   $   -109.00               |
|  LULU260717C00122000           5    -21.1%   $    -63.00               |
|  UAL260717C00122000            3    +24.6%   $    +48.00               |
|  AVGO260717C00405000           1    -57.9%   $    -30.22               |
|  AMD260717C00557500            1    -35.8%   $    -24.00               |
|  LULU260717C00123000           1    -51.1%   $    -24.00               |
|  AMD260717C00555000            1    -22.1%   $    -15.00               |
|  ... 1 more position(s)                                                |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=66.1s reconcile=2.6s cancel=0.06s manage=8.07s scan=52.32s entries=0.09s
STATUS: options_morning_bot run complete (PAPER) elapsed=66.1s. run=#4137 https://github.com/28twagg-ops/TradingBot/actions/runs/29511411937
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 16 buckets closed trades, $-448.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 6.6% (22/335)
```

---

## Run 20260716T153533Z

- UTC timestamp: `20260716T153533Z`
- GitHub run: [#4138](https://github.com/28twagg-ops/TradingBot/actions/runs/29511799235)
- Run id: `29511799235`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`47s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T11:35:36.257522-04:00","date":"2026-07-16","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":45.8,"phases_s":{"reconcile":3.45,"cancel":0.07,"manage":4.58,"scan":34.79,"entries":0.1,"reconcile2":2.44},"signals":90,"placed":0,"equity":128047.41,"open_positions":8,"pending_orders":6,"open_lots":25,"submitted_today":32,"filled_today":35,"unattributed_contracts":0,"top_signals":["S173:ADI","S173:AMAT","S173:BLDR","S173:CAT","S173:EME","S173:EMR","S173:GNRC","S173:HUBB"],"github_run":"4138","github_run_id":"29511799235","status":"ok"}
```

### Live bot full output

```text
15:35:34  INFO      Mode: exits
15:35:35  INFO        Daily log -> logs/daily/2026-07-16.md
15:35:35  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (5 ledger rows)
15:35:35  INFO        place_all_stops: checking 2 positions...
15:35:35  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
15:35:35  INFO        STOP already live CARR @ $67.55
15:35:35  INFO        [positions] 2/2 (2 valid)
15:35:35  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:35 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $483.34|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L +1.0%  $+0.84                                            HOLD|
|  CARR  P&L +1.5%  $+1.29                                           HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T11:35:36.257522-04:00 ===

[Run context]
Paper auth OK — equity $128047.41, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-16 11:35:43,311 INFO   EXIT [b28|c028_s165_w1_0928_1005_r2|S165] stop_loss (-56.0%) SELL 1 AVGO260717C00405000 @<= 0.24

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 90 signal(s); top: ['S173:ADI', 'S173:AMAT', 'S173:BLDR', 'S173:CAT', 'S173:EME', 'S173:EMR', 'S173:GNRC', 'S173:HUBB']
Paper lab: $127913 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  All bucket slots blocked or closed for today's signals — skip entry loop.
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $128,047.41                             |
|  Signals this run              90                                      |
|  Orders submitted (session)    32                                      |
|  Orders filled today (ledger)  35                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             25                                      |
|  Broker option positions       8                                       |
|  Pending orders                6                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=233  buckets=44  win=40%                             |
|  Returns   avg=+24.2%  med=-13.6%  p10=-76.4%  p90=+99.3%              |
|  Realized  $+5,415.77                                                  |
|  Raw incl dropped  trades=336  real=$+4,292.58                         |
|  Today     trades=23  avg=-22.3%  med=-52.7%  real=$-470.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b62  c062_s173_w3_1045_  8  50% +511.3 +520.8 +1100.0 $    +97        |
|  b29  c029_s165_w2_1005_  2  50% +100.0 +100.0 +250.0 $    +20         |
|  b28  c028_s165_w1_0928_  5 100% +85.7 +94.1 +102.0 $   +221           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 36 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 11   0% -61.2 -74.0 -98.5 $   -446       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (6)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S165:AMD(5), S173:LULU(1)               |
+------------------------------------------------------------------------+
|  b11  S165 AMD      limit=0.73                                         |
|  b31  S165 AMD      limit=0.73                                         |
|  b51  S165 AMD      limit=0.73                                         |
|  b71  S165 AMD      limit=0.73                                         |
|  b91  S165 AMD      limit=0.73                                         |
|  ... 1 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|  PENDING EXITS (3)                                                     |
+------------------------------------------------------------------------+
|  b3   S173 ADBE260717C00240000 x1 stop_loss (-61.4%)                   |
|  b80  S173 UAL260717C00122000 x1 take_profit (+53.8%)                  |
|  b28  S165 AVGO260717C00405000 x1 stop_loss (-56.0%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (8)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  ADBE260717C00240000           7    -81.8%   $   -252.00               |
|  AVGO260717C00400000           6    -26.0%   $    -97.00               |
|  LULU260717C00122000           5    -21.1%   $    -63.00               |
|  AVGO260717C00405000           1    -56.0%   $    -29.22               |
|  AMD260717C00557500            1    -35.8%   $    -24.00               |
|  AMD260717C00555000            1    -22.1%   $    -15.00               |
|  AMD260717C00552500            1    -10.0%   $     -7.00               |
|  UAL260717C00122000            3     +1.5%   $     +3.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=45.8s reconcile=3.45s cancel=0.07s manage=4.58s scan=34.79s entries=0.1s
STATUS: options_morning_bot run complete (PAPER) elapsed=45.8s. run=#4138 https://github.com/28twagg-ops/TradingBot/actions/runs/29511799235
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 17 buckets closed trades, $-470.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 6.6% (22/336)
```

---

## Run 20260716T154035Z

- UTC timestamp: `20260716T154035Z`
- GitHub run: [#4139](https://github.com/28twagg-ops/TradingBot/actions/runs/29512183512)
- Run id: `29512183512`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`10s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T11:40:38.427930-04:00","date":"2026-07-16","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":8.5,"phases_s":{"reconcile":2.57,"cancel":0.25,"manage":5.33},"signals":0,"placed":0,"equity":128279.39,"open_positions":7,"pending_orders":6,"open_lots":24,"submitted_today":32,"filled_today":35,"unattributed_contracts":0,"top_signals":[],"github_run":"4139","github_run_id":"29512183512","status":"ok"}
```

### Live bot full output

```text
15:40:36  INFO      Mode: exits
15:40:37  INFO        Daily log -> logs/daily/2026-07-16.md
15:40:37  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (5 ledger rows)
15:40:37  INFO        place_all_stops: checking 2 positions...
15:40:37  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
15:40:37  INFO        STOP already live CARR @ $67.55
15:40:37  INFO        [positions] 2/2 (2 valid)
15:40:37  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:40 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $483.04|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L +0.8%  $+0.70                                            HOLD|
|  CARR  P&L +1.3%  $+1.13                                           HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T11:40:38.427930-04:00 ===

[Run context]
Paper auth OK — equity $128279.39, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
Cancelled 6 unfilled LAB entry order(s).

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $128,279.39                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    32                                      |
|  Orders filled today (ledger)  35                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             24                                      |
|  Broker option positions       7                                       |
|  Pending orders                6                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=233  buckets=44  win=40%                             |
|  Returns   avg=+24.2%  med=-13.6%  p10=-76.4%  p90=+99.3%              |
|  Realized  $+5,415.77                                                  |
|  Raw incl dropped  trades=336  real=$+4,292.58                         |
|  Today     trades=23  avg=-22.3%  med=-52.7%  real=$-470.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b62  c062_s173_w3_1045_  8  50% +511.3 +520.8 +1100.0 $    +97        |
|  b29  c029_s165_w2_1005_  2  50% +100.0 +100.0 +250.0 $    +20         |
|  b28  c028_s165_w1_0928_  5 100% +85.7 +94.1 +102.0 $   +221           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 36 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 11   0% -61.2 -74.0 -98.5 $   -446       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (6)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S165:AMD(5), S173:LULU(1)               |
+------------------------------------------------------------------------+
|  b11  S165 AMD      limit=0.73                                         |
|  b31  S165 AMD      limit=0.73                                         |
|  b51  S165 AMD      limit=0.73                                         |
|  b71  S165 AMD      limit=0.73                                         |
|  b91  S165 AMD      limit=0.73                                         |
|  ... 1 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b3   S173 ADBE260717C00240000 x1 stop_loss (-61.4%)                   |
|  b80  S173 UAL260717C00122000 x1 take_profit (+53.8%)                  |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (7)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  ADBE260717C00240000           7    -79.5%   $   -245.00               |
|  AVGO260717C00400000           6    -22.8%   $    -85.00               |
|  LULU260717C00122000           5    -16.1%   $    -48.00               |
|  AMD260717C00557500            1    -35.8%   $    -24.00               |
|  UAL260717C00122000            3    +10.8%   $    +21.00               |
|  AMD260717C00555000            1    -22.1%   $    -15.00               |
|  AMD260717C00552500            1    -12.9%   $     -9.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=8.5s reconcile=2.57s cancel=0.25s manage=5.33s
STATUS: options_morning_bot run complete (PAPER) elapsed=8.5s. run=#4139 https://github.com/28twagg-ops/TradingBot/actions/runs/29512183512
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 17 buckets closed trades, $-470.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 6.6% (22/336)
```

---

## Run 20260716T154536Z

- UTC timestamp: `20260716T154536Z`
- GitHub run: [#4140](https://github.com/28twagg-ops/TradingBot/actions/runs/29512557228)
- Run id: `29512557228`
- Live bot: exit=`0`, duration=`4s`
- Options bot: exit=`0`, duration=`14s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T11:45:41.351361-04:00","date":"2026-07-16","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":12.3,"phases_s":{"reconcile":2.73,"cancel":0.24,"manage":8.3},"signals":0,"placed":0,"equity":127836.39,"open_positions":7,"pending_orders":0,"open_lots":24,"submitted_today":32,"filled_today":35,"unattributed_contracts":0,"top_signals":[],"github_run":"4140","github_run_id":"29512557228","status":"ok"}
```

### Live bot full output

```text
15:45:37  INFO      Mode: exits
15:45:39  INFO        Daily log -> logs/daily/2026-07-16.md
15:45:39  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (5 ledger rows)
15:45:39  INFO        place_all_stops: checking 2 positions...
15:45:39  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
15:45:39  INFO        STOP already live CARR @ $67.55
15:45:40  INFO        [positions] 2/2 (2 valid)
15:45:40  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:45 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $483.03|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L +0.7%  $+0.63                                            HOLD|
|  CARR  P&L +1.3%  $+1.13                                           HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T11:45:41.351361-04:00 ===

[Run context]
Paper auth OK — equity $127836.39, account PA36KS87UPRS

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
|  Equity                        $127,836.39                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    32                                      |
|  Orders filled today (ledger)  35                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             24                                      |
|  Broker option positions       7                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=233  buckets=44  win=40%                             |
|  Returns   avg=+24.2%  med=-13.6%  p10=-76.4%  p90=+99.3%              |
|  Realized  $+5,415.77                                                  |
|  Raw incl dropped  trades=336  real=$+4,292.58                         |
|  Today     trades=23  avg=-22.3%  med=-52.7%  real=$-470.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b62  c062_s173_w3_1045_  8  50% +511.3 +520.8 +1100.0 $    +97        |
|  b29  c029_s165_w2_1005_  2  50% +100.0 +100.0 +250.0 $    +20         |
|  b28  c028_s165_w1_0928_  5 100% +85.7 +94.1 +102.0 $   +221           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 36 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 11   0% -61.2 -74.0 -98.5 $   -446       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b3   S173 ADBE260717C00240000 x1 stop_loss (-61.4%)                   |
|  b80  S173 UAL260717C00122000 x1 take_profit (+53.8%)                  |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (7)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  ADBE260717C00240000           7    -72.7%   $   -224.00               |
|  AVGO260717C00400000           6    -19.6%   $    -73.00               |
|  LULU260717C00122000           5    -16.1%   $    -48.00               |
|  AMD260717C00557500            1    -38.8%   $    -26.00               |
|  AMD260717C00555000            1    -29.4%   $    -20.00               |
|  AMD260717C00552500            1    -14.3%   $    -10.00               |
|  UAL260717C00122000            3     +3.1%   $     +6.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=12.3s reconcile=2.73s cancel=0.24s manage=8.3s
STATUS: options_morning_bot run complete (PAPER) elapsed=12.3s. run=#4140 https://github.com/28twagg-ops/TradingBot/actions/runs/29512557228
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 17 buckets closed trades, $-470.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 6.6% (22/336)
```

---

## Run 20260716T155037Z

- UTC timestamp: `20260716T155037Z`
- GitHub run: [#4141](https://github.com/28twagg-ops/TradingBot/actions/runs/29512929296)
- Run id: `29512929296`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`10s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T11:50:41.556566-04:00","date":"2026-07-16","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":8.1,"phases_s":{"reconcile":2.65,"cancel":0.22,"manage":4.72},"signals":0,"placed":0,"equity":128077.63,"open_positions":7,"pending_orders":0,"open_lots":24,"submitted_today":32,"filled_today":35,"unattributed_contracts":0,"top_signals":[],"github_run":"4141","github_run_id":"29512929296","status":"ok"}
```

### Live bot full output

```text
15:50:38  INFO      Mode: exits
15:50:39  INFO        Daily log -> logs/daily/2026-07-16.md
15:50:39  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (5 ledger rows)
15:50:40  INFO        place_all_stops: checking 2 positions...
15:50:40  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
15:50:40  INFO        STOP already live CARR @ $67.55
15:50:40  INFO        [positions] 2/2 (2 valid)
15:50:40  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:50 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.79|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L +0.6%  $+0.55                                            HOLD|
|  CARR  P&L +1.2%  $+1.02                                           HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T11:50:41.556566-04:00 ===

[Run context]
Paper auth OK — equity $128077.63, account PA36KS87UPRS

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
|  Equity                        $128,077.63                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    32                                      |
|  Orders filled today (ledger)  35                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             24                                      |
|  Broker option positions       7                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=233  buckets=44  win=40%                             |
|  Returns   avg=+24.2%  med=-13.6%  p10=-76.4%  p90=+99.3%              |
|  Realized  $+5,415.77                                                  |
|  Raw incl dropped  trades=336  real=$+4,292.58                         |
|  Today     trades=23  avg=-22.3%  med=-52.7%  real=$-470.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b62  c062_s173_w3_1045_  8  50% +511.3 +520.8 +1100.0 $    +97        |
|  b29  c029_s165_w2_1005_  2  50% +100.0 +100.0 +250.0 $    +20         |
|  b28  c028_s165_w1_0928_  5 100% +85.7 +94.1 +102.0 $   +221           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 36 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 11   0% -61.2 -74.0 -98.5 $   -446       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b3   S173 ADBE260717C00240000 x1 stop_loss (-61.4%)                   |
|  b80  S173 UAL260717C00122000 x1 take_profit (+53.8%)                  |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (7)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  ADBE260717C00240000           7    -72.7%   $   -224.00               |
|  AVGO260717C00400000           6    -19.6%   $    -73.00               |
|  LULU260717C00122000           5    -24.5%   $    -73.00               |
|  UAL260717C00122000            3    -20.0%   $    -39.00               |
|  AMD260717C00557500            1    -43.3%   $    -29.00               |
|  AMD260717C00555000            1    -32.4%   $    -22.00               |
|  AMD260717C00552500            1    -21.4%   $    -15.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=8.1s reconcile=2.65s cancel=0.22s manage=4.72s
STATUS: options_morning_bot run complete (PAPER) elapsed=8.1s. run=#4141 https://github.com/28twagg-ops/TradingBot/actions/runs/29512929296
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 17 buckets closed trades, $-470.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 6.6% (22/336)
```

---

## Run 20260716T155534Z

- UTC timestamp: `20260716T155534Z`
- GitHub run: [#4142](https://github.com/28twagg-ops/TradingBot/actions/runs/29513301479)
- Run id: `29513301479`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`11s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T11:55:36.822795-04:00","date":"2026-07-16","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":10.4,"phases_s":{"reconcile":5.54,"cancel":0.09,"manage":4.19},"signals":0,"placed":0,"equity":127921.39,"open_positions":7,"pending_orders":0,"open_lots":24,"submitted_today":32,"filled_today":35,"unattributed_contracts":0,"top_signals":[],"github_run":"4142","github_run_id":"29513301479","status":"ok"}
```

### Live bot full output

```text
15:55:35  INFO      Mode: exits
15:55:35  INFO        Daily log -> logs/daily/2026-07-16.md
15:55:35  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (5 ledger rows)
15:55:35  INFO        place_all_stops: checking 2 positions...
15:55:35  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
15:55:35  INFO        STOP already live CARR @ $67.55
15:55:35  INFO        [positions] 2/2 (2 valid)
15:55:36  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:55 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $483.18|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L +0.9%  $+0.74                                            HOLD|
|  CARR  P&L +1.4%  $+1.23                                           HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T11:55:36.822795-04:00 ===

[Run context]
Paper auth OK — equity $127921.39, account PA36KS87UPRS

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
|  Equity                        $127,921.39                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    32                                      |
|  Orders filled today (ledger)  35                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             24                                      |
|  Broker option positions       7                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=233  buckets=44  win=40%                             |
|  Returns   avg=+24.2%  med=-13.6%  p10=-76.4%  p90=+99.3%              |
|  Realized  $+5,415.77                                                  |
|  Raw incl dropped  trades=336  real=$+4,292.58                         |
|  Today     trades=23  avg=-22.3%  med=-52.7%  real=$-470.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b62  c062_s173_w3_1045_  8  50% +511.3 +520.8 +1100.0 $    +97        |
|  b29  c029_s165_w2_1005_  2  50% +100.0 +100.0 +250.0 $    +20         |
|  b28  c028_s165_w1_0928_  5 100% +85.7 +94.1 +102.0 $   +221           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 36 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 11   0% -61.2 -74.0 -98.5 $   -446       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b3   S173 ADBE260717C00240000 x1 stop_loss (-61.4%)                   |
|  b80  S173 UAL260717C00122000 x1 take_profit (+53.8%)                  |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (7)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  ADBE260717C00240000           7    -72.7%   $   -224.00               |
|  LULU260717C00122000           5    -31.2%   $    -93.00               |
|  AVGO260717C00400000           6    -19.6%   $    -73.00               |
|  UAL260717C00122000            3    -16.9%   $    -33.00               |
|  AMD260717C00557500            1    -43.3%   $    -29.00               |
|  AMD260717C00555000            1    -30.9%   $    -21.00               |
|  AMD260717C00552500            1    -20.0%   $    -14.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=10.4s reconcile=5.54s cancel=0.09s manage=4.19s
STATUS: options_morning_bot run complete (PAPER) elapsed=10.4s. run=#4142 https://github.com/28twagg-ops/TradingBot/actions/runs/29513301479
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 17 buckets closed trades, $-470.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 6.6% (22/336)
```

---

## Run 20260716T160036Z

- UTC timestamp: `20260716T160036Z`
- GitHub run: [#4143](https://github.com/28twagg-ops/TradingBot/actions/runs/29513671994)
- Run id: `29513671994`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`19s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T12:00:39.957524-04:00","date":"2026-07-16","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":18.3,"phases_s":{"reconcile":2.45,"cancel":0.18,"manage":15.16},"signals":0,"placed":0,"equity":127835.39,"open_positions":7,"pending_orders":0,"open_lots":24,"submitted_today":32,"filled_today":35,"unattributed_contracts":0,"top_signals":[],"github_run":"4143","github_run_id":"29513671994","status":"ok"}
```

### Live bot full output

```text
16:00:37  INFO      Mode: exits
16:00:38  INFO        Daily log -> logs/daily/2026-07-16.md
16:00:38  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (5 ledger rows)
16:00:38  INFO        place_all_stops: checking 2 positions...
16:00:38  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
16:00:38  INFO        STOP already live CARR @ $67.55
16:00:38  INFO        [positions] 2/2 (2 valid)
16:00:39  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:00 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $483.22|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L +0.8%  $+0.67                                            HOLD|
|  CARR  P&L +1.6%  $+1.34                                           HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T12:00:39.957524-04:00 ===

[Run context]
Paper auth OK — equity $127835.39, account PA36KS87UPRS

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
|  Equity                        $127,835.39                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    32                                      |
|  Orders filled today (ledger)  35                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             24                                      |
|  Broker option positions       7                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=233  buckets=44  win=40%                             |
|  Returns   avg=+24.2%  med=-13.6%  p10=-76.4%  p90=+99.3%              |
|  Realized  $+5,415.77                                                  |
|  Raw incl dropped  trades=336  real=$+4,292.58                         |
|  Today     trades=23  avg=-22.3%  med=-52.7%  real=$-470.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b62  c062_s173_w3_1045_  8  50% +511.3 +520.8 +1100.0 $    +97        |
|  b29  c029_s165_w2_1005_  2  50% +100.0 +100.0 +250.0 $    +20         |
|  b28  c028_s165_w1_0928_  5 100% +85.7 +94.1 +102.0 $   +221           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 36 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 11   0% -61.2 -74.0 -98.5 $   -446       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b3   S173 ADBE260717C00240000 x1 stop_loss (-61.4%)                   |
|  b80  S173 UAL260717C00122000 x1 take_profit (+53.8%)                  |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (7)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  ADBE260717C00240000           7    -72.7%   $   -224.00               |
|  AVGO260717C00400000           6    -27.6%   $   -103.00               |
|  LULU260717C00122000           5    -27.9%   $    -83.00               |
|  AMD260717C00557500            1    -44.8%   $    -30.00               |
|  AMD260717C00555000            1    -32.4%   $    -22.00               |
|  AMD260717C00552500            1    -21.4%   $    -15.00               |
|  UAL260717C00122000            3     +0.0%   $     +0.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=18.3s reconcile=2.45s cancel=0.18s manage=15.16s
STATUS: options_morning_bot run complete (PAPER) elapsed=18.3s. run=#4143 https://github.com/28twagg-ops/TradingBot/actions/runs/29513671994
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 17 buckets closed trades, $-470.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 6.6% (22/336)
```

---

## Run 20260716T160537Z

- UTC timestamp: `20260716T160537Z`
- GitHub run: [#4144](https://github.com/28twagg-ops/TradingBot/actions/runs/29514050387)
- Run id: `29514050387`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`12s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T12:05:40.542924-04:00","date":"2026-07-16","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":10.1,"phases_s":{"reconcile":5.09,"cancel":0.19,"manage":4.3},"signals":0,"placed":0,"equity":127108.39,"open_positions":6,"pending_orders":0,"open_lots":24,"submitted_today":32,"filled_today":35,"unattributed_contracts":0,"top_signals":[],"github_run":"4144","github_run_id":"29514050387","status":"ok"}
```

### Live bot full output

```text
16:05:38  INFO      Mode: exits
16:05:39  INFO        Daily log -> logs/daily/2026-07-16.md
16:05:39  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (5 ledger rows)
16:05:39  INFO        place_all_stops: checking 2 positions...
16:05:39  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
16:05:39  INFO        STOP already live CARR @ $67.55
16:05:39  INFO        [positions] 2/2 (2 valid)
16:05:39  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:05 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $483.23|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L +0.8%  $+0.73                                            HOLD|
|  CARR  P&L +1.5%  $+1.29                                           HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T12:05:40.542924-04:00 ===

[Run context]
Paper auth OK — equity $127108.39, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-16 12:05:50,281 INFO   EXIT [b22|c022_s173_w3_1045_1120_r2|S173] stop_loss (-52.2%) SELL 1 AMD260717C00557500 @<= 0.28

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $127,108.39                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    32                                      |
|  Orders filled today (ledger)  35                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             24                                      |
|  Broker option positions       6                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=233  buckets=44  win=40%                             |
|  Returns   avg=+24.2%  med=-13.6%  p10=-76.4%  p90=+99.3%              |
|  Realized  $+5,415.77                                                  |
|  Raw incl dropped  trades=336  real=$+4,292.58                         |
|  Today     trades=23  avg=-22.3%  med=-52.7%  real=$-470.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b62  c062_s173_w3_1045_  8  50% +511.3 +520.8 +1100.0 $    +97        |
|  b29  c029_s165_w2_1005_  2  50% +100.0 +100.0 +250.0 $    +20         |
|  b28  c028_s165_w1_0928_  5 100% +85.7 +94.1 +102.0 $   +221           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 36 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 11   0% -61.2 -74.0 -98.5 $   -446       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (3)                                                     |
+------------------------------------------------------------------------+
|  b3   S173 ADBE260717C00240000 x1 stop_loss (-61.4%)                   |
|  b80  S173 UAL260717C00122000 x1 take_profit (+53.8%)                  |
|  b22  S173 AMD260717C00557500 x1 stop_loss (-52.2%)                    |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (6)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  ADBE260717C00240000           7    -72.7%   $   -224.00               |
|  AVGO260717C00400000           6    -35.7%   $   -133.00               |
|  LULU260717C00122000           5    -31.2%   $    -93.00               |
|  UAL260717C00122000            3    -32.3%   $    -63.00               |
|  AMD260717C00552500            1    -42.9%   $    -30.00               |
|  AMD260717C00555000            1    -44.1%   $    -30.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=10.1s reconcile=5.09s cancel=0.19s manage=4.3s
STATUS: options_morning_bot run complete (PAPER) elapsed=10.1s. run=#4144 https://github.com/28twagg-ops/TradingBot/actions/runs/29514050387
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 17 buckets closed trades, $-470.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 6.6% (22/336)
```

---

## Run 20260716T161043Z

- UTC timestamp: `20260716T161043Z`
- GitHub run: [#4145](https://github.com/28twagg-ops/TradingBot/actions/runs/29514410910)
- Run id: `29514410910`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`10s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T12:10:46.745409-04:00","date":"2026-07-16","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":8.7,"phases_s":{"reconcile":4.86,"cancel":0.11,"manage":3.3},"signals":0,"placed":0,"equity":127361.35,"open_positions":6,"pending_orders":0,"open_lots":22,"submitted_today":32,"filled_today":35,"unattributed_contracts":0,"top_signals":[],"github_run":"4145","github_run_id":"29514410910","status":"ok"}
```

### Live bot full output

```text
16:10:45  INFO      Mode: exits
16:10:45  INFO        Daily log -> logs/daily/2026-07-16.md
16:10:45  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (5 ledger rows)
16:10:45  INFO        place_all_stops: checking 2 positions...
16:10:45  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
16:10:45  INFO        STOP already live CARR @ $67.55
16:10:45  INFO        [positions] 2/2 (2 valid)
16:10:46  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $483.21|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L +0.8%  $+0.70                                            HOLD|
|  CARR  P&L +1.5%  $+1.30                                           HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T12:10:46.745409-04:00 ===

[Run context]
Paper auth OK — equity $127362.71, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-16 12:10:53,455 INFO   EXIT [b43|c043_s173_w4_1120_1135_r3|S173] stop_loss (-54.5%) SELL 1 ADBE260717C00240000 @<= 0.21

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $127,361.35                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    32                                      |
|  Orders filled today (ledger)  35                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             22                                      |
|  Broker option positions       6                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=235  buckets=44  win=40%                             |
|  Returns   avg=+23.5%  med=-13.8%  p10=-75.8%  p90=+98.7%              |
|  Realized  $+5,357.77                                                  |
|  Raw incl dropped  trades=338  real=$+4,234.58                         |
|  Today     trades=25  avg=-24.9%  med=-53.7%  real=$-528.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b62  c062_s173_w3_1045_  8  50% +511.3 +520.8 +1100.0 $    +97        |
|  b29  c029_s165_w2_1005_  2  50% +100.0 +100.0 +250.0 $    +20         |
|  b28  c028_s165_w1_0928_  5 100% +85.7 +94.1 +102.0 $   +221           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 36 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 11   0% -61.2 -74.0 -98.5 $   -446       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b80  S173 UAL260717C00122000 x1 take_profit (+53.8%)                  |
|  b43  S173 ADBE260717C00240000 x1 stop_loss (-54.5%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (6)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  ADBE260717C00240000           6    -56.8%   $   -150.00               |
|  AVGO260717C00400000           6    -34.0%   $   -127.00               |
|  UAL260717C00122000            3    -46.2%   $    -90.00               |
|  LULU260717C00122000           5    -24.5%   $    -73.00               |
|  AMD260717C00555000            1    -44.1%   $    -30.00               |
|  AMD260717C00552500            1    -37.1%   $    -26.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=8.7s reconcile=4.86s cancel=0.11s manage=3.3s
STATUS: options_morning_bot run complete (PAPER) elapsed=8.7s. run=#4145 https://github.com/28twagg-ops/TradingBot/actions/runs/29514410910
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 19 buckets closed trades, $-528.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 6.5% (22/338)
```

---

## Run 20260716T161532Z

- UTC timestamp: `20260716T161532Z`
- GitHub run: [#4146](https://github.com/28twagg-ops/TradingBot/actions/runs/29514778950)
- Run id: `29514778950`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`10s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T12:15:34.590880-04:00","date":"2026-07-16","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":8.6,"phases_s":{"reconcile":2.33,"cancel":0.03,"manage":5.98},"signals":0,"placed":0,"equity":127139.43,"open_positions":6,"pending_orders":0,"open_lots":22,"submitted_today":32,"filled_today":35,"unattributed_contracts":0,"top_signals":[],"github_run":"4146","github_run_id":"29514778950","status":"ok"}
```

### Live bot full output

```text
16:15:33  INFO      Mode: exits
16:15:33  INFO        Daily log -> logs/daily/2026-07-16.md
16:15:33  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (5 ledger rows)
16:15:33  INFO        place_all_stops: checking 2 positions...
16:15:33  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
16:15:33  INFO        STOP already live CARR @ $67.55
16:15:33  INFO        [positions] 2/2 (2 valid)
16:15:33  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:15 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $483.25|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L +0.8%  $+0.69                                            HOLD|
|  CARR  P&L +1.6%  $+1.36                                           HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T12:15:34.590880-04:00 ===

[Run context]
Paper auth OK — equity $127143.43, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-16 12:15:41,253 INFO   EXIT [b42|c042_s173_w3_1045_1120_r3|S173] stop_loss (-54.4%) SELL 1 AMD260717C00555000 @<= 0.32

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $127,139.43                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    32                                      |
|  Orders filled today (ledger)  35                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             22                                      |
|  Broker option positions       6                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=235  buckets=44  win=40%                             |
|  Returns   avg=+23.5%  med=-13.8%  p10=-75.8%  p90=+98.7%              |
|  Realized  $+5,357.77                                                  |
|  Raw incl dropped  trades=338  real=$+4,234.58                         |
|  Today     trades=25  avg=-24.9%  med=-53.7%  real=$-528.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b62  c062_s173_w3_1045_  8  50% +511.3 +520.8 +1100.0 $    +97        |
|  b29  c029_s165_w2_1005_  2  50% +100.0 +100.0 +250.0 $    +20         |
|  b28  c028_s165_w1_0928_  5 100% +85.7 +94.1 +102.0 $   +221           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 36 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 11   0% -61.2 -74.0 -98.5 $   -446       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (3)                                                     |
+------------------------------------------------------------------------+
|  b80  S173 UAL260717C00122000 x1 take_profit (+53.8%)                  |
|  b43  S173 ADBE260717C00240000 x1 stop_loss (-54.5%)                   |
|  b42  S173 AMD260717C00555000 x1 stop_loss (-54.4%)                    |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (6)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  ADBE260717C00240000           6    -59.1%   $   -156.00               |
|  AVGO260717C00400000           6    -32.4%   $   -121.00               |
|  UAL260717C00122000            3    -55.4%   $   -108.00               |
|  LULU260717C00122000           5    -29.5%   $    -88.00               |
|  AMD260717C00555000            1    -54.4%   $    -37.00               |
|  AMD260717C00552500            1    -42.9%   $    -30.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=8.6s reconcile=2.33s cancel=0.03s manage=5.98s
STATUS: options_morning_bot run complete (PAPER) elapsed=8.6s. run=#4146 https://github.com/28twagg-ops/TradingBot/actions/runs/29514778950
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 19 buckets closed trades, $-528.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 6.5% (22/338)
```

---

## Run 20260716T162039Z

- UTC timestamp: `20260716T162039Z`
- GitHub run: [#4147](https://github.com/28twagg-ops/TradingBot/actions/runs/29515125170)
- Run id: `29515125170`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`6s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T12:20:42.567235-04:00","date":"2026-07-16","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":4.1,"phases_s":{"reconcile":2.05,"cancel":0.08,"manage":1.68},"signals":0,"placed":0,"equity":127264.51,"open_positions":5,"pending_orders":0,"open_lots":20,"submitted_today":32,"filled_today":35,"unattributed_contracts":0,"top_signals":[],"github_run":"4147","github_run_id":"29515125170","status":"ok"}
```

### Live bot full output

```text
16:20:40  INFO      Mode: exits
16:20:41  INFO        Daily log -> logs/daily/2026-07-16.md
16:20:41  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (5 ledger rows)
16:20:41  INFO        place_all_stops: checking 2 positions...
16:20:41  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
16:20:41  INFO        STOP already live CARR @ $67.55
16:20:41  INFO        [positions] 2/2 (2 valid)
16:20:41  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $483.17|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L +0.8%  $+0.67                                            HOLD|
|  CARR  P&L +1.5%  $+1.29                                           HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T12:20:42.567235-04:00 ===

[Run context]
Paper auth OK — equity $127264.51, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-16 12:20:45,980 INFO   EXIT [b22|c022_s173_w3_1045_1120_r2|S173] stop_loss (-50.0%) SELL 1 ADBE260717C00240000 @<= 0.23

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $127,264.51                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    32                                      |
|  Orders filled today (ledger)  35                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             20                                      |
|  Broker option positions       5                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=237  buckets=45  win=40%                             |
|  Returns   avg=+22.9%  med=-14.6%  p10=-75.2%  p90=+98.0%              |
|  Realized  $+5,285.77                                                  |
|  Raw incl dropped  trades=340  real=$+4,162.58                         |
|  Today     trades=27  avg=-27.3%  med=-53.7%  real=$-600.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b62  c062_s173_w3_1045_  8  50% +511.3 +520.8 +1100.0 $    +97        |
|  b29  c029_s165_w2_1005_  2  50% +100.0 +100.0 +250.0 $    +20         |
|  b28  c028_s165_w1_0928_  5 100% +85.7 +94.1 +102.0 $   +221           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 37 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 11   0% -61.2 -74.0 -98.5 $   -446       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b80  S173 UAL260717C00122000 x1 take_profit (+53.8%)                  |
|  b22  S173 ADBE260717C00240000 x1 stop_loss (-50.0%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (5)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AVGO260717C00400000           6    -32.4%   $   -121.00               |
|  UAL260717C00122000            3    -58.5%   $   -114.00               |
|  ADBE260717C00240000           5    -50.0%   $   -110.00               |
|  LULU260717C00122000           5    -36.2%   $   -108.00               |
|  AMD260717C00552500            1    -47.1%   $    -33.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=4.1s reconcile=2.05s cancel=0.08s manage=1.68s
STATUS: options_morning_bot run complete (PAPER) elapsed=4.1s. run=#4147 https://github.com/28twagg-ops/TradingBot/actions/runs/29515125170
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 21 buckets closed trades, $-600.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 6.5% (22/340)
```

---

## Run 20260716T162533Z

- UTC timestamp: `20260716T162533Z`
- GitHub run: [#4148](https://github.com/28twagg-ops/TradingBot/actions/runs/29515470519)
- Run id: `29515470519`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`9s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T12:25:36.250590-04:00","date":"2026-07-16","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":7.4,"phases_s":{"reconcile":5.38,"cancel":0.06,"manage":1.7},"signals":0,"placed":0,"equity":127196.29,"open_positions":4,"pending_orders":0,"open_lots":19,"submitted_today":32,"filled_today":35,"unattributed_contracts":0,"top_signals":[],"github_run":"4148","github_run_id":"29515470519","status":"ok"}
```

### Live bot full output

```text
16:25:34  INFO      Mode: exits
16:25:35  INFO        Daily log -> logs/daily/2026-07-16.md
16:25:35  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (5 ledger rows)
16:25:35  INFO        place_all_stops: checking 2 positions...
16:25:35  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
16:25:35  INFO        STOP already live CARR @ $67.55
16:25:35  INFO        [positions] 2/2 (2 valid)
16:25:35  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:25 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.96|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L +0.5%  $+0.42                                            HOLD|
|  CARR  P&L +1.5%  $+1.33                                           HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T12:25:36.250590-04:00 ===

[Run context]
Paper auth OK — equity $127196.29, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-16 12:25:43,493 INFO   EXIT [b2|c002_s173_w3_1045_1120_r1|S173] stop_loss (-52.9%) SELL 1 AMD260717C00552500 @<= 0.30

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $127,196.29                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    32                                      |
|  Orders filled today (ledger)  35                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             19                                      |
|  Broker option positions       4                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=238  buckets=45  win=39%                             |
|  Returns   avg=+22.5%  med=-15.0%  p10=-74.9%  p90=+97.7%              |
|  Realized  $+5,260.77                                                  |
|  Raw incl dropped  trades=341  real=$+4,137.58                         |
|  Today     trades=28  avg=-28.2%  med=-53.3%  real=$-625.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b62  c062_s173_w3_1045_  8  50% +511.3 +520.8 +1100.0 $    +97        |
|  b29  c029_s165_w2_1005_  2  50% +100.0 +100.0 +250.0 $    +20         |
|  b28  c028_s165_w1_0928_  5 100% +85.7 +94.1 +102.0 $   +221           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 37 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 11   0% -61.2 -74.0 -98.5 $   -446       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b80  S173 UAL260717C00122000 x1 take_profit (+53.8%)                  |
|  b2   S173 AMD260717C00552500 x1 stop_loss (-52.9%)                    |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (4)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AVGO260717C00400000           6    -32.4%   $   -121.00               |
|  UAL260717C00122000            3    -55.4%   $   -108.00               |
|  LULU260717C00122000           5    -31.2%   $    -93.00               |
|  ADBE260717C00240000           4    -40.9%   $    -72.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=7.4s reconcile=5.38s cancel=0.06s manage=1.7s
STATUS: options_morning_bot run complete (PAPER) elapsed=7.4s. run=#4148 https://github.com/28twagg-ops/TradingBot/actions/runs/29515470519
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 21 buckets closed trades, $-625.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 6.5% (22/341)
```

---

## Run 20260716T163040Z

- UTC timestamp: `20260716T163040Z`
- GitHub run: [#4149](https://github.com/28twagg-ops/TradingBot/actions/runs/29515822521)
- Run id: `29515822521`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`9s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T12:30:43.650611-04:00","date":"2026-07-16","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":6.8,"phases_s":{"reconcile":2.45,"cancel":0.12,"manage":3.87},"signals":0,"placed":0,"equity":127446.27,"open_positions":4,"pending_orders":0,"open_lots":18,"submitted_today":32,"filled_today":35,"unattributed_contracts":0,"top_signals":[],"github_run":"4149","github_run_id":"29515822521","status":"ok"}
```

### Live bot full output

```text
16:30:41  INFO      Mode: exits
16:30:42  INFO        Daily log -> logs/daily/2026-07-16.md
16:30:42  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (5 ledger rows)
16:30:42  INFO        place_all_stops: checking 2 positions...
16:30:42  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
16:30:42  INFO        STOP already live CARR @ $67.55
16:30:42  INFO        [positions] 2/2 (2 valid)
16:30:42  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:30 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.94|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L +0.4%  $+0.38                                            HOLD|
|  CARR  P&L +1.6%  $+1.35                                           HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T12:30:43.650611-04:00 ===

[Run context]
Paper auth OK — equity $127446.27, account PA36KS87UPRS

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
|  Equity                        $127,446.27                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    32                                      |
|  Orders filled today (ledger)  35                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             18                                      |
|  Broker option positions       4                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=239  buckets=45  win=39%                             |
|  Returns   avg=+22.2%  med=-15.4%  p10=-74.6%  p90=+97.3%              |
|  Realized  $+5,223.77                                                  |
|  Raw incl dropped  trades=342  real=$+4,100.58                         |
|  Today     trades=29  avg=-29.1%  med=-52.9%  real=$-662.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b62  c062_s173_w3_1045_  8  50% +511.3 +520.8 +1100.0 $    +97        |
|  b29  c029_s165_w2_1005_  2  50% +100.0 +100.0 +250.0 $    +20         |
|  b28  c028_s165_w1_0928_  5 100% +85.7 +94.1 +102.0 $   +221           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 37 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 11   0% -61.2 -74.0 -98.5 $   -446       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b80  S173 UAL260717C00122000 x1 take_profit (+53.8%)                  |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (4)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AVGO260717C00400000           6    -35.7%   $   -133.00               |
|  UAL260717C00122000            3    -53.8%   $   -105.00               |
|  LULU260717C00122000           5    -31.2%   $    -93.00               |
|  ADBE260717C00240000           4    -36.4%   $    -64.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=6.8s reconcile=2.45s cancel=0.12s manage=3.87s
STATUS: options_morning_bot run complete (PAPER) elapsed=6.8s. run=#4149 https://github.com/28twagg-ops/TradingBot/actions/runs/29515822521
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 22 buckets closed trades, $-662.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 6.4% (22/342)
```

---

## Run 20260716T163644Z

- UTC timestamp: `20260716T163644Z`
- GitHub run: [#4150](https://github.com/28twagg-ops/TradingBot/actions/runs/29516183523)
- Run id: `29516183523`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`12s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T12:36:48.652221-04:00","date":"2026-07-16","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":10.8,"phases_s":{"reconcile":8.8,"cancel":0.14,"manage":1.41},"signals":0,"placed":0,"equity":127518.27,"open_positions":4,"pending_orders":0,"open_lots":18,"submitted_today":32,"filled_today":35,"unattributed_contracts":0,"top_signals":[],"github_run":"4150","github_run_id":"29516183523","status":"ok"}
```

### Live bot full output

```text
16:36:46  INFO      Mode: exits
16:36:47  INFO        Daily log -> logs/daily/2026-07-16.md
16:36:47  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (5 ledger rows)
16:36:47  INFO        place_all_stops: checking 2 positions...
16:36:47  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
16:36:47  INFO        STOP already live CARR @ $67.55
16:36:47  INFO        [positions] 2/2 (2 valid)
16:36:47  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $483.18|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L +0.6%  $+0.48                                            HOLD|
|  CARR  P&L +1.7%  $+1.49                                           HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T12:36:48.652221-04:00 ===

[Run context]
Paper auth OK — equity $127518.27, account PA36KS87UPRS

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
|  Equity                        $127,518.27                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    32                                      |
|  Orders filled today (ledger)  35                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             18                                      |
|  Broker option positions       4                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=239  buckets=45  win=39%                             |
|  Returns   avg=+22.2%  med=-15.4%  p10=-74.6%  p90=+97.3%              |
|  Realized  $+5,223.77                                                  |
|  Raw incl dropped  trades=342  real=$+4,100.58                         |
|  Today     trades=29  avg=-29.1%  med=-52.9%  real=$-662.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b62  c062_s173_w3_1045_  8  50% +511.3 +520.8 +1100.0 $    +97        |
|  b29  c029_s165_w2_1005_  2  50% +100.0 +100.0 +250.0 $    +20         |
|  b28  c028_s165_w1_0928_  5 100% +85.7 +94.1 +102.0 $   +221           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 37 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 11   0% -61.2 -74.0 -98.5 $   -446       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b80  S173 UAL260717C00122000 x1 take_profit (+53.8%)                  |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (4)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AVGO260717C00400000           6    -35.7%   $   -133.00               |
|  UAL260717C00122000            3    -46.2%   $    -90.00               |
|  LULU260717C00122000           5    -29.5%   $    -88.00               |
|  ADBE260717C00240000           4    -18.2%   $    -32.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=10.8s reconcile=8.8s cancel=0.14s manage=1.41s
STATUS: options_morning_bot run complete (PAPER) elapsed=10.8s. run=#4150 https://github.com/28twagg-ops/TradingBot/actions/runs/29516183523
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 22 buckets closed trades, $-662.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 6.4% (22/342)
```

---

## Run 20260716T164035Z

- UTC timestamp: `20260716T164035Z`
- GitHub run: [#4151](https://github.com/28twagg-ops/TradingBot/actions/runs/29516531779)
- Run id: `29516531779`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`8s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T12:40:39.428850-04:00","date":"2026-07-16","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":6.5,"phases_s":{"reconcile":4.32,"cancel":0.12,"manage":1.67},"signals":0,"placed":0,"equity":127444.27,"open_positions":4,"pending_orders":0,"open_lots":18,"submitted_today":32,"filled_today":35,"unattributed_contracts":0,"top_signals":[],"github_run":"4151","github_run_id":"29516531779","status":"ok"}
```

### Live bot full output

```text
16:40:37  INFO      Mode: exits
16:40:38  INFO        Daily log -> logs/daily/2026-07-16.md
16:40:38  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (5 ledger rows)
16:40:38  INFO        place_all_stops: checking 2 positions...
16:40:38  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
16:40:38  INFO        STOP already live CARR @ $67.55
16:40:38  INFO        [positions] 2/2 (2 valid)
16:40:38  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:40 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $483.32|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L +0.6%  $+0.54                                            HOLD|
|  CARR  P&L +1.8%  $+1.57                                           HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T12:40:39.428850-04:00 ===

[Run context]
Paper auth OK — equity $127444.27, account PA36KS87UPRS

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
|  Equity                        $127,444.27                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    32                                      |
|  Orders filled today (ledger)  35                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             18                                      |
|  Broker option positions       4                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=239  buckets=45  win=39%                             |
|  Returns   avg=+22.2%  med=-15.4%  p10=-74.6%  p90=+97.3%              |
|  Realized  $+5,223.77                                                  |
|  Raw incl dropped  trades=342  real=$+4,100.58                         |
|  Today     trades=29  avg=-29.1%  med=-52.9%  real=$-662.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b62  c062_s173_w3_1045_  8  50% +511.3 +520.8 +1100.0 $    +97        |
|  b29  c029_s165_w2_1005_  2  50% +100.0 +100.0 +250.0 $    +20         |
|  b28  c028_s165_w1_0928_  5 100% +85.7 +94.1 +102.0 $   +221           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 37 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 11   0% -61.2 -74.0 -98.5 $   -446       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b80  S173 UAL260717C00122000 x1 take_profit (+53.8%)                  |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (4)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AVGO260717C00400000           6    -34.0%   $   -127.00               |
|  UAL260717C00122000            3    -46.2%   $    -90.00               |
|  LULU260717C00122000           5    -29.5%   $    -88.00               |
|  ADBE260717C00240000           4    -15.9%   $    -28.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=6.5s reconcile=4.32s cancel=0.12s manage=1.67s
STATUS: options_morning_bot run complete (PAPER) elapsed=6.5s. run=#4151 https://github.com/28twagg-ops/TradingBot/actions/runs/29516531779
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 22 buckets closed trades, $-662.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 6.4% (22/342)
```

---

## Run 20260716T164537Z

- UTC timestamp: `20260716T164537Z`
- GitHub run: [#4152](https://github.com/28twagg-ops/TradingBot/actions/runs/29516886510)
- Run id: `29516886510`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`6s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T12:45:40.228820-04:00","date":"2026-07-16","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":4.3,"phases_s":{"reconcile":2.45,"cancel":0.08,"manage":1.5},"signals":0,"placed":0,"equity":127212.27,"open_positions":4,"pending_orders":0,"open_lots":18,"submitted_today":32,"filled_today":35,"unattributed_contracts":0,"top_signals":[],"github_run":"4152","github_run_id":"29516886510","status":"ok"}
```

### Live bot full output

```text
16:45:38  INFO      Mode: exits
16:45:39  INFO        Daily log -> logs/daily/2026-07-16.md
16:45:39  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (5 ledger rows)
16:45:39  INFO        place_all_stops: checking 2 positions...
16:45:39  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
16:45:39  INFO        STOP already live CARR @ $67.55
16:45:39  INFO        [positions] 2/2 (2 valid)
16:45:39  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:45 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $483.53|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L +0.8%  $+0.67                                            HOLD|
|  CARR  P&L +1.9%  $+1.64                                           HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T12:45:40.228820-04:00 ===

[Run context]
Paper auth OK — equity $127212.27, account PA36KS87UPRS

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
|  Equity                        $127,212.27                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    32                                      |
|  Orders filled today (ledger)  35                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             18                                      |
|  Broker option positions       4                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=239  buckets=45  win=39%                             |
|  Returns   avg=+22.2%  med=-15.4%  p10=-74.6%  p90=+97.3%              |
|  Realized  $+5,223.77                                                  |
|  Raw incl dropped  trades=342  real=$+4,100.58                         |
|  Today     trades=29  avg=-29.1%  med=-52.9%  real=$-662.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b62  c062_s173_w3_1045_  8  50% +511.3 +520.8 +1100.0 $    +97        |
|  b29  c029_s165_w2_1005_  2  50% +100.0 +100.0 +250.0 $    +20         |
|  b28  c028_s165_w1_0928_  5 100% +85.7 +94.1 +102.0 $   +221           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 37 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 11   0% -61.2 -74.0 -98.5 $   -446       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b80  S173 UAL260717C00122000 x1 take_profit (+53.8%)                  |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (4)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AVGO260717C00400000           6    -37.3%   $   -139.00               |
|  UAL260717C00122000            3    -44.6%   $    -87.00               |
|  LULU260717C00122000           5    -27.9%   $    -83.00               |
|  ADBE260717C00240000           4    -13.6%   $    -24.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=4.3s reconcile=2.45s cancel=0.08s manage=1.5s
STATUS: options_morning_bot run complete (PAPER) elapsed=4.3s. run=#4152 https://github.com/28twagg-ops/TradingBot/actions/runs/29516886510
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 22 buckets closed trades, $-662.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 6.4% (22/342)
```

---

## Run 20260716T164814Z

- UTC timestamp: `20260716T164814Z`
- GitHub run: [#4153](https://github.com/28twagg-ops/TradingBot/actions/runs/29517078035)
- Run id: `29517078035`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`6s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T12:48:17.693684-04:00","date":"2026-07-16","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":5.1,"phases_s":{"reconcile":2.58,"cancel":0.21,"manage":1.79},"signals":0,"placed":0,"equity":126978.27,"open_positions":4,"pending_orders":0,"open_lots":18,"submitted_today":32,"filled_today":35,"unattributed_contracts":0,"top_signals":[],"github_run":"4153","github_run_id":"29517078035","status":"ok"}
```

### Live bot full output

```text
16:48:15  INFO      Mode: exits
16:48:16  INFO        Daily log -> logs/daily/2026-07-16.md
16:48:16  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (5 ledger rows)
16:48:16  INFO        place_all_stops: checking 2 positions...
16:48:16  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
16:48:16  INFO        STOP already live CARR @ $67.55
16:48:16  INFO        [positions] 2/2 (2 valid)
16:48:16  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:48 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $483.51|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L +0.8%  $+0.68                                            HOLD|
|  CARR  P&L +1.9%  $+1.63                                           HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T12:48:17.693684-04:00 ===

[Run context]
Paper auth OK — equity $126978.27, account PA36KS87UPRS

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
|  Equity                        $126,978.27                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    32                                      |
|  Orders filled today (ledger)  35                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             18                                      |
|  Broker option positions       4                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=239  buckets=45  win=39%                             |
|  Returns   avg=+22.2%  med=-15.4%  p10=-74.6%  p90=+97.3%              |
|  Realized  $+5,223.77                                                  |
|  Raw incl dropped  trades=342  real=$+4,100.58                         |
|  Today     trades=29  avg=-29.1%  med=-52.9%  real=$-662.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b62  c062_s173_w3_1045_  8  50% +511.3 +520.8 +1100.0 $    +97        |
|  b29  c029_s165_w2_1005_  2  50% +100.0 +100.0 +250.0 $    +20         |
|  b28  c028_s165_w1_0928_  5 100% +85.7 +94.1 +102.0 $   +221           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 37 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 11   0% -61.2 -74.0 -98.5 $   -446       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b80  S173 UAL260717C00122000 x1 take_profit (+53.8%)                  |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (4)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AVGO260717C00400000           6    -43.7%   $   -163.00               |
|  UAL260717C00122000            3    -44.6%   $    -87.00               |
|  LULU260717C00122000           5    -27.9%   $    -83.00               |
|  ADBE260717C00240000           4     -4.5%   $     -8.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=5.1s reconcile=2.58s cancel=0.21s manage=1.79s
STATUS: options_morning_bot run complete (PAPER) elapsed=5.1s. run=#4153 https://github.com/28twagg-ops/TradingBot/actions/runs/29517078035
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 22 buckets closed trades, $-662.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 6.4% (22/342)
```

---

## Run 20260716T165036Z

- UTC timestamp: `20260716T165036Z`
- GitHub run: [#4154](https://github.com/28twagg-ops/TradingBot/actions/runs/29517237747)
- Run id: `29517237747`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`6s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T12:50:39.470366-04:00","date":"2026-07-16","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":4.1,"phases_s":{"reconcile":2.58,"cancel":0.08,"manage":1.12},"signals":0,"placed":0,"equity":127025.27,"open_positions":4,"pending_orders":0,"open_lots":18,"submitted_today":32,"filled_today":35,"unattributed_contracts":0,"top_signals":[],"github_run":"4154","github_run_id":"29517237747","status":"ok"}
```

### Live bot full output

```text
16:50:37  INFO      Mode: exits
16:50:38  INFO        Daily log -> logs/daily/2026-07-16.md
16:50:38  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (5 ledger rows)
16:50:38  INFO        place_all_stops: checking 2 positions...
16:50:38  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
16:50:38  INFO        STOP already live CARR @ $67.55
16:50:38  INFO        [positions] 2/2 (2 valid)
16:50:38  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:50 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $483.49|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L +0.8%  $+0.65                                            HOLD|
|  CARR  P&L +1.9%  $+1.63                                           HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T12:50:39.470366-04:00 ===

[Run context]
Paper auth OK — equity $127025.27, account PA36KS87UPRS

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
|  Equity                        $127,025.27                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    32                                      |
|  Orders filled today (ledger)  35                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             18                                      |
|  Broker option positions       4                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=239  buckets=45  win=39%                             |
|  Returns   avg=+22.2%  med=-15.4%  p10=-74.6%  p90=+97.3%              |
|  Realized  $+5,223.77                                                  |
|  Raw incl dropped  trades=342  real=$+4,100.58                         |
|  Today     trades=29  avg=-29.1%  med=-52.9%  real=$-662.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b62  c062_s173_w3_1045_  8  50% +511.3 +520.8 +1100.0 $    +97        |
|  b29  c029_s165_w2_1005_  2  50% +100.0 +100.0 +250.0 $    +20         |
|  b28  c028_s165_w1_0928_  5 100% +85.7 +94.1 +102.0 $   +221           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 37 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 11   0% -61.2 -74.0 -98.5 $   -446       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b80  S173 UAL260717C00122000 x1 take_profit (+53.8%)                  |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (4)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AVGO260717C00400000           6    -46.9%   $   -175.00               |
|  UAL260717C00122000            3    -41.5%   $    -81.00               |
|  LULU260717C00122000           5    -22.8%   $    -68.00               |
|  ADBE260717C00240000           4    +13.6%   $    +24.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=4.1s reconcile=2.58s cancel=0.08s manage=1.12s
STATUS: options_morning_bot run complete (PAPER) elapsed=4.1s. run=#4154 https://github.com/28twagg-ops/TradingBot/actions/runs/29517237747
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 22 buckets closed trades, $-662.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 6.4% (22/342)
```

---

## Run 20260716T165535Z

- UTC timestamp: `20260716T165535Z`
- GitHub run: [#4155](https://github.com/28twagg-ops/TradingBot/actions/runs/29517584880)
- Run id: `29517584880`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`6s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T12:55:39.374791-04:00","date":"2026-07-16","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":4.5,"phases_s":{"reconcile":3.05,"cancel":0.08,"manage":1.07},"signals":0,"placed":0,"equity":127027.27,"open_positions":4,"pending_orders":0,"open_lots":18,"submitted_today":32,"filled_today":35,"unattributed_contracts":0,"top_signals":[],"github_run":"4155","github_run_id":"29517584880","status":"ok"}
```

### Live bot full output

```text
16:55:37  INFO      Mode: exits
16:55:38  INFO        Daily log -> logs/daily/2026-07-16.md
16:55:38  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (5 ledger rows)
16:55:38  INFO        place_all_stops: checking 2 positions...
16:55:38  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
16:55:38  INFO        STOP already live CARR @ $67.55
16:55:38  INFO        [positions] 2/2 (2 valid)
16:55:38  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:55 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $483.82|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L +0.9%  $+0.79                                            HOLD|
|  CARR  P&L +2.1%  $+1.82                                           HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T12:55:39.374791-04:00 ===

[Run context]
Paper auth OK — equity $127003.27, account PA36KS87UPRS

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
|  Equity                        $127,027.27                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    32                                      |
|  Orders filled today (ledger)  35                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             18                                      |
|  Broker option positions       4                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=239  buckets=45  win=39%                             |
|  Returns   avg=+22.2%  med=-15.4%  p10=-74.6%  p90=+97.3%              |
|  Realized  $+5,223.77                                                  |
|  Raw incl dropped  trades=342  real=$+4,100.58                         |
|  Today     trades=29  avg=-29.1%  med=-52.9%  real=$-662.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b62  c062_s173_w3_1045_  8  50% +511.3 +520.8 +1100.0 $    +97        |
|  b29  c029_s165_w2_1005_  2  50% +100.0 +100.0 +250.0 $    +20         |
|  b28  c028_s165_w1_0928_  5 100% +85.7 +94.1 +102.0 $   +221           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 37 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 11   0% -61.2 -74.0 -98.5 $   -446       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b80  S173 UAL260717C00122000 x1 take_profit (+53.8%)                  |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (4)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AVGO260717C00400000           6    -45.3%   $   -169.00               |
|  LULU260717C00122000           5    -31.2%   $    -93.00               |
|  UAL260717C00122000            3    -40.0%   $    -78.00               |
|  ADBE260717C00240000           4    +34.1%   $    +60.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=4.5s reconcile=3.05s cancel=0.08s manage=1.07s
STATUS: options_morning_bot run complete (PAPER) elapsed=4.5s. run=#4155 https://github.com/28twagg-ops/TradingBot/actions/runs/29517584880
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 22 buckets closed trades, $-662.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 6.4% (22/342)
```

---

## Run 20260716T170039Z

- UTC timestamp: `20260716T170039Z`
- GitHub run: [#4156](https://github.com/28twagg-ops/TradingBot/actions/runs/29517935857)
- Run id: `29517935857`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`7s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T13:00:41.878190-04:00","date":"2026-07-16","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":6.0,"phases_s":{"reconcile":2.33,"cancel":0.09,"manage":3.28},"signals":0,"placed":0,"equity":126156.31,"open_positions":4,"pending_orders":0,"open_lots":18,"submitted_today":32,"filled_today":35,"unattributed_contracts":0,"top_signals":[],"github_run":"4156","github_run_id":"29517935857","status":"ok"}
```

### Live bot full output

```text
17:00:40  INFO      Mode: exits
17:00:40  INFO        Daily log -> logs/daily/2026-07-16.md
17:00:40  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (5 ledger rows)
17:00:40  INFO        place_all_stops: checking 2 positions...
17:00:40  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
17:00:40  INFO        STOP already live CARR @ $67.55
17:00:40  INFO        [positions] 2/2 (2 valid)
17:00:41  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:00 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $484.22|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L +1.3%  $+1.08                                            HOLD|
|  CARR  P&L +2.2%  $+1.92                                           HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T13:00:41.878190-04:00 ===

[Run context]
Paper auth OK — equity $126156.31, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-16 13:00:47,092 INFO   EXIT [b48|c048_s165_w1_0928_1005_r3|S165] stop_loss (-58.2%) SELL 1 AVGO260717C00400000 @<= 0.27

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $126,156.31                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    32                                      |
|  Orders filled today (ledger)  35                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             18                                      |
|  Broker option positions       4                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=239  buckets=45  win=39%                             |
|  Returns   avg=+22.2%  med=-15.4%  p10=-74.6%  p90=+97.3%              |
|  Realized  $+5,223.77                                                  |
|  Raw incl dropped  trades=342  real=$+4,100.58                         |
|  Today     trades=29  avg=-29.1%  med=-52.9%  real=$-662.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b62  c062_s173_w3_1045_  8  50% +511.3 +520.8 +1100.0 $    +97        |
|  b29  c029_s165_w2_1005_  2  50% +100.0 +100.0 +250.0 $    +20         |
|  b28  c028_s165_w1_0928_  5 100% +85.7 +94.1 +102.0 $   +221           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 37 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 11   0% -61.2 -74.0 -98.5 $   -446       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b80  S173 UAL260717C00122000 x1 take_profit (+53.8%)                  |
|  b48  S165 AVGO260717C00400000 x1 stop_loss (-58.2%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (4)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AVGO260717C00400000           6    -58.2%   $   -217.00               |
|  LULU260717C00122000           5    -46.3%   $   -138.00               |
|  UAL260717C00122000            3    -36.9%   $    -72.00               |
|  ADBE260717C00240000           4    +15.9%   $    +28.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=6.0s reconcile=2.33s cancel=0.09s manage=3.28s
STATUS: options_morning_bot run complete (PAPER) elapsed=6.0s. run=#4156 https://github.com/28twagg-ops/TradingBot/actions/runs/29517935857
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 22 buckets closed trades, $-662.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 6.4% (22/342)
```

---

## Run 20260716T170535Z

- UTC timestamp: `20260716T170535Z`
- GitHub run: [#4157](https://github.com/28twagg-ops/TradingBot/actions/runs/29518296900)
- Run id: `29518296900`
- Live bot: exit=`0`, duration=`4s`
- Options bot: exit=`0`, duration=`7s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T13:05:39.978213-04:00","date":"2026-07-16","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":6.1,"phases_s":{"reconcile":2.59,"cancel":0.22,"manage":2.8},"signals":0,"placed":0,"equity":126161.85,"open_positions":4,"pending_orders":0,"open_lots":17,"submitted_today":32,"filled_today":35,"unattributed_contracts":0,"top_signals":[],"github_run":"4157","github_run_id":"29518296900","status":"ok"}
```

### Live bot full output

```text
17:05:36  INFO      Mode: exits
17:05:38  INFO        Daily log -> logs/daily/2026-07-16.md
17:05:38  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (5 ledger rows)
17:05:38  INFO        place_all_stops: checking 2 positions...
17:05:38  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
17:05:38  INFO        STOP already live CARR @ $67.55
17:05:38  INFO        [positions] 2/2 (2 valid)
17:05:39  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:05 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $484.43|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L +1.4%  $+1.20                                            HOLD|
|  CARR  P&L +2.3%  $+2.01                                           HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T13:05:39.978213-04:00 ===

[Run context]
Paper auth OK — equity $126161.85, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-16 13:05:44,698 INFO   EXIT [b70|c070_s165_w3_1045_1120_r4|S165] stop_loss (-59.8%) SELL 1 AVGO260717C00400000 @<= 0.26
2026-07-16 13:05:45,904 INFO   EXIT [b62|c062_s173_w3_1045_1120_r4|S173] stop_loss (-59.7%) SELL 1 LULU260717C00122000 @<= 0.21

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $126,161.85                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    32                                      |
|  Orders filled today (ledger)  35                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             17                                      |
|  Broker option positions       4                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=240  buckets=45  win=39%                             |
|  Returns   avg=+21.9%  med=-15.6%  p10=-74.3%  p90=+97.0%              |
|  Realized  $+5,178.77                                                  |
|  Raw incl dropped  trades=343  real=$+4,055.58                         |
|  Today     trades=30  avg=-30.2%  med=-53.3%  real=$-707.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b62  c062_s173_w3_1045_  8  50% +511.3 +520.8 +1100.0 $    +97        |
|  b29  c029_s165_w2_1005_  2  50% +100.0 +100.0 +250.0 $    +20         |
|  b28  c028_s165_w1_0928_  5 100% +85.7 +94.1 +102.0 $   +221           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 37 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 11   0% -61.2 -74.0 -98.5 $   -446       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (3)                                                     |
+------------------------------------------------------------------------+
|  b80  S173 UAL260717C00122000 x1 take_profit (+53.8%)                  |
|  b70  S165 AVGO260717C00400000 x1 stop_loss (-59.8%)                   |
|  b62  S173 LULU260717C00122000 x1 stop_loss (-59.7%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (4)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AVGO260717C00400000           5    -59.8%   $   -185.83               |
|  LULU260717C00122000           4    -59.7%   $   -142.40               |
|  UAL260717C00122000            3    -16.9%   $    -33.00               |
|  ADBE260717C00240000           4    +15.9%   $    +28.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=6.1s reconcile=2.59s cancel=0.22s manage=2.8s
STATUS: options_morning_bot run complete (PAPER) elapsed=6.1s. run=#4157 https://github.com/28twagg-ops/TradingBot/actions/runs/29518296900
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 22 buckets closed trades, $-707.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 6.4% (22/343)
```

---

## Run 20260716T171054Z

- UTC timestamp: `20260716T171054Z`
- GitHub run: [#4158](https://github.com/28twagg-ops/TradingBot/actions/runs/29518641788)
- Run id: `29518641788`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`6s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T13:10:57.941744-04:00","date":"2026-07-16","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":5.1,"phases_s":{"reconcile":2.42,"cancel":0.18,"manage":2.02},"signals":0,"placed":0,"equity":126257.77,"open_positions":4,"pending_orders":0,"open_lots":15,"submitted_today":32,"filled_today":35,"unattributed_contracts":0,"top_signals":[],"github_run":"4158","github_run_id":"29518641788","status":"ok"}
```

### Live bot full output

```text
17:10:55  INFO      Mode: exits
17:10:56  INFO        Daily log -> logs/daily/2026-07-16.md
17:10:56  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (5 ledger rows)
17:10:56  INFO        place_all_stops: checking 2 positions...
17:10:56  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
17:10:56  INFO        STOP already live CARR @ $67.55
17:10:57  INFO        [positions] 2/2 (2 valid)
17:10:57  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $484.35|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L +1.4%  $+1.16                                            HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T13:10:57.941744-04:00 ===

[Run context]
Paper auth OK — equity $126257.77, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-16 13:11:02,478 INFO   EXIT [b10|c010_s165_w3_1045_1120_r1|S165] stop_loss (-59.8%) SELL 1 AVGO260717C00400000 @<= 0.22
2026-07-16 13:11:02,846 INFO   EXIT [b23|c023_s173_w4_1120_1135_r2|S173] stop_loss (-66.4%) SELL 1 LULU260717C00122000 @<= 0.17

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $126,257.77                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    32                                      |
|  Orders filled today (ledger)  35                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             15                                      |
|  Broker option positions       4                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=242  buckets=45  win=39%                             |
|  Returns   avg=+21.2%  med=-16.4%  p10=-73.7%  p90=+96.6%              |
|  Realized  $+5,110.77                                                  |
|  Raw incl dropped  trades=345  real=$+3,987.58                         |
|  Today     trades=32  avg=-31.9%  med=-54.4%  real=$-775.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b29  c029_s165_w2_1005_  2  50% +100.0 +100.0 +250.0 $    +20         |
|  b28  c028_s165_w1_0928_  5 100% +85.7 +94.1 +102.0 $   +221           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b99  c099_s163_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 37 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 11   0% -61.2 -74.0 -98.5 $   -446       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (3)                                                     |
+------------------------------------------------------------------------+
|  b80  S173 UAL260717C00122000 x1 take_profit (+53.8%)                  |
|  b10  S165 AVGO260717C00400000 x1 stop_loss (-59.8%)                   |
|  b23  S173 LULU260717C00122000 x1 stop_loss (-66.4%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (4)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  LULU260717C00122000           4    -66.4%   $   -158.40               |
|  AVGO260717C00400000           3    -59.8%   $   -111.50               |
|  UAL260717C00122000            3    -30.8%   $    -60.00               |
|  ADBE260717C00240000           4    +15.9%   $    +28.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=5.1s reconcile=2.42s cancel=0.18s manage=2.02s
STATUS: options_morning_bot run complete (PAPER) elapsed=5.1s. run=#4158 https://github.com/28twagg-ops/TradingBot/actions/runs/29518641788
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 23 buckets closed trades, $-775.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 6.4% (22/345)
```

---

## Run 20260716T171535Z

- UTC timestamp: `20260716T171535Z`
- GitHub run: [#4159](https://github.com/28twagg-ops/TradingBot/actions/runs/29518989793)
- Run id: `29518989793`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`5s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T13:15:38.601476-04:00","date":"2026-07-16","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":3.5,"phases_s":{"reconcile":2.22,"cancel":0.02,"manage":1.05},"signals":0,"placed":0,"equity":126204.17,"open_positions":4,"pending_orders":0,"open_lots":13,"submitted_today":32,"filled_today":35,"unattributed_contracts":0,"top_signals":[],"github_run":"4159","github_run_id":"29518989793","status":"ok"}
```

### Live bot full output

```text
17:15:37  INFO      Mode: exits
17:15:37  INFO        Daily log -> logs/daily/2026-07-16.md
17:15:37  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (5 ledger rows)
17:15:37  INFO        place_all_stops: checking 2 positions...
17:15:37  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
17:15:37  INFO        STOP already live CARR @ $67.55
17:15:37  INFO        [positions] 2/2 (2 valid)
17:15:37  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:15 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $484.50|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L +1.4%  $+1.20                                            HOLD|
|  CARR  P&L +2.4%  $+2.09                                           HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T13:15:38.601476-04:00 ===

[Run context]
Paper auth OK — equity $126204.17, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-16 13:15:41,431 INFO   EXIT [b62|c062_s173_w3_1045_1120_r4|S173] stop_loss (-66.4%) SELL 1 LULU260717C00122000 @<= 0.21
2026-07-16 13:15:41,940 INFO   EXIT [b50|c050_s165_w3_1045_1120_r3|S165] stop_loss (-59.8%) SELL 1 AVGO260717C00400000 @<= 0.26

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $126,204.17                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    32                                      |
|  Orders filled today (ledger)  35                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             13                                      |
|  Broker option positions       4                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=244  buckets=46  win=39%                             |
|  Returns   avg=+20.5%  med=-17.7%  p10=-73.1%  p90=+96.5%              |
|  Realized  $+5,032.77                                                  |
|  Raw incl dropped  trades=347  real=$+3,909.58                         |
|  Today     trades=34  avg=-33.7%  med=-55.4%  real=$-853.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b29  c029_s165_w2_1005_  2  50% +100.0 +100.0 +250.0 $    +20         |
|  b28  c028_s165_w1_0928_  5 100% +85.7 +94.1 +102.0 $   +221           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b99  c099_s163_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 38 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 11   0% -61.2 -74.0 -98.5 $   -446       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (3)                                                     |
+------------------------------------------------------------------------+
|  b80  S173 UAL260717C00122000 x1 take_profit (+53.8%)                  |
|  b62  S173 LULU260717C00122000 x1 stop_loss (-66.4%)                   |
|  b50  S165 AVGO260717C00400000 x1 stop_loss (-59.8%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (4)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  LULU260717C00122000           3    -66.4%   $   -118.80               |
|  AVGO260717C00400000           3    -59.8%   $   -111.50               |
|  UAL260717C00122000            3    -30.8%   $    -60.00               |
|  ADBE260717C00240000           4    +15.9%   $    +28.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=3.5s reconcile=2.22s cancel=0.02s manage=1.05s
STATUS: options_morning_bot run complete (PAPER) elapsed=3.5s. run=#4159 https://github.com/28twagg-ops/TradingBot/actions/runs/29518989793
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 25 buckets closed trades, $-853.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 6.3% (22/347)
```

---

## Run 20260716T172037Z

- UTC timestamp: `20260716T172037Z`
- GitHub run: [#4160](https://github.com/28twagg-ops/TradingBot/actions/runs/29519333491)
- Run id: `29519333491`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`6s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T13:20:40.347744-04:00","date":"2026-07-16","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":4.1,"phases_s":{"reconcile":1.94,"cancel":0.09,"manage":1.81},"signals":0,"placed":0,"equity":126055.13,"open_positions":4,"pending_orders":0,"open_lots":11,"submitted_today":32,"filled_today":55,"unattributed_contracts":0,"top_signals":[],"github_run":"4160","github_run_id":"29519333491","status":"ok"}
```

### Live bot full output

```text
17:20:38  INFO      Mode: exits
17:20:39  INFO        Daily log -> logs/daily/2026-07-16.md
17:20:39  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (5 ledger rows)
17:20:39  INFO        place_all_stops: checking 2 positions...
17:20:39  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
17:20:39  INFO        STOP already live CARR @ $67.55
17:20:39  INFO        [positions] 2/2 (2 valid)
17:20:39  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $484.55|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L +1.4%  $+1.18                                            HOLD|
|  CARR  P&L +2.5%  $+2.16                                           HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T13:20:40.347744-04:00 ===

[Run context]
Paper auth OK — equity $126055.13, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-16 13:20:43,090 INFO   EXIT [b63|c063_s173_w4_1120_1135_r4|S173] stop_loss (-58.1%) SELL 1 LULU260717C00122000 @<= 0.26
2026-07-16 13:20:44,339 INFO   EXIT [b90|c090_s165_w3_1045_1120_r5|S165] stop_loss (-59.8%) SELL 1 AVGO260717C00400000 @<= 0.26

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $126,055.13                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    32                                      |
|  Orders filled today (ledger)  55                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             11                                      |
|  Broker option positions       4                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=279  buckets=46  win=36%                             |
|  Returns   avg=+15.0%  med=-20.0%  p10=-77.0%  p90=+94.5%              |
|  Realized  $+4,366.77                                                  |
|  Raw incl dropped  trades=382  real=$+3,243.58                         |
|  Today     trades=43  avg=-40.7%  med=-56.4%  real=$-1,203.00          |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b28  c028_s165_w1_0928_  6 100% +85.1 +88.0 +102.0 $   +266           |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b99  c099_s163_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b89  c089_s165_w2_1005_  4  75% +220.0 +69.9 +790.0 $   +127          |
|  ... 38 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_ 13   0% -61.8 -74.0 -98.5 $   -536       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (3)                                                     |
+------------------------------------------------------------------------+
|  b80  S173 UAL260717C00122000 x1 take_profit (+53.8%)                  |
|  b63  S173 LULU260717C00122000 x1 stop_loss (-58.1%)                   |
|  b90  S165 AVGO260717C00400000 x1 stop_loss (-59.8%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (4)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  UAL260717C00122000            3    -44.6%   $    -87.00               |
|  AVGO260717C00400000           2    -59.8%   $    -74.33               |
|  LULU260717C00122000           2    -58.1%   $    -69.20               |
|  ADBE260717C00240000           4    +13.6%   $    +24.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=4.1s reconcile=1.94s cancel=0.09s manage=1.81s
STATUS: options_morning_bot run complete (PAPER) elapsed=4.1s. run=#4160 https://github.com/28twagg-ops/TradingBot/actions/runs/29519333491
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 26 buckets closed trades, $-1,203.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 5.8% (22/382)
```

---

## Run 20260716T172532Z

- UTC timestamp: `20260716T172532Z`
- GitHub run: [#4161](https://github.com/28twagg-ops/TradingBot/actions/runs/29519672073)
- Run id: `29519672073`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`4s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T13:25:35.149420-04:00","date":"2026-07-16","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":3.0,"phases_s":{"reconcile":2.45,"cancel":0.04,"manage":0.26},"signals":0,"placed":0,"equity":125990.53,"open_positions":4,"pending_orders":0,"open_lots":11,"submitted_today":32,"filled_today":55,"unattributed_contracts":0,"top_signals":[],"github_run":"4161","github_run_id":"29519672073","status":"ok"}
```

### Live bot full output

```text
17:25:33  INFO      Mode: exits
17:25:34  INFO        Daily log -> logs/daily/2026-07-16.md
17:25:34  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (5 ledger rows)
17:25:34  INFO        place_all_stops: checking 2 positions...
17:25:34  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
17:25:34  INFO        STOP already live CARR @ $67.55
17:25:34  INFO        [positions] 2/2 (2 valid)
17:25:34  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:25 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $484.16|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L +1.1%  $+0.94                                            HOLD|
|  CARR  P&L +2.3%  $+2.01                                           HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T13:25:35.149420-04:00 ===

[Run context]
Paper auth OK — equity $125990.53, account PA36KS87UPRS

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
|  Equity                        $125,990.53                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    32                                      |
|  Orders filled today (ledger)  55                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             11                                      |
|  Broker option positions       4                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=286  buckets=46  win=35%                             |
|  Returns   avg=+14.0%  med=-21.4%  p10=-77.0%  p90=+93.6%              |
|  Realized  $+4,249.77                                                  |
|  Raw incl dropped  trades=389  real=$+3,126.58                         |
|  Today     trades=43  avg=-40.7%  med=-56.4%  real=$-1,203.00          |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b28  c028_s165_w1_0928_  7 100% +85.4 +87.3 +102.0 $   +314           |
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
|  PENDING EXITS (3)                                                     |
+------------------------------------------------------------------------+
|  b80  S173 UAL260717C00122000 x1 take_profit (+53.8%)                  |
|  b63  S173 LULU260717C00122000 x1 stop_loss (-58.1%)                   |
|  b90  S165 AVGO260717C00400000 x1 stop_loss (-59.8%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (4)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  UAL260717C00122000            3    -44.6%   $    -87.00               |
|  AVGO260717C00400000           2    -61.4%   $    -76.33               |
|  LULU260717C00122000           2    -58.1%   $    -69.20               |
|  ADBE260717C00240000           4    -11.4%   $    -20.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=3.0s reconcile=2.45s cancel=0.04s manage=0.26s
STATUS: options_morning_bot run complete (PAPER) elapsed=3.0s. run=#4161 https://github.com/28twagg-ops/TradingBot/actions/runs/29519672073
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 26 buckets closed trades, $-1,203.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 5.7% (22/389)
```

---

## Run 20260716T173038Z

- UTC timestamp: `20260716T173038Z`
- GitHub run: [#4162](https://github.com/28twagg-ops/TradingBot/actions/runs/29520014894)
- Run id: `29520014894`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`7s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T13:30:42.512598-04:00","date":"2026-07-16","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":4.8,"phases_s":{"reconcile":2.67,"cancel":0.22,"manage":1.12},"signals":0,"placed":0,"equity":126374.09,"open_positions":4,"pending_orders":0,"open_lots":11,"submitted_today":32,"filled_today":55,"unattributed_contracts":0,"top_signals":[],"github_run":"4162","github_run_id":"29520014894","status":"ok"}
```

### Live bot full output

```text
17:30:39  INFO      Mode: exits
17:30:40  INFO        Daily log -> logs/daily/2026-07-16.md
17:30:40  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (5 ledger rows)
17:30:40  INFO        place_all_stops: checking 2 positions...
17:30:40  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
17:30:40  INFO        STOP already live CARR @ $67.55
17:30:41  INFO        [positions] 2/2 (2 valid)
17:30:41  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:30 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $484.15|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L +1.0%  $+0.87                                            HOLD|
|  CARR  P&L +2.4%  $+2.07                                           HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T13:30:42.512598-04:00 ===

[Run context]
Paper auth OK — equity $126374.09, account PA36KS87UPRS

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
|  Equity                        $126,374.09                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    32                                      |
|  Orders filled today (ledger)  55                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             11                                      |
|  Broker option positions       4                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=288  buckets=46  win=35%                             |
|  Returns   avg=+14.0%  med=-21.4%  p10=-77.0%  p90=+93.4%              |
|  Realized  $+4,274.77                                                  |
|  Raw incl dropped  trades=391  real=$+3,151.58                         |
|  Today     trades=43  avg=-40.7%  med=-56.4%  real=$-1,203.00          |
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
|  PENDING EXITS (3)                                                     |
+------------------------------------------------------------------------+
|  b80  S173 UAL260717C00122000 x1 take_profit (+53.8%)                  |
|  b63  S173 LULU260717C00122000 x1 stop_loss (-58.1%)                   |
|  b90  S165 AVGO260717C00400000 x1 stop_loss (-59.8%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (4)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  UAL260717C00122000            3    -43.1%   $    -84.00               |
|  AVGO260717C00400000           2    -63.0%   $    -78.33               |
|  LULU260717C00122000           2    -58.1%   $    -69.20               |
|  ADBE260717C00240000           4    +31.8%   $    +56.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=4.8s reconcile=2.67s cancel=0.22s manage=1.12s
STATUS: options_morning_bot run complete (PAPER) elapsed=4.8s. run=#4162 https://github.com/28twagg-ops/TradingBot/actions/runs/29520014894
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 26 buckets closed trades, $-1,203.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 5.6% (22/391)
```

---

## Run 20260716T173536Z

- UTC timestamp: `20260716T173536Z`
- GitHub run: [#4163](https://github.com/28twagg-ops/TradingBot/actions/runs/29520362465)
- Run id: `29520362465`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`7s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T13:35:39.186714-04:00","date":"2026-07-16","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":6.2,"phases_s":{"reconcile":3.92,"cancel":0.2,"manage":1.66},"signals":0,"placed":0,"equity":126134.11,"open_positions":4,"pending_orders":0,"open_lots":10,"submitted_today":32,"filled_today":55,"unattributed_contracts":0,"top_signals":[],"github_run":"4163","github_run_id":"29520362465","status":"ok"}
```

### Live bot full output

```text
17:35:37  INFO      Mode: exits
17:35:37  INFO        Daily log -> logs/daily/2026-07-16.md
17:35:37  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (5 ledger rows)
17:35:37  INFO        place_all_stops: checking 2 positions...
17:35:37  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
17:35:38  INFO        STOP already live CARR @ $67.55
17:35:38  INFO        [positions] 2/2 (2 valid)
17:35:38  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:35 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $484.06|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L +0.9%  $+0.77                                            HOLD|
|  CARR  P&L +2.4%  $+2.09                                           HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T13:35:39.186714-04:00 ===

[Run context]
Paper auth OK — equity $126134.11, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-16 13:35:45,255 INFO   EXIT [b48|c048_s165_w1_0928_1005_r3|S165] stop_loss (-61.4%) SELL 1 AVGO260717C00400000 @<= 0.25

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $126,134.11                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    32                                      |
|  Orders filled today (ledger)  55                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             10                                      |
|  Broker option positions       4                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=288  buckets=46  win=35%                             |
|  Returns   avg=+14.0%  med=-21.4%  p10=-77.0%  p90=+93.4%              |
|  Realized  $+4,274.77                                                  |
|  Raw incl dropped  trades=391  real=$+3,151.58                         |
|  Today     trades=43  avg=-40.7%  med=-56.4%  real=$-1,203.00          |
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
|  PENDING EXITS (3)                                                     |
+------------------------------------------------------------------------+
|  b80  S173 UAL260717C00122000 x1 take_profit (+53.8%)                  |
|  b63  S173 LULU260717C00122000 x1 stop_loss (-58.1%)                   |
|  b48  S165 AVGO260717C00400000 x1 stop_loss (-61.4%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (4)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  ADBE260717C00240000           4    +47.7%   $    +84.00               |
|  UAL260717C00122000            3    -36.9%   $    -72.00               |
|  LULU260717C00122000           2    -58.1%   $    -69.20               |
|  AVGO260717C00400000           1    -61.4%   $    -38.17               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=6.2s reconcile=3.92s cancel=0.2s manage=1.66s
STATUS: options_morning_bot run complete (PAPER) elapsed=6.2s. run=#4163 https://github.com/28twagg-ops/TradingBot/actions/runs/29520362465
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 26 buckets closed trades, $-1,203.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 5.6% (22/391)
```

---

## Run 20260716T174037Z

- UTC timestamp: `20260716T174037Z`
- GitHub run: [#4164](https://github.com/28twagg-ops/TradingBot/actions/runs/29520706579)
- Run id: `29520706579`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`6s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T13:40:40.676502-04:00","date":"2026-07-16","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":4.4,"phases_s":{"reconcile":2.44,"cancel":0.12,"manage":1.42},"signals":0,"placed":0,"equity":125769.05,"open_positions":3,"pending_orders":0,"open_lots":9,"submitted_today":32,"filled_today":55,"unattributed_contracts":0,"top_signals":[],"github_run":"4164","github_run_id":"29520706579","status":"ok"}
```

### Live bot full output

```text
17:40:38  INFO      Mode: exits
17:40:39  INFO        Daily log -> logs/daily/2026-07-16.md
17:40:39  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (5 ledger rows)
17:40:39  INFO        place_all_stops: checking 2 positions...
17:40:39  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
17:40:39  INFO        STOP already live CARR @ $67.55
17:40:39  INFO        [positions] 2/2 (2 valid)
17:40:39  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:40 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $484.04|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L +0.9%  $+0.76                                            HOLD|
|  CARR  P&L +2.4%  $+2.08                                           HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T13:40:40.676502-04:00 ===

[Run context]
Paper auth OK — equity $125769.05, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-16 13:40:44,126 INFO   EXIT [b83|c083_s173_w4_1120_1135_r5|S173] stop_loss (-58.1%) SELL 1 LULU260717C00122000 @<= 0.22

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $125,769.05                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    32                                      |
|  Orders filled today (ledger)  55                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             9                                       |
|  Broker option positions       3                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=288  buckets=46  win=35%                             |
|  Returns   avg=+14.0%  med=-21.4%  p10=-77.0%  p90=+93.4%              |
|  Realized  $+4,274.77                                                  |
|  Raw incl dropped  trades=391  real=$+3,151.58                         |
|  Today     trades=43  avg=-40.7%  med=-56.4%  real=$-1,203.00          |
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
|  PENDING EXITS (3)                                                     |
+------------------------------------------------------------------------+
|  b80  S173 UAL260717C00122000 x1 take_profit (+53.8%)                  |
|  b48  S165 AVGO260717C00400000 x1 stop_loss (-61.4%)                   |
|  b83  S173 LULU260717C00122000 x1 stop_loss (-58.1%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (3)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  UAL260717C00122000            3    -36.9%   $    -72.00               |
|  ADBE260717C00240000           4    +31.8%   $    +56.00               |
|  AVGO260717C00400000           1    -67.8%   $    -42.17               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=4.4s reconcile=2.44s cancel=0.12s manage=1.42s
STATUS: options_morning_bot run complete (PAPER) elapsed=4.4s. run=#4164 https://github.com/28twagg-ops/TradingBot/actions/runs/29520706579
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 26 buckets closed trades, $-1,203.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 5.6% (22/391)
```

---

## Run 20260716T174534Z

- UTC timestamp: `20260716T174534Z`
- GitHub run: [#4165](https://github.com/28twagg-ops/TradingBot/actions/runs/29521057788)
- Run id: `29521057788`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`5s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T13:45:37.495806-04:00","date":"2026-07-16","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":3.7,"phases_s":{"reconcile":2.28,"cancel":0.07,"manage":0.68},"signals":0,"placed":0,"equity":125719.07,"open_positions":3,"pending_orders":0,"open_lots":8,"submitted_today":32,"filled_today":55,"unattributed_contracts":0,"top_signals":[],"github_run":"4165","github_run_id":"29521057788","status":"ok"}
```

### Live bot full output

```text
17:45:35  INFO      Mode: exits
17:45:36  INFO        Daily log -> logs/daily/2026-07-16.md
17:45:36  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (5 ledger rows)
17:45:36  INFO        place_all_stops: checking 2 positions...
17:45:36  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
17:45:36  INFO        STOP already live CARR @ $67.55
17:45:36  INFO        [positions] 2/2 (2 valid)
17:45:36  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:45 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $484.01|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L +0.8%  $+0.72                                            HOLD|
|  CARR  P&L +2.4%  $+2.08                                           HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T13:45:37.495806-04:00 ===

[Run context]
Paper auth OK — equity $125719.07, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-16 13:45:41,002 INFO   EXIT [b43|c043_s173_w4_1120_1135_r3|S173] take_profit (+61.4%) SELL 1 ADBE260717C00240000 @<= 0.72

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $125,719.07                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    32                                      |
|  Orders filled today (ledger)  55                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             8                                       |
|  Broker option positions       3                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=289  buckets=46  win=35%                             |
|  Returns   avg=+13.8%  med=-22.9%  p10=-77.0%  p90=+93.3%              |
|  Realized  $+4,236.77                                                  |
|  Raw incl dropped  trades=392  real=$+3,113.58                         |
|  Today     trades=44  avg=-41.2%  med=-56.5%  real=$-1,241.00          |
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
|  PENDING EXITS (3)                                                     |
+------------------------------------------------------------------------+
|  b80  S173 UAL260717C00122000 x1 take_profit (+53.8%)                  |
|  b48  S165 AVGO260717C00400000 x1 stop_loss (-61.4%)                   |
|  b43  S173 ADBE260717C00240000 x1 take_profit (+61.4%)                 |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (3)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  ADBE260717C00240000           4    +47.7%   $    +84.00               |
|  UAL260717C00122000            3    -43.1%   $    -84.00               |
|  AVGO260717C00400000           1    -67.8%   $    -42.17               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=3.7s reconcile=2.28s cancel=0.07s manage=0.68s
STATUS: options_morning_bot run complete (PAPER) elapsed=3.7s. run=#4165 https://github.com/28twagg-ops/TradingBot/actions/runs/29521057788
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 26 buckets closed trades, $-1,241.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 5.6% (22/392)
```

---

## Run 20260716T175043Z

- UTC timestamp: `20260716T175043Z`
- GitHub run: [#4166](https://github.com/28twagg-ops/TradingBot/actions/runs/29521402989)
- Run id: `29521402989`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`5s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T13:50:46.763207-04:00","date":"2026-07-16","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":4.2,"phases_s":{"reconcile":2.44,"cancel":0.18,"manage":1.05},"signals":0,"placed":0,"equity":125819.33,"open_positions":3,"pending_orders":0,"open_lots":7,"submitted_today":32,"filled_today":55,"unattributed_contracts":0,"top_signals":[],"github_run":"4166","github_run_id":"29521402989","status":"ok"}
```

### Live bot full output

```text
17:50:44  INFO      Mode: exits
17:50:45  INFO        Daily log -> logs/daily/2026-07-16.md
17:50:45  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (5 ledger rows)
17:50:45  INFO        place_all_stops: checking 2 positions...
17:50:45  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
17:50:45  INFO        STOP already live CARR @ $67.55
17:50:45  INFO        [positions] 2/2 (2 valid)
17:50:45  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:50 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $484.03|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L +0.8%  $+0.72                                            HOLD|
|  CARR  P&L +2.4%  $+2.10                                           HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T13:50:46.763207-04:00 ===

[Run context]
Paper auth OK — equity $125819.33, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-16 13:50:50,709 INFO   EXIT [b42|c042_s173_w3_1045_1120_r3|S173] take_profit (+70.5%) SELL 1 ADBE260717C00240000 @<= 0.76

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $125,819.33                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    32                                      |
|  Orders filled today (ledger)  55                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             7                                       |
|  Broker option positions       3                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=290  buckets=46  win=36%                             |
|  Returns   avg=+14.0%  med=-21.4%  p10=-77.0%  p90=+93.2%              |
|  Realized  $+4,271.77                                                  |
|  Raw incl dropped  trades=393  real=$+3,148.58                         |
|  Today     trades=45  avg=-38.3%  med=-56.4%  real=$-1,206.00          |
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
|  PENDING EXITS (3)                                                     |
+------------------------------------------------------------------------+
|  b80  S173 UAL260717C00122000 x1 take_profit (+53.8%)                  |
|  b48  S165 AVGO260717C00400000 x1 stop_loss (-61.4%)                   |
|  b42  S173 ADBE260717C00240000 x1 take_profit (+70.5%)                 |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (3)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  ADBE260717C00240000           3    +70.5%   $    +93.00               |
|  UAL260717C00122000            3    -38.5%   $    -75.00               |
|  AVGO260717C00400000           1    -67.8%   $    -42.17               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=4.2s reconcile=2.44s cancel=0.18s manage=1.05s
STATUS: options_morning_bot run complete (PAPER) elapsed=4.2s. run=#4166 https://github.com/28twagg-ops/TradingBot/actions/runs/29521402989
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 26 buckets closed trades, $-1,206.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 5.6% (22/393)
```

---

## Run 20260716T175540Z

- UTC timestamp: `20260716T175540Z`
- GitHub run: [#4167](https://github.com/28twagg-ops/TradingBot/actions/runs/29521753694)
- Run id: `29521753694`
- Live bot: exit=`0`, duration=`4s`
- Options bot: exit=`0`, duration=`4s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T13:55:44.862861-04:00","date":"2026-07-16","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":3.2,"phases_s":{"reconcile":2.32,"cancel":0.07,"manage":0.46},"signals":0,"placed":0,"equity":125846.03,"open_positions":3,"pending_orders":0,"open_lots":6,"submitted_today":32,"filled_today":55,"unattributed_contracts":0,"top_signals":[],"github_run":"4167","github_run_id":"29521753694","status":"ok"}
```

### Live bot full output

```text
17:55:42  INFO      Mode: exits
17:55:43  INFO        Daily log -> logs/daily/2026-07-16.md
17:55:43  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (5 ledger rows)
17:55:43  INFO        place_all_stops: checking 2 positions...
17:55:43  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
17:55:43  INFO        STOP already live CARR @ $67.55
17:55:43  INFO        [positions] 2/2 (2 valid)
17:55:43  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:55 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $483.92|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L +0.8%  $+0.68                                            HOLD|
|  CARR  P&L +2.4%  $+2.03                                           HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T13:55:44.862861-04:00 ===

[Run context]
Paper auth OK — equity $125846.03, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-16 13:55:47,837 INFO   EXIT [b62|c062_s173_w3_1045_1120_r4|S173] take_profit (+93.2%) SELL 1 ADBE260717C00240000 @<= 0.82

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $125,846.03                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    32                                      |
|  Orders filled today (ledger)  55                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             6                                       |
|  Broker option positions       3                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=291  buckets=46  win=36%                             |
|  Returns   avg=+14.3%  med=-20.0%  p10=-77.0%  p90=+93.1%              |
|  Realized  $+4,308.77                                                  |
|  Raw incl dropped  trades=394  real=$+3,185.58                         |
|  Today     trades=46  avg=-35.8%  med=-56.2%  real=$-1,169.00          |
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
|  PENDING EXITS (3)                                                     |
+------------------------------------------------------------------------+
|  b80  S173 UAL260717C00122000 x1 take_profit (+53.8%)                  |
|  b48  S165 AVGO260717C00400000 x1 stop_loss (-61.4%)                   |
|  b62  S173 ADBE260717C00240000 x1 take_profit (+93.2%)                 |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (3)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  ADBE260717C00240000           2    +93.2%   $    +82.00               |
|  UAL260717C00122000            3    -38.5%   $    -75.00               |
|  AVGO260717C00400000           1    -67.8%   $    -42.17               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=3.2s reconcile=2.32s cancel=0.07s manage=0.46s
STATUS: options_morning_bot run complete (PAPER) elapsed=3.2s. run=#4167 https://github.com/28twagg-ops/TradingBot/actions/runs/29521753694
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 26 buckets closed trades, $-1,169.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 5.6% (22/394)
```

---

## Run 20260716T175733Z

- UTC timestamp: `20260716T175733Z`
- GitHub run: [#4168](https://github.com/28twagg-ops/TradingBot/actions/runs/29521884559)
- Run id: `29521884559`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`5s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T13:57:36.892444-04:00","date":"2026-07-16","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":4.3,"phases_s":{"reconcile":2.5,"cancel":0.22,"manage":1.06},"signals":0,"placed":0,"equity":125802.01,"open_positions":3,"pending_orders":0,"open_lots":5,"submitted_today":32,"filled_today":55,"unattributed_contracts":0,"top_signals":[],"github_run":"4168","github_run_id":"29521884559","status":"ok"}
```

### Live bot full output

```text
17:57:34  INFO      Mode: exits
17:57:35  INFO        Daily log -> logs/daily/2026-07-16.md
17:57:35  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (5 ledger rows)
17:57:35  INFO        place_all_stops: checking 2 positions...
17:57:35  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
17:57:35  INFO        STOP already live CARR @ $67.55
17:57:35  INFO        [positions] 2/2 (2 valid)
17:57:36  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:57 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $483.97|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L +0.9%  $+0.76                                            HOLD|
|  CARR  P&L +2.3%  $+2.00                                           HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T13:57:36.892444-04:00 ===

[Run context]
Paper auth OK — equity $125802.01, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-16 13:57:41,006 INFO   EXIT [b2|c002_s173_w3_1045_1120_r1|S173] take_profit (+84.1%) SELL 1 ADBE260717C00240000 @<= 0.82

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $125,802.01                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    32                                      |
|  Orders filled today (ledger)  55                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             5                                       |
|  Broker option positions       3                                       |
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
|  PENDING EXITS (3)                                                     |
+------------------------------------------------------------------------+
|  b80  S173 UAL260717C00122000 x1 take_profit (+53.8%)                  |
|  b48  S165 AVGO260717C00400000 x1 stop_loss (-61.4%)                   |
|  b2   S173 ADBE260717C00240000 x1 take_profit (+84.1%)                 |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (3)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  UAL260717C00122000            3    -38.5%   $    -75.00               |
|  AVGO260717C00400000           1    -67.8%   $    -42.17               |
|  ADBE260717C00240000           1    +84.1%   $    +37.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=4.3s reconcile=2.5s cancel=0.22s manage=1.06s
STATUS: options_morning_bot run complete (PAPER) elapsed=4.3s. run=#4168 https://github.com/28twagg-ops/TradingBot/actions/runs/29521884559
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 26 buckets closed trades, $-1,132.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 5.6% (22/395)
```

---

## Run 20260716T180041Z

- UTC timestamp: `20260716T180041Z`
- GitHub run: [#4169](https://github.com/28twagg-ops/TradingBot/actions/runs/29522107552)
- Run id: `29522107552`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`4s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T14:00:45.110207-04:00","date":"2026-07-16","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":2.7,"phases_s":{"reconcile":2.32,"cancel":0.04,"manage":0.05},"signals":0,"placed":0,"equity":125824.01,"open_positions":3,"pending_orders":0,"open_lots":5,"submitted_today":32,"filled_today":55,"unattributed_contracts":0,"top_signals":[],"github_run":"4169","github_run_id":"29522107552","status":"ok"}
```

### Live bot full output

```text
18:00:43  INFO      Mode: exits
18:00:43  INFO        Daily log -> logs/daily/2026-07-16.md
18:00:43  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (5 ledger rows)
18:00:43  INFO        place_all_stops: checking 2 positions...
18:00:43  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
18:00:43  INFO        STOP already live CARR @ $67.55
18:00:44  INFO        [positions] 2/2 (2 valid)
18:00:44  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:00 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $483.87|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L +0.8%  $+0.68                                            HOLD|
|  CARR  P&L +2.3%  $+1.98                                           HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T14:00:45.110207-04:00 ===

[Run context]
Paper auth OK — equity $125824.01, account PA36KS87UPRS

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
|  Equity                        $125,824.01                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    32                                      |
|  Orders filled today (ledger)  55                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             5                                       |
|  Broker option positions       3                                       |
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
|  PENDING EXITS (3)                                                     |
+------------------------------------------------------------------------+
|  b80  S173 UAL260717C00122000 x1 take_profit (+53.8%)                  |
|  b48  S165 AVGO260717C00400000 x1 stop_loss (-61.4%)                   |
|  b2   S173 ADBE260717C00240000 x1 take_profit (+84.1%)                 |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (3)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  UAL260717C00122000            3    -38.5%   $    -75.00               |
|  AVGO260717C00400000           1    -67.8%   $    -42.17               |
|  ADBE260717C00240000           1    +65.9%   $    +29.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=2.7s reconcile=2.32s cancel=0.04s manage=0.05s
STATUS: options_morning_bot run complete (PAPER) elapsed=2.7s. run=#4169 https://github.com/28twagg-ops/TradingBot/actions/runs/29522107552
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 26 buckets closed trades, $-1,132.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 5.6% (22/395)
```

---

## Run 20260716T180539Z

- UTC timestamp: `20260716T180539Z`
- GitHub run: [#4170](https://github.com/28twagg-ops/TradingBot/actions/runs/29522479689)
- Run id: `29522479689`
- Live bot: exit=`0`, duration=`4s`
- Options bot: exit=`0`, duration=`4s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T14:05:43.831893-04:00","date":"2026-07-16","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":3.5,"phases_s":{"reconcile":2.54,"cancel":0.24,"manage":0.16},"signals":0,"placed":0,"equity":125761.31,"open_positions":2,"pending_orders":0,"open_lots":4,"submitted_today":32,"filled_today":55,"unattributed_contracts":0,"top_signals":[],"github_run":"4170","github_run_id":"29522479689","status":"ok"}
```

### Live bot full output

```text
18:05:40  INFO      Mode: exits
18:05:42  INFO        Daily log -> logs/daily/2026-07-16.md
18:05:42  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (5 ledger rows)
18:05:42  INFO        place_all_stops: checking 2 positions...
18:05:42  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
18:05:42  INFO        STOP already live CARR @ $67.55
18:05:42  INFO        [positions] 2/2 (2 valid)
18:05:42  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:05 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $483.51|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L +0.7%  $+0.58                                            HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T14:05:43.831893-04:00 ===

[Run context]
Paper auth OK — equity $125761.31, account PA36KS87UPRS

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
|  Equity                        $125,761.31                             |
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
|  b80  S173 UAL260717C00122000 x1 take_profit (+53.8%)                  |
|  b48  S165 AVGO260717C00400000 x1 stop_loss (-61.4%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (2)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  UAL260717C00122000            3    -38.5%   $    -75.00               |
|  AVGO260717C00400000           1    -67.8%   $    -42.17               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=3.5s reconcile=2.54s cancel=0.24s manage=0.16s
STATUS: options_morning_bot run complete (PAPER) elapsed=3.5s. run=#4170 https://github.com/28twagg-ops/TradingBot/actions/runs/29522479689
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 26 buckets closed trades, $-1,132.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 5.6% (22/395)
```

---

## Run 20260716T181038Z

- UTC timestamp: `20260716T181038Z`
- GitHub run: [#4171](https://github.com/28twagg-ops/TradingBot/actions/runs/29522830037)
- Run id: `29522830037`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`4s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T14:10:41.918885-04:00","date":"2026-07-16","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":2.6,"phases_s":{"reconcile":2.25,"cancel":0.06,"manage":0.05},"signals":0,"placed":0,"equity":125584.99,"open_positions":2,"pending_orders":0,"open_lots":4,"submitted_today":32,"filled_today":55,"unattributed_contracts":0,"top_signals":[],"github_run":"4171","github_run_id":"29522830037","status":"ok"}
```

### Live bot full output

```text
18:10:40  INFO      Mode: exits
18:10:40  INFO        Daily log -> logs/daily/2026-07-16.md
18:10:40  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (5 ledger rows)
18:10:40  INFO        place_all_stops: checking 2 positions...
18:10:40  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
18:10:40  INFO        STOP already live CARR @ $67.55
18:10:41  INFO        [positions] 2/2 (2 valid)
18:10:41  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $483.80|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L +0.8%  $+0.73                                            HOLD|
|  CARR  P&L +2.2%  $+1.86                                           HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T14:10:41.918885-04:00 ===

[Run context]
Paper auth OK — equity $125584.99, account PA36KS87UPRS

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
|  Equity                        $125,584.99                             |
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
|  b80  S173 UAL260717C00122000 x1 take_profit (+53.8%)                  |
|  b48  S165 AVGO260717C00400000 x1 stop_loss (-61.4%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (2)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  UAL260717C00122000            3    -38.5%   $    -75.00               |
|  AVGO260717C00400000           1    -75.9%   $    -47.17               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=2.6s reconcile=2.25s cancel=0.06s manage=0.05s
STATUS: options_morning_bot run complete (PAPER) elapsed=2.6s. run=#4171 https://github.com/28twagg-ops/TradingBot/actions/runs/29522830037
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 26 buckets closed trades, $-1,132.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 5.6% (22/395)
```

---

## Run 20260716T181535Z

- UTC timestamp: `20260716T181535Z`
- GitHub run: [#4172](https://github.com/28twagg-ops/TradingBot/actions/runs/29523167835)
- Run id: `29523167835`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`4s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T14:15:38.251080-04:00","date":"2026-07-16","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":2.4,"phases_s":{"reconcile":2.16,"cancel":0.04,"manage":0.02},"signals":0,"placed":0,"equity":125635.99,"open_positions":2,"pending_orders":0,"open_lots":4,"submitted_today":32,"filled_today":55,"unattributed_contracts":0,"top_signals":[],"github_run":"4172","github_run_id":"29523167835","status":"ok"}
```

### Live bot full output

```text
18:15:36  INFO      Mode: exits
18:15:37  INFO        Daily log -> logs/daily/2026-07-16.md
18:15:37  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (5 ledger rows)
18:15:37  INFO        place_all_stops: checking 2 positions...
18:15:37  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
18:15:37  INFO        STOP already live CARR @ $67.55
18:15:37  INFO        [positions] 2/2 (2 valid)
18:15:37  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:15 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $483.85|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L +0.8%  $+0.73                                            HOLD|
|  CARR  P&L +2.2%  $+1.92                                           HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T14:15:38.251080-04:00 ===

[Run context]
Paper auth OK — equity $125635.99, account PA36KS87UPRS

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
|  Equity                        $125,635.99                             |
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
|  b80  S173 UAL260717C00122000 x1 take_profit (+53.8%)                  |
|  b48  S165 AVGO260717C00400000 x1 stop_loss (-61.4%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (2)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  UAL260717C00122000            3    -27.7%   $    -54.00               |
|  AVGO260717C00400000           1    -72.7%   $    -45.17               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=2.4s reconcile=2.16s cancel=0.04s manage=0.02s
STATUS: options_morning_bot run complete (PAPER) elapsed=2.4s. run=#4172 https://github.com/28twagg-ops/TradingBot/actions/runs/29523167835
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 26 buckets closed trades, $-1,132.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 5.6% (22/395)
```

---

## Run 20260716T182038Z

- UTC timestamp: `20260716T182038Z`
- GitHub run: [#4173](https://github.com/28twagg-ops/TradingBot/actions/runs/29523504441)
- Run id: `29523504441`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`4s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T14:20:41.760629-04:00","date":"2026-07-16","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":3.1,"phases_s":{"reconcile":2.29,"cancel":0.1,"manage":0.07},"signals":0,"placed":0,"equity":126183.99,"open_positions":2,"pending_orders":0,"open_lots":4,"submitted_today":32,"filled_today":55,"unattributed_contracts":0,"top_signals":[],"github_run":"4173","github_run_id":"29523504441","status":"ok"}
```

### Live bot full output

```text
18:20:39  INFO      Mode: exits
18:20:40  INFO        Daily log -> logs/daily/2026-07-16.md
18:20:40  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (5 ledger rows)
18:20:40  INFO        place_all_stops: checking 2 positions...
18:20:40  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
18:20:40  INFO        STOP already live CARR @ $67.55
18:20:40  INFO        [positions] 2/2 (2 valid)
18:20:40  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $483.93|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L +1.0%  $+0.86                                            HOLD|
|  CARR  P&L +2.2%  $+1.87                                           HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T14:20:41.760629-04:00 ===

[Run context]
Paper auth OK — equity $126183.99, account PA36KS87UPRS

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
|  Equity                        $126,183.99                             |
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
|  b80  S173 UAL260717C00122000 x1 take_profit (+53.8%)                  |
|  b48  S165 AVGO260717C00400000 x1 stop_loss (-61.4%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (2)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  UAL260717C00122000            3    -27.7%   $    -54.00               |
|  AVGO260717C00400000           1    -69.4%   $    -43.17               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=3.1s reconcile=2.29s cancel=0.1s manage=0.07s
STATUS: options_morning_bot run complete (PAPER) elapsed=3.1s. run=#4173 https://github.com/28twagg-ops/TradingBot/actions/runs/29523504441
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 26 buckets closed trades, $-1,132.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 5.6% (22/395)
```

---

## Run 20260716T182533Z

- UTC timestamp: `20260716T182533Z`
- GitHub run: [#4174](https://github.com/28twagg-ops/TradingBot/actions/runs/29523846511)
- Run id: `29523846511`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`7s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T14:25:36.230147-04:00","date":"2026-07-16","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":5.8,"phases_s":{"reconcile":5.46,"cancel":0.07,"manage":0.05},"signals":0,"placed":0,"equity":126449.07,"open_positions":2,"pending_orders":0,"open_lots":4,"submitted_today":32,"filled_today":55,"unattributed_contracts":0,"top_signals":[],"github_run":"4174","github_run_id":"29523846511","status":"ok"}
```

### Live bot full output

```text
18:25:34  INFO      Mode: exits
18:25:35  INFO        Daily log -> logs/daily/2026-07-16.md
18:25:35  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (5 ledger rows)
18:25:35  INFO        place_all_stops: checking 2 positions...
18:25:35  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
18:25:35  INFO        STOP already live CARR @ $67.55
18:25:35  INFO        [positions] 2/2 (2 valid)
18:25:35  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:25 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $484.05|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L +1.1%  $+0.92                                            HOLD|
|  CARR  P&L +2.2%  $+1.92                                           HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T14:25:36.230147-04:00 ===

[Run context]
Paper auth OK — equity $126449.07, account PA36KS87UPRS

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
|  Equity                        $126,449.07                             |
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
|  b80  S173 UAL260717C00122000 x1 take_profit (+53.8%)                  |
|  b48  S165 AVGO260717C00400000 x1 stop_loss (-61.4%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (2)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  UAL260717C00122000            3    -27.7%   $    -54.00               |
|  AVGO260717C00400000           1    -66.2%   $    -41.17               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=5.8s reconcile=5.46s cancel=0.07s manage=0.05s
STATUS: options_morning_bot run complete (PAPER) elapsed=5.8s. run=#4174 https://github.com/28twagg-ops/TradingBot/actions/runs/29523846511
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 26 buckets closed trades, $-1,132.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 5.6% (22/395)
```

---

## Run 20260716T183037Z

- UTC timestamp: `20260716T183037Z`
- GitHub run: [#4175](https://github.com/28twagg-ops/TradingBot/actions/runs/29524183445)
- Run id: `29524183445`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`4s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-16T14:30:39.512412-04:00","date":"2026-07-16","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":2.8,"phases_s":{"reconcile":2.15,"cancel":0.04,"manage":0.06},"signals":0,"placed":0,"equity":125975.99,"open_positions":2,"pending_orders":0,"open_lots":4,"submitted_today":32,"filled_today":55,"unattributed_contracts":0,"top_signals":[],"github_run":"4175","github_run_id":"29524183445","status":"ok"}
```

### Live bot full output

```text
18:30:38  INFO      Mode: exits
18:30:38  INFO        Daily log -> logs/daily/2026-07-16.md
18:30:38  INFO        Daily log reconciled -> logs/daily/2026-07-16.md (5 ledger rows)
18:30:38  INFO        place_all_stops: checking 2 positions...
18:30:38  INFO        STOP skipped AME: fractional (0.3685 shares) — software exit will handle it
18:30:38  INFO        STOP already live CARR @ $67.55
18:30:38  INFO        [positions] 2/2 (2 valid)
18:30:38  INFO        Daily log -> logs/daily/2026-07-16.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:30 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $483.69|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L +0.8%  $+0.69                                            HOLD|
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
=== options_morning_bot (PAPER) 2026-07-16T14:30:39.512412-04:00 ===

[Run context]
Paper auth OK — equity $125975.99, account PA36KS87UPRS

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
|  Equity                        $125,975.99                             |
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
|  b80  S173 UAL260717C00122000 x1 take_profit (+53.8%)                  |
|  b48  S165 AVGO260717C00400000 x1 stop_loss (-61.4%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (2)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  UAL260717C00122000            3    -64.6%   $   -126.00               |
|  AVGO260717C00400000           1    -69.4%   $    -43.17               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-16.log
elapsed=2.8s reconcile=2.15s cancel=0.04s manage=0.06s
STATUS: options_morning_bot run complete (PAPER) elapsed=2.8s. run=#4175 https://github.com/28twagg-ops/TradingBot/actions/runs/29524183445
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_buckets.csv
Summary: 26 buckets closed trades, $-1,132.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-16_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 5.6% (22/395)
```

---
