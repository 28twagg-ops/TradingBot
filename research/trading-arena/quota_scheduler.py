"""Fair, quota-conscious allocation of free Groq research.

The provider owns the actual limits. This module intentionally uses neither
paid fallback nor user-configured billing. The local target is a request
safety ceiling; HTTP rate headers and Retry-After always override it.
"""
import datetime as dt
import math
import re

UTC=dt.timezone.utc
DAILY_REQUEST_TARGET=72
MAX_BATCH=5
SUCCESS={"RESEARCHED","RESEARCH_IDEA_NEEDS_DATA","RESEARCH_IDEA_NEEDS_REVISION"}
MIN_INTERVAL_MINUTES=40
RESET_CHUNKS=re.compile(r"(\d+(?:\.\d+)?)(h|m|s)")


def seconds_for_duration(value):
    if value is None:return None
    value=str(value).strip()
    if not value:return None
    if re.fullmatch(r"\d+(?:\.\d+)?",value):
        return min(86400.,float(value))
    found=RESET_CHUNKS.findall(value)
    if not found or "".join(a+b for a,b in found)!=value:
        return None
    total=sum(float(n)*{"h":3600,"m":60,"s":1}[unit] for n,unit in found)
    return min(86400.,total) if math.isfinite(total) else None


def read_provider_headers(headers):
    """Only numeric budget metadata, never provider body, key, or user text."""
    if not headers:return {}
    normalized={k.lower():v for k,v in headers.items()}
    info={}
    for name,key in (
        ("x-ratelimit-remaining-requests","remaining_daily_requests"),
        ("x-ratelimit-limit-requests","limit_daily_requests"),
        ("x-ratelimit-remaining-tokens","remaining_minute_tokens"),
        ("x-ratelimit-limit-tokens","limit_minute_tokens")):
        raw=normalized.get(name)
        try:
            if raw is not None and 0<=int(raw)<=100000000:
                info[key]=int(raw)
        except (ValueError,TypeError):
            pass
    for name,key in (
        ("retry-after","retry_after_seconds"),
        ("x-ratelimit-reset-requests","reset_daily_seconds"),
        ("x-ratelimit-reset-tokens","reset_minute_seconds")):
        result=seconds_for_duration(normalized.get(name))
        if result is not None:info[key]=round(result,3)
    return info


def _date(cycle):
    return str(cycle)[:10]


def counted_provider_attempt(event):
    if not isinstance(event,dict):return False
    if event.get("ai_requests",0)>0:return True
    # Legacy events reported 0 for a request that failed with HTTP 429.
    # Conservatively count them to avoid overspending the account.
    if event.get("status")=="AI_UNAVAILABLE":
        return str(event.get("safe_error","")).startswith("GROQ_HTTP_")
    return False


def remaining_time_paced_credit(now,events,target=DAILY_REQUEST_TARGET):
    """Evenly release one request at a time across the UTC day, catch up if late.

    May consume remaining previous slots after missed GitHub Actions jobs, up to
    the conservative safety target; provider headers may impose a lower cap.
    """
    if now.tzinfo is None or not 1<=target<=250:
        raise ValueError("UTC aware date and bounded target required")
    sec=(now.astimezone(UTC)-now.astimezone(UTC).replace(
        hour=0,minute=0,second=0,microsecond=0)).total_seconds()
    ceiling=min(target,1+int((sec/86400)*target))
    used=sum(_date(x.get("cycle"))==now.date().isoformat() and
             counted_provider_attempt(x) for x in events if isinstance(x,dict))
    return max(0,ceiling-used)


def _when(value):
    try:
        when=dt.datetime.fromisoformat(str(value).replace("Z","+00:00"))
        return when if when.tzinfo else None
    except (ValueError,TypeError):
        return None


def eligible_worker_order(accounts,events,now,limit=MAX_BATCH,minimum_gap=MIN_INTERVAL_MINUTES,priority_workers=()):
    """Prioritize the FEWEST successful research sessions, not failures.

    Bots whose last call failed stay eligible on the next chance after a
    reasonable rest. A failed API response must not be counted as research.
    """
    if type(limit)!=int or not 1<=limit<=MAX_BATCH:
        raise ValueError("Outside permitted batch size")
    roster=list(accounts)
    completed_today={id:0 for id in roster}
    recent_by_worker={id:None for id in roster}
    last_success={id:None for id in roster}
    attempted_today={id:0 for id in roster}
    failure_streak={id:0 for id in roster}
    date=now.astimezone(UTC).date().isoformat()
    for x in events:
        if not isinstance(x,dict):continue
        id=x.get("worker")
        if id not in completed_today:continue
        when=_when(x.get("cycle"))
        if when is None or when>now:continue
        if recent_by_worker[id] is None or when>recent_by_worker[id]:
            recent_by_worker[id]=when
        if _date(x.get("cycle"))==date:attempted_today[id]+=1
        if x.get("status") in SUCCESS:
            failure_streak[id]=0
            if _date(x.get("cycle"))==date:completed_today[id]+=1
        elif x.get("status") in ("AI_UNAVAILABLE","REJECTED_INVALID_MODEL_EXPERIMENT"):
            failure_streak[id]+=1
            if last_success[id] is None or when>last_success[id]:
                last_success[id]=when
    def gap_minutes(id):
        # Avoid repeatedly spending free quota on the same broken account.
        # Backoff is bounded; a failed bot always gets another chance.
        streak=failure_streak[id]
        return max(minimum_gap, min(240,40*2**min(3,streak-2))) if streak>=3 else minimum_gap
    selected=[id for id in roster if recent_by_worker[id] is None or
              (now-recent_by_worker[id]).total_seconds()>=gap_minutes(id)*60]
    oldest=dt.datetime(1970,1,1,tzinfo=UTC)
    # A time-boxed evaluation may prioritize a declared subset WITHOUT
    # bypassing cooldowns, request limits, or ledger/evidence safety gates.
    priority=set(priority_workers) & set(roster)
    selected.sort(key=lambda id:(
        0 if id in priority else 1,
        completed_today[id],
        # If every model call fails, spread attempts instead of letting one
        # permanently failing bot monopolize the available free request slots.
        attempted_today[id],
        # Historic completed work breaks ties across midnight.
        len(accounts[id].get("groq_experiments",[])),
        last_success[id] or oldest,
        recent_by_worker[id] or oldest,
        id))
    return selected[:limit]


def cooldown_deadline(now,provider,code):
    """Respect Retry-After and daily rate-limit reset; no immediate retry."""
    if code not in (403,429):return None
    seconds=provider.get("retry_after_seconds")
    if provider.get("remaining_daily_requests")==0:
        seconds=max(seconds or 0,provider.get("reset_daily_seconds") or 3600)
    if seconds is None:
        seconds=900 if code==429 else 3600
    return (now+dt.timedelta(seconds=max(60,min(86400,seconds+5)))).isoformat()


def cooldown_active(state,now):
    when=_when(state.get("cooldown_until"))
    return when is not None and now<when


def spacing_seconds(meta):
    """Avoid bursts against Groq's TPM even while daily requests remain."""
    reset=meta.get("reset_minute_seconds") or 0
    if meta.get("remaining_minute_tokens",100000)<3000:
        return min(95.,max(40.,reset+5))
    return 40.
