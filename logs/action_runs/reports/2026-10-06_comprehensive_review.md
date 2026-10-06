# Daily Comprehensive Action Review - 2026-10-06

_Auto-generated from GitHub Actions run output. Each run appends a summary; full stdout is in linked per-run log files._
## Run 20261006T130130Z

- UTC timestamp: `20261006T130130Z`
- GitHub run: [#11955](https://github.com/28twagg-ops/TradingBot/actions/runs/37467372646)
- Run id: `37467372646`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`13s`
- Full logs: `logs/action_runs/20261006T130130Z_live_bot.log`, `logs/action_runs/20261006T130130Z_live_options.log`, `logs/action_runs/20261006T130130Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1615 | 48.2 | -26.7 | +38.8 | $+18,271 |
| TAINTED | 1959 | 33.0 | -40.0 | +12.0 | $-10,116 |
| KEEP-only | 786 | 60.9 | +50.9 | +59.0 | $+12,135 |
| KEEP-only recent | 593 | 59.4 | +53.3 | +66.7 | $+8,074 |

- KEEP strategies (23): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S411, S412
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-06T09:01:36.736542-04:00","date":"2026-10-06","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.2,"phases_s":{"reconcile":0.51},"signals":0,"placed":0,"equity":987590.56,"open_positions":4,"pending_orders":0,"open_lots":3,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11955","github_run_id":"37467372646","status":"ok","data_quality":{"clean":{"n":1615,"win":48.24,"med":-26.67,"avg":38.81,"pnl":18270.83},"tainted":{"n":1959,"win":32.98,"med":-40.0,"avg":12.04,"pnl":-10116.28},"keep_only":{"n":786,"win":60.94,"med":50.87,"avg":58.97,"pnl":12135.45},"keep_only_recent":{"n":593,"win":59.36,"med":53.33,"avg":66.68,"pnl":8074.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
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
|  Equity                                                         $222.98|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $222.98|
|  Cash                                                           $222.98|
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
|  2026-10-05  SELL  LNT  MomReversal  $33.46  P&L $-0.11                |
|  2026-10-05  SELL  NCLH  EarningsDrift  $33.39  P&L $-0.19             |
|  2026-10-05  SELL  CMI  MomReversal  $33.40  P&L $-0.20                |
|  2026-10-02  SELL  NCLH  EarningsDrift  $33.63  P&L $+0.05             |
|  2026-10-02  SELL  CMS  MomReversal  $33.43  P&L $-0.17                |
|  2026-10-02  SELL  BA  MomReversal  $33.25  P&L $-0.35                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-06T09:01:33.543370-04:00 share=25% ===
2026-10-06 09:01:33,543 INFO === options_live_micro LIVE 2026-10-06T09:01:33.543370-04:00 share=25% ===
Live account equity $222.98 cash $222.98 #225458845 options_level=3
2026-10-06 09:01:33,760 INFO Live account equity $222.98 cash $222.98 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-10-06 09:01:33,818 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-10-06 09:01:33,877 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (166 earlier lines - see full log file)
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 295 | 21 |
| S164 | 339 | 25 |
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
| 2026-10-02 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-06
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |  1914 | WARN | <<<
| Missing exit records (post) |  1913 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     3 | INFO |
| Total closed lots           |  2685 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-06_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-06_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1615 med=-26.7% | TAINTED n=1959 med=-40.0% | KEEP-only n=786 med=+50.9% | KILL=21 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=222.98 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261006T130628Z

- UTC timestamp: `20261006T130628Z`
- GitHub run: [#11956](https://github.com/28twagg-ops/TradingBot/actions/runs/37468035316)
- Run id: `37468035316`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`10s`
- Full logs: `logs/action_runs/20261006T130628Z_live_bot.log`, `logs/action_runs/20261006T130628Z_live_options.log`, `logs/action_runs/20261006T130628Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1615 | 48.2 | -26.7 | +38.8 | $+18,271 |
| TAINTED | 1959 | 33.0 | -40.0 | +12.0 | $-10,116 |
| KEEP-only | 786 | 60.9 | +50.9 | +59.0 | $+12,135 |
| KEEP-only recent | 593 | 59.4 | +53.3 | +66.7 | $+8,074 |

- KEEP strategies (23): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S411, S412
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-06T09:06:33.093299-04:00","date":"2026-10-06","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.6,"phases_s":{"reconcile":0.08},"signals":0,"placed":0,"equity":987605.12,"open_positions":4,"pending_orders":0,"open_lots":3,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11956","github_run_id":"37468035316","status":"ok","data_quality":{"clean":{"n":1615,"win":48.24,"med":-26.67,"avg":38.81,"pnl":18270.83},"tainted":{"n":1959,"win":32.98,"med":-40.0,"avg":12.04,"pnl":-10116.28},"keep_only":{"n":786,"win":60.94,"med":50.87,"avg":58.97,"pnl":12135.45},"keep_only_recent":{"n":593,"win":59.36,"med":53.33,"avg":66.68,"pnl":8074.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:06:29  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $222.98|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $222.98|
|  Cash                                                           $222.98|
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
|  2026-10-05  SELL  LNT  MomReversal  $33.46  P&L $-0.11                |
|  2026-10-05  SELL  NCLH  EarningsDrift  $33.39  P&L $-0.19             |
|  2026-10-05  SELL  CMI  MomReversal  $33.40  P&L $-0.20                |
|  2026-10-02  SELL  NCLH  EarningsDrift  $33.63  P&L $+0.05             |
|  2026-10-02  SELL  CMS  MomReversal  $33.43  P&L $-0.17                |
|  2026-10-02  SELL  BA  MomReversal  $33.25  P&L $-0.35                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-06T09:06:30.962705-04:00 share=25% ===
2026-10-06 09:06:30,962 INFO === options_live_micro LIVE 2026-10-06T09:06:30.962705-04:00 share=25% ===
Live account equity $222.98 cash $222.98 #225458845 options_level=3
2026-10-06 09:06:31,001 INFO Live account equity $222.98 cash $222.98 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-10-06 09:06:31,007 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-10-06 09:06:31,014 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (166 earlier lines - see full log file)
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 295 | 21 |
| S164 | 339 | 25 |
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
| 2026-10-02 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-06
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |  1914 | WARN | <<<
| Missing exit records (post) |  1913 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     3 | INFO |
| Total closed lots           |  2685 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-06_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-06_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1615 med=-26.7% | TAINTED n=1959 med=-40.0% | KEEP-only n=786 med=+50.9% | KILL=21 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=222.98 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261006T131138Z

- UTC timestamp: `20261006T131138Z`
- GitHub run: [#11957](https://github.com/28twagg-ops/TradingBot/actions/runs/37468669401)
- Run id: `37468669401`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`13s`
- Full logs: `logs/action_runs/20261006T131138Z_live_bot.log`, `logs/action_runs/20261006T131138Z_live_options.log`, `logs/action_runs/20261006T131138Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1615 | 48.2 | -26.7 | +38.8 | $+18,271 |
| TAINTED | 1959 | 33.0 | -40.0 | +12.0 | $-10,116 |
| KEEP-only | 786 | 60.9 | +50.9 | +59.0 | $+12,135 |
| KEEP-only recent | 593 | 59.4 | +53.3 | +66.7 | $+8,074 |

- KEEP strategies (23): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S411, S412
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-06T09:11:43.435592-04:00","date":"2026-10-06","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.8,"phases_s":{"reconcile":0.13},"signals":0,"placed":0,"equity":987640.02,"open_positions":4,"pending_orders":0,"open_lots":3,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11957","github_run_id":"37468669401","status":"ok","data_quality":{"clean":{"n":1615,"win":48.24,"med":-26.67,"avg":38.81,"pnl":18270.83},"tainted":{"n":1959,"win":32.98,"med":-40.0,"avg":12.04,"pnl":-10116.28},"keep_only":{"n":786,"win":60.94,"med":50.87,"avg":58.97,"pnl":12135.45},"keep_only_recent":{"n":593,"win":59.36,"med":53.33,"avg":66.68,"pnl":8074.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:11:39  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $222.98|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $222.98|
|  Cash                                                           $222.98|
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
|  2026-10-05  SELL  LNT  MomReversal  $33.46  P&L $-0.11                |
|  2026-10-05  SELL  NCLH  EarningsDrift  $33.39  P&L $-0.19             |
|  2026-10-05  SELL  CMI  MomReversal  $33.40  P&L $-0.20                |
|  2026-10-02  SELL  NCLH  EarningsDrift  $33.63  P&L $+0.05             |
|  2026-10-02  SELL  CMS  MomReversal  $33.43  P&L $-0.17                |
|  2026-10-02  SELL  BA  MomReversal  $33.25  P&L $-0.35                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-06T09:11:40.795384-04:00 share=25% ===
2026-10-06 09:11:40,795 INFO === options_live_micro LIVE 2026-10-06T09:11:40.795384-04:00 share=25% ===
Live account equity $222.98 cash $222.98 #225458845 options_level=3
2026-10-06 09:11:40,850 INFO Live account equity $222.98 cash $222.98 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-10-06 09:11:40,861 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-10-06 09:11:40,872 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (166 earlier lines - see full log file)
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 295 | 21 |
| S164 | 339 | 25 |
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
| 2026-10-02 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-06
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |  1914 | WARN | <<<
| Missing exit records (post) |  1913 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     3 | INFO |
| Total closed lots           |  2685 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-06_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-06_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1615 med=-26.7% | TAINTED n=1959 med=-40.0% | KEEP-only n=786 med=+50.9% | KILL=21 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=222.98 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261006T131625Z

- UTC timestamp: `20261006T131625Z`
- GitHub run: [#11958](https://github.com/28twagg-ops/TradingBot/actions/runs/37469315438)
- Run id: `37469315438`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`11s`
- Full logs: `logs/action_runs/20261006T131625Z_live_bot.log`, `logs/action_runs/20261006T131625Z_live_options.log`, `logs/action_runs/20261006T131625Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1615 | 48.2 | -26.7 | +38.8 | $+18,271 |
| TAINTED | 1959 | 33.0 | -40.0 | +12.0 | $-10,116 |
| KEEP-only | 786 | 60.9 | +50.9 | +59.0 | $+12,135 |
| KEEP-only recent | 593 | 59.4 | +53.3 | +66.7 | $+8,074 |

- KEEP strategies (23): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S411, S412
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-06T09:16:30.397025-04:00","date":"2026-10-06","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.1,"phases_s":{"reconcile":0.43},"signals":0,"placed":0,"equity":987543.72,"open_positions":4,"pending_orders":0,"open_lots":3,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11958","github_run_id":"37469315438","status":"ok","data_quality":{"clean":{"n":1615,"win":48.24,"med":-26.67,"avg":38.81,"pnl":18270.83},"tainted":{"n":1959,"win":32.98,"med":-40.0,"avg":12.04,"pnl":-10116.28},"keep_only":{"n":786,"win":60.94,"med":50.87,"avg":58.97,"pnl":12135.45},"keep_only_recent":{"n":593,"win":59.36,"med":53.33,"avg":66.68,"pnl":8074.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:16:26  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $222.98|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $222.98|
|  Cash                                                           $222.98|
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
|  2026-10-05  SELL  LNT  MomReversal  $33.46  P&L $-0.11                |
|  2026-10-05  SELL  NCLH  EarningsDrift  $33.39  P&L $-0.19             |
|  2026-10-05  SELL  CMI  MomReversal  $33.40  P&L $-0.20                |
|  2026-10-02  SELL  NCLH  EarningsDrift  $33.63  P&L $+0.05             |
|  2026-10-02  SELL  CMS  MomReversal  $33.43  P&L $-0.17                |
|  2026-10-02  SELL  BA  MomReversal  $33.25  P&L $-0.35                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-06T09:16:27.654379-04:00 share=25% ===
2026-10-06 09:16:27,654 INFO === options_live_micro LIVE 2026-10-06T09:16:27.654379-04:00 share=25% ===
Live account equity $222.98 cash $222.98 #225458845 options_level=3
2026-10-06 09:16:27,834 INFO Live account equity $222.98 cash $222.98 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-10-06 09:16:27,896 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-10-06 09:16:27,952 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (166 earlier lines - see full log file)
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 295 | 21 |
| S164 | 339 | 25 |
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
| 2026-10-02 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-06
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |  1914 | WARN | <<<
| Missing exit records (post) |  1913 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     3 | INFO |
| Total closed lots           |  2685 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-06_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-06_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1615 med=-26.7% | TAINTED n=1959 med=-40.0% | KEEP-only n=786 med=+50.9% | KILL=21 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=222.98 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261006T132140Z

- UTC timestamp: `20261006T132140Z`
- GitHub run: [#11959](https://github.com/28twagg-ops/TradingBot/actions/runs/37469958927)
- Run id: `37469958927`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`13s`
- Full logs: `logs/action_runs/20261006T132140Z_live_bot.log`, `logs/action_runs/20261006T132140Z_live_options.log`, `logs/action_runs/20261006T132140Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1615 | 48.2 | -26.7 | +38.8 | $+18,271 |
| TAINTED | 1959 | 33.0 | -40.0 | +12.0 | $-10,116 |
| KEEP-only | 786 | 60.9 | +50.9 | +59.0 | $+12,135 |
| KEEP-only recent | 593 | 59.4 | +53.3 | +66.7 | $+8,074 |

- KEEP strategies (23): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S411, S412
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-06T09:21:46.311998-04:00","date":"2026-10-06","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.21},"signals":0,"placed":0,"equity":987607.05,"open_positions":4,"pending_orders":0,"open_lots":3,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11959","github_run_id":"37469958927","status":"ok","data_quality":{"clean":{"n":1615,"win":48.24,"med":-26.67,"avg":38.81,"pnl":18270.83},"tainted":{"n":1959,"win":32.98,"med":-40.0,"avg":12.04,"pnl":-10116.28},"keep_only":{"n":786,"win":60.94,"med":50.87,"avg":58.97,"pnl":12135.45},"keep_only_recent":{"n":593,"win":59.36,"med":53.33,"avg":66.68,"pnl":8074.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:21:42  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $222.98|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $222.98|
|  Cash                                                           $222.98|
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
|  2026-10-05  SELL  LNT  MomReversal  $33.46  P&L $-0.11                |
|  2026-10-05  SELL  NCLH  EarningsDrift  $33.39  P&L $-0.19             |
|  2026-10-05  SELL  CMI  MomReversal  $33.40  P&L $-0.20                |
|  2026-10-02  SELL  NCLH  EarningsDrift  $33.63  P&L $+0.05             |
|  2026-10-02  SELL  CMS  MomReversal  $33.43  P&L $-0.17                |
|  2026-10-02  SELL  BA  MomReversal  $33.25  P&L $-0.35                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-06T09:21:43.380584-04:00 share=25% ===
2026-10-06 09:21:43,380 INFO === options_live_micro LIVE 2026-10-06T09:21:43.380584-04:00 share=25% ===
Live account equity $222.98 cash $222.98 #225458845 options_level=3
2026-10-06 09:21:43,476 INFO Live account equity $222.98 cash $222.98 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-10-06 09:21:43,501 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-10-06 09:21:43,527 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (166 earlier lines - see full log file)
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 295 | 21 |
| S164 | 339 | 25 |
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
| 2026-10-02 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-06
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |  1914 | WARN | <<<
| Missing exit records (post) |  1913 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     3 | INFO |
| Total closed lots           |  2685 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-06_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-06_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1615 med=-26.7% | TAINTED n=1959 med=-40.0% | KEEP-only n=786 med=+50.9% | KILL=21 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=222.98 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261006T132617Z

- UTC timestamp: `20261006T132617Z`
- GitHub run: [#11960](https://github.com/28twagg-ops/TradingBot/actions/runs/37470617534)
- Run id: `37470617534`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`9s`
- Full logs: `logs/action_runs/20261006T132617Z_live_bot.log`, `logs/action_runs/20261006T132617Z_live_options.log`, `logs/action_runs/20261006T132617Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1615 | 48.2 | -26.7 | +38.8 | $+18,271 |
| TAINTED | 1959 | 33.0 | -40.0 | +12.0 | $-10,116 |
| KEEP-only | 786 | 60.9 | +50.9 | +59.0 | $+12,135 |
| KEEP-only recent | 593 | 59.4 | +53.3 | +66.7 | $+8,074 |

- KEEP strategies (23): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S411, S412
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-06T09:26:23.555893-04:00","date":"2026-10-06","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.8,"phases_s":{"reconcile":0.27},"signals":0,"placed":0,"equity":987501.3,"open_positions":4,"pending_orders":0,"open_lots":3,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11960","github_run_id":"37470617534","status":"ok","data_quality":{"clean":{"n":1615,"win":48.24,"med":-26.67,"avg":38.81,"pnl":18270.83},"tainted":{"n":1959,"win":32.98,"med":-40.0,"avg":12.04,"pnl":-10116.28},"keep_only":{"n":786,"win":60.94,"med":50.87,"avg":58.97,"pnl":12135.45},"keep_only_recent":{"n":593,"win":59.36,"med":53.33,"avg":66.68,"pnl":8074.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:26:19  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $222.98|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $222.98|
|  Cash                                                           $222.98|
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
|  2026-10-05  SELL  LNT  MomReversal  $33.46  P&L $-0.11                |
|  2026-10-05  SELL  NCLH  EarningsDrift  $33.39  P&L $-0.19             |
|  2026-10-05  SELL  CMI  MomReversal  $33.40  P&L $-0.20                |
|  2026-10-02  SELL  NCLH  EarningsDrift  $33.63  P&L $+0.05             |
|  2026-10-02  SELL  CMS  MomReversal  $33.43  P&L $-0.17                |
|  2026-10-02  SELL  BA  MomReversal  $33.25  P&L $-0.35                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-06T09:26:20.785063-04:00 share=25% ===
2026-10-06 09:26:20,785 INFO === options_live_micro LIVE 2026-10-06T09:26:20.785063-04:00 share=25% ===
Live account equity $222.98 cash $222.98 #225458845 options_level=3
2026-10-06 09:26:21,103 INFO Live account equity $222.98 cash $222.98 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-10-06 09:26:21,138 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-10-06 09:26:21,173 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (166 earlier lines - see full log file)
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 295 | 21 |
| S164 | 339 | 25 |
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
| 2026-10-02 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-06
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |  1914 | WARN | <<<
| Missing exit records (post) |  1913 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     3 | INFO |
| Total closed lots           |  2685 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-06_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-06_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1615 med=-26.7% | TAINTED n=1959 med=-40.0% | KEEP-only n=786 med=+50.9% | KILL=21 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=222.98 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261006T133128Z

- UTC timestamp: `20261006T133128Z`
- GitHub run: [#11961](https://github.com/28twagg-ops/TradingBot/actions/runs/37471280007)
- Run id: `37471280007`
- Live bot: exit=`0`, duration=`216s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20261006T133128Z_live_bot.log`, `logs/action_runs/20261006T133128Z_live_options.log`, `logs/action_runs/20261006T133128Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1615 | 48.2 | -26.7 | +38.8 | $+18,271 |
| TAINTED | 1959 | 33.0 | -40.0 | +12.0 | $-10,116 |
| KEEP-only | 786 | 60.9 | +50.9 | +59.0 | $+12,135 |
| KEEP-only recent | 593 | 59.4 | +53.3 | +66.7 | $+8,074 |

- KEEP strategies (23): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S411, S412
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-06T09:26:23.555893-04:00","date":"2026-10-06","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.8,"phases_s":{"reconcile":0.27},"signals":0,"placed":0,"equity":987501.3,"open_positions":4,"pending_orders":0,"open_lots":3,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11960","github_run_id":"37470617534","status":"ok","data_quality":{"clean":{"n":1615,"win":48.24,"med":-26.67,"avg":38.81,"pnl":18270.83},"tainted":{"n":1959,"win":32.98,"med":-40.0,"avg":12.04,"pnl":-10116.28},"keep_only":{"n":786,"win":60.94,"med":50.87,"avg":58.97,"pnl":12135.45},"keep_only_recent":{"n":593,"win":59.36,"med":53.33,"avg":66.68,"pnl":8074.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:31:29  INFO      Mode: morning_prep
13:31:30  INFO      Fetching tickers (universe=both)...
13:31:30  INFO        S&P 500: 503
13:31:30  INFO        MidCap 400: 400
13:31:30  INFO        Total: 903 tickers
13:31:31  INFO        [prep_universe] 40/903 (40 valid)
13:31:33  INFO        [prep_universe] 80/903 (80 valid)
13:31:34  INFO        [prep_universe] 120/903 (120 valid)
13:31:35  INFO        [prep_universe] 160/903 (160 valid)
13:31:37  INFO        [prep_universe] 200/903 (199 valid)
13:31:45  INFO        [prep_universe] 240/903 (238 valid)
13:31:55  INFO        [prep_universe] 280/903 (278 valid)
13:32:08  INFO        [prep_universe] 320/903 (318 valid)
13:32:21  INFO        [prep_universe] 360/903 (358 valid)
13:32:32  INFO        [prep_universe] 400/903 (398 valid)
13:32:45  INFO        [prep_universe] 440/903 (438 valid)
13:32:55  INFO        [prep_universe] 480/903 (478 valid)
13:33:08  INFO        [prep_universe] 520/903 (518 valid)
13:33:19  INFO        [prep_universe] 560/903 (558 valid)
13:33:32  INFO        [prep_universe] 600/903 (598 valid)
13:33:45  INFO        [prep_universe] 640/903 (638 valid)
13:33:55  INFO        [prep_universe] 680/903 (678 valid)
13:34:08  INFO        [prep_universe] 720/903 (718 valid)
13:34:19  INFO        [prep_universe] 760/903 (758 valid)
13:34:32  INFO        [prep_universe] 800/903 (798 valid)
13:34:45  INFO        [prep_universe] 840/903 (838 valid)
13:34:55  INFO        [prep_universe] 880/903 (878 valid)
13:35:02  INFO        [prep_universe] 903/903 (901 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $222.98|
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

```

### Paper options bot (tail)

```text

```

---

## Run 20261006T133649Z

- UTC timestamp: `20261006T133649Z`
- GitHub run: [#11962](https://github.com/28twagg-ops/TradingBot/actions/runs/37471948722)
- Run id: `37471948722`
- Live bot: exit=`0`, duration=`216s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20261006T133649Z_live_bot.log`, `logs/action_runs/20261006T133649Z_live_options.log`, `logs/action_runs/20261006T133649Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1615 | 48.2 | -26.7 | +38.8 | $+18,271 |
| TAINTED | 1959 | 33.0 | -40.0 | +12.0 | $-10,116 |
| KEEP-only | 786 | 60.9 | +50.9 | +59.0 | $+12,135 |
| KEEP-only recent | 593 | 59.4 | +53.3 | +66.7 | $+8,074 |

- KEEP strategies (23): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S411, S412
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-06T09:26:23.555893-04:00","date":"2026-10-06","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.8,"phases_s":{"reconcile":0.27},"signals":0,"placed":0,"equity":987501.3,"open_positions":4,"pending_orders":0,"open_lots":3,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11960","github_run_id":"37470617534","status":"ok","data_quality":{"clean":{"n":1615,"win":48.24,"med":-26.67,"avg":38.81,"pnl":18270.83},"tainted":{"n":1959,"win":32.98,"med":-40.0,"avg":12.04,"pnl":-10116.28},"keep_only":{"n":786,"win":60.94,"med":50.87,"avg":58.97,"pnl":12135.45},"keep_only_recent":{"n":593,"win":59.36,"med":53.33,"avg":66.68,"pnl":8074.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:36:50  INFO      Mode: morning_prep
13:36:51  INFO      Fetching tickers (universe=both)...
13:36:51  INFO        S&P 500: 503
13:36:51  INFO        MidCap 400: 400
13:36:51  INFO        Total: 903 tickers
13:36:52  INFO        [prep_universe] 40/903 (40 valid)
13:36:53  INFO        [prep_universe] 80/903 (80 valid)
13:36:55  INFO        [prep_universe] 120/903 (120 valid)
13:36:56  INFO        [prep_universe] 160/903 (160 valid)
13:36:57  INFO        [prep_universe] 200/903 (199 valid)
13:37:05  INFO        [prep_universe] 240/903 (238 valid)
13:37:15  INFO        [prep_universe] 280/903 (278 valid)
13:37:28  INFO        [prep_universe] 320/903 (318 valid)
13:37:41  INFO        [prep_universe] 360/903 (358 valid)
13:37:51  INFO        [prep_universe] 400/903 (398 valid)
13:38:04  INFO        [prep_universe] 440/903 (438 valid)
13:38:18  INFO        [prep_universe] 480/903 (478 valid)
13:38:28  INFO        [prep_universe] 520/903 (518 valid)
13:38:41  INFO        [prep_universe] 560/903 (558 valid)
13:38:53  INFO        [prep_universe] 600/903 (598 valid)
13:39:03  INFO        [prep_universe] 640/903 (638 valid)
13:39:17  INFO        [prep_universe] 680/903 (678 valid)
13:39:30  INFO        [prep_universe] 720/903 (718 valid)
13:39:40  INFO        [prep_universe] 760/903 (758 valid)
13:39:52  INFO        [prep_universe] 800/903 (798 valid)
13:40:05  INFO        [prep_universe] 840/903 (838 valid)
13:40:16  INFO        [prep_universe] 880/903 (878 valid)
13:40:23  INFO        [prep_universe] 903/903 (901 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $222.98|
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
=== options_live_micro LIVE 2026-10-06T09:40:26.212831-04:00 share=25% ===
2026-10-06 09:40:26,212 INFO === options_live_micro LIVE 2026-10-06T09:40:26.212831-04:00 share=25% ===
Live account equity $222.98 cash $222.98 #225458845 options_level=3
2026-10-06 09:40:26,271 INFO Live account equity $222.98 cash $222.98 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-10-06 09:40:26,305 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-10-06 09:40:26,330 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=3 paper_keys=yes dry_run=False
  alpaca positions=9
  No missing lots.
options_reconcile: done
Layout: controlled:77:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:77:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      77
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$987,155.63
  buying_power=$3,826,858.58 cash=$979,691.52
  open option orders: 2
    NKE261023C00035000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
    NKE261016C00034000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
  open option positions: 4
    DKNG261009C00022500 qty=-1 mkt=$-3.00
    DKNG261016C00023500 qty=1 mkt=$3.00
    NKE261016C00034000 qty=1 mkt=$55.00
    NKE261023C00035000 qty=1 mkt=$45.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-10-06T09:40:28.921887-04:00 ===

[Run context]
Paper auth OK — equity $987142.32, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
S406-only twin b91 s406_only — S406 | TP+50%/SL-40% | paper edge test
Variation study: 75 lab/promising bucket(s) | cohort: 75 unique (S163, S164, S166, S167, S168, S169, S170, S171, S172, S175, S200, S201 … +63 more) | max 200 new entries/run
Dropped (no new entries; ex-reflected P&L): S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
Shared-OCC entry block ON (one lab lot per contract)
  EXIT [b421|lab0421_s365_w2_1005_1045_r2|S365] stop_loss (-93.0%) SELL blocked (uncovered/shared OCC) DKNG261016C00023500 x1: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
Protective stops: placed=0 upgraded=0 already=2 failed=1 (market-first)

[Scan + entries]
Scanning 117 symbols for [S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S204, S205, S206, S208, S210, S213, S214, S215, S219, S220, S221, S402, S403, S350, S352, S356, S357, S358, S359, S361, S362, S364, S365, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S395, S396, S397, S398, S404, S406, S409, S410, S411, S412, S413, S414, S415] …
Fetched daily bars for 113/117 symbols
```

---
