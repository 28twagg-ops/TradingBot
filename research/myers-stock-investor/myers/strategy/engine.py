from __future__ import annotations

from datetime import date

from myers.analysis.metrics import compute_metrics
from myers.config import StrategyConfig, load_config
from myers.data.fundamentals import fetch_fundamentals
from myers.data.market import latest_price_as_of
from myers.schemas import CompanyAnalysis, Recommendation
from myers.strategy.eligibility import excluded_reason
from myers.strategy.scoring import assess_confidence, build_category_scores, total_score
from myers.strategy.signals import determine_recommendation
from myers.valuation.engine import value_company


def analyze_stock(
    ticker: str,
    as_of_date: date | None = None,
    cfg: StrategyConfig | None = None,
) -> CompanyAnalysis:
    """Myers decision engine: validate → screen → analyze → value → score → signal."""
    cfg = cfg or load_config()
    as_of = as_of_date or date.today()
    ticker = ticker.upper().strip()

    if cfg.live_trading_enabled:
        # Safety belt — this codebase never enables live trading by default.
        raise RuntimeError("live_trading_enabled must remain false in v1")

    fund = fetch_fundamentals(ticker, as_of=as_of)
    price = latest_price_as_of(ticker, as_of)
    ex = excluded_reason(fund, cfg, as_of)
    metrics = compute_metrics(fund)
    val = value_company(fund, metrics, price, cfg.valuation)
    cats = build_category_scores(fund, metrics, val, cfg)
    score = total_score(cats, cfg)
    confidence = assess_confidence(fund, metrics)

    if ex:
        rec, reasons, risks = determine_recommendation(
            score=score,
            confidence=confidence,
            valuation=val,
            metrics=metrics,
            cfg=cfg,
            excluded=True,
        )
        reasons = [ex] + reasons
    else:
        rec, reasons, risks = determine_recommendation(
            score=score,
            confidence=confidence,
            valuation=val,
            metrics=metrics,
            cfg=cfg,
            excluded=False,
        )

    thesis = _basic_thesis(ticker, fund, metrics, val, rec)

    return CompanyAnalysis(
        ticker=ticker,
        analysis_date=as_of,
        company_name=fund.company_name,
        sector=fund.sector,
        industry=fund.industry,
        current_price=price,
        market_cap=fund.market_cap,
        fundamental_score=score,
        data_confidence=confidence,
        category_scores=cats,
        valuation=val,
        recommendation=rec,
        major_risks=risks,
        investment_thesis=thesis,
        reasons=reasons,
        metrics=metrics,
        missing_fields=list(fund.missing),
        source_references=[
            f"yfinance:{ticker}",
            f"retrieved:{fund.retrieved_at.isoformat()}Z",
        ],
        model_version=cfg.model_version,
    )


def _basic_thesis(ticker, fund, metrics, val, rec: Recommendation) -> str:
    name = fund.company_name or ticker
    parts = [
        f"{name} is analyzed as a business ownership candidate.",
        f"Recommendation={rec.value}.",
    ]
    if metrics.get("fcf_margin") is not None:
        parts.append(f"FCF margin≈{metrics['fcf_margin']:.1%}.")
    if metrics.get("net_debt_to_ebitda") is not None:
        parts.append(f"Net debt/EBITDA≈{metrics['net_debt_to_ebitda']:.2f}.")
    if val.base_margin_of_safety is not None:
        parts.append(f"Base DCF margin of safety≈{val.base_margin_of_safety:.0%}.")
    parts.append(
        "Customer concentration and key-person risk are UNKNOWN until 10-K/proxy review."
    )
    return " ".join(parts)
