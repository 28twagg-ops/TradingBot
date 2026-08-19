# Daily Comprehensive Action Review - 2026-08-19

_Auto-generated from GitHub Actions run output. Each run appends a summary; full stdout is in linked per-run log files._
## Run 20260819T130159Z

- UTC timestamp: `20260819T130159Z`
- GitHub run: [#7468](https://github.com/28twagg-ops/TradingBot/actions/runs/32255635527)
- Run id: `32255635527`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T130159Z_live_bot.log`, `logs/action_runs/20260819T130159Z_live_options.log`, `logs/action_runs/20260819T130159Z_options_bot.log`

### Live bot (tail)

```text
13:02:00  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:02 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $517.13|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $517.13|
|  Cash                                                           $284.37|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $232.76|
|  Open P&L                                                        $+0.22|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (3 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AAPL     Pullback50      $77.34     $310.56  $309.86  -0.2%   $-0.17  |
|  CDW      Pullback50      $77.60     $134.83  $134.97  +0.1%   $+0.08  |
|  MNST     MomReversal     $77.82     $47.41   $47.60   +0.4%   $+0.31  |
|                                                                        |
|  Total invested                                                 $232.76|
|  Total open P&L                                                  $+0.22|
+========================================================================+

+========================================================================+
|                     OPTION HOLDINGS  (0 contracts)                     |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
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
|  2026-08-18  SELL  CNC  Pullback50  $77.65  P&L $+0.14                 |
|  2026-08-18  SELL  AON  Pullback50  $69.74  P&L $-0.36                 |
|  2026-08-18  SELL  AEE  Pullback50  $69.70  P&L $-0.40                 |
|  2026-08-18  SELL  AFL  Pullback50  $69.80  P&L $-0.36                 |
|  2026-08-18  SELL  AES  Pullback50  $70.15  P&L $+0.00                 |
|  2026-08-18  SELL  AKAM  Pullback50  $69.79  P&L $-0.37                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T09:02:02.673726-04:00 share=50% ===
2026-08-19 09:02:02,673 INFO === options_live_micro LIVE 2026-08-19T09:02:02.673726-04:00 share=50% ===
Live account equity $517.13 cash $284.37 #225458845 options_level=3
2026-08-19 09:02:02,880 INFO Live account equity $517.13 cash $284.37 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-08-19 09:02:02,941 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-08-19 09:02:03,000 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T130551Z

- UTC timestamp: `20260819T130551Z`
- GitHub run: [#7469](https://github.com/28twagg-ops/TradingBot/actions/runs/32256104204)
- Run id: `32256104204`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T130551Z_live_bot.log`, `logs/action_runs/20260819T130551Z_live_options.log`, `logs/action_runs/20260819T130551Z_options_bot.log`

### Live bot (tail)

```text
13:05:52  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:05 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $517.15|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $517.15|
|  Cash                                                           $284.37|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $232.78|
|  Open P&L                                                        $+0.24|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (3 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AAPL     Pullback50      $77.36     $310.56  $309.94  -0.2%   $-0.15  |
|  CDW      Pullback50      $77.60     $134.83  $134.97  +0.1%   $+0.08  |
|  MNST     MomReversal     $77.82     $47.41   $47.60   +0.4%   $+0.31  |
|                                                                        |
|  Total invested                                                 $232.78|
|  Total open P&L                                                  $+0.24|
+========================================================================+

+========================================================================+
|                     OPTION HOLDINGS  (0 contracts)                     |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
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
|  2026-08-18  SELL  CNC  Pullback50  $77.65  P&L $+0.14                 |
|  2026-08-18  SELL  AON  Pullback50  $69.74  P&L $-0.36                 |
|  2026-08-18  SELL  AEE  Pullback50  $69.70  P&L $-0.40                 |
|  2026-08-18  SELL  AFL  Pullback50  $69.80  P&L $-0.36                 |
|  2026-08-18  SELL  AES  Pullback50  $70.15  P&L $+0.00                 |
|  2026-08-18  SELL  AKAM  Pullback50  $69.79  P&L $-0.37                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T09:05:54.341759-04:00 share=50% ===
2026-08-19 09:05:54,341 INFO === options_live_micro LIVE 2026-08-19T09:05:54.341759-04:00 share=50% ===
Live account equity $517.15 cash $284.37 #225458845 options_level=3
2026-08-19 09:05:54,407 INFO Live account equity $517.15 cash $284.37 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-08-19 09:05:54,420 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-08-19 09:05:54,432 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T131055Z

- UTC timestamp: `20260819T131055Z`
- GitHub run: [#7470](https://github.com/28twagg-ops/TradingBot/actions/runs/32256563842)
- Run id: `32256563842`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T131055Z_live_bot.log`, `logs/action_runs/20260819T131055Z_live_options.log`, `logs/action_runs/20260819T131055Z_options_bot.log`

### Live bot (tail)

```text
13:10:56  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $516.97|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $516.97|
|  Cash                                                           $284.37|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $232.60|
|  Open P&L                                                        $+0.06|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (3 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AAPL     Pullback50      $77.40     $310.56  $310.13  -0.1%   $-0.11  |
|  CDW      Pullback50      $77.60     $134.83  $134.97  +0.1%   $+0.08  |
|  MNST     MomReversal     $77.60     $47.41   $47.46   +0.1%   $+0.09  |
|                                                                        |
|  Total invested                                                 $232.60|
|  Total open P&L                                                  $+0.06|
+========================================================================+

+========================================================================+
|                     OPTION HOLDINGS  (0 contracts)                     |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
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
|  2026-08-18  SELL  CNC  Pullback50  $77.65  P&L $+0.14                 |
|  2026-08-18  SELL  AON  Pullback50  $69.74  P&L $-0.36                 |
|  2026-08-18  SELL  AEE  Pullback50  $69.70  P&L $-0.40                 |
|  2026-08-18  SELL  AFL  Pullback50  $69.80  P&L $-0.36                 |
|  2026-08-18  SELL  AES  Pullback50  $70.15  P&L $+0.00                 |
|  2026-08-18  SELL  AKAM  Pullback50  $69.79  P&L $-0.37                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T09:10:57.585819-04:00 share=50% ===
2026-08-19 09:10:57,585 INFO === options_live_micro LIVE 2026-08-19T09:10:57.585819-04:00 share=50% ===
Live account equity $516.97 cash $284.37 #225458845 options_level=3
2026-08-19 09:10:57,629 INFO Live account equity $516.97 cash $284.37 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-08-19 09:10:57,637 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-08-19 09:10:57,646 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---
