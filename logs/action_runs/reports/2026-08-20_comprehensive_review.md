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
