# Daily Comprehensive Action Review — 2026-07-14

_Auto-generated from GitHub Actions run output. This document appends every run for the day._

## Run 20260714T130049Z

- UTC timestamp: `20260714T130049Z`
- GitHub run: [#3836](https://github.com/28twagg-ops/TradingBot/actions/runs/29334696346)
- Run id: `29334696346`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`5s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-14T09:00:51.397488-04:00","date":"2026-07-14","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":3.5,"phases_s":{"reconcile":3.3},"signals":0,"placed":0,"equity":133642.92,"open_positions":2,"pending_orders":0,"open_lots":7,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"3836","github_run_id":"29334696346","status":"ok"}
```

### Live bot full output

```text
13:00:50  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:00 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $480.07|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $480.07|
|  Cash                                                           $388.72|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $91.35|
|  Open P&L                                                        $+0.01|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (1 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  NI       Pullback50      $91.35     $47.07   $47.07   +0.0%   $+0.01  |
|                                                                        |
|  Total invested                                                  $91.35|
|  Total open P&L                                                  $+0.01|
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
|  2026-07-13  SELL  JCI  Pullback50  $91.32  P&L $+0.09                 |
|  2026-07-13  SELL  FANG  Pullback50  $91.32  P&L $+0.02                |
|  2026-07-13  SELL  MO  Pullback50  $91.26  P&L $-0.08                  |
|  2026-07-13  SELL  ETN  Pullback50  $95.96  P&L $-0.70                 |
|  2026-07-13  SELL  EXR  Pullback50  $96.39  P&L $-0.50                 |
|  2026-07-13  SELL  AME  Pullback50  $96.22  P&L $-0.67                 |
+========================================================================+
```

### Options bot full output

```text
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-14T09:00:51.397488-04:00 ===

[Run context]
After hours (09:00 ET) — exit summary only.
Paper auth OK — equity $133642.92, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $133,642.92                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             7                                       |
|  Broker option positions       2                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=106  buckets=35  win=55%                             |
|  Returns   avg=+31.5%  med=+7.0%  p10=-77.8%  p90=+81.1%               |
|  Realized  $+6,674.77                                                  |
|  Raw incl dropped  trades=197  real=$+5,979.58                         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b62  c062_s173_w3_1045_  3  67% +713.3 +1100.0 +1100.0 $   +107       |
|  b60  c060_s173_w1_0928_  3  67% +44.3 +78.8 +96.7 $    +41            |
|  b92  c092_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s166_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s166_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s163_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b98  c098_s163_w3_1045_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b99  c099_s163_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 27 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s173_w2_1005_  3   0% -55.5 -77.0 -77.0 $    -96       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (2)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  INTC260715C00113000           4    -41.7%   $    -94.40               |
|  SMCI260717C00029000           3    -22.5%   $    -42.75               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-14.log
elapsed=3.5s reconcile=3.3s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=3.5s. run=#3836 https://github.com/28twagg-ops/TradingBot/actions/runs/29334696346
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-14_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-14_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-14_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-14_strategy_selection.csv
Summary: keep=0 watch=4 drop=1
```

---

