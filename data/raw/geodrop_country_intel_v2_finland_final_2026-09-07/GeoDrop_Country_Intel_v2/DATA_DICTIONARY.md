# Data Dictionary / High-Signal Predictors

The fields below exist because they repeatedly separated plausible-looking ecommerce ideas from credible ones in GeoDrop research and external cross-border ecommerce evidence.

| Predictor | Why retained | Canonical location |
|---|---|---|
| exact local search demand | prevents trend-story hallucination | acquisition + product_market |
| CPC / bid range | determines paid feasibility | acquisition |
| monthly search seasonality | exposes temporary spikes | acquisition |
| Google Shopping / comparison seller count | actual purchasability | competition |
| GOOD_SELLER_COUNT | raw seller count is misleading | competition |
| merchant quality | specialist/helpful merchant scarcity is the moat | competition |
| CONTENT_GAP | advice may be weak even where stock is plentiful | competition |
| exact local retail price | needed for contribution | competition/product_market |
| dealer/net cost | public wholesale proxies are insufficient | supply/product_market |
| delivery time + visible shipping price | waiting/shipping cost reduces cross-border value | consumer/supply |
| returns burden | lenient/clear returns reduce perceived risk | consumer/supply |
| local payment | institutional trust + checkout conversion | consumer/supply |
| resale authorization | avoids non-viable grey-market model | supply |
| warranty/RMA | technical products can hide service costs | supply |
| installed base | predicts durable aftermarket demand | structural |
| replacement cycle | distinguishes durable ecosystem from trend | structural |
| regulation/climate/local problem | creates country-specific necessity | structural |
| source-market proof | constrains ideation to models already working | source_markets |
| supplier stock reliability | prevents post-launch collapse | supply/outcome |
| realized contribution | true economic target | outcome |
| posterior P(CVR > breakeven) | quantitative scale/kill evidence | experiment/outcome |

Cross-border research retained in the source registry supports trustworthiness/reputation, price competitiveness, product uniqueness, communication/waiting cost, logistics, third-party payment/certification, reviews, and return-policy leniency as purchase-intention/trust factors.
