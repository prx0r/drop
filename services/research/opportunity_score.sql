-- Illustrative only; calibrate weights empirically.
-- Inputs should be normalized/percentile-scored by country/category.
SELECT
  *,
  (search_demand_score * 0.20
   + demand_momentum_score * 0.15
   + contribution_margin_score * 0.25
   + price_gap_score * 0.10
   + cpc_efficiency_score * 0.15
   + supplier_reliability_score * 0.15) AS opportunity_score
FROM candidate_products;
