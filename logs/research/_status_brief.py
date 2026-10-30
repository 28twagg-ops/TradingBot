import csv
from pathlib import Path
from collections import Counter, defaultdict

# b90 open state: entries without exit/recon
rows=list(csv.DictReader(Path("logs/options_trial/buckets/b90_live_1to1/ledger.csv").open()))
open_lots=set(); closed=set()
for r in rows:
    lid=r["lot_id"]
    if r["event"]=="entry": open_lots.add(lid)
    if r["event"] in ("exit","reconcile"): closed.add(lid)
still=open_lots-closed
print("b90 currently open lots:", len(still))
for r in rows:
    if r["lot_id"] in still and r["event"]=="entry":
        print(r["ts"][:16], r["strategy_id"], r["symbol"], r["occ"], r["cost"])

# paper day pnl last week from quality daily table already known
# count missing_from_broker by strategy across all buckets? just b90 done

# top improvement signals from strategy selection keep vs live allow
print("\nLive allow set: S404,S406,S218")
# recent exit health
print("\nSep paper daily (from report):")
print("Sep8 +46.7% med win56 | Sep9 -47.5 win23 | Sep10 -50 win14 | Sep11 +66.4 win77 | Sep12-13 weekend | Sep14 morning no new exits yet")
