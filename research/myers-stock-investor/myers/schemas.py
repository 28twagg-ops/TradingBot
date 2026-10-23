from __future__ import annotations

from datetime import date
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class Confidence(str, Enum):
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
    NONE = "NONE"


class Recommendation(str, Enum):
    BUY_CANDIDATE = "BUY_CANDIDATE"
    WATCH = "WATCH"
    HOLD = "HOLD"
    SELL_CANDIDATE = "SELL_CANDIDATE"
    INSUFFICIENT_DATA = "INSUFFICIENT_DATA"
    EXCLUDED = "EXCLUDED"


class MetricValue(BaseModel):
    name: str
    value: float | None = None
    unit: str | None = None
    missing_reason: str | None = None
    source: str | None = None


class CategoryScore(BaseModel):
    name: str
    score: float
    components: dict[str, float] = Field(default_factory=dict)
    notes: list[str] = Field(default_factory=list)


class ValuationResult(BaseModel):
    enterprise_value: float | None = None
    ev_to_ebitda: float | None = None
    ev_to_ebit: float | None = None
    price_to_earnings: float | None = None
    price_to_fcf: float | None = None
    fcf_yield: float | None = None
    fair_value_bear: float | None = None
    fair_value_base: float | None = None
    fair_value_bull: float | None = None
    base_margin_of_safety: float | None = None
    reverse_dcf_implied_growth: float | None = None
    reverse_dcf_interpretation: str | None = None
    assumptions: dict[str, Any] = Field(default_factory=dict)


class CompanyAnalysis(BaseModel):
    ticker: str
    analysis_date: date
    company_name: str | None = None
    sector: str | None = None
    industry: str | None = None
    current_price: float | None = None
    market_cap: float | None = None
    fundamental_score: float
    data_confidence: Confidence
    category_scores: list[CategoryScore] = Field(default_factory=list)
    valuation: ValuationResult = Field(default_factory=ValuationResult)
    recommendation: Recommendation
    major_risks: list[str] = Field(default_factory=list)
    investment_thesis: str = ""
    reasons: list[str] = Field(default_factory=list)
    metrics: dict[str, float | None] = Field(default_factory=dict)
    missing_fields: list[str] = Field(default_factory=list)
    source_references: list[str] = Field(default_factory=list)
    model_version: str = "1.0.0"
    pit_limitation: str = (
        "Fundamentals from yfinance are not fully point-in-time; "
        "prices respect as_of_date, fundamentals may include later restatements."
    )
