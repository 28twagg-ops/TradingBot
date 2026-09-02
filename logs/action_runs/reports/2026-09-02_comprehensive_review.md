# Daily Comprehensive Action Review - 2026-09-02

_Auto-generated from GitHub Actions run output. Each run appends a summary; full stdout is in linked per-run log files._
## Run 20260902T130103Z

- UTC timestamp: `20260902T130103Z`
- GitHub run: [#8788](https://github.com/28twagg-ops/TradingBot/actions/runs/33633111722)
- Run id: `33633111722`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`11s`
- Full logs: `logs/action_runs/20260902T130103Z_live_bot.log`, `logs/action_runs/20260902T130103Z_live_options.log`, `logs/action_runs/20260902T130103Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 832 | 41.8 | -47.2 | +15.3 | $+8,190 |
| TAINTED | 1762 | 33.0 | -39.2 | +12.2 | $-9,207 |
| KEEP-only | 308 | 63.0 | +37.5 | +41.9 | $+5,683 |
| KEEP-only recent | 120 | 58.3 | +50.0 | +50.8 | $+1,657 |

- KEEP strategies (11): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406, S412
- KILL strategies (17): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S352, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-02T09:01:08.659588-04:00","date":"2026-09-02","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.6,"phases_s":{"reconcile":0.08},"signals":0,"placed":0,"equity":999332.06,"open_positions":28,"pending_orders":0,"open_lots":74,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"8788","github_run_id":"33633111722","status":"ok","data_quality":{"clean":{"n":832,"win":41.83,"med":-47.2,"avg":15.32,"pnl":8189.53},"tainted":{"n":1762,"win":33.03,"med":-39.16,"avg":12.18,"pnl":-9207.34},"keep_only":{"n":308,"win":62.99,"med":37.5,"avg":41.88,"pnl":5683.45},"keep_only_recent":{"n":120,"win":58.33,"med":50.0,"avg":50.79,"pnl":1657.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406","S412"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S352","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:01:04  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $231.40|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $231.40|
|  Cash                                                           $162.01|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $69.39|
|  Open P&L                                                        $-0.01|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  BWXT     MomReversal     $34.89     $161.11  $162.00  +0.6%   $+0.19  |
|  SYNA     MomReversal     $34.50     $95.54   $95.00   -0.6%   $-0.20  |
|                                                                        |
|  Total invested                                                  $69.39|
|  Total open P&L                                                  $-0.01|
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
|  2026-09-01  SELL  GME  EarningsDrift  $34.71  P&L $+0.02              |
|  2026-09-01  SELL  EQIX  Pullback50  $34.63  P&L $-0.19                |
|  2026-09-01  SELL  DLR  Pullback50  $34.69  P&L $-0.19                 |
|  2026-09-01  SELL  NVT  MomReversal  $34.43  P&L $-0.45                |
|  2026-08-31  SELL  ARE  Pullback50  $34.98  P&L $+0.16                 |
|  2026-08-31  SELL  FFIV  Pullback50  $34.80  P&L $+0.01                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-02T09:01:05.732829-04:00 share=25% ===
2026-09-02 09:01:05,732 INFO === options_live_micro LIVE 2026-09-02T09:01:05.732829-04:00 share=25% ===
Live account equity $231.40 cash $162.01 #225458845 options_level=3
2026-09-02 09:01:05,945 INFO Live account equity $231.40 cash $162.01 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-02 09:01:05,953 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-02 09:01:05,964 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (150 earlier lines - see full log file)
| Window | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    2 |    1 |    6 |    1 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    21 |
| w2     |    5 |    4 |   10 |    4 |    5 |    4 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    41 |
| w3     |    6 |    5 |   12 |    4 |    6 |    4 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    48 |
| w4     |    5 |    3 |    9 |    2 |    4 |    4 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    36 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 213 | 8 |
| S164 | 235 | 9 |
| S165 | 1681 | 22 |
| S166 | 107 | 5 |
| S167 | 235 | 9 |
| S168 | 156 | 7 |
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
| 2026-09-01 |    8 |    6 |    6 |    2 |    6 |    6 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    34 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-02
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   980 | WARN | <<<
| Missing exit records (post) |   980 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |    74 | INFO |
| Total closed lots           |  1782 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=832 med=-47.2% | TAINTED n=1762 med=-39.2% | KEEP-only n=308 med=+37.5% | KILL=17 KEEP=11
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=231.4 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260902T130558Z

- UTC timestamp: `20260902T130558Z`
- GitHub run: [#8789](https://github.com/28twagg-ops/TradingBot/actions/runs/33633612174)
- Run id: `33633612174`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`5s`
- Paper options: exit=`0`, duration=`12s`
- Full logs: `logs/action_runs/20260902T130558Z_live_bot.log`, `logs/action_runs/20260902T130558Z_live_options.log`, `logs/action_runs/20260902T130558Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 832 | 41.8 | -47.2 | +15.3 | $+8,190 |
| TAINTED | 1762 | 33.0 | -39.2 | +12.2 | $-9,207 |
| KEEP-only | 308 | 63.0 | +37.5 | +41.9 | $+5,683 |
| KEEP-only recent | 120 | 58.3 | +50.0 | +50.8 | $+1,657 |

- KEEP strategies (11): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406, S412
- KILL strategies (17): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S352, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-02T09:06:07.256878-04:00","date":"2026-09-02","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.11},"signals":0,"placed":0,"equity":999332.06,"open_positions":28,"pending_orders":0,"open_lots":74,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"8789","github_run_id":"33633612174","status":"ok","data_quality":{"clean":{"n":832,"win":41.83,"med":-47.2,"avg":15.32,"pnl":8189.53},"tainted":{"n":1762,"win":33.03,"med":-39.16,"avg":12.18,"pnl":-9207.34},"keep_only":{"n":308,"win":62.99,"med":37.5,"avg":41.88,"pnl":5683.45},"keep_only_recent":{"n":120,"win":58.33,"med":50.0,"avg":50.79,"pnl":1657.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406","S412"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S352","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

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
|  Equity                                                         $230.89|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $230.89|
|  Cash                                                           $162.01|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $68.88|
|  Open P&L                                                        $-0.52|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  BWXT     MomReversal     $34.46     $161.11  $160.01  -0.7%   $-0.24  |
|  SYNA     MomReversal     $34.41     $95.54   $94.75   -0.8%   $-0.29  |
|                                                                        |
|  Total invested                                                  $68.88|
|  Total open P&L                                                  $-0.52|
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
|  2026-09-01  SELL  GME  EarningsDrift  $34.71  P&L $+0.02              |
|  2026-09-01  SELL  EQIX  Pullback50  $34.63  P&L $-0.19                |
|  2026-09-01  SELL  DLR  Pullback50  $34.69  P&L $-0.19                 |
|  2026-09-01  SELL  NVT  MomReversal  $34.43  P&L $-0.45                |
|  2026-08-31  SELL  ARE  Pullback50  $34.98  P&L $+0.16                 |
|  2026-08-31  SELL  FFIV  Pullback50  $34.80  P&L $+0.01                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-02T09:06:00.473435-04:00 share=25% ===
2026-09-02 09:06:00,473 INFO === options_live_micro LIVE 2026-09-02T09:06:00.473435-04:00 share=25% ===
Live account equity $230.89 cash $162.01 #225458845 options_level=3
2026-09-02 09:06:04,308 INFO Live account equity $230.89 cash $162.01 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-02 09:06:04,316 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-02 09:06:04,324 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (150 earlier lines - see full log file)
| Window | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    2 |    1 |    6 |    1 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    21 |
| w2     |    5 |    4 |   10 |    4 |    5 |    4 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    41 |
| w3     |    6 |    5 |   12 |    4 |    6 |    4 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    48 |
| w4     |    5 |    3 |    9 |    2 |    4 |    4 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    36 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 213 | 8 |
| S164 | 235 | 9 |
| S165 | 1681 | 22 |
| S166 | 107 | 5 |
| S167 | 235 | 9 |
| S168 | 156 | 7 |
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
| 2026-09-01 |    8 |    6 |    6 |    2 |    6 |    6 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    34 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-02
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   980 | WARN | <<<
| Missing exit records (post) |   980 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |    74 | INFO |
| Total closed lots           |  1782 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=832 med=-47.2% | TAINTED n=1762 med=-39.2% | KEEP-only n=308 med=+37.5% | KILL=17 KEEP=11
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.89 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260902T131101Z

- UTC timestamp: `20260902T131101Z`
- GitHub run: [#8790](https://github.com/28twagg-ops/TradingBot/actions/runs/33634105939)
- Run id: `33634105939`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`12s`
- Full logs: `logs/action_runs/20260902T131101Z_live_bot.log`, `logs/action_runs/20260902T131101Z_live_options.log`, `logs/action_runs/20260902T131101Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 832 | 41.8 | -47.2 | +15.3 | $+8,190 |
| TAINTED | 1762 | 33.0 | -39.2 | +12.2 | $-9,207 |
| KEEP-only | 308 | 63.0 | +37.5 | +41.9 | $+5,683 |
| KEEP-only recent | 120 | 58.3 | +50.0 | +50.8 | $+1,657 |

- KEEP strategies (11): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406, S412
- KILL strategies (17): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S352, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-02T09:11:07.332482-04:00","date":"2026-09-02","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.0,"phases_s":{"reconcile":0.35},"signals":0,"placed":0,"equity":999332.06,"open_positions":28,"pending_orders":0,"open_lots":74,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"8790","github_run_id":"33634105939","status":"ok","data_quality":{"clean":{"n":832,"win":41.83,"med":-47.2,"avg":15.32,"pnl":8189.53},"tainted":{"n":1762,"win":33.03,"med":-39.16,"avg":12.18,"pnl":-9207.34},"keep_only":{"n":308,"win":62.99,"med":37.5,"avg":41.88,"pnl":5683.45},"keep_only_recent":{"n":120,"win":58.33,"med":50.0,"avg":50.79,"pnl":1657.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406","S412"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S352","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:11:02  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.89|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $230.89|
|  Cash                                                           $162.01|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $68.88|
|  Open P&L                                                        $-0.52|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  BWXT     MomReversal     $34.46     $161.11  $160.01  -0.7%   $-0.24  |
|  SYNA     MomReversal     $34.41     $95.54   $94.75   -0.8%   $-0.29  |
|                                                                        |
|  Total invested                                                  $68.88|
|  Total open P&L                                                  $-0.52|
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
|  2026-09-01  SELL  GME  EarningsDrift  $34.71  P&L $+0.02              |
|  2026-09-01  SELL  EQIX  Pullback50  $34.63  P&L $-0.19                |
|  2026-09-01  SELL  DLR  Pullback50  $34.69  P&L $-0.19                 |
|  2026-09-01  SELL  NVT  MomReversal  $34.43  P&L $-0.45                |
|  2026-08-31  SELL  ARE  Pullback50  $34.98  P&L $+0.16                 |
|  2026-08-31  SELL  FFIV  Pullback50  $34.80  P&L $+0.01                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-02T09:11:04.255986-04:00 share=25% ===
2026-09-02 09:11:04,256 INFO === options_live_micro LIVE 2026-09-02T09:11:04.255986-04:00 share=25% ===
Live account equity $230.89 cash $162.01 #225458845 options_level=3
2026-09-02 09:11:04,416 INFO Live account equity $230.89 cash $162.01 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-02 09:11:04,463 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-02 09:11:04,509 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (150 earlier lines - see full log file)
| Window | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    2 |    1 |    6 |    1 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    21 |
| w2     |    5 |    4 |   10 |    4 |    5 |    4 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    41 |
| w3     |    6 |    5 |   12 |    4 |    6 |    4 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    48 |
| w4     |    5 |    3 |    9 |    2 |    4 |    4 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    36 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 213 | 8 |
| S164 | 235 | 9 |
| S165 | 1681 | 22 |
| S166 | 107 | 5 |
| S167 | 235 | 9 |
| S168 | 156 | 7 |
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
| 2026-09-01 |    8 |    6 |    6 |    2 |    6 |    6 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    34 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-02
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   980 | WARN | <<<
| Missing exit records (post) |   980 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |    74 | INFO |
| Total closed lots           |  1782 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=832 med=-47.2% | TAINTED n=1762 med=-39.2% | KEEP-only n=308 med=+37.5% | KILL=17 KEEP=11
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.89 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260902T131614Z

- UTC timestamp: `20260902T131614Z`
- GitHub run: [#8791](https://github.com/28twagg-ops/TradingBot/actions/runs/33634595390)
- Run id: `33634595390`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`10s`
- Full logs: `logs/action_runs/20260902T131614Z_live_bot.log`, `logs/action_runs/20260902T131614Z_live_options.log`, `logs/action_runs/20260902T131614Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 832 | 41.8 | -47.2 | +15.3 | $+8,190 |
| TAINTED | 1762 | 33.0 | -39.2 | +12.2 | $-9,207 |
| KEEP-only | 308 | 63.0 | +37.5 | +41.9 | $+5,683 |
| KEEP-only recent | 120 | 58.3 | +50.0 | +50.8 | $+1,657 |

- KEEP strategies (11): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406, S412
- KILL strategies (17): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S352, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-02T09:16:22.984933-04:00","date":"2026-09-02","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.4,"phases_s":{"reconcile":0.6},"signals":0,"placed":0,"equity":999332.06,"open_positions":28,"pending_orders":0,"open_lots":74,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"8791","github_run_id":"33634595390","status":"ok","data_quality":{"clean":{"n":832,"win":41.83,"med":-47.2,"avg":15.32,"pnl":8189.53},"tainted":{"n":1762,"win":33.03,"med":-39.16,"avg":12.18,"pnl":-9207.34},"keep_only":{"n":308,"win":62.99,"med":37.5,"avg":41.88,"pnl":5683.45},"keep_only_recent":{"n":120,"win":58.33,"med":50.0,"avg":50.79,"pnl":1657.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406","S412"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S352","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:16:17  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.89|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $230.89|
|  Cash                                                           $162.01|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $68.88|
|  Open P&L                                                        $-0.52|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  BWXT     MomReversal     $34.46     $161.11  $160.01  -0.7%   $-0.24  |
|  SYNA     MomReversal     $34.41     $95.54   $94.75   -0.8%   $-0.29  |
|                                                                        |
|  Total invested                                                  $68.88|
|  Total open P&L                                                  $-0.52|
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
|  2026-09-01  SELL  GME  EarningsDrift  $34.71  P&L $+0.02              |
|  2026-09-01  SELL  EQIX  Pullback50  $34.63  P&L $-0.19                |
|  2026-09-01  SELL  DLR  Pullback50  $34.69  P&L $-0.19                 |
|  2026-09-01  SELL  NVT  MomReversal  $34.43  P&L $-0.45                |
|  2026-08-31  SELL  ARE  Pullback50  $34.98  P&L $+0.16                 |
|  2026-08-31  SELL  FFIV  Pullback50  $34.80  P&L $+0.01                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-02T09:16:19.605373-04:00 share=25% ===
2026-09-02 09:16:19,605 INFO === options_live_micro LIVE 2026-09-02T09:16:19.605373-04:00 share=25% ===
Live account equity $230.89 cash $162.01 #225458845 options_level=3
2026-09-02 09:16:19,864 INFO Live account equity $230.89 cash $162.01 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-02 09:16:19,950 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-02 09:16:20,027 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (150 earlier lines - see full log file)
| Window | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    2 |    1 |    6 |    1 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    21 |
| w2     |    5 |    4 |   10 |    4 |    5 |    4 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    41 |
| w3     |    6 |    5 |   12 |    4 |    6 |    4 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    48 |
| w4     |    5 |    3 |    9 |    2 |    4 |    4 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    36 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 213 | 8 |
| S164 | 235 | 9 |
| S165 | 1681 | 22 |
| S166 | 107 | 5 |
| S167 | 235 | 9 |
| S168 | 156 | 7 |
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
| 2026-09-01 |    8 |    6 |    6 |    2 |    6 |    6 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    34 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-02
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   980 | WARN | <<<
| Missing exit records (post) |   980 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |    74 | INFO |
| Total closed lots           |  1782 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=832 med=-47.2% | TAINTED n=1762 med=-39.2% | KEEP-only n=308 med=+37.5% | KILL=17 KEEP=11
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.89 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260902T132058Z

- UTC timestamp: `20260902T132058Z`
- GitHub run: [#8792](https://github.com/28twagg-ops/TradingBot/actions/runs/33635084333)
- Run id: `33635084333`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`12s`
- Full logs: `logs/action_runs/20260902T132058Z_live_bot.log`, `logs/action_runs/20260902T132058Z_live_options.log`, `logs/action_runs/20260902T132058Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 832 | 41.8 | -47.2 | +15.3 | $+8,190 |
| TAINTED | 1762 | 33.0 | -39.2 | +12.2 | $-9,207 |
| KEEP-only | 308 | 63.0 | +37.5 | +41.9 | $+5,683 |
| KEEP-only recent | 120 | 58.3 | +50.0 | +50.8 | $+1,657 |

- KEEP strategies (11): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406, S412
- KILL strategies (17): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S352, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-02T09:21:04.014998-04:00","date":"2026-09-02","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.11},"signals":0,"placed":0,"equity":999332.06,"open_positions":28,"pending_orders":0,"open_lots":74,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"8792","github_run_id":"33635084333","status":"ok","data_quality":{"clean":{"n":832,"win":41.83,"med":-47.2,"avg":15.32,"pnl":8189.53},"tainted":{"n":1762,"win":33.03,"med":-39.16,"avg":12.18,"pnl":-9207.34},"keep_only":{"n":308,"win":62.99,"med":37.5,"avg":41.88,"pnl":5683.45},"keep_only_recent":{"n":120,"win":58.33,"med":50.0,"avg":50.79,"pnl":1657.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406","S412"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S352","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:20:59  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.89|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $230.89|
|  Cash                                                           $162.01|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $68.88|
|  Open P&L                                                        $-0.52|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  BWXT     MomReversal     $34.46     $161.11  $160.01  -0.7%   $-0.24  |
|  SYNA     MomReversal     $34.41     $95.54   $94.75   -0.8%   $-0.29  |
|                                                                        |
|  Total invested                                                  $68.88|
|  Total open P&L                                                  $-0.52|
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
|  2026-09-01  SELL  GME  EarningsDrift  $34.71  P&L $+0.02              |
|  2026-09-01  SELL  EQIX  Pullback50  $34.63  P&L $-0.19                |
|  2026-09-01  SELL  DLR  Pullback50  $34.69  P&L $-0.19                 |
|  2026-09-01  SELL  NVT  MomReversal  $34.43  P&L $-0.45                |
|  2026-08-31  SELL  ARE  Pullback50  $34.98  P&L $+0.16                 |
|  2026-08-31  SELL  FFIV  Pullback50  $34.80  P&L $+0.01                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-02T09:21:00.868383-04:00 share=25% ===
2026-09-02 09:21:00,868 INFO === options_live_micro LIVE 2026-09-02T09:21:00.868383-04:00 share=25% ===
Live account equity $230.89 cash $162.01 #225458845 options_level=3
2026-09-02 09:21:01,157 INFO Live account equity $230.89 cash $162.01 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-02 09:21:01,164 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-02 09:21:01,172 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (150 earlier lines - see full log file)
| Window | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    2 |    1 |    6 |    1 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    21 |
| w2     |    5 |    4 |   10 |    4 |    5 |    4 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    41 |
| w3     |    6 |    5 |   12 |    4 |    6 |    4 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    48 |
| w4     |    5 |    3 |    9 |    2 |    4 |    4 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    36 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 213 | 8 |
| S164 | 235 | 9 |
| S165 | 1681 | 22 |
| S166 | 107 | 5 |
| S167 | 235 | 9 |
| S168 | 156 | 7 |
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
| 2026-09-01 |    8 |    6 |    6 |    2 |    6 |    6 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    34 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-02
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   980 | WARN | <<<
| Missing exit records (post) |   980 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |    74 | INFO |
| Total closed lots           |  1782 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=832 med=-47.2% | TAINTED n=1762 med=-39.2% | KEEP-only n=308 med=+37.5% | KILL=17 KEEP=11
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.89 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260902T132600Z

- UTC timestamp: `20260902T132600Z`
- GitHub run: [#8793](https://github.com/28twagg-ops/TradingBot/actions/runs/33635582162)
- Run id: `33635582162`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`13s`
- Full logs: `logs/action_runs/20260902T132600Z_live_bot.log`, `logs/action_runs/20260902T132600Z_live_options.log`, `logs/action_runs/20260902T132600Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 832 | 41.8 | -47.2 | +15.3 | $+8,190 |
| TAINTED | 1762 | 33.0 | -39.2 | +12.2 | $-9,207 |
| KEEP-only | 308 | 63.0 | +37.5 | +41.9 | $+5,683 |
| KEEP-only recent | 120 | 58.3 | +50.0 | +50.8 | $+1,657 |

- KEEP strategies (11): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406, S412
- KILL strategies (17): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S352, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-02T09:26:05.719709-04:00","date":"2026-09-02","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.11},"signals":0,"placed":0,"equity":999332.06,"open_positions":28,"pending_orders":0,"open_lots":74,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"8793","github_run_id":"33635582162","status":"ok","data_quality":{"clean":{"n":832,"win":41.83,"med":-47.2,"avg":15.32,"pnl":8189.53},"tainted":{"n":1762,"win":33.03,"med":-39.16,"avg":12.18,"pnl":-9207.34},"keep_only":{"n":308,"win":62.99,"med":37.5,"avg":41.88,"pnl":5683.45},"keep_only_recent":{"n":120,"win":58.33,"med":50.0,"avg":50.79,"pnl":1657.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406","S412"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S352","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:26:01  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $231.09|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $231.09|
|  Cash                                                           $162.01|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $69.08|
|  Open P&L                                                        $-0.32|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  BWXT     MomReversal     $34.66     $161.11  $160.94  -0.1%   $-0.04  |
|  SYNA     MomReversal     $34.41     $95.54   $94.75   -0.8%   $-0.29  |
|                                                                        |
|  Total invested                                                  $69.08|
|  Total open P&L                                                  $-0.32|
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
|  2026-09-01  SELL  GME  EarningsDrift  $34.71  P&L $+0.02              |
|  2026-09-01  SELL  EQIX  Pullback50  $34.63  P&L $-0.19                |
|  2026-09-01  SELL  DLR  Pullback50  $34.69  P&L $-0.19                 |
|  2026-09-01  SELL  NVT  MomReversal  $34.43  P&L $-0.45                |
|  2026-08-31  SELL  ARE  Pullback50  $34.98  P&L $+0.16                 |
|  2026-08-31  SELL  FFIV  Pullback50  $34.80  P&L $+0.01                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-02T09:26:02.611618-04:00 share=25% ===
2026-09-02 09:26:02,611 INFO === options_live_micro LIVE 2026-09-02T09:26:02.611618-04:00 share=25% ===
Live account equity $231.09 cash $162.01 #225458845 options_level=3
2026-09-02 09:26:02,669 INFO Live account equity $231.09 cash $162.01 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-02 09:26:02,683 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-02 09:26:02,693 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (150 earlier lines - see full log file)
| Window | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    2 |    1 |    6 |    1 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    21 |
| w2     |    5 |    4 |   10 |    4 |    5 |    4 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    41 |
| w3     |    6 |    5 |   12 |    4 |    6 |    4 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    48 |
| w4     |    5 |    3 |    9 |    2 |    4 |    4 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    36 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 213 | 8 |
| S164 | 235 | 9 |
| S165 | 1681 | 22 |
| S166 | 107 | 5 |
| S167 | 235 | 9 |
| S168 | 156 | 7 |
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
| 2026-09-01 |    8 |    6 |    6 |    2 |    6 |    6 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    34 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-02
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   980 | WARN | <<<
| Missing exit records (post) |   980 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |    74 | INFO |
| Total closed lots           |  1782 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=832 med=-47.2% | TAINTED n=1762 med=-39.2% | KEEP-only n=308 med=+37.5% | KILL=17 KEEP=11
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=231.09 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---
