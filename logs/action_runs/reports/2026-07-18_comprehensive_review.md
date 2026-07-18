# Daily Comprehensive Action Review — 2026-07-18

_Auto-generated from GitHub Actions run output. This document appends every run for the day._

## Run 20260718T005835Z

- UTC timestamp: `20260718T005835Z`
- GitHub run: [#4391](https://github.com/28twagg-ops/TradingBot/actions/runs/29624234553)
- Run id: `29624234553`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`4s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T20:58:37.962605-04:00","date":"2026-07-17","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":2.3,"phases_s":{"reconcile":1.79},"signals":0,"placed":0,"equity":125578.95,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":40,"filled_today":60,"unattributed_contracts":0,"top_signals":[],"github_run":"4391","github_run_id":"29624234553","status":"ok"}
```

### Live bot full output

```text
00:58:36  INFO      Mode: weekly
00:58:37  INFO        Weekly summary -> logs/weekly/2026-W29.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                            WEEKLY|
|  Time                                                         00:58 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.98|
+========================================================================+

+========================================================================+
|              RUBBER BAND BOT  |  Week 29 / 2026  |  LIVE               |
+========================================================================+
+------------------------------------------------------------------------+
|  Date                                                 2026-07-18  (Jul)|
|  Regime                                                            BULL|
|  Strategy                                        52wkLow  +  Pullback50|
|  Execution                      Summary mode only (no orders submitted)|
|  Buys today                                                           0|
|  Cash-based cap            27850 max trades with current available cash|
+------------------------------------------------------------------------+
|  Equity           $482.98       Cash             $302.65               |
|  Invested         $180.33       Available        $278.50               |
|  Open P&L         $+1.17        Realized P&L     $-4.62                |
+------------------------------------------------------------------------+
|  This week          0 buys  |  32 sells  |  Win rate 38%  |  P&L $+5.38|
|  All time  990 trades  |  Avg hold 1.8d  |  Return -5.1%  |  P&L $-4.62|
+------------------------------------------------------------------------+
|  TICKER  STRATEGY       INVESTED   ENTRY     NOW       P&L%      P&L$  |
+------------------------------------------------------------------------+
|  CARR    Pullback50     $87.03     $67.89    $68.69    +1.2%     $+1.01|
|  EMR     Pullback50     $93.30     $139.30   $139.54   +0.2%     $+0.16|
+------------------------------------------------------------------------+
|  Next month                               Aug:  VolumeSpike  +  52wkLow|
+========================================================================+

+========================================================================+
|                        YEAR-BY-YEAR PERFORMANCE                        |
+========================================================================+
|  YEAR   START     END       RETURN    P&L $       TRADES   WIN%        |
+------------------------------------------------------------------------+
|  2026   $509      $484      -4.8%     $-24.44     990      31.2% ✗     |
+------------------------------------------------------------------------+
|  Profitable years                                             0/1  (0%)|
|  Best  year                                      2026   -4.8%   $-24.44|
|  Worst year                                      2026   -4.8%   $-24.44|
+========================================================================+
```

### Options bot full output

```text
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-17T20:58:37.962605-04:00 ===

[Run context]
After hours (20:58 ET) — exit summary only.
Paper auth OK — equity $125578.95, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $125,578.95                             |
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
elapsed=2.3s reconcile=1.79s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=2.3s. run=#4391 https://github.com/28twagg-ops/TradingBot/actions/runs/29624234553
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_buckets.csv
Summary: 27 buckets closed trades, $+2,200.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-17_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 3.6% (22/604)
  File "/home/runner/work/TradingBot/TradingBot/scripts/options_signal_frequency.py", line 80
    return f"{day}|{sid}|{re.sub(r'\s+', ' ', line.strip())[:160]}"
                                                                   ^
SyntaxError: f-string expression part cannot include a backslash
signal_frequency report failed (non-fatal)
## Ledger health — 2026-07-17
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |     0 | OK |
| Missing exit records (post) |     0 | OK |
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |   264 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
```

---

