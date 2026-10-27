"""Offline, API-free tests of source freedom and safe source handling."""
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from open_research import (discover, safe_query, safe_domain, requested_sources,
                           search_web, search_github, fetch_public_index,
                           url_for_display, requires_unavailable_test_inputs)

class IndependentDiscoveryTests(unittest.TestCase):
    def test_custom_domains_not_whitelisted_to_prestigious_publishers(self):
        self.assertEqual(safe_domain("obscure-trading-blog.example"),"obscure-trading-blog.example")
        self.assertEqual(safe_domain("tiktok.com"),"tiktok.com")
        self.assertEqual(safe_domain("reddit.com"),"reddit.com")
        for hostile in ("localhost","127.0.0.1","evil.local","169.254.169.254",
                        "example.com/path","http://example.com","example.com\nabc"):
            self.assertIsNone(safe_domain(hostile))
    def test_unavailable_data_claims_never_count_as_verified_hourly_backtest(self):
        for claim in (
            "When 5-minute BTC momentum spikes, ETH rises",
            "When the order book depth doubles, prices rise",
            "If BTC-USD volatility and VWAP diverge, buy",
            "If BTC and ETH exhibit correlation divergence, rotate positions",
            "When the opening-range high is broken, buy calls"
        ):
            self.assertTrue(requires_unavailable_test_inputs(claim),claim)
        self.assertFalse(requires_unavailable_test_inputs(
            "When BTC-USD exceeds the maximum of the prior 20 hourly closes by 1%, buy"))

    def test_choice_is_bots_own_for_forums_video_social(self):
        self.assertEqual(requested_sources(["tiktok","reddit","youtube","academic"]),
                         ["tiktok","reddit","youtube"])
        self.assertEqual(requested_sources(["forum","blog","web"]),
                         ["forum","blog","web"])
        self.assertEqual(safe_query("    unusual  stock \n idea "), "unusual stock idea")
    def test_bing_results_are_snippet_only_and_links_never_fetched(self):
        xml=b'<rss><channel><item><title>Unusual strategy</title><link>https://www.tiktok.com/@ideas/video/1</link><description>Untrusted post</description></item></channel></rss>'
        calls=[]
        def provider(url):
            calls.append(url)
            return xml
        findings=search_web("odd strategies","tiktok",fetcher=provider)
        self.assertEqual(len(findings),1)
        self.assertEqual(findings[0]["read_level"],"public_search_result_only")
        self.assertIn("site%3Atiktok.com",calls[0])
        self.assertTrue(calls[0].startswith("https://www.bing.com/search?"))
        self.assertEqual(len(calls),1)
        self.assertEqual(url_for_display("https://localhost/secrets"),"")
        self.assertEqual(url_for_display("https://127.0.0.1/private"),"")
    def test_git_repositories_are_metadata_not_executed(self):
        rows='{"items":[{"full_name":"hello/strange-strategy","html_url":"https://github.com/hello/strange-strategy","description":"unusual backtest script"}]}'
        items=search_github("unknown hedge",fetcher=lambda _:rows.encode())
        self.assertEqual(items[0]["platform"],"github")
        self.assertEqual(items[0]["read_level"],"repository_metadata_only")
    def test_unavailable_sources_are_not_fabricated(self):
        result=discover("weird strategy",["reddit","tiktok","github"],
             web_search=lambda *_:[],github_search=lambda *_:[])
        self.assertEqual(result["found"],[])
        self.assertEqual(result["attempted"],["reddit","tiktok","github"])
    def test_untrusted_links_never_permit_endpoints_outside_search_provider(self):
        with self.assertRaises(ValueError):
            fetch_public_index("https://evil.example/steal",cache={})
        with self.assertRaises(ValueError):
            fetch_public_index("https://127.0.0.1/",cache={})
    def test_custom_site_used_only_as_index_query(self):
        calls=[]
        def web(query,channel,domain):
            calls.append((query,channel,domain))
            return [{"url":"https://quaint.example/trading",
                     "title":"Unusual","platform":"custom_site",
                     "read_level":"public_search_result_only","snippet":"snippet"}]
        result=discover("30 year old trend",["github"],"quaint.example",
             web_search=web,github_search=lambda *_:[])
        self.assertEqual(calls[0],("30 year old trend","web","quaint.example"))
        self.assertEqual(result["found"][0]["platform"],"custom_site")
    def test_reddit_youtube_tiktok_no_pretend_video_transcript(self):
        for p in ("reddit","youtube","tiktok"):
            r=discover("market research",[p],
                 web_search=lambda *_:[{"url":"https://www.example.com/video",
                     "title":"video metadata","platform":p,
                     "read_level":"public_search_result_only","snippet":"unverified"}])
            self.assertEqual(r["found"][0]["read_level"],"public_search_result_only")

if __name__=="__main__": unittest.main()
