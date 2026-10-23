from __future__ import annotations

from myers.config import StrategyConfig
from myers.schemas import Confidence, Recommendation, ValuationResult


_CONF_RANK = {
    Confidence.NONE: 0,
    Confidence.LOW: 1,
    Confidence.MEDIUM: 2,
    Confidence.HIGH: 3,
}


def determine_recommendation(
    *,
    score: float,
    confidence: Confidence,
    valuation: ValuationResult,
    metrics: dict[str, float | None],
    cfg: StrategyConfig,
    excluded: bool = False,
) -> tuple[Recommendation, list[str], list[str]]:
    reasons: list[str] = []
    risks: list[str] = []

    if excluded:
        return Recommendation.EXCLUDED, ["Failed universe / sector eligibility"], risks

    if confidence == Confidence.NONE or score <= 0:
        return (
            Recommendation.INSUFFICIENT_DATA,
            ["Material financial inputs missing; no automated eligibility"],
            risks,
        )

    nd = metrics.get("net_debt_to_ebitda")
    if nd is not None and nd > cfg.screening.max_net_debt_to_ebitda:
        risks.append(f"Elevated leverage net_debt/EBITDA={nd:.2f}")
    ic = metrics.get("interest_coverage")
    if ic is not None and ic < cfg.screening.min_interest_coverage:
        risks.append(f"Weak interest coverage={ic:.2f}")
    cc = metrics.get("cash_conversion")
    if cc is not None and cc < 0.6:
        risks.append(f"Weak cash conversion CFO/NI={cc:.2f}")
    if metrics.get("fcf_margin") is not None and (metrics["fcf_margin"] or 0) < 0:
        risks.append("Negative free cash flow margin")

    mos = valuation.base_margin_of_safety
    min_conf = Confidence[cfg.signals.buy_min_confidence]

    # Hard block buys on critical leverage/cash flags
    critical_risk = any("Elevated leverage" in r or "Negative free cash flow" in r for r in risks)

    if (
        score >= cfg.signals.buy_min_score
        and _CONF_RANK[confidence] >= _CONF_RANK[min_conf]
        and mos is not None
        and mos >= cfg.valuation.margin_of_safety_buy
        and not critical_risk
    ):
        reasons.append(
            f"Score {score:.0f} with base margin of safety {mos:.0%} "
            f"(threshold {cfg.valuation.margin_of_safety_buy:.0%})"
        )
        return Recommendation.BUY_CANDIDATE, reasons, risks

    if score >= cfg.signals.buy_min_score and (mos is None or mos < cfg.valuation.margin_of_safety_buy):
        reasons.append(
            "Business quality/score attractive but valuation lacks required margin of safety → WATCH"
        )
        return Recommendation.WATCH, reasons, risks

    if score >= cfg.signals.watch_min_score:
        reasons.append(f"Mixed/moderate score {score:.0f}")
        return Recommendation.WATCH, reasons, risks

    if critical_risk or score < 40:
        reasons.append("Significant fundamental concerns")
        return Recommendation.SELL_CANDIDATE, reasons, risks

    reasons.append("Below watch threshold; not a candidate")
    return Recommendation.WATCH, reasons, risks
