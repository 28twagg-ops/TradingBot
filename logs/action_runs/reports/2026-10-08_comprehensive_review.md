# Daily Comprehensive Action Review - 2026-10-08

_Auto-generated from GitHub Actions run output. Each run appends a summary; full stdout is in linked per-run log files._
## Run 20261008T130130Z

- UTC timestamp: `20261008T130130Z`
- GitHub run: [#12214](https://github.com/28twagg-ops/TradingBot/actions/runs/37780951966)
- Run id: `37780951966`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`14s`
- Full logs: `logs/action_runs/20261008T130130Z_live_bot.log`, `logs/action_runs/20261008T130130Z_live_options.log`, `logs/action_runs/20261008T130130Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1629 | 48.6 | -24.2 | +38.8 | $+18,602 |
| TAINTED | 1965 | 32.9 | -40.0 | +11.9 | $-10,172 |
| KEEP-only | 799 | 61.5 | +51.4 | +58.8 | $+12,486 |
| KEEP-only recent | 606 | 60.1 | +53.3 | +66.3 | $+8,425 |

- KEEP strategies (23): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S411, S412
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-08T09:01:36.367159-04:00","date":"2026-10-08","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.5,"phases_s":{"reconcile":0.62},"signals":0,"placed":0,"equity":987096.21,"open_positions":11,"pending_orders":0,"open_lots":10,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"12214","github_run_id":"37780951966","status":"ok","data_quality":{"clean":{"n":1629,"win":48.56,"med":-24.24,"avg":38.83,"pnl":18601.83},"tainted":{"n":1965,"win":32.93,"med":-40.0,"avg":11.92,"pnl":-10172.28},"keep_only":{"n":799,"win":61.45,"med":51.39,"avg":58.79,"pnl":12486.45},"keep_only_recent":{"n":606,"win":60.07,"med":53.33,"avg":66.27,"pnl":8425.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:01:30  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.43|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $224.43|
|  Cash                                                           $224.43|
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
|  2026-10-07  SELL  AMZN  Pullback50  $34.07  P&L $+0.54                |
|  2026-10-07  SELL  GOOG  Pullback50  $33.90  P&L $+0.39                |
|  2026-10-07  SELL  AES  Pullback50  $33.51  P&L $-0.00                 |
|  2026-10-07  SELL  TECH  Pullback50  $33.54  P&L $+0.00                |
|  2026-10-07  SELL  AES  Pullback50  $33.53  P&L $-0.01                 |
|  2026-10-07  SELL  AMGN  Pullback50  $33.44  P&L $-0.08                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-08T09:01:32.789620-04:00 share=25% ===
2026-10-08 09:01:32,789 INFO === options_live_micro LIVE 2026-10-08T09:01:32.789620-04:00 share=25% ===
Live account equity $224.43 cash $224.43 #225458845 options_level=3
2026-10-08 09:01:33,036 INFO Live account equity $224.43 cash $224.43 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-10-08 09:01:33,111 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-10-08 09:01:33,185 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (177 earlier lines - see full log file)
| S163 | 297 | 22 |
| S164 | 341 | 26 |
| S165 | 1761 | 36 |
| S166 | 143 | 12 |
| S167 | 320 | 24 |
| S168 | 240 | 21 |
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
| 2026-10-02 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-07 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-08
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |  1914 | WARN | <<<
| Missing exit records (post) |  1913 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |    10 | INFO |
| Total closed lots           |  2705 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-08_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-08_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1629 med=-24.2% | TAINTED n=1965 med=-40.0% | KEEP-only n=799 med=+51.4% | KILL=21 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.43 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261008T130616Z

- UTC timestamp: `20261008T130616Z`
- GitHub run: [#12215](https://github.com/28twagg-ops/TradingBot/actions/runs/37781592528)
- Run id: `37781592528`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`9s`
- Full logs: `logs/action_runs/20261008T130616Z_live_bot.log`, `logs/action_runs/20261008T130616Z_live_options.log`, `logs/action_runs/20261008T130616Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1629 | 48.6 | -24.2 | +38.8 | $+18,602 |
| TAINTED | 1965 | 32.9 | -40.0 | +11.9 | $-10,172 |
| KEEP-only | 799 | 61.5 | +51.4 | +58.8 | $+12,486 |
| KEEP-only recent | 606 | 60.1 | +53.3 | +66.3 | $+8,425 |

- KEEP strategies (23): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S411, S412
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-08T09:06:22.390741-04:00","date":"2026-10-08","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.8,"phases_s":{"reconcile":0.3},"signals":0,"placed":0,"equity":987094.48,"open_positions":11,"pending_orders":0,"open_lots":10,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"12215","github_run_id":"37781592528","status":"ok","data_quality":{"clean":{"n":1629,"win":48.56,"med":-24.24,"avg":38.83,"pnl":18601.83},"tainted":{"n":1965,"win":32.93,"med":-40.0,"avg":11.92,"pnl":-10172.28},"keep_only":{"n":799,"win":61.45,"med":51.39,"avg":58.79,"pnl":12486.45},"keep_only_recent":{"n":606,"win":60.07,"med":53.33,"avg":66.27,"pnl":8425.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
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
|  Equity                                                         $224.43|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $224.43|
|  Cash                                                           $224.43|
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
|  2026-10-07  SELL  AMZN  Pullback50  $34.07  P&L $+0.54                |
|  2026-10-07  SELL  GOOG  Pullback50  $33.90  P&L $+0.39                |
|  2026-10-07  SELL  AES  Pullback50  $33.51  P&L $-0.00                 |
|  2026-10-07  SELL  TECH  Pullback50  $33.54  P&L $+0.00                |
|  2026-10-07  SELL  AES  Pullback50  $33.53  P&L $-0.01                 |
|  2026-10-07  SELL  AMGN  Pullback50  $33.44  P&L $-0.08                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-08T09:06:20.004911-04:00 share=25% ===
2026-10-08 09:06:20,004 INFO === options_live_micro LIVE 2026-10-08T09:06:20.004911-04:00 share=25% ===
Live account equity $224.43 cash $224.43 #225458845 options_level=3
2026-10-08 09:06:20,127 INFO Live account equity $224.43 cash $224.43 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-10-08 09:06:20,158 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-10-08 09:06:20,189 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (177 earlier lines - see full log file)
| S163 | 297 | 22 |
| S164 | 341 | 26 |
| S165 | 1761 | 36 |
| S166 | 143 | 12 |
| S167 | 320 | 24 |
| S168 | 240 | 21 |
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
| 2026-10-02 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-07 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-08
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |  1914 | WARN | <<<
| Missing exit records (post) |  1913 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |    10 | INFO |
| Total closed lots           |  2705 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-08_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-08_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1629 med=-24.2% | TAINTED n=1965 med=-40.0% | KEEP-only n=799 med=+51.4% | KILL=21 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.43 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261008T131129Z

- UTC timestamp: `20261008T131129Z`
- GitHub run: [#12216](https://github.com/28twagg-ops/TradingBot/actions/runs/37782229384)
- Run id: `37782229384`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`13s`
- Full logs: `logs/action_runs/20261008T131129Z_live_bot.log`, `logs/action_runs/20261008T131129Z_live_options.log`, `logs/action_runs/20261008T131129Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1629 | 48.6 | -24.2 | +38.8 | $+18,602 |
| TAINTED | 1965 | 32.9 | -40.0 | +11.9 | $-10,172 |
| KEEP-only | 799 | 61.5 | +51.4 | +58.8 | $+12,486 |
| KEEP-only recent | 606 | 60.1 | +53.3 | +66.3 | $+8,425 |

- KEEP strategies (23): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S411, S412
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-08T09:11:33.951673-04:00","date":"2026-10-08","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.1},"signals":0,"placed":0,"equity":986975.26,"open_positions":11,"pending_orders":0,"open_lots":10,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"12216","github_run_id":"37782229384","status":"ok","data_quality":{"clean":{"n":1629,"win":48.56,"med":-24.24,"avg":38.83,"pnl":18601.83},"tainted":{"n":1965,"win":32.93,"med":-40.0,"avg":11.92,"pnl":-10172.28},"keep_only":{"n":799,"win":61.45,"med":51.39,"avg":58.79,"pnl":12486.45},"keep_only_recent":{"n":606,"win":60.07,"med":53.33,"avg":66.27,"pnl":8425.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:11:30  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.43|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $224.43|
|  Cash                                                           $224.43|
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
|  2026-10-07  SELL  AMZN  Pullback50  $34.07  P&L $+0.54                |
|  2026-10-07  SELL  GOOG  Pullback50  $33.90  P&L $+0.39                |
|  2026-10-07  SELL  AES  Pullback50  $33.51  P&L $-0.00                 |
|  2026-10-07  SELL  TECH  Pullback50  $33.54  P&L $+0.00                |
|  2026-10-07  SELL  AES  Pullback50  $33.53  P&L $-0.01                 |
|  2026-10-07  SELL  AMGN  Pullback50  $33.44  P&L $-0.08                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-08T09:11:31.404839-04:00 share=25% ===
2026-10-08 09:11:31,404 INFO === options_live_micro LIVE 2026-10-08T09:11:31.404839-04:00 share=25% ===
Live account equity $224.43 cash $224.43 #225458845 options_level=3
2026-10-08 09:11:31,453 INFO Live account equity $224.43 cash $224.43 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-10-08 09:11:31,461 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-10-08 09:11:31,468 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (177 earlier lines - see full log file)
| S163 | 297 | 22 |
| S164 | 341 | 26 |
| S165 | 1761 | 36 |
| S166 | 143 | 12 |
| S167 | 320 | 24 |
| S168 | 240 | 21 |
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
| 2026-10-02 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-07 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-08
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |  1914 | WARN | <<<
| Missing exit records (post) |  1913 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |    10 | INFO |
| Total closed lots           |  2705 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-08_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-08_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1629 med=-24.2% | TAINTED n=1965 med=-40.0% | KEEP-only n=799 med=+51.4% | KILL=21 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.43 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261008T131630Z

- UTC timestamp: `20261008T131630Z`
- GitHub run: [#12217](https://github.com/28twagg-ops/TradingBot/actions/runs/37782870569)
- Run id: `37782870569`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`13s`
- Full logs: `logs/action_runs/20261008T131630Z_live_bot.log`, `logs/action_runs/20261008T131630Z_live_options.log`, `logs/action_runs/20261008T131630Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1629 | 48.6 | -24.2 | +38.8 | $+18,602 |
| TAINTED | 1965 | 32.9 | -40.0 | +11.9 | $-10,172 |
| KEEP-only | 799 | 61.5 | +51.4 | +58.8 | $+12,486 |
| KEEP-only recent | 606 | 60.1 | +53.3 | +66.3 | $+8,425 |

- KEEP strategies (23): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S411, S412
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-08T09:16:36.288658-04:00","date":"2026-10-08","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.8,"phases_s":{"reconcile":0.11},"signals":0,"placed":0,"equity":986978.05,"open_positions":11,"pending_orders":0,"open_lots":10,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"12217","github_run_id":"37782870569","status":"ok","data_quality":{"clean":{"n":1629,"win":48.56,"med":-24.24,"avg":38.83,"pnl":18601.83},"tainted":{"n":1965,"win":32.93,"med":-40.0,"avg":11.92,"pnl":-10172.28},"keep_only":{"n":799,"win":61.45,"med":51.39,"avg":58.79,"pnl":12486.45},"keep_only_recent":{"n":606,"win":60.07,"med":53.33,"avg":66.27,"pnl":8425.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:16:32  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.43|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $224.43|
|  Cash                                                           $224.43|
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
|  2026-10-07  SELL  AMZN  Pullback50  $34.07  P&L $+0.54                |
|  2026-10-07  SELL  GOOG  Pullback50  $33.90  P&L $+0.39                |
|  2026-10-07  SELL  AES  Pullback50  $33.51  P&L $-0.00                 |
|  2026-10-07  SELL  TECH  Pullback50  $33.54  P&L $+0.00                |
|  2026-10-07  SELL  AES  Pullback50  $33.53  P&L $-0.01                 |
|  2026-10-07  SELL  AMGN  Pullback50  $33.44  P&L $-0.08                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-08T09:16:33.611844-04:00 share=25% ===
2026-10-08 09:16:33,611 INFO === options_live_micro LIVE 2026-10-08T09:16:33.611844-04:00 share=25% ===
Live account equity $224.43 cash $224.43 #225458845 options_level=3
2026-10-08 09:16:33,654 INFO Live account equity $224.43 cash $224.43 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-10-08 09:16:33,662 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-10-08 09:16:33,670 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (177 earlier lines - see full log file)
| S163 | 297 | 22 |
| S164 | 341 | 26 |
| S165 | 1761 | 36 |
| S166 | 143 | 12 |
| S167 | 320 | 24 |
| S168 | 240 | 21 |
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
| 2026-10-02 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-07 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-08
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |  1914 | WARN | <<<
| Missing exit records (post) |  1913 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |    10 | INFO |
| Total closed lots           |  2705 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-08_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-08_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1629 med=-24.2% | TAINTED n=1965 med=-40.0% | KEEP-only n=799 med=+51.4% | KILL=21 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.43 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261008T132120Z

- UTC timestamp: `20261008T132120Z`
- GitHub run: [#12218](https://github.com/28twagg-ops/TradingBot/actions/runs/37783521383)
- Run id: `37783521383`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`11s`
- Full logs: `logs/action_runs/20261008T132120Z_live_bot.log`, `logs/action_runs/20261008T132120Z_live_options.log`, `logs/action_runs/20261008T132120Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1629 | 48.6 | -24.2 | +38.8 | $+18,602 |
| TAINTED | 1965 | 32.9 | -40.0 | +11.9 | $-10,172 |
| KEEP-only | 799 | 61.5 | +51.4 | +58.8 | $+12,486 |
| KEEP-only recent | 606 | 60.1 | +53.3 | +66.3 | $+8,425 |

- KEEP strategies (23): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S411, S412
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-08T09:21:24.902303-04:00","date":"2026-10-08","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.16},"signals":0,"placed":0,"equity":986999.59,"open_positions":11,"pending_orders":0,"open_lots":10,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"12218","github_run_id":"37783521383","status":"ok","data_quality":{"clean":{"n":1629,"win":48.56,"med":-24.24,"avg":38.83,"pnl":18601.83},"tainted":{"n":1965,"win":32.93,"med":-40.0,"avg":11.92,"pnl":-10172.28},"keep_only":{"n":799,"win":61.45,"med":51.39,"avg":58.79,"pnl":12486.45},"keep_only_recent":{"n":606,"win":60.07,"med":53.33,"avg":66.27,"pnl":8425.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
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
|  Equity                                                         $224.43|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $224.43|
|  Cash                                                           $224.43|
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
|  2026-10-07  SELL  AMZN  Pullback50  $34.07  P&L $+0.54                |
|  2026-10-07  SELL  GOOG  Pullback50  $33.90  P&L $+0.39                |
|  2026-10-07  SELL  AES  Pullback50  $33.51  P&L $-0.00                 |
|  2026-10-07  SELL  TECH  Pullback50  $33.54  P&L $+0.00                |
|  2026-10-07  SELL  AES  Pullback50  $33.53  P&L $-0.01                 |
|  2026-10-07  SELL  AMGN  Pullback50  $33.44  P&L $-0.08                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-08T09:21:22.677909-04:00 share=25% ===
2026-10-08 09:21:22,677 INFO === options_live_micro LIVE 2026-10-08T09:21:22.677909-04:00 share=25% ===
Live account equity $224.43 cash $224.43 #225458845 options_level=3
2026-10-08 09:21:22,711 INFO Live account equity $224.43 cash $224.43 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-10-08 09:21:22,717 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-10-08 09:21:22,722 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (177 earlier lines - see full log file)
| S163 | 297 | 22 |
| S164 | 341 | 26 |
| S165 | 1761 | 36 |
| S166 | 143 | 12 |
| S167 | 320 | 24 |
| S168 | 240 | 21 |
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
| 2026-10-02 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-07 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-08
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |  1914 | WARN | <<<
| Missing exit records (post) |  1913 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |    10 | INFO |
| Total closed lots           |  2705 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-08_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-08_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1629 med=-24.2% | TAINTED n=1965 med=-40.0% | KEEP-only n=799 med=+51.4% | KILL=21 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.43 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261008T132616Z

- UTC timestamp: `20261008T132616Z`
- GitHub run: [#12219](https://github.com/28twagg-ops/TradingBot/actions/runs/37784167171)
- Run id: `37784167171`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`8s`
- Full logs: `logs/action_runs/20261008T132616Z_live_bot.log`, `logs/action_runs/20261008T132616Z_live_options.log`, `logs/action_runs/20261008T132616Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1629 | 48.6 | -24.2 | +38.8 | $+18,602 |
| TAINTED | 1965 | 32.9 | -40.0 | +11.9 | $-10,172 |
| KEEP-only | 799 | 61.5 | +51.4 | +58.8 | $+12,486 |
| KEEP-only recent | 606 | 60.1 | +53.3 | +66.3 | $+8,425 |

- KEEP strategies (23): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S411, S412
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-08T09:26:21.900750-04:00","date":"2026-10-08","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.0,"phases_s":{"reconcile":0.28},"signals":0,"placed":0,"equity":986833.26,"open_positions":11,"pending_orders":0,"open_lots":10,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"12219","github_run_id":"37784167171","status":"ok","data_quality":{"clean":{"n":1629,"win":48.56,"med":-24.24,"avg":38.83,"pnl":18601.83},"tainted":{"n":1965,"win":32.93,"med":-40.0,"avg":11.92,"pnl":-10172.28},"keep_only":{"n":799,"win":61.45,"med":51.39,"avg":58.79,"pnl":12486.45},"keep_only_recent":{"n":606,"win":60.07,"med":53.33,"avg":66.27,"pnl":8425.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:26:17  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.43|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $224.43|
|  Cash                                                           $224.43|
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
|  2026-10-07  SELL  AMZN  Pullback50  $34.07  P&L $+0.54                |
|  2026-10-07  SELL  GOOG  Pullback50  $33.90  P&L $+0.39                |
|  2026-10-07  SELL  AES  Pullback50  $33.51  P&L $-0.00                 |
|  2026-10-07  SELL  TECH  Pullback50  $33.54  P&L $+0.00                |
|  2026-10-07  SELL  AES  Pullback50  $33.53  P&L $-0.01                 |
|  2026-10-07  SELL  AMGN  Pullback50  $33.44  P&L $-0.08                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-08T09:26:19.583745-04:00 share=25% ===
2026-10-08 09:26:19,583 INFO === options_live_micro LIVE 2026-10-08T09:26:19.583745-04:00 share=25% ===
Live account equity $224.43 cash $224.43 #225458845 options_level=3
2026-10-08 09:26:19,706 INFO Live account equity $224.43 cash $224.43 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-10-08 09:26:19,766 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-10-08 09:26:19,800 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (177 earlier lines - see full log file)
| S163 | 297 | 22 |
| S164 | 341 | 26 |
| S165 | 1761 | 36 |
| S166 | 143 | 12 |
| S167 | 320 | 24 |
| S168 | 240 | 21 |
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
| 2026-10-02 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-07 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-08
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |  1914 | WARN | <<<
| Missing exit records (post) |  1913 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |    10 | INFO |
| Total closed lots           |  2705 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-08_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-08_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1629 med=-24.2% | TAINTED n=1965 med=-40.0% | KEEP-only n=799 med=+51.4% | KILL=21 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.43 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261008T133130Z

- UTC timestamp: `20261008T133130Z`
- GitHub run: [#12220](https://github.com/28twagg-ops/TradingBot/actions/runs/37784823749)
- Run id: `37784823749`
- Live bot: exit=`0`, duration=`215s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20261008T133130Z_live_bot.log`, `logs/action_runs/20261008T133130Z_live_options.log`, `logs/action_runs/20261008T133130Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1629 | 48.6 | -24.2 | +38.8 | $+18,602 |
| TAINTED | 1965 | 32.9 | -40.0 | +11.9 | $-10,172 |
| KEEP-only | 799 | 61.5 | +51.4 | +58.8 | $+12,486 |
| KEEP-only recent | 606 | 60.1 | +53.3 | +66.3 | $+8,425 |

- KEEP strategies (23): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S411, S412
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-08T09:26:21.900750-04:00","date":"2026-10-08","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.0,"phases_s":{"reconcile":0.28},"signals":0,"placed":0,"equity":986833.26,"open_positions":11,"pending_orders":0,"open_lots":10,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"12219","github_run_id":"37784167171","status":"ok","data_quality":{"clean":{"n":1629,"win":48.56,"med":-24.24,"avg":38.83,"pnl":18601.83},"tainted":{"n":1965,"win":32.93,"med":-40.0,"avg":11.92,"pnl":-10172.28},"keep_only":{"n":799,"win":61.45,"med":51.39,"avg":58.79,"pnl":12486.45},"keep_only_recent":{"n":606,"win":60.07,"med":53.33,"avg":66.27,"pnl":8425.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:31:31  INFO      Mode: morning_prep
13:31:32  INFO        [prep_positions] 3/3 (3 valid)
13:31:32  INFO      Fetching tickers (universe=both)...
13:31:32  INFO        S&P 500: 503
13:31:32  INFO        MidCap 400: 400
13:31:32  INFO        Total: 902 tickers
13:31:33  INFO        [prep_universe] 40/899 (40 valid)
13:31:35  INFO        [prep_universe] 80/899 (80 valid)
13:31:36  INFO        [prep_universe] 120/899 (120 valid)
13:31:38  INFO        [prep_universe] 160/899 (160 valid)
13:31:39  INFO        [prep_universe] 200/899 (199 valid)
13:31:46  INFO        [prep_universe] 240/899 (238 valid)
13:31:59  INFO        [prep_universe] 280/899 (278 valid)
13:32:09  INFO        [prep_universe] 320/899 (318 valid)
13:32:23  INFO        [prep_universe] 360/899 (358 valid)
13:32:33  INFO        [prep_universe] 400/899 (398 valid)
13:32:46  INFO        [prep_universe] 440/899 (438 valid)
13:32:59  INFO        [prep_universe] 480/899 (477 valid)
13:33:11  INFO        [prep_universe] 520/899 (517 valid)
13:33:21  INFO        [prep_universe] 560/899 (557 valid)
13:33:34  INFO        [prep_universe] 600/899 (597 valid)
13:33:47  INFO        [prep_universe] 640/899 (637 valid)
13:33:57  INFO        [prep_universe] 680/899 (677 valid)
13:34:10  INFO        [prep_universe] 720/899 (717 valid)
13:34:23  INFO        [prep_universe] 760/899 (757 valid)
13:34:33  INFO        [prep_universe] 800/899 (797 valid)
13:34:46  INFO        [prep_universe] 840/899 (837 valid)
13:34:59  INFO        [prep_universe] 880/899 (877 valid)
13:35:03  INFO        [prep_universe] 899/899 (896 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.58|
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
|  Invested                                                       $101.11|
|  Open P&L                                                        $+0.16|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  KTOS     MomReversal     $33.83     $42.19   $42.41   +0.5%   $+0.18  |
|  NRG      EarningsDrift   $33.61     $107.50  $107.39  -0.1%   $-0.04  |
|  OC       MomReversal     $33.67     $113.39  $113.46  +0.1%   $+0.02  |
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
|  Signal candidates                                                   43|
|  Universe scanned                                                   899|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-08T09:35:06.197055-04:00 share=25% ===
2026-10-08 09:35:06,197 INFO === options_live_micro LIVE 2026-10-08T09:35:06.197055-04:00 share=25% ===
Live account equity $224.16 cash $123.47 #225458845 options_level=3
2026-10-08 09:35:06,269 INFO Live account equity $224.16 cash $123.47 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-10-08 09:35:06,292 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-10-08 09:35:06,308 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=10 paper_keys=yes dry_run=False
  alpaca positions=13
  FLAG 3 lot(s) missing from Alpaca
    b51|S396|2a51458e MARA261009C00010000
    b52|S397|59806b61 COIN261009C00190000
    b66|S163|d832ca5a COIN261009C00192500
  reconcile: backfill exit b51|S396 MARA -52.6% fill=0.27
  reconcile: backfill exit b52|S397 COIN -28.4% fill=0.48
  reconcile: backfill exit b66|S163 COIN -95.7% fill=0.02
  State updated (attributed/cleared=3, leftover=0).
options_reconcile: done
Layout: controlled:77:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:77:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      77
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$987,131.70
  buying_power=$3,825,767.20 cash=$979,758.20
  open option orders: 6
    XOM261009C00167500 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
    MARA261106C00011500 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
    MARA261016C00011000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
    MARA261023C00011000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
    MARA261030C00011500 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
  open option positions: 8
    C261009C00131000 qty=1 mkt=$5.00
    DKNG261009C00022500 qty=-1 mkt=$-10.00
    DKNG261016C00023500 qty=1 mkt=$0.00
    MARA261016C00011000 qty=1 mkt=$16.00
    MARA261023C00011000 qty=1 mkt=$30.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-10-08T09:35:09.107037-04:00 ===

[Run context]
Paper auth OK — equity $987134.70, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
S406-only twin b91 s406_only — S406 | TP+50%/SL-40% | paper edge test
Variation study: 75 lab/promising bucket(s) | cohort: 75 unique (S163, S164, S166, S167, S168, S169, S170, S171, S172, S175, S200, S201 … +63 more) | max 200 new entries/run
Dropped (no new entries; ex-reflected P&L): S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
Shared-OCC entry block ON (one lab lot per contract)
2026-10-08 09:35:10,083 INFO   EXIT [b6|lab0006_s210_w2_1005_1045_r1|S210] take_profit (+214.9%) SELL 1 XOM261009C00167500 @<= 1.45
  EXIT [b421|lab0421_s365_w2_1005_1045_r2|S365] stop_loss (-100.0%) SELL blocked (uncovered/shared OCC) DKNG261016C00023500 x1: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
Protective stops: placed=0 upgraded=0 already=5 failed=2 (market-first)

[Scan + entries]
Scanning 117 symbols for [S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S204, S205, S206, S208, S210, S213, S214, S215, S219, S220, S221, S402, S403, S350, S352, S356, S357, S358, S359, S361, S362, S364, S365, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S395, S396, S397, S398, S404, S406, S409, S410, S411, S412, S413, S414, S415] …
Fetched daily bars for 113/117 symbols
```

---

## Run 20261008T133712Z

- UTC timestamp: `20261008T133712Z`
- GitHub run: [#12221](https://github.com/28twagg-ops/TradingBot/actions/runs/37785483309)
- Run id: `37785483309`
- Live bot: exit=`0`, duration=`215s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20261008T133712Z_live_bot.log`, `logs/action_runs/20261008T133712Z_live_options.log`, `logs/action_runs/20261008T133712Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1629 | 48.6 | -24.2 | +38.8 | $+18,602 |
| TAINTED | 1965 | 32.9 | -40.0 | +11.9 | $-10,172 |
| KEEP-only | 799 | 61.5 | +51.4 | +58.8 | $+12,486 |
| KEEP-only recent | 606 | 60.1 | +53.3 | +66.3 | $+8,425 |

- KEEP strategies (23): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S411, S412
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-08T09:26:21.900750-04:00","date":"2026-10-08","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.0,"phases_s":{"reconcile":0.28},"signals":0,"placed":0,"equity":986833.26,"open_positions":11,"pending_orders":0,"open_lots":10,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"12219","github_run_id":"37784167171","status":"ok","data_quality":{"clean":{"n":1629,"win":48.56,"med":-24.24,"avg":38.83,"pnl":18601.83},"tainted":{"n":1965,"win":32.93,"med":-40.0,"avg":11.92,"pnl":-10172.28},"keep_only":{"n":799,"win":61.45,"med":51.39,"avg":58.79,"pnl":12486.45},"keep_only_recent":{"n":606,"win":60.07,"med":53.33,"avg":66.27,"pnl":8425.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:37:13  INFO      Mode: morning_prep
13:37:14  INFO        [prep_positions] 3/3 (3 valid)
13:37:14  INFO      Fetching tickers (universe=both)...
13:37:14  INFO        S&P 500: 503
13:37:14  INFO        MidCap 400: 400
13:37:14  INFO        Total: 902 tickers
13:37:15  INFO        [prep_universe] 40/899 (40 valid)
13:37:17  INFO        [prep_universe] 80/899 (80 valid)
13:37:18  INFO        [prep_universe] 120/899 (120 valid)
13:37:19  INFO        [prep_universe] 160/899 (160 valid)
13:37:20  INFO        [prep_universe] 200/899 (199 valid)
13:37:27  INFO        [prep_universe] 240/899 (238 valid)
13:37:41  INFO        [prep_universe] 280/899 (278 valid)
13:37:51  INFO        [prep_universe] 320/899 (318 valid)
13:38:04  INFO        [prep_universe] 360/899 (358 valid)
13:38:17  INFO        [prep_universe] 400/899 (398 valid)
13:38:27  INFO        [prep_universe] 440/899 (438 valid)
13:38:41  INFO        [prep_universe] 480/899 (477 valid)
13:38:51  INFO        [prep_universe] 520/899 (517 valid)
13:39:04  INFO        [prep_universe] 560/899 (557 valid)
13:39:15  INFO        [prep_universe] 600/899 (597 valid)
13:39:28  INFO        [prep_universe] 640/899 (637 valid)
13:39:41  INFO        [prep_universe] 680/899 (677 valid)
13:39:51  INFO        [prep_universe] 720/899 (717 valid)
13:40:04  INFO        [prep_universe] 760/899 (757 valid)
13:40:18  INFO        [prep_universe] 800/899 (797 valid)
13:40:28  INFO        [prep_universe] 840/899 (837 valid)
13:40:41  INFO        [prep_universe] 880/899 (877 valid)
13:40:45  INFO        [prep_universe] 899/899 (896 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:37 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.30|
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
|  Invested                                                       $100.83|
|  Open P&L                                                        $-0.12|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  KTOS     MomReversal     $33.58     $42.19   $42.10   -0.2%   $-0.07  |
|  NRG      EarningsDrift   $33.58     $107.50  $107.28  -0.2%   $-0.07  |
|  OC       MomReversal     $33.67     $113.39  $113.45  +0.1%   $+0.02  |
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
|  Universe scanned                                                   899|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-08T09:40:47.818788-04:00 share=25% ===
2026-10-08 09:40:47,818 INFO === options_live_micro LIVE 2026-10-08T09:40:47.818788-04:00 share=25% ===
Live account equity $224.54 cash $123.47 #225458845 options_level=3
2026-10-08 09:40:48,015 INFO Live account equity $224.54 cash $123.47 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-10-08 09:40:48,194 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-10-08 09:40:48,312 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=10 paper_keys=yes dry_run=False
  alpaca positions=11
  FLAG 5 lot(s) missing from Alpaca
    b65|S168|a25464a1 MARA261016C00011000
    b51|S396|2a51458e MARA261009C00010000
    b52|S397|59806b61 COIN261009C00190000
    b66|S163|d832ca5a COIN261009C00192500
    b6|S210|279a68c9 XOM261009C00167500
  reconcile: backfill exit b65|S168 MARA -54.8% fill=0.14
  reconcile: backfill exit b51|S396 MARA -52.6% fill=0.27
  reconcile: backfill exit b52|S397 COIN -28.4% fill=0.48
  reconcile: backfill exit b66|S163 COIN -95.7% fill=0.02
  reconcile: backfill exit b6|S210 XOM +214.9% fill=1.48
  State updated (attributed/cleared=5, leftover=0).
options_reconcile: done
Layout: controlled:77:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:77:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      77
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$987,367.76
  buying_power=$3,827,496.24 cash=$979,920.16
  open option orders: 4
    MARA261106C00011500 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
    MARA261023C00011000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
    MARA261030C00011500 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
    C261009C00131000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
  open option positions: 6
    C261009C00131000 qty=1 mkt=$5.00
    DKNG261009C00022500 qty=-1 mkt=$-10.00
    DKNG261016C00023500 qty=1 mkt=$0.00
    MARA261023C00011000 qty=1 mkt=$25.00
    MARA261030C00011500 qty=1 mkt=$27.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-10-08T09:40:51.225146-04:00 ===

[Run context]
Paper auth OK — equity $987364.26, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
S406-only twin b91 s406_only — S406 | TP+50%/SL-40% | paper edge test
Variation study: 75 lab/promising bucket(s) | cohort: 75 unique (S163, S164, S166, S167, S168, S169, S170, S171, S172, S175, S200, S201 … +63 more) | max 200 new entries/run
Dropped (no new entries; ex-reflected P&L): S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
Shared-OCC entry block ON (one lab lot per contract)
  EXIT [b421|lab0421_s365_w2_1005_1045_r2|S365] stop_loss (-100.0%) SELL blocked (uncovered/shared OCC) DKNG261016C00023500 x1: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
Protective stops: placed=0 upgraded=0 already=4 failed=1 (market-first)

[Scan + entries]
Scanning 117 symbols for [S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S204, S205, S206, S208, S210, S213, S214, S215, S219, S220, S221, S402, S403, S350, S352, S356, S357, S358, S359, S361, S362, S364, S365, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S395, S396, S397, S398, S404, S406, S409, S410, S411, S412, S413, S414, S415] …
Fetched daily bars for 113/117 symbols
```

---
