# Daily Comprehensive Action Review - 2026-09-04

_Auto-generated from GitHub Actions run output. Each run appends a summary; full stdout is in linked per-run log files._
## Run 20260904T130109Z

- UTC timestamp: `20260904T130109Z`
- GitHub run: [#9052](https://github.com/28twagg-ops/TradingBot/actions/runs/33875654882)
- Run id: `33875654882`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`14s`
- Full logs: `logs/action_runs/20260904T130109Z_live_bot.log`, `logs/action_runs/20260904T130109Z_live_options.log`, `logs/action_runs/20260904T130109Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1010 | 49.8 | +0.0 | +47.0 | $+15,267 |
| TAINTED | 1772 | 33.2 | -39.0 | +12.3 | $-9,135 |
| KEEP-only | 554 | 63.7 | +51.2 | +74.5 | $+10,136 |
| KEEP-only recent | 346 | 60.4 | +53.8 | +91.5 | $+4,879 |

- KEEP strategies (23): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S359, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (16): ORPHAN, S164, S203, S207, S211, S212, S216, S217, S351, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T09:01:17.125111-04:00","date":"2026-09-04","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.3,"phases_s":{"reconcile":0.54},"signals":0,"placed":0,"equity":1007263.09,"open_positions":15,"pending_orders":0,"open_lots":19,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9052","github_run_id":"33875654882","status":"ok","data_quality":{"clean":{"n":1010,"win":49.8,"med":0.0,"avg":46.97,"pnl":15267.13},"tainted":{"n":1772,"win":33.18,"med":-39.02,"avg":12.29,"pnl":-9135.34},"keep_only":{"n":554,"win":63.72,"med":51.18,"avg":74.54,"pnl":10136.45},"keep_only_recent":{"n":346,"win":60.4,"med":53.78,"avg":91.49,"pnl":4879.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S359","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S203","S207","S211","S212","S216","S217","S351","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:01:10  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.52|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $230.52|
|  Cash                                                           $160.84|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $69.68|
|  Open P&L                                                        $+0.54|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AMZN     Pullback50      $35.14     $255.49  $259.60  +1.6%   $+0.56  |
|  LII      MomReversal     $34.54     $386.29  $386.08  -0.1%   $-0.02  |
|                                                                        |
|  Total invested                                                  $69.68|
|  Total open P&L                                                  $+0.54|
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
|  2026-09-03  SELL  ACGL  Pullback50  $34.56  P&L $-0.00                |
|  2026-09-03  SELL  CNM  MomReversal  $34.27  P&L $-0.24                |
|  2026-09-03  SELL  ACGL  Pullback50  $34.60  P&L $+0.00                |
|  2026-09-03  SELL  AES  Pullback50  $34.50  P&L $+0.00                 |
|  2026-09-02  SELL  MO  Pullback50  $34.52  P&L $+0.00                  |
|  2026-09-02  SELL  AES  Pullback50  $34.50  P&L $-0.03                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-04T09:01:12.871029-04:00 share=25% ===
2026-09-04 09:01:12,871 INFO === options_live_micro LIVE 2026-09-04T09:01:12.871029-04:00 share=25% ===
Live account equity $230.52 cash $160.84 #225458845 options_level=3
2026-09-04 09:01:13,100 INFO Live account equity $230.52 cash $160.84 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-04 09:01:13,171 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-04 09:01:13,242 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (160 earlier lines - see full log file)
| w1     |    4 |    3 |    8 |    2 |    4 |    3 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    32 |
| w2     |    6 |    5 |   11 |    6 |    6 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    48 |
| w3     |    8 |    6 |   13 |    5 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    56 |
| w4     |    6 |    4 |   10 |    3 |    5 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    43 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 233 | 10 |
| S164 | 249 | 11 |
| S165 | 1695 | 24 |
| S166 | 125 | 7 |
| S167 | 249 | 11 |
| S168 | 180 | 9 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-04
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   981 | WARN | <<<
| Missing exit records (post) |   981 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |    19 | INFO |
| Total closed lots           |  1967 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1010 med=+0.0% | TAINTED n=1772 med=-39.0% | KEEP-only n=554 med=+51.2% | KILL=16 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.52 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260904T130601Z

- UTC timestamp: `20260904T130601Z`
- GitHub run: [#9053](https://github.com/28twagg-ops/TradingBot/actions/runs/33876103043)
- Run id: `33876103043`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`13s`
- Full logs: `logs/action_runs/20260904T130601Z_live_bot.log`, `logs/action_runs/20260904T130601Z_live_options.log`, `logs/action_runs/20260904T130601Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1010 | 49.8 | +0.0 | +47.0 | $+15,267 |
| TAINTED | 1772 | 33.2 | -39.0 | +12.3 | $-9,135 |
| KEEP-only | 554 | 63.7 | +51.2 | +74.5 | $+10,136 |
| KEEP-only recent | 346 | 60.4 | +53.8 | +91.5 | $+4,879 |

- KEEP strategies (23): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S359, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (16): ORPHAN, S164, S203, S207, S211, S212, S216, S217, S351, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T09:06:08.422526-04:00","date":"2026-09-04","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.5,"phases_s":{"reconcile":0.65},"signals":0,"placed":0,"equity":1007263.09,"open_positions":15,"pending_orders":0,"open_lots":19,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9053","github_run_id":"33876103043","status":"ok","data_quality":{"clean":{"n":1010,"win":49.8,"med":0.0,"avg":46.97,"pnl":15267.13},"tainted":{"n":1772,"win":33.18,"med":-39.02,"avg":12.29,"pnl":-9135.34},"keep_only":{"n":554,"win":63.72,"med":51.18,"avg":74.54,"pnl":10136.45},"keep_only_recent":{"n":346,"win":60.4,"med":53.78,"avg":91.49,"pnl":4879.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S359","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S203","S207","S211","S212","S216","S217","S351","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:06:02  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.51|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $230.51|
|  Cash                                                           $160.84|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $69.67|
|  Open P&L                                                        $+0.53|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AMZN     Pullback50      $35.13     $255.49  $259.56  +1.6%   $+0.55  |
|  LII      MomReversal     $34.54     $386.29  $386.08  -0.1%   $-0.02  |
|                                                                        |
|  Total invested                                                  $69.67|
|  Total open P&L                                                  $+0.53|
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
|  2026-09-03  SELL  ACGL  Pullback50  $34.56  P&L $-0.00                |
|  2026-09-03  SELL  CNM  MomReversal  $34.27  P&L $-0.24                |
|  2026-09-03  SELL  ACGL  Pullback50  $34.60  P&L $+0.00                |
|  2026-09-03  SELL  AES  Pullback50  $34.50  P&L $+0.00                 |
|  2026-09-02  SELL  MO  Pullback50  $34.52  P&L $+0.00                  |
|  2026-09-02  SELL  AES  Pullback50  $34.50  P&L $-0.03                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-04T09:06:05.010610-04:00 share=25% ===
2026-09-04 09:06:05,010 INFO === options_live_micro LIVE 2026-09-04T09:06:05.010610-04:00 share=25% ===
Live account equity $230.51 cash $160.84 #225458845 options_level=3
2026-09-04 09:06:05,252 INFO Live account equity $230.51 cash $160.84 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-04 09:06:05,325 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-04 09:06:05,398 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (160 earlier lines - see full log file)
| w1     |    4 |    3 |    8 |    2 |    4 |    3 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    32 |
| w2     |    6 |    5 |   11 |    6 |    6 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    48 |
| w3     |    8 |    6 |   13 |    5 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    56 |
| w4     |    6 |    4 |   10 |    3 |    5 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    43 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 233 | 10 |
| S164 | 249 | 11 |
| S165 | 1695 | 24 |
| S166 | 125 | 7 |
| S167 | 249 | 11 |
| S168 | 180 | 9 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-04
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   981 | WARN | <<<
| Missing exit records (post) |   981 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |    19 | INFO |
| Total closed lots           |  1967 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1010 med=+0.0% | TAINTED n=1772 med=-39.0% | KEEP-only n=554 med=+51.2% | KILL=16 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.51 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260904T131108Z

- UTC timestamp: `20260904T131108Z`
- GitHub run: [#9054](https://github.com/28twagg-ops/TradingBot/actions/runs/33876553539)
- Run id: `33876553539`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`12s`
- Full logs: `logs/action_runs/20260904T131108Z_live_bot.log`, `logs/action_runs/20260904T131108Z_live_options.log`, `logs/action_runs/20260904T131108Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1010 | 49.8 | +0.0 | +47.0 | $+15,267 |
| TAINTED | 1772 | 33.2 | -39.0 | +12.3 | $-9,135 |
| KEEP-only | 554 | 63.7 | +51.2 | +74.5 | $+10,136 |
| KEEP-only recent | 346 | 60.4 | +53.8 | +91.5 | $+4,879 |

- KEEP strategies (23): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S359, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (16): ORPHAN, S164, S203, S207, S211, S212, S216, S217, S351, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T09:11:16.582225-04:00","date":"2026-09-04","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.4,"phases_s":{"reconcile":0.69},"signals":0,"placed":0,"equity":1007263.09,"open_positions":15,"pending_orders":0,"open_lots":19,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9054","github_run_id":"33876553539","status":"ok","data_quality":{"clean":{"n":1010,"win":49.8,"med":0.0,"avg":46.97,"pnl":15267.13},"tainted":{"n":1772,"win":33.18,"med":-39.02,"avg":12.29,"pnl":-9135.34},"keep_only":{"n":554,"win":63.72,"med":51.18,"avg":74.54,"pnl":10136.45},"keep_only_recent":{"n":346,"win":60.4,"med":53.78,"avg":91.49,"pnl":4879.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S359","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S203","S207","S211","S212","S216","S217","S351","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:11:10  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.51|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $230.51|
|  Cash                                                           $160.84|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $69.67|
|  Open P&L                                                        $+0.53|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AMZN     Pullback50      $35.13     $255.49  $259.56  +1.6%   $+0.55  |
|  LII      MomReversal     $34.54     $386.29  $386.08  -0.1%   $-0.02  |
|                                                                        |
|  Total invested                                                  $69.67|
|  Total open P&L                                                  $+0.53|
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
|  2026-09-03  SELL  ACGL  Pullback50  $34.56  P&L $-0.00                |
|  2026-09-03  SELL  CNM  MomReversal  $34.27  P&L $-0.24                |
|  2026-09-03  SELL  ACGL  Pullback50  $34.60  P&L $+0.00                |
|  2026-09-03  SELL  AES  Pullback50  $34.50  P&L $+0.00                 |
|  2026-09-02  SELL  MO  Pullback50  $34.52  P&L $+0.00                  |
|  2026-09-02  SELL  AES  Pullback50  $34.50  P&L $-0.03                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-04T09:11:12.753051-04:00 share=25% ===
2026-09-04 09:11:12,753 INFO === options_live_micro LIVE 2026-09-04T09:11:12.753051-04:00 share=25% ===
Live account equity $230.51 cash $160.84 #225458845 options_level=3
2026-09-04 09:11:12,974 INFO Live account equity $230.51 cash $160.84 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-04 09:11:13,074 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-04 09:11:13,143 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (160 earlier lines - see full log file)
| w1     |    4 |    3 |    8 |    2 |    4 |    3 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    32 |
| w2     |    6 |    5 |   11 |    6 |    6 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    48 |
| w3     |    8 |    6 |   13 |    5 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    56 |
| w4     |    6 |    4 |   10 |    3 |    5 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    43 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 233 | 10 |
| S164 | 249 | 11 |
| S165 | 1695 | 24 |
| S166 | 125 | 7 |
| S167 | 249 | 11 |
| S168 | 180 | 9 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-04
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   981 | WARN | <<<
| Missing exit records (post) |   981 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |    19 | INFO |
| Total closed lots           |  1967 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1010 med=+0.0% | TAINTED n=1772 med=-39.0% | KEEP-only n=554 med=+51.2% | KILL=16 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.51 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260904T131610Z

- UTC timestamp: `20260904T131610Z`
- GitHub run: [#9055](https://github.com/28twagg-ops/TradingBot/actions/runs/33877014653)
- Run id: `33877014653`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`12s`
- Full logs: `logs/action_runs/20260904T131610Z_live_bot.log`, `logs/action_runs/20260904T131610Z_live_options.log`, `logs/action_runs/20260904T131610Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1010 | 49.8 | +0.0 | +47.0 | $+15,267 |
| TAINTED | 1772 | 33.2 | -39.0 | +12.3 | $-9,135 |
| KEEP-only | 554 | 63.7 | +51.2 | +74.5 | $+10,136 |
| KEEP-only recent | 346 | 60.4 | +53.8 | +91.5 | $+4,879 |

- KEEP strategies (23): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S359, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (16): ORPHAN, S164, S203, S207, S211, S212, S216, S217, S351, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T09:16:15.708973-04:00","date":"2026-09-04","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.12},"signals":0,"placed":0,"equity":1007263.09,"open_positions":15,"pending_orders":0,"open_lots":19,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9055","github_run_id":"33877014653","status":"ok","data_quality":{"clean":{"n":1010,"win":49.8,"med":0.0,"avg":46.97,"pnl":15267.13},"tainted":{"n":1772,"win":33.18,"med":-39.02,"avg":12.29,"pnl":-9135.34},"keep_only":{"n":554,"win":63.72,"med":51.18,"avg":74.54,"pnl":10136.45},"keep_only_recent":{"n":346,"win":60.4,"med":53.78,"avg":91.49,"pnl":4879.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S359","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S203","S207","S211","S212","S216","S217","S351","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:16:11  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.53|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $230.53|
|  Cash                                                           $160.84|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $69.69|
|  Open P&L                                                        $+0.55|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AMZN     Pullback50      $35.15     $255.49  $259.72  +1.7%   $+0.57  |
|  LII      MomReversal     $34.54     $386.29  $386.08  -0.1%   $-0.02  |
|                                                                        |
|  Total invested                                                  $69.69|
|  Total open P&L                                                  $+0.55|
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
|  2026-09-03  SELL  ACGL  Pullback50  $34.56  P&L $-0.00                |
|  2026-09-03  SELL  CNM  MomReversal  $34.27  P&L $-0.24                |
|  2026-09-03  SELL  ACGL  Pullback50  $34.60  P&L $+0.00                |
|  2026-09-03  SELL  AES  Pullback50  $34.50  P&L $+0.00                 |
|  2026-09-02  SELL  MO  Pullback50  $34.52  P&L $+0.00                  |
|  2026-09-02  SELL  AES  Pullback50  $34.50  P&L $-0.03                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-04T09:16:13.018260-04:00 share=25% ===
2026-09-04 09:16:13,018 INFO === options_live_micro LIVE 2026-09-04T09:16:13.018260-04:00 share=25% ===
Live account equity $230.53 cash $160.84 #225458845 options_level=3
2026-09-04 09:16:13,075 INFO Live account equity $230.53 cash $160.84 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-04 09:16:13,094 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-04 09:16:13,105 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (160 earlier lines - see full log file)
| w1     |    4 |    3 |    8 |    2 |    4 |    3 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    32 |
| w2     |    6 |    5 |   11 |    6 |    6 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    48 |
| w3     |    8 |    6 |   13 |    5 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    56 |
| w4     |    6 |    4 |   10 |    3 |    5 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    43 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 233 | 10 |
| S164 | 249 | 11 |
| S165 | 1695 | 24 |
| S166 | 125 | 7 |
| S167 | 249 | 11 |
| S168 | 180 | 9 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-04
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   981 | WARN | <<<
| Missing exit records (post) |   981 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |    19 | INFO |
| Total closed lots           |  1967 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1010 med=+0.0% | TAINTED n=1772 med=-39.0% | KEEP-only n=554 med=+51.2% | KILL=16 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.53 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260904T132059Z

- UTC timestamp: `20260904T132059Z`
- GitHub run: [#9056](https://github.com/28twagg-ops/TradingBot/actions/runs/33877473696)
- Run id: `33877473696`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`14s`
- Full logs: `logs/action_runs/20260904T132059Z_live_bot.log`, `logs/action_runs/20260904T132059Z_live_options.log`, `logs/action_runs/20260904T132059Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1010 | 49.8 | +0.0 | +47.0 | $+15,267 |
| TAINTED | 1772 | 33.2 | -39.0 | +12.3 | $-9,135 |
| KEEP-only | 554 | 63.7 | +51.2 | +74.5 | $+10,136 |
| KEEP-only recent | 346 | 60.4 | +53.8 | +91.5 | $+4,879 |

- KEEP strategies (23): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S359, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (16): ORPHAN, S164, S203, S207, S211, S212, S216, S217, S351, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T09:21:05.517829-04:00","date":"2026-09-04","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.6,"phases_s":{"reconcile":0.55},"signals":0,"placed":0,"equity":1007263.09,"open_positions":15,"pending_orders":0,"open_lots":19,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9056","github_run_id":"33877473696","status":"ok","data_quality":{"clean":{"n":1010,"win":49.8,"med":0.0,"avg":46.97,"pnl":15267.13},"tainted":{"n":1772,"win":33.18,"med":-39.02,"avg":12.29,"pnl":-9135.34},"keep_only":{"n":554,"win":63.72,"med":51.18,"avg":74.54,"pnl":10136.45},"keep_only_recent":{"n":346,"win":60.4,"med":53.78,"avg":91.49,"pnl":4879.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S359","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S203","S207","S211","S212","S216","S217","S351","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:21:00  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.51|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $230.51|
|  Cash                                                           $160.84|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $69.67|
|  Open P&L                                                        $+0.53|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AMZN     Pullback50      $35.12     $255.49  $259.51  +1.6%   $+0.54  |
|  LII      MomReversal     $34.54     $386.29  $386.08  -0.1%   $-0.02  |
|                                                                        |
|  Total invested                                                  $69.67|
|  Total open P&L                                                  $+0.53|
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
|  2026-09-03  SELL  ACGL  Pullback50  $34.56  P&L $-0.00                |
|  2026-09-03  SELL  CNM  MomReversal  $34.27  P&L $-0.24                |
|  2026-09-03  SELL  ACGL  Pullback50  $34.60  P&L $+0.00                |
|  2026-09-03  SELL  AES  Pullback50  $34.50  P&L $+0.00                 |
|  2026-09-02  SELL  MO  Pullback50  $34.52  P&L $+0.00                  |
|  2026-09-02  SELL  AES  Pullback50  $34.50  P&L $-0.03                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-04T09:21:01.933448-04:00 share=25% ===
2026-09-04 09:21:01,933 INFO === options_live_micro LIVE 2026-09-04T09:21:01.933448-04:00 share=25% ===
Live account equity $230.51 cash $160.84 #225458845 options_level=3
2026-09-04 09:21:02,173 INFO Live account equity $230.51 cash $160.84 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-04 09:21:02,246 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-04 09:21:02,318 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (160 earlier lines - see full log file)
| w1     |    4 |    3 |    8 |    2 |    4 |    3 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    32 |
| w2     |    6 |    5 |   11 |    6 |    6 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    48 |
| w3     |    8 |    6 |   13 |    5 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    56 |
| w4     |    6 |    4 |   10 |    3 |    5 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    43 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 233 | 10 |
| S164 | 249 | 11 |
| S165 | 1695 | 24 |
| S166 | 125 | 7 |
| S167 | 249 | 11 |
| S168 | 180 | 9 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-04
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   981 | WARN | <<<
| Missing exit records (post) |   981 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |    19 | INFO |
| Total closed lots           |  1967 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1010 med=+0.0% | TAINTED n=1772 med=-39.0% | KEEP-only n=554 med=+51.2% | KILL=16 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.51 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260904T132603Z

- UTC timestamp: `20260904T132603Z`
- GitHub run: [#9057](https://github.com/28twagg-ops/TradingBot/actions/runs/33877933750)
- Run id: `33877933750`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`12s`
- Full logs: `logs/action_runs/20260904T132603Z_live_bot.log`, `logs/action_runs/20260904T132603Z_live_options.log`, `logs/action_runs/20260904T132603Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1010 | 49.8 | +0.0 | +47.0 | $+15,267 |
| TAINTED | 1772 | 33.2 | -39.0 | +12.3 | $-9,135 |
| KEEP-only | 554 | 63.7 | +51.2 | +74.5 | $+10,136 |
| KEEP-only recent | 346 | 60.4 | +53.8 | +91.5 | $+4,879 |

- KEEP strategies (23): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S359, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (16): ORPHAN, S164, S203, S207, S211, S212, S216, S217, S351, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T09:26:09.324838-04:00","date":"2026-09-04","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.8,"phases_s":{"reconcile":0.15},"signals":0,"placed":0,"equity":1007263.09,"open_positions":15,"pending_orders":0,"open_lots":19,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9057","github_run_id":"33877933750","status":"ok","data_quality":{"clean":{"n":1010,"win":49.8,"med":0.0,"avg":46.97,"pnl":15267.13},"tainted":{"n":1772,"win":33.18,"med":-39.02,"avg":12.29,"pnl":-9135.34},"keep_only":{"n":554,"win":63.72,"med":51.18,"avg":74.54,"pnl":10136.45},"keep_only_recent":{"n":346,"win":60.4,"med":53.78,"avg":91.49,"pnl":4879.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S359","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S203","S207","S211","S212","S216","S217","S351","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:26:05  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.50|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $230.50|
|  Cash                                                           $160.84|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $69.66|
|  Open P&L                                                        $+0.52|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AMZN     Pullback50      $35.12     $255.49  $259.50  +1.6%   $+0.54  |
|  LII      MomReversal     $34.54     $386.29  $386.08  -0.1%   $-0.02  |
|                                                                        |
|  Total invested                                                  $69.66|
|  Total open P&L                                                  $+0.52|
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
|  2026-09-03  SELL  ACGL  Pullback50  $34.56  P&L $-0.00                |
|  2026-09-03  SELL  CNM  MomReversal  $34.27  P&L $-0.24                |
|  2026-09-03  SELL  ACGL  Pullback50  $34.60  P&L $+0.00                |
|  2026-09-03  SELL  AES  Pullback50  $34.50  P&L $+0.00                 |
|  2026-09-02  SELL  MO  Pullback50  $34.52  P&L $+0.00                  |
|  2026-09-02  SELL  AES  Pullback50  $34.50  P&L $-0.03                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-04T09:26:06.412626-04:00 share=25% ===
2026-09-04 09:26:06,412 INFO === options_live_micro LIVE 2026-09-04T09:26:06.412626-04:00 share=25% ===
Live account equity $230.50 cash $160.84 #225458845 options_level=3
2026-09-04 09:26:06,508 INFO Live account equity $230.50 cash $160.84 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-04 09:26:06,520 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-04 09:26:06,532 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (160 earlier lines - see full log file)
| w1     |    4 |    3 |    8 |    2 |    4 |    3 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    32 |
| w2     |    6 |    5 |   11 |    6 |    6 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    48 |
| w3     |    8 |    6 |   13 |    5 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    56 |
| w4     |    6 |    4 |   10 |    3 |    5 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    43 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 233 | 10 |
| S164 | 249 | 11 |
| S165 | 1695 | 24 |
| S166 | 125 | 7 |
| S167 | 249 | 11 |
| S168 | 180 | 9 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-04
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   981 | WARN | <<<
| Missing exit records (post) |   981 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |    19 | INFO |
| Total closed lots           |  1967 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1010 med=+0.0% | TAINTED n=1772 med=-39.0% | KEEP-only n=554 med=+51.2% | KILL=16 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.5 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260904T133632Z

- UTC timestamp: `20260904T133632Z`
- GitHub run: [#9059](https://github.com/28twagg-ops/TradingBot/actions/runs/33878873755)
- Run id: `33878873755`
- Live bot: exit=`0`, duration=`218s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260904T133632Z_live_bot.log`, `logs/action_runs/20260904T133632Z_live_options.log`, `logs/action_runs/20260904T133632Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1010 | 49.8 | +0.0 | +47.0 | $+15,267 |
| TAINTED | 1772 | 33.2 | -39.0 | +12.3 | $-9,135 |
| KEEP-only | 554 | 63.7 | +51.2 | +74.5 | $+10,136 |
| KEEP-only recent | 346 | 60.4 | +53.8 | +91.5 | $+4,879 |

- KEEP strategies (23): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S359, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (16): ORPHAN, S164, S203, S207, S211, S212, S216, S217, S351, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T09:26:09.324838-04:00","date":"2026-09-04","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.8,"phases_s":{"reconcile":0.15},"signals":0,"placed":0,"equity":1007263.09,"open_positions":15,"pending_orders":0,"open_lots":19,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9057","github_run_id":"33877933750","status":"ok","data_quality":{"clean":{"n":1010,"win":49.8,"med":0.0,"avg":46.97,"pnl":15267.13},"tainted":{"n":1772,"win":33.18,"med":-39.02,"avg":12.29,"pnl":-9135.34},"keep_only":{"n":554,"win":63.72,"med":51.18,"avg":74.54,"pnl":10136.45},"keep_only_recent":{"n":346,"win":60.4,"med":53.78,"avg":91.49,"pnl":4879.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S359","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S203","S207","S211","S212","S216","S217","S351","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:36:33  INFO      Mode: morning_prep
13:36:35  INFO        [prep_positions] 2/2 (2 valid)
13:36:35  INFO      Fetching tickers (universe=both)...
13:36:35  INFO        S&P 500: 503
13:36:35  INFO        MidCap 400: 400
13:36:35  INFO        Total: 903 tickers
13:36:36  INFO        [prep_universe] 40/901 (40 valid)
13:36:38  INFO        [prep_universe] 80/901 (80 valid)
13:36:39  INFO        [prep_universe] 120/901 (120 valid)
13:36:41  INFO        [prep_universe] 160/901 (160 valid)
13:36:42  INFO        [prep_universe] 200/901 (199 valid)
13:36:49  INFO        [prep_universe] 240/901 (238 valid)
13:37:00  INFO        [prep_universe] 280/901 (278 valid)
13:37:13  INFO        [prep_universe] 320/901 (318 valid)
13:37:27  INFO        [prep_universe] 360/901 (358 valid)
13:37:37  INFO        [prep_universe] 400/901 (397 valid)
13:37:51  INFO        [prep_universe] 440/901 (437 valid)
13:38:01  INFO        [prep_universe] 480/901 (477 valid)
13:38:15  INFO        [prep_universe] 520/901 (517 valid)
13:38:25  INFO        [prep_universe] 560/901 (557 valid)
13:38:38  INFO        [prep_universe] 600/901 (597 valid)
13:38:49  INFO        [prep_universe] 640/901 (637 valid)
13:39:02  INFO        [prep_universe] 680/901 (677 valid)
13:39:13  INFO        [prep_universe] 720/901 (717 valid)
13:39:26  INFO        [prep_universe] 760/901 (757 valid)
13:39:37  INFO        [prep_universe] 800/901 (797 valid)
13:39:50  INFO        [prep_universe] 840/901 (837 valid)
13:40:00  INFO        [prep_universe] 880/901 (877 valid)
13:40:07  INFO        [prep_universe] 901/901 (898 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.75|
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
|  Invested                                                        $69.91|
|  Open P&L                                                        $+0.77|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AMZN     Pullback50      $35.11     $255.49  $259.42  +1.5%   $+0.53  |
|  LII      MomReversal     $34.80     $386.29  $388.95  +0.7%   $+0.24  |
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
|  Signal candidates                                                   54|
|  Universe scanned                                                   901|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-04T09:40:11.314197-04:00 share=25% ===
2026-09-04 09:40:11,314 INFO === options_live_micro LIVE 2026-09-04T09:40:11.314197-04:00 share=25% ===
Live account equity $230.61 cash $160.84 #225458845 options_level=3
2026-09-04 09:40:11,564 INFO Live account equity $230.61 cash $160.84 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-04 09:40:11,833 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-04 09:40:11,988 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=19 paper_keys=yes dry_run=False
  alpaca positions=16
  FLAG b316|S355|d7e1a5e1 missing from Alpaca
  FLAG b96|S211|837bd36f missing from Alpaca
  FLAG b99|S211|32be36ec missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$1,006,733.22
  buying_power=$3,994,580.88 cash=$1,004,695.22
  open option orders: 11
    AVGO260909C00372500 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
    AVGO260904C00367500 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
    AVGO260909C00375000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
    AVGO260904C00357500 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
    NVDA260904C00227500 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
  open option positions: 16
    AVGO260909C00380000 qty=3 mkt=$183.00
    AVGO260911C00385000 qty=1 mkt=$86.00
    BA260904C00210000 qty=2 mkt=$142.00
    BA260904C00215000 qty=-1 mkt=$-4.00
    BA260904C00217500 qty=-1 mkt=$-3.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-04T09:40:15.227053-04:00 ===

[Run context]
Paper auth OK — equity $1006767.22, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
  EXIT [b85|lab0085_s210_w3_1045_1120_r2|S210] take_profit (+728.0%) SELL failed NVDA260904C00232500: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b84|lab0084_s210_w3_1045_1120_r1|S210] take_profit (+728.0%) SELL failed NVDA260904C00232500: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b1112|lab1112_s166_w3_1045_1120_r1|S166] take_profit (+64.9%) SELL failed AVGO260909C00380000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b1127|lab1127_s168_w3_1045_1120_r2|S168] take_profit (+64.9%) SELL failed AVGO260909C00380000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b1126|lab1126_s168_w3_1045_1120_r1|S168] take_profit (+64.9%) SELL failed AVGO260909C00380000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b439|lab0439_s366_w4_1120_1135_r2|S366] take_profit (+92.5%) SELL failed MARA260925C00011000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b438|lab0438_s366_w4_1120_1135_r1|S366] take_profit (+92.5%) SELL failed MARA260925C00011000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
2026-09-04 09:40:25,016 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-48.7%) SELL 1 TSLA260904C00375000 @<= 0.17
  EXIT [b293|lab0293_s352_w3_1045_1120_r2|S352] take_profit (+471.4%) SELL failed MARA260904C00011000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b292|lab0292_s352_w3_1045_1120_r1|S352] take_profit (+471.4%) SELL failed MARA260904C00011000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
Protective stops: placed=3 upgraded=0 already=2 failed=7 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
```

---

## Run 20260904T134211Z

- UTC timestamp: `20260904T134211Z`
- GitHub run: [#9060](https://github.com/28twagg-ops/TradingBot/actions/runs/33879337569)
- Run id: `33879337569`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260904T134211Z_live_bot.log`, `logs/action_runs/20260904T134211Z_live_options.log`, `logs/action_runs/20260904T134211Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1010 | 49.8 | +0.0 | +47.0 | $+15,267 |
| TAINTED | 1772 | 33.2 | -39.0 | +12.3 | $-9,135 |
| KEEP-only | 554 | 63.7 | +51.2 | +74.5 | $+10,136 |
| KEEP-only recent | 346 | 60.4 | +53.8 | +91.5 | $+4,879 |

- KEEP strategies (23): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S359, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (16): ORPHAN, S164, S203, S207, S211, S212, S216, S217, S351, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T09:26:09.324838-04:00","date":"2026-09-04","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.8,"phases_s":{"reconcile":0.15},"signals":0,"placed":0,"equity":1007263.09,"open_positions":15,"pending_orders":0,"open_lots":19,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9057","github_run_id":"33877933750","status":"ok","data_quality":{"clean":{"n":1010,"win":49.8,"med":0.0,"avg":46.97,"pnl":15267.13},"tainted":{"n":1772,"win":33.18,"med":-39.02,"avg":12.29,"pnl":-9135.34},"keep_only":{"n":554,"win":63.72,"med":51.18,"avg":74.54,"pnl":10136.45},"keep_only_recent":{"n":346,"win":60.4,"med":53.78,"avg":91.49,"pnl":4879.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S359","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S203","S207","S211","S212","S216","S217","S351","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:42:12  INFO      Mode: morning_prep
13:42:13  INFO        [prep_positions] 2/2 (2 valid)
13:42:13  INFO      Fetching tickers (universe=both)...
13:42:13  INFO        S&P 500: 503
13:42:13  INFO        MidCap 400: 400
13:42:13  INFO        Total: 903 tickers
13:42:14  INFO        [prep_universe] 40/901 (40 valid)
13:42:16  INFO        [prep_universe] 80/901 (80 valid)
13:42:17  INFO        [prep_universe] 120/901 (120 valid)
13:42:18  INFO        [prep_universe] 160/901 (160 valid)
13:42:20  INFO        [prep_universe] 200/901 (199 valid)
13:42:27  INFO        [prep_universe] 240/901 (238 valid)
13:42:40  INFO        [prep_universe] 280/901 (278 valid)
13:42:50  INFO        [prep_universe] 320/901 (318 valid)
13:43:03  INFO        [prep_universe] 360/901 (358 valid)
13:43:16  INFO        [prep_universe] 400/901 (397 valid)
13:43:26  INFO        [prep_universe] 440/901 (437 valid)
13:43:39  INFO        [prep_universe] 480/901 (477 valid)
13:43:49  INFO        [prep_universe] 520/901 (517 valid)
13:44:02  INFO        [prep_universe] 560/901 (557 valid)
13:44:15  INFO        [prep_universe] 600/901 (597 valid)
13:44:26  INFO        [prep_universe] 640/901 (637 valid)
13:44:39  INFO        [prep_universe] 680/901 (677 valid)
13:44:52  INFO        [prep_universe] 720/901 (717 valid)
13:45:02  INFO        [prep_universe] 760/901 (757 valid)
13:45:15  INFO        [prep_universe] 800/901 (797 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20260904T134627Z

- UTC timestamp: `20260904T134627Z`
- GitHub run: [#9061](https://github.com/28twagg-ops/TradingBot/actions/runs/33879795145)
- Run id: `33879795145`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260904T134627Z_live_bot.log`, `logs/action_runs/20260904T134627Z_live_options.log`, `logs/action_runs/20260904T134627Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1010 | 49.8 | +0.0 | +47.0 | $+15,267 |
| TAINTED | 1772 | 33.2 | -39.0 | +12.3 | $-9,135 |
| KEEP-only | 554 | 63.7 | +51.2 | +74.5 | $+10,136 |
| KEEP-only recent | 346 | 60.4 | +53.8 | +91.5 | $+4,879 |

- KEEP strategies (23): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S359, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (16): ORPHAN, S164, S203, S207, S211, S212, S216, S217, S351, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T09:26:09.324838-04:00","date":"2026-09-04","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.8,"phases_s":{"reconcile":0.15},"signals":0,"placed":0,"equity":1007263.09,"open_positions":15,"pending_orders":0,"open_lots":19,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9057","github_run_id":"33877933750","status":"ok","data_quality":{"clean":{"n":1010,"win":49.8,"med":0.0,"avg":46.97,"pnl":15267.13},"tainted":{"n":1772,"win":33.18,"med":-39.02,"avg":12.29,"pnl":-9135.34},"keep_only":{"n":554,"win":63.72,"med":51.18,"avg":74.54,"pnl":10136.45},"keep_only_recent":{"n":346,"win":60.4,"med":53.78,"avg":91.49,"pnl":4879.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S359","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S203","S207","S211","S212","S216","S217","S351","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
... (207 earlier lines - see full log file)
|    SKIP [eq] MTD  Pullback50                                      cap 3|
|    SKIP [eq] MDLZ  Pullback50                                     cap 3|
|    SKIP [eq] MS  Pullback50                                       cap 3|
|    SKIP [eq] ROST  Pullback50                                     cap 3|
|    SKIP [eq] SBUX  Pullback50                                     cap 3|
|    SKIP [eq] TFC  Pullback50                                      cap 3|
|    SKIP [eq] USB  Pullback50                                      cap 3|
|    SKIP [eq] UNP  Pullback50                                      cap 3|
|    SKIP [eq] GWW  Pullback50                                      cap 3|
|    SKIP [eq] WAB  Pullback50                                      cap 3|
|    SKIP [eq] WMB  Pullback50                                      cap 3|
|    SKIP [eq] AHR  Pullback50                                      cap 3|
|    SKIP [eq] AM  Pullback50                                       cap 3|
|    SKIP [eq] AMG  Pullback50                                      cap 3|
|    SKIP [eq] ARMK  Pullback50                                     cap 3|
|    SKIP [eq] ASB  Pullback50                                      cap 3|
|    SKIP [eq] BKH  Pullback50                                      cap 3|
|    SKIP [eq] CBSH  Pullback50                                     cap 3|
|    SKIP [eq] CCK  Pullback50                                      cap 3|
|    SKIP [eq] CFR  Pullback50                                      cap 3|
|    SKIP [eq] EPR  Pullback50                                      cap 3|
|    SKIP [eq] EWBC  Pullback50                                     cap 3|
|    SKIP [eq] FHI  Pullback50                                      cap 3|
|    SKIP [eq] HOMB  Pullback50                                     cap 3|
|    SKIP [eq] JAZZ  Pullback50                                     cap 3|
|    SKIP [eq] LEA  Pullback50                                      cap 3|
|    SKIP [eq] LIVN  Pullback50                                     cap 3|
|    SKIP [eq] LFUS  Pullback50                                     cap 3|
|    SKIP [eq] NLY  Pullback50                                      cap 3|
|    SKIP [eq] NVT  Pullback50                                      cap 3|
|    SKIP [eq] NWE  Pullback50                                      cap 3|
|    SKIP [eq] ORI  Pullback50                                      cap 3|
|    SKIP [eq] OZK  Pullback50                                      cap 3|
|    SKIP [eq] PNFP  Pullback50                                     cap 3|
|    SKIP [eq] RS  Pullback50                                       cap 3|
|    SKIP [eq] SCI  Pullback50                                      cap 3|
|    SKIP [eq] SIRI  Pullback50                                     cap 3|
|    SKIP [eq] SITM  Pullback50                                     cap 3|
|    SKIP [eq] SLM  Pullback50                                      cap 3|
|    SKIP [eq] UBSI  Pullback50                                     cap 3|
|    SKIP [eq] UMBF  Pullback50                                     cap 3|
|    SKIP [eq] WTS  Pullback50                                      cap 3|
|    SKIP [eq] ZION  Pullback50                                     cap 3|

+========================================================================+
|                         BUY FILL CONFIRMATION                          |
+========================================================================+
|  Pending submits                                                      1|
+------------------------------------------------------------------------+
|  APD                                                  still unconfirmed|
+========================================================================+
+========================================================================+13:50:18  INFO        place_all_stops: checking 3 positions...
13:50:18  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
13:50:18  INFO        STOP skipped APD: fractional (0.1144 shares) — software exit will handle it
13:50:18  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
13:50:18  INFO        Daily log -> logs/daily/2026-09-04.md
13:50:18  INFO        Dashboard written → logs/dashboard.md


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
|  Scanned                                                            898|
|  Signals                                                             62|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  1 unconfirmed|
|  Exits                                                                0|
|  Open pos                                                             3|
|  Equity                                                         $230.38|
|  Cash                                                           $126.25|
+========================================================================+
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---
