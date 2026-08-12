"""
options_data_quality_report.py - Split options results into CLEAN vs TAINTED.

CLEAN  = natural take_profit / stop_loss / EOD exits on non-outage days
TAINTED = reconcile_fill / missing_from_broker / known GitHub-outage days
KEEP-only = CLEAN exits from strategies with n>=10, med>=0, win>=50%

Writes:
  logs/options_trial/reports/YYYY-MM-DD_data_quality.md
  logs/options_trial/reports/YYYY-MM-DD_data_quality.csv
  logs/options_trial/reports/latest_data_quality.json
  logs/options_trial/reports/latest_data_quality_snippet.md

Always exits 0 for GHA.
"""
from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from options_lab import LEDGER_PATH, TRIAL_ROOT, ensure_trial_layout  # noqa: E402

REPORTS_DIR = TRIAL_ROOT / "reports"

# Days when GitHub Actions / bot runtime was known degraded
KNOWN_OUTAGE_DAYS = {
    date(2026, 8, 1),
    date(2026, 8, 6),
}

NATURAL_REASON_RE = r"take_profit|stop_loss|^EOD$|eod"
RECENT_SINCE = date(2026, 8, 3)


def _norm_ret(s: pd.Series) -> pd.Series:
    s = pd.to_numeric(s, errors="coerce")
    return s.apply(lambda x: x / 100.0 if pd.notna(x) and abs(x) > 2 else x)


def _tag_exits(exits: pd.DataFrame) -> pd.DataFrame:
    out = exits.copy()
    reason = out["reason"].astype(str)
    out["is_reconcile"] = reason.str.contains("reconcile|missing_from_broker", case=False, na=False)
    out["is_natural"] = reason.str.contains(NATURAL_REASON_RE, case=False, na=False, regex=True)
    out["is_outage_day"] = out["day"].isin(KNOWN_OUTAGE_DAYS)
    out["quality"] = "TAINTED"
    out.loc[out["is_natural"] & ~out["is_outage_day"] & ~out["is_reconcile"], "quality"] = "CLEAN"
    out["ret"] = _norm_ret(out["return_pct"])
    return out


def _summarize(sub: pd.DataFrame) -> dict:
    r = sub["ret"].dropna()
    if r.empty:
        return {"n": 0, "win": 0.0, "med": 0.0, "avg": 0.0, "pnl": 0.0}
    return {
        "n": int(len(r)),
        "win": float((r > 0).mean() * 100),
        "med": float(r.median() * 100),
        "avg": float(r.mean() * 100),
        "pnl": float(pd.to_numeric(sub["pnl_usd"], errors="coerce").fillna(0).sum()),
    }


def _fmt_slice(label: str, s: dict) -> str:
    return (
        f"| {label} | {s['n']} | {s['win']:.1f} | {s['med']:+.1f} | "
        f"{s['avg']:+.1f} | ${s['pnl']:+,.0f} |"
    )


def compute_quality(ledger_path: Path | None = None) -> dict | None:
    """Return quality payload for reports / console / GHA, or None if no data."""
    path = ledger_path or LEDGER_PATH
    if not path.exists():
        return None

    df = pd.read_csv(path)
    if df.empty or "event" not in df.columns:
        return None

    df["ts"] = pd.to_datetime(df["ts"], format="mixed", utc=True)
    df["day"] = df["ts"].dt.date
    df["return_pct"] = pd.to_numeric(df.get("return_pct"), errors="coerce")
    df["pnl_usd"] = pd.to_numeric(df.get("pnl_usd"), errors="coerce")

    exits = df[df["event"].astype(str).str.lower() == "exit"].copy()
    if exits.empty:
        return None

    exits = _tag_exits(exits)
    clean = exits[exits["quality"] == "CLEAN"]
    tainted = exits[exits["quality"] == "TAINTED"]
    recent = clean[clean["day"] >= RECENT_SINCE]

    rows = []
    keep_ids: set[str] = set()
    kill_ids: set[str] = set()
    if not clean.empty:
        for sid, sub in clean.groupby("strategy_id", dropna=False):
            s = _summarize(sub)
            if s["n"] < 1:
                continue
            verdict = "WATCH"
            if s["n"] >= 10 and s["med"] <= -20:
                verdict = "KILL"
                kill_ids.add(str(sid))
            elif s["n"] >= 10 and s["med"] >= 0 and s["win"] >= 50:
                verdict = "KEEP"
                keep_ids.add(str(sid))
            rows.append({
                "strategy_id": sid,
                "quality": "CLEAN",
                "n": s["n"],
                "win_pct": round(s["win"], 1),
                "med_pct": round(s["med"], 1),
                "avg_pct": round(s["avg"], 1),
                "pnl_usd": round(s["pnl"], 2),
                "verdict": verdict,
            })

    keep_only = clean[clean["strategy_id"].astype(str).isin(keep_ids)] if keep_ids else clean.iloc[0:0]
    keep_recent = keep_only[keep_only["day"] >= RECENT_SINCE] if not keep_only.empty else keep_only

    daily = []
    for day, sub in exits.groupby("day"):
        tag = "OUTAGE" if day in KNOWN_OUTAGE_DAYS else (
            "BUGGY" if int(sub["is_reconcile"].sum()) else "OK"
        )
        s = _summarize(sub)
        if s["n"] == 0:
            continue
        daily.append({
            "day": day.isoformat() if hasattr(day, "isoformat") else str(day),
            "tag": tag,
            "n": s["n"],
            "reconcile": int(sub["is_reconcile"].sum()),
            "win": round(s["win"], 1),
            "med": round(s["med"], 1),
        })

    return {
        "as_of": date.today().isoformat(),
        "outage_days": [d.isoformat() for d in sorted(KNOWN_OUTAGE_DAYS)],
        "slices": {
            "all": _summarize(exits),
            "clean": _summarize(clean),
            "tainted": _summarize(tainted),
            "clean_recent": _summarize(recent),
            "keep_only": _summarize(keep_only),
            "keep_only_recent": _summarize(keep_recent),
        },
        "keep_strategies": sorted(keep_ids),
        "kill_strategies": sorted(kill_ids),
        "strategy_rows": rows,
        "daily": daily,
    }


def write_reports(payload: dict) -> tuple[Path, Path, Path, Path]:
    ensure_trial_layout()
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    today = payload["as_of"]
    md_path = REPORTS_DIR / f"{today}_data_quality.md"
    csv_path = REPORTS_DIR / f"{today}_data_quality.csv"
    json_path = REPORTS_DIR / "latest_data_quality.json"
    snippet_path = REPORTS_DIR / "latest_data_quality_snippet.md"

    slices = payload["slices"]
    strat_df = pd.DataFrame(payload["strategy_rows"])
    if not strat_df.empty:
        strat_df = strat_df.sort_values(["verdict", "med_pct"], ascending=[True, True])
        strat_df.to_csv(csv_path, index=False)
    else:
        csv_path.write_text("strategy_id,quality,n,win_pct,med_pct,avg_pct,pnl_usd,verdict\n", encoding="utf-8")

    kills = strat_df[strat_df["verdict"] == "KILL"] if not strat_df.empty else pd.DataFrame()
    keeps = strat_df[strat_df["verdict"] == "KEEP"] if not strat_df.empty else pd.DataFrame()

    lines = [
        f"# Options data quality report - {today}",
        "",
        "Splits ledger exits into **CLEAN** (natural TP/SL/EOD, healthy runtime) "
        "vs **TAINTED** (reconcile_fill / broker-missing / known GitHub outage days).",
        "**KEEP-only** = CLEAN exits from strategies with n>=10, med>=0%, win>=50%.",
        "",
        "## Headline",
        "",
        "| Slice | n | Win% | Med% | Avg% | Realized $ |",
        "|---|---:|---:|---:|---:|---:|",
        _fmt_slice("ALL", slices["all"]),
        _fmt_slice("CLEAN (perfect running)", slices["clean"]),
        _fmt_slice("TAINTED (errors/outages)", slices["tainted"]),
        _fmt_slice(f"CLEAN since {RECENT_SINCE.isoformat()}", slices["clean_recent"]),
        _fmt_slice("KEEP-only (CLEAN keepers)", slices["keep_only"]),
        _fmt_slice(f"KEEP-only since {RECENT_SINCE.isoformat()}", slices["keep_only_recent"]),
        "",
        "## Known outage / degraded days",
        "",
        ", ".join(payload["outage_days"]) or "_none_",
        "",
        "## Daily exit health",
        "",
        "| Day | Tag | n | reconcile-ish | Win% | Med% |",
        "|---|---|---:|---:|---:|---:|",
    ]
    for d in payload["daily"]:
        lines.append(
            f"| {d['day']} | {d['tag']} | {d['n']} | {d['reconcile']} | "
            f"{d['win']:.0f} | {d['med']:+.1f} |"
        )

    lines += ["", "## CLEAN strategy kill list (n>=10, med<=-20%)", ""]
    if kills.empty:
        lines.append("_None yet at strategy grain (need more natural exits)._")
    else:
        lines.append("| strategy | n | win% | med% | avg% | $ |")
        lines.append("|---|---:|---:|---:|---:|---:|")
        for _, r in kills.iterrows():
            lines.append(
                f"| {r['strategy_id']} | {r['n']} | {r['win_pct']} | "
                f"{r['med_pct']:+} | {r['avg_pct']:+} | ${r['pnl_usd']:+,.0f} |"
            )

    lines += ["", "## CLEAN strategy keep list (n>=10, med>=0, win>=50%)", ""]
    if keeps.empty:
        lines.append("_None yet._")
    else:
        lines.append("| strategy | n | win% | med% | avg% | $ |")
        lines.append("|---|---:|---:|---:|---:|---:|")
        for _, r in keeps.sort_values("med_pct", ascending=False).iterrows():
            lines.append(
                f"| {r['strategy_id']} | {r['n']} | {r['win_pct']} | "
                f"{r['med_pct']:+} | {r['avg_pct']:+} | ${r['pnl_usd']:+,.0f} |"
            )

    lines += [
        "",
        "## Notes",
        "",
        "- Prefer CLEAN numbers for promotion / kill decisions.",
        "- KEEP-only is the optimistic lens (past keepers only).",
        "- KILL/KEEP tags are advisory for now - all strategies still trade so "
        "weak names can surprise over the next ~week.",
        "- `reconcile_fill` / outage days are TAINTED, not alpha.",
        "- Protective broker stops (LS...) reduce damage when GitHub is down.",
        "",
    ]
    md_path.write_text("\n".join(lines), encoding="utf-8")

    # Compact JSON for bot console / dashboard (drop bulky daily/strategy if huge)
    json_payload = {
        "as_of": payload["as_of"],
        "outage_days": payload["outage_days"],
        "slices": payload["slices"],
        "keep_strategies": payload["keep_strategies"],
        "kill_strategies": payload["kill_strategies"],
        "keep_count": len(payload["keep_strategies"]),
        "kill_count": len(payload["kill_strategies"]),
    }
    json_path.write_text(json.dumps(json_payload, indent=2), encoding="utf-8")

    c = slices["clean"]
    t = slices["tainted"]
    k = slices["keep_only"]
    kr = slices["keep_only_recent"]
    snippet = [
        "### Options data quality (CLEAN vs TAINTED vs KEEP-only)",
        "",
        "| Slice | n | Win% | Med% | Avg% | $ |",
        "|---|---:|---:|---:|---:|---:|",
        _fmt_slice("CLEAN", c),
        _fmt_slice("TAINTED", t),
        _fmt_slice("KEEP-only", k),
        _fmt_slice("KEEP-only recent", kr),
        "",
        f"- KEEP strategies ({len(payload['keep_strategies'])}): "
        f"{', '.join(payload['keep_strategies']) or '_none_'}",
        f"- KILL strategies ({len(payload['kill_strategies'])}): "
        f"{', '.join(payload['kill_strategies']) or '_none_'}",
        "",
    ]
    snippet_path.write_text("\n".join(snippet), encoding="utf-8")
    return md_path, csv_path, json_path, snippet_path


def run() -> int:
    ensure_trial_layout()
    today = date.today().isoformat()
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    md_path = REPORTS_DIR / f"{today}_data_quality.md"

    payload = compute_quality()
    if payload is None:
        md_path.write_text("# Options data quality\n\n_No ledger exits yet._\n", encoding="utf-8")
        (REPORTS_DIR / "latest_data_quality_snippet.md").write_text(
            "### Options data quality\n\n_No ledger exits yet._\n", encoding="utf-8"
        )
        print(f"Wrote {md_path} (empty)")
        return 0

    md_path, csv_path, json_path, snippet_path = write_reports(payload)
    s = payload["slices"]
    print(f"Wrote {md_path}")
    print(f"Wrote {csv_path}")
    print(f"Wrote {json_path}")
    print(f"Wrote {snippet_path}")
    print(
        f"CLEAN n={s['clean']['n']} med={s['clean']['med']:+.1f}% | "
        f"TAINTED n={s['tainted']['n']} med={s['tainted']['med']:+.1f}% | "
        f"KEEP-only n={s['keep_only']['n']} med={s['keep_only']['med']:+.1f}% | "
        f"KILL={len(payload['kill_strategies'])} KEEP={len(payload['keep_strategies'])}"
    )
    return 0


def main() -> int:
    try:
        return run()
    except Exception as e:
        print(f"data quality report failed (non-fatal): {e}")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
