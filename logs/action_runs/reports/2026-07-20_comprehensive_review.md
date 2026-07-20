# Daily Comprehensive Action Review — 2026-07-20

_Auto-generated from GitHub Actions run output. This document appends every run for the day._

## Run 20260720T030001Z

- UTC timestamp: `20260720T030001Z`
- GitHub run: [#4392](https://github.com/28twagg-ops/TradingBot/actions/runs/29711961045)
- Run id: `29711961045`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-17T20:58:37.962605-04:00","date":"2026-07-17","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":2.3,"phases_s":{"reconcile":1.79},"signals":0,"placed":0,"equity":125578.95,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":40,"filled_today":60,"unattributed_contracts":0,"top_signals":[],"github_run":"4391","github_run_id":"29624234553","status":"ok"}
```

### Live bot full output

```text
03:00:02  INFO      Mode: weekly
03:00:04  INFO        Weekly summary -> logs/weekly/2026-W30.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                            WEEKLY|
|  Time                                                         03:00 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.98|
+========================================================================+

+========================================================================+
|              RUBBER BAND BOT  |  Week 30 / 2026  |  LIVE               |
+========================================================================+
+------------------------------------------------------------------------+
|  Date                                                 2026-07-20  (Jul)|
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
Weekend — skip options paper bot
```

---

## Run 20260720T054823Z

- UTC timestamp: `20260720T054823Z`
- GitHub run: [#4393](https://github.com/28twagg-ops/TradingBot/actions/runs/29719972204)
- Run id: `29719972204`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`4s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T01:48:27.136300-04:00","date":"2026-07-20","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":2.7,"phases_s":{"reconcile":2.23},"signals":0,"placed":0,"equity":126605.53,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4393","github_run_id":"29719972204","status":"ok"}
```

### Live bot full output

```text
05:48:24  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         05:48 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.98|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $482.98|
|  Cash                                                           $302.65|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $180.33|
|  Open P&L                                                        $+1.17|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (2 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CARR     Pullback50      $87.03     $67.89   $68.69   +1.2%   $+1.01  |
|  EMR      Pullback50      $93.30     $139.30  $139.54  +0.2%   $+0.16  |
|                                                                        |
|  Total invested                                                 $180.33|
|  Total open P&L                                                  $+1.17|
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
|  2026-07-17  SELL  EBAY  Pullback50  $93.44  P&L $+0.30                |
|  2026-07-17  SELL  CMS  Pullback50  $22.29  P&L $-0.14                 |
|  2026-07-17  SELL  DOV  Pullback50  $81.38  P&L $-0.50                 |
|  2026-07-17  SELL  DRI  Pullback50  $95.97  P&L $-0.89                 |
|  2026-07-17  SELL  BG  Pullback50  $97.67  P&L $-0.08                  |
|  2026-07-17  SELL  CNP  Pullback50  $99.12  P&L $+2.36                 |
+========================================================================+
```

### Options bot full output

```text
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-20T01:48:27.136300-04:00 ===

[Run context]
After hours (01:48 ET) — exit summary only.
Paper auth OK — equity $126605.53, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $126,605.53                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
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
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=2.7s reconcile=2.23s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=2.7s. run=#4393 https://github.com/28twagg-ops/TradingBot/actions/runs/29719972204
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 3.6% (22/604)
  File "/home/runner/work/TradingBot/TradingBot/scripts/options_signal_frequency.py", line 80
    return f"{day}|{sid}|{re.sub(r'\s+', ' ', line.strip())[:160]}"
                                                                   ^
SyntaxError: f-string expression part cannot include a backslash
signal_frequency report failed (non-fatal)
## Ledger health — 2026-07-20
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |    27 | WARN | <<<
| Missing exit records (post) |    27 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |   264 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
```

---

## Run 20260720T130036Z

- UTC timestamp: `20260720T130036Z`
- GitHub run: [#4394](https://github.com/28twagg-ops/TradingBot/actions/runs/29744391750)
- Run id: `29744391750`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`4s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T09:00:38.414950-04:00","date":"2026-07-20","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":2.2,"phases_s":{"reconcile":1.98},"signals":0,"placed":0,"equity":128229.53,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4394","github_run_id":"29744391750","status":"ok"}
```

### Live bot full output

```text
13:00:37  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:00 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $484.78|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $484.78|
|  Cash                                                           $302.65|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $182.13|
|  Open P&L                                                        $+2.97|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (2 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CARR     Pullback50      $88.50     $67.89   $69.85   +2.9%   $+2.48  |
|  EMR      Pullback50      $93.63     $139.30  $140.03  +0.5%   $+0.49  |
|                                                                        |
|  Total invested                                                 $182.13|
|  Total open P&L                                                  $+2.97|
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
|  2026-07-17  SELL  EBAY  Pullback50  $93.44  P&L $+0.30                |
|  2026-07-17  SELL  CMS  Pullback50  $22.29  P&L $-0.14                 |
|  2026-07-17  SELL  DOV  Pullback50  $81.38  P&L $-0.50                 |
|  2026-07-17  SELL  DRI  Pullback50  $95.97  P&L $-0.89                 |
|  2026-07-17  SELL  BG  Pullback50  $97.67  P&L $-0.08                  |
|  2026-07-17  SELL  CNP  Pullback50  $99.12  P&L $+2.36                 |
+========================================================================+
```

### Options bot full output

```text
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-20T09:00:38.414950-04:00 ===

[Run context]
After hours (09:00 ET) — exit summary only.
Paper auth OK — equity $128229.53, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $128,229.53                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
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
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=2.2s reconcile=1.98s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=2.2s. run=#4394 https://github.com/28twagg-ops/TradingBot/actions/runs/29744391750
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 3.6% (22/604)
  File "/home/runner/work/TradingBot/TradingBot/scripts/options_signal_frequency.py", line 80
    return f"{day}|{sid}|{re.sub(r'\s+', ' ', line.strip())[:160]}"
                                                                   ^
SyntaxError: f-string expression part cannot include a backslash
signal_frequency report failed (non-fatal)
## Ledger health — 2026-07-20
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |    27 | WARN | <<<
| Missing exit records (post) |    27 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |   264 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
```

---

## Run 20260720T130537Z

- UTC timestamp: `20260720T130537Z`
- GitHub run: [#4395](https://github.com/28twagg-ops/TradingBot/actions/runs/29744728347)
- Run id: `29744728347`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`4s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T09:05:40.923839-04:00","date":"2026-07-20","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":2.4,"phases_s":{"reconcile":2.03},"signals":0,"placed":0,"equity":129093.53,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4395","github_run_id":"29744728347","status":"ok"}
```

### Live bot full output

```text
13:05:38  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:05 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $484.78|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $484.78|
|  Cash                                                           $302.65|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $182.13|
|  Open P&L                                                        $+2.97|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (2 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CARR     Pullback50      $88.50     $67.89   $69.85   +2.9%   $+2.48  |
|  EMR      Pullback50      $93.63     $139.30  $140.03  +0.5%   $+0.49  |
|                                                                        |
|  Total invested                                                 $182.13|
|  Total open P&L                                                  $+2.97|
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
|  2026-07-17  SELL  EBAY  Pullback50  $93.44  P&L $+0.30                |
|  2026-07-17  SELL  CMS  Pullback50  $22.29  P&L $-0.14                 |
|  2026-07-17  SELL  DOV  Pullback50  $81.38  P&L $-0.50                 |
|  2026-07-17  SELL  DRI  Pullback50  $95.97  P&L $-0.89                 |
|  2026-07-17  SELL  BG  Pullback50  $97.67  P&L $-0.08                  |
|  2026-07-17  SELL  CNP  Pullback50  $99.12  P&L $+2.36                 |
+========================================================================+
```

### Options bot full output

```text
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-20T09:05:40.923839-04:00 ===

[Run context]
After hours (09:05 ET) — exit summary only.
Paper auth OK — equity $129093.53, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $129,093.53                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
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
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=2.4s reconcile=2.03s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=2.4s. run=#4395 https://github.com/28twagg-ops/TradingBot/actions/runs/29744728347
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 3.6% (22/604)
  File "/home/runner/work/TradingBot/TradingBot/scripts/options_signal_frequency.py", line 80
    return f"{day}|{sid}|{re.sub(r'\s+', ' ', line.strip())[:160]}"
                                                                   ^
SyntaxError: f-string expression part cannot include a backslash
signal_frequency report failed (non-fatal)
## Ledger health — 2026-07-20
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |    27 | WARN | <<<
| Missing exit records (post) |    27 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |   264 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
```

---

## Run 20260720T131034Z

- UTC timestamp: `20260720T131034Z`
- GitHub run: [#4396](https://github.com/28twagg-ops/TradingBot/actions/runs/29745074327)
- Run id: `29745074327`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`7s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T09:10:36.151186-04:00","date":"2026-07-20","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":5.5,"phases_s":{"reconcile":5.26},"signals":0,"placed":0,"equity":128932.49,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4396","github_run_id":"29745074327","status":"ok"}
```

### Live bot full output

```text
13:10:35  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $484.78|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $484.78|
|  Cash                                                           $302.65|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $182.13|
|  Open P&L                                                        $+2.97|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (2 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CARR     Pullback50      $88.50     $67.89   $69.85   +2.9%   $+2.48  |
|  EMR      Pullback50      $93.63     $139.30  $140.03  +0.5%   $+0.49  |
|                                                                        |
|  Total invested                                                 $182.13|
|  Total open P&L                                                  $+2.97|
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
|  2026-07-17  SELL  EBAY  Pullback50  $93.44  P&L $+0.30                |
|  2026-07-17  SELL  CMS  Pullback50  $22.29  P&L $-0.14                 |
|  2026-07-17  SELL  DOV  Pullback50  $81.38  P&L $-0.50                 |
|  2026-07-17  SELL  DRI  Pullback50  $95.97  P&L $-0.89                 |
|  2026-07-17  SELL  BG  Pullback50  $97.67  P&L $-0.08                  |
|  2026-07-17  SELL  CNP  Pullback50  $99.12  P&L $+2.36                 |
+========================================================================+
```

### Options bot full output

```text
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-20T09:10:36.151186-04:00 ===

[Run context]
After hours (09:10 ET) — exit summary only.
Paper auth OK — equity $128932.49, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $128,932.49                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
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
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=5.5s reconcile=5.26s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=5.5s. run=#4396 https://github.com/28twagg-ops/TradingBot/actions/runs/29745074327
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 3.6% (22/604)
  File "/home/runner/work/TradingBot/TradingBot/scripts/options_signal_frequency.py", line 80
    return f"{day}|{sid}|{re.sub(r'\s+', ' ', line.strip())[:160]}"
                                                                   ^
SyntaxError: f-string expression part cannot include a backslash
signal_frequency report failed (non-fatal)
## Ledger health — 2026-07-20
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |    27 | WARN | <<<
| Missing exit records (post) |    27 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |   264 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
```

---

## Run 20260720T131536Z

- UTC timestamp: `20260720T131536Z`
- GitHub run: [#4397](https://github.com/28twagg-ops/TradingBot/actions/runs/29745441251)
- Run id: `29745441251`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`3s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T09:15:38.981520-04:00","date":"2026-07-20","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":2.0,"phases_s":{"reconcile":1.67},"signals":0,"placed":0,"equity":128321.33,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4397","github_run_id":"29745441251","status":"ok"}
```

### Live bot full output

```text
13:15:37  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:15 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $484.78|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $484.78|
|  Cash                                                           $302.65|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $182.13|
|  Open P&L                                                        $+2.97|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (2 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CARR     Pullback50      $88.50     $67.89   $69.85   +2.9%   $+2.48  |
|  EMR      Pullback50      $93.63     $139.30  $140.03  +0.5%   $+0.49  |
|                                                                        |
|  Total invested                                                 $182.13|
|  Total open P&L                                                  $+2.97|
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
|  2026-07-17  SELL  EBAY  Pullback50  $93.44  P&L $+0.30                |
|  2026-07-17  SELL  CMS  Pullback50  $22.29  P&L $-0.14                 |
|  2026-07-17  SELL  DOV  Pullback50  $81.38  P&L $-0.50                 |
|  2026-07-17  SELL  DRI  Pullback50  $95.97  P&L $-0.89                 |
|  2026-07-17  SELL  BG  Pullback50  $97.67  P&L $-0.08                  |
|  2026-07-17  SELL  CNP  Pullback50  $99.12  P&L $+2.36                 |
+========================================================================+
```

### Options bot full output

```text
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-20T09:15:38.981520-04:00 ===

[Run context]
After hours (09:15 ET) — exit summary only.
Paper auth OK — equity $128321.33, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $128,321.33                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
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
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=2.0s reconcile=1.67s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=2.0s. run=#4397 https://github.com/28twagg-ops/TradingBot/actions/runs/29745441251
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 3.6% (22/604)
  File "/home/runner/work/TradingBot/TradingBot/scripts/options_signal_frequency.py", line 80
    return f"{day}|{sid}|{re.sub(r'\s+', ' ', line.strip())[:160]}"
                                                                   ^
SyntaxError: f-string expression part cannot include a backslash
signal_frequency report failed (non-fatal)
## Ledger health — 2026-07-20
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |    27 | WARN | <<<
| Missing exit records (post) |    27 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |   264 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
```

---

## Run 20260720T132039Z

- UTC timestamp: `20260720T132039Z`
- GitHub run: [#4398](https://github.com/28twagg-ops/TradingBot/actions/runs/29745808029)
- Run id: `29745808029`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`4s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T09:20:41.522515-04:00","date":"2026-07-20","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.9,"phases_s":{"reconcile":1.62},"signals":0,"placed":0,"equity":128578.85,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4398","github_run_id":"29745808029","status":"ok"}
```

### Live bot full output

```text
13:20:39  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $484.78|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $484.78|
|  Cash                                                           $302.65|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $182.13|
|  Open P&L                                                        $+2.97|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (2 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CARR     Pullback50      $88.50     $67.89   $69.85   +2.9%   $+2.48  |
|  EMR      Pullback50      $93.63     $139.30  $140.03  +0.5%   $+0.49  |
|                                                                        |
|  Total invested                                                 $182.13|
|  Total open P&L                                                  $+2.97|
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
|  2026-07-17  SELL  EBAY  Pullback50  $93.44  P&L $+0.30                |
|  2026-07-17  SELL  CMS  Pullback50  $22.29  P&L $-0.14                 |
|  2026-07-17  SELL  DOV  Pullback50  $81.38  P&L $-0.50                 |
|  2026-07-17  SELL  DRI  Pullback50  $95.97  P&L $-0.89                 |
|  2026-07-17  SELL  BG  Pullback50  $97.67  P&L $-0.08                  |
|  2026-07-17  SELL  CNP  Pullback50  $99.12  P&L $+2.36                 |
+========================================================================+
```

### Options bot full output

```text
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-20T09:20:41.522515-04:00 ===

[Run context]
After hours (09:20 ET) — exit summary only.
Paper auth OK — equity $128578.85, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $128,578.85                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
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
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=1.9s reconcile=1.62s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.9s. run=#4398 https://github.com/28twagg-ops/TradingBot/actions/runs/29745808029
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 3.6% (22/604)
  File "/home/runner/work/TradingBot/TradingBot/scripts/options_signal_frequency.py", line 80
    return f"{day}|{sid}|{re.sub(r'\s+', ' ', line.strip())[:160]}"
                                                                   ^
SyntaxError: f-string expression part cannot include a backslash
signal_frequency report failed (non-fatal)
## Ledger health — 2026-07-20
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |    27 | WARN | <<<
| Missing exit records (post) |    27 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |   264 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
```

---

## Run 20260720T132535Z

- UTC timestamp: `20260720T132535Z`
- GitHub run: [#4399](https://github.com/28twagg-ops/TradingBot/actions/runs/29746157854)
- Run id: `29746157854`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`3s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T09:25:37.764773-04:00","date":"2026-07-20","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.9,"phases_s":{"reconcile":1.63},"signals":0,"placed":0,"equity":128365.53,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"4399","github_run_id":"29746157854","status":"ok"}
```

### Live bot full output

```text
13:25:36  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:25 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $484.78|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $484.78|
|  Cash                                                           $302.65|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $182.13|
|  Open P&L                                                        $+2.97|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (2 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CARR     Pullback50      $88.50     $67.89   $69.85   +2.9%   $+2.48  |
|  EMR      Pullback50      $93.63     $139.30  $140.03  +0.5%   $+0.49  |
|                                                                        |
|  Total invested                                                 $182.13|
|  Total open P&L                                                  $+2.97|
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
|  2026-07-17  SELL  EBAY  Pullback50  $93.44  P&L $+0.30                |
|  2026-07-17  SELL  CMS  Pullback50  $22.29  P&L $-0.14                 |
|  2026-07-17  SELL  DOV  Pullback50  $81.38  P&L $-0.50                 |
|  2026-07-17  SELL  DRI  Pullback50  $95.97  P&L $-0.89                 |
|  2026-07-17  SELL  BG  Pullback50  $97.67  P&L $-0.08                  |
|  2026-07-17  SELL  CNP  Pullback50  $99.12  P&L $+2.36                 |
+========================================================================+
```

### Options bot full output

```text
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-20T09:25:37.764773-04:00 ===

[Run context]
After hours (09:25 ET) — exit summary only.
Paper auth OK — equity $128365.53, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $128,365.53                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
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
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=1.9s reconcile=1.63s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.9s. run=#4399 https://github.com/28twagg-ops/TradingBot/actions/runs/29746157854
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 3.6% (22/604)
  File "/home/runner/work/TradingBot/TradingBot/scripts/options_signal_frequency.py", line 80
    return f"{day}|{sid}|{re.sub(r'\s+', ' ', line.strip())[:160]}"
                                                                   ^
SyntaxError: f-string expression part cannot include a backslash
signal_frequency report failed (non-fatal)
## Ledger health — 2026-07-20
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |    27 | WARN | <<<
| Missing exit records (post) |    27 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |   264 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
```

---

## Run 20260720T133038Z

- UTC timestamp: `20260720T133038Z`
- GitHub run: [#4400](https://github.com/28twagg-ops/TradingBot/actions/runs/29746501287)
- Run id: `29746501287`
- Live bot: exit=`0`, duration=`217s`
- Options bot: exit=`0`, duration=`37s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T09:34:16.564381-04:00","date":"2026-07-20","mode":"entry+manage","header":"entry+manage (5 new)","elapsed_s":34.7,"phases_s":{"reconcile":1.96,"cancel":0.14,"manage":0.13,"scan":16.51,"entries":13.37,"reconcile2":2.01},"signals":21,"placed":5,"equity":129660.09,"open_positions":1,"pending_orders":0,"open_lots":5,"submitted_today":5,"filled_today":5,"unattributed_contracts":0,"top_signals":["S173:ADM","S173:AXON","S173:FANG","S173:GDDY","S173:HONA","S173:ORCL","S173:CRM","S173:DOCS"],"github_run":"4400","github_run_id":"29746501287","status":"ok"}
```

### Live bot full output

```text
13:30:39  INFO      Mode: morning_prep
13:30:42  INFO        [prep_positions] 2/2 (2 valid)
13:30:42  INFO      Fetching tickers (universe=both)...
13:30:43  INFO        S&P 500: 503
13:30:43  INFO        MidCap 400: 400
13:30:43  INFO        Total: 903 tickers
13:30:45  INFO        [prep_universe] 40/901 (40 valid)
13:30:47  INFO        [prep_universe] 80/901 (80 valid)
13:30:49  INFO        [prep_universe] 120/901 (120 valid)
13:30:52  INFO        [prep_universe] 160/901 (160 valid)
13:30:53  INFO        [prep_universe] 200/901 (199 valid)
13:30:58  INFO        [prep_universe] 240/901 (238 valid)
13:31:09  INFO        [prep_universe] 280/901 (278 valid)
13:31:20  INFO        [prep_universe] 320/901 (318 valid)
13:31:34  INFO        [prep_universe] 360/901 (358 valid)
13:31:44  INFO        [prep_universe] 400/901 (397 valid)
13:31:58  INFO        [prep_universe] 440/901 (437 valid)
13:32:08  INFO        [prep_universe] 480/901 (477 valid)
13:32:21  INFO        [prep_universe] 520/901 (517 valid)
13:32:32  INFO        [prep_universe] 560/901 (556 valid)
13:32:45  INFO        [prep_universe] 600/901 (596 valid)
13:32:56  INFO        [prep_universe] 640/901 (636 valid)
13:33:09  INFO        [prep_universe] 680/901 (676 valid)
13:33:19  INFO        [prep_universe] 720/901 (715 valid)
13:33:33  INFO        [prep_universe] 760/901 (755 valid)
13:33:46  INFO        [prep_universe] 800/901 (795 valid)
13:33:56  INFO        [prep_universe] 840/901 (834 valid)
13:34:10  INFO        [prep_universe] 880/901 (874 valid)
13:34:14  INFO        [prep_universe] 901/901 (895 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:30 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $483.34|
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
|  Open positions                                                       2|
|  Invested                                                       $180.69|
|  Open P&L                                                        $+1.53|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CARR     Pullback50      $87.41     $67.89   $68.99   +1.6%   $+1.39  |
|  EMR      Pullback50      $93.28     $139.30  $139.51  +0.1%   $+0.14  |
+========================================================================+

+========================================================================+
|                            OPEN SELL ORDERS                            |
+========================================================================+
|  Count                                                                1|
|  TICKER    TYPE              QTY       LIMIT       STOP                |
+------------------------------------------------------------------------+
|  CARR      OrderType.STOP    1         None        67.55               |
+========================================================================+

+========================================================================+
|                              PREP SUMMARY                              |
+========================================================================+
|  Saved                                                              yes|
|  Exit candidates                                                      2|
|  Signal candidates                                                   43|
|  Universe scanned                                                   901|
+========================================================================+
```

### Options bot full output

```text
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-20T09:34:16.564381-04:00 ===

[Run context]
Paper auth OK — equity $129688.09, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 21 signal(s); top: ['S173:ADM', 'S173:AXON', 'S173:FANG', 'S173:GDDY', 'S173:HONA', 'S173:ORCL', 'S173:CRM', 'S173:DOCS']
Paper lab: $129745 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 80 no tradeable call, 20 pending order
Placed 5 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $129,660.09                             |
|  Signals this run              21                                      |
|  Orders submitted (session)    5                                       |
|  Orders filled today (ledger)  5                                       |
|  Entries placed this run       5                                       |
|  Open virtual lots             5                                       |
|  Broker option positions       1                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=493  buckets=49  win=34%                             |
|  Returns   avg=+7.2%  med=-33.9%  p10=-77.0%  p90=+93.9%               |
|  Realized  $+3,526.77                                                  |
|  Raw incl dropped  trades=607  real=$+2,028.58                         |
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
|  OPEN OPTIONS (1)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  CRM260724C00185000            5    -14.3%   $    -45.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=34.7s reconcile=1.96s cancel=0.14s manage=0.13s scan=16.51s entries=13.37s
STATUS: options_morning_bot run complete (PAPER) elapsed=34.7s. run=#4400 https://github.com/28twagg-ops/TradingBot/actions/runs/29746501287
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 3.6% (22/607)
  File "/home/runner/work/TradingBot/TradingBot/scripts/options_signal_frequency.py", line 80
    return f"{day}|{sid}|{re.sub(r'\s+', ' ', line.strip())[:160]}"
                                                                   ^
SyntaxError: f-string expression part cannot include a backslash
signal_frequency report failed (non-fatal)
## Ledger health — 2026-07-20
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |    27 | WARN | <<<
| Missing exit records (post) |    27 | WARN | <<<
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |     5 | INFO |
| Total closed lots           |   267 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
```

---

## Run 20260720T133537Z

- UTC timestamp: `20260720T133537Z`
- GitHub run: [#4401](https://github.com/28twagg-ops/TradingBot/actions/runs/29746866282)
- Run id: `29746866282`
- Live bot: exit=`0`, duration=`215s`
- Options bot: exit=`0`, duration=`23s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T09:39:12.770159-04:00","date":"2026-07-20","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":21.6,"phases_s":{"reconcile":1.67,"cancel":0.03,"manage":0.32,"scan":16.79,"entries":2.47},"signals":24,"placed":0,"equity":129893.43,"open_positions":1,"pending_orders":0,"open_lots":5,"submitted_today":5,"filled_today":5,"unattributed_contracts":0,"top_signals":["S173:ADM","S173:AXON","S173:FANG","S173:GDDY","S173:HONA","S173:ORCL","S173:CRM","S173:NOW"],"github_run":"4401","github_run_id":"29746866282","status":"ok"}
```

### Live bot full output

```text
13:35:38  INFO      Mode: morning_prep
13:35:39  INFO        [prep_positions] 2/2 (2 valid)
13:35:39  INFO        Universe cache hit: 903 tickers (tickers_2026-07-20.json)
13:35:40  INFO        [prep_universe] 40/901 (40 valid)
13:35:41  INFO        [prep_universe] 80/901 (80 valid)
13:35:42  INFO        [prep_universe] 120/901 (120 valid)
13:35:44  INFO        [prep_universe] 160/901 (160 valid)
13:35:45  INFO        [prep_universe] 200/901 (199 valid)
13:35:52  INFO        [prep_universe] 240/901 (238 valid)
13:36:05  INFO        [prep_universe] 280/901 (278 valid)
13:36:18  INFO        [prep_universe] 320/901 (318 valid)
13:36:28  INFO        [prep_universe] 360/901 (358 valid)
13:36:41  INFO        [prep_universe] 400/901 (397 valid)
13:36:54  INFO        [prep_universe] 440/901 (437 valid)
13:37:04  INFO        [prep_universe] 480/901 (477 valid)
13:37:17  INFO        [prep_universe] 520/901 (517 valid)
13:37:30  INFO        [prep_universe] 560/901 (556 valid)
13:37:43  INFO        [prep_universe] 600/901 (596 valid)
13:37:52  INFO        [prep_universe] 640/901 (636 valid)
13:38:05  INFO        [prep_universe] 680/901 (676 valid)
13:38:18  INFO        [prep_universe] 720/901 (715 valid)
13:38:28  INFO        [prep_universe] 760/901 (755 valid)
13:38:41  INFO        [prep_universe] 800/901 (795 valid)
13:38:54  INFO        [prep_universe] 840/901 (834 valid)
13:39:04  INFO        [prep_universe] 880/901 (874 valid)
13:39:10  INFO        [prep_universe] 901/901 (895 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:35 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $481.93|
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
|  Open positions                                                       2|
|  Invested                                                       $179.28|
|  Open P&L                                                        $+0.12|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CARR     Pullback50      $86.71     $67.89   $68.44   +0.8%   $+0.69  |
|  EMR      Pullback50      $92.56     $139.30  $138.44  -0.6%   $-0.58  |
+========================================================================+

+========================================================================+
|                            OPEN SELL ORDERS                            |
+========================================================================+
|  Count                                                                1|
|  TICKER    TYPE              QTY       LIMIT       STOP                |
+------------------------------------------------------------------------+
|  CARR      OrderType.STOP    1         None        67.55               |
+========================================================================+

+========================================================================+
|                              PREP SUMMARY                              |
+========================================================================+
|  Saved                                                              yes|
|  Exit candidates                                                      2|
|  Signal candidates                                                   22|
|  Universe scanned                                                   901|
+========================================================================+
```

### Options bot full output

```text
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-20T09:39:12.770159-04:00 ===

[Run context]
Paper auth OK — equity $129893.43, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 24 signal(s); top: ['S173:ADM', 'S173:AXON', 'S173:FANG', 'S173:GDDY', 'S173:HONA', 'S173:ORCL', 'S173:CRM', 'S173:NOW']
Paper lab: $129822 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 50 no tradeable call
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $129,893.43                             |
|  Signals this run              24                                      |
|  Orders submitted (session)    5                                       |
|  Orders filled today (ledger)  5                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             5                                       |
|  Broker option positions       1                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=494  buckets=49  win=34%                             |
|  Returns   avg=+7.3%  med=-33.8%  p10=-77.0%  p90=+93.8%               |
|  Realized  $+3,557.77                                                  |
|  Raw incl dropped  trades=608  real=$+2,059.58                         |
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
|  OPEN OPTIONS (1)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  CRM260724C00185000            5     -4.8%   $    -15.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=21.6s reconcile=1.67s cancel=0.03s manage=0.32s scan=16.79s entries=2.47s
STATUS: options_morning_bot run complete (PAPER) elapsed=21.6s. run=#4401 https://github.com/28twagg-ops/TradingBot/actions/runs/29746866282
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 3.6% (22/608)
  File "/home/runner/work/TradingBot/TradingBot/scripts/options_signal_frequency.py", line 80
    return f"{day}|{sid}|{re.sub(r'\s+', ' ', line.strip())[:160]}"
                                                                   ^
SyntaxError: f-string expression part cannot include a backslash
signal_frequency report failed (non-fatal)
## Ledger health — 2026-07-20
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |    27 | WARN | <<<
| Missing exit records (post) |    27 | WARN | <<<
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |     5 | INFO |
| Total closed lots           |   267 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
```

---

## Run 20260720T134043Z

- UTC timestamp: `20260720T134043Z`
- GitHub run: [#4402](https://github.com/28twagg-ops/TradingBot/actions/runs/29747227265)
- Run id: `29747227265`
- Live bot: exit=`0`, duration=`217s`
- Options bot: exit=`0`, duration=`30s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T09:44:20.965121-04:00","date":"2026-07-20","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":28.4,"phases_s":{"reconcile":2.1,"cancel":0.16,"manage":1.38,"scan":15.49,"entries":8.17},"signals":24,"placed":0,"equity":129231.43,"open_positions":1,"pending_orders":0,"open_lots":5,"submitted_today":5,"filled_today":5,"unattributed_contracts":0,"top_signals":["S173:ADM","S173:ADSK","S173:AXON","S173:FANG","S173:IT","S173:GDDY","S173:ORCL","S173:CRM"],"github_run":"4402","github_run_id":"29747227265","status":"ok"}
```

### Live bot full output

```text
13:40:44  INFO      Mode: morning_prep
13:40:46  INFO        [prep_positions] 2/2 (2 valid)
13:40:46  INFO        Universe cache hit: 903 tickers (tickers_2026-07-20.json)
13:40:47  INFO        [prep_universe] 40/901 (40 valid)
13:40:49  INFO        [prep_universe] 80/901 (80 valid)
13:40:50  INFO        [prep_universe] 120/901 (120 valid)
13:40:51  INFO        [prep_universe] 160/901 (160 valid)
13:40:53  INFO        [prep_universe] 200/901 (199 valid)
13:41:00  INFO        [prep_universe] 240/901 (238 valid)
13:41:13  INFO        [prep_universe] 280/901 (278 valid)
13:41:24  INFO        [prep_universe] 320/901 (318 valid)
13:41:37  INFO        [prep_universe] 360/901 (358 valid)
13:41:48  INFO        [prep_universe] 400/901 (397 valid)
13:42:01  INFO        [prep_universe] 440/901 (437 valid)
13:42:11  INFO        [prep_universe] 480/901 (477 valid)
13:42:25  INFO        [prep_universe] 520/901 (517 valid)
13:42:35  INFO        [prep_universe] 560/901 (556 valid)
13:42:49  INFO        [prep_universe] 600/901 (596 valid)
13:42:59  INFO        [prep_universe] 640/901 (636 valid)
13:43:12  INFO        [prep_universe] 680/901 (676 valid)
13:43:23  INFO        [prep_universe] 720/901 (715 valid)
13:43:36  INFO        [prep_universe] 760/901 (755 valid)
13:43:47  INFO        [prep_universe] 800/901 (795 valid)
13:44:00  INFO        [prep_universe] 840/901 (834 valid)
13:44:11  INFO        [prep_universe] 880/901 (874 valid)
13:44:18  INFO        [prep_universe] 901/901 (895 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:40 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.36|
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
|  Open positions                                                       2|
|  Invested                                                       $179.71|
|  Open P&L                                                        $+0.55|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CARR     Pullback50      $87.12     $67.89   $68.76   +1.3%   $+1.10  |
|  EMR      Pullback50      $92.59     $139.30  $138.48  -0.6%   $-0.55  |
+========================================================================+

+========================================================================+
|                            OPEN SELL ORDERS                            |
+========================================================================+
|  Count                                                                1|
|  TICKER    TYPE              QTY       LIMIT       STOP                |
+------------------------------------------------------------------------+
|  CARR      OrderType.STOP    1         None        67.55               |
+========================================================================+

+========================================================================+
|                              PREP SUMMARY                              |
+========================================================================+
|  Saved                                                              yes|
|  Exit candidates                                                      2|
|  Signal candidates                                                   25|
|  Universe scanned                                                   901|
+========================================================================+
```

### Options bot full output

```text
Layout: controlled:100:c000_s173_w1_0928_1005_r1
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-07-20T09:44:20.965121-04:00 ===

[Run context]
Paper auth OK — equity $129193.43, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 24 signal(s); top: ['S173:ADM', 'S173:ADSK', 'S173:AXON', 'S173:FANG', 'S173:IT', 'S173:GDDY', 'S173:ORCL', 'S173:CRM']
Paper lab: $129358 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 50 no tradeable call
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $129,231.43                             |
|  Signals this run              24                                      |
|  Orders submitted (session)    5                                       |
|  Orders filled today (ledger)  5                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             5                                       |
|  Broker option positions       1                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=495  buckets=49  win=34%                             |
|  Returns   avg=+7.4%  med=-33.8%  p10=-77.0%  p90=+93.7%               |
|  Realized  $+3,579.77                                                  |
|  Raw incl dropped  trades=609  real=$+2,081.58                         |
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
|  OPEN OPTIONS (1)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  CRM260724C00185000            5    +19.0%   $    +60.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=28.4s reconcile=2.1s cancel=0.16s manage=1.38s scan=15.49s entries=8.17s
STATUS: options_morning_bot run complete (PAPER) elapsed=28.4s. run=#4402 https://github.com/28twagg-ops/TradingBot/actions/runs/29747227265
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 3.6% (22/609)
  File "/home/runner/work/TradingBot/TradingBot/scripts/options_signal_frequency.py", line 80
    return f"{day}|{sid}|{re.sub(r'\s+', ' ', line.strip())[:160]}"
                                                                   ^
SyntaxError: f-string expression part cannot include a backslash
signal_frequency report failed (non-fatal)
## Ledger health — 2026-07-20
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |    27 | WARN | <<<
| Missing exit records (post) |    27 | WARN | <<<
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |     5 | INFO |
| Total closed lots           |   267 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
```

---

## Run 20260720T134534Z

- UTC timestamp: `20260720T134534Z`
- GitHub run: [#4403](https://github.com/28twagg-ops/TradingBot/actions/runs/29747585055)
- Run id: `29747585055`
- Live bot: exit=`0`, duration=`0s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T09:44:20.965121-04:00","date":"2026-07-20","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":28.4,"phases_s":{"reconcile":2.1,"cancel":0.16,"manage":1.38,"scan":15.49,"entries":8.17},"signals":24,"placed":0,"equity":129231.43,"open_positions":1,"pending_orders":0,"open_lots":5,"submitted_today":5,"filled_today":5,"unattributed_contracts":0,"top_signals":["S173:ADM","S173:ADSK","S173:AXON","S173:FANG","S173:IT","S173:GDDY","S173:ORCL","S173:CRM"],"github_run":"4402","github_run_id":"29747227265","status":"ok"}
```

### Live bot full output

```text
13:45:35  INFO      Mode: morning_scan
13:45:35  INFO        [positions] 2/2 (2 valid)
13:45:35  INFO        SELL LIMIT EMR  qty=0.668609659  limit=$138.63  id=f438205f-cea6-4357-82e2-c69f8d13de52
13:45:56  INFO        SELL LIMIT filled EMR (confirmed by position check)
13:45:56  INFO        TX logged: SELL EMR  P&L -0.28%
13:45:56  INFO        SELL order cancelled CARR  type=OrderType.STOP  id=e3b06fff-6c14-4de5-95e1-cb325b0d5d06
13:45:56  INFO        SELL LIMIT CARR  qty=1.267012313  limit=$68.60  id=6ee540c0-b440-4fe7-b969-65e6539b417f
13:46:16  INFO        SELL LIMIT filled CARR (confirmed by position check)
13:46:16  INFO        TX logged: SELL CARR  P&L 1.54%
13:46:16  INFO        Universe cache hit: 903 tickers (tickers_2026-07-20.json)
13:46:17  INFO        [universe] 40/903 (40 valid)
13:46:18  INFO        [universe] 80/903 (80 valid)
13:46:19  INFO        [universe] 120/903 (120 valid)
13:46:21  INFO        [universe] 160/903 (160 valid)
13:46:22  INFO        [universe] 200/903 (199 valid)
13:46:29  INFO        [universe] 240/903 (238 valid)
13:46:42  INFO        [universe] 280/903 (278 valid)
13:46:55  INFO        [universe] 320/903 (318 valid)
13:47:05  INFO        [universe] 360/903 (358 valid)
13:47:18  INFO        [universe] 400/903 (397 valid)
13:47:31  INFO        [universe] 440/903 (437 valid)
13:47:41  INFO        [universe] 480/903 (477 valid)
13:47:54  INFO        [universe] 520/903 (517 valid)
13:48:07  INFO        [universe] 560/903 (556 valid)
13:48:17  INFO        [universe] 600/903 (596 valid)
13:48:30  INFO        [universe] 640/903 (636 valid)
13:48:42  INFO        [universe] 680/903 (676 valid)
13:48:55  INFO        [universe] 720/903 (715 valid)
13:49:05  INFO        [universe] 760/903 (755 valid)
13:49:18  INFO        [universe] 800/903 (795 valid)
13:49:31  INFO        [universe] 840/903 (834 valid)
13:49:41  INFO        [universe] 880/903 (874 valid)
13:49:48  INFO        [universe] 903/903 (897 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_SCAN|
|  Time                                                         13:45 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.87|
+========================================================================+

+========================================================================+
|                   RUBBER BAND BOT v8  --  DAILY SCAN                   |
+========================================================================+
|  Mode                                                      *** LIVE ***|
|  Date                                                        2026-07-20|
|  Universe                                                          both|
|  Month                                        Jul: 52wkLow + Pullback50|
|  Regime                                                            BULL|
|  Exit                                      midline / stop-0.5% / 3d max|
+========================================================================+

+========================================================================+
|                                ACCOUNT                                 |
+========================================================================+
|  Equity                                                         $482.87|
|  Cash                                                           $302.65|
|  Reserve                                          $24.14  (always kept)|
|  Available                                    $278.51  (for new trades)|
|  Seasonal trade                   $96.57  (20% -- scheduled strategies)|
|  Off-sched trade                      $96.57  (20% -- other strategies)|
+========================================================================+

+========================================================================+
|                           HOLDINGS  (2 open)                           |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CARR     Pullback50      $87.35     $67.89   $68.94   +1.5%   $+1.33  |
|  EMR      Pullback50      $92.88     $139.30  $138.91  -0.3%   $-0.26  |
|                                                                        |
|  Total invested                                                 $180.22|
|  Total open P&L                                                  $+1.06|
|  Buys today: 0  |  entry cap: 3  |  max open: 5                        |
+========================================================================+

+========================================================================+
|                               PLAN CACHE                               |
+========================================================================+
|  Mode                                                           morning|
|  File                                      logs/plans/morning_plan.json|
|  Use cached plan                                  no (stale (15840.1m))|
+========================================================================+

+========================================================================+
|          EXIT EVALUATION  (EOD -- midline + stop + max-hold)           |
+========================================================================+
|  EMR  P&L -0.3%  $-0.26                       EXIT: max_hold 3d (-0.3%)|
|  CARR  P&L +1.5%  $+1.33                      EXIT: max_hold 4d (+1.5%)|
+========================================================================+

+========================================================================+
|                           EXIT EVAL SUMMARY                            |
+========================================================================+
|  Exit eval    attempted 2 | filled 2 | partial 0 | pending 0 | failed 0|
|  Other skips     already logged today 0  |  no price data 0  |  holds 0|
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
|                         SIGNALS FOUND  --  26                          |
+========================================================================+
|  TICKER   STRATEGY        TIER   PRICE    RSI    VOL_Z   TRIGGER       |
+------------------------------------------------------------------------+
|  AMZN     Pullback50      SEAS   $250.23  63.5   -1.13   50MA bounce (-|
|  BG       Pullback50      SEAS   $119.78  70.8   -2.19   50MA bounce (+|
|  CNP      Pullback50      SEAS   $43.34   40.2   -2.55   50MA bounce (+|
|  KO       Pullback50      SEAS   $81.84   47.7   -1.75   50MA bounce (+|
|  COP      Pullback50      SEAS   $114.23  71.4   -2.92   50MA bounce (+|
|  XOM      Pullback50      SEAS   $147.25  74.1   -2.67   50MA bounce (+|
|  HON      Pullback50      SEAS   $225.19  46.9   -1.36   50MA bounce (+|
|  IRM      Pullback50      SEAS   $125.25  41.6   -3.11   50MA bounce (-|
|  MAA      Pullback50      SEAS   $133.31  34.6   -3.42   50MA bounce (-|
|  NEE      Pullback50      SEAS   $89.00   51.5   -3.07   50MA bounce (+|
|  OXY      Pullback50      SEAS   $54.71   71.1   -2.24   50MA bounce (-|
|  TPR      Pullback50      SEAS   $141.87  42.0   -2.15   50MA bounce (+|
|  VRSN     Pullback50      SEAS   $278.87  92.3   -2.18   50MA bounce (-|
|  WEC      Pullback50      SEAS   $113.81  37.0   -2.83   50MA bounce (+|
|  WMB      Pullback50      SEAS   $74.67   48.5   -2.36   50MA bounce (+|
|  XEL      Pullback50      SEAS   $79.56   41.0   -3.06   50MA bounce (+|
|  AVT      Pullback50      SEAS   $87.03   48.6   -2.30   50MA bounce (+|
|  COLM     Pullback50      SEAS   $63.53   59.0   -2.67   50MA bounce (+|
|  DTM      Pullback50      SEAS   $146.27  46.2   -3.38   50MA bounce (+|
|  HGV      Pullback50      SEAS   $49.95   36.1   -2.05   50MA bounce (-|
|  IRT      Pullback50      SEAS   $16.64   47.5   -1.69   50MA bounce (+|
|  MTDR     Pullback50      SEAS   $53.24   66.0   -2.76   50MA bounce (-|
|  MUR      Pullback50      SEAS   $36.52   62.0   -1.84   50MA bounce (+|
|  NOV      Pullback50      SEAS   $19.63   68.0   -1.82   50MA bounce (-|
|  RRX      Pullback50      SEAS   $211.78  44.8   -1.97   50MA bounce (+|
|  VMI      Pullback50      SEAS   $539.71  33.1   -1.84   50MA bounce (+|
|                                                                        |
+========================================================================+

+========================================================================+
|                              ENTRY ORDERS                              |13:49:49  INFO        BUY  AMZN  $96.57  [Pullback50]  id=93fbae13-ad84-4212-8696-b448c9a0f752
13:49:50  INFO        BUY  BG  $96.57  [Pullback50]  id=a9f6ea17-2ac2-4e11-b587-97eed58251ca
13:49:50  INFO        BUY  CNP  $96.57  [Pullback50]  id=ec40d919-f73e-43c7-99e4-ac62877f142f
13:49:50  INFO        BUY  KO  $96.57  [Pullback50]  id=6e2a24b5-6591-45da-a39d-28cf450b931b
```

### Options bot full output

```text

## Run 20260720T135101Z

- UTC timestamp: `20260720T135101Z`
- GitHub run: [#4404](https://github.com/28twagg-ops/TradingBot/actions/runs/29747954147)
- Run id: `29747954147`
- Live bot: exit=`0`, duration=`0s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T09:44:20.965121-04:00","date":"2026-07-20","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":28.4,"phases_s":{"reconcile":2.1,"cancel":0.16,"manage":1.38,"scan":15.49,"entries":8.17},"signals":24,"placed":0,"equity":129231.43,"open_positions":1,"pending_orders":0,"open_lots":5,"submitted_today":5,"filled_today":5,"unattributed_contracts":0,"top_signals":["S173:ADM","S173:ADSK","S173:AXON","S173:FANG","S173:IT","S173:GDDY","S173:ORCL","S173:CRM"],"github_run":"4402","github_run_id":"29747227265","status":"ok"}
```

### Live bot full output

```text
13:51:02  INFO      Mode: morning_scan
13:51:03  INFO        [positions] 4/4 (4 valid)
13:51:03  INFO        SELL LIMIT BG  qty=0.803862803  limit=$119.95  id=c6b97304-b2f7-469f-8507-bdc197b4f1a7
13:51:34  INFO        SELL LIMIT filled BG (confirmed by position check)
13:51:34  INFO        TX logged: SELL BG  P&L 0.04%
13:51:34  INFO        SELL LIMIT AMZN  qty=0.386604955  limit=$250.12  id=e0038396-440e-4c22-958a-0a8f446fa049
13:52:05  INFO        SELL LIMIT filled AMZN (confirmed by position check)
13:52:05  INFO        TX logged: SELL AMZN  P&L 0.07%
13:52:05  INFO        Universe cache hit: 903 tickers (tickers_2026-07-20.json)
13:52:06  INFO        [universe] 40/901 (40 valid)
13:52:07  INFO        [universe] 80/901 (80 valid)
13:52:08  INFO        [universe] 120/901 (120 valid)
13:52:10  INFO        [universe] 160/901 (160 valid)
13:52:11  INFO        [universe] 200/901 (199 valid)
13:52:18  INFO        [universe] 240/901 (238 valid)
13:52:32  INFO        [universe] 280/901 (278 valid)
13:52:42  INFO        [universe] 320/901 (318 valid)
13:52:55  INFO        [universe] 360/901 (358 valid)
13:53:06  INFO        [universe] 400/901 (397 valid)
13:53:19  INFO        [universe] 440/901 (437 valid)
13:53:29  INFO        [universe] 480/901 (477 valid)
13:53:43  INFO        [universe] 520/901 (517 valid)
13:53:56  INFO        [universe] 560/901 (556 valid)
13:54:06  INFO        [universe] 600/901 (596 valid)
13:54:20  INFO        [universe] 640/901 (636 valid)
13:54:30  INFO        [universe] 680/901 (676 valid)
13:54:43  INFO        [universe] 720/901 (715 valid)
13:54:54  INFO        [universe] 760/901 (755 valid)
13:55:07  INFO        [universe] 800/901 (795 valid)
```

### Options bot full output

```text

## Run 20260720T135557Z

- UTC timestamp: `20260720T135557Z`
- GitHub run: [#4405](https://github.com/28twagg-ops/TradingBot/actions/runs/29748320760)
- Run id: `29748320760`
- Live bot: exit=`0`, duration=`0s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T09:44:20.965121-04:00","date":"2026-07-20","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":28.4,"phases_s":{"reconcile":2.1,"cancel":0.16,"manage":1.38,"scan":15.49,"entries":8.17},"signals":24,"placed":0,"equity":129231.43,"open_positions":1,"pending_orders":0,"open_lots":5,"submitted_today":5,"filled_today":5,"unattributed_contracts":0,"top_signals":["S173:ADM","S173:ADSK","S173:AXON","S173:FANG","S173:IT","S173:GDDY","S173:ORCL","S173:CRM"],"github_run":"4402","github_run_id":"29747227265","status":"ok"}
```

### Live bot full output

```text
13:55:58  INFO      Mode: morning_scan
13:55:59  INFO        [positions] 2/2 (2 valid)
13:55:59  INFO        Universe cache hit: 903 tickers (tickers_2026-07-20.json)
13:56:00  INFO        [universe] 40/901 (40 valid)
13:56:01  INFO        [universe] 80/901 (80 valid)
13:56:03  INFO        [universe] 120/901 (120 valid)
13:56:13  INFO        [universe] 160/901 (160 valid)
13:56:23  INFO        [universe] 200/901 (199 valid)
13:56:37  INFO        [universe] 240/901 (238 valid)
13:56:47  INFO        [universe] 280/901 (278 valid)
13:57:01  INFO        [universe] 320/901 (318 valid)
13:57:11  INFO        [universe] 360/901 (358 valid)
13:57:24  INFO        [universe] 400/901 (397 valid)
13:57:35  INFO        [universe] 440/901 (437 valid)
13:57:48  INFO        [universe] 480/901 (477 valid)
13:57:59  INFO        [universe] 520/901 (517 valid)
13:58:12  INFO        [universe] 560/901 (556 valid)
13:58:25  INFO        [universe] 600/901 (596 valid)
13:58:36  INFO        [universe] 640/901 (636 valid)
13:58:49  INFO        [universe] 680/901 (676 valid)
13:58:59  INFO        [universe] 720/901 (715 valid)
13:59:13  INFO        [universe] 760/901 (755 valid)
13:59:23  INFO        [universe] 800/901 (795 valid)
13:59:36  INFO        [universe] 840/901 (834 valid)
13:59:47  INFO        [universe] 880/901 (874 valid)
13:59:54  INFO        [universe] 901/901 (895 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_SCAN|
|  Time                                                         13:55 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.75|
+========================================================================+

+========================================================================+
|                   RUBBER BAND BOT v8  --  DAILY SCAN                   |
+========================================================================+
|  Mode                                                      *** LIVE ***|
|  Date                                                        2026-07-20|
|  Universe                                                          both|
|  Month                                        Jul: 52wkLow + Pullback50|
|  Regime                                                            BULL|
|  Exit                                      midline / stop-0.5% / 3d max|
+========================================================================+

+========================================================================+
|                                ACCOUNT                                 |
+========================================================================+
|  Equity                                                         $482.75|
|  Cash                                                           $289.38|
|  Reserve                                          $24.14  (always kept)|
|  Available                                    $265.24  (for new trades)|
|  Seasonal trade                   $96.55  (20% -- scheduled strategies)|
|  Off-sched trade                      $96.55  (20% -- other strategies)|
+========================================================================+

+========================================================================+
|                           HOLDINGS  (2 open)                           |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CNP      Pullback50      $96.64     $43.36   $43.40   +0.1%   $+0.08  |
|  KO       Pullback50      $96.73     $81.88   $82.03   +0.2%   $+0.17  |
|                                                                        |
|  Total invested                                                 $193.37|
|  Total open P&L                                                  $+0.26|
|  Buys today: 0  |  entry cap: 3  |  max open: 5                        |
+========================================================================+

+========================================================================+
|                               PLAN CACHE                               |
+========================================================================+
|  Mode                                                           morning|
|  File                                      logs/plans/morning_plan.json|
|  Use cached plan                                  no (stale (15850.5m))|
+========================================================================+

+========================================================================+
|          EXIT EVALUATION  (EOD -- midline + stop + max-hold)           |
+========================================================================+
|  CNP  P&L +0.1%  $+0.08                                            HOLD|
|  KO  P&L +0.2%  $+0.17                                             HOLD|
+========================================================================+

+========================================================================+
|                           EXIT EVAL SUMMARY                            |
+========================================================================+
|  Exit eval    attempted 0 | filled 0 | partial 0 | pending 0 | failed 0|
|  Other skips     already logged today 0  |  no price data 0  |  holds 2|
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
|                         SIGNALS FOUND  --  24                          |
+========================================================================+
|  TICKER   STRATEGY        TIER   PRICE    RSI    VOL_Z   TRIGGER       |
+------------------------------------------------------------------------+
|  AMZN     Pullback50      SEAS   $249.67  63.0   -1.11   50MA bounce (-|
|  BG       Pullback50      SEAS   $120.19  71.3   -2.17   50MA bounce (+|
|  BRK-B    Pullback50      SEAS   $490.50  44.2   -2.70   50MA bounce (+|
|  CI       Pullback50      SEAS   $284.90  54.4   -1.86   50MA bounce (-|
|  COP      Pullback50      SEAS   $114.78  73.0   -2.90   50MA bounce (+|
|  EW       Pullback50      SEAS   $86.16   36.2   -1.68   50MA bounce (-|
|  HUBB     Pullback50      SEAS   $493.31  41.1   -2.28   50MA bounce (+|
|  HON      Pullback50      SEAS   $225.58  47.4   -1.35   50MA bounce (+|
|  IRM      Pullback50      SEAS   $125.47  42.0   -3.09   50MA bounce (-|
|  KDP      Pullback50      SEAS   $30.96   34.3   -1.52   50MA bounce (+|
|  LIN      Pullback50      SEAS   $514.21  51.7   -3.00   50MA bounce (-|
|  MAA      Pullback50      SEAS   $133.59  35.4   -3.41   50MA bounce (-|
|  OXY      Pullback50      SEAS   $54.83   71.7   -2.21   50MA bounce (-|
|  TJX      Pullback50      SEAS   $154.87  59.6   -2.07   50MA bounce (-|
|  VRSN     Pullback50      SEAS   $278.46  92.2   -2.13   50MA bounce (-|
|  WEC      Pullback50      SEAS   $113.62  36.4   -2.79   50MA bounce (+|
|  XEL      Pullback50      SEAS   $79.42   40.4   -3.05   50MA bounce (-|
|  WMB      Pullback50      SEAS   $74.93   49.5   -2.34   50MA bounce (+|
|  AVT      Pullback50      SEAS   $86.95   48.4   -2.29   50MA bounce (+|
|  HGV      Pullback50      SEAS   $50.30   37.7   -2.04   50MA bounce (+|
|  IRT      Pullback50      SEAS   $16.68   48.3   -1.68   50MA bounce (+|
|  MUR      Pullback50      SEAS   $36.58   62.3   -1.83   50MA bounce (+|
|  NOV      Pullback50      SEAS   $19.70   68.6   -1.81   50MA bounce (-|
|  RRX      Pullback50      SEAS   $210.26  43.7   -1.96   50MA bounce (-|
|                                                                        |
+========================================================================+

+========================================================================+
|                              ENTRY ORDERS                              |
+========================================================================+
|  Signal scaling: 24 signals / 3 slots → sea=$88 off=$88  (max sea=$97 ~|13:59:55  ERROR       BUY FAILED AMZN: {"code":40010001,"message":"client_order_id must be unique"}
13:59:55  ERROR       BUY FAILED BG: {"code":40010001,"message":"client_order_id must be unique"}
13:59:56  ERROR       BUY FAILED BRK-B: {"code":42210000,"message":"asset \"BRK-B\" not found"}
13:59:56  INFO        BUY  CI  $88.41  [Pullback50]  id=28079009-c1f2-4c27-afa4-19e4ca0058cc
13:59:56  INFO        BUY  COP  $88.41  [Pullback50]  id=62cf3ce5-5b3f-48c5-9815-0bbdd4bc923b
14:00:18  INFO        place_all_stops: checking 4 positions...
14:00:18  INFO        STOP skipped CI: fractional (0.3102 shares) — software exit will handle it
14:00:18  INFO        STOP-MARKET placed CNP  qty=2 (pos=2.2270)  stop=$43.14  id=edcfc2f9-6f88-4de4-99c8-21f76d8a830e
14:00:18  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
14:00:18  INFO        STOP-MARKET placed KO  qty=1 (pos=1.1793)  stop=$81.47  id=a3987083-892e-435c-8426-f063cae11c9e
14:00:18  INFO        Daily log -> logs/daily/2026-07-20.md
14:00:18  INFO        Dashboard written → logs/dashboard.md

|    ENTER [S] AMZN  Pullback50                                    $88.41|
|    ENTER [S] BG  Pullback50                                      $88.41|
|    ENTER [S] BRK-B  Pullback50                                   $88.41|
|    ENTER [S] CI  Pullback50                                      $88.41|
|    BUY SUBMITTED [S~  fill pending — batched confirmation after entries|
|    ENTER [S] COP  Pullback50                                     $88.41|
|    BUY SUBMITTED [S~  fill pending — batched confirmation after entries|
|    SKIP [S] EW  Pullback50                              not enough cash|
|    SKIP [S] HUBB  Pullback50                            not enough cash|
|    SKIP [S] HON  Pullback50                             not enough cash|
|    SKIP [S] IRM  Pullback50                             not enough cash|
|    SKIP [S] KDP  Pullback50                             not enough cash|
|    SKIP [S] LIN  Pullback50                             not enough cash|
|    SKIP [S] MAA  Pullback50                             not enough cash|
|    SKIP [S] OXY  Pullback50                             not enough cash|
|    SKIP [S] TJX  Pullback50                             not enough cash|
|    SKIP [S] VRSN  Pullback50                            not enough cash|
|    SKIP [S] WEC  Pullback50                             not enough cash|
|    SKIP [S] XEL  Pullback50                             not enough cash|
|    SKIP [S] WMB  Pullback50                             not enough cash|
|    SKIP [S] AVT  Pullback50                             not enough cash|
|    SKIP [S] HGV  Pullback50                             not enough cash|
|    SKIP [S] IRT  Pullback50                             not enough cash|
|    SKIP [S] MUR  Pullback50                             not enough cash|
|    SKIP [S] NOV  Pullback50                             not enough cash|
|    SKIP [S] RRX  Pullback50                             not enough cash|

+========================================================================+
|                         BUY FILL CONFIRMATION                          |
+========================================================================+
|  Pending submits                                                      2|
+------------------------------------------------------------------------+
|  CI                                                   still unconfirmed|
|  COP                                                  still unconfirmed|
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
|  Signals                                                             24|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  2 unconfirmed|
|  Exits                                                                0|
|  Open pos                                                             4|
|  Equity                                                         $482.85|
|  Cash                                                           $112.58|
+========================================================================+
```

### Options bot full output

```text

## Run 20260720T140105Z

- UTC timestamp: `20260720T140105Z`
- GitHub run: [#4406](https://github.com/28twagg-ops/TradingBot/actions/runs/29748689380)
- Run id: `29748689380`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`50s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T10:01:08.775493-04:00","date":"2026-07-20","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":48.8,"phases_s":{"reconcile":1.87,"cancel":0.13,"manage":1.86,"scan":34.23,"entries":10.13},"signals":17,"placed":0,"equity":128219.43,"open_positions":1,"pending_orders":0,"open_lots":5,"submitted_today":5,"filled_today":5,"unattributed_contracts":0,"top_signals":["S173:ADM","S173:AXON","S173:FANG","S173:CRM","S173:WDAY","S173:DOCS","S173:POST","S165:HONA"],"github_run":"4406","github_run_id":"29748689380","status":"ok"}
```

### Live bot full output

```text
14:01:06  INFO      Mode: exits
14:01:07  INFO        Daily log -> logs/daily/2026-07-20.md
14:01:07  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (4 ledger rows)
14:01:07  INFO        place_all_stops: checking 4 positions...
14:01:07  INFO        STOP skipped CI: fractional (0.3102 shares) — software exit will handle it
14:01:07  INFO        STOP already live CNP @ $43.14
14:01:07  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
14:01:07  INFO        STOP already live KO @ $81.47
14:01:07  INFO        [positions] 4/4 (4 valid)
14:01:08  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $483.05|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  COP  P&L +0.1%  $+0.05                                            HOLD|
|  CI  P&L +0.1%  $+0.06                                             HOLD|
|  CNP  P&L +0.1%  $+0.10                                            HOLD|
|  KO  P&L +0.4%  $+0.36                                             HOLD|
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
=== options_morning_bot (PAPER) 2026-07-20T10:01:08.775493-04:00 ===

[Run context]
Paper auth OK — equity $128219.43, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 17 signal(s); top: ['S173:ADM', 'S173:AXON', 'S173:FANG', 'S173:CRM', 'S173:WDAY', 'S173:DOCS', 'S173:POST', 'S165:HONA']
Paper lab: $127913 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 50 no tradeable call
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $128,219.43                             |
|  Signals this run              17                                      |
|  Orders submitted (session)    5                                       |
|  Orders filled today (ledger)  5                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             5                                       |
|  Broker option positions       1                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=495  buckets=49  win=34%                             |
|  Returns   avg=+7.4%  med=-33.8%  p10=-77.0%  p90=+93.7%               |
|  Realized  $+3,579.77                                                  |
|  Raw incl dropped  trades=609  real=$+2,081.58                         |
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
|  OPEN OPTIONS (1)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  CRM260724C00185000            5    -22.2%   $    -70.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=48.8s reconcile=1.87s cancel=0.13s manage=1.86s scan=34.23s entries=10.13s
STATUS: options_morning_bot run complete (PAPER) elapsed=48.8s. run=#4406 https://github.com/28twagg-ops/TradingBot/actions/runs/29748689380
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 3.6% (22/609)
  File "/home/runner/work/TradingBot/TradingBot/scripts/options_signal_frequency.py", line 80
    return f"{day}|{sid}|{re.sub(r'\s+', ' ', line.strip())[:160]}"
                                                                   ^
SyntaxError: f-string expression part cannot include a backslash
signal_frequency report failed (non-fatal)
## Ledger health — 2026-07-20
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |    27 | WARN | <<<
| Missing exit records (post) |    27 | WARN | <<<
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |     5 | INFO |
| Total closed lots           |   267 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
```

---

## Run 20260720T140618Z

- UTC timestamp: `20260720T140618Z`
- GitHub run: [#4408](https://github.com/28twagg-ops/TradingBot/actions/runs/29749093642)
- Run id: `29749093642`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`37s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T10:06:21.468124-04:00","date":"2026-07-20","mode":"entry+manage","header":"entry+manage (5 new)","elapsed_s":35.2,"phases_s":{"reconcile":1.86,"cancel":0.09,"manage":0.52,"scan":22.22,"entries":7.79,"reconcile2":1.81},"signals":17,"placed":5,"equity":128473.43,"open_positions":1,"pending_orders":5,"open_lots":5,"submitted_today":10,"filled_today":5,"unattributed_contracts":0,"top_signals":["S173:ADM","S173:AXON","S173:FANG","S173:CRM","S173:WDAY","S173:DOCS","S173:POST","S165:HONA"],"github_run":"4408","github_run_id":"29749093642","status":"ok"}
```

### Live bot full output

```text
14:06:19  INFO      Mode: exits
14:06:20  INFO        Daily log -> logs/daily/2026-07-20.md
14:06:20  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (4 ledger rows)
14:06:20  INFO        place_all_stops: checking 4 positions...
14:06:20  INFO        STOP skipped CI: fractional (0.3102 shares) — software exit will handle it
14:06:20  INFO        STOP already live CNP @ $43.14
14:06:20  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
14:06:20  INFO        STOP already live KO @ $81.47
14:06:20  INFO        [positions] 4/4 (4 valid)
14:06:20  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.47|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CI  P&L -0.3%  $-0.30                                             HOLD|
|  CNP  P&L -0.1%  $-0.06                                            HOLD|
|  COP  P&L +0.1%  $+0.12                                            HOLD|
|  KO  P&L +0.2%  $+0.21                                             HOLD|
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
=== options_morning_bot (PAPER) 2026-07-20T10:06:21.468124-04:00 ===

[Run context]
Paper auth OK — equity $128473.43, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 17 signal(s); top: ['S173:ADM', 'S173:AXON', 'S173:FANG', 'S173:CRM', 'S173:WDAY', 'S173:DOCS', 'S173:POST', 'S165:HONA']
Paper lab: $128567 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 65 no tradeable call, 15 pending order
Placed 5 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $128,473.43                             |
|  Signals this run              17                                      |
|  Orders submitted (session)    10                                      |
|  Orders filled today (ledger)  5                                       |
|  Entries placed this run       5                                       |
|  Open virtual lots             5                                       |
|  Broker option positions       1                                       |
|  Pending orders                5                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=495  buckets=49  win=34%                             |
|  Returns   avg=+7.4%  med=-33.8%  p10=-77.0%  p90=+93.7%               |
|  Realized  $+3,579.77                                                  |
|  Raw incl dropped  trades=609  real=$+2,081.58                         |
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
|  PENDING ORDERS (5)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S173:CRM(5)                             |
+------------------------------------------------------------------------+
|  b1   S173 CRM      limit=0.58                                         |
|  b21  S173 CRM      limit=0.58                                         |
|  b41  S173 CRM      limit=0.58                                         |
|  b61  S173 CRM      limit=0.58                                         |
|  b81  S173 CRM      limit=0.58                                         |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (1)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  CRM260724C00185000            5    -15.9%   $    -50.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=35.2s reconcile=1.86s cancel=0.09s manage=0.52s scan=22.22s entries=7.79s
STATUS: options_morning_bot run complete (PAPER) elapsed=35.2s. run=#4408 https://github.com/28twagg-ops/TradingBot/actions/runs/29749093642
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 3.6% (22/609)
  File "/home/runner/work/TradingBot/TradingBot/scripts/options_signal_frequency.py", line 80
    return f"{day}|{sid}|{re.sub(r'\s+', ' ', line.strip())[:160]}"
                                                                   ^
SyntaxError: f-string expression part cannot include a backslash
signal_frequency report failed (non-fatal)
## Ledger health — 2026-07-20
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |    27 | WARN | <<<
| Missing exit records (post) |    27 | WARN | <<<
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |     5 | INFO |
| Total closed lots           |   267 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
```

---

## Run 20260720T141036Z

- UTC timestamp: `20260720T141036Z`
- GitHub run: [#4409](https://github.com/28twagg-ops/TradingBot/actions/runs/29749433701)
- Run id: `29749433701`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`32s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T10:10:39.212848-04:00","date":"2026-07-20","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":30.7,"phases_s":{"reconcile":1.63,"cancel":0.01,"manage":0.21,"scan":24.97,"entries":3.39},"signals":17,"placed":0,"equity":128583.33,"open_positions":1,"pending_orders":0,"open_lots":10,"submitted_today":10,"filled_today":10,"unattributed_contracts":0,"top_signals":["S173:ADM","S173:AXON","S173:FANG","S173:CRM","S173:WDAY","S173:DOCS","S173:POST","S165:HONA"],"github_run":"4409","github_run_id":"29749433701","status":"ok"}
```

### Live bot full output

```text
14:10:37  INFO      Mode: exits
14:10:38  INFO        Daily log -> logs/daily/2026-07-20.md
14:10:38  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (4 ledger rows)
14:10:38  INFO        place_all_stops: checking 4 positions...
14:10:38  INFO        STOP skipped CI: fractional (0.3102 shares) — software exit will handle it
14:10:38  INFO        STOP already live CNP @ $43.14
14:10:38  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
14:10:38  INFO        STOP already live KO @ $81.47
14:10:38  INFO        [positions] 4/4 (4 valid)
14:10:38  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.41|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CI  P&L -0.2%  $-0.20                                             HOLD|
|  CNP  P&L -0.1%  $-0.08                                            HOLD|
|  COP  P&L -0.0%  $-0.03                                            HOLD|
|  KO  P&L +0.2%  $+0.23                                             HOLD|
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
=== options_morning_bot (PAPER) 2026-07-20T10:10:39.212848-04:00 ===

[Run context]
Paper auth OK — equity $128583.33, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 17 signal(s); top: ['S173:ADM', 'S173:AXON', 'S173:FANG', 'S173:CRM', 'S173:WDAY', 'S173:DOCS', 'S173:POST', 'S165:HONA']
Paper lab: $128573 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 50 no tradeable call
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $128,583.33                             |
|  Signals this run              17                                      |
|  Orders submitted (session)    10                                      |
|  Orders filled today (ledger)  10                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             10                                      |
|  Broker option positions       1                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=497  buckets=49  win=34%                             |
|  Returns   avg=+7.4%  med=-33.8%  p10=-77.0%  p90=+93.5%               |
|  Realized  $+3,607.77                                                  |
|  Raw incl dropped  trades=611  real=$+2,109.58                         |
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
|  OPEN OPTIONS (1)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  CRM260724C00185000           10    -13.3%   $    -80.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=30.7s reconcile=1.63s cancel=0.01s manage=0.21s scan=24.97s entries=3.39s
STATUS: options_morning_bot run complete (PAPER) elapsed=30.7s. run=#4409 https://github.com/28twagg-ops/TradingBot/actions/runs/29749433701
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 3.6% (22/611)
  File "/home/runner/work/TradingBot/TradingBot/scripts/options_signal_frequency.py", line 80
    return f"{day}|{sid}|{re.sub(r'\s+', ' ', line.strip())[:160]}"
                                                                   ^
SyntaxError: f-string expression part cannot include a backslash
signal_frequency report failed (non-fatal)
## Ledger health — 2026-07-20
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |    27 | WARN | <<<
| Missing exit records (post) |    27 | WARN | <<<
| State/ledger mismatches     |     5 | WARN | <<<
| Total open lots             |    10 | INFO |
| Total closed lots           |   269 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
```

---
