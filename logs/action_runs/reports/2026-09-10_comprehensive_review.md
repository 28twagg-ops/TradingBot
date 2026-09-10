# Daily Comprehensive Action Review - 2026-09-10

_Auto-generated from GitHub Actions run output. Each run appends a summary; full stdout is in linked per-run log files._
## Run 20260910T130109Z

- UTC timestamp: `20260910T130109Z`
- GitHub run: [#9580](https://github.com/28twagg-ops/TradingBot/actions/runs/34479945062)
- Run id: `34479945062`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`15s`
- Full logs: `logs/action_runs/20260910T130109Z_live_bot.log`, `logs/action_runs/20260910T130109Z_live_options.log`, `logs/action_runs/20260910T130109Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1124 | 50.0 | +2.4 | +44.1 | $+15,928 |
| TAINTED | 1805 | 33.6 | -38.4 | +12.5 | $-8,747 |
| KEEP-only | 639 | 63.4 | +51.4 | +70.5 | $+11,196 |
| KEEP-only recent | 431 | 60.6 | +53.3 | +82.2 | $+5,939 |

- KEEP strategies (25): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S359, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T09:01:17.969947-04:00","date":"2026-09-10","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.5,"phases_s":{"reconcile":0.47},"signals":0,"placed":0,"equity":1003474.53,"open_positions":15,"pending_orders":0,"open_lots":46,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9580","github_run_id":"34479945062","status":"ok","data_quality":{"clean":{"n":1124,"win":50.0,"med":2.38,"avg":44.07,"pnl":15927.59},"tainted":{"n":1805,"win":33.57,"med":-38.36,"avg":12.49,"pnl":-8746.84},"keep_only":{"n":639,"win":63.38,"med":51.39,"avg":70.55,"pnl":11196.45},"keep_only_recent":{"n":431,"win":60.56,"med":53.33,"avg":82.23,"pnl":5939.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S359","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:01:12  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.71|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $227.71|
|  Cash                                                           $125.88|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $101.83|
|  Open P&L                                                        $-1.10|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (3 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CNM      MomReversal     $33.71     $41.73   $41.00   -1.8%   $-0.60  |
|  FSLR     MomReversal     $33.60     $203.22  $199.00  -2.1%   $-0.71  |
|  TXT      MomReversal     $34.52     $80.00   $80.50   +0.6%   $+0.21  |
|                                                                        |
|  Total invested                                                 $101.83|
|  Total open P&L                                                  $-1.10|
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
|  2026-09-09  SELL  BAX  Pullback50  $9.45  P&L $-0.05                  |
|  2026-09-09  SELL  AAPL  Pullback50  $34.40  P&L $+0.04                |
|  2026-09-09  SELL  C  Pullback50  $34.30  P&L $-0.03                   |
|  2026-09-09  SELL  MKSI  MomReversal  $34.18  P&L $-0.31               |
|  2026-09-09  SELL  MGM  MomReversal  $34.07  P&L $-0.42                |
|  2026-09-08  SELL  AMCR  Pullback50  $34.40  P&L $-0.19                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-10T09:01:14.157100-04:00 share=25% ===
2026-09-10 09:01:14,157 INFO === options_live_micro LIVE 2026-09-10T09:01:14.157100-04:00 share=25% ===
Live account equity $227.71 cash $125.88 #225458845 options_level=3
2026-09-10 09:01:14,364 INFO Live account equity $227.71 cash $125.88 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-10 09:01:14,422 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-10 09:01:14,480 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (159 earlier lines - see full log file)
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 249 | 13 |
| S164 | 271 | 15 |
| S165 | 1711 | 28 |
| S166 | 135 | 9 |
| S167 | 265 | 15 |
| S168 | 198 | 13 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1202 | WARN | <<<
| Missing exit records (post) |  1187 | WARN | <<<
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |    46 | INFO |
| Total closed lots           |  2102 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1124 med=+2.4% | TAINTED n=1805 med=-38.4% | KEEP-only n=639 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.71 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T130602Z

- UTC timestamp: `20260910T130602Z`
- GitHub run: [#9581](https://github.com/28twagg-ops/TradingBot/actions/runs/34480448491)
- Run id: `34480448491`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`12s`
- Full logs: `logs/action_runs/20260910T130602Z_live_bot.log`, `logs/action_runs/20260910T130602Z_live_options.log`, `logs/action_runs/20260910T130602Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1124 | 50.0 | +2.4 | +44.1 | $+15,928 |
| TAINTED | 1805 | 33.6 | -38.4 | +12.5 | $-8,747 |
| KEEP-only | 639 | 63.4 | +51.4 | +70.5 | $+11,196 |
| KEEP-only recent | 431 | 60.6 | +53.3 | +82.2 | $+5,939 |

- KEEP strategies (25): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S359, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T09:06:07.616483-04:00","date":"2026-09-10","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.09},"signals":0,"placed":0,"equity":1003456.53,"open_positions":15,"pending_orders":0,"open_lots":46,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9581","github_run_id":"34480448491","status":"ok","data_quality":{"clean":{"n":1124,"win":50.0,"med":2.38,"avg":44.07,"pnl":15927.59},"tainted":{"n":1805,"win":33.57,"med":-38.36,"avg":12.49,"pnl":-8746.84},"keep_only":{"n":639,"win":63.38,"med":51.39,"avg":70.55,"pnl":11196.45},"keep_only_recent":{"n":431,"win":60.56,"med":53.33,"avg":82.23,"pnl":5939.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S359","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:06:03  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.82|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $227.82|
|  Cash                                                           $125.88|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $101.94|
|  Open P&L                                                        $-0.99|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (3 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CNM      MomReversal     $33.71     $41.73   $41.00   -1.8%   $-0.60  |
|  FSLR     MomReversal     $33.71     $203.22  $199.68  -1.7%   $-0.60  |
|  TXT      MomReversal     $34.52     $80.00   $80.50   +0.6%   $+0.21  |
|                                                                        |
|  Total invested                                                 $101.94|
|  Total open P&L                                                  $-0.99|
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
|  2026-09-09  SELL  BAX  Pullback50  $9.45  P&L $-0.05                  |
|  2026-09-09  SELL  AAPL  Pullback50  $34.40  P&L $+0.04                |
|  2026-09-09  SELL  C  Pullback50  $34.30  P&L $-0.03                   |
|  2026-09-09  SELL  MKSI  MomReversal  $34.18  P&L $-0.31               |
|  2026-09-09  SELL  MGM  MomReversal  $34.07  P&L $-0.42                |
|  2026-09-08  SELL  AMCR  Pullback50  $34.40  P&L $-0.19                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-10T09:06:04.915858-04:00 share=25% ===
2026-09-10 09:06:04,915 INFO === options_live_micro LIVE 2026-09-10T09:06:04.915858-04:00 share=25% ===
Live account equity $227.82 cash $125.88 #225458845 options_level=3
2026-09-10 09:06:04,958 INFO Live account equity $227.82 cash $125.88 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-10 09:06:04,967 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-10 09:06:04,974 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (159 earlier lines - see full log file)
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 249 | 13 |
| S164 | 271 | 15 |
| S165 | 1711 | 28 |
| S166 | 135 | 9 |
| S167 | 265 | 15 |
| S168 | 198 | 13 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1202 | WARN | <<<
| Missing exit records (post) |  1187 | WARN | <<<
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |    46 | INFO |
| Total closed lots           |  2102 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1124 med=+2.4% | TAINTED n=1805 med=-38.4% | KEEP-only n=639 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.82 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T131108Z

- UTC timestamp: `20260910T131108Z`
- GitHub run: [#9582](https://github.com/28twagg-ops/TradingBot/actions/runs/34480945905)
- Run id: `34480945905`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`13s`
- Full logs: `logs/action_runs/20260910T131108Z_live_bot.log`, `logs/action_runs/20260910T131108Z_live_options.log`, `logs/action_runs/20260910T131108Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1124 | 50.0 | +2.4 | +44.1 | $+15,928 |
| TAINTED | 1805 | 33.6 | -38.4 | +12.5 | $-8,747 |
| KEEP-only | 639 | 63.4 | +51.4 | +70.5 | $+11,196 |
| KEEP-only recent | 431 | 60.6 | +53.3 | +82.2 | $+5,939 |

- KEEP strategies (25): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S359, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T09:11:14.344830-04:00","date":"2026-09-10","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.7,"phases_s":{"reconcile":0.57},"signals":0,"placed":0,"equity":1003501.53,"open_positions":15,"pending_orders":0,"open_lots":46,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9582","github_run_id":"34480945905","status":"ok","data_quality":{"clean":{"n":1124,"win":50.0,"med":2.38,"avg":44.07,"pnl":15927.59},"tainted":{"n":1805,"win":33.57,"med":-38.36,"avg":12.49,"pnl":-8746.84},"keep_only":{"n":639,"win":63.38,"med":51.39,"avg":70.55,"pnl":11196.45},"keep_only_recent":{"n":431,"win":60.56,"med":53.33,"avg":82.23,"pnl":5939.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S359","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:11:09  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.71|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $227.71|
|  Cash                                                           $125.88|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $101.83|
|  Open P&L                                                        $-1.10|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (3 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CNM      MomReversal     $33.71     $41.73   $41.00   -1.8%   $-0.60  |
|  FSLR     MomReversal     $33.60     $203.22  $199.02  -2.1%   $-0.71  |
|  TXT      MomReversal     $34.52     $80.00   $80.50   +0.6%   $+0.21  |
|                                                                        |
|  Total invested                                                 $101.83|
|  Total open P&L                                                  $-1.10|
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
|  2026-09-09  SELL  BAX  Pullback50  $9.45  P&L $-0.05                  |
|  2026-09-09  SELL  AAPL  Pullback50  $34.40  P&L $+0.04                |
|  2026-09-09  SELL  C  Pullback50  $34.30  P&L $-0.03                   |
|  2026-09-09  SELL  MKSI  MomReversal  $34.18  P&L $-0.31               |
|  2026-09-09  SELL  MGM  MomReversal  $34.07  P&L $-0.42                |
|  2026-09-08  SELL  AMCR  Pullback50  $34.40  P&L $-0.19                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-10T09:11:11.014738-04:00 share=25% ===
2026-09-10 09:11:11,014 INFO === options_live_micro LIVE 2026-09-10T09:11:11.014738-04:00 share=25% ===
Live account equity $227.71 cash $125.88 #225458845 options_level=3
2026-09-10 09:11:11,242 INFO Live account equity $227.71 cash $125.88 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-10 09:11:11,330 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-10 09:11:11,387 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (159 earlier lines - see full log file)
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 249 | 13 |
| S164 | 271 | 15 |
| S165 | 1711 | 28 |
| S166 | 135 | 9 |
| S167 | 265 | 15 |
| S168 | 198 | 13 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1202 | WARN | <<<
| Missing exit records (post) |  1187 | WARN | <<<
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |    46 | INFO |
| Total closed lots           |  2102 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1124 med=+2.4% | TAINTED n=1805 med=-38.4% | KEEP-only n=639 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.71 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T131605Z

- UTC timestamp: `20260910T131605Z`
- GitHub run: [#9583](https://github.com/28twagg-ops/TradingBot/actions/runs/34481461282)
- Run id: `34481461282`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`13s`
- Full logs: `logs/action_runs/20260910T131605Z_live_bot.log`, `logs/action_runs/20260910T131605Z_live_options.log`, `logs/action_runs/20260910T131605Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1124 | 50.0 | +2.4 | +44.1 | $+15,928 |
| TAINTED | 1805 | 33.6 | -38.4 | +12.5 | $-8,747 |
| KEEP-only | 639 | 63.4 | +51.4 | +70.5 | $+11,196 |
| KEEP-only recent | 431 | 60.6 | +53.3 | +82.2 | $+5,939 |

- KEEP strategies (25): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S359, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T09:16:10.947073-04:00","date":"2026-09-10","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.09},"signals":0,"placed":0,"equity":1003474.53,"open_positions":15,"pending_orders":0,"open_lots":46,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9583","github_run_id":"34481461282","status":"ok","data_quality":{"clean":{"n":1124,"win":50.0,"med":2.38,"avg":44.07,"pnl":15927.59},"tainted":{"n":1805,"win":33.57,"med":-38.36,"avg":12.49,"pnl":-8746.84},"keep_only":{"n":639,"win":63.38,"med":51.39,"avg":70.55,"pnl":11196.45},"keep_only_recent":{"n":431,"win":60.56,"med":53.33,"avg":82.23,"pnl":5939.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S359","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:16:06  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.79|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $227.79|
|  Cash                                                           $125.88|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $101.91|
|  Open P&L                                                        $-1.02|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (3 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CNM      MomReversal     $33.71     $41.73   $41.00   -1.8%   $-0.60  |
|  FSLR     MomReversal     $33.68     $203.22  $199.50  -1.8%   $-0.63  |
|  TXT      MomReversal     $34.52     $80.00   $80.50   +0.6%   $+0.21  |
|                                                                        |
|  Total invested                                                 $101.91|
|  Total open P&L                                                  $-1.02|
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
|  2026-09-09  SELL  BAX  Pullback50  $9.45  P&L $-0.05                  |
|  2026-09-09  SELL  AAPL  Pullback50  $34.40  P&L $+0.04                |
|  2026-09-09  SELL  C  Pullback50  $34.30  P&L $-0.03                   |
|  2026-09-09  SELL  MKSI  MomReversal  $34.18  P&L $-0.31               |
|  2026-09-09  SELL  MGM  MomReversal  $34.07  P&L $-0.42                |
|  2026-09-08  SELL  AMCR  Pullback50  $34.40  P&L $-0.19                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-10T09:16:07.827287-04:00 share=25% ===
2026-09-10 09:16:07,827 INFO === options_live_micro LIVE 2026-09-10T09:16:07.827287-04:00 share=25% ===
Live account equity $227.79 cash $125.88 #225458845 options_level=3
2026-09-10 09:16:07,872 INFO Live account equity $227.79 cash $125.88 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-10 09:16:07,880 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-10 09:16:07,888 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (159 earlier lines - see full log file)
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 249 | 13 |
| S164 | 271 | 15 |
| S165 | 1711 | 28 |
| S166 | 135 | 9 |
| S167 | 265 | 15 |
| S168 | 198 | 13 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1202 | WARN | <<<
| Missing exit records (post) |  1187 | WARN | <<<
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |    46 | INFO |
| Total closed lots           |  2102 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1124 med=+2.4% | TAINTED n=1805 med=-38.4% | KEEP-only n=639 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.79 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T132101Z

- UTC timestamp: `20260910T132101Z`
- GitHub run: [#9584](https://github.com/28twagg-ops/TradingBot/actions/runs/34481978596)
- Run id: `34481978596`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`13s`
- Full logs: `logs/action_runs/20260910T132101Z_live_bot.log`, `logs/action_runs/20260910T132101Z_live_options.log`, `logs/action_runs/20260910T132101Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1124 | 50.0 | +2.4 | +44.1 | $+15,928 |
| TAINTED | 1805 | 33.6 | -38.4 | +12.5 | $-8,747 |
| KEEP-only | 639 | 63.4 | +51.4 | +70.5 | $+11,196 |
| KEEP-only recent | 431 | 60.6 | +53.3 | +82.2 | $+5,939 |

- KEEP strategies (25): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S359, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T09:21:06.109311-04:00","date":"2026-09-10","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.11},"signals":0,"placed":0,"equity":1003504.58,"open_positions":15,"pending_orders":0,"open_lots":46,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9584","github_run_id":"34481978596","status":"ok","data_quality":{"clean":{"n":1124,"win":50.0,"med":2.38,"avg":44.07,"pnl":15927.59},"tainted":{"n":1805,"win":33.57,"med":-38.36,"avg":12.49,"pnl":-8746.84},"keep_only":{"n":639,"win":63.38,"med":51.39,"avg":70.55,"pnl":11196.45},"keep_only_recent":{"n":431,"win":60.56,"med":53.33,"avg":82.23,"pnl":5939.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S359","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:21:02  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.99|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $227.99|
|  Cash                                                           $125.88|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $102.11|
|  Open P&L                                                        $-0.82|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (3 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CNM      MomReversal     $33.82     $41.73   $41.14   -1.4%   $-0.49  |
|  FSLR     MomReversal     $33.77     $203.22  $200.00  -1.6%   $-0.54  |
|  TXT      MomReversal     $34.52     $80.00   $80.50   +0.6%   $+0.21  |
|                                                                        |
|  Total invested                                                 $102.11|
|  Total open P&L                                                  $-0.82|
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
|  2026-09-09  SELL  BAX  Pullback50  $9.45  P&L $-0.05                  |
|  2026-09-09  SELL  AAPL  Pullback50  $34.40  P&L $+0.04                |
|  2026-09-09  SELL  C  Pullback50  $34.30  P&L $-0.03                   |
|  2026-09-09  SELL  MKSI  MomReversal  $34.18  P&L $-0.31               |
|  2026-09-09  SELL  MGM  MomReversal  $34.07  P&L $-0.42                |
|  2026-09-08  SELL  AMCR  Pullback50  $34.40  P&L $-0.19                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-10T09:21:03.392887-04:00 share=25% ===
2026-09-10 09:21:03,392 INFO === options_live_micro LIVE 2026-09-10T09:21:03.392887-04:00 share=25% ===
Live account equity $227.99 cash $125.88 #225458845 options_level=3
2026-09-10 09:21:03,435 INFO Live account equity $227.99 cash $125.88 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-10 09:21:03,442 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-10 09:21:03,469 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (159 earlier lines - see full log file)
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 249 | 13 |
| S164 | 271 | 15 |
| S165 | 1711 | 28 |
| S166 | 135 | 9 |
| S167 | 265 | 15 |
| S168 | 198 | 13 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1202 | WARN | <<<
| Missing exit records (post) |  1187 | WARN | <<<
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |    46 | INFO |
| Total closed lots           |  2102 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1124 med=+2.4% | TAINTED n=1805 med=-38.4% | KEEP-only n=639 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.99 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T132614Z

- UTC timestamp: `20260910T132614Z`
- GitHub run: [#9585](https://github.com/28twagg-ops/TradingBot/actions/runs/34482500285)
- Run id: `34482500285`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`13s`
- Full logs: `logs/action_runs/20260910T132614Z_live_bot.log`, `logs/action_runs/20260910T132614Z_live_options.log`, `logs/action_runs/20260910T132614Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1124 | 50.0 | +2.4 | +44.1 | $+15,928 |
| TAINTED | 1805 | 33.6 | -38.4 | +12.5 | $-8,747 |
| KEEP-only | 639 | 63.4 | +51.4 | +70.5 | $+11,196 |
| KEEP-only recent | 431 | 60.6 | +53.3 | +82.2 | $+5,939 |

- KEEP strategies (25): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S359, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T09:26:20.104784-04:00","date":"2026-09-10","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.5,"phases_s":{"reconcile":0.5},"signals":0,"placed":0,"equity":1003513.53,"open_positions":15,"pending_orders":0,"open_lots":46,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9585","github_run_id":"34482500285","status":"ok","data_quality":{"clean":{"n":1124,"win":50.0,"med":2.38,"avg":44.07,"pnl":15927.59},"tainted":{"n":1805,"win":33.57,"med":-38.36,"avg":12.49,"pnl":-8746.84},"keep_only":{"n":639,"win":63.38,"med":51.39,"avg":70.55,"pnl":11196.45},"keep_only_recent":{"n":431,"win":60.56,"med":53.33,"avg":82.23,"pnl":5939.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S359","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:26:15  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.82|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $227.82|
|  Cash                                                           $125.88|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $101.94|
|  Open P&L                                                        $-0.99|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (3 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CNM      MomReversal     $33.82     $41.73   $41.14   -1.4%   $-0.49  |
|  FSLR     MomReversal     $33.60     $203.22  $199.00  -2.1%   $-0.71  |
|  TXT      MomReversal     $34.52     $80.00   $80.50   +0.6%   $+0.21  |
|                                                                        |
|  Total invested                                                 $101.94|
|  Total open P&L                                                  $-0.99|
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
|  2026-09-09  SELL  BAX  Pullback50  $9.45  P&L $-0.05                  |
|  2026-09-09  SELL  AAPL  Pullback50  $34.40  P&L $+0.04                |
|  2026-09-09  SELL  C  Pullback50  $34.30  P&L $-0.03                   |
|  2026-09-09  SELL  MKSI  MomReversal  $34.18  P&L $-0.31               |
|  2026-09-09  SELL  MGM  MomReversal  $34.07  P&L $-0.42                |
|  2026-09-08  SELL  AMCR  Pullback50  $34.40  P&L $-0.19                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-10T09:26:16.819172-04:00 share=25% ===
2026-09-10 09:26:16,819 INFO === options_live_micro LIVE 2026-09-10T09:26:16.819172-04:00 share=25% ===
Live account equity $227.82 cash $125.88 #225458845 options_level=3
2026-09-10 09:26:17,025 INFO Live account equity $227.82 cash $125.88 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-10 09:26:17,078 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-10 09:26:17,131 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (159 earlier lines - see full log file)
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 249 | 13 |
| S164 | 271 | 15 |
| S165 | 1711 | 28 |
| S166 | 135 | 9 |
| S167 | 265 | 15 |
| S168 | 198 | 13 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1202 | WARN | <<<
| Missing exit records (post) |  1187 | WARN | <<<
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |    46 | INFO |
| Total closed lots           |  2102 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1124 med=+2.4% | TAINTED n=1805 med=-38.4% | KEEP-only n=639 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.82 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T133104Z

- UTC timestamp: `20260910T133104Z`
- GitHub run: [#9586](https://github.com/28twagg-ops/TradingBot/actions/runs/34483016283)
- Run id: `34483016283`
- Live bot: exit=`0`, duration=`217s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260910T133104Z_live_bot.log`, `logs/action_runs/20260910T133104Z_live_options.log`, `logs/action_runs/20260910T133104Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1124 | 50.0 | +2.4 | +44.1 | $+15,928 |
| TAINTED | 1805 | 33.6 | -38.4 | +12.5 | $-8,747 |
| KEEP-only | 639 | 63.4 | +51.4 | +70.5 | $+11,196 |
| KEEP-only recent | 431 | 60.6 | +53.3 | +82.2 | $+5,939 |

- KEEP strategies (25): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S359, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T09:26:20.104784-04:00","date":"2026-09-10","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.5,"phases_s":{"reconcile":0.5},"signals":0,"placed":0,"equity":1003513.53,"open_positions":15,"pending_orders":0,"open_lots":46,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9585","github_run_id":"34482500285","status":"ok","data_quality":{"clean":{"n":1124,"win":50.0,"med":2.38,"avg":44.07,"pnl":15927.59},"tainted":{"n":1805,"win":33.57,"med":-38.36,"avg":12.49,"pnl":-8746.84},"keep_only":{"n":639,"win":63.38,"med":51.39,"avg":70.55,"pnl":11196.45},"keep_only_recent":{"n":431,"win":60.56,"med":53.33,"avg":82.23,"pnl":5939.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S359","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:31:05  INFO      Mode: morning_prep
13:31:07  INFO        [prep_positions] 3/3 (3 valid)
13:31:07  INFO      Fetching tickers (universe=both)...
13:31:07  INFO        S&P 500: 503
13:31:07  INFO        MidCap 400: 400
13:31:07  INFO        Total: 903 tickers
13:31:09  INFO        [prep_universe] 40/900 (40 valid)
13:31:10  INFO        [prep_universe] 80/900 (80 valid)
13:31:11  INFO        [prep_universe] 120/900 (120 valid)
13:31:13  INFO        [prep_universe] 160/900 (160 valid)
13:31:14  INFO        [prep_universe] 200/900 (199 valid)
13:31:22  INFO        [prep_universe] 240/900 (238 valid)
13:31:32  INFO        [prep_universe] 280/900 (278 valid)
13:31:46  INFO        [prep_universe] 320/900 (318 valid)
13:31:56  INFO        [prep_universe] 360/900 (358 valid)
13:32:09  INFO        [prep_universe] 400/900 (397 valid)
13:32:20  INFO        [prep_universe] 440/900 (437 valid)
13:32:33  INFO        [prep_universe] 480/900 (477 valid)
13:32:44  INFO        [prep_universe] 520/900 (517 valid)
13:32:57  INFO        [prep_universe] 560/900 (557 valid)
13:33:07  INFO        [prep_universe] 600/900 (597 valid)
13:33:21  INFO        [prep_universe] 640/900 (637 valid)
13:33:34  INFO        [prep_universe] 680/900 (677 valid)
13:33:44  INFO        [prep_universe] 720/900 (717 valid)
13:33:58  INFO        [prep_universe] 760/900 (757 valid)
13:34:08  INFO        [prep_universe] 800/900 (797 valid)
13:34:21  INFO        [prep_universe] 840/900 (837 valid)
13:34:32  INFO        [prep_universe] 880/900 (877 valid)
13:34:39  INFO        [prep_universe] 900/900 (897 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.70|
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
|  Invested                                                       $100.82|
|  Open P&L                                                        $-2.11|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CNM      MomReversal     $33.73     $41.73   $41.03   -1.7%   $-0.58  |
|  FSLR     MomReversal     $33.38     $203.22  $197.72  -2.7%   $-0.93  |
|  TXT      MomReversal     $33.71     $80.00   $78.61   -1.7%   $-0.60  |
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
|  Exit candidates                                                      3|
|  Signal candidates                                                   30|
|  Universe scanned                                                   900|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-10T09:34:42.601526-04:00 share=25% ===
2026-09-10 09:34:42,601 INFO === options_live_micro LIVE 2026-09-10T09:34:42.601526-04:00 share=25% ===
Live account equity $227.62 cash $125.88 #225458845 options_level=3
2026-09-10 09:34:42,903 INFO Live account equity $227.62 cash $125.88 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-10 09:34:43,122 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-10 09:34:43,258 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=46 paper_keys=yes dry_run=False
  alpaca positions=16
  FLAG b903|S411|c1edd829 missing from Alpaca
  FLAG b902|S411|ca4a7934 missing from Alpaca
  FLAG b238|S401|65ccd2ec missing from Alpaca
  FLAG b197|S218|c945d9ea missing from Alpaca
  FLAG b196|S218|8af6f434 missing from Alpaca
  FLAG b183|S217|4720dd96 missing from Alpaca
  FLAG b182|S217|5e079f33 missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$1,002,680.78
  buying_power=$3,958,428.92 cash=$1,037,801.28
  open option orders: 6
    C260911C00140000 OrderSide.SELL qty=2 status=OrderStatus.NEW limit=None
    SHOP260911C00147000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=0.35
    MARA260925C00012500 OrderSide.SELL qty=4 status=OrderStatus.NEW limit=None
    MARA260925C00011000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
    MARA260925C00011500 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
  open option positions: 15
    AVGO260911C00400000 qty=3 mkt=$3.00
    C260911C00140000 qty=2 mkt=$82.00
    CRWD260911C00222500 qty=-1 mkt=$-19.00
    CRWD260911C00235000 qty=1 mkt=$1.00
    MARA260911C00012000 qty=-1 mkt=$-16.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-10T09:34:46.681367-04:00 ===

[Run context]
Paper auth OK — equity $1002683.78, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
2026-09-10 09:34:49,066 INFO   EXIT [b164|lab0164_s216_w1_0928_1005_r1|S216] stop_loss (-97.5%) SELL 1 AVGO260911C00400000 @<= 0.01
  EXIT [b862|lab0862_s408_w4_1120_1135_r1|S408] stop_loss (-92.3%) SELL failed CRWD260911C00235000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b1055|lab1055_s165_w2_1005_1045_r2|S165] stop_loss (-100.0%) SELL failed SHOP260911C00146000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b1054|lab1054_s165_w2_1005_1045_r1|S165] stop_loss (-100.0%) SELL failed SHOP260911C00146000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
2026-09-10 09:34:51,333 INFO   EXIT [b1137|lab1137_s163_w1_0928_1005_r2|S163] stop_loss (-84.9%) SELL 1 ZS260911C00180000 @<= 0.06
2026-09-10 09:34:51,762 INFO   EXIT [b778|lab0778_s397_w2_1005_1045_r1|S397] stop_loss (-74.1%) SELL 1 ZS260911C00175000 @<= 0.16
  EXIT [b330|lab0330_s357_w2_1005_1045_r1|S357] stop_loss (-100.0%) SELL failed PATH260925C00017000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
Protective stops: placed=0 upgraded=0 already=4 failed=6 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
```

---

## Run 20260910T133651Z

- UTC timestamp: `20260910T133651Z`
- GitHub run: [#9587](https://github.com/28twagg-ops/TradingBot/actions/runs/34483542269)
- Run id: `34483542269`
- Live bot: exit=`0`, duration=`217s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260910T133651Z_live_bot.log`, `logs/action_runs/20260910T133651Z_live_options.log`, `logs/action_runs/20260910T133651Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1124 | 50.0 | +2.4 | +44.1 | $+15,928 |
| TAINTED | 1805 | 33.6 | -38.4 | +12.5 | $-8,747 |
| KEEP-only | 639 | 63.4 | +51.4 | +70.5 | $+11,196 |
| KEEP-only recent | 431 | 60.6 | +53.3 | +82.2 | $+5,939 |

- KEEP strategies (25): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S359, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T09:26:20.104784-04:00","date":"2026-09-10","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.5,"phases_s":{"reconcile":0.5},"signals":0,"placed":0,"equity":1003513.53,"open_positions":15,"pending_orders":0,"open_lots":46,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9585","github_run_id":"34482500285","status":"ok","data_quality":{"clean":{"n":1124,"win":50.0,"med":2.38,"avg":44.07,"pnl":15927.59},"tainted":{"n":1805,"win":33.57,"med":-38.36,"avg":12.49,"pnl":-8746.84},"keep_only":{"n":639,"win":63.38,"med":51.39,"avg":70.55,"pnl":11196.45},"keep_only_recent":{"n":431,"win":60.56,"med":53.33,"avg":82.23,"pnl":5939.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S359","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:36:52  INFO      Mode: morning_prep
13:36:53  INFO        [prep_positions] 3/3 (3 valid)
13:36:53  INFO      Fetching tickers (universe=both)...
13:36:53  INFO        S&P 500: 503
13:36:54  INFO        MidCap 400: 400
13:36:54  INFO        Total: 903 tickers
13:36:55  INFO        [prep_universe] 40/900 (40 valid)
13:36:56  INFO        [prep_universe] 80/900 (80 valid)
13:36:57  INFO        [prep_universe] 120/900 (120 valid)
13:36:58  INFO        [prep_universe] 160/900 (160 valid)
13:36:59  INFO        [prep_universe] 200/900 (199 valid)
13:37:07  INFO        [prep_universe] 240/900 (238 valid)
13:37:20  INFO        [prep_universe] 280/900 (278 valid)
13:37:33  INFO        [prep_universe] 320/900 (318 valid)
13:37:43  INFO        [prep_universe] 360/900 (358 valid)
13:37:56  INFO        [prep_universe] 400/900 (397 valid)
13:38:09  INFO        [prep_universe] 440/900 (437 valid)
13:38:19  INFO        [prep_universe] 480/900 (477 valid)
13:38:31  INFO        [prep_universe] 520/900 (517 valid)
13:38:44  INFO        [prep_universe] 560/900 (557 valid)
13:38:55  INFO        [prep_universe] 600/900 (597 valid)
13:39:08  INFO        [prep_universe] 640/900 (637 valid)
13:39:20  INFO        [prep_universe] 680/900 (677 valid)
13:39:31  INFO        [prep_universe] 720/900 (717 valid)
13:39:44  INFO        [prep_universe] 760/900 (757 valid)
13:39:56  INFO        [prep_universe] 800/900 (797 valid)
13:40:07  INFO        [prep_universe] 840/900 (837 valid)
13:40:20  INFO        [prep_universe] 880/900 (877 valid)
13:40:26  INFO        [prep_universe] 900/900 (897 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.54|
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
|  Invested                                                       $101.66|
|  Open P&L                                                        $-1.27|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CNM      MomReversal     $33.93     $41.73   $41.27   -1.1%   $-0.38  |
|  FSLR     MomReversal     $33.67     $203.22  $199.41  -1.9%   $-0.64  |
|  TXT      MomReversal     $34.06     $80.00   $79.43   -0.7%   $-0.25  |
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
|  Exit candidates                                                      3|
|  Signal candidates                                                   36|
|  Universe scanned                                                   900|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-10T09:40:29.537783-04:00 share=25% ===
2026-09-10 09:40:29,537 INFO === options_live_micro LIVE 2026-09-10T09:40:29.537783-04:00 share=25% ===
Live account equity $227.54 cash $125.88 #225458845 options_level=3
2026-09-10 09:40:29,633 INFO Live account equity $227.54 cash $125.88 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-10 09:40:29,709 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-10 09:40:29,759 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=46 paper_keys=yes dry_run=False
  alpaca positions=15
  FLAG b778|S397|463ee241 missing from Alpaca
  FLAG b903|S411|c1edd829 missing from Alpaca
  FLAG b902|S411|ca4a7934 missing from Alpaca
  FLAG b238|S401|65ccd2ec missing from Alpaca
  FLAG b197|S218|c945d9ea missing from Alpaca
  FLAG b196|S218|8af6f434 missing from Alpaca
  FLAG b183|S217|4720dd96 missing from Alpaca
  FLAG b182|S217|5e079f33 missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$1,002,442.24
  buying_power=$3,958,187.36 cash=$1,037,818.24
  open option orders: 7
    ZS260911C00180000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=0.06
    C260911C00140000 OrderSide.SELL qty=2 status=OrderStatus.NEW limit=None
    SHOP260911C00147000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=0.35
    MARA260925C00012500 OrderSide.SELL qty=4 status=OrderStatus.NEW limit=None
    MARA260925C00011000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
  open option positions: 14
    AVGO260911C00400000 qty=2 mkt=$2.00
    C260911C00140000 qty=2 mkt=$94.00
    CRWD260911C00222500 qty=-1 mkt=$-34.00
    CRWD260911C00235000 qty=1 mkt=$1.00
    MARA260911C00012000 qty=-1 mkt=$-11.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-10T09:40:32.759822-04:00 ===

[Run context]
Paper auth OK — equity $1002447.74, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
  EXIT [b330|lab0330_s357_w2_1005_1045_r1|S357] stop_loss (-100.0%) SELL failed PATH260925C00017000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
2026-09-10 09:40:34,471 INFO   EXIT [b167|lab0167_s216_w2_1005_1045_r2|S216] stop_loss (-97.5%) SELL 1 AVGO260911C00400000 @<= 0.01
  EXIT [b1055|lab1055_s165_w2_1005_1045_r2|S165] stop_loss (-100.0%) SELL failed SHOP260911C00146000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b1054|lab1054_s165_w2_1005_1045_r1|S165] stop_loss (-100.0%) SELL failed SHOP260911C00146000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b862|lab0862_s408_w4_1120_1135_r1|S408] stop_loss (-92.3%) SELL failed CRWD260911C00235000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
Protective stops: placed=0 upgraded=0 already=3 failed=6 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
```

---

## Run 20260910T134209Z

- UTC timestamp: `20260910T134209Z`
- GitHub run: [#9588](https://github.com/28twagg-ops/TradingBot/actions/runs/34484065658)
- Run id: `34484065658`
- Live bot: exit=`0`, duration=`218s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260910T134209Z_live_bot.log`, `logs/action_runs/20260910T134209Z_live_options.log`, `logs/action_runs/20260910T134209Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1124 | 50.0 | +2.4 | +44.1 | $+15,928 |
| TAINTED | 1805 | 33.6 | -38.4 | +12.5 | $-8,747 |
| KEEP-only | 639 | 63.4 | +51.4 | +70.5 | $+11,196 |
| KEEP-only recent | 431 | 60.6 | +53.3 | +82.2 | $+5,939 |

- KEEP strategies (25): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S359, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T09:26:20.104784-04:00","date":"2026-09-10","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.5,"phases_s":{"reconcile":0.5},"signals":0,"placed":0,"equity":1003513.53,"open_positions":15,"pending_orders":0,"open_lots":46,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9585","github_run_id":"34482500285","status":"ok","data_quality":{"clean":{"n":1124,"win":50.0,"med":2.38,"avg":44.07,"pnl":15927.59},"tainted":{"n":1805,"win":33.57,"med":-38.36,"avg":12.49,"pnl":-8746.84},"keep_only":{"n":639,"win":63.38,"med":51.39,"avg":70.55,"pnl":11196.45},"keep_only_recent":{"n":431,"win":60.56,"med":53.33,"avg":82.23,"pnl":5939.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S359","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:42:12  INFO      Mode: morning_prep
13:42:12  INFO        [prep_positions] 3/3 (3 valid)
13:42:12  INFO        Universe cache hit: 903 tickers (tickers_2026-09-10.json)
13:42:13  INFO        [prep_universe] 40/900 (40 valid)
13:42:15  INFO        [prep_universe] 80/900 (80 valid)
13:42:16  INFO        [prep_universe] 120/900 (120 valid)
13:42:17  INFO        [prep_universe] 160/900 (160 valid)
13:42:18  INFO        [prep_universe] 200/900 (199 valid)
13:42:29  INFO        [prep_universe] 240/900 (238 valid)
13:42:39  INFO        [prep_universe] 280/900 (278 valid)
13:42:52  INFO        [prep_universe] 320/900 (318 valid)
13:43:04  INFO        [prep_universe] 360/900 (358 valid)
13:43:14  INFO        [prep_universe] 400/900 (397 valid)
13:43:27  INFO        [prep_universe] 440/900 (437 valid)
13:43:40  INFO        [prep_universe] 480/900 (477 valid)
13:43:50  INFO        [prep_universe] 520/900 (517 valid)
13:44:03  INFO        [prep_universe] 560/900 (557 valid)
13:44:16  INFO        [prep_universe] 600/900 (597 valid)
13:44:26  INFO        [prep_universe] 640/900 (637 valid)
13:44:39  INFO        [prep_universe] 680/900 (677 valid)
13:44:52  INFO        [prep_universe] 720/900 (717 valid)
13:45:02  INFO        [prep_universe] 760/900 (757 valid)
13:45:15  INFO        [prep_universe] 800/900 (797 valid)
13:45:28  INFO        [prep_universe] 840/900 (837 valid)
13:45:38  INFO        [prep_universe] 880/900 (877 valid)
13:45:45  INFO        [prep_universe] 900/900 (897 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:42 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.40|
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
|  Invested                                                       $101.52|
|  Open P&L                                                        $-1.41|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CNM      MomReversal     $33.90     $41.73   $41.23   -1.2%   $-0.41  |
|  FSLR     MomReversal     $33.85     $203.22  $200.50  -1.3%   $-0.46  |
|  TXT      MomReversal     $33.77     $80.00   $78.75   -1.6%   $-0.54  |
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
|  Exit candidates                                                      3|
|  Signal candidates                                                   29|
|  Universe scanned                                                   900|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-10T09:45:48.143009-04:00 share=25% ===
2026-09-10 09:45:48,143 INFO === options_live_micro LIVE 2026-09-10T09:45:48.143009-04:00 share=25% ===
Live account equity $227.31 cash $125.88 #225458845 options_level=3
2026-09-10 09:45:48,210 INFO Live account equity $227.31 cash $125.88 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-10 09:45:48,244 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-10 09:45:48,267 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=37 paper_keys=yes dry_run=False
  alpaca positions=15
  FLAG b778|S397|463ee241 missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$1,002,449.70
  buying_power=$3,958,485.80 cash=$1,037,827.20
  open option orders: 6
    C260911C00140000 OrderSide.SELL qty=2 status=OrderStatus.NEW limit=None
    SHOP260911C00147000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=0.35
    MARA260925C00012500 OrderSide.SELL qty=4 status=OrderStatus.NEW limit=None
    MARA260925C00011000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
    MARA260925C00011500 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
  open option positions: 14
    AVGO260911C00400000 qty=1 mkt=$2.00
    C260911C00140000 qty=2 mkt=$108.00
    CRWD260911C00222500 qty=-1 mkt=$-49.00
    CRWD260911C00235000 qty=1 mkt=$3.00
    MARA260911C00012000 qty=-1 mkt=$-9.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-10T09:45:51.056222-04:00 ===

[Run context]
Paper auth OK — equity $1002448.70, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
  EXIT [b862|lab0862_s408_w4_1120_1135_r1|S408] stop_loss (-76.9%) SELL failed CRWD260911C00235000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
2026-09-10 09:45:53,399 INFO   EXIT [b166|lab0166_s216_w2_1005_1045_r1|S216] stop_loss (-95.0%) SELL 1 AVGO260911C00400000 @<= 0.03
  EXIT [b330|lab0330_s357_w2_1005_1045_r1|S357] stop_loss (-100.0%) SELL failed PATH260925C00017000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b1055|lab1055_s165_w2_1005_1045_r2|S165] stop_loss (-100.0%) SELL failed SHOP260911C00146000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b1054|lab1054_s165_w2_1005_1045_r1|S165] stop_loss (-100.0%) SELL failed SHOP260911C00146000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
2026-09-10 09:45:54,353 INFO   EXIT [b1136|lab1136_s163_w1_0928_1005_r1|S163] stop_loss (-75.9%) SELL 1 ZS260911C00180000 @<= 0.09
Protective stops: placed=0 upgraded=0 already=4 failed=5 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
```

---

## Run 20260910T134810Z

- UTC timestamp: `20260910T134810Z`
- GitHub run: [#9589](https://github.com/28twagg-ops/TradingBot/actions/runs/34484592238)
- Run id: `34484592238`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260910T134810Z_live_bot.log`, `logs/action_runs/20260910T134810Z_live_options.log`, `logs/action_runs/20260910T134810Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1124 | 50.0 | +2.4 | +44.1 | $+15,928 |
| TAINTED | 1805 | 33.6 | -38.4 | +12.5 | $-8,747 |
| KEEP-only | 639 | 63.4 | +51.4 | +70.5 | $+11,196 |
| KEEP-only recent | 431 | 60.6 | +53.3 | +82.2 | $+5,939 |

- KEEP strategies (25): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S359, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T09:26:20.104784-04:00","date":"2026-09-10","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.5,"phases_s":{"reconcile":0.5},"signals":0,"placed":0,"equity":1003513.53,"open_positions":15,"pending_orders":0,"open_lots":46,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9585","github_run_id":"34482500285","status":"ok","data_quality":{"clean":{"n":1124,"win":50.0,"med":2.38,"avg":44.07,"pnl":15927.59},"tainted":{"n":1805,"win":33.57,"med":-38.36,"avg":12.49,"pnl":-8746.84},"keep_only":{"n":639,"win":63.38,"med":51.39,"avg":70.55,"pnl":11196.45},"keep_only_recent":{"n":431,"win":60.56,"med":53.33,"avg":82.23,"pnl":5939.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S359","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:48:10  INFO      Mode: morning_scan
13:48:11  INFO        [positions] 3/3 (3 valid)
13:48:11  INFO        SELL MARKET [urgent] FSLR closed
13:48:13  INFO        TX logged: SELL FSLR  P&L -1.39%
13:48:13  INFO        SELL MARKET [urgent] TXT closed
13:48:15  INFO        TX logged: SELL TXT  P&L -1.26%
13:48:15  INFO        SELL MARKET [urgent] CNM closed
13:48:17  INFO        TX logged: SELL CNM  P&L -0.66%
13:48:17  INFO        Universe cache hit: 903 tickers (tickers_2026-09-10.json)
13:48:18  INFO        [universe] 40/903 (40 valid)
13:48:20  INFO        [universe] 80/903 (80 valid)
13:48:21  INFO        [universe] 120/903 (120 valid)
13:48:22  INFO        [universe] 160/903 (160 valid)
13:48:24  INFO        [universe] 200/903 (199 valid)
13:48:31  INFO        [universe] 240/903 (238 valid)
13:48:44  INFO        [universe] 280/903 (278 valid)
13:48:54  INFO        [universe] 320/903 (318 valid)
13:49:07  INFO        [universe] 360/903 (358 valid)
13:49:20  INFO        [universe] 400/903 (397 valid)
13:49:30  INFO        [universe] 440/903 (437 valid)
13:49:43  INFO        [universe] 480/903 (477 valid)
13:49:56  INFO        [universe] 520/903 (517 valid)
13:50:06  INFO        [universe] 560/903 (557 valid)
13:50:19  INFO        [universe] 600/903 (597 valid)
13:50:32  INFO        [universe] 640/903 (637 valid)
13:50:42  INFO        [universe] 680/903 (677 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20260910T135203Z

- UTC timestamp: `20260910T135203Z`
- GitHub run: [#9590](https://github.com/28twagg-ops/TradingBot/actions/runs/34485122525)
- Run id: `34485122525`
- Live bot: exit=`0`, duration=`248s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260910T135203Z_live_bot.log`, `logs/action_runs/20260910T135203Z_live_options.log`, `logs/action_runs/20260910T135203Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1124 | 50.0 | +2.4 | +44.1 | $+15,928 |
| TAINTED | 1805 | 33.6 | -38.4 | +12.5 | $-8,747 |
| KEEP-only | 639 | 63.4 | +51.4 | +70.5 | $+11,196 |
| KEEP-only recent | 431 | 60.6 | +53.3 | +82.2 | $+5,939 |

- KEEP strategies (25): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S359, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T09:26:20.104784-04:00","date":"2026-09-10","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.5,"phases_s":{"reconcile":0.5},"signals":0,"placed":0,"equity":1003513.53,"open_positions":15,"pending_orders":0,"open_lots":46,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9585","github_run_id":"34482500285","status":"ok","data_quality":{"clean":{"n":1124,"win":50.0,"med":2.38,"avg":44.07,"pnl":15927.59},"tainted":{"n":1805,"win":33.57,"med":-38.36,"avg":12.49,"pnl":-8746.84},"keep_only":{"n":639,"win":63.38,"med":51.39,"avg":70.55,"pnl":11196.45},"keep_only_recent":{"n":431,"win":60.56,"med":53.33,"avg":82.23,"pnl":5939.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S359","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
... (117 earlier lines - see full log file)
|  BWA      Pullback50      eq     $65.01   50.7   -3.04   50MA bounce (-|
|  CHE      Pullback50      eq     $521.22  40.4   -1.93   50MA bounce (+|
|  KEX      Pullback50      eq     $138.09  46.9   -3.09   50MA bounce (-|
|  KNSL     Pullback50      eq     $365.23  39.6   -3.02   50MA bounce (+|
|  NWE      Pullback50      eq     $70.58   48.8   -2.74   50MA bounce (-|
|  SANM     Pullback50      eq     $203.29  59.5   -2.51   50MA bounce (+|
|  TOST     Pullback50      eq     $32.64   31.6   -2.65   50MA bounce (-|
|                                                                        |
+========================================================================+

+========================================================================+
|                              ENTRY ORDERS                              |
+========================================================================+
|    ENTER [eq] ABBV  Pullback50                                   $34.11|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    ENTER [eq] AES  Pullback50                                    $34.11|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    ENTER [eq] MO  Pullback50                                     $34.11|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    SKIP [eq] AAPL  Pullback50                                     cap 3|
|    SKIP [eq] CI  Pullback50                                       cap 3|
|    SKIP [eq] COHR  Pullback50                                     cap 3|
|    SKIP [eq] EG  Pullback50                                       cap 3|
|    SKIP [eq] FFIV  Pullback50                                     cap 3|
|    SKIP [eq] FAST  Pullback50                                     cap 3|
|    SKIP [eq] FTNT  Pullback50                                     cap 3|
|    SKIP [eq] GM  Pullback50                                       cap 3|
|    SKIP [eq] MA  Pullback50                                       cap 3|
|    SKIP [eq] MS  Pullback50                                       cap 3|13:56:10  INFO        place_all_stops: checking 3 positions...
13:56:10  INFO        STOP skipped ABBV: fractional (0.1343 shares) — software exit will handle it
13:56:10  INFO        STOP-MARKET placed AES  qty=2 (pos=2.3013)  stop=$14.74  id=3ec801bd-c5fe-4419-9699-42d0c260fbe2
13:56:10  INFO        STOP skipped MO: fractional (0.4947 shares) — software exit will handle it
13:56:10  INFO        Daily log -> logs/daily/2026-09-10.md
13:56:10  INFO        Dashboard written → logs/dashboard.md

|    SKIP [eq] NTRS  Pullback50                                     cap 3|
|    SKIP [eq] V  Pullback50                                        cap 3|
|    SKIP [eq] WRB  Pullback50                                      cap 3|
|    SKIP [eq] ATI  Pullback50                                      cap 3|
|    SKIP [eq] BWA  Pullback50                                      cap 3|
|    SKIP [eq] CHE  Pullback50                                      cap 3|
|    SKIP [eq] KEX  Pullback50                                      cap 3|
|    SKIP [eq] KNSL  Pullback50                                     cap 3|
|    SKIP [eq] NWE  Pullback50                                      cap 3|
|    SKIP [eq] SANM  Pullback50                                     cap 3|
|    SKIP [eq] TOST  Pullback50                                     cap 3|
|    SKIP [eq] AVAV  RSIRecovery                                    cap 3|

+========================================================================+
|                         BUY FILL CONFIRMATION                          |
+========================================================================+
|  Pending submits                                                      3|
+------------------------------------------------------------------------+
|  ABBV                                                 still unconfirmed|
|  AES                                                  still unconfirmed|
|  MO                                                   still unconfirmed|
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
|  Scanned                                                            900|
|  Signals                                                             25|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  3 unconfirmed|
|  Exits                                                                0|
|  Open pos                                                             3|
|  Equity                                                         $227.38|
|  Cash                                                           $125.10|
+========================================================================+
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20260910T135957Z

- UTC timestamp: `20260910T135957Z`
- GitHub run: [#9591](https://github.com/28twagg-ops/TradingBot/actions/runs/34485647892)
- Run id: `34485647892`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260910T135957Z_live_bot.log`, `logs/action_runs/20260910T135957Z_live_options.log`, `logs/action_runs/20260910T135957Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1124 | 50.0 | +2.4 | +44.1 | $+15,928 |
| TAINTED | 1805 | 33.6 | -38.4 | +12.5 | $-8,747 |
| KEEP-only | 639 | 63.4 | +51.4 | +70.5 | $+11,196 |
| KEEP-only recent | 431 | 60.6 | +53.3 | +82.2 | $+5,939 |

- KEEP strategies (25): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S359, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T09:26:20.104784-04:00","date":"2026-09-10","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.5,"phases_s":{"reconcile":0.5},"signals":0,"placed":0,"equity":1003513.53,"open_positions":15,"pending_orders":0,"open_lots":46,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9585","github_run_id":"34482500285","status":"ok","data_quality":{"clean":{"n":1124,"win":50.0,"med":2.38,"avg":44.07,"pnl":15927.59},"tainted":{"n":1805,"win":33.57,"med":-38.36,"avg":12.49,"pnl":-8746.84},"keep_only":{"n":639,"win":63.38,"med":51.39,"avg":70.55,"pnl":11196.45},"keep_only_recent":{"n":431,"win":60.56,"med":53.33,"avg":82.23,"pnl":5939.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S359","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:59:58  INFO      Mode: morning_scan
13:59:59  INFO        [positions] 3/3 (3 valid)
13:59:59  INFO        SELL order cancelled AES  type=OrderType.STOP  id=3ec801bd-c5fe-4419-9699-42d0c260fbe2
13:59:59  INFO        SELL LIMIT AES  qty=2.301304679  limit=$14.81  id=e9f78f97-63ad-423d-b350-f96b40b04793
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20260910T140158Z

- UTC timestamp: `20260910T140158Z`
- GitHub run: [#9592](https://github.com/28twagg-ops/TradingBot/actions/runs/34486178928)
- Run id: `34486178928`
- Live bot: exit=`0`, duration=`5s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`165s`
- Full logs: `logs/action_runs/20260910T140158Z_live_bot.log`, `logs/action_runs/20260910T140158Z_live_options.log`, `logs/action_runs/20260910T140158Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1128 | 49.8 | +0.0 | +43.7 | $+15,817 |
| TAINTED | 1812 | 33.5 | -38.6 | +12.3 | $-8,848 |
| KEEP-only | 641 | 63.2 | +51.4 | +70.1 | $+11,148 |
| KEEP-only recent | 433 | 60.3 | +53.3 | +81.5 | $+5,891 |

- KEEP strategies (25): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S359, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T10:02:08.565319-04:00","date":"2026-09-10","mode":"entry+manage","header":"entry+manage (55 new)","elapsed_s":152.8,"phases_s":{"reconcile":0.25,"cancel":0.05,"manage":3.06,"protective_stops":1.05,"scan":56.47,"entries":71.86,"reconcile2":2.61},"signals":372,"placed":55,"equity":1002512.15,"open_positions":25,"pending_orders":6,"open_lots":80,"submitted_today":55,"filled_today":49,"unattributed_contracts":0,"top_signals":["S401:TSLA","S359:TSLA","S361:TSLA","S362:TSLA","S363:TSLA","S364:TSLA","S365:TSLA","S366:TSLA"],"github_run":"9592","github_run_id":"34486178928","status":"ok","data_quality":{"clean":{"n":1128,"win":49.82,"med":0.0,"avg":43.68,"pnl":15816.59},"tainted":{"n":1812,"win":33.5,"med":-38.59,"avg":12.27,"pnl":-8847.84},"keep_only":{"n":641,"win":63.18,"med":51.39,"avg":70.13,"pnl":11148.45},"keep_only_recent":{"n":433,"win":60.28,"med":53.33,"avg":81.55,"pnl":5891.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S359","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
14:02:00  INFO      Mode: exits
14:02:00  INFO        Daily log -> logs/daily/2026-09-10.md
14:02:00  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (3 ledger rows)
14:02:00  INFO        place_all_stops: checking 1 positions...
14:02:00  INFO        STOP skipped ABBV: fractional (0.1343 shares) — software exit will handle it
14:02:00  INFO        [positions] 1/1 (1 valid)
14:02:01  INFO        SELL MARKET [urgent] ABBV closed
14:02:03  INFO        TX logged: SELL ABBV  P&L -0.58%
14:02:03  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:02 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.17|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ABBV  P&L -0.6%  $-0.20                        EXIT: stop_loss (-0.6%)|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  1 attempted  |  1 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
|  Logged exits                                                         1|
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
|  ABBV                                        -0.58%  (threshold -0.50%)|
|  Count                                                                1|
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-10T10:02:05.008813-04:00 share=25% ===
2026-09-10 10:02:05,008 INFO === options_live_micro LIVE 2026-09-10T10:02:05.008813-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 10:02:05,094 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-10 10:02:05,205 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-10 10:02:05,248 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (199 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 253 | 14 |
| S164 | 271 | 15 |
| S165 | 1711 | 28 |
| S166 | 135 | 9 |
| S167 | 265 | 15 |
| S168 | 198 | 13 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1201 | WARN | <<<
| Missing exit records (post) |  1186 | WARN | <<<
| State/ledger mismatches     |     5 | WARN | <<<
| Total open lots             |    80 | INFO |
| Total closed lots           |  2112 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1128 med=+0.0% | TAINTED n=1812 med=-38.6% | KEEP-only n=641 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T140611Z

- UTC timestamp: `20260910T140611Z`
- GitHub run: [#9593](https://github.com/28twagg-ops/TradingBot/actions/runs/34486722706)
- Run id: `34486722706`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`200s`
- Full logs: `logs/action_runs/20260910T140611Z_live_bot.log`, `logs/action_runs/20260910T140611Z_live_options.log`, `logs/action_runs/20260910T140611Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1126 | 49.9 | +0.0 | +43.9 | $+15,872 |
| TAINTED | 1817 | 33.4 | -39.0 | +12.1 | $-8,965 |
| KEEP-only | 640 | 63.3 | +51.4 | +70.4 | $+11,179 |
| KEEP-only recent | 432 | 60.4 | +53.3 | +81.9 | $+5,922 |

- KEEP strategies (25): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S359, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T10:06:19.086438-04:00","date":"2026-09-10","mode":"entry+manage","header":"entry+manage (54 new)","elapsed_s":189.6,"phases_s":{"reconcile":2.47,"cancel":0.12,"manage":12.11,"protective_stops":2.79,"scan":48.69,"entries":100.94,"reconcile2":5.2},"signals":372,"placed":54,"equity":1001727.07,"open_positions":38,"pending_orders":12,"open_lots":127,"submitted_today":54,"filled_today":97,"unattributed_contracts":0,"top_signals":["S401:TSLA","S359:TSLA","S361:TSLA","S362:TSLA","S363:TSLA","S364:TSLA","S365:TSLA","S366:TSLA"],"github_run":"9593","github_run_id":"34486722706","status":"ok","data_quality":{"clean":{"n":1126,"win":49.91,"med":0.0,"avg":43.86,"pnl":15871.59},"tainted":{"n":1817,"win":33.41,"med":-38.98,"avg":12.06,"pnl":-8964.84},"keep_only":{"n":640,"win":63.28,"med":51.39,"avg":70.36,"pnl":11179.45},"keep_only_recent":{"n":432,"win":60.42,"med":53.33,"avg":81.91,"pnl":5922.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S359","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
14:06:12  INFO      Mode: exits
14:06:13  INFO        Daily log -> logs/daily/2026-09-10.md
14:06:13  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (4 ledger rows)
14:06:14  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T10:06:15.366227-04:00 share=25% ===
2026-09-10 10:06:15,366 INFO === options_live_micro LIVE 2026-09-10T10:06:15.366227-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 10:06:15,575 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-10 10:06:15,796 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-10 10:06:15,917 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (220 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 253 | 14 |
| S164 | 275 | 16 |
| S165 | 1711 | 28 |
| S166 | 135 | 9 |
| S167 | 269 | 16 |
| S168 | 200 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |    4 |    4 |    0 |    0 |    4 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    14 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1201 | WARN | <<<
| Missing exit records (post) |  1186 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   127 | INFO |
| Total closed lots           |  2115 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1126 med=+0.0% | TAINTED n=1817 med=-39.0% | KEEP-only n=640 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T141101Z

- UTC timestamp: `20260910T141101Z`
- GitHub run: [#9594](https://github.com/28twagg-ops/TradingBot/actions/runs/34487258494)
- Run id: `34487258494`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`108s`
- Full logs: `logs/action_runs/20260910T141101Z_live_bot.log`, `logs/action_runs/20260910T141101Z_live_options.log`, `logs/action_runs/20260910T141101Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1127 | 49.9 | +0.0 | +43.8 | $+15,848 |
| TAINTED | 1817 | 33.4 | -39.0 | +12.1 | $-8,965 |
| KEEP-only | 641 | 63.2 | +51.4 | +70.1 | $+11,155 |
| KEEP-only recent | 433 | 60.3 | +53.3 | +81.5 | $+5,898 |

- KEEP strategies (25): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S359, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T10:11:06.797880-04:00","date":"2026-09-10","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":98.6,"phases_s":{"reconcile":0.36,"cancel":0.07,"manage":13.75,"protective_stops":2.06,"scan":34.75,"entries":29.35,"reconcile2":0.33},"signals":372,"placed":0,"equity":1001358.73,"open_positions":38,"pending_orders":12,"open_lots":126,"submitted_today":54,"filled_today":97,"unattributed_contracts":0,"top_signals":["S401:TSLA","S359:TSLA","S361:TSLA","S362:TSLA","S363:TSLA","S364:TSLA","S365:TSLA","S366:TSLA"],"github_run":"9594","github_run_id":"34487258494","status":"ok","data_quality":{"clean":{"n":1127,"win":49.87,"med":0.0,"avg":43.76,"pnl":15847.59},"tainted":{"n":1817,"win":33.41,"med":-38.98,"avg":12.06,"pnl":-8964.84},"keep_only":{"n":641,"win":63.18,"med":51.39,"avg":70.13,"pnl":11155.45},"keep_only_recent":{"n":433,"win":60.28,"med":53.33,"avg":81.55,"pnl":5898.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S359","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
14:11:02  INFO      Mode: exits
14:11:02  INFO        Daily log -> logs/daily/2026-09-10.md
14:11:02  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
14:11:03  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T10:11:03.766056-04:00 share=25% ===
2026-09-10 10:11:03,766 INFO === options_live_micro LIVE 2026-09-10T10:11:03.766056-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 10:11:04,141 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-10 10:11:04,277 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-10 10:11:04,367 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (207 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 253 | 14 |
| S164 | 275 | 16 |
| S165 | 1711 | 28 |
| S166 | 135 | 9 |
| S167 | 269 | 16 |
| S168 | 200 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |    4 |    4 |    0 |    0 |    4 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    14 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1201 | WARN | <<<
| Missing exit records (post) |  1186 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   126 | INFO |
| Total closed lots           |  2116 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1127 med=+0.0% | TAINTED n=1817 med=-39.0% | KEEP-only n=641 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T141640Z

- UTC timestamp: `20260910T141640Z`
- GitHub run: [#9595](https://github.com/28twagg-ops/TradingBot/actions/runs/34487804014)
- Run id: `34487804014`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`118s`
- Full logs: `logs/action_runs/20260910T141640Z_live_bot.log`, `logs/action_runs/20260910T141640Z_live_options.log`, `logs/action_runs/20260910T141640Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1129 | 49.8 | +0.0 | +43.6 | $+15,799 |
| TAINTED | 1818 | 33.4 | -39.0 | +12.0 | $-9,009 |
| KEEP-only | 642 | 63.1 | +51.2 | +70.0 | $+11,129 |
| KEEP-only recent | 434 | 60.1 | +53.3 | +81.3 | $+5,872 |

- KEEP strategies (25): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S359, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T10:16:45.995701-04:00","date":"2026-09-10","mode":"entry+manage","header":"entry+manage (2 new)","elapsed_s":106.7,"phases_s":{"reconcile":0.32,"cancel":0.03,"manage":10.88,"protective_stops":0.75,"scan":53.04,"entries":22.12,"reconcile2":3.33},"signals":372,"placed":2,"equity":1001142.57,"open_positions":38,"pending_orders":8,"open_lots":129,"submitted_today":56,"filled_today":103,"unattributed_contracts":0,"top_signals":["S401:TSLA","S359:TSLA","S361:TSLA","S362:TSLA","S363:TSLA","S364:TSLA","S365:TSLA","S366:TSLA"],"github_run":"9595","github_run_id":"34487804014","status":"ok","data_quality":{"clean":{"n":1129,"win":49.78,"med":0.0,"avg":43.6,"pnl":15798.59},"tainted":{"n":1818,"win":33.39,"med":-39.0,"avg":12.01,"pnl":-9008.84},"keep_only":{"n":642,"win":63.08,"med":51.18,"avg":69.96,"pnl":11129.45},"keep_only_recent":{"n":434,"win":60.14,"med":53.33,"avg":81.28,"pnl":5872.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S359","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
14:16:41  INFO      Mode: exits
14:16:41  INFO        Daily log -> logs/daily/2026-09-10.md
14:16:41  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
14:16:41  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T10:16:42.977573-04:00 share=25% ===
2026-09-10 10:16:42,977 INFO === options_live_micro LIVE 2026-09-10T10:16:42.977573-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 10:16:43,018 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-10 10:16:43,052 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-10 10:16:43,065 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (208 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 253 | 14 |
| S164 | 275 | 16 |
| S165 | 1711 | 28 |
| S166 | 135 | 9 |
| S167 | 269 | 16 |
| S168 | 200 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |    4 |    4 |    0 |    0 |    4 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    14 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1201 | WARN | <<<
| Missing exit records (post) |  1186 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   129 | INFO |
| Total closed lots           |  2118 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1129 med=+0.0% | TAINTED n=1818 med=-39.0% | KEEP-only n=642 med=+51.2% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T142109Z

- UTC timestamp: `20260910T142109Z`
- GitHub run: [#9596](https://github.com/28twagg-ops/TradingBot/actions/runs/34488353861)
- Run id: `34488353861`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`121s`
- Full logs: `logs/action_runs/20260910T142109Z_live_bot.log`, `logs/action_runs/20260910T142109Z_live_options.log`, `logs/action_runs/20260910T142109Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1130 | 49.7 | -1.2 | +43.5 | $+15,776 |
| TAINTED | 1818 | 33.4 | -39.0 | +12.0 | $-9,009 |
| KEEP-only | 643 | 63.0 | +51.0 | +69.8 | $+11,106 |
| KEEP-only recent | 435 | 60.0 | +53.3 | +81.0 | $+5,849 |

- KEEP strategies (25): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S359, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T10:21:15.955722-04:00","date":"2026-09-10","mode":"entry+manage","header":"entry+manage (1 new)","elapsed_s":108.7,"phases_s":{"reconcile":0.42,"cancel":0.12,"manage":16.86,"protective_stops":3.03,"scan":46.09,"entries":28.41,"reconcile2":0.5},"signals":372,"placed":1,"equity":1000998.97,"open_positions":39,"pending_orders":8,"open_lots":129,"submitted_today":57,"filled_today":104,"unattributed_contracts":0,"top_signals":["S401:TSLA","S359:TSLA","S361:TSLA","S362:TSLA","S363:TSLA","S364:TSLA","S365:TSLA","S366:TSLA"],"github_run":"9596","github_run_id":"34488353861","status":"ok","data_quality":{"clean":{"n":1130,"win":49.73,"med":-1.25,"avg":43.52,"pnl":15775.59},"tainted":{"n":1818,"win":33.39,"med":-39.0,"avg":12.01,"pnl":-9008.84},"keep_only":{"n":643,"win":62.99,"med":50.98,"avg":69.78,"pnl":11106.45},"keep_only_recent":{"n":435,"win":60.0,"med":53.33,"avg":80.98,"pnl":5849.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S359","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
14:21:10  INFO      Mode: exits
14:21:10  INFO        Daily log -> logs/daily/2026-09-10.md
14:21:10  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
14:21:11  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T10:21:12.069489-04:00 share=25% ===
2026-09-10 10:21:12,069 INFO === options_live_micro LIVE 2026-09-10T10:21:12.069489-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 10:21:12,276 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-10 10:21:12,450 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-10 10:21:12,564 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (207 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 253 | 14 |
| S164 | 275 | 16 |
| S165 | 1711 | 28 |
| S166 | 135 | 9 |
| S167 | 269 | 16 |
| S168 | 200 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |    4 |    4 |    0 |    0 |    4 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    14 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1201 | WARN | <<<
| Missing exit records (post) |  1186 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   129 | INFO |
| Total closed lots           |  2119 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1130 med=-1.2% | TAINTED n=1818 med=-39.0% | KEEP-only n=643 med=+51.0% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T142610Z

- UTC timestamp: `20260910T142610Z`
- GitHub run: [#9597](https://github.com/28twagg-ops/TradingBot/actions/runs/34488909280)
- Run id: `34488909280`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`129s`
- Full logs: `logs/action_runs/20260910T142610Z_live_bot.log`, `logs/action_runs/20260910T142610Z_live_options.log`, `logs/action_runs/20260910T142610Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1132 | 49.6 | -2.6 | +43.3 | $+15,729 |
| TAINTED | 1818 | 33.4 | -39.0 | +12.0 | $-9,009 |
| KEEP-only | 628 | 63.2 | +51.4 | +68.4 | $+11,077 |
| KEEP-only recent | 420 | 60.2 | +53.3 | +79.4 | $+5,820 |

- KEEP strategies (24): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T10:26:18.677762-04:00","date":"2026-09-10","mode":"entry+manage","header":"entry+manage (3 new)","elapsed_s":116.8,"phases_s":{"reconcile":0.52,"cancel":0.14,"manage":19.58,"protective_stops":4.27,"scan":53.26,"entries":33.39,"reconcile2":0.58},"signals":372,"placed":3,"equity":1001572.92,"open_positions":39,"pending_orders":11,"open_lots":127,"submitted_today":60,"filled_today":104,"unattributed_contracts":0,"top_signals":["S401:TSLA","S359:TSLA","S361:TSLA","S362:TSLA","S363:TSLA","S364:TSLA","S365:TSLA","S366:TSLA"],"github_run":"9597","github_run_id":"34488909280","status":"ok","data_quality":{"clean":{"n":1132,"win":49.65,"med":-2.6,"avg":43.34,"pnl":15728.59},"tainted":{"n":1818,"win":33.39,"med":-39.0,"avg":12.01,"pnl":-9008.84},"keep_only":{"n":628,"win":63.22,"med":51.39,"avg":68.43,"pnl":11077.45},"keep_only_recent":{"n":420,"win":60.24,"med":53.33,"avg":79.36,"pnl":5820.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
14:26:12  INFO      Mode: exits
14:26:13  INFO        Daily log -> logs/daily/2026-09-10.md
14:26:13  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
14:26:13  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T10:26:14.590807-04:00 share=25% ===
2026-09-10 10:26:14,590 INFO === options_live_micro LIVE 2026-09-10T10:26:14.590807-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 10:26:14,814 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-10 10:26:15,017 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-10 10:26:15,151 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (196 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 253 | 14 |
| S164 | 275 | 16 |
| S165 | 1711 | 28 |
| S166 | 135 | 9 |
| S167 | 269 | 16 |
| S168 | 200 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |    4 |    4 |    0 |    0 |    4 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    14 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1201 | WARN | <<<
| Missing exit records (post) |  1186 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   127 | INFO |
| Total closed lots           |  2121 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1132 med=-2.6% | TAINTED n=1818 med=-39.0% | KEEP-only n=628 med=+51.4% | KILL=18 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T143107Z

- UTC timestamp: `20260910T143107Z`
- GitHub run: [#9598](https://github.com/28twagg-ops/TradingBot/actions/runs/34489461789)
- Run id: `34489461789`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`116s`
- Full logs: `logs/action_runs/20260910T143107Z_live_bot.log`, `logs/action_runs/20260910T143107Z_live_options.log`, `logs/action_runs/20260910T143107Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1133 | 49.6 | -2.7 | +43.2 | $+15,706 |
| TAINTED | 1818 | 33.4 | -39.0 | +12.0 | $-9,009 |
| KEEP-only | 628 | 63.2 | +51.4 | +68.4 | $+11,077 |
| KEEP-only recent | 420 | 60.2 | +53.3 | +79.4 | $+5,820 |

- KEEP strategies (24): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T10:31:13.289927-04:00","date":"2026-09-10","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":104.4,"phases_s":{"reconcile":0.85,"cancel":0.09,"manage":19.44,"protective_stops":2.85,"scan":45.66,"entries":19.69,"reconcile2":0.37},"signals":372,"placed":0,"equity":1001622.72,"open_positions":39,"pending_orders":8,"open_lots":126,"submitted_today":60,"filled_today":107,"unattributed_contracts":0,"top_signals":["S401:TSLA","S359:TSLA","S361:TSLA","S362:TSLA","S363:TSLA","S364:TSLA","S365:TSLA","S366:TSLA"],"github_run":"9598","github_run_id":"34489461789","status":"ok","data_quality":{"clean":{"n":1133,"win":49.6,"med":-2.7,"avg":43.23,"pnl":15705.59},"tainted":{"n":1818,"win":33.39,"med":-39.0,"avg":12.01,"pnl":-9008.84},"keep_only":{"n":628,"win":63.22,"med":51.39,"avg":68.43,"pnl":11077.45},"keep_only_recent":{"n":420,"win":60.24,"med":53.33,"avg":79.36,"pnl":5820.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
14:31:08  INFO      Mode: exits
14:31:08  INFO        Daily log -> logs/daily/2026-09-10.md
14:31:08  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
14:31:09  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T10:31:09.857171-04:00 share=25% ===
2026-09-10 10:31:09,857 INFO === options_live_micro LIVE 2026-09-10T10:31:09.857171-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 10:31:10,001 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-10 10:31:10,117 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-10 10:31:10,194 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (200 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 253 | 14 |
| S164 | 275 | 16 |
| S165 | 1711 | 28 |
| S166 | 135 | 9 |
| S167 | 269 | 16 |
| S168 | 200 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |    4 |    4 |    0 |    0 |    4 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    14 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1201 | WARN | <<<
| Missing exit records (post) |  1186 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   126 | INFO |
| Total closed lots           |  2122 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1133 med=-2.7% | TAINTED n=1818 med=-39.0% | KEEP-only n=628 med=+51.4% | KILL=18 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T143612Z

- UTC timestamp: `20260910T143612Z`
- GitHub run: [#9599](https://github.com/28twagg-ops/TradingBot/actions/runs/34490007572)
- Run id: `34490007572`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`101s`
- Full logs: `logs/action_runs/20260910T143612Z_live_bot.log`, `logs/action_runs/20260910T143612Z_live_options.log`, `logs/action_runs/20260910T143612Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1136 | 49.6 | -2.6 | +43.2 | $+15,762 |
| TAINTED | 1818 | 33.4 | -39.0 | +12.0 | $-9,009 |
| KEEP-only | 630 | 63.2 | +51.4 | +68.2 | $+11,086 |
| KEEP-only recent | 422 | 60.2 | +53.3 | +78.9 | $+5,829 |

- KEEP strategies (24): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T10:36:18.657398-04:00","date":"2026-09-10","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":92.5,"phases_s":{"reconcile":0.49,"cancel":0.13,"manage":16.98,"protective_stops":3.65,"scan":35.54,"entries":24.72,"reconcile2":0.56},"signals":372,"placed":0,"equity":1002123.7,"open_positions":39,"pending_orders":8,"open_lots":123,"submitted_today":60,"filled_today":107,"unattributed_contracts":0,"top_signals":["S401:TSLA","S359:TSLA","S361:TSLA","S362:TSLA","S363:TSLA","S364:TSLA","S365:TSLA","S366:TSLA"],"github_run":"9599","github_run_id":"34490007572","status":"ok","data_quality":{"clean":{"n":1136,"win":49.65,"med":-2.6,"avg":43.17,"pnl":15761.59},"tainted":{"n":1818,"win":33.39,"med":-39.0,"avg":12.01,"pnl":-9008.84},"keep_only":{"n":630,"win":63.17,"med":51.39,"avg":68.18,"pnl":11086.45},"keep_only_recent":{"n":422,"win":60.19,"med":53.33,"avg":78.95,"pnl":5829.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
14:36:13  INFO      Mode: exits
14:36:14  INFO        Daily log -> logs/daily/2026-09-10.md
14:36:14  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
14:36:14  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T10:36:15.570353-04:00 share=25% ===
2026-09-10 10:36:15,570 INFO === options_live_micro LIVE 2026-09-10T10:36:15.570353-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 10:36:15,790 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-10 10:36:15,958 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-10 10:36:16,070 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (194 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 253 | 14 |
| S164 | 275 | 16 |
| S165 | 1711 | 28 |
| S166 | 135 | 9 |
| S167 | 269 | 16 |
| S168 | 200 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |    4 |    4 |    0 |    0 |    4 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    14 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1201 | WARN | <<<
| Missing exit records (post) |  1186 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   123 | INFO |
| Total closed lots           |  2125 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1136 med=-2.6% | TAINTED n=1818 med=-39.0% | KEEP-only n=630 med=+51.4% | KILL=18 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T144105Z

- UTC timestamp: `20260910T144105Z`
- GitHub run: [#9600](https://github.com/28twagg-ops/TradingBot/actions/runs/34490551388)
- Run id: `34490551388`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`104s`
- Full logs: `logs/action_runs/20260910T144105Z_live_bot.log`, `logs/action_runs/20260910T144105Z_live_options.log`, `logs/action_runs/20260910T144105Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1138 | 49.6 | -2.6 | +43.1 | $+15,772 |
| TAINTED | 1819 | 33.4 | -39.0 | +12.0 | $-9,046 |
| KEEP-only | 632 | 63.1 | +51.4 | +67.9 | $+11,096 |
| KEEP-only recent | 424 | 60.1 | +53.3 | +78.5 | $+5,839 |

- KEEP strategies (24): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T10:41:11.089706-04:00","date":"2026-09-10","mode":"entry+manage","header":"entry+manage (2 new)","elapsed_s":92.5,"phases_s":{"reconcile":0.36,"cancel":0.05,"manage":13.31,"protective_stops":1.48,"scan":45.92,"entries":10.47,"reconcile2":0.44},"signals":372,"placed":2,"equity":1002122.14,"open_positions":40,"pending_orders":8,"open_lots":123,"submitted_today":62,"filled_today":109,"unattributed_contracts":0,"top_signals":["S401:TSLA","S359:TSLA","S361:TSLA","S362:TSLA","S363:TSLA","S364:TSLA","S365:TSLA","S366:TSLA"],"github_run":"9600","github_run_id":"34490551388","status":"ok","data_quality":{"clean":{"n":1138,"win":49.65,"med":-2.6,"avg":43.08,"pnl":15771.59},"tainted":{"n":1819,"win":33.37,"med":-39.02,"avg":11.97,"pnl":-9045.84},"keep_only":{"n":632,"win":63.13,"med":51.39,"avg":67.94,"pnl":11096.45},"keep_only_recent":{"n":424,"win":60.14,"med":53.33,"avg":78.53,"pnl":5839.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
14:41:06  INFO      Mode: exits
14:41:07  INFO        Daily log -> logs/daily/2026-09-10.md
14:41:07  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
14:41:07  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T10:41:08.090465-04:00 share=25% ===
2026-09-10 10:41:08,090 INFO === options_live_micro LIVE 2026-09-10T10:41:08.090465-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 10:41:08,188 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-10 10:41:08,267 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-10 10:41:08,317 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (193 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 253 | 14 |
| S164 | 275 | 16 |
| S165 | 1711 | 28 |
| S166 | 135 | 9 |
| S167 | 269 | 16 |
| S168 | 200 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |    4 |    4 |    0 |    0 |    4 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    14 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1201 | WARN | <<<
| Missing exit records (post) |  1186 | WARN | <<<
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |   123 | INFO |
| Total closed lots           |  2128 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1138 med=-2.6% | TAINTED n=1819 med=-39.0% | KEEP-only n=632 med=+51.4% | KILL=18 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T144606Z

- UTC timestamp: `20260910T144606Z`
- GitHub run: [#9601](https://github.com/28twagg-ops/TradingBot/actions/runs/34491107744)
- Run id: `34491107744`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`233s`
- Full logs: `logs/action_runs/20260910T144606Z_live_bot.log`, `logs/action_runs/20260910T144606Z_live_options.log`, `logs/action_runs/20260910T144606Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1138 | 49.6 | -2.6 | +43.1 | $+15,772 |
| TAINTED | 1819 | 33.4 | -39.0 | +12.0 | $-9,046 |
| KEEP-only | 632 | 63.1 | +51.4 | +67.9 | $+11,096 |
| KEEP-only recent | 424 | 60.1 | +53.3 | +78.5 | $+5,839 |

- KEEP strategies (24): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T10:46:11.292217-04:00","date":"2026-09-10","mode":"entry+manage","header":"entry+manage (48 new)","elapsed_s":221.2,"phases_s":{"reconcile":0.2,"cancel":0.03,"manage":14.96,"protective_stops":0.57,"scan":53.36,"entries":128.67,"reconcile2":1.05},"signals":372,"placed":48,"equity":1001941.68,"open_positions":44,"pending_orders":37,"open_lots":140,"submitted_today":110,"filled_today":128,"unattributed_contracts":0,"top_signals":["S401:TSLA","S359:TSLA","S361:TSLA","S362:TSLA","S363:TSLA","S364:TSLA","S365:TSLA","S366:TSLA"],"github_run":"9601","github_run_id":"34491107744","status":"ok","data_quality":{"clean":{"n":1138,"win":49.65,"med":-2.6,"avg":43.08,"pnl":15771.59},"tainted":{"n":1819,"win":33.37,"med":-39.02,"avg":11.97,"pnl":-9045.84},"keep_only":{"n":632,"win":63.13,"med":51.39,"avg":67.94,"pnl":11096.45},"keep_only_recent":{"n":424,"win":60.14,"med":53.33,"avg":78.53,"pnl":5839.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
14:46:07  INFO      Mode: exits
14:46:07  INFO        Daily log -> logs/daily/2026-09-10.md
14:46:07  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
14:46:07  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T10:46:08.260816-04:00 share=25% ===
2026-09-10 10:46:08,260 INFO === options_live_micro LIVE 2026-09-10T10:46:08.260816-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 10:46:08,301 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-10 10:46:08,322 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-10 10:46:08,334 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (276 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 255 | 14 |
| S164 | 279 | 18 |
| S165 | 1715 | 30 |
| S166 | 135 | 9 |
| S167 | 273 | 17 |
| S168 | 202 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |    6 |    8 |    4 |    0 |    8 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    30 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1201 | WARN | <<<
| Missing exit records (post) |  1186 | WARN | <<<
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |   140 | INFO |
| Total closed lots           |  2128 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1138 med=-2.6% | TAINTED n=1819 med=-39.0% | KEEP-only n=632 med=+51.4% | KILL=18 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T145122Z

- UTC timestamp: `20260910T145122Z`
- GitHub run: [#9602](https://github.com/28twagg-ops/TradingBot/actions/runs/34491655399)
- Run id: `34491655399`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`229s`
- Full logs: `logs/action_runs/20260910T145122Z_live_bot.log`, `logs/action_runs/20260910T145122Z_live_options.log`, `logs/action_runs/20260910T145122Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1138 | 49.6 | -2.6 | +43.1 | $+15,772 |
| TAINTED | 1821 | 33.3 | -39.0 | +11.9 | $-9,102 |
| KEEP-only | 632 | 63.1 | +51.4 | +67.9 | $+11,096 |
| KEEP-only recent | 424 | 60.1 | +53.3 | +78.5 | $+5,839 |

- KEEP strategies (24): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T10:51:29.093344-04:00","date":"2026-09-10","mode":"entry+manage","header":"entry+manage (6 new)","elapsed_s":216.5,"phases_s":{"reconcile":1.52,"cancel":0.15,"manage":21.28,"protective_stops":4.83,"scan":54.52,"entries":108.71,"reconcile2":0.83},"signals":372,"placed":6,"equity":1001613.88,"open_positions":49,"pending_orders":9,"open_lots":150,"submitted_today":68,"filled_today":138,"unattributed_contracts":0,"top_signals":["S401:TSLA","S359:TSLA","S361:TSLA","S362:TSLA","S363:TSLA","S364:TSLA","S365:TSLA","S366:TSLA"],"github_run":"9602","github_run_id":"34491655399","status":"ok","data_quality":{"clean":{"n":1138,"win":49.65,"med":-2.6,"avg":43.08,"pnl":15771.59},"tainted":{"n":1821,"win":33.33,"med":-39.02,"avg":11.9,"pnl":-9101.84},"keep_only":{"n":632,"win":63.13,"med":51.39,"avg":67.94,"pnl":11096.45},"keep_only_recent":{"n":424,"win":60.14,"med":53.33,"avg":78.53,"pnl":5839.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
14:51:22  INFO      Mode: exits
14:51:23  INFO        Daily log -> logs/daily/2026-09-10.md
14:51:23  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
14:51:24  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:51 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T10:51:25.120086-04:00 share=25% ===
2026-09-10 10:51:25,120 INFO === options_live_micro LIVE 2026-09-10T10:51:25.120086-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 10:51:25,351 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-10 10:51:25,576 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-10 10:51:25,710 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (206 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 253 | 14 |
| S164 | 277 | 16 |
| S165 | 1713 | 28 |
| S166 | 135 | 9 |
| S167 | 271 | 16 |
| S168 | 200 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |    4 |    6 |    2 |    0 |    6 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    20 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1201 | WARN | <<<
| Missing exit records (post) |  1186 | WARN | <<<
| State/ledger mismatches     |    10 | WARN | <<<
| Total open lots             |   150 | INFO |
| Total closed lots           |  2130 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1138 med=-2.6% | TAINTED n=1821 med=-39.0% | KEEP-only n=632 med=+51.4% | KILL=18 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T145634Z

- UTC timestamp: `20260910T145634Z`
- GitHub run: [#9603](https://github.com/28twagg-ops/TradingBot/actions/runs/34492202743)
- Run id: `34492202743`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`144s`
- Full logs: `logs/action_runs/20260910T145634Z_live_bot.log`, `logs/action_runs/20260910T145634Z_live_options.log`, `logs/action_runs/20260910T145634Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1138 | 49.6 | -2.6 | +43.1 | $+15,772 |
| TAINTED | 1821 | 33.3 | -39.0 | +11.9 | $-9,102 |
| KEEP-only | 632 | 63.1 | +51.4 | +67.9 | $+11,096 |
| KEEP-only recent | 424 | 60.1 | +53.3 | +78.5 | $+5,839 |

- KEEP strategies (24): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T10:56:42.756277-04:00","date":"2026-09-10","mode":"entry+manage","header":"entry+manage (1 new)","elapsed_s":131.6,"phases_s":{"reconcile":1.09,"cancel":0.15,"manage":24.6,"protective_stops":4.96,"scan":53.86,"entries":36.95,"reconcile2":0.67},"signals":372,"placed":1,"equity":1001834.67,"open_positions":50,"pending_orders":32,"open_lots":151,"submitted_today":111,"filled_today":139,"unattributed_contracts":0,"top_signals":["S401:TSLA","S359:TSLA","S361:TSLA","S362:TSLA","S363:TSLA","S364:TSLA","S365:TSLA","S366:TSLA"],"github_run":"9603","github_run_id":"34492202743","status":"ok","data_quality":{"clean":{"n":1138,"win":49.65,"med":-2.6,"avg":43.08,"pnl":15771.59},"tainted":{"n":1821,"win":33.33,"med":-39.02,"avg":11.9,"pnl":-9101.84},"keep_only":{"n":632,"win":63.13,"med":51.39,"avg":67.94,"pnl":11096.45},"keep_only_recent":{"n":424,"win":60.14,"med":53.33,"avg":78.53,"pnl":5839.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
14:56:35  INFO      Mode: exits
14:56:36  INFO        Daily log -> logs/daily/2026-09-10.md
14:56:36  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
14:56:37  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:56 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T10:56:38.785524-04:00 share=25% ===
2026-09-10 10:56:38,785 INFO === options_live_micro LIVE 2026-09-10T10:56:38.785524-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 10:56:39,017 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-10 10:56:39,259 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-10 10:56:39,402 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (201 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 255 | 14 |
| S164 | 279 | 18 |
| S165 | 1715 | 30 |
| S166 | 135 | 9 |
| S167 | 273 | 17 |
| S168 | 202 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |    6 |    8 |    4 |    0 |    8 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    30 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1201 | WARN | <<<
| Missing exit records (post) |  1186 | WARN | <<<
| State/ledger mismatches     |    10 | WARN | <<<
| Total open lots             |   151 | INFO |
| Total closed lots           |  2130 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1138 med=-2.6% | TAINTED n=1821 med=-39.0% | KEEP-only n=632 med=+51.4% | KILL=18 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T150108Z

- UTC timestamp: `20260910T150108Z`
- GitHub run: [#9604](https://github.com/28twagg-ops/TradingBot/actions/runs/34492745944)
- Run id: `34492745944`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`142s`
- Full logs: `logs/action_runs/20260910T150108Z_live_bot.log`, `logs/action_runs/20260910T150108Z_live_options.log`, `logs/action_runs/20260910T150108Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1140 | 49.6 | -2.7 | +42.9 | $+15,748 |
| TAINTED | 1821 | 33.3 | -39.0 | +11.9 | $-9,102 |
| KEEP-only | 633 | 63.0 | +51.4 | +67.7 | $+11,090 |
| KEEP-only recent | 425 | 60.0 | +53.3 | +78.1 | $+5,833 |

- KEEP strategies (24): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T11:01:16.309217-04:00","date":"2026-09-10","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":130.2,"phases_s":{"reconcile":0.63,"cancel":0.11,"manage":27.53,"protective_stops":4.14,"scan":53.23,"entries":24.43,"reconcile2":0.44},"signals":372,"placed":0,"equity":1001538.49,"open_positions":50,"pending_orders":28,"open_lots":154,"submitted_today":111,"filled_today":144,"unattributed_contracts":0,"top_signals":["S401:TSLA","S359:TSLA","S361:TSLA","S362:TSLA","S363:TSLA","S364:TSLA","S365:TSLA","S366:TSLA"],"github_run":"9604","github_run_id":"34492745944","status":"ok","data_quality":{"clean":{"n":1140,"win":49.56,"med":-2.7,"avg":42.89,"pnl":15747.59},"tainted":{"n":1821,"win":33.33,"med":-39.02,"avg":11.9,"pnl":-9101.84},"keep_only":{"n":633,"win":63.03,"med":51.39,"avg":67.7,"pnl":11090.45},"keep_only_recent":{"n":425,"win":60.0,"med":53.33,"avg":78.15,"pnl":5833.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
15:01:11  INFO      Mode: exits
15:01:11  INFO        Daily log -> logs/daily/2026-09-10.md
15:01:11  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
15:01:12  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T11:01:13.054018-04:00 share=25% ===
2026-09-10 11:01:13,054 INFO === options_live_micro LIVE 2026-09-10T11:01:13.054018-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 11:01:13,189 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-10 11:01:13,295 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-10 11:01:13,364 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (204 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 255 | 14 |
| S164 | 279 | 18 |
| S165 | 1715 | 30 |
| S166 | 135 | 9 |
| S167 | 273 | 17 |
| S168 | 202 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |    6 |    8 |    4 |    0 |    8 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    30 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1201 | WARN | <<<
| Missing exit records (post) |  1186 | WARN | <<<
| State/ledger mismatches     |     9 | WARN | <<<
| Total open lots             |   154 | INFO |
| Total closed lots           |  2131 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1140 med=-2.7% | TAINTED n=1821 med=-39.0% | KEEP-only n=633 med=+51.4% | KILL=18 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T150729Z

- UTC timestamp: `20260910T150729Z`
- GitHub run: [#9605](https://github.com/28twagg-ops/TradingBot/actions/runs/34493307439)
- Run id: `34493307439`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`141s`
- Full logs: `logs/action_runs/20260910T150729Z_live_bot.log`, `logs/action_runs/20260910T150729Z_live_options.log`, `logs/action_runs/20260910T150729Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1143 | 49.6 | -2.7 | +42.8 | $+15,789 |
| TAINTED | 1821 | 33.3 | -39.0 | +11.9 | $-9,102 |
| KEEP-only | 635 | 63.1 | +51.4 | +67.6 | $+11,142 |
| KEEP-only recent | 427 | 60.2 | +53.3 | +78.0 | $+5,885 |

- KEEP strategies (24): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T11:07:36.194752-04:00","date":"2026-09-10","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":128.2,"phases_s":{"reconcile":0.74,"cancel":0.12,"manage":24.8,"protective_stops":5.07,"scan":52.0,"entries":30.52,"reconcile2":0.46},"signals":372,"placed":0,"equity":1001135.75,"open_positions":52,"pending_orders":22,"open_lots":157,"submitted_today":111,"filled_today":150,"unattributed_contracts":0,"top_signals":["S401:TSLA","S359:TSLA","S361:TSLA","S362:TSLA","S363:TSLA","S364:TSLA","S365:TSLA","S366:TSLA"],"github_run":"9605","github_run_id":"34493307439","status":"ok","data_quality":{"clean":{"n":1143,"win":49.61,"med":-2.7,"avg":42.83,"pnl":15788.59},"tainted":{"n":1821,"win":33.33,"med":-39.02,"avg":11.9,"pnl":-9101.84},"keep_only":{"n":635,"win":63.15,"med":51.39,"avg":67.65,"pnl":11142.45},"keep_only_recent":{"n":427,"win":60.19,"med":53.33,"avg":78.02,"pnl":5885.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
15:07:30  INFO      Mode: exits
15:07:30  INFO        Daily log -> logs/daily/2026-09-10.md
15:07:30  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
15:07:31  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:07 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T11:07:32.141136-04:00 share=25% ===
2026-09-10 11:07:32,141 INFO === options_live_micro LIVE 2026-09-10T11:07:32.141136-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 11:07:32,360 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-10 11:07:32,578 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-10 11:07:32,695 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (202 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 255 | 14 |
| S164 | 279 | 18 |
| S165 | 1715 | 30 |
| S166 | 135 | 9 |
| S167 | 273 | 17 |
| S168 | 202 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |    6 |    8 |    4 |    0 |    8 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    30 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1201 | WARN | <<<
| Missing exit records (post) |  1186 | WARN | <<<
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |   157 | INFO |
| Total closed lots           |  2133 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1143 med=-2.7% | TAINTED n=1821 med=-39.0% | KEEP-only n=635 med=+51.4% | KILL=18 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T151112Z

- UTC timestamp: `20260910T151112Z`
- GitHub run: [#9606](https://github.com/28twagg-ops/TradingBot/actions/runs/34493837064)
- Run id: `34493837064`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`144s`
- Full logs: `logs/action_runs/20260910T151112Z_live_bot.log`, `logs/action_runs/20260910T151112Z_live_options.log`, `logs/action_runs/20260910T151112Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1141 | 49.6 | -2.7 | +42.9 | $+15,773 |
| TAINTED | 1823 | 33.4 | -39.0 | +11.9 | $-9,086 |
| KEEP-only | 634 | 63.1 | +51.2 | +67.7 | $+11,115 |
| KEEP-only recent | 426 | 60.1 | +53.3 | +78.1 | $+5,858 |

- KEEP strategies (24): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T11:11:20.772262-04:00","date":"2026-09-10","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":132.2,"phases_s":{"reconcile":0.93,"cancel":0.15,"manage":25.13,"protective_stops":5.16,"scan":54.39,"entries":33.89,"reconcile2":0.45},"signals":372,"placed":0,"equity":1001155.21,"open_positions":52,"pending_orders":22,"open_lots":157,"submitted_today":111,"filled_today":150,"unattributed_contracts":0,"top_signals":["S401:TSLA","S359:TSLA","S361:TSLA","S362:TSLA","S363:TSLA","S364:TSLA","S365:TSLA","S366:TSLA"],"github_run":"9606","github_run_id":"34493837064","status":"ok","data_quality":{"clean":{"n":1141,"win":49.61,"med":-2.7,"avg":42.9,"pnl":15772.59},"tainted":{"n":1823,"win":33.35,"med":-39.02,"avg":11.89,"pnl":-9085.84},"keep_only":{"n":634,"win":63.09,"med":51.18,"avg":67.67,"pnl":11115.45},"keep_only_recent":{"n":426,"win":60.09,"med":53.33,"avg":78.08,"pnl":5858.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
15:11:13  INFO      Mode: exits
15:11:14  INFO        Daily log -> logs/daily/2026-09-10.md
15:11:14  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
15:11:15  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T11:11:16.764471-04:00 share=25% ===
2026-09-10 11:11:16,764 INFO === options_live_micro LIVE 2026-09-10T11:11:16.764471-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 11:11:17,069 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-10 11:11:17,385 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-10 11:11:17,524 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (200 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 255 | 14 |
| S164 | 279 | 18 |
| S165 | 1715 | 30 |
| S166 | 135 | 9 |
| S167 | 273 | 17 |
| S168 | 202 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |    6 |    8 |    4 |    0 |    8 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    30 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1201 | WARN | <<<
| Missing exit records (post) |  1186 | WARN | <<<
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |   157 | INFO |
| Total closed lots           |  2133 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1141 med=-2.7% | TAINTED n=1823 med=-39.0% | KEEP-only n=634 med=+51.2% | KILL=18 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T151605Z

- UTC timestamp: `20260910T151605Z`
- GitHub run: [#9607](https://github.com/28twagg-ops/TradingBot/actions/runs/34494378111)
- Run id: `34494378111`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`148s`
- Full logs: `logs/action_runs/20260910T151605Z_live_bot.log`, `logs/action_runs/20260910T151605Z_live_options.log`, `logs/action_runs/20260910T151605Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1142 | 49.6 | -2.7 | +42.8 | $+15,747 |
| TAINTED | 1823 | 33.4 | -39.0 | +11.9 | $-9,086 |
| KEEP-only | 634 | 63.1 | +51.2 | +67.7 | $+11,115 |
| KEEP-only recent | 426 | 60.1 | +53.3 | +78.1 | $+5,858 |

- KEEP strategies (24): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T11:16:13.139808-04:00","date":"2026-09-10","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":135.5,"phases_s":{"reconcile":0.62,"cancel":0.16,"manage":28.04,"protective_stops":6.03,"scan":54.45,"entries":35.68,"reconcile2":1.13},"signals":372,"placed":0,"equity":1000969.21,"open_positions":52,"pending_orders":10,"open_lots":168,"submitted_today":111,"filled_today":162,"unattributed_contracts":0,"top_signals":["S401:TSLA","S359:TSLA","S361:TSLA","S362:TSLA","S363:TSLA","S364:TSLA","S365:TSLA","S366:TSLA"],"github_run":"9607","github_run_id":"34494378111","status":"ok","data_quality":{"clean":{"n":1142,"win":49.56,"med":-2.7,"avg":42.82,"pnl":15746.59},"tainted":{"n":1823,"win":33.35,"med":-39.02,"avg":11.89,"pnl":-9085.84},"keep_only":{"n":634,"win":63.09,"med":51.18,"avg":67.67,"pnl":11115.45},"keep_only_recent":{"n":426,"win":60.09,"med":53.33,"avg":78.08,"pnl":5858.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
15:16:06  INFO      Mode: exits
15:16:07  INFO        Daily log -> logs/daily/2026-09-10.md
15:16:07  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
15:16:08  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T11:16:08.973392-04:00 share=25% ===
2026-09-10 11:16:08,973 INFO === options_live_micro LIVE 2026-09-10T11:16:08.973392-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 11:16:09,196 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-10 11:16:09,399 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-10 11:16:09,534 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (201 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 257 | 14 |
| S164 | 279 | 18 |
| S165 | 1715 | 30 |
| S166 | 135 | 9 |
| S167 | 273 | 17 |
| S168 | 204 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |    8 |    8 |    4 |    0 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    34 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1201 | WARN | <<<
| Missing exit records (post) |  1186 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   168 | INFO |
| Total closed lots           |  2133 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1142 med=-2.7% | TAINTED n=1823 med=-39.0% | KEEP-only n=634 med=+51.2% | KILL=18 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T152115Z

- UTC timestamp: `20260910T152115Z`
- GitHub run: [#9608](https://github.com/28twagg-ops/TradingBot/actions/runs/34494946506)
- Run id: `34494946506`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`212s`
- Full logs: `logs/action_runs/20260910T152115Z_live_bot.log`, `logs/action_runs/20260910T152115Z_live_options.log`, `logs/action_runs/20260910T152115Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1144 | 49.5 | -5.2 | +42.7 | $+15,721 |
| TAINTED | 1825 | 33.4 | -39.0 | +12.0 | $-9,081 |
| KEEP-only | 635 | 63.0 | +51.0 | +67.5 | $+11,091 |
| KEEP-only recent | 427 | 60.0 | +53.3 | +77.8 | $+5,834 |

- KEEP strategies (24): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T11:21:21.486509-04:00","date":"2026-09-10","mode":"entry+manage","header":"entry+manage (45 new)","elapsed_s":200.2,"phases_s":{"reconcile":0.15,"cancel":0.03,"manage":13.12,"protective_stops":0.81,"scan":51.44,"entries":109.67,"reconcile2":2.34},"signals":372,"placed":45,"equity":1000565.83,"open_positions":55,"pending_orders":12,"open_lots":203,"submitted_today":156,"filled_today":205,"unattributed_contracts":0,"top_signals":["S401:TSLA","S359:TSLA","S361:TSLA","S362:TSLA","S363:TSLA","S364:TSLA","S365:TSLA","S366:TSLA"],"github_run":"9608","github_run_id":"34494946506","status":"ok","data_quality":{"clean":{"n":1144,"win":49.48,"med":-5.2,"avg":42.66,"pnl":15720.59},"tainted":{"n":1825,"win":33.37,"med":-38.98,"avg":12.01,"pnl":-9080.84},"keep_only":{"n":635,"win":62.99,"med":50.98,"avg":67.51,"pnl":11091.45},"keep_only_recent":{"n":427,"win":59.95,"med":53.33,"avg":77.81,"pnl":5834.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
15:21:16  INFO      Mode: exits
15:21:17  INFO        Daily log -> logs/daily/2026-09-10.md
15:21:17  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
15:21:17  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T11:21:18.061710-04:00 share=25% ===
2026-09-10 11:21:18,061 INFO === options_live_micro LIVE 2026-09-10T11:21:18.061710-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 11:21:18,105 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-10 11:21:18,300 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-10 11:21:18,314 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (241 earlier lines - see full log file)
| w4     |    7 |    5 |   11 |    3 |    6 |    8 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    49 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 261 | 14 |
| S164 | 283 | 19 |
| S165 | 1719 | 31 |
| S166 | 135 | 9 |
| S167 | 277 | 18 |
| S168 | 208 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   12 |   12 |    8 |    0 |   12 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    54 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     9 | WARN | <<<
| Total open lots             |   203 | INFO |
| Total closed lots           |  2137 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1144 med=-5.2% | TAINTED n=1825 med=-39.0% | KEEP-only n=635 med=+51.0% | KILL=18 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T152620Z

- UTC timestamp: `20260910T152620Z`
- GitHub run: [#9609](https://github.com/28twagg-ops/TradingBot/actions/runs/34495491644)
- Run id: `34495491644`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`177s`
- Full logs: `logs/action_runs/20260910T152620Z_live_bot.log`, `logs/action_runs/20260910T152620Z_live_options.log`, `logs/action_runs/20260910T152620Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1143 | 49.5 | -2.7 | +42.7 | $+15,734 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 634 | 63.1 | +51.2 | +67.7 | $+11,115 |
| KEEP-only recent | 426 | 60.1 | +53.3 | +78.1 | $+5,858 |

- KEEP strategies (24): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T11:26:29.564346-04:00","date":"2026-09-10","mode":"entry+manage","header":"entry+manage (6 new)","elapsed_s":163.8,"phases_s":{"reconcile":2.74,"cancel":0.16,"manage":30.31,"protective_stops":6.34,"scan":52.56,"entries":45.26,"reconcile2":0.81},"signals":372,"placed":6,"equity":1000514.35,"open_positions":58,"pending_orders":11,"open_lots":207,"submitted_today":117,"filled_today":210,"unattributed_contracts":0,"top_signals":["S401:TSLA","S359:TSLA","S361:TSLA","S362:TSLA","S363:TSLA","S364:TSLA","S365:TSLA","S366:TSLA"],"github_run":"9609","github_run_id":"34495491644","status":"ok","data_quality":{"clean":{"n":1143,"win":49.52,"med":-2.7,"avg":42.74,"pnl":15733.59},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":634,"win":63.09,"med":51.18,"avg":67.67,"pnl":11115.45},"keep_only_recent":{"n":426,"win":60.09,"med":53.33,"avg":78.08,"pnl":5858.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
15:26:21  INFO      Mode: exits
15:26:23  INFO        Daily log -> logs/daily/2026-09-10.md
15:26:23  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
15:26:23  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T11:26:24.447021-04:00 share=25% ===
2026-09-10 11:26:24,447 INFO === options_live_micro LIVE 2026-09-10T11:26:24.447021-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 11:26:24,690 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-10 11:26:24,906 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-10 11:26:25,050 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (214 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     9 | WARN | <<<
| Total open lots             |   207 | INFO |
| Total closed lots           |  2137 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1143 med=-2.7% | TAINTED n=1827 med=-38.8% | KEEP-only n=634 med=+51.2% | KILL=18 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T153118Z

- UTC timestamp: `20260910T153118Z`
- GitHub run: [#9610](https://github.com/28twagg-ops/TradingBot/actions/runs/34496035079)
- Run id: `34496035079`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`149s`
- Full logs: `logs/action_runs/20260910T153118Z_live_bot.log`, `logs/action_runs/20260910T153118Z_live_options.log`, `logs/action_runs/20260910T153118Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1145 | 49.5 | -2.7 | +42.7 | $+15,748 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 635 | 63.1 | +51.4 | +67.7 | $+11,152 |
| KEEP-only recent | 427 | 60.2 | +53.3 | +78.1 | $+5,895 |

- KEEP strategies (24): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T11:31:24.883425-04:00","date":"2026-09-10","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":136.9,"phases_s":{"reconcile":0.57,"cancel":0.08,"manage":26.91,"protective_stops":3.93,"scan":45.56,"entries":34.05,"reconcile2":0.52},"signals":372,"placed":0,"equity":1000195.09,"open_positions":58,"pending_orders":10,"open_lots":203,"submitted_today":117,"filled_today":213,"unattributed_contracts":0,"top_signals":["S401:TSLA","S359:TSLA","S361:TSLA","S362:TSLA","S363:TSLA","S364:TSLA","S365:TSLA","S366:TSLA"],"github_run":"9610","github_run_id":"34496035079","status":"ok","data_quality":{"clean":{"n":1145,"win":49.52,"med":-2.7,"avg":42.69,"pnl":15747.59},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":635,"win":63.15,"med":51.39,"avg":67.68,"pnl":11152.45},"keep_only_recent":{"n":427,"win":60.19,"med":53.33,"avg":78.07,"pnl":5895.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
15:31:19  INFO      Mode: exits
15:31:20  INFO        Daily log -> logs/daily/2026-09-10.md
15:31:20  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
15:31:20  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T11:31:21.450103-04:00 share=25% ===
2026-09-10 11:31:21,450 INFO === options_live_micro LIVE 2026-09-10T11:31:21.450103-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 11:31:21,589 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-10 11:31:21,705 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-10 11:31:21,781 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (208 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     9 | WARN | <<<
| Total open lots             |   203 | INFO |
| Total closed lots           |  2139 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1145 med=-2.7% | TAINTED n=1827 med=-38.8% | KEEP-only n=635 med=+51.4% | KILL=18 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T153609Z

- UTC timestamp: `20260910T153609Z`
- GitHub run: [#9611](https://github.com/28twagg-ops/TradingBot/actions/runs/34496587388)
- Run id: `34496587388`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`46s`
- Full logs: `logs/action_runs/20260910T153609Z_live_bot.log`, `logs/action_runs/20260910T153609Z_live_options.log`, `logs/action_runs/20260910T153609Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1145 | 49.5 | -2.7 | +42.7 | $+15,748 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 635 | 63.1 | +51.4 | +67.7 | $+11,152 |
| KEEP-only recent | 427 | 60.2 | +53.3 | +78.1 | $+5,895 |

- KEEP strategies (24): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T11:36:15.872762-04:00","date":"2026-09-10","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":38.8,"phases_s":{"reconcile":0.52,"cancel":1.01,"manage":30.75,"protective_stops":5.93},"signals":0,"placed":0,"equity":1000434.93,"open_positions":58,"pending_orders":10,"open_lots":203,"submitted_today":117,"filled_today":213,"unattributed_contracts":0,"top_signals":[],"github_run":"9611","github_run_id":"34496587388","status":"ok","data_quality":{"clean":{"n":1145,"win":49.52,"med":-2.7,"avg":42.69,"pnl":15747.59},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":635,"win":63.15,"med":51.39,"avg":67.68,"pnl":11152.45},"keep_only_recent":{"n":427,"win":60.19,"med":53.33,"avg":78.07,"pnl":5895.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
15:36:10  INFO      Mode: exits
15:36:11  INFO        Daily log -> logs/daily/2026-09-10.md
15:36:11  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
15:36:12  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T11:36:12.838649-04:00 share=25% ===
2026-09-10 11:36:12,838 INFO === options_live_micro LIVE 2026-09-10T11:36:12.838649-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 11:36:13,089 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: manage/exits only
2026-09-10 11:36:13,318 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-10 11:36:13,394 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (191 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     9 | WARN | <<<
| Total open lots             |   203 | INFO |
| Total closed lots           |  2139 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1145 med=-2.7% | TAINTED n=1827 med=-38.8% | KEEP-only n=635 med=+51.4% | KILL=18 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T154104Z

- UTC timestamp: `20260910T154104Z`
- GitHub run: [#9612](https://github.com/28twagg-ops/TradingBot/actions/runs/34497127594)
- Run id: `34497127594`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`39s`
- Full logs: `logs/action_runs/20260910T154104Z_live_bot.log`, `logs/action_runs/20260910T154104Z_live_options.log`, `logs/action_runs/20260910T154104Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1145 | 49.5 | -2.7 | +42.7 | $+15,748 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 635 | 63.1 | +51.4 | +67.7 | $+11,152 |
| KEEP-only recent | 427 | 60.2 | +53.3 | +78.1 | $+5,895 |

- KEEP strategies (24): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T11:41:11.047561-04:00","date":"2026-09-10","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":27.7,"phases_s":{"reconcile":0.26,"cancel":0.1,"manage":24.54,"protective_stops":2.23},"signals":0,"placed":0,"equity":1000304.91,"open_positions":57,"pending_orders":0,"open_lots":202,"submitted_today":117,"filled_today":213,"unattributed_contracts":0,"top_signals":[],"github_run":"9612","github_run_id":"34497127594","status":"ok","data_quality":{"clean":{"n":1145,"win":49.52,"med":-2.7,"avg":42.69,"pnl":15747.59},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":635,"win":63.15,"med":51.39,"avg":67.68,"pnl":11152.45},"keep_only_recent":{"n":427,"win":60.19,"med":53.33,"avg":78.07,"pnl":5895.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
15:41:05  INFO      Mode: exits
15:41:06  INFO        Daily log -> logs/daily/2026-09-10.md
15:41:06  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
15:41:06  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T11:41:07.335134-04:00 share=25% ===
2026-09-10 11:41:07,335 INFO === options_live_micro LIVE 2026-09-10T11:41:07.335134-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 11:41:07,474 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: manage/exits only
2026-09-10 11:41:07,587 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-10 11:41:07,625 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (178 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     9 | WARN | <<<
| Total open lots             |   202 | INFO |
| Total closed lots           |  2139 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1145 med=-2.7% | TAINTED n=1827 med=-38.8% | KEEP-only n=635 med=+51.4% | KILL=18 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T154603Z

- UTC timestamp: `20260910T154603Z`
- GitHub run: [#9613](https://github.com/28twagg-ops/TradingBot/actions/runs/34497671019)
- Run id: `34497671019`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`36s`
- Full logs: `logs/action_runs/20260910T154603Z_live_bot.log`, `logs/action_runs/20260910T154603Z_live_options.log`, `logs/action_runs/20260910T154603Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1145 | 49.5 | -2.7 | +42.7 | $+15,748 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 635 | 63.1 | +51.4 | +67.7 | $+11,152 |
| KEEP-only recent | 427 | 60.2 | +53.3 | +78.1 | $+5,895 |

- KEEP strategies (24): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T11:46:09.396782-04:00","date":"2026-09-10","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":23.9,"phases_s":{"reconcile":0.17,"cancel":0.05,"manage":22.14,"protective_stops":1.02},"signals":0,"placed":0,"equity":1000307.89,"open_positions":56,"pending_orders":0,"open_lots":201,"submitted_today":117,"filled_today":213,"unattributed_contracts":0,"top_signals":[],"github_run":"9613","github_run_id":"34497671019","status":"ok","data_quality":{"clean":{"n":1145,"win":49.52,"med":-2.7,"avg":42.69,"pnl":15747.59},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":635,"win":63.15,"med":51.39,"avg":67.68,"pnl":11152.45},"keep_only_recent":{"n":427,"win":60.19,"med":53.33,"avg":78.07,"pnl":5895.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
15:46:04  INFO      Mode: exits
15:46:05  INFO        Daily log -> logs/daily/2026-09-10.md
15:46:05  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
15:46:05  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T11:46:06.133455-04:00 share=25% ===
2026-09-10 11:46:06,133 INFO === options_live_micro LIVE 2026-09-10T11:46:06.133455-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 11:46:06,192 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: manage/exits only
2026-09-10 11:46:06,226 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-10 11:46:06,237 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (178 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     9 | WARN | <<<
| Total open lots             |   201 | INFO |
| Total closed lots           |  2139 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1145 med=-2.7% | TAINTED n=1827 med=-38.8% | KEEP-only n=635 med=+51.4% | KILL=18 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T155105Z

- UTC timestamp: `20260910T155105Z`
- GitHub run: [#9614](https://github.com/28twagg-ops/TradingBot/actions/runs/34498221571)
- Run id: `34498221571`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`35s`
- Full logs: `logs/action_runs/20260910T155105Z_live_bot.log`, `logs/action_runs/20260910T155105Z_live_options.log`, `logs/action_runs/20260910T155105Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1145 | 49.5 | -2.7 | +42.7 | $+15,748 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 635 | 63.1 | +51.4 | +67.7 | $+11,152 |
| KEEP-only recent | 427 | 60.2 | +53.3 | +78.1 | $+5,895 |

- KEEP strategies (24): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T11:51:11.876950-04:00","date":"2026-09-10","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":23.5,"phases_s":{"reconcile":0.27,"cancel":0.09,"manage":20.31,"protective_stops":2.21},"signals":0,"placed":0,"equity":1000018.84,"open_positions":55,"pending_orders":0,"open_lots":199,"submitted_today":117,"filled_today":213,"unattributed_contracts":0,"top_signals":[],"github_run":"9614","github_run_id":"34498221571","status":"ok","data_quality":{"clean":{"n":1145,"win":49.52,"med":-2.7,"avg":42.69,"pnl":15747.59},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":635,"win":63.15,"med":51.39,"avg":67.68,"pnl":11152.45},"keep_only_recent":{"n":427,"win":60.19,"med":53.33,"avg":78.07,"pnl":5895.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
15:51:06  INFO      Mode: exits
15:51:06  INFO        Daily log -> logs/daily/2026-09-10.md
15:51:06  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
15:51:06  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:51 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T11:51:08.538804-04:00 share=25% ===
2026-09-10 11:51:08,538 INFO === options_live_micro LIVE 2026-09-10T11:51:08.538804-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 11:51:08,650 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: manage/exits only
2026-09-10 11:51:08,774 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-10 11:51:08,802 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (181 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     9 | WARN | <<<
| Total open lots             |   199 | INFO |
| Total closed lots           |  2139 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1145 med=-2.7% | TAINTED n=1827 med=-38.8% | KEEP-only n=635 med=+51.4% | KILL=18 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T155605Z

- UTC timestamp: `20260910T155605Z`
- GitHub run: [#9615](https://github.com/28twagg-ops/TradingBot/actions/runs/34498756266)
- Run id: `34498756266`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`31s`
- Full logs: `logs/action_runs/20260910T155605Z_live_bot.log`, `logs/action_runs/20260910T155605Z_live_options.log`, `logs/action_runs/20260910T155605Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1145 | 49.5 | -2.7 | +42.7 | $+15,748 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 635 | 63.1 | +51.4 | +67.7 | $+11,152 |
| KEEP-only recent | 427 | 60.2 | +53.3 | +78.1 | $+5,895 |

- KEEP strategies (24): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T11:56:10.879367-04:00","date":"2026-09-10","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":19.9,"phases_s":{"reconcile":0.14,"cancel":0.05,"manage":18.12,"protective_stops":1.05},"signals":0,"placed":0,"equity":999972.84,"open_positions":55,"pending_orders":0,"open_lots":199,"submitted_today":117,"filled_today":213,"unattributed_contracts":0,"top_signals":[],"github_run":"9615","github_run_id":"34498756266","status":"ok","data_quality":{"clean":{"n":1145,"win":49.52,"med":-2.7,"avg":42.69,"pnl":15747.59},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":635,"win":63.15,"med":51.39,"avg":67.68,"pnl":11152.45},"keep_only_recent":{"n":427,"win":60.19,"med":53.33,"avg":78.07,"pnl":5895.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
15:56:06  INFO      Mode: exits
15:56:06  INFO        Daily log -> logs/daily/2026-09-10.md
15:56:06  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
15:56:07  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:56 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T11:56:07.837074-04:00 share=25% ===
2026-09-10 11:56:07,837 INFO === options_live_micro LIVE 2026-09-10T11:56:07.837074-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 11:56:07,904 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: manage/exits only
2026-09-10 11:56:07,935 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-10 11:56:07,945 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (179 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     9 | WARN | <<<
| Total open lots             |   199 | INFO |
| Total closed lots           |  2139 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1145 med=-2.7% | TAINTED n=1827 med=-38.8% | KEEP-only n=635 med=+51.4% | KILL=18 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T160102Z

- UTC timestamp: `20260910T160102Z`
- GitHub run: [#9616](https://github.com/28twagg-ops/TradingBot/actions/runs/34499283906)
- Run id: `34499283906`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`51s`
- Full logs: `logs/action_runs/20260910T160102Z_live_bot.log`, `logs/action_runs/20260910T160102Z_live_options.log`, `logs/action_runs/20260910T160102Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1147 | 49.4 | -7.7 | +42.5 | $+15,718 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 636 | 63.1 | +51.2 | +67.5 | $+11,125 |
| KEEP-only recent | 428 | 60.0 | +53.3 | +77.8 | $+5,868 |

- KEEP strategies (24): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T12:01:08.603555-04:00","date":"2026-09-10","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":40.2,"phases_s":{"reconcile":0.46,"cancel":0.15,"manage":35.28,"protective_stops":3.65},"signals":0,"placed":0,"equity":1000081.8,"open_positions":54,"pending_orders":0,"open_lots":197,"submitted_today":117,"filled_today":213,"unattributed_contracts":0,"top_signals":[],"github_run":"9616","github_run_id":"34499283906","status":"ok","data_quality":{"clean":{"n":1147,"win":49.43,"med":-7.69,"avg":42.53,"pnl":15717.59},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":636,"win":63.05,"med":51.18,"avg":67.49,"pnl":11125.45},"keep_only_recent":{"n":428,"win":60.05,"med":53.33,"avg":77.77,"pnl":5868.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
16:01:03  INFO      Mode: exits
16:01:03  INFO        Daily log -> logs/daily/2026-09-10.md
16:01:03  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
16:01:04  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T12:01:05.351335-04:00 share=25% ===
2026-09-10 12:01:05,351 INFO === options_live_micro LIVE 2026-09-10T12:01:05.351335-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 12:01:05,509 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: manage/exits only
2026-09-10 12:01:05,654 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-10 12:01:05,696 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (178 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |   197 | INFO |
| Total closed lots           |  2140 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1147 med=-7.7% | TAINTED n=1827 med=-38.8% | KEEP-only n=636 med=+51.2% | KILL=18 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T160725Z

- UTC timestamp: `20260910T160725Z`
- GitHub run: [#9617](https://github.com/28twagg-ops/TradingBot/actions/runs/34499822734)
- Run id: `34499822734`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`39s`
- Full logs: `logs/action_runs/20260910T160725Z_live_bot.log`, `logs/action_runs/20260910T160725Z_live_options.log`, `logs/action_runs/20260910T160725Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1148 | 49.5 | -5.2 | +42.5 | $+15,729 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 637 | 63.1 | +51.4 | +67.5 | $+11,136 |
| KEEP-only recent | 429 | 60.1 | +53.3 | +77.7 | $+5,879 |

- KEEP strategies (24): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T12:07:32.879261-04:00","date":"2026-09-10","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":25.7,"phases_s":{"reconcile":0.36,"cancel":0.13,"manage":20.9,"protective_stops":3.62},"signals":0,"placed":0,"equity":999406.88,"open_positions":50,"pending_orders":0,"open_lots":160,"submitted_today":117,"filled_today":213,"unattributed_contracts":0,"top_signals":[],"github_run":"9617","github_run_id":"34499822734","status":"ok","data_quality":{"clean":{"n":1148,"win":49.48,"med":-5.2,"avg":42.55,"pnl":15728.59},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":637,"win":63.11,"med":51.39,"avg":67.48,"pnl":11136.45},"keep_only_recent":{"n":429,"win":60.14,"med":53.33,"avg":77.73,"pnl":5879.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
16:07:26  INFO      Mode: exits
16:07:27  INFO        Daily log -> logs/daily/2026-09-10.md
16:07:27  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
16:07:27  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:07 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T12:07:28.320691-04:00 share=25% ===
2026-09-10 12:07:28,320 INFO === options_live_micro LIVE 2026-09-10T12:07:28.320691-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 12:07:28,465 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: manage/exits only
2026-09-10 12:07:28,586 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-10 12:07:28,626 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (222 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |   160 | INFO |
| Total closed lots           |  2141 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1148 med=-5.2% | TAINTED n=1827 med=-38.8% | KEEP-only n=637 med=+51.4% | KILL=18 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T161105Z

- UTC timestamp: `20260910T161105Z`
- GitHub run: [#9618](https://github.com/28twagg-ops/TradingBot/actions/runs/34500357830)
- Run id: `34500357830`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`39s`
- Full logs: `logs/action_runs/20260910T161105Z_live_bot.log`, `logs/action_runs/20260910T161105Z_live_options.log`, `logs/action_runs/20260910T161105Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1151 | 49.3 | -7.7 | +42.3 | $+15,658 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 638 | 63.0 | +51.2 | +67.3 | $+11,103 |
| KEEP-only recent | 430 | 60.0 | +53.3 | +77.4 | $+5,846 |

- KEEP strategies (24): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T12:11:12.666276-04:00","date":"2026-09-10","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":28.7,"phases_s":{"reconcile":1.13,"cancel":0.19,"manage":22.23,"protective_stops":4.43},"signals":0,"placed":0,"equity":999245.62,"open_positions":47,"pending_orders":0,"open_lots":149,"submitted_today":117,"filled_today":213,"unattributed_contracts":0,"top_signals":[],"github_run":"9618","github_run_id":"34500357830","status":"ok","data_quality":{"clean":{"n":1151,"win":49.35,"med":-7.69,"avg":42.3,"pnl":15657.59},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":638,"win":63.01,"med":51.18,"avg":67.28,"pnl":11103.45},"keep_only_recent":{"n":430,"win":60.0,"med":53.33,"avg":77.41,"pnl":5846.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
16:11:06  INFO      Mode: exits
16:11:07  INFO        Daily log -> logs/daily/2026-09-10.md
16:11:07  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
16:11:07  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T12:11:08.774587-04:00 share=25% ===
2026-09-10 12:11:08,774 INFO === options_live_micro LIVE 2026-09-10T12:11:08.774587-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 12:11:08,968 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: manage/exits only
2026-09-10 12:11:09,159 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-10 12:11:09,216 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (192 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   149 | INFO |
| Total closed lots           |  2143 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1151 med=-7.7% | TAINTED n=1827 med=-38.8% | KEEP-only n=638 med=+51.2% | KILL=18 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T161607Z

- UTC timestamp: `20260910T161607Z`
- GitHub run: [#9619](https://github.com/28twagg-ops/TradingBot/actions/runs/34500887580)
- Run id: `34500887580`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`36s`
- Full logs: `logs/action_runs/20260910T161607Z_live_bot.log`, `logs/action_runs/20260910T161607Z_live_options.log`, `logs/action_runs/20260910T161607Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1154 | 49.2 | -7.7 | +42.1 | $+15,584 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 639 | 62.9 | +51.0 | +67.1 | $+11,094 |
| KEEP-only recent | 431 | 59.9 | +53.3 | +77.1 | $+5,837 |

- KEEP strategies (24): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T12:16:13.446235-04:00","date":"2026-09-10","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":26.2,"phases_s":{"reconcile":0.57,"cancel":0.2,"manage":20.44,"protective_stops":4.21},"signals":0,"placed":0,"equity":999298.54,"open_positions":45,"pending_orders":0,"open_lots":146,"submitted_today":117,"filled_today":213,"unattributed_contracts":0,"top_signals":[],"github_run":"9619","github_run_id":"34500887580","status":"ok","data_quality":{"clean":{"n":1154,"win":49.22,"med":-7.69,"avg":42.05,"pnl":15583.59},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":639,"win":62.91,"med":50.98,"avg":67.1,"pnl":11094.45},"keep_only_recent":{"n":431,"win":59.86,"med":53.33,"avg":77.11,"pnl":5837.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
16:16:08  INFO      Mode: exits
16:16:09  INFO        Daily log -> logs/daily/2026-09-10.md
16:16:09  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
16:16:09  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T12:16:10.372092-04:00 share=25% ===
2026-09-10 12:16:10,372 INFO === options_live_micro LIVE 2026-09-10T12:16:10.372092-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 12:16:10,664 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: manage/exits only
2026-09-10 12:16:10,831 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-10 12:16:10,887 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (187 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |   146 | INFO |
| Total closed lots           |  2145 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1154 med=-7.7% | TAINTED n=1827 med=-38.8% | KEEP-only n=639 med=+51.0% | KILL=18 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T162244Z

- UTC timestamp: `20260910T162244Z`
- GitHub run: [#9620](https://github.com/28twagg-ops/TradingBot/actions/runs/34501419463)
- Run id: `34501419463`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`26s`
- Full logs: `logs/action_runs/20260910T162244Z_live_bot.log`, `logs/action_runs/20260910T162244Z_live_options.log`, `logs/action_runs/20260910T162244Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1155 | 49.2 | -7.7 | +42.0 | $+15,563 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 615 | 63.4 | +51.4 | +68.1 | $+10,693 |
| KEEP-only recent | 415 | 61.2 | +53.6 | +80.7 | $+5,988 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406, S412
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S398, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T12:22:50.355916-04:00","date":"2026-09-10","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":13.2,"phases_s":{"reconcile":0.2,"cancel":0.04,"manage":11.63,"protective_stops":0.81},"signals":0,"placed":0,"equity":999464.46,"open_positions":44,"pending_orders":0,"open_lots":142,"submitted_today":117,"filled_today":213,"unattributed_contracts":0,"top_signals":[],"github_run":"9620","github_run_id":"34501419463","status":"ok","data_quality":{"clean":{"n":1155,"win":49.18,"med":-7.69,"avg":41.97,"pnl":15562.59},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":615,"win":63.41,"med":51.39,"avg":68.14,"pnl":10693.45},"keep_only_recent":{"n":415,"win":61.2,"med":53.57,"avg":80.7,"pnl":5988.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S398","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
16:22:45  INFO      Mode: exits
16:22:45  INFO        Daily log -> logs/daily/2026-09-10.md
16:22:45  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
16:22:45  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:22 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T12:22:46.682514-04:00 share=25% ===
2026-09-10 12:22:46,682 INFO === options_live_micro LIVE 2026-09-10T12:22:46.682514-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 12:22:46,720 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: manage/exits only
2026-09-10 12:22:46,740 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-10 12:22:46,750 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (184 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |   142 | INFO |
| Total closed lots           |  2146 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1155 med=-7.7% | TAINTED n=1827 med=-38.8% | KEEP-only n=615 med=+51.4% | KILL=19 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T162558Z

- UTC timestamp: `20260910T162558Z`
- GitHub run: [#9621](https://github.com/28twagg-ops/TradingBot/actions/runs/34501952173)
- Run id: `34501952173`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`34s`
- Full logs: `logs/action_runs/20260910T162558Z_live_bot.log`, `logs/action_runs/20260910T162558Z_live_options.log`, `logs/action_runs/20260910T162558Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1156 | 49.1 | -10.1 | +41.9 | $+15,535 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 616 | 63.3 | +51.4 | +67.9 | $+10,665 |
| KEEP-only recent | 416 | 61.1 | +53.4 | +80.4 | $+5,960 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406, S412
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S398, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T12:26:05.927915-04:00","date":"2026-09-10","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":23.2,"phases_s":{"reconcile":0.47,"cancel":0.2,"manage":17.87,"protective_stops":3.96},"signals":0,"placed":0,"equity":999362.94,"open_positions":44,"pending_orders":0,"open_lots":141,"submitted_today":117,"filled_today":213,"unattributed_contracts":0,"top_signals":[],"github_run":"9621","github_run_id":"34501952173","status":"ok","data_quality":{"clean":{"n":1156,"win":49.13,"med":-10.1,"avg":41.89,"pnl":15534.59},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":616,"win":63.31,"med":51.39,"avg":67.94,"pnl":10665.45},"keep_only_recent":{"n":416,"win":61.06,"med":53.45,"avg":80.38,"pnl":5960.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S398","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
16:25:59  INFO      Mode: exits
16:26:00  INFO        Daily log -> logs/daily/2026-09-10.md
16:26:00  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
16:26:01  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T12:26:02.285245-04:00 share=25% ===
2026-09-10 12:26:02,285 INFO === options_live_micro LIVE 2026-09-10T12:26:02.285245-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 12:26:02,490 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: manage/exits only
2026-09-10 12:26:02,713 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-10 12:26:02,770 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (180 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |   141 | INFO |
| Total closed lots           |  2147 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1156 med=-10.1% | TAINTED n=1827 med=-38.8% | KEEP-only n=616 med=+51.4% | KILL=19 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T163116Z

- UTC timestamp: `20260910T163116Z`
- GitHub run: [#9622](https://github.com/28twagg-ops/TradingBot/actions/runs/34502474281)
- Run id: `34502474281`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`28s`
- Full logs: `logs/action_runs/20260910T163116Z_live_bot.log`, `logs/action_runs/20260910T163116Z_live_options.log`, `logs/action_runs/20260910T163116Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1158 | 49.1 | -14.2 | +41.7 | $+15,497 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 618 | 63.1 | +51.2 | +67.6 | $+10,627 |
| KEEP-only recent | 418 | 60.8 | +53.3 | +79.8 | $+5,922 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406, S412
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S398, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T12:31:22.310661-04:00","date":"2026-09-10","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":16.3,"phases_s":{"reconcile":0.8,"cancel":0.04,"manage":13.55,"protective_stops":1.06},"signals":0,"placed":0,"equity":999333.4,"open_positions":42,"pending_orders":0,"open_lots":139,"submitted_today":117,"filled_today":213,"unattributed_contracts":0,"top_signals":[],"github_run":"9622","github_run_id":"34502474281","status":"ok","data_quality":{"clean":{"n":1158,"win":49.05,"med":-14.18,"avg":41.74,"pnl":15496.59},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":618,"win":63.11,"med":51.18,"avg":67.57,"pnl":10627.45},"keep_only_recent":{"n":418,"win":60.77,"med":53.33,"avg":79.77,"pnl":5922.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S398","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
16:31:18  INFO      Mode: exits
16:31:18  INFO        Daily log -> logs/daily/2026-09-10.md
16:31:18  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
16:31:18  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T12:31:19.540932-04:00 share=25% ===
2026-09-10 12:31:19,541 INFO === options_live_micro LIVE 2026-09-10T12:31:19.540932-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 12:31:19,603 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: manage/exits only
2026-09-10 12:31:19,638 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-10 12:31:19,649 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (179 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |   139 | INFO |
| Total closed lots           |  2149 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1158 med=-14.2% | TAINTED n=1827 med=-38.8% | KEEP-only n=618 med=+51.2% | KILL=19 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T163601Z

- UTC timestamp: `20260910T163601Z`
- GitHub run: [#9623](https://github.com/28twagg-ops/TradingBot/actions/runs/34502990834)
- Run id: `34502990834`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`29s`
- Full logs: `logs/action_runs/20260910T163601Z_live_bot.log`, `logs/action_runs/20260910T163601Z_live_options.log`, `logs/action_runs/20260910T163601Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1158 | 49.1 | -14.2 | +41.7 | $+15,497 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 618 | 63.1 | +51.2 | +67.6 | $+10,627 |
| KEEP-only recent | 418 | 60.8 | +53.3 | +79.8 | $+5,922 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406, S412
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S398, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T12:36:06.819323-04:00","date":"2026-09-10","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":16.5,"phases_s":{"reconcile":0.3,"cancel":0.1,"manage":13.67,"protective_stops":1.72},"signals":0,"placed":0,"equity":999144.28,"open_positions":42,"pending_orders":0,"open_lots":134,"submitted_today":117,"filled_today":213,"unattributed_contracts":0,"top_signals":[],"github_run":"9623","github_run_id":"34502990834","status":"ok","data_quality":{"clean":{"n":1158,"win":49.05,"med":-14.18,"avg":41.74,"pnl":15496.59},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":618,"win":63.11,"med":51.18,"avg":67.57,"pnl":10627.45},"keep_only_recent":{"n":418,"win":60.77,"med":53.33,"avg":79.77,"pnl":5922.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S398","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
16:36:02  INFO      Mode: exits
16:36:02  INFO        Daily log -> logs/daily/2026-09-10.md
16:36:02  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
16:36:02  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T12:36:03.682669-04:00 share=25% ===
2026-09-10 12:36:03,682 INFO === options_live_micro LIVE 2026-09-10T12:36:03.682669-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 12:36:03,767 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: manage/exits only
2026-09-10 12:36:03,829 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-10 12:36:03,849 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (189 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |   134 | INFO |
| Total closed lots           |  2149 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1158 med=-14.2% | TAINTED n=1827 med=-38.8% | KEEP-only n=618 med=+51.2% | KILL=19 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T164102Z

- UTC timestamp: `20260910T164102Z`
- GitHub run: [#9624](https://github.com/28twagg-ops/TradingBot/actions/runs/34503482060)
- Run id: `34503482060`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`39s`
- Full logs: `logs/action_runs/20260910T164102Z_live_bot.log`, `logs/action_runs/20260910T164102Z_live_options.log`, `logs/action_runs/20260910T164102Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1160 | 49.0 | -15.9 | +41.6 | $+15,453 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 619 | 63.0 | +51.0 | +67.4 | $+10,608 |
| KEEP-only recent | 419 | 60.6 | +53.3 | +79.4 | $+5,903 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406, S412
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S398, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T12:41:10.560456-04:00","date":"2026-09-10","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":26.0,"phases_s":{"reconcile":0.64,"cancel":0.23,"manage":19.75,"protective_stops":4.2},"signals":0,"placed":0,"equity":999317.71,"open_positions":41,"pending_orders":0,"open_lots":131,"submitted_today":117,"filled_today":213,"unattributed_contracts":0,"top_signals":[],"github_run":"9624","github_run_id":"34503482060","status":"ok","data_quality":{"clean":{"n":1160,"win":48.97,"med":-15.93,"avg":41.58,"pnl":15453.09},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":619,"win":63.0,"med":50.98,"avg":67.36,"pnl":10608.45},"keep_only_recent":{"n":419,"win":60.62,"med":53.33,"avg":79.43,"pnl":5903.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S398","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
16:41:03  INFO      Mode: exits
16:41:04  INFO        Daily log -> logs/daily/2026-09-10.md
16:41:04  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
16:41:05  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T12:41:06.079165-04:00 share=25% ===
2026-09-10 12:41:06,079 INFO === options_live_micro LIVE 2026-09-10T12:41:06.079165-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 12:41:06,324 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: manage/exits only
2026-09-10 12:41:06,548 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-10 12:41:06,623 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (181 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     5 | WARN | <<<
| Total open lots             |   131 | INFO |
| Total closed lots           |  2150 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1160 med=-15.9% | TAINTED n=1827 med=-38.8% | KEEP-only n=619 med=+51.0% | KILL=19 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T164610Z

- UTC timestamp: `20260910T164610Z`
- GitHub run: [#9625](https://github.com/28twagg-ops/TradingBot/actions/runs/34503993311)
- Run id: `34503993311`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`36s`
- Full logs: `logs/action_runs/20260910T164610Z_live_bot.log`, `logs/action_runs/20260910T164610Z_live_options.log`, `logs/action_runs/20260910T164610Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1160 | 49.0 | -15.9 | +41.6 | $+15,453 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 619 | 63.0 | +51.0 | +67.4 | $+10,608 |
| KEEP-only recent | 419 | 60.6 | +53.3 | +79.4 | $+5,903 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406, S412
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S398, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T12:46:18.215190-04:00","date":"2026-09-10","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":24.5,"phases_s":{"reconcile":0.58,"cancel":0.23,"manage":18.69,"protective_stops":4.13},"signals":0,"placed":0,"equity":999420.2,"open_positions":40,"pending_orders":0,"open_lots":130,"submitted_today":117,"filled_today":213,"unattributed_contracts":0,"top_signals":[],"github_run":"9625","github_run_id":"34503993311","status":"ok","data_quality":{"clean":{"n":1160,"win":48.97,"med":-15.93,"avg":41.58,"pnl":15453.09},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":619,"win":63.0,"med":50.98,"avg":67.36,"pnl":10608.45},"keep_only_recent":{"n":419,"win":60.62,"med":53.33,"avg":79.43,"pnl":5903.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S398","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
16:46:11  INFO      Mode: exits
16:46:12  INFO        Daily log -> logs/daily/2026-09-10.md
16:46:12  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
16:46:12  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T12:46:14.415391-04:00 share=25% ===
2026-09-10 12:46:14,415 INFO === options_live_micro LIVE 2026-09-10T12:46:14.415391-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 12:46:14,637 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: manage/exits only
2026-09-10 12:46:14,929 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-10 12:46:14,995 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (179 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     5 | WARN | <<<
| Total open lots             |   130 | INFO |
| Total closed lots           |  2150 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1160 med=-15.9% | TAINTED n=1827 med=-38.8% | KEEP-only n=619 med=+51.0% | KILL=19 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T165113Z

- UTC timestamp: `20260910T165113Z`
- GitHub run: [#9626](https://github.com/28twagg-ops/TradingBot/actions/runs/34504506202)
- Run id: `34504506202`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`24s`
- Full logs: `logs/action_runs/20260910T165113Z_live_bot.log`, `logs/action_runs/20260910T165113Z_live_options.log`, `logs/action_runs/20260910T165113Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1160 | 49.0 | -15.9 | +41.6 | $+15,453 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 619 | 63.0 | +51.0 | +67.4 | $+10,608 |
| KEEP-only recent | 419 | 60.6 | +53.3 | +79.4 | $+5,903 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406, S412
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S398, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T12:51:18.956159-04:00","date":"2026-09-10","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":13.0,"phases_s":{"reconcile":0.15,"cancel":0.03,"manage":11.43,"protective_stops":0.87},"signals":0,"placed":0,"equity":999236.7,"open_positions":40,"pending_orders":0,"open_lots":130,"submitted_today":117,"filled_today":213,"unattributed_contracts":0,"top_signals":[],"github_run":"9626","github_run_id":"34504506202","status":"ok","data_quality":{"clean":{"n":1160,"win":48.97,"med":-15.93,"avg":41.58,"pnl":15453.09},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":619,"win":63.0,"med":50.98,"avg":67.36,"pnl":10608.45},"keep_only_recent":{"n":419,"win":60.62,"med":53.33,"avg":79.43,"pnl":5903.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S398","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
16:51:15  INFO      Mode: exits
16:51:15  INFO        Daily log -> logs/daily/2026-09-10.md
16:51:15  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
16:51:15  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:51 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T12:51:16.202367-04:00 share=25% ===
2026-09-10 12:51:16,202 INFO === options_live_micro LIVE 2026-09-10T12:51:16.202367-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 12:51:16,249 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: manage/exits only
2026-09-10 12:51:16,275 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-10 12:51:16,283 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (179 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     5 | WARN | <<<
| Total open lots             |   130 | INFO |
| Total closed lots           |  2150 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1160 med=-15.9% | TAINTED n=1827 med=-38.8% | KEEP-only n=619 med=+51.0% | KILL=19 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T165618Z

- UTC timestamp: `20260910T165618Z`
- GitHub run: [#9627](https://github.com/28twagg-ops/TradingBot/actions/runs/34505007812)
- Run id: `34505007812`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`27s`
- Full logs: `logs/action_runs/20260910T165618Z_live_bot.log`, `logs/action_runs/20260910T165618Z_live_options.log`, `logs/action_runs/20260910T165618Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1162 | 48.9 | -16.6 | +41.4 | $+15,392 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 619 | 63.0 | +51.0 | +67.4 | $+10,608 |
| KEEP-only recent | 419 | 60.6 | +53.3 | +79.4 | $+5,903 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406, S412
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S398, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T12:56:23.838650-04:00","date":"2026-09-10","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":18.8,"phases_s":{"reconcile":0.47,"cancel":0.15,"manage":14.21,"protective_stops":3.37},"signals":0,"placed":0,"equity":999316.16,"open_positions":39,"pending_orders":0,"open_lots":128,"submitted_today":117,"filled_today":213,"unattributed_contracts":0,"top_signals":[],"github_run":"9627","github_run_id":"34505007812","status":"ok","data_quality":{"clean":{"n":1162,"win":48.88,"med":-16.6,"avg":41.43,"pnl":15392.09},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":619,"win":63.0,"med":50.98,"avg":67.36,"pnl":10608.45},"keep_only_recent":{"n":419,"win":60.62,"med":53.33,"avg":79.43,"pnl":5903.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S398","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
16:56:19  INFO      Mode: exits
16:56:20  INFO        Daily log -> logs/daily/2026-09-10.md
16:56:20  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
16:56:20  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:56 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T12:56:21.460748-04:00 share=25% ===
2026-09-10 12:56:21,460 INFO === options_live_micro LIVE 2026-09-10T12:56:21.460748-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 12:56:21,606 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: manage/exits only
2026-09-10 12:56:21,724 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-10 12:56:21,763 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (182 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |   128 | INFO |
| Total closed lots           |  2151 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1162 med=-16.6% | TAINTED n=1827 med=-38.8% | KEEP-only n=619 med=+51.0% | KILL=19 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T170111Z

- UTC timestamp: `20260910T170111Z`
- GitHub run: [#9628](https://github.com/28twagg-ops/TradingBot/actions/runs/34505506225)
- Run id: `34505506225`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`31s`
- Full logs: `logs/action_runs/20260910T170111Z_live_bot.log`, `logs/action_runs/20260910T170111Z_live_options.log`, `logs/action_runs/20260910T170111Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1163 | 48.9 | -16.0 | +41.4 | $+15,424 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 620 | 63.1 | +51.2 | +67.3 | $+10,640 |
| KEEP-only recent | 420 | 60.7 | +53.3 | +79.4 | $+5,935 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406, S412
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S398, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T13:01:16.384221-04:00","date":"2026-09-10","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":22.3,"phases_s":{"reconcile":0.69,"cancel":0.12,"manage":18.16,"protective_stops":2.69},"signals":0,"placed":0,"equity":999455.12,"open_positions":38,"pending_orders":0,"open_lots":126,"submitted_today":117,"filled_today":213,"unattributed_contracts":0,"top_signals":[],"github_run":"9628","github_run_id":"34505506225","status":"ok","data_quality":{"clean":{"n":1163,"win":48.93,"med":-16.0,"avg":41.44,"pnl":15424.09},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":620,"win":63.06,"med":51.18,"avg":67.34,"pnl":10640.45},"keep_only_recent":{"n":420,"win":60.71,"med":53.33,"avg":79.37,"pnl":5935.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S398","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
17:01:12  INFO      Mode: exits
17:01:12  INFO        Daily log -> logs/daily/2026-09-10.md
17:01:12  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
17:01:12  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T13:01:13.469033-04:00 share=25% ===
2026-09-10 13:01:13,469 INFO === options_live_micro LIVE 2026-09-10T13:01:13.469033-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 13:01:13,610 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: manage/exits only
2026-09-10 13:01:13,754 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-10 13:01:13,792 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (185 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |   126 | INFO |
| Total closed lots           |  2152 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1163 med=-16.0% | TAINTED n=1827 med=-38.8% | KEEP-only n=620 med=+51.2% | KILL=19 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T170606Z

- UTC timestamp: `20260910T170606Z`
- GitHub run: [#9629](https://github.com/28twagg-ops/TradingBot/actions/runs/34506018274)
- Run id: `34506018274`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`38s`
- Full logs: `logs/action_runs/20260910T170606Z_live_bot.log`, `logs/action_runs/20260910T170606Z_live_options.log`, `logs/action_runs/20260910T170606Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1165 | 48.9 | -16.0 | +41.4 | $+15,432 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 596 | 63.6 | +51.5 | +69.5 | $+10,676 |
| KEEP-only recent | 396 | 61.4 | +53.7 | +83.3 | $+5,971 |

- KEEP strategies (22): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S398, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T13:06:14.788052-04:00","date":"2026-09-10","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":25.3,"phases_s":{"reconcile":0.58,"cancel":0.23,"manage":19.08,"protective_stops":4.63},"signals":0,"placed":0,"equity":999483.54,"open_positions":37,"pending_orders":0,"open_lots":122,"submitted_today":117,"filled_today":213,"unattributed_contracts":0,"top_signals":[],"github_run":"9629","github_run_id":"34506018274","status":"ok","data_quality":{"clean":{"n":1165,"win":48.93,"med":-16.0,"avg":41.38,"pnl":15432.09},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":596,"win":63.59,"med":51.48,"avg":69.47,"pnl":10676.45},"keep_only_recent":{"n":396,"win":61.36,"med":53.71,"avg":83.3,"pnl":5971.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S398","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
17:06:07  INFO      Mode: exits
17:06:08  INFO        Daily log -> logs/daily/2026-09-10.md
17:06:08  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
17:06:09  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T13:06:10.251024-04:00 share=25% ===
2026-09-10 13:06:10,251 INFO === options_live_micro LIVE 2026-09-10T13:06:10.251024-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 13:06:10,506 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: manage/exits only
2026-09-10 13:06:10,733 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-10 13:06:10,811 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (181 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |   122 | INFO |
| Total closed lots           |  2154 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1165 med=-16.0% | TAINTED n=1827 med=-38.8% | KEEP-only n=596 med=+51.5% | KILL=19 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T171057Z

- UTC timestamp: `20260910T171057Z`
- GitHub run: [#9630](https://github.com/28twagg-ops/TradingBot/actions/runs/34506533705)
- Run id: `34506533705`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`22s`
- Full logs: `logs/action_runs/20260910T171057Z_live_bot.log`, `logs/action_runs/20260910T171057Z_live_options.log`, `logs/action_runs/20260910T171057Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1166 | 48.9 | -16.6 | +41.3 | $+15,404 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 596 | 63.6 | +51.5 | +69.5 | $+10,676 |
| KEEP-only recent | 396 | 61.4 | +53.7 | +83.3 | $+5,971 |

- KEEP strategies (22): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T13:11:01.626195-04:00","date":"2026-09-10","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":13.2,"phases_s":{"reconcile":0.16,"cancel":0.05,"manage":11.74,"protective_stops":0.8},"signals":0,"placed":0,"equity":999602.0,"open_positions":38,"pending_orders":0,"open_lots":121,"submitted_today":117,"filled_today":213,"unattributed_contracts":0,"top_signals":[],"github_run":"9630","github_run_id":"34506533705","status":"ok","data_quality":{"clean":{"n":1166,"win":48.89,"med":-16.6,"avg":41.3,"pnl":15404.09},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":596,"win":63.59,"med":51.48,"avg":69.47,"pnl":10676.45},"keep_only_recent":{"n":396,"win":61.36,"med":53.71,"avg":83.3,"pnl":5971.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
17:10:58  INFO      Mode: exits
17:10:58  INFO        Daily log -> logs/daily/2026-09-10.md
17:10:58  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
17:10:58  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T13:10:59.412742-04:00 share=25% ===
2026-09-10 13:10:59,412 INFO === options_live_micro LIVE 2026-09-10T13:10:59.412742-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 13:10:59,450 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: manage/exits only
2026-09-10 13:10:59,470 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-10 13:10:59,477 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (178 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  2155 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1166 med=-16.6% | TAINTED n=1827 med=-38.8% | KEEP-only n=596 med=+51.5% | KILL=20 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T171725Z

- UTC timestamp: `20260910T171725Z`
- GitHub run: [#9631](https://github.com/28twagg-ops/TradingBot/actions/runs/34507038946)
- Run id: `34507038946`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`34s`
- Full logs: `logs/action_runs/20260910T171725Z_live_bot.log`, `logs/action_runs/20260910T171725Z_live_options.log`, `logs/action_runs/20260910T171725Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1167 | 48.8 | -17.2 | +41.2 | $+15,376 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 597 | 63.5 | +51.4 | +69.3 | $+10,648 |
| KEEP-only recent | 397 | 61.2 | +53.6 | +83.0 | $+5,943 |

- KEEP strategies (22): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T13:17:33.503727-04:00","date":"2026-09-10","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":20.5,"phases_s":{"reconcile":0.48,"cancel":0.17,"manage":16.07,"protective_stops":3.06},"signals":0,"placed":0,"equity":999574.91,"open_positions":37,"pending_orders":0,"open_lots":117,"submitted_today":117,"filled_today":213,"unattributed_contracts":0,"top_signals":[],"github_run":"9631","github_run_id":"34507038946","status":"ok","data_quality":{"clean":{"n":1167,"win":48.84,"med":-17.19,"avg":41.22,"pnl":15376.09},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":597,"win":63.48,"med":51.39,"avg":69.27,"pnl":10648.45},"keep_only_recent":{"n":397,"win":61.21,"med":53.57,"avg":82.97,"pnl":5943.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
17:17:26  INFO      Mode: exits
17:17:27  INFO        Daily log -> logs/daily/2026-09-10.md
17:17:27  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
17:17:28  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:17 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T13:17:28.853482-04:00 share=25% ===
2026-09-10 13:17:28,853 INFO === options_live_micro LIVE 2026-09-10T13:17:28.853482-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 13:17:29,268 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: manage/exits only
2026-09-10 13:17:29,442 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-10 13:17:29,499 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (184 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |   117 | INFO |
| Total closed lots           |  2156 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1167 med=-17.2% | TAINTED n=1827 med=-38.8% | KEEP-only n=597 med=+51.4% | KILL=20 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T172059Z

- UTC timestamp: `20260910T172059Z`
- GitHub run: [#9632](https://github.com/28twagg-ops/TradingBot/actions/runs/34507563546)
- Run id: `34507563546`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`20s`
- Full logs: `logs/action_runs/20260910T172059Z_live_bot.log`, `logs/action_runs/20260910T172059Z_live_options.log`, `logs/action_runs/20260910T172059Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1167 | 48.8 | -17.2 | +41.2 | $+15,376 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 597 | 63.5 | +51.4 | +69.3 | $+10,648 |
| KEEP-only recent | 397 | 61.2 | +53.6 | +83.0 | $+5,943 |

- KEEP strategies (22): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T13:21:03.063350-04:00","date":"2026-09-10","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":10.5,"phases_s":{"reconcile":0.26,"cancel":0.04,"manage":9.06,"protective_stops":0.64},"signals":0,"placed":0,"equity":999499.58,"open_positions":36,"pending_orders":0,"open_lots":116,"submitted_today":117,"filled_today":213,"unattributed_contracts":0,"top_signals":[],"github_run":"9632","github_run_id":"34507563546","status":"ok","data_quality":{"clean":{"n":1167,"win":48.84,"med":-17.19,"avg":41.22,"pnl":15376.09},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":597,"win":63.48,"med":51.39,"avg":69.27,"pnl":10648.45},"keep_only_recent":{"n":397,"win":61.21,"med":53.57,"avg":82.97,"pnl":5943.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
17:20:59  INFO      Mode: exits
17:21:00  INFO        Daily log -> logs/daily/2026-09-10.md
17:21:00  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
17:21:00  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T13:21:00.776503-04:00 share=25% ===
2026-09-10 13:21:00,776 INFO === options_live_micro LIVE 2026-09-10T13:21:00.776503-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 13:21:00,813 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: manage/exits only
2026-09-10 13:21:00,836 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-10 13:21:00,842 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (179 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |   116 | INFO |
| Total closed lots           |  2156 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1167 med=-17.2% | TAINTED n=1827 med=-38.8% | KEEP-only n=597 med=+51.4% | KILL=20 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T172620Z

- UTC timestamp: `20260910T172620Z`
- GitHub run: [#9633](https://github.com/28twagg-ops/TradingBot/actions/runs/34508078159)
- Run id: `34508078159`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`23s`
- Full logs: `logs/action_runs/20260910T172620Z_live_bot.log`, `logs/action_runs/20260910T172620Z_live_options.log`, `logs/action_runs/20260910T172620Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1168 | 48.8 | -17.2 | +41.1 | $+15,349 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 598 | 63.4 | +51.4 | +69.1 | $+10,621 |
| KEEP-only recent | 398 | 61.1 | +53.4 | +82.6 | $+5,916 |

- KEEP strategies (22): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T13:26:26.536382-04:00","date":"2026-09-10","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":11.3,"phases_s":{"reconcile":0.17,"cancel":0.03,"manage":9.99,"protective_stops":0.58},"signals":0,"placed":0,"equity":999528.22,"open_positions":36,"pending_orders":0,"open_lots":115,"submitted_today":117,"filled_today":213,"unattributed_contracts":0,"top_signals":[],"github_run":"9633","github_run_id":"34508078159","status":"ok","data_quality":{"clean":{"n":1168,"win":48.8,"med":-17.22,"avg":41.14,"pnl":15349.09},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":598,"win":63.38,"med":51.39,"avg":69.07,"pnl":10621.45},"keep_only_recent":{"n":398,"win":61.06,"med":53.45,"avg":82.63,"pnl":5916.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
17:26:21  INFO      Mode: exits
17:26:22  INFO        Daily log -> logs/daily/2026-09-10.md
17:26:22  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
17:26:22  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T13:26:23.574709-04:00 share=25% ===
2026-09-10 13:26:23,574 INFO === options_live_micro LIVE 2026-09-10T13:26:23.574709-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 13:26:23,626 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: manage/exits only
2026-09-10 13:26:23,666 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-10 13:26:23,673 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (178 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |   115 | INFO |
| Total closed lots           |  2157 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1168 med=-17.2% | TAINTED n=1827 med=-38.8% | KEEP-only n=598 med=+51.4% | KILL=20 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T173111Z

- UTC timestamp: `20260910T173111Z`
- GitHub run: [#9634](https://github.com/28twagg-ops/TradingBot/actions/runs/34508585415)
- Run id: `34508585415`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`34s`
- Full logs: `logs/action_runs/20260910T173111Z_live_bot.log`, `logs/action_runs/20260910T173111Z_live_options.log`, `logs/action_runs/20260910T173111Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1168 | 48.8 | -17.2 | +41.1 | $+15,349 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 598 | 63.4 | +51.4 | +69.1 | $+10,621 |
| KEEP-only recent | 398 | 61.1 | +53.4 | +82.6 | $+5,916 |

- KEEP strategies (22): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T13:31:18.820239-04:00","date":"2026-09-10","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":22.8,"phases_s":{"reconcile":0.72,"cancel":0.23,"manage":16.87,"protective_stops":3.98},"signals":0,"placed":0,"equity":999786.78,"open_positions":35,"pending_orders":0,"open_lots":111,"submitted_today":117,"filled_today":213,"unattributed_contracts":0,"top_signals":[],"github_run":"9634","github_run_id":"34508585415","status":"ok","data_quality":{"clean":{"n":1168,"win":48.8,"med":-17.22,"avg":41.14,"pnl":15349.09},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":598,"win":63.38,"med":51.39,"avg":69.07,"pnl":10621.45},"keep_only_recent":{"n":398,"win":61.06,"med":53.45,"avg":82.63,"pnl":5916.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
17:31:12  INFO      Mode: exits
17:31:13  INFO        Daily log -> logs/daily/2026-09-10.md
17:31:13  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
17:31:13  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T13:31:14.491751-04:00 share=25% ===
2026-09-10 13:31:14,491 INFO === options_live_micro LIVE 2026-09-10T13:31:14.491751-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 13:31:14,726 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: manage/exits only
2026-09-10 13:31:15,044 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-10 13:31:15,112 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (182 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |   111 | INFO |
| Total closed lots           |  2157 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1168 med=-17.2% | TAINTED n=1827 med=-38.8% | KEEP-only n=598 med=+51.4% | KILL=20 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T173603Z

- UTC timestamp: `20260910T173603Z`
- GitHub run: [#9635](https://github.com/28twagg-ops/TradingBot/actions/runs/34509092913)
- Run id: `34509092913`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`31s`
- Full logs: `logs/action_runs/20260910T173603Z_live_bot.log`, `logs/action_runs/20260910T173603Z_live_options.log`, `logs/action_runs/20260910T173603Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1168 | 48.8 | -17.2 | +41.1 | $+15,349 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 598 | 63.4 | +51.4 | +69.1 | $+10,621 |
| KEEP-only recent | 398 | 61.1 | +53.4 | +82.6 | $+5,916 |

- KEEP strategies (22): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T13:36:10.731707-04:00","date":"2026-09-10","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":18.6,"phases_s":{"reconcile":0.42,"cancel":0.18,"manage":14.14,"protective_stops":3.13},"signals":0,"placed":0,"equity":999972.78,"open_positions":35,"pending_orders":0,"open_lots":111,"submitted_today":117,"filled_today":213,"unattributed_contracts":0,"top_signals":[],"github_run":"9635","github_run_id":"34509092913","status":"ok","data_quality":{"clean":{"n":1168,"win":48.8,"med":-17.22,"avg":41.14,"pnl":15349.09},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":598,"win":63.38,"med":51.39,"avg":69.07,"pnl":10621.45},"keep_only_recent":{"n":398,"win":61.06,"med":53.45,"avg":82.63,"pnl":5916.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
17:36:04  INFO      Mode: exits
17:36:05  INFO        Daily log -> logs/daily/2026-09-10.md
17:36:05  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
17:36:05  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T13:36:06.908699-04:00 share=25% ===
2026-09-10 13:36:06,908 INFO === options_live_micro LIVE 2026-09-10T13:36:06.908699-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 13:36:07,104 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: manage/exits only
2026-09-10 13:36:07,324 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-10 13:36:07,380 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (177 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |   111 | INFO |
| Total closed lots           |  2157 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1168 med=-17.2% | TAINTED n=1827 med=-38.8% | KEEP-only n=598 med=+51.4% | KILL=20 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T174125Z

- UTC timestamp: `20260910T174125Z`
- GitHub run: [#9636](https://github.com/28twagg-ops/TradingBot/actions/runs/34509607784)
- Run id: `34509607784`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`22s`
- Full logs: `logs/action_runs/20260910T174125Z_live_bot.log`, `logs/action_runs/20260910T174125Z_live_options.log`, `logs/action_runs/20260910T174125Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1168 | 48.8 | -17.2 | +41.1 | $+15,349 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 598 | 63.4 | +51.4 | +69.1 | $+10,621 |
| KEEP-only recent | 398 | 61.1 | +53.4 | +82.6 | $+5,916 |

- KEEP strategies (22): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T13:41:30.399215-04:00","date":"2026-09-10","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":10.0,"phases_s":{"reconcile":0.16,"cancel":0.04,"manage":8.75,"protective_stops":0.53},"signals":0,"placed":0,"equity":999821.78,"open_positions":35,"pending_orders":0,"open_lots":111,"submitted_today":117,"filled_today":213,"unattributed_contracts":0,"top_signals":[],"github_run":"9636","github_run_id":"34509607784","status":"ok","data_quality":{"clean":{"n":1168,"win":48.8,"med":-17.22,"avg":41.14,"pnl":15349.09},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":598,"win":63.38,"med":51.39,"avg":69.07,"pnl":10621.45},"keep_only_recent":{"n":398,"win":61.06,"med":53.45,"avg":82.63,"pnl":5916.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
17:41:26  INFO      Mode: exits
17:41:26  INFO        Daily log -> logs/daily/2026-09-10.md
17:41:26  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
17:41:26  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T13:41:27.613990-04:00 share=25% ===
2026-09-10 13:41:27,614 INFO === options_live_micro LIVE 2026-09-10T13:41:27.613990-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 13:41:27,657 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: manage/exits only
2026-09-10 13:41:27,678 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-10 13:41:27,684 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (179 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |   111 | INFO |
| Total closed lots           |  2157 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1168 med=-17.2% | TAINTED n=1827 med=-38.8% | KEEP-only n=598 med=+51.4% | KILL=20 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T174602Z

- UTC timestamp: `20260910T174602Z`
- GitHub run: [#9637](https://github.com/28twagg-ops/TradingBot/actions/runs/34510108700)
- Run id: `34510108700`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`22s`
- Full logs: `logs/action_runs/20260910T174602Z_live_bot.log`, `logs/action_runs/20260910T174602Z_live_options.log`, `logs/action_runs/20260910T174602Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1168 | 48.8 | -17.2 | +41.1 | $+15,349 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 598 | 63.4 | +51.4 | +69.1 | $+10,621 |
| KEEP-only recent | 398 | 61.1 | +53.4 | +82.6 | $+5,916 |

- KEEP strategies (22): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T13:46:07.157604-04:00","date":"2026-09-10","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":10.3,"phases_s":{"reconcile":0.29,"cancel":0.03,"manage":8.88,"protective_stops":0.57},"signals":0,"placed":0,"equity":999991.28,"open_positions":35,"pending_orders":0,"open_lots":111,"submitted_today":117,"filled_today":213,"unattributed_contracts":0,"top_signals":[],"github_run":"9637","github_run_id":"34510108700","status":"ok","data_quality":{"clean":{"n":1168,"win":48.8,"med":-17.22,"avg":41.14,"pnl":15349.09},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":598,"win":63.38,"med":51.39,"avg":69.07,"pnl":10621.45},"keep_only_recent":{"n":398,"win":61.06,"med":53.45,"avg":82.63,"pnl":5916.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
17:46:03  INFO      Mode: exits
17:46:03  INFO        Daily log -> logs/daily/2026-09-10.md
17:46:03  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
17:46:03  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T13:46:04.449584-04:00 share=25% ===
2026-09-10 13:46:04,449 INFO === options_live_micro LIVE 2026-09-10T13:46:04.449584-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 13:46:04,488 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: manage/exits only
2026-09-10 13:46:04,508 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-10 13:46:04,515 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (178 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |   111 | INFO |
| Total closed lots           |  2157 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1168 med=-17.2% | TAINTED n=1827 med=-38.8% | KEEP-only n=598 med=+51.4% | KILL=20 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T175059Z

- UTC timestamp: `20260910T175059Z`
- GitHub run: [#9638](https://github.com/28twagg-ops/TradingBot/actions/runs/34510617259)
- Run id: `34510617259`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`27s`
- Full logs: `logs/action_runs/20260910T175059Z_live_bot.log`, `logs/action_runs/20260910T175059Z_live_options.log`, `logs/action_runs/20260910T175059Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1168 | 48.8 | -17.2 | +41.1 | $+15,349 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 598 | 63.4 | +51.4 | +69.1 | $+10,621 |
| KEEP-only recent | 398 | 61.1 | +53.4 | +82.6 | $+5,916 |

- KEEP strategies (22): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T13:51:05.159144-04:00","date":"2026-09-10","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":17.5,"phases_s":{"reconcile":0.41,"cancel":0.18,"manage":13.02,"protective_stops":3.1},"signals":0,"placed":0,"equity":999996.78,"open_positions":34,"pending_orders":0,"open_lots":111,"submitted_today":117,"filled_today":213,"unattributed_contracts":0,"top_signals":[],"github_run":"9638","github_run_id":"34510617259","status":"ok","data_quality":{"clean":{"n":1168,"win":48.8,"med":-17.22,"avg":41.14,"pnl":15349.09},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":598,"win":63.38,"med":51.39,"avg":69.07,"pnl":10621.45},"keep_only_recent":{"n":398,"win":61.06,"med":53.45,"avg":82.63,"pnl":5916.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
17:51:00  INFO      Mode: exits
17:51:01  INFO        Daily log -> logs/daily/2026-09-10.md
17:51:01  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
17:51:01  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:51 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T13:51:02.265542-04:00 share=25% ===
2026-09-10 13:51:02,265 INFO === options_live_micro LIVE 2026-09-10T13:51:02.265542-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 13:51:02,467 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: manage/exits only
2026-09-10 13:51:02,640 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-10 13:51:02,698 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (180 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |   111 | INFO |
| Total closed lots           |  2157 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1168 med=-17.2% | TAINTED n=1827 med=-38.8% | KEEP-only n=598 med=+51.4% | KILL=20 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T175614Z

- UTC timestamp: `20260910T175614Z`
- GitHub run: [#9639](https://github.com/28twagg-ops/TradingBot/actions/runs/34511120501)
- Run id: `34511120501`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`29s`
- Full logs: `logs/action_runs/20260910T175614Z_live_bot.log`, `logs/action_runs/20260910T175614Z_live_options.log`, `logs/action_runs/20260910T175614Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1168 | 48.8 | -17.2 | +41.1 | $+15,349 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 598 | 63.4 | +51.4 | +69.1 | $+10,621 |
| KEEP-only recent | 398 | 61.1 | +53.4 | +82.6 | $+5,916 |

- KEEP strategies (22): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T13:56:21.745833-04:00","date":"2026-09-10","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":16.8,"phases_s":{"reconcile":0.38,"cancel":0.17,"manage":12.51,"protective_stops":2.93},"signals":0,"placed":0,"equity":999829.76,"open_positions":34,"pending_orders":0,"open_lots":110,"submitted_today":117,"filled_today":213,"unattributed_contracts":0,"top_signals":[],"github_run":"9639","github_run_id":"34511120501","status":"ok","data_quality":{"clean":{"n":1168,"win":48.8,"med":-17.22,"avg":41.14,"pnl":15349.09},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":598,"win":63.38,"med":51.39,"avg":69.07,"pnl":10621.45},"keep_only_recent":{"n":398,"win":61.06,"med":53.45,"avg":82.63,"pnl":5916.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
17:56:16  INFO      Mode: exits
17:56:16  INFO        Daily log -> logs/daily/2026-09-10.md
17:56:16  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
17:56:17  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:56 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T13:56:18.102541-04:00 share=25% ===
2026-09-10 13:56:18,102 INFO === options_live_micro LIVE 2026-09-10T13:56:18.102541-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 13:56:18,313 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: manage/exits only
2026-09-10 13:56:18,483 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-10 13:56:18,541 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (180 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |   110 | INFO |
| Total closed lots           |  2157 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1168 med=-17.2% | TAINTED n=1827 med=-38.8% | KEEP-only n=598 med=+51.4% | KILL=20 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T180125Z

- UTC timestamp: `20260910T180125Z`
- GitHub run: [#9640](https://github.com/28twagg-ops/TradingBot/actions/runs/34511622329)
- Run id: `34511622329`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`31s`
- Full logs: `logs/action_runs/20260910T180125Z_live_bot.log`, `logs/action_runs/20260910T180125Z_live_options.log`, `logs/action_runs/20260910T180125Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1169 | 48.8 | -17.2 | +41.1 | $+15,320 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 599 | 63.3 | +51.4 | +68.9 | $+10,592 |
| KEEP-only recent | 399 | 60.9 | +53.3 | +82.3 | $+5,887 |

- KEEP strategies (22): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T14:01:32.604690-04:00","date":"2026-09-10","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":19.3,"phases_s":{"reconcile":0.54,"cancel":0.21,"manage":14.43,"protective_stops":3.39},"signals":0,"placed":0,"equity":999766.75,"open_positions":34,"pending_orders":0,"open_lots":109,"submitted_today":117,"filled_today":213,"unattributed_contracts":0,"top_signals":[],"github_run":"9640","github_run_id":"34511622329","status":"ok","data_quality":{"clean":{"n":1169,"win":48.76,"med":-17.24,"avg":41.07,"pnl":15320.09},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":599,"win":63.27,"med":51.39,"avg":68.87,"pnl":10592.45},"keep_only_recent":{"n":399,"win":60.9,"med":53.33,"avg":82.3,"pnl":5887.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
18:01:26  INFO      Mode: exits
18:01:27  INFO        Daily log -> logs/daily/2026-09-10.md
18:01:27  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
18:01:27  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T14:01:28.483704-04:00 share=25% ===
2026-09-10 14:01:28,483 INFO === options_live_micro LIVE 2026-09-10T14:01:28.483704-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 14:01:28,719 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: manage/exits only
2026-09-10 14:01:28,936 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-10 14:01:29,008 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (179 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |   109 | INFO |
| Total closed lots           |  2158 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1169 med=-17.2% | TAINTED n=1827 med=-38.8% | KEEP-only n=599 med=+51.4% | KILL=20 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T180606Z

- UTC timestamp: `20260910T180606Z`
- GitHub run: [#9641](https://github.com/28twagg-ops/TradingBot/actions/runs/34512135218)
- Run id: `34512135218`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`23s`
- Full logs: `logs/action_runs/20260910T180606Z_live_bot.log`, `logs/action_runs/20260910T180606Z_live_options.log`, `logs/action_runs/20260910T180606Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1170 | 48.7 | -18.7 | +41.0 | $+15,289 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 600 | 63.2 | +51.2 | +68.7 | $+10,561 |
| KEEP-only recent | 400 | 60.8 | +53.3 | +82.0 | $+5,856 |

- KEEP strategies (22): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T14:06:13.350042-04:00","date":"2026-09-10","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":11.0,"phases_s":{"reconcile":0.15,"cancel":0.04,"manage":9.18,"protective_stops":0.75},"signals":0,"placed":0,"equity":999608.71,"open_positions":34,"pending_orders":0,"open_lots":108,"submitted_today":117,"filled_today":213,"unattributed_contracts":0,"top_signals":[],"github_run":"9641","github_run_id":"34512135218","status":"ok","data_quality":{"clean":{"n":1170,"win":48.72,"med":-18.7,"avg":40.99,"pnl":15289.09},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":600,"win":63.17,"med":51.18,"avg":68.67,"pnl":10561.45},"keep_only_recent":{"n":400,"win":60.75,"med":53.33,"avg":81.97,"pnl":5856.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
18:06:09  INFO      Mode: exits
18:06:09  INFO        Daily log -> logs/daily/2026-09-10.md
18:06:09  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
18:06:09  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T14:06:10.489759-04:00 share=25% ===
2026-09-10 14:06:10,489 INFO === options_live_micro LIVE 2026-09-10T14:06:10.489759-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 14:06:10,530 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: manage/exits only
2026-09-10 14:06:10,551 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-10 14:06:10,557 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (179 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |   108 | INFO |
| Total closed lots           |  2159 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1170 med=-18.7% | TAINTED n=1827 med=-38.8% | KEEP-only n=600 med=+51.2% | KILL=20 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T181124Z

- UTC timestamp: `20260910T181124Z`
- GitHub run: [#9642](https://github.com/28twagg-ops/TradingBot/actions/runs/34512644183)
- Run id: `34512644183`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`22s`
- Full logs: `logs/action_runs/20260910T181124Z_live_bot.log`, `logs/action_runs/20260910T181124Z_live_options.log`, `logs/action_runs/20260910T181124Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1171 | 48.7 | -20.1 | +40.9 | $+15,258 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 601 | 63.1 | +51.0 | +68.5 | $+10,530 |
| KEEP-only recent | 401 | 60.6 | +53.3 | +81.6 | $+5,825 |

- KEEP strategies (22): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T14:11:29.146853-04:00","date":"2026-09-10","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":11.0,"phases_s":{"reconcile":0.45,"cancel":0.05,"manage":9.15,"protective_stops":0.76},"signals":0,"placed":0,"equity":999608.18,"open_positions":33,"pending_orders":0,"open_lots":106,"submitted_today":117,"filled_today":213,"unattributed_contracts":0,"top_signals":[],"github_run":"9642","github_run_id":"34512644183","status":"ok","data_quality":{"clean":{"n":1171,"win":48.68,"med":-20.15,"avg":40.91,"pnl":15258.09},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":601,"win":63.06,"med":50.98,"avg":68.47,"pnl":10530.45},"keep_only_recent":{"n":401,"win":60.6,"med":53.33,"avg":81.63,"pnl":5825.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
18:11:25  INFO      Mode: exits
18:11:25  INFO        Daily log -> logs/daily/2026-09-10.md
18:11:25  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
18:11:25  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T14:11:26.364411-04:00 share=25% ===
2026-09-10 14:11:26,364 INFO === options_live_micro LIVE 2026-09-10T14:11:26.364411-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 14:11:26,421 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: manage/exits only
2026-09-10 14:11:26,453 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-10 14:11:26,464 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (184 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |   106 | INFO |
| Total closed lots           |  2160 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1171 med=-20.1% | TAINTED n=1827 med=-38.8% | KEEP-only n=601 med=+51.0% | KILL=20 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T181603Z

- UTC timestamp: `20260910T181603Z`
- GitHub run: [#9643](https://github.com/28twagg-ops/TradingBot/actions/runs/34513152453)
- Run id: `34513152453`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`36s`
- Full logs: `logs/action_runs/20260910T181603Z_live_bot.log`, `logs/action_runs/20260910T181603Z_live_options.log`, `logs/action_runs/20260910T181603Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1173 | 48.6 | -22.2 | +40.7 | $+15,205 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 603 | 62.9 | +50.9 | +68.1 | $+10,477 |
| KEEP-only recent | 403 | 60.3 | +53.3 | +81.0 | $+5,772 |

- KEEP strategies (22): S163, S168, S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406
- KILL strategies (20): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S356, S360, S365, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T14:16:10.909430-04:00","date":"2026-09-10","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":23.6,"phases_s":{"reconcile":0.61,"cancel":0.25,"manage":17.6,"protective_stops":4.36},"signals":0,"placed":0,"equity":999640.14,"open_positions":32,"pending_orders":0,"open_lots":104,"submitted_today":117,"filled_today":213,"unattributed_contracts":0,"top_signals":[],"github_run":"9643","github_run_id":"34513152453","status":"ok","data_quality":{"clean":{"n":1173,"win":48.59,"med":-22.22,"avg":40.75,"pnl":15205.09},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":603,"win":62.85,"med":50.94,"avg":68.07,"pnl":10477.45},"keep_only_recent":{"n":403,"win":60.3,"med":53.33,"avg":80.97,"pnl":5772.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S356","S360","S365","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
18:16:04  INFO      Mode: exits
18:16:05  INFO        Daily log -> logs/daily/2026-09-10.md
18:16:05  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
18:16:06  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T14:16:07.173816-04:00 share=25% ===
2026-09-10 14:16:07,173 INFO === options_live_micro LIVE 2026-09-10T14:16:07.173816-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 14:16:07,424 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: manage/exits only
2026-09-10 14:16:07,649 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-10 14:16:07,725 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (182 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |   104 | INFO |
| Total closed lots           |  2162 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1173 med=-22.2% | TAINTED n=1827 med=-38.8% | KEEP-only n=603 med=+50.9% | KILL=20 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T182109Z

- UTC timestamp: `20260910T182109Z`
- GitHub run: [#9644](https://github.com/28twagg-ops/TradingBot/actions/runs/34513671148)
- Run id: `34513671148`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`21s`
- Full logs: `logs/action_runs/20260910T182109Z_live_bot.log`, `logs/action_runs/20260910T182109Z_live_options.log`, `logs/action_runs/20260910T182109Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1174 | 48.6 | -22.6 | +40.7 | $+15,187 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 583 | 63.3 | +51.4 | +67.3 | $+10,446 |
| KEEP-only recent | 386 | 61.1 | +53.4 | +80.3 | $+5,801 |

- KEEP strategies (21): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406
- KILL strategies (21): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S356, S360, S365, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T14:21:14.317377-04:00","date":"2026-09-10","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":9.7,"phases_s":{"reconcile":0.14,"cancel":0.03,"manage":8.3,"protective_stops":0.66},"signals":0,"placed":0,"equity":999688.6,"open_positions":32,"pending_orders":0,"open_lots":102,"submitted_today":117,"filled_today":213,"unattributed_contracts":0,"top_signals":[],"github_run":"9644","github_run_id":"34513671148","status":"ok","data_quality":{"clean":{"n":1174,"win":48.55,"med":-22.59,"avg":40.67,"pnl":15187.09},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":583,"win":63.29,"med":51.39,"avg":67.28,"pnl":10446.45},"keep_only_recent":{"n":386,"win":61.14,"med":53.45,"avg":80.3,"pnl":5801.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S356","S360","S365","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
18:21:10  INFO      Mode: exits
18:21:10  INFO        Daily log -> logs/daily/2026-09-10.md
18:21:10  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
18:21:10  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T14:21:11.569098-04:00 share=25% ===
2026-09-10 14:21:11,569 INFO === options_live_micro LIVE 2026-09-10T14:21:11.569098-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 14:21:11,609 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: manage/exits only
2026-09-10 14:21:11,628 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-10 14:21:11,634 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (180 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |   102 | INFO |
| Total closed lots           |  2163 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1174 med=-22.6% | TAINTED n=1827 med=-38.8% | KEEP-only n=583 med=+51.4% | KILL=21 KEEP=21
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T182643Z

- UTC timestamp: `20260910T182643Z`
- GitHub run: [#9645](https://github.com/28twagg-ops/TradingBot/actions/runs/34514186694)
- Run id: `34514186694`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`21s`
- Full logs: `logs/action_runs/20260910T182643Z_live_bot.log`, `logs/action_runs/20260910T182643Z_live_options.log`, `logs/action_runs/20260910T182643Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1174 | 48.6 | -22.6 | +40.7 | $+15,187 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 583 | 63.3 | +51.4 | +67.3 | $+10,446 |
| KEEP-only recent | 386 | 61.1 | +53.4 | +80.3 | $+5,801 |

- KEEP strategies (21): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406
- KILL strategies (21): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S356, S360, S365, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T14:26:48.843583-04:00","date":"2026-09-10","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":9.4,"phases_s":{"reconcile":0.19,"cancel":0.03,"manage":7.85,"protective_stops":0.59},"signals":0,"placed":0,"equity":999700.1,"open_positions":32,"pending_orders":0,"open_lots":102,"submitted_today":117,"filled_today":213,"unattributed_contracts":0,"top_signals":[],"github_run":"9645","github_run_id":"34514186694","status":"ok","data_quality":{"clean":{"n":1174,"win":48.55,"med":-22.59,"avg":40.67,"pnl":15187.09},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":583,"win":63.29,"med":51.39,"avg":67.28,"pnl":10446.45},"keep_only_recent":{"n":386,"win":61.14,"med":53.45,"avg":80.3,"pnl":5801.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S356","S360","S365","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
18:26:44  INFO      Mode: exits
18:26:44  INFO        Daily log -> logs/daily/2026-09-10.md
18:26:44  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
18:26:44  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T14:26:45.819836-04:00 share=25% ===
2026-09-10 14:26:45,819 INFO === options_live_micro LIVE 2026-09-10T14:26:45.819836-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 14:26:45,932 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: manage/exits only
2026-09-10 14:26:45,953 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-10 14:26:45,959 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (178 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |   102 | INFO |
| Total closed lots           |  2163 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1174 med=-22.6% | TAINTED n=1827 med=-38.8% | KEEP-only n=583 med=+51.4% | KILL=21 KEEP=21
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T183114Z

- UTC timestamp: `20260910T183114Z`
- GitHub run: [#9646](https://github.com/28twagg-ops/TradingBot/actions/runs/34514711952)
- Run id: `34514711952`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`24s`
- Full logs: `logs/action_runs/20260910T183114Z_live_bot.log`, `logs/action_runs/20260910T183114Z_live_options.log`, `logs/action_runs/20260910T183114Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1174 | 48.6 | -22.6 | +40.7 | $+15,187 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 583 | 63.3 | +51.4 | +67.3 | $+10,446 |
| KEEP-only recent | 386 | 61.1 | +53.4 | +80.3 | $+5,801 |

- KEEP strategies (21): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406
- KILL strategies (21): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S356, S360, S365, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T14:31:20.760064-04:00","date":"2026-09-10","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":13.0,"phases_s":{"reconcile":0.25,"cancel":0.08,"manage":10.29,"protective_stops":1.52},"signals":0,"placed":0,"equity":999556.55,"open_positions":31,"pending_orders":0,"open_lots":100,"submitted_today":117,"filled_today":213,"unattributed_contracts":0,"top_signals":[],"github_run":"9646","github_run_id":"34514711952","status":"ok","data_quality":{"clean":{"n":1174,"win":48.55,"med":-22.59,"avg":40.67,"pnl":15187.09},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":583,"win":63.29,"med":51.39,"avg":67.28,"pnl":10446.45},"keep_only_recent":{"n":386,"win":61.14,"med":53.45,"avg":80.3,"pnl":5801.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S356","S360","S365","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
18:31:15  INFO      Mode: exits
18:31:16  INFO        Daily log -> logs/daily/2026-09-10.md
18:31:16  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
18:31:16  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T14:31:17.687900-04:00 share=25% ===
2026-09-10 14:31:17,687 INFO === options_live_micro LIVE 2026-09-10T14:31:17.687900-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 14:31:17,792 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: manage/exits only
2026-09-10 14:31:17,878 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-10 14:31:17,899 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (181 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |   100 | INFO |
| Total closed lots           |  2163 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1174 med=-22.6% | TAINTED n=1827 med=-38.8% | KEEP-only n=583 med=+51.4% | KILL=21 KEEP=21
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T183603Z

- UTC timestamp: `20260910T183603Z`
- GitHub run: [#9647](https://github.com/28twagg-ops/TradingBot/actions/runs/34515226394)
- Run id: `34515226394`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`23s`
- Full logs: `logs/action_runs/20260910T183603Z_live_bot.log`, `logs/action_runs/20260910T183603Z_live_options.log`, `logs/action_runs/20260910T183603Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1174 | 48.6 | -22.6 | +40.7 | $+15,187 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 583 | 63.3 | +51.4 | +67.3 | $+10,446 |
| KEEP-only recent | 386 | 61.1 | +53.4 | +80.3 | $+5,801 |

- KEEP strategies (21): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406
- KILL strategies (21): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S356, S360, S365, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T14:36:09.066908-04:00","date":"2026-09-10","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":11.9,"phases_s":{"reconcile":0.19,"cancel":0.08,"manage":9.74,"protective_stops":1.28},"signals":0,"placed":0,"equity":999541.54,"open_positions":31,"pending_orders":0,"open_lots":100,"submitted_today":117,"filled_today":213,"unattributed_contracts":0,"top_signals":[],"github_run":"9647","github_run_id":"34515226394","status":"ok","data_quality":{"clean":{"n":1174,"win":48.55,"med":-22.59,"avg":40.67,"pnl":15187.09},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":583,"win":63.29,"med":51.39,"avg":67.28,"pnl":10446.45},"keep_only_recent":{"n":386,"win":61.14,"med":53.45,"avg":80.3,"pnl":5801.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S356","S360","S365","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
18:36:04  INFO      Mode: exits
18:36:05  INFO        Daily log -> logs/daily/2026-09-10.md
18:36:05  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
18:36:05  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T14:36:06.030538-04:00 share=25% ===
2026-09-10 14:36:06,030 INFO === options_live_micro LIVE 2026-09-10T14:36:06.030538-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 14:36:06,122 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: manage/exits only
2026-09-10 14:36:06,185 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-10 14:36:06,205 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (178 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |   100 | INFO |
| Total closed lots           |  2163 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1174 med=-22.6% | TAINTED n=1827 med=-38.8% | KEEP-only n=583 med=+51.4% | KILL=21 KEEP=21
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T184103Z

- UTC timestamp: `20260910T184103Z`
- GitHub run: [#9648](https://github.com/28twagg-ops/TradingBot/actions/runs/34515731478)
- Run id: `34515731478`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`21s`
- Full logs: `logs/action_runs/20260910T184103Z_live_bot.log`, `logs/action_runs/20260910T184103Z_live_options.log`, `logs/action_runs/20260910T184103Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1174 | 48.6 | -22.6 | +40.7 | $+15,187 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 583 | 63.3 | +51.4 | +67.3 | $+10,446 |
| KEEP-only recent | 386 | 61.1 | +53.4 | +80.3 | $+5,801 |

- KEEP strategies (21): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406
- KILL strategies (21): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S356, S360, S365, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T14:41:08.510394-04:00","date":"2026-09-10","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":9.2,"phases_s":{"reconcile":0.16,"cancel":0.03,"manage":7.86,"protective_stops":0.57},"signals":0,"placed":0,"equity":999629.55,"open_positions":31,"pending_orders":0,"open_lots":100,"submitted_today":117,"filled_today":213,"unattributed_contracts":0,"top_signals":[],"github_run":"9648","github_run_id":"34515731478","status":"ok","data_quality":{"clean":{"n":1174,"win":48.55,"med":-22.59,"avg":40.67,"pnl":15187.09},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":583,"win":63.29,"med":51.39,"avg":67.28,"pnl":10446.45},"keep_only_recent":{"n":386,"win":61.14,"med":53.45,"avg":80.3,"pnl":5801.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S356","S360","S365","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
18:41:04  INFO      Mode: exits
18:41:04  INFO        Daily log -> logs/daily/2026-09-10.md
18:41:04  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
18:41:04  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T14:41:05.724808-04:00 share=25% ===
2026-09-10 14:41:05,724 INFO === options_live_micro LIVE 2026-09-10T14:41:05.724808-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 14:41:05,765 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: manage/exits only
2026-09-10 14:41:05,783 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-10 14:41:05,790 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (178 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |   100 | INFO |
| Total closed lots           |  2163 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1174 med=-22.6% | TAINTED n=1827 med=-38.8% | KEEP-only n=583 med=+51.4% | KILL=21 KEEP=21
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T184609Z

- UTC timestamp: `20260910T184609Z`
- GitHub run: [#9649](https://github.com/28twagg-ops/TradingBot/actions/runs/34516234884)
- Run id: `34516234884`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`29s`
- Full logs: `logs/action_runs/20260910T184609Z_live_bot.log`, `logs/action_runs/20260910T184609Z_live_options.log`, `logs/action_runs/20260910T184609Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1174 | 48.6 | -22.6 | +40.7 | $+15,187 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 583 | 63.3 | +51.4 | +67.3 | $+10,446 |
| KEEP-only recent | 386 | 61.1 | +53.4 | +80.3 | $+5,801 |

- KEEP strategies (21): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406
- KILL strategies (21): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S356, S360, S365, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T14:46:16.461353-04:00","date":"2026-09-10","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":18.0,"phases_s":{"reconcile":0.49,"cancel":0.19,"manage":13.53,"protective_stops":3.12},"signals":0,"placed":0,"equity":999683.8,"open_positions":31,"pending_orders":0,"open_lots":100,"submitted_today":117,"filled_today":213,"unattributed_contracts":0,"top_signals":[],"github_run":"9649","github_run_id":"34516234884","status":"ok","data_quality":{"clean":{"n":1174,"win":48.55,"med":-22.59,"avg":40.67,"pnl":15187.09},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":583,"win":63.29,"med":51.39,"avg":67.28,"pnl":10446.45},"keep_only_recent":{"n":386,"win":61.14,"med":53.45,"avg":80.3,"pnl":5801.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S356","S360","S365","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
18:46:10  INFO      Mode: exits
18:46:11  INFO        Daily log -> logs/daily/2026-09-10.md
18:46:11  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
18:46:11  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T14:46:12.503635-04:00 share=25% ===
2026-09-10 14:46:12,503 INFO === options_live_micro LIVE 2026-09-10T14:46:12.503635-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 14:46:12,710 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: manage/exits only
2026-09-10 14:46:12,888 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-10 14:46:12,944 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (178 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |   100 | INFO |
| Total closed lots           |  2163 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1174 med=-22.6% | TAINTED n=1827 med=-38.8% | KEEP-only n=583 med=+51.4% | KILL=21 KEEP=21
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T185153Z

- UTC timestamp: `20260910T185153Z`
- GitHub run: [#9650](https://github.com/28twagg-ops/TradingBot/actions/runs/34516743749)
- Run id: `34516743749`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`23s`
- Full logs: `logs/action_runs/20260910T185153Z_live_bot.log`, `logs/action_runs/20260910T185153Z_live_options.log`, `logs/action_runs/20260910T185153Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1174 | 48.6 | -22.6 | +40.7 | $+15,187 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 583 | 63.3 | +51.4 | +67.3 | $+10,446 |
| KEEP-only recent | 386 | 61.1 | +53.4 | +80.3 | $+5,801 |

- KEEP strategies (21): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406
- KILL strategies (21): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S356, S360, S365, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T14:51:59.984130-04:00","date":"2026-09-10","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":10.1,"phases_s":{"reconcile":0.21,"cancel":0.06,"manage":8.66,"protective_stops":0.57},"signals":0,"placed":0,"equity":999692.55,"open_positions":31,"pending_orders":0,"open_lots":100,"submitted_today":117,"filled_today":213,"unattributed_contracts":0,"top_signals":[],"github_run":"9650","github_run_id":"34516743749","status":"ok","data_quality":{"clean":{"n":1174,"win":48.55,"med":-22.59,"avg":40.67,"pnl":15187.09},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":583,"win":63.29,"med":51.39,"avg":67.28,"pnl":10446.45},"keep_only_recent":{"n":386,"win":61.14,"med":53.45,"avg":80.3,"pnl":5801.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S356","S360","S365","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
18:51:55  INFO      Mode: exits
18:51:55  INFO        Daily log -> logs/daily/2026-09-10.md
18:51:55  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
18:51:55  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:51 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T14:51:56.797890-04:00 share=25% ===
2026-09-10 14:51:56,797 INFO === options_live_micro LIVE 2026-09-10T14:51:56.797890-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 14:51:56,838 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: manage/exits only
2026-09-10 14:51:56,856 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-10 14:51:56,862 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (178 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |   100 | INFO |
| Total closed lots           |  2163 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1174 med=-22.6% | TAINTED n=1827 med=-38.8% | KEEP-only n=583 med=+51.4% | KILL=21 KEEP=21
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T185724Z

- UTC timestamp: `20260910T185724Z`
- GitHub run: [#9651](https://github.com/28twagg-ops/TradingBot/actions/runs/34517243307)
- Run id: `34517243307`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`29s`
- Full logs: `logs/action_runs/20260910T185724Z_live_bot.log`, `logs/action_runs/20260910T185724Z_live_options.log`, `logs/action_runs/20260910T185724Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1174 | 48.6 | -22.6 | +40.7 | $+15,187 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 583 | 63.3 | +51.4 | +67.3 | $+10,446 |
| KEEP-only recent | 386 | 61.1 | +53.4 | +80.3 | $+5,801 |

- KEEP strategies (21): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406
- KILL strategies (21): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S356, S360, S365, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T14:57:30.758133-04:00","date":"2026-09-10","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":18.0,"phases_s":{"reconcile":0.44,"cancel":0.18,"manage":13.52,"protective_stops":3.02},"signals":0,"placed":0,"equity":999658.9,"open_positions":31,"pending_orders":0,"open_lots":100,"submitted_today":117,"filled_today":213,"unattributed_contracts":0,"top_signals":[],"github_run":"9651","github_run_id":"34517243307","status":"ok","data_quality":{"clean":{"n":1174,"win":48.55,"med":-22.59,"avg":40.67,"pnl":15187.09},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":583,"win":63.29,"med":51.39,"avg":67.28,"pnl":10446.45},"keep_only_recent":{"n":386,"win":61.14,"med":53.45,"avg":80.3,"pnl":5801.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S356","S360","S365","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
18:57:25  INFO      Mode: exits
18:57:26  INFO        Daily log -> logs/daily/2026-09-10.md
18:57:26  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
18:57:26  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:57 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T14:57:27.336213-04:00 share=25% ===
2026-09-10 14:57:27,336 INFO === options_live_micro LIVE 2026-09-10T14:57:27.336213-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 14:57:27,541 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: manage/exits only
2026-09-10 14:57:27,711 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-10 14:57:27,768 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (178 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |   100 | INFO |
| Total closed lots           |  2163 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1174 med=-22.6% | TAINTED n=1827 med=-38.8% | KEEP-only n=583 med=+51.4% | KILL=21 KEEP=21
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T190107Z

- UTC timestamp: `20260910T190107Z`
- GitHub run: [#9652](https://github.com/28twagg-ops/TradingBot/actions/runs/34517740777)
- Run id: `34517740777`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`25s`
- Full logs: `logs/action_runs/20260910T190107Z_live_bot.log`, `logs/action_runs/20260910T190107Z_live_options.log`, `logs/action_runs/20260910T190107Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1174 | 48.6 | -22.6 | +40.7 | $+15,187 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 583 | 63.3 | +51.4 | +67.3 | $+10,446 |
| KEEP-only recent | 386 | 61.1 | +53.4 | +80.3 | $+5,801 |

- KEEP strategies (21): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406
- KILL strategies (21): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S356, S360, S365, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T15:01:13.318361-04:00","date":"2026-09-10","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":13.4,"phases_s":{"reconcile":0.16,"cancel":0.05,"manage":11.61,"protective_stops":1.08},"signals":0,"placed":0,"equity":999702.55,"open_positions":31,"pending_orders":0,"open_lots":100,"submitted_today":117,"filled_today":213,"unattributed_contracts":0,"top_signals":[],"github_run":"9652","github_run_id":"34517740777","status":"ok","data_quality":{"clean":{"n":1174,"win":48.55,"med":-22.59,"avg":40.67,"pnl":15187.09},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":583,"win":63.29,"med":51.39,"avg":67.28,"pnl":10446.45},"keep_only_recent":{"n":386,"win":61.14,"med":53.45,"avg":80.3,"pnl":5801.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S356","S360","S365","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
19:01:08  INFO      Mode: exits
19:01:08  INFO        Daily log -> logs/daily/2026-09-10.md
19:01:08  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
19:01:08  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         19:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T15:01:10.124406-04:00 share=25% ===
2026-09-10 15:01:10,124 INFO === options_live_micro LIVE 2026-09-10T15:01:10.124406-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 15:01:10,183 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: manage/exits only
2026-09-10 15:01:10,289 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-10 15:01:10,299 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (178 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |   100 | INFO |
| Total closed lots           |  2163 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1174 med=-22.6% | TAINTED n=1827 med=-38.8% | KEEP-only n=583 med=+51.4% | KILL=21 KEEP=21
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T190611Z

- UTC timestamp: `20260910T190611Z`
- GitHub run: [#9653](https://github.com/28twagg-ops/TradingBot/actions/runs/34518258221)
- Run id: `34518258221`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`21s`
- Full logs: `logs/action_runs/20260910T190611Z_live_bot.log`, `logs/action_runs/20260910T190611Z_live_options.log`, `logs/action_runs/20260910T190611Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1174 | 48.6 | -22.6 | +40.7 | $+15,187 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 583 | 63.3 | +51.4 | +67.3 | $+10,446 |
| KEEP-only recent | 386 | 61.1 | +53.4 | +80.3 | $+5,801 |

- KEEP strategies (21): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406
- KILL strategies (21): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S356, S360, S365, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T15:06:16.370684-04:00","date":"2026-09-10","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":9.1,"phases_s":{"reconcile":0.11,"cancel":0.03,"manage":7.82,"protective_stops":0.61},"signals":0,"placed":0,"equity":999536.55,"open_positions":31,"pending_orders":0,"open_lots":100,"submitted_today":117,"filled_today":213,"unattributed_contracts":0,"top_signals":[],"github_run":"9653","github_run_id":"34518258221","status":"ok","data_quality":{"clean":{"n":1174,"win":48.55,"med":-22.59,"avg":40.67,"pnl":15187.09},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":583,"win":63.29,"med":51.39,"avg":67.28,"pnl":10446.45},"keep_only_recent":{"n":386,"win":61.14,"med":53.45,"avg":80.3,"pnl":5801.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S356","S360","S365","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
19:06:12  INFO      Mode: exits
19:06:12  INFO        Daily log -> logs/daily/2026-09-10.md
19:06:12  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
19:06:12  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         19:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T15:06:13.632882-04:00 share=25% ===
2026-09-10 15:06:13,632 INFO === options_live_micro LIVE 2026-09-10T15:06:13.632882-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 15:06:13,679 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: manage/exits only
2026-09-10 15:06:13,702 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-10 15:06:13,709 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (178 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |   100 | INFO |
| Total closed lots           |  2163 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1174 med=-22.6% | TAINTED n=1827 med=-38.8% | KEEP-only n=583 med=+51.4% | KILL=21 KEEP=21
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T191109Z

- UTC timestamp: `20260910T191109Z`
- GitHub run: [#9654](https://github.com/28twagg-ops/TradingBot/actions/runs/34518762109)
- Run id: `34518762109`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`28s`
- Full logs: `logs/action_runs/20260910T191109Z_live_bot.log`, `logs/action_runs/20260910T191109Z_live_options.log`, `logs/action_runs/20260910T191109Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1174 | 48.6 | -22.6 | +40.7 | $+15,187 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 583 | 63.3 | +51.4 | +67.3 | $+10,446 |
| KEEP-only recent | 386 | 61.1 | +53.4 | +80.3 | $+5,801 |

- KEEP strategies (21): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406
- KILL strategies (21): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S356, S360, S365, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T15:11:15.826927-04:00","date":"2026-09-10","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":17.4,"phases_s":{"reconcile":0.72,"cancel":0.18,"manage":12.77,"protective_stops":2.99},"signals":0,"placed":0,"equity":999633.05,"open_positions":31,"pending_orders":0,"open_lots":100,"submitted_today":117,"filled_today":213,"unattributed_contracts":0,"top_signals":[],"github_run":"9654","github_run_id":"34518762109","status":"ok","data_quality":{"clean":{"n":1174,"win":48.55,"med":-22.59,"avg":40.67,"pnl":15187.09},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":583,"win":63.29,"med":51.39,"avg":67.28,"pnl":10446.45},"keep_only_recent":{"n":386,"win":61.14,"med":53.45,"avg":80.3,"pnl":5801.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S356","S360","S365","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
19:11:10  INFO      Mode: exits
19:11:11  INFO        Daily log -> logs/daily/2026-09-10.md
19:11:11  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
19:11:11  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         19:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T15:11:12.277467-04:00 share=25% ===
2026-09-10 15:11:12,277 INFO === options_live_micro LIVE 2026-09-10T15:11:12.277467-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 15:11:12,475 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: manage/exits only
2026-09-10 15:11:12,648 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-10 15:11:12,705 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (178 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |   100 | INFO |
| Total closed lots           |  2163 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1174 med=-22.6% | TAINTED n=1827 med=-38.8% | KEEP-only n=583 med=+51.4% | KILL=21 KEEP=21
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T191559Z

- UTC timestamp: `20260910T191559Z`
- GitHub run: [#9655](https://github.com/28twagg-ops/TradingBot/actions/runs/34519269288)
- Run id: `34519269288`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`24s`
- Full logs: `logs/action_runs/20260910T191559Z_live_bot.log`, `logs/action_runs/20260910T191559Z_live_options.log`, `logs/action_runs/20260910T191559Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1174 | 48.6 | -22.6 | +40.7 | $+15,187 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 583 | 63.3 | +51.4 | +67.3 | $+10,446 |
| KEEP-only recent | 386 | 61.1 | +53.4 | +80.3 | $+5,801 |

- KEEP strategies (21): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406
- KILL strategies (21): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S356, S360, S365, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T15:16:04.318904-04:00","date":"2026-09-10","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":13.4,"phases_s":{"reconcile":0.29,"cancel":0.09,"manage":10.62,"protective_stops":1.8},"signals":0,"placed":0,"equity":999644.54,"open_positions":31,"pending_orders":0,"open_lots":100,"submitted_today":117,"filled_today":213,"unattributed_contracts":0,"top_signals":[],"github_run":"9655","github_run_id":"34519269288","status":"ok","data_quality":{"clean":{"n":1174,"win":48.55,"med":-22.59,"avg":40.67,"pnl":15187.09},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":583,"win":63.29,"med":51.39,"avg":67.28,"pnl":10446.45},"keep_only_recent":{"n":386,"win":61.14,"med":53.45,"avg":80.3,"pnl":5801.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S356","S360","S365","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
19:16:00  INFO      Mode: exits
19:16:00  INFO        Daily log -> logs/daily/2026-09-10.md
19:16:00  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
19:16:00  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         19:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T15:16:01.499407-04:00 share=25% ===
2026-09-10 15:16:01,499 INFO === options_live_micro LIVE 2026-09-10T15:16:01.499407-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 15:16:01,593 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: manage/exits only
2026-09-10 15:16:01,666 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-10 15:16:01,690 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (178 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |   100 | INFO |
| Total closed lots           |  2163 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1174 med=-22.6% | TAINTED n=1827 med=-38.8% | KEEP-only n=583 med=+51.4% | KILL=21 KEEP=21
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T192212Z

- UTC timestamp: `20260910T192212Z`
- GitHub run: [#9656](https://github.com/28twagg-ops/TradingBot/actions/runs/34519773660)
- Run id: `34519773660`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`21s`
- Full logs: `logs/action_runs/20260910T192212Z_live_bot.log`, `logs/action_runs/20260910T192212Z_live_options.log`, `logs/action_runs/20260910T192212Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1174 | 48.6 | -22.6 | +40.7 | $+15,187 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 583 | 63.3 | +51.4 | +67.3 | $+10,446 |
| KEEP-only recent | 386 | 61.1 | +53.4 | +80.3 | $+5,801 |

- KEEP strategies (21): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406
- KILL strategies (21): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S356, S360, S365, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T15:22:18.215217-04:00","date":"2026-09-10","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":14.0,"phases_s":{"reconcile":0.43,"cancel":0.1,"manage":11.08,"protective_stops":1.71},"signals":0,"placed":0,"equity":999502.55,"open_positions":31,"pending_orders":0,"open_lots":100,"submitted_today":117,"filled_today":213,"unattributed_contracts":0,"top_signals":[],"github_run":"9656","github_run_id":"34519773660","status":"ok","data_quality":{"clean":{"n":1174,"win":48.55,"med":-22.59,"avg":40.67,"pnl":15187.09},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":583,"win":63.29,"med":51.39,"avg":67.28,"pnl":10446.45},"keep_only_recent":{"n":386,"win":61.14,"med":53.45,"avg":80.3,"pnl":5801.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S356","S360","S365","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
19:22:13  INFO      Mode: exits
19:22:14  INFO        Daily log -> logs/daily/2026-09-10.md
19:22:14  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
19:22:14  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         19:22 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T15:22:15.321882-04:00 share=25% ===
2026-09-10 15:22:15,321 INFO === options_live_micro LIVE 2026-09-10T15:22:15.321882-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 15:22:15,459 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: manage/exits only
2026-09-10 15:22:15,569 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-10 15:22:15,606 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (180 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |   100 | INFO |
| Total closed lots           |  2163 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1174 med=-22.6% | TAINTED n=1827 med=-38.8% | KEEP-only n=583 med=+51.4% | KILL=21 KEEP=21
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T192604Z

- UTC timestamp: `20260910T192604Z`
- GitHub run: [#9657](https://github.com/28twagg-ops/TradingBot/actions/runs/34520275934)
- Run id: `34520275934`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`29s`
- Full logs: `logs/action_runs/20260910T192604Z_live_bot.log`, `logs/action_runs/20260910T192604Z_live_options.log`, `logs/action_runs/20260910T192604Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1174 | 48.6 | -22.6 | +40.7 | $+15,187 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 583 | 63.3 | +51.4 | +67.3 | $+10,446 |
| KEEP-only recent | 386 | 61.1 | +53.4 | +80.3 | $+5,801 |

- KEEP strategies (21): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406
- KILL strategies (21): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S356, S360, S365, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T15:26:12.326167-04:00","date":"2026-09-10","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":16.2,"phases_s":{"reconcile":0.37,"cancel":0.17,"manage":12.01,"protective_stops":2.92},"signals":0,"placed":0,"equity":999442.5,"open_positions":30,"pending_orders":0,"open_lots":98,"submitted_today":117,"filled_today":213,"unattributed_contracts":0,"top_signals":[],"github_run":"9657","github_run_id":"34520275934","status":"ok","data_quality":{"clean":{"n":1174,"win":48.55,"med":-22.59,"avg":40.67,"pnl":15187.09},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":583,"win":63.29,"med":51.39,"avg":67.28,"pnl":10446.45},"keep_only_recent":{"n":386,"win":61.14,"med":53.45,"avg":80.3,"pnl":5801.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S356","S360","S365","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
19:26:05  INFO      Mode: exits
19:26:06  INFO        Daily log -> logs/daily/2026-09-10.md
19:26:06  INFO        Daily log reconciled -> logs/daily/2026-09-10.md (5 ledger rows)
19:26:07  INFO        Daily log -> logs/daily/2026-09-10.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         19:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
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
=== options_live_micro LIVE 2026-09-10T15:26:08.004539-04:00 share=25% ===
2026-09-10 15:26:08,004 INFO === options_live_micro LIVE 2026-09-10T15:26:08.004539-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 15:26:08,211 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: manage/exits only
2026-09-10 15:26:08,380 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-10 15:26:08,436 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (184 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    98 | INFO |
| Total closed lots           |  2163 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1174 med=-22.6% | TAINTED n=1827 med=-38.8% | KEEP-only n=583 med=+51.4% | KILL=21 KEEP=21
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T193102Z

- UTC timestamp: `20260910T193102Z`
- GitHub run: [#9658](https://github.com/28twagg-ops/TradingBot/actions/runs/34520754973)
- Run id: `34520754973`
- Live bot: exit=`0`, duration=`217s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`28s`
- Full logs: `logs/action_runs/20260910T193102Z_live_bot.log`, `logs/action_runs/20260910T193102Z_live_options.log`, `logs/action_runs/20260910T193102Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1175 | 48.5 | -22.9 | +40.6 | $+15,153 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 583 | 63.3 | +51.4 | +67.3 | $+10,446 |
| KEEP-only recent | 386 | 61.1 | +53.4 | +80.3 | $+5,801 |

- KEEP strategies (21): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406
- KILL strategies (21): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S356, S360, S365, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T15:34:43.193701-04:00","date":"2026-09-10","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":16.4,"phases_s":{"reconcile":0.15,"cancel":0.04,"manage":15.22,"protective_stops":0.5},"signals":0,"placed":0,"equity":999403.48,"open_positions":30,"pending_orders":0,"open_lots":97,"submitted_today":117,"filled_today":213,"unattributed_contracts":0,"top_signals":[],"github_run":"9658","github_run_id":"34520754973","status":"ok","data_quality":{"clean":{"n":1175,"win":48.51,"med":-22.95,"avg":40.6,"pnl":15153.09},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":583,"win":63.29,"med":51.39,"avg":67.28,"pnl":10446.45},"keep_only_recent":{"n":386,"win":61.14,"med":53.45,"avg":80.3,"pnl":5801.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S356","S360","S365","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
19:31:03  INFO      Mode: evening_prep
19:31:04  INFO        Universe cache hit: 903 tickers (tickers_2026-09-10.json)
19:31:05  INFO        [prep_universe] 40/903 (40 valid)
19:31:07  INFO        [prep_universe] 80/903 (80 valid)
19:31:08  INFO        [prep_universe] 120/903 (120 valid)
19:31:10  INFO        [prep_universe] 160/903 (160 valid)
19:31:11  INFO        [prep_universe] 200/903 (199 valid)
19:31:18  INFO        [prep_universe] 240/903 (238 valid)
19:31:31  INFO        [prep_universe] 280/903 (278 valid)
19:31:41  INFO        [prep_universe] 320/903 (318 valid)
19:31:54  INFO        [prep_universe] 360/903 (358 valid)
19:32:07  INFO        [prep_universe] 400/903 (397 valid)
19:32:17  INFO        [prep_universe] 440/903 (437 valid)
19:32:30  INFO        [prep_universe] 480/903 (477 valid)
19:32:42  INFO        [prep_universe] 520/903 (517 valid)
19:32:53  INFO        [prep_universe] 560/903 (557 valid)
19:33:06  INFO        [prep_universe] 600/903 (597 valid)
19:33:18  INFO        [prep_universe] 640/903 (637 valid)
19:33:29  INFO        [prep_universe] 680/903 (677 valid)
19:33:41  INFO        [prep_universe] 720/903 (717 valid)
19:33:54  INFO        [prep_universe] 760/903 (757 valid)
19:34:07  INFO        [prep_universe] 800/903 (797 valid)
19:34:17  INFO        [prep_universe] 840/903 (837 valid)
19:34:30  INFO        [prep_universe] 880/903 (877 valid)
19:34:37  INFO        [prep_universe] 903/903 (900 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      EVENING_PREP|
|  Time                                                         19:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                              EVENING PREP                              |
+========================================================================+
|  Goal                   Precompute exits/signals for next execution run|
|  Plan file                                 logs/plans/evening_plan.json|
|  Regime                                                            BULL|
+========================================================================+

+========================================================================+
|                       OPEN POSITION P&L SNAPSHOT                       |
+========================================================================+
|  Open positions                                                       0|
|  Invested                                                         $0.00|
|  Open P&L                                                        $+0.00|
|                                                                        |
|  No open positions.                                                    |
|                                                                        |
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
|  Exit candidates                                                      0|
|  Signal candidates                                                   28|
|  Universe scanned                                                   903|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-10T15:34:40.457908-04:00 share=25% ===
2026-09-10 15:34:40,457 INFO === options_live_micro LIVE 2026-09-10T15:34:40.457908-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 15:34:40,501 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: manage/exits only
2026-09-10 15:34:40,523 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-10 15:34:40,530 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (181 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    97 | INFO |
| Total closed lots           |  2164 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1175 med=-22.9% | TAINTED n=1827 med=-38.8% | KEEP-only n=583 med=+51.4% | KILL=21 KEEP=21
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T193624Z

- UTC timestamp: `20260910T193624Z`
- GitHub run: [#9659](https://github.com/28twagg-ops/TradingBot/actions/runs/34521261467)
- Run id: `34521261467`
- Live bot: exit=`0`, duration=`217s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`26s`
- Full logs: `logs/action_runs/20260910T193624Z_live_bot.log`, `logs/action_runs/20260910T193624Z_live_options.log`, `logs/action_runs/20260910T193624Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1175 | 48.5 | -22.9 | +40.6 | $+15,153 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 583 | 63.3 | +51.4 | +67.3 | $+10,446 |
| KEEP-only recent | 386 | 61.1 | +53.4 | +80.3 | $+5,801 |

- KEEP strategies (21): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406
- KILL strategies (21): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S356, S360, S365, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T15:40:05.891688-04:00","date":"2026-09-10","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":16.8,"phases_s":{"reconcile":0.49,"cancel":0.19,"manage":12.69,"protective_stops":2.73},"signals":0,"placed":0,"equity":999425.43,"open_positions":29,"pending_orders":0,"open_lots":95,"submitted_today":117,"filled_today":213,"unattributed_contracts":0,"top_signals":[],"github_run":"9659","github_run_id":"34521261467","status":"ok","data_quality":{"clean":{"n":1175,"win":48.51,"med":-22.95,"avg":40.6,"pnl":15153.09},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":583,"win":63.29,"med":51.39,"avg":67.28,"pnl":10446.45},"keep_only_recent":{"n":386,"win":61.14,"med":53.45,"avg":80.3,"pnl":5801.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S356","S360","S365","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
19:36:26  INFO      Mode: evening_prep
19:36:26  INFO        Universe cache hit: 903 tickers (tickers_2026-09-10.json)
19:36:27  INFO        [prep_universe] 40/903 (40 valid)
19:36:29  INFO        [prep_universe] 80/903 (80 valid)
19:36:30  INFO        [prep_universe] 120/903 (120 valid)
19:36:31  INFO        [prep_universe] 160/903 (160 valid)
19:36:32  INFO        [prep_universe] 200/903 (199 valid)
19:36:40  INFO        [prep_universe] 240/903 (238 valid)
19:36:53  INFO        [prep_universe] 280/903 (278 valid)
19:37:03  INFO        [prep_universe] 320/903 (318 valid)
19:37:16  INFO        [prep_universe] 360/903 (358 valid)
19:37:27  INFO        [prep_universe] 400/903 (397 valid)
19:37:40  INFO        [prep_universe] 440/903 (437 valid)
19:37:53  INFO        [prep_universe] 480/903 (477 valid)
19:38:03  INFO        [prep_universe] 520/903 (517 valid)
19:38:16  INFO        [prep_universe] 560/903 (557 valid)
19:38:27  INFO        [prep_universe] 600/903 (597 valid)
19:38:40  INFO        [prep_universe] 640/903 (637 valid)
19:38:53  INFO        [prep_universe] 680/903 (677 valid)
19:39:03  INFO        [prep_universe] 720/903 (717 valid)
19:39:16  INFO        [prep_universe] 760/903 (757 valid)
19:39:27  INFO        [prep_universe] 800/903 (797 valid)
19:39:40  INFO        [prep_universe] 840/903 (837 valid)
19:39:53  INFO        [prep_universe] 880/903 (877 valid)
19:40:00  INFO        [prep_universe] 903/903 (900 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      EVENING_PREP|
|  Time                                                         19:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                              EVENING PREP                              |
+========================================================================+
|  Goal                   Precompute exits/signals for next execution run|
|  Plan file                                 logs/plans/evening_plan.json|
|  Regime                                                            BULL|
+========================================================================+

+========================================================================+
|                       OPEN POSITION P&L SNAPSHOT                       |
+========================================================================+
|  Open positions                                                       0|
|  Invested                                                         $0.00|
|  Open P&L                                                        $+0.00|
|                                                                        |
|  No open positions.                                                    |
|                                                                        |
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
|  Exit candidates                                                      0|
|  Signal candidates                                                   33|
|  Universe scanned                                                   903|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-10T15:40:02.479448-04:00 share=25% ===
2026-09-10 15:40:02,479 INFO === options_live_micro LIVE 2026-09-10T15:40:02.479448-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 15:40:03,055 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: manage/exits only
2026-09-10 15:40:03,224 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-10 15:40:03,279 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (180 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    95 | INFO |
| Total closed lots           |  2164 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1175 med=-22.9% | TAINTED n=1827 med=-38.8% | KEEP-only n=583 med=+51.4% | KILL=21 KEEP=21
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T194151Z

- UTC timestamp: `20260910T194151Z`
- GitHub run: [#9660](https://github.com/28twagg-ops/TradingBot/actions/runs/34521759664)
- Run id: `34521759664`
- Live bot: exit=`0`, duration=`216s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`26s`
- Full logs: `logs/action_runs/20260910T194151Z_live_bot.log`, `logs/action_runs/20260910T194151Z_live_options.log`, `logs/action_runs/20260910T194151Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1175 | 48.5 | -22.9 | +40.6 | $+15,153 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 583 | 63.3 | +51.4 | +67.3 | $+10,446 |
| KEEP-only recent | 386 | 61.1 | +53.4 | +80.3 | $+5,801 |

- KEEP strategies (21): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406
- KILL strategies (21): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S356, S360, S365, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T15:45:30.709544-04:00","date":"2026-09-10","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":15.2,"phases_s":{"reconcile":0.27,"cancel":0.08,"manage":13.17,"protective_stops":1.11},"signals":0,"placed":0,"equity":999474.43,"open_positions":29,"pending_orders":0,"open_lots":95,"submitted_today":117,"filled_today":213,"unattributed_contracts":0,"top_signals":[],"github_run":"9660","github_run_id":"34521759664","status":"ok","data_quality":{"clean":{"n":1175,"win":48.51,"med":-22.95,"avg":40.6,"pnl":15153.09},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":583,"win":63.29,"med":51.39,"avg":67.28,"pnl":10446.45},"keep_only_recent":{"n":386,"win":61.14,"med":53.45,"avg":80.3,"pnl":5801.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S356","S360","S365","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
19:41:53  INFO      Mode: evening_prep
19:41:53  INFO        Universe cache hit: 903 tickers (tickers_2026-09-10.json)
19:41:54  INFO        [prep_universe] 40/903 (40 valid)
19:41:56  INFO        [prep_universe] 80/903 (80 valid)
19:41:57  INFO        [prep_universe] 120/903 (120 valid)
19:41:58  INFO        [prep_universe] 160/903 (160 valid)
19:42:00  INFO        [prep_universe] 200/903 (199 valid)
19:42:07  INFO        [prep_universe] 240/903 (238 valid)
19:42:20  INFO        [prep_universe] 280/903 (278 valid)
19:42:30  INFO        [prep_universe] 320/903 (318 valid)
19:42:43  INFO        [prep_universe] 360/903 (358 valid)
19:42:56  INFO        [prep_universe] 400/903 (397 valid)
19:43:06  INFO        [prep_universe] 440/903 (437 valid)
19:43:19  INFO        [prep_universe] 480/903 (477 valid)
19:43:32  INFO        [prep_universe] 520/903 (517 valid)
19:43:42  INFO        [prep_universe] 560/903 (557 valid)
19:43:55  INFO        [prep_universe] 600/903 (597 valid)
19:44:08  INFO        [prep_universe] 640/903 (637 valid)
19:44:18  INFO        [prep_universe] 680/903 (677 valid)
19:44:32  INFO        [prep_universe] 720/903 (717 valid)
19:44:45  INFO        [prep_universe] 760/903 (757 valid)
19:44:55  INFO        [prep_universe] 800/903 (797 valid)
19:45:08  INFO        [prep_universe] 840/903 (837 valid)
19:45:18  INFO        [prep_universe] 880/903 (877 valid)
19:45:25  INFO        [prep_universe] 903/903 (900 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      EVENING_PREP|
|  Time                                                         19:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.16|
+========================================================================+

+========================================================================+
|                              EVENING PREP                              |
+========================================================================+
|  Goal                   Precompute exits/signals for next execution run|
|  Plan file                                 logs/plans/evening_plan.json|
|  Regime                                                            BULL|
+========================================================================+

+========================================================================+
|                       OPEN POSITION P&L SNAPSHOT                       |
+========================================================================+
|  Open positions                                                       0|
|  Invested                                                         $0.00|
|  Open P&L                                                        $+0.00|
|                                                                        |
|  No open positions.                                                    |
|                                                                        |
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
|  Exit candidates                                                      0|
|  Signal candidates                                                   35|
|  Universe scanned                                                   903|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-10T15:45:27.839642-04:00 share=25% ===
2026-09-10 15:45:27,839 INFO === options_live_micro LIVE 2026-09-10T15:45:27.839642-04:00 share=25% ===
Live account equity $227.16 cash $227.16 #225458845 options_level=3
2026-09-10 15:45:27,936 INFO Live account equity $227.16 cash $227.16 #225458845 options_level=3
Live micro: manage/exits only
2026-09-10 15:45:27,999 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-10 15:45:28,021 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (181 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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
| 2026-09-03 |   10 |    4 |    4 |   16 |    4 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |
| 2026-09-04 |   12 |   14 |    8 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-08 |    4 |    8 |    8 |    0 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |
| 2026-09-10 |   10 |   10 |    6 |    0 |   10 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-10
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    15 | WARN | <<<
| Orphaned lots (post-stable) |  1200 | WARN | <<<
| Missing exit records (post) |  1185 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    95 | INFO |
| Total closed lots           |  2164 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1175 med=-22.9% | TAINTED n=1827 med=-38.8% | KEEP-only n=583 med=+51.4% | KILL=21 KEEP=21
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260910T194724Z

- UTC timestamp: `20260910T194724Z`
- GitHub run: [#9661](https://github.com/28twagg-ops/TradingBot/actions/runs/34522235663)
- Run id: `34522235663`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260910T194724Z_live_bot.log`, `logs/action_runs/20260910T194724Z_live_options.log`, `logs/action_runs/20260910T194724Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1175 | 48.5 | -22.9 | +40.6 | $+15,153 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 583 | 63.3 | +51.4 | +67.3 | $+10,446 |
| KEEP-only recent | 386 | 61.1 | +53.4 | +80.3 | $+5,801 |

- KEEP strategies (21): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406
- KILL strategies (21): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S356, S360, S365, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T15:40:05.891688-04:00","date":"2026-09-10","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":16.8,"phases_s":{"reconcile":0.49,"cancel":0.19,"manage":12.69,"protective_stops":2.73},"signals":0,"placed":0,"equity":999425.43,"open_positions":29,"pending_orders":0,"open_lots":95,"submitted_today":117,"filled_today":213,"unattributed_contracts":0,"top_signals":[],"github_run":"9659","github_run_id":"34521261467","status":"ok","data_quality":{"clean":{"n":1175,"win":48.51,"med":-22.95,"avg":40.6,"pnl":15153.09},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":583,"win":63.29,"med":51.39,"avg":67.28,"pnl":10446.45},"keep_only_recent":{"n":386,"win":61.14,"med":53.45,"avg":80.3,"pnl":5801.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S356","S360","S365","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
19:47:26  INFO      Mode: scan
19:47:27  INFO        Universe cache hit: 903 tickers (tickers_2026-09-10.json)
19:47:29  INFO        [universe] 40/903 (40 valid)
19:47:30  INFO        [universe] 80/903 (80 valid)
19:47:31  INFO        [universe] 120/903 (120 valid)
19:47:33  INFO        [universe] 160/903 (160 valid)
19:47:34  INFO        [universe] 200/903 (199 valid)
19:47:42  INFO        [universe] 240/903 (238 valid)
19:47:52  INFO        [universe] 280/903 (278 valid)
19:48:05  INFO        [universe] 320/903 (318 valid)
19:48:18  INFO        [universe] 360/903 (358 valid)
19:48:29  INFO        [universe] 400/903 (397 valid)
19:48:42  INFO        [universe] 440/903 (437 valid)
19:48:52  INFO        [universe] 480/903 (477 valid)
19:49:05  INFO        [universe] 520/903 (517 valid)
19:49:16  INFO        [universe] 560/903 (557 valid)
19:49:29  INFO        [universe] 600/903 (597 valid)
19:49:42  INFO        [universe] 640/903 (637 valid)
19:49:52  INFO        [universe] 680/903 (677 valid)
19:50:06  INFO        [universe] 720/903 (717 valid)
19:50:16  INFO        [universe] 760/903 (757 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20260910T195134Z

- UTC timestamp: `20260910T195134Z`
- GitHub run: [#9662](https://github.com/28twagg-ops/TradingBot/actions/runs/34522727414)
- Run id: `34522727414`
- Live bot: exit=`0`, duration=`246s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260910T195134Z_live_bot.log`, `logs/action_runs/20260910T195134Z_live_options.log`, `logs/action_runs/20260910T195134Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1175 | 48.5 | -22.9 | +40.6 | $+15,153 |
| TAINTED | 1827 | 33.3 | -38.8 | +12.0 | $-9,106 |
| KEEP-only | 583 | 63.3 | +51.4 | +67.3 | $+10,446 |
| KEEP-only recent | 386 | 61.1 | +53.4 | +80.3 | $+5,801 |

- KEEP strategies (21): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S357, S361, S362, S363, S364, S397, S399, S401, S403, S404, S406
- KILL strategies (21): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S356, S360, S365, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-10T15:55:43.344703-04:00","date":"2026-09-10","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":6.9,"phases_s":{"reconcile":0.12,"cancel":0.04,"manage":5.66,"protective_stops":0.53},"signals":0,"placed":0,"equity":999261.91,"open_positions":28,"pending_orders":0,"open_lots":94,"submitted_today":117,"filled_today":213,"unattributed_contracts":0,"top_signals":[],"github_run":"9662","github_run_id":"34522727414","status":"ok","data_quality":{"clean":{"n":1175,"win":48.51,"med":-22.95,"avg":40.6,"pnl":15153.09},"tainted":{"n":1827,"win":33.33,"med":-38.81,"avg":11.98,"pnl":-9105.84},"keep_only":{"n":583,"win":63.29,"med":51.39,"avg":67.28,"pnl":10446.45},"keep_only_recent":{"n":386,"win":61.14,"med":53.45,"avg":80.3,"pnl":5801.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S357","S361","S362","S363","S364","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S356","S360","S365","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
... (142 earlier lines - see full log file)
|    ENTER [eq] ABBV  Pullback50                                   $34.07|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    ENTER [eq] AES  Pullback50                                    $34.07|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|19:55:39  INFO        place_all_stops: checking 3 positions...
19:55:39  INFO        STOP skipped ABBV: fractional (0.1339 shares) — software exit will handle it
19:55:39  INFO        STOP-MARKET placed AES  qty=2 (pos=2.2986)  stop=$14.74  id=863df9ff-d447-428c-bfea-adade35ec407
19:55:39  INFO        STOP skipped RL: fractional (0.1016 shares) — software exit will handle it
19:55:39  INFO        place_eod_stops: updating 3 stops to current price...
19:55:39  INFO        EOD stop skip ABBV: 0.1339 shares (fractional) — ext_exits will cover
19:55:39  INFO        EOD stop: cancelled old stop AES
19:55:39  WARNING     EOD stop failed AES: {"available":"0.298604877","code":40310000,"existing_qty":"2.298604877","held_for_orders":"2","message":"insufficient qty available for order (requested: 2, available: 0.298604877)","symbol":"AES"}
19:55:39  INFO        EOD stop skip RL: 0.1016 shares (fractional) — ext_exits will cover
19:55:39  INFO        Daily log -> logs/daily/2026-09-10.md
19:55:39  INFO        Dashboard written → logs/dashboard.md

|    SKIP [eq] A  Pullback50                                        cap 3|
|    SKIP [eq] ADP  Pullback50                                      cap 3|
|    SKIP [eq] CNC  Pullback50                                      cap 3|
|    SKIP [eq] FAST  Pullback50                                     cap 3|
|    SKIP [eq] FTNT  Pullback50                                     cap 3|
|    SKIP [eq] HAS  Pullback50                                      cap 3|
|    SKIP [eq] PM  Pullback50                                       cap 3|
|    SKIP [eq] PRU  Pullback50                                      cap 3|
|    SKIP [eq] V  Pullback50                                        cap 3|
|    SKIP [eq] ALV  Pullback50                                      cap 3|
|    SKIP [eq] BWA  Pullback50                                      cap 3|
|    SKIP [eq] CFR  Pullback50                                      cap 3|
|    SKIP [eq] KEX  Pullback50                                      cap 3|
|    SKIP [eq] SBRA  Pullback50                                     cap 3|
|    SKIP [eq] SANM  Pullback50                                     cap 3|
|    SKIP [eq] SHC  Pullback50                                      cap 3|
|    SKIP [eq] SITM  Pullback50                                     cap 3|
|    SKIP [eq] SSB  Pullback50                                      cap 3|
|    SKIP [eq] UBSI  Pullback50                                     cap 3|
|    SKIP [eq] ISRG  RSIRecovery                                    cap 3|
|    SKIP [eq] KVUE  RSIRecovery                                    cap 3|
|    SKIP [eq] PKG  RSIRecovery                                     cap 3|
|    SKIP [eq] AVAV  RSIRecovery                                    cap 3|
|    SKIP [eq] BAH  RSIRecovery                                     cap 3|
|    SKIP [eq] CHWY  RSIRecovery                                    cap 3|
|    SKIP [eq] LH  RubberBand                                       cap 3|
|    SKIP [eq] AAPL  TrendResumption                                cap 3|
|    SKIP [eq] ELV  TrendResumption                                 cap 3|
|    SKIP [eq] AAPL  VWAP_Reclaim                                   cap 3|
|    SKIP [eq] ELV  VWAP_Reclaim                                    cap 3|
|    SKIP [eq] HLI  VWAP_Reclaim                                    cap 3|
|    SKIP [eq] SITM  VWAP_Reclaim                                   cap 3|

+========================================================================+
|                         BUY FILL CONFIRMATION                          |
+========================================================================+
|  Pending submits                                                      3|
+------------------------------------------------------------------------+
|  RL                                                   still unconfirmed|
|  ABBV                                                 still unconfirmed|
|  AES                                                  still unconfirmed|
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
|  Scanned                                                            900|
|  Signals                                                             35|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  3 unconfirmed|
|  Exits                                                                0|
|  Open pos                                                             3|
|  Equity                                                         $227.14|
|  Cash                                                           $124.98|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-10T15:55:40.654383-04:00 share=25% ===
2026-09-10 15:55:40,654 INFO === options_live_micro LIVE 2026-09-10T15:55:40.654383-04:00 share=25% ===
Live account equity $227.15 cash $124.98 #225458845 options_level=3
2026-09-10 15:55:40,698 INFO Live account equity $227.15 cash $124.98 #225458845 options_level=3
Live micro: manage/exits only
2026-09-10 15:55:40,721 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-10 15:55:40,737 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (48 earlier lines - see full log file)
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|[OPTIONS BOT DAILY VITALS (MATRIX EXPERIMENT)]                          |
+========================================================================+
|-- ACCOUNT STATUS (manage-only) --                                      |
|Equity       : $999,261.91                                              |
|Open Risk    : 94 lots (28 broker pos)                                  |
|Today's Run  : 0 signals -> 0 orders submitted                          |
|                                                                        |
|-- SYSTEM HEALTH --                                                     |
|Zombies      : 0 (Ledger is clean)                                      |
|Lab Status   : 94 Active Lots | 0 Pending Orders                        |
|Auto-Matrix  : (Pending EOD report generation)                          |
+========================================================================+
+========================================================================+
|[DATA QUALITY: CLEAN vs ERRORS vs KEEP-ONLY]                            |
+========================================================================+
|  CLEAN              n=1175  win= 48.5%  med= -22.9%  $+15,153          |
|  TAINTED            n=1827  win= 33.3%  med= -38.8%  $-9,106           |
|  KEEP-only          n=583   win= 63.3%  med= +51.4%  $+10,446          |
|  KEEP recent        n=386   win= 61.1%  med= +53.4%  $+5,801           |
|  KEEP(21): S163,S168,S173,S174,S210,S218,S350,S353...                  |
|  KILL(21): ORPHAN,S164,S202,S203,S207,S211,S212,S216...                |
+========================================================================+
+========================================================================+
|[+++ OVERPERFORMING STRATEGIES (n>=10)]                                 |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b832 lab0832_s406_w3_1045..  85%  +126.9%    13                       |
|  b238 lab0238_s401_w3_1045..  81%  +115.2%    16                       |
|  b861 lab0861_s408_w3_1045..  73%  +100.0%    11                       |
|  b365 lab0365_s361_w2_1005..  91%  +82.8%    11                        |
+========================================================================+
|[--- UNDERPERFORMING STRATEGIES (n>=10)]                                |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b47  lab0047_s205_w4_1120..   4%  -78.0%    28                        |
|  b167 lab0167_s216_w2_1005..  20%  -71.8%    10                        |
|  b307 lab0307_s354_w2_1005..  30%  -69.9%    10                        |
|  b1   lab0001_s200_w1_0928..   0%  -65.8%    10                        |
+========================================================================+
+========================================================================+
|[PENDING EXITS (4)]                                                     |
+========================================================================+
|  b1151 S164 ZS260911C00180000 x1 stop_loss (-75.9%)                    |
|  b861 S408 TSLA260914C00405000 x1 stop_loss (-50.0%)                   |
|  b900 S411 TSLA260914C00390000 x1 stop_loss (-51.5%)                   |
|  b407 S364 SMCI260918C00042000 x1 stop_loss (-50.0%)                   |
+========================================================================+
+========================================================================+
|[OPEN OPTIONS (28)]                                                     |
+========================================================================+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|  ---------------------------------------------------------             |
|  MARA260918C00012000          44    -11.6%   $   -232.00               |
|  ZS260911C00180000             4    -94.0%   $   -124.62               |
|  SHOP260911C00146000           2   -100.0%   $   -112.00               |
|  SMCI260918C00042000           3    -50.0%   $    -93.00               |
|  AMD260914C00550000            2    -53.3%   $    -64.00               |
|  COIN260911C00182500           4    -23.9%   $    -64.00               |
|  QQQ260914C00725000            2    -44.4%   $    -56.00               |
|  TSLA260914C00387500           2    -41.9%   $    -52.00               |
|  ... 20 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-09-10.log
elapsed=6.9s reconcile=0.12s cancel=0.04s manage=5.66s
STATUS: options_morning_bot run complete (PAPER) elapsed=6.9s. run=#9662 https://github.com/28twagg-ops/TradingBot/actions/runs/34522727414
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_buckets.csv
Summary: 49 buckets closed trades, $-1,020.50 realized
STALE WARNING: 16 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-10_strategy_selection.csv
Summary: keep=0 watch=79 drop=26
Orphan rate: 12.4% (371/3002) ALERT
```

---
