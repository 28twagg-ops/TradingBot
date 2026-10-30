from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from myers.config import StrategyConfig
from myers.schemas import CompanyAnalysis, Confidence, Recommendation


@dataclass
class RejectionRecord:
    ticker: str
    date: str
    score: float | None
    min_score: float
    price: float | None
    fair_value_base: float | None
    margin_of_safety: float | None
    min_mos: float
    recommendation: str
    confidence: str
    categories: list[str] = field(default_factory=list)
    reasons: list[str] = field(default_factory=list)
    would_pass_alt: dict[str, bool] = field(default_factory=dict)


def classify_rejections(
    analysis: CompanyAnalysis,
    cfg: StrategyConfig,
    *,
    portfolio_block: str | None = None,
) -> RejectionRecord:
    """Collect ALL applicable rejection categories (not just the first)."""
    cats: list[str] = []
    reasons: list[str] = []
    m = analysis.metrics
    v = analysis.valuation
    mos = v.base_margin_of_safety

    if analysis.recommendation == Recommendation.EXCLUDED:
        cats.append("other_eligibility")
        reasons.extend(analysis.reasons or ["excluded from universe"])

    if analysis.data_confidence in (Confidence.NONE, Confidence.LOW) and analysis.missing_fields:
        cats.append("missing_or_unreliable_data")
        reasons.append(f"confidence={analysis.data_confidence.value}; missing={analysis.missing_fields}")

    nd = m.get("net_debt_to_ebitda")
    if nd is not None and nd > cfg.screening.max_net_debt_to_ebitda:
        cats.append("excessive_debt")
        reasons.append(f"net_debt/EBITDA={nd:.2f} > {cfg.screening.max_net_debt_to_ebitda}")

    ic = m.get("interest_coverage")
    if ic is not None and ic < cfg.screening.min_interest_coverage:
        cats.append("insufficient_financial_health")
        reasons.append(f"interest_coverage={ic:.2f}")

    fm = m.get("fcf_margin")
    cc = m.get("cash_conversion")
    if (fm is not None and fm < 0) or (cc is not None and cc < 0.6):
        cats.append("weak_or_inconsistent_cash_flow")
        reasons.append(f"fcf_margin={fm}, cash_conversion={cc}")

    if analysis.fundamental_score < cfg.signals.buy_min_score:
        cats.append("low_business_quality_or_score")
        reasons.append(
            f"score={analysis.fundamental_score:.1f} < min {cfg.signals.buy_min_score}"
        )

    if mos is None:
        cats.append("insufficient_margin_of_safety")
        reasons.append("margin_of_safety unavailable")
    elif mos < cfg.valuation.margin_of_safety_buy:
        cats.append("insufficient_margin_of_safety")
        reasons.append(
            f"MOS={mos:.1%} < required {cfg.valuation.margin_of_safety_buy:.1%}"
        )
        if mos < 0:
            cats.append("excessive_valuation")
            reasons.append("price above base fair value (negative MOS)")

    # Concentration UNKNOWN is a soft review flag, not a hard reject in v1
    if any("UNKNOWN" in n for n in (analysis.major_risks or [])):
        cats.append("customer_or_management_concentration_unknown")

    if portfolio_block:
        cats.append("portfolio_concentration_restrictions")
        reasons.append(portfolio_block)

    if not cats and analysis.recommendation != Recommendation.BUY_CANDIDATE:
        cats.append("other_documented")
        reasons.extend(analysis.reasons or ["did not meet buy rules"])

    # Alternative parameter what-if (same analysis numbers)
    would = {
        "mos_15": bool(
            analysis.fundamental_score >= 70
            and mos is not None
            and mos >= 0.15
            and analysis.recommendation != Recommendation.EXCLUDED
        ),
        "mos_0_score_80": bool(
            analysis.fundamental_score >= 80
            and mos is not None
            and mos >= 0.0
            and analysis.recommendation != Recommendation.EXCLUDED
        ),
        "mos_30_score_60": bool(
            analysis.fundamental_score >= 60
            and mos is not None
            and mos >= 0.30
            and analysis.recommendation != Recommendation.EXCLUDED
        ),
    }

    return RejectionRecord(
        ticker=analysis.ticker,
        date=analysis.analysis_date.isoformat(),
        score=analysis.fundamental_score,
        min_score=cfg.signals.buy_min_score,
        price=analysis.current_price,
        fair_value_base=v.fair_value_base,
        margin_of_safety=mos,
        min_mos=cfg.valuation.margin_of_safety_buy,
        recommendation=analysis.recommendation.value,
        confidence=analysis.data_confidence.value,
        categories=sorted(set(cats)),
        reasons=reasons,
        would_pass_alt=would,
    )


def summarize_diagnostics(rows: list[RejectionRecord]) -> dict[str, Any]:
    from collections import Counter

    n = len(rows)
    buys = sum(1 for r in rows if r.recommendation == "BUY_CANDIDATE")
    cat_counts: Counter[str] = Counter()
    for r in rows:
        if r.recommendation == "BUY_CANDIDATE":
            continue
        for c in r.categories:
            cat_counts[c] += 1
    scores = [r.score for r in rows if r.score is not None]
    moss = [r.margin_of_safety for r in rows if r.margin_of_safety is not None]
    near = sorted(
        [r for r in rows if r.recommendation != "BUY_CANDIDATE"],
        key=lambda r: (
            -(r.score or 0),
            -(r.margin_of_safety if r.margin_of_safety is not None else -99),
        ),
    )[:15]
    return {
        "n_evaluated": n,
        "n_buy_candidate": buys,
        "buy_rate": buys / n if n else 0.0,
        "rejection_category_counts": dict(cat_counts.most_common()),
        "score_median": float(pd_median(scores)),
        "mos_median": float(pd_median(moss)),
        "would_pass_mos_15": sum(1 for r in rows if r.would_pass_alt.get("mos_15")),
        "would_pass_quality_fair": sum(1 for r in rows if r.would_pass_alt.get("mos_0_score_80")),
        "would_pass_deep_value": sum(1 for r in rows if r.would_pass_alt.get("mos_30_score_60")),
        "closest_to_qualifying": [
            {
                "ticker": r.ticker,
                "date": r.date,
                "score": r.score,
                "mos": r.margin_of_safety,
                "categories": r.categories,
            }
            for r in near
        ],
    }


def pd_median(xs: list[float]) -> float:
    if not xs:
        return float("nan")
    s = sorted(xs)
    mid = len(s) // 2
    if len(s) % 2:
        return s[mid]
    return 0.5 * (s[mid - 1] + s[mid])
