# Daily Comprehensive Action Review — 2026-07-10

_Auto-generated from GitHub Actions run output. This document appends every run for the day._

## Run 20260710T130044Z

- UTC timestamp: `20260710T130044Z`
- GitHub run: [#3574](https://github.com/28twagg-ops/TradingBot/actions/runs/29094467740)
- Run id: `29094467740`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`2s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-10T09:00:46.591959-04:00","date":"2026-07-10","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.3,"phases_s":{"reconcile":0.13},"signals":0,"placed":0,"equity":157705.12,"open_positions":19,"pending_orders":0,"open_lots":19,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"3574","github_run_id":"29094467740","status":"ok"}
```

### Live bot full output

```text
13:00:45  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:00 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $481.85|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $481.85|
|  Cash                                                           $213.66|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $268.19|
|  Open P&L                                                        $+0.17|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (3 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AME      Pullback50      $86.35     $233.44  $232.99  -0.2%   $-0.17  |
|  CARR     Pullback50      $95.13     $67.90   $68.00   +0.2%   $+0.15  |
|  HST      Pullback50      $86.71     $23.03   $23.08   +0.2%   $+0.19  |
|                                                                        |
|  Total invested                                                 $268.19|
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
|  2026-07-09  SELL  CSCO  Pullback50  $99.56  P&L $+4.33                |
|  2026-07-09  SELL  CDNS  Pullback50  $88.40  P&L $+1.86                |
|  2026-07-09  SELL  AES  Pullback50  $97.24  P&L $+0.76                 |
|  2026-07-08  SELL  ATO  Pullback50  $96.20  P&L $-0.35                 |
|  2026-07-08  SELL  MAR  Pullback50  $96.50  P&L $-0.52                 |
|  2026-07-08  SELL  DECK  Pullback50  $87.47  P&L $-2.12                |
+========================================================================+
```

### Options bot full output

```text
Traceback (most recent call last):
  File "/home/runner/work/TradingBot/TradingBot/scripts/init_options_trial.py", line 15, in <module>
    from local_docs import local_docs
ModuleNotFoundError: No module named 'local_docs'
=== options_morning_bot (PAPER) 2026-07-10T09:00:46.591959-04:00 ===

[Run context]
After hours (09:00 ET) — exit summary only.
Paper auth OK — equity $157705.12, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $157,705.12                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             19                                      |
|  Broker option positions       19                                      |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD                                                    |
+------------------------------------------------------------------------+
|  All-time  trades=52  buckets=39  win=94%                              |
|  Returns   avg=+39.6%  med=+36.5%  p10=+24.0%  p90=+70.8%              |
|  Realized  $+2,154.53                                                  |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b70  c070_s165_w3_1045_  1 100% +59.1 +59.1 +59.1 $    +28            |
|  b58  c058_s163_w3_1045_  1 100% +59.1 +59.1 +59.1 $    +25            |
|  b0   c000_s173_w1_0928_  4 100% +61.5 +55.7 +84.7 $   +748            |
|  b73  c073_s166_w2_1005_  1 100% +55.6 +55.6 +55.6 $    +36            |
|  b82  c082_s173_w3_1045_  1 100% +55.6 +55.6 +55.6 $    +36            |
|  b92  c092_s166_w1_0928_  2 100% +53.6 +53.6 +70.8 $    +95            |
|  b93  c093_s166_w2_1005_  2 100% +53.6 +53.6 +70.8 $    +95            |
|  b95  c095_s166_w4_1120_  2 100% +50.5 +50.5 +70.8 $    +95            |
|  ... 31 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b78  c078_s163_w3_1045_  1   0% -23.3 -23.3 -23.3 $    -19       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (19)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AVGO260710C00400000          49   +847.8%   $+23,230.00               |
|  ANET260710C00185000          22   +780.0%   $ +4,680.00               |
|  CCL260717C00026000           93    +47.9%   $ +3,342.00               |
|  MRNA260710C00085000          54   -100.0%   $ -1,667.00               |
|  GOOGL260710C00365000         75    -23.1%   $ -1,419.00               |
|  GOOGL260710C00362500         24    +98.6%   $ +1,394.00               |
|  INTC260710C00118000          25    -42.4%   $   -958.00               |
|  INTC260710C00119000          24    -50.2%   $   -896.00               |
|  ... 11 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-10.log
elapsed=0.3s reconcile=0.13s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.3s. run=#3574 https://github.com/28twagg-ops/TradingBot/actions/runs/29094467740
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-10_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-10_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-10_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-10_strategy_selection.csv
Summary: keep=0 watch=5 drop=0
```

---

