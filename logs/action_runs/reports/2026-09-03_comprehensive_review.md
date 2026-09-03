# Daily Comprehensive Action Review - 2026-09-03

_Auto-generated from GitHub Actions run output. Each run appends a summary; full stdout is in linked per-run log files._
## Run 20260903T130103Z

- UTC timestamp: `20260903T130103Z`
- GitHub run: [#8920](https://github.com/28twagg-ops/TradingBot/actions/runs/33758493417)
- Run id: `33758493417`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`12s`
- Full logs: `logs/action_runs/20260903T130103Z_live_bot.log`, `logs/action_runs/20260903T130103Z_live_options.log`, `logs/action_runs/20260903T130103Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 871 | 42.5 | -46.9 | +15.6 | $+8,494 |
| TAINTED | 1766 | 33.1 | -39.2 | +12.2 | $-9,184 |
| KEEP-only | 355 | 62.0 | +37.7 | +41.1 | $+5,979 |
| KEEP-only recent | 167 | 57.5 | +50.0 | +46.5 | $+1,953 |

- KEEP strategies (14): S173, S174, S210, S218, S350, S362, S363, S364, S397, S398, S401, S404, S406, S412
- KILL strategies (19): ORPHAN, S165, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S360, S399, S403, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-03T09:01:08.597095-04:00","date":"2026-09-03","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.11},"signals":0,"placed":0,"equity":999486.18,"open_positions":26,"pending_orders":0,"open_lots":118,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"8920","github_run_id":"33758493417","status":"ok","data_quality":{"clean":{"n":871,"win":42.48,"med":-46.88,"avg":15.58,"pnl":8493.53},"tainted":{"n":1766,"win":33.07,"med":-39.16,"avg":12.18,"pnl":-9184.34},"keep_only":{"n":355,"win":61.97,"med":37.69,"avg":41.06,"pnl":5979.45},"keep_only_recent":{"n":167,"win":57.49,"med":50.0,"avg":46.53,"pnl":1953.0},"keep_strategies":["S173","S174","S210","S218","S350","S362","S363","S364","S397","S398","S401","S404","S406","S412"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S360","S399","S403","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:01:04  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.37|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $230.37|
|  Cash                                                           $195.68|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $34.69|
|  Open P&L                                                        $+0.11|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (1 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AMZN     Pullback50      $34.69     $255.49  $256.30  +0.3%   $+0.11  |
|                                                                        |
|  Total invested                                                  $34.69|
|  Total open P&L                                                  $+0.11|
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
|  2026-09-02  SELL  MO  Pullback50  $34.52  P&L $+0.00                  |
|  2026-09-02  SELL  AES  Pullback50  $34.50  P&L $-0.03                 |
|  2026-09-02  SELL  AES  Pullback50  $34.57  P&L $-0.01                 |
|  2026-09-02  SELL  AIZ  Pullback50  $34.26  P&L $-0.32                 |
|  2026-09-02  SELL  SYNA  MomReversal  $34.43  P&L $-0.27               |
|  2026-09-02  SELL  GME  EarningsDrift  $35.03  P&L $+0.35              |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-03T09:01:05.666150-04:00 share=25% ===
2026-09-03 09:01:05,666 INFO === options_live_micro LIVE 2026-09-03T09:01:05.666150-04:00 share=25% ===
Live account equity $230.37 cash $195.68 #225458845 options_level=3
2026-09-03 09:01:05,719 INFO Live account equity $230.37 cash $195.68 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-03 09:01:05,726 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-03 09:01:05,736 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (153 earlier lines - see full log file)
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    3 |    2 |    7 |    1 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    26 |
| w2     |    6 |    5 |   11 |    5 |    6 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    47 |
| w3     |    7 |    6 |   13 |    4 |    7 |    5 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    53 |
| w4     |    5 |    4 |   10 |    2 |    5 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    40 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 223 | 9 |
| S164 | 245 | 10 |
| S165 | 1691 | 23 |
| S166 | 109 | 6 |
| S167 | 245 | 10 |
| S168 | 170 | 8 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-03
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   981 | WARN | <<<
| Missing exit records (post) |   981 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |   118 | INFO |
| Total closed lots           |  1823 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-03_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-03_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=871 med=-46.9% | TAINTED n=1766 med=-39.2% | KEEP-only n=355 med=+37.7% | KILL=19 KEEP=14
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.37 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260903T130600Z

- UTC timestamp: `20260903T130600Z`
- GitHub run: [#8921](https://github.com/28twagg-ops/TradingBot/actions/runs/33758999109)
- Run id: `33758999109`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`13s`
- Full logs: `logs/action_runs/20260903T130600Z_live_bot.log`, `logs/action_runs/20260903T130600Z_live_options.log`, `logs/action_runs/20260903T130600Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 871 | 42.5 | -46.9 | +15.6 | $+8,494 |
| TAINTED | 1766 | 33.1 | -39.2 | +12.2 | $-9,184 |
| KEEP-only | 355 | 62.0 | +37.7 | +41.1 | $+5,979 |
| KEEP-only recent | 167 | 57.5 | +50.0 | +46.5 | $+1,953 |

- KEEP strategies (14): S173, S174, S210, S218, S350, S362, S363, S364, S397, S398, S401, S404, S406, S412
- KILL strategies (19): ORPHAN, S165, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S360, S399, S403, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-03T09:06:06.263970-04:00","date":"2026-09-03","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.8,"phases_s":{"reconcile":0.19},"signals":0,"placed":0,"equity":999486.18,"open_positions":26,"pending_orders":0,"open_lots":118,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"8921","github_run_id":"33758999109","status":"ok","data_quality":{"clean":{"n":871,"win":42.48,"med":-46.88,"avg":15.58,"pnl":8493.53},"tainted":{"n":1766,"win":33.07,"med":-39.16,"avg":12.18,"pnl":-9184.34},"keep_only":{"n":355,"win":61.97,"med":37.69,"avg":41.06,"pnl":5979.45},"keep_only_recent":{"n":167,"win":57.49,"med":50.0,"avg":46.53,"pnl":1953.0},"keep_strategies":["S173","S174","S210","S218","S350","S362","S363","S364","S397","S398","S401","S404","S406","S412"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S360","S399","S403","S405","S407","S408","S411"]}}
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
|  Equity                                                         $230.39|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $230.39|
|  Cash                                                           $195.68|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $34.71|
|  Open P&L                                                        $+0.13|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (1 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AMZN     Pullback50      $34.71     $255.49  $256.46  +0.4%   $+0.13  |
|                                                                        |
|  Total invested                                                  $34.71|
|  Total open P&L                                                  $+0.13|
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
|  2026-09-02  SELL  MO  Pullback50  $34.52  P&L $+0.00                  |
|  2026-09-02  SELL  AES  Pullback50  $34.50  P&L $-0.03                 |
|  2026-09-02  SELL  AES  Pullback50  $34.57  P&L $-0.01                 |
|  2026-09-02  SELL  AIZ  Pullback50  $34.26  P&L $-0.32                 |
|  2026-09-02  SELL  SYNA  MomReversal  $34.43  P&L $-0.27               |
|  2026-09-02  SELL  GME  EarningsDrift  $35.03  P&L $+0.35              |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-03T09:06:03.380917-04:00 share=25% ===
2026-09-03 09:06:03,380 INFO === options_live_micro LIVE 2026-09-03T09:06:03.380917-04:00 share=25% ===
Live account equity $230.39 cash $195.68 #225458845 options_level=3
2026-09-03 09:06:03,466 INFO Live account equity $230.39 cash $195.68 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-03 09:06:03,488 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-03 09:06:03,509 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (153 earlier lines - see full log file)
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    3 |    2 |    7 |    1 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    26 |
| w2     |    6 |    5 |   11 |    5 |    6 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    47 |
| w3     |    7 |    6 |   13 |    4 |    7 |    5 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    53 |
| w4     |    5 |    4 |   10 |    2 |    5 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    40 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 223 | 9 |
| S164 | 245 | 10 |
| S165 | 1691 | 23 |
| S166 | 109 | 6 |
| S167 | 245 | 10 |
| S168 | 170 | 8 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-03
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   981 | WARN | <<<
| Missing exit records (post) |   981 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |   118 | INFO |
| Total closed lots           |  1823 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-03_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-03_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=871 med=-46.9% | TAINTED n=1766 med=-39.2% | KEEP-only n=355 med=+37.7% | KILL=19 KEEP=14
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.39 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260903T131103Z

- UTC timestamp: `20260903T131103Z`
- GitHub run: [#8922](https://github.com/28twagg-ops/TradingBot/actions/runs/33759503789)
- Run id: `33759503789`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`12s`
- Full logs: `logs/action_runs/20260903T131103Z_live_bot.log`, `logs/action_runs/20260903T131103Z_live_options.log`, `logs/action_runs/20260903T131103Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 871 | 42.5 | -46.9 | +15.6 | $+8,494 |
| TAINTED | 1766 | 33.1 | -39.2 | +12.2 | $-9,184 |
| KEEP-only | 355 | 62.0 | +37.7 | +41.1 | $+5,979 |
| KEEP-only recent | 167 | 57.5 | +50.0 | +46.5 | $+1,953 |

- KEEP strategies (14): S173, S174, S210, S218, S350, S362, S363, S364, S397, S398, S401, S404, S406, S412
- KILL strategies (19): ORPHAN, S165, S203, S207, S211, S212, S216, S217, S351, S352, S354, S355, S360, S399, S403, S405, S407, S408, S411
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-03T09:11:08.898724-04:00","date":"2026-09-03","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.8,"phases_s":{"reconcile":0.2},"signals":0,"placed":0,"equity":999486.18,"open_positions":26,"pending_orders":0,"open_lots":118,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"8922","github_run_id":"33759503789","status":"ok","data_quality":{"clean":{"n":871,"win":42.48,"med":-46.88,"avg":15.58,"pnl":8493.53},"tainted":{"n":1766,"win":33.07,"med":-39.16,"avg":12.18,"pnl":-9184.34},"keep_only":{"n":355,"win":61.97,"med":37.69,"avg":41.06,"pnl":5979.45},"keep_only_recent":{"n":167,"win":57.49,"med":50.0,"avg":46.53,"pnl":1953.0},"keep_strategies":["S173","S174","S210","S218","S350","S362","S363","S364","S397","S398","S401","S404","S406","S412"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S216","S217","S351","S352","S354","S355","S360","S399","S403","S405","S407","S408","S411"]}}
```

### Live bot (tail)

```text
13:11:04  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $230.34|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $230.34|
|  Cash                                                           $195.68|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $34.66|
|  Open P&L                                                        $+0.08|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (1 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AMZN     Pullback50      $34.66     $255.49  $256.08  +0.2%   $+0.08  |
|                                                                        |
|  Total invested                                                  $34.66|
|  Total open P&L                                                  $+0.08|
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
|  2026-09-02  SELL  MO  Pullback50  $34.52  P&L $+0.00                  |
|  2026-09-02  SELL  AES  Pullback50  $34.50  P&L $-0.03                 |
|  2026-09-02  SELL  AES  Pullback50  $34.57  P&L $-0.01                 |
|  2026-09-02  SELL  AIZ  Pullback50  $34.26  P&L $-0.32                 |
|  2026-09-02  SELL  SYNA  MomReversal  $34.43  P&L $-0.27               |
|  2026-09-02  SELL  GME  EarningsDrift  $35.03  P&L $+0.35              |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-03T09:11:05.918315-04:00 share=25% ===
2026-09-03 09:11:05,918 INFO === options_live_micro LIVE 2026-09-03T09:11:05.918315-04:00 share=25% ===
Live account equity $230.34 cash $195.68 #225458845 options_level=3
2026-09-03 09:11:06,029 INFO Live account equity $230.34 cash $195.68 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-03 09:11:06,057 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-03 09:11:06,088 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (153 earlier lines - see full log file)
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    3 |    2 |    7 |    1 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    26 |
| w2     |    6 |    5 |   11 |    5 |    6 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    47 |
| w3     |    7 |    6 |   13 |    4 |    7 |    5 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    53 |
| w4     |    5 |    4 |   10 |    2 |    5 |    5 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    40 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 223 | 9 |
| S164 | 245 | 10 |
| S165 | 1691 | 23 |
| S166 | 109 | 6 |
| S167 | 245 | 10 |
| S168 | 170 | 8 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-03
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   981 | WARN | <<<
| Missing exit records (post) |   981 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |   118 | INFO |
| Total closed lots           |  1823 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-03_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-03_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=871 med=-46.9% | TAINTED n=1766 med=-39.2% | KEEP-only n=355 med=+37.7% | KILL=19 KEEP=14
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.34 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---
