-- DROP × CG × CGE canonical BigQuery schema.
-- Use your actual project id in place of `PROJECT`.

CREATE SCHEMA IF NOT EXISTS `PROJECT.drop_evidence`;
CREATE SCHEMA IF NOT EXISTS `PROJECT.drop_graph`;
CREATE SCHEMA IF NOT EXISTS `PROJECT.drop_campaign`;
CREATE SCHEMA IF NOT EXISTS `PROJECT.drop_live`;

CREATE TABLE IF NOT EXISTS `PROJECT.drop_evidence.observations` (
  evidence_id STRING NOT NULL,
  claim_type STRING NOT NULL,
  subject_type STRING NOT NULL,
  subject_id STRING NOT NULL,
  country STRING,
  value_json JSON,
  numeric_value FLOAT64,
  unit STRING,
  as_of TIMESTAMP,
  retrieved_at TIMESTAMP NOT NULL,
  source_url STRING,
  source_title STRING,
  source_tier STRING NOT NULL,       -- A/B/C/D
  source_hash STRING,
  collector STRING,
  extractor_version STRING,
  verification_state STRING NOT NULL, -- RAW/CANDIDATE/VERIFIED/REJECTED/CONFLICTED
  verifier STRING,
  verified_at TIMESTAMP,
  supersedes_evidence_id STRING,
  stale_after_days INT64,
  notes STRING
)
PARTITION BY DATE(retrieved_at)
CLUSTER BY country, claim_type, subject_type, subject_id;

CREATE TABLE IF NOT EXISTS `PROJECT.drop_evidence.buyer_role_observations` (
  observation_id STRING NOT NULL,
  country STRING NOT NULL,
  campaign_atom_id STRING,
  source_evidence_id STRING NOT NULL,
  observed_at TIMESTAMP,
  intent_class STRING, -- BUY_EXACT_PART / WHICH_PART_FITS / DIY_REPLACE / BUY_PART_HIRE_INSTALLER / NEED_REPAIRER / NEED_DIAGNOSIS
  problem_noticer STRING,
  diagnoser STRING,
  sku_selector STRING,
  payer STRING,
  installer STRING,
  verified BOOL
)
PARTITION BY DATE(observed_at)
CLUSTER BY country, campaign_atom_id, sku_selector;

CREATE TABLE IF NOT EXISTS `PROJECT.drop_evidence.supplier_observations` (
  observation_id STRING NOT NULL,
  supplier_id STRING NOT NULL,
  country STRING,
  observed_at TIMESTAMP NOT NULL,
  source_evidence_id STRING NOT NULL,
  sku STRING,
  mpn STRING,
  public_price FLOAT64,
  currency STRING,
  stock_qty INT64,
  stock_state STRING,
  dealer_cost FLOAT64,
  dealer_discount FLOAT64,
  reseller_allowed BOOL,
  direct_ship BOOL,
  blind_ship BOOL,
  feed_type STRING,
  returns_known BOOL,
  warranty_known BOOL,
  moq_value FLOAT64,
  terms_expiry TIMESTAMP,
  verified BOOL
)
PARTITION BY DATE(observed_at)
CLUSTER BY country, supplier_id, mpn;

CREATE TABLE IF NOT EXISTS `PROJECT.drop_evidence.demand_events` (
  event_id STRING NOT NULL,
  country STRING NOT NULL,
  campaign_atom_id STRING,
  occurred_at TIMESTAMP,
  event_type STRING, -- TRANSACTION / VERIFIED_PURCHASE / EXACT_SEARCH / QUOTE / CHECKOUT_START / SERVICE_REPLACEMENT
  quantity FLOAT64,
  source_evidence_id STRING,
  intent_class STRING,
  exact_model_or_mpn BOOL,
  verified BOOL
)
PARTITION BY DATE(occurred_at)
CLUSTER BY country, campaign_atom_id, event_type;

CREATE TABLE IF NOT EXISTS `PROJECT.drop_graph.entities` (
  entity_id STRING NOT NULL,
  entity_type STRING NOT NULL, -- OEM / ASSET / MODEL / GENERATION / COMPONENT / SKU / SUPPLIER
  canonical_name STRING NOT NULL,
  country STRING,
  attributes JSON,
  created_at TIMESTAMP,
  updated_at TIMESTAMP
)
CLUSTER BY entity_type, country;

CREATE TABLE IF NOT EXISTS `PROJECT.drop_graph.compatibility_edges` (
  edge_id STRING NOT NULL,
  from_entity_id STRING NOT NULL,
  relation STRING NOT NULL, -- FITS / DOES_NOT_FIT / REPLACED_BY / SUPERSEDES / REQUIRES_PART / REQUIRES_ADAPTER
  to_entity_id STRING,
  qualifiers JSON,
  evidence_id STRING NOT NULL,
  verified BOOL NOT NULL,
  valid_from TIMESTAMP,
  valid_to TIMESTAMP,
  created_at TIMESTAMP
)
CLUSTER BY from_entity_id, relation, to_entity_id;

CREATE TABLE IF NOT EXISTS `PROJECT.drop_graph.installed_base_observations` (
  observation_id STRING NOT NULL,
  country STRING NOT NULL,
  entity_id STRING NOT NULL,
  surviving_units_low FLOAT64,
  surviving_units_mid FLOAT64,
  surviving_units_high FLOAT64,
  annual_trigger_rate_low FLOAT64,
  annual_trigger_rate_mid FLOAT64,
  annual_trigger_rate_high FLOAT64,
  as_of DATE,
  evidence_id STRING NOT NULL,
  verified BOOL
)
CLUSTER BY country, entity_id;

CREATE TABLE IF NOT EXISTS `PROJECT.drop_campaign.campaign_versions` (
  campaign_version_id STRING NOT NULL,
  campaign_id STRING NOT NULL,
  parent_version_id STRING,
  created_at TIMESTAMP NOT NULL,
  created_by STRING,
  schema_version STRING NOT NULL,
  hypothesis_json JSON NOT NULL,
  hypothesis_hash STRING NOT NULL,
  state STRING NOT NULL,
  track STRING NOT NULL,
  country STRING NOT NULL,
  atom_id STRING,
  git_commit_sha STRING,
  mutation_receipt_id STRING
)
PARTITION BY DATE(created_at)
CLUSTER BY country, track, campaign_id;

CREATE TABLE IF NOT EXISTS `PROJECT.drop_campaign.evidence_snapshots` (
  evidence_snapshot_id STRING NOT NULL,
  campaign_version_id STRING NOT NULL,
  as_of TIMESTAMP NOT NULL,
  compiler_version STRING NOT NULL,
  rubric_version_id STRING NOT NULL,
  manifest_json JSON NOT NULL,
  manifest_hash STRING NOT NULL,
  created_at TIMESTAMP NOT NULL
)
PARTITION BY DATE(created_at)
CLUSTER BY campaign_version_id;

CREATE TABLE IF NOT EXISTS `PROJECT.drop_campaign.gate_results` (
  run_id STRING NOT NULL,
  campaign_version_id STRING NOT NULL,
  evidence_snapshot_id STRING NOT NULL,
  rubric_version_id STRING NOT NULL,
  gate_id STRING NOT NULL,
  state STRING NOT NULL, -- PASS/FAIL/UNKNOWN
  metric_value FLOAT64,
  threshold_json JSON,
  evidence_ids ARRAY<STRING>,
  reason STRING,
  created_at TIMESTAMP NOT NULL
)
PARTITION BY DATE(created_at)
CLUSTER BY campaign_version_id, gate_id, state;

CREATE TABLE IF NOT EXISTS `PROJECT.drop_campaign.evaluation_runs` (
  run_id STRING NOT NULL,
  campaign_version_id STRING NOT NULL,
  evidence_snapshot_id STRING NOT NULL,
  rubric_version_id STRING NOT NULL,
  cg_git_sha STRING NOT NULL,
  worldpack_id STRING NOT NULL,
  public_gate_pass BOOL NOT NULL,
  secret_suite_pass BOOL,
  verdict STRING NOT NULL,
  metrics JSON,
  receipt_hash STRING,
  created_at TIMESTAMP NOT NULL
)
PARTITION BY DATE(created_at)
CLUSTER BY verdict, campaign_version_id;

CREATE TABLE IF NOT EXISTS `PROJECT.drop_campaign.mutation_proposals` (
  mutation_id STRING NOT NULL,
  parent_campaign_version_id STRING NOT NULL,
  proposer STRING NOT NULL,
  cge_git_sha STRING,
  mutation_type STRING NOT NULL,
  mutation_json JSON NOT NULL,
  rationale STRING,
  target_failed_gate STRING,
  created_at TIMESTAMP NOT NULL,
  admission_state STRING NOT NULL, -- PROPOSED/QUARANTINED/ADMITTED/REJECTED
  child_campaign_version_id STRING
)
PARTITION BY DATE(created_at)
CLUSTER BY mutation_type, admission_state;

CREATE TABLE IF NOT EXISTS `PROJECT.drop_campaign.research_actions` (
  action_id STRING NOT NULL,
  campaign_version_id STRING NOT NULL,
  target_gate STRING NOT NULL,
  action_type STRING NOT NULL,
  action_json JSON NOT NULL,
  expected_information_value FLOAT64,
  expected_cash_cost FLOAT64,
  expected_human_minutes FLOAT64,
  prior_source STRING,
  state STRING NOT NULL, -- PROPOSED/APPROVED/RUNNING/DONE/FAILED
  created_at TIMESTAMP NOT NULL,
  completed_at TIMESTAMP
)
PARTITION BY DATE(created_at)
CLUSTER BY state, target_gate, action_type;

CREATE TABLE IF NOT EXISTS `PROJECT.drop_campaign.research_action_outcomes` (
  outcome_id STRING NOT NULL,
  action_id STRING NOT NULL,
  result_state STRING NOT NULL,
  evidence_ids ARRAY<STRING>,
  gates_resolved ARRAY<STRING>,
  gate_outcomes JSON,
  cash_cost FLOAT64,
  human_minutes FLOAT64,
  completed_at TIMESTAMP NOT NULL
)
PARTITION BY DATE(completed_at);

CREATE TABLE IF NOT EXISTS `PROJECT.drop_campaign.incumbent_benchmark_cases` (
  case_id STRING NOT NULL,
  campaign_atom_id STRING NOT NULL,
  suite_layer STRING NOT NULL, -- DEV/VALIDATION/SECRET
  prompt_hash STRING NOT NULL,
  expected_resolution_json JSON,
  created_at TIMESTAMP NOT NULL
)
CLUSTER BY campaign_atom_id, suite_layer;

CREATE TABLE IF NOT EXISTS `PROJECT.drop_campaign.incumbent_benchmark_results` (
  run_id STRING NOT NULL,
  campaign_atom_id STRING NOT NULL,
  incumbent_id STRING NOT NULL,
  case_id STRING NOT NULL,
  correct BOOL NOT NULL,
  executable BOOL NOT NULL,
  compatibility_supported BOOL,
  stock_current BOOL,
  merchant_named BOOL,
  observed_at TIMESTAMP NOT NULL
)
PARTITION BY DATE(observed_at)
CLUSTER BY campaign_atom_id, incumbent_id;

CREATE TABLE IF NOT EXISTS `PROJECT.drop_live.transactions` (
  order_id STRING NOT NULL,
  campaign_version_id STRING NOT NULL,
  occurred_at TIMESTAMP NOT NULL,
  sku STRING,
  revenue FLOAT64,
  currency STRING,
  supplier_cost FLOAT64,
  shipping_cost FLOAT64,
  payment_fee FLOAT64,
  ad_cost_attributed FLOAT64,
  returned BOOL,
  wrong_part BOOL,
  resolution_success BOOL,
  human_intervention BOOL,
  supplier_id STRING,
  country STRING
)
PARTITION BY DATE(occurred_at)
CLUSTER BY campaign_version_id, country, supplier_id;
