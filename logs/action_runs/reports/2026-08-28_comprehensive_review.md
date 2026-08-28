# Daily Comprehensive Action Review - 2026-08-28

_Auto-generated from GitHub Actions run output. Each run appends a summary; full stdout is in linked per-run log files._
## Run 20260828T130059Z

- UTC timestamp: `20260828T130059Z`
- GitHub run: [#8392](https://github.com/28twagg-ops/TradingBot/actions/runs/33173442426)
- Run id: `33173442426`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`9s`
- Full logs: `logs/action_runs/20260828T130059Z_live_bot.log`, `logs/action_runs/20260828T130059Z_live_options.log`, `logs/action_runs/20260828T130059Z_options_bot.log`


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
{"ts_et":"2026-08-28T09:01:02.892197-04:00","date":"2026-08-28","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.12},"signals":0,"placed":0,"equity":999917.44,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"8392","github_run_id":"33173442426","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:01:00  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $265.97|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $265.97|
|  Cash                                                           $226.12|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $39.85|
|  Open P&L                                                        $-0.04|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (1 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  SYNA     MomReversal     $39.85     $97.11   $97.00   -0.1%   $-0.04  |
|                                                                        |
|  Total invested                                                  $39.85|
|  Total open P&L                                                  $-0.04|
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
|  2026-08-27  SELL  AES  Pullback50  $39.88  P&L $-0.00                 |
|  2026-08-27  SELL  AAPL  Pullback50  $39.93  P&L $+0.04                |
|  2026-08-27  SELL  AON  Pullback50  $44.26  P&L $-0.24                 |
|  2026-08-27  SELL  AES  Pullback50  $44.48  P&L $-0.02                 |
|  2026-08-27  SELL  APH  Pullback50  $45.64  P&L $-0.26                 |
|  2026-08-27  SELL  AES  Pullback50  $45.98  P&L $-0.00                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-28T09:01:01.223241-04:00 share=25% ===
2026-08-28 09:01:01,223 INFO === options_live_micro LIVE 2026-08-28T09:01:01.223241-04:00 share=25% ===
Live account equity $265.97 cash $226.12 #225458845 options_level=3
2026-08-28 09:01:01,320 INFO Live account equity $265.97 cash $226.12 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-08-28 09:01:01,347 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-08-28 09:01:01,372 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (124 earlier lines - see full log file)
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
## Ledger health — 2026-08-28
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   976 | WARN | <<<
| Missing exit records (post) |   976 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |  1770 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-28_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-28_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=821 med=-47.5% | TAINTED n=1761 med=-39.3% | KEEP-only n=294 med=+37.5% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=265.97 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | MomReversal | 17 | 41% | +0.24% | -0.61% | -1.60% | 1.81 | 1.6d | $+3.17 | WATCH |
| 3 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260828T130554Z

- UTC timestamp: `20260828T130554Z`
- GitHub run: [#8393](https://github.com/28twagg-ops/TradingBot/actions/runs/33173809604)
- Run id: `33173809604`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`10s`
- Full logs: `logs/action_runs/20260828T130554Z_live_bot.log`, `logs/action_runs/20260828T130554Z_live_options.log`, `logs/action_runs/20260828T130554Z_options_bot.log`


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
{"ts_et":"2026-08-28T09:06:00.236928-04:00","date":"2026-08-28","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.0,"phases_s":{"reconcile":0.35},"signals":0,"placed":0,"equity":999917.44,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"8393","github_run_id":"33173809604","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:05:55  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:05 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $265.97|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $265.97|
|  Cash                                                           $226.12|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $39.85|
|  Open P&L                                                        $-0.04|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (1 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  SYNA     MomReversal     $39.85     $97.11   $97.00   -0.1%   $-0.04  |
|                                                                        |
|  Total invested                                                  $39.85|
|  Total open P&L                                                  $-0.04|
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
|  2026-08-27  SELL  AES  Pullback50  $39.88  P&L $-0.00                 |
|  2026-08-27  SELL  AAPL  Pullback50  $39.93  P&L $+0.04                |
|  2026-08-27  SELL  AON  Pullback50  $44.26  P&L $-0.24                 |
|  2026-08-27  SELL  AES  Pullback50  $44.48  P&L $-0.02                 |
|  2026-08-27  SELL  APH  Pullback50  $45.64  P&L $-0.26                 |
|  2026-08-27  SELL  AES  Pullback50  $45.98  P&L $-0.00                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-28T09:05:58.294459-04:00 share=25% ===
2026-08-28 09:05:58,294 INFO === options_live_micro LIVE 2026-08-28T09:05:58.294459-04:00 share=25% ===
Live account equity $265.97 cash $226.12 #225458845 options_level=3
2026-08-28 09:05:58,522 INFO Live account equity $265.97 cash $226.12 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-08-28 09:05:58,593 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-08-28 09:05:58,662 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (124 earlier lines - see full log file)
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
## Ledger health — 2026-08-28
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   976 | WARN | <<<
| Missing exit records (post) |   976 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |  1770 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-28_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-28_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=821 med=-47.5% | TAINTED n=1761 med=-39.3% | KEEP-only n=294 med=+37.5% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=265.97 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | MomReversal | 17 | 41% | +0.24% | -0.61% | -1.60% | 1.81 | 1.6d | $+3.17 | WATCH |
| 3 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260828T131055Z

- UTC timestamp: `20260828T131055Z`
- GitHub run: [#8394](https://github.com/28twagg-ops/TradingBot/actions/runs/33174176654)
- Run id: `33174176654`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`9s`
- Full logs: `logs/action_runs/20260828T131055Z_live_bot.log`, `logs/action_runs/20260828T131055Z_live_options.log`, `logs/action_runs/20260828T131055Z_options_bot.log`


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
{"ts_et":"2026-08-28T09:10:58.565255-04:00","date":"2026-08-28","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.6,"phases_s":{"reconcile":0.04},"signals":0,"placed":0,"equity":999917.44,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"8394","github_run_id":"33174176654","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

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
|  Equity                                                         $265.97|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $265.97|
|  Cash                                                           $226.12|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $39.85|
|  Open P&L                                                        $-0.04|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (1 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  SYNA     MomReversal     $39.85     $97.11   $97.00   -0.1%   $-0.04  |
|                                                                        |
|  Total invested                                                  $39.85|
|  Total open P&L                                                  $-0.04|
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
|  2026-08-27  SELL  AES  Pullback50  $39.88  P&L $-0.00                 |
|  2026-08-27  SELL  AAPL  Pullback50  $39.93  P&L $+0.04                |
|  2026-08-27  SELL  AON  Pullback50  $44.26  P&L $-0.24                 |
|  2026-08-27  SELL  AES  Pullback50  $44.48  P&L $-0.02                 |
|  2026-08-27  SELL  APH  Pullback50  $45.64  P&L $-0.26                 |
|  2026-08-27  SELL  AES  Pullback50  $45.98  P&L $-0.00                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-28T09:10:57.067574-04:00 share=25% ===
2026-08-28 09:10:57,067 INFO === options_live_micro LIVE 2026-08-28T09:10:57.067574-04:00 share=25% ===
Live account equity $265.97 cash $226.12 #225458845 options_level=3
2026-08-28 09:10:57,109 INFO Live account equity $265.97 cash $226.12 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-08-28 09:10:57,118 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-08-28 09:10:57,125 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (124 earlier lines - see full log file)
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
## Ledger health — 2026-08-28
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   976 | WARN | <<<
| Missing exit records (post) |   976 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |  1770 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-28_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-28_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=821 med=-47.5% | TAINTED n=1761 med=-39.3% | KEEP-only n=294 med=+37.5% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=265.97 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | MomReversal | 17 | 41% | +0.24% | -0.61% | -1.60% | 1.81 | 1.6d | $+3.17 | WATCH |
| 3 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260828T131557Z

- UTC timestamp: `20260828T131557Z`
- GitHub run: [#8395](https://github.com/28twagg-ops/TradingBot/actions/runs/33174544806)
- Run id: `33174544806`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`9s`
- Full logs: `logs/action_runs/20260828T131557Z_live_bot.log`, `logs/action_runs/20260828T131557Z_live_options.log`, `logs/action_runs/20260828T131557Z_options_bot.log`


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
{"ts_et":"2026-08-28T09:16:00.933161-04:00","date":"2026-08-28","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.8,"phases_s":{"reconcile":0.23},"signals":0,"placed":0,"equity":999917.44,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"8395","github_run_id":"33174544806","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:15:57  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:15 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $265.97|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $265.97|
|  Cash                                                           $226.12|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $39.85|
|  Open P&L                                                        $-0.04|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (1 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  SYNA     MomReversal     $39.85     $97.11   $97.00   -0.1%   $-0.04  |
|                                                                        |
|  Total invested                                                  $39.85|
|  Total open P&L                                                  $-0.04|
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
|  2026-08-27  SELL  AES  Pullback50  $39.88  P&L $-0.00                 |
|  2026-08-27  SELL  AAPL  Pullback50  $39.93  P&L $+0.04                |
|  2026-08-27  SELL  AON  Pullback50  $44.26  P&L $-0.24                 |
|  2026-08-27  SELL  AES  Pullback50  $44.48  P&L $-0.02                 |
|  2026-08-27  SELL  APH  Pullback50  $45.64  P&L $-0.26                 |
|  2026-08-27  SELL  AES  Pullback50  $45.98  P&L $-0.00                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-28T09:15:59.190749-04:00 share=25% ===
2026-08-28 09:15:59,190 INFO === options_live_micro LIVE 2026-08-28T09:15:59.190749-04:00 share=25% ===
Live account equity $265.97 cash $226.12 #225458845 options_level=3
2026-08-28 09:15:59,353 INFO Live account equity $265.97 cash $226.12 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-08-28 09:15:59,398 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-08-28 09:15:59,442 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (124 earlier lines - see full log file)
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
## Ledger health — 2026-08-28
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   976 | WARN | <<<
| Missing exit records (post) |   976 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |  1770 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-28_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-28_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=821 med=-47.5% | TAINTED n=1761 med=-39.3% | KEEP-only n=294 med=+37.5% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=265.97 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | MomReversal | 17 | 41% | +0.24% | -0.61% | -1.60% | 1.81 | 1.6d | $+3.17 | WATCH |
| 3 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260828T132058Z

- UTC timestamp: `20260828T132058Z`
- GitHub run: [#8396](https://github.com/28twagg-ops/TradingBot/actions/runs/33174910985)
- Run id: `33174910985`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`9s`
- Full logs: `logs/action_runs/20260828T132058Z_live_bot.log`, `logs/action_runs/20260828T132058Z_live_options.log`, `logs/action_runs/20260828T132058Z_options_bot.log`


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
{"ts_et":"2026-08-28T09:21:01.537701-04:00","date":"2026-08-28","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.11},"signals":0,"placed":0,"equity":999917.44,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"8396","github_run_id":"33174910985","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:20:58  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $265.97|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $265.97|
|  Cash                                                           $226.12|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $39.85|
|  Open P&L                                                        $-0.04|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (1 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  SYNA     MomReversal     $39.85     $97.11   $97.00   -0.1%   $-0.04  |
|                                                                        |
|  Total invested                                                  $39.85|
|  Total open P&L                                                  $-0.04|
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
|  2026-08-27  SELL  AES  Pullback50  $39.88  P&L $-0.00                 |
|  2026-08-27  SELL  AAPL  Pullback50  $39.93  P&L $+0.04                |
|  2026-08-27  SELL  AON  Pullback50  $44.26  P&L $-0.24                 |
|  2026-08-27  SELL  AES  Pullback50  $44.48  P&L $-0.02                 |
|  2026-08-27  SELL  APH  Pullback50  $45.64  P&L $-0.26                 |
|  2026-08-27  SELL  AES  Pullback50  $45.98  P&L $-0.00                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-28T09:20:59.955550-04:00 share=25% ===
2026-08-28 09:20:59,955 INFO === options_live_micro LIVE 2026-08-28T09:20:59.955550-04:00 share=25% ===
Live account equity $265.97 cash $226.12 #225458845 options_level=3
2026-08-28 09:21:00,040 INFO Live account equity $265.97 cash $226.12 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-08-28 09:21:00,062 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-08-28 09:21:00,096 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (124 earlier lines - see full log file)
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
## Ledger health — 2026-08-28
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   976 | WARN | <<<
| Missing exit records (post) |   976 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |  1770 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-28_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-28_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=821 med=-47.5% | TAINTED n=1761 med=-39.3% | KEEP-only n=294 med=+37.5% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=265.97 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | MomReversal | 17 | 41% | +0.24% | -0.61% | -1.60% | 1.81 | 1.6d | $+3.17 | WATCH |
| 3 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260828T132552Z

- UTC timestamp: `20260828T132552Z`
- GitHub run: [#8397](https://github.com/28twagg-ops/TradingBot/actions/runs/33175284079)
- Run id: `33175284079`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`9s`
- Full logs: `logs/action_runs/20260828T132552Z_live_bot.log`, `logs/action_runs/20260828T132552Z_live_options.log`, `logs/action_runs/20260828T132552Z_options_bot.log`


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
{"ts_et":"2026-08-28T09:25:56.504094-04:00","date":"2026-08-28","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.6,"phases_s":{"reconcile":0.04},"signals":0,"placed":0,"equity":999917.44,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"8397","github_run_id":"33175284079","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

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
|  Equity                                                         $265.97|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $265.97|
|  Cash                                                           $226.12|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $39.85|
|  Open P&L                                                        $-0.04|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (1 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  SYNA     MomReversal     $39.85     $97.11   $97.00   -0.1%   $-0.04  |
|                                                                        |
|  Total invested                                                  $39.85|
|  Total open P&L                                                  $-0.04|
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
|  2026-08-27  SELL  AES  Pullback50  $39.88  P&L $-0.00                 |
|  2026-08-27  SELL  AAPL  Pullback50  $39.93  P&L $+0.04                |
|  2026-08-27  SELL  AON  Pullback50  $44.26  P&L $-0.24                 |
|  2026-08-27  SELL  AES  Pullback50  $44.48  P&L $-0.02                 |
|  2026-08-27  SELL  APH  Pullback50  $45.64  P&L $-0.26                 |
|  2026-08-27  SELL  AES  Pullback50  $45.98  P&L $-0.00                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-28T09:25:54.889897-04:00 share=25% ===
2026-08-28 09:25:54,889 INFO === options_live_micro LIVE 2026-08-28T09:25:54.889897-04:00 share=25% ===
Live account equity $265.97 cash $226.12 #225458845 options_level=3
2026-08-28 09:25:54,935 INFO Live account equity $265.97 cash $226.12 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-08-28 09:25:54,945 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-08-28 09:25:54,954 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (124 earlier lines - see full log file)
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
## Ledger health — 2026-08-28
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   976 | WARN | <<<
| Missing exit records (post) |   976 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |  1770 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-28_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-28_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=821 med=-47.5% | TAINTED n=1761 med=-39.3% | KEEP-only n=294 med=+37.5% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=265.97 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | MomReversal | 17 | 41% | +0.24% | -0.61% | -1.60% | 1.81 | 1.6d | $+3.17 | WATCH |
| 3 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260828T133056Z

- UTC timestamp: `20260828T133056Z`
- GitHub run: [#8398](https://github.com/28twagg-ops/TradingBot/actions/runs/33175661127)
- Run id: `33175661127`
- Live bot: exit=`0`, duration=`218s`
- Live options: exit=`0`, duration=`8s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260828T133056Z_live_bot.log`, `logs/action_runs/20260828T133056Z_live_options.log`, `logs/action_runs/20260828T133056Z_options_bot.log`


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
{"ts_et":"2026-08-28T09:25:56.504094-04:00","date":"2026-08-28","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.6,"phases_s":{"reconcile":0.04},"signals":0,"placed":0,"equity":999917.44,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"8397","github_run_id":"33175284079","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:30:57  INFO      Mode: morning_prep
13:30:59  INFO        [prep_positions] 3/3 (3 valid)
13:30:59  INFO      Fetching tickers (universe=both)...
13:30:59  INFO        S&P 500: 503
13:30:59  INFO        MidCap 400: 400
13:30:59  INFO        Total: 903 tickers
13:31:01  INFO        [prep_universe] 40/900 (40 valid)
13:31:02  INFO        [prep_universe] 80/900 (80 valid)
13:31:03  INFO        [prep_universe] 120/900 (120 valid)
13:31:05  INFO        [prep_universe] 160/900 (160 valid)
13:31:06  INFO        [prep_universe] 200/900 (199 valid)
13:31:14  INFO        [prep_universe] 240/900 (238 valid)
13:31:25  INFO        [prep_universe] 280/900 (278 valid)
13:31:38  INFO        [prep_universe] 320/900 (318 valid)
13:31:49  INFO        [prep_universe] 360/900 (358 valid)
13:32:03  INFO        [prep_universe] 400/900 (397 valid)
13:32:13  INFO        [prep_universe] 440/900 (437 valid)
13:32:24  INFO        [prep_universe] 480/900 (477 valid)
13:32:38  INFO        [prep_universe] 520/900 (517 valid)
13:32:48  INFO        [prep_universe] 560/900 (557 valid)
13:33:02  INFO        [prep_universe] 600/900 (597 valid)
13:33:12  INFO        [prep_universe] 640/900 (637 valid)
13:33:26  INFO        [prep_universe] 680/900 (677 valid)
13:33:36  INFO        [prep_universe] 720/900 (717 valid)
13:33:50  INFO        [prep_universe] 760/900 (757 valid)
13:34:00  INFO        [prep_universe] 800/900 (797 valid)
13:34:14  INFO        [prep_universe] 840/900 (836 valid)
13:34:24  INFO        [prep_universe] 880/900 (876 valid)
13:34:31  INFO        [prep_universe] 900/900 (896 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:30 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $266.23|
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
|  Invested                                                       $119.90|
|  Open P&L                                                        $+0.23|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $39.90     $14.73   $14.73   +0.0%   $+0.01  |
|  SYNA     MomReversal     $40.13     $97.11   $97.68   +0.6%   $+0.24  |
|  WSO      MomReversal     $39.87     $315.96  $315.82  -0.0%   $-0.02  |
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
|  Exit candidates                                                      1|
|  Signal candidates                                                   38|
|  Universe scanned                                                   900|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-28T09:34:35.056702-04:00 share=25% ===
2026-08-28 09:34:35,056 INFO === options_live_micro LIVE 2026-08-28T09:34:35.056702-04:00 share=25% ===
Live account equity $266.44 cash $146.33 #225458845 options_level=3
2026-08-28 09:34:35,302 INFO Live account equity $266.44 cash $146.33 #225458845 options_level=3
Live micro sleeve $67 (25% of $266) deployed $0 open_strategies=0/3 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy / min_cost $20)
2026-08-28 09:34:35,590 INFO Live micro sleeve $67 (25% of $266) deployed $0 open_strategies=0/3 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy / min_cost $20)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win
2026-08-28 09:34:35,590 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win
Live micro signals: 5
2026-08-28 09:34:39,947 INFO Live micro signals: 5
  try S404 100%win/+80%med COIN
2026-08-28 09:34:39,948 INFO   try S404 100%win/+80%med COIN
  skip S404 COIN: no contract under $67
2026-08-28 09:34:41,175 INFO   skip S404 COIN: no contract under $67
  try S404 100%win/+80%med MARA
2026-08-28 09:34:41,175 INFO   try S404 100%win/+80%med MARA
LIVE BUY S404 100%win MARA MARA260904C00011500 limit=0.57 ask=0.58 cost=$58 id=f9a90613-3b1f-47f3-af32-703fb3d6e7a9
2026-08-28 09:34:41,524 INFO LIVE BUY S404 100%win MARA MARA260904C00011500 limit=0.57 ask=0.58 cost=$58 id=f9a90613-3b1f-47f3-af32-703fb3d6e7a9
  skip S404 MSTR: already attempted today
2026-08-28 09:34:41,525 INFO   skip S404 MSTR: already attempted today
  try S406 56%win/+58%med MRK
2026-08-28 09:34:41,525 INFO   try S406 56%win/+58%med MRK
  skip S406 MRK: no contract under $17
2026-08-28 09:34:41,804 INFO   skip S406 MRK: no contract under $17
  try S218 56%win/+49%med MCD
2026-08-28 09:34:41,804 INFO   try S218 56%win/+49%med MCD
  skip S218 MCD: no contract under $17
2026-08-28 09:34:42,055 INFO   skip S218 MCD: no contract under $17
LIVE PROT check MARA260904C00011500: have_ols=False open_matched=0 ols_id=- ols_type=-
2026-08-28 09:34:42,199 INFO LIVE PROT check MARA260904C00011500: have_ols=False open_matched=0 ols_id=- ols_type=-
LIVE PROT STOP-MKT MARA260904C00011500 x1 stop=0.34 id=397ceec6-0682-42c7-957b-4bacc1f1dab5
2026-08-28 09:34:42,281 INFO LIVE PROT STOP-MKT MARA260904C00011500 x1 stop=0.34 id=397ceec6-0682-42c7-957b-4bacc1f1dab5
Live micro done. open_options=1 lots=1
2026-08-28 09:34:42,352 INFO Live micro done. open_options=1 lots=1
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=0 paper_keys=yes dry_run=False
  alpaca positions=0
options_reconcile: done
Layout: grid:100:live_1to1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> grid:100:live_1to1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-08-28T09:34:44.053769-04:00 ===

[Run context]
Paper auth OK — equity $999917.44, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Allowed (new entries only): S218, S404, S406

[Scan + entries]
Scanning 117 symbols for [S218, S404, S406] …
Fetched daily bars for 113/117 symbols
```

---

## Run 20260828T133626Z

- UTC timestamp: `20260828T133626Z`
- GitHub run: [#8399](https://github.com/28twagg-ops/TradingBot/actions/runs/33176052219)
- Run id: `33176052219`
- Live bot: exit=`0`, duration=`218s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260828T133626Z_live_bot.log`, `logs/action_runs/20260828T133626Z_live_options.log`, `logs/action_runs/20260828T133626Z_options_bot.log`


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
{"ts_et":"2026-08-28T09:25:56.504094-04:00","date":"2026-08-28","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.6,"phases_s":{"reconcile":0.04},"signals":0,"placed":0,"equity":999917.44,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"8397","github_run_id":"33175284079","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:36:28  INFO      Mode: morning_prep
13:36:29  INFO        [prep_positions] 3/3 (3 valid)
13:36:29  INFO      Fetching tickers (universe=both)...
13:36:29  INFO        S&P 500: 503
13:36:30  INFO        MidCap 400: 400
13:36:30  INFO        Total: 903 tickers
13:36:31  INFO        [prep_universe] 40/900 (40 valid)
13:36:32  INFO        [prep_universe] 80/900 (80 valid)
13:36:34  INFO        [prep_universe] 120/900 (120 valid)
13:36:35  INFO        [prep_universe] 160/900 (160 valid)
13:36:36  INFO        [prep_universe] 200/900 (199 valid)
13:36:44  INFO        [prep_universe] 240/900 (238 valid)
13:36:54  INFO        [prep_universe] 280/900 (278 valid)
13:37:07  INFO        [prep_universe] 320/900 (318 valid)
13:37:21  INFO        [prep_universe] 360/900 (358 valid)
13:37:31  INFO        [prep_universe] 400/900 (397 valid)
13:37:45  INFO        [prep_universe] 440/900 (437 valid)
13:37:55  INFO        [prep_universe] 480/900 (477 valid)
13:38:09  INFO        [prep_universe] 520/900 (517 valid)
13:38:19  INFO        [prep_universe] 560/900 (557 valid)
13:38:32  INFO        [prep_universe] 600/900 (597 valid)
13:38:43  INFO        [prep_universe] 640/900 (637 valid)
13:38:56  INFO        [prep_universe] 680/900 (677 valid)
13:39:07  INFO        [prep_universe] 720/900 (717 valid)
13:39:20  INFO        [prep_universe] 760/900 (757 valid)
13:39:30  INFO        [prep_universe] 800/900 (797 valid)
13:39:44  INFO        [prep_universe] 840/900 (836 valid)
13:39:54  INFO        [prep_universe] 880/900 (876 valid)
13:40:01  INFO        [prep_universe] 900/900 (896 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $257.79|
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
|  Invested                                                       $119.51|
|  Open P&L                                                        $-0.16|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $39.92     $14.73   $14.74   +0.1%   $+0.03  |
|  SYNA     MomReversal     $39.64     $97.11   $96.50   -0.6%   $-0.25  |
|  WSO      MomReversal     $39.95     $315.96  $316.45  +0.2%   $+0.06  |
+========================================================================+

+========================================================================+
|                            OPEN SELL ORDERS                            |
+========================================================================+
|  Count                                                                1|
|  TICKER    TYPE              QTY       LIMIT       STOP                |
+------------------------------------------------------------------------+
|  MARA260~  OrderType.STOP    1         None        0.34                |
+========================================================================+

+========================================================================+
|                              PREP SUMMARY                              |
+========================================================================+
|  Saved                                                              yes|
|  Exit candidates                                                      2|
|  Signal candidates                                                   28|
|  Universe scanned                                                   900|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-28T09:40:04.906600-04:00 share=25% ===
2026-08-28 09:40:04,906 INFO === options_live_micro LIVE 2026-08-28T09:40:04.906600-04:00 share=25% ===
Live account equity $259.67 cash $90.28 #225458845 options_level=3
2026-08-28 09:40:05,182 INFO Live account equity $259.67 cash $90.28 #225458845 options_level=3
Live micro cancel-scan MARA260904C00011500: symbol-scoped n=1
2026-08-28 09:40:05,326 INFO Live micro cancel-scan MARA260904C00011500: symbol-scoped n=1
Live micro cancel-scan MARA260904C00011500: no non-OLS sell to cancel
2026-08-28 09:40:05,326 INFO Live micro cancel-scan MARA260904C00011500: no non-OLS sell to cancel
Live micro orphan_adopt MARA260904C00011500 x1 entry=0.56
2026-08-28 09:40:05,327 INFO Live micro orphan_adopt MARA260904C00011500 x1 entry=0.56
Live micro hold ORPHAN MARA260904C00011500 -10.7% (tp +50% / sl -40%)
2026-08-28 09:40:05,401 INFO Live micro hold ORPHAN MARA260904C00011500 -10.7% (tp +50% / sl -40%)
Live micro cancel-scan MARA260904C00011500: symbol-scoped n=1
2026-08-28 09:40:05,470 INFO Live micro cancel-scan MARA260904C00011500: symbol-scoped n=1
Live micro cancel-scan MARA260904C00011500: no non-OLS sell to cancel
2026-08-28 09:40:05,471 INFO Live micro cancel-scan MARA260904C00011500: no non-OLS sell to cancel
LIVE PROT check MARA260904C00011500: have_ols=True open_matched=1 ols_id=397ceec6-0682-42c7-957b-4bacc1f1dab5 ols_type=stop
2026-08-28 09:40:05,625 INFO LIVE PROT check MARA260904C00011500: have_ols=True open_matched=1 ols_id=397ceec6-0682-42c7-957b-4bacc1f1dab5 ols_type=stop
Live micro sleeve $65 (25% of $260) deployed $50 open_strategies=0/3 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy / min_cost $20)
2026-08-28 09:40:05,695 INFO Live micro sleeve $65 (25% of $260) deployed $50 open_strategies=0/3 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy / min_cost $20)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win
2026-08-28 09:40:05,695 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win
Live micro signals: 7
2026-08-28 09:40:10,432 INFO Live micro signals: 7
  try S404 100%win/+80%med COIN
2026-08-28 09:40:10,432 INFO   try S404 100%win/+80%med COIN
  skip S404 COIN: no contract under $18
2026-08-28 09:40:10,982 INFO   skip S404 COIN: no contract under $18
  try S404 100%win/+80%med MARA
2026-08-28 09:40:10,982 INFO   try S404 100%win/+80%med MARA
  skip S404 MARA: cost $52 > $17
2026-08-28 09:40:11,512 INFO   skip S404 MARA: cost $52 > $17
  try S404 100%win/+80%med MSTR
2026-08-28 09:40:11,512 INFO   try S404 100%win/+80%med MSTR
  skip S404 MSTR: no contract under $17
2026-08-28 09:40:11,834 INFO   skip S404 MSTR: no contract under $17
  try S406 56%win/+58%med ARM
2026-08-28 09:40:11,834 INFO   try S406 56%win/+58%med ARM
  skip S406 ARM: no contract under $17
2026-08-28 09:40:12,110 INFO   skip S406 ARM: no contract under $17
  try S406 56%win/+58%med MRK
2026-08-28 09:40:12,110 INFO   try S406 56%win/+58%med MRK
  skip S406 MRK: no contract under $17
2026-08-28 09:40:12,384 INFO   skip S406 MRK: no contract under $17
  try S406 56%win/+58%med MSTR
2026-08-28 09:40:12,384 INFO   try S406 56%win/+58%med MSTR
  skip S406 MSTR: no contract under $17
2026-08-28 09:40:12,614 INFO   skip S406 MSTR: no contract under $17
  try S218 56%win/+49%med MCD
2026-08-28 09:40:12,615 INFO   try S218 56%win/+49%med MCD
  skip S218 MCD: cost $7 < min $20 (lottery ticket filter)
2026-08-28 09:40:12,859 INFO   skip S218 MCD: cost $7 < min $20 (lottery ticket filter)
LIVE PROT check MARA260904C00011500: have_ols=True open_matched=1 ols_id=397ceec6-0682-42c7-957b-4bacc1f1dab5 ols_type=stop
2026-08-28 09:40:12,998 INFO LIVE PROT check MARA260904C00011500: have_ols=True open_matched=1 ols_id=397ceec6-0682-42c7-957b-4bacc1f1dab5 ols_type=stop
Live micro done. open_options=1 lots=1
2026-08-28 09:40:13,072 INFO Live micro done. open_options=1 lots=1
```

### Paper options bot (tail)

```text

```

---

## Run 20260828T134117Z

- UTC timestamp: `20260828T134117Z`
- GitHub run: [#8400](https://github.com/28twagg-ops/TradingBot/actions/runs/33176436109)
- Run id: `33176436109`
- Live bot: exit=`0`, duration=`217s`
- Live options: exit=`0`, duration=`3s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260828T134117Z_live_bot.log`, `logs/action_runs/20260828T134117Z_live_options.log`, `logs/action_runs/20260828T134117Z_options_bot.log`


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
{"ts_et":"2026-08-28T09:25:56.504094-04:00","date":"2026-08-28","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.6,"phases_s":{"reconcile":0.04},"signals":0,"placed":0,"equity":999917.44,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"8397","github_run_id":"33175284079","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:41:18  INFO      Mode: morning_prep
13:41:19  INFO        [prep_positions] 3/3 (3 valid)
13:41:19  INFO        Universe cache hit: 903 tickers (tickers_2026-08-28.json)
13:41:20  INFO        [prep_universe] 40/900 (40 valid)
13:41:21  INFO        [prep_universe] 80/900 (80 valid)
13:41:22  INFO        [prep_universe] 120/900 (120 valid)
13:41:24  INFO        [prep_universe] 160/900 (160 valid)
13:41:25  INFO        [prep_universe] 200/900 (199 valid)
13:41:32  INFO        [prep_universe] 240/900 (238 valid)
13:41:45  INFO        [prep_universe] 280/900 (278 valid)
13:41:58  INFO        [prep_universe] 320/900 (318 valid)
13:42:08  INFO        [prep_universe] 360/900 (358 valid)
13:42:21  INFO        [prep_universe] 400/900 (397 valid)
13:42:34  INFO        [prep_universe] 440/900 (437 valid)
13:42:44  INFO        [prep_universe] 480/900 (477 valid)
13:42:57  INFO        [prep_universe] 520/900 (517 valid)
13:43:10  INFO        [prep_universe] 560/900 (557 valid)
13:43:20  INFO        [prep_universe] 600/900 (597 valid)
13:43:33  INFO        [prep_universe] 640/900 (637 valid)
13:43:46  INFO        [prep_universe] 680/900 (677 valid)
13:43:56  INFO        [prep_universe] 720/900 (717 valid)
13:44:09  INFO        [prep_universe] 760/900 (757 valid)
13:44:22  INFO        [prep_universe] 800/900 (797 valid)
13:44:32  INFO        [prep_universe] 840/900 (836 valid)
13:44:45  INFO        [prep_universe] 880/900 (876 valid)
13:44:52  INFO        [prep_universe] 900/900 (896 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $257.72|
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
|  Invested                                                       $119.44|
|  Open P&L                                                        $-0.23|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $39.90     $14.73   $14.73   +0.0%   $+0.01  |
|  SYNA     MomReversal     $39.84     $97.11   $96.99   -0.1%   $-0.05  |
|  WSO      MomReversal     $39.70     $315.96  $314.43  -0.5%   $-0.19  |
+========================================================================+

+========================================================================+
|                            OPEN SELL ORDERS                            |
+========================================================================+
|  Count                                                                1|
|  TICKER    TYPE              QTY       LIMIT       STOP                |
+------------------------------------------------------------------------+
|  MARA260~  OrderType.STOP    1         None        0.34                |
+========================================================================+

+========================================================================+
|                              PREP SUMMARY                              |
+========================================================================+
|  Saved                                                              yes|
|  Exit candidates                                                      1|
|  Signal candidates                                                   22|
|  Universe scanned                                                   900|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-28T09:44:55.622642-04:00 share=25% ===
2026-08-28 09:44:55,622 INFO === options_live_micro LIVE 2026-08-28T09:44:55.622642-04:00 share=25% ===
Live account equity $256.89 cash $90.28 #225458845 options_level=3
2026-08-28 09:44:55,666 INFO Live account equity $256.89 cash $90.28 #225458845 options_level=3
Live micro fill confirmed S404 MARA260904C00011500
2026-08-28 09:44:55,694 INFO Live micro fill confirmed S404 MARA260904C00011500
Live micro hold S404 MARA260904C00011500 -16.1% (tp +50% / sl -40%)
2026-08-28 09:44:55,703 INFO Live micro hold S404 MARA260904C00011500 -16.1% (tp +50% / sl -40%)
Live micro cancel-scan MARA260904C00011500: symbol-scoped n=1
2026-08-28 09:44:55,713 INFO Live micro cancel-scan MARA260904C00011500: symbol-scoped n=1
Live micro cancel-scan MARA260904C00011500: no non-OLS sell to cancel
2026-08-28 09:44:55,713 INFO Live micro cancel-scan MARA260904C00011500: no non-OLS sell to cancel
LIVE PROT check MARA260904C00011500: have_ols=True open_matched=1 ols_id=397ceec6-0682-42c7-957b-4bacc1f1dab5 ols_type=stop
2026-08-28 09:44:55,733 INFO LIVE PROT check MARA260904C00011500: have_ols=True open_matched=1 ols_id=397ceec6-0682-42c7-957b-4bacc1f1dab5 ols_type=stop
Live micro sleeve $64 (25% of $257) deployed $47 open_strategies=1/3 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy / min_cost $20)
2026-08-28 09:44:55,743 INFO Live micro sleeve $64 (25% of $257) deployed $47 open_strategies=1/3 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy / min_cost $20)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win
2026-08-28 09:44:55,743 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win
Live micro signals: 5
2026-08-28 09:44:56,827 INFO Live micro signals: 5
  skip S404 COIN: already attempted today
2026-08-28 09:44:56,828 INFO   skip S404 COIN: already attempted today
  skip S404 MARA: already attempted today
2026-08-28 09:44:56,828 INFO   skip S404 MARA: already attempted today
  skip S404 MSTR: already attempted today
2026-08-28 09:44:56,828 INFO   skip S404 MSTR: already attempted today
  try S406 56%win/+58%med MRK
2026-08-28 09:44:56,828 INFO   try S406 56%win/+58%med MRK
  skip S406 MRK: no contract under $17
2026-08-28 09:44:56,993 INFO   skip S406 MRK: no contract under $17
  try S218 56%win/+49%med MCD
2026-08-28 09:44:56,993 INFO   try S218 56%win/+49%med MCD
  skip S218 MCD: no contract under $17
2026-08-28 09:44:57,104 INFO   skip S218 MCD: no contract under $17
LIVE PROT check MARA260904C00011500: have_ols=True open_matched=1 ols_id=397ceec6-0682-42c7-957b-4bacc1f1dab5 ols_type=stop
2026-08-28 09:44:57,124 INFO LIVE PROT check MARA260904C00011500: have_ols=True open_matched=1 ols_id=397ceec6-0682-42c7-957b-4bacc1f1dab5 ols_type=stop
Live micro done. open_options=1 lots=1
2026-08-28 09:44:57,144 INFO Live micro done. open_options=1 lots=1
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=0 paper_keys=yes dry_run=False
  alpaca positions=0
options_reconcile: done
Layout: grid:100:live_1to1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> grid:100:live_1to1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      100
=== options_morning_bot (PAPER) 2026-08-28T09:44:58.651836-04:00 ===

[Run context]
Paper auth OK — equity $999917.44, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Allowed (new entries only): S218, S404, S406

[Scan + entries]
Scanning 117 symbols for [S218, S404, S406] …
Fetched daily bars for 113/117 symbols
```

---

## Run 20260828T135132Z

- UTC timestamp: `20260828T135132Z`
- GitHub run: [#8402](https://github.com/28twagg-ops/TradingBot/actions/runs/33177216592)
- Run id: `33177216592`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260828T135132Z_live_bot.log`, `logs/action_runs/20260828T135132Z_live_options.log`, `logs/action_runs/20260828T135132Z_options_bot.log`


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
{"ts_et":"2026-08-28T09:25:56.504094-04:00","date":"2026-08-28","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.6,"phases_s":{"reconcile":0.04},"signals":0,"placed":0,"equity":999917.44,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"8397","github_run_id":"33175284079","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
... (67 earlier lines - see full log file)
|  SYNA     MomReversal     $39.79     $97.11   $96.86   -0.3%   $-0.10  |
|  WSO      MomReversal     $39.84     $315.96  $315.55  -0.1%   $-0.05  |
|                                                                        |
|  Total invested                                                  $79.63|
|  Total open P&L                                                  $-0.15|
|  Buys today: 0  |  entry cap: 1  |  max open: 3                        |
+========================================================================+

+========================================================================+
|                               PLAN CACHE                               |
+========================================================================+
|  Mode                                                           morning|
|  File                                      logs/plans/morning_plan.json|
|  Use cached plan                                   no (stale (2896.1m))|
+========================================================================+

+========================================================================+
|          EXIT EVALUATION  (EOD -- midline + stop + max-hold)           |
+========================================================================+
|  SYNA  P&L -0.3%  $-0.10                                           HOLD|
|  WSO  P&L -0.1%  $-0.05                                            HOLD|
+========================================================================+

+========================================================================+
|                           EXIT EVAL SUMMARY                            |
+========================================================================+
|  Exit eval    attempted 0 | filled 0 | partial 0 | pending 0 | failed 0|
|  Other skips     already logged today 0  |  no price data 0  |  holds 2|
|  Stop-loss breaches                                                none|
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+

+========================================================================+
|                             DATA DOWNLOAD                              |
+========================================================================+
|  Universe: both  |  Alpaca primary / yfinance fallback                 |
+========================================================================+

+========================================================================+
|                              SIGNAL SCAN                               |
+========================================================================+
|  Month: Aug  |  Regime: BULL                                           |
|  Primary: VolumeSpike  |  Secondary: 52wkLow (display only — schedule ~|
|  Source                                                       live scan|
+========================================================================+

+========================================================================+
|                         SIGNALS FOUND  --  17                          |
+========================================================================+
|  TICKER   STRATEGY        TIER   PRICE    RSI    VOL_Z   TRIGGER       |
+------------------------------------------------------------------------+
|  AES      Pullback50      eq     $14.73   50.8   -2.06   50MA bounce (+|
|  AON      Pullback50      eq     $353.56  46.8   -1.81   50MA bounce (+|
|  ADM      Pullback50      eq     $80.77   51.0   -2.71   50MA bounce (+|
|  EIX      Pullback50      eq     $74.78   70.4   -2.09   50MA bounce (+|
|  EW       Pullback50      eq     $90.03   40.5   -3.07   50MA bounce (+|
|  HIG      Pullback50      eq     $138.59  43.2   -2.22   50MA bounce (+|
|  KVUE     Pullback50      eq     $19.31   56.7   -2.18   50MA bounce (+|
|  PHM      Pullback50      eq     $128.92  48.0   -3.28   50MA bounce (-|
|  PGR      Pullback50      eq     $218.54  55.1   -2.05   50MA bounce (+|
|  RF       Pullback50      eq     $30.57   35.4   -2.98   50MA bounce (-|
|  WFC      Pullback50      eq     $85.76   41.8   -2.96   50MA bounce (-|
|  ASB      Pullback50      eq     $31.01   44.4   -3.29   50MA bounce (+|
|  CBSH     Pullback50      eq     $58.22   45.7   -3.24   50MA bounce (-|
|  ELS      Pullback50      eq     $64.14   46.9   -2.63   50MA bounce (-|
|  LIVN     Pullback50      eq     $80.40   63.2   -1.80   50MA bounce (-|
|  OC       Pullback50      eq     $144.27  30.1   -2.43   50MA bounce (-|
|  PNFP     Pullback50      eq     $101.89  40.6   -3.13   50MA bounce (-|
|                                                                        |
+========================================================================+

+========================================================================+
|                              ENTRY ORDERS                              |
+========================================================================+
|    ENTER [eq] AES  Pullback50                                    $38.52|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    SKIP [eq] AON  Pullback50                                      cap 3|
|    SKIP [eq] ADM  Pullback50                                      cap 3|
|    SKIP [eq] EIX  Pullback50                                      cap 3|
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20260828T135628Z

- UTC timestamp: `20260828T135628Z`
- GitHub run: [#8403](https://github.com/28twagg-ops/TradingBot/actions/runs/33177609968)
- Run id: `33177609968`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260828T135628Z_live_bot.log`, `logs/action_runs/20260828T135628Z_live_options.log`, `logs/action_runs/20260828T135628Z_options_bot.log`


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
{"ts_et":"2026-08-28T09:25:56.504094-04:00","date":"2026-08-28","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.6,"phases_s":{"reconcile":0.04},"signals":0,"placed":0,"equity":999917.44,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"8397","github_run_id":"33175284079","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:56:29  INFO      Mode: morning_scan
13:56:29  INFO        [positions] 3/3 (3 valid)
13:56:29  INFO        SELL order cancelled AES  type=OrderType.STOP  id=26358f25-01ad-47e1-ace0-e32a306a47dc
13:56:29  INFO        SELL LIMIT AES  qty=2.613012676  limit=$14.73  id=3f5f2cf2-9100-4229-983c-ff752c5b6be1
13:56:59  INFO        SELL LIMIT filled AES (confirmed by position check)
13:57:00  INFO        TX logged: SELL AES  P&L -0.01%
13:57:00  INFO        Universe cache hit: 903 tickers (tickers_2026-08-28.json)
13:57:01  INFO        [universe] 40/901 (40 valid)
13:57:02  INFO        [universe] 80/901 (80 valid)
13:57:03  INFO        [universe] 120/901 (120 valid)
13:57:04  INFO        [universe] 160/901 (160 valid)
13:57:06  INFO        [universe] 200/901 (199 valid)
13:57:13  INFO        [universe] 240/901 (238 valid)
13:57:26  INFO        [universe] 280/901 (278 valid)
13:57:39  INFO        [universe] 320/901 (318 valid)
13:57:49  INFO        [universe] 360/901 (358 valid)
13:58:02  INFO        [universe] 400/901 (397 valid)
13:58:14  INFO        [universe] 440/901 (437 valid)
13:58:24  INFO        [universe] 480/901 (477 valid)
13:58:37  INFO        [universe] 520/901 (517 valid)
13:58:50  INFO        [universe] 560/901 (557 valid)
13:59:00  INFO        [universe] 600/901 (597 valid)
13:59:13  INFO        [universe] 640/901 (637 valid)
13:59:26  INFO        [universe] 680/901 (677 valid)
13:59:36  INFO        [universe] 720/901 (717 valid)
13:59:49  INFO        [universe] 760/901 (757 valid)
14:00:02  INFO        [universe] 800/901 (797 valid)
14:00:12  INFO        [universe] 840/901 (836 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---
