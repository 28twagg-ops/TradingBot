# Daily Comprehensive Action Review - 2026-10-01

_Auto-generated from GitHub Actions run output. Each run appends a summary; full stdout is in linked per-run log files._
## Run 20261001T130130Z

- UTC timestamp: `20261001T130130Z`
- GitHub run: [#11559](https://github.com/28twagg-ops/TradingBot/actions/runs/36865589698)
- Run id: `36865589698`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`14s`
- Full logs: `logs/action_runs/20261001T130130Z_live_bot.log`, `logs/action_runs/20261001T130130Z_live_options.log`, `logs/action_runs/20261001T130130Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1601 | 48.2 | -26.7 | +39.0 | $+18,087 |
| TAINTED | 1951 | 33.1 | -40.0 | +12.3 | $-9,974 |
| KEEP-only | 777 | 60.9 | +50.9 | +59.4 | $+11,977 |
| KEEP-only recent | 584 | 59.2 | +53.3 | +67.3 | $+7,916 |

- KEEP strategies (23): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S411, S412
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-01T09:01:36.670267-04:00","date":"2026-10-01","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.5,"phases_s":{"reconcile":0.64},"signals":0,"placed":0,"equity":990677.99,"open_positions":14,"pending_orders":0,"open_lots":34,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11559","github_run_id":"36865589698","status":"ok","data_quality":{"clean":{"n":1601,"win":48.16,"med":-26.67,"avg":39.03,"pnl":18086.83},"tainted":{"n":1951,"win":33.11,"med":-40.0,"avg":12.31,"pnl":-9974.28},"keep_only":{"n":777,"win":60.88,"med":50.85,"avg":59.36,"pnl":11977.45},"keep_only_recent":{"n":584,"win":59.25,"med":53.33,"avg":67.32,"pnl":7916.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:01:31  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $222.99|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $222.99|
|  Cash                                                           $122.56|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $100.43|
|  Open P&L                                                        $+0.20|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (3 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  FCN      MomReversal     $33.50     $133.92  $134.29  +0.3%   $+0.09  |
|  LNT      MomReversal     $33.46     $63.21   $63.30   +0.1%   $+0.05  |
|  PNW      MomReversal     $33.47     $92.88   $93.04   +0.2%   $+0.06  |
|                                                                        |
|  Total invested                                                 $100.43|
|  Total open P&L                                                  $+0.20|
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
|  2026-09-30  SELL  AES  Pullback50  $33.53  P&L $+0.05                 |
|  2026-09-30  SELL  EBAY  Pullback50  $33.33  P&L $-0.17                |
|  2026-09-30  SELL  CMS  MomReversal  $3.42  P&L $-0.02                 |
|  2026-09-30  SELL  GOOG  Pullback50  $33.49  P&L $-0.01                |
|  2026-09-30  SELL  NCLH  EarningsDrift  $33.62  P&L $+0.17             |
|  2026-09-29  SELL  AES  Pullback50  $33.44  P&L $-0.02                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-01T09:01:33.057610-04:00 share=25% ===
2026-10-01 09:01:33,057 INFO === options_live_micro LIVE 2026-10-01T09:01:33.057610-04:00 share=25% ===
Live account equity $222.99 cash $122.56 #225458845 options_level=3
2026-10-01 09:01:33,310 INFO Live account equity $222.99 cash $122.56 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-10-01 09:01:33,383 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-10-01 09:01:33,458 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (174 earlier lines - see full log file)
| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 295 | 21 |
| S164 | 337 | 24 |
| S165 | 1761 | 36 |
| S166 | 141 | 11 |
| S167 | 318 | 23 |
| S168 | 238 | 20 |
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
| 2026-09-24 |   10 |   12 |   12 |    0 |   11 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    55 |
| 2026-09-25 |   12 |   14 |   12 |    0 |   12 |   12 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-28 |    2 |    4 |    2 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    14 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-01
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    21 | WARN | <<<
| Orphaned lots (post-stable) |  1838 | WARN | <<<
| Missing exit records (post) |  1817 | WARN | <<<
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |    34 | INFO |
| Total closed lots           |  2665 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-01_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-01_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1601 med=-26.7% | TAINTED n=1951 med=-40.0% | KEEP-only n=777 med=+50.9% | KILL=21 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=222.99 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261001T130617Z

- UTC timestamp: `20261001T130617Z`
- GitHub run: [#11560](https://github.com/28twagg-ops/TradingBot/actions/runs/36866161043)
- Run id: `36866161043`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`13s`
- Full logs: `logs/action_runs/20261001T130617Z_live_bot.log`, `logs/action_runs/20261001T130617Z_live_options.log`, `logs/action_runs/20261001T130617Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1601 | 48.2 | -26.7 | +39.0 | $+18,087 |
| TAINTED | 1951 | 33.1 | -40.0 | +12.3 | $-9,974 |
| KEEP-only | 777 | 60.9 | +50.9 | +59.4 | $+11,977 |
| KEEP-only recent | 584 | 59.2 | +53.3 | +67.3 | $+7,916 |

- KEEP strategies (23): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S411, S412
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-01T09:06:22.151684-04:00","date":"2026-10-01","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.8,"phases_s":{"reconcile":0.12},"signals":0,"placed":0,"equity":990616.55,"open_positions":14,"pending_orders":0,"open_lots":34,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11560","github_run_id":"36866161043","status":"ok","data_quality":{"clean":{"n":1601,"win":48.16,"med":-26.67,"avg":39.03,"pnl":18086.83},"tainted":{"n":1951,"win":33.11,"med":-40.0,"avg":12.31,"pnl":-9974.28},"keep_only":{"n":777,"win":60.88,"med":50.85,"avg":59.36,"pnl":11977.45},"keep_only_recent":{"n":584,"win":59.25,"med":53.33,"avg":67.32,"pnl":7916.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:06:18  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $222.99|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $222.99|
|  Cash                                                           $122.56|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $100.43|
|  Open P&L                                                        $+0.20|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (3 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  FCN      MomReversal     $33.50     $133.92  $134.29  +0.3%   $+0.09  |
|  LNT      MomReversal     $33.46     $63.21   $63.30   +0.1%   $+0.05  |
|  PNW      MomReversal     $33.47     $92.88   $93.04   +0.2%   $+0.06  |
|                                                                        |
|  Total invested                                                 $100.43|
|  Total open P&L                                                  $+0.20|
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
|  2026-09-30  SELL  AES  Pullback50  $33.53  P&L $+0.05                 |
|  2026-09-30  SELL  EBAY  Pullback50  $33.33  P&L $-0.17                |
|  2026-09-30  SELL  CMS  MomReversal  $3.42  P&L $-0.02                 |
|  2026-09-30  SELL  GOOG  Pullback50  $33.49  P&L $-0.01                |
|  2026-09-30  SELL  NCLH  EarningsDrift  $33.62  P&L $+0.17             |
|  2026-09-29  SELL  AES  Pullback50  $33.44  P&L $-0.02                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-01T09:06:19.528524-04:00 share=25% ===
2026-10-01 09:06:19,528 INFO === options_live_micro LIVE 2026-10-01T09:06:19.528524-04:00 share=25% ===
Live account equity $222.99 cash $122.56 #225458845 options_level=3
2026-10-01 09:06:19,585 INFO Live account equity $222.99 cash $122.56 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-10-01 09:06:19,599 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-10-01 09:06:19,609 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (174 earlier lines - see full log file)
| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 295 | 21 |
| S164 | 337 | 24 |
| S165 | 1761 | 36 |
| S166 | 141 | 11 |
| S167 | 318 | 23 |
| S168 | 238 | 20 |
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
| 2026-09-24 |   10 |   12 |   12 |    0 |   11 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    55 |
| 2026-09-25 |   12 |   14 |   12 |    0 |   12 |   12 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-28 |    2 |    4 |    2 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    14 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-01
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    21 | WARN | <<<
| Orphaned lots (post-stable) |  1838 | WARN | <<<
| Missing exit records (post) |  1817 | WARN | <<<
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |    34 | INFO |
| Total closed lots           |  2665 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-01_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-01_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1601 med=-26.7% | TAINTED n=1951 med=-40.0% | KEEP-only n=777 med=+50.9% | KILL=21 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=222.99 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261001T131120Z

- UTC timestamp: `20261001T131120Z`
- GitHub run: [#11561](https://github.com/28twagg-ops/TradingBot/actions/runs/36866701939)
- Run id: `36866701939`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`13s`
- Full logs: `logs/action_runs/20261001T131120Z_live_bot.log`, `logs/action_runs/20261001T131120Z_live_options.log`, `logs/action_runs/20261001T131120Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1601 | 48.2 | -26.7 | +39.0 | $+18,087 |
| TAINTED | 1951 | 33.1 | -40.0 | +12.3 | $-9,974 |
| KEEP-only | 777 | 60.9 | +50.9 | +59.4 | $+11,977 |
| KEEP-only recent | 584 | 59.2 | +53.3 | +67.3 | $+7,916 |

- KEEP strategies (23): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S411, S412
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-01T09:11:26.231612-04:00","date":"2026-10-01","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.22},"signals":0,"placed":0,"equity":990479.33,"open_positions":14,"pending_orders":0,"open_lots":34,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11561","github_run_id":"36866701939","status":"ok","data_quality":{"clean":{"n":1601,"win":48.16,"med":-26.67,"avg":39.03,"pnl":18086.83},"tainted":{"n":1951,"win":33.11,"med":-40.0,"avg":12.31,"pnl":-9974.28},"keep_only":{"n":777,"win":60.88,"med":50.85,"avg":59.36,"pnl":11977.45},"keep_only_recent":{"n":584,"win":59.25,"med":53.33,"avg":67.32,"pnl":7916.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:11:21  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $222.99|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $222.99|
|  Cash                                                           $122.56|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $100.43|
|  Open P&L                                                        $+0.20|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (3 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  FCN      MomReversal     $33.50     $133.92  $134.29  +0.3%   $+0.09  |
|  LNT      MomReversal     $33.46     $63.21   $63.30   +0.1%   $+0.05  |
|  PNW      MomReversal     $33.47     $92.88   $93.04   +0.2%   $+0.06  |
|                                                                        |
|  Total invested                                                 $100.43|
|  Total open P&L                                                  $+0.20|
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
|  2026-09-30  SELL  AES  Pullback50  $33.53  P&L $+0.05                 |
|  2026-09-30  SELL  EBAY  Pullback50  $33.33  P&L $-0.17                |
|  2026-09-30  SELL  CMS  MomReversal  $3.42  P&L $-0.02                 |
|  2026-09-30  SELL  GOOG  Pullback50  $33.49  P&L $-0.01                |
|  2026-09-30  SELL  NCLH  EarningsDrift  $33.62  P&L $+0.17             |
|  2026-09-29  SELL  AES  Pullback50  $33.44  P&L $-0.02                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-01T09:11:22.996141-04:00 share=25% ===
2026-10-01 09:11:22,996 INFO === options_live_micro LIVE 2026-10-01T09:11:22.996141-04:00 share=25% ===
Live account equity $222.99 cash $122.56 #225458845 options_level=3
2026-10-01 09:11:23,082 INFO Live account equity $222.99 cash $122.56 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-10-01 09:11:23,161 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-10-01 09:11:23,183 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (174 earlier lines - see full log file)
| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 295 | 21 |
| S164 | 337 | 24 |
| S165 | 1761 | 36 |
| S166 | 141 | 11 |
| S167 | 318 | 23 |
| S168 | 238 | 20 |
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
| 2026-09-24 |   10 |   12 |   12 |    0 |   11 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    55 |
| 2026-09-25 |   12 |   14 |   12 |    0 |   12 |   12 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-28 |    2 |    4 |    2 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    14 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-01
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    21 | WARN | <<<
| Orphaned lots (post-stable) |  1838 | WARN | <<<
| Missing exit records (post) |  1817 | WARN | <<<
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |    34 | INFO |
| Total closed lots           |  2665 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-01_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-01_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1601 med=-26.7% | TAINTED n=1951 med=-40.0% | KEEP-only n=777 med=+50.9% | KILL=21 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=222.99 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261001T131617Z

- UTC timestamp: `20261001T131617Z`
- GitHub run: [#11562](https://github.com/28twagg-ops/TradingBot/actions/runs/36867311135)
- Run id: `36867311135`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`12s`
- Full logs: `logs/action_runs/20261001T131617Z_live_bot.log`, `logs/action_runs/20261001T131617Z_live_options.log`, `logs/action_runs/20261001T131617Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1601 | 48.2 | -26.7 | +39.0 | $+18,087 |
| TAINTED | 1951 | 33.1 | -40.0 | +12.3 | $-9,974 |
| KEEP-only | 777 | 60.9 | +50.9 | +59.4 | $+11,977 |
| KEEP-only recent | 584 | 59.2 | +53.3 | +67.3 | $+7,916 |

- KEEP strategies (23): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S411, S412
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-01T09:16:22.476970-04:00","date":"2026-10-01","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.09},"signals":0,"placed":0,"equity":990364.29,"open_positions":14,"pending_orders":0,"open_lots":34,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11562","github_run_id":"36867311135","status":"ok","data_quality":{"clean":{"n":1601,"win":48.16,"med":-26.67,"avg":39.03,"pnl":18086.83},"tainted":{"n":1951,"win":33.11,"med":-40.0,"avg":12.31,"pnl":-9974.28},"keep_only":{"n":777,"win":60.88,"med":50.85,"avg":59.36,"pnl":11977.45},"keep_only_recent":{"n":584,"win":59.25,"med":53.33,"avg":67.32,"pnl":7916.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
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
|  Equity                                                         $222.99|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $222.99|
|  Cash                                                           $122.56|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $100.43|
|  Open P&L                                                        $+0.20|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (3 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  FCN      MomReversal     $33.50     $133.92  $134.29  +0.3%   $+0.09  |
|  LNT      MomReversal     $33.46     $63.21   $63.30   +0.1%   $+0.05  |
|  PNW      MomReversal     $33.47     $92.88   $93.04   +0.2%   $+0.06  |
|                                                                        |
|  Total invested                                                 $100.43|
|  Total open P&L                                                  $+0.20|
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
|  2026-09-30  SELL  AES  Pullback50  $33.53  P&L $+0.05                 |
|  2026-09-30  SELL  EBAY  Pullback50  $33.33  P&L $-0.17                |
|  2026-09-30  SELL  CMS  MomReversal  $3.42  P&L $-0.02                 |
|  2026-09-30  SELL  GOOG  Pullback50  $33.49  P&L $-0.01                |
|  2026-09-30  SELL  NCLH  EarningsDrift  $33.62  P&L $+0.17             |
|  2026-09-29  SELL  AES  Pullback50  $33.44  P&L $-0.02                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-01T09:16:19.855673-04:00 share=25% ===
2026-10-01 09:16:19,855 INFO === options_live_micro LIVE 2026-10-01T09:16:19.855673-04:00 share=25% ===
Live account equity $222.99 cash $122.56 #225458845 options_level=3
2026-10-01 09:16:19,895 INFO Live account equity $222.99 cash $122.56 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-10-01 09:16:19,921 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-10-01 09:16:19,928 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (174 earlier lines - see full log file)
| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 295 | 21 |
| S164 | 337 | 24 |
| S165 | 1761 | 36 |
| S166 | 141 | 11 |
| S167 | 318 | 23 |
| S168 | 238 | 20 |
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
| 2026-09-24 |   10 |   12 |   12 |    0 |   11 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    55 |
| 2026-09-25 |   12 |   14 |   12 |    0 |   12 |   12 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-28 |    2 |    4 |    2 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    14 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-01
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    21 | WARN | <<<
| Orphaned lots (post-stable) |  1838 | WARN | <<<
| Missing exit records (post) |  1817 | WARN | <<<
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |    34 | INFO |
| Total closed lots           |  2665 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-01_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-01_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1601 med=-26.7% | TAINTED n=1951 med=-40.0% | KEEP-only n=777 med=+50.9% | KILL=21 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=222.99 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261001T132119Z

- UTC timestamp: `20261001T132119Z`
- GitHub run: [#11563](https://github.com/28twagg-ops/TradingBot/actions/runs/36867911588)
- Run id: `36867911588`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`9s`
- Full logs: `logs/action_runs/20261001T132119Z_live_bot.log`, `logs/action_runs/20261001T132119Z_live_options.log`, `logs/action_runs/20261001T132119Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1601 | 48.2 | -26.7 | +39.0 | $+18,087 |
| TAINTED | 1951 | 33.1 | -40.0 | +12.3 | $-9,974 |
| KEEP-only | 777 | 60.9 | +50.9 | +59.4 | $+11,977 |
| KEEP-only recent | 584 | 59.2 | +53.3 | +67.3 | $+7,916 |

- KEEP strategies (23): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S411, S412
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-01T09:21:25.669788-04:00","date":"2026-10-01","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.32},"signals":0,"placed":0,"equity":990446.98,"open_positions":14,"pending_orders":0,"open_lots":34,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11563","github_run_id":"36867911588","status":"ok","data_quality":{"clean":{"n":1601,"win":48.16,"med":-26.67,"avg":39.03,"pnl":18086.83},"tainted":{"n":1951,"win":33.11,"med":-40.0,"avg":12.31,"pnl":-9974.28},"keep_only":{"n":777,"win":60.88,"med":50.85,"avg":59.36,"pnl":11977.45},"keep_only_recent":{"n":584,"win":59.25,"med":53.33,"avg":67.32,"pnl":7916.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:21:21  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $222.99|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $222.99|
|  Cash                                                           $122.56|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $100.43|
|  Open P&L                                                        $+0.20|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (3 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  FCN      MomReversal     $33.50     $133.92  $134.29  +0.3%   $+0.09  |
|  LNT      MomReversal     $33.46     $63.21   $63.30   +0.1%   $+0.05  |
|  PNW      MomReversal     $33.47     $92.88   $93.04   +0.2%   $+0.06  |
|                                                                        |
|  Total invested                                                 $100.43|
|  Total open P&L                                                  $+0.20|
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
|  2026-09-30  SELL  AES  Pullback50  $33.53  P&L $+0.05                 |
|  2026-09-30  SELL  EBAY  Pullback50  $33.33  P&L $-0.17                |
|  2026-09-30  SELL  CMS  MomReversal  $3.42  P&L $-0.02                 |
|  2026-09-30  SELL  GOOG  Pullback50  $33.49  P&L $-0.01                |
|  2026-09-30  SELL  NCLH  EarningsDrift  $33.62  P&L $+0.17             |
|  2026-09-29  SELL  AES  Pullback50  $33.44  P&L $-0.02                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-01T09:21:22.663963-04:00 share=25% ===
2026-10-01 09:21:22,664 INFO === options_live_micro LIVE 2026-10-01T09:21:22.663963-04:00 share=25% ===
Live account equity $222.99 cash $122.56 #225458845 options_level=3
2026-10-01 09:21:22,826 INFO Live account equity $222.99 cash $122.56 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-10-01 09:21:22,906 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-10-01 09:21:22,948 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (174 earlier lines - see full log file)
| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 295 | 21 |
| S164 | 337 | 24 |
| S165 | 1761 | 36 |
| S166 | 141 | 11 |
| S167 | 318 | 23 |
| S168 | 238 | 20 |
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
| 2026-09-24 |   10 |   12 |   12 |    0 |   11 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    55 |
| 2026-09-25 |   12 |   14 |   12 |    0 |   12 |   12 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-28 |    2 |    4 |    2 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    14 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-01
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    21 | WARN | <<<
| Orphaned lots (post-stable) |  1838 | WARN | <<<
| Missing exit records (post) |  1817 | WARN | <<<
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |    34 | INFO |
| Total closed lots           |  2665 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-01_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-01_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1601 med=-26.7% | TAINTED n=1951 med=-40.0% | KEEP-only n=777 med=+50.9% | KILL=21 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=222.99 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261001T132635Z

- UTC timestamp: `20261001T132635Z`
- GitHub run: [#11564](https://github.com/28twagg-ops/TradingBot/actions/runs/36868512569)
- Run id: `36868512569`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`8s`
- Full logs: `logs/action_runs/20261001T132635Z_live_bot.log`, `logs/action_runs/20261001T132635Z_live_options.log`, `logs/action_runs/20261001T132635Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1601 | 48.2 | -26.7 | +39.0 | $+18,087 |
| TAINTED | 1951 | 33.1 | -40.0 | +12.3 | $-9,974 |
| KEEP-only | 777 | 60.9 | +50.9 | +59.4 | $+11,977 |
| KEEP-only recent | 584 | 59.2 | +53.3 | +67.3 | $+7,916 |

- KEEP strategies (23): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S411, S412
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-01T09:26:40.205514-04:00","date":"2026-10-01","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.34},"signals":0,"placed":0,"equity":990485.59,"open_positions":14,"pending_orders":0,"open_lots":34,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11564","github_run_id":"36868512569","status":"ok","data_quality":{"clean":{"n":1601,"win":48.16,"med":-26.67,"avg":39.03,"pnl":18086.83},"tainted":{"n":1951,"win":33.11,"med":-40.0,"avg":12.31,"pnl":-9974.28},"keep_only":{"n":777,"win":60.88,"med":50.85,"avg":59.36,"pnl":11977.45},"keep_only_recent":{"n":584,"win":59.25,"med":53.33,"avg":67.32,"pnl":7916.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:26:37  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $222.99|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $222.99|
|  Cash                                                           $122.56|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $100.43|
|  Open P&L                                                        $+0.20|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (3 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  FCN      MomReversal     $33.50     $133.92  $134.29  +0.3%   $+0.09  |
|  LNT      MomReversal     $33.46     $63.21   $63.30   +0.1%   $+0.05  |
|  PNW      MomReversal     $33.47     $92.88   $93.04   +0.2%   $+0.06  |
|                                                                        |
|  Total invested                                                 $100.43|
|  Total open P&L                                                  $+0.20|
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
|  2026-09-30  SELL  AES  Pullback50  $33.53  P&L $+0.05                 |
|  2026-09-30  SELL  EBAY  Pullback50  $33.33  P&L $-0.17                |
|  2026-09-30  SELL  CMS  MomReversal  $3.42  P&L $-0.02                 |
|  2026-09-30  SELL  GOOG  Pullback50  $33.49  P&L $-0.01                |
|  2026-09-30  SELL  NCLH  EarningsDrift  $33.62  P&L $+0.17             |
|  2026-09-29  SELL  AES  Pullback50  $33.44  P&L $-0.02                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-01T09:26:38.080080-04:00 share=25% ===
2026-10-01 09:26:38,080 INFO === options_live_micro LIVE 2026-10-01T09:26:38.080080-04:00 share=25% ===
Live account equity $222.99 cash $122.56 #225458845 options_level=3
2026-10-01 09:26:38,235 INFO Live account equity $222.99 cash $122.56 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-10-01 09:26:38,269 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-10-01 09:26:38,303 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (174 earlier lines - see full log file)
| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 295 | 21 |
| S164 | 337 | 24 |
| S165 | 1761 | 36 |
| S166 | 141 | 11 |
| S167 | 318 | 23 |
| S168 | 238 | 20 |
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
| 2026-09-24 |   10 |   12 |   12 |    0 |   11 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    55 |
| 2026-09-25 |   12 |   14 |   12 |    0 |   12 |   12 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-28 |    2 |    4 |    2 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    14 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-01
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    21 | WARN | <<<
| Orphaned lots (post-stable) |  1838 | WARN | <<<
| Missing exit records (post) |  1817 | WARN | <<<
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |    34 | INFO |
| Total closed lots           |  2665 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-01_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-01_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1601 med=-26.7% | TAINTED n=1951 med=-40.0% | KEEP-only n=777 med=+50.9% | KILL=21 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=222.99 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261001T133128Z

- UTC timestamp: `20261001T133128Z`
- GitHub run: [#11565](https://github.com/28twagg-ops/TradingBot/actions/runs/36869115642)
- Run id: `36869115642`
- Live bot: exit=`0`, duration=`218s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20261001T133128Z_live_bot.log`, `logs/action_runs/20261001T133128Z_live_options.log`, `logs/action_runs/20261001T133128Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1601 | 48.2 | -26.7 | +39.0 | $+18,087 |
| TAINTED | 1951 | 33.1 | -40.0 | +12.3 | $-9,974 |
| KEEP-only | 777 | 60.9 | +50.9 | +59.4 | $+11,977 |
| KEEP-only recent | 584 | 59.2 | +53.3 | +67.3 | $+7,916 |

- KEEP strategies (23): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S411, S412
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-01T09:26:40.205514-04:00","date":"2026-10-01","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.34},"signals":0,"placed":0,"equity":990485.59,"open_positions":14,"pending_orders":0,"open_lots":34,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11564","github_run_id":"36868512569","status":"ok","data_quality":{"clean":{"n":1601,"win":48.16,"med":-26.67,"avg":39.03,"pnl":18086.83},"tainted":{"n":1951,"win":33.11,"med":-40.0,"avg":12.31,"pnl":-9974.28},"keep_only":{"n":777,"win":60.88,"med":50.85,"avg":59.36,"pnl":11977.45},"keep_only_recent":{"n":584,"win":59.25,"med":53.33,"avg":67.32,"pnl":7916.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:31:29  INFO      Mode: morning_prep
13:31:30  INFO        [prep_positions] 3/3 (3 valid)
13:31:30  INFO      Fetching tickers (universe=both)...
13:31:30  INFO        S&P 500: 503
13:31:31  INFO        MidCap 400: 400
13:31:31  INFO        Total: 903 tickers
13:31:33  INFO        [prep_universe] 40/900 (40 valid)
13:31:35  INFO        [prep_universe] 80/900 (80 valid)
13:31:36  INFO        [prep_universe] 120/900 (120 valid)
13:31:37  INFO        [prep_universe] 160/900 (160 valid)
13:31:39  INFO        [prep_universe] 200/900 (199 valid)
13:31:46  INFO        [prep_universe] 240/900 (238 valid)
13:31:57  INFO        [prep_universe] 280/900 (278 valid)
13:32:10  INFO        [prep_universe] 320/900 (318 valid)
13:32:20  INFO        [prep_universe] 360/900 (358 valid)
13:32:34  INFO        [prep_universe] 400/900 (398 valid)
13:32:44  INFO        [prep_universe] 440/900 (438 valid)
13:32:57  INFO        [prep_universe] 480/900 (478 valid)
13:33:10  INFO        [prep_universe] 520/900 (518 valid)
13:33:20  INFO        [prep_universe] 560/900 (558 valid)
13:33:33  INFO        [prep_universe] 600/900 (598 valid)
13:33:44  INFO        [prep_universe] 640/900 (638 valid)
13:33:57  INFO        [prep_universe] 680/900 (678 valid)
13:34:11  INFO        [prep_universe] 720/900 (718 valid)
13:34:21  INFO        [prep_universe] 760/900 (758 valid)
13:34:34  INFO        [prep_universe] 800/900 (798 valid)
13:34:44  INFO        [prep_universe] 840/900 (838 valid)
13:34:57  INFO        [prep_universe] 880/900 (878 valid)
13:35:04  INFO        [prep_universe] 900/900 (898 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.61|
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
|  Invested                                                       $101.05|
|  Open P&L                                                        $+0.82|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  FCN      MomReversal     $34.43     $133.92  $138.00  +3.0%   $+1.02  |
|  LNT      MomReversal     $33.34     $63.21   $63.08   -0.2%   $-0.07  |
|  PNW      MomReversal     $33.28     $92.88   $92.51   -0.4%   $-0.13  |
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
|  Signal candidates                                                   23|
|  Universe scanned                                                   900|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-01T09:35:07.049955-04:00 share=25% ===
2026-10-01 09:35:07,050 INFO === options_live_micro LIVE 2026-10-01T09:35:07.049955-04:00 share=25% ===
Live account equity $223.92 cash $122.56 #225458845 options_level=3
2026-10-01 09:35:07,238 INFO Live account equity $223.92 cash $122.56 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-10-01 09:35:07,417 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-10-01 09:35:07,534 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=34 paper_keys=yes dry_run=False
  alpaca positions=19
  No missing lots.
options_reconcile: done
Layout: controlled:77:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:77:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      77
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$991,083.45
  buying_power=$3,837,511.80 cash=$973,606.95
  open option orders: 6
    OXY261016C00058000 OrderSide.SELL qty=2 status=OrderStatus.NEW limit=None
    OXY261023C00060000 OrderSide.SELL qty=2 status=OrderStatus.NEW limit=None
    CVX261016C00220000 OrderSide.SELL qty=2 status=OrderStatus.NEW limit=None
    NKE261002C00040000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
    NKE261002C00038500 OrderSide.SELL qty=6 status=OrderStatus.NEW limit=None
  open option positions: 15
    CVNA261002C00066000 qty=-1 mkt=$-23.00
    CVNA261002C00068000 qty=-1 mkt=$-75.00
    CVNA261002C00069000 qty=2 mkt=$2.00
    CVX261002C00210000 qty=-1 mkt=$-14.00
    CVX261002C00220000 qty=1 mkt=$0.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-10-01T09:35:10.289375-04:00 ===

[Run context]
Paper auth OK — equity $991072.98, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
S406-only twin b91 s406_only — S406 | TP+50%/SL-40% | paper edge test
Variation study: 75 lab/promising bucket(s) | cohort: 75 unique (S163, S164, S166, S167, S168, S169, S170, S171, S172, S175, S200, S201 … +63 more) | max 200 new entries/run
Dropped (no new entries; ex-reflected P&L): S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
Shared-OCC entry block ON (one lab lot per contract)
2026-10-01 09:35:12,333 INFO   EXIT [b433|lab0433_s366_w1_0928_1005_r2|S366] stop_loss (-67.9%) SELL 1 OXY261023C00060000 @<= 0.14
2026-10-01 09:35:13,030 INFO   EXIT [b419|lab0419_s365_w1_0928_1005_r2|S365] stop_loss (-51.4%) SELL 1 CVX261016C00220000 @<= 0.32
  EXIT [b171|lab0171_s216_w4_1120_1135_r2|S216] stop_loss (-96.6%) SELL blocked (uncovered/shared OCC) CVNA261002C00069000 x1: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b170|lab0170_s216_w4_1120_1135_r1|S216] stop_loss (-96.6%) SELL blocked (uncovered/shared OCC) CVNA261002C00069000 x1: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
2026-10-01 09:35:14,565 INFO   EXIT [b434|lab0434_s366_w2_1005_1045_r1|S366] stop_loss (-50.7%) SELL 1 OXY261023C00059000 @<= 0.33
  EXIT [b421|lab0421_s365_w2_1005_1045_r2|S365] stop_loss (-90.7%) SELL blocked (uncovered/shared OCC) DKNG261016C00023500 x1: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
2026-10-01 09:35:15,429 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-100.0%) SELL 1 CVX261002C00220000 @<= 0.01
2026-10-01 09:35:16,329 INFO   EXIT [b0|orphan_reconcile|ORPHAN] take_profit (+104.2%) SELL 1 MSFT261002C00530000 @<= 1.43
Protective stops: placed=0 upgraded=0 already=4 failed=6 (market-first)

[Scan + entries]
Scanning 117 symbols for [S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S204, S205, S206, S208, S210, S213, S214, S215, S219, S220, S221, S402, S403, S350, S352, S356, S357, S358, S359, S361, S362, S364, S365, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S395, S396, S397, S398, S404, S406, S409, S410, S411, S412, S413, S414, S415] …
```

---

## Run 20261001T134247Z

- UTC timestamp: `20261001T134247Z`
- GitHub run: [#11567](https://github.com/28twagg-ops/TradingBot/actions/runs/36870366581)
- Run id: `36870366581`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20261001T134247Z_live_bot.log`, `logs/action_runs/20261001T134247Z_live_options.log`, `logs/action_runs/20261001T134247Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1601 | 48.2 | -26.7 | +39.0 | $+18,087 |
| TAINTED | 1951 | 33.1 | -40.0 | +12.3 | $-9,974 |
| KEEP-only | 777 | 60.9 | +50.9 | +59.4 | $+11,977 |
| KEEP-only recent | 584 | 59.2 | +53.3 | +67.3 | $+7,916 |

- KEEP strategies (23): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S411, S412
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-01T09:26:40.205514-04:00","date":"2026-10-01","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.34},"signals":0,"placed":0,"equity":990485.59,"open_positions":14,"pending_orders":0,"open_lots":34,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11564","github_run_id":"36868512569","status":"ok","data_quality":{"clean":{"n":1601,"win":48.16,"med":-26.67,"avg":39.03,"pnl":18086.83},"tainted":{"n":1951,"win":33.11,"med":-40.0,"avg":12.31,"pnl":-9974.28},"keep_only":{"n":777,"win":60.88,"med":50.85,"avg":59.36,"pnl":11977.45},"keep_only_recent":{"n":584,"win":59.25,"med":53.33,"avg":67.32,"pnl":7916.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:42:48  INFO      Mode: morning_prep
13:42:48  INFO        [prep_positions] 3/3 (3 valid)
13:42:48  INFO        Universe cache hit: 903 tickers (tickers_2026-10-01.json)
13:42:49  INFO        [prep_universe] 40/900 (40 valid)
13:42:51  INFO        [prep_universe] 80/900 (80 valid)
13:42:52  INFO        [prep_universe] 120/900 (120 valid)
13:42:53  INFO        [prep_universe] 160/900 (160 valid)
13:42:54  INFO        [prep_universe] 200/900 (199 valid)
13:43:02  INFO        [prep_universe] 240/900 (238 valid)
13:43:15  INFO        [prep_universe] 280/900 (278 valid)
13:43:28  INFO        [prep_universe] 320/900 (318 valid)
13:43:38  INFO        [prep_universe] 360/900 (358 valid)
13:43:51  INFO        [prep_universe] 400/900 (398 valid)
13:44:04  INFO        [prep_universe] 440/900 (438 valid)
13:44:14  INFO        [prep_universe] 480/900 (478 valid)
13:44:27  INFO        [prep_universe] 520/900 (518 valid)
13:44:40  INFO        [prep_universe] 560/900 (558 valid)
13:44:50  INFO        [prep_universe] 600/900 (598 valid)
13:45:03  INFO        [prep_universe] 640/900 (638 valid)
13:45:13  INFO        [prep_universe] 680/900 (678 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20261001T135247Z

- UTC timestamp: `20261001T135247Z`
- GitHub run: [#11569](https://github.com/28twagg-ops/TradingBot/actions/runs/36871636130)
- Run id: `36871636130`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20261001T135247Z_live_bot.log`, `logs/action_runs/20261001T135247Z_live_options.log`, `logs/action_runs/20261001T135247Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1601 | 48.2 | -26.7 | +39.0 | $+18,087 |
| TAINTED | 1951 | 33.1 | -40.0 | +12.3 | $-9,974 |
| KEEP-only | 777 | 60.9 | +50.9 | +59.4 | $+11,977 |
| KEEP-only recent | 584 | 59.2 | +53.3 | +67.3 | $+7,916 |

- KEEP strategies (23): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S411, S412
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-01T09:26:40.205514-04:00","date":"2026-10-01","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.34},"signals":0,"placed":0,"equity":990485.59,"open_positions":14,"pending_orders":0,"open_lots":34,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11564","github_run_id":"36868512569","status":"ok","data_quality":{"clean":{"n":1601,"win":48.16,"med":-26.67,"avg":39.03,"pnl":18086.83},"tainted":{"n":1951,"win":33.11,"med":-40.0,"avg":12.31,"pnl":-9974.28},"keep_only":{"n":777,"win":60.88,"med":50.85,"avg":59.36,"pnl":11977.45},"keep_only_recent":{"n":584,"win":59.25,"med":53.33,"avg":67.32,"pnl":7916.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:52:49  INFO      Mode: morning_scan
13:52:49  INFO        [positions] 1/1 (1 valid)
13:52:49  INFO        Universe cache hit: 903 tickers (tickers_2026-10-01.json)
13:52:50  INFO        [universe] 40/902 (40 valid)
13:52:51  INFO        [universe] 80/902 (80 valid)
13:52:52  INFO        [universe] 120/902 (120 valid)
13:52:53  INFO        [universe] 160/902 (160 valid)
13:52:54  INFO        [universe] 200/902 (199 valid)
13:53:04  INFO        [universe] 240/902 (238 valid)
13:53:14  INFO        [universe] 280/902 (278 valid)
13:53:27  INFO        [universe] 320/902 (318 valid)
13:53:40  INFO        [universe] 360/902 (358 valid)
13:53:50  INFO        [universe] 400/902 (398 valid)
13:54:03  INFO        [universe] 440/902 (438 valid)
13:54:16  INFO        [universe] 480/902 (478 valid)
13:54:26  INFO        [universe] 520/902 (518 valid)
13:54:39  INFO        [universe] 560/902 (558 valid)
13:54:51  INFO        [universe] 600/902 (598 valid)
13:55:04  INFO        [universe] 640/902 (638 valid)
13:55:14  INFO        [universe] 680/902 (678 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20261001T135655Z

- UTC timestamp: `20261001T135655Z`
- GitHub run: [#11570](https://github.com/28twagg-ops/TradingBot/actions/runs/36872266598)
- Run id: `36872266598`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20261001T135655Z_live_bot.log`, `logs/action_runs/20261001T135655Z_live_options.log`, `logs/action_runs/20261001T135655Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1601 | 48.2 | -26.7 | +39.0 | $+18,087 |
| TAINTED | 1951 | 33.1 | -40.0 | +12.3 | $-9,974 |
| KEEP-only | 777 | 60.9 | +50.9 | +59.4 | $+11,977 |
| KEEP-only recent | 584 | 59.2 | +53.3 | +67.3 | $+7,916 |

- KEEP strategies (23): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S411, S412
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-01T09:26:40.205514-04:00","date":"2026-10-01","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.34},"signals":0,"placed":0,"equity":990485.59,"open_positions":14,"pending_orders":0,"open_lots":34,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11564","github_run_id":"36868512569","status":"ok","data_quality":{"clean":{"n":1601,"win":48.16,"med":-26.67,"avg":39.03,"pnl":18086.83},"tainted":{"n":1951,"win":33.11,"med":-40.0,"avg":12.31,"pnl":-9974.28},"keep_only":{"n":777,"win":60.88,"med":50.85,"avg":59.36,"pnl":11977.45},"keep_only_recent":{"n":584,"win":59.25,"med":53.33,"avg":67.32,"pnl":7916.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
... (130 earlier lines - see full log file)
|  SOLV     Pullback50      eq     $87.83   51.9   -1.90   50MA bounce (-|
|  APPF     Pullback50      eq     $204.17  46.6   -2.06   50MA bounce (-|
|  COKE     Pullback50      eq     $190.20  46.6   -1.23   50MA bounce (-|
|  LFUS     Pullback50      eq     $425.12  45.5   -1.80   50MA bounce (+|
|  MANH     Pullback50      eq     $203.45  52.0   -2.07   50MA bounce (+|
|  PCTY     Pullback50      eq     $146.82  62.3   -2.88   50MA bounce (+|
|  RGA      Pullback50      eq     $246.66  45.3   -2.03   50MA bounce (+|
|  ROIV     Pullback50      eq     $36.42   23.4   -1.20   50MA bounce (-|
|  SNX      Pullback50      eq     $259.14  43.9   -1.14   50MA bounce (+|
|                                                                        |
+========================================================================+

+========================================================================+
|                              ENTRY ORDERS                              |
+========================================================================+
|    ENTER [eq] AES  Pullback50                                    $33.45|
14:00:34  INFO        BUY  AES  $33.45  [Pullback50]  id=3a1f0633-07ed-45ab-9238-1ac091c24e1f
14:00:34  INFO        BUY  BBY  $33.45  [Pullback50]  id=77ce24c9-818b-477a-9374-ec5801993aae
14:00:56  INFO        place_all_stops: checking 3 positions...
14:00:56  INFO        STOP-MARKET placed AES  qty=2 (pos=2.2417)  stop=$14.84  id=3a6171a0-7520-4db8-84f9-9c4fd0dd80bf
14:00:56  INFO        STOP skipped BBY: fractional (0.3827 shares) — software exit will handle it
14:00:56  INFO        STOP skipped FCN: fractional (0.2495 shares) — software exit will handle it
14:00:56  INFO        Daily log -> logs/daily/2026-10-01.md
14:00:57  INFO        Dashboard written → logs/dashboard.md
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    ENTER [eq] BBY  Pullback50                                    $33.45|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    SKIP [eq] CAH  Pullback50                                      cap 3|
|    SKIP [eq] COHR  Pullback50                                     cap 3|
|    SKIP [eq] DVN  Pullback50                                      cap 3|
|    SKIP [eq] FDS  Pullback50                                      cap 3|
|    SKIP [eq] FAST  Pullback50                                     cap 3|
|    SKIP [eq] GRMN  Pullback50                                     cap 3|
|    SKIP [eq] GEV  Pullback50                                      cap 3|
|    SKIP [eq] IEX  Pullback50                                      cap 3|
|    SKIP [eq] HUM  Pullback50                                      cap 3|
|    SKIP [eq] KDP  Pullback50                                      cap 3|
|    SKIP [eq] PWR  Pullback50                                      cap 3|
|    SKIP [eq] ROK  Pullback50                                      cap 3|
|    SKIP [eq] SOLV  Pullback50                                     cap 3|
|    SKIP [eq] APPF  Pullback50                                     cap 3|
|    SKIP [eq] COKE  Pullback50                                     cap 3|
|    SKIP [eq] LFUS  Pullback50                                     cap 3|
|    SKIP [eq] MANH  Pullback50                                     cap 3|
|    SKIP [eq] PCTY  Pullback50                                     cap 3|
|    SKIP [eq] RGA  Pullback50                                      cap 3|
|    SKIP [eq] ROIV  Pullback50                                     cap 3|
|    SKIP [eq] SNX  Pullback50                                      cap 3|

+========================================================================+
|                         BUY FILL CONFIRMATION                          |
+========================================================================+
|  Pending submits                                                      2|
+------------------------------------------------------------------------+
|  AES                                                  still unconfirmed|
|  BBY                                                  still unconfirmed|
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
|  Strategy   RubberBand + GapDown (display only — schedule not enforced)|
|  Scanned                                                            900|
|  Signals                                                             23|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  2 unconfirmed|
|  Exits                                                                0|
|  Open pos                                                             3|
|  Equity                                                         $223.09|
|  Cash                                                           $121.77|
+========================================================================+
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20261001T140231Z

- UTC timestamp: `20261001T140231Z`
- GitHub run: [#11571](https://github.com/28twagg-ops/TradingBot/actions/runs/36872910192)
- Run id: `36872910192`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`75s`
- Full logs: `logs/action_runs/20261001T140231Z_live_bot.log`, `logs/action_runs/20261001T140231Z_live_options.log`, `logs/action_runs/20261001T140231Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1605 | 48.1 | -28.6 | +38.9 | $+18,052 |
| TAINTED | 1952 | 33.1 | -40.0 | +12.3 | $-9,981 |
| KEEP-only | 778 | 60.8 | +50.8 | +59.2 | $+11,940 |
| KEEP-only recent | 585 | 59.1 | +53.3 | +67.1 | $+7,879 |

- KEEP strategies (23): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S411, S412
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-01T10:02:36.790682-04:00","date":"2026-10-01","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":62.3,"phases_s":{"reconcile":0.16,"cancel":0.03,"manage":1.97,"protective_stops":0.3,"scan":59.24,"entries":0.03},"signals":4,"placed":0,"equity":990995.87,"open_positions":13,"pending_orders":0,"open_lots":29,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":["S403:XOM","S403:CVX","S403:ABBV","S210:COST"],"github_run":"11571","github_run_id":"36872910192","status":"ok","data_quality":{"clean":{"n":1605,"win":48.1,"med":-28.57,"avg":38.9,"pnl":18051.83},"tainted":{"n":1952,"win":33.09,"med":-40.0,"avg":12.28,"pnl":-9981.28},"keep_only":{"n":778,"win":60.8,"med":50.79,"avg":59.22,"pnl":11940.45},"keep_only_recent":{"n":585,"win":59.15,"med":53.33,"avg":67.11,"pnl":7879.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:02:32  INFO      Mode: exits
14:02:32  INFO        place_all_stops: checking 3 positions...
14:02:32  INFO        STOP already live AES @ $14.84
14:02:32  INFO        STOP skipped BBY: fractional (0.3827 shares) — software exit will handle it
14:02:32  INFO        STOP skipped FCN: fractional (0.2495 shares) — software exit will handle it
14:02:32  INFO        [positions] 3/3 (3 valid)
14:02:32  INFO        Daily log -> logs/daily/2026-10-01.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:02 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.09|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AES  P&L -0.0%  $-0.01                                            HOLD|
|  BBY  P&L +0.0%  $+0.01                                            HOLD|
|  FCN  P&L +3.1%  $+1.03                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
=== options_live_micro LIVE 2026-10-01T10:02:33.608200-04:00 share=25% ===
2026-10-01 10:02:33,608 INFO === options_live_micro LIVE 2026-10-01T10:02:33.608200-04:00 share=25% ===
Live account equity $223.09 cash $121.77 #225458845 options_level=3
2026-10-01 10:02:33,650 INFO Live account equity $223.09 cash $121.77 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-10-01 10:02:33,673 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-10-01 10:02:33,688 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (201 earlier lines - see full log file)
| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 295 | 21 |
| S164 | 337 | 24 |
| S165 | 1761 | 36 |
| S166 | 141 | 11 |
| S167 | 318 | 23 |
| S168 | 238 | 20 |
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
| 2026-09-24 |   10 |   12 |   12 |    0 |   11 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    55 |
| 2026-09-25 |   12 |   14 |   12 |    0 |   12 |   12 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-28 |    2 |    4 |    2 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    14 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-01
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    21 | WARN | <<<
| Orphaned lots (post-stable) |  1838 | WARN | <<<
| Missing exit records (post) |  1817 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    29 | INFO |
| Total closed lots           |  2669 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-01_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-01_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1605 med=-28.6% | TAINTED n=1952 med=-40.0% | KEEP-only n=778 med=+50.8% | KILL=21 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.1 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261001T140617Z

- UTC timestamp: `20261001T140617Z`
- GitHub run: [#11572](https://github.com/28twagg-ops/TradingBot/actions/runs/36873561714)
- Run id: `36873561714`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`53s`
- Full logs: `logs/action_runs/20261001T140617Z_live_bot.log`, `logs/action_runs/20261001T140617Z_live_options.log`, `logs/action_runs/20261001T140617Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1606 | 48.1 | -27.6 | +38.9 | $+18,090 |
| TAINTED | 1952 | 33.1 | -40.0 | +12.3 | $-9,981 |
| KEEP-only | 779 | 60.8 | +50.9 | +59.2 | $+11,978 |
| KEEP-only recent | 586 | 59.2 | +53.3 | +67.1 | $+7,917 |

- KEEP strategies (23): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S411, S412
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-01T10:06:24.173706-04:00","date":"2026-10-01","mode":"entry+manage","header":"entry+manage (1 new)","elapsed_s":43.2,"phases_s":{"reconcile":0.36,"cancel":0.11,"manage":2.63,"protective_stops":1.45,"scan":35.43,"entries":0.78,"reconcile2":0.39},"signals":4,"placed":1,"equity":991209.87,"open_positions":13,"pending_orders":1,"open_lots":28,"submitted_today":1,"filled_today":0,"unattributed_contracts":0,"top_signals":["S403:XOM","S403:CVX","S403:ABBV","S210:COST"],"github_run":"11572","github_run_id":"36873561714","status":"ok","data_quality":{"clean":{"n":1606,"win":48.13,"med":-27.62,"avg":38.91,"pnl":18089.83},"tainted":{"n":1952,"win":33.09,"med":-40.0,"avg":12.28,"pnl":-9981.28},"keep_only":{"n":779,"win":60.85,"med":50.85,"avg":59.21,"pnl":11978.45},"keep_only_recent":{"n":586,"win":59.22,"med":53.33,"avg":67.09,"pnl":7917.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:06:18  INFO      Mode: exits
14:06:18  INFO        place_all_stops: checking 3 positions...
14:06:19  INFO        STOP already live AES @ $14.84
14:06:19  INFO        STOP skipped BBY: fractional (0.3827 shares) — software exit will handle it
14:06:19  INFO        STOP skipped FCN: fractional (0.2495 shares) — software exit will handle it
14:06:19  INFO        [positions] 3/3 (3 valid)
14:06:19  INFO        Daily log -> logs/daily/2026-10-01.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.15|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  BBY  P&L -0.0%  $-0.00                                            HOLD|
|  AES  P&L +0.0%  $+0.00                                            HOLD|
|  FCN  P&L +3.3%  $+1.09                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
=== options_live_micro LIVE 2026-10-01T10:06:20.839681-04:00 share=25% ===
2026-10-01 10:06:20,839 INFO === options_live_micro LIVE 2026-10-01T10:06:20.839681-04:00 share=25% ===
Live account equity $223.15 cash $121.77 #225458845 options_level=3
2026-10-01 10:06:21,029 INFO Live account equity $223.15 cash $121.77 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-10-01 10:06:21,336 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-10-01 10:06:21,444 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (204 earlier lines - see full log file)
| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 295 | 21 |
| S164 | 337 | 24 |
| S165 | 1761 | 36 |
| S166 | 141 | 11 |
| S167 | 318 | 23 |
| S168 | 238 | 20 |
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
| 2026-09-24 |   10 |   12 |   12 |    0 |   11 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    55 |
| 2026-09-25 |   12 |   14 |   12 |    0 |   12 |   12 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-28 |    2 |    4 |    2 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    14 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-01
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    21 | WARN | <<<
| Orphaned lots (post-stable) |  1838 | WARN | <<<
| Missing exit records (post) |  1817 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    28 | INFO |
| Total closed lots           |  2670 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-01_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-01_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1606 med=-27.6% | TAINTED n=1952 med=-40.0% | KEEP-only n=779 med=+50.9% | KILL=21 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.15 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261001T141113Z

- UTC timestamp: `20261001T141113Z`
- GitHub run: [#11573](https://github.com/28twagg-ops/TradingBot/actions/runs/36874208108)
- Run id: `36874208108`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`34s`
- Full logs: `logs/action_runs/20261001T141113Z_live_bot.log`, `logs/action_runs/20261001T141113Z_live_options.log`, `logs/action_runs/20261001T141113Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1606 | 48.1 | -27.6 | +38.9 | $+18,090 |
| TAINTED | 1952 | 33.1 | -40.0 | +12.3 | $-9,981 |
| KEEP-only | 779 | 60.8 | +50.9 | +59.2 | $+11,978 |
| KEEP-only recent | 586 | 59.2 | +53.3 | +67.1 | $+7,917 |

- KEEP strategies (23): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S411, S412
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-01T10:11:18.707617-04:00","date":"2026-10-01","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":26.6,"phases_s":{"reconcile":0.27,"cancel":0.08,"manage":1.52,"protective_stops":1.01,"scan":23.0,"entries":0.31},"signals":4,"placed":0,"equity":991373.33,"open_positions":14,"pending_orders":0,"open_lots":29,"submitted_today":1,"filled_today":1,"unattributed_contracts":0,"top_signals":["S403:XOM","S403:CVX","S403:ABBV","S210:COST"],"github_run":"11573","github_run_id":"36874208108","status":"ok","data_quality":{"clean":{"n":1606,"win":48.13,"med":-27.62,"avg":38.91,"pnl":18089.83},"tainted":{"n":1952,"win":33.09,"med":-40.0,"avg":12.28,"pnl":-9981.28},"keep_only":{"n":779,"win":60.85,"med":50.85,"avg":59.21,"pnl":11978.45},"keep_only_recent":{"n":586,"win":59.22,"med":53.33,"avg":67.09,"pnl":7917.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:11:14  INFO      Mode: exits
14:11:15  INFO        place_all_stops: checking 3 positions...
14:11:15  INFO        STOP already live AES @ $14.84
14:11:15  INFO        STOP skipped BBY: fractional (0.3827 shares) — software exit will handle it
14:11:15  INFO        STOP skipped FCN: fractional (0.2495 shares) — software exit will handle it
14:11:15  INFO        [positions] 3/3 (3 valid)
14:11:15  INFO        Daily log -> logs/daily/2026-10-01.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.29|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AES  P&L +0.0%  $+0.00                                            HOLD|
|  BBY  P&L +0.4%  $+0.15                                            HOLD|
|  FCN  P&L +3.2%  $+1.09                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
=== options_live_micro LIVE 2026-10-01T10:11:16.281752-04:00 share=25% ===
2026-10-01 10:11:16,281 INFO === options_live_micro LIVE 2026-10-01T10:11:16.281752-04:00 share=25% ===
Live account equity $223.29 cash $121.77 #225458845 options_level=3
2026-10-01 10:11:16,399 INFO Live account equity $223.29 cash $121.77 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-10-01 10:11:16,483 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-10-01 10:11:16,540 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (195 earlier lines - see full log file)
| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 295 | 21 |
| S164 | 337 | 24 |
| S165 | 1761 | 36 |
| S166 | 141 | 11 |
| S167 | 318 | 23 |
| S168 | 238 | 20 |
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
| 2026-09-24 |   10 |   12 |   12 |    0 |   11 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    55 |
| 2026-09-25 |   12 |   14 |   12 |    0 |   12 |   12 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-28 |    2 |    4 |    2 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    14 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-01
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    21 | WARN | <<<
| Orphaned lots (post-stable) |  1838 | WARN | <<<
| Missing exit records (post) |  1817 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    29 | INFO |
| Total closed lots           |  2670 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-01_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-01_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1606 med=-27.6% | TAINTED n=1952 med=-40.0% | KEEP-only n=779 med=+50.9% | KILL=21 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.29 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261001T141631Z

- UTC timestamp: `20261001T141631Z`
- GitHub run: [#11574](https://github.com/28twagg-ops/TradingBot/actions/runs/36874852913)
- Run id: `36874852913`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`68s`
- Full logs: `logs/action_runs/20261001T141631Z_live_bot.log`, `logs/action_runs/20261001T141631Z_live_options.log`, `logs/action_runs/20261001T141631Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1606 | 48.1 | -27.6 | +38.9 | $+18,090 |
| TAINTED | 1952 | 33.1 | -40.0 | +12.3 | $-9,981 |
| KEEP-only | 779 | 60.8 | +50.9 | +59.2 | $+11,978 |
| KEEP-only recent | 586 | 59.2 | +53.3 | +67.1 | $+7,917 |

- KEEP strategies (23): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S411, S412
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-01T10:16:37.131241-04:00","date":"2026-10-01","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":55.8,"phases_s":{"reconcile":0.1,"cancel":0.02,"manage":1.59,"protective_stops":0.32,"scan":53.13,"entries":0.11},"signals":4,"placed":0,"equity":991422.82,"open_positions":14,"pending_orders":0,"open_lots":29,"submitted_today":1,"filled_today":1,"unattributed_contracts":0,"top_signals":["S403:XOM","S403:CVX","S403:ABBV","S210:COST"],"github_run":"11574","github_run_id":"36874852913","status":"ok","data_quality":{"clean":{"n":1606,"win":48.13,"med":-27.62,"avg":38.91,"pnl":18089.83},"tainted":{"n":1952,"win":33.09,"med":-40.0,"avg":12.28,"pnl":-9981.28},"keep_only":{"n":779,"win":60.85,"med":50.85,"avg":59.21,"pnl":11978.45},"keep_only_recent":{"n":586,"win":59.22,"med":53.33,"avg":67.09,"pnl":7917.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:16:32  INFO      Mode: exits
14:16:32  INFO        place_all_stops: checking 3 positions...
14:16:32  INFO        STOP already live AES @ $14.84
14:16:32  INFO        STOP skipped BBY: fractional (0.3827 shares) — software exit will handle it
14:16:32  INFO        STOP skipped FCN: fractional (0.2495 shares) — software exit will handle it
14:16:33  INFO        [positions] 3/3 (3 valid)
14:16:33  INFO        Daily log -> logs/daily/2026-10-01.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.65|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AES  P&L +0.0%  $+0.00                                            HOLD|
|  BBY  P&L +0.7%  $+0.24                                            HOLD|
|  FCN  P&L +4.1%  $+1.35                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
=== options_live_micro LIVE 2026-10-01T10:16:34.021298-04:00 share=25% ===
2026-10-01 10:16:34,021 INFO === options_live_micro LIVE 2026-10-01T10:16:34.021298-04:00 share=25% ===
Live account equity $223.65 cash $121.77 #225458845 options_level=3
2026-10-01 10:16:34,066 INFO Live account equity $223.65 cash $121.77 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-10-01 10:16:34,091 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-10-01 10:16:34,106 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (196 earlier lines - see full log file)
| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 295 | 21 |
| S164 | 337 | 24 |
| S165 | 1761 | 36 |
| S166 | 141 | 11 |
| S167 | 318 | 23 |
| S168 | 238 | 20 |
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
| 2026-09-24 |   10 |   12 |   12 |    0 |   11 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    55 |
| 2026-09-25 |   12 |   14 |   12 |    0 |   12 |   12 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-28 |    2 |    4 |    2 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    14 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-01
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    21 | WARN | <<<
| Orphaned lots (post-stable) |  1838 | WARN | <<<
| Missing exit records (post) |  1817 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    29 | INFO |
| Total closed lots           |  2670 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-01_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-01_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1606 med=-27.6% | TAINTED n=1952 med=-40.0% | KEEP-only n=779 med=+50.9% | KILL=21 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.65 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261001T142225Z

- UTC timestamp: `20261001T142225Z`
- GitHub run: [#11575](https://github.com/28twagg-ops/TradingBot/actions/runs/36875504712)
- Run id: `36875504712`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`50s`
- Full logs: `logs/action_runs/20261001T142225Z_live_bot.log`, `logs/action_runs/20261001T142225Z_live_options.log`, `logs/action_runs/20261001T142225Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1606 | 48.1 | -27.6 | +38.9 | $+18,090 |
| TAINTED | 1952 | 33.1 | -40.0 | +12.3 | $-9,981 |
| KEEP-only | 779 | 60.8 | +50.9 | +59.2 | $+11,978 |
| KEEP-only recent | 586 | 59.2 | +53.3 | +67.1 | $+7,917 |

- KEEP strategies (23): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S411, S412
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-01T10:22:30.874317-04:00","date":"2026-10-01","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":40.0,"phases_s":{"reconcile":0.25,"cancel":0.07,"manage":2.07,"protective_stops":0.94,"scan":35.84,"entries":0.35},"signals":4,"placed":0,"equity":991494.72,"open_positions":14,"pending_orders":0,"open_lots":29,"submitted_today":1,"filled_today":1,"unattributed_contracts":0,"top_signals":["S403:XOM","S403:CVX","S403:ABBV","S210:COST"],"github_run":"11575","github_run_id":"36875504712","status":"ok","data_quality":{"clean":{"n":1606,"win":48.13,"med":-27.62,"avg":38.91,"pnl":18089.83},"tainted":{"n":1952,"win":33.09,"med":-40.0,"avg":12.28,"pnl":-9981.28},"keep_only":{"n":779,"win":60.85,"med":50.85,"avg":59.21,"pnl":11978.45},"keep_only_recent":{"n":586,"win":59.22,"med":53.33,"avg":67.09,"pnl":7917.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:22:26  INFO      Mode: exits
14:22:26  INFO        place_all_stops: checking 3 positions...
14:22:27  INFO        STOP already live AES @ $14.84
14:22:27  INFO        STOP skipped BBY: fractional (0.3827 shares) — software exit will handle it
14:22:27  INFO        STOP skipped FCN: fractional (0.2495 shares) — software exit will handle it
14:22:27  INFO        [positions] 3/3 (3 valid)
14:22:27  INFO        Daily log -> logs/daily/2026-10-01.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:22 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.55|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AES  P&L +0.0%  $+0.00                                            HOLD|
|  BBY  P&L +0.8%  $+0.26                                            HOLD|
|  FCN  P&L +3.7%  $+1.24                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
=== options_live_micro LIVE 2026-10-01T10:22:28.085184-04:00 share=25% ===
2026-10-01 10:22:28,085 INFO === options_live_micro LIVE 2026-10-01T10:22:28.085184-04:00 share=25% ===
Live account equity $223.55 cash $121.77 #225458845 options_level=3
2026-10-01 10:22:28,251 INFO Live account equity $223.55 cash $121.77 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-10-01 10:22:28,382 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-10-01 10:22:28,467 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (196 earlier lines - see full log file)
| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 295 | 21 |
| S164 | 337 | 24 |
| S165 | 1761 | 36 |
| S166 | 141 | 11 |
| S167 | 318 | 23 |
| S168 | 238 | 20 |
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
| 2026-09-24 |   10 |   12 |   12 |    0 |   11 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    55 |
| 2026-09-25 |   12 |   14 |   12 |    0 |   12 |   12 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-28 |    2 |    4 |    2 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    14 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-01
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    21 | WARN | <<<
| Orphaned lots (post-stable) |  1838 | WARN | <<<
| Missing exit records (post) |  1817 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    29 | INFO |
| Total closed lots           |  2670 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-01_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-01_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1606 med=-27.6% | TAINTED n=1952 med=-40.0% | KEEP-only n=779 med=+50.9% | KILL=21 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.55 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261001T142627Z

- UTC timestamp: `20261001T142627Z`
- GitHub run: [#11576](https://github.com/28twagg-ops/TradingBot/actions/runs/36876156268)
- Run id: `36876156268`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`75s`
- Full logs: `logs/action_runs/20261001T142627Z_live_bot.log`, `logs/action_runs/20261001T142627Z_live_options.log`, `logs/action_runs/20261001T142627Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1606 | 48.1 | -27.6 | +38.9 | $+18,090 |
| TAINTED | 1952 | 33.1 | -40.0 | +12.3 | $-9,981 |
| KEEP-only | 779 | 60.8 | +50.9 | +59.2 | $+11,978 |
| KEEP-only recent | 586 | 59.2 | +53.3 | +67.1 | $+7,917 |

- KEEP strategies (23): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S411, S412
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-01T10:26:35.537988-04:00","date":"2026-10-01","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":61.9,"phases_s":{"reconcile":0.51,"cancel":0.16,"manage":3.3,"protective_stops":2.03,"scan":54.4,"entries":0.66},"signals":4,"placed":0,"equity":991424.79,"open_positions":14,"pending_orders":0,"open_lots":29,"submitted_today":1,"filled_today":1,"unattributed_contracts":0,"top_signals":["S403:XOM","S403:CVX","S403:ABBV","S210:COST"],"github_run":"11576","github_run_id":"36876156268","status":"ok","data_quality":{"clean":{"n":1606,"win":48.13,"med":-27.62,"avg":38.91,"pnl":18089.83},"tainted":{"n":1952,"win":33.09,"med":-40.0,"avg":12.28,"pnl":-9981.28},"keep_only":{"n":779,"win":60.85,"med":50.85,"avg":59.21,"pnl":11978.45},"keep_only_recent":{"n":586,"win":59.22,"med":53.33,"avg":67.09,"pnl":7917.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:26:28  INFO      Mode: exits
14:26:29  INFO        place_all_stops: checking 3 positions...
14:26:29  INFO        STOP already live AES @ $14.84
14:26:29  INFO        STOP skipped BBY: fractional (0.3827 shares) — software exit will handle it
14:26:29  INFO        STOP skipped FCN: fractional (0.2495 shares) — software exit will handle it
14:26:30  INFO        [positions] 3/3 (3 valid)
14:26:30  INFO        Daily log -> logs/daily/2026-10-01.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.61|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AES  P&L +0.0%  $+0.00                                            HOLD|
|  BBY  P&L +1.0%  $+0.33                                            HOLD|
|  FCN  P&L +3.7%  $+1.23                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
=== options_live_micro LIVE 2026-10-01T10:26:31.482185-04:00 share=25% ===
2026-10-01 10:26:31,482 INFO === options_live_micro LIVE 2026-10-01T10:26:31.482185-04:00 share=25% ===
Live account equity $223.61 cash $121.77 #225458845 options_level=3
2026-10-01 10:26:31,733 INFO Live account equity $223.61 cash $121.77 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-10-01 10:26:31,966 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-10-01 10:26:32,119 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (196 earlier lines - see full log file)
| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 295 | 21 |
| S164 | 337 | 24 |
| S165 | 1761 | 36 |
| S166 | 141 | 11 |
| S167 | 318 | 23 |
| S168 | 238 | 20 |
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
| 2026-09-24 |   10 |   12 |   12 |    0 |   11 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    55 |
| 2026-09-25 |   12 |   14 |   12 |    0 |   12 |   12 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-28 |    2 |    4 |    2 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    14 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-01
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    21 | WARN | <<<
| Orphaned lots (post-stable) |  1838 | WARN | <<<
| Missing exit records (post) |  1817 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    29 | INFO |
| Total closed lots           |  2670 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-01_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-01_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1606 med=-27.6% | TAINTED n=1952 med=-40.0% | KEEP-only n=779 med=+50.9% | KILL=21 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.6 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261001T143123Z

- UTC timestamp: `20261001T143123Z`
- GitHub run: [#11577](https://github.com/28twagg-ops/TradingBot/actions/runs/36876810584)
- Run id: `36876810584`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`76s`
- Full logs: `logs/action_runs/20261001T143123Z_live_bot.log`, `logs/action_runs/20261001T143123Z_live_options.log`, `logs/action_runs/20261001T143123Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1606 | 48.1 | -27.6 | +38.9 | $+18,090 |
| TAINTED | 1952 | 33.1 | -40.0 | +12.3 | $-9,981 |
| KEEP-only | 779 | 60.8 | +50.9 | +59.2 | $+11,978 |
| KEEP-only recent | 586 | 59.2 | +53.3 | +67.1 | $+7,917 |

- KEEP strategies (23): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S411, S412
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-01T10:31:30.791606-04:00","date":"2026-10-01","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":63.1,"phases_s":{"reconcile":0.48,"cancel":0.15,"manage":3.53,"protective_stops":1.91,"scan":55.6,"entries":0.61},"signals":4,"placed":0,"equity":991501.58,"open_positions":14,"pending_orders":0,"open_lots":29,"submitted_today":1,"filled_today":1,"unattributed_contracts":0,"top_signals":["S403:XOM","S403:CVX","S403:ABBV","S210:COST"],"github_run":"11577","github_run_id":"36876810584","status":"ok","data_quality":{"clean":{"n":1606,"win":48.13,"med":-27.62,"avg":38.91,"pnl":18089.83},"tainted":{"n":1952,"win":33.09,"med":-40.0,"avg":12.28,"pnl":-9981.28},"keep_only":{"n":779,"win":60.85,"med":50.85,"avg":59.21,"pnl":11978.45},"keep_only_recent":{"n":586,"win":59.22,"med":53.33,"avg":67.09,"pnl":7917.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:31:24  INFO      Mode: exits
14:31:25  INFO        place_all_stops: checking 3 positions...
14:31:25  INFO        STOP already live AES @ $14.84
14:31:25  INFO        STOP skipped BBY: fractional (0.3827 shares) — software exit will handle it
14:31:25  INFO        STOP skipped FCN: fractional (0.2495 shares) — software exit will handle it
14:31:25  INFO        [positions] 3/3 (3 valid)
14:31:26  INFO        Daily log -> logs/daily/2026-10-01.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.47|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AES  P&L -0.0%  $-0.01                                            HOLD|
|  BBY  P&L +0.6%  $+0.19                                            HOLD|
|  FCN  P&L +3.7%  $+1.24                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
=== options_live_micro LIVE 2026-10-01T10:31:27.099278-04:00 share=25% ===
2026-10-01 10:31:27,099 INFO === options_live_micro LIVE 2026-10-01T10:31:27.099278-04:00 share=25% ===
Live account equity $223.48 cash $121.77 #225458845 options_level=3
2026-10-01 10:31:27,321 INFO Live account equity $223.48 cash $121.77 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-10-01 10:31:27,531 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-10-01 10:31:27,671 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (196 earlier lines - see full log file)
| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 295 | 21 |
| S164 | 337 | 24 |
| S165 | 1761 | 36 |
| S166 | 141 | 11 |
| S167 | 318 | 23 |
| S168 | 238 | 20 |
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
| 2026-09-24 |   10 |   12 |   12 |    0 |   11 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    55 |
| 2026-09-25 |   12 |   14 |   12 |    0 |   12 |   12 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-28 |    2 |    4 |    2 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    14 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-01
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    21 | WARN | <<<
| Orphaned lots (post-stable) |  1838 | WARN | <<<
| Missing exit records (post) |  1817 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    29 | INFO |
| Total closed lots           |  2670 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-01_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-01_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1606 med=-27.6% | TAINTED n=1952 med=-40.0% | KEEP-only n=779 med=+50.9% | KILL=21 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.47 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261001T143637Z

- UTC timestamp: `20261001T143637Z`
- GitHub run: [#11578](https://github.com/28twagg-ops/TradingBot/actions/runs/36877468751)
- Run id: `36877468751`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`68s`
- Full logs: `logs/action_runs/20261001T143637Z_live_bot.log`, `logs/action_runs/20261001T143637Z_live_options.log`, `logs/action_runs/20261001T143637Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1606 | 48.1 | -27.6 | +38.9 | $+18,090 |
| TAINTED | 1952 | 33.1 | -40.0 | +12.3 | $-9,981 |
| KEEP-only | 779 | 60.8 | +50.9 | +59.2 | $+11,978 |
| KEEP-only recent | 586 | 59.2 | +53.3 | +67.1 | $+7,917 |

- KEEP strategies (23): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S411, S412
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-01T10:36:42.657421-04:00","date":"2026-10-01","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":56.1,"phases_s":{"reconcile":0.09,"cancel":0.02,"manage":1.02,"protective_stops":0.27,"scan":54.02,"entries":0.12},"signals":4,"placed":0,"equity":991463.62,"open_positions":13,"pending_orders":0,"open_lots":29,"submitted_today":1,"filled_today":1,"unattributed_contracts":0,"top_signals":["S403:XOM","S403:CVX","S403:ABBV","S210:COST"],"github_run":"11578","github_run_id":"36877468751","status":"ok","data_quality":{"clean":{"n":1606,"win":48.13,"med":-27.62,"avg":38.91,"pnl":18089.83},"tainted":{"n":1952,"win":33.09,"med":-40.0,"avg":12.28,"pnl":-9981.28},"keep_only":{"n":779,"win":60.85,"med":50.85,"avg":59.21,"pnl":11978.45},"keep_only_recent":{"n":586,"win":59.22,"med":53.33,"avg":67.09,"pnl":7917.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:36:38  INFO      Mode: exits
14:36:38  INFO        place_all_stops: checking 3 positions...
14:36:38  INFO        STOP already live AES @ $14.84
14:36:38  INFO        STOP skipped BBY: fractional (0.3827 shares) — software exit will handle it
14:36:38  INFO        STOP skipped FCN: fractional (0.2495 shares) — software exit will handle it
14:36:39  INFO        [positions] 3/3 (3 valid)
14:36:39  INFO        Daily log -> logs/daily/2026-10-01.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.35|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AES  P&L +0.0%  $+0.01                                            HOLD|
|  BBY  P&L +0.6%  $+0.21                                            HOLD|
|  FCN  P&L +3.2%  $+1.07                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
=== options_live_micro LIVE 2026-10-01T10:36:39.953146-04:00 share=25% ===
2026-10-01 10:36:39,953 INFO === options_live_micro LIVE 2026-10-01T10:36:39.953146-04:00 share=25% ===
Live account equity $223.35 cash $121.77 #225458845 options_level=3
2026-10-01 10:36:39,997 INFO Live account equity $223.35 cash $121.77 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-10-01 10:36:40,021 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-10-01 10:36:40,041 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (198 earlier lines - see full log file)
| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 295 | 21 |
| S164 | 337 | 24 |
| S165 | 1761 | 36 |
| S166 | 141 | 11 |
| S167 | 318 | 23 |
| S168 | 238 | 20 |
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
| 2026-09-24 |   10 |   12 |   12 |    0 |   11 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    55 |
| 2026-09-25 |   12 |   14 |   12 |    0 |   12 |   12 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-28 |    2 |    4 |    2 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    14 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-01
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    21 | WARN | <<<
| Orphaned lots (post-stable) |  1838 | WARN | <<<
| Missing exit records (post) |  1817 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    29 | INFO |
| Total closed lots           |  2670 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-01_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-01_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1606 med=-27.6% | TAINTED n=1952 med=-40.0% | KEEP-only n=779 med=+50.9% | KILL=21 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.35 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261001T144135Z

- UTC timestamp: `20261001T144135Z`
- GitHub run: [#11579](https://github.com/28twagg-ops/TradingBot/actions/runs/36878126358)
- Run id: `36878126358`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`74s`
- Full logs: `logs/action_runs/20261001T144135Z_live_bot.log`, `logs/action_runs/20261001T144135Z_live_options.log`, `logs/action_runs/20261001T144135Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1607 | 48.2 | -26.7 | +38.9 | $+18,117 |
| TAINTED | 1952 | 33.1 | -40.0 | +12.3 | $-9,981 |
| KEEP-only | 779 | 60.8 | +50.9 | +59.2 | $+11,978 |
| KEEP-only recent | 586 | 59.2 | +53.3 | +67.1 | $+7,917 |

- KEEP strategies (23): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S411, S412
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-01T10:41:43.863316-04:00","date":"2026-10-01","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":60.8,"phases_s":{"reconcile":0.48,"cancel":0.16,"manage":2.8,"protective_stops":1.79,"scan":54.18,"entries":0.61},"signals":4,"placed":0,"equity":991518.33,"open_positions":13,"pending_orders":0,"open_lots":28,"submitted_today":1,"filled_today":1,"unattributed_contracts":0,"top_signals":["S403:XOM","S403:CVX","S403:ABBV","S210:COST"],"github_run":"11579","github_run_id":"36878126358","status":"ok","data_quality":{"clean":{"n":1607,"win":48.16,"med":-26.67,"avg":38.91,"pnl":18116.83},"tainted":{"n":1952,"win":33.09,"med":-40.0,"avg":12.28,"pnl":-9981.28},"keep_only":{"n":779,"win":60.85,"med":50.85,"avg":59.21,"pnl":11978.45},"keep_only_recent":{"n":586,"win":59.22,"med":53.33,"avg":67.09,"pnl":7917.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:41:36  INFO      Mode: exits
14:41:37  INFO        place_all_stops: checking 3 positions...
14:41:37  INFO        STOP already live AES @ $14.84
14:41:37  INFO        STOP skipped BBY: fractional (0.3827 shares) — software exit will handle it
14:41:37  INFO        STOP skipped FCN: fractional (0.2495 shares) — software exit will handle it
14:41:38  INFO        [positions] 3/3 (3 valid)
14:41:39  INFO        Daily log -> logs/daily/2026-10-01.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.51|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AES  P&L +0.0%  $+0.01                                            HOLD|
|  BBY  P&L +0.3%  $+0.11                                            HOLD|
|  FCN  P&L +4.0%  $+1.34                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
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
=== options_live_micro LIVE 2026-10-01T10:41:39.856274-04:00 share=25% ===
2026-10-01 10:41:39,856 INFO === options_live_micro LIVE 2026-10-01T10:41:39.856274-04:00 share=25% ===
Live account equity $223.51 cash $121.77 #225458845 options_level=3
2026-10-01 10:41:40,094 INFO Live account equity $223.51 cash $121.77 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-10-01 10:41:40,315 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-10-01 10:41:40,475 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (199 earlier lines - see full log file)
| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 295 | 21 |
| S164 | 337 | 24 |
| S165 | 1761 | 36 |
| S166 | 141 | 11 |
| S167 | 318 | 23 |
| S168 | 238 | 20 |
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
| 2026-09-24 |   10 |   12 |   12 |    0 |   11 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    55 |
| 2026-09-25 |   12 |   14 |   12 |    0 |   12 |   12 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |
| 2026-09-28 |    2 |    4 |    2 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    14 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-01
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |    21 | WARN | <<<
| Orphaned lots (post-stable) |  1838 | WARN | <<<
| Missing exit records (post) |  1817 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    28 | INFO |
| Total closed lots           |  2671 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-01_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-01_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1607 med=-26.7% | TAINTED n=1952 med=-40.0% | KEEP-only n=779 med=+50.9% | KILL=21 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.51 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---
