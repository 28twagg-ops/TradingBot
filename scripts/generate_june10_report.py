"""Generate June 10 stop-loss incident report from committed logs."""
import csv
import re
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOGS = ROOT / "logs"
TARGET = "2026-06-10"
OUT = ROOT / "docs" / "incidents" / "june_10_incident_report.md"


def load_stop_items_for_date(target):
    items = []
    if not (LOGS / "stop_losses_to_look_into.txt").exists():
        return items
    text = (LOGS / "stop_losses_to_look_into.txt").read_text(encoding="utf-8")
    blocks = text.split("------------------------------------------------------------------------")
    for block in blocks:
        if target not in block:
            continue
        d = {}
        for line in block.splitlines():
            if line.startswith("Timestamp:"):
                d["timestamp"] = line.split(":", 1)[1].strip()
            elif line.startswith("Ticker:"):
                d["ticker"] = line.split(":", 1)[1].strip()
            elif line.startswith("Strategy:"):
                d["strategy"] = line.split(":", 1)[1].strip()
            elif line.startswith("P&L at breach:"):
                d["pnl_breach"] = line.split(":", 1)[1].strip()
            elif line.startswith("Root cause:"):
                d["root_cause"] = line.split(":", 1)[1].strip()
        if d.get("ticker"):
            items.append(d)
    return items


def main():
    txs = []
    if (LOGS / "transactions.csv").exists():
        with open(LOGS / "transactions.csv", newline="", encoding="utf-8") as f:
            txs = [r for r in csv.DictReader(f) if r.get("date") == TARGET]

    audit = {}
    if (LOGS / "execution_audit.csv").exists():
        with open(LOGS / "execution_audit.csv", newline="", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                if r.get("date") == TARGET:
                    audit[r["ticker"] + "|" + r["action"]] = r

    stops = load_stop_items_for_date(TARGET)
    buys_today = {t["ticker"] for t in txs if t["action"] == "BUY"}
    sells_after = [t for t in txs if t["action"] == "SELL"]

    lines = [
        f"# June 10 Incident Report",
        f"Generated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}",
        "",
        "## Summary",
        f"- Stop-loss investigations logged: **{len(stops)}**",
        f"- Buys on {TARGET}: **{len(buys_today)}**",
        f"- Sells on {TARGET}: **{len(sells_after)}**",
        f"- PDT-deferred entries: **{sum(1 for s in stops if 'PDT' in s.get('root_cause', ''))}**",
        "",
        "## Afternoon stop breaches (same-day entries)",
        "",
        "| Time | Ticker | Strategy | Breach P&L | Root cause | Sold same day? |",
        "|------|--------|----------|------------|------------|----------------|",
    ]
    sold_tickers = {t["ticker"] for t in sells_after}
    for s in stops:
        sold = "yes" if s["ticker"] in sold_tickers else "no"
        lines.append(
            f"| {s.get('timestamp', '')[:16]} | {s['ticker']} | {s.get('strategy', '?')} "
            f"| {s.get('pnl_breach', '?')} | {s.get('root_cause', '?')} | {sold} |"
        )

    lines += [
        "",
        "## Execution audit (June 10)",
        "",
        "| Action | Ticker | Expected | Actual | Slippage% | Method |",
        "|--------|--------|----------|--------|-----------|--------|",
    ]
    for r in sorted(audit.values(), key=lambda x: x.get("timestamp", "")):
        lines.append(
            f"| {r.get('action')} | {r.get('ticker')} | {r.get('expected_price')} "
            f"| {r.get('actual_price')} | {r.get('slippage_pct')} | {r.get('execution_method')} |"
        )

  # EOD open P&L from daily log
    daily = LOGS / "daily" / f"{TARGET}.md"
    if daily.exists():
        m = re.search(r"Open P&L \| \$(.+?) \|", daily.read_text(encoding="utf-8"))
        if m:
            lines += ["", f"## End-of-day open P&L (daily log): **${m.group(1)}**"]

    lines += [
        "",
        "## Diagnosis",
        "- Same-day buys could not exit on stop breach due to strict PDT guard.",
        "- Fractional positions (~$20) skip broker GTC stops; software exit was deferred.",
        "- Morning scan ~22 min after exits (universe fetch bottleneck).",
        "",
        "## Recommended fixes (implemented in pipeline update)",
        "- Prep/execute split with plan cache; parallel fetch; paper-relaxed same-day stop exits.",
    ]

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
