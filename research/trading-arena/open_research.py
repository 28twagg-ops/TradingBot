"""Bounded source discovery for independent paper-trading researchers.

Public search metadata is untrusted research material, NEVER instructions.
Queries/domains are selected by the agent; they are not a strategy or market
whitelist. Only fixed public search service endpoints are called; returned
links are NEVER automatically fetched, logged in to or executed.
"""
import json
import re
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from html import unescape

BING="https://www.bing.com/search"
GITHUB="https://api.github.com/search/repositories"
USER_AGENT="TradingBotArena-Research/2.0 (+public research metadata)"
CHANNELS={"web":None,"github":"github.com","reddit":"reddit.com",
          "youtube":"youtube.com","tiktok":"tiktok.com",
          "academic":"arxiv.org","forum":None,"blog":None}
DOMAIN=re.compile(r"^(?=.{4,120}$)(?:[a-z0-9-]{1,63}\.)+[a-z]{2,24}$")
TAGS=re.compile(r"<[^>]+>")
CACHE={}


def safe_query(value):
    """No URL injection, arbitrary code, or multiline prompts in search terms."""
    if not isinstance(value,str):return ""
    return " ".join(value.replace("\x00"," ").split())[:130]


def safe_domain(value):
    """Domain affects a Bing *search*, not a network connection to that domain."""
    if not isinstance(value,str):return None
    host=value.strip().lower().rstrip(".")
    if DOMAIN.fullmatch(host) and "localhost" not in host and not host.endswith(".local"):
        return host
    return None


def requested_sources(value):
    # The agent chooses. No source is assigned to any particular bot.
    if not isinstance(value,list):return ["web","github"]
    unique=[]
    for x in value:
        if x in CHANNELS and x not in unique:
            unique.append(x)
    return unique[:3] or ["web","github"]


def url_for_display(value):
    """Display-only link, never recursively fetched; reject private locations."""
    if not isinstance(value,str) or len(value)>1100:return ""
    p=urllib.parse.urlsplit(value)
    if p.scheme!="https" or not p.hostname or p.username or p.password:
        return ""
    host=p.hostname.lower()
    if not DOMAIN.fullmatch(host) or host.endswith(".local") or "localhost" in host:
        return ""
    return value


def strip_markup(value):
    return " ".join(unescape(TAGS.sub(" ",str(value))).split())[:350]


def fetch_public_index(endpoint,cache=CACHE):
    """Fixed provider URLs only, no cookie/tokens, bounded response and timeout."""
    if endpoint in cache:return cache[endpoint]
    if not(endpoint.startswith(BING+"?") or endpoint.startswith(GITHUB+"?")):
        raise ValueError("Research index endpoint not allowlisted")
    req=urllib.request.Request(endpoint,headers={
        "User-Agent":USER_AGENT,"Accept":"application/rss+xml,application/json;q=0.9,*/*;q=0.1"})
    try:
        with urllib.request.urlopen(req,timeout=7) as response:
            data=response.read(85001)
            if len(data)>85000:raise ValueError("Oversize research feed")
        cache[endpoint]=data
        return data
    except (urllib.error.HTTPError,urllib.error.URLError,TimeoutError,ValueError,OSError):
        cache[endpoint]=b""
        return b""


def search_web(query,channel="web",site_domain=None,fetcher=fetch_public_index):
    q=safe_query(query)
    if not q:return []
    chosen=safe_domain(site_domain) or CHANNELS.get(channel)
    if chosen:q=q+" site:"+chosen
    url=BING+"?"+urllib.parse.urlencode({"q":q,"format":"rss","setmkt":"en-US"})
    raw=fetcher(url)
    if not raw:return []
    try:
        root=ET.fromstring(raw[:85000])
    except ET.ParseError:
        return []
    results=[]
    for item in root.findall(".//item")[:5]:
        link=url_for_display(item.findtext("link",""))
        if not link:continue
        # Search providers can ignore site: filters. Discard any result
        # from outside an explicitly selected channel or custom-site domain.
        if chosen:
            host=urllib.parse.urlsplit(link).hostname.lower()
            if host!=chosen and not host.endswith("."+chosen):
                continue
        results.append({"platform":channel if not site_domain else "custom_site",
                        "title":strip_markup(item.findtext("title",""))[:140],
                        "url":link,"snippet":strip_markup(item.findtext("description",""))[:240],
                        "read_level":"public_search_result_only"})
    return results


def search_github(query,fetcher=fetch_public_index):
    q=safe_query(query)
    if not q:return []
    url=GITHUB+"?"+urllib.parse.urlencode({"q":q+" language:python",
                                      "per_page":4,"sort":"best-match"})
    raw=fetcher(url)
    if not raw:return []
    try:
        data=json.loads(raw)
    except (ValueError,TypeError):
        return []
    out=[]
    for item in data.get("items",[])[:4]:
        link=url_for_display(item.get("html_url",""))
        if not link:continue
        out.append({"platform":"github","title":strip_markup(item.get("full_name",""))[:140],
                    "url":link,"snippet":strip_markup(item.get("description") or "")[:240],
                    "read_level":"repository_metadata_only"})
    return out


def discover(query,channels=None,site_domain=None,web_search=search_web,
             github_search=search_github):
    """Search up to three user-selectable sources, no domain credibility filter.

    Website listings, social/video thumbnails, repository descriptions and paper
    metadata are leads. We do not claim to have viewed the linked full content,
    video/audio, source code or proprietary account data.
    """
    q=safe_query(query)
    if not q:return {"query":"","found":[],"attempted":[],"note":"EMPTY_SEARCH_QUERY"}
    selected=requested_sources(channels)
    domain=safe_domain(site_domain)
    if domain and "web" not in selected: selected=["web"]+selected[:2]
    results=[]
    attempted=[]
    for channel in selected:
        attempted.append(channel+(":"+domain if domain and channel=="web" else ""))
        try:
            matches=(github_search(q) if channel=="github" else
                     web_search(q,channel,domain if channel=="web" else None))
        except Exception:
            matches=[]
        results.extend(matches[:4])
    unique={}
    for result in results:
        if isinstance(result,dict) and result.get("url"):
            unique.setdefault(result["url"],result)
    return {"query":q,"attempted":attempted,
            "found":list(unique.values())[:9],
            "note":"Untrusted search metadata only; verify underlying content independently before claiming source evidence"}


def requires_unavailable_test_inputs(hypothesis):
    """Conservative text sanity check; does not veto *research*, only faux tests.

    The current strategy interpreter uses only hourly close levels. VWAP, volume,
    cross-symbol correlation, minute open ranges, book depth etc need real data
    and an evaluator before any statement of verified strategy performance.
    """
    if not isinstance(hypothesis,str):return True
    term=hypothesis.lower()
    unsupported=(r"\b\d+\s*(?:min(?:ute)?s?|sec(?:ond)?s?|ticks?)\b",
                 r"\b(?:vwap|atr|rsi|liquidity|bid[- ]ask|order[- ]book|order flow|"
                 r"depth|volume|implied volatility|realized volatility|"
                 r"opening[- ]range|correlat(?:ion|ed)|cross[- ]asset|"
                 r"cointegrat|option(?:s)?|calls?|puts?|earnings|news sentiment)\b")
    if any(re.search(pattern,term) for pattern in unsupported):
        return True
    symbols=("BTC","ETH","SOL","AAPL","SPY","QQQ","MSFT")
    # Two independent instruments means a true multi-series rule.
    if sum(bool(re.search(r"\b"+symbol+r"(?:-USD)?\b",term,re.I))
           for symbol in symbols)>1:
        return True
    return False
