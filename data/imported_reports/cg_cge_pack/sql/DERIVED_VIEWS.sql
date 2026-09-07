-- Derived views. Replace PROJECT.

CREATE OR REPLACE VIEW `PROJECT.drop_campaign.current_campaign_state` AS
WITH latest AS (
  SELECT *,
    ROW_NUMBER() OVER (PARTITION BY campaign_id ORDER BY created_at DESC) AS rn
  FROM `PROJECT.drop_campaign.campaign_versions`
)
SELECT * EXCEPT(rn)
FROM latest
WHERE rn = 1;

CREATE OR REPLACE VIEW `PROJECT.drop_campaign.latest_run` AS
WITH ranked AS (
  SELECT *,
    ROW_NUMBER() OVER (
      PARTITION BY campaign_version_id
      ORDER BY created_at DESC
    ) AS rn
  FROM `PROJECT.drop_campaign.evaluation_runs`
)
SELECT * EXCEPT(rn)
FROM ranked
WHERE rn = 1;

CREATE OR REPLACE VIEW `PROJECT.drop_campaign.blocked_gates` AS
SELECT
  g.campaign_version_id,
  g.gate_id,
  g.state,
  g.reason,
  g.run_id,
  r.verdict
FROM `PROJECT.drop_campaign.gate_results` g
JOIN `PROJECT.drop_campaign.latest_run` r
USING (campaign_version_id, run_id)
WHERE g.state IN ('FAIL','UNKNOWN');

CREATE OR REPLACE VIEW `PROJECT.drop_live.campaign_outcomes` AS
SELECT
  campaign_version_id,
  COUNT(*) AS orders,
  SUM(revenue) AS revenue,
  SUM(revenue - IFNULL(supplier_cost,0) - IFNULL(shipping_cost,0) -
      IFNULL(payment_fee,0) - IFNULL(ad_cost_attributed,0)) AS contribution,
  SAFE_DIVIDE(COUNTIF(wrong_part), COUNT(*)) AS wrong_part_rate,
  SAFE_DIVIDE(COUNTIF(returned), COUNT(*)) AS return_rate,
  SAFE_DIVIDE(COUNTIF(resolution_success), COUNT(*)) AS resolution_success_rate,
  SAFE_DIVIDE(COUNTIF(human_intervention), COUNT(*)) AS human_intervention_rate
FROM `PROJECT.drop_live.transactions`
GROUP BY campaign_version_id;

CREATE OR REPLACE VIEW `PROJECT.drop_campaign.research_action_learning` AS
SELECT
  a.action_type,
  a.target_gate,
  COUNT(*) AS n,
  SAFE_DIVIDE(COUNTIF(o.result_state='SUCCESS'), COUNT(*)) AS action_success_rate,
  AVG(o.cash_cost) AS mean_cash_cost,
  AVG(o.human_minutes) AS mean_human_minutes,
  SAFE_DIVIDE(
    SUM(ARRAY_LENGTH(o.gates_resolved)),
    COUNT(*)
  ) AS mean_gates_resolved
FROM `PROJECT.drop_campaign.research_actions` a
JOIN `PROJECT.drop_campaign.research_action_outcomes` o
USING(action_id)
GROUP BY a.action_type, a.target_gate;
