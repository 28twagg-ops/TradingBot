# Daily Comprehensive Action Review — 2026-07-13

_Auto-generated from GitHub Actions run output. This document appends every run for the day._

## Run 20260713T130052Z

- UTC timestamp: `20260713T130052Z`
- GitHub run: [#3705](https://github.com/28twagg-ops/TradingBot/actions/runs/29252025147)
- Run id: `29252025147`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`6s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-13T09:00:54.782248-04:00","date":"2026-07-13","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":5.3,"phases_s":{"reconcile":4.91},"signals":0,"placed":0,"equity":136938.77,"open_positions":4,"pending_orders":0,"open_lots":54,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"3705","github_run_id":"29252025147","status":"ok"}
```

### Live bot full output

```text
13:00:53  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:00 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $481.81|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $481.81|
|  Cash                                                           $180.36|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $301.45|
|  Open P&L                                                        $+0.17|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (4 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CARR     Pullback50      $95.82     $67.90   $68.50   +0.9%   $+0.84  |
|  CHD      Pullback50      $94.40     $96.44   $96.36   -0.1%   $-0.08  |
|  CMI      Pullback50      $93.65     $674.69  $669.37  -0.8%   $-0.74  |
|  HST      Pullback50      $17.58     $23.03   $23.22   +0.8%   $+0.14  |
|                                                                        |
|  Total invested                                                 $301.45|
|  Total open P&L                                                  $+0.17|
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
|  2026-07-10  SELL  ATO  Pullback50  $97.03  P&L $-0.01                 |
|  2026-07-10  SELL  AME  Pullback50  $87.12  P&L $+0.62                 |
|  2026-07-10  SELL  DECK  Pullback50  $94.50  P&L $-0.51                |
|  2026-07-09  SELL  CSCO  Pullback50  $99.56  P&L $+4.33                |
|  2026-07-09  SELL  CDNS  Pullback50  $88.40  P&L $+1.86                |
|  2026-07-09  SELL  AES  Pullback50  $97.24  P&L $+0.76                 |
+========================================================================+
```

### Options bot full output

```text
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-13T09:00:54.782248-04:00 ===

[Run context]
After hours (09:00 ET) — exit summary only.
Paper auth OK — equity $136938.77, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $136,938.77                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             54                                      |
|  Broker option positions       4                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD                                                    |
+------------------------------------------------------------------------+
|  All-time  trades=92  buckets=46  win=72%                              |
|  Returns   avg=+24.4%  med=+32.3%  p10=-77.7%  p90=+70.5%              |
|  Realized  $+7,585.58                                                  |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b70  c070_s165_w3_1045_  1 100% +59.1 +59.1 +59.1 $    +28            |
|  b58  c058_s163_w3_1045_  1 100% +59.1 +59.1 +59.1 $    +25            |
|  b73  c073_s166_w2_1005_  1 100% +55.6 +55.6 +55.6 $    +36            |
|  b92  c092_s166_w1_0928_  2 100% +53.6 +53.6 +70.8 $    +95            |
|  b93  c093_s166_w2_1005_  2 100% +53.6 +53.6 +70.8 $    +95            |
|  b95  c095_s166_w4_1120_  2 100% +50.5 +50.5 +70.8 $    +95            |
|  b96  c096_s163_w1_0928_  2 100% +50.5 +50.5 +70.8 $    +95            |
|  b98  c098_s163_w3_1045_  2 100% +50.5 +50.5 +70.8 $    +95            |
|  ... 38 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b0   c000_s173_w1_0928_ 22  45% +22.4 -64.3 -100.0 $  +6311      |
+========================================================================+
+========================================================================+
|  PENDING EXITS (4)                                                     |
+------------------------------------------------------------------------+
|  b46  S174 INTC260713C00115000 x1 EOD                                  |
|  b80  S173 T260717C00021000 x1 EOD                                     |
|  b47  S174 PSKY260717C00010000 x1 EOD                                  |
|  b47  S174 INTC260713C00114000 x1 EOD                                  |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (4)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  INTC260713C00115000          31     -5.6%   $   -102.69               |
|  PSKY260717C00010000           4    +37.5%   $    +12.00               |
|  T260717C00021000             10     -2.8%   $    -10.00               |
|  INTC260713C00114000           9     +0.1%   $     +0.60               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-13.log
elapsed=5.3s reconcile=4.91s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=5.3s. run=#3705 https://github.com/28twagg-ops/TradingBot/actions/runs/29252025147
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-13_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-13_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-13_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-13_strategy_selection.csv
Summary: keep=0 watch=5 drop=0
```

---

