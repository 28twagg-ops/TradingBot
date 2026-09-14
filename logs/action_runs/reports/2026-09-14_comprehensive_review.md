# Daily Comprehensive Action Review - 2026-09-14

_Auto-generated from GitHub Actions run output. Each run appends a summary; full stdout is in linked per-run log files._
## Run 20260914T130114Z

- UTC timestamp: `20260914T130114Z`
- GitHub run: [#9844](https://github.com/28twagg-ops/TradingBot/actions/runs/34846557144)
- Run id: `34846557144`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`24s`
- Full logs: `logs/action_runs/20260914T130114Z_live_bot.log`, `logs/action_runs/20260914T130114Z_live_options.log`, `logs/action_runs/20260914T130114Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1204 | 49.2 | -10.1 | +40.8 | $+15,812 |
| TAINTED | 1829 | 33.4 | -38.8 | +12.0 | $-9,097 |
| KEEP-only | 626 | 63.3 | +51.4 | +64.2 | $+10,734 |
| KEEP-only recent | 429 | 61.3 | +53.3 | +74.5 | $+6,089 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-14T09:01:20.773745-04:00","date":"2026-09-14","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":11.6,"phases_s":{"reconcile":4.65},"signals":0,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":41,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9844","github_run_id":"34846557144","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
13:01:15  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.44|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $226.44|
|  Cash                                                           $158.78|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $67.66|
|  Open P&L                                                        $-0.61|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AMZN     Pullback50      $33.85     $256.11  $253.61  -1.0%   $-0.33  |
|  TKR      MomReversal     $33.82     $119.14  $118.18  -0.8%   $-0.27  |
|                                                                        |
|  Total invested                                                  $67.66|
|  Total open P&L                                                  $-0.61|
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
|  2026-09-11  SELL  RL  MomReversal  $33.81  P&L $-0.25                 |
|  2026-09-11  SELL  ADI  Pullback50  $34.06  P&L $-0.10                 |
|  2026-09-11  SELL  ABBV  Pullback50  $34.61  P&L $+0.61                |
|  2026-09-10  SELL  AES  Pullback50  $34.05  P&L $-0.00                 |
|  2026-09-10  SELL  ABBV  Pullback50  $33.90  P&L $-0.20                |
|  2026-09-10  SELL  AES  Pullback50  $34.09  P&L $+0.01                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-14T09:01:17.291782-04:00 share=25% ===
2026-09-14 09:01:17,291 INFO === options_live_micro LIVE 2026-09-14T09:01:17.291782-04:00 share=25% ===
Live account equity $226.44 cash $158.78 #225458845 options_level=3
2026-09-14 09:01:17,488 INFO Live account equity $226.44 cash $158.78 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-14 09:01:17,552 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-14 09:01:17,615 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (161 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-14
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     4 | WARN | <<<
| Orphaned lots (post-stable) |  1235 | WARN | <<<
| Missing exit records (post) |  1231 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    41 | INFO |
| Total closed lots           |  2193 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-14_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-14_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1204 med=-10.1% | TAINTED n=1829 med=-38.8% | KEEP-only n=626 med=+51.4% | KILL=19 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.44 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260914T130608Z

- UTC timestamp: `20260914T130608Z`
- GitHub run: [#9845](https://github.com/28twagg-ops/TradingBot/actions/runs/34847041058)
- Run id: `34847041058`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`24s`
- Full logs: `logs/action_runs/20260914T130608Z_live_bot.log`, `logs/action_runs/20260914T130608Z_live_options.log`, `logs/action_runs/20260914T130608Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1204 | 49.2 | -10.1 | +40.8 | $+15,812 |
| TAINTED | 1829 | 33.4 | -38.8 | +12.0 | $-9,097 |
| KEEP-only | 626 | 63.3 | +51.4 | +64.2 | $+10,734 |
| KEEP-only recent | 429 | 61.3 | +53.3 | +74.5 | $+6,089 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-14T09:06:14.655371-04:00","date":"2026-09-14","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":11.4,"phases_s":{"reconcile":4.48},"signals":0,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":41,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9845","github_run_id":"34847041058","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
13:06:09  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.40|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $226.40|
|  Cash                                                           $158.78|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $67.62|
|  Open P&L                                                        $-0.65|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AMZN     Pullback50      $33.80     $256.11  $253.25  -1.1%   $-0.38  |
|  TKR      MomReversal     $33.82     $119.14  $118.18  -0.8%   $-0.27  |
|                                                                        |
|  Total invested                                                  $67.62|
|  Total open P&L                                                  $-0.65|
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
|  2026-09-11  SELL  RL  MomReversal  $33.81  P&L $-0.25                 |
|  2026-09-11  SELL  ADI  Pullback50  $34.06  P&L $-0.10                 |
|  2026-09-11  SELL  ABBV  Pullback50  $34.61  P&L $+0.61                |
|  2026-09-10  SELL  AES  Pullback50  $34.05  P&L $-0.00                 |
|  2026-09-10  SELL  ABBV  Pullback50  $33.90  P&L $-0.20                |
|  2026-09-10  SELL  AES  Pullback50  $34.09  P&L $+0.01                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-14T09:06:11.128847-04:00 share=25% ===
2026-09-14 09:06:11,128 INFO === options_live_micro LIVE 2026-09-14T09:06:11.128847-04:00 share=25% ===
Live account equity $226.40 cash $158.78 #225458845 options_level=3
2026-09-14 09:06:11,253 INFO Live account equity $226.40 cash $158.78 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-14 09:06:11,360 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-14 09:06:11,392 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (155 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-14
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     4 | WARN | <<<
| Orphaned lots (post-stable) |  1235 | WARN | <<<
| Missing exit records (post) |  1231 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    41 | INFO |
| Total closed lots           |  2193 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-14_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-14_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1204 med=-10.1% | TAINTED n=1829 med=-38.8% | KEEP-only n=626 med=+51.4% | KILL=19 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.4 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260914T131105Z

- UTC timestamp: `20260914T131105Z`
- GitHub run: [#9846](https://github.com/28twagg-ops/TradingBot/actions/runs/34847544795)
- Run id: `34847544795`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`23s`
- Full logs: `logs/action_runs/20260914T131105Z_live_bot.log`, `logs/action_runs/20260914T131105Z_live_options.log`, `logs/action_runs/20260914T131105Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1204 | 49.2 | -10.1 | +40.8 | $+15,812 |
| TAINTED | 1829 | 33.4 | -38.8 | +12.0 | $-9,097 |
| KEEP-only | 626 | 63.3 | +51.4 | +64.2 | $+10,734 |
| KEEP-only recent | 429 | 61.3 | +53.3 | +74.5 | $+6,089 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-14T09:11:10.439498-04:00","date":"2026-09-14","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":10.9,"phases_s":{"reconcile":4.18},"signals":0,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":41,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9846","github_run_id":"34847544795","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
13:11:06  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.38|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $226.38|
|  Cash                                                           $158.78|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $67.60|
|  Open P&L                                                        $-0.67|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AMZN     Pullback50      $33.79     $256.11  $253.15  -1.2%   $-0.39  |
|  TKR      MomReversal     $33.82     $119.14  $118.18  -0.8%   $-0.27  |
|                                                                        |
|  Total invested                                                  $67.60|
|  Total open P&L                                                  $-0.67|
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
|  2026-09-11  SELL  RL  MomReversal  $33.81  P&L $-0.25                 |
|  2026-09-11  SELL  ADI  Pullback50  $34.06  P&L $-0.10                 |
|  2026-09-11  SELL  ABBV  Pullback50  $34.61  P&L $+0.61                |
|  2026-09-10  SELL  AES  Pullback50  $34.05  P&L $-0.00                 |
|  2026-09-10  SELL  ABBV  Pullback50  $33.90  P&L $-0.20                |
|  2026-09-10  SELL  AES  Pullback50  $34.09  P&L $+0.01                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-14T09:11:07.302267-04:00 share=25% ===
2026-09-14 09:11:07,302 INFO === options_live_micro LIVE 2026-09-14T09:11:07.302267-04:00 share=25% ===
Live account equity $226.38 cash $158.78 #225458845 options_level=3
2026-09-14 09:11:07,353 INFO Live account equity $226.38 cash $158.78 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-14 09:11:07,361 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-14 09:11:07,368 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (155 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-14
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     4 | WARN | <<<
| Orphaned lots (post-stable) |  1235 | WARN | <<<
| Missing exit records (post) |  1231 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    41 | INFO |
| Total closed lots           |  2193 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-14_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-14_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1204 med=-10.1% | TAINTED n=1829 med=-38.8% | KEEP-only n=626 med=+51.4% | KILL=19 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.38 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260914T131605Z

- UTC timestamp: `20260914T131605Z`
- GitHub run: [#9847](https://github.com/28twagg-ops/TradingBot/actions/runs/34848076249)
- Run id: `34848076249`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`24s`
- Full logs: `logs/action_runs/20260914T131605Z_live_bot.log`, `logs/action_runs/20260914T131605Z_live_options.log`, `logs/action_runs/20260914T131605Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1204 | 49.2 | -10.1 | +40.8 | $+15,812 |
| TAINTED | 1829 | 33.4 | -38.8 | +12.0 | $-9,097 |
| KEEP-only | 626 | 63.3 | +51.4 | +64.2 | $+10,734 |
| KEEP-only recent | 429 | 61.3 | +53.3 | +74.5 | $+6,089 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-14T09:16:13.546727-04:00","date":"2026-09-14","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":11.9,"phases_s":{"reconcile":4.81},"signals":0,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":41,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9847","github_run_id":"34848076249","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
13:16:08  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.36|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $226.36|
|  Cash                                                           $158.78|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $67.58|
|  Open P&L                                                        $-0.69|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AMZN     Pullback50      $33.77     $256.11  $253.00  -1.2%   $-0.41  |
|  TKR      MomReversal     $33.82     $119.14  $118.18  -0.8%   $-0.27  |
|                                                                        |
|  Total invested                                                  $67.58|
|  Total open P&L                                                  $-0.69|
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
|  2026-09-11  SELL  RL  MomReversal  $33.81  P&L $-0.25                 |
|  2026-09-11  SELL  ADI  Pullback50  $34.06  P&L $-0.10                 |
|  2026-09-11  SELL  ABBV  Pullback50  $34.61  P&L $+0.61                |
|  2026-09-10  SELL  AES  Pullback50  $34.05  P&L $-0.00                 |
|  2026-09-10  SELL  ABBV  Pullback50  $33.90  P&L $-0.20                |
|  2026-09-10  SELL  AES  Pullback50  $34.09  P&L $+0.01                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-14T09:16:10.100563-04:00 share=25% ===
2026-09-14 09:16:10,100 INFO === options_live_micro LIVE 2026-09-14T09:16:10.100563-04:00 share=25% ===
Live account equity $226.36 cash $158.78 #225458845 options_level=3
2026-09-14 09:16:10,326 INFO Live account equity $226.36 cash $158.78 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-14 09:16:10,396 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-14 09:16:10,466 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (155 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-14
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     4 | WARN | <<<
| Orphaned lots (post-stable) |  1235 | WARN | <<<
| Missing exit records (post) |  1231 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    41 | INFO |
| Total closed lots           |  2193 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-14_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-14_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1204 med=-10.1% | TAINTED n=1829 med=-38.8% | KEEP-only n=626 med=+51.4% | KILL=19 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.36 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260914T132109Z

- UTC timestamp: `20260914T132109Z`
- GitHub run: [#9848](https://github.com/28twagg-ops/TradingBot/actions/runs/34848591706)
- Run id: `34848591706`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`23s`
- Full logs: `logs/action_runs/20260914T132109Z_live_bot.log`, `logs/action_runs/20260914T132109Z_live_options.log`, `logs/action_runs/20260914T132109Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1204 | 49.2 | -10.1 | +40.8 | $+15,812 |
| TAINTED | 1829 | 33.4 | -38.8 | +12.0 | $-9,097 |
| KEEP-only | 626 | 63.3 | +51.4 | +64.2 | $+10,734 |
| KEEP-only recent | 429 | 61.3 | +53.3 | +74.5 | $+6,089 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-14T09:21:15.192890-04:00","date":"2026-09-14","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":10.9,"phases_s":{"reconcile":4.17},"signals":0,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":41,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9848","github_run_id":"34848591706","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
13:21:10  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.37|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $226.37|
|  Cash                                                           $158.78|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $67.59|
|  Open P&L                                                        $-0.68|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AMZN     Pullback50      $33.77     $256.11  $253.04  -1.2%   $-0.41  |
|  TKR      MomReversal     $33.82     $119.14  $118.18  -0.8%   $-0.27  |
|                                                                        |
|  Total invested                                                  $67.59|
|  Total open P&L                                                  $-0.68|
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
|  2026-09-11  SELL  RL  MomReversal  $33.81  P&L $-0.25                 |
|  2026-09-11  SELL  ADI  Pullback50  $34.06  P&L $-0.10                 |
|  2026-09-11  SELL  ABBV  Pullback50  $34.61  P&L $+0.61                |
|  2026-09-10  SELL  AES  Pullback50  $34.05  P&L $-0.00                 |
|  2026-09-10  SELL  ABBV  Pullback50  $33.90  P&L $-0.20                |
|  2026-09-10  SELL  AES  Pullback50  $34.09  P&L $+0.01                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-14T09:21:12.132464-04:00 share=25% ===
2026-09-14 09:21:12,132 INFO === options_live_micro LIVE 2026-09-14T09:21:12.132464-04:00 share=25% ===
Live account equity $226.37 cash $158.78 #225458845 options_level=3
2026-09-14 09:21:12,190 INFO Live account equity $226.37 cash $158.78 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-14 09:21:12,216 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-14 09:21:12,228 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (155 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-14
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     4 | WARN | <<<
| Orphaned lots (post-stable) |  1235 | WARN | <<<
| Missing exit records (post) |  1231 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    41 | INFO |
| Total closed lots           |  2193 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-14_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-14_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1204 med=-10.1% | TAINTED n=1829 med=-38.8% | KEEP-only n=626 med=+51.4% | KILL=19 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.37 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260914T132614Z

- UTC timestamp: `20260914T132614Z`
- GitHub run: [#9849](https://github.com/28twagg-ops/TradingBot/actions/runs/34849104508)
- Run id: `34849104508`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`24s`
- Full logs: `logs/action_runs/20260914T132614Z_live_bot.log`, `logs/action_runs/20260914T132614Z_live_options.log`, `logs/action_runs/20260914T132614Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1204 | 49.2 | -10.1 | +40.8 | $+15,812 |
| TAINTED | 1829 | 33.4 | -38.8 | +12.0 | $-9,097 |
| KEEP-only | 626 | 63.3 | +51.4 | +64.2 | $+10,734 |
| KEEP-only recent | 429 | 61.3 | +53.3 | +74.5 | $+6,089 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-14T09:26:21.164064-04:00","date":"2026-09-14","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":11.8,"phases_s":{"reconcile":4.75},"signals":0,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":41,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9849","github_run_id":"34849104508","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
13:26:15  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.40|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $226.40|
|  Cash                                                           $158.78|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $67.62|
|  Open P&L                                                        $-0.65|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (2 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AMZN     Pullback50      $33.80     $256.11  $253.25  -1.1%   $-0.38  |
|  TKR      MomReversal     $33.82     $119.14  $118.18  -0.8%   $-0.27  |
|                                                                        |
|  Total invested                                                  $67.62|
|  Total open P&L                                                  $-0.65|
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
|  2026-09-11  SELL  RL  MomReversal  $33.81  P&L $-0.25                 |
|  2026-09-11  SELL  ADI  Pullback50  $34.06  P&L $-0.10                 |
|  2026-09-11  SELL  ABBV  Pullback50  $34.61  P&L $+0.61                |
|  2026-09-10  SELL  AES  Pullback50  $34.05  P&L $-0.00                 |
|  2026-09-10  SELL  ABBV  Pullback50  $33.90  P&L $-0.20                |
|  2026-09-10  SELL  AES  Pullback50  $34.09  P&L $+0.01                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-14T09:26:17.718407-04:00 share=25% ===
2026-09-14 09:26:17,718 INFO === options_live_micro LIVE 2026-09-14T09:26:17.718407-04:00 share=25% ===
Live account equity $226.40 cash $158.78 #225458845 options_level=3
2026-09-14 09:26:17,942 INFO Live account equity $226.40 cash $158.78 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-09-14 09:26:18,014 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-09-14 09:26:18,081 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (155 earlier lines - see full log file)
| w4     |    6 |    4 |   10 |    3 |    5 |    7 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    44 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 259 | 14 |
| S164 | 281 | 18 |
| S165 | 1717 | 30 |
| S166 | 135 | 9 |
| S167 | 275 | 17 |
| S168 | 206 | 14 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-09-14
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     4 | WARN | <<<
| Orphaned lots (post-stable) |  1235 | WARN | <<<
| Missing exit records (post) |  1231 | WARN | <<<
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    41 | INFO |
| Total closed lots           |  2193 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-14_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-09-14_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1204 med=-10.1% | TAINTED n=1829 med=-38.8% | KEEP-only n=626 med=+51.4% | KILL=19 KEEP=23
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=226.4 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260914T133107Z

- UTC timestamp: `20260914T133107Z`
- GitHub run: [#9850](https://github.com/28twagg-ops/TradingBot/actions/runs/34849617457)
- Run id: `34849617457`
- Live bot: exit=`0`, duration=`216s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260914T133107Z_live_bot.log`, `logs/action_runs/20260914T133107Z_live_options.log`, `logs/action_runs/20260914T133107Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1204 | 49.2 | -10.1 | +40.8 | $+15,812 |
| TAINTED | 1829 | 33.4 | -38.8 | +12.0 | $-9,097 |
| KEEP-only | 626 | 63.3 | +51.4 | +64.2 | $+10,734 |
| KEEP-only recent | 429 | 61.3 | +53.3 | +74.5 | $+6,089 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-14T09:26:21.164064-04:00","date":"2026-09-14","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":11.8,"phases_s":{"reconcile":4.75},"signals":0,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":41,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9849","github_run_id":"34849104508","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
13:31:09  INFO      Mode: morning_prep
13:31:09  INFO        [prep_positions] 2/2 (2 valid)
13:31:09  INFO      Fetching tickers (universe=both)...
13:31:09  INFO        S&P 500: 503
13:31:09  INFO        MidCap 400: 400
13:31:09  INFO        Total: 903 tickers
13:31:10  INFO        [prep_universe] 40/901 (40 valid)
13:31:12  INFO        [prep_universe] 80/901 (80 valid)
13:31:13  INFO        [prep_universe] 120/901 (120 valid)
13:31:14  INFO        [prep_universe] 160/901 (160 valid)
13:31:15  INFO        [prep_universe] 200/901 (199 valid)
13:31:23  INFO        [prep_universe] 240/901 (238 valid)
13:31:36  INFO        [prep_universe] 280/901 (278 valid)
13:31:48  INFO        [prep_universe] 320/901 (318 valid)
13:31:58  INFO        [prep_universe] 360/901 (358 valid)
13:32:11  INFO        [prep_universe] 400/901 (398 valid)
13:32:24  INFO        [prep_universe] 440/901 (438 valid)
13:32:34  INFO        [prep_universe] 480/901 (478 valid)
13:32:47  INFO        [prep_universe] 520/901 (518 valid)
13:33:00  INFO        [prep_universe] 560/901 (558 valid)
13:33:13  INFO        [prep_universe] 600/901 (598 valid)
13:33:23  INFO        [prep_universe] 640/901 (638 valid)
13:33:36  INFO        [prep_universe] 680/901 (678 valid)
13:33:49  INFO        [prep_universe] 720/901 (718 valid)
13:33:59  INFO        [prep_universe] 760/901 (758 valid)
13:34:11  INFO        [prep_universe] 800/901 (798 valid)
13:34:24  INFO        [prep_universe] 840/901 (838 valid)
13:34:34  INFO        [prep_universe] 880/901 (878 valid)
13:34:41  INFO        [prep_universe] 901/901 (899 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.53|
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
|  Invested                                                        $66.76|
|  Open P&L                                                        $-1.51|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AMZN     Pullback50      $33.54     $256.11  $251.33  -1.9%   $-0.64  |
|  TKR      MomReversal     $33.21     $119.14  $116.08  -2.6%   $-0.88  |
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
|  Signal candidates                                                   39|
|  Universe scanned                                                   901|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-14T09:34:44.515468-04:00 share=25% ===
2026-09-14 09:34:44,515 INFO === options_live_micro LIVE 2026-09-14T09:34:44.515468-04:00 share=25% ===
Live account equity $225.62 cash $158.78 #225458845 options_level=3
2026-09-14 09:34:44,736 INFO Live account equity $225.62 cash $158.78 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-14 09:34:44,781 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-14 09:34:44,798 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=41 paper_keys=yes dry_run=False
  alpaca positions=9
  FLAG b193|S218|235f18c1 missing from Alpaca
  FLAG b192|S218|0277ef32 missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE FAIL: {"code":50010000,"message":"internal server error occurred"}
paper probe failed (non-fatal)
=== options_morning_bot (PAPER) 2026-09-14T09:34:47.447630-04:00 ===

[Run context]
2026-09-14 09:34:47,509 WARNING paper get_account failed attempt 1/3 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 2s
2026-09-14 09:34:49,584 WARNING paper get_account failed attempt 2/3 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 4s
2026-09-14 09:34:53,601 ERROR paper get_account failed after 3 attempts: {"code":50010000,"message":"internal server error occurred"}
WARN: get_account failed ({"code":50010000,"message":"internal server error occurred"}) but positions OK (n=9). Keys are fine; Alpaca account endpoint is flaky. Using cached equity $1000241.84.
2026-09-14 09:34:53,630 WARNING paper get_account failed attempt 1/2 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 2s
2026-09-14 09:34:55,654 ERROR paper get_account failed after 2 attempts: {"code":50010000,"message":"internal server error occurred"}
WARN: using cached paper equity $1000241.84 (get_account: {"code":50010000,"message":"internal server error occurred"})
2026-09-14 09:34:55,721 WARNING lab get_account failed attempt 1/2: {"code":50010000,"message":"internal server error occurred"}
2026-09-14 09:34:57,747 ERROR lab get_account failed after 2 attempts: {"code":50010000,"message":"internal server error occurred"}

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
  EXIT [b330|lab0330_s357_w2_1005_1045_r1|S357] stop_loss (-100.0%) SELL failed PATH260925C00017000: {"code":50010000,"message":"internal server error occurred"}
  EXIT [b802|lab0802_s404_w2_1005_1045_r1|S404] stop_loss (-100.0%) SELL failed AMD260914C00550000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b779|lab0779_s397_w2_1005_1045_r2|S397] stop_loss (-100.0%) SELL failed AMD260914C00550000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
Protective stops: placed=0 upgraded=0 already=1 failed=4 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
```

---

## Run 20260914T133640Z

- UTC timestamp: `20260914T133640Z`
- GitHub run: [#9851](https://github.com/28twagg-ops/TradingBot/actions/runs/34850134176)
- Run id: `34850134176`
- Live bot: exit=`0`, duration=`217s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260914T133640Z_live_bot.log`, `logs/action_runs/20260914T133640Z_live_options.log`, `logs/action_runs/20260914T133640Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1204 | 49.2 | -10.1 | +40.8 | $+15,812 |
| TAINTED | 1829 | 33.4 | -38.8 | +12.0 | $-9,097 |
| KEEP-only | 626 | 63.3 | +51.4 | +64.2 | $+10,734 |
| KEEP-only recent | 429 | 61.3 | +53.3 | +74.5 | $+6,089 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-14T09:26:21.164064-04:00","date":"2026-09-14","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":11.8,"phases_s":{"reconcile":4.75},"signals":0,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":41,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9849","github_run_id":"34849104508","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
13:36:41  INFO      Mode: morning_prep
13:36:42  INFO        [prep_positions] 2/2 (2 valid)
13:36:42  INFO      Fetching tickers (universe=both)...
13:36:42  INFO        S&P 500: 503
13:36:43  INFO        MidCap 400: 400
13:36:43  INFO        Total: 903 tickers
13:36:44  INFO        [prep_universe] 40/901 (40 valid)
13:36:46  INFO        [prep_universe] 80/901 (80 valid)
13:36:47  INFO        [prep_universe] 120/901 (120 valid)
13:36:49  INFO        [prep_universe] 160/901 (160 valid)
13:36:50  INFO        [prep_universe] 200/901 (199 valid)
13:36:57  INFO        [prep_universe] 240/901 (238 valid)
13:37:08  INFO        [prep_universe] 280/901 (278 valid)
13:37:21  INFO        [prep_universe] 320/901 (318 valid)
13:37:31  INFO        [prep_universe] 360/901 (358 valid)
13:37:45  INFO        [prep_universe] 400/901 (398 valid)
13:37:55  INFO        [prep_universe] 440/901 (438 valid)
13:38:09  INFO        [prep_universe] 480/901 (478 valid)
13:38:22  INFO        [prep_universe] 520/901 (518 valid)
13:38:32  INFO        [prep_universe] 560/901 (558 valid)
13:38:46  INFO        [prep_universe] 600/901 (598 valid)
13:38:56  INFO        [prep_universe] 640/901 (638 valid)
13:39:09  INFO        [prep_universe] 680/901 (678 valid)
13:39:20  INFO        [prep_universe] 720/901 (718 valid)
13:39:33  INFO        [prep_universe] 760/901 (758 valid)
13:39:43  INFO        [prep_universe] 800/901 (798 valid)
13:39:57  INFO        [prep_universe] 840/901 (838 valid)
13:40:07  INFO        [prep_universe] 880/901 (878 valid)
13:40:14  INFO        [prep_universe] 901/901 (899 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.03|
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
|  Invested                                                        $67.25|
|  Open P&L                                                        $-1.02|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AMZN     Pullback50      $33.86     $256.11  $253.69  -0.9%   $-0.32  |
|  TKR      MomReversal     $33.39     $119.14  $116.69  -2.1%   $-0.70  |
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
|  Signal candidates                                                   48|
|  Universe scanned                                                   901|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-14T09:40:17.874932-04:00 share=25% ===
2026-09-14 09:40:17,875 INFO === options_live_micro LIVE 2026-09-14T09:40:17.874932-04:00 share=25% ===
Live account equity $226.12 cash $158.78 #225458845 options_level=3
2026-09-14 09:40:18,099 INFO Live account equity $226.12 cash $158.78 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-14 09:40:18,309 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-14 09:40:18,449 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=41 paper_keys=yes dry_run=False
  alpaca positions=9
  FLAG b193|S218|235f18c1 missing from Alpaca
  FLAG b192|S218|0277ef32 missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1164:live_1to1+variations (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1164:live_1to1+variations)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1164
PROBE FAIL: {"code":50010000,"message":"internal server error occurred"}
paper probe failed (non-fatal)
=== options_morning_bot (PAPER) 2026-09-14T09:40:21.619846-04:00 ===

[Run context]
2026-09-14 09:40:21,851 WARNING paper get_account failed attempt 1/3 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 2s
2026-09-14 09:40:23,939 WARNING paper get_account failed attempt 2/3 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 4s
2026-09-14 09:40:28,011 ERROR paper get_account failed after 3 attempts: {"code":50010000,"message":"internal server error occurred"}
WARN: get_account failed ({"code":50010000,"message":"internal server error occurred"}) but positions OK (n=9). Keys are fine; Alpaca account endpoint is flaky. Using cached equity $1000241.84.
2026-09-14 09:40:28,238 WARNING paper get_account failed attempt 1/2 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 2s
2026-09-14 09:40:30,315 ERROR paper get_account failed after 2 attempts: {"code":50010000,"message":"internal server error occurred"}
WARN: using cached paper equity $1000241.84 (get_account: {"code":50010000,"message":"internal server error occurred"})
2026-09-14 09:40:30,457 WARNING lab get_account failed attempt 1/2: {"code":50010000,"message":"internal server error occurred"}
2026-09-14 09:40:32,537 ERROR lab get_account failed after 2 attempts: {"code":50010000,"message":"internal server error occurred"}

[Setup]
LIVE 1:1 bucket b90 live_1to1 — S218, S404, S406 | TP+50%/SL-40% | stop-mkt | min $20
Variation study: 1163 lab/promising bucket(s) | cohort: all paper strategies | max 400 new entries/run
Dropped (no new entries; ex-reflected P&L): S203, S207, S212, S360, S405, S407
  EXIT [b330|lab0330_s357_w2_1005_1045_r1|S357] stop_loss (-100.0%) SELL failed PATH260925C00017000: {"code":50010000,"message":"internal server error occurred"}
  EXIT [b802|lab0802_s404_w2_1005_1045_r1|S404] stop_loss (-100.0%) SELL failed AMD260914C00550000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b779|lab0779_s397_w2_1005_1045_r2|S397] stop_loss (-100.0%) SELL failed AMD260914C00550000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
Protective stops: placed=0 upgraded=0 already=1 failed=4 (market-first)

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S204, S205, S206, S208, S209, S210, S211, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S406, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 113/117 symbols
```

---

## Run 20260914T134222Z

- UTC timestamp: `20260914T134222Z`
- GitHub run: [#9852](https://github.com/28twagg-ops/TradingBot/actions/runs/34850647259)
- Run id: `34850647259`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260914T134222Z_live_bot.log`, `logs/action_runs/20260914T134222Z_live_options.log`, `logs/action_runs/20260914T134222Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1204 | 49.2 | -10.1 | +40.8 | $+15,812 |
| TAINTED | 1829 | 33.4 | -38.8 | +12.0 | $-9,097 |
| KEEP-only | 626 | 63.3 | +51.4 | +64.2 | $+10,734 |
| KEEP-only recent | 429 | 61.3 | +53.3 | +74.5 | $+6,089 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-14T09:26:21.164064-04:00","date":"2026-09-14","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":11.8,"phases_s":{"reconcile":4.75},"signals":0,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":41,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9849","github_run_id":"34849104508","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
13:42:23  INFO      Mode: morning_prep
13:42:25  INFO        [prep_positions] 2/2 (2 valid)
13:42:25  INFO        Universe cache hit: 903 tickers (tickers_2026-09-14.json)
13:42:26  INFO        [prep_universe] 40/901 (40 valid)
13:42:28  INFO        [prep_universe] 80/901 (80 valid)
13:42:29  INFO        [prep_universe] 120/901 (120 valid)
13:42:30  INFO        [prep_universe] 160/901 (160 valid)
13:42:31  INFO        [prep_universe] 200/901 (199 valid)
13:42:39  INFO        [prep_universe] 240/901 (238 valid)
13:42:52  INFO        [prep_universe] 280/901 (278 valid)
13:43:02  INFO        [prep_universe] 320/901 (318 valid)
13:43:16  INFO        [prep_universe] 360/901 (358 valid)
13:43:26  INFO        [prep_universe] 400/901 (398 valid)
13:43:39  INFO        [prep_universe] 440/901 (438 valid)
13:43:50  INFO        [prep_universe] 480/901 (478 valid)
13:44:03  INFO        [prep_universe] 520/901 (518 valid)
13:44:16  INFO        [prep_universe] 560/901 (558 valid)
13:44:27  INFO        [prep_universe] 600/901 (598 valid)
13:44:40  INFO        [prep_universe] 640/901 (638 valid)
13:44:50  INFO        [prep_universe] 680/901 (678 valid)
13:45:04  INFO        [prep_universe] 720/901 (718 valid)
13:45:14  INFO        [prep_universe] 760/901 (758 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20260914T135222Z

- UTC timestamp: `20260914T135222Z`
- GitHub run: [#9854](https://github.com/28twagg-ops/TradingBot/actions/runs/34851699467)
- Run id: `34851699467`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260914T135222Z_live_bot.log`, `logs/action_runs/20260914T135222Z_live_options.log`, `logs/action_runs/20260914T135222Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1204 | 49.2 | -10.1 | +40.8 | $+15,812 |
| TAINTED | 1829 | 33.4 | -38.8 | +12.0 | $-9,097 |
| KEEP-only | 626 | 63.3 | +51.4 | +64.2 | $+10,734 |
| KEEP-only recent | 429 | 61.3 | +53.3 | +74.5 | $+6,089 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-14T09:26:21.164064-04:00","date":"2026-09-14","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":11.8,"phases_s":{"reconcile":4.75},"signals":0,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":41,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9849","github_run_id":"34849104508","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
... (116 earlier lines - see full log file)
|  Source                                                       live scan|
+========================================================================+

+========================================================================+
|                         SIGNALS FOUND  --  43                          |
+========================================================================+
|  TICKER   STRATEGY        TIER   PRICE    RSI    VOL_Z   TRIGGER       |
+------------------------------------------------------------------------+
|  GOOGL    Pullback50      eq     $345.53  47.9   -2.81   50MA bounce (-|
|  GOOG     Pullback50      eq     $341.95  47.6   -3.02   50MA bounce (-|
|  AMZN     Pullback50      eq     $253.91  41.2   -2.68   50MA bounce (-|
|  AES      Pullback50      eq     $14.81   62.3   -2.40   50MA bounce (+|
|  TECH     Pullback50      eq     $72.28   45.9   -2.34   50MA bounce (+|
|  XYZ      Pullback50      eq     $79.90   46.5   -2.28   50MA bounce (-|
|  BF-B     Pullback50      eq     $26.90   37.8   -2.49   50MA bounce (-|
|  CB       Pullback50      eq     $343.62  47.3   -2.74   50MA bounce (-|
|  EBAY     Pullback50      eq     $108.63  53.2   -2.03   50MA bounce (-|
|  BEN      Pullback50      eq     $33.47   39.4   -2.28   50MA bounce (-|
|  FCX      Pullback50      eq     $68.11   30.6   -2.11   50MA bounce (+|
|  HIG      Pullback50      eq     $138.65  49.1   -2.25   50MA bounce (-|
|  PANW     Pullback50      eq     $351.10  50.1   -1.76   50MA bounce (+|
|  PAYX     Pullback50      eq     $117.95  31.3   -2.68   50MA bounce (+|
|  PRU      Pullback50      eq     $119.97  43.3   -2.82   50MA bounce (-|
|  SYF      Pullback50      eq     $76.20   36.1   -2.95   50MA bounce (-|
|  USB      Pullback50      eq     $63.03   54.5   -3.46   50MA bounce (-|
|  VLTO     Pullback50      eq     $96.58   37.4   -2.44   50MA bounce (+|
|  VTRS     Pullback50      eq     $16.65   52.1   -2.46   50MA bounce (-|
|  WRB      Pullback50      eq     $71.25   60.4   -1.89   50MA bounce (+|
|  ZBH      Pullback50      eq     $96.20   37.0   -2.40   50MA bounce (+|
|  AN       Pullback50      eq     $206.62  69.6   -2.15   50MA bounce (+|
|  BJ       Pullback50      eq     $93.41   37.5   -1.68   50MA bounce (+|
|  CBSH     Pullback50      eq     $58.78   51.7   -3.03   50MA bounce (-|
|  CFR      Pullback50      eq     $164.60  50.6   -3.22   50MA bounce (+|
|  FAF      Pullback50      eq     $72.67   51.6   -2.35   50MA bounce (-|13:56:29  INFO        place_all_stops: checking 2 positions...
13:56:29  INFO        STOP skipped ALL: fractional (0.1317 shares) — software exit will handle it
13:56:29  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
13:56:29  INFO        Daily log -> logs/daily/2026-09-14.md
13:56:29  INFO        Dashboard written → logs/dashboard.md

|  FLR      Pullback50      eq     $52.42   53.7   -2.55   50MA bounce (+|
|  GEF      Pullback50      eq     $82.92   37.1   -2.25   50MA bounce (+|
|  HRB      Pullback50      eq     $46.55   17.0   -2.23   50MA bounce (+|
|  HWC      Pullback50      eq     $75.72   55.2   -2.90   50MA bounce (-|
|  HOMB     Pullback50      eq     $30.20   52.4   -3.11   50MA bounce (-|
|  LEA      Pullback50      eq     $130.24  64.3   -2.56   50MA bounce (-|
|  LIVN     Pullback50      eq     $79.52   55.2   -2.85   50MA bounce (-|
|  MOH      Pullback50      eq     $209.66  64.2   -2.18   50MA bounce (+|
|  ORI      Pullback50      eq     $41.82   48.5   -2.83   50MA bounce (-|
|  PATH     Pullback50      eq     $14.29   37.3   -3.01   50MA bounce (+|
|  SBRA     Pullback50      eq     $20.68   54.0   -1.52   50MA bounce (-|
|  SHC      Pullback50      eq     $18.57   38.7   -1.41   50MA bounce (+|
|  SIRI     Pullback50      eq     $29.62   59.9   -2.38   50MA bounce (-|
|  SLAB     Pullback50      eq     $219.50  60.1   -2.02   50MA bounce (+|
|  TCBI     Pullback50      eq     $99.41   56.7   -3.19   50MA bounce (-|
|  UBSI     Pullback50      eq     $47.65   48.5   -3.30   50MA bounce (-|
|  ZION     Pullback50      eq     $69.72   60.4   -2.53   50MA bounce (+|
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
|  Scanned                                                            899|
|  Signals                                                             43|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  0 unconfirmed|
|  Exits                                                                1|
|  Open pos                                                             2|
|  Equity                                                         $226.30|
|  Cash                                                           $158.29|
+========================================================================+
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20260914T135751Z

- UTC timestamp: `20260914T135751Z`
- GitHub run: [#9855](https://github.com/28twagg-ops/TradingBot/actions/runs/34852225484)
- Run id: `34852225484`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260914T135751Z_live_bot.log`, `logs/action_runs/20260914T135751Z_live_options.log`, `logs/action_runs/20260914T135751Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1204 | 49.2 | -10.1 | +40.8 | $+15,812 |
| TAINTED | 1829 | 33.4 | -38.8 | +12.0 | $-9,097 |
| KEEP-only | 626 | 63.3 | +51.4 | +64.2 | $+10,734 |
| KEEP-only recent | 429 | 61.3 | +53.3 | +74.5 | $+6,089 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-14T09:26:21.164064-04:00","date":"2026-09-14","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":11.8,"phases_s":{"reconcile":4.75},"signals":0,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":41,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9849","github_run_id":"34849104508","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
13:57:53  INFO      Mode: morning_scan
13:57:54  INFO        [positions] 2/2 (2 valid)
13:57:54  INFO        Universe cache hit: 903 tickers (tickers_2026-09-14.json)
13:57:55  INFO        [universe] 40/901 (40 valid)
13:57:57  INFO        [universe] 80/901 (80 valid)
13:57:58  INFO        [universe] 120/901 (120 valid)
13:57:59  INFO        [universe] 160/901 (160 valid)
13:58:01  INFO        [universe] 200/901 (199 valid)
13:58:08  INFO        [universe] 240/901 (238 valid)
13:58:21  INFO        [universe] 280/901 (278 valid)
13:58:32  INFO        [universe] 320/901 (318 valid)
13:58:45  INFO        [universe] 360/901 (358 valid)
13:58:55  INFO        [universe] 400/901 (398 valid)
13:59:09  INFO        [universe] 440/901 (438 valid)
13:59:19  INFO        [universe] 480/901 (478 valid)
13:59:32  INFO        [universe] 520/901 (518 valid)
13:59:43  INFO        [universe] 560/901 (558 valid)
13:59:56  INFO        [universe] 600/901 (598 valid)
14:00:10  INFO        [universe] 640/901 (638 valid)
14:00:20  INFO        [universe] 680/901 (678 valid)
14:00:30  INFO        [universe] 720/901 (718 valid)
14:00:44  INFO        [universe] 760/901 (758 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20260914T140215Z

- UTC timestamp: `20260914T140215Z`
- GitHub run: [#9856](https://github.com/28twagg-ops/TradingBot/actions/runs/34852741555)
- Run id: `34852741555`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260914T140215Z_live_bot.log`, `logs/action_runs/20260914T140215Z_live_options.log`, `logs/action_runs/20260914T140215Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1204 | 49.2 | -10.1 | +40.8 | $+15,812 |
| TAINTED | 1829 | 33.4 | -38.8 | +12.0 | $-9,097 |
| KEEP-only | 626 | 63.3 | +51.4 | +64.2 | $+10,734 |
| KEEP-only recent | 429 | 61.3 | +53.3 | +74.5 | $+6,089 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-14T09:26:21.164064-04:00","date":"2026-09-14","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":11.8,"phases_s":{"reconcile":4.75},"signals":0,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":41,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9849","github_run_id":"34849104508","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
14:02:16  INFO      Mode: exits
14:02:17  INFO        Daily log -> logs/daily/2026-09-14.md
14:02:17  INFO        Daily log reconciled -> logs/daily/2026-09-14.md (1 ledger rows)
14:02:17  INFO        place_all_stops: checking 2 positions...
14:02:17  INFO        STOP skipped ALL: fractional (0.1317 shares) — software exit will handle it
14:02:17  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
14:02:18  INFO        [positions] 2/2 (2 valid)
14:02:18  INFO        Daily log -> logs/daily/2026-09-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:02 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.32|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALL  P&L -0.0%  $-0.01                                            HOLD|
|  ALLE  P&L +0.6%  $+0.20                                           HOLD|
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
=== options_live_micro LIVE 2026-09-14T10:02:19.542004-04:00 share=25% ===
2026-09-14 10:02:19,542 INFO === options_live_micro LIVE 2026-09-14T10:02:19.542004-04:00 share=25% ===
Live account equity $226.32 cash $158.29 #225458845 options_level=3
2026-09-14 10:02:19,851 INFO Live account equity $226.32 cash $158.29 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-14 10:02:20,124 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-14 10:02:20,318 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (153 earlier lines - see full log file)
  [b289 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b296 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b297 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b776 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b777 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b784 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b785 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b792 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b793 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b800 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b801 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1052 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1053 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1150 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1151 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1122 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1123 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1094 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1095 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1108 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1109 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b16 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b17 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b280 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b281 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b288 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b289 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b296 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b297 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b362 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b363 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b376 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b377 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b390 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b391 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b418 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b419 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b776 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b777 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b784 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b785 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b792 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b793 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b800 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b801 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b828 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b829 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b856 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b857 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b898 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b899 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b912 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b913 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b234 UPST] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b235 UPST] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b178 CELH] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b179 CELH] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 QQQ] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b192 QQQ] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b193 QQQ] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b234 QQQ] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b235 QQQ] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 IWM] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b192 IWM] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b193 IWM] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b178 HD] ENTRY failed: {"code":40310000,"existing_order_id":"efbafaec-2349-45fb-b0c3-9c9099e0c949","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b179 HD] ENTRY failed: {"code":40310000,"existing_order_id":"efbafaec-2349-45fb-b0c3-9c9099e0c949","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b234 HD] ENTRY failed: {"code":40310000,"existing_order_id":"efbafaec-2349-45fb-b0c3-9c9099e0c949","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b235 HD] ENTRY failed: {"code":40310000,"existing_order_id":"efbafaec-2349-45fb-b0c3-9c9099e0c949","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b80 BAC] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b81 BAC] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b80 MS] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b81 MS] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b234 MS] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b235 MS] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b234 BA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b235 BA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
```

---

## Run 20260914T140747Z

- UTC timestamp: `20260914T140747Z`
- GitHub run: [#9857](https://github.com/28twagg-ops/TradingBot/actions/runs/34853284683)
- Run id: `34853284683`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260914T140747Z_live_bot.log`, `logs/action_runs/20260914T140747Z_live_options.log`, `logs/action_runs/20260914T140747Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1204 | 49.2 | -10.1 | +40.8 | $+15,812 |
| TAINTED | 1829 | 33.4 | -38.8 | +12.0 | $-9,097 |
| KEEP-only | 626 | 63.3 | +51.4 | +64.2 | $+10,734 |
| KEEP-only recent | 429 | 61.3 | +53.3 | +74.5 | $+6,089 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-14T09:26:21.164064-04:00","date":"2026-09-14","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":11.8,"phases_s":{"reconcile":4.75},"signals":0,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":41,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9849","github_run_id":"34849104508","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
14:07:48  INFO      Mode: exits
14:07:48  INFO        Daily log -> logs/daily/2026-09-14.md
14:07:48  INFO        Daily log reconciled -> logs/daily/2026-09-14.md (1 ledger rows)
14:07:49  INFO        place_all_stops: checking 2 positions...
14:07:49  INFO        STOP skipped ALL: fractional (0.1317 shares) — software exit will handle it
14:07:49  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
14:07:49  INFO        [positions] 2/2 (2 valid)
14:07:49  INFO        Daily log -> logs/daily/2026-09-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:07 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.43|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALL  P&L +0.1%  $+0.02                                            HOLD|
|  ALLE  P&L +0.8%  $+0.28                                           HOLD|
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
=== options_live_micro LIVE 2026-09-14T10:07:51.077636-04:00 share=25% ===
2026-09-14 10:07:51,077 INFO === options_live_micro LIVE 2026-09-14T10:07:51.077636-04:00 share=25% ===
Live account equity $226.43 cash $158.29 #225458845 options_level=3
2026-09-14 10:07:51,333 INFO Live account equity $226.43 cash $158.29 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-14 10:07:51,570 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-14 10:07:51,756 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (125 earlier lines - see full log file)
  [b19 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b282 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b283 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b290 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b291 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b298 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b299 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b306 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b307 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b778 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b786 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b787 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b794 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b795 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b803 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1054 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1055 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1152 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1153 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1124 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1125 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1096 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1097 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1110 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1111 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1138 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1139 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b278 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b279 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b282 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b283 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b290 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b291 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b298 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b299 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b306 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b307 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b778 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b786 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b787 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b794 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b795 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b803 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1054 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1055 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1152 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1153 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1124 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1125 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1096 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1097 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1110 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1111 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1138 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1139 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b18 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b19 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b282 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b283 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b290 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b291 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b298 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b299 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b306 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b307 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b364 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b365 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b378 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b379 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b392 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b393 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b778 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b786 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b787 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b794 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b795 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b803 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
```

---

## Run 20260914T141303Z

- UTC timestamp: `20260914T141303Z`
- GitHub run: [#9858](https://github.com/28twagg-ops/TradingBot/actions/runs/34853831517)
- Run id: `34853831517`
- Live bot: exit=`0`, duration=`5s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260914T141303Z_live_bot.log`, `logs/action_runs/20260914T141303Z_live_options.log`, `logs/action_runs/20260914T141303Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1204 | 49.2 | -10.1 | +40.8 | $+15,812 |
| TAINTED | 1829 | 33.4 | -38.8 | +12.0 | $-9,097 |
| KEEP-only | 626 | 63.3 | +51.4 | +64.2 | $+10,734 |
| KEEP-only recent | 429 | 61.3 | +53.3 | +74.5 | $+6,089 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-14T09:26:21.164064-04:00","date":"2026-09-14","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":11.8,"phases_s":{"reconcile":4.75},"signals":0,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":41,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9849","github_run_id":"34849104508","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
14:13:06  INFO      Mode: exits
14:13:07  INFO        Daily log -> logs/daily/2026-09-14.md
14:13:07  INFO        Daily log reconciled -> logs/daily/2026-09-14.md (1 ledger rows)
14:13:07  INFO        place_all_stops: checking 2 positions...
14:13:07  INFO        STOP skipped ALL: fractional (0.1317 shares) — software exit will handle it
14:13:07  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
14:13:07  INFO        [positions] 2/2 (2 valid)
14:13:07  INFO        Daily log -> logs/daily/2026-09-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:13 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.42|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALL  P&L +0.1%  $+0.03                                            HOLD|
|  ALLE  P&L +0.8%  $+0.26                                           HOLD|
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
=== options_live_micro LIVE 2026-09-14T10:13:08.664855-04:00 share=25% ===
2026-09-14 10:13:08,664 INFO === options_live_micro LIVE 2026-09-14T10:13:08.664855-04:00 share=25% ===
Live account equity $226.42 cash $158.29 #225458845 options_level=3
2026-09-14 10:13:08,806 INFO Live account equity $226.42 cash $158.29 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-14 10:13:08,916 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-14 10:13:09,002 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (118 earlier lines - see full log file)
  [b306 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b307 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b778 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b786 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b787 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b794 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b795 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b803 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1054 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1055 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1152 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1153 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1124 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1125 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1096 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1097 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1110 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1111 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1138 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1139 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b278 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b279 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b282 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b283 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b290 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b291 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b298 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b299 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b306 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b307 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b778 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b786 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b787 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b794 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b795 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b803 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1054 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1055 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1152 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1153 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1124 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1125 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1096 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1097 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1110 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1111 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1138 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1139 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b18 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b19 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b282 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b283 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b290 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b291 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b298 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b299 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b306 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b307 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b364 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b365 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b378 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b379 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b392 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b393 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b778 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b786 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b787 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b794 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b795 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b803 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b830 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b831 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b900 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b901 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b914 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b915 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
```

---

## Run 20260914T141711Z

- UTC timestamp: `20260914T141711Z`
- GitHub run: [#9859](https://github.com/28twagg-ops/TradingBot/actions/runs/34854379071)
- Run id: `34854379071`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260914T141711Z_live_bot.log`, `logs/action_runs/20260914T141711Z_live_options.log`, `logs/action_runs/20260914T141711Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1204 | 49.2 | -10.1 | +40.8 | $+15,812 |
| TAINTED | 1829 | 33.4 | -38.8 | +12.0 | $-9,097 |
| KEEP-only | 626 | 63.3 | +51.4 | +64.2 | $+10,734 |
| KEEP-only recent | 429 | 61.3 | +53.3 | +74.5 | $+6,089 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-14T09:26:21.164064-04:00","date":"2026-09-14","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":11.8,"phases_s":{"reconcile":4.75},"signals":0,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":41,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9849","github_run_id":"34849104508","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
14:17:12  INFO      Mode: exits
14:17:12  INFO        Daily log -> logs/daily/2026-09-14.md
14:17:12  INFO        Daily log reconciled -> logs/daily/2026-09-14.md (1 ledger rows)
14:17:12  INFO        place_all_stops: checking 2 positions...
14:17:12  INFO        STOP skipped ALL: fractional (0.1317 shares) — software exit will handle it
14:17:12  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
14:17:12  INFO        [positions] 2/2 (2 valid)
14:17:12  INFO        Daily log -> logs/daily/2026-09-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:17 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.55|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALL  P&L -0.0%  $-0.01                                            HOLD|
|  ALLE  P&L +1.3%  $+0.43                                           HOLD|
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
=== options_live_micro LIVE 2026-09-14T10:17:13.738614-04:00 share=25% ===
2026-09-14 10:17:13,738 INFO === options_live_micro LIVE 2026-09-14T10:17:13.738614-04:00 share=25% ===
Live account equity $226.55 cash $158.29 #225458845 options_level=3
2026-09-14 10:17:13,781 INFO Live account equity $226.55 cash $158.29 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-14 10:17:13,898 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-14 10:17:13,911 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (134 earlier lines - see full log file)
  [b1097 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1110 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1111 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1138 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1139 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b278 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b279 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b282 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b283 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b298 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b299 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b306 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b307 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b778 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b786 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b787 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b794 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b795 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b803 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1054 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1055 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1152 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1153 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1124 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1125 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1096 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1097 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1110 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1111 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1138 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1139 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b18 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b19 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b282 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b283 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b290 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b291 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b298 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b299 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b306 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b307 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b364 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b365 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b378 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b379 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b392 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b393 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b778 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b786 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b787 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b794 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b795 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b803 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b830 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b831 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b900 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b901 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b914 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b915 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b236 UPST] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b237 UPST] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 QQQ] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b194 QQQ] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b195 QQQ] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b236 QQQ] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b237 QQQ] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 IWM] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b194 IWM] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b195 IWM] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b82 BAC] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b83 BAC] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b82 MS] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b83 MS] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b236 MS] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b237 MS] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b236 BA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b237 BA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
```

---

## Run 20260914T142241Z

- UTC timestamp: `20260914T142241Z`
- GitHub run: [#9860](https://github.com/28twagg-ops/TradingBot/actions/runs/34854925577)
- Run id: `34854925577`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260914T142241Z_live_bot.log`, `logs/action_runs/20260914T142241Z_live_options.log`, `logs/action_runs/20260914T142241Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1204 | 49.2 | -10.1 | +40.8 | $+15,812 |
| TAINTED | 1829 | 33.4 | -38.8 | +12.0 | $-9,097 |
| KEEP-only | 626 | 63.3 | +51.4 | +64.2 | $+10,734 |
| KEEP-only recent | 429 | 61.3 | +53.3 | +74.5 | $+6,089 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-14T09:26:21.164064-04:00","date":"2026-09-14","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":11.8,"phases_s":{"reconcile":4.75},"signals":0,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":41,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9849","github_run_id":"34849104508","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
14:22:42  INFO      Mode: exits
14:22:42  INFO        Daily log -> logs/daily/2026-09-14.md
14:22:42  INFO        Daily log reconciled -> logs/daily/2026-09-14.md (1 ledger rows)
14:22:42  INFO        place_all_stops: checking 2 positions...
14:22:42  INFO        STOP skipped ALL: fractional (0.1317 shares) — software exit will handle it
14:22:42  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
14:22:42  INFO        [positions] 2/2 (2 valid)
14:22:42  INFO        Daily log -> logs/daily/2026-09-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:22 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.57|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALL  P&L -0.1%  $-0.03                                            HOLD|
|  ALLE  P&L +1.4%  $+0.47                                           HOLD|
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
=== options_live_micro LIVE 2026-09-14T10:22:43.608845-04:00 share=25% ===
2026-09-14 10:22:43,608 INFO === options_live_micro LIVE 2026-09-14T10:22:43.608845-04:00 share=25% ===
Live account equity $226.57 cash $158.29 #225458845 options_level=3
2026-09-14 10:22:43,653 INFO Live account equity $226.57 cash $158.29 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-14 10:22:43,681 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-14 10:22:43,696 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (116 earlier lines - see full log file)
  [b306 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b307 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b778 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b786 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b787 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b794 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b795 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b803 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1054 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1055 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1152 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1153 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1124 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1125 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1096 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1097 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1110 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1111 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1138 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1139 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b278 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b279 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b282 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b283 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b290 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b291 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b298 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b299 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b306 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b307 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b778 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b786 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b787 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b794 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b795 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b803 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1054 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1055 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1152 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1153 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1124 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1125 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1096 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1097 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1110 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1111 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1138 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1139 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b18 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b19 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b282 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b283 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b290 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b291 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b298 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b299 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b306 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b307 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b364 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b365 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b378 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b379 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b392 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b393 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b778 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b786 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b787 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b794 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b795 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b803 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b830 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b831 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b900 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b901 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b914 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b915 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
```

---

## Run 20260914T142710Z

- UTC timestamp: `20260914T142710Z`
- GitHub run: [#9861](https://github.com/28twagg-ops/TradingBot/actions/runs/34855462206)
- Run id: `34855462206`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260914T142710Z_live_bot.log`, `logs/action_runs/20260914T142710Z_live_options.log`, `logs/action_runs/20260914T142710Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1204 | 49.2 | -10.1 | +40.8 | $+15,812 |
| TAINTED | 1829 | 33.4 | -38.8 | +12.0 | $-9,097 |
| KEEP-only | 626 | 63.3 | +51.4 | +64.2 | $+10,734 |
| KEEP-only recent | 429 | 61.3 | +53.3 | +74.5 | $+6,089 |

- KEEP strategies (23): S163, S168, S173, S174, S210, S218, S350, S353, S354, S355, S356, S357, S361, S362, S363, S364, S365, S397, S399, S401, S403, S404, S406
- KILL strategies (19): ORPHAN, S164, S202, S203, S207, S211, S212, S216, S217, S351, S352, S360, S366, S398, S405, S407, S408, S411, S412
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-09-14T09:26:21.164064-04:00","date":"2026-09-14","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":11.8,"phases_s":{"reconcile":4.75},"signals":0,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":41,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9849","github_run_id":"34849104508","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
14:27:12  INFO      Mode: exits
14:27:12  INFO        Daily log -> logs/daily/2026-09-14.md
14:27:12  INFO        Daily log reconciled -> logs/daily/2026-09-14.md (1 ledger rows)
14:27:12  INFO        place_all_stops: checking 2 positions...
14:27:12  INFO        STOP skipped ALL: fractional (0.1317 shares) — software exit will handle it
14:27:12  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
14:27:12  INFO        [positions] 2/2 (2 valid)
14:27:12  INFO        Daily log -> logs/daily/2026-09-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:27 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.52|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALL  P&L -0.1%  $-0.03                                            HOLD|
|  ALLE  P&L +1.2%  $+0.42                                           HOLD|
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
=== options_live_micro LIVE 2026-09-14T10:27:13.358862-04:00 share=25% ===
2026-09-14 10:27:13,358 INFO === options_live_micro LIVE 2026-09-14T10:27:13.358862-04:00 share=25% ===
Live account equity $226.52 cash $158.29 #225458845 options_level=3
2026-09-14 10:27:13,495 INFO Live account equity $226.52 cash $158.29 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-14 10:27:13,564 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-14 10:27:13,637 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (157 earlier lines - see full log file)
  [b290 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b291 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b298 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b299 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b306 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b307 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b778 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b786 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b787 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b794 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b795 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b803 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1054 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1055 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1152 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1153 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1124 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1125 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1096 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1097 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1110 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1111 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1138 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1139 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b18 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b19 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b282 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b283 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b290 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b291 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b298 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b299 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b306 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b307 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b364 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b365 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b378 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b379 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b392 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b393 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b778 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b786 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b787 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b794 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b795 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b803 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b830 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b831 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b900 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b901 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b914 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b915 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b236 UPST] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b237 UPST] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b181 CELH] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 QQQ] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b194 QQQ] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b195 QQQ] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b236 QQQ] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b237 QQQ] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 IWM] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b194 IWM] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b195 IWM] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b181 HD] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b236 HD] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b237 HD] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b82 BAC] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b83 BAC] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b378 GS] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b379 GS] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b392 GS] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b393 GS] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 GS] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b914 GS] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b915 GS] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b236 BA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b237 BA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
```

---
