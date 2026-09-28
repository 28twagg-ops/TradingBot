# Daily Comprehensive Action Review - 2026-09-28

_Auto-generated from GitHub Actions run output. Each run appends a summary; full stdout is in linked per-run log files._
## Run 20260928T130122Z

- UTC timestamp: `20260928T130122Z`
- GitHub run: [#11163](https://github.com/28twagg-ops/TradingBot/actions/runs/36425509010)
- Run id: `36425509010`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`24s`
- Full logs: `logs/action_runs/20260928T130122Z_live_bot.log`, `logs/action_runs/20260928T130122Z_live_options.log`, `logs/action_runs/20260928T130122Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1508 | 50.2 | +8.6 | +43.6 | $+19,714 |
| TAINTED | 1908 | 33.4 | -38.8 | +12.7 | $-9,602 |
| KEEP-only | 798 | 63.3 | +52.8 | +66.8 | $+13,806 |
| KEEP-only recent | 603 | 62.5 | +56.9 | +76.9 | $+9,721 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T09:01:29.203386-04:00","date":"2026-09-28","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":11.2,"phases_s":{"reconcile":4.44},"signals":0,"placed":0,"equity":996963.17,"open_positions":18,"pending_orders":0,"open_lots":77,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11163","github_run_id":"36425509010","status":"ok","data_quality":{"clean":{"n":1508,"win":50.2,"med":8.63,"avg":43.62,"pnl":19714.16},"tainted":{"n":1908,"win":33.39,"med":-38.81,"avg":12.66,"pnl":-9602.28},"keep_only":{"n":798,"win":63.28,"med":52.75,"avg":66.75,"pnl":13806.45},"keep_only_recent":{"n":603,"win":62.52,"med":56.92,"avg":76.9,"pnl":9721.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:01:24  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.89|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $223.89|
|  Cash                                                           $156.73|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $67.16|
|  Open P&L                                                        $+0.02|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CVS      MomReversal     $33.63     $89.14   $89.30   +0.2%   $+0.06  |
|  EVR      MomReversal     $33.53     $262.43  $262.10  -0.1%   $-0.04  |
|                                                                        |
|  Total invested                                                  $67.16|
|  Total open P&L                                                  $+0.02|
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
|  2026-09-25  SELL  AYI  MomReversal  $33.58  P&L $+0.01                |
|  2026-09-25  SELL  COP  Pullback50  $33.54  P&L $-0.17                 |
|  2026-09-25  SELL  GOOG  Pullback50  $33.59  P&L $-0.01                |
|  2026-09-25  SELL  GOOGL  Pullback50  $33.59  P&L $-0.01               |
|  2026-09-25  SELL  KNF  MomReversal  $33.28  P&L $-0.47                |
|  2026-09-24  SELL  AES  Pullback50  $33.74  P&L $-0.02                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-28T09:01:25.441314-04:00 share=25% ===
2026-09-28 09:01:25,441 INFO === options_live_micro LIVE 2026-09-28T09:01:25.441314-04:00 share=25% ===
Live account equity $223.89 cash $156.73 #225458845 options_level=3
2026-09-28 09:01:25,575 INFO Live account equity $223.89 cash $156.73 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-28 09:01:25,607 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-28 09:01:25,639 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (189 earlier lines - see full log file)

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 293 | 21 |
| S164 | 333 | 24 |
| S165 | 1759 | 36 |
| S166 | 139 | 10 |
| S167 | 316 | 23 |
| S168 | 236 | 20 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-28
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1589 | WARN | <<<
| Missing exit records (post) |  1589 | WARN | <<<
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |    77 | INFO |
| Total closed lots           |  2539 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1508 med=+8.6% | TAINTED n=1908 med=-38.8% | KEEP-only n=798 med=+52.8% | KILL=19 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.89 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260928T130616Z

- UTC timestamp: `20260928T130616Z`
- GitHub run: [#11164](https://github.com/28twagg-ops/TradingBot/actions/runs/36426083938)
- Run id: `36426083938`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`21s`
- Full logs: `logs/action_runs/20260928T130616Z_live_bot.log`, `logs/action_runs/20260928T130616Z_live_options.log`, `logs/action_runs/20260928T130616Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1508 | 50.2 | +8.6 | +43.6 | $+19,714 |
| TAINTED | 1908 | 33.4 | -38.8 | +12.7 | $-9,602 |
| KEEP-only | 798 | 63.3 | +52.8 | +66.8 | $+13,806 |
| KEEP-only recent | 603 | 62.5 | +56.9 | +76.9 | $+9,721 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T09:06:22.556782-04:00","date":"2026-09-28","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":11.5,"phases_s":{"reconcile":4.63},"signals":0,"placed":0,"equity":996963.17,"open_positions":18,"pending_orders":0,"open_lots":77,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11164","github_run_id":"36426083938","status":"ok","data_quality":{"clean":{"n":1508,"win":50.2,"med":8.63,"avg":43.62,"pnl":19714.16},"tainted":{"n":1908,"win":33.39,"med":-38.81,"avg":12.66,"pnl":-9602.28},"keep_only":{"n":798,"win":63.28,"med":52.75,"avg":66.75,"pnl":13806.45},"keep_only_recent":{"n":603,"win":62.52,"med":56.92,"avg":76.9,"pnl":9721.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:06:17  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.16|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $224.16|
|  Cash                                                           $156.73|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $67.43|
|  Open P&L                                                        $+0.29|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CVS      MomReversal     $33.67     $89.14   $89.40   +0.3%   $+0.10  |
|  EVR      MomReversal     $33.76     $262.43  $263.91  +0.6%   $+0.19  |
|                                                                        |
|  Total invested                                                  $67.43|
|  Total open P&L                                                  $+0.29|
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
|  2026-09-25  SELL  AYI  MomReversal  $33.58  P&L $+0.01                |
|  2026-09-25  SELL  COP  Pullback50  $33.54  P&L $-0.17                 |
|  2026-09-25  SELL  GOOG  Pullback50  $33.59  P&L $-0.01                |
|  2026-09-25  SELL  GOOGL  Pullback50  $33.59  P&L $-0.01               |
|  2026-09-25  SELL  KNF  MomReversal  $33.28  P&L $-0.47                |
|  2026-09-24  SELL  AES  Pullback50  $33.74  P&L $-0.02                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-28T09:06:19.589600-04:00 share=25% ===
2026-09-28 09:06:19,589 INFO === options_live_micro LIVE 2026-09-28T09:06:19.589600-04:00 share=25% ===
Live account equity $224.16 cash $156.73 #225458845 options_level=3
2026-09-28 09:06:19,778 INFO Live account equity $224.16 cash $156.73 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-28 09:06:19,853 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-28 09:06:19,909 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (174 earlier lines - see full log file)

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 293 | 21 |
| S164 | 333 | 24 |
| S165 | 1759 | 36 |
| S166 | 139 | 10 |
| S167 | 316 | 23 |
| S168 | 236 | 20 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-28
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1589 | WARN | <<<
| Missing exit records (post) |  1589 | WARN | <<<
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |    77 | INFO |
| Total closed lots           |  2539 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1508 med=+8.6% | TAINTED n=1908 med=-38.8% | KEEP-only n=798 med=+52.8% | KILL=19 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260928T131117Z

- UTC timestamp: `20260928T131117Z`
- GitHub run: [#11165](https://github.com/28twagg-ops/TradingBot/actions/runs/36426670662)
- Run id: `36426670662`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`23s`
- Full logs: `logs/action_runs/20260928T131117Z_live_bot.log`, `logs/action_runs/20260928T131117Z_live_options.log`, `logs/action_runs/20260928T131117Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1508 | 50.2 | +8.6 | +43.6 | $+19,714 |
| TAINTED | 1908 | 33.4 | -38.8 | +12.7 | $-9,602 |
| KEEP-only | 798 | 63.3 | +52.8 | +66.8 | $+13,806 |
| KEEP-only recent | 603 | 62.5 | +56.9 | +76.9 | $+9,721 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T09:11:22.767778-04:00","date":"2026-09-28","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":10.9,"phases_s":{"reconcile":4.15},"signals":0,"placed":0,"equity":996963.17,"open_positions":18,"pending_orders":0,"open_lots":77,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11165","github_run_id":"36426670662","status":"ok","data_quality":{"clean":{"n":1508,"win":50.2,"med":8.63,"avg":43.62,"pnl":19714.16},"tainted":{"n":1908,"win":33.39,"med":-38.81,"avg":12.66,"pnl":-9602.28},"keep_only":{"n":798,"win":63.28,"med":52.75,"avg":66.75,"pnl":13806.45},"keep_only_recent":{"n":603,"win":62.52,"med":56.92,"avg":76.9,"pnl":9721.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:11:19  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.20|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $224.20|
|  Cash                                                           $156.73|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $67.47|
|  Open P&L                                                        $+0.33|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CVS      MomReversal     $33.71     $89.14   $89.50   +0.4%   $+0.14  |
|  EVR      MomReversal     $33.76     $262.43  $263.91  +0.6%   $+0.19  |
|                                                                        |
|  Total invested                                                  $67.47|
|  Total open P&L                                                  $+0.33|
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
|  2026-09-25  SELL  AYI  MomReversal  $33.58  P&L $+0.01                |
|  2026-09-25  SELL  COP  Pullback50  $33.54  P&L $-0.17                 |
|  2026-09-25  SELL  GOOG  Pullback50  $33.59  P&L $-0.01                |
|  2026-09-25  SELL  GOOGL  Pullback50  $33.59  P&L $-0.01               |
|  2026-09-25  SELL  KNF  MomReversal  $33.28  P&L $-0.47                |
|  2026-09-24  SELL  AES  Pullback50  $33.74  P&L $-0.02                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-28T09:11:20.043324-04:00 share=25% ===
2026-09-28 09:11:20,043 INFO === options_live_micro LIVE 2026-09-28T09:11:20.043324-04:00 share=25% ===
Live account equity $224.20 cash $156.73 #225458845 options_level=3
2026-09-28 09:11:20,087 INFO Live account equity $224.20 cash $156.73 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-28 09:11:20,096 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-28 09:11:20,103 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (174 earlier lines - see full log file)

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 293 | 21 |
| S164 | 333 | 24 |
| S165 | 1759 | 36 |
| S166 | 139 | 10 |
| S167 | 316 | 23 |
| S168 | 236 | 20 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-28
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1589 | WARN | <<<
| Missing exit records (post) |  1589 | WARN | <<<
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |    77 | INFO |
| Total closed lots           |  2539 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1508 med=+8.6% | TAINTED n=1908 med=-38.8% | KEEP-only n=798 med=+52.8% | KILL=19 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.2 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260928T131625Z

- UTC timestamp: `20260928T131625Z`
- GitHub run: [#11166](https://github.com/28twagg-ops/TradingBot/actions/runs/36427265384)
- Run id: `36427265384`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`21s`
- Full logs: `logs/action_runs/20260928T131625Z_live_bot.log`, `logs/action_runs/20260928T131625Z_live_options.log`, `logs/action_runs/20260928T131625Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1508 | 50.2 | +8.6 | +43.6 | $+19,714 |
| TAINTED | 1908 | 33.4 | -38.8 | +12.7 | $-9,602 |
| KEEP-only | 798 | 63.3 | +52.8 | +66.8 | $+13,806 |
| KEEP-only recent | 603 | 62.5 | +56.9 | +76.9 | $+9,721 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T09:16:31.071320-04:00","date":"2026-09-28","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":11.8,"phases_s":{"reconcile":4.86},"signals":0,"placed":0,"equity":996963.17,"open_positions":18,"pending_orders":0,"open_lots":77,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11166","github_run_id":"36427265384","status":"ok","data_quality":{"clean":{"n":1508,"win":50.2,"med":8.63,"avg":43.62,"pnl":19714.16},"tainted":{"n":1908,"win":33.39,"med":-38.81,"avg":12.66,"pnl":-9602.28},"keep_only":{"n":798,"win":63.28,"med":52.75,"avg":66.75,"pnl":13806.45},"keep_only_recent":{"n":603,"win":62.52,"med":56.92,"avg":76.9,"pnl":9721.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
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
|  Equity                                                         $224.20|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $224.20|
|  Cash                                                           $156.73|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $67.47|
|  Open P&L                                                        $+0.33|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CVS      MomReversal     $33.71     $89.14   $89.52   +0.4%   $+0.14  |
|  EVR      MomReversal     $33.76     $262.43  $263.91  +0.6%   $+0.19  |
|                                                                        |
|  Total invested                                                  $67.47|
|  Total open P&L                                                  $+0.33|
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
|  2026-09-25  SELL  AYI  MomReversal  $33.58  P&L $+0.01                |
|  2026-09-25  SELL  COP  Pullback50  $33.54  P&L $-0.17                 |
|  2026-09-25  SELL  GOOG  Pullback50  $33.59  P&L $-0.01                |
|  2026-09-25  SELL  GOOGL  Pullback50  $33.59  P&L $-0.01               |
|  2026-09-25  SELL  KNF  MomReversal  $33.28  P&L $-0.47                |
|  2026-09-24  SELL  AES  Pullback50  $33.74  P&L $-0.02                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-28T09:16:28.245843-04:00 share=25% ===
2026-09-28 09:16:28,245 INFO === options_live_micro LIVE 2026-09-28T09:16:28.245843-04:00 share=25% ===
Live account equity $224.20 cash $156.73 #225458845 options_level=3
2026-09-28 09:16:28,439 INFO Live account equity $224.20 cash $156.73 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-28 09:16:28,502 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-28 09:16:28,559 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (174 earlier lines - see full log file)

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 293 | 21 |
| S164 | 333 | 24 |
| S165 | 1759 | 36 |
| S166 | 139 | 10 |
| S167 | 316 | 23 |
| S168 | 236 | 20 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-28
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1589 | WARN | <<<
| Missing exit records (post) |  1589 | WARN | <<<
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |    77 | INFO |
| Total closed lots           |  2539 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1508 med=+8.6% | TAINTED n=1908 med=-38.8% | KEEP-only n=798 med=+52.8% | KILL=19 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.2 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260928T132122Z

- UTC timestamp: `20260928T132122Z`
- GitHub run: [#11167](https://github.com/28twagg-ops/TradingBot/actions/runs/36427867423)
- Run id: `36427867423`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`25s`
- Full logs: `logs/action_runs/20260928T132122Z_live_bot.log`, `logs/action_runs/20260928T132122Z_live_options.log`, `logs/action_runs/20260928T132122Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1508 | 50.2 | +8.6 | +43.6 | $+19,714 |
| TAINTED | 1908 | 33.4 | -38.8 | +12.7 | $-9,602 |
| KEEP-only | 798 | 63.3 | +52.8 | +66.8 | $+13,806 |
| KEEP-only recent | 603 | 62.5 | +56.9 | +76.9 | $+9,721 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T09:21:29.714547-04:00","date":"2026-09-28","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":11.9,"phases_s":{"reconcile":4.78},"signals":0,"placed":0,"equity":996963.17,"open_positions":18,"pending_orders":0,"open_lots":77,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11167","github_run_id":"36427867423","status":"ok","data_quality":{"clean":{"n":1508,"win":50.2,"med":8.63,"avg":43.62,"pnl":19714.16},"tainted":{"n":1908,"win":33.39,"med":-38.81,"avg":12.66,"pnl":-9602.28},"keep_only":{"n":798,"win":63.28,"med":52.75,"avg":66.75,"pnl":13806.45},"keep_only_recent":{"n":603,"win":62.52,"med":56.92,"avg":76.9,"pnl":9721.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:21:23  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.01|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $224.01|
|  Cash                                                           $156.73|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $67.28|
|  Open P&L                                                        $+0.14|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CVS      MomReversal     $33.71     $89.14   $89.52   +0.4%   $+0.14  |
|  EVR      MomReversal     $33.57     $262.43  $262.41  -0.0%   $-0.00  |
|                                                                        |
|  Total invested                                                  $67.28|
|  Total open P&L                                                  $+0.14|
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
|  2026-09-25  SELL  AYI  MomReversal  $33.58  P&L $+0.01                |
|  2026-09-25  SELL  COP  Pullback50  $33.54  P&L $-0.17                 |
|  2026-09-25  SELL  GOOG  Pullback50  $33.59  P&L $-0.01                |
|  2026-09-25  SELL  GOOGL  Pullback50  $33.59  P&L $-0.01               |
|  2026-09-25  SELL  KNF  MomReversal  $33.28  P&L $-0.47                |
|  2026-09-24  SELL  AES  Pullback50  $33.74  P&L $-0.02                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-28T09:21:26.094727-04:00 share=25% ===
2026-09-28 09:21:26,094 INFO === options_live_micro LIVE 2026-09-28T09:21:26.094727-04:00 share=25% ===
Live account equity $224.01 cash $156.73 #225458845 options_level=3
2026-09-28 09:21:26,341 INFO Live account equity $224.01 cash $156.73 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-28 09:21:26,415 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-28 09:21:26,488 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (174 earlier lines - see full log file)

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 293 | 21 |
| S164 | 333 | 24 |
| S165 | 1759 | 36 |
| S166 | 139 | 10 |
| S167 | 316 | 23 |
| S168 | 236 | 20 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-28
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1589 | WARN | <<<
| Missing exit records (post) |  1589 | WARN | <<<
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |    77 | INFO |
| Total closed lots           |  2539 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1508 med=+8.6% | TAINTED n=1908 med=-38.8% | KEEP-only n=798 med=+52.8% | KILL=19 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.01 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260928T132628Z

- UTC timestamp: `20260928T132628Z`
- GitHub run: [#11168](https://github.com/28twagg-ops/TradingBot/actions/runs/36428453493)
- Run id: `36428453493`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`24s`
- Full logs: `logs/action_runs/20260928T132628Z_live_bot.log`, `logs/action_runs/20260928T132628Z_live_options.log`, `logs/action_runs/20260928T132628Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1508 | 50.2 | +8.6 | +43.6 | $+19,714 |
| TAINTED | 1908 | 33.4 | -38.8 | +12.7 | $-9,602 |
| KEEP-only | 798 | 63.3 | +52.8 | +66.8 | $+13,806 |
| KEEP-only recent | 603 | 62.5 | +56.9 | +76.9 | $+9,721 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T09:26:34.508343-04:00","date":"2026-09-28","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":11.4,"phases_s":{"reconcile":4.51},"signals":0,"placed":0,"equity":996963.17,"open_positions":18,"pending_orders":0,"open_lots":77,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11168","github_run_id":"36428453493","status":"ok","data_quality":{"clean":{"n":1508,"win":50.2,"med":8.63,"avg":43.62,"pnl":19714.16},"tainted":{"n":1908,"win":33.39,"med":-38.81,"avg":12.66,"pnl":-9602.28},"keep_only":{"n":798,"win":63.28,"med":52.75,"avg":66.75,"pnl":13806.45},"keep_only_recent":{"n":603,"win":62.52,"med":56.92,"avg":76.9,"pnl":9721.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:26:29  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.01|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $224.01|
|  Cash                                                           $156.73|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $67.28|
|  Open P&L                                                        $+0.14|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CVS      MomReversal     $33.71     $89.14   $89.52   +0.4%   $+0.14  |
|  EVR      MomReversal     $33.57     $262.43  $262.41  -0.0%   $-0.00  |
|                                                                        |
|  Total invested                                                  $67.28|
|  Total open P&L                                                  $+0.14|
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
|  2026-09-25  SELL  AYI  MomReversal  $33.58  P&L $+0.01                |
|  2026-09-25  SELL  COP  Pullback50  $33.54  P&L $-0.17                 |
|  2026-09-25  SELL  GOOG  Pullback50  $33.59  P&L $-0.01                |
|  2026-09-25  SELL  GOOGL  Pullback50  $33.59  P&L $-0.01               |
|  2026-09-25  SELL  KNF  MomReversal  $33.28  P&L $-0.47                |
|  2026-09-24  SELL  AES  Pullback50  $33.74  P&L $-0.02                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-28T09:26:31.006751-04:00 share=25% ===
2026-09-28 09:26:31,006 INFO === options_live_micro LIVE 2026-09-28T09:26:31.006751-04:00 share=25% ===
Live account equity $224.01 cash $156.73 #225458845 options_level=3
2026-09-28 09:26:31,172 INFO Live account equity $224.01 cash $156.73 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-28 09:26:31,216 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-28 09:26:31,260 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (174 earlier lines - see full log file)

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 293 | 21 |
| S164 | 333 | 24 |
| S165 | 1759 | 36 |
| S166 | 139 | 10 |
| S167 | 316 | 23 |
| S168 | 236 | 20 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-28
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1589 | WARN | <<<
| Missing exit records (post) |  1589 | WARN | <<<
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |    77 | INFO |
| Total closed lots           |  2539 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1508 med=+8.6% | TAINTED n=1908 med=-38.8% | KEEP-only n=798 med=+52.8% | KILL=19 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.01 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260928T133125Z

- UTC timestamp: `20260928T133125Z`
- GitHub run: [#11169](https://github.com/28twagg-ops/TradingBot/actions/runs/36429045855)
- Run id: `36429045855`
- Live bot: exit=`0`, duration=`215s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260928T133125Z_live_bot.log`, `logs/action_runs/20260928T133125Z_live_options.log`, `logs/action_runs/20260928T133125Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1508 | 50.2 | +8.6 | +43.6 | $+19,714 |
| TAINTED | 1908 | 33.4 | -38.8 | +12.7 | $-9,602 |
| KEEP-only | 798 | 63.3 | +52.8 | +66.8 | $+13,806 |
| KEEP-only recent | 603 | 62.5 | +56.9 | +76.9 | $+9,721 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T09:26:34.508343-04:00","date":"2026-09-28","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":11.4,"phases_s":{"reconcile":4.51},"signals":0,"placed":0,"equity":996963.17,"open_positions":18,"pending_orders":0,"open_lots":77,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11168","github_run_id":"36428453493","status":"ok","data_quality":{"clean":{"n":1508,"win":50.2,"med":8.63,"avg":43.62,"pnl":19714.16},"tainted":{"n":1908,"win":33.39,"med":-38.81,"avg":12.66,"pnl":-9602.28},"keep_only":{"n":798,"win":63.28,"med":52.75,"avg":66.75,"pnl":13806.45},"keep_only_recent":{"n":603,"win":62.52,"med":56.92,"avg":76.9,"pnl":9721.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:31:26  INFO      Mode: morning_prep
13:31:26  INFO        [prep_positions] 2/2 (2 valid)
13:31:26  INFO      Fetching tickers (universe=both)...
13:31:27  INFO        S&P 500: 503
13:31:27  INFO        MidCap 400: 400
13:31:27  INFO        Total: 903 tickers
13:31:28  INFO        [prep_universe] 40/901 (40 valid)
13:31:29  INFO        [prep_universe] 80/901 (80 valid)
13:31:30  INFO        [prep_universe] 120/901 (120 valid)
13:31:32  INFO        [prep_universe] 160/901 (160 valid)
13:31:33  INFO        [prep_universe] 200/901 (199 valid)
13:31:40  INFO        [prep_universe] 240/901 (238 valid)
13:31:53  INFO        [prep_universe] 280/901 (278 valid)
13:32:06  INFO        [prep_universe] 320/901 (318 valid)
13:32:16  INFO        [prep_universe] 360/901 (358 valid)
13:32:29  INFO        [prep_universe] 400/901 (398 valid)
13:32:39  INFO        [prep_universe] 440/901 (438 valid)
13:32:52  INFO        [prep_universe] 480/901 (478 valid)
13:33:05  INFO        [prep_universe] 520/901 (518 valid)
13:33:16  INFO        [prep_universe] 560/901 (558 valid)
13:33:28  INFO        [prep_universe] 600/901 (598 valid)
13:33:41  INFO        [prep_universe] 640/901 (638 valid)
13:33:51  INFO        [prep_universe] 680/901 (678 valid)
13:34:05  INFO        [prep_universe] 720/901 (718 valid)
13:34:18  INFO        [prep_universe] 760/901 (758 valid)
13:34:28  INFO        [prep_universe] 800/901 (798 valid)
13:34:41  INFO        [prep_universe] 840/901 (838 valid)
13:34:54  INFO        [prep_universe] 880/901 (878 valid)
13:34:58  INFO        [prep_universe] 901/901 (899 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.82|
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
|  Open positions                                                       2|
|  Invested                                                        $67.09|
|  Open P&L                                                        $-0.05|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CVS      MomReversal     $33.64     $89.14   $89.33   +0.2%   $+0.07  |
|  EVR      MomReversal     $33.45     $262.43  $261.48  -0.4%   $-0.12  |
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
|  Signal candidates                                                   16|
|  Universe scanned                                                   901|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-28T09:35:01.056841-04:00 share=25% ===
2026-09-28 09:35:01,056 INFO === options_live_micro LIVE 2026-09-28T09:35:01.056841-04:00 share=25% ===
Live account equity $223.15 cash $156.73 #225458845 options_level=3
2026-09-28 09:35:01,416 INFO Live account equity $223.15 cash $156.73 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-28 09:35:01,484 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-28 09:35:01,571 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=77 paper_keys=yes dry_run=False
  alpaca positions=20
  FLAG b165|S216|5d7c0be9 missing from Alpaca
  FLAG b164|S216|5ffa0bf9 missing from Alpaca
  FLAG b235|S401|f217bb6f missing from Alpaca
  FLAG b234|S401|fbe8f114 missing from Alpaca
  FLAG b193|S218|2903f4ed missing from Alpaca
  FLAG b0|ORPHAN|7b0f4512 missing from Alpaca
  FLAG b179|S217|29d1def0 missing from Alpaca
  FLAG b178|S217|e851d44d missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$995,925.10
  buying_power=$3,852,911.19 cash=$975,894.11
  open option orders: 8
    XOM261002C00170000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
    DKNG261002C00021500 OrderSide.SELL qty=22 status=OrderStatus.NEW limit=None
    DKNG261009C00022500 OrderSide.SELL qty=2 status=OrderStatus.NEW limit=None
    NKE261002C00039500 OrderSide.SELL qty=2 status=OrderStatus.NEW limit=None
    NKE261002C00038500 OrderSide.SELL qty=6 status=OrderStatus.NEW limit=None
  open option positions: 16
    DKNG261002C00021000 qty=4 mkt=$320.00
    DKNG261002C00021500 qty=22 mkt=$1,386.00
    DKNG261002C00022000 qty=4 mkt=$176.00
    DKNG261002C00022500 qty=2 mkt=$42.00
    DKNG261009C00022500 qty=2 mkt=$84.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-28T09:35:04.631133-04:00 ===

[Run context]
Paper auth OK — equity $995930.11, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
2026-09-28 09:35:07,016 INFO   EXIT [b318|lab0318_s355_w4_1120_1135_r1|S355] stop_loss (-57.1%) SELL 1 MARA261002C00013500 @<= 0.19
  EXIT [b86|lab0086_s210_w4_1120_1135_r1|S210] stop_loss (-89.3%) SELL failed SPY260928C00775000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
Protective stops: placed=5 upgraded=0 already=9 failed=1 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
```

---

## Run 20260928T133653Z

- UTC timestamp: `20260928T133653Z`
- GitHub run: [#11170](https://github.com/28twagg-ops/TradingBot/actions/runs/36429632432)
- Run id: `36429632432`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260928T133653Z_live_bot.log`, `logs/action_runs/20260928T133653Z_live_options.log`, `logs/action_runs/20260928T133653Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1508 | 50.2 | +8.6 | +43.6 | $+19,714 |
| TAINTED | 1908 | 33.4 | -38.8 | +12.7 | $-9,602 |
| KEEP-only | 798 | 63.3 | +52.8 | +66.8 | $+13,806 |
| KEEP-only recent | 603 | 62.5 | +56.9 | +76.9 | $+9,721 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T09:26:34.508343-04:00","date":"2026-09-28","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":11.4,"phases_s":{"reconcile":4.51},"signals":0,"placed":0,"equity":996963.17,"open_positions":18,"pending_orders":0,"open_lots":77,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11168","github_run_id":"36428453493","status":"ok","data_quality":{"clean":{"n":1508,"win":50.2,"med":8.63,"avg":43.62,"pnl":19714.16},"tainted":{"n":1908,"win":33.39,"med":-38.81,"avg":12.66,"pnl":-9602.28},"keep_only":{"n":798,"win":63.28,"med":52.75,"avg":66.75,"pnl":13806.45},"keep_only_recent":{"n":603,"win":62.52,"med":56.92,"avg":76.9,"pnl":9721.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:36:54  INFO      Mode: morning_prep
13:36:55  INFO        [prep_positions] 2/2 (2 valid)
13:36:55  INFO      Fetching tickers (universe=both)...
13:36:55  INFO        S&P 500: 503
13:36:55  INFO        MidCap 400: 400
13:36:55  INFO        Total: 903 tickers
13:36:56  INFO        [prep_universe] 40/901 (40 valid)
13:36:57  INFO        [prep_universe] 80/901 (80 valid)
13:36:59  INFO        [prep_universe] 120/901 (120 valid)
13:37:00  INFO        [prep_universe] 160/901 (160 valid)
13:37:01  INFO        [prep_universe] 200/901 (199 valid)
13:37:08  INFO        [prep_universe] 240/901 (238 valid)
13:37:21  INFO        [prep_universe] 280/901 (278 valid)
13:37:34  INFO        [prep_universe] 320/901 (318 valid)
13:37:44  INFO        [prep_universe] 360/901 (358 valid)
13:37:57  INFO        [prep_universe] 400/901 (398 valid)
13:38:10  INFO        [prep_universe] 440/901 (438 valid)
13:38:20  INFO        [prep_universe] 480/901 (478 valid)
13:38:33  INFO        [prep_universe] 520/901 (518 valid)
13:38:46  INFO        [prep_universe] 560/901 (558 valid)
13:38:58  INFO        [prep_universe] 600/901 (598 valid)
13:39:08  INFO        [prep_universe] 640/901 (638 valid)
13:39:21  INFO        [prep_universe] 680/901 (678 valid)
13:39:34  INFO        [prep_universe] 720/901 (718 valid)
13:39:44  INFO        [prep_universe] 760/901 (758 valid)
13:39:57  INFO        [prep_universe] 800/901 (798 valid)
13:40:10  INFO        [prep_universe] 840/901 (838 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---
