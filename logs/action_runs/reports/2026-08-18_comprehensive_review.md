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
