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
