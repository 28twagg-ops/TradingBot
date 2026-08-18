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

## Run 20260818T133202Z

- UTC timestamp: `20260818T133202Z`
- GitHub run: [#7342](https://github.com/28twagg-ops/TradingBot/actions/runs/32142717288)
- Run id: `32142717288`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
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
13:32:03  INFO      Mode: morning_prep
13:32:05  INFO        [prep_positions] 1/1 (1 valid)
13:32:05  INFO      Fetching tickers (universe=both)...
13:32:05  INFO        S&P 500: 503
13:32:05  INFO        MidCap 400: 400
13:32:05  INFO        Total: 903 tickers
13:32:07  INFO        [prep_universe] 40/902 (40 valid)
13:32:08  INFO        [prep_universe] 80/902 (80 valid)
13:32:10  INFO        [prep_universe] 120/902 (120 valid)
13:32:11  INFO        [prep_universe] 160/902 (160 valid)
13:32:13  INFO        [prep_universe] 200/902 (199 valid)
13:32:20  INFO        [prep_universe] 240/902 (238 valid)
13:32:31  INFO        [prep_universe] 280/902 (278 valid)
13:32:42  INFO        [prep_universe] 320/902 (318 valid)
13:32:56  INFO        [prep_universe] 360/902 (358 valid)
13:33:06  INFO        [prep_universe] 400/902 (397 valid)
13:33:20  INFO        [prep_universe] 440/902 (437 valid)
13:33:31  INFO        [prep_universe] 480/902 (476 valid)
13:33:42  INFO        [prep_universe] 520/902 (516 valid)
13:33:55  INFO        [prep_universe] 560/902 (556 valid)
13:34:08  INFO        [prep_universe] 600/902 (596 valid)
13:34:19  INFO        [prep_universe] 640/902 (636 valid)
13:34:30  INFO        [prep_universe] 680/902 (676 valid)
13:34:43  INFO        [prep_universe] 720/902 (716 valid)
13:34:53  INFO        [prep_universe] 760/902 (756 valid)
13:35:07  INFO        [prep_universe] 800/902 (796 valid)
13:35:18  INFO        [prep_universe] 840/902 (835 valid)
13:35:31  INFO        [prep_universe] 880/902 (875 valid)
13:35:38  INFO        [prep_universe] 902/902 (897 valid)
```

### Options bot full output

```text

## Run 20260818T133644Z

- UTC timestamp: `20260818T133644Z`
- GitHub run: [#7343](https://github.com/28twagg-ops/TradingBot/actions/runs/32143202526)
- Run id: `32143202526`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
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
13:36:45  INFO      Mode: morning_prep
13:36:46  INFO        [prep_positions] 1/1 (1 valid)
13:36:46  INFO      Fetching tickers (universe=both)...
13:36:47  INFO        S&P 500: 503
13:36:47  INFO        MidCap 400: 400
13:36:47  INFO        Total: 903 tickers
13:36:48  INFO        [prep_universe] 40/902 (40 valid)
13:36:49  INFO        [prep_universe] 80/902 (80 valid)
13:36:50  INFO        [prep_universe] 120/902 (120 valid)
13:36:52  INFO        [prep_universe] 160/902 (160 valid)
13:36:53  INFO        [prep_universe] 200/902 (199 valid)
13:37:01  INFO        [prep_universe] 240/902 (238 valid)
13:37:11  INFO        [prep_universe] 280/902 (278 valid)
13:37:26  INFO        [prep_universe] 320/902 (318 valid)
13:37:36  INFO        [prep_universe] 360/902 (358 valid)
13:37:47  INFO        [prep_universe] 400/902 (397 valid)
13:38:01  INFO        [prep_universe] 440/902 (437 valid)
13:38:11  INFO        [prep_universe] 480/902 (476 valid)
13:38:24  INFO        [prep_universe] 520/902 (516 valid)
13:38:38  INFO        [prep_universe] 560/902 (556 valid)
13:38:48  INFO        [prep_universe] 600/902 (596 valid)
13:39:02  INFO        [prep_universe] 640/902 (636 valid)
13:39:12  INFO        [prep_universe] 680/902 (676 valid)
13:39:26  INFO        [prep_universe] 720/902 (716 valid)
13:39:36  INFO        [prep_universe] 760/902 (756 valid)
13:39:50  INFO        [prep_universe] 800/902 (796 valid)
13:40:00  INFO        [prep_universe] 840/902 (835 valid)
13:40:12  INFO        [prep_universe] 880/902 (875 valid)
13:40:19  INFO        [prep_universe] 902/902 (897 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $467.82|
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
|  Open positions                                                       1|
|  Invested                                                        $70.27|
|  Open P&L                                                        $+0.11|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $70.27     $14.75   $14.77   +0.2%   $+0.11  |
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
|  Signal candidates                                                   25|
|  Universe scanned                                                   902|
+========================================================================+
```

### Options bot full output

```text

## Run 20260818T134538Z

- UTC timestamp: `20260818T134538Z`
- GitHub run: [#7344](https://github.com/28twagg-ops/TradingBot/actions/runs/32143690431)
- Run id: `32143690431`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
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
13:45:39  INFO      Mode: morning_scan
13:45:40  INFO        [positions] 1/1 (1 valid)
13:45:41  INFO        SELL LIMIT AES  qty=4.757764817  limit=$14.76  id=50d13bfa-ebac-4430-ba73-9f034b98342e
```

### Options bot full output

```text

## Run 20260818T134701Z

- UTC timestamp: `20260818T134701Z`
- GitHub run: [#7345](https://github.com/28twagg-ops/TradingBot/actions/runs/32144172942)
- Run id: `32144172942`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
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
13:47:02  INFO      Mode: morning_scan
13:47:04  INFO        Universe cache hit: 903 tickers (tickers_2026-08-18.json)
13:47:05  INFO        [universe] 40/903 (40 valid)
13:47:07  INFO        [universe] 80/903 (80 valid)
13:47:08  INFO        [universe] 120/903 (120 valid)
13:47:09  INFO        [universe] 160/903 (160 valid)
13:47:11  INFO        [universe] 200/903 (199 valid)
13:47:18  INFO        [universe] 240/903 (238 valid)
13:47:29  INFO        [universe] 280/903 (278 valid)
13:47:42  INFO        [universe] 320/903 (318 valid)
13:47:53  INFO        [universe] 360/903 (358 valid)
13:48:06  INFO        [universe] 400/903 (397 valid)
13:48:17  INFO        [universe] 440/903 (437 valid)
13:48:30  INFO        [universe] 480/903 (476 valid)
13:48:41  INFO        [universe] 520/903 (516 valid)
13:48:55  INFO        [universe] 560/903 (556 valid)
13:49:05  INFO        [universe] 600/903 (596 valid)
13:49:19  INFO        [universe] 640/903 (636 valid)
13:49:29  INFO        [universe] 680/903 (676 valid)
13:49:42  INFO        [universe] 720/903 (716 valid)
13:49:53  INFO        [universe] 760/903 (756 valid)
13:50:07  INFO        [universe] 800/903 (796 valid)
13:50:17  INFO        [universe] 840/903 (835 valid)
13:50:31  INFO        [universe] 880/903 (875 valid)
```

### Options bot full output

```text

## Run 20260818T135138Z

- UTC timestamp: `20260818T135138Z`
- GitHub run: [#7346](https://github.com/28twagg-ops/TradingBot/actions/runs/32144665635)
- Run id: `32144665635`
- Live bot: exit=`0`, duration=`0s`
- Live options: exit=`0`, duration=`0s`
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
13:51:39  INFO      Mode: morning_scan
13:51:41  INFO        [positions] 3/3 (3 valid)
13:51:41  INFO        SELL MARKET [urgent] AKAM closed
13:51:43  INFO        TX logged: SELL AKAM  P&L -0.53%
13:51:44  INFO        SELL LIMIT AES  qty=4.751439214  limit=$14.76  id=e442509f-e86e-486a-a275-80862722dc8a
13:52:14  INFO        SELL LIMIT filled AES (confirmed by position check)
13:52:14  INFO        TX logged: SELL AES  P&L 0.0%
13:52:14  INFO        Universe cache hit: 903 tickers (tickers_2026-08-18.json)
13:52:16  INFO        [universe] 40/902 (40 valid)
13:52:17  INFO        [universe] 80/902 (80 valid)
13:52:18  INFO        [universe] 120/902 (120 valid)
13:52:20  INFO        [universe] 160/902 (160 valid)
13:52:21  INFO        [universe] 200/902 (199 valid)
13:52:29  INFO        [universe] 240/902 (238 valid)
13:52:39  INFO        [universe] 280/902 (278 valid)
13:52:52  INFO        [universe] 320/902 (318 valid)
13:53:03  INFO        [universe] 360/902 (358 valid)
13:53:16  INFO        [universe] 400/902 (397 valid)
13:53:27  INFO        [universe] 440/902 (437 valid)
13:53:40  INFO        [universe] 480/902 (476 valid)
13:53:51  INFO        [universe] 520/902 (516 valid)
13:54:04  INFO        [universe] 560/902 (556 valid)
13:54:15  INFO        [universe] 600/902 (596 valid)
13:54:28  INFO        [universe] 640/902 (636 valid)
13:54:42  INFO        [universe] 680/902 (676 valid)
13:54:52  INFO        [universe] 720/902 (716 valid)
13:55:06  INFO        [universe] 760/902 (756 valid)
13:55:16  INFO        [universe] 800/902 (796 valid)
```

### Options bot full output

```text

## Run 20260818T135626Z

- UTC timestamp: `20260818T135626Z`
- GitHub run: [#7347](https://github.com/28twagg-ops/TradingBot/actions/runs/32145160492)
- Run id: `32145160492`
- Live bot: exit=`0`, duration=`239s`
- Live options: exit=`0`, duration=`0s`
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
13:56:27  INFO      Mode: morning_scan
13:56:28  INFO        [positions] 1/1 (1 valid)
13:56:28  INFO        Universe cache hit: 903 tickers (tickers_2026-08-18.json)
13:56:29  INFO        [universe] 40/902 (40 valid)
13:56:30  INFO        [universe] 80/902 (80 valid)
13:56:32  INFO        [universe] 120/902 (120 valid)
13:56:33  INFO        [universe] 160/902 (160 valid)
13:56:34  INFO        [universe] 200/902 (199 valid)
13:56:42  INFO        [universe] 240/902 (238 valid)
13:56:55  INFO        [universe] 280/902 (278 valid)
13:57:05  INFO        [universe] 320/902 (318 valid)
13:57:19  INFO        [universe] 360/902 (358 valid)
13:57:29  INFO        [universe] 400/902 (397 valid)
13:57:42  INFO        [universe] 440/902 (437 valid)
13:57:53  INFO        [universe] 480/902 (476 valid)
13:58:06  INFO        [universe] 520/902 (516 valid)
13:58:16  INFO        [universe] 560/902 (556 valid)
13:58:30  INFO        [universe] 600/902 (596 valid)
13:58:43  INFO        [universe] 640/902 (636 valid)
13:58:53  INFO        [universe] 680/902 (676 valid)
13:59:06  INFO        [universe] 720/902 (716 valid)
13:59:17  INFO        [universe] 760/902 (756 valid)
13:59:30  INFO        [universe] 800/902 (796 valid)
13:59:40  INFO        [universe] 840/902 (835 valid)
13:59:54  INFO        [universe] 880/902 (875 valid)
14:00:01  INFO        [universe] 902/902 (897 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_SCAN|
|  Time                                                         13:56 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $467.41|
+========================================================================+

+========================================================================+
|                   RUBBER BAND BOT v8  --  DAILY SCAN                   |
+========================================================================+
|  Mode                                                      *** LIVE ***|
|  Date                                                        2026-08-18|
|  Universe                                                          both|
|  Mo~  Aug: VolumeSpike + 52wkLow (display only — schedule not enforced)|
|  Disabled  GapDown, GoldenPocket, VolumeSpike (see DISABLED_STRATEGIES)|
|  Regime                                                            BULL|
|  Exit                                      midline / stop-0.5% / 3d max|
+========================================================================+

+========================================================================+
|                                ACCOUNT                                 |
+========================================================================+
|  Equity                                                         $467.41|
|  Cash                                                           $397.18|
|  Reserve                                          $23.37  (always kept)|
|  Stock ~  $70.23 / $233.71  (50% equity; 50% reserved for live options)|
|  Available                                    $163.47  (new stock buys)|
|  Trade size             $70.11  (15% per signal — all strategies equal)|
+========================================================================+

+========================================================================+
|                           HOLDINGS  (1 open)                           |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AFL      Pullback50      $70.23     $122.53  $122.65  +0.1%   $+0.07  |
|                                                                        |
|  Total invested                                                  $70.23|
|  Total open P&L                                                  $+0.07|
|  Buys today: 0  |  entry cap: 2  |  max open: 3                        |
+========================================================================+

+========================================================================+
|                               PLAN CACHE                               |
+========================================================================+
|  Mode                                                           morning|
|  File                                      logs/plans/morning_plan.json|
|  Use cached plan                                  no (stale (57611.0m))|
+========================================================================+

+========================================================================+
|          EXIT EVALUATION  (EOD -- midline + stop + max-hold)           |
+========================================================================+
|  AFL  P&L +0.1%  $+0.07                                            HOLD|
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
|  Month: Aug  |  Regime: BULL                                           |
|  Primary: VolumeSpike  |  Secondary: 52wkLow (display only — schedule ~|
|  Source                                                       live scan|
+========================================================================+

+========================================================================+
|                         SIGNALS FOUND  --  36                          |
+========================================================================+
|  TICKER   STRATEGY        TIER   PRICE    RSI    VOL_Z   TRIGGER       |
+------------------------------------------------------------------------+
|  AES      Pullback50      eq     $14.77   43.2   -2.17   50MA bounce (+|
|  AEE      Pullback50      eq     $110.89  54.5   -2.22   50MA bounce (-|
|  AON      Pullback50      eq     $349.46  22.2   -1.32   50MA bounce (+|
|  BRK-B    Pullback50      eq     $502.03  40.8   -3.03   50MA bounce (+|
|  CNC      Pullback50      eq     $65.58   58.2   -1.78   50MA bounce (+|
|  CDW      Pullback50      eq     $135.47  37.1   -1.46   50MA bounce (-|
|  CB       Pullback50      eq     $347.43  33.0   -1.93   50MA bounce (+|
|  CHD      Pullback50      eq     $98.99   47.1   -2.32   50MA bounce (+|
|  C        Pullback50      eq     $137.55  74.1   -2.92   50MA bounce (+|
|  CL       Pullback50      eq     $91.79   43.7   -2.56   50MA bounce (+|
|  DDOG     Pullback50      eq     $250.61  45.8   -1.50   50MA bounce (+|
|  DUK      Pullback50      eq     $125.55  39.7   -1.78   50MA bounce (-|
|  ELV      Pullback50      eq     $399.67  66.7   -2.73   50MA bounce (+|
|  EIX      Pullback50      eq     $73.31   37.0   -1.87   50MA bounce (-|
|  ESS      Pullback50      eq     $286.11  38.8   -1.93   50MA bounce (-|
|  EVRG     Pullback50      eq     $84.43   53.1   -2.99   50MA bounce (-|
|  EXC      Pullback50      eq     $46.40   45.1   -1.84   50MA bounce (+|
|  FE       Pullback50      eq     $48.19   39.7   -2.07   50MA bounce (+|
|  HLT      Pullback50      eq     $328.86  56.0   -2.54   50MA bounce (-|
|  INVH     Pullback50      eq     $30.10   49.9   -2.21   50MA bounce (+|
|  KVUE     Pullback50      eq     $19.10   39.2   -2.21   50MA bounce (+|
|  KEY      Pullback50      eq     $23.09   68.4   -2.72   50MA bounce (+|
|  L        Pullback50      eq     $113.71  22.4   -2.71   50MA bounce (+|
|  MU       Pullback50      eq     $962.05  72.8   -2.27   50MA bounce (-|
|  RCL      Pullback50      eq     $299.83  25.0   -1.70   50MA bounce (-|
|  VTRS     Pullback50      eq     $16.49   26.2   -2.36   50MA bounce (-|
|  WRB      Pullback50      eq     $71.08   27.8   -2.72   50MA bounce (+|
|  WM       Pullback50      eq     $227.91  34.2   -2.43   50MA bounce (+|
|  WST      Pullback50      eq     $348.62  64.2   -1.57   50MA bounce (+|
|  BKH      Pullback50      eq     $74.02   55.2   -2.20   50MA bounce (+|
|  BRKR     Pullback50      eq     $58.43   45.0   -1.26   50MA bounce (+|14:00:03  ERROR       BUY FAILED AES: {"code":40010001,"message":"client_order_id must be unique"}
14:00:03  INFO        BUY  AEE  $70.11  [Pullback50]  id=39b58e82-d1e7-4a26-841a-ef4b18554c7e
14:00:03  INFO        BUY  AON  $70.11  [Pullback50]  id=67a83e1b-8d4f-4a90-9eb1-aba0546c6ef2
14:00:25  INFO        place_all_stops: checking 3 positions...
14:00:25  INFO        STOP skipped AEE: fractional (0.6341 shares) — software exit will handle it
14:00:25  INFO        STOP skipped AFL: fractional (0.5726 shares) — software exit will handle it
14:00:25  INFO        STOP skipped AON: fractional (0.2011 shares) — software exit will handle it
14:00:25  INFO        Daily log -> logs/daily/2026-08-18.md
14:00:25  INFO        Dashboard written → logs/dashboard.md

|  GHC      Pullback50      eq     $1180.~  34.0   -2.70   50MA bounce (+|
|  OGE      Pullback50      eq     $47.84   50.6   -2.66   50MA bounce (-|
|  PVH      Pullback50      eq     $79.76   28.4   -2.78   50MA bounce (-|
|  SNX      Pullback50      eq     $260.42  62.6   -1.87   50MA bounce (+|
|  VNOM     Pullback50      eq     $43.43   51.1   -2.30   50MA bounce (+|
|                                                                        |
+========================================================================+

+========================================================================+
|                              ENTRY ORDERS                              |
+========================================================================+
|    ENTER [eq] AES  Pullback50                                    $70.11|
|    ENTER [eq] AEE  Pullback50                                    $70.11|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    ENTER [eq] AON  Pullback50                                    $70.11|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    SKIP [eq] BRK-B  Pullback50                                    cap 3|
|    SKIP [eq] CNC  Pullback50                                      cap 3|
|    SKIP [eq] CDW  Pullback50                                      cap 3|
|    SKIP [eq] CB  Pullback50                                       cap 3|
|    SKIP [eq] CHD  Pullback50                                      cap 3|
|    SKIP [eq] C  Pullback50                                        cap 3|
|    SKIP [eq] CL  Pullback50                                       cap 3|
|    SKIP [eq] DDOG  Pullback50                                     cap 3|
|    SKIP [eq] DUK  Pullback50                                      cap 3|
|    SKIP [eq] ELV  Pullback50                                      cap 3|
|    SKIP [eq] EIX  Pullback50                                      cap 3|
|    SKIP [eq] ESS  Pullback50                                      cap 3|
|    SKIP [eq] EVRG  Pullback50                                     cap 3|
|    SKIP [eq] EXC  Pullback50                                      cap 3|
|    SKIP [eq] FE  Pullback50                                       cap 3|
|    SKIP [eq] HLT  Pullback50                                      cap 3|
|    SKIP [eq] INVH  Pullback50                                     cap 3|
|    SKIP [eq] KVUE  Pullback50                                     cap 3|
|    SKIP [eq] KEY  Pullback50                                      cap 3|
|    SKIP [eq] L  Pullback50                                        cap 3|
|    SKIP [eq] MU  Pullback50                                       cap 3|
|    SKIP [eq] RCL  Pullback50                                      cap 3|
|    SKIP [eq] VTRS  Pullback50                                     cap 3|
|    SKIP [eq] WRB  Pullback50                                      cap 3|
|    SKIP [eq] WM  Pullback50                                       cap 3|
|    SKIP [eq] WST  Pullback50                                      cap 3|
|    SKIP [eq] BKH  Pullback50                                      cap 3|
|    SKIP [eq] BRKR  Pullback50                                     cap 3|
|    SKIP [eq] GHC  Pullback50                                      cap 3|
|    SKIP [eq] OGE  Pullback50                                      cap 3|
|    SKIP [eq] PVH  Pullback50                                      cap 3|
|    SKIP [eq] SNX  Pullback50                                      cap 3|
|    SKIP [eq] VNOM  Pullback50                                     cap 3|

+========================================================================+
|                         BUY FILL CONFIRMATION                          |
+========================================================================+
|  Pending submits                                                      2|
+------------------------------------------------------------------------+
|  AEE                                                  still unconfirmed|
|  AON                                                  still unconfirmed|
+========================================================================+
+========================================================================+

+========================================================================+
|                           GTC STOP PLACEMENT                           |
+========================================================================+
|  Waiting 5s for 2 buy submit(s) to settle...                           |
+========================================================================+

+========================================================================+
|                            SESSION SUMMARY                             |
+========================================================================+
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Strategy  VolumeSpike + 52wkLow (display only — schedule not enforced)|
|  Scanned                                                            897|
|  Signals                                                             36|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  2 unconfirmed|
|  Exits                                                                0|
|  Open pos                                                             3|
|  Equity                                                         $467.24|
|  Cash                                                           $256.98|
+========================================================================+
```

### Live options micro full output

```text
=== options_live_micro LIVE 2026-08-18T10:00:26.145562-04:00 share=50% ===
2026-08-18 10:00:26,145 INFO === options_live_micro LIVE 2026-08-18T10:00:26.145562-04:00 share=50% ===
Live account equity $467.24 cash $256.98 #225458845 options_level=3
2026-08-18 10:00:26,368 INFO Live account equity $467.24 cash $256.98 #225458845 options_level=3
Live micro sleeve $234 (50% of $467) deployed $0 max_prem $75 (paper baseline $75 / tp=+50% sl=-50%)
2026-08-18 10:00:26,668 INFO Live micro sleeve $234 (50% of $467) deployed $0 max_prem $75 (paper baseline $75 / tp=+50% sl=-50%)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-18 10:00:26,669 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 24
2026-08-18 10:00:42,850 INFO Live micro signals: 24
  try S404 100%win/+80%med AFRM
2026-08-18 10:00:42,909 INFO   try S404 100%win/+80%med AFRM
  skip S404 AFRM: no contract under $75
2026-08-18 10:00:43,790 INFO   skip S404 AFRM: no contract under $75
  try S404 100%win/+80%med AMD
2026-08-18 10:00:43,852 INFO   try S404 100%win/+80%med AMD
  skip S404 AMD: no contract under $75
2026-08-18 10:00:45,032 INFO   skip S404 AMD: no contract under $75
  try S404 100%win/+80%med ARM
2026-08-18 10:00:45,092 INFO   try S404 100%win/+80%med ARM
  skip S404 ARM: no contract under $75
2026-08-18 10:00:45,596 INFO   skip S404 ARM: no contract under $75
  try S404 100%win/+80%med AVGO
2026-08-18 10:00:45,654 INFO   try S404 100%win/+80%med AVGO
LIVE BUY S404 100%win AVGO AVGO260821C00412500 limit=0.32 ask=0.33 cost=$33 id=7cb280cf-0448-4fed-8ba5-f1f7b1500d48
2026-08-18 10:00:46,753 INFO LIVE BUY S404 100%win AVGO AVGO260821C00412500 limit=0.32 ask=0.33 cost=$33 id=7cb280cf-0448-4fed-8ba5-f1f7b1500d48
LIVE PROT STOP AVGO260821C00412500 x1 stop=0.16 id=908c8211-a3df-42c5-aaca-255145878623
2026-08-18 10:00:46,953 INFO LIVE PROT STOP AVGO260821C00412500 x1 stop=0.16 id=908c8211-a3df-42c5-aaca-255145878623
Live micro done. open_options=1 lots=1
2026-08-18 10:00:47,019 INFO Live micro done. open_options=1 lots=1
```

### Options bot full output

```text

## Run 20260818T140715Z

- UTC timestamp: `20260818T140715Z`
- GitHub run: [#7349](https://github.com/28twagg-ops/TradingBot/actions/runs/32146166105)
- Run id: `32146166105`
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
14:07:15  INFO      Mode: exits
14:07:16  INFO        Daily log -> logs/daily/2026-08-18.md
14:07:16  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (2 ledger rows)
14:07:16  INFO        place_all_stops: checking 4 positions...
14:07:16  INFO        STOP skipped AEE: fractional (0.6341 shares) — software exit will handle it
14:07:16  INFO        STOP skipped AFL: fractional (0.5726 shares) — software exit will handle it
14:07:16  INFO        STOP skipped AON: fractional (0.2011 shares) — software exit will handle it
14:07:17  INFO        [positions] 3/3 (3 valid)
14:07:17  INFO        Daily log -> logs/daily/2026-08-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:07 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $462.32|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AEE  P&L -0.2%  $-0.14                                            HOLD|
|  AON  P&L +0.1%  $+0.04                                            HOLD|
|  AFL  P&L +0.2%  $+0.12                                            HOLD|
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
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro full output

```text
=== options_live_micro LIVE 2026-08-18T10:07:17.938118-04:00 share=50% ===
2026-08-18 10:07:17,938 INFO === options_live_micro LIVE 2026-08-18T10:07:17.938118-04:00 share=50% ===
Live account equity $462.32 cash $225.93 #225458845 options_level=3
2026-08-18 10:07:18,167 INFO Live account equity $462.32 cash $225.93 #225458845 options_level=3
Live micro: already at max 1 option position
2026-08-18 10:07:18,536 INFO Live micro: already at max 1 option position
Live micro done. open_options=1 lots=1
2026-08-18 10:07:18,740 INFO Live micro done. open_options=1 lots=1
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=43 paper_keys=yes dry_run=False
  alpaca positions=15
  FLAG b793|S399|da035398 missing from Alpaca
  FLAG b792|S399|f60fbedb missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-18T10:07:20.404178-04:00 ===

[Run context]
2026-08-18 10:07:20,595 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-18 10:07:28,656 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-18 10:07:44,721 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
2026-08-18 10:08:08,791 WARNING paper get_account failed attempt 4/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 32s
2026-08-18 10:08:40,853 WARNING paper get_account failed attempt 5/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 40s
2026-08-18 10:09:20,934 ERROR paper get_account failed after 6 attempts: {"code":50010000,"message":"internal server error occurred"}
WARN: get_account failed ({"code":50010000,"message":"internal server error occurred"}) but positions OK (n=15). Keys are fine; Alpaca account endpoint is flaky. Continuing manage/exits; skipping new entries until equity is readable.
2026-08-18 10:09:21,103 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-18 10:09:29,171 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-18 10:09:45,237 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
2026-08-18 10:10:09,302 WARNING paper get_account failed attempt 4/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 32s
2026-08-18 10:10:41,367 WARNING paper get_account failed attempt 5/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 40s
```

---

## Run 20260818T141145Z

- UTC timestamp: `20260818T141145Z`
- GitHub run: [#7350](https://github.com/28twagg-ops/TradingBot/actions/runs/32146672124)
- Run id: `32146672124`
- Live bot: exit=`0`, duration=`3s`
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
14:11:46  INFO      Mode: exits
14:11:47  INFO        Daily log -> logs/daily/2026-08-18.md
14:11:47  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (2 ledger rows)
14:11:47  INFO        place_all_stops: checking 4 positions...
14:11:47  INFO        STOP skipped AEE: fractional (0.6341 shares) — software exit will handle it
14:11:47  INFO        STOP skipped AFL: fractional (0.5726 shares) — software exit will handle it
14:11:47  INFO        STOP skipped AON: fractional (0.2011 shares) — software exit will handle it
14:11:47  INFO        [positions] 3/3 (3 valid)
14:11:47  INFO        Daily log -> logs/daily/2026-08-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $458.12|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AEE  P&L -0.3%  $-0.19                                            HOLD|
|  AON  P&L -0.1%  $-0.06                                            HOLD|
|  AFL  P&L +0.1%  $+0.08                                            HOLD|
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
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro full output

```text
=== options_live_micro LIVE 2026-08-18T10:11:48.737513-04:00 share=50% ===
2026-08-18 10:11:48,737 INFO === options_live_micro LIVE 2026-08-18T10:11:48.737513-04:00 share=50% ===
Live account equity $458.12 cash $225.93 #225458845 options_level=3
2026-08-18 10:11:49,157 INFO Live account equity $458.12 cash $225.93 #225458845 options_level=3
Live micro: already at max 1 option position
2026-08-18 10:11:49,392 INFO Live micro: already at max 1 option position
Live micro done. open_options=1 lots=1
2026-08-18 10:11:49,504 INFO Live micro done. open_options=1 lots=1
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=43 paper_keys=yes dry_run=False
  alpaca positions=15
  FLAG b793|S399|da035398 missing from Alpaca
  FLAG b792|S399|f60fbedb missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-18T10:11:51.485521-04:00 ===

[Run context]
2026-08-18 10:11:51,650 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-18 10:11:59,705 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-18 10:12:15,756 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
2026-08-18 10:12:39,823 WARNING paper get_account failed attempt 4/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 32s
2026-08-18 10:13:11,874 WARNING paper get_account failed attempt 5/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 40s
2026-08-18 10:13:51,955 ERROR paper get_account failed after 6 attempts: {"code":50010000,"message":"internal server error occurred"}
WARN: get_account failed ({"code":50010000,"message":"internal server error occurred"}) but positions OK (n=15). Keys are fine; Alpaca account endpoint is flaky. Continuing manage/exits; skipping new entries until equity is readable.
2026-08-18 10:13:52,069 WARNING paper get_account failed attempt 1/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 8s
2026-08-18 10:14:00,158 WARNING paper get_account failed attempt 2/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 16s
2026-08-18 10:14:16,290 WARNING paper get_account failed attempt 3/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 24s
2026-08-18 10:14:40,361 WARNING paper get_account failed attempt 4/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 32s
2026-08-18 10:15:12,418 WARNING paper get_account failed attempt 5/6 (transient): {"code":50010000,"message":"internal server error occurred"}; sleep 40s
```

---

## Run 20260818T141631Z

- UTC timestamp: `20260818T141631Z`
- GitHub run: [#7351](https://github.com/28twagg-ops/TradingBot/actions/runs/32147174839)
- Run id: `32147174839`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`2s`
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
14:16:32  INFO      Mode: exits
14:16:33  INFO        Daily log -> logs/daily/2026-08-18.md
14:16:33  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (2 ledger rows)
14:16:33  INFO        place_all_stops: checking 4 positions...
14:16:33  INFO        STOP skipped AEE: fractional (0.6341 shares) — software exit will handle it
14:16:33  INFO        STOP skipped AFL: fractional (0.5726 shares) — software exit will handle it
14:16:33  INFO        STOP skipped AON: fractional (0.2011 shares) — software exit will handle it
14:16:33  INFO        [positions] 3/3 (3 valid)
14:16:33  INFO        Daily log -> logs/daily/2026-08-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $458.20|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AEE  P&L -0.2%  $-0.16                                            HOLD|
|  AFL  P&L +0.0%  $+0.03                                            HOLD|
|  AON  P&L +0.1%  $+0.05                                            HOLD|
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
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro full output

```text
=== options_live_micro LIVE 2026-08-18T10:16:34.420460-04:00 share=50% ===
2026-08-18 10:16:34,420 INFO === options_live_micro LIVE 2026-08-18T10:16:34.420460-04:00 share=50% ===
Live account equity $458.21 cash $225.93 #225458845 options_level=3
2026-08-18 10:16:34,663 INFO Live account equity $458.21 cash $225.93 #225458845 options_level=3
Live micro: already at max 1 option position
2026-08-18 10:16:35,053 INFO Live micro: already at max 1 option position
Live micro done. open_options=1 lots=1
2026-08-18 10:16:35,277 INFO Live micro done. open_options=1 lots=1
```

### Options bot full output

```text

## Run 20260818T142108Z

- UTC timestamp: `20260818T142108Z`
- GitHub run: [#7352](https://github.com/28twagg-ops/TradingBot/actions/runs/32147684508)
- Run id: `32147684508`
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
14:21:09  INFO      Mode: exits
14:21:09  INFO        Daily log -> logs/daily/2026-08-18.md
14:21:09  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (2 ledger rows)
14:21:09  INFO        place_all_stops: checking 4 positions...
14:21:09  INFO        STOP skipped AEE: fractional (0.6341 shares) — software exit will handle it
14:21:09  INFO        STOP skipped AFL: fractional (0.5726 shares) — software exit will handle it
14:21:09  INFO        STOP skipped AON: fractional (0.2011 shares) — software exit will handle it
14:21:10  INFO        [positions] 3/3 (3 valid)
14:21:10  INFO        Daily log -> logs/daily/2026-08-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $458.00|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AEE  P&L -0.3%  $-0.19                                            HOLD|
|  AON  P&L -0.1%  $-0.09                                            HOLD|
|  AFL  P&L -0.0%  $-0.02                                            HOLD|
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
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro full output

```text
=== options_live_micro LIVE 2026-08-18T10:21:11.133939-04:00 share=50% ===
2026-08-18 10:21:11,134 INFO === options_live_micro LIVE 2026-08-18T10:21:11.133939-04:00 share=50% ===
Live account equity $457.98 cash $225.93 #225458845 options_level=3
2026-08-18 10:21:11,281 INFO Live account equity $457.98 cash $225.93 #225458845 options_level=3
Live micro: already at max 1 option position
2026-08-18 10:21:11,519 INFO Live micro: already at max 1 option position
Live micro done. open_options=1 lots=1
2026-08-18 10:21:11,643 INFO Live micro done. open_options=1 lots=1
```

### Options bot full output

```text

## Run 20260818T142559Z

- UTC timestamp: `20260818T142559Z`
- GitHub run: [#7353](https://github.com/28twagg-ops/TradingBot/actions/runs/32148188580)
- Run id: `32148188580`
- Live bot: exit=`0`, duration=`4s`
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
14:26:00  INFO      Mode: exits
14:26:01  INFO        Daily log -> logs/daily/2026-08-18.md
14:26:01  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (2 ledger rows)
14:26:01  INFO        place_all_stops: checking 4 positions...
14:26:01  INFO        STOP skipped AEE: fractional (0.6341 shares) — software exit will handle it
14:26:01  INFO        STOP skipped AFL: fractional (0.5726 shares) — software exit will handle it
14:26:01  INFO        STOP skipped AON: fractional (0.2011 shares) — software exit will handle it
14:26:02  INFO        [positions] 3/3 (3 valid)
14:26:02  INFO        Daily log -> logs/daily/2026-08-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $455.91|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AEE  P&L -0.4%  $-0.26                                            HOLD|
|  AFL  P&L -0.1%  $-0.07                                            HOLD|
|  AON  P&L -0.1%  $-0.05                                            HOLD|
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
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro full output

```text
=== options_live_micro LIVE 2026-08-18T10:26:03.737814-04:00 share=50% ===
2026-08-18 10:26:03,737 INFO === options_live_micro LIVE 2026-08-18T10:26:03.737814-04:00 share=50% ===
Live account equity $455.91 cash $225.93 #225458845 options_level=3
2026-08-18 10:26:03,961 INFO Live account equity $455.91 cash $225.93 #225458845 options_level=3
Live micro: already at max 1 option position
2026-08-18 10:26:04,371 INFO Live micro: already at max 1 option position
Live micro done. open_options=1 lots=1
2026-08-18 10:26:04,606 INFO Live micro done. open_options=1 lots=1
```

### Options bot full output

```text

## Run 20260818T144104Z

- UTC timestamp: `20260818T144104Z`
- GitHub run: [#7356](https://github.com/28twagg-ops/TradingBot/actions/runs/32149727734)
- Run id: `32149727734`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`2s`
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
14:41:06  INFO      Mode: exits
14:41:07  INFO        Daily log -> logs/daily/2026-08-18.md
14:41:07  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (2 ledger rows)
14:41:07  INFO        place_all_stops: checking 4 positions...
14:41:07  INFO        STOP skipped AEE: fractional (0.6341 shares) — software exit will handle it
14:41:07  INFO        STOP skipped AFL: fractional (0.5726 shares) — software exit will handle it
14:41:07  INFO        STOP skipped AON: fractional (0.2011 shares) — software exit will handle it
14:41:07  INFO        [positions] 3/3 (3 valid)
14:41:07  INFO        Daily log -> logs/daily/2026-08-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $457.75|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AEE  P&L -0.4%  $-0.26                                            HOLD|
|  AON  P&L -0.2%  $-0.16                                            HOLD|
|  AFL  P&L -0.2%  $-0.12                                            HOLD|
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
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro full output

```text
=== options_live_micro LIVE 2026-08-18T10:41:08.829326-04:00 share=50% ===
2026-08-18 10:41:08,829 INFO === options_live_micro LIVE 2026-08-18T10:41:08.829326-04:00 share=50% ===
Live account equity $457.75 cash $225.93 #225458845 options_level=3
2026-08-18 10:41:09,383 INFO Live account equity $457.75 cash $225.93 #225458845 options_level=3
Live micro: already at max 1 option position
2026-08-18 10:41:09,772 INFO Live micro: already at max 1 option position
Live micro done. open_options=1 lots=1
2026-08-18 10:41:09,990 INFO Live micro done. open_options=1 lots=1
```

### Options bot full output

```text

## Run 20260818T144552Z

- UTC timestamp: `20260818T144552Z`
- GitHub run: [#7357](https://github.com/28twagg-ops/TradingBot/actions/runs/32150243532)
- Run id: `32150243532`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`0s`

### Live bot full output

```text
14:45:53  INFO      Mode: exits
14:45:54  INFO        Daily log -> logs/daily/2026-08-18.md
14:45:54  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (2 ledger rows)
14:45:54  INFO        place_all_stops: checking 4 positions...
14:45:54  INFO        STOP skipped AEE: fractional (0.6341 shares) — software exit will handle it
14:45:54  INFO        STOP skipped AFL: fractional (0.5726 shares) — software exit will handle it
14:45:54  INFO        STOP skipped AON: fractional (0.2011 shares) — software exit will handle it
14:45:54  INFO        [positions] 3/3 (3 valid)
14:45:54  INFO        Daily log -> logs/daily/2026-08-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:45 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $458.02|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AEE  P&L -0.3%  $-0.20                                            HOLD|
|  AFL  P&L -0.1%  $-0.08                                            HOLD|
|  AON  P&L +0.0%  $+0.01                                            HOLD|
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
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro full output

```text
=== options_live_micro LIVE 2026-08-18T10:45:55.396003-04:00 share=50% ===
2026-08-18 10:45:55,396 INFO === options_live_micro LIVE 2026-08-18T10:45:55.396003-04:00 share=50% ===
Live account equity $458.04 cash $225.93 #225458845 options_level=3
2026-08-18 10:45:55,570 INFO Live account equity $458.04 cash $225.93 #225458845 options_level=3
Live micro hold S404 AVGO260821C00412500 -29.0% (tp +50% / sl -50%)
2026-08-18 10:45:55,669 INFO Live micro hold S404 AVGO260821C00412500 -29.0% (tp +50% / sl -50%)
Live micro: already at max 1 option position
2026-08-18 10:45:55,804 INFO Live micro: already at max 1 option position
Live micro done. open_options=1 lots=1
2026-08-18 10:45:55,939 INFO Live micro done. open_options=1 lots=1
```

### Paper options bot full output

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T145100Z

- UTC timestamp: `20260818T145100Z`
- GitHub run: [#7358](https://github.com/28twagg-ops/TradingBot/actions/runs/32150752851)
- Run id: `32150752851`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`

### Live bot full output

```text
14:51:01  INFO      Mode: exits
14:51:02  INFO        Daily log -> logs/daily/2026-08-18.md
14:51:02  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (2 ledger rows)
14:51:02  INFO        place_all_stops: checking 4 positions...
14:51:02  INFO        STOP skipped AEE: fractional (0.6341 shares) — software exit will handle it
14:51:02  INFO        STOP skipped AFL: fractional (0.5726 shares) — software exit will handle it
14:51:02  INFO        STOP skipped AON: fractional (0.2011 shares) — software exit will handle it
14:51:02  INFO        [positions] 3/3 (3 valid)
14:51:03  INFO        Daily log -> logs/daily/2026-08-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:51 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $457.87|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AEE  P&L -0.4%  $-0.27                                            HOLD|
|  AFL  P&L -0.1%  $-0.09                                            HOLD|
|  AON  P&L -0.1%  $-0.04                                            HOLD|
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
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00412500     $0.31    $0.22    -29.0%   $-9.00    $22.00   |
|                                                                        |
|  Options open P&L                                                $-9.00|
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

### Live options micro full output

```text
=== options_live_micro LIVE 2026-08-18T10:51:03.886402-04:00 share=50% ===
2026-08-18 10:51:03,886 INFO === options_live_micro LIVE 2026-08-18T10:51:03.886402-04:00 share=50% ===
Live account equity $457.89 cash $225.93 #225458845 options_level=3
2026-08-18 10:51:04,120 INFO Live account equity $457.89 cash $225.93 #225458845 options_level=3
Live micro hold S404 AVGO260821C00412500 -29.0% (tp +50% / sl -50%)
2026-08-18 10:51:04,275 INFO Live micro hold S404 AVGO260821C00412500 -29.0% (tp +50% / sl -50%)
Live micro: at max 1 option — manage/exits only (no new buys)
2026-08-18 10:51:04,479 INFO Live micro: at max 1 option — manage/exits only (no new buys)
Live micro done. open_options=1 lots=1
2026-08-18 10:51:04,546 INFO Live micro done. open_options=1 lots=1
```

### Paper options bot full output

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T145549Z

- UTC timestamp: `20260818T145549Z`
- GitHub run: [#7359](https://github.com/28twagg-ops/TradingBot/actions/runs/32151260816)
- Run id: `32151260816`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`12s`
- Paper options: exit=`0`, duration=`0s`

### Live bot full output

```text
14:55:50  INFO      Mode: exits
14:55:51  INFO        Daily log -> logs/daily/2026-08-18.md
14:55:51  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (2 ledger rows)
14:55:51  INFO        place_all_stops: checking 4 positions...
14:55:51  INFO        STOP skipped AEE: fractional (0.6341 shares) — software exit will handle it
14:55:51  INFO        STOP skipped AFL: fractional (0.5726 shares) — software exit will handle it
14:55:51  INFO        STOP skipped AON: fractional (0.2011 shares) — software exit will handle it
14:55:51  INFO        [positions] 3/3 (3 valid)
14:55:51  INFO        Daily log -> logs/daily/2026-08-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:55 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $458.05|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AEE  P&L -0.2%  $-0.14                                            HOLD|
|  AFL  P&L -0.1%  $-0.08                                            HOLD|
|  AON  P&L -0.0%  $-0.03                                            HOLD|
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
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00412500     $0.31    $0.22    -29.0%   $-9.00    $22.00   |
|                                                                        |
|  Options open P&L                                                $-9.00|
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

### Live options micro full output

```text
=== options_live_micro LIVE 2026-08-18T10:55:52.552675-04:00 share=50% ===
2026-08-18 10:55:52,552 INFO === options_live_micro LIVE 2026-08-18T10:55:52.552675-04:00 share=50% ===
Live account equity $458.04 cash $225.93 #225458845 options_level=3
2026-08-18 10:55:52,655 INFO Live account equity $458.04 cash $225.93 #225458845 options_level=3
Live micro hold S404 AVGO260821C00412500 -29.0% (tp +50% / sl -50%)
2026-08-18 10:55:52,789 INFO Live micro hold S404 AVGO260821C00412500 -29.0% (tp +50% / sl -50%)
Live micro sleeve $229 (50% of $458) deployed $22 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
2026-08-18 10:55:52,898 INFO Live micro sleeve $229 (50% of $458) deployed $22 open_strategies=1/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-18 10:55:52,898 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 22
2026-08-18 10:56:02,029 INFO Live micro signals: 22
  skip S404 AFRM: strategy already open (paper bucket rule)
2026-08-18 10:56:02,030 INFO   skip S404 AFRM: strategy already open (paper bucket rule)
  skip S404 AMD: strategy already open (paper bucket rule)
2026-08-18 10:56:02,030 INFO   skip S404 AMD: strategy already open (paper bucket rule)
  skip S404 ARM: strategy already open (paper bucket rule)
2026-08-18 10:56:02,030 INFO   skip S404 ARM: strategy already open (paper bucket rule)
  skip S404 AVGO: strategy already open (paper bucket rule)
2026-08-18 10:56:02,030 INFO   skip S404 AVGO: strategy already open (paper bucket rule)
  skip S404 CAT: strategy already open (paper bucket rule)
2026-08-18 10:56:02,030 INFO   skip S404 CAT: strategy already open (paper bucket rule)
  skip S404 CVNA: strategy already open (paper bucket rule)
2026-08-18 10:56:02,030 INFO   skip S404 CVNA: strategy already open (paper bucket rule)
  skip S404 DOCN: strategy already open (paper bucket rule)
2026-08-18 10:56:02,030 INFO   skip S404 DOCN: strategy already open (paper bucket rule)
  skip S404 HOOD: strategy already open (paper bucket rule)
2026-08-18 10:56:02,031 INFO   skip S404 HOOD: strategy already open (paper bucket rule)
  skip S404 MARA: strategy already open (paper bucket rule)
2026-08-18 10:56:02,031 INFO   skip S404 MARA: strategy already open (paper bucket rule)
  skip S404 META: strategy already open (paper bucket rule)
2026-08-18 10:56:02,031 INFO   skip S404 META: strategy already open (paper bucket rule)
  skip S404 NVDA: strategy already open (paper bucket rule)
2026-08-18 10:56:02,031 INFO   skip S404 NVDA: strategy already open (paper bucket rule)
  skip S404 PATH: strategy already open (paper bucket rule)
2026-08-18 10:56:02,031 INFO   skip S404 PATH: strategy already open (paper bucket rule)
  skip S404 SMCI: strategy already open (paper bucket rule)
2026-08-18 10:56:02,031 INFO   skip S404 SMCI: strategy already open (paper bucket rule)
  skip S404 UPST: strategy already open (paper bucket rule)
2026-08-18 10:56:02,031 INFO   skip S404 UPST: strategy already open (paper bucket rule)
  try S406 56%win/+58%med AFRM
2026-08-18 10:56:02,031 INFO   try S406 56%win/+58%med AFRM
  skip S406 AFRM: no contract under $75
2026-08-18 10:56:02,384 INFO   skip S406 AFRM: no contract under $75
  try S406 56%win/+58%med TSLA
2026-08-18 10:56:02,384 INFO   try S406 56%win/+58%med TSLA
LIVE BUY S406 56%win TSLA TSLA260821C00357500 limit=0.62 ask=0.63 cost=$63 id=334c6131-c884-4578-a9bb-9d8db19169f5
2026-08-18 10:56:02,929 INFO LIVE BUY S406 56%win TSLA TSLA260821C00357500 limit=0.62 ask=0.63 cost=$63 id=334c6131-c884-4578-a9bb-9d8db19169f5
  try S218 56%win/+49%med NKE
2026-08-18 10:56:02,929 INFO   try S218 56%win/+49%med NKE
LIVE BUY S218 56%win NKE NKE260821C00040000 limit=0.54 ask=0.55 cost=$55 id=6fe24f90-9d69-4165-858a-275b5e90e561
2026-08-18 10:56:03,245 INFO LIVE BUY S218 56%win NKE NKE260821C00040000 limit=0.54 ask=0.55 cost=$55 id=6fe24f90-9d69-4165-858a-275b5e90e561
  skip S218 PG: strategy already open (paper bucket rule)
2026-08-18 10:56:03,246 INFO   skip S218 PG: strategy already open (paper bucket rule)
  try S210 55%win/+47%med AXP
2026-08-18 10:56:03,246 INFO   try S210 55%win/+47%med AXP
  skip S210 AXP: no contract under $75
2026-08-18 10:56:03,500 INFO   skip S210 AXP: no contract under $75
  try S210 55%win/+47%med CELH
2026-08-18 10:56:03,500 INFO   try S210 55%win/+47%med CELH
LIVE BUY S210 55%win CELH CELH260821C00030000 limit=0.71 ask=0.72 cost=$72 id=accf9428-a2cf-4585-9e23-cd6ea4481ce5
2026-08-18 10:56:03,816 INFO LIVE BUY S210 55%win CELH CELH260821C00030000 limit=0.71 ask=0.72 cost=$72 id=accf9428-a2cf-4585-9e23-cd6ea4481ce5
  skip S210 HOOD: strategy already open (paper bucket rule)
2026-08-18 10:56:03,816 INFO   skip S210 HOOD: strategy already open (paper bucket rule)
  skip S210 UNP: strategy already open (paper bucket rule)
2026-08-18 10:56:03,816 INFO   skip S210 UNP: strategy already open (paper bucket rule)
Live micro done. open_options=2 lots=4
2026-08-18 10:56:03,898 INFO Live micro done. open_options=2 lots=4
```

### Paper options bot full output

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T150057Z

- UTC timestamp: `20260818T150057Z`
- GitHub run: [#7360](https://github.com/28twagg-ops/TradingBot/actions/runs/32151783835)
- Run id: `32151783835`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`20s`
- Paper options: exit=`0`, duration=`0s`

### Live bot full output

```text
15:00:58  INFO      Mode: exits
15:00:58  INFO        Daily log -> logs/daily/2026-08-18.md
15:00:58  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (2 ledger rows)
15:00:58  INFO        place_all_stops: checking 6 positions...
15:00:58  INFO        STOP skipped AEE: fractional (0.6341 shares) — software exit will handle it
15:00:58  INFO        STOP skipped AFL: fractional (0.5726 shares) — software exit will handle it
15:00:58  INFO        STOP skipped AON: fractional (0.2011 shares) — software exit will handle it
15:00:59  INFO        [positions] 3/3 (3 valid)
15:00:59  INFO        Daily log -> logs/daily/2026-08-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:00 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $440.94|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AEE  P&L -0.2%  $-0.16                                            HOLD|
|  AFL  P&L -0.2%  $-0.13                                            HOLD|
|  AON  P&L +0.0%  $+0.02                                            HOLD|
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
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00412500     $0.31    $0.19    -38.7%   $-12.00   $19.00   |
|  CELH260821C00030000     $0.70    $0.60    -14.3%   $-10.00   $60.00   |
|  TSLA260821C00357500     $0.62    $0.59    -4.8%    $-3.00    $59.00   |
|                                                                        |
|  Options open P&L                                               $-25.00|
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

### Live options micro full output

```text
=== options_live_micro LIVE 2026-08-18T11:01:00.063986-04:00 share=50% ===
2026-08-18 11:01:00,064 INFO === options_live_micro LIVE 2026-08-18T11:01:00.063986-04:00 share=50% ===
Live account equity $441.95 cash $93.84 #225458845 options_level=3
2026-08-18 11:01:00,246 INFO Live account equity $441.95 cash $93.84 #225458845 options_level=3
Live micro hold S404 AVGO260821C00412500 -38.7% (tp +50% / sl -50%)
2026-08-18 11:01:00,312 INFO Live micro hold S404 AVGO260821C00412500 -38.7% (tp +50% / sl -50%)
Live micro hold S406 TSLA260821C00357500 -4.8% (tp +50% / sl -50%)
2026-08-18 11:01:00,312 INFO Live micro hold S406 TSLA260821C00357500 -4.8% (tp +50% / sl -50%)
Live micro hold S210 CELH260821C00030000 -14.3% (tp +50% / sl -50%)
2026-08-18 11:01:00,312 INFO Live micro hold S210 CELH260821C00030000 -14.3% (tp +50% / sl -50%)
LIVE PROT STOP TSLA260821C00357500 x1 stop=0.31 id=8b5dcf74-248a-4a93-931f-1eb358c64ed8
2026-08-18 11:01:00,381 INFO LIVE PROT STOP TSLA260821C00357500 x1 stop=0.31 id=8b5dcf74-248a-4a93-931f-1eb358c64ed8
LIVE PROT STOP CELH260821C00030000 x1 stop=0.35 id=8917116c-360a-4e67-997d-78def9d6d9a2
2026-08-18 11:01:00,408 INFO LIVE PROT STOP CELH260821C00030000 x1 stop=0.35 id=8917116c-360a-4e67-997d-78def9d6d9a2
Live micro sleeve $221 (50% of $442) deployed $138 open_strategies=4/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
2026-08-18 11:01:00,427 INFO Live micro sleeve $221 (50% of $442) deployed $138 open_strategies=4/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-18 11:01:00,427 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 22
2026-08-18 11:01:19,587 INFO Live micro signals: 22
  skip S404 AFRM: strategy already open (paper bucket rule)
2026-08-18 11:01:19,588 INFO   skip S404 AFRM: strategy already open (paper bucket rule)
  skip S404 AMD: strategy already open (paper bucket rule)
2026-08-18 11:01:19,588 INFO   skip S404 AMD: strategy already open (paper bucket rule)
  skip S404 ARM: strategy already open (paper bucket rule)
2026-08-18 11:01:19,588 INFO   skip S404 ARM: strategy already open (paper bucket rule)
  skip S404 AVGO: strategy already open (paper bucket rule)
2026-08-18 11:01:19,588 INFO   skip S404 AVGO: strategy already open (paper bucket rule)
  skip S404 CAT: strategy already open (paper bucket rule)
2026-08-18 11:01:19,588 INFO   skip S404 CAT: strategy already open (paper bucket rule)
  skip S404 CVNA: strategy already open (paper bucket rule)
2026-08-18 11:01:19,588 INFO   skip S404 CVNA: strategy already open (paper bucket rule)
  skip S404 DOCN: strategy already open (paper bucket rule)
2026-08-18 11:01:19,588 INFO   skip S404 DOCN: strategy already open (paper bucket rule)
  skip S404 HOOD: strategy already open (paper bucket rule)
2026-08-18 11:01:19,589 INFO   skip S404 HOOD: strategy already open (paper bucket rule)
  skip S404 MARA: strategy already open (paper bucket rule)
2026-08-18 11:01:19,589 INFO   skip S404 MARA: strategy already open (paper bucket rule)
  skip S404 META: strategy already open (paper bucket rule)
2026-08-18 11:01:19,589 INFO   skip S404 META: strategy already open (paper bucket rule)
  skip S404 NVDA: strategy already open (paper bucket rule)
2026-08-18 11:01:19,589 INFO   skip S404 NVDA: strategy already open (paper bucket rule)
  skip S404 PATH: strategy already open (paper bucket rule)
2026-08-18 11:01:19,589 INFO   skip S404 PATH: strategy already open (paper bucket rule)
  skip S404 SMCI: strategy already open (paper bucket rule)
2026-08-18 11:01:19,589 INFO   skip S404 SMCI: strategy already open (paper bucket rule)
  skip S404 UPST: strategy already open (paper bucket rule)
2026-08-18 11:01:19,589 INFO   skip S404 UPST: strategy already open (paper bucket rule)
  skip S406 AFRM: strategy already open (paper bucket rule)
2026-08-18 11:01:19,589 INFO   skip S406 AFRM: strategy already open (paper bucket rule)
  skip S406 PATH: strategy already open (paper bucket rule)
2026-08-18 11:01:19,589 INFO   skip S406 PATH: strategy already open (paper bucket rule)
  skip S218 NKE: strategy already open (paper bucket rule)
2026-08-18 11:01:19,589 INFO   skip S218 NKE: strategy already open (paper bucket rule)
  skip S218 PG: strategy already open (paper bucket rule)
2026-08-18 11:01:19,590 INFO   skip S218 PG: strategy already open (paper bucket rule)
  skip S210 AXP: strategy already open (paper bucket rule)
2026-08-18 11:01:19,590 INFO   skip S210 AXP: strategy already open (paper bucket rule)
  skip S210 CELH: strategy already open (paper bucket rule)
2026-08-18 11:01:19,590 INFO   skip S210 CELH: strategy already open (paper bucket rule)
  skip S210 HOOD: strategy already open (paper bucket rule)
2026-08-18 11:01:19,590 INFO   skip S210 HOOD: strategy already open (paper bucket rule)
  skip S210 UNP: strategy already open (paper bucket rule)
2026-08-18 11:01:19,590 INFO   skip S210 UNP: strategy already open (paper bucket rule)
Live micro done. open_options=3 lots=4
2026-08-18 11:01:19,648 INFO Live micro done. open_options=3 lots=4
```

### Paper options bot full output

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T151205Z

- UTC timestamp: `20260818T151205Z`
- GitHub run: [#7362](https://github.com/28twagg-ops/TradingBot/actions/runs/32152795649)
- Run id: `32152795649`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`12s`
- Paper options: exit=`0`, duration=`0s`

### Live bot full output

```text
15:12:06  INFO      Mode: exits
15:12:06  INFO        Daily log -> logs/daily/2026-08-18.md
15:12:06  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (2 ledger rows)
15:12:06  INFO        place_all_stops: checking 6 positions...
15:12:06  INFO        STOP skipped AEE: fractional (0.6341 shares) — software exit will handle it
15:12:06  INFO        STOP skipped AFL: fractional (0.5726 shares) — software exit will handle it
15:12:06  INFO        STOP skipped AON: fractional (0.2011 shares) — software exit will handle it
15:12:07  INFO        [positions] 3/3 (3 valid)
15:12:07  INFO        Daily log -> logs/daily/2026-08-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:12 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $442.11|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AFL  P&L -0.1%  $-0.08                                            HOLD|
|  AEE  P&L -0.1%  $-0.06                                            HOLD|
|  AON  P&L +0.1%  $+0.05                                            HOLD|
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
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00412500     $0.31    $0.19    -38.7%   $-12.00   $19.00   |
|  CELH260821C00030000     $0.70    $0.56    -20.0%   $-14.00   $56.00   |
|  TSLA260821C00357500     $0.62    $0.63    +1.6%    $+1.00    $63.00   |
|                                                                        |
|  Options open P&L                                               $-25.00|
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

### Live options micro full output

```text
=== options_live_micro LIVE 2026-08-18T11:12:08.194460-04:00 share=50% ===
2026-08-18 11:12:08,194 INFO === options_live_micro LIVE 2026-08-18T11:12:08.194460-04:00 share=50% ===
Live account equity $442.11 cash $93.84 #225458845 options_level=3
2026-08-18 11:12:08,240 INFO Live account equity $442.11 cash $93.84 #225458845 options_level=3
Live micro hold S404 AVGO260821C00412500 -38.7% (tp +50% / sl -50%)
2026-08-18 11:12:08,269 INFO Live micro hold S404 AVGO260821C00412500 -38.7% (tp +50% / sl -50%)
Live micro hold S406 TSLA260821C00357500 +1.6% (tp +50% / sl -50%)
2026-08-18 11:12:08,269 INFO Live micro hold S406 TSLA260821C00357500 +1.6% (tp +50% / sl -50%)
Live micro hold S210 CELH260821C00030000 -20.0% (tp +50% / sl -50%)
2026-08-18 11:12:08,269 INFO Live micro hold S210 CELH260821C00030000 -20.0% (tp +50% / sl -50%)
Live micro sleeve $221 (50% of $442) deployed $138 open_strategies=4/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
2026-08-18 11:12:08,334 INFO Live micro sleeve $221 (50% of $442) deployed $138 open_strategies=4/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-18 11:12:08,334 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 24
2026-08-18 11:12:19,752 INFO Live micro signals: 24
  skip S404 AFRM: strategy already open (paper bucket rule)
2026-08-18 11:12:19,753 INFO   skip S404 AFRM: strategy already open (paper bucket rule)
  skip S404 AMD: strategy already open (paper bucket rule)
2026-08-18 11:12:19,753 INFO   skip S404 AMD: strategy already open (paper bucket rule)
  skip S404 ARM: strategy already open (paper bucket rule)
2026-08-18 11:12:19,753 INFO   skip S404 ARM: strategy already open (paper bucket rule)
  skip S404 AVGO: strategy already open (paper bucket rule)
2026-08-18 11:12:19,753 INFO   skip S404 AVGO: strategy already open (paper bucket rule)
  skip S404 CAT: strategy already open (paper bucket rule)
2026-08-18 11:12:19,753 INFO   skip S404 CAT: strategy already open (paper bucket rule)
  skip S404 CVNA: strategy already open (paper bucket rule)
2026-08-18 11:12:19,753 INFO   skip S404 CVNA: strategy already open (paper bucket rule)
  skip S404 DOCN: strategy already open (paper bucket rule)
2026-08-18 11:12:19,753 INFO   skip S404 DOCN: strategy already open (paper bucket rule)
  skip S404 HOOD: strategy already open (paper bucket rule)
2026-08-18 11:12:19,753 INFO   skip S404 HOOD: strategy already open (paper bucket rule)
  skip S404 MARA: strategy already open (paper bucket rule)
2026-08-18 11:12:19,754 INFO   skip S404 MARA: strategy already open (paper bucket rule)
  skip S404 META: strategy already open (paper bucket rule)
2026-08-18 11:12:19,754 INFO   skip S404 META: strategy already open (paper bucket rule)
  skip S404 NVDA: strategy already open (paper bucket rule)
2026-08-18 11:12:19,754 INFO   skip S404 NVDA: strategy already open (paper bucket rule)
  skip S404 PATH: strategy already open (paper bucket rule)
2026-08-18 11:12:19,754 INFO   skip S404 PATH: strategy already open (paper bucket rule)
  skip S404 SMCI: strategy already open (paper bucket rule)
2026-08-18 11:12:19,754 INFO   skip S404 SMCI: strategy already open (paper bucket rule)
  skip S404 UPST: strategy already open (paper bucket rule)
2026-08-18 11:12:19,754 INFO   skip S404 UPST: strategy already open (paper bucket rule)
  skip S406 AFRM: strategy already open (paper bucket rule)
2026-08-18 11:12:19,754 INFO   skip S406 AFRM: strategy already open (paper bucket rule)
  skip S406 META: strategy already open (paper bucket rule)
2026-08-18 11:12:19,754 INFO   skip S406 META: strategy already open (paper bucket rule)
  skip S406 PATH: strategy already open (paper bucket rule)
2026-08-18 11:12:19,755 INFO   skip S406 PATH: strategy already open (paper bucket rule)
  skip S406 TSLA: strategy already open (paper bucket rule)
2026-08-18 11:12:19,755 INFO   skip S406 TSLA: strategy already open (paper bucket rule)
  skip S218 NKE: strategy already open (paper bucket rule)
2026-08-18 11:12:19,755 INFO   skip S218 NKE: strategy already open (paper bucket rule)
  skip S218 PG: strategy already open (paper bucket rule)
2026-08-18 11:12:19,755 INFO   skip S218 PG: strategy already open (paper bucket rule)
  skip S210 AXP: strategy already open (paper bucket rule)
2026-08-18 11:12:19,755 INFO   skip S210 AXP: strategy already open (paper bucket rule)
  skip S210 CELH: strategy already open (paper bucket rule)
2026-08-18 11:12:19,755 INFO   skip S210 CELH: strategy already open (paper bucket rule)
  skip S210 HOOD: strategy already open (paper bucket rule)
2026-08-18 11:12:19,755 INFO   skip S210 HOOD: strategy already open (paper bucket rule)
  skip S210 UNP: strategy already open (paper bucket rule)
2026-08-18 11:12:19,755 INFO   skip S210 UNP: strategy already open (paper bucket rule)
Live micro done. open_options=3 lots=4
2026-08-18 11:12:19,814 INFO Live micro done. open_options=3 lots=4
```

### Paper options bot full output

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T151603Z

- UTC timestamp: `20260818T151603Z`
- GitHub run: [#7363](https://github.com/28twagg-ops/TradingBot/actions/runs/32153303096)
- Run id: `32153303096`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`14s`
- Paper options: exit=`0`, duration=`0s`

### Live bot full output

```text
15:16:04  INFO      Mode: exits
15:16:05  INFO        Daily log -> logs/daily/2026-08-18.md
15:16:05  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (2 ledger rows)
15:16:05  INFO        place_all_stops: checking 6 positions...
15:16:05  INFO        STOP skipped AEE: fractional (0.6341 shares) — software exit will handle it
15:16:05  INFO        STOP skipped AFL: fractional (0.5726 shares) — software exit will handle it
15:16:05  INFO        STOP skipped AON: fractional (0.2011 shares) — software exit will handle it
15:16:06  INFO        [positions] 3/3 (3 valid)
15:16:06  INFO        Daily log -> logs/daily/2026-08-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $451.82|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AEE  P&L -0.4%  $-0.27                                            HOLD|
|  AFL  P&L -0.2%  $-0.14                                            HOLD|
|  AON  P&L +0.0%  $+0.03                                            HOLD|
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
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00412500     $0.31    $0.19    -38.7%   $-12.00   $19.00   |
|  CELH260821C00030000     $0.70    $0.60    -14.3%   $-10.00   $60.00   |
|  TSLA260821C00357500     $0.62    $0.69    +11.3%   $+7.00    $69.00   |
|                                                                        |
|  Options open P&L                                               $-15.00|
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

### Live options micro full output

```text
=== options_live_micro LIVE 2026-08-18T11:16:07.149687-04:00 share=50% ===
2026-08-18 11:16:07,149 INFO === options_live_micro LIVE 2026-08-18T11:16:07.149687-04:00 share=50% ===
Live account equity $451.82 cash $93.84 #225458845 options_level=3
2026-08-18 11:16:07,405 INFO Live account equity $451.82 cash $93.84 #225458845 options_level=3
Live micro hold S404 AVGO260821C00412500 -38.7% (tp +50% / sl -50%)
2026-08-18 11:16:07,630 INFO Live micro hold S404 AVGO260821C00412500 -38.7% (tp +50% / sl -50%)
Live micro hold S406 TSLA260821C00357500 +11.3% (tp +50% / sl -50%)
2026-08-18 11:16:07,631 INFO Live micro hold S406 TSLA260821C00357500 +11.3% (tp +50% / sl -50%)
Live micro hold S210 CELH260821C00030000 -14.3% (tp +50% / sl -50%)
2026-08-18 11:16:07,631 INFO Live micro hold S210 CELH260821C00030000 -14.3% (tp +50% / sl -50%)
Live micro sleeve $226 (50% of $452) deployed $148 open_strategies=4/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
2026-08-18 11:16:08,022 INFO Live micro sleeve $226 (50% of $452) deployed $148 open_strategies=4/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-18 11:16:08,022 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 24
2026-08-18 11:16:19,777 INFO Live micro signals: 24
  skip S404 AFRM: strategy already open (paper bucket rule)
2026-08-18 11:16:19,777 INFO   skip S404 AFRM: strategy already open (paper bucket rule)
  skip S404 AMD: strategy already open (paper bucket rule)
2026-08-18 11:16:19,777 INFO   skip S404 AMD: strategy already open (paper bucket rule)
  skip S404 ARM: strategy already open (paper bucket rule)
2026-08-18 11:16:19,777 INFO   skip S404 ARM: strategy already open (paper bucket rule)
  skip S404 AVGO: strategy already open (paper bucket rule)
2026-08-18 11:16:19,777 INFO   skip S404 AVGO: strategy already open (paper bucket rule)
  skip S404 CAT: strategy already open (paper bucket rule)
2026-08-18 11:16:19,777 INFO   skip S404 CAT: strategy already open (paper bucket rule)
  skip S404 CVNA: strategy already open (paper bucket rule)
2026-08-18 11:16:19,777 INFO   skip S404 CVNA: strategy already open (paper bucket rule)
  skip S404 DOCN: strategy already open (paper bucket rule)
2026-08-18 11:16:19,777 INFO   skip S404 DOCN: strategy already open (paper bucket rule)
  skip S404 HOOD: strategy already open (paper bucket rule)
2026-08-18 11:16:19,777 INFO   skip S404 HOOD: strategy already open (paper bucket rule)
  skip S404 MARA: strategy already open (paper bucket rule)
2026-08-18 11:16:19,777 INFO   skip S404 MARA: strategy already open (paper bucket rule)
  skip S404 META: strategy already open (paper bucket rule)
2026-08-18 11:16:19,777 INFO   skip S404 META: strategy already open (paper bucket rule)
  skip S404 NVDA: strategy already open (paper bucket rule)
2026-08-18 11:16:19,777 INFO   skip S404 NVDA: strategy already open (paper bucket rule)
  skip S404 PATH: strategy already open (paper bucket rule)
2026-08-18 11:16:19,778 INFO   skip S404 PATH: strategy already open (paper bucket rule)
  skip S404 SMCI: strategy already open (paper bucket rule)
2026-08-18 11:16:19,778 INFO   skip S404 SMCI: strategy already open (paper bucket rule)
  skip S404 UPST: strategy already open (paper bucket rule)
2026-08-18 11:16:19,778 INFO   skip S404 UPST: strategy already open (paper bucket rule)
  skip S406 AFRM: strategy already open (paper bucket rule)
2026-08-18 11:16:19,778 INFO   skip S406 AFRM: strategy already open (paper bucket rule)
  skip S406 PATH: strategy already open (paper bucket rule)
2026-08-18 11:16:19,778 INFO   skip S406 PATH: strategy already open (paper bucket rule)
  skip S406 TSLA: strategy already open (paper bucket rule)
2026-08-18 11:16:19,778 INFO   skip S406 TSLA: strategy already open (paper bucket rule)
  skip S406 UPST: strategy already open (paper bucket rule)
2026-08-18 11:16:19,778 INFO   skip S406 UPST: strategy already open (paper bucket rule)
  skip S218 NKE: strategy already open (paper bucket rule)
2026-08-18 11:16:19,778 INFO   skip S218 NKE: strategy already open (paper bucket rule)
  skip S218 PG: strategy already open (paper bucket rule)
2026-08-18 11:16:19,778 INFO   skip S218 PG: strategy already open (paper bucket rule)
  skip S210 AXP: strategy already open (paper bucket rule)
2026-08-18 11:16:19,778 INFO   skip S210 AXP: strategy already open (paper bucket rule)
  skip S210 CELH: strategy already open (paper bucket rule)
2026-08-18 11:16:19,778 INFO   skip S210 CELH: strategy already open (paper bucket rule)
  skip S210 HOOD: strategy already open (paper bucket rule)
2026-08-18 11:16:19,778 INFO   skip S210 HOOD: strategy already open (paper bucket rule)
  skip S210 UNP: strategy already open (paper bucket rule)
2026-08-18 11:16:19,778 INFO   skip S210 UNP: strategy already open (paper bucket rule)
Live micro done. open_options=3 lots=4
2026-08-18 11:16:20,144 INFO Live micro done. open_options=3 lots=4
```

### Paper options bot full output

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T152104Z

- UTC timestamp: `20260818T152104Z`
- GitHub run: [#7364](https://github.com/28twagg-ops/TradingBot/actions/runs/32153810726)
- Run id: `32153810726`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`13s`
- Paper options: exit=`0`, duration=`0s`

### Live bot full output

```text
15:21:05  INFO      Mode: exits
15:21:06  INFO        Daily log -> logs/daily/2026-08-18.md
15:21:06  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (2 ledger rows)
15:21:06  INFO        place_all_stops: checking 6 positions...
15:21:06  INFO        STOP skipped AEE: fractional (0.6341 shares) — software exit will handle it
15:21:06  INFO        STOP skipped AFL: fractional (0.5726 shares) — software exit will handle it
15:21:06  INFO        STOP skipped AON: fractional (0.2011 shares) — software exit will handle it
15:21:07  INFO        [positions] 3/3 (3 valid)
15:21:07  INFO        Daily log -> logs/daily/2026-08-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $449.77|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AEE  P&L -0.3%  $-0.20                                            HOLD|
|  AFL  P&L -0.2%  $-0.16                                            HOLD|
|  AON  P&L -0.1%  $-0.08                                            HOLD|
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
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00412500     $0.31    $0.19    -38.7%   $-12.00   $19.00   |
|  CELH260821C00030000     $0.70    $0.62    -11.4%   $-8.00    $62.00   |
|  TSLA260821C00357500     $0.62    $0.65    +4.8%    $+3.00    $65.00   |
|                                                                        |
|  Options open P&L                                               $-17.00|
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

### Live options micro full output

```text
=== options_live_micro LIVE 2026-08-18T11:21:08.354912-04:00 share=50% ===
2026-08-18 11:21:08,354 INFO === options_live_micro LIVE 2026-08-18T11:21:08.354912-04:00 share=50% ===
Live account equity $449.77 cash $93.84 #225458845 options_level=3
2026-08-18 11:21:08,568 INFO Live account equity $449.77 cash $93.84 #225458845 options_level=3
Live micro hold S404 AVGO260821C00412500 -38.7% (tp +50% / sl -50%)
2026-08-18 11:21:08,746 INFO Live micro hold S404 AVGO260821C00412500 -38.7% (tp +50% / sl -50%)
Live micro hold S406 TSLA260821C00357500 +4.8% (tp +50% / sl -50%)
2026-08-18 11:21:08,746 INFO Live micro hold S406 TSLA260821C00357500 +4.8% (tp +50% / sl -50%)
Live micro hold S210 CELH260821C00030000 -11.4% (tp +50% / sl -50%)
2026-08-18 11:21:08,746 INFO Live micro hold S210 CELH260821C00030000 -11.4% (tp +50% / sl -50%)
Live micro sleeve $225 (50% of $450) deployed $146 open_strategies=4/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
2026-08-18 11:21:09,044 INFO Live micro sleeve $225 (50% of $450) deployed $146 open_strategies=4/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-18 11:21:09,045 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 23
2026-08-18 11:21:19,833 INFO Live micro signals: 23
  skip S404 AFRM: strategy already open (paper bucket rule)
2026-08-18 11:21:19,834 INFO   skip S404 AFRM: strategy already open (paper bucket rule)
  skip S404 AMD: strategy already open (paper bucket rule)
2026-08-18 11:21:19,834 INFO   skip S404 AMD: strategy already open (paper bucket rule)
  skip S404 ARM: strategy already open (paper bucket rule)
2026-08-18 11:21:19,834 INFO   skip S404 ARM: strategy already open (paper bucket rule)
  skip S404 AVGO: strategy already open (paper bucket rule)
2026-08-18 11:21:19,834 INFO   skip S404 AVGO: strategy already open (paper bucket rule)
  skip S404 CAT: strategy already open (paper bucket rule)
2026-08-18 11:21:19,834 INFO   skip S404 CAT: strategy already open (paper bucket rule)
  skip S404 CVNA: strategy already open (paper bucket rule)
2026-08-18 11:21:19,834 INFO   skip S404 CVNA: strategy already open (paper bucket rule)
  skip S404 DOCN: strategy already open (paper bucket rule)
2026-08-18 11:21:19,834 INFO   skip S404 DOCN: strategy already open (paper bucket rule)
  skip S404 HOOD: strategy already open (paper bucket rule)
2026-08-18 11:21:19,834 INFO   skip S404 HOOD: strategy already open (paper bucket rule)
  skip S404 MARA: strategy already open (paper bucket rule)
2026-08-18 11:21:19,834 INFO   skip S404 MARA: strategy already open (paper bucket rule)
  skip S404 META: strategy already open (paper bucket rule)
2026-08-18 11:21:19,834 INFO   skip S404 META: strategy already open (paper bucket rule)
  skip S404 NVDA: strategy already open (paper bucket rule)
2026-08-18 11:21:19,834 INFO   skip S404 NVDA: strategy already open (paper bucket rule)
  skip S404 PATH: strategy already open (paper bucket rule)
2026-08-18 11:21:19,835 INFO   skip S404 PATH: strategy already open (paper bucket rule)
  skip S404 SMCI: strategy already open (paper bucket rule)
2026-08-18 11:21:19,835 INFO   skip S404 SMCI: strategy already open (paper bucket rule)
  skip S404 UPST: strategy already open (paper bucket rule)
2026-08-18 11:21:19,835 INFO   skip S404 UPST: strategy already open (paper bucket rule)
  skip S406 AFRM: strategy already open (paper bucket rule)
2026-08-18 11:21:19,835 INFO   skip S406 AFRM: strategy already open (paper bucket rule)
  skip S406 PATH: strategy already open (paper bucket rule)
2026-08-18 11:21:19,835 INFO   skip S406 PATH: strategy already open (paper bucket rule)
  skip S406 TSLA: strategy already open (paper bucket rule)
2026-08-18 11:21:19,835 INFO   skip S406 TSLA: strategy already open (paper bucket rule)
  skip S218 NKE: strategy already open (paper bucket rule)
2026-08-18 11:21:19,835 INFO   skip S218 NKE: strategy already open (paper bucket rule)
  skip S218 PG: strategy already open (paper bucket rule)
2026-08-18 11:21:19,835 INFO   skip S218 PG: strategy already open (paper bucket rule)
  skip S210 AXP: strategy already open (paper bucket rule)
2026-08-18 11:21:19,835 INFO   skip S210 AXP: strategy already open (paper bucket rule)
  skip S210 CELH: strategy already open (paper bucket rule)
2026-08-18 11:21:19,835 INFO   skip S210 CELH: strategy already open (paper bucket rule)
  skip S210 HOOD: strategy already open (paper bucket rule)
2026-08-18 11:21:19,835 INFO   skip S210 HOOD: strategy already open (paper bucket rule)
  skip S210 UNP: strategy already open (paper bucket rule)
2026-08-18 11:21:19,835 INFO   skip S210 UNP: strategy already open (paper bucket rule)
Live micro done. open_options=3 lots=4
2026-08-18 11:21:20,174 INFO Live micro done. open_options=3 lots=4
```

### Paper options bot full output

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T152607Z

- UTC timestamp: `20260818T152607Z`
- GitHub run: [#7365](https://github.com/28twagg-ops/TradingBot/actions/runs/32154316052)
- Run id: `32154316052`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`14s`
- Paper options: exit=`0`, duration=`0s`

### Live bot full output

```text
15:26:08  INFO      Mode: exits
15:26:09  INFO        Daily log -> logs/daily/2026-08-18.md
15:26:09  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (2 ledger rows)
15:26:09  INFO        place_all_stops: checking 6 positions...
15:26:09  INFO        STOP skipped AEE: fractional (0.6341 shares) — software exit will handle it
15:26:09  INFO        STOP skipped AFL: fractional (0.5726 shares) — software exit will handle it
15:26:09  INFO        STOP skipped AON: fractional (0.2011 shares) — software exit will handle it
15:26:10  INFO        [positions] 3/3 (3 valid)
15:26:10  INFO        Daily log -> logs/daily/2026-08-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $450.40|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AFL  P&L -0.4%  $-0.30                                            HOLD|
|  AEE  P&L -0.4%  $-0.26                                            HOLD|
|  AON  P&L -0.4%  $-0.25                                            HOLD|
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
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00412500     $0.31    $0.19    -38.7%   $-12.00   $19.00   |
|  CELH260821C00030000     $0.70    $0.60    -14.3%   $-10.00   $60.00   |
|  TSLA260821C00357500     $0.62    $0.69    +11.3%   $+7.00    $69.00   |
|                                                                        |
|  Options open P&L                                               $-15.00|
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

### Live options micro full output

```text
=== options_live_micro LIVE 2026-08-18T11:26:11.972918-04:00 share=50% ===
2026-08-18 11:26:11,972 INFO === options_live_micro LIVE 2026-08-18T11:26:11.972918-04:00 share=50% ===
Live account equity $451.40 cash $93.84 #225458845 options_level=3
2026-08-18 11:26:12,200 INFO Live account equity $451.40 cash $93.84 #225458845 options_level=3
Live micro hold S404 AVGO260821C00412500 -38.7% (tp +50% / sl -50%)
2026-08-18 11:26:12,476 INFO Live micro hold S404 AVGO260821C00412500 -38.7% (tp +50% / sl -50%)
Live micro hold S406 TSLA260821C00357500 +11.3% (tp +50% / sl -50%)
2026-08-18 11:26:12,476 INFO Live micro hold S406 TSLA260821C00357500 +11.3% (tp +50% / sl -50%)
Live micro hold S210 CELH260821C00030000 -14.3% (tp +50% / sl -50%)
2026-08-18 11:26:12,476 INFO Live micro hold S210 CELH260821C00030000 -14.3% (tp +50% / sl -50%)
Live micro sleeve $226 (50% of $451) deployed $148 open_strategies=4/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
2026-08-18 11:26:12,835 INFO Live micro sleeve $226 (50% of $451) deployed $148 open_strategies=4/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-18 11:26:12,835 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 22
2026-08-18 11:26:23,782 INFO Live micro signals: 22
  skip S404 AFRM: strategy already open (paper bucket rule)
2026-08-18 11:26:23,782 INFO   skip S404 AFRM: strategy already open (paper bucket rule)
  skip S404 AMD: strategy already open (paper bucket rule)
2026-08-18 11:26:23,782 INFO   skip S404 AMD: strategy already open (paper bucket rule)
  skip S404 ARM: strategy already open (paper bucket rule)
2026-08-18 11:26:23,782 INFO   skip S404 ARM: strategy already open (paper bucket rule)
  skip S404 AVGO: strategy already open (paper bucket rule)
2026-08-18 11:26:23,782 INFO   skip S404 AVGO: strategy already open (paper bucket rule)
  skip S404 CAT: strategy already open (paper bucket rule)
2026-08-18 11:26:23,782 INFO   skip S404 CAT: strategy already open (paper bucket rule)
  skip S404 CVNA: strategy already open (paper bucket rule)
2026-08-18 11:26:23,783 INFO   skip S404 CVNA: strategy already open (paper bucket rule)
  skip S404 DOCN: strategy already open (paper bucket rule)
2026-08-18 11:26:23,783 INFO   skip S404 DOCN: strategy already open (paper bucket rule)
  skip S404 HOOD: strategy already open (paper bucket rule)
2026-08-18 11:26:23,783 INFO   skip S404 HOOD: strategy already open (paper bucket rule)
  skip S404 MARA: strategy already open (paper bucket rule)
2026-08-18 11:26:23,783 INFO   skip S404 MARA: strategy already open (paper bucket rule)
  skip S404 META: strategy already open (paper bucket rule)
2026-08-18 11:26:23,783 INFO   skip S404 META: strategy already open (paper bucket rule)
  skip S404 NVDA: strategy already open (paper bucket rule)
2026-08-18 11:26:23,783 INFO   skip S404 NVDA: strategy already open (paper bucket rule)
  skip S404 PATH: strategy already open (paper bucket rule)
2026-08-18 11:26:23,783 INFO   skip S404 PATH: strategy already open (paper bucket rule)
  skip S404 SMCI: strategy already open (paper bucket rule)
2026-08-18 11:26:23,783 INFO   skip S404 SMCI: strategy already open (paper bucket rule)
  skip S404 UPST: strategy already open (paper bucket rule)
2026-08-18 11:26:23,783 INFO   skip S404 UPST: strategy already open (paper bucket rule)
  skip S406 AFRM: strategy already open (paper bucket rule)
2026-08-18 11:26:23,783 INFO   skip S406 AFRM: strategy already open (paper bucket rule)
  skip S406 PATH: strategy already open (paper bucket rule)
2026-08-18 11:26:23,783 INFO   skip S406 PATH: strategy already open (paper bucket rule)
  skip S406 TSLA: strategy already open (paper bucket rule)
2026-08-18 11:26:23,783 INFO   skip S406 TSLA: strategy already open (paper bucket rule)
  skip S218 NKE: strategy already open (paper bucket rule)
2026-08-18 11:26:23,783 INFO   skip S218 NKE: strategy already open (paper bucket rule)
  skip S218 PG: strategy already open (paper bucket rule)
2026-08-18 11:26:23,784 INFO   skip S218 PG: strategy already open (paper bucket rule)
  skip S210 AXP: strategy already open (paper bucket rule)
2026-08-18 11:26:23,784 INFO   skip S210 AXP: strategy already open (paper bucket rule)
  skip S210 CELH: strategy already open (paper bucket rule)
2026-08-18 11:26:23,784 INFO   skip S210 CELH: strategy already open (paper bucket rule)
  skip S210 HOOD: strategy already open (paper bucket rule)
2026-08-18 11:26:23,784 INFO   skip S210 HOOD: strategy already open (paper bucket rule)
Live micro done. open_options=3 lots=4
2026-08-18 11:26:24,140 INFO Live micro done. open_options=3 lots=4
```

### Paper options bot full output

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T153114Z

- UTC timestamp: `20260818T153114Z`
- GitHub run: [#7366](https://github.com/28twagg-ops/TradingBot/actions/runs/32154822791)
- Run id: `32154822791`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`16s`
- Paper options: exit=`0`, duration=`0s`

### Live bot full output

```text
15:31:14  INFO      Mode: exits
15:31:16  INFO        Daily log -> logs/daily/2026-08-18.md
15:31:16  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (2 ledger rows)
15:31:16  INFO        place_all_stops: checking 6 positions...
15:31:16  INFO        STOP skipped AEE: fractional (0.6341 shares) — software exit will handle it
15:31:16  INFO        STOP skipped AFL: fractional (0.5726 shares) — software exit will handle it
15:31:16  INFO        STOP skipped AON: fractional (0.2011 shares) — software exit will handle it
15:31:16  INFO        [positions] 3/3 (3 valid)
15:31:16  INFO        Daily log -> logs/daily/2026-08-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $450.44|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AFL  P&L -0.4%  $-0.28                                            HOLD|
|  AON  P&L -0.4%  $-0.27                                            HOLD|
|  AEE  P&L -0.3%  $-0.21                                            HOLD|
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
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00412500     $0.31    $0.19    -38.7%   $-12.00   $19.00   |
|  CELH260821C00030000     $0.70    $0.55    -21.4%   $-15.00   $55.00   |
|  TSLA260821C00357500     $0.62    $0.74    +19.4%   $+12.00   $74.00   |
|                                                                        |
|  Options open P&L                                               $-15.00|
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

### Live options micro full output

```text
=== options_live_micro LIVE 2026-08-18T11:31:17.769131-04:00 share=50% ===
2026-08-18 11:31:17,769 INFO === options_live_micro LIVE 2026-08-18T11:31:17.769131-04:00 share=50% ===
Live account equity $451.44 cash $93.84 #225458845 options_level=3
2026-08-18 11:31:17,993 INFO Live account equity $451.44 cash $93.84 #225458845 options_level=3
Live micro hold S404 AVGO260821C00412500 -38.7% (tp +50% / sl -50%)
2026-08-18 11:31:18,207 INFO Live micro hold S404 AVGO260821C00412500 -38.7% (tp +50% / sl -50%)
Live micro hold S406 TSLA260821C00357500 +19.4% (tp +50% / sl -50%)
2026-08-18 11:31:18,207 INFO Live micro hold S406 TSLA260821C00357500 +19.4% (tp +50% / sl -50%)
Live micro hold S210 CELH260821C00030000 -21.4% (tp +50% / sl -50%)
2026-08-18 11:31:18,207 INFO Live micro hold S210 CELH260821C00030000 -21.4% (tp +50% / sl -50%)
Live micro sleeve $226 (50% of $451) deployed $148 open_strategies=4/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
2026-08-18 11:31:18,557 INFO Live micro sleeve $226 (50% of $451) deployed $148 open_strategies=4/4 (paper baseline $75 / tp=+50% sl=-50% / 1 contract per strategy)
Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
2026-08-18 11:31:18,557 INFO Live micro entry order (CLEAN win): S404 100%win, S406 56%win, S218 56%win, S210 55%win
Live micro signals: 24
2026-08-18 11:31:33,333 INFO Live micro signals: 24
  skip S404 AFRM: strategy already open (paper bucket rule)
2026-08-18 11:31:33,333 INFO   skip S404 AFRM: strategy already open (paper bucket rule)
  skip S404 AMD: strategy already open (paper bucket rule)
2026-08-18 11:31:33,333 INFO   skip S404 AMD: strategy already open (paper bucket rule)
  skip S404 ARM: strategy already open (paper bucket rule)
2026-08-18 11:31:33,333 INFO   skip S404 ARM: strategy already open (paper bucket rule)
  skip S404 AVGO: strategy already open (paper bucket rule)
2026-08-18 11:31:33,333 INFO   skip S404 AVGO: strategy already open (paper bucket rule)
  skip S404 CAT: strategy already open (paper bucket rule)
2026-08-18 11:31:33,334 INFO   skip S404 CAT: strategy already open (paper bucket rule)
  skip S404 CVNA: strategy already open (paper bucket rule)
2026-08-18 11:31:33,334 INFO   skip S404 CVNA: strategy already open (paper bucket rule)
  skip S404 DOCN: strategy already open (paper bucket rule)
2026-08-18 11:31:33,334 INFO   skip S404 DOCN: strategy already open (paper bucket rule)
  skip S404 HOOD: strategy already open (paper bucket rule)
2026-08-18 11:31:33,334 INFO   skip S404 HOOD: strategy already open (paper bucket rule)
  skip S404 MARA: strategy already open (paper bucket rule)
2026-08-18 11:31:33,334 INFO   skip S404 MARA: strategy already open (paper bucket rule)
  skip S404 META: strategy already open (paper bucket rule)
2026-08-18 11:31:33,334 INFO   skip S404 META: strategy already open (paper bucket rule)
  skip S404 NVDA: strategy already open (paper bucket rule)
2026-08-18 11:31:33,334 INFO   skip S404 NVDA: strategy already open (paper bucket rule)
  skip S404 PATH: strategy already open (paper bucket rule)
2026-08-18 11:31:33,334 INFO   skip S404 PATH: strategy already open (paper bucket rule)
  skip S404 SMCI: strategy already open (paper bucket rule)
2026-08-18 11:31:33,334 INFO   skip S404 SMCI: strategy already open (paper bucket rule)
  skip S404 UPST: strategy already open (paper bucket rule)
2026-08-18 11:31:33,335 INFO   skip S404 UPST: strategy already open (paper bucket rule)
  skip S406 AFRM: strategy already open (paper bucket rule)
2026-08-18 11:31:33,335 INFO   skip S406 AFRM: strategy already open (paper bucket rule)
  skip S406 PATH: strategy already open (paper bucket rule)
2026-08-18 11:31:33,335 INFO   skip S406 PATH: strategy already open (paper bucket rule)
  skip S406 TSLA: strategy already open (paper bucket rule)
2026-08-18 11:31:33,335 INFO   skip S406 TSLA: strategy already open (paper bucket rule)
  skip S406 UPST: strategy already open (paper bucket rule)
2026-08-18 11:31:33,335 INFO   skip S406 UPST: strategy already open (paper bucket rule)
  skip S218 NKE: strategy already open (paper bucket rule)
2026-08-18 11:31:33,335 INFO   skip S218 NKE: strategy already open (paper bucket rule)
  skip S218 PG: strategy already open (paper bucket rule)
2026-08-18 11:31:33,335 INFO   skip S218 PG: strategy already open (paper bucket rule)
  skip S210 AXP: strategy already open (paper bucket rule)
2026-08-18 11:31:33,335 INFO   skip S210 AXP: strategy already open (paper bucket rule)
  skip S210 CELH: strategy already open (paper bucket rule)
2026-08-18 11:31:33,335 INFO   skip S210 CELH: strategy already open (paper bucket rule)
  skip S210 HOOD: strategy already open (paper bucket rule)
2026-08-18 11:31:33,335 INFO   skip S210 HOOD: strategy already open (paper bucket rule)
  skip S210 UNP: strategy already open (paper bucket rule)
2026-08-18 11:31:33,335 INFO   skip S210 UNP: strategy already open (paper bucket rule)
Live micro done. open_options=3 lots=4
2026-08-18 11:31:33,689 INFO Live micro done. open_options=3 lots=4
```

### Paper options bot full output

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T153552Z

- UTC timestamp: `20260818T153552Z`
- GitHub run: [#7367](https://github.com/28twagg-ops/TradingBot/actions/runs/32155334522)
- Run id: `32155334522`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`

### Live bot full output

```text
15:35:53  INFO      Mode: exits
15:35:53  INFO        Daily log -> logs/daily/2026-08-18.md
15:35:53  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (2 ledger rows)
15:35:53  INFO        place_all_stops: checking 7 positions...
15:35:53  INFO        STOP skipped AEE: fractional (0.6341 shares) — software exit will handle it
15:35:53  INFO        STOP skipped AFL: fractional (0.5726 shares) — software exit will handle it
15:35:53  INFO        STOP skipped AON: fractional (0.2011 shares) — software exit will handle it
15:35:54  INFO        [positions] 3/3 (3 valid)
15:35:54  INFO        Daily log -> logs/daily/2026-08-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:35 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $442.32|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AON  P&L -0.5%  $-0.33                                            HOLD|
|  AFL  P&L -0.4%  $-0.28                                            HOLD|
|  AEE  P&L -0.3%  $-0.23                                            HOLD|
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
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00412500     $0.31    $0.19    -38.7%   $-12.00   $19.00   |
|  CELH260821C00030000     $0.70    $0.51    -27.1%   $-19.00   $51.00   |
|  NKE260821C00040000      $0.54    $0.55    +1.9%    $+1.00    $55.00   |
|  TSLA260821C00357500     $0.62    $0.69    +11.3%   $+7.00    $69.00   |
|                                                                        |
|  Options open P&L                                               $-23.00|
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

### Live options micro full output

```text
=== options_live_micro LIVE 2026-08-18T11:35:54.997983-04:00 share=50% ===
2026-08-18 11:35:54,998 INFO === options_live_micro LIVE 2026-08-18T11:35:54.997983-04:00 share=50% ===
Live account equity $443.32 cash $39.80 #225458845 options_level=3
2026-08-18 11:35:55,093 INFO Live account equity $443.32 cash $39.80 #225458845 options_level=3
Live micro hold S404 AVGO260821C00412500 -38.7% (tp +50% / sl -50%)
2026-08-18 11:35:55,182 INFO Live micro hold S404 AVGO260821C00412500 -38.7% (tp +50% / sl -50%)
Live micro hold S406 TSLA260821C00357500 +11.3% (tp +50% / sl -50%)
2026-08-18 11:35:55,182 INFO Live micro hold S406 TSLA260821C00357500 +11.3% (tp +50% / sl -50%)
Live micro hold S218 NKE260821C00040000 +1.9% (tp +50% / sl -50%)
2026-08-18 11:35:55,182 INFO Live micro hold S218 NKE260821C00040000 +1.9% (tp +50% / sl -50%)
Live micro hold S210 CELH260821C00030000 -27.1% (tp +50% / sl -50%)
2026-08-18 11:35:55,182 INFO Live micro hold S210 CELH260821C00030000 -27.1% (tp +50% / sl -50%)
LIVE PROT STOP NKE260821C00040000 x1 stop=0.27 id=74a1abb9-fd89-4801-a984-de01aec9adb5
2026-08-18 11:35:55,304 INFO LIVE PROT STOP NKE260821C00040000 x1 stop=0.27 id=74a1abb9-fd89-4801-a984-de01aec9adb5
Live micro: manage/exits only
2026-08-18 11:35:55,326 INFO Live micro: manage/exits only
Live micro done. open_options=4 lots=4
2026-08-18 11:35:55,349 INFO Live micro done. open_options=4 lots=4
```

### Paper options bot full output

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T155229Z

- UTC timestamp: `20260818T155229Z`
- GitHub run: [#7370](https://github.com/28twagg-ops/TradingBot/actions/runs/32156836695)
- Run id: `32156836695`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`

### Live bot full output

```text
15:52:30  INFO      Mode: exits
15:52:30  INFO        Daily log -> logs/daily/2026-08-18.md
15:52:30  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (2 ledger rows)
15:52:30  INFO        place_all_stops: checking 7 positions...
15:52:30  INFO        STOP skipped AEE: fractional (0.6341 shares) — software exit will handle it
15:52:30  INFO        STOP skipped AFL: fractional (0.5726 shares) — software exit will handle it
15:52:30  INFO        STOP skipped AON: fractional (0.2011 shares) — software exit will handle it
15:52:30  INFO        [positions] 3/3 (3 valid)
15:52:31  INFO        Daily log -> logs/daily/2026-08-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:52 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $468.46|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AFL  P&L -0.4%  $-0.31                                            HOLD|
|  AEE  P&L -0.3%  $-0.23                                            HOLD|
|  AON  P&L -0.2%  $-0.16                                            HOLD|
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
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00412500     $0.31    $0.19    -38.7%   $-12.00   $19.00   |
|  CELH260821C00030000     $0.70    $0.56    -20.0%   $-14.00   $56.00   |
|  NKE260821C00040000      $0.54    $0.57    +5.6%    $+3.00    $57.00   |
|  TSLA260821C00357500     $0.62    $0.88    +41.9%   $+26.00   $88.00   |
|                                                                        |
|  Options open P&L                                                $+3.00|
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

### Live options micro full output

```text
=== options_live_micro LIVE 2026-08-18T11:52:32.154611-04:00 share=50% ===
2026-08-18 11:52:32,154 INFO === options_live_micro LIVE 2026-08-18T11:52:32.154611-04:00 share=50% ===
Live account equity $468.46 cash $39.80 #225458845 options_level=3
2026-08-18 11:52:32,538 INFO Live account equity $468.46 cash $39.80 #225458845 options_level=3
Live micro hold S404 AVGO260821C00412500 -38.7% (tp +50% / sl -50%)
2026-08-18 11:52:32,555 INFO Live micro hold S404 AVGO260821C00412500 -38.7% (tp +50% / sl -50%)
Live micro hold S406 TSLA260821C00357500 +40.3% (tp +50% / sl -50%)
2026-08-18 11:52:32,555 INFO Live micro hold S406 TSLA260821C00357500 +40.3% (tp +50% / sl -50%)
Live micro hold S218 NKE260821C00040000 +5.6% (tp +50% / sl -50%)
2026-08-18 11:52:32,556 INFO Live micro hold S218 NKE260821C00040000 +5.6% (tp +50% / sl -50%)
Live micro hold S210 CELH260821C00030000 -20.0% (tp +50% / sl -50%)
2026-08-18 11:52:32,556 INFO Live micro hold S210 CELH260821C00030000 -20.0% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-18 11:52:32,609 INFO Live micro: manage/exits only
Live micro done. open_options=4 lots=4
2026-08-18 11:52:32,632 INFO Live micro done. open_options=4 lots=4
```

### Paper options bot full output

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T155554Z

- UTC timestamp: `20260818T155554Z`
- GitHub run: [#7371](https://github.com/28twagg-ops/TradingBot/actions/runs/32157333539)
- Run id: `32157333539`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`0s`

### Live bot full output

```text
15:55:54  INFO      Mode: exits
15:55:55  INFO        Daily log -> logs/daily/2026-08-18.md
15:55:55  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (2 ledger rows)
15:55:55  INFO        place_all_stops: checking 7 positions...
15:55:55  INFO        STOP skipped AEE: fractional (0.6341 shares) — software exit will handle it
15:55:55  INFO        STOP skipped AFL: fractional (0.5726 shares) — software exit will handle it
15:55:55  INFO        STOP skipped AON: fractional (0.2011 shares) — software exit will handle it
15:55:55  INFO        [positions] 3/3 (3 valid)
15:55:55  INFO        SELL MARKET [urgent] AFL closed
15:55:58  INFO        TX logged: SELL AFL  P&L -0.52%
15:55:58  INFO        Daily log -> logs/daily/2026-08-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:55 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $480.29|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AFL  P&L -0.5%  $-0.36                         EXIT: stop_loss (-0.5%)|
|  AEE  P&L -0.4%  $-0.31                                            HOLD|
|  AON  P&L -0.3%  $-0.20                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  1 attempted  |  1 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                2|
|  Logged exits                                                         1|
+========================================================================+

+========================================================================+
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00412500     $0.31    $0.19    -38.7%   $-12.00   $19.00   |
|  CELH260821C00030000     $0.70    $0.51    -27.1%   $-19.00   $51.00   |
|  NKE260821C00040000      $0.54    $0.63    +16.7%   $+9.00    $63.00   |
|  TSLA260821C00357500     $0.62    $0.96    +54.8%   $+34.00   $96.00   |
|                                                                        |
|  Options open P&L                                               $+12.00|
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  AFL                                         -0.52%  (threshold -0.50%)|
|  Count                                                                1|
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro full output

```text
=== options_live_micro LIVE 2026-08-18T11:55:59.103674-04:00 share=50% ===
2026-08-18 11:55:59,103 INFO === options_live_micro LIVE 2026-08-18T11:55:59.103674-04:00 share=50% ===
Live account equity $478.23 cash $109.58 #225458845 options_level=3
2026-08-18 11:55:59,393 INFO Live account equity $478.23 cash $109.58 #225458845 options_level=3
Live micro hold S404 AVGO260821C00412500 -38.7% (tp +50% / sl -50%)
2026-08-18 11:55:59,475 INFO Live micro hold S404 AVGO260821C00412500 -38.7% (tp +50% / sl -50%)
LIVE EXIT take_profit (+54.8%) TSLA260821C00357500 x1 limit=0.93 id=4267cfd4-ba4b-45e8-8cd9-b799f6e1b5c2
2026-08-18 11:56:00,343 INFO LIVE EXIT take_profit (+54.8%) TSLA260821C00357500 x1 limit=0.93 id=4267cfd4-ba4b-45e8-8cd9-b799f6e1b5c2
Live micro hold S218 NKE260821C00040000 +16.7% (tp +50% / sl -50%)
2026-08-18 11:56:00,343 INFO Live micro hold S218 NKE260821C00040000 +16.7% (tp +50% / sl -50%)
Live micro hold S210 CELH260821C00030000 -27.1% (tp +50% / sl -50%)
2026-08-18 11:56:00,344 INFO Live micro hold S210 CELH260821C00030000 -27.1% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-18 11:56:00,478 INFO Live micro: manage/exits only
Live micro done. open_options=3 lots=3
2026-08-18 11:56:00,511 INFO Live micro done. open_options=3 lots=3
```

### Paper options bot full output

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T160650Z

- UTC timestamp: `20260818T160650Z`
- GitHub run: [#7373](https://github.com/28twagg-ops/TradingBot/actions/runs/32158313680)
- Run id: `32158313680`
- Live bot: exit=`0`, duration=`5s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`

### Live bot full output

```text
16:06:51  INFO      Mode: exits
16:06:51  INFO        Daily log -> logs/daily/2026-08-18.md
16:06:51  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (3 ledger rows)
16:06:51  INFO        place_all_stops: checking 5 positions...
16:06:51  INFO        STOP skipped AEE: fractional (0.6341 shares) — software exit will handle it
16:06:51  INFO        STOP skipped AON: fractional (0.2011 shares) — software exit will handle it
16:06:52  INFO        [positions] 2/2 (2 valid)
16:06:52  INFO        SELL MARKET [urgent] AEE closed
16:06:54  INFO        TX logged: SELL AEE  P&L -0.58%
16:06:55  INFO        Daily log -> logs/daily/2026-08-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $492.00|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AEE  P&L -0.6%  $-0.40                         EXIT: stop_loss (-0.6%)|
|  AON  P&L -0.5%  $-0.32                                            HOLD|
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
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00412500     $0.31    $0.25    -19.4%   $-6.00    $25.00   |
|  CELH260821C00030000     $0.70    $0.58    -17.1%   $-12.00   $58.00   |
|  NKE260821C00040000      $0.54    $0.63    +16.7%   $+9.00    $63.00   |
|                                                                        |
|  Options open P&L                                                $-9.00|
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  AEE                                         -0.58%  (threshold -0.50%)|
|  Count                                                                1|
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro full output

```text
=== options_live_micro LIVE 2026-08-18T12:06:55.776407-04:00 share=50% ===
2026-08-18 12:06:55,776 INFO === options_live_micro LIVE 2026-08-18T12:06:55.776407-04:00 share=50% ===
Live account equity $491.99 cash $276.21 #225458845 options_level=3
2026-08-18 12:06:55,927 INFO Live account equity $491.99 cash $276.21 #225458845 options_level=3
Live micro hold S404 AVGO260821C00412500 -19.4% (tp +50% / sl -50%)
2026-08-18 12:06:56,007 INFO Live micro hold S404 AVGO260821C00412500 -19.4% (tp +50% / sl -50%)
Live micro hold S218 NKE260821C00040000 +16.7% (tp +50% / sl -50%)
2026-08-18 12:06:56,007 INFO Live micro hold S218 NKE260821C00040000 +16.7% (tp +50% / sl -50%)
Live micro hold S210 CELH260821C00030000 -17.1% (tp +50% / sl -50%)
2026-08-18 12:06:56,007 INFO Live micro hold S210 CELH260821C00030000 -17.1% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-18 12:06:56,168 INFO Live micro: manage/exits only
Live micro done. open_options=3 lots=3
2026-08-18 12:06:56,224 INFO Live micro done. open_options=3 lots=3
```

### Paper options bot full output

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T161057Z

- UTC timestamp: `20260818T161057Z`
- GitHub run: [#7374](https://github.com/28twagg-ops/TradingBot/actions/runs/32158800425)
- Run id: `32158800425`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`

### Live bot full output

```text
16:10:58  INFO      Mode: exits
16:11:00  INFO        Daily log -> logs/daily/2026-08-18.md
16:11:00  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (4 ledger rows)
16:11:00  INFO        place_all_stops: checking 4 positions...
16:11:00  INFO        STOP skipped AON: fractional (0.2011 shares) — software exit will handle it
16:11:00  INFO        [positions] 1/1 (1 valid)
16:11:01  INFO        Daily log -> logs/daily/2026-08-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $493.07|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AON  P&L -0.3%  $-0.24                                            HOLD|
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
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00412500     $0.31    $0.23    -25.8%   $-8.00    $23.00   |
|  CELH260821C00030000     $0.70    $0.62    -11.4%   $-8.00    $62.00   |
|  NKE260821C00040000      $0.54    $0.62    +14.8%   $+8.00    $62.00   |
|                                                                        |
|  Options open P&L                                                $-8.00|
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

### Live options micro full output

```text
=== options_live_micro LIVE 2026-08-18T12:11:01.837907-04:00 share=50% ===
2026-08-18 12:11:01,837 INFO === options_live_micro LIVE 2026-08-18T12:11:01.837907-04:00 share=50% ===
Live account equity $493.07 cash $276.21 #225458845 options_level=3
2026-08-18 12:11:02,085 INFO Live account equity $493.07 cash $276.21 #225458845 options_level=3
Live micro hold S404 AVGO260821C00412500 -25.8% (tp +50% / sl -50%)
2026-08-18 12:11:02,321 INFO Live micro hold S404 AVGO260821C00412500 -25.8% (tp +50% / sl -50%)
Live micro hold S218 NKE260821C00040000 +14.8% (tp +50% / sl -50%)
2026-08-18 12:11:02,321 INFO Live micro hold S218 NKE260821C00040000 +14.8% (tp +50% / sl -50%)
Live micro hold S210 CELH260821C00030000 -11.4% (tp +50% / sl -50%)
2026-08-18 12:11:02,321 INFO Live micro hold S210 CELH260821C00030000 -11.4% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-18 12:11:02,639 INFO Live micro: manage/exits only
Live micro done. open_options=3 lots=3
2026-08-18 12:11:02,719 INFO Live micro done. open_options=3 lots=3
```

### Paper options bot full output

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T162203Z

- UTC timestamp: `20260818T162203Z`
- GitHub run: [#7376](https://github.com/28twagg-ops/TradingBot/actions/runs/32159718436)
- Run id: `32159718436`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`

### Live bot full output

```text
16:22:04  INFO      Mode: exits
16:22:04  INFO        Daily log -> logs/daily/2026-08-18.md
16:22:04  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (4 ledger rows)
16:22:04  INFO        place_all_stops: checking 4 positions...
16:22:04  INFO        STOP skipped AON: fractional (0.2011 shares) — software exit will handle it
16:22:04  INFO        [positions] 1/1 (1 valid)
16:22:05  INFO        Daily log -> logs/daily/2026-08-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:22 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $500.97|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AON  P&L -0.5%  $-0.34                                            HOLD|
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
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00412500     $0.31    $0.23    -25.8%   $-8.00    $23.00   |
|  CELH260821C00030000     $0.70    $0.63    -10.0%   $-7.00    $63.00   |
|  NKE260821C00040000      $0.54    $0.69    +27.8%   $+15.00   $69.00   |
|                                                                        |
|  Options open P&L                                                $+0.00|
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

### Live options micro full output

```text
=== options_live_micro LIVE 2026-08-18T12:22:05.818822-04:00 share=50% ===
2026-08-18 12:22:05,818 INFO === options_live_micro LIVE 2026-08-18T12:22:05.818822-04:00 share=50% ===
Live account equity $495.97 cash $276.21 #225458845 options_level=3
2026-08-18 12:22:05,881 INFO Live account equity $495.97 cash $276.21 #225458845 options_level=3
Live micro hold S404 AVGO260821C00412500 -25.8% (tp +50% / sl -50%)
2026-08-18 12:22:05,908 INFO Live micro hold S404 AVGO260821C00412500 -25.8% (tp +50% / sl -50%)
Live micro hold S218 NKE260821C00040000 +27.8% (tp +50% / sl -50%)
2026-08-18 12:22:05,908 INFO Live micro hold S218 NKE260821C00040000 +27.8% (tp +50% / sl -50%)
Live micro hold S210 CELH260821C00030000 -17.1% (tp +50% / sl -50%)
2026-08-18 12:22:05,909 INFO Live micro hold S210 CELH260821C00030000 -17.1% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-18 12:22:05,962 INFO Live micro: manage/exits only
Live micro done. open_options=3 lots=3
2026-08-18 12:22:05,975 INFO Live micro done. open_options=3 lots=3
```

### Paper options bot full output

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T162554Z

- UTC timestamp: `20260818T162554Z`
- GitHub run: [#7377](https://github.com/28twagg-ops/TradingBot/actions/runs/32160177063)
- Run id: `32160177063`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`

### Live bot full output

```text
16:25:55  INFO      Mode: exits
16:25:56  INFO        Daily log -> logs/daily/2026-08-18.md
16:25:56  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (4 ledger rows)
16:25:56  INFO        place_all_stops: checking 4 positions...
16:25:56  INFO        STOP skipped AON: fractional (0.2011 shares) — software exit will handle it
16:25:56  INFO        [positions] 1/1 (1 valid)
16:25:57  INFO        Daily log -> logs/daily/2026-08-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:25 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $502.11|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AON  P&L -0.3%  $-0.20                                            HOLD|
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
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00412500     $0.31    $0.23    -25.8%   $-8.00    $23.00   |
|  CELH260821C00030000     $0.70    $0.59    -15.7%   $-11.00   $59.00   |
|  NKE260821C00040000      $0.54    $0.74    +37.0%   $+20.00   $74.00   |
|                                                                        |
|  Options open P&L                                                $+1.00|
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

### Live options micro full output

```text
=== options_live_micro LIVE 2026-08-18T12:25:57.927255-04:00 share=50% ===
2026-08-18 12:25:57,927 INFO === options_live_micro LIVE 2026-08-18T12:25:57.927255-04:00 share=50% ===
Live account equity $502.11 cash $276.21 #225458845 options_level=3
2026-08-18 12:25:58,176 INFO Live account equity $502.11 cash $276.21 #225458845 options_level=3
Live micro hold S404 AVGO260821C00412500 -25.8% (tp +50% / sl -50%)
2026-08-18 12:25:58,330 INFO Live micro hold S404 AVGO260821C00412500 -25.8% (tp +50% / sl -50%)
Live micro hold S218 NKE260821C00040000 +37.0% (tp +50% / sl -50%)
2026-08-18 12:25:58,330 INFO Live micro hold S218 NKE260821C00040000 +37.0% (tp +50% / sl -50%)
Live micro hold S210 CELH260821C00030000 -15.7% (tp +50% / sl -50%)
2026-08-18 12:25:58,331 INFO Live micro hold S210 CELH260821C00030000 -15.7% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-18 12:25:58,628 INFO Live micro: manage/exits only
Live micro done. open_options=3 lots=3
2026-08-18 12:25:58,711 INFO Live micro done. open_options=3 lots=3
```

### Paper options bot full output

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T163650Z

- UTC timestamp: `20260818T163650Z`
- GitHub run: [#7379](https://github.com/28twagg-ops/TradingBot/actions/runs/32161075021)
- Run id: `32161075021`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`0s`

### Live bot full output

```text
16:36:51  INFO      Mode: exits
16:36:52  INFO        Daily log -> logs/daily/2026-08-18.md
16:36:52  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (4 ledger rows)
16:36:52  INFO        place_all_stops: checking 4 positions...
16:36:52  INFO        STOP skipped AON: fractional (0.2011 shares) — software exit will handle it
16:36:52  INFO        [positions] 1/1 (1 valid)
16:36:52  INFO        Daily log -> logs/daily/2026-08-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $491.98|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AON  P&L -0.5%  $-0.33                                            HOLD|
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
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00412500     $0.31    $0.23    -25.8%   $-8.00    $23.00   |
|  CELH260821C00030000     $0.70    $0.57    -18.6%   $-13.00   $57.00   |
|  NKE260821C00040000      $0.54    $0.66    +22.2%   $+12.00   $66.00   |
|                                                                        |
|  Options open P&L                                                $-9.00|
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

### Live options micro full output

```text
=== options_live_micro LIVE 2026-08-18T12:36:53.359112-04:00 share=50% ===
2026-08-18 12:36:53,359 INFO === options_live_micro LIVE 2026-08-18T12:36:53.359112-04:00 share=50% ===
Live account equity $491.98 cash $276.21 #225458845 options_level=3
2026-08-18 12:36:53,567 INFO Live account equity $491.98 cash $276.21 #225458845 options_level=3
Live micro hold S404 AVGO260821C00412500 -25.8% (tp +50% / sl -50%)
2026-08-18 12:36:53,707 INFO Live micro hold S404 AVGO260821C00412500 -25.8% (tp +50% / sl -50%)
Live micro hold S218 NKE260821C00040000 +22.2% (tp +50% / sl -50%)
2026-08-18 12:36:53,707 INFO Live micro hold S218 NKE260821C00040000 +22.2% (tp +50% / sl -50%)
Live micro hold S210 CELH260821C00030000 -18.6% (tp +50% / sl -50%)
2026-08-18 12:36:53,707 INFO Live micro hold S210 CELH260821C00030000 -18.6% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-18 12:36:53,939 INFO Live micro: manage/exits only
Live micro done. open_options=3 lots=3
2026-08-18 12:36:53,997 INFO Live micro done. open_options=3 lots=3
```

### Paper options bot full output

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T164350Z

- UTC timestamp: `20260818T164350Z`
- GitHub run: [#7380](https://github.com/28twagg-ops/TradingBot/actions/runs/32161509002)
- Run id: `32161509002`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`0s`

### Live bot full output

```text
16:43:51  INFO      Mode: exits
16:43:51  INFO        Daily log -> logs/daily/2026-08-18.md
16:43:51  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (4 ledger rows)
16:43:51  INFO        place_all_stops: checking 4 positions...
16:43:51  INFO        STOP skipped AON: fractional (0.2011 shares) — software exit will handle it
16:43:52  INFO        [positions] 1/1 (1 valid)
16:43:52  INFO        Daily log -> logs/daily/2026-08-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:43 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $496.01|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AON  P&L -0.4%  $-0.30                                            HOLD|
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
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00412500     $0.31    $0.23    -25.8%   $-8.00    $23.00   |
|  CELH260821C00030000     $0.70    $0.57    -18.6%   $-13.00   $57.00   |
|  NKE260821C00040000      $0.54    $0.70    +29.6%   $+16.00   $70.00   |
|                                                                        |
|  Options open P&L                                                $-5.00|
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

### Live options micro full output

```text
=== options_live_micro LIVE 2026-08-18T12:43:53.208413-04:00 share=50% ===
2026-08-18 12:43:53,208 INFO === options_live_micro LIVE 2026-08-18T12:43:53.208413-04:00 share=50% ===
Live account equity $496.01 cash $276.21 #225458845 options_level=3
2026-08-18 12:43:53,444 INFO Live account equity $496.01 cash $276.21 #225458845 options_level=3
Live micro hold S404 AVGO260821C00412500 -25.8% (tp +50% / sl -50%)
2026-08-18 12:43:53,592 INFO Live micro hold S404 AVGO260821C00412500 -25.8% (tp +50% / sl -50%)
Live micro hold S218 NKE260821C00040000 +29.6% (tp +50% / sl -50%)
2026-08-18 12:43:53,593 INFO Live micro hold S218 NKE260821C00040000 +29.6% (tp +50% / sl -50%)
Live micro hold S210 CELH260821C00030000 -18.6% (tp +50% / sl -50%)
2026-08-18 12:43:53,593 INFO Live micro hold S210 CELH260821C00030000 -18.6% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-18 12:43:53,829 INFO Live micro: manage/exits only
Live micro done. open_options=3 lots=3
2026-08-18 12:43:53,889 INFO Live micro done. open_options=3 lots=3
```

### Paper options bot full output

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T164639Z

- UTC timestamp: `20260818T164639Z`
- GitHub run: [#7381](https://github.com/28twagg-ops/TradingBot/actions/runs/32161955939)
- Run id: `32161955939`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`

### Live bot full output

```text
16:46:40  INFO      Mode: exits
16:46:41  INFO        Daily log -> logs/daily/2026-08-18.md
16:46:41  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (4 ledger rows)
16:46:41  INFO        place_all_stops: checking 4 positions...
16:46:41  INFO        STOP skipped AON: fractional (0.2011 shares) — software exit will handle it
16:46:42  INFO        [positions] 1/1 (1 valid)
16:46:42  INFO        Daily log -> logs/daily/2026-08-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $499.01|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AON  P&L -0.4%  $-0.30                                            HOLD|
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
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00412500     $0.31    $0.23    -25.8%   $-8.00    $23.00   |
|  CELH260821C00030000     $0.70    $0.59    -15.7%   $-11.00   $59.00   |
|  NKE260821C00040000      $0.54    $0.71    +31.5%   $+17.00   $71.00   |
|                                                                        |
|  Options open P&L                                                $-2.00|
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

### Live options micro full output

```text
=== options_live_micro LIVE 2026-08-18T12:46:42.982234-04:00 share=50% ===
2026-08-18 12:46:42,982 INFO === options_live_micro LIVE 2026-08-18T12:46:42.982234-04:00 share=50% ===
Live account equity $499.01 cash $276.21 #225458845 options_level=3
2026-08-18 12:46:43,202 INFO Live account equity $499.01 cash $276.21 #225458845 options_level=3
Live micro hold S404 AVGO260821C00412500 -25.8% (tp +50% / sl -50%)
2026-08-18 12:46:43,331 INFO Live micro hold S404 AVGO260821C00412500 -25.8% (tp +50% / sl -50%)
Live micro hold S218 NKE260821C00040000 +31.5% (tp +50% / sl -50%)
2026-08-18 12:46:43,332 INFO Live micro hold S218 NKE260821C00040000 +31.5% (tp +50% / sl -50%)
Live micro hold S210 CELH260821C00030000 -15.7% (tp +50% / sl -50%)
2026-08-18 12:46:43,332 INFO Live micro hold S210 CELH260821C00030000 -15.7% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-18 12:46:43,585 INFO Live micro: manage/exits only
Live micro done. open_options=3 lots=3
2026-08-18 12:46:43,711 INFO Live micro done. open_options=3 lots=3
```

### Paper options bot full output

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T165051Z

- UTC timestamp: `20260818T165051Z`
- GitHub run: [#7382](https://github.com/28twagg-ops/TradingBot/actions/runs/32162394711)
- Run id: `32162394711`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`

### Live bot full output

```text
16:50:52  INFO      Mode: exits
16:50:52  INFO        Daily log -> logs/daily/2026-08-18.md
16:50:52  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (4 ledger rows)
16:50:52  INFO        place_all_stops: checking 4 positions...
16:50:52  INFO        STOP skipped AON: fractional (0.2011 shares) — software exit will handle it
16:50:52  INFO        [positions] 1/1 (1 valid)
16:50:52  INFO        Daily log -> logs/daily/2026-08-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:50 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $499.98|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AON  P&L -0.5%  $-0.33                                            HOLD|
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
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00412500     $0.31    $0.23    -25.8%   $-8.00    $23.00   |
|  CELH260821C00030000     $0.70    $0.62    -11.4%   $-8.00    $62.00   |
|  NKE260821C00040000      $0.54    $0.69    +27.8%   $+15.00   $69.00   |
|                                                                        |
|  Options open P&L                                                $-1.00|
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

### Live options micro full output

```text
=== options_live_micro LIVE 2026-08-18T12:50:53.518482-04:00 share=50% ===
2026-08-18 12:50:53,518 INFO === options_live_micro LIVE 2026-08-18T12:50:53.518482-04:00 share=50% ===
Live account equity $499.98 cash $276.21 #225458845 options_level=3
2026-08-18 12:50:53,589 INFO Live account equity $499.98 cash $276.21 #225458845 options_level=3
Live micro hold S404 AVGO260821C00412500 -25.8% (tp +50% / sl -50%)
2026-08-18 12:50:53,615 INFO Live micro hold S404 AVGO260821C00412500 -25.8% (tp +50% / sl -50%)
Live micro hold S218 NKE260821C00040000 +27.8% (tp +50% / sl -50%)
2026-08-18 12:50:53,615 INFO Live micro hold S218 NKE260821C00040000 +27.8% (tp +50% / sl -50%)
Live micro hold S210 CELH260821C00030000 -11.4% (tp +50% / sl -50%)
2026-08-18 12:50:53,615 INFO Live micro hold S210 CELH260821C00030000 -11.4% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-18 12:50:53,665 INFO Live micro: manage/exits only
Live micro done. open_options=3 lots=3
2026-08-18 12:50:53,679 INFO Live micro done. open_options=3 lots=3
```

### Paper options bot full output

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T171559Z

- UTC timestamp: `20260818T171559Z`
- GitHub run: [#7387](https://github.com/28twagg-ops/TradingBot/actions/runs/32164602110)
- Run id: `32164602110`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260818T171559Z_live_bot.log`, `logs/action_runs/20260818T171559Z_live_options.log`, `logs/action_runs/20260818T171559Z_options_bot.log`

### Live bot (tail)

```text
17:16:00  INFO      Mode: exits
17:16:00  INFO        Daily log -> logs/daily/2026-08-18.md
17:16:00  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (4 ledger rows)
17:16:01  INFO        place_all_stops: checking 4 positions...
17:16:01  INFO        STOP skipped AON: fractional (0.2011 shares) — software exit will handle it
17:16:01  INFO        [positions] 1/1 (1 valid)
17:16:01  INFO        Daily log -> logs/daily/2026-08-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $482.04|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AON  P&L -0.4%  $-0.27                                            HOLD|
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
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00412500     $0.31    $0.21    -32.3%   $-10.00   $21.00   |
|  CELH260821C00030000     $0.70    $0.50    -28.6%   $-20.00   $50.00   |
|  NKE260821C00040000      $0.54    $0.65    +20.4%   $+11.00   $65.00   |
|                                                                        |
|  Options open P&L                                               $-19.00|
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
=== options_live_micro LIVE 2026-08-18T13:16:02.347624-04:00 share=50% ===
2026-08-18 13:16:02,347 INFO === options_live_micro LIVE 2026-08-18T13:16:02.347624-04:00 share=50% ===
Live account equity $482.04 cash $276.21 #225458845 options_level=3
2026-08-18 13:16:02,523 INFO Live account equity $482.04 cash $276.21 #225458845 options_level=3
Live micro hold S404 AVGO260821C00412500 -32.3% (tp +50% / sl -50%)
2026-08-18 13:16:02,607 INFO Live micro hold S404 AVGO260821C00412500 -32.3% (tp +50% / sl -50%)
Live micro hold S218 NKE260821C00040000 +20.4% (tp +50% / sl -50%)
2026-08-18 13:16:02,607 INFO Live micro hold S218 NKE260821C00040000 +20.4% (tp +50% / sl -50%)
Live micro hold S210 CELH260821C00030000 -28.6% (tp +50% / sl -50%)
2026-08-18 13:16:02,607 INFO Live micro hold S210 CELH260821C00030000 -28.6% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-18 13:16:02,759 INFO Live micro: manage/exits only
Live micro done. open_options=3 lots=3
2026-08-18 13:16:02,802 INFO Live micro done. open_options=3 lots=3
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T172057Z

- UTC timestamp: `20260818T172057Z`
- GitHub run: [#7388](https://github.com/28twagg-ops/TradingBot/actions/runs/32165041229)
- Run id: `32165041229`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260818T172057Z_live_bot.log`, `logs/action_runs/20260818T172057Z_live_options.log`, `logs/action_runs/20260818T172057Z_options_bot.log`

### Live bot (tail)

```text
17:20:58  INFO      Mode: exits
17:20:59  INFO        Daily log -> logs/daily/2026-08-18.md
17:20:59  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (4 ledger rows)
17:20:59  INFO        place_all_stops: checking 4 positions...
17:20:59  INFO        STOP skipped AON: fractional (0.2011 shares) — software exit will handle it
17:20:59  INFO        [positions] 1/1 (1 valid)
17:20:59  INFO        Daily log -> logs/daily/2026-08-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $483.99|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AON  P&L -0.5%  $-0.32                                            HOLD|
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
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00412500     $0.31    $0.21    -32.3%   $-10.00   $21.00   |
|  CELH260821C00030000     $0.70    $0.50    -28.6%   $-20.00   $50.00   |
|  NKE260821C00040000      $0.54    $0.67    +24.1%   $+13.00   $67.00   |
|                                                                        |
|  Options open P&L                                               $-17.00|
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
=== options_live_micro LIVE 2026-08-18T13:21:00.765321-04:00 share=50% ===
2026-08-18 13:21:00,765 INFO === options_live_micro LIVE 2026-08-18T13:21:00.765321-04:00 share=50% ===
Live account equity $483.99 cash $276.21 #225458845 options_level=3
2026-08-18 13:21:00,991 INFO Live account equity $483.99 cash $276.21 #225458845 options_level=3
Live micro hold S404 AVGO260821C00412500 -32.3% (tp +50% / sl -50%)
2026-08-18 13:21:01,114 INFO Live micro hold S404 AVGO260821C00412500 -32.3% (tp +50% / sl -50%)
Live micro hold S218 NKE260821C00040000 +24.1% (tp +50% / sl -50%)
2026-08-18 13:21:01,114 INFO Live micro hold S218 NKE260821C00040000 +24.1% (tp +50% / sl -50%)
Live micro hold S210 CELH260821C00030000 -28.6% (tp +50% / sl -50%)
2026-08-18 13:21:01,114 INFO Live micro hold S210 CELH260821C00030000 -28.6% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-18 13:21:01,356 INFO Live micro: manage/exits only
Live micro done. open_options=3 lots=3
2026-08-18 13:21:01,416 INFO Live micro done. open_options=3 lots=3
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T172603Z

- UTC timestamp: `20260818T172603Z`
- GitHub run: [#7389](https://github.com/28twagg-ops/TradingBot/actions/runs/32165485040)
- Run id: `32165485040`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260818T172603Z_live_bot.log`, `logs/action_runs/20260818T172603Z_live_options.log`, `logs/action_runs/20260818T172603Z_options_bot.log`

### Live bot (tail)

```text
17:26:04  INFO      Mode: exits
17:26:05  INFO        Daily log -> logs/daily/2026-08-18.md
17:26:05  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (4 ledger rows)
17:26:05  INFO        place_all_stops: checking 4 positions...
17:26:05  INFO        STOP skipped AON: fractional (0.2011 shares) — software exit will handle it
17:26:05  INFO        [positions] 1/1 (1 valid)
17:26:05  INFO        Daily log -> logs/daily/2026-08-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $489.04|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AON  P&L -0.4%  $-0.27                                            HOLD|
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
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00412500     $0.31    $0.21    -32.3%   $-10.00   $21.00   |
|  CELH260821C00030000     $0.70    $0.52    -25.7%   $-18.00   $52.00   |
|  NKE260821C00040000      $0.54    $0.70    +29.6%   $+16.00   $70.00   |
|                                                                        |
|  Options open P&L                                               $-12.00|
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
=== options_live_micro LIVE 2026-08-18T13:26:06.608620-04:00 share=50% ===
2026-08-18 13:26:06,608 INFO === options_live_micro LIVE 2026-08-18T13:26:06.608620-04:00 share=50% ===
Live account equity $489.04 cash $276.21 #225458845 options_level=3
2026-08-18 13:26:06,670 INFO Live account equity $489.04 cash $276.21 #225458845 options_level=3
Live micro hold S404 AVGO260821C00412500 -32.3% (tp +50% / sl -50%)
2026-08-18 13:26:06,702 INFO Live micro hold S404 AVGO260821C00412500 -32.3% (tp +50% / sl -50%)
Live micro hold S218 NKE260821C00040000 +29.6% (tp +50% / sl -50%)
2026-08-18 13:26:06,703 INFO Live micro hold S218 NKE260821C00040000 +29.6% (tp +50% / sl -50%)
Live micro hold S210 CELH260821C00030000 -25.7% (tp +50% / sl -50%)
2026-08-18 13:26:06,703 INFO Live micro hold S210 CELH260821C00030000 -25.7% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-18 13:26:06,760 INFO Live micro: manage/exits only
Live micro done. open_options=3 lots=3
2026-08-18 13:26:06,774 INFO Live micro done. open_options=3 lots=3
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T173058Z

- UTC timestamp: `20260818T173058Z`
- GitHub run: [#7390](https://github.com/28twagg-ops/TradingBot/actions/runs/32165923157)
- Run id: `32165923157`
- Live bot: exit=`0`, duration=`5s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260818T173058Z_live_bot.log`, `logs/action_runs/20260818T173058Z_live_options.log`, `logs/action_runs/20260818T173058Z_options_bot.log`

### Live bot (tail)

```text
17:30:59  INFO      Mode: exits
17:31:00  INFO        Daily log -> logs/daily/2026-08-18.md
17:31:00  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (4 ledger rows)
17:31:00  INFO        place_all_stops: checking 4 positions...
17:31:00  INFO        STOP skipped AON: fractional (0.2011 shares) — software exit will handle it
17:31:00  INFO        [positions] 1/1 (1 valid)
17:31:00  INFO        SELL MARKET [urgent] AON closed
17:31:02  INFO        TX logged: SELL AON  P&L -0.51%
17:31:03  INFO        Daily log -> logs/daily/2026-08-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:30 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $483.95|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AON  P&L -0.5%  $-0.36                         EXIT: stop_loss (-0.5%)|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  1 attempted  |  1 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
|  Logged exits                                                         1|
+========================================================================+

+========================================================================+
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00412500     $0.31    $0.21    -32.3%   $-10.00   $21.00   |
|  CELH260821C00030000     $0.70    $0.49    -30.0%   $-21.00   $49.00   |
|  NKE260821C00040000      $0.54    $0.66    +22.2%   $+12.00   $66.00   |
|                                                                        |
|  Options open P&L                                               $-19.00|
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  AON                                         -0.51%  (threshold -0.50%)|
|  Count                                                                1|
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-18T13:31:03.866488-04:00 share=50% ===
2026-08-18 13:31:03,866 INFO === options_live_micro LIVE 2026-08-18T13:31:03.866488-04:00 share=50% ===
Live account equity $481.93 cash $345.93 #225458845 options_level=3
2026-08-18 13:31:04,109 INFO Live account equity $481.93 cash $345.93 #225458845 options_level=3
Live micro hold S404 AVGO260821C00412500 -32.3% (tp +50% / sl -50%)
2026-08-18 13:31:04,230 INFO Live micro hold S404 AVGO260821C00412500 -32.3% (tp +50% / sl -50%)
Live micro hold S218 NKE260821C00040000 +22.2% (tp +50% / sl -50%)
2026-08-18 13:31:04,231 INFO Live micro hold S218 NKE260821C00040000 +22.2% (tp +50% / sl -50%)
Live micro hold S210 CELH260821C00030000 -30.0% (tp +50% / sl -50%)
2026-08-18 13:31:04,231 INFO Live micro hold S210 CELH260821C00030000 -30.0% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-18 13:31:04,501 INFO Live micro: manage/exits only
Live micro done. open_options=3 lots=3
2026-08-18 13:31:04,562 INFO Live micro done. open_options=3 lots=3
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T173553Z

- UTC timestamp: `20260818T173553Z`
- GitHub run: [#7391](https://github.com/28twagg-ops/TradingBot/actions/runs/32166368138)
- Run id: `32166368138`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260818T173553Z_live_bot.log`, `logs/action_runs/20260818T173553Z_live_options.log`, `logs/action_runs/20260818T173553Z_options_bot.log`

### Live bot (tail)

```text
17:35:54  INFO      Mode: exits
17:35:54  INFO        Daily log -> logs/daily/2026-08-18.md
17:35:54  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (5 ledger rows)
17:35:55  INFO        place_all_stops: checking 3 positions...

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:35 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $473.93|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open positions.                                                    |
|                                                                        |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-18T13:35:55.907227-04:00 share=50% ===
2026-08-18 13:35:55,907 INFO === options_live_micro LIVE 2026-08-18T13:35:55.907227-04:00 share=50% ===
Live account equity $473.93 cash $345.93 #225458845 options_level=3
2026-08-18 13:35:56,009 INFO Live account equity $473.93 cash $345.93 #225458845 options_level=3
Live micro hold S404 AVGO260821C00412500 -32.3% (tp +50% / sl -50%)
2026-08-18 13:35:56,069 INFO Live micro hold S404 AVGO260821C00412500 -32.3% (tp +50% / sl -50%)
Live micro hold S218 NKE260821C00040000 +13.0% (tp +50% / sl -50%)
2026-08-18 13:35:56,069 INFO Live micro hold S218 NKE260821C00040000 +13.0% (tp +50% / sl -50%)
Live micro hold S210 CELH260821C00030000 -34.3% (tp +50% / sl -50%)
2026-08-18 13:35:56,069 INFO Live micro hold S210 CELH260821C00030000 -34.3% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-18 13:35:56,179 INFO Live micro: manage/exits only
Live micro done. open_options=3 lots=3
2026-08-18 13:35:56,213 INFO Live micro done. open_options=3 lots=3
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T174053Z

- UTC timestamp: `20260818T174053Z`
- GitHub run: [#7392](https://github.com/28twagg-ops/TradingBot/actions/runs/32166810649)
- Run id: `32166810649`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260818T174053Z_live_bot.log`, `logs/action_runs/20260818T174053Z_live_options.log`, `logs/action_runs/20260818T174053Z_options_bot.log`

### Live bot (tail)

```text
17:40:54  INFO      Mode: exits
17:40:54  INFO        Daily log -> logs/daily/2026-08-18.md
17:40:54  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (5 ledger rows)
17:40:55  INFO        place_all_stops: checking 3 positions...

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:40 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $476.93|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open positions.                                                    |
|                                                                        |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-18T13:40:55.857757-04:00 share=50% ===
2026-08-18 13:40:55,857 INFO === options_live_micro LIVE 2026-08-18T13:40:55.857757-04:00 share=50% ===
Live account equity $476.93 cash $345.93 #225458845 options_level=3
2026-08-18 13:40:55,970 INFO Live account equity $476.93 cash $345.93 #225458845 options_level=3
Live micro hold S404 AVGO260821C00412500 -32.3% (tp +50% / sl -50%)
2026-08-18 13:40:56,024 INFO Live micro hold S404 AVGO260821C00412500 -32.3% (tp +50% / sl -50%)
Live micro hold S218 NKE260821C00040000 +11.1% (tp +50% / sl -50%)
2026-08-18 13:40:56,025 INFO Live micro hold S218 NKE260821C00040000 +11.1% (tp +50% / sl -50%)
Live micro hold S210 CELH260821C00030000 -28.6% (tp +50% / sl -50%)
2026-08-18 13:40:56,025 INFO Live micro hold S210 CELH260821C00030000 -28.6% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-18 13:40:56,131 INFO Live micro: manage/exits only
Live micro done. open_options=3 lots=3
2026-08-18 13:40:56,156 INFO Live micro done. open_options=3 lots=3
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T174604Z

- UTC timestamp: `20260818T174604Z`
- GitHub run: [#7393](https://github.com/28twagg-ops/TradingBot/actions/runs/32167259279)
- Run id: `32167259279`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260818T174604Z_live_bot.log`, `logs/action_runs/20260818T174604Z_live_options.log`, `logs/action_runs/20260818T174604Z_options_bot.log`

### Live bot (tail)

```text
17:46:05  INFO      Mode: exits
17:46:05  INFO        Daily log -> logs/daily/2026-08-18.md
17:46:05  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (5 ledger rows)
17:46:05  INFO        place_all_stops: checking 3 positions...

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $476.93|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open positions.                                                    |
|                                                                        |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-18T13:46:06.621296-04:00 share=50% ===
2026-08-18 13:46:06,621 INFO === options_live_micro LIVE 2026-08-18T13:46:06.621296-04:00 share=50% ===
Live account equity $476.93 cash $345.93 #225458845 options_level=3
2026-08-18 13:46:06,664 INFO Live account equity $476.93 cash $345.93 #225458845 options_level=3
Live micro hold S404 AVGO260821C00412500 -29.0% (tp +50% / sl -50%)
2026-08-18 13:46:06,697 INFO Live micro hold S404 AVGO260821C00412500 -29.0% (tp +50% / sl -50%)
Live micro hold S218 NKE260821C00040000 +9.3% (tp +50% / sl -50%)
2026-08-18 13:46:06,697 INFO Live micro hold S218 NKE260821C00040000 +9.3% (tp +50% / sl -50%)
Live micro hold S210 CELH260821C00030000 -28.6% (tp +50% / sl -50%)
2026-08-18 13:46:06,697 INFO Live micro hold S210 CELH260821C00030000 -28.6% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-18 13:46:06,736 INFO Live micro: manage/exits only
Live micro done. open_options=3 lots=3
2026-08-18 13:46:06,749 INFO Live micro done. open_options=3 lots=3
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T175054Z

- UTC timestamp: `20260818T175054Z`
- GitHub run: [#7394](https://github.com/28twagg-ops/TradingBot/actions/runs/32167708212)
- Run id: `32167708212`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260818T175054Z_live_bot.log`, `logs/action_runs/20260818T175054Z_live_options.log`, `logs/action_runs/20260818T175054Z_options_bot.log`

### Live bot (tail)

```text
17:50:55  INFO      Mode: exits
17:50:56  INFO        Daily log -> logs/daily/2026-08-18.md
17:50:56  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (5 ledger rows)
17:50:56  INFO        place_all_stops: checking 3 positions...

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:50 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $477.93|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open positions.                                                    |
|                                                                        |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-18T13:50:56.976314-04:00 share=50% ===
2026-08-18 13:50:56,976 INFO === options_live_micro LIVE 2026-08-18T13:50:56.976314-04:00 share=50% ===
Live account equity $477.93 cash $345.93 #225458845 options_level=3
2026-08-18 13:50:57,038 INFO Live account equity $477.93 cash $345.93 #225458845 options_level=3
Live micro hold S404 AVGO260821C00412500 -29.0% (tp +50% / sl -50%)
2026-08-18 13:50:57,070 INFO Live micro hold S404 AVGO260821C00412500 -29.0% (tp +50% / sl -50%)
Live micro hold S218 NKE260821C00040000 +11.1% (tp +50% / sl -50%)
2026-08-18 13:50:57,070 INFO Live micro hold S218 NKE260821C00040000 +11.1% (tp +50% / sl -50%)
Live micro hold S210 CELH260821C00030000 -28.6% (tp +50% / sl -50%)
2026-08-18 13:50:57,070 INFO Live micro hold S210 CELH260821C00030000 -28.6% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-18 13:50:57,122 INFO Live micro: manage/exits only
Live micro done. open_options=3 lots=3
2026-08-18 13:50:57,135 INFO Live micro done. open_options=3 lots=3
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T175555Z

- UTC timestamp: `20260818T175555Z`
- GitHub run: [#7395](https://github.com/28twagg-ops/TradingBot/actions/runs/32168154680)
- Run id: `32168154680`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260818T175555Z_live_bot.log`, `logs/action_runs/20260818T175555Z_live_options.log`, `logs/action_runs/20260818T175555Z_options_bot.log`

### Live bot (tail)

```text
17:55:56  INFO      Mode: exits
17:55:56  INFO        Daily log -> logs/daily/2026-08-18.md
17:55:56  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (5 ledger rows)
17:55:56  INFO        place_all_stops: checking 3 positions...

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:55 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $483.93|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open positions.                                                    |
|                                                                        |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-18T13:55:57.693449-04:00 share=50% ===
2026-08-18 13:55:57,693 INFO === options_live_micro LIVE 2026-08-18T13:55:57.693449-04:00 share=50% ===
Live account equity $483.93 cash $345.93 #225458845 options_level=3
2026-08-18 13:55:57,863 INFO Live account equity $483.93 cash $345.93 #225458845 options_level=3
Live micro hold S404 AVGO260821C00412500 -32.3% (tp +50% / sl -50%)
2026-08-18 13:55:57,900 INFO Live micro hold S404 AVGO260821C00412500 -32.3% (tp +50% / sl -50%)
Live micro hold S218 NKE260821C00040000 +11.1% (tp +50% / sl -50%)
2026-08-18 13:55:57,900 INFO Live micro hold S218 NKE260821C00040000 +11.1% (tp +50% / sl -50%)
Live micro hold S210 CELH260821C00030000 -18.6% (tp +50% / sl -50%)
2026-08-18 13:55:57,900 INFO Live micro hold S210 CELH260821C00030000 -18.6% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-18 13:55:57,951 INFO Live micro: manage/exits only
Live micro done. open_options=3 lots=3
2026-08-18 13:55:57,964 INFO Live micro done. open_options=3 lots=3
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T180115Z

- UTC timestamp: `20260818T180115Z`
- GitHub run: [#7396](https://github.com/28twagg-ops/TradingBot/actions/runs/32168600553)
- Run id: `32168600553`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260818T180115Z_live_bot.log`, `logs/action_runs/20260818T180115Z_live_options.log`, `logs/action_runs/20260818T180115Z_options_bot.log`

### Live bot (tail)

```text
18:01:16  INFO      Mode: exits
18:01:17  INFO        Daily log -> logs/daily/2026-08-18.md
18:01:17  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (5 ledger rows)
18:01:17  INFO        place_all_stops: checking 3 positions...

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $479.93|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open positions.                                                    |
|                                                                        |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-18T14:01:18.886677-04:00 share=50% ===
2026-08-18 14:01:18,886 INFO === options_live_micro LIVE 2026-08-18T14:01:18.886677-04:00 share=50% ===
Live account equity $479.93 cash $345.93 #225458845 options_level=3
2026-08-18 14:01:19,126 INFO Live account equity $479.93 cash $345.93 #225458845 options_level=3
Live micro hold S404 AVGO260821C00412500 -32.3% (tp +50% / sl -50%)
2026-08-18 14:01:19,287 INFO Live micro hold S404 AVGO260821C00412500 -32.3% (tp +50% / sl -50%)
Live micro hold S218 NKE260821C00040000 +16.7% (tp +50% / sl -50%)
2026-08-18 14:01:19,287 INFO Live micro hold S218 NKE260821C00040000 +16.7% (tp +50% / sl -50%)
Live micro hold S210 CELH260821C00030000 -28.6% (tp +50% / sl -50%)
2026-08-18 14:01:19,287 INFO Live micro hold S210 CELH260821C00030000 -28.6% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-18 14:01:19,592 INFO Live micro: manage/exits only
Live micro done. open_options=3 lots=3
2026-08-18 14:01:19,667 INFO Live micro done. open_options=3 lots=3
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T180558Z

- UTC timestamp: `20260818T180558Z`
- GitHub run: [#7397](https://github.com/28twagg-ops/TradingBot/actions/runs/32169058055)
- Run id: `32169058055`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260818T180558Z_live_bot.log`, `logs/action_runs/20260818T180558Z_live_options.log`, `logs/action_runs/20260818T180558Z_options_bot.log`

### Live bot (tail)

```text
18:05:59  INFO      Mode: exits
18:06:00  INFO        Daily log -> logs/daily/2026-08-18.md
18:06:00  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (5 ledger rows)
18:06:00  INFO        place_all_stops: checking 3 positions...

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $480.93|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open positions.                                                    |
|                                                                        |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-18T14:06:01.693055-04:00 share=50% ===
2026-08-18 14:06:01,693 INFO === options_live_micro LIVE 2026-08-18T14:06:01.693055-04:00 share=50% ===
Live account equity $480.93 cash $345.93 #225458845 options_level=3
2026-08-18 14:06:01,938 INFO Live account equity $480.93 cash $345.93 #225458845 options_level=3
Live micro hold S404 AVGO260821C00412500 -32.3% (tp +50% / sl -50%)
2026-08-18 14:06:02,193 INFO Live micro hold S404 AVGO260821C00412500 -32.3% (tp +50% / sl -50%)
Live micro hold S218 NKE260821C00040000 +18.5% (tp +50% / sl -50%)
2026-08-18 14:06:02,194 INFO Live micro hold S218 NKE260821C00040000 +18.5% (tp +50% / sl -50%)
Live micro hold S210 CELH260821C00030000 -28.6% (tp +50% / sl -50%)
2026-08-18 14:06:02,194 INFO Live micro hold S210 CELH260821C00030000 -28.6% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-18 14:06:02,492 INFO Live micro: manage/exits only
Live micro done. open_options=3 lots=3
2026-08-18 14:06:02,570 INFO Live micro done. open_options=3 lots=3
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T181223Z

- UTC timestamp: `20260818T181223Z`
- GitHub run: [#7398](https://github.com/28twagg-ops/TradingBot/actions/runs/32169511086)
- Run id: `32169511086`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260818T181223Z_live_bot.log`, `logs/action_runs/20260818T181223Z_live_options.log`, `logs/action_runs/20260818T181223Z_options_bot.log`

### Live bot (tail)

```text
18:12:24  INFO      Mode: exits
18:12:24  INFO        Daily log -> logs/daily/2026-08-18.md
18:12:24  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (5 ledger rows)
18:12:24  INFO        place_all_stops: checking 3 positions...

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:12 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $489.93|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open positions.                                                    |
|                                                                        |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-18T14:12:25.382487-04:00 share=50% ===
2026-08-18 14:12:25,382 INFO === options_live_micro LIVE 2026-08-18T14:12:25.382487-04:00 share=50% ===
Live account equity $489.93 cash $345.93 #225458845 options_level=3
2026-08-18 14:12:25,431 INFO Live account equity $489.93 cash $345.93 #225458845 options_level=3
Live micro hold S404 AVGO260821C00412500 -35.5% (tp +50% / sl -50%)
2026-08-18 14:12:25,465 INFO Live micro hold S404 AVGO260821C00412500 -35.5% (tp +50% / sl -50%)
Live micro hold S218 NKE260821C00040000 +35.2% (tp +50% / sl -50%)
2026-08-18 14:12:25,466 INFO Live micro hold S218 NKE260821C00040000 +35.2% (tp +50% / sl -50%)
Live micro hold S210 CELH260821C00030000 -27.1% (tp +50% / sl -50%)
2026-08-18 14:12:25,466 INFO Live micro hold S210 CELH260821C00030000 -27.1% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-18 14:12:25,504 INFO Live micro: manage/exits only
Live micro done. open_options=3 lots=3
2026-08-18 14:12:25,513 INFO Live micro done. open_options=3 lots=3
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T181619Z

- UTC timestamp: `20260818T181619Z`
- GitHub run: [#7399](https://github.com/28twagg-ops/TradingBot/actions/runs/32169965984)
- Run id: `32169965984`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260818T181619Z_live_bot.log`, `logs/action_runs/20260818T181619Z_live_options.log`, `logs/action_runs/20260818T181619Z_options_bot.log`

### Live bot (tail)

```text
18:16:20  INFO      Mode: exits
18:16:20  INFO        Daily log -> logs/daily/2026-08-18.md
18:16:20  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (5 ledger rows)
18:16:20  INFO        place_all_stops: checking 3 positions...

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $498.93|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open positions.                                                    |
|                                                                        |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-18T14:16:21.494374-04:00 share=50% ===
2026-08-18 14:16:21,494 INFO === options_live_micro LIVE 2026-08-18T14:16:21.494374-04:00 share=50% ===
Live account equity $496.93 cash $345.93 #225458845 options_level=3
2026-08-18 14:16:21,562 INFO Live account equity $496.93 cash $345.93 #225458845 options_level=3
Live micro hold S404 AVGO260821C00412500 -35.5% (tp +50% / sl -50%)
2026-08-18 14:16:21,589 INFO Live micro hold S404 AVGO260821C00412500 -35.5% (tp +50% / sl -50%)
Live micro hold S218 NKE260821C00040000 +46.3% (tp +50% / sl -50%)
2026-08-18 14:16:21,589 INFO Live micro hold S218 NKE260821C00040000 +46.3% (tp +50% / sl -50%)
Live micro hold S210 CELH260821C00030000 -25.7% (tp +50% / sl -50%)
2026-08-18 14:16:21,589 INFO Live micro hold S210 CELH260821C00030000 -25.7% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-18 14:16:21,638 INFO Live micro: manage/exits only
Live micro done. open_options=3 lots=3
2026-08-18 14:16:21,650 INFO Live micro done. open_options=3 lots=3
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T182056Z

- UTC timestamp: `20260818T182056Z`
- GitHub run: [#7400](https://github.com/28twagg-ops/TradingBot/actions/runs/32170421503)
- Run id: `32170421503`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260818T182056Z_live_bot.log`, `logs/action_runs/20260818T182056Z_live_options.log`, `logs/action_runs/20260818T182056Z_options_bot.log`

### Live bot (tail)

```text
18:20:56  INFO      Mode: exits
18:20:57  INFO        Daily log -> logs/daily/2026-08-18.md
18:20:57  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (5 ledger rows)
18:20:57  INFO        place_all_stops: checking 3 positions...

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $497.93|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open positions.                                                    |
|                                                                        |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-18T14:20:58.180042-04:00 share=50% ===
2026-08-18 14:20:58,180 INFO === options_live_micro LIVE 2026-08-18T14:20:58.180042-04:00 share=50% ===
Live account equity $497.93 cash $345.93 #225458845 options_level=3
2026-08-18 14:20:58,226 INFO Live account equity $497.93 cash $345.93 #225458845 options_level=3
Live micro hold S404 AVGO260821C00412500 -35.5% (tp +50% / sl -50%)
2026-08-18 14:20:58,245 INFO Live micro hold S404 AVGO260821C00412500 -35.5% (tp +50% / sl -50%)
Live micro hold S218 NKE260821C00040000 +48.1% (tp +50% / sl -50%)
2026-08-18 14:20:58,245 INFO Live micro hold S218 NKE260821C00040000 +48.1% (tp +50% / sl -50%)
Live micro hold S210 CELH260821C00030000 -25.7% (tp +50% / sl -50%)
2026-08-18 14:20:58,246 INFO Live micro hold S210 CELH260821C00030000 -25.7% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-18 14:20:58,281 INFO Live micro: manage/exits only
Live micro done. open_options=3 lots=3
2026-08-18 14:20:58,290 INFO Live micro done. open_options=3 lots=3
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T182603Z

- UTC timestamp: `20260818T182603Z`
- GitHub run: [#7401](https://github.com/28twagg-ops/TradingBot/actions/runs/32170880651)
- Run id: `32170880651`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260818T182603Z_live_bot.log`, `logs/action_runs/20260818T182603Z_live_options.log`, `logs/action_runs/20260818T182603Z_options_bot.log`

### Live bot (tail)

```text
18:26:04  INFO      Mode: exits
18:26:05  INFO        Daily log -> logs/daily/2026-08-18.md
18:26:05  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (5 ledger rows)
18:26:05  INFO        place_all_stops: checking 3 positions...

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $505.93|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open positions.                                                    |
|                                                                        |
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-18T14:26:06.110158-04:00 share=50% ===
2026-08-18 14:26:06,110 INFO === options_live_micro LIVE 2026-08-18T14:26:06.110158-04:00 share=50% ===
Live account equity $505.93 cash $345.93 #225458845 options_level=3
2026-08-18 14:26:06,348 INFO Live account equity $505.93 cash $345.93 #225458845 options_level=3
Live micro hold S404 AVGO260821C00412500 -35.5% (tp +50% / sl -50%)
2026-08-18 14:26:06,475 INFO Live micro hold S404 AVGO260821C00412500 -35.5% (tp +50% / sl -50%)
LIVE EXIT take_profit (+63.0%) NKE260821C00040000 x1 limit=0.85 id=29c86933-4091-4fe0-8df6-f45c579bc9df
2026-08-18 14:26:07,252 INFO LIVE EXIT take_profit (+63.0%) NKE260821C00040000 x1 limit=0.85 id=29c86933-4091-4fe0-8df6-f45c579bc9df
Live micro hold S210 CELH260821C00030000 -25.7% (tp +50% / sl -50%)
2026-08-18 14:26:07,252 INFO Live micro hold S210 CELH260821C00030000 -25.7% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-18 14:26:07,427 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=2
2026-08-18 14:26:07,485 INFO Live micro done. open_options=2 lots=2
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T184451Z

- UTC timestamp: `20260818T184451Z`
- GitHub run: [#7404](https://github.com/28twagg-ops/TradingBot/actions/runs/32172273093)
- Run id: `32172273093`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260818T184451Z_live_bot.log`, `logs/action_runs/20260818T184451Z_live_options.log`, `logs/action_runs/20260818T184451Z_options_bot.log`

### Live bot (tail)

```text
18:44:52  INFO      Mode: exits
18:44:53  INFO        Daily log -> logs/daily/2026-08-18.md
18:44:53  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (5 ledger rows)
18:44:53  INFO        place_all_stops: checking 2 positions...
18:44:53  INFO        Daily log -> logs/daily/2026-08-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:44 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $509.90|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00412500     $0.31    $0.19    -38.7%   $-12.00   $19.00   |
|  CELH260821C00030000     $0.70    $0.57    -18.6%   $-13.00   $57.00   |
|                                                                        |
|  Options open P&L                                               $-25.00|
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
=== options_live_micro LIVE 2026-08-18T14:44:54.214038-04:00 share=50% ===
2026-08-18 14:44:54,214 INFO === options_live_micro LIVE 2026-08-18T14:44:54.214038-04:00 share=50% ===
Live account equity $509.90 cash $433.90 #225458845 options_level=3
2026-08-18 14:44:54,282 INFO Live account equity $509.90 cash $433.90 #225458845 options_level=3
Live micro hold S404 AVGO260821C00412500 -38.7% (tp +50% / sl -50%)
2026-08-18 14:44:54,319 INFO Live micro hold S404 AVGO260821C00412500 -38.7% (tp +50% / sl -50%)
Live micro hold S210 CELH260821C00030000 -18.6% (tp +50% / sl -50%)
2026-08-18 14:44:54,319 INFO Live micro hold S210 CELH260821C00030000 -18.6% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-18 14:44:54,363 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=2
2026-08-18 14:44:54,378 INFO Live micro done. open_options=2 lots=2
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T184556Z

- UTC timestamp: `20260818T184556Z`
- GitHub run: [#7405](https://github.com/28twagg-ops/TradingBot/actions/runs/32172742218)
- Run id: `32172742218`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260818T184556Z_live_bot.log`, `logs/action_runs/20260818T184556Z_live_options.log`, `logs/action_runs/20260818T184556Z_options_bot.log`

### Live bot (tail)

```text
18:45:57  INFO      Mode: exits
18:45:57  INFO        Daily log -> logs/daily/2026-08-18.md
18:45:57  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (5 ledger rows)
18:45:58  INFO        place_all_stops: checking 2 positions...
18:45:58  INFO        Daily log -> logs/daily/2026-08-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:45 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $509.90|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00412500     $0.31    $0.19    -38.7%   $-12.00   $19.00   |
|  CELH260821C00030000     $0.70    $0.57    -18.6%   $-13.00   $57.00   |
|                                                                        |
|  Options open P&L                                               $-25.00|
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
=== options_live_micro LIVE 2026-08-18T14:45:58.888652-04:00 share=50% ===
2026-08-18 14:45:58,888 INFO === options_live_micro LIVE 2026-08-18T14:45:58.888652-04:00 share=50% ===
Live account equity $509.90 cash $433.90 #225458845 options_level=3
2026-08-18 14:45:58,942 INFO Live account equity $509.90 cash $433.90 #225458845 options_level=3
Live micro hold S404 AVGO260821C00412500 -38.7% (tp +50% / sl -50%)
2026-08-18 14:45:58,961 INFO Live micro hold S404 AVGO260821C00412500 -38.7% (tp +50% / sl -50%)
Live micro hold S210 CELH260821C00030000 -18.6% (tp +50% / sl -50%)
2026-08-18 14:45:58,961 INFO Live micro hold S210 CELH260821C00030000 -18.6% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-18 14:45:58,985 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=2
2026-08-18 14:45:58,994 INFO Live micro done. open_options=2 lots=2
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T185101Z

- UTC timestamp: `20260818T185101Z`
- GitHub run: [#7406](https://github.com/28twagg-ops/TradingBot/actions/runs/32173206116)
- Run id: `32173206116`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260818T185101Z_live_bot.log`, `logs/action_runs/20260818T185101Z_live_options.log`, `logs/action_runs/20260818T185101Z_options_bot.log`

### Live bot (tail)

```text
18:51:02  INFO      Mode: exits
18:51:03  INFO        Daily log -> logs/daily/2026-08-18.md
18:51:03  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (5 ledger rows)
18:51:03  INFO        place_all_stops: checking 2 positions...
18:51:03  INFO        Daily log -> logs/daily/2026-08-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:51 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $509.90|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00412500     $0.31    $0.19    -38.7%   $-12.00   $19.00   |
|  CELH260821C00030000     $0.70    $0.57    -18.6%   $-13.00   $57.00   |
|                                                                        |
|  Options open P&L                                               $-25.00|
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
=== options_live_micro LIVE 2026-08-18T14:51:04.265110-04:00 share=50% ===
2026-08-18 14:51:04,265 INFO === options_live_micro LIVE 2026-08-18T14:51:04.265110-04:00 share=50% ===
Live account equity $509.90 cash $433.90 #225458845 options_level=3
2026-08-18 14:51:04,635 INFO Live account equity $509.90 cash $433.90 #225458845 options_level=3
Live micro hold S404 AVGO260821C00412500 -38.7% (tp +50% / sl -50%)
2026-08-18 14:51:04,709 INFO Live micro hold S404 AVGO260821C00412500 -38.7% (tp +50% / sl -50%)
Live micro hold S210 CELH260821C00030000 -18.6% (tp +50% / sl -50%)
2026-08-18 14:51:04,709 INFO Live micro hold S210 CELH260821C00030000 -18.6% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-18 14:51:04,825 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=2
2026-08-18 14:51:04,862 INFO Live micro done. open_options=2 lots=2
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T185605Z

- UTC timestamp: `20260818T185605Z`
- GitHub run: [#7407](https://github.com/28twagg-ops/TradingBot/actions/runs/32173673363)
- Run id: `32173673363`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260818T185605Z_live_bot.log`, `logs/action_runs/20260818T185605Z_live_options.log`, `logs/action_runs/20260818T185605Z_options_bot.log`

### Live bot (tail)

```text
18:56:05  INFO      Mode: exits
18:56:06  INFO        Daily log -> logs/daily/2026-08-18.md
18:56:06  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (5 ledger rows)
18:56:06  INFO        place_all_stops: checking 2 positions...
18:56:06  INFO        Daily log -> logs/daily/2026-08-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:56 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $509.90|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00412500     $0.31    $0.19    -38.7%   $-12.00   $19.00   |
|  CELH260821C00030000     $0.70    $0.57    -18.6%   $-13.00   $57.00   |
|                                                                        |
|  Options open P&L                                               $-25.00|
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
=== options_live_micro LIVE 2026-08-18T14:56:07.579687-04:00 share=50% ===
2026-08-18 14:56:07,579 INFO === options_live_micro LIVE 2026-08-18T14:56:07.579687-04:00 share=50% ===
Live account equity $509.90 cash $433.90 #225458845 options_level=3
2026-08-18 14:56:07,755 INFO Live account equity $509.90 cash $433.90 #225458845 options_level=3
Live micro hold S404 AVGO260821C00412500 -38.7% (tp +50% / sl -50%)
2026-08-18 14:56:07,835 INFO Live micro hold S404 AVGO260821C00412500 -38.7% (tp +50% / sl -50%)
Live micro hold S210 CELH260821C00030000 -18.6% (tp +50% / sl -50%)
2026-08-18 14:56:07,835 INFO Live micro hold S210 CELH260821C00030000 -18.6% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-18 14:56:07,980 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=2
2026-08-18 14:56:08,035 INFO Live micro done. open_options=2 lots=2
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T191555Z

- UTC timestamp: `20260818T191555Z`
- GitHub run: [#7411](https://github.com/28twagg-ops/TradingBot/actions/runs/32175552016)
- Run id: `32175552016`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260818T191555Z_live_bot.log`, `logs/action_runs/20260818T191555Z_live_options.log`, `logs/action_runs/20260818T191555Z_options_bot.log`

### Live bot (tail)

```text
19:15:56  INFO      Mode: exits
19:15:56  INFO        Daily log -> logs/daily/2026-08-18.md
19:15:56  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (5 ledger rows)
19:15:56  INFO        place_all_stops: checking 2 positions...
19:15:56  INFO        Daily log -> logs/daily/2026-08-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         19:15 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $514.90|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00412500     $0.31    $0.19    -38.7%   $-12.00   $19.00   |
|  CELH260821C00030000     $0.70    $0.62    -11.4%   $-8.00    $62.00   |
|                                                                        |
|  Options open P&L                                               $-20.00|
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
=== options_live_micro LIVE 2026-08-18T15:15:57.316294-04:00 share=50% ===
2026-08-18 15:15:57,316 INFO === options_live_micro LIVE 2026-08-18T15:15:57.316294-04:00 share=50% ===
Live account equity $514.90 cash $433.90 #225458845 options_level=3
2026-08-18 15:15:57,376 INFO Live account equity $514.90 cash $433.90 #225458845 options_level=3
Live micro hold S404 AVGO260821C00412500 -38.7% (tp +50% / sl -50%)
2026-08-18 15:15:57,402 INFO Live micro hold S404 AVGO260821C00412500 -38.7% (tp +50% / sl -50%)
Live micro hold S210 CELH260821C00030000 -11.4% (tp +50% / sl -50%)
2026-08-18 15:15:57,402 INFO Live micro hold S210 CELH260821C00030000 -11.4% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-18 15:15:57,438 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=2
2026-08-18 15:15:57,451 INFO Live micro done. open_options=2 lots=2
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T192058Z

- UTC timestamp: `20260818T192058Z`
- GitHub run: [#7412](https://github.com/28twagg-ops/TradingBot/actions/runs/32176006813)
- Run id: `32176006813`
- Live bot: exit=`0`, duration=`4s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260818T192058Z_live_bot.log`, `logs/action_runs/20260818T192058Z_live_options.log`, `logs/action_runs/20260818T192058Z_options_bot.log`

### Live bot (tail)

```text
19:21:01  INFO      Mode: exits
19:21:02  INFO        Daily log -> logs/daily/2026-08-18.md
19:21:02  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (5 ledger rows)
19:21:02  INFO        place_all_stops: checking 2 positions...
19:21:02  INFO        Daily log -> logs/daily/2026-08-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         19:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $514.90|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00412500     $0.31    $0.19    -38.7%   $-12.00   $19.00   |
|  CELH260821C00030000     $0.70    $0.62    -11.4%   $-8.00    $62.00   |
|                                                                        |
|  Options open P&L                                               $-20.00|
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
=== options_live_micro LIVE 2026-08-18T15:21:03.494519-04:00 share=50% ===
2026-08-18 15:21:03,494 INFO === options_live_micro LIVE 2026-08-18T15:21:03.494519-04:00 share=50% ===
Live account equity $514.90 cash $433.90 #225458845 options_level=3
2026-08-18 15:21:03,727 INFO Live account equity $514.90 cash $433.90 #225458845 options_level=3
Live micro hold S404 AVGO260821C00412500 -38.7% (tp +50% / sl -50%)
2026-08-18 15:21:03,885 INFO Live micro hold S404 AVGO260821C00412500 -38.7% (tp +50% / sl -50%)
Live micro hold S210 CELH260821C00030000 -11.4% (tp +50% / sl -50%)
2026-08-18 15:21:03,885 INFO Live micro hold S210 CELH260821C00030000 -11.4% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-18 15:21:04,167 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=2
2026-08-18 15:21:04,267 INFO Live micro done. open_options=2 lots=2
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T192613Z

- UTC timestamp: `20260818T192613Z`
- GitHub run: [#7413](https://github.com/28twagg-ops/TradingBot/actions/runs/32176468349)
- Run id: `32176468349`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260818T192613Z_live_bot.log`, `logs/action_runs/20260818T192613Z_live_options.log`, `logs/action_runs/20260818T192613Z_options_bot.log`

### Live bot (tail)

```text
19:26:15  INFO      Mode: exits
19:26:15  INFO        Daily log -> logs/daily/2026-08-18.md
19:26:15  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (5 ledger rows)
19:26:15  INFO        place_all_stops: checking 2 positions...
19:26:15  INFO        Daily log -> logs/daily/2026-08-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         19:26 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $511.90|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open stock positions.                                              |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           0|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|            OPTIONS SLEEVE  (managed by options_live_micro)             |
+========================================================================+
|  CONTRACT                ENTRY    NOW      P&L%     P&L$      MV       |
+------------------------------------------------------------------------+
|  AVGO260821C00412500     $0.31    $0.19    -38.7%   $-12.00   $19.00   |
|  CELH260821C00030000     $0.70    $0.59    -15.7%   $-11.00   $59.00   |
|                                                                        |
|  Options open P&L                                               $-23.00|
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
=== options_live_micro LIVE 2026-08-18T15:26:16.540689-04:00 share=50% ===
2026-08-18 15:26:16,540 INFO === options_live_micro LIVE 2026-08-18T15:26:16.540689-04:00 share=50% ===
Live account equity $511.90 cash $433.90 #225458845 options_level=3
2026-08-18 15:26:16,594 INFO Live account equity $511.90 cash $433.90 #225458845 options_level=3
Live micro hold S404 AVGO260821C00412500 -38.7% (tp +50% / sl -50%)
2026-08-18 15:26:16,660 INFO Live micro hold S404 AVGO260821C00412500 -38.7% (tp +50% / sl -50%)
Live micro hold S210 CELH260821C00030000 -15.7% (tp +50% / sl -50%)
2026-08-18 15:26:16,660 INFO Live micro hold S210 CELH260821C00030000 -15.7% (tp +50% / sl -50%)
Live micro: manage/exits only
2026-08-18 15:26:16,863 INFO Live micro: manage/exits only
Live micro done. open_options=2 lots=2
2026-08-18 15:26:16,914 INFO Live micro done. open_options=2 lots=2
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T193059Z

- UTC timestamp: `20260818T193059Z`
- GitHub run: [#7414](https://github.com/28twagg-ops/TradingBot/actions/runs/32176937956)
- Run id: `32176937956`
- Live bot: exit=`0`, duration=`217s`
- Live options: exit=`0`, duration=`3s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260818T193059Z_live_bot.log`, `logs/action_runs/20260818T193059Z_live_options.log`, `logs/action_runs/20260818T193059Z_options_bot.log`

### Live bot (tail)

```text
19:31:00  INFO      Mode: evening_prep
19:31:01  INFO        Universe cache hit: 903 tickers (tickers_2026-08-18.json)
19:31:02  INFO        [prep_universe] 40/903 (40 valid)
19:31:04  INFO        [prep_universe] 80/903 (80 valid)
19:31:06  INFO        [prep_universe] 120/903 (120 valid)
19:31:07  INFO        [prep_universe] 160/903 (160 valid)
19:31:09  INFO        [prep_universe] 200/903 (199 valid)
19:31:14  INFO        [prep_universe] 240/903 (238 valid)
19:31:28  INFO        [prep_universe] 280/903 (278 valid)
19:31:38  INFO        [prep_universe] 320/903 (318 valid)
19:31:52  INFO        [prep_universe] 360/903 (358 valid)
19:32:02  INFO        [prep_universe] 400/903 (397 valid)
19:32:16  INFO        [prep_universe] 440/903 (437 valid)
19:32:27  INFO        [prep_universe] 480/903 (477 valid)
19:32:40  INFO        [prep_universe] 520/903 (517 valid)
19:32:50  INFO        [prep_universe] 560/903 (557 valid)
19:33:03  INFO        [prep_universe] 600/903 (597 valid)
19:33:14  INFO        [prep_universe] 640/903 (637 valid)
19:33:28  INFO        [prep_universe] 680/903 (677 valid)
19:33:38  INFO        [prep_universe] 720/903 (717 valid)
19:33:52  INFO        [prep_universe] 760/903 (757 valid)
19:34:02  INFO        [prep_universe] 800/903 (797 valid)
19:34:16  INFO        [prep_universe] 840/903 (836 valid)
19:34:27  INFO        [prep_universe] 880/903 (876 valid)
19:34:34  INFO        [prep_universe] 903/903 (899 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      EVENING_PREP|
|  Time                                                         19:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $511.90|
+========================================================================+

+========================================================================+
|                              EVENING PREP                              |
+========================================================================+
|  Goal                   Precompute exits/signals for next execution run|
|  Plan file                                 logs/plans/evening_plan.json|
|  Regime                                                            BULL|
+========================================================================+

+========================================================================+
|                       OPEN POSITION P&L SNAPSHOT                       |
+========================================================================+
|  Open positions                                                       0|
|  Invested                                                         $0.00|
|  Open P&L                                                        $+0.00|
|                                                                        |
|  No open positions.                                                    |
|                                                                        |
+========================================================================+

+========================================================================+
|                            OPEN SELL ORDERS                            |
+========================================================================+
|  Count                                                                2|
|  TICKER    TYPE              QTY       LIMIT       STOP                |
+------------------------------------------------------------------------+
|  CELH260~  OrderType.STOP_~  1         0.32        0.35                |
|  AVGO260~  OrderType.STOP_~  1         0.15        0.16                |
+========================================================================+

+========================================================================+
|                              PREP SUMMARY                              |
+========================================================================+
|  Saved                                                              yes|
|  Exit candidates                                                      0|
|  Signal candidates                                                   26|
|  Universe scanned                                                   903|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-18T15:34:37.235747-04:00 share=50% ===
2026-08-18 15:34:37,235 INFO === options_live_micro LIVE 2026-08-18T15:34:37.235747-04:00 share=50% ===
Live account equity $514.90 cash $433.90 #225458845 options_level=3
2026-08-18 15:34:37,427 INFO Live account equity $514.90 cash $433.90 #225458845 options_level=3
LIVE EXIT EOD AVGO260821C00412500 x1 limit=0.20 id=5ac7a42f-895b-46c5-8f8e-787813906c13
2026-08-18 15:34:38,605 INFO LIVE EXIT EOD AVGO260821C00412500 x1 limit=0.20 id=5ac7a42f-895b-46c5-8f8e-787813906c13
LIVE EXIT EOD CELH260821C00030000 x1 limit=0.63 id=bc9c0fa0-420c-4f89-8125-b82e118eff47
2026-08-18 15:34:38,884 INFO LIVE EXIT EOD CELH260821C00030000 x1 limit=0.63 id=bc9c0fa0-420c-4f89-8125-b82e118eff47
Live micro: manage/exits only
2026-08-18 15:34:38,940 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-08-18 15:34:38,995 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T193601Z

- UTC timestamp: `20260818T193601Z`
- GitHub run: [#7415](https://github.com/28twagg-ops/TradingBot/actions/runs/32177425274)
- Run id: `32177425274`
- Live bot: exit=`0`, duration=`216s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260818T193601Z_live_bot.log`, `logs/action_runs/20260818T193601Z_live_options.log`, `logs/action_runs/20260818T193601Z_options_bot.log`

### Live bot (tail)

```text
19:36:02  INFO      Mode: evening_prep
19:36:03  INFO        Universe cache hit: 903 tickers (tickers_2026-08-18.json)
19:36:04  INFO        [prep_universe] 40/903 (40 valid)
19:36:05  INFO        [prep_universe] 80/903 (80 valid)
19:36:07  INFO        [prep_universe] 120/903 (120 valid)
19:36:09  INFO        [prep_universe] 160/903 (160 valid)
19:36:11  INFO        [prep_universe] 200/903 (199 valid)
19:36:16  INFO        [prep_universe] 240/903 (238 valid)
19:36:29  INFO        [prep_universe] 280/903 (278 valid)
19:36:40  INFO        [prep_universe] 320/903 (318 valid)
19:36:54  INFO        [prep_universe] 360/903 (358 valid)
19:37:04  INFO        [prep_universe] 400/903 (397 valid)
19:37:17  INFO        [prep_universe] 440/903 (437 valid)
19:37:28  INFO        [prep_universe] 480/903 (477 valid)
19:37:41  INFO        [prep_universe] 520/903 (517 valid)
19:37:52  INFO        [prep_universe] 560/903 (557 valid)
19:38:05  INFO        [prep_universe] 600/903 (597 valid)
19:38:16  INFO        [prep_universe] 640/903 (637 valid)
19:38:29  INFO        [prep_universe] 680/903 (677 valid)
19:38:40  INFO        [prep_universe] 720/903 (717 valid)
19:38:53  INFO        [prep_universe] 760/903 (757 valid)
19:39:04  INFO        [prep_universe] 800/903 (797 valid)
19:39:17  INFO        [prep_universe] 840/903 (836 valid)
19:39:28  INFO        [prep_universe] 880/903 (876 valid)
19:39:35  INFO        [prep_universe] 903/903 (899 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      EVENING_PREP|
|  Time                                                         19:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $516.82|
+========================================================================+

+========================================================================+
|                              EVENING PREP                              |
+========================================================================+
|  Goal                   Precompute exits/signals for next execution run|
|  Plan file                                 logs/plans/evening_plan.json|
|  Regime                                                            BULL|
+========================================================================+

+========================================================================+
|                       OPEN POSITION P&L SNAPSHOT                       |
+========================================================================+
|  Open positions                                                       0|
|  Invested                                                         $0.00|
|  Open P&L                                                        $+0.00|
|                                                                        |
|  No open positions.                                                    |
|                                                                        |
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
|  Signal candidates                                                   25|
|  Universe scanned                                                   903|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-18T15:39:38.255978-04:00 share=50% ===
2026-08-18 15:39:38,256 INFO === options_live_micro LIVE 2026-08-18T15:39:38.255978-04:00 share=50% ===
Live account equity $516.82 cash $516.82 #225458845 options_level=3
2026-08-18 15:39:38,365 INFO Live account equity $516.82 cash $516.82 #225458845 options_level=3
Live micro: manage/exits only
2026-08-18 15:39:38,456 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-08-18 15:39:38,485 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T194057Z

- UTC timestamp: `20260818T194057Z`
- GitHub run: [#7416](https://github.com/28twagg-ops/TradingBot/actions/runs/32177897897)
- Run id: `32177897897`
- Live bot: exit=`0`, duration=`217s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260818T194057Z_live_bot.log`, `logs/action_runs/20260818T194057Z_live_options.log`, `logs/action_runs/20260818T194057Z_options_bot.log`

### Live bot (tail)

```text
19:40:58  INFO      Mode: evening_prep
19:40:59  INFO        Universe cache hit: 903 tickers (tickers_2026-08-18.json)
19:41:00  INFO        [prep_universe] 40/903 (40 valid)
19:41:02  INFO        [prep_universe] 80/903 (80 valid)
19:41:04  INFO        [prep_universe] 120/903 (120 valid)
19:41:06  INFO        [prep_universe] 160/903 (160 valid)
19:41:08  INFO        [prep_universe] 200/903 (199 valid)
19:41:12  INFO        [prep_universe] 240/903 (238 valid)
19:41:26  INFO        [prep_universe] 280/903 (278 valid)
19:41:37  INFO        [prep_universe] 320/903 (318 valid)
19:41:48  INFO        [prep_universe] 360/903 (358 valid)
19:42:01  INFO        [prep_universe] 400/903 (397 valid)
19:42:12  INFO        [prep_universe] 440/903 (437 valid)
19:42:26  INFO        [prep_universe] 480/903 (477 valid)
19:42:37  INFO        [prep_universe] 520/903 (517 valid)
19:42:50  INFO        [prep_universe] 560/903 (557 valid)
19:43:00  INFO        [prep_universe] 600/903 (597 valid)
19:43:14  INFO        [prep_universe] 640/903 (637 valid)
19:43:25  INFO        [prep_universe] 680/903 (677 valid)
19:43:36  INFO        [prep_universe] 720/903 (717 valid)
19:43:49  INFO        [prep_universe] 760/903 (757 valid)
19:44:00  INFO        [prep_universe] 800/903 (797 valid)
19:44:13  INFO        [prep_universe] 840/903 (836 valid)
19:44:24  INFO        [prep_universe] 880/903 (876 valid)
19:44:31  INFO        [prep_universe] 903/903 (899 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      EVENING_PREP|
|  Time                                                         19:40 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $516.82|
+========================================================================+

+========================================================================+
|                              EVENING PREP                              |
+========================================================================+
|  Goal                   Precompute exits/signals for next execution run|
|  Plan file                                 logs/plans/evening_plan.json|
|  Regime                                                            BULL|
+========================================================================+

+========================================================================+
|                       OPEN POSITION P&L SNAPSHOT                       |
+========================================================================+
|  Open positions                                                       0|
|  Invested                                                         $0.00|
|  Open P&L                                                        $+0.00|
|                                                                        |
|  No open positions.                                                    |
|                                                                        |
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
|  Signal candidates                                                   26|
|  Universe scanned                                                   903|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-18T15:44:35.059180-04:00 share=50% ===
2026-08-18 15:44:35,059 INFO === options_live_micro LIVE 2026-08-18T15:44:35.059180-04:00 share=50% ===
Live account equity $516.82 cash $516.82 #225458845 options_level=3
2026-08-18 15:44:35,301 INFO Live account equity $516.82 cash $516.82 #225458845 options_level=3
Live micro: manage/exits only
2026-08-18 15:44:35,504 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-08-18 15:44:35,572 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T194555Z

- UTC timestamp: `20260818T194555Z`
- GitHub run: [#7417](https://github.com/28twagg-ops/TradingBot/actions/runs/32178369345)
- Run id: `32178369345`
- Live bot: exit=`0`, duration=`247s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260818T194555Z_live_bot.log`, `logs/action_runs/20260818T194555Z_live_options.log`, `logs/action_runs/20260818T194555Z_options_bot.log`

### Live bot (tail)

```text
... (122 earlier lines - see full log file)
|  UGI      VWAP_Reclaim    eq     $38.51   60.8   4.12    VWAP reclaim V|
|  VNOM     Pullback50      eq     $43.48   51.3   -0.56   50MA bounce (+|
|                                                                        |
+========================================================================+

+========================================================================+
|                              ENTRY ORDERS                              |
+========================================================================+
|    ENTER [eq] MNST  MomReversal                                  $77.52|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    ENTER [eq] AAPL  Pullback50                                   $77.52|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    ENTER [eq] BRK-B  Pullback50                                  $77.52|
|    ENTER [eq] CNC  Pullback50                                    $77.52|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    SKIP [eq] CDW  Pullback50                                      cap 3|
|    SKIP [eq] CHD  Pullback50                                      cap 3|
|    SKIP [eq] C  Pullback50                                        cap 3|
|    SKIP [eq] CL  Pullback50                                       cap 3|
|    SKIP [eq] EIX  Pullback50                                      cap 3|
|    SKIP [eq] HLT  Pullback50                                      cap 3|
|    SKIP [eq] KDP  Pullback50                                      cap 3|
|    SKIP [eq] MS  Pullback50                                       cap 3|
|    SKIP [eq] PM  Pullback50                                       cap 3|
|    SKIP [eq] RCL  Pullback50                                      cap 3|19:50:02  INFO        place_all_stops: checking 3 positions...
19:50:02  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
19:50:02  INFO        STOP-MARKET placed CNC  qty=1 (pos=1.1876)  stop=$64.94  id=d3eeff45-2c0e-4b72-9375-2a519d2cf149
19:50:02  INFO        STOP-MARKET placed MNST  qty=1 (pos=1.6350)  stop=$47.17  id=10fb0685-7929-4fbe-b791-c053c71e4b03
19:50:02  INFO        place_eod_stops: updating 3 stops to current price...
19:50:02  INFO        EOD stop skip AAPL: 0.2496 shares (fractional) — ext_exits will cover
19:50:02  INFO        EOD stop: cancelled old stop CNC
19:50:02  WARNING     EOD stop failed CNC: {"available":"0.187565116","code":40310000,"existing_qty":"1.187565116","held_for_orders":"1","message":"insufficient qty available for order (requested: 1, available: 0.187565116)","symbol":"CNC"}
19:50:02  INFO        EOD stop: cancelled old stop MNST
19:50:02  WARNING     EOD stop failed MNST: {"available":"0.634956125","code":40310000,"existing_qty":"1.634956125","held_for_orders":"1","message":"insufficient qty available for order (requested: 1, available: 0.634956125)","symbol":"MNST"}
19:50:02  INFO        Daily log -> logs/daily/2026-08-18.md
19:50:02  INFO        Dashboard written → logs/dashboard.md

|    SKIP [eq] VTR  Pullback50                                      cap 3|
|    SKIP [eq] BKH  Pullback50                                      cap 3|
|    SKIP [eq] PVH  Pullback50                                      cap 3|
|    SKIP [eq] SLAB  Pullback50                                     cap 3|
|    SKIP [eq] SNX  Pullback50                                      cap 3|
|    SKIP [eq] VNOM  Pullback50                                     cap 3|
|    SKIP [eq] EBAY  RSIRecovery                                    cap 3|
|    SKIP [eq] AZO  VWAP_Reclaim                                    cap 3|
|    SKIP [eq] DT  VWAP_Reclaim                                     cap 3|
|    SKIP [eq] UGI  VWAP_Reclaim                                    cap 3|

+========================================================================+
|                         BUY FILL CONFIRMATION                          |
+========================================================================+
|  Pending submits                                                      3|
+------------------------------------------------------------------------+
|  MNST                                                 still unconfirmed|
|  AAPL                                                 still unconfirmed|
|  CNC                                                  still unconfirmed|
+========================================================================+
+========================================================================+

+========================================================================+
|                           GTC STOP PLACEMENT                           |
+========================================================================+
|  Waiting 5s for 3 buy submit(s) to settle...                           |
+========================================================================+

+========================================================================+
|                            SESSION SUMMARY                             |
+========================================================================+
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Strategy  VolumeSpike + 52wkLow (display only — schedule not enforced)|
|  Scanned                                                            899|
|  Signals                                                             24|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  3 unconfirmed|
|  Exits                                                                0|
|  Open pos                                                             3|
|  Equity                                                         $516.82|
|  Cash                                                           $284.29|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-18T15:50:03.682612-04:00 share=50% ===
2026-08-18 15:50:03,682 INFO === options_live_micro LIVE 2026-08-18T15:50:03.682612-04:00 share=50% ===
Live account equity $516.84 cash $284.29 #225458845 options_level=3
2026-08-18 15:50:03,764 INFO Live account equity $516.84 cash $284.29 #225458845 options_level=3
Live micro: manage/exits only
2026-08-18 15:50:03,817 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-08-18 15:50:03,831 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T195104Z

- UTC timestamp: `20260818T195104Z`
- GitHub run: [#7418](https://github.com/28twagg-ops/TradingBot/actions/runs/32178838077)
- Run id: `32178838077`
- Live bot: exit=`0`, duration=`245s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260818T195104Z_live_bot.log`, `logs/action_runs/20260818T195104Z_live_options.log`, `logs/action_runs/20260818T195104Z_options_bot.log`

### Live bot (tail)

```text
... (97 earlier lines - see full log file)
|  Exit eval    attempted 1 | filled 1 | partial 0 | pending 0 | failed 0|
|  Other skips     already logged today 0  |  no price data 0  |  holds 2|
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
|  Month: Aug  |  Regime: BULL                                           |
|  Primary: VolumeSpike  |  Secondary: 52wkLow (display only — schedule ~|
|  Source                                                       live scan|
+========================================================================+

+========================================================================+
|                         SIGNALS FOUND  --  21                          |
+========================================================================+
|  TICKER   STRATEGY        TIER   PRICE    RSI    VOL_Z   TRIGGER       |
+------------------------------------------------------------------------+
|  AZO      VWAP_Reclaim    eq     $3085.~  44.2   1.43    VWAP reclaim V|
|  BRK-B    Pullback50      eq     $502.98  45.0   -1.98   50MA bounce (+|
|  CDW      Pullback50      eq     $135.59  37.2   -1.03   50MA bounce (-|
|  CNC      Pullback50      eq     $65.39   57.9   -1.22   50MA bounce (+|
|  CHD      Pullback50      eq     $99.25   48.0   -1.72   50MA bounce (+|
|  C        Pullback50      eq     $137.75  74.8   -1.85   50MA bounce (+|
|  CL       Pullback50      eq     $91.49   42.4   -1.07   50MA bounce (-|
|  EIX      Pullback50      eq     $73.29   36.9   -0.82   50MA bounce (-|
|  EBAY     RSIRecovery     eq     $102.73  31.2   0.58    RSI 25.5→31.2 |
|  HLT      Pullback50      eq     $327.90  55.3   -1.38   50MA bounce (-|
|  HUM      Pullback50      eq     $384.17  60.2   -1.15   50MA bounce (+|
|  KDP      Pullback50      eq     $30.95   46.5   -1.96   50MA bounce (-|
|  MS       Pullback50      eq     $217.29  73.9   -1.74   50MA bounce (+|
|  PM       RSIRecovery     eq     $187.63  33.6   0.31    RSI 25.2→33.6 |
|  RCL      Pullback50      eq     $300.38  25.3   -1.12   50MA bounce (-|
|  VTR      Pullback50      eq     $91.50   37.4   -1.58   50MA bounce (+|
|  BKH      Pullback50      eq     $73.16   51.1   -0.79   50MA bounce (-|
|  DT       VWAP_Reclaim    eq     $49.25   65.2   2.51    VWAP reclaim V|
|  SLAB     Pullback50      eq     $218.97  70.0   -1.83   50MA bounce (+|
|  UGI      VWAP_Reclaim    eq     $38.59   61.1   4.12    VWAP reclaim V|
|  VNOM     Pullback50      eq     $43.54   51.6   -0.47   50MA bounce (+|
|                                                                        |
+========================================================================+

+========================================================================+
|                              ENTRY ORDERS                              |19:55:09  INFO        place_all_stops: checking 2 positions...
19:55:09  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
19:55:09  INFO        STOP-MARKET placed MNST  qty=1 (pos=1.6350)  stop=$47.17  id=71e2cd59-a36f-4a65-bd40-bf3f3a434a03
19:55:09  INFO        place_eod_stops: updating 2 stops to current price...
19:55:09  INFO        EOD stop skip AAPL: 0.2496 shares (fractional) — ext_exits will cover
19:55:09  INFO        EOD stop: cancelled old stop MNST
19:55:09  WARNING     EOD stop failed MNST: {"available":"0.634956125","code":40310000,"existing_qty":"1.634956125","held_for_orders":"1","message":"insufficient qty available for order (requested: 1, available: 0.634956125)","symbol":"MNST"}
19:55:09  INFO        Daily log -> logs/daily/2026-08-18.md
19:55:09  INFO        Dashboard written → logs/dashboard.md

+========================================================================+
|  Skipped                                  no entry slots (max_trades=0)|
+========================================================================+

+========================================================================+
|                            SESSION SUMMARY                             |
+========================================================================+
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Strategy  VolumeSpike + 52wkLow (display only — schedule not enforced)|
|  Scanned                                                            897|
|  Signals                                                             21|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  0 unconfirmed|
|  Exits                                                                1|
|  Open pos                                                             2|
|  Equity                                                         $517.00|
|  Cash                                                           $361.93|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-18T15:55:10.110171-04:00 share=50% ===
2026-08-18 15:55:10,110 INFO === options_live_micro LIVE 2026-08-18T15:55:10.110171-04:00 share=50% ===
Live account equity $517.01 cash $361.93 #225458845 options_level=3
2026-08-18 15:55:10,153 INFO Live account equity $517.01 cash $361.93 #225458845 options_level=3
Live micro: manage/exits only
2026-08-18 15:55:10,180 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-08-18 15:55:10,189 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T195614Z

- UTC timestamp: `20260818T195614Z`
- GitHub run: [#7419](https://github.com/28twagg-ops/TradingBot/actions/runs/32179306744)
- Run id: `32179306744`
- Live bot: exit=`0`, duration=`234s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260818T195614Z_live_bot.log`, `logs/action_runs/20260818T195614Z_live_options.log`, `logs/action_runs/20260818T195614Z_options_bot.log`

### Live bot (tail)

```text
... (124 earlier lines - see full log file)
|  C        Pullback50      eq     $137.72  74.7   -1.80   50MA bounce (+|
|  CL       Pullback50      eq     $91.47   42.3   -0.97   50MA bounce (-|
|  EIX      Pullback50      eq     $73.59   37.8   -0.76   50MA bounce (-|
|  EBAY     RSIRecovery     eq     $102.49  30.7   0.65    RSI 25.5→30.7 |
|  HLT      Pullback50      eq     $328.01  55.3   -1.32   50MA bounce (-|
|  KDP      Pullback50      eq     $30.89   46.0   -1.82   50MA bounce (-|
|  MS       Pullback50      eq     $217.36  74.1   -1.70   50MA bounce (+|
|  PM       RSIRecovery     eq     $188.21  34.7   0.40    RSI 25.2→34.7 |
|  ROST     Pullback50      eq     $236.34  25.4   0.78    50MA bounce (+|
|  RCL      Pullback50      eq     $300.61  25.4   -1.08   50MA bounce (-|
|  BC       Pullback50      eq     $81.40   53.0   -0.36   50MA bounce (+|
|  BKH      Pullback50      eq     $73.21   51.4   -0.64   50MA bounce (-|
|  DT       VWAP_Reclaim    eq     $49.28   65.3   2.57    VWAP reclaim V|
|  SNX      Pullback50      eq     $259.94  62.0   0.07    50MA bounce (+|
|  UGI      VWAP_Reclaim    eq     $38.55   61.0   4.13    VWAP reclaim V|
|                                                                        |
+========================================================================+

+========================================================================+
|                              ENTRY ORDERS                              |
+========================================================================+
|    ENTER [eq] BRK-B  Pullback50                                  $77.53|
|    ENTER [eq] CDW  Pullback50                                    $77.53|19:59:53  INFO        BUY  CDW  $77.53  [Pullback50]  id=2bae2e71-d79f-47a5-b9dc-d09f2f3540ef
20:00:07  INFO        place_all_stops: checking 3 positions...
20:00:07  INFO        STOP skipped AAPL: fractional (0.2496 shares) — software exit will handle it
20:00:07  INFO        STOP skipped CDW: fractional (0.5749 shares) — software exit will handle it
20:00:07  INFO        STOP-MARKET placed MNST  qty=1 (pos=1.6350)  stop=$47.17  id=9d9d7ab1-8ed6-43a6-8340-c36673b2e814
20:00:08  INFO        Daily log -> logs/daily/2026-08-18.md
20:00:08  INFO        Dashboard written → logs/dashboard.md

|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    SKIP [eq] CNC  Pullback50                                      cap 3|
|    SKIP [eq] CHD  Pullback50                                      cap 3|
|    SKIP [eq] C  Pullback50                                        cap 3|
|    SKIP [eq] CL  Pullback50                                       cap 3|
|    SKIP [eq] EIX  Pullback50                                      cap 3|
|    SKIP [eq] HLT  Pullback50                                      cap 3|
|    SKIP [eq] KDP  Pullback50                                      cap 3|
|    SKIP [eq] MS  Pullback50                                       cap 3|
|    SKIP [eq] ROST  Pullback50                                     cap 3|
|    SKIP [eq] RCL  Pullback50                                      cap 3|
|    SKIP [eq] BC  Pullback50                                       cap 3|
|    SKIP [eq] BKH  Pullback50                                      cap 3|
|    SKIP [eq] SNX  Pullback50                                      cap 3|
|    SKIP [eq] EBAY  RSIRecovery                                    cap 3|
|    SKIP [eq] PM  RSIRecovery                                      cap 3|
|    SKIP [eq] AZO  VWAP_Reclaim                                    cap 3|
|    SKIP [eq] DT  VWAP_Reclaim                                     cap 3|
|    SKIP [eq] UGI  VWAP_Reclaim                                    cap 3|

+========================================================================+
|                         BUY FILL CONFIRMATION                          |
+========================================================================+
|  Pending submits                                                      1|
+------------------------------------------------------------------------+
|  CDW                                                  still unconfirmed|
+========================================================================+
+========================================================================+

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
|  Strategy  VolumeSpike + 52wkLow (display only — schedule not enforced)|
|  Scanned                                                            897|
|  Signals                                                             20|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  1 unconfirmed|
|  Exits                                                                0|
|  Open pos                                                             3|
|  Equity                                                         $516.88|
|  Cash                                                           $284.41|
+========================================================================+
```

### Live options micro (tail)

```text
=== options_live_micro LIVE 2026-08-18T16:00:08.880990-04:00 share=50% ===
2026-08-18 16:00:08,881 INFO === options_live_micro LIVE 2026-08-18T16:00:08.880990-04:00 share=50% ===
Live account equity $516.88 cash $284.41 #225458845 options_level=3
2026-08-18 16:00:09,298 INFO Live account equity $516.88 cash $284.41 #225458845 options_level=3
Live micro: manage/exits only
2026-08-18 16:00:09,513 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-08-18 16:00:09,582 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T200123Z

- UTC timestamp: `20260818T200123Z`
- GitHub run: [#7420](https://github.com/28twagg-ops/TradingBot/actions/runs/32179778760)
- Run id: `32179778760`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260818T200123Z_live_bot.log`, `logs/action_runs/20260818T200123Z_live_options.log`, `logs/action_runs/20260818T200123Z_options_bot.log`

### Live bot (tail)

```text
20:01:25  INFO      Mode: ext_exits
20:01:26  INFO        Daily log -> logs/daily/2026-08-18.md
20:01:26  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (6 ledger rows)
20:01:26  INFO        Daily log -> logs/daily/2026-08-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         20:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $516.87|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  AAPL  P&L -0.1%  $-0.11         HOLDING until 9:35am scan (Pullback50)|
|  MNST  P&L -0.1%  $-0.05        HOLDING until 9:35am scan (MomReversal)|
|  CDW  P&L +0.1%  $+0.08          HOLDING until 9:35am scan (Pullback50)|
+========================================================================+

+========================================================================+
|                          EXTENDED HOURS SELLS                          |
+========================================================================+
|                                                                        |
|  No extended-hours sells this run.                                     |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                         ext_exits|
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
=== options_live_micro LIVE 2026-08-18T16:01:27.020282-04:00 share=50% ===
2026-08-18 16:01:27,020 INFO === options_live_micro LIVE 2026-08-18T16:01:27.020282-04:00 share=50% ===
Live account equity $516.87 cash $284.41 #225458845 options_level=3
2026-08-18 16:01:27,169 INFO Live account equity $516.87 cash $284.41 #225458845 options_level=3
Live micro: manage/exits only
2026-08-18 16:01:27,280 INFO Live micro: manage/exits only
Live micro done. open_options=0 lots=0
2026-08-18 16:01:27,317 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T201209Z

- UTC timestamp: `20260818T201209Z`
- GitHub run: [#7422](https://github.com/28twagg-ops/TradingBot/actions/runs/32180737334)
- Run id: `32180737334`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260818T201209Z_live_bot.log`, `logs/action_runs/20260818T201209Z_live_options.log`, `logs/action_runs/20260818T201209Z_options_bot.log`

### Live bot (tail)

```text
20:12:10  INFO      Mode: ext_exits
20:12:11  INFO        Daily log -> logs/daily/2026-08-18.md
20:12:11  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (6 ledger rows)
20:12:11  INFO        Daily log -> logs/daily/2026-08-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         20:12 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $516.78|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  AAPL  P&L -0.3%  $-0.20         HOLDING until 9:35am scan (Pullback50)|
|  MNST  P&L -0.1%  $-0.05        HOLDING until 9:35am scan (MomReversal)|
|  CDW  P&L +0.1%  $+0.08          HOLDING until 9:35am scan (Pullback50)|
+========================================================================+

+========================================================================+
|                          EXTENDED HOURS SELLS                          |
+========================================================================+
|                                                                        |
|  No extended-hours sells this run.                                     |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                         ext_exits|
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
=== options_live_micro LIVE 2026-08-18T16:12:12.283834-04:00 share=50% ===
2026-08-18 16:12:12,283 INFO === options_live_micro LIVE 2026-08-18T16:12:12.283834-04:00 share=50% ===
Live account equity $516.78 cash $284.41 #225458845 options_level=3
2026-08-18 16:12:12,326 INFO Live account equity $516.78 cash $284.41 #225458845 options_level=3
Live micro done. open_options=0 lots=0
2026-08-18 16:12:12,350 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T201610Z

- UTC timestamp: `20260818T201610Z`
- GitHub run: [#7423](https://github.com/28twagg-ops/TradingBot/actions/runs/32181203538)
- Run id: `32181203538`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260818T201610Z_live_bot.log`, `logs/action_runs/20260818T201610Z_live_options.log`, `logs/action_runs/20260818T201610Z_options_bot.log`

### Live bot (tail)

```text
20:16:12  INFO      Mode: ext_exits
20:16:13  INFO        Daily log -> logs/daily/2026-08-18.md
20:16:13  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (6 ledger rows)
20:16:13  INFO        Daily log -> logs/daily/2026-08-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         20:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $516.79|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  AAPL  P&L -0.2%  $-0.19         HOLDING until 9:35am scan (Pullback50)|
|  MNST  P&L -0.1%  $-0.05        HOLDING until 9:35am scan (MomReversal)|
|  CDW  P&L +0.1%  $+0.08          HOLDING until 9:35am scan (Pullback50)|
+========================================================================+

+========================================================================+
|                          EXTENDED HOURS SELLS                          |
+========================================================================+
|                                                                        |
|  No extended-hours sells this run.                                     |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                         ext_exits|
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
=== options_live_micro LIVE 2026-08-18T16:16:14.265060-04:00 share=50% ===
2026-08-18 16:16:14,265 INFO === options_live_micro LIVE 2026-08-18T16:16:14.265060-04:00 share=50% ===
Live account equity $516.79 cash $284.41 #225458845 options_level=3
2026-08-18 16:16:14,408 INFO Live account equity $516.79 cash $284.41 #225458845 options_level=3
Live micro done. open_options=0 lots=0
2026-08-18 16:16:14,543 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T203155Z

- UTC timestamp: `20260818T203155Z`
- GitHub run: [#7426](https://github.com/28twagg-ops/TradingBot/actions/runs/32182586235)
- Run id: `32182586235`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260818T203155Z_live_bot.log`, `logs/action_runs/20260818T203155Z_live_options.log`, `logs/action_runs/20260818T203155Z_options_bot.log`

### Live bot (tail)

```text
20:31:56  INFO      Mode: ext_exits
20:31:57  INFO        Daily log -> logs/daily/2026-08-18.md
20:31:57  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (6 ledger rows)
20:31:58  INFO        Daily log -> logs/daily/2026-08-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         20:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $516.84|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  AAPL  P&L -0.2%  $-0.15         HOLDING until 9:35am scan (Pullback50)|
|  MNST  P&L -0.1%  $-0.05        HOLDING until 9:35am scan (MomReversal)|
|  CDW  P&L +0.1%  $+0.08          HOLDING until 9:35am scan (Pullback50)|
+========================================================================+

+========================================================================+
|                          EXTENDED HOURS SELLS                          |
+========================================================================+
|                                                                        |
|  No extended-hours sells this run.                                     |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                         ext_exits|
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
=== options_live_micro LIVE 2026-08-18T16:31:59.080360-04:00 share=50% ===
2026-08-18 16:31:59,080 INFO === options_live_micro LIVE 2026-08-18T16:31:59.080360-04:00 share=50% ===
Live account equity $516.84 cash $284.41 #225458845 options_level=3
2026-08-18 16:31:59,300 INFO Live account equity $516.84 cash $284.41 #225458845 options_level=3
Live micro done. open_options=0 lots=0
2026-08-18 16:31:59,476 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T203606Z

- UTC timestamp: `20260818T203606Z`
- GitHub run: [#7427](https://github.com/28twagg-ops/TradingBot/actions/runs/32183052620)
- Run id: `32183052620`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260818T203606Z_live_bot.log`, `logs/action_runs/20260818T203606Z_live_options.log`, `logs/action_runs/20260818T203606Z_options_bot.log`

### Live bot (tail)

```text
20:36:08  INFO      Mode: ext_exits
20:36:08  INFO        Daily log -> logs/daily/2026-08-18.md
20:36:08  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (6 ledger rows)
20:36:09  INFO        Daily log -> logs/daily/2026-08-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         20:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $517.03|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  AAPL  P&L -0.2%  $-0.18         HOLDING until 9:35am scan (Pullback50)|
|  CDW  P&L +0.1%  $+0.08          HOLDING until 9:35am scan (Pullback50)|
|  MNST  P&L +0.2%  $+0.18        HOLDING until 9:35am scan (MomReversal)|
+========================================================================+

+========================================================================+
|                          EXTENDED HOURS SELLS                          |
+========================================================================+
|                                                                        |
|  No extended-hours sells this run.                                     |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                         ext_exits|
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
=== options_live_micro LIVE 2026-08-18T16:36:10.192984-04:00 share=50% ===
2026-08-18 16:36:10,193 INFO === options_live_micro LIVE 2026-08-18T16:36:10.192984-04:00 share=50% ===
Live account equity $517.03 cash $284.41 #225458845 options_level=3
2026-08-18 16:36:10,388 INFO Live account equity $517.03 cash $284.41 #225458845 options_level=3
Live micro done. open_options=0 lots=0
2026-08-18 16:36:10,559 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T204054Z

- UTC timestamp: `20260818T204054Z`
- GitHub run: [#7428](https://github.com/28twagg-ops/TradingBot/actions/runs/32183524385)
- Run id: `32183524385`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260818T204054Z_live_bot.log`, `logs/action_runs/20260818T204054Z_live_options.log`, `logs/action_runs/20260818T204054Z_options_bot.log`

### Live bot (tail)

```text
20:40:55  INFO      Mode: ext_exits
20:40:55  INFO        Daily log -> logs/daily/2026-08-18.md
20:40:55  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (6 ledger rows)
20:40:55  INFO        Daily log -> logs/daily/2026-08-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         20:40 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $516.77|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  AAPL  P&L -0.2%  $-0.16         HOLDING until 9:35am scan (Pullback50)|
|  MNST  P&L -0.1%  $-0.09        HOLDING until 9:35am scan (MomReversal)|
|  CDW  P&L +0.1%  $+0.08          HOLDING until 9:35am scan (Pullback50)|
+========================================================================+

+========================================================================+
|                          EXTENDED HOURS SELLS                          |
+========================================================================+
|                                                                        |
|  No extended-hours sells this run.                                     |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                         ext_exits|
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
=== options_live_micro LIVE 2026-08-18T16:40:56.631775-04:00 share=50% ===
2026-08-18 16:40:56,631 INFO === options_live_micro LIVE 2026-08-18T16:40:56.631775-04:00 share=50% ===
Live account equity $516.77 cash $284.41 #225458845 options_level=3
2026-08-18 16:40:56,725 INFO Live account equity $516.77 cash $284.41 #225458845 options_level=3
Live micro done. open_options=0 lots=0
2026-08-18 16:40:56,804 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T204559Z

- UTC timestamp: `20260818T204559Z`
- GitHub run: [#7429](https://github.com/28twagg-ops/TradingBot/actions/runs/32184004224)
- Run id: `32184004224`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260818T204559Z_live_bot.log`, `logs/action_runs/20260818T204559Z_live_options.log`, `logs/action_runs/20260818T204559Z_options_bot.log`

### Live bot (tail)

```text
20:46:01  INFO      Mode: ext_exits
20:46:01  INFO        Daily log -> logs/daily/2026-08-18.md
20:46:01  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (6 ledger rows)
20:46:01  INFO        Daily log -> logs/daily/2026-08-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         20:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $516.76|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  AAPL  P&L -0.2%  $-0.17         HOLDING until 9:35am scan (Pullback50)|
|  MNST  P&L -0.1%  $-0.09        HOLDING until 9:35am scan (MomReversal)|
|  CDW  P&L +0.1%  $+0.08          HOLDING until 9:35am scan (Pullback50)|
+========================================================================+

+========================================================================+
|                          EXTENDED HOURS SELLS                          |
+========================================================================+
|                                                                        |
|  No extended-hours sells this run.                                     |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                         ext_exits|
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
=== options_live_micro LIVE 2026-08-18T16:46:02.041674-04:00 share=50% ===
2026-08-18 16:46:02,041 INFO === options_live_micro LIVE 2026-08-18T16:46:02.041674-04:00 share=50% ===
Live account equity $516.76 cash $284.41 #225458845 options_level=3
2026-08-18 16:46:02,076 INFO Live account equity $516.76 cash $284.41 #225458845 options_level=3
Live micro done. open_options=0 lots=0
2026-08-18 16:46:02,106 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T205108Z

- UTC timestamp: `20260818T205108Z`
- GitHub run: [#7430](https://github.com/28twagg-ops/TradingBot/actions/runs/32184463060)
- Run id: `32184463060`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260818T205108Z_live_bot.log`, `logs/action_runs/20260818T205108Z_live_options.log`, `logs/action_runs/20260818T205108Z_options_bot.log`

### Live bot (tail)

```text
20:51:09  INFO      Mode: ext_exits
20:51:10  INFO        Daily log -> logs/daily/2026-08-18.md
20:51:10  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (6 ledger rows)
20:51:10  INFO        Daily log -> logs/daily/2026-08-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         20:51 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $516.74|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  AAPL  P&L -0.2%  $-0.19         HOLDING until 9:35am scan (Pullback50)|
|  MNST  P&L -0.1%  $-0.09        HOLDING until 9:35am scan (MomReversal)|
|  CDW  P&L +0.1%  $+0.08          HOLDING until 9:35am scan (Pullback50)|
+========================================================================+

+========================================================================+
|                          EXTENDED HOURS SELLS                          |
+========================================================================+
|                                                                        |
|  No extended-hours sells this run.                                     |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                         ext_exits|
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
=== options_live_micro LIVE 2026-08-18T16:51:11.522503-04:00 share=50% ===
2026-08-18 16:51:11,522 INFO === options_live_micro LIVE 2026-08-18T16:51:11.522503-04:00 share=50% ===
Live account equity $516.74 cash $284.41 #225458845 options_level=3
2026-08-18 16:51:11,743 INFO Live account equity $516.74 cash $284.41 #225458845 options_level=3
Live micro done. open_options=0 lots=0
2026-08-18 16:51:11,950 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T210759Z

- UTC timestamp: `20260818T210759Z`
- GitHub run: [#7433](https://github.com/28twagg-ops/TradingBot/actions/runs/32185835258)
- Run id: `32185835258`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260818T210759Z_live_bot.log`, `logs/action_runs/20260818T210759Z_live_options.log`, `logs/action_runs/20260818T210759Z_options_bot.log`

### Live bot (tail)

```text
21:08:00  INFO      Mode: ext_exits
21:08:00  INFO        Daily log -> logs/daily/2026-08-18.md
21:08:00  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (6 ledger rows)
21:08:01  INFO        Daily log -> logs/daily/2026-08-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         21:08 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $516.71|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  AAPL  P&L -0.3%  $-0.22         HOLDING until 9:35am scan (Pullback50)|
|  MNST  P&L -0.1%  $-0.09        HOLDING until 9:35am scan (MomReversal)|
|  CDW  P&L +0.1%  $+0.08          HOLDING until 9:35am scan (Pullback50)|
+========================================================================+

+========================================================================+
|                          EXTENDED HOURS SELLS                          |
+========================================================================+
|                                                                        |
|  No extended-hours sells this run.                                     |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                         ext_exits|
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
=== options_live_micro LIVE 2026-08-18T17:08:01.911103-04:00 share=50% ===
2026-08-18 17:08:01,911 INFO === options_live_micro LIVE 2026-08-18T17:08:01.911103-04:00 share=50% ===
Live account equity $516.71 cash $284.41 #225458845 options_level=3
2026-08-18 17:08:02,010 INFO Live account equity $516.71 cash $284.41 #225458845 options_level=3
Live micro done. open_options=0 lots=0
2026-08-18 17:08:02,088 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T211124Z

- UTC timestamp: `20260818T211124Z`
- GitHub run: [#7434](https://github.com/28twagg-ops/TradingBot/actions/runs/32186283590)
- Run id: `32186283590`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260818T211124Z_live_bot.log`, `logs/action_runs/20260818T211124Z_live_options.log`, `logs/action_runs/20260818T211124Z_options_bot.log`

### Live bot (tail)

```text
21:11:25  INFO      Mode: ext_exits
21:11:26  INFO        Daily log -> logs/daily/2026-08-18.md
21:11:26  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (6 ledger rows)
21:11:27  INFO        Daily log -> logs/daily/2026-08-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         21:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $516.71|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  AAPL  P&L -0.3%  $-0.22         HOLDING until 9:35am scan (Pullback50)|
|  MNST  P&L -0.1%  $-0.09        HOLDING until 9:35am scan (MomReversal)|
|  CDW  P&L +0.1%  $+0.08          HOLDING until 9:35am scan (Pullback50)|
+========================================================================+

+========================================================================+
|                          EXTENDED HOURS SELLS                          |
+========================================================================+
|                                                                        |
|  No extended-hours sells this run.                                     |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                         ext_exits|
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
=== options_live_micro LIVE 2026-08-18T17:11:27.912119-04:00 share=50% ===
2026-08-18 17:11:27,912 INFO === options_live_micro LIVE 2026-08-18T17:11:27.912119-04:00 share=50% ===
Live account equity $516.71 cash $284.41 #225458845 options_level=3
2026-08-18 17:11:28,404 INFO Live account equity $516.71 cash $284.41 #225458845 options_level=3
Live micro done. open_options=0 lots=0
2026-08-18 17:11:28,607 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T211553Z

- UTC timestamp: `20260818T211553Z`
- GitHub run: [#7435](https://github.com/28twagg-ops/TradingBot/actions/runs/32186726058)
- Run id: `32186726058`
- Live bot: exit=`0`, duration=`3s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260818T211553Z_live_bot.log`, `logs/action_runs/20260818T211553Z_live_options.log`, `logs/action_runs/20260818T211553Z_options_bot.log`

### Live bot (tail)

```text
21:15:54  INFO      Mode: ext_exits
21:15:55  INFO        Daily log -> logs/daily/2026-08-18.md
21:15:55  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (6 ledger rows)
21:15:56  INFO        Daily log -> logs/daily/2026-08-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         21:15 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $516.71|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  AAPL  P&L -0.3%  $-0.23         HOLDING until 9:35am scan (Pullback50)|
|  MNST  P&L -0.1%  $-0.09        HOLDING until 9:35am scan (MomReversal)|
|  CDW  P&L +0.1%  $+0.08          HOLDING until 9:35am scan (Pullback50)|
+========================================================================+

+========================================================================+
|                          EXTENDED HOURS SELLS                          |
+========================================================================+
|                                                                        |
|  No extended-hours sells this run.                                     |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                         ext_exits|
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
=== options_live_micro LIVE 2026-08-18T17:15:57.324431-04:00 share=50% ===
2026-08-18 17:15:57,324 INFO === options_live_micro LIVE 2026-08-18T17:15:57.324431-04:00 share=50% ===
Live account equity $516.71 cash $284.41 #225458845 options_level=3
2026-08-18 17:15:57,565 INFO Live account equity $516.71 cash $284.41 #225458845 options_level=3
Live micro done. open_options=0 lots=0
2026-08-18 17:15:57,776 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T212055Z

- UTC timestamp: `20260818T212055Z`
- GitHub run: [#7436](https://github.com/28twagg-ops/TradingBot/actions/runs/32187161784)
- Run id: `32187161784`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260818T212055Z_live_bot.log`, `logs/action_runs/20260818T212055Z_live_options.log`, `logs/action_runs/20260818T212055Z_options_bot.log`

### Live bot (tail)

```text
21:20:55  INFO      Mode: ext_exits
21:20:56  INFO        Daily log -> logs/daily/2026-08-18.md
21:20:56  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (6 ledger rows)
21:20:57  INFO        Daily log -> logs/daily/2026-08-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         21:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $516.72|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  AAPL  P&L -0.3%  $-0.21         HOLDING until 9:35am scan (Pullback50)|
|  MNST  P&L -0.1%  $-0.09        HOLDING until 9:35am scan (MomReversal)|
|  CDW  P&L +0.1%  $+0.08          HOLDING until 9:35am scan (Pullback50)|
+========================================================================+

+========================================================================+
|                          EXTENDED HOURS SELLS                          |
+========================================================================+
|                                                                        |
|  No extended-hours sells this run.                                     |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                         ext_exits|
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
=== options_live_micro LIVE 2026-08-18T17:20:58.235183-04:00 share=50% ===
2026-08-18 17:20:58,235 INFO === options_live_micro LIVE 2026-08-18T17:20:58.235183-04:00 share=50% ===
Live account equity $516.72 cash $284.41 #225458845 options_level=3
2026-08-18 17:20:58,506 INFO Live account equity $516.72 cash $284.41 #225458845 options_level=3
Live micro done. open_options=0 lots=0
2026-08-18 17:20:58,736 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T213154Z

- UTC timestamp: `20260818T213154Z`
- GitHub run: [#7438](https://github.com/28twagg-ops/TradingBot/actions/runs/32188032214)
- Run id: `32188032214`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260818T213154Z_live_bot.log`, `logs/action_runs/20260818T213154Z_live_options.log`, `logs/action_runs/20260818T213154Z_options_bot.log`

### Live bot (tail)

```text
21:31:55  INFO      Mode: ext_exits
21:31:55  INFO        Daily log -> logs/daily/2026-08-18.md
21:31:55  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (6 ledger rows)
21:31:55  INFO        Daily log -> logs/daily/2026-08-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         21:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $516.75|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  AAPL  P&L -0.2%  $-0.19         HOLDING until 9:35am scan (Pullback50)|
|  MNST  P&L -0.1%  $-0.09        HOLDING until 9:35am scan (MomReversal)|
|  CDW  P&L +0.1%  $+0.08          HOLDING until 9:35am scan (Pullback50)|
+========================================================================+

+========================================================================+
|                          EXTENDED HOURS SELLS                          |
+========================================================================+
|                                                                        |
|  No extended-hours sells this run.                                     |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                         ext_exits|
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
=== options_live_micro LIVE 2026-08-18T17:31:56.329643-04:00 share=50% ===
2026-08-18 17:31:56,329 INFO === options_live_micro LIVE 2026-08-18T17:31:56.329643-04:00 share=50% ===
Live account equity $516.75 cash $284.41 #225458845 options_level=3
2026-08-18 17:31:56,366 INFO Live account equity $516.75 cash $284.41 #225458845 options_level=3
Live micro done. open_options=0 lots=0
2026-08-18 17:31:56,397 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T214145Z

- UTC timestamp: `20260818T214145Z`
- GitHub run: [#7440](https://github.com/28twagg-ops/TradingBot/actions/runs/32188901318)
- Run id: `32188901318`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260818T214145Z_live_bot.log`, `logs/action_runs/20260818T214145Z_live_options.log`, `logs/action_runs/20260818T214145Z_options_bot.log`

### Live bot (tail)

```text
21:41:46  INFO      Mode: ext_exits
21:41:46  INFO        Daily log -> logs/daily/2026-08-18.md
21:41:46  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (6 ledger rows)
21:41:46  INFO        Daily log -> logs/daily/2026-08-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         21:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $516.77|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  AAPL  P&L -0.2%  $-0.17         HOLDING until 9:35am scan (Pullback50)|
|  MNST  P&L -0.1%  $-0.09        HOLDING until 9:35am scan (MomReversal)|
|  CDW  P&L +0.1%  $+0.08          HOLDING until 9:35am scan (Pullback50)|
+========================================================================+

+========================================================================+
|                          EXTENDED HOURS SELLS                          |
+========================================================================+
|                                                                        |
|  No extended-hours sells this run.                                     |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                         ext_exits|
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
=== options_live_micro LIVE 2026-08-18T17:41:47.482639-04:00 share=50% ===
2026-08-18 17:41:47,482 INFO === options_live_micro LIVE 2026-08-18T17:41:47.482639-04:00 share=50% ===
Live account equity $516.77 cash $284.41 #225458845 options_level=3
2026-08-18 17:41:47,531 INFO Live account equity $516.77 cash $284.41 #225458845 options_level=3
Live micro done. open_options=0 lots=0
2026-08-18 17:41:47,558 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T214553Z

- UTC timestamp: `20260818T214553Z`
- GitHub run: [#7441](https://github.com/28twagg-ops/TradingBot/actions/runs/32189331878)
- Run id: `32189331878`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`0s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260818T214553Z_live_bot.log`, `logs/action_runs/20260818T214553Z_live_options.log`, `logs/action_runs/20260818T214553Z_options_bot.log`

### Live bot (tail)

```text
21:45:54  INFO      Mode: ext_exits
21:45:54  INFO        Daily log -> logs/daily/2026-08-18.md
21:45:54  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (6 ledger rows)
21:45:54  INFO        Daily log -> logs/daily/2026-08-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         21:45 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $517.07|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  AAPL  P&L -0.2%  $-0.19         HOLDING until 9:35am scan (Pullback50)|
|  CDW  P&L +0.1%  $+0.08          HOLDING until 9:35am scan (Pullback50)|
|  MNST  P&L +0.3%  $+0.23        HOLDING until 9:35am scan (MomReversal)|
+========================================================================+

+========================================================================+
|                          EXTENDED HOURS SELLS                          |
+========================================================================+
|                                                                        |
|  No extended-hours sells this run.                                     |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                         ext_exits|
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
=== options_live_micro LIVE 2026-08-18T17:45:55.745562-04:00 share=50% ===
2026-08-18 17:45:55,745 INFO === options_live_micro LIVE 2026-08-18T17:45:55.745562-04:00 share=50% ===
Live account equity $517.07 cash $284.41 #225458845 options_level=3
2026-08-18 17:45:55,832 INFO Live account equity $517.07 cash $284.41 #225458845 options_level=3
Live micro done. open_options=0 lots=0
2026-08-18 17:45:55,897 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T215054Z

- UTC timestamp: `20260818T215054Z`
- GitHub run: [#7442](https://github.com/28twagg-ops/TradingBot/actions/runs/32189757694)
- Run id: `32189757694`
- Live bot: exit=`0`, duration=`2s`
- Live options: exit=`0`, duration=`1s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260818T215054Z_live_bot.log`, `logs/action_runs/20260818T215054Z_live_options.log`, `logs/action_runs/20260818T215054Z_options_bot.log`

### Live bot (tail)

```text
21:50:55  INFO      Mode: ext_exits
21:50:56  INFO        Daily log -> logs/daily/2026-08-18.md
21:50:56  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (6 ledger rows)
21:50:56  INFO        Daily log -> logs/daily/2026-08-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         21:50 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $517.08|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  AAPL  P&L -0.2%  $-0.18         HOLDING until 9:35am scan (Pullback50)|
|  CDW  P&L +0.1%  $+0.08          HOLDING until 9:35am scan (Pullback50)|
|  MNST  P&L +0.3%  $+0.23        HOLDING until 9:35am scan (MomReversal)|
+========================================================================+

+========================================================================+
|                          EXTENDED HOURS SELLS                          |
+========================================================================+
|                                                                        |
|  No extended-hours sells this run.                                     |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                         ext_exits|
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
=== options_live_micro LIVE 2026-08-18T17:50:57.335828-04:00 share=50% ===
2026-08-18 17:50:57,335 INFO === options_live_micro LIVE 2026-08-18T17:50:57.335828-04:00 share=50% ===
Live account equity $517.08 cash $284.41 #225458845 options_level=3
2026-08-18 17:50:57,423 INFO Live account equity $517.08 cash $284.41 #225458845 options_level=3
Live micro done. open_options=0 lots=0
2026-08-18 17:50:57,489 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---

## Run 20260818T215559Z

- UTC timestamp: `20260818T215559Z`
- GitHub run: [#7443](https://github.com/28twagg-ops/TradingBot/actions/runs/32190183504)
- Run id: `32190183504`
- Live bot: exit=`0`, duration=`1s`
- Live options: exit=`0`, duration=`2s`
- Paper options: exit=`0`, duration=`0s`
- Full logs: `logs/action_runs/20260818T215559Z_live_bot.log`, `logs/action_runs/20260818T215559Z_live_options.log`, `logs/action_runs/20260818T215559Z_options_bot.log`

### Live bot (tail)

```text
21:56:00  INFO      Mode: ext_exits
21:56:00  INFO        Daily log -> logs/daily/2026-08-18.md
21:56:00  INFO        Daily log reconciled -> logs/daily/2026-08-18.md (6 ledger rows)
21:56:00  INFO        Daily log -> logs/daily/2026-08-18.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         21:56 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $517.08|
+========================================================================+

+========================================================================+
|                           STOCKS EXIT CHECK                            |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  AAPL  P&L -0.2%  $-0.19         HOLDING until 9:35am scan (Pullback50)|
|  CDW  P&L +0.1%  $+0.08          HOLDING until 9:35am scan (Pullback50)|
|  MNST  P&L +0.3%  $+0.23        HOLDING until 9:35am scan (MomReversal)|
+========================================================================+

+========================================================================+
|                          EXTENDED HOURS SELLS                          |
+========================================================================+
|                                                                        |
|  No extended-hours sells this run.                                     |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                         ext_exits|
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
=== options_live_micro LIVE 2026-08-18T17:56:01.368442-04:00 share=50% ===
2026-08-18 17:56:01,368 INFO === options_live_micro LIVE 2026-08-18T17:56:01.368442-04:00 share=50% ===
Live account equity $517.08 cash $284.41 #225458845 options_level=3
2026-08-18 17:56:01,902 INFO Live account equity $517.08 cash $284.41 #225458845 options_level=3
Live micro done. open_options=0 lots=0
2026-08-18 17:56:02,016 INFO Live micro done. open_options=0 lots=0
```

### Paper options bot (tail)

```text
Paper options bot disabled (OPTIONS_PAPER_ENABLED=0)
```

---
