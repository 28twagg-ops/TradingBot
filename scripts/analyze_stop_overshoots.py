"""Agent 1: Stop overshoot forensics from committed logs."""
import csv
import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOGS = ROOT / "logs"
OUT_DIR = LOGS / "analysis"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def parse_look_into():
    items = []
    p = LOGS / "stop_losses_to_look_into.txt"
    if not p.exists():
        return items
    for block in p.read_text(encoding="utf-8").split(
        "------------------------------------------------------------------------"
    ):
        if "Ticker:" not in block:
            continue
        d = {}
        for line in block.splitlines():
            if ":" not in line:
                continue
            k, v = line.split(":", 1)
            d[k.strip().lower().replace(" ", "_")] = v.strip()
        if d.get("ticker"):
            items.append(d)
    return items


def main():
    stops = []
    with open(LOGS / "transactions.csv", newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r.get("action") != "SELL" or "stop_loss" not in r.get("exit_reason", ""):
                continue
            try:
                pnl = float(r.get("pnl_pct", 0))
                amt = float(r.get("dollar_amount", 0) or 0)
                hold = int(r.get("hold_days", 0) or 0)
            except Exception:
                continue
            stops.append(
                {
                    "date": r["date"],
                    "time": (r.get("timestamp") or "")[:19],
                    "ticker": r["ticker"],
                    "strategy": r.get("strategy", ""),
                    "pnl_pct": pnl,
                    "pnl_dollar": float(r.get("pnl_dollar", 0) or 0),
                    "dollars": amt,
                    "hold_days": hold,
                    "reason": r.get("exit_reason", ""),
                    "method": r.get("sell_method", ""),
                    "fractional": amt < 25,
                }
            )

    bad = [s for s in stops if s["pnl_pct"] < -0.5]
    bad.sort(key=lambda x: x["pnl_pct"])

    look = parse_look_into()
    pdt_count = sum(1 for x in look if "pdt" in x.get("root_cause", "").lower())

    buckets = {"-0.5_to_-1": 0, "-1_to_-2": 0, "-2_to_-5": 0, "-5_plus": 0}
    for s in bad:
        p = s["pnl_pct"]
        if p >= -1:
            buckets["-0.5_to_-1"] += 1
        elif p >= -2:
            buckets["-1_to_-2"] += 1
        elif p >= -5:
            buckets["-2_to_-5"] += 1
        else:
            buckets["-5_plus"] += 1

    # Extra loss vs -0.5% theoretical cap on position size
    extra_loss = 0.0
    for s in bad:
        overshoot_pct = (-0.5 - s["pnl_pct"]) if s["pnl_pct"] < -0.5 else 0
        extra_loss += overshoot_pct * s["dollars"] / 100.0

    lines = [
        "# Stop Overshoot Forensics",
        f"Generated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}",
        "",
        "## Summary",
        f"- Total stop-loss sells: **{len(stops)}**",
        f"- Worse than -0.5% threshold: **{len(bad)}** ({100*len(bad)/max(len(stops),1):.1f}%)",
        f"- Fractional sells (<$25): **{sum(1 for s in bad if s['fractional'])}** / {len(bad)}",
        f"- Same-day (hold 0d): **{sum(1 for s in bad if s['hold_days']==0)}** / {len(bad)}",
        f"- Look-into file entries: **{len(look)}** (PDT deferred: **{pdt_count}**)",
        f"- Rough extra loss vs -0.5% cap (overshoot × size): **${extra_loss:.2f}**",
        "",
        "## Overshoot severity buckets",
        "",
        "| Bucket | Count |",
        "|--------|------:|",
    ]
    for k, v in buckets.items():
        lines.append(f"| {k}% | {v} |")

    lines += [
        "",
        "## Worst 50 stop exits",
        "",
        "| Date | Ticker | P&L% | Hold | $Size | Sell method |",
        "|------|--------|------|------|-------|-------------|",
    ]
    for s in bad[:50]:
        lines.append(
            f"| {s['date']} | {s['ticker']} | {s['pnl_pct']:+.2f}% | {s['hold_days']}d "
            f"| ${s['dollars']:.2f} | {s['method'][:24]} |"
        )

  # Audit slippage on stop sells
    audit_stops = []
    ap = LOGS / "execution_audit.csv"
    if ap.exists():
        with open(ap, newline="", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                if r.get("action") == "SELL" and "stop" in r.get("exit_reason", "").lower():
                    try:
                        slip = float(r.get("slippage_pct", 0) or 0)
                    except Exception:
                        slip = 0
                    audit_stops.append((r.get("date"), r.get("ticker"), slip, r.get("execution_method", "")))

    if audit_stops:
        lines += ["", "## Execution audit (stop sells)", "", "| Date | Ticker | Slippage% | Method |", "|------|--------|-----------|--------|"]
        for row in sorted(audit_stops, key=lambda x: float(x[2]))[:30]:
            lines.append(f"| {row[0]} | {row[1]} | {row[2]} | {row[3]} |")

    out = OUT_DIR / "stop_overshoot_timelines.md"
    out.write_text("\n".join(lines), encoding="utf-8")

    csv_out = OUT_DIR / "stop_overshoot_worst50.csv"
    with open(csv_out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(bad[0].keys()) if bad else [])
        if bad:
            w.writeheader()
            w.writerows(bad[:50])

    print(f"Wrote {out} and {csv_out}")
    print(f"bad={len(bad)} extra_loss=${extra_loss:.2f} pdt_look={pdt_count}")


if __name__ == "__main__":
    main()
