# Daily Comprehensive Action Review - 2026-09-24

_Auto-generated from GitHub Actions run output. Each run appends a summary; full stdout is in linked per-run log files._
## Run 20260924T130122Z

- UTC timestamp: `20260924T130122Z`
- GitHub run: [#10899](https://github.com/28twagg-ops/TradingBot/actions/runs/36002691094)
- Run id: `36002691094`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`14s`
- Full logs: `logs/action_runs/20260924T130122Z_live_bot.log`, `logs/action_runs/20260924T130122Z_live_options.log`, `logs/action_runs/20260924T130122Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1403 | 49.0 | -17.2 | +42.9 | $+17,366 |
| TAINTED | 1887 | 33.4 | -38.8 | +12.8 | $-9,483 |
| KEEP-only | 727 | 62.3 | +51.7 | +69.9 | $+11,927 |
| KEEP-only recent | 534 | 60.5 | +54.3 | +81.2 | $+7,682 |

- KEEP strategies (24): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S403, S404, S406, S412
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-24T09:01:28.391945-04:00","date":"2026-09-24","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.4,"phases_s":{"reconcile":0.6},"signals":0,"placed":0,"equity":996694.33,"open_positions":11,"pending_orders":0,"open_lots":18,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10899","github_run_id":"36002691094","status":"ok","data_quality":{"clean":{"n":1403,"win":48.97,"med":-17.19,"avg":42.88,"pnl":17366.16},"tainted":{"n":1887,"win":33.39,"med":-38.81,"avg":12.83,"pnl":-9483.28},"keep_only":{"n":727,"win":62.31,"med":51.72,"avg":69.85,"pnl":11927.45},"keep_only_recent":{"n":534,"win":60.49,"med":54.33,"avg":81.25,"pnl":7682.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:01:23  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.27|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $225.27|
|  Cash                                                           $123.50|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $101.77|
|  Open P&L                                                        $+0.70|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (3 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  COP      Pullback50      $34.19     $127.75  $129.57  +1.4%   $+0.48  |
|  MLM      MomReversal     $33.54     $490.97  $488.91  -0.4%   $-0.14  |
|  MO       Pullback50      $34.04     $68.86   $69.60   +1.1%   $+0.36  |
|                                                                        |
|  Total invested                                                 $101.77|
|  Total open P&L                                                  $+0.70|
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
|  2026-09-23  SELL  ADM  Pullback50  $33.46  P&L $-0.25                 |
|  2026-09-23  SELL  TECH  Pullback50  $33.71  P&L $+0.00                |
|  2026-09-23  SELL  CCL  MomReversal  $11.15  P&L $-0.37                |
|  2026-09-22  SELL  NCLH  MomReversal  $5.11  P&L $-0.03                |
|  2026-09-22  SELL  AME  Pullback50  $33.91  P&L $+0.06                 |
|  2026-09-22  SELL  AMZN  Pullback50  $33.86  P&L $-0.01                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-24T09:01:24.891512-04:00 share=25% ===
2026-09-24 09:01:24,891 INFO === options_live_micro LIVE 2026-09-24T09:01:24.891512-04:00 share=25% ===
Live account equity $225.27 cash $123.50 #225458845 options_level=3
2026-09-24 09:01:25,098 INFO Live account equity $225.27 cash $123.50 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-24 09:01:25,155 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-24 09:01:25,212 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (175 earlier lines - see full log file)

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
## Ledger health — 2026-09-24
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1581 | WARN | <<<
| Missing exit records (post) |  1578 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    18 | INFO |
| Total closed lots           |  2423 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-24_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-24_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1403 med=-17.2% | TAINTED n=1887 med=-38.8% | KEEP-only n=727 med=+51.7% | KILL=19 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=225.27 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260924T130615Z

- UTC timestamp: `20260924T130615Z`
- GitHub run: [#10900](https://github.com/28twagg-ops/TradingBot/actions/runs/36003254864)
- Run id: `36003254864`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`14s`
- Full logs: `logs/action_runs/20260924T130615Z_live_bot.log`, `logs/action_runs/20260924T130615Z_live_options.log`, `logs/action_runs/20260924T130615Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1403 | 49.0 | -17.2 | +42.9 | $+17,366 |
| TAINTED | 1887 | 33.4 | -38.8 | +12.8 | $-9,483 |
| KEEP-only | 727 | 62.3 | +51.7 | +69.9 | $+11,927 |
| KEEP-only recent | 534 | 60.5 | +54.3 | +81.2 | $+7,682 |

- KEEP strategies (24): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S403, S404, S406, S412
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-24T09:06:21.243897-04:00","date":"2026-09-24","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.0,"phases_s":{"reconcile":0.26},"signals":0,"placed":0,"equity":996666.33,"open_positions":11,"pending_orders":0,"open_lots":18,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10900","github_run_id":"36003254864","status":"ok","data_quality":{"clean":{"n":1403,"win":48.97,"med":-17.19,"avg":42.88,"pnl":17366.16},"tainted":{"n":1887,"win":33.39,"med":-38.81,"avg":12.83,"pnl":-9483.28},"keep_only":{"n":727,"win":62.31,"med":51.72,"avg":69.85,"pnl":11927.45},"keep_only_recent":{"n":534,"win":60.49,"med":54.33,"avg":81.25,"pnl":7682.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S401","S405","S407","S408"]}}
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
|  Equity                                                         $225.13|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $225.13|
|  Cash                                                           $123.50|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $101.63|
|  Open P&L                                                        $+0.56|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (3 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  COP      Pullback50      $34.19     $127.75  $129.57  +1.4%   $+0.48  |
|  MLM      MomReversal     $33.54     $490.97  $488.91  -0.4%   $-0.14  |
|  MO       Pullback50      $33.90     $68.86   $69.30   +0.6%   $+0.22  |
|                                                                        |
|  Total invested                                                 $101.63|
|  Total open P&L                                                  $+0.56|
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
|  2026-09-23  SELL  ADM  Pullback50  $33.46  P&L $-0.25                 |
|  2026-09-23  SELL  TECH  Pullback50  $33.71  P&L $+0.00                |
|  2026-09-23  SELL  CCL  MomReversal  $11.15  P&L $-0.37                |
|  2026-09-22  SELL  NCLH  MomReversal  $5.11  P&L $-0.03                |
|  2026-09-22  SELL  AME  Pullback50  $33.91  P&L $+0.06                 |
|  2026-09-22  SELL  AMZN  Pullback50  $33.86  P&L $-0.01                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-24T09:06:17.597251-04:00 share=25% ===
2026-09-24 09:06:17,597 INFO === options_live_micro LIVE 2026-09-24T09:06:17.597251-04:00 share=25% ===
Live account equity $225.13 cash $123.50 #225458845 options_level=3
2026-09-24 09:06:17,723 INFO Live account equity $225.13 cash $123.50 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-24 09:06:17,759 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-24 09:06:17,794 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (175 earlier lines - see full log file)

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
## Ledger health — 2026-09-24
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1581 | WARN | <<<
| Missing exit records (post) |  1578 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    18 | INFO |
| Total closed lots           |  2423 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-24_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-24_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1403 med=-17.2% | TAINTED n=1887 med=-38.8% | KEEP-only n=727 med=+51.7% | KILL=19 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=225.13 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260924T131123Z

- UTC timestamp: `20260924T131123Z`
- GitHub run: [#10901](https://github.com/28twagg-ops/TradingBot/actions/runs/36003805189)
- Run id: `36003805189`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`14s`
- Full logs: `logs/action_runs/20260924T131123Z_live_bot.log`, `logs/action_runs/20260924T131123Z_live_options.log`, `logs/action_runs/20260924T131123Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1403 | 49.0 | -17.2 | +42.9 | $+17,366 |
| TAINTED | 1887 | 33.4 | -38.8 | +12.8 | $-9,483 |
| KEEP-only | 727 | 62.3 | +51.7 | +69.9 | $+11,927 |
| KEEP-only recent | 534 | 60.5 | +54.3 | +81.2 | $+7,682 |

- KEEP strategies (24): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S403, S404, S406, S412
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-24T09:11:29.895809-04:00","date":"2026-09-24","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.4,"phases_s":{"reconcile":0.58},"signals":0,"placed":0,"equity":996627.56,"open_positions":11,"pending_orders":0,"open_lots":18,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10901","github_run_id":"36003805189","status":"ok","data_quality":{"clean":{"n":1403,"win":48.97,"med":-17.19,"avg":42.88,"pnl":17366.16},"tainted":{"n":1887,"win":33.39,"med":-38.81,"avg":12.83,"pnl":-9483.28},"keep_only":{"n":727,"win":62.31,"med":51.72,"avg":69.85,"pnl":11927.45},"keep_only_recent":{"n":534,"win":60.49,"med":54.33,"avg":81.25,"pnl":7682.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:11:24  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.13|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $225.13|
|  Cash                                                           $123.50|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $101.63|
|  Open P&L                                                        $+0.56|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (3 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  COP      Pullback50      $34.19     $127.75  $129.57  +1.4%   $+0.48  |
|  MLM      MomReversal     $33.54     $490.97  $488.91  -0.4%   $-0.14  |
|  MO       Pullback50      $33.90     $68.86   $69.30   +0.6%   $+0.22  |
|                                                                        |
|  Total invested                                                 $101.63|
|  Total open P&L                                                  $+0.56|
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
|  2026-09-23  SELL  ADM  Pullback50  $33.46  P&L $-0.25                 |
|  2026-09-23  SELL  TECH  Pullback50  $33.71  P&L $+0.00                |
|  2026-09-23  SELL  CCL  MomReversal  $11.15  P&L $-0.37                |
|  2026-09-22  SELL  NCLH  MomReversal  $5.11  P&L $-0.03                |
|  2026-09-22  SELL  AME  Pullback50  $33.91  P&L $+0.06                 |
|  2026-09-22  SELL  AMZN  Pullback50  $33.86  P&L $-0.01                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-24T09:11:26.478376-04:00 share=25% ===
2026-09-24 09:11:26,478 INFO === options_live_micro LIVE 2026-09-24T09:11:26.478376-04:00 share=25% ===
Live account equity $225.13 cash $123.50 #225458845 options_level=3
2026-09-24 09:11:26,735 INFO Live account equity $225.13 cash $123.50 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-24 09:11:26,814 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-24 09:11:26,894 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (175 earlier lines - see full log file)

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
## Ledger health — 2026-09-24
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1581 | WARN | <<<
| Missing exit records (post) |  1578 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    18 | INFO |
| Total closed lots           |  2423 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-24_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-24_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1403 med=-17.2% | TAINTED n=1887 med=-38.8% | KEEP-only n=727 med=+51.7% | KILL=19 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=225.13 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260924T131619Z

- UTC timestamp: `20260924T131619Z`
- GitHub run: [#10902](https://github.com/28twagg-ops/TradingBot/actions/runs/36004364590)
- Run id: `36004364590`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`14s`
- Full logs: `logs/action_runs/20260924T131619Z_live_bot.log`, `logs/action_runs/20260924T131619Z_live_options.log`, `logs/action_runs/20260924T131619Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1403 | 49.0 | -17.2 | +42.9 | $+17,366 |
| TAINTED | 1887 | 33.4 | -38.8 | +12.8 | $-9,483 |
| KEEP-only | 727 | 62.3 | +51.7 | +69.9 | $+11,927 |
| KEEP-only recent | 534 | 60.5 | +54.3 | +81.2 | $+7,682 |

- KEEP strategies (24): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S403, S404, S406, S412
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-24T09:16:25.831850-04:00","date":"2026-09-24","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.3,"phases_s":{"reconcile":0.46},"signals":0,"placed":0,"equity":996646.33,"open_positions":11,"pending_orders":0,"open_lots":18,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10902","github_run_id":"36004364590","status":"ok","data_quality":{"clean":{"n":1403,"win":48.97,"med":-17.19,"avg":42.88,"pnl":17366.16},"tainted":{"n":1887,"win":33.39,"med":-38.81,"avg":12.83,"pnl":-9483.28},"keep_only":{"n":727,"win":62.31,"med":51.72,"avg":69.85,"pnl":11927.45},"keep_only_recent":{"n":534,"win":60.49,"med":54.33,"avg":81.25,"pnl":7682.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:16:20  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.24|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $225.24|
|  Cash                                                           $123.50|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $101.74|
|  Open P&L                                                        $+0.67|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (3 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  COP      Pullback50      $34.20     $127.75  $129.62  +1.5%   $+0.49  |
|  MLM      MomReversal     $33.54     $490.97  $488.91  -0.4%   $-0.14  |
|  MO       Pullback50      $33.99     $68.86   $69.50   +0.9%   $+0.31  |
|                                                                        |
|  Total invested                                                 $101.74|
|  Total open P&L                                                  $+0.67|
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
|  2026-09-23  SELL  ADM  Pullback50  $33.46  P&L $-0.25                 |
|  2026-09-23  SELL  TECH  Pullback50  $33.71  P&L $+0.00                |
|  2026-09-23  SELL  CCL  MomReversal  $11.15  P&L $-0.37                |
|  2026-09-22  SELL  NCLH  MomReversal  $5.11  P&L $-0.03                |
|  2026-09-22  SELL  AME  Pullback50  $33.91  P&L $+0.06                 |
|  2026-09-22  SELL  AMZN  Pullback50  $33.86  P&L $-0.01                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-24T09:16:22.319125-04:00 share=25% ===
2026-09-24 09:16:22,319 INFO === options_live_micro LIVE 2026-09-24T09:16:22.319125-04:00 share=25% ===
Live account equity $225.24 cash $123.50 #225458845 options_level=3
2026-09-24 09:16:22,514 INFO Live account equity $225.24 cash $123.50 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-24 09:16:22,568 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-24 09:16:22,621 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (175 earlier lines - see full log file)

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
## Ledger health — 2026-09-24
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1581 | WARN | <<<
| Missing exit records (post) |  1578 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    18 | INFO |
| Total closed lots           |  2423 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-24_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-24_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1403 med=-17.2% | TAINTED n=1887 med=-38.8% | KEEP-only n=727 med=+51.7% | KILL=19 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=225.24 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260924T132117Z

- UTC timestamp: `20260924T132117Z`
- GitHub run: [#10903](https://github.com/28twagg-ops/TradingBot/actions/runs/36004930816)
- Run id: `36004930816`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`11s`
- Full logs: `logs/action_runs/20260924T132117Z_live_bot.log`, `logs/action_runs/20260924T132117Z_live_options.log`, `logs/action_runs/20260924T132117Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1403 | 49.0 | -17.2 | +42.9 | $+17,366 |
| TAINTED | 1887 | 33.4 | -38.8 | +12.8 | $-9,483 |
| KEEP-only | 727 | 62.3 | +51.7 | +69.9 | $+11,927 |
| KEEP-only recent | 534 | 60.5 | +54.3 | +81.2 | $+7,682 |

- KEEP strategies (24): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S403, S404, S406, S412
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-24T09:21:23.610787-04:00","date":"2026-09-24","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.1,"phases_s":{"reconcile":0.44},"signals":0,"placed":0,"equity":996628.33,"open_positions":11,"pending_orders":0,"open_lots":18,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10903","github_run_id":"36004930816","status":"ok","data_quality":{"clean":{"n":1403,"win":48.97,"med":-17.19,"avg":42.88,"pnl":17366.16},"tainted":{"n":1887,"win":33.39,"med":-38.81,"avg":12.83,"pnl":-9483.28},"keep_only":{"n":727,"win":62.31,"med":51.72,"avg":69.85,"pnl":11927.45},"keep_only_recent":{"n":534,"win":60.49,"med":54.33,"avg":81.25,"pnl":7682.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:21:18  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.24|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $225.24|
|  Cash                                                           $123.50|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $101.74|
|  Open P&L                                                        $+0.67|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (3 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  COP      Pullback50      $34.20     $127.75  $129.62  +1.5%   $+0.49  |
|  MLM      MomReversal     $33.54     $490.97  $488.91  -0.4%   $-0.14  |
|  MO       Pullback50      $33.99     $68.86   $69.50   +0.9%   $+0.31  |
|                                                                        |
|  Total invested                                                 $101.74|
|  Total open P&L                                                  $+0.67|
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
|  2026-09-23  SELL  ADM  Pullback50  $33.46  P&L $-0.25                 |
|  2026-09-23  SELL  TECH  Pullback50  $33.71  P&L $+0.00                |
|  2026-09-23  SELL  CCL  MomReversal  $11.15  P&L $-0.37                |
|  2026-09-22  SELL  NCLH  MomReversal  $5.11  P&L $-0.03                |
|  2026-09-22  SELL  AME  Pullback50  $33.91  P&L $+0.06                 |
|  2026-09-22  SELL  AMZN  Pullback50  $33.86  P&L $-0.01                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-24T09:21:20.270339-04:00 share=25% ===
2026-09-24 09:21:20,270 INFO === options_live_micro LIVE 2026-09-24T09:21:20.270339-04:00 share=25% ===
Live account equity $225.24 cash $123.50 #225458845 options_level=3
2026-09-24 09:21:20,476 INFO Live account equity $225.24 cash $123.50 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-24 09:21:20,534 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-24 09:21:20,592 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (175 earlier lines - see full log file)

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
## Ledger health — 2026-09-24
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1581 | WARN | <<<
| Missing exit records (post) |  1578 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    18 | INFO |
| Total closed lots           |  2423 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-24_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-24_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1403 med=-17.2% | TAINTED n=1887 med=-38.8% | KEEP-only n=727 med=+51.7% | KILL=19 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=225.24 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260924T132626Z

- UTC timestamp: `20260924T132626Z`
- GitHub run: [#10904](https://github.com/28twagg-ops/TradingBot/actions/runs/36005507693)
- Run id: `36005507693`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`10s`
- Full logs: `logs/action_runs/20260924T132626Z_live_bot.log`, `logs/action_runs/20260924T132626Z_live_options.log`, `logs/action_runs/20260924T132626Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1403 | 49.0 | -17.2 | +42.9 | $+17,366 |
| TAINTED | 1887 | 33.4 | -38.8 | +12.8 | $-9,483 |
| KEEP-only | 727 | 62.3 | +51.7 | +69.9 | $+11,927 |
| KEEP-only recent | 534 | 60.5 | +54.3 | +81.2 | $+7,682 |

- KEEP strategies (24): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S403, S404, S406, S412
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-24T09:26:33.290399-04:00","date":"2026-09-24","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.3},"signals":0,"placed":0,"equity":996607.46,"open_positions":11,"pending_orders":0,"open_lots":18,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10904","github_run_id":"36005507693","status":"ok","data_quality":{"clean":{"n":1403,"win":48.97,"med":-17.19,"avg":42.88,"pnl":17366.16},"tainted":{"n":1887,"win":33.39,"med":-38.81,"avg":12.83,"pnl":-9483.28},"keep_only":{"n":727,"win":62.31,"med":51.72,"avg":69.85,"pnl":11927.45},"keep_only_recent":{"n":534,"win":60.49,"med":54.33,"avg":81.25,"pnl":7682.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S401","S405","S407","S408"]}}
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
|  Equity                                                         $225.19|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $225.19|
|  Cash                                                           $123.50|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $101.69|
|  Open P&L                                                        $+0.62|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (3 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  COP      Pullback50      $34.20     $127.75  $129.62  +1.5%   $+0.49  |
|  MLM      MomReversal     $33.54     $490.97  $488.91  -0.4%   $-0.14  |
|  MO       Pullback50      $33.95     $68.86   $69.41   +0.8%   $+0.27  |
|                                                                        |
|  Total invested                                                 $101.69|
|  Total open P&L                                                  $+0.62|
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
|  2026-09-23  SELL  ADM  Pullback50  $33.46  P&L $-0.25                 |
|  2026-09-23  SELL  TECH  Pullback50  $33.71  P&L $+0.00                |
|  2026-09-23  SELL  CCL  MomReversal  $11.15  P&L $-0.37                |
|  2026-09-22  SELL  NCLH  MomReversal  $5.11  P&L $-0.03                |
|  2026-09-22  SELL  AME  Pullback50  $33.91  P&L $+0.06                 |
|  2026-09-22  SELL  AMZN  Pullback50  $33.86  P&L $-0.01                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-24T09:26:30.069946-04:00 share=25% ===
2026-09-24 09:26:30,070 INFO === options_live_micro LIVE 2026-09-24T09:26:30.069946-04:00 share=25% ===
Live account equity $225.19 cash $123.50 #225458845 options_level=3
2026-09-24 09:26:30,495 INFO Live account equity $225.19 cash $123.50 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-24 09:26:30,545 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-24 09:26:30,583 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (175 earlier lines - see full log file)

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
## Ledger health — 2026-09-24
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1581 | WARN | <<<
| Missing exit records (post) |  1578 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    18 | INFO |
| Total closed lots           |  2423 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-24_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-24_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1403 med=-17.2% | TAINTED n=1887 med=-38.8% | KEEP-only n=727 med=+51.7% | KILL=19 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=225.19 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260924T133118Z

- UTC timestamp: `20260924T133118Z`
- GitHub run: [#10905](https://github.com/28twagg-ops/TradingBot/actions/runs/36006079385)
- Run id: `36006079385`
- Live bot: exit=`0`, duration=`217s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260924T133118Z_live_bot.log`, `logs/action_runs/20260924T133118Z_live_options.log`, `logs/action_runs/20260924T133118Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1403 | 49.0 | -17.2 | +42.9 | $+17,366 |
| TAINTED | 1887 | 33.4 | -38.8 | +12.8 | $-9,483 |
| KEEP-only | 727 | 62.3 | +51.7 | +69.9 | $+11,927 |
| KEEP-only recent | 534 | 60.5 | +54.3 | +81.2 | $+7,682 |

- KEEP strategies (24): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S403, S404, S406, S412
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-24T09:26:33.290399-04:00","date":"2026-09-24","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.3},"signals":0,"placed":0,"equity":996607.46,"open_positions":11,"pending_orders":0,"open_lots":18,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10904","github_run_id":"36005507693","status":"ok","data_quality":{"clean":{"n":1403,"win":48.97,"med":-17.19,"avg":42.88,"pnl":17366.16},"tainted":{"n":1887,"win":33.39,"med":-38.81,"avg":12.83,"pnl":-9483.28},"keep_only":{"n":727,"win":62.31,"med":51.72,"avg":69.85,"pnl":11927.45},"keep_only_recent":{"n":534,"win":60.49,"med":54.33,"avg":81.25,"pnl":7682.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:31:19  INFO      Mode: morning_prep
13:31:20  INFO        [prep_positions] 3/3 (3 valid)
13:31:20  INFO      Fetching tickers (universe=both)...
13:31:21  INFO        S&P 500: 503
13:31:21  INFO        MidCap 400: 400
13:31:21  INFO        Total: 901 tickers
13:31:22  INFO        [prep_universe] 40/898 (40 valid)
13:31:23  INFO        [prep_universe] 80/898 (80 valid)
13:31:25  INFO        [prep_universe] 120/898 (120 valid)
13:31:26  INFO        [prep_universe] 160/898 (160 valid)
13:31:28  INFO        [prep_universe] 200/898 (199 valid)
13:31:35  INFO        [prep_universe] 240/898 (238 valid)
13:31:49  INFO        [prep_universe] 280/898 (278 valid)
13:31:59  INFO        [prep_universe] 320/898 (318 valid)
13:32:10  INFO        [prep_universe] 360/898 (358 valid)
13:32:23  INFO        [prep_universe] 400/898 (398 valid)
13:32:36  INFO        [prep_universe] 440/898 (438 valid)
13:32:47  INFO        [prep_universe] 480/898 (478 valid)
13:33:00  INFO        [prep_universe] 520/898 (518 valid)
13:33:11  INFO        [prep_universe] 560/898 (558 valid)
13:33:24  INFO        [prep_universe] 600/898 (598 valid)
13:33:34  INFO        [prep_universe] 640/898 (638 valid)
13:33:48  INFO        [prep_universe] 680/898 (678 valid)
13:33:58  INFO        [prep_universe] 720/898 (718 valid)
13:34:11  INFO        [prep_universe] 760/898 (758 valid)
13:34:22  INFO        [prep_universe] 800/898 (798 valid)
13:34:35  INFO        [prep_universe] 840/898 (838 valid)
13:34:46  INFO        [prep_universe] 880/898 (878 valid)
13:34:53  INFO        [prep_universe] 898/898 (896 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.11|
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
|  Open positions                                                       3|
|  Invested                                                       $101.61|
|  Open P&L                                                        $+0.54|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  COP      Pullback50      $34.12     $127.75  $129.29  +1.2%   $+0.41  |
|  MLM      MomReversal     $33.53     $490.97  $488.83  -0.4%   $-0.15  |
|  MO       Pullback50      $33.96     $68.86   $69.44   +0.8%   $+0.28  |
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
|  Signal candidates                                                   33|
|  Universe scanned                                                   898|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-24T09:34:56.175139-04:00 share=25% ===
2026-09-24 09:34:56,175 INFO === options_live_micro LIVE 2026-09-24T09:34:56.175139-04:00 share=25% ===
Live account equity $225.24 cash $123.50 #225458845 options_level=3
2026-09-24 09:34:56,417 INFO Live account equity $225.24 cash $123.50 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-24 09:34:56,638 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-24 09:34:56,783 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=18 paper_keys=yes dry_run=False
  alpaca positions=12
  FLAG b367|S361|dac1f5d6 missing from Alpaca
  FLAG b366|S361|9565c242 missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$996,829.20
  buying_power=$3,943,130.40 cash=$1,031,588.20
  open option orders: 4
    MCD260925C00272500 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=0.01
    XOM260925C00167500 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
    COIN260925C00217500 OrderSide.SELL qty=2 status=OrderStatus.NEW limit=None
    MARA260925C00011000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
  open option positions: 11
    BAC260925C00058000 qty=1 mkt=$2.00
    COIN260925C00217500 qty=2 mkt=$64.00
    COIN260925C00230000 qty=1 mkt=$5.00
    MARA260925C00011500 qty=-1 mkt=$-199.00
    MARA260925C00012000 qty=-1 mkt=$-150.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-24T09:35:00.444134-04:00 ===

[Run context]
Paper auth OK — equity $996837.77, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
2026-09-24 09:35:03,236 INFO   EXIT [b858|lab0858_s408_w2_1005_1045_r1|S408] stop_loss (-66.7%) SELL 1 COIN260925C00230000 @<= 0.02
2026-09-24 09:35:03,950 INFO   EXIT [b182|lab0182_s217_w3_1045_1120_r1|S217] stop_loss (-50.0%) SELL 1 BAC260925C00058000 @<= 0.03
2026-09-24 09:35:04,651 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-90.0%) SELL 1 MS260925C00210000 @<= 0.02
  EXIT [b434|lab0434_s366_w2_1005_1045_r1|S366] take_profit (+93.3%) SELL failed MARA260925C00012500: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b433|lab0433_s366_w1_0928_1005_r2|S366] take_profit (+93.3%) SELL failed MARA260925C00012500: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b432|lab0432_s366_w1_0928_1005_r1|S366] take_profit (+93.3%) SELL failed MARA260925C00012500: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
Protective stops: placed=0 upgraded=0 already=5 failed=3 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
```

---

## Run 20260924T133703Z

- UTC timestamp: `20260924T133703Z`
- GitHub run: [#10906](https://github.com/28twagg-ops/TradingBot/actions/runs/36006643562)
- Run id: `36006643562`
- Live bot: exit=`0`, duration=`216s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260924T133703Z_live_bot.log`, `logs/action_runs/20260924T133703Z_live_options.log`, `logs/action_runs/20260924T133703Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1403 | 49.0 | -17.2 | +42.9 | $+17,366 |
| TAINTED | 1887 | 33.4 | -38.8 | +12.8 | $-9,483 |
| KEEP-only | 727 | 62.3 | +51.7 | +69.9 | $+11,927 |
| KEEP-only recent | 534 | 60.5 | +54.3 | +81.2 | $+7,682 |

- KEEP strategies (24): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S403, S404, S406, S412
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-24T09:26:33.290399-04:00","date":"2026-09-24","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.3},"signals":0,"placed":0,"equity":996607.46,"open_positions":11,"pending_orders":0,"open_lots":18,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10904","github_run_id":"36005507693","status":"ok","data_quality":{"clean":{"n":1403,"win":48.97,"med":-17.19,"avg":42.88,"pnl":17366.16},"tainted":{"n":1887,"win":33.39,"med":-38.81,"avg":12.83,"pnl":-9483.28},"keep_only":{"n":727,"win":62.31,"med":51.72,"avg":69.85,"pnl":11927.45},"keep_only_recent":{"n":534,"win":60.49,"med":54.33,"avg":81.25,"pnl":7682.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:37:04  INFO      Mode: morning_prep
13:37:06  INFO        [prep_positions] 3/3 (3 valid)
13:37:06  INFO      Fetching tickers (universe=both)...
13:37:06  INFO        S&P 500: 503
13:37:06  INFO        MidCap 400: 400
13:37:06  INFO        Total: 901 tickers
13:37:07  INFO        [prep_universe] 40/898 (40 valid)
13:37:09  INFO        [prep_universe] 80/898 (80 valid)
13:37:10  INFO        [prep_universe] 120/898 (120 valid)
13:37:12  INFO        [prep_universe] 160/898 (160 valid)
13:37:13  INFO        [prep_universe] 200/898 (199 valid)
13:37:21  INFO        [prep_universe] 240/898 (238 valid)
13:37:31  INFO        [prep_universe] 280/898 (278 valid)
13:37:44  INFO        [prep_universe] 320/898 (318 valid)
13:37:57  INFO        [prep_universe] 360/898 (358 valid)
13:38:08  INFO        [prep_universe] 400/898 (398 valid)
13:38:21  INFO        [prep_universe] 440/898 (438 valid)
13:38:31  INFO        [prep_universe] 480/898 (478 valid)
13:38:45  INFO        [prep_universe] 520/898 (518 valid)
13:38:55  INFO        [prep_universe] 560/898 (558 valid)
13:39:08  INFO        [prep_universe] 600/898 (598 valid)
13:39:22  INFO        [prep_universe] 640/898 (638 valid)
13:39:32  INFO        [prep_universe] 680/898 (678 valid)
13:39:45  INFO        [prep_universe] 720/898 (718 valid)
13:39:55  INFO        [prep_universe] 760/898 (758 valid)
13:40:09  INFO        [prep_universe] 800/898 (798 valid)
13:40:19  INFO        [prep_universe] 840/898 (838 valid)
13:40:32  INFO        [prep_universe] 880/898 (878 valid)
13:40:36  INFO        [prep_universe] 898/898 (896 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:37 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.34|
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
|  Open positions                                                       3|
|  Invested                                                       $101.84|
|  Open P&L                                                        $+0.77|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  COP      Pullback50      $34.17     $127.75  $129.49  +1.4%   $+0.46  |
|  MLM      MomReversal     $33.54     $490.97  $488.93  -0.4%   $-0.14  |
|  MO       Pullback50      $34.13     $68.86   $69.77   +1.3%   $+0.45  |
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
|  Signal candidates                                                   33|
|  Universe scanned                                                   898|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-24T09:40:39.927926-04:00 share=25% ===
2026-09-24 09:40:39,927 INFO === options_live_micro LIVE 2026-09-24T09:40:39.927926-04:00 share=25% ===
Live account equity $225.36 cash $123.50 #225458845 options_level=3
2026-09-24 09:40:40,355 INFO Live account equity $225.36 cash $123.50 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-24 09:40:40,533 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-24 09:40:40,648 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=18 paper_keys=yes dry_run=False
  alpaca positions=10
  FLAG b915|S412|0987e7a6 missing from Alpaca
  FLAG b914|S412|857c33cc missing from Alpaca
  FLAG b859|S408|fd45af48 missing from Alpaca
  FLAG b858|S408|753d233a missing from Alpaca
  FLAG b367|S361|dac1f5d6 missing from Alpaca
  FLAG b366|S361|9565c242 missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE OK: paper account status=AccountStatus.ACTIVE equity=$996,751.63
  buying_power=$3,943,045.12 cash=$1,031,635.13
  open option orders: 5
    MS260925C00210000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=0.02
    BAC260925C00058000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=0.03
    MCD260925C00272500 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=0.01
    XOM260925C00167500 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
    MARA260925C00011000 OrderSide.SELL qty=1 status=OrderStatus.NEW limit=None
  open option positions: 9
    BAC260925C00058000 qty=1 mkt=$2.00
    MARA260925C00011500 qty=-1 mkt=$-220.00
    MARA260925C00012000 qty=-1 mkt=$-167.00
    MARA260925C00012500 qty=3 mkt=$318.00
    MCD260925C00272500 qty=1 mkt=$0.00
PROBE: check-only pass (use --smoke-entry to place a test order)
=== options_morning_bot (PAPER) 2026-09-24T09:40:43.900534-04:00 ===

[Run context]
Paper auth OK — equity $996755.13, account PA33P8KT02IL

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
  EXIT [b434|lab0434_s366_w2_1005_1045_r1|S366] take_profit (+113.4%) SELL failed MARA260925C00012500: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b433|lab0433_s366_w1_0928_1005_r2|S366] take_profit (+113.4%) SELL failed MARA260925C00012500: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b432|lab0432_s366_w1_0928_1005_r1|S366] take_profit (+113.4%) SELL failed MARA260925C00012500: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
Protective stops: placed=0 upgraded=0 already=4 failed=2 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
```

---

## Run 20260924T134236Z

- UTC timestamp: `20260924T134236Z`
- GitHub run: [#10907](https://github.com/28twagg-ops/TradingBot/actions/runs/36007222529)
- Run id: `36007222529`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260924T134236Z_live_bot.log`, `logs/action_runs/20260924T134236Z_live_options.log`, `logs/action_runs/20260924T134236Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1403 | 49.0 | -17.2 | +42.9 | $+17,366 |
| TAINTED | 1887 | 33.4 | -38.8 | +12.8 | $-9,483 |
| KEEP-only | 727 | 62.3 | +51.7 | +69.9 | $+11,927 |
| KEEP-only recent | 534 | 60.5 | +54.3 | +81.2 | $+7,682 |

- KEEP strategies (24): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S403, S404, S406, S412
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-24T09:26:33.290399-04:00","date":"2026-09-24","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.3},"signals":0,"placed":0,"equity":996607.46,"open_positions":11,"pending_orders":0,"open_lots":18,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10904","github_run_id":"36005507693","status":"ok","data_quality":{"clean":{"n":1403,"win":48.97,"med":-17.19,"avg":42.88,"pnl":17366.16},"tainted":{"n":1887,"win":33.39,"med":-38.81,"avg":12.83,"pnl":-9483.28},"keep_only":{"n":727,"win":62.31,"med":51.72,"avg":69.85,"pnl":11927.45},"keep_only_recent":{"n":534,"win":60.49,"med":54.33,"avg":81.25,"pnl":7682.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:42:37  INFO      Mode: morning_prep
13:42:38  INFO        [prep_positions] 3/3 (3 valid)
13:42:38  INFO        Universe cache hit: 901 tickers (tickers_2026-09-24.json)
13:42:39  INFO        [prep_universe] 40/898 (40 valid)
13:42:40  INFO        [prep_universe] 80/898 (80 valid)
13:42:41  INFO        [prep_universe] 120/898 (120 valid)
13:42:43  INFO        [prep_universe] 160/898 (160 valid)
13:42:44  INFO        [prep_universe] 200/898 (199 valid)
13:42:54  INFO        [prep_universe] 240/898 (238 valid)
13:43:04  INFO        [prep_universe] 280/898 (278 valid)
13:43:17  INFO        [prep_universe] 320/898 (318 valid)
13:43:30  INFO        [prep_universe] 360/898 (358 valid)
13:43:40  INFO        [prep_universe] 400/898 (398 valid)
13:43:53  INFO        [prep_universe] 440/898 (438 valid)
13:44:06  INFO        [prep_universe] 480/898 (478 valid)
13:44:16  INFO        [prep_universe] 520/898 (518 valid)
13:44:29  INFO        [prep_universe] 560/898 (558 valid)
13:44:41  INFO        [prep_universe] 600/898 (598 valid)
13:44:52  INFO        [prep_universe] 640/898 (638 valid)
13:45:05  INFO        [prep_universe] 680/898 (678 valid)
13:45:18  INFO        [prep_universe] 720/898 (718 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20260924T134654Z

- UTC timestamp: `20260924T134654Z`
- GitHub run: [#10908](https://github.com/28twagg-ops/TradingBot/actions/runs/36007810077)
- Run id: `36007810077`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260924T134654Z_live_bot.log`, `logs/action_runs/20260924T134654Z_live_options.log`, `logs/action_runs/20260924T134654Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1403 | 49.0 | -17.2 | +42.9 | $+17,366 |
| TAINTED | 1887 | 33.4 | -38.8 | +12.8 | $-9,483 |
| KEEP-only | 727 | 62.3 | +51.7 | +69.9 | $+11,927 |
| KEEP-only recent | 534 | 60.5 | +54.3 | +81.2 | $+7,682 |

- KEEP strategies (24): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S403, S404, S406, S412
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-24T09:26:33.290399-04:00","date":"2026-09-24","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.3},"signals":0,"placed":0,"equity":996607.46,"open_positions":11,"pending_orders":0,"open_lots":18,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10904","github_run_id":"36005507693","status":"ok","data_quality":{"clean":{"n":1403,"win":48.97,"med":-17.19,"avg":42.88,"pnl":17366.16},"tainted":{"n":1887,"win":33.39,"med":-38.81,"avg":12.83,"pnl":-9483.28},"keep_only":{"n":727,"win":62.31,"med":51.72,"avg":69.85,"pnl":11927.45},"keep_only_recent":{"n":534,"win":60.49,"med":54.33,"avg":81.25,"pnl":7682.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:46:55  INFO      Mode: morning_scan
13:46:56  INFO        [positions] 3/3 (3 valid)
13:46:56  INFO        SELL MARKET [urgent] MLM closed
13:46:58  INFO        TX logged: SELL MLM  P&L -0.8%
13:46:58  INFO        SELL LIMIT MO  qty=0.489122542  limit=$70.17  id=511ed5cf-be00-4c66-a244-25a341e2ac4a
13:47:29  INFO        SELL LIMIT filled MO (confirmed by position check)
13:47:29  INFO        TX logged: SELL MO  P&L 1.93%
13:47:29  INFO        Universe cache hit: 901 tickers (tickers_2026-09-24.json)
13:47:30  INFO        [universe] 40/900 (40 valid)
13:47:31  INFO        [universe] 80/900 (80 valid)
13:47:32  INFO        [universe] 120/900 (120 valid)
13:47:33  INFO        [universe] 160/900 (160 valid)
13:47:35  INFO        [universe] 200/900 (199 valid)
13:47:42  INFO        [universe] 240/900 (238 valid)
13:47:55  INFO        [universe] 280/900 (278 valid)
13:48:08  INFO        [universe] 320/900 (318 valid)
13:48:18  INFO        [universe] 360/900 (358 valid)
13:48:31  INFO        [universe] 400/900 (398 valid)
13:48:41  INFO        [universe] 440/900 (438 valid)
13:48:54  INFO        [universe] 480/900 (478 valid)
13:49:07  INFO        [universe] 520/900 (518 valid)
13:49:17  INFO        [universe] 560/900 (558 valid)
13:49:31  INFO        [universe] 600/900 (598 valid)
13:49:44  INFO        [universe] 640/900 (638 valid)
13:49:54  INFO        [universe] 680/900 (678 valid)
13:50:07  INFO        [universe] 720/900 (718 valid)
13:50:17  INFO        [universe] 760/900 (758 valid)
13:50:30  INFO        [universe] 800/900 (798 valid)
13:50:44  INFO        [universe] 840/900 (838 valid)
13:50:54  INFO        [universe] 880/900 (878 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20260924T135234Z

- UTC timestamp: `20260924T135234Z`
- GitHub run: [#10909](https://github.com/28twagg-ops/TradingBot/actions/runs/36008405096)
- Run id: `36008405096`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260924T135234Z_live_bot.log`, `logs/action_runs/20260924T135234Z_live_options.log`, `logs/action_runs/20260924T135234Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1403 | 49.0 | -17.2 | +42.9 | $+17,366 |
| TAINTED | 1887 | 33.4 | -38.8 | +12.8 | $-9,483 |
| KEEP-only | 727 | 62.3 | +51.7 | +69.9 | $+11,927 |
| KEEP-only recent | 534 | 60.5 | +54.3 | +81.2 | $+7,682 |

- KEEP strategies (24): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S403, S404, S406, S412
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-24T09:26:33.290399-04:00","date":"2026-09-24","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.3},"signals":0,"placed":0,"equity":996607.46,"open_positions":11,"pending_orders":0,"open_lots":18,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10904","github_run_id":"36005507693","status":"ok","data_quality":{"clean":{"n":1403,"win":48.97,"med":-17.19,"avg":42.88,"pnl":17366.16},"tainted":{"n":1887,"win":33.39,"med":-38.81,"avg":12.83,"pnl":-9483.28},"keep_only":{"n":727,"win":62.31,"med":51.72,"avg":69.85,"pnl":11927.45},"keep_only_recent":{"n":534,"win":60.49,"med":54.33,"avg":81.25,"pnl":7682.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:52:35  INFO      Mode: morning_scan
13:52:36  INFO        [positions] 1/1 (1 valid)
13:52:36  INFO        Universe cache hit: 901 tickers (tickers_2026-09-24.json)
13:52:37  INFO        [universe] 40/900 (40 valid)
13:52:39  INFO        [universe] 80/900 (80 valid)
13:52:40  INFO        [universe] 120/900 (120 valid)
13:52:41  INFO        [universe] 160/900 (160 valid)
13:52:43  INFO        [universe] 200/900 (199 valid)
13:52:50  INFO        [universe] 240/900 (238 valid)
13:53:03  INFO        [universe] 280/900 (278 valid)
13:53:18  INFO        [universe] 320/900 (318 valid)
13:53:25  INFO        [universe] 360/900 (358 valid)
13:53:38  INFO        [universe] 400/900 (398 valid)
13:53:49  INFO        [universe] 440/900 (438 valid)
13:54:02  INFO        [universe] 480/900 (478 valid)
13:54:15  INFO        [universe] 520/900 (518 valid)
13:54:25  INFO        [universe] 560/900 (558 valid)
13:54:39  INFO        [universe] 600/900 (598 valid)
13:54:49  INFO        [universe] 640/900 (638 valid)
13:55:02  INFO        [universe] 680/900 (678 valid)
13:55:13  INFO        [universe] 720/900 (718 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20260924T135659Z

- UTC timestamp: `20260924T135659Z`
- GitHub run: [#10910](https://github.com/28twagg-ops/TradingBot/actions/runs/36008996221)
- Run id: `36008996221`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260924T135659Z_live_bot.log`, `logs/action_runs/20260924T135659Z_live_options.log`, `logs/action_runs/20260924T135659Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1403 | 49.0 | -17.2 | +42.9 | $+17,366 |
| TAINTED | 1887 | 33.4 | -38.8 | +12.8 | $-9,483 |
| KEEP-only | 727 | 62.3 | +51.7 | +69.9 | $+11,927 |
| KEEP-only recent | 534 | 60.5 | +54.3 | +81.2 | $+7,682 |

- KEEP strategies (24): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S403, S404, S406, S412
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-24T09:26:33.290399-04:00","date":"2026-09-24","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.3},"signals":0,"placed":0,"equity":996607.46,"open_positions":11,"pending_orders":0,"open_lots":18,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"10904","github_run_id":"36005507693","status":"ok","data_quality":{"clean":{"n":1403,"win":48.97,"med":-17.19,"avg":42.88,"pnl":17366.16},"tainted":{"n":1887,"win":33.39,"med":-38.81,"avg":12.83,"pnl":-9483.28},"keep_only":{"n":727,"win":62.31,"med":51.72,"avg":69.85,"pnl":11927.45},"keep_only_recent":{"n":534,"win":60.49,"med":54.33,"avg":81.25,"pnl":7682.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
... (72 earlier lines - see full log file)

+========================================================================+
|                               PLAN CACHE                               |
+========================================================================+
|  Mode                                                           morning|
|  File                                      logs/plans/morning_plan.json|
|  Use cached plan                                   no (stale (8656.6m))|
+========================================================================+

+========================================================================+
|          EXIT EVALUATION  (EOD -- midline + stop + max-hold)           |
+========================================================================+
|  COP  P&L +1.6%  $+0.52                                            HOLD|
+========================================================================+

+========================================================================+
|                           EXIT EVAL SUMMARY                            |
+========================================================================+
|  Exit eval    attempted 0 | filled 0 | partial 0 | pending 0 | failed 0|
|  Other skips     already logged today 0  |  no price data 0  |  holds 1|
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
|                         SIGNALS FOUND  --  36                          |
+========================================================================+
|  TICKER   STRATEGY        TIER   PRICE    RSI    VOL_Z   TRIGGER       |
+------------------------------------------------------------------------+
|  AES      Pullback50      eq     $14.84   62.8   -2.37   50MA bounce (+|
|  COHR     Pullback50      eq     $295.35  58.5   -2.44   50MA bounce (-|
|  GLW      Pullback50      eq     $153.97  55.3   -2.14   50MA bounce (+|
|  CPAY     Pullback50      eq     $397.37  27.0   -2.63   50MA bounce (-|
|  DRI      Pullback50      eq     $210.88  41.7   -2.14   50MA bounce (-|
|  ECL      Pullback50      eq     $277.78  47.8   -2.34   50MA bounce (-|
|  EG       Pullback50      eq     $375.50  39.4   -1.16   50MA bounce (+|
|  JCI      Pullback50      eq     $144.79  54.4   -2.28   50MA bounce (-|
|  LLY      Pullback50      eq     $1182.~  57.5   -2.53   50MA bounce (+|
|  MAR      Pullback50      eq     $353.79  67.4   -1.92   50MA bounce (+|
|  MA       Pullback50      eq     $564.67  32.9   -2.29   50MA bounce (-|
|  MDLZ     Pullback50      eq     $62.01   54.7   -2.39   50MA bounce (-|
|  OXY      Pullback50      eq     $58.28   41.4   -2.48   50MA bounce (-|
|  PFG      Pullback50      eq     $114.18  37.7   -1.79   50MA bounce (+|
|  DGX      Pullback50      eq     $235.31  45.1   -1.89   50MA bounce (+|
|  RSG      Pullback50      eq     $215.81  32.1   -2.59   50MA bounce (-|
|  VLTO     Pullback50      eq     $96.97   46.2   -1.61   50MA bounce (+|
|  WAB      Pullback50      eq     $291.06  64.8   -2.39   50MA bounce (+|
|  V        Pullback50      eq     $365.24  33.6   -1.52   50MA bounce (-|
|  WELL     Pullback50      eq     $236.54  42.7   -1.51   50MA bounce (-|
|  AIT      Pullback50      eq     $334.83  62.7   -1.61   50MA bounce (-|
|  CLH      Pullback50      eq     $315.19  43.7   -2.80   50MA bounce (+|
|  COKE     Pullback50      eq     $188.91  39.2   -1.27   50MA bounce (-|
|  EGP      Pullback50      eq     $204.91  68.2   -1.43   50MA bounce (+|
|  FLS      Pullback50      eq     $76.41   47.7   -2.82   50MA bounce (+|
|  GEF      Pullback50      eq     $84.81   48.7   -2.49   50MA bounce (+|
|  GHC      Pullback50      eq     $1153.~  60.8   -2.23   50MA bounce (-|
|  KRYS     Pullback50      eq     $342.18  29.4   -1.34   50MA bounce (-|
|  MSA      Pullback50      eq     $183.12  40.5   -1.78   50MA bounce (-|
|  MTSI     Pullback50      eq     $271.06  54.4   -2.10   50MA bounce (-|14:00:37  INFO        BUY  AES  $33.82  [Pullback50]  id=453fc7d4-d9bf-4da7-bc65-35e42ea7e63c
14:00:37  INFO        BUY  COHR  $33.82  [Pullback50]  id=58c57615-1866-4aa9-9b56-c593c0606ec4
14:00:59  INFO        place_all_stops: checking 3 positions...
14:00:59  INFO        STOP-MARKET placed AES  qty=2 (pos=2.2786)  stop=$14.76  id=ece6dc00-a212-48e4-8cc9-2f123fae6f53
14:00:59  INFO        STOP skipped COHR: fractional (0.1141 shares) — software exit will handle it
14:00:59  INFO        STOP skipped COP: fractional (0.2639 shares) — software exit will handle it
14:00:59  INFO        Daily log -> logs/daily/2026-09-24.md
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20260924T140231Z

- UTC timestamp: `20260924T140231Z`
- GitHub run: [#10911](https://github.com/28twagg-ops/TradingBot/actions/runs/36009591963)
- Run id: `36009591963`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`133s`
- Full logs: `logs/action_runs/20260924T140231Z_live_bot.log`, `logs/action_runs/20260924T140231Z_live_options.log`, `logs/action_runs/20260924T140231Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1407 | 48.8 | -20.1 | +42.5 | $+17,321 |
| TAINTED | 1890 | 33.3 | -38.8 | +12.7 | $-9,558 |
| KEEP-only | 729 | 62.1 | +51.6 | +69.5 | $+11,897 |
| KEEP-only recent | 536 | 60.3 | +54.0 | +80.7 | $+7,652 |

- KEEP strategies (24): S163, S167, S168, S173, S174, S210, S218, S350, S352, S353, S356, S357, S359, S361, S362, S364, S365, S397, S398, S399, S403, S404, S406, S412
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S354, S355, S360, S363, S366, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-24T10:02:36.711694-04:00","date":"2026-09-24","mode":"entry+manage","header":"entry+manage (62 new)","elapsed_s":121.9,"phases_s":{"reconcile":0.12,"cancel":0.04,"manage":0.64,"protective_stops":0.12,"scan":52.88,"entries":55.24,"reconcile2":2.55},"signals":243,"placed":62,"equity":996750.63,"open_positions":22,"pending_orders":7,"open_lots":63,"submitted_today":62,"filled_today":55,"unattributed_contracts":0,"top_signals":["S210:NVDA","S165:AMD","S164:AMD","S168:AMD","S167:AMD","S163:AMD","S350:AMD","S351:AMD"],"github_run":"10911","github_run_id":"36009591963","status":"ok","data_quality":{"clean":{"n":1407,"win":48.83,"med":-20.15,"avg":42.55,"pnl":17321.16},"tainted":{"n":1890,"win":33.33,"med":-38.81,"avg":12.73,"pnl":-9558.28},"keep_only":{"n":729,"win":62.14,"med":51.61,"avg":69.46,"pnl":11897.45},"keep_only_recent":{"n":536,"win":60.26,"med":54.05,"avg":80.68,"pnl":7652.0},"keep_strategies":["S163","S167","S168","S173","S174","S210","S218","S350","S352","S353","S356","S357","S359","S361","S362","S364","S365","S397","S398","S399","S403","S404","S406","S412"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S354","S355","S360","S363","S366","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
14:02:32  INFO      Mode: exits
14:02:32  INFO        Daily log -> logs/daily/2026-09-24.md
14:02:32  INFO        Daily log reconciled -> logs/daily/2026-09-24.md (2 ledger rows)
14:02:32  INFO        place_all_stops: checking 3 positions...
14:02:32  INFO        STOP already live AES @ $14.76
14:02:32  INFO        STOP skipped COHR: fractional (0.1141 shares) — software exit will handle it
14:02:32  INFO        STOP skipped COP: fractional (0.2639 shares) — software exit will handle it
14:02:33  INFO        [positions] 3/3 (3 valid)
14:02:33  INFO        Daily log -> logs/daily/2026-09-24.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:02 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.48|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AES  P&L +0.0%  $+0.01                                            HOLD|
|  COHR  P&L +0.1%  $+0.03                                           HOLD|
|  COP  P&L +1.6%  $+0.53                                            HOLD|
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
=== options_live_micro LIVE 2026-09-24T10:02:33.872633-04:00 share=25% ===
2026-09-24 10:02:33,872 INFO === options_live_micro LIVE 2026-09-24T10:02:33.872633-04:00 share=25% ===
Live account equity $225.48 cash $123.59 #225458845 options_level=3
2026-09-24 10:02:33,931 INFO Live account equity $225.48 cash $123.59 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-24 10:02:33,964 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-24 10:02:33,985 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (209 earlier lines - see full log file)
## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 273 | 18 |
| S164 | 311 | 23 |
| S165 | 1739 | 34 |
| S166 | 139 | 10 |
| S167 | 297 | 21 |
| S168 | 216 | 17 |
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
| 2026-09-24 |    2 |    4 |    4 |    0 |    4 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    16 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-24
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     3 | WARN | <<<
| Orphaned lots (post-stable) |  1581 | WARN | <<<
| Missing exit records (post) |  1578 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    63 | INFO |
| Total closed lots           |  2430 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-24_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-24_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1407 med=-20.1% | TAINTED n=1890 med=-38.8% | KEEP-only n=729 med=+51.6% | KILL=19 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=225.48 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---
