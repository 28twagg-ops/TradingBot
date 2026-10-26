# Daily Comprehensive Action Review - 2026-10-26

_Auto-generated from GitHub Actions run output. Each run appends a summary; full stdout is in linked per-run log files._
## Run 20261026T130145Z

- UTC timestamp: `20261026T130145Z`
- GitHub run: [#13798](https://github.com/28twagg-ops/TradingBot/actions/runs/40326889510)
- Run id: `40326889510`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`12s`
- Full logs: `logs/action_runs/20261026T130145Z_live_bot.log`, `logs/action_runs/20261026T130145Z_live_options.log`, `logs/action_runs/20261026T130145Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1740 | 48.0 | -30.1 | +35.9 | $+18,391 |
| TAINTED | 2041 | 31.7 | -41.2 | +9.7 | $-11,840 |
| KEEP-only | 835 | 60.1 | +50.0 | +51.9 | $+12,073 |
| KEEP-only recent | 650 | 58.9 | +52.8 | +58.1 | $+8,564 |

- KEEP strategies (23): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S403, S404, S406, S410, S411
- KILL strategies (22): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-26T09:01:51.345316-04:00","date":"2026-10-26","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.5,"phases_s":{"reconcile":0.48},"signals":0,"placed":0,"equity":992898.84,"open_positions":3,"pending_orders":0,"open_lots":3,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"13798","github_run_id":"40326889510","status":"ok","data_quality":{"clean":{"n":1740,"win":48.05,"med":-30.07,"avg":35.89,"pnl":18390.83},"tainted":{"n":2041,"win":31.75,"med":-41.18,"avg":9.67,"pnl":-11840.28},"keep_only":{"n":835,"win":60.12,"med":50.0,"avg":51.9,"pnl":12073.45},"keep_only_recent":{"n":650,"win":58.92,"med":52.83,"avg":58.08,"pnl":8564.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:01:46  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.17|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $227.17|
|  Cash                                                           $193.21|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $33.96|
|  Open P&L                                                        $-0.20|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (1 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  WFRD     EarningsDrift   $33.96     $86.76   $86.25   -0.6%   $-0.20  |
|                                                                        |
|  Total invested                                                  $33.96|
|  Total open P&L                                                  $-0.20|
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
|  2026-10-23  SELL  WFRD  EarningsDrift  $34.24  P&L $+0.08             |
|  2026-10-23  SELL  ALGM  MomReversal  $2.54  P&L $-0.02                |
|  2026-10-23  SELL  ADI  Pullback50  $33.94  P&L $-0.27                 |
|  2026-10-23  SELL  FITB  Pullback50  $34.22  P&L $-0.00                |
|  2026-10-23  SELL  BMY  Pullback50  $34.20  P&L $-0.01                 |
|  2026-10-23  SELL  TECH  Pullback50  $34.29  P&L $-0.03                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-26T09:01:48.545540-04:00 share=25% ===
2026-10-26 09:01:48,545 INFO === options_live_micro LIVE 2026-10-26T09:01:48.545540-04:00 share=25% ===
Live account equity $227.17 cash $193.21 #225458845 options_level=3
2026-10-26 09:01:48,755 INFO Live account equity $227.17 cash $193.21 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-10-26 09:01:48,812 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-10-26 09:01:48,869 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (187 earlier lines - see full log file)
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
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-26
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1917 | WARN | <<<
| Missing exit records (post) |  1917 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     3 | INFO |
| Total closed lots           |  2892 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1740 med=-30.1% | TAINTED n=2041 med=-41.2% | KEEP-only n=835 med=+50.0% | KILL=22 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.17 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261026T130650Z

- UTC timestamp: `20261026T130650Z`
- GitHub run: [#13799](https://github.com/28twagg-ops/TradingBot/actions/runs/40327560250)
- Run id: `40327560250`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`13s`
- Full logs: `logs/action_runs/20261026T130650Z_live_bot.log`, `logs/action_runs/20261026T130650Z_live_options.log`, `logs/action_runs/20261026T130650Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1740 | 48.0 | -30.1 | +35.9 | $+18,391 |
| TAINTED | 2041 | 31.7 | -41.2 | +9.7 | $-11,840 |
| KEEP-only | 835 | 60.1 | +50.0 | +51.9 | $+12,073 |
| KEEP-only recent | 650 | 58.9 | +52.8 | +58.1 | $+8,564 |

- KEEP strategies (23): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S403, S404, S406, S410, S411
- KILL strategies (22): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-26T09:06:55.083554-04:00","date":"2026-10-26","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.09},"signals":0,"placed":0,"equity":992763.83,"open_positions":3,"pending_orders":0,"open_lots":3,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"13799","github_run_id":"40327560250","status":"ok","data_quality":{"clean":{"n":1740,"win":48.05,"med":-30.07,"avg":35.89,"pnl":18390.83},"tainted":{"n":2041,"win":31.75,"med":-41.18,"avg":9.67,"pnl":-11840.28},"keep_only":{"n":835,"win":60.12,"med":50.0,"avg":51.9,"pnl":12073.45},"keep_only_recent":{"n":650,"win":58.92,"med":52.83,"avg":58.08,"pnl":8564.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:06:51  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.17|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $227.17|
|  Cash                                                           $193.21|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $33.96|
|  Open P&L                                                        $-0.20|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (1 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  WFRD     EarningsDrift   $33.96     $86.76   $86.25   -0.6%   $-0.20  |
|                                                                        |
|  Total invested                                                  $33.96|
|  Total open P&L                                                  $-0.20|
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
|  2026-10-23  SELL  WFRD  EarningsDrift  $34.24  P&L $+0.08             |
|  2026-10-23  SELL  ALGM  MomReversal  $2.54  P&L $-0.02                |
|  2026-10-23  SELL  ADI  Pullback50  $33.94  P&L $-0.27                 |
|  2026-10-23  SELL  FITB  Pullback50  $34.22  P&L $-0.00                |
|  2026-10-23  SELL  BMY  Pullback50  $34.20  P&L $-0.01                 |
|  2026-10-23  SELL  TECH  Pullback50  $34.29  P&L $-0.03                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-26T09:06:52.386933-04:00 share=25% ===
2026-10-26 09:06:52,387 INFO === options_live_micro LIVE 2026-10-26T09:06:52.386933-04:00 share=25% ===
Live account equity $227.17 cash $193.21 #225458845 options_level=3
2026-10-26 09:06:52,430 INFO Live account equity $227.17 cash $193.21 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-10-26 09:06:52,439 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-10-26 09:06:52,446 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (187 earlier lines - see full log file)
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
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-26
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1917 | WARN | <<<
| Missing exit records (post) |  1917 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     3 | INFO |
| Total closed lots           |  2892 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1740 med=-30.1% | TAINTED n=2041 med=-41.2% | KEEP-only n=835 med=+50.0% | KILL=22 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.17 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261026T131140Z

- UTC timestamp: `20261026T131140Z`
- GitHub run: [#13800](https://github.com/28twagg-ops/TradingBot/actions/runs/40328240786)
- Run id: `40328240786`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`9s`
- Full logs: `logs/action_runs/20261026T131140Z_live_bot.log`, `logs/action_runs/20261026T131140Z_live_options.log`, `logs/action_runs/20261026T131140Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1740 | 48.0 | -30.1 | +35.9 | $+18,391 |
| TAINTED | 2041 | 31.7 | -41.2 | +9.7 | $-11,840 |
| KEEP-only | 835 | 60.1 | +50.0 | +51.9 | $+12,073 |
| KEEP-only recent | 650 | 58.9 | +52.8 | +58.1 | $+8,564 |

- KEEP strategies (23): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S403, S404, S406, S410, S411
- KILL strategies (22): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-26T09:11:44.779393-04:00","date":"2026-10-26","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.33},"signals":0,"placed":0,"equity":992998.58,"open_positions":3,"pending_orders":0,"open_lots":3,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"13800","github_run_id":"40328240786","status":"ok","data_quality":{"clean":{"n":1740,"win":48.05,"med":-30.07,"avg":35.89,"pnl":18390.83},"tainted":{"n":2041,"win":31.75,"med":-41.18,"avg":9.67,"pnl":-11840.28},"keep_only":{"n":835,"win":60.12,"med":50.0,"avg":51.9,"pnl":12073.45},"keep_only_recent":{"n":650,"win":58.92,"med":52.83,"avg":58.08,"pnl":8564.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:11:41  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.17|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $227.17|
|  Cash                                                           $193.21|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $33.96|
|  Open P&L                                                        $-0.20|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (1 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  WFRD     EarningsDrift   $33.96     $86.76   $86.25   -0.6%   $-0.20  |
|                                                                        |
|  Total invested                                                  $33.96|
|  Total open P&L                                                  $-0.20|
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
|  2026-10-23  SELL  WFRD  EarningsDrift  $34.24  P&L $+0.08             |
|  2026-10-23  SELL  ALGM  MomReversal  $2.54  P&L $-0.02                |
|  2026-10-23  SELL  ADI  Pullback50  $33.94  P&L $-0.27                 |
|  2026-10-23  SELL  FITB  Pullback50  $34.22  P&L $-0.00                |
|  2026-10-23  SELL  BMY  Pullback50  $34.20  P&L $-0.01                 |
|  2026-10-23  SELL  TECH  Pullback50  $34.29  P&L $-0.03                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-26T09:11:42.182659-04:00 share=25% ===
2026-10-26 09:11:42,182 INFO === options_live_micro LIVE 2026-10-26T09:11:42.182659-04:00 share=25% ===
Live account equity $227.17 cash $193.21 #225458845 options_level=3
2026-10-26 09:11:42,658 INFO Live account equity $227.17 cash $193.21 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-10-26 09:11:42,689 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-10-26 09:11:42,719 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (187 earlier lines - see full log file)
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
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-26
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1917 | WARN | <<<
| Missing exit records (post) |  1917 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     3 | INFO |
| Total closed lots           |  2892 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1740 med=-30.1% | TAINTED n=2041 med=-41.2% | KEEP-only n=835 med=+50.0% | KILL=22 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.17 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261026T131652Z

- UTC timestamp: `20261026T131652Z`
- GitHub run: [#13801](https://github.com/28twagg-ops/TradingBot/actions/runs/40328948986)
- Run id: `40328948986`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`9s`
- Full logs: `logs/action_runs/20261026T131652Z_live_bot.log`, `logs/action_runs/20261026T131652Z_live_options.log`, `logs/action_runs/20261026T131652Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1740 | 48.0 | -30.1 | +35.9 | $+18,391 |
| TAINTED | 2041 | 31.7 | -41.2 | +9.7 | $-11,840 |
| KEEP-only | 835 | 60.1 | +50.0 | +51.9 | $+12,073 |
| KEEP-only recent | 650 | 58.9 | +52.8 | +58.1 | $+8,564 |

- KEEP strategies (23): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S403, S404, S406, S410, S411
- KILL strategies (22): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-26T09:16:57.011436-04:00","date":"2026-10-26","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.24},"signals":0,"placed":0,"equity":992972.33,"open_positions":3,"pending_orders":0,"open_lots":3,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"13801","github_run_id":"40328948986","status":"ok","data_quality":{"clean":{"n":1740,"win":48.05,"med":-30.07,"avg":35.89,"pnl":18390.83},"tainted":{"n":2041,"win":31.75,"med":-41.18,"avg":9.67,"pnl":-11840.28},"keep_only":{"n":835,"win":60.12,"med":50.0,"avg":51.9,"pnl":12073.45},"keep_only_recent":{"n":650,"win":58.92,"med":52.83,"avg":58.08,"pnl":8564.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:16:53  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.17|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $227.17|
|  Cash                                                           $193.21|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $33.96|
|  Open P&L                                                        $-0.20|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (1 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  WFRD     EarningsDrift   $33.96     $86.76   $86.25   -0.6%   $-0.20  |
|                                                                        |
|  Total invested                                                  $33.96|
|  Total open P&L                                                  $-0.20|
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
|  2026-10-23  SELL  WFRD  EarningsDrift  $34.24  P&L $+0.08             |
|  2026-10-23  SELL  ALGM  MomReversal  $2.54  P&L $-0.02                |
|  2026-10-23  SELL  ADI  Pullback50  $33.94  P&L $-0.27                 |
|  2026-10-23  SELL  FITB  Pullback50  $34.22  P&L $-0.00                |
|  2026-10-23  SELL  BMY  Pullback50  $34.20  P&L $-0.01                 |
|  2026-10-23  SELL  TECH  Pullback50  $34.29  P&L $-0.03                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-26T09:16:54.657553-04:00 share=25% ===
2026-10-26 09:16:54,657 INFO === options_live_micro LIVE 2026-10-26T09:16:54.657553-04:00 share=25% ===
Live account equity $227.17 cash $193.21 #225458845 options_level=3
2026-10-26 09:16:54,821 INFO Live account equity $227.17 cash $193.21 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-10-26 09:16:54,863 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-10-26 09:16:54,905 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (187 earlier lines - see full log file)
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
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-26
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1917 | WARN | <<<
| Missing exit records (post) |  1917 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     3 | INFO |
| Total closed lots           |  2892 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1740 med=-30.1% | TAINTED n=2041 med=-41.2% | KEEP-only n=835 med=+50.0% | KILL=22 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.17 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261026T132642Z

- UTC timestamp: `20261026T132642Z`
- GitHub run: [#13803](https://github.com/28twagg-ops/TradingBot/actions/runs/40330373329)
- Run id: `40330373329`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`13s`
- Full logs: `logs/action_runs/20261026T132642Z_live_bot.log`, `logs/action_runs/20261026T132642Z_live_options.log`, `logs/action_runs/20261026T132642Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1740 | 48.0 | -30.1 | +35.9 | $+18,391 |
| TAINTED | 2041 | 31.7 | -41.2 | +9.7 | $-11,840 |
| KEEP-only | 835 | 60.1 | +50.0 | +51.9 | $+12,073 |
| KEEP-only recent | 650 | 58.9 | +52.8 | +58.1 | $+8,564 |

- KEEP strategies (23): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S403, S404, S406, S410, S411
- KILL strategies (22): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-26T09:26:47.594123-04:00","date":"2026-10-26","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.09},"signals":0,"placed":0,"equity":993099.33,"open_positions":3,"pending_orders":0,"open_lots":3,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"13803","github_run_id":"40330373329","status":"ok","data_quality":{"clean":{"n":1740,"win":48.05,"med":-30.07,"avg":35.89,"pnl":18390.83},"tainted":{"n":2041,"win":31.75,"med":-41.18,"avg":9.67,"pnl":-11840.28},"keep_only":{"n":835,"win":60.12,"med":50.0,"avg":51.9,"pnl":12073.45},"keep_only_recent":{"n":650,"win":58.92,"med":52.83,"avg":58.08,"pnl":8564.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:26:43  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.17|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $227.17|
|  Cash                                                           $193.21|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $33.96|
|  Open P&L                                                        $-0.20|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (1 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  WFRD     EarningsDrift   $33.96     $86.76   $86.25   -0.6%   $-0.20  |
|                                                                        |
|  Total invested                                                  $33.96|
|  Total open P&L                                                  $-0.20|
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
|  2026-10-23  SELL  WFRD  EarningsDrift  $34.24  P&L $+0.08             |
|  2026-10-23  SELL  ALGM  MomReversal  $2.54  P&L $-0.02                |
|  2026-10-23  SELL  ADI  Pullback50  $33.94  P&L $-0.27                 |
|  2026-10-23  SELL  FITB  Pullback50  $34.22  P&L $-0.00                |
|  2026-10-23  SELL  BMY  Pullback50  $34.20  P&L $-0.01                 |
|  2026-10-23  SELL  TECH  Pullback50  $34.29  P&L $-0.03                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-26T09:26:44.943146-04:00 share=25% ===
2026-10-26 09:26:44,943 INFO === options_live_micro LIVE 2026-10-26T09:26:44.943146-04:00 share=25% ===
Live account equity $227.17 cash $193.21 #225458845 options_level=3
2026-10-26 09:26:45,007 INFO Live account equity $227.17 cash $193.21 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-10-26 09:26:45,015 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-10-26 09:26:45,024 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (187 earlier lines - see full log file)
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
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-26
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1917 | WARN | <<<
| Missing exit records (post) |  1917 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     3 | INFO |
| Total closed lots           |  2892 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1740 med=-30.1% | TAINTED n=2041 med=-41.2% | KEEP-only n=835 med=+50.0% | KILL=22 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.17 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261026T132907Z

- UTC timestamp: `20261026T132907Z`
- GitHub run: [#13802](https://github.com/28twagg-ops/TradingBot/actions/runs/40329664625)
- Run id: `40329664625`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`66s`
- Full logs: `logs/action_runs/20261026T132907Z_live_bot.log`, `logs/action_runs/20261026T132907Z_live_options.log`, `logs/action_runs/20261026T132907Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1740 | 48.0 | -30.1 | +35.9 | $+18,391 |
| TAINTED | 2041 | 31.7 | -41.2 | +9.7 | $-11,840 |
| KEEP-only | 835 | 60.1 | +50.0 | +51.9 | $+12,073 |
| KEEP-only recent | 650 | 58.9 | +52.8 | +58.1 | $+8,564 |

- KEEP strategies (23): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S403, S404, S406, S410, S411
- KILL strategies (22): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-26T09:29:12.676441-04:00","date":"2026-10-26","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":51.7,"phases_s":{"reconcile":0.1,"cancel":0.04,"manage":0.38,"protective_stops":0.06,"scan":49.79,"entries":0.56},"signals":49,"placed":0,"equity":993132.33,"open_positions":3,"pending_orders":0,"open_lots":3,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":["S430:AMD","S432:AMD","S430:CRWD","S431:CRWD","S432:CRWD","S430:PANW","S432:PANW","S430:DDOG"],"github_run":"13802","github_run_id":"40329664625","status":"ok","data_quality":{"clean":{"n":1740,"win":48.05,"med":-30.07,"avg":35.89,"pnl":18390.83},"tainted":{"n":2041,"win":31.75,"med":-41.18,"avg":9.67,"pnl":-11840.28},"keep_only":{"n":835,"win":60.12,"med":50.0,"avg":51.9,"pnl":12073.45},"keep_only_recent":{"n":650,"win":58.92,"med":52.83,"avg":58.08,"pnl":8564.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:29:08  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:29 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.17|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $227.17|
|  Cash                                                           $193.21|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $33.96|
|  Open P&L                                                        $-0.20|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (1 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  WFRD     EarningsDrift   $33.96     $86.76   $86.25   -0.6%   $-0.20  |
|                                                                        |
|  Total invested                                                  $33.96|
|  Total open P&L                                                  $-0.20|
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
|  2026-10-23  SELL  WFRD  EarningsDrift  $34.24  P&L $+0.08             |
|  2026-10-23  SELL  ALGM  MomReversal  $2.54  P&L $-0.02                |
|  2026-10-23  SELL  ADI  Pullback50  $33.94  P&L $-0.27                 |
|  2026-10-23  SELL  FITB  Pullback50  $34.22  P&L $-0.00                |
|  2026-10-23  SELL  BMY  Pullback50  $34.20  P&L $-0.01                 |
|  2026-10-23  SELL  TECH  Pullback50  $34.29  P&L $-0.03                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-26T09:29:09.502303-04:00 share=25% ===
2026-10-26 09:29:09,502 INFO === options_live_micro LIVE 2026-10-26T09:29:09.502303-04:00 share=25% ===
Live account equity $227.17 cash $193.21 #225458845 options_level=3
2026-10-26 09:29:09,565 INFO Live account equity $227.17 cash $193.21 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-10-26 09:29:09,599 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-10-26 09:29:09,621 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (199 earlier lines - see full log file)
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
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-26
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1917 | WARN | <<<
| Missing exit records (post) |  1917 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     3 | INFO |
| Total closed lots           |  2892 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1740 med=-30.1% | TAINTED n=2041 med=-41.2% | KEEP-only n=835 med=+50.0% | KILL=22 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.17 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261026T133214Z

- UTC timestamp: `20261026T133214Z`
- GitHub run: [#13804](https://github.com/28twagg-ops/TradingBot/actions/runs/40331101561)
- Run id: `40331101561`
- Live bot: exit=`0`, duration=`217s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20261026T133214Z_live_bot.log`, `logs/action_runs/20261026T133214Z_live_options.log`, `logs/action_runs/20261026T133214Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1740 | 48.0 | -30.1 | +35.9 | $+18,391 |
| TAINTED | 2041 | 31.7 | -41.2 | +9.7 | $-11,840 |
| KEEP-only | 835 | 60.1 | +50.0 | +51.9 | $+12,073 |
| KEEP-only recent | 650 | 58.9 | +52.8 | +58.1 | $+8,564 |

- KEEP strategies (23): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S403, S404, S406, S410, S411
- KILL strategies (22): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-26T09:26:47.594123-04:00","date":"2026-10-26","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.09},"signals":0,"placed":0,"equity":993099.33,"open_positions":3,"pending_orders":0,"open_lots":3,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"13803","github_run_id":"40330373329","status":"ok","data_quality":{"clean":{"n":1740,"win":48.05,"med":-30.07,"avg":35.89,"pnl":18390.83},"tainted":{"n":2041,"win":31.75,"med":-41.18,"avg":9.67,"pnl":-11840.28},"keep_only":{"n":835,"win":60.12,"med":50.0,"avg":51.9,"pnl":12073.45},"keep_only_recent":{"n":650,"win":58.92,"med":52.83,"avg":58.08,"pnl":8564.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
... (98 earlier lines - see full log file)
13:33:42  INFO        [prep_universe] 480/902 (477 valid)
13:33:52  INFO        [prep_universe] 520/902 (517 valid)
13:34:05  INFO        [prep_universe] 560/902 (557 valid)
13:34:18  INFO        [prep_universe] 600/902 (597 valid)
13:34:29  INFO        [prep_universe] 640/902 (637 valid)
13:34:42  INFO        [prep_universe] 680/902 (677 valid)
13:34:55  INFO        [prep_universe] 720/902 (717 valid)
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/utils.py:568: Pandas4Warning: The inplace keyword in DataFrame.sort_index is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  quotes.sort_index(inplace=True)
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/utils.py:585: Pandas4Warning: The inplace keyword in DataFrame.set_index is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  dividends.set_index("date", inplace=True)
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/utils.py:587: Pandas4Warning: The inplace keyword in DataFrame.sort_index is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  dividends.sort_index(inplace=True)
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/utils.py:514: Pandas4Warning: The inplace keyword in DataFrame.drop is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  df.drop(
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/utils.py:518: Pandas4Warning: The inplace keyword in DataFrame.rename is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  df.rename(columns={
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/multi.py:220: Pandas4Warning: The inplace keyword in DataFrame.rename is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  data.rename(columns=ctx.isins, inplace=True)
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/multi.py:224: Pandas4Warning: The inplace keyword in DataFrame.sort_index is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  data.sort_index(level=0, axis=1, inplace=True)
13:35:05  INFO        [prep_universe] 760/902 (757 valid)
13:35:18  INFO        [prep_universe] 800/902 (797 valid)
13:35:28  INFO        [prep_universe] 840/902 (837 valid)
13:35:41  INFO        [prep_universe] 880/902 (877 valid)
13:35:48  INFO        [prep_universe] 902/902 (899 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:32 UTC|
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
|  Open positions                                                       1|
|  Invested                                                        $34.19|
|  Open P&L                                                        $+0.03|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  WFRD     EarningsDrift   $34.19     $86.76   $86.85   +0.1%   $+0.03  |
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
|  Signal candidates                                                   30|
|  Universe scanned                                                   902|
+========================================================================+
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20261026T133758Z

- UTC timestamp: `20261026T133758Z`
- GitHub run: [#13805](https://github.com/28twagg-ops/TradingBot/actions/runs/40331842507)
- Run id: `40331842507`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20261026T133758Z_live_bot.log`, `logs/action_runs/20261026T133758Z_live_options.log`, `logs/action_runs/20261026T133758Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1740 | 48.0 | -30.1 | +35.9 | $+18,391 |
| TAINTED | 2041 | 31.7 | -41.2 | +9.7 | $-11,840 |
| KEEP-only | 835 | 60.1 | +50.0 | +51.9 | $+12,073 |
| KEEP-only recent | 650 | 58.9 | +52.8 | +58.1 | $+8,564 |

- KEEP strategies (23): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S403, S404, S406, S410, S411
- KILL strategies (22): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-26T09:29:12.676441-04:00","date":"2026-10-26","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":51.7,"phases_s":{"reconcile":0.1,"cancel":0.04,"manage":0.38,"protective_stops":0.06,"scan":49.79,"entries":0.56},"signals":49,"placed":0,"equity":993132.33,"open_positions":3,"pending_orders":0,"open_lots":3,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":["S430:AMD","S432:AMD","S430:CRWD","S431:CRWD","S432:CRWD","S430:PANW","S432:PANW","S430:DDOG"],"github_run":"13802","github_run_id":"40329664625","status":"ok","data_quality":{"clean":{"n":1740,"win":48.05,"med":-30.07,"avg":35.89,"pnl":18390.83},"tainted":{"n":2041,"win":31.75,"med":-41.18,"avg":9.67,"pnl":-11840.28},"keep_only":{"n":835,"win":60.12,"med":50.0,"avg":51.9,"pnl":12073.45},"keep_only_recent":{"n":650,"win":58.92,"med":52.83,"avg":58.08,"pnl":8564.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
... (20 earlier lines - see full log file)
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  df.rename(columns={
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/utils.py:568: Pandas4Warning: The inplace keyword in DataFrame.sort_index is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  quotes.sort_index(inplace=True)
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/utils.py:514: Pandas4Warning: The inplace keyword in DataFrame.drop is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  df.drop(
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/utils.py:518: Pandas4Warning: The inplace keyword in DataFrame.rename is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  df.rename(columns={
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/multi.py:220: Pandas4Warning: The inplace keyword in DataFrame.rename is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  data.rename(columns=ctx.isins, inplace=True)
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/multi.py:224: Pandas4Warning: The inplace keyword in DataFrame.sort_index is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  data.sort_index(level=0, axis=1, inplace=True)
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/multi.py:224: Pandas4Warning: The inplace keyword in DataFrame.sort_index is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  data.sort_index(level=0, axis=1, inplace=True)
13:38:03  INFO        [prep_universe] 80/902 (80 valid)
13:38:04  INFO        [prep_universe] 120/902 (120 valid)
13:38:05  INFO        [prep_universe] 160/902 (160 valid)
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/utils.py:568: Pandas4Warning: The inplace keyword in DataFrame.sort_index is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  quotes.sort_index(inplace=True)
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/utils.py:514: Pandas4Warning: The inplace keyword in DataFrame.drop is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  df.drop(
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/utils.py:518: Pandas4Warning: The inplace keyword in DataFrame.rename is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  df.rename(columns={
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/multi.py:220: Pandas4Warning: The inplace keyword in DataFrame.rename is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  data.rename(columns=ctx.isins, inplace=True)
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/multi.py:224: Pandas4Warning: The inplace keyword in DataFrame.sort_index is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  data.sort_index(level=0, axis=1, inplace=True)
13:38:07  INFO        [prep_universe] 200/902 (199 valid)
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/utils.py:568: Pandas4Warning: The inplace keyword in DataFrame.sort_index is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  quotes.sort_index(inplace=True)
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/utils.py:514: Pandas4Warning: The inplace keyword in DataFrame.drop is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  df.drop(
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/utils.py:518: Pandas4Warning: The inplace keyword in DataFrame.rename is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  df.rename(columns={
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/multi.py:220: Pandas4Warning: The inplace keyword in DataFrame.rename is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  data.rename(columns=ctx.isins, inplace=True)
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/multi.py:224: Pandas4Warning: The inplace keyword in DataFrame.sort_index is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  data.sort_index(level=0, axis=1, inplace=True)
13:38:14  INFO        [prep_universe] 240/902 (238 valid)
13:38:27  INFO        [prep_universe] 280/902 (278 valid)
13:38:38  INFO        [prep_universe] 320/902 (318 valid)
13:38:51  INFO        [prep_universe] 360/902 (358 valid)
13:39:04  INFO        [prep_universe] 400/902 (398 valid)
13:39:14  INFO        [prep_universe] 440/902 (438 valid)
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/utils.py:568: Pandas4Warning: The inplace keyword in DataFrame.sort_index is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  quotes.sort_index(inplace=True)
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/utils.py:514: Pandas4Warning: The inplace keyword in DataFrame.drop is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  df.drop(
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/utils.py:518: Pandas4Warning: The inplace keyword in DataFrame.rename is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  df.rename(columns={
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/multi.py:220: Pandas4Warning: The inplace keyword in DataFrame.rename is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  data.rename(columns=ctx.isins, inplace=True)
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/multi.py:224: Pandas4Warning: The inplace keyword in DataFrame.sort_index is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  data.sort_index(level=0, axis=1, inplace=True)
13:39:27  INFO        [prep_universe] 480/902 (477 valid)
13:39:38  INFO        [prep_universe] 520/902 (517 valid)
13:39:51  INFO        [prep_universe] 560/902 (557 valid)
13:40:01  INFO        [prep_universe] 600/902 (597 valid)
13:40:14  INFO        [prep_universe] 640/902 (637 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20261026T134242Z

- UTC timestamp: `20261026T134242Z`
- GitHub run: [#13806](https://github.com/28twagg-ops/TradingBot/actions/runs/40332582216)
- Run id: `40332582216`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20261026T134242Z_live_bot.log`, `logs/action_runs/20261026T134242Z_live_options.log`, `logs/action_runs/20261026T134242Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1740 | 48.0 | -30.1 | +35.9 | $+18,391 |
| TAINTED | 2041 | 31.7 | -41.2 | +9.7 | $-11,840 |
| KEEP-only | 835 | 60.1 | +50.0 | +51.9 | $+12,073 |
| KEEP-only recent | 650 | 58.9 | +52.8 | +58.1 | $+8,564 |

- KEEP strategies (23): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S403, S404, S406, S410, S411
- KILL strategies (22): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-26T09:26:47.594123-04:00","date":"2026-10-26","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.09},"signals":0,"placed":0,"equity":993099.33,"open_positions":3,"pending_orders":0,"open_lots":3,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"13803","github_run_id":"40330373329","status":"ok","data_quality":{"clean":{"n":1740,"win":48.05,"med":-30.07,"avg":35.89,"pnl":18390.83},"tainted":{"n":2041,"win":31.75,"med":-41.18,"avg":9.67,"pnl":-11840.28},"keep_only":{"n":835,"win":60.12,"med":50.0,"avg":51.9,"pnl":12073.45},"keep_only_recent":{"n":650,"win":58.92,"med":52.83,"avg":58.08,"pnl":8564.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
... (46 earlier lines - see full log file)
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/utils.py:514: Pandas4Warning: The inplace keyword in DataFrame.drop is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  df.drop(
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/utils.py:518: Pandas4Warning: The inplace keyword in DataFrame.rename is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  df.rename(columns={
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/multi.py:220: Pandas4Warning: The inplace keyword in DataFrame.rename is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  data.rename(columns=ctx.isins, inplace=True)
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/multi.py:224: Pandas4Warning: The inplace keyword in DataFrame.sort_index is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  data.sort_index(level=0, axis=1, inplace=True)
13:42:49  INFO        [prep_universe] 200/902 (199 valid)
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/utils.py:568: Pandas4Warning: The inplace keyword in DataFrame.sort_index is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  quotes.sort_index(inplace=True)
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/utils.py:514: Pandas4Warning: The inplace keyword in DataFrame.drop is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  df.drop(
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/utils.py:518: Pandas4Warning: The inplace keyword in DataFrame.rename is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  df.rename(columns={
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/multi.py:220: Pandas4Warning: The inplace keyword in DataFrame.rename is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  data.rename(columns=ctx.isins, inplace=True)
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/multi.py:224: Pandas4Warning: The inplace keyword in DataFrame.sort_index is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  data.sort_index(level=0, axis=1, inplace=True)
13:42:59  INFO        [prep_universe] 240/902 (238 valid)
13:43:12  INFO        [prep_universe] 280/902 (278 valid)
13:43:21  INFO        [prep_universe] 320/902 (318 valid)
13:43:34  INFO        [prep_universe] 360/902 (358 valid)
13:43:47  INFO        [prep_universe] 400/902 (398 valid)
13:44:00  INFO        [prep_universe] 440/902 (438 valid)
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/utils.py:568: Pandas4Warning: The inplace keyword in DataFrame.sort_index is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  quotes.sort_index(inplace=True)
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/utils.py:514: Pandas4Warning: The inplace keyword in DataFrame.drop is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  df.drop(
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/utils.py:518: Pandas4Warning: The inplace keyword in DataFrame.rename is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  df.rename(columns={
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/multi.py:220: Pandas4Warning: The inplace keyword in DataFrame.rename is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  data.rename(columns=ctx.isins, inplace=True)
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/multi.py:224: Pandas4Warning: The inplace keyword in DataFrame.sort_index is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  data.sort_index(level=0, axis=1, inplace=True)
13:44:10  INFO        [prep_universe] 480/902 (477 valid)
13:44:22  INFO        [prep_universe] 520/902 (517 valid)
13:44:35  INFO        [prep_universe] 560/902 (557 valid)
13:44:48  INFO        [prep_universe] 600/902 (597 valid)
13:44:57  INFO        [prep_universe] 640/902 (637 valid)
13:45:10  INFO        [prep_universe] 680/902 (677 valid)
13:45:23  INFO        [prep_universe] 720/902 (717 valid)
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/utils.py:568: Pandas4Warning: The inplace keyword in DataFrame.sort_index is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  quotes.sort_index(inplace=True)
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/utils.py:585: Pandas4Warning: The inplace keyword in DataFrame.set_index is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  dividends.set_index("date", inplace=True)
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/utils.py:587: Pandas4Warning: The inplace keyword in DataFrame.sort_index is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  dividends.sort_index(inplace=True)
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/utils.py:514: Pandas4Warning: The inplace keyword in DataFrame.drop is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  df.drop(
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/utils.py:518: Pandas4Warning: The inplace keyword in DataFrame.rename is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  df.rename(columns={
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/multi.py:220: Pandas4Warning: The inplace keyword in DataFrame.rename is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  data.rename(columns=ctx.isins, inplace=True)
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/multi.py:224: Pandas4Warning: The inplace keyword in DataFrame.sort_index is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  data.sort_index(level=0, axis=1, inplace=True)
13:45:33  INFO        [prep_universe] 760/902 (757 valid)
13:45:46  INFO        [prep_universe] 800/902 (797 valid)
13:45:59  INFO        [prep_universe] 840/902 (837 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20261026T134810Z

- UTC timestamp: `20261026T134810Z`
- GitHub run: [#13807](https://github.com/28twagg-ops/TradingBot/actions/runs/40333321231)
- Run id: `40333321231`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20261026T134810Z_live_bot.log`, `logs/action_runs/20261026T134810Z_live_options.log`, `logs/action_runs/20261026T134810Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1740 | 48.0 | -30.1 | +35.9 | $+18,391 |
| TAINTED | 2041 | 31.7 | -41.2 | +9.7 | $-11,840 |
| KEEP-only | 835 | 60.1 | +50.0 | +51.9 | $+12,073 |
| KEEP-only recent | 650 | 58.9 | +52.8 | +58.1 | $+8,564 |

- KEEP strategies (23): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S403, S404, S406, S410, S411
- KILL strategies (22): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-26T09:29:12.676441-04:00","date":"2026-10-26","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":51.7,"phases_s":{"reconcile":0.1,"cancel":0.04,"manage":0.38,"protective_stops":0.06,"scan":49.79,"entries":0.56},"signals":49,"placed":0,"equity":993132.33,"open_positions":3,"pending_orders":0,"open_lots":3,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":["S430:AMD","S432:AMD","S430:CRWD","S431:CRWD","S432:CRWD","S430:PANW","S432:PANW","S430:DDOG"],"github_run":"13802","github_run_id":"40329664625","status":"ok","data_quality":{"clean":{"n":1740,"win":48.05,"med":-30.07,"avg":35.89,"pnl":18390.83},"tainted":{"n":2041,"win":31.75,"med":-41.18,"avg":9.67,"pnl":-11840.28},"keep_only":{"n":835,"win":60.12,"med":50.0,"avg":51.9,"pnl":12073.45},"keep_only_recent":{"n":650,"win":58.92,"med":52.83,"avg":58.08,"pnl":8564.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
... (24 earlier lines - see full log file)
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/multi.py:220: Pandas4Warning: The inplace keyword in DataFrame.rename is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  data.rename(columns=ctx.isins, inplace=True)
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/multi.py:224: Pandas4Warning: The inplace keyword in DataFrame.sort_index is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  data.sort_index(level=0, axis=1, inplace=True)
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/utils.py:568: Pandas4Warning: The inplace keyword in DataFrame.sort_index is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  quotes.sort_index(inplace=True)
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/utils.py:514: Pandas4Warning: The inplace keyword in DataFrame.drop is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  df.drop(
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/utils.py:518: Pandas4Warning: The inplace keyword in DataFrame.rename is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  df.rename(columns={
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/multi.py:220: Pandas4Warning: The inplace keyword in DataFrame.rename is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  data.rename(columns=ctx.isins, inplace=True)
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/multi.py:224: Pandas4Warning: The inplace keyword in DataFrame.sort_index is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  data.sort_index(level=0, axis=1, inplace=True)
13:48:36  INFO        [universe] 80/903 (80 valid)
13:48:37  INFO        [universe] 120/903 (120 valid)
13:48:38  INFO        [universe] 160/903 (160 valid)
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/utils.py:568: Pandas4Warning: The inplace keyword in DataFrame.sort_index is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  quotes.sort_index(inplace=True)
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/utils.py:514: Pandas4Warning: The inplace keyword in DataFrame.drop is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  df.drop(
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/utils.py:518: Pandas4Warning: The inplace keyword in DataFrame.rename is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  df.rename(columns={
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/multi.py:220: Pandas4Warning: The inplace keyword in DataFrame.rename is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  data.rename(columns=ctx.isins, inplace=True)
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/multi.py:224: Pandas4Warning: The inplace keyword in DataFrame.sort_index is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  data.sort_index(level=0, axis=1, inplace=True)
13:48:39  INFO        [universe] 200/903 (199 valid)
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/utils.py:568: Pandas4Warning: The inplace keyword in DataFrame.sort_index is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  quotes.sort_index(inplace=True)
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/utils.py:514: Pandas4Warning: The inplace keyword in DataFrame.drop is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  df.drop(
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/utils.py:518: Pandas4Warning: The inplace keyword in DataFrame.rename is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  df.rename(columns={
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/multi.py:220: Pandas4Warning: The inplace keyword in DataFrame.rename is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  data.rename(columns=ctx.isins, inplace=True)
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/multi.py:224: Pandas4Warning: The inplace keyword in DataFrame.sort_index is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  data.sort_index(level=0, axis=1, inplace=True)
13:48:49  INFO        [universe] 240/903 (238 valid)
13:48:59  INFO        [universe] 280/903 (278 valid)
13:49:12  INFO        [universe] 320/903 (318 valid)
13:49:24  INFO        [universe] 360/903 (358 valid)
13:49:37  INFO        [universe] 400/903 (398 valid)
13:49:47  INFO        [universe] 440/903 (438 valid)
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/utils.py:568: Pandas4Warning: The inplace keyword in DataFrame.sort_index is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  quotes.sort_index(inplace=True)
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/utils.py:514: Pandas4Warning: The inplace keyword in DataFrame.drop is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  df.drop(
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/utils.py:518: Pandas4Warning: The inplace keyword in DataFrame.rename is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  df.rename(columns={
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/multi.py:220: Pandas4Warning: The inplace keyword in DataFrame.rename is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  data.rename(columns=ctx.isins, inplace=True)
/opt/hostedtoolcache/Python/3.11.17/x64/lib/python3.11/site-packages/yfinance/multi.py:224: Pandas4Warning: The inplace keyword in DataFrame.sort_index is deprecated and will be removed in a future version (PDEP-8).
See https://pandas.pydata.org/docs/dev/whatsnew/v3.1.0.html#deprecation-inplace for more details.
  data.sort_index(level=0, axis=1, inplace=True)
13:50:01  INFO        [universe] 480/903 (477 valid)
13:50:11  INFO        [universe] 520/903 (517 valid)
13:50:24  INFO        [universe] 560/903 (557 valid)
13:50:37  INFO        [universe] 600/903 (597 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20261026T135230Z

- UTC timestamp: `20261026T135230Z`
- GitHub run: [#13808](https://github.com/28twagg-ops/TradingBot/actions/runs/40334065805)
- Run id: `40334065805`
- Live bot: exit=`0`, duration=`34s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`63s`
- Full logs: `logs/action_runs/20261026T135230Z_live_bot.log`, `logs/action_runs/20261026T135230Z_live_options.log`, `logs/action_runs/20261026T135230Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1740 | 48.0 | -30.1 | +35.9 | $+18,391 |
| TAINTED | 2043 | 31.7 | -41.5 | +9.6 | $-11,895 |
| KEEP-only | 835 | 60.1 | +50.0 | +51.9 | $+12,073 |
| KEEP-only recent | 650 | 58.9 | +52.8 | +58.1 | $+8,564 |

- KEEP strategies (23): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S403, S404, S406, S410, S411
- KILL strategies (22): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-26T09:53:07.848879-04:00","date":"2026-10-26","mode":"entry+manage","header":"entry+manage (2 new)","elapsed_s":50.7,"phases_s":{"reconcile":0.12,"cancel":0.03,"manage":0.15,"protective_stops":0.02,"scan":49.44,"entries":0.29,"reconcile2":0.08},"signals":126,"placed":2,"equity":993324.29,"open_positions":2,"pending_orders":1,"open_lots":2,"submitted_today":2,"filled_today":1,"unattributed_contracts":0,"top_signals":["S430:NVDA","S432:NVDA","S210:TSLA","S430:TSLA","S432:TSLA","S164:COIN","S168:COIN","S167:COIN"],"github_run":"13808","github_run_id":"40334065805","status":"ok","data_quality":{"clean":{"n":1740,"win":48.05,"med":-30.07,"avg":35.89,"pnl":18390.83},"tainted":{"n":2043,"win":31.72,"med":-41.46,"avg":9.61,"pnl":-11895.28},"keep_only":{"n":835,"win":60.12,"med":50.0,"avg":51.9,"pnl":12073.45},"keep_only_recent":{"n":650,"win":58.92,"med":52.83,"avg":58.08,"pnl":8564.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
... (102 earlier lines - see full log file)
|  ROIV     Pullback50      eq     $36.67   55.2   -1.68   50MA bounce (+|
|  SLAB     Pullback50      eq     $221.66  38.2   -2.46   50MA bounce (+|
|  UMBF     Pullback50      eq     $136.85  65.8   -2.99   50MA bounce (-|
|  UNM      Pullback50      eq     $92.50   52.4   -2.63   50MA bounce (+|
|                                                                        |
+========================================================================+

+========================================================================+
|                              ENTRY ORDERS                              |
+========================================================================+
|    ENTER [eq] ABT  Pullback50                                    $34.09|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    ENTER [eq] AES  Pullback50                                    $34.09|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    ENTER [eq] AME  Pullback50                                    $34.09|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    SKIP [eq] COF  Pullback50                                      cap 3|
|    SKIP [eq] JCI  Pullback50                                      cap 3|
|    SKIP [eq] NDSN  Pullback50                                     cap 3|
|    SKIP [eq] PRU  Pullback50                                      cap 3|13:53:03  INFO        place_all_stops: checking 3 positions...
13:53:03  INFO        STOP skipped ABT: fractional (0.3291 shares) — software exit will handle it
13:53:03  INFO        STOP-MARKET placed AES  qty=2 (pos=2.2724)  stop=$14.92  id=2411c37e-60e6-46f5-9f5e-3b8d819026c4
13:53:03  INFO        STOP skipped AME: fractional (0.1401 shares) — software exit will handle it
13:53:03  INFO        Daily log -> logs/daily/2026-10-26.md
13:53:03  INFO        Dashboard written → logs/dashboard.md

|    SKIP [eq] RF  Pullback50                                       cap 3|
|    SKIP [eq] SYF  Pullback50                                      cap 3|
|    SKIP [eq] USB  Pullback50                                      cap 3|
|    SKIP [eq] VTR  Pullback50                                      cap 3|
|    SKIP [eq] AHR  Pullback50                                      cap 3|
|    SKIP [eq] ATR  Pullback50                                      cap 3|
|    SKIP [eq] AVNT  Pullback50                                     cap 3|
|    SKIP [eq] CFR  Pullback50                                      cap 3|
|    SKIP [eq] CHE  Pullback50                                      cap 3|
|    SKIP [eq] CNO  Pullback50                                      cap 3|
|    SKIP [eq] EGP  Pullback50                                      cap 3|
|    SKIP [eq] GEF  Pullback50                                      cap 3|
|    SKIP [eq] HWC  Pullback50                                      cap 3|
|    SKIP [eq] MSA  Pullback50                                      cap 3|
|    SKIP [eq] MTG  Pullback50                                      cap 3|
|    SKIP [eq] NOV  Pullback50                                      cap 3|
|    SKIP [eq] ONB  Pullback50                                      cap 3|
|    SKIP [eq] ROIV  Pullback50                                     cap 3|
|    SKIP [eq] SLAB  Pullback50                                     cap 3|
|    SKIP [eq] UMBF  Pullback50                                     cap 3|
|    SKIP [eq] UNM  Pullback50                                      cap 3|

+========================================================================+
|                         BUY FILL CONFIRMATION                          |
+========================================================================+
|  Pending submits                                                      3|
+------------------------------------------------------------------------+
|  ABT                                                  still unconfirmed|
|  AES                                                  still unconfirmed|
|  AME                                                  still unconfirmed|
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
|  Strategy   RubberBand + GapDown (display only — schedule not enforced)|
|  Scanned                                                              0|
|  Signals                                                             28|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  3 unconfirmed|
|  Exits                                                                0|
|  Open pos                                                             3|
|  Equity                                                         $227.17|
|  Cash                                                           $125.00|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-26T09:53:04.846203-04:00 share=25% ===
2026-10-26 09:53:04,846 INFO === options_live_micro LIVE 2026-10-26T09:53:04.846203-04:00 share=25% ===
Live account equity $227.15 cash $125.00 #225458845 options_level=3
2026-10-26 09:53:05,096 INFO Live account equity $227.15 cash $125.00 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-10-26 09:53:05,129 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-10-26 09:53:05,147 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (207 earlier lines - see full log file)
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
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-26
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1917 | WARN | <<<
| Missing exit records (post) |  1917 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     2 | INFO |
| Total closed lots           |  2894 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1740 med=-30.1% | TAINTED n=2043 med=-41.5% | KEEP-only n=835 med=+50.0% | KILL=22 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.17 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261026T135647Z

- UTC timestamp: `20261026T135647Z`
- GitHub run: [#13809](https://github.com/28twagg-ops/TradingBot/actions/runs/40334812596)
- Run id: `40334812596`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`52s`
- Full logs: `logs/action_runs/20261026T135647Z_live_bot.log`, `logs/action_runs/20261026T135647Z_live_options.log`, `logs/action_runs/20261026T135647Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1740 | 48.0 | -30.1 | +35.9 | $+18,391 |
| TAINTED | 2043 | 31.7 | -41.5 | +9.6 | $-11,895 |
| KEEP-only | 835 | 60.1 | +50.0 | +51.9 | $+12,073 |
| KEEP-only recent | 650 | 58.9 | +52.8 | +58.1 | $+8,564 |

- KEEP strategies (23): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S403, S404, S406, S410, S411
- KILL strategies (22): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-26T09:56:52.529364-04:00","date":"2026-10-26","mode":"entry+manage","header":"entry+manage (1 new)","elapsed_s":39.9,"phases_s":{"reconcile":0.12,"cancel":0.04,"manage":0.35,"protective_stops":0.07,"scan":38.43,"entries":0.23,"reconcile2":0.1},"signals":126,"placed":1,"equity":993386.23,"open_positions":4,"pending_orders":1,"open_lots":3,"submitted_today":3,"filled_today":2,"unattributed_contracts":1,"top_signals":["S430:NVDA","S432:NVDA","S210:TSLA","S430:TSLA","S432:TSLA","S164:COIN","S168:COIN","S167:COIN"],"github_run":"13809","github_run_id":"40334812596","status":"ok","data_quality":{"clean":{"n":1740,"win":48.05,"med":-30.07,"avg":35.89,"pnl":18390.83},"tainted":{"n":2043,"win":31.72,"med":-41.46,"avg":9.61,"pnl":-11895.28},"keep_only":{"n":835,"win":60.12,"med":50.0,"avg":51.9,"pnl":12073.45},"keep_only_recent":{"n":650,"win":58.92,"med":52.83,"avg":58.08,"pnl":8564.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:56:48  INFO      Mode: morning_scan
13:56:48  INFO      Morning scan already completed today (2026-10-26T13:53:04.001785Z) — exits-only pass
13:56:48  INFO        Daily log -> logs/daily/2026-10-26.md
13:56:48  INFO        Daily log reconciled -> logs/daily/2026-10-26.md (1 ledger rows)
13:56:48  INFO        place_all_stops: checking 3 positions...
13:56:48  INFO        STOP skipped ABT: fractional (0.3291 shares) — software exit will handle it
13:56:48  INFO        STOP already live AES @ $14.92
13:56:48  INFO        STOP skipped AME: fractional (0.1401 shares) — software exit will handle it
13:56:49  INFO        [positions] 3/3 (3 valid)
13:56:49  INFO        Daily log -> logs/daily/2026-10-26.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_SCAN|
|  Time                                                         13:56 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.20|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ABT  P&L -0.1%  $-0.05                                            HOLD|
|  AES  P&L -0.0%  $-0.01                                            HOLD|
|  AME  P&L +0.1%  $+0.02                                            HOLD|
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
=== options_live_micro LIVE 2026-10-26T09:56:49.952029-04:00 share=25% ===
2026-10-26 09:56:49,952 INFO === options_live_micro LIVE 2026-10-26T09:56:49.952029-04:00 share=25% ===
Live account equity $227.20 cash $125.00 #225458845 options_level=3
2026-10-26 09:56:50,009 INFO Live account equity $227.20 cash $125.00 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-10-26 09:56:50,043 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-10-26 09:56:50,066 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (207 earlier lines - see full log file)
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
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-26
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1917 | WARN | <<<
| Missing exit records (post) |  1917 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     3 | INFO |
| Total closed lots           |  2894 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1740 med=-30.1% | TAINTED n=2043 med=-41.5% | KEEP-only n=835 med=+50.0% | KILL=22 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.22 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261026T140136Z

- UTC timestamp: `20261026T140136Z`
- GitHub run: [#13810](https://github.com/28twagg-ops/TradingBot/actions/runs/40335578252)
- Run id: `40335578252`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`32s`
- Full logs: `logs/action_runs/20261026T140136Z_live_bot.log`, `logs/action_runs/20261026T140136Z_live_options.log`, `logs/action_runs/20261026T140136Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1740 | 48.0 | -30.1 | +35.9 | $+18,391 |
| TAINTED | 2043 | 31.7 | -41.5 | +9.6 | $-11,895 |
| KEEP-only | 835 | 60.1 | +50.0 | +51.9 | $+12,073 |
| KEEP-only recent | 650 | 58.9 | +52.8 | +58.1 | $+8,564 |

- KEEP strategies (23): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S403, S404, S406, S410, S411
- KILL strategies (22): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-26T10:01:41.796429-04:00","date":"2026-10-26","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":23.3,"phases_s":{"reconcile":0.38,"cancel":0.13,"manage":1.22,"protective_stops":0.37,"scan":20.48,"entries":0.08},"signals":126,"placed":0,"equity":993500.29,"open_positions":4,"pending_orders":0,"open_lots":4,"submitted_today":3,"filled_today":3,"unattributed_contracts":0,"top_signals":["S430:NVDA","S432:NVDA","S210:TSLA","S430:TSLA","S432:TSLA","S164:COIN","S168:COIN","S167:COIN"],"github_run":"13810","github_run_id":"40335578252","status":"ok","data_quality":{"clean":{"n":1740,"win":48.05,"med":-30.07,"avg":35.89,"pnl":18390.83},"tainted":{"n":2043,"win":31.72,"med":-41.46,"avg":9.61,"pnl":-11895.28},"keep_only":{"n":835,"win":60.12,"med":50.0,"avg":51.9,"pnl":12073.45},"keep_only_recent":{"n":650,"win":58.92,"med":52.83,"avg":58.08,"pnl":8564.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:01:36  INFO      Mode: exits
14:01:37  INFO        Daily log -> logs/daily/2026-10-26.md
14:01:37  INFO        Daily log reconciled -> logs/daily/2026-10-26.md (1 ledger rows)
14:01:37  INFO        place_all_stops: checking 3 positions...
14:01:37  INFO        STOP skipped ABT: fractional (0.3291 shares) — software exit will handle it
14:01:37  INFO        STOP already live AES @ $14.92
14:01:37  INFO        STOP skipped AME: fractional (0.1401 shares) — software exit will handle it
14:01:37  INFO        [positions] 3/3 (3 valid)
14:01:38  INFO        Daily log -> logs/daily/2026-10-26.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.31|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AES  P&L -0.1%  $-0.02                                            HOLD|
|  AME  P&L -0.0%  $-0.01                                            HOLD|
|  ABT  P&L +0.3%  $+0.10                                            HOLD|
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
=== options_live_micro LIVE 2026-10-26T10:01:38.832855-04:00 share=25% ===
2026-10-26 10:01:38,832 INFO === options_live_micro LIVE 2026-10-26T10:01:38.832855-04:00 share=25% ===
Live account equity $227.30 cash $125.00 #225458845 options_level=3
2026-10-26 10:01:39,031 INFO Live account equity $227.30 cash $125.00 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-10-26 10:01:39,203 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-10-26 10:01:39,315 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (202 earlier lines - see full log file)
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
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-26
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1917 | WARN | <<<
| Missing exit records (post) |  1917 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     4 | INFO |
| Total closed lots           |  2894 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1740 med=-30.1% | TAINTED n=2043 med=-41.5% | KEEP-only n=835 med=+50.0% | KILL=22 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.3 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261026T140656Z

- UTC timestamp: `20261026T140656Z`
- GitHub run: [#13811](https://github.com/28twagg-ops/TradingBot/actions/runs/40336321830)
- Run id: `40336321830`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`66s`
- Full logs: `logs/action_runs/20261026T140656Z_live_bot.log`, `logs/action_runs/20261026T140656Z_live_options.log`, `logs/action_runs/20261026T140656Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1740 | 48.0 | -30.1 | +35.9 | $+18,391 |
| TAINTED | 2043 | 31.7 | -41.5 | +9.6 | $-11,895 |
| KEEP-only | 835 | 60.1 | +50.0 | +51.9 | $+12,073 |
| KEEP-only recent | 650 | 58.9 | +52.8 | +58.1 | $+8,564 |

- KEEP strategies (23): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S403, S404, S406, S410, S411
- KILL strategies (22): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-26T10:07:02.558247-04:00","date":"2026-10-26","mode":"entry+manage","header":"entry+manage (8 new)","elapsed_s":51.2,"phases_s":{"reconcile":0.2,"cancel":0.05,"manage":1.7,"protective_stops":0.16,"scan":42.86,"entries":4.71,"reconcile2":0.33},"signals":126,"placed":8,"equity":993783.2,"open_positions":9,"pending_orders":3,"open_lots":9,"submitted_today":11,"filled_today":8,"unattributed_contracts":0,"top_signals":["S430:NVDA","S432:NVDA","S210:TSLA","S430:TSLA","S432:TSLA","S164:COIN","S168:COIN","S167:COIN"],"github_run":"13811","github_run_id":"40336321830","status":"ok","data_quality":{"clean":{"n":1740,"win":48.05,"med":-30.07,"avg":35.89,"pnl":18390.83},"tainted":{"n":2043,"win":31.72,"med":-41.46,"avg":9.61,"pnl":-11895.28},"keep_only":{"n":835,"win":60.12,"med":50.0,"avg":51.9,"pnl":12073.45},"keep_only_recent":{"n":650,"win":58.92,"med":52.83,"avg":58.08,"pnl":8564.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:06:57  INFO      Mode: exits
14:06:58  INFO        Daily log -> logs/daily/2026-10-26.md
14:06:58  INFO        Daily log reconciled -> logs/daily/2026-10-26.md (1 ledger rows)
14:06:58  INFO        place_all_stops: checking 3 positions...
14:06:58  INFO        STOP skipped ABT: fractional (0.3291 shares) — software exit will handle it
14:06:58  INFO        STOP already live AES @ $14.92
14:06:58  INFO        STOP skipped AME: fractional (0.1401 shares) — software exit will handle it
14:06:58  INFO        [positions] 3/3 (3 valid)
14:06:58  INFO        Daily log -> logs/daily/2026-10-26.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.27|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L -0.3%  $-0.11                                            HOLD|
|  AES  P&L -0.2%  $-0.06                                            HOLD|
|  ABT  P&L +0.6%  $+0.20                                            HOLD|
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
=== options_live_micro LIVE 2026-10-26T10:06:59.268119-04:00 share=25% ===
2026-10-26 10:06:59,268 INFO === options_live_micro LIVE 2026-10-26T10:06:59.268119-04:00 share=25% ===
Live account equity $227.27 cash $125.00 #225458845 options_level=3
2026-10-26 10:06:59,381 INFO Live account equity $227.27 cash $125.00 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-10-26 10:06:59,462 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-10-26 10:06:59,516 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (217 earlier lines - see full log file)
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
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-26
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1917 | WARN | <<<
| Missing exit records (post) |  1917 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     9 | INFO |
| Total closed lots           |  2894 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1740 med=-30.1% | TAINTED n=2043 med=-41.5% | KEEP-only n=835 med=+50.0% | KILL=22 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.27 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261026T141135Z

- UTC timestamp: `20261026T141135Z`
- GitHub run: [#13812](https://github.com/28twagg-ops/TradingBot/actions/runs/40337097451)
- Run id: `40337097451`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`63s`
- Full logs: `logs/action_runs/20261026T141135Z_live_bot.log`, `logs/action_runs/20261026T141135Z_live_options.log`, `logs/action_runs/20261026T141135Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1740 | 48.0 | -30.1 | +35.9 | $+18,391 |
| TAINTED | 2043 | 31.7 | -41.5 | +9.6 | $-11,895 |
| KEEP-only | 835 | 60.1 | +50.0 | +51.9 | $+12,073 |
| KEEP-only recent | 650 | 58.9 | +52.8 | +58.1 | $+8,564 |

- KEEP strategies (23): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S403, S404, S406, S410, S411
- KILL strategies (22): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-26T10:11:40.305808-04:00","date":"2026-10-26","mode":"entry+manage","header":"entry+manage (1 new)","elapsed_s":50.3,"phases_s":{"reconcile":0.13,"cancel":0.02,"manage":1.53,"protective_stops":0.11,"scan":45.88,"entries":1.78,"reconcile2":0.12},"signals":126,"placed":1,"equity":993637.9,"open_positions":10,"pending_orders":3,"open_lots":10,"submitted_today":12,"filled_today":9,"unattributed_contracts":0,"top_signals":["S430:NVDA","S432:NVDA","S210:TSLA","S430:TSLA","S432:TSLA","S164:COIN","S168:COIN","S167:COIN"],"github_run":"13812","github_run_id":"40337097451","status":"ok","data_quality":{"clean":{"n":1740,"win":48.05,"med":-30.07,"avg":35.89,"pnl":18390.83},"tainted":{"n":2043,"win":31.72,"med":-41.46,"avg":9.61,"pnl":-11895.28},"keep_only":{"n":835,"win":60.12,"med":50.0,"avg":51.9,"pnl":12073.45},"keep_only_recent":{"n":650,"win":58.92,"med":52.83,"avg":58.08,"pnl":8564.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:11:36  INFO      Mode: exits
14:11:36  INFO        Daily log -> logs/daily/2026-10-26.md
14:11:36  INFO        Daily log reconciled -> logs/daily/2026-10-26.md (1 ledger rows)
14:11:36  INFO        place_all_stops: checking 3 positions...
14:11:36  INFO        STOP skipped ABT: fractional (0.3291 shares) — software exit will handle it
14:11:36  INFO        STOP already live AES @ $14.92
14:11:36  INFO        STOP skipped AME: fractional (0.1401 shares) — software exit will handle it
14:11:36  INFO        [positions] 3/3 (3 valid)
14:11:37  INFO        Daily log -> logs/daily/2026-10-26.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.35|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AME  P&L -0.2%  $-0.08                                            HOLD|
|  AES  P&L -0.2%  $-0.07                                            HOLD|
|  ABT  P&L +0.8%  $+0.27                                            HOLD|
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
=== options_live_micro LIVE 2026-10-26T10:11:37.772191-04:00 share=25% ===
2026-10-26 10:11:37,772 INFO === options_live_micro LIVE 2026-10-26T10:11:37.772191-04:00 share=25% ===
Live account equity $227.36 cash $125.00 #225458845 options_level=3
2026-10-26 10:11:37,818 INFO Live account equity $227.36 cash $125.00 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-10-26 10:11:37,846 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-10-26 10:11:37,862 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (221 earlier lines - see full log file)
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
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-26
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1917 | WARN | <<<
| Missing exit records (post) |  1917 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |    10 | INFO |
| Total closed lots           |  2894 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1740 med=-30.1% | TAINTED n=2043 med=-41.5% | KEEP-only n=835 med=+50.0% | KILL=22 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.35 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261026T141642Z

- UTC timestamp: `20261026T141642Z`
- GitHub run: [#13813](https://github.com/28twagg-ops/TradingBot/actions/runs/40337880629)
- Run id: `40337880629`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`67s`
- Full logs: `logs/action_runs/20261026T141642Z_live_bot.log`, `logs/action_runs/20261026T141642Z_live_options.log`, `logs/action_runs/20261026T141642Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1740 | 48.0 | -30.1 | +35.9 | $+18,391 |
| TAINTED | 2043 | 31.7 | -41.5 | +9.6 | $-11,895 |
| KEEP-only | 835 | 60.1 | +50.0 | +51.9 | $+12,073 |
| KEEP-only recent | 650 | 58.9 | +52.8 | +58.1 | $+8,564 |

- KEEP strategies (23): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S403, S404, S406, S410, S411
- KILL strategies (22): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-26T10:16:48.375077-04:00","date":"2026-10-26","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":54.3,"phases_s":{"reconcile":0.25,"cancel":0.08,"manage":2.23,"protective_stops":0.4,"scan":45.57,"entries":4.28,"reconcile2":0.42},"signals":126,"placed":0,"equity":993532.52,"open_positions":10,"pending_orders":3,"open_lots":10,"submitted_today":12,"filled_today":9,"unattributed_contracts":0,"top_signals":["S430:NVDA","S432:NVDA","S210:TSLA","S430:TSLA","S432:TSLA","S164:COIN","S168:COIN","S167:COIN"],"github_run":"13813","github_run_id":"40337880629","status":"ok","data_quality":{"clean":{"n":1740,"win":48.05,"med":-30.07,"avg":35.89,"pnl":18390.83},"tainted":{"n":2043,"win":31.72,"med":-41.46,"avg":9.61,"pnl":-11895.28},"keep_only":{"n":835,"win":60.12,"med":50.0,"avg":51.9,"pnl":12073.45},"keep_only_recent":{"n":650,"win":58.92,"med":52.83,"avg":58.08,"pnl":8564.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:16:43  INFO      Mode: exits
14:16:43  INFO        Daily log -> logs/daily/2026-10-26.md
14:16:43  INFO        Daily log reconciled -> logs/daily/2026-10-26.md (1 ledger rows)
14:16:43  INFO        place_all_stops: checking 3 positions...
14:16:43  INFO        STOP skipped ABT: fractional (0.3291 shares) — software exit will handle it
14:16:43  INFO        STOP already live AES @ $14.92
14:16:43  INFO        STOP skipped AME: fractional (0.1401 shares) — software exit will handle it
14:16:44  INFO        [positions] 3/3 (3 valid)
14:16:44  INFO        Daily log -> logs/daily/2026-10-26.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.65|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AES  P&L -0.2%  $-0.06                                            HOLD|
|  AME  P&L +0.1%  $+0.03                                            HOLD|
|  ABT  P&L +1.3%  $+0.45                                            HOLD|
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
=== options_live_micro LIVE 2026-10-26T10:16:45.167106-04:00 share=25% ===
2026-10-26 10:16:45,167 INFO === options_live_micro LIVE 2026-10-26T10:16:45.167106-04:00 share=25% ===
Live account equity $227.65 cash $125.00 #225458845 options_level=3
2026-10-26 10:16:45,317 INFO Live account equity $227.65 cash $125.00 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-10-26 10:16:45,446 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-10-26 10:16:45,533 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (220 earlier lines - see full log file)
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
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-26
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1917 | WARN | <<<
| Missing exit records (post) |  1917 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |    10 | INFO |
| Total closed lots           |  2894 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1740 med=-30.1% | TAINTED n=2043 med=-41.5% | KEEP-only n=835 med=+50.0% | KILL=22 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.65 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261026T142143Z

- UTC timestamp: `20261026T142143Z`
- GitHub run: [#13814](https://github.com/28twagg-ops/TradingBot/actions/runs/40338667460)
- Run id: `40338667460`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`54s`
- Full logs: `logs/action_runs/20261026T142143Z_live_bot.log`, `logs/action_runs/20261026T142143Z_live_options.log`, `logs/action_runs/20261026T142143Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1741 | 48.1 | -30.0 | +35.9 | $+18,396 |
| TAINTED | 2043 | 31.7 | -41.5 | +9.6 | $-11,895 |
| KEEP-only | 836 | 60.2 | +50.0 | +51.9 | $+12,078 |
| KEEP-only recent | 651 | 59.0 | +52.8 | +58.1 | $+8,569 |

- KEEP strategies (23): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S403, S404, S406, S410, S411
- KILL strategies (22): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-26T10:21:49.009088-04:00","date":"2026-10-26","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":42.7,"phases_s":{"reconcile":0.17,"cancel":0.05,"manage":2.35,"protective_stops":0.23,"scan":35.15,"entries":3.81,"reconcile2":0.19},"signals":126,"placed":0,"equity":993409.52,"open_positions":9,"pending_orders":3,"open_lots":9,"submitted_today":12,"filled_today":9,"unattributed_contracts":0,"top_signals":["S430:NVDA","S432:NVDA","S210:TSLA","S430:TSLA","S432:TSLA","S164:COIN","S168:COIN","S167:COIN"],"github_run":"13814","github_run_id":"40338667460","status":"ok","data_quality":{"clean":{"n":1741,"win":48.08,"med":-30.0,"avg":35.9,"pnl":18395.83},"tainted":{"n":2043,"win":31.72,"med":-41.46,"avg":9.61,"pnl":-11895.28},"keep_only":{"n":836,"win":60.17,"med":50.0,"avg":51.92,"pnl":12078.45},"keep_only_recent":{"n":651,"win":58.99,"med":52.83,"avg":58.09,"pnl":8569.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:21:44  INFO      Mode: exits
14:21:44  INFO        Daily log -> logs/daily/2026-10-26.md
14:21:44  INFO        Daily log reconciled -> logs/daily/2026-10-26.md (1 ledger rows)
14:21:44  INFO        place_all_stops: checking 3 positions...
14:21:44  INFO        STOP skipped ABT: fractional (0.3291 shares) — software exit will handle it
14:21:44  INFO        STOP already live AES @ $14.92
14:21:44  INFO        STOP skipped AME: fractional (0.1401 shares) — software exit will handle it
14:21:45  INFO        [positions] 3/3 (3 valid)
14:21:45  INFO        Daily log -> logs/daily/2026-10-26.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.53|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AES  P&L -0.1%  $-0.05                                            HOLD|
|  AME  P&L -0.0%  $-0.00                                            HOLD|
|  ABT  P&L +1.0%  $+0.34                                            HOLD|
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
=== options_live_micro LIVE 2026-10-26T10:21:46.110452-04:00 share=25% ===
2026-10-26 10:21:46,110 INFO === options_live_micro LIVE 2026-10-26T10:21:46.110452-04:00 share=25% ===
Live account equity $227.53 cash $125.00 #225458845 options_level=3
2026-10-26 10:21:46,244 INFO Live account equity $227.53 cash $125.00 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-10-26 10:21:46,311 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-10-26 10:21:46,355 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (221 earlier lines - see full log file)
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
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-26
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1917 | WARN | <<<
| Missing exit records (post) |  1917 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     9 | INFO |
| Total closed lots           |  2895 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1741 med=-30.0% | TAINTED n=2043 med=-41.5% | KEEP-only n=836 med=+50.0% | KILL=22 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.53 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261026T142636Z

- UTC timestamp: `20261026T142636Z`
- GitHub run: [#13815](https://github.com/28twagg-ops/TradingBot/actions/runs/40339448424)
- Run id: `40339448424`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`75s`
- Full logs: `logs/action_runs/20261026T142636Z_live_bot.log`, `logs/action_runs/20261026T142636Z_live_options.log`, `logs/action_runs/20261026T142636Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1741 | 48.1 | -30.0 | +35.9 | $+18,396 |
| TAINTED | 2043 | 31.7 | -41.5 | +9.6 | $-11,895 |
| KEEP-only | 836 | 60.2 | +50.0 | +51.9 | $+12,078 |
| KEEP-only recent | 651 | 59.0 | +52.8 | +58.1 | $+8,569 |

- KEEP strategies (23): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S403, S404, S406, S410, S411
- KILL strategies (22): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-26T10:26:44.344985-04:00","date":"2026-10-26","mode":"entry+manage","header":"entry+manage (1 new)","elapsed_s":61.5,"phases_s":{"reconcile":0.48,"cancel":0.16,"manage":3.4,"protective_stops":0.92,"scan":46.4,"entries":7.78,"reconcile2":0.49},"signals":126,"placed":1,"equity":993287.94,"open_positions":11,"pending_orders":2,"open_lots":11,"submitted_today":13,"filled_today":11,"unattributed_contracts":0,"top_signals":["S430:NVDA","S432:NVDA","S210:TSLA","S430:TSLA","S432:TSLA","S164:COIN","S168:COIN","S167:COIN"],"github_run":"13815","github_run_id":"40339448424","status":"ok","data_quality":{"clean":{"n":1741,"win":48.08,"med":-30.0,"avg":35.9,"pnl":18395.83},"tainted":{"n":2043,"win":31.72,"med":-41.46,"avg":9.61,"pnl":-11895.28},"keep_only":{"n":836,"win":60.17,"med":50.0,"avg":51.92,"pnl":12078.45},"keep_only_recent":{"n":651,"win":58.99,"med":52.83,"avg":58.09,"pnl":8569.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:26:37  INFO      Mode: exits
14:26:38  INFO        Daily log -> logs/daily/2026-10-26.md
14:26:38  INFO        Daily log reconciled -> logs/daily/2026-10-26.md (1 ledger rows)
14:26:38  INFO        place_all_stops: checking 3 positions...
14:26:38  INFO        STOP skipped ABT: fractional (0.3291 shares) — software exit will handle it
14:26:38  INFO        STOP already live AES @ $14.92
14:26:38  INFO        STOP skipped AME: fractional (0.1401 shares) — software exit will handle it
14:26:38  INFO        [positions] 3/3 (3 valid)
14:26:39  INFO        Daily log -> logs/daily/2026-10-26.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.53|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AES  P&L -0.2%  $-0.06                                            HOLD|
|  AME  P&L -0.1%  $-0.04                                            HOLD|
|  ABT  P&L +1.1%  $+0.38                                            HOLD|
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
=== options_live_micro LIVE 2026-10-26T10:26:40.094082-04:00 share=25% ===
2026-10-26 10:26:40,094 INFO === options_live_micro LIVE 2026-10-26T10:26:40.094082-04:00 share=25% ===
Live account equity $227.50 cash $125.00 #225458845 options_level=3
2026-10-26 10:26:40,320 INFO Live account equity $227.50 cash $125.00 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-10-26 10:26:40,530 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-10-26 10:26:40,669 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (221 earlier lines - see full log file)
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
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-26
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1917 | WARN | <<<
| Missing exit records (post) |  1917 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |    11 | INFO |
| Total closed lots           |  2895 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1741 med=-30.0% | TAINTED n=2043 med=-41.5% | KEEP-only n=836 med=+50.0% | KILL=22 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.5 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261026T143130Z

- UTC timestamp: `20261026T143130Z`
- GitHub run: [#13816](https://github.com/28twagg-ops/TradingBot/actions/runs/40340125630)
- Run id: `40340125630`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`37s`
- Full logs: `logs/action_runs/20261026T143130Z_live_bot.log`, `logs/action_runs/20261026T143130Z_live_options.log`, `logs/action_runs/20261026T143130Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1741 | 48.1 | -30.0 | +35.9 | $+18,396 |
| TAINTED | 2043 | 31.7 | -41.5 | +9.6 | $-11,895 |
| KEEP-only | 836 | 60.2 | +50.0 | +51.9 | $+12,078 |
| KEEP-only recent | 651 | 59.0 | +52.8 | +58.1 | $+8,569 |

- KEEP strategies (23): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S403, S404, S406, S410, S411
- KILL strategies (22): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-26T10:31:34.416798-04:00","date":"2026-10-26","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":29.1,"phases_s":{"reconcile":0.25,"cancel":0.06,"manage":2.97,"protective_stops":0.38,"scan":18.89,"entries":5.2,"reconcile2":0.28},"signals":126,"placed":0,"equity":993294.44,"open_positions":11,"pending_orders":2,"open_lots":11,"submitted_today":13,"filled_today":11,"unattributed_contracts":0,"top_signals":["S430:NVDA","S432:NVDA","S210:TSLA","S430:TSLA","S432:TSLA","S164:COIN","S168:COIN","S167:COIN"],"github_run":"13816","github_run_id":"40340125630","status":"ok","data_quality":{"clean":{"n":1741,"win":48.08,"med":-30.0,"avg":35.9,"pnl":18395.83},"tainted":{"n":2043,"win":31.72,"med":-41.46,"avg":9.61,"pnl":-11895.28},"keep_only":{"n":836,"win":60.17,"med":50.0,"avg":51.92,"pnl":12078.45},"keep_only_recent":{"n":651,"win":58.99,"med":52.83,"avg":58.09,"pnl":8569.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:31:30  INFO      Mode: exits
14:31:31  INFO        Daily log -> logs/daily/2026-10-26.md
14:31:31  INFO        Daily log reconciled -> logs/daily/2026-10-26.md (1 ledger rows)
14:31:31  INFO        place_all_stops: checking 3 positions...
14:31:31  INFO        STOP skipped ABT: fractional (0.3291 shares) — software exit will handle it
14:31:31  INFO        STOP already live AES @ $14.92
14:31:31  INFO        STOP skipped AME: fractional (0.1401 shares) — software exit will handle it
14:31:31  INFO        [positions] 3/3 (3 valid)
14:31:31  INFO        Daily log -> logs/daily/2026-10-26.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.55|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AES  P&L -0.2%  $-0.06                                            HOLD|
|  AME  P&L -0.1%  $-0.02                                            HOLD|
|  ABT  P&L +1.2%  $+0.40                                            HOLD|
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
=== options_live_micro LIVE 2026-10-26T10:31:32.171780-04:00 share=25% ===
2026-10-26 10:31:32,171 INFO === options_live_micro LIVE 2026-10-26T10:31:32.171780-04:00 share=25% ===
Live account equity $227.55 cash $125.00 #225458845 options_level=3
2026-10-26 10:31:32,340 INFO Live account equity $227.55 cash $125.00 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-10-26 10:31:32,477 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-10-26 10:31:32,567 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (219 earlier lines - see full log file)
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
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-26
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1917 | WARN | <<<
| Missing exit records (post) |  1917 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |    11 | INFO |
| Total closed lots           |  2895 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1741 med=-30.0% | TAINTED n=2043 med=-41.5% | KEEP-only n=836 med=+50.0% | KILL=22 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.55 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261026T143651Z

- UTC timestamp: `20261026T143651Z`
- GitHub run: [#13817](https://github.com/28twagg-ops/TradingBot/actions/runs/40340936377)
- Run id: `40340936377`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`66s`
- Full logs: `logs/action_runs/20261026T143651Z_live_bot.log`, `logs/action_runs/20261026T143651Z_live_options.log`, `logs/action_runs/20261026T143651Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1741 | 48.1 | -30.0 | +35.9 | $+18,396 |
| TAINTED | 2043 | 31.7 | -41.5 | +9.6 | $-11,895 |
| KEEP-only | 836 | 60.2 | +50.0 | +51.9 | $+12,078 |
| KEEP-only recent | 651 | 59.0 | +52.8 | +58.1 | $+8,569 |

- KEEP strategies (23): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S403, S404, S406, S410, S411
- KILL strategies (22): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-26T10:36:58.119597-04:00","date":"2026-10-26","mode":"entry+manage","header":"entry+manage (1 new)","elapsed_s":54.1,"phases_s":{"reconcile":0.39,"cancel":0.11,"manage":5.28,"protective_stops":0.68,"scan":40.28,"entries":5.51,"reconcile2":0.43},"signals":126,"placed":1,"equity":993320.44,"open_positions":12,"pending_orders":2,"open_lots":12,"submitted_today":14,"filled_today":12,"unattributed_contracts":0,"top_signals":["S430:NVDA","S432:NVDA","S210:TSLA","S430:TSLA","S432:TSLA","S164:COIN","S168:COIN","S167:COIN"],"github_run":"13817","github_run_id":"40340936377","status":"ok","data_quality":{"clean":{"n":1741,"win":48.08,"med":-30.0,"avg":35.9,"pnl":18395.83},"tainted":{"n":2043,"win":31.72,"med":-41.46,"avg":9.61,"pnl":-11895.28},"keep_only":{"n":836,"win":60.17,"med":50.0,"avg":51.92,"pnl":12078.45},"keep_only_recent":{"n":651,"win":58.99,"med":52.83,"avg":58.09,"pnl":8569.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:36:52  INFO      Mode: exits
14:36:53  INFO        Daily log -> logs/daily/2026-10-26.md
14:36:53  INFO        Daily log reconciled -> logs/daily/2026-10-26.md (1 ledger rows)
14:36:53  INFO        place_all_stops: checking 3 positions...
14:36:53  INFO        STOP skipped ABT: fractional (0.3291 shares) — software exit will handle it
14:36:53  INFO        STOP already live AES @ $14.92
14:36:53  INFO        STOP skipped AME: fractional (0.1401 shares) — software exit will handle it
14:36:54  INFO        [positions] 3/3 (3 valid)
14:36:54  INFO        Daily log -> logs/daily/2026-10-26.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.68|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AES  P&L -0.2%  $-0.06                                            HOLD|
|  AME  P&L -0.1%  $-0.03                                            HOLD|
|  ABT  P&L +1.5%  $+0.51                                            HOLD|
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
=== options_live_micro LIVE 2026-10-26T10:36:54.975826-04:00 share=25% ===
2026-10-26 10:36:54,975 INFO === options_live_micro LIVE 2026-10-26T10:36:54.975826-04:00 share=25% ===
Live account equity $227.66 cash $125.00 #225458845 options_level=3
2026-10-26 10:36:55,185 INFO Live account equity $227.66 cash $125.00 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-10-26 10:36:55,373 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-10-26 10:36:55,489 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (220 earlier lines - see full log file)
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
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-26
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1917 | WARN | <<<
| Missing exit records (post) |  1917 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |    12 | INFO |
| Total closed lots           |  2895 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1741 med=-30.0% | TAINTED n=2043 med=-41.5% | KEEP-only n=836 med=+50.0% | KILL=22 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.66 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261026T144143Z

- UTC timestamp: `20261026T144143Z`
- GitHub run: [#13818](https://github.com/28twagg-ops/TradingBot/actions/runs/40341731504)
- Run id: `40341731504`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`42s`
- Full logs: `logs/action_runs/20261026T144143Z_live_bot.log`, `logs/action_runs/20261026T144143Z_live_options.log`, `logs/action_runs/20261026T144143Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1741 | 48.1 | -30.0 | +35.9 | $+18,396 |
| TAINTED | 2043 | 31.7 | -41.5 | +9.6 | $-11,895 |
| KEEP-only | 836 | 60.2 | +50.0 | +51.9 | $+12,078 |
| KEEP-only recent | 651 | 59.0 | +52.8 | +58.1 | $+8,569 |

- KEEP strategies (23): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S403, S404, S406, S410, S411
- KILL strategies (22): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-26T10:41:49.189669-04:00","date":"2026-10-26","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":32.7,"phases_s":{"reconcile":0.4,"cancel":0.16,"manage":3.26,"protective_stops":0.78,"scan":20.15,"entries":6.03,"reconcile2":0.41},"signals":126,"placed":0,"equity":993143.9,"open_positions":13,"pending_orders":1,"open_lots":13,"submitted_today":14,"filled_today":13,"unattributed_contracts":0,"top_signals":["S430:NVDA","S432:NVDA","S210:TSLA","S430:TSLA","S432:TSLA","S164:COIN","S168:COIN","S167:COIN"],"github_run":"13818","github_run_id":"40341731504","status":"ok","data_quality":{"clean":{"n":1741,"win":48.08,"med":-30.0,"avg":35.9,"pnl":18395.83},"tainted":{"n":2043,"win":31.72,"med":-41.46,"avg":9.61,"pnl":-11895.28},"keep_only":{"n":836,"win":60.17,"med":50.0,"avg":51.92,"pnl":12078.45},"keep_only_recent":{"n":651,"win":58.99,"med":52.83,"avg":58.09,"pnl":8569.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:41:44  INFO      Mode: exits
14:41:44  INFO        Daily log -> logs/daily/2026-10-26.md
14:41:44  INFO        Daily log reconciled -> logs/daily/2026-10-26.md (1 ledger rows)
14:41:44  INFO        place_all_stops: checking 3 positions...
14:41:44  INFO        STOP skipped ABT: fractional (0.3291 shares) — software exit will handle it
14:41:44  INFO        STOP already live AES @ $14.92
14:41:44  INFO        STOP skipped AME: fractional (0.1401 shares) — software exit will handle it
14:41:45  INFO        [positions] 3/3 (3 valid)
14:41:45  INFO        Daily log -> logs/daily/2026-10-26.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.66|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AES  P&L -0.1%  $-0.05                                            HOLD|
|  AME  P&L +0.1%  $+0.02                                            HOLD|
|  ABT  P&L +1.3%  $+0.45                                            HOLD|
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
=== options_live_micro LIVE 2026-10-26T10:41:46.224701-04:00 share=25% ===
2026-10-26 10:41:46,224 INFO === options_live_micro LIVE 2026-10-26T10:41:46.224701-04:00 share=25% ===
Live account equity $227.65 cash $125.00 #225458845 options_level=3
2026-10-26 10:41:46,423 INFO Live account equity $227.65 cash $125.00 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-10-26 10:41:46,600 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-10-26 10:41:46,715 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (219 earlier lines - see full log file)
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
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-26
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1917 | WARN | <<<
| Missing exit records (post) |  1917 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |    13 | INFO |
| Total closed lots           |  2895 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1741 med=-30.0% | TAINTED n=2043 med=-41.5% | KEEP-only n=836 med=+50.0% | KILL=22 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.65 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261026T144642Z

- UTC timestamp: `20261026T144642Z`
- GitHub run: [#13819](https://github.com/28twagg-ops/TradingBot/actions/runs/40342537221)
- Run id: `40342537221`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`61s`
- Full logs: `logs/action_runs/20261026T144642Z_live_bot.log`, `logs/action_runs/20261026T144642Z_live_options.log`, `logs/action_runs/20261026T144642Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1742 | 48.1 | -29.3 | +35.9 | $+18,421 |
| TAINTED | 2043 | 31.7 | -41.5 | +9.6 | $-11,895 |
| KEEP-only | 836 | 60.2 | +50.0 | +51.9 | $+12,078 |
| KEEP-only recent | 651 | 59.0 | +52.8 | +58.1 | $+8,569 |

- KEEP strategies (23): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S403, S404, S406, S410, S411
- KILL strategies (22): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-26T10:46:47.778986-04:00","date":"2026-10-26","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":48.5,"phases_s":{"reconcile":0.15,"cancel":0.03,"manage":1.97,"protective_stops":0.2,"scan":45.34,"entries":0.03,"reconcile2":0.11},"signals":126,"placed":0,"equity":992865.38,"open_positions":12,"pending_orders":1,"open_lots":12,"submitted_today":14,"filled_today":13,"unattributed_contracts":0,"top_signals":["S430:NVDA","S432:NVDA","S210:TSLA","S430:TSLA","S432:TSLA","S164:COIN","S168:COIN","S167:COIN"],"github_run":"13819","github_run_id":"40342537221","status":"ok","data_quality":{"clean":{"n":1742,"win":48.11,"med":-29.29,"avg":35.92,"pnl":18420.83},"tainted":{"n":2043,"win":31.72,"med":-41.46,"avg":9.61,"pnl":-11895.28},"keep_only":{"n":836,"win":60.17,"med":50.0,"avg":51.92,"pnl":12078.45},"keep_only_recent":{"n":651,"win":58.99,"med":52.83,"avg":58.09,"pnl":8569.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:46:43  INFO      Mode: exits
14:46:44  INFO        Daily log -> logs/daily/2026-10-26.md
14:46:44  INFO        Daily log reconciled -> logs/daily/2026-10-26.md (1 ledger rows)
14:46:44  INFO        place_all_stops: checking 3 positions...
14:46:44  INFO        STOP skipped ABT: fractional (0.3291 shares) — software exit will handle it
14:46:44  INFO        STOP already live AES @ $14.92
14:46:44  INFO        STOP skipped AME: fractional (0.1401 shares) — software exit will handle it
14:46:44  INFO        [positions] 3/3 (3 valid)
14:46:44  INFO        Daily log -> logs/daily/2026-10-26.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.63|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AES  P&L -0.1%  $-0.05                                            HOLD|
|  AME  P&L -0.1%  $-0.02                                            HOLD|
|  ABT  P&L +1.4%  $+0.47                                            HOLD|
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
=== options_live_micro LIVE 2026-10-26T10:46:45.154437-04:00 share=25% ===
2026-10-26 10:46:45,154 INFO === options_live_micro LIVE 2026-10-26T10:46:45.154437-04:00 share=25% ===
Live account equity $227.63 cash $125.00 #225458845 options_level=3
2026-10-26 10:46:45,213 INFO Live account equity $227.63 cash $125.00 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-10-26 10:46:45,248 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-10-26 10:46:45,274 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (219 earlier lines - see full log file)
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
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-26
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1917 | WARN | <<<
| Missing exit records (post) |  1917 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |    12 | INFO |
| Total closed lots           |  2896 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1742 med=-29.3% | TAINTED n=2043 med=-41.5% | KEEP-only n=836 med=+50.0% | KILL=22 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.63 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261026T145144Z

- UTC timestamp: `20261026T145144Z`
- GitHub run: [#13820](https://github.com/28twagg-ops/TradingBot/actions/runs/40343347478)
- Run id: `40343347478`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`58s`
- Full logs: `logs/action_runs/20261026T145144Z_live_bot.log`, `logs/action_runs/20261026T145144Z_live_options.log`, `logs/action_runs/20261026T145144Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1742 | 48.1 | -29.3 | +35.9 | $+18,421 |
| TAINTED | 2044 | 31.7 | -41.5 | +9.6 | $-11,901 |
| KEEP-only | 836 | 60.2 | +50.0 | +51.9 | $+12,078 |
| KEEP-only recent | 651 | 59.0 | +52.8 | +58.1 | $+8,569 |

- KEEP strategies (23): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S403, S404, S406, S410, S411
- KILL strategies (22): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-26T10:51:52.608006-04:00","date":"2026-10-26","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":45.0,"phases_s":{"reconcile":0.47,"cancel":0.18,"manage":2.83,"protective_stops":0.88,"scan":38.4,"entries":0.09,"reconcile2":0.47},"signals":126,"placed":0,"equity":992747.01,"open_positions":11,"pending_orders":1,"open_lots":11,"submitted_today":14,"filled_today":13,"unattributed_contracts":0,"top_signals":["S430:NVDA","S432:NVDA","S210:TSLA","S430:TSLA","S432:TSLA","S164:COIN","S168:COIN","S167:COIN"],"github_run":"13820","github_run_id":"40343347478","status":"ok","data_quality":{"clean":{"n":1742,"win":48.11,"med":-29.29,"avg":35.92,"pnl":18420.83},"tainted":{"n":2044,"win":31.7,"med":-41.46,"avg":9.59,"pnl":-11901.28},"keep_only":{"n":836,"win":60.17,"med":50.0,"avg":51.92,"pnl":12078.45},"keep_only_recent":{"n":651,"win":58.99,"med":52.83,"avg":58.09,"pnl":8569.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:51:45  INFO      Mode: exits
14:51:46  INFO        Daily log -> logs/daily/2026-10-26.md
14:51:46  INFO        Daily log reconciled -> logs/daily/2026-10-26.md (1 ledger rows)
14:51:46  INFO        place_all_stops: checking 3 positions...
14:51:46  INFO        STOP skipped ABT: fractional (0.3291 shares) — software exit will handle it
14:51:46  INFO        STOP already live AES @ $14.92
14:51:46  INFO        STOP skipped AME: fractional (0.1401 shares) — software exit will handle it
14:51:47  INFO        [positions] 3/3 (3 valid)
14:51:47  INFO        Daily log -> logs/daily/2026-10-26.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:51 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.62|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AES  P&L -0.2%  $-0.06                                            HOLD|
|  AME  P&L +0.1%  $+0.05                                            HOLD|
|  ABT  P&L +1.1%  $+0.39                                            HOLD|
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
=== options_live_micro LIVE 2026-10-26T10:51:48.476449-04:00 share=25% ===
2026-10-26 10:51:48,476 INFO === options_live_micro LIVE 2026-10-26T10:51:48.476449-04:00 share=25% ===
Live account equity $227.62 cash $125.00 #225458845 options_level=3
2026-10-26 10:51:49,067 INFO Live account equity $227.62 cash $125.00 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-10-26 10:51:49,285 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-10-26 10:51:49,430 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (221 earlier lines - see full log file)
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
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-26
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1917 | WARN | <<<
| Missing exit records (post) |  1917 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |    11 | INFO |
| Total closed lots           |  2897 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1742 med=-29.3% | TAINTED n=2044 med=-41.5% | KEEP-only n=836 med=+50.0% | KILL=22 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.62 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261026T145647Z

- UTC timestamp: `20261026T145647Z`
- GitHub run: [#13821](https://github.com/28twagg-ops/TradingBot/actions/runs/40344146350)
- Run id: `40344146350`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`33s`
- Full logs: `logs/action_runs/20261026T145647Z_live_bot.log`, `logs/action_runs/20261026T145647Z_live_options.log`, `logs/action_runs/20261026T145647Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1742 | 48.1 | -29.3 | +35.9 | $+18,421 |
| TAINTED | 2044 | 31.7 | -41.5 | +9.6 | $-11,901 |
| KEEP-only | 836 | 60.2 | +50.0 | +51.9 | $+12,078 |
| KEEP-only recent | 651 | 59.0 | +52.8 | +58.1 | $+8,569 |

- KEEP strategies (23): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S403, S404, S406, S410, S411
- KILL strategies (22): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-26T10:56:52.140115-04:00","date":"2026-10-26","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":24.5,"phases_s":{"reconcile":0.3,"cancel":0.09,"manage":1.98,"protective_stops":0.54,"scan":20.09,"entries":0.05,"reconcile2":0.33},"signals":126,"placed":0,"equity":992628.63,"open_positions":11,"pending_orders":1,"open_lots":11,"submitted_today":14,"filled_today":13,"unattributed_contracts":0,"top_signals":["S430:NVDA","S432:NVDA","S210:TSLA","S430:TSLA","S432:TSLA","S164:COIN","S168:COIN","S167:COIN"],"github_run":"13821","github_run_id":"40344146350","status":"ok","data_quality":{"clean":{"n":1742,"win":48.11,"med":-29.29,"avg":35.92,"pnl":18420.83},"tainted":{"n":2044,"win":31.7,"med":-41.46,"avg":9.59,"pnl":-11901.28},"keep_only":{"n":836,"win":60.17,"med":50.0,"avg":51.92,"pnl":12078.45},"keep_only_recent":{"n":651,"win":58.99,"med":52.83,"avg":58.09,"pnl":8569.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:56:48  INFO      Mode: exits
14:56:48  INFO        Daily log -> logs/daily/2026-10-26.md
14:56:48  INFO        Daily log reconciled -> logs/daily/2026-10-26.md (1 ledger rows)
14:56:48  INFO        place_all_stops: checking 3 positions...
14:56:48  INFO        STOP skipped ABT: fractional (0.3291 shares) — software exit will handle it
14:56:48  INFO        STOP already live AES @ $14.92
14:56:48  INFO        STOP skipped AME: fractional (0.1401 shares) — software exit will handle it
14:56:48  INFO        [positions] 3/3 (3 valid)
14:56:49  INFO        Daily log -> logs/daily/2026-10-26.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:56 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.65|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AES  P&L -0.1%  $-0.03                                            HOLD|
|  AME  P&L +0.2%  $+0.06                                            HOLD|
|  ABT  P&L +1.1%  $+0.38                                            HOLD|
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
=== options_live_micro LIVE 2026-10-26T10:56:49.552112-04:00 share=25% ===
2026-10-26 10:56:49,552 INFO === options_live_micro LIVE 2026-10-26T10:56:49.552112-04:00 share=25% ===
Live account equity $227.65 cash $125.00 #225458845 options_level=3
2026-10-26 10:56:49,678 INFO Live account equity $227.65 cash $125.00 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-10-26 10:56:49,800 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-10-26 10:56:49,873 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (218 earlier lines - see full log file)
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
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-26
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1917 | WARN | <<<
| Missing exit records (post) |  1917 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |    11 | INFO |
| Total closed lots           |  2897 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1742 med=-29.3% | TAINTED n=2044 med=-41.5% | KEEP-only n=836 med=+50.0% | KILL=22 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.65 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261026T150144Z

- UTC timestamp: `20261026T150144Z`
- GitHub run: [#13822](https://github.com/28twagg-ops/TradingBot/actions/runs/40344975030)
- Run id: `40344975030`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`42s`
- Full logs: `logs/action_runs/20261026T150144Z_live_bot.log`, `logs/action_runs/20261026T150144Z_live_options.log`, `logs/action_runs/20261026T150144Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1744 | 48.2 | -28.6 | +35.9 | $+18,457 |
| TAINTED | 2044 | 31.7 | -41.5 | +9.6 | $-11,901 |
| KEEP-only | 847 | 60.6 | +50.9 | +52.1 | $+12,515 |
| KEEP-only recent | 662 | 59.5 | +53.0 | +58.2 | $+9,006 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S396, S397, S403, S404, S406, S410, S411
- KILL strategies (22): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-26T11:01:48.776185-04:00","date":"2026-10-26","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":32.0,"phases_s":{"reconcile":0.09,"cancel":0.02,"manage":1.56,"protective_stops":0.09,"scan":29.59,"entries":0.03,"reconcile2":0.09},"signals":126,"placed":0,"equity":992526.34,"open_positions":9,"pending_orders":1,"open_lots":9,"submitted_today":14,"filled_today":13,"unattributed_contracts":0,"top_signals":["S430:NVDA","S432:NVDA","S210:TSLA","S430:TSLA","S432:TSLA","S164:COIN","S168:COIN","S167:COIN"],"github_run":"13822","github_run_id":"40344975030","status":"ok","data_quality":{"clean":{"n":1744,"win":48.17,"med":-28.57,"avg":35.95,"pnl":18456.83},"tainted":{"n":2044,"win":31.7,"med":-41.46,"avg":9.59,"pnl":-11901.28},"keep_only":{"n":847,"win":60.57,"med":50.85,"avg":52.1,"pnl":12515.45},"keep_only_recent":{"n":662,"win":59.52,"med":53.0,"avg":58.22,"pnl":9006.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S396","S397","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:01:45  INFO      Mode: exits
15:01:45  INFO        Daily log -> logs/daily/2026-10-26.md
15:01:45  INFO        Daily log reconciled -> logs/daily/2026-10-26.md (1 ledger rows)
15:01:45  INFO        place_all_stops: checking 3 positions...
15:01:45  INFO        STOP skipped ABT: fractional (0.3291 shares) — software exit will handle it
15:01:45  INFO        STOP already live AES @ $14.92
15:01:45  INFO        STOP skipped AME: fractional (0.1401 shares) — software exit will handle it
15:01:45  INFO        [positions] 3/3 (3 valid)
15:01:45  INFO        Daily log -> logs/daily/2026-10-26.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.68|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AES  P&L -0.2%  $-0.06                                            HOLD|
|  AME  P&L +0.3%  $+0.10                                            HOLD|
|  ABT  P&L +1.2%  $+0.40                                            HOLD|
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
=== options_live_micro LIVE 2026-10-26T11:01:46.584091-04:00 share=25% ===
2026-10-26 11:01:46,584 INFO === options_live_micro LIVE 2026-10-26T11:01:46.584091-04:00 share=25% ===
Live account equity $227.68 cash $125.00 #225458845 options_level=3
2026-10-26 11:01:46,619 INFO Live account equity $227.68 cash $125.00 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-10-26 11:01:46,639 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-10-26 11:01:46,651 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (220 earlier lines - see full log file)
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
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-26
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1917 | WARN | <<<
| Missing exit records (post) |  1917 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     9 | INFO |
| Total closed lots           |  2899 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1744 med=-28.6% | TAINTED n=2044 med=-41.5% | KEEP-only n=847 med=+50.9% | KILL=22 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.68 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261026T150647Z

- UTC timestamp: `20261026T150647Z`
- GitHub run: [#13823](https://github.com/28twagg-ops/TradingBot/actions/runs/40345797577)
- Run id: `40345797577`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`39s`
- Full logs: `logs/action_runs/20261026T150647Z_live_bot.log`, `logs/action_runs/20261026T150647Z_live_options.log`, `logs/action_runs/20261026T150647Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1744 | 48.2 | -28.6 | +35.9 | $+18,457 |
| TAINTED | 2044 | 31.7 | -41.5 | +9.6 | $-11,901 |
| KEEP-only | 847 | 60.6 | +50.9 | +52.1 | $+12,515 |
| KEEP-only recent | 662 | 59.5 | +53.0 | +58.2 | $+9,006 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S396, S397, S403, S404, S406, S410, S411
- KILL strategies (22): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-26T11:06:53.944707-04:00","date":"2026-10-26","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":29.4,"phases_s":{"reconcile":0.3,"cancel":0.09,"manage":2.0,"protective_stops":0.46,"scan":25.17,"entries":0.05,"reconcile2":0.33},"signals":126,"placed":0,"equity":992554.8,"open_positions":9,"pending_orders":1,"open_lots":9,"submitted_today":14,"filled_today":13,"unattributed_contracts":0,"top_signals":["S430:NVDA","S432:NVDA","S210:TSLA","S430:TSLA","S432:TSLA","S164:COIN","S168:COIN","S167:COIN"],"github_run":"13823","github_run_id":"40345797577","status":"ok","data_quality":{"clean":{"n":1744,"win":48.17,"med":-28.57,"avg":35.95,"pnl":18456.83},"tainted":{"n":2044,"win":31.7,"med":-41.46,"avg":9.59,"pnl":-11901.28},"keep_only":{"n":847,"win":60.57,"med":50.85,"avg":52.1,"pnl":12515.45},"keep_only_recent":{"n":662,"win":59.52,"med":53.0,"avg":58.22,"pnl":9006.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S396","S397","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:06:49  INFO      Mode: exits
15:06:50  INFO        Daily log -> logs/daily/2026-10-26.md
15:06:50  INFO        Daily log reconciled -> logs/daily/2026-10-26.md (1 ledger rows)
15:06:50  INFO        place_all_stops: checking 3 positions...
15:06:50  INFO        STOP skipped ABT: fractional (0.3291 shares) — software exit will handle it
15:06:50  INFO        STOP already live AES @ $14.92
15:06:50  INFO        STOP skipped AME: fractional (0.1401 shares) — software exit will handle it
15:06:50  INFO        [positions] 3/3 (3 valid)
15:06:50  INFO        Daily log -> logs/daily/2026-10-26.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.69|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AES  P&L -0.2%  $-0.07                                            HOLD|
|  AME  P&L +0.4%  $+0.14                                            HOLD|
|  ABT  P&L +1.1%  $+0.38                                            HOLD|
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
=== options_live_micro LIVE 2026-10-26T11:06:51.410031-04:00 share=25% ===
2026-10-26 11:06:51,410 INFO === options_live_micro LIVE 2026-10-26T11:06:51.410031-04:00 share=25% ===
Live account equity $227.69 cash $125.00 #225458845 options_level=3
2026-10-26 11:06:51,530 INFO Live account equity $227.69 cash $125.00 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-10-26 11:06:51,637 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-10-26 11:06:51,702 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (218 earlier lines - see full log file)
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
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-26
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1917 | WARN | <<<
| Missing exit records (post) |  1917 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     9 | INFO |
| Total closed lots           |  2899 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1744 med=-28.6% | TAINTED n=2044 med=-41.5% | KEEP-only n=847 med=+50.9% | KILL=22 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.69 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261026T151147Z

- UTC timestamp: `20261026T151147Z`
- GitHub run: [#13824](https://github.com/28twagg-ops/TradingBot/actions/runs/40346634018)
- Run id: `40346634018`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`30s`
- Full logs: `logs/action_runs/20261026T151147Z_live_bot.log`, `logs/action_runs/20261026T151147Z_live_options.log`, `logs/action_runs/20261026T151147Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1745 | 48.1 | -28.6 | +35.9 | $+18,447 |
| TAINTED | 2045 | 31.7 | -41.5 | +9.6 | $-11,919 |
| KEEP-only | 848 | 60.5 | +50.8 | +52.0 | $+12,505 |
| KEEP-only recent | 663 | 59.4 | +52.9 | +58.1 | $+8,996 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S396, S397, S403, S404, S406, S410, S411
- KILL strategies (22): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-26T11:11:52.739462-04:00","date":"2026-10-26","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":22.3,"phases_s":{"reconcile":0.22,"cancel":0.06,"manage":1.29,"protective_stops":0.29,"scan":19.43,"entries":0.04,"reconcile2":0.23},"signals":126,"placed":0,"equity":992606.28,"open_positions":7,"pending_orders":1,"open_lots":7,"submitted_today":14,"filled_today":13,"unattributed_contracts":0,"top_signals":["S430:NVDA","S432:NVDA","S210:TSLA","S430:TSLA","S432:TSLA","S164:COIN","S168:COIN","S167:COIN"],"github_run":"13824","github_run_id":"40346634018","status":"ok","data_quality":{"clean":{"n":1745,"win":48.14,"med":-28.57,"avg":35.9,"pnl":18446.83},"tainted":{"n":2045,"win":31.69,"med":-41.46,"avg":9.56,"pnl":-11919.28},"keep_only":{"n":848,"win":60.5,"med":50.82,"avg":51.98,"pnl":12505.45},"keep_only_recent":{"n":663,"win":59.43,"med":52.94,"avg":58.05,"pnl":8996.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S396","S397","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:11:48  INFO      Mode: exits
15:11:49  INFO        Daily log -> logs/daily/2026-10-26.md
15:11:49  INFO        Daily log reconciled -> logs/daily/2026-10-26.md (1 ledger rows)
15:11:49  INFO        place_all_stops: checking 3 positions...
15:11:49  INFO        STOP skipped ABT: fractional (0.3291 shares) — software exit will handle it
15:11:49  INFO        STOP already live AES @ $14.92
15:11:49  INFO        STOP skipped AME: fractional (0.1401 shares) — software exit will handle it
15:11:49  INFO        [positions] 3/3 (3 valid)
15:11:49  INFO        Daily log -> logs/daily/2026-10-26.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.74|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AES  P&L -0.1%  $-0.03                                            HOLD|
|  AME  P&L +0.5%  $+0.16                                            HOLD|
|  ABT  P&L +1.1%  $+0.38                                            HOLD|
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
=== options_live_micro LIVE 2026-10-26T11:11:50.370421-04:00 share=25% ===
2026-10-26 11:11:50,370 INFO === options_live_micro LIVE 2026-10-26T11:11:50.370421-04:00 share=25% ===
Live account equity $227.74 cash $125.00 #225458845 options_level=3
2026-10-26 11:11:50,501 INFO Live account equity $227.74 cash $125.00 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-10-26 11:11:50,605 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-10-26 11:11:50,673 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (220 earlier lines - see full log file)
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
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-26
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1917 | WARN | <<<
| Missing exit records (post) |  1917 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     7 | INFO |
| Total closed lots           |  2901 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1745 med=-28.6% | TAINTED n=2045 med=-41.5% | KEEP-only n=848 med=+50.8% | KILL=22 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.74 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261026T151709Z

- UTC timestamp: `20261026T151709Z`
- GitHub run: [#13825](https://github.com/28twagg-ops/TradingBot/actions/runs/40347455461)
- Run id: `40347455461`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`56s`
- Full logs: `logs/action_runs/20261026T151709Z_live_bot.log`, `logs/action_runs/20261026T151709Z_live_options.log`, `logs/action_runs/20261026T151709Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1745 | 48.1 | -28.6 | +35.9 | $+18,447 |
| TAINTED | 2045 | 31.7 | -41.5 | +9.6 | $-11,919 |
| KEEP-only | 848 | 60.5 | +50.8 | +52.0 | $+12,505 |
| KEEP-only recent | 663 | 59.4 | +52.9 | +58.1 | $+8,996 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S396, S397, S403, S404, S406, S410, S411
- KILL strategies (22): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-26T11:17:16.837315-04:00","date":"2026-10-26","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":42.9,"phases_s":{"reconcile":0.41,"cancel":0.13,"manage":1.55,"protective_stops":0.5,"scan":38.56,"entries":0.07,"reconcile2":0.44},"signals":126,"placed":0,"equity":992726.52,"open_positions":7,"pending_orders":1,"open_lots":7,"submitted_today":14,"filled_today":13,"unattributed_contracts":0,"top_signals":["S430:NVDA","S432:NVDA","S210:TSLA","S430:TSLA","S432:TSLA","S164:COIN","S168:COIN","S167:COIN"],"github_run":"13825","github_run_id":"40347455461","status":"ok","data_quality":{"clean":{"n":1745,"win":48.14,"med":-28.57,"avg":35.9,"pnl":18446.83},"tainted":{"n":2045,"win":31.69,"med":-41.46,"avg":9.56,"pnl":-11919.28},"keep_only":{"n":848,"win":60.5,"med":50.82,"avg":51.98,"pnl":12505.45},"keep_only_recent":{"n":663,"win":59.43,"med":52.94,"avg":58.05,"pnl":8996.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S396","S397","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:17:11  INFO      Mode: exits
15:17:11  INFO        Daily log -> logs/daily/2026-10-26.md
15:17:11  INFO        Daily log reconciled -> logs/daily/2026-10-26.md (1 ledger rows)
15:17:11  INFO        place_all_stops: checking 3 positions...
15:17:11  INFO        STOP skipped ABT: fractional (0.3291 shares) — software exit will handle it
15:17:11  INFO        STOP already live AES @ $14.92
15:17:11  INFO        STOP skipped AME: fractional (0.1401 shares) — software exit will handle it
15:17:12  INFO        [positions] 3/3 (3 valid)
15:17:12  INFO        Daily log -> logs/daily/2026-10-26.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:17 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.78|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AES  P&L -0.1%  $-0.03                                            HOLD|
|  AME  P&L +0.5%  $+0.18                                            HOLD|
|  ABT  P&L +1.2%  $+0.40                                            HOLD|
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
=== options_live_micro LIVE 2026-10-26T11:17:13.339984-04:00 share=25% ===
2026-10-26 11:17:13,340 INFO === options_live_micro LIVE 2026-10-26T11:17:13.339984-04:00 share=25% ===
Live account equity $227.80 cash $125.00 #225458845 options_level=3
2026-10-26 11:17:13,539 INFO Live account equity $227.80 cash $125.00 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-10-26 11:17:13,713 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-10-26 11:17:13,825 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (216 earlier lines - see full log file)
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
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-26
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1917 | WARN | <<<
| Missing exit records (post) |  1917 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     7 | INFO |
| Total closed lots           |  2901 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1745 med=-28.6% | TAINTED n=2045 med=-41.5% | KEEP-only n=848 med=+50.8% | KILL=22 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.79 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261026T152157Z

- UTC timestamp: `20261026T152157Z`
- GitHub run: [#13826](https://github.com/28twagg-ops/TradingBot/actions/runs/40348281430)
- Run id: `40348281430`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`65s`
- Full logs: `logs/action_runs/20261026T152157Z_live_bot.log`, `logs/action_runs/20261026T152157Z_live_options.log`, `logs/action_runs/20261026T152157Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1745 | 48.1 | -28.6 | +35.9 | $+18,447 |
| TAINTED | 2045 | 31.7 | -41.5 | +9.6 | $-11,919 |
| KEEP-only | 848 | 60.5 | +50.8 | +52.0 | $+12,505 |
| KEEP-only recent | 663 | 59.4 | +52.9 | +58.1 | $+8,996 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S396, S397, S403, S404, S406, S410, S411
- KILL strategies (22): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-26T11:22:05.382781-04:00","date":"2026-10-26","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":52.1,"phases_s":{"reconcile":0.62,"cancel":0.16,"manage":2.55,"protective_stops":0.62,"scan":46.23,"entries":0.09,"reconcile2":0.5},"signals":126,"placed":0,"equity":992601.7,"open_positions":7,"pending_orders":1,"open_lots":7,"submitted_today":14,"filled_today":13,"unattributed_contracts":0,"top_signals":["S430:NVDA","S432:NVDA","S210:TSLA","S430:TSLA","S432:TSLA","S164:COIN","S168:COIN","S167:COIN"],"github_run":"13826","github_run_id":"40348281430","status":"ok","data_quality":{"clean":{"n":1745,"win":48.14,"med":-28.57,"avg":35.9,"pnl":18446.83},"tainted":{"n":2045,"win":31.69,"med":-41.46,"avg":9.56,"pnl":-11919.28},"keep_only":{"n":848,"win":60.5,"med":50.82,"avg":51.98,"pnl":12505.45},"keep_only_recent":{"n":663,"win":59.43,"med":52.94,"avg":58.05,"pnl":8996.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S396","S397","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:21:58  INFO      Mode: exits
15:21:59  INFO        Daily log -> logs/daily/2026-10-26.md
15:21:59  INFO        Daily log reconciled -> logs/daily/2026-10-26.md (1 ledger rows)
15:21:59  INFO        place_all_stops: checking 3 positions...
15:21:59  INFO        STOP skipped ABT: fractional (0.3291 shares) — software exit will handle it
15:21:59  INFO        STOP already live AES @ $14.92
15:21:59  INFO        STOP skipped AME: fractional (0.1401 shares) — software exit will handle it
15:22:00  INFO        [positions] 3/3 (3 valid)
15:22:00  INFO        Daily log -> logs/daily/2026-10-26.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.83|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AES  P&L -0.1%  $-0.05                                            HOLD|
|  AME  P&L +0.6%  $+0.20                                            HOLD|
|  ABT  P&L +1.3%  $+0.44                                            HOLD|
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
=== options_live_micro LIVE 2026-10-26T11:22:01.345732-04:00 share=25% ===
2026-10-26 11:22:01,345 INFO === options_live_micro LIVE 2026-10-26T11:22:01.345732-04:00 share=25% ===
Live account equity $227.84 cash $125.00 #225458845 options_level=3
2026-10-26 11:22:01,601 INFO Live account equity $227.84 cash $125.00 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-10-26 11:22:01,819 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-10-26 11:22:01,964 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (216 earlier lines - see full log file)
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
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-26
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1917 | WARN | <<<
| Missing exit records (post) |  1917 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     7 | INFO |
| Total closed lots           |  2901 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1745 med=-28.6% | TAINTED n=2045 med=-41.5% | KEEP-only n=848 med=+50.8% | KILL=22 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.83 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261026T152650Z

- UTC timestamp: `20261026T152650Z`
- GitHub run: [#13827](https://github.com/28twagg-ops/TradingBot/actions/runs/40349092062)
- Run id: `40349092062`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`60s`
- Full logs: `logs/action_runs/20261026T152650Z_live_bot.log`, `logs/action_runs/20261026T152650Z_live_options.log`, `logs/action_runs/20261026T152650Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1745 | 48.1 | -28.6 | +35.9 | $+18,447 |
| TAINTED | 2045 | 31.7 | -41.5 | +9.6 | $-11,919 |
| KEEP-only | 848 | 60.5 | +50.8 | +52.0 | $+12,505 |
| KEEP-only recent | 663 | 59.4 | +52.9 | +58.1 | $+8,996 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S396, S397, S403, S404, S406, S410, S411
- KILL strategies (22): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-26T11:26:56.564999-04:00","date":"2026-10-26","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":47.5,"phases_s":{"reconcile":0.24,"cancel":0.07,"manage":1.13,"protective_stops":0.28,"scan":44.57,"entries":0.05,"reconcile2":0.28},"signals":126,"placed":0,"equity":992498.26,"open_positions":7,"pending_orders":1,"open_lots":7,"submitted_today":14,"filled_today":13,"unattributed_contracts":0,"top_signals":["S430:NVDA","S432:NVDA","S210:TSLA","S430:TSLA","S432:TSLA","S164:COIN","S168:COIN","S167:COIN"],"github_run":"13827","github_run_id":"40349092062","status":"ok","data_quality":{"clean":{"n":1745,"win":48.14,"med":-28.57,"avg":35.9,"pnl":18446.83},"tainted":{"n":2045,"win":31.69,"med":-41.46,"avg":9.56,"pnl":-11919.28},"keep_only":{"n":848,"win":60.5,"med":50.82,"avg":51.98,"pnl":12505.45},"keep_only_recent":{"n":663,"win":59.43,"med":52.94,"avg":58.05,"pnl":8996.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S396","S397","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:26:51  INFO      Mode: exits
15:26:52  INFO        Daily log -> logs/daily/2026-10-26.md
15:26:52  INFO        Daily log reconciled -> logs/daily/2026-10-26.md (1 ledger rows)
15:26:52  INFO        place_all_stops: checking 3 positions...
15:26:52  INFO        STOP skipped ABT: fractional (0.3291 shares) — software exit will handle it
15:26:52  INFO        STOP already live AES @ $14.92
15:26:52  INFO        STOP skipped AME: fractional (0.1401 shares) — software exit will handle it
15:26:52  INFO        [positions] 3/3 (3 valid)
15:26:52  INFO        Daily log -> logs/daily/2026-10-26.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.88|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AES  P&L -0.1%  $-0.03                                            HOLD|
|  AME  P&L +0.7%  $+0.23                                            HOLD|
|  ABT  P&L +1.3%  $+0.45                                            HOLD|
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
=== options_live_micro LIVE 2026-10-26T11:26:53.433470-04:00 share=25% ===
2026-10-26 11:26:53,433 INFO === options_live_micro LIVE 2026-10-26T11:26:53.433470-04:00 share=25% ===
Live account equity $227.89 cash $125.00 #225458845 options_level=3
2026-10-26 11:26:53,598 INFO Live account equity $227.89 cash $125.00 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-10-26 11:26:53,737 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-10-26 11:26:53,829 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (216 earlier lines - see full log file)
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
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-26
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1917 | WARN | <<<
| Missing exit records (post) |  1917 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     7 | INFO |
| Total closed lots           |  2901 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1745 med=-28.6% | TAINTED n=2045 med=-41.5% | KEEP-only n=848 med=+50.8% | KILL=22 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.88 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261026T153149Z

- UTC timestamp: `20261026T153149Z`
- GitHub run: [#13828](https://github.com/28twagg-ops/TradingBot/actions/runs/40349916667)
- Run id: `40349916667`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`45s`
- Full logs: `logs/action_runs/20261026T153149Z_live_bot.log`, `logs/action_runs/20261026T153149Z_live_options.log`, `logs/action_runs/20261026T153149Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1745 | 48.1 | -28.6 | +35.9 | $+18,447 |
| TAINTED | 2045 | 31.7 | -41.5 | +9.6 | $-11,919 |
| KEEP-only | 848 | 60.5 | +50.8 | +52.0 | $+12,505 |
| KEEP-only recent | 663 | 59.4 | +52.9 | +58.1 | $+8,996 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S396, S397, S403, S404, S406, S410, S411
- KILL strategies (22): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-26T11:31:56.045001-04:00","date":"2026-10-26","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":33.6,"phases_s":{"reconcile":0.38,"cancel":0.12,"manage":1.56,"protective_stops":0.49,"scan":29.51,"entries":0.08,"reconcile2":0.38},"signals":126,"placed":0,"equity":992515.73,"open_positions":7,"pending_orders":1,"open_lots":7,"submitted_today":14,"filled_today":13,"unattributed_contracts":0,"top_signals":["S430:NVDA","S432:NVDA","S210:TSLA","S430:TSLA","S432:TSLA","S164:COIN","S168:COIN","S167:COIN"],"github_run":"13828","github_run_id":"40349916667","status":"ok","data_quality":{"clean":{"n":1745,"win":48.14,"med":-28.57,"avg":35.9,"pnl":18446.83},"tainted":{"n":2045,"win":31.69,"med":-41.46,"avg":9.56,"pnl":-11919.28},"keep_only":{"n":848,"win":60.5,"med":50.82,"avg":51.98,"pnl":12505.45},"keep_only_recent":{"n":663,"win":59.43,"med":52.94,"avg":58.05,"pnl":8996.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S396","S397","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:31:50  INFO      Mode: exits
15:31:51  INFO        Daily log -> logs/daily/2026-10-26.md
15:31:51  INFO        Daily log reconciled -> logs/daily/2026-10-26.md (1 ledger rows)
15:31:51  INFO        place_all_stops: checking 3 positions...
15:31:51  INFO        STOP skipped ABT: fractional (0.3291 shares) — software exit will handle it
15:31:51  INFO        STOP already live AES @ $14.92
15:31:51  INFO        STOP skipped AME: fractional (0.1401 shares) — software exit will handle it
15:31:51  INFO        [positions] 3/3 (3 valid)
15:31:52  INFO        Daily log -> logs/daily/2026-10-26.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.82|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AES  P&L -0.1%  $-0.05                                            HOLD|
|  AME  P&L +0.6%  $+0.20                                            HOLD|
|  ABT  P&L +1.3%  $+0.43                                            HOLD|
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
=== options_live_micro LIVE 2026-10-26T11:31:52.811535-04:00 share=25% ===
2026-10-26 11:31:52,811 INFO === options_live_micro LIVE 2026-10-26T11:31:52.811535-04:00 share=25% ===
Live account equity $227.82 cash $125.00 #225458845 options_level=3
2026-10-26 11:31:53,007 INFO Live account equity $227.82 cash $125.00 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-10-26 11:31:53,179 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-10-26 11:31:53,293 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (216 earlier lines - see full log file)
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
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-26
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1917 | WARN | <<<
| Missing exit records (post) |  1917 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     7 | INFO |
| Total closed lots           |  2901 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1745 med=-28.6% | TAINTED n=2045 med=-41.5% | KEEP-only n=848 med=+50.8% | KILL=22 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.82 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261026T153648Z

- UTC timestamp: `20261026T153648Z`
- GitHub run: [#13829](https://github.com/28twagg-ops/TradingBot/actions/runs/40350740172)
- Run id: `40350740172`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`13s`
- Full logs: `logs/action_runs/20261026T153648Z_live_bot.log`, `logs/action_runs/20261026T153648Z_live_options.log`, `logs/action_runs/20261026T153648Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1745 | 48.1 | -28.6 | +35.9 | $+18,447 |
| TAINTED | 2045 | 31.7 | -41.5 | +9.6 | $-11,919 |
| KEEP-only | 848 | 60.5 | +50.8 | +52.0 | $+12,505 |
| KEEP-only recent | 663 | 59.4 | +52.9 | +58.1 | $+8,996 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S396, S397, S403, S404, S406, S410, S411
- KILL strategies (22): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-26T11:36:53.775777-04:00","date":"2026-10-26","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":1.3,"phases_s":{"reconcile":0.1,"cancel":0.04,"manage":0.53,"protective_stops":0.09},"signals":0,"placed":0,"equity":992492.96,"open_positions":7,"pending_orders":1,"open_lots":7,"submitted_today":14,"filled_today":13,"unattributed_contracts":0,"top_signals":[],"github_run":"13829","github_run_id":"40350740172","status":"ok","data_quality":{"clean":{"n":1745,"win":48.14,"med":-28.57,"avg":35.9,"pnl":18446.83},"tainted":{"n":2045,"win":31.69,"med":-41.46,"avg":9.56,"pnl":-11919.28},"keep_only":{"n":848,"win":60.5,"med":50.82,"avg":51.98,"pnl":12505.45},"keep_only_recent":{"n":663,"win":59.43,"med":52.94,"avg":58.05,"pnl":8996.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S396","S397","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:36:49  INFO      Mode: exits
15:36:49  INFO        Daily log -> logs/daily/2026-10-26.md
15:36:49  INFO        Daily log reconciled -> logs/daily/2026-10-26.md (1 ledger rows)
15:36:49  INFO        place_all_stops: checking 3 positions...
15:36:49  INFO        STOP skipped ABT: fractional (0.3291 shares) — software exit will handle it
15:36:49  INFO        STOP already live AES @ $14.92
15:36:49  INFO        STOP skipped AME: fractional (0.1401 shares) — software exit will handle it
15:36:50  INFO        [positions] 3/3 (3 valid)
15:36:50  INFO        Daily log -> logs/daily/2026-10-26.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.79|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AES  P&L -0.1%  $-0.04                                            HOLD|
|  AME  P&L +0.5%  $+0.18                                            HOLD|
|  ABT  P&L +1.2%  $+0.41                                            HOLD|
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
=== options_live_micro LIVE 2026-10-26T11:36:51.134590-04:00 share=25% ===
2026-10-26 11:36:51,134 INFO === options_live_micro LIVE 2026-10-26T11:36:51.134590-04:00 share=25% ===
Live account equity $227.79 cash $125.00 #225458845 options_level=3
2026-10-26 11:36:51,176 INFO Live account equity $227.79 cash $125.00 #225458845 options_level=3
Live micro: manage/exits only
2026-10-26 11:36:51,202 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-10-26 11:36:51,209 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (212 earlier lines - see full log file)
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
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-26
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1917 | WARN | <<<
| Missing exit records (post) |  1917 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     7 | INFO |
| Total closed lots           |  2901 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1745 med=-28.6% | TAINTED n=2045 med=-41.5% | KEEP-only n=848 med=+50.8% | KILL=22 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.79 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261026T154154Z

- UTC timestamp: `20261026T154154Z`
- GitHub run: [#13830](https://github.com/28twagg-ops/TradingBot/actions/runs/40351557217)
- Run id: `40351557217`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`15s`
- Full logs: `logs/action_runs/20261026T154154Z_live_bot.log`, `logs/action_runs/20261026T154154Z_live_options.log`, `logs/action_runs/20261026T154154Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1745 | 48.1 | -28.6 | +35.9 | $+18,447 |
| TAINTED | 2045 | 31.7 | -41.5 | +9.6 | $-11,919 |
| KEEP-only | 848 | 60.5 | +50.8 | +52.0 | $+12,505 |
| KEEP-only recent | 663 | 59.4 | +52.9 | +58.1 | $+8,996 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S396, S397, S403, S404, S406, S410, S411
- KILL strategies (22): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-26T11:41:59.695038-04:00","date":"2026-10-26","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":2.4,"phases_s":{"reconcile":0.2,"cancel":0.09,"manage":1.33,"protective_stops":0.19},"signals":0,"placed":0,"equity":992449.92,"open_positions":7,"pending_orders":0,"open_lots":7,"submitted_today":14,"filled_today":13,"unattributed_contracts":0,"top_signals":[],"github_run":"13830","github_run_id":"40351557217","status":"ok","data_quality":{"clean":{"n":1745,"win":48.14,"med":-28.57,"avg":35.9,"pnl":18446.83},"tainted":{"n":2045,"win":31.69,"med":-41.46,"avg":9.56,"pnl":-11919.28},"keep_only":{"n":848,"win":60.5,"med":50.82,"avg":51.98,"pnl":12505.45},"keep_only_recent":{"n":663,"win":59.43,"med":52.94,"avg":58.05,"pnl":8996.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S396","S397","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:41:55  INFO      Mode: exits
15:41:55  INFO        Daily log -> logs/daily/2026-10-26.md
15:41:55  INFO        Daily log reconciled -> logs/daily/2026-10-26.md (1 ledger rows)
15:41:55  INFO        place_all_stops: checking 3 positions...
15:41:55  INFO        STOP skipped ABT: fractional (0.3291 shares) — software exit will handle it
15:41:55  INFO        STOP already live AES @ $14.92
15:41:55  INFO        STOP skipped AME: fractional (0.1401 shares) — software exit will handle it
15:41:55  INFO        [positions] 3/3 (3 valid)
15:41:56  INFO        Daily log -> logs/daily/2026-10-26.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.85|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AES  P&L -0.1%  $-0.02                                            HOLD|
|  AME  P&L +0.6%  $+0.22                                            HOLD|
|  ABT  P&L +1.2%  $+0.42                                            HOLD|
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
=== options_live_micro LIVE 2026-10-26T11:41:56.871646-04:00 share=25% ===
2026-10-26 11:41:56,871 INFO === options_live_micro LIVE 2026-10-26T11:41:56.871646-04:00 share=25% ===
Live account equity $227.85 cash $125.00 #225458845 options_level=3
2026-10-26 11:41:56,980 INFO Live account equity $227.85 cash $125.00 #225458845 options_level=3
Live micro: manage/exits only
2026-10-26 11:41:57,054 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-10-26 11:41:57,079 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (204 earlier lines - see full log file)
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
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-26
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1917 | WARN | <<<
| Missing exit records (post) |  1917 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     7 | INFO |
| Total closed lots           |  2901 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1745 med=-28.6% | TAINTED n=2045 med=-41.5% | KEEP-only n=848 med=+50.8% | KILL=22 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.85 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261026T154654Z

- UTC timestamp: `20261026T154654Z`
- GitHub run: [#13831](https://github.com/28twagg-ops/TradingBot/actions/runs/40352376803)
- Run id: `40352376803`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`11s`
- Full logs: `logs/action_runs/20261026T154654Z_live_bot.log`, `logs/action_runs/20261026T154654Z_live_options.log`, `logs/action_runs/20261026T154654Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1745 | 48.1 | -28.6 | +35.9 | $+18,447 |
| TAINTED | 2045 | 31.7 | -41.5 | +9.6 | $-11,919 |
| KEEP-only | 848 | 60.5 | +50.8 | +52.0 | $+12,505 |
| KEEP-only recent | 663 | 59.4 | +52.9 | +58.1 | $+8,996 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S396, S397, S403, S404, S406, S410, S411
- KILL strategies (22): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-26T11:46:59.198485-04:00","date":"2026-10-26","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":3.0,"phases_s":{"reconcile":0.31,"cancel":0.12,"manage":1.74,"protective_stops":0.31},"signals":0,"placed":0,"equity":992442.26,"open_positions":7,"pending_orders":0,"open_lots":7,"submitted_today":14,"filled_today":13,"unattributed_contracts":0,"top_signals":[],"github_run":"13831","github_run_id":"40352376803","status":"ok","data_quality":{"clean":{"n":1745,"win":48.14,"med":-28.57,"avg":35.9,"pnl":18446.83},"tainted":{"n":2045,"win":31.69,"med":-41.46,"avg":9.56,"pnl":-11919.28},"keep_only":{"n":848,"win":60.5,"med":50.82,"avg":51.98,"pnl":12505.45},"keep_only_recent":{"n":663,"win":59.43,"med":52.94,"avg":58.05,"pnl":8996.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S396","S397","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:46:55  INFO      Mode: exits
15:46:55  INFO        Daily log -> logs/daily/2026-10-26.md
15:46:55  INFO        Daily log reconciled -> logs/daily/2026-10-26.md (1 ledger rows)
15:46:55  INFO        place_all_stops: checking 3 positions...
15:46:55  INFO        STOP skipped ABT: fractional (0.3291 shares) — software exit will handle it
15:46:55  INFO        STOP already live AES @ $14.92
15:46:55  INFO        STOP skipped AME: fractional (0.1401 shares) — software exit will handle it
15:46:56  INFO        [positions] 3/3 (3 valid)
15:46:56  INFO        Daily log -> logs/daily/2026-10-26.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.81|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AES  P&L -0.1%  $-0.03                                            HOLD|
|  AME  P&L +0.5%  $+0.18                                            HOLD|
|  ABT  P&L +1.3%  $+0.43                                            HOLD|
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
=== options_live_micro LIVE 2026-10-26T11:46:56.885157-04:00 share=25% ===
2026-10-26 11:46:56,885 INFO === options_live_micro LIVE 2026-10-26T11:46:56.885157-04:00 share=25% ===
Live account equity $227.81 cash $125.00 #225458845 options_level=3
2026-10-26 11:46:57,039 INFO Live account equity $227.81 cash $125.00 #225458845 options_level=3
Live micro: manage/exits only
2026-10-26 11:46:57,166 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-10-26 11:46:57,209 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (204 earlier lines - see full log file)
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
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-26
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1917 | WARN | <<<
| Missing exit records (post) |  1917 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     7 | INFO |
| Total closed lots           |  2901 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1745 med=-28.6% | TAINTED n=2045 med=-41.5% | KEEP-only n=848 med=+50.8% | KILL=22 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.81 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261026T155144Z

- UTC timestamp: `20261026T155144Z`
- GitHub run: [#13832](https://github.com/28twagg-ops/TradingBot/actions/runs/40353196811)
- Run id: `40353196811`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`14s`
- Full logs: `logs/action_runs/20261026T155144Z_live_bot.log`, `logs/action_runs/20261026T155144Z_live_options.log`, `logs/action_runs/20261026T155144Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1745 | 48.1 | -28.6 | +35.9 | $+18,447 |
| TAINTED | 2045 | 31.7 | -41.5 | +9.6 | $-11,919 |
| KEEP-only | 848 | 60.5 | +50.8 | +52.0 | $+12,505 |
| KEEP-only recent | 663 | 59.4 | +52.9 | +58.1 | $+8,996 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S396, S397, S403, S404, S406, S410, S411
- KILL strategies (22): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-26T11:51:50.802995-04:00","date":"2026-10-26","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":3.2,"phases_s":{"reconcile":0.39,"cancel":0.19,"manage":1.48,"protective_stops":0.49},"signals":0,"placed":0,"equity":992490.76,"open_positions":7,"pending_orders":0,"open_lots":7,"submitted_today":14,"filled_today":13,"unattributed_contracts":0,"top_signals":[],"github_run":"13832","github_run_id":"40353196811","status":"ok","data_quality":{"clean":{"n":1745,"win":48.14,"med":-28.57,"avg":35.9,"pnl":18446.83},"tainted":{"n":2045,"win":31.69,"med":-41.46,"avg":9.56,"pnl":-11919.28},"keep_only":{"n":848,"win":60.5,"med":50.82,"avg":51.98,"pnl":12505.45},"keep_only_recent":{"n":663,"win":59.43,"med":52.94,"avg":58.05,"pnl":8996.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S396","S397","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:51:45  INFO      Mode: exits
15:51:46  INFO        Daily log -> logs/daily/2026-10-26.md
15:51:46  INFO        Daily log reconciled -> logs/daily/2026-10-26.md (1 ledger rows)
15:51:46  INFO        place_all_stops: checking 3 positions...
15:51:46  INFO        STOP skipped ABT: fractional (0.3291 shares) — software exit will handle it
15:51:46  INFO        STOP already live AES @ $14.92
15:51:46  INFO        STOP skipped AME: fractional (0.1401 shares) — software exit will handle it
15:51:46  INFO        [positions] 3/3 (3 valid)
15:51:47  INFO        Daily log -> logs/daily/2026-10-26.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:51 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.71|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AES  P&L -0.1%  $-0.02                                            HOLD|
|  AME  P&L +0.3%  $+0.11                                            HOLD|
|  ABT  P&L +1.2%  $+0.39                                            HOLD|
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
=== options_live_micro LIVE 2026-10-26T11:51:47.823990-04:00 share=25% ===
2026-10-26 11:51:47,824 INFO === options_live_micro LIVE 2026-10-26T11:51:47.823990-04:00 share=25% ===
Live account equity $227.73 cash $125.00 #225458845 options_level=3
2026-10-26 11:51:48,019 INFO Live account equity $227.73 cash $125.00 #225458845 options_level=3
Live micro: manage/exits only
2026-10-26 11:51:48,191 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-10-26 11:51:48,248 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (204 earlier lines - see full log file)
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
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-26
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1917 | WARN | <<<
| Missing exit records (post) |  1917 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     7 | INFO |
| Total closed lots           |  2901 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1745 med=-28.6% | TAINTED n=2045 med=-41.5% | KEEP-only n=848 med=+50.8% | KILL=22 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.73 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261026T155713Z

- UTC timestamp: `20261026T155713Z`
- GitHub run: [#13833](https://github.com/28twagg-ops/TradingBot/actions/runs/40354010563)
- Run id: `40354010563`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`11s`
- Full logs: `logs/action_runs/20261026T155713Z_live_bot.log`, `logs/action_runs/20261026T155713Z_live_options.log`, `logs/action_runs/20261026T155713Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1745 | 48.1 | -28.6 | +35.9 | $+18,447 |
| TAINTED | 2045 | 31.7 | -41.5 | +9.6 | $-11,919 |
| KEEP-only | 848 | 60.5 | +50.8 | +52.0 | $+12,505 |
| KEEP-only recent | 663 | 59.4 | +52.9 | +58.1 | $+8,996 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S396, S397, S403, S404, S406, S410, S411
- KILL strategies (22): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-26T11:57:18.985486-04:00","date":"2026-10-26","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":2.2,"phases_s":{"reconcile":0.24,"cancel":0.1,"manage":1.14,"protective_stops":0.25},"signals":0,"placed":0,"equity":992469.16,"open_positions":7,"pending_orders":0,"open_lots":7,"submitted_today":14,"filled_today":13,"unattributed_contracts":0,"top_signals":[],"github_run":"13833","github_run_id":"40354010563","status":"ok","data_quality":{"clean":{"n":1745,"win":48.14,"med":-28.57,"avg":35.9,"pnl":18446.83},"tainted":{"n":2045,"win":31.69,"med":-41.46,"avg":9.56,"pnl":-11919.28},"keep_only":{"n":848,"win":60.5,"med":50.82,"avg":51.98,"pnl":12505.45},"keep_only_recent":{"n":663,"win":59.43,"med":52.94,"avg":58.05,"pnl":8996.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S396","S397","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:57:14  INFO      Mode: exits
15:57:15  INFO        Daily log -> logs/daily/2026-10-26.md
15:57:15  INFO        Daily log reconciled -> logs/daily/2026-10-26.md (1 ledger rows)
15:57:15  INFO        place_all_stops: checking 3 positions...
15:57:15  INFO        STOP skipped ABT: fractional (0.3291 shares) — software exit will handle it
15:57:15  INFO        STOP already live AES @ $14.92
15:57:15  INFO        STOP skipped AME: fractional (0.1401 shares) — software exit will handle it
15:57:15  INFO        [positions] 3/3 (3 valid)
15:57:16  INFO        Daily log -> logs/daily/2026-10-26.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:57 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.70|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AES  P&L -0.0%  $-0.01                                            HOLD|
|  AME  P&L +0.3%  $+0.11                                            HOLD|
|  ABT  P&L +1.1%  $+0.36                                            HOLD|
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
=== options_live_micro LIVE 2026-10-26T11:57:16.555179-04:00 share=25% ===
2026-10-26 11:57:16,555 INFO === options_live_micro LIVE 2026-10-26T11:57:16.555179-04:00 share=25% ===
Live account equity $227.70 cash $125.00 #225458845 options_level=3
2026-10-26 11:57:16,686 INFO Live account equity $227.70 cash $125.00 #225458845 options_level=3
Live micro: manage/exits only
2026-10-26 11:57:16,842 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-10-26 11:57:16,878 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (204 earlier lines - see full log file)
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
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-26
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1917 | WARN | <<<
| Missing exit records (post) |  1917 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     7 | INFO |
| Total closed lots           |  2901 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1745 med=-28.6% | TAINTED n=2045 med=-41.5% | KEEP-only n=848 med=+50.8% | KILL=22 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.7 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261026T160154Z

- UTC timestamp: `20261026T160154Z`
- GitHub run: [#13834](https://github.com/28twagg-ops/TradingBot/actions/runs/40354831933)
- Run id: `40354831933`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`19s`
- Full logs: `logs/action_runs/20261026T160154Z_live_bot.log`, `logs/action_runs/20261026T160154Z_live_options.log`, `logs/action_runs/20261026T160154Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1745 | 48.1 | -28.6 | +35.9 | $+18,447 |
| TAINTED | 2045 | 31.7 | -41.5 | +9.6 | $-11,919 |
| KEEP-only | 848 | 60.5 | +50.8 | +52.0 | $+12,505 |
| KEEP-only recent | 663 | 59.4 | +52.9 | +58.1 | $+8,996 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S396, S397, S403, S404, S406, S410, S411
- KILL strategies (22): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-26T12:02:01.480309-04:00","date":"2026-10-26","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":6.2,"phases_s":{"reconcile":0.59,"cancel":0.25,"manage":3.97,"protective_stops":0.55},"signals":0,"placed":0,"equity":992572.55,"open_positions":7,"pending_orders":0,"open_lots":7,"submitted_today":14,"filled_today":13,"unattributed_contracts":0,"top_signals":[],"github_run":"13834","github_run_id":"40354831933","status":"ok","data_quality":{"clean":{"n":1745,"win":48.14,"med":-28.57,"avg":35.9,"pnl":18446.83},"tainted":{"n":2045,"win":31.69,"med":-41.46,"avg":9.56,"pnl":-11919.28},"keep_only":{"n":848,"win":60.5,"med":50.82,"avg":51.98,"pnl":12505.45},"keep_only_recent":{"n":663,"win":59.43,"med":52.94,"avg":58.05,"pnl":8996.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S396","S397","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
16:01:55  INFO      Mode: exits
16:01:55  INFO        Daily log -> logs/daily/2026-10-26.md
16:01:55  INFO        Daily log reconciled -> logs/daily/2026-10-26.md (1 ledger rows)
16:01:56  INFO        place_all_stops: checking 3 positions...
16:01:56  INFO        STOP skipped ABT: fractional (0.3291 shares) — software exit will handle it
16:01:56  INFO        STOP already live AES @ $14.92
16:01:56  INFO        STOP skipped AME: fractional (0.1401 shares) — software exit will handle it
16:01:56  INFO        [positions] 3/3 (3 valid)
16:01:56  INFO        Daily log -> logs/daily/2026-10-26.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.59|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AES  P&L -0.1%  $-0.03                                            HOLD|
|  AME  P&L +0.2%  $+0.08                                            HOLD|
|  ABT  P&L +0.9%  $+0.31                                            HOLD|
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
=== options_live_micro LIVE 2026-10-26T12:01:57.734665-04:00 share=25% ===
2026-10-26 12:01:57,734 INFO === options_live_micro LIVE 2026-10-26T12:01:57.734665-04:00 share=25% ===
Live account equity $227.59 cash $125.00 #225458845 options_level=3
2026-10-26 12:01:57,959 INFO Live account equity $227.59 cash $125.00 #225458845 options_level=3
Live micro: manage/exits only
2026-10-26 12:01:58,167 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-10-26 12:01:58,236 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (210 earlier lines - see full log file)
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
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-26
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1917 | WARN | <<<
| Missing exit records (post) |  1917 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     7 | INFO |
| Total closed lots           |  2901 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1745 med=-28.6% | TAINTED n=2045 med=-41.5% | KEEP-only n=848 med=+50.8% | KILL=22 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.59 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261026T160646Z

- UTC timestamp: `20261026T160646Z`
- GitHub run: [#13835](https://github.com/28twagg-ops/TradingBot/actions/runs/40355644376)
- Run id: `40355644376`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`14s`
- Full logs: `logs/action_runs/20261026T160646Z_live_bot.log`, `logs/action_runs/20261026T160646Z_live_options.log`, `logs/action_runs/20261026T160646Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1746 | 48.1 | -29.3 | +35.9 | $+18,432 |
| TAINTED | 2045 | 31.7 | -41.5 | +9.6 | $-11,919 |
| KEEP-only | 849 | 60.4 | +50.8 | +51.9 | $+12,490 |
| KEEP-only recent | 664 | 59.3 | +52.9 | +57.9 | $+8,981 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S396, S397, S403, S404, S406, S410, S411
- KILL strategies (22): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-26T12:06:52.964134-04:00","date":"2026-10-26","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":3.4,"phases_s":{"reconcile":0.5,"cancel":0.21,"manage":1.47,"protective_stops":0.5},"signals":0,"placed":0,"equity":992641.24,"open_positions":6,"pending_orders":0,"open_lots":6,"submitted_today":14,"filled_today":13,"unattributed_contracts":0,"top_signals":[],"github_run":"13835","github_run_id":"40355644376","status":"ok","data_quality":{"clean":{"n":1746,"win":48.11,"med":-29.29,"avg":35.86,"pnl":18431.83},"tainted":{"n":2045,"win":31.69,"med":-41.46,"avg":9.56,"pnl":-11919.28},"keep_only":{"n":849,"win":60.42,"med":50.79,"avg":51.87,"pnl":12490.45},"keep_only_recent":{"n":664,"win":59.34,"med":52.94,"avg":57.91,"pnl":8981.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S396","S397","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
16:06:47  INFO      Mode: exits
16:06:48  INFO        Daily log -> logs/daily/2026-10-26.md
16:06:48  INFO        Daily log reconciled -> logs/daily/2026-10-26.md (1 ledger rows)
16:06:48  INFO        place_all_stops: checking 3 positions...
16:06:48  INFO        STOP skipped ABT: fractional (0.3291 shares) — software exit will handle it
16:06:48  INFO        STOP already live AES @ $14.92
16:06:48  INFO        STOP skipped AME: fractional (0.1401 shares) — software exit will handle it
16:06:48  INFO        [positions] 3/3 (3 valid)
16:06:49  INFO        Daily log -> logs/daily/2026-10-26.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.66|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AES  P&L -0.1%  $-0.02                                            HOLD|
|  AME  P&L +0.2%  $+0.08                                            HOLD|
|  ABT  P&L +1.1%  $+0.36                                            HOLD|
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
=== options_live_micro LIVE 2026-10-26T12:06:49.750793-04:00 share=25% ===
2026-10-26 12:06:49,750 INFO === options_live_micro LIVE 2026-10-26T12:06:49.750793-04:00 share=25% ===
Live account equity $227.66 cash $125.00 #225458845 options_level=3
2026-10-26 12:06:49,980 INFO Live account equity $227.66 cash $125.00 #225458845 options_level=3
Live micro: manage/exits only
2026-10-26 12:06:50,190 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-10-26 12:06:50,258 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (206 earlier lines - see full log file)
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
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-26
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1917 | WARN | <<<
| Missing exit records (post) |  1917 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     6 | INFO |
| Total closed lots           |  2902 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1746 med=-29.3% | TAINTED n=2045 med=-41.5% | KEEP-only n=849 med=+50.8% | KILL=22 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.66 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261026T161149Z

- UTC timestamp: `20261026T161149Z`
- GitHub run: [#13836](https://github.com/28twagg-ops/TradingBot/actions/runs/40356458847)
- Run id: `40356458847`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`11s`
- Full logs: `logs/action_runs/20261026T161149Z_live_bot.log`, `logs/action_runs/20261026T161149Z_live_options.log`, `logs/action_runs/20261026T161149Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1746 | 48.1 | -29.3 | +35.9 | $+18,432 |
| TAINTED | 2045 | 31.7 | -41.5 | +9.6 | $-11,919 |
| KEEP-only | 849 | 60.4 | +50.8 | +51.9 | $+12,490 |
| KEEP-only recent | 664 | 59.3 | +52.9 | +57.9 | $+8,981 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S396, S397, S403, S404, S406, S410, S411
- KILL strategies (22): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-26T12:11:55.489047-04:00","date":"2026-10-26","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":2.5,"phases_s":{"reconcile":0.3,"cancel":0.14,"manage":1.15,"protective_stops":0.32},"signals":0,"placed":0,"equity":992585.83,"open_positions":6,"pending_orders":0,"open_lots":6,"submitted_today":14,"filled_today":13,"unattributed_contracts":0,"top_signals":[],"github_run":"13836","github_run_id":"40356458847","status":"ok","data_quality":{"clean":{"n":1746,"win":48.11,"med":-29.29,"avg":35.86,"pnl":18431.83},"tainted":{"n":2045,"win":31.69,"med":-41.46,"avg":9.56,"pnl":-11919.28},"keep_only":{"n":849,"win":60.42,"med":50.79,"avg":51.87,"pnl":12490.45},"keep_only_recent":{"n":664,"win":59.34,"med":52.94,"avg":57.91,"pnl":8981.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S396","S397","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
16:11:50  INFO      Mode: exits
16:11:51  INFO        Daily log -> logs/daily/2026-10-26.md
16:11:51  INFO        Daily log reconciled -> logs/daily/2026-10-26.md (1 ledger rows)
16:11:51  INFO        place_all_stops: checking 3 positions...
16:11:51  INFO        STOP skipped ABT: fractional (0.3291 shares) — software exit will handle it
16:11:51  INFO        STOP already live AES @ $14.92
16:11:51  INFO        STOP skipped AME: fractional (0.1401 shares) — software exit will handle it
16:11:51  INFO        [positions] 3/3 (3 valid)
16:11:51  INFO        Daily log -> logs/daily/2026-10-26.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $227.65|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AES  P&L -0.0%  $-0.01                                            HOLD|
|  AME  P&L +0.2%  $+0.08                                            HOLD|
|  ABT  P&L +1.0%  $+0.34                                            HOLD|
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
=== options_live_micro LIVE 2026-10-26T12:11:52.533741-04:00 share=25% ===
2026-10-26 12:11:52,533 INFO === options_live_micro LIVE 2026-10-26T12:11:52.533741-04:00 share=25% ===
Live account equity $227.64 cash $125.00 #225458845 options_level=3
2026-10-26 12:11:52,678 INFO Live account equity $227.64 cash $125.00 #225458845 options_level=3
Live micro: manage/exits only
2026-10-26 12:11:52,800 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-10-26 12:11:52,840 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (203 earlier lines - see full log file)
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
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-26
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1917 | WARN | <<<
| Missing exit records (post) |  1917 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     6 | INFO |
| Total closed lots           |  2902 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-26_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1746 med=-29.3% | TAINTED n=2045 med=-41.5% | KEEP-only n=849 med=+50.8% | KILL=22 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=227.65 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---
