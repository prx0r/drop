from __future__ import annotations
class KopyHandoffAdapter:
    """Kopy has a strong public UI product, but no dependable public developer API was found.
    Generate a human-operable handoff manifest instead of browser automation or invented endpoints.
    """
    def manifest(self, product_urls:list[str], target_language:str) -> dict:
        return {"tool":"Kopy","mode":"manual_handoff","target_language":target_language,"product_urls":product_urls,"instructions":["Import source URLs in Kopy","Use native translation as a draft only","Replace generated claims with canonical facts","Export/publish only after QA gate"]}
