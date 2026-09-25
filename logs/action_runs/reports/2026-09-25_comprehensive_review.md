# Daily Comprehensive Action Review - 2026-09-25

_Auto-generated from GitHub Actions run output. Each run appends a summary; full stdout is in linked per-run log files._
## Run 20260925T130121Z

- UTC timestamp: `20260925T130121Z`
- GitHub run: [#11031](https://github.com/28twagg-ops/TradingBot/actions/runs/36138222161)
- Run id: `36138222161`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`13s`
- Full logs: `logs/action_runs/20260925T130121Z_live_bot.log`, `logs/action_runs/20260925T130121Z_live_options.log`, `logs/action_runs/20260925T130121Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1487 | 50.2 | +13.1 | +43.0 | $+19,456 |
| TAINTED | 1897 | 33.3 | -39.0 | +12.5 | $-9,668 |
| KEEP-only | 837 | 62.4 | +52.2 | +64.9 | $+14,152 |
| KEEP-only recent | 640 | 61.6 | +55.4 | +74.2 | $+10,070 |

- KEEP strategies (26): S163, S164, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (17): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-25T09:01:26.358812-04:00","date":"2026-09-25","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.11},"signals":0,"placed":0,"equity":996584.32,"open_positions":21,"pending_orders":0,"open_lots":55,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11031","github_run_id":"36138222161","status":"ok","data_quality":{"clean":{"n":1487,"win":50.17,"med":13.11,"avg":43.01,"pnl":19456.16},"tainted":{"n":1897,"win":33.26,"med":-38.98,"avg":12.54,"pnl":-9668.28},"keep_only":{"n":837,"win":62.37,"med":52.17,"avg":64.85,"pnl":14152.45},"keep_only_recent":{"n":640,"win":61.56,"med":55.36,"avg":74.2,"pnl":10070.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S399","S405","S407","S408"]}}
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
|  Equity                                                         $224.41|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $224.41|
|  Cash                                                           $157.20|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $67.21|
|  Open P&L                                                        $-0.25|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  COP      Pullback50      $33.69     $127.75  $127.69  -0.0%   $-0.02  |
|  KNF      MomReversal     $33.51     $53.69   $53.31   -0.7%   $-0.24  |
|                                                                        |
|  Total invested                                                  $67.21|
|  Total open P&L                                                  $-0.25|
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
|  2026-09-24  SELL  AES  Pullback50  $33.74  P&L $-0.02                 |
|  2026-09-24  SELL  AES  Pullback50  $33.87  P&L $+0.06                 |
|  2026-09-24  SELL  COHR  Pullback50  $33.50  P&L $-0.31                |
|  2026-09-24  SELL  MO  Pullback50  $34.33  P&L $+0.65                  |
|  2026-09-24  SELL  MLM  MomReversal  $33.41  P&L $-0.27                |
|  2026-09-23  SELL  ADM  Pullback50  $33.46  P&L $-0.25                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-25T09:01:23.276966-04:00 share=25% ===
2026-09-25 09:01:23,277 INFO === options_live_micro LIVE 2026-09-25T09:01:23.276966-04:00 share=25% ===
Live account equity $224.41 cash $157.20 #225458845 options_level=3
2026-09-25 09:01:23,328 INFO Live account equity $224.41 cash $157.20 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-25 09:01:23,337 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-25 09:01:23,344 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 281 | 19 |
| S164 | 319 | 23 |
| S165 | 1747 | 34 |
| S166 | 139 | 10 |
| S167 | 304 | 21 |
| S168 | 224 | 18 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-25
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1578 | WARN | <<<
| Missing exit records (post) |  1578 | WARN | <<<
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |    55 | INFO |
| Total closed lots           |  2511 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-25_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-25_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1487 med=+13.1% | TAINTED n=1897 med=-39.0% | KEEP-only n=837 med=+52.2% | KILL=17 KEEP=26
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.41 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260925T130615Z

- UTC timestamp: `20260925T130615Z`
- GitHub run: [#11032](https://github.com/28twagg-ops/TradingBot/actions/runs/36138735342)
- Run id: `36138735342`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`13s`
- Full logs: `logs/action_runs/20260925T130615Z_live_bot.log`, `logs/action_runs/20260925T130615Z_live_options.log`, `logs/action_runs/20260925T130615Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1487 | 50.2 | +13.1 | +43.0 | $+19,456 |
| TAINTED | 1897 | 33.3 | -39.0 | +12.5 | $-9,668 |
| KEEP-only | 837 | 62.4 | +52.2 | +64.9 | $+14,152 |
| KEEP-only recent | 640 | 61.6 | +55.4 | +74.2 | $+10,070 |

- KEEP strategies (26): S163, S164, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (17): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-25T09:06:21.690855-04:00","date":"2026-09-25","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.2,"phases_s":{"reconcile":0.43},"signals":0,"placed":0,"equity":996543.55,"open_positions":21,"pending_orders":0,"open_lots":55,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11032","github_run_id":"36138735342","status":"ok","data_quality":{"clean":{"n":1487,"win":50.17,"med":13.11,"avg":43.01,"pnl":19456.16},"tainted":{"n":1897,"win":33.26,"med":-38.98,"avg":12.54,"pnl":-9668.28},"keep_only":{"n":837,"win":62.37,"med":52.17,"avg":64.85,"pnl":14152.45},"keep_only_recent":{"n":640,"win":61.56,"med":55.36,"avg":74.2,"pnl":10070.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:06:16  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.41|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $224.41|
|  Cash                                                           $157.20|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $67.21|
|  Open P&L                                                        $-0.25|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  COP      Pullback50      $33.69     $127.75  $127.69  -0.0%   $-0.02  |
|  KNF      MomReversal     $33.51     $53.69   $53.31   -0.7%   $-0.24  |
|                                                                        |
|  Total invested                                                  $67.21|
|  Total open P&L                                                  $-0.25|
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
|  2026-09-24  SELL  AES  Pullback50  $33.74  P&L $-0.02                 |
|  2026-09-24  SELL  AES  Pullback50  $33.87  P&L $+0.06                 |
|  2026-09-24  SELL  COHR  Pullback50  $33.50  P&L $-0.31                |
|  2026-09-24  SELL  MO  Pullback50  $34.33  P&L $+0.65                  |
|  2026-09-24  SELL  MLM  MomReversal  $33.41  P&L $-0.27                |
|  2026-09-23  SELL  ADM  Pullback50  $33.46  P&L $-0.25                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-25T09:06:18.403875-04:00 share=25% ===
2026-09-25 09:06:18,403 INFO === options_live_micro LIVE 2026-09-25T09:06:18.403875-04:00 share=25% ===
Live account equity $224.41 cash $157.20 #225458845 options_level=3
2026-09-25 09:06:18,593 INFO Live account equity $224.41 cash $157.20 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-25 09:06:18,644 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-25 09:06:18,694 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 281 | 19 |
| S164 | 319 | 23 |
| S165 | 1747 | 34 |
| S166 | 139 | 10 |
| S167 | 304 | 21 |
| S168 | 224 | 18 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-25
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1578 | WARN | <<<
| Missing exit records (post) |  1578 | WARN | <<<
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |    55 | INFO |
| Total closed lots           |  2511 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-25_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-25_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1487 med=+13.1% | TAINTED n=1897 med=-39.0% | KEEP-only n=837 med=+52.2% | KILL=17 KEEP=26
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.41 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260925T131114Z

- UTC timestamp: `20260925T131114Z`
- GitHub run: [#11033](https://github.com/28twagg-ops/TradingBot/actions/runs/36139245105)
- Run id: `36139245105`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`14s`
- Full logs: `logs/action_runs/20260925T131114Z_live_bot.log`, `logs/action_runs/20260925T131114Z_live_options.log`, `logs/action_runs/20260925T131114Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1487 | 50.2 | +13.1 | +43.0 | $+19,456 |
| TAINTED | 1897 | 33.3 | -39.0 | +12.5 | $-9,668 |
| KEEP-only | 837 | 62.4 | +52.2 | +64.9 | $+14,152 |
| KEEP-only recent | 640 | 61.6 | +55.4 | +74.2 | $+10,070 |

- KEEP strategies (26): S163, S164, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (17): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-25T09:11:20.778548-04:00","date":"2026-09-25","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.4,"phases_s":{"reconcile":0.54},"signals":0,"placed":0,"equity":996559.55,"open_positions":21,"pending_orders":0,"open_lots":55,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11033","github_run_id":"36139245105","status":"ok","data_quality":{"clean":{"n":1487,"win":50.17,"med":13.11,"avg":43.01,"pnl":19456.16},"tainted":{"n":1897,"win":33.26,"med":-38.98,"avg":12.54,"pnl":-9668.28},"keep_only":{"n":837,"win":62.37,"med":52.17,"avg":64.85,"pnl":14152.45},"keep_only_recent":{"n":640,"win":61.56,"med":55.36,"avg":74.2,"pnl":10070.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:11:15  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.30|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $224.30|
|  Cash                                                           $157.20|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $67.10|
|  Open P&L                                                        $-0.36|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  COP      Pullback50      $33.59     $127.75  $127.30  -0.4%   $-0.12  |
|  KNF      MomReversal     $33.51     $53.69   $53.31   -0.7%   $-0.24  |
|                                                                        |
|  Total invested                                                  $67.10|
|  Total open P&L                                                  $-0.36|
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
|  2026-09-24  SELL  AES  Pullback50  $33.74  P&L $-0.02                 |
|  2026-09-24  SELL  AES  Pullback50  $33.87  P&L $+0.06                 |
|  2026-09-24  SELL  COHR  Pullback50  $33.50  P&L $-0.31                |
|  2026-09-24  SELL  MO  Pullback50  $34.33  P&L $+0.65                  |
|  2026-09-24  SELL  MLM  MomReversal  $33.41  P&L $-0.27                |
|  2026-09-23  SELL  ADM  Pullback50  $33.46  P&L $-0.25                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-25T09:11:17.197660-04:00 share=25% ===
2026-09-25 09:11:17,197 INFO === options_live_micro LIVE 2026-09-25T09:11:17.197660-04:00 share=25% ===
Live account equity $224.30 cash $157.20 #225458845 options_level=3
2026-09-25 09:11:17,423 INFO Live account equity $224.30 cash $157.20 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-25 09:11:17,492 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-25 09:11:17,565 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 281 | 19 |
| S164 | 319 | 23 |
| S165 | 1747 | 34 |
| S166 | 139 | 10 |
| S167 | 304 | 21 |
| S168 | 224 | 18 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-25
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1578 | WARN | <<<
| Missing exit records (post) |  1578 | WARN | <<<
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |    55 | INFO |
| Total closed lots           |  2511 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-25_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-25_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1487 med=+13.1% | TAINTED n=1897 med=-39.0% | KEEP-only n=837 med=+52.2% | KILL=17 KEEP=26
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.3 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260925T131613Z

- UTC timestamp: `20260925T131613Z`
- GitHub run: [#11034](https://github.com/28twagg-ops/TradingBot/actions/runs/36139766730)
- Run id: `36139766730`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`14s`
- Full logs: `logs/action_runs/20260925T131613Z_live_bot.log`, `logs/action_runs/20260925T131613Z_live_options.log`, `logs/action_runs/20260925T131613Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1487 | 50.2 | +13.1 | +43.0 | $+19,456 |
| TAINTED | 1897 | 33.3 | -39.0 | +12.5 | $-9,668 |
| KEEP-only | 837 | 62.4 | +52.2 | +64.9 | $+14,152 |
| KEEP-only recent | 640 | 61.6 | +55.4 | +74.2 | $+10,070 |

- KEEP strategies (26): S163, S164, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (17): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-25T09:16:20.681450-04:00","date":"2026-09-25","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.4,"phases_s":{"reconcile":0.53},"signals":0,"placed":0,"equity":996576.55,"open_positions":21,"pending_orders":0,"open_lots":55,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11034","github_run_id":"36139766730","status":"ok","data_quality":{"clean":{"n":1487,"win":50.17,"med":13.11,"avg":43.01,"pnl":19456.16},"tainted":{"n":1897,"win":33.26,"med":-38.98,"avg":12.54,"pnl":-9668.28},"keep_only":{"n":837,"win":62.37,"med":52.17,"avg":64.85,"pnl":14152.45},"keep_only_recent":{"n":640,"win":61.56,"med":55.36,"avg":74.2,"pnl":10070.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:16:15  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.26|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $224.26|
|  Cash                                                           $157.20|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $67.06|
|  Open P&L                                                        $-0.40|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  COP      Pullback50      $33.54     $127.75  $127.12  -0.5%   $-0.17  |
|  KNF      MomReversal     $33.51     $53.69   $53.31   -0.7%   $-0.24  |
|                                                                        |
|  Total invested                                                  $67.06|
|  Total open P&L                                                  $-0.40|
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
|  2026-09-24  SELL  AES  Pullback50  $33.74  P&L $-0.02                 |
|  2026-09-24  SELL  AES  Pullback50  $33.87  P&L $+0.06                 |
|  2026-09-24  SELL  COHR  Pullback50  $33.50  P&L $-0.31                |
|  2026-09-24  SELL  MO  Pullback50  $34.33  P&L $+0.65                  |
|  2026-09-24  SELL  MLM  MomReversal  $33.41  P&L $-0.27                |
|  2026-09-23  SELL  ADM  Pullback50  $33.46  P&L $-0.25                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-25T09:16:17.224938-04:00 share=25% ===
2026-09-25 09:16:17,225 INFO === options_live_micro LIVE 2026-09-25T09:16:17.224938-04:00 share=25% ===
Live account equity $224.26 cash $157.20 #225458845 options_level=3
2026-09-25 09:16:17,451 INFO Live account equity $224.26 cash $157.20 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-25 09:16:17,520 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-25 09:16:17,588 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 281 | 19 |
| S164 | 319 | 23 |
| S165 | 1747 | 34 |
| S166 | 139 | 10 |
| S167 | 304 | 21 |
| S168 | 224 | 18 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-25
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1578 | WARN | <<<
| Missing exit records (post) |  1578 | WARN | <<<
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |    55 | INFO |
| Total closed lots           |  2511 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-25_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-25_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1487 med=+13.1% | TAINTED n=1897 med=-39.0% | KEEP-only n=837 med=+52.2% | KILL=17 KEEP=26
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.26 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260925T132113Z

- UTC timestamp: `20260925T132113Z`
- GitHub run: [#11035](https://github.com/28twagg-ops/TradingBot/actions/runs/36140284502)
- Run id: `36140284502`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`13s`
- Full logs: `logs/action_runs/20260925T132113Z_live_bot.log`, `logs/action_runs/20260925T132113Z_live_options.log`, `logs/action_runs/20260925T132113Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1487 | 50.2 | +13.1 | +43.0 | $+19,456 |
| TAINTED | 1897 | 33.3 | -39.0 | +12.5 | $-9,668 |
| KEEP-only | 837 | 62.4 | +52.2 | +64.9 | $+14,152 |
| KEEP-only recent | 640 | 61.6 | +55.4 | +74.2 | $+10,070 |

- KEEP strategies (26): S163, S164, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (17): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-25T09:21:18.515103-04:00","date":"2026-09-25","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.8,"phases_s":{"reconcile":0.11},"signals":0,"placed":0,"equity":996598.55,"open_positions":21,"pending_orders":0,"open_lots":55,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11035","github_run_id":"36140284502","status":"ok","data_quality":{"clean":{"n":1487,"win":50.17,"med":13.11,"avg":43.01,"pnl":19456.16},"tainted":{"n":1897,"win":33.26,"med":-38.98,"avg":12.54,"pnl":-9668.28},"keep_only":{"n":837,"win":62.37,"med":52.17,"avg":64.85,"pnl":14152.45},"keep_only_recent":{"n":640,"win":61.56,"med":55.36,"avg":74.2,"pnl":10070.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:21:14  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.26|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $224.26|
|  Cash                                                           $157.20|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $67.06|
|  Open P&L                                                        $-0.40|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  COP      Pullback50      $33.54     $127.75  $127.12  -0.5%   $-0.17  |
|  KNF      MomReversal     $33.51     $53.69   $53.31   -0.7%   $-0.24  |
|                                                                        |
|  Total invested                                                  $67.06|
|  Total open P&L                                                  $-0.40|
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
|  2026-09-24  SELL  AES  Pullback50  $33.74  P&L $-0.02                 |
|  2026-09-24  SELL  AES  Pullback50  $33.87  P&L $+0.06                 |
|  2026-09-24  SELL  COHR  Pullback50  $33.50  P&L $-0.31                |
|  2026-09-24  SELL  MO  Pullback50  $34.33  P&L $+0.65                  |
|  2026-09-24  SELL  MLM  MomReversal  $33.41  P&L $-0.27                |
|  2026-09-23  SELL  ADM  Pullback50  $33.46  P&L $-0.25                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-25T09:21:15.772123-04:00 share=25% ===
2026-09-25 09:21:15,772 INFO === options_live_micro LIVE 2026-09-25T09:21:15.772123-04:00 share=25% ===
Live account equity $224.26 cash $157.20 #225458845 options_level=3
2026-09-25 09:21:15,813 INFO Live account equity $224.26 cash $157.20 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-25 09:21:15,821 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-25 09:21:15,828 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 281 | 19 |
| S164 | 319 | 23 |
| S165 | 1747 | 34 |
| S166 | 139 | 10 |
| S167 | 304 | 21 |
| S168 | 224 | 18 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-25
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1578 | WARN | <<<
| Missing exit records (post) |  1578 | WARN | <<<
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |    55 | INFO |
| Total closed lots           |  2511 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-25_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-25_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1487 med=+13.1% | TAINTED n=1897 med=-39.0% | KEEP-only n=837 med=+52.2% | KILL=17 KEEP=26
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.26 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260925T132615Z

- UTC timestamp: `20260925T132615Z`
- GitHub run: [#11036](https://github.com/28twagg-ops/TradingBot/actions/runs/36140809077)
- Run id: `36140809077`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`13s`
- Full logs: `logs/action_runs/20260925T132615Z_live_bot.log`, `logs/action_runs/20260925T132615Z_live_options.log`, `logs/action_runs/20260925T132615Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1487 | 50.2 | +13.1 | +43.0 | $+19,456 |
| TAINTED | 1897 | 33.3 | -39.0 | +12.5 | $-9,668 |
| KEEP-only | 837 | 62.4 | +52.2 | +64.9 | $+14,152 |
| KEEP-only recent | 640 | 61.6 | +55.4 | +74.2 | $+10,070 |

- KEEP strategies (26): S163, S164, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (17): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-25T09:26:21.595011-04:00","date":"2026-09-25","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.2,"phases_s":{"reconcile":0.47},"signals":0,"placed":0,"equity":996677.55,"open_positions":21,"pending_orders":0,"open_lots":55,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11036","github_run_id":"36140809077","status":"ok","data_quality":{"clean":{"n":1487,"win":50.17,"med":13.11,"avg":43.01,"pnl":19456.16},"tainted":{"n":1897,"win":33.26,"med":-38.98,"avg":12.54,"pnl":-9668.28},"keep_only":{"n":837,"win":62.37,"med":52.17,"avg":64.85,"pnl":14152.45},"keep_only_recent":{"n":640,"win":61.56,"med":55.36,"avg":74.2,"pnl":10070.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:26:16  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.22|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $224.22|
|  Cash                                                           $157.20|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $67.02|
|  Open P&L                                                        $-0.44|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  COP      Pullback50      $33.51     $127.75  $127.00  -0.6%   $-0.20  |
|  KNF      MomReversal     $33.51     $53.69   $53.31   -0.7%   $-0.24  |
|                                                                        |
|  Total invested                                                  $67.02|
|  Total open P&L                                                  $-0.44|
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
|  2026-09-24  SELL  AES  Pullback50  $33.74  P&L $-0.02                 |
|  2026-09-24  SELL  AES  Pullback50  $33.87  P&L $+0.06                 |
|  2026-09-24  SELL  COHR  Pullback50  $33.50  P&L $-0.31                |
|  2026-09-24  SELL  MO  Pullback50  $34.33  P&L $+0.65                  |
|  2026-09-24  SELL  MLM  MomReversal  $33.41  P&L $-0.27                |
|  2026-09-23  SELL  ADM  Pullback50  $33.46  P&L $-0.25                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-25T09:26:18.358493-04:00 share=25% ===
2026-09-25 09:26:18,358 INFO === options_live_micro LIVE 2026-09-25T09:26:18.358493-04:00 share=25% ===
Live account equity $224.22 cash $157.20 #225458845 options_level=3
2026-09-25 09:26:18,562 INFO Live account equity $224.22 cash $157.20 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-25 09:26:18,623 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-25 09:26:18,682 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 281 | 19 |
| S164 | 319 | 23 |
| S165 | 1747 | 34 |
| S166 | 139 | 10 |
| S167 | 304 | 21 |
| S168 | 224 | 18 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-25
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1578 | WARN | <<<
| Missing exit records (post) |  1578 | WARN | <<<
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |    55 | INFO |
| Total closed lots           |  2511 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-25_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-25_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1487 med=+13.1% | TAINTED n=1897 med=-39.0% | KEEP-only n=837 med=+52.2% | KILL=17 KEEP=26
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.22 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260925T133118Z

- UTC timestamp: `20260925T133118Z`
- GitHub run: [#11037](https://github.com/28twagg-ops/TradingBot/actions/runs/36141338395)
- Run id: `36141338395`
- Live bot: exit=`0`, duration=`218s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260925T133118Z_live_bot.log`, `logs/action_runs/20260925T133118Z_live_options.log`, `logs/action_runs/20260925T133118Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1487 | 50.2 | +13.1 | +43.0 | $+19,456 |
| TAINTED | 1897 | 33.3 | -39.0 | +12.5 | $-9,668 |
| KEEP-only | 837 | 62.4 | +52.2 | +64.9 | $+14,152 |
| KEEP-only recent | 640 | 61.6 | +55.4 | +74.2 | $+10,070 |

- KEEP strategies (26): S163, S164, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (17): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-25T09:26:21.595011-04:00","date":"2026-09-25","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.2,"phases_s":{"reconcile":0.47},"signals":0,"placed":0,"equity":996677.55,"open_positions":21,"pending_orders":0,"open_lots":55,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11036","github_run_id":"36140809077","status":"ok","data_quality":{"clean":{"n":1487,"win":50.17,"med":13.11,"avg":43.01,"pnl":19456.16},"tainted":{"n":1897,"win":33.26,"med":-38.98,"avg":12.54,"pnl":-9668.28},"keep_only":{"n":837,"win":62.37,"med":52.17,"avg":64.85,"pnl":14152.45},"keep_only_recent":{"n":640,"win":61.56,"med":55.36,"avg":74.2,"pnl":10070.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:31:19  INFO      Mode: morning_prep
13:31:20  INFO        [prep_positions] 2/2 (2 valid)
13:31:20  INFO      Fetching tickers (universe=both)...
13:31:20  INFO        S&P 500: 503
13:31:21  INFO        MidCap 400: 400
13:31:21  INFO        Total: 903 tickers
13:31:22  INFO        [prep_universe] 40/901 (40 valid)
13:31:23  INFO        [prep_universe] 80/901 (80 valid)
13:31:25  INFO        [prep_universe] 120/901 (120 valid)
13:31:26  INFO        [prep_universe] 160/901 (160 valid)
13:31:28  INFO        [prep_universe] 200/901 (199 valid)
13:31:35  INFO        [prep_universe] 240/901 (238 valid)
13:31:45  INFO        [prep_universe] 280/901 (278 valid)
13:31:58  INFO        [prep_universe] 320/901 (318 valid)
13:32:11  INFO        [prep_universe] 360/901 (358 valid)
13:32:22  INFO        [prep_universe] 400/901 (398 valid)
13:32:34  INFO        [prep_universe] 440/901 (438 valid)
13:32:47  INFO        [prep_universe] 480/901 (478 valid)
13:32:58  INFO        [prep_universe] 520/901 (518 valid)
13:33:11  INFO        [prep_universe] 560/901 (558 valid)
13:33:21  INFO        [prep_universe] 600/901 (598 valid)
13:33:34  INFO        [prep_universe] 640/901 (638 valid)
13:33:47  INFO        [prep_universe] 680/901 (678 valid)
13:33:58  INFO        [prep_universe] 720/901 (718 valid)
13:34:11  INFO        [prep_universe] 760/901 (758 valid)
13:34:21  INFO        [prep_universe] 800/901 (798 valid)
13:34:34  INFO        [prep_universe] 840/901 (838 valid)
13:34:47  INFO        [prep_universe] 880/901 (878 valid)
13:34:54  INFO        [prep_universe] 901/901 (899 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.61|
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
|  Invested                                                        $67.41|
|  Open P&L                                                        $-0.05|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  COP      Pullback50      $33.66     $127.75  $127.55  -0.2%   $-0.05  |
|  KNF      MomReversal     $33.76     $53.69   $53.70   +0.0%   $+0.01  |
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
|  Signal candidates                                                   21|
|  Universe scanned                                                   901|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-25T09:34:57.225955-04:00 share=25% ===
2026-09-25 09:34:57,226 INFO === options_live_micro LIVE 2026-09-25T09:34:57.225955-04:00 share=25% ===
Live account equity $224.45 cash $157.20 #225458845 options_level=3
2026-09-25 09:34:57,710 INFO Live account equity $224.45 cash $157.20 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-25 09:34:57,846 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-25 09:34:57,938 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=55 paper_keys=yes dry_run=False
  alpaca positions=16
  FLAG b182|S217|1ee5deac missing from Alpaca
  FLAG b313|S355|7cd7364f missing from Alpaca
  FLAG b312|S355|701d857b missing from Alpaca
  FLAG b305|S354|be81694b missing from Alpaca
  FLAG b304|S354|83cbcf5c missing from Alpaca
  FLAG b407|S364|e3631db2 missing from Alpaca
  FLAG b406|S364|1a908a71 missing from Alpaca
  FLAG b393|S363|d774b079 missing from Alpaca
  FLAG b392|S363|2bac38c5 missing from Alpaca
  FLAG b315|S355|082099ad missing from Alpaca
  FLAG b314|S355|c1c792c6 missing from Alpaca
  FLAG b307|S354|e475bc43 missing from Alpaca
  FLAG b306|S354|09906e47 missing from Alpaca
  FLAG b1139|S163|fb350c4b missing from Alpaca
  FLAG b1138|S163|59763089 missing from Alpaca
  FLAG b1125|S168|577dd84f missing from Alpaca
  FLAG b1124|S168|df03928c missing from Alpaca
  FLAG b1137|S163|8769e380 missing from Alpaca
  FLAG b1136|S163|28c5f119 missing from Alpaca
  FLAG b1123|S168|bdd3fc1b missing from Alpaca
  FLAG b1122|S168|8e9d1a64 missing from Alpaca
  FLAG b167|S216|c2b7214d missing from Alpaca
  FLAG b919|S412|07761773 missing from Alpaca
  FLAG b918|S412|a7424798 missing from Alpaca
  FLAG b369|S361|aeab0d40 missing from Alpaca
  FLAG b368|S361|0f1513f0 missing from Alpaca
  FLAG b905|S411|5ec849b3 missing from Alpaca
  FLAG b904|S411|a172c811 missing from Alpaca
  FLAG b806|S404|207b10b2 missing from Alpaca
  FLAG b783|S397|8a0dcd91 missing from Alpaca
  FLAG b0|ORPHAN|b11f80ab missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$996,170.77
  buying_power=$3,934,239.88 cash=$1,030,948.77
  open option orders: 10
    MCD260925C00272500 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=0.01
    MS260925C00210000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=0.01
    MARA260925C00014500 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=0.01
    SMCI260925C00040000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
    SMCI260925C00042000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
  open option positions: 15
    JPM260925C00342500 qty=6 mkt=$306.00
    JPM260925C00345000 qty=-1 mkt=$-24.00
    MARA260925C00011500 qty=-1 mkt=$-116.00
    MARA260925C00012000 qty=-1 mkt=$-66.00
    MARA260925C00014500 qty=1 mkt=$0.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-25T09:35:01.788418-04:00 ===

[Run context]
Paper auth OK — equity $996176.77, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
  EXIT [b391|lab0391_s363_w1_0928_1005_r2|S363] take_profit (+61.8%) SELL failed SMCI261002C00044500: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b390|lab0390_s363_w1_0928_1005_r1|S363] take_profit (+61.8%) SELL failed SMCI261002C00044500: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b194|lab0194_s218_w2_1005_1045_r1|S218] stop_loss (-95.3%) SELL failed MCD260925C00245000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
2026-09-25 09:35:05,145 INFO   EXIT [b421|lab0421_s365_w2_1005_1045_r2|S365] stop_loss (-50.0%) SELL 1 MARA261009C00014500 @<= 0.24
2026-09-25 09:35:06,925 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-44.1%) SELL 1 MARA261009C00014000 @<= 0.34
2026-09-25 09:35:08,137 INFO   EXIT [b168|lab0168_s216_w3_1045_1120_r1|S216] stop_loss (-61.0%) SELL 1 V260925C00370000 @<= 0.24
Protective stops: placed=0 upgraded=0 already=7 failed=4 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
```

---

## Run 20260925T133651Z

- UTC timestamp: `20260925T133651Z`
- GitHub run: [#11038](https://github.com/28twagg-ops/TradingBot/actions/runs/36141868251)
- Run id: `36141868251`
- Live bot: exit=`0`, duration=`218s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260925T133651Z_live_bot.log`, `logs/action_runs/20260925T133651Z_live_options.log`, `logs/action_runs/20260925T133651Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1487 | 50.2 | +13.1 | +43.0 | $+19,456 |
| TAINTED | 1897 | 33.3 | -39.0 | +12.5 | $-9,668 |
| KEEP-only | 837 | 62.4 | +52.2 | +64.9 | $+14,152 |
| KEEP-only recent | 640 | 61.6 | +55.4 | +74.2 | $+10,070 |

- KEEP strategies (26): S163, S164, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (17): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-25T09:26:21.595011-04:00","date":"2026-09-25","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.2,"phases_s":{"reconcile":0.47},"signals":0,"placed":0,"equity":996677.55,"open_positions":21,"pending_orders":0,"open_lots":55,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11036","github_run_id":"36140809077","status":"ok","data_quality":{"clean":{"n":1487,"win":50.17,"med":13.11,"avg":43.01,"pnl":19456.16},"tainted":{"n":1897,"win":33.26,"med":-38.98,"avg":12.54,"pnl":-9668.28},"keep_only":{"n":837,"win":62.37,"med":52.17,"avg":64.85,"pnl":14152.45},"keep_only_recent":{"n":640,"win":61.56,"med":55.36,"avg":74.2,"pnl":10070.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:36:52  INFO      Mode: morning_prep
13:36:53  INFO        [prep_positions] 2/2 (2 valid)
13:36:53  INFO      Fetching tickers (universe=both)...
13:36:53  INFO        S&P 500: 503
13:36:53  INFO        MidCap 400: 400
13:36:53  INFO        Total: 903 tickers
13:36:54  INFO        [prep_universe] 40/901 (40 valid)
13:36:55  INFO        [prep_universe] 80/901 (80 valid)
13:36:57  INFO        [prep_universe] 120/901 (120 valid)
13:36:58  INFO        [prep_universe] 160/901 (160 valid)
13:36:59  INFO        [prep_universe] 200/901 (199 valid)
13:37:07  INFO        [prep_universe] 240/901 (238 valid)
13:37:20  INFO        [prep_universe] 280/901 (278 valid)
13:37:30  INFO        [prep_universe] 320/901 (318 valid)
13:37:43  INFO        [prep_universe] 360/901 (358 valid)
13:37:56  INFO        [prep_universe] 400/901 (398 valid)
13:38:06  INFO        [prep_universe] 440/901 (438 valid)
13:38:19  INFO        [prep_universe] 480/901 (478 valid)
13:38:32  INFO        [prep_universe] 520/901 (518 valid)
13:38:42  INFO        [prep_universe] 560/901 (558 valid)
13:38:55  INFO        [prep_universe] 600/901 (598 valid)
13:39:08  INFO        [prep_universe] 640/901 (638 valid)
13:39:18  INFO        [prep_universe] 680/901 (678 valid)
13:39:31  INFO        [prep_universe] 720/901 (718 valid)
13:39:44  INFO        [prep_universe] 760/901 (758 valid)
13:39:53  INFO        [prep_universe] 800/901 (798 valid)
13:40:07  INFO        [prep_universe] 840/901 (838 valid)
13:40:20  INFO        [prep_universe] 880/901 (878 valid)
13:40:26  INFO        [prep_universe] 901/901 (899 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.20|
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
|  Invested                                                        $67.00|
|  Open P&L                                                        $-0.46|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  COP      Pullback50      $33.72     $127.75  $127.77  +0.0%   $+0.01  |
|  KNF      MomReversal     $33.29     $53.69   $52.95   -1.4%   $-0.46  |
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
|  Signal candidates                                                   24|
|  Universe scanned                                                   901|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-25T09:40:29.818855-04:00 share=25% ===
2026-09-25 09:40:29,818 INFO === options_live_micro LIVE 2026-09-25T09:40:29.818855-04:00 share=25% ===
Live account equity $224.35 cash $157.20 #225458845 options_level=3
2026-09-25 09:40:29,861 INFO Live account equity $224.35 cash $157.20 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-25 09:40:29,885 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-25 09:40:29,902 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=55 paper_keys=yes dry_run=False
  alpaca positions=16
  FLAG b182|S217|1ee5deac missing from Alpaca
  FLAG b313|S355|7cd7364f missing from Alpaca
  FLAG b312|S355|701d857b missing from Alpaca
  FLAG b305|S354|be81694b missing from Alpaca
  FLAG b304|S354|83cbcf5c missing from Alpaca
  FLAG b407|S364|e3631db2 missing from Alpaca
  FLAG b406|S364|1a908a71 missing from Alpaca
  FLAG b393|S363|d774b079 missing from Alpaca
  FLAG b392|S363|2bac38c5 missing from Alpaca
  FLAG b315|S355|082099ad missing from Alpaca
  FLAG b314|S355|c1c792c6 missing from Alpaca
  FLAG b307|S354|e475bc43 missing from Alpaca
  FLAG b306|S354|09906e47 missing from Alpaca
  FLAG b1139|S163|fb350c4b missing from Alpaca
  FLAG b1138|S163|59763089 missing from Alpaca
  FLAG b1125|S168|577dd84f missing from Alpaca
  FLAG b1124|S168|df03928c missing from Alpaca
  FLAG b1137|S163|8769e380 missing from Alpaca
  FLAG b1136|S163|28c5f119 missing from Alpaca
  FLAG b1123|S168|bdd3fc1b missing from Alpaca
  FLAG b1122|S168|8e9d1a64 missing from Alpaca
  FLAG b167|S216|c2b7214d missing from Alpaca
  FLAG b919|S412|07761773 missing from Alpaca
  FLAG b918|S412|a7424798 missing from Alpaca
  FLAG b369|S361|aeab0d40 missing from Alpaca
  FLAG b368|S361|0f1513f0 missing from Alpaca
  FLAG b905|S411|5ec849b3 missing from Alpaca
  FLAG b904|S411|a172c811 missing from Alpaca
  FLAG b806|S404|207b10b2 missing from Alpaca
  FLAG b783|S397|8a0dcd91 missing from Alpaca
  FLAG b0|ORPHAN|b11f80ab missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$996,206.23
  buying_power=$3,934,817.52 cash=$1,031,006.73
  open option orders: 9
    V260925C00370000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=0.24
    MCD260925C00272500 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=0.01
    MS260925C00210000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=0.01
    MARA260925C00014500 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=0.01
    SMCI260925C00040000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
  open option positions: 15
    JPM260925C00342500 qty=6 mkt=$264.00
    JPM260925C00345000 qty=-1 mkt=$-20.00
    MARA260925C00011500 qty=-1 mkt=$-134.00
    MARA260925C00012000 qty=-1 mkt=$-80.00
    MARA260925C00014500 qty=1 mkt=$0.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-25T09:40:33.620531-04:00 ===

[Run context]
Paper auth OK — equity $996200.23, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
  EXIT [b194|lab0194_s218_w2_1005_1045_r1|S218] stop_loss (-95.3%) SELL failed MCD260925C00245000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b391|lab0391_s363_w1_0928_1005_r2|S363] take_profit (+78.2%) SELL failed SMCI261002C00044500: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b390|lab0390_s363_w1_0928_1005_r1|S363] take_profit (+78.2%) SELL failed SMCI261002C00044500: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
Protective stops: placed=2 upgraded=0 already=5 failed=4 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
```

---

## Run 20260925T134237Z

- UTC timestamp: `20260925T134237Z`
- GitHub run: [#11039](https://github.com/28twagg-ops/TradingBot/actions/runs/36142402893)
- Run id: `36142402893`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260925T134237Z_live_bot.log`, `logs/action_runs/20260925T134237Z_live_options.log`, `logs/action_runs/20260925T134237Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1487 | 50.2 | +13.1 | +43.0 | $+19,456 |
| TAINTED | 1897 | 33.3 | -39.0 | +12.5 | $-9,668 |
| KEEP-only | 837 | 62.4 | +52.2 | +64.9 | $+14,152 |
| KEEP-only recent | 640 | 61.6 | +55.4 | +74.2 | $+10,070 |

- KEEP strategies (26): S163, S164, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S401, S403, S404, S406, S411, S412
- KILL strategies (17): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S399, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-25T09:26:21.595011-04:00","date":"2026-09-25","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.2,"phases_s":{"reconcile":0.47},"signals":0,"placed":0,"equity":996677.55,"open_positions":21,"pending_orders":0,"open_lots":55,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"11036","github_run_id":"36140809077","status":"ok","data_quality":{"clean":{"n":1487,"win":50.17,"med":13.11,"avg":43.01,"pnl":19456.16},"tainted":{"n":1897,"win":33.26,"med":-38.98,"avg":12.54,"pnl":-9668.28},"keep_only":{"n":837,"win":62.37,"med":52.17,"avg":64.85,"pnl":14152.45},"keep_only_recent":{"n":640,"win":61.56,"med":55.36,"avg":74.2,"pnl":10070.0},"keep_strategies":["S163","S164","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S401","S403","S404","S406","S411","S412"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S399","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:42:39  INFO      Mode: morning_prep
13:42:39  INFO        [prep_positions] 2/2 (2 valid)
13:42:39  INFO        Universe cache hit: 903 tickers (tickers_2026-09-25.json)
13:42:40  INFO        [prep_universe] 40/901 (40 valid)
13:42:41  INFO        [prep_universe] 80/901 (80 valid)
13:42:43  INFO        [prep_universe] 120/901 (120 valid)
13:42:44  INFO        [prep_universe] 160/901 (160 valid)
13:42:45  INFO        [prep_universe] 200/901 (199 valid)
13:42:52  INFO        [prep_universe] 240/901 (238 valid)
13:43:05  INFO        [prep_universe] 280/901 (278 valid)
13:43:18  INFO        [prep_universe] 320/901 (318 valid)
13:43:28  INFO        [prep_universe] 360/901 (358 valid)
13:43:41  INFO        [prep_universe] 400/901 (398 valid)
13:43:54  INFO        [prep_universe] 440/901 (438 valid)
13:44:07  INFO        [prep_universe] 480/901 (478 valid)
13:44:17  INFO        [prep_universe] 520/901 (518 valid)
13:44:30  INFO        [prep_universe] 560/901 (558 valid)
13:44:42  INFO        [prep_universe] 600/901 (598 valid)
13:44:52  INFO        [prep_universe] 640/901 (638 valid)
13:45:05  INFO        [prep_universe] 680/901 (678 valid)
13:45:18  INFO        [prep_universe] 720/901 (718 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---
