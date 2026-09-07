from __future__ import annotations

from abc import ABC, abstractmethod
from q4radar.models import ProductSeed, Market, ProductObservation


class Source(ABC):
    name: str

    @abstractmethod
    def enrich(self, product: ProductSeed, market: Market, obs: ProductObservation) -> ProductObservation:
        """Return observation enriched with this source. Must be idempotent enough for scan retries."""
        raise NotImplementedError
