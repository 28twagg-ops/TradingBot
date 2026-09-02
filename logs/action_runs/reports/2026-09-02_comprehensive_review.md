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

## Run 20260902T141604Z

- UTC timestamp: `20260902T141604Z`
- GitHub run: [#8803](https://github.com/28twagg-ops/TradingBot/actions/runs/33640818405)
- Run id: `33640818405`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`102s`
- Full logs: `logs/action_runs/20260902T141604Z_live_bot.log`, `logs/action_runs/20260902T141604Z_live_options.log`, `logs/action_runs/20260902T141604Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 851 | 43.0 | -46.7 | +16.7 | $+8,762 |
| TAINTED | 1763 | 33.1 | -39.0 | +12.2 | $-9,183 |
| KEEP-only | 348 | 62.6 | +38.0 | +42.3 | $+6,024 |
| KEEP-only recent | 160 | 58.8 | +51.1 | +49.5 | $+1,998 |

- KEEP strategies (14): S173, S174, S210, S218, S350, S362, S363, S364, S397, S398, S401, S404, S406, S412
- KILL strategies (17): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S352, S354, S355, S360, S399, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-02T10:16:12.026373-04:00","date":"2026-09-02","mode":"entry+manage","header":"entry+manage (3 new)","elapsed_s":89.6,"phases_s":{"reconcile":0.39,"cancel":0.15,"manage":8.16,"protective_stops":3.69,"scan":53.87,"entries":18.61,"reconcile2":0.45},"signals":135,"placed":3,"equity":999373.84,"open_positions":20,"pending_orders":42,"open_lots":76,"submitted_today":104,"filled_today":62,"unattributed_contracts":0,"top_signals":["S165:SNOW","S164:SNOW","S168:SNOW","S167:SNOW","S163:SNOW","S218:SNOW","S350:SNOW","S351:SNOW"],"github_run":"8803","github_run_id":"33640818405","status":"ok","data_quality":{"clean":{"n":851,"win":43.01,"med":-46.67,"avg":16.7,"pnl":8761.53},"tainted":{"n":1763,"win":33.07,"med":-39.02,"avg":12.2,"pnl":-9183.34},"keep_only":{"n":348,"win":62.64,"med":37.96,"avg":42.31,"pnl":6024.45},"keep_only_recent":{"n":160,"win":58.75,"med":51.09,"avg":49.5,"pnl":1998.0},"keep_strategies":["S173","S174","S210","S218","S350","S362","S363","S364","S397","S398","S401","S404","S406","S412"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S352","S354","S355","S360","S399","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:16:05  INFO      Mode: exits
14:16:06  INFO        Daily log -> logs/daily/2026-09-02.md
14:16:06  INFO        Daily log reconciled -> logs/daily/2026-09-02.md (5 ledger rows)
14:16:06  INFO        place_all_stops: checking 1 positions...
14:16:06  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
14:16:06  INFO        [positions] 1/1 (1 valid)
14:16:06  INFO        Daily log -> logs/daily/2026-09-02.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.31|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMZN  P&L +0.0%  $+0.00                                           HOLD|
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
=== options_live_micro LIVE 2026-09-02T10:16:07.774968-04:00 share=25% ===
2026-09-02 10:16:07,775 INFO === options_live_micro LIVE 2026-09-02T10:16:07.774968-04:00 share=25% ===
Live account equity $230.31 cash $195.72 #225458845 options_level=3
2026-09-02 10:16:08,021 INFO Live account equity $230.31 cash $195.72 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-02 10:16:08,239 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-02 10:16:08,376 INFO Live micro done. open_options=0 lots=0
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
| Total open lots             |    76 | INFO |
| Total closed lots           |  1802 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=851 med=-46.7% | TAINTED n=1763 med=-39.0% | KEEP-only n=348 med=+38.0% | KILL=17 KEEP=14
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.31 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260902T142303Z

- UTC timestamp: `20260902T142303Z`
- GitHub run: [#8804](https://github.com/28twagg-ops/TradingBot/actions/runs/33641359486)
- Run id: `33641359486`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`65s`
- Full logs: `logs/action_runs/20260902T142303Z_live_bot.log`, `logs/action_runs/20260902T142303Z_live_options.log`, `logs/action_runs/20260902T142303Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 851 | 43.0 | -46.7 | +16.7 | $+8,762 |
| TAINTED | 1763 | 33.1 | -39.0 | +12.2 | $-9,183 |
| KEEP-only | 348 | 62.6 | +38.0 | +42.3 | $+6,024 |
| KEEP-only recent | 160 | 58.8 | +51.1 | +49.5 | $+1,998 |

- KEEP strategies (14): S173, S174, S210, S218, S350, S362, S363, S364, S397, S398, S401, S404, S406, S412
- KILL strategies (17): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S352, S354, S355, S360, S399, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-02T10:23:10.933288-04:00","date":"2026-09-02","mode":"entry+manage","header":"entry+manage (7 new)","elapsed_s":55.0,"phases_s":{"reconcile":0.22,"cancel":0.06,"manage":3.9,"protective_stops":1.08,"scan":40.99,"entries":6.89,"reconcile2":0.16},"signals":135,"placed":7,"equity":999457.82,"open_positions":20,"pending_orders":49,"open_lots":76,"submitted_today":111,"filled_today":62,"unattributed_contracts":0,"top_signals":["S165:SNOW","S164:SNOW","S168:SNOW","S167:SNOW","S163:SNOW","S218:SNOW","S350:SNOW","S351:SNOW"],"github_run":"8804","github_run_id":"33641359486","status":"ok","data_quality":{"clean":{"n":851,"win":43.01,"med":-46.67,"avg":16.7,"pnl":8761.53},"tainted":{"n":1763,"win":33.07,"med":-39.02,"avg":12.2,"pnl":-9183.34},"keep_only":{"n":348,"win":62.64,"med":37.96,"avg":42.31,"pnl":6024.45},"keep_only_recent":{"n":160,"win":58.75,"med":51.09,"avg":49.5,"pnl":1998.0},"keep_strategies":["S173","S174","S210","S218","S350","S362","S363","S364","S397","S398","S401","S404","S406","S412"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S352","S354","S355","S360","S399","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:23:06  INFO      Mode: exits
14:23:06  INFO        Daily log -> logs/daily/2026-09-02.md
14:23:06  INFO        Daily log reconciled -> logs/daily/2026-09-02.md (5 ledger rows)
14:23:06  INFO        place_all_stops: checking 1 positions...
14:23:06  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
14:23:06  INFO        [positions] 1/1 (1 valid)
14:23:07  INFO        Daily log -> logs/daily/2026-09-02.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:23 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.35|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMZN  P&L +0.1%  $+0.04                                           HOLD|
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
=== options_live_micro LIVE 2026-09-02T10:23:07.882453-04:00 share=25% ===
2026-09-02 10:23:07,882 INFO === options_live_micro LIVE 2026-09-02T10:23:07.882453-04:00 share=25% ===
Live account equity $230.35 cash $195.72 #225458845 options_level=3
2026-09-02 10:23:07,986 INFO Live account equity $230.35 cash $195.72 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-02 10:23:08,064 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-02 10:23:08,116 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (189 earlier lines - see full log file)
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    3 |    2 |    7 |    1 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    26 |
| w2     |    6 |    5 |   11 |    5 |    6 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    47 |
| w3     |    6 |    5 |   12 |    4 |    6 |    4 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    48 |
| w4     |    5 |    3 |    9 |    2 |    4 |    4 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    36 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 217 | 9 |
| S164 | 241 | 10 |
| S165 | 1687 | 23 |
| S166 | 109 | 6 |
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
| 2026-09-02 |    4 |    6 |    6 |    2 |    6 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    28 |

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
| Total open lots             |    76 | INFO |
| Total closed lots           |  1802 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=851 med=-46.7% | TAINTED n=1763 med=-39.0% | KEEP-only n=348 med=+38.0% | KILL=17 KEEP=14
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.34 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260902T142600Z

- UTC timestamp: `20260902T142600Z`
- GitHub run: [#8805](https://github.com/28twagg-ops/TradingBot/actions/runs/33641904947)
- Run id: `33641904947`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`100s`
- Full logs: `logs/action_runs/20260902T142600Z_live_bot.log`, `logs/action_runs/20260902T142600Z_live_options.log`, `logs/action_runs/20260902T142600Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 851 | 43.0 | -46.7 | +16.7 | $+8,762 |
| TAINTED | 1765 | 33.1 | -39.0 | +12.2 | $-9,155 |
| KEEP-only | 348 | 62.6 | +38.0 | +42.3 | $+6,024 |
| KEEP-only recent | 160 | 58.8 | +51.1 | +49.5 | $+1,998 |

- KEEP strategies (14): S173, S174, S210, S218, S350, S362, S363, S364, S397, S398, S401, S404, S406, S412
- KILL strategies (17): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S352, S354, S355, S360, S399, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-02T10:26:08.617672-04:00","date":"2026-09-02","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":87.6,"phases_s":{"reconcile":0.59,"cancel":0.17,"manage":8.33,"protective_stops":3.55,"scan":56.02,"entries":14.28,"reconcile2":0.46},"signals":135,"placed":0,"equity":999335.73,"open_positions":21,"pending_orders":46,"open_lots":79,"submitted_today":111,"filled_today":65,"unattributed_contracts":0,"top_signals":["S165:SNOW","S164:SNOW","S168:SNOW","S167:SNOW","S163:SNOW","S218:SNOW","S350:SNOW","S351:SNOW"],"github_run":"8805","github_run_id":"33641904947","status":"ok","data_quality":{"clean":{"n":851,"win":43.01,"med":-46.67,"avg":16.7,"pnl":8761.53},"tainted":{"n":1765,"win":33.09,"med":-39.02,"avg":12.22,"pnl":-9155.34},"keep_only":{"n":348,"win":62.64,"med":37.96,"avg":42.31,"pnl":6024.45},"keep_only_recent":{"n":160,"win":58.75,"med":51.09,"avg":49.5,"pnl":1998.0},"keep_strategies":["S173","S174","S210","S218","S350","S362","S363","S364","S397","S398","S401","S404","S406","S412"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S352","S354","S355","S360","S399","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:26:01  INFO      Mode: exits
14:26:02  INFO        Daily log -> logs/daily/2026-09-02.md
14:26:02  INFO        Daily log reconciled -> logs/daily/2026-09-02.md (5 ledger rows)
14:26:02  INFO        place_all_stops: checking 1 positions...
14:26:02  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
14:26:03  INFO        [positions] 1/1 (1 valid)
14:26:03  INFO        Daily log -> logs/daily/2026-09-02.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.34|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMZN  P&L +0.1%  $+0.04                                           HOLD|
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
=== options_live_micro LIVE 2026-09-02T10:26:04.340775-04:00 share=25% ===
2026-09-02 10:26:04,340 INFO === options_live_micro LIVE 2026-09-02T10:26:04.340775-04:00 share=25% ===
Live account equity $230.34 cash $195.72 #225458845 options_level=3
2026-09-02 10:26:04,566 INFO Live account equity $230.34 cash $195.72 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-02 10:26:04,793 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-02 10:26:04,945 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (186 earlier lines - see full log file)
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    3 |    2 |    7 |    1 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    26 |
| w2     |    6 |    5 |   11 |    5 |    6 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    47 |
| w3     |    6 |    5 |   12 |    4 |    6 |    4 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    48 |
| w4     |    5 |    3 |    9 |    2 |    4 |    4 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    36 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 217 | 9 |
| S164 | 241 | 10 |
| S165 | 1687 | 23 |
| S166 | 109 | 6 |
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
| 2026-09-02 |    4 |    6 |    6 |    2 |    6 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    28 |

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
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    79 | INFO |
| Total closed lots           |  1803 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=851 med=-46.7% | TAINTED n=1765 med=-39.0% | KEEP-only n=348 med=+38.0% | KILL=17 KEEP=14
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.34 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260902T143102Z

- UTC timestamp: `20260902T143102Z`
- GitHub run: [#8806](https://github.com/28twagg-ops/TradingBot/actions/runs/33642449470)
- Run id: `33642449470`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`67s`
- Full logs: `logs/action_runs/20260902T143102Z_live_bot.log`, `logs/action_runs/20260902T143102Z_live_options.log`, `logs/action_runs/20260902T143102Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 851 | 43.0 | -46.7 | +16.7 | $+8,762 |
| TAINTED | 1765 | 33.1 | -39.0 | +12.2 | $-9,155 |
| KEEP-only | 348 | 62.6 | +38.0 | +42.3 | $+6,024 |
| KEEP-only recent | 160 | 58.8 | +51.1 | +49.5 | $+1,998 |

- KEEP strategies (14): S173, S174, S210, S218, S350, S362, S363, S364, S397, S398, S401, S404, S406, S412
- KILL strategies (17): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S352, S354, S355, S360, S399, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-02T10:31:08.114337-04:00","date":"2026-09-02","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":56.3,"phases_s":{"reconcile":0.1,"cancel":0.03,"manage":4.52,"protective_stops":0.56,"scan":45.77,"entries":4.18,"reconcile2":0.13},"signals":135,"placed":0,"equity":999166.73,"open_positions":21,"pending_orders":46,"open_lots":79,"submitted_today":111,"filled_today":65,"unattributed_contracts":0,"top_signals":["S165:SNOW","S164:SNOW","S168:SNOW","S167:SNOW","S163:SNOW","S218:SNOW","S350:SNOW","S351:SNOW"],"github_run":"8806","github_run_id":"33642449470","status":"ok","data_quality":{"clean":{"n":851,"win":43.01,"med":-46.67,"avg":16.7,"pnl":8761.53},"tainted":{"n":1765,"win":33.09,"med":-39.02,"avg":12.22,"pnl":-9155.34},"keep_only":{"n":348,"win":62.64,"med":37.96,"avg":42.31,"pnl":6024.45},"keep_only_recent":{"n":160,"win":58.75,"med":51.09,"avg":49.5,"pnl":1998.0},"keep_strategies":["S173","S174","S210","S218","S350","S362","S363","S364","S397","S398","S401","S404","S406","S412"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S352","S354","S355","S360","S399","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:31:04  INFO      Mode: exits
14:31:04  INFO        Daily log -> logs/daily/2026-09-02.md
14:31:04  INFO        Daily log reconciled -> logs/daily/2026-09-02.md (5 ledger rows)
14:31:04  INFO        place_all_stops: checking 1 positions...
14:31:04  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
14:31:04  INFO        [positions] 1/1 (1 valid)
14:31:04  INFO        Daily log -> logs/daily/2026-09-02.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:31 UTC|
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
=== options_live_micro LIVE 2026-09-02T10:31:05.505638-04:00 share=25% ===
2026-09-02 10:31:05,505 INFO === options_live_micro LIVE 2026-09-02T10:31:05.505638-04:00 share=25% ===
Live account equity $230.33 cash $195.72 #225458845 options_level=3
2026-09-02 10:31:05,548 INFO Live account equity $230.33 cash $195.72 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-02 10:31:05,570 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-02 10:31:05,586 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (190 earlier lines - see full log file)
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    3 |    2 |    7 |    1 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    26 |
| w2     |    6 |    5 |   11 |    5 |    6 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    47 |
| w3     |    6 |    5 |   12 |    4 |    6 |    4 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    48 |
| w4     |    5 |    3 |    9 |    2 |    4 |    4 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    36 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 217 | 9 |
| S164 | 241 | 10 |
| S165 | 1687 | 23 |
| S166 | 109 | 6 |
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
| 2026-09-02 |    4 |    6 |    6 |    2 |    6 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    28 |

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
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    79 | INFO |
| Total closed lots           |  1803 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=851 med=-46.7% | TAINTED n=1765 med=-39.0% | KEEP-only n=348 med=+38.0% | KILL=17 KEEP=14
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.33 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260902T143559Z

- UTC timestamp: `20260902T143559Z`
- GitHub run: [#8807](https://github.com/28twagg-ops/TradingBot/actions/runs/33642981590)
- Run id: `33642981590`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`70s`
- Full logs: `logs/action_runs/20260902T143559Z_live_bot.log`, `logs/action_runs/20260902T143559Z_live_options.log`, `logs/action_runs/20260902T143559Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 851 | 43.0 | -46.7 | +16.7 | $+8,762 |
| TAINTED | 1765 | 33.1 | -39.0 | +12.2 | $-9,155 |
| KEEP-only | 348 | 62.6 | +38.0 | +42.3 | $+6,024 |
| KEEP-only recent | 160 | 58.8 | +51.1 | +49.5 | $+1,998 |

- KEEP strategies (14): S173, S174, S210, S218, S350, S362, S363, S364, S397, S398, S401, S404, S406, S412
- KILL strategies (17): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S352, S354, S355, S360, S399, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-02T10:36:05.632474-04:00","date":"2026-09-02","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":61.6,"phases_s":{"reconcile":0.36,"cancel":0.13,"manage":6.66,"protective_stops":3.14,"scan":35.72,"entries":11.7,"reconcile2":0.39},"signals":135,"placed":0,"equity":999152.73,"open_positions":21,"pending_orders":46,"open_lots":79,"submitted_today":111,"filled_today":65,"unattributed_contracts":0,"top_signals":["S165:SNOW","S164:SNOW","S168:SNOW","S167:SNOW","S163:SNOW","S218:SNOW","S350:SNOW","S351:SNOW"],"github_run":"8807","github_run_id":"33642981590","status":"ok","data_quality":{"clean":{"n":851,"win":43.01,"med":-46.67,"avg":16.7,"pnl":8761.53},"tainted":{"n":1765,"win":33.09,"med":-39.02,"avg":12.22,"pnl":-9155.34},"keep_only":{"n":348,"win":62.64,"med":37.96,"avg":42.31,"pnl":6024.45},"keep_only_recent":{"n":160,"win":58.75,"med":51.09,"avg":49.5,"pnl":1998.0},"keep_strategies":["S173","S174","S210","S218","S350","S362","S363","S364","S397","S398","S401","S404","S406","S412"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S352","S354","S355","S360","S399","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:36:00  INFO      Mode: exits
14:36:01  INFO        Daily log -> logs/daily/2026-09-02.md
14:36:01  INFO        Daily log reconciled -> logs/daily/2026-09-02.md (5 ledger rows)
14:36:01  INFO        place_all_stops: checking 1 positions...
14:36:01  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
14:36:01  INFO        [positions] 1/1 (1 valid)
14:36:01  INFO        Daily log -> logs/daily/2026-09-02.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.31|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMZN  P&L +0.0%  $+0.01                                           HOLD|
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
=== options_live_micro LIVE 2026-09-02T10:36:02.467685-04:00 share=25% ===
2026-09-02 10:36:02,467 INFO === options_live_micro LIVE 2026-09-02T10:36:02.467685-04:00 share=25% ===
Live account equity $230.32 cash $195.72 #225458845 options_level=3
2026-09-02 10:36:02,835 INFO Live account equity $230.32 cash $195.72 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-02 10:36:03,006 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-02 10:36:03,124 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (185 earlier lines - see full log file)
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    3 |    2 |    7 |    1 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    26 |
| w2     |    6 |    5 |   11 |    5 |    6 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    47 |
| w3     |    6 |    5 |   12 |    4 |    6 |    4 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    48 |
| w4     |    5 |    3 |    9 |    2 |    4 |    4 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    36 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 217 | 9 |
| S164 | 241 | 10 |
| S165 | 1687 | 23 |
| S166 | 109 | 6 |
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
| 2026-09-02 |    4 |    6 |    6 |    2 |    6 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    28 |

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
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    79 | INFO |
| Total closed lots           |  1803 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=851 med=-46.7% | TAINTED n=1765 med=-39.0% | KEEP-only n=348 med=+38.0% | KILL=17 KEEP=14
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.31 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260902T144101Z

- UTC timestamp: `20260902T144101Z`
- GitHub run: [#8808](https://github.com/28twagg-ops/TradingBot/actions/runs/33643531686)
- Run id: `33643531686`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`85s`
- Full logs: `logs/action_runs/20260902T144101Z_live_bot.log`, `logs/action_runs/20260902T144101Z_live_options.log`, `logs/action_runs/20260902T144101Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 851 | 43.0 | -46.7 | +16.7 | $+8,762 |
| TAINTED | 1765 | 33.1 | -39.0 | +12.2 | $-9,155 |
| KEEP-only | 348 | 62.6 | +38.0 | +42.3 | $+6,024 |
| KEEP-only recent | 160 | 58.8 | +51.1 | +49.5 | $+1,998 |

- KEEP strategies (14): S173, S174, S210, S218, S350, S362, S363, S364, S397, S398, S401, S404, S406, S412
- KILL strategies (17): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S352, S354, S355, S360, S399, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-02T10:41:08.137048-04:00","date":"2026-09-02","mode":"entry+manage","header":"entry+manage (2 new)","elapsed_s":73.6,"phases_s":{"reconcile":0.34,"cancel":0.13,"manage":7.28,"protective_stops":3.2,"scan":47.25,"entries":11.18,"reconcile2":0.41},"signals":135,"placed":2,"equity":999205.73,"open_positions":22,"pending_orders":46,"open_lots":81,"submitted_today":113,"filled_today":67,"unattributed_contracts":0,"top_signals":["S165:SNOW","S164:SNOW","S168:SNOW","S167:SNOW","S163:SNOW","S218:SNOW","S350:SNOW","S351:SNOW"],"github_run":"8808","github_run_id":"33643531686","status":"ok","data_quality":{"clean":{"n":851,"win":43.01,"med":-46.67,"avg":16.7,"pnl":8761.53},"tainted":{"n":1765,"win":33.09,"med":-39.02,"avg":12.22,"pnl":-9155.34},"keep_only":{"n":348,"win":62.64,"med":37.96,"avg":42.31,"pnl":6024.45},"keep_only_recent":{"n":160,"win":58.75,"med":51.09,"avg":49.5,"pnl":1998.0},"keep_strategies":["S173","S174","S210","S218","S350","S362","S363","S364","S397","S398","S401","S404","S406","S412"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S352","S354","S355","S360","S399","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:41:02  INFO      Mode: exits
14:41:02  INFO        Daily log -> logs/daily/2026-09-02.md
14:41:02  INFO        Daily log reconciled -> logs/daily/2026-09-02.md (5 ledger rows)
14:41:03  INFO        place_all_stops: checking 1 positions...
14:41:03  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
14:41:03  INFO        [positions] 1/1 (1 valid)
14:41:03  INFO        Daily log -> logs/daily/2026-09-02.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.29|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMZN  P&L -0.1%  $-0.02                                           HOLD|
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
=== options_live_micro LIVE 2026-09-02T10:41:04.385046-04:00 share=25% ===
2026-09-02 10:41:04,385 INFO === options_live_micro LIVE 2026-09-02T10:41:04.385046-04:00 share=25% ===
Live account equity $230.28 cash $195.72 #225458845 options_level=3
2026-09-02 10:41:04,605 INFO Live account equity $230.28 cash $195.72 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-02 10:41:04,810 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-02 10:41:04,928 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (184 earlier lines - see full log file)
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    3 |    2 |    7 |    1 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    26 |
| w2     |    6 |    5 |   11 |    5 |    6 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    47 |
| w3     |    6 |    5 |   12 |    4 |    6 |    4 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    48 |
| w4     |    5 |    3 |    9 |    2 |    4 |    4 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    36 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 217 | 9 |
| S164 | 241 | 10 |
| S165 | 1687 | 23 |
| S166 | 109 | 6 |
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
| 2026-09-02 |    4 |    6 |    6 |    2 |    6 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    28 |

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
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    81 | INFO |
| Total closed lots           |  1803 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=851 med=-46.7% | TAINTED n=1765 med=-39.0% | KEEP-only n=348 med=+38.0% | KILL=17 KEEP=14
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.28 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260902T144554Z

- UTC timestamp: `20260902T144554Z`
- GitHub run: [#8809](https://github.com/28twagg-ops/TradingBot/actions/runs/33644084436)
- Run id: `33644084436`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`136s`
- Full logs: `logs/action_runs/20260902T144554Z_live_bot.log`, `logs/action_runs/20260902T144554Z_live_options.log`, `logs/action_runs/20260902T144554Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 851 | 43.0 | -46.7 | +16.7 | $+8,762 |
| TAINTED | 1765 | 33.1 | -39.0 | +12.2 | $-9,155 |
| KEEP-only | 348 | 62.6 | +38.0 | +42.3 | $+6,024 |
| KEEP-only recent | 160 | 58.8 | +51.1 | +49.5 | $+1,998 |

- KEEP strategies (14): S173, S174, S210, S218, S350, S362, S363, S364, S397, S398, S401, S404, S406, S412
- KILL strategies (17): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S352, S354, S355, S360, S399, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-02T10:45:59.562591-04:00","date":"2026-09-02","mode":"entry+manage","header":"entry+manage (37 new)","elapsed_s":124.4,"phases_s":{"reconcile":0.12,"cancel":0.03,"manage":4.76,"protective_stops":0.72,"scan":55.01,"entries":46.53,"reconcile2":4.04},"signals":135,"placed":37,"equity":999222.67,"open_positions":23,"pending_orders":63,"open_lots":101,"submitted_today":150,"filled_today":87,"unattributed_contracts":0,"top_signals":["S165:SNOW","S164:SNOW","S168:SNOW","S167:SNOW","S163:SNOW","S218:SNOW","S350:SNOW","S351:SNOW"],"github_run":"8809","github_run_id":"33644084436","status":"ok","data_quality":{"clean":{"n":851,"win":43.01,"med":-46.67,"avg":16.7,"pnl":8761.53},"tainted":{"n":1765,"win":33.09,"med":-39.02,"avg":12.22,"pnl":-9155.34},"keep_only":{"n":348,"win":62.64,"med":37.96,"avg":42.31,"pnl":6024.45},"keep_only_recent":{"n":160,"win":58.75,"med":51.09,"avg":49.5,"pnl":1998.0},"keep_strategies":["S173","S174","S210","S218","S350","S362","S363","S364","S397","S398","S401","S404","S406","S412"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S352","S354","S355","S360","S399","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:45:55  INFO      Mode: exits
14:45:55  INFO        Daily log -> logs/daily/2026-09-02.md
14:45:55  INFO        Daily log reconciled -> logs/daily/2026-09-02.md (5 ledger rows)
14:45:55  INFO        place_all_stops: checking 1 positions...
14:45:55  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
14:45:55  INFO        [positions] 1/1 (1 valid)
14:45:55  INFO        Daily log -> logs/daily/2026-09-02.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:45 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.28|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMZN  P&L -0.1%  $-0.02                                           HOLD|
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
=== options_live_micro LIVE 2026-09-02T10:45:56.668644-04:00 share=25% ===
2026-09-02 10:45:56,668 INFO === options_live_micro LIVE 2026-09-02T10:45:56.668644-04:00 share=25% ===
Live account equity $230.28 cash $195.72 #225458845 options_level=3
2026-09-02 10:45:56,708 INFO Live account equity $230.28 cash $195.72 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-02 10:45:56,750 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-02 10:45:56,793 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (198 earlier lines - see full log file)
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    3 |    2 |    7 |    1 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    26 |
| w2     |    6 |    5 |   11 |    5 |    6 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    47 |
| w3     |    7 |    6 |   13 |    4 |    7 |    5 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    53 |
| w4     |    5 |    3 |    9 |    2 |    4 |    4 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    36 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 221 | 9 |
| S164 | 243 | 10 |
| S165 | 1689 | 23 |
| S166 | 109 | 6 |
| S167 | 243 | 10 |
| S168 | 164 | 8 |
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
| 2026-09-02 |    8 |    8 |    8 |    2 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    42 |

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
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |   101 | INFO |
| Total closed lots           |  1803 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=851 med=-46.7% | TAINTED n=1765 med=-39.0% | KEEP-only n=348 med=+38.0% | KILL=17 KEEP=14
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.28 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260902T145105Z

- UTC timestamp: `20260902T145105Z`
- GitHub run: [#8810](https://github.com/28twagg-ops/TradingBot/actions/runs/33644625180)
- Run id: `33644625180`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`90s`
- Full logs: `logs/action_runs/20260902T145105Z_live_bot.log`, `logs/action_runs/20260902T145105Z_live_options.log`, `logs/action_runs/20260902T145105Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 851 | 43.0 | -46.7 | +16.7 | $+8,762 |
| TAINTED | 1766 | 33.1 | -39.2 | +12.2 | $-9,184 |
| KEEP-only | 348 | 62.6 | +38.0 | +42.3 | $+6,024 |
| KEEP-only recent | 160 | 58.8 | +51.1 | +49.5 | $+1,998 |

- KEEP strategies (14): S173, S174, S210, S218, S350, S362, S363, S364, S397, S398, S401, S404, S406, S412
- KILL strategies (17): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S352, S354, S355, S360, S399, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-02T10:51:12.313401-04:00","date":"2026-09-02","mode":"entry+manage","header":"entry+manage (4 new)","elapsed_s":78.2,"phases_s":{"reconcile":1.79,"cancel":0.12,"manage":7.96,"protective_stops":2.6,"scan":47.05,"entries":14.49,"reconcile2":0.76},"signals":135,"placed":4,"equity":999008.92,"open_positions":24,"pending_orders":54,"open_lots":114,"submitted_today":154,"filled_today":100,"unattributed_contracts":0,"top_signals":["S165:SNOW","S164:SNOW","S168:SNOW","S167:SNOW","S163:SNOW","S218:SNOW","S350:SNOW","S351:SNOW"],"github_run":"8810","github_run_id":"33644625180","status":"ok","data_quality":{"clean":{"n":851,"win":43.01,"med":-46.67,"avg":16.7,"pnl":8761.53},"tainted":{"n":1766,"win":33.07,"med":-39.16,"avg":12.18,"pnl":-9184.34},"keep_only":{"n":348,"win":62.64,"med":37.96,"avg":42.31,"pnl":6024.45},"keep_only_recent":{"n":160,"win":58.75,"med":51.09,"avg":49.5,"pnl":1998.0},"keep_strategies":["S173","S174","S210","S218","S350","S362","S363","S364","S397","S398","S401","S404","S406","S412"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S352","S354","S355","S360","S399","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:51:06  INFO      Mode: exits
14:51:07  INFO        Daily log -> logs/daily/2026-09-02.md
14:51:07  INFO        Daily log reconciled -> logs/daily/2026-09-02.md (5 ledger rows)
14:51:07  INFO        place_all_stops: checking 1 positions...
14:51:07  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
14:51:07  INFO        [positions] 1/1 (1 valid)
14:51:07  INFO        Daily log -> logs/daily/2026-09-02.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:51 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.28|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMZN  P&L -0.1%  $-0.02                                           HOLD|
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
=== options_live_micro LIVE 2026-09-02T10:51:08.629415-04:00 share=25% ===
2026-09-02 10:51:08,629 INFO === options_live_micro LIVE 2026-09-02T10:51:08.629415-04:00 share=25% ===
Live account equity $230.28 cash $195.72 #225458845 options_level=3
2026-09-02 10:51:08,844 INFO Live account equity $230.28 cash $195.72 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-02 10:51:09,028 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-02 10:51:09,150 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (192 earlier lines - see full log file)
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    3 |    2 |    7 |    1 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    26 |
| w2     |    6 |    5 |   11 |    5 |    6 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    47 |
| w3     |    7 |    6 |   13 |    4 |    7 |    5 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    53 |
| w4     |    5 |    3 |    9 |    2 |    4 |    4 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    36 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 223 | 9 |
| S164 | 243 | 10 |
| S165 | 1689 | 23 |
| S166 | 109 | 6 |
| S167 | 243 | 10 |
| S168 | 166 | 8 |
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
| 2026-09-02 |   10 |    8 |    8 |    2 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    46 |

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
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |   114 | INFO |
| Total closed lots           |  1804 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=851 med=-46.7% | TAINTED n=1766 med=-39.2% | KEEP-only n=348 med=+38.0% | KILL=17 KEEP=14
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.28 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260902T145611Z

- UTC timestamp: `20260902T145611Z`
- GitHub run: [#8811](https://github.com/28twagg-ops/TradingBot/actions/runs/33645164724)
- Run id: `33645164724`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`71s`
- Full logs: `logs/action_runs/20260902T145611Z_live_bot.log`, `logs/action_runs/20260902T145611Z_live_options.log`, `logs/action_runs/20260902T145611Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 851 | 43.0 | -46.7 | +16.7 | $+8,762 |
| TAINTED | 1766 | 33.1 | -39.2 | +12.2 | $-9,184 |
| KEEP-only | 348 | 62.6 | +38.0 | +42.3 | $+6,024 |
| KEEP-only recent | 160 | 58.8 | +51.1 | +49.5 | $+1,998 |

- KEEP strategies (14): S173, S174, S210, S218, S350, S362, S363, S364, S397, S398, S401, S404, S406, S412
- KILL strategies (17): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S352, S354, S355, S360, S399, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-02T10:56:18.465921-04:00","date":"2026-09-02","mode":"entry+manage","header":"entry+manage (2 new)","elapsed_s":60.8,"phases_s":{"reconcile":0.85,"cancel":0.1,"manage":6.25,"protective_stops":2.15,"scan":38.91,"entries":9.49,"reconcile2":0.29},"signals":135,"placed":2,"equity":999040.62,"open_positions":25,"pending_orders":54,"open_lots":116,"submitted_today":156,"filled_today":102,"unattributed_contracts":0,"top_signals":["S165:SNOW","S164:SNOW","S168:SNOW","S167:SNOW","S163:SNOW","S218:SNOW","S350:SNOW","S351:SNOW"],"github_run":"8811","github_run_id":"33645164724","status":"ok","data_quality":{"clean":{"n":851,"win":43.01,"med":-46.67,"avg":16.7,"pnl":8761.53},"tainted":{"n":1766,"win":33.07,"med":-39.16,"avg":12.18,"pnl":-9184.34},"keep_only":{"n":348,"win":62.64,"med":37.96,"avg":42.31,"pnl":6024.45},"keep_only_recent":{"n":160,"win":58.75,"med":51.09,"avg":49.5,"pnl":1998.0},"keep_strategies":["S173","S174","S210","S218","S350","S362","S363","S364","S397","S398","S401","S404","S406","S412"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S352","S354","S355","S360","S399","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:56:13  INFO      Mode: exits
14:56:13  INFO        Daily log -> logs/daily/2026-09-02.md
14:56:13  INFO        Daily log reconciled -> logs/daily/2026-09-02.md (5 ledger rows)
14:56:13  INFO        place_all_stops: checking 1 positions...
14:56:13  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
14:56:14  INFO        [positions] 1/1 (1 valid)
14:56:14  INFO        Daily log -> logs/daily/2026-09-02.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:56 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.30|
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
=== options_live_micro LIVE 2026-09-02T10:56:15.294458-04:00 share=25% ===
2026-09-02 10:56:15,294 INFO === options_live_micro LIVE 2026-09-02T10:56:15.294458-04:00 share=25% ===
Live account equity $230.28 cash $195.72 #225458845 options_level=3
2026-09-02 10:56:15,475 INFO Live account equity $230.28 cash $195.72 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-02 10:56:15,683 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-02 10:56:15,788 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (190 earlier lines - see full log file)
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    3 |    2 |    7 |    1 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    26 |
| w2     |    6 |    5 |   11 |    5 |    6 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    47 |
| w3     |    7 |    6 |   13 |    4 |    7 |    5 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    53 |
| w4     |    5 |    3 |    9 |    2 |    4 |    4 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    36 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 223 | 9 |
| S164 | 243 | 10 |
| S165 | 1689 | 23 |
| S166 | 109 | 6 |
| S167 | 243 | 10 |
| S168 | 166 | 8 |
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
| 2026-09-02 |   10 |    8 |    8 |    2 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    46 |

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
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |   116 | INFO |
| Total closed lots           |  1804 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=851 med=-46.7% | TAINTED n=1766 med=-39.2% | KEEP-only n=348 med=+38.0% | KILL=17 KEEP=14
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.29 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260902T150101Z

- UTC timestamp: `20260902T150101Z`
- GitHub run: [#8812](https://github.com/28twagg-ops/TradingBot/actions/runs/33645694632)
- Run id: `33645694632`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`91s`
- Full logs: `logs/action_runs/20260902T150101Z_live_bot.log`, `logs/action_runs/20260902T150101Z_live_options.log`, `logs/action_runs/20260902T150101Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 851 | 43.0 | -46.7 | +16.7 | $+8,762 |
| TAINTED | 1766 | 33.1 | -39.2 | +12.2 | $-9,184 |
| KEEP-only | 348 | 62.6 | +38.0 | +42.3 | $+6,024 |
| KEEP-only recent | 160 | 58.8 | +51.1 | +49.5 | $+1,998 |

- KEEP strategies (14): S173, S174, S210, S218, S350, S362, S363, S364, S397, S398, S401, S404, S406, S412
- KILL strategies (17): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S352, S354, S355, S360, S399, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-02T11:01:09.507491-04:00","date":"2026-09-02","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":80.4,"phases_s":{"reconcile":0.4,"cancel":0.13,"manage":8.56,"protective_stops":3.41,"scan":51.03,"entries":12.91,"reconcile2":0.34},"signals":135,"placed":0,"equity":998899.62,"open_positions":25,"pending_orders":54,"open_lots":116,"submitted_today":156,"filled_today":102,"unattributed_contracts":0,"top_signals":["S165:SNOW","S164:SNOW","S168:SNOW","S167:SNOW","S163:SNOW","S218:SNOW","S350:SNOW","S351:SNOW"],"github_run":"8812","github_run_id":"33645694632","status":"ok","data_quality":{"clean":{"n":851,"win":43.01,"med":-46.67,"avg":16.7,"pnl":8761.53},"tainted":{"n":1766,"win":33.07,"med":-39.16,"avg":12.18,"pnl":-9184.34},"keep_only":{"n":348,"win":62.64,"med":37.96,"avg":42.31,"pnl":6024.45},"keep_only_recent":{"n":160,"win":58.75,"med":51.09,"avg":49.5,"pnl":1998.0},"keep_strategies":["S173","S174","S210","S218","S350","S362","S363","S364","S397","S398","S401","S404","S406","S412"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S352","S354","S355","S360","S399","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:01:03  INFO      Mode: exits
15:01:03  INFO        Daily log -> logs/daily/2026-09-02.md
15:01:03  INFO        Daily log reconciled -> logs/daily/2026-09-02.md (5 ledger rows)
15:01:04  INFO        place_all_stops: checking 1 positions...
15:01:04  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
15:01:04  INFO        [positions] 1/1 (1 valid)
15:01:04  INFO        Daily log -> logs/daily/2026-09-02.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.26|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMZN  P&L -0.1%  $-0.04                                           HOLD|
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
=== options_live_micro LIVE 2026-09-02T11:01:05.510199-04:00 share=25% ===
2026-09-02 11:01:05,510 INFO === options_live_micro LIVE 2026-09-02T11:01:05.510199-04:00 share=25% ===
Live account equity $230.26 cash $195.72 #225458845 options_level=3
2026-09-02 11:01:05,713 INFO Live account equity $230.26 cash $195.72 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-02 11:01:05,896 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-02 11:01:06,012 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (190 earlier lines - see full log file)
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    3 |    2 |    7 |    1 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    26 |
| w2     |    6 |    5 |   11 |    5 |    6 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    47 |
| w3     |    7 |    6 |   13 |    4 |    7 |    5 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    53 |
| w4     |    5 |    3 |    9 |    2 |    4 |    4 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    36 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 223 | 9 |
| S164 | 243 | 10 |
| S165 | 1689 | 23 |
| S166 | 109 | 6 |
| S167 | 243 | 10 |
| S168 | 166 | 8 |
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
| 2026-09-02 |   10 |    8 |    8 |    2 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    46 |

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
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |   116 | INFO |
| Total closed lots           |  1804 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=851 med=-46.7% | TAINTED n=1766 med=-39.2% | KEEP-only n=348 med=+38.0% | KILL=17 KEEP=14
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.26 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260902T150611Z

- UTC timestamp: `20260902T150611Z`
- GitHub run: [#8813](https://github.com/28twagg-ops/TradingBot/actions/runs/33646238800)
- Run id: `33646238800`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`94s`
- Full logs: `logs/action_runs/20260902T150611Z_live_bot.log`, `logs/action_runs/20260902T150611Z_live_options.log`, `logs/action_runs/20260902T150611Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 851 | 43.0 | -46.7 | +16.7 | $+8,762 |
| TAINTED | 1766 | 33.1 | -39.2 | +12.2 | $-9,184 |
| KEEP-only | 348 | 62.6 | +38.0 | +42.3 | $+6,024 |
| KEEP-only recent | 160 | 58.8 | +51.1 | +49.5 | $+1,998 |

- KEEP strategies (14): S173, S174, S210, S218, S350, S362, S363, S364, S397, S398, S401, S404, S406, S412
- KILL strategies (17): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S352, S354, S355, S360, S399, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-02T11:06:17.639759-04:00","date":"2026-09-02","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":82.7,"phases_s":{"reconcile":0.4,"cancel":0.13,"manage":7.87,"protective_stops":3.09,"scan":54.79,"entries":12.36,"reconcile2":0.35},"signals":135,"placed":0,"equity":998916.62,"open_positions":25,"pending_orders":54,"open_lots":116,"submitted_today":156,"filled_today":102,"unattributed_contracts":0,"top_signals":["S165:SNOW","S164:SNOW","S168:SNOW","S167:SNOW","S163:SNOW","S218:SNOW","S350:SNOW","S351:SNOW"],"github_run":"8813","github_run_id":"33646238800","status":"ok","data_quality":{"clean":{"n":851,"win":43.01,"med":-46.67,"avg":16.7,"pnl":8761.53},"tainted":{"n":1766,"win":33.07,"med":-39.16,"avg":12.18,"pnl":-9184.34},"keep_only":{"n":348,"win":62.64,"med":37.96,"avg":42.31,"pnl":6024.45},"keep_only_recent":{"n":160,"win":58.75,"med":51.09,"avg":49.5,"pnl":1998.0},"keep_strategies":["S173","S174","S210","S218","S350","S362","S363","S364","S397","S398","S401","S404","S406","S412"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S352","S354","S355","S360","S399","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:06:11  INFO      Mode: exits
15:06:12  INFO        Daily log -> logs/daily/2026-09-02.md
15:06:12  INFO        Daily log reconciled -> logs/daily/2026-09-02.md (5 ledger rows)
15:06:12  INFO        place_all_stops: checking 1 positions...
15:06:12  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
15:06:12  INFO        [positions] 1/1 (1 valid)
15:06:13  INFO        Daily log -> logs/daily/2026-09-02.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.35|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMZN  P&L +0.1%  $+0.05                                           HOLD|
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
=== options_live_micro LIVE 2026-09-02T11:06:14.043471-04:00 share=25% ===
2026-09-02 11:06:14,043 INFO === options_live_micro LIVE 2026-09-02T11:06:14.043471-04:00 share=25% ===
Live account equity $230.35 cash $195.72 #225458845 options_level=3
2026-09-02 11:06:14,260 INFO Live account equity $230.35 cash $195.72 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-02 11:06:14,434 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-02 11:06:14,553 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (190 earlier lines - see full log file)
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    3 |    2 |    7 |    1 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    26 |
| w2     |    6 |    5 |   11 |    5 |    6 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    47 |
| w3     |    7 |    6 |   13 |    4 |    7 |    5 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    53 |
| w4     |    5 |    3 |    9 |    2 |    4 |    4 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    36 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 223 | 9 |
| S164 | 243 | 10 |
| S165 | 1689 | 23 |
| S166 | 109 | 6 |
| S167 | 243 | 10 |
| S168 | 166 | 8 |
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
| 2026-09-02 |   10 |    8 |    8 |    2 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    46 |

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
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |   116 | INFO |
| Total closed lots           |  1804 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=851 med=-46.7% | TAINTED n=1766 med=-39.2% | KEEP-only n=348 med=+38.0% | KILL=17 KEEP=14
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.35 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260902T151058Z

- UTC timestamp: `20260902T151058Z`
- GitHub run: [#8814](https://github.com/28twagg-ops/TradingBot/actions/runs/33646779473)
- Run id: `33646779473`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`84s`
- Full logs: `logs/action_runs/20260902T151058Z_live_bot.log`, `logs/action_runs/20260902T151058Z_live_options.log`, `logs/action_runs/20260902T151058Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 851 | 43.0 | -46.7 | +16.7 | $+8,762 |
| TAINTED | 1766 | 33.1 | -39.2 | +12.2 | $-9,184 |
| KEEP-only | 348 | 62.6 | +38.0 | +42.3 | $+6,024 |
| KEEP-only recent | 160 | 58.8 | +51.1 | +49.5 | $+1,998 |

- KEEP strategies (14): S173, S174, S210, S218, S350, S362, S363, S364, S397, S398, S401, S404, S406, S412
- KILL strategies (17): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S352, S354, S355, S360, S399, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-02T11:11:04.175289-04:00","date":"2026-09-02","mode":"entry+manage","header":"entry+manage (2 new)","elapsed_s":73.1,"phases_s":{"reconcile":1.61,"cancel":0.06,"manage":6.06,"protective_stops":1.65,"scan":55.02,"entries":6.21,"reconcile2":0.2},"signals":135,"placed":2,"equity":998869.41,"open_positions":26,"pending_orders":49,"open_lots":123,"submitted_today":158,"filled_today":109,"unattributed_contracts":0,"top_signals":["S165:SNOW","S164:SNOW","S168:SNOW","S167:SNOW","S163:SNOW","S218:SNOW","S350:SNOW","S351:SNOW"],"github_run":"8814","github_run_id":"33646779473","status":"ok","data_quality":{"clean":{"n":851,"win":43.01,"med":-46.67,"avg":16.7,"pnl":8761.53},"tainted":{"n":1766,"win":33.07,"med":-39.16,"avg":12.18,"pnl":-9184.34},"keep_only":{"n":348,"win":62.64,"med":37.96,"avg":42.31,"pnl":6024.45},"keep_only_recent":{"n":160,"win":58.75,"med":51.09,"avg":49.5,"pnl":1998.0},"keep_strategies":["S173","S174","S210","S218","S350","S362","S363","S364","S397","S398","S401","S404","S406","S412"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S352","S354","S355","S360","S399","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:10:59  INFO      Mode: exits
15:10:59  INFO        Daily log -> logs/daily/2026-09-02.md
15:10:59  INFO        Daily log reconciled -> logs/daily/2026-09-02.md (5 ledger rows)
15:10:59  INFO        place_all_stops: checking 1 positions...
15:10:59  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
15:11:00  INFO        [positions] 1/1 (1 valid)
15:11:00  INFO        Daily log -> logs/daily/2026-09-02.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.26|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMZN  P&L -0.1%  $-0.04                                           HOLD|
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
=== options_live_micro LIVE 2026-09-02T11:11:01.017269-04:00 share=25% ===
2026-09-02 11:11:01,017 INFO === options_live_micro LIVE 2026-09-02T11:11:01.017269-04:00 share=25% ===
Live account equity $230.26 cash $195.72 #225458845 options_level=3
2026-09-02 11:11:01,116 INFO Live account equity $230.26 cash $195.72 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-02 11:11:01,204 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-02 11:11:01,258 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (192 earlier lines - see full log file)
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    3 |    2 |    7 |    1 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    26 |
| w2     |    6 |    5 |   11 |    5 |    6 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    47 |
| w3     |    7 |    6 |   13 |    4 |    7 |    5 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    53 |
| w4     |    5 |    3 |    9 |    2 |    4 |    4 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    36 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 223 | 9 |
| S164 | 243 | 10 |
| S165 | 1689 | 23 |
| S166 | 109 | 6 |
| S167 | 243 | 10 |
| S168 | 166 | 8 |
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
| 2026-09-02 |   10 |    8 |    8 |    2 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    46 |

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
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |   123 | INFO |
| Total closed lots           |  1804 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=851 med=-46.7% | TAINTED n=1766 med=-39.2% | KEEP-only n=348 med=+38.0% | KILL=17 KEEP=14
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.26 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260902T151603Z

- UTC timestamp: `20260902T151603Z`
- GitHub run: [#8815](https://github.com/28twagg-ops/TradingBot/actions/runs/33647315756)
- Run id: `33647315756`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`77s`
- Full logs: `logs/action_runs/20260902T151603Z_live_bot.log`, `logs/action_runs/20260902T151603Z_live_options.log`, `logs/action_runs/20260902T151603Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 851 | 43.0 | -46.7 | +16.7 | $+8,762 |
| TAINTED | 1766 | 33.1 | -39.2 | +12.2 | $-9,184 |
| KEEP-only | 348 | 62.6 | +38.0 | +42.3 | $+6,024 |
| KEEP-only recent | 160 | 58.8 | +51.1 | +49.5 | $+1,998 |

- KEEP strategies (14): S173, S174, S210, S218, S350, S362, S363, S364, S397, S398, S401, S404, S406, S412
- KILL strategies (17): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S352, S354, S355, S360, S399, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-02T11:16:09.194546-04:00","date":"2026-09-02","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":65.6,"phases_s":{"reconcile":0.1,"cancel":0.03,"manage":5.33,"protective_stops":0.51,"scan":54.9,"entries":3.46,"reconcile2":0.09},"signals":135,"placed":0,"equity":998899.41,"open_positions":26,"pending_orders":49,"open_lots":123,"submitted_today":158,"filled_today":109,"unattributed_contracts":0,"top_signals":["S165:SNOW","S164:SNOW","S168:SNOW","S167:SNOW","S163:SNOW","S218:SNOW","S350:SNOW","S351:SNOW"],"github_run":"8815","github_run_id":"33647315756","status":"ok","data_quality":{"clean":{"n":851,"win":43.01,"med":-46.67,"avg":16.7,"pnl":8761.53},"tainted":{"n":1766,"win":33.07,"med":-39.16,"avg":12.18,"pnl":-9184.34},"keep_only":{"n":348,"win":62.64,"med":37.96,"avg":42.31,"pnl":6024.45},"keep_only_recent":{"n":160,"win":58.75,"med":51.09,"avg":49.5,"pnl":1998.0},"keep_strategies":["S173","S174","S210","S218","S350","S362","S363","S364","S397","S398","S401","S404","S406","S412"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S352","S354","S355","S360","S399","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:16:04  INFO      Mode: exits
15:16:05  INFO        Daily log -> logs/daily/2026-09-02.md
15:16:05  INFO        Daily log reconciled -> logs/daily/2026-09-02.md (5 ledger rows)
15:16:05  INFO        place_all_stops: checking 1 positions...
15:16:05  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
15:16:05  INFO        [positions] 1/1 (1 valid)
15:16:05  INFO        Daily log -> logs/daily/2026-09-02.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.22|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMZN  P&L -0.2%  $-0.08                                           HOLD|
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
=== options_live_micro LIVE 2026-09-02T11:16:06.458753-04:00 share=25% ===
2026-09-02 11:16:06,458 INFO === options_live_micro LIVE 2026-09-02T11:16:06.458753-04:00 share=25% ===
Live account equity $230.22 cash $195.72 #225458845 options_level=3
2026-09-02 11:16:06,503 INFO Live account equity $230.22 cash $195.72 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-02 11:16:06,532 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-02 11:16:06,551 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (188 earlier lines - see full log file)
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    3 |    2 |    7 |    1 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    26 |
| w2     |    6 |    5 |   11 |    5 |    6 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    47 |
| w3     |    7 |    6 |   13 |    4 |    7 |    5 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    53 |
| w4     |    5 |    3 |    9 |    2 |    4 |    4 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    36 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 223 | 9 |
| S164 | 243 | 10 |
| S165 | 1689 | 23 |
| S166 | 109 | 6 |
| S167 | 243 | 10 |
| S168 | 166 | 8 |
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
| 2026-09-02 |   10 |    8 |    8 |    2 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    46 |

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
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |   123 | INFO |
| Total closed lots           |  1804 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=851 med=-46.7% | TAINTED n=1766 med=-39.2% | KEEP-only n=348 med=+38.0% | KILL=17 KEEP=14
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.22 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260902T152118Z

- UTC timestamp: `20260902T152118Z`
- GitHub run: [#8816](https://github.com/28twagg-ops/TradingBot/actions/runs/33647862540)
- Run id: `33647862540`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`84s`
- Full logs: `logs/action_runs/20260902T152118Z_live_bot.log`, `logs/action_runs/20260902T152118Z_live_options.log`, `logs/action_runs/20260902T152118Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 852 | 43.0 | -46.7 | +16.6 | $+8,744 |
| TAINTED | 1766 | 33.1 | -39.2 | +12.2 | $-9,184 |
| KEEP-only | 348 | 62.6 | +38.0 | +42.3 | $+6,024 |
| KEEP-only recent | 160 | 58.8 | +51.1 | +49.5 | $+1,998 |

- KEEP strategies (14): S173, S174, S210, S218, S350, S362, S363, S364, S397, S398, S401, S404, S406, S412
- KILL strategies (17): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S352, S354, S355, S360, S399, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-02T11:21:22.580902-04:00","date":"2026-09-02","mode":"entry+manage","header":"entry+manage (32 new)","elapsed_s":75.5,"phases_s":{"reconcile":0.16,"cancel":0.03,"manage":4.38,"protective_stops":0.57,"scan":35.03,"entries":15.73,"reconcile2":0.5},"signals":135,"placed":32,"equity":998891.35,"open_positions":29,"pending_orders":69,"open_lots":134,"submitted_today":190,"filled_today":121,"unattributed_contracts":0,"top_signals":["S165:SNOW","S164:SNOW","S168:SNOW","S167:SNOW","S163:SNOW","S218:SNOW","S350:SNOW","S351:SNOW"],"github_run":"8816","github_run_id":"33647862540","status":"ok","data_quality":{"clean":{"n":852,"win":42.96,"med":-46.67,"avg":16.59,"pnl":8743.53},"tainted":{"n":1766,"win":33.07,"med":-39.16,"avg":12.18,"pnl":-9184.34},"keep_only":{"n":348,"win":62.64,"med":37.96,"avg":42.31,"pnl":6024.45},"keep_only_recent":{"n":160,"win":58.75,"med":51.09,"avg":49.5,"pnl":1998.0},"keep_strategies":["S173","S174","S210","S218","S350","S362","S363","S364","S397","S398","S401","S404","S406","S412"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S352","S354","S355","S360","S399","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:21:19  INFO      Mode: exits
15:21:19  INFO        Daily log -> logs/daily/2026-09-02.md
15:21:19  INFO        Daily log reconciled -> logs/daily/2026-09-02.md (5 ledger rows)
15:21:19  INFO        place_all_stops: checking 1 positions...
15:21:19  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
15:21:19  INFO        [positions] 1/1 (1 valid)
15:21:19  INFO        Daily log -> logs/daily/2026-09-02.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.23|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMZN  P&L -0.2%  $-0.07                                           HOLD|
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
=== options_live_micro LIVE 2026-09-02T11:21:20.366582-04:00 share=25% ===
2026-09-02 11:21:20,366 INFO === options_live_micro LIVE 2026-09-02T11:21:20.366582-04:00 share=25% ===
Live account equity $230.24 cash $195.72 #225458845 options_level=3
2026-09-02 11:21:20,422 INFO Live account equity $230.24 cash $195.72 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-02 11:21:20,480 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-02 11:21:20,505 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (197 earlier lines - see full log file)
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    3 |    2 |    7 |    1 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    26 |
| w2     |    6 |    5 |   11 |    5 |    6 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    47 |
| w3     |    7 |    6 |   13 |    4 |    7 |    5 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    53 |
| w4     |    5 |    4 |   10 |    2 |    5 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    40 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 223 | 9 |
| S164 | 245 | 10 |
| S165 | 1691 | 23 |
| S166 | 109 | 6 |
| S167 | 245 | 10 |
| S168 | 170 | 8 |
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
| 2026-09-02 |   10 |   10 |   10 |    2 |   10 |   14 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    56 |

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
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |   134 | INFO |
| Total closed lots           |  1805 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=852 med=-46.7% | TAINTED n=1766 med=-39.2% | KEEP-only n=348 med=+38.0% | KILL=17 KEEP=14
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.23 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260902T152605Z

- UTC timestamp: `20260902T152605Z`
- GitHub run: [#8817](https://github.com/28twagg-ops/TradingBot/actions/runs/33648396130)
- Run id: `33648396130`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`102s`
- Full logs: `logs/action_runs/20260902T152605Z_live_bot.log`, `logs/action_runs/20260902T152605Z_live_options.log`, `logs/action_runs/20260902T152605Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 853 | 42.9 | -46.7 | +16.5 | $+8,728 |
| TAINTED | 1766 | 33.1 | -39.2 | +12.2 | $-9,184 |
| KEEP-only | 348 | 62.6 | +38.0 | +42.3 | $+6,024 |
| KEEP-only recent | 160 | 58.8 | +51.1 | +49.5 | $+1,998 |

- KEEP strategies (14): S173, S174, S210, S218, S350, S362, S363, S364, S397, S398, S401, S404, S406, S412
- KILL strategies (17): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S352, S354, S355, S360, S399, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-02T11:26:14.591024-04:00","date":"2026-09-02","mode":"entry+manage","header":"entry+manage (2 new)","elapsed_s":90.6,"phases_s":{"reconcile":0.45,"cancel":0.15,"manage":10.07,"protective_stops":4.26,"scan":54.76,"entries":15.77,"reconcile2":0.45},"signals":135,"placed":2,"equity":998816.03,"open_positions":28,"pending_orders":71,"open_lots":133,"submitted_today":192,"filled_today":121,"unattributed_contracts":0,"top_signals":["S165:SNOW","S164:SNOW","S168:SNOW","S167:SNOW","S163:SNOW","S218:SNOW","S350:SNOW","S351:SNOW"],"github_run":"8817","github_run_id":"33648396130","status":"ok","data_quality":{"clean":{"n":853,"win":42.91,"med":-46.67,"avg":16.49,"pnl":8727.53},"tainted":{"n":1766,"win":33.07,"med":-39.16,"avg":12.18,"pnl":-9184.34},"keep_only":{"n":348,"win":62.64,"med":37.96,"avg":42.31,"pnl":6024.45},"keep_only_recent":{"n":160,"win":58.75,"med":51.09,"avg":49.5,"pnl":1998.0},"keep_strategies":["S173","S174","S210","S218","S350","S362","S363","S364","S397","S398","S401","S404","S406","S412"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S352","S354","S355","S360","S399","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:26:07  INFO      Mode: exits
15:26:08  INFO        Daily log -> logs/daily/2026-09-02.md
15:26:08  INFO        Daily log reconciled -> logs/daily/2026-09-02.md (5 ledger rows)
15:26:08  INFO        place_all_stops: checking 1 positions...
15:26:08  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
15:26:08  INFO        [positions] 1/1 (1 valid)
15:26:09  INFO        Daily log -> logs/daily/2026-09-02.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:26 UTC|
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
=== options_live_micro LIVE 2026-09-02T11:26:10.758035-04:00 share=25% ===
2026-09-02 11:26:10,758 INFO === options_live_micro LIVE 2026-09-02T11:26:10.758035-04:00 share=25% ===
Live account equity $230.25 cash $195.72 #225458845 options_level=3
2026-09-02 11:26:10,982 INFO Live account equity $230.25 cash $195.72 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-02 11:26:11,198 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-02 11:26:11,341 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (189 earlier lines - see full log file)
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    3 |    2 |    7 |    1 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    26 |
| w2     |    6 |    5 |   11 |    5 |    6 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    47 |
| w3     |    7 |    6 |   13 |    4 |    7 |    5 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    53 |
| w4     |    5 |    4 |   10 |    2 |    5 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    40 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 223 | 9 |
| S164 | 245 | 10 |
| S165 | 1691 | 23 |
| S166 | 109 | 6 |
| S167 | 245 | 10 |
| S168 | 170 | 8 |
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
| 2026-09-02 |   10 |   10 |   10 |    2 |   10 |   14 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    56 |

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
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |   133 | INFO |
| Total closed lots           |  1806 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=853 med=-46.7% | TAINTED n=1766 med=-39.2% | KEEP-only n=348 med=+38.0% | KILL=17 KEEP=14
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.25 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260902T153109Z

- UTC timestamp: `20260902T153109Z`
- GitHub run: [#8818](https://github.com/28twagg-ops/TradingBot/actions/runs/33648937220)
- Run id: `33648937220`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`3s`
- Paper options: exit=`0`, duration=`75s`
- Full logs: `logs/action_runs/20260902T153109Z_live_bot.log`, `logs/action_runs/20260902T153109Z_live_options.log`, `logs/action_runs/20260902T153109Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 853 | 42.9 | -46.7 | +16.5 | $+8,728 |
| TAINTED | 1766 | 33.1 | -39.2 | +12.2 | $-9,184 |
| KEEP-only | 348 | 62.6 | +38.0 | +42.3 | $+6,024 |
| KEEP-only recent | 160 | 58.8 | +51.1 | +49.5 | $+1,998 |

- KEEP strategies (14): S173, S174, S210, S218, S350, S362, S363, S364, S397, S398, S401, S404, S406, S412
- KILL strategies (17): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S352, S354, S355, S360, S399, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-02T11:31:18.369358-04:00","date":"2026-09-02","mode":"entry+manage","header":"entry+manage (9 new)","elapsed_s":64.0,"phases_s":{"reconcile":0.1,"cancel":0.03,"manage":5.27,"protective_stops":0.59,"scan":52.72,"entries":3.77,"reconcile2":0.34},"signals":135,"placed":9,"equity":998786.01,"open_positions":30,"pending_orders":75,"open_lots":138,"submitted_today":201,"filled_today":126,"unattributed_contracts":0,"top_signals":["S165:SNOW","S164:SNOW","S168:SNOW","S167:SNOW","S163:SNOW","S218:SNOW","S350:SNOW","S351:SNOW"],"github_run":"8818","github_run_id":"33648937220","status":"ok","data_quality":{"clean":{"n":853,"win":42.91,"med":-46.67,"avg":16.49,"pnl":8727.53},"tainted":{"n":1766,"win":33.07,"med":-39.16,"avg":12.18,"pnl":-9184.34},"keep_only":{"n":348,"win":62.64,"med":37.96,"avg":42.31,"pnl":6024.45},"keep_only_recent":{"n":160,"win":58.75,"med":51.09,"avg":49.5,"pnl":1998.0},"keep_strategies":["S173","S174","S210","S218","S350","S362","S363","S364","S397","S398","S401","S404","S406","S412"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S352","S354","S355","S360","S399","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:31:11  INFO      Mode: exits
15:31:12  INFO        Daily log -> logs/daily/2026-09-02.md
15:31:12  INFO        Daily log reconciled -> logs/daily/2026-09-02.md (5 ledger rows)
15:31:12  INFO        place_all_stops: checking 1 positions...
15:31:12  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
15:31:12  INFO        [positions] 1/1 (1 valid)
15:31:12  INFO        Daily log -> logs/daily/2026-09-02.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.28|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMZN  P&L -0.1%  $-0.02                                           HOLD|
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
=== options_live_micro LIVE 2026-09-02T11:31:13.394256-04:00 share=25% ===
2026-09-02 11:31:13,394 INFO === options_live_micro LIVE 2026-09-02T11:31:13.394256-04:00 share=25% ===
Live account equity $230.28 cash $195.72 #225458845 options_level=3
2026-09-02 11:31:15,664 INFO Live account equity $230.28 cash $195.72 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-02 11:31:15,693 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-02 11:31:15,722 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (186 earlier lines - see full log file)
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    3 |    2 |    7 |    1 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    26 |
| w2     |    6 |    5 |   11 |    5 |    6 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    47 |
| w3     |    7 |    6 |   13 |    4 |    7 |    5 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    53 |
| w4     |    5 |    4 |   10 |    2 |    5 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    40 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 223 | 9 |
| S164 | 245 | 10 |
| S165 | 1691 | 23 |
| S166 | 109 | 6 |
| S167 | 245 | 10 |
| S168 | 170 | 8 |
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
| 2026-09-02 |   10 |   10 |   10 |    2 |   10 |   14 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    56 |

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
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |   138 | INFO |
| Total closed lots           |  1806 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=853 med=-46.7% | TAINTED n=1766 med=-39.2% | KEEP-only n=348 med=+38.0% | KILL=17 KEEP=14
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.28 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260902T153644Z

- UTC timestamp: `20260902T153644Z`
- GitHub run: [#8819](https://github.com/28twagg-ops/TradingBot/actions/runs/33649487268)
- Run id: `33649487268`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`28s`
- Full logs: `logs/action_runs/20260902T153644Z_live_bot.log`, `logs/action_runs/20260902T153644Z_live_options.log`, `logs/action_runs/20260902T153644Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 853 | 42.9 | -46.7 | +16.5 | $+8,728 |
| TAINTED | 1766 | 33.1 | -39.2 | +12.2 | $-9,184 |
| KEEP-only | 348 | 62.6 | +38.0 | +42.3 | $+6,024 |
| KEEP-only recent | 160 | 58.8 | +51.1 | +49.5 | $+1,998 |

- KEEP strategies (14): S173, S174, S210, S218, S350, S362, S363, S364, S397, S398, S401, S404, S406, S412
- KILL strategies (17): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S352, S354, S355, S360, S399, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-02T11:36:51.247237-04:00","date":"2026-09-02","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":17.4,"phases_s":{"reconcile":0.42,"cancel":4.47,"manage":9.01,"protective_stops":2.82},"signals":0,"placed":0,"equity":998756.8,"open_positions":31,"pending_orders":73,"open_lots":140,"submitted_today":201,"filled_today":128,"unattributed_contracts":0,"top_signals":[],"github_run":"8819","github_run_id":"33649487268","status":"ok","data_quality":{"clean":{"n":853,"win":42.91,"med":-46.67,"avg":16.49,"pnl":8727.53},"tainted":{"n":1766,"win":33.07,"med":-39.16,"avg":12.18,"pnl":-9184.34},"keep_only":{"n":348,"win":62.64,"med":37.96,"avg":42.31,"pnl":6024.45},"keep_only_recent":{"n":160,"win":58.75,"med":51.09,"avg":49.5,"pnl":1998.0},"keep_strategies":["S173","S174","S210","S218","S350","S362","S363","S364","S397","S398","S401","S404","S406","S412"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S352","S354","S355","S360","S399","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:36:45  INFO      Mode: exits
15:36:46  INFO        Daily log -> logs/daily/2026-09-02.md
15:36:46  INFO        Daily log reconciled -> logs/daily/2026-09-02.md (5 ledger rows)
15:36:46  INFO        place_all_stops: checking 1 positions...
15:36:46  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
15:36:46  INFO        [positions] 1/1 (1 valid)
15:36:47  INFO        Daily log -> logs/daily/2026-09-02.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:36 UTC|
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
=== options_live_micro LIVE 2026-09-02T11:36:47.790336-04:00 share=25% ===
2026-09-02 11:36:47,790 INFO === options_live_micro LIVE 2026-09-02T11:36:47.790336-04:00 share=25% ===
Live account equity $230.29 cash $195.72 #225458845 options_level=3
2026-09-02 11:36:48,006 INFO Live account equity $230.29 cash $195.72 #225458845 options_level=3
Live micro: manage/exits only
2026-09-02 11:36:48,178 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-02 11:36:48,236 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (175 earlier lines - see full log file)
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    3 |    2 |    7 |    1 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    26 |
| w2     |    6 |    5 |   11 |    5 |    6 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    47 |
| w3     |    7 |    6 |   13 |    4 |    7 |    5 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    53 |
| w4     |    5 |    4 |   10 |    2 |    5 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    40 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 223 | 9 |
| S164 | 245 | 10 |
| S165 | 1691 | 23 |
| S166 | 109 | 6 |
| S167 | 245 | 10 |
| S168 | 170 | 8 |
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
| 2026-09-02 |   10 |   10 |   10 |    2 |   10 |   14 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    56 |

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
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |   140 | INFO |
| Total closed lots           |  1806 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=853 med=-46.7% | TAINTED n=1766 med=-39.2% | KEEP-only n=348 med=+38.0% | KILL=17 KEEP=14
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.29 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260902T154059Z

- UTC timestamp: `20260902T154059Z`
- GitHub run: [#8820](https://github.com/28twagg-ops/TradingBot/actions/runs/33650026606)
- Run id: `33650026606`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`26s`
- Full logs: `logs/action_runs/20260902T154059Z_live_bot.log`, `logs/action_runs/20260902T154059Z_live_options.log`, `logs/action_runs/20260902T154059Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 853 | 42.9 | -46.7 | +16.5 | $+8,728 |
| TAINTED | 1766 | 33.1 | -39.2 | +12.2 | $-9,184 |
| KEEP-only | 348 | 62.6 | +38.0 | +42.3 | $+6,024 |
| KEEP-only recent | 160 | 58.8 | +51.1 | +49.5 | $+1,998 |

- KEEP strategies (14): S173, S174, S210, S218, S350, S362, S363, S364, S397, S398, S401, S404, S406, S412
- KILL strategies (17): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S352, S354, S355, S360, S399, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-02T11:41:07.718593-04:00","date":"2026-09-02","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":14.2,"phases_s":{"reconcile":0.5,"cancel":0.22,"manage":9.91,"protective_stops":2.74},"signals":0,"placed":0,"equity":998727.8,"open_positions":31,"pending_orders":0,"open_lots":140,"submitted_today":201,"filled_today":128,"unattributed_contracts":0,"top_signals":[],"github_run":"8820","github_run_id":"33650026606","status":"ok","data_quality":{"clean":{"n":853,"win":42.91,"med":-46.67,"avg":16.49,"pnl":8727.53},"tainted":{"n":1766,"win":33.07,"med":-39.16,"avg":12.18,"pnl":-9184.34},"keep_only":{"n":348,"win":62.64,"med":37.96,"avg":42.31,"pnl":6024.45},"keep_only_recent":{"n":160,"win":58.75,"med":51.09,"avg":49.5,"pnl":1998.0},"keep_strategies":["S173","S174","S210","S218","S350","S362","S363","S364","S397","S398","S401","S404","S406","S412"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S352","S354","S355","S360","S399","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:41:01  INFO      Mode: exits
15:41:01  INFO        Daily log -> logs/daily/2026-09-02.md
15:41:01  INFO        Daily log reconciled -> logs/daily/2026-09-02.md (5 ledger rows)
15:41:02  INFO        place_all_stops: checking 1 positions...
15:41:02  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
15:41:02  INFO        [positions] 1/1 (1 valid)
15:41:02  INFO        Daily log -> logs/daily/2026-09-02.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.24|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMZN  P&L -0.2%  $-0.07                                           HOLD|
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
=== options_live_micro LIVE 2026-09-02T11:41:03.463323-04:00 share=25% ===
2026-09-02 11:41:03,463 INFO === options_live_micro LIVE 2026-09-02T11:41:03.463323-04:00 share=25% ===
Live account equity $230.23 cash $195.72 #225458845 options_level=3
2026-09-02 11:41:03,910 INFO Live account equity $230.23 cash $195.72 #225458845 options_level=3
Live micro: manage/exits only
2026-09-02 11:41:04,121 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-02 11:41:04,195 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (162 earlier lines - see full log file)
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    3 |    2 |    7 |    1 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    26 |
| w2     |    6 |    5 |   11 |    5 |    6 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    47 |
| w3     |    7 |    6 |   13 |    4 |    7 |    5 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    53 |
| w4     |    5 |    4 |   10 |    2 |    5 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    40 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 223 | 9 |
| S164 | 245 | 10 |
| S165 | 1691 | 23 |
| S166 | 109 | 6 |
| S167 | 245 | 10 |
| S168 | 170 | 8 |
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
| 2026-09-02 |   10 |   10 |   10 |    2 |   10 |   14 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    56 |

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
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |   140 | INFO |
| Total closed lots           |  1806 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=853 med=-46.7% | TAINTED n=1766 med=-39.2% | KEEP-only n=348 med=+38.0% | KILL=17 KEEP=14
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.23 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260902T154608Z

- UTC timestamp: `20260902T154608Z`
- GitHub run: [#8821](https://github.com/28twagg-ops/TradingBot/actions/runs/33650565845)
- Run id: `33650565845`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`17s`
- Full logs: `logs/action_runs/20260902T154608Z_live_bot.log`, `logs/action_runs/20260902T154608Z_live_options.log`, `logs/action_runs/20260902T154608Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 853 | 42.9 | -46.7 | +16.5 | $+8,728 |
| TAINTED | 1766 | 33.1 | -39.2 | +12.2 | $-9,184 |
| KEEP-only | 348 | 62.6 | +38.0 | +42.3 | $+6,024 |
| KEEP-only recent | 160 | 58.8 | +51.1 | +49.5 | $+1,998 |

- KEEP strategies (14): S173, S174, S210, S218, S350, S362, S363, S364, S397, S398, S401, S404, S406, S412
- KILL strategies (17): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S352, S354, S355, S360, S399, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-02T11:46:13.610861-04:00","date":"2026-09-02","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":8.3,"phases_s":{"reconcile":0.25,"cancel":0.07,"manage":6.31,"protective_stops":1.13},"signals":0,"placed":0,"equity":998677.8,"open_positions":31,"pending_orders":0,"open_lots":140,"submitted_today":201,"filled_today":128,"unattributed_contracts":0,"top_signals":[],"github_run":"8821","github_run_id":"33650565845","status":"ok","data_quality":{"clean":{"n":853,"win":42.91,"med":-46.67,"avg":16.49,"pnl":8727.53},"tainted":{"n":1766,"win":33.07,"med":-39.16,"avg":12.18,"pnl":-9184.34},"keep_only":{"n":348,"win":62.64,"med":37.96,"avg":42.31,"pnl":6024.45},"keep_only_recent":{"n":160,"win":58.75,"med":51.09,"avg":49.5,"pnl":1998.0},"keep_strategies":["S173","S174","S210","S218","S350","S362","S363","S364","S397","S398","S401","S404","S406","S412"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S352","S354","S355","S360","S399","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:46:10  INFO      Mode: exits
15:46:10  INFO        Daily log -> logs/daily/2026-09-02.md
15:46:10  INFO        Daily log reconciled -> logs/daily/2026-09-02.md (5 ledger rows)
15:46:10  INFO        place_all_stops: checking 1 positions...
15:46:10  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
15:46:10  INFO        [positions] 1/1 (1 valid)
15:46:10  INFO        Daily log -> logs/daily/2026-09-02.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.17|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMZN  P&L -0.4%  $-0.13                                           HOLD|
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
=== options_live_micro LIVE 2026-09-02T11:46:11.243521-04:00 share=25% ===
2026-09-02 11:46:11,243 INFO === options_live_micro LIVE 2026-09-02T11:46:11.243521-04:00 share=25% ===
Live account equity $230.18 cash $195.72 #225458845 options_level=3
2026-09-02 11:46:11,334 INFO Live account equity $230.18 cash $195.72 #225458845 options_level=3
Live micro: manage/exits only
2026-09-02 11:46:11,411 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-02 11:46:11,432 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (168 earlier lines - see full log file)
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    3 |    2 |    7 |    1 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    26 |
| w2     |    6 |    5 |   11 |    5 |    6 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    47 |
| w3     |    7 |    6 |   13 |    4 |    7 |    5 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    53 |
| w4     |    5 |    4 |   10 |    2 |    5 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    40 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 223 | 9 |
| S164 | 245 | 10 |
| S165 | 1691 | 23 |
| S166 | 109 | 6 |
| S167 | 245 | 10 |
| S168 | 170 | 8 |
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
| 2026-09-02 |   10 |   10 |   10 |    2 |   10 |   14 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    56 |

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
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |   140 | INFO |
| Total closed lots           |  1806 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=853 med=-46.7% | TAINTED n=1766 med=-39.2% | KEEP-only n=348 med=+38.0% | KILL=17 KEEP=14
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.17 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260902T155106Z

- UTC timestamp: `20260902T155106Z`
- GitHub run: [#8822](https://github.com/28twagg-ops/TradingBot/actions/runs/33651102838)
- Run id: `33651102838`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`19s`
- Full logs: `logs/action_runs/20260902T155106Z_live_bot.log`, `logs/action_runs/20260902T155106Z_live_options.log`, `logs/action_runs/20260902T155106Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 854 | 42.9 | -46.7 | +16.4 | $+8,717 |
| TAINTED | 1766 | 33.1 | -39.2 | +12.2 | $-9,184 |
| KEEP-only | 349 | 62.5 | +37.7 | +42.0 | $+6,013 |
| KEEP-only recent | 161 | 58.4 | +50.0 | +48.8 | $+1,987 |

- KEEP strategies (14): S173, S174, S210, S218, S350, S362, S363, S364, S397, S398, S401, S404, S406, S412
- KILL strategies (17): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S352, S354, S355, S360, S399, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-02T11:51:12.053213-04:00","date":"2026-09-02","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":7.6,"phases_s":{"reconcile":0.2,"cancel":0.04,"manage":6.37,"protective_stops":0.41},"signals":0,"placed":0,"equity":998681.78,"open_positions":31,"pending_orders":0,"open_lots":139,"submitted_today":201,"filled_today":128,"unattributed_contracts":0,"top_signals":[],"github_run":"8822","github_run_id":"33651102838","status":"ok","data_quality":{"clean":{"n":854,"win":42.86,"med":-46.67,"avg":16.39,"pnl":8716.53},"tainted":{"n":1766,"win":33.07,"med":-39.16,"avg":12.18,"pnl":-9184.34},"keep_only":{"n":349,"win":62.46,"med":37.69,"avg":42.0,"pnl":6013.45},"keep_only_recent":{"n":161,"win":58.39,"med":50.0,"avg":48.79,"pnl":1987.0},"keep_strategies":["S173","S174","S210","S218","S350","S362","S363","S364","S397","S398","S401","S404","S406","S412"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S352","S354","S355","S360","S399","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:51:07  INFO      Mode: exits
15:51:07  INFO        Daily log -> logs/daily/2026-09-02.md
15:51:07  INFO        Daily log reconciled -> logs/daily/2026-09-02.md (5 ledger rows)
15:51:07  INFO        place_all_stops: checking 1 positions...
15:51:07  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
15:51:07  INFO        [positions] 1/1 (1 valid)
15:51:07  INFO        Daily log -> logs/daily/2026-09-02.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:51 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.18|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMZN  P&L -0.4%  $-0.12                                           HOLD|
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
=== options_live_micro LIVE 2026-09-02T11:51:08.433857-04:00 share=25% ===
2026-09-02 11:51:08,433 INFO === options_live_micro LIVE 2026-09-02T11:51:08.433857-04:00 share=25% ===
Live account equity $230.18 cash $195.72 #225458845 options_level=3
2026-09-02 11:51:08,477 INFO Live account equity $230.18 cash $195.72 #225458845 options_level=3
Live micro: manage/exits only
2026-09-02 11:51:08,503 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-02 11:51:08,511 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (170 earlier lines - see full log file)
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    3 |    2 |    7 |    1 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    26 |
| w2     |    6 |    5 |   11 |    5 |    6 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    47 |
| w3     |    7 |    6 |   13 |    4 |    7 |    5 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    53 |
| w4     |    5 |    4 |   10 |    2 |    5 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    40 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 223 | 9 |
| S164 | 245 | 10 |
| S165 | 1691 | 23 |
| S166 | 109 | 6 |
| S167 | 245 | 10 |
| S168 | 170 | 8 |
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
| 2026-09-02 |   10 |   10 |   10 |    2 |   10 |   14 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    56 |

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
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |   139 | INFO |
| Total closed lots           |  1807 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=854 med=-46.7% | TAINTED n=1766 med=-39.2% | KEEP-only n=349 med=+37.7% | KILL=17 KEEP=14
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.18 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260902T160101Z

- UTC timestamp: `20260902T160101Z`
- GitHub run: [#8824](https://github.com/28twagg-ops/TradingBot/actions/runs/33652154615)
- Run id: `33652154615`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`25s`
- Full logs: `logs/action_runs/20260902T160101Z_live_bot.log`, `logs/action_runs/20260902T160101Z_live_options.log`, `logs/action_runs/20260902T160101Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 854 | 42.9 | -46.7 | +16.4 | $+8,717 |
| TAINTED | 1766 | 33.1 | -39.2 | +12.2 | $-9,184 |
| KEEP-only | 349 | 62.5 | +37.7 | +42.0 | $+6,013 |
| KEEP-only recent | 161 | 58.4 | +50.0 | +48.8 | $+1,987 |

- KEEP strategies (14): S173, S174, S210, S218, S350, S362, S363, S364, S397, S398, S401, S404, S406, S412
- KILL strategies (17): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S352, S354, S355, S360, S399, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-02T12:01:08.361475-04:00","date":"2026-09-02","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":13.1,"phases_s":{"reconcile":0.34,"cancel":0.18,"manage":9.25,"protective_stops":2.63},"signals":0,"placed":0,"equity":998892.78,"open_positions":31,"pending_orders":0,"open_lots":139,"submitted_today":201,"filled_today":128,"unattributed_contracts":0,"top_signals":[],"github_run":"8824","github_run_id":"33652154615","status":"ok","data_quality":{"clean":{"n":854,"win":42.86,"med":-46.67,"avg":16.39,"pnl":8716.53},"tainted":{"n":1766,"win":33.07,"med":-39.16,"avg":12.18,"pnl":-9184.34},"keep_only":{"n":349,"win":62.46,"med":37.69,"avg":42.0,"pnl":6013.45},"keep_only_recent":{"n":161,"win":58.39,"med":50.0,"avg":48.79,"pnl":1987.0},"keep_strategies":["S173","S174","S210","S218","S350","S362","S363","S364","S397","S398","S401","S404","S406","S412"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S352","S354","S355","S360","S399","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
16:01:02  INFO      Mode: exits
16:01:03  INFO        Daily log -> logs/daily/2026-09-02.md
16:01:03  INFO        Daily log reconciled -> logs/daily/2026-09-02.md (5 ledger rows)
16:01:03  INFO        place_all_stops: checking 1 positions...
16:01:03  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
16:01:03  INFO        [positions] 1/1 (1 valid)
16:01:03  INFO        Daily log -> logs/daily/2026-09-02.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.24|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMZN  P&L -0.2%  $-0.06                                           HOLD|
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
=== options_live_micro LIVE 2026-09-02T12:01:04.683558-04:00 share=25% ===
2026-09-02 12:01:04,683 INFO === options_live_micro LIVE 2026-09-02T12:01:04.683558-04:00 share=25% ===
Live account equity $230.24 cash $195.72 #225458845 options_level=3
2026-09-02 12:01:04,882 INFO Live account equity $230.24 cash $195.72 #225458845 options_level=3
Live micro: manage/exits only
2026-09-02 12:01:05,056 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-02 12:01:05,123 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (172 earlier lines - see full log file)
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    3 |    2 |    7 |    1 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    26 |
| w2     |    6 |    5 |   11 |    5 |    6 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    47 |
| w3     |    7 |    6 |   13 |    4 |    7 |    5 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    53 |
| w4     |    5 |    4 |   10 |    2 |    5 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    40 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 223 | 9 |
| S164 | 245 | 10 |
| S165 | 1691 | 23 |
| S166 | 109 | 6 |
| S167 | 245 | 10 |
| S168 | 170 | 8 |
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
| 2026-09-02 |   10 |   10 |   10 |    2 |   10 |   14 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    56 |

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
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |   139 | INFO |
| Total closed lots           |  1807 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=854 med=-46.7% | TAINTED n=1766 med=-39.2% | KEEP-only n=349 med=+37.7% | KILL=17 KEEP=14
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.24 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260902T160558Z

- UTC timestamp: `20260902T160558Z`
- GitHub run: [#8825](https://github.com/28twagg-ops/TradingBot/actions/runs/33652689646)
- Run id: `33652689646`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`18s`
- Full logs: `logs/action_runs/20260902T160558Z_live_bot.log`, `logs/action_runs/20260902T160558Z_live_options.log`, `logs/action_runs/20260902T160558Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 857 | 42.7 | -46.7 | +16.2 | $+8,670 |
| TAINTED | 1766 | 33.1 | -39.2 | +12.2 | $-9,184 |
| KEEP-only | 351 | 62.1 | +37.7 | +41.5 | $+5,998 |
| KEEP-only recent | 163 | 57.7 | +50.0 | +47.6 | $+1,972 |

- KEEP strategies (14): S173, S174, S210, S218, S350, S362, S363, S364, S397, S398, S401, S404, S406, S412
- KILL strategies (17): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S352, S354, S355, S360, S399, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-02T12:06:03.464451-04:00","date":"2026-09-02","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":6.7,"phases_s":{"reconcile":0.23,"cancel":0.03,"manage":5.57,"protective_stops":0.38},"signals":0,"placed":0,"equity":998878.72,"open_positions":30,"pending_orders":0,"open_lots":136,"submitted_today":201,"filled_today":128,"unattributed_contracts":0,"top_signals":[],"github_run":"8825","github_run_id":"33652689646","status":"ok","data_quality":{"clean":{"n":857,"win":42.71,"med":-46.67,"avg":16.17,"pnl":8669.53},"tainted":{"n":1766,"win":33.07,"med":-39.16,"avg":12.18,"pnl":-9184.34},"keep_only":{"n":351,"win":62.11,"med":37.69,"avg":41.5,"pnl":5998.45},"keep_only_recent":{"n":163,"win":57.67,"med":50.0,"avg":47.63,"pnl":1972.0},"keep_strategies":["S173","S174","S210","S218","S350","S362","S363","S364","S397","S398","S401","S404","S406","S412"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S352","S354","S355","S360","S399","S403","S405","S407","S408"]}}
```

### Live bot (tail)

```text
16:05:59  INFO      Mode: exits
16:05:59  INFO        Daily log -> logs/daily/2026-09-02.md
16:05:59  INFO        Daily log reconciled -> logs/daily/2026-09-02.md (5 ledger rows)
16:05:59  INFO        place_all_stops: checking 1 positions...
16:05:59  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
16:05:59  INFO        [positions] 1/1 (1 valid)
16:05:59  INFO        Daily log -> logs/daily/2026-09-02.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:05 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.22|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMZN  P&L -0.2%  $-0.08                                           HOLD|
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
=== options_live_micro LIVE 2026-09-02T12:06:00.518463-04:00 share=25% ===
2026-09-02 12:06:00,518 INFO === options_live_micro LIVE 2026-09-02T12:06:00.518463-04:00 share=25% ===
Live account equity $230.22 cash $195.72 #225458845 options_level=3
2026-09-02 12:06:00,558 INFO Live account equity $230.22 cash $195.72 #225458845 options_level=3
Live micro: manage/exits only
2026-09-02 12:06:00,580 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-02 12:06:00,587 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (173 earlier lines - see full log file)
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    3 |    2 |    7 |    1 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    26 |
| w2     |    6 |    5 |   11 |    5 |    6 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    47 |
| w3     |    7 |    6 |   13 |    4 |    7 |    5 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    53 |
| w4     |    5 |    4 |   10 |    2 |    5 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    40 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 223 | 9 |
| S164 | 245 | 10 |
| S165 | 1691 | 23 |
| S166 | 109 | 6 |
| S167 | 245 | 10 |
| S168 | 170 | 8 |
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
| 2026-09-02 |   10 |   10 |   10 |    2 |   10 |   14 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    56 |

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
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |   136 | INFO |
| Total closed lots           |  1810 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-02_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=857 med=-46.7% | TAINTED n=1766 med=-39.2% | KEEP-only n=351 med=+37.7% | KILL=17 KEEP=14
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.22 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---
