#!/usr/bin/env python3
"""Year-over-year pattern analysis: midcap promote / crash / stable cohorts."""
from __future__ import annotations

try:
    from repo_root import find_repo_root
except ImportError:
    import sys as _sys
    from pathlib import Path as _Path
    _sys.path.insert(0, str(_Path(__file__).resolve().parents[2] / "live-bots" / "shared"))
    from repo_root import find_repo_root


import json
from datetime import date, timedelta
from pathlib import Path

import pandas as pd
import yfinance as yf

OUT = find_repo_root(Path(__file__)) / "logs" / "research"
OUT.mkdir(parents=True, exist_ok=True)

# Curated case studies from S&P index change history (2023-2026)
CASES = {
    "promoted_sp500": {
        "SMCI": {"added": "2024-03-18", "note": "AI server boom; revenue hypergrowth"},
        "CRWD": {"added": "2024-06-24", "note": "Cybersecurity platform scale"},
        "PLTR": {"added": "2024-09-23", "note": "Gov+enterprise AI adoption"},
        "DECK": {"added": "2024-03-18", "note": "HOKA/UGG brand momentum"},
        "VST": {"added": "2024-05-08", "note": "Power/data-center demand"},
        "CVNA": {"added": "2025-12-22", "note": "Turnaround + used-car re-rating"},
        "FIX": {"added": "2025-12-22", "note": "Data-center HVAC contractor"},
        "APP": {"added": "2025-09-22", "note": "Mobile ad-tech profitability"},
        "HOOD": {"added": "2025-09-22", "note": "Retail trading + crypto rev"},
        "COIN": {"added": "2025-05-19", "note": "Crypto cycle beneficiary"},
        "DASH": {"added": "2025-03-24", "note": "Delivery platform profitability"},
        "GDDY": {"added": "2024-06-24", "note": "Domain/hosting cash cow"},
    },
    "demoted_or_crashed": {
        "BBWI": {"removed": "2024-10-01", "note": "Mall retail structural decline"},
        "VFC": {"removed": "2024-04-03", "note": "Vans/North Face brand fatigue"},
        "XRAY": {"removed": "2024-04-03", "note": "Dental equipment demand slump"},
        "ENPH": {"removed": "2025-09-22", "note": "Solar inventory glut + rates"},
        "EPAM": {"removed": "2026-06-02", "note": "IT services Eastern Europe exposure"},
        "ZION": {"removed": "2024-03-18", "note": "Regional bank CRE stress"},
        "WHR": {"removed": "2024-03-18", "note": "Appliance cycle + China"},
        "ETSY": {"removed": "2024-09-23", "note": "Post-COVID handmade slowdown"},
        "ILMN": {"removed": "2024-06-24", "note": "Genomics competition + spend cut"},
        "CZR": {"removed": "2025-09-22", "note": "Gaming leverage + weak traffic"},
        "CELH": {"note": "High-growth beverage; volatile drawdowns (still midcap)"},
        "UPST": {"note": "AI lending model; 90%+ drawdown from peak"},
    },
    "stable_midcap": {
        "ROL": {"note": "Pest control; steady compounder in S&P 400"},
        "POOL": {"note": "Pool supplies oligopoly; removed S&P500 2026 for RDDT"},
        "MKTX": {"note": "Bond trading platform; mature fintech midcap"},
        "PAYC": {"note": "Payroll SaaS; consistent midcap"},
        "TECH": {"note": "Bio tools (Bio-Techne); defensive growth"},
        "WST": {"note": "Medical packaging; low-vol compounder"},
        "BRO": {"note": "Insurance broker rollup"},
        "RBC": {"note": "Industrial bearings; cyclical but stable index member"},
    },
}


def _fetch_metrics(ticker: str, as_of: date | None = None) -> dict:
    as_of = as_of or date.today()
    t = yf.Ticker(ticker)
    hist = t.history(start=str(as_of - timedelta(days=800)), end=str(as_of + timedelta(days=1)))
    if hist.empty:
        return {"ticker": ticker, "error": "no price data"}

    px = hist["Close"]
    last = float(px.iloc[-1])
    d252 = px.iloc[-252] if len(px) >= 252 else px.iloc[0]
    d504 = px.iloc[-504] if len(px) >= 504 else px.iloc[0]
    y1 = (last / float(d252) - 1) * 100
    y2 = (last / float(d504) - 1) * 100 if len(px) >= 504 else None
    peak = float(px.max())
    dd = (last / peak - 1) * 100

    info = {}
    try:
        info = t.info or {}
    except Exception:
        pass

    mcap = info.get("marketCap")
    rev_growth = info.get("revenueGrowth")
    profit_margin = info.get("profitMargins")
    pe = info.get("trailingPE")
    sector = info.get("sector", "Unknown")
    industry = info.get("industry", "")

    return {
        "ticker": ticker,
        "price": round(last, 2),
        "return_1y_pct": round(y1, 1),
        "return_2y_pct": round(y2, 1) if y2 is not None else None,
        "drawdown_from_peak_pct": round(dd, 1),
        "market_cap_b": round(mcap / 1e9, 2) if mcap else None,
        "revenue_growth_pct": round(rev_growth * 100, 1) if rev_growth else None,
        "profit_margin_pct": round(profit_margin * 100, 1) if profit_margin else None,
        "pe": round(pe, 1) if pe else None,
        "sector": sector,
        "industry": industry,
    }


def main() -> None:
    rows = []
    for cohort, cases in CASES.items():
        for ticker, meta in cases.items():
            m = _fetch_metrics(ticker)
            m["cohort"] = cohort
            m.update(meta)
            rows.append(m)
            print(f"{cohort:20} {ticker:6} 1y={m.get('return_1y_pct')}% mcap=${m.get('market_cap_b')}B")

    df = pd.DataFrame(rows)
    df.to_csv(OUT / "midcap_yoy_cases.csv", index=False)

    summary = {}
    for cohort in CASES:
        sub = df[df["cohort"] == cohort]
        summary[cohort] = {
            "n": len(sub),
            "median_1y_return": float(sub["return_1y_pct"].median()),
            "median_drawdown": float(sub["drawdown_from_peak_pct"].median()),
            "median_rev_growth": float(sub["revenue_growth_pct"].dropna().median()) if sub["revenue_growth_pct"].notna().any() else None,
            "median_mcap_b": float(sub["market_cap_b"].dropna().median()) if sub["market_cap_b"].notna().any() else None,
        }

    payload = {"generated": str(date.today()), "summary": summary, "cases": rows}
    (OUT / "midcap_yoy_analysis.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print("\nSummary:", json.dumps(summary, indent=2))
    print(f"Wrote {OUT / 'midcap_yoy_analysis.json'}")


if __name__ == "__main__":
    main()
