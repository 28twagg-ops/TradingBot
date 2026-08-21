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
