# Data Source Matrix

| Layer | Preferred sources | Canonical output |
|---|---|---|
| macro/ecommerce | national statistics, PostNord/industry reports | observations + macro series |
| installed base | registries, trade bodies, stock/sales tables | ecosystems + installed_base series |
| geography/risk | climate, damage/insurance, outages, coverage | problems + geographic report |
| query demand | Google Ads Keyword Planner, Google Trends | queries + search series |
| shopping demand | Merchant Center Best Sellers where eligible | acquisition report/series |
| competition | Prisjakt/Hintaopas/PriceRunner, Shopping/SERPs | merchants + seller/price snapshots |
| companies/services | legal registries, dealer/installer lists | merchants/service census |
| trade flows | SSB/StatFin, Eurostat Comext, UN Comtrade | trade_code_map + imports series |
| source-market models | Sweden/Germany/Netherlands merchant census | source_archetypes + gaps |
| supply | manufacturers, distributors, CJ/BigBuy/etc | product_market/supply snapshots |
| outcomes | store/ads/analytics/payment/RMA | experiments + outcomes + metrics series |

Large raw datasets should be stored externally and referenced by immutable URI/hash; the country ZIP keeps normalized high-signal rows and acquisition contracts rather than duplicating gigabytes.
