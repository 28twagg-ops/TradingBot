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

## Run 20260720T141540Z

- UTC timestamp: `20260720T141540Z`
- GitHub run: [#4410](https://github.com/28twagg-ops/TradingBot/actions/runs/29749803204)
- Run id: `29749803204`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`39s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T10:15:43.952130-04:00","date":"2026-07-20","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":37.5,"phases_s":{"reconcile":1.89,"cancel":0.12,"manage":0.88,"scan":26.37,"entries":7.76},"signals":19,"placed":0,"equity":128883.33,"open_positions":1,"pending_orders":0,"open_lots":10,"submitted_today":10,"filled_today":10,"unattributed_contracts":0,"top_signals":["S173:ADM","S173:AXON","S173:FANG","S173:GDDY","S173:CRM","S173:WDAY","S173:DOCS","S173:PATH"],"github_run":"4410","github_run_id":"29749803204","status":"ok"}
```

### Live bot full output

```text
14:15:41  INFO      Mode: exits
14:15:42  INFO        Daily log -> logs/daily/2026-07-20.md
14:15:42  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (4 ledger rows)
14:15:42  INFO        place_all_stops: checking 4 positions...
14:15:42  INFO        STOP skipped CI: fractional (0.3102 shares) — software exit will handle it
14:15:42  INFO        STOP already live CNP @ $43.14
14:15:42  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
14:15:42  INFO        STOP already live KO @ $81.47
14:15:42  INFO        [positions] 4/4 (4 valid)
14:15:43  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:15 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.81|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CI  P&L -0.1%  $-0.10                                             HOLD|
|  CNP  P&L +0.0%  $+0.01                                            HOLD|
|  COP  P&L +0.2%  $+0.14                                            HOLD|
|  KO  P&L +0.3%  $+0.25                                             HOLD|
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
=== options_morning_bot (PAPER) 2026-07-20T10:15:43.952130-04:00 ===

[Run context]
Paper auth OK — equity $128883.33, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 19 signal(s); top: ['S173:ADM', 'S173:AXON', 'S173:FANG', 'S173:GDDY', 'S173:CRM', 'S173:WDAY', 'S173:DOCS', 'S173:PATH']
Paper lab: $128931 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 50 no tradeable call
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $128,883.33                             |
|  Signals this run              19                                      |
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
|  CRM260724C00185000           10    -10.0%   $    -60.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=37.5s reconcile=1.89s cancel=0.12s manage=0.88s scan=26.37s entries=7.76s
STATUS: options_morning_bot run complete (PAPER) elapsed=37.5s. run=#4410 https://github.com/28twagg-ops/TradingBot/actions/runs/29749803204
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

## Run 20260720T142036Z

- UTC timestamp: `20260720T142036Z`
- GitHub run: [#4411](https://github.com/28twagg-ops/TradingBot/actions/runs/29750173114)
- Run id: `29750173114`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`37s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T10:20:40.174430-04:00","date":"2026-07-20","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":35.8,"phases_s":{"reconcile":1.94,"cancel":0.13,"manage":0.68,"scan":23.81,"entries":8.57},"signals":18,"placed":0,"equity":128645.33,"open_positions":1,"pending_orders":0,"open_lots":10,"submitted_today":10,"filled_today":10,"unattributed_contracts":0,"top_signals":["S173:ADM","S173:AXON","S173:FANG","S173:GDDY","S173:CRM","S173:WDAY","S173:DOCS","S173:POST"],"github_run":"4411","github_run_id":"29750173114","status":"ok"}
```

### Live bot full output

```text
14:20:37  INFO      Mode: exits
14:20:38  INFO        Daily log -> logs/daily/2026-07-20.md
14:20:38  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (4 ledger rows)
14:20:38  INFO        place_all_stops: checking 4 positions...
14:20:38  INFO        STOP skipped CI: fractional (0.3102 shares) — software exit will handle it
14:20:38  INFO        STOP already live CNP @ $43.14
14:20:38  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
14:20:38  INFO        STOP already live KO @ $81.47
14:20:39  INFO        [positions] 4/4 (4 valid)
14:20:39  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $483.63|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CNP  P&L +0.1%  $+0.10                                            HOLD|
|  CI  P&L +0.1%  $+0.12                                             HOLD|
|  COP  P&L +0.5%  $+0.44                                            HOLD|
|  KO  P&L +0.5%  $+0.49                                             HOLD|
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
=== options_morning_bot (PAPER) 2026-07-20T10:20:40.174430-04:00 ===

[Run context]
Paper auth OK — equity $128645.33, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 18 signal(s); top: ['S173:ADM', 'S173:AXON', 'S173:FANG', 'S173:GDDY', 'S173:CRM', 'S173:WDAY', 'S173:DOCS', 'S173:POST']
Paper lab: $128547 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 50 no tradeable call
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $128,645.33                             |
|  Signals this run              18                                      |
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
|  CRM260724C00185000           10     -8.3%   $    -50.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=35.8s reconcile=1.94s cancel=0.13s manage=0.68s scan=23.81s entries=8.57s
STATUS: options_morning_bot run complete (PAPER) elapsed=35.8s. run=#4411 https://github.com/28twagg-ops/TradingBot/actions/runs/29750173114
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

## Run 20260720T142546Z

- UTC timestamp: `20260720T142546Z`
- GitHub run: [#4412](https://github.com/28twagg-ops/TradingBot/actions/runs/29750538672)
- Run id: `29750538672`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`32s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T10:25:49.285046-04:00","date":"2026-07-20","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":30.9,"phases_s":{"reconcile":1.75,"cancel":0.13,"manage":0.68,"scan":19.56,"entries":8.21},"signals":19,"placed":0,"equity":129357.33,"open_positions":1,"pending_orders":0,"open_lots":10,"submitted_today":10,"filled_today":10,"unattributed_contracts":0,"top_signals":["S173:ADM","S173:AXON","S173:CRL","S173:FANG","S173:GDDY","S173:CRM","S173:WDAY","S173:DOCS"],"github_run":"4412","github_run_id":"29750538672","status":"ok"}
```

### Live bot full output

```text
14:25:46  INFO      Mode: exits
14:25:47  INFO        Daily log -> logs/daily/2026-07-20.md
14:25:47  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (4 ledger rows)
14:25:47  INFO        place_all_stops: checking 4 positions...
14:25:47  INFO        STOP skipped CI: fractional (0.3102 shares) — software exit will handle it
14:25:47  INFO        STOP already live CNP @ $43.14
14:25:47  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
14:25:47  INFO        STOP already live KO @ $81.47
14:25:48  INFO        [positions] 4/4 (4 valid)
14:25:48  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:25 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.99|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CI  P&L -0.1%  $-0.10                                             HOLD|
|  CNP  P&L +0.0%  $+0.01                                            HOLD|
|  KO  P&L +0.2%  $+0.21                                             HOLD|
|  COP  P&L +0.4%  $+0.38                                            HOLD|
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
=== options_morning_bot (PAPER) 2026-07-20T10:25:49.285046-04:00 ===

[Run context]
Paper auth OK — equity $129357.33, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 19 signal(s); top: ['S173:ADM', 'S173:AXON', 'S173:CRL', 'S173:FANG', 'S173:GDDY', 'S173:CRM', 'S173:WDAY', 'S173:DOCS']
Paper lab: $129385 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 50 no tradeable call
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $129,357.33                             |
|  Signals this run              19                                      |
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
|  CRM260724C00185000           10    -15.0%   $    -90.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=30.9s reconcile=1.75s cancel=0.13s manage=0.68s scan=19.56s entries=8.21s
STATUS: options_morning_bot run complete (PAPER) elapsed=30.9s. run=#4412 https://github.com/28twagg-ops/TradingBot/actions/runs/29750538672
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

## Run 20260720T143037Z

- UTC timestamp: `20260720T143037Z`
- GitHub run: [#4413](https://github.com/28twagg-ops/TradingBot/actions/runs/29750902799)
- Run id: `29750902799`
- Live bot: exit=`0`, duration=`4s`
- Options bot: exit=`0`, duration=`57s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T10:30:42.391943-04:00","date":"2026-07-20","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":55.5,"phases_s":{"reconcile":1.95,"cancel":0.15,"manage":1.1,"scan":41.96,"entries":9.66},"signals":18,"placed":0,"equity":129785.33,"open_positions":1,"pending_orders":0,"open_lots":10,"submitted_today":10,"filled_today":10,"unattributed_contracts":0,"top_signals":["S173:ADM","S173:AXON","S173:FANG","S173:GDDY","S173:CRM","S173:WDAY","S173:DOCS","S173:POST"],"github_run":"4413","github_run_id":"29750902799","status":"ok"}
```

### Live bot full output

```text
14:30:39  INFO      Mode: exits
14:30:40  INFO        Daily log -> logs/daily/2026-07-20.md
14:30:40  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (4 ledger rows)
14:30:40  INFO        place_all_stops: checking 4 positions...
14:30:40  INFO        STOP skipped CI: fractional (0.3102 shares) — software exit will handle it
14:30:40  INFO        STOP already live CNP @ $43.14
14:30:40  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
14:30:40  INFO        STOP already live KO @ $81.47
14:30:41  INFO        [positions] 4/4 (4 valid)
14:30:41  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:30 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $483.36|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CI  P&L +0.1%  $+0.06                                             HOLD|
|  CNP  P&L +0.2%  $+0.15                                            HOLD|
|  KO  P&L +0.2%  $+0.16                                             HOLD|
|  COP  P&L +0.6%  $+0.49                                            HOLD|
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
=== options_morning_bot (PAPER) 2026-07-20T10:30:42.391943-04:00 ===

[Run context]
Paper auth OK — equity $129801.33, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 18 signal(s); top: ['S173:ADM', 'S173:AXON', 'S173:FANG', 'S173:GDDY', 'S173:CRM', 'S173:WDAY', 'S173:DOCS', 'S173:POST']
Paper lab: $129545 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 50 no tradeable call
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $129,785.33                             |
|  Signals this run              18                                      |
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
|  CRM260724C00185000           10     -8.3%   $    -50.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=55.5s reconcile=1.95s cancel=0.15s manage=1.1s scan=41.96s entries=9.66s
STATUS: options_morning_bot run complete (PAPER) elapsed=55.5s. run=#4413 https://github.com/28twagg-ops/TradingBot/actions/runs/29750902799
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

## Run 20260720T143534Z

- UTC timestamp: `20260720T143534Z`
- GitHub run: [#4414](https://github.com/28twagg-ops/TradingBot/actions/runs/29751279981)
- Run id: `29751279981`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`32s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T10:35:36.873476-04:00","date":"2026-07-20","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":31.0,"phases_s":{"reconcile":1.64,"cancel":0.17,"manage":0.22,"scan":24.5,"entries":4.16},"signals":19,"placed":0,"equity":129317.33,"open_positions":1,"pending_orders":0,"open_lots":10,"submitted_today":10,"filled_today":10,"unattributed_contracts":0,"top_signals":["S173:ADM","S173:AXON","S173:FANG","S173:GDDY","S173:CRM","S173:WDAY","S173:DOCS","S173:PATH"],"github_run":"4414","github_run_id":"29751279981","status":"ok"}
```

### Live bot full output

```text
14:35:35  INFO      Mode: exits
14:35:35  INFO        Daily log -> logs/daily/2026-07-20.md
14:35:35  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (4 ledger rows)
14:35:35  INFO        place_all_stops: checking 4 positions...
14:35:35  INFO        STOP skipped CI: fractional (0.3102 shares) — software exit will handle it
14:35:35  INFO        STOP already live CNP @ $43.14
14:35:35  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
14:35:35  INFO        STOP already live KO @ $81.47
14:35:35  INFO        [positions] 4/4 (4 valid)
14:35:35  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:35 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.98|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CI  P&L -0.4%  $-0.37                                             HOLD|
|  CNP  P&L +0.1%  $+0.07                                            HOLD|
|  KO  P&L +0.1%  $+0.11                                             HOLD|
|  COP  P&L +0.8%  $+0.68                                            HOLD|
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
=== options_morning_bot (PAPER) 2026-07-20T10:35:36.873476-04:00 ===

[Run context]
Paper auth OK — equity $129317.33, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 19 signal(s); top: ['S173:ADM', 'S173:AXON', 'S173:FANG', 'S173:GDDY', 'S173:CRM', 'S173:WDAY', 'S173:DOCS', 'S173:PATH']
Paper lab: $129369 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 50 no tradeable call
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $129,317.33                             |
|  Signals this run              19                                      |
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
|  CRM260724C00185000           10     -3.3%   $    -20.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=31.0s reconcile=1.64s cancel=0.17s manage=0.22s scan=24.5s entries=4.16s
STATUS: options_morning_bot run complete (PAPER) elapsed=31.0s. run=#4414 https://github.com/28twagg-ops/TradingBot/actions/runs/29751279981
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

## Run 20260720T144034Z

- UTC timestamp: `20260720T144034Z`
- GitHub run: [#4415](https://github.com/28twagg-ops/TradingBot/actions/runs/29751652264)
- Run id: `29751652264`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`34s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T10:40:38.070302-04:00","date":"2026-07-20","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":32.8,"phases_s":{"reconcile":1.67,"cancel":0.03,"manage":0.28,"scan":27.05,"entries":3.33},"signals":19,"placed":0,"equity":129325.33,"open_positions":1,"pending_orders":0,"open_lots":10,"submitted_today":10,"filled_today":10,"unattributed_contracts":0,"top_signals":["S173:ADM","S173:AXON","S173:FANG","S173:GDDY","S173:CRM","S173:WDAY","S173:DOCS","S173:PATH"],"github_run":"4415","github_run_id":"29751652264","status":"ok"}
```

### Live bot full output

```text
14:40:35  INFO      Mode: exits
14:40:36  INFO        Daily log -> logs/daily/2026-07-20.md
14:40:36  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (4 ledger rows)
14:40:36  INFO        place_all_stops: checking 4 positions...
14:40:36  INFO        STOP skipped CI: fractional (0.3102 shares) — software exit will handle it
14:40:36  INFO        STOP already live CNP @ $43.14
14:40:36  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
14:40:36  INFO        STOP already live KO @ $81.47
14:40:37  INFO        [positions] 4/4 (4 valid)
14:40:37  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:40 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $483.09|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CI  P&L -0.4%  $-0.32                                             HOLD|
|  CNP  P&L +0.0%  $+0.03                                            HOLD|
|  KO  P&L +0.2%  $+0.16                                             HOLD|
|  COP  P&L +0.8%  $+0.73                                            HOLD|
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
=== options_morning_bot (PAPER) 2026-07-20T10:40:38.070302-04:00 ===

[Run context]
Paper auth OK — equity $129325.33, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 19 signal(s); top: ['S173:ADM', 'S173:AXON', 'S173:FANG', 'S173:GDDY', 'S173:CRM', 'S173:WDAY', 'S173:DOCS', 'S173:PATH']
Paper lab: $129351 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 50 no tradeable call
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $129,325.33                             |
|  Signals this run              19                                      |
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
|  CRM260724C00185000           10     +6.7%   $    +40.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=32.8s reconcile=1.67s cancel=0.03s manage=0.28s scan=27.05s entries=3.33s
STATUS: options_morning_bot run complete (PAPER) elapsed=32.8s. run=#4415 https://github.com/28twagg-ops/TradingBot/actions/runs/29751652264
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

## Run 20260720T144536Z

- UTC timestamp: `20260720T144536Z`
- GitHub run: [#4416](https://github.com/28twagg-ops/TradingBot/actions/runs/29752027182)
- Run id: `29752027182`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`51s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T10:45:38.718962-04:00","date":"2026-07-20","mode":"entry+manage","header":"entry+manage (5 new)","elapsed_s":48.8,"phases_s":{"reconcile":2.38,"cancel":0.05,"manage":0.33,"scan":33.74,"entries":10.12,"reconcile2":1.79},"signals":19,"placed":5,"equity":128917.33,"open_positions":1,"pending_orders":5,"open_lots":10,"submitted_today":15,"filled_today":10,"unattributed_contracts":0,"top_signals":["S173:ADM","S173:AXON","S173:FANG","S173:GDDY","S173:CRM","S173:WDAY","S173:DOCS","S173:PATH"],"github_run":"4416","github_run_id":"29752027182","status":"ok"}
```

### Live bot full output

```text
14:45:37  INFO      Mode: exits
14:45:37  INFO        Daily log -> logs/daily/2026-07-20.md
14:45:37  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (4 ledger rows)
14:45:37  INFO        place_all_stops: checking 4 positions...
14:45:37  INFO        STOP skipped CI: fractional (0.3102 shares) — software exit will handle it
14:45:37  INFO        STOP already live CNP @ $43.14
14:45:37  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
14:45:37  INFO        STOP already live KO @ $81.47
14:45:37  INFO        [positions] 4/4 (4 valid)
14:45:37  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:45 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $483.54|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CI  P&L -0.3%  $-0.27                                             HOLD|
|  KO  P&L +0.3%  $+0.24                                             HOLD|
|  CNP  P&L +0.3%  $+0.25                                            HOLD|
|  COP  P&L +0.9%  $+0.82                                            HOLD|
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
=== options_morning_bot (PAPER) 2026-07-20T10:45:38.718962-04:00 ===

[Run context]
Paper auth OK — equity $128917.33, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 19 signal(s); top: ['S173:ADM', 'S173:AXON', 'S173:FANG', 'S173:GDDY', 'S173:CRM', 'S173:WDAY', 'S173:DOCS', 'S173:PATH']
Paper lab: $129391 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 120 no tradeable call, 20 pending order
Placed 5 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $128,917.33                             |
|  Signals this run              19                                      |
|  Orders submitted (session)    15                                      |
|  Orders filled today (ledger)  10                                      |
|  Entries placed this run       5                                       |
|  Open virtual lots             10                                      |
|  Broker option positions       1                                       |
|  Pending orders                5                                       |
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
|  PENDING ORDERS (5)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S173:CRM(5)                             |
+------------------------------------------------------------------------+
|  b2   S173 CRM      limit=0.70                                         |
|  b22  S173 CRM      limit=0.70                                         |
|  b42  S173 CRM      limit=0.70                                         |
|  b62  S173 CRM      limit=0.70                                         |
|  b82  S173 CRM      limit=0.70                                         |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (1)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  CRM260724C00185000           10     +6.7%   $    +40.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=48.8s reconcile=2.38s cancel=0.05s manage=0.33s scan=33.74s entries=10.12s
STATUS: options_morning_bot run complete (PAPER) elapsed=48.8s. run=#4416 https://github.com/28twagg-ops/TradingBot/actions/runs/29752027182
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

## Run 20260720T145043Z

- UTC timestamp: `20260720T145043Z`
- GitHub run: [#4417](https://github.com/28twagg-ops/TradingBot/actions/runs/29752408089)
- Run id: `29752408089`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`41s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T10:50:47.349747-04:00","date":"2026-07-20","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":39.3,"phases_s":{"reconcile":1.96,"cancel":0.15,"manage":0.75,"scan":24.6,"entries":9.31,"reconcile2":1.94},"signals":19,"placed":0,"equity":129217.33,"open_positions":1,"pending_orders":5,"open_lots":10,"submitted_today":15,"filled_today":10,"unattributed_contracts":0,"top_signals":["S173:ADM","S173:AXON","S173:FANG","S173:GDDY","S173:CRM","S173:WDAY","S173:DOCS","S173:PATH"],"github_run":"4417","github_run_id":"29752408089","status":"ok"}
```

### Live bot full output

```text
14:50:44  INFO      Mode: exits
14:50:45  INFO        Daily log -> logs/daily/2026-07-20.md
14:50:45  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (4 ledger rows)
14:50:45  INFO        place_all_stops: checking 4 positions...
14:50:45  INFO        STOP skipped CI: fractional (0.3102 shares) — software exit will handle it
14:50:45  INFO        STOP already live CNP @ $43.14
14:50:45  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
14:50:45  INFO        STOP already live KO @ $81.47
14:50:46  INFO        [positions] 4/4 (4 valid)
14:50:46  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:50 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $483.43|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CI  P&L -0.2%  $-0.21                                             HOLD|
|  CNP  P&L +0.1%  $+0.06                                            HOLD|
|  KO  P&L +0.3%  $+0.27                                             HOLD|
|  COP  P&L +0.9%  $+0.81                                            HOLD|
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
=== options_morning_bot (PAPER) 2026-07-20T10:50:47.349747-04:00 ===

[Run context]
Paper auth OK — equity $129217.33, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 19 signal(s); top: ['S173:ADM', 'S173:AXON', 'S173:FANG', 'S173:GDDY', 'S173:CRM', 'S173:WDAY', 'S173:DOCS', 'S173:PATH']
Paper lab: $129293 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 50 no tradeable call, 45 pending order
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $129,217.33                             |
|  Signals this run              19                                      |
|  Orders submitted (session)    15                                      |
|  Orders filled today (ledger)  10                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             10                                      |
|  Broker option positions       1                                       |
|  Pending orders                5                                       |
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
|  PENDING ORDERS (5)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S173:CRM(5)                             |
+------------------------------------------------------------------------+
|  b2   S173 CRM      limit=0.70                                         |
|  b22  S173 CRM      limit=0.70                                         |
|  b42  S173 CRM      limit=0.70                                         |
|  b62  S173 CRM      limit=0.70                                         |
|  b82  S173 CRM      limit=0.70                                         |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (1)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  CRM260724C00185000           10     +8.3%   $    +50.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=39.3s reconcile=1.96s cancel=0.15s manage=0.75s scan=24.6s entries=9.31s
STATUS: options_morning_bot run complete (PAPER) elapsed=39.3s. run=#4417 https://github.com/28twagg-ops/TradingBot/actions/runs/29752408089
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

## Run 20260720T145534Z

- UTC timestamp: `20260720T145534Z`
- GitHub run: [#4418](https://github.com/28twagg-ops/TradingBot/actions/runs/29752789250)
- Run id: `29752789250`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`42s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T10:55:37.423501-04:00","date":"2026-07-20","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":40.7,"phases_s":{"reconcile":1.75,"cancel":0.09,"manage":0.61,"scan":29.77,"entries":6.35,"reconcile2":1.71},"signals":20,"placed":0,"equity":129159.33,"open_positions":1,"pending_orders":5,"open_lots":10,"submitted_today":15,"filled_today":10,"unattributed_contracts":0,"top_signals":["S173:ADM","S173:AXON","S173:FANG","S173:GDDY","S173:CRM","S173:NOW","S173:WDAY","S173:DOCS"],"github_run":"4418","github_run_id":"29752789250","status":"ok"}
```

### Live bot full output

```text
14:55:35  INFO      Mode: exits
14:55:35  INFO        Daily log -> logs/daily/2026-07-20.md
14:55:35  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (4 ledger rows)
14:55:36  INFO        place_all_stops: checking 4 positions...
14:55:36  INFO        STOP skipped CI: fractional (0.3102 shares) — software exit will handle it
14:55:36  INFO        STOP already live CNP @ $43.14
14:55:36  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
14:55:36  INFO        STOP already live KO @ $81.47
14:55:36  INFO        [positions] 4/4 (4 valid)
14:55:36  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:55 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $483.85|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CI  P&L -0.1%  $-0.05                                             HOLD|
|  CNP  P&L +0.0%  $+0.02                                            HOLD|
|  KO  P&L +0.3%  $+0.31                                             HOLD|
|  COP  P&L +1.2%  $+1.07                                            HOLD|
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
=== options_morning_bot (PAPER) 2026-07-20T10:55:37.423501-04:00 ===

[Run context]
Paper auth OK — equity $129159.33, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 20 signal(s); top: ['S173:ADM', 'S173:AXON', 'S173:FANG', 'S173:GDDY', 'S173:CRM', 'S173:NOW', 'S173:WDAY', 'S173:DOCS']
Paper lab: $129335 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 50 no tradeable call, 50 pending order
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $129,159.33                             |
|  Signals this run              20                                      |
|  Orders submitted (session)    15                                      |
|  Orders filled today (ledger)  10                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             10                                      |
|  Broker option positions       1                                       |
|  Pending orders                5                                       |
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
|  PENDING ORDERS (5)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S173:CRM(5)                             |
+------------------------------------------------------------------------+
|  b2   S173 CRM      limit=0.70                                         |
|  b22  S173 CRM      limit=0.70                                         |
|  b42  S173 CRM      limit=0.70                                         |
|  b62  S173 CRM      limit=0.70                                         |
|  b82  S173 CRM      limit=0.70                                         |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (1)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  CRM260724C00185000           10    +13.3%   $    +80.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=40.7s reconcile=1.75s cancel=0.09s manage=0.61s scan=29.77s entries=6.35s
STATUS: options_morning_bot run complete (PAPER) elapsed=40.7s. run=#4418 https://github.com/28twagg-ops/TradingBot/actions/runs/29752789250
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

## Run 20260720T150046Z

- UTC timestamp: `20260720T150046Z`
- GitHub run: [#4419](https://github.com/28twagg-ops/TradingBot/actions/runs/29753170435)
- Run id: `29753170435`
- Live bot: exit=`0`, duration=`4s`
- Options bot: exit=`0`, duration=`64s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T11:00:52.224393-04:00","date":"2026-07-20","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":63.0,"phases_s":{"reconcile":2.02,"cancel":0.16,"manage":1.19,"scan":48.02,"entries":10.68},"signals":20,"placed":0,"equity":129018.23,"open_positions":1,"pending_orders":0,"open_lots":15,"submitted_today":15,"filled_today":15,"unattributed_contracts":0,"top_signals":["S173:ADM","S173:AXON","S173:FANG","S173:GDDY","S173:CRM","S173:NOW","S173:WDAY","S173:DOCS"],"github_run":"4419","github_run_id":"29753170435","status":"ok"}
```

### Live bot full output

```text
15:00:48  INFO      Mode: exits
15:00:50  INFO        Daily log -> logs/daily/2026-07-20.md
15:00:50  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (4 ledger rows)
15:00:50  INFO        place_all_stops: checking 4 positions...
15:00:50  INFO        STOP skipped CI: fractional (0.3102 shares) — software exit will handle it
15:00:50  INFO        STOP already live CNP @ $43.14
15:00:50  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
15:00:50  INFO        STOP already live KO @ $81.47
15:00:51  INFO        [positions] 4/4 (4 valid)
15:00:51  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:00 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $483.61|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CI  P&L -0.1%  $-0.13                                             HOLD|
|  CNP  P&L +0.1%  $+0.08                                            HOLD|
|  KO  P&L +0.3%  $+0.29                                             HOLD|
|  COP  P&L +1.0%  $+0.88                                            HOLD|
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
=== options_morning_bot (PAPER) 2026-07-20T11:00:52.224393-04:00 ===

[Run context]
Paper auth OK — equity $129016.23, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 20 signal(s); top: ['S173:ADM', 'S173:AXON', 'S173:FANG', 'S173:GDDY', 'S173:CRM', 'S173:NOW', 'S173:WDAY', 'S173:DOCS']
Paper lab: $129162 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 50 no tradeable call
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $129,018.23                             |
|  Signals this run              20                                      |
|  Orders submitted (session)    15                                      |
|  Orders filled today (ledger)  15                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             15                                      |
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
|  CRM260724C00185000           15     +4.2%   $    +40.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=63.0s reconcile=2.02s cancel=0.16s manage=1.19s scan=48.02s entries=10.68s
STATUS: options_morning_bot run complete (PAPER) elapsed=63.0s. run=#4419 https://github.com/28twagg-ops/TradingBot/actions/runs/29753170435
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
| Total open lots             |    15 | INFO |
| Total closed lots           |   269 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
```

---

## Run 20260720T150534Z

- UTC timestamp: `20260720T150534Z`
- GitHub run: [#4420](https://github.com/28twagg-ops/TradingBot/actions/runs/29753552520)
- Run id: `29753552520`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`32s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T11:05:37.587723-04:00","date":"2026-07-20","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":30.4,"phases_s":{"reconcile":1.61,"cancel":0.02,"manage":0.21,"scan":24.72,"entries":3.58},"signals":21,"placed":0,"equity":129019.23,"open_positions":1,"pending_orders":0,"open_lots":15,"submitted_today":15,"filled_today":15,"unattributed_contracts":0,"top_signals":["S173:ADM","S173:AXON","S173:FANG","S173:GDDY","S173:INTU","S173:CRM","S173:NOW","S173:WDAY"],"github_run":"4420","github_run_id":"29753552520","status":"ok"}
```

### Live bot full output

```text
15:05:36  INFO      Mode: exits
15:05:36  INFO        Daily log -> logs/daily/2026-07-20.md
15:05:36  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (4 ledger rows)
15:05:36  INFO        place_all_stops: checking 4 positions...
15:05:36  INFO        STOP skipped CI: fractional (0.3102 shares) — software exit will handle it
15:05:36  INFO        STOP already live CNP @ $43.14
15:05:36  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
15:05:36  INFO        STOP already live KO @ $81.47
15:05:36  INFO        [positions] 4/4 (4 valid)
15:05:36  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:05 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.97|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CNP  P&L -0.2%  $-0.23                                            HOLD|
|  CI  P&L -0.2%  $-0.14                                             HOLD|
|  KO  P&L +0.1%  $+0.08                                             HOLD|
|  COP  P&L +0.9%  $+0.75                                            HOLD|
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
=== options_morning_bot (PAPER) 2026-07-20T11:05:37.587723-04:00 ===

[Run context]
Paper auth OK — equity $129019.23, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 21 signal(s); top: ['S173:ADM', 'S173:AXON', 'S173:FANG', 'S173:GDDY', 'S173:INTU', 'S173:CRM', 'S173:NOW', 'S173:WDAY']
Paper lab: $129039 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 50 no tradeable call
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $129,019.23                             |
|  Signals this run              21                                      |
|  Orders submitted (session)    15                                      |
|  Orders filled today (ledger)  15                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             15                                      |
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
|  CRM260724C00185000           15    +10.5%   $   +100.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=30.4s reconcile=1.61s cancel=0.02s manage=0.21s scan=24.72s entries=3.58s
STATUS: options_morning_bot run complete (PAPER) elapsed=30.4s. run=#4420 https://github.com/28twagg-ops/TradingBot/actions/runs/29753552520
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
| Total open lots             |    15 | INFO |
| Total closed lots           |   269 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
```

---

## Run 20260720T151330Z

- UTC timestamp: `20260720T151330Z`
- GitHub run: [#4421](https://github.com/28twagg-ops/TradingBot/actions/runs/29753933863)
- Run id: `29753933863`
- Live bot: exit=`0`, duration=`5s`
- Options bot: exit=`0`, duration=`27s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T11:13:35.875302-04:00","date":"2026-07-20","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":26.5,"phases_s":{"reconcile":4.2,"cancel":0.15,"manage":0.77,"scan":12.71,"entries":8.17},"signals":22,"placed":0,"equity":129402.23,"open_positions":1,"pending_orders":0,"open_lots":15,"submitted_today":15,"filled_today":15,"unattributed_contracts":0,"top_signals":["S173:ADM","S173:AXON","S173:FANG","S173:GDDY","S173:INTU","S173:CRM","S173:NOW","S173:WDAY"],"github_run":"4421","github_run_id":"29753933863","status":"ok"}
```

### Live bot full output

```text
15:13:33  INFO      Mode: exits
15:13:34  INFO        Daily log -> logs/daily/2026-07-20.md
15:13:34  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (4 ledger rows)
15:13:34  INFO        place_all_stops: checking 4 positions...
15:13:34  INFO        STOP skipped CI: fractional (0.3102 shares) — software exit will handle it
15:13:34  INFO        STOP already live CNP @ $43.14
15:13:34  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
15:13:34  INFO        STOP already live KO @ $81.47
15:13:35  INFO        [positions] 4/4 (4 valid)
15:13:35  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:13 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.45|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CNP  P&L -0.4%  $-0.36                                            HOLD|
|  CI  P&L -0.1%  $-0.12                                             HOLD|
|  KO  P&L -0.0%  $-0.03                                             HOLD|
|  COP  P&L +0.5%  $+0.48                                            HOLD|
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
=== options_morning_bot (PAPER) 2026-07-20T11:13:35.875302-04:00 ===

[Run context]
Paper auth OK — equity $129402.23, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 22 signal(s); top: ['S173:ADM', 'S173:AXON', 'S173:FANG', 'S173:GDDY', 'S173:INTU', 'S173:CRM', 'S173:NOW', 'S173:WDAY']
Paper lab: $129393 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 50 no tradeable call
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $129,402.23                             |
|  Signals this run              22                                      |
|  Orders submitted (session)    15                                      |
|  Orders filled today (ledger)  15                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             15                                      |
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
|  CRM260724C00185000           15    +12.1%   $   +115.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=26.5s reconcile=4.2s cancel=0.15s manage=0.77s scan=12.71s entries=8.17s
STATUS: options_morning_bot run complete (PAPER) elapsed=26.5s. run=#4421 https://github.com/28twagg-ops/TradingBot/actions/runs/29753933863
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
| Total open lots             |    15 | INFO |
| Total closed lots           |   269 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
```

---

## Run 20260720T151537Z

- UTC timestamp: `20260720T151537Z`
- GitHub run: [#4422](https://github.com/28twagg-ops/TradingBot/actions/runs/29754309599)
- Run id: `29754309599`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`32s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T11:15:40.545060-04:00","date":"2026-07-20","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":29.7,"phases_s":{"reconcile":2.67,"cancel":0.02,"manage":0.32,"scan":22.19,"entries":4.25},"signals":22,"placed":0,"equity":129350.23,"open_positions":1,"pending_orders":0,"open_lots":15,"submitted_today":15,"filled_today":15,"unattributed_contracts":0,"top_signals":["S173:ADM","S173:AXON","S173:FANG","S173:GDDY","S173:INTU","S173:CRM","S173:NOW","S173:WDAY"],"github_run":"4422","github_run_id":"29754309599","status":"ok"}
```

### Live bot full output

```text
15:15:38  INFO      Mode: exits
15:15:39  INFO        Daily log -> logs/daily/2026-07-20.md
15:15:39  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (4 ledger rows)
15:15:39  INFO        place_all_stops: checking 4 positions...
15:15:39  INFO        STOP skipped CI: fractional (0.3102 shares) — software exit will handle it
15:15:39  INFO        STOP already live CNP @ $43.14
15:15:39  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
15:15:39  INFO        STOP already live KO @ $81.47
15:15:39  INFO        [positions] 4/4 (4 valid)
15:15:39  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:15 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.68|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CNP  P&L -0.4%  $-0.38                                            HOLD|
|  CI  P&L -0.0%  $-0.04                                             HOLD|
|  KO  P&L +0.0%  $+0.00                                             HOLD|
|  COP  P&L +0.7%  $+0.60                                            HOLD|
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
=== options_morning_bot (PAPER) 2026-07-20T11:15:40.545060-04:00 ===

[Run context]
Paper auth OK — equity $129350.23, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 22 signal(s); top: ['S173:ADM', 'S173:AXON', 'S173:FANG', 'S173:GDDY', 'S173:INTU', 'S173:CRM', 'S173:NOW', 'S173:WDAY']
Paper lab: $129488 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 50 no tradeable call
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $129,350.23                             |
|  Signals this run              22                                      |
|  Orders submitted (session)    15                                      |
|  Orders filled today (ledger)  15                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             15                                      |
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
|  CRM260724C00185000           15    +26.3%   $   +250.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=29.7s reconcile=2.67s cancel=0.02s manage=0.32s scan=22.19s entries=4.25s
STATUS: options_morning_bot run complete (PAPER) elapsed=29.7s. run=#4422 https://github.com/28twagg-ops/TradingBot/actions/runs/29754309599
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
| Total open lots             |    15 | INFO |
| Total closed lots           |   269 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
```

---

## Run 20260720T152040Z

- UTC timestamp: `20260720T152040Z`
- GitHub run: [#4423](https://github.com/28twagg-ops/TradingBot/actions/runs/29754685938)
- Run id: `29754685938`
- Live bot: exit=`0`, duration=`6s`
- Options bot: exit=`0`, duration=`46s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T11:20:47.238504-04:00","date":"2026-07-20","mode":"entry+manage","header":"entry+manage (5 new)","elapsed_s":44.0,"phases_s":{"reconcile":1.89,"cancel":0.12,"manage":0.81,"scan":20.7,"entries":17.91,"reconcile2":1.94},"signals":24,"placed":5,"equity":129605.23,"open_positions":1,"pending_orders":5,"open_lots":15,"submitted_today":20,"filled_today":15,"unattributed_contracts":0,"top_signals":["S173:ADM","S173:ADSK","S173:AXON","S173:FANG","S173:GDDY","S173:INTU","S173:CRM","S173:NOW"],"github_run":"4423","github_run_id":"29754685938","status":"ok"}
```

### Live bot full output

```text
15:20:42  INFO      Mode: exits
15:20:43  INFO        Daily log -> logs/daily/2026-07-20.md
15:20:43  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (4 ledger rows)
15:20:43  INFO        place_all_stops: checking 4 positions...
15:20:43  INFO        STOP skipped CI: fractional (0.3102 shares) — software exit will handle it
15:20:43  INFO        STOP skipped CNP: fractional (0.2270 shares) — software exit will handle it
15:20:43  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
15:20:43  INFO        STOP already live KO @ $81.47
15:20:43  INFO        [positions] 4/4 (4 valid)
15:20:43  INFO        SELL MARKET [urgent] CNP closed
15:20:46  INFO        TX logged: SELL CNP  P&L -0.62%
15:20:46  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.66|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CNP  P&L -0.6%  $-0.06                         EXIT: stop_loss (-0.6%)|
|  CI  P&L -0.1%  $-0.13                                             HOLD|
|  KO  P&L -0.1%  $-0.08                                             HOLD|
|  COP  P&L +1.0%  $+0.89                                            HOLD|
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
|  CNP                                         -0.62%  (threshold -0.50%)|
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
=== options_morning_bot (PAPER) 2026-07-20T11:20:47.238504-04:00 ===

[Run context]
Paper auth OK — equity $129605.23, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 24 signal(s); top: ['S173:ADM', 'S173:ADSK', 'S173:AXON', 'S173:FANG', 'S173:GDDY', 'S173:INTU', 'S173:CRM', 'S173:NOW']
Paper lab: $129716 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 130 no tradeable call, 35 pending order
Placed 5 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $129,605.23                             |
|  Signals this run              24                                      |
|  Orders submitted (session)    20                                      |
|  Orders filled today (ledger)  15                                      |
|  Entries placed this run       5                                       |
|  Open virtual lots             15                                      |
|  Broker option positions       1                                       |
|  Pending orders                5                                       |
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
|  PENDING ORDERS (5)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S173:CRM(5)                             |
+------------------------------------------------------------------------+
|  b3   S173 CRM      limit=0.62                                         |
|  b23  S173 CRM      limit=0.62                                         |
|  b43  S173 CRM      limit=0.62                                         |
|  b63  S173 CRM      limit=0.62                                         |
|  b83  S173 CRM      limit=0.62                                         |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (1)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  CRM260724C00185000           15    +27.9%   $   +265.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=44.0s reconcile=1.89s cancel=0.12s manage=0.81s scan=20.7s entries=17.91s
STATUS: options_morning_bot run complete (PAPER) elapsed=44.0s. run=#4423 https://github.com/28twagg-ops/TradingBot/actions/runs/29754685938
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
| Total open lots             |    15 | INFO |
| Total closed lots           |   269 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
```

---

## Run 20260720T152539Z

- UTC timestamp: `20260720T152539Z`
- GitHub run: [#4424](https://github.com/28twagg-ops/TradingBot/actions/runs/29755062700)
- Run id: `29755062700`
- Live bot: exit=`0`, duration=`4s`
- Options bot: exit=`0`, duration=`35s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T11:25:44.264502-04:00","date":"2026-07-20","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":33.6,"phases_s":{"reconcile":1.99,"cancel":0.14,"manage":0.74,"scan":19.77,"entries":8.41,"reconcile2":1.99},"signals":24,"placed":0,"equity":129915.23,"open_positions":1,"pending_orders":5,"open_lots":15,"submitted_today":20,"filled_today":15,"unattributed_contracts":0,"top_signals":["S173:ADM","S173:ADSK","S173:AXON","S173:FANG","S173:GDDY","S173:INTU","S173:CRM","S173:NOW"],"github_run":"4424","github_run_id":"29755062700","status":"ok"}
```

### Live bot full output

```text
15:25:41  INFO      Mode: exits
15:25:42  INFO        Daily log -> logs/daily/2026-07-20.md
15:25:42  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (5 ledger rows)
15:25:42  INFO        place_all_stops: checking 3 positions...
15:25:42  INFO        STOP skipped CI: fractional (0.3102 shares) — software exit will handle it
15:25:42  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
15:25:42  INFO        STOP already live KO @ $81.47
15:25:43  INFO        [positions] 3/3 (3 valid)
15:25:43  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:25 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.45|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  KO  P&L -0.3%  $-0.32                                             HOLD|
|  CI  P&L -0.3%  $-0.23                                             HOLD|
|  COP  P&L +1.1%  $+1.01                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
=== options_morning_bot (PAPER) 2026-07-20T11:25:44.264502-04:00 ===

[Run context]
Paper auth OK — equity $129915.23, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 24 signal(s); top: ['S173:ADM', 'S173:ADSK', 'S173:AXON', 'S173:FANG', 'S173:GDDY', 'S173:INTU', 'S173:CRM', 'S173:NOW']
Paper lab: $129939 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 50 no tradeable call, 70 pending order
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $129,915.23                             |
|  Signals this run              24                                      |
|  Orders submitted (session)    20                                      |
|  Orders filled today (ledger)  15                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             15                                      |
|  Broker option positions       1                                       |
|  Pending orders                5                                       |
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
|  PENDING ORDERS (5)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S173:CRM(5)                             |
+------------------------------------------------------------------------+
|  b3   S173 CRM      limit=0.62                                         |
|  b23  S173 CRM      limit=0.62                                         |
|  b43  S173 CRM      limit=0.62                                         |
|  b63  S173 CRM      limit=0.62                                         |
|  b83  S173 CRM      limit=0.62                                         |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (1)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  CRM260724C00185000           15    +35.8%   $   +340.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=33.6s reconcile=1.99s cancel=0.14s manage=0.74s scan=19.77s entries=8.41s
STATUS: options_morning_bot run complete (PAPER) elapsed=33.6s. run=#4424 https://github.com/28twagg-ops/TradingBot/actions/runs/29755062700
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
| Total open lots             |    15 | INFO |
| Total closed lots           |   269 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
```

---

## Run 20260720T153040Z

- UTC timestamp: `20260720T153040Z`
- GitHub run: [#4425](https://github.com/28twagg-ops/TradingBot/actions/runs/29755436207)
- Run id: `29755436207`
- Live bot: exit=`0`, duration=`4s`
- Options bot: exit=`0`, duration=`56s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T11:30:45.160914-04:00","date":"2026-07-20","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":54.4,"phases_s":{"reconcile":2.0,"cancel":0.16,"manage":1.29,"scan":33.58,"entries":10.16,"reconcile2":1.98},"signals":25,"placed":0,"equity":130469.23,"open_positions":1,"pending_orders":5,"open_lots":15,"submitted_today":20,"filled_today":15,"unattributed_contracts":0,"top_signals":["S173:ADM","S173:ADSK","S173:AXON","S173:FANG","S173:GDDY","S173:INTU","S173:CRM","S173:NOW"],"github_run":"4425","github_run_id":"29755436207","status":"ok"}
```

### Live bot full output

```text
15:30:41  INFO      Mode: exits
15:30:43  INFO        Daily log -> logs/daily/2026-07-20.md
15:30:43  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (5 ledger rows)
15:30:43  INFO        place_all_stops: checking 3 positions...
15:30:43  INFO        STOP skipped CI: fractional (0.3102 shares) — software exit will handle it
15:30:43  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
15:30:43  INFO        STOP already live KO @ $81.47
15:30:44  INFO        [positions] 3/3 (3 valid)
15:30:44  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:30 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.38|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  KO  P&L -0.5%  $-0.44                                             HOLD|
|  CI  P&L -0.2%  $-0.19                                             HOLD|
|  COP  P&L +1.2%  $+1.02                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
=== options_morning_bot (PAPER) 2026-07-20T11:30:45.160914-04:00 ===

[Run context]
Paper auth OK — equity $130469.23, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 25 signal(s); top: ['S173:ADM', 'S173:ADSK', 'S173:AXON', 'S173:FANG', 'S173:GDDY', 'S173:INTU', 'S173:CRM', 'S173:NOW']
Paper lab: $130596 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 50 no tradeable call, 75 pending order
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $130,469.23                             |
|  Signals this run              25                                      |
|  Orders submitted (session)    20                                      |
|  Orders filled today (ledger)  15                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             15                                      |
|  Broker option positions       1                                       |
|  Pending orders                5                                       |
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
|  PENDING ORDERS (5)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S173:CRM(5)                             |
+------------------------------------------------------------------------+
|  b3   S173 CRM      limit=0.62                                         |
|  b23  S173 CRM      limit=0.62                                         |
|  b43  S173 CRM      limit=0.62                                         |
|  b63  S173 CRM      limit=0.62                                         |
|  b83  S173 CRM      limit=0.62                                         |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (1)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  CRM260724C00185000           15    +34.2%   $   +325.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=54.4s reconcile=2.0s cancel=0.16s manage=1.29s scan=33.58s entries=10.16s
STATUS: options_morning_bot run complete (PAPER) elapsed=54.4s. run=#4425 https://github.com/28twagg-ops/TradingBot/actions/runs/29755436207
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
| Total open lots             |    15 | INFO |
| Total closed lots           |   269 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
```

---

## Run 20260720T153536Z

- UTC timestamp: `20260720T153536Z`
- GitHub run: [#4426](https://github.com/28twagg-ops/TradingBot/actions/runs/29755818341)
- Run id: `29755818341`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`28s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T11:35:39.675120-04:00","date":"2026-07-20","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":26.7,"phases_s":{"reconcile":1.62,"cancel":0.02,"manage":0.18,"scan":18.68,"entries":4.17,"reconcile2":1.76},"signals":25,"placed":0,"equity":130578.23,"open_positions":1,"pending_orders":5,"open_lots":15,"submitted_today":20,"filled_today":15,"unattributed_contracts":0,"top_signals":["S173:ADM","S173:ADSK","S173:AXON","S173:FANG","S173:GDDY","S173:INTU","S173:CRM","S173:NOW"],"github_run":"4426","github_run_id":"29755818341","status":"ok"}
```

### Live bot full output

```text
15:35:38  INFO      Mode: exits
15:35:38  INFO        Daily log -> logs/daily/2026-07-20.md
15:35:38  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (5 ledger rows)
15:35:38  INFO        place_all_stops: checking 3 positions...
15:35:38  INFO        STOP skipped CI: fractional (0.3102 shares) — software exit will handle it
15:35:38  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
15:35:38  INFO        STOP already live KO @ $81.47
15:35:38  INFO        [positions] 3/3 (3 valid)
15:35:38  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:35 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.26|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  KO  P&L -0.5%  $-0.47                                             HOLD|
|  CI  P&L -0.3%  $-0.27                                             HOLD|
|  COP  P&L +1.2%  $+1.03                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
=== options_morning_bot (PAPER) 2026-07-20T11:35:39.675120-04:00 ===

[Run context]
Paper auth OK — equity $130578.23, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Scan + entries]
Scanning 903 symbols for [S173, S165, S166, S163] …
Fetched daily bars for 903/903 symbols
Found 25 signal(s); top: ['S173:ADM', 'S173:ADSK', 'S173:AXON', 'S173:FANG', 'S173:GDDY', 'S173:INTU', 'S173:CRM', 'S173:NOW']
Paper lab: $130589 broker equity -> 100 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 50 no tradeable call, 75 pending order
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $130,578.23                             |
|  Signals this run              25                                      |
|  Orders submitted (session)    20                                      |
|  Orders filled today (ledger)  15                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             15                                      |
|  Broker option positions       1                                       |
|  Pending orders                5                                       |
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
|  PENDING ORDERS (5)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S173:CRM(5)                             |
+------------------------------------------------------------------------+
|  b3   S173 CRM      limit=0.62                                         |
|  b23  S173 CRM      limit=0.62                                         |
|  b43  S173 CRM      limit=0.62                                         |
|  b63  S173 CRM      limit=0.62                                         |
|  b83  S173 CRM      limit=0.62                                         |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (1)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  CRM260724C00185000           15    +34.2%   $   +325.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=26.7s reconcile=1.62s cancel=0.02s manage=0.18s scan=18.68s entries=4.17s
STATUS: options_morning_bot run complete (PAPER) elapsed=26.7s. run=#4426 https://github.com/28twagg-ops/TradingBot/actions/runs/29755818341
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
| Total open lots             |    15 | INFO |
| Total closed lots           |   269 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
```

---

## Run 20260720T154038Z

- UTC timestamp: `20260720T154038Z`
- GitHub run: [#4427](https://github.com/28twagg-ops/TradingBot/actions/runs/29756201576)
- Run id: `29756201576`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`6s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T11:40:41.536892-04:00","date":"2026-07-20","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":3.7,"phases_s":{"reconcile":2.32,"cancel":0.14,"manage":0.69},"signals":0,"placed":0,"equity":130072.13,"open_positions":2,"pending_orders":0,"open_lots":20,"submitted_today":20,"filled_today":20,"unattributed_contracts":0,"top_signals":[],"github_run":"4427","github_run_id":"29756201576","status":"ok"}
```

### Live bot full output

```text
15:40:39  INFO      Mode: exits
15:40:39  INFO        Daily log -> logs/daily/2026-07-20.md
15:40:39  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (5 ledger rows)
15:40:39  INFO        place_all_stops: checking 3 positions...
15:40:39  INFO        STOP skipped CI: fractional (0.3102 shares) — software exit will handle it
15:40:39  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
15:40:39  INFO        STOP skipped KO: fractional (0.1793 shares) — software exit will handle it
15:40:40  INFO        [positions] 3/3 (3 valid)
15:40:40  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:40 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.00|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CI  P&L -0.4%  $-0.36                                             HOLD|
|  KO  P&L -0.4%  $-0.06                                             HOLD|
|  COP  P&L +1.0%  $+0.86                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
=== options_morning_bot (PAPER) 2026-07-20T11:40:41.536892-04:00 ===

[Run context]
Paper auth OK — equity $130072.13, account PA36KS87UPRS

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
|  Equity                        $130,072.13                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    20                                      |
|  Orders filled today (ledger)  20                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             20                                      |
|  Broker option positions       2                                       |
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
|  OPEN OPTIONS (2)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  CRM260724C00185000           15    +29.5%   $   +280.00               |
|  CRM260724C00187500            5     -4.8%   $    -15.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=3.7s reconcile=2.32s cancel=0.14s manage=0.69s
STATUS: options_morning_bot run complete (PAPER) elapsed=3.7s. run=#4427 https://github.com/28twagg-ops/TradingBot/actions/runs/29756201576
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
| Total open lots             |    20 | INFO |
| Total closed lots           |   269 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
```

---

## Run 20260720T154539Z

- UTC timestamp: `20260720T154539Z`
- GitHub run: [#4428](https://github.com/28twagg-ops/TradingBot/actions/runs/29756580077)
- Run id: `29756580077`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`6s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T11:45:43.300484-04:00","date":"2026-07-20","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":4.5,"phases_s":{"reconcile":2.05,"cancel":0.22,"manage":1.29},"signals":0,"placed":0,"equity":130626.13,"open_positions":2,"pending_orders":0,"open_lots":20,"submitted_today":20,"filled_today":20,"unattributed_contracts":0,"top_signals":[],"github_run":"4428","github_run_id":"29756580077","status":"ok"}
```

### Live bot full output

```text
15:45:40  INFO      Mode: exits
15:45:41  INFO        Daily log -> logs/daily/2026-07-20.md
15:45:41  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (5 ledger rows)
15:45:41  INFO        place_all_stops: checking 3 positions...
15:45:41  INFO        STOP skipped CI: fractional (0.3102 shares) — software exit will handle it
15:45:41  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
15:45:41  INFO        STOP skipped KO: fractional (0.1793 shares) — software exit will handle it
15:45:41  INFO        [positions] 3/3 (3 valid)
15:45:42  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:45 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.19|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  KO  P&L -0.4%  $-0.06                                             HOLD|
|  CI  P&L -0.4%  $-0.31                                             HOLD|
|  COP  P&L +1.1%  $+1.01                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
=== options_morning_bot (PAPER) 2026-07-20T11:45:43.300484-04:00 ===

[Run context]
Paper auth OK — equity $130626.13, account PA36KS87UPRS

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
|  Equity                        $130,626.13                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    20                                      |
|  Orders filled today (ledger)  20                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             20                                      |
|  Broker option positions       2                                       |
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
|  OPEN OPTIONS (2)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  CRM260724C00185000           15    +32.6%   $   +310.00               |
|  CRM260724C00187500            5     -4.8%   $    -15.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=4.5s reconcile=2.05s cancel=0.22s manage=1.29s
STATUS: options_morning_bot run complete (PAPER) elapsed=4.5s. run=#4428 https://github.com/28twagg-ops/TradingBot/actions/runs/29756580077
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
| Total open lots             |    20 | INFO |
| Total closed lots           |   269 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
```

---

## Run 20260720T155051Z

- UTC timestamp: `20260720T155051Z`
- GitHub run: [#4429](https://github.com/28twagg-ops/TradingBot/actions/runs/29756943582)
- Run id: `29756943582`
- Live bot: exit=`0`, duration=`4s`
- Options bot: exit=`0`, duration=`6s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T11:50:56.113639-04:00","date":"2026-07-20","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":4.7,"phases_s":{"reconcile":2.0,"cancel":0.24,"manage":1.4},"signals":0,"placed":0,"equity":130176.13,"open_positions":2,"pending_orders":0,"open_lots":20,"submitted_today":20,"filled_today":20,"unattributed_contracts":0,"top_signals":[],"github_run":"4429","github_run_id":"29756943582","status":"ok"}
```

### Live bot full output

```text
15:50:53  INFO      Mode: exits
15:50:54  INFO        Daily log -> logs/daily/2026-07-20.md
15:50:54  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (5 ledger rows)
15:50:54  INFO        place_all_stops: checking 3 positions...
15:50:54  INFO        STOP skipped CI: fractional (0.3102 shares) — software exit will handle it
15:50:54  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
15:50:54  INFO        STOP skipped KO: fractional (0.1793 shares) — software exit will handle it
15:50:54  INFO        [positions] 3/3 (3 valid)
15:50:55  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:50 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.37|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  KO  P&L -0.4%  $-0.05                                             HOLD|
|  CI  P&L -0.2%  $-0.17                                             HOLD|
|  COP  P&L +1.2%  $+1.04                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
=== options_morning_bot (PAPER) 2026-07-20T11:50:56.113639-04:00 ===

[Run context]
Paper auth OK — equity $130176.13, account PA36KS87UPRS

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
|  Equity                        $130,176.13                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    20                                      |
|  Orders filled today (ledger)  20                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             20                                      |
|  Broker option positions       2                                       |
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
|  OPEN OPTIONS (2)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  CRM260724C00185000           15    +37.4%   $   +355.00               |
|  CRM260724C00187500            5     +0.0%   $     +0.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=4.7s reconcile=2.0s cancel=0.24s manage=1.4s
STATUS: options_morning_bot run complete (PAPER) elapsed=4.7s. run=#4429 https://github.com/28twagg-ops/TradingBot/actions/runs/29756943582
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
| Total open lots             |    20 | INFO |
| Total closed lots           |   269 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
```

---

## Run 20260720T155534Z

- UTC timestamp: `20260720T155534Z`
- GitHub run: [#4430](https://github.com/28twagg-ops/TradingBot/actions/runs/29757308487)
- Run id: `29757308487`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`7s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T11:55:36.458616-04:00","date":"2026-07-20","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":5.9,"phases_s":{"reconcile":4.37,"cancel":0.09,"manage":0.6},"signals":0,"placed":0,"equity":130672.13,"open_positions":2,"pending_orders":0,"open_lots":20,"submitted_today":20,"filled_today":20,"unattributed_contracts":0,"top_signals":[],"github_run":"4430","github_run_id":"29757308487","status":"ok"}
```

### Live bot full output

```text
15:55:34  INFO      Mode: exits
15:55:35  INFO        Daily log -> logs/daily/2026-07-20.md
15:55:35  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (5 ledger rows)
15:55:35  INFO        place_all_stops: checking 3 positions...
15:55:35  INFO        STOP skipped CI: fractional (0.3102 shares) — software exit will handle it
15:55:35  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
15:55:35  INFO        STOP skipped KO: fractional (0.1793 shares) — software exit will handle it
15:55:35  INFO        [positions] 3/3 (3 valid)
15:55:35  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:55 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.31|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  KO  P&L -0.5%  $-0.07                                             HOLD|
|  CI  P&L -0.2%  $-0.20                                             HOLD|
|  COP  P&L +1.2%  $+1.03                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
=== options_morning_bot (PAPER) 2026-07-20T11:55:36.458616-04:00 ===

[Run context]
Paper auth OK — equity $130672.13, account PA36KS87UPRS

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
|  Equity                        $130,672.13                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    20                                      |
|  Orders filled today (ledger)  20                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             20                                      |
|  Broker option positions       2                                       |
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
|  OPEN OPTIONS (2)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  CRM260724C00185000           15    +35.8%   $   +340.00               |
|  CRM260724C00187500            5     +0.0%   $     +0.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=5.9s reconcile=4.37s cancel=0.09s manage=0.6s
STATUS: options_morning_bot run complete (PAPER) elapsed=5.9s. run=#4430 https://github.com/28twagg-ops/TradingBot/actions/runs/29757308487
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
| Total open lots             |    20 | INFO |
| Total closed lots           |   269 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
```

---

## Run 20260720T160044Z

- UTC timestamp: `20260720T160044Z`
- GitHub run: [#4432](https://github.com/28twagg-ops/TradingBot/actions/runs/29757670708)
- Run id: `29757670708`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`6s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T12:00:47.344126-04:00","date":"2026-07-20","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":4.2,"phases_s":{"reconcile":1.77,"cancel":0.11,"manage":1.94},"signals":0,"placed":0,"equity":130939.13,"open_positions":2,"pending_orders":0,"open_lots":20,"submitted_today":20,"filled_today":20,"unattributed_contracts":0,"top_signals":[],"github_run":"4432","github_run_id":"29757670708","status":"ok"}
```

### Live bot full output

```text
16:00:45  INFO      Mode: exits
16:00:46  INFO        Daily log -> logs/daily/2026-07-20.md
16:00:46  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (5 ledger rows)
16:00:46  INFO        place_all_stops: checking 3 positions...
16:00:46  INFO        STOP skipped CI: fractional (0.3102 shares) — software exit will handle it
16:00:46  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
16:00:46  INFO        STOP skipped KO: fractional (0.1793 shares) — software exit will handle it
16:00:46  INFO        [positions] 3/3 (3 valid)
16:00:46  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:00 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.19|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  KO  P&L -0.5%  $-0.07                                             HOLD|
|  CI  P&L -0.3%  $-0.26                                             HOLD|
|  COP  P&L +1.1%  $+0.97                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
=== options_morning_bot (PAPER) 2026-07-20T12:00:47.344126-04:00 ===

[Run context]
Paper auth OK — equity $130939.13, account PA36KS87UPRS

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
|  Equity                        $130,939.13                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    20                                      |
|  Orders filled today (ledger)  20                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             20                                      |
|  Broker option positions       2                                       |
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
|  OPEN OPTIONS (2)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  CRM260724C00185000           15    +38.9%   $   +370.00               |
|  CRM260724C00187500            5     +3.2%   $    +10.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=4.2s reconcile=1.77s cancel=0.11s manage=1.94s
STATUS: options_morning_bot run complete (PAPER) elapsed=4.2s. run=#4432 https://github.com/28twagg-ops/TradingBot/actions/runs/29757670708
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
| Total open lots             |    20 | INFO |
| Total closed lots           |   269 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
```

---

## Run 20260720T160537Z

- UTC timestamp: `20260720T160537Z`
- GitHub run: [#4433](https://github.com/28twagg-ops/TradingBot/actions/runs/29758036223)
- Run id: `29758036223`
- Live bot: exit=`0`, duration=`4s`
- Options bot: exit=`0`, duration=`4s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T12:05:42.031511-04:00","date":"2026-07-20","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":2.8,"phases_s":{"reconcile":1.61,"cancel":0.04,"manage":0.6},"signals":0,"placed":0,"equity":131353.01,"open_positions":2,"pending_orders":0,"open_lots":20,"submitted_today":20,"filled_today":20,"unattributed_contracts":0,"top_signals":[],"github_run":"4433","github_run_id":"29758036223","status":"ok"}
```

### Live bot full output

```text
16:05:37  INFO      Mode: exits
16:05:38  INFO        Daily log -> logs/daily/2026-07-20.md
16:05:38  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (5 ledger rows)
16:05:38  INFO        place_all_stops: checking 3 positions...
16:05:38  INFO        STOP skipped CI: fractional (0.3102 shares) — software exit will handle it
16:05:38  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
16:05:38  INFO        STOP skipped KO: fractional (0.1793 shares) — software exit will handle it
16:05:38  INFO        [positions] 3/3 (3 valid)
16:05:38  INFO        SELL MARKET [urgent] KO closed
16:05:41  INFO        TX logged: SELL KO  P&L -0.56%
16:05:41  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:05 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.28|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  KO  P&L -0.6%  $-0.08                          EXIT: stop_loss (-0.6%)|
|  CI  P&L -0.2%  $-0.16                                             HOLD|
|  COP  P&L +1.1%  $+0.98                                            HOLD|
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
|  KO                                          -0.56%  (threshold -0.50%)|
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
=== options_morning_bot (PAPER) 2026-07-20T12:05:42.031511-04:00 ===

[Run context]
Paper auth OK — equity $131341.01, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-20 12:05:44,635 INFO   EXIT [b80|c080_s173_w1_0928_1005_r5|S173] take_profit (+62.6%) SELL 1 CRM260724C00185000 @<= 1.00

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $131,353.01                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    20                                      |
|  Orders filled today (ledger)  20                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             20                                      |
|  Broker option positions       2                                       |
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
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b80  S173 CRM260724C00185000 x1 take_profit (+62.6%)                  |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (2)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  CRM260724C00185000           15    +62.6%   $   +595.00               |
|  CRM260724C00187500            5    +12.9%   $    +40.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=2.8s reconcile=1.61s cancel=0.04s manage=0.6s
STATUS: options_morning_bot run complete (PAPER) elapsed=2.8s. run=#4433 https://github.com/28twagg-ops/TradingBot/actions/runs/29758036223
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
| Total open lots             |    20 | INFO |
| Total closed lots           |   269 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
```

---

## Run 20260720T161036Z

- UTC timestamp: `20260720T161036Z`
- GitHub run: [#4434](https://github.com/28twagg-ops/TradingBot/actions/runs/29758408685)
- Run id: `29758408685`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`4s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T12:10:38.965622-04:00","date":"2026-07-20","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":3.0,"phases_s":{"reconcile":1.72,"cancel":0.07,"manage":0.66},"signals":0,"placed":0,"equity":131479.35,"open_positions":2,"pending_orders":0,"open_lots":19,"submitted_today":20,"filled_today":20,"unattributed_contracts":0,"top_signals":[],"github_run":"4434","github_run_id":"29758408685","status":"ok"}
```

### Live bot full output

```text
16:10:37  INFO      Mode: exits
16:10:37  INFO        Daily log -> logs/daily/2026-07-20.md
16:10:37  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (6 ledger rows)
16:10:37  INFO        place_all_stops: checking 2 positions...
16:10:37  INFO        STOP skipped CI: fractional (0.3102 shares) — software exit will handle it
16:10:37  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
16:10:37  INFO        [positions] 2/2 (2 valid)
16:10:38  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.12|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CI  P&L -0.4%  $-0.34                                             HOLD|
|  COP  P&L +1.1%  $+0.98                                            HOLD|
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
=== options_morning_bot (PAPER) 2026-07-20T12:10:38.965622-04:00 ===

[Run context]
Paper auth OK — equity $131479.35, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-20 12:10:41,505 INFO   EXIT [b40|c040_s173_w1_0928_1005_r3|S173] take_profit (+62.6%) SELL 1 CRM260724C00185000 @<= 1.04

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $131,479.35                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    20                                      |
|  Orders filled today (ledger)  20                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             19                                      |
|  Broker option positions       2                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=498  buckets=49  win=35%                             |
|  Returns   avg=+7.6%  med=-33.6%  p10=-77.0%  p90=+93.4%               |
|  Realized  $+3,647.77                                                  |
|  Raw incl dropped  trades=612  real=$+2,149.58                         |
|  Today     trades=1  avg=+63.5%  med=+63.5%  real=$+40.00              |
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
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b40  S173 CRM260724C00185000 x1 take_profit (+62.6%)                  |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (2)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  CRM260724C00185000           14    +62.6%   $   +555.33               |
|  CRM260724C00187500            5    +14.5%   $    +45.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=3.0s reconcile=1.72s cancel=0.07s manage=0.66s
STATUS: options_morning_bot run complete (PAPER) elapsed=3.0s. run=#4434 https://github.com/28twagg-ops/TradingBot/actions/runs/29758408685
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.csv
Summary: 1 buckets closed trades, $+40.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 3.6% (22/612)
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
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |    19 | INFO |
| Total closed lots           |   270 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
```

---

## Run 20260720T161537Z

- UTC timestamp: `20260720T161537Z`
- GitHub run: [#4435](https://github.com/28twagg-ops/TradingBot/actions/runs/29758775879)
- Run id: `29758775879`
- Live bot: exit=`0`, duration=`4s`
- Options bot: exit=`0`, duration=`5s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T12:15:41.753004-04:00","date":"2026-07-20","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":4.1,"phases_s":{"reconcile":1.96,"cancel":0.24,"manage":1.31},"signals":0,"placed":0,"equity":131455.09,"open_positions":2,"pending_orders":0,"open_lots":18,"submitted_today":20,"filled_today":20,"unattributed_contracts":0,"top_signals":[],"github_run":"4435","github_run_id":"29758775879","status":"ok"}
```

### Live bot full output

```text
16:15:38  INFO      Mode: exits
16:15:40  INFO        Daily log -> logs/daily/2026-07-20.md
16:15:40  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (6 ledger rows)
16:15:40  INFO        place_all_stops: checking 2 positions...
16:15:40  INFO        STOP skipped CI: fractional (0.3102 shares) — software exit will handle it
16:15:40  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
16:15:40  INFO        [positions] 2/2 (2 valid)
16:15:40  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:15 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.27|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CI  P&L -0.3%  $-0.27                                             HOLD|
|  COP  P&L +1.2%  $+1.06                                            HOLD|
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
=== options_morning_bot (PAPER) 2026-07-20T12:15:41.753004-04:00 ===

[Run context]
Paper auth OK — equity $131455.09, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-20 12:15:45,223 INFO   EXIT [b41|c041_s173_w2_1005_1045_r3|S173] take_profit (+64.2%) SELL 1 CRM260724C00185000 @<= 1.01

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $131,455.09                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    20                                      |
|  Orders filled today (ledger)  20                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             18                                      |
|  Broker option positions       2                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=499  buckets=49  win=35%                             |
|  Returns   avg=+7.7%  med=-33.3%  p10=-77.0%  p90=+93.3%               |
|  Realized  $+3,688.77                                                  |
|  Raw incl dropped  trades=613  real=$+2,190.58                         |
|  Today     trades=2  avg=+64.3%  med=+64.3%  real=$+81.00              |
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
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b41  S173 CRM260724C00185000 x1 take_profit (+64.2%)                  |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (2)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  CRM260724C00185000           12    +64.2%   $   +488.00               |
|  CRM260724C00187500            5    +14.5%   $    +45.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=4.1s reconcile=1.96s cancel=0.24s manage=1.31s
STATUS: options_morning_bot run complete (PAPER) elapsed=4.1s. run=#4435 https://github.com/28twagg-ops/TradingBot/actions/runs/29758775879
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.csv
Summary: 2 buckets closed trades, $+81.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 3.6% (22/613)
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
| Total open lots             |    18 | INFO |
| Total closed lots           |   270 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
```

---

## Run 20260720T162036Z

- UTC timestamp: `20260720T162036Z`
- GitHub run: [#4436](https://github.com/28twagg-ops/TradingBot/actions/runs/29759138098)
- Run id: `29759138098`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`4s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T12:20:39.947678-04:00","date":"2026-07-20","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":2.7,"phases_s":{"reconcile":1.78,"cancel":0.06,"manage":0.54},"signals":0,"placed":0,"equity":131377.11,"open_positions":2,"pending_orders":0,"open_lots":17,"submitted_today":20,"filled_today":20,"unattributed_contracts":0,"top_signals":[],"github_run":"4436","github_run_id":"29759138098","status":"ok"}
```

### Live bot full output

```text
16:20:38  INFO      Mode: exits
16:20:38  INFO        Daily log -> logs/daily/2026-07-20.md
16:20:38  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (6 ledger rows)
16:20:38  INFO        place_all_stops: checking 2 positions...
16:20:38  INFO        STOP skipped CI: fractional (0.3102 shares) — software exit will handle it
16:20:38  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
16:20:39  INFO        [positions] 2/2 (2 valid)
16:20:39  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.05|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CI  P&L -0.5%  $-0.40                                             HOLD|
|  COP  P&L +1.1%  $+0.98                                            HOLD|
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
=== options_morning_bot (PAPER) 2026-07-20T12:20:39.947678-04:00 ===

[Run context]
Paper auth OK — equity $131377.11, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-20 12:20:42,475 INFO   EXIT [b61|c061_s173_w2_1005_1045_r4|S173] take_profit (+70.5%) SELL 1 CRM260724C00185000 @<= 1.05

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $131,377.11                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    20                                      |
|  Orders filled today (ledger)  20                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             17                                      |
|  Broker option positions       2                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=500  buckets=49  win=35%                             |
|  Returns   avg=+7.8%  med=-33.3%  p10=-77.0%  p90=+93.2%               |
|  Realized  $+3,735.77                                                  |
|  Raw incl dropped  trades=614  real=$+2,237.58                         |
|  Today     trades=3  avg=+70.3%  med=+65.1%  real=$+128.00             |
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
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b61  S173 CRM260724C00185000 x1 take_profit (+70.5%)                  |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (2)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  CRM260724C00185000           12    +70.5%   $   +536.00               |
|  CRM260724C00187500            5    +17.7%   $    +55.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=2.7s reconcile=1.78s cancel=0.06s manage=0.54s
STATUS: options_morning_bot run complete (PAPER) elapsed=2.7s. run=#4436 https://github.com/28twagg-ops/TradingBot/actions/runs/29759138098
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.csv
Summary: 3 buckets closed trades, $+128.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 3.6% (22/614)
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
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |    17 | INFO |
| Total closed lots           |   271 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
```

---

## Run 20260720T162535Z

- UTC timestamp: `20260720T162535Z`
- GitHub run: [#4437](https://github.com/28twagg-ops/TradingBot/actions/runs/29759498521)
- Run id: `29759498521`
- Live bot: exit=`0`, duration=`4s`
- Options bot: exit=`0`, duration=`4s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T12:25:40.638553-04:00","date":"2026-07-20","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":2.6,"phases_s":{"reconcile":1.62,"cancel":0.07,"manage":0.56},"signals":0,"placed":0,"equity":131241.05,"open_positions":2,"pending_orders":0,"open_lots":16,"submitted_today":20,"filled_today":20,"unattributed_contracts":0,"top_signals":[],"github_run":"4437","github_run_id":"29759498521","status":"ok"}
```

### Live bot full output

```text
16:25:36  INFO      Mode: exits
16:25:37  INFO        Daily log -> logs/daily/2026-07-20.md
16:25:37  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (6 ledger rows)
16:25:37  INFO        place_all_stops: checking 2 positions...
16:25:37  INFO        STOP skipped CI: fractional (0.3102 shares) — software exit will handle it
16:25:37  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
16:25:37  INFO        [positions] 2/2 (2 valid)
16:25:37  INFO        SELL MARKET [urgent] CI closed
16:25:39  INFO        TX logged: SELL CI  P&L -0.58%
16:25:39  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:25 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.05|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CI  P&L -0.6%  $-0.52                          EXIT: stop_loss (-0.6%)|
|  COP  P&L +1.2%  $+1.10                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  1 attempted  |  1 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
|  Logged exits                                                         1|
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  CI                                          -0.58%  (threshold -0.50%)|
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
=== options_morning_bot (PAPER) 2026-07-20T12:25:40.638553-04:00 ===

[Run context]
Paper auth OK — equity $131241.05, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-20 12:25:43,005 INFO   EXIT [b2|c002_s173_w3_1045_1120_r1|S173] take_profit (+81.6%) SELL 1 CRM260724C00185000 @<= 1.12

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $131,241.05                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    20                                      |
|  Orders filled today (ledger)  20                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             16                                      |
|  Broker option positions       2                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=501  buckets=49  win=35%                             |
|  Returns   avg=+8.0%  med=-33.3%  p10=-77.0%  p90=+93.1%               |
|  Realized  $+3,786.77                                                  |
|  Raw incl dropped  trades=615  real=$+2,288.58                         |
|  Today     trades=4  avg=+75.1%  med=+73.8%  real=$+179.00             |
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
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b2   S173 CRM260724C00185000 x1 take_profit (+81.6%)                  |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (2)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  CRM260724C00185000           11    +81.6%   $   +568.33               |
|  CRM260724C00187500            5    +25.8%   $    +80.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=2.6s reconcile=1.62s cancel=0.07s manage=0.56s
STATUS: options_morning_bot run complete (PAPER) elapsed=2.6s. run=#4437 https://github.com/28twagg-ops/TradingBot/actions/runs/29759498521
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.csv
Summary: 4 buckets closed trades, $+179.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 3.6% (22/615)
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
| State/ledger mismatches     |    10 | WARN | <<<
| Total open lots             |    16 | INFO |
| Total closed lots           |   271 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
```

---

## Run 20260720T163039Z

- UTC timestamp: `20260720T163039Z`
- GitHub run: [#4438](https://github.com/28twagg-ops/TradingBot/actions/runs/29759856499)
- Run id: `29759856499`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`6s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T12:30:43.232933-04:00","date":"2026-07-20","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":4.6,"phases_s":{"reconcile":2.01,"cancel":0.23,"manage":1.76},"signals":0,"placed":0,"equity":131516.03,"open_positions":2,"pending_orders":0,"open_lots":15,"submitted_today":20,"filled_today":20,"unattributed_contracts":0,"top_signals":[],"github_run":"4438","github_run_id":"29759856499","status":"ok"}
```

### Live bot full output

```text
16:30:39  INFO      Mode: exits
16:30:41  INFO        Daily log -> logs/daily/2026-07-20.md
16:30:41  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (7 ledger rows)
16:30:41  INFO        place_all_stops: checking 1 positions...
16:30:41  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
16:30:41  INFO        [positions] 1/1 (1 valid)
16:30:42  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:30 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.13|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  COP  P&L +1.3%  $+1.19                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_morning_bot (PAPER) 2026-07-20T12:30:43.232933-04:00 ===

[Run context]
Paper auth OK — equity $131516.03, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-20 12:30:47,582 INFO   EXIT [b0|c000_s173_w1_0928_1005_r1|S173] take_profit (+94.2%) SELL 1 CRM260724C00185000 @<= 1.24

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $131,516.03                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    20                                      |
|  Orders filled today (ledger)  20                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             15                                      |
|  Broker option positions       2                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=502  buckets=49  win=35%                             |
|  Returns   avg=+8.1%  med=-32.8%  p10=-77.0%  p90=+92.9%               |
|  Realized  $+3,831.77                                                  |
|  Raw incl dropped  trades=616  real=$+2,333.58                         |
|  Today     trades=5  avg=+73.0%  med=+65.1%  real=$+224.00             |
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
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b0   S173 CRM260724C00185000 x1 take_profit (+94.2%)                  |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (2)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  CRM260724C00185000           10    +94.2%   $   +596.67               |
|  CRM260724C00187500            5    +33.9%   $   +105.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=4.6s reconcile=2.01s cancel=0.23s manage=1.76s
STATUS: options_morning_bot run complete (PAPER) elapsed=4.6s. run=#4438 https://github.com/28twagg-ops/TradingBot/actions/runs/29759856499
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.csv
Summary: 5 buckets closed trades, $+224.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 3.6% (22/616)
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
| State/ledger mismatches     |    10 | WARN | <<<
| Total open lots             |    15 | INFO |
| Total closed lots           |   272 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
```

---

## Run 20260720T163537Z

- UTC timestamp: `20260720T163537Z`
- GitHub run: [#4439](https://github.com/28twagg-ops/TradingBot/actions/runs/29760222824)
- Run id: `29760222824`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`5s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T12:35:39.933091-04:00","date":"2026-07-20","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":3.8,"phases_s":{"reconcile":1.93,"cancel":0.18,"manage":1.2},"signals":0,"placed":0,"equity":131661.01,"open_positions":2,"pending_orders":0,"open_lots":14,"submitted_today":20,"filled_today":20,"unattributed_contracts":0,"top_signals":[],"github_run":"4439","github_run_id":"29760222824","status":"ok"}
```

### Live bot full output

```text
16:35:37  INFO      Mode: exits
16:35:38  INFO        Daily log -> logs/daily/2026-07-20.md
16:35:38  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (7 ledger rows)
16:35:38  INFO        place_all_stops: checking 1 positions...
16:35:38  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
16:35:39  INFO        [positions] 1/1 (1 valid)
16:35:39  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:35 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.06|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  COP  P&L +1.3%  $+1.12                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_morning_bot (PAPER) 2026-07-20T12:35:39.933091-04:00 ===

[Run context]
Paper auth OK — equity $131661.01, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-20 12:35:43,266 INFO   EXIT [b42|c042_s173_w3_1045_1120_r3|S173] take_profit (+95.8%) SELL 1 CRM260724C00185000 @<= 1.25

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $131,661.01                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    20                                      |
|  Orders filled today (ledger)  20                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             14                                      |
|  Broker option positions       2                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=503  buckets=49  win=35%                             |
|  Returns   avg=+8.3%  med=-32.3%  p10=-77.0%  p90=+93.9%               |
|  Realized  $+3,893.77                                                  |
|  Raw incl dropped  trades=617  real=$+2,395.58                         |
|  Today     trades=6  avg=+77.2%  med=+73.8%  real=$+286.00             |
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
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b42  S173 CRM260724C00185000 x1 take_profit (+95.8%)                  |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (2)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  CRM260724C00185000            9    +95.8%   $   +546.00               |
|  CRM260724C00187500            5    +40.3%   $   +125.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=3.8s reconcile=1.93s cancel=0.18s manage=1.2s
STATUS: options_morning_bot run complete (PAPER) elapsed=3.8s. run=#4439 https://github.com/28twagg-ops/TradingBot/actions/runs/29760222824
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.csv
Summary: 6 buckets closed trades, $+286.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 3.6% (22/617)
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
| State/ledger mismatches     |     9 | WARN | <<<
| Total open lots             |    14 | INFO |
| Total closed lots           |   272 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
```

---

## Run 20260720T164036Z

- UTC timestamp: `20260720T164036Z`
- GitHub run: [#4440](https://github.com/28twagg-ops/TradingBot/actions/runs/29760572360)
- Run id: `29760572360`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`6s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T12:40:39.671498-04:00","date":"2026-07-20","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":4.1,"phases_s":{"reconcile":1.91,"cancel":0.23,"manage":1.35},"signals":0,"placed":0,"equity":131681.47,"open_positions":2,"pending_orders":0,"open_lots":13,"submitted_today":20,"filled_today":20,"unattributed_contracts":0,"top_signals":[],"github_run":"4440","github_run_id":"29760572360","status":"ok"}
```

### Live bot full output

```text
16:40:37  INFO      Mode: exits
16:40:38  INFO        Daily log -> logs/daily/2026-07-20.md
16:40:38  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (7 ledger rows)
16:40:38  INFO        place_all_stops: checking 1 positions...
16:40:38  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
16:40:38  INFO        [positions] 1/1 (1 valid)
16:40:38  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:40 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.06|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  COP  P&L +1.3%  $+1.12                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_morning_bot (PAPER) 2026-07-20T12:40:39.671498-04:00 ===

[Run context]
Paper auth OK — equity $131681.47, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-20 12:40:43,506 INFO   EXIT [b0|c000_s173_w1_0928_1005_r1|S173] take_profit (+102.1%) SELL 1 CRM260724C00185000 @<= 1.25

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $131,681.47                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    20                                      |
|  Orders filled today (ledger)  20                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             13                                      |
|  Broker option positions       2                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=504  buckets=49  win=35%                             |
|  Returns   avg=+8.4%  med=-31.9%  p10=-77.0%  p90=+93.8%               |
|  Realized  $+3,950.77                                                  |
|  Raw incl dropped  trades=618  real=$+2,452.58                         |
|  Today     trades=7  avg=+77.8%  med=+81.4%  real=$+343.00             |
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
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b0   S173 CRM260724C00185000 x1 take_profit (+102.1%                  |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (2)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  CRM260724C00185000            7   +102.1%   $   +452.67               |
|  CRM260724C00187500            5    +45.2%   $   +140.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=4.1s reconcile=1.91s cancel=0.23s manage=1.35s
STATUS: options_morning_bot run complete (PAPER) elapsed=4.1s. run=#4440 https://github.com/28twagg-ops/TradingBot/actions/runs/29760572360
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.csv
Summary: 7 buckets closed trades, $+343.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 3.6% (22/618)
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
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |    13 | INFO |
| Total closed lots           |   272 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
```

---

## Run 20260720T164540Z

- UTC timestamp: `20260720T164540Z`
- GitHub run: [#4441](https://github.com/28twagg-ops/TradingBot/actions/runs/29760921990)
- Run id: `29760921990`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`6s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T12:45:44.685887-04:00","date":"2026-07-20","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":4.4,"phases_s":{"reconcile":1.92,"cancel":0.23,"manage":1.69},"signals":0,"placed":0,"equity":131208.09,"open_positions":2,"pending_orders":0,"open_lots":12,"submitted_today":20,"filled_today":20,"unattributed_contracts":0,"top_signals":[],"github_run":"4441","github_run_id":"29760921990","status":"ok"}
```

### Live bot full output

```text
16:45:42  INFO      Mode: exits
16:45:43  INFO        Daily log -> logs/daily/2026-07-20.md
16:45:43  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (7 ledger rows)
16:45:43  INFO        place_all_stops: checking 1 positions...
16:45:43  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
16:45:43  INFO        [positions] 1/1 (1 valid)
16:45:43  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:45 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.26|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  COP  P&L +1.5%  $+1.32                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_morning_bot (PAPER) 2026-07-20T12:45:44.685887-04:00 ===

[Run context]
Paper auth OK — equity $131208.09, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-20 12:45:48,361 INFO   EXIT [b83|c083_s173_w4_1120_1135_r5|S173] take_profit (+53.2%) SELL 1 CRM260724C00187500 @<= 0.92
2026-07-20 12:45:48,879 INFO   EXIT [b2|c002_s173_w3_1045_1120_r1|S173] take_profit (+106.8%) SELL 1 CRM260724C00185000 @<= 1.32

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $131,208.09                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    20                                      |
|  Orders filled today (ledger)  20                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             12                                      |
|  Broker option positions       2                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=505  buckets=49  win=35%                             |
|  Returns   avg=+8.6%  med=-31.5%  p10=-77.0%  p90=+94.2%               |
|  Realized  $+4,015.77                                                  |
|  Raw incl dropped  trades=619  real=$+2,517.58                         |
|  Today     trades=8  avg=+81.0%  med=+81.9%  real=$+408.00             |
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
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b83  S173 CRM260724C00187500 x1 take_profit (+53.2%)                  |
|  b2   S173 CRM260724C00185000 x1 take_profit (+106.8%                  |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (2)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  CRM260724C00185000            7   +106.8%   $   +473.67               |
|  CRM260724C00187500            4    +53.2%   $   +132.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=4.4s reconcile=1.92s cancel=0.23s manage=1.69s
STATUS: options_morning_bot run complete (PAPER) elapsed=4.4s. run=#4441 https://github.com/28twagg-ops/TradingBot/actions/runs/29760921990
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.csv
Summary: 7 buckets closed trades, $+408.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 3.5% (22/619)
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
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |    12 | INFO |
| Total closed lots           |   272 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
```

---

## Run 20260720T165038Z

- UTC timestamp: `20260720T165038Z`
- GitHub run: [#4442](https://github.com/28twagg-ops/TradingBot/actions/runs/29761263864)
- Run id: `29761263864`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`4s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T12:50:40.751318-04:00","date":"2026-07-20","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":3.0,"phases_s":{"reconcile":1.96,"cancel":0.08,"manage":0.62},"signals":0,"placed":0,"equity":131315.93,"open_positions":2,"pending_orders":0,"open_lots":10,"submitted_today":20,"filled_today":20,"unattributed_contracts":0,"top_signals":[],"github_run":"4442","github_run_id":"29761263864","status":"ok"}
```

### Live bot full output

```text
16:50:39  INFO      Mode: exits
16:50:39  INFO        Daily log -> logs/daily/2026-07-20.md
16:50:39  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (7 ledger rows)
16:50:39  INFO        place_all_stops: checking 1 positions...
16:50:39  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
16:50:39  INFO        [positions] 1/1 (1 valid)
16:50:39  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:50 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.17|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  COP  P&L +1.4%  $+1.23                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_morning_bot (PAPER) 2026-07-20T12:50:40.751318-04:00 ===

[Run context]
Paper auth OK — equity $131315.93, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-20 12:50:43,335 INFO   EXIT [b43|c043_s173_w4_1120_1135_r3|S173] take_profit (+50.0%) SELL 1 CRM260724C00187500 @<= 0.94
2026-07-20 12:50:43,551 INFO   EXIT [b22|c022_s173_w3_1045_1120_r2|S173] take_profit (+100.5%) SELL 1 CRM260724C00185000 @<= 1.28

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $131,315.93                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    20                                      |
|  Orders filled today (ledger)  20                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             10                                      |
|  Broker option positions       2                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=507  buckets=49  win=36%                             |
|  Returns   avg=+8.9%  med=-31.5%  p10=-77.0%  p90=+94.2%               |
|  Realized  $+4,110.77                                                  |
|  Raw incl dropped  trades=621  real=$+2,612.58                         |
|  Today     trades=10  avg=+79.0%  med=+81.9%  real=$+503.00            |
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
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b43  S173 CRM260724C00187500 x1 take_profit (+50.0%)                  |
|  b22  S173 CRM260724C00185000 x1 take_profit (+100.5%                  |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (2)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  CRM260724C00185000            6   +100.5%   $   +382.00               |
|  CRM260724C00187500            4    +50.0%   $   +124.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=3.0s reconcile=1.96s cancel=0.08s manage=0.62s
STATUS: options_morning_bot run complete (PAPER) elapsed=3.0s. run=#4442 https://github.com/28twagg-ops/TradingBot/actions/runs/29761263864
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.csv
Summary: 8 buckets closed trades, $+503.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 3.5% (22/621)
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
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |    10 | INFO |
| Total closed lots           |   273 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
```

---

## Run 20260720T165537Z

- UTC timestamp: `20260720T165537Z`
- GitHub run: [#4443](https://github.com/28twagg-ops/TradingBot/actions/runs/29761608317)
- Run id: `29761608317`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`4s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T12:55:39.822781-04:00","date":"2026-07-20","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":2.7,"phases_s":{"reconcile":1.66,"cancel":0.13,"manage":0.47},"signals":0,"placed":0,"equity":131220.91,"open_positions":2,"pending_orders":0,"open_lots":9,"submitted_today":20,"filled_today":20,"unattributed_contracts":0,"top_signals":[],"github_run":"4443","github_run_id":"29761608317","status":"ok"}
```

### Live bot full output

```text
16:55:38  INFO      Mode: exits
16:55:38  INFO        Daily log -> logs/daily/2026-07-20.md
16:55:38  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (7 ledger rows)
16:55:38  INFO        place_all_stops: checking 1 positions...
16:55:38  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
16:55:38  INFO        [positions] 1/1 (1 valid)
16:55:39  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:55 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.34|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  COP  P&L +1.6%  $+1.40                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_morning_bot (PAPER) 2026-07-20T12:55:39.822781-04:00 ===

[Run context]
Paper auth OK — equity $131220.91, account PA36KS87UPRS

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
|  Equity                        $131,220.91                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    20                                      |
|  Orders filled today (ledger)  20                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             9                                       |
|  Broker option positions       2                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=508  buckets=49  win=36%                             |
|  Returns   avg=+8.9%  med=-31.5%  p10=-77.0%  p90=+94.2%               |
|  Realized  $+4,142.77                                                  |
|  Raw incl dropped  trades=622  real=$+2,644.58                         |
|  Today     trades=11  avg=+76.5%  med=+81.4%  real=$+535.00            |
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
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b22  S173 CRM260724C00185000 x1 take_profit (+100.5%                  |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (2)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  CRM260724C00185000            6    +97.4%   $   +370.00               |
|  CRM260724C00187500            3    +46.8%   $    +87.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=2.7s reconcile=1.66s cancel=0.13s manage=0.47s
STATUS: options_morning_bot run complete (PAPER) elapsed=2.7s. run=#4443 https://github.com/28twagg-ops/TradingBot/actions/runs/29761608317
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.csv
Summary: 9 buckets closed trades, $+535.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 3.5% (22/622)
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
| State/ledger mismatches     |     9 | WARN | <<<
| Total open lots             |     9 | INFO |
| Total closed lots           |   274 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
```

---

## Run 20260720T170037Z

- UTC timestamp: `20260720T170037Z`
- GitHub run: [#4444](https://github.com/28twagg-ops/TradingBot/actions/runs/29761952423)
- Run id: `29761952423`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`4s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T13:00:39.964531-04:00","date":"2026-07-20","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":2.6,"phases_s":{"reconcile":1.54,"cancel":0.03,"manage":0.74},"signals":0,"placed":0,"equity":131393.91,"open_positions":2,"pending_orders":0,"open_lots":9,"submitted_today":20,"filled_today":20,"unattributed_contracts":0,"top_signals":[],"github_run":"4444","github_run_id":"29761952423","status":"ok"}
```

### Live bot full output

```text
17:00:38  INFO      Mode: exits
17:00:39  INFO        Daily log -> logs/daily/2026-07-20.md
17:00:39  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (7 ledger rows)
17:00:39  INFO        place_all_stops: checking 1 positions...
17:00:39  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
17:00:39  INFO        [positions] 1/1 (1 valid)
17:00:39  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:00 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.25|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  COP  P&L +1.5%  $+1.31                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_morning_bot (PAPER) 2026-07-20T13:00:39.964531-04:00 ===

[Run context]
Paper auth OK — equity $131393.91, account PA36KS87UPRS

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
|  Equity                        $131,393.91                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    20                                      |
|  Orders filled today (ledger)  20                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             9                                       |
|  Broker option positions       2                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=508  buckets=49  win=36%                             |
|  Returns   avg=+8.9%  med=-31.5%  p10=-77.0%  p90=+94.2%               |
|  Realized  $+4,142.77                                                  |
|  Raw incl dropped  trades=622  real=$+2,644.58                         |
|  Today     trades=11  avg=+76.5%  med=+81.4%  real=$+535.00            |
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
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b22  S173 CRM260724C00185000 x1 take_profit (+100.5%                  |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (2)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  CRM260724C00185000            6    +94.2%   $   +358.00               |
|  CRM260724C00187500            3    +45.2%   $    +84.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=2.6s reconcile=1.54s cancel=0.03s manage=0.74s
STATUS: options_morning_bot run complete (PAPER) elapsed=2.6s. run=#4444 https://github.com/28twagg-ops/TradingBot/actions/runs/29761952423
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.csv
Summary: 9 buckets closed trades, $+535.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 3.5% (22/622)
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
| State/ledger mismatches     |     9 | WARN | <<<
| Total open lots             |     9 | INFO |
| Total closed lots           |   274 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
```

---

## Run 20260720T170535Z

- UTC timestamp: `20260720T170535Z`
- GitHub run: [#4445](https://github.com/28twagg-ops/TradingBot/actions/runs/29762296011)
- Run id: `29762296011`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`3s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T13:05:38.053510-04:00","date":"2026-07-20","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":2.0,"phases_s":{"reconcile":1.49,"cancel":0.02,"manage":0.24},"signals":0,"placed":0,"equity":131151.91,"open_positions":2,"pending_orders":0,"open_lots":9,"submitted_today":20,"filled_today":20,"unattributed_contracts":0,"top_signals":[],"github_run":"4445","github_run_id":"29762296011","status":"ok"}
```

### Live bot full output

```text
17:05:36  INFO      Mode: exits
17:05:37  INFO        Daily log -> logs/daily/2026-07-20.md
17:05:37  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (7 ledger rows)
17:05:37  INFO        place_all_stops: checking 1 positions...
17:05:37  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
17:05:37  INFO        [positions] 1/1 (1 valid)
17:05:37  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:05 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.24|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  COP  P&L +1.5%  $+1.30                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_morning_bot (PAPER) 2026-07-20T13:05:38.053510-04:00 ===

[Run context]
Paper auth OK — equity $131187.91, account PA36KS87UPRS

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
|  Equity                        $131,151.91                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    20                                      |
|  Orders filled today (ledger)  20                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             9                                       |
|  Broker option positions       2                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=508  buckets=49  win=36%                             |
|  Returns   avg=+8.9%  med=-31.5%  p10=-77.0%  p90=+94.2%               |
|  Realized  $+4,142.77                                                  |
|  Raw incl dropped  trades=622  real=$+2,644.58                         |
|  Today     trades=11  avg=+76.5%  med=+81.4%  real=$+535.00            |
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
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b22  S173 CRM260724C00185000 x1 take_profit (+100.5%                  |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (2)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  CRM260724C00185000            6    +98.9%   $   +376.00               |
|  CRM260724C00187500            3    +45.2%   $    +84.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=2.0s reconcile=1.49s cancel=0.02s manage=0.24s
STATUS: options_morning_bot run complete (PAPER) elapsed=2.0s. run=#4445 https://github.com/28twagg-ops/TradingBot/actions/runs/29762296011
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.csv
Summary: 9 buckets closed trades, $+535.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 3.5% (22/622)
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
| State/ledger mismatches     |     9 | WARN | <<<
| Total open lots             |     9 | INFO |
| Total closed lots           |   274 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
```

---

## Run 20260720T171034Z

- UTC timestamp: `20260720T171034Z`
- GitHub run: [#4446](https://github.com/28twagg-ops/TradingBot/actions/runs/29762617335)
- Run id: `29762617335`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`4s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T13:10:36.607854-04:00","date":"2026-07-20","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":2.4,"phases_s":{"reconcile":1.83,"cancel":0.04,"manage":0.26},"signals":0,"placed":0,"equity":131132.87,"open_positions":2,"pending_orders":0,"open_lots":9,"submitted_today":20,"filled_today":20,"unattributed_contracts":0,"top_signals":[],"github_run":"4446","github_run_id":"29762617335","status":"ok"}
```

### Live bot full output

```text
17:10:35  INFO      Mode: exits
17:10:35  INFO        Daily log -> logs/daily/2026-07-20.md
17:10:35  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (7 ledger rows)
17:10:35  INFO        place_all_stops: checking 1 positions...
17:10:35  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
17:10:35  INFO        [positions] 1/1 (1 valid)
17:10:35  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.26|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  COP  P&L +1.5%  $+1.32                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_morning_bot (PAPER) 2026-07-20T13:10:36.607854-04:00 ===

[Run context]
Paper auth OK — equity $131132.87, account PA36KS87UPRS

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
|  Equity                        $131,132.87                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    20                                      |
|  Orders filled today (ledger)  20                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             9                                       |
|  Broker option positions       2                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=508  buckets=49  win=36%                             |
|  Returns   avg=+8.9%  med=-31.5%  p10=-77.0%  p90=+94.2%               |
|  Realized  $+4,142.77                                                  |
|  Raw incl dropped  trades=622  real=$+2,644.58                         |
|  Today     trades=11  avg=+76.5%  med=+81.4%  real=$+535.00            |
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
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b22  S173 CRM260724C00185000 x1 take_profit (+100.5%                  |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (2)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  CRM260724C00185000            6    +92.6%   $   +352.00               |
|  CRM260724C00187500            3    +46.8%   $    +87.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=2.4s reconcile=1.83s cancel=0.04s manage=0.26s
STATUS: options_morning_bot run complete (PAPER) elapsed=2.4s. run=#4446 https://github.com/28twagg-ops/TradingBot/actions/runs/29762617335
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.csv
Summary: 9 buckets closed trades, $+535.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 3.5% (22/622)
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
| State/ledger mismatches     |     9 | WARN | <<<
| Total open lots             |     9 | INFO |
| Total closed lots           |   274 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
```

---

## Run 20260720T171537Z

- UTC timestamp: `20260720T171537Z`
- GitHub run: [#4447](https://github.com/28twagg-ops/TradingBot/actions/runs/29762947216)
- Run id: `29762947216`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`4s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T13:15:39.852746-04:00","date":"2026-07-20","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":2.7,"phases_s":{"reconcile":1.32,"cancel":0.09,"manage":0.79},"signals":0,"placed":0,"equity":130933.89,"open_positions":2,"pending_orders":0,"open_lots":8,"submitted_today":20,"filled_today":20,"unattributed_contracts":0,"top_signals":[],"github_run":"4447","github_run_id":"29762947216","status":"ok"}
```

### Live bot full output

```text
17:15:38  INFO      Mode: exits
17:15:38  INFO        Daily log -> logs/daily/2026-07-20.md
17:15:38  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (7 ledger rows)
17:15:38  INFO        place_all_stops: checking 1 positions...
17:15:38  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
17:15:39  INFO        [positions] 1/1 (1 valid)
17:15:39  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:15 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.19|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  COP  P&L +1.4%  $+1.25                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_morning_bot (PAPER) 2026-07-20T13:15:39.852746-04:00 ===

[Run context]
Paper auth OK — equity $130933.89, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-20 13:15:42,090 INFO   EXIT [b23|c023_s173_w4_1120_1135_r2|S173] take_profit (+54.8%) SELL 1 CRM260724C00187500 @<= 0.93
2026-07-20 13:15:42,378 INFO   EXIT [b80|c080_s173_w1_0928_1005_r5|S173] take_profit (+105.3%) SELL 1 CRM260724C00185000 @<= 1.31

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $130,933.89                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    20                                      |
|  Orders filled today (ledger)  20                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             8                                       |
|  Broker option positions       2                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=509  buckets=49  win=36%                             |
|  Returns   avg=+9.1%  med=-31.5%  p10=-77.0%  p90=+94.1%               |
|  Realized  $+4,200.77                                                  |
|  Raw incl dropped  trades=623  real=$+2,702.58                         |
|  Today     trades=12  avg=+77.0%  med=+81.9%  real=$+593.00            |
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
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b23  S173 CRM260724C00187500 x1 take_profit (+54.8%)                  |
|  b80  S173 CRM260724C00185000 x1 take_profit (+105.3%                  |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (2)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  CRM260724C00185000            5   +105.3%   $   +333.33               |
|  CRM260724C00187500            2    +54.8%   $    +68.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=2.7s reconcile=1.32s cancel=0.09s manage=0.79s
STATUS: options_morning_bot run complete (PAPER) elapsed=2.7s. run=#4447 https://github.com/28twagg-ops/TradingBot/actions/runs/29762947216
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.csv
Summary: 10 buckets closed trades, $+593.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 3.5% (22/623)
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
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |     8 | INFO |
| Total closed lots           |   274 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
```

---

## Run 20260720T172037Z

- UTC timestamp: `20260720T172037Z`
- GitHub run: [#4448](https://github.com/28twagg-ops/TradingBot/actions/runs/29763260215)
- Run id: `29763260215`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`5s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T13:20:40.224516-04:00","date":"2026-07-20","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":4.0,"phases_s":{"reconcile":1.81,"cancel":0.21,"manage":1.4},"signals":0,"placed":0,"equity":131360.81,"open_positions":2,"pending_orders":0,"open_lots":6,"submitted_today":20,"filled_today":20,"unattributed_contracts":0,"top_signals":[],"github_run":"4448","github_run_id":"29763260215","status":"ok"}
```

### Live bot full output

```text
17:20:38  INFO      Mode: exits
17:20:38  INFO        Daily log -> logs/daily/2026-07-20.md
17:20:38  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (7 ledger rows)
17:20:38  INFO        place_all_stops: checking 1 positions...
17:20:38  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
17:20:39  INFO        [positions] 1/1 (1 valid)
17:20:39  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.19|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  COP  P&L +1.4%  $+1.25                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_morning_bot (PAPER) 2026-07-20T13:20:40.224516-04:00 ===

[Run context]
Paper auth OK — equity $131360.81, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-20 13:20:43,528 INFO   EXIT [b43|c043_s173_w4_1120_1135_r3|S173] take_profit (+53.2%) SELL 1 CRM260724C00187500 @<= 0.92
2026-07-20 13:20:43,947 INFO   EXIT [b41|c041_s173_w2_1005_1045_r3|S173] take_profit (+106.8%) SELL 1 CRM260724C00185000 @<= 1.32

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $131,360.81                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    20                                      |
|  Orders filled today (ledger)  20                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             6                                       |
|  Broker option positions       2                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=511  buckets=49  win=36%                             |
|  Returns   avg=+9.4%  med=-31.5%  p10=-77.0%  p90=+94.2%               |
|  Realized  $+4,302.77                                                  |
|  Raw incl dropped  trades=625  real=$+2,804.58                         |
|  Today     trades=14  avg=+77.6%  med=+81.9%  real=$+695.00            |
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
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b43  S173 CRM260724C00187500 x1 take_profit (+53.2%)                  |
|  b41  S173 CRM260724C00185000 x1 take_profit (+106.8%                  |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (2)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  CRM260724C00185000            4   +106.8%   $   +270.67               |
|  CRM260724C00187500            1    +53.2%   $    +33.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=4.0s reconcile=1.81s cancel=0.21s manage=1.4s
STATUS: options_morning_bot run complete (PAPER) elapsed=4.0s. run=#4448 https://github.com/28twagg-ops/TradingBot/actions/runs/29763260215
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.csv
Summary: 11 buckets closed trades, $+695.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 3.5% (22/625)
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
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |     6 | INFO |
| Total closed lots           |   274 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
```

---

## Run 20260720T172535Z

- UTC timestamp: `20260720T172535Z`
- GitHub run: [#4449](https://github.com/28twagg-ops/TradingBot/actions/runs/29763589768)
- Run id: `29763589768`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`3s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T13:25:37.942005-04:00","date":"2026-07-20","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":2.0,"phases_s":{"reconcile":1.46,"cancel":0.02,"manage":0.17},"signals":0,"placed":0,"equity":131521.83,"open_positions":2,"pending_orders":0,"open_lots":5,"submitted_today":20,"filled_today":20,"unattributed_contracts":0,"top_signals":[],"github_run":"4449","github_run_id":"29763589768","status":"ok"}
```

### Live bot full output

```text
17:25:36  INFO      Mode: exits
17:25:36  INFO        Daily log -> logs/daily/2026-07-20.md
17:25:36  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (7 ledger rows)
17:25:36  INFO        place_all_stops: checking 1 positions...
17:25:36  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
17:25:37  INFO        [positions] 1/1 (1 valid)
17:25:37  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:25 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.21|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  COP  P&L +1.4%  $+1.27                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_morning_bot (PAPER) 2026-07-20T13:25:37.942005-04:00 ===

[Run context]
Paper auth OK — equity $131521.83, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-20 13:25:39,692 INFO   EXIT [b3|c003_s173_w4_1120_1135_r1|S173] take_profit (+51.6%) SELL 1 CRM260724C00187500 @<= 0.91

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $131,521.83                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    20                                      |
|  Orders filled today (ledger)  20                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             5                                       |
|  Broker option positions       2                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=512  buckets=49  win=36%                             |
|  Returns   avg=+9.5%  med=-31.2%  p10=-76.7%  p90=+94.2%               |
|  Realized  $+4,335.77                                                  |
|  Raw incl dropped  trades=626  real=$+2,837.58                         |
|  Today     trades=15  avg=+76.0%  med=+81.4%  real=$+728.00            |
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
|  PENDING EXITS (2)                                                     |
+------------------------------------------------------------------------+
|  b41  S173 CRM260724C00185000 x1 take_profit (+106.8%                  |
|  b3   S173 CRM260724C00187500 x1 take_profit (+51.6%)                  |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (2)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  CRM260724C00185000            4   +105.3%   $   +266.67               |
|  CRM260724C00187500            1    +51.6%   $    +32.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=2.0s reconcile=1.46s cancel=0.02s manage=0.17s
STATUS: options_morning_bot run complete (PAPER) elapsed=2.0s. run=#4449 https://github.com/28twagg-ops/TradingBot/actions/runs/29763589768
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.csv
Summary: 11 buckets closed trades, $+728.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 3.5% (22/626)
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
| Total open lots             |     5 | INFO |
| Total closed lots           |   274 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
```

---

## Run 20260720T173036Z

- UTC timestamp: `20260720T173036Z`
- GitHub run: [#4450](https://github.com/28twagg-ops/TradingBot/actions/runs/29763907009)
- Run id: `29763907009`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`4s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T13:30:39.768997-04:00","date":"2026-07-20","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":3.3,"phases_s":{"reconcile":1.66,"cancel":0.18,"manage":0.9},"signals":0,"placed":0,"equity":131195.79,"open_positions":1,"pending_orders":0,"open_lots":3,"submitted_today":20,"filled_today":20,"unattributed_contracts":0,"top_signals":[],"github_run":"4450","github_run_id":"29763907009","status":"ok"}
```

### Live bot full output

```text
17:30:37  INFO      Mode: exits
17:30:38  INFO        Daily log -> logs/daily/2026-07-20.md
17:30:38  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (7 ledger rows)
17:30:38  INFO        place_all_stops: checking 1 positions...
17:30:38  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
17:30:38  INFO        [positions] 1/1 (1 valid)
17:30:38  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:30 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.23|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  COP  P&L +1.4%  $+1.28                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_morning_bot (PAPER) 2026-07-20T13:30:39.768997-04:00 ===

[Run context]
Paper auth OK — equity $131195.79, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-20 13:30:42,799 INFO   EXIT [b21|c021_s173_w2_1005_1045_r2|S173] take_profit (+114.7%) SELL 1 CRM260724C00185000 @<= 1.33

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $131,195.79                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    20                                      |
|  Orders filled today (ledger)  20                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             3                                       |
|  Broker option positions       1                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=513  buckets=49  win=36%                             |
|  Returns   avg=+9.5%  med=-30.9%  p10=-76.4%  p90=+94.2%               |
|  Realized  $+4,367.77                                                  |
|  Raw incl dropped  trades=627  real=$+2,869.58                         |
|  Today     trades=16  avg=+74.5%  med=+73.3%  real=$+760.00            |
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
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b21  S173 CRM260724C00185000 x1 take_profit (+114.7%                  |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (1)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  CRM260724C00185000            2   +114.7%   $   +145.33               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=3.3s reconcile=1.66s cancel=0.18s manage=0.9s
STATUS: options_morning_bot run complete (PAPER) elapsed=3.3s. run=#4450 https://github.com/28twagg-ops/TradingBot/actions/runs/29763907009
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.csv
Summary: 12 buckets closed trades, $+760.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 3.5% (22/627)
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
| Total open lots             |     3 | INFO |
| Total closed lots           |   274 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
```

---

## Run 20260720T173829Z

- UTC timestamp: `20260720T173829Z`
- GitHub run: [#4451](https://github.com/28twagg-ops/TradingBot/actions/runs/29764233863)
- Run id: `29764233863`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`4s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T13:38:32.248252-04:00","date":"2026-07-20","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":2.3,"phases_s":{"reconcile":1.55,"cancel":0.07,"manage":0.31},"signals":0,"placed":0,"equity":131231.77,"open_positions":1,"pending_orders":0,"open_lots":2,"submitted_today":20,"filled_today":20,"unattributed_contracts":0,"top_signals":[],"github_run":"4451","github_run_id":"29764233863","status":"ok"}
```

### Live bot full output

```text
17:38:30  INFO      Mode: exits
17:38:31  INFO        Daily log -> logs/daily/2026-07-20.md
17:38:31  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (7 ledger rows)
17:38:31  INFO        place_all_stops: checking 1 positions...
17:38:31  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
17:38:31  INFO        [positions] 1/1 (1 valid)
17:38:31  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:38 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.25|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  COP  P&L +1.5%  $+1.31                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_morning_bot (PAPER) 2026-07-20T13:38:32.248252-04:00 ===

[Run context]
Paper auth OK — equity $131231.77, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-20 13:38:34,308 INFO   EXIT [b20|c020_s173_w1_0928_1005_r2|S173] take_profit (+113.2%) SELL 1 CRM260724C00185000 @<= 1.32

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $131,231.77                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    20                                      |
|  Orders filled today (ledger)  20                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             2                                       |
|  Broker option positions       1                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=514  buckets=49  win=37%                             |
|  Returns   avg=+9.8%  med=-30.4%  p10=-76.1%  p90=+95.5%               |
|  Realized  $+4,446.77                                                  |
|  Raw incl dropped  trades=628  real=$+2,948.58                         |
|  Today     trades=17  avg=+78.3%  med=+81.4%  real=$+839.00            |
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
|  Low  b21  c021_s173_w2_1005_ 23   4% -55.2 -72.1 -98.5 $   -863       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b20  S173 CRM260724C00185000 x1 take_profit (+113.2%                  |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (1)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  CRM260724C00185000            2   +113.2%   $   +143.33               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=2.3s reconcile=1.55s cancel=0.07s manage=0.31s
STATUS: options_morning_bot run complete (PAPER) elapsed=2.3s. run=#4451 https://github.com/28twagg-ops/TradingBot/actions/runs/29764233863
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.csv
Summary: 13 buckets closed trades, $+839.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 3.5% (22/628)
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
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |     2 | INFO |
| Total closed lots           |   274 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
```

---

## Run 20260720T174045Z

- UTC timestamp: `20260720T174045Z`
- GitHub run: [#4452](https://github.com/28twagg-ops/TradingBot/actions/runs/29764543581)
- Run id: `29764543581`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`5s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T13:40:48.701876-04:00","date":"2026-07-20","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":3.8,"phases_s":{"reconcile":2.35,"cancel":0.09,"manage":0.48},"signals":0,"placed":0,"equity":131131.75,"open_positions":1,"pending_orders":0,"open_lots":1,"submitted_today":20,"filled_today":20,"unattributed_contracts":0,"top_signals":[],"github_run":"4452","github_run_id":"29764543581","status":"ok"}
```

### Live bot full output

```text
17:40:47  INFO      Mode: exits
17:40:47  INFO        Daily log -> logs/daily/2026-07-20.md
17:40:47  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (7 ledger rows)
17:40:47  INFO        place_all_stops: checking 1 positions...
17:40:47  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
17:40:47  INFO        [positions] 1/1 (1 valid)
17:40:48  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:40 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.22|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  COP  P&L +1.4%  $+1.28                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_morning_bot (PAPER) 2026-07-20T13:40:48.701876-04:00 ===

[Run context]
Paper auth OK — equity $131131.75, account PA36KS87UPRS

[Setup]
Active buckets: 100 | Strategies: S173, S165, S166, S163
Dropped (no new entries; ex-reflected P&L): S174
2026-07-20 13:40:52,372 INFO   EXIT [b20|c020_s173_w1_0928_1005_r2|S173] take_profit (+110.0%) SELL 1 CRM260724C00185000 @<= 1.30

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $131,131.75                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    20                                      |
|  Orders filled today (ledger)  20                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             1                                       |
|  Broker option positions       1                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=515  buckets=49  win=37%                             |
|  Returns   avg=+10.0%  med=-30.0%  p10=-75.8%  p90=+96.4%              |
|  Realized  $+4,518.77                                                  |
|  Raw incl dropped  trades=629  real=$+3,020.58                         |
|  Today     trades=18  avg=+80.3%  med=+81.9%  real=$+911.00            |
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
|  Low  b21  c021_s173_w2_1005_ 23   4% -55.2 -72.1 -98.5 $   -863       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (1)                                                     |
+------------------------------------------------------------------------+
|  b20  S173 CRM260724C00185000 x1 take_profit (+110.0%                  |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (1)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  CRM260724C00185000            1   +110.0%   $    +69.67               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=3.8s reconcile=2.35s cancel=0.09s manage=0.48s
STATUS: options_morning_bot run complete (PAPER) elapsed=3.8s. run=#4452 https://github.com/28twagg-ops/TradingBot/actions/runs/29764543581
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.csv
Summary: 14 buckets closed trades, $+911.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 3.5% (22/629)
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
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |     1 | INFO |
| Total closed lots           |   274 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
```

---

## Run 20260720T174537Z

- UTC timestamp: `20260720T174537Z`
- GitHub run: [#4453](https://github.com/28twagg-ops/TradingBot/actions/runs/29764856978)
- Run id: `29764856978`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`4s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T13:45:40.257021-04:00","date":"2026-07-20","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":2.5,"phases_s":{"reconcile":1.76,"cancel":0.18,"manage":0.12},"signals":0,"placed":0,"equity":131079.73,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":20,"filled_today":20,"unattributed_contracts":0,"top_signals":[],"github_run":"4453","github_run_id":"29764856978","status":"ok"}
```

### Live bot full output

```text
17:45:38  INFO      Mode: exits
17:45:38  INFO        Daily log -> logs/daily/2026-07-20.md
17:45:38  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (7 ledger rows)
17:45:39  INFO        place_all_stops: checking 1 positions...
17:45:39  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
17:45:39  INFO        [positions] 1/1 (1 valid)
17:45:39  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:45 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.20|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  COP  P&L +1.4%  $+1.26                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_morning_bot (PAPER) 2026-07-20T13:45:40.257021-04:00 ===

[Run context]
Paper auth OK — equity $131079.73, account PA36KS87UPRS

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
|  Equity                        $131,079.73                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    20                                      |
|  Orders filled today (ledger)  20                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=516  buckets=49  win=37%                             |
|  Returns   avg=+10.2%  med=-28.8%  p10=-75.5%  p90=+97.5%              |
|  Realized  $+4,588.77                                                  |
|  Raw incl dropped  trades=630  real=$+3,090.58                         |
|  Today     trades=19  avg=+81.9%  med=+82.5%  real=$+981.00            |
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
|  Low  b21  c021_s173_w2_1005_ 23   4% -55.2 -72.1 -98.5 $   -863       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=2.5s reconcile=1.76s cancel=0.18s manage=0.12s
STATUS: options_morning_bot run complete (PAPER) elapsed=2.5s. run=#4453 https://github.com/28twagg-ops/TradingBot/actions/runs/29764856978
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.csv
Summary: 14 buckets closed trades, $+981.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 3.5% (22/630)
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
| Total closed lots           |   274 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
```

---

## Run 20260720T175039Z

- UTC timestamp: `20260720T175039Z`
- GitHub run: [#4454](https://github.com/28twagg-ops/TradingBot/actions/runs/29765170431)
- Run id: `29765170431`
- Live bot: exit=`0`, duration=`4s`
- Options bot: exit=`0`, duration=`5s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T13:50:44.598144-04:00","date":"2026-07-20","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":3.1,"phases_s":{"reconcile":1.8,"cancel":0.23,"manage":0.16},"signals":0,"placed":0,"equity":131249.77,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":20,"filled_today":20,"unattributed_contracts":0,"top_signals":[],"github_run":"4454","github_run_id":"29765170431","status":"ok"}
```

### Live bot full output

```text
17:50:41  INFO      Mode: exits
17:50:43  INFO        Daily log -> logs/daily/2026-07-20.md
17:50:43  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (7 ledger rows)
17:50:43  INFO        place_all_stops: checking 1 positions...
17:50:43  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
17:50:43  INFO        [positions] 1/1 (1 valid)
17:50:43  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:50 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.21|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  COP  P&L +1.4%  $+1.27                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_morning_bot (PAPER) 2026-07-20T13:50:44.598144-04:00 ===

[Run context]
Paper auth OK — equity $131249.77, account PA36KS87UPRS

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
|  Equity                        $131,249.77                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    20                                      |
|  Orders filled today (ledger)  20                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=516  buckets=49  win=37%                             |
|  Returns   avg=+10.2%  med=-28.8%  p10=-75.5%  p90=+97.5%              |
|  Realized  $+4,588.77                                                  |
|  Raw incl dropped  trades=630  real=$+3,090.58                         |
|  Today     trades=19  avg=+81.9%  med=+82.5%  real=$+981.00            |
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
|  Low  b21  c021_s173_w2_1005_ 23   4% -55.2 -72.1 -98.5 $   -863       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=3.1s reconcile=1.8s cancel=0.23s manage=0.16s
STATUS: options_morning_bot run complete (PAPER) elapsed=3.1s. run=#4454 https://github.com/28twagg-ops/TradingBot/actions/runs/29765170431
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.csv
Summary: 14 buckets closed trades, $+981.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 3.5% (22/630)
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
| Total closed lots           |   274 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
```

---

## Run 20260720T175541Z

- UTC timestamp: `20260720T175541Z`
- GitHub run: [#4455](https://github.com/28twagg-ops/TradingBot/actions/runs/29765505182)
- Run id: `29765505182`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`4s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T13:55:44.972741-04:00","date":"2026-07-20","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":2.7,"phases_s":{"reconcile":1.81,"cancel":0.22,"manage":0.14},"signals":0,"placed":0,"equity":131433.73,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":20,"filled_today":20,"unattributed_contracts":0,"top_signals":[],"github_run":"4455","github_run_id":"29765505182","status":"ok"}
```

### Live bot full output

```text
17:55:42  INFO      Mode: exits
17:55:43  INFO        Daily log -> logs/daily/2026-07-20.md
17:55:43  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (7 ledger rows)
17:55:43  INFO        place_all_stops: checking 1 positions...
17:55:43  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
17:55:43  INFO        [positions] 1/1 (1 valid)
17:55:44  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:55 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.13|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  COP  P&L +1.4%  $+1.20                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_morning_bot (PAPER) 2026-07-20T13:55:44.972741-04:00 ===

[Run context]
Paper auth OK — equity $131433.73, account PA36KS87UPRS

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
|  Equity                        $131,433.73                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    20                                      |
|  Orders filled today (ledger)  20                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=516  buckets=49  win=37%                             |
|  Returns   avg=+10.2%  med=-28.8%  p10=-75.5%  p90=+97.5%              |
|  Realized  $+4,588.77                                                  |
|  Raw incl dropped  trades=630  real=$+3,090.58                         |
|  Today     trades=19  avg=+81.9%  med=+82.5%  real=$+981.00            |
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
|  Low  b21  c021_s173_w2_1005_ 23   4% -55.2 -72.1 -98.5 $   -863       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=2.7s reconcile=1.81s cancel=0.22s manage=0.14s
STATUS: options_morning_bot run complete (PAPER) elapsed=2.7s. run=#4455 https://github.com/28twagg-ops/TradingBot/actions/runs/29765505182
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.csv
Summary: 14 buckets closed trades, $+981.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 3.5% (22/630)
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
| Total closed lots           |   274 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
```

---

## Run 20260720T180044Z

- UTC timestamp: `20260720T180044Z`
- GitHub run: [#4456](https://github.com/28twagg-ops/TradingBot/actions/runs/29765878810)
- Run id: `29765878810`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`4s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T14:00:47.623010-04:00","date":"2026-07-20","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":2.4,"phases_s":{"reconcile":1.5,"cancel":0.07,"manage":0.04},"signals":0,"placed":0,"equity":131490.53,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":20,"filled_today":20,"unattributed_contracts":0,"top_signals":[],"github_run":"4456","github_run_id":"29765878810","status":"ok"}
```

### Live bot full output

```text
18:00:45  INFO      Mode: exits
18:00:46  INFO        Daily log -> logs/daily/2026-07-20.md
18:00:46  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (7 ledger rows)
18:00:46  INFO        place_all_stops: checking 1 positions...
18:00:46  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
18:00:46  INFO        [positions] 1/1 (1 valid)
18:00:46  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:00 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.10|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  COP  P&L +1.3%  $+1.16                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_morning_bot (PAPER) 2026-07-20T14:00:47.623010-04:00 ===

[Run context]
Paper auth OK — equity $131490.53, account PA36KS87UPRS

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
|  Equity                        $131,490.53                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    20                                      |
|  Orders filled today (ledger)  20                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=516  buckets=49  win=37%                             |
|  Returns   avg=+10.2%  med=-28.8%  p10=-75.5%  p90=+97.5%              |
|  Realized  $+4,588.77                                                  |
|  Raw incl dropped  trades=630  real=$+3,090.58                         |
|  Today     trades=19  avg=+81.9%  med=+82.5%  real=$+981.00            |
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
|  Low  b21  c021_s173_w2_1005_ 23   4% -55.2 -72.1 -98.5 $   -863       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=2.4s reconcile=1.5s cancel=0.07s manage=0.04s
STATUS: options_morning_bot run complete (PAPER) elapsed=2.4s. run=#4456 https://github.com/28twagg-ops/TradingBot/actions/runs/29765878810
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.csv
Summary: 14 buckets closed trades, $+981.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 3.5% (22/630)
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
| Total closed lots           |   274 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
```

---

## Run 20260720T180534Z

- UTC timestamp: `20260720T180534Z`
- GitHub run: [#4457](https://github.com/28twagg-ops/TradingBot/actions/runs/29766233254)
- Run id: `29766233254`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`4s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T14:05:36.171979-04:00","date":"2026-07-20","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":2.2,"phases_s":{"reconcile":1.87,"cancel":0.02,"manage":0.01},"signals":0,"placed":0,"equity":131407.73,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":20,"filled_today":20,"unattributed_contracts":0,"top_signals":[],"github_run":"4457","github_run_id":"29766233254","status":"ok"}
```

### Live bot full output

```text
18:05:35  INFO      Mode: exits
18:05:35  INFO        Daily log -> logs/daily/2026-07-20.md
18:05:35  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (7 ledger rows)
18:05:35  INFO        place_all_stops: checking 1 positions...
18:05:35  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
18:05:35  INFO        [positions] 1/1 (1 valid)
18:05:35  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:05 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.09|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  COP  P&L +1.3%  $+1.15                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_morning_bot (PAPER) 2026-07-20T14:05:36.171979-04:00 ===

[Run context]
Paper auth OK — equity $131407.73, account PA36KS87UPRS

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
|  Equity                        $131,407.73                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    20                                      |
|  Orders filled today (ledger)  20                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=516  buckets=49  win=37%                             |
|  Returns   avg=+10.2%  med=-28.8%  p10=-75.5%  p90=+97.5%              |
|  Realized  $+4,588.77                                                  |
|  Raw incl dropped  trades=630  real=$+3,090.58                         |
|  Today     trades=19  avg=+81.9%  med=+82.5%  real=$+981.00            |
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
|  Low  b21  c021_s173_w2_1005_ 23   4% -55.2 -72.1 -98.5 $   -863       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=2.2s reconcile=1.87s cancel=0.02s manage=0.01s
STATUS: options_morning_bot run complete (PAPER) elapsed=2.2s. run=#4457 https://github.com/28twagg-ops/TradingBot/actions/runs/29766233254
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.csv
Summary: 14 buckets closed trades, $+981.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.csv
Summary: keep=0 watch=2 drop=3
Orphan rate: 3.5% (22/630)
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
| Total closed lots           |   274 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
```

---

## Run 20260720T181033Z

- UTC timestamp: `20260720T181033Z`
- GitHub run: [#4458](https://github.com/28twagg-ops/TradingBot/actions/runs/29766589868)
- Run id: `29766589868`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`6s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T14:10:37.912315-04:00","date":"2026-07-20","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":1.7,"phases_s":{"reconcile":1.29,"cancel":0.07,"manage":0.05},"signals":0,"placed":0,"equity":131469.73,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":20,"filled_today":20,"unattributed_contracts":0,"top_signals":[],"github_run":"4458","github_run_id":"29766589868","status":"ok"}
```

### Live bot full output

```text
18:10:35  INFO      Mode: exits
18:10:36  INFO        Daily log -> logs/daily/2026-07-20.md
18:10:36  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (7 ledger rows)
18:10:36  INFO        place_all_stops: checking 1 positions...
18:10:36  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
18:10:36  INFO        [positions] 1/1 (1 valid)
18:10:36  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $481.96|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  COP  P&L +1.2%  $+1.02                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=0 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=2
  zombies_flagged=0
options_reconcile: done
Layout: controlled:140:c000_s173_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:140:c000_s173_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      140
=== options_morning_bot (PAPER) 2026-07-20T14:10:37.912315-04:00 ===

[Run context]
Paper auth OK — equity $131469.73, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S173, S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $131,469.73                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    20                                      |
|  Orders filled today (ledger)  20                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=516  buckets=49  win=37%                             |
|  Returns   avg=+10.2%  med=-28.8%  p10=-75.5%  p90=+97.5%              |
|  Realized  $+4,588.77                                                  |
|  Raw incl dropped  trades=630  real=$+3,090.58                         |
|  Today     trades=19  avg=+81.9%  med=+82.5%  real=$+981.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b51  c051_s164_w4_1120_  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  c091_s167_w4_1120_  3  67% +142.7 +197.0 +247.0 $   +282         |
|  b31  c031_s173_w4_1120_  2 100% +145.5 +145.5 +175.8 $   +192         |
|  b28  c028_s173_w1_0928_ 17  76% +49.5 +80.0 +102.0 $   +448           |
|  b92  c092_s165_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s165_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s165_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 41 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s164_w2_1005_ 23   4% -55.2 -72.1 -98.5 $   -863       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=1.7s reconcile=1.29s cancel=0.07s manage=0.05s
STATUS: options_morning_bot run complete (PAPER) elapsed=1.7s. run=#4458 https://github.com/28twagg-ops/TradingBot/actions/runs/29766589868
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.csv
Summary: 14 buckets closed trades, $+981.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 3.5% (22/630)
# Options signal frequency

_Generated 2026-07-20T14:10:41.798394_

Headline counts are **unique (strategy, underlying, date)** from `ENTRY` lines in `logs/options_trial/runs/*.log`.
Raw log-line counts (multi-bucket duplicates) are shown below for debug.

### Unique underlying symbols per day (headline)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-08 |    0 |    0 |    3 |    0 |    0 |    0 |    2 |    1 |     6 |
| 2026-07-09 |    0 |    0 |    1 |    0 |    0 |    0 |    2 |    3 |     6 |
| 2026-07-10 |    0 |    0 |    1 |    0 |    0 |    0 |    1 |    1 |     3 |
| 2026-07-13 |    0 |    0 |    2 |    0 |    0 |    0 |    3 |    2 |     7 |
| 2026-07-14 |    0 |    0 |    3 |    0 |    0 |    0 |    2 |    0 |     5 |
| 2026-07-16 |    0 |    0 |    2 |    0 |    0 |    0 |    3 |    0 |     5 |
| 2026-07-17 |    0 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |     4 |
| 2026-07-20 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S164 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S165 | 14 | 7 | 2.0 | ~19 active signal-days |
| S166 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S167 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S168 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 0 | 0 |
| S164 | 0 | 0 |
| S165 | 1309 | 14 |
| S166 | 0 | 0 |
| S167 | 0 | 0 |
| S168 | 0 | 0 |
| S173 | 1636 | 17 |
| S174 | 843 | 7 |

### Raw log lines per day (debug / multi-bucket)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |    0 |   100 |
| 2026-07-08 |    0 |    0 |  100 |    0 |    0 |    0 |  100 |  100 |   300 |
| 2026-07-09 |    0 |    0 |   24 |    0 |    0 |    0 |  100 |   15 |   139 |
| 2026-07-10 |    0 |    0 |  242 |    0 |    0 |    0 |  230 |  202 |   674 |
| 2026-07-13 |    0 |    0 |  190 |    0 |    0 |    0 |  212 |  188 |   590 |
| 2026-07-14 |    0 |    0 |  194 |    0 |    0 |    0 |  185 |  106 |   485 |
| 2026-07-15 |    0 |    0 |  146 |    0 |    0 |    0 |  154 |   58 |   358 |
| 2026-07-16 |    0 |    0 |  179 |    0 |    0 |    0 |  205 |   58 |   442 |
| 2026-07-17 |    0 |    0 |  127 |    0 |    0 |    0 |  207 |   58 |   392 |
| 2026-07-20 |    0 |    0 |  107 |    0 |    0 |    0 |  143 |   58 |   308 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-07-20
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |    27 | WARN | <<<
| Missing exit records (post) |    27 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |   274 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=481.96 router=PENDING leaderboard_rows=8
```

---

## Run 20260720T181225Z

- UTC timestamp: `20260720T181225Z`
- GitHub run: [#4459](https://github.com/28twagg-ops/TradingBot/actions/runs/29766720302)
- Run id: `29766720302`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`7s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T14:12:29.258447-04:00","date":"2026-07-20","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":1.8,"phases_s":{"reconcile":1.5,"cancel":0.03,"manage":0.04},"signals":0,"placed":0,"equity":131445.73,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":20,"filled_today":20,"unattributed_contracts":0,"top_signals":[],"github_run":"4459","github_run_id":"29766720302","status":"ok"}
```

### Live bot full output

```text
18:12:27  INFO      Mode: exits
18:12:27  INFO        Daily log -> logs/daily/2026-07-20.md
18:12:27  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (7 ledger rows)
18:12:27  INFO        place_all_stops: checking 1 positions...
18:12:27  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
18:12:27  INFO        [positions] 1/1 (1 valid)
18:12:27  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:12 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.04|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  COP  P&L +1.2%  $+1.10                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=0 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=2
  zombies_flagged=0
options_reconcile: done
Layout: controlled:140:c000_s173_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:140:c000_s173_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      140
=== options_morning_bot (PAPER) 2026-07-20T14:12:29.258447-04:00 ===

[Run context]
Paper auth OK — equity $131445.73, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S173, S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $131,445.73                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    20                                      |
|  Orders filled today (ledger)  20                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=516  buckets=49  win=37%                             |
|  Returns   avg=+10.2%  med=-28.8%  p10=-75.5%  p90=+97.5%              |
|  Realized  $+4,588.77                                                  |
|  Raw incl dropped  trades=630  real=$+3,090.58                         |
|  Today     trades=19  avg=+81.9%  med=+82.5%  real=$+981.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b51  c051_s164_w4_1120_  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  c091_s167_w4_1120_  3  67% +142.7 +197.0 +247.0 $   +282         |
|  b31  c031_s173_w4_1120_  2 100% +145.5 +145.5 +175.8 $   +192         |
|  b28  c028_s173_w1_0928_ 17  76% +49.5 +80.0 +102.0 $   +448           |
|  b92  c092_s165_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s165_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s165_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 41 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s164_w2_1005_ 23   4% -55.2 -72.1 -98.5 $   -863       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=1.8s reconcile=1.5s cancel=0.03s manage=0.04s
STATUS: options_morning_bot run complete (PAPER) elapsed=1.8s. run=#4459 https://github.com/28twagg-ops/TradingBot/actions/runs/29766720302
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.csv
Summary: 14 buckets closed trades, $+981.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 3.5% (22/630)
# Options signal frequency

_Generated 2026-07-20T14:12:33.935163_

Headline counts are **unique (strategy, underlying, date)** from `ENTRY` lines in `logs/options_trial/runs/*.log`.
Raw log-line counts (multi-bucket duplicates) are shown below for debug.

### Unique underlying symbols per day (headline)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-08 |    0 |    0 |    3 |    0 |    0 |    0 |    2 |    1 |     6 |
| 2026-07-09 |    0 |    0 |    1 |    0 |    0 |    0 |    2 |    3 |     6 |
| 2026-07-10 |    0 |    0 |    1 |    0 |    0 |    0 |    1 |    1 |     3 |
| 2026-07-13 |    0 |    0 |    2 |    0 |    0 |    0 |    3 |    2 |     7 |
| 2026-07-14 |    0 |    0 |    3 |    0 |    0 |    0 |    2 |    0 |     5 |
| 2026-07-16 |    0 |    0 |    2 |    0 |    0 |    0 |    3 |    0 |     5 |
| 2026-07-17 |    0 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |     4 |
| 2026-07-20 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S164 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S165 | 14 | 7 | 2.0 | ~19 active signal-days |
| S166 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S167 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S168 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 0 | 0 |
| S164 | 0 | 0 |
| S165 | 1309 | 14 |
| S166 | 0 | 0 |
| S167 | 0 | 0 |
| S168 | 0 | 0 |
| S173 | 1636 | 17 |
| S174 | 843 | 7 |

### Raw log lines per day (debug / multi-bucket)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |    0 |   100 |
| 2026-07-08 |    0 |    0 |  100 |    0 |    0 |    0 |  100 |  100 |   300 |
| 2026-07-09 |    0 |    0 |   24 |    0 |    0 |    0 |  100 |   15 |   139 |
| 2026-07-10 |    0 |    0 |  242 |    0 |    0 |    0 |  230 |  202 |   674 |
| 2026-07-13 |    0 |    0 |  190 |    0 |    0 |    0 |  212 |  188 |   590 |
| 2026-07-14 |    0 |    0 |  194 |    0 |    0 |    0 |  185 |  106 |   485 |
| 2026-07-15 |    0 |    0 |  146 |    0 |    0 |    0 |  154 |   58 |   358 |
| 2026-07-16 |    0 |    0 |  179 |    0 |    0 |    0 |  205 |   58 |   442 |
| 2026-07-17 |    0 |    0 |  127 |    0 |    0 |    0 |  207 |   58 |   392 |
| 2026-07-20 |    0 |    0 |  107 |    0 |    0 |    0 |  143 |   58 |   308 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-07-20
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |    27 | WARN | <<<
| Missing exit records (post) |    27 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |   274 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=482.04 router=PENDING leaderboard_rows=8
```

---

## Run 20260720T181537Z

- UTC timestamp: `20260720T181537Z`
- GitHub run: [#4460](https://github.com/28twagg-ops/TradingBot/actions/runs/29766947614)
- Run id: `29766947614`
- Live bot: exit=`0`, duration=`4s`
- Options bot: exit=`0`, duration=`7s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T14:15:42.930547-04:00","date":"2026-07-20","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":2.9,"phases_s":{"reconcile":1.91,"cancel":0.24,"manage":0.16},"signals":0,"placed":0,"equity":131358.97,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":20,"filled_today":20,"unattributed_contracts":0,"top_signals":[],"github_run":"4460","github_run_id":"29766947614","status":"ok"}
```

### Live bot full output

```text
18:15:39  INFO      Mode: exits
18:15:40  INFO        Daily log -> logs/daily/2026-07-20.md
18:15:40  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (7 ledger rows)
18:15:40  INFO        place_all_stops: checking 1 positions...
18:15:40  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
18:15:40  INFO        [positions] 1/1 (1 valid)
18:15:40  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:15 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $481.99|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  COP  P&L +1.2%  $+1.05                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=0 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=2
  zombies_flagged=0
options_reconcile: done
Layout: controlled:140:c000_s173_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:140:c000_s173_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      140
=== options_morning_bot (PAPER) 2026-07-20T14:15:42.930547-04:00 ===

[Run context]
Paper auth OK — equity $131357.21, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S173, S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $131,358.97                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    20                                      |
|  Orders filled today (ledger)  20                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=516  buckets=49  win=37%                             |
|  Returns   avg=+10.2%  med=-28.8%  p10=-75.5%  p90=+97.5%              |
|  Realized  $+4,588.77                                                  |
|  Raw incl dropped  trades=630  real=$+3,090.58                         |
|  Today     trades=19  avg=+81.9%  med=+82.5%  real=$+981.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b51  c051_s164_w4_1120_  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  c091_s167_w4_1120_  3  67% +142.7 +197.0 +247.0 $   +282         |
|  b31  c031_s173_w4_1120_  2 100% +145.5 +145.5 +175.8 $   +192         |
|  b28  c028_s173_w1_0928_ 17  76% +49.5 +80.0 +102.0 $   +448           |
|  b92  c092_s165_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s165_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s165_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 41 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s164_w2_1005_ 23   4% -55.2 -72.1 -98.5 $   -863       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=2.9s reconcile=1.91s cancel=0.24s manage=0.16s
STATUS: options_morning_bot run complete (PAPER) elapsed=2.9s. run=#4460 https://github.com/28twagg-ops/TradingBot/actions/runs/29766947614
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.csv
Summary: 14 buckets closed trades, $+981.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 3.5% (22/630)
# Options signal frequency

_Generated 2026-07-20T14:15:48.721283_

Headline counts are **unique (strategy, underlying, date)** from `ENTRY` lines in `logs/options_trial/runs/*.log`.
Raw log-line counts (multi-bucket duplicates) are shown below for debug.

### Unique underlying symbols per day (headline)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-08 |    0 |    0 |    3 |    0 |    0 |    0 |    2 |    1 |     6 |
| 2026-07-09 |    0 |    0 |    1 |    0 |    0 |    0 |    2 |    3 |     6 |
| 2026-07-10 |    0 |    0 |    1 |    0 |    0 |    0 |    1 |    1 |     3 |
| 2026-07-13 |    0 |    0 |    2 |    0 |    0 |    0 |    3 |    2 |     7 |
| 2026-07-14 |    0 |    0 |    3 |    0 |    0 |    0 |    2 |    0 |     5 |
| 2026-07-16 |    0 |    0 |    2 |    0 |    0 |    0 |    3 |    0 |     5 |
| 2026-07-17 |    0 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |     4 |
| 2026-07-20 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S164 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S165 | 14 | 7 | 2.0 | ~19 active signal-days |
| S166 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S167 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S168 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 0 | 0 |
| S164 | 0 | 0 |
| S165 | 1309 | 14 |
| S166 | 0 | 0 |
| S167 | 0 | 0 |
| S168 | 0 | 0 |
| S173 | 1636 | 17 |
| S174 | 843 | 7 |

### Raw log lines per day (debug / multi-bucket)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |    0 |   100 |
| 2026-07-08 |    0 |    0 |  100 |    0 |    0 |    0 |  100 |  100 |   300 |
| 2026-07-09 |    0 |    0 |   24 |    0 |    0 |    0 |  100 |   15 |   139 |
| 2026-07-10 |    0 |    0 |  242 |    0 |    0 |    0 |  230 |  202 |   674 |
| 2026-07-13 |    0 |    0 |  190 |    0 |    0 |    0 |  212 |  188 |   590 |
| 2026-07-14 |    0 |    0 |  194 |    0 |    0 |    0 |  185 |  106 |   485 |
| 2026-07-15 |    0 |    0 |  146 |    0 |    0 |    0 |  154 |   58 |   358 |
| 2026-07-16 |    0 |    0 |  179 |    0 |    0 |    0 |  205 |   58 |   442 |
| 2026-07-17 |    0 |    0 |  127 |    0 |    0 |    0 |  207 |   58 |   392 |
| 2026-07-20 |    0 |    0 |  107 |    0 |    0 |    0 |  143 |   58 |   308 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-07-20
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |    27 | WARN | <<<
| Missing exit records (post) |    27 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |   274 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=481.99 router=PENDING leaderboard_rows=8
```

---

## Run 20260720T182034Z

- UTC timestamp: `20260720T182034Z`
- GitHub run: [#4461](https://github.com/28twagg-ops/TradingBot/actions/runs/29767303974)
- Run id: `29767303974`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`7s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T14:20:38.909186-04:00","date":"2026-07-20","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":2.2,"phases_s":{"reconcile":1.57,"cancel":0.07,"manage":0.04},"signals":0,"placed":0,"equity":131295.73,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":20,"filled_today":20,"unattributed_contracts":0,"top_signals":[],"github_run":"4461","github_run_id":"29767303974","status":"ok"}
```

### Live bot full output

```text
18:20:35  INFO      Mode: exits
18:20:36  INFO        Daily log -> logs/daily/2026-07-20.md
18:20:36  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (7 ledger rows)
18:20:36  INFO        place_all_stops: checking 1 positions...
18:20:36  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
18:20:36  INFO        [positions] 1/1 (1 valid)
18:20:37  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $481.99|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  COP  P&L +1.2%  $+1.05                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=0 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=2
  zombies_flagged=0
options_reconcile: done
Layout: controlled:140:c000_s173_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:140:c000_s173_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      140
=== options_morning_bot (PAPER) 2026-07-20T14:20:38.909186-04:00 ===

[Run context]
Paper auth OK — equity $131295.73, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S173, S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $131,295.73                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    20                                      |
|  Orders filled today (ledger)  20                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=516  buckets=49  win=37%                             |
|  Returns   avg=+10.2%  med=-28.8%  p10=-75.5%  p90=+97.5%              |
|  Realized  $+4,588.77                                                  |
|  Raw incl dropped  trades=630  real=$+3,090.58                         |
|  Today     trades=19  avg=+81.9%  med=+82.5%  real=$+981.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b51  c051_s164_w4_1120_  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  c091_s167_w4_1120_  3  67% +142.7 +197.0 +247.0 $   +282         |
|  b31  c031_s173_w4_1120_  2 100% +145.5 +145.5 +175.8 $   +192         |
|  b28  c028_s173_w1_0928_ 17  76% +49.5 +80.0 +102.0 $   +448           |
|  b92  c092_s165_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s165_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s165_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 41 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s164_w2_1005_ 23   4% -55.2 -72.1 -98.5 $   -863       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=2.2s reconcile=1.57s cancel=0.07s manage=0.04s
STATUS: options_morning_bot run complete (PAPER) elapsed=2.2s. run=#4461 https://github.com/28twagg-ops/TradingBot/actions/runs/29767303974
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.csv
Summary: 14 buckets closed trades, $+981.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 3.5% (22/630)
# Options signal frequency

_Generated 2026-07-20T14:20:44.026547_

Headline counts are **unique (strategy, underlying, date)** from `ENTRY` lines in `logs/options_trial/runs/*.log`.
Raw log-line counts (multi-bucket duplicates) are shown below for debug.

### Unique underlying symbols per day (headline)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-08 |    0 |    0 |    3 |    0 |    0 |    0 |    2 |    1 |     6 |
| 2026-07-09 |    0 |    0 |    1 |    0 |    0 |    0 |    2 |    3 |     6 |
| 2026-07-10 |    0 |    0 |    1 |    0 |    0 |    0 |    1 |    1 |     3 |
| 2026-07-13 |    0 |    0 |    2 |    0 |    0 |    0 |    3 |    2 |     7 |
| 2026-07-14 |    0 |    0 |    3 |    0 |    0 |    0 |    2 |    0 |     5 |
| 2026-07-16 |    0 |    0 |    2 |    0 |    0 |    0 |    3 |    0 |     5 |
| 2026-07-17 |    0 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |     4 |
| 2026-07-20 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S164 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S165 | 14 | 7 | 2.0 | ~19 active signal-days |
| S166 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S167 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S168 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 0 | 0 |
| S164 | 0 | 0 |
| S165 | 1309 | 14 |
| S166 | 0 | 0 |
| S167 | 0 | 0 |
| S168 | 0 | 0 |
| S173 | 1636 | 17 |
| S174 | 843 | 7 |

### Raw log lines per day (debug / multi-bucket)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |    0 |   100 |
| 2026-07-08 |    0 |    0 |  100 |    0 |    0 |    0 |  100 |  100 |   300 |
| 2026-07-09 |    0 |    0 |   24 |    0 |    0 |    0 |  100 |   15 |   139 |
| 2026-07-10 |    0 |    0 |  242 |    0 |    0 |    0 |  230 |  202 |   674 |
| 2026-07-13 |    0 |    0 |  190 |    0 |    0 |    0 |  212 |  188 |   590 |
| 2026-07-14 |    0 |    0 |  194 |    0 |    0 |    0 |  185 |  106 |   485 |
| 2026-07-15 |    0 |    0 |  146 |    0 |    0 |    0 |  154 |   58 |   358 |
| 2026-07-16 |    0 |    0 |  179 |    0 |    0 |    0 |  205 |   58 |   442 |
| 2026-07-17 |    0 |    0 |  127 |    0 |    0 |    0 |  207 |   58 |   392 |
| 2026-07-20 |    0 |    0 |  107 |    0 |    0 |    0 |  143 |   58 |   308 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-07-20
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |    27 | WARN | <<<
| Missing exit records (post) |    27 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |   274 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=481.99 router=PENDING leaderboard_rows=8
```

---

## Run 20260720T182536Z

- UTC timestamp: `20260720T182536Z`
- GitHub run: [#4462](https://github.com/28twagg-ops/TradingBot/actions/runs/29767658522)
- Run id: `29767658522`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`8s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T14:25:40.854247-04:00","date":"2026-07-20","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":2.8,"phases_s":{"reconcile":1.85,"cancel":0.22,"manage":0.15},"signals":0,"placed":0,"equity":131030.05,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":20,"filled_today":20,"unattributed_contracts":0,"top_signals":[],"github_run":"4462","github_run_id":"29767658522","status":"ok"}
```

### Live bot full output

```text
18:25:37  INFO      Mode: exits
18:25:38  INFO        Daily log -> logs/daily/2026-07-20.md
18:25:38  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (7 ledger rows)
18:25:38  INFO        place_all_stops: checking 1 positions...
18:25:38  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
18:25:38  INFO        [positions] 1/1 (1 valid)
18:25:38  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:25 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $481.96|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  COP  P&L +1.2%  $+1.02                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=0 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=2
  zombies_flagged=0
options_reconcile: done
Layout: controlled:140:c000_s173_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:140:c000_s173_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      140
=== options_morning_bot (PAPER) 2026-07-20T14:25:40.854247-04:00 ===

[Run context]
Paper auth OK — equity $131030.05, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S173, S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $131,030.05                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    20                                      |
|  Orders filled today (ledger)  20                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=516  buckets=49  win=37%                             |
|  Returns   avg=+10.2%  med=-28.8%  p10=-75.5%  p90=+97.5%              |
|  Realized  $+4,588.77                                                  |
|  Raw incl dropped  trades=630  real=$+3,090.58                         |
|  Today     trades=19  avg=+81.9%  med=+82.5%  real=$+981.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b51  c051_s164_w4_1120_  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  c091_s167_w4_1120_  3  67% +142.7 +197.0 +247.0 $   +282         |
|  b31  c031_s173_w4_1120_  2 100% +145.5 +145.5 +175.8 $   +192         |
|  b28  c028_s173_w1_0928_ 17  76% +49.5 +80.0 +102.0 $   +448           |
|  b92  c092_s165_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s165_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s165_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 41 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s164_w2_1005_ 23   4% -55.2 -72.1 -98.5 $   -863       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=2.8s reconcile=1.85s cancel=0.22s manage=0.15s
STATUS: options_morning_bot run complete (PAPER) elapsed=2.8s. run=#4462 https://github.com/28twagg-ops/TradingBot/actions/runs/29767658522
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.csv
Summary: 14 buckets closed trades, $+981.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 3.5% (22/630)
# Options signal frequency

_Generated 2026-07-20T14:25:46.566212_

Headline counts are **unique (strategy, underlying, date)** from `ENTRY` lines in `logs/options_trial/runs/*.log`.
Raw log-line counts (multi-bucket duplicates) are shown below for debug.

### Unique underlying symbols per day (headline)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-08 |    0 |    0 |    3 |    0 |    0 |    0 |    2 |    1 |     6 |
| 2026-07-09 |    0 |    0 |    1 |    0 |    0 |    0 |    2 |    3 |     6 |
| 2026-07-10 |    0 |    0 |    1 |    0 |    0 |    0 |    1 |    1 |     3 |
| 2026-07-13 |    0 |    0 |    2 |    0 |    0 |    0 |    3 |    2 |     7 |
| 2026-07-14 |    0 |    0 |    3 |    0 |    0 |    0 |    2 |    0 |     5 |
| 2026-07-16 |    0 |    0 |    2 |    0 |    0 |    0 |    3 |    0 |     5 |
| 2026-07-17 |    0 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |     4 |
| 2026-07-20 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S164 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S165 | 14 | 7 | 2.0 | ~19 active signal-days |
| S166 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S167 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S168 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 0 | 0 |
| S164 | 0 | 0 |
| S165 | 1309 | 14 |
| S166 | 0 | 0 |
| S167 | 0 | 0 |
| S168 | 0 | 0 |
| S173 | 1636 | 17 |
| S174 | 843 | 7 |

### Raw log lines per day (debug / multi-bucket)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |    0 |   100 |
| 2026-07-08 |    0 |    0 |  100 |    0 |    0 |    0 |  100 |  100 |   300 |
| 2026-07-09 |    0 |    0 |   24 |    0 |    0 |    0 |  100 |   15 |   139 |
| 2026-07-10 |    0 |    0 |  242 |    0 |    0 |    0 |  230 |  202 |   674 |
| 2026-07-13 |    0 |    0 |  190 |    0 |    0 |    0 |  212 |  188 |   590 |
| 2026-07-14 |    0 |    0 |  194 |    0 |    0 |    0 |  185 |  106 |   485 |
| 2026-07-15 |    0 |    0 |  146 |    0 |    0 |    0 |  154 |   58 |   358 |
| 2026-07-16 |    0 |    0 |  179 |    0 |    0 |    0 |  205 |   58 |   442 |
| 2026-07-17 |    0 |    0 |  127 |    0 |    0 |    0 |  207 |   58 |   392 |
| 2026-07-20 |    0 |    0 |  107 |    0 |    0 |    0 |  143 |   58 |   308 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-07-20
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |    27 | WARN | <<<
| Missing exit records (post) |    27 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |   274 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=481.96 router=PENDING leaderboard_rows=8
```

---

## Run 20260720T183035Z

- UTC timestamp: `20260720T183035Z`
- GitHub run: [#4463](https://github.com/28twagg-ops/TradingBot/actions/runs/29768011792)
- Run id: `29768011792`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`7s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T14:30:38.211717-04:00","date":"2026-07-20","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":1.9,"phases_s":{"reconcile":1.58,"cancel":0.02,"manage":0.03},"signals":0,"placed":0,"equity":130949.73,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":20,"filled_today":20,"unattributed_contracts":0,"top_signals":[],"github_run":"4463","github_run_id":"29768011792","status":"ok"}
```

### Live bot full output

```text
18:30:36  INFO      Mode: exits
18:30:36  INFO        Daily log -> logs/daily/2026-07-20.md
18:30:36  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (7 ledger rows)
18:30:36  INFO        place_all_stops: checking 1 positions...
18:30:36  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
18:30:36  INFO        [positions] 1/1 (1 valid)
18:30:36  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:30 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $481.97|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  COP  P&L +1.2%  $+1.03                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=0 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=2
  zombies_flagged=0
options_reconcile: done
Layout: controlled:140:c000_s173_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:140:c000_s173_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      140
=== options_morning_bot (PAPER) 2026-07-20T14:30:38.211717-04:00 ===

[Run context]
Paper auth OK — equity $130949.73, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S173, S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $130,949.73                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    20                                      |
|  Orders filled today (ledger)  20                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=516  buckets=49  win=37%                             |
|  Returns   avg=+10.2%  med=-28.8%  p10=-75.5%  p90=+97.5%              |
|  Realized  $+4,588.77                                                  |
|  Raw incl dropped  trades=630  real=$+3,090.58                         |
|  Today     trades=19  avg=+81.9%  med=+82.5%  real=$+981.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b51  c051_s164_w4_1120_  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  c091_s167_w4_1120_  3  67% +142.7 +197.0 +247.0 $   +282         |
|  b31  c031_s173_w4_1120_  2 100% +145.5 +145.5 +175.8 $   +192         |
|  b28  c028_s173_w1_0928_ 17  76% +49.5 +80.0 +102.0 $   +448           |
|  b92  c092_s165_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s165_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s165_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 41 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s164_w2_1005_ 23   4% -55.2 -72.1 -98.5 $   -863       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=1.9s reconcile=1.58s cancel=0.02s manage=0.03s
STATUS: options_morning_bot run complete (PAPER) elapsed=1.9s. run=#4463 https://github.com/28twagg-ops/TradingBot/actions/runs/29768011792
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.csv
Summary: 14 buckets closed trades, $+981.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 3.5% (22/630)
# Options signal frequency

_Generated 2026-07-20T14:30:43.067265_

Headline counts are **unique (strategy, underlying, date)** from `ENTRY` lines in `logs/options_trial/runs/*.log`.
Raw log-line counts (multi-bucket duplicates) are shown below for debug.

### Unique underlying symbols per day (headline)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-08 |    0 |    0 |    3 |    0 |    0 |    0 |    2 |    1 |     6 |
| 2026-07-09 |    0 |    0 |    1 |    0 |    0 |    0 |    2 |    3 |     6 |
| 2026-07-10 |    0 |    0 |    1 |    0 |    0 |    0 |    1 |    1 |     3 |
| 2026-07-13 |    0 |    0 |    2 |    0 |    0 |    0 |    3 |    2 |     7 |
| 2026-07-14 |    0 |    0 |    3 |    0 |    0 |    0 |    2 |    0 |     5 |
| 2026-07-16 |    0 |    0 |    2 |    0 |    0 |    0 |    3 |    0 |     5 |
| 2026-07-17 |    0 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |     4 |
| 2026-07-20 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S164 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S165 | 14 | 7 | 2.0 | ~19 active signal-days |
| S166 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S167 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S168 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 0 | 0 |
| S164 | 0 | 0 |
| S165 | 1309 | 14 |
| S166 | 0 | 0 |
| S167 | 0 | 0 |
| S168 | 0 | 0 |
| S173 | 1636 | 17 |
| S174 | 843 | 7 |

### Raw log lines per day (debug / multi-bucket)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |    0 |   100 |
| 2026-07-08 |    0 |    0 |  100 |    0 |    0 |    0 |  100 |  100 |   300 |
| 2026-07-09 |    0 |    0 |   24 |    0 |    0 |    0 |  100 |   15 |   139 |
| 2026-07-10 |    0 |    0 |  242 |    0 |    0 |    0 |  230 |  202 |   674 |
| 2026-07-13 |    0 |    0 |  190 |    0 |    0 |    0 |  212 |  188 |   590 |
| 2026-07-14 |    0 |    0 |  194 |    0 |    0 |    0 |  185 |  106 |   485 |
| 2026-07-15 |    0 |    0 |  146 |    0 |    0 |    0 |  154 |   58 |   358 |
| 2026-07-16 |    0 |    0 |  179 |    0 |    0 |    0 |  205 |   58 |   442 |
| 2026-07-17 |    0 |    0 |  127 |    0 |    0 |    0 |  207 |   58 |   392 |
| 2026-07-20 |    0 |    0 |  107 |    0 |    0 |    0 |  143 |   58 |   308 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-07-20
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |    27 | WARN | <<<
| Missing exit records (post) |    27 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |   274 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=481.97 router=PENDING leaderboard_rows=8
```

---

## Run 20260720T183535Z

- UTC timestamp: `20260720T183535Z`
- GitHub run: [#4464](https://github.com/28twagg-ops/TradingBot/actions/runs/29768369292)
- Run id: `29768369292`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`6s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-20T14:35:39.149612-04:00","date":"2026-07-20","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":1.8,"phases_s":{"reconcile":1.49,"cancel":0.02,"manage":0.02},"signals":0,"placed":0,"equity":130811.77,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":20,"filled_today":20,"unattributed_contracts":0,"top_signals":[],"github_run":"4464","github_run_id":"29768369292","status":"ok"}
```

### Live bot full output

```text
18:35:37  INFO      Mode: exits
18:35:37  INFO        Daily log -> logs/daily/2026-07-20.md
18:35:37  INFO        Daily log reconciled -> logs/daily/2026-07-20.md (7 ledger rows)
18:35:37  INFO        place_all_stops: checking 1 positions...
18:35:37  INFO        STOP skipped COP: fractional (0.7700 shares) — software exit will handle it
18:35:37  INFO        [positions] 1/1 (1 valid)
18:35:37  INFO        Daily log -> logs/daily/2026-07-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:35 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $481.90|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  COP  P&L +1.1%  $+0.96                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=0 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=2
  zombies_flagged=0
options_reconcile: done
Layout: controlled:140:c000_s173_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:140:c000_s173_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      140
=== options_morning_bot (PAPER) 2026-07-20T14:35:39.149612-04:00 ===

[Run context]
Paper auth OK — equity $130811.77, account PA36KS87UPRS

[Setup]
Active buckets: 140 | Strategies: S173, S165, S164, S168, S167, S166, S163
Dropped (no new entries; ex-reflected P&L): S174

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $130,811.77                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    20                                      |
|  Orders filled today (ledger)  20                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S174)                                |
+------------------------------------------------------------------------+
|  Reflected trades=516  buckets=49  win=37%                             |
|  Returns   avg=+10.2%  med=-28.8%  p10=-75.5%  p90=+97.5%              |
|  Realized  $+4,588.77                                                  |
|  Raw incl dropped  trades=630  real=$+3,090.58                         |
|  Today     trades=19  avg=+81.9%  med=+82.5%  real=$+981.00            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b51  c051_s164_w4_1120_  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  c091_s167_w4_1120_  3  67% +142.7 +197.0 +247.0 $   +282         |
|  b31  c031_s173_w4_1120_  2 100% +145.5 +145.5 +175.8 $   +192         |
|  b28  c028_s173_w1_0928_ 17  76% +49.5 +80.0 +102.0 $   +448           |
|  b92  c092_s165_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b93  c093_s165_w2_1005_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b95  c095_s165_w4_1120_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  b96  c096_s166_w1_0928_  1 100% +70.8 +70.8 +70.8 $    +71            |
|  ... 41 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b21  c021_s164_w2_1005_ 23   4% -55.2 -72.1 -98.5 $   -863       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-20.log
elapsed=1.8s reconcile=1.49s cancel=0.02s manage=0.02s
STATUS: options_morning_bot run complete (PAPER) elapsed=1.8s. run=#4464 https://github.com/28twagg-ops/TradingBot/actions/runs/29768369292
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_buckets.csv
Summary: 14 buckets closed trades, $+981.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-20_strategy_selection.csv
Summary: keep=0 watch=5 drop=3
Orphan rate: 3.5% (22/630)
# Options signal frequency

_Generated 2026-07-20T14:35:43.776839_

Headline counts are **unique (strategy, underlying, date)** from `ENTRY` lines in `logs/options_trial/runs/*.log`.
Raw log-line counts (multi-bucket duplicates) are shown below for debug.

### Unique underlying symbols per day (headline)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-08 |    0 |    0 |    3 |    0 |    0 |    0 |    2 |    1 |     6 |
| 2026-07-09 |    0 |    0 |    1 |    0 |    0 |    0 |    2 |    3 |     6 |
| 2026-07-10 |    0 |    0 |    1 |    0 |    0 |    0 |    1 |    1 |     3 |
| 2026-07-13 |    0 |    0 |    2 |    0 |    0 |    0 |    3 |    2 |     7 |
| 2026-07-14 |    0 |    0 |    3 |    0 |    0 |    0 |    2 |    0 |     5 |
| 2026-07-16 |    0 |    0 |    2 |    0 |    0 |    0 |    3 |    0 |     5 |
| 2026-07-17 |    0 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |     4 |
| 2026-07-20 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S164 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S165 | 14 | 7 | 2.0 | ~19 active signal-days |
| S166 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S167 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S168 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 0 | 0 |
| S164 | 0 | 0 |
| S165 | 1309 | 14 |
| S166 | 0 | 0 |
| S167 | 0 | 0 |
| S168 | 0 | 0 |
| S173 | 1636 | 17 |
| S174 | 843 | 7 |

### Raw log lines per day (debug / multi-bucket)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |    0 |   100 |
| 2026-07-08 |    0 |    0 |  100 |    0 |    0 |    0 |  100 |  100 |   300 |
| 2026-07-09 |    0 |    0 |   24 |    0 |    0 |    0 |  100 |   15 |   139 |
| 2026-07-10 |    0 |    0 |  242 |    0 |    0 |    0 |  230 |  202 |   674 |
| 2026-07-13 |    0 |    0 |  190 |    0 |    0 |    0 |  212 |  188 |   590 |
| 2026-07-14 |    0 |    0 |  194 |    0 |    0 |    0 |  185 |  106 |   485 |
| 2026-07-15 |    0 |    0 |  146 |    0 |    0 |    0 |  154 |   58 |   358 |
| 2026-07-16 |    0 |    0 |  179 |    0 |    0 |    0 |  205 |   58 |   442 |
| 2026-07-17 |    0 |    0 |  127 |    0 |    0 |    0 |  207 |   58 |   392 |
| 2026-07-20 |    0 |    0 |  107 |    0 |    0 |    0 |  143 |   58 |   308 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-07-20
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |    27 | WARN | <<<
| Missing exit records (post) |    27 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |   274 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   589 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=481.9 router=PENDING leaderboard_rows=8
```

---
