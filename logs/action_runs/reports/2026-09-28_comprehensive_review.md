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

## Run 20260928T134151Z

- UTC timestamp: `20260928T134151Z`
- GitHub run: [#11171](https://github.com/28twagg-ops/TradingBot/actions/runs/36430227046)
- Run id: `36430227046`
- Live bot: exit=`0`, duration=`217s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260928T134151Z_live_bot.log`, `logs/action_runs/20260928T134151Z_live_options.log`, `logs/action_runs/20260928T134151Z_options_bot.log`


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
13:41:52  INFO      Mode: morning_prep
13:41:53  INFO        [prep_positions] 2/2 (2 valid)
13:41:53  INFO        Universe cache hit: 903 tickers (tickers_2026-09-28.json)
13:41:54  INFO        [prep_universe] 40/901 (40 valid)
13:41:55  INFO        [prep_universe] 80/901 (80 valid)
13:41:56  INFO        [prep_universe] 120/901 (120 valid)
13:41:58  INFO        [prep_universe] 160/901 (160 valid)
13:41:59  INFO        [prep_universe] 200/901 (199 valid)
13:42:06  INFO        [prep_universe] 240/901 (238 valid)
13:42:19  INFO        [prep_universe] 280/901 (278 valid)
13:42:32  INFO        [prep_universe] 320/901 (318 valid)
13:42:42  INFO        [prep_universe] 360/901 (358 valid)
13:42:55  INFO        [prep_universe] 400/901 (398 valid)
13:43:06  INFO        [prep_universe] 440/901 (438 valid)
13:43:19  INFO        [prep_universe] 480/901 (478 valid)
13:43:32  INFO        [prep_universe] 520/901 (518 valid)
13:43:42  INFO        [prep_universe] 560/901 (558 valid)
13:43:55  INFO        [prep_universe] 600/901 (598 valid)
13:44:08  INFO        [prep_universe] 640/901 (638 valid)
13:44:19  INFO        [prep_universe] 680/901 (678 valid)
13:44:32  INFO        [prep_universe] 720/901 (718 valid)
13:44:42  INFO        [prep_universe] 760/901 (758 valid)
13:44:55  INFO        [prep_universe] 800/901 (798 valid)
13:45:08  INFO        [prep_universe] 840/901 (838 valid)
13:45:18  INFO        [prep_universe] 880/901 (878 valid)
13:45:26  INFO        [prep_universe] 901/901 (899 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.20|
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
|  Invested                                                        $66.47|
|  Open P&L                                                        $-0.67|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  CVS      MomReversal     $33.53     $89.14   $89.03   -0.1%   $-0.04  |
|  EVR      MomReversal     $32.95     $262.43  $257.55  -1.9%   $-0.62  |
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
|  Signal candidates                                                   34|
|  Universe scanned                                                   901|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-28T09:45:28.835562-04:00 share=25% ===
2026-09-28 09:45:28,835 INFO === options_live_micro LIVE 2026-09-28T09:45:28.835562-04:00 share=25% ===
Live account equity $223.74 cash $156.73 #225458845 options_level=3
2026-09-28 09:45:28,953 INFO Live account equity $223.74 cash $156.73 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-28 09:45:29,051 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-28 09:45:29,117 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text

```

---

## Run 20260928T134715Z

- UTC timestamp: `20260928T134715Z`
- GitHub run: [#11172](https://github.com/28twagg-ops/TradingBot/actions/runs/36430830658)
- Run id: `36430830658`
- Live bot: exit=`0`, duration=`56s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260928T134715Z_live_bot.log`, `logs/action_runs/20260928T134715Z_live_options.log`, `logs/action_runs/20260928T134715Z_options_bot.log`


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
... (123 earlier lines - see full log file)
|  RNR      Pullback50      eq     $326.53  56.3   -2.10   50MA bounce (+|
|  TTC      Pullback50      eq     $96.85   60.7   -1.87   50MA bounce (+|
|  UNM      Pullback50      eq     $91.61   41.2   -1.51   50MA bounce (+|13:47:41  INFO        BUY  AES  $33.58  [Pullback50]  id=2603368f-ad1f-4610-a3e2-6e6843c3d02a
13:47:41  INFO        BUY  AKAM  $33.58  [Pullback50]  id=3b859902-6edc-4aca-a5cf-c6b73f20fb7a
13:47:41  INFO        BUY  GOOGL  $33.58  [Pullback50]  id=3660ac1c-4c58-4ccd-96db-2b046e41b98e
13:48:11  INFO        place_all_stops: checking 3 positions...
13:48:11  INFO        STOP-MARKET placed AES  qty=2 (pos=2.2563)  stop=$14.80  id=43881840-a6e3-4c98-9dff-9b85aaf9f451
13:48:11  INFO        STOP skipped AKAM: fractional (0.2986 shares) — software exit will handle it
13:48:11  INFO        STOP skipped GOOGL: fractional (0.0979 shares) — software exit will handle it
13:48:11  INFO        Daily log -> logs/daily/2026-09-28.md
13:48:11  INFO        Dashboard written → logs/dashboard.md

|  WTS      Pullback50      eq     $357.67  45.7   -1.74   50MA bounce (-|
|                                                                        |
+========================================================================+

+========================================================================+
|                              ENTRY ORDERS                              |
+========================================================================+
|    ENTER [eq] AES  Pullback50                                    $33.58|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    ENTER [eq] AKAM  Pullback50                                   $33.58|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    ENTER [eq] GOOGL  Pullback50                                  $33.58|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    SKIP [eq] MO  Pullback50                                       cap 3|
|    SKIP [eq] GOOG  Pullback50                                     cap 3|
|    SKIP [eq] TECH  Pullback50                                     cap 3|
|    SKIP [eq] ECL  Pullback50                                      cap 3|
|    SKIP [eq] FCX  Pullback50                                      cap 3|
|    SKIP [eq] IEX  Pullback50                                      cap 3|
|    SKIP [eq] INCY  Pullback50                                     cap 3|
|    SKIP [eq] LLY  Pullback50                                      cap 3|
|    SKIP [eq] MSI  Pullback50                                      cap 3|
|    SKIP [eq] PM  Pullback50                                       cap 3|
|    SKIP [eq] DGX  Pullback50                                      cap 3|
|    SKIP [eq] ROST  Pullback50                                     cap 3|
|    SKIP [eq] TT  Pullback50                                       cap 3|
|    SKIP [eq] V  Pullback50                                        cap 3|
|    SKIP [eq] ITT  Pullback50                                      cap 3|
|    SKIP [eq] MOG-A  Pullback50                                    cap 3|
|    SKIP [eq] MSM  Pullback50                                      cap 3|
|    SKIP [eq] QLYS  Pullback50                                     cap 3|
|    SKIP [eq] RNR  Pullback50                                      cap 3|
|    SKIP [eq] TTC  Pullback50                                      cap 3|
|    SKIP [eq] UNM  Pullback50                                      cap 3|
|    SKIP [eq] WTS  Pullback50                                      cap 3|

+========================================================================+
|                         BUY FILL CONFIRMATION                          |
+========================================================================+
|  Pending submits                                                      3|
+------------------------------------------------------------------------+
|  AES                                                  still unconfirmed|
|  AKAM                                                 still unconfirmed|
|  GOOGL                                                still unconfirmed|
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
|  Scanned                                                              0|
|  Signals                                                             25|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  3 unconfirmed|
|  Exits                                                                2|
|  Open pos                                                             3|
|  Equity                                                         $223.61|
|  Cash                                                           $122.96|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-28T09:48:12.352751-04:00 share=25% ===
2026-09-28 09:48:12,352 INFO === options_live_micro LIVE 2026-09-28T09:48:12.352751-04:00 share=25% ===
Live account equity $223.62 cash $122.96 #225458845 options_level=3
2026-09-28 09:48:12,488 INFO Live account equity $223.62 cash $122.96 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-28 09:48:12,605 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-28 09:48:12,677 INFO Live micro done. open_options=0 lots=0
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
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$996,010.59
  buying_power=$3,854,287.16 cash=$975,914.09
  open option orders: 13
    DKNG261002C00022500 OrderSide.SELL qty=2 status=OrderStatus.NEW limit=None
    DKNG261002C00022000 OrderSide.SELL qty=4 status=OrderStatus.NEW limit=None
    DKNG261002C00021000 OrderSide.SELL qty=4 status=OrderStatus.NEW limit=None
    MARA261016C00014500 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
    SMCI261002C00044500 OrderSide.SELL qty=2 status=OrderStatus.NEW limit=None
  open option positions: 16
    DKNG261002C00021000 qty=4 mkt=$300.00
    DKNG261002C00021500 qty=22 mkt=$1,056.00
    DKNG261002C00022000 qty=4 mkt=$124.00
    DKNG261002C00022500 qty=2 mkt=$36.00
    DKNG261009C00022500 qty=2 mkt=$80.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-28T09:48:15.156437-04:00 ===

[Run context]
Paper auth OK — equity $996009.08, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
  EXIT [b86|lab0086_s210_w4_1120_1135_r1|S210] stop_loss (-91.1%) SELL failed SPY260928C00775000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
Protective stops: placed=1 upgraded=0 already=13 failed=1 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
Found 464 signal(s); top: ['S401:PLTR', 'S359:PLTR', 'S361:PLTR', 'S362:PLTR', 'S363:PLTR', 'S364:PLTR', 'S365:PLTR', 'S366:PLTR']
Paper lab: $996009 broker equity -> 1164 bucket(s) ($500 virtual each, unlimited paper)
```

---

## Run 20260928T135205Z

- UTC timestamp: `20260928T135205Z`
- GitHub run: [#11173](https://github.com/28twagg-ops/TradingBot/actions/runs/36431443478)
- Run id: `36431443478`
- Live bot: exit=`0`, duration=`93s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260928T135205Z_live_bot.log`, `logs/action_runs/20260928T135205Z_live_options.log`, `logs/action_runs/20260928T135205Z_options_bot.log`


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
... (80 earlier lines - see full log file)
|                           EXIT EVAL SUMMARY                            |
+========================================================================+
|  Exit eval    attempted 3 | filled 3 | partial 0 | pending 0 | failed 0|
|  Other skips     already logged today 0  |  no price data 0  |  holds 0|
|  Stop-loss breaches                                                none|
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
|  Source                          cached signals (signals fresh (11.6m))|
|  Universe scanned in prep                                           901|
+========================================================================+

+========================================================================+
|                         SIGNALS FOUND  --  25                          |
+========================================================================+
|  TICKER   STRATEGY        TIER   PRICE    RSI    VOL_Z   TRIGGER       |
+------------------------------------------------------------------------+
|  AES      Pullback50      eq     $14.87   60.0   -2.34   50MA bounce (+|
|  AKAM     Pullback50      eq     $113.39  59.1   -0.64   50MA bounce (+|
|  GOOGL    Pullback50      eq     $342.47  52.9   -2.63   50MA bounce (-|
|  MO       Pullback50      eq     $69.16   57.6   -2.62   50MA bounce (+|
|  GOOG     Pullback50      eq     $338.92  52.7   -2.46   50MA bounce (-|
|  TECH     Pullback50      eq     $72.58   64.6   -2.44   50MA bounce (+|
|  ECL      Pullback50      eq     $278.29  50.3   -2.45   50MA bounce (+|
|  FCX      Pullback50      eq     $70.08   31.1   -2.39   50MA bounce (+|
|  IEX      Pullback50      eq     $230.22  59.3   -2.56   50MA bounce (+|
|  INCY     Pullback50      eq     $123.88  48.8   -2.09   50MA bounce (+|
|  LLY      Pullback50      eq     $1188.~  75.9   -2.64   50MA bounce (+|
|  MSI      Pullback50      eq     $456.45  43.7   -2.57   50MA bounce (-|
|  PM       Pullback50      eq     $191.33  64.1   -2.20   50MA bounce (+|
|  DGX      Pullback50      eq     $235.81  50.4   -2.00   50MA bounce (-|
|  ROST     Pullback50      eq     $237.11  61.6   -2.52   50MA bounce (-|
|  TT       Pullback50      eq     $452.12  54.6   -2.52   50MA bounce (-|
|  V        Pullback50      eq     $368.14  49.3   -1.50   50MA bounce (-|
|  ITT      Pullback50      eq     $205.80  54.2   -1.90   50MA bounce (+|
|  MOG-A    Pullback50      eq     $387.81  66.3   -1.51   50MA bounce (-|
|  MSM      Pullback50      eq     $121.86  55.2   -2.02   50MA bounce (+|
|  QLYS     Pullback50      eq     $171.02  50.4   -2.08   50MA bounce (+|
|  RNR      Pullback50      eq     $326.53  56.3   -2.10   50MA bounce (+|
|  TTC      Pullback50      eq     $96.85   60.7   -1.87   50MA bounce (+|13:53:38  INFO        Daily log -> logs/daily/2026-09-28.md
13:53:38  INFO        Dashboard written → logs/dashboard.md

|  UNM      Pullback50      eq     $91.61   41.2   -1.51   50MA bounce (+|
|  WTS      Pullback50      eq     $357.67  45.7   -1.74   50MA bounce (-|
|                                                                        |
+========================================================================+

+========================================================================+
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
|  Signals                                                             25|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  0 unconfirmed|
|  Exits                                                                3|
|  Open pos                                                             0|
|  Equity                                                         $223.66|
|  Cash                                                           $223.66|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-28T09:53:39.021959-04:00 share=25% ===
2026-09-28 09:53:39,022 INFO === options_live_micro LIVE 2026-09-28T09:53:39.021959-04:00 share=25% ===
Live account equity $223.66 cash $223.66 #225458845 options_level=3
2026-09-28 09:53:39,096 INFO Live account equity $223.66 cash $223.66 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-28 09:53:39,139 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-28 09:53:39,169 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=69 paper_keys=yes dry_run=False
  alpaca positions=24
  FLAG b318|S355|c3aa6da9 missing from Alpaca
  FLAG b311|S354|6ee30227 missing from Alpaca
  FLAG b310|S354|45a22a8b missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$996,012.91
  buying_power=$3,849,929.26 cash=$975,012.53
  open option orders: 20
    MSFT260928C00510000 OrderSide.SELL qty=4 status=OrderStatus.NEW limit=None
    MCD261002C00242500 OrderSide.SELL qty=2 status=OrderStatus.NEW limit=None
    CVNA261002C00070000 OrderSide.BUY qty=1 status=OrderStatus.NEW limit=0.14
    CVNA261002C00070000 OrderSide.BUY qty=1 status=OrderStatus.NEW limit=0.14
    CVNA261002C00070000 OrderSide.BUY qty=1 status=OrderStatus.NEW limit=0.14
  open option positions: 20
    DKNG261002C00021000 qty=4 mkt=$272.00
    DKNG261002C00021500 qty=22 mkt=$1,034.00
    DKNG261002C00022000 qty=4 mkt=$116.00
    DKNG261002C00022500 qty=2 mkt=$32.00
    DKNG261009C00022500 qty=2 mkt=$80.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-28T09:53:41.889632-04:00 ===

[Run context]
Paper auth OK — equity $996013.03, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
2026-09-28 09:53:45,151 INFO   EXIT [b345|lab0345_s359_w1_0928_1005_r2|S359] take_profit (+80.6%) SELL 1 MSFT260928C00510000 @<= 1.07
  EXIT [b86|lab0086_s210_w4_1120_1135_r1|S210] stop_loss (-91.1%) SELL failed SPY260928C00775000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
Protective stops: placed=3 upgraded=0 already=14 failed=2 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
Found 464 signal(s); top: ['S401:PLTR', 'S359:PLTR', 'S361:PLTR', 'S362:PLTR', 'S363:PLTR', 'S364:PLTR', 'S365:PLTR', 'S366:PLTR']
Paper lab: $996013 broker equity -> 1164 bucket(s) ($500 virtual each, unlimited paper)
```

---

## Run 20260928T135659Z

- UTC timestamp: `20260928T135659Z`
- GitHub run: [#11174](https://github.com/28twagg-ops/TradingBot/actions/runs/36432053690)
- Run id: `36432053690`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`145s`
- Full logs: `logs/action_runs/20260928T135659Z_live_bot.log`, `logs/action_runs/20260928T135659Z_live_options.log`, `logs/action_runs/20260928T135659Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1509 | 50.2 | +12.5 | +43.6 | $+19,752 |
| TAINTED | 1910 | 33.4 | -38.8 | +12.7 | $-9,579 |
| KEEP-only | 799 | 63.3 | +52.8 | +66.7 | $+13,844 |
| KEEP-only recent | 604 | 62.6 | +56.9 | +76.9 | $+9,759 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T09:57:06.750600-04:00","date":"2026-09-28","mode":"entry+manage","header":"entry+manage (3 new)","elapsed_s":132.3,"phases_s":{"reconcile":0.56,"cancel":0.15,"manage":7.71,"protective_stops":2.06,"scan":53.71,"entries":58.82,"reconcile2":0.51},"signals":464,"placed":3,"equity":995996.14,"open_positions":21,"pending_orders":11,"open_lots":81,"submitted_today":28,"filled_today":17,"unattributed_contracts":7,"top_signals":["S401:PLTR","S359:PLTR","S361:PLTR","S362:PLTR","S363:PLTR","S364:PLTR","S365:PLTR","S366:PLTR"],"github_run":"11174","github_run_id":"36432053690","status":"ok","data_quality":{"clean":{"n":1509,"win":50.23,"med":12.5,"avg":43.63,"pnl":19752.16},"tainted":{"n":1910,"win":33.4,"med":-38.81,"avg":12.65,"pnl":-9579.28},"keep_only":{"n":799,"win":63.33,"med":52.78,"avg":66.74,"pnl":13844.45},"keep_only_recent":{"n":604,"win":62.58,"med":56.92,"avg":76.87,"pnl":9759.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:57:00  INFO      Mode: morning_scan
13:57:01  INFO      Morning scan already completed today (2026-09-28T13:48:11.713808Z) — exits-only pass
13:57:01  INFO        Daily log -> logs/daily/2026-09-28.md
13:57:01  INFO        Daily log reconciled -> logs/daily/2026-09-28.md (2 ledger rows)
13:57:02  INFO        Daily log -> logs/daily/2026-09-28.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_SCAN|
|  Time                                                         13:57 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.66|
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
=== options_live_micro LIVE 2026-09-28T09:57:03.110003-04:00 share=25% ===
2026-09-28 09:57:03,110 INFO === options_live_micro LIVE 2026-09-28T09:57:03.110003-04:00 share=25% ===
Live account equity $223.66 cash $223.66 #225458845 options_level=3
2026-09-28 09:57:03,330 INFO Live account equity $223.66 cash $223.66 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-28 09:57:03,531 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-28 09:57:03,665 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (197 earlier lines - see full log file)

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
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    81 | INFO |
| Total closed lots           |  2542 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1509 med=+12.5% | TAINTED n=1910 med=-38.8% | KEEP-only n=799 med=+52.8% | KILL=19 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.66 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260928T140404Z

- UTC timestamp: `20260928T140404Z`
- GitHub run: [#11175](https://github.com/28twagg-ops/TradingBot/actions/runs/36432667125)
- Run id: `36432667125`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260928T140404Z_live_bot.log`, `logs/action_runs/20260928T140404Z_live_options.log`, `logs/action_runs/20260928T140404Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1509 | 50.2 | +12.5 | +43.6 | $+19,752 |
| TAINTED | 1910 | 33.4 | -38.8 | +12.7 | $-9,579 |
| KEEP-only | 799 | 63.3 | +52.8 | +66.7 | $+13,844 |
| KEEP-only recent | 604 | 62.6 | +56.9 | +76.9 | $+9,759 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T09:57:06.750600-04:00","date":"2026-09-28","mode":"entry+manage","header":"entry+manage (3 new)","elapsed_s":132.3,"phases_s":{"reconcile":0.56,"cancel":0.15,"manage":7.71,"protective_stops":2.06,"scan":53.71,"entries":58.82,"reconcile2":0.51},"signals":464,"placed":3,"equity":995996.14,"open_positions":21,"pending_orders":11,"open_lots":81,"submitted_today":28,"filled_today":17,"unattributed_contracts":7,"top_signals":["S401:PLTR","S359:PLTR","S361:PLTR","S362:PLTR","S363:PLTR","S364:PLTR","S365:PLTR","S366:PLTR"],"github_run":"11174","github_run_id":"36432053690","status":"ok","data_quality":{"clean":{"n":1509,"win":50.23,"med":12.5,"avg":43.63,"pnl":19752.16},"tainted":{"n":1910,"win":33.4,"med":-38.81,"avg":12.65,"pnl":-9579.28},"keep_only":{"n":799,"win":63.33,"med":52.78,"avg":66.74,"pnl":13844.45},"keep_only_recent":{"n":604,"win":62.58,"med":56.92,"avg":76.87,"pnl":9759.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:04:05  INFO      Mode: exits
14:04:06  INFO        Daily log -> logs/daily/2026-09-28.md
14:04:06  INFO        Daily log reconciled -> logs/daily/2026-09-28.md (5 ledger rows)
14:04:06  INFO        Daily log -> logs/daily/2026-09-28.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:04 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.66|
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
=== options_live_micro LIVE 2026-09-28T10:04:06.965057-04:00 share=25% ===
2026-09-28 10:04:06,965 INFO === options_live_micro LIVE 2026-09-28T10:04:06.965057-04:00 share=25% ===
Live account equity $223.66 cash $223.66 #225458845 options_level=3
2026-09-28 10:04:07,006 INFO Live account equity $223.66 cash $223.66 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-28 10:04:07,025 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-28 10:04:07,038 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=81 paper_keys=yes dry_run=False
  alpaca positions=25
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$996,427.85
  buying_power=$3,850,475.96 cash=$975,113.25
  open option orders: 20
    MSFT260928C00510000 OrderSide.SELL qty=2 status=OrderStatus.NEW limit=None
    LLY261002C01300000 OrderSide.BUY qty=1 status=OrderStatus.NEW limit=0.37
    WFC261002C00083000 OrderSide.BUY qty=1 status=OrderStatus.NEW limit=0.68
    WFC261002C00083000 OrderSide.BUY qty=1 status=OrderStatus.NEW limit=0.68
    PLTR261002C00205000 OrderSide.SELL qty=6 status=OrderStatus.NEW limit=None
  open option positions: 21
    CVNA261002C00070000 qty=8 mkt=$64.00
    DKNG261002C00021000 qty=4 mkt=$332.00
    DKNG261002C00021500 qty=22 mkt=$1,232.00
    DKNG261002C00022000 qty=4 mkt=$136.00
    DKNG261002C00022500 qty=2 mkt=$34.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-28T10:04:09.694612-04:00 ===

[Run context]
Paper auth OK — equity $996415.73, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
  EXIT [b86|lab0086_s210_w4_1120_1135_r1|S210] stop_loss (-91.1%) SELL failed SPY260928C00775000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
2026-09-28 10:04:14,428 INFO   EXIT [b277|lab0277_s350_w1_0928_1005_r2|S350] take_profit (+143.5%) SELL 1 MSFT260928C00510000 @<= 1.45
Protective stops: placed=1 upgraded=0 already=18 failed=1 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
Found 464 signal(s); top: ['S401:PLTR', 'S359:PLTR', 'S361:PLTR', 'S362:PLTR', 'S363:PLTR', 'S364:PLTR', 'S365:PLTR', 'S366:PLTR']
Paper lab: $996416 broker equity -> 1164 bucket(s) ($500 virtual each, unlimited paper)
```

---

## Run 20260928T140729Z

- UTC timestamp: `20260928T140729Z`
- GitHub run: [#11176](https://github.com/28twagg-ops/TradingBot/actions/runs/36433288356)
- Run id: `36433288356`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260928T140729Z_live_bot.log`, `logs/action_runs/20260928T140729Z_live_options.log`, `logs/action_runs/20260928T140729Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1509 | 50.2 | +12.5 | +43.6 | $+19,752 |
| TAINTED | 1910 | 33.4 | -38.8 | +12.7 | $-9,579 |
| KEEP-only | 799 | 63.3 | +52.8 | +66.7 | $+13,844 |
| KEEP-only recent | 604 | 62.6 | +56.9 | +76.9 | $+9,759 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T09:57:06.750600-04:00","date":"2026-09-28","mode":"entry+manage","header":"entry+manage (3 new)","elapsed_s":132.3,"phases_s":{"reconcile":0.56,"cancel":0.15,"manage":7.71,"protective_stops":2.06,"scan":53.71,"entries":58.82,"reconcile2":0.51},"signals":464,"placed":3,"equity":995996.14,"open_positions":21,"pending_orders":11,"open_lots":81,"submitted_today":28,"filled_today":17,"unattributed_contracts":7,"top_signals":["S401:PLTR","S359:PLTR","S361:PLTR","S362:PLTR","S363:PLTR","S364:PLTR","S365:PLTR","S366:PLTR"],"github_run":"11174","github_run_id":"36432053690","status":"ok","data_quality":{"clean":{"n":1509,"win":50.23,"med":12.5,"avg":43.63,"pnl":19752.16},"tainted":{"n":1910,"win":33.4,"med":-38.81,"avg":12.65,"pnl":-9579.28},"keep_only":{"n":799,"win":63.33,"med":52.78,"avg":66.74,"pnl":13844.45},"keep_only_recent":{"n":604,"win":62.58,"med":56.92,"avg":76.87,"pnl":9759.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:07:31  INFO      Mode: exits
14:07:31  INFO        Daily log -> logs/daily/2026-09-28.md
14:07:31  INFO        Daily log reconciled -> logs/daily/2026-09-28.md (5 ledger rows)
14:07:32  INFO        Daily log -> logs/daily/2026-09-28.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:07 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.66|
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
=== options_live_micro LIVE 2026-09-28T10:07:32.948969-04:00 share=25% ===
2026-09-28 10:07:32,949 INFO === options_live_micro LIVE 2026-09-28T10:07:32.948969-04:00 share=25% ===
Live account equity $223.66 cash $223.66 #225458845 options_level=3
2026-09-28 10:07:33,415 INFO Live account equity $223.66 cash $223.66 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-28 10:07:33,609 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-28 10:07:33,687 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=81 paper_keys=yes dry_run=False
  alpaca positions=25
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$996,543.65
  buying_power=$3,851,562.88 cash=$975,258.23
  open option orders: 20
    CVNA261002C00070000 OrderSide.SELL qty=8 status=OrderStatus.NEW limit=None
    LLY261002C01300000 OrderSide.BUY qty=1 status=OrderStatus.NEW limit=0.37
    WFC261002C00083000 OrderSide.BUY qty=1 status=OrderStatus.NEW limit=0.68
    WFC261002C00083000 OrderSide.BUY qty=1 status=OrderStatus.NEW limit=0.68
    PLTR261002C00205000 OrderSide.SELL qty=6 status=OrderStatus.NEW limit=None
  open option positions: 21
    CVNA261002C00070000 qty=8 mkt=$64.00
    DKNG261002C00021000 qty=4 mkt=$344.00
    DKNG261002C00021500 qty=22 mkt=$1,276.00
    DKNG261002C00022000 qty=4 mkt=$144.00
    DKNG261002C00022500 qty=2 mkt=$48.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-28T10:07:36.762786-04:00 ===

[Run context]
Paper auth OK — equity $996543.90, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
  EXIT [b86|lab0086_s210_w4_1120_1135_r1|S210] stop_loss (-92.9%) SELL failed SPY260928C00775000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
2026-09-28 10:07:42,812 INFO   EXIT [b276|lab0276_s350_w1_0928_1005_r1|S350] take_profit (+67.7%) SELL 1 MSFT260928C00510000 @<= 1.01
Protective stops: placed=0 upgraded=0 already=18 failed=2 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
Found 464 signal(s); top: ['S401:PLTR', 'S359:PLTR', 'S361:PLTR', 'S362:PLTR', 'S363:PLTR', 'S364:PLTR', 'S365:PLTR', 'S366:PLTR']
Paper lab: $996544 broker equity -> 1164 bucket(s) ($500 virtual each, unlimited paper)
  [b236 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9ca0fcc7-0910-4a48-987f-09d8d8710492","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b237 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9ca0fcc7-0910-4a48-987f-09d8d8710492","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b364 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9ca0fcc7-0910-4a48-987f-09d8d8710492","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b365 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9ca0fcc7-0910-4a48-987f-09d8d8710492","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b378 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9ca0fcc7-0910-4a48-987f-09d8d8710492","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b379 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9ca0fcc7-0910-4a48-987f-09d8d8710492","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b392 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9ca0fcc7-0910-4a48-987f-09d8d8710492","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b393 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9ca0fcc7-0910-4a48-987f-09d8d8710492","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b900 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9f9ef7a9-9ef8-473e-833b-3c1ae50757ff","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b901 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9f9ef7a9-9ef8-473e-833b-3c1ae50757ff","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b914 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9ca0fcc7-0910-4a48-987f-09d8d8710492","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b915 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9ca0fcc7-0910-4a48-987f-09d8d8710492","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b392 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"c5b59451-ff0d-41bf-ba6a-d942f2adb0d2","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b393 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"c5b59451-ff0d-41bf-ba6a-d942f2adb0d2","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b900 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"9bd36d3d-8427-42a7-81c0-b4570d22b72a","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b901 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"9bd36d3d-8427-42a7-81c0-b4570d22b72a","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b914 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"2fa42a0b-385b-4145-8d38-8c1c9c1692e5","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b915 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"2fa42a0b-385b-4145-8d38-8c1c9c1692e5","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
```

---

## Run 20260928T141217Z

- UTC timestamp: `20260928T141217Z`
- GitHub run: [#11177](https://github.com/28twagg-ops/TradingBot/actions/runs/36433921045)
- Run id: `36433921045`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260928T141217Z_live_bot.log`, `logs/action_runs/20260928T141217Z_live_options.log`, `logs/action_runs/20260928T141217Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1509 | 50.2 | +12.5 | +43.6 | $+19,752 |
| TAINTED | 1910 | 33.4 | -38.8 | +12.7 | $-9,579 |
| KEEP-only | 799 | 63.3 | +52.8 | +66.7 | $+13,844 |
| KEEP-only recent | 604 | 62.6 | +56.9 | +76.9 | $+9,759 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T09:57:06.750600-04:00","date":"2026-09-28","mode":"entry+manage","header":"entry+manage (3 new)","elapsed_s":132.3,"phases_s":{"reconcile":0.56,"cancel":0.15,"manage":7.71,"protective_stops":2.06,"scan":53.71,"entries":58.82,"reconcile2":0.51},"signals":464,"placed":3,"equity":995996.14,"open_positions":21,"pending_orders":11,"open_lots":81,"submitted_today":28,"filled_today":17,"unattributed_contracts":7,"top_signals":["S401:PLTR","S359:PLTR","S361:PLTR","S362:PLTR","S363:PLTR","S364:PLTR","S365:PLTR","S366:PLTR"],"github_run":"11174","github_run_id":"36432053690","status":"ok","data_quality":{"clean":{"n":1509,"win":50.23,"med":12.5,"avg":43.63,"pnl":19752.16},"tainted":{"n":1910,"win":33.4,"med":-38.81,"avg":12.65,"pnl":-9579.28},"keep_only":{"n":799,"win":63.33,"med":52.78,"avg":66.74,"pnl":13844.45},"keep_only_recent":{"n":604,"win":62.58,"med":56.92,"avg":76.87,"pnl":9759.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:12:18  INFO      Mode: exits
14:12:18  INFO        Daily log -> logs/daily/2026-09-28.md
14:12:18  INFO        Daily log reconciled -> logs/daily/2026-09-28.md (5 ledger rows)
14:12:19  INFO        Daily log -> logs/daily/2026-09-28.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:12 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.66|
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
=== options_live_micro LIVE 2026-09-28T10:12:19.897908-04:00 share=25% ===
2026-09-28 10:12:19,897 INFO === options_live_micro LIVE 2026-09-28T10:12:19.897908-04:00 share=25% ===
Live account equity $223.66 cash $223.66 #225458845 options_level=3
2026-09-28 10:12:20,023 INFO Live account equity $223.66 cash $223.66 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-28 10:12:20,120 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-28 10:12:20,184 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=89 paper_keys=yes dry_run=False
  alpaca positions=25
  FLAG b277|S350|d9481e7f missing from Alpaca
  FLAG b276|S350|9629162a missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$996,963.85
  buying_power=$3,851,950.08 cash=$975,296.15
  open option orders: 20
    CVNA261002C00068000 OrderSide.BUY qty=1 status=OrderStatus.NEW limit=0.27
    CVNA261002C00068000 OrderSide.BUY qty=1 status=OrderStatus.NEW limit=0.27
    CVNA261002C00068000 OrderSide.BUY qty=1 status=OrderStatus.NEW limit=0.27
    CVNA261002C00068000 OrderSide.BUY qty=1 status=OrderStatus.NEW limit=0.27
    CVNA261002C00068000 OrderSide.BUY qty=1 status=OrderStatus.NEW limit=0.27
  open option positions: 21
    CVNA261002C00070000 qty=8 mkt=$88.00
    DKNG261002C00021000 qty=4 mkt=$352.00
    DKNG261002C00021500 qty=22 mkt=$1,298.00
    DKNG261002C00022000 qty=4 mkt=$168.00
    DKNG261002C00022500 qty=2 mkt=$52.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-28T10:12:23.123552-04:00 ===

[Run context]
Paper auth OK — equity $996981.65, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
  EXIT [b86|lab0086_s210_w4_1120_1135_r1|S210] stop_loss (-92.9%) SELL failed SPY260928C00775000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
Protective stops: placed=1 upgraded=0 already=18 failed=1 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
Found 464 signal(s); top: ['S401:PLTR', 'S359:PLTR', 'S361:PLTR', 'S362:PLTR', 'S363:PLTR', 'S364:PLTR', 'S365:PLTR', 'S366:PLTR']
Paper lab: $996982 broker equity -> 1164 bucket(s) ($500 virtual each, unlimited paper)
  [b364 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9f9ef7a9-9ef8-473e-833b-3c1ae50757ff","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b365 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9f9ef7a9-9ef8-473e-833b-3c1ae50757ff","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b378 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9f9ef7a9-9ef8-473e-833b-3c1ae50757ff","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b379 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9f9ef7a9-9ef8-473e-833b-3c1ae50757ff","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b392 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9f9ef7a9-9ef8-473e-833b-3c1ae50757ff","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b393 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9f9ef7a9-9ef8-473e-833b-3c1ae50757ff","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b914 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9f9ef7a9-9ef8-473e-833b-3c1ae50757ff","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b915 PLTR] ENTRY failed: {"code":40310000,"existing_order_id":"9f9ef7a9-9ef8-473e-833b-3c1ae50757ff","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b364 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"c5b59451-ff0d-41bf-ba6a-d942f2adb0d2","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b365 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"c5b59451-ff0d-41bf-ba6a-d942f2adb0d2","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b378 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"c5b59451-ff0d-41bf-ba6a-d942f2adb0d2","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b379 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"c5b59451-ff0d-41bf-ba6a-d942f2adb0d2","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b392 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"c5b59451-ff0d-41bf-ba6a-d942f2adb0d2","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b393 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"c5b59451-ff0d-41bf-ba6a-d942f2adb0d2","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b914 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"c5b59451-ff0d-41bf-ba6a-d942f2adb0d2","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b915 DKNG] ENTRY failed: {"code":40310000,"existing_order_id":"c5b59451-ff0d-41bf-ba6a-d942f2adb0d2","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b282 CVNA] ENTRY failed: {"code":40310000,"existing_order_id":"72862e86-8f2a-4a8a-a78e-bd02af64adc1","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b283 CVNA] ENTRY failed: {"code":40310000,"existing_order_id":"72862e86-8f2a-4a8a-a78e-bd02af64adc1","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b794 CVNA] ENTRY failed: {"code":40310000,"existing_order_id":"72862e86-8f2a-4a8a-a78e-bd02af64adc1","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b795 CVNA] ENTRY failed: {"code":40310000,"existing_order_id":"72862e86-8f2a-4a8a-a78e-bd02af64adc1","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
```

---

## Run 20260928T141705Z

- UTC timestamp: `20260928T141705Z`
- GitHub run: [#11178](https://github.com/28twagg-ops/TradingBot/actions/runs/36434550685)
- Run id: `36434550685`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`217s`
- Full logs: `logs/action_runs/20260928T141705Z_live_bot.log`, `logs/action_runs/20260928T141705Z_live_options.log`, `logs/action_runs/20260928T141705Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1509 | 50.2 | +12.5 | +43.6 | $+19,752 |
| TAINTED | 1912 | 33.5 | -38.6 | +12.7 | $-9,478 |
| KEEP-only | 799 | 63.3 | +52.8 | +66.7 | $+13,844 |
| KEEP-only recent | 604 | 62.6 | +56.9 | +76.9 | $+9,759 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T10:17:10.345686-04:00","date":"2026-09-28","mode":"entry+manage","header":"entry+manage (23 new)","elapsed_s":204.4,"phases_s":{"reconcile":0.85,"cancel":0.03,"manage":5.66,"protective_stops":0.35,"scan":53.7,"entries":129.8,"reconcile2":3.98},"signals":464,"placed":23,"equity":996603.15,"open_positions":27,"pending_orders":14,"open_lots":121,"submitted_today":59,"filled_today":59,"unattributed_contracts":0,"top_signals":["S401:PLTR","S359:PLTR","S361:PLTR","S362:PLTR","S363:PLTR","S364:PLTR","S365:PLTR","S366:PLTR"],"github_run":"11178","github_run_id":"36434550685","status":"ok","data_quality":{"clean":{"n":1509,"win":50.23,"med":12.5,"avg":43.63,"pnl":19752.16},"tainted":{"n":1912,"win":33.47,"med":-38.59,"avg":12.73,"pnl":-9478.28},"keep_only":{"n":799,"win":63.33,"med":52.78,"avg":66.74,"pnl":13844.45},"keep_only_recent":{"n":604,"win":62.58,"med":56.92,"avg":76.87,"pnl":9759.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:17:06  INFO      Mode: exits
14:17:06  INFO        Daily log -> logs/daily/2026-09-28.md
14:17:06  INFO        Daily log reconciled -> logs/daily/2026-09-28.md (5 ledger rows)
14:17:06  INFO        Daily log -> logs/daily/2026-09-28.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:17 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.66|
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
=== options_live_micro LIVE 2026-09-28T10:17:07.611344-04:00 share=25% ===
2026-09-28 10:17:07,611 INFO === options_live_micro LIVE 2026-09-28T10:17:07.611344-04:00 share=25% ===
Live account equity $223.66 cash $223.66 #225458845 options_level=3
2026-09-28 10:17:07,655 INFO Live account equity $223.66 cash $223.66 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-28 10:17:07,675 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-28 10:17:07,688 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (217 earlier lines - see full log file)
| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 295 | 21 |
| S164 | 335 | 24 |
| S165 | 1761 | 36 |
| S166 | 139 | 10 |
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
| 2026-09-28 |    2 |    2 |    2 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |

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
| Total open lots             |   121 | INFO |
| Total closed lots           |  2544 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1509 med=+12.5% | TAINTED n=1912 med=-38.6% | KEEP-only n=799 med=+52.8% | KILL=19 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.66 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260928T142221Z

- UTC timestamp: `20260928T142221Z`
- GitHub run: [#11179](https://github.com/28twagg-ops/TradingBot/actions/runs/36435179709)
- Run id: `36435179709`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`178s`
- Full logs: `logs/action_runs/20260928T142221Z_live_bot.log`, `logs/action_runs/20260928T142221Z_live_options.log`, `logs/action_runs/20260928T142221Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1509 | 50.2 | +12.5 | +43.6 | $+19,752 |
| TAINTED | 1911 | 33.4 | -38.8 | +12.7 | $-9,564 |
| KEEP-only | 799 | 63.3 | +52.8 | +66.7 | $+13,844 |
| KEEP-only recent | 604 | 62.6 | +56.9 | +76.9 | $+9,759 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T10:22:26.093716-04:00","date":"2026-09-28","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":165.3,"phases_s":{"reconcile":1.65,"cancel":0.03,"manage":6.58,"protective_stops":0.33,"scan":53.75,"entries":92.79,"reconcile2":0.17},"signals":464,"placed":0,"equity":996846.69,"open_positions":27,"pending_orders":5,"open_lots":121,"submitted_today":44,"filled_today":59,"unattributed_contracts":0,"top_signals":["S401:PLTR","S359:PLTR","S361:PLTR","S362:PLTR","S363:PLTR","S364:PLTR","S365:PLTR","S366:PLTR"],"github_run":"11179","github_run_id":"36435179709","status":"ok","data_quality":{"clean":{"n":1509,"win":50.23,"med":12.5,"avg":43.63,"pnl":19752.16},"tainted":{"n":1911,"win":33.44,"med":-38.81,"avg":12.66,"pnl":-9564.28},"keep_only":{"n":799,"win":63.33,"med":52.78,"avg":66.74,"pnl":13844.45},"keep_only_recent":{"n":604,"win":62.58,"med":56.92,"avg":76.87,"pnl":9759.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:22:21  INFO      Mode: exits
14:22:22  INFO        Daily log -> logs/daily/2026-09-28.md
14:22:22  INFO        Daily log reconciled -> logs/daily/2026-09-28.md (5 ledger rows)
14:22:22  INFO        Daily log -> logs/daily/2026-09-28.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:22 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.66|
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
=== options_live_micro LIVE 2026-09-28T10:22:23.033405-04:00 share=25% ===
2026-09-28 10:22:23,033 INFO === options_live_micro LIVE 2026-09-28T10:22:23.033405-04:00 share=25% ===
Live account equity $223.66 cash $223.66 #225458845 options_level=3
2026-09-28 10:22:23,368 INFO Live account equity $223.66 cash $223.66 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-28 10:22:23,389 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-28 10:22:23,403 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (198 earlier lines - see full log file)
| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 295 | 21 |
| S164 | 335 | 24 |
| S165 | 1761 | 36 |
| S166 | 139 | 10 |
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
| 2026-09-28 |    2 |    2 |    2 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |

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
| Total open lots             |   121 | INFO |
| Total closed lots           |  2543 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1509 med=+12.5% | TAINTED n=1911 med=-38.8% | KEEP-only n=799 med=+52.8% | KILL=19 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.66 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260928T142700Z

- UTC timestamp: `20260928T142700Z`
- GitHub run: [#11180](https://github.com/28twagg-ops/TradingBot/actions/runs/36435795608)
- Run id: `36435795608`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`106s`
- Full logs: `logs/action_runs/20260928T142700Z_live_bot.log`, `logs/action_runs/20260928T142700Z_live_options.log`, `logs/action_runs/20260928T142700Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1509 | 50.2 | +12.5 | +43.6 | $+19,752 |
| TAINTED | 1912 | 33.5 | -38.6 | +12.7 | $-9,478 |
| KEEP-only | 799 | 63.3 | +52.8 | +66.7 | $+13,844 |
| KEEP-only recent | 604 | 62.6 | +56.9 | +76.9 | $+9,759 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T10:27:05.213834-04:00","date":"2026-09-28","mode":"entry+manage","header":"entry+manage (4 new)","elapsed_s":97.6,"phases_s":{"reconcile":0.48,"cancel":0.09,"manage":7.36,"protective_stops":1.1,"scan":24.05,"entries":53.61,"reconcile2":3.26},"signals":464,"placed":4,"equity":996717.69,"open_positions":27,"pending_orders":18,"open_lots":121,"submitted_today":63,"filled_today":59,"unattributed_contracts":0,"top_signals":["S401:PLTR","S359:PLTR","S361:PLTR","S362:PLTR","S363:PLTR","S364:PLTR","S365:PLTR","S366:PLTR"],"github_run":"11180","github_run_id":"36435795608","status":"ok","data_quality":{"clean":{"n":1509,"win":50.23,"med":12.5,"avg":43.63,"pnl":19752.16},"tainted":{"n":1912,"win":33.47,"med":-38.59,"avg":12.73,"pnl":-9478.28},"keep_only":{"n":799,"win":63.33,"med":52.78,"avg":66.74,"pnl":13844.45},"keep_only_recent":{"n":604,"win":62.58,"med":56.92,"avg":76.87,"pnl":9759.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:27:00  INFO      Mode: exits
14:27:01  INFO        Daily log -> logs/daily/2026-09-28.md
14:27:01  INFO        Daily log reconciled -> logs/daily/2026-09-28.md (5 ledger rows)
14:27:01  INFO        Daily log -> logs/daily/2026-09-28.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:27 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.66|
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
=== options_live_micro LIVE 2026-09-28T10:27:02.468072-04:00 share=25% ===
2026-09-28 10:27:02,468 INFO === options_live_micro LIVE 2026-09-28T10:27:02.468072-04:00 share=25% ===
Live account equity $223.66 cash $223.66 #225458845 options_level=3
2026-09-28 10:27:02,626 INFO Live account equity $223.66 cash $223.66 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-28 10:27:02,750 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-28 10:27:02,831 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (203 earlier lines - see full log file)
| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 295 | 21 |
| S164 | 335 | 24 |
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
| 2026-09-28 |    2 |    2 |    2 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |

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
| Total open lots             |   121 | INFO |
| Total closed lots           |  2544 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1509 med=+12.5% | TAINTED n=1912 med=-38.6% | KEEP-only n=799 med=+52.8% | KILL=19 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.66 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260928T143119Z

- UTC timestamp: `20260928T143119Z`
- GitHub run: [#11181](https://github.com/28twagg-ops/TradingBot/actions/runs/36436436530)
- Run id: `36436436530`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`134s`
- Full logs: `logs/action_runs/20260928T143119Z_live_bot.log`, `logs/action_runs/20260928T143119Z_live_options.log`, `logs/action_runs/20260928T143119Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1509 | 50.2 | +12.5 | +43.6 | $+19,752 |
| TAINTED | 1913 | 33.5 | -38.8 | +12.7 | $-9,501 |
| KEEP-only | 799 | 63.3 | +52.8 | +66.7 | $+13,844 |
| KEEP-only recent | 604 | 62.6 | +56.9 | +76.9 | $+9,759 |

- KEEP strategies (25): S163, S164, S167, S168, S173, S174, S210, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (19): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-28T10:31:25.249174-04:00","date":"2026-09-28","mode":"entry+manage","header":"entry+manage (1 new)","elapsed_s":121.4,"phases_s":{"reconcile":0.34,"cancel":0.03,"manage":9.03,"protective_stops":0.5,"scan":53.07,"entries":45.17,"reconcile2":3.29},"signals":464,"placed":1,"equity":996567.42,"open_positions":29,"pending_orders":14,"open_lots":122,"submitted_today":64,"filled_today":66,"unattributed_contracts":0,"top_signals":["S401:PLTR","S359:PLTR","S361:PLTR","S362:PLTR","S363:PLTR","S364:PLTR","S365:PLTR","S366:PLTR"],"github_run":"11181","github_run_id":"36436436530","status":"ok","data_quality":{"clean":{"n":1509,"win":50.23,"med":12.5,"avg":43.63,"pnl":19752.16},"tainted":{"n":1913,"win":33.46,"med":-38.81,"avg":12.7,"pnl":-9501.28},"keep_only":{"n":799,"win":63.33,"med":52.78,"avg":66.74,"pnl":13844.45},"keep_only_recent":{"n":604,"win":62.58,"med":56.92,"avg":76.87,"pnl":9759.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:31:20  INFO      Mode: exits
14:31:20  INFO        Daily log -> logs/daily/2026-09-28.md
14:31:20  INFO        Daily log reconciled -> logs/daily/2026-09-28.md (5 ledger rows)
14:31:21  INFO        Daily log -> logs/daily/2026-09-28.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.66|
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
=== options_live_micro LIVE 2026-09-28T10:31:21.961494-04:00 share=25% ===
2026-09-28 10:31:21,961 INFO === options_live_micro LIVE 2026-09-28T10:31:21.961494-04:00 share=25% ===
Live account equity $223.66 cash $223.66 #225458845 options_level=3
2026-09-28 10:31:22,230 INFO Live account equity $223.66 cash $223.66 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-28 10:31:22,250 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-28 10:31:22,265 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (210 earlier lines - see full log file)
| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 295 | 21 |
| S164 | 335 | 24 |
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
| 2026-09-28 |    2 |    2 |    2 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |

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
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |   122 | INFO |
| Total closed lots           |  2545 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-28_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1509 med=+12.5% | TAINTED n=1913 med=-38.8% | KEEP-only n=799 med=+52.8% | KILL=19 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.66 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---
