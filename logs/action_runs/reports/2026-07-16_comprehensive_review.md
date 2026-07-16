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
