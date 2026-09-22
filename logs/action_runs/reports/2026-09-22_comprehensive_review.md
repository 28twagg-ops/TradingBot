# Daily Comprehensive Action Review - 2026-09-22

_Auto-generated from GitHub Actions run output. Each run appends a summary; full stdout is in linked per-run log files._
## Run 20260922T130119Z

- UTC timestamp: `20260922T130119Z`
- GitHub run: [#10635](https://github.com/28twagg-ops/TradingBot/actions/runs/35730630082)
- Run id: `35730630082`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`13s`
- Full logs: `logs/action_runs/20260922T130119Z_live_bot.log`, `logs/action_runs/20260922T130119Z_live_options.log`, `logs/action_runs/20260922T130119Z_options_bot.log`


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
{"ts_et":"2026-09-22T09:01:27.017985-04:00","date":"2026-09-22","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.3,"phases_s":{"reconcile":0.46},"signals":0,"placed":0,"equity":997383.89,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10635","github_run_id":"35730630082","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
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
|  Equity                                                         $226.67|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $226.67|
|  Cash                                                           $192.56|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $34.11|
|  Open P&L                                                        $+0.21|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (1 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  SCHW     Pullback50      $34.11     $106.15  $106.80  +0.6%   $+0.21  |
|                                                                        |
|  Total invested                                                  $34.11|
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
|  2026-09-21  SELL  ESAB  MomReversal  $33.77  P&L $-0.25               |
|  2026-09-21  SELL  SITM  EarningsDrift  $34.07  P&L $+0.08             |
|  2026-09-21  SELL  EQIX  Pullback50  $34.70  P&L $+0.82                |
|  2026-09-21  SELL  DRI  Pullback50  $33.71  P&L $-0.19                 |
|  2026-09-21  SELL  TJX  MomReversal  $34.28  P&L $+0.39                |
|  2026-09-21  SELL  PPG  MomReversal  $33.65  P&L $-0.23                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-22T09:01:23.639464-04:00 share=25% ===
2026-09-22 09:01:23,639 INFO === options_live_micro LIVE 2026-09-22T09:01:23.639464-04:00 share=25% ===
Live account equity $226.67 cash $192.56 #225458845 options_level=3
2026-09-22 09:01:23,847 INFO Live account equity $226.67 cash $192.56 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-22 09:01:23,905 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-22 09:01:23,962 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (166 earlier lines - see full log file)

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
## Ledger health — 2026-09-22
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1485 | WARN | <<<
| Missing exit records (post) |  1482 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-22_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-22_data_quality.csv
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

## Run 20260922T130605Z

- UTC timestamp: `20260922T130605Z`
- GitHub run: [#10636](https://github.com/28twagg-ops/TradingBot/actions/runs/35731165075)
- Run id: `35731165075`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`10s`
- Full logs: `logs/action_runs/20260922T130605Z_live_bot.log`, `logs/action_runs/20260922T130605Z_live_options.log`, `logs/action_runs/20260922T130605Z_options_bot.log`


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
{"ts_et":"2026-09-22T09:06:11.564800-04:00","date":"2026-09-22","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.1,"phases_s":{"reconcile":0.45},"signals":0,"placed":0,"equity":997357.89,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10636","github_run_id":"35731165075","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
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
|  Equity                                                         $226.65|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $226.65|
|  Cash                                                           $192.56|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $34.09|
|  Open P&L                                                        $+0.19|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (1 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  SCHW     Pullback50      $34.09     $106.15  $106.75  +0.6%   $+0.19  |
|                                                                        |
|  Total invested                                                  $34.09|
|  Total open P&L                                                  $+0.19|
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
|  2026-09-21  SELL  ESAB  MomReversal  $33.77  P&L $-0.25               |
|  2026-09-21  SELL  SITM  EarningsDrift  $34.07  P&L $+0.08             |
|  2026-09-21  SELL  EQIX  Pullback50  $34.70  P&L $+0.82                |
|  2026-09-21  SELL  DRI  Pullback50  $33.71  P&L $-0.19                 |
|  2026-09-21  SELL  TJX  MomReversal  $34.28  P&L $+0.39                |
|  2026-09-21  SELL  PPG  MomReversal  $33.65  P&L $-0.23                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-22T09:06:08.201853-04:00 share=25% ===
2026-09-22 09:06:08,201 INFO === options_live_micro LIVE 2026-09-22T09:06:08.201853-04:00 share=25% ===
Live account equity $226.65 cash $192.56 #225458845 options_level=3
2026-09-22 09:06:08,397 INFO Live account equity $226.65 cash $192.56 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-22 09:06:08,529 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-22 09:06:08,586 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (166 earlier lines - see full log file)

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
## Ledger health — 2026-09-22
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1485 | WARN | <<<
| Missing exit records (post) |  1482 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-22_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-22_data_quality.csv
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

## Run 20260922T131115Z

- UTC timestamp: `20260922T131115Z`
- GitHub run: [#10637](https://github.com/28twagg-ops/TradingBot/actions/runs/35731699816)
- Run id: `35731699816`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`14s`
- Full logs: `logs/action_runs/20260922T131115Z_live_bot.log`, `logs/action_runs/20260922T131115Z_live_options.log`, `logs/action_runs/20260922T131115Z_options_bot.log`


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
{"ts_et":"2026-09-22T09:11:21.544499-04:00","date":"2026-09-22","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.4,"phases_s":{"reconcile":0.55},"signals":0,"placed":0,"equity":997390.89,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10637","github_run_id":"35731699816","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:11:16  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.65|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $226.65|
|  Cash                                                           $192.56|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $34.09|
|  Open P&L                                                        $+0.19|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (1 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  SCHW     Pullback50      $34.09     $106.15  $106.75  +0.6%   $+0.19  |
|                                                                        |
|  Total invested                                                  $34.09|
|  Total open P&L                                                  $+0.19|
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
|  2026-09-21  SELL  ESAB  MomReversal  $33.77  P&L $-0.25               |
|  2026-09-21  SELL  SITM  EarningsDrift  $34.07  P&L $+0.08             |
|  2026-09-21  SELL  EQIX  Pullback50  $34.70  P&L $+0.82                |
|  2026-09-21  SELL  DRI  Pullback50  $33.71  P&L $-0.19                 |
|  2026-09-21  SELL  TJX  MomReversal  $34.28  P&L $+0.39                |
|  2026-09-21  SELL  PPG  MomReversal  $33.65  P&L $-0.23                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-22T09:11:18.031828-04:00 share=25% ===
2026-09-22 09:11:18,031 INFO === options_live_micro LIVE 2026-09-22T09:11:18.031828-04:00 share=25% ===
Live account equity $226.65 cash $192.56 #225458845 options_level=3
2026-09-22 09:11:18,265 INFO Live account equity $226.65 cash $192.56 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-22 09:11:18,335 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-22 09:11:18,405 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (166 earlier lines - see full log file)

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
## Ledger health — 2026-09-22
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1485 | WARN | <<<
| Missing exit records (post) |  1482 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-22_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-22_data_quality.csv
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

## Run 20260922T131614Z

- UTC timestamp: `20260922T131614Z`
- GitHub run: [#10638](https://github.com/28twagg-ops/TradingBot/actions/runs/35732240929)
- Run id: `35732240929`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`14s`
- Full logs: `logs/action_runs/20260922T131614Z_live_bot.log`, `logs/action_runs/20260922T131614Z_live_options.log`, `logs/action_runs/20260922T131614Z_options_bot.log`


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
{"ts_et":"2026-09-22T09:16:22.440445-04:00","date":"2026-09-22","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.5,"phases_s":{"reconcile":0.51},"signals":0,"placed":0,"equity":997429.89,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10638","github_run_id":"35732240929","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:16:16  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.65|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $226.65|
|  Cash                                                           $192.56|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $34.09|
|  Open P&L                                                        $+0.19|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (1 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  SCHW     Pullback50      $34.09     $106.15  $106.75  +0.6%   $+0.19  |
|                                                                        |
|  Total invested                                                  $34.09|
|  Total open P&L                                                  $+0.19|
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
|  2026-09-21  SELL  ESAB  MomReversal  $33.77  P&L $-0.25               |
|  2026-09-21  SELL  SITM  EarningsDrift  $34.07  P&L $+0.08             |
|  2026-09-21  SELL  EQIX  Pullback50  $34.70  P&L $+0.82                |
|  2026-09-21  SELL  DRI  Pullback50  $33.71  P&L $-0.19                 |
|  2026-09-21  SELL  TJX  MomReversal  $34.28  P&L $+0.39                |
|  2026-09-21  SELL  PPG  MomReversal  $33.65  P&L $-0.23                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-22T09:16:18.570533-04:00 share=25% ===
2026-09-22 09:16:18,570 INFO === options_live_micro LIVE 2026-09-22T09:16:18.570533-04:00 share=25% ===
Live account equity $226.65 cash $192.56 #225458845 options_level=3
2026-09-22 09:16:18,796 INFO Live account equity $226.65 cash $192.56 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-22 09:16:18,866 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-22 09:16:18,933 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (166 earlier lines - see full log file)

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
## Ledger health — 2026-09-22
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1485 | WARN | <<<
| Missing exit records (post) |  1482 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-22_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-22_data_quality.csv
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

## Run 20260922T132116Z

- UTC timestamp: `20260922T132116Z`
- GitHub run: [#10639](https://github.com/28twagg-ops/TradingBot/actions/runs/35732776584)
- Run id: `35732776584`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`14s`
- Full logs: `logs/action_runs/20260922T132116Z_live_bot.log`, `logs/action_runs/20260922T132116Z_live_options.log`, `logs/action_runs/20260922T132116Z_options_bot.log`


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
{"ts_et":"2026-09-22T09:21:22.684980-04:00","date":"2026-09-22","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.3,"phases_s":{"reconcile":0.45},"signals":0,"placed":0,"equity":997446.89,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10639","github_run_id":"35732776584","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:21:17  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.65|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $226.65|
|  Cash                                                           $192.56|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $34.09|
|  Open P&L                                                        $+0.19|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (1 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  SCHW     Pullback50      $34.09     $106.15  $106.75  +0.6%   $+0.19  |
|                                                                        |
|  Total invested                                                  $34.09|
|  Total open P&L                                                  $+0.19|
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
|  2026-09-21  SELL  ESAB  MomReversal  $33.77  P&L $-0.25               |
|  2026-09-21  SELL  SITM  EarningsDrift  $34.07  P&L $+0.08             |
|  2026-09-21  SELL  EQIX  Pullback50  $34.70  P&L $+0.82                |
|  2026-09-21  SELL  DRI  Pullback50  $33.71  P&L $-0.19                 |
|  2026-09-21  SELL  TJX  MomReversal  $34.28  P&L $+0.39                |
|  2026-09-21  SELL  PPG  MomReversal  $33.65  P&L $-0.23                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-22T09:21:19.252479-04:00 share=25% ===
2026-09-22 09:21:19,252 INFO === options_live_micro LIVE 2026-09-22T09:21:19.252479-04:00 share=25% ===
Live account equity $226.65 cash $192.56 #225458845 options_level=3
2026-09-22 09:21:19,463 INFO Live account equity $226.65 cash $192.56 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-22 09:21:19,523 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-22 09:21:19,581 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (166 earlier lines - see full log file)

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
## Ledger health — 2026-09-22
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1485 | WARN | <<<
| Missing exit records (post) |  1482 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-22_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-22_data_quality.csv
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

## Run 20260922T132609Z

- UTC timestamp: `20260922T132609Z`
- GitHub run: [#10640](https://github.com/28twagg-ops/TradingBot/actions/runs/35733314601)
- Run id: `35733314601`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`13s`
- Full logs: `logs/action_runs/20260922T132609Z_live_bot.log`, `logs/action_runs/20260922T132609Z_live_options.log`, `logs/action_runs/20260922T132609Z_options_bot.log`


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
{"ts_et":"2026-09-22T09:26:16.263253-04:00","date":"2026-09-22","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.24},"signals":0,"placed":0,"equity":997314.89,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10640","github_run_id":"35733314601","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:26:12  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.68|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $226.68|
|  Cash                                                           $192.56|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $34.12|
|  Open P&L                                                        $+0.22|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (1 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  SCHW     Pullback50      $34.12     $106.15  $106.83  +0.6%   $+0.22  |
|                                                                        |
|  Total invested                                                  $34.12|
|  Total open P&L                                                  $+0.22|
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
|  2026-09-21  SELL  ESAB  MomReversal  $33.77  P&L $-0.25               |
|  2026-09-21  SELL  SITM  EarningsDrift  $34.07  P&L $+0.08             |
|  2026-09-21  SELL  EQIX  Pullback50  $34.70  P&L $+0.82                |
|  2026-09-21  SELL  DRI  Pullback50  $33.71  P&L $-0.19                 |
|  2026-09-21  SELL  TJX  MomReversal  $34.28  P&L $+0.39                |
|  2026-09-21  SELL  PPG  MomReversal  $33.65  P&L $-0.23                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-22T09:26:13.173550-04:00 share=25% ===
2026-09-22 09:26:13,173 INFO === options_live_micro LIVE 2026-09-22T09:26:13.173550-04:00 share=25% ===
Live account equity $226.68 cash $192.56 #225458845 options_level=3
2026-09-22 09:26:13,257 INFO Live account equity $226.68 cash $192.56 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-22 09:26:13,289 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-22 09:26:13,310 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (166 earlier lines - see full log file)

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
## Ledger health — 2026-09-22
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1485 | WARN | <<<
| Missing exit records (post) |  1482 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    50 | INFO |
| Total closed lots           |  2385 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-22_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-22_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1367 med=-12.5% | TAINTED n=1882 med=-38.9% | KEEP-only n=751 med=+51.4% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.68 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260922T133123Z

- UTC timestamp: `20260922T133123Z`
- GitHub run: [#10641](https://github.com/28twagg-ops/TradingBot/actions/runs/35733859191)
- Run id: `35733859191`
- Live bot: exit=`0`, duration=`216s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260922T133123Z_live_bot.log`, `logs/action_runs/20260922T133123Z_live_options.log`, `logs/action_runs/20260922T133123Z_options_bot.log`


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
{"ts_et":"2026-09-22T09:26:16.263253-04:00","date":"2026-09-22","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.24},"signals":0,"placed":0,"equity":997314.89,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10640","github_run_id":"35733314601","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:31:23  INFO      Mode: morning_prep
13:31:24  INFO        [prep_positions] 1/1 (1 valid)
13:31:24  INFO      Fetching tickers (universe=both)...
13:31:24  INFO        S&P 500: 503
13:31:24  INFO        MidCap 400: 400
13:31:24  INFO        Total: 901 tickers
13:31:25  INFO        [prep_universe] 40/900 (40 valid)
13:31:27  INFO        [prep_universe] 80/900 (80 valid)
13:31:28  INFO        [prep_universe] 120/900 (120 valid)
13:31:29  INFO        [prep_universe] 160/900 (160 valid)
13:31:31  INFO        [prep_universe] 200/900 (199 valid)
13:31:38  INFO        [prep_universe] 240/900 (238 valid)
13:31:51  INFO        [prep_universe] 280/900 (278 valid)
13:32:01  INFO        [prep_universe] 320/900 (318 valid)
13:32:14  INFO        [prep_universe] 360/900 (358 valid)
13:32:27  INFO        [prep_universe] 400/900 (398 valid)
13:32:37  INFO        [prep_universe] 440/900 (438 valid)
13:32:50  INFO        [prep_universe] 480/900 (478 valid)
13:33:02  INFO        [prep_universe] 520/900 (518 valid)
13:33:12  INFO        [prep_universe] 560/900 (558 valid)
13:33:25  INFO        [prep_universe] 600/900 (598 valid)
13:33:38  INFO        [prep_universe] 640/900 (638 valid)
13:33:51  INFO        [prep_universe] 680/900 (678 valid)
13:34:01  INFO        [prep_universe] 720/900 (718 valid)
13:34:14  INFO        [prep_universe] 760/900 (758 valid)
13:34:27  INFO        [prep_universe] 800/900 (798 valid)
13:34:37  INFO        [prep_universe] 840/900 (838 valid)
13:34:50  INFO        [prep_universe] 880/900 (878 valid)
13:34:56  INFO        [prep_universe] 900/900 (898 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.10|
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
|  Invested                                                        $33.54|
|  Open P&L                                                        $-0.36|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  SCHW     Pullback50      $33.54     $106.15  $105.01  -1.1%   $-0.36  |
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
|  Universe scanned                                                   900|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-22T09:34:59.954519-04:00 share=25% ===
2026-09-22 09:34:59,954 INFO === options_live_micro LIVE 2026-09-22T09:34:59.954519-04:00 share=25% ===
Live account equity $226.03 cash $192.56 #225458845 options_level=3
2026-09-22 09:35:00,026 INFO Live account equity $226.03 cash $192.56 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-22 09:35:00,073 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-22 09:35:00,124 INFO Live micro done. open_options=0 lots=0
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
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$996,647.39
  buying_power=$3,934,994.56 cash=$1,031,280.89
  open option orders: 4
    NFLX261009C00078000 OrderSide.SELL qty=2 status=OrderStatus.NEW limit=None
    NFLX261002C00077000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
    BAC260925C00058000 OrderSide.SELL qty=7 status=OrderStatus.NEW limit=None
    MARA260925C00011000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
  open option positions: 15
    AXP260925C00325000 qty=2 mkt=$76.00
    BAC260925C00058000 qty=7 mkt=$413.00
    BAC260925C00059000 qty=2 mkt=$42.00
    CELH260925C00029000 qty=2 mkt=$104.00
    CELH260925C00029500 qty=2 mkt=$8.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-22T09:35:02.856751-04:00 ===

[Run context]
Paper auth OK — equity $996651.28, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
2026-09-22 09:35:03,799 INFO   EXIT [b239|lab0239_s401_w3_1045_1120_r2|S401] stop_loss (-84.1%) SELL 1 MDT260925C00094000 @<= 0.08
  EXIT [b434|lab0434_s366_w2_1005_1045_r1|S366] take_profit (+79.2%) SELL failed MARA260925C00012500: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b433|lab0433_s366_w1_0928_1005_r2|S366] take_profit (+79.2%) SELL failed MARA260925C00012500: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b432|lab0432_s366_w1_0928_1005_r1|S366] take_profit (+79.2%) SELL failed MARA260925C00012500: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
2026-09-22 09:35:09,516 INFO   EXIT [b166|lab0166_s216_w2_1005_1045_r1|S216] stop_loss (-88.6%) SELL 1 CELH260925C00029500 @<= 0.05
Protective stops: placed=7 upgraded=0 already=4 failed=2 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
```

---

## Run 20260922T133700Z

- UTC timestamp: `20260922T133700Z`
- GitHub run: [#10642](https://github.com/28twagg-ops/TradingBot/actions/runs/35734417701)
- Run id: `35734417701`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260922T133700Z_live_bot.log`, `logs/action_runs/20260922T133700Z_live_options.log`, `logs/action_runs/20260922T133700Z_options_bot.log`


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
{"ts_et":"2026-09-22T09:26:16.263253-04:00","date":"2026-09-22","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.24},"signals":0,"placed":0,"equity":997314.89,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10640","github_run_id":"35733314601","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:37:01  INFO      Mode: morning_prep
13:37:02  INFO        [prep_positions] 1/1 (1 valid)
13:37:02  INFO      Fetching tickers (universe=both)...
13:37:03  INFO        S&P 500: 503
13:37:03  INFO        MidCap 400: 400
13:37:03  INFO        Total: 901 tickers
13:37:04  INFO        [prep_universe] 40/900 (40 valid)
13:37:06  INFO        [prep_universe] 80/900 (80 valid)
13:37:07  INFO        [prep_universe] 120/900 (120 valid)
13:37:08  INFO        [prep_universe] 160/900 (160 valid)
13:37:10  INFO        [prep_universe] 200/900 (199 valid)
13:37:17  INFO        [prep_universe] 240/900 (238 valid)
13:37:28  INFO        [prep_universe] 280/900 (278 valid)
13:37:41  INFO        [prep_universe] 320/900 (318 valid)
13:37:51  INFO        [prep_universe] 360/900 (358 valid)
13:38:05  INFO        [prep_universe] 400/900 (398 valid)
13:38:18  INFO        [prep_universe] 440/900 (438 valid)
13:38:28  INFO        [prep_universe] 480/900 (478 valid)
13:38:42  INFO        [prep_universe] 520/900 (518 valid)
13:38:52  INFO        [prep_universe] 560/900 (558 valid)
13:39:06  INFO        [prep_universe] 600/900 (598 valid)
13:39:16  INFO        [prep_universe] 640/900 (638 valid)
13:39:29  INFO        [prep_universe] 680/900 (678 valid)
13:39:40  INFO        [prep_universe] 720/900 (718 valid)
13:39:53  INFO        [prep_universe] 760/900 (758 valid)
13:40:04  INFO        [prep_universe] 800/900 (798 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20260922T134157Z

- UTC timestamp: `20260922T134157Z`
- GitHub run: [#10643](https://github.com/28twagg-ops/TradingBot/actions/runs/35734974501)
- Run id: `35734974501`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260922T134157Z_live_bot.log`, `logs/action_runs/20260922T134157Z_live_options.log`, `logs/action_runs/20260922T134157Z_options_bot.log`


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
{"ts_et":"2026-09-22T09:26:16.263253-04:00","date":"2026-09-22","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.24},"signals":0,"placed":0,"equity":997314.89,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10640","github_run_id":"35733314601","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:41:58  INFO      Mode: morning_prep
13:41:58  INFO        [prep_positions] 1/1 (1 valid)
13:41:58  INFO        Universe cache hit: 901 tickers (tickers_2026-09-22.json)
13:41:59  INFO        [prep_universe] 40/900 (40 valid)
13:42:01  INFO        [prep_universe] 80/900 (80 valid)
13:42:02  INFO        [prep_universe] 120/900 (120 valid)
13:42:03  INFO        [prep_universe] 160/900 (160 valid)
13:42:05  INFO        [prep_universe] 200/900 (199 valid)
13:42:12  INFO        [prep_universe] 240/900 (238 valid)
13:42:25  INFO        [prep_universe] 280/900 (278 valid)
13:42:37  INFO        [prep_universe] 320/900 (318 valid)
13:42:47  INFO        [prep_universe] 360/900 (358 valid)
13:43:00  INFO        [prep_universe] 400/900 (398 valid)
13:43:13  INFO        [prep_universe] 440/900 (438 valid)
13:43:23  INFO        [prep_universe] 480/900 (478 valid)
13:43:36  INFO        [prep_universe] 520/900 (518 valid)
13:43:49  INFO        [prep_universe] 560/900 (558 valid)
13:43:59  INFO        [prep_universe] 600/900 (598 valid)
13:44:12  INFO        [prep_universe] 640/900 (638 valid)
13:44:25  INFO        [prep_universe] 680/900 (678 valid)
13:44:35  INFO        [prep_universe] 720/900 (718 valid)
13:44:48  INFO        [prep_universe] 760/900 (758 valid)
13:45:01  INFO        [prep_universe] 800/900 (798 valid)
13:45:11  INFO        [prep_universe] 840/900 (838 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20260922T134654Z

- UTC timestamp: `20260922T134654Z`
- GitHub run: [#10644](https://github.com/28twagg-ops/TradingBot/actions/runs/35735550466)
- Run id: `35735550466`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260922T134654Z_live_bot.log`, `logs/action_runs/20260922T134654Z_live_options.log`, `logs/action_runs/20260922T134654Z_options_bot.log`


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
{"ts_et":"2026-09-22T09:26:16.263253-04:00","date":"2026-09-22","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.24},"signals":0,"placed":0,"equity":997314.89,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10640","github_run_id":"35733314601","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:46:55  INFO      Mode: morning_scan
13:46:58  INFO        [positions] 1/1 (1 valid)
13:46:58  INFO        SELL MARKET [urgent] SCHW closed
13:47:00  INFO        TX logged: SELL SCHW  P&L -2.06%
13:47:00  INFO        Universe cache hit: 901 tickers (tickers_2026-09-22.json)
13:47:02  INFO        [universe] 40/901 (40 valid)
13:47:07  INFO        [universe] 80/901 (80 valid)
13:47:09  INFO        [universe] 120/901 (120 valid)
13:47:10  INFO        [universe] 160/901 (160 valid)
13:47:13  INFO        [universe] 200/901 (199 valid)
13:47:15  INFO        [universe] 240/901 (238 valid)
13:47:26  INFO        [universe] 280/901 (278 valid)
13:47:37  INFO        [universe] 320/901 (318 valid)
13:47:51  INFO        [universe] 360/901 (358 valid)
13:48:01  INFO        [universe] 400/901 (398 valid)
13:48:15  INFO        [universe] 440/901 (438 valid)
13:48:26  INFO        [universe] 480/901 (478 valid)
13:48:37  INFO        [universe] 520/901 (518 valid)
13:48:51  INFO        [universe] 560/901 (558 valid)
13:49:02  INFO        [universe] 600/901 (598 valid)
13:49:16  INFO        [universe] 640/901 (638 valid)
13:49:27  INFO        [universe] 680/901 (678 valid)
13:49:37  INFO        [universe] 720/901 (718 valid)
13:49:51  INFO        [universe] 760/901 (758 valid)
13:50:02  INFO        [universe] 800/901 (798 valid)
13:50:16  INFO        [universe] 840/901 (838 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20260922T135150Z

- UTC timestamp: `20260922T135150Z`
- GitHub run: [#10645](https://github.com/28twagg-ops/TradingBot/actions/runs/35736116988)
- Run id: `35736116988`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260922T135150Z_live_bot.log`, `logs/action_runs/20260922T135150Z_live_options.log`, `logs/action_runs/20260922T135150Z_options_bot.log`


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
{"ts_et":"2026-09-22T09:26:16.263253-04:00","date":"2026-09-22","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.24},"signals":0,"placed":0,"equity":997314.89,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10640","github_run_id":"35733314601","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
... (121 earlier lines - see full log file)
|  LIVN     Pullback50      eq     $79.35   47.3   -2.35   50MA bounce (-|
|  MSM      Pullback50      eq     $121.52  63.4   -1.79   50MA bounce (-|
|  MTSI     Pullback50      eq     $276.79  55.9   -2.12   50MA bounce (+|
|  SN       Pullback50      eq     $170.16  44.4   -1.59   50MA bounce (-|
|  WTRG     Pullback50      eq     $40.51   43.1   -2.89   50MA bounce (+|
|                                                                        |
+========================================================================+

+========================================================================+
|                              ENTRY ORDERS                              |
+========================================================================+
|    ENTER [eq] AES  Pullback50                                    $33.86|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    ENTER [eq] AMZN  Pullback50                                   $33.86|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    ENTER [eq] AME  Pullback50                                    $33.86|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    SKIP [eq] BRK-B  Pullback50                                    cap 3|
|    SKIP [eq] KO  Pullback50                                       cap 3|
|    SKIP [eq] DLR  Pullback50                                      cap 3|
|    SKIP [eq] EW  Pullback50                                       cap 3|
|    SKIP [eq] EQIX  Pullback50                                     cap 3|
|    SKIP [eq] XOM  Pullback50                                      cap 3|
|    SKIP [eq] JCI  Pullback50                                      cap 3|
|    SKIP [eq] KDP  Pullback50                                      cap 3|13:55:55  INFO        place_all_stops: checking 3 positions...
13:55:55  INFO        STOP-MARKET placed AES  qty=2 (pos=2.2782)  stop=$14.78  id=f773abbb-714b-453c-aa3b-9010190308a0
13:55:55  INFO        STOP skipped AME: fractional (0.1397 shares) — software exit will handle it
13:55:55  INFO        STOP skipped AMZN: fractional (0.1315 shares) — software exit will handle it
13:55:55  INFO        Daily log -> logs/daily/2026-09-22.md
13:55:55  INFO        Dashboard written → logs/dashboard.md

|    SKIP [eq] LH  Pullback50                                       cap 3|
|    SKIP [eq] LRCX  Pullback50                                     cap 3|
|    SKIP [eq] DGX  Pullback50                                      cap 3|
|    SKIP [eq] PWR  Pullback50                                      cap 3|
|    SKIP [eq] SJM  Pullback50                                      cap 3|
|    SKIP [eq] UAL  Pullback50                                      cap 3|
|    SKIP [eq] WSM  Pullback50                                      cap 3|
|    SKIP [eq] ASH  Pullback50                                      cap 3|
|    SKIP [eq] CLH  Pullback50                                      cap 3|
|    SKIP [eq] GHC  Pullback50                                      cap 3|
|    SKIP [eq] KRYS  Pullback50                                     cap 3|
|    SKIP [eq] LIVN  Pullback50                                     cap 3|
|    SKIP [eq] MSM  Pullback50                                      cap 3|
|    SKIP [eq] MTSI  Pullback50                                     cap 3|
|    SKIP [eq] SN  Pullback50                                       cap 3|
|    SKIP [eq] WTRG  Pullback50                                     cap 3|

+========================================================================+
|                         BUY FILL CONFIRMATION                          |
+========================================================================+
|  Pending submits                                                      3|
+------------------------------------------------------------------------+
|  AES                                                  still unconfirmed|
|  AMZN                                                 still unconfirmed|
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
|  Strategy  GapDown + VolumeSpike (display only — schedule not enforced)|
|  Scanned                                                            899|
|  Signals                                                             27|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  3 unconfirmed|
|  Exits                                                                0|
|  Open pos                                                             3|
|  Equity                                                         $225.74|
|  Cash                                                           $124.17|
+========================================================================+
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20260922T135721Z

- UTC timestamp: `20260922T135721Z`
- GitHub run: [#10646](https://github.com/28twagg-ops/TradingBot/actions/runs/35736684182)
- Run id: `35736684182`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260922T135721Z_live_bot.log`, `logs/action_runs/20260922T135721Z_live_options.log`, `logs/action_runs/20260922T135721Z_options_bot.log`


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
{"ts_et":"2026-09-22T09:26:16.263253-04:00","date":"2026-09-22","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.24},"signals":0,"placed":0,"equity":997314.89,"open_positions":15,"pending_orders":0,"open_lots":50,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10640","github_run_id":"35733314601","status":"ok","data_quality":{"clean":{"n":1367,"win":49.23,"med":-12.5,"avg":44.2,"pnl":17587.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":751,"win":61.92,"med":51.39,"avg":69.85,"pnl":12368.45},"keep_only_recent":{"n":557,"win":60.14,"med":53.57,"avg":80.97,"pnl":8146.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:57:24  INFO      Mode: morning_scan
13:57:25  INFO        [positions] 3/3 (3 valid)
13:57:25  INFO        SELL order cancelled AES  type=OrderType.STOP  id=f773abbb-714b-453c-aa3b-9010190308a0
13:57:25  INFO        SELL LIMIT AES  qty=2.278236988  limit=$14.85  id=608f056c-7273-47bc-a4a7-31becd41169b
13:57:56  INFO        SELL LIMIT filled AES (confirmed by position check)
13:57:56  INFO        TX logged: SELL AES  P&L -0.04%
13:57:56  INFO        SELL LIMIT AMZN  qty=0.131485926  limit=$257.01  id=b6d03677-9b9d-4bd9-b6ee-9b4ec91def74
13:58:26  INFO        SELL LIMIT filled AMZN (confirmed by position check)
13:58:27  INFO        TX logged: SELL AMZN  P&L -0.03%
13:58:27  INFO        SELL LIMIT AME  qty=0.139732835  limit=$242.23  id=87b37de5-7df4-4f15-9212-0e5d3a0eb582
13:58:57  INFO        SELL LIMIT filled AME (confirmed by position check)
13:58:57  INFO        TX logged: SELL AME  P&L 0.18%
13:58:57  INFO        Universe cache hit: 901 tickers (tickers_2026-09-22.json)
13:58:58  INFO        [universe] 40/901 (40 valid)
13:59:00  INFO        [universe] 80/901 (80 valid)
13:59:01  INFO        [universe] 120/901 (120 valid)
13:59:02  INFO        [universe] 160/901 (160 valid)
13:59:03  INFO        [universe] 200/901 (199 valid)
13:59:11  INFO        [universe] 240/901 (238 valid)
13:59:24  INFO        [universe] 280/901 (278 valid)
13:59:34  INFO        [universe] 320/901 (318 valid)
13:59:47  INFO        [universe] 360/901 (358 valid)
13:59:58  INFO        [universe] 400/901 (398 valid)
14:00:11  INFO        [universe] 440/901 (438 valid)
14:00:25  INFO        [universe] 480/901 (478 valid)
14:00:35  INFO        [universe] 520/901 (518 valid)
14:00:49  INFO        [universe] 560/901 (558 valid)
14:00:59  INFO        [universe] 600/901 (598 valid)
14:01:12  INFO        [universe] 640/901 (638 valid)
14:01:23  INFO        [universe] 680/901 (678 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20260922T140312Z

- UTC timestamp: `20260922T140312Z`
- GitHub run: [#10647](https://github.com/28twagg-ops/TradingBot/actions/runs/35737248569)
- Run id: `35737248569`
- Live bot: exit=`0`, duration=`5s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`70s`
- Full logs: `logs/action_runs/20260922T140312Z_live_bot.log`, `logs/action_runs/20260922T140312Z_live_options.log`, `logs/action_runs/20260922T140312Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1371 | 49.1 | -15.9 | +43.9 | $+17,446 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 753 | 61.8 | +51.0 | +69.4 | $+12,250 |
| KEEP-only recent | 559 | 59.9 | +53.3 | +80.4 | $+8,028 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-22T10:03:24.693484-04:00","date":"2026-09-22","mode":"entry+manage","header":"entry+manage (4 new)","elapsed_s":57.1,"phases_s":{"reconcile":0.44,"cancel":0.12,"manage":4.4,"protective_stops":1.48,"scan":39.23,"entries":8.76,"reconcile2":0.57},"signals":56,"placed":4,"equity":996478.85,"open_positions":13,"pending_orders":0,"open_lots":30,"submitted_today":4,"filled_today":4,"unattributed_contracts":0,"top_signals":["S211:AMD","S401:AMD","S210:COIN","S401:COIN","S401:META","S401:AMZN","S401:MARA","S401:MSTR"],"github_run":"10647","github_run_id":"35737248569","status":"ok","data_quality":{"clean":{"n":1371,"win":49.09,"med":-15.87,"avg":43.91,"pnl":17446.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":753,"win":61.75,"med":50.98,"avg":69.44,"pnl":12250.45},"keep_only_recent":{"n":559,"win":59.93,"med":53.33,"avg":80.38,"pnl":8028.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:03:15  INFO      Mode: exits
14:03:16  INFO        Daily log -> logs/daily/2026-09-22.md
14:03:16  INFO        Daily log reconciled -> logs/daily/2026-09-22.md (1 ledger rows)
14:03:17  INFO        Daily log -> logs/daily/2026-09-22.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:03 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.79|
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
=== options_live_micro LIVE 2026-09-22T10:03:18.435348-04:00 share=25% ===
2026-09-22 10:03:18,435 INFO === options_live_micro LIVE 2026-09-22T10:03:18.435348-04:00 share=25% ===
Live account equity $225.79 cash $225.79 #225458845 options_level=3
2026-09-22 10:03:18,651 INFO Live account equity $225.79 cash $225.79 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-22 10:03:18,936 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-22 10:03:19,051 INFO Live micro done. open_options=0 lots=0
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
## Ledger health — 2026-09-22
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1485 | WARN | <<<
| Missing exit records (post) |  1482 | WARN | <<<
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |    30 | INFO |
| Total closed lots           |  2388 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-22_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-22_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1371 med=-15.9% | TAINTED n=1882 med=-38.9% | KEEP-only n=753 med=+51.0% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=225.79 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260922T140610Z

- UTC timestamp: `20260922T140610Z`
- GitHub run: [#10648](https://github.com/28twagg-ops/TradingBot/actions/runs/35737826355)
- Run id: `35737826355`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`72s`
- Full logs: `logs/action_runs/20260922T140610Z_live_bot.log`, `logs/action_runs/20260922T140610Z_live_options.log`, `logs/action_runs/20260922T140610Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1373 | 49.1 | -15.9 | +43.8 | $+17,423 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 754 | 61.7 | +51.0 | +69.2 | $+12,194 |
| KEEP-only recent | 560 | 59.8 | +53.3 | +80.1 | $+7,972 |

- KEEP strategies (25): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-22T10:06:15.009249-04:00","date":"2026-09-22","mode":"entry+manage","header":"entry+manage (4 new)","elapsed_s":60.4,"phases_s":{"reconcile":0.14,"cancel":0.03,"manage":3.17,"protective_stops":0.27,"scan":52.41,"entries":3.09,"reconcile2":0.36},"signals":56,"placed":4,"equity":996596.19,"open_positions":14,"pending_orders":0,"open_lots":32,"submitted_today":8,"filled_today":8,"unattributed_contracts":0,"top_signals":["S211:AMD","S401:AMD","S210:COIN","S401:COIN","S401:META","S401:AMZN","S401:MARA","S401:MSTR"],"github_run":"10648","github_run_id":"35737826355","status":"ok","data_quality":{"clean":{"n":1373,"win":49.09,"med":-15.87,"avg":43.83,"pnl":17423.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":754,"win":61.67,"med":50.96,"avg":69.24,"pnl":12194.45},"keep_only_recent":{"n":560,"win":59.82,"med":53.33,"avg":80.09,"pnl":7972.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:06:11  INFO      Mode: exits
14:06:11  INFO        Daily log -> logs/daily/2026-09-22.md
14:06:11  INFO        Daily log reconciled -> logs/daily/2026-09-22.md (4 ledger rows)
14:06:11  INFO        Daily log -> logs/daily/2026-09-22.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.79|
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
=== options_live_micro LIVE 2026-09-22T10:06:12.330213-04:00 share=25% ===
2026-09-22 10:06:12,330 INFO === options_live_micro LIVE 2026-09-22T10:06:12.330213-04:00 share=25% ===
Live account equity $225.79 cash $225.79 #225458845 options_level=3
2026-09-22 10:06:12,388 INFO Live account equity $225.79 cash $225.79 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-22 10:06:12,423 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-22 10:06:12,446 INFO Live micro done. open_options=0 lots=0
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
## Ledger health — 2026-09-22
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1485 | WARN | <<<
| Missing exit records (post) |  1482 | WARN | <<<
| State/ledger mismatches     |     2 | WARN | <<<
| Total open lots             |    32 | INFO |
| Total closed lots           |  2390 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-22_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-22_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1373 med=-15.9% | TAINTED n=1882 med=-38.9% | KEEP-only n=754 med=+51.0% | KILL=18 KEEP=25
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=225.79 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260922T141110Z

- UTC timestamp: `20260922T141110Z`
- GitHub run: [#10649](https://github.com/28twagg-ops/TradingBot/actions/runs/35738408715)
- Run id: `35738408715`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`52s`
- Full logs: `logs/action_runs/20260922T141110Z_live_bot.log`, `logs/action_runs/20260922T141110Z_live_options.log`, `logs/action_runs/20260922T141110Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1377 | 49.1 | -15.9 | +43.7 | $+17,330 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 713 | 62.3 | +51.6 | +70.6 | $+11,733 |
| KEEP-only recent | 520 | 60.4 | +54.0 | +82.6 | $+7,488 |

- KEEP strategies (24): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-22T10:11:15.000016-04:00","date":"2026-09-22","mode":"entry+manage","header":"entry+manage (2 new)","elapsed_s":42.7,"phases_s":{"reconcile":0.25,"cancel":0.02,"manage":4.1,"protective_stops":0.19,"scan":35.07,"entries":1.95,"reconcile2":0.32},"signals":56,"placed":2,"equity":996420.53,"open_positions":12,"pending_orders":0,"open_lots":30,"submitted_today":10,"filled_today":10,"unattributed_contracts":0,"top_signals":["S211:AMD","S401:AMD","S210:COIN","S401:COIN","S401:META","S401:AMZN","S401:MARA","S401:MSTR"],"github_run":"10649","github_run_id":"35738408715","status":"ok","data_quality":{"clean":{"n":1377,"win":49.09,"med":-15.87,"avg":43.7,"pnl":17330.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":713,"win":62.27,"med":51.61,"avg":70.63,"pnl":11733.45},"keep_only_recent":{"n":520,"win":60.38,"med":54.05,"avg":82.62,"pnl":7488.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:11:11  INFO      Mode: exits
14:11:11  INFO        Daily log -> logs/daily/2026-09-22.md
14:11:11  INFO        Daily log reconciled -> logs/daily/2026-09-22.md (4 ledger rows)
14:11:11  INFO        Daily log -> logs/daily/2026-09-22.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.79|
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
=== options_live_micro LIVE 2026-09-22T10:11:12.388803-04:00 share=25% ===
2026-09-22 10:11:12,388 INFO === options_live_micro LIVE 2026-09-22T10:11:12.388803-04:00 share=25% ===
Live account equity $225.79 cash $225.79 #225458845 options_level=3
2026-09-22 10:11:12,431 INFO Live account equity $225.79 cash $225.79 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-22 10:11:12,464 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-22 10:11:12,477 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (193 earlier lines - see full log file)

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
## Ledger health — 2026-09-22
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1485 | WARN | <<<
| Missing exit records (post) |  1482 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |    30 | INFO |
| Total closed lots           |  2392 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-22_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-22_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1377 med=-15.9% | TAINTED n=1882 med=-38.9% | KEEP-only n=713 med=+51.6% | KILL=18 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=225.79 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260922T141619Z

- UTC timestamp: `20260922T141619Z`
- GitHub run: [#10650](https://github.com/28twagg-ops/TradingBot/actions/runs/35738992771)
- Run id: `35738992771`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`79s`
- Full logs: `logs/action_runs/20260922T141619Z_live_bot.log`, `logs/action_runs/20260922T141619Z_live_options.log`, `logs/action_runs/20260922T141619Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1377 | 49.1 | -15.9 | +43.7 | $+17,330 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 713 | 62.3 | +51.6 | +70.6 | $+11,733 |
| KEEP-only recent | 520 | 60.4 | +54.0 | +82.6 | $+7,488 |

- KEEP strategies (24): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-22T10:16:25.827872-04:00","date":"2026-09-22","mode":"entry+manage","header":"entry+manage (7 new)","elapsed_s":66.6,"phases_s":{"reconcile":0.24,"cancel":0.07,"manage":4.59,"protective_stops":0.42,"scan":53.32,"entries":6.36,"reconcile2":0.51},"signals":56,"placed":7,"equity":996257.74,"open_positions":12,"pending_orders":0,"open_lots":33,"submitted_today":17,"filled_today":17,"unattributed_contracts":0,"top_signals":["S211:AMD","S401:AMD","S210:COIN","S401:COIN","S401:META","S401:AMZN","S401:MARA","S401:MSTR"],"github_run":"10650","github_run_id":"35738992771","status":"ok","data_quality":{"clean":{"n":1377,"win":49.09,"med":-15.87,"avg":43.7,"pnl":17330.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":713,"win":62.27,"med":51.61,"avg":70.63,"pnl":11733.45},"keep_only_recent":{"n":520,"win":60.38,"med":54.05,"avg":82.62,"pnl":7488.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:16:20  INFO      Mode: exits
14:16:21  INFO        Daily log -> logs/daily/2026-09-22.md
14:16:21  INFO        Daily log reconciled -> logs/daily/2026-09-22.md (4 ledger rows)
14:16:21  INFO        Daily log -> logs/daily/2026-09-22.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.79|
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
=== options_live_micro LIVE 2026-09-22T10:16:22.509827-04:00 share=25% ===
2026-09-22 10:16:22,509 INFO === options_live_micro LIVE 2026-09-22T10:16:22.509827-04:00 share=25% ===
Live account equity $225.79 cash $225.79 #225458845 options_level=3
2026-09-22 10:16:22,648 INFO Live account equity $225.79 cash $225.79 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-22 10:16:22,761 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-22 10:16:22,835 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (194 earlier lines - see full log file)

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
## Ledger health — 2026-09-22
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1485 | WARN | <<<
| Missing exit records (post) |  1482 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |    33 | INFO |
| Total closed lots           |  2392 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-22_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-22_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1377 med=-15.9% | TAINTED n=1882 med=-38.9% | KEEP-only n=713 med=+51.6% | KILL=18 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=225.79 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260922T142111Z

- UTC timestamp: `20260922T142111Z`
- GitHub run: [#10651](https://github.com/28twagg-ops/TradingBot/actions/runs/35739578729)
- Run id: `35739578729`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`64s`
- Full logs: `logs/action_runs/20260922T142111Z_live_bot.log`, `logs/action_runs/20260922T142111Z_live_options.log`, `logs/action_runs/20260922T142111Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1377 | 49.1 | -15.9 | +43.7 | $+17,330 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 713 | 62.3 | +51.6 | +70.6 | $+11,733 |
| KEEP-only recent | 520 | 60.4 | +54.0 | +82.6 | $+7,488 |

- KEEP strategies (24): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-22T10:21:18.920282-04:00","date":"2026-09-22","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":54.1,"phases_s":{"reconcile":0.39,"cancel":0.13,"manage":6.61,"protective_stops":0.78,"scan":35.23,"entries":10.39},"signals":56,"placed":0,"equity":996108.53,"open_positions":12,"pending_orders":0,"open_lots":33,"submitted_today":17,"filled_today":17,"unattributed_contracts":0,"top_signals":["S211:AMD","S401:AMD","S210:COIN","S401:COIN","S401:META","S401:AMZN","S401:MARA","S401:MSTR"],"github_run":"10651","github_run_id":"35739578729","status":"ok","data_quality":{"clean":{"n":1377,"win":49.09,"med":-15.87,"avg":43.7,"pnl":17330.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":713,"win":62.27,"med":51.61,"avg":70.63,"pnl":11733.45},"keep_only_recent":{"n":520,"win":60.38,"med":54.05,"avg":82.62,"pnl":7488.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:21:12  INFO      Mode: exits
14:21:13  INFO        Daily log -> logs/daily/2026-09-22.md
14:21:13  INFO        Daily log reconciled -> logs/daily/2026-09-22.md (4 ledger rows)
14:21:14  INFO        Daily log -> logs/daily/2026-09-22.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.79|
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
=== options_live_micro LIVE 2026-09-22T10:21:15.188995-04:00 share=25% ===
2026-09-22 10:21:15,189 INFO === options_live_micro LIVE 2026-09-22T10:21:15.188995-04:00 share=25% ===
Live account equity $225.79 cash $225.79 #225458845 options_level=3
2026-09-22 10:21:15,386 INFO Live account equity $225.79 cash $225.79 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-22 10:21:15,639 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-22 10:21:15,752 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (187 earlier lines - see full log file)

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
## Ledger health — 2026-09-22
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1485 | WARN | <<<
| Missing exit records (post) |  1482 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |    33 | INFO |
| Total closed lots           |  2392 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-22_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-22_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1377 med=-15.9% | TAINTED n=1882 med=-38.9% | KEEP-only n=713 med=+51.6% | KILL=18 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=225.79 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260922T142610Z

- UTC timestamp: `20260922T142610Z`
- GitHub run: [#10652](https://github.com/28twagg-ops/TradingBot/actions/runs/35740160815)
- Run id: `35740160815`
- Live bot: exit=`0`, duration=`5s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`63s`
- Full logs: `logs/action_runs/20260922T142610Z_live_bot.log`, `logs/action_runs/20260922T142610Z_live_options.log`, `logs/action_runs/20260922T142610Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1377 | 49.1 | -15.9 | +43.7 | $+17,330 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 713 | 62.3 | +51.6 | +70.6 | $+11,733 |
| KEEP-only recent | 520 | 60.4 | +54.0 | +82.6 | $+7,488 |

- KEEP strategies (24): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-22T10:26:20.113277-04:00","date":"2026-09-22","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":53.5,"phases_s":{"reconcile":0.39,"cancel":0.12,"manage":6.02,"protective_stops":1.06,"scan":34.78,"entries":10.52},"signals":56,"placed":0,"equity":996042.03,"open_positions":12,"pending_orders":0,"open_lots":33,"submitted_today":17,"filled_today":17,"unattributed_contracts":0,"top_signals":["S211:AMD","S401:AMD","S210:COIN","S401:COIN","S401:META","S401:AMZN","S401:MARA","S401:MSTR"],"github_run":"10652","github_run_id":"35740160815","status":"ok","data_quality":{"clean":{"n":1377,"win":49.09,"med":-15.87,"avg":43.7,"pnl":17330.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":713,"win":62.27,"med":51.61,"avg":70.63,"pnl":11733.45},"keep_only_recent":{"n":520,"win":60.38,"med":54.05,"avg":82.62,"pnl":7488.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:26:12  INFO      Mode: exits
14:26:15  INFO        Daily log -> logs/daily/2026-09-22.md
14:26:15  INFO        Daily log reconciled -> logs/daily/2026-09-22.md (4 ledger rows)
14:26:16  INFO        Daily log -> logs/daily/2026-09-22.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.79|
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
=== options_live_micro LIVE 2026-09-22T10:26:16.957206-04:00 share=25% ===
2026-09-22 10:26:16,957 INFO === options_live_micro LIVE 2026-09-22T10:26:16.957206-04:00 share=25% ===
Live account equity $225.79 cash $225.79 #225458845 options_level=3
2026-09-22 10:26:17,152 INFO Live account equity $225.79 cash $225.79 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-22 10:26:17,450 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-22 10:26:17,561 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (189 earlier lines - see full log file)

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
## Ledger health — 2026-09-22
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1485 | WARN | <<<
| Missing exit records (post) |  1482 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |    33 | INFO |
| Total closed lots           |  2392 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-22_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-22_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1377 med=-15.9% | TAINTED n=1882 med=-38.9% | KEEP-only n=713 med=+51.6% | KILL=18 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=225.79 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260922T143117Z

- UTC timestamp: `20260922T143117Z`
- GitHub run: [#10653](https://github.com/28twagg-ops/TradingBot/actions/runs/35740736798)
- Run id: `35740736798`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`72s`
- Full logs: `logs/action_runs/20260922T143117Z_live_bot.log`, `logs/action_runs/20260922T143117Z_live_options.log`, `logs/action_runs/20260922T143117Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1378 | 49.1 | -15.9 | +43.6 | $+17,308 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 714 | 62.2 | +51.6 | +70.5 | $+11,711 |
| KEEP-only recent | 521 | 60.3 | +54.0 | +82.4 | $+7,466 |

- KEEP strategies (24): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-22T10:31:22.726947-04:00","date":"2026-09-22","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":60.6,"phases_s":{"reconcile":0.16,"cancel":0.02,"manage":3.76,"protective_stops":0.14,"scan":54.07,"entries":1.92},"signals":56,"placed":0,"equity":996015.51,"open_positions":11,"pending_orders":0,"open_lots":32,"submitted_today":17,"filled_today":17,"unattributed_contracts":0,"top_signals":["S211:AMD","S401:AMD","S210:COIN","S401:COIN","S401:META","S401:AMZN","S401:MARA","S401:MSTR"],"github_run":"10653","github_run_id":"35740736798","status":"ok","data_quality":{"clean":{"n":1378,"win":49.06,"med":-15.93,"avg":43.63,"pnl":17308.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":714,"win":62.18,"med":51.59,"avg":70.47,"pnl":11711.45},"keep_only_recent":{"n":521,"win":60.27,"med":54.0,"avg":82.38,"pnl":7466.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:31:18  INFO      Mode: exits
14:31:18  INFO        Daily log -> logs/daily/2026-09-22.md
14:31:18  INFO        Daily log reconciled -> logs/daily/2026-09-22.md (4 ledger rows)
14:31:19  INFO        Daily log -> logs/daily/2026-09-22.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.79|
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
=== options_live_micro LIVE 2026-09-22T10:31:19.803200-04:00 share=25% ===
2026-09-22 10:31:19,803 INFO === options_live_micro LIVE 2026-09-22T10:31:19.803200-04:00 share=25% ===
Live account equity $225.79 cash $225.79 #225458845 options_level=3
2026-09-22 10:31:19,858 INFO Live account equity $225.79 cash $225.79 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-22 10:31:19,881 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-22 10:31:19,895 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (187 earlier lines - see full log file)

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
## Ledger health — 2026-09-22
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1485 | WARN | <<<
| Missing exit records (post) |  1482 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |    32 | INFO |
| Total closed lots           |  2393 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-22_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-22_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1378 med=-15.9% | TAINTED n=1882 med=-38.9% | KEEP-only n=714 med=+51.6% | KILL=18 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=225.79 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260922T143623Z

- UTC timestamp: `20260922T143623Z`
- GitHub run: [#10654](https://github.com/28twagg-ops/TradingBot/actions/runs/35741315830)
- Run id: `35741315830`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`66s`
- Full logs: `logs/action_runs/20260922T143623Z_live_bot.log`, `logs/action_runs/20260922T143623Z_live_options.log`, `logs/action_runs/20260922T143623Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1378 | 49.1 | -15.9 | +43.6 | $+17,308 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 714 | 62.2 | +51.6 | +70.5 | $+11,711 |
| KEEP-only recent | 521 | 60.3 | +54.0 | +82.4 | $+7,466 |

- KEEP strategies (24): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-22T10:36:29.130172-04:00","date":"2026-09-22","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":53.6,"phases_s":{"reconcile":0.12,"cancel":0.03,"manage":3.28,"protective_stops":0.16,"scan":46.04,"entries":3.29},"signals":56,"placed":0,"equity":996059.86,"open_positions":11,"pending_orders":0,"open_lots":26,"submitted_today":17,"filled_today":17,"unattributed_contracts":0,"top_signals":["S211:AMD","S401:AMD","S210:COIN","S401:COIN","S401:META","S401:AMZN","S401:MARA","S401:MSTR"],"github_run":"10654","github_run_id":"35741315830","status":"ok","data_quality":{"clean":{"n":1378,"win":49.06,"med":-15.93,"avg":43.63,"pnl":17308.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":714,"win":62.18,"med":51.59,"avg":70.47,"pnl":11711.45},"keep_only_recent":{"n":521,"win":60.27,"med":54.0,"avg":82.38,"pnl":7466.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:36:25  INFO      Mode: exits
14:36:25  INFO        Daily log -> logs/daily/2026-09-22.md
14:36:25  INFO        Daily log reconciled -> logs/daily/2026-09-22.md (4 ledger rows)
14:36:25  INFO        Daily log -> logs/daily/2026-09-22.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.79|
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
=== options_live_micro LIVE 2026-09-22T10:36:26.192055-04:00 share=25% ===
2026-09-22 10:36:26,192 INFO === options_live_micro LIVE 2026-09-22T10:36:26.192055-04:00 share=25% ===
Live account equity $225.79 cash $225.79 #225458845 options_level=3
2026-09-22 10:36:26,248 INFO Live account equity $225.79 cash $225.79 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-22 10:36:26,282 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-22 10:36:26,303 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (194 earlier lines - see full log file)

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
## Ledger health — 2026-09-22
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1485 | WARN | <<<
| Missing exit records (post) |  1482 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |    26 | INFO |
| Total closed lots           |  2393 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-22_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-22_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1378 med=-15.9% | TAINTED n=1882 med=-38.9% | KEEP-only n=714 med=+51.6% | KILL=18 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=225.79 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260922T144141Z

- UTC timestamp: `20260922T144141Z`
- GitHub run: [#10655](https://github.com/28twagg-ops/TradingBot/actions/runs/35741900537)
- Run id: `35741900537`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`49s`
- Full logs: `logs/action_runs/20260922T144141Z_live_bot.log`, `logs/action_runs/20260922T144141Z_live_options.log`, `logs/action_runs/20260922T144141Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1378 | 49.1 | -15.9 | +43.6 | $+17,308 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 714 | 62.2 | +51.6 | +70.5 | $+11,711 |
| KEEP-only recent | 521 | 60.3 | +54.0 | +82.4 | $+7,466 |

- KEEP strategies (24): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-22T10:41:47.006749-04:00","date":"2026-09-22","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":40.4,"phases_s":{"reconcile":0.25,"cancel":0.07,"manage":3.97,"protective_stops":0.43,"scan":28.84,"entries":6.37},"signals":56,"placed":0,"equity":996222.86,"open_positions":11,"pending_orders":0,"open_lots":26,"submitted_today":17,"filled_today":17,"unattributed_contracts":0,"top_signals":["S211:AMD","S401:AMD","S210:COIN","S401:COIN","S401:META","S401:AMZN","S401:MARA","S401:MSTR"],"github_run":"10655","github_run_id":"35741900537","status":"ok","data_quality":{"clean":{"n":1378,"win":49.06,"med":-15.93,"avg":43.63,"pnl":17308.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":714,"win":62.18,"med":51.59,"avg":70.47,"pnl":11711.45},"keep_only_recent":{"n":521,"win":60.27,"med":54.0,"avg":82.38,"pnl":7466.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:41:42  INFO      Mode: exits
14:41:43  INFO        Daily log -> logs/daily/2026-09-22.md
14:41:43  INFO        Daily log reconciled -> logs/daily/2026-09-22.md (4 ledger rows)
14:41:43  INFO        Daily log -> logs/daily/2026-09-22.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.79|
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
=== options_live_micro LIVE 2026-09-22T10:41:44.145132-04:00 share=25% ===
2026-09-22 10:41:44,145 INFO === options_live_micro LIVE 2026-09-22T10:41:44.145132-04:00 share=25% ===
Live account equity $225.79 cash $225.79 #225458845 options_level=3
2026-09-22 10:41:44,257 INFO Live account equity $225.79 cash $225.79 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-22 10:41:44,339 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-22 10:41:44,392 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (187 earlier lines - see full log file)

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
## Ledger health — 2026-09-22
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1485 | WARN | <<<
| Missing exit records (post) |  1482 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |    26 | INFO |
| Total closed lots           |  2393 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-22_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-22_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1378 med=-15.9% | TAINTED n=1882 med=-38.9% | KEEP-only n=714 med=+51.6% | KILL=18 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=225.79 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260922T144612Z

- UTC timestamp: `20260922T144612Z`
- GitHub run: [#10656](https://github.com/28twagg-ops/TradingBot/actions/runs/35742484354)
- Run id: `35742484354`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`70s`
- Full logs: `logs/action_runs/20260922T144612Z_live_bot.log`, `logs/action_runs/20260922T144612Z_live_options.log`, `logs/action_runs/20260922T144612Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1378 | 49.1 | -15.9 | +43.6 | $+17,308 |
| TAINTED | 1882 | 33.3 | -38.9 | +12.7 | $-9,546 |
| KEEP-only | 714 | 62.2 | +51.6 | +70.5 | $+11,711 |
| KEEP-only recent | 521 | 60.3 | +54.0 | +82.4 | $+7,466 |

- KEEP strategies (24): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-22T10:46:19.296785-04:00","date":"2026-09-22","mode":"entry+manage","header":"entry+manage (4 new)","elapsed_s":58.0,"phases_s":{"reconcile":0.17,"cancel":0.05,"manage":4.33,"protective_stops":0.27,"scan":46.57,"entries":5.44,"reconcile2":0.27},"signals":56,"placed":4,"equity":996275.86,"open_positions":12,"pending_orders":2,"open_lots":28,"submitted_today":21,"filled_today":19,"unattributed_contracts":0,"top_signals":["S211:AMD","S401:AMD","S210:COIN","S401:COIN","S401:META","S401:AMZN","S401:MARA","S401:MSTR"],"github_run":"10656","github_run_id":"35742484354","status":"ok","data_quality":{"clean":{"n":1378,"win":49.06,"med":-15.93,"avg":43.63,"pnl":17308.16},"tainted":{"n":1882,"win":33.32,"med":-38.9,"avg":12.69,"pnl":-9546.28},"keep_only":{"n":714,"win":62.18,"med":51.59,"avg":70.47,"pnl":11711.45},"keep_only_recent":{"n":521,"win":60.27,"med":54.0,"avg":82.38,"pnl":7466.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:46:14  INFO      Mode: exits
14:46:15  INFO        Daily log -> logs/daily/2026-09-22.md
14:46:15  INFO        Daily log reconciled -> logs/daily/2026-09-22.md (4 ledger rows)
14:46:15  INFO        Daily log -> logs/daily/2026-09-22.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.79|
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
=== options_live_micro LIVE 2026-09-22T10:46:16.222528-04:00 share=25% ===
2026-09-22 10:46:16,222 INFO === options_live_micro LIVE 2026-09-22T10:46:16.222528-04:00 share=25% ===
Live account equity $225.79 cash $225.79 #225458845 options_level=3
2026-09-22 10:46:16,305 INFO Live account equity $225.79 cash $225.79 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-22 10:46:16,368 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-22 10:46:16,410 INFO Live micro done. open_options=0 lots=0
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
## Ledger health — 2026-09-22
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1485 | WARN | <<<
| Missing exit records (post) |  1482 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |    28 | INFO |
| Total closed lots           |  2393 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-22_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-22_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1378 med=-15.9% | TAINTED n=1882 med=-38.9% | KEEP-only n=714 med=+51.6% | KILL=18 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=225.79 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---
