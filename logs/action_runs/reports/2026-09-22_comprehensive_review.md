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
