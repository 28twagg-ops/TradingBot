from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass

from myers.config import StrategyConfig


@dataclass(frozen=True)
class StrategyProfile:
    key: str
    name: str
    description: str
    buy_min_score: float
    margin_of_safety_buy: float
    ranking_mode: bool = False
    reference_mode: bool = False


PROFILES: dict[str, StrategyProfile] = {
    "conservative_acquirer": StrategyProfile(
        key="conservative_acquirer",
        name="Strategy A — Conservative Acquirer",
        description="Score≥70, MOS≥25%, strong cash/leverage gates.",
        buy_min_score=70,
        margin_of_safety_buy=0.25,
    ),
    "balanced_value": StrategyProfile(
        key="balanced_value",
        name="Strategy B — Balanced Value",
        description="Score≥70, MOS≥15%.",
        buy_min_score=70,
        margin_of_safety_buy=0.15,
    ),
    "quality_fair_value": StrategyProfile(
        key="quality_fair_value",
        name="Strategy C — Quality at Fair Value",
        description="Score≥80, MOS≥0%.",
        buy_min_score=80,
        margin_of_safety_buy=0.0,
    ),
    "deep_value": StrategyProfile(
        key="deep_value",
        name="Strategy D — Deep Value",
        description="Score≥60, MOS≥30%, distress exclusions remain.",
        buy_min_score=60,
        margin_of_safety_buy=0.30,
    ),
    "quality_value_ranking": StrategyProfile(
        key="quality_value_ranking",
        name="Strategy E — Quality/Value Ranking",
        description="Rank by score+MOS; soft floors score≥55, MOS≥5%.",
        buy_min_score=55,
        margin_of_safety_buy=0.05,
        ranking_mode=True,
    ),
    "simple_reference": StrategyProfile(
        key="simple_reference",
        name="Strategy F — Simple Reference",
        description="Equal-weight top liquid names each rebalance (no MOS filter).",
        buy_min_score=0,
        margin_of_safety_buy=-1.0,
        reference_mode=True,
    ),
}


def resolve_profile(name: str | None) -> StrategyProfile:
    if not name:
        return PROFILES["conservative_acquirer"]
    key = name.strip().lower().replace(" ", "_").replace("-", "_")
    aliases = {
        "a": "conservative_acquirer",
        "conservative": "conservative_acquirer",
        "b": "balanced_value",
        "balanced": "balanced_value",
        "c": "quality_fair_value",
        "quality": "quality_fair_value",
        "d": "deep_value",
        "deep": "deep_value",
        "e": "quality_value_ranking",
        "ranking": "quality_value_ranking",
        "f": "simple_reference",
        "reference": "simple_reference",
    }
    key = aliases.get(key, key)
    if key not in PROFILES:
        raise ValueError(f"Unknown profile {name!r}. Choose from {list(PROFILES)}")
    return PROFILES[key]


def config_for_profile(cfg: StrategyConfig, profile: StrategyProfile) -> StrategyConfig:
    data = deepcopy(cfg.model_dump())
    data["signals"]["buy_min_score"] = profile.buy_min_score
    data["valuation"]["margin_of_safety_buy"] = profile.margin_of_safety_buy
    return StrategyConfig.model_validate(data)
