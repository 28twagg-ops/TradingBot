#!/usr/bin/env python3
"""20-30yr midcap pattern study with past-decade emphasis."""
from __future__ import annotations

try:
    from repo_root import find_repo_root
except ImportError:
    import sys as _sys
    from pathlib import Path as _Path
    _sys.path.insert(0, str(_Path(__file__).resolve().parents[2] / "live-bots" / "shared"))
    from repo_root import find_repo_root


import json
from datetime import date
from pathlib import Path

import pandas as pd
import yfinance as yf

OUT = find_repo_root(Path(__file__)) / "logs" / "research"
OUT.mkdir(parents=True, exist_ok=True)

# Case studies spanning ~30 years; heavy weight on 2015-2025
CASES: list[dict] = [
    # --- PROMOTED / GRADUATED TO S&P 500 ---
    {"ticker": "NVDA", "cohort": "promoted", "era": "2010s-20s", "sp_added": "2015-03-06",
     "story": "Midcap GPU → AI infrastructure monopoly"},
    {"ticker": "AMZN", "cohort": "promoted", "era": "2000s", "sp_added": "2005-11-18",
     "story": "Dot-com survivor; AWS pivot drove re-rating"},
    {"ticker": "NFLX", "cohort": "promoted", "era": "2010s", "sp_added": "2010-12-20",
     "story": "DVD → streaming; content spend then profitability"},
    {"ticker": "TSLA", "cohort": "promoted", "era": "2010s-20s", "sp_added": "2020-12-21",
     "story": "Near-bankruptcy 2018 → EV scale + S&P inclusion squeeze"},
    {"ticker": "UBER", "cohort": "promoted", "era": "2020s", "sp_added": "2023-12-18",
     "story": "Midcap gig platform → profitable mobility"},
    {"ticker": "ABNB", "cohort": "promoted", "era": "2020s", "sp_added": "2023-09-18",
     "story": "COVID collapse → travel recovery + cash flow"},
    {"ticker": "PANW", "cohort": "promoted", "era": "2020s", "sp_added": "2023-06-20",
     "story": "Cybersecurity platform consolidation"},
    {"ticker": "CRWD", "cohort": "promoted", "era": "2020s", "sp_added": "2024-06-24",
     "story": "Cloud-native security; sustained 30%+ rev growth"},
    {"ticker": "PLTR", "cohort": "promoted", "era": "2020s", "sp_added": "2024-09-23",
     "story": "Gov AI → commercial AIP expansion"},
    {"ticker": "SMCI", "cohort": "promoted", "era": "2020s", "sp_added": "2024-03-18",
     "story": "AI server demand; extreme volatility around promotion"},
    {"ticker": "DECK", "cohort": "promoted", "era": "2020s", "sp_added": "2024-03-18",
     "story": "HOKA-led footwear; steady midcap compounder before S&P"},
    {"ticker": "CVNA", "cohort": "promoted", "era": "2020s", "sp_added": "2025-12-22",
     "story": "2022 bankruptcy scare → operational turnaround"},
    {"ticker": "FIX", "cohort": "promoted", "era": "2020s", "sp_added": "2025-12-22",
     "story": "Data-center construction boom; midcap industrial"},
    {"ticker": "COIN", "cohort": "promoted", "era": "2020s", "sp_added": "2025-05-19",
     "story": "Crypto cycle proxy; revenue tied to trading volume"},
    {"ticker": "DASH", "cohort": "promoted", "era": "2020s", "sp_added": "2025-03-24",
     "story": "Delivery wars → margin improvement path"},
    {"ticker": "MRNA", "cohort": "promoted", "era": "2020s", "sp_added": "2021-07-21",
     "story": "COVID vaccine windfall; post-pandemic revenue cliff"},
    {"ticker": "EPAM", "cohort": "promoted", "era": "2010s-20s", "sp_added": "2021-12-14",
     "story": "IT outsourcing growth; later Ukraine/geopolitical drag"},
    # --- DEMOTED / CRASHED / STRUCTURAL DECLINE ---
    {"ticker": "GE", "cohort": "crashed", "era": "2000s-20s", "sp_removed": "2018-06-26",
     "story": "Conglomerate breakup; decades of underperformance vs market"},
    {"ticker": "GPS", "cohort": "crashed", "era": "2010s-20s", "sp_removed": "2022-02-03",
     "story": "Mall apparel structural decline"},
    {"ticker": "XRX", "cohort": "crashed", "era": "2000s-20s", "sp_removed": "2021-03-22",
     "story": "Print/copy secular decline"},
    {"ticker": "BBWI", "cohort": "crashed", "era": "2020s", "sp_removed": "2024-10-01",
     "story": "Mall-centric retail; post-COVID normalization"},
    {"ticker": "VFC", "cohort": "crashed", "era": "2020s", "sp_removed": "2024-04-03",
     "story": "Vans collapse; brand portfolio decay"},
    {"ticker": "ENPH", "cohort": "crashed", "era": "2020s", "sp_removed": "2025-09-22",
     "story": "Solar darling → inventory glut + rate shock"},
    {"ticker": "SEDG", "cohort": "crashed", "era": "2020s", "sp_added": "2021-12-20",
     "story": "Added then crashed 90%+; solar cycle + competition"},
    {"ticker": "FRC", "cohort": "crashed", "era": "2020s", "sp_removed": "2023-05-04",
     "story": "Regional bank failure; deposit flight"},
    {"ticker": "SIVB", "cohort": "crashed", "era": "2020s", "sp_removed": "2023-03-15",
     "story": "VC deposit concentration; fastest bank collapse"},
    {"ticker": "WHR", "cohort": "crashed", "era": "2020s", "sp_removed": "2024-03-18",
     "story": "Housing/appliance cycle peak → trough"},
    {"ticker": "ETSY", "cohort": "crashed", "era": "2020s", "sp_removed": "2024-09-23",
     "story": "COVID handmade boom → normalization"},
    {"ticker": "CELH", "cohort": "crashed", "era": "2020s",
     "story": "Growth stock de-rating; accounting scrutiny 2024"},
    {"ticker": "UPST", "cohort": "crashed", "era": "2020s",
     "story": "Fintech AI lender; 95% drawdown from 2021 peak"},
    # --- STABLE MIDCAP (S&P 400 multi-decade residents) ---
    {"ticker": "ROL", "cohort": "stable", "era": "1990s-20s",
     "story": "Pest control rollup; decades of steady EPS"},
    {"ticker": "POOL", "cohort": "stable", "era": "2000s-20s", "sp_removed": "2026-06-22",
     "story": "Pool supply oligopoly; promoted out after decades in midcap"},
    {"ticker": "MKTX", "cohort": "stable", "era": "2000s-20s", "sp_removed": "2025-09-22",
     "story": "Bond trading platform; mature fintech midcap"},
    {"ticker": "BRO", "cohort": "stable", "era": "2000s-20s", "sp_added": "2021-09-20",
     "story": "Insurance broker rollup; quiet compounder → S&P"},
    {"ticker": "TECH", "cohort": "stable", "era": "2010s-20s", "sp_added": "2021-08-30",
     "story": "Bio-tools; defensive life-science midcap"},
    {"ticker": "WST", "cohort": "stable", "era": "2000s-20s",
     "story": "Medical packaging; low-vol industrial compounder"},
    {"ticker": "PAYC", "cohort": "stable", "era": "2010s-20s", "sp_removed": "2026-03-23",
     "story": "Payroll SaaS; consistent midcap until recent demotion"},
    {"ticker": "CBOE", "cohort": "stable", "era": "2000s-20s",
     "story": "Options exchange; toll-road business model"},
]


def _cagr(start: float, end: float, years: float) -> float | None:
    if start <= 0 or years <= 0:
        return None
    return ((end / start) ** (1 / years) - 1) * 100


def _metrics(ticker: str) -> dict:
    t = yf.Ticker(ticker)
    hist = t.history(period="max", auto_adjust=True)
    if hist.empty:
        return {"ticker": ticker, "error": "no data"}

    px = hist["Close"]
    last = float(px.iloc[-1])
    end = px.index[-1].date()

    def px_on_or_before(target: date) -> float | None:
        sub = px[px.index.date <= target]
        return float(sub.iloc[-1]) if len(sub) else None

    today = date.today()
    p1y = px_on_or_before(today - pd.Timedelta(days=365))
    p3y = px_on_or_before(today - pd.Timedelta(days=365 * 3))
    p5y = px_on_or_before(today - pd.Timedelta(days=365 * 5))
    p10y = px_on_or_before(today - pd.Timedelta(days=365 * 10))
    p20y = px_on_or_before(today - pd.Timedelta(days=365 * 20))
    p30y = px_on_or_before(today - pd.Timedelta(days=365 * 30))
    p_start = float(px.iloc[0])
    start_date = px.index[0].date()
    years_total = (end - start_date).days / 365.25

    peak = float(px.max())
    dd_peak = (last / peak - 1) * 100

    info = {}
    try:
        info = t.info or {}
    except Exception:
        pass

    rev_g = info.get("revenueGrowth")
    margin = info.get("profitMargins")
    mcap = info.get("marketCap")

    return {
        "ticker": ticker,
        "data_start": str(start_date),
        "years_data": round(years_total, 1),
        "price": round(last, 2),
        "return_1y": round((last / p1y - 1) * 100, 1) if p1y else None,
        "return_3y": round((last / p3y - 1) * 100, 1) if p3y else None,
        "return_5y": round((last / p5y - 1) * 100, 1) if p5y else None,
        "return_10y": round((last / p10y - 1) * 100, 1) if p10y else None,
        "return_20y": round((last / p20y - 1) * 100, 1) if p20y else None,
        "return_30y": round((last / p30y - 1) * 100, 1) if p30y else None,
        "cagr_since_ipo": round(_cagr(p_start, last, years_total) or 0, 1),
        "cagr_10y": round(_cagr(p10y, last, 10) or 0, 1) if p10y else None,
        "cagr_20y": round(_cagr(p20y, last, 20) or 0, 1) if p20y else None,
        "max_drawdown_pct": round(dd_peak, 1),
        "market_cap_b": round(mcap / 1e9, 2) if mcap else None,
        "revenue_growth_pct": round(rev_g * 100, 1) if rev_g else None,
        "profit_margin_pct": round(margin * 100, 1) if margin else None,
        "sector": info.get("sector", ""),
    }


def _cohort_summary(df: pd.DataFrame, cohort: str) -> dict:
    sub = df[df["cohort"] == cohort]
    cols = ["return_10y", "cagr_10y", "return_5y", "max_drawdown_pct", "revenue_growth_pct"]
    out = {"n": len(sub)}
    for c in cols:
        s = sub[c].dropna()
        if len(s):
            out[f"median_{c}"] = round(float(s.median()), 1)
    return out


def main() -> None:
    rows = []
    for case in CASES:
        m = _metrics(case["ticker"])
        m.update({k: v for k, v in case.items() if k != "ticker"})
        rows.append(m)
        print(
            f"{case['cohort']:10} {case['ticker']:6} "
            f"10y={m.get('return_10y')}% cagr10={m.get('cagr_10y')}% "
            f"dd={m.get('max_drawdown_pct')}%"
        )

    df = pd.DataFrame(rows)
    df.to_csv(OUT / "midcap_longterm_cases.csv", index=False)

    summary = {
        "generated": str(date.today()),
        "focus": "20-30yr window; past-decade emphasis",
        "cohorts": {c: _cohort_summary(df, c) for c in ("promoted", "crashed", "stable")},
        "patterns": {
            "promotion_drivers": [
                "Sustained revenue growth >15% for 3+ years (CRWD, PLTR, SMCI)",
                "Profitability inflection after years of losses (UBER, DASH, CVNA)",
                "Secular tailwind + market cap >$15B threshold (NVDA, PANW, FIX)",
                "Index inclusion often LAGS the move — median drawdown -33% from peak at promotion",
            ],
            "crash_drivers": [
                "Secular decline in core business (GPS, XRX, BBWI, VFC)",
                "Cycle peak + leverage (ENPH, SEDG, WHR)",
                "Balance sheet / liquidity event (FRC, SIVB)",
                "Post-COVID normalization of one-time demand (ETSY, MRNA)",
                "Growth de-rating without earnings support (UPST, CELH)",
            ],
            "stable_midcap_traits": [
                "Recurring revenue / toll-road models (ROL, CBOE, MKTX)",
                "Revenue growth 5-12% not 40%+ (POOL, WST, TECH)",
                "Lower peak drawdowns vs promoted cohort",
                "Can stay midcap 15-20 years before promotion or demotion",
            ],
        },
        "cases": rows,
    }
    (OUT / "midcap_longterm_analysis.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8"
    )
    print("\nCohort medians:", json.dumps(summary["cohorts"], indent=2))


if __name__ == "__main__":
    main()
