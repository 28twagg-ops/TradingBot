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

## Run 20260902T133121Z

- UTC timestamp: `20260902T133121Z`
- GitHub run: [#8794](https://github.com/28twagg-ops/TradingBot/actions/runs/33636090032)
- Run id: `33636090032`
- Live bot: exit=`0`, duration=`216s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260902T133121Z_live_bot.log`, `logs/action_runs/20260902T133121Z_live_options.log`, `logs/action_runs/20260902T133121Z_options_bot.log`


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
13:31:22  INFO      Mode: morning_prep
13:31:23  INFO        [prep_positions] 3/3 (3 valid)
13:31:23  INFO      Fetching tickers (universe=both)...
13:31:23  INFO        S&P 500: 503
13:31:24  INFO        MidCap 400: 400
13:31:24  INFO        Total: 903 tickers
13:31:25  INFO        [prep_universe] 40/900 (40 valid)
13:31:27  INFO        [prep_universe] 80/900 (80 valid)
13:31:29  INFO        [prep_universe] 120/900 (120 valid)
13:31:31  INFO        [prep_universe] 160/900 (160 valid)
13:31:32  INFO        [prep_universe] 200/900 (199 valid)
13:31:37  INFO        [prep_universe] 240/900 (238 valid)
13:31:50  INFO        [prep_universe] 280/900 (278 valid)
13:32:00  INFO        [prep_universe] 320/900 (318 valid)
13:32:14  INFO        [prep_universe] 360/900 (358 valid)
13:32:27  INFO        [prep_universe] 400/900 (397 valid)
13:32:37  INFO        [prep_universe] 440/900 (437 valid)
13:32:50  INFO        [prep_universe] 480/900 (477 valid)
13:33:00  INFO        [prep_universe] 520/900 (517 valid)
13:33:14  INFO        [prep_universe] 560/900 (557 valid)
13:33:27  INFO        [prep_universe] 600/900 (597 valid)
13:33:37  INFO        [prep_universe] 640/900 (637 valid)
13:33:50  INFO        [prep_universe] 680/900 (677 valid)
13:34:01  INFO        [prep_universe] 720/900 (717 valid)
13:34:14  INFO        [prep_universe] 760/900 (757 valid)
13:34:27  INFO        [prep_universe] 800/900 (797 valid)
13:34:37  INFO        [prep_universe] 840/900 (836 valid)
13:34:51  INFO        [prep_universe] 880/900 (876 valid)
13:34:54  INFO        [prep_universe] 900/900 (896 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $231.23|
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
|  Invested                                                       $103.92|
|  Open P&L                                                        $-0.17|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  BWXT     MomReversal     $34.26     $161.11  $159.04  -1.3%   $-0.44  |
|  GME      EarningsDrift   $34.97     $18.77   $18.92   +0.8%   $+0.28  |
|  SYNA     MomReversal     $34.70     $95.54   $95.53   -0.0%   $-0.00  |
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
|  Signal candidates                                                   30|
|  Universe scanned                                                   900|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-02T09:34:58.423278-04:00 share=25% ===
2026-09-02 09:34:58,423 INFO === options_live_micro LIVE 2026-09-02T09:34:58.423278-04:00 share=25% ===
Live account equity $231.35 cash $127.31 #225458845 options_level=3
2026-09-02 09:34:58,610 INFO Live account equity $231.35 cash $127.31 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-02 09:34:58,799 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-02 09:34:58,916 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=74 paper_keys=yes dry_run=False
  alpaca positions=26
  FLAG b197|S218|a29e65f5 missing from Alpaca
  FLAG b196|S218|5faa0e4b missing from Alpaca
  FLAG b861|S408|15841d91 missing from Alpaca
  FLAG b860|S408|b52661bc missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$999,392.96
  buying_power=$3,982,411.84 cash=$996,352.96
  open option orders: 20
    NVDA260904C00227500 OrderSide.SELL qty=4 status=OrderStatus.NEW limit=None
    SPY260904C00772000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
    NVDA260909C00232500 OrderSide.SELL qty=3 status=OrderStatus.NEW limit=None
    SMCI260904C00038500 OrderSide.SELL qty=4 status=OrderStatus.NEW limit=None
    MARA260918C00011000 OrderSide.SELL qty=2 status=OrderStatus.NEW limit=None
  open option positions: 26
    AMD260902C00477500 qty=-1 mkt=$-25.00
    AMD260902C00480000 qty=1 mkt=$7.00
    AMD260904C00495000 qty=4 mkt=$160.00
    AMD260904C00497500 qty=12 mkt=$396.00
    AMD260904C00500000 qty=2 mkt=$60.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-02T09:35:02.356797-04:00 ===

[Run context]
Paper auth OK — equity $999370.96, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
  EXIT [b284|lab0284_s351_w3_1045_1120_r1|S351] stop_loss (-79.4%) SELL failed AMD260902C00480000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
2026-09-02 09:35:06,087 INFO   EXIT [b807|lab0807_s404_w4_1120_1135_r2|S404] take_profit (+53.2%) SELL 1 SMCI260904C00038000 @<= 0.92
2026-09-02 09:35:15,104 INFO   EXIT [b799|lab0799_s399_w4_1120_1135_r2|S399] stop_loss (-51.4%) SELL 1 AMD260904C00502500 @<= 0.14
2026-09-02 09:35:19,897 INFO   EXIT [b303|lab0303_s353_w4_1120_1135_r2|S353] take_profit (+53.1%) SELL 1 SMCI260904C00038500 @<= 0.73
2026-09-02 09:35:20,406 INFO   EXIT [b317|lab0317_s355_w3_1045_1120_r2|S355] take_profit (+61.5%) SELL 1 SMCI260911C00040000 @<= 0.82
```

---

## Run 20260902T133642Z

- UTC timestamp: `20260902T133642Z`
- GitHub run: [#8795](https://github.com/28twagg-ops/TradingBot/actions/runs/33636603370)
- Run id: `33636603370`
- Live bot: exit=`0`, duration=`217s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260902T133642Z_live_bot.log`, `logs/action_runs/20260902T133642Z_live_options.log`, `logs/action_runs/20260902T133642Z_options_bot.log`


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
13:36:42  INFO      Mode: morning_prep
13:36:44  INFO        [prep_positions] 3/3 (3 valid)
13:36:44  INFO      Fetching tickers (universe=both)...
13:36:44  INFO        S&P 500: 503
13:36:44  INFO        MidCap 400: 400
13:36:44  INFO        Total: 903 tickers
13:36:45  INFO        [prep_universe] 40/900 (40 valid)
13:36:47  INFO        [prep_universe] 80/900 (80 valid)
13:36:48  INFO        [prep_universe] 120/900 (120 valid)
13:36:49  INFO        [prep_universe] 160/900 (160 valid)
13:36:50  INFO        [prep_universe] 200/900 (199 valid)
13:36:58  INFO        [prep_universe] 240/900 (238 valid)
13:37:11  INFO        [prep_universe] 280/900 (278 valid)
13:37:21  INFO        [prep_universe] 320/900 (318 valid)
13:37:35  INFO        [prep_universe] 360/900 (358 valid)
13:37:45  INFO        [prep_universe] 400/900 (397 valid)
13:37:58  INFO        [prep_universe] 440/900 (437 valid)
13:38:09  INFO        [prep_universe] 480/900 (477 valid)
13:38:22  INFO        [prep_universe] 520/900 (517 valid)
13:38:35  INFO        [prep_universe] 560/900 (557 valid)
13:38:46  INFO        [prep_universe] 600/900 (597 valid)
13:38:59  INFO        [prep_universe] 640/900 (637 valid)
13:39:09  INFO        [prep_universe] 680/900 (677 valid)
13:39:23  INFO        [prep_universe] 720/900 (717 valid)
13:39:33  INFO        [prep_universe] 760/900 (757 valid)
13:39:46  INFO        [prep_universe] 800/900 (797 valid)
13:39:56  INFO        [prep_universe] 840/900 (836 valid)
13:40:10  INFO        [prep_universe] 880/900 (876 valid)
13:40:17  INFO        [prep_universe] 900/900 (896 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $231.28|
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
|  Invested                                                       $103.97|
|  Open P&L                                                        $-0.12|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  BWXT     MomReversal     $34.23     $161.11  $158.92  -1.4%   $-0.47  |
|  GME      EarningsDrift   $34.97     $18.77   $18.92   +0.8%   $+0.28  |
|  SYNA     MomReversal     $34.77     $95.54   $95.74   +0.2%   $+0.07  |
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
|  Signal candidates                                                   30|
|  Universe scanned                                                   900|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-02T09:40:20.357739-04:00 share=25% ===
2026-09-02 09:40:20,357 INFO === options_live_micro LIVE 2026-09-02T09:40:20.357739-04:00 share=25% ===
Live account equity $231.35 cash $127.31 #225458845 options_level=3
2026-09-02 09:40:20,587 INFO Live account equity $231.35 cash $127.31 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-02 09:40:20,791 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-02 09:40:20,937 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=74 paper_keys=yes dry_run=False
  alpaca positions=26
  FLAG b197|S218|a29e65f5 missing from Alpaca
  FLAG b196|S218|5faa0e4b missing from Alpaca
  FLAG b861|S408|15841d91 missing from Alpaca
  FLAG b860|S408|b52661bc missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$999,343.92
  buying_power=$3,973,859.68 cash=$996,464.92
  open option orders: 20
    AMD260902C00480000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=0.16
    SMCI260911C00040000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=0.82
    SMCI260904C00038500 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=0.73
    NVDA260904C00227500 OrderSide.SELL qty=4 status=OrderStatus.NEW limit=None
    SPY260904C00772000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
  open option positions: 26
    AMD260902C00477500 qty=-1 mkt=$-25.00
    AMD260902C00480000 qty=1 mkt=$6.00
    AMD260904C00495000 qty=4 mkt=$180.00
    AMD260904C00497500 qty=12 mkt=$456.00
    AMD260904C00500000 qty=2 mkt=$60.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-02T09:40:24.105676-04:00 ===

[Run context]
Paper auth OK — equity $999347.92, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
2026-09-02 09:40:27,232 INFO   EXIT [b284|lab0284_s351_w3_1045_1120_r1|S351] stop_loss (-82.4%) SELL 1 AMD260902C00480000 @<= 0.03
  EXIT [b798|lab0798_s399_w4_1120_1135_r1|S399] stop_loss (-51.4%) SELL failed AMD260904C00502500: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
2026-09-02 09:40:42,592 INFO   EXIT [b269|lab0269_s403_w4_1120_1135_r2|S403] take_profit (+54.6%) SELL 1 WFC260904C00088000 @<= 0.71
Protective stops: placed=1 upgraded=0 already=19 failed=4 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
```

---

## Run 20260902T134218Z

- UTC timestamp: `20260902T134218Z`
- GitHub run: [#8796](https://github.com/28twagg-ops/TradingBot/actions/runs/33637118535)
- Run id: `33637118535`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260902T134218Z_live_bot.log`, `logs/action_runs/20260902T134218Z_live_options.log`, `logs/action_runs/20260902T134218Z_options_bot.log`


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
13:42:19  INFO      Mode: morning_prep
13:42:19  INFO        [prep_positions] 3/3 (3 valid)
13:42:19  INFO        Universe cache hit: 903 tickers (tickers_2026-09-02.json)
13:42:20  INFO        [prep_universe] 40/900 (40 valid)
13:42:22  INFO        [prep_universe] 80/900 (80 valid)
13:42:23  INFO        [prep_universe] 120/900 (120 valid)
13:42:24  INFO        [prep_universe] 160/900 (160 valid)
13:42:26  INFO        [prep_universe] 200/900 (199 valid)
13:42:33  INFO        [prep_universe] 240/900 (238 valid)
13:42:46  INFO        [prep_universe] 280/900 (278 valid)
13:42:59  INFO        [prep_universe] 320/900 (318 valid)
13:43:09  INFO        [prep_universe] 360/900 (358 valid)
13:43:22  INFO        [prep_universe] 400/900 (397 valid)
13:43:35  INFO        [prep_universe] 440/900 (437 valid)
13:43:45  INFO        [prep_universe] 480/900 (477 valid)
13:43:58  INFO        [prep_universe] 520/900 (517 valid)
13:44:11  INFO        [prep_universe] 560/900 (557 valid)
13:44:21  INFO        [prep_universe] 600/900 (597 valid)
13:44:34  INFO        [prep_universe] 640/900 (637 valid)
13:44:47  INFO        [prep_universe] 680/900 (677 valid)
13:44:57  INFO        [prep_universe] 720/900 (717 valid)
13:45:10  INFO        [prep_universe] 760/900 (757 valid)
13:45:23  INFO        [prep_universe] 800/900 (797 valid)
13:45:33  INFO        [prep_universe] 840/900 (836 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20260902T134652Z

- UTC timestamp: `20260902T134652Z`
- GitHub run: [#8797](https://github.com/28twagg-ops/TradingBot/actions/runs/33637642371)
- Run id: `33637642371`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260902T134652Z_live_bot.log`, `logs/action_runs/20260902T134652Z_live_options.log`, `logs/action_runs/20260902T134652Z_options_bot.log`


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
13:46:53  INFO      Mode: morning_scan
13:46:54  INFO        [positions] 3/3 (3 valid)
13:46:54  INFO        SELL MARKET [urgent] BWXT closed
13:46:57  INFO        TX logged: SELL BWXT  P&L -2.31%
13:46:57  INFO        SELL LIMIT GME  qty=1.84816196  limit=$18.95  id=43ac7571-6e1f-49d2-982c-ab04d2f01de1
13:47:27  INFO        SELL LIMIT filled GME (confirmed by position check)
13:47:27  INFO        TX logged: SELL GME  P&L 1.01%
13:47:27  INFO        Universe cache hit: 903 tickers (tickers_2026-09-02.json)
13:47:28  INFO        [universe] 40/902 (40 valid)
13:47:30  INFO        [universe] 80/902 (80 valid)
13:47:31  INFO        [universe] 120/902 (120 valid)
13:47:32  INFO        [universe] 160/902 (160 valid)
13:47:33  INFO        [universe] 200/902 (199 valid)
13:47:41  INFO        [universe] 240/902 (238 valid)
13:47:54  INFO        [universe] 280/902 (278 valid)
13:48:04  INFO        [universe] 320/902 (318 valid)
13:48:17  INFO        [universe] 360/902 (358 valid)
13:48:30  INFO        [universe] 400/902 (397 valid)
13:48:40  INFO        [universe] 440/902 (437 valid)
13:48:54  INFO        [universe] 480/902 (477 valid)
13:49:04  INFO        [universe] 520/902 (517 valid)
13:49:17  INFO        [universe] 560/902 (557 valid)
13:49:30  INFO        [universe] 600/902 (597 valid)
13:49:41  INFO        [universe] 640/902 (637 valid)
13:49:54  INFO        [universe] 680/902 (677 valid)
13:50:04  INFO        [universe] 720/902 (717 valid)
13:50:17  INFO        [universe] 760/902 (757 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20260902T135130Z

- UTC timestamp: `20260902T135130Z`
- GitHub run: [#8798](https://github.com/28twagg-ops/TradingBot/actions/runs/33638161863)
- Run id: `33638161863`
- Live bot: exit=`0`, duration=`253s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260902T135130Z_live_bot.log`, `logs/action_runs/20260902T135130Z_live_options.log`, `logs/action_runs/20260902T135130Z_options_bot.log`


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
... (146 earlier lines - see full log file)
|  SSB      Pullback50      eq     $105.47  28.2   -2.21   50MA bounce (+|
|                                                                        |13:55:11  INFO        BUY  AES  $34.59  [Pullback50]  id=350e468e-1474-4bdd-9af0-d1d9ee6e272f
13:55:11  INFO        BUY  AMZN  $34.59  [Pullback50]  id=4ae62db2-423b-4609-97da-0ab7122ca63e
13:55:12  INFO        BUY  AIZ  $34.59  [Pullback50]  id=f16989b8-d53e-45cd-b756-c1cdc261349c
13:55:42  INFO        place_all_stops: checking 3 positions...
13:55:42  INFO        STOP-MARKET placed AES  qty=2 (pos=2.3412)  stop=$14.70  id=71d0ee6f-7feb-448a-8e56-39549cfe244c
13:55:42  INFO        STOP skipped AIZ: fractional (0.1216 shares) — software exit will handle it
13:55:42  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
13:55:42  INFO        Daily log -> logs/daily/2026-09-02.md
13:55:42  INFO        Dashboard written → logs/dashboard.md

+========================================================================+

+========================================================================+
|                              ENTRY ORDERS                              |
+========================================================================+
|    ENTER [eq] AES  Pullback50                                    $34.59|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    ENTER [eq] AMZN  Pullback50                                   $34.59|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    ENTER [eq] AIZ  Pullback50                                    $34.59|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    SKIP [eq] BRK-B  Pullback50                                    cap 3|
|    SKIP [eq] CNC  Pullback50                                      cap 3|
|    SKIP [eq] CI  Pullback50                                       cap 3|
|    SKIP [eq] LLY  Pullback50                                      cap 3|
|    SKIP [eq] MU  Pullback50                                       cap 3|
|    SKIP [eq] NTRS  Pullback50                                     cap 3|
|    SKIP [eq] PRU  Pullback50                                      cap 3|
|    SKIP [eq] SW  Pullback50                                       cap 3|
|    SKIP [eq] SWK  Pullback50                                      cap 3|
|    SKIP [eq] STLD  Pullback50                                     cap 3|
|    SKIP [eq] AFG  Pullback50                                      cap 3|
|    SKIP [eq] ARWR  Pullback50                                     cap 3|
|    SKIP [eq] AVT  Pullback50                                      cap 3|
|    SKIP [eq] BRKR  Pullback50                                     cap 3|
|    SKIP [eq] CFR  Pullback50                                      cap 3|
|    SKIP [eq] ELAN  Pullback50                                     cap 3|
|    SKIP [eq] HQY  Pullback50                                      cap 3|
|    SKIP [eq] NLY  Pullback50                                      cap 3|
|    SKIP [eq] NVST  Pullback50                                     cap 3|
|    SKIP [eq] ORI  Pullback50                                      cap 3|
|    SKIP [eq] RS  Pullback50                                       cap 3|
|    SKIP [eq] SLAB  Pullback50                                     cap 3|
|    SKIP [eq] SNX  Pullback50                                      cap 3|
|    SKIP [eq] SSB  Pullback50                                      cap 3|
|    SKIP [eq] DELL  TrendResumption                                cap 3|

+========================================================================+
|                         BUY FILL CONFIRMATION                          |
+========================================================================+
|  Pending submits                                                      3|
+------------------------------------------------------------------------+
|  AES                                                  still unconfirmed|
|  AMZN                                                 still unconfirmed|
|  AIZ                                                  still unconfirmed|
+========================================================================+
+========================================================================+

+========================================================================+
|                           GTC STOP PLACEMENT                           |
+========================================================================+
|  Waiting 5s for 3 buy submit(s) to settle...                           |
+========================================================================+

+========================================================================+
|                            SESSION SUMMARY                             |
+========================================================================+
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Strategy  GapDown + VolumeSpike (display only — schedule not enforced)|
|  Scanned                                                            899|
|  Signals                                                             28|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  3 unconfirmed|
|  Exits                                                                1|
|  Open pos                                                             3|
|  Equity                                                         $230.23|
|  Cash                                                           $126.81|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-02T09:55:43.536834-04:00 share=25% ===
2026-09-02 09:55:43,536 INFO === options_live_micro LIVE 2026-09-02T09:55:43.536834-04:00 share=25% ===
Live account equity $230.22 cash $126.81 #225458845 options_level=3
2026-09-02 09:55:43,704 INFO Live account equity $230.22 cash $126.81 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-02 09:55:43,848 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-02 09:55:43,943 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=70 paper_keys=yes dry_run=False
  alpaca positions=21
  FLAG b805|S404|219de775 missing from Alpaca
  FLAG b804|S404|c5d24808 missing from Alpaca
  FLAG b789|S398|d2011a2f missing from Alpaca
  FLAG b788|S398|340df09e missing from Alpaca
  FLAG b781|S397|206cc1b1 missing from Alpaca
  FLAG b780|S397|8763abf3 missing from Alpaca
  FLAG b301|S353|d09e2e01 missing from Alpaca
  FLAG b300|S353|53b2ae21 missing from Alpaca
  FLAG b284|S351|fff2a0df missing from Alpaca
  FLAG b1141|S163|2b128319 missing from Alpaca
  FLAG b1140|S163|9494c377 missing from Alpaca
  FLAG b1099|S167|a0af6cbb missing from Alpaca
  FLAG b1098|S167|7acae978 missing from Alpaca
  FLAG b1127|S168|eb7bd373 missing from Alpaca
  FLAG b1126|S168|56986ceb missing from Alpaca
  FLAG b1057|S165|aca5d4c9 missing from Alpaca
  FLAG b1056|S165|cbb3cc2e missing from Alpaca
  FLAG b797|S399|ed5d91ab missing from Alpaca
  FLAG b796|S399|b042d07b missing from Alpaca
  FLAG b198|S218|fa5cda04 missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$998,929.37
  buying_power=$3,976,769.48 cash=$997,192.37
  open option orders: 14
    SMCI260904C00038000 OrderSide.SELL qty=3 status=OrderStatus.NEW limit=None
    NVDA260904C00227500 OrderSide.SELL qty=4 status=OrderStatus.NEW limit=None
    NVDA260909C00232500 OrderSide.SELL qty=3 status=OrderStatus.NEW limit=None
    MARA260918C00011000 OrderSide.SELL qty=2 status=OrderStatus.NEW limit=None
    MARA260925C00011500 OrderSide.SELL qty=2 status=OrderStatus.NEW limit=None
  open option positions: 21
    AMD260902C00477500 qty=-1 mkt=$-4.00
    AMD260904C00502500 qty=1 mkt=$10.00
    BA260904C00212500 qty=2 mkt=$122.00
    DKNG260918C00026000 qty=2 mkt=$90.00
    MARA260904C00010000 qty=2 mkt=$68.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-02T09:55:46.556430-04:00 ===

[Run context]
Paper auth OK — equity $998922.37, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
  EXIT [b798|lab0798_s399_w4_1120_1135_r1|S399] stop_loss (-71.4%) SELL failed AMD260904C00502500: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
2026-09-02 09:55:52,314 INFO   EXIT [b268|lab0268_s403_w4_1120_1135_r1|S403] take_profit (+77.3%) SELL 1 WFC260904C00088000 @<= 0.87
Protective stops: placed=2 upgraded=0 already=15 failed=2 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
```

---

## Run 20260902T135716Z

- UTC timestamp: `20260902T135716Z`
- GitHub run: [#8799](https://github.com/28twagg-ops/TradingBot/actions/runs/33638682801)
- Run id: `33638682801`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260902T135716Z_live_bot.log`, `logs/action_runs/20260902T135716Z_live_options.log`, `logs/action_runs/20260902T135716Z_options_bot.log`


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
13:57:18  INFO      Mode: morning_scan
13:57:18  INFO        [positions] 3/3 (3 valid)
13:57:18  INFO        SELL MARKET [urgent] AIZ closed
13:57:20  INFO        TX logged: SELL AIZ  P&L -0.92%
13:57:21  INFO        SELL order cancelled AES  type=OrderType.STOP  id=71d0ee6f-7feb-448a-8e56-39549cfe244c
13:57:21  INFO        SELL LIMIT AES  qty=2.341241308  limit=$14.76  id=6a1705df-1525-4a69-b59c-cd2177ba936a
13:57:51  INFO        SELL LIMIT filled AES (confirmed by position check)
13:57:51  INFO        TX logged: SELL AES  P&L -0.02%
13:57:51  INFO        Universe cache hit: 903 tickers (tickers_2026-09-02.json)
13:57:52  INFO        [universe] 40/902 (40 valid)
13:57:53  INFO        [universe] 80/902 (80 valid)
13:57:54  INFO        [universe] 120/902 (120 valid)
13:57:56  INFO        [universe] 160/902 (160 valid)
13:57:57  INFO        [universe] 200/902 (199 valid)
13:58:04  INFO        [universe] 240/902 (238 valid)
13:58:17  INFO        [universe] 280/902 (278 valid)
13:58:27  INFO        [universe] 320/902 (318 valid)
13:58:40  INFO        [universe] 360/902 (358 valid)
13:58:53  INFO        [universe] 400/902 (397 valid)
13:59:03  INFO        [universe] 440/902 (437 valid)
13:59:16  INFO        [universe] 480/902 (477 valid)
13:59:29  INFO        [universe] 520/902 (517 valid)
13:59:42  INFO        [universe] 560/902 (557 valid)
13:59:52  INFO        [universe] 600/902 (597 valid)
14:00:05  INFO        [universe] 640/902 (637 valid)
14:00:18  INFO        [universe] 680/902 (677 valid)
14:00:28  INFO        [universe] 720/902 (717 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20260902T140150Z

- UTC timestamp: `20260902T140150Z`
- GitHub run: [#8800](https://github.com/28twagg-ops/TradingBot/actions/runs/33639213157)
- Run id: `33639213157`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`128s`
- Full logs: `logs/action_runs/20260902T140150Z_live_bot.log`, `logs/action_runs/20260902T140150Z_live_options.log`, `logs/action_runs/20260902T140150Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 842 | 42.4 | -47.0 | +15.8 | $+8,406 |
| TAINTED | 1763 | 33.1 | -39.0 | +12.2 | $-9,183 |
| KEEP-only | 326 | 62.6 | +37.6 | +39.9 | $+5,594 |
| KEEP-only recent | 138 | 58.0 | +50.0 | +44.9 | $+1,568 |

- KEEP strategies (12): S173, S174, S210, S218, S350, S364, S397, S398, S401, S404, S406, S412
- KILL strategies (17): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S352, S354, S355, S360, S399, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-02T10:01:55.057959-04:00","date":"2026-09-02","mode":"entry+manage","header":"entry+manage (55 new)","elapsed_s":116.3,"phases_s":{"reconcile":0.17,"cancel":0.03,"manage":4.51,"protective_stops":0.35,"scan":54.92,"entries":38.72,"reconcile2":4.35},"signals":135,"placed":55,"equity":999180.35,"open_positions":25,"pending_orders":31,"open_lots":61,"submitted_today":55,"filled_today":24,"unattributed_contracts":0,"top_signals":["S165:SNOW","S164:SNOW","S168:SNOW","S167:SNOW","S163:SNOW","S218:SNOW","S350:SNOW","S351:SNOW"],"github_run":"8800","github_run_id":"33639213157","status":"ok","data_quality":{"clean":{"n":842,"win":42.4,"med":-46.97,"avg":15.85,"pnl":8405.53},"tainted":{"n":1763,"win":33.07,"med":-39.02,"avg":12.2,"pnl":-9183.34},"keep_only":{"n":326,"win":62.58,"med":37.59,"avg":39.86,"pnl":5594.45},"keep_only_recent":{"n":138,"win":57.97,"med":50.0,"avg":44.86,"pnl":1568.0},"keep_strategies":["S173","S174","S210","S218","S350","S364","S397","S398","S401","S404","S406","S412"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S352","S354","S355","S360","S399","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:01:51  INFO      Mode: exits
14:01:51  INFO        Daily log -> logs/daily/2026-09-02.md
14:01:51  INFO        Daily log reconciled -> logs/daily/2026-09-02.md (3 ledger rows)
14:01:51  INFO        place_all_stops: checking 1 positions...
14:01:51  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
14:01:51  INFO        [positions] 1/1 (1 valid)
14:01:51  INFO        Daily log -> logs/daily/2026-09-02.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.25|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMZN  P&L -0.1%  $-0.05                                           HOLD|
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
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
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
=== options_live_micro LIVE 2026-09-02T10:01:52.237553-04:00 share=25% ===
2026-09-02 10:01:52,237 INFO === options_live_micro LIVE 2026-09-02T10:01:52.237553-04:00 share=25% ===
Live account equity $230.25 cash $195.72 #225458845 options_level=3
2026-09-02 10:01:52,282 INFO Live account equity $230.25 cash $195.72 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-02 10:01:52,305 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-02 10:01:52,321 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (199 earlier lines - see full log file)
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    3 |    2 |    7 |    1 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    26 |
| w2     |    5 |    4 |   10 |    4 |    5 |    4 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    41 |
| w3     |    6 |    5 |   12 |    4 |    6 |    4 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    48 |
| w4     |    5 |    3 |    9 |    2 |    4 |    4 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    36 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 215 | 9 |
| S164 | 237 | 10 |
| S165 | 1683 | 23 |
| S166 | 107 | 5 |
| S167 | 237 | 10 |
| S168 | 158 | 8 |
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
| 2026-09-02 |    2 |    2 |    2 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |

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
| Total open lots             |    61 | INFO |
| Total closed lots           |  1793 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=842 med=-47.0% | TAINTED n=1763 med=-39.0% | KEEP-only n=326 med=+37.6% | KILL=17 KEEP=12
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.25 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260902T140601Z

- UTC timestamp: `20260902T140601Z`
- GitHub run: [#8801](https://github.com/28twagg-ops/TradingBot/actions/runs/33639742927)
- Run id: `33639742927`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`125s`
- Full logs: `logs/action_runs/20260902T140601Z_live_bot.log`, `logs/action_runs/20260902T140601Z_live_options.log`, `logs/action_runs/20260902T140601Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 846 | 42.7 | -46.7 | +16.2 | $+8,515 |
| TAINTED | 1763 | 33.1 | -39.0 | +12.2 | $-9,183 |
| KEEP-only | 347 | 62.5 | +37.7 | +42.2 | $+5,995 |
| KEEP-only recent | 159 | 58.5 | +50.0 | +49.2 | $+1,969 |

- KEEP strategies (14): S173, S174, S210, S218, S350, S362, S363, S364, S397, S398, S401, S404, S406, S412
- KILL strategies (17): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S352, S354, S355, S360, S399, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-02T10:06:09.595598-04:00","date":"2026-09-02","mode":"entry+manage","header":"entry+manage (46 new)","elapsed_s":111.1,"phases_s":{"reconcile":0.23,"cancel":0.03,"manage":5.13,"protective_stops":0.54,"scan":46.32,"entries":37.42,"reconcile2":4.94},"signals":135,"placed":46,"equity":999250.38,"open_positions":26,"pending_orders":41,"open_lots":89,"submitted_today":101,"filled_today":60,"unattributed_contracts":0,"top_signals":["S165:SNOW","S164:SNOW","S168:SNOW","S167:SNOW","S163:SNOW","S218:SNOW","S350:SNOW","S351:SNOW"],"github_run":"8801","github_run_id":"33639742927","status":"ok","data_quality":{"clean":{"n":846,"win":42.67,"med":-46.74,"avg":16.21,"pnl":8514.53},"tainted":{"n":1763,"win":33.07,"med":-39.02,"avg":12.2,"pnl":-9183.34},"keep_only":{"n":347,"win":62.54,"med":37.69,"avg":42.17,"pnl":5995.45},"keep_only_recent":{"n":159,"win":58.49,"med":50.0,"avg":49.24,"pnl":1969.0},"keep_strategies":["S173","S174","S210","S218","S350","S362","S363","S364","S397","S398","S401","S404","S406","S412"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S352","S354","S355","S360","S399","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:06:02  INFO      Mode: exits
14:06:03  INFO        Daily log -> logs/daily/2026-09-02.md
14:06:03  INFO        Daily log reconciled -> logs/daily/2026-09-02.md (5 ledger rows)
14:06:03  INFO        place_all_stops: checking 1 positions...
14:06:03  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
14:06:03  INFO        [positions] 1/1 (1 valid)
14:06:03  INFO        Daily log -> logs/daily/2026-09-02.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.29|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMZN  P&L -0.0%  $-0.01                                           HOLD|
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
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
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
=== options_live_micro LIVE 2026-09-02T10:06:04.225400-04:00 share=25% ===
2026-09-02 10:06:04,225 INFO === options_live_micro LIVE 2026-09-02T10:06:04.225400-04:00 share=25% ===
Live account equity $230.28 cash $195.72 #225458845 options_level=3
2026-09-02 10:06:04,298 INFO Live account equity $230.28 cash $195.72 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-02 10:06:04,360 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-02 10:06:04,405 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (205 earlier lines - see full log file)
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    3 |    2 |    7 |    1 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    26 |
| w2     |    6 |    5 |   11 |    4 |    6 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    46 |
| w3     |    6 |    5 |   12 |    4 |    6 |    4 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    48 |
| w4     |    5 |    3 |    9 |    2 |    4 |    4 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    36 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 217 | 9 |
| S164 | 241 | 10 |
| S165 | 1687 | 23 |
| S166 | 107 | 5 |
| S167 | 241 | 10 |
| S168 | 160 | 8 |
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
| 2026-09-02 |    4 |    6 |    6 |    0 |    6 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    26 |

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
| Total open lots             |    89 | INFO |
| Total closed lots           |  1797 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=846 med=-46.7% | TAINTED n=1763 med=-39.0% | KEEP-only n=347 med=+37.7% | KILL=17 KEEP=14
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.29 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260902T141056Z

- UTC timestamp: `20260902T141056Z`
- GitHub run: [#8802](https://github.com/28twagg-ops/TradingBot/actions/runs/33640277947)
- Run id: `33640277947`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`62s`
- Full logs: `logs/action_runs/20260902T141056Z_live_bot.log`, `logs/action_runs/20260902T141056Z_live_options.log`, `logs/action_runs/20260902T141056Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 850 | 42.9 | -46.7 | +16.6 | $+8,711 |
| TAINTED | 1763 | 33.1 | -39.0 | +12.2 | $-9,183 |
| KEEP-only | 348 | 62.6 | +38.0 | +42.3 | $+6,024 |
| KEEP-only recent | 160 | 58.8 | +51.1 | +49.5 | $+1,998 |

- KEEP strategies (14): S173, S174, S210, S218, S350, S362, S363, S364, S397, S398, S401, S404, S406, S412
- KILL strategies (17): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S352, S354, S355, S360, S399, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-02T10:11:02.595471-04:00","date":"2026-09-02","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":54.8,"phases_s":{"reconcile":0.51,"cancel":0.12,"manage":8.18,"protective_stops":3.75,"scan":22.69,"entries":15.43,"reconcile2":0.41},"signals":135,"placed":0,"equity":999248.14,"open_positions":24,"pending_orders":39,"open_lots":87,"submitted_today":101,"filled_today":62,"unattributed_contracts":0,"top_signals":["S165:SNOW","S164:SNOW","S168:SNOW","S167:SNOW","S163:SNOW","S218:SNOW","S350:SNOW","S351:SNOW"],"github_run":"8802","github_run_id":"33640277947","status":"ok","data_quality":{"clean":{"n":850,"win":42.94,"med":-46.67,"avg":16.63,"pnl":8710.53},"tainted":{"n":1763,"win":33.07,"med":-39.02,"avg":12.2,"pnl":-9183.34},"keep_only":{"n":348,"win":62.64,"med":37.96,"avg":42.31,"pnl":6024.45},"keep_only_recent":{"n":160,"win":58.75,"med":51.09,"avg":49.5,"pnl":1998.0},"keep_strategies":["S173","S174","S210","S218","S350","S362","S363","S364","S397","S398","S401","S404","S406","S412"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S352","S354","S355","S360","S399","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:10:58  INFO      Mode: exits
14:10:58  INFO        Daily log -> logs/daily/2026-09-02.md
14:10:58  INFO        Daily log reconciled -> logs/daily/2026-09-02.md (5 ledger rows)
14:10:58  INFO        place_all_stops: checking 1 positions...
14:10:58  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
14:10:59  INFO        [positions] 1/1 (1 valid)
14:10:59  INFO        Daily log -> logs/daily/2026-09-02.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.33|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMZN  P&L +0.1%  $+0.03                                           HOLD|
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
|                                                                        |
|  No open option positions.                                             |
|                                                                        |
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
=== options_live_micro LIVE 2026-09-02T10:10:59.872725-04:00 share=25% ===
2026-09-02 10:10:59,872 INFO === options_live_micro LIVE 2026-09-02T10:10:59.872725-04:00 share=25% ===
Live account equity $230.33 cash $195.72 #225458845 options_level=3
2026-09-02 10:11:00,103 INFO Live account equity $230.33 cash $195.72 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-02 10:11:00,313 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-02 10:11:00,441 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (196 earlier lines - see full log file)
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    3 |    2 |    7 |    1 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    26 |
| w2     |    6 |    5 |   11 |    4 |    6 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    46 |
| w3     |    6 |    5 |   12 |    4 |    6 |    4 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    48 |
| w4     |    5 |    3 |    9 |    2 |    4 |    4 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    36 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 217 | 9 |
| S164 | 241 | 10 |
| S165 | 1687 | 23 |
| S166 | 107 | 5 |
| S167 | 241 | 10 |
| S168 | 160 | 8 |
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
| 2026-09-02 |    4 |    6 |    6 |    0 |    6 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    26 |

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
| Total open lots             |    87 | INFO |
| Total closed lots           |  1801 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=850 med=-46.7% | TAINTED n=1763 med=-39.0% | KEEP-only n=348 med=+38.0% | KILL=17 KEEP=14
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.33 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---
