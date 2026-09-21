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
