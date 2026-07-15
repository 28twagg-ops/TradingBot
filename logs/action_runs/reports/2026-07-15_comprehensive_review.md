# Daily Comprehensive Action Review — 2026-07-15

_Auto-generated from GitHub Actions run output. This document appends every run for the day._

## Run 20260715T204540Z

- UTC timestamp: `20260715T204540Z`
- GitHub run: [#4061](https://github.com/28twagg-ops/TradingBot/actions/runs/29449474764)
- Run id: `29449474764`
- Live bot: exit=`0`, duration=`8s`
- Options bot: exit=`0`, duration=`5s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-15T16:45:48.943238-04:00","date":"2026-07-15","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":3.9,"phases_s":{"reconcile":3.41},"signals":0,"placed":0,"equity":133254.68,"open_positions":3,"pending_orders":0,"open_lots":14,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4061","github_run_id":"29449474764","status":"ok"}
```

### Live bot full output

```text
20:45:41  INFO      Mode: ext_exits
20:45:42  INFO        Daily log -> logs/daily/2026-07-15.md
20:45:42  INFO        Daily log reconciled -> logs/daily/2026-07-15.md (0 ledger rows)
20:45:42  INFO        SELL LIMIT [EXT HRS] CDNS  qty=0.254824738  limit=$371.44  id=ed71469a-941c-42bb-b615-e508e1160a33
20:45:47  INFO        SELL LIMIT[EXT] pending for CDNS — 9:35am will follow up
20:45:47  INFO        Daily log -> logs/daily/2026-07-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         20:45 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $481.19|
+========================================================================+

+========================================================================+
|                       EXIT CHECK [EXTENDED HRS]                        |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  CDNS  P&L -1.3%  $-1.23         EXIT [EXTENDED HRS]: stop_loss (-1.3%)|
|  CDNS                             SELL pending (after-hours limit open)|
|  CHH  P&L +0.6%  $+0.59          HOLDING until 9:35am scan (Pullback50)|
|  HST  P&L +1.8%  $+1.65          HOLDING until 9:35am scan (Pullback50)|
|  EVR  P&L +1.9%  $+1.84          HOLDING until 9:35am scan (Pullback50)|
+========================================================================+

+========================================================================+
|                          EXTENDED HOURS SELLS                          |
+========================================================================+
|                                                                        |
|  No extended-hours sells this run.                                     |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                         ext_exits|
|  Candidates                                                           4|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  1 attempted  |  0 filled  |  0 partial  |  1 pending  |  0 failed|
|  Holds                                                                3|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  CDNS                                        -1.28%  (threshold -0.50%)|
|  Count                                                                1|
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             1|
+========================================================================+
```

### Options bot full output

```text
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-15T16:45:48.943238-04:00 ===

[Run context]
After hours (16:45 ET) — exit summary only.
Paper auth OK — equity $133254.68, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $133,254.68                             |
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
elapsed=3.9s reconcile=3.41s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=3.9s. run=#4061 https://github.com/28twagg-ops/TradingBot/actions/runs/29449474764
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-15_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-15_buckets.csv
Summary: 4 buckets closed trades, $-105.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-15_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-15_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
```

---

