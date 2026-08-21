# Daily Comprehensive Action Review - 2026-08-21

_Auto-generated from GitHub Actions run output. Each run appends a summary; full stdout is in linked per-run log files._
## Run 20260821T130057Z

- UTC timestamp: `20260821T130057Z`
- GitHub run: [#7732](https://github.com/28twagg-ops/TradingBot/actions/runs/32484604599)
- Run id: `32484604599`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260821T130057Z_live_bot.log`, `logs/action_runs/20260821T130057Z_live_options.log`, `logs/action_runs/20260821T130057Z_options_bot.log`

### Live bot (tail)

```text
13:00:59  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:00 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $413.38|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $413.38|
|  Cash                                                           $310.80|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $100.58|
|  Open P&L                                                        $+0.52|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AON      Pullback50      $70.40     $350.82  $353.01  +0.6%   $+0.44  |
|  MNST     MomReversal     $30.19     $47.41   $47.54   +0.3%   $+0.08  |
|                                                                        |
|  Total invested                                                 $100.58|
|  Total open P&L                                                  $+0.52|
+========================================================================+

+========================================================================+
|                     OPTION HOLDINGS  (1 contracts)                     |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
|                                                                        |
|  Options open P&L                                                $-7.00|
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
|  2026-08-20  SELL  AES  Pullback50  $62.00  P&L $+0.00                 |
|  2026-08-20  SELL  ARE  Pullback50  $69.70  P&L $-0.12                 |
|  2026-08-20  SELL  JKHY  MA_Squeeze  $71.62  P&L $+0.75                |
|  2026-08-20  SELL  ARE  Pullback50  $70.48  P&L $-0.24                 |
|  2026-08-19  SELL  AAPL  Pullback50  $79.01  P&L $+1.50                |
|  2026-08-19  SELL  JKHY  MA_Squeeze  $70.80  P&L $+0.05                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-21T09:01:00.859216-04:00 share=50% ===
2026-08-21 09:01:00,859 INFO === options_live_micro LIVE 2026-08-21T09:01:00.859216-04:00 share=50% ===
Live account equity $413.38 cash $310.80 #225458845 options_level=3
2026-08-21 09:01:01,105 INFO Live account equity $413.38 cash $310.80 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-08-21 09:01:01,179 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=1 lots=0
2026-08-21 09:01:01,253 INFO Live micro done. open_options=1 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260821T130703Z

- UTC timestamp: `20260821T130703Z`
- GitHub run: [#7733](https://github.com/28twagg-ops/TradingBot/actions/runs/32485028784)
- Run id: `32485028784`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260821T130703Z_live_bot.log`, `logs/action_runs/20260821T130703Z_live_options.log`, `logs/action_runs/20260821T130703Z_options_bot.log`

### Live bot (tail)

```text
13:07:05  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:07 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $413.38|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $413.38|
|  Cash                                                           $310.80|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $100.58|
|  Open P&L                                                        $+0.52|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AON      Pullback50      $70.40     $350.82  $353.01  +0.6%   $+0.44  |
|  MNST     MomReversal     $30.19     $47.41   $47.54   +0.3%   $+0.08  |
|                                                                        |
|  Total invested                                                 $100.58|
|  Total open P&L                                                  $+0.52|
+========================================================================+

+========================================================================+
|                     OPTION HOLDINGS  (1 contracts)                     |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
|                                                                        |
|  Options open P&L                                                $-7.00|
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
|  2026-08-20  SELL  AES  Pullback50  $62.00  P&L $+0.00                 |
|  2026-08-20  SELL  ARE  Pullback50  $69.70  P&L $-0.12                 |
|  2026-08-20  SELL  JKHY  MA_Squeeze  $71.62  P&L $+0.75                |
|  2026-08-20  SELL  ARE  Pullback50  $70.48  P&L $-0.24                 |
|  2026-08-19  SELL  AAPL  Pullback50  $79.01  P&L $+1.50                |
|  2026-08-19  SELL  JKHY  MA_Squeeze  $70.80  P&L $+0.05                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-21T09:07:06.104379-04:00 share=50% ===
2026-08-21 09:07:06,104 INFO === options_live_micro LIVE 2026-08-21T09:07:06.104379-04:00 share=50% ===
Live account equity $413.38 cash $310.80 #225458845 options_level=3
2026-08-21 09:07:06,163 INFO Live account equity $413.38 cash $310.80 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-08-21 09:07:06,176 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=1 lots=0
2026-08-21 09:07:06,194 INFO Live micro done. open_options=1 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260821T131053Z

- UTC timestamp: `20260821T131053Z`
- GitHub run: [#7734](https://github.com/28twagg-ops/TradingBot/actions/runs/32485436610)
- Run id: `32485436610`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260821T131053Z_live_bot.log`, `logs/action_runs/20260821T131053Z_live_options.log`, `logs/action_runs/20260821T131053Z_options_bot.log`

### Live bot (tail)

```text
13:10:54  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $413.38|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $413.38|
|  Cash                                                           $310.80|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $100.58|
|  Open P&L                                                        $+0.52|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AON      Pullback50      $70.40     $350.82  $353.01  +0.6%   $+0.44  |
|  MNST     MomReversal     $30.19     $47.41   $47.54   +0.3%   $+0.08  |
|                                                                        |
|  Total invested                                                 $100.58|
|  Total open P&L                                                  $+0.52|
+========================================================================+

+========================================================================+
|                     OPTION HOLDINGS  (1 contracts)                     |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
|                                                                        |
|  Options open P&L                                                $-7.00|
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
|  2026-08-20  SELL  AES  Pullback50  $62.00  P&L $+0.00                 |
|  2026-08-20  SELL  ARE  Pullback50  $69.70  P&L $-0.12                 |
|  2026-08-20  SELL  JKHY  MA_Squeeze  $71.62  P&L $+0.75                |
|  2026-08-20  SELL  ARE  Pullback50  $70.48  P&L $-0.24                 |
|  2026-08-19  SELL  AAPL  Pullback50  $79.01  P&L $+1.50                |
|  2026-08-19  SELL  JKHY  MA_Squeeze  $70.80  P&L $+0.05                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-21T09:10:55.182468-04:00 share=50% ===
2026-08-21 09:10:55,182 INFO === options_live_micro LIVE 2026-08-21T09:10:55.182468-04:00 share=50% ===
Live account equity $413.38 cash $310.80 #225458845 options_level=3
2026-08-21 09:10:55,228 INFO Live account equity $413.38 cash $310.80 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-08-21 09:10:55,238 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=1 lots=0
2026-08-21 09:10:55,248 INFO Live micro done. open_options=1 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260821T131602Z

- UTC timestamp: `20260821T131602Z`
- GitHub run: [#7735](https://github.com/28twagg-ops/TradingBot/actions/runs/32485858507)
- Run id: `32485858507`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260821T131602Z_live_bot.log`, `logs/action_runs/20260821T131602Z_live_options.log`, `logs/action_runs/20260821T131602Z_options_bot.log`

### Live bot (tail)

```text
13:16:04  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $413.38|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $413.38|
|  Cash                                                           $310.80|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $100.58|
|  Open P&L                                                        $+0.52|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AON      Pullback50      $70.40     $350.82  $353.01  +0.6%   $+0.44  |
|  MNST     MomReversal     $30.19     $47.41   $47.54   +0.3%   $+0.08  |
|                                                                        |
|  Total invested                                                 $100.58|
|  Total open P&L                                                  $+0.52|
+========================================================================+

+========================================================================+
|                     OPTION HOLDINGS  (1 contracts)                     |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
|                                                                        |
|  Options open P&L                                                $-7.00|
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
|  2026-08-20  SELL  AES  Pullback50  $62.00  P&L $+0.00                 |
|  2026-08-20  SELL  ARE  Pullback50  $69.70  P&L $-0.12                 |
|  2026-08-20  SELL  JKHY  MA_Squeeze  $71.62  P&L $+0.75                |
|  2026-08-20  SELL  ARE  Pullback50  $70.48  P&L $-0.24                 |
|  2026-08-19  SELL  AAPL  Pullback50  $79.01  P&L $+1.50                |
|  2026-08-19  SELL  JKHY  MA_Squeeze  $70.80  P&L $+0.05                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-21T09:16:06.305503-04:00 share=50% ===
2026-08-21 09:16:06,305 INFO === options_live_micro LIVE 2026-08-21T09:16:06.305503-04:00 share=50% ===
Live account equity $413.38 cash $310.80 #225458845 options_level=3
2026-08-21 09:16:06,521 INFO Live account equity $413.38 cash $310.80 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-08-21 09:16:06,581 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=1 lots=0
2026-08-21 09:16:06,642 INFO Live micro done. open_options=1 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260821T132301Z

- UTC timestamp: `20260821T132301Z`
- GitHub run: [#7736](https://github.com/28twagg-ops/TradingBot/actions/runs/32486284431)
- Run id: `32486284431`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260821T132301Z_live_bot.log`, `logs/action_runs/20260821T132301Z_live_options.log`, `logs/action_runs/20260821T132301Z_options_bot.log`

### Live bot (tail)

```text
13:23:03  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:23 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $413.37|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $413.37|
|  Cash                                                           $310.80|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $100.57|
|  Open P&L                                                        $+0.51|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AON      Pullback50      $70.39     $350.82  $352.95  +0.6%   $+0.43  |
|  MNST     MomReversal     $30.19     $47.41   $47.54   +0.3%   $+0.08  |
|                                                                        |
|  Total invested                                                 $100.57|
|  Total open P&L                                                  $+0.51|
+========================================================================+

+========================================================================+
|                     OPTION HOLDINGS  (1 contracts)                     |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
|                                                                        |
|  Options open P&L                                                $-7.00|
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
|  2026-08-20  SELL  AES  Pullback50  $62.00  P&L $+0.00                 |
|  2026-08-20  SELL  ARE  Pullback50  $69.70  P&L $-0.12                 |
|  2026-08-20  SELL  JKHY  MA_Squeeze  $71.62  P&L $+0.75                |
|  2026-08-20  SELL  ARE  Pullback50  $70.48  P&L $-0.24                 |
|  2026-08-19  SELL  AAPL  Pullback50  $79.01  P&L $+1.50                |
|  2026-08-19  SELL  JKHY  MA_Squeeze  $70.80  P&L $+0.05                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-21T09:23:06.258006-04:00 share=50% ===
2026-08-21 09:23:06,258 INFO === options_live_micro LIVE 2026-08-21T09:23:06.258006-04:00 share=50% ===
Live account equity $413.37 cash $310.80 #225458845 options_level=3
2026-08-21 09:23:06,304 INFO Live account equity $413.37 cash $310.80 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-08-21 09:23:06,316 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=1 lots=0
2026-08-21 09:23:06,324 INFO Live micro done. open_options=1 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260821T132552Z

- UTC timestamp: `20260821T132552Z`
- GitHub run: [#7737](https://github.com/28twagg-ops/TradingBot/actions/runs/32486721595)
- Run id: `32486721595`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260821T132552Z_live_bot.log`, `logs/action_runs/20260821T132552Z_live_options.log`, `logs/action_runs/20260821T132552Z_options_bot.log`

### Live bot (tail)

```text
13:25:53  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:25 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $413.37|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $413.37|
|  Cash                                                           $310.80|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $100.57|
|  Open P&L                                                        $+0.51|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AON      Pullback50      $70.39     $350.82  $352.95  +0.6%   $+0.43  |
|  MNST     MomReversal     $30.19     $47.41   $47.54   +0.3%   $+0.08  |
|                                                                        |
|  Total invested                                                 $100.57|
|  Total open P&L                                                  $+0.51|
+========================================================================+

+========================================================================+
|                     OPTION HOLDINGS  (1 contracts)                     |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  WMT260821C00110000      $0.09    $0.02    -77.8%   $-7.00    $2.00    |
|                                                                        |
|  Options open P&L                                                $-7.00|
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
|  2026-08-20  SELL  AES  Pullback50  $62.00  P&L $+0.00                 |
|  2026-08-20  SELL  ARE  Pullback50  $69.70  P&L $-0.12                 |
|  2026-08-20  SELL  JKHY  MA_Squeeze  $71.62  P&L $+0.75                |
|  2026-08-20  SELL  ARE  Pullback50  $70.48  P&L $-0.24                 |
|  2026-08-19  SELL  AAPL  Pullback50  $79.01  P&L $+1.50                |
|  2026-08-19  SELL  JKHY  MA_Squeeze  $70.80  P&L $+0.05                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-21T09:25:55.382649-04:00 share=50% ===
2026-08-21 09:25:55,382 INFO === options_live_micro LIVE 2026-08-21T09:25:55.382649-04:00 share=50% ===
Live account equity $413.37 cash $310.80 #225458845 options_level=3
2026-08-21 09:25:55,600 INFO Live account equity $413.37 cash $310.80 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-08-21 09:25:55,660 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=1 lots=0
2026-08-21 09:25:55,719 INFO Live micro done. open_options=1 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260821T133332Z

- UTC timestamp: `20260821T133332Z`
- GitHub run: [#7738](https://github.com/28twagg-ops/TradingBot/actions/runs/32487159122)
- Run id: `32487159122`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260821T133332Z_live_bot.log`, `logs/action_runs/20260821T133332Z_live_options.log`, `logs/action_runs/20260821T133332Z_options_bot.log`

### Live bot (tail)

```text
13:33:33  INFO      Mode: morning_prep
13:33:34  INFO        [prep_positions] 3/3 (3 valid)
13:33:34  INFO      Fetching tickers (universe=both)...
13:33:34  INFO        S&P 500: 503
13:33:34  INFO        MidCap 400: 400
13:33:34  INFO        Total: 903 tickers
13:33:37  INFO        [prep_universe] 40/900 (40 valid)
13:33:38  INFO        [prep_universe] 80/900 (80 valid)
13:33:40  INFO        [prep_universe] 120/900 (120 valid)
13:33:41  INFO        [prep_universe] 160/900 (160 valid)
13:33:43  INFO        [prep_universe] 200/900 (199 valid)
13:33:48  INFO        [prep_universe] 240/900 (238 valid)
13:33:59  INFO        [prep_universe] 280/900 (278 valid)
13:34:13  INFO        [prep_universe] 320/900 (318 valid)
13:34:23  INFO        [prep_universe] 360/900 (358 valid)
13:34:37  INFO        [prep_universe] 400/900 (397 valid)
13:34:50  INFO        [prep_universe] 440/900 (437 valid)
13:35:00  INFO        [prep_universe] 480/900 (477 valid)
13:35:11  INFO        [prep_universe] 520/900 (517 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260821T133622Z

- UTC timestamp: `20260821T133622Z`
- GitHub run: [#7739](https://github.com/28twagg-ops/TradingBot/actions/runs/32487600554)
- Run id: `32487600554`
- Live bot: exit=`0`, duration=`217s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260821T133622Z_live_bot.log`, `logs/action_runs/20260821T133622Z_live_options.log`, `logs/action_runs/20260821T133622Z_options_bot.log`

### Live bot (tail)

```text
13:36:24  INFO      Mode: morning_prep
13:36:24  INFO        [prep_positions] 3/3 (3 valid)
13:36:24  INFO      Fetching tickers (universe=both)...
13:36:24  INFO        S&P 500: 503
13:36:25  INFO        MidCap 400: 400
13:36:25  INFO        Total: 903 tickers
13:36:26  INFO        [prep_universe] 40/900 (40 valid)
13:36:29  INFO        [prep_universe] 80/900 (80 valid)
13:36:31  INFO        [prep_universe] 120/900 (120 valid)
13:36:33  INFO        [prep_universe] 160/900 (160 valid)
13:36:36  INFO        [prep_universe] 200/900 (199 valid)
13:36:41  INFO        [prep_universe] 240/900 (238 valid)
13:36:52  INFO        [prep_universe] 280/900 (278 valid)
13:37:03  INFO        [prep_universe] 320/900 (318 valid)
13:37:16  INFO        [prep_universe] 360/900 (358 valid)
13:37:27  INFO        [prep_universe] 400/900 (397 valid)
13:37:38  INFO        [prep_universe] 440/900 (437 valid)
13:37:51  INFO        [prep_universe] 480/900 (477 valid)
13:38:02  INFO        [prep_universe] 520/900 (517 valid)
13:38:16  INFO        [prep_universe] 560/900 (557 valid)
13:38:26  INFO        [prep_universe] 600/900 (597 valid)
13:38:40  INFO        [prep_universe] 640/900 (637 valid)
13:38:51  INFO        [prep_universe] 680/900 (677 valid)
13:39:04  INFO        [prep_universe] 720/900 (717 valid)
13:39:14  INFO        [prep_universe] 760/900 (757 valid)
13:39:27  INFO        [prep_universe] 800/900 (797 valid)
13:39:39  INFO        [prep_universe] 840/900 (836 valid)
13:39:50  INFO        [prep_universe] 880/900 (876 valid)
13:39:57  INFO        [prep_universe] 900/900 (896 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $410.96|
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
|  Invested                                                       $162.14|
|  Open P&L                                                        $+0.11|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $61.95     $14.76   $14.76   -0.0%   $-0.02  |
|  AON      Pullback50      $70.10     $350.82  $351.51  +0.2%   $+0.14  |
|  MNST     MomReversal     $30.09     $47.41   $47.39   -0.0%   $-0.01  |
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
|  Exit candidates                                                      2|
|  Signal candidates                                                   27|
|  Universe scanned                                                   900|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-21T09:39:59.985488-04:00 share=50% ===
2026-08-21 09:39:59,985 INFO === options_live_micro LIVE 2026-08-21T09:39:59.985488-04:00 share=50% ===
Live account equity $411.40 cash $248.82 #225458845 options_level=3
2026-08-21 09:40:00,113 INFO Live account equity $411.40 cash $248.82 #225458845 options_level=3
Live micro sleeve $206 (50% of $411) deployed $0 open_strategies=0/4 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy)
2026-08-21 09:40:00,285 INFO Live micro sleeve $206 (50% of $411) deployed $0 open_strategies=0/4 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-21 09:40:00,285 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 4
2026-08-21 09:40:15,615 INFO Live micro signals: 4
  try S218 56%win/+49%med COST
2026-08-21 09:40:15,616 INFO   try S218 56%win/+49%med COST
  skip S218 COST: no contract under $75
2026-08-21 09:40:15,921 INFO   skip S218 COST: no contract under $75
  try S218 56%win/+49%med SYK
2026-08-21 09:40:15,921 INFO   try S218 56%win/+49%med SYK
  skip S218 SYK: no contract under $75
2026-08-21 09:40:16,075 INFO   skip S218 SYK: no contract under $75
  try S210 55%win/+47%med AMD
2026-08-21 09:40:16,075 INFO   try S210 55%win/+47%med AMD
  skip S210 AMD: no contract under $75
2026-08-21 09:40:16,270 INFO   skip S210 AMD: no contract under $75
  try S210 55%win/+47%med COIN
2026-08-21 09:40:16,271 INFO   try S210 55%win/+47%med COIN
  skip S210 COIN: no contract under $75
2026-08-21 09:40:16,451 INFO   skip S210 COIN: no contract under $75
Live micro done. open_options=1 lots=0
2026-08-21 09:40:16,632 INFO Live micro done. open_options=1 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260821T134612Z

- UTC timestamp: `20260821T134612Z`
- GitHub run: [#7741](https://github.com/28twagg-ops/TradingBot/actions/runs/32488470325)
- Run id: `32488470325`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260821T134612Z_live_bot.log`, `logs/action_runs/20260821T134612Z_live_options.log`, `logs/action_runs/20260821T134612Z_options_bot.log`

### Live bot (tail)

```text
13:46:13  INFO      Mode: morning_scan
13:46:13  INFO        [positions] 3/3 (3 valid)
13:46:14  INFO        SELL LIMIT AES  qty=4.198509485  limit=$14.75  id=1358e9cf-0928-43ba-a031-72b42f8946ff
13:46:44  INFO        SELL LIMIT filled AES (confirmed by position check)
13:46:44  INFO        TX logged: SELL AES  P&L -0.03%
13:46:44  INFO        SELL LIMIT MNST  qty=0.634956125  limit=$47.59  id=3ae3bf81-7fef-4428-ac03-5bbdae70ef48
13:47:04  INFO        SELL LIMIT filled MNST (confirmed by position check)
13:47:04  INFO        TX logged: SELL MNST  P&L 0.43%
13:47:04  INFO        Universe cache hit: 903 tickers (tickers_2026-08-21.json)
13:47:05  INFO        [universe] 40/902 (40 valid)
13:47:07  INFO        [universe] 80/902 (80 valid)
13:47:08  INFO        [universe] 120/902 (120 valid)
13:47:10  INFO        [universe] 160/902 (160 valid)
13:47:11  INFO        [universe] 200/902 (199 valid)
13:47:19  INFO        [universe] 240/902 (238 valid)
13:47:29  INFO        [universe] 280/902 (278 valid)
13:47:42  INFO        [universe] 320/902 (318 valid)
13:47:55  INFO        [universe] 360/902 (358 valid)
13:48:05  INFO        [universe] 400/902 (397 valid)
13:48:19  INFO        [universe] 440/902 (437 valid)
13:48:29  INFO        [universe] 480/902 (477 valid)
13:48:42  INFO        [universe] 520/902 (517 valid)
13:48:53  INFO        [universe] 560/902 (557 valid)
13:49:06  INFO        [universe] 600/902 (597 valid)
13:49:17  INFO        [universe] 640/902 (637 valid)
13:49:30  INFO        [universe] 680/902 (677 valid)
13:49:41  INFO        [universe] 720/902 (717 valid)
13:49:54  INFO        [universe] 760/902 (757 valid)
13:50:04  INFO        [universe] 800/902 (797 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260821T135615Z

- UTC timestamp: `20260821T135615Z`
- GitHub run: [#7743](https://github.com/28twagg-ops/TradingBot/actions/runs/32489358900)
- Run id: `32489358900`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260821T135615Z_live_bot.log`, `logs/action_runs/20260821T135615Z_live_options.log`, `logs/action_runs/20260821T135615Z_options_bot.log`

### Live bot (tail)

```text
13:56:16  INFO      Mode: morning_scan
13:56:17  INFO        [positions] 3/3 (3 valid)
13:56:18  INFO        SELL order cancelled AES  type=OrderType.STOP  id=8d746935-244e-4e0d-820c-fed0dad4b600
13:56:18  INFO        SELL LIMIT AES  qty=3.952590585  limit=$14.76  id=aeed8564-f563-474a-ae35-5793628cc919
13:56:48  INFO        SELL LIMIT filled AES (confirmed by position check)
13:56:48  INFO        TX logged: SELL AES  P&L 0.03%
13:56:48  INFO        Universe cache hit: 903 tickers (tickers_2026-08-21.json)
13:56:49  INFO        [universe] 40/901 (40 valid)
13:56:51  INFO        [universe] 80/901 (80 valid)
13:56:53  INFO        [universe] 120/901 (120 valid)
13:56:55  INFO        [universe] 160/901 (160 valid)
13:56:56  INFO        [universe] 200/901 (199 valid)
13:57:01  INFO        [universe] 240/901 (238 valid)
13:57:14  INFO        [universe] 280/901 (278 valid)
13:57:27  INFO        [universe] 320/901 (318 valid)
13:57:38  INFO        [universe] 360/901 (358 valid)
13:57:51  INFO        [universe] 400/901 (397 valid)
13:58:02  INFO        [universe] 440/901 (437 valid)
13:58:13  INFO        [universe] 480/901 (477 valid)
13:58:26  INFO        [universe] 520/901 (517 valid)
13:58:37  INFO        [universe] 560/901 (557 valid)
13:58:50  INFO        [universe] 600/901 (597 valid)
13:59:01  INFO        [universe] 640/901 (637 valid)
13:59:14  INFO        [universe] 680/901 (677 valid)
13:59:25  INFO        [universe] 720/901 (717 valid)
13:59:38  INFO        [universe] 760/901 (757 valid)
13:59:52  INFO        [universe] 800/901 (797 valid)
14:00:02  INFO        [universe] 840/901 (836 valid)
14:00:14  INFO        [universe] 880/901 (876 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260821T140131Z

- UTC timestamp: `20260821T140131Z`
- GitHub run: [#7744](https://github.com/28twagg-ops/TradingBot/actions/runs/32489804534)
- Run id: `32489804534`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`4s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260821T140131Z_live_bot.log`, `logs/action_runs/20260821T140131Z_live_options.log`, `logs/action_runs/20260821T140131Z_options_bot.log`

### Live bot (tail)

```text
14:01:33  INFO      Mode: exits
14:01:33  INFO        Daily log -> logs/daily/2026-08-21.md
14:01:33  INFO        Daily log reconciled -> logs/daily/2026-08-21.md (2 ledger rows)
14:01:33  INFO        place_all_stops: checking 5 positions...
14:01:33  INFO        STOP skipped AME: fractional (0.2433 shares) — software exit will handle it
14:01:33  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
14:01:34  INFO        [positions] 2/2 (2 valid)
14:01:34  INFO        Daily log -> logs/daily/2026-08-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $368.39|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L -0.0%  $-0.01                                            HOLD|
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
|  AMD260824C00502500      $0.62    $0.32    -48.4%   $-30.00   $32.00   |
|  COST260828C01000000     $0.63    $0.50    -20.6%   $-13.00   $50.00   |
|  WMT260821C00110000      $0.09    $0.00    -100.0%  $-9.00    $0.00    |
|                                                                        |
|  Options open P&L                                               $-52.00|
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
=== options_live_micro LIVE 2026-08-21T10:01:35.106321-04:00 share=50% ===
2026-08-21 10:01:35,106 INFO === options_live_micro LIVE 2026-08-21T10:01:35.106321-04:00 share=50% ===
Live account equity $368.39 cash $157.52 #225458845 options_level=3
2026-08-21 10:01:35,253 INFO Live account equity $368.39 cash $157.52 #225458845 options_level=3
Live micro sleeve $184 (50% of $368) deployed $82 open_strategies=0/4 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy)
2026-08-21 10:01:35,475 INFO Live micro sleeve $184 (50% of $368) deployed $82 open_strategies=0/4 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-21 10:01:35,475 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 4
2026-08-21 10:01:36,571 INFO Live micro signals: 4
  try S218 56%win/+49%med COST
2026-08-21 10:01:36,571 INFO   try S218 56%win/+49%med COST
LIVE BUY failed S218 COST: {"buy_limit_price":"0.61","code":40310000,"existing_order_id":"622ffbfc-8e23-41cb-900c-8ad08e486bd6","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.35"}
2026-08-21 10:01:37,185 INFO LIVE BUY failed S218 COST: {"buy_limit_price":"0.61","code":40310000,"existing_order_id":"622ffbfc-8e23-41cb-900c-8ad08e486bd6","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.35"}
  try S218 56%win/+49%med SYK
2026-08-21 10:01:37,185 INFO   try S218 56%win/+49%med SYK
  skip S218 SYK: no contract under $75
2026-08-21 10:01:37,417 INFO   skip S218 SYK: no contract under $75
  try S210 55%win/+47%med AMD
2026-08-21 10:01:37,417 INFO   try S210 55%win/+47%med AMD
LIVE BUY S210 55%win AMD AMD260824C00497500 limit=0.62 ask=0.63 cost=$63 id=d46f8249-4f0d-4167-bd7b-a6b0747ab0ab
2026-08-21 10:01:37,954 INFO LIVE BUY S210 55%win AMD AMD260824C00497500 limit=0.62 ask=0.63 cost=$63 id=d46f8249-4f0d-4167-bd7b-a6b0747ab0ab
  skip S210 COIN: strategy already open (paper bucket rule)
2026-08-21 10:01:37,955 INFO   skip S210 COIN: strategy already open (paper bucket rule)
Live micro done. open_options=4 lots=1
2026-08-21 10:01:38,058 INFO Live micro done. open_options=4 lots=1
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260821T140640Z

- UTC timestamp: `20260821T140640Z`
- GitHub run: [#7745](https://github.com/28twagg-ops/TradingBot/actions/runs/32490223904)
- Run id: `32490223904`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`5s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260821T140640Z_live_bot.log`, `logs/action_runs/20260821T140640Z_live_options.log`, `logs/action_runs/20260821T140640Z_options_bot.log`

### Live bot (tail)

```text
14:06:41  INFO      Mode: exits
14:06:42  INFO        Daily log -> logs/daily/2026-08-21.md
14:06:42  INFO        Daily log reconciled -> logs/daily/2026-08-21.md (3 ledger rows)
14:06:42  INFO        place_all_stops: checking 6 positions...
14:06:42  INFO        STOP skipped AME: fractional (0.2433 shares) — software exit will handle it
14:06:42  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
14:06:42  INFO        [positions] 2/2 (2 valid)
14:06:43  INFO        Daily log -> logs/daily/2026-08-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $355.34|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L -0.2%  $-0.12                                            HOLD|
|  AON  P&L +1.0%  $+0.67                                            HOLD|
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
|  AMD260824C00497500      $0.62    $0.52    -16.1%   $-10.00   $52.00   |
|  AMD260824C00502500      $0.62    $0.29    -53.2%   $-33.00   $29.00   |
|  COST260828C01000000     $0.63    $0.50    -20.6%   $-13.00   $50.00   |
|  WMT260821C00110000      $0.09    $0.00    -100.0%  $-9.00    $0.00    |
|                                                                        |
|  Options open P&L                                               $-65.00|
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
=== options_live_micro LIVE 2026-08-21T10:06:44.105633-04:00 share=50% ===
2026-08-21 10:06:44,105 INFO === options_live_micro LIVE 2026-08-21T10:06:44.105633-04:00 share=50% ===
Live account equity $355.34 cash $95.47 #225458845 options_level=3
2026-08-21 10:06:44,416 INFO Live account equity $355.34 cash $95.47 #225458845 options_level=3
Live micro fill confirmed S210 AMD260824C00497500
2026-08-21 10:06:44,489 INFO Live micro fill confirmed S210 AMD260824C00497500
Live micro hold S210 AMD260824C00497500 -16.1% (tp +50% / sl -40%)
2026-08-21 10:06:44,589 INFO Live micro hold S210 AMD260824C00497500 -16.1% (tp +50% / sl -40%)
LIVE PROT STOP AMD260824C00497500 x1 stop=0.37 id=75d65e1a-192d-4ee2-af7b-07262a798c38
2026-08-21 10:06:44,833 INFO LIVE PROT STOP AMD260824C00497500 x1 stop=0.37 id=75d65e1a-192d-4ee2-af7b-07262a798c38
Live micro sleeve $178 (50% of $355) deployed $131 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy)
2026-08-21 10:06:44,932 INFO Live micro sleeve $178 (50% of $355) deployed $131 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-21 10:06:44,932 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 4
2026-08-21 10:06:46,867 INFO Live micro signals: 4
  try S218 56%win/+49%med COST
2026-08-21 10:06:46,867 INFO   try S218 56%win/+49%med COST
  skip S218 COST: cost $58 > $47
2026-08-21 10:06:47,523 INFO   skip S218 COST: cost $58 > $47
  try S218 56%win/+49%med SYK
2026-08-21 10:06:47,523 INFO   try S218 56%win/+49%med SYK
  skip S218 SYK: no contract under $47
2026-08-21 10:06:47,762 INFO   skip S218 SYK: no contract under $47
  skip S210 AMD: strategy already open (paper bucket rule)
2026-08-21 10:06:47,762 INFO   skip S210 AMD: strategy already open (paper bucket rule)
  skip S210 COIN: strategy already open (paper bucket rule)
2026-08-21 10:06:47,762 INFO   skip S210 COIN: strategy already open (paper bucket rule)
Live micro done. open_options=4 lots=1
2026-08-21 10:06:48,022 INFO Live micro done. open_options=4 lots=1
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260821T141054Z

- UTC timestamp: `20260821T141054Z`
- GitHub run: [#7746](https://github.com/28twagg-ops/TradingBot/actions/runs/32490667789)
- Run id: `32490667789`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`3s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260821T141054Z_live_bot.log`, `logs/action_runs/20260821T141054Z_live_options.log`, `logs/action_runs/20260821T141054Z_options_bot.log`

### Live bot (tail)

```text
14:10:55  INFO      Mode: exits
14:10:56  INFO        Daily log -> logs/daily/2026-08-21.md
14:10:56  INFO        Daily log reconciled -> logs/daily/2026-08-21.md (3 ledger rows)
14:10:56  INFO        place_all_stops: checking 6 positions...
14:10:56  INFO        STOP skipped AME: fractional (0.2433 shares) — software exit will handle it
14:10:56  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
14:10:57  INFO        [positions] 2/2 (2 valid)
14:10:57  INFO        Daily log -> logs/daily/2026-08-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $343.47|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L -0.3%  $-0.18                                            HOLD|
|  AON  P&L +1.2%  $+0.85                                            HOLD|
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
|  AMD260824C00497500      $0.62    $0.44    -29.0%   $-18.00   $44.00   |
|  AMD260824C00502500      $0.62    $0.25    -59.7%   $-37.00   $25.00   |
|  COST260828C01000000     $0.63    $0.50    -20.6%   $-13.00   $50.00   |
|  WMT260821C00110000      $0.09    $0.00    -100.0%  $-9.00    $0.00    |
|                                                                        |
|  Options open P&L                                               $-77.00|
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
=== options_live_micro LIVE 2026-08-21T10:10:57.919419-04:00 share=50% ===
2026-08-21 10:10:57,919 INFO === options_live_micro LIVE 2026-08-21T10:10:57.919419-04:00 share=50% ===
Live account equity $343.47 cash $95.47 #225458845 options_level=3
2026-08-21 10:10:58,069 INFO Live account equity $343.47 cash $95.47 #225458845 options_level=3
Live micro hold S210 AMD260824C00497500 -29.0% (tp +50% / sl -40%)
2026-08-21 10:10:58,141 INFO Live micro hold S210 AMD260824C00497500 -29.0% (tp +50% / sl -40%)
Live micro sleeve $172 (50% of $343) deployed $119 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy)
2026-08-21 10:10:58,244 INFO Live micro sleeve $172 (50% of $343) deployed $119 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-21 10:10:58,245 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 4
2026-08-21 10:10:59,568 INFO Live micro signals: 4
  try S218 56%win/+49%med COST
2026-08-21 10:10:59,568 INFO   try S218 56%win/+49%med COST
  skip S218 COST: cost $61 > $53
2026-08-21 10:11:00,113 INFO   skip S218 COST: cost $61 > $53
  try S218 56%win/+49%med SYK
2026-08-21 10:11:00,113 INFO   try S218 56%win/+49%med SYK
  skip S218 SYK: no contract under $53
2026-08-21 10:11:00,288 INFO   skip S218 SYK: no contract under $53
  skip S210 AMD: strategy already open (paper bucket rule)
2026-08-21 10:11:00,288 INFO   skip S210 AMD: strategy already open (paper bucket rule)
  skip S210 COIN: strategy already open (paper bucket rule)
2026-08-21 10:11:00,288 INFO   skip S210 COIN: strategy already open (paper bucket rule)
Live micro done. open_options=4 lots=1
2026-08-21 10:11:00,386 INFO Live micro done. open_options=4 lots=1
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260821T141554Z

- UTC timestamp: `20260821T141554Z`
- GitHub run: [#7747](https://github.com/28twagg-ops/TradingBot/actions/runs/32491116190)
- Run id: `32491116190`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`8s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260821T141554Z_live_bot.log`, `logs/action_runs/20260821T141554Z_live_options.log`, `logs/action_runs/20260821T141554Z_options_bot.log`

### Live bot (tail)

```text
14:15:55  INFO      Mode: exits
14:15:57  INFO        Daily log -> logs/daily/2026-08-21.md
14:15:57  INFO        Daily log reconciled -> logs/daily/2026-08-21.md (3 ledger rows)
14:15:57  INFO        place_all_stops: checking 6 positions...
14:15:57  INFO        STOP skipped AME: fractional (0.2433 shares) — software exit will handle it
14:15:57  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
14:15:57  INFO        [positions] 2/2 (2 valid)
14:15:58  INFO        Daily log -> logs/daily/2026-08-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:15 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $332.63|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L -0.3%  $-0.19                                            HOLD|
|  AON  P&L +1.5%  $+1.04                                            HOLD|
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
|  AMD260824C00497500      $0.62    $0.33    -46.8%   $-29.00   $33.00   |
|  AMD260824C00502500      $0.62    $0.20    -67.7%   $-42.00   $20.00   |
|  COST260828C01000000     $0.63    $0.55    -12.7%   $-8.00    $55.00   |
|  WMT260821C00110000      $0.09    $0.00    -100.0%  $-9.00    $0.00    |
|                                                                        |
|  Options open P&L                                               $-88.00|
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
=== options_live_micro LIVE 2026-08-21T10:15:59.020550-04:00 share=50% ===
2026-08-21 10:15:59,020 INFO === options_live_micro LIVE 2026-08-21T10:15:59.020550-04:00 share=50% ===
Live account equity $332.63 cash $95.47 #225458845 options_level=3
2026-08-21 10:15:59,262 INFO Live account equity $332.63 cash $95.47 #225458845 options_level=3
LIVE EXIT stop_loss (-46.8%) AMD260824C00497500 x1 limit=0.34 id=97c2356d-3448-4946-ad52-087311fddb06
2026-08-21 10:16:03,046 INFO LIVE EXIT stop_loss (-46.8%) AMD260824C00497500 x1 limit=0.34 id=97c2356d-3448-4946-ad52-087311fddb06
Live micro sleeve $166 (50% of $333) deployed $75 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy)
2026-08-21 10:16:03,202 INFO Live micro sleeve $166 (50% of $333) deployed $75 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-21 10:16:03,202 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 4
2026-08-21 10:16:05,144 INFO Live micro signals: 4
  try S218 56%win/+49%med COST
2026-08-21 10:16:05,144 INFO   try S218 56%win/+49%med COST
LIVE BUY failed S218 COST: {"buy_limit_price":"0.61","code":40310000,"existing_order_id":"622ffbfc-8e23-41cb-900c-8ad08e486bd6","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.35"}
2026-08-21 10:16:05,965 INFO LIVE BUY failed S218 COST: {"buy_limit_price":"0.61","code":40310000,"existing_order_id":"622ffbfc-8e23-41cb-900c-8ad08e486bd6","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.35"}
  try S218 56%win/+49%med SYK
2026-08-21 10:16:05,965 INFO   try S218 56%win/+49%med SYK
  skip S218 SYK: no contract under $75
2026-08-21 10:16:06,262 INFO   skip S218 SYK: no contract under $75
  skip S210 AMD: strategy already open (paper bucket rule)
2026-08-21 10:16:06,262 INFO   skip S210 AMD: strategy already open (paper bucket rule)
  skip S210 COIN: strategy already open (paper bucket rule)
2026-08-21 10:16:06,262 INFO   skip S210 COIN: strategy already open (paper bucket rule)
Live micro done. open_options=3 lots=0
2026-08-21 10:16:06,433 INFO Live micro done. open_options=3 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260821T142210Z

- UTC timestamp: `20260821T142210Z`
- GitHub run: [#7748](https://github.com/28twagg-ops/TradingBot/actions/runs/32491570356)
- Run id: `32491570356`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`4s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260821T142210Z_live_bot.log`, `logs/action_runs/20260821T142210Z_live_options.log`, `logs/action_runs/20260821T142210Z_options_bot.log`

### Live bot (tail)

```text
14:22:12  INFO      Mode: exits
14:22:12  INFO        Daily log -> logs/daily/2026-08-21.md
14:22:12  INFO        Daily log reconciled -> logs/daily/2026-08-21.md (3 ledger rows)
14:22:12  INFO        place_all_stops: checking 5 positions...
14:22:12  INFO        STOP skipped AME: fractional (0.2433 shares) — software exit will handle it
14:22:12  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
14:22:12  INFO        [positions] 2/2 (2 valid)
14:22:12  INFO        Daily log -> logs/daily/2026-08-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:22 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $333.70|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L -0.3%  $-0.15                                            HOLD|
|  AON  P&L +1.6%  $+1.11                                            HOLD|
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
|  AMD260824C00502500      $0.62    $0.15    -75.8%   $-47.00   $15.00   |
|  COST260828C01000000     $0.63    $0.60    -4.8%    $-3.00    $60.00   |
|  WMT260821C00110000      $0.09    $0.00    -100.0%  $-9.00    $0.00    |
|                                                                        |
|  Options open P&L                                               $-59.00|
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
=== options_live_micro LIVE 2026-08-21T10:22:13.629771-04:00 share=50% ===
2026-08-21 10:22:13,629 INFO === options_live_micro LIVE 2026-08-21T10:22:13.629771-04:00 share=50% ===
Live account equity $333.70 cash $129.42 #225458845 options_level=3
2026-08-21 10:22:13,753 INFO Live account equity $333.70 cash $129.42 #225458845 options_level=3
Live micro sleeve $167 (50% of $334) deployed $75 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy)
2026-08-21 10:22:13,849 INFO Live micro sleeve $167 (50% of $334) deployed $75 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-21 10:22:13,849 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 4
2026-08-21 10:22:15,499 INFO Live micro signals: 4
  try S218 56%win/+49%med COST
2026-08-21 10:22:15,500 INFO   try S218 56%win/+49%med COST
LIVE BUY failed S218 COST: {"buy_limit_price":"0.65","code":40310000,"existing_order_id":"622ffbfc-8e23-41cb-900c-8ad08e486bd6","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.35"}
2026-08-21 10:22:15,802 INFO LIVE BUY failed S218 COST: {"buy_limit_price":"0.65","code":40310000,"existing_order_id":"622ffbfc-8e23-41cb-900c-8ad08e486bd6","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.35"}
  try S218 56%win/+49%med SYK
2026-08-21 10:22:15,803 INFO   try S218 56%win/+49%med SYK
  skip S218 SYK: no contract under $75
2026-08-21 10:22:15,947 INFO   skip S218 SYK: no contract under $75
  skip S210 AMD: strategy already open (paper bucket rule)
2026-08-21 10:22:15,947 INFO   skip S210 AMD: strategy already open (paper bucket rule)
  skip S210 COIN: strategy already open (paper bucket rule)
2026-08-21 10:22:15,947 INFO   skip S210 COIN: strategy already open (paper bucket rule)
Live micro done. open_options=3 lots=0
2026-08-21 10:22:16,002 INFO Live micro done. open_options=3 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260821T142550Z

- UTC timestamp: `20260821T142550Z`
- GitHub run: [#7749](https://github.com/28twagg-ops/TradingBot/actions/runs/32492018521)
- Run id: `32492018521`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`3s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260821T142550Z_live_bot.log`, `logs/action_runs/20260821T142550Z_live_options.log`, `logs/action_runs/20260821T142550Z_options_bot.log`

### Live bot (tail)

```text
14:25:51  INFO      Mode: exits
14:25:52  INFO        Daily log -> logs/daily/2026-08-21.md
14:25:52  INFO        Daily log reconciled -> logs/daily/2026-08-21.md (3 ledger rows)
14:25:52  INFO        place_all_stops: checking 5 positions...
14:25:52  INFO        STOP skipped AME: fractional (0.2433 shares) — software exit will handle it
14:25:52  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
14:25:52  INFO        [positions] 2/2 (2 valid)
14:25:52  INFO        Daily log -> logs/daily/2026-08-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:25 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $334.76|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L -0.1%  $-0.06                                            HOLD|
|  AON  P&L +1.6%  $+1.09                                            HOLD|
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
|  AMD260824C00502500      $0.62    $0.15    -75.8%   $-47.00   $15.00   |
|  COST260828C01000000     $0.63    $0.61    -3.2%    $-2.00    $61.00   |
|  WMT260821C00110000      $0.09    $0.00    -100.0%  $-9.00    $0.00    |
|                                                                        |
|  Options open P&L                                               $-58.00|
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
=== options_live_micro LIVE 2026-08-21T10:25:53.353055-04:00 share=50% ===
2026-08-21 10:25:53,353 INFO === options_live_micro LIVE 2026-08-21T10:25:53.353055-04:00 share=50% ===
Live account equity $334.76 cash $129.42 #225458845 options_level=3
2026-08-21 10:25:53,412 INFO Live account equity $334.76 cash $129.42 #225458845 options_level=3
Live micro sleeve $167 (50% of $335) deployed $76 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy)
2026-08-21 10:25:53,469 INFO Live micro sleeve $167 (50% of $335) deployed $76 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-21 10:25:53,470 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 4
2026-08-21 10:25:55,109 INFO Live micro signals: 4
  try S218 56%win/+49%med COST
2026-08-21 10:25:55,109 INFO   try S218 56%win/+49%med COST
LIVE BUY failed S218 COST: {"buy_limit_price":"0.67","code":40310000,"existing_order_id":"622ffbfc-8e23-41cb-900c-8ad08e486bd6","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.35"}
2026-08-21 10:25:55,323 INFO LIVE BUY failed S218 COST: {"buy_limit_price":"0.67","code":40310000,"existing_order_id":"622ffbfc-8e23-41cb-900c-8ad08e486bd6","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.35"}
  try S218 56%win/+49%med SYK
2026-08-21 10:25:55,323 INFO   try S218 56%win/+49%med SYK
  skip S218 SYK: no contract under $75
2026-08-21 10:25:55,409 INFO   skip S218 SYK: no contract under $75
  skip S210 AMD: strategy already open (paper bucket rule)
2026-08-21 10:25:55,410 INFO   skip S210 AMD: strategy already open (paper bucket rule)
  skip S210 COIN: strategy already open (paper bucket rule)
2026-08-21 10:25:55,410 INFO   skip S210 COIN: strategy already open (paper bucket rule)
Live micro done. open_options=3 lots=0
2026-08-21 10:25:55,435 INFO Live micro done. open_options=3 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260821T143053Z

- UTC timestamp: `20260821T143053Z`
- GitHub run: [#7750](https://github.com/28twagg-ops/TradingBot/actions/runs/32492467254)
- Run id: `32492467254`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`5s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260821T143053Z_live_bot.log`, `logs/action_runs/20260821T143053Z_live_options.log`, `logs/action_runs/20260821T143053Z_options_bot.log`

### Live bot (tail)

```text
14:30:54  INFO      Mode: exits
14:30:55  INFO        Daily log -> logs/daily/2026-08-21.md
14:30:55  INFO        Daily log reconciled -> logs/daily/2026-08-21.md (3 ledger rows)
14:30:55  INFO        place_all_stops: checking 5 positions...
14:30:55  INFO        STOP skipped AME: fractional (0.2433 shares) — software exit will handle it
14:30:55  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
14:30:56  INFO        [positions] 2/2 (2 valid)
14:30:56  INFO        Daily log -> logs/daily/2026-08-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:30 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $326.65|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L -0.2%  $-0.13                                            HOLD|
|  AON  P&L +1.5%  $+1.04                                            HOLD|
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
|  AMD260824C00502500      $0.62    $0.15    -75.8%   $-47.00   $15.00   |
|  COST260828C01000000     $0.63    $0.53    -15.9%   $-10.00   $53.00   |
|  WMT260821C00110000      $0.09    $0.00    -100.0%  $-9.00    $0.00    |
|                                                                        |
|  Options open P&L                                               $-66.00|
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
=== options_live_micro LIVE 2026-08-21T10:30:57.323024-04:00 share=50% ===
2026-08-21 10:30:57,323 INFO === options_live_micro LIVE 2026-08-21T10:30:57.323024-04:00 share=50% ===
Live account equity $326.65 cash $129.42 #225458845 options_level=3
2026-08-21 10:30:57,558 INFO Live account equity $326.65 cash $129.42 #225458845 options_level=3
Live micro sleeve $163 (50% of $327) deployed $68 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy)
2026-08-21 10:30:57,851 INFO Live micro sleeve $163 (50% of $327) deployed $68 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-21 10:30:57,852 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 4
2026-08-21 10:30:59,767 INFO Live micro signals: 4
  try S218 56%win/+49%med COST
2026-08-21 10:30:59,767 INFO   try S218 56%win/+49%med COST
LIVE BUY failed S218 COST: {"buy_limit_price":"0.64","code":40310000,"existing_order_id":"622ffbfc-8e23-41cb-900c-8ad08e486bd6","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.35"}
2026-08-21 10:31:00,618 INFO LIVE BUY failed S218 COST: {"buy_limit_price":"0.64","code":40310000,"existing_order_id":"622ffbfc-8e23-41cb-900c-8ad08e486bd6","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.35"}
  try S218 56%win/+49%med SYK
2026-08-21 10:31:00,618 INFO   try S218 56%win/+49%med SYK
  skip S218 SYK: no contract under $75
2026-08-21 10:31:00,985 INFO   skip S218 SYK: no contract under $75
  skip S210 AMD: strategy already open (paper bucket rule)
2026-08-21 10:31:00,985 INFO   skip S210 AMD: strategy already open (paper bucket rule)
  skip S210 COIN: strategy already open (paper bucket rule)
2026-08-21 10:31:00,986 INFO   skip S210 COIN: strategy already open (paper bucket rule)
Live micro done. open_options=3 lots=0
2026-08-21 10:31:01,128 INFO Live micro done. open_options=3 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260821T143554Z

- UTC timestamp: `20260821T143554Z`
- GitHub run: [#7751](https://github.com/28twagg-ops/TradingBot/actions/runs/32492918480)
- Run id: `32492918480`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`4s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260821T143554Z_live_bot.log`, `logs/action_runs/20260821T143554Z_live_options.log`, `logs/action_runs/20260821T143554Z_options_bot.log`

### Live bot (tail)

```text
14:35:55  INFO      Mode: exits
14:35:56  INFO        Daily log -> logs/daily/2026-08-21.md
14:35:56  INFO        Daily log reconciled -> logs/daily/2026-08-21.md (3 ledger rows)
14:35:56  INFO        place_all_stops: checking 5 positions...
14:35:56  INFO        STOP skipped AME: fractional (0.2433 shares) — software exit will handle it
14:35:56  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
14:35:58  INFO        [positions] 2/2 (2 valid)
14:35:58  INFO        Daily log -> logs/daily/2026-08-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:35 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $331.63|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L -0.2%  $-0.13                                            HOLD|
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
|  AMD260824C00502500      $0.62    $0.19    -69.4%   $-43.00   $19.00   |
|  COST260828C01000000     $0.63    $0.54    -14.3%   $-9.00    $54.00   |
|  WMT260821C00110000      $0.09    $0.00    -100.0%  $-9.00    $0.00    |
|                                                                        |
|  Options open P&L                                               $-61.00|
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
=== options_live_micro LIVE 2026-08-21T10:35:59.184675-04:00 share=50% ===
2026-08-21 10:35:59,184 INFO === options_live_micro LIVE 2026-08-21T10:35:59.184675-04:00 share=50% ===
Live account equity $331.63 cash $129.42 #225458845 options_level=3
2026-08-21 10:35:59,555 INFO Live account equity $331.63 cash $129.42 #225458845 options_level=3
Live micro sleeve $166 (50% of $332) deployed $73 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy)
2026-08-21 10:35:59,836 INFO Live micro sleeve $166 (50% of $332) deployed $73 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-21 10:35:59,836 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 4
2026-08-21 10:36:01,474 INFO Live micro signals: 4
  try S218 56%win/+49%med COST
2026-08-21 10:36:01,475 INFO   try S218 56%win/+49%med COST
LIVE BUY failed S218 COST: {"buy_limit_price":"0.56","code":40310000,"existing_order_id":"622ffbfc-8e23-41cb-900c-8ad08e486bd6","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.35"}
2026-08-21 10:36:02,269 INFO LIVE BUY failed S218 COST: {"buy_limit_price":"0.56","code":40310000,"existing_order_id":"622ffbfc-8e23-41cb-900c-8ad08e486bd6","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.35"}
  try S218 56%win/+49%med SYK
2026-08-21 10:36:02,269 INFO   try S218 56%win/+49%med SYK
  skip S218 SYK: no contract under $75
2026-08-21 10:36:02,650 INFO   skip S218 SYK: no contract under $75
  skip S210 AMD: strategy already open (paper bucket rule)
2026-08-21 10:36:02,650 INFO   skip S210 AMD: strategy already open (paper bucket rule)
  skip S210 COIN: strategy already open (paper bucket rule)
2026-08-21 10:36:02,650 INFO   skip S210 COIN: strategy already open (paper bucket rule)
Live micro done. open_options=3 lots=0
2026-08-21 10:36:02,785 INFO Live micro done. open_options=3 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260821T144052Z

- UTC timestamp: `20260821T144052Z`
- GitHub run: [#7752](https://github.com/28twagg-ops/TradingBot/actions/runs/32493365511)
- Run id: `32493365511`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`3s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260821T144052Z_live_bot.log`, `logs/action_runs/20260821T144052Z_live_options.log`, `logs/action_runs/20260821T144052Z_options_bot.log`

### Live bot (tail)

```text
14:40:53  INFO      Mode: exits
14:40:53  INFO        Daily log -> logs/daily/2026-08-21.md
14:40:53  INFO        Daily log reconciled -> logs/daily/2026-08-21.md (3 ledger rows)
14:40:53  INFO        place_all_stops: checking 5 positions...
14:40:53  INFO        STOP skipped AME: fractional (0.2433 shares) — software exit will handle it
14:40:53  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
14:40:53  INFO        [positions] 2/2 (2 valid)
14:40:54  INFO        Daily log -> logs/daily/2026-08-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:40 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $330.60|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L -0.4%  $-0.24                                            HOLD|
|  AON  P&L +1.6%  $+1.10                                            HOLD|
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
|  AMD260824C00502500      $0.62    $0.19    -69.4%   $-43.00   $19.00   |
|  COST260828C01000000     $0.63    $0.53    -15.9%   $-10.00   $53.00   |
|  WMT260821C00110000      $0.09    $0.00    -100.0%  $-9.00    $0.00    |
|                                                                        |
|  Options open P&L                                               $-62.00|
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
=== options_live_micro LIVE 2026-08-21T10:40:54.896028-04:00 share=50% ===
2026-08-21 10:40:54,896 INFO === options_live_micro LIVE 2026-08-21T10:40:54.896028-04:00 share=50% ===
Live account equity $330.60 cash $129.42 #225458845 options_level=3
2026-08-21 10:40:54,964 INFO Live account equity $330.60 cash $129.42 #225458845 options_level=3
Live micro sleeve $165 (50% of $331) deployed $72 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy)
2026-08-21 10:40:55,020 INFO Live micro sleeve $165 (50% of $331) deployed $72 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-21 10:40:55,021 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 4
2026-08-21 10:40:56,685 INFO Live micro signals: 4
  try S218 56%win/+49%med COST
2026-08-21 10:40:56,685 INFO   try S218 56%win/+49%med COST
LIVE BUY failed S218 COST: {"buy_limit_price":"0.63","code":40310000,"existing_order_id":"622ffbfc-8e23-41cb-900c-8ad08e486bd6","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.35"}
2026-08-21 10:40:57,082 INFO LIVE BUY failed S218 COST: {"buy_limit_price":"0.63","code":40310000,"existing_order_id":"622ffbfc-8e23-41cb-900c-8ad08e486bd6","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.35"}
  try S218 56%win/+49%med SYK
2026-08-21 10:40:57,082 INFO   try S218 56%win/+49%med SYK
  skip S218 SYK: no contract under $75
2026-08-21 10:40:57,210 INFO   skip S218 SYK: no contract under $75
  skip S210 AMD: strategy already open (paper bucket rule)
2026-08-21 10:40:57,211 INFO   skip S210 AMD: strategy already open (paper bucket rule)
  skip S210 COIN: strategy already open (paper bucket rule)
2026-08-21 10:40:57,211 INFO   skip S210 COIN: strategy already open (paper bucket rule)
Live micro done. open_options=3 lots=0
2026-08-21 10:40:57,237 INFO Live micro done. open_options=3 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---
