"""Streamlit dashboard for Myers Stock Investor (research / paper only)."""
from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path

import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from myers.config import load_config
from myers.strategy.diagnostics import classify_rejections, summarize_diagnostics
from myers.strategy.engine import analyze_stock
from myers.strategy.profiles import PROFILES
from myers.schemas import Recommendation

st.set_page_config(page_title="Myers Stock Investor", layout="wide")
cfg = load_config()

st.title("Myers Stock Investor")
st.caption(
    f"Model {cfg.model_version} · mode={cfg.backtest.research_mode} · "
    f"Live trading {'ON' if cfg.live_trading_enabled else 'DISABLED'}"
)

tabs = st.tabs(
    [
        "Overview",
        "Screener",
        "Company",
        "Diagnostics",
        "Backtest outputs",
        "Data / Audit",
    ]
)

with tabs[0]:
    st.subheader("Market overview (ad-hoc slice)")
    tickers = st.text_input("Tickers", "AAPL,MSFT,COST,XOM,JNJ,CAT,UNH,PG,WMT,MRK")
    as_of = st.date_input("As-of", value=date.today())
    if st.button("Run overview"):
        rows = []
        rejs = []
        for t in [x.strip().upper() for x in tickers.split(",") if x.strip()]:
            try:
                a = analyze_stock(t, as_of_date=as_of, cfg=cfg)
                rows.append(
                    {
                        "ticker": a.ticker,
                        "company": a.company_name,
                        "sector": a.sector,
                        "price": a.current_price,
                        "score": a.fundamental_score,
                        "confidence": a.data_confidence.value,
                        "mos": a.valuation.base_margin_of_safety,
                        "status": a.recommendation.value,
                    }
                )
                if a.recommendation != Recommendation.BUY_CANDIDATE:
                    rejs.append(classify_rejections(a, cfg))
            except Exception as exc:
                rows.append({"ticker": t, "status": f"ERROR: {exc}"})
        df = pd.DataFrame(rows)
        st.dataframe(df, use_container_width=True)
        if len(df):
            st.metric("Median score", f"{df['score'].median():.1f}" if "score" in df else "n/a")
            st.metric(
                "Buy candidates",
                int((df["status"] == "BUY_CANDIDATE").sum()) if "status" in df else 0,
            )
        if rejs:
            st.json(summarize_diagnostics(rejs))

with tabs[1]:
    st.subheader("Stock screener")
    st.write("Use Overview to populate; filter in the dataframe column headers.")
    st.info("Screener uses the same deterministic engine as `python -m myers analyze`.")

with tabs[2]:
    t = st.text_input("Ticker", "AAPL", key="dd")
    if st.button("Deep dive"):
        a = analyze_stock(t.upper(), cfg=cfg)
        c1, c2, c3 = st.columns(3)
        c1.metric("Score", f"{a.fundamental_score:.1f}")
        c2.metric("MOS", f"{(a.valuation.base_margin_of_safety or 0):.1%}")
        c3.metric("Status", a.recommendation.value)
        st.write(a.investment_thesis)
        st.write("Reverse DCF:", a.valuation.reverse_dcf_interpretation)
        st.write(
            "Implied growth:",
            a.valuation.reverse_dcf_implied_growth,
        )
        st.json(a.model_dump(mode="json"))

with tabs[3]:
    st.subheader("Screening diagnostics")
    path = ROOT / "outputs" / "backtest" / "rejections.csv"
    if path.exists():
        rdf = pd.read_csv(path)
        st.dataframe(rdf.head(200), use_container_width=True)
        if "categories" in rdf.columns:
            st.write("Load metrics.json for aggregated category counts.")
        mpath = ROOT / "outputs" / "backtest" / "metrics.json"
        if mpath.exists():
            st.json(json.loads(mpath.read_text(encoding="utf-8")).get("diagnostics", {}))
    else:
        st.warning("No rejections.csv yet — run `python -m myers backtest` first.")

with tabs[4]:
    st.subheader("Backtest / comparison outputs")
    for label, p in [
        ("Backtest summary", ROOT / "outputs" / "backtest" / "summary.md"),
        ("Comparison", ROOT / "outputs" / "compare" / "comparison.md"),
        ("Audit", ROOT / "outputs" / "AUDIT_REPORT.md"),
    ]:
        if p.exists():
            st.markdown(f"### {label}")
            st.markdown(p.read_text(encoding="utf-8")[:12000])
        else:
            st.write(f"Missing {p}")

with tabs[5]:
    st.markdown(
        f"""
### Data providers
- Prices: yfinance adjusted closes (splits/dividends in close when auto_adjust=True)
- Fundamentals: yfinance statements/info (**not filing-date PIT**)
- SEC EDGAR helper: optional enrichment (`myers/data/sec_edgar.py`)

### Research mode
Current config: **{cfg.backtest.research_mode}**

Validated mode refuses to run until a PIT fundamentals provider is wired.

### Profiles
"""
    )
    for k, p in PROFILES.items():
        st.write(f"- `{k}`: {p.description}")
