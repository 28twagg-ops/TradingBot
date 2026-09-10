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
