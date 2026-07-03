"""
options_strategy_registry.py
================================================================================
Master registry of ~220 options strategy archetypes for grid testing and
historical backtest. Loads/saves YAML; expands category templates into full
catalog.

Usage:
  python simulations/options_strategy_registry.py --write   # emit YAML
  python simulations/options_strategy_registry.py --list    # print summary
  from options_strategy_registry import load_registry, mechanics_dict
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass, field
from pathlib import Path

REGISTRY_PATH = Path(__file__).resolve().parent / "options_strategy_registry.json"

# Strike offset keys shared with options_strategy_grid.py
STRIKE_OFFSETS = {"ATM": 0.0, "OTM1": 0.015, "OTM2": 0.030, "OTM3": 0.050,
                  "ITM1": -0.015, "ITM2": -0.030}


@dataclass
class StrategyDef:
    id: str
    name: str
    category: str
    right: str                    # C or P
    signal: str                   # gap_down, gap_up, volume_spike, ...
    drift: float                  # annualized underlying bias (synthetic sim)
    strike_offset: str = "ATM"
    structure: str = "long_single"
    side: str = "long"            # long | short (premium direction)
    multi_leg: bool = False
    dte_default: int = 7
    filters: dict = field(default_factory=dict)
    notes: str = ""

    @property
    def mechanic_key(self) -> str:
        return f"{self.id}_{self.name.replace(' ', '')[:24]}"


def _s(id_: str, name: str, cat: str, right: str, signal: str, drift: float,
       strike: str = "ATM", structure: str = "long_single", side: str = "long",
       multi_leg: bool = False, dte: int = 7, **filters) -> StrategyDef:
    return StrategyDef(
        id=id_, name=name, category=cat, right=right, signal=signal,
        drift=drift, strike_offset=strike, structure=structure, side=side,
        multi_leg=multi_leg, dte_default=dte, filters=dict(filters),
    )


def build_registry() -> list[StrategyDef]:
    """Build full ~220 strategy catalog from category templates."""
    out: list[StrategyDef] = []

    # --- 1. Directional long premium (20) ---
    long_specs = [
        ("S001", "Long ATM call", "C", "momentum", 0.12, "ATM"),
        ("S002", "Long OTM call 5pct", "C", "momentum", 0.14, "OTM1"),
        ("S003", "Long deep OTM call", "C", "momentum", 0.18, "OTM3"),
        ("S004", "Long ITM call replacement", "C", "momentum", 0.08, "ITM1"),
        ("S005", "Long ATM put", "P", "breakdown", 0.12, "ATM"),
        ("S006", "Long OTM put hedge", "P", "breakdown", 0.14, "OTM1"),
        ("S007", "Long put crash hedge", "P", "breakdown", 0.10, "ATM", 7),
        ("S008", "Long call MA pullback", "C", "pullback_ma", 0.11, "ATM"),
        ("S009", "Long call vol spike uptrend", "C", "volume_spike", 0.15, "ATM"),
        ("S010", "Long put support break", "P", "breakdown", 0.13, "ATM"),
        ("S011", "Long call RSI oversold", "C", "rsi_oversold", 0.12, "ATM"),
        ("S012", "Long put RSI overbought", "P", "rsi_overbought", 0.12, "ATM"),
        ("S013", "Long call MACD bull cross", "C", "macd_bull", 0.11, "ATM"),
        ("S014", "Long put MACD bear cross", "P", "macd_bear", 0.11, "ATM"),
        ("S015", "Long call earnings drift", "C", "earnings_positive", 0.14, "ATM"),
        ("S016", "Long put guidance gap", "P", "earnings_negative", 0.16, "ATM"),
        ("S017", "Long call sector leader", "C", "sector_leader", 0.10, "ATM"),
        ("S018", "Long put sector laggard", "P", "sector_laggard", 0.10, "ATM"),
        ("S019", "Long call 52wk high BO", "C", "high_52w_break", 0.13, "ATM"),
        ("S020", "Long put 52wk low BD", "P", "low_52w_break", 0.13, "ATM"),
    ]
    for row in long_specs:
        dte = row[6] if len(row) > 6 else 7
        out.append(_s(row[0], row[1], "directional_long", row[2], row[3], row[4],
                      row[5], dte=dte))

    # --- 2. Directional short premium (18) ---
    short_specs = [
        ("S021", "Cash secured short put", "P", "support_retest", 0.08, "OTM1", "short_put", "short"),
        ("S022", "Covered short call", "C", "resistance_retest", 0.08, "OTM1", "short_call", "short"),
        ("S023", "Short OTM put high IV", "P", "iv_rank_high", 0.07, "OTM1", "short_put", "short"),
        ("S024", "Short OTM call covered", "C", "iv_rank_high", 0.07, "OTM1", "short_call", "short"),
        ("S025", "Short strangle proxy", "C", "iv_rank_high", 0.05, "OTM2", "short_strangle", "short", True),
        ("S026", "Bull put spread income", "P", "uptrend", 0.09, "OTM1", "bull_put_spread", "short", True),
        ("S027", "Bear call spread income", "C", "downtrend", 0.09, "OTM1", "bear_call_spread", "short", True),
        ("S028", "Short put IV crush post event", "P", "post_event_iv", 0.10, "OTM1", "short_put", "short"),
        ("S029", "Short call failed BO", "C", "failed_breakout", 0.09, "OTM1", "short_call", "short"),
        ("S030", "Short put failed BD", "P", "failed_breakdown", 0.09, "OTM1", "short_put", "short"),
        ("S031", "Short premium IV>80", "P", "iv_rank_high", 0.08, "OTM1", "short_put", "short"),
        ("S032", "Short premium term inverted", "P", "term_inverted", 0.07, "OTM1", "short_put", "short"),
        ("S033", "Short put uptrend", "P", "uptrend", 0.08, "OTM1", "short_put", "short"),
        ("S034", "Short call downtrend", "C", "downtrend", 0.08, "OTM1", "short_call", "short"),
        ("S035", "Short weekly put theta", "P", "uptrend", 0.09, "OTM1", "short_put", "short", False, 7),
        ("S036", "Short monthly call vs stock", "C", "neutral", 0.06, "OTM1", "short_call", "short", False, 30),
        ("S037", "Short put support", "P", "support_retest", 0.08, "OTM1", "short_put", "short"),
        ("S038", "Short call resistance", "C", "resistance_retest", 0.08, "OTM1", "short_call", "short"),
    ]
    for row in short_specs:
        ml = row[8] if len(row) > 8 else False
        dte = row[9] if len(row) > 9 else 7
        out.append(_s(row[0], row[1], "directional_short", row[2], row[3], row[4],
                      row[5], row[6], row[7], ml, dte))

    # --- 3. Vertical debit (16) ---
    debit_specs = [
        ("S039", "Bull call spread debit", "C", "gap_down", 0.14, "ATM", "bull_call_spread", "long", True),
        ("S040", "Bear put spread debit", "P", "gap_up", 0.14, "ATM", "bear_put_spread", "long", True),
        ("S041", "ATM bull call spread", "C", "momentum", 0.12, "ATM", "bull_call_spread", "long", True),
        ("S042", "OTM bull call spread", "C", "momentum", 0.13, "OTM1", "bull_call_spread", "long", True),
        ("S043", "ITM bull call spread", "C", "momentum", 0.10, "ITM1", "bull_call_spread", "long", True),
        ("S044", "Bear put gap continuation", "P", "gap_down_cont", 0.15, "ATM", "bear_put_spread", "long", True),
        ("S045", "Bull call gap fade", "C", "gap_down", 0.16, "ATM", "bull_call_spread", "long", True),
        ("S046", "Debit spread 1to1 RR", "C", "momentum", 0.11, "ATM", "bull_call_spread", "long", True),
        ("S047", "Debit spread 1to2 RR", "C", "momentum", 0.13, "OTM1", "bull_call_spread", "long", True),
        ("S048", "Debit spread 7 DTE", "C", "gap_down", 0.14, "ATM", "bull_call_spread", "long", True, 7),
        ("S049", "Debit spread 14 DTE", "C", "gap_down", 0.12, "ATM", "bull_call_spread", "long", True, 14),
        ("S050", "Debit spread 30 DTE", "C", "momentum", 0.10, "ATM", "bull_call_spread", "long", True, 30),
        ("S051", "Debit spread first hour", "C", "gap_down", 0.15, "ATM", "bull_call_spread", "long", True),
        ("S052", "Debit spread last hour", "C", "power_hour", 0.12, "ATM", "bull_call_spread", "long", True),
        ("S053", "Debit spread high IV", "C", "iv_rank_high", 0.11, "ATM", "bull_call_spread", "long", True),
        ("S054", "Debit spread low IV", "C", "iv_rank_low", 0.13, "ATM", "bull_call_spread", "long", True),
    ]
    for row in debit_specs:
        dte = row[9] if len(row) > 9 else 7
        out.append(_s(row[0], row[1], "vertical_debit", row[2], row[3], row[4],
                      row[5], row[6], row[7], row[8], dte))

    # --- 4. Vertical credit (16) ---
    credit_specs = [
        ("S055", "Bull put spread credit", "P", "uptrend", 0.09, "OTM1", "bull_put_spread", "short", True),
        ("S056", "Bear call spread credit", "C", "downtrend", 0.09, "OTM1", "bear_call_spread", "short", True),
        ("S057", "Credit spread 0.30 delta", "P", "neutral", 0.08, "OTM1", "bull_put_spread", "short", True),
        ("S058", "Credit spread 0.16 delta", "P", "neutral", 0.07, "OTM2", "bull_put_spread", "short", True),
        ("S059", "Credit spread 0.10 delta", "P", "neutral", 0.06, "OTM3", "bull_put_spread", "short", True),
        ("S060", "Credit spread 7 DTE", "P", "uptrend", 0.09, "OTM1", "bull_put_spread", "short", True, 7),
        ("S061", "Credit spread 21 DTE", "P", "uptrend", 0.08, "OTM1", "bull_put_spread", "short", True, 21),
        ("S062", "Credit spread 45 DTE", "P", "uptrend", 0.07, "OTM1", "bull_put_spread", "short", True, 45),
        ("S063", "Credit spread high IV rank", "P", "iv_rank_high", 0.08, "OTM1", "bull_put_spread", "short", True),
        ("S064", "Credit spread elevated skew", "P", "skew_steep", 0.08, "OTM1", "bull_put_spread", "short", True),
        ("S065", "Credit spread roll when tested", "P", "support_retest", 0.07, "OTM1", "bull_put_spread", "short", True),
        ("S066", "Credit spread 50pct profit", "P", "neutral", 0.08, "OTM1", "bull_put_spread", "short", True),
        ("S067", "Credit spread close 21 DTE", "P", "neutral", 0.08, "OTM1", "bull_put_spread", "short", True, 21),
        ("S068", "Credit spread bull regime", "P", "regime_bull", 0.09, "OTM1", "bull_put_spread", "short", True),
        ("S069", "Credit spread low vol regime", "P", "regime_low_vol", 0.08, "OTM1", "bull_put_spread", "short", True),
        ("S070", "Credit spread iron condor lite", "P", "neutral", 0.07, "OTM2", "iron_condor", "short", True),
    ]
    for row in credit_specs:
        dte = row[9] if len(row) > 9 else 7
        out.append(_s(row[0], row[1], "vertical_credit", row[2], row[3], row[4],
                      row[5], row[6], row[7], row[8], dte))

    # --- 5. Straddle/strangle (14) ---
    straddle_specs = [
        ("S071", "Long ATM straddle", "C", "pre_event", 0.06, "ATM", "straddle", "long", True),
        ("S072", "Long OTM strangle", "C", "iv_rank_low", 0.08, "OTM1", "strangle", "long", True),
        ("S073", "Short ATM straddle", "C", "iv_rank_high", 0.05, "ATM", "straddle", "short", True),
        ("S074", "Short OTM strangle wings", "C", "iv_rank_high", 0.06, "OTM1", "strangle", "short", True),
        ("S075", "Long straddle HV<<IV", "C", "iv_vs_hv_low", 0.07, "ATM", "straddle", "long", True),
        ("S076", "Short straddle IV>>HV", "C", "iv_vs_hv_high", 0.05, "ATM", "straddle", "short", True),
        ("S077", "Straddle buy pre earnings", "C", "pre_earnings", 0.08, "ATM", "straddle", "long", True, 3),
        ("S078", "Straddle sell earnings AM", "C", "post_earnings_iv", 0.06, "ATM", "straddle", "short", True, 3),
        ("S079", "Strangle at expected move", "C", "pre_event", 0.07, "OTM1", "strangle", "long", True),
        ("S080", "Strangle outside EM", "C", "pre_event", 0.08, "OTM2", "strangle", "long", True),
        ("S081", "Strip long 2P 1C", "P", "bearish_vol", 0.10, "ATM", "strip", "long", True),
        ("S082", "Strap long 2C 1P", "C", "bullish_vol", 0.10, "ATM", "strap", "long", True),
        ("S083", "Long straddle delta hedge", "C", "pre_event", 0.06, "ATM", "straddle", "long", True),
        ("S084", "Short strangle iron condor", "C", "neutral", 0.05, "OTM2", "iron_condor", "short", True),
    ]
    for row in straddle_specs:
        dte = row[9] if len(row) > 9 else 7
        out.append(_s(row[0], row[1], "straddle_strangle", row[2], row[3], row[4],
                      row[5], row[6], row[7], row[8], dte))

    # --- 6. Iron condor / butterfly (18) ---
    neutral_specs = [
        ("S085", "Iron condor 30-45 DTE", "C", "neutral", 0.05, "OTM2", "iron_condor", "short", True, 30),
        ("S086", "Iron condor weekly", "C", "neutral", 0.06, "OTM2", "iron_condor", "short", True, 7),
        ("S087", "Iron condor 16 delta", "C", "neutral", 0.05, "OTM2", "iron_condor", "short", True),
        ("S088", "Iron condor 10 delta", "C", "neutral", 0.04, "OTM3", "iron_condor", "short", True),
        ("S089", "Iron butterfly ATM", "C", "neutral", 0.05, "ATM", "iron_butterfly", "short", True),
        ("S090", "Reverse iron butterfly", "C", "pre_event", 0.08, "ATM", "iron_butterfly", "long", True),
        ("S091", "Long butterfly pin", "C", "opex_pin", 0.07, "ATM", "butterfly", "long", True),
        ("S092", "Short butterfly range", "C", "neutral", 0.05, "ATM", "butterfly", "short", True),
        ("S093", "Iron condor SPY", "C", "neutral", 0.05, "OTM2", "iron_condor", "short", True, 14),
        ("S094", "Iron condor high IV name", "C", "iv_rank_high", 0.06, "OTM2", "iron_condor", "short", True),
        ("S095", "Iron condor 50pct profit", "C", "neutral", 0.05, "OTM2", "iron_condor", "short", True),
        ("S096", "Iron condor adjust tested", "C", "neutral", 0.05, "OTM2", "iron_condor", "short", True),
        ("S097", "Broken wing butterfly", "C", "neutral", 0.06, "OTM1", "butterfly", "long", True),
        ("S098", "Call butterfly bullish", "C", "momentum", 0.08, "OTM1", "butterfly", "long", True),
        ("S099", "Put butterfly bearish", "P", "breakdown", 0.08, "OTM1", "butterfly", "long", True),
        ("S100", "Double iron condor", "C", "neutral", 0.04, "OTM2", "iron_condor", "short", True, 30),
        ("S101", "Jade lizard", "P", "neutral", 0.07, "OTM1", "jade_lizard", "short", True),
        ("S102", "Big lizard", "P", "neutral", 0.06, "OTM2", "jade_lizard", "short", True),
    ]
    for row in neutral_specs:
        ml = row[8] if len(row) > 8 else False
        dte = row[9] if len(row) > 9 else 7
        out.append(_s(row[0], row[1], "neutral_structures", row[2], row[3], row[4],
                      row[5], row[6], row[7], ml, dte))

    # --- 7. Calendar & diagonal (14) ---
    cal_specs = [
        ("S103", "Long calendar spread", "C", "term_contango", 0.08, "ATM", "calendar", "long", True),
        ("S104", "Short calendar vol expansion", "C", "term_backwardation", 0.07, "ATM", "calendar", "short", True),
        ("S105", "Double calendar", "C", "term_contango", 0.07, "ATM", "calendar", "long", True),
        ("S106", "Diagonal call bull", "C", "uptrend", 0.10, "OTM1", "diagonal", "long", True),
        ("S107", "Diagonal put bear", "P", "downtrend", 0.10, "OTM1", "diagonal", "long", True),
        ("S108", "Calendar ATM same strike", "C", "term_contango", 0.08, "ATM", "calendar", "long", True),
        ("S109", "Calendar OTM directional", "C", "momentum", 0.09, "OTM1", "calendar", "long", True),
        ("S110", "Calendar avoid earnings", "C", "pre_earnings", 0.07, "ATM", "calendar", "long", True),
        ("S111", "Diagonal PMCC", "C", "uptrend", 0.09, "OTM1", "diagonal", "long", True, 30),
        ("S112", "Call calendar low front IV", "C", "iv_rank_low", 0.08, "ATM", "calendar", "long", True),
        ("S113", "Put calendar high front IV", "P", "iv_rank_high", 0.08, "ATM", "calendar", "long", True),
        ("S114", "LEAPS diagonal", "C", "uptrend", 0.08, "ITM1", "diagonal", "long", True, 60),
        ("S115", "Calendar roll forward", "C", "term_contango", 0.07, "ATM", "calendar", "long", True),
        ("S116", "Diagonal roll up out", "C", "momentum", 0.09, "OTM1", "diagonal", "long", True),
    ]
    for row in cal_specs:
        dte = row[9] if len(row) > 9 else 7
        out.append(_s(row[0], row[1], "calendar_diagonal", row[2], row[3], row[4],
                      row[5], row[6], row[7], row[8], dte))

    # --- 8. Ratio & synthetic (12) ---
    ratio_specs = [
        ("S117", "Ratio call spread 1x2", "C", "momentum", 0.11, "ATM", "ratio_call", "long", True),
        ("S118", "Ratio put spread 1x2", "P", "breakdown", 0.11, "ATM", "ratio_put", "long", True),
        ("S119", "Call backspread", "C", "pre_event", 0.12, "OTM1", "backspread", "long", True),
        ("S120", "Put backspread", "P", "pre_event", 0.12, "OTM1", "backspread", "long", True),
        ("S121", "Synthetic long stock", "C", "momentum", 0.10, "ATM", "synthetic", "long", True),
        ("S122", "Synthetic short stock", "P", "breakdown", 0.10, "ATM", "synthetic", "long", True),
        ("S123", "Conversion arb", "C", "neutral", 0.02, "ATM", "conversion", "long", True),
        ("S124", "Box spread arb", "C", "neutral", 0.01, "ATM", "box", "long", True),
        ("S125", "Risk reversal skew", "C", "skew_steep", 0.11, "OTM1", "risk_reversal", "long", True),
        ("S126", "Collar long stock", "P", "neutral", 0.06, "OTM1", "collar", "long", True),
        ("S127", "Zero cost collar", "P", "neutral", 0.06, "OTM1", "collar", "long", True),
        ("S128", "Split strike collar", "P", "neutral", 0.06, "OTM2", "collar", "long", True),
    ]
    for row in ratio_specs:
        out.append(_s(row[0], row[1], "ratio_synthetic", row[2], row[3], row[4],
                      row[5], row[6], row[7], row[8]))

    # --- 9. Volatility & Greeks (20) ---
    vol_specs = [
        ("S129", "Long vol IV rank<20", "C", "iv_rank_low", 0.10, "ATM", "straddle", "long", True),
        ("S130", "Short vol IV rank>80", "P", "iv_rank_high", 0.07, "OTM1", "short_put", "short"),
        ("S131", "IV pct mean rev buy calls", "C", "iv_rank_low", 0.11, "ATM"),
        ("S132", "IV pct expansion straddle", "C", "iv_rank_low", 0.08, "ATM", "straddle", "long", True),
        ("S133", "Vega neutral iron condor", "C", "neutral", 0.05, "OTM2", "iron_condor", "short", True),
        ("S134", "Delta neutral straddle scalp", "C", "pre_event", 0.06, "ATM", "straddle", "long", True),
        ("S135", "Gamma scalping", "C", "pre_event", 0.07, "ATM", "straddle", "long", True),
        ("S136", "Theta harvest short opts", "P", "iv_rank_high", 0.08, "OTM1", "short_put", "short"),
        ("S137", "Charm decay into expiry", "P", "neutral", 0.09, "OTM1", "short_put", "short", False, 1),
        ("S138", "Skew buy put spread", "P", "skew_steep", 0.11, "OTM1", "bear_put_spread", "long", True),
        ("S139", "Put skew steep sell spread", "P", "skew_steep", 0.08, "OTM1", "bull_put_spread", "short", True),
        ("S140", "Call skew steep sell spread", "C", "skew_steep", 0.08, "OTM1", "bear_call_spread", "short", True),
        ("S141", "Term structure calendar vol", "C", "term_contango", 0.08, "ATM", "calendar", "long", True),
        ("S142", "Contango short calendar", "C", "term_contango", 0.07, "ATM", "calendar", "short", True),
        ("S143", "RV>IV long vol", "C", "iv_vs_hv_low", 0.09, "ATM", "straddle", "long", True),
        ("S144", "IV>RV short vol", "P", "iv_vs_hv_high", 0.07, "OTM1", "short_put", "short"),
        ("S145", "VIX call hedge", "C", "crash_hedge", 0.08, "OTM1"),
        ("S146", "VIX put spread mean rev", "P", "vix_high", 0.09, "OTM1", "bear_put_spread", "long", True),
        ("S147", "Beta delta hedge SPY", "C", "neutral", 0.05, "ATM"),
        ("S148", "Vol surface smile trade", "C", "skew_steep", 0.08, "OTM1"),
    ]
    for row in vol_specs:
        strike = row[5] if len(row) > 5 else "ATM"
        struct = row[6] if len(row) > 6 else "long_single"
        side = row[7] if len(row) > 7 else "long"
        ml = row[8] if len(row) > 8 and isinstance(row[8], bool) else (
            struct not in ("long_single", "short_put", "short_call"))
        dte = row[9] if len(row) > 9 else 7
        out.append(_s(row[0], row[1], "volatility_greeks", row[2], row[3], row[4],
                      strike, struct, side, ml, dte))

    # --- 10. Event & seasonality (14) ---
    event_names = [
        ("S149", "Pre-earnings long straddle", "pre_earnings", 0.08, "straddle", True, 3),
        ("S150", "Post-earnings IV crush short", "post_earnings_iv", 0.07, "strangle", True, 3),
        ("S151", "Earnings EM vs actual fade", "post_earnings_iv", 0.08, "straddle", True, 3),
        ("S152", "FDA binary straddle", "pre_event", 0.09, "straddle", True, 7),
        ("S153", "Dividend capture", "ex_div", 0.06, "long_single", False, 14),
        ("S154", "Ex-div short call avoid", "ex_div", 0.07, "short_call", False, 14),
        ("S155", "OPEX gamma pin iron fly", "opex_pin", 0.06, "iron_butterfly", True, 7),
        ("S156", "OPEX vol crush Monday", "opex_pin", 0.07, "short_put", False, 7),
        ("S157", "FOMC straddle", "fomc", 0.08, "straddle", True, 3),
        ("S158", "CPI jobs ORB options", "macro_orb", 0.10, "long_single", False, 1),
        ("S159", "Month-end rebalance", "month_end", 0.07, "long_single", False, 7),
        ("S160", "January effect call skew", "seasonal_jan", 0.08, "long_single", False, 14),
        ("S161", "Tax loss put premium Dec", "seasonal_dec", 0.07, "short_put", False, 30),
        ("S162", "Quad witching reduced size", "opex_pin", 0.06, "iron_condor", True, 7),
    ]
    for eid, name, sig, drift, struct, ml, dte in event_names:
        side = "short" if "short" in struct else "long"
        out.append(_s(eid, name, "event_seasonality", "C", sig, drift, "ATM",
                      struct, side, ml, dte))

    # --- 11. Equity-signal mapped (22) — core bot edge ---
    equity_specs = [
        ("S163", "A1 GapDown ATM call EOD", "C", "gap_down", 0.18, "ATM", "long_single", "long", False, 7),
        ("S164", "GapDown bull call spread", "C", "gap_down", 0.16, "ATM", "bull_call_spread", "long", True, 7),
        ("S165", "GapDown long call 3 DTE", "C", "gap_down", 0.17, "ATM", "long_single", "long", False, 3),
        ("S166", "GapDown strong call", "C", "gap_down_strong", 0.20, "ATM", "long_single", "long", False, 7),
        ("S167", "GapDown weak skip/half", "C", "gap_down_weak", 0.10, "ATM", "long_single", "long", False, 7),
        ("S168", "GapUp long put EOD", "P", "gap_up", 0.18, "ATM", "long_single", "long", False, 7),
        ("S169", "VolumeSpike long call EOD", "C", "volume_spike", 0.15, "ATM", "long_single", "long", False, 7),
        ("S170", "Pullback50 long call 3 DTE", "C", "pullback50", 0.14, "ATM", "long_single", "long", False, 3),
        ("S171", "Pullback50 bull put spread", "P", "pullback50", 0.12, "OTM1", "bull_put_spread", "short", True, 7),
        ("S172", "52wkLow long call 7 DTE", "C", "low_52w", 0.13, "ATM", "long_single", "long", False, 7),
        ("S173", "MomReversal long call", "C", "mom_reversal", 0.14, "ATM", "long_single", "long", False, 1),
        ("S174", "RubberBand long call EOD", "C", "rubber_band", 0.16, "ATM", "long_single", "long", False, 7),
        ("S175", "RSIRecovery long call 3 DTE", "C", "rsi_recovery", 0.13, "ATM", "long_single", "long", False, 3),
        ("S176", "Seasonal calendar match DTE", "C", "seasonal", 0.11, "ATM", "long_single", "long", False, 7),
        ("S177", "Regime bull calls only", "C", "regime_bull", 0.12, "ATM", "long_single", "long", False, 7),
        ("S178", "Regime bear puts only", "P", "regime_bear", 0.12, "ATM", "long_single", "long", False, 7),
        ("S179", "Regime corr reduced size", "C", "regime_corr", 0.08, "ATM", "long_single", "long", False, 7),
        ("S180", "Signal IV rank filter", "C", "gap_down", 0.15, "ATM", "long_single", "long", False, 7),
        ("S181", "Signal low spread filter", "C", "gap_down", 0.16, "ATM", "long_single", "long", False, 7),
        ("S182", "Signal OI filter", "C", "gap_down", 0.16, "ATM", "long_single", "long", False, 7),
        ("S183", "GapDown VolumeSpike confirm", "C", "gap_down_vol", 0.19, "ATM", "long_single", "long", False, 7),
        ("S184", "Fade low vol gap long put", "P", "gap_up_low_vol", 0.14, "ATM", "long_single", "long", False, 7),
    ]
    for row in equity_specs:
        out.append(_s(row[0], row[1], "equity_signal", row[2], row[3], row[4],
                      row[5], row[6], row[7], row[8], row[9]))

    # --- 12. Intraday microstructure (14) ---
    intra_specs = [
        ("S185", "ORB breakout call 15m", "C", "orb_breakout", 0.13),
        ("S186", "ORB breakdown put 15m", "P", "orb_breakdown", 0.13),
        ("S187", "First hour gap fade call", "C", "gap_down", 0.17),
        ("S188", "VWAP reclaim long call", "C", "vwap_reclaim", 0.12),
        ("S189", "VWAP rejection long put", "P", "vwap_reject", 0.14),
        ("S190", "Midday consolidation BO", "C", "midday_breakout", 0.11),
        ("S191", "Power hour momentum call", "C", "power_hour", 0.13),
        ("S192", "Power hour fade put", "P", "power_hour_fade", 0.12),
        ("S193", "10AM reversal call", "C", "ten_am_reversal", 0.14),
        ("S194", "Lunch lull vol sell", "P", "lunch_lull", 0.07, "OTM1", "short_put", "short"),
        ("S195", "Last hour theta short weekly", "P", "power_hour", 0.08, "OTM1", "short_put", "short", False, 1),
        ("S196", "Tick imbalance proxy", "C", "tape_imbalance", 0.10),
        ("S197", "Bid-ask imbalance open", "C", "open_imbalance", 0.11),
        ("S198", "Large opening print follow", "C", "open_print", 0.12),
    ]
    for row in intra_specs:
        if len(row) == 5:
            out.append(_s(row[0], row[1], "intraday", row[2], row[3], row[4]))
        else:
            ml = row[8] if len(row) > 8 else False
            dte = row[9] if len(row) > 9 else 7
            out.append(_s(row[0], row[1], "intraday", row[2], row[3], row[4],
                          row[5], row[6], row[7], ml, dte))

    # --- 13. Flow & sentiment (12) ---
    flow_specs = [
        ("S199", "UOA call sweep follow", "C", "uoa_call", 0.12),
        ("S200", "UOA put sweep follow", "P", "uoa_put", 0.12),
        ("S201", "PCR contrarian bullish", "C", "pcr_high", 0.11),
        ("S202", "PCR contrarian bearish", "P", "pcr_low", 0.11),
        ("S203", "Max pain pin weekly", "C", "max_pain", 0.06, "ATM", "iron_butterfly", "short", True),
        ("S204", "GEX positive fade", "C", "gex_positive", 0.08),
        ("S205", "GEX negative trend follow", "C", "gex_negative", 0.12),
        ("S206", "Dealer delta hedge proxy", "C", "dealer_flow", 0.09),
        ("S207", "OI change breakout", "C", "oi_breakout", 0.11),
        ("S208", "Vol weighted PCR skew", "P", "pcr_skew", 0.10),
        ("S209", "Dark pool print call", "C", "dark_pool", 0.12),
        ("S210", "13F lag overlay", "C", "fundamental_lag", 0.08),
    ]
    for row in flow_specs:
        if len(row) == 5:
            out.append(_s(row[0], row[1], "flow_sentiment", row[2], row[3], row[4]))
        else:
            ml = row[8] if len(row) > 8 else False
            out.append(_s(row[0], row[1], "flow_sentiment", row[2], row[3], row[4],
                          row[5], row[6], row[7], ml))

    # --- 14. Portfolio risk overlays (10) — meta, use gap_down proxy ---
    risk_specs = [
        ("S211", "Fixed 1pct risk per trade", "gap_down", 0.16),
        ("S212", "Kelly half sizing", "gap_down", 0.16),
        ("S213", "Tier0 1 contract 75 max", "gap_down", 0.16),
        ("S214", "Tier1 2pct equity", "gap_down", 0.16),
        ("S215", "Max 3 concurrent", "gap_down", 0.16),
        ("S216", "Max 20pct premium at risk", "gap_down", 0.16),
        ("S217", "Stop minus 50pct premium", "gap_down", 0.16),
        ("S218", "Stop underlying minus 1pct", "gap_down", 0.16),
        ("S219", "Profit take plus 50pct", "gap_down", 0.16),
        ("S220", "Sector correlation cap", "gap_down", 0.16),
    ]
    for eid, name, sig, drift in risk_specs:
        out.append(_s(eid, name, "risk_overlay", "C", sig, drift))

    # Deduplicate by id (vol section may have dupes if we had bugs)
    seen: set[str] = set()
    unique: list[StrategyDef] = []
    for s in out:
        if s.id not in seen:
            seen.add(s.id)
            unique.append(s)

    return unique


def mechanics_dict(strategies: list[StrategyDef] | None = None) -> dict:
    """Convert registry to MECHANICS dict for options_strategy_grid.py."""
    strategies = strategies or load_registry()
    mech: dict = {}
    for s in strategies:
        drift = s.drift if s.side == "long" else s.drift * 0.85
        if s.right == "P" and s.side == "long":
            drift = -abs(drift)
        elif s.right == "C" and s.side == "long":
            drift = abs(drift)
        elif s.right == "P" and s.side == "short":
            drift = abs(drift) * 0.7   # short put wants flat/up
        elif s.right == "C" and s.side == "short":
            drift = -abs(drift) * 0.7
        mech[s.mechanic_key] = {
            "right": s.right,
            "drift": drift,
            "side": s.side,
            "strike_offset": s.strike_offset,
            "signal": s.signal,
            "structure": s.structure,
            "multi_leg": s.multi_leg,
            "strategy_id": s.id,
        }
    return mech


def load_registry(path: Path | None = None) -> list[StrategyDef]:
    path = path or REGISTRY_PATH
    if path.exists():
        raw = json.loads(path.read_text(encoding="utf-8"))
        return [StrategyDef(**row) for row in raw["strategies"]]
    return build_registry()


def save_registry(strategies: list[StrategyDef] | None = None,
                  path: Path | None = None) -> Path:
    path = path or REGISTRY_PATH
    strategies = strategies or build_registry()
    payload = {
        "version": 1,
        "count": len(strategies),
        "strategies": [asdict(s) for s in strategies],
    }
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return path


def main() -> int:
    ap = argparse.ArgumentParser(description="Options strategy registry")
    ap.add_argument("--write", action="store_true", help="write registry JSON/YAML")
    ap.add_argument("--list", action="store_true", help="list strategies")
    args = ap.parse_args()
    strategies = build_registry()
    if args.write:
        p = save_registry(strategies)
        print(f"Wrote {len(strategies)} strategies -> {p}")
    if args.list or not (args.write):
        cats: dict[str, int] = {}
        for s in strategies:
            cats[s.category] = cats.get(s.category, 0) + 1
        print(f"Registry: {len(strategies)} strategies")
        for cat, n in sorted(cats.items()):
            print(f"  {cat}: {n}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
