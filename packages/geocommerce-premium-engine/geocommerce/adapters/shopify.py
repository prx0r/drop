from __future__ import annotations
import httpx
from .base import NotConfigured, AdapterError
from ..settings import settings
class ShopifyAdminAdapter:
    API_VERSION="2026-07"
    def graphql(self, query:str, variables:dict|None=None):
        if not settings.shopify_store or not settings.shopify_admin_token: raise NotConfigured("SHOPIFY_STORE/SHOPIFY_ADMIN_TOKEN required")
        host=settings.shopify_store.replace("https://","").rstrip("/")
        url=f"https://{host}/admin/api/{self.API_VERSION}/graphql.json"
        headers={"X-Shopify-Access-Token":settings.shopify_admin_token,"Content-Type":"application/json"}
        with httpx.Client(timeout=45) as client: r=client.post(url,headers=headers,json={"query":query,"variables":variables or {}})
        if r.status_code>=400: raise AdapterError(f"Shopify {r.status_code}: {r.text[:800]}")
        data=r.json()
        if data.get("errors"): raise AdapterError(str(data["errors"])[:800])
        return data.get("data",{})
    def create_product_shell(self,title:str,product_type:str,vendor:str="GeoCommerce"):
        q='''mutation Create($product: ProductCreateInput!) { productCreate(product:$product) { product { id title } userErrors { field message } } }'''
        return self.graphql(q,{"product":{"title":title,"productType":product_type,"vendor":vendor,"status":"DRAFT"}})
