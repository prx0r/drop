from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class ShoppingResult:
    title: str
    price: float | None
    currency: str | None
    merchant: str | None
    link: str | None
    image_url: str | None
    position: int


class ShoppingProvider(Protocol):
    def search(self, *, query: str, country: str, language: str) -> list[ShoppingResult]: ...


@dataclass(frozen=True)
class KeywordMetric:
    keyword: str
    monthly_searches: float
    cpc: float
    competition: float | None = None


class KeywordProvider(Protocol):
    def metrics(self, *, keywords: list[str], country: str, language: str) -> list[KeywordMetric]: ...
