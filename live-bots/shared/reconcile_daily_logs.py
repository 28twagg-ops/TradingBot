"""
Rebuild daily markdown logs from transactions.csv when scan push failed
or an early fallback log was written before trades were recorded.
"""
from __future__ import annotations

import csv
import re
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

SCHEDULE_JUNE = {"p": "GapDown", "s": "VolumeSpike"}  # fallback labels only
CASH_RESERVE_PCT = 0.05
EXIT_STOP = -0.005
EXIT_DAYS_MAX = 3


def _read_csv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def _ledger_for_day(tx_rows: list[dict], day: str) -> list[dict]:
    return [r for r in tx_rows if r.get("date") == day]


def _last_run_for_day(run_rows: list[dict], day: str) -> dict | None:
    hits = [r for r in run_rows if (r.get("timestamp") or "").startswith(day)]
    return hits[-1] if hits else None


def _needs_rebuild(text: str, ledger_count: int) -> bool:
    if "Fallback log" in text:
        return True
    if ledger_count > 0 and "_No trades today._" in text:
        return True
    return False


def _format_trades_table(ledger: list[dict]) -> list[str]:
    if not ledger:
        return ["_No trades today._"]
    lines = [
        "| Time | Action | Ticker | Strategy | Price | Amount | Note |",
        "|------|--------|--------|----------|-------|--------|------|",
    ]
    for t in sorted(ledger, key=lambda r: r.get("timestamp", "")):
        ts = t.get("timestamp", "")
        tm = ts[11:16] if len(ts) >= 16 else "--:--"
        action = (t.get("action") or "").upper()
        try:
            px = float(t.get("price") or 0)
        except (TypeError, ValueError):
            px = 0.0
        try:
            amt = float(t.get("dollar_amount") or 0)
        except (TypeError, ValueError):
            amt = 0.0
        note = t.get("exit_reason", "") if action == "SELL" else "--"
        note = note or "--"
        lines.append(
            f"| {tm} | {action:<4} | {t.get('ticker', '')} | {t.get('strategy', '?')} | "
            f"${px:.2f} | ${amt:.2f} | {note} |"
        )
    return lines


def _extract_section(text: str, header: str, next_header: str | None = None) -> list[str]:
    start = text.find(header)
    if start < 0:
        return []
    start = text.find("\n", start) + 1
    if next_header:
        end = text.find(next_header, start)
        if end < 0:
            end = len(text)
    else:
        end = len(text)
    return text[start:end].strip().splitlines()


def rebuild_day(logs_dir: Path, day: str, dry_run: bool = False) -> bool:
    daily_dir = logs_dir / "daily"
    fname = daily_dir / f"{day}.md"
    tx_rows = _read_csv(logs_dir / "transactions.csv")
    run_rows = _read_csv(logs_dir / "runs.csv")
    ledger = _ledger_for_day(tx_rows, day)

    if not ledger and not fname.exists():
        return False

    existing = fname.read_text(encoding="utf-8") if fname.exists() else ""
    if existing and not _needs_rebuild(existing, len(ledger)):
        return False

    run = _last_run_for_day(run_rows, day)
    equity = float(run.get("equity", 0) or 0) if run else 0.0
    cash = float(run.get("cash", 0) or 0) if run else 0.0
    if ledger:
        try:
            equity = float(ledger[-1].get("equity_after") or equity)
        except (TypeError, ValueError):
            pass

    holdings_lines = _extract_section(existing, "## Holdings", "## Trades today")
    month = int(day[5:7])
    sc = SCHEDULE_JUNE

    lines = [
        f"# Daily Log -- {day}",
        "",
        "> Reconciled from `transactions.csv` "
        f"({datetime.now().strftime('%Y-%m-%d %H:%M UTC')}).",
        "",
        "## Account",
        "| | |",
        "|---|---|",
        f"| Equity | **${equity:,.2f}** |",
        f"| Cash | ${cash:,.2f} |",
        f"| Reserve | ${equity * CASH_RESERVE_PCT:,.2f} |",
        f"| Regime | BULL |",
        f"| Universe | both |",
        f"| Exit mode | midline / stop{EXIT_STOP * 100:.1f}% / {EXIT_DAYS_MAX}d max |",
        f"| Strategies | {sc['p']} + {sc['s']} |",
        "",
        "## Holdings",
    ]
    if holdings_lines and not holdings_lines[0].startswith("_No"):
        lines.extend(holdings_lines)
    else:
        if run and run.get("tickers"):
            lines.append(f"_EOD open tickers ({run.get('open_positions', '?')}): "
                         f"{run.get('tickers', '').replace('|', ', ')}_")
        else:
            lines.append("_Holdings snapshot not available — see runs.csv._")

    lines += ["", "## Trades today"]
    lines.extend(_format_trades_table(ledger))
    lines += [
        "",
        "## Signals",
        "_Signals not recovered (scan log push may have failed)._",
        "",
        "---",
        f"_RBv8 reconcile {datetime.now().strftime('%H:%M UTC')}_",
    ]

    new_text = "\n".join(lines)
    if dry_run:
        print(f"Would rebuild {fname} ({len(ledger)} trades)")
        return True
    fname.parent.mkdir(parents=True, exist_ok=True)
    fname.write_text(new_text, encoding="utf-8")
    print(f"Rebuilt {fname} ({len(ledger)} trades)")
    return True


def main():
    logs_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("logs")
    days_back = int(sys.argv[2]) if len(sys.argv) > 2 else 7
    dry_run = "--dry-run" in sys.argv

    rebuilt = 0
    today = date.today()
    for i in range(days_back):
        d = today - timedelta(days=i)
        if rebuild_day(logs_dir, d.isoformat(), dry_run=dry_run):
            rebuilt += 1
    print(f"Reconcile complete: {rebuilt} file(s) updated")


if __name__ == "__main__":
    main()
