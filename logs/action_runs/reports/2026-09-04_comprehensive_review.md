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

## Run 20260904T135126Z

- UTC timestamp: `20260904T135126Z`
- GitHub run: [#9062](https://github.com/28twagg-ops/TradingBot/actions/runs/33880255123)
- Run id: `33880255123`
- Live bot: exit=`0`, duration=`216s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260904T135126Z_live_bot.log`, `logs/action_runs/20260904T135126Z_live_options.log`, `logs/action_runs/20260904T135126Z_options_bot.log`


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
... (126 earlier lines - see full log file)
|  CI       Pullback50      eq     $283.53  61.2   -2.84   50MA bounce (+|
|  CFG      Pullback50      eq     $70.91   34.9   -2.31   50MA bounce (-|
|  DLR      Pullback50      eq     $188.29  35.7   -1.56   50MA bounce (+|
|  ECL      Pullback50      eq     $278.30  53.3   -2.18   50MA bounce (-|
|  EQIX     Pullback50      eq     $1041.~  33.0   -2.65   50MA bounce (-|
|  FTNT     Pullback50      eq     $157.57  51.3   -2.68   50MA bounce (-|
|  IBKR     Pullback50      eq     $92.15   46.5   -2.45   50MA bounce (+|
|  JCI      Pullback50      eq     $143.94  31.1   -2.83   50MA bounce (-|
|  KEYS     Pullback50      eq     $328.01  30.8   -1.45   50MA bounce (+|
|  MDLZ     Pullback50      eq     $61.29   44.2   -3.22   50MA bounce (-|
|  MS       Pullback50      eq     $216.50  47.5   -3.57   50MA bounce (+|
|  QCOM     Pullback50      eq     $170.16  63.1   -2.71   50MA bounce (+|
|  ROST     Pullback50      eq     $232.31  46.1   -1.76   50MA bounce (-|
|  STX      Pullback50      eq     $847.79  30.9   -2.36   50MA bounce (-|
|  SBUX     Pullback50      eq     $105.96  44.2   -3.09   50MA bounce (+|
|  TFC      Pullback50      eq     $51.52   43.3   -3.41   50MA bounce (-|
|  USB      Pullback50      eq     $63.49   41.6   -2.98   50MA bounce (+|
|  UNP      Pullback50      eq     $290.93  37.8   -2.78   50MA bounce (-|
|  VTRS     Pullback50      eq     $16.85   62.1   -2.18   50MA bounce (+|
|  WAB      Pullback50      eq     $282.22  27.7   -2.55   50MA bounce (-|13:55:02  INFO        place_all_stops: checking 3 positions...
13:55:02  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
13:55:02  INFO        STOP skipped APD: fractional (0.1144 shares) — software exit will handle it
13:55:02  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
13:55:02  INFO        Daily log -> logs/daily/2026-09-04.md
13:55:02  INFO        Dashboard written → logs/dashboard.md

|  WMB      Pullback50      eq     $74.08   52.3   -1.63   50MA bounce (+|
|  AM       Pullback50      eq     $22.31   52.9   -1.76   50MA bounce (-|
|  AHR      Pullback50      eq     $55.58   56.2   -1.40   50MA bounce (+|
|  AMG      Pullback50      eq     $365.11  45.0   -2.63   50MA bounce (+|
|  ASB      Pullback50      eq     $31.01   36.4   -2.44   50MA bounce (-|
|  BKH      Pullback50      eq     $73.32   49.6   -2.79   50MA bounce (-|
|  CFR      Pullback50      eq     $163.25  34.9   -3.17   50MA bounce (+|
|  CXT      Pullback50      eq     $50.63   51.4   -2.87   50MA bounce (-|
|  EPR      Pullback50      eq     $60.65   51.3   -2.66   50MA bounce (-|
|  EWBC     Pullback50      eq     $130.62  34.5   -2.86   50MA bounce (-|
|  FHI      Pullback50      eq     $61.42   36.7   -2.99   50MA bounce (+|
|  HOMB     Pullback50      eq     $30.06   33.2   -3.13   50MA bounce (-|
|  JAZZ     Pullback50      eq     $248.30  49.9   -0.97   50MA bounce (-|
|  LFUS     Pullback50      eq     $423.92  31.3   -2.32   50MA bounce (-|
|  LIVN     Pullback50      eq     $81.04   48.3   -2.81   50MA bounce (+|
|  LEA      Pullback50      eq     $132.27  66.5   -2.57   50MA bounce (+|
|  NOVT     Pullback50      eq     $149.79  30.9   -2.95   50MA bounce (-|
|  NWE      Pullback50      eq     $70.91   50.6   -2.82   50MA bounce (-|
|  NLY      Pullback50      eq     $22.80   37.7   -2.80   50MA bounce (-|
|  ORI      Pullback50      eq     $41.92   42.7   -2.91   50MA bounce (-|
|  OZK      Pullback50      eq     $50.35   43.1   -2.98   50MA bounce (-|
|  PNFP     Pullback50      eq     $101.51  33.6   -3.00   50MA bounce (-|
|  RS       Pullback50      eq     $398.85  34.8   -1.89   50MA bounce (+|
|  SCI      Pullback50      eq     $81.85   46.7   -3.78   50MA bounce (+|
|  SLM      Pullback50      eq     $26.21   38.4   -2.50   50MA bounce (+|
|  UMBF     Pullback50      eq     $143.87  32.0   -2.67   50MA bounce (-|
|  UBSI     Pullback50      eq     $47.72   35.4   -3.11   50MA bounce (+|
|  USFD     Pullback50      eq     $104.08  33.3   -2.66   50MA bounce (+|
|  WTS      Pullback50      eq     $360.42  31.4   -3.04   50MA bounce (-|
|  ZION     Pullback50      eq     $69.35   39.1   -2.73   50MA bounce (-|
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
|  Scanned                                                            897|
|  Signals                                                             56|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  0 unconfirmed|
|  Exits                                                                0|
|  Open pos                                                             3|
|  Equity                                                         $230.62|
|  Cash                                                           $126.25|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-04T09:55:03.299904-04:00 share=25% ===
2026-09-04 09:55:03,299 INFO === options_live_micro LIVE 2026-09-04T09:55:03.299904-04:00 share=25% ===
Live account equity $230.62 cash $126.25 #225458845 options_level=3
2026-09-04 09:55:03,342 INFO Live account equity $230.62 cash $126.25 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-04 09:55:03,380 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-04 09:55:03,395 INFO Live micro done. open_options=0 lots=0
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
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$1,006,838.20
  buying_power=$3,994,648.80 cash=$1,004,712.20
  open option orders: 14
    TSLA260909C00387500 OrderSide.SELL qty=12 status=OrderStatus.NEW limit=None
    TSLA260909C00390000 OrderSide.SELL qty=4 status=OrderStatus.NEW limit=None
    TSLA260909C00385000 OrderSide.SELL qty=5 status=OrderStatus.NEW limit=None
    AVGO260909C00372500 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
    AVGO260904C00367500 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
  open option positions: 16
    AVGO260909C00380000 qty=3 mkt=$180.00
    AVGO260911C00385000 qty=1 mkt=$92.00
    BA260904C00210000 qty=2 mkt=$144.00
    BA260904C00215000 qty=-1 mkt=$-4.00
    BA260904C00217500 qty=-1 mkt=$-3.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-04T09:55:06.281437-04:00 ===

[Run context]
Paper auth OK — equity $1006836.20, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
2026-09-04 09:55:08,420 INFO   EXIT [b281|lab0281_s351_w1_0928_1005_r2|S351] stop_loss (-58.3%) SELL 1 TSLA260904C00375000 @<= 0.14
  EXIT [b439|lab0439_s366_w4_1120_1135_r2|S366] take_profit (+100.0%) SELL failed MARA260925C00011000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b438|lab0438_s366_w4_1120_1135_r1|S366] take_profit (+100.0%) SELL failed MARA260925C00011000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b85|lab0085_s210_w3_1045_1120_r2|S210] take_profit (+920.0%) SELL failed NVDA260904C00232500: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b84|lab0084_s210_w3_1045_1120_r1|S210] take_profit (+920.0%) SELL failed NVDA260904C00232500: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b1112|lab1112_s166_w3_1045_1120_r1|S166] take_profit (+62.2%) SELL failed AVGO260909C00380000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b1127|lab1127_s168_w3_1045_1120_r2|S168] take_profit (+62.2%) SELL failed AVGO260909C00380000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b1126|lab1126_s168_w3_1045_1120_r1|S168] take_profit (+62.2%) SELL failed AVGO260909C00380000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b293|lab0293_s352_w3_1045_1120_r2|S352] take_profit (+500.0%) SELL failed MARA260904C00011000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b292|lab0292_s352_w3_1045_1120_r1|S352] take_profit (+500.0%) SELL failed MARA260904C00011000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
Protective stops: placed=0 upgraded=0 already=5 failed=7 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
```

---

## Run 20260904T135633Z

- UTC timestamp: `20260904T135633Z`
- GitHub run: [#9063](https://github.com/28twagg-ops/TradingBot/actions/runs/33880720569)
- Run id: `33880720569`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`126s`
- Full logs: `logs/action_runs/20260904T135633Z_live_bot.log`, `logs/action_runs/20260904T135633Z_live_options.log`, `logs/action_runs/20260904T135633Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1011 | 49.8 | +0.0 | +46.9 | $+15,253 |
| TAINTED | 1780 | 33.4 | -38.6 | +12.8 | $-8,751 |
| KEEP-only | 554 | 63.7 | +51.2 | +74.5 | $+10,136 |
| KEEP-only recent | 346 | 60.4 | +53.8 | +91.5 | $+4,879 |

- KEEP strategies (23): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S359, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (16): ORPHAN, S164, S203, S207, S211, S212, S216, S217, S351, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T09:56:39.529666-04:00","date":"2026-09-04","mode":"entry+manage","header":"entry+manage (39 new)","elapsed_s":114.9,"phases_s":{"reconcile":0.3,"cancel":0.03,"manage":3.75,"protective_stops":0.74,"scan":46.43,"entries":42.57,"reconcile2":1.48},"signals":308,"placed":39,"equity":1006940.18,"open_positions":24,"pending_orders":10,"open_lots":69,"submitted_today":39,"filled_today":56,"unattributed_contracts":0,"top_signals":["S165:TSLA","S164:TSLA","S168:TSLA","S167:TSLA","S166:TSLA","S163:TSLA","S350:TSLA","S351:TSLA"],"github_run":"9063","github_run_id":"33880720569","status":"ok","data_quality":{"clean":{"n":1011,"win":49.75,"med":0.0,"avg":46.88,"pnl":15252.96},"tainted":{"n":1780,"win":33.43,"med":-38.59,"avg":12.77,"pnl":-8750.84},"keep_only":{"n":554,"win":63.72,"med":51.18,"avg":74.54,"pnl":10136.45},"keep_only_recent":{"n":346,"win":60.4,"med":53.78,"avg":91.49,"pnl":4879.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S359","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S203","S207","S211","S212","S216","S217","S351","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:56:34  INFO      Mode: morning_scan
13:56:34  INFO      Morning scan already completed today (2026-09-04T13:50:18.126124Z) — exits-only pass
13:56:34  INFO        place_all_stops: checking 3 positions...
13:56:34  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
13:56:34  INFO        STOP skipped APD: fractional (0.1144 shares) — software exit will handle it
13:56:34  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
13:56:35  INFO        [positions] 3/3 (3 valid)
13:56:35  INFO        Daily log -> logs/daily/2026-09-04.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_SCAN|
|  Time                                                         13:56 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.49|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  APD  P&L -0.1%  $-0.04                                            HOLD|
|  LII  P&L +0.6%  $+0.21                                            HOLD|
|  AMZN  P&L +1.0%  $+0.36                                           HOLD|
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
=== options_live_micro LIVE 2026-09-04T09:56:36.176291-04:00 share=25% ===
2026-09-04 09:56:36,176 INFO === options_live_micro LIVE 2026-09-04T09:56:36.176291-04:00 share=25% ===
Live account equity $230.49 cash $126.25 #225458845 options_level=3
2026-09-04 09:56:36,235 INFO Live account equity $230.49 cash $126.25 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-04 09:56:36,528 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-04 09:56:36,557 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (192 earlier lines - see full log file)
| w2     |    6 |    5 |   11 |    6 |    6 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    48 |
| w3     |    8 |    6 |   13 |    5 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    56 |
| w4     |    6 |    4 |   10 |    3 |    5 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    43 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 237 | 11 |
| S164 | 249 | 11 |
| S165 | 1695 | 24 |
| S166 | 129 | 8 |
| S167 | 249 | 11 |
| S168 | 182 | 10 |
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
| 2026-09-04 |    4 |    0 |    0 |    4 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |

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
| State/ledger mismatches     |     3 | WARN | <<<
| Total open lots             |    69 | INFO |
| Total closed lots           |  1973 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1011 med=+0.0% | TAINTED n=1780 med=-38.6% | KEEP-only n=554 med=+51.2% | KILL=16 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.49 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260904T140110Z

- UTC timestamp: `20260904T140110Z`
- GitHub run: [#9064](https://github.com/28twagg-ops/TradingBot/actions/runs/33881189776)
- Run id: `33881189776`
- Live bot: exit=`0`, duration=`5s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`105s`
- Full logs: `logs/action_runs/20260904T140110Z_live_bot.log`, `logs/action_runs/20260904T140110Z_live_options.log`, `logs/action_runs/20260904T140110Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1013 | 49.9 | +0.0 | +47.4 | $+15,342 |
| TAINTED | 1781 | 33.4 | -38.4 | +12.7 | $-8,763 |
| KEEP-only | 555 | 63.8 | +51.4 | +75.3 | $+10,171 |
| KEEP-only recent | 347 | 60.5 | +54.0 | +92.7 | $+4,914 |

- KEEP strategies (23): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S359, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (16): ORPHAN, S164, S203, S207, S211, S212, S216, S217, S351, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T10:01:19.512937-04:00","date":"2026-09-04","mode":"entry+manage","header":"entry+manage (4 new)","elapsed_s":93.7,"phases_s":{"reconcile":1.24,"cancel":0.12,"manage":9.13,"protective_stops":3.56,"scan":52.87,"entries":21.94,"reconcile2":0.72},"signals":308,"placed":4,"equity":1006746.09,"open_positions":26,"pending_orders":4,"open_lots":73,"submitted_today":43,"filled_today":66,"unattributed_contracts":0,"top_signals":["S165:TSLA","S164:TSLA","S168:TSLA","S167:TSLA","S166:TSLA","S163:TSLA","S350:TSLA","S351:TSLA"],"github_run":"9064","github_run_id":"33881189776","status":"ok","data_quality":{"clean":{"n":1013,"win":49.85,"med":0.0,"avg":47.38,"pnl":15341.96},"tainted":{"n":1781,"win":33.41,"med":-38.36,"avg":12.74,"pnl":-8762.84},"keep_only":{"n":555,"win":63.78,"med":51.39,"avg":75.31,"pnl":10171.45},"keep_only_recent":{"n":347,"win":60.52,"med":54.0,"avg":92.66,"pnl":4914.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S359","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S203","S207","S211","S212","S216","S217","S351","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
14:01:13  INFO      Mode: exits
14:01:13  INFO        place_all_stops: checking 3 positions...
14:01:13  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
14:01:13  INFO        STOP skipped APD: fractional (0.1144 shares) — software exit will handle it
14:01:13  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
14:01:14  INFO        [positions] 3/3 (3 valid)
14:01:14  INFO        Daily log -> logs/daily/2026-09-04.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.33|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  APD  P&L -0.0%  $-0.00                                            HOLD|
|  LII  P&L +0.0%  $+0.01                                            HOLD|
|  AMZN  P&L +1.0%  $+0.35                                           HOLD|
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
=== options_live_micro LIVE 2026-09-04T10:01:15.748390-04:00 share=25% ===
2026-09-04 10:01:15,748 INFO === options_live_micro LIVE 2026-09-04T10:01:15.748390-04:00 share=25% ===
Live account equity $230.31 cash $126.25 #225458845 options_level=3
2026-09-04 10:01:15,954 INFO Live account equity $230.31 cash $126.25 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-04 10:01:16,163 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-04 10:01:16,325 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (191 earlier lines - see full log file)
| w2     |    6 |    5 |   11 |    6 |    6 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    48 |
| w3     |    8 |    6 |   13 |    5 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    56 |
| w4     |    6 |    4 |   10 |    3 |    5 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    43 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 237 | 11 |
| S164 | 253 | 12 |
| S165 | 1695 | 24 |
| S166 | 129 | 8 |
| S167 | 249 | 11 |
| S168 | 182 | 10 |
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
| 2026-09-04 |    4 |    4 |    0 |    4 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    14 |

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
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    73 | INFO |
| Total closed lots           |  1976 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1013 med=+0.0% | TAINTED n=1781 med=-38.4% | KEEP-only n=555 med=+51.4% | KILL=16 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.33 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260904T140558Z

- UTC timestamp: `20260904T140558Z`
- GitHub run: [#9065](https://github.com/28twagg-ops/TradingBot/actions/runs/33881678857)
- Run id: `33881678857`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`202s`
- Full logs: `logs/action_runs/20260904T140558Z_live_bot.log`, `logs/action_runs/20260904T140558Z_live_options.log`, `logs/action_runs/20260904T140558Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1014 | 49.9 | +0.0 | +47.8 | $+15,375 |
| TAINTED | 1783 | 33.5 | -38.4 | +12.8 | $-8,664 |
| KEEP-only | 556 | 63.8 | +51.5 | +76.0 | $+10,204 |
| KEEP-only recent | 348 | 60.6 | +54.1 | +93.8 | $+4,947 |

- KEEP strategies (23): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S359, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (16): ORPHAN, S164, S203, S207, S211, S212, S216, S217, S351, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T10:06:05.768170-04:00","date":"2026-09-04","mode":"entry+manage","header":"entry+manage (44 new)","elapsed_s":191.4,"phases_s":{"reconcile":0.43,"cancel":0.13,"manage":8.76,"protective_stops":3.24,"scan":47.52,"entries":106.02,"reconcile2":4.74},"signals":308,"placed":44,"equity":1006651.85,"open_positions":34,"pending_orders":14,"open_lots":104,"submitted_today":87,"filled_today":100,"unattributed_contracts":0,"top_signals":["S165:TSLA","S164:TSLA","S168:TSLA","S167:TSLA","S166:TSLA","S163:TSLA","S350:TSLA","S351:TSLA"],"github_run":"9065","github_run_id":"33881678857","status":"ok","data_quality":{"clean":{"n":1014,"win":49.9,"med":0.0,"avg":47.8,"pnl":15374.96},"tainted":{"n":1783,"win":33.48,"med":-38.36,"avg":12.81,"pnl":-8663.84},"keep_only":{"n":556,"win":63.85,"med":51.48,"avg":76.02,"pnl":10204.45},"keep_only_recent":{"n":348,"win":60.63,"med":54.12,"avg":93.75,"pnl":4947.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S359","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S203","S207","S211","S212","S216","S217","S351","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
14:05:59  INFO      Mode: exits
14:06:00  INFO        place_all_stops: checking 3 positions...
14:06:00  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
14:06:00  INFO        STOP skipped APD: fractional (0.1144 shares) — software exit will handle it
14:06:00  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
14:06:01  INFO        [positions] 3/3 (3 valid)
14:06:01  INFO        Daily log -> logs/daily/2026-09-04.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.47|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  LII  P&L +0.1%  $+0.02                                            HOLD|
|  APD  P&L +0.2%  $+0.08                                            HOLD|
|  AMZN  P&L +1.2%  $+0.40                                           HOLD|
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
=== options_live_micro LIVE 2026-09-04T10:06:02.115883-04:00 share=25% ===
2026-09-04 10:06:02,115 INFO === options_live_micro LIVE 2026-09-04T10:06:02.115883-04:00 share=25% ===
Live account equity $230.47 cash $126.25 #225458845 options_level=3
2026-09-04 10:06:02,314 INFO Live account equity $230.47 cash $126.25 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-04 10:06:02,494 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-04 10:06:02,623 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (224 earlier lines - see full log file)
| w2     |    7 |    6 |   12 |    7 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    54 |
| w3     |    8 |    6 |   13 |    5 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    56 |
| w4     |    6 |    4 |   10 |    3 |    5 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    43 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 241 | 12 |
| S164 | 257 | 13 |
| S165 | 1699 | 25 |
| S166 | 133 | 9 |
| S167 | 253 | 12 |
| S168 | 184 | 11 |
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
| 2026-09-04 |    8 |    8 |    4 |    8 |    4 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |

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
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |   104 | INFO |
| Total closed lots           |  1979 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1014 med=+0.0% | TAINTED n=1783 med=-38.4% | KEEP-only n=556 med=+51.5% | KILL=16 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.48 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260904T141057Z

- UTC timestamp: `20260904T141057Z`
- GitHub run: [#9066](https://github.com/28twagg-ops/TradingBot/actions/runs/33882159411)
- Run id: `33882159411`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`122s`
- Full logs: `logs/action_runs/20260904T141057Z_live_bot.log`, `logs/action_runs/20260904T141057Z_live_options.log`, `logs/action_runs/20260904T141057Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1015 | 50.0 | +0.0 | +47.8 | $+15,425 |
| TAINTED | 1783 | 33.5 | -38.4 | +12.8 | $-8,664 |
| KEEP-only | 556 | 63.8 | +51.5 | +76.0 | $+10,204 |
| KEEP-only recent | 348 | 60.6 | +54.1 | +93.8 | $+4,947 |

- KEEP strategies (23): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S359, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (16): ORPHAN, S164, S203, S207, S211, S212, S216, S217, S351, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T10:11:02.860510-04:00","date":"2026-09-04","mode":"entry+manage","header":"entry+manage (3 new)","elapsed_s":110.9,"phases_s":{"reconcile":0.84,"cancel":0.03,"manage":7.28,"protective_stops":0.67,"scan":45.99,"entries":36.5,"reconcile2":0.33},"signals":308,"placed":3,"equity":1006183.58,"open_positions":35,"pending_orders":9,"open_lots":111,"submitted_today":90,"filled_today":108,"unattributed_contracts":0,"top_signals":["S165:TSLA","S164:TSLA","S168:TSLA","S167:TSLA","S166:TSLA","S163:TSLA","S350:TSLA","S351:TSLA"],"github_run":"9066","github_run_id":"33882159411","status":"ok","data_quality":{"clean":{"n":1015,"win":49.95,"med":0.0,"avg":47.84,"pnl":15424.96},"tainted":{"n":1783,"win":33.48,"med":-38.36,"avg":12.81,"pnl":-8663.84},"keep_only":{"n":556,"win":63.85,"med":51.48,"avg":76.02,"pnl":10204.45},"keep_only_recent":{"n":348,"win":60.63,"med":54.12,"avg":93.75,"pnl":4947.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S359","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S203","S207","S211","S212","S216","S217","S351","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
14:10:58  INFO      Mode: exits
14:10:59  INFO        place_all_stops: checking 3 positions...
14:10:59  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
14:10:59  INFO        STOP skipped APD: fractional (0.1144 shares) — software exit will handle it
14:10:59  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
14:10:59  INFO        [positions] 3/3 (3 valid)
14:10:59  INFO        Daily log -> logs/daily/2026-09-04.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.42|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  LII  P&L +0.1%  $+0.03                                            HOLD|
|  APD  P&L +0.3%  $+0.10                                            HOLD|
|  AMZN  P&L +0.9%  $+0.33                                           HOLD|
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
=== options_live_micro LIVE 2026-09-04T10:11:00.211100-04:00 share=25% ===
2026-09-04 10:11:00,211 INFO === options_live_micro LIVE 2026-09-04T10:11:00.211100-04:00 share=25% ===
Live account equity $230.42 cash $126.25 #225458845 options_level=3
2026-09-04 10:11:00,262 INFO Live account equity $230.42 cash $126.25 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-04 10:11:00,290 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-04 10:11:00,308 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (198 earlier lines - see full log file)
| w2     |    7 |    6 |   12 |    7 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    54 |
| w3     |    8 |    6 |   13 |    5 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    56 |
| w4     |    6 |    4 |   10 |    3 |    5 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    43 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 241 | 12 |
| S164 | 257 | 13 |
| S165 | 1699 | 25 |
| S166 | 133 | 9 |
| S167 | 253 | 12 |
| S168 | 184 | 11 |
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
| 2026-09-04 |    8 |    8 |    4 |    8 |    4 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |

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
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |   111 | INFO |
| Total closed lots           |  1980 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1015 med=+0.0% | TAINTED n=1783 med=-38.4% | KEEP-only n=556 med=+51.5% | KILL=16 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.42 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260904T141558Z

- UTC timestamp: `20260904T141558Z`
- GitHub run: [#9067](https://github.com/28twagg-ops/TradingBot/actions/runs/33882632442)
- Run id: `33882632442`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`119s`
- Full logs: `logs/action_runs/20260904T141558Z_live_bot.log`, `logs/action_runs/20260904T141558Z_live_options.log`, `logs/action_runs/20260904T141558Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1017 | 49.9 | +0.0 | +47.6 | $+15,392 |
| TAINTED | 1783 | 33.5 | -38.4 | +12.8 | $-8,664 |
| KEEP-only | 545 | 64.0 | +51.4 | +74.0 | $+10,169 |
| KEEP-only recent | 337 | 60.8 | +54.0 | +91.1 | $+4,912 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (17): ORPHAN, S164, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T10:16:04.532918-04:00","date":"2026-09-04","mode":"entry+manage","header":"entry+manage (2 new)","elapsed_s":106.9,"phases_s":{"reconcile":0.24,"cancel":0.03,"manage":8.78,"protective_stops":1.05,"scan":46.12,"entries":27.8,"reconcile2":3.31},"signals":308,"placed":2,"equity":1006085.47,"open_positions":35,"pending_orders":8,"open_lots":104,"submitted_today":92,"filled_today":111,"unattributed_contracts":0,"top_signals":["S165:TSLA","S164:TSLA","S168:TSLA","S167:TSLA","S166:TSLA","S163:TSLA","S350:TSLA","S351:TSLA"],"github_run":"9067","github_run_id":"33882632442","status":"ok","data_quality":{"clean":{"n":1017,"win":49.85,"med":0.0,"avg":47.64,"pnl":15391.96},"tainted":{"n":1783,"win":33.48,"med":-38.36,"avg":12.81,"pnl":-8663.84},"keep_only":{"n":545,"win":64.04,"med":51.39,"avg":74.05,"pnl":10169.45},"keep_only_recent":{"n":337,"win":60.83,"med":54.0,"avg":91.14,"pnl":4912.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
14:15:59  INFO      Mode: exits
14:15:59  INFO        place_all_stops: checking 3 positions...
14:15:59  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
14:15:59  INFO        STOP skipped APD: fractional (0.1144 shares) — software exit will handle it
14:15:59  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
14:16:00  INFO        [positions] 3/3 (3 valid)
14:16:00  INFO        Daily log -> logs/daily/2026-09-04.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:15 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.49|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  LII  P&L +0.2%  $+0.07                                            HOLD|
|  APD  P&L +0.3%  $+0.09                                            HOLD|
|  AMZN  P&L +1.0%  $+0.36                                           HOLD|
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
=== options_live_micro LIVE 2026-09-04T10:16:01.070793-04:00 share=25% ===
2026-09-04 10:16:01,070 INFO === options_live_micro LIVE 2026-09-04T10:16:01.070793-04:00 share=25% ===
Live account equity $230.49 cash $126.25 #225458845 options_level=3
2026-09-04 10:16:01,132 INFO Live account equity $230.49 cash $126.25 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-04 10:16:01,179 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-04 10:16:01,204 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (197 earlier lines - see full log file)
| w2     |    7 |    6 |   12 |    7 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    54 |
| w3     |    8 |    6 |   13 |    5 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    56 |
| w4     |    6 |    4 |   10 |    3 |    5 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    43 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 241 | 12 |
| S164 | 257 | 13 |
| S165 | 1699 | 25 |
| S166 | 133 | 9 |
| S167 | 253 | 12 |
| S168 | 184 | 11 |
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
| 2026-09-04 |    8 |    8 |    4 |    8 |    4 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |

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
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |   104 | INFO |
| Total closed lots           |  1982 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1017 med=+0.0% | TAINTED n=1783 med=-38.4% | KEEP-only n=545 med=+51.4% | KILL=17 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.49 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260904T142104Z

- UTC timestamp: `20260904T142104Z`
- GitHub run: [#9068](https://github.com/28twagg-ops/TradingBot/actions/runs/33883115220)
- Run id: `33883115220`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`116s`
- Full logs: `logs/action_runs/20260904T142104Z_live_bot.log`, `logs/action_runs/20260904T142104Z_live_options.log`, `logs/action_runs/20260904T142104Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1017 | 49.9 | +0.0 | +47.6 | $+15,392 |
| TAINTED | 1783 | 33.5 | -38.4 | +12.8 | $-8,664 |
| KEEP-only | 545 | 64.0 | +51.4 | +74.0 | $+10,169 |
| KEEP-only recent | 337 | 60.8 | +54.0 | +91.1 | $+4,912 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (17): ORPHAN, S164, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T10:21:12.784405-04:00","date":"2026-09-04","mode":"entry+manage","header":"entry+manage (1 new)","elapsed_s":105.5,"phases_s":{"reconcile":0.52,"cancel":0.16,"manage":11.84,"protective_stops":4.99,"scan":35.32,"entries":40.3,"reconcile2":0.52},"signals":308,"placed":1,"equity":1005722.95,"open_positions":35,"pending_orders":8,"open_lots":101,"submitted_today":93,"filled_today":112,"unattributed_contracts":0,"top_signals":["S165:TSLA","S164:TSLA","S168:TSLA","S167:TSLA","S166:TSLA","S163:TSLA","S350:TSLA","S351:TSLA"],"github_run":"9068","github_run_id":"33883115220","status":"ok","data_quality":{"clean":{"n":1017,"win":49.85,"med":0.0,"avg":47.64,"pnl":15391.96},"tainted":{"n":1783,"win":33.48,"med":-38.36,"avg":12.81,"pnl":-8663.84},"keep_only":{"n":545,"win":64.04,"med":51.39,"avg":74.05,"pnl":10169.45},"keep_only_recent":{"n":337,"win":60.83,"med":54.0,"avg":91.14,"pnl":4912.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
14:21:05  INFO      Mode: exits
14:21:06  INFO        place_all_stops: checking 3 positions...
14:21:06  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
14:21:06  INFO        STOP skipped APD: fractional (0.1144 shares) — software exit will handle it
14:21:06  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
14:21:07  INFO        [positions] 3/3 (3 valid)
14:21:07  INFO        Daily log -> logs/daily/2026-09-04.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.51|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  LII  P&L +0.2%  $+0.07                                            HOLD|
|  APD  P&L +0.5%  $+0.18                                            HOLD|
|  AMZN  P&L +0.9%  $+0.29                                           HOLD|
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
=== options_live_micro LIVE 2026-09-04T10:21:08.445536-04:00 share=25% ===
2026-09-04 10:21:08,445 INFO === options_live_micro LIVE 2026-09-04T10:21:08.445536-04:00 share=25% ===
Live account equity $230.52 cash $126.25 #225458845 options_level=3
2026-09-04 10:21:08,696 INFO Live account equity $230.52 cash $126.25 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-04 10:21:09,010 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-04 10:21:09,161 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (204 earlier lines - see full log file)
| w2     |    7 |    6 |   12 |    7 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    54 |
| w3     |    8 |    6 |   13 |    5 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    56 |
| w4     |    6 |    4 |   10 |    3 |    5 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    43 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 241 | 12 |
| S164 | 257 | 13 |
| S165 | 1699 | 25 |
| S166 | 133 | 9 |
| S167 | 253 | 12 |
| S168 | 184 | 11 |
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
| 2026-09-04 |    8 |    8 |    4 |    8 |    4 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |

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
| State/ledger mismatches     |     6 | WARN | <<<
| Total open lots             |   101 | INFO |
| Total closed lots           |  1982 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1017 med=+0.0% | TAINTED n=1783 med=-38.4% | KEEP-only n=545 med=+51.4% | KILL=17 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.52 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260904T142611Z

- UTC timestamp: `20260904T142611Z`
- GitHub run: [#9069](https://github.com/28twagg-ops/TradingBot/actions/runs/33883596720)
- Run id: `33883596720`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`122s`
- Full logs: `logs/action_runs/20260904T142611Z_live_bot.log`, `logs/action_runs/20260904T142611Z_live_options.log`, `logs/action_runs/20260904T142611Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1018 | 49.9 | +0.0 | +47.7 | $+15,449 |
| TAINTED | 1784 | 33.5 | -38.3 | +12.8 | $-8,639 |
| KEEP-only | 545 | 64.0 | +51.4 | +74.0 | $+10,169 |
| KEEP-only recent | 337 | 60.8 | +54.0 | +91.1 | $+4,912 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (17): ORPHAN, S164, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T10:26:19.989236-04:00","date":"2026-09-04","mode":"entry+manage","header":"entry+manage (4 new)","elapsed_s":110.8,"phases_s":{"reconcile":0.46,"cancel":0.13,"manage":11.74,"protective_stops":4.62,"scan":41.5,"entries":34.14,"reconcile2":0.9},"signals":308,"placed":4,"equity":1005936.88,"open_positions":37,"pending_orders":8,"open_lots":104,"submitted_today":97,"filled_today":116,"unattributed_contracts":0,"top_signals":["S165:TSLA","S164:TSLA","S168:TSLA","S167:TSLA","S166:TSLA","S163:TSLA","S350:TSLA","S351:TSLA"],"github_run":"9069","github_run_id":"33883596720","status":"ok","data_quality":{"clean":{"n":1018,"win":49.9,"med":0.0,"avg":47.68,"pnl":15448.96},"tainted":{"n":1784,"win":33.52,"med":-38.34,"avg":12.83,"pnl":-8638.84},"keep_only":{"n":545,"win":64.04,"med":51.39,"avg":74.05,"pnl":10169.45},"keep_only_recent":{"n":337,"win":60.83,"med":54.0,"avg":91.14,"pnl":4912.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
14:26:13  INFO      Mode: exits
14:26:13  INFO        place_all_stops: checking 3 positions...
14:26:13  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
14:26:14  INFO        STOP skipped APD: fractional (0.1144 shares) — software exit will handle it
14:26:14  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
14:26:14  INFO        [positions] 3/3 (3 valid)
14:26:15  INFO        Daily log -> logs/daily/2026-09-04.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.60|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  LII  P&L +0.5%  $+0.16                                            HOLD|
|  APD  P&L +0.5%  $+0.18                                            HOLD|
|  AMZN  P&L +0.8%  $+0.28                                           HOLD|
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
=== options_live_micro LIVE 2026-09-04T10:26:15.807144-04:00 share=25% ===
2026-09-04 10:26:15,807 INFO === options_live_micro LIVE 2026-09-04T10:26:15.807144-04:00 share=25% ===
Live account equity $230.59 cash $126.25 #225458845 options_level=3
2026-09-04 10:26:16,035 INFO Live account equity $230.59 cash $126.25 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-04 10:26:16,290 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-04 10:26:16,433 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (200 earlier lines - see full log file)
| w2     |    7 |    6 |   12 |    7 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    54 |
| w3     |    8 |    6 |   13 |    5 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    56 |
| w4     |    6 |    4 |   10 |    3 |    5 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    43 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 241 | 12 |
| S164 | 257 | 13 |
| S165 | 1699 | 25 |
| S166 | 133 | 9 |
| S167 | 253 | 12 |
| S168 | 184 | 11 |
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
| 2026-09-04 |    8 |    8 |    4 |    8 |    4 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |

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
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   104 | INFO |
| Total closed lots           |  1984 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1018 med=+0.0% | TAINTED n=1784 med=-38.3% | KEEP-only n=545 med=+51.4% | KILL=17 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.59 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260904T143101Z

- UTC timestamp: `20260904T143101Z`
- GitHub run: [#9070](https://github.com/28twagg-ops/TradingBot/actions/runs/33884078712)
- Run id: `33884078712`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`102s`
- Full logs: `logs/action_runs/20260904T143101Z_live_bot.log`, `logs/action_runs/20260904T143101Z_live_options.log`, `logs/action_runs/20260904T143101Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1019 | 50.0 | +0.0 | +47.7 | $+15,515 |
| TAINTED | 1784 | 33.5 | -38.3 | +12.8 | $-8,639 |
| KEEP-only | 545 | 64.0 | +51.4 | +74.0 | $+10,169 |
| KEEP-only recent | 337 | 60.8 | +54.0 | +91.1 | $+4,912 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (17): ORPHAN, S164, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T10:31:07.724398-04:00","date":"2026-09-04","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":92.4,"phases_s":{"reconcile":0.47,"cancel":0.09,"manage":10.92,"protective_stops":3.0,"scan":34.47,"entries":24.17,"reconcile2":0.36},"signals":308,"placed":0,"equity":1006007.74,"open_positions":36,"pending_orders":8,"open_lots":103,"submitted_today":97,"filled_today":116,"unattributed_contracts":0,"top_signals":["S165:TSLA","S164:TSLA","S168:TSLA","S167:TSLA","S166:TSLA","S163:TSLA","S350:TSLA","S351:TSLA"],"github_run":"9070","github_run_id":"33884078712","status":"ok","data_quality":{"clean":{"n":1019,"win":49.95,"med":0.0,"avg":47.74,"pnl":15514.96},"tainted":{"n":1784,"win":33.52,"med":-38.34,"avg":12.83,"pnl":-8638.84},"keep_only":{"n":545,"win":64.04,"med":51.39,"avg":74.05,"pnl":10169.45},"keep_only_recent":{"n":337,"win":60.83,"med":54.0,"avg":91.14,"pnl":4912.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
14:31:02  INFO      Mode: exits
14:31:03  INFO        place_all_stops: checking 3 positions...
14:31:03  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
14:31:03  INFO        STOP skipped APD: fractional (0.1144 shares) — software exit will handle it
14:31:03  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
14:31:03  INFO        [positions] 3/3 (3 valid)
14:31:03  INFO        Daily log -> logs/daily/2026-09-04.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.68|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  APD  P&L +0.6%  $+0.22                                            HOLD|
|  LII  P&L +0.7%  $+0.23                                            HOLD|
|  AMZN  P&L +0.7%  $+0.26                                           HOLD|
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
=== options_live_micro LIVE 2026-09-04T10:31:04.248415-04:00 share=25% ===
2026-09-04 10:31:04,248 INFO === options_live_micro LIVE 2026-09-04T10:31:04.248415-04:00 share=25% ===
Live account equity $230.67 cash $126.25 #225458845 options_level=3
2026-09-04 10:31:04,416 INFO Live account equity $230.67 cash $126.25 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-04 10:31:04,596 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-04 10:31:04,675 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (201 earlier lines - see full log file)
| w2     |    7 |    6 |   12 |    7 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    54 |
| w3     |    8 |    6 |   13 |    5 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    56 |
| w4     |    6 |    4 |   10 |    3 |    5 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    43 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 241 | 12 |
| S164 | 257 | 13 |
| S165 | 1699 | 25 |
| S166 | 133 | 9 |
| S167 | 253 | 12 |
| S168 | 184 | 11 |
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
| 2026-09-04 |    8 |    8 |    4 |    8 |    4 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |

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
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   103 | INFO |
| Total closed lots           |  1985 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1019 med=+0.0% | TAINTED n=1784 med=-38.3% | KEEP-only n=545 med=+51.4% | KILL=17 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.68 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260904T143600Z

- UTC timestamp: `20260904T143600Z`
- GitHub run: [#9071](https://github.com/28twagg-ops/TradingBot/actions/runs/33884572959)
- Run id: `33884572959`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`107s`
- Full logs: `logs/action_runs/20260904T143600Z_live_bot.log`, `logs/action_runs/20260904T143600Z_live_options.log`, `logs/action_runs/20260904T143600Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1019 | 50.0 | +0.0 | +47.7 | $+15,515 |
| TAINTED | 1784 | 33.5 | -38.3 | +12.8 | $-8,639 |
| KEEP-only | 545 | 64.0 | +51.4 | +74.0 | $+10,169 |
| KEEP-only recent | 337 | 60.8 | +54.0 | +91.1 | $+4,912 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (17): ORPHAN, S164, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T10:36:05.896778-04:00","date":"2026-09-04","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":95.7,"phases_s":{"reconcile":0.19,"cancel":0.03,"manage":7.38,"protective_stops":1.1,"scan":45.7,"entries":21.58,"reconcile2":0.11},"signals":308,"placed":0,"equity":1005933.72,"open_positions":36,"pending_orders":8,"open_lots":103,"submitted_today":97,"filled_today":116,"unattributed_contracts":0,"top_signals":["S165:TSLA","S164:TSLA","S168:TSLA","S167:TSLA","S166:TSLA","S163:TSLA","S350:TSLA","S351:TSLA"],"github_run":"9071","github_run_id":"33884572959","status":"ok","data_quality":{"clean":{"n":1019,"win":49.95,"med":0.0,"avg":47.74,"pnl":15514.96},"tainted":{"n":1784,"win":33.52,"med":-38.34,"avg":12.83,"pnl":-8638.84},"keep_only":{"n":545,"win":64.04,"med":51.39,"avg":74.05,"pnl":10169.45},"keep_only_recent":{"n":337,"win":60.83,"med":54.0,"avg":91.14,"pnl":4912.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
14:36:01  INFO      Mode: exits
14:36:01  INFO        place_all_stops: checking 3 positions...
14:36:01  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
14:36:01  INFO        STOP skipped APD: fractional (0.1144 shares) — software exit will handle it
14:36:01  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
14:36:02  INFO        [positions] 3/3 (3 valid)
14:36:02  INFO        Daily log -> logs/daily/2026-09-04.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.63|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMZN  P&L +0.6%  $+0.19                                           HOLD|
|  APD  P&L +0.6%  $+0.22                                            HOLD|
|  LII  P&L +0.7%  $+0.25                                            HOLD|
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
=== options_live_micro LIVE 2026-09-04T10:36:02.867222-04:00 share=25% ===
2026-09-04 10:36:02,867 INFO === options_live_micro LIVE 2026-09-04T10:36:02.867222-04:00 share=25% ===
Live account equity $230.63 cash $126.25 #225458845 options_level=3
2026-09-04 10:36:02,977 INFO Live account equity $230.63 cash $126.25 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-04 10:36:03,030 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-04 10:36:03,058 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (197 earlier lines - see full log file)
| w2     |    7 |    6 |   12 |    7 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    54 |
| w3     |    8 |    6 |   13 |    5 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    56 |
| w4     |    6 |    4 |   10 |    3 |    5 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    43 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 241 | 12 |
| S164 | 257 | 13 |
| S165 | 1699 | 25 |
| S166 | 133 | 9 |
| S167 | 253 | 12 |
| S168 | 184 | 11 |
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
| 2026-09-04 |    8 |    8 |    4 |    8 |    4 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |

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
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   103 | INFO |
| Total closed lots           |  1985 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1019 med=+0.0% | TAINTED n=1784 med=-38.3% | KEEP-only n=545 med=+51.4% | KILL=17 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.63 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260904T144100Z

- UTC timestamp: `20260904T144100Z`
- GitHub run: [#9072](https://github.com/28twagg-ops/TradingBot/actions/runs/33885050981)
- Run id: `33885050981`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`102s`
- Full logs: `logs/action_runs/20260904T144100Z_live_bot.log`, `logs/action_runs/20260904T144100Z_live_options.log`, `logs/action_runs/20260904T144100Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1020 | 49.9 | +0.0 | +47.7 | $+15,496 |
| TAINTED | 1784 | 33.5 | -38.3 | +12.8 | $-8,639 |
| KEEP-only | 546 | 63.9 | +51.2 | +73.8 | $+10,150 |
| KEEP-only recent | 338 | 60.7 | +53.8 | +90.7 | $+4,893 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (17): ORPHAN, S164, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T10:41:06.723583-04:00","date":"2026-09-04","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":93.4,"phases_s":{"reconcile":0.39,"cancel":0.13,"manage":11.94,"protective_stops":4.42,"scan":35.11,"entries":30.21,"reconcile2":0.42},"signals":308,"placed":0,"equity":1005913.72,"open_positions":35,"pending_orders":8,"open_lots":102,"submitted_today":97,"filled_today":116,"unattributed_contracts":0,"top_signals":["S165:TSLA","S164:TSLA","S168:TSLA","S167:TSLA","S166:TSLA","S163:TSLA","S350:TSLA","S351:TSLA"],"github_run":"9072","github_run_id":"33885050981","status":"ok","data_quality":{"clean":{"n":1020,"win":49.9,"med":0.0,"avg":47.65,"pnl":15495.96},"tainted":{"n":1784,"win":33.52,"med":-38.34,"avg":12.83,"pnl":-8638.84},"keep_only":{"n":546,"win":63.92,"med":51.18,"avg":73.83,"pnl":10150.45},"keep_only_recent":{"n":338,"win":60.65,"med":53.78,"avg":90.74,"pnl":4893.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
14:41:01  INFO      Mode: exits
14:41:02  INFO        place_all_stops: checking 3 positions...
14:41:02  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
14:41:02  INFO        STOP skipped APD: fractional (0.1144 shares) — software exit will handle it
14:41:02  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
14:41:02  INFO        [positions] 3/3 (3 valid)
14:41:02  INFO        Daily log -> logs/daily/2026-09-04.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.59|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  APD  P&L +0.5%  $+0.18                                            HOLD|
|  AMZN  P&L +0.6%  $+0.22                                           HOLD|
|  LII  P&L +0.6%  $+0.22                                            HOLD|
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
=== options_live_micro LIVE 2026-09-04T10:41:03.641834-04:00 share=25% ===
2026-09-04 10:41:03,641 INFO === options_live_micro LIVE 2026-09-04T10:41:03.641834-04:00 share=25% ===
Live account equity $230.59 cash $126.25 #225458845 options_level=3
2026-09-04 10:41:03,843 INFO Live account equity $230.59 cash $126.25 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-04 10:41:04,023 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-04 10:41:04,163 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (192 earlier lines - see full log file)
| w2     |    7 |    6 |   12 |    7 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    54 |
| w3     |    8 |    6 |   13 |    5 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    56 |
| w4     |    6 |    4 |   10 |    3 |    5 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    43 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 241 | 12 |
| S164 | 257 | 13 |
| S165 | 1699 | 25 |
| S166 | 133 | 9 |
| S167 | 253 | 12 |
| S168 | 184 | 11 |
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
| 2026-09-04 |    8 |    8 |    4 |    8 |    4 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |

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
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |   102 | INFO |
| Total closed lots           |  1986 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1020 med=+0.0% | TAINTED n=1784 med=-38.3% | KEEP-only n=546 med=+51.2% | KILL=17 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.59 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260904T144600Z

- UTC timestamp: `20260904T144600Z`
- GitHub run: [#9073](https://github.com/28twagg-ops/TradingBot/actions/runs/33885529925)
- Run id: `33885529925`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`191s`
- Full logs: `logs/action_runs/20260904T144600Z_live_bot.log`, `logs/action_runs/20260904T144600Z_live_options.log`, `logs/action_runs/20260904T144600Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1020 | 49.9 | +0.0 | +47.7 | $+15,496 |
| TAINTED | 1785 | 33.6 | -38.3 | +12.8 | $-8,611 |
| KEEP-only | 546 | 63.9 | +51.2 | +73.8 | $+10,150 |
| KEEP-only recent | 338 | 60.7 | +53.8 | +90.7 | $+4,893 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (17): ORPHAN, S164, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T10:46:05.560812-04:00","date":"2026-09-04","mode":"entry+manage","header":"entry+manage (33 new)","elapsed_s":179.3,"phases_s":{"reconcile":0.15,"cancel":0.03,"manage":7.67,"protective_stops":1.09,"scan":46.45,"entries":96.73,"reconcile2":1.17},"signals":308,"placed":33,"equity":1005758.7,"open_positions":42,"pending_orders":20,"open_lots":123,"submitted_today":130,"filled_today":137,"unattributed_contracts":0,"top_signals":["S165:TSLA","S164:TSLA","S168:TSLA","S167:TSLA","S166:TSLA","S163:TSLA","S350:TSLA","S351:TSLA"],"github_run":"9073","github_run_id":"33885529925","status":"ok","data_quality":{"clean":{"n":1020,"win":49.9,"med":0.0,"avg":47.65,"pnl":15495.96},"tainted":{"n":1785,"win":33.56,"med":-38.33,"avg":12.84,"pnl":-8610.84},"keep_only":{"n":546,"win":63.92,"med":51.18,"avg":73.83,"pnl":10150.45},"keep_only_recent":{"n":338,"win":60.65,"med":53.78,"avg":90.74,"pnl":4893.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
14:46:01  INFO      Mode: exits
14:46:01  INFO        place_all_stops: checking 3 positions...
14:46:01  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
14:46:01  INFO        STOP skipped APD: fractional (0.1144 shares) — software exit will handle it
14:46:01  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
14:46:01  INFO        [positions] 3/3 (3 valid)
14:46:01  INFO        Daily log -> logs/daily/2026-09-04.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.59|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  APD  P&L +0.5%  $+0.17                                            HOLD|
|  AMZN  P&L +0.6%  $+0.21                                           HOLD|
|  LII  P&L +0.7%  $+0.25                                            HOLD|
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
=== options_live_micro LIVE 2026-09-04T10:46:02.564043-04:00 share=25% ===
2026-09-04 10:46:02,564 INFO === options_live_micro LIVE 2026-09-04T10:46:02.564043-04:00 share=25% ===
Live account equity $230.59 cash $126.25 #225458845 options_level=3
2026-09-04 10:46:02,629 INFO Live account equity $230.59 cash $126.25 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-04 10:46:02,679 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-04 10:46:02,701 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (231 earlier lines - see full log file)
| w2     |    7 |    6 |   12 |    7 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    54 |
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    43 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 245 | 12 |
| S164 | 259 | 13 |
| S165 | 1703 | 26 |
| S166 | 135 | 9 |
| S167 | 257 | 13 |
| S168 | 184 | 11 |
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
| 2026-09-04 |   12 |   10 |    8 |   10 |    8 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    52 |

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
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |   123 | INFO |
| Total closed lots           |  1987 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1020 med=+0.0% | TAINTED n=1785 med=-38.3% | KEEP-only n=546 med=+51.2% | KILL=17 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.59 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260904T145058Z

- UTC timestamp: `20260904T145058Z`
- GitHub run: [#9074](https://github.com/28twagg-ops/TradingBot/actions/runs/33886005235)
- Run id: `33886005235`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`136s`
- Full logs: `logs/action_runs/20260904T145058Z_live_bot.log`, `logs/action_runs/20260904T145058Z_live_options.log`, `logs/action_runs/20260904T145058Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1020 | 49.9 | +0.0 | +47.7 | $+15,496 |
| TAINTED | 1785 | 33.6 | -38.3 | +12.8 | $-8,611 |
| KEEP-only | 546 | 63.9 | +51.2 | +73.8 | $+10,150 |
| KEEP-only recent | 338 | 60.7 | +53.8 | +90.7 | $+4,893 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (17): ORPHAN, S164, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T10:51:04.392986-04:00","date":"2026-09-04","mode":"entry+manage","header":"entry+manage (4 new)","elapsed_s":124.6,"phases_s":{"reconcile":0.33,"cancel":0.06,"manage":10.93,"protective_stops":1.98,"scan":45.68,"entries":38.24,"reconcile2":3.52},"signals":308,"placed":4,"equity":1005656.01,"open_positions":43,"pending_orders":16,"open_lots":129,"submitted_today":134,"filled_today":145,"unattributed_contracts":0,"top_signals":["S165:TSLA","S164:TSLA","S168:TSLA","S167:TSLA","S166:TSLA","S163:TSLA","S350:TSLA","S351:TSLA"],"github_run":"9074","github_run_id":"33886005235","status":"ok","data_quality":{"clean":{"n":1020,"win":49.9,"med":0.0,"avg":47.65,"pnl":15495.96},"tainted":{"n":1785,"win":33.56,"med":-38.33,"avg":12.84,"pnl":-8610.84},"keep_only":{"n":546,"win":63.92,"med":51.18,"avg":73.83,"pnl":10150.45},"keep_only_recent":{"n":338,"win":60.65,"med":53.78,"avg":90.74,"pnl":4893.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
14:50:59  INFO      Mode: exits
14:50:59  INFO        place_all_stops: checking 3 positions...
14:50:59  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
14:50:59  INFO        STOP skipped APD: fractional (0.1144 shares) — software exit will handle it
14:50:59  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
14:50:59  INFO        [positions] 3/3 (3 valid)
14:51:00  INFO        Daily log -> logs/daily/2026-09-04.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:50 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.40|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  APD  P&L +0.4%  $+0.14                                            HOLD|
|  AMZN  P&L +0.4%  $+0.15                                           HOLD|
|  LII  P&L +0.4%  $+0.15                                            HOLD|
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
=== options_live_micro LIVE 2026-09-04T10:51:00.960030-04:00 share=25% ===
2026-09-04 10:51:00,960 INFO === options_live_micro LIVE 2026-09-04T10:51:00.960030-04:00 share=25% ===
Live account equity $230.40 cash $126.25 #225458845 options_level=3
2026-09-04 10:51:01,057 INFO Live account equity $230.40 cash $126.25 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-04 10:51:01,158 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-04 10:51:01,209 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (199 earlier lines - see full log file)
| w2     |    7 |    6 |   12 |    7 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    54 |
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    43 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 245 | 12 |
| S164 | 259 | 13 |
| S165 | 1703 | 26 |
| S166 | 135 | 9 |
| S167 | 257 | 13 |
| S168 | 184 | 11 |
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
| 2026-09-04 |   12 |   10 |    8 |   10 |    8 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    52 |

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
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |   129 | INFO |
| Total closed lots           |  1987 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1020 med=+0.0% | TAINTED n=1785 med=-38.3% | KEEP-only n=546 med=+51.2% | KILL=17 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.4 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260904T145604Z

- UTC timestamp: `20260904T145604Z`
- GitHub run: [#9075](https://github.com/28twagg-ops/TradingBot/actions/runs/33886484050)
- Run id: `33886484050`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`118s`
- Full logs: `logs/action_runs/20260904T145604Z_live_bot.log`, `logs/action_runs/20260904T145604Z_live_options.log`, `logs/action_runs/20260904T145604Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1020 | 49.9 | +0.0 | +47.7 | $+15,496 |
| TAINTED | 1786 | 33.5 | -38.3 | +12.8 | $-8,625 |
| KEEP-only | 546 | 63.9 | +51.2 | +73.8 | $+10,150 |
| KEEP-only recent | 338 | 60.7 | +53.8 | +90.7 | $+4,893 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (17): ORPHAN, S164, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T10:56:11.345041-04:00","date":"2026-09-04","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":108.7,"phases_s":{"reconcile":0.51,"cancel":0.1,"manage":12.27,"protective_stops":4.07,"scan":29.12,"entries":36.34,"reconcile2":0.34},"signals":308,"placed":0,"equity":1005571.63,"open_positions":45,"pending_orders":12,"open_lots":133,"submitted_today":134,"filled_today":149,"unattributed_contracts":0,"top_signals":["S165:TSLA","S164:TSLA","S168:TSLA","S167:TSLA","S166:TSLA","S163:TSLA","S350:TSLA","S351:TSLA"],"github_run":"9075","github_run_id":"33886484050","status":"ok","data_quality":{"clean":{"n":1020,"win":49.9,"med":0.0,"avg":47.65,"pnl":15495.96},"tainted":{"n":1786,"win":33.54,"med":-38.25,"avg":12.82,"pnl":-8624.84},"keep_only":{"n":546,"win":63.92,"med":51.18,"avg":73.83,"pnl":10150.45},"keep_only_recent":{"n":338,"win":60.65,"med":53.78,"avg":90.74,"pnl":4893.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
14:56:05  INFO      Mode: exits
14:56:06  INFO        place_all_stops: checking 3 positions...
14:56:06  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
14:56:06  INFO        STOP skipped APD: fractional (0.1144 shares) — software exit will handle it
14:56:06  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
14:56:06  INFO        [positions] 3/3 (3 valid)
14:56:07  INFO        Daily log -> logs/daily/2026-09-04.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:56 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.47|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMZN  P&L +0.4%  $+0.14                                           HOLD|
|  APD  P&L +0.4%  $+0.15                                            HOLD|
|  LII  P&L +0.6%  $+0.22                                            HOLD|
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
=== options_live_micro LIVE 2026-09-04T10:56:07.816891-04:00 share=25% ===
2026-09-04 10:56:07,816 INFO === options_live_micro LIVE 2026-09-04T10:56:07.816891-04:00 share=25% ===
Live account equity $230.47 cash $126.25 #225458845 options_level=3
2026-09-04 10:56:07,998 INFO Live account equity $230.47 cash $126.25 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-04 10:56:08,201 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-04 10:56:08,288 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (201 earlier lines - see full log file)
| w2     |    7 |    6 |   12 |    7 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    54 |
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    43 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 245 | 12 |
| S164 | 259 | 13 |
| S165 | 1703 | 26 |
| S166 | 135 | 9 |
| S167 | 257 | 13 |
| S168 | 184 | 11 |
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
| 2026-09-04 |   12 |   10 |    8 |   10 |    8 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    52 |

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
| State/ledger mismatches     |     9 | WARN | <<<
| Total open lots             |   133 | INFO |
| Total closed lots           |  1988 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1020 med=+0.0% | TAINTED n=1786 med=-38.3% | KEEP-only n=546 med=+51.2% | KILL=17 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.47 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260904T150139Z

- UTC timestamp: `20260904T150139Z`
- GitHub run: [#9076](https://github.com/28twagg-ops/TradingBot/actions/runs/33886954931)
- Run id: `33886954931`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`121s`
- Full logs: `logs/action_runs/20260904T150139Z_live_bot.log`, `logs/action_runs/20260904T150139Z_live_options.log`, `logs/action_runs/20260904T150139Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1020 | 49.9 | +0.0 | +47.7 | $+15,496 |
| TAINTED | 1786 | 33.5 | -38.3 | +12.8 | $-8,625 |
| KEEP-only | 546 | 63.9 | +51.2 | +73.8 | $+10,150 |
| KEEP-only recent | 338 | 60.7 | +53.8 | +90.7 | $+4,893 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (17): ORPHAN, S164, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T11:01:45.069630-04:00","date":"2026-09-04","mode":"entry+manage","header":"entry+manage (2 new)","elapsed_s":111.3,"phases_s":{"reconcile":0.48,"cancel":0.09,"manage":11.23,"protective_stops":3.67,"scan":35.55,"entries":31.58,"reconcile2":0.36},"signals":308,"placed":2,"equity":1005586.47,"open_positions":46,"pending_orders":8,"open_lots":139,"submitted_today":136,"filled_today":155,"unattributed_contracts":0,"top_signals":["S165:TSLA","S164:TSLA","S168:TSLA","S167:TSLA","S166:TSLA","S163:TSLA","S350:TSLA","S351:TSLA"],"github_run":"9076","github_run_id":"33886954931","status":"ok","data_quality":{"clean":{"n":1020,"win":49.9,"med":0.0,"avg":47.65,"pnl":15495.96},"tainted":{"n":1786,"win":33.54,"med":-38.25,"avg":12.82,"pnl":-8624.84},"keep_only":{"n":546,"win":63.92,"med":51.18,"avg":73.83,"pnl":10150.45},"keep_only_recent":{"n":338,"win":60.65,"med":53.78,"avg":90.74,"pnl":4893.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
15:01:40  INFO      Mode: exits
15:01:40  INFO        place_all_stops: checking 3 positions...
15:01:40  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
15:01:40  INFO        STOP skipped APD: fractional (0.1144 shares) — software exit will handle it
15:01:40  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
15:01:41  INFO        [positions] 3/3 (3 valid)
15:01:41  INFO        Daily log -> logs/daily/2026-09-04.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.48|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMZN  P&L +0.3%  $+0.09                                           HOLD|
|  APD  P&L +0.5%  $+0.18                                            HOLD|
|  LII  P&L +0.7%  $+0.24                                            HOLD|
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
=== options_live_micro LIVE 2026-09-04T11:01:42.152844-04:00 share=25% ===
2026-09-04 11:01:42,152 INFO === options_live_micro LIVE 2026-09-04T11:01:42.152844-04:00 share=25% ===
Live account equity $230.48 cash $126.25 #225458845 options_level=3
2026-09-04 11:01:42,334 INFO Live account equity $230.48 cash $126.25 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-04 11:01:42,513 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-04 11:01:42,603 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (199 earlier lines - see full log file)
| w2     |    7 |    6 |   12 |    7 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    54 |
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    43 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 245 | 12 |
| S164 | 259 | 13 |
| S165 | 1703 | 26 |
| S166 | 135 | 9 |
| S167 | 257 | 13 |
| S168 | 184 | 11 |
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
| 2026-09-04 |   12 |   10 |    8 |   10 |    8 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    52 |

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
| State/ledger mismatches     |     9 | WARN | <<<
| Total open lots             |   139 | INFO |
| Total closed lots           |  1988 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1020 med=+0.0% | TAINTED n=1786 med=-38.3% | KEEP-only n=546 med=+51.2% | KILL=17 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.48 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260904T150602Z

- UTC timestamp: `20260904T150602Z`
- GitHub run: [#9077](https://github.com/28twagg-ops/TradingBot/actions/runs/33887435422)
- Run id: `33887435422`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`122s`
- Full logs: `logs/action_runs/20260904T150602Z_live_bot.log`, `logs/action_runs/20260904T150602Z_live_options.log`, `logs/action_runs/20260904T150602Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1020 | 49.9 | +0.0 | +47.7 | $+15,496 |
| TAINTED | 1786 | 33.5 | -38.3 | +12.8 | $-8,625 |
| KEEP-only | 546 | 63.9 | +51.2 | +73.8 | $+10,150 |
| KEEP-only recent | 338 | 60.7 | +53.8 | +90.7 | $+4,893 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (17): ORPHAN, S164, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T11:06:07.739423-04:00","date":"2026-09-04","mode":"entry+manage","header":"entry+manage (2 new)","elapsed_s":111.7,"phases_s":{"reconcile":0.25,"cancel":0.03,"manage":8.31,"protective_stops":0.93,"scan":46.07,"entries":30.02,"reconcile2":0.11},"signals":308,"placed":2,"equity":1005507.37,"open_positions":46,"pending_orders":10,"open_lots":139,"submitted_today":138,"filled_today":155,"unattributed_contracts":0,"top_signals":["S165:TSLA","S164:TSLA","S168:TSLA","S167:TSLA","S166:TSLA","S163:TSLA","S350:TSLA","S351:TSLA"],"github_run":"9077","github_run_id":"33887435422","status":"ok","data_quality":{"clean":{"n":1020,"win":49.9,"med":0.0,"avg":47.65,"pnl":15495.96},"tainted":{"n":1786,"win":33.54,"med":-38.25,"avg":12.82,"pnl":-8624.84},"keep_only":{"n":546,"win":63.92,"med":51.18,"avg":73.83,"pnl":10150.45},"keep_only_recent":{"n":338,"win":60.65,"med":53.78,"avg":90.74,"pnl":4893.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
15:06:03  INFO      Mode: exits
15:06:03  INFO        place_all_stops: checking 3 positions...
15:06:03  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
15:06:03  INFO        STOP skipped APD: fractional (0.1144 shares) — software exit will handle it
15:06:03  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
15:06:04  INFO        [positions] 3/3 (3 valid)
15:06:04  INFO        Daily log -> logs/daily/2026-09-04.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.34|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMZN  P&L +0.1%  $+0.05                                           HOLD|
|  LII  P&L +0.4%  $+0.15                                            HOLD|
|  APD  P&L +0.5%  $+0.17                                            HOLD|
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
=== options_live_micro LIVE 2026-09-04T11:06:05.066634-04:00 share=25% ===
2026-09-04 11:06:05,066 INFO === options_live_micro LIVE 2026-09-04T11:06:05.066634-04:00 share=25% ===
Live account equity $230.34 cash $126.25 #225458845 options_level=3
2026-09-04 11:06:05,123 INFO Live account equity $230.34 cash $126.25 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-04 11:06:05,148 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-04 11:06:05,164 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (201 earlier lines - see full log file)
| w2     |    7 |    6 |   12 |    7 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    54 |
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    43 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 245 | 12 |
| S164 | 259 | 13 |
| S165 | 1703 | 26 |
| S166 | 135 | 9 |
| S167 | 257 | 13 |
| S168 | 184 | 11 |
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
| 2026-09-04 |   12 |   10 |    8 |   10 |    8 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    52 |

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
| State/ledger mismatches     |     9 | WARN | <<<
| Total open lots             |   139 | INFO |
| Total closed lots           |  1988 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1020 med=+0.0% | TAINTED n=1786 med=-38.3% | KEEP-only n=546 med=+51.2% | KILL=17 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.34 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260904T151058Z

- UTC timestamp: `20260904T151058Z`
- GitHub run: [#9078](https://github.com/28twagg-ops/TradingBot/actions/runs/33887912408)
- Run id: `33887912408`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`131s`
- Full logs: `logs/action_runs/20260904T151058Z_live_bot.log`, `logs/action_runs/20260904T151058Z_live_options.log`, `logs/action_runs/20260904T151058Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1020 | 49.9 | +0.0 | +47.7 | $+15,496 |
| TAINTED | 1786 | 33.5 | -38.3 | +12.8 | $-8,625 |
| KEEP-only | 546 | 63.9 | +51.2 | +73.8 | $+10,150 |
| KEEP-only recent | 338 | 60.7 | +53.8 | +90.7 | $+4,893 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (17): ORPHAN, S164, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T11:11:05.439068-04:00","date":"2026-09-04","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":119.7,"phases_s":{"reconcile":0.36,"cancel":0.06,"manage":10.43,"protective_stops":2.45,"scan":54.23,"entries":24.45,"reconcile2":0.24},"signals":308,"placed":0,"equity":1005442.31,"open_positions":46,"pending_orders":8,"open_lots":141,"submitted_today":138,"filled_today":157,"unattributed_contracts":0,"top_signals":["S165:TSLA","S164:TSLA","S168:TSLA","S167:TSLA","S166:TSLA","S163:TSLA","S350:TSLA","S351:TSLA"],"github_run":"9078","github_run_id":"33887912408","status":"ok","data_quality":{"clean":{"n":1020,"win":49.9,"med":0.0,"avg":47.65,"pnl":15495.96},"tainted":{"n":1786,"win":33.54,"med":-38.25,"avg":12.82,"pnl":-8624.84},"keep_only":{"n":546,"win":63.92,"med":51.18,"avg":73.83,"pnl":10150.45},"keep_only_recent":{"n":338,"win":60.65,"med":53.78,"avg":90.74,"pnl":4893.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
15:10:59  INFO      Mode: exits
15:11:00  INFO        place_all_stops: checking 3 positions...
15:11:00  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
15:11:00  INFO        STOP skipped APD: fractional (0.1144 shares) — software exit will handle it
15:11:00  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
15:11:00  INFO        [positions] 3/3 (3 valid)
15:11:00  INFO        Daily log -> logs/daily/2026-09-04.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.31|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMZN  P&L +0.0%  $+0.02                                           HOLD|
|  APD  P&L +0.4%  $+0.13                                            HOLD|
|  LII  P&L +0.6%  $+0.20                                            HOLD|
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
=== options_live_micro LIVE 2026-09-04T11:11:02.109492-04:00 share=25% ===
2026-09-04 11:11:02,109 INFO === options_live_micro LIVE 2026-09-04T11:11:02.109492-04:00 share=25% ===
Live account equity $230.30 cash $126.25 #225458845 options_level=3
2026-09-04 11:11:02,198 INFO Live account equity $230.30 cash $126.25 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-04 11:11:02,335 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-04 11:11:02,378 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (199 earlier lines - see full log file)
| w2     |    7 |    6 |   12 |    7 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    54 |
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    43 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 245 | 12 |
| S164 | 261 | 13 |
| S165 | 1703 | 26 |
| S166 | 135 | 9 |
| S167 | 257 | 13 |
| S168 | 184 | 11 |
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
| 2026-09-04 |   12 |   12 |    8 |   10 |    8 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    54 |

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
| State/ledger mismatches     |     9 | WARN | <<<
| Total open lots             |   141 | INFO |
| Total closed lots           |  1988 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1020 med=+0.0% | TAINTED n=1786 med=-38.3% | KEEP-only n=546 med=+51.2% | KILL=17 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.31 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260904T151605Z

- UTC timestamp: `20260904T151605Z`
- GitHub run: [#9079](https://github.com/28twagg-ops/TradingBot/actions/runs/33888390227)
- Run id: `33888390227`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`106s`
- Full logs: `logs/action_runs/20260904T151605Z_live_bot.log`, `logs/action_runs/20260904T151605Z_live_options.log`, `logs/action_runs/20260904T151605Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1020 | 49.9 | +0.0 | +47.7 | $+15,496 |
| TAINTED | 1786 | 33.5 | -38.3 | +12.8 | $-8,625 |
| KEEP-only | 546 | 63.9 | +51.2 | +73.8 | $+10,150 |
| KEEP-only recent | 338 | 60.7 | +53.8 | +90.7 | $+4,893 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (17): ORPHAN, S164, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T11:16:11.581019-04:00","date":"2026-09-04","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":96.9,"phases_s":{"reconcile":0.16,"cancel":0.03,"manage":8.17,"protective_stops":1.11,"scan":35.5,"entries":23.17,"reconcile2":3.12},"signals":308,"placed":0,"equity":1005258.31,"open_positions":46,"pending_orders":8,"open_lots":141,"submitted_today":138,"filled_today":157,"unattributed_contracts":0,"top_signals":["S165:TSLA","S164:TSLA","S168:TSLA","S167:TSLA","S166:TSLA","S163:TSLA","S350:TSLA","S351:TSLA"],"github_run":"9079","github_run_id":"33888390227","status":"ok","data_quality":{"clean":{"n":1020,"win":49.9,"med":0.0,"avg":47.65,"pnl":15495.96},"tainted":{"n":1786,"win":33.54,"med":-38.25,"avg":12.82,"pnl":-8624.84},"keep_only":{"n":546,"win":63.92,"med":51.18,"avg":73.83,"pnl":10150.45},"keep_only_recent":{"n":338,"win":60.65,"med":53.78,"avg":90.74,"pnl":4893.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
15:16:07  INFO      Mode: exits
15:16:07  INFO        place_all_stops: checking 3 positions...
15:16:07  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
15:16:07  INFO        STOP skipped APD: fractional (0.1144 shares) — software exit will handle it
15:16:07  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
15:16:08  INFO        [positions] 3/3 (3 valid)
15:16:08  INFO        Daily log -> logs/daily/2026-09-04.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.36|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMZN  P&L +0.0%  $+0.01                                           HOLD|
|  APD  P&L +0.4%  $+0.14                                            HOLD|
|  LII  P&L +0.7%  $+0.23                                            HOLD|
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
=== options_live_micro LIVE 2026-09-04T11:16:08.994207-04:00 share=25% ===
2026-09-04 11:16:08,994 INFO === options_live_micro LIVE 2026-09-04T11:16:08.994207-04:00 share=25% ===
Live account equity $230.36 cash $126.25 #225458845 options_level=3
2026-09-04 11:16:09,034 INFO Live account equity $230.36 cash $126.25 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-04 11:16:09,058 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-04 11:16:09,072 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (201 earlier lines - see full log file)
| w2     |    7 |    6 |   12 |    7 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    54 |
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    43 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 245 | 12 |
| S164 | 261 | 13 |
| S165 | 1703 | 26 |
| S166 | 135 | 9 |
| S167 | 257 | 13 |
| S168 | 184 | 11 |
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
| 2026-09-04 |   12 |   12 |    8 |   10 |    8 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    54 |

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
| State/ledger mismatches     |     9 | WARN | <<<
| Total open lots             |   141 | INFO |
| Total closed lots           |  1988 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1020 med=+0.0% | TAINTED n=1786 med=-38.3% | KEEP-only n=546 med=+51.2% | KILL=17 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.36 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260904T152636Z

- UTC timestamp: `20260904T152636Z`
- GitHub run: [#9081](https://github.com/28twagg-ops/TradingBot/actions/runs/33889345837)
- Run id: `33889345837`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`234s`
- Full logs: `logs/action_runs/20260904T152636Z_live_bot.log`, `logs/action_runs/20260904T152636Z_live_options.log`, `logs/action_runs/20260904T152636Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1021 | 49.9 | +0.0 | +47.6 | $+15,481 |
| TAINTED | 1787 | 33.6 | -38.2 | +12.9 | $-8,581 |
| KEEP-only | 546 | 63.9 | +51.2 | +73.8 | $+10,150 |
| KEEP-only recent | 338 | 60.7 | +53.8 | +90.7 | $+4,893 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (17): ORPHAN, S164, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T11:26:41.325021-04:00","date":"2026-09-04","mode":"entry+manage","header":"entry+manage (5 new)","elapsed_s":222.6,"phases_s":{"reconcile":1.42,"cancel":0.03,"manage":8.23,"protective_stops":0.91,"scan":45.53,"entries":139.64,"reconcile2":0.39},"signals":308,"placed":5,"equity":1005168.85,"open_positions":47,"pending_orders":8,"open_lots":152,"submitted_today":143,"filled_today":174,"unattributed_contracts":0,"top_signals":["S165:TSLA","S164:TSLA","S168:TSLA","S167:TSLA","S166:TSLA","S163:TSLA","S350:TSLA","S351:TSLA"],"github_run":"9081","github_run_id":"33889345837","status":"ok","data_quality":{"clean":{"n":1021,"win":49.85,"med":0.0,"avg":47.56,"pnl":15480.96},"tainted":{"n":1787,"win":33.58,"med":-38.18,"avg":12.87,"pnl":-8580.84},"keep_only":{"n":546,"win":63.92,"med":51.18,"avg":73.83,"pnl":10150.45},"keep_only_recent":{"n":338,"win":60.65,"med":53.78,"avg":90.74,"pnl":4893.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
15:26:37  INFO      Mode: exits
15:26:37  INFO        place_all_stops: checking 3 positions...
15:26:37  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
15:26:37  INFO        STOP skipped APD: fractional (0.1144 shares) — software exit will handle it
15:26:37  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
15:26:37  INFO        [positions] 3/3 (3 valid)
15:26:37  INFO        Daily log -> logs/daily/2026-09-04.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.42|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMZN  P&L +0.2%  $+0.06                                           HOLD|
|  APD  P&L +0.4%  $+0.14                                            HOLD|
|  LII  P&L +0.7%  $+0.25                                            HOLD|
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
=== options_live_micro LIVE 2026-09-04T11:26:38.392798-04:00 share=25% ===
2026-09-04 11:26:38,392 INFO === options_live_micro LIVE 2026-09-04T11:26:38.392798-04:00 share=25% ===
Live account equity $230.42 cash $126.25 #225458845 options_level=3
2026-09-04 11:26:38,434 INFO Live account equity $230.42 cash $126.25 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-04 11:26:38,463 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-04 11:26:38,476 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (280 earlier lines - see full log file)
| w2     |    7 |    6 |   12 |    7 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    54 |
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 245 | 12 |
| S164 | 261 | 13 |
| S165 | 1703 | 26 |
| S166 | 135 | 9 |
| S167 | 257 | 13 |
| S168 | 188 | 11 |
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
| 2026-09-04 |   12 |   12 |    8 |   10 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    58 |

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
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |   152 | INFO |
| Total closed lots           |  1989 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1021 med=+0.0% | TAINTED n=1787 med=-38.2% | KEEP-only n=546 med=+51.2% | KILL=17 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.42 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260904T153143Z

- UTC timestamp: `20260904T153143Z`
- GitHub run: [#9082](https://github.com/28twagg-ops/TradingBot/actions/runs/33889824768)
- Run id: `33889824768`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`206s`
- Full logs: `logs/action_runs/20260904T153143Z_live_bot.log`, `logs/action_runs/20260904T153143Z_live_options.log`, `logs/action_runs/20260904T153143Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1021 | 49.9 | +0.0 | +47.5 | $+15,486 |
| TAINTED | 1788 | 33.6 | -38.3 | +12.8 | $-8,598 |
| KEEP-only | 547 | 63.8 | +51.0 | +73.6 | $+10,140 |
| KEEP-only recent | 339 | 60.5 | +53.6 | +90.3 | $+4,883 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (17): ORPHAN, S164, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T11:31:50.008083-04:00","date":"2026-09-04","mode":"entry+manage","header":"entry+manage (8 new)","elapsed_s":195.1,"phases_s":{"reconcile":1.25,"cancel":0.03,"manage":9.49,"protective_stops":1.25,"scan":46.84,"entries":109.84,"reconcile2":3.6},"signals":308,"placed":8,"equity":1004969.56,"open_positions":48,"pending_orders":8,"open_lots":163,"submitted_today":146,"filled_today":186,"unattributed_contracts":0,"top_signals":["S165:TSLA","S164:TSLA","S168:TSLA","S167:TSLA","S166:TSLA","S163:TSLA","S350:TSLA","S351:TSLA"],"github_run":"9082","github_run_id":"33889824768","status":"ok","data_quality":{"clean":{"n":1021,"win":49.85,"med":0.0,"avg":47.55,"pnl":15485.96},"tainted":{"n":1788,"win":33.56,"med":-38.25,"avg":12.83,"pnl":-8597.84},"keep_only":{"n":547,"win":63.8,"med":50.98,"avg":73.59,"pnl":10140.45},"keep_only_recent":{"n":339,"win":60.47,"med":53.57,"avg":90.3,"pnl":4883.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
15:31:44  INFO      Mode: exits
15:31:44  INFO        place_all_stops: checking 3 positions...
15:31:44  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
15:31:44  INFO        STOP skipped APD: fractional (0.1144 shares) — software exit will handle it
15:31:44  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
15:31:45  INFO        [positions] 3/3 (3 valid)
15:31:45  INFO        Daily log -> logs/daily/2026-09-04.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.38|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMZN  P&L +0.1%  $+0.05                                           HOLD|
|  APD  P&L +0.3%  $+0.10                                            HOLD|
|  LII  P&L +0.7%  $+0.25                                            HOLD|
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
=== options_live_micro LIVE 2026-09-04T11:31:46.720073-04:00 share=25% ===
2026-09-04 11:31:46,720 INFO === options_live_micro LIVE 2026-09-04T11:31:46.720073-04:00 share=25% ===
Live account equity $230.37 cash $126.25 #225458845 options_level=3
2026-09-04 11:31:46,777 INFO Live account equity $230.37 cash $126.25 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-04 11:31:46,855 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-04 11:31:46,879 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (269 earlier lines - see full log file)
| w2     |    7 |    6 |   12 |    7 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    54 |
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    5 |   10 |    3 |    5 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 245 | 12 |
| S164 | 265 | 13 |
| S165 | 1703 | 26 |
| S166 | 135 | 9 |
| S167 | 257 | 13 |
| S168 | 188 | 11 |
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
| 2026-09-04 |   12 |   16 |    8 |   10 |    8 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    62 |

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
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |   163 | INFO |
| Total closed lots           |  1990 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1021 med=+0.0% | TAINTED n=1788 med=-38.3% | KEEP-only n=547 med=+51.0% | KILL=17 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.37 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260904T153623Z

- UTC timestamp: `20260904T153623Z`
- GitHub run: [#9083](https://github.com/28twagg-ops/TradingBot/actions/runs/33890309756)
- Run id: `33890309756`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`32s`
- Full logs: `logs/action_runs/20260904T153623Z_live_bot.log`, `logs/action_runs/20260904T153623Z_live_options.log`, `logs/action_runs/20260904T153623Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1021 | 49.9 | +0.0 | +47.6 | $+15,481 |
| TAINTED | 1789 | 33.5 | -38.3 | +12.8 | $-8,597 |
| KEEP-only | 546 | 63.9 | +51.2 | +73.8 | $+10,150 |
| KEEP-only recent | 338 | 60.7 | +53.8 | +90.7 | $+4,893 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (17): ORPHAN, S164, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T11:36:29.359253-04:00","date":"2026-09-04","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":22.2,"phases_s":{"reconcile":0.86,"cancel":0.71,"manage":15.37,"protective_stops":4.71},"signals":0,"placed":0,"equity":1005086.28,"open_positions":47,"pending_orders":4,"open_lots":162,"submitted_today":143,"filled_today":186,"unattributed_contracts":0,"top_signals":[],"github_run":"9083","github_run_id":"33890309756","status":"ok","data_quality":{"clean":{"n":1021,"win":49.85,"med":0.0,"avg":47.56,"pnl":15480.96},"tainted":{"n":1789,"win":33.54,"med":-38.33,"avg":12.79,"pnl":-8596.84},"keep_only":{"n":546,"win":63.92,"med":51.18,"avg":73.83,"pnl":10150.45},"keep_only_recent":{"n":338,"win":60.65,"med":53.78,"avg":90.74,"pnl":4893.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
15:36:24  INFO      Mode: exits
15:36:24  INFO        place_all_stops: checking 3 positions...
15:36:24  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
15:36:24  INFO        STOP skipped APD: fractional (0.1144 shares) — software exit will handle it
15:36:24  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
15:36:25  INFO        [positions] 3/3 (3 valid)
15:36:25  INFO        Daily log -> logs/daily/2026-09-04.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.38|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMZN  P&L +0.2%  $+0.07                                           HOLD|
|  APD  P&L +0.2%  $+0.08                                            HOLD|
|  LII  P&L +0.8%  $+0.26                                            HOLD|
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
=== options_live_micro LIVE 2026-09-04T11:36:26.387634-04:00 share=25% ===
2026-09-04 11:36:26,387 INFO === options_live_micro LIVE 2026-09-04T11:36:26.387634-04:00 share=25% ===
Live account equity $230.38 cash $126.25 #225458845 options_level=3
2026-09-04 11:36:26,603 INFO Live account equity $230.38 cash $126.25 #225458845 options_level=3
Live micro: manage/exits only
2026-09-04 11:36:26,783 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-04 11:36:26,841 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (186 earlier lines - see full log file)
| w2     |    7 |    6 |   12 |    7 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    54 |
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 245 | 12 |
| S164 | 263 | 13 |
| S165 | 1703 | 26 |
| S166 | 135 | 9 |
| S167 | 257 | 13 |
| S168 | 190 | 11 |
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
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |   162 | INFO |
| Total closed lots           |  1991 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1021 med=+0.0% | TAINTED n=1789 med=-38.3% | KEEP-only n=546 med=+51.2% | KILL=17 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.38 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260904T154101Z

- UTC timestamp: `20260904T154101Z`
- GitHub run: [#9084](https://github.com/28twagg-ops/TradingBot/actions/runs/33890785182)
- Run id: `33890785182`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`24s`
- Full logs: `logs/action_runs/20260904T154101Z_live_bot.log`, `logs/action_runs/20260904T154101Z_live_options.log`, `logs/action_runs/20260904T154101Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1022 | 49.8 | +0.0 | +47.5 | $+15,460 |
| TAINTED | 1789 | 33.5 | -38.3 | +12.8 | $-8,597 |
| KEEP-only | 546 | 63.9 | +51.2 | +73.8 | $+10,150 |
| KEEP-only recent | 338 | 60.7 | +53.8 | +90.7 | $+4,893 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T11:41:07.021391-04:00","date":"2026-09-04","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":12.4,"phases_s":{"reconcile":0.34,"cancel":0.05,"manage":10.18,"protective_stops":1.2},"signals":0,"placed":0,"equity":1005333.24,"open_positions":47,"pending_orders":0,"open_lots":160,"submitted_today":143,"filled_today":186,"unattributed_contracts":0,"top_signals":[],"github_run":"9084","github_run_id":"33890785182","status":"ok","data_quality":{"clean":{"n":1022,"win":49.8,"med":0.0,"avg":47.47,"pnl":15459.96},"tainted":{"n":1789,"win":33.54,"med":-38.33,"avg":12.79,"pnl":-8596.84},"keep_only":{"n":546,"win":63.92,"med":51.18,"avg":73.83,"pnl":10150.45},"keep_only_recent":{"n":338,"win":60.65,"med":53.78,"avg":90.74,"pnl":4893.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
15:41:02  INFO      Mode: exits
15:41:02  INFO        place_all_stops: checking 3 positions...
15:41:02  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
15:41:02  INFO        STOP skipped APD: fractional (0.1144 shares) — software exit will handle it
15:41:02  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
15:41:03  INFO        [positions] 3/3 (3 valid)
15:41:03  INFO        Daily log -> logs/daily/2026-09-04.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.35|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMZN  P&L +0.1%  $+0.05                                           HOLD|
|  APD  P&L +0.2%  $+0.06                                            HOLD|
|  LII  P&L +0.8%  $+0.27                                            HOLD|
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
=== options_live_micro LIVE 2026-09-04T11:41:04.181035-04:00 share=25% ===
2026-09-04 11:41:04,181 INFO === options_live_micro LIVE 2026-09-04T11:41:04.181035-04:00 share=25% ===
Live account equity $230.35 cash $126.25 #225458845 options_level=3
2026-09-04 11:41:04,242 INFO Live account equity $230.35 cash $126.25 #225458845 options_level=3
Live micro: manage/exits only
2026-09-04 11:41:04,313 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-04 11:41:04,328 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
| w2     |    7 |    6 |   12 |    7 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    54 |
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 245 | 12 |
| S164 | 263 | 13 |
| S165 | 1703 | 26 |
| S166 | 135 | 9 |
| S167 | 257 | 13 |
| S168 | 190 | 11 |
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
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |   160 | INFO |
| Total closed lots           |  1992 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1022 med=+0.0% | TAINTED n=1789 med=-38.3% | KEEP-only n=546 med=+51.2% | KILL=18 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.35 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260904T154558Z

- UTC timestamp: `20260904T154558Z`
- GitHub run: [#9085](https://github.com/28twagg-ops/TradingBot/actions/runs/33891264095)
- Run id: `33891264095`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`32s`
- Full logs: `logs/action_runs/20260904T154558Z_live_bot.log`, `logs/action_runs/20260904T154558Z_live_options.log`, `logs/action_runs/20260904T154558Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1022 | 49.8 | +0.0 | +47.5 | $+15,460 |
| TAINTED | 1789 | 33.5 | -38.3 | +12.8 | $-8,597 |
| KEEP-only | 546 | 63.9 | +51.2 | +73.8 | $+10,150 |
| KEEP-only recent | 338 | 60.7 | +53.8 | +90.7 | $+4,893 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T11:46:07.101487-04:00","date":"2026-09-04","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":21.8,"phases_s":{"reconcile":0.48,"cancel":0.2,"manage":15.32,"protective_stops":5.12},"signals":0,"placed":0,"equity":1005456.22,"open_positions":48,"pending_orders":0,"open_lots":160,"submitted_today":143,"filled_today":186,"unattributed_contracts":0,"top_signals":[],"github_run":"9085","github_run_id":"33891264095","status":"ok","data_quality":{"clean":{"n":1022,"win":49.8,"med":0.0,"avg":47.47,"pnl":15459.96},"tainted":{"n":1789,"win":33.54,"med":-38.33,"avg":12.79,"pnl":-8596.84},"keep_only":{"n":546,"win":63.92,"med":51.18,"avg":73.83,"pnl":10150.45},"keep_only_recent":{"n":338,"win":60.65,"med":53.78,"avg":90.74,"pnl":4893.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
15:46:01  INFO      Mode: exits
15:46:01  INFO        place_all_stops: checking 3 positions...
15:46:01  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
15:46:01  INFO        STOP skipped APD: fractional (0.1144 shares) — software exit will handle it
15:46:01  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
15:46:02  INFO        [positions] 3/3 (3 valid)
15:46:02  INFO        Daily log -> logs/daily/2026-09-04.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.41|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  APD  P&L +0.1%  $+0.04                                            HOLD|
|  AMZN  P&L +0.2%  $+0.07                                           HOLD|
|  LII  P&L +0.9%  $+0.33                                            HOLD|
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
=== options_live_micro LIVE 2026-09-04T11:46:03.496460-04:00 share=25% ===
2026-09-04 11:46:03,496 INFO === options_live_micro LIVE 2026-09-04T11:46:03.496460-04:00 share=25% ===
Live account equity $230.41 cash $126.25 #225458845 options_level=3
2026-09-04 11:46:03,718 INFO Live account equity $230.41 cash $126.25 #225458845 options_level=3
Live micro: manage/exits only
2026-09-04 11:46:03,904 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-04 11:46:03,967 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (167 earlier lines - see full log file)
| w2     |    7 |    6 |   12 |    7 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    54 |
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 245 | 12 |
| S164 | 263 | 13 |
| S165 | 1703 | 26 |
| S166 | 135 | 9 |
| S167 | 257 | 13 |
| S168 | 190 | 11 |
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
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |   160 | INFO |
| Total closed lots           |  1992 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1022 med=+0.0% | TAINTED n=1789 med=-38.3% | KEEP-only n=546 med=+51.2% | KILL=18 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.41 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260904T155101Z

- UTC timestamp: `20260904T155101Z`
- GitHub run: [#9086](https://github.com/28twagg-ops/TradingBot/actions/runs/33891737351)
- Run id: `33891737351`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`33s`
- Full logs: `logs/action_runs/20260904T155101Z_live_bot.log`, `logs/action_runs/20260904T155101Z_live_options.log`, `logs/action_runs/20260904T155101Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1022 | 49.8 | +0.0 | +47.5 | $+15,460 |
| TAINTED | 1789 | 33.5 | -38.3 | +12.8 | $-8,597 |
| KEEP-only | 546 | 63.9 | +51.2 | +73.8 | $+10,150 |
| KEEP-only recent | 338 | 60.7 | +53.8 | +90.7 | $+4,893 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T11:51:08.479180-04:00","date":"2026-09-04","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":21.9,"phases_s":{"reconcile":0.44,"cancel":0.2,"manage":15.32,"protective_stops":5.13},"signals":0,"placed":0,"equity":1005348.2,"open_positions":46,"pending_orders":0,"open_lots":159,"submitted_today":143,"filled_today":186,"unattributed_contracts":0,"top_signals":[],"github_run":"9086","github_run_id":"33891737351","status":"ok","data_quality":{"clean":{"n":1022,"win":49.8,"med":0.0,"avg":47.47,"pnl":15459.96},"tainted":{"n":1789,"win":33.54,"med":-38.33,"avg":12.79,"pnl":-8596.84},"keep_only":{"n":546,"win":63.92,"med":51.18,"avg":73.83,"pnl":10150.45},"keep_only_recent":{"n":338,"win":60.65,"med":53.78,"avg":90.74,"pnl":4893.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
15:51:02  INFO      Mode: exits
15:51:02  INFO        place_all_stops: checking 3 positions...
15:51:02  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
15:51:02  INFO        STOP skipped APD: fractional (0.1144 shares) — software exit will handle it
15:51:02  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
15:51:03  INFO        [positions] 3/3 (3 valid)
15:51:04  INFO        Daily log -> logs/daily/2026-09-04.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:51 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.40|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  APD  P&L +0.1%  $+0.05                                            HOLD|
|  AMZN  P&L +0.2%  $+0.08                                           HOLD|
|  LII  P&L +0.9%  $+0.30                                            HOLD|
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
=== options_live_micro LIVE 2026-09-04T11:51:04.921576-04:00 share=25% ===
2026-09-04 11:51:04,921 INFO === options_live_micro LIVE 2026-09-04T11:51:04.921576-04:00 share=25% ===
Live account equity $230.40 cash $126.25 #225458845 options_level=3
2026-09-04 11:51:05,134 INFO Live account equity $230.40 cash $126.25 #225458845 options_level=3
Live micro: manage/exits only
2026-09-04 11:51:05,327 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-04 11:51:05,388 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (173 earlier lines - see full log file)
| w2     |    7 |    6 |   12 |    7 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    54 |
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 245 | 12 |
| S164 | 263 | 13 |
| S165 | 1703 | 26 |
| S166 | 135 | 9 |
| S167 | 257 | 13 |
| S168 | 190 | 11 |
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
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |   159 | INFO |
| Total closed lots           |  1992 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1022 med=+0.0% | TAINTED n=1789 med=-38.3% | KEEP-only n=546 med=+51.2% | KILL=18 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.4 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260904T155600Z

- UTC timestamp: `20260904T155600Z`
- GitHub run: [#9087](https://github.com/28twagg-ops/TradingBot/actions/runs/33892201361)
- Run id: `33892201361`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`30s`
- Full logs: `logs/action_runs/20260904T155600Z_live_bot.log`, `logs/action_runs/20260904T155600Z_live_options.log`, `logs/action_runs/20260904T155600Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1022 | 49.8 | +0.0 | +47.5 | $+15,460 |
| TAINTED | 1789 | 33.5 | -38.3 | +12.8 | $-8,597 |
| KEEP-only | 546 | 63.9 | +51.2 | +73.8 | $+10,150 |
| KEEP-only recent | 338 | 60.7 | +53.8 | +90.7 | $+4,893 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T11:56:07.282933-04:00","date":"2026-09-04","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":20.6,"phases_s":{"reconcile":0.61,"cancel":0.2,"manage":14.26,"protective_stops":4.9},"signals":0,"placed":0,"equity":1005342.18,"open_positions":46,"pending_orders":0,"open_lots":158,"submitted_today":143,"filled_today":186,"unattributed_contracts":0,"top_signals":[],"github_run":"9087","github_run_id":"33892201361","status":"ok","data_quality":{"clean":{"n":1022,"win":49.8,"med":0.0,"avg":47.47,"pnl":15459.96},"tainted":{"n":1789,"win":33.54,"med":-38.33,"avg":12.79,"pnl":-8596.84},"keep_only":{"n":546,"win":63.92,"med":51.18,"avg":73.83,"pnl":10150.45},"keep_only_recent":{"n":338,"win":60.65,"med":53.78,"avg":90.74,"pnl":4893.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
15:56:02  INFO      Mode: exits
15:56:02  INFO        place_all_stops: checking 3 positions...
15:56:02  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
15:56:02  INFO        STOP skipped APD: fractional (0.1144 shares) — software exit will handle it
15:56:02  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
15:56:03  INFO        [positions] 3/3 (3 valid)
15:56:03  INFO        Daily log -> logs/daily/2026-09-04.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:56 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.45|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  APD  P&L +0.2%  $+0.07                                            HOLD|
|  AMZN  P&L +0.3%  $+0.10                                           HOLD|
|  LII  P&L +0.9%  $+0.31                                            HOLD|
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
=== options_live_micro LIVE 2026-09-04T11:56:04.257177-04:00 share=25% ===
2026-09-04 11:56:04,257 INFO === options_live_micro LIVE 2026-09-04T11:56:04.257177-04:00 share=25% ===
Live account equity $230.45 cash $126.25 #225458845 options_level=3
2026-09-04 11:56:04,495 INFO Live account equity $230.45 cash $126.25 #225458845 options_level=3
Live micro: manage/exits only
2026-09-04 11:56:04,686 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-04 11:56:04,748 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (167 earlier lines - see full log file)
| w2     |    7 |    6 |   12 |    7 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    54 |
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 245 | 12 |
| S164 | 263 | 13 |
| S165 | 1703 | 26 |
| S166 | 135 | 9 |
| S167 | 257 | 13 |
| S168 | 190 | 11 |
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
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |   158 | INFO |
| Total closed lots           |  1992 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1022 med=+0.0% | TAINTED n=1789 med=-38.3% | KEEP-only n=546 med=+51.2% | KILL=18 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.45 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260904T160112Z

- UTC timestamp: `20260904T160112Z`
- GitHub run: [#9088](https://github.com/28twagg-ops/TradingBot/actions/runs/33892659022)
- Run id: `33892659022`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`33s`
- Full logs: `logs/action_runs/20260904T160112Z_live_bot.log`, `logs/action_runs/20260904T160112Z_live_options.log`, `logs/action_runs/20260904T160112Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1022 | 49.8 | +0.0 | +47.5 | $+15,460 |
| TAINTED | 1789 | 33.5 | -38.3 | +12.8 | $-8,597 |
| KEEP-only | 546 | 63.9 | +51.2 | +73.8 | $+10,150 |
| KEEP-only recent | 338 | 60.7 | +53.8 | +90.7 | $+4,893 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T12:01:21.164150-04:00","date":"2026-09-04","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":20.4,"phases_s":{"reconcile":0.47,"cancel":0.18,"manage":14.77,"protective_stops":4.26},"signals":0,"placed":0,"equity":1005310.16,"open_positions":47,"pending_orders":0,"open_lots":158,"submitted_today":143,"filled_today":186,"unattributed_contracts":0,"top_signals":[],"github_run":"9088","github_run_id":"33892659022","status":"ok","data_quality":{"clean":{"n":1022,"win":49.8,"med":0.0,"avg":47.47,"pnl":15459.96},"tainted":{"n":1789,"win":33.54,"med":-38.33,"avg":12.79,"pnl":-8596.84},"keep_only":{"n":546,"win":63.92,"med":51.18,"avg":73.83,"pnl":10150.45},"keep_only_recent":{"n":338,"win":60.65,"med":53.78,"avg":90.74,"pnl":4893.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
16:01:13  INFO      Mode: exits
16:01:14  INFO        place_all_stops: checking 3 positions...
16:01:14  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
16:01:14  INFO        STOP skipped APD: fractional (0.1144 shares) — software exit will handle it
16:01:14  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
16:01:15  INFO        [positions] 3/3 (3 valid)
16:01:15  INFO        Daily log -> logs/daily/2026-09-04.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.42|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  APD  P&L +0.2%  $+0.06                                            HOLD|
|  AMZN  P&L +0.2%  $+0.06                                           HOLD|
|  LII  P&L +1.0%  $+0.33                                            HOLD|
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
=== options_live_micro LIVE 2026-09-04T12:01:16.752954-04:00 share=25% ===
2026-09-04 12:01:16,753 INFO === options_live_micro LIVE 2026-09-04T12:01:16.752954-04:00 share=25% ===
Live account equity $230.42 cash $126.25 #225458845 options_level=3
2026-09-04 12:01:16,972 INFO Live account equity $230.42 cash $126.25 #225458845 options_level=3
Live micro: manage/exits only
2026-09-04 12:01:17,212 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-04 12:01:17,270 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (165 earlier lines - see full log file)
| w2     |    7 |    6 |   12 |    7 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    54 |
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 245 | 12 |
| S164 | 263 | 13 |
| S165 | 1703 | 26 |
| S166 | 135 | 9 |
| S167 | 257 | 13 |
| S168 | 190 | 11 |
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
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |   158 | INFO |
| Total closed lots           |  1992 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1022 med=+0.0% | TAINTED n=1789 med=-38.3% | KEEP-only n=546 med=+51.2% | KILL=18 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.42 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260904T160559Z

- UTC timestamp: `20260904T160559Z`
- GitHub run: [#9089](https://github.com/28twagg-ops/TradingBot/actions/runs/33893136306)
- Run id: `33893136306`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`33s`
- Full logs: `logs/action_runs/20260904T160559Z_live_bot.log`, `logs/action_runs/20260904T160559Z_live_options.log`, `logs/action_runs/20260904T160559Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1022 | 49.8 | +0.0 | +47.5 | $+15,460 |
| TAINTED | 1789 | 33.5 | -38.3 | +12.8 | $-8,597 |
| KEEP-only | 546 | 63.9 | +51.2 | +73.8 | $+10,150 |
| KEEP-only recent | 338 | 60.7 | +53.8 | +90.7 | $+4,893 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T12:06:07.379657-04:00","date":"2026-09-04","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":21.3,"phases_s":{"reconcile":0.55,"cancel":0.19,"manage":15.08,"protective_stops":4.51},"signals":0,"placed":0,"equity":1005297.16,"open_positions":47,"pending_orders":0,"open_lots":158,"submitted_today":143,"filled_today":186,"unattributed_contracts":0,"top_signals":[],"github_run":"9089","github_run_id":"33893136306","status":"ok","data_quality":{"clean":{"n":1022,"win":49.8,"med":0.0,"avg":47.47,"pnl":15459.96},"tainted":{"n":1789,"win":33.54,"med":-38.33,"avg":12.79,"pnl":-8596.84},"keep_only":{"n":546,"win":63.92,"med":51.18,"avg":73.83,"pnl":10150.45},"keep_only_recent":{"n":338,"win":60.65,"med":53.78,"avg":90.74,"pnl":4893.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
16:06:00  INFO      Mode: exits
16:06:01  INFO        place_all_stops: checking 3 positions...
16:06:01  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
16:06:01  INFO        STOP skipped APD: fractional (0.1144 shares) — software exit will handle it
16:06:01  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
16:06:02  INFO        [positions] 3/3 (3 valid)
16:06:02  INFO        Daily log -> logs/daily/2026-09-04.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.47|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AMZN  P&L +0.2%  $+0.07                                           HOLD|
|  APD  P&L +0.2%  $+0.07                                            HOLD|
|  LII  P&L +1.0%  $+0.36                                            HOLD|
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
=== options_live_micro LIVE 2026-09-04T12:06:03.629079-04:00 share=25% ===
2026-09-04 12:06:03,629 INFO === options_live_micro LIVE 2026-09-04T12:06:03.629079-04:00 share=25% ===
Live account equity $230.47 cash $126.25 #225458845 options_level=3
2026-09-04 12:06:03,857 INFO Live account equity $230.47 cash $126.25 #225458845 options_level=3
Live micro: manage/exits only
2026-09-04 12:06:04,033 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-04 12:06:04,097 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (165 earlier lines - see full log file)
| w2     |    7 |    6 |   12 |    7 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    54 |
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 245 | 12 |
| S164 | 263 | 13 |
| S165 | 1703 | 26 |
| S166 | 135 | 9 |
| S167 | 257 | 13 |
| S168 | 190 | 11 |
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
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |   158 | INFO |
| Total closed lots           |  1992 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1022 med=+0.0% | TAINTED n=1789 med=-38.3% | KEEP-only n=546 med=+51.2% | KILL=18 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.47 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260904T161121Z

- UTC timestamp: `20260904T161121Z`
- GitHub run: [#9090](https://github.com/28twagg-ops/TradingBot/actions/runs/33893601485)
- Run id: `33893601485`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`22s`
- Full logs: `logs/action_runs/20260904T161121Z_live_bot.log`, `logs/action_runs/20260904T161121Z_live_options.log`, `logs/action_runs/20260904T161121Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1022 | 49.8 | +0.0 | +47.5 | $+15,460 |
| TAINTED | 1789 | 33.5 | -38.3 | +12.8 | $-8,597 |
| KEEP-only | 546 | 63.9 | +51.2 | +73.8 | $+10,150 |
| KEEP-only recent | 338 | 60.7 | +53.8 | +90.7 | $+4,893 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T12:11:25.926950-04:00","date":"2026-09-04","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":10.9,"phases_s":{"reconcile":0.13,"cancel":0.07,"manage":9.2,"protective_stops":1.0},"signals":0,"placed":0,"equity":1005328.16,"open_positions":47,"pending_orders":0,"open_lots":158,"submitted_today":143,"filled_today":186,"unattributed_contracts":0,"top_signals":[],"github_run":"9090","github_run_id":"33893601485","status":"ok","data_quality":{"clean":{"n":1022,"win":49.8,"med":0.0,"avg":47.47,"pnl":15459.96},"tainted":{"n":1789,"win":33.54,"med":-38.33,"avg":12.79,"pnl":-8596.84},"keep_only":{"n":546,"win":63.92,"med":51.18,"avg":73.83,"pnl":10150.45},"keep_only_recent":{"n":338,"win":60.65,"med":53.78,"avg":90.74,"pnl":4893.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
16:11:21  INFO      Mode: exits
16:11:22  INFO        place_all_stops: checking 3 positions...
16:11:22  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
16:11:22  INFO        STOP skipped APD: fractional (0.1144 shares) — software exit will handle it
16:11:22  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
16:11:22  INFO        [positions] 3/3 (3 valid)
16:11:22  INFO        Daily log -> logs/daily/2026-09-04.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.47|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  APD  P&L +0.2%  $+0.05                                            HOLD|
|  AMZN  P&L +0.2%  $+0.08                                           HOLD|
|  LII  P&L +1.0%  $+0.36                                            HOLD|
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
=== options_live_micro LIVE 2026-09-04T12:11:23.233708-04:00 share=25% ===
2026-09-04 12:11:23,233 INFO === options_live_micro LIVE 2026-09-04T12:11:23.233708-04:00 share=25% ===
Live account equity $230.47 cash $126.25 #225458845 options_level=3
2026-09-04 12:11:23,292 INFO Live account equity $230.47 cash $126.25 #225458845 options_level=3
Live micro: manage/exits only
2026-09-04 12:11:23,327 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-04 12:11:23,340 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (165 earlier lines - see full log file)
| w2     |    7 |    6 |   12 |    7 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    54 |
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 245 | 12 |
| S164 | 263 | 13 |
| S165 | 1703 | 26 |
| S166 | 135 | 9 |
| S167 | 257 | 13 |
| S168 | 190 | 11 |
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
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |   158 | INFO |
| Total closed lots           |  1992 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1022 med=+0.0% | TAINTED n=1789 med=-38.3% | KEEP-only n=546 med=+51.2% | KILL=18 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.47 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260904T161602Z

- UTC timestamp: `20260904T161602Z`
- GitHub run: [#9091](https://github.com/28twagg-ops/TradingBot/actions/runs/33894070416)
- Run id: `33894070416`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`36s`
- Full logs: `logs/action_runs/20260904T161602Z_live_bot.log`, `logs/action_runs/20260904T161602Z_live_options.log`, `logs/action_runs/20260904T161602Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1022 | 49.8 | +0.0 | +47.5 | $+15,460 |
| TAINTED | 1789 | 33.5 | -38.3 | +12.8 | $-8,597 |
| KEEP-only | 546 | 63.9 | +51.2 | +73.8 | $+10,150 |
| KEEP-only recent | 338 | 60.7 | +53.8 | +90.7 | $+4,893 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T12:16:10.631735-04:00","date":"2026-09-04","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":23.4,"phases_s":{"reconcile":0.51,"cancel":0.22,"manage":16.67,"protective_stops":5.18},"signals":0,"placed":0,"equity":1005311.94,"open_positions":46,"pending_orders":0,"open_lots":149,"submitted_today":143,"filled_today":186,"unattributed_contracts":0,"top_signals":[],"github_run":"9091","github_run_id":"33894070416","status":"ok","data_quality":{"clean":{"n":1022,"win":49.8,"med":0.0,"avg":47.47,"pnl":15459.96},"tainted":{"n":1789,"win":33.54,"med":-38.33,"avg":12.79,"pnl":-8596.84},"keep_only":{"n":546,"win":63.92,"med":51.18,"avg":73.83,"pnl":10150.45},"keep_only_recent":{"n":338,"win":60.65,"med":53.78,"avg":90.74,"pnl":4893.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
16:16:03  INFO      Mode: exits
16:16:04  INFO        place_all_stops: checking 3 positions...
16:16:04  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
16:16:04  INFO        STOP skipped APD: fractional (0.1144 shares) — software exit will handle it
16:16:04  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
16:16:04  INFO        [positions] 3/3 (3 valid)
16:16:05  INFO        Daily log -> logs/daily/2026-09-04.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.54|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  APD  P&L +0.2%  $+0.06                                            HOLD|
|  AMZN  P&L +0.4%  $+0.14                                           HOLD|
|  LII  P&L +1.1%  $+0.36                                            HOLD|
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
=== options_live_micro LIVE 2026-09-04T12:16:06.141222-04:00 share=25% ===
2026-09-04 12:16:06,141 INFO === options_live_micro LIVE 2026-09-04T12:16:06.141222-04:00 share=25% ===
Live account equity $230.53 cash $126.25 #225458845 options_level=3
2026-09-04 12:16:06,385 INFO Live account equity $230.53 cash $126.25 #225458845 options_level=3
Live micro: manage/exits only
2026-09-04 12:16:06,626 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-04 12:16:06,698 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (181 earlier lines - see full log file)
| w2     |    7 |    6 |   12 |    7 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    54 |
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 245 | 12 |
| S164 | 263 | 13 |
| S165 | 1703 | 26 |
| S166 | 135 | 9 |
| S167 | 257 | 13 |
| S168 | 190 | 11 |
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
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |   149 | INFO |
| Total closed lots           |  1992 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1022 med=+0.0% | TAINTED n=1789 med=-38.3% | KEEP-only n=546 med=+51.2% | KILL=18 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.53 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260904T162134Z

- UTC timestamp: `20260904T162134Z`
- GitHub run: [#9092](https://github.com/28twagg-ops/TradingBot/actions/runs/33894532935)
- Run id: `33894532935`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`26s`
- Full logs: `logs/action_runs/20260904T162134Z_live_bot.log`, `logs/action_runs/20260904T162134Z_live_options.log`, `logs/action_runs/20260904T162134Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1023 | 49.9 | +0.0 | +47.5 | $+15,481 |
| TAINTED | 1790 | 33.5 | -38.3 | +12.8 | $-8,613 |
| KEEP-only | 547 | 64.0 | +51.0 | +73.8 | $+10,171 |
| KEEP-only recent | 339 | 60.8 | +53.6 | +90.6 | $+4,914 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T12:21:40.422717-04:00","date":"2026-09-04","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":16.2,"phases_s":{"reconcile":0.87,"cancel":0.13,"manage":10.76,"protective_stops":3.51},"signals":0,"placed":0,"equity":1005266.9,"open_positions":45,"pending_orders":0,"open_lots":147,"submitted_today":143,"filled_today":186,"unattributed_contracts":0,"top_signals":[],"github_run":"9092","github_run_id":"33894532935","status":"ok","data_quality":{"clean":{"n":1023,"win":49.85,"med":0.0,"avg":47.47,"pnl":15480.96},"tainted":{"n":1790,"win":33.52,"med":-38.34,"avg":12.76,"pnl":-8612.84},"keep_only":{"n":547,"win":63.99,"med":50.98,"avg":73.79,"pnl":10171.45},"keep_only_recent":{"n":339,"win":60.77,"med":53.57,"avg":90.62,"pnl":4914.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
16:21:35  INFO      Mode: exits
16:21:35  INFO        place_all_stops: checking 3 positions...
16:21:35  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
16:21:35  INFO        STOP skipped APD: fractional (0.1144 shares) — software exit will handle it
16:21:35  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
16:21:36  INFO        [positions] 3/3 (3 valid)
16:21:36  INFO        Daily log -> logs/daily/2026-09-04.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.64|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  APD  P&L +0.2%  $+0.07                                            HOLD|
|  AMZN  P&L +0.6%  $+0.21                                           HOLD|
|  LII  P&L +1.1%  $+0.39                                            HOLD|
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
=== options_live_micro LIVE 2026-09-04T12:21:37.196274-04:00 share=25% ===
2026-09-04 12:21:37,196 INFO === options_live_micro LIVE 2026-09-04T12:21:37.196274-04:00 share=25% ===
Live account equity $230.64 cash $126.25 #225458845 options_level=3
2026-09-04 12:21:37,343 INFO Live account equity $230.64 cash $126.25 #225458845 options_level=3
Live micro: manage/exits only
2026-09-04 12:21:37,534 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-04 12:21:37,564 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (172 earlier lines - see full log file)
| w2     |    7 |    6 |   12 |    7 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    54 |
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 245 | 12 |
| S164 | 263 | 13 |
| S165 | 1703 | 26 |
| S166 | 135 | 9 |
| S167 | 257 | 13 |
| S168 | 190 | 11 |
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
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |   147 | INFO |
| Total closed lots           |  1994 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1023 med=+0.0% | TAINTED n=1790 med=-38.3% | KEEP-only n=547 med=+51.0% | KILL=18 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.64 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260904T162601Z

- UTC timestamp: `20260904T162601Z`
- GitHub run: [#9093](https://github.com/28twagg-ops/TradingBot/actions/runs/33895008791)
- Run id: `33895008791`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`24s`
- Full logs: `logs/action_runs/20260904T162601Z_live_bot.log`, `logs/action_runs/20260904T162601Z_live_options.log`, `logs/action_runs/20260904T162601Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1023 | 49.9 | +0.0 | +47.5 | $+15,481 |
| TAINTED | 1790 | 33.5 | -38.3 | +12.8 | $-8,613 |
| KEEP-only | 547 | 64.0 | +51.0 | +73.8 | $+10,171 |
| KEEP-only recent | 339 | 60.8 | +53.6 | +90.6 | $+4,914 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T12:26:07.305518-04:00","date":"2026-09-04","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":14.7,"phases_s":{"reconcile":0.29,"cancel":0.13,"manage":10.64,"protective_stops":3.14},"signals":0,"placed":0,"equity":1005184.88,"open_positions":45,"pending_orders":0,"open_lots":146,"submitted_today":143,"filled_today":186,"unattributed_contracts":0,"top_signals":[],"github_run":"9093","github_run_id":"33895008791","status":"ok","data_quality":{"clean":{"n":1023,"win":49.85,"med":0.0,"avg":47.47,"pnl":15480.96},"tainted":{"n":1790,"win":33.52,"med":-38.34,"avg":12.76,"pnl":-8612.84},"keep_only":{"n":547,"win":63.99,"med":50.98,"avg":73.79,"pnl":10171.45},"keep_only_recent":{"n":339,"win":60.77,"med":53.57,"avg":90.62,"pnl":4914.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
16:26:02  INFO      Mode: exits
16:26:03  INFO        place_all_stops: checking 3 positions...
16:26:03  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
16:26:03  INFO        STOP skipped APD: fractional (0.1144 shares) — software exit will handle it
16:26:03  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
16:26:03  INFO        [positions] 3/3 (3 valid)
16:26:03  INFO        Daily log -> logs/daily/2026-09-04.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.58|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  APD  P&L +0.2%  $+0.06                                            HOLD|
|  AMZN  P&L +0.6%  $+0.20                                           HOLD|
|  LII  P&L +1.0%  $+0.35                                            HOLD|
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
=== options_live_micro LIVE 2026-09-04T12:26:04.463447-04:00 share=25% ===
2026-09-04 12:26:04,463 INFO === options_live_micro LIVE 2026-09-04T12:26:04.463447-04:00 share=25% ===
Live account equity $230.58 cash $126.25 #225458845 options_level=3
2026-09-04 12:26:04,635 INFO Live account equity $230.58 cash $126.25 #225458845 options_level=3
Live micro: manage/exits only
2026-09-04 12:26:04,779 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-04 12:26:04,842 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (168 earlier lines - see full log file)
| w2     |    7 |    6 |   12 |    7 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    54 |
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 245 | 12 |
| S164 | 263 | 13 |
| S165 | 1703 | 26 |
| S166 | 135 | 9 |
| S167 | 257 | 13 |
| S168 | 190 | 11 |
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
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |   146 | INFO |
| Total closed lots           |  1994 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1023 med=+0.0% | TAINTED n=1790 med=-38.3% | KEEP-only n=547 med=+51.0% | KILL=18 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.58 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260904T163100Z

- UTC timestamp: `20260904T163100Z`
- GitHub run: [#9094](https://github.com/28twagg-ops/TradingBot/actions/runs/33895480647)
- Run id: `33895480647`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`25s`
- Full logs: `logs/action_runs/20260904T163100Z_live_bot.log`, `logs/action_runs/20260904T163100Z_live_options.log`, `logs/action_runs/20260904T163100Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1023 | 49.9 | +0.0 | +47.5 | $+15,481 |
| TAINTED | 1790 | 33.5 | -38.3 | +12.8 | $-8,613 |
| KEEP-only | 547 | 64.0 | +51.0 | +73.8 | $+10,171 |
| KEEP-only recent | 339 | 60.8 | +53.6 | +90.6 | $+4,914 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T12:31:06.325440-04:00","date":"2026-09-04","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":13.6,"phases_s":{"reconcile":0.49,"cancel":0.08,"manage":10.44,"protective_stops":1.92},"signals":0,"placed":0,"equity":1005112.88,"open_positions":45,"pending_orders":0,"open_lots":146,"submitted_today":143,"filled_today":186,"unattributed_contracts":0,"top_signals":[],"github_run":"9094","github_run_id":"33895480647","status":"ok","data_quality":{"clean":{"n":1023,"win":49.85,"med":0.0,"avg":47.47,"pnl":15480.96},"tainted":{"n":1790,"win":33.52,"med":-38.34,"avg":12.76,"pnl":-8612.84},"keep_only":{"n":547,"win":63.99,"med":50.98,"avg":73.79,"pnl":10171.45},"keep_only_recent":{"n":339,"win":60.77,"med":53.57,"avg":90.62,"pnl":4914.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
16:31:01  INFO      Mode: exits
16:31:01  INFO        place_all_stops: checking 3 positions...
16:31:01  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
16:31:01  INFO        STOP skipped APD: fractional (0.1144 shares) — software exit will handle it
16:31:01  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
16:31:02  INFO        [positions] 3/3 (3 valid)
16:31:02  INFO        Daily log -> logs/daily/2026-09-04.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.51|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  APD  P&L +0.1%  $+0.02                                            HOLD|
|  AMZN  P&L +0.7%  $+0.23                                           HOLD|
|  LII  P&L +0.8%  $+0.28                                            HOLD|
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
=== options_live_micro LIVE 2026-09-04T12:31:03.097989-04:00 share=25% ===
2026-09-04 12:31:03,098 INFO === options_live_micro LIVE 2026-09-04T12:31:03.097989-04:00 share=25% ===
Live account equity $230.51 cash $126.25 #225458845 options_level=3
2026-09-04 12:31:03,194 INFO Live account equity $230.51 cash $126.25 #225458845 options_level=3
Live micro: manage/exits only
2026-09-04 12:31:03,273 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-04 12:31:03,299 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (166 earlier lines - see full log file)
| w2     |    7 |    6 |   12 |    7 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    54 |
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 245 | 12 |
| S164 | 263 | 13 |
| S165 | 1703 | 26 |
| S166 | 135 | 9 |
| S167 | 257 | 13 |
| S168 | 190 | 11 |
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
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |   146 | INFO |
| Total closed lots           |  1994 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1023 med=+0.0% | TAINTED n=1790 med=-38.3% | KEEP-only n=547 med=+51.0% | KILL=18 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.51 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260904T163558Z

- UTC timestamp: `20260904T163558Z`
- GitHub run: [#9095](https://github.com/28twagg-ops/TradingBot/actions/runs/33895948221)
- Run id: `33895948221`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`33s`
- Full logs: `logs/action_runs/20260904T163558Z_live_bot.log`, `logs/action_runs/20260904T163558Z_live_options.log`, `logs/action_runs/20260904T163558Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1023 | 49.9 | +0.0 | +47.5 | $+15,481 |
| TAINTED | 1790 | 33.5 | -38.3 | +12.8 | $-8,613 |
| KEEP-only | 547 | 64.0 | +51.0 | +73.8 | $+10,171 |
| KEEP-only recent | 339 | 60.8 | +53.6 | +90.6 | $+4,914 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T12:36:05.702604-04:00","date":"2026-09-04","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":20.9,"phases_s":{"reconcile":0.43,"cancel":0.2,"manage":14.72,"protective_stops":4.73},"signals":0,"placed":0,"equity":1005135.88,"open_positions":45,"pending_orders":0,"open_lots":146,"submitted_today":143,"filled_today":186,"unattributed_contracts":0,"top_signals":[],"github_run":"9095","github_run_id":"33895948221","status":"ok","data_quality":{"clean":{"n":1023,"win":49.85,"med":0.0,"avg":47.47,"pnl":15480.96},"tainted":{"n":1790,"win":33.52,"med":-38.34,"avg":12.76,"pnl":-8612.84},"keep_only":{"n":547,"win":63.99,"med":50.98,"avg":73.79,"pnl":10171.45},"keep_only_recent":{"n":339,"win":60.77,"med":53.57,"avg":90.62,"pnl":4914.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
16:35:59  INFO      Mode: exits
16:36:00  INFO        place_all_stops: checking 3 positions...
16:36:00  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
16:36:00  INFO        STOP skipped APD: fractional (0.1144 shares) — software exit will handle it
16:36:00  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
16:36:00  INFO        [positions] 3/3 (3 valid)
16:36:01  INFO        Daily log -> logs/daily/2026-09-04.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.52|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  APD  P&L +0.1%  $+0.02                                            HOLD|
|  AMZN  P&L +0.7%  $+0.25                                           HOLD|
|  LII  P&L +0.8%  $+0.29                                            HOLD|
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
=== options_live_micro LIVE 2026-09-04T12:36:02.003683-04:00 share=25% ===
2026-09-04 12:36:02,003 INFO === options_live_micro LIVE 2026-09-04T12:36:02.003683-04:00 share=25% ===
Live account equity $230.52 cash $126.25 #225458845 options_level=3
2026-09-04 12:36:02,224 INFO Live account equity $230.52 cash $126.25 #225458845 options_level=3
Live micro: manage/exits only
2026-09-04 12:36:02,412 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-04 12:36:02,478 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (166 earlier lines - see full log file)
| w2     |    7 |    6 |   12 |    7 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    54 |
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 245 | 12 |
| S164 | 263 | 13 |
| S165 | 1703 | 26 |
| S166 | 135 | 9 |
| S167 | 257 | 13 |
| S168 | 190 | 11 |
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
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |   146 | INFO |
| Total closed lots           |  1994 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1023 med=+0.0% | TAINTED n=1790 med=-38.3% | KEEP-only n=547 med=+51.0% | KILL=18 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.52 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260904T164101Z

- UTC timestamp: `20260904T164101Z`
- GitHub run: [#9096](https://github.com/28twagg-ops/TradingBot/actions/runs/33896410758)
- Run id: `33896410758`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`28s`
- Full logs: `logs/action_runs/20260904T164101Z_live_bot.log`, `logs/action_runs/20260904T164101Z_live_options.log`, `logs/action_runs/20260904T164101Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1023 | 49.9 | +0.0 | +47.5 | $+15,481 |
| TAINTED | 1790 | 33.5 | -38.3 | +12.8 | $-8,613 |
| KEEP-only | 547 | 64.0 | +51.0 | +73.8 | $+10,171 |
| KEEP-only recent | 339 | 60.8 | +53.6 | +90.6 | $+4,914 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T12:41:07.540715-04:00","date":"2026-09-04","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":19.1,"phases_s":{"reconcile":0.43,"cancel":0.2,"manage":12.82,"protective_stops":4.95},"signals":0,"placed":0,"equity":1005124.88,"open_positions":45,"pending_orders":0,"open_lots":146,"submitted_today":143,"filled_today":186,"unattributed_contracts":0,"top_signals":[],"github_run":"9096","github_run_id":"33896410758","status":"ok","data_quality":{"clean":{"n":1023,"win":49.85,"med":0.0,"avg":47.47,"pnl":15480.96},"tainted":{"n":1790,"win":33.52,"med":-38.34,"avg":12.76,"pnl":-8612.84},"keep_only":{"n":547,"win":63.99,"med":50.98,"avg":73.79,"pnl":10171.45},"keep_only_recent":{"n":339,"win":60.77,"med":53.57,"avg":90.62,"pnl":4914.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
16:41:02  INFO      Mode: exits
16:41:02  INFO        place_all_stops: checking 3 positions...
16:41:02  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
16:41:02  INFO        STOP skipped APD: fractional (0.1144 shares) — software exit will handle it
16:41:02  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
16:41:03  INFO        [positions] 3/3 (3 valid)
16:41:03  INFO        Daily log -> logs/daily/2026-09-04.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.51|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  APD  P&L +0.0%  $+0.00                                            HOLD|
|  AMZN  P&L +0.6%  $+0.22                                           HOLD|
|  LII  P&L +0.9%  $+0.31                                            HOLD|
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
=== options_live_micro LIVE 2026-09-04T12:41:04.529433-04:00 share=25% ===
2026-09-04 12:41:04,529 INFO === options_live_micro LIVE 2026-09-04T12:41:04.529433-04:00 share=25% ===
Live account equity $230.51 cash $126.25 #225458845 options_level=3
2026-09-04 12:41:04,741 INFO Live account equity $230.51 cash $126.25 #225458845 options_level=3
Live micro: manage/exits only
2026-09-04 12:41:04,924 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-04 12:41:04,985 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (166 earlier lines - see full log file)
| w2     |    7 |    6 |   12 |    7 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    54 |
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 245 | 12 |
| S164 | 263 | 13 |
| S165 | 1703 | 26 |
| S166 | 135 | 9 |
| S167 | 257 | 13 |
| S168 | 190 | 11 |
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
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |   146 | INFO |
| Total closed lots           |  1994 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1023 med=+0.0% | TAINTED n=1790 med=-38.3% | KEEP-only n=547 med=+51.0% | KILL=18 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.51 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260904T164624Z

- UTC timestamp: `20260904T164624Z`
- GitHub run: [#9097](https://github.com/28twagg-ops/TradingBot/actions/runs/33896862960)
- Run id: `33896862960`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`32s`
- Full logs: `logs/action_runs/20260904T164624Z_live_bot.log`, `logs/action_runs/20260904T164624Z_live_options.log`, `logs/action_runs/20260904T164624Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1023 | 49.9 | +0.0 | +47.5 | $+15,481 |
| TAINTED | 1790 | 33.5 | -38.3 | +12.8 | $-8,613 |
| KEEP-only | 547 | 64.0 | +51.0 | +73.8 | $+10,171 |
| KEEP-only recent | 339 | 60.8 | +53.6 | +90.6 | $+4,914 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T12:46:33.461343-04:00","date":"2026-09-04","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":21.0,"phases_s":{"reconcile":0.48,"cancel":0.22,"manage":14.32,"protective_stops":5.24},"signals":0,"placed":0,"equity":1005184.68,"open_positions":44,"pending_orders":0,"open_lots":138,"submitted_today":143,"filled_today":186,"unattributed_contracts":0,"top_signals":[],"github_run":"9097","github_run_id":"33896862960","status":"ok","data_quality":{"clean":{"n":1023,"win":49.85,"med":0.0,"avg":47.47,"pnl":15480.96},"tainted":{"n":1790,"win":33.52,"med":-38.34,"avg":12.76,"pnl":-8612.84},"keep_only":{"n":547,"win":63.99,"med":50.98,"avg":73.79,"pnl":10171.45},"keep_only_recent":{"n":339,"win":60.77,"med":53.57,"avg":90.62,"pnl":4914.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
16:46:25  INFO      Mode: exits
16:46:27  INFO        place_all_stops: checking 3 positions...
16:46:27  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
16:46:27  INFO        STOP skipped APD: fractional (0.1144 shares) — software exit will handle it
16:46:27  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
16:46:27  INFO        [positions] 3/3 (3 valid)
16:46:28  INFO        Daily log -> logs/daily/2026-09-04.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.56|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  APD  P&L +0.1%  $+0.02                                            HOLD|
|  AMZN  P&L +0.7%  $+0.24                                           HOLD|
|  LII  P&L +1.0%  $+0.33                                            HOLD|
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
=== options_live_micro LIVE 2026-09-04T12:46:28.926736-04:00 share=25% ===
2026-09-04 12:46:28,926 INFO === options_live_micro LIVE 2026-09-04T12:46:28.926736-04:00 share=25% ===
Live account equity $230.56 cash $126.25 #225458845 options_level=3
2026-09-04 12:46:29,160 INFO Live account equity $230.56 cash $126.25 #225458845 options_level=3
Live micro: manage/exits only
2026-09-04 12:46:29,717 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-04 12:46:29,797 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (175 earlier lines - see full log file)
| w2     |    7 |    6 |   12 |    7 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    54 |
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 245 | 12 |
| S164 | 263 | 13 |
| S165 | 1703 | 26 |
| S166 | 135 | 9 |
| S167 | 257 | 13 |
| S168 | 190 | 11 |
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
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |   138 | INFO |
| Total closed lots           |  1994 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1023 med=+0.0% | TAINTED n=1790 med=-38.3% | KEEP-only n=547 med=+51.0% | KILL=18 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.56 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260904T165101Z

- UTC timestamp: `20260904T165101Z`
- GitHub run: [#9098](https://github.com/28twagg-ops/TradingBot/actions/runs/33897317098)
- Run id: `33897317098`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`29s`
- Full logs: `logs/action_runs/20260904T165101Z_live_bot.log`, `logs/action_runs/20260904T165101Z_live_options.log`, `logs/action_runs/20260904T165101Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1023 | 49.9 | +0.0 | +47.5 | $+15,481 |
| TAINTED | 1790 | 33.5 | -38.3 | +12.8 | $-8,613 |
| KEEP-only | 547 | 64.0 | +51.0 | +73.8 | $+10,171 |
| KEEP-only recent | 339 | 60.8 | +53.6 | +90.6 | $+4,914 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T12:51:07.350710-04:00","date":"2026-09-04","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":19.3,"phases_s":{"reconcile":0.42,"cancel":0.2,"manage":13.28,"protective_stops":4.71},"signals":0,"placed":0,"equity":1005315.68,"open_positions":44,"pending_orders":0,"open_lots":138,"submitted_today":143,"filled_today":186,"unattributed_contracts":0,"top_signals":[],"github_run":"9098","github_run_id":"33897317098","status":"ok","data_quality":{"clean":{"n":1023,"win":49.85,"med":0.0,"avg":47.47,"pnl":15480.96},"tainted":{"n":1790,"win":33.52,"med":-38.34,"avg":12.76,"pnl":-8612.84},"keep_only":{"n":547,"win":63.99,"med":50.98,"avg":73.79,"pnl":10171.45},"keep_only_recent":{"n":339,"win":60.77,"med":53.57,"avg":90.62,"pnl":4914.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
16:51:02  INFO      Mode: exits
16:51:02  INFO        place_all_stops: checking 3 positions...
16:51:02  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
16:51:02  INFO        STOP skipped APD: fractional (0.1144 shares) — software exit will handle it
16:51:02  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
16:51:03  INFO        [positions] 3/3 (3 valid)
16:51:03  INFO        Daily log -> logs/daily/2026-09-04.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:51 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.54|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  APD  P&L +0.1%  $+0.03                                            HOLD|
|  AMZN  P&L +0.7%  $+0.23                                           HOLD|
|  LII  P&L +0.9%  $+0.32                                            HOLD|
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
=== options_live_micro LIVE 2026-09-04T12:51:04.317815-04:00 share=25% ===
2026-09-04 12:51:04,317 INFO === options_live_micro LIVE 2026-09-04T12:51:04.317815-04:00 share=25% ===
Live account equity $230.55 cash $126.25 #225458845 options_level=3
2026-09-04 12:51:04,527 INFO Live account equity $230.55 cash $126.25 #225458845 options_level=3
Live micro: manage/exits only
2026-09-04 12:51:04,729 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-04 12:51:04,791 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (168 earlier lines - see full log file)
| w2     |    7 |    6 |   12 |    7 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    54 |
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 245 | 12 |
| S164 | 263 | 13 |
| S165 | 1703 | 26 |
| S166 | 135 | 9 |
| S167 | 257 | 13 |
| S168 | 190 | 11 |
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
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |   138 | INFO |
| Total closed lots           |  1994 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1023 med=+0.0% | TAINTED n=1790 med=-38.3% | KEEP-only n=547 med=+51.0% | KILL=18 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.55 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260904T165558Z

- UTC timestamp: `20260904T165558Z`
- GitHub run: [#9099](https://github.com/28twagg-ops/TradingBot/actions/runs/33897760365)
- Run id: `33897760365`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`35s`
- Full logs: `logs/action_runs/20260904T165558Z_live_bot.log`, `logs/action_runs/20260904T165558Z_live_options.log`, `logs/action_runs/20260904T165558Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1023 | 49.9 | +0.0 | +47.5 | $+15,481 |
| TAINTED | 1790 | 33.5 | -38.3 | +12.8 | $-8,613 |
| KEEP-only | 547 | 64.0 | +51.0 | +73.8 | $+10,171 |
| KEEP-only recent | 339 | 60.8 | +53.6 | +90.6 | $+4,914 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T12:56:05.905593-04:00","date":"2026-09-04","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":22.6,"phases_s":{"reconcile":0.52,"cancel":0.24,"manage":15.18,"protective_stops":5.87},"signals":0,"placed":0,"equity":1005330.68,"open_positions":44,"pending_orders":0,"open_lots":138,"submitted_today":143,"filled_today":186,"unattributed_contracts":0,"top_signals":[],"github_run":"9099","github_run_id":"33897760365","status":"ok","data_quality":{"clean":{"n":1023,"win":49.85,"med":0.0,"avg":47.47,"pnl":15480.96},"tainted":{"n":1790,"win":33.52,"med":-38.34,"avg":12.76,"pnl":-8612.84},"keep_only":{"n":547,"win":63.99,"med":50.98,"avg":73.79,"pnl":10171.45},"keep_only_recent":{"n":339,"win":60.77,"med":53.57,"avg":90.62,"pnl":4914.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
16:55:59  INFO      Mode: exits
16:56:00  INFO        place_all_stops: checking 3 positions...
16:56:00  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
16:56:00  INFO        STOP skipped APD: fractional (0.1144 shares) — software exit will handle it
16:56:00  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
16:56:00  INFO        [positions] 3/3 (3 valid)
16:56:01  INFO        Daily log -> logs/daily/2026-09-04.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:56 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.55|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  APD  P&L +0.1%  $+0.03                                            HOLD|
|  AMZN  P&L +0.7%  $+0.24                                           HOLD|
|  LII  P&L +0.9%  $+0.31                                            HOLD|
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
=== options_live_micro LIVE 2026-09-04T12:56:02.146852-04:00 share=25% ===
2026-09-04 12:56:02,146 INFO === options_live_micro LIVE 2026-09-04T12:56:02.146852-04:00 share=25% ===
Live account equity $230.55 cash $126.25 #225458845 options_level=3
2026-09-04 12:56:02,380 INFO Live account equity $230.55 cash $126.25 #225458845 options_level=3
Live micro: manage/exits only
2026-09-04 12:56:02,594 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-04 12:56:02,665 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (172 earlier lines - see full log file)
| w2     |    7 |    6 |   12 |    7 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    54 |
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 245 | 12 |
| S164 | 263 | 13 |
| S165 | 1703 | 26 |
| S166 | 135 | 9 |
| S167 | 257 | 13 |
| S168 | 190 | 11 |
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
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |   138 | INFO |
| Total closed lots           |  1994 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1023 med=+0.0% | TAINTED n=1790 med=-38.3% | KEEP-only n=547 med=+51.0% | KILL=18 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.55 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260904T170107Z

- UTC timestamp: `20260904T170107Z`
- GitHub run: [#9100](https://github.com/28twagg-ops/TradingBot/actions/runs/33898200444)
- Run id: `33898200444`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`29s`
- Full logs: `logs/action_runs/20260904T170107Z_live_bot.log`, `logs/action_runs/20260904T170107Z_live_options.log`, `logs/action_runs/20260904T170107Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1024 | 49.9 | +0.0 | +47.5 | $+15,511 |
| TAINTED | 1790 | 33.5 | -38.3 | +12.8 | $-8,613 |
| KEEP-only | 548 | 64.1 | +50.9 | +73.7 | $+10,201 |
| KEEP-only recent | 340 | 60.9 | +53.4 | +90.5 | $+4,944 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T13:01:14.564060-04:00","date":"2026-09-04","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":21.5,"phases_s":{"reconcile":0.55,"cancel":0.23,"manage":14.32,"protective_stops":5.77},"signals":0,"placed":0,"equity":1005278.66,"open_positions":44,"pending_orders":0,"open_lots":137,"submitted_today":143,"filled_today":186,"unattributed_contracts":0,"top_signals":[],"github_run":"9100","github_run_id":"33898200444","status":"ok","data_quality":{"clean":{"n":1024,"win":49.9,"med":0.0,"avg":47.47,"pnl":15510.96},"tainted":{"n":1790,"win":33.52,"med":-38.34,"avg":12.76,"pnl":-8612.84},"keep_only":{"n":548,"win":64.05,"med":50.93,"avg":73.74,"pnl":10201.45},"keep_only_recent":{"n":340,"win":60.88,"med":53.45,"avg":90.5,"pnl":4944.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
17:01:09  INFO      Mode: exits
17:01:10  INFO        place_all_stops: checking 3 positions...
17:01:10  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
17:01:10  INFO        STOP skipped APD: fractional (0.1144 shares) — software exit will handle it
17:01:10  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
17:01:10  INFO        [positions] 3/3 (3 valid)
17:01:11  INFO        Daily log -> logs/daily/2026-09-04.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.52|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  APD  P&L +0.1%  $+0.04                                            HOLD|
|  AMZN  P&L +0.7%  $+0.23                                           HOLD|
|  LII  P&L +0.8%  $+0.28                                            HOLD|
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
=== options_live_micro LIVE 2026-09-04T13:01:11.763994-04:00 share=25% ===
2026-09-04 13:01:11,764 INFO === options_live_micro LIVE 2026-09-04T13:01:11.763994-04:00 share=25% ===
Live account equity $230.52 cash $126.25 #225458845 options_level=3
2026-09-04 13:01:12,021 INFO Live account equity $230.52 cash $126.25 #225458845 options_level=3
Live micro: manage/exits only
2026-09-04 13:01:12,256 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-04 13:01:12,333 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (166 earlier lines - see full log file)
| w2     |    7 |    6 |   12 |    7 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    54 |
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 245 | 12 |
| S164 | 263 | 13 |
| S165 | 1703 | 26 |
| S166 | 135 | 9 |
| S167 | 257 | 13 |
| S168 | 190 | 11 |
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
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |   137 | INFO |
| Total closed lots           |  1995 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1024 med=+0.0% | TAINTED n=1790 med=-38.3% | KEEP-only n=548 med=+50.9% | KILL=18 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.52 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260904T170558Z

- UTC timestamp: `20260904T170558Z`
- GitHub run: [#9101](https://github.com/28twagg-ops/TradingBot/actions/runs/33898655490)
- Run id: `33898655490`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`18s`
- Full logs: `logs/action_runs/20260904T170558Z_live_bot.log`, `logs/action_runs/20260904T170558Z_live_options.log`, `logs/action_runs/20260904T170558Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1024 | 49.9 | +0.0 | +47.5 | $+15,511 |
| TAINTED | 1790 | 33.5 | -38.3 | +12.8 | $-8,613 |
| KEEP-only | 548 | 64.1 | +50.9 | +73.7 | $+10,201 |
| KEEP-only recent | 340 | 60.9 | +53.4 | +90.5 | $+4,944 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T13:06:03.892832-04:00","date":"2026-09-04","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":9.2,"phases_s":{"reconcile":0.12,"cancel":0.04,"manage":7.78,"protective_stops":0.82},"signals":0,"placed":0,"equity":1005187.66,"open_positions":44,"pending_orders":0,"open_lots":137,"submitted_today":143,"filled_today":186,"unattributed_contracts":0,"top_signals":[],"github_run":"9101","github_run_id":"33898655490","status":"ok","data_quality":{"clean":{"n":1024,"win":49.9,"med":0.0,"avg":47.47,"pnl":15510.96},"tainted":{"n":1790,"win":33.52,"med":-38.34,"avg":12.76,"pnl":-8612.84},"keep_only":{"n":548,"win":64.05,"med":50.93,"avg":73.74,"pnl":10201.45},"keep_only_recent":{"n":340,"win":60.88,"med":53.45,"avg":90.5,"pnl":4944.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
17:06:00  INFO      Mode: exits
17:06:00  INFO        place_all_stops: checking 3 positions...
17:06:00  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
17:06:00  INFO        STOP skipped APD: fractional (0.1144 shares) — software exit will handle it
17:06:00  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
17:06:00  INFO        [positions] 3/3 (3 valid)
17:06:00  INFO        Daily log -> logs/daily/2026-09-04.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.50|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  APD  P&L +0.1%  $+0.02                                            HOLD|
|  AMZN  P&L +0.6%  $+0.22                                           HOLD|
|  LII  P&L +0.8%  $+0.28                                            HOLD|
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
=== options_live_micro LIVE 2026-09-04T13:06:01.646507-04:00 share=25% ===
2026-09-04 13:06:01,646 INFO === options_live_micro LIVE 2026-09-04T13:06:01.646507-04:00 share=25% ===
Live account equity $230.50 cash $126.25 #225458845 options_level=3
2026-09-04 13:06:01,686 INFO Live account equity $230.50 cash $126.25 #225458845 options_level=3
Live micro: manage/exits only
2026-09-04 13:06:01,708 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-04 13:06:01,715 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (166 earlier lines - see full log file)
| w2     |    7 |    6 |   12 |    7 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    54 |
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 245 | 12 |
| S164 | 263 | 13 |
| S165 | 1703 | 26 |
| S166 | 135 | 9 |
| S167 | 257 | 13 |
| S168 | 190 | 11 |
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
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |   137 | INFO |
| Total closed lots           |  1995 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1024 med=+0.0% | TAINTED n=1790 med=-38.3% | KEEP-only n=548 med=+50.9% | KILL=18 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.5 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260904T171105Z

- UTC timestamp: `20260904T171105Z`
- GitHub run: [#9102](https://github.com/28twagg-ops/TradingBot/actions/runs/33899101958)
- Run id: `33899101958`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`30s`
- Full logs: `logs/action_runs/20260904T171105Z_live_bot.log`, `logs/action_runs/20260904T171105Z_live_options.log`, `logs/action_runs/20260904T171105Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1024 | 49.9 | +0.0 | +47.5 | $+15,511 |
| TAINTED | 1790 | 33.5 | -38.3 | +12.8 | $-8,613 |
| KEEP-only | 548 | 64.1 | +50.9 | +73.7 | $+10,201 |
| KEEP-only recent | 340 | 60.9 | +53.4 | +90.5 | $+4,944 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T13:11:13.046727-04:00","date":"2026-09-04","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":18.9,"phases_s":{"reconcile":0.44,"cancel":0.19,"manage":12.97,"protective_stops":4.55},"signals":0,"placed":0,"equity":1005138.66,"open_positions":44,"pending_orders":0,"open_lots":137,"submitted_today":143,"filled_today":186,"unattributed_contracts":0,"top_signals":[],"github_run":"9102","github_run_id":"33899101958","status":"ok","data_quality":{"clean":{"n":1024,"win":49.9,"med":0.0,"avg":47.47,"pnl":15510.96},"tainted":{"n":1790,"win":33.52,"med":-38.34,"avg":12.76,"pnl":-8612.84},"keep_only":{"n":548,"win":64.05,"med":50.93,"avg":73.74,"pnl":10201.45},"keep_only_recent":{"n":340,"win":60.88,"med":53.45,"avg":90.5,"pnl":4944.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
17:11:07  INFO      Mode: exits
17:11:07  INFO        place_all_stops: checking 3 positions...
17:11:07  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
17:11:07  INFO        STOP skipped APD: fractional (0.1144 shares) — software exit will handle it
17:11:07  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
17:11:08  INFO        [positions] 3/3 (3 valid)
17:11:08  INFO        Daily log -> logs/daily/2026-09-04.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.47|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  APD  P&L -0.0%  $-0.01                                            HOLD|
|  AMZN  P&L +0.6%  $+0.22                                           HOLD|
|  LII  P&L +0.8%  $+0.29                                            HOLD|
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
=== options_live_micro LIVE 2026-09-04T13:11:09.560071-04:00 share=25% ===
2026-09-04 13:11:09,560 INFO === options_live_micro LIVE 2026-09-04T13:11:09.560071-04:00 share=25% ===
Live account equity $230.47 cash $126.25 #225458845 options_level=3
2026-09-04 13:11:09,772 INFO Live account equity $230.47 cash $126.25 #225458845 options_level=3
Live micro: manage/exits only
2026-09-04 13:11:09,949 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-04 13:11:10,013 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (166 earlier lines - see full log file)
| w2     |    7 |    6 |   12 |    7 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    54 |
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 245 | 12 |
| S164 | 263 | 13 |
| S165 | 1703 | 26 |
| S166 | 135 | 9 |
| S167 | 257 | 13 |
| S168 | 190 | 11 |
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
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |   137 | INFO |
| Total closed lots           |  1995 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1024 med=+0.0% | TAINTED n=1790 med=-38.3% | KEEP-only n=548 med=+50.9% | KILL=18 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.47 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260904T171603Z

- UTC timestamp: `20260904T171603Z`
- GitHub run: [#9103](https://github.com/28twagg-ops/TradingBot/actions/runs/33899552945)
- Run id: `33899552945`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`28s`
- Full logs: `logs/action_runs/20260904T171603Z_live_bot.log`, `logs/action_runs/20260904T171603Z_live_options.log`, `logs/action_runs/20260904T171603Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1024 | 49.9 | +0.0 | +47.5 | $+15,511 |
| TAINTED | 1790 | 33.5 | -38.3 | +12.8 | $-8,613 |
| KEEP-only | 548 | 64.1 | +50.9 | +73.7 | $+10,201 |
| KEEP-only recent | 340 | 60.9 | +53.4 | +90.5 | $+4,944 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T13:16:10.529727-04:00","date":"2026-09-04","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":18.2,"phases_s":{"reconcile":0.59,"cancel":0.18,"manage":12.27,"protective_stops":4.43},"signals":0,"placed":0,"equity":1005097.61,"open_positions":43,"pending_orders":0,"open_lots":135,"submitted_today":143,"filled_today":186,"unattributed_contracts":0,"top_signals":[],"github_run":"9103","github_run_id":"33899552945","status":"ok","data_quality":{"clean":{"n":1024,"win":49.9,"med":0.0,"avg":47.47,"pnl":15510.96},"tainted":{"n":1790,"win":33.52,"med":-38.34,"avg":12.76,"pnl":-8612.84},"keep_only":{"n":548,"win":64.05,"med":50.93,"avg":73.74,"pnl":10201.45},"keep_only_recent":{"n":340,"win":60.88,"med":53.45,"avg":90.5,"pnl":4944.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
17:16:04  INFO      Mode: exits
17:16:05  INFO        place_all_stops: checking 3 positions...
17:16:05  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
17:16:05  INFO        STOP skipped APD: fractional (0.1144 shares) — software exit will handle it
17:16:05  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
17:16:05  INFO        [positions] 3/3 (3 valid)
17:16:06  INFO        Daily log -> logs/daily/2026-09-04.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.41|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  APD  P&L -0.0%  $-0.02                                            HOLD|
|  AMZN  P&L +0.6%  $+0.22                                           HOLD|
|  LII  P&L +0.7%  $+0.24                                            HOLD|
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
=== options_live_micro LIVE 2026-09-04T13:16:06.915649-04:00 share=25% ===
2026-09-04 13:16:06,915 INFO === options_live_micro LIVE 2026-09-04T13:16:06.915649-04:00 share=25% ===
Live account equity $230.41 cash $126.25 #225458845 options_level=3
2026-09-04 13:16:07,118 INFO Live account equity $230.41 cash $126.25 #225458845 options_level=3
Live micro: manage/exits only
2026-09-04 13:16:07,294 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-04 13:16:07,351 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (169 earlier lines - see full log file)
| w2     |    7 |    6 |   12 |    7 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    54 |
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 245 | 12 |
| S164 | 263 | 13 |
| S165 | 1703 | 26 |
| S166 | 135 | 9 |
| S167 | 257 | 13 |
| S168 | 190 | 11 |
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
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |   135 | INFO |
| Total closed lots           |  1995 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1024 med=+0.0% | TAINTED n=1790 med=-38.3% | KEEP-only n=548 med=+50.9% | KILL=18 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.41 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260904T172102Z

- UTC timestamp: `20260904T172102Z`
- GitHub run: [#9104](https://github.com/28twagg-ops/TradingBot/actions/runs/33900005174)
- Run id: `33900005174`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`20s`
- Full logs: `logs/action_runs/20260904T172102Z_live_bot.log`, `logs/action_runs/20260904T172102Z_live_options.log`, `logs/action_runs/20260904T172102Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1024 | 49.9 | +0.0 | +47.5 | $+15,511 |
| TAINTED | 1790 | 33.5 | -38.3 | +12.8 | $-8,613 |
| KEEP-only | 548 | 64.1 | +50.9 | +73.7 | $+10,201 |
| KEEP-only recent | 340 | 60.9 | +53.4 | +90.5 | $+4,944 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T13:21:07.991411-04:00","date":"2026-09-04","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":8.6,"phases_s":{"reconcile":0.11,"cancel":0.04,"manage":7.09,"protective_stops":0.81},"signals":0,"placed":0,"equity":1005239.61,"open_positions":43,"pending_orders":0,"open_lots":135,"submitted_today":143,"filled_today":186,"unattributed_contracts":0,"top_signals":[],"github_run":"9104","github_run_id":"33900005174","status":"ok","data_quality":{"clean":{"n":1024,"win":49.9,"med":0.0,"avg":47.47,"pnl":15510.96},"tainted":{"n":1790,"win":33.52,"med":-38.34,"avg":12.76,"pnl":-8612.84},"keep_only":{"n":548,"win":64.05,"med":50.93,"avg":73.74,"pnl":10201.45},"keep_only_recent":{"n":340,"win":60.88,"med":53.45,"avg":90.5,"pnl":4944.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
17:21:03  INFO      Mode: exits
17:21:03  INFO        place_all_stops: checking 3 positions...
17:21:03  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
17:21:03  INFO        STOP skipped APD: fractional (0.1144 shares) — software exit will handle it
17:21:03  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
17:21:03  INFO        [positions] 3/3 (3 valid)
17:21:04  INFO        Daily log -> logs/daily/2026-09-04.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.36|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  APD  P&L -0.0%  $-0.01                                            HOLD|
|  LII  P&L +0.5%  $+0.17                                            HOLD|
|  AMZN  P&L +0.7%  $+0.23                                           HOLD|
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
=== options_live_micro LIVE 2026-09-04T13:21:04.872867-04:00 share=25% ===
2026-09-04 13:21:04,872 INFO === options_live_micro LIVE 2026-09-04T13:21:04.872867-04:00 share=25% ===
Live account equity $230.36 cash $126.25 #225458845 options_level=3
2026-09-04 13:21:05,009 INFO Live account equity $230.36 cash $126.25 #225458845 options_level=3
Live micro: manage/exits only
2026-09-04 13:21:05,033 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-04 13:21:05,041 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (168 earlier lines - see full log file)
| w2     |    7 |    6 |   12 |    7 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    54 |
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 245 | 12 |
| S164 | 263 | 13 |
| S165 | 1703 | 26 |
| S166 | 135 | 9 |
| S167 | 257 | 13 |
| S168 | 190 | 11 |
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
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |   135 | INFO |
| Total closed lots           |  1995 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1024 med=+0.0% | TAINTED n=1790 med=-38.3% | KEEP-only n=548 med=+50.9% | KILL=18 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.36 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260904T172559Z

- UTC timestamp: `20260904T172559Z`
- GitHub run: [#9105](https://github.com/28twagg-ops/TradingBot/actions/runs/33900457026)
- Run id: `33900457026`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`31s`
- Full logs: `logs/action_runs/20260904T172559Z_live_bot.log`, `logs/action_runs/20260904T172559Z_live_options.log`, `logs/action_runs/20260904T172559Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1024 | 49.9 | +0.0 | +47.5 | $+15,511 |
| TAINTED | 1790 | 33.5 | -38.3 | +12.8 | $-8,613 |
| KEEP-only | 548 | 64.1 | +50.9 | +73.7 | $+10,201 |
| KEEP-only recent | 340 | 60.9 | +53.4 | +90.5 | $+4,944 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T13:26:07.026722-04:00","date":"2026-09-04","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":20.1,"phases_s":{"reconcile":0.51,"cancel":0.24,"manage":13.32,"protective_stops":5.23},"signals":0,"placed":0,"equity":1005423.59,"open_positions":44,"pending_orders":0,"open_lots":135,"submitted_today":143,"filled_today":186,"unattributed_contracts":0,"top_signals":[],"github_run":"9105","github_run_id":"33900457026","status":"ok","data_quality":{"clean":{"n":1024,"win":49.9,"med":0.0,"avg":47.47,"pnl":15510.96},"tainted":{"n":1790,"win":33.52,"med":-38.34,"avg":12.76,"pnl":-8612.84},"keep_only":{"n":548,"win":64.05,"med":50.93,"avg":73.74,"pnl":10201.45},"keep_only_recent":{"n":340,"win":60.88,"med":53.45,"avg":90.5,"pnl":4944.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
17:26:00  INFO      Mode: exits
17:26:00  INFO        place_all_stops: checking 3 positions...
17:26:00  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
17:26:00  INFO        STOP skipped APD: fractional (0.1144 shares) — software exit will handle it
17:26:00  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
17:26:01  INFO        [positions] 3/3 (3 valid)
17:26:02  INFO        Daily log -> logs/daily/2026-09-04.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.33|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  APD  P&L -0.1%  $-0.04                                            HOLD|
|  LII  P&L +0.5%  $+0.17                                            HOLD|
|  AMZN  P&L +0.6%  $+0.22                                           HOLD|
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
=== options_live_micro LIVE 2026-09-04T13:26:03.339359-04:00 share=25% ===
2026-09-04 13:26:03,339 INFO === options_live_micro LIVE 2026-09-04T13:26:03.339359-04:00 share=25% ===
Live account equity $230.34 cash $126.25 #225458845 options_level=3
2026-09-04 13:26:03,562 INFO Live account equity $230.34 cash $126.25 #225458845 options_level=3
Live micro: manage/exits only
2026-09-04 13:26:03,788 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-04 13:26:03,899 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (168 earlier lines - see full log file)
| w2     |    7 |    6 |   12 |    7 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    54 |
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 245 | 12 |
| S164 | 263 | 13 |
| S165 | 1703 | 26 |
| S166 | 135 | 9 |
| S167 | 257 | 13 |
| S168 | 190 | 11 |
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
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |   135 | INFO |
| Total closed lots           |  1995 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1024 med=+0.0% | TAINTED n=1790 med=-38.3% | KEEP-only n=548 med=+50.9% | KILL=18 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.34 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260904T173058Z

- UTC timestamp: `20260904T173058Z`
- GitHub run: [#9106](https://github.com/28twagg-ops/TradingBot/actions/runs/33900899050)
- Run id: `33900899050`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`20s`
- Full logs: `logs/action_runs/20260904T173058Z_live_bot.log`, `logs/action_runs/20260904T173058Z_live_options.log`, `logs/action_runs/20260904T173058Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1024 | 49.9 | +0.0 | +47.5 | $+15,511 |
| TAINTED | 1790 | 33.5 | -38.3 | +12.8 | $-8,613 |
| KEEP-only | 548 | 64.1 | +50.9 | +73.7 | $+10,201 |
| KEEP-only recent | 340 | 60.9 | +53.4 | +90.5 | $+4,944 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T13:31:04.069279-04:00","date":"2026-09-04","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":9.0,"phases_s":{"reconcile":0.15,"cancel":0.04,"manage":7.36,"protective_stops":0.94},"signals":0,"placed":0,"equity":1005425.59,"open_positions":44,"pending_orders":0,"open_lots":135,"submitted_today":143,"filled_today":186,"unattributed_contracts":0,"top_signals":[],"github_run":"9106","github_run_id":"33900899050","status":"ok","data_quality":{"clean":{"n":1024,"win":49.9,"med":0.0,"avg":47.47,"pnl":15510.96},"tainted":{"n":1790,"win":33.52,"med":-38.34,"avg":12.76,"pnl":-8612.84},"keep_only":{"n":548,"win":64.05,"med":50.93,"avg":73.74,"pnl":10201.45},"keep_only_recent":{"n":340,"win":60.88,"med":53.45,"avg":90.5,"pnl":4944.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
17:30:59  INFO      Mode: exits
17:30:59  INFO        place_all_stops: checking 3 positions...
17:30:59  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
17:30:59  INFO        STOP skipped APD: fractional (0.1144 shares) — software exit will handle it
17:30:59  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
17:30:59  INFO        [positions] 3/3 (3 valid)
17:30:59  INFO        Daily log -> logs/daily/2026-09-04.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:30 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.25|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  APD  P&L -0.2%  $-0.05                                            HOLD|
|  LII  P&L +0.4%  $+0.15                                            HOLD|
|  AMZN  P&L +0.5%  $+0.19                                           HOLD|
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
=== options_live_micro LIVE 2026-09-04T13:31:00.529103-04:00 share=25% ===
2026-09-04 13:31:00,529 INFO === options_live_micro LIVE 2026-09-04T13:31:00.529103-04:00 share=25% ===
Live account equity $230.25 cash $126.25 #225458845 options_level=3
2026-09-04 13:31:00,909 INFO Live account equity $230.25 cash $126.25 #225458845 options_level=3
Live micro: manage/exits only
2026-09-04 13:31:00,957 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-04 13:31:00,971 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (168 earlier lines - see full log file)
| w2     |    7 |    6 |   12 |    7 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    54 |
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 245 | 12 |
| S164 | 263 | 13 |
| S165 | 1703 | 26 |
| S166 | 135 | 9 |
| S167 | 257 | 13 |
| S168 | 190 | 11 |
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
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |   135 | INFO |
| Total closed lots           |  1995 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1024 med=+0.0% | TAINTED n=1790 med=-38.3% | KEEP-only n=548 med=+50.9% | KILL=18 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.25 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260904T173558Z

- UTC timestamp: `20260904T173558Z`
- GitHub run: [#9107](https://github.com/28twagg-ops/TradingBot/actions/runs/33901349357)
- Run id: `33901349357`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`32s`
- Full logs: `logs/action_runs/20260904T173558Z_live_bot.log`, `logs/action_runs/20260904T173558Z_live_options.log`, `logs/action_runs/20260904T173558Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1024 | 49.9 | +0.0 | +47.5 | $+15,511 |
| TAINTED | 1790 | 33.5 | -38.3 | +12.8 | $-8,613 |
| KEEP-only | 548 | 64.1 | +50.9 | +73.7 | $+10,201 |
| KEEP-only recent | 340 | 60.9 | +53.4 | +90.5 | $+4,944 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T13:36:05.259932-04:00","date":"2026-09-04","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":20.9,"phases_s":{"reconcile":0.52,"cancel":0.24,"manage":14.13,"protective_stops":5.22},"signals":0,"placed":0,"equity":1005500.59,"open_positions":44,"pending_orders":0,"open_lots":135,"submitted_today":143,"filled_today":186,"unattributed_contracts":0,"top_signals":[],"github_run":"9107","github_run_id":"33901349357","status":"ok","data_quality":{"clean":{"n":1024,"win":49.9,"med":0.0,"avg":47.47,"pnl":15510.96},"tainted":{"n":1790,"win":33.52,"med":-38.34,"avg":12.76,"pnl":-8612.84},"keep_only":{"n":548,"win":64.05,"med":50.93,"avg":73.74,"pnl":10201.45},"keep_only_recent":{"n":340,"win":60.88,"med":53.45,"avg":90.5,"pnl":4944.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
17:35:58  INFO      Mode: exits
17:35:59  INFO        place_all_stops: checking 3 positions...
17:35:59  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
17:35:59  INFO        STOP skipped APD: fractional (0.1144 shares) — software exit will handle it
17:35:59  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
17:36:00  INFO        [positions] 3/3 (3 valid)
17:36:00  INFO        Daily log -> logs/daily/2026-09-04.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:35 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.21|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  APD  P&L -0.2%  $-0.07                                            HOLD|
|  LII  P&L +0.4%  $+0.13                                            HOLD|
|  AMZN  P&L +0.5%  $+0.18                                           HOLD|
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
=== options_live_micro LIVE 2026-09-04T13:36:01.498759-04:00 share=25% ===
2026-09-04 13:36:01,498 INFO === options_live_micro LIVE 2026-09-04T13:36:01.498759-04:00 share=25% ===
Live account equity $230.21 cash $126.25 #225458845 options_level=3
2026-09-04 13:36:01,724 INFO Live account equity $230.21 cash $126.25 #225458845 options_level=3
Live micro: manage/exits only
2026-09-04 13:36:01,932 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-04 13:36:02,002 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (168 earlier lines - see full log file)
| w2     |    7 |    6 |   12 |    7 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    54 |
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 245 | 12 |
| S164 | 263 | 13 |
| S165 | 1703 | 26 |
| S166 | 135 | 9 |
| S167 | 257 | 13 |
| S168 | 190 | 11 |
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
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |   135 | INFO |
| Total closed lots           |  1995 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1024 med=+0.0% | TAINTED n=1790 med=-38.3% | KEEP-only n=548 med=+50.9% | KILL=18 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.21 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260904T174105Z

- UTC timestamp: `20260904T174105Z`
- GitHub run: [#9108](https://github.com/28twagg-ops/TradingBot/actions/runs/33901788902)
- Run id: `33901788902`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`28s`
- Full logs: `logs/action_runs/20260904T174105Z_live_bot.log`, `logs/action_runs/20260904T174105Z_live_options.log`, `logs/action_runs/20260904T174105Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1024 | 49.9 | +0.0 | +47.5 | $+15,511 |
| TAINTED | 1790 | 33.5 | -38.3 | +12.8 | $-8,613 |
| KEEP-only | 548 | 64.1 | +50.9 | +73.7 | $+10,201 |
| KEEP-only recent | 340 | 60.9 | +53.4 | +90.5 | $+4,944 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T13:41:12.238261-04:00","date":"2026-09-04","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":18.7,"phases_s":{"reconcile":0.42,"cancel":0.19,"manage":12.84,"protective_stops":4.55},"signals":0,"placed":0,"equity":1005473.59,"open_positions":43,"pending_orders":0,"open_lots":135,"submitted_today":143,"filled_today":186,"unattributed_contracts":0,"top_signals":[],"github_run":"9108","github_run_id":"33901788902","status":"ok","data_quality":{"clean":{"n":1024,"win":49.9,"med":0.0,"avg":47.47,"pnl":15510.96},"tainted":{"n":1790,"win":33.52,"med":-38.34,"avg":12.76,"pnl":-8612.84},"keep_only":{"n":548,"win":64.05,"med":50.93,"avg":73.74,"pnl":10201.45},"keep_only_recent":{"n":340,"win":60.88,"med":53.45,"avg":90.5,"pnl":4944.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
17:41:06  INFO      Mode: exits
17:41:07  INFO        place_all_stops: checking 3 positions...
17:41:07  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
17:41:07  INFO        STOP skipped APD: fractional (0.1144 shares) — software exit will handle it
17:41:07  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
17:41:07  INFO        [positions] 3/3 (3 valid)
17:41:08  INFO        Daily log -> logs/daily/2026-09-04.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.18|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  APD  P&L -0.2%  $-0.07                                            HOLD|
|  LII  P&L +0.3%  $+0.09                                            HOLD|
|  AMZN  P&L +0.5%  $+0.18                                           HOLD|
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
=== options_live_micro LIVE 2026-09-04T13:41:08.759233-04:00 share=25% ===
2026-09-04 13:41:08,759 INFO === options_live_micro LIVE 2026-09-04T13:41:08.759233-04:00 share=25% ===
Live account equity $230.17 cash $126.25 #225458845 options_level=3
2026-09-04 13:41:08,970 INFO Live account equity $230.17 cash $126.25 #225458845 options_level=3
Live micro: manage/exits only
2026-09-04 13:41:09,234 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-04 13:41:09,291 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (176 earlier lines - see full log file)
| w2     |    7 |    6 |   12 |    7 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    54 |
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 245 | 12 |
| S164 | 263 | 13 |
| S165 | 1703 | 26 |
| S166 | 135 | 9 |
| S167 | 257 | 13 |
| S168 | 190 | 11 |
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
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |   135 | INFO |
| Total closed lots           |  1995 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1024 med=+0.0% | TAINTED n=1790 med=-38.3% | KEEP-only n=548 med=+50.9% | KILL=18 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.17 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260904T174601Z

- UTC timestamp: `20260904T174601Z`
- GitHub run: [#9109](https://github.com/28twagg-ops/TradingBot/actions/runs/33902222138)
- Run id: `33902222138`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`24s`
- Full logs: `logs/action_runs/20260904T174601Z_live_bot.log`, `logs/action_runs/20260904T174601Z_live_options.log`, `logs/action_runs/20260904T174601Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1024 | 49.9 | +0.0 | +47.5 | $+15,511 |
| TAINTED | 1790 | 33.5 | -38.3 | +12.8 | $-8,613 |
| KEEP-only | 548 | 64.1 | +50.9 | +73.7 | $+10,201 |
| KEEP-only recent | 340 | 60.9 | +53.4 | +90.5 | $+4,944 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T13:46:07.346315-04:00","date":"2026-09-04","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":12.8,"phases_s":{"reconcile":0.21,"cancel":0.09,"manage":9.96,"protective_stops":2.0},"signals":0,"placed":0,"equity":1005440.57,"open_positions":43,"pending_orders":0,"open_lots":134,"submitted_today":143,"filled_today":186,"unattributed_contracts":0,"top_signals":[],"github_run":"9109","github_run_id":"33902222138","status":"ok","data_quality":{"clean":{"n":1024,"win":49.9,"med":0.0,"avg":47.47,"pnl":15510.96},"tainted":{"n":1790,"win":33.52,"med":-38.34,"avg":12.76,"pnl":-8612.84},"keep_only":{"n":548,"win":64.05,"med":50.93,"avg":73.74,"pnl":10201.45},"keep_only_recent":{"n":340,"win":60.88,"med":53.45,"avg":90.5,"pnl":4944.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
17:46:02  INFO      Mode: exits
17:46:02  INFO        place_all_stops: checking 3 positions...
17:46:02  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
17:46:02  INFO        STOP skipped APD: fractional (0.1144 shares) — software exit will handle it
17:46:02  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
17:46:02  INFO        [positions] 3/3 (3 valid)
17:46:02  INFO        Daily log -> logs/daily/2026-09-04.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.28|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  APD  P&L -0.2%  $-0.06                                            HOLD|
|  AMZN  P&L +0.5%  $+0.18                                           HOLD|
|  LII  P&L +0.6%  $+0.19                                            HOLD|
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
=== options_live_micro LIVE 2026-09-04T13:46:03.810383-04:00 share=25% ===
2026-09-04 13:46:03,810 INFO === options_live_micro LIVE 2026-09-04T13:46:03.810383-04:00 share=25% ===
Live account equity $230.28 cash $126.25 #225458845 options_level=3
2026-09-04 13:46:03,907 INFO Live account equity $230.28 cash $126.25 #225458845 options_level=3
Live micro: manage/exits only
2026-09-04 13:46:03,998 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-04 13:46:04,024 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (175 earlier lines - see full log file)
| w2     |    7 |    6 |   12 |    7 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    54 |
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 245 | 12 |
| S164 | 263 | 13 |
| S165 | 1703 | 26 |
| S166 | 135 | 9 |
| S167 | 257 | 13 |
| S168 | 190 | 11 |
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
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |   134 | INFO |
| Total closed lots           |  1995 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1024 med=+0.0% | TAINTED n=1790 med=-38.3% | KEEP-only n=548 med=+50.9% | KILL=18 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.28 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260904T175107Z

- UTC timestamp: `20260904T175107Z`
- GitHub run: [#9110](https://github.com/28twagg-ops/TradingBot/actions/runs/33902659884)
- Run id: `33902659884`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`33s`
- Full logs: `logs/action_runs/20260904T175107Z_live_bot.log`, `logs/action_runs/20260904T175107Z_live_options.log`, `logs/action_runs/20260904T175107Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1024 | 49.9 | +0.0 | +47.5 | $+15,511 |
| TAINTED | 1790 | 33.5 | -38.3 | +12.8 | $-8,613 |
| KEEP-only | 548 | 64.1 | +50.9 | +73.7 | $+10,201 |
| KEEP-only recent | 340 | 60.9 | +53.4 | +90.5 | $+4,944 |

- KEEP strategies (22): S173, S174, S210, S218, S350, S352, S353, S354, S355, S357, S361, S362, S363, S364, S397, S398, S399, S401, S403, S404, S406, S412
- KILL strategies (18): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S359, S360, S365, S366, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-04T13:51:15.826348-04:00","date":"2026-09-04","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":20.4,"phases_s":{"reconcile":0.56,"cancel":0.23,"manage":13.18,"protective_stops":5.49},"signals":0,"placed":0,"equity":1005485.57,"open_positions":43,"pending_orders":0,"open_lots":134,"submitted_today":143,"filled_today":186,"unattributed_contracts":0,"top_signals":[],"github_run":"9110","github_run_id":"33902659884","status":"ok","data_quality":{"clean":{"n":1024,"win":49.9,"med":0.0,"avg":47.47,"pnl":15510.96},"tainted":{"n":1790,"win":33.52,"med":-38.34,"avg":12.76,"pnl":-8612.84},"keep_only":{"n":548,"win":64.05,"med":50.93,"avg":73.74,"pnl":10201.45},"keep_only_recent":{"n":340,"win":60.88,"med":53.45,"avg":90.5,"pnl":4944.0},"keep_strategies":["S173","S174","S210","S218","S350","S352","S353","S354","S355","S357","S361","S362","S363","S364","S397","S398","S399","S401","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S359","S360","S365","S366","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
17:51:08  INFO      Mode: exits
17:51:09  INFO        place_all_stops: checking 3 positions...
17:51:09  INFO        STOP skipped AMZN: fractional (0.1353 shares) — software exit will handle it
17:51:09  INFO        STOP skipped APD: fractional (0.1144 shares) — software exit will handle it
17:51:09  INFO        STOP skipped LII: fractional (0.0895 shares) — software exit will handle it
17:51:10  INFO        [positions] 3/3 (3 valid)
17:51:11  INFO        Daily log -> logs/daily/2026-09-04.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:51 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.27|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  APD  P&L -0.2%  $-0.07                                            HOLD|
|  LII  P&L +0.5%  $+0.16                                            HOLD|
|  AMZN  P&L +0.6%  $+0.21                                           HOLD|
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
=== options_live_micro LIVE 2026-09-04T13:51:12.080281-04:00 share=25% ===
2026-09-04 13:51:12,080 INFO === options_live_micro LIVE 2026-09-04T13:51:12.080281-04:00 share=25% ===
Live account equity $230.28 cash $126.25 #225458845 options_level=3
2026-09-04 13:51:12,313 INFO Live account equity $230.28 cash $126.25 #225458845 options_level=3
Live micro: manage/exits only
2026-09-04 13:51:12,521 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-04 13:51:12,591 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (173 earlier lines - see full log file)
| w2     |    7 |    6 |   12 |    7 |    7 |    6 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    54 |
| w3     |    9 |    7 |   14 |    6 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    61 |
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 245 | 12 |
| S164 | 263 | 13 |
| S165 | 1703 | 26 |
| S166 | 135 | 9 |
| S167 | 257 | 13 |
| S168 | 190 | 11 |
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
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |   134 | INFO |
| Total closed lots           |  1995 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-04_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1024 med=+0.0% | TAINTED n=1790 med=-38.3% | KEEP-only n=548 med=+50.9% | KILL=18 KEEP=22
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.27 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---
