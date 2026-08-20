# Daily Comprehensive Action Review - 2026-08-20

_Auto-generated from GitHub Actions run output. Each run appends a summary; full stdout is in linked per-run log files._
## Run 20260820T130059Z

- UTC timestamp: `20260820T130059Z`
- GitHub run: [#7600](https://github.com/28twagg-ops/TradingBot/actions/runs/32371805838)
- Run id: `32371805838`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T130059Z_live_bot.log`, `logs/action_runs/20260820T130059Z_live_options.log`, `logs/action_runs/20260820T130059Z_options_bot.log`

### Live bot (tail)

```text
13:00:59  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.12|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $472.12|
|  Cash                                                           $394.98|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $77.14|
|  Open P&L                                                        $-0.37|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (1 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  MNST     MomReversal     $77.14     $47.41   $47.18   -0.5%   $-0.37  |
|                                                                        |
|  Total invested                                                  $77.14|
|  Total open P&L                                                  $-0.37|
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
|  2026-08-19  SELL  AAPL  Pullback50  $79.01  P&L $+1.50                |
|  2026-08-19  SELL  JKHY  MA_Squeeze  $70.80  P&L $+0.05                |
|  2026-08-19  SELL  CDW  Pullback50  $77.10  P&L $-0.42                 |
|  2026-08-18  SELL  CNC  Pullback50  $77.65  P&L $+0.14                 |
|  2026-08-18  SELL  AON  Pullback50  $69.74  P&L $-0.36                 |
|  2026-08-18  SELL  AEE  Pullback50  $69.70  P&L $-0.40                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-20T09:01:01.272831-04:00 share=50% ===
2026-08-20 09:01:01,272 INFO === options_live_micro LIVE 2026-08-20T09:01:01.272831-04:00 share=50% ===
Live account equity $472.12 cash $394.98 #225458845 options_level=3
2026-08-20 09:01:01,475 INFO Live account equity $472.12 cash $394.98 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-08-20 09:01:01,533 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-08-20 09:01:01,592 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T130557Z

- UTC timestamp: `20260820T130557Z`
- GitHub run: [#7601](https://github.com/28twagg-ops/TradingBot/actions/runs/32372275364)
- Run id: `32372275364`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T130557Z_live_bot.log`, `logs/action_runs/20260820T130557Z_live_options.log`, `logs/action_runs/20260820T130557Z_options_bot.log`

### Live bot (tail)

```text
13:05:58  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:05 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.12|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $472.12|
|  Cash                                                           $394.98|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $77.14|
|  Open P&L                                                        $-0.37|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (1 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  MNST     MomReversal     $77.14     $47.41   $47.18   -0.5%   $-0.37  |
|                                                                        |
|  Total invested                                                  $77.14|
|  Total open P&L                                                  $-0.37|
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
|  2026-08-19  SELL  AAPL  Pullback50  $79.01  P&L $+1.50                |
|  2026-08-19  SELL  JKHY  MA_Squeeze  $70.80  P&L $+0.05                |
|  2026-08-19  SELL  CDW  Pullback50  $77.10  P&L $-0.42                 |
|  2026-08-18  SELL  CNC  Pullback50  $77.65  P&L $+0.14                 |
|  2026-08-18  SELL  AON  Pullback50  $69.74  P&L $-0.36                 |
|  2026-08-18  SELL  AEE  Pullback50  $69.70  P&L $-0.40                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-20T09:06:00.155646-04:00 share=50% ===
2026-08-20 09:06:00,155 INFO === options_live_micro LIVE 2026-08-20T09:06:00.155646-04:00 share=50% ===
Live account equity $472.12 cash $394.98 #225458845 options_level=3
2026-08-20 09:06:00,305 INFO Live account equity $472.12 cash $394.98 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-08-20 09:06:00,346 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-08-20 09:06:00,386 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T131051Z

- UTC timestamp: `20260820T131051Z`
- GitHub run: [#7602](https://github.com/28twagg-ops/TradingBot/actions/runs/32372731373)
- Run id: `32372731373`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T131051Z_live_bot.log`, `logs/action_runs/20260820T131051Z_live_options.log`, `logs/action_runs/20260820T131051Z_options_bot.log`

### Live bot (tail)

```text
13:10:52  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.12|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $472.12|
|  Cash                                                           $394.98|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $77.14|
|  Open P&L                                                        $-0.37|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (1 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  MNST     MomReversal     $77.14     $47.41   $47.18   -0.5%   $-0.37  |
|                                                                        |
|  Total invested                                                  $77.14|
|  Total open P&L                                                  $-0.37|
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
|  2026-08-19  SELL  AAPL  Pullback50  $79.01  P&L $+1.50                |
|  2026-08-19  SELL  JKHY  MA_Squeeze  $70.80  P&L $+0.05                |
|  2026-08-19  SELL  CDW  Pullback50  $77.10  P&L $-0.42                 |
|  2026-08-18  SELL  CNC  Pullback50  $77.65  P&L $+0.14                 |
|  2026-08-18  SELL  AON  Pullback50  $69.74  P&L $-0.36                 |
|  2026-08-18  SELL  AEE  Pullback50  $69.70  P&L $-0.40                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-20T09:10:53.038367-04:00 share=50% ===
2026-08-20 09:10:53,038 INFO === options_live_micro LIVE 2026-08-20T09:10:53.038367-04:00 share=50% ===
Live account equity $472.12 cash $394.98 #225458845 options_level=3
2026-08-20 09:10:53,082 INFO Live account equity $472.12 cash $394.98 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-08-20 09:10:53,090 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-08-20 09:10:53,098 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T131556Z

- UTC timestamp: `20260820T131556Z`
- GitHub run: [#7603](https://github.com/28twagg-ops/TradingBot/actions/runs/32373198471)
- Run id: `32373198471`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T131556Z_live_bot.log`, `logs/action_runs/20260820T131556Z_live_options.log`, `logs/action_runs/20260820T131556Z_options_bot.log`

### Live bot (tail)

```text
13:15:58  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:15 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.12|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $472.12|
|  Cash                                                           $394.98|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $77.14|
|  Open P&L                                                        $-0.37|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (1 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  MNST     MomReversal     $77.14     $47.41   $47.18   -0.5%   $-0.37  |
|                                                                        |
|  Total invested                                                  $77.14|
|  Total open P&L                                                  $-0.37|
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
|  2026-08-19  SELL  AAPL  Pullback50  $79.01  P&L $+1.50                |
|  2026-08-19  SELL  JKHY  MA_Squeeze  $70.80  P&L $+0.05                |
|  2026-08-19  SELL  CDW  Pullback50  $77.10  P&L $-0.42                 |
|  2026-08-18  SELL  CNC  Pullback50  $77.65  P&L $+0.14                 |
|  2026-08-18  SELL  AON  Pullback50  $69.74  P&L $-0.36                 |
|  2026-08-18  SELL  AEE  Pullback50  $69.70  P&L $-0.40                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-20T09:15:59.268237-04:00 share=50% ===
2026-08-20 09:15:59,268 INFO === options_live_micro LIVE 2026-08-20T09:15:59.268237-04:00 share=50% ===
Live account equity $472.12 cash $394.98 #225458845 options_level=3
2026-08-20 09:15:59,382 INFO Live account equity $472.12 cash $394.98 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-08-20 09:15:59,412 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-08-20 09:15:59,441 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T132050Z

- UTC timestamp: `20260820T132050Z`
- GitHub run: [#7604](https://github.com/28twagg-ops/TradingBot/actions/runs/32373665765)
- Run id: `32373665765`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T132050Z_live_bot.log`, `logs/action_runs/20260820T132050Z_live_options.log`, `logs/action_runs/20260820T132050Z_options_bot.log`

### Live bot (tail)

```text
13:20:51  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.07|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $472.07|
|  Cash                                                           $394.98|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $77.09|
|  Open P&L                                                        $-0.42|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (1 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  MNST     MomReversal     $77.09     $47.41   $47.15   -0.5%   $-0.42  |
|                                                                        |
|  Total invested                                                  $77.09|
|  Total open P&L                                                  $-0.42|
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
|  2026-08-19  SELL  AAPL  Pullback50  $79.01  P&L $+1.50                |
|  2026-08-19  SELL  JKHY  MA_Squeeze  $70.80  P&L $+0.05                |
|  2026-08-19  SELL  CDW  Pullback50  $77.10  P&L $-0.42                 |
|  2026-08-18  SELL  CNC  Pullback50  $77.65  P&L $+0.14                 |
|  2026-08-18  SELL  AON  Pullback50  $69.74  P&L $-0.36                 |
|  2026-08-18  SELL  AEE  Pullback50  $69.70  P&L $-0.40                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-20T09:20:52.811470-04:00 share=50% ===
2026-08-20 09:20:52,811 INFO === options_live_micro LIVE 2026-08-20T09:20:52.811470-04:00 share=50% ===
Live account equity $472.07 cash $394.98 #225458845 options_level=3
2026-08-20 09:20:52,854 INFO Live account equity $472.07 cash $394.98 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-08-20 09:20:52,870 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-08-20 09:20:52,878 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T132553Z

- UTC timestamp: `20260820T132553Z`
- GitHub run: [#7605](https://github.com/28twagg-ops/TradingBot/actions/runs/32374142705)
- Run id: `32374142705`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T132553Z_live_bot.log`, `logs/action_runs/20260820T132553Z_live_options.log`, `logs/action_runs/20260820T132553Z_options_bot.log`

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
|  Equity                                                         $472.30|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $472.30|
|  Cash                                                           $394.98|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $77.32|
|  Open P&L                                                        $-0.19|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (1 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  MNST     MomReversal     $77.32     $47.41   $47.29   -0.2%   $-0.19  |
|                                                                        |
|  Total invested                                                  $77.32|
|  Total open P&L                                                  $-0.19|
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
|  2026-08-19  SELL  AAPL  Pullback50  $79.01  P&L $+1.50                |
|  2026-08-19  SELL  JKHY  MA_Squeeze  $70.80  P&L $+0.05                |
|  2026-08-19  SELL  CDW  Pullback50  $77.10  P&L $-0.42                 |
|  2026-08-18  SELL  CNC  Pullback50  $77.65  P&L $+0.14                 |
|  2026-08-18  SELL  AON  Pullback50  $69.74  P&L $-0.36                 |
|  2026-08-18  SELL  AEE  Pullback50  $69.70  P&L $-0.40                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-20T09:25:55.259873-04:00 share=50% ===
2026-08-20 09:25:55,259 INFO === options_live_micro LIVE 2026-08-20T09:25:55.259873-04:00 share=50% ===
Live account equity $472.30 cash $394.98 #225458845 options_level=3
2026-08-20 09:25:55,374 INFO Live account equity $472.30 cash $394.98 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-08-20 09:25:55,402 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-08-20 09:25:55,431 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T133053Z

- UTC timestamp: `20260820T133053Z`
- GitHub run: [#7606](https://github.com/28twagg-ops/TradingBot/actions/runs/32374614728)
- Run id: `32374614728`
- Live bot: exit=`0`, duration=`219s`
- Live options: exit=`0`, duration=`18s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T133053Z_live_bot.log`, `logs/action_runs/20260820T133053Z_live_options.log`, `logs/action_runs/20260820T133053Z_options_bot.log`

### Live bot (tail)

```text
13:30:54  INFO      Mode: morning_prep
13:30:56  INFO        [prep_positions] 3/3 (3 valid)
13:30:56  INFO      Fetching tickers (universe=both)...
13:30:56  INFO        S&P 500: 503
13:30:57  INFO        MidCap 400: 400
13:30:57  INFO        Total: 903 tickers
13:30:58  INFO        [prep_universe] 40/900 (40 valid)
13:31:00  INFO        [prep_universe] 80/900 (80 valid)
13:31:02  INFO        [prep_universe] 120/900 (120 valid)
13:31:04  INFO        [prep_universe] 160/900 (160 valid)
13:31:06  INFO        [prep_universe] 200/900 (199 valid)
13:31:11  INFO        [prep_universe] 240/900 (238 valid)
13:31:21  INFO        [prep_universe] 280/900 (278 valid)
13:31:35  INFO        [prep_universe] 320/900 (318 valid)
13:31:47  INFO        [prep_universe] 360/900 (358 valid)
13:31:58  INFO        [prep_universe] 400/900 (397 valid)
13:32:10  INFO        [prep_universe] 440/900 (437 valid)
13:32:21  INFO        [prep_universe] 480/900 (477 valid)
13:32:35  INFO        [prep_universe] 520/900 (517 valid)
13:32:46  INFO        [prep_universe] 560/900 (557 valid)
13:33:00  INFO        [prep_universe] 600/900 (597 valid)
13:33:10  INFO        [prep_universe] 640/900 (637 valid)
13:33:24  INFO        [prep_universe] 680/900 (677 valid)
13:33:34  INFO        [prep_universe] 720/900 (717 valid)
13:33:48  INFO        [prep_universe] 760/900 (757 valid)
13:33:58  INFO        [prep_universe] 800/900 (797 valid)
13:34:12  INFO        [prep_universe] 840/900 (836 valid)
13:34:22  INFO        [prep_universe] 880/900 (876 valid)
13:34:29  INFO        [prep_universe] 900/900 (896 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:30 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $471.34|
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
|  Invested                                                       $171.10|
|  Open P&L                                                        $-0.74|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ARE      Pullback50      $70.30     $50.78   $50.37   -0.8%   $-0.57  |
|  JKHY     MA_Squeeze      $70.88     $163.31  $163.34  +0.0%   $+0.01  |
|  MNST     MomReversal     $29.93     $47.41   $47.13   -0.6%   $-0.18  |
+========================================================================+

+========================================================================+
|                            OPEN SELL ORDERS                            |
+========================================================================+
|  Count                                                                0|
|                                                                        |
|  No open sell orders.                                                  |
|                                                                        |
+========================================================================+

+========================================================================+
|                              PREP SUMMARY                              |
+========================================================================+
|  Saved                                                              yes|
|  Exit candidates                                                      3|
|  Signal candidates                                                   37|
|  Universe scanned                                                   900|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-20T09:34:32.837652-04:00 share=50% ===
2026-08-20 09:34:32,837 INFO === options_live_micro LIVE 2026-08-20T09:34:32.837652-04:00 share=50% ===
Live account equity $471.67 cash $300.24 #225458845 options_level=3
2026-08-20 09:34:33,035 INFO Live account equity $471.67 cash $300.24 #225458845 options_level=3
Live micro sleeve $236 (50% of $472) deployed $0 open_strategies=0/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
2026-08-20 09:34:33,287 INFO Live micro sleeve $236 (50% of $472) deployed $0 open_strategies=0/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-20 09:34:33,287 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 11
2026-08-20 09:34:47,173 INFO Live micro signals: 11
  try S404 100%win/+80%med COST
2026-08-20 09:34:47,174 INFO   try S404 100%win/+80%med COST
  skip S404 COST: no contract under $75
2026-08-20 09:34:47,767 INFO   skip S404 COST: no contract under $75
  try S404 100%win/+80%med CRWD
2026-08-20 09:34:47,767 INFO   try S404 100%win/+80%med CRWD
  skip S404 CRWD: no contract under $75
2026-08-20 09:34:47,975 INFO   skip S404 CRWD: no contract under $75
  try S404 100%win/+80%med HD
2026-08-20 09:34:47,975 INFO   try S404 100%win/+80%med HD
  skip S404 HD: no contract under $75
2026-08-20 09:34:48,162 INFO   skip S404 HD: no contract under $75
  try S404 100%win/+80%med WMT
2026-08-20 09:34:48,162 INFO   try S404 100%win/+80%med WMT
LIVE BUY S404 100%win WMT WMT260821C00110000 limit=0.09 ask=0.10 cost=$10 id=e6cd86dc-0e0a-4897-bbe7-543a0fcc9847
2026-08-20 09:34:48,421 INFO LIVE BUY S404 100%win WMT WMT260821C00110000 limit=0.09 ask=0.10 cost=$10 id=e6cd86dc-0e0a-4897-bbe7-543a0fcc9847
  try S406 56%win/+58%med COST
2026-08-20 09:34:48,421 INFO   try S406 56%win/+58%med COST
  skip S406 COST: no contract under $75
2026-08-20 09:34:48,670 INFO   skip S406 COST: no contract under $75
  try S406 56%win/+58%med CPB
2026-08-20 09:34:48,670 INFO   try S406 56%win/+58%med CPB
LIVE BUY S406 56%win CPB CPB260821C00023000 limit=0.61 ask=0.62 cost=$62 id=e00e118a-a87b-4b3e-948e-a89950a35282
2026-08-20 09:34:48,930 INFO LIVE BUY S406 56%win CPB CPB260821C00023000 limit=0.61 ask=0.62 cost=$62 id=e00e118a-a87b-4b3e-948e-a89950a35282
  try S218 56%win/+49%med CL
2026-08-20 09:34:48,930 INFO   try S218 56%win/+49%med CL
  skip S218 CL: no contract under $75
2026-08-20 09:34:49,157 INFO   skip S218 CL: no contract under $75
  try S218 56%win/+49%med COST
2026-08-20 09:34:49,157 INFO   try S218 56%win/+49%med COST
  skip S218 COST: no contract under $75
2026-08-20 09:34:49,216 INFO   skip S218 COST: no contract under $75
  try S210 55%win/+47%med ABBV
2026-08-20 09:34:49,216 INFO   try S210 55%win/+47%med ABBV
  skip S210 ABBV: no contract under $75
2026-08-20 09:34:49,448 INFO   skip S210 ABBV: no contract under $75
  try S210 55%win/+47%med SJM
2026-08-20 09:34:49,448 INFO   try S210 55%win/+47%med SJM
  skip S210 SJM: no contract under $75
2026-08-20 09:34:49,651 INFO   skip S210 SJM: no contract under $75
  try S210 55%win/+47%med XEL
2026-08-20 09:34:49,651 INFO   try S210 55%win/+47%med XEL
  skip S210 XEL: no contract under $75
2026-08-20 09:34:49,860 INFO   skip S210 XEL: no contract under $75
LIVE PROT STOP CPB260821C00023000 x1 stop=0.30 id=17cd36da-1eae-4243-b2e5-944af72e9976
2026-08-20 09:34:50,068 INFO LIVE PROT STOP CPB260821C00023000 x1 stop=0.30 id=17cd36da-1eae-4243-b2e5-944af72e9976
Live micro done. open_options=1 lots=2
2026-08-20 09:34:50,126 INFO Live micro done. open_options=1 lots=2
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T133550Z

- UTC timestamp: `20260820T133550Z`
- GitHub run: [#7607](https://github.com/28twagg-ops/TradingBot/actions/runs/32375093895)
- Run id: `32375093895`
- Live bot: exit=`0`, duration=`218s`
- Live options: exit=`0`, duration=`6s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T133550Z_live_bot.log`, `logs/action_runs/20260820T133550Z_live_options.log`, `logs/action_runs/20260820T133550Z_options_bot.log`

### Live bot (tail)

```text
13:35:51  INFO      Mode: morning_prep
13:35:52  INFO        [prep_positions] 3/3 (3 valid)
13:35:52  INFO        Universe cache hit: 903 tickers (tickers_2026-08-20.json)
13:35:54  INFO        [prep_universe] 40/900 (40 valid)
13:35:55  INFO        [prep_universe] 80/900 (80 valid)
13:35:56  INFO        [prep_universe] 120/900 (120 valid)
13:35:58  INFO        [prep_universe] 160/900 (160 valid)
13:35:59  INFO        [prep_universe] 200/900 (199 valid)
13:36:07  INFO        [prep_universe] 240/900 (238 valid)
13:36:18  INFO        [prep_universe] 280/900 (278 valid)
13:36:33  INFO        [prep_universe] 320/900 (318 valid)
13:36:44  INFO        [prep_universe] 360/900 (358 valid)
13:36:56  INFO        [prep_universe] 400/900 (397 valid)
13:37:06  INFO        [prep_universe] 440/900 (437 valid)
13:37:19  INFO        [prep_universe] 480/900 (477 valid)
13:37:31  INFO        [prep_universe] 520/900 (517 valid)
13:37:44  INFO        [prep_universe] 560/900 (557 valid)
13:37:55  INFO        [prep_universe] 600/900 (597 valid)
13:38:05  INFO        [prep_universe] 640/900 (637 valid)
13:38:19  INFO        [prep_universe] 680/900 (677 valid)
13:38:30  INFO        [prep_universe] 720/900 (717 valid)
13:38:43  INFO        [prep_universe] 760/900 (757 valid)
13:38:54  INFO        [prep_universe] 800/900 (797 valid)
13:39:08  INFO        [prep_universe] 840/900 (836 valid)
13:39:18  INFO        [prep_universe] 880/900 (876 valid)
13:39:26  INFO        [prep_universe] 900/900 (896 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:35 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $443.63|
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
|  Invested                                                       $171.48|
|  Open P&L                                                        $-0.36|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ARE      Pullback50      $70.18     $50.78   $50.28   -1.0%   $-0.69  |
|  JKHY     MA_Squeeze      $71.14     $163.31  $163.94  +0.4%   $+0.27  |
|  MNST     MomReversal     $30.16     $47.41   $47.50   +0.2%   $+0.06  |
+========================================================================+

+========================================================================+
|                            OPEN SELL ORDERS                            |
+========================================================================+
|  Count                                                                1|
|  TICKER    TYPE              QTY       LIMIT       STOP                |
+------------------------------------------------------------------------+
|  CPB2608~  OrderType.STOP_~  1         0.28        0.3                 |
+========================================================================+

+========================================================================+
|                              PREP SUMMARY                              |
+========================================================================+
|  Saved                                                              yes|
|  Exit candidates                                                      2|
|  Signal candidates                                                   51|
|  Universe scanned                                                   900|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-20T09:39:29.376335-04:00 share=50% ===
2026-08-20 09:39:29,376 INFO === options_live_micro LIVE 2026-08-20T09:39:29.376335-04:00 share=50% ===
Live account equity $443.81 cash $231.15 #225458845 options_level=3
2026-08-20 09:39:29,612 INFO Live account equity $443.81 cash $231.15 #225458845 options_level=3
Live micro fill confirmed S404 WMT260821C00110000
2026-08-20 09:39:29,681 INFO Live micro fill confirmed S404 WMT260821C00110000
Live micro fill confirmed S406 CPB260821C00023000
2026-08-20 09:39:29,681 INFO Live micro fill confirmed S406 CPB260821C00023000
Live micro hold S404 WMT260821C00110000 -33.3% (tp +50% / sl -50%)
2026-08-20 09:39:29,754 INFO Live micro hold S404 WMT260821C00110000 -33.3% (tp +50% / sl -50%)
Live micro hold S406 CPB260821C00023000 -41.7% (tp +50% / sl -50%)
2026-08-20 09:39:29,754 INFO Live micro hold S406 CPB260821C00023000 -41.7% (tp +50% / sl -50%)
LIVE PROT STOP WMT260821C00110000 x1 stop=0.04 id=34614c71-7372-4108-9da6-2915f0d7a2c8
2026-08-20 09:39:30,010 INFO LIVE PROT STOP WMT260821C00110000 x1 stop=0.04 id=34614c71-7372-4108-9da6-2915f0d7a2c8
Live micro sleeve $222 (50% of $444) deployed $41 open_strategies=2/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
2026-08-20 09:39:30,154 INFO Live micro sleeve $222 (50% of $444) deployed $41 open_strategies=2/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-20 09:39:30,154 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 11
2026-08-20 09:39:32,133 INFO Live micro signals: 11
  skip S404 COST: strategy already open (paper bucket rule)
2026-08-20 09:39:32,134 INFO   skip S404 COST: strategy already open (paper bucket rule)
  skip S404 CRWD: strategy already open (paper bucket rule)
2026-08-20 09:39:32,134 INFO   skip S404 CRWD: strategy already open (paper bucket rule)
  skip S404 HD: strategy already open (paper bucket rule)
2026-08-20 09:39:32,134 INFO   skip S404 HD: strategy already open (paper bucket rule)
  skip S404 WMT: strategy already open (paper bucket rule)
2026-08-20 09:39:32,134 INFO   skip S404 WMT: strategy already open (paper bucket rule)
  skip S406 COST: strategy already open (paper bucket rule)
2026-08-20 09:39:32,134 INFO   skip S406 COST: strategy already open (paper bucket rule)
  skip S406 CPB: strategy already open (paper bucket rule)
2026-08-20 09:39:32,134 INFO   skip S406 CPB: strategy already open (paper bucket rule)
  try S218 56%win/+49%med CL
2026-08-20 09:39:32,134 INFO   try S218 56%win/+49%med CL
  skip S218 CL: no contract under $75
2026-08-20 09:39:32,774 INFO   skip S218 CL: no contract under $75
  try S218 56%win/+49%med COST
2026-08-20 09:39:32,774 INFO   try S218 56%win/+49%med COST
  skip S218 COST: no contract under $75
2026-08-20 09:39:33,124 INFO   skip S218 COST: no contract under $75
  try S210 55%win/+47%med ABBV
2026-08-20 09:39:33,124 INFO   try S210 55%win/+47%med ABBV
  skip S210 ABBV: no contract under $75
2026-08-20 09:39:33,407 INFO   skip S210 ABBV: no contract under $75
  try S210 55%win/+47%med SJM
2026-08-20 09:39:33,407 INFO   try S210 55%win/+47%med SJM
  skip S210 SJM: no contract under $75
2026-08-20 09:39:33,626 INFO   skip S210 SJM: no contract under $75
  try S210 55%win/+47%med XEL
2026-08-20 09:39:33,627 INFO   try S210 55%win/+47%med XEL
  skip S210 XEL: no contract under $75
2026-08-20 09:39:33,921 INFO   skip S210 XEL: no contract under $75
Live micro done. open_options=2 lots=2
2026-08-20 09:39:34,214 INFO Live micro done. open_options=2 lots=2
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T134256Z

- UTC timestamp: `20260820T134256Z`
- GitHub run: [#7608](https://github.com/28twagg-ops/TradingBot/actions/runs/32375569537)
- Run id: `32375569537`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T134256Z_live_bot.log`, `logs/action_runs/20260820T134256Z_live_options.log`, `logs/action_runs/20260820T134256Z_options_bot.log`

### Live bot (tail)

```text
13:42:56  INFO      Mode: morning_prep
13:42:57  INFO        [prep_positions] 3/3 (3 valid)
13:42:57  INFO        Universe cache hit: 903 tickers (tickers_2026-08-20.json)
13:42:59  INFO        [prep_universe] 40/900 (40 valid)
13:43:00  INFO        [prep_universe] 80/900 (80 valid)
13:43:01  INFO        [prep_universe] 120/900 (120 valid)
13:43:03  INFO        [prep_universe] 160/900 (160 valid)
13:43:04  INFO        [prep_universe] 200/900 (199 valid)
13:43:11  INFO        [prep_universe] 240/900 (238 valid)
13:43:25  INFO        [prep_universe] 280/900 (278 valid)
13:43:35  INFO        [prep_universe] 320/900 (318 valid)
13:43:48  INFO        [prep_universe] 360/900 (358 valid)
13:43:59  INFO        [prep_universe] 400/900 (397 valid)
13:44:11  INFO        [prep_universe] 440/900 (437 valid)
13:44:24  INFO        [prep_universe] 480/900 (477 valid)
13:44:35  INFO        [prep_universe] 520/900 (517 valid)
13:44:47  INFO        [prep_universe] 560/900 (557 valid)
13:45:00  INFO        [prep_universe] 600/900 (597 valid)
13:45:11  INFO        [prep_universe] 640/900 (637 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T134620Z

- UTC timestamp: `20260820T134620Z`
- GitHub run: [#7609](https://github.com/28twagg-ops/TradingBot/actions/runs/32376045765)
- Run id: `32376045765`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T134620Z_live_bot.log`, `logs/action_runs/20260820T134620Z_live_options.log`, `logs/action_runs/20260820T134620Z_options_bot.log`

### Live bot (tail)

```text
13:46:21  INFO      Mode: morning_scan
13:46:22  INFO        [positions] 3/3 (3 valid)
13:46:22  INFO        SELL LIMIT ARE  qty=1.3956282  limit=$50.50  id=35d7969d-d3aa-45a9-b2ec-8853e3a5de88
13:46:52  INFO        SELL LIMIT filled ARE (confirmed by position check)
13:46:52  INFO        TX logged: SELL ARE  P&L -0.34%
13:46:52  INFO        SELL LIMIT JKHY  qty=0.433959953  limit=$164.97  id=8a468b6a-2350-43d7-a21e-7ecb0a4cf76e
13:47:23  INFO        SELL LIMIT not filled for JKHY, falling back to market
13:47:23  INFO        SELL MARKET JKHY closed
13:47:25  INFO        TX logged: SELL JKHY  P&L 1.05%
13:47:25  INFO        Universe cache hit: 903 tickers (tickers_2026-08-20.json)
13:47:26  INFO        [universe] 40/902 (40 valid)
13:47:27  INFO        [universe] 80/902 (80 valid)
13:47:29  INFO        [universe] 120/902 (120 valid)
13:47:31  INFO        [universe] 160/902 (160 valid)
13:47:32  INFO        [universe] 200/902 (199 valid)
13:47:39  INFO        [universe] 240/902 (238 valid)
13:47:50  INFO        [universe] 280/902 (278 valid)
13:48:03  INFO        [universe] 320/902 (318 valid)
13:48:13  INFO        [universe] 360/902 (358 valid)
13:48:26  INFO        [universe] 400/902 (397 valid)
13:48:39  INFO        [universe] 440/902 (437 valid)
13:48:49  INFO        [universe] 480/902 (477 valid)
13:49:02  INFO        [universe] 520/902 (517 valid)
13:49:15  INFO        [universe] 560/902 (557 valid)
13:49:25  INFO        [universe] 600/902 (597 valid)
13:49:38  INFO        [universe] 640/902 (637 valid)
13:49:51  INFO        [universe] 680/902 (677 valid)
13:50:02  INFO        [universe] 720/902 (717 valid)
13:50:15  INFO        [universe] 760/902 (757 valid)
13:50:25  INFO        [universe] 800/902 (797 valid)
13:50:39  INFO        [universe] 840/902 (836 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T135152Z

- UTC timestamp: `20260820T135152Z`
- GitHub run: [#7610](https://github.com/28twagg-ops/TradingBot/actions/runs/32376523368)
- Run id: `32376523368`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T135152Z_live_bot.log`, `logs/action_runs/20260820T135152Z_live_options.log`, `logs/action_runs/20260820T135152Z_options_bot.log`

### Live bot (tail)

```text
13:51:53  INFO      Mode: morning_scan
13:51:53  INFO        [positions] 1/1 (1 valid)
13:51:53  INFO        Universe cache hit: 903 tickers (tickers_2026-08-20.json)
13:51:55  INFO        [universe] 40/902 (40 valid)
13:51:56  INFO        [universe] 80/902 (80 valid)
13:51:57  INFO        [universe] 120/902 (120 valid)
13:51:59  INFO        [universe] 160/902 (160 valid)
13:52:00  INFO        [universe] 200/902 (199 valid)
13:52:10  INFO        [universe] 240/902 (238 valid)
13:52:21  INFO        [universe] 280/902 (278 valid)
13:52:34  INFO        [universe] 320/902 (318 valid)
13:52:47  INFO        [universe] 360/902 (358 valid)
13:52:57  INFO        [universe] 400/902 (397 valid)
13:53:10  INFO        [universe] 440/902 (437 valid)
13:53:20  INFO        [universe] 480/902 (477 valid)
13:53:34  INFO        [universe] 520/902 (517 valid)
13:53:47  INFO        [universe] 560/902 (557 valid)
13:53:57  INFO        [universe] 600/902 (597 valid)
13:54:10  INFO        [universe] 640/902 (637 valid)
13:54:23  INFO        [universe] 680/902 (677 valid)
13:54:33  INFO        [universe] 720/902 (717 valid)
13:54:46  INFO        [universe] 760/902 (757 valid)
13:54:59  INFO        [universe] 800/902 (797 valid)
13:55:09  INFO        [universe] 840/902 (836 valid)
13:55:23  INFO        [universe] 880/902 (876 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T135636Z

- UTC timestamp: `20260820T135636Z`
- GitHub run: [#7611](https://github.com/28twagg-ops/TradingBot/actions/runs/32377001996)
- Run id: `32377001996`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T135636Z_live_bot.log`, `logs/action_runs/20260820T135636Z_live_options.log`, `logs/action_runs/20260820T135636Z_options_bot.log`

### Live bot (tail)

```text
13:56:37  INFO      Mode: morning_scan
13:56:39  INFO        [positions] 3/3 (3 valid)
13:56:39  INFO        SELL LIMIT ARE  qty=1.376352547  limit=$50.64  id=af31537b-a392-424e-bbb9-10a3601b7c21
13:57:10  INFO        SELL LIMIT filled ARE (confirmed by position check)
13:57:10  INFO        TX logged: SELL ARE  P&L -0.18%
13:57:10  INFO        Universe cache hit: 903 tickers (tickers_2026-08-20.json)
13:57:11  INFO        [universe] 40/901 (40 valid)
13:57:12  INFO        [universe] 80/901 (80 valid)
13:57:13  INFO        [universe] 120/901 (120 valid)
13:57:15  INFO        [universe] 160/901 (160 valid)
13:57:16  INFO        [universe] 200/901 (199 valid)
13:57:23  INFO        [universe] 240/901 (238 valid)
13:57:37  INFO        [universe] 280/901 (278 valid)
13:57:47  INFO        [universe] 320/901 (318 valid)
13:58:00  INFO        [universe] 360/901 (358 valid)
13:58:11  INFO        [universe] 400/901 (397 valid)
13:58:24  INFO        [universe] 440/901 (437 valid)
13:58:35  INFO        [universe] 480/901 (477 valid)
13:58:48  INFO        [universe] 520/901 (517 valid)
13:58:59  INFO        [universe] 560/901 (557 valid)
13:59:12  INFO        [universe] 600/901 (597 valid)
13:59:22  INFO        [universe] 640/901 (637 valid)
13:59:36  INFO        [universe] 680/901 (677 valid)
13:59:46  INFO        [universe] 720/901 (717 valid)
13:59:59  INFO        [universe] 760/901 (757 valid)
14:00:14  INFO        [universe] 800/901 (797 valid)
14:00:25  INFO        [universe] 840/901 (836 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T140132Z

- UTC timestamp: `20260820T140132Z`
- GitHub run: [#7612](https://github.com/28twagg-ops/TradingBot/actions/runs/32377500623)
- Run id: `32377500623`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`5s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T140132Z_live_bot.log`, `logs/action_runs/20260820T140132Z_live_options.log`, `logs/action_runs/20260820T140132Z_options_bot.log`

### Live bot (tail)

```text
14:01:33  INFO      Mode: exits
14:01:34  INFO        Daily log -> logs/daily/2026-08-20.md
14:01:34  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (2 ledger rows)
14:01:34  INFO        place_all_stops: checking 4 positions...
14:01:34  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
14:01:34  INFO        STOP skipped MNST: fractional (0.6350 shares) — software exit will handle it
14:01:35  INFO        [positions] 2/2 (2 valid)
14:01:35  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $451.16|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AON  P&L -0.0%  $-0.02                                            HOLD|
|  MNST  P&L +0.5%  $+0.15                                           HOLD|
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
|  CPB260821C00023000      $0.60    $0.45    -25.0%   $-15.00   $45.00   |
|  WMT260821C00110000      $0.09    $0.03    -66.7%   $-6.00    $3.00    |
|                                                                        |
|  Options open P&L                                               $-21.00|
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
=== options_live_micro LIVE 2026-08-20T10:01:36.379898-04:00 share=50% ===
2026-08-20 10:01:36,379 INFO === options_live_micro LIVE 2026-08-20T10:01:36.379898-04:00 share=50% ===
Live account equity $451.16 cash $302.97 #225458845 options_level=3
2026-08-20 10:01:36,453 INFO Live account equity $451.16 cash $302.97 #225458845 options_level=3
LIVE EXIT stop_loss (-66.7%) WMT260821C00110000 x1 limit=0.04 id=709af2b2-487c-4768-b9f3-c8bab5fb7bb6
2026-08-20 10:01:37,267 INFO LIVE EXIT stop_loss (-66.7%) WMT260821C00110000 x1 limit=0.04 id=709af2b2-487c-4768-b9f3-c8bab5fb7bb6
Live micro hold S406 CPB260821C00023000 -25.0% (tp +50% / sl -50%)
2026-08-20 10:01:37,267 INFO Live micro hold S406 CPB260821C00023000 -25.0% (tp +50% / sl -50%)
Live micro sleeve $226 (50% of $451) deployed $48 open_strategies=2/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
2026-08-20 10:01:37,365 INFO Live micro sleeve $226 (50% of $451) deployed $48 open_strategies=2/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-20 10:01:37,365 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 11
2026-08-20 10:01:39,315 INFO Live micro signals: 11
  skip S404 COST: strategy already open (paper bucket rule)
2026-08-20 10:01:39,315 INFO   skip S404 COST: strategy already open (paper bucket rule)
  skip S404 CRWD: strategy already open (paper bucket rule)
2026-08-20 10:01:39,315 INFO   skip S404 CRWD: strategy already open (paper bucket rule)
  skip S404 HD: strategy already open (paper bucket rule)
2026-08-20 10:01:39,315 INFO   skip S404 HD: strategy already open (paper bucket rule)
  skip S404 WMT: strategy already open (paper bucket rule)
2026-08-20 10:01:39,316 INFO   skip S404 WMT: strategy already open (paper bucket rule)
  skip S406 COST: strategy already open (paper bucket rule)
2026-08-20 10:01:39,316 INFO   skip S406 COST: strategy already open (paper bucket rule)
  skip S406 CPB: strategy already open (paper bucket rule)
2026-08-20 10:01:39,316 INFO   skip S406 CPB: strategy already open (paper bucket rule)
  try S218 56%win/+49%med CL
2026-08-20 10:01:39,316 INFO   try S218 56%win/+49%med CL
  skip S218 CL: no contract under $75
2026-08-20 10:01:39,596 INFO   skip S218 CL: no contract under $75
  try S218 56%win/+49%med COST
2026-08-20 10:01:39,597 INFO   try S218 56%win/+49%med COST
  skip S218 COST: no contract under $75
2026-08-20 10:01:39,963 INFO   skip S218 COST: no contract under $75
  try S210 55%win/+47%med ABBV
2026-08-20 10:01:39,964 INFO   try S210 55%win/+47%med ABBV
  skip S210 ABBV: no contract under $75
2026-08-20 10:01:40,292 INFO   skip S210 ABBV: no contract under $75
  try S210 55%win/+47%med SJM
2026-08-20 10:01:40,292 INFO   try S210 55%win/+47%med SJM
  skip S210 SJM: no contract under $75
2026-08-20 10:01:40,457 INFO   skip S210 SJM: no contract under $75
  try S210 55%win/+47%med XEL
2026-08-20 10:01:40,458 INFO   try S210 55%win/+47%med XEL
  skip S210 XEL: no contract under $75
2026-08-20 10:01:40,697 INFO   skip S210 XEL: no contract under $75
Live micro done. open_options=2 lots=1
2026-08-20 10:01:40,736 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T140555Z

- UTC timestamp: `20260820T140555Z`
- GitHub run: [#7613](https://github.com/28twagg-ops/TradingBot/actions/runs/32378004081)
- Run id: `32378004081`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`6s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T140555Z_live_bot.log`, `logs/action_runs/20260820T140555Z_live_options.log`, `logs/action_runs/20260820T140555Z_options_bot.log`

### Live bot (tail)

```text
14:05:56  INFO      Mode: exits
14:05:57  INFO        Daily log -> logs/daily/2026-08-20.md
14:05:57  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (3 ledger rows)
14:05:57  INFO        place_all_stops: checking 4 positions...
14:05:57  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
14:05:57  INFO        STOP skipped MNST: fractional (0.6350 shares) — software exit will handle it
14:05:58  INFO        [positions] 2/2 (2 valid)
14:05:58  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:05 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $436.53|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.4%  $+0.12                                           HOLD|
|  AON  P&L +0.5%  $+0.38                                            HOLD|
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
|  CPB260821C00023000      $0.60    $0.30    -50.0%   $-30.00   $30.00   |
|  WMT260821C00110000      $0.09    $0.03    -66.7%   $-6.00    $3.00    |
|                                                                        |
|  Options open P&L                                               $-36.00|
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
=== options_live_micro LIVE 2026-08-20T10:05:59.721065-04:00 share=50% ===
2026-08-20 10:05:59,721 INFO === options_live_micro LIVE 2026-08-20T10:05:59.721065-04:00 share=50% ===
Live account equity $436.52 cash $302.97 #225458845 options_level=3
2026-08-20 10:05:59,978 INFO Live account equity $436.52 cash $302.97 #225458845 options_level=3
LIVE EXIT stop_loss (-50.0%) CPB260821C00023000 x1 limit=0.31 id=17ac582e-cc6c-4ef7-af83-c7f7ff772a03
2026-08-20 10:06:00,951 INFO LIVE EXIT stop_loss (-50.0%) CPB260821C00023000 x1 limit=0.31 id=17ac582e-cc6c-4ef7-af83-c7f7ff772a03
Live micro sleeve $218 (50% of $437) deployed $3 open_strategies=2/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
2026-08-20 10:06:01,135 INFO Live micro sleeve $218 (50% of $437) deployed $3 open_strategies=2/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-20 10:06:01,135 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 11
2026-08-20 10:06:03,044 INFO Live micro signals: 11
  skip S404 COST: strategy already open (paper bucket rule)
2026-08-20 10:06:03,044 INFO   skip S404 COST: strategy already open (paper bucket rule)
  skip S404 CRWD: strategy already open (paper bucket rule)
2026-08-20 10:06:03,044 INFO   skip S404 CRWD: strategy already open (paper bucket rule)
  skip S404 HD: strategy already open (paper bucket rule)
2026-08-20 10:06:03,044 INFO   skip S404 HD: strategy already open (paper bucket rule)
  skip S404 WMT: strategy already open (paper bucket rule)
2026-08-20 10:06:03,044 INFO   skip S404 WMT: strategy already open (paper bucket rule)
  skip S406 COST: strategy already open (paper bucket rule)
2026-08-20 10:06:03,044 INFO   skip S406 COST: strategy already open (paper bucket rule)
  skip S406 CPB: strategy already open (paper bucket rule)
2026-08-20 10:06:03,044 INFO   skip S406 CPB: strategy already open (paper bucket rule)
  try S218 56%win/+49%med CL
2026-08-20 10:06:03,045 INFO   try S218 56%win/+49%med CL
  skip S218 CL: no contract under $75
2026-08-20 10:06:03,584 INFO   skip S218 CL: no contract under $75
  try S218 56%win/+49%med COST
2026-08-20 10:06:03,584 INFO   try S218 56%win/+49%med COST
  skip S218 COST: no contract under $75
2026-08-20 10:06:03,913 INFO   skip S218 COST: no contract under $75
  try S210 55%win/+47%med ABBV
2026-08-20 10:06:03,913 INFO   try S210 55%win/+47%med ABBV
  skip S210 ABBV: no contract under $75
2026-08-20 10:06:04,237 INFO   skip S210 ABBV: no contract under $75
  try S210 55%win/+47%med SJM
2026-08-20 10:06:04,237 INFO   try S210 55%win/+47%med SJM
  skip S210 SJM: no contract under $75
2026-08-20 10:06:04,551 INFO   skip S210 SJM: no contract under $75
  try S210 55%win/+47%med XEL
2026-08-20 10:06:04,552 INFO   try S210 55%win/+47%med XEL
  skip S210 XEL: no contract under $75
2026-08-20 10:06:04,888 INFO   skip S210 XEL: no contract under $75
Live micro done. open_options=1 lots=0
2026-08-20 10:06:05,073 INFO Live micro done. open_options=1 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T141100Z

- UTC timestamp: `20260820T141100Z`
- GitHub run: [#7614](https://github.com/28twagg-ops/TradingBot/actions/runs/32378498789)
- Run id: `32378498789`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`3s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T141100Z_live_bot.log`, `logs/action_runs/20260820T141100Z_live_options.log`, `logs/action_runs/20260820T141100Z_options_bot.log`

### Live bot (tail)

```text
14:11:02  INFO      Mode: exits
14:11:02  INFO        Daily log -> logs/daily/2026-08-20.md
14:11:02  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (3 ledger rows)
14:11:02  INFO        place_all_stops: checking 3 positions...
14:11:02  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
14:11:02  INFO        STOP skipped MNST: fractional (0.6350 shares) — software exit will handle it
14:11:03  INFO        [positions] 2/2 (2 valid)
14:11:03  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $441.22|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AON  P&L +0.2%  $+0.13                                            HOLD|
|  MNST  P&L +0.4%  $+0.11                                           HOLD|
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
|  WMT260821C00110000      $0.09    $0.03    -66.7%   $-6.00    $3.00    |
|                                                                        |
|  Options open P&L                                                $-6.00|
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
=== options_live_micro LIVE 2026-08-20T10:11:03.942415-04:00 share=50% ===
2026-08-20 10:11:03,942 INFO === options_live_micro LIVE 2026-08-20T10:11:03.942415-04:00 share=50% ===
Live account equity $441.21 cash $337.91 #225458845 options_level=3
2026-08-20 10:11:04,030 INFO Live account equity $441.21 cash $337.91 #225458845 options_level=3
Live micro sleeve $221 (50% of $441) deployed $3 open_strategies=2/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
2026-08-20 10:11:04,077 INFO Live micro sleeve $221 (50% of $441) deployed $3 open_strategies=2/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-20 10:11:04,077 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 11
2026-08-20 10:11:05,354 INFO Live micro signals: 11
  skip S404 COST: strategy already open (paper bucket rule)
2026-08-20 10:11:05,354 INFO   skip S404 COST: strategy already open (paper bucket rule)
  skip S404 CRWD: strategy already open (paper bucket rule)
2026-08-20 10:11:05,354 INFO   skip S404 CRWD: strategy already open (paper bucket rule)
  skip S404 HD: strategy already open (paper bucket rule)
2026-08-20 10:11:05,355 INFO   skip S404 HD: strategy already open (paper bucket rule)
  skip S404 WMT: strategy already open (paper bucket rule)
2026-08-20 10:11:05,355 INFO   skip S404 WMT: strategy already open (paper bucket rule)
  skip S406 COST: strategy already open (paper bucket rule)
2026-08-20 10:11:05,355 INFO   skip S406 COST: strategy already open (paper bucket rule)
  skip S406 CPB: strategy already open (paper bucket rule)
2026-08-20 10:11:05,355 INFO   skip S406 CPB: strategy already open (paper bucket rule)
  try S218 56%win/+49%med CL
2026-08-20 10:11:05,355 INFO   try S218 56%win/+49%med CL
  skip S218 CL: no contract under $75
2026-08-20 10:11:05,573 INFO   skip S218 CL: no contract under $75
  try S218 56%win/+49%med COST
2026-08-20 10:11:05,573 INFO   try S218 56%win/+49%med COST
  skip S218 COST: no contract under $75
2026-08-20 10:11:05,668 INFO   skip S218 COST: no contract under $75
  try S210 55%win/+47%med ABBV
2026-08-20 10:11:05,668 INFO   try S210 55%win/+47%med ABBV
  skip S210 ABBV: no contract under $75
2026-08-20 10:11:05,722 INFO   skip S210 ABBV: no contract under $75
  try S210 55%win/+47%med SJM
2026-08-20 10:11:05,722 INFO   try S210 55%win/+47%med SJM
  skip S210 SJM: no contract under $75
2026-08-20 10:11:05,843 INFO   skip S210 SJM: no contract under $75
  try S210 55%win/+47%med XEL
2026-08-20 10:11:05,843 INFO   try S210 55%win/+47%med XEL
  skip S210 XEL: no contract under $75
2026-08-20 10:11:05,904 INFO   skip S210 XEL: no contract under $75
Live micro done. open_options=1 lots=0
2026-08-20 10:11:05,923 INFO Live micro done. open_options=1 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T141547Z

- UTC timestamp: `20260820T141547Z`
- GitHub run: [#7615](https://github.com/28twagg-ops/TradingBot/actions/runs/32378996933)
- Run id: `32378996933`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`4s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T141547Z_live_bot.log`, `logs/action_runs/20260820T141547Z_live_options.log`, `logs/action_runs/20260820T141547Z_options_bot.log`

### Live bot (tail)

```text
14:15:48  INFO      Mode: exits
14:15:49  INFO        Daily log -> logs/daily/2026-08-20.md
14:15:49  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (3 ledger rows)
14:15:49  INFO        place_all_stops: checking 3 positions...
14:15:49  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
14:15:49  INFO        STOP skipped MNST: fractional (0.6350 shares) — software exit will handle it
14:15:49  INFO        [positions] 2/2 (2 valid)
14:15:50  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:15 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $441.32|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AON  P&L +0.3%  $+0.24                                            HOLD|
|  MNST  P&L +0.4%  $+0.13                                           HOLD|
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
|  WMT260821C00110000      $0.09    $0.03    -66.7%   $-6.00    $3.00    |
|                                                                        |
|  Options open P&L                                                $-6.00|
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
=== options_live_micro LIVE 2026-08-20T10:15:50.668171-04:00 share=50% ===
2026-08-20 10:15:50,668 INFO === options_live_micro LIVE 2026-08-20T10:15:50.668171-04:00 share=50% ===
Live account equity $441.34 cash $337.91 #225458845 options_level=3
2026-08-20 10:15:50,913 INFO Live account equity $441.34 cash $337.91 #225458845 options_level=3
Live micro sleeve $221 (50% of $441) deployed $3 open_strategies=2/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
2026-08-20 10:15:51,337 INFO Live micro sleeve $221 (50% of $441) deployed $3 open_strategies=2/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-20 10:15:51,338 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 11
2026-08-20 10:15:52,189 INFO Live micro signals: 11
  skip S404 COST: strategy already open (paper bucket rule)
2026-08-20 10:15:52,189 INFO   skip S404 COST: strategy already open (paper bucket rule)
  skip S404 CRWD: strategy already open (paper bucket rule)
2026-08-20 10:15:52,189 INFO   skip S404 CRWD: strategy already open (paper bucket rule)
  skip S404 HD: strategy already open (paper bucket rule)
2026-08-20 10:15:52,189 INFO   skip S404 HD: strategy already open (paper bucket rule)
  skip S404 WMT: strategy already open (paper bucket rule)
2026-08-20 10:15:52,189 INFO   skip S404 WMT: strategy already open (paper bucket rule)
  skip S406 COST: strategy already open (paper bucket rule)
2026-08-20 10:15:52,189 INFO   skip S406 COST: strategy already open (paper bucket rule)
  skip S406 CPB: strategy already open (paper bucket rule)
2026-08-20 10:15:52,189 INFO   skip S406 CPB: strategy already open (paper bucket rule)
  try S218 56%win/+49%med CL
2026-08-20 10:15:52,189 INFO   try S218 56%win/+49%med CL
  skip S218 CL: no contract under $75
2026-08-20 10:15:52,940 INFO   skip S218 CL: no contract under $75
  try S218 56%win/+49%med COST
2026-08-20 10:15:52,940 INFO   try S218 56%win/+49%med COST
  skip S218 COST: no contract under $75
2026-08-20 10:15:53,493 INFO   skip S218 COST: no contract under $75
  try S210 55%win/+47%med ABBV
2026-08-20 10:15:53,493 INFO   try S210 55%win/+47%med ABBV
  skip S210 ABBV: no contract under $75
2026-08-20 10:15:53,877 INFO   skip S210 ABBV: no contract under $75
  try S210 55%win/+47%med SJM
2026-08-20 10:15:53,877 INFO   try S210 55%win/+47%med SJM
  skip S210 SJM: no contract under $75
2026-08-20 10:15:54,166 INFO   skip S210 SJM: no contract under $75
  try S210 55%win/+47%med XEL
2026-08-20 10:15:54,166 INFO   try S210 55%win/+47%med XEL
  skip S210 XEL: no contract under $75
2026-08-20 10:15:54,585 INFO   skip S210 XEL: no contract under $75
Live micro done. open_options=1 lots=0
2026-08-20 10:15:54,794 INFO Live micro done. open_options=1 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T142050Z

- UTC timestamp: `20260820T142050Z`
- GitHub run: [#7616](https://github.com/28twagg-ops/TradingBot/actions/runs/32379498384)
- Run id: `32379498384`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`5s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T142050Z_live_bot.log`, `logs/action_runs/20260820T142050Z_live_options.log`, `logs/action_runs/20260820T142050Z_options_bot.log`

### Live bot (tail)

```text
14:20:51  INFO      Mode: exits
14:20:52  INFO        Daily log -> logs/daily/2026-08-20.md
14:20:52  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (3 ledger rows)
14:20:52  INFO        place_all_stops: checking 3 positions...
14:20:52  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
14:20:52  INFO        STOP skipped MNST: fractional (0.6350 shares) — software exit will handle it
14:20:53  INFO        [positions] 2/2 (2 valid)
14:20:53  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $441.27|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.3%  $+0.08                                           HOLD|
|  AON  P&L +0.3%  $+0.22                                            HOLD|
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
|  WMT260821C00110000      $0.09    $0.03    -66.7%   $-6.00    $3.00    |
|                                                                        |
|  Options open P&L                                                $-6.00|
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
=== options_live_micro LIVE 2026-08-20T10:20:54.228498-04:00 share=50% ===
2026-08-20 10:20:54,228 INFO === options_live_micro LIVE 2026-08-20T10:20:54.228498-04:00 share=50% ===
Live account equity $441.27 cash $337.91 #225458845 options_level=3
2026-08-20 10:20:54,455 INFO Live account equity $441.27 cash $337.91 #225458845 options_level=3
Live micro sleeve $221 (50% of $441) deployed $3 open_strategies=2/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
2026-08-20 10:20:54,740 INFO Live micro sleeve $221 (50% of $441) deployed $3 open_strategies=2/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-20 10:20:54,740 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 11
2026-08-20 10:20:56,656 INFO Live micro signals: 11
  skip S404 COST: strategy already open (paper bucket rule)
2026-08-20 10:20:56,656 INFO   skip S404 COST: strategy already open (paper bucket rule)
  skip S404 CRWD: strategy already open (paper bucket rule)
2026-08-20 10:20:56,656 INFO   skip S404 CRWD: strategy already open (paper bucket rule)
  skip S404 HD: strategy already open (paper bucket rule)
2026-08-20 10:20:56,656 INFO   skip S404 HD: strategy already open (paper bucket rule)
  skip S404 WMT: strategy already open (paper bucket rule)
2026-08-20 10:20:56,657 INFO   skip S404 WMT: strategy already open (paper bucket rule)
  skip S406 COST: strategy already open (paper bucket rule)
2026-08-20 10:20:56,657 INFO   skip S406 COST: strategy already open (paper bucket rule)
  skip S406 CPB: strategy already open (paper bucket rule)
2026-08-20 10:20:56,657 INFO   skip S406 CPB: strategy already open (paper bucket rule)
  try S218 56%win/+49%med CL
2026-08-20 10:20:56,657 INFO   try S218 56%win/+49%med CL
  skip S218 CL: no contract under $75
2026-08-20 10:20:57,539 INFO   skip S218 CL: no contract under $75
  try S218 56%win/+49%med COST
2026-08-20 10:20:57,540 INFO   try S218 56%win/+49%med COST
  skip S218 COST: no contract under $75
2026-08-20 10:20:57,851 INFO   skip S218 COST: no contract under $75
  try S210 55%win/+47%med ABBV
2026-08-20 10:20:57,851 INFO   try S210 55%win/+47%med ABBV
  skip S210 ABBV: no contract under $75
2026-08-20 10:20:58,126 INFO   skip S210 ABBV: no contract under $75
  try S210 55%win/+47%med SJM
2026-08-20 10:20:58,126 INFO   try S210 55%win/+47%med SJM
  skip S210 SJM: no contract under $75
2026-08-20 10:20:58,433 INFO   skip S210 SJM: no contract under $75
  try S210 55%win/+47%med XEL
2026-08-20 10:20:58,433 INFO   try S210 55%win/+47%med XEL
  skip S210 XEL: no contract under $75
2026-08-20 10:20:58,678 INFO   skip S210 XEL: no contract under $75
Live micro done. open_options=1 lots=0
2026-08-20 10:20:58,822 INFO Live micro done. open_options=1 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T142554Z

- UTC timestamp: `20260820T142554Z`
- GitHub run: [#7617](https://github.com/28twagg-ops/TradingBot/actions/runs/32380000108)
- Run id: `32380000108`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`6s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T142554Z_live_bot.log`, `logs/action_runs/20260820T142554Z_live_options.log`, `logs/action_runs/20260820T142554Z_options_bot.log`

### Live bot (tail)

```text
14:25:55  INFO      Mode: exits
14:25:56  INFO        Daily log -> logs/daily/2026-08-20.md
14:25:56  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (3 ledger rows)
14:25:56  INFO        place_all_stops: checking 3 positions...
14:25:56  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
14:25:56  INFO        STOP skipped MNST: fractional (0.6350 shares) — software exit will handle it
14:25:56  INFO        [positions] 2/2 (2 valid)
14:25:57  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:25 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $440.16|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.1%  $+0.03                                           HOLD|
|  AON  P&L +0.2%  $+0.16                                            HOLD|
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
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
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
=== options_live_micro LIVE 2026-08-20T10:25:58.095972-04:00 share=50% ===
2026-08-20 10:25:58,096 INFO === options_live_micro LIVE 2026-08-20T10:25:58.095972-04:00 share=50% ===
Live account equity $440.16 cash $337.91 #225458845 options_level=3
2026-08-20 10:25:58,343 INFO Live account equity $440.16 cash $337.91 #225458845 options_level=3
Live micro sleeve $220 (50% of $440) deployed $2 open_strategies=2/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
2026-08-20 10:25:58,650 INFO Live micro sleeve $220 (50% of $440) deployed $2 open_strategies=2/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-20 10:25:58,650 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 11
2026-08-20 10:26:00,560 INFO Live micro signals: 11
  skip S404 COST: strategy already open (paper bucket rule)
2026-08-20 10:26:00,561 INFO   skip S404 COST: strategy already open (paper bucket rule)
  skip S404 CRWD: strategy already open (paper bucket rule)
2026-08-20 10:26:00,561 INFO   skip S404 CRWD: strategy already open (paper bucket rule)
  skip S404 HD: strategy already open (paper bucket rule)
2026-08-20 10:26:00,561 INFO   skip S404 HD: strategy already open (paper bucket rule)
  skip S404 WMT: strategy already open (paper bucket rule)
2026-08-20 10:26:00,561 INFO   skip S404 WMT: strategy already open (paper bucket rule)
  skip S406 COST: strategy already open (paper bucket rule)
2026-08-20 10:26:00,561 INFO   skip S406 COST: strategy already open (paper bucket rule)
  skip S406 CPB: strategy already open (paper bucket rule)
2026-08-20 10:26:00,561 INFO   skip S406 CPB: strategy already open (paper bucket rule)
  try S218 56%win/+49%med CL
2026-08-20 10:26:00,562 INFO   try S218 56%win/+49%med CL
  skip S218 CL: no contract under $75
2026-08-20 10:26:01,430 INFO   skip S218 CL: no contract under $75
  try S218 56%win/+49%med COST
2026-08-20 10:26:01,430 INFO   try S218 56%win/+49%med COST
  skip S218 COST: no contract under $75
2026-08-20 10:26:02,133 INFO   skip S218 COST: no contract under $75
  try S210 55%win/+47%med ABBV
2026-08-20 10:26:02,133 INFO   try S210 55%win/+47%med ABBV
  skip S210 ABBV: no contract under $75
2026-08-20 10:26:02,461 INFO   skip S210 ABBV: no contract under $75
  try S210 55%win/+47%med SJM
2026-08-20 10:26:02,461 INFO   try S210 55%win/+47%med SJM
  skip S210 SJM: no contract under $75
2026-08-20 10:26:02,870 INFO   skip S210 SJM: no contract under $75
  try S210 55%win/+47%med XEL
2026-08-20 10:26:02,870 INFO   try S210 55%win/+47%med XEL
  skip S210 XEL: no contract under $75
2026-08-20 10:26:03,292 INFO   skip S210 XEL: no contract under $75
Live micro done. open_options=1 lots=0
2026-08-20 10:26:03,433 INFO Live micro done. open_options=1 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T143057Z

- UTC timestamp: `20260820T143057Z`
- GitHub run: [#7618](https://github.com/28twagg-ops/TradingBot/actions/runs/32380496347)
- Run id: `32380496347`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`6s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T143057Z_live_bot.log`, `logs/action_runs/20260820T143057Z_live_options.log`, `logs/action_runs/20260820T143057Z_options_bot.log`

### Live bot (tail)

```text
14:30:58  INFO      Mode: exits
14:30:59  INFO        Daily log -> logs/daily/2026-08-20.md
14:30:59  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (3 ledger rows)
14:30:59  INFO        place_all_stops: checking 3 positions...
14:30:59  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
14:30:59  INFO        STOP skipped MNST: fractional (0.6350 shares) — software exit will handle it
14:30:59  INFO        [positions] 2/2 (2 valid)
14:31:00  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:30 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $440.16|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L -0.1%  $-0.03                                           HOLD|
|  AON  P&L +0.3%  $+0.22                                            HOLD|
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
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
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
=== options_live_micro LIVE 2026-08-20T10:31:01.075092-04:00 share=50% ===
2026-08-20 10:31:01,075 INFO === options_live_micro LIVE 2026-08-20T10:31:01.075092-04:00 share=50% ===
Live account equity $440.16 cash $337.91 #225458845 options_level=3
2026-08-20 10:31:01,283 INFO Live account equity $440.16 cash $337.91 #225458845 options_level=3
Live micro sleeve $220 (50% of $440) deployed $2 open_strategies=2/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
2026-08-20 10:31:01,561 INFO Live micro sleeve $220 (50% of $440) deployed $2 open_strategies=2/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-20 10:31:01,561 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 11
2026-08-20 10:31:02,830 INFO Live micro signals: 11
  skip S404 COST: strategy already open (paper bucket rule)
2026-08-20 10:31:02,830 INFO   skip S404 COST: strategy already open (paper bucket rule)
  skip S404 CRWD: strategy already open (paper bucket rule)
2026-08-20 10:31:02,830 INFO   skip S404 CRWD: strategy already open (paper bucket rule)
  skip S404 HD: strategy already open (paper bucket rule)
2026-08-20 10:31:02,830 INFO   skip S404 HD: strategy already open (paper bucket rule)
  skip S404 WMT: strategy already open (paper bucket rule)
2026-08-20 10:31:02,830 INFO   skip S404 WMT: strategy already open (paper bucket rule)
  skip S406 COST: strategy already open (paper bucket rule)
2026-08-20 10:31:02,830 INFO   skip S406 COST: strategy already open (paper bucket rule)
  skip S406 CPB: strategy already open (paper bucket rule)
2026-08-20 10:31:02,830 INFO   skip S406 CPB: strategy already open (paper bucket rule)
  try S218 56%win/+49%med CL
2026-08-20 10:31:02,830 INFO   try S218 56%win/+49%med CL
  skip S218 CL: no contract under $75
2026-08-20 10:31:03,678 INFO   skip S218 CL: no contract under $75
  try S218 56%win/+49%med COST
2026-08-20 10:31:03,678 INFO   try S218 56%win/+49%med COST
  skip S218 COST: no contract under $75
2026-08-20 10:31:04,308 INFO   skip S218 COST: no contract under $75
  try S210 55%win/+47%med ABBV
2026-08-20 10:31:04,309 INFO   try S210 55%win/+47%med ABBV
  skip S210 ABBV: no contract under $75
2026-08-20 10:31:05,076 INFO   skip S210 ABBV: no contract under $75
  try S210 55%win/+47%med SJM
2026-08-20 10:31:05,076 INFO   try S210 55%win/+47%med SJM
  skip S210 SJM: no contract under $75
2026-08-20 10:31:05,661 INFO   skip S210 SJM: no contract under $75
  try S210 55%win/+47%med XEL
2026-08-20 10:31:05,661 INFO   try S210 55%win/+47%med XEL
  skip S210 XEL: no contract under $75
2026-08-20 10:31:06,340 INFO   skip S210 XEL: no contract under $75
Live micro done. open_options=1 lots=0
2026-08-20 10:31:06,459 INFO Live micro done. open_options=1 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T144140Z

- UTC timestamp: `20260820T144140Z`
- GitHub run: [#7620](https://github.com/28twagg-ops/TradingBot/actions/runs/32381502517)
- Run id: `32381502517`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`3s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T144140Z_live_bot.log`, `logs/action_runs/20260820T144140Z_live_options.log`, `logs/action_runs/20260820T144140Z_options_bot.log`

### Live bot (tail)

```text
14:41:41  INFO      Mode: exits
14:41:41  INFO        Daily log -> logs/daily/2026-08-20.md
14:41:41  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (3 ledger rows)
14:41:41  INFO        place_all_stops: checking 3 positions...
14:41:41  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
14:41:41  INFO        STOP skipped MNST: fractional (0.6350 shares) — software exit will handle it
14:41:41  INFO        [positions] 2/2 (2 valid)
14:41:42  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $440.17|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L -0.3%  $-0.08                                           HOLD|
|  AON  P&L +0.4%  $+0.28                                            HOLD|
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
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
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
=== options_live_micro LIVE 2026-08-20T10:41:42.735108-04:00 share=50% ===
2026-08-20 10:41:42,735 INFO === options_live_micro LIVE 2026-08-20T10:41:42.735108-04:00 share=50% ===
Live account equity $440.17 cash $337.91 #225458845 options_level=3
2026-08-20 10:41:42,810 INFO Live account equity $440.17 cash $337.91 #225458845 options_level=3
Live micro sleeve $220 (50% of $440) deployed $2 open_strategies=2/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
2026-08-20 10:41:42,890 INFO Live micro sleeve $220 (50% of $440) deployed $2 open_strategies=2/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-20 10:41:42,891 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 11
2026-08-20 10:41:44,553 INFO Live micro signals: 11
  skip S404 COST: strategy already open (paper bucket rule)
2026-08-20 10:41:44,553 INFO   skip S404 COST: strategy already open (paper bucket rule)
  skip S404 CRWD: strategy already open (paper bucket rule)
2026-08-20 10:41:44,553 INFO   skip S404 CRWD: strategy already open (paper bucket rule)
  skip S404 HD: strategy already open (paper bucket rule)
2026-08-20 10:41:44,553 INFO   skip S404 HD: strategy already open (paper bucket rule)
  skip S404 WMT: strategy already open (paper bucket rule)
2026-08-20 10:41:44,553 INFO   skip S404 WMT: strategy already open (paper bucket rule)
  skip S406 COST: strategy already open (paper bucket rule)
2026-08-20 10:41:44,553 INFO   skip S406 COST: strategy already open (paper bucket rule)
  skip S406 CPB: strategy already open (paper bucket rule)
2026-08-20 10:41:44,553 INFO   skip S406 CPB: strategy already open (paper bucket rule)
  try S218 56%win/+49%med CL
2026-08-20 10:41:44,554 INFO   try S218 56%win/+49%med CL
  skip S218 CL: no contract under $75
2026-08-20 10:41:44,714 INFO   skip S218 CL: no contract under $75
  try S218 56%win/+49%med COST
2026-08-20 10:41:44,714 INFO   try S218 56%win/+49%med COST
  skip S218 COST: no contract under $75
2026-08-20 10:41:44,782 INFO   skip S218 COST: no contract under $75
  try S210 55%win/+47%med ABBV
2026-08-20 10:41:44,783 INFO   try S210 55%win/+47%med ABBV
  skip S210 ABBV: no contract under $75
2026-08-20 10:41:44,836 INFO   skip S210 ABBV: no contract under $75
  try S210 55%win/+47%med SJM
2026-08-20 10:41:44,836 INFO   try S210 55%win/+47%med SJM
  skip S210 SJM: no contract under $75
2026-08-20 10:41:44,875 INFO   skip S210 SJM: no contract under $75
  try S210 55%win/+47%med XEL
2026-08-20 10:41:44,876 INFO   try S210 55%win/+47%med XEL
  skip S210 XEL: no contract under $75
2026-08-20 10:41:44,953 INFO   skip S210 XEL: no contract under $75
Live micro done. open_options=1 lots=0
2026-08-20 10:41:45,002 INFO Live micro done. open_options=1 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T144556Z

- UTC timestamp: `20260820T144556Z`
- GitHub run: [#7621](https://github.com/28twagg-ops/TradingBot/actions/runs/32382002420)
- Run id: `32382002420`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`6s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T144556Z_live_bot.log`, `logs/action_runs/20260820T144556Z_live_options.log`, `logs/action_runs/20260820T144556Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 821 | 41.8 | -47.5 | +15.4 | $+8,207 |
| TAINTED | 1761 | 33.0 | -39.3 | +12.2 | $-9,205 |
| KEEP-only | 294 | 63.3 | +37.5 | +42.9 | $+5,699 |
| KEEP-only recent | 106 | 58.5 | +50.0 | +54.8 | $+1,673 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406
- KILL strategies (16): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-17T19:56:23.633587-04:00","date":"2026-08-17","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":261.1,"phases_s":{"reconcile":140.41},"signals":0,"placed":0,"equity":null,"open_positions":14,"pending_orders":0,"open_lots":45,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"7335","github_run_id":"32082431205","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:45:57  INFO      Mode: exits
14:45:58  INFO        Daily log -> logs/daily/2026-08-20.md
14:45:58  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (3 ledger rows)
14:45:58  INFO        place_all_stops: checking 3 positions...
14:45:58  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
14:45:58  INFO        STOP skipped MNST: fractional (0.6350 shares) — software exit will handle it
14:45:58  INFO        [positions] 2/2 (2 valid)
14:45:59  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:45 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $440.35|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L -0.1%  $-0.04                                           HOLD|
|  AON  P&L +0.6%  $+0.42                                            HOLD|
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
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
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
=== options_live_micro LIVE 2026-08-20T10:45:59.984352-04:00 share=50% ===
2026-08-20 10:45:59,984 INFO === options_live_micro LIVE 2026-08-20T10:45:59.984352-04:00 share=50% ===
Live account equity $440.35 cash $337.91 #225458845 options_level=3
2026-08-20 10:46:00,256 INFO Live account equity $440.35 cash $337.91 #225458845 options_level=3
Live micro sleeve $220 (50% of $440) deployed $2 open_strategies=2/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
2026-08-20 10:46:00,648 INFO Live micro sleeve $220 (50% of $440) deployed $2 open_strategies=2/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-20 10:46:00,648 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 11
2026-08-20 10:46:02,535 INFO Live micro signals: 11
  skip S404 COST: strategy already open (paper bucket rule)
2026-08-20 10:46:02,535 INFO   skip S404 COST: strategy already open (paper bucket rule)
  skip S404 CRWD: strategy already open (paper bucket rule)
2026-08-20 10:46:02,535 INFO   skip S404 CRWD: strategy already open (paper bucket rule)
  skip S404 HD: strategy already open (paper bucket rule)
2026-08-20 10:46:02,535 INFO   skip S404 HD: strategy already open (paper bucket rule)
  skip S404 WMT: strategy already open (paper bucket rule)
2026-08-20 10:46:02,535 INFO   skip S404 WMT: strategy already open (paper bucket rule)
  skip S406 COST: strategy already open (paper bucket rule)
2026-08-20 10:46:02,535 INFO   skip S406 COST: strategy already open (paper bucket rule)
  skip S406 CPB: strategy already open (paper bucket rule)
2026-08-20 10:46:02,535 INFO   skip S406 CPB: strategy already open (paper bucket rule)
  try S218 56%win/+49%med CL
2026-08-20 10:46:02,536 INFO   try S218 56%win/+49%med CL
LIVE BUY S218 56%win CL CL260821C00090000 limit=0.52 ask=0.53 cost=$53 id=4099c642-2cc0-4f31-b470-61757da7a595
2026-08-20 10:46:03,492 INFO LIVE BUY S218 56%win CL CL260821C00090000 limit=0.52 ask=0.53 cost=$53 id=4099c642-2cc0-4f31-b470-61757da7a595
  skip S218 COST: strategy already open (paper bucket rule)
2026-08-20 10:46:03,492 INFO   skip S218 COST: strategy already open (paper bucket rule)
  try S210 55%win/+47%med ABBV
2026-08-20 10:46:03,492 INFO   try S210 55%win/+47%med ABBV
  skip S210 ABBV: no contract under $75
2026-08-20 10:46:04,024 INFO   skip S210 ABBV: no contract under $75
  try S210 55%win/+47%med SJM
2026-08-20 10:46:04,024 INFO   try S210 55%win/+47%med SJM
  skip S210 SJM: no contract under $75
2026-08-20 10:46:04,437 INFO   skip S210 SJM: no contract under $75
  try S210 55%win/+47%med XEL
2026-08-20 10:46:04,437 INFO   try S210 55%win/+47%med XEL
  skip S210 XEL: no contract under $75
2026-08-20 10:46:04,847 INFO   skip S210 XEL: no contract under $75
LIVE PROT STOP CL260821C00090000 x1 stop=0.26 id=f9c6e1e9-ecfc-4364-96f8-36190d133315
2026-08-20 10:46:05,089 INFO LIVE PROT STOP CL260821C00090000 x1 stop=0.26 id=f9c6e1e9-ecfc-4364-96f8-36190d133315
Live micro done. open_options=2 lots=1
2026-08-20 10:46:05,162 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=41 paper_keys=yes dry_run=False
  alpaca positions=12
  FLAG b449|S367|7eae09da missing from Alpaca
  FLAG b448|S367|61b1450d missing from Alpaca
  FLAG b321|S356|0b0b6401 missing from Alpaca
  FLAG b320|S356|25c8ebed missing from Alpaca
  FLAG b99|S211|8ac90a4a missing from Alpaca
  FLAG b98|S211|c05d2ba2 missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-20T10:46:07.864823-04:00 ===

[Run context]
2026-08-20 10:46:08,127 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-20 10:46:16,245 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-20 10:46:32,327 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
2026-08-20 10:46:56,416 WARNING paper get_account failed attempt 4/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 32s
2026-08-20 10:47:28,492 WARNING paper get_account failed attempt 5/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 40s
2026-08-20 10:48:08,566 ERROR paper get_account failed after 6 attempts: {"code":50010000,"message":"internal server error occurred"}
WARN: get_account failed ({"code":50010000,"message":"internal server error occurred"}) but positions OK (n=12). Keys are fine; Alpaca account endpoint is flaky. Continuing manage/exits; skipping new entries until equity is readable.
2026-08-20 10:48:08,729 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-20 10:48:16,804 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-20 10:48:32,878 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
2026-08-20 10:48:56,954 WARNING paper get_account failed attempt 4/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 32s
2026-08-20 10:49:29,028 WARNING paper get_account failed attempt 5/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 40s
2026-08-20 10:50:09,147 ERROR paper get_account failed after 6 attempts: {"code":50010000,"message":"internal server error occurred"}
2026-08-20 10:50:09,254 WARNING lab get_account failed attempt 1/3: {"code":50010000,"message":"internal server error occurred"}
2026-08-20 10:50:19,330 WARNING lab get_account failed attempt 2/3: {"code":50010000,"message":"internal server error occurred"}
```

---

## Run 20260820T145657Z

- UTC timestamp: `20260820T145657Z`
- GitHub run: [#7623](https://github.com/28twagg-ops/TradingBot/actions/runs/32383005623)
- Run id: `32383005623`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`4s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T145657Z_live_bot.log`, `logs/action_runs/20260820T145657Z_live_options.log`, `logs/action_runs/20260820T145657Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 821 | 41.8 | -47.5 | +15.4 | $+8,207 |
| TAINTED | 1761 | 33.0 | -39.3 | +12.2 | $-9,205 |
| KEEP-only | 294 | 63.3 | +37.5 | +42.9 | $+5,699 |
| KEEP-only recent | 106 | 58.5 | +50.0 | +54.8 | $+1,673 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406
- KILL strategies (16): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-17T19:56:23.633587-04:00","date":"2026-08-17","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":261.1,"phases_s":{"reconcile":140.41},"signals":0,"placed":0,"equity":null,"open_positions":14,"pending_orders":0,"open_lots":45,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"7335","github_run_id":"32082431205","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:56:58  INFO      Mode: exits
14:56:59  INFO        Daily log -> logs/daily/2026-08-20.md
14:56:59  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (3 ledger rows)
14:56:59  INFO        place_all_stops: checking 4 positions...
14:56:59  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
14:56:59  INFO        STOP skipped MNST: fractional (0.6350 shares) — software exit will handle it
14:56:59  INFO        [positions] 2/2 (2 valid)
14:57:00  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:56 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $418.40|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.1%  $+0.02                                           HOLD|
|  AON  P&L +0.6%  $+0.45                                            HOLD|
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
|  CL260821C00090000       $0.52    $0.30    -42.3%   $-22.00   $30.00   |
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
|                                                                        |
|  Options open P&L                                               $-29.00|
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
=== options_live_micro LIVE 2026-08-20T10:57:00.795760-04:00 share=50% ===
2026-08-20 10:57:00,795 INFO === options_live_micro LIVE 2026-08-20T10:57:00.795760-04:00 share=50% ===
Live account equity $418.40 cash $285.87 #225458845 options_level=3
2026-08-20 10:57:01,065 INFO Live account equity $418.40 cash $285.87 #225458845 options_level=3
Live micro fill confirmed S218 CL260821C00090000
2026-08-20 10:57:01,162 INFO Live micro fill confirmed S218 CL260821C00090000
Live micro hold S218 CL260821C00090000 -42.3% (tp +50% / sl -50%)
2026-08-20 10:57:01,257 INFO Live micro hold S218 CL260821C00090000 -42.3% (tp +50% / sl -50%)
Live micro sleeve $209 (50% of $418) deployed $32 open_strategies=3/4 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy)
2026-08-20 10:57:01,485 INFO Live micro sleeve $209 (50% of $418) deployed $32 open_strategies=3/4 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-20 10:57:01,485 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 11
2026-08-20 10:57:02,740 INFO Live micro signals: 11
  skip S404 COST: strategy already open (paper bucket rule)
2026-08-20 10:57:02,740 INFO   skip S404 COST: strategy already open (paper bucket rule)
  skip S404 CRWD: strategy already open (paper bucket rule)
2026-08-20 10:57:02,740 INFO   skip S404 CRWD: strategy already open (paper bucket rule)
  skip S404 HD: strategy already open (paper bucket rule)
2026-08-20 10:57:02,740 INFO   skip S404 HD: strategy already open (paper bucket rule)
  skip S404 WMT: strategy already open (paper bucket rule)
2026-08-20 10:57:02,740 INFO   skip S404 WMT: strategy already open (paper bucket rule)
  skip S406 COST: strategy already open (paper bucket rule)
2026-08-20 10:57:02,740 INFO   skip S406 COST: strategy already open (paper bucket rule)
  skip S406 CPB: strategy already open (paper bucket rule)
2026-08-20 10:57:02,740 INFO   skip S406 CPB: strategy already open (paper bucket rule)
  skip S218 CL: strategy already open (paper bucket rule)
2026-08-20 10:57:02,740 INFO   skip S218 CL: strategy already open (paper bucket rule)
  skip S218 COST: strategy already open (paper bucket rule)
2026-08-20 10:57:02,740 INFO   skip S218 COST: strategy already open (paper bucket rule)
  try S210 55%win/+47%med ABBV
2026-08-20 10:57:02,741 INFO   try S210 55%win/+47%med ABBV
  skip S210 ABBV: no contract under $75
2026-08-20 10:57:03,407 INFO   skip S210 ABBV: no contract under $75
  try S210 55%win/+47%med SJM
2026-08-20 10:57:03,408 INFO   try S210 55%win/+47%med SJM
  skip S210 SJM: no contract under $75
2026-08-20 10:57:03,693 INFO   skip S210 SJM: no contract under $75
  try S210 55%win/+47%med XEL
2026-08-20 10:57:03,693 INFO   try S210 55%win/+47%med XEL
  skip S210 XEL: no contract under $75
2026-08-20 10:57:03,991 INFO   skip S210 XEL: no contract under $75
Live micro done. open_options=2 lots=1
2026-08-20 10:57:04,233 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=35 paper_keys=yes dry_run=False
  alpaca positions=12
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-20T10:57:05.897424-04:00 ===

[Run context]
2026-08-20 10:57:06,141 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-20 10:57:14,216 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-20 10:57:30,291 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
2026-08-20 10:57:54,361 WARNING paper get_account failed attempt 4/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 32s
2026-08-20 10:58:26,434 WARNING paper get_account failed attempt 5/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 40s
2026-08-20 10:59:06,508 ERROR paper get_account failed after 6 attempts: {"code":50010000,"message":"internal server error occurred"}
WARN: get_account failed ({"code":50010000,"message":"internal server error occurred"}) but positions OK (n=12). Keys are fine; Alpaca account endpoint is flaky. Continuing manage/exits; skipping new entries until equity is readable.
2026-08-20 10:59:06,653 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-20 10:59:14,740 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-20 10:59:30,832 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
2026-08-20 10:59:54,908 WARNING paper get_account failed attempt 4/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 32s
2026-08-20 11:00:26,983 WARNING paper get_account failed attempt 5/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 40s
```

---

## Run 20260820T150151Z

- UTC timestamp: `20260820T150151Z`
- GitHub run: [#7624](https://github.com/28twagg-ops/TradingBot/actions/runs/32383505175)
- Run id: `32383505175`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`3s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T150151Z_live_bot.log`, `logs/action_runs/20260820T150151Z_live_options.log`, `logs/action_runs/20260820T150151Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 821 | 41.8 | -47.5 | +15.4 | $+8,207 |
| TAINTED | 1761 | 33.0 | -39.3 | +12.2 | $-9,205 |
| KEEP-only | 294 | 63.3 | +37.5 | +42.9 | $+5,699 |
| KEEP-only recent | 106 | 58.5 | +50.0 | +54.8 | $+1,673 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406
- KILL strategies (16): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-17T19:56:23.633587-04:00","date":"2026-08-17","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":261.1,"phases_s":{"reconcile":140.41},"signals":0,"placed":0,"equity":null,"open_positions":14,"pending_orders":0,"open_lots":45,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"7335","github_run_id":"32082431205","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:01:51  INFO      Mode: exits
15:01:52  INFO        Daily log -> logs/daily/2026-08-20.md
15:01:52  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (3 ledger rows)
15:01:53  INFO        place_all_stops: checking 4 positions...
15:01:53  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
15:01:53  INFO        STOP skipped MNST: fractional (0.6350 shares) — software exit will handle it
15:01:53  INFO        [positions] 2/2 (2 valid)
15:01:53  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $418.48|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.3%  $+0.08                                           HOLD|
|  AON  P&L +0.7%  $+0.46                                            HOLD|
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
|  CL260821C00090000       $0.52    $0.30    -42.3%   $-22.00   $30.00   |
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
|                                                                        |
|  Options open P&L                                               $-29.00|
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
=== options_live_micro LIVE 2026-08-20T11:01:54.347322-04:00 share=50% ===
2026-08-20 11:01:54,347 INFO === options_live_micro LIVE 2026-08-20T11:01:54.347322-04:00 share=50% ===
Live account equity $418.43 cash $285.87 #225458845 options_level=3
2026-08-20 11:01:54,469 INFO Live account equity $418.43 cash $285.87 #225458845 options_level=3
Live micro fill confirmed S218 CL260821C00090000
2026-08-20 11:01:54,501 INFO Live micro fill confirmed S218 CL260821C00090000
Live micro hold S218 CL260821C00090000 -42.3% (tp +50% / sl -50%)
2026-08-20 11:01:54,533 INFO Live micro hold S218 CL260821C00090000 -42.3% (tp +50% / sl -50%)
Live micro sleeve $209 (50% of $418) deployed $32 open_strategies=3/4 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy)
2026-08-20 11:01:54,673 INFO Live micro sleeve $209 (50% of $418) deployed $32 open_strategies=3/4 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-20 11:01:54,674 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 11
2026-08-20 11:01:55,723 INFO Live micro signals: 11
  skip S404 COST: strategy already open (paper bucket rule)
2026-08-20 11:01:55,723 INFO   skip S404 COST: strategy already open (paper bucket rule)
  skip S404 CRWD: strategy already open (paper bucket rule)
2026-08-20 11:01:55,723 INFO   skip S404 CRWD: strategy already open (paper bucket rule)
  skip S404 HD: strategy already open (paper bucket rule)
2026-08-20 11:01:55,723 INFO   skip S404 HD: strategy already open (paper bucket rule)
  skip S404 WMT: strategy already open (paper bucket rule)
2026-08-20 11:01:55,723 INFO   skip S404 WMT: strategy already open (paper bucket rule)
  skip S406 COST: strategy already open (paper bucket rule)
2026-08-20 11:01:55,724 INFO   skip S406 COST: strategy already open (paper bucket rule)
  skip S406 CPB: strategy already open (paper bucket rule)
2026-08-20 11:01:55,724 INFO   skip S406 CPB: strategy already open (paper bucket rule)
  skip S218 CL: strategy already open (paper bucket rule)
2026-08-20 11:01:55,724 INFO   skip S218 CL: strategy already open (paper bucket rule)
  skip S218 COST: strategy already open (paper bucket rule)
2026-08-20 11:01:55,724 INFO   skip S218 COST: strategy already open (paper bucket rule)
  try S210 55%win/+47%med ABBV
2026-08-20 11:01:55,724 INFO   try S210 55%win/+47%med ABBV
  skip S210 ABBV: no contract under $75
2026-08-20 11:01:56,079 INFO   skip S210 ABBV: no contract under $75
  try S210 55%win/+47%med SJM
2026-08-20 11:01:56,079 INFO   try S210 55%win/+47%med SJM
  skip S210 SJM: no contract under $75
2026-08-20 11:01:56,242 INFO   skip S210 SJM: no contract under $75
  try S210 55%win/+47%med XEL
2026-08-20 11:01:56,242 INFO   try S210 55%win/+47%med XEL
  skip S210 XEL: no contract under $75
2026-08-20 11:01:56,647 INFO   skip S210 XEL: no contract under $75
Live micro done. open_options=2 lots=1
2026-08-20 11:01:56,778 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=35 paper_keys=yes dry_run=False
  alpaca positions=12
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-20T11:01:58.121134-04:00 ===

[Run context]
2026-08-20 11:01:58,277 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-20 11:02:06,356 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-20 11:02:22,431 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
2026-08-20 11:02:46,501 WARNING paper get_account failed attempt 4/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 32s
2026-08-20 11:03:18,570 WARNING paper get_account failed attempt 5/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 40s
2026-08-20 11:03:58,635 ERROR paper get_account failed after 6 attempts: {"code":50010000,"message":"internal server error occurred"}
WARN: get_account failed ({"code":50010000,"message":"internal server error occurred"}) but positions OK (n=12). Keys are fine; Alpaca account endpoint is flaky. Continuing manage/exits; skipping new entries until equity is readable.
2026-08-20 11:03:58,769 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-20 11:04:06,820 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-20 11:04:22,875 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
2026-08-20 11:04:46,932 WARNING paper get_account failed attempt 4/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 32s
2026-08-20 11:05:19,001 WARNING paper get_account failed attempt 5/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 40s
2026-08-20 11:05:59,059 ERROR paper get_account failed after 6 attempts: {"code":50010000,"message":"internal server error occurred"}
2026-08-20 11:05:59,130 WARNING lab get_account failed attempt 1/3: {"code":50010000,"message":"internal server error occurred"}
```

---

## Run 20260820T150711Z

- UTC timestamp: `20260820T150711Z`
- GitHub run: [#7625](https://github.com/28twagg-ops/TradingBot/actions/runs/32384003342)
- Run id: `32384003342`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`5s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T150711Z_live_bot.log`, `logs/action_runs/20260820T150711Z_live_options.log`, `logs/action_runs/20260820T150711Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 821 | 41.8 | -47.5 | +15.4 | $+8,207 |
| TAINTED | 1761 | 33.0 | -39.3 | +12.2 | $-9,205 |
| KEEP-only | 294 | 63.3 | +37.5 | +42.9 | $+5,699 |
| KEEP-only recent | 106 | 58.5 | +50.0 | +54.8 | $+1,673 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406
- KILL strategies (16): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-17T19:56:23.633587-04:00","date":"2026-08-17","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":261.1,"phases_s":{"reconcile":140.41},"signals":0,"placed":0,"equity":null,"open_positions":14,"pending_orders":0,"open_lots":45,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"7335","github_run_id":"32082431205","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:07:13  INFO      Mode: exits
15:07:14  INFO        Daily log -> logs/daily/2026-08-20.md
15:07:14  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (3 ledger rows)
15:07:14  INFO        place_all_stops: checking 4 positions...
15:07:14  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
15:07:14  INFO        STOP skipped MNST: fractional (0.6350 shares) — software exit will handle it
15:07:15  INFO        [positions] 2/2 (2 valid)
15:07:15  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:07 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $423.68|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.3%  $+0.09                                           HOLD|
|  AON  P&L +0.9%  $+0.65                                            HOLD|
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
|  CL260821C00090000       $0.52    $0.35    -32.7%   $-17.00   $35.00   |
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
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
=== options_live_micro LIVE 2026-08-20T11:07:16.499351-04:00 share=50% ===
2026-08-20 11:07:16,499 INFO === options_live_micro LIVE 2026-08-20T11:07:16.499351-04:00 share=50% ===
Live account equity $423.68 cash $285.87 #225458845 options_level=3
2026-08-20 11:07:16,745 INFO Live account equity $423.68 cash $285.87 #225458845 options_level=3
Live micro hold S218 CL260821C00090000 -32.7% (tp +50% / sl -50%)
2026-08-20 11:07:16,914 INFO Live micro hold S218 CL260821C00090000 -32.7% (tp +50% / sl -50%)
Live micro sleeve $212 (50% of $424) deployed $37 open_strategies=3/4 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy)
2026-08-20 11:07:17,142 INFO Live micro sleeve $212 (50% of $424) deployed $37 open_strategies=3/4 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-20 11:07:17,142 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 11
2026-08-20 11:07:19,153 INFO Live micro signals: 11
  skip S404 COST: strategy already open (paper bucket rule)
2026-08-20 11:07:19,153 INFO   skip S404 COST: strategy already open (paper bucket rule)
  skip S404 CRWD: strategy already open (paper bucket rule)
2026-08-20 11:07:19,153 INFO   skip S404 CRWD: strategy already open (paper bucket rule)
  skip S404 HD: strategy already open (paper bucket rule)
2026-08-20 11:07:19,154 INFO   skip S404 HD: strategy already open (paper bucket rule)
  skip S404 WMT: strategy already open (paper bucket rule)
2026-08-20 11:07:19,154 INFO   skip S404 WMT: strategy already open (paper bucket rule)
  skip S406 COST: strategy already open (paper bucket rule)
2026-08-20 11:07:19,154 INFO   skip S406 COST: strategy already open (paper bucket rule)
  skip S406 CPB: strategy already open (paper bucket rule)
2026-08-20 11:07:19,154 INFO   skip S406 CPB: strategy already open (paper bucket rule)
  skip S218 CL: strategy already open (paper bucket rule)
2026-08-20 11:07:19,154 INFO   skip S218 CL: strategy already open (paper bucket rule)
  skip S218 COST: strategy already open (paper bucket rule)
2026-08-20 11:07:19,154 INFO   skip S218 COST: strategy already open (paper bucket rule)
  try S210 55%win/+47%med ABBV
2026-08-20 11:07:19,154 INFO   try S210 55%win/+47%med ABBV
  skip S210 ABBV: no contract under $75
2026-08-20 11:07:19,780 INFO   skip S210 ABBV: no contract under $75
  try S210 55%win/+47%med SJM
2026-08-20 11:07:19,781 INFO   try S210 55%win/+47%med SJM
  skip S210 SJM: no contract under $75
2026-08-20 11:07:20,029 INFO   skip S210 SJM: no contract under $75
  try S210 55%win/+47%med XEL
2026-08-20 11:07:20,029 INFO   try S210 55%win/+47%med XEL
  skip S210 XEL: no contract under $75
2026-08-20 11:07:20,304 INFO   skip S210 XEL: no contract under $75
Live micro done. open_options=2 lots=1
2026-08-20 11:07:20,538 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=35 paper_keys=yes dry_run=False
  alpaca positions=12
options_reconcile: done
Layout: grid:100:baseline (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> grid:100:baseline)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-08-20T11:07:22.420053-04:00 ===

[Run context]
2026-08-20 11:07:22,656 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-20 11:07:30,732 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-20 11:07:46,805 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
2026-08-20 11:08:10,880 WARNING paper get_account failed attempt 4/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 32s
2026-08-20 11:08:42,954 WARNING paper get_account failed attempt 5/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 40s
2026-08-20 11:09:23,043 ERROR paper get_account failed after 6 attempts: {"code":50010000,"message":"internal server error occurred"}
WARN: get_account failed ({"code":50010000,"message":"internal server error occurred"}) but positions OK (n=12). Keys are fine; Alpaca account endpoint is flaky. Continuing manage/exits; skipping new entries until equity is readable.
2026-08-20 11:09:23,187 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-20 11:09:31,269 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-20 11:09:47,343 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
2026-08-20 11:10:11,421 WARNING paper get_account failed attempt 4/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 32s
2026-08-20 11:10:43,501 WARNING paper get_account failed attempt 5/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 40s
```

---

## Run 20260820T151152Z

- UTC timestamp: `20260820T151152Z`
- GitHub run: [#7626](https://github.com/28twagg-ops/TradingBot/actions/runs/32384493467)
- Run id: `32384493467`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`3s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T151152Z_live_bot.log`, `logs/action_runs/20260820T151152Z_live_options.log`, `logs/action_runs/20260820T151152Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 821 | 41.8 | -47.5 | +15.4 | $+8,207 |
| TAINTED | 1761 | 33.0 | -39.3 | +12.2 | $-9,205 |
| KEEP-only | 294 | 63.3 | +37.5 | +42.9 | $+5,699 |
| KEEP-only recent | 106 | 58.5 | +50.0 | +54.8 | $+1,673 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406
- KILL strategies (16): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-17T19:56:23.633587-04:00","date":"2026-08-17","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":261.1,"phases_s":{"reconcile":140.41},"signals":0,"placed":0,"equity":null,"open_positions":14,"pending_orders":0,"open_lots":45,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"7335","github_run_id":"32082431205","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:11:53  INFO      Mode: exits
15:11:54  INFO        Daily log -> logs/daily/2026-08-20.md
15:11:54  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (3 ledger rows)
15:11:54  INFO        place_all_stops: checking 4 positions...
15:11:54  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
15:11:54  INFO        STOP skipped MNST: fractional (0.6350 shares) — software exit will handle it
15:11:54  INFO        [positions] 2/2 (2 valid)
15:11:54  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $423.77|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.3%  $+0.10                                           HOLD|
|  AON  P&L +1.1%  $+0.73                                            HOLD|
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
|  CL260821C00090000       $0.52    $0.35    -32.7%   $-17.00   $35.00   |
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
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
=== options_live_micro LIVE 2026-08-20T11:11:55.323254-04:00 share=50% ===
2026-08-20 11:11:55,323 INFO === options_live_micro LIVE 2026-08-20T11:11:55.323254-04:00 share=50% ===
Live account equity $423.77 cash $285.87 #225458845 options_level=3
2026-08-20 11:11:55,369 INFO Live account equity $423.77 cash $285.87 #225458845 options_level=3
Live micro hold S218 CL260821C00090000 -32.7% (tp +50% / sl -50%)
2026-08-20 11:11:55,396 INFO Live micro hold S218 CL260821C00090000 -32.7% (tp +50% / sl -50%)
Live micro sleeve $212 (50% of $424) deployed $37 open_strategies=3/4 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy)
2026-08-20 11:11:55,423 INFO Live micro sleeve $212 (50% of $424) deployed $37 open_strategies=3/4 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-20 11:11:55,423 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 11
2026-08-20 11:11:57,061 INFO Live micro signals: 11
  skip S404 COST: strategy already open (paper bucket rule)
2026-08-20 11:11:57,062 INFO   skip S404 COST: strategy already open (paper bucket rule)
  skip S404 CRWD: strategy already open (paper bucket rule)
2026-08-20 11:11:57,062 INFO   skip S404 CRWD: strategy already open (paper bucket rule)
  skip S404 HD: strategy already open (paper bucket rule)
2026-08-20 11:11:57,062 INFO   skip S404 HD: strategy already open (paper bucket rule)
  skip S404 WMT: strategy already open (paper bucket rule)
2026-08-20 11:11:57,062 INFO   skip S404 WMT: strategy already open (paper bucket rule)
  skip S406 COST: strategy already open (paper bucket rule)
2026-08-20 11:11:57,062 INFO   skip S406 COST: strategy already open (paper bucket rule)
  skip S406 CPB: strategy already open (paper bucket rule)
2026-08-20 11:11:57,062 INFO   skip S406 CPB: strategy already open (paper bucket rule)
  skip S218 CL: strategy already open (paper bucket rule)
2026-08-20 11:11:57,062 INFO   skip S218 CL: strategy already open (paper bucket rule)
  skip S218 COST: strategy already open (paper bucket rule)
2026-08-20 11:11:57,062 INFO   skip S218 COST: strategy already open (paper bucket rule)
  try S210 55%win/+47%med ABBV
2026-08-20 11:11:57,062 INFO   try S210 55%win/+47%med ABBV
  skip S210 ABBV: no contract under $75
2026-08-20 11:11:57,173 INFO   skip S210 ABBV: no contract under $75
  try S210 55%win/+47%med SJM
2026-08-20 11:11:57,173 INFO   try S210 55%win/+47%med SJM
  skip S210 SJM: no contract under $75
2026-08-20 11:11:57,206 INFO   skip S210 SJM: no contract under $75
  try S210 55%win/+47%med XEL
2026-08-20 11:11:57,206 INFO   try S210 55%win/+47%med XEL
  skip S210 XEL: no contract under $75
2026-08-20 11:11:57,237 INFO   skip S210 XEL: no contract under $75
Live micro done. open_options=2 lots=1
2026-08-20 11:11:57,271 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=35 paper_keys=yes dry_run=False
  alpaca positions=12
options_reconcile: done
Layout: grid:100:baseline (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> grid:100:baseline)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-08-20T11:11:58.684695-04:00 ===

[Run context]
2026-08-20 11:11:58,739 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-20 11:12:06,753 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-20 11:12:22,764 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
2026-08-20 11:12:46,806 WARNING paper get_account failed attempt 4/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 32s
2026-08-20 11:13:18,846 WARNING paper get_account failed attempt 5/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 40s
2026-08-20 11:13:58,861 ERROR paper get_account failed after 6 attempts: {"code":50010000,"message":"internal server error occurred"}
WARN: get_account failed ({"code":50010000,"message":"internal server error occurred"}) but positions OK (n=12). Keys are fine; Alpaca account endpoint is flaky. Continuing manage/exits; skipping new entries until equity is readable.
2026-08-20 11:13:58,933 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-20 11:14:06,952 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-20 11:14:22,979 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
2026-08-20 11:14:46,997 WARNING paper get_account failed attempt 4/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 32s
2026-08-20 11:15:19,010 WARNING paper get_account failed attempt 5/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 40s
```

---

## Run 20260820T151629Z

- UTC timestamp: `20260820T151629Z`
- GitHub run: [#7627](https://github.com/28twagg-ops/TradingBot/actions/runs/32384992677)
- Run id: `32384992677`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`5s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T151629Z_live_bot.log`, `logs/action_runs/20260820T151629Z_live_options.log`, `logs/action_runs/20260820T151629Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 821 | 41.8 | -47.5 | +15.4 | $+8,207 |
| TAINTED | 1761 | 33.0 | -39.3 | +12.2 | $-9,205 |
| KEEP-only | 294 | 63.3 | +37.5 | +42.9 | $+5,699 |
| KEEP-only recent | 106 | 58.5 | +50.0 | +54.8 | $+1,673 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406
- KILL strategies (16): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-17T19:56:23.633587-04:00","date":"2026-08-17","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":261.1,"phases_s":{"reconcile":140.41},"signals":0,"placed":0,"equity":null,"open_positions":14,"pending_orders":0,"open_lots":45,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"7335","github_run_id":"32082431205","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:16:30  INFO      Mode: exits
15:16:31  INFO        Daily log -> logs/daily/2026-08-20.md
15:16:31  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (3 ledger rows)
15:16:31  INFO        place_all_stops: checking 4 positions...
15:16:31  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
15:16:31  INFO        STOP skipped MNST: fractional (0.6350 shares) — software exit will handle it
15:16:32  INFO        [positions] 2/2 (2 valid)
15:16:32  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $428.63|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.2%  $+0.05                                           HOLD|
|  AON  P&L +0.9%  $+0.64                                            HOLD|
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
|  CL260821C00090000       $0.52    $0.40    -23.1%   $-12.00   $40.00   |
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
|                                                                        |
|  Options open P&L                                               $-19.00|
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
=== options_live_micro LIVE 2026-08-20T11:16:33.625411-04:00 share=50% ===
2026-08-20 11:16:33,625 INFO === options_live_micro LIVE 2026-08-20T11:16:33.625411-04:00 share=50% ===
Live account equity $428.63 cash $285.87 #225458845 options_level=3
2026-08-20 11:16:33,965 INFO Live account equity $428.63 cash $285.87 #225458845 options_level=3
Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
2026-08-20 11:16:34,101 INFO Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
Live micro sleeve $214 (50% of $429) deployed $42 open_strategies=3/4 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy)
2026-08-20 11:16:34,305 INFO Live micro sleeve $214 (50% of $429) deployed $42 open_strategies=3/4 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-20 11:16:34,305 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 11
2026-08-20 11:16:36,220 INFO Live micro signals: 11
  skip S404 COST: strategy already open (paper bucket rule)
2026-08-20 11:16:36,221 INFO   skip S404 COST: strategy already open (paper bucket rule)
  skip S404 CRWD: strategy already open (paper bucket rule)
2026-08-20 11:16:36,221 INFO   skip S404 CRWD: strategy already open (paper bucket rule)
  skip S404 HD: strategy already open (paper bucket rule)
2026-08-20 11:16:36,221 INFO   skip S404 HD: strategy already open (paper bucket rule)
  skip S404 WMT: strategy already open (paper bucket rule)
2026-08-20 11:16:36,221 INFO   skip S404 WMT: strategy already open (paper bucket rule)
  skip S406 COST: strategy already open (paper bucket rule)
2026-08-20 11:16:36,221 INFO   skip S406 COST: strategy already open (paper bucket rule)
  skip S406 CPB: strategy already open (paper bucket rule)
2026-08-20 11:16:36,221 INFO   skip S406 CPB: strategy already open (paper bucket rule)
  skip S218 CL: strategy already open (paper bucket rule)
2026-08-20 11:16:36,221 INFO   skip S218 CL: strategy already open (paper bucket rule)
  skip S218 COST: strategy already open (paper bucket rule)
2026-08-20 11:16:36,222 INFO   skip S218 COST: strategy already open (paper bucket rule)
  try S210 55%win/+47%med ABBV
2026-08-20 11:16:36,222 INFO   try S210 55%win/+47%med ABBV
  skip S210 ABBV: no contract under $75
2026-08-20 11:16:36,746 INFO   skip S210 ABBV: no contract under $75
  try S210 55%win/+47%med SJM
2026-08-20 11:16:36,747 INFO   try S210 55%win/+47%med SJM
  skip S210 SJM: no contract under $75
2026-08-20 11:16:37,035 INFO   skip S210 SJM: no contract under $75
  try S210 55%win/+47%med XEL
2026-08-20 11:16:37,035 INFO   try S210 55%win/+47%med XEL
  skip S210 XEL: no contract under $75
2026-08-20 11:16:37,334 INFO   skip S210 XEL: no contract under $75
Live micro done. open_options=2 lots=1
2026-08-20 11:16:37,555 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=35 paper_keys=yes dry_run=False
  alpaca positions=12
options_reconcile: done
Layout: grid:100:baseline (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> grid:100:baseline)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-08-20T11:16:39.199799-04:00 ===

[Run context]
2026-08-20 11:16:39,408 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-20 11:16:47,486 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-20 11:17:03,547 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
2026-08-20 11:17:27,646 WARNING paper get_account failed attempt 4/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 32s
2026-08-20 11:17:59,707 WARNING paper get_account failed attempt 5/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 40s
2026-08-20 11:18:39,778 ERROR paper get_account failed after 6 attempts: {"code":50010000,"message":"internal server error occurred"}
WARN: get_account failed ({"code":50010000,"message":"internal server error occurred"}) but positions OK (n=12). Keys are fine; Alpaca account endpoint is flaky. Continuing manage/exits; skipping new entries until equity is readable.
2026-08-20 11:18:39,906 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-20 11:18:47,969 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-20 11:19:04,031 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
2026-08-20 11:19:28,095 WARNING paper get_account failed attempt 4/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 32s
2026-08-20 11:20:00,238 WARNING paper get_account failed attempt 5/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 40s
2026-08-20 11:20:40,302 ERROR paper get_account failed after 6 attempts: {"code":50010000,"message":"internal server error occurred"}
2026-08-20 11:20:40,369 WARNING lab get_account failed attempt 1/3: {"code":50010000,"message":"internal server error occurred"}
2026-08-20 11:20:50,464 WARNING lab get_account failed attempt 2/3: {"code":50010000,"message":"internal server error occurred"}
```

---

## Run 20260820T152202Z

- UTC timestamp: `20260820T152202Z`
- GitHub run: [#7628](https://github.com/28twagg-ops/TradingBot/actions/runs/32385495743)
- Run id: `32385495743`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`4s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T152202Z_live_bot.log`, `logs/action_runs/20260820T152202Z_live_options.log`, `logs/action_runs/20260820T152202Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 821 | 41.8 | -47.5 | +15.4 | $+8,207 |
| TAINTED | 1761 | 33.0 | -39.3 | +12.2 | $-9,205 |
| KEEP-only | 294 | 63.3 | +37.5 | +42.9 | $+5,699 |
| KEEP-only recent | 106 | 58.5 | +50.0 | +54.8 | $+1,673 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406
- KILL strategies (16): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-17T19:56:23.633587-04:00","date":"2026-08-17","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":261.1,"phases_s":{"reconcile":140.41},"signals":0,"placed":0,"equity":null,"open_positions":14,"pending_orders":0,"open_lots":45,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"7335","github_run_id":"32082431205","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:22:04  INFO      Mode: exits
15:22:05  INFO        Daily log -> logs/daily/2026-08-20.md
15:22:05  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (3 ledger rows)
15:22:05  INFO        place_all_stops: checking 4 positions...
15:22:05  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
15:22:05  INFO        STOP skipped MNST: fractional (0.6350 shares) — software exit will handle it
15:22:05  INFO        [positions] 2/2 (2 valid)
15:22:06  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:22 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $428.61|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.0%  $+0.01                                           HOLD|
|  AON  P&L +0.9%  $+0.66                                            HOLD|
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
|  CL260821C00090000       $0.52    $0.40    -23.1%   $-12.00   $40.00   |
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
|                                                                        |
|  Options open P&L                                               $-19.00|
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
=== options_live_micro LIVE 2026-08-20T11:22:06.958855-04:00 share=50% ===
2026-08-20 11:22:06,958 INFO === options_live_micro LIVE 2026-08-20T11:22:06.958855-04:00 share=50% ===
Live account equity $428.61 cash $285.87 #225458845 options_level=3
2026-08-20 11:22:07,094 INFO Live account equity $428.61 cash $285.87 #225458845 options_level=3
Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
2026-08-20 11:22:07,163 INFO Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
Live micro sleeve $214 (50% of $429) deployed $42 open_strategies=3/4 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy)
2026-08-20 11:22:07,275 INFO Live micro sleeve $214 (50% of $429) deployed $42 open_strategies=3/4 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-20 11:22:07,276 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 11
2026-08-20 11:22:08,939 INFO Live micro signals: 11
  skip S404 COST: strategy already open (paper bucket rule)
2026-08-20 11:22:08,939 INFO   skip S404 COST: strategy already open (paper bucket rule)
  skip S404 CRWD: strategy already open (paper bucket rule)
2026-08-20 11:22:08,939 INFO   skip S404 CRWD: strategy already open (paper bucket rule)
  skip S404 HD: strategy already open (paper bucket rule)
2026-08-20 11:22:08,940 INFO   skip S404 HD: strategy already open (paper bucket rule)
  skip S404 WMT: strategy already open (paper bucket rule)
2026-08-20 11:22:08,940 INFO   skip S404 WMT: strategy already open (paper bucket rule)
  skip S406 COST: strategy already open (paper bucket rule)
2026-08-20 11:22:08,940 INFO   skip S406 COST: strategy already open (paper bucket rule)
  skip S406 CPB: strategy already open (paper bucket rule)
2026-08-20 11:22:08,940 INFO   skip S406 CPB: strategy already open (paper bucket rule)
  skip S218 CL: strategy already open (paper bucket rule)
2026-08-20 11:22:08,940 INFO   skip S218 CL: strategy already open (paper bucket rule)
  skip S218 COST: strategy already open (paper bucket rule)
2026-08-20 11:22:08,940 INFO   skip S218 COST: strategy already open (paper bucket rule)
  try S210 55%win/+47%med ABBV
2026-08-20 11:22:08,940 INFO   try S210 55%win/+47%med ABBV
  skip S210 ABBV: no contract under $75
2026-08-20 11:22:09,492 INFO   skip S210 ABBV: no contract under $75
  try S210 55%win/+47%med SJM
2026-08-20 11:22:09,492 INFO   try S210 55%win/+47%med SJM
  skip S210 SJM: no contract under $75
2026-08-20 11:22:09,672 INFO   skip S210 SJM: no contract under $75
  try S210 55%win/+47%med XEL
2026-08-20 11:22:09,672 INFO   try S210 55%win/+47%med XEL
  skip S210 XEL: no contract under $75
2026-08-20 11:22:09,876 INFO   skip S210 XEL: no contract under $75
Live micro done. open_options=2 lots=1
2026-08-20 11:22:09,989 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=35 paper_keys=yes dry_run=False
  alpaca positions=12
options_reconcile: done
Layout: grid:100:baseline (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> grid:100:baseline)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-08-20T11:22:11.547298-04:00 ===

[Run context]
2026-08-20 11:22:11,832 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-20 11:22:19,918 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-20 11:22:35,994 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
2026-08-20 11:23:00,042 WARNING paper get_account failed attempt 4/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 32s
2026-08-20 11:23:32,090 WARNING paper get_account failed attempt 5/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 40s
2026-08-20 11:24:12,134 ERROR paper get_account failed after 6 attempts: {"code":50010000,"message":"internal server error occurred"}
WARN: get_account failed ({"code":50010000,"message":"internal server error occurred"}) but positions OK (n=12). Keys are fine; Alpaca account endpoint is flaky. Continuing manage/exits; skipping new entries until equity is readable.
2026-08-20 11:24:12,218 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-20 11:24:20,266 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-20 11:24:36,310 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
2026-08-20 11:25:00,355 WARNING paper get_account failed attempt 4/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 32s
2026-08-20 11:25:32,533 WARNING paper get_account failed attempt 5/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 40s
```

---

## Run 20260820T152645Z

- UTC timestamp: `20260820T152645Z`
- GitHub run: [#7629](https://github.com/28twagg-ops/TradingBot/actions/runs/32385997094)
- Run id: `32385997094`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`4s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T152645Z_live_bot.log`, `logs/action_runs/20260820T152645Z_live_options.log`, `logs/action_runs/20260820T152645Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 821 | 41.8 | -47.5 | +15.4 | $+8,207 |
| TAINTED | 1761 | 33.0 | -39.3 | +12.2 | $-9,205 |
| KEEP-only | 294 | 63.3 | +37.5 | +42.9 | $+5,699 |
| KEEP-only recent | 106 | 58.5 | +50.0 | +54.8 | $+1,673 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406
- KILL strategies (16): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-17T19:56:23.633587-04:00","date":"2026-08-17","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":261.1,"phases_s":{"reconcile":140.41},"signals":0,"placed":0,"equity":null,"open_positions":14,"pending_orders":0,"open_lots":45,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"7335","github_run_id":"32082431205","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:26:46  INFO      Mode: exits
15:26:46  INFO        Daily log -> logs/daily/2026-08-20.md
15:26:46  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (3 ledger rows)
15:26:46  INFO        place_all_stops: checking 4 positions...
15:26:46  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
15:26:46  INFO        STOP skipped MNST: fractional (0.6350 shares) — software exit will handle it
15:26:47  INFO        [positions] 2/2 (2 valid)
15:26:47  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $428.69|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.1%  $+0.03                                           HOLD|
|  AON  P&L +1.0%  $+0.73                                            HOLD|
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
|  CL260821C00090000       $0.52    $0.40    -23.1%   $-12.00   $40.00   |
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
|                                                                        |
|  Options open P&L                                               $-19.00|
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
=== options_live_micro LIVE 2026-08-20T11:26:48.196882-04:00 share=50% ===
2026-08-20 11:26:48,196 INFO === options_live_micro LIVE 2026-08-20T11:26:48.196882-04:00 share=50% ===
Live account equity $428.69 cash $285.87 #225458845 options_level=3
2026-08-20 11:26:48,402 INFO Live account equity $428.69 cash $285.87 #225458845 options_level=3
Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
2026-08-20 11:26:48,498 INFO Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
Live micro sleeve $214 (50% of $429) deployed $42 open_strategies=3/4 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy)
2026-08-20 11:26:48,603 INFO Live micro sleeve $214 (50% of $429) deployed $42 open_strategies=3/4 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-20 11:26:48,603 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 11
2026-08-20 11:26:50,235 INFO Live micro signals: 11
  skip S404 COST: strategy already open (paper bucket rule)
2026-08-20 11:26:50,235 INFO   skip S404 COST: strategy already open (paper bucket rule)
  skip S404 CRWD: strategy already open (paper bucket rule)
2026-08-20 11:26:50,235 INFO   skip S404 CRWD: strategy already open (paper bucket rule)
  skip S404 HD: strategy already open (paper bucket rule)
2026-08-20 11:26:50,235 INFO   skip S404 HD: strategy already open (paper bucket rule)
  skip S404 WMT: strategy already open (paper bucket rule)
2026-08-20 11:26:50,235 INFO   skip S404 WMT: strategy already open (paper bucket rule)
  skip S406 COST: strategy already open (paper bucket rule)
2026-08-20 11:26:50,236 INFO   skip S406 COST: strategy already open (paper bucket rule)
  skip S406 CPB: strategy already open (paper bucket rule)
2026-08-20 11:26:50,236 INFO   skip S406 CPB: strategy already open (paper bucket rule)
  skip S218 CL: strategy already open (paper bucket rule)
2026-08-20 11:26:50,236 INFO   skip S218 CL: strategy already open (paper bucket rule)
  skip S218 COST: strategy already open (paper bucket rule)
2026-08-20 11:26:50,236 INFO   skip S218 COST: strategy already open (paper bucket rule)
  try S210 55%win/+47%med ABBV
2026-08-20 11:26:50,236 INFO   try S210 55%win/+47%med ABBV
  skip S210 ABBV: no contract under $75
2026-08-20 11:26:50,586 INFO   skip S210 ABBV: no contract under $75
  try S210 55%win/+47%med SJM
2026-08-20 11:26:50,586 INFO   try S210 55%win/+47%med SJM
  skip S210 SJM: no contract under $75
2026-08-20 11:26:50,730 INFO   skip S210 SJM: no contract under $75
  try S210 55%win/+47%med XEL
2026-08-20 11:26:50,731 INFO   try S210 55%win/+47%med XEL
  skip S210 XEL: no contract under $75
2026-08-20 11:26:50,874 INFO   skip S210 XEL: no contract under $75
Live micro done. open_options=2 lots=1
2026-08-20 11:26:50,980 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=35 paper_keys=yes dry_run=False
  alpaca positions=12
options_reconcile: done
Layout: grid:100:baseline (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> grid:100:baseline)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-08-20T11:26:52.499262-04:00 ===

[Run context]
2026-08-20 11:26:52,620 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-20 11:27:00,673 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-20 11:27:16,748 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
2026-08-20 11:27:40,799 WARNING paper get_account failed attempt 4/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 32s
2026-08-20 11:28:12,835 WARNING paper get_account failed attempt 5/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 40s
2026-08-20 11:28:52,875 ERROR paper get_account failed after 6 attempts: {"code":50010000,"message":"internal server error occurred"}
WARN: get_account failed ({"code":50010000,"message":"internal server error occurred"}) but positions OK (n=12). Keys are fine; Alpaca account endpoint is flaky. Continuing manage/exits; skipping new entries until equity is readable.
2026-08-20 11:28:52,963 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-20 11:29:01,001 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-20 11:29:17,037 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
2026-08-20 11:29:41,073 WARNING paper get_account failed attempt 4/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 32s
2026-08-20 11:30:13,108 WARNING paper get_account failed attempt 5/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 40s
```

---

## Run 20260820T153515Z

- UTC timestamp: `20260820T153515Z`
- GitHub run: [#7630](https://github.com/28twagg-ops/TradingBot/actions/runs/32386498381)
- Run id: `32386498381`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T153515Z_live_bot.log`, `logs/action_runs/20260820T153515Z_live_options.log`, `logs/action_runs/20260820T153515Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 821 | 41.8 | -47.5 | +15.4 | $+8,207 |
| TAINTED | 1761 | 33.0 | -39.3 | +12.2 | $-9,205 |
| KEEP-only | 294 | 63.3 | +37.5 | +42.9 | $+5,699 |
| KEEP-only recent | 106 | 58.5 | +50.0 | +54.8 | $+1,673 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406
- KILL strategies (16): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-17T19:56:23.633587-04:00","date":"2026-08-17","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":261.1,"phases_s":{"reconcile":140.41},"signals":0,"placed":0,"equity":null,"open_positions":14,"pending_orders":0,"open_lots":45,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"7335","github_run_id":"32082431205","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:35:16  INFO      Mode: exits
15:35:17  INFO        Daily log -> logs/daily/2026-08-20.md
15:35:17  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (3 ledger rows)
15:35:17  INFO        place_all_stops: checking 4 positions...
15:35:17  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
15:35:17  INFO        STOP skipped MNST: fractional (0.6350 shares) — software exit will handle it
15:35:18  INFO        [positions] 2/2 (2 valid)
15:35:18  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:35 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $438.64|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L -0.0%  $-0.01                                           HOLD|
|  AON  P&L +1.0%  $+0.69                                            HOLD|
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
|  CL260821C00090000       $0.52    $0.50    -3.8%    $-2.00    $50.00   |
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
|                                                                        |
|  Options open P&L                                                $-9.00|
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
=== options_live_micro LIVE 2026-08-20T11:35:19.407286-04:00 share=50% ===
2026-08-20 11:35:19,407 INFO === options_live_micro LIVE 2026-08-20T11:35:19.407286-04:00 share=50% ===
Live account equity $438.61 cash $285.87 #225458845 options_level=3
2026-08-20 11:35:19,620 INFO Live account equity $438.61 cash $285.87 #225458845 options_level=3
Live micro hold S218 CL260821C00090000 -3.8% (tp +50% / sl -50%)
2026-08-20 11:35:19,810 INFO Live micro hold S218 CL260821C00090000 -3.8% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-20 11:35:19,942 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-20 11:35:20,001 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=35 paper_keys=yes dry_run=False
  alpaca positions=12
options_reconcile: done
Layout: grid:100:baseline (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> grid:100:baseline)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-08-20T11:35:21.552544-04:00 ===

[Run context]
2026-08-20 11:35:21,779 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-20 11:35:29,842 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-20 11:35:45,903 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
```

---

## Run 20260820T153657Z

- UTC timestamp: `20260820T153657Z`
- GitHub run: [#7631](https://github.com/28twagg-ops/TradingBot/actions/runs/32386999800)
- Run id: `32386999800`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T153657Z_live_bot.log`, `logs/action_runs/20260820T153657Z_live_options.log`, `logs/action_runs/20260820T153657Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 821 | 41.8 | -47.5 | +15.4 | $+8,207 |
| TAINTED | 1761 | 33.0 | -39.3 | +12.2 | $-9,205 |
| KEEP-only | 294 | 63.3 | +37.5 | +42.9 | $+5,699 |
| KEEP-only recent | 106 | 58.5 | +50.0 | +54.8 | $+1,673 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406
- KILL strategies (16): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-17T19:56:23.633587-04:00","date":"2026-08-17","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":261.1,"phases_s":{"reconcile":140.41},"signals":0,"placed":0,"equity":null,"open_positions":14,"pending_orders":0,"open_lots":45,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"7335","github_run_id":"32082431205","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:36:59  INFO      Mode: exits
15:36:59  INFO        Daily log -> logs/daily/2026-08-20.md
15:36:59  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (3 ledger rows)
15:36:59  INFO        place_all_stops: checking 4 positions...
15:36:59  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
15:36:59  INFO        STOP skipped MNST: fractional (0.6350 shares) — software exit will handle it
15:36:59  INFO        [positions] 2/2 (2 valid)
15:36:59  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $438.65|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.1%  $+0.03                                           HOLD|
|  AON  P&L +1.0%  $+0.69                                            HOLD|
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
|  CL260821C00090000       $0.52    $0.50    -3.8%    $-2.00    $50.00   |
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
|                                                                        |
|  Options open P&L                                                $-9.00|
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
=== options_live_micro LIVE 2026-08-20T11:37:00.676982-04:00 share=50% ===
2026-08-20 11:37:00,677 INFO === options_live_micro LIVE 2026-08-20T11:37:00.676982-04:00 share=50% ===
Live account equity $438.65 cash $285.87 #225458845 options_level=3
2026-08-20 11:37:00,732 INFO Live account equity $438.65 cash $285.87 #225458845 options_level=3
Live micro hold S218 CL260821C00090000 -3.8% (tp +50% / sl -50%)
2026-08-20 11:37:00,765 INFO Live micro hold S218 CL260821C00090000 -3.8% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-20 11:37:00,792 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-20 11:37:00,814 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=35 paper_keys=yes dry_run=False
  alpaca positions=12
options_reconcile: done
Layout: grid:100:baseline (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> grid:100:baseline)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-08-20T11:37:02.375213-04:00 ===

[Run context]
2026-08-20 11:37:02,558 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-20 11:37:10,589 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-20 11:37:26,602 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
2026-08-20 11:37:50,629 WARNING paper get_account failed attempt 4/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 32s
2026-08-20 11:38:22,655 WARNING paper get_account failed attempt 5/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 40s
2026-08-20 11:39:02,672 ERROR paper get_account failed after 6 attempts: {"code":50010000,"message":"internal server error occurred"}
WARN: get_account failed ({"code":50010000,"message":"internal server error occurred"}) but positions OK (n=12). Keys are fine; Alpaca account endpoint is flaky. Continuing manage/exits; skipping new entries until equity is readable.
2026-08-20 11:39:02,705 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-20 11:39:10,759 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-20 11:39:26,772 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
2026-08-20 11:39:50,784 WARNING paper get_account failed attempt 4/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 32s
2026-08-20 11:40:22,806 WARNING paper get_account failed attempt 5/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 40s
```

---

## Run 20260820T154711Z

- UTC timestamp: `20260820T154711Z`
- GitHub run: [#7633](https://github.com/28twagg-ops/TradingBot/actions/runs/32387985731)
- Run id: `32387985731`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T154711Z_live_bot.log`, `logs/action_runs/20260820T154711Z_live_options.log`, `logs/action_runs/20260820T154711Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 821 | 41.8 | -47.5 | +15.4 | $+8,207 |
| TAINTED | 1761 | 33.0 | -39.3 | +12.2 | $-9,205 |
| KEEP-only | 294 | 63.3 | +37.5 | +42.9 | $+5,699 |
| KEEP-only recent | 106 | 58.5 | +50.0 | +54.8 | $+1,673 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406
- KILL strategies (16): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-17T19:56:23.633587-04:00","date":"2026-08-17","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":261.1,"phases_s":{"reconcile":140.41},"signals":0,"placed":0,"equity":null,"open_positions":14,"pending_orders":0,"open_lots":45,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"7335","github_run_id":"32082431205","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:47:12  INFO      Mode: exits
15:47:13  INFO        Daily log -> logs/daily/2026-08-20.md
15:47:13  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (3 ledger rows)
15:47:13  INFO        place_all_stops: checking 4 positions...
15:47:13  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
15:47:13  INFO        STOP skipped MNST: fractional (0.6350 shares) — software exit will handle it
15:47:13  INFO        [positions] 2/2 (2 valid)
15:47:13  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:47 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $438.81|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.2%  $+0.05                                           HOLD|
|  AON  P&L +1.2%  $+0.83                                            HOLD|
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
|  CL260821C00090000       $0.52    $0.50    -3.8%    $-2.00    $50.00   |
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
|                                                                        |
|  Options open P&L                                                $-9.00|
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
=== options_live_micro LIVE 2026-08-20T11:47:14.514977-04:00 share=50% ===
2026-08-20 11:47:14,515 INFO === options_live_micro LIVE 2026-08-20T11:47:14.514977-04:00 share=50% ===
Live account equity $438.81 cash $285.87 #225458845 options_level=3
2026-08-20 11:47:14,565 INFO Live account equity $438.81 cash $285.87 #225458845 options_level=3
Live micro hold S218 CL260821C00090000 -3.8% (tp +50% / sl -50%)
2026-08-20 11:47:14,586 INFO Live micro hold S218 CL260821C00090000 -3.8% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-20 11:47:14,604 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-20 11:47:14,612 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=35 paper_keys=yes dry_run=False
  alpaca positions=12
options_reconcile: done
Layout: grid:100:baseline (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> grid:100:baseline)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-08-20T11:47:16.242792-04:00 ===

[Run context]
2026-08-20 11:47:16,290 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-20 11:47:24,303 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-20 11:47:40,316 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
2026-08-20 11:48:04,328 WARNING paper get_account failed attempt 4/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 32s
2026-08-20 11:48:36,361 WARNING paper get_account failed attempt 5/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 40s
2026-08-20 11:49:16,385 ERROR paper get_account failed after 6 attempts: {"code":50010000,"message":"internal server error occurred"}
WARN: get_account failed ({"code":50010000,"message":"internal server error occurred"}) but positions OK (n=12). Keys are fine; Alpaca account endpoint is flaky. Continuing manage/exits; skipping new entries until equity is readable.
2026-08-20 11:49:16,417 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-20 11:49:24,428 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-20 11:49:40,446 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
2026-08-20 11:50:04,559 WARNING paper get_account failed attempt 4/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 32s
```

---

## Run 20260820T160629Z

- UTC timestamp: `20260820T160629Z`
- GitHub run: [#7637](https://github.com/28twagg-ops/TradingBot/actions/runs/32389963336)
- Run id: `32389963336`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T160629Z_live_bot.log`, `logs/action_runs/20260820T160629Z_live_options.log`, `logs/action_runs/20260820T160629Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 821 | 41.8 | -47.5 | +15.4 | $+8,207 |
| TAINTED | 1761 | 33.0 | -39.3 | +12.2 | $-9,205 |
| KEEP-only | 294 | 63.3 | +37.5 | +42.9 | $+5,699 |
| KEEP-only recent | 106 | 58.5 | +50.0 | +54.8 | $+1,673 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406
- KILL strategies (16): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-17T19:56:23.633587-04:00","date":"2026-08-17","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":261.1,"phases_s":{"reconcile":140.41},"signals":0,"placed":0,"equity":null,"open_positions":14,"pending_orders":0,"open_lots":45,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"7335","github_run_id":"32082431205","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
16:06:30  INFO      Mode: exits
16:06:31  INFO        Daily log -> logs/daily/2026-08-20.md
16:06:31  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (3 ledger rows)
16:06:31  INFO        place_all_stops: checking 4 positions...
16:06:31  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
16:06:31  INFO        STOP skipped MNST: fractional (0.6350 shares) — software exit will handle it
16:06:31  INFO        [positions] 2/2 (2 valid)
16:06:32  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $423.00|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.1%  $+0.04                                           HOLD|
|  AON  P&L +1.5%  $+1.02                                            HOLD|
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
|  CL260821C00090000       $0.52    $0.35    -32.7%   $-17.00   $35.00   |
|  WMT260821C00110000      $0.09    $0.01    -88.9%   $-8.00    $1.00    |
|                                                                        |
|  Options open P&L                                               $-25.00|
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
=== options_live_micro LIVE 2026-08-20T12:06:33.064550-04:00 share=50% ===
2026-08-20 12:06:33,064 INFO === options_live_micro LIVE 2026-08-20T12:06:33.064550-04:00 share=50% ===
Live account equity $423.00 cash $285.87 #225458845 options_level=3
2026-08-20 12:06:33,290 INFO Live account equity $423.00 cash $285.87 #225458845 options_level=3
Live micro hold S218 CL260821C00090000 -32.7% (tp +50% / sl -50%)
2026-08-20 12:06:33,440 INFO Live micro hold S218 CL260821C00090000 -32.7% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-20 12:06:33,582 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-20 12:06:33,659 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=35 paper_keys=yes dry_run=False
  alpaca positions=12
options_reconcile: done
Layout: grid:100:baseline (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> grid:100:baseline)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-08-20T12:06:35.524725-04:00 ===

[Run context]
2026-08-20 12:06:35,764 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-20 12:06:43,840 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-20 12:06:59,916 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
2026-08-20 12:07:24,001 WARNING paper get_account failed attempt 4/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 32s
2026-08-20 12:07:56,079 WARNING paper get_account failed attempt 5/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 40s
2026-08-20 12:08:36,152 ERROR paper get_account failed after 6 attempts: {"code":50010000,"message":"internal server error occurred"}
WARN: get_account failed ({"code":50010000,"message":"internal server error occurred"}) but positions OK (n=12). Keys are fine; Alpaca account endpoint is flaky. Continuing manage/exits; skipping new entries until equity is readable.
2026-08-20 12:08:36,347 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-20 12:08:44,419 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-20 12:09:00,492 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
2026-08-20 12:09:24,565 WARNING paper get_account failed attempt 4/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 32s
2026-08-20 12:09:56,665 WARNING paper get_account failed attempt 5/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 40s
2026-08-20 12:10:36,741 ERROR paper get_account failed after 6 attempts: {"code":50010000,"message":"internal server error occurred"}
2026-08-20 12:10:36,818 WARNING lab get_account failed attempt 1/3: {"code":50010000,"message":"internal server error occurred"}
2026-08-20 12:10:46,904 WARNING lab get_account failed attempt 2/3: {"code":50010000,"message":"internal server error occurred"}
```

---

## Run 20260820T161218Z

- UTC timestamp: `20260820T161218Z`
- GitHub run: [#7638](https://github.com/28twagg-ops/TradingBot/actions/runs/32390444144)
- Run id: `32390444144`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T161218Z_live_bot.log`, `logs/action_runs/20260820T161218Z_live_options.log`, `logs/action_runs/20260820T161218Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 821 | 41.8 | -47.5 | +15.4 | $+8,207 |
| TAINTED | 1761 | 33.0 | -39.3 | +12.2 | $-9,205 |
| KEEP-only | 294 | 63.3 | +37.5 | +42.9 | $+5,699 |
| KEEP-only recent | 106 | 58.5 | +50.0 | +54.8 | $+1,673 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406
- KILL strategies (16): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-17T19:56:23.633587-04:00","date":"2026-08-17","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":261.1,"phases_s":{"reconcile":140.41},"signals":0,"placed":0,"equity":null,"open_positions":14,"pending_orders":0,"open_lots":45,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"7335","github_run_id":"32082431205","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
16:12:19  INFO      Mode: exits
16:12:19  INFO        Daily log -> logs/daily/2026-08-20.md
16:12:19  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (3 ledger rows)
16:12:19  INFO        place_all_stops: checking 4 positions...
16:12:19  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
16:12:19  INFO        STOP skipped MNST: fractional (0.6350 shares) — software exit will handle it
16:12:19  INFO        [positions] 2/2 (2 valid)
16:12:20  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:12 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $423.91|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.3%  $+0.09                                           HOLD|
|  AON  P&L +1.3%  $+0.90                                            HOLD|
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
|  CL260821C00090000       $0.52    $0.35    -32.7%   $-17.00   $35.00   |
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
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
=== options_live_micro LIVE 2026-08-20T12:12:20.898360-04:00 share=50% ===
2026-08-20 12:12:20,898 INFO === options_live_micro LIVE 2026-08-20T12:12:20.898360-04:00 share=50% ===
Live account equity $423.91 cash $285.87 #225458845 options_level=3
2026-08-20 12:12:20,947 INFO Live account equity $423.91 cash $285.87 #225458845 options_level=3
Live micro hold S218 CL260821C00090000 -32.7% (tp +50% / sl -50%)
2026-08-20 12:12:20,972 INFO Live micro hold S218 CL260821C00090000 -32.7% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-20 12:12:20,991 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-20 12:12:20,999 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=35 paper_keys=yes dry_run=False
  alpaca positions=12
options_reconcile: done
Layout: grid:100:baseline (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> grid:100:baseline)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-08-20T12:12:22.485862-04:00 ===

[Run context]
2026-08-20 12:12:22,560 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-20 12:12:30,582 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-20 12:12:46,596 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
2026-08-20 12:13:10,616 WARNING paper get_account failed attempt 4/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 32s
2026-08-20 12:13:42,631 WARNING paper get_account failed attempt 5/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 40s
2026-08-20 12:14:22,651 ERROR paper get_account failed after 6 attempts: {"code":50010000,"message":"internal server error occurred"}
WARN: get_account failed ({"code":50010000,"message":"internal server error occurred"}) but positions OK (n=12). Keys are fine; Alpaca account endpoint is flaky. Continuing manage/exits; skipping new entries until equity is readable.
2026-08-20 12:14:22,684 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-20 12:14:30,696 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-20 12:14:46,718 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
2026-08-20 12:15:10,734 WARNING paper get_account failed attempt 4/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 32s
```

---

## Run 20260820T161634Z

- UTC timestamp: `20260820T161634Z`
- GitHub run: [#7639](https://github.com/28twagg-ops/TradingBot/actions/runs/32390927531)
- Run id: `32390927531`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T161634Z_live_bot.log`, `logs/action_runs/20260820T161634Z_live_options.log`, `logs/action_runs/20260820T161634Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 821 | 41.8 | -47.5 | +15.4 | $+8,207 |
| TAINTED | 1761 | 33.0 | -39.3 | +12.2 | $-9,205 |
| KEEP-only | 294 | 63.3 | +37.5 | +42.9 | $+5,699 |
| KEEP-only recent | 106 | 58.5 | +50.0 | +54.8 | $+1,673 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406
- KILL strategies (16): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-17T19:56:23.633587-04:00","date":"2026-08-17","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":261.1,"phases_s":{"reconcile":140.41},"signals":0,"placed":0,"equity":null,"open_positions":14,"pending_orders":0,"open_lots":45,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"7335","github_run_id":"32082431205","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
16:16:35  INFO      Mode: exits
16:16:36  INFO        Daily log -> logs/daily/2026-08-20.md
16:16:36  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (3 ledger rows)
16:16:36  INFO        place_all_stops: checking 4 positions...
16:16:36  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
16:16:36  INFO        STOP skipped MNST: fractional (0.6350 shares) — software exit will handle it
16:16:36  INFO        [positions] 2/2 (2 valid)
16:16:37  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $427.86|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.4%  $+0.11                                           HOLD|
|  AON  P&L +1.2%  $+0.82                                            HOLD|
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
|  CL260821C00090000       $0.52    $0.40    -23.1%   $-12.00   $40.00   |
|  WMT260821C00110000      $0.09    $0.01    -88.9%   $-8.00    $1.00    |
|                                                                        |
|  Options open P&L                                               $-20.00|
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
=== options_live_micro LIVE 2026-08-20T12:16:37.963397-04:00 share=50% ===
2026-08-20 12:16:37,963 INFO === options_live_micro LIVE 2026-08-20T12:16:37.963397-04:00 share=50% ===
Live account equity $427.86 cash $285.87 #225458845 options_level=3
2026-08-20 12:16:38,222 INFO Live account equity $427.86 cash $285.87 #225458845 options_level=3
Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
2026-08-20 12:16:38,388 INFO Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-20 12:16:38,538 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-20 12:16:38,619 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=35 paper_keys=yes dry_run=False
  alpaca positions=12
options_reconcile: done
Layout: grid:100:baseline (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> grid:100:baseline)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-08-20T12:16:40.207159-04:00 ===

[Run context]
2026-08-20 12:16:40,446 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-20 12:16:48,522 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-20 12:17:04,624 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
2026-08-20 12:17:28,715 WARNING paper get_account failed attempt 4/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 32s
2026-08-20 12:18:00,864 WARNING paper get_account failed attempt 5/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 40s
2026-08-20 12:18:40,941 ERROR paper get_account failed after 6 attempts: {"code":50010000,"message":"internal server error occurred"}
WARN: get_account failed ({"code":50010000,"message":"internal server error occurred"}) but positions OK (n=12). Keys are fine; Alpaca account endpoint is flaky. Continuing manage/exits; skipping new entries until equity is readable.
2026-08-20 12:18:41,120 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-20 12:18:49,200 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-20 12:19:05,282 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
2026-08-20 12:19:29,360 WARNING paper get_account failed attempt 4/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 32s
2026-08-20 12:20:01,437 WARNING paper get_account failed attempt 5/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 40s
2026-08-20 12:20:41,513 ERROR paper get_account failed after 6 attempts: {"code":50010000,"message":"internal server error occurred"}
2026-08-20 12:20:41,596 WARNING lab get_account failed attempt 1/3: {"code":50010000,"message":"internal server error occurred"}
2026-08-20 12:20:51,675 WARNING lab get_account failed attempt 2/3: {"code":50010000,"message":"internal server error occurred"}
2026-08-20 12:21:01,752 ERROR lab get_account failed after 3 attempts: {"code":50010000,"message":"internal server error occurred"}

[Setup]
LIVE MIRROR control study — strategies: S210, S218, S404, S406 | baseline arm only (same TP/SL as live micro)
Allowed (new entries only): S210, S218, S404, S406
  EXIT [b776|lab0776_s397_w1_0928_1005_r1|S397] take_profit (+229.8%) SELL failed MARA260821C00009000: {"code":50010000,"message":"internal server error occurred"}
  EXIT [b0|orphan_reconcile|ORPHAN] take_profit (+229.8%) SELL failed MARA260821C00009000: {"code":50010000,"message":"internal server error occurred"}
  EXIT [b115|lab0115_s212_w4_1120_1135_r2|S212] stop_loss (-100.0%) SELL failed MCD260821C00290000: {"code":50010000,"message":"internal server error occurred"}
```

---

## Run 20260820T163225Z

- UTC timestamp: `20260820T163225Z`
- GitHub run: [#7642](https://github.com/28twagg-ops/TradingBot/actions/runs/32392328246)
- Run id: `32392328246`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T163225Z_live_bot.log`, `logs/action_runs/20260820T163225Z_live_options.log`, `logs/action_runs/20260820T163225Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 821 | 41.8 | -47.5 | +15.4 | $+8,207 |
| TAINTED | 1761 | 33.0 | -39.3 | +12.2 | $-9,205 |
| KEEP-only | 294 | 63.3 | +37.5 | +42.9 | $+5,699 |
| KEEP-only recent | 106 | 58.5 | +50.0 | +54.8 | $+1,673 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406
- KILL strategies (16): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-17T19:56:23.633587-04:00","date":"2026-08-17","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":261.1,"phases_s":{"reconcile":140.41},"signals":0,"placed":0,"equity":null,"open_positions":14,"pending_orders":0,"open_lots":45,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"7335","github_run_id":"32082431205","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
16:32:26  INFO      Mode: exits
16:32:27  INFO        Daily log -> logs/daily/2026-08-20.md
16:32:27  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (3 ledger rows)
16:32:27  INFO        place_all_stops: checking 4 positions...
16:32:27  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
16:32:27  INFO        STOP skipped MNST: fractional (0.6350 shares) — software exit will handle it
16:32:28  INFO        [positions] 2/2 (2 valid)
16:32:28  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:32 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $428.72|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.4%  $+0.11                                           HOLD|
|  AON  P&L +1.0%  $+0.69                                            HOLD|
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
|  CL260821C00090000       $0.52    $0.40    -23.1%   $-12.00   $40.00   |
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
|                                                                        |
|  Options open P&L                                               $-19.00|
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
=== options_live_micro LIVE 2026-08-20T12:32:29.422727-04:00 share=50% ===
2026-08-20 12:32:29,422 INFO === options_live_micro LIVE 2026-08-20T12:32:29.422727-04:00 share=50% ===
Live account equity $428.72 cash $285.87 #225458845 options_level=3
2026-08-20 12:32:29,635 INFO Live account equity $428.72 cash $285.87 #225458845 options_level=3
Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
2026-08-20 12:32:29,760 INFO Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-20 12:32:29,878 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-20 12:32:29,938 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=35 paper_keys=yes dry_run=False
  alpaca positions=12
options_reconcile: done
Layout: grid:100:baseline (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> grid:100:baseline)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-08-20T12:32:31.560364-04:00 ===

[Run context]
2026-08-20 12:32:31,770 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-20 12:32:39,844 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-20 12:32:55,907 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
2026-08-20 12:33:19,970 WARNING paper get_account failed attempt 4/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 32s
2026-08-20 12:33:52,035 WARNING paper get_account failed attempt 5/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 40s
2026-08-20 12:34:32,098 ERROR paper get_account failed after 6 attempts: {"code":50010000,"message":"internal server error occurred"}
WARN: get_account failed ({"code":50010000,"message":"internal server error occurred"}) but positions OK (n=12). Keys are fine; Alpaca account endpoint is flaky. Continuing manage/exits; skipping new entries until equity is readable.
2026-08-20 12:34:32,253 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-20 12:34:40,317 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-20 12:34:56,380 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
2026-08-20 12:35:20,446 WARNING paper get_account failed attempt 4/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 32s
2026-08-20 12:35:52,525 WARNING paper get_account failed attempt 5/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 40s
```

---

## Run 20260820T163704Z

- UTC timestamp: `20260820T163704Z`
- GitHub run: [#7643](https://github.com/28twagg-ops/TradingBot/actions/runs/32392808528)
- Run id: `32392808528`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T163704Z_live_bot.log`, `logs/action_runs/20260820T163704Z_live_options.log`, `logs/action_runs/20260820T163704Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 821 | 41.8 | -47.5 | +15.4 | $+8,207 |
| TAINTED | 1761 | 33.0 | -39.3 | +12.2 | $-9,205 |
| KEEP-only | 294 | 63.3 | +37.5 | +42.9 | $+5,699 |
| KEEP-only recent | 106 | 58.5 | +50.0 | +54.8 | $+1,673 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406
- KILL strategies (16): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-17T19:56:23.633587-04:00","date":"2026-08-17","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":261.1,"phases_s":{"reconcile":140.41},"signals":0,"placed":0,"equity":null,"open_positions":14,"pending_orders":0,"open_lots":45,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"7335","github_run_id":"32082431205","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
16:37:06  INFO      Mode: exits
16:37:06  INFO        Daily log -> logs/daily/2026-08-20.md
16:37:06  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (3 ledger rows)
16:37:07  INFO        place_all_stops: checking 4 positions...
16:37:07  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
16:37:07  INFO        STOP skipped MNST: fractional (0.6350 shares) — software exit will handle it
16:37:07  INFO        [positions] 2/2 (2 valid)
16:37:07  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:37 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $428.69|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.4%  $+0.11                                           HOLD|
|  AON  P&L +0.9%  $+0.65                                            HOLD|
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
|  CL260821C00090000       $0.52    $0.40    -23.1%   $-12.00   $40.00   |
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
|                                                                        |
|  Options open P&L                                               $-19.00|
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
=== options_live_micro LIVE 2026-08-20T12:37:08.371046-04:00 share=50% ===
2026-08-20 12:37:08,371 INFO === options_live_micro LIVE 2026-08-20T12:37:08.371046-04:00 share=50% ===
Live account equity $428.69 cash $285.87 #225458845 options_level=3
2026-08-20 12:37:08,619 INFO Live account equity $428.69 cash $285.87 #225458845 options_level=3
Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
2026-08-20 12:37:08,750 INFO Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-20 12:37:08,877 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-20 12:37:08,936 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=35 paper_keys=yes dry_run=False
  alpaca positions=12
options_reconcile: done
Layout: grid:100:baseline (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> grid:100:baseline)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-08-20T12:37:10.288151-04:00 ===

[Run context]
2026-08-20 12:37:10,499 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-20 12:37:18,574 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-20 12:37:34,638 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
2026-08-20 12:37:58,701 WARNING paper get_account failed attempt 4/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 32s
2026-08-20 12:38:30,764 WARNING paper get_account failed attempt 5/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 40s
2026-08-20 12:39:10,825 ERROR paper get_account failed after 6 attempts: {"code":50010000,"message":"internal server error occurred"}
WARN: get_account failed ({"code":50010000,"message":"internal server error occurred"}) but positions OK (n=12). Keys are fine; Alpaca account endpoint is flaky. Continuing manage/exits; skipping new entries until equity is readable.
2026-08-20 12:39:10,946 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-20 12:39:19,011 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-20 12:39:35,074 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
2026-08-20 12:39:59,144 WARNING paper get_account failed attempt 4/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 32s
2026-08-20 12:40:31,213 WARNING paper get_account failed attempt 5/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 40s
```

---

## Run 20260820T164145Z

- UTC timestamp: `20260820T164145Z`
- GitHub run: [#7644](https://github.com/28twagg-ops/TradingBot/actions/runs/32393273386)
- Run id: `32393273386`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T164145Z_live_bot.log`, `logs/action_runs/20260820T164145Z_live_options.log`, `logs/action_runs/20260820T164145Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 821 | 41.8 | -47.5 | +15.4 | $+8,207 |
| TAINTED | 1761 | 33.0 | -39.3 | +12.2 | $-9,205 |
| KEEP-only | 294 | 63.3 | +37.5 | +42.9 | $+5,699 |
| KEEP-only recent | 106 | 58.5 | +50.0 | +54.8 | $+1,673 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406
- KILL strategies (16): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-17T19:56:23.633587-04:00","date":"2026-08-17","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":261.1,"phases_s":{"reconcile":140.41},"signals":0,"placed":0,"equity":null,"open_positions":14,"pending_orders":0,"open_lots":45,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"7335","github_run_id":"32082431205","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
16:41:46  INFO      Mode: exits
16:41:46  INFO        Daily log -> logs/daily/2026-08-20.md
16:41:46  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (3 ledger rows)
16:41:46  INFO        place_all_stops: checking 4 positions...
16:41:46  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
16:41:46  INFO        STOP skipped MNST: fractional (0.6350 shares) — software exit will handle it
16:41:47  INFO        [positions] 2/2 (2 valid)
16:41:47  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $428.63|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.4%  $+0.11                                           HOLD|
|  AON  P&L +0.8%  $+0.59                                            HOLD|
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
|  CL260821C00090000       $0.52    $0.40    -23.1%   $-12.00   $40.00   |
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
|                                                                        |
|  Options open P&L                                               $-19.00|
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
=== options_live_micro LIVE 2026-08-20T12:41:47.995334-04:00 share=50% ===
2026-08-20 12:41:47,995 INFO === options_live_micro LIVE 2026-08-20T12:41:47.995334-04:00 share=50% ===
Live account equity $428.63 cash $285.87 #225458845 options_level=3
2026-08-20 12:41:48,045 INFO Live account equity $428.63 cash $285.87 #225458845 options_level=3
Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
2026-08-20 12:41:48,160 INFO Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-20 12:41:48,188 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-20 12:41:48,209 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=35 paper_keys=yes dry_run=False
  alpaca positions=12
options_reconcile: done
Layout: grid:100:baseline (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> grid:100:baseline)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-08-20T12:41:49.657305-04:00 ===

[Run context]
2026-08-20 12:41:49,732 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-20 12:41:57,749 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-20 12:42:13,761 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
2026-08-20 12:42:37,783 WARNING paper get_account failed attempt 4/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 32s
2026-08-20 12:43:09,797 WARNING paper get_account failed attempt 5/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 40s
2026-08-20 12:43:49,811 ERROR paper get_account failed after 6 attempts: {"code":50010000,"message":"internal server error occurred"}
WARN: get_account failed ({"code":50010000,"message":"internal server error occurred"}) but positions OK (n=12). Keys are fine; Alpaca account endpoint is flaky. Continuing manage/exits; skipping new entries until equity is readable.
2026-08-20 12:43:49,834 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-20 12:43:57,848 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-20 12:44:13,869 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
2026-08-20 12:44:37,883 WARNING paper get_account failed attempt 4/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 32s
2026-08-20 12:45:09,898 WARNING paper get_account failed attempt 5/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 40s
```

---

## Run 20260820T164637Z

- UTC timestamp: `20260820T164637Z`
- GitHub run: [#7645](https://github.com/28twagg-ops/TradingBot/actions/runs/32393746325)
- Run id: `32393746325`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T164637Z_live_bot.log`, `logs/action_runs/20260820T164637Z_live_options.log`, `logs/action_runs/20260820T164637Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 821 | 41.8 | -47.5 | +15.4 | $+8,207 |
| TAINTED | 1761 | 33.0 | -39.3 | +12.2 | $-9,205 |
| KEEP-only | 294 | 63.3 | +37.5 | +42.9 | $+5,699 |
| KEEP-only recent | 106 | 58.5 | +50.0 | +54.8 | $+1,673 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406
- KILL strategies (16): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-17T19:56:23.633587-04:00","date":"2026-08-17","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":261.1,"phases_s":{"reconcile":140.41},"signals":0,"placed":0,"equity":null,"open_positions":14,"pending_orders":0,"open_lots":45,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"7335","github_run_id":"32082431205","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
16:46:39  INFO      Mode: exits
16:46:40  INFO        Daily log -> logs/daily/2026-08-20.md
16:46:40  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (3 ledger rows)
16:46:40  INFO        place_all_stops: checking 4 positions...
16:46:40  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
16:46:40  INFO        STOP skipped MNST: fractional (0.6350 shares) — software exit will handle it
16:46:41  INFO        [positions] 2/2 (2 valid)
16:46:41  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $428.52|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.2%  $+0.06                                           HOLD|
|  AON  P&L +0.7%  $+0.52                                            HOLD|
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
|  CL260821C00090000       $0.52    $0.40    -23.1%   $-12.00   $40.00   |
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
|                                                                        |
|  Options open P&L                                               $-19.00|
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
=== options_live_micro LIVE 2026-08-20T12:46:42.060180-04:00 share=50% ===
2026-08-20 12:46:42,060 INFO === options_live_micro LIVE 2026-08-20T12:46:42.060180-04:00 share=50% ===
Live account equity $428.52 cash $285.87 #225458845 options_level=3
2026-08-20 12:46:42,273 INFO Live account equity $428.52 cash $285.87 #225458845 options_level=3
Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
2026-08-20 12:46:42,392 INFO Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-20 12:46:42,520 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-20 12:46:42,599 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=35 paper_keys=yes dry_run=False
  alpaca positions=12
options_reconcile: done
Layout: grid:100:baseline (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> grid:100:baseline)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-08-20T12:46:44.681230-04:00 ===

[Run context]
2026-08-20 12:46:44,898 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-20 12:46:52,980 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-20 12:47:09,045 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
2026-08-20 12:47:33,114 WARNING paper get_account failed attempt 4/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 32s
2026-08-20 12:48:05,209 WARNING paper get_account failed attempt 5/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 40s
2026-08-20 12:48:45,278 ERROR paper get_account failed after 6 attempts: {"code":50010000,"message":"internal server error occurred"}
WARN: get_account failed ({"code":50010000,"message":"internal server error occurred"}) but positions OK (n=12). Keys are fine; Alpaca account endpoint is flaky. Continuing manage/exits; skipping new entries until equity is readable.
2026-08-20 12:48:45,403 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-20 12:48:53,465 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-20 12:49:09,528 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
2026-08-20 12:49:33,590 WARNING paper get_account failed attempt 4/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 32s
2026-08-20 12:50:05,652 WARNING paper get_account failed attempt 5/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 40s
2026-08-20 12:50:45,715 ERROR paper get_account failed after 6 attempts: {"code":50010000,"message":"internal server error occurred"}
2026-08-20 12:50:45,791 WARNING lab get_account failed attempt 1/3: {"code":50010000,"message":"internal server error occurred"}
2026-08-20 12:50:55,853 WARNING lab get_account failed attempt 2/3: {"code":50010000,"message":"internal server error occurred"}
```

---

## Run 20260820T165203Z

- UTC timestamp: `20260820T165203Z`
- GitHub run: [#7646](https://github.com/28twagg-ops/TradingBot/actions/runs/32394212293)
- Run id: `32394212293`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T165203Z_live_bot.log`, `logs/action_runs/20260820T165203Z_live_options.log`, `logs/action_runs/20260820T165203Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 821 | 41.8 | -47.5 | +15.4 | $+8,207 |
| TAINTED | 1761 | 33.0 | -39.3 | +12.2 | $-9,205 |
| KEEP-only | 294 | 63.3 | +37.5 | +42.9 | $+5,699 |
| KEEP-only recent | 106 | 58.5 | +50.0 | +54.8 | $+1,673 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406
- KILL strategies (16): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-17T19:56:23.633587-04:00","date":"2026-08-17","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":261.1,"phases_s":{"reconcile":140.41},"signals":0,"placed":0,"equity":null,"open_positions":14,"pending_orders":0,"open_lots":45,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"7335","github_run_id":"32082431205","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
16:52:04  INFO      Mode: exits
16:52:05  INFO        Daily log -> logs/daily/2026-08-20.md
16:52:05  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (3 ledger rows)
16:52:05  INFO        place_all_stops: checking 4 positions...
16:52:05  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
16:52:05  INFO        STOP skipped MNST: fractional (0.6350 shares) — software exit will handle it
16:52:05  INFO        [positions] 2/2 (2 valid)
16:52:06  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:52 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $428.53|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.3%  $+0.08                                           HOLD|
|  AON  P&L +0.7%  $+0.51                                            HOLD|
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
|  CL260821C00090000       $0.52    $0.40    -23.1%   $-12.00   $40.00   |
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
|                                                                        |
|  Options open P&L                                               $-19.00|
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
=== options_live_micro LIVE 2026-08-20T12:52:06.907209-04:00 share=50% ===
2026-08-20 12:52:06,907 INFO === options_live_micro LIVE 2026-08-20T12:52:06.907209-04:00 share=50% ===
Live account equity $428.53 cash $285.87 #225458845 options_level=3
2026-08-20 12:52:07,445 INFO Live account equity $428.53 cash $285.87 #225458845 options_level=3
Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
2026-08-20 12:52:07,598 INFO Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-20 12:52:07,767 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-20 12:52:07,843 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=35 paper_keys=yes dry_run=False
  alpaca positions=12
options_reconcile: done
Layout: grid:100:baseline (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> grid:100:baseline)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-08-20T12:52:09.158734-04:00 ===

[Run context]
2026-08-20 12:52:09,428 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-20 12:52:17,501 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-20 12:52:33,573 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
2026-08-20 12:52:57,649 WARNING paper get_account failed attempt 4/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 32s
2026-08-20 12:53:29,724 WARNING paper get_account failed attempt 5/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 40s
2026-08-20 12:54:09,815 ERROR paper get_account failed after 6 attempts: {"code":50010000,"message":"internal server error occurred"}
WARN: get_account failed ({"code":50010000,"message":"internal server error occurred"}) but positions OK (n=12). Keys are fine; Alpaca account endpoint is flaky. Continuing manage/exits; skipping new entries until equity is readable.
2026-08-20 12:54:09,971 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-20 12:54:18,043 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-20 12:54:34,117 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
2026-08-20 12:54:58,196 WARNING paper get_account failed attempt 4/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 32s
2026-08-20 12:55:30,273 WARNING paper get_account failed attempt 5/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 40s
```

---

## Run 20260820T165644Z

- UTC timestamp: `20260820T165644Z`
- GitHub run: [#7647](https://github.com/28twagg-ops/TradingBot/actions/runs/32394675487)
- Run id: `32394675487`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T165644Z_live_bot.log`, `logs/action_runs/20260820T165644Z_live_options.log`, `logs/action_runs/20260820T165644Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 821 | 41.8 | -47.5 | +15.4 | $+8,207 |
| TAINTED | 1761 | 33.0 | -39.3 | +12.2 | $-9,205 |
| KEEP-only | 294 | 63.3 | +37.5 | +42.9 | $+5,699 |
| KEEP-only recent | 106 | 58.5 | +50.0 | +54.8 | $+1,673 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406
- KILL strategies (16): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-17T19:56:23.633587-04:00","date":"2026-08-17","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":261.1,"phases_s":{"reconcile":140.41},"signals":0,"placed":0,"equity":null,"open_positions":14,"pending_orders":0,"open_lots":45,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"7335","github_run_id":"32082431205","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
16:56:45  INFO      Mode: exits
16:56:46  INFO        Daily log -> logs/daily/2026-08-20.md
16:56:46  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (3 ledger rows)
16:56:46  INFO        place_all_stops: checking 4 positions...
16:56:46  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
16:56:46  INFO        STOP skipped MNST: fractional (0.6350 shares) — software exit will handle it
16:56:46  INFO        [positions] 2/2 (2 valid)
16:56:47  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:56 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $428.52|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.2%  $+0.06                                           HOLD|
|  AON  P&L +0.8%  $+0.53                                            HOLD|
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
|  CL260821C00090000       $0.52    $0.40    -23.1%   $-12.00   $40.00   |
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
|                                                                        |
|  Options open P&L                                               $-19.00|
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
=== options_live_micro LIVE 2026-08-20T12:56:47.761531-04:00 share=50% ===
2026-08-20 12:56:47,761 INFO === options_live_micro LIVE 2026-08-20T12:56:47.761531-04:00 share=50% ===
Live account equity $428.52 cash $285.87 #225458845 options_level=3
2026-08-20 12:56:47,964 INFO Live account equity $428.52 cash $285.87 #225458845 options_level=3
Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
2026-08-20 12:56:48,085 INFO Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-20 12:56:48,195 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-20 12:56:48,251 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=35 paper_keys=yes dry_run=False
  alpaca positions=12
options_reconcile: done
Layout: grid:100:baseline (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> grid:100:baseline)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-08-20T12:56:50.097791-04:00 ===

[Run context]
2026-08-20 12:56:50,309 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-20 12:56:58,372 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-20 12:57:14,434 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
2026-08-20 12:57:38,503 WARNING paper get_account failed attempt 4/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 32s
2026-08-20 12:58:10,570 WARNING paper get_account failed attempt 5/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 40s
2026-08-20 12:58:50,635 ERROR paper get_account failed after 6 attempts: {"code":50010000,"message":"internal server error occurred"}
WARN: get_account failed ({"code":50010000,"message":"internal server error occurred"}) but positions OK (n=12). Keys are fine; Alpaca account endpoint is flaky. Continuing manage/exits; skipping new entries until equity is readable.
2026-08-20 12:58:50,765 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-20 12:58:58,835 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-20 12:59:14,923 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
2026-08-20 12:59:39,012 WARNING paper get_account failed attempt 4/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 32s
2026-08-20 13:00:11,074 WARNING paper get_account failed attempt 5/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 40s
```

---

## Run 20260820T170127Z

- UTC timestamp: `20260820T170127Z`
- GitHub run: [#7648](https://github.com/28twagg-ops/TradingBot/actions/runs/32395146922)
- Run id: `32395146922`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T170127Z_live_bot.log`, `logs/action_runs/20260820T170127Z_live_options.log`, `logs/action_runs/20260820T170127Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 821 | 41.8 | -47.5 | +15.4 | $+8,207 |
| TAINTED | 1761 | 33.0 | -39.3 | +12.2 | $-9,205 |
| KEEP-only | 294 | 63.3 | +37.5 | +42.9 | $+5,699 |
| KEEP-only recent | 106 | 58.5 | +50.0 | +54.8 | $+1,673 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406
- KILL strategies (16): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-17T19:56:23.633587-04:00","date":"2026-08-17","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":261.1,"phases_s":{"reconcile":140.41},"signals":0,"placed":0,"equity":null,"open_positions":14,"pending_orders":0,"open_lots":45,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"7335","github_run_id":"32082431205","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
17:01:28  INFO      Mode: exits
17:01:28  INFO        Daily log -> logs/daily/2026-08-20.md
17:01:28  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (3 ledger rows)
17:01:28  INFO        place_all_stops: checking 4 positions...
17:01:28  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
17:01:28  INFO        STOP skipped MNST: fractional (0.6350 shares) — software exit will handle it
17:01:29  INFO        [positions] 2/2 (2 valid)
17:01:29  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $428.49|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.1%  $+0.03                                           HOLD|
|  AON  P&L +0.8%  $+0.53                                            HOLD|
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
|  CL260821C00090000       $0.52    $0.40    -23.1%   $-12.00   $40.00   |
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
|                                                                        |
|  Options open P&L                                               $-19.00|
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
=== options_live_micro LIVE 2026-08-20T13:01:30.184057-04:00 share=50% ===
2026-08-20 13:01:30,184 INFO === options_live_micro LIVE 2026-08-20T13:01:30.184057-04:00 share=50% ===
Live account equity $428.49 cash $285.87 #225458845 options_level=3
2026-08-20 13:01:30,362 INFO Live account equity $428.49 cash $285.87 #225458845 options_level=3
Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
2026-08-20 13:01:30,475 INFO Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-20 13:01:30,570 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-20 13:01:30,635 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=35 paper_keys=yes dry_run=False
  alpaca positions=12
options_reconcile: done
Layout: grid:100:baseline (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> grid:100:baseline)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-08-20T13:01:32.133572-04:00 ===

[Run context]
2026-08-20 13:01:32,271 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-20 13:01:40,304 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-20 13:01:56,339 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
2026-08-20 13:02:20,379 WARNING paper get_account failed attempt 4/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 32s
2026-08-20 13:02:52,415 WARNING paper get_account failed attempt 5/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 40s
2026-08-20 13:03:32,450 ERROR paper get_account failed after 6 attempts: {"code":50010000,"message":"internal server error occurred"}
WARN: get_account failed ({"code":50010000,"message":"internal server error occurred"}) but positions OK (n=12). Keys are fine; Alpaca account endpoint is flaky. Continuing manage/exits; skipping new entries until equity is readable.
2026-08-20 13:03:32,527 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-20 13:03:40,560 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-20 13:03:56,598 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
2026-08-20 13:04:20,662 WARNING paper get_account failed attempt 4/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 32s
2026-08-20 13:04:52,700 WARNING paper get_account failed attempt 5/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 40s
2026-08-20 13:05:32,742 ERROR paper get_account failed after 6 attempts: {"code":50010000,"message":"internal server error occurred"}
2026-08-20 13:05:32,778 WARNING lab get_account failed attempt 1/3: {"code":50010000,"message":"internal server error occurred"}
2026-08-20 13:05:42,811 WARNING lab get_account failed attempt 2/3: {"code":50010000,"message":"internal server error occurred"}
```

---

## Run 20260820T171156Z

- UTC timestamp: `20260820T171156Z`
- GitHub run: [#7650](https://github.com/28twagg-ops/TradingBot/actions/runs/32396083029)
- Run id: `32396083029`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T171156Z_live_bot.log`, `logs/action_runs/20260820T171156Z_live_options.log`, `logs/action_runs/20260820T171156Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 821 | 41.8 | -47.5 | +15.4 | $+8,207 |
| TAINTED | 1761 | 33.0 | -39.3 | +12.2 | $-9,205 |
| KEEP-only | 294 | 63.3 | +37.5 | +42.9 | $+5,699 |
| KEEP-only recent | 106 | 58.5 | +50.0 | +54.8 | $+1,673 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406
- KILL strategies (16): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-17T19:56:23.633587-04:00","date":"2026-08-17","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":261.1,"phases_s":{"reconcile":140.41},"signals":0,"placed":0,"equity":null,"open_positions":14,"pending_orders":0,"open_lots":45,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"7335","github_run_id":"32082431205","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
17:11:57  INFO      Mode: exits
17:11:57  INFO        Daily log -> logs/daily/2026-08-20.md
17:11:57  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (3 ledger rows)
17:11:57  INFO        place_all_stops: checking 4 positions...
17:11:57  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
17:11:57  INFO        STOP skipped MNST: fractional (0.6350 shares) — software exit will handle it
17:11:58  INFO        [positions] 2/2 (2 valid)
17:11:58  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $428.48|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.2%  $+0.07                                           HOLD|
|  AON  P&L +0.7%  $+0.47                                            HOLD|
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
|  CL260821C00090000       $0.52    $0.40    -23.1%   $-12.00   $40.00   |
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
|                                                                        |
|  Options open P&L                                               $-19.00|
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
=== options_live_micro LIVE 2026-08-20T13:11:59.734566-04:00 share=50% ===
2026-08-20 13:11:59,734 INFO === options_live_micro LIVE 2026-08-20T13:11:59.734566-04:00 share=50% ===
Live account equity $428.48 cash $285.87 #225458845 options_level=3
2026-08-20 13:11:59,943 INFO Live account equity $428.48 cash $285.87 #225458845 options_level=3
Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
2026-08-20 13:12:00,080 INFO Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-20 13:12:00,216 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-20 13:12:00,289 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=35 paper_keys=yes dry_run=False
  alpaca positions=12
options_reconcile: done
Layout: grid:100:baseline (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> grid:100:baseline)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-08-20T13:12:01.813501-04:00 ===

[Run context]
2026-08-20 13:12:02,021 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-20 13:12:10,099 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-20 13:12:26,166 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
2026-08-20 13:12:50,234 WARNING paper get_account failed attempt 4/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 32s
2026-08-20 13:13:22,300 WARNING paper get_account failed attempt 5/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 40s
2026-08-20 13:14:02,373 ERROR paper get_account failed after 6 attempts: {"code":50010000,"message":"internal server error occurred"}
WARN: get_account failed ({"code":50010000,"message":"internal server error occurred"}) but positions OK (n=12). Keys are fine; Alpaca account endpoint is flaky. Continuing manage/exits; skipping new entries until equity is readable.
2026-08-20 13:14:02,505 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-20 13:14:10,602 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-20 13:14:26,669 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
2026-08-20 13:14:50,737 WARNING paper get_account failed attempt 4/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 32s
2026-08-20 13:15:22,826 WARNING paper get_account failed attempt 5/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 40s
```

---

## Run 20260820T172029Z

- UTC timestamp: `20260820T172029Z`
- GitHub run: [#7651](https://github.com/28twagg-ops/TradingBot/actions/runs/32396554678)
- Run id: `32396554678`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T172029Z_live_bot.log`, `logs/action_runs/20260820T172029Z_live_options.log`, `logs/action_runs/20260820T172029Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 821 | 41.8 | -47.5 | +15.4 | $+8,207 |
| TAINTED | 1761 | 33.0 | -39.3 | +12.2 | $-9,205 |
| KEEP-only | 294 | 63.3 | +37.5 | +42.9 | $+5,699 |
| KEEP-only recent | 106 | 58.5 | +50.0 | +54.8 | $+1,673 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406
- KILL strategies (16): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-17T19:56:23.633587-04:00","date":"2026-08-17","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":261.1,"phases_s":{"reconcile":140.41},"signals":0,"placed":0,"equity":null,"open_positions":14,"pending_orders":0,"open_lots":45,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"7335","github_run_id":"32082431205","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
17:20:30  INFO      Mode: exits
17:20:31  INFO        Daily log -> logs/daily/2026-08-20.md
17:20:31  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (3 ledger rows)
17:20:31  INFO        place_all_stops: checking 4 positions...
17:20:31  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
17:20:31  INFO        STOP skipped MNST: fractional (0.6350 shares) — software exit will handle it
17:20:31  INFO        [positions] 2/2 (2 valid)
17:20:31  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $428.34|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.1%  $+0.04                                           HOLD|
|  AON  P&L +0.5%  $+0.36                                            HOLD|
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
|  CL260821C00090000       $0.52    $0.40    -23.1%   $-12.00   $40.00   |
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
|                                                                        |
|  Options open P&L                                               $-19.00|
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
=== options_live_micro LIVE 2026-08-20T13:20:32.634724-04:00 share=50% ===
2026-08-20 13:20:32,634 INFO === options_live_micro LIVE 2026-08-20T13:20:32.634724-04:00 share=50% ===
Live account equity $428.34 cash $285.87 #225458845 options_level=3
2026-08-20 13:20:32,721 INFO Live account equity $428.34 cash $285.87 #225458845 options_level=3
Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
2026-08-20 13:20:32,754 INFO Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-20 13:20:32,780 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-20 13:20:32,794 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=35 paper_keys=yes dry_run=False
  alpaca positions=12
options_reconcile: done
Layout: grid:100:baseline (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> grid:100:baseline)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-08-20T13:20:34.224753-04:00 ===

[Run context]
2026-08-20 13:20:34,291 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-20 13:20:42,313 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-20 13:20:58,327 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
```

---

## Run 20260820T172726Z

- UTC timestamp: `20260820T172726Z`
- GitHub run: [#7653](https://github.com/28twagg-ops/TradingBot/actions/runs/32397481331)
- Run id: `32397481331`
- Live bot: exit=`0`, duration=`5s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`181s`
- Full logs: `logs/action_runs/20260820T172726Z_live_bot.log`, `logs/action_runs/20260820T172726Z_live_options.log`, `logs/action_runs/20260820T172726Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 821 | 41.8 | -47.5 | +15.4 | $+8,207 |
| TAINTED | 1761 | 33.0 | -39.3 | +12.2 | $-9,205 |
| KEEP-only | 294 | 63.3 | +37.5 | +42.9 | $+5,699 |
| KEEP-only recent | 106 | 58.5 | +50.0 | +54.8 | $+1,673 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406
- KILL strategies (16): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-20T13:27:34.911505-04:00","date":"2026-08-20","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":175.5,"phases_s":{"reconcile":2.58,"cancel":0.15,"manage":159.64,"protective_stops":3.82},"signals":0,"placed":0,"equity":122196.11,"open_positions":9,"pending_orders":0,"open_lots":35,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"7653","github_run_id":"32397481331","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
17:27:28  INFO      Mode: exits
17:27:29  INFO        Daily log -> logs/daily/2026-08-20.md
17:27:29  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (3 ledger rows)
17:27:29  INFO        place_all_stops: checking 4 positions...
17:27:29  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
17:27:29  INFO        STOP skipped MNST: fractional (0.6350 shares) — software exit will handle it
17:27:30  INFO        [positions] 2/2 (2 valid)
17:27:31  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:27 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $428.34|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.2%  $+0.07                                           HOLD|
|  AON  P&L +0.5%  $+0.33                                            HOLD|
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
|  CL260821C00090000       $0.52    $0.40    -23.1%   $-12.00   $40.00   |
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
|                                                                        |
|  Options open P&L                                               $-19.00|
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
=== options_live_micro LIVE 2026-08-20T13:27:32.402846-04:00 share=50% ===
2026-08-20 13:27:32,402 INFO === options_live_micro LIVE 2026-08-20T13:27:32.402846-04:00 share=50% ===
Live account equity $428.34 cash $285.87 #225458845 options_level=3
2026-08-20 13:27:32,673 INFO Live account equity $428.34 cash $285.87 #225458845 options_level=3
Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
2026-08-20 13:27:32,869 INFO Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-20 13:27:33,069 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-20 13:27:33,158 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
... (183 earlier lines - see full log file)
| Window | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    2 |    1 |    6 |    1 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    21 |
| w2     |    5 |    4 |   10 |    4 |    5 |    4 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    41 |
| w3     |    5 |    4 |   11 |    3 |    5 |    3 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    42 |
| w4     |    4 |    2 |    8 |    2 |    3 |    3 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    31 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 205 | 6 |
| S164 | 229 | 7 |
| S165 | 1675 | 20 |
| S166 | 105 | 4 |
| S167 | 229 | 7 |
| S168 | 150 | 5 |
| S169 | 0 | 0 |
| S170 | 0 | 0 |
| S171 | 0 | 0 |
| S172 | 0 | 0 |
| S175 | 0 | 0 |
| S173 | 1911 | 17 |
| S174 | 891 | 7 |

### Raw log lines per day (debug / multi-bucket)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |    0 |   100 |
| 2026-07-08 |    0 |    0 |  100 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |  100 |   300 |
| 2026-07-09 |    0 |    0 |   24 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |   15 |   139 |
| 2026-07-10 |    0 |    0 |  242 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  230 |  202 |   674 |
| 2026-07-13 |    0 |    0 |  190 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  212 |  188 |   590 |
| 2026-07-14 |    0 |    0 |  194 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  185 |  106 |   485 |
| 2026-07-15 |    0 |    0 |  146 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  154 |   58 |   358 |
| 2026-07-16 |    0 |    0 |  179 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  205 |   58 |   442 |
| 2026-07-17 |    0 |    0 |  127 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  207 |   58 |   392 |
| 2026-07-20 |    0 |    0 |  107 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  143 |   58 |   308 |
| 2026-07-21 |   30 |   35 |  113 |   30 |   35 |   35 |    0 |    0 |    0 |    0 |    0 |  118 |   48 |   444 |
| 2026-07-22 |   40 |   47 |   86 |   15 |   45 |   20 |    0 |    0 |    0 |    0 |    0 |   77 |    0 |   330 |
| 2026-07-23 |   30 |   42 |   50 |   15 |   40 |   20 |    0 |    0 |    0 |    0 |    0 |   40 |    0 |   237 |
| 2026-07-24 |   75 |   87 |   85 |   15 |   77 |   55 |    0 |    0 |    0 |    0 |    0 |   40 |    0 |   434 |
| 2026-07-27 |   14 |    0 |   14 |   14 |   14 |   14 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    70 |
| 2026-07-28 |    6 |    8 |    8 |    8 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |
| 2026-07-29 |   10 |   10 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-08-20
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    35 | WARN | <<<
| Orphaned lots (post-stable) |   975 | WARN | <<<
| Missing exit records (post) |   945 | WARN | <<<
| State/ledger mismatches     |     5 | WARN | <<<
| Total open lots             |    35 | INFO |
| Total closed lots           |  1770 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-20_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-20_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=821 med=-47.5% | TAINTED n=1761 med=-39.3% | KEEP-only n=294 med=+37.5% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=428.34 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 3 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260820T173136Z

- UTC timestamp: `20260820T173136Z`
- GitHub run: [#7654](https://github.com/28twagg-ops/TradingBot/actions/runs/32397947702)
- Run id: `32397947702`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`164s`
- Full logs: `logs/action_runs/20260820T173136Z_live_bot.log`, `logs/action_runs/20260820T173136Z_live_options.log`, `logs/action_runs/20260820T173136Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 821 | 41.8 | -47.5 | +15.4 | $+8,207 |
| TAINTED | 1761 | 33.0 | -39.3 | +12.2 | $-9,205 |
| KEEP-only | 294 | 63.3 | +37.5 | +42.9 | $+5,699 |
| KEEP-only recent | 106 | 58.5 | +50.0 | +54.8 | $+1,673 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406
- KILL strategies (16): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-20T13:31:41.245867-04:00","date":"2026-08-20","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":156.1,"phases_s":{"reconcile":2.11,"cancel":0.01,"manage":144.54,"protective_stops":0.76},"signals":0,"placed":0,"equity":122196.11,"open_positions":9,"pending_orders":0,"open_lots":35,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"7654","github_run_id":"32397947702","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
17:31:37  INFO      Mode: exits
17:31:38  INFO        Daily log -> logs/daily/2026-08-20.md
17:31:38  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (3 ledger rows)
17:31:38  INFO        place_all_stops: checking 4 positions...
17:31:38  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
17:31:38  INFO        STOP skipped MNST: fractional (0.6350 shares) — software exit will handle it
17:31:38  INFO        [positions] 2/2 (2 valid)
17:31:38  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $428.27|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.1%  $+0.04                                           HOLD|
|  AON  P&L +0.4%  $+0.30                                            HOLD|
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
|  CL260821C00090000       $0.52    $0.40    -23.1%   $-12.00   $40.00   |
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
|                                                                        |
|  Options open P&L                                               $-19.00|
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
=== options_live_micro LIVE 2026-08-20T13:31:39.682380-04:00 share=50% ===
2026-08-20 13:31:39,682 INFO === options_live_micro LIVE 2026-08-20T13:31:39.682380-04:00 share=50% ===
Live account equity $428.27 cash $285.87 #225458845 options_level=3
2026-08-20 13:31:39,747 INFO Live account equity $428.27 cash $285.87 #225458845 options_level=3
Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
2026-08-20 13:31:39,793 INFO Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-20 13:31:39,810 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-20 13:31:39,837 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
... (183 earlier lines - see full log file)
| Window | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    2 |    1 |    6 |    1 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    21 |
| w2     |    5 |    4 |   10 |    4 |    5 |    4 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    41 |
| w3     |    5 |    4 |   11 |    3 |    5 |    3 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    42 |
| w4     |    4 |    2 |    8 |    2 |    3 |    3 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    31 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 205 | 6 |
| S164 | 229 | 7 |
| S165 | 1675 | 20 |
| S166 | 105 | 4 |
| S167 | 229 | 7 |
| S168 | 150 | 5 |
| S169 | 0 | 0 |
| S170 | 0 | 0 |
| S171 | 0 | 0 |
| S172 | 0 | 0 |
| S175 | 0 | 0 |
| S173 | 1911 | 17 |
| S174 | 891 | 7 |

### Raw log lines per day (debug / multi-bucket)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |    0 |   100 |
| 2026-07-08 |    0 |    0 |  100 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |  100 |   300 |
| 2026-07-09 |    0 |    0 |   24 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |   15 |   139 |
| 2026-07-10 |    0 |    0 |  242 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  230 |  202 |   674 |
| 2026-07-13 |    0 |    0 |  190 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  212 |  188 |   590 |
| 2026-07-14 |    0 |    0 |  194 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  185 |  106 |   485 |
| 2026-07-15 |    0 |    0 |  146 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  154 |   58 |   358 |
| 2026-07-16 |    0 |    0 |  179 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  205 |   58 |   442 |
| 2026-07-17 |    0 |    0 |  127 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  207 |   58 |   392 |
| 2026-07-20 |    0 |    0 |  107 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  143 |   58 |   308 |
| 2026-07-21 |   30 |   35 |  113 |   30 |   35 |   35 |    0 |    0 |    0 |    0 |    0 |  118 |   48 |   444 |
| 2026-07-22 |   40 |   47 |   86 |   15 |   45 |   20 |    0 |    0 |    0 |    0 |    0 |   77 |    0 |   330 |
| 2026-07-23 |   30 |   42 |   50 |   15 |   40 |   20 |    0 |    0 |    0 |    0 |    0 |   40 |    0 |   237 |
| 2026-07-24 |   75 |   87 |   85 |   15 |   77 |   55 |    0 |    0 |    0 |    0 |    0 |   40 |    0 |   434 |
| 2026-07-27 |   14 |    0 |   14 |   14 |   14 |   14 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    70 |
| 2026-07-28 |    6 |    8 |    8 |    8 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |
| 2026-07-29 |   10 |   10 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-08-20
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    35 | WARN | <<<
| Orphaned lots (post-stable) |   975 | WARN | <<<
| Missing exit records (post) |   945 | WARN | <<<
| State/ledger mismatches     |     5 | WARN | <<<
| Total open lots             |    35 | INFO |
| Total closed lots           |  1770 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-20_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-20_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=821 med=-47.5% | TAINTED n=1761 med=-39.3% | KEEP-only n=294 med=+37.5% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=428.27 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 3 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260820T173558Z

- UTC timestamp: `20260820T173558Z`
- GitHub run: [#7655](https://github.com/28twagg-ops/TradingBot/actions/runs/32398409431)
- Run id: `32398409431`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`164s`
- Full logs: `logs/action_runs/20260820T173558Z_live_bot.log`, `logs/action_runs/20260820T173558Z_live_options.log`, `logs/action_runs/20260820T173558Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 821 | 41.8 | -47.5 | +15.4 | $+8,207 |
| TAINTED | 1761 | 33.0 | -39.3 | +12.2 | $-9,205 |
| KEEP-only | 294 | 63.3 | +37.5 | +42.9 | $+5,699 |
| KEEP-only recent | 106 | 58.5 | +50.0 | +54.8 | $+1,673 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406
- KILL strategies (16): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-20T13:36:02.483164-04:00","date":"2026-08-20","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":156.1,"phases_s":{"reconcile":2.09,"cancel":0.02,"manage":144.79,"protective_stops":0.7},"signals":0,"placed":0,"equity":122196.11,"open_positions":9,"pending_orders":0,"open_lots":35,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"7655","github_run_id":"32398409431","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
17:35:59  INFO      Mode: exits
17:35:59  INFO        Daily log -> logs/daily/2026-08-20.md
17:35:59  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (3 ledger rows)
17:35:59  INFO        place_all_stops: checking 4 positions...
17:35:59  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
17:35:59  INFO        STOP skipped MNST: fractional (0.6350 shares) — software exit will handle it
17:36:00  INFO        [positions] 2/2 (2 valid)
17:36:00  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:35 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $428.23|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.0%  $+0.01                                           HOLD|
|  AON  P&L +0.4%  $+0.28                                            HOLD|
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
|  CL260821C00090000       $0.52    $0.40    -23.1%   $-12.00   $40.00   |
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
|                                                                        |
|  Options open P&L                                               $-19.00|
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
=== options_live_micro LIVE 2026-08-20T13:36:01.002874-04:00 share=50% ===
2026-08-20 13:36:01,002 INFO === options_live_micro LIVE 2026-08-20T13:36:01.002874-04:00 share=50% ===
Live account equity $428.23 cash $285.87 #225458845 options_level=3
2026-08-20 13:36:01,048 INFO Live account equity $428.23 cash $285.87 #225458845 options_level=3
Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
2026-08-20 13:36:01,068 INFO Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-20 13:36:01,092 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-20 13:36:01,106 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
... (183 earlier lines - see full log file)
| Window | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    2 |    1 |    6 |    1 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    21 |
| w2     |    5 |    4 |   10 |    4 |    5 |    4 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    41 |
| w3     |    5 |    4 |   11 |    3 |    5 |    3 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    42 |
| w4     |    4 |    2 |    8 |    2 |    3 |    3 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    31 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 205 | 6 |
| S164 | 229 | 7 |
| S165 | 1675 | 20 |
| S166 | 105 | 4 |
| S167 | 229 | 7 |
| S168 | 150 | 5 |
| S169 | 0 | 0 |
| S170 | 0 | 0 |
| S171 | 0 | 0 |
| S172 | 0 | 0 |
| S175 | 0 | 0 |
| S173 | 1911 | 17 |
| S174 | 891 | 7 |

### Raw log lines per day (debug / multi-bucket)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |    0 |   100 |
| 2026-07-08 |    0 |    0 |  100 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |  100 |   300 |
| 2026-07-09 |    0 |    0 |   24 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |   15 |   139 |
| 2026-07-10 |    0 |    0 |  242 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  230 |  202 |   674 |
| 2026-07-13 |    0 |    0 |  190 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  212 |  188 |   590 |
| 2026-07-14 |    0 |    0 |  194 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  185 |  106 |   485 |
| 2026-07-15 |    0 |    0 |  146 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  154 |   58 |   358 |
| 2026-07-16 |    0 |    0 |  179 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  205 |   58 |   442 |
| 2026-07-17 |    0 |    0 |  127 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  207 |   58 |   392 |
| 2026-07-20 |    0 |    0 |  107 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  143 |   58 |   308 |
| 2026-07-21 |   30 |   35 |  113 |   30 |   35 |   35 |    0 |    0 |    0 |    0 |    0 |  118 |   48 |   444 |
| 2026-07-22 |   40 |   47 |   86 |   15 |   45 |   20 |    0 |    0 |    0 |    0 |    0 |   77 |    0 |   330 |
| 2026-07-23 |   30 |   42 |   50 |   15 |   40 |   20 |    0 |    0 |    0 |    0 |    0 |   40 |    0 |   237 |
| 2026-07-24 |   75 |   87 |   85 |   15 |   77 |   55 |    0 |    0 |    0 |    0 |    0 |   40 |    0 |   434 |
| 2026-07-27 |   14 |    0 |   14 |   14 |   14 |   14 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    70 |
| 2026-07-28 |    6 |    8 |    8 |    8 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |
| 2026-07-29 |   10 |   10 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-08-20
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    35 | WARN | <<<
| Orphaned lots (post-stable) |   975 | WARN | <<<
| Missing exit records (post) |   945 | WARN | <<<
| State/ledger mismatches     |     5 | WARN | <<<
| Total open lots             |    35 | INFO |
| Total closed lots           |  1770 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-20_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-20_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=821 med=-47.5% | TAINTED n=1761 med=-39.3% | KEEP-only n=294 med=+37.5% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=428.23 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 3 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260820T174056Z

- UTC timestamp: `20260820T174056Z`
- GitHub run: [#7656](https://github.com/28twagg-ops/TradingBot/actions/runs/32398872869)
- Run id: `32398872869`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T174056Z_live_bot.log`, `logs/action_runs/20260820T174056Z_live_options.log`, `logs/action_runs/20260820T174056Z_options_bot.log`

### Live bot (tail)

```text
17:40:57  INFO      Mode: exits
17:40:58  INFO        Daily log -> logs/daily/2026-08-20.md
17:40:58  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (3 ledger rows)
17:40:58  INFO        place_all_stops: checking 4 positions...
17:40:58  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
17:40:58  INFO        STOP skipped MNST: fractional (0.6350 shares) — software exit will handle it
17:40:58  INFO        [positions] 2/2 (2 valid)
17:40:59  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:40 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $428.19|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L -0.0%  $-0.00                                           HOLD|
|  AON  P&L +0.4%  $+0.26                                            HOLD|
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
|  CL260821C00090000       $0.52    $0.40    -23.1%   $-12.00   $40.00   |
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
|                                                                        |
|  Options open P&L                                               $-19.00|
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
=== options_live_micro LIVE 2026-08-20T13:41:00.308847-04:00 share=50% ===
2026-08-20 13:41:00,308 INFO === options_live_micro LIVE 2026-08-20T13:41:00.308847-04:00 share=50% ===
Live account equity $428.19 cash $285.87 #225458845 options_level=3
2026-08-20 13:41:00,557 INFO Live account equity $428.19 cash $285.87 #225458845 options_level=3
Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
2026-08-20 13:41:00,699 INFO Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-20 13:41:00,851 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-20 13:41:00,921 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T175554Z

- UTC timestamp: `20260820T175554Z`
- GitHub run: [#7659](https://github.com/28twagg-ops/TradingBot/actions/runs/32400269044)
- Run id: `32400269044`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T175554Z_live_bot.log`, `logs/action_runs/20260820T175554Z_live_options.log`, `logs/action_runs/20260820T175554Z_options_bot.log`

### Live bot (tail)

```text
17:55:56  INFO      Mode: exits
17:55:56  INFO        Daily log -> logs/daily/2026-08-20.md
17:55:56  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (3 ledger rows)
17:55:56  INFO        place_all_stops: checking 4 positions...
17:55:56  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
17:55:56  INFO        STOP skipped MNST: fractional (0.6350 shares) — software exit will handle it
17:55:56  INFO        [positions] 2/2 (2 valid)
17:55:56  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:55 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $428.36|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L -0.1%  $-0.02                                           HOLD|
|  AON  P&L +0.6%  $+0.45                                            HOLD|
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
|  CL260821C00090000       $0.52    $0.40    -23.1%   $-12.00   $40.00   |
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
|                                                                        |
|  Options open P&L                                               $-19.00|
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
=== options_live_micro LIVE 2026-08-20T13:55:57.659166-04:00 share=50% ===
2026-08-20 13:55:57,659 INFO === options_live_micro LIVE 2026-08-20T13:55:57.659166-04:00 share=50% ===
Live account equity $428.36 cash $285.87 #225458845 options_level=3
2026-08-20 13:55:57,706 INFO Live account equity $428.36 cash $285.87 #225458845 options_level=3
Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
2026-08-20 13:55:57,728 INFO Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-20 13:55:57,753 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-20 13:55:57,765 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T180057Z

- UTC timestamp: `20260820T180057Z`
- GitHub run: [#7660](https://github.com/28twagg-ops/TradingBot/actions/runs/32400737660)
- Run id: `32400737660`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T180057Z_live_bot.log`, `logs/action_runs/20260820T180057Z_live_options.log`, `logs/action_runs/20260820T180057Z_options_bot.log`

### Live bot (tail)

```text
18:00:58  INFO      Mode: exits
18:01:00  INFO        Daily log -> logs/daily/2026-08-20.md
18:01:00  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (3 ledger rows)
18:01:00  INFO        place_all_stops: checking 4 positions...
18:01:00  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
18:01:00  INFO        STOP skipped MNST: fractional (0.6350 shares) — software exit will handle it
18:01:00  INFO        [positions] 2/2 (2 valid)
18:01:01  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:00 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $428.26|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L -0.1%  $-0.02                                           HOLD|
|  AON  P&L +0.5%  $+0.35                                            HOLD|
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
|  CL260821C00090000       $0.52    $0.40    -23.1%   $-12.00   $40.00   |
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
|                                                                        |
|  Options open P&L                                               $-19.00|
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
=== options_live_micro LIVE 2026-08-20T14:01:01.867738-04:00 share=50% ===
2026-08-20 14:01:01,867 INFO === options_live_micro LIVE 2026-08-20T14:01:01.867738-04:00 share=50% ===
Live account equity $428.25 cash $285.87 #225458845 options_level=3
2026-08-20 14:01:02,129 INFO Live account equity $428.25 cash $285.87 #225458845 options_level=3
Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
2026-08-20 14:01:02,307 INFO Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-20 14:01:02,460 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-20 14:01:02,535 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T180551Z

- UTC timestamp: `20260820T180551Z`
- GitHub run: [#7661](https://github.com/28twagg-ops/TradingBot/actions/runs/32401220361)
- Run id: `32401220361`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T180551Z_live_bot.log`, `logs/action_runs/20260820T180551Z_live_options.log`, `logs/action_runs/20260820T180551Z_options_bot.log`

### Live bot (tail)

```text
18:05:52  INFO      Mode: exits
18:05:52  INFO        Daily log -> logs/daily/2026-08-20.md
18:05:52  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (3 ledger rows)
18:05:52  INFO        place_all_stops: checking 4 positions...
18:05:52  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
18:05:52  INFO        STOP skipped MNST: fractional (0.6350 shares) — software exit will handle it
18:05:53  INFO        [positions] 2/2 (2 valid)
18:05:53  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:05 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $428.05|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L -0.5%  $-0.14                                           HOLD|
|  AON  P&L +0.4%  $+0.26                                            HOLD|
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
|  CL260821C00090000       $0.52    $0.40    -23.1%   $-12.00   $40.00   |
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
|                                                                        |
|  Options open P&L                                               $-19.00|
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
=== options_live_micro LIVE 2026-08-20T14:05:54.199754-04:00 share=50% ===
2026-08-20 14:05:54,199 INFO === options_live_micro LIVE 2026-08-20T14:05:54.199754-04:00 share=50% ===
Live account equity $428.05 cash $285.87 #225458845 options_level=3
2026-08-20 14:05:54,302 INFO Live account equity $428.05 cash $285.87 #225458845 options_level=3
Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
2026-08-20 14:05:54,357 INFO Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-20 14:05:54,412 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-20 14:05:54,441 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T181057Z

- UTC timestamp: `20260820T181057Z`
- GitHub run: [#7662](https://github.com/28twagg-ops/TradingBot/actions/runs/32401678753)
- Run id: `32401678753`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T181057Z_live_bot.log`, `logs/action_runs/20260820T181057Z_live_options.log`, `logs/action_runs/20260820T181057Z_options_bot.log`

### Live bot (tail)

```text
18:10:58  INFO      Mode: exits
18:11:00  INFO        Daily log -> logs/daily/2026-08-20.md
18:11:00  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (3 ledger rows)
18:11:00  INFO        place_all_stops: checking 4 positions...
18:11:00  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
18:11:00  INFO        STOP skipped MNST: fractional (0.6350 shares) — software exit will handle it
18:11:01  INFO        [positions] 2/2 (2 valid)
18:11:01  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $428.14|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L -0.2%  $-0.06                                           HOLD|
|  AON  P&L +0.4%  $+0.27                                            HOLD|
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
|  CL260821C00090000       $0.52    $0.40    -23.1%   $-12.00   $40.00   |
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
|                                                                        |
|  Options open P&L                                               $-19.00|
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
=== options_live_micro LIVE 2026-08-20T14:11:02.389771-04:00 share=50% ===
2026-08-20 14:11:02,389 INFO === options_live_micro LIVE 2026-08-20T14:11:02.389771-04:00 share=50% ===
Live account equity $428.14 cash $285.87 #225458845 options_level=3
2026-08-20 14:11:02,673 INFO Live account equity $428.14 cash $285.87 #225458845 options_level=3
Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
2026-08-20 14:11:02,820 INFO Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-20 14:11:02,966 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-20 14:11:03,037 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T181600Z

- UTC timestamp: `20260820T181600Z`
- GitHub run: [#7663](https://github.com/28twagg-ops/TradingBot/actions/runs/32402144387)
- Run id: `32402144387`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T181600Z_live_bot.log`, `logs/action_runs/20260820T181600Z_live_options.log`, `logs/action_runs/20260820T181600Z_options_bot.log`

### Live bot (tail)

```text
18:16:02  INFO      Mode: exits
18:16:02  INFO        Daily log -> logs/daily/2026-08-20.md
18:16:02  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (3 ledger rows)
18:16:03  INFO        place_all_stops: checking 4 positions...
18:16:03  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
18:16:03  INFO        STOP skipped MNST: fractional (0.6350 shares) — software exit will handle it
18:16:03  INFO        [positions] 2/2 (2 valid)
18:16:04  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $428.23|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L -0.1%  $-0.04                                           HOLD|
|  AON  P&L +0.5%  $+0.34                                            HOLD|
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
|  CL260821C00090000       $0.52    $0.40    -23.1%   $-12.00   $40.00   |
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
|                                                                        |
|  Options open P&L                                               $-19.00|
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
=== options_live_micro LIVE 2026-08-20T14:16:04.835413-04:00 share=50% ===
2026-08-20 14:16:04,835 INFO === options_live_micro LIVE 2026-08-20T14:16:04.835413-04:00 share=50% ===
Live account equity $428.23 cash $285.87 #225458845 options_level=3
2026-08-20 14:16:05,006 INFO Live account equity $428.23 cash $285.87 #225458845 options_level=3
Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
2026-08-20 14:16:05,099 INFO Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-20 14:16:05,179 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-20 14:16:05,219 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T182052Z

- UTC timestamp: `20260820T182052Z`
- GitHub run: [#7664](https://github.com/28twagg-ops/TradingBot/actions/runs/32402604974)
- Run id: `32402604974`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T182052Z_live_bot.log`, `logs/action_runs/20260820T182052Z_live_options.log`, `logs/action_runs/20260820T182052Z_options_bot.log`

### Live bot (tail)

```text
18:20:53  INFO      Mode: exits
18:20:54  INFO        Daily log -> logs/daily/2026-08-20.md
18:20:54  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (3 ledger rows)
18:20:54  INFO        place_all_stops: checking 4 positions...
18:20:54  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
18:20:54  INFO        STOP skipped MNST: fractional (0.6350 shares) — software exit will handle it
18:20:54  INFO        [positions] 2/2 (2 valid)
18:20:55  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $428.18|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L -0.3%  $-0.08                                           HOLD|
|  AON  P&L +0.5%  $+0.33                                            HOLD|
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
|  CL260821C00090000       $0.52    $0.40    -23.1%   $-12.00   $40.00   |
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
|                                                                        |
|  Options open P&L                                               $-19.00|
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
=== options_live_micro LIVE 2026-08-20T14:20:56.091950-04:00 share=50% ===
2026-08-20 14:20:56,092 INFO === options_live_micro LIVE 2026-08-20T14:20:56.091950-04:00 share=50% ===
Live account equity $428.18 cash $285.87 #225458845 options_level=3
2026-08-20 14:20:56,301 INFO Live account equity $428.18 cash $285.87 #225458845 options_level=3
Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
2026-08-20 14:20:56,427 INFO Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-20 14:20:56,544 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-20 14:20:56,606 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T182654Z

- UTC timestamp: `20260820T182654Z`
- GitHub run: [#7665](https://github.com/28twagg-ops/TradingBot/actions/runs/32403063382)
- Run id: `32403063382`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T182654Z_live_bot.log`, `logs/action_runs/20260820T182654Z_live_options.log`, `logs/action_runs/20260820T182654Z_options_bot.log`

### Live bot (tail)

```text
18:26:56  INFO      Mode: exits
18:26:56  INFO        Daily log -> logs/daily/2026-08-20.md
18:26:56  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (3 ledger rows)
18:26:56  INFO        place_all_stops: checking 4 positions...
18:26:56  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
18:26:56  INFO        STOP skipped MNST: fractional (0.6350 shares) — software exit will handle it
18:26:56  INFO        [positions] 2/2 (2 valid)
18:26:56  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $428.21|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L -0.1%  $-0.04                                           HOLD|
|  AON  P&L +0.5%  $+0.32                                            HOLD|
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
|  CL260821C00090000       $0.52    $0.40    -23.1%   $-12.00   $40.00   |
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
|                                                                        |
|  Options open P&L                                               $-19.00|
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
=== options_live_micro LIVE 2026-08-20T14:26:57.708421-04:00 share=50% ===
2026-08-20 14:26:57,708 INFO === options_live_micro LIVE 2026-08-20T14:26:57.708421-04:00 share=50% ===
Live account equity $428.21 cash $285.87 #225458845 options_level=3
2026-08-20 14:26:57,755 INFO Live account equity $428.21 cash $285.87 #225458845 options_level=3
Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
2026-08-20 14:26:57,777 INFO Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-20 14:26:57,795 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-20 14:26:57,812 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T183059Z

- UTC timestamp: `20260820T183059Z`
- GitHub run: [#7666](https://github.com/28twagg-ops/TradingBot/actions/runs/32403528510)
- Run id: `32403528510`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T183059Z_live_bot.log`, `logs/action_runs/20260820T183059Z_live_options.log`, `logs/action_runs/20260820T183059Z_options_bot.log`

### Live bot (tail)

```text
18:31:00  INFO      Mode: exits
18:31:02  INFO        Daily log -> logs/daily/2026-08-20.md
18:31:02  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (3 ledger rows)
18:31:02  INFO        place_all_stops: checking 4 positions...
18:31:02  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
18:31:02  INFO        STOP skipped MNST: fractional (0.6350 shares) — software exit will handle it
18:31:02  INFO        [positions] 2/2 (2 valid)
18:31:03  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $428.28|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L -0.1%  $-0.03                                           HOLD|
|  AON  P&L +0.5%  $+0.38                                            HOLD|
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
|  CL260821C00090000       $0.52    $0.40    -23.1%   $-12.00   $40.00   |
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
|                                                                        |
|  Options open P&L                                               $-19.00|
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
=== options_live_micro LIVE 2026-08-20T14:31:04.420775-04:00 share=50% ===
2026-08-20 14:31:04,420 INFO === options_live_micro LIVE 2026-08-20T14:31:04.420775-04:00 share=50% ===
Live account equity $428.29 cash $285.87 #225458845 options_level=3
2026-08-20 14:31:04,646 INFO Live account equity $428.29 cash $285.87 #225458845 options_level=3
Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
2026-08-20 14:31:04,796 INFO Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-20 14:31:04,942 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-20 14:31:05,011 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T183553Z

- UTC timestamp: `20260820T183553Z`
- GitHub run: [#7667](https://github.com/28twagg-ops/TradingBot/actions/runs/32403988409)
- Run id: `32403988409`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T183553Z_live_bot.log`, `logs/action_runs/20260820T183553Z_live_options.log`, `logs/action_runs/20260820T183553Z_options_bot.log`

### Live bot (tail)

```text
18:35:54  INFO      Mode: exits
18:35:55  INFO        Daily log -> logs/daily/2026-08-20.md
18:35:55  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (3 ledger rows)
18:35:55  INFO        place_all_stops: checking 4 positions...
18:35:55  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
18:35:55  INFO        STOP skipped MNST: fractional (0.6350 shares) — software exit will handle it
18:35:56  INFO        [positions] 2/2 (2 valid)
18:35:56  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:35 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $428.31|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.0%  $+0.00                                           HOLD|
|  AON  P&L +0.5%  $+0.38                                            HOLD|
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
|  CL260821C00090000       $0.52    $0.40    -23.1%   $-12.00   $40.00   |
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
|                                                                        |
|  Options open P&L                                               $-19.00|
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
=== options_live_micro LIVE 2026-08-20T14:35:57.750015-04:00 share=50% ===
2026-08-20 14:35:57,750 INFO === options_live_micro LIVE 2026-08-20T14:35:57.750015-04:00 share=50% ===
Live account equity $428.31 cash $285.87 #225458845 options_level=3
2026-08-20 14:35:57,979 INFO Live account equity $428.31 cash $285.87 #225458845 options_level=3
Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
2026-08-20 14:35:58,147 INFO Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-20 14:35:58,287 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-20 14:35:58,356 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T184051Z

- UTC timestamp: `20260820T184051Z`
- GitHub run: [#7668](https://github.com/28twagg-ops/TradingBot/actions/runs/32404441046)
- Run id: `32404441046`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T184051Z_live_bot.log`, `logs/action_runs/20260820T184051Z_live_options.log`, `logs/action_runs/20260820T184051Z_options_bot.log`

### Live bot (tail)

```text
18:40:52  INFO      Mode: exits
18:40:52  INFO        Daily log -> logs/daily/2026-08-20.md
18:40:52  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (3 ledger rows)
18:40:52  INFO        place_all_stops: checking 4 positions...
18:40:52  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
18:40:52  INFO        STOP skipped MNST: fractional (0.6350 shares) — software exit will handle it
18:40:53  INFO        [positions] 2/2 (2 valid)
18:40:53  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:40 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $428.38|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.1%  $+0.02                                           HOLD|
|  AON  P&L +0.6%  $+0.43                                            HOLD|
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
|  CL260821C00090000       $0.52    $0.40    -23.1%   $-12.00   $40.00   |
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
|                                                                        |
|  Options open P&L                                               $-19.00|
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
=== options_live_micro LIVE 2026-08-20T14:40:54.196609-04:00 share=50% ===
2026-08-20 14:40:54,196 INFO === options_live_micro LIVE 2026-08-20T14:40:54.196609-04:00 share=50% ===
Live account equity $428.38 cash $285.87 #225458845 options_level=3
2026-08-20 14:40:54,289 INFO Live account equity $428.38 cash $285.87 #225458845 options_level=3
Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
2026-08-20 14:40:54,341 INFO Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-20 14:40:54,395 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-20 14:40:54,419 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T184602Z

- UTC timestamp: `20260820T184602Z`
- GitHub run: [#7669](https://github.com/28twagg-ops/TradingBot/actions/runs/32404894590)
- Run id: `32404894590`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T184602Z_live_bot.log`, `logs/action_runs/20260820T184602Z_live_options.log`, `logs/action_runs/20260820T184602Z_options_bot.log`

### Live bot (tail)

```text
18:46:03  INFO      Mode: exits
18:46:03  INFO        Daily log -> logs/daily/2026-08-20.md
18:46:03  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (3 ledger rows)
18:46:04  INFO        place_all_stops: checking 4 positions...
18:46:04  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
18:46:04  INFO        STOP skipped MNST: fractional (0.6350 shares) — software exit will handle it
18:46:04  INFO        [positions] 2/2 (2 valid)
18:46:05  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $428.45|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L -0.0%  $-0.01                                           HOLD|
|  AON  P&L +0.8%  $+0.54                                            HOLD|
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
|  CL260821C00090000       $0.52    $0.40    -23.1%   $-12.00   $40.00   |
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
|                                                                        |
|  Options open P&L                                               $-19.00|
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
=== options_live_micro LIVE 2026-08-20T14:46:05.855162-04:00 share=50% ===
2026-08-20 14:46:05,855 INFO === options_live_micro LIVE 2026-08-20T14:46:05.855162-04:00 share=50% ===
Live account equity $428.46 cash $285.87 #225458845 options_level=3
2026-08-20 14:46:06,094 INFO Live account equity $428.46 cash $285.87 #225458845 options_level=3
Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
2026-08-20 14:46:06,252 INFO Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-20 14:46:06,375 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-20 14:46:06,433 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T185052Z

- UTC timestamp: `20260820T185052Z`
- GitHub run: [#7670](https://github.com/28twagg-ops/TradingBot/actions/runs/32405349590)
- Run id: `32405349590`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T185052Z_live_bot.log`, `logs/action_runs/20260820T185052Z_live_options.log`, `logs/action_runs/20260820T185052Z_options_bot.log`

### Live bot (tail)

```text
18:50:53  INFO      Mode: exits
18:50:54  INFO        Daily log -> logs/daily/2026-08-20.md
18:50:54  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (3 ledger rows)
18:50:54  INFO        place_all_stops: checking 4 positions...
18:50:54  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
18:50:54  INFO        STOP skipped MNST: fractional (0.6350 shares) — software exit will handle it
18:50:55  INFO        [positions] 2/2 (2 valid)
18:50:56  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:50 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $428.52|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.1%  $+0.02                                           HOLD|
|  AON  P&L +0.8%  $+0.56                                            HOLD|
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
|  CL260821C00090000       $0.52    $0.40    -23.1%   $-12.00   $40.00   |
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
|                                                                        |
|  Options open P&L                                               $-19.00|
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
=== options_live_micro LIVE 2026-08-20T14:50:56.952194-04:00 share=50% ===
2026-08-20 14:50:56,952 INFO === options_live_micro LIVE 2026-08-20T14:50:56.952194-04:00 share=50% ===
Live account equity $428.52 cash $285.87 #225458845 options_level=3
2026-08-20 14:50:57,214 INFO Live account equity $428.52 cash $285.87 #225458845 options_level=3
Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
2026-08-20 14:50:57,363 INFO Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-20 14:50:57,515 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-20 14:50:57,591 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T185555Z

- UTC timestamp: `20260820T185555Z`
- GitHub run: [#7671](https://github.com/28twagg-ops/TradingBot/actions/runs/32405810695)
- Run id: `32405810695`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T185555Z_live_bot.log`, `logs/action_runs/20260820T185555Z_live_options.log`, `logs/action_runs/20260820T185555Z_options_bot.log`

### Live bot (tail)

```text
18:55:57  INFO      Mode: exits
18:55:58  INFO        Daily log -> logs/daily/2026-08-20.md
18:55:58  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (3 ledger rows)
18:55:58  INFO        place_all_stops: checking 4 positions...
18:55:58  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
18:55:58  INFO        STOP skipped MNST: fractional (0.6350 shares) — software exit will handle it
18:55:59  INFO        [positions] 2/2 (2 valid)
18:55:59  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:55 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $428.42|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.0%  $+0.01                                           HOLD|
|  AON  P&L +0.7%  $+0.48                                            HOLD|
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
|  CL260821C00090000       $0.52    $0.40    -23.1%   $-12.00   $40.00   |
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
|                                                                        |
|  Options open P&L                                               $-19.00|
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
=== options_live_micro LIVE 2026-08-20T14:56:00.554894-04:00 share=50% ===
2026-08-20 14:56:00,554 INFO === options_live_micro LIVE 2026-08-20T14:56:00.554894-04:00 share=50% ===
Live account equity $428.42 cash $285.87 #225458845 options_level=3
2026-08-20 14:56:00,791 INFO Live account equity $428.42 cash $285.87 #225458845 options_level=3
Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
2026-08-20 14:56:00,952 INFO Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-20 14:56:01,105 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-20 14:56:01,213 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T190104Z

- UTC timestamp: `20260820T190104Z`
- GitHub run: [#7672](https://github.com/28twagg-ops/TradingBot/actions/runs/32406269302)
- Run id: `32406269302`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T190104Z_live_bot.log`, `logs/action_runs/20260820T190104Z_live_options.log`, `logs/action_runs/20260820T190104Z_options_bot.log`

### Live bot (tail)

```text
19:01:05  INFO      Mode: exits
19:01:06  INFO        Daily log -> logs/daily/2026-08-20.md
19:01:06  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (3 ledger rows)
19:01:06  INFO        place_all_stops: checking 4 positions...
19:01:06  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
19:01:06  INFO        STOP skipped MNST: fractional (0.6350 shares) — software exit will handle it
19:01:07  INFO        [positions] 2/2 (2 valid)
19:01:07  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         19:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $428.36|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.1%  $+0.04                                           HOLD|
|  AON  P&L +0.6%  $+0.39                                            HOLD|
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
|  CL260821C00090000       $0.52    $0.40    -23.1%   $-12.00   $40.00   |
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
|                                                                        |
|  Options open P&L                                               $-19.00|
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
=== options_live_micro LIVE 2026-08-20T15:01:08.479002-04:00 share=50% ===
2026-08-20 15:01:08,479 INFO === options_live_micro LIVE 2026-08-20T15:01:08.479002-04:00 share=50% ===
Live account equity $428.36 cash $285.87 #225458845 options_level=3
2026-08-20 15:01:08,605 INFO Live account equity $428.36 cash $285.87 #225458845 options_level=3
Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
2026-08-20 15:01:08,687 INFO Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-20 15:01:08,749 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-20 15:01:08,777 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T190550Z

- UTC timestamp: `20260820T190550Z`
- GitHub run: [#7673](https://github.com/28twagg-ops/TradingBot/actions/runs/32406735454)
- Run id: `32406735454`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T190550Z_live_bot.log`, `logs/action_runs/20260820T190550Z_live_options.log`, `logs/action_runs/20260820T190550Z_options_bot.log`

### Live bot (tail)

```text
19:05:51  INFO      Mode: exits
19:05:51  INFO        Daily log -> logs/daily/2026-08-20.md
19:05:51  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (3 ledger rows)
19:05:52  INFO        place_all_stops: checking 4 positions...
19:05:52  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
19:05:52  INFO        STOP skipped MNST: fractional (0.6350 shares) — software exit will handle it
19:05:52  INFO        [positions] 2/2 (2 valid)
19:05:53  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         19:05 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $428.37|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.2%  $+0.06                                           HOLD|
|  AON  P&L +0.5%  $+0.37                                            HOLD|
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
|  CL260821C00090000       $0.52    $0.40    -23.1%   $-12.00   $40.00   |
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
|                                                                        |
|  Options open P&L                                               $-19.00|
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
=== options_live_micro LIVE 2026-08-20T15:05:53.872166-04:00 share=50% ===
2026-08-20 15:05:53,872 INFO === options_live_micro LIVE 2026-08-20T15:05:53.872166-04:00 share=50% ===
Live account equity $428.37 cash $285.87 #225458845 options_level=3
2026-08-20 15:05:54,037 INFO Live account equity $428.37 cash $285.87 #225458845 options_level=3
Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
2026-08-20 15:05:54,133 INFO Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-20 15:05:54,231 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-20 15:05:54,280 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T191048Z

- UTC timestamp: `20260820T191048Z`
- GitHub run: [#7674](https://github.com/28twagg-ops/TradingBot/actions/runs/32407188729)
- Run id: `32407188729`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T191048Z_live_bot.log`, `logs/action_runs/20260820T191048Z_live_options.log`, `logs/action_runs/20260820T191048Z_options_bot.log`

### Live bot (tail)

```text
19:10:49  INFO      Mode: exits
19:10:50  INFO        Daily log -> logs/daily/2026-08-20.md
19:10:50  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (3 ledger rows)
19:10:50  INFO        place_all_stops: checking 4 positions...
19:10:50  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
19:10:50  INFO        STOP skipped MNST: fractional (0.6350 shares) — software exit will handle it
19:10:50  INFO        [positions] 2/2 (2 valid)
19:10:50  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         19:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $428.39|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AON  P&L +0.4%  $+0.29                                            HOLD|
|  MNST  P&L +0.6%  $+0.17                                           HOLD|
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
|  CL260821C00090000       $0.52    $0.40    -23.1%   $-12.00   $40.00   |
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
|                                                                        |
|  Options open P&L                                               $-19.00|
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
=== options_live_micro LIVE 2026-08-20T15:10:51.659257-04:00 share=50% ===
2026-08-20 15:10:51,659 INFO === options_live_micro LIVE 2026-08-20T15:10:51.659257-04:00 share=50% ===
Live account equity $428.39 cash $285.87 #225458845 options_level=3
2026-08-20 15:10:51,708 INFO Live account equity $428.39 cash $285.87 #225458845 options_level=3
Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
2026-08-20 15:10:51,749 INFO Live micro hold S218 CL260821C00090000 -23.1% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-20 15:10:51,790 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-20 15:10:51,814 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T192148Z

- UTC timestamp: `20260820T192148Z`
- GitHub run: [#7676](https://github.com/28twagg-ops/TradingBot/actions/runs/32408093569)
- Run id: `32408093569`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T192148Z_live_bot.log`, `logs/action_runs/20260820T192148Z_live_options.log`, `logs/action_runs/20260820T192148Z_options_bot.log`

### Live bot (tail)

```text
19:21:49  INFO      Mode: exits
19:21:50  INFO        Daily log -> logs/daily/2026-08-20.md
19:21:50  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (3 ledger rows)
19:21:50  INFO        place_all_stops: checking 4 positions...
19:21:50  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
19:21:50  INFO        STOP skipped MNST: fractional (0.6350 shares) — software exit will handle it
19:21:51  INFO        [positions] 2/2 (2 valid)
19:21:51  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         19:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $408.51|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AON  P&L +0.5%  $+0.37                                            HOLD|
|  MNST  P&L +0.7%  $+0.21                                           HOLD|
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
|  CL260821C00090000       $0.52    $0.20    -61.5%   $-32.00   $20.00   |
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
|                                                                        |
|  Options open P&L                                               $-39.00|
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
=== options_live_micro LIVE 2026-08-20T15:21:52.128480-04:00 share=50% ===
2026-08-20 15:21:52,128 INFO === options_live_micro LIVE 2026-08-20T15:21:52.128480-04:00 share=50% ===
Live account equity $408.52 cash $285.87 #225458845 options_level=3
2026-08-20 15:21:52,368 INFO Live account equity $408.52 cash $285.87 #225458845 options_level=3
LIVE EXIT stop_loss (-61.5%) CL260821C00090000 x1 limit=0.21 id=84851455-0853-4fcb-869d-28a9fd16be44
2026-08-20 15:21:53,130 INFO LIVE EXIT stop_loss (-61.5%) CL260821C00090000 x1 limit=0.21 id=84851455-0853-4fcb-869d-28a9fd16be44
Live micro: manage/exits only
2026-08-20 15:21:53,193 INFO Live micro: manage/exits only
Live micro done. open_options=1 lots=0
2026-08-20 15:21:53,253 INFO Live micro done. open_options=1 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T192556Z

- UTC timestamp: `20260820T192556Z`
- GitHub run: [#7677](https://github.com/28twagg-ops/TradingBot/actions/runs/32408544954)
- Run id: `32408544954`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T192556Z_live_bot.log`, `logs/action_runs/20260820T192556Z_live_options.log`, `logs/action_runs/20260820T192556Z_options_bot.log`

### Live bot (tail)

```text
19:25:57  INFO      Mode: exits
19:25:58  INFO        Daily log -> logs/daily/2026-08-20.md
19:25:58  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (3 ledger rows)
19:25:58  INFO        place_all_stops: checking 3 positions...
19:25:58  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
19:25:58  INFO        STOP skipped MNST: fractional (0.6350 shares) — software exit will handle it
19:25:58  INFO        [positions] 2/2 (2 valid)
19:25:59  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         19:25 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $413.41|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AON  P&L +0.4%  $+0.31                                            HOLD|
|  MNST  P&L +0.7%  $+0.20                                           HOLD|
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
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
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
=== options_live_micro LIVE 2026-08-20T15:26:00.007522-04:00 share=50% ===
2026-08-20 15:26:00,007 INFO === options_live_micro LIVE 2026-08-20T15:26:00.007522-04:00 share=50% ===
Live account equity $413.41 cash $310.83 #225458845 options_level=3
2026-08-20 15:26:00,195 INFO Live account equity $413.41 cash $310.83 #225458845 options_level=3
Live micro: manage/exits only
2026-08-20 15:26:00,436 INFO Live micro: manage/exits only
Live micro done. open_options=1 lots=0
2026-08-20 15:26:00,493 INFO Live micro done. open_options=1 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T193051Z

- UTC timestamp: `20260820T193051Z`
- GitHub run: [#7678](https://github.com/28twagg-ops/TradingBot/actions/runs/32408993392)
- Run id: `32408993392`
- Live bot: exit=`0`, duration=`218s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T193051Z_live_bot.log`, `logs/action_runs/20260820T193051Z_live_options.log`, `logs/action_runs/20260820T193051Z_options_bot.log`

### Live bot (tail)

```text
19:30:53  INFO      Mode: evening_prep
19:30:55  INFO        [prep_positions] 2/2 (2 valid)
19:30:55  INFO        Universe cache hit: 903 tickers (tickers_2026-08-20.json)
19:30:57  INFO        [prep_universe] 40/901 (40 valid)
19:30:59  INFO        [prep_universe] 80/901 (80 valid)
19:31:01  INFO        [prep_universe] 120/901 (120 valid)
19:31:03  INFO        [prep_universe] 160/901 (160 valid)
19:31:05  INFO        [prep_universe] 200/901 (199 valid)
19:31:08  INFO        [prep_universe] 240/901 (238 valid)
19:31:21  INFO        [prep_universe] 280/901 (278 valid)
19:31:32  INFO        [prep_universe] 320/901 (318 valid)
19:31:46  INFO        [prep_universe] 360/901 (358 valid)
19:31:57  INFO        [prep_universe] 400/901 (397 valid)
19:32:08  INFO        [prep_universe] 440/901 (437 valid)
19:32:22  INFO        [prep_universe] 480/901 (477 valid)
19:32:33  INFO        [prep_universe] 520/901 (517 valid)
19:32:44  INFO        [prep_universe] 560/901 (557 valid)
19:32:56  INFO        [prep_universe] 600/901 (597 valid)
19:33:09  INFO        [prep_universe] 640/901 (637 valid)
19:33:20  INFO        [prep_universe] 680/901 (677 valid)
19:33:33  INFO        [prep_universe] 720/901 (717 valid)
19:33:44  INFO        [prep_universe] 760/901 (757 valid)
19:33:55  INFO        [prep_universe] 800/901 (797 valid)
19:34:09  INFO        [prep_universe] 840/901 (836 valid)
19:34:19  INFO        [prep_universe] 880/901 (876 valid)
19:34:26  INFO        [prep_universe] 901/901 (897 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      EVENING_PREP|
|  Time                                                         19:30 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $413.53|
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
|  Invested                                                       $100.70|
|  Open P&L                                                        $+0.64|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AON      Pullback50      $70.38     $350.82  $352.90  +0.6%   $+0.42  |
|  MNST     MomReversal     $30.32     $47.41   $47.76   +0.7%   $+0.22  |
+========================================================================+

+========================================================================+
|                            OPEN SELL ORDERS                            |
+========================================================================+
|  Count                                                                1|
|  TICKER    TYPE              QTY       LIMIT       STOP                |
+------------------------------------------------------------------------+
|  WMT2608~  OrderType.LIMIT   1         0.04        None                |
+========================================================================+

+========================================================================+
|                              PREP SUMMARY                              |
+========================================================================+
|  Saved                                                              yes|
|  Exit candidates                                                      0|
|  Signal candidates                                                   39|
|  Universe scanned                                                   901|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-20T15:34:30.066523-04:00 share=50% ===
2026-08-20 15:34:30,066 INFO === options_live_micro LIVE 2026-08-20T15:34:30.066523-04:00 share=50% ===
Live account equity $413.49 cash $310.83 #225458845 options_level=3
2026-08-20 15:34:30,293 INFO Live account equity $413.49 cash $310.83 #225458845 options_level=3
Live micro: manage/exits only
2026-08-20 15:34:30,535 INFO Live micro: manage/exits only
Live micro done. open_options=1 lots=0
2026-08-20 15:34:30,607 INFO Live micro done. open_options=1 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T194137Z

- UTC timestamp: `20260820T194137Z`
- GitHub run: [#7680](https://github.com/28twagg-ops/TradingBot/actions/runs/32409904561)
- Run id: `32409904561`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T194137Z_live_bot.log`, `logs/action_runs/20260820T194137Z_live_options.log`, `logs/action_runs/20260820T194137Z_options_bot.log`

### Live bot (tail)

```text
19:41:38  INFO      Mode: evening_prep
19:41:39  INFO        [prep_positions] 2/2 (2 valid)
19:41:39  INFO        Universe cache hit: 903 tickers (tickers_2026-08-20.json)
19:41:40  INFO        [prep_universe] 40/901 (40 valid)
19:41:41  INFO        [prep_universe] 80/901 (80 valid)
19:41:43  INFO        [prep_universe] 120/901 (120 valid)
19:41:44  INFO        [prep_universe] 160/901 (160 valid)
19:41:45  INFO        [prep_universe] 200/901 (199 valid)
19:41:52  INFO        [prep_universe] 240/901 (238 valid)
19:42:05  INFO        [prep_universe] 280/901 (278 valid)
19:42:16  INFO        [prep_universe] 320/901 (318 valid)
19:42:29  INFO        [prep_universe] 360/901 (358 valid)
19:42:39  INFO        [prep_universe] 400/901 (397 valid)
19:42:52  INFO        [prep_universe] 440/901 (437 valid)
19:43:06  INFO        [prep_universe] 480/901 (477 valid)
19:43:16  INFO        [prep_universe] 520/901 (517 valid)
19:43:29  INFO        [prep_universe] 560/901 (557 valid)
19:43:42  INFO        [prep_universe] 600/901 (597 valid)
19:43:52  INFO        [prep_universe] 640/901 (637 valid)
19:44:05  INFO        [prep_universe] 680/901 (677 valid)
19:44:15  INFO        [prep_universe] 720/901 (717 valid)
19:44:28  INFO        [prep_universe] 760/901 (757 valid)
19:44:41  INFO        [prep_universe] 800/901 (797 valid)
19:44:51  INFO        [prep_universe] 840/901 (836 valid)
19:45:05  INFO        [prep_universe] 880/901 (876 valid)
19:45:12  INFO        [prep_universe] 901/901 (897 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      EVENING_PREP|
|  Time                                                         19:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $413.46|
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
|  Invested                                                       $100.63|
|  Open P&L                                                        $+0.57|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AON      Pullback50      $70.34     $350.82  $352.74  +0.5%   $+0.38  |
|  MNST     MomReversal     $30.29     $47.41   $47.70   +0.6%   $+0.19  |
+========================================================================+

+========================================================================+
|                            OPEN SELL ORDERS                            |
+========================================================================+
|  Count                                                                1|
|  TICKER    TYPE              QTY       LIMIT       STOP                |
+------------------------------------------------------------------------+
|  WMT2608~  OrderType.LIMIT   1         0.04        None                |
+========================================================================+

+========================================================================+
|                              PREP SUMMARY                              |
+========================================================================+
|  Saved                                                              yes|
|  Exit candidates                                                      0|
|  Signal candidates                                                   33|
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

## Run 20260820T194617Z

- UTC timestamp: `20260820T194617Z`
- GitHub run: [#7681](https://github.com/28twagg-ops/TradingBot/actions/runs/32410352331)
- Run id: `32410352331`
- Live bot: exit=`0`, duration=`231s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T194617Z_live_bot.log`, `logs/action_runs/20260820T194617Z_live_options.log`, `logs/action_runs/20260820T194617Z_options_bot.log`

### Live bot (tail)

```text
... (162 earlier lines - see full log file)
|  NWE      Pullback50      eq     $70.83   61.6   -1.93   50MA bounce (-|
|  ORI      Pullback50      eq     $41.92   27.2   -2.23   50MA bounce (+|
|  PB       Pullback50      eq     $72.74   33.1   -1.30   50MA bounce (-|
|  PNFP     Pullback50      eq     $101.65  40.1   -1.48   50MA bounce (+|
|  VNO      Pullback50      eq     $38.67   45.7   -1.04   50MA bounce (-|
|                                                                        |
+========================================================================+

+========================================================================+
|                              ENTRY ORDERS                              |
+========================================================================+
|    ENTER [eq] AES  Pullback50                                    $62.02|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    SKIP [eq] ACGL  Pullback50                                     cap 3|
|    SKIP [eq] BXP  Pullback50                                      cap 3|
|    SKIP [eq] CB  Pullback50                                       cap 3|
|    SKIP [eq] ELV  Pullback50                                      cap 3|
|    SKIP [eq] ESS  Pullback50                                      cap 3|
|    SKIP [eq] ES  Pullback50                                       cap 3|
|    SKIP [eq] EXR  Pullback50                                      cap 3|
|    SKIP [eq] DOC  Pullback50                                      cap 3|
|    SKIP [eq] HIG  Pullback50                                      cap 3|
|    SKIP [eq] HUM  Pullback50                                      cap 3|
|    SKIP [eq] MU  Pullback50                                       cap 3|
|    SKIP [eq] O  Pullback50                                        cap 3|
|    SKIP [eq] PHM  Pullback50                                      cap 3|
|    SKIP [eq] TTWO  Pullback50                                     cap 3|
|    SKIP [eq] TER  Pullback50                                      cap 3|
|    SKIP [eq] ALV  Pullback50                                      cap 3|
|    SKIP [eq] ASB  Pullback50                                      cap 3|
|    SKIP [eq] BC  Pullback50                                       cap 3|
|    SKIP [eq] BKH  Pullback50                                      cap 3|
|    SKIP [eq] CAVA  Pullback50                                     cap 3|
|    SKIP [eq] CBSH  Pullback50                                     cap 3|
|    SKIP [eq] CHH  Pullback50                                      cap 3|
|    SKIP [eq] HIMS  Pullback50                                     cap 3|
|    SKIP [eq] IRT  Pullback50                                      cap 3|
|    SKIP [eq] IESC  Pullback50                                     cap 3|
|    SKIP [eq] KEX  Pullback50                                      cap 3|
|    SKIP [eq] NWE  Pullback50                                      cap 3|
|    SKIP [eq] ORI  Pullback50                                      cap 3|
|    SKIP [eq] PB  Pullback50                                       cap 3|
|    SKIP [eq] PNFP  Pullback50                                     cap 3|
|    SKIP [eq] VNO  Pullback50                                      cap 3|
|    SKIP [eq] DE  VWAP_Reclaim                                     cap 3|
|    SKIP [eq] LOW  VWAP_Reclaim                                    cap 3|
|    SKIP [eq] NDSN  VWAP_Reclaim                                   cap 3|
|    SKIP [eq] PCG  VWAP_Reclaim                                    cap 3|
|    SKIP [eq] CNH  VWAP_Reclaim                                    cap 3|

+========================================================================+
|                         BUY FILL CONFIRMATION                          |
+========================================================================+
|  Pending submits                                                      1|
+------------------------------------------------------------------------+
|  AES                                                  still unconfirmed|
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
|  Signals                                                             37|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  1 unconfirmed|
|  Exits                                                                0|
|  Open pos                                                             3|
|  Equity                                                         $413.36|
|  Cash                                                           $248.82|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-20T15:50:09.607340-04:00 share=50% ===
2026-08-20 15:50:09,607 INFO === options_live_micro LIVE 2026-08-20T15:50:09.607340-04:00 share=50% ===
Live account equity $413.36 cash $248.82 #225458845 options_level=3
2026-08-20 15:50:09,667 INFO Live account equity $413.36 cash $248.82 #225458845 options_level=3
Live micro: manage/exits only
2026-08-20 15:50:09,719 INFO Live micro: manage/exits only
Live micro done. open_options=1 lots=0
2026-08-20 15:50:09,762 INFO Live micro done. open_options=1 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T195115Z

- UTC timestamp: `20260820T195115Z`
- GitHub run: [#7682](https://github.com/28twagg-ops/TradingBot/actions/runs/32410802597)
- Run id: `32410802597`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T195115Z_live_bot.log`, `logs/action_runs/20260820T195115Z_live_options.log`, `logs/action_runs/20260820T195115Z_options_bot.log`

### Live bot (tail)

```text
19:51:16  INFO      Mode: scan
19:51:17  INFO        [positions] 3/3 (3 valid)
19:51:18  INFO        SELL LIMIT AES  qty=4.199458178  limit=$14.76  id=2a979c4b-64c4-4118-ac6e-140ad85881b0
19:51:48  INFO        SELL LIMIT filled AES (confirmed by position check)
19:51:48  INFO        TX logged: SELL AES  P&L 0.0%
19:51:48  INFO        Universe cache hit: 903 tickers (tickers_2026-08-20.json)
19:51:49  INFO        [universe] 40/901 (40 valid)
19:51:51  INFO        [universe] 80/901 (80 valid)
19:51:53  INFO        [universe] 120/901 (120 valid)
19:51:54  INFO        [universe] 160/901 (160 valid)
19:51:55  INFO        [universe] 200/901 (199 valid)
19:52:03  INFO        [universe] 240/901 (238 valid)
19:52:14  INFO        [universe] 280/901 (278 valid)
19:52:24  INFO        [universe] 320/901 (318 valid)
19:52:38  INFO        [universe] 360/901 (358 valid)
19:52:49  INFO        [universe] 400/901 (397 valid)
19:53:03  INFO        [universe] 440/901 (437 valid)
19:53:14  INFO        [universe] 480/901 (477 valid)
19:53:27  INFO        [universe] 520/901 (517 valid)
19:53:38  INFO        [universe] 560/901 (557 valid)
19:53:51  INFO        [universe] 600/901 (597 valid)
19:54:02  INFO        [universe] 640/901 (637 valid)
19:54:15  INFO        [universe] 680/901 (677 valid)
19:54:26  INFO        [universe] 720/901 (717 valid)
19:54:39  INFO        [universe] 760/901 (757 valid)
19:54:50  INFO        [universe] 800/901 (797 valid)
19:55:03  INFO        [universe] 840/901 (836 valid)
19:55:14  INFO        [universe] 880/901 (876 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T195623Z

- UTC timestamp: `20260820T195623Z`
- GitHub run: [#7683](https://github.com/28twagg-ops/TradingBot/actions/runs/32411253279)
- Run id: `32411253279`
- Live bot: exit=`0`, duration=`232s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T195623Z_live_bot.log`, `logs/action_runs/20260820T195623Z_live_options.log`, `logs/action_runs/20260820T195623Z_options_bot.log`

### Live bot (tail)

```text
... (156 earlier lines - see full log file)
|  NWE      Pullback50      eq     $70.81   61.4   -1.78   50MA bounce (-|
|  ORI      Pullback50      eq     $41.86   26.0   -1.98   50MA bounce (+|
|  PB       Pullback50      eq     $72.83   33.6   -1.06   50MA bounce (-|
|  PNFP     Pullback50      eq     $101.70  40.3   -1.36   50MA bounce (+|
|  VNO      Pullback50      eq     $38.72   46.1   -0.94   50MA bounce (-|
|                                                                        |
+========================================================================+

+========================================================================+
|                              ENTRY ORDERS                              |
+========================================================================+
|    ENTER [eq] AES  Pullback50                                    $61.98|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    SKIP [eq] BXP  Pullback50                                      cap 3|
|    SKIP [eq] CB  Pullback50                                       cap 3|
|    SKIP [eq] ELV  Pullback50                                      cap 3|
|    SKIP [eq] ESS  Pullback50                                      cap 3|
|    SKIP [eq] ES  Pullback50                                       cap 3|
|    SKIP [eq] EXR  Pullback50                                      cap 3|
|    SKIP [eq] HIG  Pullback50                                      cap 3|
|    SKIP [eq] DOC  Pullback50                                      cap 3|
|    SKIP [eq] HUM  Pullback50                                      cap 3|
|    SKIP [eq] MU  Pullback50                                       cap 3|
|    SKIP [eq] PHM  Pullback50                                      cap 3|
|    SKIP [eq] O  Pullback50                                        cap 3|
|    SKIP [eq] TTWO  Pullback50                                     cap 3|
|    SKIP [eq] TER  Pullback50                                      cap 3|
|    SKIP [eq] ALV  Pullback50                                      cap 3|
|    SKIP [eq] ASB  Pullback50                                      cap 3|
|    SKIP [eq] BC  Pullback50                                       cap 3|
|    SKIP [eq] BKH  Pullback50                                      cap 3|
|    SKIP [eq] CAVA  Pullback50                                     cap 3|
|    SKIP [eq] CHH  Pullback50                                      cap 3|
|    SKIP [eq] CNO  Pullback50                                      cap 3|
|    SKIP [eq] CXT  Pullback50                                      cap 3|
|    SKIP [eq] FFIN  Pullback50                                     cap 3|
|    SKIP [eq] HIMS  Pullback50                                     cap 3|
|    SKIP [eq] IRT  Pullback50                                      cap 3|
|    SKIP [eq] KEX  Pullback50                                      cap 3|
|    SKIP [eq] NWE  Pullback50                                      cap 3|
|    SKIP [eq] ORI  Pullback50                                      cap 3|
|    SKIP [eq] PB  Pullback50                                       cap 3|
|    SKIP [eq] PNFP  Pullback50                                     cap 3|
|    SKIP [eq] VNO  Pullback50                                      cap 3|
|    SKIP [eq] DE  VWAP_Reclaim                                     cap 3|
|    SKIP [eq] LOW  VWAP_Reclaim                                    cap 3|
|    SKIP [eq] NDSN  VWAP_Reclaim                                   cap 3|
|    SKIP [eq] PCG  VWAP_Reclaim                                    cap 3|
|    SKIP [eq] CNH  VWAP_Reclaim                                    cap 3|

+========================================================================+
|                         BUY FILL CONFIRMATION                          |
+========================================================================+
|  Pending submits                                                      1|
+------------------------------------------------------------------------+
|  AES                                                  still unconfirmed|
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
|  Signals                                                             37|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  1 unconfirmed|
|  Exits                                                                0|
|  Open pos                                                             2|
|  Equity                                                         $413.16|
|  Cash                                                           $310.82|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-20T16:00:15.868426-04:00 share=50% ===
2026-08-20 16:00:15,868 INFO === options_live_micro LIVE 2026-08-20T16:00:15.868426-04:00 share=50% ===
Live account equity $413.16 cash $310.82 #225458845 options_level=3
2026-08-20 16:00:16,067 INFO Live account equity $413.16 cash $310.82 #225458845 options_level=3
Live micro: manage/exits only
2026-08-20 16:00:16,237 INFO Live micro: manage/exits only
Live micro done. open_options=1 lots=0
2026-08-20 16:00:16,292 INFO Live micro done. open_options=1 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T200120Z

- UTC timestamp: `20260820T200120Z`
- GitHub run: [#7684](https://github.com/28twagg-ops/TradingBot/actions/runs/32411699820)
- Run id: `32411699820`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T200120Z_live_bot.log`, `logs/action_runs/20260820T200120Z_live_options.log`, `logs/action_runs/20260820T200120Z_options_bot.log`

### Live bot (tail)

```text
20:01:21  INFO      Mode: ext_exits
20:01:21  INFO        Daily log -> logs/daily/2026-08-20.md
20:01:21  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (4 ledger rows)
20:01:21  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         20:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $413.16|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.2%  $+0.05        HOLDING until 9:35am scan (MomReversal)|
|  AON  P&L +0.3%  $+0.22          HOLDING until 9:35am scan (Pullback50)|
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
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
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
=== options_live_micro LIVE 2026-08-20T16:01:22.521506-04:00 share=50% ===
2026-08-20 16:01:22,521 INFO === options_live_micro LIVE 2026-08-20T16:01:22.521506-04:00 share=50% ===
Live account equity $413.16 cash $310.82 #225458845 options_level=3
2026-08-20 16:01:22,601 INFO Live account equity $413.16 cash $310.82 #225458845 options_level=3
Live micro: manage/exits only
2026-08-20 16:01:22,645 INFO Live micro: manage/exits only
Live micro done. open_options=1 lots=0
2026-08-20 16:01:22,691 INFO Live micro done. open_options=1 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T200554Z

- UTC timestamp: `20260820T200554Z`
- GitHub run: [#7685](https://github.com/28twagg-ops/TradingBot/actions/runs/32412155872)
- Run id: `32412155872`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T200554Z_live_bot.log`, `logs/action_runs/20260820T200554Z_live_options.log`, `logs/action_runs/20260820T200554Z_options_bot.log`

### Live bot (tail)

```text
20:05:55  INFO      Mode: ext_exits
20:05:56  INFO        Daily log -> logs/daily/2026-08-20.md
20:05:56  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (4 ledger rows)
20:05:56  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         20:05 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $413.16|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.2%  $+0.05        HOLDING until 9:35am scan (MomReversal)|
|  AON  P&L +0.3%  $+0.22          HOLDING until 9:35am scan (Pullback50)|
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
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
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
=== options_live_micro LIVE 2026-08-20T16:05:57.357801-04:00 share=50% ===
2026-08-20 16:05:57,357 INFO === options_live_micro LIVE 2026-08-20T16:05:57.357801-04:00 share=50% ===
Live account equity $413.16 cash $310.82 #225458845 options_level=3
2026-08-20 16:05:57,780 INFO Live account equity $413.16 cash $310.82 #225458845 options_level=3
Live micro done. open_options=1 lots=0
2026-08-20 16:05:57,956 INFO Live micro done. open_options=1 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T201055Z

- UTC timestamp: `20260820T201055Z`
- GitHub run: [#7686](https://github.com/28twagg-ops/TradingBot/actions/runs/32412608313)
- Run id: `32412608313`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T201055Z_live_bot.log`, `logs/action_runs/20260820T201055Z_live_options.log`, `logs/action_runs/20260820T201055Z_options_bot.log`

### Live bot (tail)

```text
20:10:56  INFO      Mode: ext_exits
20:10:57  INFO        Daily log -> logs/daily/2026-08-20.md
20:10:57  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (4 ledger rows)
20:10:57  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         20:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $413.16|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.2%  $+0.05        HOLDING until 9:35am scan (MomReversal)|
|  AON  P&L +0.3%  $+0.22          HOLDING until 9:35am scan (Pullback50)|
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
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
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
=== options_live_micro LIVE 2026-08-20T16:10:58.265716-04:00 share=50% ===
2026-08-20 16:10:58,265 INFO === options_live_micro LIVE 2026-08-20T16:10:58.265716-04:00 share=50% ===
Live account equity $413.16 cash $310.82 #225458845 options_level=3
2026-08-20 16:10:58,366 INFO Live account equity $413.16 cash $310.82 #225458845 options_level=3
Live micro done. open_options=1 lots=0
2026-08-20 16:10:58,454 INFO Live micro done. open_options=1 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T201553Z

- UTC timestamp: `20260820T201553Z`
- GitHub run: [#7687](https://github.com/28twagg-ops/TradingBot/actions/runs/32413065270)
- Run id: `32413065270`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T201553Z_live_bot.log`, `logs/action_runs/20260820T201553Z_live_options.log`, `logs/action_runs/20260820T201553Z_options_bot.log`

### Live bot (tail)

```text
20:15:55  INFO      Mode: ext_exits
20:15:55  INFO        Daily log -> logs/daily/2026-08-20.md
20:15:55  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (4 ledger rows)
20:15:55  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         20:15 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $413.16|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.2%  $+0.05        HOLDING until 9:35am scan (MomReversal)|
|  AON  P&L +0.3%  $+0.22          HOLDING until 9:35am scan (Pullback50)|
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
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
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
=== options_live_micro LIVE 2026-08-20T16:15:56.360814-04:00 share=50% ===
2026-08-20 16:15:56,360 INFO === options_live_micro LIVE 2026-08-20T16:15:56.360814-04:00 share=50% ===
Live account equity $413.16 cash $310.82 #225458845 options_level=3
2026-08-20 16:15:56,408 INFO Live account equity $413.16 cash $310.82 #225458845 options_level=3
Live micro done. open_options=1 lots=0
2026-08-20 16:15:56,435 INFO Live micro done. open_options=1 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T202102Z

- UTC timestamp: `20260820T202102Z`
- GitHub run: [#7688](https://github.com/28twagg-ops/TradingBot/actions/runs/32413516201)
- Run id: `32413516201`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T202102Z_live_bot.log`, `logs/action_runs/20260820T202102Z_live_options.log`, `logs/action_runs/20260820T202102Z_options_bot.log`

### Live bot (tail)

```text
20:21:03  INFO      Mode: ext_exits
20:21:04  INFO        Daily log -> logs/daily/2026-08-20.md
20:21:04  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (4 ledger rows)
20:21:05  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         20:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $413.16|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.2%  $+0.05        HOLDING until 9:35am scan (MomReversal)|
|  AON  P&L +0.3%  $+0.22          HOLDING until 9:35am scan (Pullback50)|
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
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
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
=== options_live_micro LIVE 2026-08-20T16:21:05.947832-04:00 share=50% ===
2026-08-20 16:21:05,947 INFO === options_live_micro LIVE 2026-08-20T16:21:05.947832-04:00 share=50% ===
Live account equity $413.16 cash $310.82 #225458845 options_level=3
2026-08-20 16:21:06,188 INFO Live account equity $413.16 cash $310.82 #225458845 options_level=3
Live micro done. open_options=1 lots=0
2026-08-20 16:21:06,382 INFO Live micro done. open_options=1 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T203141Z

- UTC timestamp: `20260820T203141Z`
- GitHub run: [#7690](https://github.com/28twagg-ops/TradingBot/actions/runs/32414411395)
- Run id: `32414411395`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T203141Z_live_bot.log`, `logs/action_runs/20260820T203141Z_live_options.log`, `logs/action_runs/20260820T203141Z_options_bot.log`

### Live bot (tail)

```text
20:31:42  INFO      Mode: ext_exits
20:31:43  INFO        Daily log -> logs/daily/2026-08-20.md
20:31:43  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (4 ledger rows)
20:31:43  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         20:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $413.16|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.2%  $+0.05        HOLDING until 9:35am scan (MomReversal)|
|  AON  P&L +0.3%  $+0.22          HOLDING until 9:35am scan (Pullback50)|
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
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
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
=== options_live_micro LIVE 2026-08-20T16:31:44.570385-04:00 share=50% ===
2026-08-20 16:31:44,570 INFO === options_live_micro LIVE 2026-08-20T16:31:44.570385-04:00 share=50% ===
Live account equity $413.16 cash $310.82 #225458845 options_level=3
2026-08-20 16:31:44,709 INFO Live account equity $413.16 cash $310.82 #225458845 options_level=3
Live micro done. open_options=1 lots=0
2026-08-20 16:31:44,829 INFO Live micro done. open_options=1 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T203558Z

- UTC timestamp: `20260820T203558Z`
- GitHub run: [#7691](https://github.com/28twagg-ops/TradingBot/actions/runs/32414867484)
- Run id: `32414867484`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T203558Z_live_bot.log`, `logs/action_runs/20260820T203558Z_live_options.log`, `logs/action_runs/20260820T203558Z_options_bot.log`

### Live bot (tail)

```text
20:36:00  INFO      Mode: ext_exits
20:36:01  INFO        Daily log -> logs/daily/2026-08-20.md
20:36:01  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (4 ledger rows)
20:36:02  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         20:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $413.16|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.2%  $+0.05        HOLDING until 9:35am scan (MomReversal)|
|  AON  P&L +0.3%  $+0.22          HOLDING until 9:35am scan (Pullback50)|
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
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
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
=== options_live_micro LIVE 2026-08-20T16:36:03.305632-04:00 share=50% ===
2026-08-20 16:36:03,305 INFO === options_live_micro LIVE 2026-08-20T16:36:03.305632-04:00 share=50% ===
Live account equity $413.16 cash $310.82 #225458845 options_level=3
2026-08-20 16:36:03,540 INFO Live account equity $413.16 cash $310.82 #225458845 options_level=3
Live micro done. open_options=1 lots=0
2026-08-20 16:36:03,757 INFO Live micro done. open_options=1 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T205056Z

- UTC timestamp: `20260820T205056Z`
- GitHub run: [#7694](https://github.com/28twagg-ops/TradingBot/actions/runs/32416214157)
- Run id: `32416214157`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T205056Z_live_bot.log`, `logs/action_runs/20260820T205056Z_live_options.log`, `logs/action_runs/20260820T205056Z_options_bot.log`

### Live bot (tail)

```text
20:50:57  INFO      Mode: ext_exits
20:50:58  INFO        Daily log -> logs/daily/2026-08-20.md
20:50:58  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (4 ledger rows)
20:50:58  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         20:50 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $413.17|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.2%  $+0.06        HOLDING until 9:35am scan (MomReversal)|
|  AON  P&L +0.3%  $+0.22          HOLDING until 9:35am scan (Pullback50)|
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
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
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
=== options_live_micro LIVE 2026-08-20T16:50:59.437748-04:00 share=50% ===
2026-08-20 16:50:59,437 INFO === options_live_micro LIVE 2026-08-20T16:50:59.437748-04:00 share=50% ===
Live account equity $413.17 cash $310.82 #225458845 options_level=3
2026-08-20 16:50:59,642 INFO Live account equity $413.17 cash $310.82 #225458845 options_level=3
Live micro done. open_options=1 lots=0
2026-08-20 16:50:59,820 INFO Live micro done. open_options=1 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T205549Z

- UTC timestamp: `20260820T205549Z`
- GitHub run: [#7695](https://github.com/28twagg-ops/TradingBot/actions/runs/32416660683)
- Run id: `32416660683`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`4s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T205549Z_live_bot.log`, `logs/action_runs/20260820T205549Z_live_options.log`, `logs/action_runs/20260820T205549Z_options_bot.log`

### Live bot (tail)

```text
20:55:50  INFO      Mode: ext_exits
20:55:50  INFO        Daily log -> logs/daily/2026-08-20.md
20:55:50  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (4 ledger rows)
20:55:50  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         20:55 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $413.17|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.2%  $+0.06        HOLDING until 9:35am scan (MomReversal)|
|  AON  P&L +0.3%  $+0.22          HOLDING until 9:35am scan (Pullback50)|
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
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
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
=== options_live_micro LIVE 2026-08-20T16:55:51.735618-04:00 share=50% ===
2026-08-20 16:55:51,735 INFO === options_live_micro LIVE 2026-08-20T16:55:51.735618-04:00 share=50% ===
Live account equity $413.17 cash $310.82 #225458845 options_level=3
2026-08-20 16:55:54,899 INFO Live account equity $413.17 cash $310.82 #225458845 options_level=3
Live micro done. open_options=1 lots=0
2026-08-20 16:55:54,942 INFO Live micro done. open_options=1 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T210056Z

- UTC timestamp: `20260820T210056Z`
- GitHub run: [#7696](https://github.com/28twagg-ops/TradingBot/actions/runs/32417103470)
- Run id: `32417103470`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T210056Z_live_bot.log`, `logs/action_runs/20260820T210056Z_live_options.log`, `logs/action_runs/20260820T210056Z_options_bot.log`

### Live bot (tail)

```text
21:00:56  INFO      Mode: ext_exits
21:00:57  INFO        Daily log -> logs/daily/2026-08-20.md
21:00:57  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (4 ledger rows)
21:00:58  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         21:00 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $413.17|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.2%  $+0.06        HOLDING until 9:35am scan (MomReversal)|
|  AON  P&L +0.3%  $+0.22          HOLDING until 9:35am scan (Pullback50)|
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
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
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
=== options_live_micro LIVE 2026-08-20T17:00:59.142616-04:00 share=50% ===
2026-08-20 17:00:59,142 INFO === options_live_micro LIVE 2026-08-20T17:00:59.142616-04:00 share=50% ===
Live account equity $413.17 cash $310.82 #225458845 options_level=3
2026-08-20 17:00:59,378 INFO Live account equity $413.17 cash $310.82 #225458845 options_level=3
Live micro done. open_options=1 lots=0
2026-08-20 17:00:59,601 INFO Live micro done. open_options=1 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T210620Z

- UTC timestamp: `20260820T210620Z`
- GitHub run: [#7697](https://github.com/28twagg-ops/TradingBot/actions/runs/32417552343)
- Run id: `32417552343`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T210620Z_live_bot.log`, `logs/action_runs/20260820T210620Z_live_options.log`, `logs/action_runs/20260820T210620Z_options_bot.log`

### Live bot (tail)

```text
21:06:21  INFO      Mode: ext_exits
21:06:22  INFO        Daily log -> logs/daily/2026-08-20.md
21:06:22  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (4 ledger rows)
21:06:23  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         21:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $413.17|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.2%  $+0.06        HOLDING until 9:35am scan (MomReversal)|
|  AON  P&L +0.3%  $+0.22          HOLDING until 9:35am scan (Pullback50)|
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
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
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
=== options_live_micro LIVE 2026-08-20T17:06:23.843721-04:00 share=50% ===
2026-08-20 17:06:23,843 INFO === options_live_micro LIVE 2026-08-20T17:06:23.843721-04:00 share=50% ===
Live account equity $413.17 cash $310.82 #225458845 options_level=3
2026-08-20 17:06:24,067 INFO Live account equity $413.17 cash $310.82 #225458845 options_level=3
Live micro done. open_options=1 lots=0
2026-08-20 17:06:24,284 INFO Live micro done. open_options=1 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T211051Z

- UTC timestamp: `20260820T211051Z`
- GitHub run: [#7698](https://github.com/28twagg-ops/TradingBot/actions/runs/32417987845)
- Run id: `32417987845`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T211051Z_live_bot.log`, `logs/action_runs/20260820T211051Z_live_options.log`, `logs/action_runs/20260820T211051Z_options_bot.log`

### Live bot (tail)

```text
21:10:53  INFO      Mode: ext_exits
21:10:53  INFO        Daily log -> logs/daily/2026-08-20.md
21:10:53  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (4 ledger rows)
21:10:54  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         21:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $413.17|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.2%  $+0.06        HOLDING until 9:35am scan (MomReversal)|
|  AON  P&L +0.3%  $+0.22          HOLDING until 9:35am scan (Pullback50)|
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
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
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
=== options_live_micro LIVE 2026-08-20T17:10:54.781069-04:00 share=50% ===
2026-08-20 17:10:54,781 INFO === options_live_micro LIVE 2026-08-20T17:10:54.781069-04:00 share=50% ===
Live account equity $413.17 cash $310.82 #225458845 options_level=3
2026-08-20 17:10:54,822 INFO Live account equity $413.17 cash $310.82 #225458845 options_level=3
Live micro done. open_options=1 lots=0
2026-08-20 17:10:54,846 INFO Live micro done. open_options=1 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T211550Z

- UTC timestamp: `20260820T211550Z`
- GitHub run: [#7699](https://github.com/28twagg-ops/TradingBot/actions/runs/32418429781)
- Run id: `32418429781`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T211550Z_live_bot.log`, `logs/action_runs/20260820T211550Z_live_options.log`, `logs/action_runs/20260820T211550Z_options_bot.log`

### Live bot (tail)

```text
21:15:51  INFO      Mode: ext_exits
21:15:52  INFO        Daily log -> logs/daily/2026-08-20.md
21:15:52  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (4 ledger rows)
21:15:52  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         21:15 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $413.17|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.2%  $+0.06        HOLDING until 9:35am scan (MomReversal)|
|  AON  P&L +0.3%  $+0.22          HOLDING until 9:35am scan (Pullback50)|
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
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
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
=== options_live_micro LIVE 2026-08-20T17:15:53.012216-04:00 share=50% ===
2026-08-20 17:15:53,012 INFO === options_live_micro LIVE 2026-08-20T17:15:53.012216-04:00 share=50% ===
Live account equity $413.17 cash $310.82 #225458845 options_level=3
2026-08-20 17:15:53,053 INFO Live account equity $413.17 cash $310.82 #225458845 options_level=3
Live micro done. open_options=1 lots=0
2026-08-20 17:15:53,078 INFO Live micro done. open_options=1 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T212052Z

- UTC timestamp: `20260820T212052Z`
- GitHub run: [#7700](https://github.com/28twagg-ops/TradingBot/actions/runs/32418860651)
- Run id: `32418860651`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T212052Z_live_bot.log`, `logs/action_runs/20260820T212052Z_live_options.log`, `logs/action_runs/20260820T212052Z_options_bot.log`

### Live bot (tail)

```text
21:20:53  INFO      Mode: ext_exits
21:20:53  INFO        Daily log -> logs/daily/2026-08-20.md
21:20:53  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (4 ledger rows)
21:20:53  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         21:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $413.17|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.2%  $+0.06        HOLDING until 9:35am scan (MomReversal)|
|  AON  P&L +0.3%  $+0.22          HOLDING until 9:35am scan (Pullback50)|
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
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
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
=== options_live_micro LIVE 2026-08-20T17:20:54.541377-04:00 share=50% ===
2026-08-20 17:20:54,541 INFO === options_live_micro LIVE 2026-08-20T17:20:54.541377-04:00 share=50% ===
Live account equity $413.17 cash $310.82 #225458845 options_level=3
2026-08-20 17:20:54,600 INFO Live account equity $413.17 cash $310.82 #225458845 options_level=3
Live micro done. open_options=1 lots=0
2026-08-20 17:20:54,641 INFO Live micro done. open_options=1 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T213601Z

- UTC timestamp: `20260820T213601Z`
- GitHub run: [#7703](https://github.com/28twagg-ops/TradingBot/actions/runs/32420125975)
- Run id: `32420125975`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T213601Z_live_bot.log`, `logs/action_runs/20260820T213601Z_live_options.log`, `logs/action_runs/20260820T213601Z_options_bot.log`

### Live bot (tail)

```text
21:36:02  INFO      Mode: ext_exits
21:36:03  INFO        Daily log -> logs/daily/2026-08-20.md
21:36:03  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (4 ledger rows)
21:36:04  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         21:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $413.17|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.2%  $+0.06        HOLDING until 9:35am scan (MomReversal)|
|  AON  P&L +0.3%  $+0.22          HOLDING until 9:35am scan (Pullback50)|
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
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
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
=== options_live_micro LIVE 2026-08-20T17:36:05.035026-04:00 share=50% ===
2026-08-20 17:36:05,035 INFO === options_live_micro LIVE 2026-08-20T17:36:05.035026-04:00 share=50% ===
Live account equity $413.17 cash $310.82 #225458845 options_level=3
2026-08-20 17:36:05,261 INFO Live account equity $413.17 cash $310.82 #225458845 options_level=3
Live micro done. open_options=1 lots=0
2026-08-20 17:36:05,470 INFO Live micro done. open_options=1 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T214059Z

- UTC timestamp: `20260820T214059Z`
- GitHub run: [#7704](https://github.com/28twagg-ops/TradingBot/actions/runs/32420541872)
- Run id: `32420541872`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T214059Z_live_bot.log`, `logs/action_runs/20260820T214059Z_live_options.log`, `logs/action_runs/20260820T214059Z_options_bot.log`

### Live bot (tail)

```text
21:41:00  INFO      Mode: ext_exits
21:41:01  INFO        Daily log -> logs/daily/2026-08-20.md
21:41:01  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (4 ledger rows)
21:41:02  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         21:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $413.17|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.2%  $+0.06        HOLDING until 9:35am scan (MomReversal)|
|  AON  P&L +0.3%  $+0.22          HOLDING until 9:35am scan (Pullback50)|
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
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
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
=== options_live_micro LIVE 2026-08-20T17:41:02.770334-04:00 share=50% ===
2026-08-20 17:41:02,770 INFO === options_live_micro LIVE 2026-08-20T17:41:02.770334-04:00 share=50% ===
Live account equity $413.17 cash $310.82 #225458845 options_level=3
2026-08-20 17:41:02,963 INFO Live account equity $413.17 cash $310.82 #225458845 options_level=3
Live micro done. open_options=1 lots=0
2026-08-20 17:41:03,146 INFO Live micro done. open_options=1 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T214555Z

- UTC timestamp: `20260820T214555Z`
- GitHub run: [#7705](https://github.com/28twagg-ops/TradingBot/actions/runs/32420955384)
- Run id: `32420955384`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T214555Z_live_bot.log`, `logs/action_runs/20260820T214555Z_live_options.log`, `logs/action_runs/20260820T214555Z_options_bot.log`

### Live bot (tail)

```text
21:45:55  INFO      Mode: ext_exits
21:45:56  INFO        Daily log -> logs/daily/2026-08-20.md
21:45:56  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (4 ledger rows)
21:45:56  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         21:45 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $413.17|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.2%  $+0.06        HOLDING until 9:35am scan (MomReversal)|
|  AON  P&L +0.3%  $+0.22          HOLDING until 9:35am scan (Pullback50)|
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
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
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
=== options_live_micro LIVE 2026-08-20T17:45:57.618538-04:00 share=50% ===
2026-08-20 17:45:57,618 INFO === options_live_micro LIVE 2026-08-20T17:45:57.618538-04:00 share=50% ===
Live account equity $413.17 cash $310.82 #225458845 options_level=3
2026-08-20 17:45:57,829 INFO Live account equity $413.17 cash $310.82 #225458845 options_level=3
Live micro done. open_options=1 lots=0
2026-08-20 17:45:58,006 INFO Live micro done. open_options=1 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T215053Z

- UTC timestamp: `20260820T215053Z`
- GitHub run: [#7706](https://github.com/28twagg-ops/TradingBot/actions/runs/32421363771)
- Run id: `32421363771`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T215053Z_live_bot.log`, `logs/action_runs/20260820T215053Z_live_options.log`, `logs/action_runs/20260820T215053Z_options_bot.log`

### Live bot (tail)

```text
21:50:53  INFO      Mode: ext_exits
21:50:54  INFO        Daily log -> logs/daily/2026-08-20.md
21:50:54  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (4 ledger rows)
21:50:54  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         21:50 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $413.17|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.2%  $+0.06        HOLDING until 9:35am scan (MomReversal)|
|  AON  P&L +0.3%  $+0.22          HOLDING until 9:35am scan (Pullback50)|
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
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
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
=== options_live_micro LIVE 2026-08-20T17:50:55.421500-04:00 share=50% ===
2026-08-20 17:50:55,421 INFO === options_live_micro LIVE 2026-08-20T17:50:55.421500-04:00 share=50% ===
Live account equity $413.17 cash $310.82 #225458845 options_level=3
2026-08-20 17:50:55,665 INFO Live account equity $413.17 cash $310.82 #225458845 options_level=3
Live micro done. open_options=1 lots=0
2026-08-20 17:50:55,703 INFO Live micro done. open_options=1 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T215550Z

- UTC timestamp: `20260820T215550Z`
- GitHub run: [#7707](https://github.com/28twagg-ops/TradingBot/actions/runs/32421774173)
- Run id: `32421774173`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T215550Z_live_bot.log`, `logs/action_runs/20260820T215550Z_live_options.log`, `logs/action_runs/20260820T215550Z_options_bot.log`

### Live bot (tail)

```text
21:55:51  INFO      Mode: ext_exits
21:55:52  INFO        Daily log -> logs/daily/2026-08-20.md
21:55:52  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (4 ledger rows)
21:55:52  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         21:55 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $413.17|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.2%  $+0.06        HOLDING until 9:35am scan (MomReversal)|
|  AON  P&L +0.3%  $+0.22          HOLDING until 9:35am scan (Pullback50)|
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
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
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
=== options_live_micro LIVE 2026-08-20T17:55:53.205054-04:00 share=50% ===
2026-08-20 17:55:53,205 INFO === options_live_micro LIVE 2026-08-20T17:55:53.205054-04:00 share=50% ===
Live account equity $413.17 cash $310.82 #225458845 options_level=3
2026-08-20 17:55:53,302 INFO Live account equity $413.17 cash $310.82 #225458845 options_level=3
Live micro done. open_options=1 lots=0
2026-08-20 17:55:53,381 INFO Live micro done. open_options=1 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T220058Z

- UTC timestamp: `20260820T220058Z`
- GitHub run: [#7708](https://github.com/28twagg-ops/TradingBot/actions/runs/32422184492)
- Run id: `32422184492`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T220058Z_live_bot.log`, `logs/action_runs/20260820T220058Z_live_options.log`, `logs/action_runs/20260820T220058Z_options_bot.log`

### Live bot (tail)

```text
22:00:59  INFO      Mode: ext_exits
22:01:00  INFO        Daily log -> logs/daily/2026-08-20.md
22:01:00  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (4 ledger rows)
22:01:00  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         22:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $413.17|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.2%  $+0.06        HOLDING until 9:35am scan (MomReversal)|
|  AON  P&L +0.3%  $+0.22          HOLDING until 9:35am scan (Pullback50)|
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
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
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
=== options_live_micro LIVE 2026-08-20T18:01:01.136223-04:00 share=50% ===
2026-08-20 18:01:01,136 INFO === options_live_micro LIVE 2026-08-20T18:01:01.136223-04:00 share=50% ===
Live account equity $413.17 cash $310.82 #225458845 options_level=3
2026-08-20 18:01:01,180 INFO Live account equity $413.17 cash $310.82 #225458845 options_level=3
Live micro done. open_options=1 lots=0
2026-08-20 18:01:01,208 INFO Live micro done. open_options=1 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T220553Z

- UTC timestamp: `20260820T220553Z`
- GitHub run: [#7709](https://github.com/28twagg-ops/TradingBot/actions/runs/32422595854)
- Run id: `32422595854`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T220553Z_live_bot.log`, `logs/action_runs/20260820T220553Z_live_options.log`, `logs/action_runs/20260820T220553Z_options_bot.log`

### Live bot (tail)

```text
22:05:54  INFO      Mode: ext_exits
22:05:55  INFO        Daily log -> logs/daily/2026-08-20.md
22:05:55  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (4 ledger rows)
22:05:55  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         22:05 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $413.17|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.2%  $+0.06        HOLDING until 9:35am scan (MomReversal)|
|  AON  P&L +0.3%  $+0.22          HOLDING until 9:35am scan (Pullback50)|
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
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
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
=== options_live_micro LIVE 2026-08-20T18:05:56.410733-04:00 share=50% ===
2026-08-20 18:05:56,410 INFO === options_live_micro LIVE 2026-08-20T18:05:56.410733-04:00 share=50% ===
Live account equity $413.17 cash $310.82 #225458845 options_level=3
2026-08-20 18:05:56,638 INFO Live account equity $413.17 cash $310.82 #225458845 options_level=3
Live micro done. open_options=1 lots=0
2026-08-20 18:05:56,846 INFO Live micro done. open_options=1 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260820T221411Z

- UTC timestamp: `20260820T221411Z`
- GitHub run: [#7710](https://github.com/28twagg-ops/TradingBot/actions/runs/32423001936)
- Run id: `32423001936`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260820T221411Z_live_bot.log`, `logs/action_runs/20260820T221411Z_live_options.log`, `logs/action_runs/20260820T221411Z_options_bot.log`

### Live bot (tail)

```text
22:14:13  INFO      Mode: ext_exits
22:14:13  INFO        Daily log -> logs/daily/2026-08-20.md
22:14:13  INFO        Daily log reconciled -> logs/daily/2026-08-20.md (4 ledger rows)
22:14:13  INFO        Daily log -> logs/daily/2026-08-20.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         22:14 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $413.12|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  MNST  P&L +0.0%  $+0.01        HOLDING until 9:35am scan (MomReversal)|
|  AON  P&L +0.3%  $+0.22          HOLDING until 9:35am scan (Pullback50)|
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
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
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
=== options_live_micro LIVE 2026-08-20T18:14:14.796769-04:00 share=50% ===
2026-08-20 18:14:14,796 INFO === options_live_micro LIVE 2026-08-20T18:14:14.796769-04:00 share=50% ===
Live account equity $413.12 cash $310.82 #225458845 options_level=3
2026-08-20 18:14:15,073 INFO Live account equity $413.12 cash $310.82 #225458845 options_level=3
Live micro done. open_options=1 lots=0
2026-08-20 18:14:15,180 INFO Live micro done. open_options=1 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---
