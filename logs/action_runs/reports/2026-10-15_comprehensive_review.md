# Daily Comprehensive Action Review - 2026-10-15

_Auto-generated from GitHub Actions run output. Each run appends a summary; full stdout is in linked per-run log files._
## Run 20261015T130150Z

- UTC timestamp: `20261015T130150Z`
- GitHub run: [#12873](https://github.com/28twagg-ops/TradingBot/actions/runs/38739027892)
- Run id: `38739027892`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`14s`
- Full logs: `logs/action_runs/20261015T130150Z_live_bot.log`, `logs/action_runs/20261015T130150Z_live_options.log`, `logs/action_runs/20261015T130150Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1672 | 48.5 | -25.0 | +37.8 | $+18,703 |
| TAINTED | 2000 | 32.4 | -40.3 | +10.9 | $-10,853 |
| KEEP-only | 805 | 61.4 | +51.0 | +56.8 | $+12,726 |
| KEEP-only recent | 612 | 60.0 | +53.3 | +63.6 | $+8,665 |

- KEEP strategies (23): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S411
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-15T09:01:56.591681-04:00","date":"2026-10-15","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.19},"signals":0,"placed":0,"equity":992001.59,"open_positions":7,"pending_orders":0,"open_lots":7,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"12873","github_run_id":"38739027892","status":"ok","data_quality":{"clean":{"n":1672,"win":48.5,"med":-25.0,"avg":37.83,"pnl":18702.83},"tainted":{"n":2000,"win":32.4,"med":-40.34,"avg":10.93,"pnl":-10853.28},"keep_only":{"n":805,"win":61.37,"med":50.98,"avg":56.78,"pnl":12726.45},"keep_only_recent":{"n":612,"win":59.97,"med":53.28,"avg":63.55,"pnl":8665.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:01:52  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.47|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $224.47|
|  Cash                                                           $156.71|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $67.76|
|  Open P&L                                                        $+0.62|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  GS       MomReversal     $33.88     $875.18  $883.26  +0.9%   $+0.31  |
|  KEY      MomReversal     $33.88     $19.69   $19.87   +0.9%   $+0.31  |
|                                                                        |
|  Total invested                                                  $67.76|
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
|  2026-10-14  SELL  APD  Pullback50  $33.53  P&L $-0.03                 |
|  2026-10-14  SELL  BBY  Pullback50  $33.44  P&L $-0.22                 |
|  2026-10-14  SELL  AMZN  Pullback50  $33.53  P&L $-0.13                |
|  2026-10-14  SELL  GS  MomReversal  $33.49  P&L $-0.17                 |
|  2026-10-13  SELL  AMZN  Pullback50  $33.66  P&L $+0.00                |
|  2026-10-13  SELL  ADP  Pullback50  $33.74  P&L $+0.05                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-15T09:01:53.378145-04:00 share=25% ===
2026-10-15 09:01:53,378 INFO === options_live_micro LIVE 2026-10-15T09:01:53.378145-04:00 share=25% ===
Live account equity $224.47 cash $156.71 #225458845 options_level=3
2026-10-15 09:01:53,447 INFO Live account equity $224.47 cash $156.71 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-10-15 09:01:53,461 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-10-15 09:01:53,472 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (188 earlier lines - see full log file)
| S167 | 327 | 28 |
| S168 | 247 | 25 |
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
| 2026-10-02 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-07 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |  1914 | WARN | <<<
| Missing exit records (post) |  1913 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     7 | INFO |
| Total closed lots           |  2783 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1672 med=-25.0% | TAINTED n=2000 med=-40.3% | KEEP-only n=805 med=+51.0% | KILL=21 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.47 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261015T130629Z

- UTC timestamp: `20261015T130629Z`
- GitHub run: [#12874](https://github.com/28twagg-ops/TradingBot/actions/runs/38739721357)
- Run id: `38739721357`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`13s`
- Full logs: `logs/action_runs/20261015T130629Z_live_bot.log`, `logs/action_runs/20261015T130629Z_live_options.log`, `logs/action_runs/20261015T130629Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1672 | 48.5 | -25.0 | +37.8 | $+18,703 |
| TAINTED | 2000 | 32.4 | -40.3 | +10.9 | $-10,853 |
| KEEP-only | 805 | 61.4 | +51.0 | +56.8 | $+12,726 |
| KEEP-only recent | 612 | 60.0 | +53.3 | +63.6 | $+8,665 |

- KEEP strategies (23): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S411
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-15T09:06:34.819263-04:00","date":"2026-10-15","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.8,"phases_s":{"reconcile":0.12},"signals":0,"placed":0,"equity":992015.76,"open_positions":7,"pending_orders":0,"open_lots":7,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"12874","github_run_id":"38739721357","status":"ok","data_quality":{"clean":{"n":1672,"win":48.5,"med":-25.0,"avg":37.83,"pnl":18702.83},"tainted":{"n":2000,"win":32.4,"med":-40.34,"avg":10.93,"pnl":-10853.28},"keep_only":{"n":805,"win":61.37,"med":50.98,"avg":56.78,"pnl":12726.45},"keep_only_recent":{"n":612,"win":59.97,"med":53.28,"avg":63.55,"pnl":8665.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:06:31  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.42|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $224.42|
|  Cash                                                           $156.71|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $67.71|
|  Open P&L                                                        $+0.57|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  GS       MomReversal     $33.83     $875.18  $882.00  +0.8%   $+0.26  |
|  KEY      MomReversal     $33.88     $19.69   $19.87   +0.9%   $+0.31  |
|                                                                        |
|  Total invested                                                  $67.71|
|  Total open P&L                                                  $+0.57|
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
|  2026-10-14  SELL  APD  Pullback50  $33.53  P&L $-0.03                 |
|  2026-10-14  SELL  BBY  Pullback50  $33.44  P&L $-0.22                 |
|  2026-10-14  SELL  AMZN  Pullback50  $33.53  P&L $-0.13                |
|  2026-10-14  SELL  GS  MomReversal  $33.49  P&L $-0.17                 |
|  2026-10-13  SELL  AMZN  Pullback50  $33.66  P&L $+0.00                |
|  2026-10-13  SELL  ADP  Pullback50  $33.74  P&L $+0.05                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-15T09:06:32.213760-04:00 share=25% ===
2026-10-15 09:06:32,213 INFO === options_live_micro LIVE 2026-10-15T09:06:32.213760-04:00 share=25% ===
Live account equity $224.42 cash $156.71 #225458845 options_level=3
2026-10-15 09:06:32,283 INFO Live account equity $224.42 cash $156.71 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-10-15 09:06:32,296 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-10-15 09:06:32,308 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (188 earlier lines - see full log file)
| S167 | 327 | 28 |
| S168 | 247 | 25 |
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
| 2026-10-02 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-07 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |  1914 | WARN | <<<
| Missing exit records (post) |  1913 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     7 | INFO |
| Total closed lots           |  2783 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1672 med=-25.0% | TAINTED n=2000 med=-40.3% | KEEP-only n=805 med=+51.0% | KILL=21 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.42 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261015T131135Z

- UTC timestamp: `20261015T131135Z`
- GitHub run: [#12875](https://github.com/28twagg-ops/TradingBot/actions/runs/38740404121)
- Run id: `38740404121`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`8s`
- Full logs: `logs/action_runs/20261015T131135Z_live_bot.log`, `logs/action_runs/20261015T131135Z_live_options.log`, `logs/action_runs/20261015T131135Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1672 | 48.5 | -25.0 | +37.8 | $+18,703 |
| TAINTED | 2000 | 32.4 | -40.3 | +10.9 | $-10,853 |
| KEEP-only | 805 | 61.4 | +51.0 | +56.8 | $+12,726 |
| KEEP-only recent | 612 | 60.0 | +53.3 | +63.6 | $+8,665 |

- KEEP strategies (23): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S411
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-15T09:11:40.387486-04:00","date":"2026-10-15","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.8,"phases_s":{"reconcile":0.31},"signals":0,"placed":0,"equity":992043.79,"open_positions":7,"pending_orders":0,"open_lots":7,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"12875","github_run_id":"38740404121","status":"ok","data_quality":{"clean":{"n":1672,"win":48.5,"med":-25.0,"avg":37.83,"pnl":18702.83},"tainted":{"n":2000,"win":32.4,"med":-40.34,"avg":10.93,"pnl":-10853.28},"keep_only":{"n":805,"win":61.37,"med":50.98,"avg":56.78,"pnl":12726.45},"keep_only_recent":{"n":612,"win":59.97,"med":53.28,"avg":63.55,"pnl":8665.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:11:36  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.31|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $224.31|
|  Cash                                                           $156.71|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $67.60|
|  Open P&L                                                        $+0.46|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  GS       MomReversal     $33.72     $875.18  $879.00  +0.4%   $+0.15  |
|  KEY      MomReversal     $33.88     $19.69   $19.87   +0.9%   $+0.31  |
|                                                                        |
|  Total invested                                                  $67.60|
|  Total open P&L                                                  $+0.46|
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
|  2026-10-14  SELL  APD  Pullback50  $33.53  P&L $-0.03                 |
|  2026-10-14  SELL  BBY  Pullback50  $33.44  P&L $-0.22                 |
|  2026-10-14  SELL  AMZN  Pullback50  $33.53  P&L $-0.13                |
|  2026-10-14  SELL  GS  MomReversal  $33.49  P&L $-0.17                 |
|  2026-10-13  SELL  AMZN  Pullback50  $33.66  P&L $+0.00                |
|  2026-10-13  SELL  ADP  Pullback50  $33.74  P&L $+0.05                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-15T09:11:38.139634-04:00 share=25% ===
2026-10-15 09:11:38,139 INFO === options_live_micro LIVE 2026-10-15T09:11:38.139634-04:00 share=25% ===
Live account equity $224.31 cash $156.71 #225458845 options_level=3
2026-10-15 09:11:38,283 INFO Live account equity $224.31 cash $156.71 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-10-15 09:11:38,342 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-10-15 09:11:38,381 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (188 earlier lines - see full log file)
| S167 | 327 | 28 |
| S168 | 247 | 25 |
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
| 2026-10-02 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-07 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |  1914 | WARN | <<<
| Missing exit records (post) |  1913 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     7 | INFO |
| Total closed lots           |  2783 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1672 med=-25.0% | TAINTED n=2000 med=-40.3% | KEEP-only n=805 med=+51.0% | KILL=21 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.31 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261015T131637Z

- UTC timestamp: `20261015T131637Z`
- GitHub run: [#12876](https://github.com/28twagg-ops/TradingBot/actions/runs/38741097735)
- Run id: `38741097735`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`13s`
- Full logs: `logs/action_runs/20261015T131637Z_live_bot.log`, `logs/action_runs/20261015T131637Z_live_options.log`, `logs/action_runs/20261015T131637Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1672 | 48.5 | -25.0 | +37.8 | $+18,703 |
| TAINTED | 2000 | 32.4 | -40.3 | +10.9 | $-10,853 |
| KEEP-only | 805 | 61.4 | +51.0 | +56.8 | $+12,726 |
| KEEP-only recent | 612 | 60.0 | +53.3 | +63.6 | $+8,665 |

- KEEP strategies (23): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S411
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-15T09:16:43.381672-04:00","date":"2026-10-15","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.1,"phases_s":{"reconcile":0.44},"signals":0,"placed":0,"equity":991984.79,"open_positions":7,"pending_orders":0,"open_lots":7,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"12876","github_run_id":"38741097735","status":"ok","data_quality":{"clean":{"n":1672,"win":48.5,"med":-25.0,"avg":37.83,"pnl":18702.83},"tainted":{"n":2000,"win":32.4,"med":-40.34,"avg":10.93,"pnl":-10853.28},"keep_only":{"n":805,"win":61.37,"med":50.98,"avg":56.78,"pnl":12726.45},"keep_only_recent":{"n":612,"win":59.97,"med":53.28,"avg":63.55,"pnl":8665.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:16:39  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.31|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $224.31|
|  Cash                                                           $156.71|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $67.60|
|  Open P&L                                                        $+0.46|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  GS       MomReversal     $33.72     $875.18  $879.00  +0.4%   $+0.15  |
|  KEY      MomReversal     $33.88     $19.69   $19.87   +0.9%   $+0.31  |
|                                                                        |
|  Total invested                                                  $67.60|
|  Total open P&L                                                  $+0.46|
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
|  2026-10-14  SELL  APD  Pullback50  $33.53  P&L $-0.03                 |
|  2026-10-14  SELL  BBY  Pullback50  $33.44  P&L $-0.22                 |
|  2026-10-14  SELL  AMZN  Pullback50  $33.53  P&L $-0.13                |
|  2026-10-14  SELL  GS  MomReversal  $33.49  P&L $-0.17                 |
|  2026-10-13  SELL  AMZN  Pullback50  $33.66  P&L $+0.00                |
|  2026-10-13  SELL  ADP  Pullback50  $33.74  P&L $+0.05                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-15T09:16:40.431884-04:00 share=25% ===
2026-10-15 09:16:40,431 INFO === options_live_micro LIVE 2026-10-15T09:16:40.431884-04:00 share=25% ===
Live account equity $224.31 cash $156.71 #225458845 options_level=3
2026-10-15 09:16:40,577 INFO Live account equity $224.31 cash $156.71 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-10-15 09:16:40,614 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-10-15 09:16:40,650 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (188 earlier lines - see full log file)
| S167 | 327 | 28 |
| S168 | 247 | 25 |
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
| 2026-10-02 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-07 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |  1914 | WARN | <<<
| Missing exit records (post) |  1913 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     7 | INFO |
| Total closed lots           |  2783 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1672 med=-25.0% | TAINTED n=2000 med=-40.3% | KEEP-only n=805 med=+51.0% | KILL=21 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.31 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261015T132143Z

- UTC timestamp: `20261015T132143Z`
- GitHub run: [#12877](https://github.com/28twagg-ops/TradingBot/actions/runs/38741794595)
- Run id: `38741794595`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`13s`
- Full logs: `logs/action_runs/20261015T132143Z_live_bot.log`, `logs/action_runs/20261015T132143Z_live_options.log`, `logs/action_runs/20261015T132143Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1672 | 48.5 | -25.0 | +37.8 | $+18,703 |
| TAINTED | 2000 | 32.4 | -40.3 | +10.9 | $-10,853 |
| KEEP-only | 805 | 61.4 | +51.0 | +56.8 | $+12,726 |
| KEEP-only recent | 612 | 60.0 | +53.3 | +63.6 | $+8,665 |

- KEEP strategies (23): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S411
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-15T09:21:48.987179-04:00","date":"2026-10-15","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.08},"signals":0,"placed":0,"equity":991856.79,"open_positions":7,"pending_orders":0,"open_lots":7,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"12877","github_run_id":"38741794595","status":"ok","data_quality":{"clean":{"n":1672,"win":48.5,"med":-25.0,"avg":37.83,"pnl":18702.83},"tainted":{"n":2000,"win":32.4,"med":-40.34,"avg":10.93,"pnl":-10853.28},"keep_only":{"n":805,"win":61.37,"med":50.98,"avg":56.78,"pnl":12726.45},"keep_only_recent":{"n":612,"win":59.97,"med":53.28,"avg":63.55,"pnl":8665.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:21:45  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.27|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $224.27|
|  Cash                                                           $156.71|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $67.56|
|  Open P&L                                                        $+0.42|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  GS       MomReversal     $33.68     $875.18  $878.00  +0.3%   $+0.11  |
|  KEY      MomReversal     $33.88     $19.69   $19.87   +0.9%   $+0.31  |
|                                                                        |
|  Total invested                                                  $67.56|
|  Total open P&L                                                  $+0.42|
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
|  2026-10-14  SELL  APD  Pullback50  $33.53  P&L $-0.03                 |
|  2026-10-14  SELL  BBY  Pullback50  $33.44  P&L $-0.22                 |
|  2026-10-14  SELL  AMZN  Pullback50  $33.53  P&L $-0.13                |
|  2026-10-14  SELL  GS  MomReversal  $33.49  P&L $-0.17                 |
|  2026-10-13  SELL  AMZN  Pullback50  $33.66  P&L $+0.00                |
|  2026-10-13  SELL  ADP  Pullback50  $33.74  P&L $+0.05                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-15T09:21:46.440900-04:00 share=25% ===
2026-10-15 09:21:46,440 INFO === options_live_micro LIVE 2026-10-15T09:21:46.440900-04:00 share=25% ===
Live account equity $224.27 cash $156.71 #225458845 options_level=3
2026-10-15 09:21:46,483 INFO Live account equity $224.27 cash $156.71 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-10-15 09:21:46,492 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-10-15 09:21:46,500 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (188 earlier lines - see full log file)
| S167 | 327 | 28 |
| S168 | 247 | 25 |
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
| 2026-10-02 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-07 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |  1914 | WARN | <<<
| Missing exit records (post) |  1913 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     7 | INFO |
| Total closed lots           |  2783 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1672 med=-25.0% | TAINTED n=2000 med=-40.3% | KEEP-only n=805 med=+51.0% | KILL=21 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.27 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261015T132646Z

- UTC timestamp: `20261015T132646Z`
- GitHub run: [#12878](https://github.com/28twagg-ops/TradingBot/actions/runs/38742501176)
- Run id: `38742501176`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`14s`
- Full logs: `logs/action_runs/20261015T132646Z_live_bot.log`, `logs/action_runs/20261015T132646Z_live_options.log`, `logs/action_runs/20261015T132646Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1672 | 48.5 | -25.0 | +37.8 | $+18,703 |
| TAINTED | 2000 | 32.4 | -40.3 | +10.9 | $-10,853 |
| KEEP-only | 805 | 61.4 | +51.0 | +56.8 | $+12,726 |
| KEEP-only recent | 612 | 60.0 | +53.3 | +63.6 | $+8,665 |

- KEEP strategies (23): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S411
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-15T09:26:51.435393-04:00","date":"2026-10-15","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.19},"signals":0,"placed":0,"equity":991896.52,"open_positions":7,"pending_orders":0,"open_lots":7,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"12878","github_run_id":"38742501176","status":"ok","data_quality":{"clean":{"n":1672,"win":48.5,"med":-25.0,"avg":37.83,"pnl":18702.83},"tainted":{"n":2000,"win":32.4,"med":-40.34,"avg":10.93,"pnl":-10853.28},"keep_only":{"n":805,"win":61.37,"med":50.98,"avg":56.78,"pnl":12726.45},"keep_only_recent":{"n":612,"win":59.97,"med":53.28,"avg":63.55,"pnl":8665.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:26:47  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.25|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $224.25|
|  Cash                                                           $156.71|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $67.54|
|  Open P&L                                                        $+0.40|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  GS       MomReversal     $33.66     $875.18  $877.50  +0.3%   $+0.09  |
|  KEY      MomReversal     $33.88     $19.69   $19.87   +0.9%   $+0.31  |
|                                                                        |
|  Total invested                                                  $67.54|
|  Total open P&L                                                  $+0.40|
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
|  2026-10-14  SELL  APD  Pullback50  $33.53  P&L $-0.03                 |
|  2026-10-14  SELL  BBY  Pullback50  $33.44  P&L $-0.22                 |
|  2026-10-14  SELL  AMZN  Pullback50  $33.53  P&L $-0.13                |
|  2026-10-14  SELL  GS  MomReversal  $33.49  P&L $-0.17                 |
|  2026-10-13  SELL  AMZN  Pullback50  $33.66  P&L $+0.00                |
|  2026-10-13  SELL  ADP  Pullback50  $33.74  P&L $+0.05                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-15T09:26:48.421677-04:00 share=25% ===
2026-10-15 09:26:48,421 INFO === options_live_micro LIVE 2026-10-15T09:26:48.421677-04:00 share=25% ===
Live account equity $224.25 cash $156.71 #225458845 options_level=3
2026-10-15 09:26:48,508 INFO Live account equity $224.25 cash $156.71 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-10-15 09:26:48,530 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-10-15 09:26:48,552 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (188 earlier lines - see full log file)
| S167 | 327 | 28 |
| S168 | 247 | 25 |
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
| 2026-10-02 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-07 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |  1914 | WARN | <<<
| Missing exit records (post) |  1913 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     7 | INFO |
| Total closed lots           |  2783 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1672 med=-25.0% | TAINTED n=2000 med=-40.3% | KEEP-only n=805 med=+51.0% | KILL=21 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.25 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261015T133146Z

- UTC timestamp: `20261015T133146Z`
- GitHub run: [#12879](https://github.com/28twagg-ops/TradingBot/actions/runs/38743211546)
- Run id: `38743211546`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20261015T133146Z_live_bot.log`, `logs/action_runs/20261015T133146Z_live_options.log`, `logs/action_runs/20261015T133146Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1672 | 48.5 | -25.0 | +37.8 | $+18,703 |
| TAINTED | 2000 | 32.4 | -40.3 | +10.9 | $-10,853 |
| KEEP-only | 805 | 61.4 | +51.0 | +56.8 | $+12,726 |
| KEEP-only recent | 612 | 60.0 | +53.3 | +63.6 | $+8,665 |

- KEEP strategies (23): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S411
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-15T09:26:51.435393-04:00","date":"2026-10-15","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.19},"signals":0,"placed":0,"equity":991896.52,"open_positions":7,"pending_orders":0,"open_lots":7,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"12878","github_run_id":"38742501176","status":"ok","data_quality":{"clean":{"n":1672,"win":48.5,"med":-25.0,"avg":37.83,"pnl":18702.83},"tainted":{"n":2000,"win":32.4,"med":-40.34,"avg":10.93,"pnl":-10853.28},"keep_only":{"n":805,"win":61.37,"med":50.98,"avg":56.78,"pnl":12726.45},"keep_only_recent":{"n":612,"win":59.97,"med":53.28,"avg":63.55,"pnl":8665.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:31:47  INFO      Mode: morning_prep
13:31:49  INFO        [prep_positions] 3/3 (3 valid)
13:31:49  INFO      Fetching tickers (universe=both)...
13:31:49  INFO        S&P 500: 503
13:31:49  INFO        MidCap 400: 400
13:31:49  INFO        Total: 903 tickers
13:31:50  INFO        [prep_universe] 40/900 (40 valid)
13:31:52  INFO        [prep_universe] 80/900 (80 valid)
13:31:53  INFO        [prep_universe] 120/900 (120 valid)
13:31:55  INFO        [prep_universe] 160/900 (160 valid)
13:31:56  INFO        [prep_universe] 200/900 (199 valid)
13:32:04  INFO        [prep_universe] 240/900 (238 valid)
13:32:14  INFO        [prep_universe] 280/900 (278 valid)
13:32:28  INFO        [prep_universe] 320/900 (318 valid)
13:32:39  INFO        [prep_universe] 360/900 (358 valid)
13:32:52  INFO        [prep_universe] 400/900 (398 valid)
13:33:03  INFO        [prep_universe] 440/900 (438 valid)
13:33:16  INFO        [prep_universe] 480/900 (477 valid)
13:33:27  INFO        [prep_universe] 520/900 (517 valid)
13:33:40  INFO        [prep_universe] 560/900 (557 valid)
13:33:51  INFO        [prep_universe] 600/900 (597 valid)
13:34:04  INFO        [prep_universe] 640/900 (637 valid)
13:34:15  INFO        [prep_universe] 680/900 (677 valid)
13:34:28  INFO        [prep_universe] 720/900 (717 valid)
13:34:39  INFO        [prep_universe] 760/900 (757 valid)
13:34:52  INFO        [prep_universe] 800/900 (797 valid)
13:35:03  INFO        [prep_universe] 840/900 (837 valid)
13:35:17  INFO        [prep_universe] 880/900 (877 valid)
13:35:21  INFO        [prep_universe] 900/900 (897 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20261015T133731Z

- UTC timestamp: `20261015T133731Z`
- GitHub run: [#12880](https://github.com/28twagg-ops/TradingBot/actions/runs/38743930955)
- Run id: `38743930955`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20261015T133731Z_live_bot.log`, `logs/action_runs/20261015T133731Z_live_options.log`, `logs/action_runs/20261015T133731Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1672 | 48.5 | -25.0 | +37.8 | $+18,703 |
| TAINTED | 2000 | 32.4 | -40.3 | +10.9 | $-10,853 |
| KEEP-only | 805 | 61.4 | +51.0 | +56.8 | $+12,726 |
| KEEP-only recent | 612 | 60.0 | +53.3 | +63.6 | $+8,665 |

- KEEP strategies (23): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S411
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-15T09:26:51.435393-04:00","date":"2026-10-15","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.19},"signals":0,"placed":0,"equity":991896.52,"open_positions":7,"pending_orders":0,"open_lots":7,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"12878","github_run_id":"38742501176","status":"ok","data_quality":{"clean":{"n":1672,"win":48.5,"med":-25.0,"avg":37.83,"pnl":18702.83},"tainted":{"n":2000,"win":32.4,"med":-40.34,"avg":10.93,"pnl":-10853.28},"keep_only":{"n":805,"win":61.37,"med":50.98,"avg":56.78,"pnl":12726.45},"keep_only_recent":{"n":612,"win":59.97,"med":53.28,"avg":63.55,"pnl":8665.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:37:32  INFO      Mode: morning_prep
13:37:34  INFO        [prep_positions] 3/3 (3 valid)
13:37:34  INFO      Fetching tickers (universe=both)...
13:37:34  INFO        S&P 500: 503
13:37:34  INFO        MidCap 400: 400
13:37:34  INFO        Total: 903 tickers
13:37:35  INFO        [prep_universe] 40/900 (40 valid)
13:37:36  INFO        [prep_universe] 80/900 (80 valid)
13:37:38  INFO        [prep_universe] 120/900 (120 valid)
13:37:39  INFO        [prep_universe] 160/900 (160 valid)
13:37:40  INFO        [prep_universe] 200/900 (199 valid)
13:37:48  INFO        [prep_universe] 240/900 (238 valid)
13:38:01  INFO        [prep_universe] 280/900 (278 valid)
13:38:11  INFO        [prep_universe] 320/900 (318 valid)
13:38:25  INFO        [prep_universe] 360/900 (358 valid)
13:38:35  INFO        [prep_universe] 400/900 (398 valid)
13:38:49  INFO        [prep_universe] 440/900 (438 valid)
13:38:59  INFO        [prep_universe] 480/900 (477 valid)
13:39:12  INFO        [prep_universe] 520/900 (517 valid)
13:39:23  INFO        [prep_universe] 560/900 (557 valid)
13:39:36  INFO        [prep_universe] 600/900 (597 valid)
13:39:49  INFO        [prep_universe] 640/900 (637 valid)
13:40:00  INFO        [prep_universe] 680/900 (677 valid)
13:40:13  INFO        [prep_universe] 720/900 (717 valid)
13:40:24  INFO        [prep_universe] 760/900 (757 valid)
13:40:37  INFO        [prep_universe] 800/900 (797 valid)
13:40:48  INFO        [prep_universe] 840/900 (837 valid)
13:41:01  INFO        [prep_universe] 880/900 (877 valid)
13:41:05  INFO        [prep_universe] 900/900 (897 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:37 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.08|
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
|  Invested                                                       $100.96|
|  Open P&L                                                        $+0.22|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  GS       MomReversal     $33.30     $875.18  $868.01  -0.8%   $-0.27  |
|  KEY      MomReversal     $33.63     $19.69   $19.73   +0.2%   $+0.06  |
|  PNC      MomReversal     $34.03     $211.72  $214.41  +1.3%   $+0.43  |
+========================================================================+

+========================================================================+
|                            OPEN SELL ORDERS                            |
+========================================================================+
|  Count                                                                1|
|  TICKER    TYPE              QTY       LIMIT       STOP                |
+------------------------------------------------------------------------+
|  KEY       OrderType.STOP    1         None        19.59               |
+========================================================================+

+========================================================================+
|                              PREP SUMMARY                              |
+========================================================================+
|  Saved                                                              yes|
|  Exit candidates                                                      1|
|  Signal candidates                                                   32|
|  Universe scanned                                                   900|
+========================================================================+
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20261015T134304Z

- UTC timestamp: `20261015T134304Z`
- GitHub run: [#12881](https://github.com/28twagg-ops/TradingBot/actions/runs/38744638319)
- Run id: `38744638319`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20261015T134304Z_live_bot.log`, `logs/action_runs/20261015T134304Z_live_options.log`, `logs/action_runs/20261015T134304Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1672 | 48.5 | -25.0 | +37.8 | $+18,703 |
| TAINTED | 2000 | 32.4 | -40.3 | +10.9 | $-10,853 |
| KEEP-only | 805 | 61.4 | +51.0 | +56.8 | $+12,726 |
| KEEP-only recent | 612 | 60.0 | +53.3 | +63.6 | $+8,665 |

- KEEP strategies (23): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S411
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-15T09:26:51.435393-04:00","date":"2026-10-15","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.19},"signals":0,"placed":0,"equity":991896.52,"open_positions":7,"pending_orders":0,"open_lots":7,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"12878","github_run_id":"38742501176","status":"ok","data_quality":{"clean":{"n":1672,"win":48.5,"med":-25.0,"avg":37.83,"pnl":18702.83},"tainted":{"n":2000,"win":32.4,"med":-40.34,"avg":10.93,"pnl":-10853.28},"keep_only":{"n":805,"win":61.37,"med":50.98,"avg":56.78,"pnl":12726.45},"keep_only_recent":{"n":612,"win":59.97,"med":53.28,"avg":63.55,"pnl":8665.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:43:04  INFO      Mode: morning_prep
13:43:05  INFO        [prep_positions] 3/3 (3 valid)
13:43:05  INFO        Universe cache hit: 903 tickers (tickers_2026-10-15.json)
13:43:06  INFO        [prep_universe] 40/900 (40 valid)
13:43:08  INFO        [prep_universe] 80/900 (80 valid)
13:43:09  INFO        [prep_universe] 120/900 (120 valid)
13:43:10  INFO        [prep_universe] 160/900 (160 valid)
13:43:12  INFO        [prep_universe] 200/900 (199 valid)
13:43:20  INFO        [prep_universe] 240/900 (238 valid)
13:43:33  INFO        [prep_universe] 280/900 (278 valid)
13:43:43  INFO        [prep_universe] 320/900 (318 valid)
13:43:56  INFO        [prep_universe] 360/900 (358 valid)
13:44:09  INFO        [prep_universe] 400/900 (398 valid)
13:44:19  INFO        [prep_universe] 440/900 (438 valid)
13:44:32  INFO        [prep_universe] 480/900 (477 valid)
13:44:43  INFO        [prep_universe] 520/900 (517 valid)
13:44:56  INFO        [prep_universe] 560/900 (557 valid)
13:45:09  INFO        [prep_universe] 600/900 (597 valid)
13:45:19  INFO        [prep_universe] 640/900 (637 valid)
13:45:33  INFO        [prep_universe] 680/900 (677 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20261015T134748Z

- UTC timestamp: `20261015T134748Z`
- GitHub run: [#12882](https://github.com/28twagg-ops/TradingBot/actions/runs/38745358636)
- Run id: `38745358636`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20261015T134748Z_live_bot.log`, `logs/action_runs/20261015T134748Z_live_options.log`, `logs/action_runs/20261015T134748Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1672 | 48.5 | -25.0 | +37.8 | $+18,703 |
| TAINTED | 2000 | 32.4 | -40.3 | +10.9 | $-10,853 |
| KEEP-only | 805 | 61.4 | +51.0 | +56.8 | $+12,726 |
| KEEP-only recent | 612 | 60.0 | +53.3 | +63.6 | $+8,665 |

- KEEP strategies (23): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S411
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-15T09:26:51.435393-04:00","date":"2026-10-15","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.19},"signals":0,"placed":0,"equity":991896.52,"open_positions":7,"pending_orders":0,"open_lots":7,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"12878","github_run_id":"38742501176","status":"ok","data_quality":{"clean":{"n":1672,"win":48.5,"med":-25.0,"avg":37.83,"pnl":18702.83},"tainted":{"n":2000,"win":32.4,"med":-40.34,"avg":10.93,"pnl":-10853.28},"keep_only":{"n":805,"win":61.37,"med":50.98,"avg":56.78,"pnl":12726.45},"keep_only_recent":{"n":612,"win":59.97,"med":53.28,"avg":63.55,"pnl":8665.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:47:51  INFO      Mode: morning_scan
13:47:52  INFO        [positions] 3/3 (3 valid)
13:47:52  INFO        SELL MARKET [urgent] GS closed
13:47:54  INFO        TX logged: SELL GS  P&L -1.4%
13:47:54  INFO        Universe cache hit: 903 tickers (tickers_2026-10-15.json)
13:47:55  INFO        [universe] 40/901 (40 valid)
13:47:56  INFO        [universe] 80/901 (80 valid)
13:47:57  INFO        [universe] 120/901 (120 valid)
13:47:58  INFO        [universe] 160/901 (160 valid)
13:47:59  INFO        [universe] 200/901 (199 valid)
13:48:07  INFO        [universe] 240/901 (238 valid)
13:48:20  INFO        [universe] 280/901 (278 valid)
13:48:33  INFO        [universe] 320/901 (318 valid)
13:48:43  INFO        [universe] 360/901 (358 valid)
13:48:56  INFO        [universe] 400/901 (398 valid)
13:49:07  INFO        [universe] 440/901 (438 valid)
13:49:20  INFO        [universe] 480/901 (477 valid)
13:49:33  INFO        [universe] 520/901 (517 valid)
13:49:43  INFO        [universe] 560/901 (557 valid)
13:49:57  INFO        [universe] 600/901 (597 valid)
13:50:07  INFO        [universe] 640/901 (637 valid)
13:50:20  INFO        [universe] 680/901 (677 valid)
13:50:33  INFO        [universe] 720/901 (717 valid)
13:50:44  INFO        [universe] 760/901 (757 valid)
13:50:57  INFO        [universe] 800/901 (797 valid)
13:51:07  INFO        [universe] 840/901 (837 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20261015T135307Z

- UTC timestamp: `20261015T135307Z`
- GitHub run: [#12883](https://github.com/28twagg-ops/TradingBot/actions/runs/38746072446)
- Run id: `38746072446`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20261015T135307Z_live_bot.log`, `logs/action_runs/20261015T135307Z_live_options.log`, `logs/action_runs/20261015T135307Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1672 | 48.5 | -25.0 | +37.8 | $+18,703 |
| TAINTED | 2000 | 32.4 | -40.3 | +10.9 | $-10,853 |
| KEEP-only | 805 | 61.4 | +51.0 | +56.8 | $+12,726 |
| KEEP-only recent | 612 | 60.0 | +53.3 | +63.6 | $+8,665 |

- KEEP strategies (23): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S411
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-15T09:26:51.435393-04:00","date":"2026-10-15","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.19},"signals":0,"placed":0,"equity":991896.52,"open_positions":7,"pending_orders":0,"open_lots":7,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"12878","github_run_id":"38742501176","status":"ok","data_quality":{"clean":{"n":1672,"win":48.5,"med":-25.0,"avg":37.83,"pnl":18702.83},"tainted":{"n":2000,"win":32.4,"med":-40.34,"avg":10.93,"pnl":-10853.28},"keep_only":{"n":805,"win":61.37,"med":50.98,"avg":56.78,"pnl":12726.45},"keep_only_recent":{"n":612,"win":59.97,"med":53.28,"avg":63.55,"pnl":8665.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:53:08  INFO      Mode: morning_scan
13:53:09  INFO        [positions] 2/2 (2 valid)
13:53:09  INFO        Universe cache hit: 903 tickers (tickers_2026-10-15.json)
13:53:10  INFO        [universe] 40/901 (40 valid)
13:53:12  INFO        [universe] 80/901 (80 valid)
13:53:13  INFO        [universe] 120/901 (120 valid)
13:53:14  INFO        [universe] 160/901 (160 valid)
13:53:16  INFO        [universe] 200/901 (199 valid)
13:53:23  INFO        [universe] 240/901 (238 valid)
13:53:36  INFO        [universe] 280/901 (278 valid)
13:53:47  INFO        [universe] 320/901 (318 valid)
13:54:00  INFO        [universe] 360/901 (358 valid)
13:54:10  INFO        [universe] 400/901 (398 valid)
13:54:24  INFO        [universe] 440/901 (438 valid)
13:54:35  INFO        [universe] 480/901 (477 valid)
13:54:48  INFO        [universe] 520/901 (517 valid)
13:54:59  INFO        [universe] 560/901 (557 valid)
13:55:12  INFO        [universe] 600/901 (597 valid)
13:55:23  INFO        [universe] 640/901 (637 valid)
13:55:36  INFO        [universe] 680/901 (677 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20261015T135734Z

- UTC timestamp: `20261015T135734Z`
- GitHub run: [#12884](https://github.com/28twagg-ops/TradingBot/actions/runs/38746794333)
- Run id: `38746794333`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`79s`
- Full logs: `logs/action_runs/20261015T135734Z_live_bot.log`, `logs/action_runs/20261015T135734Z_live_options.log`, `logs/action_runs/20261015T135734Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1672 | 48.5 | -25.0 | +37.8 | $+18,703 |
| TAINTED | 2002 | 32.4 | -40.4 | +10.8 | $-10,944 |
| KEEP-only | 805 | 61.4 | +51.0 | +56.8 | $+12,726 |
| KEEP-only recent | 612 | 60.0 | +53.3 | +63.6 | $+8,665 |

- KEEP strategies (23): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S411
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-15T09:57:42.164220-04:00","date":"2026-10-15","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":65.6,"phases_s":{"reconcile":0.49,"cancel":0.16,"manage":2.72,"protective_stops":1.34,"scan":57.97,"entries":2.07},"signals":347,"placed":0,"equity":993013.31,"open_positions":3,"pending_orders":0,"open_lots":5,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":["S164:NVDA","S168:NVDA","S167:NVDA","S163:NVDA","S350:NVDA","S352:NVDA","S356:NVDA","S357:NVDA"],"github_run":"12884","github_run_id":"38746794333","status":"ok","data_quality":{"clean":{"n":1672,"win":48.5,"med":-25.0,"avg":37.83,"pnl":18702.83},"tainted":{"n":2002,"win":32.37,"med":-40.35,"avg":10.83,"pnl":-10944.28},"keep_only":{"n":805,"win":61.37,"med":50.98,"avg":56.78,"pnl":12726.45},"keep_only_recent":{"n":612,"win":59.97,"med":53.28,"avg":63.55,"pnl":8665.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:57:35  INFO      Mode: morning_scan
13:57:36  INFO      Morning scan already completed today (2026-10-15T13:51:30.010528Z) — exits-only pass
13:57:36  INFO        Daily log -> logs/daily/2026-10-15.md
13:57:36  INFO        Daily log reconciled -> logs/daily/2026-10-15.md (1 ledger rows)
13:57:36  INFO        place_all_stops: checking 2 positions...
13:57:36  INFO        STOP already live KEY @ $19.59
13:57:36  INFO        STOP skipped PNC: fractional (0.1587 shares) — software exit will handle it
13:57:37  INFO        [positions] 2/2 (2 valid)
13:57:37  INFO        Daily log -> logs/daily/2026-10-15.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_SCAN|
|  Time                                                         13:57 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.14|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  KEY  P&L +0.8%  $+0.28                                            HOLD|
|  PNC  P&L +1.6%  $+0.52                                            HOLD|
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
=== options_live_micro LIVE 2026-10-15T09:57:38.213650-04:00 share=25% ===
2026-10-15 09:57:38,213 INFO === options_live_micro LIVE 2026-10-15T09:57:38.213650-04:00 share=25% ===
Live account equity $224.14 cash $156.16 #225458845 options_level=3
2026-10-15 09:57:38,463 INFO Live account equity $224.14 cash $156.16 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-10-15 09:57:38,690 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-10-15 09:57:38,846 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (204 earlier lines - see full log file)
| S167 | 327 | 28 |
| S168 | 247 | 25 |
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
| 2026-10-02 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-07 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-08 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-09 |    2 |    1 |    0 |    0 |    1 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-10-13 |    2 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-10-14 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-15
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |  1914 | WARN | <<<
| Missing exit records (post) |  1913 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     5 | INFO |
| Total closed lots           |  2785 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-15_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-15_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1672 med=-25.0% | TAINTED n=2002 med=-40.4% | KEEP-only n=805 med=+51.0% | KILL=21 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.14 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---
