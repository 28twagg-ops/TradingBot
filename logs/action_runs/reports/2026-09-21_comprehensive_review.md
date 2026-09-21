# Daily Comprehensive Action Review - 2026-09-21

_Auto-generated from GitHub Actions run output. Each run appends a summary; full stdout is in linked per-run log files._
## Run 20260921T130115Z

- UTC timestamp: `20260921T130115Z`
- GitHub run: [#10503](https://github.com/28twagg-ops/TradingBot/actions/runs/35602822386)
- Run id: `35602822386`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`21s`
- Full logs: `logs/action_runs/20260921T130115Z_live_bot.log`, `logs/action_runs/20260921T130115Z_live_options.log`, `logs/action_runs/20260921T130115Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T09:01:20.499276-04:00","date":"2026-09-21","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":11.1,"phases_s":{"reconcile":4.42},"signals":0,"placed":0,"equity":997158.09,"open_positions":20,"pending_orders":0,"open_lots":59,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10503","github_run_id":"35602822386","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:01:16  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.92|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $225.92|
|  Cash                                                           $158.20|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $67.72|
|  Open P&L                                                        $-0.04|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  PPG      MomReversal     $33.80     $104.75  $104.52  -0.2%   $-0.08  |
|  TJX      MomReversal     $33.91     $127.48  $127.60  +0.1%   $+0.03  |
|                                                                        |
|  Total invested                                                  $67.72|
|  Total open P&L                                                  $-0.04|
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
|  2026-09-18  SELL  YETI  EarningsDrift  $33.88  P&L $+0.01             |
|  2026-09-18  SELL  BLDR  MomReversal  $33.73  P&L $-0.26               |
|  2026-09-18  SELL  VICR  MA_Squeeze  $34.38  P&L $+0.43                |
|  2026-09-18  SELL  CIEN  MomReversal  $33.20  P&L $-0.79               |
|  2026-09-17  SELL  AMP  Pullback50  $33.90  P&L $-0.17                 |
|  2026-09-17  SELL  GLW  Pullback50  $33.94  P&L $-0.14                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-21T09:01:17.357787-04:00 share=25% ===
2026-09-21 09:01:17,357 INFO === options_live_micro LIVE 2026-09-21T09:01:17.357787-04:00 share=25% ===
Live account equity $225.92 cash $158.20 #225458845 options_level=3
2026-09-21 09:01:17,492 INFO Live account equity $225.92 cash $158.20 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-21 09:01:17,526 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-21 09:01:17,567 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (178 earlier lines - see full log file)

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
## Ledger health — 2026-09-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1430 | WARN | <<<
| Missing exit records (post) |  1427 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    59 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1367 med=-12.5% | TAINTED n=1882 med=-38.9% | KEEP-only n=751 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=225.92 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260921T130606Z

- UTC timestamp: `20260921T130606Z`
- GitHub run: [#10504](https://github.com/28twagg-ops/TradingBot/actions/runs/35603334398)
- Run id: `35603334398`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`19s`
- Full logs: `logs/action_runs/20260921T130606Z_live_bot.log`, `logs/action_runs/20260921T130606Z_live_options.log`, `logs/action_runs/20260921T130606Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T09:06:11.132438-04:00","date":"2026-09-21","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":11.5,"phases_s":{"reconcile":4.71},"signals":0,"placed":0,"equity":997158.09,"open_positions":20,"pending_orders":0,"open_lots":59,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10504","github_run_id":"35603334398","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:06:06  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.92|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $225.92|
|  Cash                                                           $158.20|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $67.72|
|  Open P&L                                                        $-0.04|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  PPG      MomReversal     $33.80     $104.75  $104.52  -0.2%   $-0.08  |
|  TJX      MomReversal     $33.91     $127.48  $127.60  +0.1%   $+0.03  |
|                                                                        |
|  Total invested                                                  $67.72|
|  Total open P&L                                                  $-0.04|
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
|  2026-09-18  SELL  YETI  EarningsDrift  $33.88  P&L $+0.01             |
|  2026-09-18  SELL  BLDR  MomReversal  $33.73  P&L $-0.26               |
|  2026-09-18  SELL  VICR  MA_Squeeze  $34.38  P&L $+0.43                |
|  2026-09-18  SELL  CIEN  MomReversal  $33.20  P&L $-0.79               |
|  2026-09-17  SELL  AMP  Pullback50  $33.90  P&L $-0.17                 |
|  2026-09-17  SELL  GLW  Pullback50  $33.94  P&L $-0.14                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-21T09:06:08.594417-04:00 share=25% ===
2026-09-21 09:06:08,594 INFO === options_live_micro LIVE 2026-09-21T09:06:08.594417-04:00 share=25% ===
Live account equity $225.92 cash $158.20 #225458845 options_level=3
2026-09-21 09:06:08,784 INFO Live account equity $225.92 cash $158.20 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-21 09:06:08,841 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-21 09:06:08,910 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)

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
## Ledger health — 2026-09-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1430 | WARN | <<<
| Missing exit records (post) |  1427 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    59 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1367 med=-12.5% | TAINTED n=1882 med=-38.9% | KEEP-only n=751 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=225.92 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260921T131104Z

- UTC timestamp: `20260921T131104Z`
- GitHub run: [#10505](https://github.com/28twagg-ops/TradingBot/actions/runs/35603851696)
- Run id: `35603851696`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`22s`
- Full logs: `logs/action_runs/20260921T131104Z_live_bot.log`, `logs/action_runs/20260921T131104Z_live_options.log`, `logs/action_runs/20260921T131104Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T09:11:09.865261-04:00","date":"2026-09-21","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":10.9,"phases_s":{"reconcile":4.18},"signals":0,"placed":0,"equity":997158.09,"open_positions":20,"pending_orders":0,"open_lots":59,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10505","github_run_id":"35603851696","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:11:05  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.92|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $225.92|
|  Cash                                                           $158.20|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $67.72|
|  Open P&L                                                        $-0.04|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  PPG      MomReversal     $33.80     $104.75  $104.52  -0.2%   $-0.08  |
|  TJX      MomReversal     $33.91     $127.48  $127.60  +0.1%   $+0.03  |
|                                                                        |
|  Total invested                                                  $67.72|
|  Total open P&L                                                  $-0.04|
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
|  2026-09-18  SELL  YETI  EarningsDrift  $33.88  P&L $+0.01             |
|  2026-09-18  SELL  BLDR  MomReversal  $33.73  P&L $-0.26               |
|  2026-09-18  SELL  VICR  MA_Squeeze  $34.38  P&L $+0.43                |
|  2026-09-18  SELL  CIEN  MomReversal  $33.20  P&L $-0.79               |
|  2026-09-17  SELL  AMP  Pullback50  $33.90  P&L $-0.17                 |
|  2026-09-17  SELL  GLW  Pullback50  $33.94  P&L $-0.14                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-21T09:11:07.168534-04:00 share=25% ===
2026-09-21 09:11:07,168 INFO === options_live_micro LIVE 2026-09-21T09:11:07.168534-04:00 share=25% ===
Live account equity $225.92 cash $158.20 #225458845 options_level=3
2026-09-21 09:11:07,229 INFO Live account equity $225.92 cash $158.20 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-21 09:11:07,247 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-21 09:11:07,258 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)

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
## Ledger health — 2026-09-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1430 | WARN | <<<
| Missing exit records (post) |  1427 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    59 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1367 med=-12.5% | TAINTED n=1882 med=-38.9% | KEEP-only n=751 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=225.92 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260921T131607Z

- UTC timestamp: `20260921T131607Z`
- GitHub run: [#10506](https://github.com/28twagg-ops/TradingBot/actions/runs/35604392571)
- Run id: `35604392571`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`21s`
- Full logs: `logs/action_runs/20260921T131607Z_live_bot.log`, `logs/action_runs/20260921T131607Z_live_options.log`, `logs/action_runs/20260921T131607Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T09:16:13.566439-04:00","date":"2026-09-21","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":11.7,"phases_s":{"reconcile":4.78},"signals":0,"placed":0,"equity":997158.09,"open_positions":20,"pending_orders":0,"open_lots":59,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10506","github_run_id":"35604392571","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:16:09  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.92|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $225.92|
|  Cash                                                           $158.20|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $67.72|
|  Open P&L                                                        $-0.04|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  PPG      MomReversal     $33.80     $104.75  $104.52  -0.2%   $-0.08  |
|  TJX      MomReversal     $33.91     $127.48  $127.60  +0.1%   $+0.03  |
|                                                                        |
|  Total invested                                                  $67.72|
|  Total open P&L                                                  $-0.04|
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
|  2026-09-18  SELL  YETI  EarningsDrift  $33.88  P&L $+0.01             |
|  2026-09-18  SELL  BLDR  MomReversal  $33.73  P&L $-0.26               |
|  2026-09-18  SELL  VICR  MA_Squeeze  $34.38  P&L $+0.43                |
|  2026-09-18  SELL  CIEN  MomReversal  $33.20  P&L $-0.79               |
|  2026-09-17  SELL  AMP  Pullback50  $33.90  P&L $-0.17                 |
|  2026-09-17  SELL  GLW  Pullback50  $33.94  P&L $-0.14                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-21T09:16:10.779946-04:00 share=25% ===
2026-09-21 09:16:10,780 INFO === options_live_micro LIVE 2026-09-21T09:16:10.779946-04:00 share=25% ===
Live account equity $225.92 cash $158.20 #225458845 options_level=3
2026-09-21 09:16:11,022 INFO Live account equity $225.92 cash $158.20 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-21 09:16:11,087 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-21 09:16:11,151 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)

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
## Ledger health — 2026-09-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1430 | WARN | <<<
| Missing exit records (post) |  1427 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    59 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1367 med=-12.5% | TAINTED n=1882 med=-38.9% | KEEP-only n=751 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=225.92 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260921T132111Z

- UTC timestamp: `20260921T132111Z`
- GitHub run: [#10507](https://github.com/28twagg-ops/TradingBot/actions/runs/35604932000)
- Run id: `35604932000`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`23s`
- Full logs: `logs/action_runs/20260921T132111Z_live_bot.log`, `logs/action_runs/20260921T132111Z_live_options.log`, `logs/action_runs/20260921T132111Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T09:21:19.006924-04:00","date":"2026-09-21","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":11.7,"phases_s":{"reconcile":4.64},"signals":0,"placed":0,"equity":997158.09,"open_positions":20,"pending_orders":0,"open_lots":59,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10507","github_run_id":"35604932000","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:21:13  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.92|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $225.92|
|  Cash                                                           $158.20|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $67.72|
|  Open P&L                                                        $-0.04|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  PPG      MomReversal     $33.80     $104.75  $104.52  -0.2%   $-0.08  |
|  TJX      MomReversal     $33.91     $127.48  $127.60  +0.1%   $+0.03  |
|                                                                        |
|  Total invested                                                  $67.72|
|  Total open P&L                                                  $-0.04|
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
|  2026-09-18  SELL  YETI  EarningsDrift  $33.88  P&L $+0.01             |
|  2026-09-18  SELL  BLDR  MomReversal  $33.73  P&L $-0.26               |
|  2026-09-18  SELL  VICR  MA_Squeeze  $34.38  P&L $+0.43                |
|  2026-09-18  SELL  CIEN  MomReversal  $33.20  P&L $-0.79               |
|  2026-09-17  SELL  AMP  Pullback50  $33.90  P&L $-0.17                 |
|  2026-09-17  SELL  GLW  Pullback50  $33.94  P&L $-0.14                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-21T09:21:15.848378-04:00 share=25% ===
2026-09-21 09:21:15,848 INFO === options_live_micro LIVE 2026-09-21T09:21:15.848378-04:00 share=25% ===
Live account equity $225.92 cash $158.20 #225458845 options_level=3
2026-09-21 09:21:16,054 INFO Live account equity $225.92 cash $158.20 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-21 09:21:16,111 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-21 09:21:16,167 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)

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
## Ledger health — 2026-09-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1430 | WARN | <<<
| Missing exit records (post) |  1427 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    59 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1367 med=-12.5% | TAINTED n=1882 med=-38.9% | KEEP-only n=751 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=225.92 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260921T132603Z

- UTC timestamp: `20260921T132603Z`
- GitHub run: [#10508](https://github.com/28twagg-ops/TradingBot/actions/runs/35605467972)
- Run id: `35605467972`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`20s`
- Full logs: `logs/action_runs/20260921T132603Z_live_bot.log`, `logs/action_runs/20260921T132603Z_live_options.log`, `logs/action_runs/20260921T132603Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T09:26:07.398042-04:00","date":"2026-09-21","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":10.7,"phases_s":{"reconcile":4.13},"signals":0,"placed":0,"equity":997158.09,"open_positions":20,"pending_orders":0,"open_lots":59,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10508","github_run_id":"35605467972","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:26:03  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.92|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $225.92|
|  Cash                                                           $158.20|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $67.72|
|  Open P&L                                                        $-0.04|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  PPG      MomReversal     $33.80     $104.75  $104.52  -0.2%   $-0.08  |
|  TJX      MomReversal     $33.91     $127.48  $127.60  +0.1%   $+0.03  |
|                                                                        |
|  Total invested                                                  $67.72|
|  Total open P&L                                                  $-0.04|
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
|  2026-09-18  SELL  YETI  EarningsDrift  $33.88  P&L $+0.01             |
|  2026-09-18  SELL  BLDR  MomReversal  $33.73  P&L $-0.26               |
|  2026-09-18  SELL  VICR  MA_Squeeze  $34.38  P&L $+0.43                |
|  2026-09-18  SELL  CIEN  MomReversal  $33.20  P&L $-0.79               |
|  2026-09-17  SELL  AMP  Pullback50  $33.90  P&L $-0.17                 |
|  2026-09-17  SELL  GLW  Pullback50  $33.94  P&L $-0.14                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-21T09:26:04.917208-04:00 share=25% ===
2026-09-21 09:26:04,917 INFO === options_live_micro LIVE 2026-09-21T09:26:04.917208-04:00 share=25% ===
Live account equity $225.92 cash $158.20 #225458845 options_level=3
2026-09-21 09:26:04,956 INFO Live account equity $225.92 cash $158.20 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-21 09:26:04,963 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-21 09:26:04,971 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)

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
## Ledger health — 2026-09-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1430 | WARN | <<<
| Missing exit records (post) |  1427 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    59 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1367 med=-12.5% | TAINTED n=1882 med=-38.9% | KEEP-only n=751 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=225.92 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260921T133119Z

- UTC timestamp: `20260921T133119Z`
- GitHub run: [#10509](https://github.com/28twagg-ops/TradingBot/actions/runs/35606006886)
- Run id: `35606006886`
- Live bot: exit=`0`, duration=`217s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260921T133119Z_live_bot.log`, `logs/action_runs/20260921T133119Z_live_options.log`, `logs/action_runs/20260921T133119Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T09:26:07.398042-04:00","date":"2026-09-21","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":10.7,"phases_s":{"reconcile":4.13},"signals":0,"placed":0,"equity":997158.09,"open_positions":20,"pending_orders":0,"open_lots":59,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10508","github_run_id":"35605467972","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:31:21  INFO      Mode: morning_prep
13:31:22  INFO        [prep_positions] 2/2 (2 valid)
13:31:22  INFO      Fetching tickers (universe=both)...
13:31:22  INFO        S&P 500: 503
13:31:22  INFO        MidCap 400: 400
13:31:22  INFO        Total: 901 tickers
13:31:23  INFO        [prep_universe] 40/899 (40 valid)
13:31:25  INFO        [prep_universe] 80/899 (80 valid)
13:31:26  INFO        [prep_universe] 120/899 (120 valid)
13:31:27  INFO        [prep_universe] 160/899 (160 valid)
13:31:28  INFO        [prep_universe] 200/899 (199 valid)
13:31:35  INFO        [prep_universe] 240/899 (238 valid)
13:31:48  INFO        [prep_universe] 280/899 (278 valid)
13:31:58  INFO        [prep_universe] 320/899 (318 valid)
13:32:11  INFO        [prep_universe] 360/899 (358 valid)
13:32:24  INFO        [prep_universe] 400/899 (398 valid)
13:32:37  INFO        [prep_universe] 440/899 (438 valid)
13:32:47  INFO        [prep_universe] 480/899 (478 valid)
13:33:00  INFO        [prep_universe] 520/899 (518 valid)
13:33:13  INFO        [prep_universe] 560/899 (558 valid)
13:33:23  INFO        [prep_universe] 600/899 (598 valid)
13:33:36  INFO        [prep_universe] 640/899 (638 valid)
13:33:46  INFO        [prep_universe] 680/899 (678 valid)
13:33:59  INFO        [prep_universe] 720/899 (718 valid)
13:34:12  INFO        [prep_universe] 760/899 (758 valid)
13:34:25  INFO        [prep_universe] 800/899 (798 valid)
13:34:35  INFO        [prep_universe] 840/899 (838 valid)
13:34:48  INFO        [prep_universe] 880/899 (878 valid)
13:34:54  INFO        [prep_universe] 899/899 (897 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.22|
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
|  Invested                                                        $68.02|
|  Open P&L                                                        $+0.26|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  PPG      MomReversal     $33.95     $104.75  $104.98  +0.2%   $+0.07  |
|  TJX      MomReversal     $34.06     $127.48  $128.18  +0.5%   $+0.18  |
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
|  Signal candidates                                                   26|
|  Universe scanned                                                   899|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-21T09:34:56.770826-04:00 share=25% ===
2026-09-21 09:34:56,770 INFO === options_live_micro LIVE 2026-09-21T09:34:56.770826-04:00 share=25% ===
Live account equity $226.28 cash $158.20 #225458845 options_level=3
2026-09-21 09:34:56,890 INFO Live account equity $226.28 cash $158.20 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-21 09:34:57,046 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-21 09:34:57,108 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=59 paper_keys=yes dry_run=False
  alpaca positions=20
  FLAG b857|S408|900c4578 missing from Alpaca
  FLAG b856|S408|be48d4c7 missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE FAIL: {"code":50010000,"message":"internal server error occurred"}
paper probe failed (non-fatal)
=== options_morning_bot (PAPER) 2026-09-21T09:34:59.185426-04:00 ===

[Run context]
2026-09-21 09:34:59,303 WARNING paper get_account failed attempt 1/3 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 2s
2026-09-21 09:35:01,355 WARNING paper get_account failed attempt 2/3 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 4s
2026-09-21 09:35:05,402 ERROR paper get_account failed after 3 attempts: {"code":50010000,"message":"internal server error occurred"}
WARN: get_account failed ({"code":50010000,"message":"internal server error occurred"}) but positions OK (n=20). Keys are fine; Alpaca account endpoint is flaky. Using cached equity $997158.09.
2026-09-21 09:35:05,515 WARNING paper get_account failed attempt 1/2 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 2s
2026-09-21 09:35:07,560 ERROR paper get_account failed after 2 attempts: {"code":50010000,"message":"internal server error occurred"}
WARN: using cached paper equity $997158.09 (get_account: {"code":50010000,"message":"internal server error occurred"})
2026-09-21 09:35:07,620 WARNING lab get_account failed attempt 1/2: {"code":50010000,"message":"internal server error occurred"}
2026-09-21 09:35:09,680 ERROR lab get_account failed after 2 attempts: {"code":50010000,"message":"internal server error occurred"}

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
  EXIT [b434|lab0434_s366_w2_1005_1045_r1|S366] take_profit (+194.0%) SELL failed MARA260925C00012500: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b433|lab0433_s366_w1_0928_1005_r2|S366] take_profit (+194.0%) SELL failed MARA260925C00012500: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b432|lab0432_s366_w1_0928_1005_r1|S366] take_profit (+194.0%) SELL failed MARA260925C00012500: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b166|lab0166_s216_w2_1005_1045_r1|S216] stop_loss (-57.1%) SELL failed CELH260925C00029500: {"code":50010000,"message":"internal server error occurred"}
```

---

## Run 20260921T133654Z

- UTC timestamp: `20260921T133654Z`
- GitHub run: [#10510](https://github.com/28twagg-ops/TradingBot/actions/runs/35606540593)
- Run id: `35606540593`
- Live bot: exit=`0`, duration=`217s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260921T133654Z_live_bot.log`, `logs/action_runs/20260921T133654Z_live_options.log`, `logs/action_runs/20260921T133654Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T09:26:07.398042-04:00","date":"2026-09-21","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":10.7,"phases_s":{"reconcile":4.13},"signals":0,"placed":0,"equity":997158.09,"open_positions":20,"pending_orders":0,"open_lots":59,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10508","github_run_id":"35605467972","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:36:56  INFO      Mode: morning_prep
13:36:57  INFO        [prep_positions] 2/2 (2 valid)
13:36:57  INFO      Fetching tickers (universe=both)...
13:36:58  INFO        S&P 500: 503
13:36:58  INFO        MidCap 400: 400
13:36:58  INFO        Total: 901 tickers
13:36:59  INFO        [prep_universe] 40/899 (40 valid)
13:37:01  INFO        [prep_universe] 80/899 (80 valid)
13:37:02  INFO        [prep_universe] 120/899 (120 valid)
13:37:03  INFO        [prep_universe] 160/899 (160 valid)
13:37:05  INFO        [prep_universe] 200/899 (199 valid)
13:37:12  INFO        [prep_universe] 240/899 (238 valid)
13:37:25  INFO        [prep_universe] 280/899 (278 valid)
13:37:36  INFO        [prep_universe] 320/899 (318 valid)
13:37:49  INFO        [prep_universe] 360/899 (358 valid)
13:37:59  INFO        [prep_universe] 400/899 (398 valid)
13:38:12  INFO        [prep_universe] 440/899 (438 valid)
13:38:23  INFO        [prep_universe] 480/899 (478 valid)
13:38:36  INFO        [prep_universe] 520/899 (518 valid)
13:38:49  INFO        [prep_universe] 560/899 (558 valid)
13:38:59  INFO        [prep_universe] 600/899 (598 valid)
13:39:13  INFO        [prep_universe] 640/899 (638 valid)
13:39:23  INFO        [prep_universe] 680/899 (678 valid)
13:39:36  INFO        [prep_universe] 720/899 (718 valid)
13:39:47  INFO        [prep_universe] 760/899 (758 valid)
13:40:00  INFO        [prep_universe] 800/899 (798 valid)
13:40:13  INFO        [prep_universe] 840/899 (838 valid)
13:40:23  INFO        [prep_universe] 880/899 (878 valid)
13:40:30  INFO        [prep_universe] 899/899 (897 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.45|
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
|  Invested                                                        $68.25|
|  Open P&L                                                        $+0.49|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  PPG      MomReversal     $33.99     $104.75  $105.08  +0.3%   $+0.11  |
|  TJX      MomReversal     $34.26     $127.48  $128.93  +1.1%   $+0.38  |
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
|  Signal candidates                                                   24|
|  Universe scanned                                                   899|
+========================================================================+
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20260921T134159Z

- UTC timestamp: `20260921T134159Z`
- GitHub run: [#10511](https://github.com/28twagg-ops/TradingBot/actions/runs/35607075332)
- Run id: `35607075332`
- Live bot: exit=`0`, duration=`215s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260921T134159Z_live_bot.log`, `logs/action_runs/20260921T134159Z_live_options.log`, `logs/action_runs/20260921T134159Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T09:26:07.398042-04:00","date":"2026-09-21","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":10.7,"phases_s":{"reconcile":4.13},"signals":0,"placed":0,"equity":997158.09,"open_positions":20,"pending_orders":0,"open_lots":59,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10508","github_run_id":"35605467972","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:42:00  INFO      Mode: morning_prep
13:42:01  INFO        [prep_positions] 2/2 (2 valid)
13:42:01  INFO        Universe cache hit: 901 tickers (tickers_2026-09-21.json)
13:42:02  INFO        [prep_universe] 40/899 (40 valid)
13:42:04  INFO        [prep_universe] 80/899 (80 valid)
13:42:05  INFO        [prep_universe] 120/899 (120 valid)
13:42:06  INFO        [prep_universe] 160/899 (160 valid)
13:42:08  INFO        [prep_universe] 200/899 (199 valid)
13:42:15  INFO        [prep_universe] 240/899 (238 valid)
13:42:28  INFO        [prep_universe] 280/899 (278 valid)
13:42:39  INFO        [prep_universe] 320/899 (318 valid)
13:42:52  INFO        [prep_universe] 360/899 (358 valid)
13:43:02  INFO        [prep_universe] 400/899 (398 valid)
13:43:15  INFO        [prep_universe] 440/899 (438 valid)
13:43:26  INFO        [prep_universe] 480/899 (478 valid)
13:43:39  INFO        [prep_universe] 520/899 (518 valid)
13:43:50  INFO        [prep_universe] 560/899 (558 valid)
13:44:03  INFO        [prep_universe] 600/899 (598 valid)
13:44:16  INFO        [prep_universe] 640/899 (638 valid)
13:44:26  INFO        [prep_universe] 680/899 (678 valid)
13:44:40  INFO        [prep_universe] 720/899 (718 valid)
13:44:50  INFO        [prep_universe] 760/899 (758 valid)
13:45:03  INFO        [prep_universe] 800/899 (798 valid)
13:45:14  INFO        [prep_universe] 840/899 (838 valid)
13:45:28  INFO        [prep_universe] 880/899 (878 valid)
13:45:32  INFO        [prep_universe] 899/899 (897 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:42 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.24|
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
|  Invested                                                        $68.03|
|  Open P&L                                                        $+0.27|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  PPG      MomReversal     $33.81     $104.75  $104.54  -0.2%   $-0.07  |
|  TJX      MomReversal     $34.22     $127.48  $128.77  +1.0%   $+0.34  |
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
|  Signal candidates                                                   14|
|  Universe scanned                                                   899|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-21T09:45:35.413750-04:00 share=25% ===
2026-09-21 09:45:35,413 INFO === options_live_micro LIVE 2026-09-21T09:45:35.413750-04:00 share=25% ===
Live account equity $226.17 cash $158.20 #225458845 options_level=3
2026-09-21 09:45:35,635 INFO Live account equity $226.17 cash $158.20 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-21 09:45:35,845 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-21 09:45:35,982 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=57 paper_keys=yes dry_run=False
  alpaca positions=17
  FLAG b263|S403|6d60396d missing from Alpaca
  FLAG b262|S403|2ab6f725 missing from Alpaca
  FLAG b859|S408|c6e24356 missing from Alpaca
  FLAG b863|S408|96caf8a7 missing from Alpaca
  FLAG b862|S408|392891dd missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE FAIL: {"code":50010000,"message":"internal server error occurred"}
paper probe failed (non-fatal)
=== options_morning_bot (PAPER) 2026-09-21T09:45:39.259381-04:00 ===

[Run context]
2026-09-21 09:45:39,490 WARNING paper get_account failed attempt 1/3 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 2s
2026-09-21 09:45:41,566 WARNING paper get_account failed attempt 2/3 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 4s
2026-09-21 09:45:45,651 ERROR paper get_account failed after 3 attempts: {"code":50010000,"message":"internal server error occurred"}
WARN: get_account failed ({"code":50010000,"message":"internal server error occurred"}) but positions OK (n=17). Keys are fine; Alpaca account endpoint is flaky. Using cached equity $997158.09.
2026-09-21 09:45:45,812 WARNING paper get_account failed attempt 1/2 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 2s
2026-09-21 09:45:47,885 ERROR paper get_account failed after 2 attempts: {"code":50010000,"message":"internal server error occurred"}
WARN: using cached paper equity $997158.09 (get_account: {"code":50010000,"message":"internal server error occurred"})
2026-09-21 09:45:48,004 WARNING lab get_account failed attempt 1/2: {"code":50010000,"message":"internal server error occurred"}
2026-09-21 09:45:50,081 ERROR lab get_account failed after 2 attempts: {"code":50010000,"message":"internal server error occurred"}

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
  EXIT [b165|lab0165_s216_w1_0928_1005_r2|S216] stop_loss (-50.9%) SELL failed CELH260925C00029000: {"code":50010000,"message":"internal server error occurred"}
```

---

## Run 20260921T134722Z

- UTC timestamp: `20260921T134722Z`
- GitHub run: [#10512](https://github.com/28twagg-ops/TradingBot/actions/runs/35607608853)
- Run id: `35607608853`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260921T134722Z_live_bot.log`, `logs/action_runs/20260921T134722Z_live_options.log`, `logs/action_runs/20260921T134722Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T09:26:07.398042-04:00","date":"2026-09-21","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":10.7,"phases_s":{"reconcile":4.13},"signals":0,"placed":0,"equity":997158.09,"open_positions":20,"pending_orders":0,"open_lots":59,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10508","github_run_id":"35605467972","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:47:24  INFO      Mode: morning_scan
13:47:24  INFO        [positions] 2/2 (2 valid)
13:47:24  INFO        SELL MARKET [urgent] PPG closed
13:47:26  INFO        TX logged: SELL PPG  P&L -0.67%
13:47:26  INFO        SELL LIMIT TJX  qty=0.26575884  limit=$128.92  id=201a8168-9269-4134-9d7e-a97bdc38481b
13:47:46  INFO        SELL LIMIT filled TJX (confirmed by position check)
13:47:46  INFO        TX logged: SELL TJX  P&L 1.17%
13:47:46  INFO        Universe cache hit: 901 tickers (tickers_2026-09-21.json)
13:47:47  INFO        [universe] 40/901 (40 valid)
13:47:48  INFO        [universe] 80/901 (80 valid)
13:47:49  INFO        [universe] 120/901 (120 valid)
13:47:51  INFO        [universe] 160/901 (160 valid)
13:47:52  INFO        [universe] 200/901 (199 valid)
13:48:01  INFO        [universe] 240/901 (238 valid)
13:48:11  INFO        [universe] 280/901 (278 valid)
13:48:24  INFO        [universe] 320/901 (318 valid)
13:48:37  INFO        [universe] 360/901 (358 valid)
13:48:47  INFO        [universe] 400/901 (398 valid)
13:49:00  INFO        [universe] 440/901 (438 valid)
13:49:12  INFO        [universe] 480/901 (478 valid)
13:49:25  INFO        [universe] 520/901 (518 valid)
13:49:35  INFO        [universe] 560/901 (558 valid)
13:49:48  INFO        [universe] 600/901 (598 valid)
13:50:01  INFO        [universe] 640/901 (638 valid)
13:50:11  INFO        [universe] 680/901 (678 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20260921T135703Z

- UTC timestamp: `20260921T135703Z`
- GitHub run: [#10514](https://github.com/28twagg-ops/TradingBot/actions/runs/35608664749)
- Run id: `35608664749`
- Live bot: exit=`0`, duration=`217s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260921T135703Z_live_bot.log`, `logs/action_runs/20260921T135703Z_live_options.log`, `logs/action_runs/20260921T135703Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T09:26:07.398042-04:00","date":"2026-09-21","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":10.7,"phases_s":{"reconcile":4.13},"signals":0,"placed":0,"equity":997158.09,"open_positions":20,"pending_orders":0,"open_lots":59,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10508","github_run_id":"35605467972","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
... (76 earlier lines - see full log file)
|  Buys today: 0  |  entry cap: 0  |  max open: 3                        |
+========================================================================+

+========================================================================+
|                               PLAN CACHE                               |
+========================================================================+
|  Mode                                                           morning|
|  File                                      logs/plans/morning_plan.json|
|  Use cached plan                                   no (stale (4336.6m))|
+========================================================================+

+========================================================================+
|          EXIT EVALUATION  (EOD -- midline + stop + max-hold)           |
+========================================================================+
|  EQIX  P&L -0.1%  $-0.05                                           HOLD|
|  DRI  P&L -0.0%  $-0.01                                            HOLD|
|  SCHW  P&L +0.1%  $+0.03                                           HOLD|
+========================================================================+

+========================================================================+
|                           EXIT EVAL SUMMARY                            |
+========================================================================+
|  Exit eval    attempted 0 | filled 0 | partial 0 | pending 0 | failed 0|
|  Other skips     already logged today 0  |  no price data 0  |  holds 3|
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
|  Source                                                       live scan|
+========================================================================+

+========================================================================+
|                          SIGNALS FOUND  --  6                          |
+========================================================================+
|  TICKER   STRATEGY        TIER   PRICE    RSI    VOL_Z   TRIGGER       |
+------------------------------------------------------------------------+
|  KMI      Pullback50      eq     $31.64   42.8   -1.73   50MA bounce (-|
|  AFG      Pullback50      eq     $142.37  49.2   -1.49   50MA bounce (-|
|  BMRN     Pullback50      eq     $64.39   46.4   -2.08   50MA bounce (+|
|  EGP      Pullback50      eq     $203.50  60.7   -1.34   50MA bounce (-|
|  ESNT     Pullback50      eq     $67.99   53.2   -1.49   50MA bounce (+|
|  NWE      Pullback50      eq     $70.53   56.3   -2.10   50MA bounce (-|
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
|  Scanned                                                            896|
|  Signals                                                              6|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  0 unconfirmed|
|  Exits                                                                0|
|  Open pos                                                             3|14:00:40  INFO        Daily log -> logs/daily/2026-09-21.md
14:00:40  INFO        Dashboard written → logs/dashboard.md

|  Equity                                                         $226.16|
|  Cash                                                           $124.40|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-21T10:00:41.186131-04:00 share=25% ===
2026-09-21 10:00:41,186 INFO === options_live_micro LIVE 2026-09-21T10:00:41.186131-04:00 share=25% ===
Live account equity $226.16 cash $124.40 #225458845 options_level=3
2026-09-21 10:00:41,391 INFO Live account equity $226.16 cash $124.40 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-21 10:00:41,566 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-21 10:00:41,683 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=59 paper_keys=yes dry_run=False
  alpaca positions=16
  FLAG b263|S403|6d60396d missing from Alpaca
  FLAG b262|S403|2ab6f725 missing from Alpaca
  FLAG b857|S408|900c4578 missing from Alpaca
  FLAG b856|S408|be48d4c7 missing from Alpaca
  FLAG b859|S408|c6e24356 missing from Alpaca
  FLAG b833|S406|36a270eb missing from Alpaca
  FLAG b832|S406|b8c8ee94 missing from Alpaca
  FLAG b863|S408|96caf8a7 missing from Alpaca
  FLAG b862|S408|392891dd missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE FAIL: {"code":50010000,"message":"internal server error occurred"}
paper probe failed (non-fatal)
=== options_morning_bot (PAPER) 2026-09-21T10:00:44.721005-04:00 ===

[Run context]
2026-09-21 10:00:45,039 WARNING paper get_account failed attempt 1/3 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 2s
2026-09-21 10:00:47,107 WARNING paper get_account failed attempt 2/3 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 4s
2026-09-21 10:00:51,191 ERROR paper get_account failed after 3 attempts: {"code":50010000,"message":"internal server error occurred"}
WARN: get_account failed ({"code":50010000,"message":"internal server error occurred"}) but positions OK (n=16). Keys are fine; Alpaca account endpoint is flaky. Using cached equity $997158.09.
2026-09-21 10:00:51,329 WARNING paper get_account failed attempt 1/2 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 2s
2026-09-21 10:00:53,391 ERROR paper get_account failed after 2 attempts: {"code":50010000,"message":"internal server error occurred"}
WARN: using cached paper equity $997158.09 (get_account: {"code":50010000,"message":"internal server error occurred"})
2026-09-21 10:00:53,481 WARNING lab get_account failed attempt 1/2: {"code":50010000,"message":"internal server error occurred"}
2026-09-21 10:00:55,560 ERROR lab get_account failed after 2 attempts: {"code":50010000,"message":"internal server error occurred"}

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
  EXIT [b434|lab0434_s366_w2_1005_1045_r1|S366] take_profit (+137.6%) SELL failed MARA260925C00012500: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b433|lab0433_s366_w1_0928_1005_r2|S366] take_profit (+137.6%) SELL failed MARA260925C00012500: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b432|lab0432_s366_w1_0928_1005_r1|S366] take_profit (+137.6%) SELL failed MARA260925C00012500: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b239|lab0239_s401_w3_1045_1120_r2|S401] stop_loss (-84.1%) SELL failed MDT260925C00094000: {"code":50010000,"message":"internal server error occurred"}
  EXIT [b238|lab0238_s401_w3_1045_1120_r1|S401] stop_loss (-84.1%) SELL failed MDT260925C00094000: {"code":50010000,"message":"internal server error occurred"}
  EXIT [b241|lab0241_s401_w4_1120_1135_r2|S401] stop_loss (-84.1%) SELL failed MDT260925C00094000: {"code":50010000,"message":"internal server error occurred"}
  EXIT [b240|lab0240_s401_w4_1120_1135_r1|S401] stop_loss (-84.1%) SELL failed MDT260925C00094000: {"code":50010000,"message":"internal server error occurred"}
```

---

## Run 20260921T140246Z

- UTC timestamp: `20260921T140246Z`
- GitHub run: [#10515](https://github.com/28twagg-ops/TradingBot/actions/runs/35609201157)
- Run id: `35609201157`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`136s`
- Full logs: `logs/action_runs/20260921T140246Z_live_bot.log`, `logs/action_runs/20260921T140246Z_live_options.log`, `logs/action_runs/20260921T140246Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T10:02:54.715112-04:00","date":"2026-09-21","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":123.7,"phases_s":{"reconcile":2.6,"cancel":0.14,"manage":42.15,"protective_stops":2.96,"scan":56.66,"entries":9.97},"signals":59,"placed":0,"equity":997158.09,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":["S165:CRWD","S164:CRWD","S168:CRWD","S167:CRWD","S163:CRWD","S209:CRWD","S350:CRWD","S351:CRWD"],"github_run":"10515","github_run_id":"35609201157","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:02:47  INFO      Mode: exits
14:02:48  INFO        Daily log -> logs/daily/2026-09-21.md
14:02:48  INFO        Daily log reconciled -> logs/daily/2026-09-21.md (2 ledger rows)
14:02:48  INFO        place_all_stops: checking 3 positions...
14:02:48  INFO        STOP skipped DRI: fractional (0.1604 shares) — software exit will handle it
14:02:48  INFO        STOP skipped EQIX: fractional (0.0327 shares) — software exit will handle it
14:02:48  INFO        STOP skipped SCHW: fractional (0.3194 shares) — software exit will handle it
14:02:49  INFO        [positions] 3/3 (3 valid)
14:02:49  INFO        Daily log -> logs/daily/2026-09-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:02 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.26|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  SCHW  P&L -0.0%  $-0.01                                           HOLD|
|  DRI  P&L +0.1%  $+0.03                                            HOLD|
|  EQIX  P&L +0.4%  $+0.14                                           HOLD|
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
=== options_live_micro LIVE 2026-09-21T10:02:50.526448-04:00 share=25% ===
2026-09-21 10:02:50,526 INFO === options_live_micro LIVE 2026-09-21T10:02:50.526448-04:00 share=25% ===
Live account equity $226.26 cash $124.40 #225458845 options_level=3
2026-09-21 10:02:50,753 INFO Live account equity $226.26 cash $124.40 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-21 10:02:50,972 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-21 10:02:51,109 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (201 earlier lines - see full log file)

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
## Ledger health — 2026-09-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1430 | WARN | <<<
| Missing exit records (post) |  1427 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1367 med=-12.5% | TAINTED n=1882 med=-38.9% | KEEP-only n=751 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.26 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260921T140630Z

- UTC timestamp: `20260921T140630Z`
- GitHub run: [#10516](https://github.com/28twagg-ops/TradingBot/actions/runs/35609747718)
- Run id: `35609747718`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`113s`
- Full logs: `logs/action_runs/20260921T140630Z_live_bot.log`, `logs/action_runs/20260921T140630Z_live_options.log`, `logs/action_runs/20260921T140630Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T10:06:36.785641-04:00","date":"2026-09-21","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":100.6,"phases_s":{"reconcile":2.13,"cancel":0.03,"manage":27.97,"protective_stops":0.71,"scan":57.2,"entries":3.91},"signals":57,"placed":0,"equity":997158.09,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":["S165:CRWD","S164:CRWD","S168:CRWD","S167:CRWD","S163:CRWD","S209:CRWD","S350:CRWD","S351:CRWD"],"github_run":"10516","github_run_id":"35609747718","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:06:31  INFO      Mode: exits
14:06:32  INFO        Daily log -> logs/daily/2026-09-21.md
14:06:32  INFO        Daily log reconciled -> logs/daily/2026-09-21.md (2 ledger rows)
14:06:32  INFO        place_all_stops: checking 3 positions...
14:06:32  INFO        STOP skipped DRI: fractional (0.1604 shares) — software exit will handle it
14:06:32  INFO        STOP skipped EQIX: fractional (0.0327 shares) — software exit will handle it
14:06:32  INFO        STOP skipped SCHW: fractional (0.3194 shares) — software exit will handle it
14:06:32  INFO        [positions] 3/3 (3 valid)
14:06:32  INFO        Daily log -> logs/daily/2026-09-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.16|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  SCHW  P&L +0.0%  $+0.01                                           HOLD|
|  EQIX  P&L +0.0%  $+0.01                                           HOLD|
|  DRI  P&L +0.1%  $+0.04                                            HOLD|
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
=== options_live_micro LIVE 2026-09-21T10:06:33.570368-04:00 share=25% ===
2026-09-21 10:06:33,570 INFO === options_live_micro LIVE 2026-09-21T10:06:33.570368-04:00 share=25% ===
Live account equity $226.16 cash $124.40 #225458845 options_level=3
2026-09-21 10:06:33,629 INFO Live account equity $226.16 cash $124.40 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-21 10:06:33,667 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-21 10:06:33,690 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (198 earlier lines - see full log file)

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
## Ledger health — 2026-09-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1430 | WARN | <<<
| Missing exit records (post) |  1427 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1367 med=-12.5% | TAINTED n=1882 med=-38.9% | KEEP-only n=751 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.16 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260921T141110Z

- UTC timestamp: `20260921T141110Z`
- GitHub run: [#10517](https://github.com/28twagg-ops/TradingBot/actions/runs/35610312978)
- Run id: `35610312978`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`132s`
- Full logs: `logs/action_runs/20260921T141110Z_live_bot.log`, `logs/action_runs/20260921T141110Z_live_options.log`, `logs/action_runs/20260921T141110Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T10:11:17.336747-04:00","date":"2026-09-21","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":119.7,"phases_s":{"reconcile":2.58,"cancel":0.15,"manage":32.71,"protective_stops":3.02,"scan":53.78,"entries":18.31},"signals":59,"placed":0,"equity":997158.09,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":["S165:CRWD","S164:CRWD","S168:CRWD","S167:CRWD","S163:CRWD","S209:CRWD","S350:CRWD","S351:CRWD"],"github_run":"10517","github_run_id":"35610312978","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:11:11  INFO      Mode: exits
14:11:12  INFO        Daily log -> logs/daily/2026-09-21.md
14:11:12  INFO        Daily log reconciled -> logs/daily/2026-09-21.md (2 ledger rows)
14:11:12  INFO        place_all_stops: checking 3 positions...
14:11:12  INFO        STOP skipped DRI: fractional (0.1604 shares) — software exit will handle it
14:11:12  INFO        STOP skipped EQIX: fractional (0.0327 shares) — software exit will handle it
14:11:12  INFO        STOP skipped SCHW: fractional (0.3194 shares) — software exit will handle it
14:11:12  INFO        [positions] 3/3 (3 valid)
14:11:13  INFO        Daily log -> logs/daily/2026-09-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.24|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  EQIX  P&L +0.0%  $+0.00                                           HOLD|
|  SCHW  P&L +0.0%  $+0.01                                           HOLD|
|  DRI  P&L +0.4%  $+0.13                                            HOLD|
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
=== options_live_micro LIVE 2026-09-21T10:11:13.821069-04:00 share=25% ===
2026-09-21 10:11:13,821 INFO === options_live_micro LIVE 2026-09-21T10:11:13.821069-04:00 share=25% ===
Live account equity $226.24 cash $124.40 #225458845 options_level=3
2026-09-21 10:11:14,050 INFO Live account equity $226.24 cash $124.40 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-21 10:11:14,259 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-21 10:11:14,399 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (199 earlier lines - see full log file)

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
## Ledger health — 2026-09-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1430 | WARN | <<<
| Missing exit records (post) |  1427 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1367 med=-12.5% | TAINTED n=1882 med=-38.9% | KEEP-only n=751 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.24 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260921T141613Z

- UTC timestamp: `20260921T141613Z`
- GitHub run: [#10518](https://github.com/28twagg-ops/TradingBot/actions/runs/35610879276)
- Run id: `35610879276`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`115s`
- Full logs: `logs/action_runs/20260921T141613Z_live_bot.log`, `logs/action_runs/20260921T141613Z_live_options.log`, `logs/action_runs/20260921T141613Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T10:16:19.424618-04:00","date":"2026-09-21","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":102.9,"phases_s":{"reconcile":2.41,"cancel":0.1,"manage":31.77,"protective_stops":2.1,"scan":45.0,"entries":12.46},"signals":59,"placed":0,"equity":997158.09,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":["S165:CRWD","S164:CRWD","S168:CRWD","S167:CRWD","S163:CRWD","S209:CRWD","S350:CRWD","S351:CRWD"],"github_run":"10518","github_run_id":"35610879276","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:16:14  INFO      Mode: exits
14:16:14  INFO        Daily log -> logs/daily/2026-09-21.md
14:16:14  INFO        Daily log reconciled -> logs/daily/2026-09-21.md (2 ledger rows)
14:16:14  INFO        place_all_stops: checking 3 positions...
14:16:14  INFO        STOP skipped DRI: fractional (0.1604 shares) — software exit will handle it
14:16:14  INFO        STOP skipped EQIX: fractional (0.0327 shares) — software exit will handle it
14:16:14  INFO        STOP skipped SCHW: fractional (0.3194 shares) — software exit will handle it
14:16:14  INFO        [positions] 3/3 (3 valid)
14:16:15  INFO        Daily log -> logs/daily/2026-09-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.40|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  SCHW  P&L +0.1%  $+0.03                                           HOLD|
|  EQIX  P&L +0.2%  $+0.08                                           HOLD|
|  DRI  P&L +0.5%  $+0.19                                            HOLD|
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
=== options_live_micro LIVE 2026-09-21T10:16:15.972081-04:00 share=25% ===
2026-09-21 10:16:15,972 INFO === options_live_micro LIVE 2026-09-21T10:16:15.972081-04:00 share=25% ===
Live account equity $226.40 cash $124.40 #225458845 options_level=3
2026-09-21 10:16:16,117 INFO Live account equity $226.40 cash $124.40 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-21 10:16:16,233 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-21 10:16:16,313 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (205 earlier lines - see full log file)

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
## Ledger health — 2026-09-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1430 | WARN | <<<
| Missing exit records (post) |  1427 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1367 med=-12.5% | TAINTED n=1882 med=-38.9% | KEEP-only n=751 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.4 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260921T142115Z

- UTC timestamp: `20260921T142115Z`
- GitHub run: [#10519](https://github.com/28twagg-ops/TradingBot/actions/runs/35611441018)
- Run id: `35611441018`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`129s`
- Full logs: `logs/action_runs/20260921T142115Z_live_bot.log`, `logs/action_runs/20260921T142115Z_live_options.log`, `logs/action_runs/20260921T142115Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T10:21:24.338373-04:00","date":"2026-09-21","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":117.6,"phases_s":{"reconcile":2.49,"cancel":0.12,"manage":36.64,"protective_stops":2.49,"scan":52.59,"entries":14.28},"signals":59,"placed":0,"equity":997158.09,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":["S165:CRWD","S164:CRWD","S168:CRWD","S167:CRWD","S163:CRWD","S209:CRWD","S350:CRWD","S351:CRWD"],"github_run":"10519","github_run_id":"35611441018","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:21:18  INFO      Mode: exits
14:21:19  INFO        Daily log -> logs/daily/2026-09-21.md
14:21:19  INFO        Daily log reconciled -> logs/daily/2026-09-21.md (2 ledger rows)
14:21:19  INFO        place_all_stops: checking 3 positions...
14:21:19  INFO        STOP skipped DRI: fractional (0.1604 shares) — software exit will handle it
14:21:19  INFO        STOP skipped EQIX: fractional (0.0327 shares) — software exit will handle it
14:21:19  INFO        STOP skipped SCHW: fractional (0.3194 shares) — software exit will handle it
14:21:19  INFO        [positions] 3/3 (3 valid)
14:21:20  INFO        Daily log -> logs/daily/2026-09-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.55|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  SCHW  P&L +0.2%  $+0.06                                           HOLD|
|  EQIX  P&L +0.3%  $+0.09                                           HOLD|
|  DRI  P&L +0.9%  $+0.30                                            HOLD|
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
=== options_live_micro LIVE 2026-09-21T10:21:21.008666-04:00 share=25% ===
2026-09-21 10:21:21,008 INFO === options_live_micro LIVE 2026-09-21T10:21:21.008666-04:00 share=25% ===
Live account equity $226.55 cash $124.40 #225458845 options_level=3
2026-09-21 10:21:21,208 INFO Live account equity $226.55 cash $124.40 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-21 10:21:21,382 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-21 10:21:21,502 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (202 earlier lines - see full log file)

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
## Ledger health — 2026-09-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1430 | WARN | <<<
| Missing exit records (post) |  1427 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1367 med=-12.5% | TAINTED n=1882 med=-38.9% | KEEP-only n=751 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.53 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260921T142825Z

- UTC timestamp: `20260921T142825Z`
- GitHub run: [#10520](https://github.com/28twagg-ops/TradingBot/actions/runs/35612008069)
- Run id: `35612008069`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`92s`
- Full logs: `logs/action_runs/20260921T142825Z_live_bot.log`, `logs/action_runs/20260921T142825Z_live_options.log`, `logs/action_runs/20260921T142825Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T10:28:32.349806-04:00","date":"2026-09-21","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":84.5,"phases_s":{"reconcile":2.27,"cancel":0.07,"manage":34.44,"protective_stops":1.38,"scan":29.12,"entries":8.6},"signals":59,"placed":0,"equity":997158.09,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":["S165:CRWD","S164:CRWD","S168:CRWD","S167:CRWD","S163:CRWD","S209:CRWD","S350:CRWD","S351:CRWD"],"github_run":"10520","github_run_id":"35612008069","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:28:27  INFO      Mode: exits
14:28:28  INFO        Daily log -> logs/daily/2026-09-21.md
14:28:28  INFO        Daily log reconciled -> logs/daily/2026-09-21.md (2 ledger rows)
14:28:28  INFO        place_all_stops: checking 3 positions...
14:28:28  INFO        STOP skipped DRI: fractional (0.1604 shares) — software exit will handle it
14:28:28  INFO        STOP skipped EQIX: fractional (0.0327 shares) — software exit will handle it
14:28:28  INFO        STOP skipped SCHW: fractional (0.3194 shares) — software exit will handle it
14:28:28  INFO        [positions] 3/3 (3 valid)
14:28:29  INFO        Daily log -> logs/daily/2026-09-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:28 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.62|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  SCHW  P&L +0.2%  $+0.08                                           HOLD|
|  EQIX  P&L +0.6%  $+0.22                                           HOLD|
|  DRI  P&L +0.7%  $+0.23                                            HOLD|
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
=== options_live_micro LIVE 2026-09-21T10:28:29.595313-04:00 share=25% ===
2026-09-21 10:28:29,595 INFO === options_live_micro LIVE 2026-09-21T10:28:29.595313-04:00 share=25% ===
Live account equity $226.63 cash $124.40 #225458845 options_level=3
2026-09-21 10:28:29,750 INFO Live account equity $226.63 cash $124.40 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-21 10:28:29,876 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-21 10:28:29,956 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (197 earlier lines - see full log file)

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
## Ledger health — 2026-09-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1430 | WARN | <<<
| Missing exit records (post) |  1427 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1367 med=-12.5% | TAINTED n=1882 med=-38.9% | KEEP-only n=751 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.63 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260921T143133Z

- UTC timestamp: `20260921T143133Z`
- GitHub run: [#10521](https://github.com/28twagg-ops/TradingBot/actions/runs/35612567963)
- Run id: `35612567963`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`115s`
- Full logs: `logs/action_runs/20260921T143133Z_live_bot.log`, `logs/action_runs/20260921T143133Z_live_options.log`, `logs/action_runs/20260921T143133Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T10:31:39.515549-04:00","date":"2026-09-21","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":102.7,"phases_s":{"reconcile":2.14,"cancel":0.03,"manage":34.0,"protective_stops":0.75,"scan":52.74,"entries":4.45},"signals":59,"placed":0,"equity":997158.09,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":["S165:CRWD","S164:CRWD","S168:CRWD","S167:CRWD","S163:CRWD","S209:CRWD","S350:CRWD","S351:CRWD"],"github_run":"10521","github_run_id":"35612567963","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:31:34  INFO      Mode: exits
14:31:35  INFO        Daily log -> logs/daily/2026-09-21.md
14:31:35  INFO        Daily log reconciled -> logs/daily/2026-09-21.md (2 ledger rows)
14:31:35  INFO        place_all_stops: checking 3 positions...
14:31:35  INFO        STOP skipped DRI: fractional (0.1604 shares) — software exit will handle it
14:31:35  INFO        STOP skipped EQIX: fractional (0.0327 shares) — software exit will handle it
14:31:35  INFO        STOP skipped SCHW: fractional (0.3194 shares) — software exit will handle it
14:31:35  INFO        [positions] 3/3 (3 valid)
14:31:35  INFO        Daily log -> logs/daily/2026-09-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.52|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  SCHW  P&L +0.2%  $+0.07                                           HOLD|
|  EQIX  P&L +0.5%  $+0.17                                           HOLD|
|  DRI  P&L +0.5%  $+0.18                                            HOLD|
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
=== options_live_micro LIVE 2026-09-21T10:31:36.400469-04:00 share=25% ===
2026-09-21 10:31:36,400 INFO === options_live_micro LIVE 2026-09-21T10:31:36.400469-04:00 share=25% ===
Live account equity $226.52 cash $124.40 #225458845 options_level=3
2026-09-21 10:31:36,542 INFO Live account equity $226.52 cash $124.40 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-21 10:31:36,627 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-21 10:31:36,666 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (203 earlier lines - see full log file)

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
## Ledger health — 2026-09-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1430 | WARN | <<<
| Missing exit records (post) |  1427 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1367 med=-12.5% | TAINTED n=1882 med=-38.9% | KEEP-only n=751 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.52 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260921T143611Z

- UTC timestamp: `20260921T143611Z`
- GitHub run: [#10522](https://github.com/28twagg-ops/TradingBot/actions/runs/35613127668)
- Run id: `35613127668`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`115s`
- Full logs: `logs/action_runs/20260921T143611Z_live_bot.log`, `logs/action_runs/20260921T143611Z_live_options.log`, `logs/action_runs/20260921T143611Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T10:36:19.836752-04:00","date":"2026-09-21","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":104.4,"phases_s":{"reconcile":2.52,"cancel":0.14,"manage":37.62,"protective_stops":2.83,"scan":34.91,"entries":17.32},"signals":59,"placed":0,"equity":997158.09,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":["S165:CRWD","S164:CRWD","S168:CRWD","S167:CRWD","S163:CRWD","S209:CRWD","S350:CRWD","S351:CRWD"],"github_run":"10522","github_run_id":"35613127668","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:36:12  INFO      Mode: exits
14:36:13  INFO        Daily log -> logs/daily/2026-09-21.md
14:36:13  INFO        Daily log reconciled -> logs/daily/2026-09-21.md (2 ledger rows)
14:36:13  INFO        place_all_stops: checking 3 positions...
14:36:13  INFO        STOP skipped DRI: fractional (0.1604 shares) — software exit will handle it
14:36:13  INFO        STOP skipped EQIX: fractional (0.0327 shares) — software exit will handle it
14:36:13  INFO        STOP skipped SCHW: fractional (0.3194 shares) — software exit will handle it
14:36:14  INFO        [positions] 3/3 (3 valid)
14:36:14  INFO        Daily log -> logs/daily/2026-09-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.42|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  SCHW  P&L +0.1%  $+0.05                                           HOLD|
|  DRI  P&L +0.3%  $+0.11                                            HOLD|
|  EQIX  P&L +0.5%  $+0.17                                           HOLD|
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
=== options_live_micro LIVE 2026-09-21T10:36:15.690008-04:00 share=25% ===
2026-09-21 10:36:15,690 INFO === options_live_micro LIVE 2026-09-21T10:36:15.690008-04:00 share=25% ===
Live account equity $226.42 cash $124.40 #225458845 options_level=3
2026-09-21 10:36:15,912 INFO Live account equity $226.42 cash $124.40 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-21 10:36:16,331 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-21 10:36:16,468 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (199 earlier lines - see full log file)

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
## Ledger health — 2026-09-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1430 | WARN | <<<
| Missing exit records (post) |  1427 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1367 med=-12.5% | TAINTED n=1882 med=-38.9% | KEEP-only n=751 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.42 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260921T144104Z

- UTC timestamp: `20260921T144104Z`
- GitHub run: [#10523](https://github.com/28twagg-ops/TradingBot/actions/runs/35613685683)
- Run id: `35613685683`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`103s`
- Full logs: `logs/action_runs/20260921T144104Z_live_bot.log`, `logs/action_runs/20260921T144104Z_live_options.log`, `logs/action_runs/20260921T144104Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T10:41:09.391715-04:00","date":"2026-09-21","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":93.8,"phases_s":{"reconcile":2.38,"cancel":0.06,"manage":38.04,"protective_stops":1.34,"scan":34.84,"entries":8.24},"signals":59,"placed":0,"equity":997158.09,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":["S165:CRWD","S164:CRWD","S168:CRWD","S167:CRWD","S163:CRWD","S209:CRWD","S350:CRWD","S351:CRWD"],"github_run":"10523","github_run_id":"35613685683","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:41:05  INFO      Mode: exits
14:41:05  INFO        Daily log -> logs/daily/2026-09-21.md
14:41:05  INFO        Daily log reconciled -> logs/daily/2026-09-21.md (2 ledger rows)
14:41:05  INFO        place_all_stops: checking 3 positions...
14:41:05  INFO        STOP skipped DRI: fractional (0.1604 shares) — software exit will handle it
14:41:05  INFO        STOP skipped EQIX: fractional (0.0327 shares) — software exit will handle it
14:41:05  INFO        STOP skipped SCHW: fractional (0.3194 shares) — software exit will handle it
14:41:05  INFO        [positions] 3/3 (3 valid)
14:41:06  INFO        Daily log -> logs/daily/2026-09-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.50|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  SCHW  P&L +0.2%  $+0.07                                           HOLD|
|  EQIX  P&L +0.5%  $+0.16                                           HOLD|
|  DRI  P&L +0.5%  $+0.17                                            HOLD|
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
=== options_live_micro LIVE 2026-09-21T10:41:06.782613-04:00 share=25% ===
2026-09-21 10:41:06,782 INFO === options_live_micro LIVE 2026-09-21T10:41:06.782613-04:00 share=25% ===
Live account equity $226.50 cash $124.40 #225458845 options_level=3
2026-09-21 10:41:06,902 INFO Live account equity $226.50 cash $124.40 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-21 10:41:06,993 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-21 10:41:07,053 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (208 earlier lines - see full log file)

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
## Ledger health — 2026-09-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1430 | WARN | <<<
| Missing exit records (post) |  1427 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1367 med=-12.5% | TAINTED n=1882 med=-38.9% | KEEP-only n=751 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.5 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260921T144613Z

- UTC timestamp: `20260921T144613Z`
- GitHub run: [#10524](https://github.com/28twagg-ops/TradingBot/actions/runs/35614246066)
- Run id: `35614246066`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`112s`
- Full logs: `logs/action_runs/20260921T144613Z_live_bot.log`, `logs/action_runs/20260921T144613Z_live_options.log`, `logs/action_runs/20260921T144613Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T10:46:20.431913-04:00","date":"2026-09-21","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":100.1,"phases_s":{"reconcile":2.11,"cancel":0.02,"manage":31.87,"protective_stops":0.55,"scan":53.19,"entries":3.74},"signals":59,"placed":0,"equity":997158.09,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":["S165:CRWD","S164:CRWD","S168:CRWD","S167:CRWD","S163:CRWD","S209:CRWD","S350:CRWD","S351:CRWD"],"github_run":"10524","github_run_id":"35614246066","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:46:16  INFO      Mode: exits
14:46:16  INFO        Daily log -> logs/daily/2026-09-21.md
14:46:16  INFO        Daily log reconciled -> logs/daily/2026-09-21.md (2 ledger rows)
14:46:16  INFO        place_all_stops: checking 3 positions...
14:46:16  INFO        STOP skipped DRI: fractional (0.1604 shares) — software exit will handle it
14:46:16  INFO        STOP skipped EQIX: fractional (0.0327 shares) — software exit will handle it
14:46:16  INFO        STOP skipped SCHW: fractional (0.3194 shares) — software exit will handle it
14:46:16  INFO        [positions] 3/3 (3 valid)
14:46:16  INFO        Daily log -> logs/daily/2026-09-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.41|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  SCHW  P&L +0.2%  $+0.05                                           HOLD|
|  DRI  P&L +0.4%  $+0.12                                            HOLD|
|  EQIX  P&L +0.4%  $+0.14                                           HOLD|
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
=== options_live_micro LIVE 2026-09-21T10:46:17.709242-04:00 share=25% ===
2026-09-21 10:46:17,709 INFO === options_live_micro LIVE 2026-09-21T10:46:17.709242-04:00 share=25% ===
Live account equity $226.41 cash $124.40 #225458845 options_level=3
2026-09-21 10:46:17,756 INFO Live account equity $226.41 cash $124.40 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-21 10:46:17,781 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-21 10:46:17,798 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (210 earlier lines - see full log file)

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
## Ledger health — 2026-09-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1430 | WARN | <<<
| Missing exit records (post) |  1427 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1367 med=-12.5% | TAINTED n=1882 med=-38.9% | KEEP-only n=751 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.41 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260921T145112Z

- UTC timestamp: `20260921T145112Z`
- GitHub run: [#10525](https://github.com/28twagg-ops/TradingBot/actions/runs/35614806666)
- Run id: `35614806666`
- Live bot: exit=`0`, duration=`5s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`134s`
- Full logs: `logs/action_runs/20260921T145112Z_live_bot.log`, `logs/action_runs/20260921T145112Z_live_options.log`, `logs/action_runs/20260921T145112Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T10:51:21.846528-04:00","date":"2026-09-21","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":121.9,"phases_s":{"reconcile":2.62,"cancel":0.16,"manage":34.1,"protective_stops":3.24,"scan":54.18,"entries":18.32},"signals":59,"placed":0,"equity":997158.09,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":["S165:CRWD","S164:CRWD","S168:CRWD","S167:CRWD","S163:CRWD","S209:CRWD","S350:CRWD","S351:CRWD"],"github_run":"10525","github_run_id":"35614806666","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:51:15  INFO      Mode: exits
14:51:16  INFO        Daily log -> logs/daily/2026-09-21.md
14:51:16  INFO        Daily log reconciled -> logs/daily/2026-09-21.md (2 ledger rows)
14:51:16  INFO        place_all_stops: checking 3 positions...
14:51:16  INFO        STOP skipped DRI: fractional (0.1604 shares) — software exit will handle it
14:51:16  INFO        STOP skipped EQIX: fractional (0.0327 shares) — software exit will handle it
14:51:16  INFO        STOP skipped SCHW: fractional (0.3194 shares) — software exit will handle it
14:51:16  INFO        [positions] 3/3 (3 valid)
14:51:17  INFO        Daily log -> logs/daily/2026-09-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:51 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.39|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  SCHW  P&L +0.1%  $+0.04                                           HOLD|
|  EQIX  P&L +0.4%  $+0.12                                           HOLD|
|  DRI  P&L +0.4%  $+0.13                                            HOLD|
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
=== options_live_micro LIVE 2026-09-21T10:51:18.126542-04:00 share=25% ===
2026-09-21 10:51:18,126 INFO === options_live_micro LIVE 2026-09-21T10:51:18.126542-04:00 share=25% ===
Live account equity $226.39 cash $124.40 #225458845 options_level=3
2026-09-21 10:51:18,355 INFO Live account equity $226.39 cash $124.40 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-21 10:51:18,565 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-21 10:51:18,704 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (207 earlier lines - see full log file)

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
## Ledger health — 2026-09-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1430 | WARN | <<<
| Missing exit records (post) |  1427 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1367 med=-12.5% | TAINTED n=1882 med=-38.9% | KEEP-only n=751 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.39 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260921T145610Z

- UTC timestamp: `20260921T145610Z`
- GitHub run: [#10526](https://github.com/28twagg-ops/TradingBot/actions/runs/35615378170)
- Run id: `35615378170`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`147s`
- Full logs: `logs/action_runs/20260921T145610Z_live_bot.log`, `logs/action_runs/20260921T145610Z_live_options.log`, `logs/action_runs/20260921T145610Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T10:56:17.979778-04:00","date":"2026-09-21","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":136.3,"phases_s":{"reconcile":2.44,"cancel":0.12,"manage":61.99,"protective_stops":2.68,"scan":46.31,"entries":13.75},"signals":59,"placed":0,"equity":997158.09,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":["S165:CRWD","S164:CRWD","S168:CRWD","S167:CRWD","S163:CRWD","S209:CRWD","S350:CRWD","S351:CRWD"],"github_run":"10526","github_run_id":"35615378170","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:56:11  INFO      Mode: exits
14:56:12  INFO        Daily log -> logs/daily/2026-09-21.md
14:56:12  INFO        Daily log reconciled -> logs/daily/2026-09-21.md (2 ledger rows)
14:56:12  INFO        place_all_stops: checking 3 positions...
14:56:12  INFO        STOP skipped DRI: fractional (0.1604 shares) — software exit will handle it
14:56:12  INFO        STOP skipped EQIX: fractional (0.0327 shares) — software exit will handle it
14:56:12  INFO        STOP skipped SCHW: fractional (0.3194 shares) — software exit will handle it
14:56:13  INFO        [positions] 3/3 (3 valid)
14:56:13  INFO        Daily log -> logs/daily/2026-09-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:56 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.41|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  SCHW  P&L +0.1%  $+0.03                                           HOLD|
|  DRI  P&L +0.4%  $+0.13                                            HOLD|
|  EQIX  P&L +0.4%  $+0.15                                           HOLD|
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
=== options_live_micro LIVE 2026-09-21T10:56:14.450144-04:00 share=25% ===
2026-09-21 10:56:14,450 INFO === options_live_micro LIVE 2026-09-21T10:56:14.450144-04:00 share=25% ===
Live account equity $226.41 cash $124.40 #225458845 options_level=3
2026-09-21 10:56:14,650 INFO Live account equity $226.41 cash $124.40 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-21 10:56:14,828 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-21 10:56:14,949 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (209 earlier lines - see full log file)

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
## Ledger health — 2026-09-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1430 | WARN | <<<
| Missing exit records (post) |  1427 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1367 med=-12.5% | TAINTED n=1882 med=-38.9% | KEEP-only n=751 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.41 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260921T150110Z

- UTC timestamp: `20260921T150110Z`
- GitHub run: [#10527](https://github.com/28twagg-ops/TradingBot/actions/runs/35615934230)
- Run id: `35615934230`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`195s`
- Full logs: `logs/action_runs/20260921T150110Z_live_bot.log`, `logs/action_runs/20260921T150110Z_live_options.log`, `logs/action_runs/20260921T150110Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T11:01:15.524223-04:00","date":"2026-09-21","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":186.1,"phases_s":{"reconcile":2.4,"cancel":0.11,"manage":125.67,"protective_stops":2.6,"scan":34.59,"entries":11.89},"signals":59,"placed":0,"equity":997158.09,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":["S165:CRWD","S164:CRWD","S168:CRWD","S167:CRWD","S163:CRWD","S209:CRWD","S350:CRWD","S351:CRWD"],"github_run":"10527","github_run_id":"35615934230","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:01:10  INFO      Mode: exits
15:01:11  INFO        Daily log -> logs/daily/2026-09-21.md
15:01:11  INFO        Daily log reconciled -> logs/daily/2026-09-21.md (2 ledger rows)
15:01:11  INFO        place_all_stops: checking 3 positions...
15:01:11  INFO        STOP skipped DRI: fractional (0.1604 shares) — software exit will handle it
15:01:11  INFO        STOP skipped EQIX: fractional (0.0327 shares) — software exit will handle it
15:01:11  INFO        STOP skipped SCHW: fractional (0.3194 shares) — software exit will handle it
15:01:11  INFO        [positions] 3/3 (3 valid)
15:01:12  INFO        Daily log -> logs/daily/2026-09-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.33|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  SCHW  P&L -0.0%  $-0.01                                           HOLD|
|  DRI  P&L +0.3%  $+0.09                                            HOLD|
|  EQIX  P&L +0.4%  $+0.15                                           HOLD|
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
=== options_live_micro LIVE 2026-09-21T11:01:12.842587-04:00 share=25% ===
2026-09-21 11:01:12,842 INFO === options_live_micro LIVE 2026-09-21T11:01:12.842587-04:00 share=25% ===
Live account equity $226.33 cash $124.40 #225458845 options_level=3
2026-09-21 11:01:12,975 INFO Live account equity $226.33 cash $124.40 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-21 11:01:13,079 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-21 11:01:13,154 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (226 earlier lines - see full log file)

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
## Ledger health — 2026-09-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1430 | WARN | <<<
| Missing exit records (post) |  1427 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1367 med=-12.5% | TAINTED n=1882 med=-38.9% | KEEP-only n=751 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.33 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260921T150610Z

- UTC timestamp: `20260921T150610Z`
- GitHub run: [#10528](https://github.com/28twagg-ops/TradingBot/actions/runs/35616505244)
- Run id: `35616505244`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`113s`
- Full logs: `logs/action_runs/20260921T150610Z_live_bot.log`, `logs/action_runs/20260921T150610Z_live_options.log`, `logs/action_runs/20260921T150610Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T11:06:14.873148-04:00","date":"2026-09-21","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":101.3,"phases_s":{"reconcile":2.13,"cancel":0.02,"manage":31.76,"protective_stops":0.6,"scan":54.76,"entries":3.43},"signals":59,"placed":0,"equity":997158.09,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":["S165:CRWD","S164:CRWD","S168:CRWD","S167:CRWD","S163:CRWD","S209:CRWD","S350:CRWD","S351:CRWD"],"github_run":"10528","github_run_id":"35616505244","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:06:10  INFO      Mode: exits
15:06:11  INFO        Daily log -> logs/daily/2026-09-21.md
15:06:11  INFO        Daily log reconciled -> logs/daily/2026-09-21.md (2 ledger rows)
15:06:11  INFO        place_all_stops: checking 3 positions...
15:06:11  INFO        STOP skipped DRI: fractional (0.1604 shares) — software exit will handle it
15:06:11  INFO        STOP skipped EQIX: fractional (0.0327 shares) — software exit will handle it
15:06:11  INFO        STOP skipped SCHW: fractional (0.3194 shares) — software exit will handle it
15:06:11  INFO        [positions] 3/3 (3 valid)
15:06:11  INFO        Daily log -> logs/daily/2026-09-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.46|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  SCHW  P&L +0.1%  $+0.05                                           HOLD|
|  DRI  P&L +0.3%  $+0.11                                            HOLD|
|  EQIX  P&L +0.6%  $+0.21                                           HOLD|
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
=== options_live_micro LIVE 2026-09-21T11:06:12.097038-04:00 share=25% ===
2026-09-21 11:06:12,097 INFO === options_live_micro LIVE 2026-09-21T11:06:12.097038-04:00 share=25% ===
Live account equity $226.46 cash $124.40 #225458845 options_level=3
2026-09-21 11:06:12,139 INFO Live account equity $226.46 cash $124.40 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-21 11:06:12,163 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-21 11:06:12,179 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (205 earlier lines - see full log file)

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
## Ledger health — 2026-09-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1430 | WARN | <<<
| Missing exit records (post) |  1427 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1367 med=-12.5% | TAINTED n=1882 med=-38.9% | KEEP-only n=751 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.46 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260921T151114Z

- UTC timestamp: `20260921T151114Z`
- GitHub run: [#10529](https://github.com/28twagg-ops/TradingBot/actions/runs/35617081226)
- Run id: `35617081226`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`116s`
- Full logs: `logs/action_runs/20260921T151114Z_live_bot.log`, `logs/action_runs/20260921T151114Z_live_options.log`, `logs/action_runs/20260921T151114Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T11:11:21.189697-04:00","date":"2026-09-21","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":104.1,"phases_s":{"reconcile":2.15,"cancel":0.03,"manage":32.59,"protective_stops":1.11,"scan":53.24,"entries":6.38},"signals":59,"placed":0,"equity":997158.09,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":["S165:CRWD","S164:CRWD","S168:CRWD","S167:CRWD","S163:CRWD","S209:CRWD","S350:CRWD","S351:CRWD"],"github_run":"10529","github_run_id":"35617081226","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:11:17  INFO      Mode: exits
15:11:17  INFO        Daily log -> logs/daily/2026-09-21.md
15:11:17  INFO        Daily log reconciled -> logs/daily/2026-09-21.md (2 ledger rows)
15:11:17  INFO        place_all_stops: checking 3 positions...
15:11:17  INFO        STOP skipped DRI: fractional (0.1604 shares) — software exit will handle it
15:11:17  INFO        STOP skipped EQIX: fractional (0.0327 shares) — software exit will handle it
15:11:17  INFO        STOP skipped SCHW: fractional (0.3194 shares) — software exit will handle it
15:11:17  INFO        [positions] 3/3 (3 valid)
15:11:17  INFO        Daily log -> logs/daily/2026-09-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.46|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  SCHW  P&L +0.2%  $+0.07                                           HOLD|
|  DRI  P&L +0.4%  $+0.12                                            HOLD|
|  EQIX  P&L +0.5%  $+0.17                                           HOLD|
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
=== options_live_micro LIVE 2026-09-21T11:11:18.486698-04:00 share=25% ===
2026-09-21 11:11:18,486 INFO === options_live_micro LIVE 2026-09-21T11:11:18.486698-04:00 share=25% ===
Live account equity $226.46 cash $124.40 #225458845 options_level=3
2026-09-21 11:11:18,546 INFO Live account equity $226.46 cash $124.40 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-21 11:11:18,581 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-21 11:11:18,602 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (207 earlier lines - see full log file)

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
## Ledger health — 2026-09-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1430 | WARN | <<<
| Missing exit records (post) |  1427 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1367 med=-12.5% | TAINTED n=1882 med=-38.9% | KEEP-only n=751 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.46 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260921T151634Z

- UTC timestamp: `20260921T151634Z`
- GitHub run: [#10530](https://github.com/28twagg-ops/TradingBot/actions/runs/35617646374)
- Run id: `35617646374`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`95s`
- Full logs: `logs/action_runs/20260921T151634Z_live_bot.log`, `logs/action_runs/20260921T151634Z_live_options.log`, `logs/action_runs/20260921T151634Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T11:16:41.403616-04:00","date":"2026-09-21","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":85.6,"phases_s":{"reconcile":2.43,"cancel":0.1,"manage":30.56,"protective_stops":2.61,"scan":28.93,"entries":12.2},"signals":59,"placed":0,"equity":997158.09,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":["S165:CRWD","S164:CRWD","S168:CRWD","S167:CRWD","S163:CRWD","S209:CRWD","S350:CRWD","S351:CRWD"],"github_run":"10530","github_run_id":"35617646374","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:16:36  INFO      Mode: exits
15:16:37  INFO        Daily log -> logs/daily/2026-09-21.md
15:16:37  INFO        Daily log reconciled -> logs/daily/2026-09-21.md (2 ledger rows)
15:16:37  INFO        place_all_stops: checking 3 positions...
15:16:37  INFO        STOP skipped DRI: fractional (0.1604 shares) — software exit will handle it
15:16:37  INFO        STOP skipped EQIX: fractional (0.0327 shares) — software exit will handle it
15:16:37  INFO        STOP skipped SCHW: fractional (0.3194 shares) — software exit will handle it
15:16:37  INFO        [positions] 3/3 (3 valid)
15:16:37  INFO        Daily log -> logs/daily/2026-09-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.59|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  SCHW  P&L +0.3%  $+0.10                                           HOLD|
|  DRI  P&L +0.4%  $+0.13                                            HOLD|
|  EQIX  P&L +0.8%  $+0.26                                           HOLD|
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
=== options_live_micro LIVE 2026-09-21T11:16:38.437969-04:00 share=25% ===
2026-09-21 11:16:38,438 INFO === options_live_micro LIVE 2026-09-21T11:16:38.437969-04:00 share=25% ===
Live account equity $226.59 cash $124.40 #225458845 options_level=3
2026-09-21 11:16:38,567 INFO Live account equity $226.59 cash $124.40 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-21 11:16:38,755 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-21 11:16:38,822 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (209 earlier lines - see full log file)

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
## Ledger health — 2026-09-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1430 | WARN | <<<
| Missing exit records (post) |  1427 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1367 med=-12.5% | TAINTED n=1882 med=-38.9% | KEEP-only n=751 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.59 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260921T152129Z

- UTC timestamp: `20260921T152129Z`
- GitHub run: [#10531](https://github.com/28twagg-ops/TradingBot/actions/runs/35618218376)
- Run id: `35618218376`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`120s`
- Full logs: `logs/action_runs/20260921T152129Z_live_bot.log`, `logs/action_runs/20260921T152129Z_live_options.log`, `logs/action_runs/20260921T152129Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T11:21:35.425371-04:00","date":"2026-09-21","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":110.9,"phases_s":{"reconcile":2.31,"cancel":0.08,"manage":58.96,"protective_stops":2.17,"scan":28.88,"entries":9.85},"signals":59,"placed":0,"equity":997158.09,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":["S165:CRWD","S164:CRWD","S168:CRWD","S167:CRWD","S163:CRWD","S209:CRWD","S350:CRWD","S351:CRWD"],"github_run":"10531","github_run_id":"35618218376","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:21:30  INFO      Mode: exits
15:21:30  INFO        Daily log -> logs/daily/2026-09-21.md
15:21:30  INFO        Daily log reconciled -> logs/daily/2026-09-21.md (2 ledger rows)
15:21:30  INFO        place_all_stops: checking 3 positions...
15:21:30  INFO        STOP skipped DRI: fractional (0.1604 shares) — software exit will handle it
15:21:31  INFO        STOP skipped EQIX: fractional (0.0327 shares) — software exit will handle it
15:21:31  INFO        STOP skipped SCHW: fractional (0.3194 shares) — software exit will handle it
15:21:31  INFO        [positions] 3/3 (3 valid)
15:21:31  INFO        Daily log -> logs/daily/2026-09-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.58|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  SCHW  P&L +0.4%  $+0.12                                           HOLD|
|  DRI  P&L +0.4%  $+0.14                                            HOLD|
|  EQIX  P&L +0.7%  $+0.23                                           HOLD|
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
=== options_live_micro LIVE 2026-09-21T11:21:32.320290-04:00 share=25% ===
2026-09-21 11:21:32,320 INFO === options_live_micro LIVE 2026-09-21T11:21:32.320290-04:00 share=25% ===
Live account equity $226.58 cash $124.40 #225458845 options_level=3
2026-09-21 11:21:32,437 INFO Live account equity $226.58 cash $124.40 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-21 11:21:32,581 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-21 11:21:32,641 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (220 earlier lines - see full log file)

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
## Ledger health — 2026-09-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1430 | WARN | <<<
| Missing exit records (post) |  1427 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1367 med=-12.5% | TAINTED n=1882 med=-38.9% | KEEP-only n=751 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.58 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260921T152617Z

- UTC timestamp: `20260921T152617Z`
- GitHub run: [#10532](https://github.com/28twagg-ops/TradingBot/actions/runs/35618783503)
- Run id: `35618783503`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`114s`
- Full logs: `logs/action_runs/20260921T152617Z_live_bot.log`, `logs/action_runs/20260921T152617Z_live_options.log`, `logs/action_runs/20260921T152617Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T11:26:24.236159-04:00","date":"2026-09-21","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":103.1,"phases_s":{"reconcile":2.48,"cancel":0.12,"manage":32.22,"protective_stops":3.12,"scan":40.38,"entries":15.8},"signals":59,"placed":0,"equity":997158.09,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":["S165:CRWD","S164:CRWD","S168:CRWD","S167:CRWD","S163:CRWD","S209:CRWD","S350:CRWD","S351:CRWD"],"github_run":"10532","github_run_id":"35618783503","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:26:18  INFO      Mode: exits
15:26:19  INFO        Daily log -> logs/daily/2026-09-21.md
15:26:19  INFO        Daily log reconciled -> logs/daily/2026-09-21.md (2 ledger rows)
15:26:19  INFO        place_all_stops: checking 3 positions...
15:26:19  INFO        STOP skipped DRI: fractional (0.1604 shares) — software exit will handle it
15:26:19  INFO        STOP skipped EQIX: fractional (0.0327 shares) — software exit will handle it
15:26:19  INFO        STOP skipped SCHW: fractional (0.3194 shares) — software exit will handle it
15:26:20  INFO        [positions] 3/3 (3 valid)
15:26:20  INFO        Daily log -> logs/daily/2026-09-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.61|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  DRI  P&L +0.4%  $+0.14                                            HOLD|
|  SCHW  P&L +0.4%  $+0.15                                           HOLD|
|  EQIX  P&L +0.6%  $+0.22                                           HOLD|
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
=== options_live_micro LIVE 2026-09-21T11:26:21.164665-04:00 share=25% ===
2026-09-21 11:26:21,164 INFO === options_live_micro LIVE 2026-09-21T11:26:21.164665-04:00 share=25% ===
Live account equity $226.61 cash $124.40 #225458845 options_level=3
2026-09-21 11:26:21,366 INFO Live account equity $226.61 cash $124.40 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-21 11:26:21,524 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-21 11:26:21,627 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (213 earlier lines - see full log file)

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
## Ledger health — 2026-09-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1430 | WARN | <<<
| Missing exit records (post) |  1427 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1367 med=-12.5% | TAINTED n=1882 med=-38.9% | KEEP-only n=751 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.61 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260921T153253Z

- UTC timestamp: `20260921T153253Z`
- GitHub run: [#10533](https://github.com/28twagg-ops/TradingBot/actions/runs/35619348216)
- Run id: `35619348216`
- Live bot: exit=`0`, duration=`5s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260921T153253Z_live_bot.log`, `logs/action_runs/20260921T153253Z_live_options.log`, `logs/action_runs/20260921T153253Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T11:26:24.236159-04:00","date":"2026-09-21","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":103.1,"phases_s":{"reconcile":2.48,"cancel":0.12,"manage":32.22,"protective_stops":3.12,"scan":40.38,"entries":15.8},"signals":59,"placed":0,"equity":997158.09,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":["S165:CRWD","S164:CRWD","S168:CRWD","S167:CRWD","S163:CRWD","S209:CRWD","S350:CRWD","S351:CRWD"],"github_run":"10532","github_run_id":"35618783503","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:32:56  INFO      Mode: exits
15:32:56  INFO        Daily log -> logs/daily/2026-09-21.md
15:32:56  INFO        Daily log reconciled -> logs/daily/2026-09-21.md (2 ledger rows)
15:32:57  INFO        place_all_stops: checking 3 positions...
15:32:57  INFO        STOP skipped DRI: fractional (0.1604 shares) — software exit will handle it
15:32:57  INFO        STOP skipped EQIX: fractional (0.0327 shares) — software exit will handle it
15:32:57  INFO        STOP skipped SCHW: fractional (0.3194 shares) — software exit will handle it
15:32:57  INFO        [positions] 3/3 (3 valid)
15:32:57  INFO        Daily log -> logs/daily/2026-09-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:32 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.61|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  SCHW  P&L +0.4%  $+0.13                                           HOLD|
|  DRI  P&L +0.4%  $+0.13                                            HOLD|
|  EQIX  P&L +0.7%  $+0.25                                           HOLD|
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
=== options_live_micro LIVE 2026-09-21T11:32:58.740786-04:00 share=25% ===
2026-09-21 11:32:58,740 INFO === options_live_micro LIVE 2026-09-21T11:32:58.740786-04:00 share=25% ===
Live account equity $226.61 cash $124.40 #225458845 options_level=3
2026-09-21 11:32:59,236 INFO Live account equity $226.61 cash $124.40 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-21 11:32:59,438 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-21 11:32:59,571 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=50 paper_keys=yes dry_run=False
  alpaca positions=16
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE FAIL: {"code":50010000,"message":"internal server error occurred"}
paper probe failed (non-fatal)
=== options_morning_bot (PAPER) 2026-09-21T11:33:02.542808-04:00 ===

[Run context]
2026-09-21 11:33:02,776 WARNING paper get_account failed attempt 1/3 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 2s
2026-09-21 11:33:04,851 WARNING paper get_account failed attempt 2/3 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 4s
2026-09-21 11:33:08,928 ERROR paper get_account failed after 3 attempts: {"code":50010000,"message":"internal server error occurred"}
WARN: get_account failed ({"code":50010000,"message":"internal server error occurred"}) but positions OK (n=16). Keys are fine; Alpaca account endpoint is flaky. Using cached equity $997158.09.
2026-09-21 11:33:09,118 WARNING paper get_account failed attempt 1/2 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 2s
2026-09-21 11:33:11,192 ERROR paper get_account failed after 2 attempts: {"code":50010000,"message":"internal server error occurred"}
WARN: using cached paper equity $997158.09 (get_account: {"code":50010000,"message":"internal server error occurred"})
2026-09-21 11:33:11,316 WARNING lab get_account failed attempt 1/2: {"code":50010000,"message":"internal server error occurred"}
2026-09-21 11:33:13,451 ERROR lab get_account failed after 2 attempts: {"code":50010000,"message":"internal server error occurred"}

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
  EXIT [b899|lab0899_s411_w1_0928_1005_r2|S411] take_profit (+53.4%) SELL failed NFLX260925C00074000: {"code":50010000,"message":"internal server error occurred"}
  EXIT [b898|lab0898_s411_w1_0928_1005_r1|S411] take_profit (+53.4%) SELL failed NFLX260925C00074000: {"code":50010000,"message":"internal server error occurred"}
  EXIT [b801|lab0801_s404_w1_0928_1005_r2|S404] take_profit (+53.4%) SELL failed NFLX260925C00074000: {"code":50010000,"message":"internal server error occurred"}
  EXIT [b800|lab0800_s404_w1_0928_1005_r1|S404] take_profit (+53.4%) SELL failed NFLX260925C00074000: {"code":50010000,"message":"internal server error occurred"}
  EXIT [b90|live_1to1|S404] take_profit (+53.4%) SELL failed NFLX260925C00074000: {"code":50010000,"message":"internal server error occurred"}
  EXIT [b777|lab0777_s397_w1_0928_1005_r2|S397] take_profit (+53.4%) SELL failed NFLX260925C00074000: {"code":50010000,"message":"internal server error occurred"}
  EXIT [b776|lab0776_s397_w1_0928_1005_r1|S397] take_profit (+53.4%) SELL failed NFLX260925C00074000: {"code":50010000,"message":"internal server error occurred"}
  EXIT [b434|lab0434_s366_w2_1005_1045_r1|S366] take_profit (+129.5%) SELL failed MARA260925C00012500: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b433|lab0433_s366_w1_0928_1005_r2|S366] take_profit (+129.5%) SELL failed MARA260925C00012500: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b432|lab0432_s366_w1_0928_1005_r1|S366] take_profit (+129.5%) SELL failed MARA260925C00012500: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b239|lab0239_s401_w3_1045_1120_r2|S401] stop_loss (-65.2%) SELL failed MDT260925C00094000: {"code":50010000,"message":"internal server error occurred"}
  EXIT [b238|lab0238_s401_w3_1045_1120_r1|S401] stop_loss (-65.2%) SELL failed MDT260925C00094000: {"code":50010000,"message":"internal server error occurred"}
  EXIT [b241|lab0241_s401_w4_1120_1135_r2|S401] stop_loss (-65.2%) SELL failed MDT260925C00094000: {"code":50010000,"message":"internal server error occurred"}
  EXIT [b240|lab0240_s401_w4_1120_1135_r1|S401] stop_loss (-65.2%) SELL failed MDT260925C00094000: {"code":50010000,"message":"internal server error occurred"}
  EXIT [b181|lab0181_s217_w2_1005_1045_r2|S217] stop_loss (-62.5%) SELL failed BAC260925C00059000: {"code":50010000,"message":"internal server error occurred"}
  EXIT [b180|lab0180_s217_w2_1005_1045_r1|S217] stop_loss (-62.5%) SELL failed BAC260925C00059000: {"code":50010000,"message":"internal server error occurred"}
Protective stops: placed=0 upgraded=0 already=5 failed=8 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
Found 59 signal(s); top: ['S165:CRWD', 'S164:CRWD', 'S168:CRWD', 'S167:CRWD', 'S163:CRWD', 'S209:CRWD', 'S350:CRWD', 'S351:CRWD']
Paper lab: $997158 broker equity -> 1164 bucket(s) ($500 virtual each, unlimited paper)
```

---

## Run 20260921T153644Z

- UTC timestamp: `20260921T153644Z`
- GitHub run: [#10534](https://github.com/28twagg-ops/TradingBot/actions/runs/35619919706)
- Run id: `35619919706`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`82s`
- Full logs: `logs/action_runs/20260921T153644Z_live_bot.log`, `logs/action_runs/20260921T153644Z_live_options.log`, `logs/action_runs/20260921T153644Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T11:36:49.857864-04:00","date":"2026-09-21","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":69.9,"phases_s":{"reconcile":2.25,"cancel":0.05,"manage":57.92,"protective_stops":0.97},"signals":0,"placed":0,"equity":997158.09,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10534","github_run_id":"35619919706","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:36:45  INFO      Mode: exits
15:36:46  INFO        Daily log -> logs/daily/2026-09-21.md
15:36:46  INFO        Daily log reconciled -> logs/daily/2026-09-21.md (2 ledger rows)
15:36:46  INFO        place_all_stops: checking 3 positions...
15:36:46  INFO        STOP skipped DRI: fractional (0.1604 shares) — software exit will handle it
15:36:46  INFO        STOP skipped EQIX: fractional (0.0327 shares) — software exit will handle it
15:36:46  INFO        STOP skipped SCHW: fractional (0.3194 shares) — software exit will handle it
15:36:46  INFO        [positions] 3/3 (3 valid)
15:36:46  INFO        Daily log -> logs/daily/2026-09-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.61|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  DRI  P&L +0.4%  $+0.12                                            HOLD|
|  SCHW  P&L +0.4%  $+0.14                                           HOLD|
|  EQIX  P&L +0.7%  $+0.25                                           HOLD|
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
=== options_live_micro LIVE 2026-09-21T11:36:47.069604-04:00 share=25% ===
2026-09-21 11:36:47,069 INFO === options_live_micro LIVE 2026-09-21T11:36:47.069604-04:00 share=25% ===
Live account equity $226.61 cash $124.40 #225458845 options_level=3
2026-09-21 11:36:47,123 INFO Live account equity $226.61 cash $124.40 #225458845 options_level=3
Live micro: manage/exits only
2026-09-21 11:36:47,166 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-21 11:36:47,176 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (184 earlier lines - see full log file)

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
## Ledger health — 2026-09-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1430 | WARN | <<<
| Missing exit records (post) |  1427 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1367 med=-12.5% | TAINTED n=1882 med=-38.9% | KEEP-only n=751 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.61 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260921T154120Z

- UTC timestamp: `20260921T154120Z`
- GitHub run: [#10535](https://github.com/28twagg-ops/TradingBot/actions/runs/35620483393)
- Run id: `35620483393`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`148s`
- Full logs: `logs/action_runs/20260921T154120Z_live_bot.log`, `logs/action_runs/20260921T154120Z_live_options.log`, `logs/action_runs/20260921T154120Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T11:41:28.080516-04:00","date":"2026-09-21","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":137.3,"phases_s":{"reconcile":2.45,"cancel":0.19,"manage":122.61,"protective_stops":3.06},"signals":0,"placed":0,"equity":997158.09,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10535","github_run_id":"35620483393","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:41:22  INFO      Mode: exits
15:41:23  INFO        Daily log -> logs/daily/2026-09-21.md
15:41:23  INFO        Daily log reconciled -> logs/daily/2026-09-21.md (2 ledger rows)
15:41:23  INFO        place_all_stops: checking 3 positions...
15:41:23  INFO        STOP skipped DRI: fractional (0.1604 shares) — software exit will handle it
15:41:23  INFO        STOP skipped EQIX: fractional (0.0327 shares) — software exit will handle it
15:41:23  INFO        STOP skipped SCHW: fractional (0.3194 shares) — software exit will handle it
15:41:23  INFO        [positions] 3/3 (3 valid)
15:41:24  INFO        Daily log -> logs/daily/2026-09-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.59|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  DRI  P&L +0.3%  $+0.09                                            HOLD|
|  SCHW  P&L +0.5%  $+0.15                                           HOLD|
|  EQIX  P&L +0.7%  $+0.25                                           HOLD|
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
=== options_live_micro LIVE 2026-09-21T11:41:24.910596-04:00 share=25% ===
2026-09-21 11:41:24,910 INFO === options_live_micro LIVE 2026-09-21T11:41:24.910596-04:00 share=25% ===
Live account equity $226.59 cash $124.40 #225458845 options_level=3
2026-09-21 11:41:25,119 INFO Live account equity $226.59 cash $124.40 #225458845 options_level=3
Live micro: manage/exits only
2026-09-21 11:41:25,291 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-21 11:41:25,348 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (198 earlier lines - see full log file)

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
## Ledger health — 2026-09-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1430 | WARN | <<<
| Missing exit records (post) |  1427 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1367 med=-12.5% | TAINTED n=1882 med=-38.9% | KEEP-only n=751 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.59 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260921T154646Z

- UTC timestamp: `20260921T154646Z`
- GitHub run: [#10536](https://github.com/28twagg-ops/TradingBot/actions/runs/35621048786)
- Run id: `35621048786`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`146s`
- Full logs: `logs/action_runs/20260921T154646Z_live_bot.log`, `logs/action_runs/20260921T154646Z_live_options.log`, `logs/action_runs/20260921T154646Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T11:46:53.073149-04:00","date":"2026-09-21","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":136.5,"phases_s":{"reconcile":2.46,"cancel":0.2,"manage":121.9,"protective_stops":3.05},"signals":0,"placed":0,"equity":997158.09,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10536","github_run_id":"35621048786","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:46:46  INFO      Mode: exits
15:46:47  INFO        Daily log -> logs/daily/2026-09-21.md
15:46:47  INFO        Daily log reconciled -> logs/daily/2026-09-21.md (2 ledger rows)
15:46:47  INFO        place_all_stops: checking 3 positions...
15:46:47  INFO        STOP skipped DRI: fractional (0.1604 shares) — software exit will handle it
15:46:47  INFO        STOP skipped EQIX: fractional (0.0327 shares) — software exit will handle it
15:46:48  INFO        STOP skipped SCHW: fractional (0.3194 shares) — software exit will handle it
15:46:48  INFO        [positions] 3/3 (3 valid)
15:46:48  INFO        Daily log -> logs/daily/2026-09-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.63|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  DRI  P&L +0.2%  $+0.08                                            HOLD|
|  SCHW  P&L +0.6%  $+0.19                                           HOLD|
|  EQIX  P&L +0.8%  $+0.26                                           HOLD|
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
=== options_live_micro LIVE 2026-09-21T11:46:49.800309-04:00 share=25% ===
2026-09-21 11:46:49,800 INFO === options_live_micro LIVE 2026-09-21T11:46:49.800309-04:00 share=25% ===
Live account equity $226.63 cash $124.40 #225458845 options_level=3
2026-09-21 11:46:50,003 INFO Live account equity $226.63 cash $124.40 #225458845 options_level=3
Live micro: manage/exits only
2026-09-21 11:46:50,263 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-21 11:46:50,320 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (198 earlier lines - see full log file)

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
## Ledger health — 2026-09-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1430 | WARN | <<<
| Missing exit records (post) |  1427 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1367 med=-12.5% | TAINTED n=1882 med=-38.9% | KEEP-only n=751 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.63 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260921T155117Z

- UTC timestamp: `20260921T155117Z`
- GitHub run: [#10537](https://github.com/28twagg-ops/TradingBot/actions/runs/35621606429)
- Run id: `35621606429`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`163s`
- Full logs: `logs/action_runs/20260921T155117Z_live_bot.log`, `logs/action_runs/20260921T155117Z_live_options.log`, `logs/action_runs/20260921T155117Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T11:51:25.013005-04:00","date":"2026-09-21","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":153.8,"phases_s":{"reconcile":2.53,"cancel":0.18,"manage":138.99,"protective_stops":3.09},"signals":0,"placed":0,"equity":997158.09,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10537","github_run_id":"35621606429","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:51:19  INFO      Mode: exits
15:51:19  INFO        Daily log -> logs/daily/2026-09-21.md
15:51:19  INFO        Daily log reconciled -> logs/daily/2026-09-21.md (2 ledger rows)
15:51:19  INFO        place_all_stops: checking 3 positions...
15:51:19  INFO        STOP skipped DRI: fractional (0.1604 shares) — software exit will handle it
15:51:19  INFO        STOP skipped EQIX: fractional (0.0327 shares) — software exit will handle it
15:51:19  INFO        STOP skipped SCHW: fractional (0.3194 shares) — software exit will handle it
15:51:20  INFO        [positions] 3/3 (3 valid)
15:51:20  INFO        Daily log -> logs/daily/2026-09-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:51 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.67|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  DRI  P&L +0.4%  $+0.14                                            HOLD|
|  SCHW  P&L +0.5%  $+0.17                                           HOLD|
|  EQIX  P&L +0.8%  $+0.25                                           HOLD|
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
=== options_live_micro LIVE 2026-09-21T11:51:21.479121-04:00 share=25% ===
2026-09-21 11:51:21,479 INFO === options_live_micro LIVE 2026-09-21T11:51:21.479121-04:00 share=25% ===
Live account equity $226.67 cash $124.40 #225458845 options_level=3
2026-09-21 11:51:21,671 INFO Live account equity $226.67 cash $124.40 #225458845 options_level=3
Live micro: manage/exits only
2026-09-21 11:51:21,977 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-21 11:51:22,034 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (202 earlier lines - see full log file)

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
## Ledger health — 2026-09-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1430 | WARN | <<<
| Missing exit records (post) |  1427 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1367 med=-12.5% | TAINTED n=1882 med=-38.9% | KEEP-only n=751 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.67 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260921T155615Z

- UTC timestamp: `20260921T155615Z`
- GitHub run: [#10538](https://github.com/28twagg-ops/TradingBot/actions/runs/35622163975)
- Run id: `35622163975`
- Live bot: exit=`0`, duration=`5s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`152s`
- Full logs: `logs/action_runs/20260921T155615Z_live_bot.log`, `logs/action_runs/20260921T155615Z_live_options.log`, `logs/action_runs/20260921T155615Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T11:56:24.523332-04:00","date":"2026-09-21","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":139.9,"phases_s":{"reconcile":2.54,"cancel":0.21,"manage":124.04,"protective_stops":3.92},"signals":0,"placed":0,"equity":997158.09,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10538","github_run_id":"35622163975","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
15:56:18  INFO      Mode: exits
15:56:19  INFO        Daily log -> logs/daily/2026-09-21.md
15:56:19  INFO        Daily log reconciled -> logs/daily/2026-09-21.md (2 ledger rows)
15:56:19  INFO        place_all_stops: checking 3 positions...
15:56:19  INFO        STOP skipped DRI: fractional (0.1604 shares) — software exit will handle it
15:56:19  INFO        STOP skipped EQIX: fractional (0.0327 shares) — software exit will handle it
15:56:19  INFO        STOP skipped SCHW: fractional (0.3194 shares) — software exit will handle it
15:56:19  INFO        [positions] 3/3 (3 valid)
15:56:20  INFO        Daily log -> logs/daily/2026-09-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:56 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.63|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  DRI  P&L +0.3%  $+0.12                                            HOLD|
|  SCHW  P&L +0.5%  $+0.16                                           HOLD|
|  EQIX  P&L +0.8%  $+0.26                                           HOLD|
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
=== options_live_micro LIVE 2026-09-21T11:56:21.002794-04:00 share=25% ===
2026-09-21 11:56:21,002 INFO === options_live_micro LIVE 2026-09-21T11:56:21.002794-04:00 share=25% ===
Live account equity $226.63 cash $124.40 #225458845 options_level=3
2026-09-21 11:56:21,227 INFO Live account equity $226.63 cash $124.40 #225458845 options_level=3
Live micro: manage/exits only
2026-09-21 11:56:21,449 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-21 11:56:21,518 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (198 earlier lines - see full log file)

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
## Ledger health — 2026-09-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1430 | WARN | <<<
| Missing exit records (post) |  1427 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1367 med=-12.5% | TAINTED n=1882 med=-38.9% | KEEP-only n=751 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.63 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260921T160121Z

- UTC timestamp: `20260921T160121Z`
- GitHub run: [#10539](https://github.com/28twagg-ops/TradingBot/actions/runs/35622714747)
- Run id: `35622714747`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`149s`
- Full logs: `logs/action_runs/20260921T160121Z_live_bot.log`, `logs/action_runs/20260921T160121Z_live_options.log`, `logs/action_runs/20260921T160121Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T12:01:28.230723-04:00","date":"2026-09-21","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":137.4,"phases_s":{"reconcile":2.47,"cancel":0.18,"manage":122.27,"protective_stops":3.39},"signals":0,"placed":0,"equity":997158.09,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10539","github_run_id":"35622714747","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
16:01:22  INFO      Mode: exits
16:01:23  INFO        Daily log -> logs/daily/2026-09-21.md
16:01:23  INFO        Daily log reconciled -> logs/daily/2026-09-21.md (2 ledger rows)
16:01:23  INFO        place_all_stops: checking 3 positions...
16:01:23  INFO        STOP skipped DRI: fractional (0.1604 shares) — software exit will handle it
16:01:23  INFO        STOP skipped EQIX: fractional (0.0327 shares) — software exit will handle it
16:01:23  INFO        STOP skipped SCHW: fractional (0.3194 shares) — software exit will handle it
16:01:23  INFO        [positions] 3/3 (3 valid)
16:01:24  INFO        Daily log -> logs/daily/2026-09-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.71|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  DRI  P&L +0.4%  $+0.14                                            HOLD|
|  SCHW  P&L +0.4%  $+0.15                                           HOLD|
|  EQIX  P&L +0.9%  $+0.32                                           HOLD|
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
=== options_live_micro LIVE 2026-09-21T12:01:24.958437-04:00 share=25% ===
2026-09-21 12:01:24,958 INFO === options_live_micro LIVE 2026-09-21T12:01:24.958437-04:00 share=25% ===
Live account equity $226.70 cash $124.40 #225458845 options_level=3
2026-09-21 12:01:25,153 INFO Live account equity $226.70 cash $124.40 #225458845 options_level=3
Live micro: manage/exits only
2026-09-21 12:01:25,314 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-21 12:01:25,365 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (198 earlier lines - see full log file)

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
## Ledger health — 2026-09-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1430 | WARN | <<<
| Missing exit records (post) |  1427 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1367 med=-12.5% | TAINTED n=1882 med=-38.9% | KEEP-only n=751 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260921T160609Z

- UTC timestamp: `20260921T160609Z`
- GitHub run: [#10540](https://github.com/28twagg-ops/TradingBot/actions/runs/35623280143)
- Run id: `35623280143`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`138s`
- Full logs: `logs/action_runs/20260921T160609Z_live_bot.log`, `logs/action_runs/20260921T160609Z_live_options.log`, `logs/action_runs/20260921T160609Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T12:06:14.504312-04:00","date":"2026-09-21","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":125.9,"phases_s":{"reconcile":2.16,"cancel":0.04,"manage":113.96,"protective_stops":1.02},"signals":0,"placed":0,"equity":997158.09,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10540","github_run_id":"35623280143","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
16:06:10  INFO      Mode: exits
16:06:10  INFO        Daily log -> logs/daily/2026-09-21.md
16:06:10  INFO        Daily log reconciled -> logs/daily/2026-09-21.md (2 ledger rows)
16:06:10  INFO        place_all_stops: checking 3 positions...
16:06:10  INFO        STOP skipped DRI: fractional (0.1604 shares) — software exit will handle it
16:06:10  INFO        STOP skipped EQIX: fractional (0.0327 shares) — software exit will handle it
16:06:10  INFO        STOP skipped SCHW: fractional (0.3194 shares) — software exit will handle it
16:06:10  INFO        [positions] 3/3 (3 valid)
16:06:10  INFO        Daily log -> logs/daily/2026-09-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.80|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  DRI  P&L +0.4%  $+0.15                                            HOLD|
|  SCHW  P&L +0.5%  $+0.15                                           HOLD|
|  EQIX  P&L +1.2%  $+0.40                                           HOLD|
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
=== options_live_micro LIVE 2026-09-21T12:06:11.717297-04:00 share=25% ===
2026-09-21 12:06:11,717 INFO === options_live_micro LIVE 2026-09-21T12:06:11.717297-04:00 share=25% ===
Live account equity $226.80 cash $124.40 #225458845 options_level=3
2026-09-21 12:06:11,780 INFO Live account equity $226.80 cash $124.40 #225458845 options_level=3
Live micro: manage/exits only
2026-09-21 12:06:11,826 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-21 12:06:11,837 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (198 earlier lines - see full log file)

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
## Ledger health — 2026-09-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1430 | WARN | <<<
| Missing exit records (post) |  1427 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1367 med=-12.5% | TAINTED n=1882 med=-38.9% | KEEP-only n=751 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.8 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260921T161113Z

- UTC timestamp: `20260921T161113Z`
- GitHub run: [#10541](https://github.com/28twagg-ops/TradingBot/actions/runs/35623842906)
- Run id: `35623842906`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`125s`
- Full logs: `logs/action_runs/20260921T161113Z_live_bot.log`, `logs/action_runs/20260921T161113Z_live_options.log`, `logs/action_runs/20260921T161113Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T12:11:17.013451-04:00","date":"2026-09-21","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":116.2,"phases_s":{"reconcile":2.1,"cancel":0.02,"manage":104.86,"protective_stops":0.72},"signals":0,"placed":0,"equity":997158.09,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10541","github_run_id":"35623842906","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
16:11:14  INFO      Mode: exits
16:11:14  INFO        Daily log -> logs/daily/2026-09-21.md
16:11:14  INFO        Daily log reconciled -> logs/daily/2026-09-21.md (2 ledger rows)
16:11:14  INFO        place_all_stops: checking 3 positions...
16:11:14  INFO        STOP skipped DRI: fractional (0.1604 shares) — software exit will handle it
16:11:14  INFO        STOP skipped EQIX: fractional (0.0327 shares) — software exit will handle it
16:11:14  INFO        STOP skipped SCHW: fractional (0.3194 shares) — software exit will handle it
16:11:14  INFO        [positions] 3/3 (3 valid)
16:11:14  INFO        Daily log -> logs/daily/2026-09-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.88|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  DRI  P&L +0.6%  $+0.20                                            HOLD|
|  SCHW  P&L +0.7%  $+0.23                                           HOLD|
|  EQIX  P&L +1.1%  $+0.36                                           HOLD|
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
=== options_live_micro LIVE 2026-09-21T12:11:14.968289-04:00 share=25% ===
2026-09-21 12:11:14,968 INFO === options_live_micro LIVE 2026-09-21T12:11:14.968289-04:00 share=25% ===
Live account equity $226.88 cash $124.40 #225458845 options_level=3
2026-09-21 12:11:15,005 INFO Live account equity $226.88 cash $124.40 #225458845 options_level=3
Live micro: manage/exits only
2026-09-21 12:11:15,027 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-21 12:11:15,034 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (196 earlier lines - see full log file)

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
## Ledger health — 2026-09-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1430 | WARN | <<<
| Missing exit records (post) |  1427 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1367 med=-12.5% | TAINTED n=1882 med=-38.9% | KEEP-only n=751 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.88 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260921T161644Z

- UTC timestamp: `20260921T161644Z`
- GitHub run: [#10542](https://github.com/28twagg-ops/TradingBot/actions/runs/35624388813)
- Run id: `35624388813`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`146s`
- Full logs: `logs/action_runs/20260921T161644Z_live_bot.log`, `logs/action_runs/20260921T161644Z_live_options.log`, `logs/action_runs/20260921T161644Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T12:16:50.737919-04:00","date":"2026-09-21","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":134.4,"phases_s":{"reconcile":2.17,"cancel":0.03,"manage":122.65,"protective_stops":0.91},"signals":0,"placed":0,"equity":997158.09,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10542","github_run_id":"35624388813","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
16:16:46  INFO      Mode: exits
16:16:47  INFO        Daily log -> logs/daily/2026-09-21.md
16:16:47  INFO        Daily log reconciled -> logs/daily/2026-09-21.md (2 ledger rows)
16:16:47  INFO        place_all_stops: checking 3 positions...
16:16:47  INFO        STOP skipped DRI: fractional (0.1604 shares) — software exit will handle it
16:16:47  INFO        STOP skipped EQIX: fractional (0.0327 shares) — software exit will handle it
16:16:47  INFO        STOP skipped SCHW: fractional (0.3194 shares) — software exit will handle it
16:16:47  INFO        [positions] 3/3 (3 valid)
16:16:47  INFO        Daily log -> logs/daily/2026-09-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.84|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  DRI  P&L +0.3%  $+0.10                                            HOLD|
|  SCHW  P&L +0.6%  $+0.22                                           HOLD|
|  EQIX  P&L +1.2%  $+0.42                                           HOLD|
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
=== options_live_micro LIVE 2026-09-21T12:16:48.120203-04:00 share=25% ===
2026-09-21 12:16:48,120 INFO === options_live_micro LIVE 2026-09-21T12:16:48.120203-04:00 share=25% ===
Live account equity $226.84 cash $124.40 #225458845 options_level=3
2026-09-21 12:16:48,165 INFO Live account equity $226.84 cash $124.40 #225458845 options_level=3
Live micro: manage/exits only
2026-09-21 12:16:48,190 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-21 12:16:48,198 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (200 earlier lines - see full log file)

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
## Ledger health — 2026-09-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1430 | WARN | <<<
| Missing exit records (post) |  1427 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1367 med=-12.5% | TAINTED n=1882 med=-38.9% | KEEP-only n=751 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.84 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260921T162109Z

- UTC timestamp: `20260921T162109Z`
- GitHub run: [#10543](https://github.com/28twagg-ops/TradingBot/actions/runs/35624920292)
- Run id: `35624920292`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`151s`
- Full logs: `logs/action_runs/20260921T162109Z_live_bot.log`, `logs/action_runs/20260921T162109Z_live_options.log`, `logs/action_runs/20260921T162109Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T12:21:15.400717-04:00","date":"2026-09-21","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":140.4,"phases_s":{"reconcile":2.35,"cancel":0.11,"manage":126.86,"protective_stops":2.33},"signals":0,"placed":0,"equity":997158.09,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10543","github_run_id":"35624920292","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
16:21:10  INFO      Mode: exits
16:21:10  INFO        Daily log -> logs/daily/2026-09-21.md
16:21:10  INFO        Daily log reconciled -> logs/daily/2026-09-21.md (2 ledger rows)
16:21:10  INFO        place_all_stops: checking 3 positions...
16:21:10  INFO        STOP skipped DRI: fractional (0.1604 shares) — software exit will handle it
16:21:10  INFO        STOP skipped EQIX: fractional (0.0327 shares) — software exit will handle it
16:21:10  INFO        STOP skipped SCHW: fractional (0.3194 shares) — software exit will handle it
16:21:11  INFO        [positions] 3/3 (3 valid)
16:21:11  INFO        Daily log -> logs/daily/2026-09-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.83|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  DRI  P&L +0.3%  $+0.11                                            HOLD|
|  SCHW  P&L +0.6%  $+0.21                                           HOLD|
|  EQIX  P&L +1.2%  $+0.42                                           HOLD|
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
=== options_live_micro LIVE 2026-09-21T12:21:11.987739-04:00 share=25% ===
2026-09-21 12:21:11,987 INFO === options_live_micro LIVE 2026-09-21T12:21:11.987739-04:00 share=25% ===
Live account equity $226.83 cash $124.40 #225458845 options_level=3
2026-09-21 12:21:12,167 INFO Live account equity $226.83 cash $124.40 #225458845 options_level=3
Live micro: manage/exits only
2026-09-21 12:21:12,434 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-21 12:21:12,481 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (200 earlier lines - see full log file)

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
## Ledger health — 2026-09-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1430 | WARN | <<<
| Missing exit records (post) |  1427 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1367 med=-12.5% | TAINTED n=1882 med=-38.9% | KEEP-only n=751 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.83 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260921T162610Z

- UTC timestamp: `20260921T162610Z`
- GitHub run: [#10544](https://github.com/28twagg-ops/TradingBot/actions/runs/35625459158)
- Run id: `35625459158`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`170s`
- Full logs: `logs/action_runs/20260921T162610Z_live_bot.log`, `logs/action_runs/20260921T162610Z_live_options.log`, `logs/action_runs/20260921T162610Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T12:26:17.780385-04:00","date":"2026-09-21","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":157.0,"phases_s":{"reconcile":2.55,"cancel":0.22,"manage":141.29,"protective_stops":3.73},"signals":0,"placed":0,"equity":997158.09,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10544","github_run_id":"35625459158","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
16:26:11  INFO      Mode: exits
16:26:12  INFO        Daily log -> logs/daily/2026-09-21.md
16:26:12  INFO        Daily log reconciled -> logs/daily/2026-09-21.md (2 ledger rows)
16:26:12  INFO        place_all_stops: checking 3 positions...
16:26:12  INFO        STOP skipped DRI: fractional (0.1604 shares) — software exit will handle it
16:26:12  INFO        STOP skipped EQIX: fractional (0.0327 shares) — software exit will handle it
16:26:12  INFO        STOP skipped SCHW: fractional (0.3194 shares) — software exit will handle it
16:26:13  INFO        [positions] 3/3 (3 valid)
16:26:13  INFO        Daily log -> logs/daily/2026-09-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.85|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  DRI  P&L +0.2%  $+0.08                                            HOLD|
|  SCHW  P&L +0.6%  $+0.19                                           HOLD|
|  EQIX  P&L +1.4%  $+0.47                                           HOLD|
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
=== options_live_micro LIVE 2026-09-21T12:26:14.224175-04:00 share=25% ===
2026-09-21 12:26:14,224 INFO === options_live_micro LIVE 2026-09-21T12:26:14.224175-04:00 share=25% ===
Live account equity $226.85 cash $124.40 #225458845 options_level=3
2026-09-21 12:26:14,446 INFO Live account equity $226.85 cash $124.40 #225458845 options_level=3
Live micro: manage/exits only
2026-09-21 12:26:14,652 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-21 12:26:14,720 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (202 earlier lines - see full log file)

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
## Ledger health — 2026-09-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1430 | WARN | <<<
| Missing exit records (post) |  1427 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1367 med=-12.5% | TAINTED n=1882 med=-38.9% | KEEP-only n=751 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.85 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260921T163134Z

- UTC timestamp: `20260921T163134Z`
- GitHub run: [#10545](https://github.com/28twagg-ops/TradingBot/actions/runs/35625986630)
- Run id: `35625986630`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`159s`
- Full logs: `logs/action_runs/20260921T163134Z_live_bot.log`, `logs/action_runs/20260921T163134Z_live_options.log`, `logs/action_runs/20260921T163134Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T12:31:41.814858-04:00","date":"2026-09-21","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":146.4,"phases_s":{"reconcile":2.45,"cancel":0.18,"manage":131.36,"protective_stops":3.36},"signals":0,"placed":0,"equity":997158.09,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10545","github_run_id":"35625986630","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
16:31:35  INFO      Mode: exits
16:31:36  INFO        Daily log -> logs/daily/2026-09-21.md
16:31:36  INFO        Daily log reconciled -> logs/daily/2026-09-21.md (2 ledger rows)
16:31:36  INFO        place_all_stops: checking 3 positions...
16:31:36  INFO        STOP skipped DRI: fractional (0.1604 shares) — software exit will handle it
16:31:36  INFO        STOP skipped EQIX: fractional (0.0327 shares) — software exit will handle it
16:31:36  INFO        STOP skipped SCHW: fractional (0.3194 shares) — software exit will handle it
16:31:37  INFO        [positions] 3/3 (3 valid)
16:31:37  INFO        Daily log -> logs/daily/2026-09-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.98|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  DRI  P&L +0.4%  $+0.12                                            HOLD|
|  SCHW  P&L +0.6%  $+0.21                                           HOLD|
|  EQIX  P&L +1.6%  $+0.54                                           HOLD|
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
=== options_live_micro LIVE 2026-09-21T12:31:38.383148-04:00 share=25% ===
2026-09-21 12:31:38,383 INFO === options_live_micro LIVE 2026-09-21T12:31:38.383148-04:00 share=25% ===
Live account equity $226.98 cash $124.40 #225458845 options_level=3
2026-09-21 12:31:38,590 INFO Live account equity $226.98 cash $124.40 #225458845 options_level=3
Live micro: manage/exits only
2026-09-21 12:31:38,763 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-21 12:31:38,820 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (200 earlier lines - see full log file)

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
## Ledger health — 2026-09-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1430 | WARN | <<<
| Missing exit records (post) |  1427 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1367 med=-12.5% | TAINTED n=1882 med=-38.9% | KEEP-only n=751 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.98 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260921T163614Z

- UTC timestamp: `20260921T163614Z`
- GitHub run: [#10546](https://github.com/28twagg-ops/TradingBot/actions/runs/35626522549)
- Run id: `35626522549`
- Live bot: exit=`0`, duration=`5s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`164s`
- Full logs: `logs/action_runs/20260921T163614Z_live_bot.log`, `logs/action_runs/20260921T163614Z_live_options.log`, `logs/action_runs/20260921T163614Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T12:36:24.839711-04:00","date":"2026-09-21","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":150.9,"phases_s":{"reconcile":2.6,"cancel":0.24,"manage":134.45,"protective_stops":4.23},"signals":0,"placed":0,"equity":997158.09,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10546","github_run_id":"35626522549","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
16:36:17  INFO      Mode: exits
16:36:18  INFO        Daily log -> logs/daily/2026-09-21.md
16:36:18  INFO        Daily log reconciled -> logs/daily/2026-09-21.md (2 ledger rows)
16:36:18  INFO        place_all_stops: checking 3 positions...
16:36:18  INFO        STOP skipped DRI: fractional (0.1604 shares) — software exit will handle it
16:36:18  INFO        STOP skipped EQIX: fractional (0.0327 shares) — software exit will handle it
16:36:18  INFO        STOP skipped SCHW: fractional (0.3194 shares) — software exit will handle it
16:36:19  INFO        [positions] 3/3 (3 valid)
16:36:19  INFO        Daily log -> logs/daily/2026-09-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.98|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  DRI  P&L +0.3%  $+0.09                                            HOLD|
|  SCHW  P&L +0.7%  $+0.23                                           HOLD|
|  EQIX  P&L +1.7%  $+0.56                                           HOLD|
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
=== options_live_micro LIVE 2026-09-21T12:36:20.600276-04:00 share=25% ===
2026-09-21 12:36:20,600 INFO === options_live_micro LIVE 2026-09-21T12:36:20.600276-04:00 share=25% ===
Live account equity $226.99 cash $124.40 #225458845 options_level=3
2026-09-21 12:36:20,853 INFO Live account equity $226.99 cash $124.40 #225458845 options_level=3
Live micro: manage/exits only
2026-09-21 12:36:21,083 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-21 12:36:21,160 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (200 earlier lines - see full log file)

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
## Ledger health — 2026-09-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1430 | WARN | <<<
| Missing exit records (post) |  1427 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1367 med=-12.5% | TAINTED n=1882 med=-38.9% | KEEP-only n=751 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.98 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260921T164109Z

- UTC timestamp: `20260921T164109Z`
- GitHub run: [#10547](https://github.com/28twagg-ops/TradingBot/actions/runs/35627061573)
- Run id: `35627061573`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`150s`
- Full logs: `logs/action_runs/20260921T164109Z_live_bot.log`, `logs/action_runs/20260921T164109Z_live_options.log`, `logs/action_runs/20260921T164109Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T12:41:14.672049-04:00","date":"2026-09-21","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":142.4,"phases_s":{"reconcile":2.31,"cancel":0.12,"manage":128.84,"protective_stops":2.4},"signals":0,"placed":0,"equity":997158.09,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10547","github_run_id":"35627061573","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
16:41:10  INFO      Mode: exits
16:41:11  INFO        Daily log -> logs/daily/2026-09-21.md
16:41:11  INFO        Daily log reconciled -> logs/daily/2026-09-21.md (2 ledger rows)
16:41:11  INFO        place_all_stops: checking 3 positions...
16:41:11  INFO        STOP skipped DRI: fractional (0.1604 shares) — software exit will handle it
16:41:11  INFO        STOP skipped EQIX: fractional (0.0327 shares) — software exit will handle it
16:41:11  INFO        STOP skipped SCHW: fractional (0.3194 shares) — software exit will handle it
16:41:11  INFO        [positions] 3/3 (3 valid)
16:41:11  INFO        Daily log -> logs/daily/2026-09-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.92|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  DRI  P&L +0.2%  $+0.07                                            HOLD|
|  SCHW  P&L +0.6%  $+0.21                                           HOLD|
|  EQIX  P&L +1.6%  $+0.55                                           HOLD|
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
=== options_live_micro LIVE 2026-09-21T12:41:12.132245-04:00 share=25% ===
2026-09-21 12:41:12,132 INFO === options_live_micro LIVE 2026-09-21T12:41:12.132245-04:00 share=25% ===
Live account equity $226.92 cash $124.40 #225458845 options_level=3
2026-09-21 12:41:12,268 INFO Live account equity $226.92 cash $124.40 #225458845 options_level=3
Live micro: manage/exits only
2026-09-21 12:41:12,381 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-21 12:41:12,416 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (200 earlier lines - see full log file)

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
## Ledger health — 2026-09-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1430 | WARN | <<<
| Missing exit records (post) |  1427 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1367 med=-12.5% | TAINTED n=1882 med=-38.9% | KEEP-only n=751 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.92 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260921T164608Z

- UTC timestamp: `20260921T164608Z`
- GitHub run: [#10548](https://github.com/28twagg-ops/TradingBot/actions/runs/35627584560)
- Run id: `35627584560`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`145s`
- Full logs: `logs/action_runs/20260921T164608Z_live_bot.log`, `logs/action_runs/20260921T164608Z_live_options.log`, `logs/action_runs/20260921T164608Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T12:46:13.445179-04:00","date":"2026-09-21","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":134.0,"phases_s":{"reconcile":2.14,"cancel":0.11,"manage":122.18,"protective_stops":0.93},"signals":0,"placed":0,"equity":997158.09,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10548","github_run_id":"35627584560","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
16:46:09  INFO      Mode: exits
16:46:09  INFO        Daily log -> logs/daily/2026-09-21.md
16:46:09  INFO        Daily log reconciled -> logs/daily/2026-09-21.md (2 ledger rows)
16:46:09  INFO        place_all_stops: checking 3 positions...
16:46:09  INFO        STOP skipped DRI: fractional (0.1604 shares) — software exit will handle it
16:46:09  INFO        STOP skipped EQIX: fractional (0.0327 shares) — software exit will handle it
16:46:09  INFO        STOP skipped SCHW: fractional (0.3194 shares) — software exit will handle it
16:46:09  INFO        [positions] 3/3 (3 valid)
16:46:10  INFO        Daily log -> logs/daily/2026-09-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.73|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  DRI  P&L -0.5%  $-0.15                                            HOLD|
|  SCHW  P&L +0.7%  $+0.24                                           HOLD|
|  EQIX  P&L +1.8%  $+0.62                                           HOLD|
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
=== options_live_micro LIVE 2026-09-21T12:46:10.807320-04:00 share=25% ===
2026-09-21 12:46:10,807 INFO === options_live_micro LIVE 2026-09-21T12:46:10.807320-04:00 share=25% ===
Live account equity $226.80 cash $124.40 #225458845 options_level=3
2026-09-21 12:46:10,867 INFO Live account equity $226.80 cash $124.40 #225458845 options_level=3
Live micro: manage/exits only
2026-09-21 12:46:10,902 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-21 12:46:10,912 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (200 earlier lines - see full log file)

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
## Ledger health — 2026-09-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1430 | WARN | <<<
| Missing exit records (post) |  1427 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1367 med=-12.5% | TAINTED n=1882 med=-38.9% | KEEP-only n=751 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.8 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260921T165109Z

- UTC timestamp: `20260921T165109Z`
- GitHub run: [#10549](https://github.com/28twagg-ops/TradingBot/actions/runs/35628117808)
- Run id: `35628117808`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`162s`
- Full logs: `logs/action_runs/20260921T165109Z_live_bot.log`, `logs/action_runs/20260921T165109Z_live_options.log`, `logs/action_runs/20260921T165109Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T12:51:16.764550-04:00","date":"2026-09-21","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":151.0,"phases_s":{"reconcile":2.46,"cancel":0.18,"manage":136.14,"protective_stops":3.28},"signals":0,"placed":0,"equity":997158.09,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10549","github_run_id":"35628117808","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
16:51:11  INFO      Mode: exits
16:51:12  INFO        Daily log -> logs/daily/2026-09-21.md
16:51:12  INFO        Daily log reconciled -> logs/daily/2026-09-21.md (2 ledger rows)
16:51:12  INFO        place_all_stops: checking 3 positions...
16:51:12  INFO        STOP skipped DRI: fractional (0.1604 shares) — software exit will handle it
16:51:12  INFO        STOP skipped EQIX: fractional (0.0327 shares) — software exit will handle it
16:51:12  INFO        STOP skipped SCHW: fractional (0.3194 shares) — software exit will handle it
16:51:12  INFO        [positions] 3/3 (3 valid)
16:51:12  INFO        Daily log -> logs/daily/2026-09-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:51 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.88|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  DRI  P&L -0.2%  $-0.07                                            HOLD|
|  SCHW  P&L +0.6%  $+0.22                                           HOLD|
|  EQIX  P&L +1.9%  $+0.63                                           HOLD|
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
=== options_live_micro LIVE 2026-09-21T12:51:13.663205-04:00 share=25% ===
2026-09-21 12:51:13,663 INFO === options_live_micro LIVE 2026-09-21T12:51:13.663205-04:00 share=25% ===
Live account equity $226.85 cash $124.40 #225458845 options_level=3
2026-09-21 12:51:13,866 INFO Live account equity $226.85 cash $124.40 #225458845 options_level=3
Live micro: manage/exits only
2026-09-21 12:51:14,048 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-21 12:51:14,109 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (201 earlier lines - see full log file)

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
## Ledger health — 2026-09-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1430 | WARN | <<<
| Missing exit records (post) |  1427 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1367 med=-12.5% | TAINTED n=1882 med=-38.9% | KEEP-only n=751 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.88 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260921T165611Z

- UTC timestamp: `20260921T165611Z`
- GitHub run: [#10550](https://github.com/28twagg-ops/TradingBot/actions/runs/35628650299)
- Run id: `35628650299`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`158s`
- Full logs: `logs/action_runs/20260921T165611Z_live_bot.log`, `logs/action_runs/20260921T165611Z_live_options.log`, `logs/action_runs/20260921T165611Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T12:56:17.290967-04:00","date":"2026-09-21","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":146.4,"phases_s":{"reconcile":2.37,"cancel":0.14,"manage":132.13,"protective_stops":2.77},"signals":0,"placed":0,"equity":997158.09,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10550","github_run_id":"35628650299","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
16:56:12  INFO      Mode: exits
16:56:12  INFO        Daily log -> logs/daily/2026-09-21.md
16:56:12  INFO        Daily log reconciled -> logs/daily/2026-09-21.md (2 ledger rows)
16:56:12  INFO        place_all_stops: checking 3 positions...
16:56:12  INFO        STOP skipped DRI: fractional (0.1604 shares) — software exit will handle it
16:56:12  INFO        STOP skipped EQIX: fractional (0.0327 shares) — software exit will handle it
16:56:12  INFO        STOP skipped SCHW: fractional (0.3194 shares) — software exit will handle it
16:56:13  INFO        [positions] 3/3 (3 valid)
16:56:13  INFO        Daily log -> logs/daily/2026-09-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:56 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.80|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  DRI  P&L -0.2%  $-0.08                                            HOLD|
|  SCHW  P&L +0.7%  $+0.23                                           HOLD|
|  EQIX  P&L +1.6%  $+0.55                                           HOLD|
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
=== options_live_micro LIVE 2026-09-21T12:56:14.267853-04:00 share=25% ===
2026-09-21 12:56:14,267 INFO === options_live_micro LIVE 2026-09-21T12:56:14.267853-04:00 share=25% ===
Live account equity $226.80 cash $124.40 #225458845 options_level=3
2026-09-21 12:56:14,423 INFO Live account equity $226.80 cash $124.40 #225458845 options_level=3
Live micro: manage/exits only
2026-09-21 12:56:14,541 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-21 12:56:14,580 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (201 earlier lines - see full log file)

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
## Ledger health — 2026-09-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1430 | WARN | <<<
| Missing exit records (post) |  1427 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1367 med=-12.5% | TAINTED n=1882 med=-38.9% | KEEP-only n=751 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.8 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260921T170117Z

- UTC timestamp: `20260921T170117Z`
- GitHub run: [#10551](https://github.com/28twagg-ops/TradingBot/actions/runs/35629171613)
- Run id: `35629171613`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`153s`
- Full logs: `logs/action_runs/20260921T170117Z_live_bot.log`, `logs/action_runs/20260921T170117Z_live_options.log`, `logs/action_runs/20260921T170117Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T13:01:22.543879-04:00","date":"2026-09-21","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":140.8,"phases_s":{"reconcile":2.23,"cancel":0.08,"manage":128.25,"protective_stops":1.45},"signals":0,"placed":0,"equity":997158.09,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10551","github_run_id":"35629171613","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
17:01:18  INFO      Mode: exits
17:01:18  INFO        Daily log -> logs/daily/2026-09-21.md
17:01:18  INFO        Daily log reconciled -> logs/daily/2026-09-21.md (2 ledger rows)
17:01:18  INFO        place_all_stops: checking 3 positions...
17:01:18  INFO        STOP skipped DRI: fractional (0.1604 shares) — software exit will handle it
17:01:18  INFO        STOP skipped EQIX: fractional (0.0327 shares) — software exit will handle it
17:01:18  INFO        STOP skipped SCHW: fractional (0.3194 shares) — software exit will handle it
17:01:18  INFO        [positions] 3/3 (3 valid)
17:01:18  INFO        Daily log -> logs/daily/2026-09-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.74|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  DRI  P&L -0.3%  $-0.11                                            HOLD|
|  SCHW  P&L +0.7%  $+0.25                                           HOLD|
|  EQIX  P&L +1.5%  $+0.49                                           HOLD|
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
=== options_live_micro LIVE 2026-09-21T13:01:19.654033-04:00 share=25% ===
2026-09-21 13:01:19,654 INFO === options_live_micro LIVE 2026-09-21T13:01:19.654033-04:00 share=25% ===
Live account equity $226.74 cash $124.40 #225458845 options_level=3
2026-09-21 13:01:19,736 INFO Live account equity $226.74 cash $124.40 #225458845 options_level=3
Live micro: manage/exits only
2026-09-21 13:01:19,799 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-21 13:01:19,820 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (201 earlier lines - see full log file)

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
## Ledger health — 2026-09-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1430 | WARN | <<<
| Missing exit records (post) |  1427 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1367 med=-12.5% | TAINTED n=1882 med=-38.9% | KEEP-only n=751 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.74 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260921T170634Z

- UTC timestamp: `20260921T170634Z`
- GitHub run: [#10552](https://github.com/28twagg-ops/TradingBot/actions/runs/35629714012)
- Run id: `35629714012`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`170s`
- Full logs: `logs/action_runs/20260921T170634Z_live_bot.log`, `logs/action_runs/20260921T170634Z_live_options.log`, `logs/action_runs/20260921T170634Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T13:06:41.696463-04:00","date":"2026-09-21","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":158.4,"phases_s":{"reconcile":2.45,"cancel":0.17,"manage":143.28,"protective_stops":3.51},"signals":0,"placed":0,"equity":997158.09,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10552","github_run_id":"35629714012","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
17:06:35  INFO      Mode: exits
17:06:36  INFO        Daily log -> logs/daily/2026-09-21.md
17:06:36  INFO        Daily log reconciled -> logs/daily/2026-09-21.md (2 ledger rows)
17:06:36  INFO        place_all_stops: checking 3 positions...
17:06:36  INFO        STOP skipped DRI: fractional (0.1604 shares) — software exit will handle it
17:06:36  INFO        STOP skipped EQIX: fractional (0.0327 shares) — software exit will handle it
17:06:36  INFO        STOP skipped SCHW: fractional (0.3194 shares) — software exit will handle it
17:06:36  INFO        [positions] 3/3 (3 valid)
17:06:36  INFO        Daily log -> logs/daily/2026-09-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.66|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  DRI  P&L -0.5%  $-0.15                                            HOLD|
|  SCHW  P&L +0.8%  $+0.27                                           HOLD|
|  EQIX  P&L +1.3%  $+0.44                                           HOLD|
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
=== options_live_micro LIVE 2026-09-21T13:06:37.721266-04:00 share=25% ===
2026-09-21 13:06:37,721 INFO === options_live_micro LIVE 2026-09-21T13:06:37.721266-04:00 share=25% ===
Live account equity $226.67 cash $124.40 #225458845 options_level=3
2026-09-21 13:06:37,931 INFO Live account equity $226.67 cash $124.40 #225458845 options_level=3
Live micro: manage/exits only
2026-09-21 13:06:38,152 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-21 13:06:38,210 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (203 earlier lines - see full log file)

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
## Ledger health — 2026-09-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1430 | WARN | <<<
| Missing exit records (post) |  1427 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1367 med=-12.5% | TAINTED n=1882 med=-38.9% | KEEP-only n=751 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.67 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260921T171118Z

- UTC timestamp: `20260921T171118Z`
- GitHub run: [#10553](https://github.com/28twagg-ops/TradingBot/actions/runs/35630253826)
- Run id: `35630253826`
- Live bot: exit=`0`, duration=`6s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`159s`
- Full logs: `logs/action_runs/20260921T171118Z_live_bot.log`, `logs/action_runs/20260921T171118Z_live_options.log`, `logs/action_runs/20260921T171118Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T13:11:27.922236-04:00","date":"2026-09-21","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":148.9,"phases_s":{"reconcile":2.54,"cancel":0.21,"manage":132.92,"protective_stops":4.15},"signals":0,"placed":0,"equity":997158.09,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10553","github_run_id":"35630253826","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
17:11:19  INFO      Mode: exits
17:11:20  INFO        Daily log -> logs/daily/2026-09-21.md
17:11:20  INFO        Daily log reconciled -> logs/daily/2026-09-21.md (2 ledger rows)
17:11:20  INFO        place_all_stops: checking 3 positions...
17:11:20  INFO        STOP skipped DRI: fractional (0.1604 shares) — software exit will handle it
17:11:20  INFO        STOP skipped EQIX: fractional (0.0327 shares) — software exit will handle it
17:11:20  INFO        STOP skipped SCHW: fractional (0.3194 shares) — software exit will handle it
17:11:20  INFO        [positions] 3/3 (3 valid)
17:11:21  INFO        SELL MARKET [urgent] DRI closed
17:11:23  INFO        TX logged: SELL DRI  P&L -0.56%
17:11:24  INFO        Daily log -> logs/daily/2026-09-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.66|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  DRI  P&L -0.6%  $-0.19                         EXIT: stop_loss (-0.6%)|
|  SCHW  P&L +0.9%  $+0.29                                           HOLD|
|  EQIX  P&L +1.3%  $+0.46                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  1 attempted  |  1 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                2|
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
|  DRI                                         -0.56%  (threshold -0.50%)|
|  Count                                                                1|
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-21T13:11:24.910448-04:00 share=25% ===
2026-09-21 13:11:24,910 INFO === options_live_micro LIVE 2026-09-21T13:11:24.910448-04:00 share=25% ===
Live account equity $226.65 cash $158.11 #225458845 options_level=3
2026-09-21 13:11:25,129 INFO Live account equity $226.65 cash $158.11 #225458845 options_level=3
Live micro: manage/exits only
2026-09-21 13:11:25,333 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-21 13:11:25,402 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (200 earlier lines - see full log file)

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
## Ledger health — 2026-09-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1430 | WARN | <<<
| Missing exit records (post) |  1427 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1367 med=-12.5% | TAINTED n=1882 med=-38.9% | KEEP-only n=751 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.65 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260921T171610Z

- UTC timestamp: `20260921T171610Z`
- GitHub run: [#10554](https://github.com/28twagg-ops/TradingBot/actions/runs/35630794695)
- Run id: `35630794695`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`152s`
- Full logs: `logs/action_runs/20260921T171610Z_live_bot.log`, `logs/action_runs/20260921T171610Z_live_options.log`, `logs/action_runs/20260921T171610Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T13:16:15.887118-04:00","date":"2026-09-21","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":140.9,"phases_s":{"reconcile":2.22,"cancel":0.07,"manage":128.28,"protective_stops":1.7},"signals":0,"placed":0,"equity":997158.09,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10554","github_run_id":"35630794695","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
17:16:11  INFO      Mode: exits
17:16:11  INFO        Daily log -> logs/daily/2026-09-21.md
17:16:11  INFO        Daily log reconciled -> logs/daily/2026-09-21.md (3 ledger rows)
17:16:11  INFO        place_all_stops: checking 2 positions...
17:16:11  INFO        STOP skipped EQIX: fractional (0.0327 shares) — software exit will handle it
17:16:11  INFO        STOP skipped SCHW: fractional (0.3194 shares) — software exit will handle it
17:16:12  INFO        [positions] 2/2 (2 valid)
17:16:12  INFO        Daily log -> logs/daily/2026-09-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.74|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  SCHW  P&L +0.9%  $+0.31                                           HOLD|
|  EQIX  P&L +1.5%  $+0.52                                           HOLD|
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
=== options_live_micro LIVE 2026-09-21T13:16:13.066696-04:00 share=25% ===
2026-09-21 13:16:13,066 INFO === options_live_micro LIVE 2026-09-21T13:16:13.066696-04:00 share=25% ===
Live account equity $226.75 cash $158.11 #225458845 options_level=3
2026-09-21 13:16:13,258 INFO Live account equity $226.75 cash $158.11 #225458845 options_level=3
Live micro: manage/exits only
2026-09-21 13:16:13,322 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-21 13:16:13,343 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (201 earlier lines - see full log file)

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
## Ledger health — 2026-09-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1430 | WARN | <<<
| Missing exit records (post) |  1427 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1367 med=-12.5% | TAINTED n=1882 med=-38.9% | KEEP-only n=751 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.74 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260921T172114Z

- UTC timestamp: `20260921T172114Z`
- GitHub run: [#10555](https://github.com/28twagg-ops/TradingBot/actions/runs/35631333437)
- Run id: `35631333437`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`164s`
- Full logs: `logs/action_runs/20260921T172114Z_live_bot.log`, `logs/action_runs/20260921T172114Z_live_options.log`, `logs/action_runs/20260921T172114Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T13:21:22.555591-04:00","date":"2026-09-21","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":151.3,"phases_s":{"reconcile":2.6,"cancel":0.24,"manage":134.11,"protective_stops":4.6},"signals":0,"placed":0,"equity":997158.09,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10555","github_run_id":"35631333437","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
17:21:15  INFO      Mode: exits
17:21:16  INFO        Daily log -> logs/daily/2026-09-21.md
17:21:16  INFO        Daily log reconciled -> logs/daily/2026-09-21.md (3 ledger rows)
17:21:16  INFO        place_all_stops: checking 2 positions...
17:21:16  INFO        STOP skipped EQIX: fractional (0.0327 shares) — software exit will handle it
17:21:16  INFO        STOP skipped SCHW: fractional (0.3194 shares) — software exit will handle it
17:21:17  INFO        [positions] 2/2 (2 valid)
17:21:17  INFO        Daily log -> logs/daily/2026-09-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.80|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  SCHW  P&L +1.2%  $+0.39                                           HOLD|
|  EQIX  P&L +1.5%  $+0.50                                           HOLD|
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
=== options_live_micro LIVE 2026-09-21T13:21:18.508759-04:00 share=25% ===
2026-09-21 13:21:18,508 INFO === options_live_micro LIVE 2026-09-21T13:21:18.508759-04:00 share=25% ===
Live account equity $226.80 cash $158.11 #225458845 options_level=3
2026-09-21 13:21:18,764 INFO Live account equity $226.80 cash $158.11 #225458845 options_level=3
Live micro: manage/exits only
2026-09-21 13:21:19,003 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-21 13:21:19,080 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (200 earlier lines - see full log file)

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
## Ledger health — 2026-09-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1430 | WARN | <<<
| Missing exit records (post) |  1427 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1367 med=-12.5% | TAINTED n=1882 med=-38.9% | KEEP-only n=751 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.81 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260921T172612Z

- UTC timestamp: `20260921T172612Z`
- GitHub run: [#10556](https://github.com/28twagg-ops/TradingBot/actions/runs/35631866660)
- Run id: `35631866660`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`157s`
- Full logs: `logs/action_runs/20260921T172612Z_live_bot.log`, `logs/action_runs/20260921T172612Z_live_options.log`, `logs/action_runs/20260921T172612Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T13:26:20.269603-04:00","date":"2026-09-21","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":144.9,"phases_s":{"reconcile":2.52,"cancel":0.24,"manage":129.65,"protective_stops":3.41},"signals":0,"placed":0,"equity":997158.09,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10556","github_run_id":"35631866660","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
17:26:14  INFO      Mode: exits
17:26:15  INFO        Daily log -> logs/daily/2026-09-21.md
17:26:15  INFO        Daily log reconciled -> logs/daily/2026-09-21.md (3 ledger rows)
17:26:15  INFO        place_all_stops: checking 2 positions...
17:26:15  INFO        STOP skipped EQIX: fractional (0.0327 shares) — software exit will handle it
17:26:15  INFO        STOP skipped SCHW: fractional (0.3194 shares) — software exit will handle it
17:26:15  INFO        [positions] 2/2 (2 valid)
17:26:16  INFO        Daily log -> logs/daily/2026-09-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.75|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  SCHW  P&L +1.0%  $+0.33                                           HOLD|
|  EQIX  P&L +1.5%  $+0.51                                           HOLD|
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
=== options_live_micro LIVE 2026-09-21T13:26:17.005658-04:00 share=25% ===
2026-09-21 13:26:17,005 INFO === options_live_micro LIVE 2026-09-21T13:26:17.005658-04:00 share=25% ===
Live account equity $226.75 cash $158.11 #225458845 options_level=3
2026-09-21 13:26:17,215 INFO Live account equity $226.75 cash $158.11 #225458845 options_level=3
Live micro: manage/exits only
2026-09-21 13:26:17,395 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-21 13:26:17,454 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (200 earlier lines - see full log file)

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
## Ledger health — 2026-09-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1430 | WARN | <<<
| Missing exit records (post) |  1427 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1367 med=-12.5% | TAINTED n=1882 med=-38.9% | KEEP-only n=751 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.75 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260921T173109Z

- UTC timestamp: `20260921T173109Z`
- GitHub run: [#10557](https://github.com/28twagg-ops/TradingBot/actions/runs/35632396764)
- Run id: `35632396764`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`157s`
- Full logs: `logs/action_runs/20260921T173109Z_live_bot.log`, `logs/action_runs/20260921T173109Z_live_options.log`, `logs/action_runs/20260921T173109Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T13:31:15.540079-04:00","date":"2026-09-21","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":148.7,"phases_s":{"reconcile":2.31,"cancel":0.12,"manage":135.03,"protective_stops":2.51},"signals":0,"placed":0,"equity":997158.09,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10557","github_run_id":"35632396764","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
17:31:10  INFO      Mode: exits
17:31:11  INFO        Daily log -> logs/daily/2026-09-21.md
17:31:11  INFO        Daily log reconciled -> logs/daily/2026-09-21.md (3 ledger rows)
17:31:11  INFO        place_all_stops: checking 2 positions...
17:31:11  INFO        STOP skipped EQIX: fractional (0.0327 shares) — software exit will handle it
17:31:11  INFO        STOP skipped SCHW: fractional (0.3194 shares) — software exit will handle it
17:31:12  INFO        [positions] 2/2 (2 valid)
17:31:12  INFO        Daily log -> logs/daily/2026-09-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.72|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  SCHW  P&L +0.9%  $+0.30                                           HOLD|
|  EQIX  P&L +1.5%  $+0.51                                           HOLD|
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
=== options_live_micro LIVE 2026-09-21T13:31:12.919311-04:00 share=25% ===
2026-09-21 13:31:12,919 INFO === options_live_micro LIVE 2026-09-21T13:31:12.919311-04:00 share=25% ===
Live account equity $226.73 cash $158.11 #225458845 options_level=3
2026-09-21 13:31:13,036 INFO Live account equity $226.73 cash $158.11 #225458845 options_level=3
Live micro: manage/exits only
2026-09-21 13:31:13,130 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-21 13:31:13,161 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (202 earlier lines - see full log file)

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
## Ledger health — 2026-09-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1430 | WARN | <<<
| Missing exit records (post) |  1427 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1367 med=-12.5% | TAINTED n=1882 med=-38.9% | KEEP-only n=751 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.74 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260921T173610Z

- UTC timestamp: `20260921T173610Z`
- GitHub run: [#10558](https://github.com/28twagg-ops/TradingBot/actions/runs/35632938290)
- Run id: `35632938290`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`86s`
- Full logs: `logs/action_runs/20260921T173610Z_live_bot.log`, `logs/action_runs/20260921T173610Z_live_options.log`, `logs/action_runs/20260921T173610Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T13:36:17.913669-04:00","date":"2026-09-21","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":74.7,"phases_s":{"reconcile":2.54,"cancel":0.22,"manage":58.63,"protective_stops":4.2},"signals":0,"placed":0,"equity":997158.09,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10558","github_run_id":"35632938290","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
17:36:12  INFO      Mode: exits
17:36:12  INFO        Daily log -> logs/daily/2026-09-21.md
17:36:12  INFO        Daily log reconciled -> logs/daily/2026-09-21.md (3 ledger rows)
17:36:12  INFO        place_all_stops: checking 2 positions...
17:36:12  INFO        STOP skipped EQIX: fractional (0.0327 shares) — software exit will handle it
17:36:12  INFO        STOP skipped SCHW: fractional (0.3194 shares) — software exit will handle it
17:36:13  INFO        [positions] 2/2 (2 valid)
17:36:13  INFO        Daily log -> logs/daily/2026-09-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.73|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  SCHW  P&L +0.9%  $+0.30                                           HOLD|
|  EQIX  P&L +1.5%  $+0.52                                           HOLD|
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
=== options_live_micro LIVE 2026-09-21T13:36:14.440496-04:00 share=25% ===
2026-09-21 13:36:14,440 INFO === options_live_micro LIVE 2026-09-21T13:36:14.440496-04:00 share=25% ===
Live account equity $226.73 cash $158.11 #225458845 options_level=3
2026-09-21 13:36:14,670 INFO Live account equity $226.73 cash $158.11 #225458845 options_level=3
Live micro: manage/exits only
2026-09-21 13:36:14,878 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-21 13:36:14,944 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (183 earlier lines - see full log file)

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
## Ledger health — 2026-09-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1430 | WARN | <<<
| Missing exit records (post) |  1427 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1367 med=-12.5% | TAINTED n=1882 med=-38.9% | KEEP-only n=751 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.73 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260921T174122Z

- UTC timestamp: `20260921T174122Z`
- GitHub run: [#10559](https://github.com/28twagg-ops/TradingBot/actions/runs/35633458893)
- Run id: `35633458893`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`48s`
- Full logs: `logs/action_runs/20260921T174122Z_live_bot.log`, `logs/action_runs/20260921T174122Z_live_options.log`, `logs/action_runs/20260921T174122Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T13:41:28.876323-04:00","date":"2026-09-21","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":36.4,"phases_s":{"reconcile":2.15,"cancel":0.03,"manage":24.56,"protective_stops":1.0},"signals":0,"placed":0,"equity":997158.09,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10559","github_run_id":"35633458893","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
17:41:24  INFO      Mode: exits
17:41:25  INFO        Daily log -> logs/daily/2026-09-21.md
17:41:25  INFO        Daily log reconciled -> logs/daily/2026-09-21.md (3 ledger rows)
17:41:25  INFO        place_all_stops: checking 2 positions...
17:41:25  INFO        STOP skipped EQIX: fractional (0.0327 shares) — software exit will handle it
17:41:25  INFO        STOP skipped SCHW: fractional (0.3194 shares) — software exit will handle it
17:41:25  INFO        [positions] 2/2 (2 valid)
17:41:25  INFO        Daily log -> logs/daily/2026-09-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.72|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  SCHW  P&L +0.9%  $+0.29                                           HOLD|
|  EQIX  P&L +1.5%  $+0.52                                           HOLD|
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
=== options_live_micro LIVE 2026-09-21T13:41:26.144851-04:00 share=25% ===
2026-09-21 13:41:26,144 INFO === options_live_micro LIVE 2026-09-21T13:41:26.144851-04:00 share=25% ===
Live account equity $226.72 cash $158.11 #225458845 options_level=3
2026-09-21 13:41:26,191 INFO Live account equity $226.72 cash $158.11 #225458845 options_level=3
Live micro: manage/exits only
2026-09-21 13:41:26,215 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-21 13:41:26,223 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (176 earlier lines - see full log file)

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
## Ledger health — 2026-09-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1430 | WARN | <<<
| Missing exit records (post) |  1427 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1367 med=-12.5% | TAINTED n=1882 med=-38.9% | KEEP-only n=751 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.72 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260921T174613Z

- UTC timestamp: `20260921T174613Z`
- GitHub run: [#10560](https://github.com/28twagg-ops/TradingBot/actions/runs/35633981860)
- Run id: `35633981860`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`77s`
- Full logs: `logs/action_runs/20260921T174613Z_live_bot.log`, `logs/action_runs/20260921T174613Z_live_options.log`, `logs/action_runs/20260921T174613Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T13:46:20.607980-04:00","date":"2026-09-21","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":66.2,"phases_s":{"reconcile":2.2,"cancel":0.07,"manage":53.67,"protective_stops":1.56},"signals":0,"placed":0,"equity":997158.09,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10560","github_run_id":"35633981860","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
17:46:16  INFO      Mode: exits
17:46:16  INFO        Daily log -> logs/daily/2026-09-21.md
17:46:16  INFO        Daily log reconciled -> logs/daily/2026-09-21.md (3 ledger rows)
17:46:16  INFO        place_all_stops: checking 2 positions...
17:46:16  INFO        STOP skipped EQIX: fractional (0.0327 shares) — software exit will handle it
17:46:16  INFO        STOP skipped SCHW: fractional (0.3194 shares) — software exit will handle it
17:46:16  INFO        [positions] 2/2 (2 valid)
17:46:16  INFO        Daily log -> logs/daily/2026-09-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.77|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  SCHW  P&L +0.9%  $+0.30                                           HOLD|
|  EQIX  P&L +1.7%  $+0.56                                           HOLD|
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
=== options_live_micro LIVE 2026-09-21T13:46:17.773844-04:00 share=25% ===
2026-09-21 13:46:17,773 INFO === options_live_micro LIVE 2026-09-21T13:46:17.773844-04:00 share=25% ===
Live account equity $226.77 cash $158.11 #225458845 options_level=3
2026-09-21 13:46:17,860 INFO Live account equity $226.77 cash $158.11 #225458845 options_level=3
Live micro: manage/exits only
2026-09-21 13:46:17,929 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-21 13:46:17,950 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (183 earlier lines - see full log file)

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
## Ledger health — 2026-09-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1430 | WARN | <<<
| Missing exit records (post) |  1427 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1367 med=-12.5% | TAINTED n=1882 med=-38.9% | KEEP-only n=751 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.77 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260921T175114Z

- UTC timestamp: `20260921T175114Z`
- GitHub run: [#10561](https://github.com/28twagg-ops/TradingBot/actions/runs/35634506737)
- Run id: `35634506737`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`78s`
- Full logs: `logs/action_runs/20260921T175114Z_live_bot.log`, `logs/action_runs/20260921T175114Z_live_options.log`, `logs/action_runs/20260921T175114Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T13:51:20.703015-04:00","date":"2026-09-21","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":66.0,"phases_s":{"reconcile":2.23,"cancel":0.07,"manage":53.25,"protective_stops":1.68},"signals":0,"placed":0,"equity":997158.09,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10561","github_run_id":"35634506737","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
17:51:16  INFO      Mode: exits
17:51:16  INFO        Daily log -> logs/daily/2026-09-21.md
17:51:16  INFO        Daily log reconciled -> logs/daily/2026-09-21.md (3 ledger rows)
17:51:16  INFO        place_all_stops: checking 2 positions...
17:51:16  INFO        STOP skipped EQIX: fractional (0.0327 shares) — software exit will handle it
17:51:16  INFO        STOP skipped SCHW: fractional (0.3194 shares) — software exit will handle it
17:51:16  INFO        [positions] 2/2 (2 valid)
17:51:16  INFO        Daily log -> logs/daily/2026-09-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:51 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.73|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  SCHW  P&L +0.8%  $+0.28                                           HOLD|
|  EQIX  P&L +1.6%  $+0.54                                           HOLD|
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
=== options_live_micro LIVE 2026-09-21T13:51:17.605273-04:00 share=25% ===
2026-09-21 13:51:17,605 INFO === options_live_micro LIVE 2026-09-21T13:51:17.605273-04:00 share=25% ===
Live account equity $226.75 cash $158.11 #225458845 options_level=3
2026-09-21 13:51:17,686 INFO Live account equity $226.75 cash $158.11 #225458845 options_level=3
Live micro: manage/exits only
2026-09-21 13:51:17,747 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-21 13:51:17,781 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (183 earlier lines - see full log file)

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
## Ledger health — 2026-09-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1430 | WARN | <<<
| Missing exit records (post) |  1427 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1367 med=-12.5% | TAINTED n=1882 med=-38.9% | KEEP-only n=751 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.75 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260921T175614Z

- UTC timestamp: `20260921T175614Z`
- GitHub run: [#10562](https://github.com/28twagg-ops/TradingBot/actions/runs/35635020622)
- Run id: `35635020622`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`88s`
- Full logs: `logs/action_runs/20260921T175614Z_live_bot.log`, `logs/action_runs/20260921T175614Z_live_options.log`, `logs/action_runs/20260921T175614Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1367 | 49.2 | -12.5 | +44.2 | $+17,587 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 751 | 61.9 | +51.4 | +69.9 | $+12,368 |
| KEEP-only recent | 557 | 60.1 | +53.6 | +81.0 | $+8,146 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-21T13:56:22.375363-04:00","date":"2026-09-21","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":75.5,"phases_s":{"reconcile":2.55,"cancel":0.23,"manage":59.27,"protective_stops":4.17},"signals":0,"placed":0,"equity":997158.09,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10562","github_run_id":"35635020622","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
17:56:16  INFO      Mode: exits
17:56:17  INFO        Daily log -> logs/daily/2026-09-21.md
17:56:17  INFO        Daily log reconciled -> logs/daily/2026-09-21.md (3 ledger rows)
17:56:17  INFO        place_all_stops: checking 2 positions...
17:56:17  INFO        STOP skipped EQIX: fractional (0.0327 shares) — software exit will handle it
17:56:17  INFO        STOP skipped SCHW: fractional (0.3194 shares) — software exit will handle it
17:56:17  INFO        [positions] 2/2 (2 valid)
17:56:17  INFO        Daily log -> logs/daily/2026-09-21.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:56 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.72|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  SCHW  P&L +0.8%  $+0.26                                           HOLD|
|  EQIX  P&L +1.6%  $+0.54                                           HOLD|
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
=== options_live_micro LIVE 2026-09-21T13:56:18.743204-04:00 share=25% ===
2026-09-21 13:56:18,743 INFO === options_live_micro LIVE 2026-09-21T13:56:18.743204-04:00 share=25% ===
Live account equity $226.72 cash $158.11 #225458845 options_level=3
2026-09-21 13:56:18,967 INFO Live account equity $226.72 cash $158.11 #225458845 options_level=3
Live micro: manage/exits only
2026-09-21 13:56:19,174 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-21 13:56:19,242 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (183 earlier lines - see full log file)

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
## Ledger health — 2026-09-21
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1430 | WARN | <<<
| Missing exit records (post) |  1427 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-21_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1367 med=-12.5% | TAINTED n=1882 med=-38.9% | KEEP-only n=751 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.72 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---
