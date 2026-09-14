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

## Run 20260914T143246Z

- UTC timestamp: `20260914T143246Z`
- GitHub run: [#9862](https://github.com/28twagg-ops/TradingBot/actions/runs/34856003727)
- Run id: `34856003727`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260914T143246Z_live_bot.log`, `logs/action_runs/20260914T143246Z_live_options.log`, `logs/action_runs/20260914T143246Z_options_bot.log`


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
14:32:47  INFO      Mode: exits
14:32:47  INFO        Daily log -> logs/daily/2026-09-14.md
14:32:47  INFO        Daily log reconciled -> logs/daily/2026-09-14.md (1 ledger rows)
14:32:47  INFO        place_all_stops: checking 2 positions...
14:32:47  INFO        STOP skipped ALL: fractional (0.1317 shares) — software exit will handle it
14:32:47  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
14:32:48  INFO        [positions] 2/2 (2 valid)
14:32:48  INFO        Daily log -> logs/daily/2026-09-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:32 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.51|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALL  P&L -0.2%  $-0.07                                            HOLD|
|  ALLE  P&L +1.3%  $+0.45                                           HOLD|
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
=== options_live_micro LIVE 2026-09-14T10:32:48.879472-04:00 share=25% ===
2026-09-14 10:32:48,879 INFO === options_live_micro LIVE 2026-09-14T10:32:48.879472-04:00 share=25% ===
Live account equity $226.51 cash $158.29 #225458845 options_level=3
2026-09-14 10:32:48,939 INFO Live account equity $226.51 cash $158.29 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-14 10:32:48,987 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-14 10:32:49,013 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (130 earlier lines - see full log file)
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

## Run 20260914T143649Z

- UTC timestamp: `20260914T143649Z`
- GitHub run: [#9863](https://github.com/28twagg-ops/TradingBot/actions/runs/34856543357)
- Run id: `34856543357`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260914T143649Z_live_bot.log`, `logs/action_runs/20260914T143649Z_live_options.log`, `logs/action_runs/20260914T143649Z_options_bot.log`


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
14:36:50  INFO      Mode: exits
14:36:51  INFO        Daily log -> logs/daily/2026-09-14.md
14:36:51  INFO        Daily log reconciled -> logs/daily/2026-09-14.md (1 ledger rows)
14:36:51  INFO        place_all_stops: checking 2 positions...
14:36:51  INFO        STOP skipped ALL: fractional (0.1317 shares) — software exit will handle it
14:36:51  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
14:36:51  INFO        [positions] 2/2 (2 valid)
14:36:51  INFO        Daily log -> logs/daily/2026-09-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.41|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALL  P&L -0.1%  $-0.04                                            HOLD|
|  ALLE  P&L +0.9%  $+0.31                                           HOLD|
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
=== options_live_micro LIVE 2026-09-14T10:36:52.128910-04:00 share=25% ===
2026-09-14 10:36:52,128 INFO === options_live_micro LIVE 2026-09-14T10:36:52.128910-04:00 share=25% ===
Live account equity $226.41 cash $158.29 #225458845 options_level=3
2026-09-14 10:36:52,175 INFO Live account equity $226.41 cash $158.29 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-14 10:36:52,206 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-14 10:36:52,225 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (158 earlier lines - see full log file)
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
  [b420 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b421 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
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
  [b858 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b859 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
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
  [b82 BAC] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b83 BAC] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b378 GS] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b379 GS] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 GS] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b914 GS] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b915 GS] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b82 MS] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b83 MS] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b236 MS] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b237 MS] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b236 BA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b237 BA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
```

---

## Run 20260914T144230Z

- UTC timestamp: `20260914T144230Z`
- GitHub run: [#9864](https://github.com/28twagg-ops/TradingBot/actions/runs/34857090737)
- Run id: `34857090737`
- Live bot: exit=`0`, duration=`5s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260914T144230Z_live_bot.log`, `logs/action_runs/20260914T144230Z_live_options.log`, `logs/action_runs/20260914T144230Z_options_bot.log`


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
14:42:33  INFO      Mode: exits
14:42:34  INFO        Daily log -> logs/daily/2026-09-14.md
14:42:34  INFO        Daily log reconciled -> logs/daily/2026-09-14.md (1 ledger rows)
14:42:34  INFO        place_all_stops: checking 2 positions...
14:42:34  INFO        STOP skipped ALL: fractional (0.1317 shares) — software exit will handle it
14:42:34  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
14:42:34  INFO        [positions] 2/2 (2 valid)
14:42:35  INFO        Daily log -> logs/daily/2026-09-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:42 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.52|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALL  P&L +0.2%  $+0.08                                            HOLD|
|  ALLE  P&L +0.9%  $+0.31                                           HOLD|
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
=== options_live_micro LIVE 2026-09-14T10:42:35.978589-04:00 share=25% ===
2026-09-14 10:42:35,978 INFO === options_live_micro LIVE 2026-09-14T10:42:35.978589-04:00 share=25% ===
Live account equity $226.52 cash $158.29 #225458845 options_level=3
2026-09-14 10:42:36,214 INFO Live account equity $226.52 cash $158.29 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-14 10:42:36,431 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-14 10:42:36,579 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (121 earlier lines - see full log file)
  [b1111 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1138 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1139 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b18 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
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
  [b420 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b421 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b778 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
```

---

## Run 20260914T144642Z

- UTC timestamp: `20260914T144642Z`
- GitHub run: [#9865](https://github.com/28twagg-ops/TradingBot/actions/runs/34857646462)
- Run id: `34857646462`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260914T144642Z_live_bot.log`, `logs/action_runs/20260914T144642Z_live_options.log`, `logs/action_runs/20260914T144642Z_options_bot.log`


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
14:46:43  INFO      Mode: exits
14:46:44  INFO        Daily log -> logs/daily/2026-09-14.md
14:46:44  INFO        Daily log reconciled -> logs/daily/2026-09-14.md (1 ledger rows)
14:46:44  INFO        place_all_stops: checking 2 positions...
14:46:44  INFO        STOP skipped ALL: fractional (0.1317 shares) — software exit will handle it
14:46:44  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
14:46:44  INFO        [positions] 2/2 (2 valid)
14:46:44  INFO        Daily log -> logs/daily/2026-09-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.40|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALL  P&L +0.0%  $+0.01                                            HOLD|
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
=== options_live_micro LIVE 2026-09-14T10:46:45.575361-04:00 share=25% ===
2026-09-14 10:46:45,575 INFO === options_live_micro LIVE 2026-09-14T10:46:45.575361-04:00 share=25% ===
Live account equity $226.40 cash $158.29 #225458845 options_level=3
2026-09-14 10:46:45,777 INFO Live account equity $226.40 cash $158.29 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-14 10:46:45,973 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-14 10:46:46,107 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (162 earlier lines - see full log file)
  [b292 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b293 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b300 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b301 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b366 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b367 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b380 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b381 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b422 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b423 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b780 MARA] ENTRY failed: {"code":40310000,"existing_order_id":"c103b7e0-eb01-43b5-93c6-18dabb5a34cc","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b781 MARA] ENTRY failed: {"code":40310000,"existing_order_id":"c103b7e0-eb01-43b5-93c6-18dabb5a34cc","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b788 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b789 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b796 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b797 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 MARA] ENTRY failed: {"code":40310000,"existing_order_id":"c103b7e0-eb01-43b5-93c6-18dabb5a34cc","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b804 MARA] ENTRY failed: {"code":40310000,"existing_order_id":"c103b7e0-eb01-43b5-93c6-18dabb5a34cc","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b805 MARA] ENTRY failed: {"code":40310000,"existing_order_id":"c103b7e0-eb01-43b5-93c6-18dabb5a34cc","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b90 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b832 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b833 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b888 MARA] ENTRY failed: {"code":40310000,"existing_order_id":"c103b7e0-eb01-43b5-93c6-18dabb5a34cc","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b889 MARA] ENTRY failed: {"code":40310000,"existing_order_id":"c103b7e0-eb01-43b5-93c6-18dabb5a34cc","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b902 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b903 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b916 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b917 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b796 ARM] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b797 ARM] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b832 ARM] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b833 ARM] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b238 UPST] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b239 UPST] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b182 CELH] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b183 CELH] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 QQQ] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b196 QQQ] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b197 QQQ] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b238 QQQ] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b239 QQQ] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 IWM] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b196 IWM] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b197 IWM] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b182 HD] ENTRY failed: {"code":40310000,"existing_order_id":"efbafaec-2349-45fb-b0c3-9c9099e0c949","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b183 HD] ENTRY failed: {"code":40310000,"existing_order_id":"efbafaec-2349-45fb-b0c3-9c9099e0c949","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b238 HD] ENTRY failed: {"code":40310000,"existing_order_id":"efbafaec-2349-45fb-b0c3-9c9099e0c949","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b239 HD] ENTRY failed: {"code":40310000,"existing_order_id":"efbafaec-2349-45fb-b0c3-9c9099e0c949","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b84 BAC] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b85 BAC] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b84 MS] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b85 MS] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b238 MS] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b239 MS] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b238 BA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b239 BA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b182 MMM] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b183 MMM] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b238 MMM] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b239 MMM] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 UNH] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b196 UNH] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b197 UNH] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  Skipped: 322 no tradeable call
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|[OPTIONS BOT DAILY VITALS (MATRIX EXPERIMENT)]                          |
+========================================================================+
|-- ACCOUNT STATUS (entry+manage) --                                     |
|Equity       : $1,000,241.84                                            |
|Open Risk    : 39 lots (8 broker pos)                                   |
|Today's Run  : 309 signals -> 0 orders submitted                        |
|                                                                        |
|-- SYSTEM HEALTH --                                                     |
|Zombies      : 0 (Ledger is clean)                                      |
|Lab Status   : 39 Active Lots | 0 Pending Orders                        |
|Auto-Matrix  : (Pending EOD report generation)                          |
+========================================================================+
```

---

## Run 20260914T145222Z

- UTC timestamp: `20260914T145222Z`
- GitHub run: [#9866](https://github.com/28twagg-ops/TradingBot/actions/runs/34858187557)
- Run id: `34858187557`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260914T145222Z_live_bot.log`, `logs/action_runs/20260914T145222Z_live_options.log`, `logs/action_runs/20260914T145222Z_options_bot.log`


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
14:52:23  INFO      Mode: exits
14:52:25  INFO        Daily log -> logs/daily/2026-09-14.md
14:52:25  INFO        Daily log reconciled -> logs/daily/2026-09-14.md (1 ledger rows)
14:52:25  INFO        place_all_stops: checking 2 positions...
14:52:25  INFO        STOP skipped ALL: fractional (0.1317 shares) — software exit will handle it
14:52:25  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
14:52:26  INFO        [positions] 2/2 (2 valid)
14:52:26  INFO        Daily log -> logs/daily/2026-09-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:52 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.20|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALL  P&L -0.2%  $-0.07                                            HOLD|
|  ALLE  P&L +0.4%  $+0.14                                           HOLD|
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
=== options_live_micro LIVE 2026-09-14T10:52:27.216895-04:00 share=25% ===
2026-09-14 10:52:27,216 INFO === options_live_micro LIVE 2026-09-14T10:52:27.216895-04:00 share=25% ===
Live account equity $226.21 cash $158.29 #225458845 options_level=3
2026-09-14 10:52:27,477 INFO Live account equity $226.21 cash $158.29 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-14 10:52:27,948 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-14 10:52:28,104 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (119 earlier lines - see full log file)
  [b780 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b781 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b788 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b789 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b796 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b797 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b804 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b805 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1056 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1057 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1154 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1155 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1098 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1099 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1112 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1113 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b284 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b285 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b292 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b293 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b300 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b301 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b780 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b781 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b788 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b789 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b796 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b797 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b804 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b805 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1056 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1057 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1154 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1155 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1098 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1099 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1112 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1113 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b20 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b21 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b284 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b285 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b292 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b293 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b300 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b301 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b366 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b367 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b380 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b381 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b422 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b423 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b780 MARA] ENTRY failed: {"code":40310000,"existing_order_id":"c103b7e0-eb01-43b5-93c6-18dabb5a34cc","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b781 MARA] ENTRY failed: {"code":40310000,"existing_order_id":"c103b7e0-eb01-43b5-93c6-18dabb5a34cc","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b788 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b789 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b796 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b797 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 MARA] ENTRY failed: {"code":40310000,"existing_order_id":"c103b7e0-eb01-43b5-93c6-18dabb5a34cc","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b804 MARA] ENTRY failed: {"code":40310000,"existing_order_id":"c103b7e0-eb01-43b5-93c6-18dabb5a34cc","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b805 MARA] ENTRY failed: {"code":40310000,"existing_order_id":"c103b7e0-eb01-43b5-93c6-18dabb5a34cc","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b90 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b832 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b833 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b860 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b861 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b888 MARA] ENTRY failed: {"code":40310000,"existing_order_id":"c103b7e0-eb01-43b5-93c6-18dabb5a34cc","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b889 MARA] ENTRY failed: {"code":40310000,"existing_order_id":"c103b7e0-eb01-43b5-93c6-18dabb5a34cc","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b902 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b903 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b916 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b917 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b832 ARM] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b833 ARM] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b238 UPST] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b239 UPST] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b182 CELH] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b183 CELH] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
```

---

## Run 20260914T145647Z

- UTC timestamp: `20260914T145647Z`
- GitHub run: [#9867](https://github.com/28twagg-ops/TradingBot/actions/runs/34858723777)
- Run id: `34858723777`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260914T145647Z_live_bot.log`, `logs/action_runs/20260914T145647Z_live_options.log`, `logs/action_runs/20260914T145647Z_options_bot.log`


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
{"ts_et":"2026-09-14T10:46:48.440347-04:00","date":"2026-09-14","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":252.3,"phases_s":{"reconcile":2.48,"cancel":0.12,"manage":8.2,"protective_stops":1.53,"scan":35.52,"entries":195.47},"signals":309,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":39,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":["S165:NVDA","S164:NVDA","S168:NVDA","S167:NVDA","S166:NVDA","S163:NVDA","S350:NVDA","S351:NVDA"],"github_run":"9865","github_run_id":"34857646462","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
14:56:48  INFO      Mode: exits
14:56:48  INFO        Daily log -> logs/daily/2026-09-14.md
14:56:48  INFO        Daily log reconciled -> logs/daily/2026-09-14.md (1 ledger rows)
14:56:49  INFO        place_all_stops: checking 2 positions...
14:56:49  INFO        STOP skipped ALL: fractional (0.1317 shares) — software exit will handle it
14:56:49  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
14:56:49  INFO        [positions] 2/2 (2 valid)
14:56:49  INFO        Daily log -> logs/daily/2026-09-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:56 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.18|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALL  P&L -0.2%  $-0.08                                            HOLD|
|  ALLE  P&L +0.4%  $+0.13                                           HOLD|
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
=== options_live_micro LIVE 2026-09-14T10:56:51.010278-04:00 share=25% ===
2026-09-14 10:56:51,010 INFO === options_live_micro LIVE 2026-09-14T10:56:51.010278-04:00 share=25% ===
Live account equity $226.18 cash $158.29 #225458845 options_level=3
2026-09-14 10:56:51,139 INFO Live account equity $226.18 cash $158.29 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-14 10:56:51,284 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-14 10:56:51,348 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (132 earlier lines - see full log file)
  [b1098 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1099 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1112 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1113 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b284 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b285 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b292 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b293 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b300 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b301 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b780 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b781 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b788 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b789 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b796 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b797 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b804 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b805 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1056 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1057 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1154 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1155 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1098 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1099 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1112 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1113 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b20 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b21 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b284 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b285 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b292 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b293 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b300 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b301 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b366 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b367 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b380 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b381 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b422 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b423 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b780 MARA] ENTRY failed: {"code":40310000,"existing_order_id":"c103b7e0-eb01-43b5-93c6-18dabb5a34cc","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b781 MARA] ENTRY failed: {"code":40310000,"existing_order_id":"c103b7e0-eb01-43b5-93c6-18dabb5a34cc","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b788 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b789 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b796 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b797 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 MARA] ENTRY failed: {"code":40310000,"existing_order_id":"c103b7e0-eb01-43b5-93c6-18dabb5a34cc","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b804 MARA] ENTRY failed: {"code":40310000,"existing_order_id":"c103b7e0-eb01-43b5-93c6-18dabb5a34cc","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b805 MARA] ENTRY failed: {"code":40310000,"existing_order_id":"c103b7e0-eb01-43b5-93c6-18dabb5a34cc","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b90 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b832 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b833 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b888 MARA] ENTRY failed: {"code":40310000,"existing_order_id":"c103b7e0-eb01-43b5-93c6-18dabb5a34cc","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b889 MARA] ENTRY failed: {"code":40310000,"existing_order_id":"c103b7e0-eb01-43b5-93c6-18dabb5a34cc","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b902 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b903 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b916 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b917 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b238 UPST] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b239 UPST] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b182 CELH] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b183 CELH] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 QQQ] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b196 QQQ] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b197 QQQ] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b238 QQQ] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b239 QQQ] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 IWM] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b196 IWM] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b197 IWM] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b84 BAC] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b85 BAC] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b380 GS] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b381 GS] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 GS] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b916 GS] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b917 GS] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b238 BA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b239 BA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
```

---

## Run 20260914T150239Z

- UTC timestamp: `20260914T150239Z`
- GitHub run: [#9868](https://github.com/28twagg-ops/TradingBot/actions/runs/34859265894)
- Run id: `34859265894`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260914T150239Z_live_bot.log`, `logs/action_runs/20260914T150239Z_live_options.log`, `logs/action_runs/20260914T150239Z_options_bot.log`


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
15:02:41  INFO      Mode: exits
15:02:41  INFO        Daily log -> logs/daily/2026-09-14.md
15:02:41  INFO        Daily log reconciled -> logs/daily/2026-09-14.md (1 ledger rows)
15:02:41  INFO        place_all_stops: checking 2 positions...
15:02:41  INFO        STOP skipped ALL: fractional (0.1317 shares) — software exit will handle it
15:02:41  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
15:02:41  INFO        [positions] 2/2 (2 valid)
15:02:41  INFO        Daily log -> logs/daily/2026-09-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:02 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.18|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALL  P&L -0.2%  $-0.07                                            HOLD|
|  ALLE  P&L +0.3%  $+0.12                                           HOLD|
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
=== options_live_micro LIVE 2026-09-14T11:02:42.666303-04:00 share=25% ===
2026-09-14 11:02:42,666 INFO === options_live_micro LIVE 2026-09-14T11:02:42.666303-04:00 share=25% ===
Live account equity $226.18 cash $158.29 #225458845 options_level=3
2026-09-14 11:02:42,755 INFO Live account equity $226.18 cash $158.29 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-14 11:02:42,844 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-14 11:02:42,889 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (109 earlier lines - see full log file)
  [b1112 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1113 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b20 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b21 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b284 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b285 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b292 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b293 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b300 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b301 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b780 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b781 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b788 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b789 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b796 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b797 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b804 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b805 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1056 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1057 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1154 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1155 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1098 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1099 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b284 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b285 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b292 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b293 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b300 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b301 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b780 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b781 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b788 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b789 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b796 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b797 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b804 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b805 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1056 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1057 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1154 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1155 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1098 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1099 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1112 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1113 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b20 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b21 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b284 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b285 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b292 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b293 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b300 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b301 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b366 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b367 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b380 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b381 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b422 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b423 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b780 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b781 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b788 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b789 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b796 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b797 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 MARA] ENTRY failed: {"code":40310000,"existing_order_id":"c103b7e0-eb01-43b5-93c6-18dabb5a34cc","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b804 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b805 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b832 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b833 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b860 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b861 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b902 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b903 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b916 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b917 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
```

---

## Run 20260914T150648Z

- UTC timestamp: `20260914T150648Z`
- GitHub run: [#9869](https://github.com/28twagg-ops/TradingBot/actions/runs/34859810797)
- Run id: `34859810797`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260914T150648Z_live_bot.log`, `logs/action_runs/20260914T150648Z_live_options.log`, `logs/action_runs/20260914T150648Z_options_bot.log`


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
{"ts_et":"2026-09-14T10:46:48.440347-04:00","date":"2026-09-14","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":252.3,"phases_s":{"reconcile":2.48,"cancel":0.12,"manage":8.2,"protective_stops":1.53,"scan":35.52,"entries":195.47},"signals":309,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":39,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":["S165:NVDA","S164:NVDA","S168:NVDA","S167:NVDA","S166:NVDA","S163:NVDA","S350:NVDA","S351:NVDA"],"github_run":"9865","github_run_id":"34857646462","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
15:06:51  INFO      Mode: exits
15:06:52  INFO        Daily log -> logs/daily/2026-09-14.md
15:06:52  INFO        Daily log reconciled -> logs/daily/2026-09-14.md (1 ledger rows)
15:06:52  INFO        place_all_stops: checking 2 positions...
15:06:52  INFO        STOP skipped ALL: fractional (0.1317 shares) — software exit will handle it
15:06:52  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
15:06:52  INFO        [positions] 2/2 (2 valid)
15:06:52  INFO        Daily log -> logs/daily/2026-09-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.22|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALL  P&L -0.4%  $-0.14                                            HOLD|
|  ALLE  P&L +0.7%  $+0.22                                           HOLD|
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
=== options_live_micro LIVE 2026-09-14T11:06:53.608871-04:00 share=25% ===
2026-09-14 11:06:53,608 INFO === options_live_micro LIVE 2026-09-14T11:06:53.608871-04:00 share=25% ===
Live account equity $226.22 cash $158.29 #225458845 options_level=3
2026-09-14 11:06:53,819 INFO Live account equity $226.22 cash $158.29 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-14 11:06:53,996 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-14 11:06:54,125 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (143 earlier lines - see full log file)
  [b796 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b797 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b804 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b805 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1056 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1057 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1154 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1155 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1098 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1099 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1112 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1113 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b20 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b21 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b284 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b285 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b292 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b293 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b300 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b301 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b366 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b367 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b380 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b381 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b422 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b423 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b780 MARA] ENTRY failed: {"code":40310000,"existing_order_id":"c103b7e0-eb01-43b5-93c6-18dabb5a34cc","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b781 MARA] ENTRY failed: {"code":40310000,"existing_order_id":"c103b7e0-eb01-43b5-93c6-18dabb5a34cc","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b788 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b789 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b796 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b797 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 MARA] ENTRY failed: {"code":40310000,"existing_order_id":"c103b7e0-eb01-43b5-93c6-18dabb5a34cc","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b804 MARA] ENTRY failed: {"code":40310000,"existing_order_id":"c103b7e0-eb01-43b5-93c6-18dabb5a34cc","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b805 MARA] ENTRY failed: {"code":40310000,"existing_order_id":"c103b7e0-eb01-43b5-93c6-18dabb5a34cc","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b90 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b832 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b833 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b860 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b861 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b888 MARA] ENTRY failed: {"code":40310000,"existing_order_id":"c103b7e0-eb01-43b5-93c6-18dabb5a34cc","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b889 MARA] ENTRY failed: {"code":40310000,"existing_order_id":"c103b7e0-eb01-43b5-93c6-18dabb5a34cc","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b902 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b903 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b916 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b917 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b796 ARM] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b797 ARM] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b832 ARM] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b833 ARM] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b182 CELH] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b183 CELH] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 QQQ] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b196 QQQ] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b197 QQQ] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b238 QQQ] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b239 QQQ] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 IWM] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b196 IWM] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b197 IWM] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b84 BAC] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b85 BAC] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 GS] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b916 GS] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b917 GS] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b84 MS] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b85 MS] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b238 MS] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b239 MS] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b238 BA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b239 BA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1056 GE] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1057 GE] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1098 GE] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1099 GE] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b300 GE] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b301 GE] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b380 GE] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b381 GE] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
```

---

## Run 20260914T151217Z

- UTC timestamp: `20260914T151217Z`
- GitHub run: [#9870](https://github.com/28twagg-ops/TradingBot/actions/runs/34860368798)
- Run id: `34860368798`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260914T151217Z_live_bot.log`, `logs/action_runs/20260914T151217Z_live_options.log`, `logs/action_runs/20260914T151217Z_options_bot.log`


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
15:12:19  INFO      Mode: exits
15:12:19  INFO        Daily log -> logs/daily/2026-09-14.md
15:12:19  INFO        Daily log reconciled -> logs/daily/2026-09-14.md (1 ledger rows)
15:12:19  INFO        place_all_stops: checking 2 positions...
15:12:19  INFO        STOP skipped ALL: fractional (0.1317 shares) — software exit will handle it
15:12:19  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
15:12:19  INFO        [positions] 2/2 (2 valid)
15:12:20  INFO        SELL MARKET [urgent] ALL closed
15:12:22  INFO        TX logged: SELL ALL  P&L -0.58%
15:12:22  INFO        Daily log -> logs/daily/2026-09-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:12 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.21|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALL  P&L -0.6%  $-0.20                         EXIT: stop_loss (-0.6%)|
|  ALLE  P&L +0.8%  $+0.28                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  1 attempted  |  1 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
|  Logged exits                                                         1|
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
|  ALL                                         -0.58%  (threshold -0.50%)|
|  Count                                                                1|
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-09-14T11:12:23.020099-04:00 share=25% ===
2026-09-14 11:12:23,020 INFO === options_live_micro LIVE 2026-09-14T11:12:23.020099-04:00 share=25% ===
Live account equity $226.21 cash $192.01 #225458845 options_level=3
2026-09-14 11:12:23,061 INFO Live account equity $226.21 cash $192.01 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-14 11:12:23,085 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-14 11:12:23,100 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (109 earlier lines - see full log file)
  [b1112 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1113 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b20 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b21 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b284 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b285 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b292 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b293 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b300 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b301 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b780 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b781 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b788 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b789 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b796 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b797 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b804 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b805 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1056 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1057 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1154 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1155 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1098 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1099 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1112 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1113 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b284 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b285 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b292 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b293 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b300 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b301 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b780 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b781 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b788 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b789 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b796 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b797 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b804 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b805 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1056 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1057 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1154 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1155 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1098 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1099 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1112 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1113 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b20 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b21 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b284 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b285 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b292 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b293 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b300 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b301 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b366 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b367 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b380 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b381 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b422 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b423 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b780 MARA] ENTRY failed: {"code":40310000,"existing_order_id":"c103b7e0-eb01-43b5-93c6-18dabb5a34cc","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b781 MARA] ENTRY failed: {"code":40310000,"existing_order_id":"c103b7e0-eb01-43b5-93c6-18dabb5a34cc","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b788 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b789 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b796 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b797 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b804 MARA] ENTRY failed: {"code":40310000,"existing_order_id":"c103b7e0-eb01-43b5-93c6-18dabb5a34cc","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b805 MARA] ENTRY failed: {"code":40310000,"existing_order_id":"c103b7e0-eb01-43b5-93c6-18dabb5a34cc","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b90 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b832 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b833 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b902 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b903 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b916 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b917 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
```

---

## Run 20260914T151638Z

- UTC timestamp: `20260914T151638Z`
- GitHub run: [#9871](https://github.com/28twagg-ops/TradingBot/actions/runs/34860915516)
- Run id: `34860915516`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260914T151638Z_live_bot.log`, `logs/action_runs/20260914T151638Z_live_options.log`, `logs/action_runs/20260914T151638Z_options_bot.log`


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
{"ts_et":"2026-09-14T10:46:48.440347-04:00","date":"2026-09-14","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":252.3,"phases_s":{"reconcile":2.48,"cancel":0.12,"manage":8.2,"protective_stops":1.53,"scan":35.52,"entries":195.47},"signals":309,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":39,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":["S165:NVDA","S164:NVDA","S168:NVDA","S167:NVDA","S166:NVDA","S163:NVDA","S350:NVDA","S351:NVDA"],"github_run":"9865","github_run_id":"34857646462","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
15:16:39  INFO      Mode: exits
15:16:39  INFO        Daily log -> logs/daily/2026-09-14.md
15:16:39  INFO        Daily log reconciled -> logs/daily/2026-09-14.md (1 ledger rows)
15:16:39  INFO        place_all_stops: checking 1 positions...
15:16:39  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
15:16:39  INFO        [positions] 1/1 (1 valid)
15:16:39  INFO        Daily log -> logs/daily/2026-09-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.15|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.7%  $+0.22                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_live_micro LIVE 2026-09-14T11:16:40.462001-04:00 share=25% ===
2026-09-14 11:16:40,462 INFO === options_live_micro LIVE 2026-09-14T11:16:40.462001-04:00 share=25% ===
Live account equity $226.15 cash $192.01 #225458845 options_level=3
2026-09-14 11:16:40,526 INFO Live account equity $226.15 cash $192.01 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-14 11:16:40,562 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-14 11:16:40,592 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (136 earlier lines - see full log file)
  [b284 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b285 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b292 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b293 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b300 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b301 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b780 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b781 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b788 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b789 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b796 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b797 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b804 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b805 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1056 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1057 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1154 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1155 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1098 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1099 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1112 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1113 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b20 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b21 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b284 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b285 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b292 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b293 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b300 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b301 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b366 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b367 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b380 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b381 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b422 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b423 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b780 MARA] ENTRY failed: {"code":40310000,"existing_order_id":"c103b7e0-eb01-43b5-93c6-18dabb5a34cc","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b781 MARA] ENTRY failed: {"code":40310000,"existing_order_id":"c103b7e0-eb01-43b5-93c6-18dabb5a34cc","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b788 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b789 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b796 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b797 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b804 MARA] ENTRY failed: {"code":40310000,"existing_order_id":"c103b7e0-eb01-43b5-93c6-18dabb5a34cc","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b805 MARA] ENTRY failed: {"code":40310000,"existing_order_id":"c103b7e0-eb01-43b5-93c6-18dabb5a34cc","message":"potential wash trade detected. use complex orders","reject_reason":"opposite side market/stop order exists"}
  [b90 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b902 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b903 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b916 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b917 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b796 ARM] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b797 ARM] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b238 UPST] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b239 UPST] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b182 CELH] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b183 CELH] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 QQQ] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b196 QQQ] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b197 QQQ] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b238 QQQ] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b239 QQQ] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 IWM] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b196 IWM] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b197 IWM] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b84 BAC] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b85 BAC] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b84 MS] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b85 MS] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b238 MS] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b239 MS] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b238 BA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b239 BA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b300 GE] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b301 GE] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b380 GE] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b381 GE] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 GE] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b916 GE] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b917 GE] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
```

---

## Run 20260914T152750Z

- UTC timestamp: `20260914T152750Z`
- GitHub run: [#9873](https://github.com/28twagg-ops/TradingBot/actions/runs/34861999834)
- Run id: `34861999834`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260914T152750Z_live_bot.log`, `logs/action_runs/20260914T152750Z_live_options.log`, `logs/action_runs/20260914T152750Z_options_bot.log`


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
{"ts_et":"2026-09-14T10:46:48.440347-04:00","date":"2026-09-14","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":252.3,"phases_s":{"reconcile":2.48,"cancel":0.12,"manage":8.2,"protective_stops":1.53,"scan":35.52,"entries":195.47},"signals":309,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":39,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":["S165:NVDA","S164:NVDA","S168:NVDA","S167:NVDA","S166:NVDA","S163:NVDA","S350:NVDA","S351:NVDA"],"github_run":"9865","github_run_id":"34857646462","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
15:27:51  INFO      Mode: exits
15:27:52  INFO        Daily log -> logs/daily/2026-09-14.md
15:27:52  INFO        Daily log reconciled -> logs/daily/2026-09-14.md (2 ledger rows)
15:27:52  INFO        place_all_stops: checking 1 positions...
15:27:52  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
15:27:52  INFO        [positions] 1/1 (1 valid)
15:27:52  INFO        Daily log -> logs/daily/2026-09-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:27 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.08|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.4%  $+0.15                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_live_micro LIVE 2026-09-14T11:27:53.481757-04:00 share=25% ===
2026-09-14 11:27:53,481 INFO === options_live_micro LIVE 2026-09-14T11:27:53.481757-04:00 share=25% ===
Live account equity $226.08 cash $192.01 #225458845 options_level=3
2026-09-14 11:27:53,706 INFO Live account equity $226.08 cash $192.01 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-14 11:27:53,915 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-14 11:27:54,051 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (110 earlier lines - see full log file)
  [b22 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b23 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b286 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b287 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b294 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b295 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b302 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b303 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b782 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b783 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b790 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b791 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b798 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b799 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b806 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b807 SMCI] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1058 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1059 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1156 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1157 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1100 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1101 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1114 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1115 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b286 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b287 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b294 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b295 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b302 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b303 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b782 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b783 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b790 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b791 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b798 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b799 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b806 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b807 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1058 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1059 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1156 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1157 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1100 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1101 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1114 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1115 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b22 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b23 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b286 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b287 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b294 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b295 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b302 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b303 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b368 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b369 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b382 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b383 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b424 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b425 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b782 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b783 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b790 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b791 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b798 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b799 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b806 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b807 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b834 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b835 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b904 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b905 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b918 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b919 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b240 UPST] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b241 UPST] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
```

---

## Run 20260914T153227Z

- UTC timestamp: `20260914T153227Z`
- GitHub run: [#9874](https://github.com/28twagg-ops/TradingBot/actions/runs/34862547184)
- Run id: `34862547184`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260914T153227Z_live_bot.log`, `logs/action_runs/20260914T153227Z_live_options.log`, `logs/action_runs/20260914T153227Z_options_bot.log`


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
{"ts_et":"2026-09-14T10:46:48.440347-04:00","date":"2026-09-14","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":252.3,"phases_s":{"reconcile":2.48,"cancel":0.12,"manage":8.2,"protective_stops":1.53,"scan":35.52,"entries":195.47},"signals":309,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":39,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":["S165:NVDA","S164:NVDA","S168:NVDA","S167:NVDA","S166:NVDA","S163:NVDA","S350:NVDA","S351:NVDA"],"github_run":"9865","github_run_id":"34857646462","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
15:32:28  INFO      Mode: exits
15:32:28  INFO        Daily log -> logs/daily/2026-09-14.md
15:32:28  INFO        Daily log reconciled -> logs/daily/2026-09-14.md (2 ledger rows)
15:32:28  INFO        place_all_stops: checking 1 positions...
15:32:28  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
15:32:29  INFO        [positions] 1/1 (1 valid)
15:32:29  INFO        Daily log -> logs/daily/2026-09-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:32 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.05|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.4%  $+0.12                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_live_micro LIVE 2026-09-14T11:32:30.276685-04:00 share=25% ===
2026-09-14 11:32:30,276 INFO === options_live_micro LIVE 2026-09-14T11:32:30.276685-04:00 share=25% ===
Live account equity $226.05 cash $192.01 #225458845 options_level=3
2026-09-14 11:32:30,503 INFO Live account equity $226.05 cash $192.01 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-09-14 11:32:30,680 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-09-14 11:32:30,798 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (130 earlier lines - see full log file)
  [b1157 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1100 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1101 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1114 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1115 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b286 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b287 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b294 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b295 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b302 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b303 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b782 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b783 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b790 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b791 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b798 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b799 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b806 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b807 AVGO] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1058 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1059 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1156 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1157 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1100 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1101 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1114 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b1115 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b22 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b23 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b286 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b287 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b294 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b295 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b302 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b303 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b368 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b369 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b382 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b383 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b424 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b425 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b782 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b783 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b790 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b791 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b798 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b799 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b806 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b807 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b834 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b835 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b862 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b863 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b904 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b905 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b918 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b919 MARA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b240 UPST] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b241 UPST] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b184 CELH] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b185 CELH] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 QQQ] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b198 QQQ] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b199 QQQ] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b240 QQQ] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b241 QQQ] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b90 IWM] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b198 IWM] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b199 IWM] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b86 BAC] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b87 BAC] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b86 MS] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b87 MS] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b240 MS] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b241 MS] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b240 BA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
  [b241 BA] ENTRY failed: {"code":50010000,"message":"internal server error occurred"}
```

---

## Run 20260914T153747Z

- UTC timestamp: `20260914T153747Z`
- GitHub run: [#9875](https://github.com/28twagg-ops/TradingBot/actions/runs/34863109331)
- Run id: `34863109331`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`34s`
- Full logs: `logs/action_runs/20260914T153747Z_live_bot.log`, `logs/action_runs/20260914T153747Z_live_options.log`, `logs/action_runs/20260914T153747Z_options_bot.log`


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
{"ts_et":"2026-09-14T11:37:55.863458-04:00","date":"2026-09-14","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":21.0,"phases_s":{"reconcile":2.59,"cancel":0.22,"manage":7.31,"protective_stops":1.59},"signals":0,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":39,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9875","github_run_id":"34863109331","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
15:37:49  INFO      Mode: exits
15:37:49  INFO        Daily log -> logs/daily/2026-09-14.md
15:37:49  INFO        Daily log reconciled -> logs/daily/2026-09-14.md (2 ledger rows)
15:37:49  INFO        place_all_stops: checking 1 positions...
15:37:49  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
15:37:50  INFO        [positions] 1/1 (1 valid)
15:37:50  INFO        Daily log -> logs/daily/2026-09-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:37 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.11|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.5%  $+0.18                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_live_micro LIVE 2026-09-14T11:37:51.820376-04:00 share=25% ===
2026-09-14 11:37:51,820 INFO === options_live_micro LIVE 2026-09-14T11:37:51.820376-04:00 share=25% ===
Live account equity $226.11 cash $192.01 #225458845 options_level=3
2026-09-14 11:37:52,051 INFO Live account equity $226.11 cash $192.01 #225458845 options_level=3
Live micro: manage/exits only
2026-09-14 11:37:52,345 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-14 11:37:52,414 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (164 earlier lines - see full log file)
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
| Total open lots             |    39 | INFO |
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
equity=226.11 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260914T154109Z

- UTC timestamp: `20260914T154109Z`
- GitHub run: [#9876](https://github.com/28twagg-ops/TradingBot/actions/runs/34863659858)
- Run id: `34863659858`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`33s`
- Full logs: `logs/action_runs/20260914T154109Z_live_bot.log`, `logs/action_runs/20260914T154109Z_live_options.log`, `logs/action_runs/20260914T154109Z_options_bot.log`


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
{"ts_et":"2026-09-14T11:41:17.469046-04:00","date":"2026-09-14","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":21.2,"phases_s":{"reconcile":2.67,"cancel":0.23,"manage":7.2,"protective_stops":1.78},"signals":0,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":39,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9876","github_run_id":"34863659858","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
15:41:10  INFO      Mode: exits
15:41:11  INFO        Daily log -> logs/daily/2026-09-14.md
15:41:11  INFO        Daily log reconciled -> logs/daily/2026-09-14.md (2 ledger rows)
15:41:11  INFO        place_all_stops: checking 1 positions...
15:41:11  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
15:41:12  INFO        [positions] 1/1 (1 valid)
15:41:12  INFO        Daily log -> logs/daily/2026-09-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.17|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.7%  $+0.24                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_live_micro LIVE 2026-09-14T11:41:13.875815-04:00 share=25% ===
2026-09-14 11:41:13,875 INFO === options_live_micro LIVE 2026-09-14T11:41:13.875815-04:00 share=25% ===
Live account equity $226.17 cash $192.01 #225458845 options_level=3
2026-09-14 11:41:14,112 INFO Live account equity $226.17 cash $192.01 #225458845 options_level=3
Live micro: manage/exits only
2026-09-14 11:41:14,365 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-14 11:41:14,440 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (164 earlier lines - see full log file)
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
| Total open lots             |    39 | INFO |
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
equity=226.17 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260914T154614Z

- UTC timestamp: `20260914T154614Z`
- GitHub run: [#9877](https://github.com/28twagg-ops/TradingBot/actions/runs/34864196194)
- Run id: `34864196194`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`29s`
- Full logs: `logs/action_runs/20260914T154614Z_live_bot.log`, `logs/action_runs/20260914T154614Z_live_options.log`, `logs/action_runs/20260914T154614Z_options_bot.log`


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
{"ts_et":"2026-09-14T11:46:19.496686-04:00","date":"2026-09-14","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":16.5,"phases_s":{"reconcile":2.15,"cancel":0.04,"manage":5.25,"protective_stops":0.38},"signals":0,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":39,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9877","github_run_id":"34864196194","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
15:46:15  INFO      Mode: exits
15:46:15  INFO        Daily log -> logs/daily/2026-09-14.md
15:46:15  INFO        Daily log reconciled -> logs/daily/2026-09-14.md (2 ledger rows)
15:46:15  INFO        place_all_stops: checking 1 positions...
15:46:15  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
15:46:15  INFO        [positions] 1/1 (1 valid)
15:46:15  INFO        Daily log -> logs/daily/2026-09-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.30|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +1.1%  $+0.37                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_live_micro LIVE 2026-09-14T11:46:16.545339-04:00 share=25% ===
2026-09-14 11:46:16,545 INFO === options_live_micro LIVE 2026-09-14T11:46:16.545339-04:00 share=25% ===
Live account equity $226.30 cash $192.01 #225458845 options_level=3
2026-09-14 11:46:16,594 INFO Live account equity $226.30 cash $192.01 #225458845 options_level=3
Live micro: manage/exits only
2026-09-14 11:46:16,636 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-14 11:46:16,649 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (164 earlier lines - see full log file)
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
| Total open lots             |    39 | INFO |
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
equity=226.3 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260914T155107Z

- UTC timestamp: `20260914T155107Z`
- GitHub run: [#9878](https://github.com/28twagg-ops/TradingBot/actions/runs/34864748748)
- Run id: `34864748748`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`33s`
- Full logs: `logs/action_runs/20260914T155107Z_live_bot.log`, `logs/action_runs/20260914T155107Z_live_options.log`, `logs/action_runs/20260914T155107Z_options_bot.log`


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
{"ts_et":"2026-09-14T11:51:14.722867-04:00","date":"2026-09-14","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":21.1,"phases_s":{"reconcile":2.58,"cancel":0.22,"manage":7.25,"protective_stops":1.82},"signals":0,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":39,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9878","github_run_id":"34864748748","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
15:51:08  INFO      Mode: exits
15:51:09  INFO        Daily log -> logs/daily/2026-09-14.md
15:51:09  INFO        Daily log reconciled -> logs/daily/2026-09-14.md (2 ledger rows)
15:51:09  INFO        place_all_stops: checking 1 positions...
15:51:09  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
15:51:09  INFO        [positions] 1/1 (1 valid)
15:51:10  INFO        Daily log -> logs/daily/2026-09-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:51 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.26|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +1.0%  $+0.33                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_live_micro LIVE 2026-09-14T11:51:10.909037-04:00 share=25% ===
2026-09-14 11:51:10,909 INFO === options_live_micro LIVE 2026-09-14T11:51:10.909037-04:00 share=25% ===
Live account equity $226.26 cash $192.01 #225458845 options_level=3
2026-09-14 11:51:11,139 INFO Live account equity $226.26 cash $192.01 #225458845 options_level=3
Live micro: manage/exits only
2026-09-14 11:51:11,423 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-14 11:51:11,492 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (164 earlier lines - see full log file)
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
| Total open lots             |    39 | INFO |
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
equity=226.26 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260914T155607Z

- UTC timestamp: `20260914T155607Z`
- GitHub run: [#9879](https://github.com/28twagg-ops/TradingBot/actions/runs/34865282734)
- Run id: `34865282734`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`33s`
- Full logs: `logs/action_runs/20260914T155607Z_live_bot.log`, `logs/action_runs/20260914T155607Z_live_options.log`, `logs/action_runs/20260914T155607Z_options_bot.log`


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
{"ts_et":"2026-09-14T11:56:14.626616-04:00","date":"2026-09-14","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":21.2,"phases_s":{"reconcile":2.61,"cancel":0.22,"manage":7.48,"protective_stops":1.62},"signals":0,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":39,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9879","github_run_id":"34865282734","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
15:56:08  INFO      Mode: exits
15:56:09  INFO        Daily log -> logs/daily/2026-09-14.md
15:56:09  INFO        Daily log reconciled -> logs/daily/2026-09-14.md (2 ledger rows)
15:56:09  INFO        place_all_stops: checking 1 positions...
15:56:09  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
15:56:09  INFO        [positions] 1/1 (1 valid)
15:56:09  INFO        Daily log -> logs/daily/2026-09-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:56 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.28|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +1.0%  $+0.35                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_live_micro LIVE 2026-09-14T11:56:10.706316-04:00 share=25% ===
2026-09-14 11:56:10,706 INFO === options_live_micro LIVE 2026-09-14T11:56:10.706316-04:00 share=25% ===
Live account equity $226.28 cash $192.01 #225458845 options_level=3
2026-09-14 11:56:10,951 INFO Live account equity $226.28 cash $192.01 #225458845 options_level=3
Live micro: manage/exits only
2026-09-14 11:56:11,172 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-14 11:56:11,244 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (164 earlier lines - see full log file)
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
| Total open lots             |    39 | INFO |
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
equity=226.28 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260914T160113Z

- UTC timestamp: `20260914T160113Z`
- GitHub run: [#9880](https://github.com/28twagg-ops/TradingBot/actions/runs/34865808746)
- Run id: `34865808746`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`31s`
- Full logs: `logs/action_runs/20260914T160113Z_live_bot.log`, `logs/action_runs/20260914T160113Z_live_options.log`, `logs/action_runs/20260914T160113Z_options_bot.log`


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
{"ts_et":"2026-09-14T12:01:21.929601-04:00","date":"2026-09-14","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":19.7,"phases_s":{"reconcile":2.45,"cancel":0.17,"manage":6.63,"protective_stops":1.38},"signals":0,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":39,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9880","github_run_id":"34865808746","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
16:01:16  INFO      Mode: exits
16:01:17  INFO        Daily log -> logs/daily/2026-09-14.md
16:01:17  INFO        Daily log reconciled -> logs/daily/2026-09-14.md (2 ledger rows)
16:01:17  INFO        place_all_stops: checking 1 positions...
16:01:17  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
16:01:17  INFO        [positions] 1/1 (1 valid)
16:01:17  INFO        Daily log -> logs/daily/2026-09-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.33|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +1.2%  $+0.40                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_live_micro LIVE 2026-09-14T12:01:18.504646-04:00 share=25% ===
2026-09-14 12:01:18,504 INFO === options_live_micro LIVE 2026-09-14T12:01:18.504646-04:00 share=25% ===
Live account equity $226.33 cash $192.01 #225458845 options_level=3
2026-09-14 12:01:18,717 INFO Live account equity $226.33 cash $192.01 #225458845 options_level=3
Live micro: manage/exits only
2026-09-14 12:01:18,891 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-14 12:01:18,947 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (164 earlier lines - see full log file)
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
| Total open lots             |    39 | INFO |
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
equity=226.33 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260914T160603Z

- UTC timestamp: `20260914T160603Z`
- GitHub run: [#9881](https://github.com/28twagg-ops/TradingBot/actions/runs/34866347541)
- Run id: `34866347541`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`27s`
- Full logs: `logs/action_runs/20260914T160603Z_live_bot.log`, `logs/action_runs/20260914T160603Z_live_options.log`, `logs/action_runs/20260914T160603Z_options_bot.log`


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
{"ts_et":"2026-09-14T12:06:07.892257-04:00","date":"2026-09-14","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":16.2,"phases_s":{"reconcile":2.14,"cancel":0.03,"manage":5.15,"protective_stops":0.32},"signals":0,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":39,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9881","github_run_id":"34866347541","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
16:06:04  INFO      Mode: exits
16:06:04  INFO        Daily log -> logs/daily/2026-09-14.md
16:06:04  INFO        Daily log reconciled -> logs/daily/2026-09-14.md (2 ledger rows)
16:06:04  INFO        place_all_stops: checking 1 positions...
16:06:04  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
16:06:04  INFO        [positions] 1/1 (1 valid)
16:06:04  INFO        Daily log -> logs/daily/2026-09-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.33|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +1.2%  $+0.40                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_live_micro LIVE 2026-09-14T12:06:05.191834-04:00 share=25% ===
2026-09-14 12:06:05,191 INFO === options_live_micro LIVE 2026-09-14T12:06:05.191834-04:00 share=25% ===
Live account equity $226.33 cash $192.01 #225458845 options_level=3
2026-09-14 12:06:05,239 INFO Live account equity $226.33 cash $192.01 #225458845 options_level=3
Live micro: manage/exits only
2026-09-14 12:06:05,270 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-14 12:06:05,277 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (164 earlier lines - see full log file)
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
| Total open lots             |    39 | INFO |
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
equity=226.33 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260914T161103Z

- UTC timestamp: `20260914T161103Z`
- GitHub run: [#9882](https://github.com/28twagg-ops/TradingBot/actions/runs/34866895771)
- Run id: `34866895771`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`28s`
- Full logs: `logs/action_runs/20260914T161103Z_live_bot.log`, `logs/action_runs/20260914T161103Z_live_options.log`, `logs/action_runs/20260914T161103Z_options_bot.log`


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
{"ts_et":"2026-09-14T12:11:09.075691-04:00","date":"2026-09-14","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":16.4,"phases_s":{"reconcile":2.12,"cancel":0.03,"manage":5.32,"protective_stops":0.26},"signals":0,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":39,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9882","github_run_id":"34866895771","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
16:11:05  INFO      Mode: exits
16:11:05  INFO        Daily log -> logs/daily/2026-09-14.md
16:11:05  INFO        Daily log reconciled -> logs/daily/2026-09-14.md (2 ledger rows)
16:11:05  INFO        place_all_stops: checking 1 positions...
16:11:05  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
16:11:05  INFO        [positions] 1/1 (1 valid)
16:11:05  INFO        Daily log -> logs/daily/2026-09-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.38|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +1.3%  $+0.45                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_live_micro LIVE 2026-09-14T12:11:06.258094-04:00 share=25% ===
2026-09-14 12:11:06,258 INFO === options_live_micro LIVE 2026-09-14T12:11:06.258094-04:00 share=25% ===
Live account equity $226.38 cash $192.01 #225458845 options_level=3
2026-09-14 12:11:06,301 INFO Live account equity $226.38 cash $192.01 #225458845 options_level=3
Live micro: manage/exits only
2026-09-14 12:11:06,340 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-14 12:11:06,350 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (164 earlier lines - see full log file)
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
| Total open lots             |    39 | INFO |
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

## Run 20260914T161606Z

- UTC timestamp: `20260914T161606Z`
- GitHub run: [#9883](https://github.com/28twagg-ops/TradingBot/actions/runs/34867412338)
- Run id: `34867412338`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`29s`
- Full logs: `logs/action_runs/20260914T161606Z_live_bot.log`, `logs/action_runs/20260914T161606Z_live_options.log`, `logs/action_runs/20260914T161606Z_options_bot.log`


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
{"ts_et":"2026-09-14T12:16:12.514615-04:00","date":"2026-09-14","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":18.2,"phases_s":{"reconcile":2.29,"cancel":0.12,"manage":6.06,"protective_stops":0.85},"signals":0,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":39,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9883","github_run_id":"34867412338","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
16:16:07  INFO      Mode: exits
16:16:08  INFO        Daily log -> logs/daily/2026-09-14.md
16:16:08  INFO        Daily log reconciled -> logs/daily/2026-09-14.md (2 ledger rows)
16:16:08  INFO        place_all_stops: checking 1 positions...
16:16:08  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
16:16:08  INFO        [positions] 1/1 (1 valid)
16:16:08  INFO        Daily log -> logs/daily/2026-09-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.41|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +1.4%  $+0.48                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_live_micro LIVE 2026-09-14T12:16:09.519226-04:00 share=25% ===
2026-09-14 12:16:09,519 INFO === options_live_micro LIVE 2026-09-14T12:16:09.519226-04:00 share=25% ===
Live account equity $226.41 cash $192.01 #225458845 options_level=3
2026-09-14 12:16:09,645 INFO Live account equity $226.41 cash $192.01 #225458845 options_level=3
Live micro: manage/exits only
2026-09-14 12:16:09,749 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-14 12:16:09,787 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (164 earlier lines - see full log file)
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
| Total open lots             |    39 | INFO |
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
equity=226.41 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260914T162108Z

- UTC timestamp: `20260914T162108Z`
- GitHub run: [#9884](https://github.com/28twagg-ops/TradingBot/actions/runs/34867939895)
- Run id: `34867939895`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`30s`
- Full logs: `logs/action_runs/20260914T162108Z_live_bot.log`, `logs/action_runs/20260914T162108Z_live_options.log`, `logs/action_runs/20260914T162108Z_options_bot.log`


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
{"ts_et":"2026-09-14T12:21:14.505924-04:00","date":"2026-09-14","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":17.7,"phases_s":{"reconcile":2.23,"cancel":0.08,"manage":5.75,"protective_stops":0.75},"signals":0,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":39,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9884","github_run_id":"34867939895","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
16:21:09  INFO      Mode: exits
16:21:10  INFO        Daily log -> logs/daily/2026-09-14.md
16:21:10  INFO        Daily log reconciled -> logs/daily/2026-09-14.md (2 ledger rows)
16:21:10  INFO        place_all_stops: checking 1 positions...
16:21:10  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
16:21:10  INFO        [positions] 1/1 (1 valid)
16:21:10  INFO        Daily log -> logs/daily/2026-09-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.43|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +1.5%  $+0.50                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_live_micro LIVE 2026-09-14T12:21:11.223727-04:00 share=25% ===
2026-09-14 12:21:11,223 INFO === options_live_micro LIVE 2026-09-14T12:21:11.223727-04:00 share=25% ===
Live account equity $226.43 cash $192.01 #225458845 options_level=3
2026-09-14 12:21:11,311 INFO Live account equity $226.43 cash $192.01 #225458845 options_level=3
Live micro: manage/exits only
2026-09-14 12:21:11,392 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-14 12:21:11,414 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (164 earlier lines - see full log file)
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
| Total open lots             |    39 | INFO |
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
equity=226.43 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260914T162608Z

- UTC timestamp: `20260914T162608Z`
- GitHub run: [#9885](https://github.com/28twagg-ops/TradingBot/actions/runs/34868473153)
- Run id: `34868473153`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`32s`
- Full logs: `logs/action_runs/20260914T162608Z_live_bot.log`, `logs/action_runs/20260914T162608Z_live_options.log`, `logs/action_runs/20260914T162608Z_options_bot.log`


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
{"ts_et":"2026-09-14T12:26:15.511700-04:00","date":"2026-09-14","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":20.1,"phases_s":{"reconcile":2.49,"cancel":0.18,"manage":6.77,"protective_stops":1.58},"signals":0,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":39,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9885","github_run_id":"34868473153","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
16:26:09  INFO      Mode: exits
16:26:10  INFO        Daily log -> logs/daily/2026-09-14.md
16:26:10  INFO        Daily log reconciled -> logs/daily/2026-09-14.md (2 ledger rows)
16:26:10  INFO        place_all_stops: checking 1 positions...
16:26:10  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
16:26:10  INFO        [positions] 1/1 (1 valid)
16:26:10  INFO        Daily log -> logs/daily/2026-09-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.44|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +1.5%  $+0.51                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_live_micro LIVE 2026-09-14T12:26:12.045362-04:00 share=25% ===
2026-09-14 12:26:12,045 INFO === options_live_micro LIVE 2026-09-14T12:26:12.045362-04:00 share=25% ===
Live account equity $226.44 cash $192.01 #225458845 options_level=3
2026-09-14 12:26:12,243 INFO Live account equity $226.44 cash $192.01 #225458845 options_level=3
Live micro: manage/exits only
2026-09-14 12:26:12,417 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-14 12:26:12,475 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (164 earlier lines - see full log file)
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
| Total open lots             |    39 | INFO |
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

## Run 20260914T163157Z

- UTC timestamp: `20260914T163157Z`
- GitHub run: [#9886](https://github.com/28twagg-ops/TradingBot/actions/runs/34868990718)
- Run id: `34868990718`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`29s`
- Full logs: `logs/action_runs/20260914T163157Z_live_bot.log`, `logs/action_runs/20260914T163157Z_live_options.log`, `logs/action_runs/20260914T163157Z_options_bot.log`


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
{"ts_et":"2026-09-14T12:32:02.624473-04:00","date":"2026-09-14","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":16.6,"phases_s":{"reconcile":2.15,"cancel":0.03,"manage":5.44,"protective_stops":0.3},"signals":0,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":39,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9886","github_run_id":"34868990718","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
16:31:58  INFO      Mode: exits
16:31:58  INFO        Daily log -> logs/daily/2026-09-14.md
16:31:58  INFO        Daily log reconciled -> logs/daily/2026-09-14.md (2 ledger rows)
16:31:58  INFO        place_all_stops: checking 1 positions...
16:31:58  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
16:31:58  INFO        [positions] 1/1 (1 valid)
16:31:58  INFO        Daily log -> logs/daily/2026-09-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.42|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +1.4%  $+0.49                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_live_micro LIVE 2026-09-14T12:31:59.702803-04:00 share=25% ===
2026-09-14 12:31:59,702 INFO === options_live_micro LIVE 2026-09-14T12:31:59.702803-04:00 share=25% ===
Live account equity $226.42 cash $192.01 #225458845 options_level=3
2026-09-14 12:31:59,742 INFO Live account equity $226.42 cash $192.01 #225458845 options_level=3
Live micro: manage/exits only
2026-09-14 12:31:59,762 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-14 12:31:59,769 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (164 earlier lines - see full log file)
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
| Total open lots             |    39 | INFO |
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
equity=226.42 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260914T163608Z

- UTC timestamp: `20260914T163608Z`
- GitHub run: [#9887](https://github.com/28twagg-ops/TradingBot/actions/runs/34869506010)
- Run id: `34869506010`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`32s`
- Full logs: `logs/action_runs/20260914T163608Z_live_bot.log`, `logs/action_runs/20260914T163608Z_live_options.log`, `logs/action_runs/20260914T163608Z_options_bot.log`


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
{"ts_et":"2026-09-14T12:36:14.713280-04:00","date":"2026-09-14","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":19.8,"phases_s":{"reconcile":2.47,"cancel":0.18,"manage":6.6,"protective_stops":1.39},"signals":0,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":39,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9887","github_run_id":"34869506010","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
16:36:09  INFO      Mode: exits
16:36:09  INFO        Daily log -> logs/daily/2026-09-14.md
16:36:09  INFO        Daily log reconciled -> logs/daily/2026-09-14.md (2 ledger rows)
16:36:09  INFO        place_all_stops: checking 1 positions...
16:36:09  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
16:36:10  INFO        [positions] 1/1 (1 valid)
16:36:10  INFO        Daily log -> logs/daily/2026-09-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.40|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +1.4%  $+0.47                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_live_micro LIVE 2026-09-14T12:36:11.186981-04:00 share=25% ===
2026-09-14 12:36:11,187 INFO === options_live_micro LIVE 2026-09-14T12:36:11.186981-04:00 share=25% ===
Live account equity $226.40 cash $192.01 #225458845 options_level=3
2026-09-14 12:36:11,407 INFO Live account equity $226.40 cash $192.01 #225458845 options_level=3
Live micro: manage/exits only
2026-09-14 12:36:11,580 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-14 12:36:11,656 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (164 earlier lines - see full log file)
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
| Total open lots             |    39 | INFO |
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

## Run 20260914T164106Z

- UTC timestamp: `20260914T164106Z`
- GitHub run: [#9888](https://github.com/28twagg-ops/TradingBot/actions/runs/34870014909)
- Run id: `34870014909`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`33s`
- Full logs: `logs/action_runs/20260914T164106Z_live_bot.log`, `logs/action_runs/20260914T164106Z_live_options.log`, `logs/action_runs/20260914T164106Z_options_bot.log`


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
{"ts_et":"2026-09-14T12:41:13.928916-04:00","date":"2026-09-14","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":21.0,"phases_s":{"reconcile":2.58,"cancel":0.21,"manage":7.25,"protective_stops":1.62},"signals":0,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":39,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9888","github_run_id":"34870014909","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
16:41:07  INFO      Mode: exits
16:41:08  INFO        Daily log -> logs/daily/2026-09-14.md
16:41:08  INFO        Daily log reconciled -> logs/daily/2026-09-14.md (2 ledger rows)
16:41:08  INFO        place_all_stops: checking 1 positions...
16:41:08  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
16:41:08  INFO        [positions] 1/1 (1 valid)
16:41:09  INFO        Daily log -> logs/daily/2026-09-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.37|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +1.3%  $+0.44                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_live_micro LIVE 2026-09-14T12:41:10.247146-04:00 share=25% ===
2026-09-14 12:41:10,247 INFO === options_live_micro LIVE 2026-09-14T12:41:10.247146-04:00 share=25% ===
Live account equity $226.37 cash $192.01 #225458845 options_level=3
2026-09-14 12:41:10,475 INFO Live account equity $226.37 cash $192.01 #225458845 options_level=3
Live micro: manage/exits only
2026-09-14 12:41:10,683 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-14 12:41:10,754 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (164 earlier lines - see full log file)
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
| Total open lots             |    39 | INFO |
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

## Run 20260914T164608Z

- UTC timestamp: `20260914T164608Z`
- GitHub run: [#9889](https://github.com/28twagg-ops/TradingBot/actions/runs/34870526267)
- Run id: `34870526267`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`27s`
- Full logs: `logs/action_runs/20260914T164608Z_live_bot.log`, `logs/action_runs/20260914T164608Z_live_options.log`, `logs/action_runs/20260914T164608Z_options_bot.log`


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
{"ts_et":"2026-09-14T12:46:13.691725-04:00","date":"2026-09-14","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":18.4,"phases_s":{"reconcile":2.4,"cancel":0.15,"manage":5.94,"protective_stops":1.11},"signals":0,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":39,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9889","github_run_id":"34870526267","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
16:46:09  INFO      Mode: exits
16:46:09  INFO        Daily log -> logs/daily/2026-09-14.md
16:46:09  INFO        Daily log reconciled -> logs/daily/2026-09-14.md (2 ledger rows)
16:46:09  INFO        place_all_stops: checking 1 positions...
16:46:09  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
16:46:10  INFO        [positions] 1/1 (1 valid)
16:46:10  INFO        Daily log -> logs/daily/2026-09-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.40|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +1.4%  $+0.47                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_live_micro LIVE 2026-09-14T12:46:10.910311-04:00 share=25% ===
2026-09-14 12:46:10,910 INFO === options_live_micro LIVE 2026-09-14T12:46:10.910311-04:00 share=25% ===
Live account equity $226.40 cash $192.01 #225458845 options_level=3
2026-09-14 12:46:11,099 INFO Live account equity $226.40 cash $192.01 #225458845 options_level=3
Live micro: manage/exits only
2026-09-14 12:46:11,204 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-14 12:46:11,238 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (164 earlier lines - see full log file)
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
| Total open lots             |    39 | INFO |
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

## Run 20260914T165100Z

- UTC timestamp: `20260914T165100Z`
- GitHub run: [#9890](https://github.com/28twagg-ops/TradingBot/actions/runs/34871036842)
- Run id: `34871036842`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`27s`
- Full logs: `logs/action_runs/20260914T165100Z_live_bot.log`, `logs/action_runs/20260914T165100Z_live_options.log`, `logs/action_runs/20260914T165100Z_options_bot.log`


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
{"ts_et":"2026-09-14T12:51:07.810261-04:00","date":"2026-09-14","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":19.9,"phases_s":{"reconcile":2.55,"cancel":0.18,"manage":6.66,"protective_stops":1.56},"signals":0,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":39,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9890","github_run_id":"34871036842","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
16:51:01  INFO      Mode: exits
16:51:02  INFO        Daily log -> logs/daily/2026-09-14.md
16:51:02  INFO        Daily log reconciled -> logs/daily/2026-09-14.md (2 ledger rows)
16:51:02  INFO        place_all_stops: checking 1 positions...
16:51:02  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
16:51:02  INFO        [positions] 1/1 (1 valid)
16:51:03  INFO        Daily log -> logs/daily/2026-09-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:51 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.48|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +1.6%  $+0.55                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_live_micro LIVE 2026-09-14T12:51:04.204654-04:00 share=25% ===
2026-09-14 12:51:04,204 INFO === options_live_micro LIVE 2026-09-14T12:51:04.204654-04:00 share=25% ===
Live account equity $226.48 cash $192.01 #225458845 options_level=3
2026-09-14 12:51:04,940 INFO Live account equity $226.48 cash $192.01 #225458845 options_level=3
Live micro: manage/exits only
2026-09-14 12:51:05,227 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-14 12:51:05,329 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (164 earlier lines - see full log file)
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
| Total open lots             |    39 | INFO |
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
equity=226.48 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260914T165601Z

- UTC timestamp: `20260914T165601Z`
- GitHub run: [#9891](https://github.com/28twagg-ops/TradingBot/actions/runs/34871543493)
- Run id: `34871543493`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`29s`
- Full logs: `logs/action_runs/20260914T165601Z_live_bot.log`, `logs/action_runs/20260914T165601Z_live_options.log`, `logs/action_runs/20260914T165601Z_options_bot.log`


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
{"ts_et":"2026-09-14T12:56:08.501468-04:00","date":"2026-09-14","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":16.6,"phases_s":{"reconcile":2.12,"cancel":0.03,"manage":5.22,"protective_stops":0.5},"signals":0,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":39,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9891","github_run_id":"34871543493","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
16:56:04  INFO      Mode: exits
16:56:04  INFO        Daily log -> logs/daily/2026-09-14.md
16:56:04  INFO        Daily log reconciled -> logs/daily/2026-09-14.md (2 ledger rows)
16:56:04  INFO        place_all_stops: checking 1 positions...
16:56:04  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
16:56:04  INFO        [positions] 1/1 (1 valid)
16:56:04  INFO        Daily log -> logs/daily/2026-09-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:56 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.49|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +1.7%  $+0.56                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_live_micro LIVE 2026-09-14T12:56:05.592876-04:00 share=25% ===
2026-09-14 12:56:05,592 INFO === options_live_micro LIVE 2026-09-14T12:56:05.592876-04:00 share=25% ===
Live account equity $226.49 cash $192.01 #225458845 options_level=3
2026-09-14 12:56:05,643 INFO Live account equity $226.49 cash $192.01 #225458845 options_level=3
Live micro: manage/exits only
2026-09-14 12:56:05,677 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-14 12:56:05,689 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (164 earlier lines - see full log file)
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
| Total open lots             |    39 | INFO |
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
equity=226.49 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260914T170109Z

- UTC timestamp: `20260914T170109Z`
- GitHub run: [#9892](https://github.com/28twagg-ops/TradingBot/actions/runs/34872042162)
- Run id: `34872042162`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`29s`
- Full logs: `logs/action_runs/20260914T170109Z_live_bot.log`, `logs/action_runs/20260914T170109Z_live_options.log`, `logs/action_runs/20260914T170109Z_options_bot.log`


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
{"ts_et":"2026-09-14T13:01:14.512266-04:00","date":"2026-09-14","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":16.8,"phases_s":{"reconcile":2.16,"cancel":0.03,"manage":5.64,"protective_stops":0.25},"signals":0,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":39,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9892","github_run_id":"34872042162","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
17:01:10  INFO      Mode: exits
17:01:10  INFO        Daily log -> logs/daily/2026-09-14.md
17:01:10  INFO        Daily log reconciled -> logs/daily/2026-09-14.md (2 ledger rows)
17:01:10  INFO        place_all_stops: checking 1 positions...
17:01:10  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
17:01:10  INFO        [positions] 1/1 (1 valid)
17:01:10  INFO        Daily log -> logs/daily/2026-09-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.46|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +1.5%  $+0.53                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_live_micro LIVE 2026-09-14T13:01:11.751314-04:00 share=25% ===
2026-09-14 13:01:11,751 INFO === options_live_micro LIVE 2026-09-14T13:01:11.751314-04:00 share=25% ===
Live account equity $226.46 cash $192.01 #225458845 options_level=3
2026-09-14 13:01:11,795 INFO Live account equity $226.46 cash $192.01 #225458845 options_level=3
Live micro: manage/exits only
2026-09-14 13:01:11,833 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-14 13:01:11,841 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (164 earlier lines - see full log file)
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
| Total open lots             |    39 | INFO |
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
equity=226.46 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260914T170607Z

- UTC timestamp: `20260914T170607Z`
- GitHub run: [#9893](https://github.com/28twagg-ops/TradingBot/actions/runs/34872558851)
- Run id: `34872558851`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`25s`
- Full logs: `logs/action_runs/20260914T170607Z_live_bot.log`, `logs/action_runs/20260914T170607Z_live_options.log`, `logs/action_runs/20260914T170607Z_options_bot.log`


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
{"ts_et":"2026-09-14T13:06:12.069835-04:00","date":"2026-09-14","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":17.0,"phases_s":{"reconcile":2.21,"cancel":0.08,"manage":5.48,"protective_stops":0.61},"signals":0,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":39,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9893","github_run_id":"34872558851","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
17:06:08  INFO      Mode: exits
17:06:08  INFO        Daily log -> logs/daily/2026-09-14.md
17:06:08  INFO        Daily log reconciled -> logs/daily/2026-09-14.md (2 ledger rows)
17:06:08  INFO        place_all_stops: checking 1 positions...
17:06:08  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
17:06:08  INFO        [positions] 1/1 (1 valid)
17:06:09  INFO        Daily log -> logs/daily/2026-09-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.46|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +1.6%  $+0.53                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_live_micro LIVE 2026-09-14T13:06:09.705067-04:00 share=25% ===
2026-09-14 13:06:09,705 INFO === options_live_micro LIVE 2026-09-14T13:06:09.705067-04:00 share=25% ===
Live account equity $226.46 cash $192.01 #225458845 options_level=3
2026-09-14 13:06:09,784 INFO Live account equity $226.46 cash $192.01 #225458845 options_level=3
Live micro: manage/exits only
2026-09-14 13:06:09,963 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-14 13:06:09,984 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (164 earlier lines - see full log file)
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
| Total open lots             |    39 | INFO |
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
equity=226.46 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260914T171103Z

- UTC timestamp: `20260914T171103Z`
- GitHub run: [#9894](https://github.com/28twagg-ops/TradingBot/actions/runs/34873080081)
- Run id: `34873080081`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`29s`
- Full logs: `logs/action_runs/20260914T171103Z_live_bot.log`, `logs/action_runs/20260914T171103Z_live_options.log`, `logs/action_runs/20260914T171103Z_options_bot.log`


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
{"ts_et":"2026-09-14T13:11:08.919843-04:00","date":"2026-09-14","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":19.5,"phases_s":{"reconcile":2.46,"cancel":0.17,"manage":6.59,"protective_stops":1.34},"signals":0,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":39,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9894","github_run_id":"34873080081","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
17:11:03  INFO      Mode: exits
17:11:04  INFO        Daily log -> logs/daily/2026-09-14.md
17:11:04  INFO        Daily log reconciled -> logs/daily/2026-09-14.md (2 ledger rows)
17:11:04  INFO        place_all_stops: checking 1 positions...
17:11:04  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
17:11:04  INFO        [positions] 1/1 (1 valid)
17:11:05  INFO        Daily log -> logs/daily/2026-09-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.36|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +1.3%  $+0.43                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_live_micro LIVE 2026-09-14T13:11:05.712492-04:00 share=25% ===
2026-09-14 13:11:05,712 INFO === options_live_micro LIVE 2026-09-14T13:11:05.712492-04:00 share=25% ===
Live account equity $226.36 cash $192.01 #225458845 options_level=3
2026-09-14 13:11:05,932 INFO Live account equity $226.36 cash $192.01 #225458845 options_level=3
Live micro: manage/exits only
2026-09-14 13:11:06,147 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-14 13:11:06,206 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (164 earlier lines - see full log file)
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
| Total open lots             |    39 | INFO |
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

## Run 20260914T171657Z

- UTC timestamp: `20260914T171657Z`
- GitHub run: [#9895](https://github.com/28twagg-ops/TradingBot/actions/runs/34873592945)
- Run id: `34873592945`
- Live bot: exit=`0`, duration=`5s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`34s`
- Full logs: `logs/action_runs/20260914T171657Z_live_bot.log`, `logs/action_runs/20260914T171657Z_live_options.log`, `logs/action_runs/20260914T171657Z_options_bot.log`


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
{"ts_et":"2026-09-14T13:17:06.869372-04:00","date":"2026-09-14","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":21.1,"phases_s":{"reconcile":2.56,"cancel":0.24,"manage":7.38,"protective_stops":1.67},"signals":0,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":39,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9895","github_run_id":"34873592945","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
17:17:00  INFO      Mode: exits
17:17:01  INFO        Daily log -> logs/daily/2026-09-14.md
17:17:01  INFO        Daily log reconciled -> logs/daily/2026-09-14.md (2 ledger rows)
17:17:01  INFO        place_all_stops: checking 1 positions...
17:17:01  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
17:17:01  INFO        [positions] 1/1 (1 valid)
17:17:01  INFO        Daily log -> logs/daily/2026-09-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:17 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.32|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +1.2%  $+0.39                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_live_micro LIVE 2026-09-14T13:17:02.835440-04:00 share=25% ===
2026-09-14 13:17:02,835 INFO === options_live_micro LIVE 2026-09-14T13:17:02.835440-04:00 share=25% ===
Live account equity $226.32 cash $192.01 #225458845 options_level=3
2026-09-14 13:17:03,056 INFO Live account equity $226.32 cash $192.01 #225458845 options_level=3
Live micro: manage/exits only
2026-09-14 13:17:03,284 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-14 13:17:03,354 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (164 earlier lines - see full log file)
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
| Total open lots             |    39 | INFO |
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
equity=226.32 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260914T172108Z

- UTC timestamp: `20260914T172108Z`
- GitHub run: [#9896](https://github.com/28twagg-ops/TradingBot/actions/runs/34874101570)
- Run id: `34874101570`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`34s`
- Full logs: `logs/action_runs/20260914T172108Z_live_bot.log`, `logs/action_runs/20260914T172108Z_live_options.log`, `logs/action_runs/20260914T172108Z_options_bot.log`


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
{"ts_et":"2026-09-14T13:21:17.189513-04:00","date":"2026-09-14","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":21.3,"phases_s":{"reconcile":2.62,"cancel":0.24,"manage":7.4,"protective_stops":1.82},"signals":0,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":39,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9896","github_run_id":"34874101570","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
17:21:10  INFO      Mode: exits
17:21:11  INFO        Daily log -> logs/daily/2026-09-14.md
17:21:11  INFO        Daily log reconciled -> logs/daily/2026-09-14.md (2 ledger rows)
17:21:11  INFO        place_all_stops: checking 1 positions...
17:21:11  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
17:21:11  INFO        [positions] 1/1 (1 valid)
17:21:12  INFO        Daily log -> logs/daily/2026-09-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.24|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.9%  $+0.31                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_live_micro LIVE 2026-09-14T13:21:13.009406-04:00 share=25% ===
2026-09-14 13:21:13,009 INFO === options_live_micro LIVE 2026-09-14T13:21:13.009406-04:00 share=25% ===
Live account equity $226.24 cash $192.01 #225458845 options_level=3
2026-09-14 13:21:13,249 INFO Live account equity $226.24 cash $192.01 #225458845 options_level=3
Live micro: manage/exits only
2026-09-14 13:21:13,494 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-14 13:21:13,566 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (164 earlier lines - see full log file)
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
| Total open lots             |    39 | INFO |
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
equity=226.24 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260914T172612Z

- UTC timestamp: `20260914T172612Z`
- GitHub run: [#9897](https://github.com/28twagg-ops/TradingBot/actions/runs/34874612908)
- Run id: `34874612908`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`29s`
- Full logs: `logs/action_runs/20260914T172612Z_live_bot.log`, `logs/action_runs/20260914T172612Z_live_options.log`, `logs/action_runs/20260914T172612Z_options_bot.log`


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
{"ts_et":"2026-09-14T13:26:18.836382-04:00","date":"2026-09-14","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":19.9,"phases_s":{"reconcile":2.52,"cancel":0.19,"manage":6.69,"protective_stops":1.4},"signals":0,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":39,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9897","github_run_id":"34874612908","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
17:26:13  INFO      Mode: exits
17:26:14  INFO        Daily log -> logs/daily/2026-09-14.md
17:26:14  INFO        Daily log reconciled -> logs/daily/2026-09-14.md (2 ledger rows)
17:26:14  INFO        place_all_stops: checking 1 positions...
17:26:14  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
17:26:14  INFO        [positions] 1/1 (1 valid)
17:26:15  INFO        Daily log -> logs/daily/2026-09-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.30|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +1.1%  $+0.38                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_live_micro LIVE 2026-09-14T13:26:15.877358-04:00 share=25% ===
2026-09-14 13:26:15,877 INFO === options_live_micro LIVE 2026-09-14T13:26:15.877358-04:00 share=25% ===
Live account equity $226.31 cash $192.01 #225458845 options_level=3
2026-09-14 13:26:16,070 INFO Live account equity $226.31 cash $192.01 #225458845 options_level=3
Live micro: manage/exits only
2026-09-14 13:26:16,259 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-14 13:26:16,315 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (164 earlier lines - see full log file)
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
| Total open lots             |    39 | INFO |
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
equity=226.31 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260914T173121Z

- UTC timestamp: `20260914T173121Z`
- GitHub run: [#9898](https://github.com/28twagg-ops/TradingBot/actions/runs/34875119899)
- Run id: `34875119899`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`30s`
- Full logs: `logs/action_runs/20260914T173121Z_live_bot.log`, `logs/action_runs/20260914T173121Z_live_options.log`, `logs/action_runs/20260914T173121Z_options_bot.log`


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
{"ts_et":"2026-09-14T13:31:27.616994-04:00","date":"2026-09-14","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":17.4,"phases_s":{"reconcile":2.21,"cancel":0.07,"manage":5.72,"protective_stops":0.58},"signals":0,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":39,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9898","github_run_id":"34875119899","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
17:31:22  INFO      Mode: exits
17:31:23  INFO        Daily log -> logs/daily/2026-09-14.md
17:31:23  INFO        Daily log reconciled -> logs/daily/2026-09-14.md (2 ledger rows)
17:31:23  INFO        place_all_stops: checking 1 positions...
17:31:23  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
17:31:23  INFO        [positions] 1/1 (1 valid)
17:31:23  INFO        Daily log -> logs/daily/2026-09-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.28|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +1.0%  $+0.35                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_live_micro LIVE 2026-09-14T13:31:24.225012-04:00 share=25% ===
2026-09-14 13:31:24,225 INFO === options_live_micro LIVE 2026-09-14T13:31:24.225012-04:00 share=25% ===
Live account equity $226.28 cash $192.01 #225458845 options_level=3
2026-09-14 13:31:24,311 INFO Live account equity $226.28 cash $192.01 #225458845 options_level=3
Live micro: manage/exits only
2026-09-14 13:31:24,420 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-14 13:31:24,443 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (164 earlier lines - see full log file)
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
| Total open lots             |    39 | INFO |
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
equity=226.28 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260914T173603Z

- UTC timestamp: `20260914T173603Z`
- GitHub run: [#9899](https://github.com/28twagg-ops/TradingBot/actions/runs/34875629254)
- Run id: `34875629254`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`29s`
- Full logs: `logs/action_runs/20260914T173603Z_live_bot.log`, `logs/action_runs/20260914T173603Z_live_options.log`, `logs/action_runs/20260914T173603Z_options_bot.log`


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
{"ts_et":"2026-09-14T13:36:09.636874-04:00","date":"2026-09-14","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":17.0,"phases_s":{"reconcile":2.16,"cancel":0.04,"manage":5.31,"protective_stops":0.35},"signals":0,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":39,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9899","github_run_id":"34875629254","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
17:36:05  INFO      Mode: exits
17:36:05  INFO        Daily log -> logs/daily/2026-09-14.md
17:36:05  INFO        Daily log reconciled -> logs/daily/2026-09-14.md (2 ledger rows)
17:36:05  INFO        place_all_stops: checking 1 positions...
17:36:05  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
17:36:05  INFO        [positions] 1/1 (1 valid)
17:36:05  INFO        Daily log -> logs/daily/2026-09-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.30|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +1.1%  $+0.37                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_live_micro LIVE 2026-09-14T13:36:06.522042-04:00 share=25% ===
2026-09-14 13:36:06,522 INFO === options_live_micro LIVE 2026-09-14T13:36:06.522042-04:00 share=25% ===
Live account equity $226.30 cash $192.01 #225458845 options_level=3
2026-09-14 13:36:06,579 INFO Live account equity $226.30 cash $192.01 #225458845 options_level=3
Live micro: manage/exits only
2026-09-14 13:36:06,612 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-14 13:36:06,623 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (164 earlier lines - see full log file)
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
| Total open lots             |    39 | INFO |
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
equity=226.3 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260914T174103Z

- UTC timestamp: `20260914T174103Z`
- GitHub run: [#9900](https://github.com/28twagg-ops/TradingBot/actions/runs/34876131833)
- Run id: `34876131833`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`28s`
- Full logs: `logs/action_runs/20260914T174103Z_live_bot.log`, `logs/action_runs/20260914T174103Z_live_options.log`, `logs/action_runs/20260914T174103Z_options_bot.log`


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
{"ts_et":"2026-09-14T13:41:09.328590-04:00","date":"2026-09-14","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":16.2,"phases_s":{"reconcile":2.12,"cancel":0.04,"manage":5.13,"protective_stops":0.29},"signals":0,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":39,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9900","github_run_id":"34876131833","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
17:41:04  INFO      Mode: exits
17:41:05  INFO        Daily log -> logs/daily/2026-09-14.md
17:41:05  INFO        Daily log reconciled -> logs/daily/2026-09-14.md (2 ledger rows)
17:41:05  INFO        place_all_stops: checking 1 positions...
17:41:05  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
17:41:05  INFO        [positions] 1/1 (1 valid)
17:41:05  INFO        Daily log -> logs/daily/2026-09-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.23|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.9%  $+0.30                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_live_micro LIVE 2026-09-14T13:41:06.221133-04:00 share=25% ===
2026-09-14 13:41:06,221 INFO === options_live_micro LIVE 2026-09-14T13:41:06.221133-04:00 share=25% ===
Live account equity $226.23 cash $192.01 #225458845 options_level=3
2026-09-14 13:41:06,262 INFO Live account equity $226.23 cash $192.01 #225458845 options_level=3
Live micro: manage/exits only
2026-09-14 13:41:06,287 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-14 13:41:06,294 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (164 earlier lines - see full log file)
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
| Total open lots             |    39 | INFO |
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
equity=226.23 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260914T174605Z

- UTC timestamp: `20260914T174605Z`
- GitHub run: [#9901](https://github.com/28twagg-ops/TradingBot/actions/runs/34876628068)
- Run id: `34876628068`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`33s`
- Full logs: `logs/action_runs/20260914T174605Z_live_bot.log`, `logs/action_runs/20260914T174605Z_live_options.log`, `logs/action_runs/20260914T174605Z_options_bot.log`


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
{"ts_et":"2026-09-14T13:46:13.423133-04:00","date":"2026-09-14","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":21.1,"phases_s":{"reconcile":2.58,"cancel":0.22,"manage":7.45,"protective_stops":1.69},"signals":0,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":39,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9901","github_run_id":"34876628068","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
17:46:06  INFO      Mode: exits
17:46:07  INFO        Daily log -> logs/daily/2026-09-14.md
17:46:07  INFO        Daily log reconciled -> logs/daily/2026-09-14.md (2 ledger rows)
17:46:07  INFO        place_all_stops: checking 1 positions...
17:46:07  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
17:46:08  INFO        [positions] 1/1 (1 valid)
17:46:08  INFO        Daily log -> logs/daily/2026-09-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.20|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.8%  $+0.27                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_live_micro LIVE 2026-09-14T13:46:09.722116-04:00 share=25% ===
2026-09-14 13:46:09,722 INFO === options_live_micro LIVE 2026-09-14T13:46:09.722116-04:00 share=25% ===
Live account equity $226.20 cash $192.01 #225458845 options_level=3
2026-09-14 13:46:09,946 INFO Live account equity $226.20 cash $192.01 #225458845 options_level=3
Live micro: manage/exits only
2026-09-14 13:46:10,249 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-14 13:46:10,320 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (164 earlier lines - see full log file)
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
| Total open lots             |    39 | INFO |
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
equity=226.2 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260914T175111Z

- UTC timestamp: `20260914T175111Z`
- GitHub run: [#9902](https://github.com/28twagg-ops/TradingBot/actions/runs/34877117641)
- Run id: `34877117641`
- Live bot: exit=`0`, duration=`5s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`33s`
- Full logs: `logs/action_runs/20260914T175111Z_live_bot.log`, `logs/action_runs/20260914T175111Z_live_options.log`, `logs/action_runs/20260914T175111Z_options_bot.log`


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
{"ts_et":"2026-09-14T13:51:21.345643-04:00","date":"2026-09-14","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":21.3,"phases_s":{"reconcile":2.59,"cancel":0.23,"manage":7.35,"protective_stops":1.82},"signals":0,"placed":0,"equity":1000241.84,"open_positions":8,"pending_orders":0,"open_lots":39,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"9902","github_run_id":"34877117641","status":"ok","data_quality":{"clean":{"n":1204,"win":49.17,"med":-10.1,"avg":40.78,"pnl":15811.82},"tainted":{"n":1829,"win":33.35,"med":-38.81,"avg":11.98,"pnl":-9096.84},"keep_only":{"n":626,"win":63.26,"med":51.39,"avg":64.19,"pnl":10734.45},"keep_only_recent":{"n":429,"win":61.31,"med":53.33,"avg":74.49,"pnl":6089.0},"keep_strategies":["S163","S168","S173","S174","S210","S218","S350","S353","S354","S355","S356","S357","S361","S362","S363","S364","S365","S397","S399","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S164","S202","S203","S207","S211","S212","S216","S217","S351","S352","S360","S366","S398","S405","S407","S408","S411","S412"]}}
```

### Live bot (tail)

```text
17:51:14  INFO      Mode: exits
17:51:15  INFO        Daily log -> logs/daily/2026-09-14.md
17:51:15  INFO        Daily log reconciled -> logs/daily/2026-09-14.md (2 ledger rows)
17:51:15  INFO        place_all_stops: checking 1 positions...
17:51:15  INFO        STOP skipped ALLE: fractional (0.2206 shares) — software exit will handle it
17:51:16  INFO        [positions] 1/1 (1 valid)
17:51:16  INFO        Daily log -> logs/daily/2026-09-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:51 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $226.23|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALLE  P&L +0.9%  $+0.30                                           HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
=== options_live_micro LIVE 2026-09-14T13:51:17.369558-04:00 share=25% ===
2026-09-14 13:51:17,369 INFO === options_live_micro LIVE 2026-09-14T13:51:17.369558-04:00 share=25% ===
Live account equity $226.23 cash $192.01 #225458845 options_level=3
2026-09-14 13:51:17,645 INFO Live account equity $226.23 cash $192.01 #225458845 options_level=3
Live micro: manage/exits only
2026-09-14 13:51:17,874 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-09-14 13:51:17,953 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (164 earlier lines - see full log file)
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
| Total open lots             |    39 | INFO |
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
equity=226.23 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 2 | 100% | +0.56% | +0.56% | +0.17% | 999.00 | 0.0d | $+0.80 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---
