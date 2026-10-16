# Daily Comprehensive Action Review - 2026-10-16

_Auto-generated from GitHub Actions run output. Each run appends a summary; full stdout is in linked per-run log files._
## Run 20261016T130138Z

- UTC timestamp: `20261016T130138Z`
- GitHub run: [#13005](https://github.com/28twagg-ops/TradingBot/actions/runs/38904523387)
- Run id: `38904523387`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`13s`
- Full logs: `logs/action_runs/20261016T130138Z_live_bot.log`, `logs/action_runs/20261016T130138Z_live_options.log`, `logs/action_runs/20261016T130138Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1685 | 48.4 | -25.0 | +37.4 | $+18,645 |
| TAINTED | 2002 | 32.4 | -40.4 | +10.8 | $-10,944 |
| KEEP-only | 826 | 61.0 | +51.0 | +55.4 | $+12,816 |
| KEEP-only recent | 633 | 59.6 | +53.2 | +61.5 | $+8,755 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S410, S411
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-16T09:01:43.721814-04:00","date":"2026-10-16","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.17},"signals":0,"placed":0,"equity":993070.38,"open_positions":5,"pending_orders":0,"open_lots":5,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"13005","github_run_id":"38904523387","status":"ok","data_quality":{"clean":{"n":1685,"win":48.43,"med":-25.0,"avg":37.45,"pnl":18644.83},"tainted":{"n":2002,"win":32.37,"med":-40.35,"avg":10.83,"pnl":-10944.28},"keep_only":{"n":826,"win":61.02,"med":50.96,"avg":55.42,"pnl":12816.45},"keep_only_recent":{"n":633,"win":59.56,"med":53.23,"avg":61.55,"pnl":8755.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:01:39  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.15|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $224.15|
|  Cash                                                           $122.52|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $101.63|
|  Open P&L                                                        $+0.85|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (3 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  APD      Pullback50      $33.64     $296.37  $296.60  +0.1%   $+0.03  |
|  KEY      MomReversal     $33.88     $19.69   $19.87   +0.9%   $+0.31  |
|  PNC      MomReversal     $34.11     $211.72  $214.94  +1.5%   $+0.51  |
|                                                                        |
|  Total invested                                                 $101.63|
|  Total open P&L                                                  $+0.85|
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
|  2026-10-15  SELL  APD  Pullback50  $33.60  P&L $-0.01                 |
|  2026-10-15  SELL  GS  MomReversal  $33.10  P&L $-0.47                 |
|  2026-10-14  SELL  APD  Pullback50  $33.53  P&L $-0.03                 |
|  2026-10-14  SELL  BBY  Pullback50  $33.44  P&L $-0.22                 |
|  2026-10-14  SELL  AMZN  Pullback50  $33.53  P&L $-0.13                |
|  2026-10-14  SELL  GS  MomReversal  $33.49  P&L $-0.17                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-16T09:01:40.919806-04:00 share=25% ===
2026-10-16 09:01:40,919 INFO === options_live_micro LIVE 2026-10-16T09:01:40.919806-04:00 share=25% ===
Live account equity $224.15 cash $122.52 #225458845 options_level=3
2026-10-16 09:01:40,976 INFO Live account equity $224.15 cash $122.52 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-10-16 09:01:40,988 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-10-16 09:01:41,000 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (186 earlier lines - see full log file)
| S168 | 248 | 26 |
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
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-16
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |  1914 | WARN | <<<
| Missing exit records (post) |  1913 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     5 | INFO |
| Total closed lots           |  2798 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-16_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-16_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1685 med=-25.0% | TAINTED n=2002 med=-40.4% | KEEP-only n=826 med=+51.0% | KILL=21 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.15 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261016T130641Z

- UTC timestamp: `20261016T130641Z`
- GitHub run: [#13006](https://github.com/28twagg-ops/TradingBot/actions/runs/38905148450)
- Run id: `38905148450`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`14s`
- Full logs: `logs/action_runs/20261016T130641Z_live_bot.log`, `logs/action_runs/20261016T130641Z_live_options.log`, `logs/action_runs/20261016T130641Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1685 | 48.4 | -25.0 | +37.4 | $+18,645 |
| TAINTED | 2002 | 32.4 | -40.4 | +10.8 | $-10,944 |
| KEEP-only | 826 | 61.0 | +51.0 | +55.4 | $+12,816 |
| KEEP-only recent | 633 | 59.6 | +53.2 | +61.5 | $+8,755 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S410, S411
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-16T09:06:47.344100-04:00","date":"2026-10-16","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.3,"phases_s":{"reconcile":0.46},"signals":0,"placed":0,"equity":993081.96,"open_positions":5,"pending_orders":0,"open_lots":5,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"13006","github_run_id":"38905148450","status":"ok","data_quality":{"clean":{"n":1685,"win":48.43,"med":-25.0,"avg":37.45,"pnl":18644.83},"tainted":{"n":2002,"win":32.37,"med":-40.35,"avg":10.83,"pnl":-10944.28},"keep_only":{"n":826,"win":61.02,"med":50.96,"avg":55.42,"pnl":12816.45},"keep_only_recent":{"n":633,"win":59.56,"med":53.23,"avg":61.55,"pnl":8755.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:06:42  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.15|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $224.15|
|  Cash                                                           $122.52|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $101.63|
|  Open P&L                                                        $+0.85|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (3 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  APD      Pullback50      $33.64     $296.37  $296.60  +0.1%   $+0.03  |
|  KEY      MomReversal     $33.88     $19.69   $19.87   +0.9%   $+0.31  |
|  PNC      MomReversal     $34.11     $211.72  $214.94  +1.5%   $+0.51  |
|                                                                        |
|  Total invested                                                 $101.63|
|  Total open P&L                                                  $+0.85|
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
|  2026-10-15  SELL  APD  Pullback50  $33.60  P&L $-0.01                 |
|  2026-10-15  SELL  GS  MomReversal  $33.10  P&L $-0.47                 |
|  2026-10-14  SELL  APD  Pullback50  $33.53  P&L $-0.03                 |
|  2026-10-14  SELL  BBY  Pullback50  $33.44  P&L $-0.22                 |
|  2026-10-14  SELL  AMZN  Pullback50  $33.53  P&L $-0.13                |
|  2026-10-14  SELL  GS  MomReversal  $33.49  P&L $-0.17                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-16T09:06:44.286800-04:00 share=25% ===
2026-10-16 09:06:44,286 INFO === options_live_micro LIVE 2026-10-16T09:06:44.286800-04:00 share=25% ===
Live account equity $224.15 cash $122.52 #225458845 options_level=3
2026-10-16 09:06:44,474 INFO Live account equity $224.15 cash $122.52 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-10-16 09:06:44,527 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-10-16 09:06:44,578 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (186 earlier lines - see full log file)
| S168 | 248 | 26 |
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
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-16
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |  1914 | WARN | <<<
| Missing exit records (post) |  1913 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     5 | INFO |
| Total closed lots           |  2798 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-16_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-16_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1685 med=-25.0% | TAINTED n=2002 med=-40.4% | KEEP-only n=826 med=+51.0% | KILL=21 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.15 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261016T131131Z

- UTC timestamp: `20261016T131131Z`
- GitHub run: [#13007](https://github.com/28twagg-ops/TradingBot/actions/runs/38905773101)
- Run id: `38905773101`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`9s`
- Full logs: `logs/action_runs/20261016T131131Z_live_bot.log`, `logs/action_runs/20261016T131131Z_live_options.log`, `logs/action_runs/20261016T131131Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1685 | 48.4 | -25.0 | +37.4 | $+18,645 |
| TAINTED | 2002 | 32.4 | -40.4 | +10.8 | $-10,944 |
| KEEP-only | 826 | 61.0 | +51.0 | +55.4 | $+12,816 |
| KEEP-only recent | 633 | 59.6 | +53.2 | +61.5 | $+8,755 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S410, S411
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-16T09:11:35.989033-04:00","date":"2026-10-16","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.8,"phases_s":{"reconcile":0.31},"signals":0,"placed":0,"equity":993156.45,"open_positions":5,"pending_orders":0,"open_lots":5,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"13007","github_run_id":"38905773101","status":"ok","data_quality":{"clean":{"n":1685,"win":48.43,"med":-25.0,"avg":37.45,"pnl":18644.83},"tainted":{"n":2002,"win":32.37,"med":-40.35,"avg":10.83,"pnl":-10944.28},"keep_only":{"n":826,"win":61.02,"med":50.96,"avg":55.42,"pnl":12816.45},"keep_only_recent":{"n":633,"win":59.56,"med":53.23,"avg":61.55,"pnl":8755.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:11:32  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.20|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $224.20|
|  Cash                                                           $122.52|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $101.68|
|  Open P&L                                                        $+0.90|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (3 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  APD      Pullback50      $33.64     $296.37  $296.60  +0.1%   $+0.03  |
|  KEY      MomReversal     $33.93     $19.69   $19.90   +1.1%   $+0.36  |
|  PNC      MomReversal     $34.11     $211.72  $214.94  +1.5%   $+0.51  |
|                                                                        |
|  Total invested                                                 $101.68|
|  Total open P&L                                                  $+0.90|
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
|  2026-10-15  SELL  APD  Pullback50  $33.60  P&L $-0.01                 |
|  2026-10-15  SELL  GS  MomReversal  $33.10  P&L $-0.47                 |
|  2026-10-14  SELL  APD  Pullback50  $33.53  P&L $-0.03                 |
|  2026-10-14  SELL  BBY  Pullback50  $33.44  P&L $-0.22                 |
|  2026-10-14  SELL  AMZN  Pullback50  $33.53  P&L $-0.13                |
|  2026-10-14  SELL  GS  MomReversal  $33.49  P&L $-0.17                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-16T09:11:33.355145-04:00 share=25% ===
2026-10-16 09:11:33,355 INFO === options_live_micro LIVE 2026-10-16T09:11:33.355145-04:00 share=25% ===
Live account equity $224.20 cash $122.52 #225458845 options_level=3
2026-10-16 09:11:33,494 INFO Live account equity $224.20 cash $122.52 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-10-16 09:11:33,533 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-10-16 09:11:33,572 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (186 earlier lines - see full log file)
| S168 | 248 | 26 |
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
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-16
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |  1914 | WARN | <<<
| Missing exit records (post) |  1913 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     5 | INFO |
| Total closed lots           |  2798 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-16_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-16_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1685 med=-25.0% | TAINTED n=2002 med=-40.4% | KEEP-only n=826 med=+51.0% | KILL=21 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.2 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261016T131643Z

- UTC timestamp: `20261016T131643Z`
- GitHub run: [#13008](https://github.com/28twagg-ops/TradingBot/actions/runs/38906406798)
- Run id: `38906406798`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`12s`
- Full logs: `logs/action_runs/20261016T131643Z_live_bot.log`, `logs/action_runs/20261016T131643Z_live_options.log`, `logs/action_runs/20261016T131643Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1685 | 48.4 | -25.0 | +37.4 | $+18,645 |
| TAINTED | 2002 | 32.4 | -40.4 | +10.8 | $-10,944 |
| KEEP-only | 826 | 61.0 | +51.0 | +55.4 | $+12,816 |
| KEEP-only recent | 633 | 59.6 | +53.2 | +61.5 | $+8,755 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S410, S411
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-16T09:16:48.423348-04:00","date":"2026-10-16","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.8,"phases_s":{"reconcile":0.1},"signals":0,"placed":0,"equity":993146.44,"open_positions":5,"pending_orders":0,"open_lots":5,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"13008","github_run_id":"38906406798","status":"ok","data_quality":{"clean":{"n":1685,"win":48.43,"med":-25.0,"avg":37.45,"pnl":18644.83},"tainted":{"n":2002,"win":32.37,"med":-40.35,"avg":10.83,"pnl":-10944.28},"keep_only":{"n":826,"win":61.02,"med":50.96,"avg":55.42,"pnl":12816.45},"keep_only_recent":{"n":633,"win":59.56,"med":53.23,"avg":61.55,"pnl":8755.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:16:44  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.20|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $224.20|
|  Cash                                                           $122.52|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $101.68|
|  Open P&L                                                        $+0.90|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (3 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  APD      Pullback50      $33.64     $296.37  $296.60  +0.1%   $+0.03  |
|  KEY      MomReversal     $33.93     $19.69   $19.90   +1.1%   $+0.36  |
|  PNC      MomReversal     $34.11     $211.72  $214.94  +1.5%   $+0.51  |
|                                                                        |
|  Total invested                                                 $101.68|
|  Total open P&L                                                  $+0.90|
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
|  2026-10-15  SELL  APD  Pullback50  $33.60  P&L $-0.01                 |
|  2026-10-15  SELL  GS  MomReversal  $33.10  P&L $-0.47                 |
|  2026-10-14  SELL  APD  Pullback50  $33.53  P&L $-0.03                 |
|  2026-10-14  SELL  BBY  Pullback50  $33.44  P&L $-0.22                 |
|  2026-10-14  SELL  AMZN  Pullback50  $33.53  P&L $-0.13                |
|  2026-10-14  SELL  GS  MomReversal  $33.49  P&L $-0.17                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-16T09:16:45.897583-04:00 share=25% ===
2026-10-16 09:16:45,897 INFO === options_live_micro LIVE 2026-10-16T09:16:45.897583-04:00 share=25% ===
Live account equity $224.20 cash $122.52 #225458845 options_level=3
2026-10-16 09:16:45,942 INFO Live account equity $224.20 cash $122.52 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-10-16 09:16:45,951 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-10-16 09:16:45,960 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (186 earlier lines - see full log file)
| S168 | 248 | 26 |
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
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-16
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |  1914 | WARN | <<<
| Missing exit records (post) |  1913 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     5 | INFO |
| Total closed lots           |  2798 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-16_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-16_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1685 med=-25.0% | TAINTED n=2002 med=-40.4% | KEEP-only n=826 med=+51.0% | KILL=21 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.2 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261016T132138Z

- UTC timestamp: `20261016T132138Z`
- GitHub run: [#13009](https://github.com/28twagg-ops/TradingBot/actions/runs/38907038382)
- Run id: `38907038382`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`12s`
- Full logs: `logs/action_runs/20261016T132138Z_live_bot.log`, `logs/action_runs/20261016T132138Z_live_options.log`, `logs/action_runs/20261016T132138Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1685 | 48.4 | -25.0 | +37.4 | $+18,645 |
| TAINTED | 2002 | 32.4 | -40.4 | +10.8 | $-10,944 |
| KEEP-only | 826 | 61.0 | +51.0 | +55.4 | $+12,816 |
| KEEP-only recent | 633 | 59.6 | +53.2 | +61.5 | $+8,755 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S410, S411
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-16T09:21:44.873886-04:00","date":"2026-10-16","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.2,"phases_s":{"reconcile":0.44},"signals":0,"placed":0,"equity":993188.29,"open_positions":5,"pending_orders":0,"open_lots":5,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"13009","github_run_id":"38907038382","status":"ok","data_quality":{"clean":{"n":1685,"win":48.43,"med":-25.0,"avg":37.45,"pnl":18644.83},"tainted":{"n":2002,"win":32.37,"med":-40.35,"avg":10.83,"pnl":-10944.28},"keep_only":{"n":826,"win":61.02,"med":50.96,"avg":55.42,"pnl":12816.45},"keep_only_recent":{"n":633,"win":59.56,"med":53.23,"avg":61.55,"pnl":8755.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:21:39  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.20|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $224.20|
|  Cash                                                           $122.52|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $101.68|
|  Open P&L                                                        $+0.90|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (3 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  APD      Pullback50      $33.64     $296.37  $296.60  +0.1%   $+0.03  |
|  KEY      MomReversal     $33.93     $19.69   $19.90   +1.1%   $+0.36  |
|  PNC      MomReversal     $34.11     $211.72  $214.94  +1.5%   $+0.51  |
|                                                                        |
|  Total invested                                                 $101.68|
|  Total open P&L                                                  $+0.90|
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
|  2026-10-15  SELL  APD  Pullback50  $33.60  P&L $-0.01                 |
|  2026-10-15  SELL  GS  MomReversal  $33.10  P&L $-0.47                 |
|  2026-10-14  SELL  APD  Pullback50  $33.53  P&L $-0.03                 |
|  2026-10-14  SELL  BBY  Pullback50  $33.44  P&L $-0.22                 |
|  2026-10-14  SELL  AMZN  Pullback50  $33.53  P&L $-0.13                |
|  2026-10-14  SELL  GS  MomReversal  $33.49  P&L $-0.17                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-16T09:21:41.657451-04:00 share=25% ===
2026-10-16 09:21:41,657 INFO === options_live_micro LIVE 2026-10-16T09:21:41.657451-04:00 share=25% ===
Live account equity $224.20 cash $122.52 #225458845 options_level=3
2026-10-16 09:21:41,865 INFO Live account equity $224.20 cash $122.52 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-10-16 09:21:41,925 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-10-16 09:21:41,983 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (186 earlier lines - see full log file)
| S168 | 248 | 26 |
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
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-16
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |  1914 | WARN | <<<
| Missing exit records (post) |  1913 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     5 | INFO |
| Total closed lots           |  2798 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-16_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-16_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1685 med=-25.0% | TAINTED n=2002 med=-40.4% | KEEP-only n=826 med=+51.0% | KILL=21 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.2 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261016T132631Z

- UTC timestamp: `20261016T132631Z`
- GitHub run: [#13010](https://github.com/28twagg-ops/TradingBot/actions/runs/38907671014)
- Run id: `38907671014`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`11s`
- Full logs: `logs/action_runs/20261016T132631Z_live_bot.log`, `logs/action_runs/20261016T132631Z_live_options.log`, `logs/action_runs/20261016T132631Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1685 | 48.4 | -25.0 | +37.4 | $+18,645 |
| TAINTED | 2002 | 32.4 | -40.4 | +10.8 | $-10,944 |
| KEEP-only | 826 | 61.0 | +51.0 | +55.4 | $+12,816 |
| KEEP-only recent | 633 | 59.6 | +53.2 | +61.5 | $+8,755 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S410, S411
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-16T09:26:36.454811-04:00","date":"2026-10-16","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.1,"phases_s":{"reconcile":0.44},"signals":0,"placed":0,"equity":993110.45,"open_positions":5,"pending_orders":0,"open_lots":5,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"13010","github_run_id":"38907671014","status":"ok","data_quality":{"clean":{"n":1685,"win":48.43,"med":-25.0,"avg":37.45,"pnl":18644.83},"tainted":{"n":2002,"win":32.37,"med":-40.35,"avg":10.83,"pnl":-10944.28},"keep_only":{"n":826,"win":61.02,"med":50.96,"avg":55.42,"pnl":12816.45},"keep_only_recent":{"n":633,"win":59.56,"med":53.23,"avg":61.55,"pnl":8755.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:26:32  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $224.20|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $224.20|
|  Cash                                                           $122.52|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $101.68|
|  Open P&L                                                        $+0.90|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (3 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  APD      Pullback50      $33.64     $296.37  $296.60  +0.1%   $+0.03  |
|  KEY      MomReversal     $33.93     $19.69   $19.90   +1.1%   $+0.36  |
|  PNC      MomReversal     $34.11     $211.72  $214.94  +1.5%   $+0.51  |
|                                                                        |
|  Total invested                                                 $101.68|
|  Total open P&L                                                  $+0.90|
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
|  2026-10-15  SELL  APD  Pullback50  $33.60  P&L $-0.01                 |
|  2026-10-15  SELL  GS  MomReversal  $33.10  P&L $-0.47                 |
|  2026-10-14  SELL  APD  Pullback50  $33.53  P&L $-0.03                 |
|  2026-10-14  SELL  BBY  Pullback50  $33.44  P&L $-0.22                 |
|  2026-10-14  SELL  AMZN  Pullback50  $33.53  P&L $-0.13                |
|  2026-10-14  SELL  GS  MomReversal  $33.49  P&L $-0.17                 |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-16T09:26:33.782544-04:00 share=25% ===
2026-10-16 09:26:33,782 INFO === options_live_micro LIVE 2026-10-16T09:26:33.782544-04:00 share=25% ===
Live account equity $224.20 cash $122.52 #225458845 options_level=3
2026-10-16 09:26:33,978 INFO Live account equity $224.20 cash $122.52 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-10-16 09:26:34,039 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-10-16 09:26:34,096 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (186 earlier lines - see full log file)
| S168 | 248 | 26 |
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
| 2026-10-15 |    2 |    2 |    0 |    2 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     7 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-10-16
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |  1914 | WARN | <<<
| Missing exit records (post) |  1913 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     5 | INFO |
| Total closed lots           |  2798 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-16_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-10-16_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1685 med=-25.0% | TAINTED n=2002 med=-40.4% | KEEP-only n=826 med=+51.0% | KILL=21 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=224.2 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 3 | 100% | +0.80% | +1.05% | +0.27% | 999.00 | 0.0d | $+1.23 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261016T133133Z

- UTC timestamp: `20261016T133133Z`
- GitHub run: [#13011](https://github.com/28twagg-ops/TradingBot/actions/runs/38908310971)
- Run id: `38908310971`
- Live bot: exit=`0`, duration=`217s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20261016T133133Z_live_bot.log`, `logs/action_runs/20261016T133133Z_live_options.log`, `logs/action_runs/20261016T133133Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1685 | 48.4 | -25.0 | +37.4 | $+18,645 |
| TAINTED | 2002 | 32.4 | -40.4 | +10.8 | $-10,944 |
| KEEP-only | 826 | 61.0 | +51.0 | +55.4 | $+12,816 |
| KEEP-only recent | 633 | 59.6 | +53.2 | +61.5 | $+8,755 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S410, S411
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-16T09:26:36.454811-04:00","date":"2026-10-16","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.1,"phases_s":{"reconcile":0.44},"signals":0,"placed":0,"equity":993110.45,"open_positions":5,"pending_orders":0,"open_lots":5,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"13010","github_run_id":"38907671014","status":"ok","data_quality":{"clean":{"n":1685,"win":48.43,"med":-25.0,"avg":37.45,"pnl":18644.83},"tainted":{"n":2002,"win":32.37,"med":-40.35,"avg":10.83,"pnl":-10944.28},"keep_only":{"n":826,"win":61.02,"med":50.96,"avg":55.42,"pnl":12816.45},"keep_only_recent":{"n":633,"win":59.56,"med":53.23,"avg":61.55,"pnl":8755.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:31:34  INFO      Mode: morning_prep
13:31:35  INFO        [prep_positions] 3/3 (3 valid)
13:31:35  INFO      Fetching tickers (universe=both)...
13:31:35  INFO        S&P 500: 503
13:31:35  INFO        MidCap 400: 400
13:31:35  INFO        Total: 903 tickers
13:31:36  INFO        [prep_universe] 40/900 (40 valid)
13:31:38  INFO        [prep_universe] 80/900 (80 valid)
13:31:40  INFO        [prep_universe] 120/900 (120 valid)
13:31:43  INFO        [prep_universe] 160/900 (160 valid)
13:31:45  INFO        [prep_universe] 200/900 (199 valid)
13:31:50  INFO        [prep_universe] 240/900 (238 valid)
13:32:01  INFO        [prep_universe] 280/900 (278 valid)
13:32:12  INFO        [prep_universe] 320/900 (318 valid)
13:32:25  INFO        [prep_universe] 360/900 (358 valid)
13:32:36  INFO        [prep_universe] 400/900 (398 valid)
13:32:49  INFO        [prep_universe] 440/900 (438 valid)
13:33:02  INFO        [prep_universe] 480/900 (477 valid)
13:33:12  INFO        [prep_universe] 520/900 (517 valid)
13:33:26  INFO        [prep_universe] 560/900 (557 valid)
13:33:36  INFO        [prep_universe] 600/900 (597 valid)
13:33:50  INFO        [prep_universe] 640/900 (637 valid)
13:34:00  INFO        [prep_universe] 680/900 (677 valid)
13:34:13  INFO        [prep_universe] 720/900 (717 valid)
13:34:24  INFO        [prep_universe] 760/900 (757 valid)
13:34:38  INFO        [prep_universe] 800/900 (797 valid)
13:34:48  INFO        [prep_universe] 840/900 (837 valid)
13:35:01  INFO        [prep_universe] 880/900 (877 valid)
13:35:08  INFO        [prep_universe] 900/900 (897 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $225.30|
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
|  Invested                                                       $102.78|
|  Open P&L                                                        $+1.99|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  APD      Pullback50      $33.74     $296.37  $297.50  +0.4%   $+0.13  |
|  KEY      MomReversal     $34.39     $19.69   $20.17   +2.4%   $+0.82  |
|  PNC      MomReversal     $34.64     $211.72  $218.29  +3.1%   $+1.04  |
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
|  Signal candidates                                                   41|
|  Universe scanned                                                   900|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-10-16T09:35:10.631737-04:00 share=25% ===
2026-10-16 09:35:10,631 INFO === options_live_micro LIVE 2026-10-16T09:35:10.631737-04:00 share=25% ===
Live account equity $225.36 cash $122.52 #225458845 options_level=3
2026-10-16 09:35:10,843 INFO Live account equity $225.36 cash $122.52 #225458845 options_level=3
Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
2026-10-16 09:35:11,036 INFO Live micro: new entries paused (LIVE_OPTIONS_ENTRIES=0); manage/orphans only
Live micro done. open_options=0 lots=0
2026-10-16 09:35:11,155 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text

```

---

## Run 20261016T134250Z

- UTC timestamp: `20261016T134250Z`
- GitHub run: [#13013](https://github.com/28twagg-ops/TradingBot/actions/runs/38909609607)
- Run id: `38909609607`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20261016T134250Z_live_bot.log`, `logs/action_runs/20261016T134250Z_live_options.log`, `logs/action_runs/20261016T134250Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1685 | 48.4 | -25.0 | +37.4 | $+18,645 |
| TAINTED | 2002 | 32.4 | -40.4 | +10.8 | $-10,944 |
| KEEP-only | 826 | 61.0 | +51.0 | +55.4 | $+12,816 |
| KEEP-only recent | 633 | 59.6 | +53.2 | +61.5 | $+8,755 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S410, S411
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-16T09:26:36.454811-04:00","date":"2026-10-16","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.1,"phases_s":{"reconcile":0.44},"signals":0,"placed":0,"equity":993110.45,"open_positions":5,"pending_orders":0,"open_lots":5,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"13010","github_run_id":"38907671014","status":"ok","data_quality":{"clean":{"n":1685,"win":48.43,"med":-25.0,"avg":37.45,"pnl":18644.83},"tainted":{"n":2002,"win":32.37,"med":-40.35,"avg":10.83,"pnl":-10944.28},"keep_only":{"n":826,"win":61.02,"med":50.96,"avg":55.42,"pnl":12816.45},"keep_only_recent":{"n":633,"win":59.56,"med":53.23,"avg":61.55,"pnl":8755.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:42:51  INFO      Mode: morning_prep
13:42:51  INFO        [prep_positions] 3/3 (3 valid)
13:42:51  INFO        Universe cache hit: 903 tickers (tickers_2026-10-16.json)
13:42:52  INFO        [prep_universe] 40/900 (40 valid)
13:42:54  INFO        [prep_universe] 80/900 (80 valid)
13:42:55  INFO        [prep_universe] 120/900 (120 valid)
13:42:56  INFO        [prep_universe] 160/900 (160 valid)
13:42:57  INFO        [prep_universe] 200/900 (199 valid)
13:43:04  INFO        [prep_universe] 240/900 (238 valid)
13:43:18  INFO        [prep_universe] 280/900 (278 valid)
13:43:30  INFO        [prep_universe] 320/900 (318 valid)
13:43:40  INFO        [prep_universe] 360/900 (358 valid)
13:43:53  INFO        [prep_universe] 400/900 (398 valid)
13:44:06  INFO        [prep_universe] 440/900 (438 valid)
13:44:16  INFO        [prep_universe] 480/900 (477 valid)
13:44:29  INFO        [prep_universe] 520/900 (517 valid)
13:44:42  INFO        [prep_universe] 560/900 (557 valid)
13:44:55  INFO        [prep_universe] 600/900 (597 valid)
13:45:05  INFO        [prep_universe] 640/900 (637 valid)
13:45:18  INFO        [prep_universe] 680/900 (677 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20261016T134716Z

- UTC timestamp: `20261016T134716Z`
- GitHub run: [#13014](https://github.com/28twagg-ops/TradingBot/actions/runs/38910267042)
- Run id: `38910267042`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20261016T134716Z_live_bot.log`, `logs/action_runs/20261016T134716Z_live_options.log`, `logs/action_runs/20261016T134716Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1685 | 48.4 | -25.0 | +37.4 | $+18,645 |
| TAINTED | 2002 | 32.4 | -40.4 | +10.8 | $-10,944 |
| KEEP-only | 826 | 61.0 | +51.0 | +55.4 | $+12,816 |
| KEEP-only recent | 633 | 59.6 | +53.2 | +61.5 | $+8,755 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S410, S411
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-16T09:26:36.454811-04:00","date":"2026-10-16","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.1,"phases_s":{"reconcile":0.44},"signals":0,"placed":0,"equity":993110.45,"open_positions":5,"pending_orders":0,"open_lots":5,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"13010","github_run_id":"38907671014","status":"ok","data_quality":{"clean":{"n":1685,"win":48.43,"med":-25.0,"avg":37.45,"pnl":18644.83},"tainted":{"n":2002,"win":32.37,"med":-40.35,"avg":10.83,"pnl":-10944.28},"keep_only":{"n":826,"win":61.02,"med":50.96,"avg":55.42,"pnl":12816.45},"keep_only_recent":{"n":633,"win":59.56,"med":53.23,"avg":61.55,"pnl":8755.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:47:17  INFO      Mode: morning_scan
13:47:18  INFO        [positions] 3/3 (3 valid)
13:47:18  INFO        SELL LIMIT APD  qty=0.113419381  limit=$298.75  id=b24db126-0baf-4099-bfd0-9738ed14fd96
13:47:48  INFO        SELL LIMIT filled APD (confirmed by position check)
13:47:48  INFO        TX logged: SELL APD  P&L 1.0%
13:47:48  INFO        SELL LIMIT KEY  qty=1.705099553  limit=$20.30  id=647f1dbb-bc81-4940-980a-5f92ac74f18b
13:48:18  INFO        SELL LIMIT filled KEY (confirmed by position check)
13:48:18  INFO        TX logged: SELL KEY  P&L 3.31%
13:48:18  INFO        Universe cache hit: 903 tickers (tickers_2026-10-16.json)
13:48:19  INFO        [universe] 40/902 (40 valid)
13:48:20  INFO        [universe] 80/902 (80 valid)
13:48:21  INFO        [universe] 120/902 (120 valid)
13:48:22  INFO        [universe] 160/902 (160 valid)
13:48:23  INFO        [universe] 200/902 (199 valid)
13:48:33  INFO        [universe] 240/902 (238 valid)
13:48:43  INFO        [universe] 280/902 (278 valid)
13:48:56  INFO        [universe] 320/902 (318 valid)
13:49:09  INFO        [universe] 360/902 (358 valid)
13:49:19  INFO        [universe] 400/902 (398 valid)
13:49:32  INFO        [universe] 440/902 (438 valid)
13:49:45  INFO        [universe] 480/902 (477 valid)
13:49:54  INFO        [universe] 520/902 (517 valid)
13:50:07  INFO        [universe] 560/902 (557 valid)
13:50:20  INFO        [universe] 600/902 (597 valid)
13:50:30  INFO        [universe] 640/902 (637 valid)
13:50:43  INFO        [universe] 680/902 (677 valid)
13:50:56  INFO        [universe] 720/902 (717 valid)
13:51:06  INFO        [universe] 760/902 (757 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---

## Run 20261016T135311Z

- UTC timestamp: `20261016T135311Z`
- GitHub run: [#13015](https://github.com/28twagg-ops/TradingBot/actions/runs/38910916541)
- Run id: `38910916541`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20261016T135311Z_live_bot.log`, `logs/action_runs/20261016T135311Z_live_options.log`, `logs/action_runs/20261016T135311Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1685 | 48.4 | -25.0 | +37.4 | $+18,645 |
| TAINTED | 2002 | 32.4 | -40.4 | +10.8 | $-10,944 |
| KEEP-only | 826 | 61.0 | +51.0 | +55.4 | $+12,816 |
| KEEP-only recent | 633 | 59.6 | +53.2 | +61.5 | $+8,755 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S397, S398, S403, S404, S406, S410, S411
- KILL strategies (21): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S399, S401, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-10-16T09:26:36.454811-04:00","date":"2026-10-16","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.1,"phases_s":{"reconcile":0.44},"signals":0,"placed":0,"equity":993110.45,"open_positions":5,"pending_orders":0,"open_lots":5,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"13010","github_run_id":"38907671014","status":"ok","data_quality":{"clean":{"n":1685,"win":48.43,"med":-25.0,"avg":37.45,"pnl":18644.83},"tainted":{"n":2002,"win":32.37,"med":-40.35,"avg":10.83,"pnl":-10944.28},"keep_only":{"n":826,"win":61.02,"med":50.96,"avg":55.42,"pnl":12816.45},"keep_only_recent":{"n":633,"win":59.56,"med":53.23,"avg":61.55,"pnl":8755.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S397","S398","S403","S404","S406","S410","S411"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S399","S401","S405","S407","S408"]}}
```

### Live bot (tail)

```text
13:53:12  INFO      Mode: morning_scan
13:53:13  INFO        [positions] 1/1 (1 valid)
13:53:13  INFO        Universe cache hit: 903 tickers (tickers_2026-10-16.json)
13:53:14  INFO        [universe] 40/902 (40 valid)
13:53:15  INFO        [universe] 80/902 (80 valid)
13:53:17  INFO        [universe] 120/902 (120 valid)
13:53:18  INFO        [universe] 160/902 (160 valid)
13:53:20  INFO        [universe] 200/902 (199 valid)
13:53:27  INFO        [universe] 240/902 (238 valid)
13:53:40  INFO        [universe] 280/902 (278 valid)
13:53:50  INFO        [universe] 320/902 (318 valid)
13:54:03  INFO        [universe] 360/902 (358 valid)
13:54:16  INFO        [universe] 400/902 (398 valid)
13:54:26  INFO        [universe] 440/902 (438 valid)
13:54:39  INFO        [universe] 480/902 (477 valid)
13:54:52  INFO        [universe] 520/902 (517 valid)
13:55:02  INFO        [universe] 560/902 (557 valid)
13:55:15  INFO        [universe] 600/902 (597 valid)
13:55:28  INFO        [universe] 640/902 (637 valid)
```

### Live options micro (tail)

```text

```

### Paper options bot (tail)

```text

```

---
