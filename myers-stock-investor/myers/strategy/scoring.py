from __future__ import annotations

from myers.config import StrategyConfig
from myers.data.fundamentals import Fundamentals
from myers.schemas import CategoryScore, Confidence, ValuationResult


def _clip(x: float, lo: float = 0.0, hi: float = 100.0) -> float:
    return max(lo, min(hi, x))


def _score_cash(metrics: dict[str, float | None], cfg: StrategyConfig) -> CategoryScore:
    comps: dict[str, float] = {}
    notes: list[str] = []
    # FCF margin
    fm = metrics.get("fcf_margin")
    if fm is None:
        comps["fcf_margin"] = 40.0
        notes.append("fcf_margin missing")
    else:
        comps["fcf_margin"] = _clip(fm / 0.15 * 100)  # 15% FCF margin ~100
    # Cash conversion
    cc = metrics.get("cash_conversion")
    if cc is None:
        comps["cash_conversion"] = 40.0
        notes.append("cash_conversion missing")
    else:
        comps["cash_conversion"] = _clip(min(cc, 1.5) / 1.2 * 100)
    # Positive FCF years
    pos = metrics.get("fcf_positive_years")
    need = float(cfg.screening.min_fcf_years_positive)
    if pos is None:
        comps["fcf_consistency"] = 40.0
        notes.append("fcf_history missing")
    else:
        comps["fcf_consistency"] = _clip(pos / max(need, 1) * 80)
    # CCC penalty if stretching
    ccc = metrics.get("ccc")
    if ccc is not None and ccc > 120:
        comps["working_capital"] = 30.0
        notes.append("long cash conversion cycle")
    elif ccc is None:
        comps["working_capital"] = 50.0
    else:
        comps["working_capital"] = _clip(100 - ccc / 2)
    score = sum(comps.values()) / len(comps)
    return CategoryScore(name="cash_quality", score=score, components=comps, notes=notes)


def _score_balance(metrics: dict[str, float | None], cfg: StrategyConfig) -> CategoryScore:
    comps: dict[str, float] = {}
    notes: list[str] = []
    nd = metrics.get("net_debt_to_ebitda")
    if nd is None:
        # Negative EBITDA or missing — do not invent safety
        comps["leverage"] = 35.0
        notes.append("net_debt_to_ebitda missing or undefined")
    elif nd < 0:
        comps["leverage"] = 95.0
    else:
        # 0 -> 100, max_net -> 50, above worse
        max_nd = cfg.screening.max_net_debt_to_ebitda
        comps["leverage"] = _clip(100 - (nd / max_nd) * 50)

    ic = metrics.get("interest_coverage")
    if ic is None:
        comps["interest_coverage"] = 45.0
        notes.append("interest_coverage missing")
    else:
        comps["interest_coverage"] = _clip(min(ic, 15) / 10 * 100)

    cr = metrics.get("current_ratio")
    if cr is None:
        comps["liquidity"] = 45.0
    else:
        comps["liquidity"] = _clip(min(cr, 3) / 2 * 100)

    score = sum(comps.values()) / len(comps)
    return CategoryScore(name="balance_sheet", score=score, components=comps, notes=notes)


def _score_quality(metrics: dict[str, float | None], f: Fundamentals) -> CategoryScore:
    comps: dict[str, float] = {}
    notes: list[str] = []
    om = metrics.get("operating_margin")
    comps["operating_margin"] = 40.0 if om is None else _clip(om / 0.25 * 100)
    gm = metrics.get("gross_margin")
    comps["gross_margin"] = 40.0 if gm is None else _clip(gm / 0.5 * 100)
    g = metrics.get("revenue_cagr_3y")
    if g is None:
        comps["growth"] = 45.0
        notes.append("revenue_cagr_3y missing")
    else:
        comps["growth"] = _clip(50 + g * 200)  # 10% CAGR -> 70
    roic = metrics.get("roic")
    comps["roic"] = 40.0 if roic is None else _clip(roic / 0.15 * 100)
    if f.sector:
        notes.append(f"sector={f.sector}")
    score = sum(comps.values()) / len(comps)
    return CategoryScore(name="business_quality", score=score, components=comps, notes=notes)


def _score_valuation(val: ValuationResult) -> CategoryScore:
    comps: dict[str, float] = {}
    notes: list[str] = []
    mos = val.base_margin_of_safety
    if mos is None:
        comps["margin_of_safety"] = 40.0
        notes.append("DCF margin of safety unavailable")
    else:
        # 25% MOS -> ~80, 0% -> 50, negative -> lower
        comps["margin_of_safety"] = _clip(50 + mos * 120)

    ev = val.ev_to_ebitda
    if ev is None:
        comps["ev_ebitda"] = 40.0
        notes.append("ev_to_ebitda missing")
    else:
        # Prefer ~6-12x; too low may be trap, too high expensive
        if ev <= 0:
            comps["ev_ebitda"] = 20.0
        elif ev < 4:
            comps["ev_ebitda"] = 55.0
            notes.append("very low multiple — check earnings quality")
        elif ev <= 12:
            comps["ev_ebitda"] = _clip(100 - (ev - 6) * 5)
        else:
            comps["ev_ebitda"] = _clip(40 - (ev - 12) * 2)

    fy = val.fcf_yield
    if fy is None:
        comps["fcf_yield"] = 40.0
    else:
        comps["fcf_yield"] = _clip(fy / 0.08 * 100)

    score = sum(comps.values()) / len(comps)
    return CategoryScore(name="valuation", score=score, components=comps, notes=notes)


def _score_mgmt_concentration(f: Fundamentals, metrics: dict[str, float | None]) -> CategoryScore:
    """v1: no filing NLP yet — score neutrally and flag UNKNOWN concentration."""
    comps = {
        "customer_concentration": 50.0,  # UNKNOWN — not treated as safe
        "key_person": 50.0,
        "capital_allocation_proxy": 50.0,
    }
    notes = [
        "customer_concentration=UNKNOWN (requires 10-K extraction)",
        "key_person=UNKNOWN (requires proxy / filing review)",
    ]
    # Mild proxy: dilution / share count not available historically here
    if metrics.get("fcf_yield") is not None and (metrics.get("fcf_yield") or 0) > 0.05:
        comps["capital_allocation_proxy"] = 65.0
        notes.append("positive FCF yield proxy for capital return capacity")
    score = sum(comps.values()) / len(comps)
    return CategoryScore(
        name="management_concentration", score=score, components=comps, notes=notes
    )


def assess_confidence(f: Fundamentals, metrics: dict[str, float | None]) -> Confidence:
    critical = [
        "revenue",
        "free_cash_flow",
        "operating_cash_flow",
        "market_cap",
        "ebitda",
        "total_debt",
        "cash",
    ]
    present = sum(1 for k in critical if metrics.get(k) is not None or getattr(f, k, None) is not None)
    # Also count missing list
    miss = len(f.missing)
    if present >= 6 and miss <= 1:
        return Confidence.HIGH
    if present >= 4 and miss <= 3:
        return Confidence.MEDIUM
    if present >= 2:
        return Confidence.LOW
    return Confidence.NONE


def total_score(
    categories: list[CategoryScore], cfg: StrategyConfig
) -> float:
    w = cfg.scoring_weights
    weight_map = {
        "cash_quality": w.cash_quality,
        "balance_sheet": w.balance_sheet,
        "business_quality": w.business_quality,
        "valuation": w.valuation,
        "management_concentration": w.management_concentration,
    }
    acc = 0.0
    tw = 0.0
    for c in categories:
        wt = weight_map.get(c.name, 0.0)
        acc += c.score * wt
        tw += wt
    return round(acc / tw if tw else 0.0, 2)


def build_category_scores(
    f: Fundamentals,
    metrics: dict[str, float | None],
    val: ValuationResult,
    cfg: StrategyConfig,
) -> list[CategoryScore]:
    return [
        _score_cash(metrics, cfg),
        _score_balance(metrics, cfg),
        _score_quality(metrics, f),
        _score_valuation(val),
        _score_mgmt_concentration(f, metrics),
    ]
