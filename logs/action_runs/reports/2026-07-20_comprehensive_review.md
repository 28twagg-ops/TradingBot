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
