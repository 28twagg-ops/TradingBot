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
