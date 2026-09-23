# Daily Comprehensive Action Review - 2026-09-23

_Auto-generated from GitHub Actions run output. Each run appends a summary; full stdout is in linked per-run log files._
## Run 20260923T130123Z

- UTC timestamp: `20260923T130123Z`
- GitHub run: [#10767](https://github.com/28twagg-ops/TradingBot/actions/runs/35864082524)
- Run id: `35864082524`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`15s`
- Full logs: `logs/action_runs/20260923T130123Z_live_bot.log`, `logs/action_runs/20260923T130123Z_live_options.log`, `logs/action_runs/20260923T130123Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1389 | 49.0 | -17.2 | +43.2 | $+17,263 |
| TAINTED | 1883 | 33.4 | -38.8 | +12.7 | $-9,542 |
| KEEP-only | 718 | 62.4 | +51.7 | +70.5 | $+11,822 |
| KEEP-only recent | 525 | 60.6 | +54.5 | +82.3 | $+7,577 |

- KEEP strategies (24): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S403, S404, S406, S412
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-23T09:01:31.047864-04:00","date":"2026-09-23","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.5,"phases_s":{"reconcile":0.59},"signals":0,"placed":0,"equity":996160.06,"open_positions":11,"pending_orders":0,"open_lots":18,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10767","github_run_id":"35864082524","status":"ok","data_quality":{"clean":{"n":1389,"win":48.96,"med":-17.19,"avg":43.24,"pnl":17263.16},"tainted":{"n":1883,"win":33.35,"med":-38.81,"avg":12.69,"pnl":-9542.28},"keep_only":{"n":718,"win":62.4,"med":51.67,"avg":70.47,"pnl":11822.45},"keep_only_recent":{"n":525,"win":60.57,"med":54.55,"avg":82.29,"pnl":7577.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:01:25  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.19|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $225.19|
|  Cash                                                           $191.68|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $33.51|
|  Open P&L                                                        $-0.35|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (1 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CCL      MomReversal     $33.51     $22.34   $22.11   -1.0%   $-0.35  |
|                                                                        |
|  Total invested                                                  $33.51|
|  Total open P&L                                                  $-0.35|
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
|  2026-09-22  SELL  NCLH  MomReversal  $5.11  P&L $-0.03                |
|  2026-09-22  SELL  AME  Pullback50  $33.91  P&L $+0.06                 |
|  2026-09-22  SELL  AMZN  Pullback50  $33.86  P&L $-0.01                |
|  2026-09-22  SELL  AES  Pullback50  $33.85  P&L $-0.01                 |
|  2026-09-22  SELL  SCHW  Pullback50  $33.20  P&L $-0.70                |
|  2026-09-21  SELL  ESAB  MomReversal  $33.77  P&L $-0.25               |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-23T09:01:26.953113-04:00 share=25% ===
2026-09-23 09:01:26,953 INFO === options_live_micro LIVE 2026-09-23T09:01:26.953113-04:00 share=25% ===
Live account equity $225.19 cash $191.68 #225458845 options_level=3
2026-09-23 09:01:27,180 INFO Live account equity $225.19 cash $191.68 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-23 09:01:27,249 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-23 09:01:27,318 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (167 earlier lines - see full log file)

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 271 | 17 |
| S164 | 307 | 22 |
| S165 | 1735 | 33 |
| S166 | 139 | 10 |
| S167 | 293 | 20 |
| S168 | 214 | 16 |
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
| 2026-09-15 |    4 |   14 |   14 |    0 |   14 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    54 |
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |
| 2026-09-18 |    4 |    8 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-23
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1517 | WARN | <<<
| Missing exit records (post) |  1514 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    18 | INFO |
| Total closed lots           |  2405 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-23_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-23_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1389 med=-17.2% | TAINTED n=1883 med=-38.8% | KEEP-only n=718 med=+51.7% | KILL=19 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=225.19 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260923T130612Z

- UTC timestamp: `20260923T130612Z`
- GitHub run: [#10768](https://github.com/28twagg-ops/TradingBot/actions/runs/35864639665)
- Run id: `35864639665`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`13s`
- Full logs: `logs/action_runs/20260923T130612Z_live_bot.log`, `logs/action_runs/20260923T130612Z_live_options.log`, `logs/action_runs/20260923T130612Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1389 | 49.0 | -17.2 | +43.2 | $+17,263 |
| TAINTED | 1883 | 33.4 | -38.8 | +12.7 | $-9,542 |
| KEEP-only | 718 | 62.4 | +51.7 | +70.5 | $+11,822 |
| KEEP-only recent | 525 | 60.6 | +54.5 | +82.3 | $+7,577 |

- KEEP strategies (24): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S403, S404, S406, S412
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-23T09:06:17.367846-04:00","date":"2026-09-23","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.8,"phases_s":{"reconcile":0.09},"signals":0,"placed":0,"equity":996180.06,"open_positions":11,"pending_orders":0,"open_lots":18,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10768","github_run_id":"35864639665","status":"ok","data_quality":{"clean":{"n":1389,"win":48.96,"med":-17.19,"avg":43.24,"pnl":17263.16},"tainted":{"n":1883,"win":33.35,"med":-38.81,"avg":12.69,"pnl":-9542.28},"keep_only":{"n":718,"win":62.4,"med":51.67,"avg":70.47,"pnl":11822.45},"keep_only_recent":{"n":525,"win":60.57,"med":54.55,"avg":82.29,"pnl":7577.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:06:13  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.26|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $225.26|
|  Cash                                                           $191.68|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $33.58|
|  Open P&L                                                        $-0.28|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (1 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CCL      MomReversal     $33.58     $22.34   $22.15   -0.8%   $-0.28  |
|                                                                        |
|  Total invested                                                  $33.58|
|  Total open P&L                                                  $-0.28|
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
|  2026-09-22  SELL  NCLH  MomReversal  $5.11  P&L $-0.03                |
|  2026-09-22  SELL  AME  Pullback50  $33.91  P&L $+0.06                 |
|  2026-09-22  SELL  AMZN  Pullback50  $33.86  P&L $-0.01                |
|  2026-09-22  SELL  AES  Pullback50  $33.85  P&L $-0.01                 |
|  2026-09-22  SELL  SCHW  Pullback50  $33.20  P&L $-0.70                |
|  2026-09-21  SELL  ESAB  MomReversal  $33.77  P&L $-0.25               |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-23T09:06:14.339250-04:00 share=25% ===
2026-09-23 09:06:14,339 INFO === options_live_micro LIVE 2026-09-23T09:06:14.339250-04:00 share=25% ===
Live account equity $225.26 cash $191.68 #225458845 options_level=3
2026-09-23 09:06:14,383 INFO Live account equity $225.26 cash $191.68 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-23 09:06:14,392 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-23 09:06:14,400 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (167 earlier lines - see full log file)

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 271 | 17 |
| S164 | 307 | 22 |
| S165 | 1735 | 33 |
| S166 | 139 | 10 |
| S167 | 293 | 20 |
| S168 | 214 | 16 |
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
| 2026-09-15 |    4 |   14 |   14 |    0 |   14 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    54 |
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |
| 2026-09-18 |    4 |    8 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-23
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1517 | WARN | <<<
| Missing exit records (post) |  1514 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    18 | INFO |
| Total closed lots           |  2405 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-23_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-23_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1389 med=-17.2% | TAINTED n=1883 med=-38.8% | KEEP-only n=718 med=+51.7% | KILL=19 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=225.26 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260923T131119Z

- UTC timestamp: `20260923T131119Z`
- GitHub run: [#10769](https://github.com/28twagg-ops/TradingBot/actions/runs/35865196168)
- Run id: `35865196168`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`14s`
- Full logs: `logs/action_runs/20260923T131119Z_live_bot.log`, `logs/action_runs/20260923T131119Z_live_options.log`, `logs/action_runs/20260923T131119Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1389 | 49.0 | -17.2 | +43.2 | $+17,263 |
| TAINTED | 1883 | 33.4 | -38.8 | +12.7 | $-9,542 |
| KEEP-only | 718 | 62.4 | +51.7 | +70.5 | $+11,822 |
| KEEP-only recent | 525 | 60.6 | +54.5 | +82.3 | $+7,577 |

- KEEP strategies (24): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S403, S404, S406, S412
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-23T09:11:25.513582-04:00","date":"2026-09-23","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.3,"phases_s":{"reconcile":0.52},"signals":0,"placed":0,"equity":996196.06,"open_positions":11,"pending_orders":0,"open_lots":18,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10769","github_run_id":"35865196168","status":"ok","data_quality":{"clean":{"n":1389,"win":48.96,"med":-17.19,"avg":43.24,"pnl":17263.16},"tainted":{"n":1883,"win":33.35,"med":-38.81,"avg":12.69,"pnl":-9542.28},"keep_only":{"n":718,"win":62.4,"med":51.67,"avg":70.47,"pnl":11822.45},"keep_only_recent":{"n":525,"win":60.57,"med":54.55,"avg":82.29,"pnl":7577.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:11:20  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.15|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $225.15|
|  Cash                                                           $191.68|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $33.47|
|  Open P&L                                                        $-0.39|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (1 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CCL      MomReversal     $33.47     $22.34   $22.08   -1.2%   $-0.39  |
|                                                                        |
|  Total invested                                                  $33.47|
|  Total open P&L                                                  $-0.39|
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
|  2026-09-22  SELL  NCLH  MomReversal  $5.11  P&L $-0.03                |
|  2026-09-22  SELL  AME  Pullback50  $33.91  P&L $+0.06                 |
|  2026-09-22  SELL  AMZN  Pullback50  $33.86  P&L $-0.01                |
|  2026-09-22  SELL  AES  Pullback50  $33.85  P&L $-0.01                 |
|  2026-09-22  SELL  SCHW  Pullback50  $33.20  P&L $-0.70                |
|  2026-09-21  SELL  ESAB  MomReversal  $33.77  P&L $-0.25               |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-23T09:11:21.925680-04:00 share=25% ===
2026-09-23 09:11:21,925 INFO === options_live_micro LIVE 2026-09-23T09:11:21.925680-04:00 share=25% ===
Live account equity $225.15 cash $191.68 #225458845 options_level=3
2026-09-23 09:11:22,153 INFO Live account equity $225.15 cash $191.68 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-23 09:11:22,232 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-23 09:11:22,302 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (167 earlier lines - see full log file)

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 271 | 17 |
| S164 | 307 | 22 |
| S165 | 1735 | 33 |
| S166 | 139 | 10 |
| S167 | 293 | 20 |
| S168 | 214 | 16 |
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
| 2026-09-15 |    4 |   14 |   14 |    0 |   14 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    54 |
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |
| 2026-09-18 |    4 |    8 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-23
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1517 | WARN | <<<
| Missing exit records (post) |  1514 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    18 | INFO |
| Total closed lots           |  2405 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-23_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-23_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1389 med=-17.2% | TAINTED n=1883 med=-38.8% | KEEP-only n=718 med=+51.7% | KILL=19 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=225.15 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260923T131616Z

- UTC timestamp: `20260923T131616Z`
- GitHub run: [#10770](https://github.com/28twagg-ops/TradingBot/actions/runs/35865766608)
- Run id: `35865766608`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`13s`
- Full logs: `logs/action_runs/20260923T131616Z_live_bot.log`, `logs/action_runs/20260923T131616Z_live_options.log`, `logs/action_runs/20260923T131616Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1389 | 49.0 | -17.2 | +43.2 | $+17,263 |
| TAINTED | 1883 | 33.4 | -38.8 | +12.7 | $-9,542 |
| KEEP-only | 718 | 62.4 | +51.7 | +70.5 | $+11,822 |
| KEEP-only recent | 525 | 60.6 | +54.5 | +82.3 | $+7,577 |

- KEEP strategies (24): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S403, S404, S406, S412
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-23T09:16:22.164140-04:00","date":"2026-09-23","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.19},"signals":0,"placed":0,"equity":996140.06,"open_positions":11,"pending_orders":0,"open_lots":18,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10770","github_run_id":"35865766608","status":"ok","data_quality":{"clean":{"n":1389,"win":48.96,"med":-17.19,"avg":43.24,"pnl":17263.16},"tainted":{"n":1883,"win":33.35,"med":-38.81,"avg":12.69,"pnl":-9542.28},"keep_only":{"n":718,"win":62.4,"med":51.67,"avg":70.47,"pnl":11822.45},"keep_only_recent":{"n":525,"win":60.57,"med":54.55,"avg":82.29,"pnl":7577.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:16:18  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.13|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $225.13|
|  Cash                                                           $191.68|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $33.45|
|  Open P&L                                                        $-0.41|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (1 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CCL      MomReversal     $33.45     $22.34   $22.07   -1.2%   $-0.41  |
|                                                                        |
|  Total invested                                                  $33.45|
|  Total open P&L                                                  $-0.41|
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
|  2026-09-22  SELL  NCLH  MomReversal  $5.11  P&L $-0.03                |
|  2026-09-22  SELL  AME  Pullback50  $33.91  P&L $+0.06                 |
|  2026-09-22  SELL  AMZN  Pullback50  $33.86  P&L $-0.01                |
|  2026-09-22  SELL  AES  Pullback50  $33.85  P&L $-0.01                 |
|  2026-09-22  SELL  SCHW  Pullback50  $33.20  P&L $-0.70                |
|  2026-09-21  SELL  ESAB  MomReversal  $33.77  P&L $-0.25               |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-23T09:16:19.372752-04:00 share=25% ===
2026-09-23 09:16:19,372 INFO === options_live_micro LIVE 2026-09-23T09:16:19.372752-04:00 share=25% ===
Live account equity $225.13 cash $191.68 #225458845 options_level=3
2026-09-23 09:16:19,456 INFO Live account equity $225.13 cash $191.68 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-23 09:16:19,477 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-23 09:16:19,498 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (167 earlier lines - see full log file)

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 271 | 17 |
| S164 | 307 | 22 |
| S165 | 1735 | 33 |
| S166 | 139 | 10 |
| S167 | 293 | 20 |
| S168 | 214 | 16 |
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
| 2026-09-15 |    4 |   14 |   14 |    0 |   14 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    54 |
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |
| 2026-09-18 |    4 |    8 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-23
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1517 | WARN | <<<
| Missing exit records (post) |  1514 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    18 | INFO |
| Total closed lots           |  2405 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-23_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-23_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1389 med=-17.2% | TAINTED n=1883 med=-38.8% | KEEP-only n=718 med=+51.7% | KILL=19 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=225.13 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260923T132125Z

- UTC timestamp: `20260923T132125Z`
- GitHub run: [#10771](https://github.com/28twagg-ops/TradingBot/actions/runs/35866328179)
- Run id: `35866328179`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`10s`
- Full logs: `logs/action_runs/20260923T132125Z_live_bot.log`, `logs/action_runs/20260923T132125Z_live_options.log`, `logs/action_runs/20260923T132125Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1389 | 49.0 | -17.2 | +43.2 | $+17,263 |
| TAINTED | 1883 | 33.4 | -38.8 | +12.7 | $-9,542 |
| KEEP-only | 718 | 62.4 | +51.7 | +70.5 | $+11,822 |
| KEEP-only recent | 525 | 60.6 | +54.5 | +82.3 | $+7,577 |

- KEEP strategies (24): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S403, S404, S406, S412
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-23T09:21:30.795734-04:00","date":"2026-09-23","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.35},"signals":0,"placed":0,"equity":996130.06,"open_positions":11,"pending_orders":0,"open_lots":18,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10771","github_run_id":"35866328179","status":"ok","data_quality":{"clean":{"n":1389,"win":48.96,"med":-17.19,"avg":43.24,"pnl":17263.16},"tainted":{"n":1883,"win":33.35,"med":-38.81,"avg":12.69,"pnl":-9542.28},"keep_only":{"n":718,"win":62.4,"med":51.67,"avg":70.47,"pnl":11822.45},"keep_only_recent":{"n":525,"win":60.57,"med":54.55,"avg":82.29,"pnl":7577.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:21:26  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.13|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $225.13|
|  Cash                                                           $191.68|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $33.45|
|  Open P&L                                                        $-0.41|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (1 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CCL      MomReversal     $33.45     $22.34   $22.07   -1.2%   $-0.41  |
|                                                                        |
|  Total invested                                                  $33.45|
|  Total open P&L                                                  $-0.41|
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
|  2026-09-22  SELL  NCLH  MomReversal  $5.11  P&L $-0.03                |
|  2026-09-22  SELL  AME  Pullback50  $33.91  P&L $+0.06                 |
|  2026-09-22  SELL  AMZN  Pullback50  $33.86  P&L $-0.01                |
|  2026-09-22  SELL  AES  Pullback50  $33.85  P&L $-0.01                 |
|  2026-09-22  SELL  SCHW  Pullback50  $33.20  P&L $-0.70                |
|  2026-09-21  SELL  ESAB  MomReversal  $33.77  P&L $-0.25               |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-23T09:21:27.474825-04:00 share=25% ===
2026-09-23 09:21:27,474 INFO === options_live_micro LIVE 2026-09-23T09:21:27.474825-04:00 share=25% ===
Live account equity $225.13 cash $191.68 #225458845 options_level=3
2026-09-23 09:21:27,640 INFO Live account equity $225.13 cash $191.68 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-23 09:21:27,788 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-23 09:21:27,835 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (167 earlier lines - see full log file)

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 271 | 17 |
| S164 | 307 | 22 |
| S165 | 1735 | 33 |
| S166 | 139 | 10 |
| S167 | 293 | 20 |
| S168 | 214 | 16 |
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
| 2026-09-15 |    4 |   14 |   14 |    0 |   14 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    54 |
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |
| 2026-09-18 |    4 |    8 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-23
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1517 | WARN | <<<
| Missing exit records (post) |  1514 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    18 | INFO |
| Total closed lots           |  2405 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-23_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-23_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1389 med=-17.2% | TAINTED n=1883 med=-38.8% | KEEP-only n=718 med=+51.7% | KILL=19 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=225.13 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260923T132611Z

- UTC timestamp: `20260923T132611Z`
- GitHub run: [#10772](https://github.com/28twagg-ops/TradingBot/actions/runs/35866909229)
- Run id: `35866909229`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`12s`
- Full logs: `logs/action_runs/20260923T132611Z_live_bot.log`, `logs/action_runs/20260923T132611Z_live_options.log`, `logs/action_runs/20260923T132611Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1389 | 49.0 | -17.2 | +43.2 | $+17,263 |
| TAINTED | 1883 | 33.4 | -38.8 | +12.7 | $-9,542 |
| KEEP-only | 718 | 62.4 | +51.7 | +70.5 | $+11,822 |
| KEEP-only recent | 525 | 60.6 | +54.5 | +82.3 | $+7,577 |

- KEEP strategies (24): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S403, S404, S406, S412
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-23T09:26:17.100412-04:00","date":"2026-09-23","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.2,"phases_s":{"reconcile":0.44},"signals":0,"placed":0,"equity":996090.06,"open_positions":11,"pending_orders":0,"open_lots":18,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10772","github_run_id":"35866909229","status":"ok","data_quality":{"clean":{"n":1389,"win":48.96,"med":-17.19,"avg":43.24,"pnl":17263.16},"tainted":{"n":1883,"win":33.35,"med":-38.81,"avg":12.69,"pnl":-9542.28},"keep_only":{"n":718,"win":62.4,"med":51.67,"avg":70.47,"pnl":11822.45},"keep_only_recent":{"n":525,"win":60.57,"med":54.55,"avg":82.29,"pnl":7577.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:26:12  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.11|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $225.11|
|  Cash                                                           $191.68|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $33.43|
|  Open P&L                                                        $-0.43|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (1 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CCL      MomReversal     $33.43     $22.34   $22.05   -1.3%   $-0.43  |
|                                                                        |
|  Total invested                                                  $33.43|
|  Total open P&L                                                  $-0.43|
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
|  2026-09-22  SELL  NCLH  MomReversal  $5.11  P&L $-0.03                |
|  2026-09-22  SELL  AME  Pullback50  $33.91  P&L $+0.06                 |
|  2026-09-22  SELL  AMZN  Pullback50  $33.86  P&L $-0.01                |
|  2026-09-22  SELL  AES  Pullback50  $33.85  P&L $-0.01                 |
|  2026-09-22  SELL  SCHW  Pullback50  $33.20  P&L $-0.70                |
|  2026-09-21  SELL  ESAB  MomReversal  $33.77  P&L $-0.25               |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-23T09:26:13.876470-04:00 share=25% ===
2026-09-23 09:26:13,876 INFO === options_live_micro LIVE 2026-09-23T09:26:13.876470-04:00 share=25% ===
Live account equity $225.11 cash $191.68 #225458845 options_level=3
2026-09-23 09:26:14,087 INFO Live account equity $225.11 cash $191.68 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-23 09:26:14,147 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-23 09:26:14,206 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (167 earlier lines - see full log file)

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 271 | 17 |
| S164 | 307 | 22 |
| S165 | 1735 | 33 |
| S166 | 139 | 10 |
| S167 | 293 | 20 |
| S168 | 214 | 16 |
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
| 2026-09-15 |    4 |   14 |   14 |    0 |   14 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    54 |
| 2026-09-16 |    4 |    4 |    4 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |
| 2026-09-18 |    4 |    8 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-23
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1517 | WARN | <<<
| Missing exit records (post) |  1514 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    18 | INFO |
| Total closed lots           |  2405 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-23_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-23_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1389 med=-17.2% | TAINTED n=1883 med=-38.8% | KEEP-only n=718 med=+51.7% | KILL=19 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=225.11 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260923T133117Z

- UTC timestamp: `20260923T133117Z`
- GitHub run: [#10773](https://github.com/28twagg-ops/TradingBot/actions/runs/35867489226)
- Run id: `35867489226`
- Live bot: exit=`0`, duration=`216s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260923T133117Z_live_bot.log`, `logs/action_runs/20260923T133117Z_live_options.log`, `logs/action_runs/20260923T133117Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1389 | 49.0 | -17.2 | +43.2 | $+17,263 |
| TAINTED | 1883 | 33.4 | -38.8 | +12.7 | $-9,542 |
| KEEP-only | 718 | 62.4 | +51.7 | +70.5 | $+11,822 |
| KEEP-only recent | 525 | 60.6 | +54.5 | +82.3 | $+7,577 |

- KEEP strategies (24): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S403, S404, S406, S412
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-23T09:26:17.100412-04:00","date":"2026-09-23","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.2,"phases_s":{"reconcile":0.44},"signals":0,"placed":0,"equity":996090.06,"open_positions":11,"pending_orders":0,"open_lots":18,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10772","github_run_id":"35866909229","status":"ok","data_quality":{"clean":{"n":1389,"win":48.96,"med":-17.19,"avg":43.24,"pnl":17263.16},"tainted":{"n":1883,"win":33.35,"med":-38.81,"avg":12.69,"pnl":-9542.28},"keep_only":{"n":718,"win":62.4,"med":51.67,"avg":70.47,"pnl":11822.45},"keep_only_recent":{"n":525,"win":60.57,"med":54.55,"avg":82.29,"pnl":7577.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:31:19  INFO      Mode: morning_prep
13:31:19  INFO        [prep_positions] 1/1 (1 valid)
13:31:19  INFO      Fetching tickers (universe=both)...
13:31:19  INFO        S&P 500: 503
13:31:20  INFO        MidCap 400: 400
13:31:20  INFO        Total: 901 tickers
13:31:21  INFO        [prep_universe] 40/900 (40 valid)
13:31:22  INFO        [prep_universe] 80/900 (80 valid)
13:31:23  INFO        [prep_universe] 120/900 (120 valid)
13:31:25  INFO        [prep_universe] 160/900 (160 valid)
13:31:26  INFO        [prep_universe] 200/900 (199 valid)
13:31:33  INFO        [prep_universe] 240/900 (238 valid)
13:31:46  INFO        [prep_universe] 280/900 (278 valid)
13:31:56  INFO        [prep_universe] 320/900 (318 valid)
13:32:09  INFO        [prep_universe] 360/900 (358 valid)
13:32:22  INFO        [prep_universe] 400/900 (398 valid)
13:32:33  INFO        [prep_universe] 440/900 (438 valid)
13:32:46  INFO        [prep_universe] 480/900 (478 valid)
13:32:59  INFO        [prep_universe] 520/900 (518 valid)
13:33:09  INFO        [prep_universe] 560/900 (558 valid)
13:33:22  INFO        [prep_universe] 600/900 (598 valid)
13:33:35  INFO        [prep_universe] 640/900 (638 valid)
13:33:45  INFO        [prep_universe] 680/900 (678 valid)
13:33:58  INFO        [prep_universe] 720/900 (718 valid)
13:34:11  INFO        [prep_universe] 760/900 (758 valid)
13:34:21  INFO        [prep_universe] 800/900 (798 valid)
13:34:34  INFO        [prep_universe] 840/900 (838 valid)
13:34:47  INFO        [prep_universe] 880/900 (878 valid)
13:34:51  INFO        [prep_universe] 900/900 (898 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.05|
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
|  Open positions                                                       1|
|  Invested                                                        $11.38|
|  Open P&L                                                        $-0.14|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CCL      MomReversal     $11.38     $22.34   $22.06   -1.2%   $-0.14  |
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
|  Signal candidates                                                   22|
|  Universe scanned                                                   900|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-23T09:34:53.776556-04:00 share=25% ===
2026-09-23 09:34:53,776 INFO === options_live_micro LIVE 2026-09-23T09:34:53.776556-04:00 share=25% ===
Live account equity $224.93 cash $213.68 #225458845 options_level=3
2026-09-23 09:34:53,866 INFO Live account equity $224.93 cash $213.68 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-23 09:34:53,932 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-23 09:34:53,976 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=18 paper_keys=yes dry_run=False
  alpaca positions=9
  FLAG b196|S218|e327b991 missing from Alpaca
  FLAG b169|S216|90cfd76c missing from Alpaca
  FLAG b0|ORPHAN|70d8f5d2 missing from Alpaca
  FLAG b241|S401|16297965 missing from Alpaca
  FLAG b240|S401|d0418d8f missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$996,307.94
  buying_power=$3,939,823.76 cash=$1,031,925.94
  open option orders: 6
    MCD260925C00272500 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=0.01
    LLY260925C01250000 OrderSide.SELL qty=3 status=OrderStatus.NEW limit=None
    RBLX260925C00053000 OrderSide.SELL qty=2 status=OrderStatus.NEW limit=None
    NFLX261002C00076000 OrderSide.SELL qty=2 status=OrderStatus.NEW limit=None
    NFLX261009C00078000 OrderSide.SELL qty=2 status=OrderStatus.NEW limit=None
  open option positions: 8
    LLY260925C01250000 qty=3 mkt=$210.00
    MARA260925C00011500 qty=-1 mkt=$-208.00
    MARA260925C00012000 qty=-1 mkt=$-156.00
    MARA260925C00012500 qty=3 mkt=$306.00
    MCD260925C00272500 qty=1 mkt=$0.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-23T09:34:57.112836-04:00 ===

[Run context]
Paper auth OK — equity $996313.94, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
  EXIT [b434|lab0434_s366_w2_1005_1045_r1|S366] take_profit (+105.4%) SELL failed MARA260925C00012500: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b433|lab0433_s366_w1_0928_1005_r2|S366] take_profit (+105.4%) SELL failed MARA260925C00012500: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b432|lab0432_s366_w1_0928_1005_r1|S366] take_profit (+105.4%) SELL failed MARA260925C00012500: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
2026-09-23 09:34:58,256 INFO   EXIT [b101|lab0101_s211_w4_1120_1135_r2|S211] stop_loss (-93.3%) SELL 1 RBLX260925C00053000 @<= 0.03
2026-09-23 09:34:59,775 INFO   EXIT [b378|lab0378_s362_w2_1005_1045_r1|S362] take_profit (+92.3%) SELL 1 LLY260925C01250000 @<= 0.72
Protective stops: placed=0 upgraded=0 already=5 failed=1 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
```

---

## Run 20260923T133650Z

- UTC timestamp: `20260923T133650Z`
- GitHub run: [#10774](https://github.com/28twagg-ops/TradingBot/actions/runs/35868076608)
- Run id: `35868076608`
- Live bot: exit=`0`, duration=`217s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260923T133650Z_live_bot.log`, `logs/action_runs/20260923T133650Z_live_options.log`, `logs/action_runs/20260923T133650Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1389 | 49.0 | -17.2 | +43.2 | $+17,263 |
| TAINTED | 1883 | 33.4 | -38.8 | +12.7 | $-9,542 |
| KEEP-only | 718 | 62.4 | +51.7 | +70.5 | $+11,822 |
| KEEP-only recent | 525 | 60.6 | +54.5 | +82.3 | $+7,577 |

- KEEP strategies (24): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S403, S404, S406, S412
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-23T09:26:17.100412-04:00","date":"2026-09-23","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.2,"phases_s":{"reconcile":0.44},"signals":0,"placed":0,"equity":996090.06,"open_positions":11,"pending_orders":0,"open_lots":18,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10772","github_run_id":"35866909229","status":"ok","data_quality":{"clean":{"n":1389,"win":48.96,"med":-17.19,"avg":43.24,"pnl":17263.16},"tainted":{"n":1883,"win":33.35,"med":-38.81,"avg":12.69,"pnl":-9542.28},"keep_only":{"n":718,"win":62.4,"med":51.67,"avg":70.47,"pnl":11822.45},"keep_only_recent":{"n":525,"win":60.57,"med":54.55,"avg":82.29,"pnl":7577.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:36:52  INFO      Mode: morning_prep
13:36:52  INFO        [prep_positions] 1/1 (1 valid)
13:36:52  INFO      Fetching tickers (universe=both)...
13:36:53  INFO        S&P 500: 503
13:36:53  INFO        MidCap 400: 400
13:36:53  INFO        Total: 901 tickers
13:36:54  INFO        [prep_universe] 40/900 (40 valid)
13:36:55  INFO        [prep_universe] 80/900 (80 valid)
13:36:57  INFO        [prep_universe] 120/900 (120 valid)
13:36:58  INFO        [prep_universe] 160/900 (160 valid)
13:36:59  INFO        [prep_universe] 200/900 (199 valid)
13:37:06  INFO        [prep_universe] 240/900 (238 valid)
13:37:19  INFO        [prep_universe] 280/900 (278 valid)
13:37:30  INFO        [prep_universe] 320/900 (318 valid)
13:37:43  INFO        [prep_universe] 360/900 (358 valid)
13:37:56  INFO        [prep_universe] 400/900 (398 valid)
13:38:06  INFO        [prep_universe] 440/900 (438 valid)
13:38:19  INFO        [prep_universe] 480/900 (478 valid)
13:38:32  INFO        [prep_universe] 520/900 (518 valid)
13:38:42  INFO        [prep_universe] 560/900 (558 valid)
13:38:55  INFO        [prep_universe] 600/900 (598 valid)
13:39:05  INFO        [prep_universe] 640/900 (638 valid)
13:39:19  INFO        [prep_universe] 680/900 (678 valid)
13:39:32  INFO        [prep_universe] 720/900 (718 valid)
13:39:42  INFO        [prep_universe] 760/900 (758 valid)
13:39:55  INFO        [prep_universe] 800/900 (798 valid)
13:40:08  INFO        [prep_universe] 840/900 (838 valid)
13:40:18  INFO        [prep_universe] 880/900 (878 valid)
13:40:25  INFO        [prep_universe] 900/900 (898 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.85|
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
|  Open positions                                                       1|
|  Invested                                                        $11.17|
|  Open P&L                                                        $-0.35|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CCL      MomReversal     $11.17     $22.34   $21.65   -3.1%   $-0.35  |
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
|  Signal candidates                                                   29|
|  Universe scanned                                                   900|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-23T09:40:28.157176-04:00 share=25% ===
2026-09-23 09:40:28,157 INFO === options_live_micro LIVE 2026-09-23T09:40:28.157176-04:00 share=25% ===
Live account equity $224.92 cash $213.68 #225458845 options_level=3
2026-09-23 09:40:28,309 INFO Live account equity $224.92 cash $213.68 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-23 09:40:28,430 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-23 09:40:28,513 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=18 paper_keys=yes dry_run=False
  alpaca positions=9
  FLAG b196|S218|e327b991 missing from Alpaca
  FLAG b169|S216|90cfd76c missing from Alpaca
  FLAG b0|ORPHAN|70d8f5d2 missing from Alpaca
  FLAG b241|S401|16297965 missing from Alpaca
  FLAG b240|S401|d0418d8f missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$996,427.92
  buying_power=$3,941,090.88 cash=$1,032,000.92
  open option orders: 5
    RBLX260925C00053000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=0.03
    MCD260925C00272500 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=0.01
    NFLX261002C00076000 OrderSide.SELL qty=2 status=OrderStatus.NEW limit=None
    NFLX261009C00078000 OrderSide.SELL qty=2 status=OrderStatus.NEW limit=None
    MARA260925C00011000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
  open option positions: 8
    LLY260925C01250000 qty=2 mkt=$80.00
    MARA260925C00011500 qty=-1 mkt=$-218.00
    MARA260925C00012000 qty=-1 mkt=$-158.00
    MARA260925C00012500 qty=3 mkt=$309.00
    MCD260925C00272500 qty=1 mkt=$0.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-23T09:40:31.822505-04:00 ===

[Run context]
Paper auth OK — equity $996427.92, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
  EXIT [b434|lab0434_s366_w2_1005_1045_r1|S366] take_profit (+107.4%) SELL failed MARA260925C00012500: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b433|lab0433_s366_w1_0928_1005_r2|S366] take_profit (+107.4%) SELL failed MARA260925C00012500: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b432|lab0432_s366_w1_0928_1005_r1|S366] take_profit (+107.4%) SELL failed MARA260925C00012500: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
Protective stops: placed=1 upgraded=0 already=4 failed=1 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
```

---

## Run 20260923T134229Z

- UTC timestamp: `20260923T134229Z`
- GitHub run: [#10775](https://github.com/28twagg-ops/TradingBot/actions/runs/35868656948)
- Run id: `35868656948`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260923T134229Z_live_bot.log`, `logs/action_runs/20260923T134229Z_live_options.log`, `logs/action_runs/20260923T134229Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1389 | 49.0 | -17.2 | +43.2 | $+17,263 |
| TAINTED | 1883 | 33.4 | -38.8 | +12.7 | $-9,542 |
| KEEP-only | 718 | 62.4 | +51.7 | +70.5 | $+11,822 |
| KEEP-only recent | 525 | 60.6 | +54.5 | +82.3 | $+7,577 |

- KEEP strategies (24): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S403, S404, S406, S412
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-23T09:26:17.100412-04:00","date":"2026-09-23","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.2,"phases_s":{"reconcile":0.44},"signals":0,"placed":0,"equity":996090.06,"open_positions":11,"pending_orders":0,"open_lots":18,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10772","github_run_id":"35866909229","status":"ok","data_quality":{"clean":{"n":1389,"win":48.96,"med":-17.19,"avg":43.24,"pnl":17263.16},"tainted":{"n":1883,"win":33.35,"med":-38.81,"avg":12.69,"pnl":-9542.28},"keep_only":{"n":718,"win":62.4,"med":51.67,"avg":70.47,"pnl":11822.45},"keep_only_recent":{"n":525,"win":60.57,"med":54.55,"avg":82.29,"pnl":7577.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:42:30  INFO      Mode: morning_prep
13:42:30  INFO        [prep_positions] 1/1 (1 valid)
13:42:30  INFO        Universe cache hit: 901 tickers (tickers_2026-09-23.json)
13:42:31  INFO        [prep_universe] 40/900 (40 valid)
13:42:33  INFO        [prep_universe] 80/900 (80 valid)
13:42:34  INFO        [prep_universe] 120/900 (120 valid)
13:42:35  INFO        [prep_universe] 160/900 (160 valid)
13:42:36  INFO        [prep_universe] 200/900 (199 valid)
13:42:44  INFO        [prep_universe] 240/900 (238 valid)
13:42:57  INFO        [prep_universe] 280/900 (278 valid)
13:43:09  INFO        [prep_universe] 320/900 (318 valid)
13:43:19  INFO        [prep_universe] 360/900 (358 valid)
13:43:32  INFO        [prep_universe] 400/900 (398 valid)
13:43:45  INFO        [prep_universe] 440/900 (438 valid)
13:43:55  INFO        [prep_universe] 480/900 (478 valid)
13:44:08  INFO        [prep_universe] 520/900 (518 valid)
13:44:21  INFO        [prep_universe] 560/900 (558 valid)
13:44:31  INFO        [prep_universe] 600/900 (598 valid)
13:44:44  INFO        [prep_universe] 640/900 (638 valid)
13:44:57  INFO        [prep_universe] 680/900 (678 valid)
13:45:10  INFO        [prep_universe] 720/900 (718 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20260923T134852Z

- UTC timestamp: `20260923T134852Z`
- GitHub run: [#10776](https://github.com/28twagg-ops/TradingBot/actions/runs/35869249260)
- Run id: `35869249260`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260923T134852Z_live_bot.log`, `logs/action_runs/20260923T134852Z_live_options.log`, `logs/action_runs/20260923T134852Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1389 | 49.0 | -17.2 | +43.2 | $+17,263 |
| TAINTED | 1883 | 33.4 | -38.8 | +12.7 | $-9,542 |
| KEEP-only | 718 | 62.4 | +51.7 | +70.5 | $+11,822 |
| KEEP-only recent | 525 | 60.6 | +54.5 | +82.3 | $+7,577 |

- KEEP strategies (24): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S403, S404, S406, S412
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-23T09:26:17.100412-04:00","date":"2026-09-23","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.2,"phases_s":{"reconcile":0.44},"signals":0,"placed":0,"equity":996090.06,"open_positions":11,"pending_orders":0,"open_lots":18,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10772","github_run_id":"35866909229","status":"ok","data_quality":{"clean":{"n":1389,"win":48.96,"med":-17.19,"avg":43.24,"pnl":17263.16},"tainted":{"n":1883,"win":33.35,"med":-38.81,"avg":12.69,"pnl":-9542.28},"keep_only":{"n":718,"win":62.4,"med":51.67,"avg":70.47,"pnl":11822.45},"keep_only_recent":{"n":525,"win":60.57,"med":54.55,"avg":82.29,"pnl":7577.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:48:53  INFO      Mode: morning_scan
13:48:53  INFO        [positions] 1/1 (1 valid)
13:48:54  INFO        SELL MARKET [urgent] CCL closed
13:48:56  INFO        TX logged: SELL CCL  P&L -3.19%
13:48:56  INFO        Universe cache hit: 901 tickers (tickers_2026-09-23.json)
13:48:57  INFO        [universe] 40/901 (40 valid)
13:48:58  INFO        [universe] 80/901 (80 valid)
13:49:00  INFO        [universe] 120/901 (120 valid)
13:49:01  INFO        [universe] 160/901 (160 valid)
13:49:02  INFO        [universe] 200/901 (199 valid)
13:49:10  INFO        [universe] 240/901 (238 valid)
13:49:23  INFO        [universe] 280/901 (278 valid)
13:49:33  INFO        [universe] 320/901 (318 valid)
13:49:46  INFO        [universe] 360/901 (358 valid)
13:49:59  INFO        [universe] 400/901 (398 valid)
13:50:09  INFO        [universe] 440/901 (438 valid)
13:50:22  INFO        [universe] 480/901 (478 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20260923T135217Z

- UTC timestamp: `20260923T135217Z`
- GitHub run: [#10777](https://github.com/28twagg-ops/TradingBot/actions/runs/35869837894)
- Run id: `35869837894`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260923T135217Z_live_bot.log`, `logs/action_runs/20260923T135217Z_live_options.log`, `logs/action_runs/20260923T135217Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1389 | 49.0 | -17.2 | +43.2 | $+17,263 |
| TAINTED | 1883 | 33.4 | -38.8 | +12.7 | $-9,542 |
| KEEP-only | 718 | 62.4 | +51.7 | +70.5 | $+11,822 |
| KEEP-only recent | 525 | 60.6 | +54.5 | +82.3 | $+7,577 |

- KEEP strategies (24): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S403, S404, S406, S412
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-23T09:26:17.100412-04:00","date":"2026-09-23","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.2,"phases_s":{"reconcile":0.44},"signals":0,"placed":0,"equity":996090.06,"open_positions":11,"pending_orders":0,"open_lots":18,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10772","github_run_id":"35866909229","status":"ok","data_quality":{"clean":{"n":1389,"win":48.96,"med":-17.19,"avg":43.24,"pnl":17263.16},"tainted":{"n":1883,"win":33.35,"med":-38.81,"avg":12.69,"pnl":-9542.28},"keep_only":{"n":718,"win":62.4,"med":51.67,"avg":70.47,"pnl":11822.45},"keep_only_recent":{"n":525,"win":60.57,"med":54.55,"avg":82.29,"pnl":7577.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
... (67 earlier lines - see full log file)
|                                                                        |
|  No open positions.                                                    |
|                                                                        |
|  Buys today: 0  |  entry cap: 3  |  max open: 3                        |
+========================================================================+

+========================================================================+
|                               PLAN CACHE                               |
+========================================================================+
|  Mode                                                           morning|
|  File                                      logs/plans/morning_plan.json|
|  Use cached plan                                   no (stale (7211.9m))|
+========================================================================+

+========================================================================+
|                             DATA DOWNLOAD                              |
+========================================================================+
|  Universe: both  |  Alpaca primary / yfinance fallback                 |
+========================================================================+

+========================================================================+
|                              SIGNAL SCAN                               |
+========================================================================+
|  Month: Sep  |  Regime: BULL                                           |
|  Primary: GapDown  |  Secondary: VolumeSpike (display only — schedule ~|
|  Source                                                       live scan|
+========================================================================+

+========================================================================+
|                         SIGNALS FOUND  --  23                          |
+========================================================================+
|  TICKER   STRATEGY        TIER   PRICE    RSI    VOL_Z   TRIGGER       |
+------------------------------------------------------------------------+
|  ADM      Pullback50      eq     $82.72   41.3   -1.78   50MA bounce (+|
|  TECH     Pullback50      eq     $72.55   61.5   -1.90   50MA bounce (+|
|  BRK-B    Pullback50      eq     $506.33  54.4   -1.72   50MA bounce (+|
|  COP      Pullback50      eq     $127.54  34.3   -1.89   50MA bounce (+|
|  EG       Pullback50      eq     $373.23  45.5   -1.17   50MA bounce (-|
|  FDS      Pullback50      eq     $279.71  36.4   -2.25   50MA bounce (-|
|  J        Pullback50      eq     $143.57  39.1   -1.78   50MA bounce (+|
|  KMI      Pullback50      eq     $31.50   44.9   -1.72   50MA bounce (-|
|  MA       Pullback50      eq     $563.43  30.3   -2.22   50MA bounce (-|
|  MET      Pullback50      eq     $96.09   48.6   -2.12   50MA bounce (+|
|  PFG      Pullback50      eq     $113.76  55.0   -1.73   50MA bounce (+|
|  SJM      Pullback50      eq     $122.00  25.2   -2.18   50MA bounce (+|
|  VLTO     Pullback50      eq     $95.56   43.0   -1.59   50MA bounce (-|
|  WAB      Pullback50      eq     $290.54  66.4   -2.38   50MA bounce (+|
|  AMG      Pullback50      eq     $362.98  54.5   -2.39   50MA bounce (+|
|  AVNT     Pullback50      eq     $40.91   25.3   -2.98   50MA bounce (-|
|  GEF      Pullback50      eq     $84.69   44.7   -2.44   50MA bounce (+|
|  MSM      Pullback50      eq     $121.94  70.2   -1.88   50MA bounce (-|
|  MORN     Pullback50      eq     $198.46  39.8   -1.93   50MA bounce (-|
|  NOV      Pullback50      eq     $20.48   30.6   -1.73   50MA bounce (+|
|  RGA      Pullback50      eq     $245.85  35.9   -2.13   50MA bounce (+|
|  SEIC     Pullback50      eq     $104.33  31.8   -1.19   50MA bounce (-|
|  TTC      Pullback50      eq     $96.75   43.4   -1.64   50MA bounce (+|
|                                                                        |
+========================================================================+

+========================================================================+
|                              ENTRY ORDERS                              |
+========================================================================+
|    ENTER [eq] ADM  Pullback50                                    $33.72|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    ENTER [eq] TECH  Pullback50                                   $33.72|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    ENTER [eq] BRK-B  Pullback50                                  $33.72|
|    ENTER [eq] COP  Pullback50                                    $33.72|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    SKIP [eq] EG  Pullback50                                       cap 3|
|    SKIP [eq] FDS  Pullback50                                      cap 3|
|    SKIP [eq] J  Pullback50                                        cap 3|
|    SKIP [eq] KMI  Pullback50                                      cap 3|
|    SKIP [eq] MA  Pullback50                                       cap 3|
|    SKIP [eq] MET  Pullback50                                      cap 3|
|    SKIP [eq] PFG  Pullback50                                      cap 3|
|    SKIP [eq] SJM  Pullback50                                      cap 3|
|    SKIP [eq] VLTO  Pullback50                                     cap 3|
|    SKIP [eq] WAB  Pullback50                                      cap 3|
|    SKIP [eq] AMG  Pullback50                                      cap 3|
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---
