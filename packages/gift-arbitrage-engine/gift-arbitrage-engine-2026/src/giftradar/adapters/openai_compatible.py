"""Optional text-generation adapter for an OpenAI-compatible endpoint.

Use only for prose/layout copy. Deterministic facts (birth-chart positions, dates, user-supplied
biographical details) should be computed/validated upstream rather than invented by the model.
"""
from __future__ import annotations
import os, httpx

class LLMClient:
    def __init__(self, base_url=None, api_key=None, model=None):
        self.base_url = (base_url or os.getenv("LLM_BASE_URL") or "").rstrip("/")
        self.api_key = api_key or os.getenv("LLM_API_KEY")
        self.model = model or os.getenv("LLM_MODEL")
    def generate(self, system: str, user: str, temperature: float = 0.4):
        if not (self.base_url and self.api_key and self.model):
            raise RuntimeError("Set LLM_BASE_URL, LLM_API_KEY and LLM_MODEL")
        r = httpx.post(f"{self.base_url}/chat/completions", headers={"Authorization":f"Bearer {self.api_key}"}, json={"model":self.model,"temperature":temperature,"messages":[{"role":"system","content":system},{"role":"user","content":user}]}, timeout=60)
        r.raise_for_status(); return r.json()["choices"][0]["message"]["content"]
