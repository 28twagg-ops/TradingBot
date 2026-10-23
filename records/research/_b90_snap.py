import csv
from pathlib import Path
rows=list(csv.DictReader(Path("logs/options_trial/buckets/b90_live_1to1/ledger.csv").open()))
exits=[r for r in rows if r["event"]=="exit"]
recon=[r for r in rows if r["event"]=="reconcile"]
entries=[r for r in rows if r["event"]=="entry"]
print(f"entries={len(entries)} exits={len(exits)} reconciles={len(recon)}")
print("CLEAN EXITS:")
total=0.0
wins=0
for r in exits:
    cost=float(r["cost"] or 0)
    fill=float(r["fill_price"] or 0)
    qty=float(r["qty"] or 1)
    if r.get("pnl_usd"):
        pnl=float(r["pnl_usd"])
    else:
        pnl = fill*100*qty - cost
    if r.get("return_pct"):
        pct=float(r["return_pct"])
    else:
        pct=((fill*100*qty/cost-1)*100 if cost else 0)
    total+=pnl
    wins += 1 if pnl>0 else 0
    print(f"{r['ts'][:10]} {r['strategy_id']} {r['symbol']:5} fill={fill:.2f} cost={cost:.0f} pnl=${pnl:+.0f} pct={pct:+.1f}% reason={r['reason']}")
print(f"n={len(exits)} wins={wins} total_pnl=${total:+.0f}")
print("RECONCILES:")
for r in recon:
    print(f"{r['ts'][:10]} {r['strategy_id']} {r['symbol']:5} reason={r['reason']} detail={(r.get('detail') or '')[:80]}")
