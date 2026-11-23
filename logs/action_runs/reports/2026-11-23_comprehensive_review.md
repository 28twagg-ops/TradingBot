# Daily Comprehensive Action Review - 2026-11-23

_Auto-generated from GitHub Actions run output. Each run appends a summary; full stdout is in linked per-run log files._
## Run 20261123T140206Z

- UTC timestamp: `20261123T140206Z`
- GitHub run: [#16432](https://github.com/28twagg-ops/TradingBot/actions/runs/45189518591)
- Run id: `45189518591`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`14s`
- Full logs: `logs/action_runs/20261123T140206Z_live_bot.log`, `logs/action_runs/20261123T140206Z_live_options.log`, `logs/action_runs/20261123T140206Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1896 | 48.5 | -26.4 | +35.0 | $+20,954 |
| TAINTED | 2169 | 30.0 | -43.1 | +6.2 | $-14,707 |
| KEEP-only | 960 | 59.7 | +51.2 | +49.7 | $+14,884 |
| KEEP-only recent | 775 | 58.6 | +52.8 | +54.3 | $+11,375 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S396, S397, S403, S404, S406, S410, S430
- KILL strategies (23): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408, S432
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-11-23T09:02:12.206616-05:00","date":"2026-11-23","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.2,"phases_s":{"reconcile":0.51},"signals":0,"placed":0,"equity":991177.67,"open_positions":1,"pending_orders":0,"open_lots":1,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"16432","github_run_id":"45189518591","status":"ok","data_quality":{"clean":{"n":1896,"win":48.47,"med":-26.45,"avg":34.98,"pnl":20953.83},"tainted":{"n":2169,"win":29.97,"med":-43.14,"avg":6.23,"pnl":-14707.28},"keep_only":{"n":960,"win":59.69,"med":51.22,"avg":49.65,"pnl":14884.45},"keep_only_recent":{"n":775,"win":58.58,"med":52.83,"avg":54.29,"pnl":11375.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S396","S397","S403","S404","S406","S410","S430"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408","S432"]}}
```

### Live bot (tail)

```text
14:02:07  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         14:02 UTC|
|  Regime                                                      CORRECTION|
|  Universe                                                          both|
|  Equity                                                         $231.54|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $231.54|
|  Cash                                                           $126.33|
|  Regime                                                      CORRECTION|
|  Universe                                                          both|
|  Total invested                                                 $105.21|
|  Open P&L                                                        $+1.47|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (3 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ACN      Pullback50      $35.16     $221.78  $225.58  +1.7%   $+0.59  |
|  EOG      Pullback50      $34.30     $149.91  $147.78  -1.4%   $-0.50  |
|  TTWO     EarningsDrift   $35.76     $210.02  $218.40  +4.0%   $+1.37  |
|                                                                        |
|  Total invested                                                 $105.21|
|  Total open P&L                                                  $+1.47|
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
|  2026-11-20  SELL  COP  Pullback50  $34.36  P&L $-0.21                 |
|  2026-11-20  SELL  ACN  Pullback50  $34.26  P&L $-0.25                 |
|  2026-11-20  SELL  TTWO  EarningsDrift  $34.60  P&L $+0.10             |
|  2026-11-20  SELL  EOG  Pullback50  $34.38  P&L $-0.19                 |
|  2026-11-20  SELL  ARES  Pullback50  $34.30  P&L $-0.27                |
|  2026-11-20  SELL  EXPD  Pullback50  $70.24  P&L $+1.64                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-11-23T09:02:09.256979-05:00 share=25% ===
2026-11-23 09:02:09,257 INFO === options_live_micro LIVE 2026-11-23T09:02:09.256979-05:00 share=25% ===
Live account equity $231.53 cash $126.33 #225458845 options_level=3
2026-11-23 09:02:09,445 INFO Live account equity $231.53 cash $126.33 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-11-23 09:02:09,503 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-11-23 09:02:09,561 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (220 earlier lines - see full log file)
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
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-27 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-28 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-29 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-30 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-02 |    2 |    0 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-11-03 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-04 |    2 |    2 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-05 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-06 |    1 |    1 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-09 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-11-10 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-12 |    0 |    4 |    0 |    2 |    4 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-11-13 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-16 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-17 |    1 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-20 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-11-23
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1925 | WARN | <<<
| Missing exit records (post) |  1925 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     1 | INFO |
| Total closed lots           |  3175 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-23_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-23_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1896 med=-26.4% | TAINTED n=2169 med=-43.1% | KEEP-only n=960 med=+51.2% | KILL=23 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=231.54 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 4 | 75% | +0.59% | +0.56% | +0.00% | 123.00 | 0.0d | $+1.22 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261123T140706Z

- UTC timestamp: `20261123T140706Z`
- GitHub run: [#16433](https://github.com/28twagg-ops/TradingBot/actions/runs/45190382272)
- Run id: `45190382272`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`12s`
- Full logs: `logs/action_runs/20261123T140706Z_live_bot.log`, `logs/action_runs/20261123T140706Z_live_options.log`, `logs/action_runs/20261123T140706Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1896 | 48.5 | -26.4 | +35.0 | $+20,954 |
| TAINTED | 2169 | 30.0 | -43.1 | +6.2 | $-14,707 |
| KEEP-only | 960 | 59.7 | +51.2 | +49.7 | $+14,884 |
| KEEP-only recent | 775 | 58.6 | +52.8 | +54.3 | $+11,375 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S396, S397, S403, S404, S406, S410, S430
- KILL strategies (23): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408, S432
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-11-23T09:07:11.596972-05:00","date":"2026-11-23","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.3,"phases_s":{"reconcile":0.53},"signals":0,"placed":0,"equity":991493.65,"open_positions":1,"pending_orders":0,"open_lots":1,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"16433","github_run_id":"45190382272","status":"ok","data_quality":{"clean":{"n":1896,"win":48.47,"med":-26.45,"avg":34.98,"pnl":20953.83},"tainted":{"n":2169,"win":29.97,"med":-43.14,"avg":6.23,"pnl":-14707.28},"keep_only":{"n":960,"win":59.69,"med":51.22,"avg":49.65,"pnl":14884.45},"keep_only_recent":{"n":775,"win":58.58,"med":52.83,"avg":54.29,"pnl":11375.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S396","S397","S403","S404","S406","S410","S430"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408","S432"]}}
```

### Live bot (tail)

```text
14:07:07  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         14:07 UTC|
|  Regime                                                      CORRECTION|
|  Universe                                                          both|
|  Equity                                                         $230.99|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $230.99|
|  Cash                                                           $126.33|
|  Regime                                                      CORRECTION|
|  Universe                                                          both|
|  Total invested                                                 $104.66|
|  Open P&L                                                        $+0.92|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (3 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ACN      Pullback50      $34.76     $221.78  $223.03  +0.6%   $+0.19  |
|  EOG      Pullback50      $34.30     $149.91  $147.78  -1.4%   $-0.50  |
|  TTWO     EarningsDrift   $35.61     $210.02  $217.50  +3.6%   $+1.23  |
|                                                                        |
|  Total invested                                                 $104.66|
|  Total open P&L                                                  $+0.92|
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
|  2026-11-20  SELL  COP  Pullback50  $34.36  P&L $-0.21                 |
|  2026-11-20  SELL  ACN  Pullback50  $34.26  P&L $-0.25                 |
|  2026-11-20  SELL  TTWO  EarningsDrift  $34.60  P&L $+0.10             |
|  2026-11-20  SELL  EOG  Pullback50  $34.38  P&L $-0.19                 |
|  2026-11-20  SELL  ARES  Pullback50  $34.30  P&L $-0.27                |
|  2026-11-20  SELL  EXPD  Pullback50  $70.24  P&L $+1.64                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-11-23T09:07:08.585410-05:00 share=25% ===
2026-11-23 09:07:08,585 INFO === options_live_micro LIVE 2026-11-23T09:07:08.585410-05:00 share=25% ===
Live account equity $230.99 cash $126.33 #225458845 options_level=3
2026-11-23 09:07:08,813 INFO Live account equity $230.99 cash $126.33 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-11-23 09:07:08,886 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-11-23 09:07:08,959 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (220 earlier lines - see full log file)
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
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-27 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-28 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-29 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-30 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-02 |    2 |    0 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-11-03 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-04 |    2 |    2 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-05 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-06 |    1 |    1 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-09 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-11-10 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-12 |    0 |    4 |    0 |    2 |    4 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-11-13 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-16 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-17 |    1 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-20 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-11-23
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1925 | WARN | <<<
| Missing exit records (post) |  1925 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     1 | INFO |
| Total closed lots           |  3175 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-23_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-23_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1896 med=-26.4% | TAINTED n=2169 med=-43.1% | KEEP-only n=960 med=+51.2% | KILL=23 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.99 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 4 | 75% | +0.59% | +0.56% | +0.00% | 123.00 | 0.0d | $+1.22 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261123T141144Z

- UTC timestamp: `20261123T141144Z`
- GitHub run: [#16434](https://github.com/28twagg-ops/TradingBot/actions/runs/45191269780)
- Run id: `45191269780`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`14s`
- Full logs: `logs/action_runs/20261123T141144Z_live_bot.log`, `logs/action_runs/20261123T141144Z_live_options.log`, `logs/action_runs/20261123T141144Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1896 | 48.5 | -26.4 | +35.0 | $+20,954 |
| TAINTED | 2169 | 30.0 | -43.1 | +6.2 | $-14,707 |
| KEEP-only | 960 | 59.7 | +51.2 | +49.7 | $+14,884 |
| KEEP-only recent | 775 | 58.6 | +52.8 | +54.3 | $+11,375 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S396, S397, S403, S404, S406, S410, S430
- KILL strategies (23): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408, S432
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-11-23T09:11:49.813157-05:00","date":"2026-11-23","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.1,"phases_s":{"reconcile":0.35},"signals":0,"placed":0,"equity":991245.13,"open_positions":1,"pending_orders":0,"open_lots":1,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"16434","github_run_id":"45191269780","status":"ok","data_quality":{"clean":{"n":1896,"win":48.47,"med":-26.45,"avg":34.98,"pnl":20953.83},"tainted":{"n":2169,"win":29.97,"med":-43.14,"avg":6.23,"pnl":-14707.28},"keep_only":{"n":960,"win":59.69,"med":51.22,"avg":49.65,"pnl":14884.45},"keep_only_recent":{"n":775,"win":58.58,"med":52.83,"avg":54.29,"pnl":11375.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S396","S397","S403","S404","S406","S410","S430"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408","S432"]}}
```

### Live bot (tail)

```text
14:11:45  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         14:11 UTC|
|  Regime                                                      CORRECTION|
|  Universe                                                          both|
|  Equity                                                         $231.14|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $231.14|
|  Cash                                                           $126.33|
|  Regime                                                      CORRECTION|
|  Universe                                                          both|
|  Total invested                                                 $104.81|
|  Open P&L                                                        $+1.07|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (3 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ACN      Pullback50      $34.99     $221.78  $224.51  +1.2%   $+0.43  |
|  EOG      Pullback50      $34.30     $149.91  $147.78  -1.4%   $-0.50  |
|  TTWO     EarningsDrift   $35.53     $210.02  $217.00  +3.3%   $+1.14  |
|                                                                        |
|  Total invested                                                 $104.81|
|  Total open P&L                                                  $+1.07|
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
|  2026-11-20  SELL  COP  Pullback50  $34.36  P&L $-0.21                 |
|  2026-11-20  SELL  ACN  Pullback50  $34.26  P&L $-0.25                 |
|  2026-11-20  SELL  TTWO  EarningsDrift  $34.60  P&L $+0.10             |
|  2026-11-20  SELL  EOG  Pullback50  $34.38  P&L $-0.19                 |
|  2026-11-20  SELL  ARES  Pullback50  $34.30  P&L $-0.27                |
|  2026-11-20  SELL  EXPD  Pullback50  $70.24  P&L $+1.64                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-11-23T09:11:47.042222-05:00 share=25% ===
2026-11-23 09:11:47,042 INFO === options_live_micro LIVE 2026-11-23T09:11:47.042222-05:00 share=25% ===
Live account equity $231.14 cash $126.33 #225458845 options_level=3
2026-11-23 09:11:47,149 INFO Live account equity $231.14 cash $126.33 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-11-23 09:11:47,182 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-11-23 09:11:47,212 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (220 earlier lines - see full log file)
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
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-27 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-28 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-29 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-30 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-02 |    2 |    0 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-11-03 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-04 |    2 |    2 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-05 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-06 |    1 |    1 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-09 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-11-10 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-12 |    0 |    4 |    0 |    2 |    4 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-11-13 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-16 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-17 |    1 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-20 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-11-23
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1925 | WARN | <<<
| Missing exit records (post) |  1925 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     1 | INFO |
| Total closed lots           |  3175 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-23_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-23_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1896 med=-26.4% | TAINTED n=2169 med=-43.1% | KEEP-only n=960 med=+51.2% | KILL=23 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=231.14 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 4 | 75% | +0.59% | +0.56% | +0.00% | 123.00 | 0.0d | $+1.22 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261123T141643Z

- UTC timestamp: `20261123T141643Z`
- GitHub run: [#16435](https://github.com/28twagg-ops/TradingBot/actions/runs/45192163021)
- Run id: `45192163021`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`14s`
- Full logs: `logs/action_runs/20261123T141643Z_live_bot.log`, `logs/action_runs/20261123T141643Z_live_options.log`, `logs/action_runs/20261123T141643Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1896 | 48.5 | -26.4 | +35.0 | $+20,954 |
| TAINTED | 2169 | 30.0 | -43.1 | +6.2 | $-14,707 |
| KEEP-only | 960 | 59.7 | +51.2 | +49.7 | $+14,884 |
| KEEP-only recent | 775 | 58.6 | +52.8 | +54.3 | $+11,375 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S396, S397, S403, S404, S406, S410, S430
- KILL strategies (23): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408, S432
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-11-23T09:16:47.883670-05:00","date":"2026-11-23","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.08},"signals":0,"placed":0,"equity":990768.71,"open_positions":1,"pending_orders":0,"open_lots":1,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"16435","github_run_id":"45192163021","status":"ok","data_quality":{"clean":{"n":1896,"win":48.47,"med":-26.45,"avg":34.98,"pnl":20953.83},"tainted":{"n":2169,"win":29.97,"med":-43.14,"avg":6.23,"pnl":-14707.28},"keep_only":{"n":960,"win":59.69,"med":51.22,"avg":49.65,"pnl":14884.45},"keep_only_recent":{"n":775,"win":58.58,"med":52.83,"avg":54.29,"pnl":11375.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S396","S397","S403","S404","S406","S410","S430"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408","S432"]}}
```

### Live bot (tail)

```text
14:16:44  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         14:16 UTC|
|  Regime                                                      CORRECTION|
|  Universe                                                          both|
|  Equity                                                         $230.70|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $230.70|
|  Cash                                                           $126.33|
|  Regime                                                      CORRECTION|
|  Universe                                                          both|
|  Total invested                                                 $104.37|
|  Open P&L                                                        $+0.63|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (3 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ACN      Pullback50      $34.99     $221.78  $224.50  +1.2%   $+0.42  |
|  EOG      Pullback50      $34.30     $149.91  $147.78  -1.4%   $-0.50  |
|  TTWO     EarningsDrift   $35.09     $210.02  $214.33  +2.1%   $+0.71  |
|                                                                        |
|  Total invested                                                 $104.37|
|  Total open P&L                                                  $+0.63|
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
|  2026-11-20  SELL  COP  Pullback50  $34.36  P&L $-0.21                 |
|  2026-11-20  SELL  ACN  Pullback50  $34.26  P&L $-0.25                 |
|  2026-11-20  SELL  TTWO  EarningsDrift  $34.60  P&L $+0.10             |
|  2026-11-20  SELL  EOG  Pullback50  $34.38  P&L $-0.19                 |
|  2026-11-20  SELL  ARES  Pullback50  $34.30  P&L $-0.27                |
|  2026-11-20  SELL  EXPD  Pullback50  $70.24  P&L $+1.64                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-11-23T09:16:45.284932-05:00 share=25% ===
2026-11-23 09:16:45,285 INFO === options_live_micro LIVE 2026-11-23T09:16:45.284932-05:00 share=25% ===
Live account equity $230.70 cash $126.33 #225458845 options_level=3
2026-11-23 09:16:45,322 INFO Live account equity $230.70 cash $126.33 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-11-23 09:16:45,330 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-11-23 09:16:45,337 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (220 earlier lines - see full log file)
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
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-27 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-28 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-29 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-30 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-02 |    2 |    0 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-11-03 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-04 |    2 |    2 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-05 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-06 |    1 |    1 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-09 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-11-10 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-12 |    0 |    4 |    0 |    2 |    4 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-11-13 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-16 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-17 |    1 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-20 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-11-23
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1925 | WARN | <<<
| Missing exit records (post) |  1925 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     1 | INFO |
| Total closed lots           |  3175 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-23_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-23_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1896 med=-26.4% | TAINTED n=2169 med=-43.1% | KEEP-only n=960 med=+51.2% | KILL=23 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.7 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 4 | 75% | +0.59% | +0.56% | +0.00% | 123.00 | 0.0d | $+1.22 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20261123T142153Z

- UTC timestamp: `20261123T142153Z`
- GitHub run: [#16436](https://github.com/28twagg-ops/TradingBot/actions/runs/45193069645)
- Run id: `45193069645`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`14s`
- Full logs: `logs/action_runs/20261123T142153Z_live_bot.log`, `logs/action_runs/20261123T142153Z_live_options.log`, `logs/action_runs/20261123T142153Z_options_bot.log`


### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 1896 | 48.5 | -26.4 | +35.0 | $+20,954 |
| TAINTED | 2169 | 30.0 | -43.1 | +6.2 | $-14,707 |
| KEEP-only | 960 | 59.7 | +51.2 | +49.7 | $+14,884 |
| KEEP-only recent | 775 | 58.6 | +52.8 | +54.3 | $+11,375 |

- KEEP strategies (24): S163, S164, S166, S167, S168, S173, S174, S210, S350, S352, S356, S357, S359, S361, S362, S364, S365, S396, S397, S403, S404, S406, S410, S430
- KILL strategies (23): ORPHAN, S202, S203, S207, S211, S212, S216, S217, S218, S351, S353, S354, S355, S360, S363, S366, S398, S399, S401, S405, S407, S408, S432
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.

- Options structured summary (latest JSON):
```json
{"ts_et":"2026-11-23T09:21:59.127519-05:00","date":"2026-11-23","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.2,"phases_s":{"reconcile":0.43},"signals":0,"placed":0,"equity":990987.68,"open_positions":1,"pending_orders":0,"open_lots":1,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"16436","github_run_id":"45193069645","status":"ok","data_quality":{"clean":{"n":1896,"win":48.47,"med":-26.45,"avg":34.98,"pnl":20953.83},"tainted":{"n":2169,"win":29.97,"med":-43.14,"avg":6.23,"pnl":-14707.28},"keep_only":{"n":960,"win":59.69,"med":51.22,"avg":49.65,"pnl":14884.45},"keep_only_recent":{"n":775,"win":58.58,"med":52.83,"avg":54.29,"pnl":11375.0},"keep_strategies":["S163","S164","S166","S167","S168","S173","S174","S210","S350","S352","S356","S357","S359","S361","S362","S364","S365","S396","S397","S403","S404","S406","S410","S430"],"kill_strategies":["ORPHAN","S202","S203","S207","S211","S212","S216","S217","S218","S351","S353","S354","S355","S360","S363","S366","S398","S399","S401","S405","S407","S408","S432"]}}
```

### Live bot (tail)

```text
14:21:54  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         14:21 UTC|
|  Regime                                                      CORRECTION|
|  Universe                                                          both|
|  Equity                                                         $230.41|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $230.41|
|  Cash                                                           $126.33|
|  Regime                                                      CORRECTION|
|  Universe                                                          both|
|  Total invested                                                 $104.08|
|  Open P&L                                                        $+0.34|
+========================================================================+

+========================================================================+
|                     STOCK HOLDINGS  (3 positions)                      |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ACN      Pullback50      $35.24     $221.78  $226.12  +2.0%   $+0.68  |
|  EOG      Pullback50      $34.30     $149.91  $147.78  -1.4%   $-0.50  |
|  TTWO     EarningsDrift   $34.54     $210.02  $211.00  +0.5%   $+0.16  |
|                                                                        |
|  Total invested                                                 $104.08|
|  Total open P&L                                                  $+0.34|
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
|  2026-11-20  SELL  COP  Pullback50  $34.36  P&L $-0.21                 |
|  2026-11-20  SELL  ACN  Pullback50  $34.26  P&L $-0.25                 |
|  2026-11-20  SELL  TTWO  EarningsDrift  $34.60  P&L $+0.10             |
|  2026-11-20  SELL  EOG  Pullback50  $34.38  P&L $-0.19                 |
|  2026-11-20  SELL  ARES  Pullback50  $34.30  P&L $-0.27                |
|  2026-11-20  SELL  EXPD  Pullback50  $70.24  P&L $+1.64                |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-11-23T09:21:56.094945-05:00 share=25% ===
2026-11-23 09:21:56,095 INFO === options_live_micro LIVE 2026-11-23T09:21:56.094945-05:00 share=25% ===
Live account equity $230.41 cash $126.33 #225458845 options_level=3
2026-11-23 09:21:56,280 INFO Live account equity $230.41 cash $126.33 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-11-23 09:21:56,338 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-11-23 09:21:56,394 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
... (220 earlier lines - see full log file)
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
| 2026-10-16 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-10-20 |    1 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-10-21 |    2 |    3 |    0 |    2 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-10-22 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-23 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-26 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-27 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-10-28 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     2 |
| 2026-10-29 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-10-30 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-02 |    2 |    0 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-11-03 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-04 |    2 |    2 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-05 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-06 |    1 |    1 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-09 |    0 |    2 |    0 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-11-10 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-12 |    0 |    4 |    0 |    2 |    4 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    12 |
| 2026-11-13 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-16 |    2 |    2 |    0 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |
| 2026-11-17 |    1 |    2 |    0 |    2 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |
| 2026-11-20 |    2 |    2 |    0 |    0 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     8 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-11-23
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |  1925 | WARN | <<<
| Missing exit records (post) |  1925 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     1 | INFO |
| Total closed lots           |  3175 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-23_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-11-23_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=1896 med=-26.4% | TAINTED n=2169 med=-43.1% | KEEP-only n=960 med=+51.2% | KILL=23 KEEP=24
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=230.41 router=CONFIRMED leaderboard_rows=108
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MA_Squeeze | 4 | 75% | +0.59% | +0.56% | +0.00% | 123.00 | 0.0d | $+1.22 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---
