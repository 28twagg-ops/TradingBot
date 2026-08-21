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

## Run 20260821T144555Z

- UTC timestamp: `20260821T144555Z`
- GitHub run: [#7753](https://github.com/28twagg-ops/TradingBot/actions/runs/32493818324)
- Run id: `32493818324`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`5s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260821T144555Z_live_bot.log`, `logs/action_runs/20260821T144555Z_live_options.log`, `logs/action_runs/20260821T144555Z_options_bot.log`

### Live bot (tail)

```text
14:45:56  INFO      Mode: exits
14:45:57  INFO        Daily log -> logs/daily/2026-08-21.md
14:45:57  INFO        Daily log reconciled -> logs/daily/2026-08-21.md (3 ledger rows)
14:45:57  INFO        place_all_stops: checking 5 positions...
14:45:57  INFO        STOP skipped AME: fractional (0.2433 shares) — software exit will handle it
14:45:57  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
14:45:58  INFO        [positions] 2/2 (2 valid)
14:45:58  INFO        Daily log -> logs/daily/2026-08-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:45 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $326.52|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L -0.4%  $-0.25                                            HOLD|
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
|  AMD260824C00502500      $0.62    $0.18    -71.0%   $-44.00   $18.00   |
|  COST260828C01000000     $0.63    $0.50    -20.6%   $-13.00   $50.00   |
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
=== options_live_micro LIVE 2026-08-21T10:45:59.629160-04:00 share=50% ===
2026-08-21 10:45:59,629 INFO === options_live_micro LIVE 2026-08-21T10:45:59.629160-04:00 share=50% ===
Live account equity $326.48 cash $129.42 #225458845 options_level=3
2026-08-21 10:45:59,831 INFO Live account equity $326.48 cash $129.42 #225458845 options_level=3
Live micro sleeve $163 (50% of $326) deployed $68 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy)
2026-08-21 10:46:00,100 INFO Live micro sleeve $163 (50% of $326) deployed $68 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-21 10:46:00,100 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 4
2026-08-21 10:46:01,956 INFO Live micro signals: 4
  try S218 56%win/+49%med COST
2026-08-21 10:46:01,956 INFO   try S218 56%win/+49%med COST
LIVE BUY failed S218 COST: {"buy_limit_price":"0.6","code":40310000,"existing_order_id":"622ffbfc-8e23-41cb-900c-8ad08e486bd6","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.35"}
2026-08-21 10:46:02,720 INFO LIVE BUY failed S218 COST: {"buy_limit_price":"0.6","code":40310000,"existing_order_id":"622ffbfc-8e23-41cb-900c-8ad08e486bd6","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.35"}
  try S218 56%win/+49%med SYK
2026-08-21 10:46:02,720 INFO   try S218 56%win/+49%med SYK
  skip S218 SYK: no contract under $75
2026-08-21 10:46:02,976 INFO   skip S218 SYK: no contract under $75
  skip S210 AMD: strategy already open (paper bucket rule)
2026-08-21 10:46:02,976 INFO   skip S210 AMD: strategy already open (paper bucket rule)
  skip S210 COIN: strategy already open (paper bucket rule)
2026-08-21 10:46:02,977 INFO   skip S210 COIN: strategy already open (paper bucket rule)
Live micro done. open_options=3 lots=0
2026-08-21 10:46:03,140 INFO Live micro done. open_options=3 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260821T145049Z

- UTC timestamp: `20260821T145049Z`
- GitHub run: [#7754](https://github.com/28twagg-ops/TradingBot/actions/runs/32494278766)
- Run id: `32494278766`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`3s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260821T145049Z_live_bot.log`, `logs/action_runs/20260821T145049Z_live_options.log`, `logs/action_runs/20260821T145049Z_options_bot.log`

### Live bot (tail)

```text
14:50:51  INFO      Mode: exits
14:50:51  INFO        Daily log -> logs/daily/2026-08-21.md
14:50:51  INFO        Daily log reconciled -> logs/daily/2026-08-21.md (3 ledger rows)
14:50:51  INFO        place_all_stops: checking 5 positions...
14:50:51  INFO        STOP skipped AME: fractional (0.2433 shares) — software exit will handle it
14:50:51  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
14:50:52  INFO        [positions] 2/2 (2 valid)
14:50:52  INFO        Daily log -> logs/daily/2026-08-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:50 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $331.63|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L -0.4%  $-0.21                                            HOLD|
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
|  AMD260824C00502500      $0.62    $0.18    -71.0%   $-44.00   $18.00   |
|  COST260828C01000000     $0.63    $0.55    -12.7%   $-8.00    $55.00   |
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
=== options_live_micro LIVE 2026-08-21T10:50:53.034640-04:00 share=50% ===
2026-08-21 10:50:53,034 INFO === options_live_micro LIVE 2026-08-21T10:50:53.034640-04:00 share=50% ===
Live account equity $331.63 cash $129.42 #225458845 options_level=3
2026-08-21 10:50:53,098 INFO Live account equity $331.63 cash $129.42 #225458845 options_level=3
Live micro sleeve $166 (50% of $332) deployed $73 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy)
2026-08-21 10:50:53,153 INFO Live micro sleeve $166 (50% of $332) deployed $73 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-21 10:50:53,153 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 4
2026-08-21 10:50:54,798 INFO Live micro signals: 4
  try S218 56%win/+49%med COST
2026-08-21 10:50:54,798 INFO   try S218 56%win/+49%med COST
LIVE BUY failed S218 COST: {"buy_limit_price":"0.6","code":40310000,"existing_order_id":"622ffbfc-8e23-41cb-900c-8ad08e486bd6","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.35"}
2026-08-21 10:50:55,053 INFO LIVE BUY failed S218 COST: {"buy_limit_price":"0.6","code":40310000,"existing_order_id":"622ffbfc-8e23-41cb-900c-8ad08e486bd6","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.35"}
  try S218 56%win/+49%med SYK
2026-08-21 10:50:55,053 INFO   try S218 56%win/+49%med SYK
  skip S218 SYK: no contract under $75
2026-08-21 10:50:55,180 INFO   skip S218 SYK: no contract under $75
  skip S210 AMD: strategy already open (paper bucket rule)
2026-08-21 10:50:55,180 INFO   skip S210 AMD: strategy already open (paper bucket rule)
  skip S210 COIN: strategy already open (paper bucket rule)
2026-08-21 10:50:55,181 INFO   skip S210 COIN: strategy already open (paper bucket rule)
Live micro done. open_options=3 lots=0
2026-08-21 10:50:55,206 INFO Live micro done. open_options=3 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260821T150012Z

- UTC timestamp: `20260821T150012Z`
- GitHub run: [#7755](https://github.com/28twagg-ops/TradingBot/actions/runs/32494738255)
- Run id: `32494738255`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`4s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260821T150012Z_live_bot.log`, `logs/action_runs/20260821T150012Z_live_options.log`, `logs/action_runs/20260821T150012Z_options_bot.log`

### Live bot (tail)

```text
15:00:14  INFO      Mode: exits
15:00:14  INFO        Daily log -> logs/daily/2026-08-21.md
15:00:14  INFO        Daily log reconciled -> logs/daily/2026-08-21.md (3 ledger rows)
15:00:14  INFO        place_all_stops: checking 5 positions...
15:00:14  INFO        STOP skipped AME: fractional (0.2433 shares) — software exit will handle it
15:00:14  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
15:00:14  INFO        [positions] 2/2 (2 valid)
15:00:15  INFO        Daily log -> logs/daily/2026-08-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:00 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $327.61|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L -0.5%  $-0.26                                            HOLD|
|  AON  P&L +1.6%  $+1.13                                            HOLD|
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
|  AMD260824C00502500      $0.62    $0.14    -77.4%   $-48.00   $14.00   |
|  COST260828C01000000     $0.63    $0.55    -12.7%   $-8.00    $55.00   |
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
=== options_live_micro LIVE 2026-08-21T11:00:15.796380-04:00 share=50% ===
2026-08-21 11:00:15,796 INFO === options_live_micro LIVE 2026-08-21T11:00:15.796380-04:00 share=50% ===
Live account equity $327.61 cash $129.42 #225458845 options_level=3
2026-08-21 11:00:15,886 INFO Live account equity $327.61 cash $129.42 #225458845 options_level=3
Live micro sleeve $164 (50% of $328) deployed $69 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy)
2026-08-21 11:00:15,991 INFO Live micro sleeve $164 (50% of $328) deployed $69 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-21 11:00:15,991 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 4
2026-08-21 11:00:17,669 INFO Live micro signals: 4
  try S218 56%win/+49%med COST
2026-08-21 11:00:17,669 INFO   try S218 56%win/+49%med COST
LIVE BUY failed S218 COST: {"buy_limit_price":"0.63","code":40310000,"existing_order_id":"622ffbfc-8e23-41cb-900c-8ad08e486bd6","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.35"}
2026-08-21 11:00:18,604 INFO LIVE BUY failed S218 COST: {"buy_limit_price":"0.63","code":40310000,"existing_order_id":"622ffbfc-8e23-41cb-900c-8ad08e486bd6","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.35"}
  try S218 56%win/+49%med SYK
2026-08-21 11:00:18,604 INFO   try S218 56%win/+49%med SYK
  skip S218 SYK: no contract under $75
2026-08-21 11:00:19,168 INFO   skip S218 SYK: no contract under $75
  skip S210 AMD: strategy already open (paper bucket rule)
2026-08-21 11:00:19,168 INFO   skip S210 AMD: strategy already open (paper bucket rule)
  skip S210 COIN: strategy already open (paper bucket rule)
2026-08-21 11:00:19,168 INFO   skip S210 COIN: strategy already open (paper bucket rule)
Live micro done. open_options=3 lots=0
2026-08-21 11:00:19,219 INFO Live micro done. open_options=3 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260821T150119Z

- UTC timestamp: `20260821T150119Z`
- GitHub run: [#7756](https://github.com/28twagg-ops/TradingBot/actions/runs/32495200143)
- Run id: `32495200143`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`3s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260821T150119Z_live_bot.log`, `logs/action_runs/20260821T150119Z_live_options.log`, `logs/action_runs/20260821T150119Z_options_bot.log`

### Live bot (tail)

```text
15:01:20  INFO      Mode: exits
15:01:21  INFO        Daily log -> logs/daily/2026-08-21.md
15:01:21  INFO        Daily log reconciled -> logs/daily/2026-08-21.md (3 ledger rows)
15:01:21  INFO        place_all_stops: checking 5 positions...
15:01:21  INFO        STOP skipped AME: fractional (0.2433 shares) — software exit will handle it
15:01:21  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
15:01:21  INFO        [positions] 2/2 (2 valid)
15:01:21  INFO        Daily log -> logs/daily/2026-08-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $327.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L -0.5%  $-0.28                                            HOLD|
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
|  AMD260824C00502500      $0.62    $0.14    -77.4%   $-48.00   $14.00   |
|  COST260828C01000000     $0.63    $0.55    -12.7%   $-8.00    $55.00   |
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
=== options_live_micro LIVE 2026-08-21T11:01:22.195599-04:00 share=50% ===
2026-08-21 11:01:22,195 INFO === options_live_micro LIVE 2026-08-21T11:01:22.195599-04:00 share=50% ===
Live account equity $327.56 cash $129.42 #225458845 options_level=3
2026-08-21 11:01:22,269 INFO Live account equity $327.56 cash $129.42 #225458845 options_level=3
Live micro sleeve $164 (50% of $328) deployed $69 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy)
2026-08-21 11:01:22,340 INFO Live micro sleeve $164 (50% of $328) deployed $69 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-21 11:01:22,340 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 4
2026-08-21 11:01:24,006 INFO Live micro signals: 4
  try S218 56%win/+49%med COST
2026-08-21 11:01:24,007 INFO   try S218 56%win/+49%med COST
LIVE BUY failed S218 COST: {"buy_limit_price":"0.63","code":40310000,"existing_order_id":"622ffbfc-8e23-41cb-900c-8ad08e486bd6","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.35"}
2026-08-21 11:01:24,355 INFO LIVE BUY failed S218 COST: {"buy_limit_price":"0.63","code":40310000,"existing_order_id":"622ffbfc-8e23-41cb-900c-8ad08e486bd6","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.35"}
  try S218 56%win/+49%med SYK
2026-08-21 11:01:24,355 INFO   try S218 56%win/+49%med SYK
  skip S218 SYK: no contract under $75
2026-08-21 11:01:24,517 INFO   skip S218 SYK: no contract under $75
  skip S210 AMD: strategy already open (paper bucket rule)
2026-08-21 11:01:24,517 INFO   skip S210 AMD: strategy already open (paper bucket rule)
  skip S210 COIN: strategy already open (paper bucket rule)
2026-08-21 11:01:24,517 INFO   skip S210 COIN: strategy already open (paper bucket rule)
Live micro done. open_options=3 lots=0
2026-08-21 11:01:24,549 INFO Live micro done. open_options=3 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260821T150553Z

- UTC timestamp: `20260821T150553Z`
- GitHub run: [#7757](https://github.com/28twagg-ops/TradingBot/actions/runs/32495661586)
- Run id: `32495661586`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`3s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260821T150553Z_live_bot.log`, `logs/action_runs/20260821T150553Z_live_options.log`, `logs/action_runs/20260821T150553Z_options_bot.log`

### Live bot (tail)

```text
15:05:54  INFO      Mode: exits
15:05:55  INFO        Daily log -> logs/daily/2026-08-21.md
15:05:55  INFO        Daily log reconciled -> logs/daily/2026-08-21.md (3 ledger rows)
15:05:55  INFO        place_all_stops: checking 5 positions...
15:05:55  INFO        STOP skipped AME: fractional (0.2433 shares) — software exit will handle it
15:05:55  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
15:05:55  INFO        [positions] 2/2 (2 valid)
15:05:55  INFO        SELL MARKET [urgent] AME closed
15:05:57  INFO        TX logged: SELL AME  P&L -0.65%
15:05:57  INFO        Daily log -> logs/daily/2026-08-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:05 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $328.36|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L -0.6%  $-0.38                         EXIT: stop_loss (-0.6%)|
|  AON  P&L +1.4%  $+1.00                                            HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AMD260824C00502500      $0.62    $0.14    -77.4%   $-48.00   $14.00   |
|  COST260828C01000000     $0.63    $0.56    -11.1%   $-7.00    $56.00   |
|  WMT260821C00110000      $0.09    $0.00    -100.0%  $-9.00    $0.00    |
|                                                                        |
|  Options open P&L                                               $-64.00|
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  AME                                         -0.65%  (threshold -0.50%)|
|  Count                                                                1|
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-21T11:05:58.156844-04:00 share=50% ===
2026-08-21 11:05:58,156 INFO === options_live_micro LIVE 2026-08-21T11:05:58.156844-04:00 share=50% ===
Live account equity $328.38 cash $187.42 #225458845 options_level=3
2026-08-21 11:05:58,223 INFO Live account equity $328.38 cash $187.42 #225458845 options_level=3
Live micro sleeve $164 (50% of $328) deployed $70 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy)
2026-08-21 11:05:58,305 INFO Live micro sleeve $164 (50% of $328) deployed $70 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-21 11:05:58,306 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 4
2026-08-21 11:06:00,195 INFO Live micro signals: 4
  try S218 56%win/+49%med COST
2026-08-21 11:06:00,195 INFO   try S218 56%win/+49%med COST
LIVE BUY failed S218 COST: {"buy_limit_price":"0.54","code":40310000,"existing_order_id":"622ffbfc-8e23-41cb-900c-8ad08e486bd6","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.35"}
2026-08-21 11:06:00,421 INFO LIVE BUY failed S218 COST: {"buy_limit_price":"0.54","code":40310000,"existing_order_id":"622ffbfc-8e23-41cb-900c-8ad08e486bd6","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.35"}
  try S218 56%win/+49%med SYK
2026-08-21 11:06:00,421 INFO   try S218 56%win/+49%med SYK
  skip S218 SYK: no contract under $75
2026-08-21 11:06:00,691 INFO   skip S218 SYK: no contract under $75
  skip S210 AMD: strategy already open (paper bucket rule)
2026-08-21 11:06:00,691 INFO   skip S210 AMD: strategy already open (paper bucket rule)
  skip S210 COIN: strategy already open (paper bucket rule)
2026-08-21 11:06:00,691 INFO   skip S210 COIN: strategy already open (paper bucket rule)
Live micro done. open_options=3 lots=0
2026-08-21 11:06:00,761 INFO Live micro done. open_options=3 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260821T151315Z

- UTC timestamp: `20260821T151315Z`
- GitHub run: [#7758](https://github.com/28twagg-ops/TradingBot/actions/runs/32496118480)
- Run id: `32496118480`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`3s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260821T151315Z_live_bot.log`, `logs/action_runs/20260821T151315Z_live_options.log`, `logs/action_runs/20260821T151315Z_options_bot.log`

### Live bot (tail)

```text
15:13:16  INFO      Mode: exits
15:13:17  INFO        Daily log -> logs/daily/2026-08-21.md
15:13:17  INFO        Daily log reconciled -> logs/daily/2026-08-21.md (4 ledger rows)
15:13:17  INFO        place_all_stops: checking 4 positions...
15:13:17  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
15:13:17  INFO        [positions] 1/1 (1 valid)
15:13:18  INFO        Daily log -> logs/daily/2026-08-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:13 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $322.21|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AON  P&L +1.2%  $+0.83                                            HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AMD260824C00502500      $0.62    $0.14    -77.4%   $-48.00   $14.00   |
|  COST260828C01000000     $0.63    $0.50    -20.6%   $-13.00   $50.00   |
|  WMT260821C00110000      $0.09    $0.00    -100.0%  $-9.00    $0.00    |
|                                                                        |
|  Options open P&L                                               $-70.00|
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
=== options_live_micro LIVE 2026-08-21T11:13:18.790568-04:00 share=50% ===
2026-08-21 11:13:18,790 INFO === options_live_micro LIVE 2026-08-21T11:13:18.790568-04:00 share=50% ===
Live account equity $322.21 cash $187.42 #225458845 options_level=3
2026-08-21 11:13:19,010 INFO Live account equity $322.21 cash $187.42 #225458845 options_level=3
Live micro sleeve $161 (50% of $322) deployed $64 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy)
2026-08-21 11:13:19,257 INFO Live micro sleeve $161 (50% of $322) deployed $64 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-21 11:13:19,257 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 4
2026-08-21 11:13:20,532 INFO Live micro signals: 4
  try S218 56%win/+49%med COST
2026-08-21 11:13:20,532 INFO   try S218 56%win/+49%med COST
LIVE BUY failed S218 COST: {"buy_limit_price":"0.6","code":40310000,"existing_order_id":"622ffbfc-8e23-41cb-900c-8ad08e486bd6","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.35"}
2026-08-21 11:13:21,170 INFO LIVE BUY failed S218 COST: {"buy_limit_price":"0.6","code":40310000,"existing_order_id":"622ffbfc-8e23-41cb-900c-8ad08e486bd6","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.35"}
  try S218 56%win/+49%med SYK
2026-08-21 11:13:21,171 INFO   try S218 56%win/+49%med SYK
  skip S218 SYK: no contract under $75
2026-08-21 11:13:21,406 INFO   skip S218 SYK: no contract under $75
  skip S210 AMD: strategy already open (paper bucket rule)
2026-08-21 11:13:21,406 INFO   skip S210 AMD: strategy already open (paper bucket rule)
  skip S210 COIN: strategy already open (paper bucket rule)
2026-08-21 11:13:21,406 INFO   skip S210 COIN: strategy already open (paper bucket rule)
Live micro done. open_options=3 lots=0
2026-08-21 11:13:21,529 INFO Live micro done. open_options=3 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260821T151550Z

- UTC timestamp: `20260821T151550Z`
- GitHub run: [#7759](https://github.com/28twagg-ops/TradingBot/actions/runs/32496573956)
- Run id: `32496573956`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`5s`
- Paper options: exit=`0`, duration=`68s`
- Full logs: `logs/action_runs/20260821T151550Z_live_bot.log`, `logs/action_runs/20260821T151550Z_live_options.log`, `logs/action_runs/20260821T151550Z_options_bot.log`


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
{"ts_et":"2026-08-21T11:16:00.011403-04:00","date":"2026-08-21","mode":"entry+manage","header":"entry+manage (1 new)","elapsed_s":59.9,"phases_s":{"reconcile":0.28,"cancel":0.1,"manage":0.14,"protective_stops":0.07,"scan":56.56,"entries":1.55,"reconcile2":0.29},"signals":4,"placed":1,"equity":1000000.0,"open_positions":1,"pending_orders":0,"open_lots":1,"submitted_today":1,"filled_today":1,"unattributed_contracts":0,"top_signals":["S210:AMD","S210:COIN","S218:SYK","S218:COST"],"github_run":"7759","github_run_id":"32496573956","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:15:51  INFO      Mode: exits
15:15:52  INFO        Daily log -> logs/daily/2026-08-21.md
15:15:52  INFO        Daily log reconciled -> logs/daily/2026-08-21.md (4 ledger rows)
15:15:52  INFO        place_all_stops: checking 4 positions...
15:15:52  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
15:15:53  INFO        [positions] 1/1 (1 valid)
15:15:53  INFO        Daily log -> logs/daily/2026-08-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:15 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $322.13|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AON  P&L +1.1%  $+0.75                                            HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AMD260824C00502500      $0.62    $0.14    -77.4%   $-48.00   $14.00   |
|  COST260828C01000000     $0.63    $0.50    -20.6%   $-13.00   $50.00   |
|  WMT260821C00110000      $0.09    $0.00    -100.0%  $-9.00    $0.00    |
|                                                                        |
|  Options open P&L                                               $-70.00|
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
=== options_live_micro LIVE 2026-08-21T11:15:54.380750-04:00 share=50% ===
2026-08-21 11:15:54,380 INFO === options_live_micro LIVE 2026-08-21T11:15:54.380750-04:00 share=50% ===
Live account equity $322.17 cash $187.42 #225458845 options_level=3
2026-08-21 11:15:54,615 INFO Live account equity $322.17 cash $187.42 #225458845 options_level=3
Live micro sleeve $161 (50% of $322) deployed $64 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy)
2026-08-21 11:15:54,915 INFO Live micro sleeve $161 (50% of $322) deployed $64 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-21 11:15:54,915 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 4
2026-08-21 11:15:56,848 INFO Live micro signals: 4
  try S218 56%win/+49%med COST
2026-08-21 11:15:56,849 INFO   try S218 56%win/+49%med COST
LIVE BUY failed S218 COST: {"buy_limit_price":"0.56","code":40310000,"existing_order_id":"622ffbfc-8e23-41cb-900c-8ad08e486bd6","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.35"}
2026-08-21 11:15:57,659 INFO LIVE BUY failed S218 COST: {"buy_limit_price":"0.56","code":40310000,"existing_order_id":"622ffbfc-8e23-41cb-900c-8ad08e486bd6","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.35"}
  try S218 56%win/+49%med SYK
2026-08-21 11:15:57,659 INFO   try S218 56%win/+49%med SYK
  skip S218 SYK: no contract under $75
2026-08-21 11:15:57,971 INFO   skip S218 SYK: no contract under $75
  skip S210 AMD: strategy already open (paper bucket rule)
2026-08-21 11:15:57,971 INFO   skip S210 AMD: strategy already open (paper bucket rule)
  skip S210 COIN: strategy already open (paper bucket rule)
2026-08-21 11:15:57,971 INFO   skip S210 COIN: strategy already open (paper bucket rule)
Live micro done. open_options=3 lots=0
2026-08-21 11:15:58,113 INFO Live micro done. open_options=3 lots=0
```

### Paper options bot (tail)

```text
... (172 earlier lines - see full log file)
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
## Ledger health — 2026-08-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   975 | WARN | <<<
| Missing exit records (post) |   975 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     1 | INFO |
| Total closed lots           |  1770 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=821 med=-47.5% | TAINTED n=1761 med=-39.3% | KEEP-only n=294 med=+37.5% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=322.17 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | MomReversal | 15 | 47% | +0.39% | -0.60% | -1.81% | 1.99 | 1.7d | $+3.53 | WATCH |
| 3 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260821T152054Z

- UTC timestamp: `20260821T152054Z`
- GitHub run: [#7760](https://github.com/28twagg-ops/TradingBot/actions/runs/32497018858)
- Run id: `32497018858`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`4s`
- Paper options: exit=`0`, duration=`59s`
- Full logs: `logs/action_runs/20260821T152054Z_live_bot.log`, `logs/action_runs/20260821T152054Z_live_options.log`, `logs/action_runs/20260821T152054Z_options_bot.log`


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
{"ts_et":"2026-08-21T11:21:01.621983-04:00","date":"2026-08-21","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":50.9,"phases_s":{"reconcile":0.23,"cancel":0.06,"manage":2.58,"protective_stops":0.11,"scan":46.56,"entries":0.72},"signals":4,"placed":0,"equity":999995.97,"open_positions":1,"pending_orders":0,"open_lots":1,"submitted_today":1,"filled_today":1,"unattributed_contracts":0,"top_signals":["S210:AMD","S210:COIN","S218:SYK","S218:COST"],"github_run":"7760","github_run_id":"32497018858","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:20:54  INFO      Mode: exits
15:20:55  INFO        Daily log -> logs/daily/2026-08-21.md
15:20:55  INFO        Daily log reconciled -> logs/daily/2026-08-21.md (4 ledger rows)
15:20:55  INFO        place_all_stops: checking 4 positions...
15:20:55  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
15:20:56  INFO        [positions] 1/1 (1 valid)
15:20:56  INFO        Daily log -> logs/daily/2026-08-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $322.21|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AON  P&L +1.2%  $+0.83                                            HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AMD260824C00502500      $0.62    $0.14    -77.4%   $-48.00   $14.00   |
|  COST260828C01000000     $0.63    $0.50    -20.6%   $-13.00   $50.00   |
|  WMT260821C00110000      $0.09    $0.00    -100.0%  $-9.00    $0.00    |
|                                                                        |
|  Options open P&L                                               $-70.00|
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
=== options_live_micro LIVE 2026-08-21T11:20:57.290054-04:00 share=25% ===
2026-08-21 11:20:57,290 INFO === options_live_micro LIVE 2026-08-21T11:20:57.290054-04:00 share=25% ===
Live account equity $322.21 cash $187.42 #225458845 options_level=3
2026-08-21 11:20:57,481 INFO Live account equity $322.21 cash $187.42 #225458845 options_level=3
Live micro orphan_adopt AMD260824C00502500 x1 entry=0.62
2026-08-21 11:20:57,600 INFO Live micro orphan_adopt AMD260824C00502500 x1 entry=0.62
Live micro orphan_adopt COST260828C01000000 x1 entry=0.63
2026-08-21 11:20:57,658 INFO Live micro orphan_adopt COST260828C01000000 x1 entry=0.63
Live micro orphan_adopt WMT260821C00110000 x1 entry=0.09
2026-08-21 11:20:57,716 INFO Live micro orphan_adopt WMT260821C00110000 x1 entry=0.09
LIVE EXIT stop_loss (-77.4%) AMD260824C00502500 x1 limit=0.11 id=d6ae2ebe-9f16-46f6-9f85-5571a76bf5a9
2026-08-21 11:20:59,253 INFO LIVE EXIT stop_loss (-77.4%) AMD260824C00502500 x1 limit=0.11 id=d6ae2ebe-9f16-46f6-9f85-5571a76bf5a9
Live micro hold ORPHAN COST260828C01000000 -20.6% (tp +50% / sl -40%)
2026-08-21 11:20:59,253 INFO Live micro hold ORPHAN COST260828C01000000 -20.6% (tp +50% / sl -40%)
LIVE EXIT stop_loss (-100.0%) WMT260821C00110000 x1 limit=0.01 id=fb05cfc6-9da8-4f7d-923c-21eb890bbe11
2026-08-21 11:20:59,728 INFO LIVE EXIT stop_loss (-100.0%) WMT260821C00110000 x1 limit=0.01 id=fb05cfc6-9da8-4f7d-923c-21eb890bbe11
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-08-21 11:20:59,847 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=2 lots=1
2026-08-21 11:21:00,032 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
... (135 earlier lines - see full log file)
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
## Ledger health — 2026-08-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   975 | WARN | <<<
| Missing exit records (post) |   975 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     1 | INFO |
| Total closed lots           |  1770 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=821 med=-47.5% | TAINTED n=1761 med=-39.3% | KEEP-only n=294 med=+37.5% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=322.21 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | MomReversal | 15 | 47% | +0.39% | -0.60% | -1.81% | 1.99 | 1.7d | $+3.53 | WATCH |
| 3 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260821T152551Z

- UTC timestamp: `20260821T152551Z`
- GitHub run: [#7761](https://github.com/28twagg-ops/TradingBot/actions/runs/32497470522)
- Run id: `32497470522`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`64s`
- Full logs: `logs/action_runs/20260821T152551Z_live_bot.log`, `logs/action_runs/20260821T152551Z_live_options.log`, `logs/action_runs/20260821T152551Z_options_bot.log`


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
{"ts_et":"2026-08-21T11:25:56.345143-04:00","date":"2026-08-21","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":55.5,"phases_s":{"reconcile":0.11,"cancel":0.03,"manage":0.85,"protective_stops":0.05,"scan":53.55,"entries":0.38},"signals":4,"placed":0,"equity":999995.97,"open_positions":1,"pending_orders":0,"open_lots":1,"submitted_today":1,"filled_today":1,"unattributed_contracts":0,"top_signals":["S210:AMD","S210:COIN","S218:SYK","S218:COST"],"github_run":"7761","github_run_id":"32497470522","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:25:52  INFO      Mode: exits
15:25:53  INFO        Daily log -> logs/daily/2026-08-21.md
15:25:53  INFO        Daily log reconciled -> logs/daily/2026-08-21.md (4 ledger rows)
15:25:53  INFO        place_all_stops: checking 3 positions...
15:25:53  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
15:25:53  INFO        [positions] 1/1 (1 valid)
15:25:53  INFO        Daily log -> logs/daily/2026-08-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:25 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $322.14|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AON  P&L +1.1%  $+0.80                                            HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  COST260828C01000000     $0.63    $0.50    -20.6%   $-13.00   $50.00   |
|  WMT260821C00110000      $0.09    $0.00    -100.0%  $-9.00    $0.00    |
|                                                                        |
|  Options open P&L                                               $-22.00|
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
=== options_live_micro LIVE 2026-08-21T11:25:54.140347-04:00 share=25% ===
2026-08-21 11:25:54,140 INFO === options_live_micro LIVE 2026-08-21T11:25:54.140347-04:00 share=25% ===
Live account equity $322.14 cash $201.38 #225458845 options_level=3
2026-08-21 11:25:54,237 INFO Live account equity $322.14 cash $201.38 #225458845 options_level=3
Live micro cancel stale sell WMT260821C00110000 id=fb05cfc6-9da8-4f7d-923c-21eb890bbe11 cid=OLX|0e750ffb2c43
2026-08-21 11:25:54,318 INFO Live micro cancel stale sell WMT260821C00110000 id=fb05cfc6-9da8-4f7d-923c-21eb890bbe11 cid=OLX|0e750ffb2c43
Live micro orphan_adopt WMT260821C00110000 x1 entry=0.09
2026-08-21 11:25:54,318 INFO Live micro orphan_adopt WMT260821C00110000 x1 entry=0.09
Live micro hold ORPHAN COST260828C01000000 -20.6% (tp +50% / sl -40%)
2026-08-21 11:25:54,346 INFO Live micro hold ORPHAN COST260828C01000000 -20.6% (tp +50% / sl -40%)
Live micro cancel stale sell WMT260821C00110000 id=fb05cfc6-9da8-4f7d-923c-21eb890bbe11 cid=OLX|0e750ffb2c43
2026-08-21 11:25:54,422 INFO Live micro cancel stale sell WMT260821C00110000 id=fb05cfc6-9da8-4f7d-923c-21eb890bbe11 cid=OLX|0e750ffb2c43
LIVE EXIT stop_loss (-100.0%) WMT260821C00110000 x1 limit=0.01 id=8a50733a-d943-442d-8d9e-3c0a5109feba
2026-08-21 11:25:54,720 INFO LIVE EXIT stop_loss (-100.0%) WMT260821C00110000 x1 limit=0.01 id=8a50733a-d943-442d-8d9e-3c0a5109feba
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-08-21 11:25:54,801 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=2 lots=1
2026-08-21 11:25:54,901 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
... (135 earlier lines - see full log file)
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
## Ledger health — 2026-08-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   975 | WARN | <<<
| Missing exit records (post) |   975 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     1 | INFO |
| Total closed lots           |  1770 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=821 med=-47.5% | TAINTED n=1761 med=-39.3% | KEEP-only n=294 med=+37.5% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=322.14 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | MomReversal | 15 | 47% | +0.39% | -0.60% | -1.81% | 1.99 | 1.7d | $+3.53 | WATCH |
| 3 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260821T153619Z

- UTC timestamp: `20260821T153619Z`
- GitHub run: [#7763](https://github.com/28twagg-ops/TradingBot/actions/runs/32498382113)
- Run id: `32498382113`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`9s`
- Full logs: `logs/action_runs/20260821T153619Z_live_bot.log`, `logs/action_runs/20260821T153619Z_live_options.log`, `logs/action_runs/20260821T153619Z_options_bot.log`


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
{"ts_et":"2026-08-21T11:36:24.857350-04:00","date":"2026-08-21","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":2.7,"phases_s":{"reconcile":0.23,"cancel":0.12,"manage":1.62,"protective_stops":0.11},"signals":0,"placed":0,"equity":999995.97,"open_positions":1,"pending_orders":0,"open_lots":1,"submitted_today":1,"filled_today":1,"unattributed_contracts":0,"top_signals":[],"github_run":"7763","github_run_id":"32498382113","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:36:19  INFO      Mode: exits
15:36:20  INFO        Daily log -> logs/daily/2026-08-21.md
15:36:20  INFO        Daily log reconciled -> logs/daily/2026-08-21.md (4 ledger rows)
15:36:20  INFO        place_all_stops: checking 3 positions...
15:36:20  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
15:36:21  INFO        [positions] 1/1 (1 valid)
15:36:21  INFO        Daily log -> logs/daily/2026-08-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $318.12|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AON  P&L +1.1%  $+0.78                                            HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  COST260828C01000000     $0.63    $0.46    -27.0%   $-17.00   $46.00   |
|  WMT260821C00110000      $0.09    $0.00    -100.0%  $-9.00    $0.00    |
|                                                                        |
|  Options open P&L                                               $-26.00|
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
=== options_live_micro LIVE 2026-08-21T11:36:22.069672-04:00 share=25% ===
2026-08-21 11:36:22,069 INFO === options_live_micro LIVE 2026-08-21T11:36:22.069672-04:00 share=25% ===
Live account equity $318.12 cash $201.38 #225458845 options_level=3
2026-08-21 11:36:22,264 INFO Live account equity $318.12 cash $201.38 #225458845 options_level=3
Live micro cancel stale sell WMT260821C00110000 id=3aaa3d92-527f-4510-b9b4-b647aa5a176b cid=OLX|9928b2eb7548
2026-08-21 11:36:22,443 INFO Live micro cancel stale sell WMT260821C00110000 id=3aaa3d92-527f-4510-b9b4-b647aa5a176b cid=OLX|9928b2eb7548
Live micro orphan_adopt WMT260821C00110000 x1 entry=0.09
2026-08-21 11:36:22,443 INFO Live micro orphan_adopt WMT260821C00110000 x1 entry=0.09
Live micro hold ORPHAN COST260828C01000000 -27.0% (tp +50% / sl -40%)
2026-08-21 11:36:22,503 INFO Live micro hold ORPHAN COST260828C01000000 -27.0% (tp +50% / sl -40%)
Live micro cancel stale sell WMT260821C00110000 id=3aaa3d92-527f-4510-b9b4-b647aa5a176b cid=OLX|9928b2eb7548
2026-08-21 11:36:22,676 INFO Live micro cancel stale sell WMT260821C00110000 id=3aaa3d92-527f-4510-b9b4-b647aa5a176b cid=OLX|9928b2eb7548
LIVE EXIT stop_loss (-100.0%) WMT260821C00110000 x1 limit=0.01 id=ee49b930-f7d9-4c6c-9652-b9f241ba72eb
2026-08-21 11:36:23,313 INFO LIVE EXIT stop_loss (-100.0%) WMT260821C00110000 x1 limit=0.01 id=ee49b930-f7d9-4c6c-9652-b9f241ba72eb
Live micro: manage/exits only
2026-08-21 11:36:23,486 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-21 11:36:23,545 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
... (130 earlier lines - see full log file)
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
## Ledger health — 2026-08-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   975 | WARN | <<<
| Missing exit records (post) |   975 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     1 | INFO |
| Total closed lots           |  1770 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=821 med=-47.5% | TAINTED n=1761 med=-39.3% | KEEP-only n=294 med=+37.5% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=318.12 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | MomReversal | 15 | 47% | +0.39% | -0.60% | -1.81% | 1.99 | 1.7d | $+3.53 | WATCH |
| 3 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260821T154100Z

- UTC timestamp: `20260821T154100Z`
- GitHub run: [#7764](https://github.com/28twagg-ops/TradingBot/actions/runs/32498829454)
- Run id: `32498829454`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`3s`
- Paper options: exit=`0`, duration=`12s`
- Full logs: `logs/action_runs/20260821T154100Z_live_bot.log`, `logs/action_runs/20260821T154100Z_live_options.log`, `logs/action_runs/20260821T154100Z_options_bot.log`


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
{"ts_et":"2026-08-21T11:41:07.752796-04:00","date":"2026-08-21","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":4.1,"phases_s":{"reconcile":0.36,"cancel":0.15,"manage":2.68,"protective_stops":0.15},"signals":0,"placed":0,"equity":999996.97,"open_positions":1,"pending_orders":0,"open_lots":1,"submitted_today":1,"filled_today":1,"unattributed_contracts":0,"top_signals":[],"github_run":"7764","github_run_id":"32498829454","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:41:01  INFO      Mode: exits
15:41:02  INFO        Daily log -> logs/daily/2026-08-21.md
15:41:02  INFO        Daily log reconciled -> logs/daily/2026-08-21.md (4 ledger rows)
15:41:02  INFO        place_all_stops: checking 3 positions...
15:41:02  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
15:41:02  INFO        [positions] 1/1 (1 valid)
15:41:03  INFO        Daily log -> logs/daily/2026-08-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $318.11|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AON  P&L +1.1%  $+0.77                                            HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  COST260828C01000000     $0.63    $0.46    -27.0%   $-17.00   $46.00   |
|  WMT260821C00110000      $0.09    $0.00    -100.0%  $-9.00    $0.00    |
|                                                                        |
|  Options open P&L                                               $-26.00|
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
=== options_live_micro LIVE 2026-08-21T11:41:04.034997-04:00 share=25% ===
2026-08-21 11:41:04,035 INFO === options_live_micro LIVE 2026-08-21T11:41:04.034997-04:00 share=25% ===
Live account equity $318.11 cash $201.38 #225458845 options_level=3
2026-08-21 11:41:04,274 INFO Live account equity $318.11 cash $201.38 #225458845 options_level=3
Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
2026-08-21 11:41:04,447 INFO Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
Live micro cancel stale sell WMT260821C00110000 id=ee49b930-f7d9-4c6c-9652-b9f241ba72eb cid=OLX|bea95270a22d broker_sym='WMT260821C00110000'
2026-08-21 11:41:04,520 INFO Live micro cancel stale sell WMT260821C00110000 id=ee49b930-f7d9-4c6c-9652-b9f241ba72eb cid=OLX|bea95270a22d broker_sym='WMT260821C00110000'
Live micro orphan_adopt WMT260821C00110000 x1 entry=0.09
2026-08-21 11:41:04,521 INFO Live micro orphan_adopt WMT260821C00110000 x1 entry=0.09
Live micro hold ORPHAN COST260828C01000000 -27.0% (tp +50% / sl -40%)
2026-08-21 11:41:04,619 INFO Live micro hold ORPHAN COST260828C01000000 -27.0% (tp +50% / sl -40%)
Live micro cancel-scan WMT260821C00110000: symbol-scoped empty; open_book n=1
2026-08-21 11:41:04,837 INFO Live micro cancel-scan WMT260821C00110000: symbol-scoped empty; open_book n=1
  open_order id=622ffbfc-8e23-41cb-900c-8ad08e486bd6 sym='COST260828C01000000' side=OrderSide.SELL status=OrderStatus.NEW cid='OLS|f7a537090f81' type=OrderType.STOP_LIMIT
2026-08-21 11:41:04,837 INFO   open_order id=622ffbfc-8e23-41cb-900c-8ad08e486bd6 sym='COST260828C01000000' side=OrderSide.SELL status=OrderStatus.NEW cid='OLS|f7a537090f81' type=OrderType.STOP_LIMIT
Live micro cancel-scan WMT260821C00110000: matched n=0
2026-08-21 11:41:04,838 INFO Live micro cancel-scan WMT260821C00110000: matched n=0
Live micro cancel-scan WMT260821C00110000: no non-OLS sell to cancel
2026-08-21 11:41:04,838 INFO Live micro cancel-scan WMT260821C00110000: no non-OLS sell to cancel
LIVE EXIT stop_loss (-100.0%) WMT260821C00110000 x1 limit=0.01 id=fd466332-45c9-41a7-8586-cea992705e87
2026-08-21 11:41:05,857 INFO LIVE EXIT stop_loss (-100.0%) WMT260821C00110000 x1 limit=0.01 id=fd466332-45c9-41a7-8586-cea992705e87
Live micro cancel-scan COST260828C01000000: symbol-scoped n=1
2026-08-21 11:41:05,930 INFO Live micro cancel-scan COST260828C01000000: symbol-scoped n=1
Live micro cancel-scan COST260828C01000000: no non-OLS sell to cancel
2026-08-21 11:41:05,930 INFO Live micro cancel-scan COST260828C01000000: no non-OLS sell to cancel
LIVE PROT check COST260828C01000000: have_ols=True open_matched=1 ols_id=622ffbfc-8e23-41cb-900c-8ad08e486bd6
2026-08-21 11:41:06,075 INFO LIVE PROT check COST260828C01000000: have_ols=True open_matched=1 ols_id=622ffbfc-8e23-41cb-900c-8ad08e486bd6
Live micro: manage/exits only
2026-08-21 11:41:06,075 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-21 11:41:06,148 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
... (130 earlier lines - see full log file)
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
## Ledger health — 2026-08-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   975 | WARN | <<<
| Missing exit records (post) |   975 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     1 | INFO |
| Total closed lots           |  1770 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=821 med=-47.5% | TAINTED n=1761 med=-39.3% | KEEP-only n=294 med=+37.5% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=318.11 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | MomReversal | 15 | 47% | +0.39% | -0.60% | -1.81% | 1.99 | 1.7d | $+3.53 | WATCH |
| 3 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260821T154559Z

- UTC timestamp: `20260821T154559Z`
- GitHub run: [#7765](https://github.com/28twagg-ops/TradingBot/actions/runs/32499285698)
- Run id: `32499285698`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`3s`
- Paper options: exit=`0`, duration=`14s`
- Full logs: `logs/action_runs/20260821T154559Z_live_bot.log`, `logs/action_runs/20260821T154559Z_live_options.log`, `logs/action_runs/20260821T154559Z_options_bot.log`


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
{"ts_et":"2026-08-21T11:46:08.522553-04:00","date":"2026-08-21","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":5.2,"phases_s":{"reconcile":0.3,"cancel":0.14,"manage":3.94,"protective_stops":0.14},"signals":0,"placed":0,"equity":999999.97,"open_positions":1,"pending_orders":0,"open_lots":1,"submitted_today":1,"filled_today":1,"unattributed_contracts":0,"top_signals":[],"github_run":"7765","github_run_id":"32499285698","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:46:01  INFO      Mode: exits
15:46:02  INFO        Daily log -> logs/daily/2026-08-21.md
15:46:02  INFO        Daily log reconciled -> logs/daily/2026-08-21.md (4 ledger rows)
15:46:02  INFO        place_all_stops: checking 3 positions...
15:46:02  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
15:46:02  INFO        [positions] 1/1 (1 valid)
15:46:03  INFO        Daily log -> logs/daily/2026-08-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $318.13|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AON  P&L +1.1%  $+0.79                                            HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  COST260828C01000000     $0.63    $0.46    -27.0%   $-17.00   $46.00   |
|  WMT260821C00110000      $0.09    $0.00    -100.0%  $-9.00    $0.00    |
|                                                                        |
|  Options open P&L                                               $-26.00|
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
=== options_live_micro LIVE 2026-08-21T11:46:04.039304-04:00 share=25% ===
2026-08-21 11:46:04,039 INFO === options_live_micro LIVE 2026-08-21T11:46:04.039304-04:00 share=25% ===
Live account equity $318.13 cash $201.38 #225458845 options_level=3
2026-08-21 11:46:04,292 INFO Live account equity $318.13 cash $201.38 #225458845 options_level=3
Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
2026-08-21 11:46:04,441 INFO Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
Live micro cancel stale sell WMT260821C00110000 id=fd466332-45c9-41a7-8586-cea992705e87 cid=OLX|587bdf2101d9 broker_sym='WMT260821C00110000'
2026-08-21 11:46:04,514 INFO Live micro cancel stale sell WMT260821C00110000 id=fd466332-45c9-41a7-8586-cea992705e87 cid=OLX|587bdf2101d9 broker_sym='WMT260821C00110000'
Live micro orphan_adopt WMT260821C00110000 x1 entry=0.09
2026-08-21 11:46:04,515 INFO Live micro orphan_adopt WMT260821C00110000 x1 entry=0.09
Live micro hold ORPHAN COST260828C01000000 -27.0% (tp +50% / sl -40%)
2026-08-21 11:46:04,593 INFO Live micro hold ORPHAN COST260828C01000000 -27.0% (tp +50% / sl -40%)
Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
2026-08-21 11:46:04,741 INFO Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
Live micro cancel stale sell WMT260821C00110000 id=fd466332-45c9-41a7-8586-cea992705e87 cid=OLX|587bdf2101d9 broker_sym='WMT260821C00110000'
2026-08-21 11:46:04,814 INFO Live micro cancel stale sell WMT260821C00110000 id=fd466332-45c9-41a7-8586-cea992705e87 cid=OLX|587bdf2101d9 broker_sym='WMT260821C00110000'
LIVE EXIT stop_loss (-100.0%) WMT260821C00110000 x1 limit=0.01 id=c10b09ff-9397-4039-b628-d9390c06369d
2026-08-21 11:46:06,344 INFO LIVE EXIT stop_loss (-100.0%) WMT260821C00110000 x1 limit=0.01 id=c10b09ff-9397-4039-b628-d9390c06369d
Live micro cancel-scan COST260828C01000000: symbol-scoped n=1
2026-08-21 11:46:06,418 INFO Live micro cancel-scan COST260828C01000000: symbol-scoped n=1
Live micro cancel-scan COST260828C01000000: no non-OLS sell to cancel
2026-08-21 11:46:06,418 INFO Live micro cancel-scan COST260828C01000000: no non-OLS sell to cancel
LIVE PROT check COST260828C01000000: have_ols=True open_matched=1 ols_id=622ffbfc-8e23-41cb-900c-8ad08e486bd6 ols_type=stop_limit
2026-08-21 11:46:06,568 INFO LIVE PROT check COST260828C01000000: have_ols=True open_matched=1 ols_id=622ffbfc-8e23-41cb-900c-8ad08e486bd6 ols_type=stop_limit
LIVE PROT upgrade COST260828C01000000: cancel stop-limit id=622ffbfc-8e23-41cb-900c-8ad08e486bd6 type=stop_limit
2026-08-21 11:46:06,568 INFO LIVE PROT upgrade COST260828C01000000: cancel stop-limit id=622ffbfc-8e23-41cb-900c-8ad08e486bd6 type=stop_limit
Live micro cancel by id (upgrade stop-limit COST260828C01000000) id=622ffbfc-8e23-41cb-900c-8ad08e486bd6
2026-08-21 11:46:06,641 INFO Live micro cancel by id (upgrade stop-limit COST260828C01000000) id=622ffbfc-8e23-41cb-900c-8ad08e486bd6
LIVE PROT STOP-MKT COST260828C01000000 x1 stop=0.38 id=ab9b8a23-2f03-4a3a-b25a-799118f49712
2026-08-21 11:46:06,726 INFO LIVE PROT STOP-MKT COST260828C01000000 x1 stop=0.38 id=ab9b8a23-2f03-4a3a-b25a-799118f49712
Live micro: manage/exits only
2026-08-21 11:46:06,727 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-21 11:46:06,800 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
... (130 earlier lines - see full log file)
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
## Ledger health — 2026-08-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   975 | WARN | <<<
| Missing exit records (post) |   975 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     1 | INFO |
| Total closed lots           |  1770 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=821 med=-47.5% | TAINTED n=1761 med=-39.3% | KEEP-only n=294 med=+37.5% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=318.13 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | MomReversal | 15 | 47% | +0.39% | -0.60% | -1.81% | 1.99 | 1.7d | $+3.53 | WATCH |
| 3 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260821T155250Z

- UTC timestamp: `20260821T155250Z`
- GitHub run: [#7766](https://github.com/28twagg-ops/TradingBot/actions/runs/32499734041)
- Run id: `32499734041`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`3s`
- Paper options: exit=`0`, duration=`12s`
- Full logs: `logs/action_runs/20260821T155250Z_live_bot.log`, `logs/action_runs/20260821T155250Z_live_options.log`, `logs/action_runs/20260821T155250Z_options_bot.log`


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
{"ts_et":"2026-08-21T11:52:56.998877-04:00","date":"2026-08-21","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":3.3,"phases_s":{"reconcile":0.31,"cancel":0.15,"manage":1.94,"protective_stops":0.15},"signals":0,"placed":0,"equity":999999.97,"open_positions":1,"pending_orders":0,"open_lots":1,"submitted_today":1,"filled_today":1,"unattributed_contracts":0,"top_signals":[],"github_run":"7766","github_run_id":"32499734041","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:52:50  INFO      Mode: exits
15:52:51  INFO        Daily log -> logs/daily/2026-08-21.md
15:52:51  INFO        Daily log reconciled -> logs/daily/2026-08-21.md (4 ledger rows)
15:52:51  INFO        place_all_stops: checking 3 positions...
15:52:51  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
15:52:52  INFO        [positions] 1/1 (1 valid)
15:52:52  INFO        Daily log -> logs/daily/2026-08-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:52 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $318.15|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AON  P&L +1.2%  $+0.81                                            HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  COST260828C01000000     $0.63    $0.46    -27.0%   $-17.00   $46.00   |
|  WMT260821C00110000      $0.09    $0.00    -100.0%  $-9.00    $0.00    |
|                                                                        |
|  Options open P&L                                               $-26.00|
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
=== options_live_micro LIVE 2026-08-21T11:52:53.577804-04:00 share=25% ===
2026-08-21 11:52:53,577 INFO === options_live_micro LIVE 2026-08-21T11:52:53.577804-04:00 share=25% ===
Live account equity $318.15 cash $201.38 #225458845 options_level=3
2026-08-21 11:52:53,836 INFO Live account equity $318.15 cash $201.38 #225458845 options_level=3
Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
2026-08-21 11:52:54,006 INFO Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
Live micro cancel stale sell WMT260821C00110000 id=c10b09ff-9397-4039-b628-d9390c06369d cid=OLX|1d8737213023 broker_sym='WMT260821C00110000'
2026-08-21 11:52:54,082 INFO Live micro cancel stale sell WMT260821C00110000 id=c10b09ff-9397-4039-b628-d9390c06369d cid=OLX|1d8737213023 broker_sym='WMT260821C00110000'
Live micro orphan_adopt WMT260821C00110000 x1 entry=0.09
2026-08-21 11:52:54,082 INFO Live micro orphan_adopt WMT260821C00110000 x1 entry=0.09
Live micro hold ORPHAN COST260828C01000000 -27.0% (tp +50% / sl -40%)
2026-08-21 11:52:54,162 INFO Live micro hold ORPHAN COST260828C01000000 -27.0% (tp +50% / sl -40%)
Live micro cancel-scan WMT260821C00110000: symbol-scoped empty; open_book n=1
2026-08-21 11:52:54,390 INFO Live micro cancel-scan WMT260821C00110000: symbol-scoped empty; open_book n=1
  open_order id=ab9b8a23-2f03-4a3a-b25a-799118f49712 sym='COST260828C01000000' side=OrderSide.SELL status=OrderStatus.NEW cid='OLS|1f926a83750f' type=OrderType.STOP
2026-08-21 11:52:54,390 INFO   open_order id=ab9b8a23-2f03-4a3a-b25a-799118f49712 sym='COST260828C01000000' side=OrderSide.SELL status=OrderStatus.NEW cid='OLS|1f926a83750f' type=OrderType.STOP
Live micro cancel-scan WMT260821C00110000: matched n=0
2026-08-21 11:52:54,390 INFO Live micro cancel-scan WMT260821C00110000: matched n=0
Live micro cancel-scan WMT260821C00110000: no non-OLS sell to cancel
2026-08-21 11:52:54,390 INFO Live micro cancel-scan WMT260821C00110000: no non-OLS sell to cancel
LIVE EXIT stop_loss (-100.0%) WMT260821C00110000 x1 limit=0.01 id=cc9820f9-024e-4bae-bb2b-23484155619d
2026-08-21 11:52:55,050 INFO LIVE EXIT stop_loss (-100.0%) WMT260821C00110000 x1 limit=0.01 id=cc9820f9-024e-4bae-bb2b-23484155619d
Live micro cancel-scan COST260828C01000000: symbol-scoped n=1
2026-08-21 11:52:55,125 INFO Live micro cancel-scan COST260828C01000000: symbol-scoped n=1
Live micro cancel-scan COST260828C01000000: no non-OLS sell to cancel
2026-08-21 11:52:55,126 INFO Live micro cancel-scan COST260828C01000000: no non-OLS sell to cancel
LIVE PROT check COST260828C01000000: have_ols=True open_matched=1 ols_id=ab9b8a23-2f03-4a3a-b25a-799118f49712 ols_type=stop
2026-08-21 11:52:55,279 INFO LIVE PROT check COST260828C01000000: have_ols=True open_matched=1 ols_id=ab9b8a23-2f03-4a3a-b25a-799118f49712 ols_type=stop
Live micro: manage/exits only
2026-08-21 11:52:55,279 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-21 11:52:55,385 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
... (130 earlier lines - see full log file)
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
## Ledger health — 2026-08-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   975 | WARN | <<<
| Missing exit records (post) |   975 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     1 | INFO |
| Total closed lots           |  1770 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=821 med=-47.5% | TAINTED n=1761 med=-39.3% | KEEP-only n=294 med=+37.5% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=318.15 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | MomReversal | 15 | 47% | +0.39% | -0.60% | -1.81% | 1.99 | 1.7d | $+3.53 | WATCH |
| 3 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260821T160145Z

- UTC timestamp: `20260821T160145Z`
- GitHub run: [#7768](https://github.com/28twagg-ops/TradingBot/actions/runs/32500620580)
- Run id: `32500620580`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`10s`
- Full logs: `logs/action_runs/20260821T160145Z_live_bot.log`, `logs/action_runs/20260821T160145Z_live_options.log`, `logs/action_runs/20260821T160145Z_options_bot.log`


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
{"ts_et":"2026-08-21T12:01:50.498338-04:00","date":"2026-08-21","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":1.2,"phases_s":{"reconcile":0.05,"cancel":0.02,"manage":0.62,"protective_stops":0.04},"signals":0,"placed":0,"equity":999995.97,"open_positions":1,"pending_orders":0,"open_lots":1,"submitted_today":1,"filled_today":1,"unattributed_contracts":0,"top_signals":[],"github_run":"7768","github_run_id":"32500620580","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
16:01:46  INFO      Mode: exits
16:01:46  INFO        Daily log -> logs/daily/2026-08-21.md
16:01:46  INFO        Daily log reconciled -> logs/daily/2026-08-21.md (4 ledger rows)
16:01:46  INFO        place_all_stops: checking 3 positions...
16:01:46  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
16:01:47  INFO        [positions] 1/1 (1 valid)
16:01:47  INFO        Daily log -> logs/daily/2026-08-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $317.17|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AON  P&L +1.2%  $+0.83                                            HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  COST260828C01000000     $0.63    $0.45    -28.6%   $-18.00   $45.00   |
|  WMT260821C00110000      $0.09    $0.00    -100.0%  $-9.00    $0.00    |
|                                                                        |
|  Options open P&L                                               $-27.00|
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
=== options_live_micro LIVE 2026-08-21T12:01:48.159256-04:00 share=25% ===
2026-08-21 12:01:48,159 INFO === options_live_micro LIVE 2026-08-21T12:01:48.159256-04:00 share=25% ===
Live account equity $317.17 cash $201.38 #225458845 options_level=3
2026-08-21 12:01:48,265 INFO Live account equity $317.17 cash $201.38 #225458845 options_level=3
Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
2026-08-21 12:01:48,323 INFO Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
Live micro cancel stale sell WMT260821C00110000 id=cc9820f9-024e-4bae-bb2b-23484155619d cid=OLX|f3e123e4f3bd broker_sym='WMT260821C00110000'
2026-08-21 12:01:48,332 INFO Live micro cancel stale sell WMT260821C00110000 id=cc9820f9-024e-4bae-bb2b-23484155619d cid=OLX|f3e123e4f3bd broker_sym='WMT260821C00110000'
Live micro orphan_adopt WMT260821C00110000 x1 entry=0.09
2026-08-21 12:01:48,332 INFO Live micro orphan_adopt WMT260821C00110000 x1 entry=0.09
Live micro hold ORPHAN COST260828C01000000 -28.6% (tp +50% / sl -40%)
2026-08-21 12:01:48,400 INFO Live micro hold ORPHAN COST260828C01000000 -28.6% (tp +50% / sl -40%)
Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
2026-08-21 12:01:48,419 INFO Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
Live micro cancel stale sell WMT260821C00110000 id=cc9820f9-024e-4bae-bb2b-23484155619d cid=OLX|f3e123e4f3bd broker_sym='WMT260821C00110000'
2026-08-21 12:01:48,426 INFO Live micro cancel stale sell WMT260821C00110000 id=cc9820f9-024e-4bae-bb2b-23484155619d cid=OLX|f3e123e4f3bd broker_sym='WMT260821C00110000'
LIVE EXIT stop_loss (-100.0%) WMT260821C00110000 x1 limit=0.01 id=f9f85954-353c-420f-bd54-246396a9f6c1
2026-08-21 12:01:48,776 INFO LIVE EXIT stop_loss (-100.0%) WMT260821C00110000 x1 limit=0.01 id=f9f85954-353c-420f-bd54-246396a9f6c1
Live micro cancel-scan COST260828C01000000: symbol-scoped n=1
2026-08-21 12:01:48,786 INFO Live micro cancel-scan COST260828C01000000: symbol-scoped n=1
Live micro cancel-scan COST260828C01000000: no non-OLS sell to cancel
2026-08-21 12:01:48,786 INFO Live micro cancel-scan COST260828C01000000: no non-OLS sell to cancel
LIVE PROT check COST260828C01000000: have_ols=True open_matched=1 ols_id=ab9b8a23-2f03-4a3a-b25a-799118f49712 ols_type=stop
2026-08-21 12:01:48,810 INFO LIVE PROT check COST260828C01000000: have_ols=True open_matched=1 ols_id=ab9b8a23-2f03-4a3a-b25a-799118f49712 ols_type=stop
Live micro: manage/exits only
2026-08-21 12:01:48,810 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-21 12:01:48,822 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
... (131 earlier lines - see full log file)
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
## Ledger health — 2026-08-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   975 | WARN | <<<
| Missing exit records (post) |   975 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     1 | INFO |
| Total closed lots           |  1770 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=821 med=-47.5% | TAINTED n=1761 med=-39.3% | KEEP-only n=294 med=+37.5% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=317.17 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | MomReversal | 15 | 47% | +0.39% | -0.60% | -1.81% | 1.99 | 1.7d | $+3.53 | WATCH |
| 3 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260821T160549Z

- UTC timestamp: `20260821T160549Z`
- GitHub run: [#7769](https://github.com/28twagg-ops/TradingBot/actions/runs/32501065430)
- Run id: `32501065430`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`10s`
- Full logs: `logs/action_runs/20260821T160549Z_live_bot.log`, `logs/action_runs/20260821T160549Z_live_options.log`, `logs/action_runs/20260821T160549Z_options_bot.log`


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
{"ts_et":"2026-08-21T12:05:54.599076-04:00","date":"2026-08-21","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":1.7,"phases_s":{"reconcile":0.12,"cancel":0.05,"manage":0.96,"protective_stops":0.05},"signals":0,"placed":0,"equity":999994.97,"open_positions":1,"pending_orders":0,"open_lots":1,"submitted_today":1,"filled_today":1,"unattributed_contracts":0,"top_signals":[],"github_run":"7769","github_run_id":"32501065430","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
16:05:50  INFO      Mode: exits
16:05:50  INFO        Daily log -> logs/daily/2026-08-21.md
16:05:50  INFO        Daily log reconciled -> logs/daily/2026-08-21.md (4 ledger rows)
16:05:50  INFO        place_all_stops: checking 3 positions...
16:05:50  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
16:05:51  INFO        [positions] 1/1 (1 valid)
16:05:51  INFO        Daily log -> logs/daily/2026-08-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:05 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $317.15|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AON  P&L +1.2%  $+0.81                                            HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  COST260828C01000000     $0.63    $0.45    -28.6%   $-18.00   $45.00   |
|  WMT260821C00110000      $0.09    $0.00    -100.0%  $-9.00    $0.00    |
|                                                                        |
|  Options open P&L                                               $-27.00|
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
=== options_live_micro LIVE 2026-08-21T12:05:52.251914-04:00 share=25% ===
2026-08-21 12:05:52,251 INFO === options_live_micro LIVE 2026-08-21T12:05:52.251914-04:00 share=25% ===
Live account equity $317.15 cash $201.38 #225458845 options_level=3
2026-08-21 12:05:52,351 INFO Live account equity $317.15 cash $201.38 #225458845 options_level=3
Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
2026-08-21 12:05:52,398 INFO Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
Live micro cancel stale sell WMT260821C00110000 id=f9f85954-353c-420f-bd54-246396a9f6c1 cid=OLX|fcb66e59ca8e broker_sym='WMT260821C00110000'
2026-08-21 12:05:52,421 INFO Live micro cancel stale sell WMT260821C00110000 id=f9f85954-353c-420f-bd54-246396a9f6c1 cid=OLX|fcb66e59ca8e broker_sym='WMT260821C00110000'
Live micro orphan_adopt WMT260821C00110000 x1 entry=0.09
2026-08-21 12:05:52,421 INFO Live micro orphan_adopt WMT260821C00110000 x1 entry=0.09
Live micro hold ORPHAN COST260828C01000000 -28.6% (tp +50% / sl -40%)
2026-08-21 12:05:52,452 INFO Live micro hold ORPHAN COST260828C01000000 -28.6% (tp +50% / sl -40%)
Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
2026-08-21 12:05:52,498 INFO Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
Live micro cancel stale sell WMT260821C00110000 id=f9f85954-353c-420f-bd54-246396a9f6c1 cid=OLX|fcb66e59ca8e broker_sym='WMT260821C00110000'
2026-08-21 12:05:52,519 INFO Live micro cancel stale sell WMT260821C00110000 id=f9f85954-353c-420f-bd54-246396a9f6c1 cid=OLX|fcb66e59ca8e broker_sym='WMT260821C00110000'
LIVE EXIT stop_loss (-100.0%) WMT260821C00110000 x1 limit=0.01 id=ba4149a4-a08c-4a90-97f4-f35a4bb0f02d
2026-08-21 12:05:53,031 INFO LIVE EXIT stop_loss (-100.0%) WMT260821C00110000 x1 limit=0.01 id=ba4149a4-a08c-4a90-97f4-f35a4bb0f02d
Live micro cancel-scan COST260828C01000000: symbol-scoped n=1
2026-08-21 12:05:53,056 INFO Live micro cancel-scan COST260828C01000000: symbol-scoped n=1
Live micro cancel-scan COST260828C01000000: no non-OLS sell to cancel
2026-08-21 12:05:53,056 INFO Live micro cancel-scan COST260828C01000000: no non-OLS sell to cancel
LIVE PROT check COST260828C01000000: have_ols=True open_matched=1 ols_id=ab9b8a23-2f03-4a3a-b25a-799118f49712 ols_type=stop
2026-08-21 12:05:53,107 INFO LIVE PROT check COST260828C01000000: have_ols=True open_matched=1 ols_id=ab9b8a23-2f03-4a3a-b25a-799118f49712 ols_type=stop
Live micro: manage/exits only
2026-08-21 12:05:53,107 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-21 12:05:53,129 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
... (130 earlier lines - see full log file)
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
## Ledger health — 2026-08-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   975 | WARN | <<<
| Missing exit records (post) |   975 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     1 | INFO |
| Total closed lots           |  1770 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=821 med=-47.5% | TAINTED n=1761 med=-39.3% | KEEP-only n=294 med=+37.5% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=317.15 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | MomReversal | 15 | 47% | +0.39% | -0.60% | -1.81% | 1.99 | 1.7d | $+3.53 | WATCH |
| 3 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260821T161049Z

- UTC timestamp: `20260821T161049Z`
- GitHub run: [#7770](https://github.com/28twagg-ops/TradingBot/actions/runs/32501513147)
- Run id: `32501513147`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`9s`
- Full logs: `logs/action_runs/20260821T161049Z_live_bot.log`, `logs/action_runs/20260821T161049Z_live_options.log`, `logs/action_runs/20260821T161049Z_options_bot.log`


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
{"ts_et":"2026-08-21T12:10:54.403639-04:00","date":"2026-08-21","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":1.7,"phases_s":{"reconcile":0.13,"cancel":0.05,"manage":0.91,"protective_stops":0.05},"signals":0,"placed":0,"equity":999991.97,"open_positions":1,"pending_orders":0,"open_lots":1,"submitted_today":1,"filled_today":1,"unattributed_contracts":0,"top_signals":[],"github_run":"7770","github_run_id":"32501513147","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
16:10:50  INFO      Mode: exits
16:10:50  INFO        Daily log -> logs/daily/2026-08-21.md
16:10:50  INFO        Daily log reconciled -> logs/daily/2026-08-21.md (4 ledger rows)
16:10:50  INFO        place_all_stops: checking 3 positions...
16:10:50  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
16:10:50  INFO        [positions] 1/1 (1 valid)
16:10:51  INFO        Daily log -> logs/daily/2026-08-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $317.29|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AON  P&L +1.4%  $+0.95                                            HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  COST260828C01000000     $0.63    $0.45    -28.6%   $-18.00   $45.00   |
|  WMT260821C00110000      $0.09    $0.00    -100.0%  $-9.00    $0.00    |
|                                                                        |
|  Options open P&L                                               $-27.00|
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
=== options_live_micro LIVE 2026-08-21T12:10:52.307535-04:00 share=25% ===
2026-08-21 12:10:52,307 INFO === options_live_micro LIVE 2026-08-21T12:10:52.307535-04:00 share=25% ===
Live account equity $317.29 cash $201.38 #225458845 options_level=3
2026-08-21 12:10:52,390 INFO Live account equity $317.29 cash $201.38 #225458845 options_level=3
Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
2026-08-21 12:10:52,436 INFO Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
Live micro cancel stale sell WMT260821C00110000 id=ba4149a4-a08c-4a90-97f4-f35a4bb0f02d cid=OLX|cefef98faca7 broker_sym='WMT260821C00110000'
2026-08-21 12:10:52,458 INFO Live micro cancel stale sell WMT260821C00110000 id=ba4149a4-a08c-4a90-97f4-f35a4bb0f02d cid=OLX|cefef98faca7 broker_sym='WMT260821C00110000'
Live micro orphan_adopt WMT260821C00110000 x1 entry=0.09
2026-08-21 12:10:52,458 INFO Live micro orphan_adopt WMT260821C00110000 x1 entry=0.09
Live micro hold ORPHAN COST260828C01000000 -28.6% (tp +50% / sl -40%)
2026-08-21 12:10:52,490 INFO Live micro hold ORPHAN COST260828C01000000 -28.6% (tp +50% / sl -40%)
Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
2026-08-21 12:10:52,536 INFO Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
Live micro cancel stale sell WMT260821C00110000 id=ba4149a4-a08c-4a90-97f4-f35a4bb0f02d cid=OLX|cefef98faca7 broker_sym='WMT260821C00110000'
2026-08-21 12:10:52,556 INFO Live micro cancel stale sell WMT260821C00110000 id=ba4149a4-a08c-4a90-97f4-f35a4bb0f02d cid=OLX|cefef98faca7 broker_sym='WMT260821C00110000'
LIVE EXIT stop_loss (-100.0%) WMT260821C00110000 x1 limit=0.01 id=ca56ef57-c07a-46db-ac29-f98cc0171530
2026-08-21 12:10:52,863 INFO LIVE EXIT stop_loss (-100.0%) WMT260821C00110000 x1 limit=0.01 id=ca56ef57-c07a-46db-ac29-f98cc0171530
Live micro cancel-scan COST260828C01000000: symbol-scoped n=1
2026-08-21 12:10:52,885 INFO Live micro cancel-scan COST260828C01000000: symbol-scoped n=1
Live micro cancel-scan COST260828C01000000: no non-OLS sell to cancel
2026-08-21 12:10:52,885 INFO Live micro cancel-scan COST260828C01000000: no non-OLS sell to cancel
LIVE PROT check COST260828C01000000: have_ols=True open_matched=1 ols_id=ab9b8a23-2f03-4a3a-b25a-799118f49712 ols_type=stop
2026-08-21 12:10:52,934 INFO LIVE PROT check COST260828C01000000: have_ols=True open_matched=1 ols_id=ab9b8a23-2f03-4a3a-b25a-799118f49712 ols_type=stop
Live micro: manage/exits only
2026-08-21 12:10:52,934 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-21 12:10:52,965 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
... (130 earlier lines - see full log file)
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
## Ledger health — 2026-08-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   975 | WARN | <<<
| Missing exit records (post) |   975 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     1 | INFO |
| Total closed lots           |  1770 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=821 med=-47.5% | TAINTED n=1761 med=-39.3% | KEEP-only n=294 med=+37.5% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=317.29 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | MomReversal | 15 | 47% | +0.39% | -0.60% | -1.81% | 1.99 | 1.7d | $+3.53 | WATCH |
| 3 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260821T161600Z

- UTC timestamp: `20260821T161600Z`
- GitHub run: [#7771](https://github.com/28twagg-ops/TradingBot/actions/runs/32501951184)
- Run id: `32501951184`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`10s`
- Full logs: `logs/action_runs/20260821T161600Z_live_bot.log`, `logs/action_runs/20260821T161600Z_live_options.log`, `logs/action_runs/20260821T161600Z_options_bot.log`


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
{"ts_et":"2026-08-21T12:16:07.613185-04:00","date":"2026-08-21","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":3.7,"phases_s":{"reconcile":0.24,"cancel":0.11,"manage":2.69,"protective_stops":0.12},"signals":0,"placed":0,"equity":999993.97,"open_positions":1,"pending_orders":0,"open_lots":1,"submitted_today":1,"filled_today":1,"unattributed_contracts":0,"top_signals":[],"github_run":"7771","github_run_id":"32501951184","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
16:16:01  INFO      Mode: exits
16:16:03  INFO        Daily log -> logs/daily/2026-08-21.md
16:16:03  INFO        Daily log reconciled -> logs/daily/2026-08-21.md (4 ledger rows)
16:16:03  INFO        place_all_stops: checking 3 positions...
16:16:03  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
16:16:03  INFO        [positions] 1/1 (1 valid)
16:16:03  INFO        Daily log -> logs/daily/2026-08-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $317.27|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AON  P&L +1.3%  $+0.93                                            HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  COST260828C01000000     $0.63    $0.45    -28.6%   $-18.00   $45.00   |
|  WMT260821C00110000      $0.09    $0.00    -100.0%  $-9.00    $0.00    |
|                                                                        |
|  Options open P&L                                               $-27.00|
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
=== options_live_micro LIVE 2026-08-21T12:16:04.594997-04:00 share=25% ===
2026-08-21 12:16:04,595 INFO === options_live_micro LIVE 2026-08-21T12:16:04.594997-04:00 share=25% ===
Live account equity $317.27 cash $201.38 #225458845 options_level=3
2026-08-21 12:16:04,822 INFO Live account equity $317.27 cash $201.38 #225458845 options_level=3
Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
2026-08-21 12:16:04,937 INFO Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
Live micro cancel stale sell WMT260821C00110000 id=ca56ef57-c07a-46db-ac29-f98cc0171530 cid=OLX|065d3898af58 broker_sym='WMT260821C00110000'
2026-08-21 12:16:04,993 INFO Live micro cancel stale sell WMT260821C00110000 id=ca56ef57-c07a-46db-ac29-f98cc0171530 cid=OLX|065d3898af58 broker_sym='WMT260821C00110000'
Live micro orphan_adopt WMT260821C00110000 x1 entry=0.09
2026-08-21 12:16:04,994 INFO Live micro orphan_adopt WMT260821C00110000 x1 entry=0.09
Live micro hold ORPHAN COST260828C01000000 -28.6% (tp +50% / sl -40%)
2026-08-21 12:16:05,052 INFO Live micro hold ORPHAN COST260828C01000000 -28.6% (tp +50% / sl -40%)
Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
2026-08-21 12:16:05,168 INFO Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
Live micro cancel stale sell WMT260821C00110000 id=ca56ef57-c07a-46db-ac29-f98cc0171530 cid=OLX|065d3898af58 broker_sym='WMT260821C00110000'
2026-08-21 12:16:05,224 INFO Live micro cancel stale sell WMT260821C00110000 id=ca56ef57-c07a-46db-ac29-f98cc0171530 cid=OLX|065d3898af58 broker_sym='WMT260821C00110000'
LIVE EXIT stop_loss (-100.0%) WMT260821C00110000 x1 limit=0.01 id=78436089-d7eb-4269-a6d5-cd013380080e
2026-08-21 12:16:05,939 INFO LIVE EXIT stop_loss (-100.0%) WMT260821C00110000 x1 limit=0.01 id=78436089-d7eb-4269-a6d5-cd013380080e
Live micro cancel-scan COST260828C01000000: symbol-scoped n=1
2026-08-21 12:16:05,997 INFO Live micro cancel-scan COST260828C01000000: symbol-scoped n=1
Live micro cancel-scan COST260828C01000000: no non-OLS sell to cancel
2026-08-21 12:16:05,997 INFO Live micro cancel-scan COST260828C01000000: no non-OLS sell to cancel
LIVE PROT check COST260828C01000000: have_ols=True open_matched=1 ols_id=ab9b8a23-2f03-4a3a-b25a-799118f49712 ols_type=stop
2026-08-21 12:16:06,126 INFO LIVE PROT check COST260828C01000000: have_ols=True open_matched=1 ols_id=ab9b8a23-2f03-4a3a-b25a-799118f49712 ols_type=stop
Live micro: manage/exits only
2026-08-21 12:16:06,126 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-21 12:16:06,187 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
... (130 earlier lines - see full log file)
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
## Ledger health — 2026-08-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   975 | WARN | <<<
| Missing exit records (post) |   975 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     1 | INFO |
| Total closed lots           |  1770 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=821 med=-47.5% | TAINTED n=1761 med=-39.3% | KEEP-only n=294 med=+37.5% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=317.27 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | MomReversal | 15 | 47% | +0.39% | -0.60% | -1.81% | 1.99 | 1.7d | $+3.53 | WATCH |
| 3 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260821T162054Z

- UTC timestamp: `20260821T162054Z`
- GitHub run: [#7772](https://github.com/28twagg-ops/TradingBot/actions/runs/32502377034)
- Run id: `32502377034`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`11s`
- Full logs: `logs/action_runs/20260821T162054Z_live_bot.log`, `logs/action_runs/20260821T162054Z_live_options.log`, `logs/action_runs/20260821T162054Z_options_bot.log`


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
{"ts_et":"2026-08-21T12:20:59.632592-04:00","date":"2026-08-21","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":3.0,"phases_s":{"reconcile":0.19,"cancel":0.1,"manage":1.99,"protective_stops":0.09},"signals":0,"placed":0,"equity":999993.97,"open_positions":1,"pending_orders":0,"open_lots":1,"submitted_today":1,"filled_today":1,"unattributed_contracts":0,"top_signals":[],"github_run":"7772","github_run_id":"32502377034","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
16:20:55  INFO      Mode: exits
16:20:55  INFO        Daily log -> logs/daily/2026-08-21.md
16:20:55  INFO        Daily log reconciled -> logs/daily/2026-08-21.md (4 ledger rows)
16:20:55  INFO        place_all_stops: checking 3 positions...
16:20:55  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
16:20:56  INFO        [positions] 1/1 (1 valid)
16:20:56  INFO        Daily log -> logs/daily/2026-08-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $317.22|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AON  P&L +1.3%  $+0.88                                            HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  COST260828C01000000     $0.63    $0.45    -28.6%   $-18.00   $45.00   |
|  WMT260821C00110000      $0.09    $0.00    -100.0%  $-9.00    $0.00    |
|                                                                        |
|  Options open P&L                                               $-27.00|
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
=== options_live_micro LIVE 2026-08-21T12:20:57.084421-04:00 share=25% ===
2026-08-21 12:20:57,084 INFO === options_live_micro LIVE 2026-08-21T12:20:57.084421-04:00 share=25% ===
Live account equity $317.22 cash $201.38 #225458845 options_level=3
2026-08-21 12:20:57,231 INFO Live account equity $317.22 cash $201.38 #225458845 options_level=3
Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
2026-08-21 12:20:57,314 INFO Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
Live micro cancel stale sell WMT260821C00110000 id=78436089-d7eb-4269-a6d5-cd013380080e cid=OLX|97dff7395141 broker_sym='WMT260821C00110000'
2026-08-21 12:20:57,355 INFO Live micro cancel stale sell WMT260821C00110000 id=78436089-d7eb-4269-a6d5-cd013380080e cid=OLX|97dff7395141 broker_sym='WMT260821C00110000'
Live micro orphan_adopt WMT260821C00110000 x1 entry=0.09
2026-08-21 12:20:57,355 INFO Live micro orphan_adopt WMT260821C00110000 x1 entry=0.09
Live micro hold ORPHAN COST260828C01000000 -28.6% (tp +50% / sl -40%)
2026-08-21 12:20:57,398 INFO Live micro hold ORPHAN COST260828C01000000 -28.6% (tp +50% / sl -40%)
Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
2026-08-21 12:20:57,482 INFO Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
Live micro cancel stale sell WMT260821C00110000 id=78436089-d7eb-4269-a6d5-cd013380080e cid=OLX|97dff7395141 broker_sym='WMT260821C00110000'
2026-08-21 12:20:57,523 INFO Live micro cancel stale sell WMT260821C00110000 id=78436089-d7eb-4269-a6d5-cd013380080e cid=OLX|97dff7395141 broker_sym='WMT260821C00110000'
LIVE EXIT stop_loss (-100.0%) WMT260821C00110000 x1 limit=0.01 id=f2368d24-d726-4ac2-8aee-8f51e6d1a1f7
2026-08-21 12:20:57,934 INFO LIVE EXIT stop_loss (-100.0%) WMT260821C00110000 x1 limit=0.01 id=f2368d24-d726-4ac2-8aee-8f51e6d1a1f7
Live micro cancel-scan COST260828C01000000: symbol-scoped n=1
2026-08-21 12:20:57,976 INFO Live micro cancel-scan COST260828C01000000: symbol-scoped n=1
Live micro cancel-scan COST260828C01000000: no non-OLS sell to cancel
2026-08-21 12:20:57,977 INFO Live micro cancel-scan COST260828C01000000: no non-OLS sell to cancel
LIVE PROT check COST260828C01000000: have_ols=True open_matched=1 ols_id=ab9b8a23-2f03-4a3a-b25a-799118f49712 ols_type=stop
2026-08-21 12:20:58,060 INFO LIVE PROT check COST260828C01000000: have_ols=True open_matched=1 ols_id=ab9b8a23-2f03-4a3a-b25a-799118f49712 ols_type=stop
Live micro: manage/exits only
2026-08-21 12:20:58,060 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-21 12:20:58,106 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
... (130 earlier lines - see full log file)
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
## Ledger health — 2026-08-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   975 | WARN | <<<
| Missing exit records (post) |   975 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     1 | INFO |
| Total closed lots           |  1770 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=821 med=-47.5% | TAINTED n=1761 med=-39.3% | KEEP-only n=294 med=+37.5% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=317.22 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | MomReversal | 15 | 47% | +0.39% | -0.60% | -1.81% | 1.99 | 1.7d | $+3.53 | WATCH |
| 3 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260821T162552Z

- UTC timestamp: `20260821T162552Z`
- GitHub run: [#7773](https://github.com/28twagg-ops/TradingBot/actions/runs/32502804453)
- Run id: `32502804453`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`10s`
- Full logs: `logs/action_runs/20260821T162552Z_live_bot.log`, `logs/action_runs/20260821T162552Z_live_options.log`, `logs/action_runs/20260821T162552Z_options_bot.log`


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
{"ts_et":"2026-08-21T12:25:56.958778-04:00","date":"2026-08-21","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":1.5,"phases_s":{"reconcile":0.06,"cancel":0.02,"manage":0.66,"protective_stops":0.02},"signals":0,"placed":0,"equity":999993.97,"open_positions":1,"pending_orders":0,"open_lots":1,"submitted_today":1,"filled_today":1,"unattributed_contracts":0,"top_signals":[],"github_run":"7773","github_run_id":"32502804453","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
16:25:53  INFO      Mode: exits
16:25:53  INFO        Daily log -> logs/daily/2026-08-21.md
16:25:53  INFO        Daily log reconciled -> logs/daily/2026-08-21.md (4 ledger rows)
16:25:53  INFO        place_all_stops: checking 3 positions...
16:25:53  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
16:25:54  INFO        [positions] 1/1 (1 valid)
16:25:54  INFO        Daily log -> logs/daily/2026-08-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:25 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $317.19|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AON  P&L +1.2%  $+0.85                                            HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  COST260828C01000000     $0.63    $0.45    -28.6%   $-18.00   $45.00   |
|  WMT260821C00110000      $0.09    $0.00    -100.0%  $-9.00    $0.00    |
|                                                                        |
|  Options open P&L                                               $-27.00|
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
=== options_live_micro LIVE 2026-08-21T12:25:54.841266-04:00 share=25% ===
2026-08-21 12:25:54,841 INFO === options_live_micro LIVE 2026-08-21T12:25:54.841266-04:00 share=25% ===
Live account equity $317.19 cash $201.38 #225458845 options_level=3
2026-08-21 12:25:54,949 INFO Live account equity $317.19 cash $201.38 #225458845 options_level=3
Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
2026-08-21 12:25:54,968 INFO Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
Live micro cancel stale sell WMT260821C00110000 id=f2368d24-d726-4ac2-8aee-8f51e6d1a1f7 cid=OLX|6475a1459035 broker_sym='WMT260821C00110000'
2026-08-21 12:25:54,977 INFO Live micro cancel stale sell WMT260821C00110000 id=f2368d24-d726-4ac2-8aee-8f51e6d1a1f7 cid=OLX|6475a1459035 broker_sym='WMT260821C00110000'
Live micro orphan_adopt WMT260821C00110000 x1 entry=0.09
2026-08-21 12:25:54,977 INFO Live micro orphan_adopt WMT260821C00110000 x1 entry=0.09
Live micro hold ORPHAN COST260828C01000000 -28.6% (tp +50% / sl -40%)
2026-08-21 12:25:54,987 INFO Live micro hold ORPHAN COST260828C01000000 -28.6% (tp +50% / sl -40%)
Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
2026-08-21 12:25:55,005 INFO Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
Live micro cancel stale sell WMT260821C00110000 id=f2368d24-d726-4ac2-8aee-8f51e6d1a1f7 cid=OLX|6475a1459035 broker_sym='WMT260821C00110000'
2026-08-21 12:25:55,012 INFO Live micro cancel stale sell WMT260821C00110000 id=f2368d24-d726-4ac2-8aee-8f51e6d1a1f7 cid=OLX|6475a1459035 broker_sym='WMT260821C00110000'
LIVE EXIT stop_loss (-100.0%) WMT260821C00110000 x1 limit=0.01 id=19e93439-249a-4269-89b3-d93020f08786
2026-08-21 12:25:55,425 INFO LIVE EXIT stop_loss (-100.0%) WMT260821C00110000 x1 limit=0.01 id=19e93439-249a-4269-89b3-d93020f08786
Live micro cancel-scan COST260828C01000000: symbol-scoped n=1
2026-08-21 12:25:55,435 INFO Live micro cancel-scan COST260828C01000000: symbol-scoped n=1
Live micro cancel-scan COST260828C01000000: no non-OLS sell to cancel
2026-08-21 12:25:55,435 INFO Live micro cancel-scan COST260828C01000000: no non-OLS sell to cancel
LIVE PROT check COST260828C01000000: have_ols=True open_matched=1 ols_id=ab9b8a23-2f03-4a3a-b25a-799118f49712 ols_type=stop
2026-08-21 12:25:55,458 INFO LIVE PROT check COST260828C01000000: have_ols=True open_matched=1 ols_id=ab9b8a23-2f03-4a3a-b25a-799118f49712 ols_type=stop
Live micro: manage/exits only
2026-08-21 12:25:55,458 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-21 12:25:55,471 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
... (130 earlier lines - see full log file)
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
## Ledger health — 2026-08-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   975 | WARN | <<<
| Missing exit records (post) |   975 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     1 | INFO |
| Total closed lots           |  1770 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=821 med=-47.5% | TAINTED n=1761 med=-39.3% | KEEP-only n=294 med=+37.5% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=317.19 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | MomReversal | 15 | 47% | +0.39% | -0.60% | -1.81% | 1.99 | 1.7d | $+3.53 | WATCH |
| 3 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260821T163050Z

- UTC timestamp: `20260821T163050Z`
- GitHub run: [#7774](https://github.com/28twagg-ops/TradingBot/actions/runs/32503229627)
- Run id: `32503229627`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`10s`
- Full logs: `logs/action_runs/20260821T163050Z_live_bot.log`, `logs/action_runs/20260821T163050Z_live_options.log`, `logs/action_runs/20260821T163050Z_options_bot.log`


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
{"ts_et":"2026-08-21T12:30:56.095822-04:00","date":"2026-08-21","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":2.0,"phases_s":{"reconcile":0.04,"cancel":0.02,"manage":1.47,"protective_stops":0.02},"signals":0,"placed":0,"equity":999996.97,"open_positions":1,"pending_orders":0,"open_lots":1,"submitted_today":1,"filled_today":1,"unattributed_contracts":0,"top_signals":[],"github_run":"7774","github_run_id":"32503229627","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
16:30:51  INFO      Mode: exits
16:30:52  INFO        Daily log -> logs/daily/2026-08-21.md
16:30:52  INFO        Daily log reconciled -> logs/daily/2026-08-21.md (4 ledger rows)
16:30:52  INFO        place_all_stops: checking 3 positions...
16:30:52  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
16:30:52  INFO        [positions] 1/1 (1 valid)
16:30:53  INFO        Daily log -> logs/daily/2026-08-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:30 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $317.22|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AON  P&L +1.3%  $+0.88                                            HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  COST260828C01000000     $0.63    $0.45    -28.6%   $-18.00   $45.00   |
|  WMT260821C00110000      $0.09    $0.00    -100.0%  $-9.00    $0.00    |
|                                                                        |
|  Options open P&L                                               $-27.00|
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
=== options_live_micro LIVE 2026-08-21T12:30:54.084047-04:00 share=25% ===
2026-08-21 12:30:54,084 INFO === options_live_micro LIVE 2026-08-21T12:30:54.084047-04:00 share=25% ===
Live account equity $317.22 cash $201.38 #225458845 options_level=3
2026-08-21 12:30:54,146 INFO Live account equity $317.22 cash $201.38 #225458845 options_level=3
Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
2026-08-21 12:30:54,166 INFO Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
Live micro cancel stale sell WMT260821C00110000 id=19e93439-249a-4269-89b3-d93020f08786 cid=OLX|352eb08e31a1 broker_sym='WMT260821C00110000'
2026-08-21 12:30:54,175 INFO Live micro cancel stale sell WMT260821C00110000 id=19e93439-249a-4269-89b3-d93020f08786 cid=OLX|352eb08e31a1 broker_sym='WMT260821C00110000'
Live micro orphan_adopt WMT260821C00110000 x1 entry=0.09
2026-08-21 12:30:54,175 INFO Live micro orphan_adopt WMT260821C00110000 x1 entry=0.09
Live micro hold ORPHAN COST260828C01000000 -28.6% (tp +50% / sl -40%)
2026-08-21 12:30:54,208 INFO Live micro hold ORPHAN COST260828C01000000 -28.6% (tp +50% / sl -40%)
Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
2026-08-21 12:30:54,224 INFO Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
Live micro cancel stale sell WMT260821C00110000 id=19e93439-249a-4269-89b3-d93020f08786 cid=OLX|352eb08e31a1 broker_sym='WMT260821C00110000'
2026-08-21 12:30:54,231 INFO Live micro cancel stale sell WMT260821C00110000 id=19e93439-249a-4269-89b3-d93020f08786 cid=OLX|352eb08e31a1 broker_sym='WMT260821C00110000'
LIVE EXIT stop_loss (-100.0%) WMT260821C00110000 x1 limit=0.01 id=530e4157-b3a6-4f7d-9e93-90e57300c899
2026-08-21 12:30:54,594 INFO LIVE EXIT stop_loss (-100.0%) WMT260821C00110000 x1 limit=0.01 id=530e4157-b3a6-4f7d-9e93-90e57300c899
Live micro cancel-scan COST260828C01000000: symbol-scoped n=1
2026-08-21 12:30:54,604 INFO Live micro cancel-scan COST260828C01000000: symbol-scoped n=1
Live micro cancel-scan COST260828C01000000: no non-OLS sell to cancel
2026-08-21 12:30:54,604 INFO Live micro cancel-scan COST260828C01000000: no non-OLS sell to cancel
LIVE PROT check COST260828C01000000: have_ols=True open_matched=1 ols_id=ab9b8a23-2f03-4a3a-b25a-799118f49712 ols_type=stop
2026-08-21 12:30:54,621 INFO LIVE PROT check COST260828C01000000: have_ols=True open_matched=1 ols_id=ab9b8a23-2f03-4a3a-b25a-799118f49712 ols_type=stop
Live micro: manage/exits only
2026-08-21 12:30:54,621 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-21 12:30:54,637 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
... (130 earlier lines - see full log file)
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
## Ledger health — 2026-08-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   975 | WARN | <<<
| Missing exit records (post) |   975 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     1 | INFO |
| Total closed lots           |  1770 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=821 med=-47.5% | TAINTED n=1761 med=-39.3% | KEEP-only n=294 med=+37.5% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=317.22 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | MomReversal | 15 | 47% | +0.39% | -0.60% | -1.81% | 1.99 | 1.7d | $+3.53 | WATCH |
| 3 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260821T163551Z

- UTC timestamp: `20260821T163551Z`
- GitHub run: [#7775](https://github.com/28twagg-ops/TradingBot/actions/runs/32503661706)
- Run id: `32503661706`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`3s`
- Paper options: exit=`0`, duration=`11s`
- Full logs: `logs/action_runs/20260821T163551Z_live_bot.log`, `logs/action_runs/20260821T163551Z_live_options.log`, `logs/action_runs/20260821T163551Z_options_bot.log`


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
{"ts_et":"2026-08-21T12:35:58.725930-04:00","date":"2026-08-21","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":3.3,"phases_s":{"reconcile":0.31,"cancel":0.14,"manage":1.96,"protective_stops":0.14},"signals":0,"placed":0,"equity":999993.97,"open_positions":1,"pending_orders":0,"open_lots":1,"submitted_today":1,"filled_today":1,"unattributed_contracts":0,"top_signals":[],"github_run":"7775","github_run_id":"32503661706","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
16:35:52  INFO      Mode: exits
16:35:53  INFO        Daily log -> logs/daily/2026-08-21.md
16:35:53  INFO        Daily log reconciled -> logs/daily/2026-08-21.md (4 ledger rows)
16:35:53  INFO        place_all_stops: checking 3 positions...
16:35:53  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
16:35:54  INFO        [positions] 1/1 (1 valid)
16:35:54  INFO        Daily log -> logs/daily/2026-08-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:35 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $317.23|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AON  P&L +1.3%  $+0.89                                            HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  COST260828C01000000     $0.63    $0.45    -28.6%   $-18.00   $45.00   |
|  WMT260821C00110000      $0.09    $0.00    -100.0%  $-9.00    $0.00    |
|                                                                        |
|  Options open P&L                                               $-27.00|
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
=== options_live_micro LIVE 2026-08-21T12:35:55.325777-04:00 share=25% ===
2026-08-21 12:35:55,325 INFO === options_live_micro LIVE 2026-08-21T12:35:55.325777-04:00 share=25% ===
Live account equity $317.23 cash $201.38 #225458845 options_level=3
2026-08-21 12:35:55,578 INFO Live account equity $317.23 cash $201.38 #225458845 options_level=3
Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
2026-08-21 12:35:55,716 INFO Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
Live micro cancel stale sell WMT260821C00110000 id=530e4157-b3a6-4f7d-9e93-90e57300c899 cid=OLX|1415109bc427 broker_sym='WMT260821C00110000'
2026-08-21 12:35:55,785 INFO Live micro cancel stale sell WMT260821C00110000 id=530e4157-b3a6-4f7d-9e93-90e57300c899 cid=OLX|1415109bc427 broker_sym='WMT260821C00110000'
Live micro orphan_adopt WMT260821C00110000 x1 entry=0.09
2026-08-21 12:35:55,786 INFO Live micro orphan_adopt WMT260821C00110000 x1 entry=0.09
Live micro hold ORPHAN COST260828C01000000 -28.6% (tp +50% / sl -40%)
2026-08-21 12:35:55,857 INFO Live micro hold ORPHAN COST260828C01000000 -28.6% (tp +50% / sl -40%)
Live micro cancel-scan WMT260821C00110000: symbol-scoped empty; open_book n=1
2026-08-21 12:35:56,068 INFO Live micro cancel-scan WMT260821C00110000: symbol-scoped empty; open_book n=1
  open_order id=ab9b8a23-2f03-4a3a-b25a-799118f49712 sym='COST260828C01000000' side=OrderSide.SELL status=OrderStatus.NEW cid='OLS|1f926a83750f' type=OrderType.STOP
2026-08-21 12:35:56,068 INFO   open_order id=ab9b8a23-2f03-4a3a-b25a-799118f49712 sym='COST260828C01000000' side=OrderSide.SELL status=OrderStatus.NEW cid='OLS|1f926a83750f' type=OrderType.STOP
Live micro cancel-scan WMT260821C00110000: matched n=0
2026-08-21 12:35:56,068 INFO Live micro cancel-scan WMT260821C00110000: matched n=0
Live micro cancel-scan WMT260821C00110000: no non-OLS sell to cancel
2026-08-21 12:35:56,068 INFO Live micro cancel-scan WMT260821C00110000: no non-OLS sell to cancel
LIVE EXIT stop_loss (-100.0%) WMT260821C00110000 x1 limit=0.01 id=6329be1e-fba2-4b40-9c40-c1c9ab3d30f5
2026-08-21 12:35:56,761 INFO LIVE EXIT stop_loss (-100.0%) WMT260821C00110000 x1 limit=0.01 id=6329be1e-fba2-4b40-9c40-c1c9ab3d30f5
Live micro cancel-scan COST260828C01000000: symbol-scoped n=1
2026-08-21 12:35:56,831 INFO Live micro cancel-scan COST260828C01000000: symbol-scoped n=1
Live micro cancel-scan COST260828C01000000: no non-OLS sell to cancel
2026-08-21 12:35:56,831 INFO Live micro cancel-scan COST260828C01000000: no non-OLS sell to cancel
LIVE PROT check COST260828C01000000: have_ols=True open_matched=1 ols_id=ab9b8a23-2f03-4a3a-b25a-799118f49712 ols_type=stop
2026-08-21 12:35:56,971 INFO LIVE PROT check COST260828C01000000: have_ols=True open_matched=1 ols_id=ab9b8a23-2f03-4a3a-b25a-799118f49712 ols_type=stop
Live micro: manage/exits only
2026-08-21 12:35:56,971 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-21 12:35:57,053 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
... (130 earlier lines - see full log file)
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
## Ledger health — 2026-08-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   975 | WARN | <<<
| Missing exit records (post) |   975 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     1 | INFO |
| Total closed lots           |  1770 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=821 med=-47.5% | TAINTED n=1761 med=-39.3% | KEEP-only n=294 med=+37.5% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=317.23 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | MomReversal | 15 | 47% | +0.39% | -0.60% | -1.81% | 1.99 | 1.7d | $+3.53 | WATCH |
| 3 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260821T164049Z

- UTC timestamp: `20260821T164049Z`
- GitHub run: [#7776](https://github.com/28twagg-ops/TradingBot/actions/runs/32504095544)
- Run id: `32504095544`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`10s`
- Full logs: `logs/action_runs/20260821T164049Z_live_bot.log`, `logs/action_runs/20260821T164049Z_live_options.log`, `logs/action_runs/20260821T164049Z_options_bot.log`


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
{"ts_et":"2026-08-21T12:40:54.254452-04:00","date":"2026-08-21","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":1.2,"phases_s":{"reconcile":0.06,"cancel":0.02,"manage":0.7,"protective_stops":0.02},"signals":0,"placed":0,"equity":999996.97,"open_positions":1,"pending_orders":0,"open_lots":1,"submitted_today":1,"filled_today":1,"unattributed_contracts":0,"top_signals":[],"github_run":"7776","github_run_id":"32504095544","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
16:40:50  INFO      Mode: exits
16:40:51  INFO        Daily log -> logs/daily/2026-08-21.md
16:40:51  INFO        Daily log reconciled -> logs/daily/2026-08-21.md (4 ledger rows)
16:40:51  INFO        place_all_stops: checking 3 positions...
16:40:51  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
16:40:51  INFO        [positions] 1/1 (1 valid)
16:40:51  INFO        Daily log -> logs/daily/2026-08-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:40 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $317.24|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AON  P&L +1.3%  $+0.90                                            HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  COST260828C01000000     $0.63    $0.45    -28.6%   $-18.00   $45.00   |
|  WMT260821C00110000      $0.09    $0.00    -100.0%  $-9.00    $0.00    |
|                                                                        |
|  Options open P&L                                               $-27.00|
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
=== options_live_micro LIVE 2026-08-21T12:40:52.461151-04:00 share=25% ===
2026-08-21 12:40:52,461 INFO === options_live_micro LIVE 2026-08-21T12:40:52.461151-04:00 share=25% ===
Live account equity $317.23 cash $201.38 #225458845 options_level=3
2026-08-21 12:40:52,533 INFO Live account equity $317.23 cash $201.38 #225458845 options_level=3
Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
2026-08-21 12:40:52,556 INFO Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
Live micro cancel stale sell WMT260821C00110000 id=6329be1e-fba2-4b40-9c40-c1c9ab3d30f5 cid=OLX|c409eaa088fe broker_sym='WMT260821C00110000'
2026-08-21 12:40:52,564 INFO Live micro cancel stale sell WMT260821C00110000 id=6329be1e-fba2-4b40-9c40-c1c9ab3d30f5 cid=OLX|c409eaa088fe broker_sym='WMT260821C00110000'
Live micro orphan_adopt WMT260821C00110000 x1 entry=0.09
2026-08-21 12:40:52,565 INFO Live micro orphan_adopt WMT260821C00110000 x1 entry=0.09
Live micro hold ORPHAN COST260828C01000000 -28.6% (tp +50% / sl -40%)
2026-08-21 12:40:52,575 INFO Live micro hold ORPHAN COST260828C01000000 -28.6% (tp +50% / sl -40%)
Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
2026-08-21 12:40:52,593 INFO Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
Live micro cancel stale sell WMT260821C00110000 id=6329be1e-fba2-4b40-9c40-c1c9ab3d30f5 cid=OLX|c409eaa088fe broker_sym='WMT260821C00110000'
2026-08-21 12:40:52,599 INFO Live micro cancel stale sell WMT260821C00110000 id=6329be1e-fba2-4b40-9c40-c1c9ab3d30f5 cid=OLX|c409eaa088fe broker_sym='WMT260821C00110000'
LIVE EXIT stop_loss (-100.0%) WMT260821C00110000 x1 limit=0.01 id=af13ef39-d311-496b-a682-fd3b623f6411
2026-08-21 12:40:52,810 INFO LIVE EXIT stop_loss (-100.0%) WMT260821C00110000 x1 limit=0.01 id=af13ef39-d311-496b-a682-fd3b623f6411
Live micro cancel-scan COST260828C01000000: symbol-scoped n=1
2026-08-21 12:40:52,819 INFO Live micro cancel-scan COST260828C01000000: symbol-scoped n=1
Live micro cancel-scan COST260828C01000000: no non-OLS sell to cancel
2026-08-21 12:40:52,819 INFO Live micro cancel-scan COST260828C01000000: no non-OLS sell to cancel
LIVE PROT check COST260828C01000000: have_ols=True open_matched=1 ols_id=ab9b8a23-2f03-4a3a-b25a-799118f49712 ols_type=stop
2026-08-21 12:40:52,843 INFO LIVE PROT check COST260828C01000000: have_ols=True open_matched=1 ols_id=ab9b8a23-2f03-4a3a-b25a-799118f49712 ols_type=stop
Live micro: manage/exits only
2026-08-21 12:40:52,843 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-21 12:40:52,851 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
... (130 earlier lines - see full log file)
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
## Ledger health — 2026-08-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   975 | WARN | <<<
| Missing exit records (post) |   975 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     1 | INFO |
| Total closed lots           |  1770 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=821 med=-47.5% | TAINTED n=1761 med=-39.3% | KEEP-only n=294 med=+37.5% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=317.24 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | MomReversal | 15 | 47% | +0.39% | -0.60% | -1.81% | 1.99 | 1.7d | $+3.53 | WATCH |
| 3 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260821T164555Z

- UTC timestamp: `20260821T164555Z`
- GitHub run: [#7777](https://github.com/28twagg-ops/TradingBot/actions/runs/32504535457)
- Run id: `32504535457`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`7s`
- Full logs: `logs/action_runs/20260821T164555Z_live_bot.log`, `logs/action_runs/20260821T164555Z_live_options.log`, `logs/action_runs/20260821T164555Z_options_bot.log`


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
{"ts_et":"2026-08-21T12:46:01.644058-04:00","date":"2026-08-21","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":1.6,"phases_s":{"reconcile":0.13,"cancel":0.07,"manage":0.94,"protective_stops":0.06},"signals":0,"placed":0,"equity":999995.97,"open_positions":1,"pending_orders":0,"open_lots":1,"submitted_today":1,"filled_today":1,"unattributed_contracts":0,"top_signals":[],"github_run":"7777","github_run_id":"32504535457","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
16:45:57  INFO      Mode: exits
16:45:58  INFO        Daily log -> logs/daily/2026-08-21.md
16:45:58  INFO        Daily log reconciled -> logs/daily/2026-08-21.md (4 ledger rows)
16:45:58  INFO        place_all_stops: checking 3 positions...
16:45:58  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
16:45:58  INFO        [positions] 1/1 (1 valid)
16:45:58  INFO        Daily log -> logs/daily/2026-08-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:45 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $317.10|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AON  P&L +1.1%  $+0.76                                            HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  COST260828C01000000     $0.63    $0.45    -28.6%   $-18.00   $45.00   |
|  WMT260821C00110000      $0.09    $0.00    -100.0%  $-9.00    $0.00    |
|                                                                        |
|  Options open P&L                                               $-27.00|
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
=== options_live_micro LIVE 2026-08-21T12:45:59.534442-04:00 share=25% ===
2026-08-21 12:45:59,534 INFO === options_live_micro LIVE 2026-08-21T12:45:59.534442-04:00 share=25% ===
Live account equity $317.10 cash $201.38 #225458845 options_level=3
2026-08-21 12:45:59,700 INFO Live account equity $317.10 cash $201.38 #225458845 options_level=3
Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
2026-08-21 12:45:59,782 INFO Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
Live micro cancel stale sell WMT260821C00110000 id=af13ef39-d311-496b-a682-fd3b623f6411 cid=OLX|cbc178cb368a broker_sym='WMT260821C00110000'
2026-08-21 12:45:59,822 INFO Live micro cancel stale sell WMT260821C00110000 id=af13ef39-d311-496b-a682-fd3b623f6411 cid=OLX|cbc178cb368a broker_sym='WMT260821C00110000'
Live micro orphan_adopt WMT260821C00110000 x1 entry=0.09
2026-08-21 12:45:59,822 INFO Live micro orphan_adopt WMT260821C00110000 x1 entry=0.09
Live micro hold ORPHAN COST260828C01000000 -28.6% (tp +50% / sl -40%)
2026-08-21 12:45:59,863 INFO Live micro hold ORPHAN COST260828C01000000 -28.6% (tp +50% / sl -40%)
Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
2026-08-21 12:45:59,943 INFO Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
Live micro cancel stale sell WMT260821C00110000 id=af13ef39-d311-496b-a682-fd3b623f6411 cid=OLX|cbc178cb368a broker_sym='WMT260821C00110000'
2026-08-21 12:45:59,982 INFO Live micro cancel stale sell WMT260821C00110000 id=af13ef39-d311-496b-a682-fd3b623f6411 cid=OLX|cbc178cb368a broker_sym='WMT260821C00110000'
LIVE EXIT stop_loss (-100.0%) WMT260821C00110000 x1 limit=0.01 id=54560199-e3c6-4592-9308-3e05cb2868de
2026-08-21 12:46:00,377 INFO LIVE EXIT stop_loss (-100.0%) WMT260821C00110000 x1 limit=0.01 id=54560199-e3c6-4592-9308-3e05cb2868de
Live micro cancel-scan COST260828C01000000: symbol-scoped n=1
2026-08-21 12:46:00,416 INFO Live micro cancel-scan COST260828C01000000: symbol-scoped n=1
Live micro cancel-scan COST260828C01000000: no non-OLS sell to cancel
2026-08-21 12:46:00,416 INFO Live micro cancel-scan COST260828C01000000: no non-OLS sell to cancel
LIVE PROT check COST260828C01000000: have_ols=True open_matched=1 ols_id=ab9b8a23-2f03-4a3a-b25a-799118f49712 ols_type=stop
2026-08-21 12:46:00,502 INFO LIVE PROT check COST260828C01000000: have_ols=True open_matched=1 ols_id=ab9b8a23-2f03-4a3a-b25a-799118f49712 ols_type=stop
Live micro: manage/exits only
2026-08-21 12:46:00,502 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-21 12:46:00,552 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
... (130 earlier lines - see full log file)
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
## Ledger health — 2026-08-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   975 | WARN | <<<
| Missing exit records (post) |   975 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     1 | INFO |
| Total closed lots           |  1770 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=821 med=-47.5% | TAINTED n=1761 med=-39.3% | KEEP-only n=294 med=+37.5% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=317.1 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | MomReversal | 15 | 47% | +0.39% | -0.60% | -1.81% | 1.99 | 1.7d | $+3.53 | WATCH |
| 3 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260821T165101Z

- UTC timestamp: `20260821T165101Z`
- GitHub run: [#7778](https://github.com/28twagg-ops/TradingBot/actions/runs/32504972056)
- Run id: `32504972056`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`9s`
- Full logs: `logs/action_runs/20260821T165101Z_live_bot.log`, `logs/action_runs/20260821T165101Z_live_options.log`, `logs/action_runs/20260821T165101Z_options_bot.log`


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
{"ts_et":"2026-08-21T12:51:07.833704-04:00","date":"2026-08-21","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":1.8,"phases_s":{"reconcile":0.13,"cancel":0.07,"manage":1.01,"protective_stops":0.08},"signals":0,"placed":0,"equity":999994.97,"open_positions":1,"pending_orders":0,"open_lots":1,"submitted_today":1,"filled_today":1,"unattributed_contracts":0,"top_signals":[],"github_run":"7778","github_run_id":"32504972056","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
16:51:02  INFO      Mode: exits
16:51:03  INFO        Daily log -> logs/daily/2026-08-21.md
16:51:03  INFO        Daily log reconciled -> logs/daily/2026-08-21.md (4 ledger rows)
16:51:03  INFO        place_all_stops: checking 3 positions...
16:51:03  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
16:51:03  INFO        [positions] 1/1 (1 valid)
16:51:04  INFO        Daily log -> logs/daily/2026-08-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:51 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $317.12|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AON  P&L +1.1%  $+0.78                                            HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  COST260828C01000000     $0.63    $0.45    -28.6%   $-18.00   $45.00   |
|  WMT260821C00110000      $0.09    $0.00    -100.0%  $-9.00    $0.00    |
|                                                                        |
|  Options open P&L                                               $-27.00|
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
=== options_live_micro LIVE 2026-08-21T12:51:04.883856-04:00 share=25% ===
2026-08-21 12:51:04,883 INFO === options_live_micro LIVE 2026-08-21T12:51:04.883856-04:00 share=25% ===
Live account equity $317.12 cash $201.38 #225458845 options_level=3
2026-08-21 12:51:05,066 INFO Live account equity $317.12 cash $201.38 #225458845 options_level=3
Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
2026-08-21 12:51:05,160 INFO Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
Live micro cancel stale sell WMT260821C00110000 id=54560199-e3c6-4592-9308-3e05cb2868de cid=OLX|30ee1a07359f broker_sym='WMT260821C00110000'
2026-08-21 12:51:05,208 INFO Live micro cancel stale sell WMT260821C00110000 id=54560199-e3c6-4592-9308-3e05cb2868de cid=OLX|30ee1a07359f broker_sym='WMT260821C00110000'
Live micro orphan_adopt WMT260821C00110000 x1 entry=0.09
2026-08-21 12:51:05,209 INFO Live micro orphan_adopt WMT260821C00110000 x1 entry=0.09
Live micro hold ORPHAN COST260828C01000000 -28.6% (tp +50% / sl -40%)
2026-08-21 12:51:05,262 INFO Live micro hold ORPHAN COST260828C01000000 -28.6% (tp +50% / sl -40%)
Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
2026-08-21 12:51:05,356 INFO Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
Live micro cancel stale sell WMT260821C00110000 id=54560199-e3c6-4592-9308-3e05cb2868de cid=OLX|30ee1a07359f broker_sym='WMT260821C00110000'
2026-08-21 12:51:05,402 INFO Live micro cancel stale sell WMT260821C00110000 id=54560199-e3c6-4592-9308-3e05cb2868de cid=OLX|30ee1a07359f broker_sym='WMT260821C00110000'
LIVE EXIT stop_loss (-100.0%) WMT260821C00110000 x1 limit=0.01 id=4582846c-9325-4dfb-bf97-1cf6fca60fc6
2026-08-21 12:51:05,882 INFO LIVE EXIT stop_loss (-100.0%) WMT260821C00110000 x1 limit=0.01 id=4582846c-9325-4dfb-bf97-1cf6fca60fc6
Live micro cancel-scan COST260828C01000000: symbol-scoped n=1
2026-08-21 12:51:05,931 INFO Live micro cancel-scan COST260828C01000000: symbol-scoped n=1
Live micro cancel-scan COST260828C01000000: no non-OLS sell to cancel
2026-08-21 12:51:05,932 INFO Live micro cancel-scan COST260828C01000000: no non-OLS sell to cancel
LIVE PROT check COST260828C01000000: have_ols=True open_matched=1 ols_id=ab9b8a23-2f03-4a3a-b25a-799118f49712 ols_type=stop
2026-08-21 12:51:06,029 INFO LIVE PROT check COST260828C01000000: have_ols=True open_matched=1 ols_id=ab9b8a23-2f03-4a3a-b25a-799118f49712 ols_type=stop
Live micro: manage/exits only
2026-08-21 12:51:06,029 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-21 12:51:06,077 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
... (130 earlier lines - see full log file)
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
## Ledger health — 2026-08-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   975 | WARN | <<<
| Missing exit records (post) |   975 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     1 | INFO |
| Total closed lots           |  1770 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=821 med=-47.5% | TAINTED n=1761 med=-39.3% | KEEP-only n=294 med=+37.5% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=317.12 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | MomReversal | 15 | 47% | +0.39% | -0.60% | -1.81% | 1.99 | 1.7d | $+3.53 | WATCH |
| 3 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260821T165550Z

- UTC timestamp: `20260821T165550Z`
- GitHub run: [#7779](https://github.com/28twagg-ops/TradingBot/actions/runs/32505406321)
- Run id: `32505406321`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`9s`
- Full logs: `logs/action_runs/20260821T165550Z_live_bot.log`, `logs/action_runs/20260821T165550Z_live_options.log`, `logs/action_runs/20260821T165550Z_options_bot.log`


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
{"ts_et":"2026-08-21T12:55:54.369644-04:00","date":"2026-08-21","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":1.4,"phases_s":{"reconcile":0.06,"cancel":0.03,"manage":0.84,"protective_stops":0.03},"signals":0,"placed":0,"equity":999994.97,"open_positions":1,"pending_orders":0,"open_lots":1,"submitted_today":1,"filled_today":1,"unattributed_contracts":0,"top_signals":[],"github_run":"7779","github_run_id":"32505406321","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
16:55:51  INFO      Mode: exits
16:55:51  INFO        Daily log -> logs/daily/2026-08-21.md
16:55:51  INFO        Daily log reconciled -> logs/daily/2026-08-21.md (4 ledger rows)
16:55:51  INFO        place_all_stops: checking 3 positions...
16:55:51  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
16:55:51  INFO        [positions] 1/1 (1 valid)
16:55:51  INFO        Daily log -> logs/daily/2026-08-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:55 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $317.17|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AON  P&L +1.2%  $+0.83                                            HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  COST260828C01000000     $0.63    $0.45    -28.6%   $-18.00   $45.00   |
|  WMT260821C00110000      $0.09    $0.00    -100.0%  $-9.00    $0.00    |
|                                                                        |
|  Options open P&L                                               $-27.00|
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
=== options_live_micro LIVE 2026-08-21T12:55:52.504962-04:00 share=25% ===
2026-08-21 12:55:52,505 INFO === options_live_micro LIVE 2026-08-21T12:55:52.504962-04:00 share=25% ===
Live account equity $317.17 cash $201.38 #225458845 options_level=3
2026-08-21 12:55:52,583 INFO Live account equity $317.17 cash $201.38 #225458845 options_level=3
Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
2026-08-21 12:55:52,608 INFO Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
Live micro cancel stale sell WMT260821C00110000 id=4582846c-9325-4dfb-bf97-1cf6fca60fc6 cid=OLX|dea837c1e092 broker_sym='WMT260821C00110000'
2026-08-21 12:55:52,619 INFO Live micro cancel stale sell WMT260821C00110000 id=4582846c-9325-4dfb-bf97-1cf6fca60fc6 cid=OLX|dea837c1e092 broker_sym='WMT260821C00110000'
Live micro orphan_adopt WMT260821C00110000 x1 entry=0.09
2026-08-21 12:55:52,620 INFO Live micro orphan_adopt WMT260821C00110000 x1 entry=0.09
Live micro hold ORPHAN COST260828C01000000 -28.6% (tp +50% / sl -40%)
2026-08-21 12:55:52,632 INFO Live micro hold ORPHAN COST260828C01000000 -28.6% (tp +50% / sl -40%)
Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
2026-08-21 12:55:52,657 INFO Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
Live micro cancel stale sell WMT260821C00110000 id=4582846c-9325-4dfb-bf97-1cf6fca60fc6 cid=OLX|dea837c1e092 broker_sym='WMT260821C00110000'
2026-08-21 12:55:52,668 INFO Live micro cancel stale sell WMT260821C00110000 id=4582846c-9325-4dfb-bf97-1cf6fca60fc6 cid=OLX|dea837c1e092 broker_sym='WMT260821C00110000'
LIVE EXIT stop_loss (-100.0%) WMT260821C00110000 x1 limit=0.01 id=e9982362-2b87-4035-b704-9857af1a5bc5
2026-08-21 12:55:52,894 INFO LIVE EXIT stop_loss (-100.0%) WMT260821C00110000 x1 limit=0.01 id=e9982362-2b87-4035-b704-9857af1a5bc5
Live micro cancel-scan COST260828C01000000: symbol-scoped n=1
2026-08-21 12:55:52,906 INFO Live micro cancel-scan COST260828C01000000: symbol-scoped n=1
Live micro cancel-scan COST260828C01000000: no non-OLS sell to cancel
2026-08-21 12:55:52,906 INFO Live micro cancel-scan COST260828C01000000: no non-OLS sell to cancel
LIVE PROT check COST260828C01000000: have_ols=True open_matched=1 ols_id=ab9b8a23-2f03-4a3a-b25a-799118f49712 ols_type=stop
2026-08-21 12:55:52,931 INFO LIVE PROT check COST260828C01000000: have_ols=True open_matched=1 ols_id=ab9b8a23-2f03-4a3a-b25a-799118f49712 ols_type=stop
Live micro: manage/exits only
2026-08-21 12:55:52,931 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-21 12:55:52,944 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
... (130 earlier lines - see full log file)
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
## Ledger health — 2026-08-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   975 | WARN | <<<
| Missing exit records (post) |   975 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     1 | INFO |
| Total closed lots           |  1770 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=821 med=-47.5% | TAINTED n=1761 med=-39.3% | KEEP-only n=294 med=+37.5% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=317.17 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | MomReversal | 15 | 47% | +0.39% | -0.60% | -1.81% | 1.99 | 1.7d | $+3.53 | WATCH |
| 3 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260821T170055Z

- UTC timestamp: `20260821T170055Z`
- GitHub run: [#7780](https://github.com/28twagg-ops/TradingBot/actions/runs/32505836359)
- Run id: `32505836359`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`11s`
- Full logs: `logs/action_runs/20260821T170055Z_live_bot.log`, `logs/action_runs/20260821T170055Z_live_options.log`, `logs/action_runs/20260821T170055Z_options_bot.log`


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
{"ts_et":"2026-08-21T13:01:03.145994-04:00","date":"2026-08-21","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":4.1,"phases_s":{"reconcile":0.26,"cancel":0.12,"manage":3.04,"protective_stops":0.12},"signals":0,"placed":0,"equity":999994.97,"open_positions":1,"pending_orders":0,"open_lots":1,"submitted_today":1,"filled_today":1,"unattributed_contracts":0,"top_signals":[],"github_run":"7780","github_run_id":"32505836359","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
17:00:56  INFO      Mode: exits
17:00:57  INFO        Daily log -> logs/daily/2026-08-21.md
17:00:57  INFO        Daily log reconciled -> logs/daily/2026-08-21.md (4 ledger rows)
17:00:57  INFO        place_all_stops: checking 3 positions...
17:00:57  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
17:00:58  INFO        [positions] 1/1 (1 valid)
17:00:59  INFO        Daily log -> logs/daily/2026-08-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:00 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $317.18|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AON  P&L +1.2%  $+0.84                                            HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  COST260828C01000000     $0.63    $0.45    -28.6%   $-18.00   $45.00   |
|  WMT260821C00110000      $0.09    $0.00    -100.0%  $-9.00    $0.00    |
|                                                                        |
|  Options open P&L                                               $-27.00|
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
=== options_live_micro LIVE 2026-08-21T13:00:59.757040-04:00 share=25% ===
2026-08-21 13:00:59,757 INFO === options_live_micro LIVE 2026-08-21T13:00:59.757040-04:00 share=25% ===
Live account equity $317.18 cash $201.38 #225458845 options_level=3
2026-08-21 13:00:59,961 INFO Live account equity $317.18 cash $201.38 #225458845 options_level=3
Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
2026-08-21 13:01:00,090 INFO Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
Live micro cancel stale sell WMT260821C00110000 id=e9982362-2b87-4035-b704-9857af1a5bc5 cid=OLX|da43c84cb023 broker_sym='WMT260821C00110000'
2026-08-21 13:01:00,148 INFO Live micro cancel stale sell WMT260821C00110000 id=e9982362-2b87-4035-b704-9857af1a5bc5 cid=OLX|da43c84cb023 broker_sym='WMT260821C00110000'
Live micro orphan_adopt WMT260821C00110000 x1 entry=0.09
2026-08-21 13:01:00,148 INFO Live micro orphan_adopt WMT260821C00110000 x1 entry=0.09
Live micro hold ORPHAN COST260828C01000000 -28.6% (tp +50% / sl -40%)
2026-08-21 13:01:00,295 INFO Live micro hold ORPHAN COST260828C01000000 -28.6% (tp +50% / sl -40%)
Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
2026-08-21 13:01:00,414 INFO Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
Live micro cancel stale sell WMT260821C00110000 id=e9982362-2b87-4035-b704-9857af1a5bc5 cid=OLX|da43c84cb023 broker_sym='WMT260821C00110000'
2026-08-21 13:01:00,471 INFO Live micro cancel stale sell WMT260821C00110000 id=e9982362-2b87-4035-b704-9857af1a5bc5 cid=OLX|da43c84cb023 broker_sym='WMT260821C00110000'
LIVE EXIT stop_loss (-100.0%) WMT260821C00110000 x1 limit=0.01 id=431becac-2d69-498b-9383-531e534cec29
2026-08-21 13:01:01,372 INFO LIVE EXIT stop_loss (-100.0%) WMT260821C00110000 x1 limit=0.01 id=431becac-2d69-498b-9383-531e534cec29
Live micro cancel-scan COST260828C01000000: symbol-scoped n=1
2026-08-21 13:01:01,430 INFO Live micro cancel-scan COST260828C01000000: symbol-scoped n=1
Live micro cancel-scan COST260828C01000000: no non-OLS sell to cancel
2026-08-21 13:01:01,431 INFO Live micro cancel-scan COST260828C01000000: no non-OLS sell to cancel
LIVE PROT check COST260828C01000000: have_ols=True open_matched=1 ols_id=ab9b8a23-2f03-4a3a-b25a-799118f49712 ols_type=stop
2026-08-21 13:01:01,557 INFO LIVE PROT check COST260828C01000000: have_ols=True open_matched=1 ols_id=ab9b8a23-2f03-4a3a-b25a-799118f49712 ols_type=stop
Live micro: manage/exits only
2026-08-21 13:01:01,557 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-21 13:01:01,617 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
... (130 earlier lines - see full log file)
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
## Ledger health — 2026-08-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   975 | WARN | <<<
| Missing exit records (post) |   975 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     1 | INFO |
| Total closed lots           |  1770 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=821 med=-47.5% | TAINTED n=1761 med=-39.3% | KEEP-only n=294 med=+37.5% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=317.18 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | MomReversal | 15 | 47% | +0.39% | -0.60% | -1.81% | 1.99 | 1.7d | $+3.53 | WATCH |
| 3 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260821T170548Z

- UTC timestamp: `20260821T170548Z`
- GitHub run: [#7781](https://github.com/28twagg-ops/TradingBot/actions/runs/32506283846)
- Run id: `32506283846`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`10s`
- Full logs: `logs/action_runs/20260821T170548Z_live_bot.log`, `logs/action_runs/20260821T170548Z_live_options.log`, `logs/action_runs/20260821T170548Z_options_bot.log`


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
{"ts_et":"2026-08-21T13:05:52.979952-04:00","date":"2026-08-21","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":1.4,"phases_s":{"reconcile":0.04,"cancel":0.02,"manage":0.61,"protective_stops":0.02},"signals":0,"placed":0,"equity":999994.97,"open_positions":1,"pending_orders":0,"open_lots":1,"submitted_today":1,"filled_today":1,"unattributed_contracts":0,"top_signals":[],"github_run":"7781","github_run_id":"32506283846","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
17:05:49  INFO      Mode: exits
17:05:49  INFO        Daily log -> logs/daily/2026-08-21.md
17:05:49  INFO        Daily log reconciled -> logs/daily/2026-08-21.md (4 ledger rows)
17:05:49  INFO        place_all_stops: checking 3 positions...
17:05:49  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
17:05:50  INFO        [positions] 1/1 (1 valid)
17:05:50  INFO        Daily log -> logs/daily/2026-08-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:05 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $317.13|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AON  P&L +1.1%  $+0.79                                            HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  COST260828C01000000     $0.63    $0.45    -28.6%   $-18.00   $45.00   |
|  WMT260821C00110000      $0.09    $0.00    -100.0%  $-9.00    $0.00    |
|                                                                        |
|  Options open P&L                                               $-27.00|
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
=== options_live_micro LIVE 2026-08-21T13:05:51.081918-04:00 share=25% ===
2026-08-21 13:05:51,081 INFO === options_live_micro LIVE 2026-08-21T13:05:51.081918-04:00 share=25% ===
Live account equity $317.13 cash $201.38 #225458845 options_level=3
2026-08-21 13:05:51,132 INFO Live account equity $317.13 cash $201.38 #225458845 options_level=3
Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
2026-08-21 13:05:51,157 INFO Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
Live micro cancel stale sell WMT260821C00110000 id=431becac-2d69-498b-9383-531e534cec29 cid=OLX|af3c6df3d773 broker_sym='WMT260821C00110000'
2026-08-21 13:05:51,165 INFO Live micro cancel stale sell WMT260821C00110000 id=431becac-2d69-498b-9383-531e534cec29 cid=OLX|af3c6df3d773 broker_sym='WMT260821C00110000'
Live micro orphan_adopt WMT260821C00110000 x1 entry=0.09
2026-08-21 13:05:51,165 INFO Live micro orphan_adopt WMT260821C00110000 x1 entry=0.09
Live micro hold ORPHAN COST260828C01000000 -28.6% (tp +50% / sl -40%)
2026-08-21 13:05:51,177 INFO Live micro hold ORPHAN COST260828C01000000 -28.6% (tp +50% / sl -40%)
Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
2026-08-21 13:05:51,192 INFO Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
Live micro cancel stale sell WMT260821C00110000 id=431becac-2d69-498b-9383-531e534cec29 cid=OLX|af3c6df3d773 broker_sym='WMT260821C00110000'
2026-08-21 13:05:51,201 INFO Live micro cancel stale sell WMT260821C00110000 id=431becac-2d69-498b-9383-531e534cec29 cid=OLX|af3c6df3d773 broker_sym='WMT260821C00110000'
LIVE EXIT stop_loss (-100.0%) WMT260821C00110000 x1 limit=0.01 id=4774d774-bc43-4f67-9cb3-71de41054f06
2026-08-21 13:05:51,406 INFO LIVE EXIT stop_loss (-100.0%) WMT260821C00110000 x1 limit=0.01 id=4774d774-bc43-4f67-9cb3-71de41054f06
Live micro cancel-scan COST260828C01000000: symbol-scoped n=1
2026-08-21 13:05:51,414 INFO Live micro cancel-scan COST260828C01000000: symbol-scoped n=1
Live micro cancel-scan COST260828C01000000: no non-OLS sell to cancel
2026-08-21 13:05:51,414 INFO Live micro cancel-scan COST260828C01000000: no non-OLS sell to cancel
LIVE PROT check COST260828C01000000: have_ols=True open_matched=1 ols_id=ab9b8a23-2f03-4a3a-b25a-799118f49712 ols_type=stop
2026-08-21 13:05:51,434 INFO LIVE PROT check COST260828C01000000: have_ols=True open_matched=1 ols_id=ab9b8a23-2f03-4a3a-b25a-799118f49712 ols_type=stop
Live micro: manage/exits only
2026-08-21 13:05:51,434 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-21 13:05:51,452 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
... (130 earlier lines - see full log file)
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
## Ledger health — 2026-08-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   975 | WARN | <<<
| Missing exit records (post) |   975 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     1 | INFO |
| Total closed lots           |  1770 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=821 med=-47.5% | TAINTED n=1761 med=-39.3% | KEEP-only n=294 med=+37.5% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=317.13 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | MomReversal | 15 | 47% | +0.39% | -0.60% | -1.81% | 1.99 | 1.7d | $+3.53 | WATCH |
| 3 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260821T171436Z

- UTC timestamp: `20260821T171436Z`
- GitHub run: [#7782](https://github.com/28twagg-ops/TradingBot/actions/runs/32506726030)
- Run id: `32506726030`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`9s`
- Full logs: `logs/action_runs/20260821T171436Z_live_bot.log`, `logs/action_runs/20260821T171436Z_live_options.log`, `logs/action_runs/20260821T171436Z_options_bot.log`


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
{"ts_et":"2026-08-21T13:14:40.956468-04:00","date":"2026-08-21","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":1.2,"phases_s":{"reconcile":0.06,"cancel":0.03,"manage":0.68,"protective_stops":0.02},"signals":0,"placed":0,"equity":999993.97,"open_positions":1,"pending_orders":0,"open_lots":1,"submitted_today":1,"filled_today":1,"unattributed_contracts":0,"top_signals":[],"github_run":"7782","github_run_id":"32506726030","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
17:14:37  INFO      Mode: exits
17:14:38  INFO        Daily log -> logs/daily/2026-08-21.md
17:14:38  INFO        Daily log reconciled -> logs/daily/2026-08-21.md (4 ledger rows)
17:14:38  INFO        place_all_stops: checking 3 positions...
17:14:38  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
17:14:38  INFO        [positions] 1/1 (1 valid)
17:14:38  INFO        Daily log -> logs/daily/2026-08-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:14 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $318.12|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AON  P&L +1.1%  $+0.78                                            HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  COST260828C01000000     $0.63    $0.46    -27.0%   $-17.00   $46.00   |
|  WMT260821C00110000      $0.09    $0.00    -100.0%  $-9.00    $0.00    |
|                                                                        |
|  Options open P&L                                               $-26.00|
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
=== options_live_micro LIVE 2026-08-21T13:14:39.050746-04:00 share=25% ===
2026-08-21 13:14:39,050 INFO === options_live_micro LIVE 2026-08-21T13:14:39.050746-04:00 share=25% ===
Live account equity $318.12 cash $201.38 #225458845 options_level=3
2026-08-21 13:14:39,122 INFO Live account equity $318.12 cash $201.38 #225458845 options_level=3
Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
2026-08-21 13:14:39,151 INFO Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
Live micro cancel stale sell WMT260821C00110000 id=4774d774-bc43-4f67-9cb3-71de41054f06 cid=OLX|cef348c62150 broker_sym='WMT260821C00110000'
2026-08-21 13:14:39,167 INFO Live micro cancel stale sell WMT260821C00110000 id=4774d774-bc43-4f67-9cb3-71de41054f06 cid=OLX|cef348c62150 broker_sym='WMT260821C00110000'
Live micro orphan_adopt WMT260821C00110000 x1 entry=0.09
2026-08-21 13:14:39,168 INFO Live micro orphan_adopt WMT260821C00110000 x1 entry=0.09
Live micro hold ORPHAN COST260828C01000000 -27.0% (tp +50% / sl -40%)
2026-08-21 13:14:39,185 INFO Live micro hold ORPHAN COST260828C01000000 -27.0% (tp +50% / sl -40%)
Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
2026-08-21 13:14:39,209 INFO Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
Live micro cancel stale sell WMT260821C00110000 id=4774d774-bc43-4f67-9cb3-71de41054f06 cid=OLX|cef348c62150 broker_sym='WMT260821C00110000'
2026-08-21 13:14:39,221 INFO Live micro cancel stale sell WMT260821C00110000 id=4774d774-bc43-4f67-9cb3-71de41054f06 cid=OLX|cef348c62150 broker_sym='WMT260821C00110000'
LIVE EXIT stop_loss (-100.0%) WMT260821C00110000 x1 limit=0.01 id=f16f44d2-1eda-48c7-b211-978e99629c33
2026-08-21 13:14:39,438 INFO LIVE EXIT stop_loss (-100.0%) WMT260821C00110000 x1 limit=0.01 id=f16f44d2-1eda-48c7-b211-978e99629c33
Live micro cancel-scan COST260828C01000000: symbol-scoped n=1
2026-08-21 13:14:39,452 INFO Live micro cancel-scan COST260828C01000000: symbol-scoped n=1
Live micro cancel-scan COST260828C01000000: no non-OLS sell to cancel
2026-08-21 13:14:39,452 INFO Live micro cancel-scan COST260828C01000000: no non-OLS sell to cancel
LIVE PROT check COST260828C01000000: have_ols=True open_matched=1 ols_id=ab9b8a23-2f03-4a3a-b25a-799118f49712 ols_type=stop
2026-08-21 13:14:39,487 INFO LIVE PROT check COST260828C01000000: have_ols=True open_matched=1 ols_id=ab9b8a23-2f03-4a3a-b25a-799118f49712 ols_type=stop
Live micro: manage/exits only
2026-08-21 13:14:39,487 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-21 13:14:39,500 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
... (130 earlier lines - see full log file)
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
## Ledger health — 2026-08-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   975 | WARN | <<<
| Missing exit records (post) |   975 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     1 | INFO |
| Total closed lots           |  1770 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=821 med=-47.5% | TAINTED n=1761 med=-39.3% | KEEP-only n=294 med=+37.5% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=318.12 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | MomReversal | 15 | 47% | +0.39% | -0.60% | -1.81% | 1.99 | 1.7d | $+3.53 | WATCH |
| 3 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260821T171556Z

- UTC timestamp: `20260821T171556Z`
- GitHub run: [#7783](https://github.com/28twagg-ops/TradingBot/actions/runs/32507167904)
- Run id: `32507167904`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`3s`
- Paper options: exit=`0`, duration=`11s`
- Full logs: `logs/action_runs/20260821T171556Z_live_bot.log`, `logs/action_runs/20260821T171556Z_live_options.log`, `logs/action_runs/20260821T171556Z_options_bot.log`


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
{"ts_et":"2026-08-21T13:16:03.590411-04:00","date":"2026-08-21","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":3.3,"phases_s":{"reconcile":0.35,"cancel":0.15,"manage":1.96,"protective_stops":0.15},"signals":0,"placed":0,"equity":999992.97,"open_positions":1,"pending_orders":0,"open_lots":1,"submitted_today":1,"filled_today":1,"unattributed_contracts":0,"top_signals":[],"github_run":"7783","github_run_id":"32507167904","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
17:15:57  INFO      Mode: exits
17:15:58  INFO        Daily log -> logs/daily/2026-08-21.md
17:15:58  INFO        Daily log reconciled -> logs/daily/2026-08-21.md (4 ledger rows)
17:15:58  INFO        place_all_stops: checking 3 positions...
17:15:58  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
17:15:59  INFO        [positions] 1/1 (1 valid)
17:15:59  INFO        Daily log -> logs/daily/2026-08-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:15 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $317.12|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AON  P&L +1.1%  $+0.78                                            HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  COST260828C01000000     $0.63    $0.45    -28.6%   $-18.00   $45.00   |
|  WMT260821C00110000      $0.09    $0.00    -100.0%  $-9.00    $0.00    |
|                                                                        |
|  Options open P&L                                               $-27.00|
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
=== options_live_micro LIVE 2026-08-21T13:16:00.189267-04:00 share=25% ===
2026-08-21 13:16:00,189 INFO === options_live_micro LIVE 2026-08-21T13:16:00.189267-04:00 share=25% ===
Live account equity $317.12 cash $201.38 #225458845 options_level=3
2026-08-21 13:16:00,432 INFO Live account equity $317.12 cash $201.38 #225458845 options_level=3
Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
2026-08-21 13:16:00,578 INFO Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
Live micro cancel stale sell WMT260821C00110000 id=f16f44d2-1eda-48c7-b211-978e99629c33 cid=OLX|b29fcd84de36 broker_sym='WMT260821C00110000'
2026-08-21 13:16:00,649 INFO Live micro cancel stale sell WMT260821C00110000 id=f16f44d2-1eda-48c7-b211-978e99629c33 cid=OLX|b29fcd84de36 broker_sym='WMT260821C00110000'
Live micro orphan_adopt WMT260821C00110000 x1 entry=0.09
2026-08-21 13:16:00,650 INFO Live micro orphan_adopt WMT260821C00110000 x1 entry=0.09
Live micro hold ORPHAN COST260828C01000000 -28.6% (tp +50% / sl -40%)
2026-08-21 13:16:00,760 INFO Live micro hold ORPHAN COST260828C01000000 -28.6% (tp +50% / sl -40%)
Live micro cancel-scan WMT260821C00110000: symbol-scoped empty; open_book n=1
2026-08-21 13:16:00,979 INFO Live micro cancel-scan WMT260821C00110000: symbol-scoped empty; open_book n=1
  open_order id=ab9b8a23-2f03-4a3a-b25a-799118f49712 sym='COST260828C01000000' side=OrderSide.SELL status=OrderStatus.NEW cid='OLS|1f926a83750f' type=OrderType.STOP
2026-08-21 13:16:00,979 INFO   open_order id=ab9b8a23-2f03-4a3a-b25a-799118f49712 sym='COST260828C01000000' side=OrderSide.SELL status=OrderStatus.NEW cid='OLS|1f926a83750f' type=OrderType.STOP
Live micro cancel-scan WMT260821C00110000: matched n=0
2026-08-21 13:16:00,980 INFO Live micro cancel-scan WMT260821C00110000: matched n=0
Live micro cancel-scan WMT260821C00110000: no non-OLS sell to cancel
2026-08-21 13:16:00,980 INFO Live micro cancel-scan WMT260821C00110000: no non-OLS sell to cancel
LIVE EXIT stop_loss (-100.0%) WMT260821C00110000 x1 limit=0.01 id=46bd0091-3272-4c4d-9423-444ff6f3f236
2026-08-21 13:16:01,640 INFO LIVE EXIT stop_loss (-100.0%) WMT260821C00110000 x1 limit=0.01 id=46bd0091-3272-4c4d-9423-444ff6f3f236
Live micro cancel-scan COST260828C01000000: symbol-scoped n=1
2026-08-21 13:16:01,711 INFO Live micro cancel-scan COST260828C01000000: symbol-scoped n=1
Live micro cancel-scan COST260828C01000000: no non-OLS sell to cancel
2026-08-21 13:16:01,712 INFO Live micro cancel-scan COST260828C01000000: no non-OLS sell to cancel
LIVE PROT check COST260828C01000000: have_ols=True open_matched=1 ols_id=ab9b8a23-2f03-4a3a-b25a-799118f49712 ols_type=stop
2026-08-21 13:16:01,866 INFO LIVE PROT check COST260828C01000000: have_ols=True open_matched=1 ols_id=ab9b8a23-2f03-4a3a-b25a-799118f49712 ols_type=stop
Live micro: manage/exits only
2026-08-21 13:16:01,866 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-21 13:16:01,944 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
... (130 earlier lines - see full log file)
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
## Ledger health — 2026-08-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   975 | WARN | <<<
| Missing exit records (post) |   975 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     1 | INFO |
| Total closed lots           |  1770 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=821 med=-47.5% | TAINTED n=1761 med=-39.3% | KEEP-only n=294 med=+37.5% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=317.12 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | MomReversal | 15 | 47% | +0.39% | -0.60% | -1.81% | 1.99 | 1.7d | $+3.53 | WATCH |
| 3 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260821T172051Z

- UTC timestamp: `20260821T172051Z`
- GitHub run: [#7784](https://github.com/28twagg-ops/TradingBot/actions/runs/32507609556)
- Run id: `32507609556`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`10s`
- Full logs: `logs/action_runs/20260821T172051Z_live_bot.log`, `logs/action_runs/20260821T172051Z_live_options.log`, `logs/action_runs/20260821T172051Z_options_bot.log`


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
{"ts_et":"2026-08-21T13:20:57.902026-04:00","date":"2026-08-21","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":2.6,"phases_s":{"reconcile":0.26,"cancel":0.13,"manage":1.38,"protective_stops":0.13},"signals":0,"placed":0,"equity":999993.97,"open_positions":1,"pending_orders":0,"open_lots":1,"submitted_today":1,"filled_today":1,"unattributed_contracts":0,"top_signals":[],"github_run":"7784","github_run_id":"32507609556","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
17:20:52  INFO      Mode: exits
17:20:53  INFO        Daily log -> logs/daily/2026-08-21.md
17:20:53  INFO        Daily log reconciled -> logs/daily/2026-08-21.md (4 ledger rows)
17:20:53  INFO        place_all_stops: checking 3 positions...
17:20:53  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
17:20:53  INFO        [positions] 1/1 (1 valid)
17:20:54  INFO        Daily log -> logs/daily/2026-08-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $317.19|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AON  P&L +1.2%  $+0.85                                            HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  COST260828C01000000     $0.63    $0.45    -28.6%   $-18.00   $45.00   |
|  WMT260821C00110000      $0.09    $0.00    -100.0%  $-9.00    $0.00    |
|                                                                        |
|  Options open P&L                                               $-27.00|
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
=== options_live_micro LIVE 2026-08-21T13:20:54.928297-04:00 share=25% ===
2026-08-21 13:20:54,928 INFO === options_live_micro LIVE 2026-08-21T13:20:54.928297-04:00 share=25% ===
Live account equity $317.19 cash $201.38 #225458845 options_level=3
2026-08-21 13:20:55,146 INFO Live account equity $317.19 cash $201.38 #225458845 options_level=3
Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
2026-08-21 13:20:55,266 INFO Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
Live micro cancel stale sell WMT260821C00110000 id=46bd0091-3272-4c4d-9423-444ff6f3f236 cid=OLX|f64b10054731 broker_sym='WMT260821C00110000'
2026-08-21 13:20:55,324 INFO Live micro cancel stale sell WMT260821C00110000 id=46bd0091-3272-4c4d-9423-444ff6f3f236 cid=OLX|f64b10054731 broker_sym='WMT260821C00110000'
Live micro orphan_adopt WMT260821C00110000 x1 entry=0.09
2026-08-21 13:20:55,325 INFO Live micro orphan_adopt WMT260821C00110000 x1 entry=0.09
Live micro hold ORPHAN COST260828C01000000 -28.6% (tp +50% / sl -40%)
2026-08-21 13:20:55,384 INFO Live micro hold ORPHAN COST260828C01000000 -28.6% (tp +50% / sl -40%)
Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
2026-08-21 13:20:55,506 INFO Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
Live micro cancel stale sell WMT260821C00110000 id=46bd0091-3272-4c4d-9423-444ff6f3f236 cid=OLX|f64b10054731 broker_sym='WMT260821C00110000'
2026-08-21 13:20:55,563 INFO Live micro cancel stale sell WMT260821C00110000 id=46bd0091-3272-4c4d-9423-444ff6f3f236 cid=OLX|f64b10054731 broker_sym='WMT260821C00110000'
LIVE EXIT stop_loss (-100.0%) WMT260821C00110000 x1 limit=0.01 id=b9a257b0-f729-4976-a2f7-609c4cdc0afe
2026-08-21 13:20:56,165 INFO LIVE EXIT stop_loss (-100.0%) WMT260821C00110000 x1 limit=0.01 id=b9a257b0-f729-4976-a2f7-609c4cdc0afe
Live micro cancel-scan COST260828C01000000: symbol-scoped n=1
2026-08-21 13:20:56,223 INFO Live micro cancel-scan COST260828C01000000: symbol-scoped n=1
Live micro cancel-scan COST260828C01000000: no non-OLS sell to cancel
2026-08-21 13:20:56,224 INFO Live micro cancel-scan COST260828C01000000: no non-OLS sell to cancel
LIVE PROT check COST260828C01000000: have_ols=True open_matched=1 ols_id=ab9b8a23-2f03-4a3a-b25a-799118f49712 ols_type=stop
2026-08-21 13:20:56,342 INFO LIVE PROT check COST260828C01000000: have_ols=True open_matched=1 ols_id=ab9b8a23-2f03-4a3a-b25a-799118f49712 ols_type=stop
Live micro: manage/exits only
2026-08-21 13:20:56,342 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-21 13:20:56,403 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
... (130 earlier lines - see full log file)
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
## Ledger health — 2026-08-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   975 | WARN | <<<
| Missing exit records (post) |   975 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     1 | INFO |
| Total closed lots           |  1770 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=821 med=-47.5% | TAINTED n=1761 med=-39.3% | KEEP-only n=294 med=+37.5% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=317.19 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | MomReversal | 15 | 47% | +0.39% | -0.60% | -1.81% | 1.99 | 1.7d | $+3.53 | WATCH |
| 3 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260821T172558Z

- UTC timestamp: `20260821T172558Z`
- GitHub run: [#7785](https://github.com/28twagg-ops/TradingBot/actions/runs/32508042513)
- Run id: `32508042513`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`12s`
- Full logs: `logs/action_runs/20260821T172558Z_live_bot.log`, `logs/action_runs/20260821T172558Z_live_options.log`, `logs/action_runs/20260821T172558Z_options_bot.log`


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
{"ts_et":"2026-08-21T13:26:05.273523-04:00","date":"2026-08-21","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":3.0,"phases_s":{"reconcile":0.29,"cancel":0.14,"manage":1.79,"protective_stops":0.14},"signals":0,"placed":0,"equity":999992.97,"open_positions":1,"pending_orders":0,"open_lots":1,"submitted_today":1,"filled_today":1,"unattributed_contracts":0,"top_signals":[],"github_run":"7785","github_run_id":"32508042513","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
17:25:59  INFO      Mode: exits
17:26:00  INFO        Daily log -> logs/daily/2026-08-21.md
17:26:00  INFO        Daily log reconciled -> logs/daily/2026-08-21.md (4 ledger rows)
17:26:00  INFO        place_all_stops: checking 3 positions...
17:26:00  INFO        STOP skipped AON: fractional (0.1994 shares) — software exit will handle it
17:26:00  INFO        [positions] 1/1 (1 valid)
17:26:01  INFO        Daily log -> logs/daily/2026-08-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $317.18|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AON  P&L +1.2%  $+0.84                                            HOLD|
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
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  COST260828C01000000     $0.63    $0.45    -28.6%   $-18.00   $45.00   |
|  WMT260821C00110000      $0.09    $0.00    -100.0%  $-9.00    $0.00    |
|                                                                        |
|  Options open P&L                                               $-27.00|
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
=== options_live_micro LIVE 2026-08-21T13:26:01.912595-04:00 share=25% ===
2026-08-21 13:26:01,912 INFO === options_live_micro LIVE 2026-08-21T13:26:01.912595-04:00 share=25% ===
Live account equity $317.18 cash $201.38 #225458845 options_level=3
2026-08-21 13:26:02,166 INFO Live account equity $317.18 cash $201.38 #225458845 options_level=3
Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
2026-08-21 13:26:02,304 INFO Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
Live micro cancel stale sell WMT260821C00110000 id=b9a257b0-f729-4976-a2f7-609c4cdc0afe cid=OLX|d7b17d24c72e broker_sym='WMT260821C00110000'
2026-08-21 13:26:02,372 INFO Live micro cancel stale sell WMT260821C00110000 id=b9a257b0-f729-4976-a2f7-609c4cdc0afe cid=OLX|d7b17d24c72e broker_sym='WMT260821C00110000'
Live micro orphan_adopt WMT260821C00110000 x1 entry=0.09
2026-08-21 13:26:02,372 INFO Live micro orphan_adopt WMT260821C00110000 x1 entry=0.09
Live micro hold ORPHAN COST260828C01000000 -28.6% (tp +50% / sl -40%)
2026-08-21 13:26:02,442 INFO Live micro hold ORPHAN COST260828C01000000 -28.6% (tp +50% / sl -40%)
Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
2026-08-21 13:26:02,582 INFO Live micro cancel-scan WMT260821C00110000: symbol-scoped n=1
Live micro cancel stale sell WMT260821C00110000 id=b9a257b0-f729-4976-a2f7-609c4cdc0afe cid=OLX|d7b17d24c72e broker_sym='WMT260821C00110000'
2026-08-21 13:26:02,649 INFO Live micro cancel stale sell WMT260821C00110000 id=b9a257b0-f729-4976-a2f7-609c4cdc0afe cid=OLX|d7b17d24c72e broker_sym='WMT260821C00110000'
LIVE EXIT stop_loss (-100.0%) WMT260821C00110000 x1 limit=0.01 id=7a60ef52-8372-450d-b339-e0a9c4b36168
2026-08-21 13:26:03,360 INFO LIVE EXIT stop_loss (-100.0%) WMT260821C00110000 x1 limit=0.01 id=7a60ef52-8372-450d-b339-e0a9c4b36168
Live micro cancel-scan COST260828C01000000: symbol-scoped n=1
2026-08-21 13:26:03,429 INFO Live micro cancel-scan COST260828C01000000: symbol-scoped n=1
Live micro cancel-scan COST260828C01000000: no non-OLS sell to cancel
2026-08-21 13:26:03,430 INFO Live micro cancel-scan COST260828C01000000: no non-OLS sell to cancel
LIVE PROT check COST260828C01000000: have_ols=True open_matched=1 ols_id=ab9b8a23-2f03-4a3a-b25a-799118f49712 ols_type=stop
2026-08-21 13:26:03,578 INFO LIVE PROT check COST260828C01000000: have_ols=True open_matched=1 ols_id=ab9b8a23-2f03-4a3a-b25a-799118f49712 ols_type=stop
Live micro: manage/exits only
2026-08-21 13:26:03,578 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=1
2026-08-21 13:26:03,649 INFO Live micro done. open_options=2 lots=1
```

### Paper options bot (tail)

```text
... (130 earlier lines - see full log file)
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
## Ledger health — 2026-08-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   975 | WARN | <<<
| Missing exit records (post) |   975 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     1 | INFO |
| Total closed lots           |  1770 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=821 med=-47.5% | TAINTED n=1761 med=-39.3% | KEEP-only n=294 med=+37.5% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=317.18 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | MomReversal | 15 | 47% | +0.39% | -0.60% | -1.81% | 1.99 | 1.7d | $+3.53 | WATCH |
| 3 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---
