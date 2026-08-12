"""
options_lab.py — Virtual $500-bucket experiment grid for the paper options bot.

Each bucket is an independent experiment cell with its own BUY and SELL rules.
The same signal can fire in every active bucket (different limits, stops, sizing).

    active_buckets = len(BUCKET_EXPERIMENTS) when OPTIONS_PAPER_UNLIMITED=1 (default)
                   else min(len(BUCKET_EXPERIMENTS), floor(equity / 500))

Each bucket uses a fixed $500 virtual equity (OPTIONS_VIRTUAL_BUCKET_USD).

Tracking (the hard part):
  - Every order tagged:  LB<bucket>|<strategy>|<YYYYMMDD>  (entry)
                         LX<bucket>|<strategy>|<lot_id>     (exit)
  - lab_state.json holds virtual lots with lot_id + bucket_id
  - reconcile_with_broker() syncs lots vs Alpaca positions each run
  - lab_ledger.csv is the long-term audit trail

Edit BUCKET_EXPERIMENTS below to add buy/sell/stop variants.
"""

from __future__ import annotations

import csv
import itertools
import json
import logging
import os
import re
import time
import uuid
from dataclasses import asdict, dataclass, field, fields
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from statistics import mean, median
from typing import Any

log = logging.getLogger(__name__)

# Each bucket is a fixed $500 virtual experiment cell (paper treats equity as unlimited).
VIRTUAL_BUCKET_USD = float(os.environ.get("OPTIONS_VIRTUAL_BUCKET_USD", "500"))
# When 1 (default), all defined profiles run regardless of broker equity.
PAPER_UNLIMITED_BUCKETS = os.environ.get("OPTIONS_PAPER_UNLIMITED", "1") != "0"
TARGET_BUCKET_PROFILES = int(os.environ.get("OPTIONS_BUCKET_COUNT", "100"))
CONTROLLED_LAYOUT = os.environ.get("OPTIONS_CONTROLLED_LAYOUT", "0") == "1"
STATE_VERSION = 5

ORPHAN_BUCKET_ID = 0
ORPHAN_PROFILE = "orphan_reconcile"
ORPHAN_STRATEGY = "ORPHAN"

# Strategies paused from new entries (layout buckets stay for audit).
# Reflected P&L / leaderboard exclude these by default.
DROPPED_STRATEGIES: frozenset[str] = frozenset(
    s.strip() for s in os.environ.get("OPTIONS_DROPPED_STRATEGIES", "S174,S173").split(",")
    if s.strip()
)
ORDER_FETCH_LIMIT = 500


def get_lab_account_safe(client, retries=3, wait=10):
    """Retry wrapper for Alpaca get_account (mirrors rubber_band / morning_bot)."""
    for i in range(retries):
        try:
            return client.get_account()
        except Exception as e:
            if i < retries - 1:
                log.warning(
                    "lab get_account failed attempt %s/%s: %s", i + 1, retries, e
                )
                time.sleep(wait)
            else:
                log.error("lab get_account failed after %s attempts: %s", retries, e)
                raise

REPO_ROOT = Path(__file__).resolve().parent.parent
TRIAL_ROOT = REPO_ROOT / "logs" / "options_trial"
STATE_PATH = TRIAL_ROOT / "_state" / "lab_state.json"
LEDGER_PATH = TRIAL_ROOT / "_ledger" / "master_ledger.csv"
BUCKETS_PATH = TRIAL_ROOT / "_state" / "lab_buckets.json"
STRATEGIES_PATH = TRIAL_ROOT / "_state" / "strategies.json"

# Legacy path (pre-trial folder split)
_LEGACY_STATE = REPO_ROOT / "logs" / "options" / "lab_state.json"

_LEDGER_FIELDS = [
    "ts", "event", "bucket_id", "profile", "strategy_id", "lot_id",
    "symbol", "occ", "qty", "limit", "fill_price", "cost",
    "return_pct", "pnl_usd", "reason", "buy_offset", "sell_offset",
    "take_profit", "stop_loss", "spread_frac", "detail", "order_id",
]


@dataclass
class BucketProfile:
    """Execution experiment for one virtual $500 bucket."""
    bucket_id: int
    name: str
    # --- BUY ---
    buy_limit_offset: float = -0.01   # from ask (negative = below ask); 0 = at ask
    buy_at_mid: bool = False          # if True, limit = mid instead of ask+offset
    max_premium: float = 75.0
    max_spread_frac: float = 0.25
    min_open_interest: int = 100
    account_cap: float = 0.20         # max fraction of $500 in open option premium
    max_contracts: int = 1
    # --- SELL ---
    sell_limit_offset: float = -0.01  # from bid (negative = below bid)
    sell_at_mid: bool = False
    take_profit: float = 0.50
    stop_loss: float = -0.50
    eod_only: bool = False            # skip intraday stops; exit at EOD only
    market_exit_eod: bool = True      # use market order after EOD_MARKET if limit fails
    # --- Controlled experiment controls ---
    strategy_scope: str = "all"       # "all" or one strategy id (e.g. S173)
    buy_start_hm: str = "09:28"
    buy_end_hm: str = "11:35"
    option_type: str = "call"
    strike_offset: int = 0
    dte_target: int = 3
    dte_min: int = 1
    dte_max: int = 7


# Experiment grid — generated up to TARGET_BUCKET_PROFILES variants.
def _build_bucket_experiments(target: int | None = None) -> list[BucketProfile]:
    n = target if target is not None else TARGET_BUCKET_PROFILES
    n = max(8, min(n, 5000))  # raised cap from 200 to 5000 for 100+ strategy framework

    if CONTROLLED_LAYOUT:
        try:
            from scripts.options_strategy_lab import load_or_init_lab
        except ImportError:
            from options_strategy_lab import load_or_init_lab
        lab = load_or_init_lab()
        bucket_dicts = lab.generate_buckets(start_idx=0)
        profiles: list[BucketProfile] = []
        for d in bucket_dicts:
            if len(profiles) >= n:
                break
            profiles.append(BucketProfile(**d))
        return profiles

    core = [
        BucketProfile(0, "baseline",
                      buy_limit_offset=-0.01, sell_limit_offset=-0.01,
                      max_premium=75, account_cap=0.95,
                      take_profit=0.50, stop_loss=-0.50),
        BucketProfile(1, "patient_buy",
                      buy_limit_offset=-0.05, sell_limit_offset=-0.01,
                      max_premium=60, account_cap=0.95,
                      take_profit=0.45, stop_loss=-0.40),
        BucketProfile(2, "aggressive_buy",
                      buy_at_mid=True, sell_limit_offset=-0.02,
                      max_premium=90, account_cap=0.95,
                      take_profit=0.55, stop_loss=-0.45),
        BucketProfile(3, "tight_stops",
                      buy_limit_offset=-0.01, sell_limit_offset=-0.01,
                      max_premium=50, account_cap=0.95,
                      take_profit=0.30, stop_loss=-0.25),
        BucketProfile(4, "wide_stops",
                      buy_limit_offset=-0.02, sell_limit_offset=-0.02,
                      max_premium=80, account_cap=0.95,
                      take_profit=0.80, stop_loss=-0.60),
        BucketProfile(5, "eod_only",
                      buy_limit_offset=-0.01, sell_limit_offset=-0.01,
                      max_premium=75, account_cap=0.95,
                      eod_only=True, take_profit=0.99, stop_loss=-0.99),
        BucketProfile(6, "loose_spread",
                      buy_limit_offset=-0.01, max_spread_frac=0.35,
                      max_premium=70, account_cap=0.95,
                      take_profit=0.50, stop_loss=-0.50),
        BucketProfile(7, "tight_spread",
                      buy_limit_offset=-0.01, max_spread_frac=0.15,
                      max_premium=65, account_cap=0.95,
                      take_profit=0.40, stop_loss=-0.35),
    ]
    if n <= len(core):
        return core[:n]

    buy_offs = [-0.10, -0.08, -0.05, -0.03, -0.02, -0.01, 0.0]
    sell_offs = [-0.05, -0.03, -0.02, -0.01, 0.0]
    tps = [0.20, 0.30, 0.40, 0.50, 0.60, 0.75, 0.90]
    sls = [-0.20, -0.30, -0.40, -0.50, -0.65]
    spreads = [0.12, 0.18, 0.25, 0.32]
    profiles = list(core)
    seen = {(
        p.buy_limit_offset, p.sell_limit_offset, p.take_profit, p.stop_loss,
        p.max_spread_frac, p.buy_at_mid, p.eod_only,
    ) for p in core}

    for buy, sell, tp, sl, spread in itertools.product(
            buy_offs, sell_offs, tps, sls, spreads):
        if len(profiles) >= n:
            break
        for buy_mid, eod in ((False, False), (True, False), (False, True)):
            if len(profiles) >= n:
                break
            key = (buy, sell, tp, sl, spread, buy_mid, eod)
            if key in seen:
                continue
            seen.add(key)
            idx = len(profiles)
            tag = "mid" if buy_mid else ("eod" if eod else "lim")
            name = f"g{idx:03d}_{tag}_tp{int(tp * 100)}_sl{int(abs(sl) * 100)}"
            profiles.append(BucketProfile(
                idx, name,
                buy_limit_offset=buy,
                buy_at_mid=buy_mid,
                sell_limit_offset=sell,
                max_spread_frac=spread,
                max_premium=90,
                account_cap=0.95,
                take_profit=tp,
                stop_loss=sl,
                eod_only=eod,
            ))
    return profiles[:n]


BUCKET_EXPERIMENTS: list[BucketProfile] = _build_bucket_experiments()


def experiment_layout_id() -> str:
    mode = "controlled" if CONTROLLED_LAYOUT else "grid"
    head = BUCKET_EXPERIMENTS[0].name if BUCKET_EXPERIMENTS else "none"
    return f"{mode}:{len(BUCKET_EXPERIMENTS)}:{head}"

# Per-strategy tweaks layered on top of bucket profile (signal-specific narrowing).
STRATEGY_TWEAKS: dict[str, dict[str, Any]] = {
    "S173": {"max_premium": 100, "account_cap": 0.25, "take_profit": 0.60, "stop_loss": -0.40},
    "S174": {},
    "S165": {"max_premium": 50, "account_cap": 0.15, "take_profit": 0.35, "stop_loss": -0.30},
    "S164": {},
    "S167": {},
    "S168": {},
    "S166": {"max_premium": 80, "take_profit": 0.70},
    "S163": {},
    "S169": {},
    "S170": {},
    "S171": {},
    "S172": {},
    "S175": {},
}

# Active paper strategies mirrored into strategies.json (S173/S174 stay dropped).
ACTIVE_PAPER_STRATEGY_IDS = [
    "S163", "S164", "S165", "S166", "S167", "S168",
    "S169", "S170", "S171", "S172", "S175",
]


def build_controlled_layout(target: int | None = None) -> list[BucketProfile]:
    """Return controlled-layout bucket profiles (audit / regression helper)."""
    return _build_bucket_experiments(target)

@dataclass
class EffectiveArm:
    """Merged bucket + strategy experiment for one trade."""
    bucket_id: int
    profile_name: str
    strategy_id: str
    virtual_equity: float = VIRTUAL_BUCKET_USD
    buy_limit_offset: float = -0.01
    buy_at_mid: bool = False
    max_premium: float = 75.0
    max_spread_frac: float = 0.25
    min_open_interest: int = 100
    account_cap: float = 0.20
    max_contracts: int = 1
    sell_limit_offset: float = -0.01
    sell_at_mid: bool = False
    take_profit: float = 0.50
    stop_loss: float = -0.50
    eod_only: bool = False
    market_exit_eod: bool = True
    strategy_scope: str = "all"
    buy_start_hm: str = "09:28"
    buy_end_hm: str = "11:35"
    option_type: str = "call"
    strike_offset: int = 0
    dte_target: int = 3
    dte_min: int = 1
    dte_max: int = 7

    @property
    def bucket_key(self) -> str:
        return f"b{self.bucket_id}"


@dataclass
class VirtualLot:
    lot_id: str
    bucket_id: int
    profile_name: str
    strategy_id: str
    occ_symbol: str
    underlying: str
    qty: int
    entry_cost: float = 0.0
    entry_price: float = 0.0          # per-share premium at fill
    buy_limit_offset: float = -0.01
    sell_limit_offset: float = -0.01
    sell_at_mid: bool = False
    take_profit: float = 0.50
    stop_loss: float = -0.50
    eod_only: bool = False
    market_exit_eod: bool = True
    entry_date: str = ""
    entry_order_id: str = ""


@dataclass
class PendingOrder:
    order_id: str
    bucket_id: int
    strategy_id: str
    occ_symbol: str
    underlying: str
    qty: int
    limit: float
    profile_name: str
    submitted: str = ""
    detail: str = ""
    spread_frac: float = 0.0
    buy_offset: float = -0.01
    take_profit: float = 0.50
    stop_loss: float = -0.50


@dataclass
class PendingExit:
    order_id: str
    lot_id: str
    bucket_id: int
    strategy_id: str
    occ_symbol: str
    qty: int
    reason: str = ""
    submitted: str = ""


def _norm_order_field(val: Any) -> str:
    """Normalize Alpaca enum/string fields (str(OrderStatus.FILLED) != 'filled')."""
    if val is None:
        return ""
    if hasattr(val, "value"):
        try:
            return str(val.value).lower()
        except Exception:
            pass
    s = str(val).lower()
    if "." in s:
        s = s.rsplit(".", 1)[-1]
    return s


@dataclass
class LabState:
    version: int = STATE_VERSION
    lots: list[VirtualLot] = field(default_factory=list)
    pending_orders: list[PendingOrder] = field(default_factory=list)
    pending_exits: list[PendingExit] = field(default_factory=list)
    bucket_open_premium: dict[str, float] = field(default_factory=dict)
    session_date: str = ""
    entries_locked: list[str] = field(default_factory=list)
    processed_orders: list[str] = field(default_factory=list)
    submitted_today: int = 0
    layout_id: str = ""

    def open_premium_for_bucket(self, bucket_id: int) -> float:
        return float(self.bucket_open_premium.get(f"b{bucket_id}", 0.0))

    def lots_for_occ(self, occ: str) -> list[VirtualLot]:
        return [l for l in self.lots if l.occ_symbol == occ and l.qty > 0]

    def bucket_has_strategy(self, bucket_id: int, strategy_id: str) -> bool:
        return any(l.bucket_id == bucket_id and l.strategy_id == strategy_id and l.qty > 0
                   for l in self.lots)

    def bucket_holds_underlying(self, bucket_id: int, underlying: str) -> bool:
        return any(l.bucket_id == bucket_id and l.underlying == underlying and l.qty > 0
                   for l in self.lots)

    def pending_for_bucket_strategy(self, bucket_id: int, strategy_id: str) -> bool:
        return any(p.bucket_id == bucket_id and p.strategy_id == strategy_id
                   for p in self.pending_orders)

    def pending_for_bucket_underlying(self, bucket_id: int, underlying: str) -> bool:
        return any(p.bucket_id == bucket_id and p.underlying == underlying
                   for p in self.pending_orders)

    def pending_exit_for_occ(self, occ: str) -> bool:
        return any(p.occ_symbol == occ for p in self.pending_exits)

    def pending_exit_for_lot(self, lot_id: str) -> bool:
        return any(p.lot_id == lot_id for p in self.pending_exits)

    def entry_slot_locked(self, bucket_id: int, strategy_id: str) -> bool:
        return entry_slot_key(bucket_id, strategy_id) in self.entries_locked

    def order_already_logged(self, order_id: str) -> bool:
        return str(order_id) in self.processed_orders


def entry_slot_key(bucket_id: int, strategy_id: str,
                   day: date | None = None) -> str:
    return f"{bucket_id}|{strategy_id}|{(day or date.today()).isoformat()}"


def rollover_session(state: LabState) -> None:
    today = date.today().isoformat()
    if state.session_date != today:
        state.session_date = today
        state.entries_locked = []
        state.submitted_today = 0


def lock_entry_slot(state: LabState, bucket_id: int, strategy_id: str) -> None:
    key = entry_slot_key(bucket_id, strategy_id)
    if key not in state.entries_locked:
        state.entries_locked.append(key)


def parse_exit_client_order_id(cid: str) -> dict[str, Any] | None:
    if not cid:
        return None
    m = re.match(r"^LX(\d+)\|([^|]+)\|([a-f0-9]{6})", cid, re.I)
    if not m:
        return None
    return {
        "side": "exit",
        "bucket_id": int(m.group(1)),
        "strategy_id": m.group(2),
        "lot_short": m.group(3).lower(),
    }


def find_lot_by_short_id(state: LabState, lot_short: str) -> VirtualLot | None:
    for lot in state.lots:
        compact = lot.lot_id.replace("-", "").lower()
        if compact.startswith(lot_short.lower()):
            return lot
    for lot in state.lots:
        if lot.lot_id.lower().startswith(lot_short.lower()):
            return lot
    return None


def mark_order_logged(state: LabState, order_id: str) -> None:
    oid = str(order_id)
    if oid and oid not in state.processed_orders:
        state.processed_orders.append(oid)
    # keep list bounded
    if len(state.processed_orders) > 500:
        state.processed_orders = state.processed_orders[-400:]


def append_entry_ledger_from_fill(
    state: LabState,
    lot: VirtualLot,
    pending: PendingOrder | None,
    *,
    order_id: str,
    fill_price: float,
    entry_cost: float,
    ts: str | None = None,
) -> None:
    if state.order_already_logged(order_id):
        return
    append_ledger({
        "ts": ts or datetime.now().isoformat(),
        "event": "entry",
        "bucket_id": lot.bucket_id,
        "profile": lot.profile_name,
        "strategy_id": lot.strategy_id,
        "lot_id": lot.lot_id,
        "symbol": lot.underlying,
        "occ": lot.occ_symbol,
        "qty": lot.qty,
        "limit": pending.limit if pending else lot.entry_price,
        "fill_price": round(fill_price, 4),
        "cost": round(entry_cost, 2),
        "buy_offset": pending.buy_offset if pending else lot.buy_limit_offset,
        "take_profit": pending.take_profit if pending else lot.take_profit,
        "stop_loss": pending.stop_loss if pending else lot.stop_loss,
        "spread_frac": pending.spread_frac if pending else "",
        "detail": pending.detail if pending else "",
        "order_id": order_id,
    })
    mark_order_logged(state, order_id)


def append_exit_ledger_from_fill(
    state: LabState,
    lot: VirtualLot,
    *,
    order_id: str,
    qty: int,
    fill_price: float,
    return_pct: float,
    reason: str,
    ts: str | None = None,
) -> None:
    if state.order_already_logged(order_id):
        return
    cost_sold = lot.entry_cost * (qty / lot.qty) if lot.qty else lot.entry_cost
    pnl_usd = cost_sold * return_pct / 100.0
    append_ledger({
        "ts": ts or datetime.now().isoformat(),
        "event": "exit",
        "bucket_id": lot.bucket_id,
        "profile": lot.profile_name,
        "strategy_id": lot.strategy_id,
        "lot_id": lot.lot_id,
        "symbol": lot.underlying,
        "occ": lot.occ_symbol,
        "qty": qty,
        "fill_price": round(fill_price, 4),
        "cost": round(cost_sold, 2),
        "return_pct": round(return_pct, 2),
        "pnl_usd": round(pnl_usd, 2),
        "reason": reason,
        "sell_offset": lot.sell_limit_offset,
        "take_profit": lot.take_profit,
        "stop_loss": lot.stop_loss,
        "order_id": order_id,
    })
    mark_order_logged(state, order_id)
    register_exit(state, lot, qty)


def trial_root() -> Path:
    return TRIAL_ROOT


def bucket_dir(bucket_id: int, profile_name: str) -> Path:
    slug = f"b{bucket_id}_{profile_name}"
    return TRIAL_ROOT / "buckets" / slug


def ensure_trial_layout() -> None:
    """Create options_trial tree (separate from rubber_band logs/)."""
    for sub in ("_state", "_ledger", "runs", "buckets", "simulations", "reports"):
        (TRIAL_ROOT / sub).mkdir(parents=True, exist_ok=True)
    for b in BUCKET_EXPERIMENTS:
        d = bucket_dir(b.bucket_id, b.name)
        d.mkdir(parents=True, exist_ok=True)
        profile_path = d / "profile.json"
        if not profile_path.exists():
            profile_path.write_text(
                json.dumps(asdict(b), indent=2), encoding="utf-8"
            )
        readme = d / "README.txt"
        if not readme.exists():
            readme.write_text(
                f"Bucket b{b.bucket_id} ({b.name}) — virtual ${VIRTUAL_BUCKET_USD:.0f}\n"
                f"  ledger.csv      — this bucket's trades only\n"
                f"  profile.json    — frozen experiment parameters\n"
                f"  summary.md      — auto-generated stats (options_lab_report.py)\n",
                encoding="utf-8",
            )
    if not STRATEGIES_PATH.exists():
        STRATEGIES_PATH.write_text(json.dumps({
            "paper_strategies": list(ACTIVE_PAPER_STRATEGY_IDS),
            "dropped_strategies": sorted(DROPPED_STRATEGIES),
            "strategy_tweaks": STRATEGY_TWEAKS,
        }, indent=2), encoding="utf-8")
    else:
        # Keep on-disk selection in sync when strategies are paused.
        try:
            raw = json.loads(STRATEGIES_PATH.read_text(encoding="utf-8"))
        except Exception:
            raw = {}
        raw["paper_strategies"] = list(ACTIVE_PAPER_STRATEGY_IDS)
        raw["dropped_strategies"] = sorted(DROPPED_STRATEGIES)
        STRATEGIES_PATH.write_text(json.dumps(raw, indent=2), encoding="utf-8")


def _merge_arm(bucket: BucketProfile, strategy_id: str,
               equity: float = VIRTUAL_BUCKET_USD) -> EffectiveArm:
    tweaks = {} if CONTROLLED_LAYOUT else STRATEGY_TWEAKS.get(strategy_id, {})
    vals = {f.name: getattr(bucket, f.name) for f in fields(BucketProfile)
            if f.name not in ("bucket_id", "name")}
    for k, v in tweaks.items():
        if k in vals:
            vals[k] = v
    ve = VIRTUAL_BUCKET_USD
    vals["max_premium"] = min(float(vals["max_premium"]), ve * vals["account_cap"])
    return EffectiveArm(
        bucket_id=bucket.bucket_id,
        profile_name=bucket.name,
        strategy_id=strategy_id,
        virtual_equity=ve,
        **vals,
    )


def active_bucket_count(equity: float) -> int:
    if PAPER_UNLIMITED_BUCKETS:
        return len(BUCKET_EXPERIMENTS)
    if equity <= 0:
        return 1
    funded = max(1, int(equity // VIRTUAL_BUCKET_USD))
    return min(funded, len(BUCKET_EXPERIMENTS))


def bucket_virtual_equity(equity: float = 0) -> float:
    return VIRTUAL_BUCKET_USD


def active_buckets(equity: float) -> list[BucketProfile]:
    return BUCKET_EXPERIMENTS[:active_bucket_count(equity)]


def arms_for_signal(strategy_id: str, equity: float) -> list[EffectiveArm]:
    if strategy_id in DROPPED_STRATEGIES:
        return []
    return [
        _merge_arm(b, strategy_id, equity)
        for b in active_buckets(equity)
        if b.strategy_scope in ("all", strategy_id)
        and b.strategy_scope not in DROPPED_STRATEGIES
    ]


def size_for_arm(arm: EffectiveArm, state: LabState, contract_cost: float) -> int:
    cap = arm.account_cap * arm.virtual_equity
    headroom = cap - state.open_premium_for_bucket(arm.bucket_id)
    if contract_cost <= 0 or headroom < contract_cost:
        return 0
    affordable = int(headroom // contract_cost)
    return max(0, min(arm.max_contracts, affordable))


def entry_limit_price(arm: EffectiveArm, bid: float, ask: float, mid: float) -> float:
    if arm.buy_at_mid:
        return round(max(0.01, mid), 2)
    return round(max(0.01, ask + arm.buy_limit_offset), 2)


def exit_limit_price(lot: VirtualLot, bid: float, ask: float, mid: float) -> float:
    if lot.sell_at_mid:
        return round(max(0.01, mid), 2)
    return round(max(0.01, bid + lot.sell_limit_offset), 2)


def make_entry_client_order_id(bucket_id: int, strategy_id: str,
                               today: date | None = None) -> str:
    d = (today or date.today()).strftime("%Y%m%d")
    # Alpaca enforces uniqueness on client_order_id. Keep stable prefix for
    # grouping, but append a short nonce so repeated retries/signals don't clash.
    nonce = uuid.uuid4().hex[:6]
    return f"LB{bucket_id}|{strategy_id}|{d}|{nonce}"[:48]


def make_exit_client_order_id(bucket_id: int, strategy_id: str, lot_id: str) -> str:
    short = lot_id.replace("-", "")[:6]
    return f"LX{bucket_id}|{strategy_id}|{short}"[:48]


def make_protective_stop_client_order_id(bucket_id: int, strategy_id: str,
                                         lot_id: str) -> str:
    """Broker-resting stop that survives GitHub/bot downtime (LS… prefix)."""
    short = lot_id.replace("-", "")[:6]
    return f"LS{bucket_id}|{strategy_id}|{short}"[:48]


def is_protective_stop_client_order_id(cid: str | None) -> bool:
    return bool(cid) and str(cid).startswith("LS")


def parse_lab_client_order_id(cid: str) -> dict[str, Any] | None:
    if not cid:
        return None
    m = re.match(r"^L([BXS])(\d+)\|([^|]+)\|", cid)
    if not m:
        return None
    kind = {"B": "entry", "X": "exit", "S": "protective_stop"}[m.group(1)]
    return {
        "side": kind,
        "bucket_id": int(m.group(2)),
        "strategy_id": m.group(3),
    }


def _rebuild_bucket_premium(state: LabState) -> None:
    prem: dict[str, float] = {}
    for lot in state.lots:
        if lot.qty <= 0:
            continue
        k = f"b{lot.bucket_id}"
        prem[k] = prem.get(k, 0.0) + lot.entry_cost
    state.bucket_open_premium = prem


def load_state() -> LabState:
    ensure_trial_layout()
    path = STATE_PATH
    if not path.exists() and _LEGACY_STATE.exists():
        path = _LEGACY_STATE
    if not path.exists():
        return LabState()
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
        lots = [VirtualLot(**x) for x in raw.get("lots", [])]
        pending = [PendingOrder(**x) for x in raw.get("pending_orders", [])]
        pending_exits = []
        for x in raw.get("pending_exits", []):
            try:
                pending_exits.append(PendingExit(**{
                    k: x[k] for k in (
                        "order_id", "lot_id", "bucket_id", "strategy_id",
                        "occ_symbol", "qty", "reason", "submitted",
                    ) if k in x
                }))
            except Exception:
                continue
        st = LabState(
            version=raw.get("version", 1),
            lots=lots,
            pending_orders=pending,
            pending_exits=pending_exits,
            bucket_open_premium=raw.get("bucket_open_premium", {}),
            session_date=raw.get("session_date", ""),
            entries_locked=list(raw.get("entries_locked", [])),
            processed_orders=list(raw.get("processed_orders", [])),
            submitted_today=int(raw.get("submitted_today", 0) or 0),
            layout_id=str(raw.get("layout_id", "") or ""),
        )
        rollover_session(st)
        sync_state_layout(st)
        _rebuild_bucket_premium(st)
        return st
    except Exception:
        return LabState()


def save_state(state: LabState) -> None:
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    _rebuild_bucket_premium(state)
    payload = {
        "version": STATE_VERSION,
        "lots": [asdict(l) for l in state.lots if l.qty > 0],
        "pending_orders": [asdict(p) for p in state.pending_orders],
        "pending_exits": [asdict(p) for p in state.pending_exits],
        "bucket_open_premium": state.bucket_open_premium,
        "session_date": state.session_date or date.today().isoformat(),
        "entries_locked": list(state.entries_locked),
        "processed_orders": list(state.processed_orders),
        "submitted_today": state.submitted_today,
        "layout_id": state.layout_id or experiment_layout_id(),
        "updated": date.today().isoformat(),
    }
    STATE_PATH.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    _write_buckets_snapshot(state)


def _write_buckets_snapshot(state: LabState) -> None:
    """Human-readable bucket summary for monitoring."""
    rows = []
    for b in BUCKET_EXPERIMENTS:
        rows.append({
            "bucket_id": b.bucket_id,
            "profile": b.name,
            "open_premium": round(state.open_premium_for_bucket(b.bucket_id), 2),
            "open_lots": sum(1 for l in state.lots if l.bucket_id == b.bucket_id and l.qty > 0),
        })
    BUCKETS_PATH.parent.mkdir(parents=True, exist_ok=True)
    BUCKETS_PATH.write_text(json.dumps(rows, indent=2), encoding="utf-8")


def new_lot_id() -> str:
    return uuid.uuid4().hex[:12]


def sync_state_layout(state: LabState) -> str | None:
    """Record experiment layout changes without wiping open lots."""
    current = experiment_layout_id()
    if state.layout_id and state.layout_id != current:
        return f"layout changed {state.layout_id} -> {current}"
    state.layout_id = current
    return None


def count_filled_entries_today(rows: list[dict] | None = None) -> int:
    today = date.today().isoformat()
    if rows is None:
        rows = _read_ledger_rows()
    n = 0
    for r in rows:
        if r.get("event") != "entry":
            continue
        ts = str(r.get("ts", ""))
        if ts.startswith(today) or str(r.get("date", "")) == today:
            n += 1
    return n


def reconcile_summary(state: LabState, positions: list[dict] | None) -> dict[str, Any]:
    """Lightweight stats for console summary."""
    open_lots = sum(1 for l in state.lots if l.qty > 0)
    orphan_lots = sum(
        1 for l in state.lots
        if l.qty > 0 and l.strategy_id == ORPHAN_STRATEGY
    )
    broker_n = len(positions or [])
    lot_qty = sum(l.qty for l in state.lots if l.qty > 0)
    broker_qty = sum(int(p.get("qty", 0) or 0) for p in (positions or []))
    unattributed = max(0, broker_qty - lot_qty)
    rows = _read_ledger_rows()
    return {
        "open_lots": open_lots,
        "orphan_lots": orphan_lots,
        "broker_positions": broker_n,
        "broker_contracts": broker_qty,
        "virtual_contracts": lot_qty,
        "unattributed_contracts": unattributed,
        "pending_orders": len(state.pending_orders),
        "pending_exits": len(state.pending_exits),
        "submitted_today": state.submitted_today,
        "filled_today": count_filled_entries_today(rows),
    }


def register_pending(state: LabState, arm: EffectiveArm, occ: str, underlying: str,
                     qty: int, limit: float, order_id: str, *,
                     detail: str = "", spread_frac: float = 0.0) -> None:
    state.pending_orders = [
        p for p in state.pending_orders
        if not (p.bucket_id == arm.bucket_id and p.strategy_id == arm.strategy_id)
    ]
    state.pending_orders.append(PendingOrder(
        order_id=str(order_id),
        bucket_id=arm.bucket_id,
        strategy_id=arm.strategy_id,
        occ_symbol=occ,
        underlying=underlying,
        qty=qty,
        limit=limit,
        profile_name=arm.profile_name,
        submitted=date.today().isoformat(),
        detail=detail,
        spread_frac=spread_frac,
        buy_offset=arm.buy_limit_offset,
        take_profit=arm.take_profit,
        stop_loss=arm.stop_loss,
    ))
    state.submitted_today += 1
    save_state(state)


def confirm_fill(state: LabState, arm: EffectiveArm, occ: str, underlying: str,
                 qty: int, entry_cost: float, entry_price: float,
                 order_id: str = "") -> VirtualLot:
    """Move pending order to confirmed virtual lot."""
    state.pending_orders = [
        p for p in state.pending_orders
        if not (p.order_id == order_id or (
            p.bucket_id == arm.bucket_id and p.strategy_id == arm.strategy_id
            and p.occ_symbol == occ and p.qty == qty
        ))
    ]
    lot = VirtualLot(
        lot_id=new_lot_id(),
        bucket_id=arm.bucket_id,
        profile_name=arm.profile_name,
        strategy_id=arm.strategy_id,
        occ_symbol=occ,
        underlying=underlying,
        qty=qty,
        entry_cost=entry_cost,
        entry_price=entry_price,
        buy_limit_offset=arm.buy_limit_offset,
        sell_limit_offset=arm.sell_limit_offset,
        sell_at_mid=arm.sell_at_mid,
        take_profit=arm.take_profit,
        stop_loss=arm.stop_loss,
        eod_only=arm.eod_only,
        market_exit_eod=arm.market_exit_eod,
        entry_date=datetime.now(timezone.utc).isoformat(),
        entry_order_id=order_id,
    )
    state.lots.append(lot)
    save_state(state)
    return lot


def register_entry_immediate(state: LabState, arm: EffectiveArm, occ: str,
                             underlying: str, qty: int, entry_cost: float,
                             entry_price: float, order_id: str = "") -> VirtualLot:
    """Deprecated: use register_pending + reconcile confirm_fill."""
    return confirm_fill(state, arm, occ, underlying, qty, entry_cost, entry_price, order_id)


def clear_pending_for_order(state: LabState, order_id: str) -> PendingOrder | None:
    found = None
    keep = []
    for p in state.pending_orders:
        if p.order_id == str(order_id):
            found = p
        else:
            keep.append(p)
    state.pending_orders = keep
    return found


def cancel_unfilled_lab_entries(trade, log_fn=None) -> int:
    """Cancel open LAB-tagged entry (buy) orders."""
    from alpaca.trading.requests import GetOrdersRequest
    from alpaca.trading.enums import QueryOrderStatus

    n = 0
    try:
        req = GetOrdersRequest(status=QueryOrderStatus.OPEN, limit=200)
        for o in trade.get_orders(req):
            cid = getattr(o, "client_order_id", "") or ""
            side = _norm_order_field(getattr(o, "side", ""))
            if not cid.startswith("LB") or side != "buy":
                continue
            try:
                trade.cancel_order_by_id(o.id)
                n += 1
            except Exception as exc:
                if log_fn:
                    log_fn(f"  cancel unfilled entry failed {cid}: {exc}")
    except Exception as exc:
        if log_fn:
            log_fn(f"  cancel unfilled entries list failed: {exc}")
    return n


def cancel_dropped_strategy_entries(trade, log_fn=None) -> int:
    """Cancel open buy orders tagged to DROPPED_STRATEGIES (no new entries)."""
    from alpaca.trading.requests import GetOrdersRequest
    from alpaca.trading.enums import QueryOrderStatus

    if not DROPPED_STRATEGIES:
        return 0
    n = 0
    try:
        req = GetOrdersRequest(status=QueryOrderStatus.OPEN, limit=200)
        for o in trade.get_orders(req):
            cid = getattr(o, "client_order_id", "") or ""
            side = _norm_order_field(getattr(o, "side", ""))
            if not cid.startswith("LB") or side != "buy":
                continue
            parsed = parse_lab_client_order_id(cid)
            if not parsed or parsed.get("strategy_id") not in DROPPED_STRATEGIES:
                continue
            try:
                trade.cancel_order_by_id(o.id)
                n += 1
                if log_fn:
                    log_fn(f"  cancel dropped entry {cid}")
            except Exception as exc:
                if log_fn:
                    log_fn(f"  cancel dropped entry failed {cid}: {exc}")
    except Exception as exc:
        if log_fn:
            log_fn(f"  cancel dropped entries list failed: {exc}")
    return n

def open_lab_entry_order_ids(trade) -> set[str]:
    """Return client_order_id prefixes bucket|strategy for open LAB buys."""
    from alpaca.trading.requests import GetOrdersRequest
    from alpaca.trading.enums import QueryOrderStatus

    out: set[str] = set()
    try:
        req = GetOrdersRequest(status=QueryOrderStatus.OPEN, limit=200)
        for o in trade.get_orders(req):
            cid = getattr(o, "client_order_id", "") or ""
            side = _norm_order_field(getattr(o, "side", ""))
            if cid.startswith("LB") and side == "buy":
                out.add(cid)
    except Exception:
        pass
    return out


def has_open_lab_entry(trade, bucket_id: int, strategy_id: str) -> bool:
    prefix = f"LB{bucket_id}|{strategy_id}|"
    return any(cid.startswith(prefix) for cid in open_lab_entry_order_ids(trade))


def register_exit(state: LabState, lot: VirtualLot, qty: int) -> None:
    if lot.qty <= qty:
        lot.qty = 0
    else:
        freed_frac = qty / lot.qty if lot.qty else 1.0
        lot.entry_cost *= (1 - freed_frac)
        lot.qty -= qty
    state.lots = [l for l in state.lots if l.qty > 0]
    save_state(state)


def register_pending_exit(
    state: LabState,
    lot: VirtualLot,
    order_id: str,
    qty: int,
    reason: str,
) -> None:
    state.pending_exits = [
        p for p in state.pending_exits
        if p.order_id != order_id and p.lot_id != lot.lot_id
    ]
    state.pending_exits.append(PendingExit(
        order_id=str(order_id),
        lot_id=lot.lot_id,
        bucket_id=lot.bucket_id,
        strategy_id=lot.strategy_id,
        occ_symbol=lot.occ_symbol,
        qty=qty,
        reason=reason,
        submitted=datetime.now().isoformat(timespec="seconds"),
    ))
    save_state(state)


def clear_pending_exit(state: LabState, order_id: str) -> None:
    oid = str(order_id)
    state.pending_exits = [p for p in state.pending_exits if p.order_id != oid]


def open_option_sell_symbols(trade, *, include_protective_stops: bool = True) -> set[str]:
    """OCC symbols with an open broker sell (avoid double-sell / uncovered).

    Protective stops use client_order_id prefix LS… and can be excluded so the
    bot can still submit take-profit / EOD exits (after canceling the stop).
    """
    from alpaca.trading.requests import GetOrdersRequest
    from alpaca.trading.enums import QueryOrderStatus

    occ_re = re.compile(r"^[A-Z]+\d{6}[CP]\d{8}$")
    out: set[str] = set()
    try:
        orders = list(trade.get_orders(
            GetOrdersRequest(status=QueryOrderStatus.OPEN, limit=ORDER_FETCH_LIMIT)
        ) or [])
    except Exception:
        return out
    for o in orders:
        if _norm_order_field(getattr(o, "side", "")) != "sell":
            continue
        cid = getattr(o, "client_order_id", "") or ""
        if not include_protective_stops and is_protective_stop_client_order_id(cid):
            continue
        sym = getattr(o, "symbol", "") or ""
        if occ_re.match(sym):
            out.add(sym)
    return out


def cancel_protective_stops_for_occ(trade, occ: str, log_fn=None) -> int:
    """Cancel resting LS… protective stops for one OCC before placing an exit."""
    from alpaca.trading.requests import GetOrdersRequest
    from alpaca.trading.enums import QueryOrderStatus

    n = 0
    try:
        orders = list(trade.get_orders(
            GetOrdersRequest(status=QueryOrderStatus.OPEN, symbols=[occ],
                             limit=ORDER_FETCH_LIMIT)
        ) or [])
    except Exception as exc:
        if log_fn:
            log_fn(f"  cancel protective list failed {occ}: {exc}")
        return 0
    for o in orders:
        cid = getattr(o, "client_order_id", "") or ""
        if not is_protective_stop_client_order_id(cid):
            continue
        if _norm_order_field(getattr(o, "side", "")) != "sell":
            continue
        try:
            trade.cancel_order_by_id(o.id)
            n += 1
            if log_fn:
                log_fn(f"  cancelled protective stop {occ} id={o.id}")
        except Exception as exc:
            if log_fn:
                log_fn(f"  cancel protective failed {occ}: {exc}")
    return n


def exit_reason_for_lot(lot: VirtualLot, plpc: float, eod: bool) -> str | None:
    if eod:
        try:
            # Check if option expires today
            pfx = lot.occ_symbol.replace(lot.underlying, "")
            exp_date = date(int("20" + pfx[:2]), int(pfx[2:4]), int(pfx[4:6]))
            if exp_date <= date.today() and lot.market_exit_eod:
                return "EOD"
        except Exception:
            pass

    if lot.eod_only and not eod:
        return None

    if plpc >= lot.take_profit:
        return f"take_profit ({plpc * 100:+.1f}%)"
    if plpc <= lot.stop_loss:
        return f"stop_loss ({plpc * 100:+.1f}%)"
    return None


def append_ledger(row: dict) -> None:
    ensure_trial_layout()
    LEDGER_PATH.parent.mkdir(parents=True, exist_ok=True)
    hdr = not LEDGER_PATH.exists()
    out = {k: row.get(k, "") for k in _LEDGER_FIELDS}
    with open(LEDGER_PATH, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=_LEDGER_FIELDS, extrasaction="ignore")
        if hdr:
            w.writeheader()
        w.writerow(out)
    bid = row.get("bucket_id", "")
    profile = row.get("profile", "")
    if bid != "" and profile:
        bpath = bucket_dir(int(bid), str(profile)) / "ledger.csv"
        bpath.parent.mkdir(parents=True, exist_ok=True)
        hdr_b = not bpath.exists()
        with open(bpath, "a", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=_LEDGER_FIELDS, extrasaction="ignore")
            if hdr_b:
                w.writeheader()
            w.writerow(out)


def _read_ledger_rows() -> list[dict]:
    if not LEDGER_PATH.exists():
        return []
    with open(LEDGER_PATH, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def _ledger_realized_pnl(
    rows: list[dict],
    *,
    exclude_strategies: set[str] | frozenset[str] | None = None,
) -> tuple[float, float, dict[str, float]]:
    """Return (all_time_usd, today_usd, per_bucket_key_usd) from closed trades."""
    today = date.today().isoformat()
    excl = set(exclude_strategies or ())
    lots: dict[str, dict] = {}
    realized_all = 0.0
    realized_today = 0.0
    by_bucket: dict[str, float] = {}

    for r in rows:
        ev = r.get("event")
        lot_id = r.get("lot_id") or ""
        if ev == "entry" and lot_id:
            try:
                lots[lot_id] = {
                    "cost": float(r.get("cost") or 0),
                    "qty": max(1, int(float(r.get("qty") or 1))),
                    "bucket_id": r.get("bucket_id", ""),
                    "profile": r.get("profile", ""),
                }
            except (TypeError, ValueError):
                pass
            continue
        if ev != "exit" or not lot_id:
            continue
        sid = str(r.get("strategy_id") or "")
        if sid and sid in excl:
            continue

        pnl: float | None = None
        if r.get("pnl_usd"):
            try:
                pnl = float(r["pnl_usd"])
            except (TypeError, ValueError):
                pnl = None
        if pnl is None:
            lot = lots.get(lot_id)
            if lot and r.get("return_pct"):
                try:
                    exit_qty = max(1, int(float(r.get("qty") or lot["qty"])))
                    entry_qty = lot["qty"] or exit_qty
                    cost_sold = lot["cost"] * (exit_qty / entry_qty)
                    pnl = cost_sold * float(r["return_pct"]) / 100.0
                    if exit_qty >= entry_qty:
                        lots.pop(lot_id, None)
                    else:
                        lot["cost"] -= cost_sold
                        lot["qty"] -= exit_qty
                except (TypeError, ValueError, ZeroDivisionError):
                    pnl = None

        if pnl is None:
            continue
        realized_all += pnl
        if str(r.get("ts", "")).startswith(today) or str(r.get("date", "")) == today:
            realized_today += pnl
        key = f"b{r.get('bucket_id', '?')}|{r.get('profile', '?')}"
        by_bucket[key] = by_bucket.get(key, 0.0) + pnl

    return realized_all, realized_today, by_bucket


def _open_pnl_stats(
    state: LabState,
    positions: list[dict] | None,
) -> tuple[float, float, float, dict[str, float]]:
    """
    Return (virtual_open_pnl_usd, premium_deployed_usd, broker_open_pnl_usd,
            per_bucket_open_usd).
    Virtual open P&L attributes broker unrealized P&L to lots by entry_cost share.
    """
    by_bucket: dict[str, float] = {}
    premium = 0.0
    virtual_open = 0.0

    if not positions:
        for lot in state.lots:
            if lot.qty <= 0:
                continue
            premium += lot.entry_cost
        return virtual_open, premium, 0.0, by_bucket

    occ_map = {p.get("symbol", ""): p for p in positions}
    broker_open = sum(float(p.get("unrealized_pl", 0) or 0) for p in positions)

    for lot in state.lots:
        if lot.qty <= 0:
            continue
        premium += lot.entry_cost
        pos = occ_map.get(lot.occ_symbol)
        if pos:
            lot_pnl = float(pos.get("unrealized_pl", 0) or 0)
            pos_cost = abs(float(pos.get("cost_basis", 0) or 0))
            if pos_cost > 0 and lot.entry_cost < pos_cost:
                lot_pnl *= lot.entry_cost / pos_cost
            elif pos.get("plpc") is not None:
                lot_pnl = lot.entry_cost * float(pos["plpc"])
        else:
            lot_pnl = 0.0
        virtual_open += lot_pnl
        key = f"b{lot.bucket_id}|{lot.profile_name}"
        by_bucket[key] = by_bucket.get(key, 0.0) + lot_pnl

    return virtual_open, premium, broker_open, by_bucket


def max_active_buckets(equity: float) -> int:
    if PAPER_UNLIMITED_BUCKETS:
        return len(BUCKET_EXPERIMENTS)
    if equity <= 0:
        return 1
    return max(1, int(equity // VIRTUAL_BUCKET_USD))


def _stats_compact() -> bool:
    """Default quiet logs; set OPTIONS_BOT_VERBOSE=1 for full bucket detail."""
    return os.getenv("OPTIONS_BOT_VERBOSE", "").strip().lower() not in (
        "1", "true", "yes",
    )


def _exits_for_date(rows: list[dict], day: str) -> list[dict]:
    """Ledger exit rows for a calendar day (ISO date string)."""
    out = []
    for r in rows:
        if r.get("event") != "exit":
            continue
        ts = str(r.get("ts", ""))
        if ts.startswith(day) or str(r.get("date", "")) == day:
            out.append(r)
    out.sort(key=lambda r: r.get("ts", ""))
    return out


def _exit_pnl_for_row(r: dict, lots_cache: dict | None = None) -> float | None:
    """USD P&L for one exit row (matches _ledger_realized_pnl logic)."""
    if r.get("pnl_usd"):
        try:
            return float(r["pnl_usd"])
        except (TypeError, ValueError):
            pass
    lot_id = r.get("lot_id") or ""
    if not lot_id or not r.get("return_pct"):
        return None
    try:
        ret = float(r["return_pct"])
    except (TypeError, ValueError):
        return None
    try:
        exit_qty = max(1, int(float(r.get("qty") or 1)))
    except (TypeError, ValueError):
        exit_qty = 1
    cost = None
    if lots_cache and lot_id in lots_cache:
        lot = lots_cache[lot_id]
        entry_qty = lot.get("qty") or 1
        cost = lot.get("cost") or 0
        cost_sold = cost * (exit_qty / entry_qty) if entry_qty else cost
        return cost_sold * ret / 100.0
    try:
        cost = float(r.get("cost") or 0)
        return cost * ret / 100.0
    except (TypeError, ValueError):
        return None


def format_exit_summary(
    state: LabState,
    equity: float | None = None,
    positions: list[dict] | None = None,
    *,
    for_date: date | None = None,
    compact: bool = True,
) -> list[str]:
    """
    After-hours / end-of-day digest: closed trades, rollups, top buckets.
    Designed for clean console output when the bot is idle.
    """
    day = (for_date or date.today()).isoformat()
    rows = _read_ledger_rows()
    exits = _exits_for_date(rows, day)
    _, realized_day, realized_by_bucket = _ledger_realized_pnl(
        rows, exclude_strategies=DROPPED_STRATEGIES)

    lines: list[str] = []
    lines.append("=" * 56)
    lines.append(f"OPTIONS EXIT SUMMARY — {day}")
    lines.append("=" * 56)

    if equity is not None:
        lines.append(f"Account equity: ${equity:,.2f}")
    open_virtual, open_premium, broker_open, _ = _open_pnl_stats(state, positions)
    if positions is not None and positions:
        lines.append(f"Open broker positions: {len(positions)}  "
                     f"unrealized ${broker_open:+,.2f}")
    elif open_premium > 0:
        lines.append(f"Virtual open premium: ${open_premium:,.2f}  "
                     f"unrealized ${open_virtual:+,.2f}")
    else:
        lines.append("Open positions: flat")

    lines.append("")
    if not exits:
        lines.append("No closed trades today.")
        lines.append("=" * 56)
        return lines

    rets: list[float] = []
    pnls: list[float] = []
    lots_cache: dict[str, dict] = {}
    for r in rows:
        if r.get("event") == "entry" and r.get("lot_id"):
            try:
                lots_cache[r["lot_id"]] = {
                    "cost": float(r.get("cost") or 0),
                    "qty": max(1, int(float(r.get("qty") or 1))),
                }
            except (TypeError, ValueError):
                pass

    for r in exits:
        if r.get("return_pct"):
            try:
                rets.append(float(r["return_pct"]))
            except (TypeError, ValueError):
                pass
        p = _exit_pnl_for_row(r, lots_cache)
        if p is not None:
            pnls.append(p)

    wins = sum(1 for x in rets if x > 0)
    lines.append("Today's closed trades")
    lines.append(f"  Count:     {len(exits)}")
    if rets:
        lines.append(f"  Win rate:  {wins}/{len(rets)} ({wins/len(rets):.0%})")
        lines.append(f"  Return:    avg {sum(rets)/len(rets):+.1f}%  "
                     f"med {sorted(rets)[len(rets)//2]:+.1f}%  "
                     f"best {max(rets):+.1f}%  worst {min(rets):+.1f}%")
    lines.append(f"  Realized:  ${realized_day:+,.2f}")

    by_strat: dict[str, list[float]] = {}
    by_reason: dict[str, int] = {}
    by_sym: dict[str, list[float]] = {}
    for r in exits:
        sid = r.get("strategy_id") or "?"
        if r.get("return_pct"):
            try:
                by_strat.setdefault(sid, []).append(float(r["return_pct"]))
            except (TypeError, ValueError):
                pass
        sym = r.get("symbol") or "?"
        if r.get("return_pct"):
            try:
                by_sym.setdefault(sym, []).append(float(r["return_pct"]))
            except (TypeError, ValueError):
                pass
        reason = r.get("reason") or "?"
        if reason.startswith("take_profit"):
            key = "take_profit"
        elif reason.startswith("stop_loss"):
            key = "stop_loss"
        elif reason == "EOD":
            key = "EOD"
        else:
            key = reason
        by_reason[key] = by_reason.get(key, 0) + 1

    lines.append("")
    lines.append("By strategy")
    for sid in sorted(by_strat):
        vals = by_strat[sid]
        w = sum(1 for x in vals if x > 0)
        lines.append(f"  {sid:6s}  n={len(vals):3d}  win={w/len(vals):.0%}  "
                     f"avg={sum(vals)/len(vals):+.1f}%")

    lines.append("")
    lines.append("By symbol")
    for sym in sorted(by_sym, key=lambda s: -len(by_sym[s])):
        vals = by_sym[sym]
        lines.append(f"  {sym:6s}  n={len(vals):3d}  avg={sum(vals)/len(vals):+.1f}%")

    lines.append("")
    lines.append("By exit type")
    for key in ("take_profit", "EOD", "stop_loss"):
        if key in by_reason:
            lines.append(f"  {key:12s}  {by_reason[key]}")
    for key, n in sorted(by_reason.items()):
        if key not in ("take_profit", "EOD", "stop_loss"):
            lines.append(f"  {key:12s}  {n}")

    day_bucket: dict[str, float] = {}
    for r in exits:
        p = _exit_pnl_for_row(r, lots_cache)
        if p is None:
            continue
        key = f"b{r.get('bucket_id', '?')}|{r.get('profile', '?')}"
        day_bucket[key] = day_bucket.get(key, 0.0) + p

    if day_bucket:
        lines.append("")
        lines.append("Top buckets today (realized $)")
        ranked = sorted(day_bucket.items(), key=lambda kv: kv[1], reverse=True)
        show = ranked[:5] if compact else ranked[:15]
        for key, pnl in show:
            lines.append(f"  {key:28s}  ${pnl:+,.2f}")
        if compact and len(ranked) > 5:
            lines.append(f"  ({len(ranked) - 5} more bucket profiles with exits)")

    lines.append("")
    show_n = 8 if compact else len(exits)
    lines.append(f"Recent exits (last {min(show_n, len(exits))})")
    for r in exits[-show_n:]:
        ts = str(r.get("ts", ""))
        tm = ts[11:19] if len(ts) >= 19 else "--:--:--"
        try:
            ret = float(r["return_pct"])
            ret_s = f"{ret:+.1f}%"
        except (TypeError, ValueError):
            ret_s = "  n/a"
        p = _exit_pnl_for_row(r, lots_cache)
        pnl_s = f"${p:+,.2f}" if p is not None else "n/a"
        reason = (r.get("reason") or "")[:28]
        lines.append(
            f"  {tm}  b{r.get('bucket_id', '?'):>2} {str(r.get('profile', ''))[:18]:18s}  "
            f"{r.get('symbol', '?'):5s} {r.get('strategy_id', '?'):5s}  "
            f"{ret_s:>7s}  {pnl_s:>9s}  {reason}"
        )

    orphan_pnl = day_bucket.get("b0|orphan_reconcile", 0.0)
    if abs(orphan_pnl) > 0.01:
        lines.append("")
        lines.append(
            f"Note: ${orphan_pnl:+,.2f} realized in orphan_reconcile "
            f"(virtual/broker tracking drift — not a bucket profile)."
        )

    lines.append("=" * 56)
    return lines


def print_exit_summary(
    state: LabState,
    equity: float | None = None,
    positions: list[dict] | None = None,
    *,
    file_fn=None,
    console_fn=None,
    for_date: date | None = None,
    compact: bool = True,
) -> None:
    lines = format_exit_summary(
        state, equity, positions, for_date=for_date, compact=compact)
    if file_fn is None and console_fn is None:
        for line in lines:
            print(line, flush=True)
        return
    if file_fn:
        for line in lines:
            file_fn(line)
    if console_fn:
        for line in lines:
            console_fn(line)


def format_trial_stats(
    state: LabState,
    equity: float | None = None,
    positions: list[dict] | None = None,
    *,
    compact: bool | None = None,
) -> list[str]:
    """Human-readable stats block for terminal + run log."""
    if compact is None:
        compact = _stats_compact()
    today = date.today().isoformat()
    lines: list[str] = []
    lines.append("=" * 56)
    lines.append("OPTIONS TRIAL STATS")
    lines.append("=" * 56)

    if equity is not None:
        nb = active_bucket_count(equity)
        fundable = max_active_buckets(equity)
        lines.append(f"Account equity: ${equity:,.2f}")
        lines.append(
            f"Active buckets: {nb} of {len(BUCKET_EXPERIMENTS)} profiles "
            f"(${VIRTUAL_BUCKET_USD:,.0f} virtual each)"
            + (" — paper unlimited mode" if PAPER_UNLIMITED_BUCKETS else "")
        )
        if not PAPER_UNLIMITED_BUCKETS and fundable < len(BUCKET_EXPERIMENTS):
            lines.append(
                f"  Note: equity funds {fundable} x ${VIRTUAL_BUCKET_USD:.0f} buckets; "
                f"set OPTIONS_PAPER_UNLIMITED=1 to run all profiles."
            )
    else:
        nb = len(BUCKET_EXPERIMENTS)
        lines.append("Account equity: (not connected)")

    rows = _read_ledger_rows()
    realized_raw, realized_today_raw, _ = _ledger_realized_pnl(rows)
    realized_all, realized_today, realized_by_bucket = _ledger_realized_pnl(
        rows, exclude_strategies=DROPPED_STRATEGIES)
    open_virtual, open_premium, broker_open, open_by_bucket = _open_pnl_stats(
        state, positions)

    drop_tag = ",".join(sorted(DROPPED_STRATEGIES)) if DROPPED_STRATEGIES else ""
    lines.append("")
    lines.append("P&L summary")
    if drop_tag:
        lines.append(
            f"  Reflected (ex-{drop_tag}): ${realized_all:+,.2f} all-time"
            f"  |  ${realized_today:+,.2f} today"
        )
        lines.append(
            f"  Raw (incl dropped):     ${realized_raw:+,.2f} all-time"
            f"  |  ${realized_today_raw:+,.2f} today"
        )
    else:
        lines.append(f"  Realized (sold):     ${realized_all:+,.2f} all-time"
                     f"  |  ${realized_today:+,.2f} today")
    if positions is not None:
        lines.append(
            f"  Open (not sold yet): ${open_virtual:+,.2f} unrealized (virtual lots)"
        )
        if broker_open and abs(broker_open - open_virtual) > 0.01:
            lines.append(
                f"                       ${broker_open:+,.2f} unrealized (broker total)"
            )
    else:
        lines.append("  Open (not sold yet): (connect broker for live unrealized P&L)")
    lines.append(f"  Premium deployed:    ${open_premium:,.2f} in open positions")
    lines.append(
        f"  Combined P&L:        ${realized_all + open_virtual:+,.2f} "
        f"(reflected realized + open virtual)"
    )

    today_rows = [r for r in rows if str(r.get("ts", "")).startswith(today)
                  or str(r.get("date", "")) == today]
    entries_today = sum(1 for r in today_rows if r.get("event") == "entry")
    exits_today = sum(
        1 for r in today_rows
        if r.get("event") == "exit"
        and str(r.get("strategy_id") or "") not in DROPPED_STRATEGIES
    )
    all_exits = [
        r for r in rows
        if r.get("event") == "exit" and r.get("return_pct")
        and str(r.get("strategy_id") or "") not in DROPPED_STRATEGIES
    ]
    rets = []
    for r in all_exits:
        try:
            rets.append(float(r["return_pct"]))
        except Exception:
            pass

    lines.append("")
    lines.append("Ledger (master)")
    lines.append(f"  Total events:     {len(rows)}")
    lines.append(f"  Today entries:    {entries_today}")
    lines.append(f"  Today exits (reflected): {exits_today}")
    if rets:
        wins = sum(1 for x in rets if x > 0)
        lines.append(f"  All-time exits (reflected): {len(rets)}  wins {wins/len(rets):.0%}")
        lines.append(f"  Avg return/trade: {sum(rets)/len(rets):+.1f}%  "
                     f"median {sorted(rets)[len(rets)//2]:+.1f}%")
    else:
        lines.append("  All-time exits (reflected): 0 (no completed trades yet)")

    lines.append("")
    lines.append("Open virtual lots (by bucket)")
    any_lot = False
    active_profiles = BUCKET_EXPERIMENTS[:nb if equity else len(BUCKET_EXPERIMENTS)]
    max_shown = 5 if compact else 20
    active_rows: list[tuple] = []
    quiet = 0
    for b in active_profiles:
        blots = [l for l in state.lots if l.bucket_id == b.bucket_id and l.qty > 0]
        prem = state.open_premium_for_bucket(b.bucket_id)
        bkey = f"b{b.bucket_id}|{b.name}"
        rpnl = realized_by_bucket.get(bkey, 0.0)
        opnl = open_by_bucket.get(bkey, 0.0)
        has_activity = bool(blots or prem > 0 or rpnl or opnl)
        if has_activity:
            any_lot = True
            active_rows.append((b, blots, prem, rpnl, opnl))
        else:
            quiet += 1
    if compact and active_rows:
        active_rows.sort(key=lambda row: abs(row[4]), reverse=True)
    shown = 0
    for b, blots, prem, rpnl, opnl in active_rows:
        if shown >= max_shown:
            break
        shown += 1
        lot_detail = ", ".join(
            f"{l.strategy_id}:{l.underlying}x{l.qty}" for l in blots[:4]
        )
        if len(blots) > 4:
            lot_detail += f" +{len(blots)-4} more"
        lines.append(
            f"  b{b.bucket_id} {b.name:22s}  prem=${prem:6.0f}  "
            f"real=${rpnl:+6.2f}  open=${opnl:+6.2f}  "
            f"lots={len(blots)}  [{lot_detail or '-'}]"
        )
        if not compact:
            lines.append(
                f"       buy: {'mid' if b.buy_at_mid else f'ask{b.buy_limit_offset:+.2f}'}  "
                f"sell: bid{b.sell_limit_offset:+.2f}  "
                f"tp={b.take_profit:+.0%} sl={b.stop_loss:+.0%}"
            )
    omitted = len(active_rows) - shown
    if omitted:
        lines.append(f"  ({omitted} more active bucket(s) omitted)")
    if quiet:
        lines.append(f"  ({quiet} quiet bucket profile(s) — no trades yet)")
    if not any_lot:
        lines.append("  (no open lots across active profiles)")

    if state.pending_orders:
        lines.append("")
        lines.append(f"Pending orders: {len(state.pending_orders)}")
        for p in state.pending_orders[:5]:
            lines.append(
                f"  b{p.bucket_id} {p.strategy_id} {p.underlying} "
                f"limit={p.limit:.2f}"
            )

    if positions is not None:
        lines.append("")
        lines.append("Alpaca option positions")
        if positions:
            for pos in positions:
                sym = pos.get("symbol", "?")
                qty = pos.get("qty", 0)
                plpc = pos.get("plpc", 0.0)
                upl = float(pos.get("unrealized_pl", 0) or 0)
                cost = float(pos.get("cost_basis", 0) or 0)
                lines.append(
                    f"  {sym}  qty={qty}  cost=${cost:,.2f}  "
                    f"return={plpc*100:+.1f}%  open P&L=${upl:+,.2f}"
                )
        else:
            lines.append("  (none)")

    if rows and all_exits:
        lines.append("")
        lines.append("Per-bucket exit stats (all time)")
        by_bucket: dict[str, list[float]] = {}
        for r in all_exits:
            try:
                key = f"b{r.get('bucket_id','?')}|{r.get('profile','?')}"
                by_bucket.setdefault(key, []).append(float(r["return_pct"]))
            except Exception:
                pass
        bucket_keys = sorted(by_bucket)
        if compact and len(bucket_keys) > 5:
            lines.append(f"  {len(bucket_keys)} bucket profiles with exits "
                         f"(showing top 5 by trade count)")
            bucket_keys = sorted(
                bucket_keys, key=lambda k: len(by_bucket[k]), reverse=True)[:5]
        for key in bucket_keys:
            vals = by_bucket[key]
            r_usd = realized_by_bucket.get(key, 0.0)
            lines.append(
                f"  {key:22s}  n={len(vals):3d}  "
                f"avg={sum(vals)/len(vals):+.1f}%  "
                f"med={sorted(vals)[len(vals)//2]:+.1f}%  "
                f"realized=${r_usd:+,.2f}"
            )

    lines.append("=" * 56)
    return lines


@dataclass
class BucketStatsRow:
    bucket_id: int
    profile: str
    exits: int
    wins: int
    avg_return_pct: float
    med_return_pct: float
    best_return_pct: float
    worst_return_pct: float
    realized_usd: float


@dataclass
class BucketLeaderboard:
    buckets_defined: int
    buckets_with_exits: int
    total_exits: int
    win_rate_pct: float
    avg_return_pct: float
    med_return_pct: float
    p10_return_pct: float
    p90_return_pct: float
    total_realized_usd: float
    rows: list[BucketStatsRow]
    excluded_strategies: tuple[str, ...] = ()
    label: str = ""


def _percentile(vals: list[float], p: float) -> float:
    if not vals:
        return 0.0
    xs = sorted(vals)
    if len(xs) == 1:
        return xs[0]
    idx = (len(xs) - 1) * p / 100.0
    lo = int(idx)
    hi = min(lo + 1, len(xs) - 1)
    frac = idx - lo
    return xs[lo] * (1 - frac) + xs[hi] * frac


def _exit_pnl_usd(r: dict, lots: dict[str, dict]) -> float:
    if r.get("pnl_usd"):
        try:
            return float(r["pnl_usd"])
        except (TypeError, ValueError):
            pass
    lot_id = r.get("lot_id") or ""
    try:
        ret = float(r.get("return_pct") or 0)
    except (TypeError, ValueError):
        return 0.0
    if not lot_id or not ret:
        return 0.0
    lot = lots.get(lot_id)
    if not lot:
        try:
            return float(r.get("cost") or 0) * ret / 100.0
        except (TypeError, ValueError):
            return 0.0
    try:
        qty = max(1, int(float(r.get("qty") or 1)))
        entry_qty = max(1, lot.get("qty", 1))
        cost = lot.get("cost", 0.0)
        return cost * (qty / entry_qty) * ret / 100.0
    except (TypeError, ValueError, ZeroDivisionError):
        return 0.0


def build_bucket_leaderboard(
    state: LabState | None = None,
    *,
    day: str | None = None,
    exclude_strategies: set[str] | frozenset[str] | None = None,
    label: str = "",
) -> BucketLeaderboard:
    """Per-bucket exit stats ranked by median return (best first).

    exclude_strategies: if set, skip exit rows for those strategy_ids (reflected P&L).
    Pass DROPPED_STRATEGIES for the active reflected view.
    """
    del state  # reserved for future open-P&L attribution per bucket
    excl = set(exclude_strategies or ())
    rows = _read_ledger_rows()
    lots: dict[str, dict] = {}
    for r in rows:
        if r.get("event") == "entry" and r.get("lot_id"):
            try:
                lots[r["lot_id"]] = {
                    "cost": float(r.get("cost") or 0),
                    "qty": max(1, int(float(r.get("qty") or 1))),
                }
            except (TypeError, ValueError):
                pass

    exits_by_bucket: dict[int, list[dict]] = {}
    for r in rows:
        if r.get("event") != "exit":
            continue
        sid = str(r.get("strategy_id") or "")
        if sid and sid in excl:
            continue
        if day and not (str(r.get("ts", "")).startswith(day)
                        or str(r.get("date", "")) == day):
            continue
        try:
            bid = int(r.get("bucket_id", -1))
        except (TypeError, ValueError):
            continue
        exits_by_bucket.setdefault(bid, []).append(r)

    stat_rows: list[BucketStatsRow] = []
    all_rets: list[float] = []
    total_realized = 0.0
    total_exits = 0
    total_wins = 0

    profile_by_id = {b.bucket_id: b.name for b in BUCKET_EXPERIMENTS}
    for bid, exs in exits_by_bucket.items():
        rets: list[float] = []
        for x in exs:
            try:
                rets.append(float(x["return_pct"]))
            except (TypeError, ValueError):
                pass
        if not rets:
            continue
        pnls = [_exit_pnl_usd(x, lots) for x in exs]
        realized = sum(pnls)
        wins = sum(1 for x in rets if x > 0)
        total_exits += len(rets)
        total_wins += wins
        total_realized += realized
        all_rets.extend(rets)
        stat_rows.append(BucketStatsRow(
            bucket_id=bid,
            profile=profile_by_id.get(bid, exs[0].get("profile", "?")),
            exits=len(rets),
            wins=wins,
            avg_return_pct=mean(rets),
            med_return_pct=median(rets),
            best_return_pct=max(rets),
            worst_return_pct=min(rets),
            realized_usd=realized,
        ))

    stat_rows.sort(key=lambda r: (r.med_return_pct, r.exits, r.realized_usd), reverse=True)
    win_rate = 100.0 * total_wins / total_exits if total_exits else 0.0
    return BucketLeaderboard(
        buckets_defined=len(BUCKET_EXPERIMENTS),
        buckets_with_exits=len(stat_rows),
        total_exits=total_exits,
        win_rate_pct=win_rate,
        avg_return_pct=mean(all_rets) if all_rets else 0.0,
        med_return_pct=median(all_rets) if all_rets else 0.0,
        p10_return_pct=_percentile(all_rets, 10),
        p90_return_pct=_percentile(all_rets, 90),
        total_realized_usd=total_realized,
        rows=stat_rows,
        excluded_strategies=tuple(sorted(excl)),
        label=label,
    )


def build_reflected_leaderboard(
    state: LabState | None = None,
    *,
    day: str | None = None,
) -> BucketLeaderboard:
    """Leaderboard excluding DROPPED_STRATEGIES (primary reflected view)."""
    excl = set(DROPPED_STRATEGIES)
    tag = ",".join(sorted(excl)) if excl else "none"
    return build_bucket_leaderboard(
        state,
        day=day,
        exclude_strategies=excl,
        label=f"ex-{tag}" if excl else "all",
    )

def print_trial_stats(
    state: LabState,
    equity: float | None = None,
    positions: list[dict] | None = None,
    log_fn=None,
    *,
    file_fn=None,
    console_fn=None,
    compact: bool | None = None,
) -> None:
    """Write full stats to file_fn; compact summary to console_fn."""
    if file_fn is None and console_fn is None:
        for line in format_trial_stats(state, equity, positions, compact=False):
            if log_fn:
                log_fn(line)
            else:
                print(line, flush=True)
        return

    use_compact = _stats_compact() if compact is None else compact
    write_fn = file_fn or log_fn
    for line in format_trial_stats(state, equity, positions, compact=False):
        if write_fn:
            write_fn(line)
        elif log_fn is None and file_fn is None:
            print(line, flush=True)

    if console_fn is not None:
        for line in format_trial_stats(state, equity, positions, compact=use_compact):
            console_fn(line)
    elif file_fn is None and log_fn is None:
        pass  # already printed full above
    elif log_fn and file_fn is None and console_fn is None:
        for line in format_trial_stats(state, equity, positions, compact=use_compact):
            log_fn(line)


def _occ_underlying(occ: str) -> str:
    m = re.match(r"^([A-Z]+)", occ or "")
    return m.group(1) if m else (occ or "")[:4]


def _fetch_lab_orders(trade) -> tuple[list, list]:
    from alpaca.trading.requests import GetOrdersRequest
    from alpaca.trading.enums import QueryOrderStatus

    closed_orders: list = []
    open_orders: list = []
    try:
        closed_orders = list(trade.get_orders(
            GetOrdersRequest(status=QueryOrderStatus.CLOSED, limit=ORDER_FETCH_LIMIT)) or [])
        open_orders = list(trade.get_orders(
            GetOrdersRequest(status=QueryOrderStatus.OPEN, limit=ORDER_FETCH_LIMIT)) or [])
    except Exception as exc:
        log = logging.getLogger("options_lab")
        log.warning("order fetch failed: %s", exc)
    return closed_orders, open_orders


def _create_orphan_lot(state: LabState, occ: str, pos, qty: int, *, log_fn) -> None:
    if qty <= 0:
        return
    orphan_key = f"orphan:{occ}"
    if any(l.occ_symbol == occ and l.entry_order_id == orphan_key and l.qty > 0
           for l in state.lots):
        return
    try:
        total_qty = max(1, int(float(getattr(pos, "qty", 0) or 0)))
    except (TypeError, ValueError):
        total_qty = max(1, qty)
    try:
        cost_basis = abs(float(getattr(pos, "cost_basis", 0) or 0))
    except (TypeError, ValueError):
        cost_basis = 0.0
    entry_cost = cost_basis * (qty / total_qty) if total_qty else 0.0
    entry_price = entry_cost / (qty * 100) if qty else 0.0
    lot = VirtualLot(
        lot_id=new_lot_id(),
        bucket_id=ORPHAN_BUCKET_ID,
        profile_name=ORPHAN_PROFILE,
        strategy_id=ORPHAN_STRATEGY,
        occ_symbol=occ,
        underlying=_occ_underlying(occ),
        qty=qty,
        entry_cost=entry_cost,
        entry_price=entry_price,
        buy_limit_offset=-0.01,
        sell_limit_offset=-0.01,
        take_profit=0.50,
        stop_loss=-0.50,
        entry_date=datetime.now(timezone.utc).isoformat(),
        entry_order_id=orphan_key,
    )
    state.lots.append(lot)
    log_fn(f"  reconcile: orphan lot b{ORPHAN_BUCKET_ID} {occ} x{qty} "
           f"@ {entry_price:.2f} (legacy/unattributed)")


def reconcile_with_broker(trade, state: LabState, log_fn=print) -> LabState:
    """
    Sync virtual lots with Alpaca positions and LAB-tagged order fills.
    Entries create lots on fill only; exits attribute via LX client_order_id.
    """
    occ_re = re.compile(r"^[A-Z]+\d{6}[CP]\d{8}$")

    def _is_opt(sym: str) -> bool:
        return bool(occ_re.match(sym or ""))

    rollover_session(state)
    layout_note = sync_state_layout(state)
    if layout_note:
        log_fn(f"  reconcile: {layout_note}")

    try:
        equity = float(get_lab_account_safe(trade).equity)
    except Exception:
        equity = VIRTUAL_BUCKET_USD

    closed_orders, open_orders = _fetch_lab_orders(trade)
    all_orders = closed_orders + open_orders
    open_ids = {str(getattr(o, "id", "")) for o in open_orders}

    def _process_entry_fill(o) -> None:
        cid = getattr(o, "client_order_id", "") or ""
        parsed = parse_lab_client_order_id(cid)
        if not parsed or parsed["side"] != "entry":
            return
        status = _norm_order_field(getattr(o, "status", ""))
        if status not in ("filled", "partially_filled"):
            return
        filled_qty = int(float(getattr(o, "filled_qty", 0) or 0))
        if filled_qty <= 0:
            return
        occ = getattr(o, "symbol", "")
        if not _is_opt(occ):
            return
        oid = str(o.id)
        existing = next((l for l in state.lots if l.entry_order_id == oid), None)
        if existing is not None:
            # Lot already created (prior run / crash between confirm and ledger).
            # Still write the ledger row if it was never logged.
            if not state.order_already_logged(oid):
                pending = next((p for p in state.pending_orders if p.order_id == oid), None)
                try:
                    fill_px = float(getattr(o, "filled_avg_price", 0) or existing.entry_price or 0)
                except Exception:
                    fill_px = existing.entry_price or 0.0
                entry_cost = existing.entry_cost or (fill_px * 100 * existing.qty)
                ts = str(getattr(o, "filled_at", "") or getattr(o, "updated_at", "") or "")
                append_entry_ledger_from_fill(
                    state, existing, pending, order_id=oid, fill_price=fill_px,
                    entry_cost=entry_cost, ts=ts or None)
                log_fn(f"  reconcile: backfill ledger entry b{existing.bucket_id}|"
                       f"{existing.strategy_id} {existing.underlying} x{existing.qty}")
            return
        if state.order_already_logged(oid):
            # A previously logged entry can be absent from state after its lot
            # was sold or trimmed during broker quantity alignment. Recreating
            # every historical fill here produces a fresh lot_id on every run
            # and can relabel old buckets after a controlled-layout change.
            return
        bucket_id = parsed["bucket_id"]
        strat = parsed["strategy_id"]
        bucket = next((b for b in BUCKET_EXPERIMENTS if b.bucket_id == bucket_id), None)
        if not bucket:
            bucket = BucketProfile(bucket_id=bucket_id, name=f"b{bucket_id}")
        arm = _merge_arm(bucket, strat, equity)
        try:
            fill_px = float(getattr(o, "filled_avg_price", 0) or 0)
        except Exception:
            fill_px = 0.0
        entry_cost = fill_px * 100 * filled_qty
        und = _occ_underlying(occ)
        pending = next((p for p in state.pending_orders if p.order_id == oid), None)
        # Prefer reclaiming an orphan lot on this OCC over creating a duplicate.
        orphan = next(
            (l for l in state.lots
             if l.occ_symbol == occ and l.strategy_id == ORPHAN_STRATEGY and l.qty > 0),
            None,
        )
        if orphan is not None:
            take = min(orphan.qty, filled_qty)
            orphan.qty -= take
            if orphan.qty <= 0:
                state.lots = [l for l in state.lots if l is not orphan]
            else:
                orphan.entry_cost *= (orphan.qty / (orphan.qty + take)) if (orphan.qty + take) else 0
            lot = VirtualLot(
                lot_id=new_lot_id(),
                bucket_id=arm.bucket_id,
                profile_name=arm.profile_name,
                strategy_id=arm.strategy_id,
                occ_symbol=occ,
                underlying=und,
                qty=take,
                entry_cost=entry_cost * (take / filled_qty) if filled_qty else entry_cost,
                entry_price=fill_px,
                buy_limit_offset=arm.buy_limit_offset,
                sell_limit_offset=arm.sell_limit_offset,
                sell_at_mid=arm.sell_at_mid,
                take_profit=arm.take_profit,
                stop_loss=arm.stop_loss,
                eod_only=arm.eod_only,
                market_exit_eod=arm.market_exit_eod,
                entry_date=datetime.now(timezone.utc).isoformat(),
                entry_order_id=oid,
            )
            state.lots.append(lot)
            if pending:
                state.pending_orders = [p for p in state.pending_orders if p.order_id != oid]
            save_state(state)
            log_fn(f"  reconcile: reattributed orphan -> b{bucket_id}|{strat} "
                   f"{und} x{take} @ {fill_px:.2f}")
        else:
            lot = confirm_fill(state, arm, occ, und, filled_qty, entry_cost, fill_px, oid)
        ts = str(getattr(o, "filled_at", "") or getattr(o, "updated_at", "") or "")
        append_entry_ledger_from_fill(
            state, lot, pending, order_id=oid, fill_price=fill_px,
            entry_cost=lot.entry_cost, ts=ts or None)
        log_fn(f"  reconcile: entry fill b{bucket_id}|{strat} {und} x{lot.qty} "
               f"@ {fill_px:.2f}")

    def _process_exit_fill(o) -> None:
        cid = getattr(o, "client_order_id", "") or ""
        parsed = parse_exit_client_order_id(cid)
        if not parsed:
            return
        side = _norm_order_field(getattr(o, "side", ""))
        if side != "sell":
            return
        status = _norm_order_field(getattr(o, "status", ""))
        if status not in ("filled", "partially_filled"):
            return
        oid = str(o.id)
        if state.order_already_logged(oid):
            clear_pending_exit(state, oid)
            return
        filled_qty = int(float(getattr(o, "filled_qty", 0) or 0))
        if filled_qty <= 0:
            return
        lot = find_lot_by_short_id(state, parsed["lot_short"])
        if not lot:
            lot = next(
                (l for l in state.lots
                 if l.bucket_id == parsed["bucket_id"]
                 and l.strategy_id == parsed["strategy_id"]
                 and l.qty > 0),
                None,
            )
        if not lot:
            # Lot may already be gone if a prior buggy path cleared it on submit.
            clear_pending_exit(state, oid)
            return
        try:
            fill_px = float(getattr(o, "filled_avg_price", 0) or 0)
        except Exception:
            fill_px = 0.0
        entry_px = lot.entry_price or (lot.entry_cost / (lot.qty * 100) if lot.qty else 0)
        if entry_px > 0:
            return_pct = (fill_px - entry_px) / entry_px * 100.0
        else:
            return_pct = 0.0
        reason = "reconcile_fill"
        pe = next((p for p in state.pending_exits if p.order_id == oid), None)
        if pe and pe.reason:
            reason = pe.reason
        ts = str(getattr(o, "filled_at", "") or "")
        append_exit_ledger_from_fill(
            state, lot, order_id=oid, qty=min(filled_qty, lot.qty),
            fill_price=fill_px, return_pct=return_pct, reason=reason, ts=ts or None)
        clear_pending_exit(state, oid)
        log_fn(f"  reconcile: exit fill b{lot.bucket_id}|{lot.strategy_id} "
               f"{lot.underlying} {return_pct:+.1f}%")

    def _lookup_order(order_id: str):
        order = next((o for o in all_orders if str(getattr(o, "id", "")) == order_id), None)
        if order is not None:
            return order
        try:
            return trade.get_order_by_id(order_id)
        except Exception:
            return None

    # --- 1) Process filled LAB entry + exit orders (closed + open) ---
    for o in all_orders:
        _process_entry_fill(o)
        _process_exit_fill(o)

    # --- 1b) Resolve pending entries that left the open book ---
    # Closed-order pagination can miss fills; look up by pending order_id.
    for p in list(state.pending_orders):
        if p.order_id in open_ids:
            continue
        order = _lookup_order(p.order_id)
        if order is not None:
            _process_entry_fill(order)

    for pe in list(state.pending_exits):
        if pe.order_id in open_ids:
            continue
        order = _lookup_order(pe.order_id)
        if order is not None:
            _process_exit_fill(order)

    # --- 2) Drop pending only when fill processed or terminal no-fill ---
    terminal_no_fill = {
        "canceled", "cancelled", "expired", "rejected", "replaced",
    }
    before_p = len(state.pending_orders)
    keep_pending: list[PendingOrder] = []
    for p in state.pending_orders:
        if p.order_id in open_ids:
            keep_pending.append(p)
            continue
        order = _lookup_order(p.order_id)
        if order is None:
            keep_pending.append(p)  # keep until broker confirms
            continue
        status = _norm_order_field(getattr(order, "status", ""))
        filled_qty = int(float(getattr(order, "filled_qty", 0) or 0))
        if status in ("filled", "partially_filled") and filled_qty > 0:
            continue  # processed above; drop
        if status in terminal_no_fill and filled_qty <= 0:
            continue  # cancelled/rejected; drop
        keep_pending.append(p)
    state.pending_orders = keep_pending
    if before_p > len(state.pending_orders):
        log_fn(f"  reconcile: cleared {before_p - len(state.pending_orders)} "
               f"resolved pending order(s)")

    before_pe = len(state.pending_exits)
    keep_exits: list[PendingExit] = []
    for pe in state.pending_exits:
        if pe.order_id in open_ids:
            keep_exits.append(pe)
            continue
        order = _lookup_order(pe.order_id)
        if order is None:
            keep_exits.append(pe)
            continue
        status = _norm_order_field(getattr(order, "status", ""))
        filled_qty = int(float(getattr(order, "filled_qty", 0) or 0))
        if status in ("filled", "partially_filled") and filled_qty > 0:
            continue
        if status in terminal_no_fill and filled_qty <= 0:
            continue
        keep_exits.append(pe)
    state.pending_exits = keep_exits
    if before_pe > len(state.pending_exits):
        log_fn(f"  reconcile: cleared {before_pe - len(state.pending_exits)} "
               f"resolved pending exit(s)")

    # --- 3) Broker positions ---
    pos_by_occ: dict[str, Any] = {}
    try:
        for p in trade.get_all_positions():
            sym = getattr(p, "symbol", "")
            ac = str(getattr(p, "asset_class", "") or "")
            if "option" in ac.lower() or _is_opt(sym):
                pos_by_occ[sym] = p
    except Exception as exc:
        log_fn(f"  reconcile: position read failed: {exc}")
        _rebuild_bucket_premium(state)
        save_state(state)
        return state

    # --- 4) Assign broker qty from LAB entry fills before orphan ---
    for occ, pos in pos_by_occ.items():
        try:
            pos_qty = int(float(getattr(pos, "qty", 0)))
        except Exception:
            continue
        if pos_qty <= 0:
            continue
        lot_qty = sum(l.qty for l in state.lots_for_occ(occ))
        need = pos_qty - lot_qty
        if need <= 0:
            continue
        for o in all_orders:
            if need <= 0:
                break
            if getattr(o, "symbol", "") != occ:
                continue
            cid = getattr(o, "client_order_id", "") or ""
            parsed = parse_lab_client_order_id(cid)
            if not parsed or parsed["side"] != "entry":
                continue
            oid = str(o.id)
            if any(l.entry_order_id == oid for l in state.lots):
                continue
            status = _norm_order_field(getattr(o, "status", ""))
            if status not in ("filled", "partially_filled"):
                continue
            filled_qty = int(float(getattr(o, "filled_qty", 0) or 0))
            if filled_qty <= 0:
                continue
            _process_entry_fill(o)
            need = pos_qty - sum(l.qty for l in state.lots_for_occ(occ))

    # --- 5) Drop lots for closed positions ---
    alive_occs = set(pos_by_occ)
    before = len(state.lots)
    state.lots = [l for l in state.lots if l.occ_symbol in alive_occs and l.qty > 0]
    if len(state.lots) < before:
        log_fn(f"  reconcile: removed {before - len(state.lots)} stale lot(s)")

    # --- 6) Qty alignment per OCC ---
    for occ, pos in pos_by_occ.items():
        try:
            pos_qty = int(float(getattr(pos, "qty", 0)))
        except Exception:
            continue
        if pos_qty <= 0:
            continue
        lots = state.lots_for_occ(occ)
        lot_qty = sum(l.qty for l in lots)
        if lot_qty == pos_qty:
            continue
        if lot_qty > pos_qty:
            trim = lot_qty - pos_qty
            for lot in sorted(lots, key=lambda x: x.entry_date):
                if trim <= 0:
                    break
                cut = min(lot.qty, trim)
                lot.qty -= cut
                lot.entry_cost *= (1 - cut / (lot.qty + cut)) if (lot.qty + cut) else 0
                trim -= cut
            state.lots = [l for l in state.lots if l.qty > 0]
            log_fn(f"  reconcile: trimmed {occ} lots to match pos qty {pos_qty}")
        elif lot_qty < pos_qty:
            orphan = pos_qty - lot_qty
            # Try pending orders for this contract before orphan bucket.
            for p in list(state.pending_orders):
                if orphan <= 0 or p.occ_symbol != occ:
                    continue
                order = _lookup_order(p.order_id)
                if order is None:
                    continue
                status = _norm_order_field(getattr(order, "status", ""))
                if status not in ("filled", "partially_filled"):
                    continue
                _process_entry_fill(order)
                orphan = pos_qty - sum(l.qty for l in state.lots_for_occ(occ))
            # Also scan all_orders again for LAB fills on this OCC (pagination miss).
            if orphan > 0:
                for o in all_orders:
                    if orphan <= 0:
                        break
                    if getattr(o, "symbol", "") != occ:
                        continue
                    cid = getattr(o, "client_order_id", "") or ""
                    if not parse_lab_client_order_id(cid):
                        continue
                    _process_entry_fill(o)
                    orphan = pos_qty - sum(l.qty for l in state.lots_for_occ(occ))
            if orphan > 0:
                _create_orphan_lot(state, occ, pos, orphan, log_fn=log_fn)

    # --- 7) Clear stale pending (>1 day) ---
    cutoff = (date.today() - timedelta(days=1)).isoformat()
    stale = [p for p in state.pending_orders if p.submitted < cutoff]
    if stale:
        state.pending_orders = [p for p in state.pending_orders if p.submitted >= cutoff]
        log_fn(f"  reconcile: cleared {len(stale)} stale pending order(s)")

    _rebuild_bucket_premium(state)
    save_state(state)
    return state
