# Daily Comprehensive Action Review — 2026-08-18

_Auto-generated from GitHub Actions run output. This document appends every run for the day._

## Run 20260818T130625Z

- UTC timestamp: `20260818T130625Z`
- GitHub run: [#7337](https://github.com/28twagg-ops/TradingBot/actions/runs/32140329758)
- Run id: `32140329758`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`0s`

### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 821 | 41.8 | -47.5 | +15.4 | $+8,207 |
| TAINTED | 1761 | 33.0 | -39.3 | +12.2 | $-9,205 |
| KEEP-only | 294 | 63.3 | +37.5 | +42.9 | $+5,699 |
| KEEP-only recent | 106 | 58.5 | +50.0 | +54.8 | $+1,673 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406
- KILL strategies (16): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-18T09:06:29.159068-04:00","date":"2026-08-18","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":260.8,"phases_s":{"reconcile":140.21},"signals":0,"placed":0,"equity":null,"open_positions":13,"pending_orders":0,"open_lots":43,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"7337","github_run_id":"32140329758","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot full output

```text
13:06:26  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $467.77|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $467.77|
|  Cash                                                           $397.55|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $70.22|
|  Open P&L                                                        $+0.07|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (1 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $70.22     $14.75   $14.76   +0.1%   $+0.07  |
|                                                                        |
|  Total invested                                                  $70.22|
|  Total open P&L                                                  $+0.07|
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
|  2026-08-17  SELL  BG  Pullback50  $70.22  P&L $+0.04                  |
|  2026-08-17  SELL  ADI  Pullback50  $70.03  P&L $-0.12                 |
|  2026-08-17  SELL  AFL  Pullback50  $69.92  P&L $-0.36                 |
|  2026-08-17  SELL  AXP  Pullback50  $69.89  P&L $-0.39                 |
|  2026-08-17  SELL  AMD  Pullback50  $70.24  P&L $-0.04                 |
|  2026-08-17  SELL  ACGL  Pullback50  $70.21  P&L $+1.31                |
+========================================================================+
```

### Live options micro full output

```text
=== options_live_micro LIVE 2026-08-18T09:06:27.422560-04:00 share=50% ===
2026-08-18 09:06:27,422 INFO === options_live_micro LIVE 2026-08-18T09:06:27.422560-04:00 share=50% ===
Live account equity $467.77 cash $397.55 #225458845 options_level=3
2026-08-18 09:06:27,461 INFO Live account equity $467.77 cash $397.55 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-08-18 09:06:27,552 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-08-18 09:06:27,559 INFO Live micro done. open_options=0 lots=0
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=45 paper_keys=yes dry_run=False
  alpaca positions=16
  FLAG b262|S403|186fe065 missing from Alpaca
  FLAG b0|ORPHAN|5c5bca01 missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-18T09:06:29.159068-04:00 ===

[Run context]
After hours (09:06 ET) — exit summary only.
2026-08-18 09:06:29,229 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-18 09:06:37,241 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-18 09:06:53,254 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
2026-08-18 09:07:17,265 WARNING paper get_account failed attempt 4/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 32s
2026-08-18 09:07:49,282 WARNING paper get_account failed attempt 5/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 40s
2026-08-18 09:08:29,296 ERROR paper get_account failed after 6 attempts: {"code":50010000,"message":"internal server error occurred"}
WARN: get_account failed ({"code":50010000,"message":"internal server error occurred"}) but positions OK (n=16). Keys are fine; Alpaca account endpoint is flaky. Continuing manage/exits; skipping new entries until equity is readable.
2026-08-18 09:08:29,316 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-18 09:08:37,328 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-18 09:08:53,339 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
2026-08-18 09:09:17,349 WARNING paper get_account failed attempt 4/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 32s
2026-08-18 09:09:49,362 WARNING paper get_account failed attempt 5/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 40s
2026-08-18 09:10:29,389 ERROR paper get_account failed after 6 attempts: {"code":50010000,"message":"internal server error occurred"}
2026-08-18 09:10:29,408 WARNING lab get_account failed attempt 1/3: {"code":50010000,"message":"internal server error occurred"}
2026-08-18 09:10:39,419 WARNING lab get_account failed attempt 2/3: {"code":50010000,"message":"internal server error occurred"}
2026-08-18 09:10:49,433 ERROR lab get_account failed after 3 attempts: {"code":50010000,"message":"internal server error occurred"}

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|[OPTIONS BOT DAILY VITALS (MATRIX EXPERIMENT)]                          |
+========================================================================+
|-- ACCOUNT STATUS (after_hours) --                                      |
|Open Risk    : 43 lots (13 broker pos)                                  |
|Today's Run  : 0 signals -> 0 orders submitted                          |
|                                                                        |
|-- SYSTEM HEALTH --                                                     |
|Zombies      : 1 WARN: See reconcile                                    |
|Lab Status   : 43 Active Lots | 0 Pending Orders                        |
|Auto-Matrix  : (Pending EOD report generation)                          |
+========================================================================+
+========================================================================+
|[DATA QUALITY: CLEAN vs ERRORS vs KEEP-ONLY]                            |
+========================================================================+
|  CLEAN              n=821   win= 41.8%  med= -47.5%  $+8,207           |
|  TAINTED            n=1761  win= 33.0%  med= -39.3%  $-9,205           |
|  KEEP-only          n=294   win= 63.3%  med= +37.5%  $+5,699           |
|  KEEP recent        n=106   win= 58.5%  med= +50.0%  $+1,673           |
|  KEEP(10): S173,S174,S210,S218,S350,S397,S398,S401...                  |
|  KILL(16): ORPHAN,S165,S203,S207,S211,S212,S217,S351...                |
+========================================================================+
+========================================================================+
|[+++ OVERPERFORMING STRATEGIES (n>=10)]                                 |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b832 lab0832_s406_w3_1045..  82%  +126.9%    11                       |
|  b238 lab0238_s401_w3_1045..  80%  +109.5%    15                       |
|  b861 lab0861_s408_w3_1045..  73%  +100.0%    11                       |
|  b365 lab0365_s361_w2_1005..  90%  +82.8%    10                        |
+========================================================================+
|[--- UNDERPERFORMING STRATEGIES (n>=10)]                                |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b47  lab0047_s205_w4_1120..   4%  -78.0%    28                        |
|  b109 lab0109_s212_w1_0928..   0%  -77.5%    10                        |
|  b114 lab0114_s212_w4_1120..   0%  -73.5%    11                        |
|  b113 lab0113_s212_w3_1045..   7%  -71.4%    15                        |
+========================================================================+
+========================================================================+
|[OPEN OPTIONS (13)]                                                     |
+========================================================================+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|  ---------------------------------------------------------             |
|  MARA260821C00009500          24    +97.2%   $   +556.00               |
|  MSTR260821C00102000           4   +106.8%   $   +312.00               |
|  MSTR260821C00103000           4    +87.0%   $   +240.00               |
|  MARA260821C00009000           4    +66.0%   $   +124.00               |
|  MARA260821C00008500           2    +69.0%   $    +98.00               |
|  MSTR260821C00105000           2    +84.3%   $    +86.00               |
|  MSTR260821C00104000           1   +120.0%   $    +60.00               |
|  MARA260828C00009500           2    +46.5%   $    +40.00               |
|  ... 5 more position(s)                                                |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-18.log
elapsed=260.8s reconcile=140.21s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=260.8s. run=#7337 https://github.com/28twagg-ops/TradingBot/actions/runs/32140329758
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-18_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-18_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-18_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-18_strategy_selection.csv
Summary: keep=0 watch=79 drop=26
Orphan rate: 13.4% (345/2582) ALERT
```

---

## Run 20260818T131206Z

- UTC timestamp: `20260818T131206Z`
- GitHub run: [#7338](https://github.com/28twagg-ops/TradingBot/actions/runs/32140802238)
- Run id: `32140802238`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`0s`

### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 821 | 41.8 | -47.5 | +15.4 | $+8,207 |
| TAINTED | 1761 | 33.0 | -39.3 | +12.2 | $-9,205 |
| KEEP-only | 294 | 63.3 | +37.5 | +42.9 | $+5,699 |
| KEEP-only recent | 106 | 58.5 | +50.0 | +54.8 | $+1,673 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406
- KILL strategies (16): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-17T19:56:23.633587-04:00","date":"2026-08-17","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":261.1,"phases_s":{"reconcile":140.41},"signals":0,"placed":0,"equity":null,"open_positions":14,"pending_orders":0,"open_lots":45,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"7335","github_run_id":"32082431205","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot full output

```text
13:12:06  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:12 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $467.77|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $467.77|
|  Cash                                                           $397.55|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $70.22|
|  Open P&L                                                        $+0.07|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (1 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $70.22     $14.75   $14.76   +0.1%   $+0.07  |
|                                                                        |
|  Total invested                                                  $70.22|
|  Total open P&L                                                  $+0.07|
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
|  2026-08-17  SELL  BG  Pullback50  $70.22  P&L $+0.04                  |
|  2026-08-17  SELL  ADI  Pullback50  $70.03  P&L $-0.12                 |
|  2026-08-17  SELL  AFL  Pullback50  $69.92  P&L $-0.36                 |
|  2026-08-17  SELL  AXP  Pullback50  $69.89  P&L $-0.39                 |
|  2026-08-17  SELL  AMD  Pullback50  $70.24  P&L $-0.04                 |
|  2026-08-17  SELL  ACGL  Pullback50  $70.21  P&L $+1.31                |
+========================================================================+
```

### Live options micro full output

```text
=== options_live_micro LIVE 2026-08-18T09:12:07.979976-04:00 share=50% ===
2026-08-18 09:12:07,980 INFO === options_live_micro LIVE 2026-08-18T09:12:07.979976-04:00 share=50% ===
Live account equity $467.77 cash $397.55 #225458845 options_level=3
2026-08-18 09:12:08,143 INFO Live account equity $467.77 cash $397.55 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-08-18 09:12:08,187 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-08-18 09:12:08,230 INFO Live micro done. open_options=0 lots=0
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=45 paper_keys=yes dry_run=False
  alpaca positions=16
  FLAG b262|S403|186fe065 missing from Alpaca
  FLAG b0|ORPHAN|5c5bca01 missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-18T09:12:09.824023-04:00 ===

[Run context]
After hours (09:12 ET) — exit summary only.
2026-08-18 09:12:09,998 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-18 09:12:18,047 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-18 09:12:34,096 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
2026-08-18 09:12:58,148 WARNING paper get_account failed attempt 4/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 32s
2026-08-18 09:13:30,196 WARNING paper get_account failed attempt 5/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 40s
2026-08-18 09:14:10,248 ERROR paper get_account failed after 6 attempts: {"code":50010000,"message":"internal server error occurred"}
WARN: get_account failed ({"code":50010000,"message":"internal server error occurred"}) but positions OK (n=16). Keys are fine; Alpaca account endpoint is flaky. Continuing manage/exits; skipping new entries until equity is readable.
2026-08-18 09:14:10,345 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-18 09:14:18,400 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-18 09:14:34,449 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
2026-08-18 09:14:58,498 WARNING paper get_account failed attempt 4/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 32s
2026-08-18 09:15:30,549 WARNING paper get_account failed attempt 5/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 40s
```

---

## Run 20260818T132345Z

- UTC timestamp: `20260818T132345Z`
- GitHub run: [#7340](https://github.com/28twagg-ops/TradingBot/actions/runs/32141749081)
- Run id: `32141749081`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`0s`

### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 821 | 41.8 | -47.5 | +15.4 | $+8,207 |
| TAINTED | 1761 | 33.0 | -39.3 | +12.2 | $-9,205 |
| KEEP-only | 294 | 63.3 | +37.5 | +42.9 | $+5,699 |
| KEEP-only recent | 106 | 58.5 | +50.0 | +54.8 | $+1,673 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406
- KILL strategies (16): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-17T19:56:23.633587-04:00","date":"2026-08-17","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":261.1,"phases_s":{"reconcile":140.41},"signals":0,"placed":0,"equity":null,"open_positions":14,"pending_orders":0,"open_lots":45,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"7335","github_run_id":"32082431205","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot full output

```text
13:23:46  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:23 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $467.77|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $467.77|
|  Cash                                                           $397.55|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $70.22|
|  Open P&L                                                        $+0.07|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (1 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $70.22     $14.75   $14.76   +0.1%   $+0.07  |
|                                                                        |
|  Total invested                                                  $70.22|
|  Total open P&L                                                  $+0.07|
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
|  2026-08-17  SELL  BG  Pullback50  $70.22  P&L $+0.04                  |
|  2026-08-17  SELL  ADI  Pullback50  $70.03  P&L $-0.12                 |
|  2026-08-17  SELL  AFL  Pullback50  $69.92  P&L $-0.36                 |
|  2026-08-17  SELL  AXP  Pullback50  $69.89  P&L $-0.39                 |
|  2026-08-17  SELL  AMD  Pullback50  $70.24  P&L $-0.04                 |
|  2026-08-17  SELL  ACGL  Pullback50  $70.21  P&L $+1.31                |
+========================================================================+
```

### Live options micro full output

```text
=== options_live_micro LIVE 2026-08-18T09:23:48.182531-04:00 share=50% ===
2026-08-18 09:23:48,182 INFO === options_live_micro LIVE 2026-08-18T09:23:48.182531-04:00 share=50% ===
Live account equity $467.77 cash $397.55 #225458845 options_level=3
2026-08-18 09:23:48,380 INFO Live account equity $467.77 cash $397.55 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-08-18 09:23:48,439 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-08-18 09:23:48,497 INFO Live micro done. open_options=0 lots=0
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=43 paper_keys=yes dry_run=False
  alpaca positions=16
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-18T09:23:50.600062-04:00 ===

[Run context]
After hours (09:23 ET) — exit summary only.
2026-08-18 09:23:50,836 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-18 09:23:58,901 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-18 09:24:14,965 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
2026-08-18 09:24:39,027 WARNING paper get_account failed attempt 4/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 32s
2026-08-18 09:25:11,091 WARNING paper get_account failed attempt 5/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 40s
```

---

## Run 20260818T132643Z

- UTC timestamp: `20260818T132643Z`
- GitHub run: [#7341](https://github.com/28twagg-ops/TradingBot/actions/runs/32142227953)
- Run id: `32142227953`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`0s`

### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 821 | 41.8 | -47.5 | +15.4 | $+8,207 |
| TAINTED | 1761 | 33.0 | -39.3 | +12.2 | $-9,205 |
| KEEP-only | 294 | 63.3 | +37.5 | +42.9 | $+5,699 |
| KEEP-only recent | 106 | 58.5 | +50.0 | +54.8 | $+1,673 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406
- KILL strategies (16): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-17T19:56:23.633587-04:00","date":"2026-08-17","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":261.1,"phases_s":{"reconcile":140.41},"signals":0,"placed":0,"equity":null,"open_positions":14,"pending_orders":0,"open_lots":45,"submitted_today":0,"filled_today":0,"unattributed_contracts":1,"top_signals":[],"github_run":"7335","github_run_id":"32082431205","status":"ok","data_quality":{"clean":{"n":821,"win":41.78,"med":-47.45,"avg":15.44,"pnl":8206.53},"tainted":{"n":1761,"win":33.05,"med":-39.29,"avg":12.19,"pnl":-9205.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot full output

```text
13:26:44  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $467.77|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $467.77|
|  Cash                                                           $397.55|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $70.22|
|  Open P&L                                                        $+0.07|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (1 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $70.22     $14.75   $14.76   +0.1%   $+0.07  |
|                                                                        |
|  Total invested                                                  $70.22|
|  Total open P&L                                                  $+0.07|
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
|  2026-08-17  SELL  BG  Pullback50  $70.22  P&L $+0.04                  |
|  2026-08-17  SELL  ADI  Pullback50  $70.03  P&L $-0.12                 |
|  2026-08-17  SELL  AFL  Pullback50  $69.92  P&L $-0.36                 |
|  2026-08-17  SELL  AXP  Pullback50  $69.89  P&L $-0.39                 |
|  2026-08-17  SELL  AMD  Pullback50  $70.24  P&L $-0.04                 |
|  2026-08-17  SELL  ACGL  Pullback50  $70.21  P&L $+1.31                |
+========================================================================+
```

### Live options micro full output

```text
=== options_live_micro LIVE 2026-08-18T09:26:46.440445-04:00 share=50% ===
2026-08-18 09:26:46,440 INFO === options_live_micro LIVE 2026-08-18T09:26:46.440445-04:00 share=50% ===
Live account equity $467.77 cash $397.55 #225458845 options_level=3
2026-08-18 09:26:46,684 INFO Live account equity $467.77 cash $397.55 #225458845 options_level=3
Live micro: outside 9:28-16:05 ET
2026-08-18 09:26:46,776 INFO Live micro: outside 9:28-16:05 ET
Live micro done. open_options=0 lots=0
2026-08-18 09:26:46,850 INFO Live micro done. open_options=0 lots=0
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=43 paper_keys=yes dry_run=False
  alpaca positions=16
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-18T09:26:49.038220-04:00 ===

[Run context]
After hours (09:26 ET) — exit summary only.
2026-08-18 09:26:49,324 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-18 09:26:57,402 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-18 09:27:13,479 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
2026-08-18 09:27:37,572 WARNING paper get_account failed attempt 4/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 32s
2026-08-18 09:28:09,650 WARNING paper get_account failed attempt 5/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 40s
2026-08-18 09:28:49,750 ERROR paper get_account failed after 6 attempts: {"code":50010000,"message":"internal server error occurred"}
WARN: get_account failed ({"code":50010000,"message":"internal server error occurred"}) but positions OK (n=16). Keys are fine; Alpaca account endpoint is flaky. Continuing manage/exits; skipping new entries until equity is readable.
2026-08-18 09:28:49,904 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-18 09:28:57,981 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-18 09:29:14,080 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
2026-08-18 09:29:38,160 WARNING paper get_account failed attempt 4/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 32s
2026-08-18 09:30:10,258 WARNING paper get_account failed attempt 5/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 40s
2026-08-18 09:30:50,339 ERROR paper get_account failed after 6 attempts: {"code":50010000,"message":"internal server error occurred"}
2026-08-18 09:30:50,526 WARNING lab get_account failed attempt 1/3: {"code":50010000,"message":"internal server error occurred"}
```

---
