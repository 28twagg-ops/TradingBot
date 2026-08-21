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
