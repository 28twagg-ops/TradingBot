# Daily Comprehensive Action Review - 2026-08-27

_Auto-generated from GitHub Actions run output. Each run appends a summary; full stdout is in linked per-run log files._
## Run 20260827T130101Z

- UTC timestamp: `20260827T130101Z`
- GitHub run: [#8260](https://github.com/28twagg-ops/TradingBot/actions/runs/33074582781)
- Run id: `33074582781`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`9s`
- Full logs: `logs/action_runs/20260827T130101Z_live_bot.log`, `logs/action_runs/20260827T130101Z_live_options.log`, `logs/action_runs/20260827T130101Z_options_bot.log`


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
{"ts_et":"2026-08-27T09:01:05.540963-04:00","date":"2026-08-27","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.0,"phases_s":{"reconcile":0.29},"signals":0,"placed":0,"equity":999930.56,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"8260","github_run_id":"33074582781","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:01:01  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $306.55|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $306.55|
|  Cash                                                           $213.92|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $92.63|
|  Open P&L                                                        $+0.75|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $46.06     $14.73   $14.75   +0.2%   $+0.08  |
|  APH      Pullback50      $46.58     $161.66  $164.05  +1.5%   $+0.68  |
|                                                                        |
|  Total invested                                                  $92.63|
|  Total open P&L                                                  $+0.75|
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
|  2026-08-26  SELL  DECK  MomReversal  $45.77  P&L $-0.28               |
|  2026-08-26  SELL  AME  Pullback50  $45.74  P&L $-0.24                 |
|  2026-08-26  SELL  NKE  MomReversal  $6.50  P&L $-0.08                 |
|  2026-08-25  SELL  AAPL  Pullback50  $45.89  P&L $-0.25                |
|  2026-08-25  SELL  GOOGL  Pullback50  $45.94  P&L $-0.25               |
|  2026-08-25  SELL  CAH  Pullback50  $46.12  P&L $+0.01                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-27T09:01:03.564602-04:00 share=25% ===
2026-08-27 09:01:03,564 INFO === options_live_micro LIVE 2026-08-27T09:01:03.564602-04:00 share=25% ===
Live account equity $306.55 cash $213.92 #225458845 options_level=3
2026-08-27 09:01:03,772 INFO Live account equity $306.55 cash $213.92 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-08-27 09:01:03,830 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-08-27 09:01:03,888 INFO Live micro done. open_options=0 lots=0
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
## Ledger health — 2026-08-27
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
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-27_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-27_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=821 med=-47.5% | TAINTED n=1761 med=-39.3% | KEEP-only n=294 med=+37.5% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=306.55 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | MomReversal | 17 | 41% | +0.24% | -0.61% | -1.60% | 1.81 | 1.6d | $+3.17 | WATCH |
| 3 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260827T130557Z

- UTC timestamp: `20260827T130557Z`
- GitHub run: [#8261](https://github.com/28twagg-ops/TradingBot/actions/runs/33075001268)
- Run id: `33075001268`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`10s`
- Full logs: `logs/action_runs/20260827T130557Z_live_bot.log`, `logs/action_runs/20260827T130557Z_live_options.log`, `logs/action_runs/20260827T130557Z_options_bot.log`


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
{"ts_et":"2026-08-27T09:06:03.165716-04:00","date":"2026-08-27","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.8,"phases_s":{"reconcile":0.16},"signals":0,"placed":0,"equity":999930.56,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"8261","github_run_id":"33075001268","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:05:59  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $306.55|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $306.55|
|  Cash                                                           $213.92|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $92.63|
|  Open P&L                                                        $+0.75|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $46.06     $14.73   $14.75   +0.2%   $+0.08  |
|  APH      Pullback50      $46.58     $161.66  $164.05  +1.5%   $+0.68  |
|                                                                        |
|  Total invested                                                  $92.63|
|  Total open P&L                                                  $+0.75|
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
|  2026-08-26  SELL  DECK  MomReversal  $45.77  P&L $-0.28               |
|  2026-08-26  SELL  AME  Pullback50  $45.74  P&L $-0.24                 |
|  2026-08-26  SELL  NKE  MomReversal  $6.50  P&L $-0.08                 |
|  2026-08-25  SELL  AAPL  Pullback50  $45.89  P&L $-0.25                |
|  2026-08-25  SELL  GOOGL  Pullback50  $45.94  P&L $-0.25               |
|  2026-08-25  SELL  CAH  Pullback50  $46.12  P&L $+0.01                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-27T09:06:01.259497-04:00 share=25% ===
2026-08-27 09:06:01,259 INFO === options_live_micro LIVE 2026-08-27T09:06:01.259497-04:00 share=25% ===
Live account equity $306.55 cash $213.92 #225458845 options_level=3
2026-08-27 09:06:01,403 INFO Live account equity $306.55 cash $213.92 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-08-27 09:06:01,444 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-08-27 09:06:01,485 INFO Live micro done. open_options=0 lots=0
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
## Ledger health — 2026-08-27
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
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-27_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-27_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=821 med=-47.5% | TAINTED n=1761 med=-39.3% | KEEP-only n=294 med=+37.5% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=306.55 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | MomReversal | 17 | 41% | +0.24% | -0.61% | -1.60% | 1.81 | 1.6d | $+3.17 | WATCH |
| 3 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260827T131059Z

- UTC timestamp: `20260827T131059Z`
- GitHub run: [#8262](https://github.com/28twagg-ops/TradingBot/actions/runs/33075418572)
- Run id: `33075418572`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`9s`
- Full logs: `logs/action_runs/20260827T131059Z_live_bot.log`, `logs/action_runs/20260827T131059Z_live_options.log`, `logs/action_runs/20260827T131059Z_options_bot.log`


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
{"ts_et":"2026-08-27T09:11:04.450843-04:00","date":"2026-08-27","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.0,"phases_s":{"reconcile":0.31},"signals":0,"placed":0,"equity":999930.56,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"8262","github_run_id":"33075418572","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:11:01  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $306.68|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $306.68|
|  Cash                                                           $213.92|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $92.76|
|  Open P&L                                                        $+0.88|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $46.06     $14.73   $14.75   +0.2%   $+0.08  |
|  APH      Pullback50      $46.71     $161.66  $164.50  +1.8%   $+0.81  |
|                                                                        |
|  Total invested                                                  $92.76|
|  Total open P&L                                                  $+0.88|
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
|  2026-08-26  SELL  DECK  MomReversal  $45.77  P&L $-0.28               |
|  2026-08-26  SELL  AME  Pullback50  $45.74  P&L $-0.24                 |
|  2026-08-26  SELL  NKE  MomReversal  $6.50  P&L $-0.08                 |
|  2026-08-25  SELL  AAPL  Pullback50  $45.89  P&L $-0.25                |
|  2026-08-25  SELL  GOOGL  Pullback50  $45.94  P&L $-0.25               |
|  2026-08-25  SELL  CAH  Pullback50  $46.12  P&L $+0.01                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-27T09:11:02.575987-04:00 share=25% ===
2026-08-27 09:11:02,576 INFO === options_live_micro LIVE 2026-08-27T09:11:02.575987-04:00 share=25% ===
Live account equity $306.68 cash $213.92 #225458845 options_level=3
2026-08-27 09:11:02,784 INFO Live account equity $306.68 cash $213.92 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-08-27 09:11:02,842 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-08-27 09:11:02,899 INFO Live micro done. open_options=0 lots=0
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
## Ledger health — 2026-08-27
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
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-27_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-27_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=821 med=-47.5% | TAINTED n=1761 med=-39.3% | KEEP-only n=294 med=+37.5% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=306.68 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | MomReversal | 17 | 41% | +0.24% | -0.61% | -1.60% | 1.81 | 1.6d | $+3.17 | WATCH |
| 3 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260827T131759Z

- UTC timestamp: `20260827T131759Z`
- GitHub run: [#8263](https://github.com/28twagg-ops/TradingBot/actions/runs/33075847063)
- Run id: `33075847063`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`9s`
- Full logs: `logs/action_runs/20260827T131759Z_live_bot.log`, `logs/action_runs/20260827T131759Z_live_options.log`, `logs/action_runs/20260827T131759Z_options_bot.log`


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
{"ts_et":"2026-08-27T09:18:03.029282-04:00","date":"2026-08-27","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.11},"signals":0,"placed":0,"equity":999930.56,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"8263","github_run_id":"33075847063","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:17:59  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:18 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $306.81|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $306.81|
|  Cash                                                           $213.92|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $92.89|
|  Open P&L                                                        $+1.01|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $46.06     $14.73   $14.75   +0.2%   $+0.08  |
|  APH      Pullback50      $46.83     $161.66  $164.95  +2.0%   $+0.93  |
|                                                                        |
|  Total invested                                                  $92.89|
|  Total open P&L                                                  $+1.01|
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
|  2026-08-26  SELL  DECK  MomReversal  $45.77  P&L $-0.28               |
|  2026-08-26  SELL  AME  Pullback50  $45.74  P&L $-0.24                 |
|  2026-08-26  SELL  NKE  MomReversal  $6.50  P&L $-0.08                 |
|  2026-08-25  SELL  AAPL  Pullback50  $45.89  P&L $-0.25                |
|  2026-08-25  SELL  GOOGL  Pullback50  $45.94  P&L $-0.25               |
|  2026-08-25  SELL  CAH  Pullback50  $46.12  P&L $+0.01                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-27T09:18:01.328903-04:00 share=25% ===
2026-08-27 09:18:01,328 INFO === options_live_micro LIVE 2026-08-27T09:18:01.328903-04:00 share=25% ===
Live account equity $306.81 cash $213.92 #225458845 options_level=3
2026-08-27 09:18:01,411 INFO Live account equity $306.81 cash $213.92 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-08-27 09:18:01,434 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-08-27 09:18:01,455 INFO Live micro done. open_options=0 lots=0
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
## Ledger health — 2026-08-27
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
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-27_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-27_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=821 med=-47.5% | TAINTED n=1761 med=-39.3% | KEEP-only n=294 med=+37.5% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=306.81 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | MomReversal | 17 | 41% | +0.24% | -0.61% | -1.60% | 1.81 | 1.6d | $+3.17 | WATCH |
| 3 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260827T132342Z

- UTC timestamp: `20260827T132342Z`
- GitHub run: [#8264](https://github.com/28twagg-ops/TradingBot/actions/runs/33076274558)
- Run id: `33076274558`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`10s`
- Full logs: `logs/action_runs/20260827T132342Z_live_bot.log`, `logs/action_runs/20260827T132342Z_live_options.log`, `logs/action_runs/20260827T132342Z_options_bot.log`


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
{"ts_et":"2026-08-27T09:23:47.559094-04:00","date":"2026-08-27","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.1,"phases_s":{"reconcile":0.36},"signals":0,"placed":0,"equity":999930.56,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"8264","github_run_id":"33076274558","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:23:43  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:23 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $306.68|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $306.68|
|  Cash                                                           $213.92|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $92.76|
|  Open P&L                                                        $+0.88|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $45.96     $14.73   $14.72   -0.0%   $-0.02  |
|  APH      Pullback50      $46.80     $161.66  $164.83  +2.0%   $+0.90  |
|                                                                        |
|  Total invested                                                  $92.76|
|  Total open P&L                                                  $+0.88|
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
|  2026-08-26  SELL  DECK  MomReversal  $45.77  P&L $-0.28               |
|  2026-08-26  SELL  AME  Pullback50  $45.74  P&L $-0.24                 |
|  2026-08-26  SELL  NKE  MomReversal  $6.50  P&L $-0.08                 |
|  2026-08-25  SELL  AAPL  Pullback50  $45.89  P&L $-0.25                |
|  2026-08-25  SELL  GOOGL  Pullback50  $45.94  P&L $-0.25               |
|  2026-08-25  SELL  CAH  Pullback50  $46.12  P&L $+0.01                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-27T09:23:45.274964-04:00 share=25% ===
2026-08-27 09:23:45,275 INFO === options_live_micro LIVE 2026-08-27T09:23:45.274964-04:00 share=25% ===
Live account equity $306.68 cash $213.92 #225458845 options_level=3
2026-08-27 09:23:45,520 INFO Live account equity $306.68 cash $213.92 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-08-27 09:23:45,593 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-08-27 09:23:45,664 INFO Live micro done. open_options=0 lots=0
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
## Ledger health — 2026-08-27
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
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-27_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-27_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=821 med=-47.5% | TAINTED n=1761 med=-39.3% | KEEP-only n=294 med=+37.5% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=306.68 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | MomReversal | 17 | 41% | +0.24% | -0.61% | -1.60% | 1.81 | 1.6d | $+3.17 | WATCH |
| 3 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260827T132555Z

- UTC timestamp: `20260827T132555Z`
- GitHub run: [#8265](https://github.com/28twagg-ops/TradingBot/actions/runs/33076705414)
- Run id: `33076705414`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`10s`
- Full logs: `logs/action_runs/20260827T132555Z_live_bot.log`, `logs/action_runs/20260827T132555Z_live_options.log`, `logs/action_runs/20260827T132555Z_options_bot.log`


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
{"ts_et":"2026-08-27T09:26:00.020967-04:00","date":"2026-08-27","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.1,"phases_s":{"reconcile":0.35},"signals":0,"placed":0,"equity":999930.56,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"8265","github_run_id":"33076705414","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:25:56  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:25 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $306.68|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $306.68|
|  Cash                                                           $213.92|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $92.76|
|  Open P&L                                                        $+0.88|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $45.96     $14.73   $14.72   -0.0%   $-0.02  |
|  APH      Pullback50      $46.80     $161.66  $164.83  +2.0%   $+0.90  |
|                                                                        |
|  Total invested                                                  $92.76|
|  Total open P&L                                                  $+0.88|
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
|  2026-08-26  SELL  DECK  MomReversal  $45.77  P&L $-0.28               |
|  2026-08-26  SELL  AME  Pullback50  $45.74  P&L $-0.24                 |
|  2026-08-26  SELL  NKE  MomReversal  $6.50  P&L $-0.08                 |
|  2026-08-25  SELL  AAPL  Pullback50  $45.89  P&L $-0.25                |
|  2026-08-25  SELL  GOOGL  Pullback50  $45.94  P&L $-0.25               |
|  2026-08-25  SELL  CAH  Pullback50  $46.12  P&L $+0.01                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-27T09:25:57.999438-04:00 share=25% ===
2026-08-27 09:25:57,999 INFO === options_live_micro LIVE 2026-08-27T09:25:57.999438-04:00 share=25% ===
Live account equity $306.68 cash $213.92 #225458845 options_level=3
2026-08-27 09:25:58,235 INFO Live account equity $306.68 cash $213.92 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-08-27 09:25:58,318 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-08-27 09:25:58,388 INFO Live micro done. open_options=0 lots=0
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
## Ledger health — 2026-08-27
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
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-27_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-27_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=821 med=-47.5% | TAINTED n=1761 med=-39.3% | KEEP-only n=294 med=+37.5% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=306.68 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | MomReversal | 17 | 41% | +0.24% | -0.61% | -1.60% | 1.81 | 1.6d | $+3.17 | WATCH |
| 3 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260827T133053Z

- UTC timestamp: `20260827T133053Z`
- GitHub run: [#8266](https://github.com/28twagg-ops/TradingBot/actions/runs/33077136525)
- Run id: `33077136525`
- Live bot: exit=`0`, duration=`217s`
- Live options: exit=`0`, duration=`7s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260827T133053Z_live_bot.log`, `logs/action_runs/20260827T133053Z_live_options.log`, `logs/action_runs/20260827T133053Z_options_bot.log`


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
{"ts_et":"2026-08-27T09:26:00.020967-04:00","date":"2026-08-27","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.1,"phases_s":{"reconcile":0.35},"signals":0,"placed":0,"equity":999930.56,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"8265","github_run_id":"33076705414","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:30:54  INFO      Mode: morning_prep
13:30:56  INFO        [prep_positions] 2/2 (2 valid)
13:30:56  INFO      Fetching tickers (universe=both)...
13:30:56  INFO        S&P 500: 503
13:30:56  INFO        MidCap 400: 400
13:30:56  INFO        Total: 903 tickers
13:30:57  INFO        [prep_universe] 40/901 (40 valid)
13:30:59  INFO        [prep_universe] 80/901 (80 valid)
13:31:01  INFO        [prep_universe] 120/901 (120 valid)
13:31:02  INFO        [prep_universe] 160/901 (160 valid)
13:31:04  INFO        [prep_universe] 200/901 (199 valid)
13:31:09  INFO        [prep_universe] 240/901 (238 valid)
13:31:22  INFO        [prep_universe] 280/901 (278 valid)
13:31:34  INFO        [prep_universe] 320/901 (318 valid)
13:31:47  INFO        [prep_universe] 360/901 (358 valid)
13:31:57  INFO        [prep_universe] 400/901 (397 valid)
13:32:11  INFO        [prep_universe] 440/901 (437 valid)
13:32:21  INFO        [prep_universe] 480/901 (477 valid)
13:32:35  INFO        [prep_universe] 520/901 (517 valid)
13:32:45  INFO        [prep_universe] 560/901 (557 valid)
13:32:58  INFO        [prep_universe] 600/901 (597 valid)
13:33:09  INFO        [prep_universe] 640/901 (637 valid)
13:33:22  INFO        [prep_universe] 680/901 (677 valid)
13:33:33  INFO        [prep_universe] 720/901 (717 valid)
13:33:46  INFO        [prep_universe] 760/901 (757 valid)
13:33:57  INFO        [prep_universe] 800/901 (797 valid)
13:34:10  INFO        [prep_universe] 840/901 (836 valid)
13:34:20  INFO        [prep_universe] 880/901 (876 valid)
13:34:27  INFO        [prep_universe] 901/901 (897 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:30 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $306.17|
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
|  Open positions                                                       2|
|  Invested                                                        $92.25|
|  Open P&L                                                        $+0.37|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $45.96     $14.73   $14.72   -0.0%   $-0.02  |
|  APH      Pullback50      $46.29     $161.66  $163.03  +0.8%   $+0.39  |
+========================================================================+

+========================================================================+
|                            OPEN SELL ORDERS                            |
+========================================================================+
|  Count                                                                1|
|  TICKER    TYPE              QTY       LIMIT       STOP                |
+------------------------------------------------------------------------+
|  AES       OrderType.STOP    3         None        14.65               |
+========================================================================+

+========================================================================+
|                              PREP SUMMARY                              |
+========================================================================+
|  Saved                                                              yes|
|  Exit candidates                                                      0|
|  Signal candidates                                                   37|
|  Universe scanned                                                   901|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-27T09:34:30.969226-04:00 share=25% ===
2026-08-27 09:34:30,969 INFO === options_live_micro LIVE 2026-08-27T09:34:30.969226-04:00 share=25% ===
Live account equity $306.02 cash $213.92 #225458845 options_level=3
2026-08-27 09:34:31,211 INFO Live account equity $306.02 cash $213.92 #225458845 options_level=3
Live micro sleeve $77 (25% of $306) deployed $0 open_strategies=0/3 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy / min_cost $20)
2026-08-27 09:34:31,511 INFO Live micro sleeve $77 (25% of $306) deployed $0 open_strategies=0/3 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy / min_cost $20)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win
2026-08-27 09:34:31,511 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win
Live micro signals: 4
2026-08-27 09:34:36,049 INFO Live micro signals: 4
  try S404 100%win/+80%med CELH
2026-08-27 09:34:36,049 INFO   try S404 100%win/+80%med CELH
  skip S404 CELH: no contract under $75
2026-08-27 09:34:36,694 INFO   skip S404 CELH: no contract under $75
  try S404 100%win/+80%med HRL
2026-08-27 09:34:36,694 INFO   try S404 100%win/+80%med HRL
  skip S404 HRL: no contract under $75
2026-08-27 09:34:36,924 INFO   skip S404 HRL: no contract under $75
  try S404 100%win/+80%med MRK
2026-08-27 09:34:36,924 INFO   try S404 100%win/+80%med MRK
  skip S404 MRK: no contract under $75
2026-08-27 09:34:37,139 INFO   skip S404 MRK: no contract under $75
  try S406 56%win/+58%med MRK
2026-08-27 09:34:37,139 INFO   try S406 56%win/+58%med MRK
  skip S406 MRK: no contract under $75
2026-08-27 09:34:37,402 INFO   skip S406 MRK: no contract under $75
Live micro done. open_options=0 lots=0
2026-08-27 09:34:37,545 INFO Live micro done. open_options=0 lots=0
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
=== options_morning_bot (PAPER) 2026-08-27T09:34:39.113632-04:00 ===

[Run context]
Paper auth OK — equity $999930.56, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Allowed (new entries only): S218, S404, S406

[Scan + entries]
Scanning 117 symbols for [S218, S404, S406] …
Fetched daily bars for 113/117 symbols
```

---

## Run 20260827T133629Z

- UTC timestamp: `20260827T133629Z`
- GitHub run: [#8267](https://github.com/28twagg-ops/TradingBot/actions/runs/33077580171)
- Run id: `33077580171`
- Live bot: exit=`0`, duration=`215s`
- Live options: exit=`0`, duration=`7s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260827T133629Z_live_bot.log`, `logs/action_runs/20260827T133629Z_live_options.log`, `logs/action_runs/20260827T133629Z_options_bot.log`


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
{"ts_et":"2026-08-27T09:26:00.020967-04:00","date":"2026-08-27","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.1,"phases_s":{"reconcile":0.35},"signals":0,"placed":0,"equity":999930.56,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"8265","github_run_id":"33076705414","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:36:30  INFO      Mode: morning_prep
13:36:31  INFO        [prep_positions] 2/2 (2 valid)
13:36:31  INFO      Fetching tickers (universe=both)...
13:36:31  INFO        S&P 500: 503
13:36:32  INFO        MidCap 400: 400
13:36:32  INFO        Total: 903 tickers
13:36:32  INFO        [prep_universe] 40/901 (40 valid)
13:36:34  INFO        [prep_universe] 80/901 (80 valid)
13:36:35  INFO        [prep_universe] 120/901 (120 valid)
13:36:36  INFO        [prep_universe] 160/901 (160 valid)
13:36:37  INFO        [prep_universe] 200/901 (199 valid)
13:36:44  INFO        [prep_universe] 240/901 (238 valid)
13:36:57  INFO        [prep_universe] 280/901 (278 valid)
13:37:10  INFO        [prep_universe] 320/901 (318 valid)
13:37:20  INFO        [prep_universe] 360/901 (358 valid)
13:37:33  INFO        [prep_universe] 400/901 (397 valid)
13:37:46  INFO        [prep_universe] 440/901 (437 valid)
13:37:56  INFO        [prep_universe] 480/901 (477 valid)
13:38:09  INFO        [prep_universe] 520/901 (517 valid)
13:38:21  INFO        [prep_universe] 560/901 (557 valid)
13:38:35  INFO        [prep_universe] 600/901 (597 valid)
13:38:45  INFO        [prep_universe] 640/901 (637 valid)
13:38:57  INFO        [prep_universe] 680/901 (677 valid)
13:39:10  INFO        [prep_universe] 720/901 (717 valid)
13:39:20  INFO        [prep_universe] 760/901 (757 valid)
13:39:33  INFO        [prep_universe] 800/901 (797 valid)
13:39:46  INFO        [prep_universe] 840/901 (836 valid)
13:39:56  INFO        [prep_universe] 880/901 (876 valid)
13:40:03  INFO        [prep_universe] 901/901 (897 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $305.81|
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
|  Open positions                                                       2|
|  Invested                                                        $91.89|
|  Open P&L                                                        $+0.01|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $45.98     $14.73   $14.72   -0.0%   $-0.00  |
|  APH      Pullback50      $45.91     $161.66  $161.70  +0.0%   $+0.01  |
+========================================================================+

+========================================================================+
|                            OPEN SELL ORDERS                            |
+========================================================================+
|  Count                                                                1|
|  TICKER    TYPE              QTY       LIMIT       STOP                |
+------------------------------------------------------------------------+
|  AES       OrderType.STOP    3         None        14.65               |
+========================================================================+

+========================================================================+
|                              PREP SUMMARY                              |
+========================================================================+
|  Saved                                                              yes|
|  Exit candidates                                                      1|
|  Signal candidates                                                   37|
|  Universe scanned                                                   901|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-27T09:40:05.437615-04:00 share=25% ===
2026-08-27 09:40:05,437 INFO === options_live_micro LIVE 2026-08-27T09:40:05.437615-04:00 share=25% ===
Live account equity $305.64 cash $213.92 #225458845 options_level=3
2026-08-27 09:40:05,578 INFO Live account equity $305.64 cash $213.92 #225458845 options_level=3
Live micro sleeve $76 (25% of $306) deployed $0 open_strategies=0/3 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy / min_cost $20)
2026-08-27 09:40:05,736 INFO Live micro sleeve $76 (25% of $306) deployed $0 open_strategies=0/3 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy / min_cost $20)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win
2026-08-27 09:40:05,736 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win
Live micro signals: 10
2026-08-27 09:40:10,572 INFO Live micro signals: 10
  try S404 100%win/+80%med CELH
2026-08-27 09:40:10,572 INFO   try S404 100%win/+80%med CELH
  skip S404 CELH: no contract under $75
2026-08-27 09:40:10,935 INFO   skip S404 CELH: no contract under $75
  try S404 100%win/+80%med HRL
2026-08-27 09:40:10,935 INFO   try S404 100%win/+80%med HRL
  skip S404 HRL: no contract under $75
2026-08-27 09:40:11,112 INFO   skip S404 HRL: no contract under $75
  try S404 100%win/+80%med MRK
2026-08-27 09:40:11,112 INFO   try S404 100%win/+80%med MRK
  skip S404 MRK: no contract under $75
2026-08-27 09:40:11,250 INFO   skip S404 MRK: no contract under $75
  try S406 56%win/+58%med MRK
2026-08-27 09:40:11,250 INFO   try S406 56%win/+58%med MRK
  skip S406 MRK: no contract under $75
2026-08-27 09:40:11,395 INFO   skip S406 MRK: no contract under $75
  try S218 56%win/+49%med AXP
2026-08-27 09:40:11,395 INFO   try S218 56%win/+49%med AXP
  skip S218 AXP: no contract under $75
2026-08-27 09:40:11,519 INFO   skip S218 AXP: no contract under $75
  try S218 56%win/+49%med BAC
2026-08-27 09:40:11,519 INFO   try S218 56%win/+49%med BAC
LIVE BUY S218 56%win BAC BAC260828C00062000 limit=0.31 ask=0.32 cost=$32 id=717ded36-8a17-4589-900b-4905166b45f0
2026-08-27 09:40:11,714 INFO LIVE BUY S218 56%win BAC BAC260828C00062000 limit=0.31 ask=0.32 cost=$32 id=717ded36-8a17-4589-900b-4905166b45f0
  skip S218 HD: already attempted today
2026-08-27 09:40:11,714 INFO   skip S218 HD: already attempted today
  skip S218 MMM: already attempted today
2026-08-27 09:40:11,714 INFO   skip S218 MMM: already attempted today
  skip S218 NKE: already attempted today
2026-08-27 09:40:11,714 INFO   skip S218 NKE: already attempted today
  skip S218 WFC: already attempted today
2026-08-27 09:40:11,714 INFO   skip S218 WFC: already attempted today
LIVE PROT check BAC260828C00062000: have_ols=False open_matched=0 ols_id=- ols_type=-
2026-08-27 09:40:11,791 INFO LIVE PROT check BAC260828C00062000: have_ols=False open_matched=0 ols_id=- ols_type=-
LIVE PROT STOP-MKT BAC260828C00062000 x1 stop=0.19 id=9ab5b626-a8be-4010-8d22-062a2f933bd9
2026-08-27 09:40:11,835 INFO LIVE PROT STOP-MKT BAC260828C00062000 x1 stop=0.19 id=9ab5b626-a8be-4010-8d22-062a2f933bd9
Live micro done. open_options=1 lots=1
2026-08-27 09:40:11,872 INFO Live micro done. open_options=1 lots=1
```

### Paper options bot (tail)

```text

```

---

## Run 20260827T134951Z

- UTC timestamp: `20260827T134951Z`
- GitHub run: [#8269](https://github.com/28twagg-ops/TradingBot/actions/runs/33078466190)
- Run id: `33078466190`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260827T134951Z_live_bot.log`, `logs/action_runs/20260827T134951Z_live_options.log`, `logs/action_runs/20260827T134951Z_options_bot.log`


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
{"ts_et":"2026-08-27T09:26:00.020967-04:00","date":"2026-08-27","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.1,"phases_s":{"reconcile":0.35},"signals":0,"placed":0,"equity":999930.56,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"8265","github_run_id":"33076705414","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:49:52  INFO      Mode: morning_scan
13:49:53  INFO        [positions] 2/2 (2 valid)
13:49:53  INFO        SELL order cancelled AES  type=OrderType.STOP  id=7574126a-a605-475b-bc96-64eb10bb2fa1
13:49:54  INFO        SELL LIMIT AES  qty=3.122512036  limit=$14.72  id=23a933a4-21ee-4776-bbbf-574deb2a1881
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20260827T135123Z

- UTC timestamp: `20260827T135123Z`
- GitHub run: [#8270](https://github.com/28twagg-ops/TradingBot/actions/runs/33078915062)
- Run id: `33078915062`
- Live bot: exit=`0`, duration=`239s`
- Live options: exit=`0`, duration=`3s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260827T135123Z_live_bot.log`, `logs/action_runs/20260827T135123Z_live_options.log`, `logs/action_runs/20260827T135123Z_options_bot.log`


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
{"ts_et":"2026-08-27T09:26:00.020967-04:00","date":"2026-08-27","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.1,"phases_s":{"reconcile":0.35},"signals":0,"placed":0,"equity":999930.56,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"8265","github_run_id":"33076705414","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
... (156 earlier lines - see full log file)
|  SLAB     Pullback50      eq     $218.71  45.2   -2.44   50MA bounce (+|
|  TREX     Pullback50      eq     $46.51   35.1   -1.58   50MA bounce (-|
|  UBSI     Pullback50      eq     $47.11   34.8   -2.91   50MA bounce (-|
|  VNO      Pullback50      eq     $38.95   46.7   -1.35   50MA bounce (-|
|                                                                        |
+========================================================================+

+========================================================================+
|                              ENTRY ORDERS                              |
+========================================================================+
|    ENTER [eq] AES  Pullback50                                    $44.51|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    ENTER [eq] AON  Pullback50                                    $44.51|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    SKIP [eq] AAPL  Pullback50                                     cap 3|
|    SKIP [eq] ACGL  Pullback50                                     cap 3|
|    SKIP [eq] BRK-B  Pullback50                                    cap 3|
|    SKIP [eq] BF-B  Pullback50                                     cap 3|
|    SKIP [eq] CTVA  Pullback50                                     cap 3|
|    SKIP [eq] DDOG  Pullback50                                     cap 3|
|    SKIP [eq] GS  Pullback50                                       cap 3|
|    SKIP [eq] DOC  Pullback50                                      cap 3|
|    SKIP [eq] HUM  Pullback50                                      cap 3|
|    SKIP [eq] KHC  Pullback50                                      cap 3|
|    SKIP [eq] LYV  Pullback50                                      cap 3|
|    SKIP [eq] MS  Pullback50                                       cap 3|
|    SKIP [eq] PFG  Pullback50                                      cap 3|
|    SKIP [eq] PLD  Pullback50                                      cap 3|
|    SKIP [eq] ROST  Pullback50                                     cap 3|
|    SKIP [eq] USB  Pullback50                                      cap 3|
|    SKIP [eq] VTR  Pullback50                                      cap 3|
|    SKIP [eq] VTRS  Pullback50                                     cap 3|
|    SKIP [eq] WST  Pullback50                                      cap 3|
|    SKIP [eq] ASB  Pullback50                                      cap 3|
|    SKIP [eq] BRKR  Pullback50                                     cap 3|
|    SKIP [eq] CDP  Pullback50                                      cap 3|
|    SKIP [eq] CHH  Pullback50                                      cap 3|
|    SKIP [eq] CSL  Pullback50                                      cap 3|
|    SKIP [eq] KEX  Pullback50                                      cap 3|
|    SKIP [eq] LIVN  Pullback50                                     cap 3|
|    SKIP [eq] MTN  Pullback50                                      cap 3|
|    SKIP [eq] NLY  Pullback50                                      cap 3|
|    SKIP [eq] ORI  Pullback50                                      cap 3|
|    SKIP [eq] PNFP  Pullback50                                     cap 3|
|    SKIP [eq] SLAB  Pullback50                                     cap 3|
|    SKIP [eq] TREX  Pullback50                                     cap 3|
|    SKIP [eq] UBSI  Pullback50                                     cap 3|
|    SKIP [eq] VNO  Pullback50                                      cap 3|

+========================================================================+
|                         BUY FILL CONFIRMATION                          |
+========================================================================+
|  Pending submits                                                      2|
+------------------------------------------------------------------------+
|  AES                                                  still unconfirmed|
|  AON                                                  still unconfirmed|
+========================================================================+
+========================================================================+

+========================================================================+
|                           GTC STOP PLACEMENT                           |
+========================================================================+
|  Waiting 5s for 2 buy submit(s) to settle...                           |
+========================================================================+

+========================================================================+
|                            SESSION SUMMARY                             |
+========================================================================+
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Strategy  VolumeSpike + 52wkLow (display only — schedule not enforced)|
|  Scanned                                                            898|
|  Signals                                                             36|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  2 unconfirmed|
|  Exits                                                                0|
|  Open pos                                                             3|
|  Equity                                                         $293.42|
|  Cash                                                           $158.76|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-27T09:55:23.299197-04:00 share=25% ===
2026-08-27 09:55:23,299 INFO === options_live_micro LIVE 2026-08-27T09:55:23.299197-04:00 share=25% ===
Live account equity $293.42 cash $158.76 #225458845 options_level=3
2026-08-27 09:55:23,523 INFO Live account equity $293.42 cash $158.76 #225458845 options_level=3
Live micro sleeve $73 (25% of $293) deployed $0 open_strategies=0/3 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy / min_cost $20)
2026-08-27 09:55:23,739 INFO Live micro sleeve $73 (25% of $293) deployed $0 open_strategies=0/3 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy / min_cost $20)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win
2026-08-27 09:55:23,739 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win
Live micro signals: 4
2026-08-27 09:55:24,825 INFO Live micro signals: 4
  try S404 100%win/+80%med CELH
2026-08-27 09:55:24,826 INFO   try S404 100%win/+80%med CELH
LIVE BUY S404 100%win CELH CELH260828C00033000 limit=0.72 ask=0.73 cost=$73 id=2a15f2d5-ee80-4fa5-9b68-8e453a417674
2026-08-27 09:55:25,392 INFO LIVE BUY S404 100%win CELH CELH260828C00033000 limit=0.72 ask=0.73 cost=$73 id=2a15f2d5-ee80-4fa5-9b68-8e453a417674
  skip S404 HRL: already attempted today
2026-08-27 09:55:25,392 INFO   skip S404 HRL: already attempted today
  skip S404 MRK: already attempted today
2026-08-27 09:55:25,392 INFO   skip S404 MRK: already attempted today
  try S406 56%win/+58%med MRK
2026-08-27 09:55:25,392 INFO   try S406 56%win/+58%med MRK
  skip S406 MRK: no contract under $9
2026-08-27 09:55:25,569 INFO   skip S406 MRK: no contract under $9
LIVE PROT check CELH260828C00033000: have_ols=False open_matched=0 ols_id=- ols_type=-
2026-08-27 09:55:25,678 INFO LIVE PROT check CELH260828C00033000: have_ols=False open_matched=0 ols_id=- ols_type=-
LIVE PROT STOP-MKT CELH260828C00033000 x1 stop=0.43 id=7d84f967-1e61-45bc-b0bf-d20a31a63a3d
2026-08-27 09:55:25,749 INFO LIVE PROT STOP-MKT CELH260828C00033000 x1 stop=0.43 id=7d84f967-1e61-45bc-b0bf-d20a31a63a3d
Live micro done. open_options=1 lots=1
2026-08-27 09:55:25,825 INFO Live micro done. open_options=1 lots=1
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
=== options_morning_bot (PAPER) 2026-08-27T09:55:27.374553-04:00 ===

[Run context]
Paper auth OK — equity $999930.56, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Allowed (new entries only): S218, S404, S406

[Scan + entries]
Scanning 117 symbols for [S218, S404, S406] …
Fetched daily bars for 113/117 symbols
```

---

## Run 20260827T135654Z

- UTC timestamp: `20260827T135654Z`
- GitHub run: [#8271](https://github.com/28twagg-ops/TradingBot/actions/runs/33079364994)
- Run id: `33079364994`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260827T135654Z_live_bot.log`, `logs/action_runs/20260827T135654Z_live_options.log`, `logs/action_runs/20260827T135654Z_options_bot.log`


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
{"ts_et":"2026-08-27T09:26:00.020967-04:00","date":"2026-08-27","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.1,"phases_s":{"reconcile":0.35},"signals":0,"placed":0,"equity":999930.56,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"8265","github_run_id":"33076705414","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:56:55  INFO      Mode: morning_scan
13:56:56  INFO        [positions] 3/3 (3 valid)
13:56:56  INFO        SELL MARKET [urgent] APH closed
13:56:58  INFO        TX logged: SELL APH  P&L -0.57%
13:56:58  INFO        SELL order cancelled AES  type=OrderType.STOP  id=e8aa95ff-1973-4975-824e-479e73f6c2ef
13:56:59  INFO        SELL LIMIT AES  qty=3.022008841  limit=$14.72  id=ddb51092-6e89-4dd2-b00b-0daff75a4ab7
13:57:29  INFO        SELL LIMIT filled AES (confirmed by position check)
13:57:29  INFO        TX logged: SELL AES  P&L -0.04%
13:57:29  INFO        Universe cache hit: 903 tickers (tickers_2026-08-27.json)
13:57:30  INFO        [universe] 40/902 (40 valid)
13:57:31  INFO        [universe] 80/902 (80 valid)
13:57:33  INFO        [universe] 120/902 (120 valid)
13:57:34  INFO        [universe] 160/902 (160 valid)
13:57:35  INFO        [universe] 200/902 (199 valid)
13:57:42  INFO        [universe] 240/902 (238 valid)
13:57:55  INFO        [universe] 280/902 (278 valid)
13:58:05  INFO        [universe] 320/902 (318 valid)
13:58:19  INFO        [universe] 360/902 (358 valid)
13:58:32  INFO        [universe] 400/902 (397 valid)
13:58:42  INFO        [universe] 440/902 (437 valid)
13:58:55  INFO        [universe] 480/902 (477 valid)
13:59:08  INFO        [universe] 520/902 (517 valid)
13:59:18  INFO        [universe] 560/902 (557 valid)
13:59:31  INFO        [universe] 600/902 (597 valid)
13:59:41  INFO        [universe] 640/902 (637 valid)
13:59:54  INFO        [universe] 680/902 (677 valid)
14:00:08  INFO        [universe] 720/902 (717 valid)
14:00:18  INFO        [universe] 760/902 (757 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20260827T140141Z

- UTC timestamp: `20260827T140141Z`
- GitHub run: [#8272](https://github.com/28twagg-ops/TradingBot/actions/runs/33079816718)
- Run id: `33079816718`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`3s`
- Paper options: exit=`0`, duration=`55s`
- Full logs: `logs/action_runs/20260827T140141Z_live_bot.log`, `logs/action_runs/20260827T140141Z_live_options.log`, `logs/action_runs/20260827T140141Z_options_bot.log`


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
{"ts_et":"2026-08-27T10:01:47.397477-04:00","date":"2026-08-27","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":47.4,"phases_s":{"reconcile":0.05,"cancel":0.02,"manage":0.03,"protective_stops":0.01,"scan":46.49,"entries":0.32},"signals":4,"placed":0,"equity":999930.56,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":["S404:CELH","S404:HRL","S404:MRK","S406:MRK"],"github_run":"8272","github_run_id":"33079816718","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:01:42  INFO      Mode: exits
14:01:43  INFO        Daily log -> logs/daily/2026-08-27.md
14:01:43  INFO        Daily log reconciled -> logs/daily/2026-08-27.md (1 ledger rows)
14:01:43  INFO        place_all_stops: checking 2 positions...
14:01:43  INFO        STOP skipped AON: fractional (0.1267 shares) — software exit will handle it
14:01:43  INFO        [positions] 1/1 (1 valid)
14:01:43  INFO        Daily log -> logs/daily/2026-08-27.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $291.31|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AON  P&L +0.0%  $+0.02                                            HOLD|
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
|  CELH260828C00033000     $0.72    $0.70    -2.8%    $-2.00    $70.00   |
|                                                                        |
|  Options open P&L                                                $-2.00|
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
=== options_live_micro LIVE 2026-08-27T10:01:44.476917-04:00 share=25% ===
2026-08-27 10:01:44,476 INFO === options_live_micro LIVE 2026-08-27T10:01:44.476917-04:00 share=25% ===
Live account equity $291.31 cash $176.79 #225458845 options_level=3
2026-08-27 10:01:44,537 INFO Live account equity $291.31 cash $176.79 #225458845 options_level=3
Live micro fill confirmed S404 CELH260828C00033000
2026-08-27 10:01:44,567 INFO Live micro fill confirmed S404 CELH260828C00033000
Live micro hold S404 CELH260828C00033000 -2.8% (tp +50% / sl -40%)
2026-08-27 10:01:44,584 INFO Live micro hold S404 CELH260828C00033000 -2.8% (tp +50% / sl -40%)
Live micro cancel-scan CELH260828C00033000: symbol-scoped n=1
2026-08-27 10:01:44,598 INFO Live micro cancel-scan CELH260828C00033000: symbol-scoped n=1
Live micro cancel-scan CELH260828C00033000: no non-OLS sell to cancel
2026-08-27 10:01:44,598 INFO Live micro cancel-scan CELH260828C00033000: no non-OLS sell to cancel
LIVE PROT check CELH260828C00033000: have_ols=True open_matched=1 ols_id=7d84f967-1e61-45bc-b0bf-d20a31a63a3d ols_type=stop
2026-08-27 10:01:44,622 INFO LIVE PROT check CELH260828C00033000: have_ols=True open_matched=1 ols_id=7d84f967-1e61-45bc-b0bf-d20a31a63a3d ols_type=stop
Live micro sleeve $73 (25% of $291) deployed $70 open_strategies=1/3 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy / min_cost $20)
2026-08-27 10:01:44,701 INFO Live micro sleeve $73 (25% of $291) deployed $70 open_strategies=1/3 (paper baseline $75 / tp=+50% sl=-40% / 1 contract per strategy / min_cost $20)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win
2026-08-27 10:01:44,701 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win
Live micro signals: 4
2026-08-27 10:01:45,643 INFO Live micro signals: 4
  skip S404 CELH: already attempted today
2026-08-27 10:01:45,643 INFO   skip S404 CELH: already attempted today
  skip S404 HRL: already attempted today
2026-08-27 10:01:45,643 INFO   skip S404 HRL: already attempted today
  skip S404 MRK: already attempted today
2026-08-27 10:01:45,643 INFO   skip S404 MRK: already attempted today
  try S406 56%win/+58%med MRK
2026-08-27 10:01:45,643 INFO   try S406 56%win/+58%med MRK
  skip S406 MRK: no contract under $3
2026-08-27 10:01:45,858 INFO   skip S406 MRK: no contract under $3
LIVE PROT check CELH260828C00033000: have_ols=True open_matched=1 ols_id=7d84f967-1e61-45bc-b0bf-d20a31a63a3d ols_type=stop
2026-08-27 10:01:45,883 INFO LIVE PROT check CELH260828C00033000: have_ols=True open_matched=1 ols_id=7d84f967-1e61-45bc-b0bf-d20a31a63a3d ols_type=stop
Live micro done. open_options=1 lots=1
2026-08-27 10:01:45,922 INFO Live micro done. open_options=1 lots=1
```

### Paper options bot (tail)

```text
... (133 earlier lines - see full log file)
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
## Ledger health — 2026-08-27
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
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-27_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-27_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=821 med=-47.5% | TAINTED n=1761 med=-39.3% | KEEP-only n=294 med=+37.5% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=291.31 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | MomReversal | 17 | 41% | +0.24% | -0.61% | -1.60% | 1.81 | 1.6d | $+3.17 | WATCH |
| 3 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---
