# Daily Comprehensive Action Review - 2026-09-18

_Auto-generated from GitHub Actions run output. Each run appends a summary; full stdout is in linked per-run log files._
## Run 20260918T130121Z

- UTC timestamp: `20260918T130121Z`
- GitHub run: [#10371](https://github.com/28twagg-ops/TradingBot/actions/runs/35347671628)
- Run id: `35347671628`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`11s`
- Full logs: `logs/action_runs/20260918T130121Z_live_bot.log`, `logs/action_runs/20260918T130121Z_live_options.log`, `logs/action_runs/20260918T130121Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1311 | 47.5 | -33.3 | +35.9 | $+15,191 |
| TAINTED | 1873 | 33.4 | -39.0 | +12.9 | $-9,351 |
| KEEP-only | 611 | 62.4 | +50.0 | +61.8 | $+10,167 |
| KEEP-only recent | 428 | 61.2 | +53.3 | +74.4 | $+6,557 |

- KEEP strategies (20): S163, S168, S173, S174, S210, S218, S350, S353, S356, S357, S361, S362, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (22): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S359, S360, S363, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-18T09:01:27.480346-04:00","date":"2026-09-18","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.3,"phases_s":{"reconcile":0.47},"signals":0,"placed":0,"equity":996630.61,"open_positions":24,"pending_orders":0,"open_lots":84,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10371","github_run_id":"35347671628","status":"ok","data_quality":{"clean":{"n":1311,"win":47.52,"med":-33.33,"avg":35.94,"pnl":15191.16},"tainted":{"n":1873,"win":33.37,"med":-38.98,"avg":12.92,"pnl":-9351.28},"keep_only":{"n":611,"win":62.36,"med":50.0,"avg":61.84,"pnl":10167.45},"keep_only_recent":{"n":428,"win":61.21,"med":53.33,"avg":74.4,"pnl":6557.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S356","S357","S361","S362","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S359","S360","S363","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
13:01:22  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.70|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $226.70|
|  Cash                                                           $226.70|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                   $0.00|
|  Open P&L                                                        $+0.00|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (0 positions)                      |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
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
|  2026-09-17  SELL  AMP  Pullback50  $33.90  P&L $-0.17                 |
|  2026-09-17  SELL  GLW  Pullback50  $33.94  P&L $-0.14                 |
|  2026-09-17  SELL  CTAS  Pullback50  $33.33  P&L $-0.29                |
|  2026-09-17  SELL  CIEN  MomReversal  $35.57  P&L $+2.03               |
|  2026-09-17  SELL  RBC  MomReversal  $35.01  P&L $+1.38                |
|  2026-09-16  SELL  CIEN  MomReversal  $33.44  P&L $-0.18               |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-18T09:01:24.493334-04:00 share=25% ===
2026-09-18 09:01:24,493 INFO === options_live_micro LIVE 2026-09-18T09:01:24.493334-04:00 share=25% ===
Live account equity $226.70 cash $226.70 #225458845 options_level=3
2026-09-18 09:01:24,616 INFO Live account equity $226.70 cash $226.70 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-18 09:01:24,654 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-18 09:01:24,685 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (175 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-18
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     5 | WARN | <<<
| Orphaned lots (post-stable) |  1370 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |    84 | INFO |
| Total closed lots           |  2321 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-18_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-18_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1311 med=-33.3% | TAINTED n=1873 med=-39.0% | KEEP-only n=611 med=+50.0% | KILL=22 KEEP=20
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260918T130609Z

- UTC timestamp: `20260918T130609Z`
- GitHub run: [#10372](https://github.com/28twagg-ops/TradingBot/actions/runs/35348153724)
- Run id: `35348153724`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`13s`
- Full logs: `logs/action_runs/20260918T130609Z_live_bot.log`, `logs/action_runs/20260918T130609Z_live_options.log`, `logs/action_runs/20260918T130609Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1311 | 47.5 | -33.3 | +35.9 | $+15,191 |
| TAINTED | 1873 | 33.4 | -39.0 | +12.9 | $-9,351 |
| KEEP-only | 611 | 62.4 | +50.0 | +61.8 | $+10,167 |
| KEEP-only recent | 428 | 61.2 | +53.3 | +74.4 | $+6,557 |

- KEEP strategies (20): S163, S168, S173, S174, S210, S218, S350, S353, S356, S357, S361, S362, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (22): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S359, S360, S363, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-18T09:06:15.339299-04:00","date":"2026-09-18","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.22},"signals":0,"placed":0,"equity":996457.61,"open_positions":24,"pending_orders":0,"open_lots":84,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10372","github_run_id":"35348153724","status":"ok","data_quality":{"clean":{"n":1311,"win":47.52,"med":-33.33,"avg":35.94,"pnl":15191.16},"tainted":{"n":1873,"win":33.37,"med":-38.98,"avg":12.92,"pnl":-9351.28},"keep_only":{"n":611,"win":62.36,"med":50.0,"avg":61.84,"pnl":10167.45},"keep_only_recent":{"n":428,"win":61.21,"med":53.33,"avg":74.4,"pnl":6557.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S356","S357","S361","S362","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S359","S360","S363","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
13:06:10  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.70|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $226.70|
|  Cash                                                           $226.70|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                   $0.00|
|  Open P&L                                                        $+0.00|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (0 positions)                      |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
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
|  2026-09-17  SELL  AMP  Pullback50  $33.90  P&L $-0.17                 |
|  2026-09-17  SELL  GLW  Pullback50  $33.94  P&L $-0.14                 |
|  2026-09-17  SELL  CTAS  Pullback50  $33.33  P&L $-0.29                |
|  2026-09-17  SELL  CIEN  MomReversal  $35.57  P&L $+2.03               |
|  2026-09-17  SELL  RBC  MomReversal  $35.01  P&L $+1.38                |
|  2026-09-16  SELL  CIEN  MomReversal  $33.44  P&L $-0.18               |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-18T09:06:12.274592-04:00 share=25% ===
2026-09-18 09:06:12,274 INFO === options_live_micro LIVE 2026-09-18T09:06:12.274592-04:00 share=25% ===
Live account equity $226.70 cash $226.70 #225458845 options_level=3
2026-09-18 09:06:12,373 INFO Live account equity $226.70 cash $226.70 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-18 09:06:12,398 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-18 09:06:12,424 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (175 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-18
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     5 | WARN | <<<
| Orphaned lots (post-stable) |  1370 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |    84 | INFO |
| Total closed lots           |  2321 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-18_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-18_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1311 med=-33.3% | TAINTED n=1873 med=-39.0% | KEEP-only n=611 med=+50.0% | KILL=22 KEEP=20
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260918T131108Z

- UTC timestamp: `20260918T131108Z`
- GitHub run: [#10373](https://github.com/28twagg-ops/TradingBot/actions/runs/35348626412)
- Run id: `35348626412`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`13s`
- Full logs: `logs/action_runs/20260918T131108Z_live_bot.log`, `logs/action_runs/20260918T131108Z_live_options.log`, `logs/action_runs/20260918T131108Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1311 | 47.5 | -33.3 | +35.9 | $+15,191 |
| TAINTED | 1873 | 33.4 | -39.0 | +12.9 | $-9,351 |
| KEEP-only | 611 | 62.4 | +50.0 | +61.8 | $+10,167 |
| KEEP-only recent | 428 | 61.2 | +53.3 | +74.4 | $+6,557 |

- KEEP strategies (20): S163, S168, S173, S174, S210, S218, S350, S353, S356, S357, S361, S362, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (22): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S359, S360, S363, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-18T09:11:16.035201-04:00","date":"2026-09-18","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.2,"phases_s":{"reconcile":0.43},"signals":0,"placed":0,"equity":996423.61,"open_positions":24,"pending_orders":0,"open_lots":84,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10373","github_run_id":"35348626412","status":"ok","data_quality":{"clean":{"n":1311,"win":47.52,"med":-33.33,"avg":35.94,"pnl":15191.16},"tainted":{"n":1873,"win":33.37,"med":-38.98,"avg":12.92,"pnl":-9351.28},"keep_only":{"n":611,"win":62.36,"med":50.0,"avg":61.84,"pnl":10167.45},"keep_only_recent":{"n":428,"win":61.21,"med":53.33,"avg":74.4,"pnl":6557.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S356","S357","S361","S362","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S359","S360","S363","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
13:11:11  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.70|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $226.70|
|  Cash                                                           $226.70|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                   $0.00|
|  Open P&L                                                        $+0.00|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (0 positions)                      |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
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
|  2026-09-17  SELL  AMP  Pullback50  $33.90  P&L $-0.17                 |
|  2026-09-17  SELL  GLW  Pullback50  $33.94  P&L $-0.14                 |
|  2026-09-17  SELL  CTAS  Pullback50  $33.33  P&L $-0.29                |
|  2026-09-17  SELL  CIEN  MomReversal  $35.57  P&L $+2.03               |
|  2026-09-17  SELL  RBC  MomReversal  $35.01  P&L $+1.38                |
|  2026-09-16  SELL  CIEN  MomReversal  $33.44  P&L $-0.18               |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-18T09:11:12.780963-04:00 share=25% ===
2026-09-18 09:11:12,781 INFO === options_live_micro LIVE 2026-09-18T09:11:12.780963-04:00 share=25% ===
Live account equity $226.70 cash $226.70 #225458845 options_level=3
2026-09-18 09:11:12,988 INFO Live account equity $226.70 cash $226.70 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-18 09:11:13,046 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-18 09:11:13,103 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (175 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-18
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     5 | WARN | <<<
| Orphaned lots (post-stable) |  1370 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |    84 | INFO |
| Total closed lots           |  2321 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-18_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-18_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1311 med=-33.3% | TAINTED n=1873 med=-39.0% | KEEP-only n=611 med=+50.0% | KILL=22 KEEP=20
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260918T131604Z

- UTC timestamp: `20260918T131604Z`
- GitHub run: [#10374](https://github.com/28twagg-ops/TradingBot/actions/runs/35349116848)
- Run id: `35349116848`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`13s`
- Full logs: `logs/action_runs/20260918T131604Z_live_bot.log`, `logs/action_runs/20260918T131604Z_live_options.log`, `logs/action_runs/20260918T131604Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1311 | 47.5 | -33.3 | +35.9 | $+15,191 |
| TAINTED | 1873 | 33.4 | -39.0 | +12.9 | $-9,351 |
| KEEP-only | 611 | 62.4 | +50.0 | +61.8 | $+10,167 |
| KEEP-only recent | 428 | 61.2 | +53.3 | +74.4 | $+6,557 |

- KEEP strategies (20): S163, S168, S173, S174, S210, S218, S350, S353, S356, S357, S361, S362, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (22): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S359, S360, S363, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-18T09:16:09.444530-04:00","date":"2026-09-18","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.1},"signals":0,"placed":0,"equity":996422.61,"open_positions":24,"pending_orders":0,"open_lots":84,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10374","github_run_id":"35349116848","status":"ok","data_quality":{"clean":{"n":1311,"win":47.52,"med":-33.33,"avg":35.94,"pnl":15191.16},"tainted":{"n":1873,"win":33.37,"med":-38.98,"avg":12.92,"pnl":-9351.28},"keep_only":{"n":611,"win":62.36,"med":50.0,"avg":61.84,"pnl":10167.45},"keep_only_recent":{"n":428,"win":61.21,"med":53.33,"avg":74.4,"pnl":6557.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S356","S357","S361","S362","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S359","S360","S363","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
13:16:05  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.70|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $226.70|
|  Cash                                                           $226.70|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                   $0.00|
|  Open P&L                                                        $+0.00|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (0 positions)                      |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
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
|  2026-09-17  SELL  AMP  Pullback50  $33.90  P&L $-0.17                 |
|  2026-09-17  SELL  GLW  Pullback50  $33.94  P&L $-0.14                 |
|  2026-09-17  SELL  CTAS  Pullback50  $33.33  P&L $-0.29                |
|  2026-09-17  SELL  CIEN  MomReversal  $35.57  P&L $+2.03               |
|  2026-09-17  SELL  RBC  MomReversal  $35.01  P&L $+1.38                |
|  2026-09-16  SELL  CIEN  MomReversal  $33.44  P&L $-0.18               |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-18T09:16:06.643362-04:00 share=25% ===
2026-09-18 09:16:06,643 INFO === options_live_micro LIVE 2026-09-18T09:16:06.643362-04:00 share=25% ===
Live account equity $226.70 cash $226.70 #225458845 options_level=3
2026-09-18 09:16:06,687 INFO Live account equity $226.70 cash $226.70 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-18 09:16:06,697 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-18 09:16:06,704 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (175 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-18
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     5 | WARN | <<<
| Orphaned lots (post-stable) |  1370 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |    84 | INFO |
| Total closed lots           |  2321 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-18_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-18_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1311 med=-33.3% | TAINTED n=1873 med=-39.0% | KEEP-only n=611 med=+50.0% | KILL=22 KEEP=20
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260918T132108Z

- UTC timestamp: `20260918T132108Z`
- GitHub run: [#10375](https://github.com/28twagg-ops/TradingBot/actions/runs/35349596786)
- Run id: `35349596786`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`13s`
- Full logs: `logs/action_runs/20260918T132108Z_live_bot.log`, `logs/action_runs/20260918T132108Z_live_options.log`, `logs/action_runs/20260918T132108Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1311 | 47.5 | -33.3 | +35.9 | $+15,191 |
| TAINTED | 1873 | 33.4 | -39.0 | +12.9 | $-9,351 |
| KEEP-only | 611 | 62.4 | +50.0 | +61.8 | $+10,167 |
| KEEP-only recent | 428 | 61.2 | +53.3 | +74.4 | $+6,557 |

- KEEP strategies (20): S163, S168, S173, S174, S210, S218, S350, S353, S356, S357, S361, S362, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (22): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S359, S360, S363, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-18T09:21:13.663700-04:00","date":"2026-09-18","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.8,"phases_s":{"reconcile":0.19},"signals":0,"placed":0,"equity":996414.16,"open_positions":24,"pending_orders":0,"open_lots":84,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10375","github_run_id":"35349596786","status":"ok","data_quality":{"clean":{"n":1311,"win":47.52,"med":-33.33,"avg":35.94,"pnl":15191.16},"tainted":{"n":1873,"win":33.37,"med":-38.98,"avg":12.92,"pnl":-9351.28},"keep_only":{"n":611,"win":62.36,"med":50.0,"avg":61.84,"pnl":10167.45},"keep_only_recent":{"n":428,"win":61.21,"med":53.33,"avg":74.4,"pnl":6557.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S356","S357","S361","S362","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S359","S360","S363","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
13:21:09  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.70|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $226.70|
|  Cash                                                           $226.70|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                   $0.00|
|  Open P&L                                                        $+0.00|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (0 positions)                      |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
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
|  2026-09-17  SELL  AMP  Pullback50  $33.90  P&L $-0.17                 |
|  2026-09-17  SELL  GLW  Pullback50  $33.94  P&L $-0.14                 |
|  2026-09-17  SELL  CTAS  Pullback50  $33.33  P&L $-0.29                |
|  2026-09-17  SELL  CIEN  MomReversal  $35.57  P&L $+2.03               |
|  2026-09-17  SELL  RBC  MomReversal  $35.01  P&L $+1.38                |
|  2026-09-16  SELL  CIEN  MomReversal  $33.44  P&L $-0.18               |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-18T09:21:10.526131-04:00 share=25% ===
2026-09-18 09:21:10,526 INFO === options_live_micro LIVE 2026-09-18T09:21:10.526131-04:00 share=25% ===
Live account equity $226.70 cash $226.70 #225458845 options_level=3
2026-09-18 09:21:10,624 INFO Live account equity $226.70 cash $226.70 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-18 09:21:10,649 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-18 09:21:10,674 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (175 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-18
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     5 | WARN | <<<
| Orphaned lots (post-stable) |  1370 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |    84 | INFO |
| Total closed lots           |  2321 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-18_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-18_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1311 med=-33.3% | TAINTED n=1873 med=-39.0% | KEEP-only n=611 med=+50.0% | KILL=22 KEEP=20
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260918T132612Z

- UTC timestamp: `20260918T132612Z`
- GitHub run: [#10376](https://github.com/28twagg-ops/TradingBot/actions/runs/35350083477)
- Run id: `35350083477`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`11s`
- Full logs: `logs/action_runs/20260918T132612Z_live_bot.log`, `logs/action_runs/20260918T132612Z_live_options.log`, `logs/action_runs/20260918T132612Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1311 | 47.5 | -33.3 | +35.9 | $+15,191 |
| TAINTED | 1873 | 33.4 | -39.0 | +12.9 | $-9,351 |
| KEEP-only | 611 | 62.4 | +50.0 | +61.8 | $+10,167 |
| KEEP-only recent | 428 | 61.2 | +53.3 | +74.4 | $+6,557 |

- KEEP strategies (20): S163, S168, S173, S174, S210, S218, S350, S353, S356, S357, S361, S362, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (22): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S359, S360, S363, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-18T09:26:18.299529-04:00","date":"2026-09-18","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.28},"signals":0,"placed":0,"equity":996522.61,"open_positions":24,"pending_orders":0,"open_lots":84,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10376","github_run_id":"35350083477","status":"ok","data_quality":{"clean":{"n":1311,"win":47.52,"med":-33.33,"avg":35.94,"pnl":15191.16},"tainted":{"n":1873,"win":33.37,"med":-38.98,"avg":12.92,"pnl":-9351.28},"keep_only":{"n":611,"win":62.36,"med":50.0,"avg":61.84,"pnl":10167.45},"keep_only_recent":{"n":428,"win":61.21,"med":53.33,"avg":74.4,"pnl":6557.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S356","S357","S361","S362","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S359","S360","S363","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
13:26:14  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.70|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $226.70|
|  Cash                                                           $226.70|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                   $0.00|
|  Open P&L                                                        $+0.00|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (0 positions)                      |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
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
|  2026-09-17  SELL  AMP  Pullback50  $33.90  P&L $-0.17                 |
|  2026-09-17  SELL  GLW  Pullback50  $33.94  P&L $-0.14                 |
|  2026-09-17  SELL  CTAS  Pullback50  $33.33  P&L $-0.29                |
|  2026-09-17  SELL  CIEN  MomReversal  $35.57  P&L $+2.03               |
|  2026-09-17  SELL  RBC  MomReversal  $35.01  P&L $+1.38                |
|  2026-09-16  SELL  CIEN  MomReversal  $33.44  P&L $-0.18               |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-18T09:26:15.398484-04:00 share=25% ===
2026-09-18 09:26:15,398 INFO === options_live_micro LIVE 2026-09-18T09:26:15.398484-04:00 share=25% ===
Live account equity $226.70 cash $226.70 #225458845 options_level=3
2026-09-18 09:26:15,529 INFO Live account equity $226.70 cash $226.70 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-18 09:26:15,562 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-18 09:26:15,593 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (175 earlier lines - see full log file)
Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 267 | 16 |
| S164 | 299 | 21 |
| S165 | 1735 | 33 |
| S166 | 135 | 9 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-18
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     5 | WARN | <<<
| Orphaned lots (post-stable) |  1370 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |    84 | INFO |
| Total closed lots           |  2321 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-18_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-18_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1311 med=-33.3% | TAINTED n=1873 med=-39.0% | KEEP-only n=611 med=+50.0% | KILL=22 KEEP=20
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260918T133113Z

- UTC timestamp: `20260918T133113Z`
- GitHub run: [#10377](https://github.com/28twagg-ops/TradingBot/actions/runs/35350566455)
- Run id: `35350566455`
- Live bot: exit=`0`, duration=`221s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260918T133113Z_live_bot.log`, `logs/action_runs/20260918T133113Z_live_options.log`, `logs/action_runs/20260918T133113Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1311 | 47.5 | -33.3 | +35.9 | $+15,191 |
| TAINTED | 1873 | 33.4 | -39.0 | +12.9 | $-9,351 |
| KEEP-only | 611 | 62.4 | +50.0 | +61.8 | $+10,167 |
| KEEP-only recent | 428 | 61.2 | +53.3 | +74.4 | $+6,557 |

- KEEP strategies (20): S163, S168, S173, S174, S210, S218, S350, S353, S356, S357, S361, S362, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (22): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S359, S360, S363, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-18T09:26:18.299529-04:00","date":"2026-09-18","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.28},"signals":0,"placed":0,"equity":996522.61,"open_positions":24,"pending_orders":0,"open_lots":84,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10376","github_run_id":"35350083477","status":"ok","data_quality":{"clean":{"n":1311,"win":47.52,"med":-33.33,"avg":35.94,"pnl":15191.16},"tainted":{"n":1873,"win":33.37,"med":-38.98,"avg":12.92,"pnl":-9351.28},"keep_only":{"n":611,"win":62.36,"med":50.0,"avg":61.84,"pnl":10167.45},"keep_only_recent":{"n":428,"win":61.21,"med":53.33,"avg":74.4,"pnl":6557.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S356","S357","S361","S362","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S359","S360","S363","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
13:31:17  INFO      Mode: morning_prep
13:31:18  INFO        [prep_positions] 3/3 (3 valid)
13:31:18  INFO      Fetching tickers (universe=both)...
13:31:18  INFO        S&P 500: 503
13:31:18  INFO        MidCap 400: 400
13:31:18  INFO        Total: 903 tickers
13:31:19  INFO        [prep_universe] 40/900 (40 valid)
13:31:21  INFO        [prep_universe] 80/900 (80 valid)
13:31:22  INFO        [prep_universe] 120/900 (120 valid)
13:31:24  INFO        [prep_universe] 160/900 (160 valid)
13:31:25  INFO        [prep_universe] 200/900 (199 valid)
13:31:32  INFO        [prep_universe] 240/900 (238 valid)
13:31:43  INFO        [prep_universe] 280/900 (278 valid)
13:31:56  INFO        [prep_universe] 320/900 (318 valid)
13:32:09  INFO        [prep_universe] 360/900 (358 valid)
13:32:20  INFO        [prep_universe] 400/900 (398 valid)
13:32:33  INFO        [prep_universe] 440/900 (438 valid)
13:32:43  INFO        [prep_universe] 480/900 (478 valid)
13:32:57  INFO        [prep_universe] 520/900 (518 valid)
13:33:07  INFO        [prep_universe] 560/900 (558 valid)
13:33:20  INFO        [prep_universe] 600/900 (598 valid)
13:33:31  INFO        [prep_universe] 640/900 (638 valid)
13:33:44  INFO        [prep_universe] 680/900 (678 valid)
13:33:58  INFO        [prep_universe] 720/900 (718 valid)
13:34:08  INFO        [prep_universe] 760/900 (758 valid)
13:34:21  INFO        [prep_universe] 800/900 (798 valid)
13:34:31  INFO        [prep_universe] 840/900 (838 valid)
13:34:45  INFO        [prep_universe] 880/900 (878 valid)
13:34:52  INFO        [prep_universe] 900/900 (898 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.60|
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
|  Invested                                                       $101.88|
|  Open P&L                                                        $-0.09|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  BLDR     MomReversal     $33.95     $57.27   $57.20   -0.1%   $-0.04  |
|  CIEN     MomReversal     $33.88     $357.43  $356.25  -0.3%   $-0.11  |
|  VICR     MA_Squeeze      $34.06     $219.62  $220.06  +0.2%   $+0.07  |
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
|  Signal candidates                                                   17|
|  Universe scanned                                                   900|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-18T09:34:55.389718-04:00 share=25% ===
2026-09-18 09:34:55,389 INFO === options_live_micro LIVE 2026-09-18T09:34:55.389718-04:00 share=25% ===
Live account equity $226.14 cash $124.72 #225458845 options_level=3
2026-09-18 09:34:55,614 INFO Live account equity $226.14 cash $124.72 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-18 09:34:55,819 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-18 09:34:55,956 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=84 paper_keys=yes dry_run=False
  alpaca positions=17
  FLAG b0|ORPHAN|92d6ead4 missing from Alpaca
  FLAG b165|S216|ea654917 missing from Alpaca
  FLAG b164|S216|860979ba missing from Alpaca
  FLAG b181|S217|bb4a175d missing from Alpaca
  FLAG b779|S397|eb8be0fb missing from Alpaca
  FLAG b778|S397|9af34f50 missing from Alpaca
  FLAG b794|S399|24008571 missing from Alpaca
  FLAG b238|S401|71d52528 missing from Alpaca
  FLAG b0|ORPHAN|1d79395b missing from Alpaca
  FLAG b796|S399|fc72dff5 missing from Alpaca
  FLAG b905|S411|f124c56d missing from Alpaca
  FLAG b904|S411|587ebec9 missing from Alpaca
  FLAG b807|S404|b94d2100 missing from Alpaca
  FLAG b806|S404|8fc58b3b missing from Alpaca
  FLAG b782|S397|df23aa2d missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$996,153.68
  buying_power=$3,929,896.88 cash=$1,030,424.21
  open option orders: 7
    PATH260918C00016000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=0.01
    OXY260918C00059000 OrderSide.SELL qty=2 status=OrderStatus.NEW limit=None
    HON260918C00217500 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
    SNOW260918C00345000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
    PATH260918C00014500 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=0.18
  open option positions: 16
    CRWD260918C00270000 qty=1 mkt=$1.00
    CRWD260918C00275000 qty=-1 mkt=$-2.00
    HON260918C00215000 qty=1 mkt=$0.00
    MARA260918C00011000 qty=-1 mkt=$-125.00
    MARA260918C00012000 qty=50 mkt=$1,600.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-18T09:34:59.425401-04:00 ===

[Run context]
Paper auth OK — equity $996155.21, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
2026-09-18 09:35:01,741 INFO   EXIT [b264|lab0264_s403_w2_1005_1045_r1|S403] stop_loss (-87.8%) SELL 1 SLB260918C00052500 @<= 0.06
2026-09-18 09:35:02,266 INFO   EXIT [b1128|lab1128_s168_w4_1120_1135_r1|S168] take_profit (+63.5%) SELL 1 MARA260918C00012000 @<= 0.33
  EXIT [b783|lab0783_s397_w4_1120_1135_r2|S397] stop_loss (-77.8%) SELL failed SNOW260918C00347500: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
2026-09-18 09:35:04,385 INFO   EXIT [b241|lab0241_s401_w4_1120_1135_r2|S401] stop_loss (-51.0%) SELL 1 OXY260918C00059000 @<= 0.22
2026-09-18 09:35:05,114 INFO   EXIT [b234|lab0234_s401_w1_0928_1005_r1|S401] stop_loss (-66.7%) SELL 1 XOM260918C00172500 @<= 0.01
  EXIT [b858|lab0858_s408_w2_1005_1045_r1|S408] stop_loss (-90.0%) SELL failed CRWD260918C00270000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
2026-09-18 09:35:07,443 INFO   EXIT [b419|lab0419_s365_w1_0928_1005_r2|S365] take_profit (+56.1%) SELL 1 MARA261002C00012000 @<= 0.86
  EXIT [b182|lab0182_s217_w3_1045_1120_r1|S217] stop_loss (-100.0%) SELL failed HON260918C00215000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b861|lab0861_s408_w3_1045_1120_r2|S408] stop_loss (-100.0%) SELL failed MSTR260918C00157500: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
Protective stops: placed=0 upgraded=0 already=2 failed=9 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
```

---

## Run 20260918T133649Z

- UTC timestamp: `20260918T133649Z`
- GitHub run: [#10378](https://github.com/28twagg-ops/TradingBot/actions/runs/35351059721)
- Run id: `35351059721`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260918T133649Z_live_bot.log`, `logs/action_runs/20260918T133649Z_live_options.log`, `logs/action_runs/20260918T133649Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1311 | 47.5 | -33.3 | +35.9 | $+15,191 |
| TAINTED | 1873 | 33.4 | -39.0 | +12.9 | $-9,351 |
| KEEP-only | 611 | 62.4 | +50.0 | +61.8 | $+10,167 |
| KEEP-only recent | 428 | 61.2 | +53.3 | +74.4 | $+6,557 |

- KEEP strategies (20): S163, S168, S173, S174, S210, S218, S350, S353, S356, S357, S361, S362, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (22): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S359, S360, S363, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-18T09:26:18.299529-04:00","date":"2026-09-18","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.28},"signals":0,"placed":0,"equity":996522.61,"open_positions":24,"pending_orders":0,"open_lots":84,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10376","github_run_id":"35350083477","status":"ok","data_quality":{"clean":{"n":1311,"win":47.52,"med":-33.33,"avg":35.94,"pnl":15191.16},"tainted":{"n":1873,"win":33.37,"med":-38.98,"avg":12.92,"pnl":-9351.28},"keep_only":{"n":611,"win":62.36,"med":50.0,"avg":61.84,"pnl":10167.45},"keep_only_recent":{"n":428,"win":61.21,"med":53.33,"avg":74.4,"pnl":6557.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S356","S357","S361","S362","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S359","S360","S363","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
13:36:51  INFO      Mode: morning_prep
13:36:53  INFO        [prep_positions] 3/3 (3 valid)
13:36:53  INFO      Fetching tickers (universe=both)...
13:36:53  INFO        S&P 500: 503
13:36:54  INFO        MidCap 400: 400
13:36:54  INFO        Total: 903 tickers
13:36:55  INFO        [prep_universe] 40/900 (40 valid)
13:36:57  INFO        [prep_universe] 80/900 (80 valid)
13:36:58  INFO        [prep_universe] 120/900 (120 valid)
13:36:59  INFO        [prep_universe] 160/900 (160 valid)
13:37:00  INFO        [prep_universe] 200/900 (199 valid)
13:37:08  INFO        [prep_universe] 240/900 (238 valid)
13:37:18  INFO        [prep_universe] 280/900 (278 valid)
13:37:32  INFO        [prep_universe] 320/900 (318 valid)
13:37:42  INFO        [prep_universe] 360/900 (358 valid)
13:37:56  INFO        [prep_universe] 400/900 (398 valid)
13:38:09  INFO        [prep_universe] 440/900 (438 valid)
13:38:19  INFO        [prep_universe] 480/900 (478 valid)
13:38:33  INFO        [prep_universe] 520/900 (518 valid)
13:38:43  INFO        [prep_universe] 560/900 (558 valid)
13:38:56  INFO        [prep_universe] 600/900 (598 valid)
13:39:07  INFO        [prep_universe] 640/900 (638 valid)
13:39:20  INFO        [prep_universe] 680/900 (678 valid)
13:39:31  INFO        [prep_universe] 720/900 (718 valid)
13:39:44  INFO        [prep_universe] 760/900 (758 valid)
13:39:55  INFO        [prep_universe] 800/900 (798 valid)
13:40:08  INFO        [prep_universe] 840/900 (838 valid)
13:40:18  INFO        [prep_universe] 880/900 (878 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20260918T134143Z

- UTC timestamp: `20260918T134143Z`
- GitHub run: [#10379](https://github.com/28twagg-ops/TradingBot/actions/runs/35351544900)
- Run id: `35351544900`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260918T134143Z_live_bot.log`, `logs/action_runs/20260918T134143Z_live_options.log`, `logs/action_runs/20260918T134143Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1311 | 47.5 | -33.3 | +35.9 | $+15,191 |
| TAINTED | 1873 | 33.4 | -39.0 | +12.9 | $-9,351 |
| KEEP-only | 611 | 62.4 | +50.0 | +61.8 | $+10,167 |
| KEEP-only recent | 428 | 61.2 | +53.3 | +74.4 | $+6,557 |

- KEEP strategies (20): S163, S168, S173, S174, S210, S218, S350, S353, S356, S357, S361, S362, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (22): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S359, S360, S363, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-18T09:26:18.299529-04:00","date":"2026-09-18","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.28},"signals":0,"placed":0,"equity":996522.61,"open_positions":24,"pending_orders":0,"open_lots":84,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10376","github_run_id":"35350083477","status":"ok","data_quality":{"clean":{"n":1311,"win":47.52,"med":-33.33,"avg":35.94,"pnl":15191.16},"tainted":{"n":1873,"win":33.37,"med":-38.98,"avg":12.92,"pnl":-9351.28},"keep_only":{"n":611,"win":62.36,"med":50.0,"avg":61.84,"pnl":10167.45},"keep_only_recent":{"n":428,"win":61.21,"med":53.33,"avg":74.4,"pnl":6557.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S356","S357","S361","S362","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S359","S360","S363","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
13:41:45  INFO      Mode: morning_prep
13:41:46  INFO        [prep_positions] 3/3 (3 valid)
13:41:46  INFO        Universe cache hit: 903 tickers (tickers_2026-09-18.json)
13:41:47  INFO        [prep_universe] 40/900 (40 valid)
13:41:48  INFO        [prep_universe] 80/900 (80 valid)
13:41:49  INFO        [prep_universe] 120/900 (120 valid)
13:41:51  INFO        [prep_universe] 160/900 (160 valid)
13:41:52  INFO        [prep_universe] 200/900 (199 valid)
13:42:02  INFO        [prep_universe] 240/900 (238 valid)
13:42:12  INFO        [prep_universe] 280/900 (278 valid)
13:42:25  INFO        [prep_universe] 320/900 (318 valid)
13:42:38  INFO        [prep_universe] 360/900 (358 valid)
13:42:47  INFO        [prep_universe] 400/900 (398 valid)
13:43:01  INFO        [prep_universe] 440/900 (438 valid)
13:43:13  INFO        [prep_universe] 480/900 (478 valid)
13:43:23  INFO        [prep_universe] 520/900 (518 valid)
13:43:36  INFO        [prep_universe] 560/900 (558 valid)
13:43:49  INFO        [prep_universe] 600/900 (598 valid)
13:44:02  INFO        [prep_universe] 640/900 (638 valid)
13:44:12  INFO        [prep_universe] 680/900 (678 valid)
13:44:25  INFO        [prep_universe] 720/900 (718 valid)
13:44:38  INFO        [prep_universe] 760/900 (758 valid)
13:44:48  INFO        [prep_universe] 800/900 (798 valid)
13:45:01  INFO        [prep_universe] 840/900 (838 valid)
13:45:14  INFO        [prep_universe] 880/900 (878 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20260918T134648Z

- UTC timestamp: `20260918T134648Z`
- GitHub run: [#10380](https://github.com/28twagg-ops/TradingBot/actions/runs/35352045492)
- Run id: `35352045492`
- Live bot: exit=`0`, duration=`36s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`80s`
- Full logs: `logs/action_runs/20260918T134648Z_live_bot.log`, `logs/action_runs/20260918T134648Z_live_options.log`, `logs/action_runs/20260918T134648Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1316 | 47.5 | -33.3 | +35.8 | $+15,193 |
| TAINTED | 1879 | 33.3 | -39.0 | +12.7 | $-9,535 |
| KEEP-only | 614 | 62.2 | +50.0 | +61.4 | $+10,145 |
| KEEP-only recent | 431 | 61.0 | +53.3 | +73.7 | $+6,535 |

- KEEP strategies (20): S163, S168, S173, S174, S210, S218, S350, S353, S356, S357, S361, S362, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (22): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S359, S360, S363, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-18T09:47:28.910019-04:00","date":"2026-09-18","mode":"entry+manage","header":"entry+manage (47 new)","elapsed_s":68.0,"phases_s":{"reconcile":0.68,"cancel":0.12,"manage":3.8,"protective_stops":1.71,"scan":41.56,"entries":14.3,"reconcile2":1.61},"signals":89,"placed":47,"equity":996432.11,"open_positions":25,"pending_orders":19,"open_lots":87,"submitted_today":47,"filled_today":28,"unattributed_contracts":0,"top_signals":["S211:META","S165:NFLX","S164:NFLX","S168:NFLX","S167:NFLX","S166:NFLX","S163:NFLX","S202:NFLX"],"github_run":"10380","github_run_id":"35352045492","status":"ok","data_quality":{"clean":{"n":1316,"win":47.49,"med":-33.33,"avg":35.82,"pnl":15193.16},"tainted":{"n":1879,"win":33.32,"med":-39.02,"avg":12.73,"pnl":-9535.28},"keep_only":{"n":614,"win":62.21,"med":50.0,"avg":61.42,"pnl":10145.45},"keep_only_recent":{"n":431,"win":61.02,"med":53.33,"avg":73.71,"pnl":6535.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S356","S357","S361","S362","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S359","S360","S363","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
... (70 earlier lines - see full log file)
|  VICR  P&L +1.3%  $+0.43                          EXIT: midline (-0.2%)|
+========================================================================+

+========================================================================+
|                           EXIT EVAL SUMMARY                            |
+========================================================================+
|  Exit eval    attempted 2 | filled 2 | partial 0 | pending 0 | failed 0|
|  Other skips     already logged today 0  |  no price data 0  |  holds 1|
|  Stop-loss breaches                                                   1|
|  CIEN                                        -2.32%  (threshold -0.50%)|
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
|  Month: Sep  |  Regime: BULL                                           |
|  Primary: GapDown  |  Secondary: VolumeSpike (display only — schedule ~|
|  Source                                                cached prep plan|
|  Universe scanned in prep                                           900|
+========================================================================+

+========================================================================+
|                         SIGNALS FOUND  --  18                          |
+========================================================================+
|  TICKER   STRATEGY        TIER   PRICE    RSI    VOL_Z   TRIGGER       |
+------------------------------------------------------------------------+
|  MO       Pullback50      eq     $69.38   54.8   -2.65   50MA bounce (+|
|  ETN      Pullback50      eq     $413.37  54.2   -2.71   50MA bounce (-|
|  EW       Pullback50      eq     $88.29   43.4   -2.58   50MA bounce (-|
|  FAST     Pullback50      eq     $49.10   44.0   -2.99   50MA bounce (+|
|  KMI      Pullback50      eq     $31.52   49.5   -2.15   50MA bounce (-|
|  MCK      Pullback50      eq     $873.72  44.0   -2.52   50MA bounce (+|
|  OKE      Pullback50      eq     $92.83   42.5   -2.52   50MA bounce (-|
|  PM       Pullback50      eq     $188.69  44.6   -2.75   50MA bounce (-|
|  TER      Pullback50      eq     $360.75  51.6   -2.44   50MA bounce (-|
|  VZ       Pullback50      eq     $47.71   34.4   -2.99   50MA bounce (+|
|  ESNT     Pullback50      eq     $66.92   37.0   -2.21   50MA bounce (-|
|  HOG      Pullback50      eq     $26.55   38.3   -3.11   50MA bounce (-|
|  KRYS     Pullback50      eq     $341.13  41.7   -2.57   50MA bounce (-|
|  LNTH     Pullback50      eq     $100.86  51.5   -2.61   50MA bounce (-|
|  NOV      Pullback50      eq     $20.34   39.9   -2.59   50MA bounce (-|
|  PAG      Pullback50      eq     $213.70  39.8   -2.22   50MA bounce (-|
|  PK       Pullback50      eq     $14.98   34.5   -2.47   50MA bounce (-|
|  SANM     Pullback50      eq     $198.98  53.2   -2.40   50MA bounce (-|
|                                                                        |
+========================================================================+

+========================================================================+
13:47:23  INFO        place_all_stops: checking 1 positions...
13:47:23  INFO        STOP skipped BLDR: fractional (0.5935 shares) — software exit will handle it
13:47:24  INFO        Daily log -> logs/daily/2026-09-18.md
13:47:24  INFO        Dashboard written → logs/dashboard.md
|                              ENTRY ORDERS                              |
+========================================================================+
|  Skipped                                  no entry slots (max_trades=0)|
+========================================================================+

+========================================================================+
|                            SESSION SUMMARY                             |
+========================================================================+
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Strategy  GapDown + VolumeSpike (display only — schedule not enforced)|
|  Scanned                                                              0|
|  Signals                                                             18|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  0 unconfirmed|
|  Exits                                                                2|
|  Open pos                                                             1|
|  Equity                                                         $226.15|
|  Cash                                                           $192.26|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-18T09:47:24.991236-04:00 share=25% ===
2026-09-18 09:47:24,991 INFO === options_live_micro LIVE 2026-09-18T09:47:24.991236-04:00 share=25% ===
Live account equity $226.15 cash $192.26 #225458845 options_level=3
2026-09-18 09:47:25,203 INFO Live account equity $226.15 cash $192.26 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-18 09:47:25,379 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-18 09:47:25,492 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (220 earlier lines - see full log file)

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 271 | 17 |
| S164 | 299 | 21 |
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
| 2026-09-18 |    4 |    0 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-18
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1368 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |    87 | INFO |
| Total closed lots           |  2331 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-18_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-18_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1316 med=-33.3% | TAINTED n=1879 med=-39.0% | KEEP-only n=614 med=+50.0% | KILL=22 KEEP=20
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.15 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260918T135109Z

- UTC timestamp: `20260918T135109Z`
- GitHub run: [#10381](https://github.com/28twagg-ops/TradingBot/actions/runs/35352538141)
- Run id: `35352538141`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`72s`
- Full logs: `logs/action_runs/20260918T135109Z_live_bot.log`, `logs/action_runs/20260918T135109Z_live_options.log`, `logs/action_runs/20260918T135109Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1317 | 47.5 | -33.3 | +35.9 | $+15,227 |
| TAINTED | 1879 | 33.3 | -39.0 | +12.7 | $-9,535 |
| KEEP-only | 614 | 62.2 | +50.0 | +61.4 | $+10,145 |
| KEEP-only recent | 431 | 61.0 | +53.3 | +73.7 | $+6,535 |

- KEEP strategies (20): S163, S168, S173, S174, S210, S218, S350, S353, S356, S357, S361, S362, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (22): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S359, S360, S363, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-18T09:51:15.390762-04:00","date":"2026-09-18","mode":"entry+manage","header":"entry+manage (1 new)","elapsed_s":60.0,"phases_s":{"reconcile":0.78,"cancel":0.05,"manage":8.39,"protective_stops":1.03,"scan":45.33,"entries":2.36,"reconcile2":0.26},"signals":89,"placed":1,"equity":996603.08,"open_positions":25,"pending_orders":7,"open_lots":98,"submitted_today":48,"filled_today":41,"unattributed_contracts":0,"top_signals":["S211:META","S165:NFLX","S164:NFLX","S168:NFLX","S167:NFLX","S166:NFLX","S163:NFLX","S202:NFLX"],"github_run":"10381","github_run_id":"35352538141","status":"ok","data_quality":{"clean":{"n":1317,"win":47.53,"med":-33.33,"avg":35.93,"pnl":15227.16},"tainted":{"n":1879,"win":33.32,"med":-39.02,"avg":12.73,"pnl":-9535.28},"keep_only":{"n":614,"win":62.21,"med":50.0,"avg":61.42,"pnl":10145.45},"keep_only_recent":{"n":431,"win":61.02,"med":53.33,"avg":73.71,"pnl":6535.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S356","S357","S361","S362","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S359","S360","S363","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
13:51:10  INFO      Mode: morning_scan
13:51:11  INFO      Morning scan already completed today (2026-09-18T13:47:24.261817Z) — exits-only pass
13:51:11  INFO        Daily log -> logs/daily/2026-09-18.md
13:51:11  INFO        Daily log reconciled -> logs/daily/2026-09-18.md (2 ledger rows)
13:51:11  INFO        place_all_stops: checking 1 positions...
13:51:11  INFO        STOP skipped BLDR: fractional (0.5935 shares) — software exit will handle it
13:51:11  INFO        [positions] 1/1 (1 valid)
13:51:11  INFO        Daily log -> logs/daily/2026-09-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_SCAN|
|  Time                                                         13:51 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.14|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  BLDR  P&L -0.3%  $-0.11                                           HOLD|
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
=== options_live_micro LIVE 2026-09-18T09:51:12.183414-04:00 share=25% ===
2026-09-18 09:51:12,183 INFO === options_live_micro LIVE 2026-09-18T09:51:12.183414-04:00 share=25% ===
Live account equity $226.14 cash $192.26 #225458845 options_level=3
2026-09-18 09:51:12,267 INFO Live account equity $226.14 cash $192.26 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-18 09:51:12,341 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-18 09:51:12,602 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (203 earlier lines - see full log file)

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 271 | 17 |
| S164 | 299 | 21 |
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
| 2026-09-18 |    4 |    0 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-18
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1368 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |    98 | INFO |
| Total closed lots           |  2332 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-18_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-18_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1317 med=-33.3% | TAINTED n=1879 med=-39.0% | KEEP-only n=614 med=+50.0% | KILL=22 KEEP=20
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.14 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260918T135607Z

- UTC timestamp: `20260918T135607Z`
- GitHub run: [#10382](https://github.com/28twagg-ops/TradingBot/actions/runs/35353034252)
- Run id: `35353034252`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`57s`
- Full logs: `logs/action_runs/20260918T135607Z_live_bot.log`, `logs/action_runs/20260918T135607Z_live_options.log`, `logs/action_runs/20260918T135607Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1319 | 47.5 | -33.3 | +36.0 | $+15,234 |
| TAINTED | 1879 | 33.3 | -39.0 | +12.7 | $-9,535 |
| KEEP-only | 616 | 62.2 | +50.0 | +61.4 | $+10,152 |
| KEEP-only recent | 433 | 61.0 | +53.3 | +73.7 | $+6,542 |

- KEEP strategies (20): S163, S168, S173, S174, S210, S218, S350, S353, S356, S357, S361, S362, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (22): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S359, S360, S363, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-18T09:56:13.224777-04:00","date":"2026-09-18","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":47.3,"phases_s":{"reconcile":0.36,"cancel":0.05,"manage":6.38,"protective_stops":1.13,"scan":35.16,"entries":2.42,"reconcile2":0.28},"signals":89,"placed":0,"equity":997073.77,"open_positions":23,"pending_orders":7,"open_lots":94,"submitted_today":48,"filled_today":41,"unattributed_contracts":0,"top_signals":["S211:META","S165:NFLX","S164:NFLX","S168:NFLX","S167:NFLX","S166:NFLX","S163:NFLX","S202:NFLX"],"github_run":"10382","github_run_id":"35353034252","status":"ok","data_quality":{"clean":{"n":1319,"win":47.54,"med":-33.33,"avg":35.98,"pnl":15234.16},"tainted":{"n":1879,"win":33.32,"med":-39.02,"avg":12.73,"pnl":-9535.28},"keep_only":{"n":616,"win":62.18,"med":50.0,"avg":61.44,"pnl":10152.45},"keep_only_recent":{"n":433,"win":60.97,"med":53.33,"avg":73.69,"pnl":6542.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S356","S357","S361","S362","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S359","S360","S363","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
13:56:08  INFO      Mode: morning_scan
13:56:08  INFO      Morning scan already completed today (2026-09-18T13:47:24.261817Z) — exits-only pass
13:56:08  INFO        Daily log -> logs/daily/2026-09-18.md
13:56:08  INFO        Daily log reconciled -> logs/daily/2026-09-18.md (2 ledger rows)
13:56:09  INFO        place_all_stops: checking 1 positions...
13:56:09  INFO        STOP skipped BLDR: fractional (0.5935 shares) — software exit will handle it
13:56:09  INFO        [positions] 1/1 (1 valid)
13:56:09  INFO        Daily log -> logs/daily/2026-09-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_SCAN|
|  Time                                                         13:56 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.14|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  BLDR  P&L -0.3%  $-0.11                                           HOLD|
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
=== options_live_micro LIVE 2026-09-18T09:56:10.240497-04:00 share=25% ===
2026-09-18 09:56:10,240 INFO === options_live_micro LIVE 2026-09-18T09:56:10.240497-04:00 share=25% ===
Live account equity $226.14 cash $192.26 #225458845 options_level=3
2026-09-18 09:56:10,322 INFO Live account equity $226.14 cash $192.26 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-18 09:56:10,392 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-18 09:56:10,433 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (208 earlier lines - see full log file)

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 271 | 17 |
| S164 | 299 | 21 |
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
| 2026-09-18 |    4 |    0 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-18
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1368 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |    94 | INFO |
| Total closed lots           |  2334 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-18_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-18_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1319 med=-33.3% | TAINTED n=1879 med=-39.0% | KEEP-only n=616 med=+50.0% | KILL=22 KEEP=20
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.14 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260918T140113Z

- UTC timestamp: `20260918T140113Z`
- GitHub run: [#10383](https://github.com/28twagg-ops/TradingBot/actions/runs/35353526135)
- Run id: `35353526135`
- Live bot: exit=`0`, duration=`6s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`76s`
- Full logs: `logs/action_runs/20260918T140113Z_live_bot.log`, `logs/action_runs/20260918T140113Z_live_options.log`, `logs/action_runs/20260918T140113Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1320 | 47.6 | -33.3 | +36.1 | $+15,273 |
| TAINTED | 1880 | 33.4 | -39.0 | +12.7 | $-9,533 |
| KEEP-only | 617 | 62.2 | +50.0 | +61.7 | $+10,191 |
| KEEP-only recent | 434 | 61.1 | +53.3 | +74.0 | $+6,581 |

- KEEP strategies (20): S163, S168, S173, S174, S210, S218, S350, S353, S356, S357, S361, S362, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (22): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S359, S360, S363, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-18T10:01:22.782531-04:00","date":"2026-09-18","mode":"entry+manage","header":"entry+manage (2 new)","elapsed_s":64.8,"phases_s":{"reconcile":0.34,"cancel":0.03,"manage":7.54,"protective_stops":0.52,"scan":53.85,"entries":1.19,"reconcile2":0.27},"signals":89,"placed":2,"equity":997044.61,"open_positions":25,"pending_orders":3,"open_lots":99,"submitted_today":50,"filled_today":47,"unattributed_contracts":0,"top_signals":["S211:META","S165:NFLX","S164:NFLX","S168:NFLX","S167:NFLX","S166:NFLX","S163:NFLX","S202:NFLX"],"github_run":"10383","github_run_id":"35353526135","status":"ok","data_quality":{"clean":{"n":1320,"win":47.58,"med":-33.33,"avg":36.11,"pnl":15273.16},"tainted":{"n":1880,"win":33.35,"med":-39.0,"avg":12.72,"pnl":-9533.28},"keep_only":{"n":617,"win":62.24,"med":50.0,"avg":61.67,"pnl":10191.45},"keep_only_recent":{"n":434,"win":61.06,"med":53.33,"avg":73.99,"pnl":6581.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S356","S357","S361","S362","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S359","S360","S363","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
14:01:16  INFO      Mode: exits
14:01:16  INFO        Daily log -> logs/daily/2026-09-18.md
14:01:16  INFO        Daily log reconciled -> logs/daily/2026-09-18.md (2 ledger rows)
14:01:16  INFO        place_all_stops: checking 1 positions...
14:01:16  INFO        STOP skipped BLDR: fractional (0.5935 shares) — software exit will handle it
14:01:17  INFO        [positions] 1/1 (1 valid)
14:01:17  INFO        SELL MARKET [urgent] BLDR closed
14:01:19  INFO        TX logged: SELL BLDR  P&L -0.75%
14:01:19  INFO        Daily log -> logs/daily/2026-09-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.99|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  BLDR  P&L -0.8%  $-0.26                        EXIT: stop_loss (-0.8%)|
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
|  BLDR                                        -0.75%  (threshold -0.50%)|
|  Count                                                                1|
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-18T10:01:19.997289-04:00 share=25% ===
2026-09-18 10:01:19,997 INFO === options_live_micro LIVE 2026-09-18T10:01:19.997289-04:00 share=25% ===
Live account equity $225.96 cash $225.96 #225458845 options_level=3
2026-09-18 10:01:20,041 INFO Live account equity $225.96 cash $225.96 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-18 10:01:20,063 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-18 10:01:20,078 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (201 earlier lines - see full log file)

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 271 | 17 |
| S164 | 299 | 21 |
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
| 2026-09-18 |    4 |    0 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-18
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1368 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |    99 | INFO |
| Total closed lots           |  2336 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-18_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-18_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1320 med=-33.3% | TAINTED n=1880 med=-39.0% | KEEP-only n=617 med=+50.0% | KILL=22 KEEP=20
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=225.96 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260918T140613Z

- UTC timestamp: `20260918T140613Z`
- GitHub run: [#10384](https://github.com/28twagg-ops/TradingBot/actions/runs/35354044253)
- Run id: `35354044253`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`113s`
- Full logs: `logs/action_runs/20260918T140613Z_live_bot.log`, `logs/action_runs/20260918T140613Z_live_options.log`, `logs/action_runs/20260918T140613Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1321 | 47.6 | -33.3 | +36.2 | $+15,299 |
| TAINTED | 1880 | 33.4 | -39.0 | +12.7 | $-9,533 |
| KEEP-only | 639 | 61.8 | +50.0 | +62.5 | $+10,230 |
| KEEP-only recent | 453 | 60.3 | +53.3 | +74.7 | $+6,560 |

- KEEP strategies (21): S163, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S361, S362, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (21): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S359, S360, S363, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-18T10:06:22.401845-04:00","date":"2026-09-18","mode":"entry+manage","header":"entry+manage (10 new)","elapsed_s":100.6,"phases_s":{"reconcile":0.6,"cancel":0.15,"manage":13.39,"protective_stops":3.19,"scan":55.21,"entries":22.96,"reconcile2":0.96},"signals":89,"placed":10,"equity":996704.47,"open_positions":27,"pending_orders":7,"open_lots":104,"submitted_today":60,"filled_today":53,"unattributed_contracts":0,"top_signals":["S211:META","S165:NFLX","S164:NFLX","S168:NFLX","S167:NFLX","S166:NFLX","S163:NFLX","S202:NFLX"],"github_run":"10384","github_run_id":"35354044253","status":"ok","data_quality":{"clean":{"n":1321,"win":47.62,"med":-33.33,"avg":36.18,"pnl":15299.16},"tainted":{"n":1880,"win":33.35,"med":-39.0,"avg":12.72,"pnl":-9533.28},"keep_only":{"n":639,"win":61.82,"med":50.0,"avg":62.55,"pnl":10230.45},"keep_only_recent":{"n":453,"win":60.26,"med":53.33,"avg":74.69,"pnl":6560.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S361","S362","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S359","S360","S363","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
14:06:15  INFO      Mode: exits
14:06:16  INFO        Daily log -> logs/daily/2026-09-18.md
14:06:16  INFO        Daily log reconciled -> logs/daily/2026-09-18.md (3 ledger rows)
14:06:17  INFO        Daily log -> logs/daily/2026-09-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.96|
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
=== options_live_micro LIVE 2026-09-18T10:06:18.296249-04:00 share=25% ===
2026-09-18 10:06:18,296 INFO === options_live_micro LIVE 2026-09-18T10:06:18.296249-04:00 share=25% ===
Live account equity $225.96 cash $225.96 #225458845 options_level=3
2026-09-18 10:06:18,525 INFO Live account equity $225.96 cash $225.96 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-18 10:06:18,731 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-18 10:06:18,879 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (249 earlier lines - see full log file)

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 271 | 17 |
| S164 | 299 | 21 |
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
| 2026-09-18 |    4 |    0 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-18
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1368 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |   104 | INFO |
| Total closed lots           |  2337 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-18_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-18_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1321 med=-33.3% | TAINTED n=1880 med=-39.0% | KEEP-only n=639 med=+50.0% | KILL=21 KEEP=21
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=225.96 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260918T141110Z

- UTC timestamp: `20260918T141110Z`
- GitHub run: [#10385](https://github.com/28twagg-ops/TradingBot/actions/runs/35354550013)
- Run id: `35354550013`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`74s`
- Full logs: `logs/action_runs/20260918T141110Z_live_bot.log`, `logs/action_runs/20260918T141110Z_live_options.log`, `logs/action_runs/20260918T141110Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1322 | 47.7 | -33.3 | +36.3 | $+15,327 |
| TAINTED | 1880 | 33.4 | -39.0 | +12.7 | $-9,533 |
| KEEP-only | 640 | 61.9 | +50.0 | +62.7 | $+10,258 |
| KEEP-only recent | 454 | 60.4 | +53.3 | +74.9 | $+6,588 |

- KEEP strategies (21): S163, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S361, S362, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (21): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S359, S360, S363, S366, S398, S405, S407, S408, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-18T10:11:17.562093-04:00","date":"2026-09-18","mode":"entry+manage","header":"entry+manage (4 new)","elapsed_s":61.8,"phases_s":{"reconcile":0.22,"cancel":0.05,"manage":8.93,"protective_stops":0.94,"scan":41.73,"entries":7.91,"reconcile2":0.35},"signals":89,"placed":4,"equity":996789.83,"open_positions":28,"pending_orders":9,"open_lots":105,"submitted_today":64,"filled_today":55,"unattributed_contracts":0,"top_signals":["S211:META","S165:NFLX","S164:NFLX","S168:NFLX","S167:NFLX","S166:NFLX","S163:NFLX","S202:NFLX"],"github_run":"10385","github_run_id":"35354550013","status":"ok","data_quality":{"clean":{"n":1322,"win":47.66,"med":-33.33,"avg":36.27,"pnl":15327.16},"tainted":{"n":1880,"win":33.35,"med":-39.0,"avg":12.72,"pnl":-9533.28},"keep_only":{"n":640,"win":61.88,"med":50.0,"avg":62.68,"pnl":10258.45},"keep_only_recent":{"n":454,"win":60.35,"med":53.33,"avg":74.85,"pnl":6588.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S361","S362","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S359","S360","S363","S366","S398","S405","S407","S408","S412"]}}
```

### Live bot (tail)

```text
14:11:12  INFO      Mode: exits
14:11:12  INFO        Daily log -> logs/daily/2026-09-18.md
14:11:12  INFO        Daily log reconciled -> logs/daily/2026-09-18.md (3 ledger rows)
14:11:13  INFO        Daily log -> logs/daily/2026-09-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.96|
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
=== options_live_micro LIVE 2026-09-18T10:11:14.161550-04:00 share=25% ===
2026-09-18 10:11:14,161 INFO === options_live_micro LIVE 2026-09-18T10:11:14.161550-04:00 share=25% ===
Live account equity $225.96 cash $225.96 #225458845 options_level=3
2026-09-18 10:11:14,272 INFO Live account equity $225.96 cash $225.96 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-18 10:11:14,395 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-18 10:11:14,446 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (245 earlier lines - see full log file)

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 271 | 17 |
| S164 | 299 | 21 |
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
| 2026-09-18 |    4 |    0 |    0 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-18
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1368 | WARN | <<<
| Missing exit records (post) |  1365 | WARN | <<<
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |   105 | INFO |
| Total closed lots           |  2338 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-18_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-18_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1322 med=-33.3% | TAINTED n=1880 med=-39.0% | KEEP-only n=640 med=+50.0% | KILL=21 KEEP=21
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=225.96 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---
