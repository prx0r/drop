from __future__ import annotations

import httpx
from .base import NotConfigured, AdapterError
from ..settings import settings


class OpenAICompatibleLLMAdapter:
    """Minimal OpenAI-compatible chat-completions adapter.

    The engine never asks this adapter to invent product facts. It is intended for
    constrained translation, rewriting, query clustering, and support phrasing.
    """

    def _configured(self) -> None:
        if not (settings.llm_base_url and settings.llm_api_key and settings.llm_model):
            raise NotConfigured("LLM_BASE_URL, LLM_API_KEY and LLM_MODEL are required")

    def complete(self, *, system: str, user: str, temperature: float = 0.1) -> str:
        self._configured()
        url = settings.llm_base_url.rstrip("/") + "/chat/completions"
        headers = {
            "Authorization": f"Bearer {settings.llm_api_key}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": settings.llm_model,
            "temperature": temperature,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
        }
        with httpx.Client(timeout=60) as client:
            r = client.post(url, headers=headers, json=payload)
        if r.status_code >= 400:
            raise AdapterError(f"LLM {r.status_code}: {r.text[:800]}")
        try:
            return r.json()["choices"][0]["message"]["content"].strip()
        except (KeyError, IndexError, TypeError) as exc:
            raise AdapterError("LLM response missing choices[0].message.content") from exc
