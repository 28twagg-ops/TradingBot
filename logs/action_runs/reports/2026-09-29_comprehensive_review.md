# Daily Comprehensive Action Review - 2026-09-29

_Auto-generated from GitHub Actions run output. Each run appends a summary; full stdout is in linked per-run log files._
## Run 20260929T130126Z

- UTC timestamp: `20260929T130126Z`
- GitHub run: [#11295](https://github.com/28twagg-ops/TradingBot/actions/runs/36571940577)
- Run id: `36571940577`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`14s`
- Full logs: `logs/action_runs/20260929T130126Z_live_bot.log`, `logs/action_runs/20260929T130126Z_live_options.log`, `logs/action_runs/20260929T130126Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1545 | 49.6 | -7.7 | +42.0 | $+19,545 |
| TAINTED | 1925 | 33.5 | -39.0 | +12.6 | $-9,424 |
| KEEP-only | 794 | 62.7 | +52.3 | +62.6 | $+13,455 |
| KEEP-only recent | 600 | 61.8 | +56.2 | +71.6 | $+9,417 |

- KEEP strategies (24): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (20): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-29T09:01:33.404944-04:00","date":"2026-09-29","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.5,"phases_s":{"reconcile":0.61},"signals":0,"placed":0,"equity":995048.15,"open_positions":30,"pending_orders":0,"open_lots":120,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11295","github_run_id":"36571940577","status":"ok","data_quality":{"clean":{"n":1545,"win":49.58,"med":-7.69,"avg":41.96,"pnl":19544.83},"tainted":{"n":1925,"win":33.45,"med":-38.98,"avg":12.59,"pnl":-9424.28},"keep_only":{"n":794,"win":62.72,"med":52.28,"avg":62.62,"pnl":13455.45},"keep_only_recent":{"n":600,"win":61.83,"med":56.2,"avg":71.58,"pnl":9417.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:01:27  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.70|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $223.70|
|  Cash                                                           $156.57|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $67.13|
|  Open P&L                                                        $+0.05|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AYI      MomReversal     $33.59     $305.46  $305.91  +0.1%   $+0.05  |
|  NNN      MomReversal     $33.54     $41.40   $41.40   +0.0%   $+0.00  |
|                                                                        |
|  Total invested                                                  $67.13|
|  Total open P&L                                                  $+0.05|
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
|  2026-09-28  SELL  AES  Pullback50  $33.53  P&L $-0.02                 |
|  2026-09-28  SELL  AES  Pullback50  $33.56  P&L $-0.00                 |
|  2026-09-28  SELL  AKAM  Pullback50  $33.59  P&L $-0.01                |
|  2026-09-28  SELL  GOOGL  Pullback50  $33.55  P&L $-0.02               |
|  2026-09-28  SELL  CVS  MomReversal  $33.86  P&L $+0.29                |
|  2026-09-28  SELL  EVR  MomReversal  $33.25  P&L $-0.32                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-29T09:01:29.641837-04:00 share=25% ===
2026-09-29 09:01:29,641 INFO === options_live_micro LIVE 2026-09-29T09:01:29.641837-04:00 share=25% ===
Live account equity $223.70 cash $156.57 #225458845 options_level=3
2026-09-29 09:01:29,878 INFO Live account equity $223.70 cash $156.57 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-29 09:01:29,950 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-29 09:01:30,021 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (175 earlier lines - see full log file)
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
## Ledger health — 2026-09-29
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1619 | WARN | <<<
| Missing exit records (post) |  1619 | WARN | <<<
| State/ledger mismatches     |     5 | WARN | <<<
| Total open lots             |   120 | INFO |
| Total closed lots           |  2587 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1545 med=-7.7% | TAINTED n=1925 med=-39.0% | KEEP-only n=794 med=+52.3% | KILL=20 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260929T130628Z

- UTC timestamp: `20260929T130628Z`
- GitHub run: [#11296](https://github.com/28twagg-ops/TradingBot/actions/runs/36572541835)
- Run id: `36572541835`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`13s`
- Full logs: `logs/action_runs/20260929T130628Z_live_bot.log`, `logs/action_runs/20260929T130628Z_live_options.log`, `logs/action_runs/20260929T130628Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1545 | 49.6 | -7.7 | +42.0 | $+19,545 |
| TAINTED | 1925 | 33.5 | -39.0 | +12.6 | $-9,424 |
| KEEP-only | 794 | 62.7 | +52.3 | +62.6 | $+13,455 |
| KEEP-only recent | 600 | 61.8 | +56.2 | +71.6 | $+9,417 |

- KEEP strategies (24): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (20): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-29T09:06:33.819109-04:00","date":"2026-09-29","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.8,"phases_s":{"reconcile":0.11},"signals":0,"placed":0,"equity":995014.15,"open_positions":30,"pending_orders":0,"open_lots":120,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11296","github_run_id":"36572541835","status":"ok","data_quality":{"clean":{"n":1545,"win":49.58,"med":-7.69,"avg":41.96,"pnl":19544.83},"tainted":{"n":1925,"win":33.45,"med":-38.98,"avg":12.59,"pnl":-9424.28},"keep_only":{"n":794,"win":62.72,"med":52.28,"avg":62.62,"pnl":13455.45},"keep_only_recent":{"n":600,"win":61.83,"med":56.2,"avg":71.58,"pnl":9417.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:06:30  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.86|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $223.86|
|  Cash                                                           $156.57|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $67.29|
|  Open P&L                                                        $+0.21|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AYI      MomReversal     $33.59     $305.46  $305.91  +0.1%   $+0.05  |
|  NNN      MomReversal     $33.70     $41.40   $41.60   +0.5%   $+0.16  |
|                                                                        |
|  Total invested                                                  $67.29|
|  Total open P&L                                                  $+0.21|
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
|  2026-09-28  SELL  AES  Pullback50  $33.53  P&L $-0.02                 |
|  2026-09-28  SELL  AES  Pullback50  $33.56  P&L $-0.00                 |
|  2026-09-28  SELL  AKAM  Pullback50  $33.59  P&L $-0.01                |
|  2026-09-28  SELL  GOOGL  Pullback50  $33.55  P&L $-0.02               |
|  2026-09-28  SELL  CVS  MomReversal  $33.86  P&L $+0.29                |
|  2026-09-28  SELL  EVR  MomReversal  $33.25  P&L $-0.32                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-29T09:06:31.139604-04:00 share=25% ===
2026-09-29 09:06:31,139 INFO === options_live_micro LIVE 2026-09-29T09:06:31.139604-04:00 share=25% ===
Live account equity $223.86 cash $156.57 #225458845 options_level=3
2026-09-29 09:06:31,183 INFO Live account equity $223.86 cash $156.57 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-29 09:06:31,191 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-29 09:06:31,199 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (173 earlier lines - see full log file)
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
## Ledger health — 2026-09-29
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1619 | WARN | <<<
| Missing exit records (post) |  1619 | WARN | <<<
| State/ledger mismatches     |     5 | WARN | <<<
| Total open lots             |   120 | INFO |
| Total closed lots           |  2587 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1545 med=-7.7% | TAINTED n=1925 med=-39.0% | KEEP-only n=794 med=+52.3% | KILL=20 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.86 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260929T131125Z

- UTC timestamp: `20260929T131125Z`
- GitHub run: [#11297](https://github.com/28twagg-ops/TradingBot/actions/runs/36573135822)
- Run id: `36573135822`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`15s`
- Full logs: `logs/action_runs/20260929T131125Z_live_bot.log`, `logs/action_runs/20260929T131125Z_live_options.log`, `logs/action_runs/20260929T131125Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1545 | 49.6 | -7.7 | +42.0 | $+19,545 |
| TAINTED | 1925 | 33.5 | -39.0 | +12.6 | $-9,424 |
| KEEP-only | 794 | 62.7 | +52.3 | +62.6 | $+13,455 |
| KEEP-only recent | 600 | 61.8 | +56.2 | +71.6 | $+9,417 |

- KEEP strategies (24): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (20): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-29T09:11:32.033690-04:00","date":"2026-09-29","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.5,"phases_s":{"reconcile":0.6},"signals":0,"placed":0,"equity":994962.21,"open_positions":30,"pending_orders":0,"open_lots":120,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11297","github_run_id":"36573135822","status":"ok","data_quality":{"clean":{"n":1545,"win":49.58,"med":-7.69,"avg":41.96,"pnl":19544.83},"tainted":{"n":1925,"win":33.45,"med":-38.98,"avg":12.59,"pnl":-9424.28},"keep_only":{"n":794,"win":62.72,"med":52.28,"avg":62.62,"pnl":13455.45},"keep_only_recent":{"n":600,"win":61.83,"med":56.2,"avg":71.58,"pnl":9417.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:11:26  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.86|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $223.86|
|  Cash                                                           $156.57|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $67.29|
|  Open P&L                                                        $+0.21|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AYI      MomReversal     $33.59     $305.46  $305.91  +0.1%   $+0.05  |
|  NNN      MomReversal     $33.70     $41.40   $41.60   +0.5%   $+0.16  |
|                                                                        |
|  Total invested                                                  $67.29|
|  Total open P&L                                                  $+0.21|
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
|  2026-09-28  SELL  AES  Pullback50  $33.53  P&L $-0.02                 |
|  2026-09-28  SELL  AES  Pullback50  $33.56  P&L $-0.00                 |
|  2026-09-28  SELL  AKAM  Pullback50  $33.59  P&L $-0.01                |
|  2026-09-28  SELL  GOOGL  Pullback50  $33.55  P&L $-0.02               |
|  2026-09-28  SELL  CVS  MomReversal  $33.86  P&L $+0.29                |
|  2026-09-28  SELL  EVR  MomReversal  $33.25  P&L $-0.32                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-29T09:11:27.972572-04:00 share=25% ===
2026-09-29 09:11:27,972 INFO === options_live_micro LIVE 2026-09-29T09:11:27.972572-04:00 share=25% ===
Live account equity $223.86 cash $156.57 #225458845 options_level=3
2026-09-29 09:11:28,206 INFO Live account equity $223.86 cash $156.57 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-29 09:11:28,278 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-29 09:11:28,347 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (173 earlier lines - see full log file)
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
## Ledger health — 2026-09-29
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1619 | WARN | <<<
| Missing exit records (post) |  1619 | WARN | <<<
| State/ledger mismatches     |     5 | WARN | <<<
| Total open lots             |   120 | INFO |
| Total closed lots           |  2587 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1545 med=-7.7% | TAINTED n=1925 med=-39.0% | KEEP-only n=794 med=+52.3% | KILL=20 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.86 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260929T131616Z

- UTC timestamp: `20260929T131616Z`
- GitHub run: [#11298](https://github.com/28twagg-ops/TradingBot/actions/runs/36573727936)
- Run id: `36573727936`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`12s`
- Full logs: `logs/action_runs/20260929T131616Z_live_bot.log`, `logs/action_runs/20260929T131616Z_live_options.log`, `logs/action_runs/20260929T131616Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1545 | 49.6 | -7.7 | +42.0 | $+19,545 |
| TAINTED | 1925 | 33.5 | -39.0 | +12.6 | $-9,424 |
| KEEP-only | 794 | 62.7 | +52.3 | +62.6 | $+13,455 |
| KEEP-only recent | 600 | 61.8 | +56.2 | +71.6 | $+9,417 |

- KEEP strategies (24): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (20): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-29T09:16:21.631394-04:00","date":"2026-09-29","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.2},"signals":0,"placed":0,"equity":994846.15,"open_positions":30,"pending_orders":0,"open_lots":120,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11298","github_run_id":"36573727936","status":"ok","data_quality":{"clean":{"n":1545,"win":49.58,"med":-7.69,"avg":41.96,"pnl":19544.83},"tainted":{"n":1925,"win":33.45,"med":-38.98,"avg":12.59,"pnl":-9424.28},"keep_only":{"n":794,"win":62.72,"med":52.28,"avg":62.62,"pnl":13455.45},"keep_only_recent":{"n":600,"win":61.83,"med":56.2,"avg":71.58,"pnl":9417.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
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
|  Equity                                                         $223.94|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $223.94|
|  Cash                                                           $156.57|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $67.37|
|  Open P&L                                                        $+0.29|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AYI      MomReversal     $33.67     $305.46  $306.60  +0.4%   $+0.13  |
|  NNN      MomReversal     $33.70     $41.40   $41.60   +0.5%   $+0.16  |
|                                                                        |
|  Total invested                                                  $67.37|
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
|  2026-09-28  SELL  AES  Pullback50  $33.53  P&L $-0.02                 |
|  2026-09-28  SELL  AES  Pullback50  $33.56  P&L $-0.00                 |
|  2026-09-28  SELL  AKAM  Pullback50  $33.59  P&L $-0.01                |
|  2026-09-28  SELL  GOOGL  Pullback50  $33.55  P&L $-0.02               |
|  2026-09-28  SELL  CVS  MomReversal  $33.86  P&L $+0.29                |
|  2026-09-28  SELL  EVR  MomReversal  $33.25  P&L $-0.32                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-29T09:16:18.466794-04:00 share=25% ===
2026-09-29 09:16:18,466 INFO === options_live_micro LIVE 2026-09-29T09:16:18.466794-04:00 share=25% ===
Live account equity $223.94 cash $156.57 #225458845 options_level=3
2026-09-29 09:16:18,942 INFO Live account equity $223.94 cash $156.57 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-29 09:16:18,965 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-29 09:16:18,986 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (173 earlier lines - see full log file)
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
## Ledger health — 2026-09-29
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1619 | WARN | <<<
| Missing exit records (post) |  1619 | WARN | <<<
| State/ledger mismatches     |     5 | WARN | <<<
| Total open lots             |   120 | INFO |
| Total closed lots           |  2587 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1545 med=-7.7% | TAINTED n=1925 med=-39.0% | KEEP-only n=794 med=+52.3% | KILL=20 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.94 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260929T132119Z

- UTC timestamp: `20260929T132119Z`
- GitHub run: [#11299](https://github.com/28twagg-ops/TradingBot/actions/runs/36574317179)
- Run id: `36574317179`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`13s`
- Full logs: `logs/action_runs/20260929T132119Z_live_bot.log`, `logs/action_runs/20260929T132119Z_live_options.log`, `logs/action_runs/20260929T132119Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1545 | 49.6 | -7.7 | +42.0 | $+19,545 |
| TAINTED | 1925 | 33.5 | -39.0 | +12.6 | $-9,424 |
| KEEP-only | 794 | 62.7 | +52.3 | +62.6 | $+13,455 |
| KEEP-only recent | 600 | 61.8 | +56.2 | +71.6 | $+9,417 |

- KEEP strategies (24): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (20): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-29T09:21:24.877030-04:00","date":"2026-09-29","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.0,"phases_s":{"reconcile":0.24},"signals":0,"placed":0,"equity":994799.15,"open_positions":30,"pending_orders":0,"open_lots":120,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11299","github_run_id":"36574317179","status":"ok","data_quality":{"clean":{"n":1545,"win":49.58,"med":-7.69,"avg":41.96,"pnl":19544.83},"tainted":{"n":1925,"win":33.45,"med":-38.98,"avg":12.59,"pnl":-9424.28},"keep_only":{"n":794,"win":62.72,"med":52.28,"avg":62.62,"pnl":13455.45},"keep_only_recent":{"n":600,"win":61.83,"med":56.2,"avg":71.58,"pnl":9417.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:21:20  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.94|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $223.94|
|  Cash                                                           $156.57|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $67.37|
|  Open P&L                                                        $+0.29|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AYI      MomReversal     $33.67     $305.46  $306.60  +0.4%   $+0.13  |
|  NNN      MomReversal     $33.70     $41.40   $41.60   +0.5%   $+0.16  |
|                                                                        |
|  Total invested                                                  $67.37|
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
|  2026-09-28  SELL  AES  Pullback50  $33.53  P&L $-0.02                 |
|  2026-09-28  SELL  AES  Pullback50  $33.56  P&L $-0.00                 |
|  2026-09-28  SELL  AKAM  Pullback50  $33.59  P&L $-0.01                |
|  2026-09-28  SELL  GOOGL  Pullback50  $33.55  P&L $-0.02               |
|  2026-09-28  SELL  CVS  MomReversal  $33.86  P&L $+0.29                |
|  2026-09-28  SELL  EVR  MomReversal  $33.25  P&L $-0.32                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-29T09:21:21.933052-04:00 share=25% ===
2026-09-29 09:21:21,933 INFO === options_live_micro LIVE 2026-09-29T09:21:21.933052-04:00 share=25% ===
Live account equity $223.94 cash $156.57 #225458845 options_level=3
2026-09-29 09:21:22,028 INFO Live account equity $223.94 cash $156.57 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-29 09:21:22,050 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-29 09:21:22,075 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (173 earlier lines - see full log file)
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
## Ledger health — 2026-09-29
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1619 | WARN | <<<
| Missing exit records (post) |  1619 | WARN | <<<
| State/ledger mismatches     |     5 | WARN | <<<
| Total open lots             |   120 | INFO |
| Total closed lots           |  2587 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1545 med=-7.7% | TAINTED n=1925 med=-39.0% | KEEP-only n=794 med=+52.3% | KILL=20 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.94 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260929T132627Z

- UTC timestamp: `20260929T132627Z`
- GitHub run: [#11300](https://github.com/28twagg-ops/TradingBot/actions/runs/36574927117)
- Run id: `36574927117`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`14s`
- Full logs: `logs/action_runs/20260929T132627Z_live_bot.log`, `logs/action_runs/20260929T132627Z_live_options.log`, `logs/action_runs/20260929T132627Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1545 | 49.6 | -7.7 | +42.0 | $+19,545 |
| TAINTED | 1925 | 33.5 | -39.0 | +12.6 | $-9,424 |
| KEEP-only | 794 | 62.7 | +52.3 | +62.6 | $+13,455 |
| KEEP-only recent | 600 | 61.8 | +56.2 | +71.6 | $+9,417 |

- KEEP strategies (24): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (20): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-29T09:26:33.211793-04:00","date":"2026-09-29","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.4,"phases_s":{"reconcile":0.54},"signals":0,"placed":0,"equity":994607.48,"open_positions":30,"pending_orders":0,"open_lots":120,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11300","github_run_id":"36574927117","status":"ok","data_quality":{"clean":{"n":1545,"win":49.58,"med":-7.69,"avg":41.96,"pnl":19544.83},"tainted":{"n":1925,"win":33.45,"med":-38.98,"avg":12.59,"pnl":-9424.28},"keep_only":{"n":794,"win":62.72,"med":52.28,"avg":62.62,"pnl":13455.45},"keep_only_recent":{"n":600,"win":61.83,"med":56.2,"avg":71.58,"pnl":9417.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:26:28  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.94|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $223.94|
|  Cash                                                           $156.57|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $67.37|
|  Open P&L                                                        $+0.29|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AYI      MomReversal     $33.67     $305.46  $306.60  +0.4%   $+0.13  |
|  NNN      MomReversal     $33.70     $41.40   $41.60   +0.5%   $+0.16  |
|                                                                        |
|  Total invested                                                  $67.37|
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
|  2026-09-28  SELL  AES  Pullback50  $33.53  P&L $-0.02                 |
|  2026-09-28  SELL  AES  Pullback50  $33.56  P&L $-0.00                 |
|  2026-09-28  SELL  AKAM  Pullback50  $33.59  P&L $-0.01                |
|  2026-09-28  SELL  GOOGL  Pullback50  $33.55  P&L $-0.02               |
|  2026-09-28  SELL  CVS  MomReversal  $33.86  P&L $+0.29                |
|  2026-09-28  SELL  EVR  MomReversal  $33.25  P&L $-0.32                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-29T09:26:29.669999-04:00 share=25% ===
2026-09-29 09:26:29,670 INFO === options_live_micro LIVE 2026-09-29T09:26:29.669999-04:00 share=25% ===
Live account equity $223.94 cash $156.57 #225458845 options_level=3
2026-09-29 09:26:29,917 INFO Live account equity $223.94 cash $156.57 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-29 09:26:29,986 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-29 09:26:30,054 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (173 earlier lines - see full log file)
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
## Ledger health — 2026-09-29
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1619 | WARN | <<<
| Missing exit records (post) |  1619 | WARN | <<<
| State/ledger mismatches     |     5 | WARN | <<<
| Total open lots             |   120 | INFO |
| Total closed lots           |  2587 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1545 med=-7.7% | TAINTED n=1925 med=-39.0% | KEEP-only n=794 med=+52.3% | KILL=20 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.94 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260929T133126Z

- UTC timestamp: `20260929T133126Z`
- GitHub run: [#11301](https://github.com/28twagg-ops/TradingBot/actions/runs/36575541309)
- Run id: `36575541309`
- Live bot: exit=`0`, duration=`218s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260929T133126Z_live_bot.log`, `logs/action_runs/20260929T133126Z_live_options.log`, `logs/action_runs/20260929T133126Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1545 | 49.6 | -7.7 | +42.0 | $+19,545 |
| TAINTED | 1925 | 33.5 | -39.0 | +12.6 | $-9,424 |
| KEEP-only | 794 | 62.7 | +52.3 | +62.6 | $+13,455 |
| KEEP-only recent | 600 | 61.8 | +56.2 | +71.6 | $+9,417 |

- KEEP strategies (24): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (20): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-29T09:26:33.211793-04:00","date":"2026-09-29","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.4,"phases_s":{"reconcile":0.54},"signals":0,"placed":0,"equity":994607.48,"open_positions":30,"pending_orders":0,"open_lots":120,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11300","github_run_id":"36574927117","status":"ok","data_quality":{"clean":{"n":1545,"win":49.58,"med":-7.69,"avg":41.96,"pnl":19544.83},"tainted":{"n":1925,"win":33.45,"med":-38.98,"avg":12.59,"pnl":-9424.28},"keep_only":{"n":794,"win":62.72,"med":52.28,"avg":62.62,"pnl":13455.45},"keep_only_recent":{"n":600,"win":61.83,"med":56.2,"avg":71.58,"pnl":9417.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:31:27  INFO      Mode: morning_prep
13:31:28  INFO        [prep_positions] 2/2 (2 valid)
13:31:28  INFO      Fetching tickers (universe=both)...
13:31:29  INFO        S&P 500: 503
13:31:29  INFO        MidCap 400: 400
13:31:29  INFO        Total: 903 tickers
13:31:30  INFO        [prep_universe] 40/901 (40 valid)
13:31:31  INFO        [prep_universe] 80/901 (80 valid)
13:31:32  INFO        [prep_universe] 120/901 (120 valid)
13:31:34  INFO        [prep_universe] 160/901 (160 valid)
13:31:35  INFO        [prep_universe] 200/901 (199 valid)
13:31:42  INFO        [prep_universe] 240/901 (238 valid)
13:31:55  INFO        [prep_universe] 280/901 (278 valid)
13:32:08  INFO        [prep_universe] 320/901 (318 valid)
13:32:18  INFO        [prep_universe] 360/901 (358 valid)
13:32:31  INFO        [prep_universe] 400/901 (398 valid)
13:32:44  INFO        [prep_universe] 440/901 (438 valid)
13:32:54  INFO        [prep_universe] 480/901 (478 valid)
13:33:07  INFO        [prep_universe] 520/901 (518 valid)
13:33:20  INFO        [prep_universe] 560/901 (558 valid)
13:33:30  INFO        [prep_universe] 600/901 (598 valid)
13:33:43  INFO        [prep_universe] 640/901 (638 valid)
13:33:53  INFO        [prep_universe] 680/901 (678 valid)
13:34:06  INFO        [prep_universe] 720/901 (718 valid)
13:34:19  INFO        [prep_universe] 760/901 (758 valid)
13:34:32  INFO        [prep_universe] 800/901 (798 valid)
13:34:42  INFO        [prep_universe] 840/901 (838 valid)
13:34:55  INFO        [prep_universe] 880/901 (878 valid)
13:35:02  INFO        [prep_universe] 901/901 (899 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.73|
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
|  Invested                                                        $67.16|
|  Open P&L                                                        $+0.08|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AYI      MomReversal     $33.88     $305.46  $308.55  +1.0%   $+0.34  |
|  NNN      MomReversal     $33.28     $41.40   $41.08   -0.8%   $-0.26  |
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
|  Signal candidates                                                   23|
|  Universe scanned                                                   901|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-29T09:35:05.164990-04:00 share=25% ===
2026-09-29 09:35:05,165 INFO === options_live_micro LIVE 2026-09-29T09:35:05.164990-04:00 share=25% ===
Live account equity $223.46 cash $156.57 #225458845 options_level=3
2026-09-29 09:35:05,252 INFO Live account equity $223.46 cash $156.57 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-29 09:35:05,322 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-29 09:35:05,364 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=120 paper_keys=yes dry_run=False
  alpaca positions=29
  FLAG b263|S403|3eabcde9 missing from Alpaca
  FLAG b265|S403|b80b4c98 missing from Alpaca
  FLAG b377|S362|cf588856 missing from Alpaca
  FLAG b376|S362|23f383f2 missing from Alpaca
  FLAG b363|S361|0128b299 missing from Alpaca
  FLAG b362|S361|7043c90d missing from Alpaca
  FLAG b235|S401|aab77879 missing from Alpaca
  FLAG b234|S401|ef2f7f9c missing from Alpaca
  FLAG b915|S412|1292c040 missing from Alpaca
  FLAG b914|S412|e8596fd6 missing from Alpaca
  FLAG b393|S363|361b9d4d missing from Alpaca
  FLAG b392|S363|e5f64cc8 missing from Alpaca
  FLAG b379|S362|c12ca7e6 missing from Alpaca
  FLAG b378|S362|b910e593 missing from Alpaca
  FLAG b365|S361|4bd5eeb0 missing from Alpaca
  FLAG b364|S361|eec24531 missing from Alpaca
  FLAG b83|S210|113f3d4c missing from Alpaca
  FLAG b82|S210|f24ba9a9 missing from Alpaca
  FLAG b182|S217|898f369e missing from Alpaca
  FLAG b0|ORPHAN|c0a8c9e7 missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$993,200.96
  buying_power=$3,843,290.64 cash=$974,032.46
  open option orders: 14
    RBLX261002C00047500 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=0.01
    NKE261002C00040000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
    HOOD261002C00129000 OrderSide.SELL qty=2 status=OrderStatus.NEW limit=None
    DKNG261016C00023000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
    DKNG261016C00023500 OrderSide.SELL qty=2 status=OrderStatus.NEW limit=None
  open option positions: 25
    CVNA261002C00066000 qty=2 mkt=$92.00
    CVNA261002C00067000 qty=4 mkt=$108.00
    CVNA261002C00068000 qty=1 mkt=$18.00
    CVNA261002C00069000 qty=5 mkt=$30.00
    CVNA261002C00070000 qty=2 mkt=$12.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-29T09:35:08.753765-04:00 ===

[Run context]
Paper auth OK — equity $993192.96, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
2026-09-29 09:35:10,084 INFO   EXIT [b797|lab0797_s399_w3_1045_1120_r2|S399] stop_loss (-69.6%) SELL 1 DKNG261002C00022500 @<= 0.08
2026-09-29 09:35:11,660 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-58.3%) SELL 1 PLTR261002C00212500 @<= 0.06
2026-09-29 09:35:13,498 INFO   EXIT [b1151|lab1151_s164_w1_0928_1005_r2|S164] stop_loss (-57.1%) SELL 1 CVNA261002C00070000 @<= 0.07
2026-09-29 09:35:14,611 INFO   EXIT [b84|lab0084_s210_w3_1045_1120_r1|S210] stop_loss (-57.7%) SELL 1 MSFT260930C00525000 @<= 0.19
2026-09-29 09:35:15,033 INFO   EXIT [b164|lab0164_s216_w1_0928_1005_r1|S216] stop_loss (-77.8%) SELL 1 WFC261002C00083000 @<= 0.12
2026-09-29 09:35:16,331 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-46.5%) SELL 1 DKNG261016C00023500 @<= 0.24
2026-09-29 09:35:18,901 INFO   EXIT [b323|lab0323_s356_w2_1005_1045_r2|S356] stop_loss (-64.3%) SELL 1 DKNG261009C00022500 @<= 0.12
2026-09-29 09:35:19,485 INFO   EXIT [b294|lab0294_s352_w4_1120_1135_r1|S352] stop_loss (-53.8%) SELL 1 CVNA261002C00069000 @<= 0.07
2026-09-29 09:35:20,281 INFO   EXIT [b899|lab0899_s411_w1_0928_1005_r2|S411] stop_loss (-50.8%) SELL 1 PLTR261002C00202500 @<= 0.31
2026-09-29 09:35:20,971 INFO   EXIT [b835|lab0835_s406_w4_1120_1135_r2|S406] stop_loss (-53.8%) SELL 1 PLTR261002C00207500 @<= 0.13
Protective stops: placed=3 upgraded=0 already=17 failed=4 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
```

---

## Run 20260929T133711Z

- UTC timestamp: `20260929T133711Z`
- GitHub run: [#11302](https://github.com/28twagg-ops/TradingBot/actions/runs/36576157396)
- Run id: `36576157396`
- Live bot: exit=`0`, duration=`216s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260929T133711Z_live_bot.log`, `logs/action_runs/20260929T133711Z_live_options.log`, `logs/action_runs/20260929T133711Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1545 | 49.6 | -7.7 | +42.0 | $+19,545 |
| TAINTED | 1925 | 33.5 | -39.0 | +12.6 | $-9,424 |
| KEEP-only | 794 | 62.7 | +52.3 | +62.6 | $+13,455 |
| KEEP-only recent | 600 | 61.8 | +56.2 | +71.6 | $+9,417 |

- KEEP strategies (24): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (20): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-29T09:26:33.211793-04:00","date":"2026-09-29","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.4,"phases_s":{"reconcile":0.54},"signals":0,"placed":0,"equity":994607.48,"open_positions":30,"pending_orders":0,"open_lots":120,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11300","github_run_id":"36574927117","status":"ok","data_quality":{"clean":{"n":1545,"win":49.58,"med":-7.69,"avg":41.96,"pnl":19544.83},"tainted":{"n":1925,"win":33.45,"med":-38.98,"avg":12.59,"pnl":-9424.28},"keep_only":{"n":794,"win":62.72,"med":52.28,"avg":62.62,"pnl":13455.45},"keep_only_recent":{"n":600,"win":61.83,"med":56.2,"avg":71.58,"pnl":9417.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:37:13  INFO      Mode: morning_prep
13:37:15  INFO        [prep_positions] 2/2 (2 valid)
13:37:15  INFO      Fetching tickers (universe=both)...
13:37:15  INFO        S&P 500: 503
13:37:15  INFO        MidCap 400: 400
13:37:15  INFO        Total: 903 tickers
13:37:16  INFO        [prep_universe] 40/901 (40 valid)
13:37:19  INFO        [prep_universe] 80/901 (80 valid)
13:37:20  INFO        [prep_universe] 120/901 (120 valid)
13:37:21  INFO        [prep_universe] 160/901 (160 valid)
13:37:22  INFO        [prep_universe] 200/901 (199 valid)
13:37:29  INFO        [prep_universe] 240/901 (238 valid)
13:37:43  INFO        [prep_universe] 280/901 (278 valid)
13:37:53  INFO        [prep_universe] 320/901 (318 valid)
13:38:06  INFO        [prep_universe] 360/901 (358 valid)
13:38:16  INFO        [prep_universe] 400/901 (398 valid)
13:38:29  INFO        [prep_universe] 440/901 (438 valid)
13:38:40  INFO        [prep_universe] 480/901 (478 valid)
13:38:53  INFO        [prep_universe] 520/901 (518 valid)
13:39:06  INFO        [prep_universe] 560/901 (558 valid)
13:39:17  INFO        [prep_universe] 600/901 (598 valid)
13:39:30  INFO        [prep_universe] 640/901 (638 valid)
13:39:40  INFO        [prep_universe] 680/901 (678 valid)
13:39:53  INFO        [prep_universe] 720/901 (718 valid)
13:40:06  INFO        [prep_universe] 760/901 (758 valid)
13:40:17  INFO        [prep_universe] 800/901 (798 valid)
13:40:30  INFO        [prep_universe] 840/901 (838 valid)
13:40:40  INFO        [prep_universe] 880/901 (878 valid)
13:40:47  INFO        [prep_universe] 901/901 (899 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:37 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.58|
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
|  Invested                                                        $67.01|
|  Open P&L                                                        $-0.07|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AYI      MomReversal     $33.67     $305.46  $306.68  +0.4%   $+0.13  |
|  NNN      MomReversal     $33.34     $41.40   $41.15   -0.6%   $-0.20  |
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
|  Universe scanned                                                   901|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-29T09:40:49.331314-04:00 share=25% ===
2026-09-29 09:40:49,331 INFO === options_live_micro LIVE 2026-09-29T09:40:49.331314-04:00 share=25% ===
Live account equity $223.70 cash $156.57 #225458845 options_level=3
2026-09-29 09:40:49,583 INFO Live account equity $223.70 cash $156.57 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-29 09:40:49,810 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-29 09:40:49,960 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=120 paper_keys=yes dry_run=False
  alpaca positions=25
  FLAG b263|S403|3eabcde9 missing from Alpaca
  FLAG b265|S403|b80b4c98 missing from Alpaca
  FLAG b377|S362|cf588856 missing from Alpaca
  FLAG b376|S362|23f383f2 missing from Alpaca
  FLAG b363|S361|0128b299 missing from Alpaca
  FLAG b362|S361|7043c90d missing from Alpaca
  FLAG b235|S401|aab77879 missing from Alpaca
  FLAG b234|S401|ef2f7f9c missing from Alpaca
  FLAG b1124|S168|14fcadae missing from Alpaca
  FLAG b1153|S164|81436fe9 missing from Alpaca
  FLAG b1152|S164|9551cc23 missing from Alpaca
  FLAG b1055|S165|ba282ae4 missing from Alpaca
  FLAG b1054|S165|9ee25db6 missing from Alpaca
  FLAG b915|S412|1292c040 missing from Alpaca
  FLAG b914|S412|e8596fd6 missing from Alpaca
  FLAG b393|S363|361b9d4d missing from Alpaca
  FLAG b392|S363|e5f64cc8 missing from Alpaca
  FLAG b379|S362|c12ca7e6 missing from Alpaca
  FLAG b378|S362|b910e593 missing from Alpaca
  FLAG b365|S361|4bd5eeb0 missing from Alpaca
  FLAG b364|S361|eec24531 missing from Alpaca
  FLAG b83|S210|113f3d4c missing from Alpaca
  FLAG b82|S210|f24ba9a9 missing from Alpaca
  FLAG b84|S210|0fa4f5bf missing from Alpaca
  FLAG b182|S217|898f369e missing from Alpaca
  FLAG b863|S408|34be010b missing from Alpaca
  FLAG b835|S406|500bf099 missing from Alpaca
  FLAG b0|ORPHAN|d8483095 missing from Alpaca
  FLAG b0|ORPHAN|2a6c4c35 missing from Alpaca
  FLAG b0|ORPHAN|c0a8c9e7 missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$993,035.70
  buying_power=$3,841,482.80 cash=$974,260.20
  open option orders: 15
    CVNA261002C00066000 OrderSide.SELL qty=2 status=OrderStatus.NEW limit=None
    CVNA261002C00068000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
    DKNG261016C00023500 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=0.24
    CVNA261002C00070000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=0.07
    RBLX261002C00047500 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=0.01
  open option positions: 21
    CVNA261002C00066000 qty=2 mkt=$120.00
    CVNA261002C00068000 qty=1 mkt=$24.00
    CVNA261002C00069000 qty=4 mkt=$56.00
    CVNA261002C00070000 qty=2 mkt=$12.00
    DKNG261002C00021000 qty=4 mkt=$176.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-29T09:40:53.120678-04:00 ===

[Run context]
Paper auth OK — equity $993055.65, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
2026-09-29 09:40:55,449 INFO   EXIT [b796|lab0796_s399_w3_1045_1120_r1|S399] stop_loss (-69.6%) SELL 1 DKNG261002C00022500 @<= 0.08
2026-09-29 09:40:56,270 INFO   EXIT [b167|lab0167_s216_w2_1005_1045_r2|S216] stop_loss (-76.3%) SELL 1 WFC261002C00083000 @<= 0.13
2026-09-29 09:40:56,892 INFO   EXIT [b898|lab0898_s411_w1_0928_1005_r1|S411] stop_loss (-60.7%) SELL 1 PLTR261002C00202500 @<= 0.21
2026-09-29 09:41:00,624 INFO   EXIT [b322|lab0322_s356_w2_1005_1045_r1|S356] stop_loss (-64.3%) SELL 1 DKNG261009C00022500 @<= 0.12
2026-09-29 09:41:01,091 INFO   EXIT [b803|lab0803_s404_w2_1005_1045_r2|S404] stop_loss (-50.3%) SELL 1 DKNG261002C00021500 @<= 0.28
Protective stops: placed=2 upgraded=0 already=15 failed=3 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
```

---

## Run 20260929T134244Z

- UTC timestamp: `20260929T134244Z`
- GitHub run: [#11303](https://github.com/28twagg-ops/TradingBot/actions/runs/36576777585)
- Run id: `36576777585`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260929T134244Z_live_bot.log`, `logs/action_runs/20260929T134244Z_live_options.log`, `logs/action_runs/20260929T134244Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1545 | 49.6 | -7.7 | +42.0 | $+19,545 |
| TAINTED | 1925 | 33.5 | -39.0 | +12.6 | $-9,424 |
| KEEP-only | 794 | 62.7 | +52.3 | +62.6 | $+13,455 |
| KEEP-only recent | 600 | 61.8 | +56.2 | +71.6 | $+9,417 |

- KEEP strategies (24): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (20): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-29T09:26:33.211793-04:00","date":"2026-09-29","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.4,"phases_s":{"reconcile":0.54},"signals":0,"placed":0,"equity":994607.48,"open_positions":30,"pending_orders":0,"open_lots":120,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11300","github_run_id":"36574927117","status":"ok","data_quality":{"clean":{"n":1545,"win":49.58,"med":-7.69,"avg":41.96,"pnl":19544.83},"tainted":{"n":1925,"win":33.45,"med":-38.98,"avg":12.59,"pnl":-9424.28},"keep_only":{"n":794,"win":62.72,"med":52.28,"avg":62.62,"pnl":13455.45},"keep_only_recent":{"n":600,"win":61.83,"med":56.2,"avg":71.58,"pnl":9417.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:42:45  INFO      Mode: morning_prep
13:42:46  INFO        [prep_positions] 2/2 (2 valid)
13:42:46  INFO        Universe cache hit: 903 tickers (tickers_2026-09-29.json)
13:42:47  INFO        [prep_universe] 40/901 (40 valid)
13:42:50  INFO        [prep_universe] 80/901 (80 valid)
13:42:51  INFO        [prep_universe] 120/901 (120 valid)
13:42:52  INFO        [prep_universe] 160/901 (160 valid)
13:42:53  INFO        [prep_universe] 200/901 (199 valid)
13:43:01  INFO        [prep_universe] 240/901 (238 valid)
13:43:11  INFO        [prep_universe] 280/901 (278 valid)
13:43:24  INFO        [prep_universe] 320/901 (318 valid)
13:43:37  INFO        [prep_universe] 360/901 (358 valid)
13:43:47  INFO        [prep_universe] 400/901 (398 valid)
13:44:01  INFO        [prep_universe] 440/901 (438 valid)
13:44:14  INFO        [prep_universe] 480/901 (478 valid)
13:44:24  INFO        [prep_universe] 520/901 (518 valid)
13:44:37  INFO        [prep_universe] 560/901 (558 valid)
13:44:47  INFO        [prep_universe] 600/901 (598 valid)
13:45:00  INFO        [prep_universe] 640/901 (638 valid)
13:45:11  INFO        [prep_universe] 680/901 (678 valid)
13:45:24  INFO        [prep_universe] 720/901 (718 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20260929T134708Z

- UTC timestamp: `20260929T134708Z`
- GitHub run: [#11304](https://github.com/28twagg-ops/TradingBot/actions/runs/36577408191)
- Run id: `36577408191`
- Live bot: exit=`0`, duration=`229s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260929T134708Z_live_bot.log`, `logs/action_runs/20260929T134708Z_live_options.log`, `logs/action_runs/20260929T134708Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1545 | 49.6 | -7.7 | +42.0 | $+19,545 |
| TAINTED | 1925 | 33.5 | -39.0 | +12.6 | $-9,424 |
| KEEP-only | 794 | 62.7 | +52.3 | +62.6 | $+13,455 |
| KEEP-only recent | 600 | 61.8 | +56.2 | +71.6 | $+9,417 |

- KEEP strategies (24): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (20): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-29T09:26:33.211793-04:00","date":"2026-09-29","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.4,"phases_s":{"reconcile":0.54},"signals":0,"placed":0,"equity":994607.48,"open_positions":30,"pending_orders":0,"open_lots":120,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11300","github_run_id":"36574927117","status":"ok","data_quality":{"clean":{"n":1545,"win":49.58,"med":-7.69,"avg":41.96,"pnl":19544.83},"tainted":{"n":1925,"win":33.45,"med":-38.98,"avg":12.59,"pnl":-9424.28},"keep_only":{"n":794,"win":62.72,"med":52.28,"avg":62.62,"pnl":13455.45},"keep_only_recent":{"n":600,"win":61.83,"med":56.2,"avg":71.58,"pnl":9417.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
... (157 earlier lines - see full log file)
|  QLYS     Pullback50      eq     $171.47  50.7   -2.07   50MA bounce (+|
|  REXR     Pullback50      eq     $37.37   53.4   -2.37   50MA bounce (-|
|  SEIC     Pullback50      eq     $104.86  36.9   -1.21   50MA bounce (-|
|  THC      Pullback50      eq     $258.22  38.2   -1.28   50MA bounce (+|
|  WTS      Pullback50      eq     $358.76  53.5   -1.67   50MA bounce (-|
|                                                                        |
+========================================================================+

+========================================================================+
|                              ENTRY ORDERS                              |
+========================================================================+
|    ENTER [eq] AES  Pullback50                                    $33.58|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    SKIP [eq] MO  Pullback50                                       cap 3|
|    SKIP [eq] TECH  Pullback50                                     cap 3|
|    SKIP [eq] BRK-B  Pullback50                                    cap 3|
|    SKIP [eq] CAT  Pullback50                                      cap 3|
|    SKIP [eq] CTAS  Pullback50                                     cap 3|
|    SKIP [eq] KO  Pullback50                                       cap 3|
|    SKIP [eq] DVN  Pullback50                                      cap 3|
|    SKIP [eq] EME  Pullback50                                      cap 3|
|    SKIP [eq] ECL  Pullback50                                      cap 3|
|    SKIP [eq] XOM  Pullback50                                      cap 3|
|    SKIP [eq] GEV  Pullback50                                      cap 3|
|    SKIP [eq] INCY  Pullback50                                     cap 3|
|    SKIP [eq] KDP  Pullback50                                      cap 3|
|    SKIP [eq] MA  Pullback50                                       cap 3|
|    SKIP [eq] MET  Pullback50                                      cap 3|
|    SKIP [eq] PFG  Pullback50                                      cap 3|
|    SKIP [eq] DGX  Pullback50                                      cap 3|
|    SKIP [eq] VLTO  Pullback50                                     cap 3|
|    SKIP [eq] V  Pullback50                                        cap 3|
|    SKIP [eq] WAB  Pullback50                                      cap 3|
|    SKIP [eq] AIT  Pullback50                                      cap 3|
|    SKIP [eq] CLH  Pullback50                                      cap 3|
|    SKIP [eq] CR  Pullback50                                       cap 3|
|    SKIP [eq] EGP  Pullback50                                      cap 3|
|    SKIP [eq] HIMS  Pullback50                                     cap 3|
|    SKIP [eq] ITT  Pullback50                                      cap 3|
|    SKIP [eq] LECO  Pullback50                                     cap 3|
|    SKIP [eq] MANH  Pullback50                                     cap 3|
|    SKIP [eq] MSA  Pullback50                                      cap 3|
|    SKIP [eq] MOG-A  Pullback50                                    cap 3|
|    SKIP [eq] MSM  Pullback50                                      cap 3|
|    SKIP [eq] QLYS  Pullback50                                     cap 3|
|    SKIP [eq] REXR  Pullback50                                     cap 3|
|    SKIP [eq] SEIC  Pullback50                                     cap 3|
|    SKIP [eq] THC  Pullback50                                      cap 3|
|    SKIP [eq] WTS  Pullback50                                      cap 3|

+========================================================================+
|                         BUY FILL CONFIRMATION                          |
+========================================================================+
|  Pending submits                                                      1|
+------------------------------------------------------------------------+
|  AES                                                  still unconfirmed|
+========================================================================+
+========================================================================+

+========================================================================+
|                           GTC STOP PLACEMENT                           |
+========================================================================+
|  Waiting 5s for 1 buy submit(s) to settle...                           |
+========================================================================+

+========================================================================+
|                            SESSION SUMMARY                             |
+========================================================================+
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Strategy  GapDown + VolumeSpike (display only — schedule not enforced)|
|  Scanned                                                            899|
|  Signals                                                             37|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  1 unconfirmed|
|  Exits                                                                0|
|  Open pos                                                             3|
|  Equity                                                         $223.77|
|  Cash                                                           $122.99|
+========================================================================+
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20260929T135232Z

- UTC timestamp: `20260929T135232Z`
- GitHub run: [#11305](https://github.com/28twagg-ops/TradingBot/actions/runs/36578037142)
- Run id: `36578037142`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260929T135232Z_live_bot.log`, `logs/action_runs/20260929T135232Z_live_options.log`, `logs/action_runs/20260929T135232Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1545 | 49.6 | -7.7 | +42.0 | $+19,545 |
| TAINTED | 1925 | 33.5 | -39.0 | +12.6 | $-9,424 |
| KEEP-only | 794 | 62.7 | +52.3 | +62.6 | $+13,455 |
| KEEP-only recent | 600 | 61.8 | +56.2 | +71.6 | $+9,417 |

- KEEP strategies (24): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (20): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-29T09:26:33.211793-04:00","date":"2026-09-29","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.4,"phases_s":{"reconcile":0.54},"signals":0,"placed":0,"equity":994607.48,"open_positions":30,"pending_orders":0,"open_lots":120,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11300","github_run_id":"36574927117","status":"ok","data_quality":{"clean":{"n":1545,"win":49.58,"med":-7.69,"avg":41.96,"pnl":19544.83},"tainted":{"n":1925,"win":33.45,"med":-38.98,"avg":12.59,"pnl":-9424.28},"keep_only":{"n":794,"win":62.72,"med":52.28,"avg":62.62,"pnl":13455.45},"keep_only_recent":{"n":600,"win":61.83,"med":56.2,"avg":71.58,"pnl":9417.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:52:33  INFO      Mode: morning_scan
13:52:34  INFO        [positions] 3/3 (3 valid)
13:52:34  INFO        SELL order cancelled AES  type=OrderType.STOP  id=ecfb107e-4d6d-43e3-80f5-219b4e122f6a
13:52:34  INFO        SELL LIMIT AES  qty=2.253255645  limit=$14.89  id=bb22b6c0-725d-4b80-b506-4efbbe95eac3
13:53:04  INFO        SELL LIMIT filled AES (confirmed by position check)
13:53:04  INFO        TX logged: SELL AES  P&L -0.05%
13:53:04  INFO        Universe cache hit: 903 tickers (tickers_2026-09-29.json)
13:53:05  INFO        [universe] 40/901 (40 valid)
13:53:06  INFO        [universe] 80/901 (80 valid)
13:53:07  INFO        [universe] 120/901 (120 valid)
13:53:09  INFO        [universe] 160/901 (160 valid)
13:53:10  INFO        [universe] 200/901 (199 valid)
13:53:17  INFO        [universe] 240/901 (238 valid)
13:53:30  INFO        [universe] 280/901 (278 valid)
13:53:43  INFO        [universe] 320/901 (318 valid)
13:53:53  INFO        [universe] 360/901 (358 valid)
13:54:06  INFO        [universe] 400/901 (398 valid)
13:54:19  INFO        [universe] 440/901 (438 valid)
13:54:29  INFO        [universe] 480/901 (478 valid)
13:54:42  INFO        [universe] 520/901 (518 valid)
13:54:52  INFO        [universe] 560/901 (558 valid)
13:55:05  INFO        [universe] 600/901 (598 valid)
13:55:18  INFO        [universe] 640/901 (638 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20260929T135654Z

- UTC timestamp: `20260929T135654Z`
- GitHub run: [#11306](https://github.com/28twagg-ops/TradingBot/actions/runs/36578677424)
- Run id: `36578677424`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`77s`
- Full logs: `logs/action_runs/20260929T135654Z_live_bot.log`, `logs/action_runs/20260929T135654Z_live_options.log`, `logs/action_runs/20260929T135654Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1549 | 49.5 | -7.7 | +41.7 | $+19,408 |
| TAINTED | 1940 | 33.2 | -39.8 | +12.0 | $-9,827 |
| KEEP-only | 796 | 62.6 | +52.1 | +62.4 | $+13,416 |
| KEEP-only recent | 602 | 61.6 | +55.9 | +71.2 | $+9,378 |

- KEEP strategies (24): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (20): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-29T09:56:59.677624-04:00","date":"2026-09-29","mode":"entry+manage","header":"entry+manage (20 new)","elapsed_s":64.3,"phases_s":{"reconcile":0.4,"cancel":0.08,"manage":3.87,"protective_stops":0.77,"scan":45.31,"entries":8.17,"reconcile2":1.02},"signals":180,"placed":20,"equity":992935.91,"open_positions":19,"pending_orders":2,"open_lots":82,"submitted_today":20,"filled_today":18,"unattributed_contracts":0,"top_signals":["S401:CRWD","S216:UBER","S216:CVNA","S216:UPST","S217:BILL","S218:BILL","S217:MCD","S218:MCD"],"github_run":"11306","github_run_id":"36578677424","status":"ok","data_quality":{"clean":{"n":1549,"win":49.45,"med":-7.69,"avg":41.71,"pnl":19407.83},"tainted":{"n":1940,"win":33.2,"med":-39.77,"avg":12.0,"pnl":-9827.28},"keep_only":{"n":796,"win":62.56,"med":52.09,"avg":62.36,"pnl":13416.45},"keep_only_recent":{"n":602,"win":61.63,"med":55.94,"avg":71.21,"pnl":9378.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:56:55  INFO      Mode: morning_scan
13:56:55  INFO      Morning scan already completed today (2026-09-29T13:50:57.032894Z) — exits-only pass
13:56:55  INFO        place_all_stops: checking 2 positions...
13:56:55  INFO        STOP skipped AYI: fractional (0.1098 shares) — software exit will handle it
13:56:55  INFO        STOP skipped NNN: fractional (0.8102 shares) — software exit will handle it
13:56:55  INFO        [positions] 2/2 (2 valid)
13:56:55  INFO        Daily log -> logs/daily/2026-09-29.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_SCAN|
|  Time                                                         13:56 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.77|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  NNN  P&L +0.0%  $+0.01                                            HOLD|
|  AYI  P&L +0.5%  $+0.16                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                2|
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
=== options_live_micro LIVE 2026-09-29T09:56:56.335602-04:00 share=25% ===
2026-09-29 09:56:56,335 INFO === options_live_micro LIVE 2026-09-29T09:56:56.335602-04:00 share=25% ===
Live account equity $223.78 cash $156.53 #225458845 options_level=3
2026-09-29 09:56:56,592 INFO Live account equity $223.78 cash $156.53 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-29 09:56:56,653 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-29 09:56:56,694 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (214 earlier lines - see full log file)
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
## Ledger health — 2026-09-29
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1619 | WARN | <<<
| Missing exit records (post) |  1619 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    82 | INFO |
| Total closed lots           |  2603 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1549 med=-7.7% | TAINTED n=1940 med=-39.8% | KEEP-only n=796 med=+52.1% | KILL=20 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.77 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260929T140114Z

- UTC timestamp: `20260929T140114Z`
- GitHub run: [#11307](https://github.com/28twagg-ops/TradingBot/actions/runs/36579318535)
- Run id: `36579318535`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`48s`
- Full logs: `logs/action_runs/20260929T140114Z_live_bot.log`, `logs/action_runs/20260929T140114Z_live_options.log`, `logs/action_runs/20260929T140114Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1550 | 49.5 | -7.7 | +41.7 | $+19,443 |
| TAINTED | 1940 | 33.2 | -39.8 | +12.0 | $-9,827 |
| KEEP-only | 796 | 62.6 | +52.1 | +62.4 | $+13,416 |
| KEEP-only recent | 602 | 61.6 | +55.9 | +71.2 | $+9,378 |

- KEEP strategies (24): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (20): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-29T10:01:20.341454-04:00","date":"2026-09-29","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":40.5,"phases_s":{"reconcile":0.4,"cancel":0.1,"manage":6.07,"protective_stops":1.54,"scan":22.5,"entries":9.41},"signals":180,"placed":0,"equity":992667.75,"open_positions":19,"pending_orders":0,"open_lots":83,"submitted_today":20,"filled_today":20,"unattributed_contracts":0,"top_signals":["S401:CRWD","S216:UBER","S216:CVNA","S216:UPST","S217:BILL","S218:BILL","S217:MCD","S218:MCD"],"github_run":"11307","github_run_id":"36579318535","status":"ok","data_quality":{"clean":{"n":1550,"win":49.48,"med":-7.69,"avg":41.73,"pnl":19442.83},"tainted":{"n":1940,"win":33.2,"med":-39.77,"avg":12.0,"pnl":-9827.28},"keep_only":{"n":796,"win":62.56,"med":52.09,"avg":62.36,"pnl":13416.45},"keep_only_recent":{"n":602,"win":61.63,"med":55.94,"avg":71.21,"pnl":9378.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:01:16  INFO      Mode: exits
14:01:16  INFO        Daily log -> logs/daily/2026-09-29.md
14:01:16  INFO        Daily log reconciled -> logs/daily/2026-09-29.md (1 ledger rows)
14:01:16  INFO        place_all_stops: checking 2 positions...
14:01:16  INFO        STOP skipped AYI: fractional (0.1098 shares) — software exit will handle it
14:01:16  INFO        STOP skipped NNN: fractional (0.8102 shares) — software exit will handle it
14:01:17  INFO        [positions] 2/2 (2 valid)
14:01:17  INFO        Daily log -> logs/daily/2026-09-29.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.50|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AYI  P&L -0.4%  $-0.12                                            HOLD|
|  NNN  P&L +0.0%  $+0.01                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                2|
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
=== options_live_micro LIVE 2026-09-29T10:01:18.058259-04:00 share=25% ===
2026-09-29 10:01:18,058 INFO === options_live_micro LIVE 2026-09-29T10:01:18.058259-04:00 share=25% ===
Live account equity $223.51 cash $156.53 #225458845 options_level=3
2026-09-29 10:01:18,214 INFO Live account equity $223.51 cash $156.53 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-29 10:01:18,343 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-29 10:01:18,427 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (194 earlier lines - see full log file)
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
## Ledger health — 2026-09-29
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1619 | WARN | <<<
| Missing exit records (post) |  1619 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    83 | INFO |
| Total closed lots           |  2604 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1550 med=-7.7% | TAINTED n=1940 med=-39.8% | KEEP-only n=796 med=+52.1% | KILL=20 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.51 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260929T140619Z

- UTC timestamp: `20260929T140619Z`
- GitHub run: [#11308](https://github.com/28twagg-ops/TradingBot/actions/runs/36579964670)
- Run id: `36579964670`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`114s`
- Full logs: `logs/action_runs/20260929T140619Z_live_bot.log`, `logs/action_runs/20260929T140619Z_live_options.log`, `logs/action_runs/20260929T140619Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1552 | 49.5 | -7.7 | +41.7 | $+19,440 |
| TAINTED | 1940 | 33.2 | -39.8 | +12.0 | $-9,827 |
| KEEP-only | 797 | 62.5 | +52.0 | +62.2 | $+13,394 |
| KEEP-only recent | 603 | 61.5 | +55.9 | +71.0 | $+9,356 |

- KEEP strategies (24): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (20): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-29T10:06:26.967983-04:00","date":"2026-09-29","mode":"entry+manage","header":"entry+manage (14 new)","elapsed_s":102.0,"phases_s":{"reconcile":0.14,"cancel":0.02,"manage":2.25,"protective_stops":0.33,"scan":54.9,"entries":34.15,"reconcile2":0.16},"signals":180,"placed":14,"equity":993049.5,"open_positions":19,"pending_orders":14,"open_lots":80,"submitted_today":34,"filled_today":20,"unattributed_contracts":0,"top_signals":["S401:CRWD","S216:UBER","S216:CVNA","S216:UPST","S217:BILL","S218:BILL","S217:MCD","S218:MCD"],"github_run":"11308","github_run_id":"36579964670","status":"ok","data_quality":{"clean":{"n":1552,"win":49.48,"med":-7.69,"avg":41.74,"pnl":19439.83},"tainted":{"n":1940,"win":33.2,"med":-39.77,"avg":12.0,"pnl":-9827.28},"keep_only":{"n":797,"win":62.48,"med":52.0,"avg":62.22,"pnl":13394.45},"keep_only_recent":{"n":603,"win":61.53,"med":55.88,"avg":71.01,"pnl":9356.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:06:20  INFO      Mode: exits
14:06:20  INFO        Daily log -> logs/daily/2026-09-29.md
14:06:20  INFO        Daily log reconciled -> logs/daily/2026-09-29.md (1 ledger rows)
14:06:20  INFO        place_all_stops: checking 2 positions...
14:06:20  INFO        STOP skipped AYI: fractional (0.1098 shares) — software exit will handle it
14:06:20  INFO        STOP skipped NNN: fractional (0.8102 shares) — software exit will handle it
14:06:21  INFO        [positions] 2/2 (2 valid)
14:06:21  INFO        SELL MARKET [urgent] AYI closed
14:06:23  INFO        TX logged: SELL AYI  P&L -0.5%
14:06:23  INFO        Daily log -> logs/daily/2026-09-29.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.44|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AYI  P&L -0.5%  $-0.17                         EXIT: stop_loss (-0.5%)|
|  NNN  P&L -0.0%  $-0.00                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  1 attempted  |  1 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
|  AYI                                         -0.50%  (threshold -0.50%)|
|  Count                                                                1|
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-29T10:06:24.007048-04:00 share=25% ===
2026-09-29 10:06:24,007 INFO === options_live_micro LIVE 2026-09-29T10:06:24.007048-04:00 share=25% ===
Live account equity $223.39 cash $189.85 #225458845 options_level=3
2026-09-29 10:06:24,177 INFO Live account equity $223.39 cash $189.85 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-29 10:06:24,202 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-29 10:06:24,217 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (213 earlier lines - see full log file)
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
## Ledger health — 2026-09-29
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1619 | WARN | <<<
| Missing exit records (post) |  1619 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    80 | INFO |
| Total closed lots           |  2606 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1552 med=-7.7% | TAINTED n=1940 med=-39.8% | KEEP-only n=797 med=+52.0% | KILL=20 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.39 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260929T141122Z

- UTC timestamp: `20260929T141122Z`
- GitHub run: [#11309](https://github.com/28twagg-ops/TradingBot/actions/runs/36580603767)
- Run id: `36580603767`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`103s`
- Full logs: `logs/action_runs/20260929T141122Z_live_bot.log`, `logs/action_runs/20260929T141122Z_live_options.log`, `logs/action_runs/20260929T141122Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1554 | 49.5 | -7.7 | +41.8 | $+19,476 |
| TAINTED | 1940 | 33.2 | -39.8 | +12.0 | $-9,827 |
| KEEP-only | 798 | 62.5 | +52.1 | +62.2 | $+13,412 |
| KEEP-only recent | 604 | 61.6 | +55.9 | +71.0 | $+9,374 |

- KEEP strategies (24): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (20): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-29T10:11:29.767236-04:00","date":"2026-09-29","mode":"entry+manage","header":"entry+manage (2 new)","elapsed_s":89.8,"phases_s":{"reconcile":0.52,"cancel":0.16,"manage":6.19,"protective_stops":2.33,"scan":52.85,"entries":24.26,"reconcile2":0.59},"signals":180,"placed":2,"equity":993229.1,"open_positions":18,"pending_orders":16,"open_lots":78,"submitted_today":36,"filled_today":20,"unattributed_contracts":0,"top_signals":["S401:CRWD","S216:UBER","S216:CVNA","S216:UPST","S217:BILL","S218:BILL","S217:MCD","S218:MCD"],"github_run":"11309","github_run_id":"36580603767","status":"ok","data_quality":{"clean":{"n":1554,"win":49.55,"med":-7.69,"avg":41.82,"pnl":19475.83},"tainted":{"n":1940,"win":33.2,"med":-39.77,"avg":12.0,"pnl":-9827.28},"keep_only":{"n":798,"win":62.53,"med":52.09,"avg":62.23,"pnl":13412.45},"keep_only_recent":{"n":604,"win":61.59,"med":55.94,"avg":71.01,"pnl":9374.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:11:23  INFO      Mode: exits
14:11:24  INFO        Daily log -> logs/daily/2026-09-29.md
14:11:24  INFO        Daily log reconciled -> logs/daily/2026-09-29.md (2 ledger rows)
14:11:24  INFO        place_all_stops: checking 1 positions...
14:11:24  INFO        STOP skipped NNN: fractional (0.8102 shares) — software exit will handle it
14:11:24  INFO        [positions] 1/1 (1 valid)
14:11:24  INFO        Daily log -> logs/daily/2026-09-29.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.40|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  NNN  P&L +0.0%  $+0.01                                            HOLD|
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
=== options_live_micro LIVE 2026-09-29T10:11:25.602239-04:00 share=25% ===
2026-09-29 10:11:25,602 INFO === options_live_micro LIVE 2026-09-29T10:11:25.602239-04:00 share=25% ===
Live account equity $223.40 cash $189.85 #225458845 options_level=3
2026-09-29 10:11:25,835 INFO Live account equity $223.40 cash $189.85 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-29 10:11:26,045 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-29 10:11:26,184 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (207 earlier lines - see full log file)
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
## Ledger health — 2026-09-29
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1619 | WARN | <<<
| Missing exit records (post) |  1619 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    78 | INFO |
| Total closed lots           |  2608 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1554 med=-7.7% | TAINTED n=1940 med=-39.8% | KEEP-only n=798 med=+52.1% | KILL=20 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.4 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260929T141610Z

- UTC timestamp: `20260929T141610Z`
- GitHub run: [#11310](https://github.com/28twagg-ops/TradingBot/actions/runs/36581242397)
- Run id: `36581242397`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`61s`
- Full logs: `logs/action_runs/20260929T141610Z_live_bot.log`, `logs/action_runs/20260929T141610Z_live_options.log`, `logs/action_runs/20260929T141610Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1555 | 49.6 | -7.7 | +41.8 | $+19,488 |
| TAINTED | 1940 | 33.2 | -39.8 | +12.0 | $-9,827 |
| KEEP-only | 799 | 62.6 | +52.2 | +62.3 | $+13,424 |
| KEEP-only recent | 605 | 61.7 | +56.0 | +71.0 | $+9,386 |

- KEEP strategies (24): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (20): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-29T10:16:16.264374-04:00","date":"2026-09-29","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":51.6,"phases_s":{"reconcile":0.47,"cancel":0.16,"manage":4.07,"protective_stops":1.18,"scan":29.27,"entries":14.08,"reconcile2":0.37},"signals":180,"placed":0,"equity":993403.34,"open_positions":17,"pending_orders":16,"open_lots":77,"submitted_today":36,"filled_today":20,"unattributed_contracts":0,"top_signals":["S401:CRWD","S216:UBER","S216:CVNA","S216:UPST","S217:BILL","S218:BILL","S217:MCD","S218:MCD"],"github_run":"11310","github_run_id":"36581242397","status":"ok","data_quality":{"clean":{"n":1555,"win":49.58,"med":-7.69,"avg":41.84,"pnl":19487.83},"tainted":{"n":1940,"win":33.2,"med":-39.77,"avg":12.0,"pnl":-9827.28},"keep_only":{"n":799,"win":62.58,"med":52.17,"avg":62.26,"pnl":13424.45},"keep_only_recent":{"n":605,"win":61.65,"med":56.0,"avg":71.03,"pnl":9386.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:16:11  INFO      Mode: exits
14:16:12  INFO        Daily log -> logs/daily/2026-09-29.md
14:16:12  INFO        Daily log reconciled -> logs/daily/2026-09-29.md (2 ledger rows)
14:16:12  INFO        place_all_stops: checking 1 positions...
14:16:12  INFO        STOP skipped NNN: fractional (0.8102 shares) — software exit will handle it
14:16:12  INFO        [positions] 1/1 (1 valid)
14:16:12  INFO        Daily log -> logs/daily/2026-09-29.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.43|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  NNN  P&L +0.1%  $+0.04                                            HOLD|
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
=== options_live_micro LIVE 2026-09-29T10:16:13.209510-04:00 share=25% ===
2026-09-29 10:16:13,209 INFO === options_live_micro LIVE 2026-09-29T10:16:13.209510-04:00 share=25% ===
Live account equity $223.43 cash $189.85 #225458845 options_level=3
2026-09-29 10:16:13,516 INFO Live account equity $223.43 cash $189.85 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-29 10:16:13,612 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-29 10:16:13,676 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (208 earlier lines - see full log file)
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
## Ledger health — 2026-09-29
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1619 | WARN | <<<
| Missing exit records (post) |  1619 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    77 | INFO |
| Total closed lots           |  2609 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1555 med=-7.7% | TAINTED n=1940 med=-39.8% | KEEP-only n=799 med=+52.2% | KILL=20 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.43 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260929T142119Z

- UTC timestamp: `20260929T142119Z`
- GitHub run: [#11311](https://github.com/28twagg-ops/TradingBot/actions/runs/36581877442)
- Run id: `36581877442`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`84s`
- Full logs: `logs/action_runs/20260929T142119Z_live_bot.log`, `logs/action_runs/20260929T142119Z_live_options.log`, `logs/action_runs/20260929T142119Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1556 | 49.6 | -7.7 | +41.8 | $+19,469 |
| TAINTED | 1940 | 33.2 | -39.8 | +12.0 | $-9,827 |
| KEEP-only | 800 | 62.5 | +52.1 | +62.1 | $+13,405 |
| KEEP-only recent | 606 | 61.6 | +55.9 | +70.8 | $+9,367 |

- KEEP strategies (24): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (20): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-29T10:21:24.470584-04:00","date":"2026-09-29","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":72.3,"phases_s":{"reconcile":0.56,"cancel":0.03,"manage":2.43,"protective_stops":0.52,"scan":53.82,"entries":4.82,"reconcile2":0.13},"signals":180,"placed":0,"equity":993448.31,"open_positions":18,"pending_orders":6,"open_lots":86,"submitted_today":36,"filled_today":30,"unattributed_contracts":0,"top_signals":["S401:CRWD","S216:UBER","S216:CVNA","S216:UPST","S217:BILL","S218:BILL","S217:MCD","S218:MCD"],"github_run":"11311","github_run_id":"36581877442","status":"ok","data_quality":{"clean":{"n":1556,"win":49.55,"med":-7.69,"avg":41.79,"pnl":19468.83},"tainted":{"n":1940,"win":33.2,"med":-39.77,"avg":12.0,"pnl":-9827.28},"keep_only":{"n":800,"win":62.5,"med":52.09,"avg":62.13,"pnl":13405.45},"keep_only_recent":{"n":606,"win":61.55,"med":55.94,"avg":70.85,"pnl":9367.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:21:20  INFO      Mode: exits
14:21:20  INFO        Daily log -> logs/daily/2026-09-29.md
14:21:20  INFO        Daily log reconciled -> logs/daily/2026-09-29.md (2 ledger rows)
14:21:20  INFO        place_all_stops: checking 1 positions...
14:21:20  INFO        STOP skipped NNN: fractional (0.8102 shares) — software exit will handle it
14:21:20  INFO        [positions] 1/1 (1 valid)
14:21:21  INFO        Daily log -> logs/daily/2026-09-29.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.42|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  NNN  P&L +0.1%  $+0.03                                            HOLD|
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
=== options_live_micro LIVE 2026-09-29T10:21:21.815847-04:00 share=25% ===
2026-09-29 10:21:21,815 INFO === options_live_micro LIVE 2026-09-29T10:21:21.815847-04:00 share=25% ===
Live account equity $223.42 cash $189.85 #225458845 options_level=3
2026-09-29 10:21:21,865 INFO Live account equity $223.42 cash $189.85 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-29 10:21:21,889 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-29 10:21:21,903 INFO Live micro done. open_options=0 lots=0
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
## Ledger health — 2026-09-29
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1619 | WARN | <<<
| Missing exit records (post) |  1619 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    86 | INFO |
| Total closed lots           |  2610 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1556 med=-7.7% | TAINTED n=1940 med=-39.8% | KEEP-only n=800 med=+52.1% | KILL=20 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.42 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260929T142651Z

- UTC timestamp: `20260929T142651Z`
- GitHub run: [#11312](https://github.com/28twagg-ops/TradingBot/actions/runs/36582505877)
- Run id: `36582505877`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`82s`
- Full logs: `logs/action_runs/20260929T142651Z_live_bot.log`, `logs/action_runs/20260929T142651Z_live_options.log`, `logs/action_runs/20260929T142651Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1557 | 49.5 | -7.7 | +41.7 | $+19,437 |
| TAINTED | 1941 | 33.2 | -39.5 | +12.5 | $-9,775 |
| KEEP-only | 801 | 62.4 | +52.0 | +62.0 | $+13,373 |
| KEEP-only recent | 607 | 61.4 | +55.9 | +70.6 | $+9,335 |

- KEEP strategies (24): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (20): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-29T10:26:56.858159-04:00","date":"2026-09-29","mode":"entry+manage","header":"entry+manage (4 new)","elapsed_s":70.6,"phases_s":{"reconcile":0.09,"cancel":0.02,"manage":2.16,"protective_stops":0.33,"scan":53.57,"entries":4.13,"reconcile2":0.27},"signals":180,"placed":4,"equity":992939.8,"open_positions":19,"pending_orders":8,"open_lots":87,"submitted_today":40,"filled_today":32,"unattributed_contracts":0,"top_signals":["S401:CRWD","S216:UBER","S216:CVNA","S216:UPST","S217:BILL","S218:BILL","S217:MCD","S218:MCD"],"github_run":"11312","github_run_id":"36582505877","status":"ok","data_quality":{"clean":{"n":1557,"win":49.52,"med":-7.69,"avg":41.73,"pnl":19436.83},"tainted":{"n":1941,"win":33.23,"med":-39.53,"avg":12.53,"pnl":-9775.28},"keep_only":{"n":801,"win":62.42,"med":52.0,"avg":61.99,"pnl":13373.45},"keep_only_recent":{"n":607,"win":61.45,"med":55.88,"avg":70.64,"pnl":9335.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:26:52  INFO      Mode: exits
14:26:52  INFO        Daily log -> logs/daily/2026-09-29.md
14:26:52  INFO        Daily log reconciled -> logs/daily/2026-09-29.md (2 ledger rows)
14:26:52  INFO        place_all_stops: checking 1 positions...
14:26:52  INFO        STOP skipped NNN: fractional (0.8102 shares) — software exit will handle it
14:26:52  INFO        [positions] 1/1 (1 valid)
14:26:52  INFO        Daily log -> logs/daily/2026-09-29.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.33|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  NNN  P&L -0.2%  $-0.06                                            HOLD|
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
=== options_live_micro LIVE 2026-09-29T10:26:53.825957-04:00 share=25% ===
2026-09-29 10:26:53,826 INFO === options_live_micro LIVE 2026-09-29T10:26:53.825957-04:00 share=25% ===
Live account equity $223.33 cash $189.85 #225458845 options_level=3
2026-09-29 10:26:54,066 INFO Live account equity $223.33 cash $189.85 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-29 10:26:54,092 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-29 10:26:54,112 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (202 earlier lines - see full log file)
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
## Ledger health — 2026-09-29
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1619 | WARN | <<<
| Missing exit records (post) |  1619 | WARN | <<<
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |    87 | INFO |
| Total closed lots           |  2612 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1557 med=-7.7% | TAINTED n=1941 med=-39.5% | KEEP-only n=801 med=+52.0% | KILL=20 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.33 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260929T143122Z

- UTC timestamp: `20260929T143122Z`
- GitHub run: [#11313](https://github.com/28twagg-ops/TradingBot/actions/runs/36583124386)
- Run id: `36583124386`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`78s`
- Full logs: `logs/action_runs/20260929T143122Z_live_bot.log`, `logs/action_runs/20260929T143122Z_live_options.log`, `logs/action_runs/20260929T143122Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1557 | 49.5 | -7.7 | +41.7 | $+19,437 |
| TAINTED | 1941 | 33.2 | -39.5 | +12.5 | $-9,775 |
| KEEP-only | 801 | 62.4 | +52.0 | +62.0 | $+13,373 |
| KEEP-only recent | 607 | 61.4 | +55.9 | +70.6 | $+9,335 |

- KEEP strategies (24): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (20): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-29T10:31:27.335437-04:00","date":"2026-09-29","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":65.6,"phases_s":{"reconcile":0.18,"cancel":0.03,"manage":2.75,"protective_stops":0.4,"scan":52.96,"entries":5.3,"reconcile2":0.11},"signals":180,"placed":0,"equity":992763.73,"open_positions":19,"pending_orders":8,"open_lots":87,"submitted_today":40,"filled_today":32,"unattributed_contracts":0,"top_signals":["S401:CRWD","S216:UBER","S216:CVNA","S216:UPST","S217:BILL","S218:BILL","S217:MCD","S218:MCD"],"github_run":"11313","github_run_id":"36583124386","status":"ok","data_quality":{"clean":{"n":1557,"win":49.52,"med":-7.69,"avg":41.73,"pnl":19436.83},"tainted":{"n":1941,"win":33.23,"med":-39.53,"avg":12.53,"pnl":-9775.28},"keep_only":{"n":801,"win":62.42,"med":52.0,"avg":61.99,"pnl":13373.45},"keep_only_recent":{"n":607,"win":61.45,"med":55.88,"avg":70.64,"pnl":9335.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:31:23  INFO      Mode: exits
14:31:23  INFO        Daily log -> logs/daily/2026-09-29.md
14:31:23  INFO        Daily log reconciled -> logs/daily/2026-09-29.md (2 ledger rows)
14:31:23  INFO        place_all_stops: checking 1 positions...
14:31:23  INFO        STOP skipped NNN: fractional (0.8102 shares) — software exit will handle it
14:31:23  INFO        [positions] 1/1 (1 valid)
14:31:23  INFO        Daily log -> logs/daily/2026-09-29.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.31|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  NNN  P&L -0.2%  $-0.08                                            HOLD|
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
=== options_live_micro LIVE 2026-09-29T10:31:24.604451-04:00 share=25% ===
2026-09-29 10:31:24,604 INFO === options_live_micro LIVE 2026-09-29T10:31:24.604451-04:00 share=25% ===
Live account equity $223.31 cash $189.85 #225458845 options_level=3
2026-09-29 10:31:24,645 INFO Live account equity $223.31 cash $189.85 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-29 10:31:24,668 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-29 10:31:24,682 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (207 earlier lines - see full log file)
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
## Ledger health — 2026-09-29
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1619 | WARN | <<<
| Missing exit records (post) |  1619 | WARN | <<<
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |    87 | INFO |
| Total closed lots           |  2612 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1557 med=-7.7% | TAINTED n=1941 med=-39.5% | KEEP-only n=801 med=+52.0% | KILL=20 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.31 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260929T143638Z

- UTC timestamp: `20260929T143638Z`
- GitHub run: [#11314](https://github.com/28twagg-ops/TradingBot/actions/runs/36583749818)
- Run id: `36583749818`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`62s`
- Full logs: `logs/action_runs/20260929T143638Z_live_bot.log`, `logs/action_runs/20260929T143638Z_live_options.log`, `logs/action_runs/20260929T143638Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1557 | 49.5 | -7.7 | +41.7 | $+19,437 |
| TAINTED | 1941 | 33.2 | -39.5 | +12.5 | $-9,775 |
| KEEP-only | 801 | 62.4 | +52.0 | +62.0 | $+13,373 |
| KEEP-only recent | 607 | 61.4 | +55.9 | +70.6 | $+9,335 |

- KEEP strategies (24): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (20): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-29T10:36:43.716783-04:00","date":"2026-09-29","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":52.1,"phases_s":{"reconcile":0.27,"cancel":0.06,"manage":3.41,"protective_stops":1.08,"scan":34.91,"entries":10.67,"reconcile2":0.23},"signals":180,"placed":0,"equity":992647.67,"open_positions":20,"pending_orders":6,"open_lots":89,"submitted_today":40,"filled_today":34,"unattributed_contracts":0,"top_signals":["S401:CRWD","S216:UBER","S216:CVNA","S216:UPST","S217:BILL","S218:BILL","S217:MCD","S218:MCD"],"github_run":"11314","github_run_id":"36583749818","status":"ok","data_quality":{"clean":{"n":1557,"win":49.52,"med":-7.69,"avg":41.73,"pnl":19436.83},"tainted":{"n":1941,"win":33.23,"med":-39.53,"avg":12.53,"pnl":-9775.28},"keep_only":{"n":801,"win":62.42,"med":52.0,"avg":61.99,"pnl":13373.45},"keep_only_recent":{"n":607,"win":61.45,"med":55.88,"avg":70.64,"pnl":9335.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:36:39  INFO      Mode: exits
14:36:40  INFO        Daily log -> logs/daily/2026-09-29.md
14:36:40  INFO        Daily log reconciled -> logs/daily/2026-09-29.md (2 ledger rows)
14:36:40  INFO        place_all_stops: checking 1 positions...
14:36:40  INFO        STOP skipped NNN: fractional (0.8102 shares) — software exit will handle it
14:36:40  INFO        [positions] 1/1 (1 valid)
14:36:40  INFO        Daily log -> logs/daily/2026-09-29.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.29|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  NNN  P&L -0.3%  $-0.10                                            HOLD|
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
=== options_live_micro LIVE 2026-09-29T10:36:41.039239-04:00 share=25% ===
2026-09-29 10:36:41,039 INFO === options_live_micro LIVE 2026-09-29T10:36:41.039239-04:00 share=25% ===
Live account equity $223.29 cash $189.85 #225458845 options_level=3
2026-09-29 10:36:41,151 INFO Live account equity $223.29 cash $189.85 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-29 10:36:41,235 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-29 10:36:41,293 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (207 earlier lines - see full log file)
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
## Ledger health — 2026-09-29
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1619 | WARN | <<<
| Missing exit records (post) |  1619 | WARN | <<<
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |    89 | INFO |
| Total closed lots           |  2612 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1557 med=-7.7% | TAINTED n=1941 med=-39.5% | KEEP-only n=801 med=+52.0% | KILL=20 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.29 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260929T144123Z

- UTC timestamp: `20260929T144123Z`
- GitHub run: [#11315](https://github.com/28twagg-ops/TradingBot/actions/runs/36584369816)
- Run id: `36584369816`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`59s`
- Full logs: `logs/action_runs/20260929T144123Z_live_bot.log`, `logs/action_runs/20260929T144123Z_live_options.log`, `logs/action_runs/20260929T144123Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1558 | 49.5 | -7.7 | +41.7 | $+19,435 |
| TAINTED | 1941 | 33.2 | -39.5 | +12.5 | $-9,775 |
| KEEP-only | 801 | 62.4 | +52.0 | +62.0 | $+13,373 |
| KEEP-only recent | 607 | 61.4 | +55.9 | +70.6 | $+9,335 |

- KEEP strategies (24): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (20): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-29T10:41:31.553620-04:00","date":"2026-09-29","mode":"entry+manage","header":"entry+manage (2 new)","elapsed_s":49.1,"phases_s":{"reconcile":0.31,"cancel":0.07,"manage":4.16,"protective_stops":1.34,"scan":29.45,"entries":11.85,"reconcile2":0.27},"signals":180,"placed":2,"equity":992568.33,"open_positions":21,"pending_orders":6,"open_lots":90,"submitted_today":42,"filled_today":36,"unattributed_contracts":0,"top_signals":["S401:CRWD","S216:UBER","S216:CVNA","S216:UPST","S217:BILL","S218:BILL","S217:MCD","S218:MCD"],"github_run":"11315","github_run_id":"36584369816","status":"ok","data_quality":{"clean":{"n":1558,"win":49.49,"med":-7.69,"avg":41.68,"pnl":19434.83},"tainted":{"n":1941,"win":33.23,"med":-39.53,"avg":12.53,"pnl":-9775.28},"keep_only":{"n":801,"win":62.42,"med":52.0,"avg":61.99,"pnl":13373.45},"keep_only_recent":{"n":607,"win":61.45,"med":55.88,"avg":70.64,"pnl":9335.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:41:25  INFO      Mode: exits
14:41:26  INFO        Daily log -> logs/daily/2026-09-29.md
14:41:26  INFO        Daily log reconciled -> logs/daily/2026-09-29.md (2 ledger rows)
14:41:26  INFO        place_all_stops: checking 1 positions...
14:41:26  INFO        STOP skipped NNN: fractional (0.8102 shares) — software exit will handle it
14:41:26  INFO        [positions] 1/1 (1 valid)
14:41:26  INFO        Daily log -> logs/daily/2026-09-29.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.27|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  NNN  P&L -0.3%  $-0.10                                            HOLD|
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
=== options_live_micro LIVE 2026-09-29T10:41:27.909164-04:00 share=25% ===
2026-09-29 10:41:27,909 INFO === options_live_micro LIVE 2026-09-29T10:41:27.909164-04:00 share=25% ===
Live account equity $223.29 cash $189.85 #225458845 options_level=3
2026-09-29 10:41:28,037 INFO Live account equity $223.29 cash $189.85 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-29 10:41:28,178 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-29 10:41:28,248 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (206 earlier lines - see full log file)
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
## Ledger health — 2026-09-29
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1619 | WARN | <<<
| Missing exit records (post) |  1619 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    90 | INFO |
| Total closed lots           |  2612 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1558 med=-7.7% | TAINTED n=1941 med=-39.5% | KEEP-only n=801 med=+52.0% | KILL=20 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.29 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260929T144613Z

- UTC timestamp: `20260929T144613Z`
- GitHub run: [#11316](https://github.com/28twagg-ops/TradingBot/actions/runs/36584997514)
- Run id: `36584997514`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`81s`
- Full logs: `logs/action_runs/20260929T144613Z_live_bot.log`, `logs/action_runs/20260929T144613Z_live_options.log`, `logs/action_runs/20260929T144613Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1558 | 49.5 | -7.7 | +41.7 | $+19,435 |
| TAINTED | 1941 | 33.2 | -39.5 | +12.5 | $-9,775 |
| KEEP-only | 801 | 62.4 | +52.0 | +62.0 | $+13,373 |
| KEEP-only recent | 607 | 61.4 | +55.9 | +70.6 | $+9,335 |

- KEEP strategies (24): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (20): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-29T10:46:17.835916-04:00","date":"2026-09-29","mode":"entry+manage","header":"entry+manage (16 new)","elapsed_s":72.7,"phases_s":{"reconcile":1.07,"cancel":0.07,"manage":3.59,"protective_stops":1.28,"scan":22.9,"entries":29.15,"reconcile2":0.49},"signals":180,"placed":16,"equity":992675.03,"open_positions":26,"pending_orders":10,"open_lots":102,"submitted_today":58,"filled_today":48,"unattributed_contracts":0,"top_signals":["S401:CRWD","S216:UBER","S216:CVNA","S216:UPST","S217:BILL","S218:BILL","S217:MCD","S218:MCD"],"github_run":"11316","github_run_id":"36584997514","status":"ok","data_quality":{"clean":{"n":1558,"win":49.49,"med":-7.69,"avg":41.68,"pnl":19434.83},"tainted":{"n":1941,"win":33.23,"med":-39.53,"avg":12.53,"pnl":-9775.28},"keep_only":{"n":801,"win":62.42,"med":52.0,"avg":61.99,"pnl":13373.45},"keep_only_recent":{"n":607,"win":61.45,"med":55.88,"avg":70.64,"pnl":9335.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:46:13  INFO      Mode: exits
14:46:14  INFO        Daily log -> logs/daily/2026-09-29.md
14:46:14  INFO        Daily log reconciled -> logs/daily/2026-09-29.md (2 ledger rows)
14:46:14  INFO        place_all_stops: checking 1 positions...
14:46:14  INFO        STOP skipped NNN: fractional (0.8102 shares) — software exit will handle it
14:46:14  INFO        [positions] 1/1 (1 valid)
14:46:14  INFO        Daily log -> logs/daily/2026-09-29.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.30|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  NNN  P&L -0.3%  $-0.09                                            HOLD|
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
=== options_live_micro LIVE 2026-09-29T10:46:15.398448-04:00 share=25% ===
2026-09-29 10:46:15,398 INFO === options_live_micro LIVE 2026-09-29T10:46:15.398448-04:00 share=25% ===
Live account equity $223.30 cash $189.85 #225458845 options_level=3
2026-09-29 10:46:15,533 INFO Live account equity $223.30 cash $189.85 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-29 10:46:15,633 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-29 10:46:15,702 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (219 earlier lines - see full log file)
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
## Ledger health — 2026-09-29
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1619 | WARN | <<<
| Missing exit records (post) |  1619 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |   102 | INFO |
| Total closed lots           |  2612 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1558 med=-7.7% | TAINTED n=1941 med=-39.5% | KEEP-only n=801 med=+52.0% | KILL=20 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.3 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260929T145144Z

- UTC timestamp: `20260929T145144Z`
- GitHub run: [#11317](https://github.com/28twagg-ops/TradingBot/actions/runs/36585623963)
- Run id: `36585623963`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`106s`
- Full logs: `logs/action_runs/20260929T145144Z_live_bot.log`, `logs/action_runs/20260929T145144Z_live_options.log`, `logs/action_runs/20260929T145144Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1560 | 49.4 | -7.7 | +41.5 | $+19,366 |
| TAINTED | 1941 | 33.2 | -39.5 | +12.5 | $-9,775 |
| KEEP-only | 803 | 62.3 | +51.7 | +61.7 | $+13,304 |
| KEEP-only recent | 609 | 61.2 | +55.6 | +70.2 | $+9,266 |

- KEEP strategies (24): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (20): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-29T10:51:51.347532-04:00","date":"2026-09-29","mode":"entry+manage","header":"entry+manage (2 new)","elapsed_s":92.8,"phases_s":{"reconcile":0.52,"cancel":0.21,"manage":6.76,"protective_stops":3.44,"scan":55.13,"entries":22.07,"reconcile2":0.65},"signals":180,"placed":2,"equity":992671.46,"open_positions":27,"pending_orders":10,"open_lots":102,"submitted_today":60,"filled_today":50,"unattributed_contracts":0,"top_signals":["S401:CRWD","S216:UBER","S216:CVNA","S216:UPST","S217:BILL","S218:BILL","S217:MCD","S218:MCD"],"github_run":"11317","github_run_id":"36585623963","status":"ok","data_quality":{"clean":{"n":1560,"win":49.42,"med":-7.69,"avg":41.55,"pnl":19365.83},"tainted":{"n":1941,"win":33.23,"med":-39.53,"avg":12.53,"pnl":-9775.28},"keep_only":{"n":803,"win":62.27,"med":51.72,"avg":61.68,"pnl":13304.45},"keep_only_recent":{"n":609,"win":61.25,"med":55.56,"avg":70.21,"pnl":9266.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:51:45  INFO      Mode: exits
14:51:46  INFO        Daily log -> logs/daily/2026-09-29.md
14:51:46  INFO        Daily log reconciled -> logs/daily/2026-09-29.md (2 ledger rows)
14:51:46  INFO        place_all_stops: checking 1 positions...
14:51:46  INFO        STOP skipped NNN: fractional (0.8102 shares) — software exit will handle it
14:51:46  INFO        [positions] 1/1 (1 valid)
14:51:46  INFO        Daily log -> logs/daily/2026-09-29.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:51 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.30|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  NNN  P&L -0.3%  $-0.09                                            HOLD|
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
=== options_live_micro LIVE 2026-09-29T10:51:47.539046-04:00 share=25% ===
2026-09-29 10:51:47,539 INFO === options_live_micro LIVE 2026-09-29T10:51:47.539046-04:00 share=25% ===
Live account equity $223.30 cash $189.85 #225458845 options_level=3
2026-09-29 10:51:47,763 INFO Live account equity $223.30 cash $189.85 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-29 10:51:47,973 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-29 10:51:48,112 INFO Live micro done. open_options=0 lots=0
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
## Ledger health — 2026-09-29
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1619 | WARN | <<<
| Missing exit records (post) |  1619 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |   102 | INFO |
| Total closed lots           |  2614 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1560 med=-7.7% | TAINTED n=1941 med=-39.5% | KEEP-only n=803 med=+51.7% | KILL=20 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.3 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260929T145632Z

- UTC timestamp: `20260929T145632Z`
- GitHub run: [#11318](https://github.com/28twagg-ops/TradingBot/actions/runs/36586190852)
- Run id: `36586190852`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`60s`
- Full logs: `logs/action_runs/20260929T145632Z_live_bot.log`, `logs/action_runs/20260929T145632Z_live_options.log`, `logs/action_runs/20260929T145632Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1561 | 49.4 | -7.7 | +41.5 | $+19,328 |
| TAINTED | 1941 | 33.2 | -39.5 | +12.5 | $-9,775 |
| KEEP-only | 804 | 62.2 | +51.7 | +61.5 | $+13,266 |
| KEEP-only recent | 610 | 61.1 | +55.3 | +70.0 | $+9,228 |

- KEEP strategies (24): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (20): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-29T10:56:38.727411-04:00","date":"2026-09-29","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":50.1,"phases_s":{"reconcile":0.12,"cancel":0.03,"manage":3.19,"protective_stops":0.47,"scan":35.19,"entries":3.95,"reconcile2":0.15},"signals":180,"placed":0,"equity":992561.19,"open_positions":27,"pending_orders":10,"open_lots":101,"submitted_today":60,"filled_today":50,"unattributed_contracts":0,"top_signals":["S401:CRWD","S216:UBER","S216:CVNA","S216:UPST","S217:BILL","S218:BILL","S217:MCD","S218:MCD"],"github_run":"11318","github_run_id":"36586190852","status":"ok","data_quality":{"clean":{"n":1561,"win":49.39,"med":-7.69,"avg":41.48,"pnl":19327.83},"tainted":{"n":1941,"win":33.23,"med":-39.53,"avg":12.53,"pnl":-9775.28},"keep_only":{"n":804,"win":62.19,"med":51.67,"avg":61.53,"pnl":13266.45},"keep_only_recent":{"n":610,"win":61.15,"med":55.28,"avg":69.99,"pnl":9228.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:56:34  INFO      Mode: exits
14:56:35  INFO        Daily log -> logs/daily/2026-09-29.md
14:56:35  INFO        Daily log reconciled -> logs/daily/2026-09-29.md (2 ledger rows)
14:56:35  INFO        place_all_stops: checking 1 positions...
14:56:35  INFO        STOP skipped NNN: fractional (0.8102 shares) — software exit will handle it
14:56:35  INFO        [positions] 1/1 (1 valid)
14:56:35  INFO        Daily log -> logs/daily/2026-09-29.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:56 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.33|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  NNN  P&L -0.2%  $-0.06                                            HOLD|
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
=== options_live_micro LIVE 2026-09-29T10:56:35.865135-04:00 share=25% ===
2026-09-29 10:56:35,865 INFO === options_live_micro LIVE 2026-09-29T10:56:35.865135-04:00 share=25% ===
Live account equity $223.33 cash $189.85 #225458845 options_level=3
2026-09-29 10:56:36,096 INFO Live account equity $223.33 cash $189.85 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-29 10:56:36,117 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-29 10:56:36,132 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (207 earlier lines - see full log file)
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
## Ledger health — 2026-09-29
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1619 | WARN | <<<
| Missing exit records (post) |  1619 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |   101 | INFO |
| Total closed lots           |  2615 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1561 med=-7.7% | TAINTED n=1941 med=-39.5% | KEEP-only n=804 med=+51.7% | KILL=20 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.33 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260929T150137Z

- UTC timestamp: `20260929T150137Z`
- GitHub run: [#11319](https://github.com/28twagg-ops/TradingBot/actions/runs/36586819688)
- Run id: `36586819688`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`82s`
- Full logs: `logs/action_runs/20260929T150137Z_live_bot.log`, `logs/action_runs/20260929T150137Z_live_options.log`, `logs/action_runs/20260929T150137Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1563 | 49.3 | -12.5 | +41.4 | $+19,257 |
| TAINTED | 1941 | 33.2 | -39.5 | +12.5 | $-9,775 |
| KEEP-only | 806 | 62.0 | +51.6 | +61.2 | $+13,195 |
| KEEP-only recent | 612 | 60.9 | +54.8 | +69.6 | $+9,157 |

- KEEP strategies (24): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (20): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-29T11:01:42.191956-04:00","date":"2026-09-29","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":70.2,"phases_s":{"reconcile":0.22,"cancel":0.03,"manage":3.48,"protective_stops":0.46,"scan":54.22,"entries":4.29,"reconcile2":0.32},"signals":180,"placed":0,"equity":992459.55,"open_positions":28,"pending_orders":6,"open_lots":103,"submitted_today":60,"filled_today":54,"unattributed_contracts":0,"top_signals":["S401:CRWD","S216:UBER","S216:CVNA","S216:UPST","S217:BILL","S218:BILL","S217:MCD","S218:MCD"],"github_run":"11319","github_run_id":"36586819688","status":"ok","data_quality":{"clean":{"n":1563,"win":49.33,"med":-12.5,"avg":41.35,"pnl":19256.83},"tainted":{"n":1941,"win":33.23,"med":-39.53,"avg":12.53,"pnl":-9775.28},"keep_only":{"n":806,"win":62.03,"med":51.61,"avg":61.23,"pnl":13195.45},"keep_only_recent":{"n":612,"win":60.95,"med":54.77,"avg":69.57,"pnl":9157.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:01:38  INFO      Mode: exits
15:01:38  INFO        Daily log -> logs/daily/2026-09-29.md
15:01:38  INFO        Daily log reconciled -> logs/daily/2026-09-29.md (2 ledger rows)
15:01:38  INFO        place_all_stops: checking 1 positions...
15:01:38  INFO        STOP skipped NNN: fractional (0.8102 shares) — software exit will handle it
15:01:38  INFO        [positions] 1/1 (1 valid)
15:01:38  INFO        Daily log -> logs/daily/2026-09-29.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.29|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  NNN  P&L -0.3%  $-0.10                                            HOLD|
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
=== options_live_micro LIVE 2026-09-29T11:01:39.446642-04:00 share=25% ===
2026-09-29 11:01:39,446 INFO === options_live_micro LIVE 2026-09-29T11:01:39.446642-04:00 share=25% ===
Live account equity $223.29 cash $189.85 #225458845 options_level=3
2026-09-29 11:01:39,498 INFO Live account equity $223.29 cash $189.85 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-29 11:01:39,519 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-29 11:01:39,535 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (206 earlier lines - see full log file)
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
## Ledger health — 2026-09-29
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1619 | WARN | <<<
| Missing exit records (post) |  1619 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |   103 | INFO |
| Total closed lots           |  2617 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1563 med=-12.5% | TAINTED n=1941 med=-39.5% | KEEP-only n=806 med=+51.6% | KILL=20 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.29 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260929T150629Z

- UTC timestamp: `20260929T150629Z`
- GitHub run: [#11320](https://github.com/28twagg-ops/TradingBot/actions/runs/36587464111)
- Run id: `36587464111`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`105s`
- Full logs: `logs/action_runs/20260929T150629Z_live_bot.log`, `logs/action_runs/20260929T150629Z_live_options.log`, `logs/action_runs/20260929T150629Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1563 | 49.3 | -12.5 | +41.4 | $+19,257 |
| TAINTED | 1942 | 33.2 | -39.8 | +12.5 | $-9,790 |
| KEEP-only | 806 | 62.0 | +51.6 | +61.2 | $+13,195 |
| KEEP-only recent | 612 | 60.9 | +54.8 | +69.6 | $+9,157 |

- KEEP strategies (24): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (20): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-29T11:06:37.818537-04:00","date":"2026-09-29","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":91.9,"phases_s":{"reconcile":0.48,"cancel":0.15,"manage":6.86,"protective_stops":2.79,"scan":55.98,"entries":21.14,"reconcile2":0.59},"signals":180,"placed":0,"equity":992443.98,"open_positions":27,"pending_orders":6,"open_lots":86,"submitted_today":60,"filled_today":54,"unattributed_contracts":0,"top_signals":["S401:CRWD","S216:UBER","S216:CVNA","S216:UPST","S217:BILL","S218:BILL","S217:MCD","S218:MCD"],"github_run":"11320","github_run_id":"36587464111","status":"ok","data_quality":{"clean":{"n":1563,"win":49.33,"med":-12.5,"avg":41.35,"pnl":19256.83},"tainted":{"n":1942,"win":33.21,"med":-39.77,"avg":12.48,"pnl":-9790.28},"keep_only":{"n":806,"win":62.03,"med":51.61,"avg":61.23,"pnl":13195.45},"keep_only_recent":{"n":612,"win":60.95,"med":54.77,"avg":69.57,"pnl":9157.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:06:31  INFO      Mode: exits
15:06:31  INFO        Daily log -> logs/daily/2026-09-29.md
15:06:31  INFO        Daily log reconciled -> logs/daily/2026-09-29.md (2 ledger rows)
15:06:31  INFO        place_all_stops: checking 1 positions...
15:06:31  INFO        STOP skipped NNN: fractional (0.8102 shares) — software exit will handle it
15:06:32  INFO        [positions] 1/1 (1 valid)
15:06:32  INFO        Daily log -> logs/daily/2026-09-29.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.25|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  NNN  P&L -0.4%  $-0.14                                            HOLD|
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
=== options_live_micro LIVE 2026-09-29T11:06:33.472505-04:00 share=25% ===
2026-09-29 11:06:33,472 INFO === options_live_micro LIVE 2026-09-29T11:06:33.472505-04:00 share=25% ===
Live account equity $223.25 cash $189.85 #225458845 options_level=3
2026-09-29 11:06:33,694 INFO Live account equity $223.25 cash $189.85 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-29 11:06:33,905 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-29 11:06:34,040 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (221 earlier lines - see full log file)
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
## Ledger health — 2026-09-29
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1619 | WARN | <<<
| Missing exit records (post) |  1619 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    86 | INFO |
| Total closed lots           |  2618 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1563 med=-12.5% | TAINTED n=1942 med=-39.8% | KEEP-only n=806 med=+51.6% | KILL=20 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.25 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260929T151144Z

- UTC timestamp: `20260929T151144Z`
- GitHub run: [#11321](https://github.com/28twagg-ops/TradingBot/actions/runs/36588103055)
- Run id: `36588103055`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`103s`
- Full logs: `logs/action_runs/20260929T151144Z_live_bot.log`, `logs/action_runs/20260929T151144Z_live_options.log`, `logs/action_runs/20260929T151144Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1564 | 49.3 | -13.4 | +41.3 | $+19,243 |
| TAINTED | 1942 | 33.2 | -39.8 | +12.5 | $-9,790 |
| KEEP-only | 806 | 62.0 | +51.6 | +61.2 | $+13,195 |
| KEEP-only recent | 612 | 60.9 | +54.8 | +69.6 | $+9,157 |

- KEEP strategies (24): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (20): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-29T11:11:52.106006-04:00","date":"2026-09-29","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":90.4,"phases_s":{"reconcile":0.53,"cancel":0.15,"manage":6.71,"protective_stops":3.22,"scan":54.09,"entries":21.12,"reconcile2":0.52},"signals":180,"placed":0,"equity":992433.98,"open_positions":27,"pending_orders":6,"open_lots":85,"submitted_today":60,"filled_today":54,"unattributed_contracts":0,"top_signals":["S401:CRWD","S216:UBER","S216:CVNA","S216:UPST","S217:BILL","S218:BILL","S217:MCD","S218:MCD"],"github_run":"11321","github_run_id":"36588103055","status":"ok","data_quality":{"clean":{"n":1564,"win":49.3,"med":-13.4,"avg":41.27,"pnl":19242.83},"tainted":{"n":1942,"win":33.21,"med":-39.77,"avg":12.48,"pnl":-9790.28},"keep_only":{"n":806,"win":62.03,"med":51.61,"avg":61.23,"pnl":13195.45},"keep_only_recent":{"n":612,"win":60.95,"med":54.77,"avg":69.57,"pnl":9157.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:11:46  INFO      Mode: exits
15:11:46  INFO        Daily log -> logs/daily/2026-09-29.md
15:11:46  INFO        Daily log reconciled -> logs/daily/2026-09-29.md (2 ledger rows)
15:11:46  INFO        place_all_stops: checking 1 positions...
15:11:46  INFO        STOP skipped NNN: fractional (0.8102 shares) — software exit will handle it
15:11:47  INFO        [positions] 1/1 (1 valid)
15:11:47  INFO        Daily log -> logs/daily/2026-09-29.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.27|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  NNN  P&L -0.4%  $-0.12                                            HOLD|
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
=== options_live_micro LIVE 2026-09-29T11:11:48.432253-04:00 share=25% ===
2026-09-29 11:11:48,432 INFO === options_live_micro LIVE 2026-09-29T11:11:48.432253-04:00 share=25% ===
Live account equity $223.27 cash $189.85 #225458845 options_level=3
2026-09-29 11:11:48,660 INFO Live account equity $223.27 cash $189.85 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-29 11:11:48,872 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-29 11:11:49,010 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (207 earlier lines - see full log file)
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
## Ledger health — 2026-09-29
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1619 | WARN | <<<
| Missing exit records (post) |  1619 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    85 | INFO |
| Total closed lots           |  2619 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1564 med=-13.4% | TAINTED n=1942 med=-39.8% | KEEP-only n=806 med=+51.6% | KILL=20 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.27 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260929T151625Z

- UTC timestamp: `20260929T151625Z`
- GitHub run: [#11322](https://github.com/28twagg-ops/TradingBot/actions/runs/36588744822)
- Run id: `36588744822`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`76s`
- Full logs: `logs/action_runs/20260929T151625Z_live_bot.log`, `logs/action_runs/20260929T151625Z_live_options.log`, `logs/action_runs/20260929T151625Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1565 | 49.3 | -14.3 | +41.2 | $+19,228 |
| TAINTED | 1942 | 33.2 | -39.8 | +12.5 | $-9,790 |
| KEEP-only | 806 | 62.0 | +51.6 | +61.2 | $+13,195 |
| KEEP-only recent | 612 | 60.9 | +54.8 | +69.6 | $+9,157 |

- KEEP strategies (24): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (20): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-29T11:16:31.436775-04:00","date":"2026-09-29","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":66.8,"phases_s":{"reconcile":0.39,"cancel":0.12,"manage":7.34,"protective_stops":2.57,"scan":35.18,"entries":17.59,"reconcile2":0.45},"signals":180,"placed":0,"equity":992228.82,"open_positions":27,"pending_orders":6,"open_lots":84,"submitted_today":60,"filled_today":54,"unattributed_contracts":0,"top_signals":["S401:CRWD","S216:UBER","S216:CVNA","S216:UPST","S217:BILL","S218:BILL","S217:MCD","S218:MCD"],"github_run":"11322","github_run_id":"36588744822","status":"ok","data_quality":{"clean":{"n":1565,"win":49.27,"med":-14.29,"avg":41.19,"pnl":19227.83},"tainted":{"n":1942,"win":33.21,"med":-39.77,"avg":12.48,"pnl":-9790.28},"keep_only":{"n":806,"win":62.03,"med":51.61,"avg":61.23,"pnl":13195.45},"keep_only_recent":{"n":612,"win":60.95,"med":54.77,"avg":69.57,"pnl":9157.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:16:26  INFO      Mode: exits
15:16:27  INFO        Daily log -> logs/daily/2026-09-29.md
15:16:27  INFO        Daily log reconciled -> logs/daily/2026-09-29.md (2 ledger rows)
15:16:27  INFO        place_all_stops: checking 1 positions...
15:16:27  INFO        STOP skipped NNN: fractional (0.8102 shares) — software exit will handle it
15:16:27  INFO        [positions] 1/1 (1 valid)
15:16:27  INFO        Daily log -> logs/daily/2026-09-29.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.25|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  NNN  P&L -0.4%  $-0.14                                            HOLD|
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
=== options_live_micro LIVE 2026-09-29T11:16:28.470145-04:00 share=25% ===
2026-09-29 11:16:28,470 INFO === options_live_micro LIVE 2026-09-29T11:16:28.470145-04:00 share=25% ===
Live account equity $223.25 cash $189.85 #225458845 options_level=3
2026-09-29 11:16:28,676 INFO Live account equity $223.25 cash $189.85 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-29 11:16:28,848 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-29 11:16:28,972 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (205 earlier lines - see full log file)
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
## Ledger health — 2026-09-29
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1619 | WARN | <<<
| Missing exit records (post) |  1619 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    84 | INFO |
| Total closed lots           |  2620 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1565 med=-14.3% | TAINTED n=1942 med=-39.8% | KEEP-only n=806 med=+51.6% | KILL=20 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.25 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260929T152131Z

- UTC timestamp: `20260929T152131Z`
- GitHub run: [#11323](https://github.com/28twagg-ops/TradingBot/actions/runs/36589381866)
- Run id: `36589381866`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`124s`
- Full logs: `logs/action_runs/20260929T152131Z_live_bot.log`, `logs/action_runs/20260929T152131Z_live_options.log`, `logs/action_runs/20260929T152131Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1567 | 49.2 | -15.9 | +41.0 | $+19,186 |
| TAINTED | 1943 | 33.2 | -39.5 | +12.6 | $-9,781 |
| KEEP-only | 807 | 62.0 | +51.6 | +61.1 | $+13,168 |
| KEEP-only recent | 613 | 60.8 | +54.5 | +69.4 | $+9,130 |

- KEEP strategies (24): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (20): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-29T11:21:38.851618-04:00","date":"2026-09-29","mode":"entry+manage","header":"entry+manage (20 new)","elapsed_s":110.6,"phases_s":{"reconcile":0.47,"cancel":0.15,"manage":7.72,"protective_stops":3.42,"scan":53.45,"entries":30.99,"reconcile2":1.13},"signals":180,"placed":20,"equity":992400.0,"open_positions":28,"pending_orders":14,"open_lots":94,"submitted_today":80,"filled_today":66,"unattributed_contracts":0,"top_signals":["S401:CRWD","S216:UBER","S216:CVNA","S216:UPST","S217:BILL","S218:BILL","S217:MCD","S218:MCD"],"github_run":"11323","github_run_id":"36589381866","status":"ok","data_quality":{"clean":{"n":1567,"win":49.2,"med":-15.87,"avg":41.05,"pnl":19185.83},"tainted":{"n":1943,"win":33.25,"med":-39.53,"avg":12.59,"pnl":-9781.28},"keep_only":{"n":807,"win":61.96,"med":51.61,"avg":61.09,"pnl":13168.45},"keep_only_recent":{"n":613,"win":60.85,"med":54.55,"avg":69.38,"pnl":9130.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:21:32  INFO      Mode: exits
15:21:33  INFO        Daily log -> logs/daily/2026-09-29.md
15:21:33  INFO        Daily log reconciled -> logs/daily/2026-09-29.md (2 ledger rows)
15:21:33  INFO        place_all_stops: checking 1 positions...
15:21:33  INFO        STOP skipped NNN: fractional (0.8102 shares) — software exit will handle it
15:21:33  INFO        [positions] 1/1 (1 valid)
15:21:33  INFO        Daily log -> logs/daily/2026-09-29.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.24|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  NNN  P&L -0.4%  $-0.15                                            HOLD|
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
=== options_live_micro LIVE 2026-09-29T11:21:34.585384-04:00 share=25% ===
2026-09-29 11:21:34,585 INFO === options_live_micro LIVE 2026-09-29T11:21:34.585384-04:00 share=25% ===
Live account equity $223.24 cash $189.85 #225458845 options_level=3
2026-09-29 11:21:34,808 INFO Live account equity $223.24 cash $189.85 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-29 11:21:35,014 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-29 11:21:35,151 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (228 earlier lines - see full log file)
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
## Ledger health — 2026-09-29
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1619 | WARN | <<<
| Missing exit records (post) |  1619 | WARN | <<<
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |    94 | INFO |
| Total closed lots           |  2623 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1567 med=-15.9% | TAINTED n=1943 med=-39.5% | KEEP-only n=807 med=+51.6% | KILL=20 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.24 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260929T152634Z

- UTC timestamp: `20260929T152634Z`
- GitHub run: [#11324](https://github.com/28twagg-ops/TradingBot/actions/runs/36590019806)
- Run id: `36590019806`
- Live bot: exit=`0`, duration=`6s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`106s`
- Full logs: `logs/action_runs/20260929T152634Z_live_bot.log`, `logs/action_runs/20260929T152634Z_live_options.log`, `logs/action_runs/20260929T152634Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1567 | 49.2 | -15.9 | +41.0 | $+19,186 |
| TAINTED | 1943 | 33.2 | -39.5 | +12.6 | $-9,781 |
| KEEP-only | 807 | 62.0 | +51.6 | +61.1 | $+13,168 |
| KEEP-only recent | 613 | 60.8 | +54.5 | +69.4 | $+9,130 |

- KEEP strategies (24): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (20): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-29T11:26:45.161948-04:00","date":"2026-09-29","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":92.3,"phases_s":{"reconcile":0.56,"cancel":0.15,"manage":6.97,"protective_stops":3.28,"scan":55.38,"entries":21.65,"reconcile2":0.6},"signals":180,"placed":0,"equity":992445.73,"open_positions":28,"pending_orders":12,"open_lots":96,"submitted_today":80,"filled_today":68,"unattributed_contracts":0,"top_signals":["S401:CRWD","S216:UBER","S216:CVNA","S216:UPST","S217:BILL","S218:BILL","S217:MCD","S218:MCD"],"github_run":"11324","github_run_id":"36590019806","status":"ok","data_quality":{"clean":{"n":1567,"win":49.2,"med":-15.87,"avg":41.05,"pnl":19185.83},"tainted":{"n":1943,"win":33.25,"med":-39.53,"avg":12.59,"pnl":-9781.28},"keep_only":{"n":807,"win":61.96,"med":51.61,"avg":61.09,"pnl":13168.45},"keep_only_recent":{"n":613,"win":60.85,"med":54.55,"avg":69.38,"pnl":9130.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:26:35  INFO      Mode: exits
15:26:36  INFO        Daily log -> logs/daily/2026-09-29.md
15:26:36  INFO        Daily log reconciled -> logs/daily/2026-09-29.md (2 ledger rows)
15:26:36  INFO        place_all_stops: checking 1 positions...
15:26:36  INFO        STOP skipped NNN: fractional (0.8102 shares) — software exit will handle it
15:26:36  INFO        [positions] 1/1 (1 valid)
15:26:37  INFO        SELL MARKET [urgent] NNN closed
15:26:39  INFO        TX logged: SELL NNN  P&L -0.57%
15:26:39  INFO        Daily log -> logs/daily/2026-09-29.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.20|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  NNN  P&L -0.6%  $-0.19                         EXIT: stop_loss (-0.6%)|
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
|  NNN                                         -0.57%  (threshold -0.50%)|
|  Count                                                                1|
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-29T11:26:40.752654-04:00 share=25% ===
2026-09-29 11:26:40,752 INFO === options_live_micro LIVE 2026-09-29T11:26:40.752654-04:00 share=25% ===
Live account equity $223.19 cash $223.19 #225458845 options_level=3
2026-09-29 11:26:40,985 INFO Live account equity $223.19 cash $223.19 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-29 11:26:41,200 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-29 11:26:41,342 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (202 earlier lines - see full log file)
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
## Ledger health — 2026-09-29
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1619 | WARN | <<<
| Missing exit records (post) |  1619 | WARN | <<<
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |    96 | INFO |
| Total closed lots           |  2623 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1567 med=-15.9% | TAINTED n=1943 med=-39.5% | KEEP-only n=807 med=+51.6% | KILL=20 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.19 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260929T153121Z

- UTC timestamp: `20260929T153121Z`
- GitHub run: [#11325](https://github.com/28twagg-ops/TradingBot/actions/runs/36590661727)
- Run id: `36590661727`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`78s`
- Full logs: `logs/action_runs/20260929T153121Z_live_bot.log`, `logs/action_runs/20260929T153121Z_live_options.log`, `logs/action_runs/20260929T153121Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1567 | 49.2 | -15.9 | +41.0 | $+19,186 |
| TAINTED | 1943 | 33.2 | -39.5 | +12.6 | $-9,781 |
| KEEP-only | 807 | 62.0 | +51.6 | +61.1 | $+13,168 |
| KEEP-only recent | 613 | 60.8 | +54.5 | +69.4 | $+9,130 |

- KEEP strategies (24): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (20): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-29T11:31:26.638396-04:00","date":"2026-09-29","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":66.2,"phases_s":{"reconcile":0.36,"cancel":0.03,"manage":3.26,"protective_stops":0.44,"scan":53.08,"entries":4.94,"reconcile2":0.11},"signals":180,"placed":0,"equity":992515.36,"open_positions":29,"pending_orders":6,"open_lots":102,"submitted_today":80,"filled_today":74,"unattributed_contracts":0,"top_signals":["S401:CRWD","S216:UBER","S216:CVNA","S216:UPST","S217:BILL","S218:BILL","S217:MCD","S218:MCD"],"github_run":"11325","github_run_id":"36590661727","status":"ok","data_quality":{"clean":{"n":1567,"win":49.2,"med":-15.87,"avg":41.05,"pnl":19185.83},"tainted":{"n":1943,"win":33.25,"med":-39.53,"avg":12.59,"pnl":-9781.28},"keep_only":{"n":807,"win":61.96,"med":51.61,"avg":61.09,"pnl":13168.45},"keep_only_recent":{"n":613,"win":60.85,"med":54.55,"avg":69.38,"pnl":9130.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:31:22  INFO      Mode: exits
15:31:23  INFO        Daily log -> logs/daily/2026-09-29.md
15:31:23  INFO        Daily log reconciled -> logs/daily/2026-09-29.md (3 ledger rows)
15:31:23  INFO        Daily log -> logs/daily/2026-09-29.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.19|
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
=== options_live_micro LIVE 2026-09-29T11:31:23.898847-04:00 share=25% ===
2026-09-29 11:31:23,898 INFO === options_live_micro LIVE 2026-09-29T11:31:23.898847-04:00 share=25% ===
Live account equity $223.19 cash $223.19 #225458845 options_level=3
2026-09-29 11:31:23,941 INFO Live account equity $223.19 cash $223.19 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-29 11:31:23,962 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-29 11:31:23,975 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (202 earlier lines - see full log file)
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
## Ledger health — 2026-09-29
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1619 | WARN | <<<
| Missing exit records (post) |  1619 | WARN | <<<
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |   102 | INFO |
| Total closed lots           |  2623 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1567 med=-15.9% | TAINTED n=1943 med=-39.5% | KEEP-only n=807 med=+51.6% | KILL=20 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.19 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260929T153640Z

- UTC timestamp: `20260929T153640Z`
- GitHub run: [#11326](https://github.com/28twagg-ops/TradingBot/actions/runs/36591304432)
- Run id: `36591304432`
- Live bot: exit=`0`, duration=`5s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`17s`
- Full logs: `logs/action_runs/20260929T153640Z_live_bot.log`, `logs/action_runs/20260929T153640Z_live_options.log`, `logs/action_runs/20260929T153640Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1567 | 49.2 | -15.9 | +41.0 | $+19,186 |
| TAINTED | 1943 | 33.2 | -39.5 | +12.6 | $-9,781 |
| KEEP-only | 807 | 62.0 | +51.6 | +61.1 | $+13,168 |
| KEEP-only recent | 613 | 60.8 | +54.5 | +69.4 | $+9,130 |

- KEEP strategies (24): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (20): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-29T11:36:49.388751-04:00","date":"2026-09-29","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":7.0,"phases_s":{"reconcile":0.25,"cancel":0.32,"manage":4.39,"protective_stops":1.53},"signals":0,"placed":0,"equity":992459.94,"open_positions":29,"pending_orders":6,"open_lots":102,"submitted_today":80,"filled_today":74,"unattributed_contracts":0,"top_signals":[],"github_run":"11326","github_run_id":"36591304432","status":"ok","data_quality":{"clean":{"n":1567,"win":49.2,"med":-15.87,"avg":41.05,"pnl":19185.83},"tainted":{"n":1943,"win":33.25,"med":-39.53,"avg":12.59,"pnl":-9781.28},"keep_only":{"n":807,"win":61.96,"med":51.61,"avg":61.09,"pnl":13168.45},"keep_only_recent":{"n":613,"win":60.85,"med":54.55,"avg":69.38,"pnl":9130.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:36:44  INFO      Mode: exits
15:36:44  INFO        Daily log -> logs/daily/2026-09-29.md
15:36:44  INFO        Daily log reconciled -> logs/daily/2026-09-29.md (3 ledger rows)
15:36:45  INFO        Daily log -> logs/daily/2026-09-29.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.19|
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
=== options_live_micro LIVE 2026-09-29T11:36:46.092619-04:00 share=25% ===
2026-09-29 11:36:46,092 INFO === options_live_micro LIVE 2026-09-29T11:36:46.092619-04:00 share=25% ===
Live account equity $223.19 cash $223.19 #225458845 options_level=3
2026-09-29 11:36:46,229 INFO Live account equity $223.19 cash $223.19 #225458845 options_level=3
Live micro: manage/exits only
2026-09-29 11:36:46,349 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-29 11:36:46,382 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (193 earlier lines - see full log file)
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
## Ledger health — 2026-09-29
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1619 | WARN | <<<
| Missing exit records (post) |  1619 | WARN | <<<
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |   102 | INFO |
| Total closed lots           |  2623 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1567 med=-15.9% | TAINTED n=1943 med=-39.5% | KEEP-only n=807 med=+51.6% | KILL=20 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.19 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260929T154133Z

- UTC timestamp: `20260929T154133Z`
- GitHub run: [#11327](https://github.com/28twagg-ops/TradingBot/actions/runs/36591934840)
- Run id: `36591934840`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`24s`
- Full logs: `logs/action_runs/20260929T154133Z_live_bot.log`, `logs/action_runs/20260929T154133Z_live_options.log`, `logs/action_runs/20260929T154133Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1567 | 49.2 | -15.9 | +41.0 | $+19,186 |
| TAINTED | 1943 | 33.2 | -39.5 | +12.6 | $-9,781 |
| KEEP-only | 807 | 62.0 | +51.6 | +61.1 | $+13,168 |
| KEEP-only recent | 613 | 60.8 | +54.5 | +69.4 | $+9,130 |

- KEEP strategies (24): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (20): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-29T11:41:40.382496-04:00","date":"2026-09-29","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":11.7,"phases_s":{"reconcile":0.48,"cancel":0.24,"manage":7.22,"protective_stops":2.97},"signals":0,"placed":0,"equity":992394.24,"open_positions":29,"pending_orders":0,"open_lots":102,"submitted_today":80,"filled_today":74,"unattributed_contracts":0,"top_signals":[],"github_run":"11327","github_run_id":"36591934840","status":"ok","data_quality":{"clean":{"n":1567,"win":49.2,"med":-15.87,"avg":41.05,"pnl":19185.83},"tainted":{"n":1943,"win":33.25,"med":-39.53,"avg":12.59,"pnl":-9781.28},"keep_only":{"n":807,"win":61.96,"med":51.61,"avg":61.09,"pnl":13168.45},"keep_only_recent":{"n":613,"win":60.85,"med":54.55,"avg":69.38,"pnl":9130.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:41:34  INFO      Mode: exits
15:41:35  INFO        Daily log -> logs/daily/2026-09-29.md
15:41:35  INFO        Daily log reconciled -> logs/daily/2026-09-29.md (3 ledger rows)
15:41:36  INFO        Daily log -> logs/daily/2026-09-29.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.19|
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
=== options_live_micro LIVE 2026-09-29T11:41:36.844072-04:00 share=25% ===
2026-09-29 11:41:36,844 INFO === options_live_micro LIVE 2026-09-29T11:41:36.844072-04:00 share=25% ===
Live account equity $223.19 cash $223.19 #225458845 options_level=3
2026-09-29 11:41:37,066 INFO Live account equity $223.19 cash $223.19 #225458845 options_level=3
Live micro: manage/exits only
2026-09-29 11:41:37,269 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-29 11:41:37,337 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (180 earlier lines - see full log file)
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
## Ledger health — 2026-09-29
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1619 | WARN | <<<
| Missing exit records (post) |  1619 | WARN | <<<
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |   102 | INFO |
| Total closed lots           |  2623 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1567 med=-15.9% | TAINTED n=1943 med=-39.5% | KEEP-only n=807 med=+51.6% | KILL=20 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.19 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260929T154623Z

- UTC timestamp: `20260929T154623Z`
- GitHub run: [#11328](https://github.com/28twagg-ops/TradingBot/actions/runs/36592567056)
- Run id: `36592567056`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`25s`
- Full logs: `logs/action_runs/20260929T154623Z_live_bot.log`, `logs/action_runs/20260929T154623Z_live_options.log`, `logs/action_runs/20260929T154623Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1567 | 49.2 | -15.9 | +41.0 | $+19,186 |
| TAINTED | 1943 | 33.2 | -39.5 | +12.6 | $-9,781 |
| KEEP-only | 807 | 62.0 | +51.6 | +61.1 | $+13,168 |
| KEEP-only recent | 613 | 60.8 | +54.5 | +69.4 | $+9,130 |

- KEEP strategies (24): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (20): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-29T11:46:30.380610-04:00","date":"2026-09-29","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":12.4,"phases_s":{"reconcile":0.52,"cancel":0.24,"manage":7.6,"protective_stops":3.2},"signals":0,"placed":0,"equity":992384.86,"open_positions":29,"pending_orders":0,"open_lots":102,"submitted_today":80,"filled_today":74,"unattributed_contracts":0,"top_signals":[],"github_run":"11328","github_run_id":"36592567056","status":"ok","data_quality":{"clean":{"n":1567,"win":49.2,"med":-15.87,"avg":41.05,"pnl":19185.83},"tainted":{"n":1943,"win":33.25,"med":-39.53,"avg":12.59,"pnl":-9781.28},"keep_only":{"n":807,"win":61.96,"med":51.61,"avg":61.09,"pnl":13168.45},"keep_only_recent":{"n":613,"win":60.85,"med":54.55,"avg":69.38,"pnl":9130.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:46:24  INFO      Mode: exits
15:46:25  INFO        Daily log -> logs/daily/2026-09-29.md
15:46:25  INFO        Daily log reconciled -> logs/daily/2026-09-29.md (3 ledger rows)
15:46:25  INFO        Daily log -> logs/daily/2026-09-29.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.19|
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
=== options_live_micro LIVE 2026-09-29T11:46:26.632821-04:00 share=25% ===
2026-09-29 11:46:26,632 INFO === options_live_micro LIVE 2026-09-29T11:46:26.632821-04:00 share=25% ===
Live account equity $223.19 cash $223.19 #225458845 options_level=3
2026-09-29 11:46:26,883 INFO Live account equity $223.19 cash $223.19 #225458845 options_level=3
Live micro: manage/exits only
2026-09-29 11:46:27,112 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-29 11:46:27,188 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (180 earlier lines - see full log file)
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
## Ledger health — 2026-09-29
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1619 | WARN | <<<
| Missing exit records (post) |  1619 | WARN | <<<
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |   102 | INFO |
| Total closed lots           |  2623 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1567 med=-15.9% | TAINTED n=1943 med=-39.5% | KEEP-only n=807 med=+51.6% | KILL=20 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.19 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260929T155123Z

- UTC timestamp: `20260929T155123Z`
- GitHub run: [#11329](https://github.com/28twagg-ops/TradingBot/actions/runs/36593196619)
- Run id: `36593196619`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`26s`
- Full logs: `logs/action_runs/20260929T155123Z_live_bot.log`, `logs/action_runs/20260929T155123Z_live_options.log`, `logs/action_runs/20260929T155123Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1567 | 49.2 | -15.9 | +41.0 | $+19,186 |
| TAINTED | 1943 | 33.2 | -39.5 | +12.6 | $-9,781 |
| KEEP-only | 807 | 62.0 | +51.6 | +61.1 | $+13,168 |
| KEEP-only recent | 613 | 60.8 | +54.5 | +69.4 | $+9,130 |

- KEEP strategies (24): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (20): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-29T11:51:30.681546-04:00","date":"2026-09-29","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":13.8,"phases_s":{"reconcile":0.51,"cancel":0.24,"manage":8.9,"protective_stops":3.38},"signals":0,"placed":0,"equity":992280.77,"open_positions":29,"pending_orders":0,"open_lots":102,"submitted_today":80,"filled_today":74,"unattributed_contracts":0,"top_signals":[],"github_run":"11329","github_run_id":"36593196619","status":"ok","data_quality":{"clean":{"n":1567,"win":49.2,"med":-15.87,"avg":41.05,"pnl":19185.83},"tainted":{"n":1943,"win":33.25,"med":-39.53,"avg":12.59,"pnl":-9781.28},"keep_only":{"n":807,"win":61.96,"med":51.61,"avg":61.09,"pnl":13168.45},"keep_only_recent":{"n":613,"win":60.85,"med":54.55,"avg":69.38,"pnl":9130.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:51:24  INFO      Mode: exits
15:51:25  INFO        Daily log -> logs/daily/2026-09-29.md
15:51:25  INFO        Daily log reconciled -> logs/daily/2026-09-29.md (3 ledger rows)
15:51:26  INFO        Daily log -> logs/daily/2026-09-29.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:51 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.19|
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
=== options_live_micro LIVE 2026-09-29T11:51:27.059532-04:00 share=25% ===
2026-09-29 11:51:27,059 INFO === options_live_micro LIVE 2026-09-29T11:51:27.059532-04:00 share=25% ===
Live account equity $223.19 cash $223.19 #225458845 options_level=3
2026-09-29 11:51:27,307 INFO Live account equity $223.19 cash $223.19 #225458845 options_level=3
Live micro: manage/exits only
2026-09-29 11:51:27,530 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-29 11:51:27,605 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (180 earlier lines - see full log file)
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
## Ledger health — 2026-09-29
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1619 | WARN | <<<
| Missing exit records (post) |  1619 | WARN | <<<
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |   102 | INFO |
| Total closed lots           |  2623 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1567 med=-15.9% | TAINTED n=1943 med=-39.5% | KEEP-only n=807 med=+51.6% | KILL=20 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.19 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260929T155636Z

- UTC timestamp: `20260929T155636Z`
- GitHub run: [#11330](https://github.com/28twagg-ops/TradingBot/actions/runs/36593828707)
- Run id: `36593828707`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`17s`
- Full logs: `logs/action_runs/20260929T155636Z_live_bot.log`, `logs/action_runs/20260929T155636Z_live_options.log`, `logs/action_runs/20260929T155636Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1567 | 49.2 | -15.9 | +41.0 | $+19,186 |
| TAINTED | 1943 | 33.2 | -39.5 | +12.6 | $-9,781 |
| KEEP-only | 807 | 62.0 | +51.6 | +61.1 | $+13,168 |
| KEEP-only recent | 613 | 60.8 | +54.5 | +69.4 | $+9,130 |

- KEEP strategies (24): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (20): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-29T11:56:43.124068-04:00","date":"2026-09-29","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":6.6,"phases_s":{"reconcile":0.24,"cancel":0.11,"manage":4.29,"protective_stops":1.41},"signals":0,"placed":0,"equity":992176.42,"open_positions":30,"pending_orders":0,"open_lots":102,"submitted_today":80,"filled_today":74,"unattributed_contracts":0,"top_signals":[],"github_run":"11330","github_run_id":"36593828707","status":"ok","data_quality":{"clean":{"n":1567,"win":49.2,"med":-15.87,"avg":41.05,"pnl":19185.83},"tainted":{"n":1943,"win":33.25,"med":-39.53,"avg":12.59,"pnl":-9781.28},"keep_only":{"n":807,"win":61.96,"med":51.61,"avg":61.09,"pnl":13168.45},"keep_only_recent":{"n":613,"win":60.85,"med":54.55,"avg":69.38,"pnl":9130.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:56:38  INFO      Mode: exits
15:56:39  INFO        Daily log -> logs/daily/2026-09-29.md
15:56:39  INFO        Daily log reconciled -> logs/daily/2026-09-29.md (3 ledger rows)
15:56:39  INFO        Daily log -> logs/daily/2026-09-29.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:56 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.19|
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
=== options_live_micro LIVE 2026-09-29T11:56:40.253196-04:00 share=25% ===
2026-09-29 11:56:40,253 INFO === options_live_micro LIVE 2026-09-29T11:56:40.253196-04:00 share=25% ===
Live account equity $223.19 cash $223.19 #225458845 options_level=3
2026-09-29 11:56:40,649 INFO Live account equity $223.19 cash $223.19 #225458845 options_level=3
Live micro: manage/exits only
2026-09-29 11:56:40,743 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-29 11:56:40,774 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (180 earlier lines - see full log file)
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
## Ledger health — 2026-09-29
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1619 | WARN | <<<
| Missing exit records (post) |  1619 | WARN | <<<
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |   102 | INFO |
| Total closed lots           |  2623 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1567 med=-15.9% | TAINTED n=1943 med=-39.5% | KEEP-only n=807 med=+51.6% | KILL=20 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.19 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260929T160126Z

- UTC timestamp: `20260929T160126Z`
- GitHub run: [#11331](https://github.com/28twagg-ops/TradingBot/actions/runs/36594465089)
- Run id: `36594465089`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`26s`
- Full logs: `logs/action_runs/20260929T160126Z_live_bot.log`, `logs/action_runs/20260929T160126Z_live_options.log`, `logs/action_runs/20260929T160126Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1567 | 49.2 | -15.9 | +41.0 | $+19,186 |
| TAINTED | 1943 | 33.2 | -39.5 | +12.6 | $-9,781 |
| KEEP-only | 807 | 62.0 | +51.6 | +61.1 | $+13,168 |
| KEEP-only recent | 613 | 60.8 | +54.5 | +69.4 | $+9,130 |

- KEEP strategies (24): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (20): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-29T12:01:33.251653-04:00","date":"2026-09-29","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":12.1,"phases_s":{"reconcile":0.48,"cancel":0.22,"manage":7.62,"protective_stops":2.92},"signals":0,"placed":0,"equity":992065.79,"open_positions":29,"pending_orders":0,"open_lots":100,"submitted_today":80,"filled_today":74,"unattributed_contracts":0,"top_signals":[],"github_run":"11331","github_run_id":"36594465089","status":"ok","data_quality":{"clean":{"n":1567,"win":49.2,"med":-15.87,"avg":41.05,"pnl":19185.83},"tainted":{"n":1943,"win":33.25,"med":-39.53,"avg":12.59,"pnl":-9781.28},"keep_only":{"n":807,"win":61.96,"med":51.61,"avg":61.09,"pnl":13168.45},"keep_only_recent":{"n":613,"win":60.85,"med":54.55,"avg":69.38,"pnl":9130.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
16:01:26  INFO      Mode: exits
16:01:27  INFO        Daily log -> logs/daily/2026-09-29.md
16:01:27  INFO        Daily log reconciled -> logs/daily/2026-09-29.md (3 ledger rows)
16:01:28  INFO        Daily log -> logs/daily/2026-09-29.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.19|
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
=== options_live_micro LIVE 2026-09-29T12:01:29.168724-04:00 share=25% ===
2026-09-29 12:01:29,168 INFO === options_live_micro LIVE 2026-09-29T12:01:29.168724-04:00 share=25% ===
Live account equity $223.19 cash $223.19 #225458845 options_level=3
2026-09-29 12:01:29,399 INFO Live account equity $223.19 cash $223.19 #225458845 options_level=3
Live micro: manage/exits only
2026-09-29 12:01:29,608 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-29 12:01:29,678 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (183 earlier lines - see full log file)
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
## Ledger health — 2026-09-29
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1619 | WARN | <<<
| Missing exit records (post) |  1619 | WARN | <<<
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |   100 | INFO |
| Total closed lots           |  2623 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1567 med=-15.9% | TAINTED n=1943 med=-39.5% | KEEP-only n=807 med=+51.6% | KILL=20 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.19 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260929T160613Z

- UTC timestamp: `20260929T160613Z`
- GitHub run: [#11332](https://github.com/28twagg-ops/TradingBot/actions/runs/36595092917)
- Run id: `36595092917`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`16s`
- Full logs: `logs/action_runs/20260929T160613Z_live_bot.log`, `logs/action_runs/20260929T160613Z_live_options.log`, `logs/action_runs/20260929T160613Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1567 | 49.2 | -15.9 | +41.0 | $+19,186 |
| TAINTED | 1943 | 33.2 | -39.5 | +12.6 | $-9,781 |
| KEEP-only | 807 | 62.0 | +51.6 | +61.1 | $+13,168 |
| KEEP-only recent | 613 | 60.8 | +54.5 | +69.4 | $+9,130 |

- KEEP strategies (24): S163, S164, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (20): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-29T12:06:18.904090-04:00","date":"2026-09-29","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":4.6,"phases_s":{"reconcile":0.15,"cancel":0.04,"manage":3.32,"protective_stops":0.5},"signals":0,"placed":0,"equity":992220.01,"open_positions":29,"pending_orders":0,"open_lots":100,"submitted_today":80,"filled_today":74,"unattributed_contracts":0,"top_signals":[],"github_run":"11332","github_run_id":"36595092917","status":"ok","data_quality":{"clean":{"n":1567,"win":49.2,"med":-15.87,"avg":41.05,"pnl":19185.83},"tainted":{"n":1943,"win":33.25,"med":-39.53,"avg":12.59,"pnl":-9781.28},"keep_only":{"n":807,"win":61.96,"med":51.61,"avg":61.09,"pnl":13168.45},"keep_only_recent":{"n":613,"win":60.85,"med":54.55,"avg":69.38,"pnl":9130.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
16:06:14  INFO      Mode: exits
16:06:14  INFO        Daily log -> logs/daily/2026-09-29.md
16:06:14  INFO        Daily log reconciled -> logs/daily/2026-09-29.md (3 ledger rows)
16:06:14  INFO        Daily log -> logs/daily/2026-09-29.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $223.19|
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
=== options_live_micro LIVE 2026-09-29T12:06:16.205554-04:00 share=25% ===
2026-09-29 12:06:16,205 INFO === options_live_micro LIVE 2026-09-29T12:06:16.205554-04:00 share=25% ===
Live account equity $223.19 cash $223.19 #225458845 options_level=3
2026-09-29 12:06:16,250 INFO Live account equity $223.19 cash $223.19 #225458845 options_level=3
Live micro: manage/exits only
2026-09-29 12:06:16,270 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-29 12:06:16,276 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (180 earlier lines - see full log file)
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
## Ledger health — 2026-09-29
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1619 | WARN | <<<
| Missing exit records (post) |  1619 | WARN | <<<
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |   100 | INFO |
| Total closed lots           |  2623 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-29_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1567 med=-15.9% | TAINTED n=1943 med=-39.5% | KEEP-only n=807 med=+51.6% | KILL=20 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=223.19 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---
