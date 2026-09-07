from __future__ import annotations

import os
from statistics import median
from q4radar.models import ProductSeed, Market, ProductObservation, Evidence
from .base import Source


class GoogleAdsKeywordSource(Source):
    name = "google-ads-keyword-planner"

    def __init__(self):
        self.customer_id = os.getenv("GOOGLE_ADS_CUSTOMER_ID", "").replace("-", "")

    @property
    def enabled(self) -> bool:
        required = [
            "GOOGLE_ADS_CUSTOMER_ID", "GOOGLE_ADS_DEVELOPER_TOKEN", "GOOGLE_ADS_CLIENT_ID",
            "GOOGLE_ADS_CLIENT_SECRET", "GOOGLE_ADS_REFRESH_TOKEN",
        ]
        return all(os.getenv(x) for x in required)

    def _client(self):
        try:
            from google.ads.googleads.client import GoogleAdsClient
        except ImportError as e:
            raise RuntimeError("Install the google extra: pip install 'q4ecom-radar[google]'") from e
        cfg = {
            "developer_token": os.environ["GOOGLE_ADS_DEVELOPER_TOKEN"],
            "client_id": os.environ["GOOGLE_ADS_CLIENT_ID"],
            "client_secret": os.environ["GOOGLE_ADS_CLIENT_SECRET"],
            "refresh_token": os.environ["GOOGLE_ADS_REFRESH_TOKEN"],
            "use_proto_plus": True,
        }
        if os.getenv("GOOGLE_ADS_LOGIN_CUSTOMER_ID"):
            cfg["login_customer_id"] = os.environ["GOOGLE_ADS_LOGIN_CUSTOMER_ID"].replace("-", "")
        return GoogleAdsClient.load_from_dict(cfg)

    def enrich(self, product: ProductSeed, market: Market, obs: ProductObservation) -> ProductObservation:
        if not self.enabled or not market.google_ads_geo_id or not market.google_ads_language_id:
            return obs
        client = self._client()
        svc = client.get_service("KeywordPlanIdeaService")
        google_ads_service = client.get_service("GoogleAdsService")
        req = client.get_type("GenerateKeywordIdeasRequest")
        req.customer_id = self.customer_id
        req.language = google_ads_service.language_constant_path(market.google_ads_language_id)
        req.geo_target_constants.append(google_ads_service.geo_target_constant_path(market.google_ads_geo_id))
        req.keyword_plan_network = client.enums.KeywordPlanNetworkEnum.GOOGLE_SEARCH
        req.include_adult_keywords = False
        req.keyword_seed.keywords.extend(product.keywords[:12])
        response = svc.generate_keyword_ideas(request=req)

        volumes, comps, cpcs = [], [], []
        for item in response:
            m = item.keyword_idea_metrics
            if m.avg_monthly_searches:
                volumes.append(float(m.avg_monthly_searches))
            try:
                comps.append(float(m.competition_index) / 100.0)
            except Exception:
                pass
            if m.high_top_of_page_bid_micros:
                cpcs.append(float(m.high_top_of_page_bid_micros) / 1_000_000.0)
        if volumes:
            obs.search_volume = sum(volumes)
            obs.evidence.append(Evidence(source=self.name, metric="aggregate_monthly_searches", value=obs.search_volume, unit="searches/month", confidence=0.95, url="https://developers.google.com/google-ads/api/docs/keyword-planning/generate-keyword-ideas"))
        if comps:
            obs.keyword_competition = sum(comps) / len(comps)
        if cpcs:
            obs.avg_cpc_usd = median(cpcs)
        return obs
