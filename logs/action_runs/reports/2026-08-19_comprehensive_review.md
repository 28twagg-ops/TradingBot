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

## Run 20260819T131554Z

- UTC timestamp: `20260819T131554Z`
- GitHub run: [#7471](https://github.com/28twagg-ops/TradingBot/actions/runs/32257022577)
- Run id: `32257022577`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T131554Z_live_bot.log`, `logs/action_runs/20260819T131554Z_live_options.log`, `logs/action_runs/20260819T131554Z_options_bot.log`

### Live bot (tail)

```text
13:15:55  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:15 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $517.01|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $517.01|
|  Cash                                                           $284.37|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $232.64|
|  Open P&L                                                        $+0.10|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (3 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AAPL     Pullback50      $77.45     $310.56  $310.30  -0.1%   $-0.06  |
|  CDW      Pullback50      $77.60     $134.83  $134.97  +0.1%   $+0.08  |
|  MNST     MomReversal     $77.60     $47.41   $47.46   +0.1%   $+0.09  |
|                                                                        |
|  Total invested                                                 $232.64|
|  Total open P&L                                                  $+0.10|
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
=== options_live_micro LIVE 2026-08-19T09:15:57.383636-04:00 share=50% ===
2026-08-19 09:15:57,383 INFO === options_live_micro LIVE 2026-08-19T09:15:57.383636-04:00 share=50% ===
Live account equity $517.01 cash $284.37 #225458845 options_level=3
2026-08-19 09:15:57,578 INFO Live account equity $517.01 cash $284.37 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-08-19 09:15:57,633 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-08-19 09:15:57,687 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T132055Z

- UTC timestamp: `20260819T132055Z`
- GitHub run: [#7472](https://github.com/28twagg-ops/TradingBot/actions/runs/32257486997)
- Run id: `32257486997`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T132055Z_live_bot.log`, `logs/action_runs/20260819T132055Z_live_options.log`, `logs/action_runs/20260819T132055Z_options_bot.log`

### Live bot (tail)

```text
13:20:57  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $516.99|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $516.99|
|  Cash                                                           $284.37|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $232.62|
|  Open P&L                                                        $+0.08|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (3 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AAPL     Pullback50      $77.43     $310.56  $310.23  -0.1%   $-0.08  |
|  CDW      Pullback50      $77.60     $134.83  $134.97  +0.1%   $+0.08  |
|  MNST     MomReversal     $77.60     $47.41   $47.46   +0.1%   $+0.09  |
|                                                                        |
|  Total invested                                                 $232.62|
|  Total open P&L                                                  $+0.08|
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
=== options_live_micro LIVE 2026-08-19T09:20:58.442529-04:00 share=50% ===
2026-08-19 09:20:58,442 INFO === options_live_micro LIVE 2026-08-19T09:20:58.442529-04:00 share=50% ===
Live account equity $516.99 cash $284.37 #225458845 options_level=3
2026-08-19 09:20:58,732 INFO Live account equity $516.99 cash $284.37 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-08-19 09:20:58,763 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-08-19 09:20:58,772 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T132553Z

- UTC timestamp: `20260819T132553Z`
- GitHub run: [#7473](https://github.com/28twagg-ops/TradingBot/actions/runs/32257957443)
- Run id: `32257957443`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T132553Z_live_bot.log`, `logs/action_runs/20260819T132553Z_live_options.log`, `logs/action_runs/20260819T132553Z_options_bot.log`

### Live bot (tail)

```text
13:25:54  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:25 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $517.42|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $517.42|
|  Cash                                                           $284.37|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $233.05|
|  Open P&L                                                        $+0.51|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (3 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AAPL     Pullback50      $77.44     $310.56  $310.29  -0.1%   $-0.07  |
|  CDW      Pullback50      $77.60     $134.83  $134.97  +0.1%   $+0.08  |
|  MNST     MomReversal     $78.00     $47.41   $47.71   +0.6%   $+0.49  |
|                                                                        |
|  Total invested                                                 $233.05|
|  Total open P&L                                                  $+0.51|
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
=== options_live_micro LIVE 2026-08-19T09:25:55.359103-04:00 share=50% ===
2026-08-19 09:25:55,359 INFO === options_live_micro LIVE 2026-08-19T09:25:55.359103-04:00 share=50% ===
Live account equity $517.42 cash $284.37 #225458845 options_level=3
2026-08-19 09:25:55,423 INFO Live account equity $517.42 cash $284.37 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-08-19 09:25:55,438 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-08-19 09:25:55,451 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T133055Z

- UTC timestamp: `20260819T133055Z`
- GitHub run: [#7474](https://github.com/28twagg-ops/TradingBot/actions/runs/32258442202)
- Run id: `32258442202`
- Live bot: exit=`0`, duration=`218s`
- Live options: exit=`0`, duration=`17s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T133055Z_live_bot.log`, `logs/action_runs/20260819T133055Z_live_options.log`, `logs/action_runs/20260819T133055Z_options_bot.log`

### Live bot (tail)

```text
13:30:56  INFO      Mode: morning_prep
13:30:58  INFO        [prep_positions] 3/3 (3 valid)
13:30:58  INFO      Fetching tickers (universe=both)...
13:30:58  INFO        S&P 500: 503
13:30:58  INFO        MidCap 400: 400
13:30:58  INFO        Total: 903 tickers
13:30:59  INFO        [prep_universe] 40/900 (40 valid)
13:31:01  INFO        [prep_universe] 80/900 (80 valid)
13:31:03  INFO        [prep_universe] 120/900 (120 valid)
13:31:05  INFO        [prep_universe] 160/900 (160 valid)
13:31:08  INFO        [prep_universe] 200/900 (199 valid)
13:31:13  INFO        [prep_universe] 240/900 (238 valid)
13:31:24  INFO        [prep_universe] 280/900 (278 valid)
13:31:35  INFO        [prep_universe] 320/900 (318 valid)
13:31:49  INFO        [prep_universe] 360/900 (358 valid)
13:32:00  INFO        [prep_universe] 400/900 (397 valid)
13:32:14  INFO        [prep_universe] 440/900 (437 valid)
13:32:25  INFO        [prep_universe] 480/900 (477 valid)
13:32:35  INFO        [prep_universe] 520/900 (517 valid)
13:32:49  INFO        [prep_universe] 560/900 (557 valid)
13:33:00  INFO        [prep_universe] 600/900 (597 valid)
13:33:14  INFO        [prep_universe] 640/900 (637 valid)
13:33:25  INFO        [prep_universe] 680/900 (677 valid)
13:33:36  INFO        [prep_universe] 720/900 (717 valid)
13:33:50  INFO        [prep_universe] 760/900 (757 valid)
13:34:00  INFO        [prep_universe] 800/900 (797 valid)
13:34:13  INFO        [prep_universe] 840/900 (836 valid)
13:34:24  INFO        [prep_universe] 880/900 (876 valid)
13:34:31  INFO        [prep_universe] 900/900 (896 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:30 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $517.05|
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
|  Invested                                                       $232.69|
|  Open P&L                                                        $+0.15|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AAPL     Pullback50      $77.57     $310.56  $310.81  +0.1%   $+0.06  |
|  CDW      Pullback50      $77.60     $134.83  $134.97  +0.1%   $+0.08  |
|  MNST     MomReversal     $77.51     $47.41   $47.41   +0.0%   $+0.00  |
+========================================================================+

+========================================================================+
|                            OPEN SELL ORDERS                            |
+========================================================================+
|  Count                                                                1|
|  TICKER    TYPE              QTY       LIMIT       STOP                |
+------------------------------------------------------------------------+
|  MNST      OrderType.STOP    1         None        47.17               |
+========================================================================+

+========================================================================+
|                              PREP SUMMARY                              |
+========================================================================+
|  Saved                                                              yes|
|  Exit candidates                                                      0|
|  Signal candidates                                                   38|
|  Universe scanned                                                   900|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T09:34:34.436524-04:00 share=50% ===
2026-08-19 09:34:34,436 INFO === options_live_micro LIVE 2026-08-19T09:34:34.436524-04:00 share=50% ===
Live account equity $518.18 cash $284.37 #225458845 options_level=3
2026-08-19 09:34:34,936 INFO Live account equity $518.18 cash $284.37 #225458845 options_level=3
Live micro sleeve $259 (50% of $518) deployed $0 open_strategies=0/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
2026-08-19 09:34:35,212 INFO Live micro sleeve $259 (50% of $518) deployed $0 open_strategies=0/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-19 09:34:35,213 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 3
2026-08-19 09:34:48,757 INFO Live micro signals: 3
  try S404 100%win/+80%med AVGO
2026-08-19 09:34:48,757 INFO   try S404 100%win/+80%med AVGO
LIVE BUY S404 100%win AVGO AVGO260821C00392500 limit=0.69 ask=0.70 cost=$70 id=d756ab40-a7d4-4584-b6b5-985f2b72d1d5
2026-08-19 09:34:49,433 INFO LIVE BUY S404 100%win AVGO AVGO260821C00392500 limit=0.69 ask=0.70 cost=$70 id=d756ab40-a7d4-4584-b6b5-985f2b72d1d5
  try S210 55%win/+47%med EOG
2026-08-19 09:34:49,433 INFO   try S210 55%win/+47%med EOG
  skip S210 EOG: no contract under $75
2026-08-19 09:34:49,657 INFO   skip S210 EOG: no contract under $75
  try S210 55%win/+47%med UNP
2026-08-19 09:34:49,657 INFO   try S210 55%win/+47%med UNP
  skip S210 UNP: no contract under $75
2026-08-19 09:34:49,882 INFO   skip S210 UNP: no contract under $75
LIVE PROT STOP AVGO260821C00392500 x1 stop=0.34 id=33deab3d-1fd0-4c1c-8fb1-7d101ab2f787
2026-08-19 09:34:50,133 INFO LIVE PROT STOP AVGO260821C00392500 x1 stop=0.34 id=33deab3d-1fd0-4c1c-8fb1-7d101ab2f787
Live micro done. open_options=1 lots=1
2026-08-19 09:34:50,202 INFO Live micro done. open_options=1 lots=1
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T133554Z

- UTC timestamp: `20260819T133554Z`
- GitHub run: [#7475](https://github.com/28twagg-ops/TradingBot/actions/runs/32258917594)
- Run id: `32258917594`
- Live bot: exit=`0`, duration=`215s`
- Live options: exit=`0`, duration=`3s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T133554Z_live_bot.log`, `logs/action_runs/20260819T133554Z_live_options.log`, `logs/action_runs/20260819T133554Z_options_bot.log`

### Live bot (tail)

```text
13:35:55  INFO      Mode: morning_prep
13:35:55  INFO        [prep_positions] 3/3 (3 valid)
13:35:55  INFO        Universe cache hit: 903 tickers (tickers_2026-08-19.json)
13:35:57  INFO        [prep_universe] 40/900 (40 valid)
13:35:59  INFO        [prep_universe] 80/900 (80 valid)
13:36:01  INFO        [prep_universe] 120/900 (120 valid)
13:36:02  INFO        [prep_universe] 160/900 (160 valid)
13:36:04  INFO        [prep_universe] 200/900 (199 valid)
13:36:09  INFO        [prep_universe] 240/900 (238 valid)
13:36:22  INFO        [prep_universe] 280/900 (278 valid)
13:36:33  INFO        [prep_universe] 320/900 (318 valid)
13:36:45  INFO        [prep_universe] 360/900 (358 valid)
13:36:59  INFO        [prep_universe] 400/900 (397 valid)
13:37:09  INFO        [prep_universe] 440/900 (437 valid)
13:37:24  INFO        [prep_universe] 480/900 (477 valid)
13:37:34  INFO        [prep_universe] 520/900 (517 valid)
13:37:47  INFO        [prep_universe] 560/900 (557 valid)
13:37:56  INFO        [prep_universe] 600/900 (597 valid)
13:38:10  INFO        [prep_universe] 640/900 (637 valid)
13:38:23  INFO        [prep_universe] 680/900 (677 valid)
13:38:33  INFO        [prep_universe] 720/900 (717 valid)
13:38:47  INFO        [prep_universe] 760/900 (757 valid)
13:38:59  INFO        [prep_universe] 800/900 (797 valid)
13:39:10  INFO        [prep_universe] 840/900 (836 valid)
13:39:23  INFO        [prep_universe] 880/900 (876 valid)
13:39:27  INFO        [prep_universe] 900/900 (896 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:35 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $503.26|
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
|  Invested                                                       $233.95|
|  Open P&L                                                        $+1.41|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AAPL     Pullback50      $77.68     $310.56  $311.22  +0.2%   $+0.17  |
|  CDW      Pullback50      $78.57     $134.83  $136.65  +1.3%   $+1.05  |
|  MNST     MomReversal     $77.71     $47.41   $47.53   +0.3%   $+0.20  |
+========================================================================+

+========================================================================+
|                            OPEN SELL ORDERS                            |
+========================================================================+
|  Count                                                                2|
|  TICKER    TYPE              QTY       LIMIT       STOP                |
+------------------------------------------------------------------------+
|  AVGO260~  OrderType.STOP_~  1         0.31        0.34                |
|  MNST      OrderType.STOP    1         None        47.17               |
+========================================================================+

+========================================================================+
|                              PREP SUMMARY                              |
+========================================================================+
|  Saved                                                              yes|
|  Exit candidates                                                      0|
|  Signal candidates                                                   36|
|  Universe scanned                                                   900|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T09:39:30.156876-04:00 share=50% ===
2026-08-19 09:39:30,156 INFO === options_live_micro LIVE 2026-08-19T09:39:30.156876-04:00 share=50% ===
Live account equity $486.26 cash $216.31 #225458845 options_level=3
2026-08-19 09:39:30,204 INFO Live account equity $486.26 cash $216.31 #225458845 options_level=3
Live micro hold S404 AVGO260821C00392500 -47.1% (tp +50% / sl -50%)
2026-08-19 09:39:30,226 INFO Live micro hold S404 AVGO260821C00392500 -47.1% (tp +50% / sl -50%)
Live micro sleeve $243 (50% of $486) deployed $36 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
2026-08-19 09:39:30,252 INFO Live micro sleeve $243 (50% of $486) deployed $36 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-19 09:39:30,252 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 3
2026-08-19 09:39:31,911 INFO Live micro signals: 3
  skip S404 AVGO: strategy already open (paper bucket rule)
2026-08-19 09:39:31,911 INFO   skip S404 AVGO: strategy already open (paper bucket rule)
  try S210 55%win/+47%med EOG
2026-08-19 09:39:31,912 INFO   try S210 55%win/+47%med EOG
  skip S210 EOG: no contract under $75
2026-08-19 09:39:32,079 INFO   skip S210 EOG: no contract under $75
  try S210 55%win/+47%med UNP
2026-08-19 09:39:32,079 INFO   try S210 55%win/+47%med UNP
  skip S210 UNP: no contract under $75
2026-08-19 09:39:32,218 INFO   skip S210 UNP: no contract under $75
Live micro done. open_options=1 lots=1
2026-08-19 09:39:32,253 INFO Live micro done. open_options=1 lots=1
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T134056Z

- UTC timestamp: `20260819T134056Z`
- GitHub run: [#7476](https://github.com/28twagg-ops/TradingBot/actions/runs/32259390107)
- Run id: `32259390107`
- Live bot: exit=`0`, duration=`218s`
- Live options: exit=`0`, duration=`5s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T134056Z_live_bot.log`, `logs/action_runs/20260819T134056Z_live_options.log`, `logs/action_runs/20260819T134056Z_options_bot.log`

### Live bot (tail)

```text
13:40:57  INFO      Mode: morning_prep
13:40:58  INFO        [prep_positions] 3/3 (3 valid)
13:40:58  INFO        Universe cache hit: 903 tickers (tickers_2026-08-19.json)
13:41:00  INFO        [prep_universe] 40/900 (40 valid)
13:41:01  INFO        [prep_universe] 80/900 (80 valid)
13:41:03  INFO        [prep_universe] 120/900 (120 valid)
13:41:04  INFO        [prep_universe] 160/900 (160 valid)
13:41:06  INFO        [prep_universe] 200/900 (199 valid)
13:41:13  INFO        [prep_universe] 240/900 (238 valid)
13:41:24  INFO        [prep_universe] 280/900 (278 valid)
13:41:37  INFO        [prep_universe] 320/900 (318 valid)
13:41:48  INFO        [prep_universe] 360/900 (358 valid)
13:42:01  INFO        [prep_universe] 400/900 (397 valid)
13:42:12  INFO        [prep_universe] 440/900 (437 valid)
13:42:25  INFO        [prep_universe] 480/900 (477 valid)
13:42:36  INFO        [prep_universe] 520/900 (517 valid)
13:42:49  INFO        [prep_universe] 560/900 (557 valid)
13:42:59  INFO        [prep_universe] 600/900 (597 valid)
13:43:13  INFO        [prep_universe] 640/900 (637 valid)
13:43:23  INFO        [prep_universe] 680/900 (677 valid)
13:43:37  INFO        [prep_universe] 720/900 (717 valid)
13:43:47  INFO        [prep_universe] 760/900 (757 valid)
13:44:01  INFO        [prep_universe] 800/900 (797 valid)
13:44:11  INFO        [prep_universe] 840/900 (836 valid)
13:44:25  INFO        [prep_universe] 880/900 (876 valid)
13:44:32  INFO        [prep_universe] 900/900 (896 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:40 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $486.04|
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
|  Invested                                                       $233.76|
|  Open P&L                                                        $+1.22|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AAPL     Pullback50      $77.79     $310.56  $311.67  +0.4%   $+0.28  |
|  CDW      Pullback50      $78.00     $134.83  $135.66  +0.6%   $+0.48  |
|  MNST     MomReversal     $77.97     $47.41   $47.69   +0.6%   $+0.46  |
+========================================================================+

+========================================================================+
|                            OPEN SELL ORDERS                            |
+========================================================================+
|  Count                                                                1|
|  TICKER    TYPE              QTY       LIMIT       STOP                |
+------------------------------------------------------------------------+
|  MNST      OrderType.STOP    1         None        47.17               |
+========================================================================+

+========================================================================+
|                              PREP SUMMARY                              |
+========================================================================+
|  Saved                                                              yes|
|  Exit candidates                                                      0|
|  Signal candidates                                                   41|
|  Universe scanned                                                   900|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T09:44:35.396403-04:00 share=50% ===
2026-08-19 09:44:35,396 INFO === options_live_micro LIVE 2026-08-19T09:44:35.396403-04:00 share=50% ===
Live account equity $480.96 cash $247.26 #225458845 options_level=3
2026-08-19 09:44:35,606 INFO Live account equity $480.96 cash $247.26 #225458845 options_level=3
Live micro reconcile: drop AVGO260821C00392500 S404 (not at broker)
2026-08-19 09:44:35,727 INFO Live micro reconcile: drop AVGO260821C00392500 S404 (not at broker)
Live micro sleeve $240 (50% of $481) deployed $0 open_strategies=0/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
2026-08-19 09:44:35,912 INFO Live micro sleeve $240 (50% of $481) deployed $0 open_strategies=0/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-19 09:44:35,912 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 3
2026-08-19 09:44:37,773 INFO Live micro signals: 3
  try S404 100%win/+80%med AVGO
2026-08-19 09:44:37,774 INFO   try S404 100%win/+80%med AVGO
LIVE BUY S404 100%win AVGO AVGO260821C00385000 limit=0.71 ask=0.72 cost=$72 id=642a7630-c2e1-49d4-ad0f-1b801cad0a11
2026-08-19 09:44:38,402 INFO LIVE BUY S404 100%win AVGO AVGO260821C00385000 limit=0.71 ask=0.72 cost=$72 id=642a7630-c2e1-49d4-ad0f-1b801cad0a11
  try S210 55%win/+47%med EOG
2026-08-19 09:44:38,403 INFO   try S210 55%win/+47%med EOG
  skip S210 EOG: no contract under $75
2026-08-19 09:44:38,596 INFO   skip S210 EOG: no contract under $75
  try S210 55%win/+47%med UNP
2026-08-19 09:44:38,596 INFO   try S210 55%win/+47%med UNP
  skip S210 UNP: no contract under $75
2026-08-19 09:44:38,804 INFO   skip S210 UNP: no contract under $75
LIVE PROT STOP AVGO260821C00385000 x1 stop=0.35 id=7acebc3b-7ac9-4c9f-ab7b-b205a1d98aeb
2026-08-19 09:44:39,011 INFO LIVE PROT STOP AVGO260821C00385000 x1 stop=0.35 id=7acebc3b-7ac9-4c9f-ab7b-b205a1d98aeb
Live micro done. open_options=1 lots=1
2026-08-19 09:44:39,080 INFO Live micro done. open_options=1 lots=1
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T134554Z

- UTC timestamp: `20260819T134554Z`
- GitHub run: [#7477](https://github.com/28twagg-ops/TradingBot/actions/runs/32259880224)
- Run id: `32259880224`
- Live bot: exit=`0`, duration=`216s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T134554Z_live_bot.log`, `logs/action_runs/20260819T134554Z_live_options.log`, `logs/action_runs/20260819T134554Z_options_bot.log`

### Live bot (tail)

```text
... (118 earlier lines - see full log file)
|  TICKER   STRATEGY        TIER   PRICE    RSI    VOL_Z   TRIGGER       |
+------------------------------------------------------------------------+
|  AEE      Pullback50      eq     $110.72  61.1   -2.27   50MA bounce (-|
|  AON      Pullback50      eq     $346.29  27.0   -1.32   50MA bounce (-|
|  BXP      Pullback50      eq     $67.61   34.6   -1.82   50MA bounce (-|
|  BRK-B    Pullback50      eq     $505.00  46.3   -3.13   50MA bounce (+|
|  CL       Pullback50      eq     $92.31   52.9   -2.63   50MA bounce (+|
|  ED       Pullback50      eq     $109.24  47.5   -2.89   50MA bounce (-|
|  CB       Pullback50      eq     $346.57  44.0   -2.80   50MA bounce (+|
|  DHI      Pullback50      eq     $151.81  56.4   -2.46   50MA bounce (+|
|  DUK      Pullback50      eq     $124.85  44.8   -1.80   50MA bounce (-|
|  EVRG     Pullback50      eq     $84.38   57.9   -3.00   50MA bounce (-|
|  EXR      Pullback50      eq     $148.85  52.5   -1.77   50MA bounce (+|
|  ESS      Pullback50      eq     $285.89  56.2   -2.01   50MA bounce (-|
|  ES       Pullback50      eq     $72.61   42.1   -2.20   50MA bounce (+|
|  FE       Pullback50      eq     $47.63   36.2   -2.18   50MA bounce (-|
|  F        Pullback50      eq     $14.23   38.6   -2.09   50MA bounce (+|
|  HRL      Pullback50      eq     $24.73   40.0   -2.57   50MA bounce (-|
|  HLT      Pullback50      eq     $333.33  58.8   -2.59   50MA bounce (+|
|  JBHT     Pullback50      eq     $279.45  58.0   -2.46   50MA bounce (-|
|  KVUE     Pullback50      eq     $19.08   45.8   -2.38   50MA bounce (+|
|  INVH     Pullback50      eq     $30.05   56.1   -2.21   50MA bounce (+|
|  KDP      Pullback50      eq     $31.26   47.8   -3.36   50MA bounce (+|
|  PGR      Pullback50      eq     $213.66  50.6   -2.94   50MA bounce (-|
|  O        Pullback50      eq     $62.81   34.5   -2.20   50MA bounce (-|
|  RCL      Pullback50      eq     $302.62  30.0   -1.63   50MA bounce (-|
|  SPG      Pullback50      eq     $222.34  31.4   -2.69   50MA bounce (-|
|  VTRS     Pullback50      eq     $16.52   28.3   -2.35   50MA bounce (-|13:49:29  INFO        place_all_stops: checking 4 positions...
13:49:29  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
13:49:29  INFO        STOP skipped CDW: fractional (0.5749 shares) — software exit will handle it
13:49:29  INFO        STOP already live MNST @ $47.17
13:49:29  INFO        Daily log -> logs/daily/2026-08-19.md
13:49:30  INFO        Dashboard written → logs/dashboard.md

|  WRB      Pullback50      eq     $70.75   32.9   -2.75   50MA bounce (-|
|  WM       Pullback50      eq     $225.85  48.5   -2.52   50MA bounce (-|
|  WY       Pullback50      eq     $24.26   56.8   -2.20   50MA bounce (-|
|  XEL      Pullback50      eq     $79.79   61.7   -2.58   50MA bounce (+|
|  AN       Pullback50      eq     $201.38  29.3   -1.43   50MA bounce (+|
|  CAVA     Pullback50      eq     $72.60   58.6   -1.56   50MA bounce (+|
|  CHH      Pullback50      eq     $110.52  47.8   -2.30   50MA bounce (+|
|  CROX     Pullback50      eq     $129.66  57.0   -1.78   50MA bounce (+|
|  CUBE     Pullback50      eq     $41.53   53.6   -2.33   50MA bounce (+|
|  ELAN     Pullback50      eq     $24.41   38.8   -1.37   50MA bounce (-|
|  ELS      Pullback50      eq     $65.10   47.1   -2.13   50MA bounce (+|
|  EXEL     Pullback50      eq     $53.80   44.6   -2.13   50MA bounce (-|
|  FCFS     Pullback50      eq     $214.35  62.1   -1.37   50MA bounce (+|
|  GATX     Pullback50      eq     $179.95  45.6   -2.26   50MA bounce (+|
|  KRYS     Pullback50      eq     $343.31  39.8   -0.53   50MA bounce (-|
|  MUSA     Pullback50      eq     $581.22  41.2   -1.99   50MA bounce (+|
|  PVH      Pullback50      eq     $80.16   31.9   -2.81   50MA bounce (+|
|  SSD      Pullback50      eq     $193.20  57.2   -2.24   50MA bounce (-|
|  TOL      Pullback50      eq     $152.18  52.2   -2.10   50MA bounce (+|
|  UTHR     Pullback50      eq     $533.49  53.7   -1.88   50MA bounce (-|
|  VNO      Pullback50      eq     $38.80   42.8   -1.54   50MA bounce (-|
|  VC       Pullback50      eq     $106.74  56.7   -2.06   50MA bounce (-|
|                                                                        |
+========================================================================+

+========================================================================+
|                              ENTRY ORDERS                              |
+========================================================================+
|  Skipped                                  no entry slots (max_trades=0)|
+========================================================================+

+========================================================================+
|                            SESSION SUMMARY                             |
+========================================================================+
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Strategy  VolumeSpike + 52wkLow (display only — schedule not enforced)|
|  Scanned                                                            896|
|  Signals                                                             48|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  0 unconfirmed|
|  Exits                                                                0|
|  Open pos                                                             3|
|  Equity                                                         $464.81|
|  Cash                                                           $177.21|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T09:49:30.878049-04:00 share=50% ===
2026-08-19 09:49:30,878 INFO === options_live_micro LIVE 2026-08-19T09:49:30.878049-04:00 share=50% ===
Live account equity $464.81 cash $177.21 #225458845 options_level=3
2026-08-19 09:49:30,931 INFO Live account equity $464.81 cash $177.21 #225458845 options_level=3
Live micro hold S404 AVGO260821C00385000 -22.9% (tp +50% / sl -50%)
2026-08-19 09:49:30,949 INFO Live micro hold S404 AVGO260821C00385000 -22.9% (tp +50% / sl -50%)
Live micro sleeve $232 (50% of $465) deployed $54 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
2026-08-19 09:49:30,981 INFO Live micro sleeve $232 (50% of $465) deployed $54 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-19 09:49:30,981 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 3
2026-08-19 09:49:32,625 INFO Live micro signals: 3
  skip S404 AVGO: strategy already open (paper bucket rule)
2026-08-19 09:49:32,625 INFO   skip S404 AVGO: strategy already open (paper bucket rule)
  try S210 55%win/+47%med EOG
2026-08-19 09:49:32,626 INFO   try S210 55%win/+47%med EOG
  skip S210 EOG: no contract under $75
2026-08-19 09:49:32,738 INFO   skip S210 EOG: no contract under $75
  try S210 55%win/+47%med UNP
2026-08-19 09:49:32,738 INFO   try S210 55%win/+47%med UNP
  skip S210 UNP: no contract under $75
2026-08-19 09:49:32,788 INFO   skip S210 UNP: no contract under $75
Live micro done. open_options=1 lots=1
2026-08-19 09:49:32,816 INFO Live micro done. open_options=1 lots=1
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T135053Z

- UTC timestamp: `20260819T135053Z`
- GitHub run: [#7478](https://github.com/28twagg-ops/TradingBot/actions/runs/32260375246)
- Run id: `32260375246`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`3s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T135053Z_live_bot.log`, `logs/action_runs/20260819T135053Z_live_options.log`, `logs/action_runs/20260819T135053Z_options_bot.log`

### Live bot (tail)

```text
13:50:55  INFO      Mode: morning_scan
13:50:55  INFO      Morning scan already completed today (2026-08-19T13:49:30.014080Z) — exits-only pass
13:50:55  INFO        place_all_stops: checking 4 positions...
13:50:55  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
13:50:55  INFO        STOP skipped CDW: fractional (0.5749 shares) — software exit will handle it
13:50:55  INFO        STOP already live MNST @ $47.17
13:50:55  INFO        [positions] 3/3 (3 valid)
13:50:55  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_SCAN|
|  Time                                                         13:50 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $456.65|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CDW  P&L -0.1%  $-0.10                                            HOLD|
|  MNST  P&L +0.5%  $+0.35                                           HOLD|
|  AAPL  P&L +0.8%  $+0.64                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00385000     $0.70    $0.46    -34.3%   $-24.00   $46.00   |
|                                                                        |
|  Options open P&L                                               $-24.00|
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T09:50:56.310235-04:00 share=50% ===
2026-08-19 09:50:56,310 INFO === options_live_micro LIVE 2026-08-19T09:50:56.310235-04:00 share=50% ===
Live account equity $456.66 cash $177.21 #225458845 options_level=3
2026-08-19 09:50:56,377 INFO Live account equity $456.66 cash $177.21 #225458845 options_level=3
Live micro hold S404 AVGO260821C00385000 -34.3% (tp +50% / sl -50%)
2026-08-19 09:50:56,398 INFO Live micro hold S404 AVGO260821C00385000 -34.3% (tp +50% / sl -50%)
Live micro sleeve $228 (50% of $457) deployed $46 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
2026-08-19 09:50:56,426 INFO Live micro sleeve $228 (50% of $457) deployed $46 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-19 09:50:56,427 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 3
2026-08-19 09:50:58,357 INFO Live micro signals: 3
  skip S404 AVGO: strategy already open (paper bucket rule)
2026-08-19 09:50:58,358 INFO   skip S404 AVGO: strategy already open (paper bucket rule)
  try S210 55%win/+47%med EOG
2026-08-19 09:50:58,358 INFO   try S210 55%win/+47%med EOG
  skip S210 EOG: no contract under $75
2026-08-19 09:50:58,477 INFO   skip S210 EOG: no contract under $75
  try S210 55%win/+47%med UNP
2026-08-19 09:50:58,477 INFO   try S210 55%win/+47%med UNP
  skip S210 UNP: no contract under $75
2026-08-19 09:50:58,579 INFO   skip S210 UNP: no contract under $75
Live micro done. open_options=1 lots=1
2026-08-19 09:50:58,617 INFO Live micro done. open_options=1 lots=1
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T135551Z

- UTC timestamp: `20260819T135551Z`
- GitHub run: [#7479](https://github.com/28twagg-ops/TradingBot/actions/runs/32260875021)
- Run id: `32260875021`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`3s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T135551Z_live_bot.log`, `logs/action_runs/20260819T135551Z_live_options.log`, `logs/action_runs/20260819T135551Z_options_bot.log`

### Live bot (tail)

```text
13:55:52  INFO      Mode: morning_scan
13:55:53  INFO      Morning scan already completed today (2026-08-19T13:49:30.014080Z) — exits-only pass
13:55:53  INFO        place_all_stops: checking 4 positions...
13:55:53  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
13:55:53  INFO        STOP skipped CDW: fractional (0.5749 shares) — software exit will handle it
13:55:53  INFO        STOP already live MNST @ $47.17
13:55:53  INFO        [positions] 3/3 (3 valid)
13:55:53  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_SCAN|
|  Time                                                         13:55 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $451.18|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CDW  P&L -0.3%  $-0.23                                            HOLD|
|  MNST  P&L +0.6%  $+0.48                                           HOLD|
|  AAPL  P&L +1.5%  $+1.19                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00385000     $0.70    $0.40    -42.9%   $-30.00   $40.00   |
|                                                                        |
|  Options open P&L                                               $-30.00|
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T09:55:54.288669-04:00 share=50% ===
2026-08-19 09:55:54,288 INFO === options_live_micro LIVE 2026-08-19T09:55:54.288669-04:00 share=50% ===
Live account equity $451.18 cash $177.21 #225458845 options_level=3
2026-08-19 09:55:54,354 INFO Live account equity $451.18 cash $177.21 #225458845 options_level=3
Live micro hold S404 AVGO260821C00385000 -42.9% (tp +50% / sl -50%)
2026-08-19 09:55:54,380 INFO Live micro hold S404 AVGO260821C00385000 -42.9% (tp +50% / sl -50%)
Live micro sleeve $226 (50% of $451) deployed $40 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
2026-08-19 09:55:54,419 INFO Live micro sleeve $226 (50% of $451) deployed $40 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-19 09:55:54,420 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 3
2026-08-19 09:55:56,105 INFO Live micro signals: 3
  skip S404 AVGO: strategy already open (paper bucket rule)
2026-08-19 09:55:56,105 INFO   skip S404 AVGO: strategy already open (paper bucket rule)
  try S210 55%win/+47%med EOG
2026-08-19 09:55:56,105 INFO   try S210 55%win/+47%med EOG
  skip S210 EOG: no contract under $75
2026-08-19 09:55:56,313 INFO   skip S210 EOG: no contract under $75
  try S210 55%win/+47%med UNP
2026-08-19 09:55:56,314 INFO   try S210 55%win/+47%med UNP
  skip S210 UNP: no contract under $75
2026-08-19 09:55:56,646 INFO   skip S210 UNP: no contract under $75
Live micro done. open_options=1 lots=1
2026-08-19 09:55:56,695 INFO Live micro done. open_options=1 lots=1
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T140057Z

- UTC timestamp: `20260819T140057Z`
- GitHub run: [#7480](https://github.com/28twagg-ops/TradingBot/actions/runs/32261382408)
- Run id: `32261382408`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`5s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T140057Z_live_bot.log`, `logs/action_runs/20260819T140057Z_live_options.log`, `logs/action_runs/20260819T140057Z_options_bot.log`

### Live bot (tail)

```text
14:00:58  INFO      Mode: exits
14:00:59  INFO        place_all_stops: checking 4 positions...
14:00:59  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
14:00:59  INFO        STOP skipped CDW: fractional (0.5749 shares) — software exit will handle it
14:00:59  INFO        STOP already live MNST @ $47.17
14:00:59  INFO        [positions] 3/3 (3 valid)
14:00:59  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:00 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $448.21|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CDW  P&L -0.3%  $-0.27                                            HOLD|
|  MNST  P&L +0.4%  $+0.31                                           HOLD|
|  AAPL  P&L +1.8%  $+1.43                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00385000     $0.70    $0.37    -47.1%   $-33.00   $37.00   |
|                                                                        |
|  Options open P&L                                               $-33.00|
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T10:01:00.522819-04:00 share=50% ===
2026-08-19 10:01:00,522 INFO === options_live_micro LIVE 2026-08-19T10:01:00.522819-04:00 share=50% ===
Live account equity $448.27 cash $177.21 #225458845 options_level=3
2026-08-19 10:01:00,623 INFO Live account equity $448.27 cash $177.21 #225458845 options_level=3
Live micro hold S404 AVGO260821C00385000 -47.1% (tp +50% / sl -50%)
2026-08-19 10:01:00,669 INFO Live micro hold S404 AVGO260821C00385000 -47.1% (tp +50% / sl -50%)
Live micro sleeve $224 (50% of $448) deployed $37 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
2026-08-19 10:01:00,743 INFO Live micro sleeve $224 (50% of $448) deployed $37 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-19 10:01:00,743 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 3
2026-08-19 10:01:02,381 INFO Live micro signals: 3
  skip S404 AVGO: strategy already open (paper bucket rule)
2026-08-19 10:01:02,381 INFO   skip S404 AVGO: strategy already open (paper bucket rule)
  try S210 55%win/+47%med EOG
2026-08-19 10:01:02,382 INFO   try S210 55%win/+47%med EOG
  skip S210 EOG: no contract under $75
2026-08-19 10:01:03,292 INFO   skip S210 EOG: no contract under $75
  try S210 55%win/+47%med UNP
2026-08-19 10:01:03,292 INFO   try S210 55%win/+47%med UNP
  skip S210 UNP: no contract under $75
2026-08-19 10:01:04,136 INFO   skip S210 UNP: no contract under $75
Live micro done. open_options=1 lots=1
2026-08-19 10:01:04,210 INFO Live micro done. open_options=1 lots=1
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T141159Z

- UTC timestamp: `20260819T141159Z`
- GitHub run: [#7482](https://github.com/28twagg-ops/TradingBot/actions/runs/32262388816)
- Run id: `32262388816`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`3s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T141159Z_live_bot.log`, `logs/action_runs/20260819T141159Z_live_options.log`, `logs/action_runs/20260819T141159Z_options_bot.log`

### Live bot (tail)

```text
14:12:01  INFO      Mode: exits
14:12:01  INFO        place_all_stops: checking 3 positions...
14:12:01  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
14:12:01  INFO        STOP skipped CDW: fractional (0.5749 shares) — software exit will handle it
14:12:01  INFO        STOP already live MNST @ $47.17
14:12:02  INFO        [positions] 3/3 (3 valid)
14:12:02  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:12 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $445.06|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CDW  P&L +0.2%  $+0.17                                            HOLD|
|  MNST  P&L +0.8%  $+0.59                                           HOLD|
|  AAPL  P&L +2.0%  $+1.58                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T10:12:03.080519-04:00 share=50% ===
2026-08-19 10:12:03,080 INFO === options_live_micro LIVE 2026-08-19T10:12:03.080519-04:00 share=50% ===
Live account equity $445.09 cash $210.18 #225458845 options_level=3
2026-08-19 10:12:03,123 INFO Live account equity $445.09 cash $210.18 #225458845 options_level=3
Live micro reconcile: drop AVGO260821C00385000 S404 (not at broker)
2026-08-19 10:12:03,140 INFO Live micro reconcile: drop AVGO260821C00385000 S404 (not at broker)
Live micro sleeve $223 (50% of $445) deployed $0 open_strategies=0/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
2026-08-19 10:12:03,275 INFO Live micro sleeve $223 (50% of $445) deployed $0 open_strategies=0/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-19 10:12:03,276 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 3
2026-08-19 10:12:04,931 INFO Live micro signals: 3
  try S404 100%win/+80%med AVGO
2026-08-19 10:12:04,931 INFO   try S404 100%win/+80%med AVGO
LIVE BUY S404 100%win AVGO AVGO260821C00380000 limit=0.54 ask=0.55 cost=$55 id=8acba8f2-f296-4ac6-af64-e0ccdaed8e15
2026-08-19 10:12:05,134 INFO LIVE BUY S404 100%win AVGO AVGO260821C00380000 limit=0.54 ask=0.55 cost=$55 id=8acba8f2-f296-4ac6-af64-e0ccdaed8e15
  try S210 55%win/+47%med EOG
2026-08-19 10:12:05,134 INFO   try S210 55%win/+47%med EOG
  skip S210 EOG: no contract under $75
2026-08-19 10:12:05,226 INFO   skip S210 EOG: no contract under $75
  try S210 55%win/+47%med UNP
2026-08-19 10:12:05,227 INFO   try S210 55%win/+47%med UNP
  skip S210 UNP: no contract under $75
2026-08-19 10:12:05,294 INFO   skip S210 UNP: no contract under $75
LIVE PROT STOP AVGO260821C00380000 x1 stop=0.27 id=109d8dd8-d73a-4f0c-af81-4670eb875c8e
2026-08-19 10:12:05,355 INFO LIVE PROT STOP AVGO260821C00380000 x1 stop=0.27 id=109d8dd8-d73a-4f0c-af81-4670eb875c8e
Live micro done. open_options=1 lots=1
2026-08-19 10:12:05,376 INFO Live micro done. open_options=1 lots=1
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T141554Z

- UTC timestamp: `20260819T141554Z`
- GitHub run: [#7483](https://github.com/28twagg-ops/TradingBot/actions/runs/32262882653)
- Run id: `32262882653`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`3s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T141554Z_live_bot.log`, `logs/action_runs/20260819T141554Z_live_options.log`, `logs/action_runs/20260819T141554Z_options_bot.log`

### Live bot (tail)

```text
14:15:55  INFO      Mode: exits
14:15:56  INFO        place_all_stops: checking 4 positions...
14:15:56  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
14:15:56  INFO        STOP skipped CDW: fractional (0.5749 shares) — software exit will handle it
14:15:56  INFO        STOP already live MNST @ $47.17
14:15:56  INFO        [positions] 3/3 (3 valid)
14:15:56  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:15 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $437.88|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CDW  P&L -0.1%  $-0.05                                            HOLD|
|  MNST  P&L +0.7%  $+0.58                                           HOLD|
|  AAPL  P&L +2.2%  $+1.69                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00380000     $0.54    $0.47    -13.0%   $-7.00    $47.00   |
|                                                                        |
|  Options open P&L                                                $-7.00|
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T10:15:57.678310-04:00 share=50% ===
2026-08-19 10:15:57,678 INFO === options_live_micro LIVE 2026-08-19T10:15:57.678310-04:00 share=50% ===
Live account equity $437.98 cash $156.13 #225458845 options_level=3
2026-08-19 10:15:57,783 INFO Live account equity $437.98 cash $156.13 #225458845 options_level=3
Live micro hold S404 AVGO260821C00380000 -13.0% (tp +50% / sl -50%)
2026-08-19 10:15:57,855 INFO Live micro hold S404 AVGO260821C00380000 -13.0% (tp +50% / sl -50%)
Live micro sleeve $219 (50% of $438) deployed $47 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
2026-08-19 10:15:57,942 INFO Live micro sleeve $219 (50% of $438) deployed $47 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-19 10:15:57,942 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 3
2026-08-19 10:15:59,585 INFO Live micro signals: 3
  skip S404 AVGO: strategy already open (paper bucket rule)
2026-08-19 10:15:59,586 INFO   skip S404 AVGO: strategy already open (paper bucket rule)
  try S210 55%win/+47%med EOG
2026-08-19 10:15:59,586 INFO   try S210 55%win/+47%med EOG
  skip S210 EOG: no contract under $75
2026-08-19 10:15:59,947 INFO   skip S210 EOG: no contract under $75
  try S210 55%win/+47%med UNP
2026-08-19 10:15:59,948 INFO   try S210 55%win/+47%med UNP
  skip S210 UNP: no contract under $75
2026-08-19 10:16:00,168 INFO   skip S210 UNP: no contract under $75
Live micro done. open_options=1 lots=1
2026-08-19 10:16:00,304 INFO Live micro done. open_options=1 lots=1
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T142429Z

- UTC timestamp: `20260819T142429Z`
- GitHub run: [#7484](https://github.com/28twagg-ops/TradingBot/actions/runs/32263384118)
- Run id: `32263384118`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T142429Z_live_bot.log`, `logs/action_runs/20260819T142429Z_live_options.log`, `logs/action_runs/20260819T142429Z_options_bot.log`

### Live bot (tail)

```text
14:24:31  INFO      Mode: exits
14:24:32  INFO        place_all_stops: checking 4 positions...
14:24:32  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
14:24:32  INFO        STOP skipped CDW: fractional (0.5749 shares) — software exit will handle it
14:24:32  INFO        STOP already live MNST @ $47.17
14:24:32  INFO        [positions] 3/3 (3 valid)
14:24:32  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:24 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $433.36|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CDW  P&L -0.2%  $-0.15                                            HOLD|
|  MNST  P&L +0.6%  $+0.44                                           HOLD|
|  AAPL  P&L +1.8%  $+1.40                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00380000     $0.54    $0.43    -20.4%   $-11.00   $43.00   |
|                                                                        |
|  Options open P&L                                               $-11.00|
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T10:24:33.545207-04:00 share=50% ===
2026-08-19 10:24:33,545 INFO === options_live_micro LIVE 2026-08-19T10:24:33.545207-04:00 share=50% ===
Live account equity $433.35 cash $156.13 #225458845 options_level=3
2026-08-19 10:24:33,745 INFO Live account equity $433.35 cash $156.13 #225458845 options_level=3
Live micro hold S404 AVGO260821C00380000 -20.4% (tp +50% / sl -50%)
2026-08-19 10:24:33,847 INFO Live micro hold S404 AVGO260821C00380000 -20.4% (tp +50% / sl -50%)
Live micro sleeve $217 (50% of $433) deployed $43 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
2026-08-19 10:24:34,011 INFO Live micro sleeve $217 (50% of $433) deployed $43 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-19 10:24:34,011 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 3
2026-08-19 10:24:35,060 INFO Live micro signals: 3
  skip S404 AVGO: strategy already open (paper bucket rule)
2026-08-19 10:24:35,060 INFO   skip S404 AVGO: strategy already open (paper bucket rule)
  try S210 55%win/+47%med EOG
2026-08-19 10:24:35,060 INFO   try S210 55%win/+47%med EOG
  skip S210 EOG: no contract under $75
2026-08-19 10:24:35,498 INFO   skip S210 EOG: no contract under $75
  try S210 55%win/+47%med UNP
2026-08-19 10:24:35,498 INFO   try S210 55%win/+47%med UNP
  skip S210 UNP: no contract under $75
2026-08-19 10:24:35,642 INFO   skip S210 UNP: no contract under $75
Live micro done. open_options=1 lots=1
2026-08-19 10:24:35,869 INFO Live micro done. open_options=1 lots=1
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T143154Z

- UTC timestamp: `20260819T143154Z`
- GitHub run: [#7486](https://github.com/28twagg-ops/TradingBot/actions/runs/32264382210)
- Run id: `32264382210`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`4s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T143154Z_live_bot.log`, `logs/action_runs/20260819T143154Z_live_options.log`, `logs/action_runs/20260819T143154Z_options_bot.log`

### Live bot (tail)

```text
14:31:55  INFO      Mode: exits
14:31:56  INFO        place_all_stops: checking 4 positions...
14:31:56  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
14:31:56  INFO        STOP skipped CDW: fractional (0.5749 shares) — software exit will handle it
14:31:56  INFO        STOP already live MNST @ $47.17
14:31:56  INFO        [positions] 3/3 (3 valid)
14:31:57  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $430.01|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CDW  P&L -0.2%  $-0.12                                            HOLD|
|  MNST  P&L +0.0%  $+0.02                                           HOLD|
|  AAPL  P&L +1.9%  $+1.44                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00380000     $0.54    $0.40    -25.9%   $-14.00   $40.00   |
|                                                                        |
|  Options open P&L                                               $-14.00|
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T10:31:57.720227-04:00 share=50% ===
2026-08-19 10:31:57,720 INFO === options_live_micro LIVE 2026-08-19T10:31:57.720227-04:00 share=50% ===
Live account equity $430.01 cash $156.13 #225458845 options_level=3
2026-08-19 10:31:58,351 INFO Live account equity $430.01 cash $156.13 #225458845 options_level=3
Live micro hold S404 AVGO260821C00380000 -25.9% (tp +50% / sl -50%)
2026-08-19 10:31:58,524 INFO Live micro hold S404 AVGO260821C00380000 -25.9% (tp +50% / sl -50%)
Live micro sleeve $215 (50% of $430) deployed $40 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
2026-08-19 10:31:58,745 INFO Live micro sleeve $215 (50% of $430) deployed $40 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-19 10:31:58,745 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 3
2026-08-19 10:32:00,007 INFO Live micro signals: 3
  skip S404 AVGO: strategy already open (paper bucket rule)
2026-08-19 10:32:00,008 INFO   skip S404 AVGO: strategy already open (paper bucket rule)
  try S210 55%win/+47%med EOG
2026-08-19 10:32:00,008 INFO   try S210 55%win/+47%med EOG
  skip S210 EOG: no contract under $75
2026-08-19 10:32:00,825 INFO   skip S210 EOG: no contract under $75
  try S210 55%win/+47%med UNP
2026-08-19 10:32:00,825 INFO   try S210 55%win/+47%med UNP
  skip S210 UNP: no contract under $75
2026-08-19 10:32:01,373 INFO   skip S210 UNP: no contract under $75
Live micro done. open_options=1 lots=1
2026-08-19 10:32:01,624 INFO Live micro done. open_options=1 lots=1
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T143556Z

- UTC timestamp: `20260819T143556Z`
- GitHub run: [#7487](https://github.com/28twagg-ops/TradingBot/actions/runs/32264884949)
- Run id: `32264884949`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`3s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T143556Z_live_bot.log`, `logs/action_runs/20260819T143556Z_live_options.log`, `logs/action_runs/20260819T143556Z_options_bot.log`

### Live bot (tail)

```text
14:35:57  INFO      Mode: exits
14:35:58  INFO        place_all_stops: checking 4 positions...
14:35:58  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
14:35:58  INFO        STOP skipped CDW: fractional (0.5749 shares) — software exit will handle it
14:35:58  INFO        STOP already live MNST @ $47.17
14:35:58  INFO        [positions] 3/3 (3 valid)
14:35:58  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:35 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $430.24|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CDW  P&L +0.0%  $+0.03                                            HOLD|
|  MNST  P&L +0.0%  $+0.04                                           HOLD|
|  AAPL  P&L +1.9%  $+1.51                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00380000     $0.54    $0.40    -25.9%   $-14.00   $40.00   |
|                                                                        |
|  Options open P&L                                               $-14.00|
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T10:35:59.030380-04:00 share=50% ===
2026-08-19 10:35:59,030 INFO === options_live_micro LIVE 2026-08-19T10:35:59.030380-04:00 share=50% ===
Live account equity $430.24 cash $156.13 #225458845 options_level=3
2026-08-19 10:35:59,089 INFO Live account equity $430.24 cash $156.13 #225458845 options_level=3
Live micro hold S404 AVGO260821C00380000 -25.9% (tp +50% / sl -50%)
2026-08-19 10:35:59,104 INFO Live micro hold S404 AVGO260821C00380000 -25.9% (tp +50% / sl -50%)
Live micro sleeve $215 (50% of $430) deployed $40 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
2026-08-19 10:35:59,142 INFO Live micro sleeve $215 (50% of $430) deployed $40 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-19 10:35:59,142 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 3
2026-08-19 10:36:00,994 INFO Live micro signals: 3
  skip S404 AVGO: strategy already open (paper bucket rule)
2026-08-19 10:36:00,994 INFO   skip S404 AVGO: strategy already open (paper bucket rule)
  try S210 55%win/+47%med EOG
2026-08-19 10:36:00,994 INFO   try S210 55%win/+47%med EOG
  skip S210 EOG: no contract under $75
2026-08-19 10:36:01,320 INFO   skip S210 EOG: no contract under $75
  try S210 55%win/+47%med UNP
2026-08-19 10:36:01,320 INFO   try S210 55%win/+47%med UNP
  skip S210 UNP: no contract under $75
2026-08-19 10:36:01,621 INFO   skip S210 UNP: no contract under $75
Live micro done. open_options=1 lots=1
2026-08-19 10:36:01,663 INFO Live micro done. open_options=1 lots=1
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T144117Z

- UTC timestamp: `20260819T144117Z`
- GitHub run: [#7488](https://github.com/28twagg-ops/TradingBot/actions/runs/32265379373)
- Run id: `32265379373`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`5s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T144117Z_live_bot.log`, `logs/action_runs/20260819T144117Z_live_options.log`, `logs/action_runs/20260819T144117Z_options_bot.log`

### Live bot (tail)

```text
14:41:18  INFO      Mode: exits
14:41:19  INFO        place_all_stops: checking 4 positions...
14:41:19  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
14:41:19  INFO        STOP skipped CDW: fractional (0.5749 shares) — software exit will handle it
14:41:19  INFO        STOP already live MNST @ $47.17
14:41:20  INFO        [positions] 3/3 (3 valid)
14:41:20  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $433.17|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.0%  $+0.00                                           HOLD|
|  CDW  P&L +0.1%  $+0.09                                            HOLD|
|  AAPL  P&L +1.8%  $+1.41                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00380000     $0.54    $0.43    -20.4%   $-11.00   $43.00   |
|                                                                        |
|  Options open P&L                                               $-11.00|
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T10:41:21.589157-04:00 share=50% ===
2026-08-19 10:41:21,589 INFO === options_live_micro LIVE 2026-08-19T10:41:21.589157-04:00 share=50% ===
Live account equity $433.18 cash $156.13 #225458845 options_level=3
2026-08-19 10:41:22,007 INFO Live account equity $433.18 cash $156.13 #225458845 options_level=3
Live micro hold S404 AVGO260821C00380000 -20.4% (tp +50% / sl -50%)
2026-08-19 10:41:22,197 INFO Live micro hold S404 AVGO260821C00380000 -20.4% (tp +50% / sl -50%)
Live micro sleeve $217 (50% of $433) deployed $43 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
2026-08-19 10:41:22,423 INFO Live micro sleeve $217 (50% of $433) deployed $43 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-19 10:41:22,423 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 3
2026-08-19 10:41:24,307 INFO Live micro signals: 3
  skip S404 AVGO: strategy already open (paper bucket rule)
2026-08-19 10:41:24,307 INFO   skip S404 AVGO: strategy already open (paper bucket rule)
  try S210 55%win/+47%med EOG
2026-08-19 10:41:24,307 INFO   try S210 55%win/+47%med EOG
  skip S210 EOG: no contract under $75
2026-08-19 10:41:24,844 INFO   skip S210 EOG: no contract under $75
  try S210 55%win/+47%med UNP
2026-08-19 10:41:24,844 INFO   try S210 55%win/+47%med UNP
  skip S210 UNP: no contract under $75
2026-08-19 10:41:25,145 INFO   skip S210 UNP: no contract under $75
Live micro done. open_options=1 lots=1
2026-08-19 10:41:25,444 INFO Live micro done. open_options=1 lots=1
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T144555Z

- UTC timestamp: `20260819T144555Z`
- GitHub run: [#7489](https://github.com/28twagg-ops/TradingBot/actions/runs/32265876489)
- Run id: `32265876489`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`5s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T144555Z_live_bot.log`, `logs/action_runs/20260819T144555Z_live_options.log`, `logs/action_runs/20260819T144555Z_options_bot.log`

### Live bot (tail)

```text
14:45:56  INFO      Mode: exits
14:45:56  INFO        place_all_stops: checking 4 positions...
14:45:56  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
14:45:56  INFO        STOP skipped CDW: fractional (0.5749 shares) — software exit will handle it
14:45:56  INFO        STOP already live MNST @ $47.17
14:45:57  INFO        [positions] 3/3 (3 valid)
14:45:58  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:45 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $437.37|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CDW  P&L +0.1%  $+0.08                                            HOLD|
|  MNST  P&L +0.3%  $+0.23                                           HOLD|
|  AAPL  P&L +1.8%  $+1.38                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00380000     $0.54    $0.47    -13.0%   $-7.00    $47.00   |
|                                                                        |
|  Options open P&L                                                $-7.00|
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T10:45:58.985414-04:00 share=50% ===
2026-08-19 10:45:58,985 INFO === options_live_micro LIVE 2026-08-19T10:45:58.985414-04:00 share=50% ===
Live account equity $437.37 cash $156.13 #225458845 options_level=3
2026-08-19 10:45:59,218 INFO Live account equity $437.37 cash $156.13 #225458845 options_level=3
Live micro hold S404 AVGO260821C00380000 -13.0% (tp +50% / sl -50%)
2026-08-19 10:45:59,421 INFO Live micro hold S404 AVGO260821C00380000 -13.0% (tp +50% / sl -50%)
Live micro sleeve $219 (50% of $437) deployed $47 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
2026-08-19 10:45:59,637 INFO Live micro sleeve $219 (50% of $437) deployed $47 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-19 10:45:59,637 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 3
2026-08-19 10:46:01,552 INFO Live micro signals: 3
  skip S404 AVGO: strategy already open (paper bucket rule)
2026-08-19 10:46:01,553 INFO   skip S404 AVGO: strategy already open (paper bucket rule)
  try S210 55%win/+47%med EOG
2026-08-19 10:46:01,553 INFO   try S210 55%win/+47%med EOG
  skip S210 EOG: no contract under $75
2026-08-19 10:46:02,362 INFO   skip S210 EOG: no contract under $75
  try S210 55%win/+47%med UNP
2026-08-19 10:46:02,362 INFO   try S210 55%win/+47%med UNP
  skip S210 UNP: no contract under $75
2026-08-19 10:46:02,840 INFO   skip S210 UNP: no contract under $75
Live micro done. open_options=1 lots=1
2026-08-19 10:46:03,064 INFO Live micro done. open_options=1 lots=1
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T145054Z

- UTC timestamp: `20260819T145054Z`
- GitHub run: [#7490](https://github.com/28twagg-ops/TradingBot/actions/runs/32266378904)
- Run id: `32266378904`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`4s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T145054Z_live_bot.log`, `logs/action_runs/20260819T145054Z_live_options.log`, `logs/action_runs/20260819T145054Z_options_bot.log`

### Live bot (tail)

```text
14:50:55  INFO      Mode: exits
14:50:56  INFO        place_all_stops: checking 4 positions...
14:50:56  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
14:50:56  INFO        STOP skipped CDW: fractional (0.5749 shares) — software exit will handle it
14:50:56  INFO        STOP already live MNST @ $47.17
14:50:56  INFO        [positions] 3/3 (3 valid)
14:50:57  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:50 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $439.29|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.0%  $+0.04                                           HOLD|
|  CDW  P&L +0.1%  $+0.05                                            HOLD|
|  AAPL  P&L +2.0%  $+1.53                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00380000     $0.54    $0.49    -9.3%    $-5.00    $49.00   |
|                                                                        |
|  Options open P&L                                                $-5.00|
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T10:50:57.978280-04:00 share=50% ===
2026-08-19 10:50:57,978 INFO === options_live_micro LIVE 2026-08-19T10:50:57.978280-04:00 share=50% ===
Live account equity $439.28 cash $156.13 #225458845 options_level=3
2026-08-19 10:50:58,238 INFO Live account equity $439.28 cash $156.13 #225458845 options_level=3
Live micro hold S404 AVGO260821C00380000 -9.3% (tp +50% / sl -50%)
2026-08-19 10:50:58,394 INFO Live micro hold S404 AVGO260821C00380000 -9.3% (tp +50% / sl -50%)
Live micro sleeve $220 (50% of $439) deployed $49 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
2026-08-19 10:50:58,636 INFO Live micro sleeve $220 (50% of $439) deployed $49 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-19 10:50:58,636 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 3
2026-08-19 10:51:00,555 INFO Live micro signals: 3
  skip S404 AVGO: strategy already open (paper bucket rule)
2026-08-19 10:51:00,556 INFO   skip S404 AVGO: strategy already open (paper bucket rule)
  try S210 55%win/+47%med EOG
2026-08-19 10:51:00,556 INFO   try S210 55%win/+47%med EOG
  skip S210 EOG: no contract under $75
2026-08-19 10:51:01,180 INFO   skip S210 EOG: no contract under $75
  try S210 55%win/+47%med UNP
2026-08-19 10:51:01,180 INFO   try S210 55%win/+47%med UNP
  skip S210 UNP: no contract under $75
2026-08-19 10:51:01,517 INFO   skip S210 UNP: no contract under $75
Live micro done. open_options=1 lots=1
2026-08-19 10:51:01,808 INFO Live micro done. open_options=1 lots=1
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T145557Z

- UTC timestamp: `20260819T145557Z`
- GitHub run: [#7491](https://github.com/28twagg-ops/TradingBot/actions/runs/32266888765)
- Run id: `32266888765`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`3s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T145557Z_live_bot.log`, `logs/action_runs/20260819T145557Z_live_options.log`, `logs/action_runs/20260819T145557Z_options_bot.log`

### Live bot (tail)

```text
14:55:59  INFO      Mode: exits
14:55:59  INFO        place_all_stops: checking 4 positions...
14:55:59  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
14:55:59  INFO        STOP skipped CDW: fractional (0.5749 shares) — software exit will handle it
14:55:59  INFO        STOP already live MNST @ $47.17
14:56:00  INFO        [positions] 3/3 (3 valid)
14:56:01  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:55 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $448.67|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.1%  $+0.07                                           HOLD|
|  CDW  P&L +0.2%  $+0.18                                            HOLD|
|  AAPL  P&L +2.3%  $+1.75                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00380000     $0.54    $0.60    +11.1%   $+6.00    $60.00   |
|                                                                        |
|  Options open P&L                                                $+6.00|
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T10:56:01.728362-04:00 share=50% ===
2026-08-19 10:56:01,728 INFO === options_live_micro LIVE 2026-08-19T10:56:01.728362-04:00 share=50% ===
Live account equity $450.67 cash $156.13 #225458845 options_level=3
2026-08-19 10:56:01,937 INFO Live account equity $450.67 cash $156.13 #225458845 options_level=3
Live micro hold S404 AVGO260821C00380000 +11.1% (tp +50% / sl -50%)
2026-08-19 10:56:02,138 INFO Live micro hold S404 AVGO260821C00380000 +11.1% (tp +50% / sl -50%)
Live micro sleeve $225 (50% of $451) deployed $60 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
2026-08-19 10:56:02,356 INFO Live micro sleeve $225 (50% of $451) deployed $60 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-19 10:56:02,356 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 3
2026-08-19 10:56:03,705 INFO Live micro signals: 3
  skip S404 AVGO: strategy already open (paper bucket rule)
2026-08-19 10:56:03,705 INFO   skip S404 AVGO: strategy already open (paper bucket rule)
  try S210 55%win/+47%med EOG
2026-08-19 10:56:03,705 INFO   try S210 55%win/+47%med EOG
  skip S210 EOG: no contract under $75
2026-08-19 10:56:04,285 INFO   skip S210 EOG: no contract under $75
  try S210 55%win/+47%med UNP
2026-08-19 10:56:04,286 INFO   try S210 55%win/+47%med UNP
  skip S210 UNP: no contract under $75
2026-08-19 10:56:04,468 INFO   skip S210 UNP: no contract under $75
Live micro done. open_options=1 lots=1
2026-08-19 10:56:04,685 INFO Live micro done. open_options=1 lots=1
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T150059Z

- UTC timestamp: `20260819T150059Z`
- GitHub run: [#7492](https://github.com/28twagg-ops/TradingBot/actions/runs/32267395651)
- Run id: `32267395651`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`4s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T150059Z_live_bot.log`, `logs/action_runs/20260819T150059Z_live_options.log`, `logs/action_runs/20260819T150059Z_options_bot.log`

### Live bot (tail)

```text
15:01:00  INFO      Mode: exits
15:01:01  INFO        place_all_stops: checking 4 positions...
15:01:01  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
15:01:01  INFO        STOP skipped CDW: fractional (0.5749 shares) — software exit will handle it
15:01:01  INFO        STOP already live MNST @ $47.17
15:01:02  INFO        [positions] 3/3 (3 valid)
15:01:02  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $445.89|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.1%  $+0.09                                           HOLD|
|  CDW  P&L +0.3%  $+0.25                                            HOLD|
|  AAPL  P&L +2.5%  $+1.91                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00380000     $0.54    $0.55    +1.9%    $+1.00    $55.00   |
|                                                                        |
|  Options open P&L                                                $+1.00|
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T11:01:03.201195-04:00 share=50% ===
2026-08-19 11:01:03,201 INFO === options_live_micro LIVE 2026-08-19T11:01:03.201195-04:00 share=50% ===
Live account equity $445.93 cash $156.13 #225458845 options_level=3
2026-08-19 11:01:03,300 INFO Live account equity $445.93 cash $156.13 #225458845 options_level=3
Live micro hold S404 AVGO260821C00380000 +1.9% (tp +50% / sl -50%)
2026-08-19 11:01:03,357 INFO Live micro hold S404 AVGO260821C00380000 +1.9% (tp +50% / sl -50%)
Live micro sleeve $223 (50% of $446) deployed $55 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
2026-08-19 11:01:03,427 INFO Live micro sleeve $223 (50% of $446) deployed $55 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-19 11:01:03,427 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 3
2026-08-19 11:01:05,343 INFO Live micro signals: 3
  skip S404 AVGO: strategy already open (paper bucket rule)
2026-08-19 11:01:05,343 INFO   skip S404 AVGO: strategy already open (paper bucket rule)
  try S210 55%win/+47%med EOG
2026-08-19 11:01:05,343 INFO   try S210 55%win/+47%med EOG
  skip S210 EOG: no contract under $75
2026-08-19 11:01:06,057 INFO   skip S210 EOG: no contract under $75
  try S210 55%win/+47%med UNP
2026-08-19 11:01:06,057 INFO   try S210 55%win/+47%med UNP
  skip S210 UNP: no contract under $75
2026-08-19 11:01:06,553 INFO   skip S210 UNP: no contract under $75
Live micro done. open_options=1 lots=1
2026-08-19 11:01:06,667 INFO Live micro done. open_options=1 lots=1
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T150559Z

- UTC timestamp: `20260819T150559Z`
- GitHub run: [#7493](https://github.com/28twagg-ops/TradingBot/actions/runs/32267900924)
- Run id: `32267900924`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`5s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T150559Z_live_bot.log`, `logs/action_runs/20260819T150559Z_live_options.log`, `logs/action_runs/20260819T150559Z_options_bot.log`

### Live bot (tail)

```text
15:06:01  INFO      Mode: exits
15:06:02  INFO        place_all_stops: checking 4 positions...
15:06:02  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
15:06:02  INFO        STOP skipped CDW: fractional (0.5749 shares) — software exit will handle it
15:06:02  INFO        STOP already live MNST @ $47.17
15:06:02  INFO        [positions] 3/3 (3 valid)
15:06:03  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $441.15|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CDW  P&L +0.1%  $+0.05                                            HOLD|
|  MNST  P&L +0.4%  $+0.30                                           HOLD|
|  AAPL  P&L +2.8%  $+2.14                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00380000     $0.54    $0.50    -7.4%    $-4.00    $50.00   |
|                                                                        |
|  Options open P&L                                                $-4.00|
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T11:06:04.216128-04:00 share=50% ===
2026-08-19 11:06:04,216 INFO === options_live_micro LIVE 2026-08-19T11:06:04.216128-04:00 share=50% ===
Live account equity $441.17 cash $156.13 #225458845 options_level=3
2026-08-19 11:06:04,443 INFO Live account equity $441.17 cash $156.13 #225458845 options_level=3
Live micro hold S404 AVGO260821C00380000 -7.4% (tp +50% / sl -50%)
2026-08-19 11:06:04,585 INFO Live micro hold S404 AVGO260821C00380000 -7.4% (tp +50% / sl -50%)
Live micro sleeve $221 (50% of $441) deployed $50 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
2026-08-19 11:06:04,801 INFO Live micro sleeve $221 (50% of $441) deployed $50 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-19 11:06:04,801 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 3
2026-08-19 11:06:06,666 INFO Live micro signals: 3
  skip S404 AVGO: strategy already open (paper bucket rule)
2026-08-19 11:06:06,666 INFO   skip S404 AVGO: strategy already open (paper bucket rule)
  try S210 55%win/+47%med EOG
2026-08-19 11:06:06,666 INFO   try S210 55%win/+47%med EOG
  skip S210 EOG: no contract under $75
2026-08-19 11:06:07,340 INFO   skip S210 EOG: no contract under $75
  try S210 55%win/+47%med UNP
2026-08-19 11:06:07,340 INFO   try S210 55%win/+47%med UNP
  skip S210 UNP: no contract under $75
2026-08-19 11:06:07,710 INFO   skip S210 UNP: no contract under $75
Live micro done. open_options=1 lots=1
2026-08-19 11:06:07,917 INFO Live micro done. open_options=1 lots=1
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T151112Z

- UTC timestamp: `20260819T151112Z`
- GitHub run: [#7494](https://github.com/28twagg-ops/TradingBot/actions/runs/32268402217)
- Run id: `32268402217`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`4s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T151112Z_live_bot.log`, `logs/action_runs/20260819T151112Z_live_options.log`, `logs/action_runs/20260819T151112Z_options_bot.log`

### Live bot (tail)

```text
15:11:15  INFO      Mode: exits
15:11:16  INFO        place_all_stops: checking 4 positions...
15:11:16  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
15:11:16  INFO        STOP skipped CDW: fractional (0.5749 shares) — software exit will handle it
15:11:16  INFO        STOP already live MNST @ $47.17
15:11:17  INFO        [positions] 3/3 (3 valid)
15:11:17  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $441.02|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.2%  $+0.15                                           HOLD|
|  CDW  P&L +0.3%  $+0.19                                            HOLD|
|  AAPL  P&L +2.6%  $+1.98                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00380000     $0.54    $0.50    -7.4%    $-4.00    $50.00   |
|                                                                        |
|  Options open P&L                                                $-4.00|
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T11:11:18.342120-04:00 share=50% ===
2026-08-19 11:11:18,342 INFO === options_live_micro LIVE 2026-08-19T11:11:18.342120-04:00 share=50% ===
Live account equity $440.87 cash $156.13 #225458845 options_level=3
2026-08-19 11:11:18,571 INFO Live account equity $440.87 cash $156.13 #225458845 options_level=3
Live micro hold S404 AVGO260821C00380000 -7.4% (tp +50% / sl -50%)
2026-08-19 11:11:18,750 INFO Live micro hold S404 AVGO260821C00380000 -7.4% (tp +50% / sl -50%)
Live micro sleeve $220 (50% of $441) deployed $50 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
2026-08-19 11:11:18,990 INFO Live micro sleeve $220 (50% of $441) deployed $50 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-19 11:11:18,990 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 3
2026-08-19 11:11:20,266 INFO Live micro signals: 3
  skip S404 AVGO: strategy already open (paper bucket rule)
2026-08-19 11:11:20,266 INFO   skip S404 AVGO: strategy already open (paper bucket rule)
  try S210 55%win/+47%med EOG
2026-08-19 11:11:20,266 INFO   try S210 55%win/+47%med EOG
  skip S210 EOG: no contract under $75
2026-08-19 11:11:20,814 INFO   skip S210 EOG: no contract under $75
  try S210 55%win/+47%med UNP
2026-08-19 11:11:20,814 INFO   try S210 55%win/+47%med UNP
  skip S210 UNP: no contract under $75
2026-08-19 11:11:21,183 INFO   skip S210 UNP: no contract under $75
Live micro done. open_options=1 lots=1
2026-08-19 11:11:21,407 INFO Live micro done. open_options=1 lots=1
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T151556Z

- UTC timestamp: `20260819T151556Z`
- GitHub run: [#7495](https://github.com/28twagg-ops/TradingBot/actions/runs/32268914437)
- Run id: `32268914437`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`5s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T151556Z_live_bot.log`, `logs/action_runs/20260819T151556Z_live_options.log`, `logs/action_runs/20260819T151556Z_options_bot.log`

### Live bot (tail)

```text
15:15:57  INFO      Mode: exits
15:15:58  INFO        place_all_stops: checking 4 positions...
15:15:58  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
15:15:58  INFO        STOP skipped CDW: fractional (0.5749 shares) — software exit will handle it
15:15:58  INFO        STOP already live MNST @ $47.17
15:15:59  INFO        [positions] 3/3 (3 valid)
15:15:59  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:15 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $443.08|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.2%  $+0.17                                           HOLD|
|  CDW  P&L +0.2%  $+0.19                                            HOLD|
|  AAPL  P&L +2.6%  $+2.05                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00380000     $0.54    $0.52    -3.7%    $-2.00    $52.00   |
|                                                                        |
|  Options open P&L                                                $-2.00|
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T11:16:00.372815-04:00 share=50% ===
2026-08-19 11:16:00,372 INFO === options_live_micro LIVE 2026-08-19T11:16:00.372815-04:00 share=50% ===
Live account equity $443.08 cash $156.13 #225458845 options_level=3
2026-08-19 11:16:00,642 INFO Live account equity $443.08 cash $156.13 #225458845 options_level=3
Live micro hold S404 AVGO260821C00380000 -3.7% (tp +50% / sl -50%)
2026-08-19 11:16:00,817 INFO Live micro hold S404 AVGO260821C00380000 -3.7% (tp +50% / sl -50%)
Live micro sleeve $222 (50% of $443) deployed $52 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
2026-08-19 11:16:01,076 INFO Live micro sleeve $222 (50% of $443) deployed $52 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-19 11:16:01,076 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 3
2026-08-19 11:16:03,005 INFO Live micro signals: 3
  skip S404 AVGO: strategy already open (paper bucket rule)
2026-08-19 11:16:03,005 INFO   skip S404 AVGO: strategy already open (paper bucket rule)
  try S210 55%win/+47%med EOG
2026-08-19 11:16:03,005 INFO   try S210 55%win/+47%med EOG
  skip S210 EOG: no contract under $75
2026-08-19 11:16:03,826 INFO   skip S210 EOG: no contract under $75
  try S210 55%win/+47%med UNP
2026-08-19 11:16:03,826 INFO   try S210 55%win/+47%med UNP
  skip S210 UNP: no contract under $75
2026-08-19 11:16:04,451 INFO   skip S210 UNP: no contract under $75
Live micro done. open_options=1 lots=1
2026-08-19 11:16:04,679 INFO Live micro done. open_options=1 lots=1
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T152053Z

- UTC timestamp: `20260819T152053Z`
- GitHub run: [#7496](https://github.com/28twagg-ops/TradingBot/actions/runs/32269414327)
- Run id: `32269414327`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`5s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T152053Z_live_bot.log`, `logs/action_runs/20260819T152053Z_live_options.log`, `logs/action_runs/20260819T152053Z_options_bot.log`

### Live bot (tail)

```text
15:20:54  INFO      Mode: exits
15:20:55  INFO        place_all_stops: checking 4 positions...
15:20:55  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
15:20:55  INFO        STOP skipped CDW: fractional (0.5749 shares) — software exit will handle it
15:20:55  INFO        STOP already live MNST @ $47.17
15:20:55  INFO        [positions] 3/3 (3 valid)
15:20:56  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $452.13|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CDW  P&L +0.2%  $+0.13                                            HOLD|
|  MNST  P&L +0.4%  $+0.30                                           HOLD|
|  AAPL  P&L +2.6%  $+2.03                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00380000     $0.54    $0.61    +13.0%   $+7.00    $61.00   |
|                                                                        |
|  Options open P&L                                                $+7.00|
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T11:20:57.061530-04:00 share=50% ===
2026-08-19 11:20:57,061 INFO === options_live_micro LIVE 2026-08-19T11:20:57.061530-04:00 share=50% ===
Live account equity $452.13 cash $156.13 #225458845 options_level=3
2026-08-19 11:20:57,300 INFO Live account equity $452.13 cash $156.13 #225458845 options_level=3
Live micro hold S404 AVGO260821C00380000 +13.0% (tp +50% / sl -50%)
2026-08-19 11:20:57,445 INFO Live micro hold S404 AVGO260821C00380000 +13.0% (tp +50% / sl -50%)
Live micro sleeve $226 (50% of $452) deployed $61 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
2026-08-19 11:20:57,661 INFO Live micro sleeve $226 (50% of $452) deployed $61 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-19 11:20:57,661 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 3
2026-08-19 11:20:59,529 INFO Live micro signals: 3
  skip S404 AVGO: strategy already open (paper bucket rule)
2026-08-19 11:20:59,529 INFO   skip S404 AVGO: strategy already open (paper bucket rule)
  try S210 55%win/+47%med EOG
2026-08-19 11:20:59,530 INFO   try S210 55%win/+47%med EOG
  skip S210 EOG: no contract under $75
2026-08-19 11:21:00,584 INFO   skip S210 EOG: no contract under $75
  try S210 55%win/+47%med UNP
2026-08-19 11:21:00,584 INFO   try S210 55%win/+47%med UNP
  skip S210 UNP: no contract under $75
2026-08-19 11:21:01,019 INFO   skip S210 UNP: no contract under $75
Live micro done. open_options=1 lots=1
2026-08-19 11:21:01,237 INFO Live micro done. open_options=1 lots=1
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T153004Z

- UTC timestamp: `20260819T153004Z`
- GitHub run: [#7497](https://github.com/28twagg-ops/TradingBot/actions/runs/32269917469)
- Run id: `32269917469`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`5s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T153004Z_live_bot.log`, `logs/action_runs/20260819T153004Z_live_options.log`, `logs/action_runs/20260819T153004Z_options_bot.log`

### Live bot (tail)

```text
15:30:05  INFO      Mode: exits
15:30:06  INFO        place_all_stops: checking 4 positions...
15:30:06  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
15:30:06  INFO        STOP skipped CDW: fractional (0.5749 shares) — software exit will handle it
15:30:06  INFO        STOP already live MNST @ $47.17
15:30:06  INFO        [positions] 3/3 (3 valid)
15:30:06  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:30 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $454.63|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CDW  P&L -0.1%  $-0.08                                            HOLD|
|  MNST  P&L +0.2%  $+0.14                                           HOLD|
|  AAPL  P&L +2.4%  $+1.90                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00380000     $0.54    $0.62    +14.8%   $+8.00    $62.00   |
|                                                                        |
|  Options open P&L                                                $+8.00|
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T11:30:07.554102-04:00 share=50% ===
2026-08-19 11:30:07,554 INFO === options_live_micro LIVE 2026-08-19T11:30:07.554102-04:00 share=50% ===
Live account equity $452.62 cash $156.13 #225458845 options_level=3
2026-08-19 11:30:07,660 INFO Live account equity $452.62 cash $156.13 #225458845 options_level=3
Live micro hold S404 AVGO260821C00380000 +14.8% (tp +50% / sl -50%)
2026-08-19 11:30:07,726 INFO Live micro hold S404 AVGO260821C00380000 +14.8% (tp +50% / sl -50%)
Live micro sleeve $226 (50% of $453) deployed $62 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
2026-08-19 11:30:07,821 INFO Live micro sleeve $226 (50% of $453) deployed $62 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-19 11:30:07,821 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 3
2026-08-19 11:30:09,447 INFO Live micro signals: 3
  skip S404 AVGO: strategy already open (paper bucket rule)
2026-08-19 11:30:09,448 INFO   skip S404 AVGO: strategy already open (paper bucket rule)
  try S210 55%win/+47%med EOG
2026-08-19 11:30:09,448 INFO   try S210 55%win/+47%med EOG
  skip S210 EOG: no contract under $75
2026-08-19 11:30:10,242 INFO   skip S210 EOG: no contract under $75
  try S210 55%win/+47%med UNP
2026-08-19 11:30:10,242 INFO   try S210 55%win/+47%med UNP
  skip S210 UNP: no contract under $75
2026-08-19 11:30:10,943 INFO   skip S210 UNP: no contract under $75
Live micro done. open_options=1 lots=1
2026-08-19 11:30:11,048 INFO Live micro done. open_options=1 lots=1
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T153212Z

- UTC timestamp: `20260819T153212Z`
- GitHub run: [#7498](https://github.com/28twagg-ops/TradingBot/actions/runs/32270419308)
- Run id: `32270419308`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`4s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T153212Z_live_bot.log`, `logs/action_runs/20260819T153212Z_live_options.log`, `logs/action_runs/20260819T153212Z_options_bot.log`

### Live bot (tail)

```text
15:32:13  INFO      Mode: exits
15:32:14  INFO        place_all_stops: checking 4 positions...
15:32:14  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
15:32:14  INFO        STOP skipped CDW: fractional (0.5749 shares) — software exit will handle it
15:32:14  INFO        STOP already live MNST @ $47.17
15:32:14  INFO        [positions] 3/3 (3 valid)
15:32:15  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:32 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $452.57|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CDW  P&L -0.0%  $-0.00                                            HOLD|
|  MNST  P&L +0.2%  $+0.12                                           HOLD|
|  AAPL  P&L +2.3%  $+1.78                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00380000     $0.54    $0.62    +14.8%   $+8.00    $62.00   |
|                                                                        |
|  Options open P&L                                                $+8.00|
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T11:32:16.001255-04:00 share=50% ===
2026-08-19 11:32:16,001 INFO === options_live_micro LIVE 2026-08-19T11:32:16.001255-04:00 share=50% ===
Live account equity $452.57 cash $156.13 #225458845 options_level=3
2026-08-19 11:32:16,208 INFO Live account equity $452.57 cash $156.13 #225458845 options_level=3
Live micro hold S404 AVGO260821C00380000 +14.8% (tp +50% / sl -50%)
2026-08-19 11:32:16,321 INFO Live micro hold S404 AVGO260821C00380000 +14.8% (tp +50% / sl -50%)
Live micro sleeve $226 (50% of $453) deployed $62 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
2026-08-19 11:32:16,517 INFO Live micro sleeve $226 (50% of $453) deployed $62 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-19 11:32:16,517 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 3
2026-08-19 11:32:18,434 INFO Live micro signals: 3
  skip S404 AVGO: strategy already open (paper bucket rule)
2026-08-19 11:32:18,434 INFO   skip S404 AVGO: strategy already open (paper bucket rule)
  try S210 55%win/+47%med EOG
2026-08-19 11:32:18,434 INFO   try S210 55%win/+47%med EOG
  skip S210 EOG: no contract under $75
2026-08-19 11:32:18,925 INFO   skip S210 EOG: no contract under $75
  try S210 55%win/+47%med UNP
2026-08-19 11:32:18,925 INFO   try S210 55%win/+47%med UNP
  skip S210 UNP: no contract under $75
2026-08-19 11:32:19,187 INFO   skip S210 UNP: no contract under $75
Live micro done. open_options=1 lots=1
2026-08-19 11:32:19,349 INFO Live micro done. open_options=1 lots=1
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T153552Z

- UTC timestamp: `20260819T153552Z`
- GitHub run: [#7499](https://github.com/28twagg-ops/TradingBot/actions/runs/32270924950)
- Run id: `32270924950`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T153552Z_live_bot.log`, `logs/action_runs/20260819T153552Z_live_options.log`, `logs/action_runs/20260819T153552Z_options_bot.log`

### Live bot (tail)

```text
15:35:53  INFO      Mode: exits
15:35:53  INFO        place_all_stops: checking 4 positions...
15:35:53  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
15:35:53  INFO        STOP skipped CDW: fractional (0.5749 shares) — software exit will handle it
15:35:53  INFO        STOP already live MNST @ $47.17
15:35:54  INFO        [positions] 3/3 (3 valid)
15:35:54  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:35 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $452.35|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CDW  P&L -0.1%  $-0.08                                            HOLD|
|  MNST  P&L +0.1%  $+0.10                                           HOLD|
|  AAPL  P&L +2.1%  $+1.67                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00380000     $0.54    $0.62    +14.8%   $+8.00    $62.00   |
|                                                                        |
|  Options open P&L                                                $+8.00|
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T11:35:54.858229-04:00 share=50% ===
2026-08-19 11:35:54,858 INFO === options_live_micro LIVE 2026-08-19T11:35:54.858229-04:00 share=50% ===
Live account equity $452.36 cash $156.13 #225458845 options_level=3
2026-08-19 11:35:54,899 INFO Live account equity $452.36 cash $156.13 #225458845 options_level=3
Live micro hold S404 AVGO260821C00380000 +14.8% (tp +50% / sl -50%)
2026-08-19 11:35:54,915 INFO Live micro hold S404 AVGO260821C00380000 +14.8% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-19 11:35:54,939 INFO Live micro: manage/exits only
Live micro done. open_options=1 lots=1
2026-08-19 11:35:54,947 INFO Live micro done. open_options=1 lots=1
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T154057Z

- UTC timestamp: `20260819T154057Z`
- GitHub run: [#7500](https://github.com/28twagg-ops/TradingBot/actions/runs/32271419883)
- Run id: `32271419883`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T154057Z_live_bot.log`, `logs/action_runs/20260819T154057Z_live_options.log`, `logs/action_runs/20260819T154057Z_options_bot.log`

### Live bot (tail)

```text
15:40:58  INFO      Mode: exits
15:40:58  INFO        place_all_stops: checking 4 positions...
15:40:58  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
15:40:58  INFO        STOP skipped CDW: fractional (0.5749 shares) — software exit will handle it
15:40:58  INFO        STOP already live MNST @ $47.17
15:40:58  INFO        [positions] 3/3 (3 valid)
15:40:59  INFO        SELL MARKET [urgent] CDW closed
15:41:01  INFO        TX logged: SELL CDW  P&L -0.54%
15:41:01  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:40 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $454.84|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CDW  P&L -0.5%  $-0.42                         EXIT: stop_loss (-0.5%)|
|  MNST  P&L +0.1%  $+0.09                                           HOLD|
|  AAPL  P&L +1.9%  $+1.50                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00380000     $0.54    $0.65    +20.4%   $+11.00   $65.00   |
|                                                                        |
|  Options open P&L                                               $+11.00|
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  CDW                                         -0.54%  (threshold -0.50%)|
|  Count                                                                1|
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T11:41:01.780502-04:00 share=50% ===
2026-08-19 11:41:01,780 INFO === options_live_micro LIVE 2026-08-19T11:41:01.780502-04:00 share=50% ===
Live account equity $454.70 cash $233.09 #225458845 options_level=3
2026-08-19 11:41:01,960 INFO Live account equity $454.70 cash $233.09 #225458845 options_level=3
Live micro hold S404 AVGO260821C00380000 +20.4% (tp +50% / sl -50%)
2026-08-19 11:41:01,992 INFO Live micro hold S404 AVGO260821C00380000 +20.4% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-19 11:41:02,008 INFO Live micro: manage/exits only
Live micro done. open_options=1 lots=1
2026-08-19 11:41:02,021 INFO Live micro done. open_options=1 lots=1
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T154556Z

- UTC timestamp: `20260819T154556Z`
- GitHub run: [#7501](https://github.com/28twagg-ops/TradingBot/actions/runs/32271909256)
- Run id: `32271909256`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T154556Z_live_bot.log`, `logs/action_runs/20260819T154556Z_live_options.log`, `logs/action_runs/20260819T154556Z_options_bot.log`

### Live bot (tail)

```text
15:45:57  INFO      Mode: exits
15:45:58  INFO        Daily log -> logs/daily/2026-08-19.md
15:45:58  INFO        Daily log reconciled -> logs/daily/2026-08-19.md (1 ledger rows)
15:45:58  INFO        place_all_stops: checking 3 positions...
15:45:58  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
15:45:59  INFO        STOP already live MNST @ $47.17
15:45:59  INFO        [positions] 2/2 (2 valid)
15:45:59  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:45 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $449.65|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.1%  $+0.08                                           HOLD|
|  AAPL  P&L +1.9%  $+1.47                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00380000     $0.54    $0.60    +11.1%   $+6.00    $60.00   |
|                                                                        |
|  Options open P&L                                                $+6.00|
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T11:46:00.735690-04:00 share=50% ===
2026-08-19 11:46:00,735 INFO === options_live_micro LIVE 2026-08-19T11:46:00.735690-04:00 share=50% ===
Live account equity $449.66 cash $233.09 #225458845 options_level=3
2026-08-19 11:46:01,003 INFO Live account equity $449.66 cash $233.09 #225458845 options_level=3
Live micro hold S404 AVGO260821C00380000 +11.1% (tp +50% / sl -50%)
2026-08-19 11:46:01,125 INFO Live micro hold S404 AVGO260821C00380000 +11.1% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-19 11:46:01,244 INFO Live micro: manage/exits only
Live micro done. open_options=1 lots=1
2026-08-19 11:46:01,306 INFO Live micro done. open_options=1 lots=1
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T155057Z

- UTC timestamp: `20260819T155057Z`
- GitHub run: [#7502](https://github.com/28twagg-ops/TradingBot/actions/runs/32272396489)
- Run id: `32272396489`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T155057Z_live_bot.log`, `logs/action_runs/20260819T155057Z_live_options.log`, `logs/action_runs/20260819T155057Z_options_bot.log`

### Live bot (tail)

```text
15:50:58  INFO      Mode: exits
15:50:58  INFO        Daily log -> logs/daily/2026-08-19.md
15:50:58  INFO        Daily log reconciled -> logs/daily/2026-08-19.md (1 ledger rows)
15:50:58  INFO        place_all_stops: checking 3 positions...
15:50:58  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
15:50:58  INFO        STOP already live MNST @ $47.17
15:50:58  INFO        [positions] 2/2 (2 valid)
15:50:58  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:50 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $449.69|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.1%  $+0.05                                           HOLD|
|  AAPL  P&L +2.0%  $+1.52                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00380000     $0.54    $0.60    +11.1%   $+6.00    $60.00   |
|                                                                        |
|  Options open P&L                                                $+6.00|
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T11:50:59.760463-04:00 share=50% ===
2026-08-19 11:50:59,760 INFO === options_live_micro LIVE 2026-08-19T11:50:59.760463-04:00 share=50% ===
Live account equity $449.68 cash $233.09 #225458845 options_level=3
2026-08-19 11:50:59,818 INFO Live account equity $449.68 cash $233.09 #225458845 options_level=3
Live micro hold S404 AVGO260821C00380000 +11.1% (tp +50% / sl -50%)
2026-08-19 11:50:59,845 INFO Live micro hold S404 AVGO260821C00380000 +11.1% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-19 11:50:59,871 INFO Live micro: manage/exits only
Live micro done. open_options=1 lots=1
2026-08-19 11:50:59,902 INFO Live micro done. open_options=1 lots=1
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T160148Z

- UTC timestamp: `20260819T160148Z`
- GitHub run: [#7504](https://github.com/28twagg-ops/TradingBot/actions/runs/32273369436)
- Run id: `32273369436`
- Live bot: exit=`0`, duration=`5s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T160148Z_live_bot.log`, `logs/action_runs/20260819T160148Z_live_options.log`, `logs/action_runs/20260819T160148Z_options_bot.log`

### Live bot (tail)

```text
16:01:51  INFO      Mode: exits
16:01:53  INFO        Daily log -> logs/daily/2026-08-19.md
16:01:53  INFO        Daily log reconciled -> logs/daily/2026-08-19.md (1 ledger rows)
16:01:53  INFO        place_all_stops: checking 3 positions...
16:01:53  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
16:01:53  INFO        STOP already live MNST @ $47.17
16:01:53  INFO        [positions] 2/2 (2 valid)
16:01:54  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $448.41|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L -0.1%  $-0.07                                           HOLD|
|  AAPL  P&L +1.8%  $+1.37                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00380000     $0.54    $0.59    +9.3%    $+5.00    $59.00   |
|                                                                        |
|  Options open P&L                                                $+5.00|
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T12:01:55.299044-04:00 share=50% ===
2026-08-19 12:01:55,299 INFO === options_live_micro LIVE 2026-08-19T12:01:55.299044-04:00 share=50% ===
Live account equity $448.42 cash $233.09 #225458845 options_level=3
2026-08-19 12:01:55,528 INFO Live account equity $448.42 cash $233.09 #225458845 options_level=3
Live micro hold S404 AVGO260821C00380000 +9.3% (tp +50% / sl -50%)
2026-08-19 12:01:55,667 INFO Live micro hold S404 AVGO260821C00380000 +9.3% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-19 12:01:55,805 INFO Live micro: manage/exits only
Live micro done. open_options=1 lots=1
2026-08-19 12:01:55,873 INFO Live micro done. open_options=1 lots=1
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T160555Z

- UTC timestamp: `20260819T160555Z`
- GitHub run: [#7505](https://github.com/28twagg-ops/TradingBot/actions/runs/32273865388)
- Run id: `32273865388`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T160555Z_live_bot.log`, `logs/action_runs/20260819T160555Z_live_options.log`, `logs/action_runs/20260819T160555Z_options_bot.log`

### Live bot (tail)

```text
16:05:57  INFO      Mode: exits
16:05:57  INFO        Daily log -> logs/daily/2026-08-19.md
16:05:57  INFO        Daily log reconciled -> logs/daily/2026-08-19.md (1 ledger rows)
16:05:57  INFO        place_all_stops: checking 3 positions...
16:05:57  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
16:05:57  INFO        STOP already live MNST @ $47.17
16:05:57  INFO        [positions] 2/2 (2 valid)
16:05:58  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:05 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $460.53|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L -0.2%  $-0.14                                           HOLD|
|  AAPL  P&L +2.0%  $+1.58                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00380000     $0.54    $0.71    +31.5%   $+17.00   $71.00   |
|                                                                        |
|  Options open P&L                                               $+17.00|
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T12:05:58.733644-04:00 share=50% ===
2026-08-19 12:05:58,733 INFO === options_live_micro LIVE 2026-08-19T12:05:58.733644-04:00 share=50% ===
Live account equity $460.55 cash $233.09 #225458845 options_level=3
2026-08-19 12:05:58,839 INFO Live account equity $460.55 cash $233.09 #225458845 options_level=3
Live micro hold S404 AVGO260821C00380000 +31.5% (tp +50% / sl -50%)
2026-08-19 12:05:58,856 INFO Live micro hold S404 AVGO260821C00380000 +31.5% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-19 12:05:58,887 INFO Live micro: manage/exits only
Live micro done. open_options=1 lots=1
2026-08-19 12:05:58,896 INFO Live micro done. open_options=1 lots=1
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T161054Z

- UTC timestamp: `20260819T161054Z`
- GitHub run: [#7506](https://github.com/28twagg-ops/TradingBot/actions/runs/32274350336)
- Run id: `32274350336`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T161054Z_live_bot.log`, `logs/action_runs/20260819T161054Z_live_options.log`, `logs/action_runs/20260819T161054Z_options_bot.log`

### Live bot (tail)

```text
16:10:55  INFO      Mode: exits
16:10:56  INFO        Daily log -> logs/daily/2026-08-19.md
16:10:56  INFO        Daily log reconciled -> logs/daily/2026-08-19.md (1 ledger rows)
16:10:56  INFO        place_all_stops: checking 3 positions...
16:10:56  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
16:10:56  INFO        STOP already live MNST @ $47.17
16:10:57  INFO        [positions] 2/2 (2 valid)
16:10:57  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $461.45|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L -0.3%  $-0.22                                           HOLD|
|  AAPL  P&L +2.0%  $+1.54                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00380000     $0.54    $0.72    +33.3%   $+18.00   $72.00   |
|                                                                        |
|  Options open P&L                                               $+18.00|
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T12:10:58.468595-04:00 share=50% ===
2026-08-19 12:10:58,468 INFO === options_live_micro LIVE 2026-08-19T12:10:58.468595-04:00 share=50% ===
Live account equity $461.43 cash $233.09 #225458845 options_level=3
2026-08-19 12:10:58,671 INFO Live account equity $461.43 cash $233.09 #225458845 options_level=3
Live micro hold S404 AVGO260821C00380000 +33.3% (tp +50% / sl -50%)
2026-08-19 12:10:58,805 INFO Live micro hold S404 AVGO260821C00380000 +33.3% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-19 12:10:58,925 INFO Live micro: manage/exits only
Live micro done. open_options=1 lots=1
2026-08-19 12:10:58,988 INFO Live micro done. open_options=1 lots=1
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T161552Z

- UTC timestamp: `20260819T161552Z`
- GitHub run: [#7507](https://github.com/28twagg-ops/TradingBot/actions/runs/32274833538)
- Run id: `32274833538`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T161552Z_live_bot.log`, `logs/action_runs/20260819T161552Z_live_options.log`, `logs/action_runs/20260819T161552Z_options_bot.log`

### Live bot (tail)

```text
16:15:53  INFO      Mode: exits
16:15:54  INFO        Daily log -> logs/daily/2026-08-19.md
16:15:54  INFO        Daily log reconciled -> logs/daily/2026-08-19.md (1 ledger rows)
16:15:54  INFO        place_all_stops: checking 3 positions...
16:15:54  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
16:15:54  INFO        STOP already live MNST @ $47.17
16:15:55  INFO        [positions] 2/2 (2 valid)
16:15:55  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:15 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $460.52|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L -0.3%  $-0.26                                           HOLD|
|  AAPL  P&L +2.1%  $+1.67                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00380000     $0.54    $0.71    +31.5%   $+17.00   $71.00   |
|                                                                        |
|  Options open P&L                                               $+17.00|
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T12:15:56.367859-04:00 share=50% ===
2026-08-19 12:15:56,367 INFO === options_live_micro LIVE 2026-08-19T12:15:56.367859-04:00 share=50% ===
Live account equity $460.52 cash $233.09 #225458845 options_level=3
2026-08-19 12:15:56,585 INFO Live account equity $460.52 cash $233.09 #225458845 options_level=3
Live micro hold S404 AVGO260821C00380000 +31.5% (tp +50% / sl -50%)
2026-08-19 12:15:56,715 INFO Live micro hold S404 AVGO260821C00380000 +31.5% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-19 12:15:56,847 INFO Live micro: manage/exits only
Live micro done. open_options=1 lots=1
2026-08-19 12:15:56,910 INFO Live micro done. open_options=1 lots=1
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T162104Z

- UTC timestamp: `20260819T162104Z`
- GitHub run: [#7508](https://github.com/28twagg-ops/TradingBot/actions/runs/32275307977)
- Run id: `32275307977`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T162104Z_live_bot.log`, `logs/action_runs/20260819T162104Z_live_options.log`, `logs/action_runs/20260819T162104Z_options_bot.log`

### Live bot (tail)

```text
16:21:05  INFO      Mode: exits
16:21:06  INFO        Daily log -> logs/daily/2026-08-19.md
16:21:06  INFO        Daily log reconciled -> logs/daily/2026-08-19.md (1 ledger rows)
16:21:06  INFO        place_all_stops: checking 3 positions...
16:21:06  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
16:21:06  INFO        STOP already live MNST @ $47.17
16:21:07  INFO        [positions] 2/2 (2 valid)
16:21:07  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $469.51|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L -0.3%  $-0.24                                           HOLD|
|  AAPL  P&L +2.1%  $+1.64                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00380000     $0.54    $0.80    +48.1%   $+26.00   $80.00   |
|                                                                        |
|  Options open P&L                                               $+26.00|
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T12:21:08.758542-04:00 share=50% ===
2026-08-19 12:21:08,758 INFO === options_live_micro LIVE 2026-08-19T12:21:08.758542-04:00 share=50% ===
Live account equity $469.52 cash $233.09 #225458845 options_level=3
2026-08-19 12:21:09,015 INFO Live account equity $469.52 cash $233.09 #225458845 options_level=3
Live micro hold S404 AVGO260821C00380000 +48.1% (tp +50% / sl -50%)
2026-08-19 12:21:09,182 INFO Live micro hold S404 AVGO260821C00380000 +48.1% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-19 12:21:09,334 INFO Live micro: manage/exits only
Live micro done. open_options=1 lots=1
2026-08-19 12:21:09,417 INFO Live micro done. open_options=1 lots=1
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T163205Z

- UTC timestamp: `20260819T163205Z`
- GitHub run: [#7510](https://github.com/28twagg-ops/TradingBot/actions/runs/32276257347)
- Run id: `32276257347`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T163205Z_live_bot.log`, `logs/action_runs/20260819T163205Z_live_options.log`, `logs/action_runs/20260819T163205Z_options_bot.log`

### Live bot (tail)

```text
16:32:06  INFO      Mode: exits
16:32:07  INFO        Daily log -> logs/daily/2026-08-19.md
16:32:07  INFO        Daily log reconciled -> logs/daily/2026-08-19.md (1 ledger rows)
16:32:07  INFO        place_all_stops: checking 3 positions...
16:32:07  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
16:32:07  INFO        STOP already live MNST @ $47.17
16:32:07  INFO        [positions] 2/2 (2 valid)
16:32:08  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:32 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.33|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L -0.3%  $-0.24                                           HOLD|
|  AAPL  P&L +1.9%  $+1.46                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00380000     $0.54    $0.83    +53.7%   $+29.00   $83.00   |
|                                                                        |
|  Options open P&L                                               $+29.00|
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T12:32:08.777553-04:00 share=50% ===
2026-08-19 12:32:08,777 INFO === options_live_micro LIVE 2026-08-19T12:32:08.777553-04:00 share=50% ===
Live account equity $472.32 cash $233.09 #225458845 options_level=3
2026-08-19 12:32:08,825 INFO Live account equity $472.32 cash $233.09 #225458845 options_level=3
LIVE EXIT take_profit (+53.7%) AVGO260821C00380000 x1 limit=0.80 id=b0c7b4b9-fda4-4256-bffc-e7a1d9e97a1f
2026-08-19 12:32:09,530 INFO LIVE EXIT take_profit (+53.7%) AVGO260821C00380000 x1 limit=0.80 id=b0c7b4b9-fda4-4256-bffc-e7a1d9e97a1f
Live micro: manage/exits only
2026-08-19 12:32:09,539 INFO Live micro: manage/exits only
Live micro done. open_options=1 lots=0
2026-08-19 12:32:09,547 INFO Live micro done. open_options=1 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T163558Z

- UTC timestamp: `20260819T163558Z`
- GitHub run: [#7511](https://github.com/28twagg-ops/TradingBot/actions/runs/32276735811)
- Run id: `32276735811`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T163558Z_live_bot.log`, `logs/action_runs/20260819T163558Z_live_options.log`, `logs/action_runs/20260819T163558Z_options_bot.log`

### Live bot (tail)

```text
16:35:59  INFO      Mode: exits
16:36:01  INFO        Daily log -> logs/daily/2026-08-19.md
16:36:01  INFO        Daily log reconciled -> logs/daily/2026-08-19.md (1 ledger rows)
16:36:01  INFO        place_all_stops: checking 2 positions...
16:36:01  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
16:36:01  INFO        STOP already live MNST @ $47.17
16:36:02  INFO        [positions] 2/2 (2 valid)
16:36:02  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.22|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L -0.2%  $-0.19                                           HOLD|
|  AAPL  P&L +1.7%  $+1.33                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T12:36:03.371103-04:00 share=50% ===
2026-08-19 12:36:03,371 INFO === options_live_micro LIVE 2026-08-19T12:36:03.371103-04:00 share=50% ===
Live account equity $472.22 cash $316.06 #225458845 options_level=3
2026-08-19 12:36:03,610 INFO Live account equity $472.22 cash $316.06 #225458845 options_level=3
Live micro: manage/exits only
2026-08-19 12:36:03,791 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-08-19 12:36:03,849 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T164054Z

- UTC timestamp: `20260819T164054Z`
- GitHub run: [#7512](https://github.com/28twagg-ops/TradingBot/actions/runs/32277206242)
- Run id: `32277206242`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T164054Z_live_bot.log`, `logs/action_runs/20260819T164054Z_live_options.log`, `logs/action_runs/20260819T164054Z_options_bot.log`

### Live bot (tail)

```text
16:40:55  INFO      Mode: exits
16:40:56  INFO        Daily log -> logs/daily/2026-08-19.md
16:40:56  INFO        Daily log reconciled -> logs/daily/2026-08-19.md (1 ledger rows)
16:40:56  INFO        place_all_stops: checking 2 positions...
16:40:56  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
16:40:56  INFO        STOP already live MNST @ $47.17
16:40:57  INFO        [positions] 2/2 (2 valid)
16:40:57  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:40 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.10|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L -0.2%  $-0.18                                           HOLD|
|  AAPL  P&L +1.5%  $+1.20                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T12:40:58.402034-04:00 share=50% ===
2026-08-19 12:40:58,402 INFO === options_live_micro LIVE 2026-08-19T12:40:58.402034-04:00 share=50% ===
Live account equity $472.10 cash $316.06 #225458845 options_level=3
2026-08-19 12:40:58,646 INFO Live account equity $472.10 cash $316.06 #225458845 options_level=3
Live micro: manage/exits only
2026-08-19 12:40:58,885 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-08-19 12:40:58,959 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T164555Z

- UTC timestamp: `20260819T164555Z`
- GitHub run: [#7513](https://github.com/28twagg-ops/TradingBot/actions/runs/32277687622)
- Run id: `32277687622`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T164555Z_live_bot.log`, `logs/action_runs/20260819T164555Z_live_options.log`, `logs/action_runs/20260819T164555Z_options_bot.log`

### Live bot (tail)

```text
16:45:56  INFO      Mode: exits
16:45:56  INFO        Daily log -> logs/daily/2026-08-19.md
16:45:56  INFO        Daily log reconciled -> logs/daily/2026-08-19.md (1 ledger rows)
16:45:56  INFO        place_all_stops: checking 2 positions...
16:45:56  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
16:45:56  INFO        STOP already live MNST @ $47.17
16:45:57  INFO        [positions] 2/2 (2 valid)
16:45:57  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:45 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.02|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L -0.3%  $-0.20                                           HOLD|
|  AAPL  P&L +1.5%  $+1.14                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T12:45:57.931686-04:00 share=50% ===
2026-08-19 12:45:57,931 INFO === options_live_micro LIVE 2026-08-19T12:45:57.931686-04:00 share=50% ===
Live account equity $472.02 cash $316.06 #225458845 options_level=3
2026-08-19 12:45:58,013 INFO Live account equity $472.02 cash $316.06 #225458845 options_level=3
Live micro: manage/exits only
2026-08-19 12:45:58,078 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-08-19 12:45:58,098 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T165115Z

- UTC timestamp: `20260819T165115Z`
- GitHub run: [#7514](https://github.com/28twagg-ops/TradingBot/actions/runs/32278165098)
- Run id: `32278165098`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T165115Z_live_bot.log`, `logs/action_runs/20260819T165115Z_live_options.log`, `logs/action_runs/20260819T165115Z_options_bot.log`

### Live bot (tail)

```text
16:51:16  INFO      Mode: exits
16:51:18  INFO        Daily log -> logs/daily/2026-08-19.md
16:51:18  INFO        Daily log reconciled -> logs/daily/2026-08-19.md (1 ledger rows)
16:51:18  INFO        place_all_stops: checking 2 positions...
16:51:18  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
16:51:18  INFO        STOP already live MNST @ $47.17
16:51:18  INFO        [positions] 2/2 (2 valid)
16:51:18  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:51 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.14|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L -0.1%  $-0.10                                           HOLD|
|  AAPL  P&L +1.5%  $+1.16                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T12:51:20.147283-04:00 share=50% ===
2026-08-19 12:51:20,147 INFO === options_live_micro LIVE 2026-08-19T12:51:20.147283-04:00 share=50% ===
Live account equity $472.14 cash $316.06 #225458845 options_level=3
2026-08-19 12:51:20,395 INFO Live account equity $472.14 cash $316.06 #225458845 options_level=3
Live micro: manage/exits only
2026-08-19 12:51:20,802 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-08-19 12:51:20,874 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T170146Z

- UTC timestamp: `20260819T170146Z`
- GitHub run: [#7516](https://github.com/28twagg-ops/TradingBot/actions/runs/32279106830)
- Run id: `32279106830`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T170146Z_live_bot.log`, `logs/action_runs/20260819T170146Z_live_options.log`, `logs/action_runs/20260819T170146Z_options_bot.log`

### Live bot (tail)

```text
17:01:47  INFO      Mode: exits
17:01:47  INFO        Daily log -> logs/daily/2026-08-19.md
17:01:47  INFO        Daily log reconciled -> logs/daily/2026-08-19.md (1 ledger rows)
17:01:47  INFO        place_all_stops: checking 2 positions...
17:01:47  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
17:01:47  INFO        STOP already live MNST @ $47.17
17:01:48  INFO        [positions] 2/2 (2 valid)
17:01:48  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $471.98|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L -0.3%  $-0.21                                           HOLD|
|  AAPL  P&L +1.4%  $+1.11                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T13:01:49.000360-04:00 share=50% ===
2026-08-19 13:01:49,000 INFO === options_live_micro LIVE 2026-08-19T13:01:49.000360-04:00 share=50% ===
Live account equity $471.98 cash $316.06 #225458845 options_level=3
2026-08-19 13:01:49,045 INFO Live account equity $471.98 cash $316.06 #225458845 options_level=3
Live micro: manage/exits only
2026-08-19 13:01:49,073 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-08-19 13:01:49,081 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T170556Z

- UTC timestamp: `20260819T170556Z`
- GitHub run: [#7517](https://github.com/28twagg-ops/TradingBot/actions/runs/32279578675)
- Run id: `32279578675`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T170556Z_live_bot.log`, `logs/action_runs/20260819T170556Z_live_options.log`, `logs/action_runs/20260819T170556Z_options_bot.log`

### Live bot (tail)

```text
17:05:57  INFO      Mode: exits
17:05:58  INFO        Daily log -> logs/daily/2026-08-19.md
17:05:58  INFO        Daily log reconciled -> logs/daily/2026-08-19.md (1 ledger rows)
17:05:58  INFO        place_all_stops: checking 2 positions...
17:05:58  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
17:05:58  INFO        STOP already live MNST @ $47.17
17:05:58  INFO        [positions] 2/2 (2 valid)
17:05:58  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:05 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.02|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L -0.2%  $-0.14                                           HOLD|
|  AAPL  P&L +1.4%  $+1.07                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T13:05:59.498695-04:00 share=50% ===
2026-08-19 13:05:59,498 INFO === options_live_micro LIVE 2026-08-19T13:05:59.498695-04:00 share=50% ===
Live account equity $472.02 cash $316.06 #225458845 options_level=3
2026-08-19 13:05:59,626 INFO Live account equity $472.02 cash $316.06 #225458845 options_level=3
Live micro: manage/exits only
2026-08-19 13:05:59,715 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-08-19 13:05:59,744 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T171648Z

- UTC timestamp: `20260819T171648Z`
- GitHub run: [#7519](https://github.com/28twagg-ops/TradingBot/actions/runs/32280517134)
- Run id: `32280517134`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T171648Z_live_bot.log`, `logs/action_runs/20260819T171648Z_live_options.log`, `logs/action_runs/20260819T171648Z_options_bot.log`

### Live bot (tail)

```text
17:16:48  INFO      Mode: exits
17:16:49  INFO        Daily log -> logs/daily/2026-08-19.md
17:16:49  INFO        Daily log reconciled -> logs/daily/2026-08-19.md (1 ledger rows)
17:16:49  INFO        place_all_stops: checking 2 positions...
17:16:49  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
17:16:49  INFO        STOP already live MNST @ $47.17
17:16:49  INFO        [positions] 2/2 (2 valid)
17:16:49  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.08|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L -0.2%  $-0.12                                           HOLD|
|  AAPL  P&L +1.5%  $+1.12                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T13:16:50.407361-04:00 share=50% ===
2026-08-19 13:16:50,407 INFO === options_live_micro LIVE 2026-08-19T13:16:50.407361-04:00 share=50% ===
Live account equity $472.11 cash $316.06 #225458845 options_level=3
2026-08-19 13:16:50,448 INFO Live account equity $472.11 cash $316.06 #225458845 options_level=3
Live micro: manage/exits only
2026-08-19 13:16:50,468 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-08-19 13:16:50,474 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T172100Z

- UTC timestamp: `20260819T172100Z`
- GitHub run: [#7520](https://github.com/28twagg-ops/TradingBot/actions/runs/32280991574)
- Run id: `32280991574`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T172100Z_live_bot.log`, `logs/action_runs/20260819T172100Z_live_options.log`, `logs/action_runs/20260819T172100Z_options_bot.log`

### Live bot (tail)

```text
17:21:01  INFO      Mode: exits
17:21:01  INFO        Daily log -> logs/daily/2026-08-19.md
17:21:01  INFO        Daily log reconciled -> logs/daily/2026-08-19.md (1 ledger rows)
17:21:01  INFO        place_all_stops: checking 2 positions...
17:21:01  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
17:21:01  INFO        STOP already live MNST @ $47.17
17:21:02  INFO        [positions] 2/2 (2 valid)
17:21:02  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.08|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L -0.1%  $-0.09                                           HOLD|
|  AAPL  P&L +1.4%  $+1.09                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T13:21:03.058547-04:00 share=50% ===
2026-08-19 13:21:03,058 INFO === options_live_micro LIVE 2026-08-19T13:21:03.058547-04:00 share=50% ===
Live account equity $472.08 cash $316.06 #225458845 options_level=3
2026-08-19 13:21:03,102 INFO Live account equity $472.08 cash $316.06 #225458845 options_level=3
Live micro: manage/exits only
2026-08-19 13:21:03,150 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-08-19 13:21:03,157 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T172609Z

- UTC timestamp: `20260819T172609Z`
- GitHub run: [#7521](https://github.com/28twagg-ops/TradingBot/actions/runs/32281467364)
- Run id: `32281467364`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T172609Z_live_bot.log`, `logs/action_runs/20260819T172609Z_live_options.log`, `logs/action_runs/20260819T172609Z_options_bot.log`

### Live bot (tail)

```text
17:26:10  INFO      Mode: exits
17:26:11  INFO        Daily log -> logs/daily/2026-08-19.md
17:26:11  INFO        Daily log reconciled -> logs/daily/2026-08-19.md (1 ledger rows)
17:26:11  INFO        place_all_stops: checking 2 positions...
17:26:11  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
17:26:11  INFO        STOP already live MNST @ $47.17
17:26:11  INFO        [positions] 2/2 (2 valid)
17:26:11  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.04|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L -0.2%  $-0.12                                           HOLD|
|  AAPL  P&L +1.4%  $+1.08                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T13:26:12.505525-04:00 share=50% ===
2026-08-19 13:26:12,505 INFO === options_live_micro LIVE 2026-08-19T13:26:12.505525-04:00 share=50% ===
Live account equity $472.04 cash $316.06 #225458845 options_level=3
2026-08-19 13:26:12,623 INFO Live account equity $472.04 cash $316.06 #225458845 options_level=3
Live micro: manage/exits only
2026-08-19 13:26:12,739 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-08-19 13:26:12,772 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T173055Z

- UTC timestamp: `20260819T173055Z`
- GitHub run: [#7522](https://github.com/28twagg-ops/TradingBot/actions/runs/32281944354)
- Run id: `32281944354`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T173055Z_live_bot.log`, `logs/action_runs/20260819T173055Z_live_options.log`, `logs/action_runs/20260819T173055Z_options_bot.log`

### Live bot (tail)

```text
17:30:57  INFO      Mode: exits
17:30:57  INFO        Daily log -> logs/daily/2026-08-19.md
17:30:57  INFO        Daily log reconciled -> logs/daily/2026-08-19.md (1 ledger rows)
17:30:57  INFO        place_all_stops: checking 2 positions...
17:30:57  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
17:30:57  INFO        STOP already live MNST @ $47.17
17:30:58  INFO        [positions] 2/2 (2 valid)
17:30:58  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:30 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.08|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L -0.2%  $-0.14                                           HOLD|
|  AAPL  P&L +1.5%  $+1.14                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T13:30:59.200332-04:00 share=50% ===
2026-08-19 13:30:59,200 INFO === options_live_micro LIVE 2026-08-19T13:30:59.200332-04:00 share=50% ===
Live account equity $472.07 cash $316.06 #225458845 options_level=3
2026-08-19 13:30:59,306 INFO Live account equity $472.07 cash $316.06 #225458845 options_level=3
Live micro: manage/exits only
2026-08-19 13:30:59,401 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-08-19 13:30:59,431 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T173617Z

- UTC timestamp: `20260819T173617Z`
- GitHub run: [#7523](https://github.com/28twagg-ops/TradingBot/actions/runs/32282430073)
- Run id: `32282430073`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T173617Z_live_bot.log`, `logs/action_runs/20260819T173617Z_live_options.log`, `logs/action_runs/20260819T173617Z_options_bot.log`

### Live bot (tail)

```text
17:36:18  INFO      Mode: exits
17:36:18  INFO        Daily log -> logs/daily/2026-08-19.md
17:36:18  INFO        Daily log reconciled -> logs/daily/2026-08-19.md (1 ledger rows)
17:36:18  INFO        place_all_stops: checking 2 positions...
17:36:18  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
17:36:18  INFO        STOP already live MNST @ $47.17
17:36:18  INFO        [positions] 2/2 (2 valid)
17:36:18  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.29|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.0%  $+0.02                                           HOLD|
|  AAPL  P&L +1.5%  $+1.19                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T13:36:19.712835-04:00 share=50% ===
2026-08-19 13:36:19,712 INFO === options_live_micro LIVE 2026-08-19T13:36:19.712835-04:00 share=50% ===
Live account equity $472.29 cash $316.06 #225458845 options_level=3
2026-08-19 13:36:19,752 INFO Live account equity $472.29 cash $316.06 #225458845 options_level=3
Live micro: manage/exits only
2026-08-19 13:36:19,812 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-08-19 13:36:19,818 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T174104Z

- UTC timestamp: `20260819T174104Z`
- GitHub run: [#7524](https://github.com/28twagg-ops/TradingBot/actions/runs/32282912624)
- Run id: `32282912624`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T174104Z_live_bot.log`, `logs/action_runs/20260819T174104Z_live_options.log`, `logs/action_runs/20260819T174104Z_options_bot.log`

### Live bot (tail)

```text
17:41:05  INFO      Mode: exits
17:41:06  INFO        Daily log -> logs/daily/2026-08-19.md
17:41:06  INFO        Daily log reconciled -> logs/daily/2026-08-19.md (1 ledger rows)
17:41:06  INFO        place_all_stops: checking 2 positions...
17:41:06  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
17:41:06  INFO        STOP already live MNST @ $47.17
17:41:07  INFO        [positions] 2/2 (2 valid)
17:41:07  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.48|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.2%  $+0.15                                           HOLD|
|  AAPL  P&L +1.6%  $+1.25                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T13:41:08.246429-04:00 share=50% ===
2026-08-19 13:41:08,246 INFO === options_live_micro LIVE 2026-08-19T13:41:08.246429-04:00 share=50% ===
Live account equity $472.48 cash $316.06 #225458845 options_level=3
2026-08-19 13:41:08,439 INFO Live account equity $472.48 cash $316.06 #225458845 options_level=3
Live micro: manage/exits only
2026-08-19 13:41:08,603 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-08-19 13:41:08,658 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T174554Z

- UTC timestamp: `20260819T174554Z`
- GitHub run: [#7525](https://github.com/28twagg-ops/TradingBot/actions/runs/32283397813)
- Run id: `32283397813`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T174554Z_live_bot.log`, `logs/action_runs/20260819T174554Z_live_options.log`, `logs/action_runs/20260819T174554Z_options_bot.log`

### Live bot (tail)

```text
17:45:56  INFO      Mode: exits
17:45:56  INFO        Daily log -> logs/daily/2026-08-19.md
17:45:56  INFO        Daily log reconciled -> logs/daily/2026-08-19.md (1 ledger rows)
17:45:56  INFO        place_all_stops: checking 2 positions...
17:45:56  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
17:45:56  INFO        STOP already live MNST @ $47.17
17:45:56  INFO        [positions] 2/2 (2 valid)
17:45:57  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:45 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.47|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.2%  $+0.17                                           HOLD|
|  AAPL  P&L +1.6%  $+1.21                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T13:45:57.871863-04:00 share=50% ===
2026-08-19 13:45:57,871 INFO === options_live_micro LIVE 2026-08-19T13:45:57.871863-04:00 share=50% ===
Live account equity $472.46 cash $316.06 #225458845 options_level=3
2026-08-19 13:45:57,931 INFO Live account equity $472.46 cash $316.06 #225458845 options_level=3
Live micro: manage/exits only
2026-08-19 13:45:57,966 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-08-19 13:45:57,977 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T175501Z

- UTC timestamp: `20260819T175501Z`
- GitHub run: [#7526](https://github.com/28twagg-ops/TradingBot/actions/runs/32283881974)
- Run id: `32283881974`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T175501Z_live_bot.log`, `logs/action_runs/20260819T175501Z_live_options.log`, `logs/action_runs/20260819T175501Z_options_bot.log`

### Live bot (tail)

```text
17:55:02  INFO      Mode: exits
17:55:03  INFO        Daily log -> logs/daily/2026-08-19.md
17:55:03  INFO        Daily log reconciled -> logs/daily/2026-08-19.md (1 ledger rows)
17:55:03  INFO        place_all_stops: checking 2 positions...
17:55:03  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
17:55:03  INFO        STOP already live MNST @ $47.17
17:55:04  INFO        [positions] 2/2 (2 valid)
17:55:04  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:55 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.71|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.6%  $+0.46                                           HOLD|
|  AAPL  P&L +1.5%  $+1.17                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T13:55:05.426463-04:00 share=50% ===
2026-08-19 13:55:05,426 INFO === options_live_micro LIVE 2026-08-19T13:55:05.426463-04:00 share=50% ===
Live account equity $472.70 cash $316.06 #225458845 options_level=3
2026-08-19 13:55:05,620 INFO Live account equity $472.70 cash $316.06 #225458845 options_level=3
Live micro: manage/exits only
2026-08-19 13:55:05,784 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-08-19 13:55:05,867 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T175629Z

- UTC timestamp: `20260819T175629Z`
- GitHub run: [#7527](https://github.com/28twagg-ops/TradingBot/actions/runs/32284365860)
- Run id: `32284365860`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T175629Z_live_bot.log`, `logs/action_runs/20260819T175629Z_live_options.log`, `logs/action_runs/20260819T175629Z_options_bot.log`

### Live bot (tail)

```text
17:56:31  INFO      Mode: exits
17:56:31  INFO        Daily log -> logs/daily/2026-08-19.md
17:56:31  INFO        Daily log reconciled -> logs/daily/2026-08-19.md (1 ledger rows)
17:56:31  INFO        place_all_stops: checking 2 positions...
17:56:31  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
17:56:31  INFO        STOP already live MNST @ $47.17
17:56:32  INFO        [positions] 2/2 (2 valid)
17:56:32  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:56 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.73|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.6%  $+0.46                                           HOLD|
|  AAPL  P&L +1.5%  $+1.19                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T13:56:33.128135-04:00 share=50% ===
2026-08-19 13:56:33,128 INFO === options_live_micro LIVE 2026-08-19T13:56:33.128135-04:00 share=50% ===
Live account equity $472.73 cash $316.06 #225458845 options_level=3
2026-08-19 13:56:33,184 INFO Live account equity $472.73 cash $316.06 #225458845 options_level=3
Live micro: manage/exits only
2026-08-19 13:56:33,221 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-08-19 13:56:33,232 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T180142Z

- UTC timestamp: `20260819T180142Z`
- GitHub run: [#7528](https://github.com/28twagg-ops/TradingBot/actions/runs/32284850694)
- Run id: `32284850694`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T180142Z_live_bot.log`, `logs/action_runs/20260819T180142Z_live_options.log`, `logs/action_runs/20260819T180142Z_options_bot.log`

### Live bot (tail)

```text
18:01:43  INFO      Mode: exits
18:01:44  INFO        Daily log -> logs/daily/2026-08-19.md
18:01:44  INFO        Daily log reconciled -> logs/daily/2026-08-19.md (1 ledger rows)
18:01:44  INFO        place_all_stops: checking 2 positions...
18:01:44  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
18:01:44  INFO        STOP already live MNST @ $47.17
18:01:44  INFO        [positions] 2/2 (2 valid)
18:01:45  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.66|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.5%  $+0.40                                           HOLD|
|  AAPL  P&L +1.5%  $+1.18                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T14:01:45.898419-04:00 share=50% ===
2026-08-19 14:01:45,898 INFO === options_live_micro LIVE 2026-08-19T14:01:45.898419-04:00 share=50% ===
Live account equity $472.66 cash $316.06 #225458845 options_level=3
2026-08-19 14:01:46,015 INFO Live account equity $472.66 cash $316.06 #225458845 options_level=3
Live micro: manage/exits only
2026-08-19 14:01:46,101 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-08-19 14:01:46,151 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T180659Z

- UTC timestamp: `20260819T180659Z`
- GitHub run: [#7529](https://github.com/28twagg-ops/TradingBot/actions/runs/32285321718)
- Run id: `32285321718`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T180659Z_live_bot.log`, `logs/action_runs/20260819T180659Z_live_options.log`, `logs/action_runs/20260819T180659Z_options_bot.log`

### Live bot (tail)

```text
18:07:00  INFO      Mode: exits
18:07:01  INFO        Daily log -> logs/daily/2026-08-19.md
18:07:01  INFO        Daily log reconciled -> logs/daily/2026-08-19.md (1 ledger rows)
18:07:02  INFO        place_all_stops: checking 2 positions...
18:07:02  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
18:07:02  INFO        STOP already live MNST @ $47.17
18:07:02  INFO        [positions] 2/2 (2 valid)
18:07:02  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:07 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.71|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.5%  $+0.42                                           HOLD|
|  AAPL  P&L +1.5%  $+1.20                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T14:07:03.916382-04:00 share=50% ===
2026-08-19 14:07:03,916 INFO === options_live_micro LIVE 2026-08-19T14:07:03.916382-04:00 share=50% ===
Live account equity $472.71 cash $316.06 #225458845 options_level=3
2026-08-19 14:07:04,162 INFO Live account equity $472.71 cash $316.06 #225458845 options_level=3
Live micro: manage/exits only
2026-08-19 14:07:04,370 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-08-19 14:07:04,446 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T181205Z

- UTC timestamp: `20260819T181205Z`
- GitHub run: [#7530](https://github.com/28twagg-ops/TradingBot/actions/runs/32285791964)
- Run id: `32285791964`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T181205Z_live_bot.log`, `logs/action_runs/20260819T181205Z_live_options.log`, `logs/action_runs/20260819T181205Z_options_bot.log`

### Live bot (tail)

```text
18:12:06  INFO      Mode: exits
18:12:06  INFO        Daily log -> logs/daily/2026-08-19.md
18:12:06  INFO        Daily log reconciled -> logs/daily/2026-08-19.md (1 ledger rows)
18:12:07  INFO        place_all_stops: checking 2 positions...
18:12:07  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
18:12:07  INFO        STOP already live MNST @ $47.17
18:12:07  INFO        [positions] 2/2 (2 valid)
18:12:07  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:12 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.99|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.9%  $+0.69                                           HOLD|
|  AAPL  P&L +1.6%  $+1.21                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T14:12:08.475662-04:00 share=50% ===
2026-08-19 14:12:08,475 INFO === options_live_micro LIVE 2026-08-19T14:12:08.475662-04:00 share=50% ===
Live account equity $472.99 cash $316.06 #225458845 options_level=3
2026-08-19 14:12:08,617 INFO Live account equity $472.99 cash $316.06 #225458845 options_level=3
Live micro: manage/exits only
2026-08-19 14:12:08,707 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-08-19 14:12:08,736 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T182237Z

- UTC timestamp: `20260819T182237Z`
- GitHub run: [#7532](https://github.com/28twagg-ops/TradingBot/actions/runs/32286741816)
- Run id: `32286741816`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T182237Z_live_bot.log`, `logs/action_runs/20260819T182237Z_live_options.log`, `logs/action_runs/20260819T182237Z_options_bot.log`

### Live bot (tail)

```text
18:22:38  INFO      Mode: exits
18:22:39  INFO        Daily log -> logs/daily/2026-08-19.md
18:22:39  INFO        Daily log reconciled -> logs/daily/2026-08-19.md (1 ledger rows)
18:22:39  INFO        place_all_stops: checking 2 positions...
18:22:39  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
18:22:39  INFO        STOP already live MNST @ $47.17
18:22:39  INFO        [positions] 2/2 (2 valid)
18:22:39  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:22 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.70|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.6%  $+0.49                                           HOLD|
|  AAPL  P&L +1.5%  $+1.12                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T14:22:40.356612-04:00 share=50% ===
2026-08-19 14:22:40,356 INFO === options_live_micro LIVE 2026-08-19T14:22:40.356612-04:00 share=50% ===
Live account equity $472.70 cash $316.06 #225458845 options_level=3
2026-08-19 14:22:40,499 INFO Live account equity $472.70 cash $316.06 #225458845 options_level=3
Live micro: manage/exits only
2026-08-19 14:22:40,573 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-08-19 14:22:40,595 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T183245Z

- UTC timestamp: `20260819T183245Z`
- GitHub run: [#7534](https://github.com/28twagg-ops/TradingBot/actions/runs/32287681130)
- Run id: `32287681130`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T183245Z_live_bot.log`, `logs/action_runs/20260819T183245Z_live_options.log`, `logs/action_runs/20260819T183245Z_options_bot.log`

### Live bot (tail)

```text
18:32:47  INFO      Mode: exits
18:32:47  INFO        Daily log -> logs/daily/2026-08-19.md
18:32:47  INFO        Daily log reconciled -> logs/daily/2026-08-19.md (1 ledger rows)
18:32:47  INFO        place_all_stops: checking 2 positions...
18:32:47  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
18:32:47  INFO        STOP already live MNST @ $47.17
18:32:47  INFO        [positions] 2/2 (2 valid)
18:32:48  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:32 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.53|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.6%  $+0.46                                           HOLD|
|  AAPL  P&L +1.3%  $+0.99                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T14:32:48.792406-04:00 share=50% ===
2026-08-19 14:32:48,792 INFO === options_live_micro LIVE 2026-08-19T14:32:48.792406-04:00 share=50% ===
Live account equity $472.53 cash $316.06 #225458845 options_level=3
2026-08-19 14:32:48,913 INFO Live account equity $472.53 cash $316.06 #225458845 options_level=3
Live micro: manage/exits only
2026-08-19 14:32:49,009 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-08-19 14:32:49,055 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T183603Z

- UTC timestamp: `20260819T183603Z`
- GitHub run: [#7535](https://github.com/28twagg-ops/TradingBot/actions/runs/32288150211)
- Run id: `32288150211`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T183603Z_live_bot.log`, `logs/action_runs/20260819T183603Z_live_options.log`, `logs/action_runs/20260819T183603Z_options_bot.log`

### Live bot (tail)

```text
18:36:04  INFO      Mode: exits
18:36:06  INFO        Daily log -> logs/daily/2026-08-19.md
18:36:06  INFO        Daily log reconciled -> logs/daily/2026-08-19.md (1 ledger rows)
18:36:06  INFO        place_all_stops: checking 2 positions...
18:36:06  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
18:36:06  INFO        STOP already live MNST @ $47.17
18:36:07  INFO        [positions] 2/2 (2 valid)
18:36:07  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.59|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.7%  $+0.53                                           HOLD|
|  AAPL  P&L +1.3%  $+0.98                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T14:36:08.567503-04:00 share=50% ===
2026-08-19 14:36:08,567 INFO === options_live_micro LIVE 2026-08-19T14:36:08.567503-04:00 share=50% ===
Live account equity $472.59 cash $316.06 #225458845 options_level=3
2026-08-19 14:36:08,946 INFO Live account equity $472.59 cash $316.06 #225458845 options_level=3
Live micro: manage/exits only
2026-08-19 14:36:09,311 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-08-19 14:36:09,445 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T184052Z

- UTC timestamp: `20260819T184052Z`
- GitHub run: [#7536](https://github.com/28twagg-ops/TradingBot/actions/runs/32288623676)
- Run id: `32288623676`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T184052Z_live_bot.log`, `logs/action_runs/20260819T184052Z_live_options.log`, `logs/action_runs/20260819T184052Z_options_bot.log`

### Live bot (tail)

```text
18:40:53  INFO      Mode: exits
18:40:53  INFO        Daily log -> logs/daily/2026-08-19.md
18:40:53  INFO        Daily log reconciled -> logs/daily/2026-08-19.md (1 ledger rows)
18:40:53  INFO        place_all_stops: checking 2 positions...
18:40:53  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
18:40:53  INFO        STOP already live MNST @ $47.17
18:40:53  INFO        [positions] 2/2 (2 valid)
18:40:53  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:40 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.69|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.7%  $+0.54                                           HOLD|
|  AAPL  P&L +1.4%  $+1.07                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T14:40:54.470575-04:00 share=50% ===
2026-08-19 14:40:54,470 INFO === options_live_micro LIVE 2026-08-19T14:40:54.470575-04:00 share=50% ===
Live account equity $472.69 cash $316.06 #225458845 options_level=3
2026-08-19 14:40:54,512 INFO Live account equity $472.69 cash $316.06 #225458845 options_level=3
Live micro: manage/exits only
2026-08-19 14:40:54,533 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-08-19 14:40:54,541 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T185146Z

- UTC timestamp: `20260819T185146Z`
- GitHub run: [#7538](https://github.com/28twagg-ops/TradingBot/actions/runs/32289584243)
- Run id: `32289584243`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T185146Z_live_bot.log`, `logs/action_runs/20260819T185146Z_live_options.log`, `logs/action_runs/20260819T185146Z_options_bot.log`

### Live bot (tail)

```text
18:51:47  INFO      Mode: exits
18:51:48  INFO        Daily log -> logs/daily/2026-08-19.md
18:51:48  INFO        Daily log reconciled -> logs/daily/2026-08-19.md (1 ledger rows)
18:51:48  INFO        place_all_stops: checking 2 positions...
18:51:48  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
18:51:48  INFO        STOP already live MNST @ $47.17
18:51:49  INFO        [positions] 2/2 (2 valid)
18:51:49  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:51 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.90|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.9%  $+0.67                                           HOLD|
|  AAPL  P&L +1.5%  $+1.15                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T14:51:50.348112-04:00 share=50% ===
2026-08-19 14:51:50,348 INFO === options_live_micro LIVE 2026-08-19T14:51:50.348112-04:00 share=50% ===
Live account equity $472.92 cash $316.06 #225458845 options_level=3
2026-08-19 14:51:50,591 INFO Live account equity $472.92 cash $316.06 #225458845 options_level=3
Live micro: manage/exits only
2026-08-19 14:51:50,816 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-08-19 14:51:50,890 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T185605Z

- UTC timestamp: `20260819T185605Z`
- GitHub run: [#7539](https://github.com/28twagg-ops/TradingBot/actions/runs/32290067115)
- Run id: `32290067115`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T185605Z_live_bot.log`, `logs/action_runs/20260819T185605Z_live_options.log`, `logs/action_runs/20260819T185605Z_options_bot.log`

### Live bot (tail)

```text
18:56:06  INFO      Mode: exits
18:56:06  INFO        Daily log -> logs/daily/2026-08-19.md
18:56:06  INFO        Daily log reconciled -> logs/daily/2026-08-19.md (1 ledger rows)
18:56:06  INFO        place_all_stops: checking 2 positions...
18:56:06  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
18:56:06  INFO        STOP already live MNST @ $47.17
18:56:06  INFO        [positions] 2/2 (2 valid)
18:56:06  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:56 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.99|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +1.0%  $+0.80                                           HOLD|
|  AAPL  P&L +1.4%  $+1.12                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T14:56:07.537649-04:00 share=50% ===
2026-08-19 14:56:07,537 INFO === options_live_micro LIVE 2026-08-19T14:56:07.537649-04:00 share=50% ===
Live account equity $472.99 cash $316.06 #225458845 options_level=3
2026-08-19 14:56:07,582 INFO Live account equity $472.99 cash $316.06 #225458845 options_level=3
Live micro: manage/exits only
2026-08-19 14:56:07,647 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-08-19 14:56:07,683 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T190137Z

- UTC timestamp: `20260819T190137Z`
- GitHub run: [#7540](https://github.com/28twagg-ops/TradingBot/actions/runs/32290548976)
- Run id: `32290548976`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T190137Z_live_bot.log`, `logs/action_runs/20260819T190137Z_live_options.log`, `logs/action_runs/20260819T190137Z_options_bot.log`

### Live bot (tail)

```text
19:01:38  INFO      Mode: exits
19:01:39  INFO        Daily log -> logs/daily/2026-08-19.md
19:01:39  INFO        Daily log reconciled -> logs/daily/2026-08-19.md (1 ledger rows)
19:01:39  INFO        place_all_stops: checking 2 positions...
19:01:39  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
19:01:39  INFO        STOP already live MNST @ $47.17
19:01:40  INFO        [positions] 2/2 (2 valid)
19:01:40  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         19:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.97|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +1.1%  $+0.83                                           HOLD|
|  AAPL  P&L +1.4%  $+1.06                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T15:01:41.573289-04:00 share=50% ===
2026-08-19 15:01:41,573 INFO === options_live_micro LIVE 2026-08-19T15:01:41.573289-04:00 share=50% ===
Live account equity $472.98 cash $316.06 #225458845 options_level=3
2026-08-19 15:01:41,786 INFO Live account equity $472.98 cash $316.06 #225458845 options_level=3
Live micro: manage/exits only
2026-08-19 15:01:41,956 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-08-19 15:01:42,012 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T190600Z

- UTC timestamp: `20260819T190600Z`
- GitHub run: [#7541](https://github.com/28twagg-ops/TradingBot/actions/runs/32291029435)
- Run id: `32291029435`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T190600Z_live_bot.log`, `logs/action_runs/20260819T190600Z_live_options.log`, `logs/action_runs/20260819T190600Z_options_bot.log`

### Live bot (tail)

```text
19:06:01  INFO      Mode: exits
19:06:01  INFO        Daily log -> logs/daily/2026-08-19.md
19:06:01  INFO        Daily log reconciled -> logs/daily/2026-08-19.md (1 ledger rows)
19:06:01  INFO        place_all_stops: checking 2 positions...
19:06:01  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
19:06:01  INFO        STOP already live MNST @ $47.17
19:06:02  INFO        [positions] 2/2 (2 valid)
19:06:02  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         19:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $473.13|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +1.1%  $+0.84                                           HOLD|
|  AAPL  P&L +1.6%  $+1.22                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T15:06:02.973206-04:00 share=50% ===
2026-08-19 15:06:02,973 INFO === options_live_micro LIVE 2026-08-19T15:06:02.973206-04:00 share=50% ===
Live account equity $473.14 cash $316.06 #225458845 options_level=3
2026-08-19 15:06:03,030 INFO Live account equity $473.14 cash $316.06 #225458845 options_level=3
Live micro: manage/exits only
2026-08-19 15:06:03,064 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-08-19 15:06:03,075 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T191050Z

- UTC timestamp: `20260819T191050Z`
- GitHub run: [#7542](https://github.com/28twagg-ops/TradingBot/actions/runs/32291496945)
- Run id: `32291496945`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T191050Z_live_bot.log`, `logs/action_runs/20260819T191050Z_live_options.log`, `logs/action_runs/20260819T191050Z_options_bot.log`

### Live bot (tail)

```text
19:10:51  INFO      Mode: exits
19:10:52  INFO        Daily log -> logs/daily/2026-08-19.md
19:10:52  INFO        Daily log reconciled -> logs/daily/2026-08-19.md (1 ledger rows)
19:10:52  INFO        place_all_stops: checking 2 positions...
19:10:52  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
19:10:52  INFO        STOP already live MNST @ $47.17
19:10:52  INFO        [positions] 2/2 (2 valid)
19:10:52  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         19:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.89|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.7%  $+0.54                                           HOLD|
|  AAPL  P&L +1.6%  $+1.27                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T15:10:53.163178-04:00 share=50% ===
2026-08-19 15:10:53,163 INFO === options_live_micro LIVE 2026-08-19T15:10:53.163178-04:00 share=50% ===
Live account equity $472.90 cash $316.06 #225458845 options_level=3
2026-08-19 15:10:53,222 INFO Live account equity $472.90 cash $316.06 #225458845 options_level=3
Live micro: manage/exits only
2026-08-19 15:10:53,266 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-08-19 15:10:53,278 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T192203Z

- UTC timestamp: `20260819T192203Z`
- GitHub run: [#7544](https://github.com/28twagg-ops/TradingBot/actions/runs/32292433243)
- Run id: `32292433243`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T192203Z_live_bot.log`, `logs/action_runs/20260819T192203Z_live_options.log`, `logs/action_runs/20260819T192203Z_options_bot.log`

### Live bot (tail)

```text
19:22:05  INFO      Mode: exits
19:22:05  INFO        Daily log -> logs/daily/2026-08-19.md
19:22:05  INFO        Daily log reconciled -> logs/daily/2026-08-19.md (1 ledger rows)
19:22:05  INFO        place_all_stops: checking 2 positions...
19:22:05  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
19:22:05  INFO        STOP already live MNST @ $47.17
19:22:06  INFO        [positions] 2/2 (2 valid)
19:22:06  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         19:22 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.80|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.3%  $+0.24                                           HOLD|
|  AAPL  P&L +1.9%  $+1.48                                           HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T15:22:07.015797-04:00 share=50% ===
2026-08-19 15:22:07,015 INFO === options_live_micro LIVE 2026-08-19T15:22:07.015797-04:00 share=50% ===
Live account equity $472.80 cash $316.06 #225458845 options_level=3
2026-08-19 15:22:07,075 INFO Live account equity $472.80 cash $316.06 #225458845 options_level=3
Live micro: manage/exits only
2026-08-19 15:22:07,109 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-08-19 15:22:07,121 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T193108Z

- UTC timestamp: `20260819T193108Z`
- GitHub run: [#7546](https://github.com/28twagg-ops/TradingBot/actions/runs/32293362966)
- Run id: `32293362966`
- Live bot: exit=`0`, duration=`216s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T193108Z_live_bot.log`, `logs/action_runs/20260819T193108Z_live_options.log`, `logs/action_runs/20260819T193108Z_options_bot.log`

### Live bot (tail)

```text
19:31:09  INFO      Mode: evening_prep
19:31:10  INFO        [prep_positions] 2/2 (2 valid)
19:31:10  INFO        Universe cache hit: 903 tickers (tickers_2026-08-19.json)
19:31:11  INFO        [prep_universe] 40/901 (40 valid)
19:31:13  INFO        [prep_universe] 80/901 (80 valid)
19:31:15  INFO        [prep_universe] 120/901 (120 valid)
19:31:17  INFO        [prep_universe] 160/901 (160 valid)
19:31:18  INFO        [prep_universe] 200/901 (199 valid)
19:31:23  INFO        [prep_universe] 240/901 (238 valid)
19:31:36  INFO        [prep_universe] 280/901 (278 valid)
19:31:49  INFO        [prep_universe] 320/901 (318 valid)
19:32:00  INFO        [prep_universe] 360/901 (358 valid)
19:32:11  INFO        [prep_universe] 400/901 (397 valid)
19:32:25  INFO        [prep_universe] 440/901 (437 valid)
19:32:35  INFO        [prep_universe] 480/901 (477 valid)
19:32:49  INFO        [prep_universe] 520/901 (517 valid)
19:32:59  INFO        [prep_universe] 560/901 (557 valid)
19:33:13  INFO        [prep_universe] 600/901 (597 valid)
19:33:23  INFO        [prep_universe] 640/901 (637 valid)
19:33:37  INFO        [prep_universe] 680/901 (677 valid)
19:33:47  INFO        [prep_universe] 720/901 (717 valid)
19:34:01  INFO        [prep_universe] 760/901 (757 valid)
19:34:12  INFO        [prep_universe] 800/901 (797 valid)
19:34:25  INFO        [prep_universe] 840/901 (836 valid)
19:34:35  INFO        [prep_universe] 880/901 (876 valid)
19:34:42  INFO        [prep_universe] 901/901 (897 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      EVENING_PREP|
|  Time                                                         19:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.66|
+========================================================================+

+========================================================================+
|                              EVENING PREP                              |
+========================================================================+
|  Goal                   Precompute exits/signals for next execution run|
|  Plan file                                 logs/plans/evening_plan.json|
|  Regime                                                            BULL|
+========================================================================+

+========================================================================+
|                       OPEN POSITION P&L SNAPSHOT                       |
+========================================================================+
|  Open positions                                                       2|
|  Invested                                                       $156.60|
|  Open P&L                                                        $+1.58|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AAPL     Pullback50      $78.98     $310.56  $316.46  +1.9%   $+1.47  |
|  MNST     MomReversal     $77.62     $47.41   $47.48   +0.1%   $+0.11  |
+========================================================================+

+========================================================================+
|                            OPEN SELL ORDERS                            |
+========================================================================+
|  Count                                                                1|
|  TICKER    TYPE              QTY       LIMIT       STOP                |
+------------------------------------------------------------------------+
|  MNST      OrderType.STOP    1         None        47.17               |
+========================================================================+

+========================================================================+
|                              PREP SUMMARY                              |
+========================================================================+
|  Saved                                                              yes|
|  Exit candidates                                                      1|
|  Signal candidates                                                   30|
|  Universe scanned                                                   901|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T15:34:45.236638-04:00 share=50% ===
2026-08-19 15:34:45,236 INFO === options_live_micro LIVE 2026-08-19T15:34:45.236638-04:00 share=50% ===
Live account equity $472.63 cash $316.06 #225458845 options_level=3
2026-08-19 15:34:45,399 INFO Live account equity $472.63 cash $316.06 #225458845 options_level=3
Live micro: manage/exits only
2026-08-19 15:34:45,553 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-08-19 15:34:45,600 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T194151Z

- UTC timestamp: `20260819T194151Z`
- GitHub run: [#7548](https://github.com/28twagg-ops/TradingBot/actions/runs/32294279656)
- Run id: `32294279656`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T194151Z_live_bot.log`, `logs/action_runs/20260819T194151Z_live_options.log`, `logs/action_runs/20260819T194151Z_options_bot.log`

### Live bot (tail)

```text
19:41:52  INFO      Mode: evening_prep
19:41:53  INFO        [prep_positions] 2/2 (2 valid)
19:41:53  INFO        Universe cache hit: 903 tickers (tickers_2026-08-19.json)
19:41:55  INFO        [prep_universe] 40/901 (40 valid)
19:41:56  INFO        [prep_universe] 80/901 (80 valid)
19:41:58  INFO        [prep_universe] 120/901 (120 valid)
19:41:59  INFO        [prep_universe] 160/901 (160 valid)
19:42:01  INFO        [prep_universe] 200/901 (199 valid)
19:42:08  INFO        [prep_universe] 240/901 (238 valid)
19:42:19  INFO        [prep_universe] 280/901 (278 valid)
19:42:30  INFO        [prep_universe] 320/901 (318 valid)
19:42:43  INFO        [prep_universe] 360/901 (358 valid)
19:42:54  INFO        [prep_universe] 400/901 (397 valid)
19:43:07  INFO        [prep_universe] 440/901 (437 valid)
19:43:21  INFO        [prep_universe] 480/901 (477 valid)
19:43:31  INFO        [prep_universe] 520/901 (517 valid)
19:43:42  INFO        [prep_universe] 560/901 (557 valid)
19:43:55  INFO        [prep_universe] 600/901 (597 valid)
19:44:06  INFO        [prep_universe] 640/901 (637 valid)
19:44:19  INFO        [prep_universe] 680/901 (677 valid)
19:44:32  INFO        [prep_universe] 720/901 (717 valid)
19:44:43  INFO        [prep_universe] 760/901 (757 valid)
19:44:56  INFO        [prep_universe] 800/901 (797 valid)
19:45:07  INFO        [prep_universe] 840/901 (836 valid)
19:45:20  INFO        [prep_universe] 880/901 (876 valid)
19:45:24  INFO        [prep_universe] 901/901 (897 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      EVENING_PREP|
|  Time                                                         19:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.51|
+========================================================================+

+========================================================================+
|                              EVENING PREP                              |
+========================================================================+
|  Goal                   Precompute exits/signals for next execution run|
|  Plan file                                 logs/plans/evening_plan.json|
|  Regime                                                            BULL|
+========================================================================+

+========================================================================+
|                       OPEN POSITION P&L SNAPSHOT                       |
+========================================================================+
|  Open positions                                                       2|
|  Invested                                                       $156.45|
|  Open P&L                                                        $+1.43|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AAPL     Pullback50      $78.76     $310.56  $315.56  +1.6%   $+1.25  |
|  MNST     MomReversal     $77.69     $47.41   $47.52   +0.2%   $+0.18  |
+========================================================================+

+========================================================================+
|                            OPEN SELL ORDERS                            |
+========================================================================+
|  Count                                                                1|
|  TICKER    TYPE              QTY       LIMIT       STOP                |
+------------------------------------------------------------------------+
|  MNST      OrderType.STOP    1         None        47.17               |
+========================================================================+

+========================================================================+
|                              PREP SUMMARY                              |
+========================================================================+
|  Saved                                                              yes|
|  Exit candidates                                                      0|
|  Signal candidates                                                   32|
|  Universe scanned                                                   901|
+========================================================================+
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T194630Z

- UTC timestamp: `20260819T194630Z`
- GitHub run: [#7549](https://github.com/28twagg-ops/TradingBot/actions/runs/32294741659)
- Run id: `32294741659`
- Live bot: exit=`0`, duration=`232s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T194630Z_live_bot.log`, `logs/action_runs/20260819T194630Z_live_options.log`, `logs/action_runs/20260819T194630Z_options_bot.log`

### Live bot (tail)

```text
... (160 earlier lines - see full log file)
|  EXEL     Pullback50      eq     $54.42   46.3   -1.22   50MA bounce (+|
|  GHC      Pullback50      eq     $1181.~  36.4   -1.48   50MA bounce (+|
|  IRT      Pullback50      eq     $16.55   47.5   -1.48   50MA bounce (-|
|  KRYS     Pullback50      eq     $343.59  39.9   -0.45   50MA bounce (-|
|  LIVN     Pullback50      eq     $81.11   50.1   -1.13   50MA bounce (+|
|  SSD      Pullback50      eq     $193.07  57.1   -0.43   50MA bounce (-|
|                                                                        |
+========================================================================+

+========================================================================+
|                              ENTRY ORDERS                              |
+========================================================================+
|    ENTER [eq] JKHY  MA_Squeeze                                   $70.87|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    SKIP [eq] ARE  Pullback50                                      cap 3|
|    SKIP [eq] AON  Pullback50                                      cap 3|
|    SKIP [eq] BXP  Pullback50                                      cap 3|
|    SKIP [eq] CDW  Pullback50                                      cap 3|
|    SKIP [eq] DHI  Pullback50                                      cap 3|
|    SKIP [eq] ELV  Pullback50                                      cap 3|
|    SKIP [eq] ESS  Pullback50                                      cap 3|
|    SKIP [eq] EXR  Pullback50                                      cap 3|
|    SKIP [eq] INVH  Pullback50                                     cap 3|
|    SKIP [eq] KVUE  Pullback50                                     cap 3|
|    SKIP [eq] KDP  Pullback50                                      cap 3|
|    SKIP [eq] O  Pullback50                                        cap 3|
|    SKIP [eq] ROST  Pullback50                                     cap 3|
|    SKIP [eq] SPG  Pullback50                                      cap 3|
|    SKIP [eq] SYY  Pullback50                                      cap 3|
|    SKIP [eq] VTR  Pullback50                                      cap 3|
|    SKIP [eq] WY  Pullback50                                       cap 3|
|    SKIP [eq] ALV  Pullback50                                      cap 3|
|    SKIP [eq] AN  Pullback50                                       cap 3|
|    SKIP [eq] BRKR  Pullback50                                     cap 3|
|    SKIP [eq] CHH  Pullback50                                      cap 3|
|    SKIP [eq] CUBE  Pullback50                                     cap 3|
|    SKIP [eq] ELAN  Pullback50                                     cap 3|
|    SKIP [eq] EXEL  Pullback50                                     cap 3|
|    SKIP [eq] GHC  Pullback50                                      cap 3|
|    SKIP [eq] IRT  Pullback50                                      cap 3|
|    SKIP [eq] KRYS  Pullback50                                     cap 3|
|    SKIP [eq] LIVN  Pullback50                                     cap 3|
|    SKIP [eq] SSD  Pullback50                                      cap 3|
|    SKIP [eq] A  TrendResumption                                   cap 3|
|    SKIP [eq] EL  TrendResumption                                  cap 3|
|    SKIP [eq] COIN  VWAP_Reclaim                                   cap 3|
|    SKIP [eq] LOW  VWAP_Reclaim                                    cap 3|
|    SKIP [eq] PGR  VWAP_Reclaim                                    cap 3|
|    SKIP [eq] TGT  VWAP_Reclaim                                    cap 3|

+========================================================================+
|                         BUY FILL CONFIRMATION                          |
+========================================================================+
|  Pending submits                                                      1|
+------------------------------------------------------------------------+
|  JKHY                                                 still unconfirmed|
+========================================================================+
+========================================================================+

+========================================================================+
|                           GTC STOP PLACEMENT                           |
+========================================================================+
|  Waiting 5s for 1 buy submit(s) to settle...                           |
+========================================================================+

+========================================================================+
|                            SESSION SUMMARY                             |
+========================================================================+
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Strategy  VolumeSpike + 52wkLow (display only — schedule not enforced)|
|  Scanned                                                            897|
|  Signals                                                             36|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  1 unconfirmed|
|  Exits                                                                0|
|  Open pos                                                             3|
|  Equity                                                         $472.36|
|  Cash                                                           $245.20|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T15:50:23.035678-04:00 share=50% ===
2026-08-19 15:50:23,035 INFO === options_live_micro LIVE 2026-08-19T15:50:23.035678-04:00 share=50% ===
Live account equity $472.36 cash $245.20 #225458845 options_level=3
2026-08-19 15:50:23,092 INFO Live account equity $472.36 cash $245.20 #225458845 options_level=3
Live micro: manage/exits only
2026-08-19 15:50:23,150 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-08-19 15:50:23,159 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T195123Z

- UTC timestamp: `20260819T195123Z`
- GitHub run: [#7550](https://github.com/28twagg-ops/TradingBot/actions/runs/32295200175)
- Run id: `32295200175`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T195123Z_live_bot.log`, `logs/action_runs/20260819T195123Z_live_options.log`, `logs/action_runs/20260819T195123Z_options_bot.log`

### Live bot (tail)

```text
19:51:24  INFO      Mode: scan
19:51:24  INFO        [positions] 3/3 (3 valid)
19:51:24  INFO        SELL LIMIT JKHY  qty=0.435193828  limit=$162.61  id=2c78a741-7067-4036-a0a0-0f75b48cedca
19:51:54  INFO        SELL LIMIT filled JKHY (confirmed by position check)
19:51:55  INFO        TX logged: SELL JKHY  P&L 0.07%
19:51:55  INFO        Universe cache hit: 903 tickers (tickers_2026-08-19.json)
19:51:56  INFO        [universe] 40/901 (40 valid)
19:51:57  INFO        [universe] 80/901 (80 valid)
19:51:58  INFO        [universe] 120/901 (120 valid)
19:52:00  INFO        [universe] 160/901 (160 valid)
19:52:01  INFO        [universe] 200/901 (199 valid)
19:52:08  INFO        [universe] 240/901 (238 valid)
19:52:21  INFO        [universe] 280/901 (278 valid)
19:52:31  INFO        [universe] 320/901 (318 valid)
19:52:45  INFO        [universe] 360/901 (358 valid)
19:52:55  INFO        [universe] 400/901 (397 valid)
19:53:09  INFO        [universe] 440/901 (437 valid)
19:53:19  INFO        [universe] 480/901 (477 valid)
19:53:32  INFO        [universe] 520/901 (517 valid)
19:53:45  INFO        [universe] 560/901 (557 valid)
19:53:55  INFO        [universe] 600/901 (597 valid)
19:54:09  INFO        [universe] 640/901 (637 valid)
19:54:19  INFO        [universe] 680/901 (677 valid)
19:54:32  INFO        [universe] 720/901 (717 valid)
19:54:45  INFO        [universe] 760/901 (757 valid)
19:54:55  INFO        [universe] 800/901 (797 valid)
19:55:08  INFO        [universe] 840/901 (836 valid)
19:55:21  INFO        [universe] 880/901 (876 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T195622Z

- UTC timestamp: `20260819T195622Z`
- GitHub run: [#7551](https://github.com/28twagg-ops/TradingBot/actions/runs/32295654307)
- Run id: `32295654307`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T195622Z_live_bot.log`, `logs/action_runs/20260819T195622Z_live_options.log`, `logs/action_runs/20260819T195622Z_options_bot.log`

### Live bot (tail)

```text
... (149 earlier lines - see full log file)
20:00:49  INFO        place_all_stops: checking 1 positions...
20:00:49  INFO        STOP-MARKET placed MNST  qty=1 (pos=1.6350)  stop=$47.17  id=eefb2d5e-ee78-4db7-8cdc-dba48fec6f6b
20:00:49  INFO        Daily log -> logs/daily/2026-08-19.md
20:00:49  INFO        Dashboard written → logs/dashboard.md

|  LIVN     Pullback50      eq     $80.83   49.6   -0.99   50MA bounce (+|
|  SMG      RSIRecovery     eq     $61.27   30.6   0.76    RSI 20.7→30.6 |
|  SSD      Pullback50      eq     $192.92  56.9   -0.20   50MA bounce (-|
|  UTHR     Pullback50      eq     $529.09  51.6   -0.82   50MA bounce (-|
|                                                                        |
+========================================================================+

+========================================================================+
|                              ENTRY ORDERS                              |
+========================================================================+
|    ENTER [eq] JKHY  MA_Squeeze                                   $70.88|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    ENTER [eq] ARE  Pullback50                                    $70.88|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    SKIP [eq] AON  Pullback50                                      cap 3|
|    SKIP [eq] CDW  Pullback50                                      cap 3|
|    SKIP [eq] DHI  Pullback50                                      cap 3|
|    SKIP [eq] ESS  Pullback50                                      cap 3|
|    SKIP [eq] KDP  Pullback50                                      cap 3|
|    SKIP [eq] KVUE  Pullback50                                     cap 3|
|    SKIP [eq] O  Pullback50                                        cap 3|
|    SKIP [eq] ROST  Pullback50                                     cap 3|
|    SKIP [eq] SPG  Pullback50                                      cap 3|
|    SKIP [eq] WY  Pullback50                                       cap 3|
|    SKIP [eq] BRKR  Pullback50                                     cap 3|
|    SKIP [eq] CHH  Pullback50                                      cap 3|
|    SKIP [eq] CUBE  Pullback50                                     cap 3|
|    SKIP [eq] ELAN  Pullback50                                     cap 3|
|    SKIP [eq] EXEL  Pullback50                                     cap 3|
|    SKIP [eq] IRT  Pullback50                                      cap 3|
|    SKIP [eq] KRYS  Pullback50                                     cap 3|
|    SKIP [eq] LIVN  Pullback50                                     cap 3|
|    SKIP [eq] SSD  Pullback50                                      cap 3|
|    SKIP [eq] UTHR  Pullback50                                     cap 3|
|    SKIP [eq] ARE  RSIRecovery                                     cap 3|
|    SKIP [eq] COLM  RSIRecovery                                    cap 3|
|    SKIP [eq] SMG  RSIRecovery                                     cap 3|
|    SKIP [eq] A  TrendResumption                                   cap 3|
|    SKIP [eq] EL  TrendResumption                                  cap 3|
|    SKIP [eq] COIN  VWAP_Reclaim                                   cap 3|
|    SKIP [eq] LOW  VWAP_Reclaim                                    cap 3|
|    SKIP [eq] PGR  VWAP_Reclaim                                    cap 3|
|    SKIP [eq] TGT  VWAP_Reclaim                                    cap 3|

+========================================================================+
|                         BUY FILL CONFIRMATION                          |
+========================================================================+
|  Pending submits                                                      2|
+------------------------------------------------------------------------+
|  JKHY                                                 still unconfirmed|
|  ARE                                                  still unconfirmed|
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
|  Strategy  VolumeSpike + 52wkLow (display only — schedule not enforced)|
|  Scanned                                                            898|
|  Signals                                                             31|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  2 unconfirmed|
|  Exits                                                                1|
|  Open pos                                                             1|
|  Equity                                                         $472.56|
|  Cash                                                           $395.01|
+========================================================================+
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T200150Z

- UTC timestamp: `20260819T200150Z`
- GitHub run: [#7552](https://github.com/28twagg-ops/TradingBot/actions/runs/32296116556)
- Run id: `32296116556`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T200150Z_live_bot.log`, `logs/action_runs/20260819T200150Z_live_options.log`, `logs/action_runs/20260819T200150Z_options_bot.log`

### Live bot (tail)

```text
20:01:51  INFO      Mode: ext_exits
20:01:52  INFO        Daily log -> logs/daily/2026-08-19.md
20:01:52  INFO        Daily log reconciled -> logs/daily/2026-08-19.md (2 ledger rows)
20:01:53  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         20:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.0%  $+0.04        HOLDING until 9:35am scan (MomReversal)|
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
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T16:01:53.935114-04:00 share=50% ===
2026-08-19 16:01:53,935 INFO === options_live_micro LIVE 2026-08-19T16:01:53.935114-04:00 share=50% ===
Live account equity $472.56 cash $395.01 #225458845 options_level=3
2026-08-19 16:01:54,158 INFO Live account equity $472.56 cash $395.01 #225458845 options_level=3
Live micro: manage/exits only
2026-08-19 16:01:54,367 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-08-19 16:01:54,435 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T200620Z

- UTC timestamp: `20260819T200620Z`
- GitHub run: [#7553](https://github.com/28twagg-ops/TradingBot/actions/runs/32296580846)
- Run id: `32296580846`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T200620Z_live_bot.log`, `logs/action_runs/20260819T200620Z_live_options.log`, `logs/action_runs/20260819T200620Z_options_bot.log`

### Live bot (tail)

```text
20:06:21  INFO      Mode: ext_exits
20:06:21  INFO        Daily log -> logs/daily/2026-08-19.md
20:06:21  INFO        Daily log reconciled -> logs/daily/2026-08-19.md (3 ledger rows)
20:06:21  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         20:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.0%  $+0.04        HOLDING until 9:35am scan (MomReversal)|
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
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T16:06:22.379728-04:00 share=50% ===
2026-08-19 16:06:22,379 INFO === options_live_micro LIVE 2026-08-19T16:06:22.379728-04:00 share=50% ===
Live account equity $472.56 cash $395.01 #225458845 options_level=3
2026-08-19 16:06:22,465 INFO Live account equity $472.56 cash $395.01 #225458845 options_level=3
Live micro done. open_options=0 lots=0
2026-08-19 16:06:22,531 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T201058Z

- UTC timestamp: `20260819T201058Z`
- GitHub run: [#7554](https://github.com/28twagg-ops/TradingBot/actions/runs/32297042686)
- Run id: `32297042686`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T201058Z_live_bot.log`, `logs/action_runs/20260819T201058Z_live_options.log`, `logs/action_runs/20260819T201058Z_options_bot.log`

### Live bot (tail)

```text
20:10:58  INFO      Mode: ext_exits
20:10:59  INFO        Daily log -> logs/daily/2026-08-19.md
20:10:59  INFO        Daily log reconciled -> logs/daily/2026-08-19.md (3 ledger rows)
20:11:00  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         20:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.0%  $+0.04        HOLDING until 9:35am scan (MomReversal)|
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
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T16:11:01.145196-04:00 share=50% ===
2026-08-19 16:11:01,145 INFO === options_live_micro LIVE 2026-08-19T16:11:01.145196-04:00 share=50% ===
Live account equity $472.56 cash $395.01 #225458845 options_level=3
2026-08-19 16:11:01,371 INFO Live account equity $472.56 cash $395.01 #225458845 options_level=3
Live micro done. open_options=0 lots=0
2026-08-19 16:11:01,586 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T201608Z

- UTC timestamp: `20260819T201608Z`
- GitHub run: [#7555](https://github.com/28twagg-ops/TradingBot/actions/runs/32297502213)
- Run id: `32297502213`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T201608Z_live_bot.log`, `logs/action_runs/20260819T201608Z_live_options.log`, `logs/action_runs/20260819T201608Z_options_bot.log`

### Live bot (tail)

```text
20:16:09  INFO      Mode: ext_exits
20:16:09  INFO        Daily log -> logs/daily/2026-08-19.md
20:16:09  INFO        Daily log reconciled -> logs/daily/2026-08-19.md (3 ledger rows)
20:16:10  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         20:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.59|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.1%  $+0.07        HOLDING until 9:35am scan (MomReversal)|
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
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T16:16:10.820792-04:00 share=50% ===
2026-08-19 16:16:10,820 INFO === options_live_micro LIVE 2026-08-19T16:16:10.820792-04:00 share=50% ===
Live account equity $472.59 cash $395.01 #225458845 options_level=3
2026-08-19 16:16:10,865 INFO Live account equity $472.59 cash $395.01 #225458845 options_level=3
Live micro done. open_options=0 lots=0
2026-08-19 16:16:10,888 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260819T202053Z

- UTC timestamp: `20260819T202053Z`
- GitHub run: [#7556](https://github.com/28twagg-ops/TradingBot/actions/runs/32297953205)
- Run id: `32297953205`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260819T202053Z_live_bot.log`, `logs/action_runs/20260819T202053Z_live_options.log`, `logs/action_runs/20260819T202053Z_options_bot.log`

### Live bot (tail)

```text
20:20:54  INFO      Mode: ext_exits
20:20:55  INFO        Daily log -> logs/daily/2026-08-19.md
20:20:55  INFO        Daily log reconciled -> logs/daily/2026-08-19.md (3 ledger rows)
20:20:55  INFO        Daily log -> logs/daily/2026-08-19.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         20:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.70|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.2%  $+0.18        HOLDING until 9:35am scan (MomReversal)|
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
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
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

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-19T16:20:56.515165-04:00 share=50% ===
2026-08-19 16:20:56,515 INFO === options_live_micro LIVE 2026-08-19T16:20:56.515165-04:00 share=50% ===
Live account equity $472.70 cash $395.01 #225458845 options_level=3
2026-08-19 16:20:56,776 INFO Live account equity $472.70 cash $395.01 #225458845 options_level=3
Live micro done. open_options=0 lots=0
2026-08-19 16:20:56,991 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---
