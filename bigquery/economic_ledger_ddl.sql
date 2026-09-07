-- BigQuery DDL for GeoDrop Economic Ledger
-- Project: project-ff2366d2-8fda-4fcb-9ba
-- Dataset: drop

-- =============================================================================
-- DIMENSIONS
-- =============================================================================

-- Country dimension (from country packs)
CREATE TABLE IF NOT EXISTS `drop.dim_country` (
    country_code STRING NOT NULL,
    country_name STRING,
    currency STRING,
    language STRING,
    population INT64,
    gdp_per_capita FLOAT64,
    cross_border_rate FLOAT64,
    mobile_payment_rate FLOAT64,
    ecommerce_penetration FLOAT64,
    pack_version STRING,
    latest_market_snapshot STRING,
    feature_vector_version STRING,
    warehouse_as_of TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP(),
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
OPTIONS (
    description = "Country dimension - canonical reference from country packs",
    require_partition_filter = FALSE
);

-- Ecosystem dimension
CREATE TABLE IF NOT EXISTS `drop.dim_ecosystem` (
    ecosystem_id STRING NOT NULL,
    ecosystem_name STRING,
    country_code STRING,
    installed_base INT64,
    installed_base_growth FLOAT64,
    replacement_pressure FLOAT64,
    avg_asset_age FLOAT64,
    warranty_expiry_wave FLOAT64,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
OPTIONS (
    description = "Ecosystem dimension - product categories within countries",
    require_partition_filter = FALSE
);

-- Product/SKU dimension
CREATE TABLE IF NOT EXISTS `drop.dim_product` (
    product_id STRING NOT NULL,
    product_family STRING,
    sku STRING,
    brand STRING,
    category STRING,
    subcategory STRING,
    eco_system STRING,
    country_code STRING,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
OPTIONS (
    description = "Product dimension - SKUs and product families",
    require_partition_filter = FALSE
);

-- Merchant dimension
CREATE TABLE IF NOT EXISTS `drop.dim_merchant` (
    merchant_id STRING NOT NULL,
    merchant_name STRING,
    country_code STRING,
    quality_score FLOAT64,
    is_good_seller BOOL,
    shipping_days INT64,
    has_local_payment BOOL,
    has_local_warranty BOOL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
OPTIONS (
    description = "Merchant dimension - sellers and their quality scores",
    require_partition_filter = FALSE
);

-- Supplier dimension
CREATE TABLE IF NOT EXISTS `drop.dim_supplier` (
    supplier_id STRING NOT NULL,
    supplier_name STRING,
    country_code STRING,
    ecosystem STRING,
    margin_pct FLOAT64,
    delivery_days INT64,
    moq INT64,
    has_dropship BOOL,
    has_api_feed BOOL,
    single_supplier_risk FLOAT64,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
OPTIONS (
    description = "Supplier dimension - supply chain entities",
    require_partition_filter = FALSE
);

-- Agent dimension
CREATE TABLE IF NOT EXISTS `drop.dim_agent` (
    agent_id STRING NOT NULL,
    agent_name STRING,
    agent_type STRING,
    model STRING,
    model_version STRING,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
OPTIONS (
    description = "Agent dimension - AI agents that make decisions",
    require_partition_filter = FALSE
);

-- Policy dimension
CREATE TABLE IF NOT EXISTS `drop.dim_policy` (
    policy_id STRING NOT NULL,
    policy_name STRING,
    policy_version STRING,
    policy_type STRING,
    description STRING,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
OPTIONS (
    description = "Policy dimension - decision-making policies",
    require_partition_filter = FALSE
);

-- =============================================================================
-- FACTS: Market Observations
-- =============================================================================

-- Market observation facts (from probes)
CREATE TABLE IF NOT EXISTS `drop.fact_market_observation` (
    observation_id STRING NOT NULL,
    observed_at TIMESTAMP NOT NULL,
    
    -- Dimensions
    country_code STRING,
    ecosystem STRING,
    product_family STRING,
    merchant_id STRING,
    supplier_id STRING,
    
    -- Observation data
    entity_type STRING,
    entity_id STRING,
    field_name STRING,
    field_value STRING,
    field_value_numeric FLOAT64,
    
    -- Source provenance
    source_type STRING,
    source_url STRING,
    source_grade STRING,
    source_name STRING,
    
    -- Independence tracking
    independence_cluster STRING,
    independent_source_count INT64,
    
    -- Metadata
    probe_id STRING,
    hypothesis_id STRING,
    candidate_id STRING,
    
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY DATE(observed_at)
CLUSTER BY country_code, ecosystem, entity_type
OPTIONS (
    description = "Market observation facts - atomic evidence from probes",
    require_partition_filter = FALSE
);

-- =============================================================================
-- FACTS: Decision Events (immutable audit trail)
-- =============================================================================

CREATE TABLE IF NOT EXISTS `drop.fact_decision_event` (
    event_id STRING NOT NULL,
    created_at TIMESTAMP NOT NULL,
    
    -- Agent/policy
    agent_id STRING,
    policy_id STRING,
    policy_version STRING,
    
    -- Context
    country_code STRING,
    ecosystem STRING,
    product_family STRING,
    candidate_id STRING,
    feature_snapshot_id STRING,
    
    -- Available actions
    available_actions ARRAY<STRING>,
    
    -- Chosen action
    chosen_action STRING,
    action_probability FLOAT64,  -- Propensity score
    
    -- Expected values
    expected_information_value FLOAT64,
    expected_cash_cost FLOAT64,
    expected_cm2 FLOAT64,
    
    -- Actual costs
    actual_cash_cost FLOAT64,
    actual_token_cost FLOAT64,
    actual_api_cost FLOAT64,
    actual_human_minutes FLOAT64,
    actual_wall_clock_seconds FLOAT64,
    
    -- Research metadata
    web_queries INT64,
    search_cost FLOAT64,
    api_calls INT64,
    
    -- Outcome
    decision_changed BOOL,
    hypothesis_affected STRING,
    downstream_experiment_ids ARRAY<STRING>,
    
    -- Quality
    result_quality STRING
)
PARTITION BY DATE(created_at)
CLUSTER BY country_code, ecosystem, chosen_action
OPTIONS (
    description = "Decision events - immutable audit trail of agent decisions",
    require_partition_filter = FALSE
);

-- =============================================================================
-- FACTS: Feature Snapshots (point-in-time, no leakage)
-- =============================================================================

CREATE TABLE IF NOT EXISTS `drop.fact_feature_snapshot` (
    snapshot_id STRING NOT NULL,
    as_of TIMESTAMP NOT NULL,
    
    -- Entity
    candidate_id STRING,
    country_code STRING,
    ecosystem STRING,
    
    -- Country features
    country_gdp_per_capita FLOAT64,
    country_cross_border_rate FLOAT64,
    country_mobile_payment_rate FLOAT64,
    country_purchasing_power FLOAT64,
    
    -- Installed base features
    installed_base INT64,
    installed_base_growth FLOAT64,
    replacement_share FLOAT64,
    avg_asset_age FLOAT64,
    warranty_expiry_wave FLOAT64,
    
    -- Search/demand features
    search_volume INT64,
    search_growth FLOAT64,
    cpc FLOAT64,
    cpc_growth FLOAT64,
    query_intent_score FLOAT64,
    
    -- Competition features
    seller_count INT64,
    good_seller_count INT64,
    merchant_quality_gap FLOAT64,
    price_dispersion FLOAT64,
    marketplace_dominance FLOAT64,
    
    -- Supply features
    supplier_margin FLOAT64,
    delivery_days FLOAT64,
    single_supplier_risk FLOAT64,
    return_risk_class STRING,
    
    -- Economics features
    aov FLOAT64,
    gross_margin_pct FLOAT64,
    source_target_gap FLOAT64,
    
    -- Localization features
    localization_score FLOAT64,
    local_payment_available BOOL,
    local_shipping_available BOOL,
    
    -- Historical performance
    previous_probes INT64,
    previous_falsifications INT64,
    historical_cm2 FLOAT64,
    
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY DATE(as_of)
CLUSTER BY country_code, ecosystem
OPTIONS (
    description = "Feature snapshots - point-in-time features for ML training (no leakage)",
    require_partition_filter = FALSE
);

-- =============================================================================
-- FACTS: Economic Outcomes (with maturity windows)
-- =============================================================================

CREATE TABLE IF NOT EXISTS `drop.fact_economic_outcome` (
    outcome_id STRING NOT NULL,
    experiment_id STRING,
    candidate_id STRING,
    country_code STRING,
    
    -- Maturity
    maturity STRING,  -- 1d, 7d, 30d, 60d, 90d
    
    -- Traffic
    impressions INT64,
    clicks INT64,
    ctr FLOAT64,
    cpc FLOAT64,
    
    -- Funnel
    atc INT64,
    `checkpoint` INT64,  -- checkout (reserved word)
    orders INT64,
    cvr FLOAT64,
    
    -- Economics
    revenue FLOAT64,
    cm0 FLOAT64,
    cm1 FLOAT64,
    cm2 FLOAT64,
    cm3 FLOAT64,
    
    -- Returns/reserves
    returns INT64,
    refunds FLOAT64,
    chargebacks INT64,
    warranty_claims INT64,
    return_reserve FLOAT64,
    warranty_reserve FLOAT64,
    chargeback_reserve FLOAT64,
    
    -- Timestamps
    experiment_start TIMESTAMP,
    outcome_observed_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP(),
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY DATE(outcome_observed_at)
CLUSTER BY country_code, experiment_id, maturity
OPTIONS (
    description = "Economic outcomes - experiment results with maturity windows",
    require_partition_filter = FALSE
);

-- =============================================================================
-- FACTS: Policy Actions (with propensity logging)
-- =============================================================================

CREATE TABLE IF NOT EXISTS `drop.fact_policy_action` (
    action_id STRING NOT NULL,
    created_at TIMESTAMP NOT NULL,
    
    -- Policy
    policy_id STRING,
    policy_version STRING,
    
    -- Context
    candidate_id STRING,
    country_code STRING,
    feature_snapshot_id STRING,
    
    -- Action set and choice
    available_actions ARRAY<STRING>,
    chosen_action STRING,
    chosen_action_probability FLOAT64,  -- Propensity
    
    -- Expected values
    expected_value FLOAT64,
    uncertainty FLOAT64,
    
    -- Actual outcome
    actual_value FLOAT64
)
PARTITION BY DATE(created_at)
CLUSTER BY country_code, policy_id
OPTIONS (
    description = "Policy actions - logged with propensity for offline policy evaluation",
    require_partition_filter = FALSE
);

-- =============================================================================
-- FACTS: Treatment Assignments
-- =============================================================================

CREATE TABLE IF NOT EXISTS `drop.fact_treatment_assignment` (
    assignment_id STRING NOT NULL,
    created_at TIMESTAMP NOT NULL,
    
    -- Experiment
    experiment_id STRING,
    candidate_id STRING,
    
    -- Randomization
    randomization_unit STRING,
    control STRING,
    treatment STRING,
    assignment_probability FLOAT64,
    actual_assignment STRING,
    
    -- Timing
    pre_period_start TIMESTAMP,
    pre_period_end TIMESTAMP,
    start TIMESTAMP,
    end TIMESTAMP,
    
    -- Measurement
    metric STRING,
    measurement_horizon_days INT64
)
OPTIONS (
    description = "Treatment assignments - randomized experiment assignments",
    require_partition_filter = FALSE
);

-- =============================================================================
-- FACTS: Cost Ledger (CM0-CM3 breakdown)
-- =============================================================================

CREATE TABLE IF NOT EXISTS `drop.fact_cost_ledger` (
    ledger_id STRING NOT NULL,
    created_at TIMESTAMP NOT NULL,
    
    -- Period
    period_start TIMESTAMP,
    period_end TIMESTAMP,
    
    -- Revenue
    gross_revenue FLOAT64,
    tax_collected FLOAT64,
    net_revenue FLOAT64,
    
    -- CM0: Product contribution costs
    cogs FLOAT64,
    supplier_freight FLOAT64,
    fulfilment FLOAT64,
    duty FLOAT64,
    payment_processing FLOAT64,
    refunds FLOAT64,
    return_shipping FLOAT64,
    warranty_reserve FLOAT64,
    chargeback_reserve FLOAT64,
    
    -- CM1: Acquisition costs
    paid_acquisition FLOAT64,
    affiliate_commissions FLOAT64,
    
    -- CM2: Automated operating costs
    ai_tokens FLOAT64,
    scraping_api FLOAT64,
    image_generation FLOAT64,
    agent_compute FLOAT64,
    per_order_software FLOAT64,
    
    -- CM3: Fully loaded costs
    domain_costs FLOAT64,
    software_costs FLOAT64,
    human_intervention FLOAT64,
    samples FLOAT64,
    setup_expenses FLOAT64,
    
    -- Calculated margins
    cm0 FLOAT64,
    cm0_margin FLOAT64,
    cm1 FLOAT64,
    cm1_margin FLOAT64,
    cm2 FLOAT64,
    cm2_margin FLOAT64,
    cm3 FLOAT64,
    cm3_margin FLOAT64,
    
    -- Context
    currency STRING,
    country_code STRING,
    experiment_id STRING
)
PARTITION BY DATE(created_at)
CLUSTER BY country_code, experiment_id
OPTIONS (
    description = "Cost ledger - complete CM0-CM3 breakdown for transactions",
    require_partition_filter = FALSE
);

-- =============================================================================
-- GRAPHS: Knowledge Graph (temporal view from BigQuery)
-- =============================================================================

CREATE TABLE IF NOT EXISTS `drop.graph_nodes` (
    node_id STRING NOT NULL,
    node_type STRING NOT NULL,
    properties_json STRING,
    confidence FLOAT64 DEFAULT 1.0,
    valid_from TIMESTAMP DEFAULT CURRENT_TIMESTAMP(),
    valid_to TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
OPTIONS (
    description = "Knowledge graph nodes - temporal view of entities",
    require_partition_filter = FALSE
);

CREATE TABLE IF NOT EXISTS `drop.graph_edges` (
    source_node STRING NOT NULL,
    target_node STRING NOT NULL,
    edge_type STRING NOT NULL,
    weight FLOAT64 DEFAULT 1.0,
    uncertainty FLOAT64 DEFAULT 0.0,
    evidence_coverage FLOAT64 DEFAULT 0.0,
    freshness FLOAT64 DEFAULT 1.0,
    source_snapshot STRING,
    valid_from TIMESTAMP DEFAULT CURRENT_TIMESTAMP(),
    valid_to TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
OPTIONS (
    description = "Knowledge graph edges - temporal relationships between entities",
    require_partition_filter = FALSE
);

CREATE TABLE IF NOT EXISTS `drop.graph_observations` (
    node_id STRING NOT NULL,
    observed_at TIMESTAMP NOT NULL,
    metric_name STRING NOT NULL,
    metric_value FLOAT64,
    evidence_type STRING,
    source STRING,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
)
PARTITION BY DATE(observed_at)
CLUSTER BY node_id, metric_name
OPTIONS (
    description = "Graph observations - time-series metrics on graph nodes",
    require_partition_filter = FALSE
);

-- =============================================================================
-- ML: Model predictions
-- =============================================================================

CREATE TABLE IF NOT EXISTS `drop.ml_predictions` (
    prediction_id STRING NOT NULL,
    created_at TIMESTAMP NOT NULL,
    model_name STRING,
    model_version STRING,
    
    -- Entity
    candidate_id STRING,
    country_code STRING,
    ecosystem STRING,
    
    -- Prediction
    prediction_type STRING,  -- "viability", "profit", "cpc", "cvr", etc.
    predicted_value FLOAT64,
    prediction_std FLOAT64,
    confidence_interval_lower FLOAT64,
    confidence_interval_upper FLOAT64,
    
    -- Feature snapshot used
    feature_snapshot_id STRING,
    
    -- Ground truth (filled later)
    actual_value FLOAT64,
    prediction_error FLOAT64
)
PARTITION BY DATE(created_at)
CLUSTER BY candidate_id, prediction_type
OPTIONS (
    description = "ML predictions - model outputs with uncertainty",
    require_partition_filter = FALSE
);

-- =============================================================================
-- EXPERIMENTS: Experiment tracking
-- =============================================================================

CREATE TABLE IF NOT EXISTS `drop.experiments` (
    experiment_id STRING NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP(),
    
    -- Design
    experiment_name STRING,
    hypothesis STRING,
    hypothesis_id STRING,
    
    -- Treatment
    treatment_type STRING,
    treatment_description STRING,
    control_description STRING,
    
    -- Randomization
    randomization_unit STRING,
    assignment_probability FLOAT64,
    
    -- Timing
    start_date DATE,
    end_date DATE,
    measurement_horizon_days INT64,
    
    -- Budget
    budget_cents INT64,
    actual_cost_cents INT64,
    
    -- Status
    status STRING,  -- "DESIGN", "RUNNING", "ANALYZED", "KILLED"
    
    -- Results
    winner STRING,  -- "treatment", "control", "inconclusive"
    p_value FLOAT64,
    confidence FLOAT64,
    
    -- Economic outcome
    treatment_cm2 FLOAT64,
    control_cm2 FLOAT64,
    incremental_cm2 FLOAT64
)
OPTIONS (
    description = "Experiments - A/B tests and probe outcomes",
    require_partition_filter = FALSE
);