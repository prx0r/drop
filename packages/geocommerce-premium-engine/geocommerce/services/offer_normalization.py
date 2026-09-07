from __future__ import annotations

from datetime import datetime, timezone
from ..models import SupplierOffer
from .markets import get_market
from .signals import save_offer


def normalize_offer_currency(offer: SupplierOffer, market_code: str, convert) -> SupplierOffer:
    """Normalize supplier offer into market currency before scoring.

    `convert` is injectable so production can use PSP/FX quotes; ECB is the research default.
    """
    market=get_market(market_code)
    if offer.currency.upper()==market.currency:
        normalized=offer.model_copy(update={'currency':market.currency})
    else:
        normalized=offer.model_copy(update={
            'unit_cost':round(convert(offer.unit_cost,offer.currency,market.currency),4),
            'shipping_cost':round(convert(offer.shipping_cost,offer.currency,market.currency),4),
            'currency':market.currency,
            'observed_at':datetime.now(timezone.utc).isoformat(),
        })
    save_offer(normalized)
    return normalized
