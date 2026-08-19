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
