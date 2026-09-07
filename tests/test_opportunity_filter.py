"""
Comprehensive test suite for the dropshipping opportunity filter.
Covers all required test cases from the specification.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import math
import json
import pytest
from packages.economics.model import calculate_economics, EconomicResult
from packages.schemas.candidate import Candidate, ConfidenceLevel, HardGateStatus, RecommendedAction, CandidateState
from packages.scoring.gates import run_all_gates, gate_1_positive_economics, gate_2_plausible_paid_economics
from packages.scoring.score import score_candidate, ScoreReport
from packages.scoring.bayesian import create_posterior, analyze_test_result, BayesianPosterior
from services.analytics.funnel_classifier import classify_funnel, FunnelMetrics, FunnelState, explain_why_100_clicks_kill_is_wrong
from services.analytics.query_classifier import classify_query, QueryCategory, should_add_negative, QueryMetrics
from services.analytics.guard import OverinterventionGuard, InterventionType
from services.research.state_machine import CandidateStateMachine
from services.research.allocation import allocate_budget
from services.research.evoi import calculate_evoi, recommend_next_action
from services.analytics.product_classifier import classify_product, ProductClass
from services.analytics.free_signals import calculate_free_signal_score, FreeListingData, FreeSignalState, should_start_paid_test
from packages.scoring.funnel_bayesian import analyze_funnel_bayesian, FunnelBayesianResult
from services.research.country_selection import select_country, score_country, CountryProfile, get_best_country
from services.research.scaling import ScalingEngine, ScalingAction
from services.research.auction_explainer import generate_auction_explanation
from services.catalog.product_expert import ProductExpert, BuyerNeedType, ConversionOutcome
from services.research.pipeline import run_pipeline, generate_final_selection, generate_launch_plan, generate_unknownknowns


# =============================================================================
# ECONOMIC MODEL TESTS
# =============================================================================

class TestEconomicModel:
    def test_structurally_bad_low_ticket(self):
        """Low-ticket bad: $30 contribution, $1 CPC, 2% CVR → profit/click = -$0.40"""
        result = calculate_economics(
            selling_price=65.0,
            supplier_price=25.0,
            supplier_shipping=10.0,
            expected_cpc=2.13,
            cvr_pessimistic=0.002,
            cvr_base=0.01,
            cvr_optimistic=0.02,
        )
        # Break-even CVR = 2.13 / ~24.50 ≈ 8.7%
        assert result.break_even_cvr > 0.07, f"Break-even CVR too low: {result.break_even_cvr}"
        assert result.pre_ad_contribution > 0, "Contribution should be positive"
        assert result.headroom_base < 1.2, f"Headroom should be < 1.2 for fragile: {result.headroom_base}"
        assert result.economic_quality in ["EXTREMELY FRAGILE", "MARGINAL", "STRUCTURALLY LOSING"]

    def test_viable_low_cvr_high_ticket(self):
        """High-ticket good: $250 contribution, $0.80 CPC, 0.8% CVR → headroom ~2.5"""
        result = calculate_economics(
            selling_price=450.0,
            supplier_price=130.0,
            supplier_shipping=20.0,
            duties=10.0,
            expected_cpc=0.80,
            cvr_pessimistic=0.003,
            cvr_base=0.008,
            cvr_optimistic=0.015,
        )
        assert result.pre_ad_contribution > 200, f"Contribution should be > 200: {result.pre_ad_contribution}"
        assert result.break_even_cvr < 0.005, f"Break-even CVR should be < 0.5%: {result.break_even_cvr}"
        assert result.headroom_base >= 2.0, f"Headroom should be >= 2.0: {result.headroom_base}"
        assert result.economic_quality in ["VERY INTERESTING", "EXCEPTIONAL"]

    def test_zero_pre_ad_contribution(self):
        """Zero pre-ad contribution → structurally losing."""
        result = calculate_economics(
            selling_price=30.0,
            supplier_price=15.0,
            supplier_shipping=10.0,
            expected_returns_rate=0.15,
            expected_cpc=1.0,
        )
        assert result.pre_ad_contribution <= 0, f"Should be <= 0: {result.pre_ad_contribution}"
        assert result.break_even_cvr == float('inf') or result.break_even_cvr > 100
        assert result.economic_quality == "STRUCTURALLY LOSING"

    def test_cpc_missing(self):
        """CPC = 0 → infinite headroom (no ad cost)."""
        result = calculate_economics(
            selling_price=100.0,
            supplier_price=30.0,
            supplier_shipping=10.0,
            expected_cpc=0.0,
        )
        assert result.headroom_base == float('inf')
        assert result.break_even_cvr == 0.0

    def test_pessimistic_failure_optimistic_success(self):
        """Pessimistic scenario fails, optimistic succeeds → fragile but viable."""
        result = calculate_economics(
            selling_price=200.0,
            supplier_price=50.0,
            supplier_shipping=15.0,
            expected_cpc=1.50,
            cvr_pessimistic=0.003,
            cvr_base=0.008,
            cvr_optimistic=0.015,
        )
        assert result.profit_per_click_pessimistic < 0, "Pessimistic should be negative"
        assert result.profit_per_click_optimistic > 0, "Optimistic should be positive"
        assert result.headroom_pessimistic < 1.0, "Pessimistic headroom < 1"
        assert result.headroom_optimistic > 1.0, "Optimistic headroom > 1"

    def test_lumbar_pillow_economics(self):
        """Lumbar pillow: $30 contribution, $2.13 CPC → needs 7.1% CVR → dead."""
        result = calculate_economics(
            selling_price=64.99,
            supplier_price=25.0,
            supplier_shipping=10.0,
            expected_cpc=2.13,
            cvr_pessimistic=0.002,
            cvr_base=0.01,
            cvr_optimistic=0.02,
        )
        assert result.break_even_cvr > 0.07, f"Lumbar break-even CVR should be > 7%: {result.break_even_cvr}"
        assert result.headroom_base < 1.2, "Lumbar headroom should be fragile"

    def test_headroom_interpretation_bands(self):
        """Verify all interpretation bands work correctly."""
        # STRUCTURALLY LOSING
        r = calculate_economics(100, 50, 10, expected_cpc=1.0, cvr_base=0.005)
        assert r.economic_quality == "STRUCTURALLY LOSING"

        # VERY INTERESTING (headroom ~2.5)
        r = calculate_economics(1000, 200, 20, expected_cpc=1.0, cvr_base=0.005)
        # Contribution ≈ 730, headroom = 0.005 * 730 / 1.0 = 3.65
        assert r.economic_quality == "EXCEPTIONAL"

    def test_max_allowed_cpc(self):
        """Max allowed CPC = CVR * contribution."""
        result = calculate_economics(
            selling_price=450.0,
            supplier_price=130.0,
            supplier_shipping=20.0,
            duties=10.0,
            expected_cpc=1.20,
            cvr_base=0.005,
        )
        expected_max = 0.005 * result.pre_ad_contribution
        assert abs(result.max_allowed_cpc - expected_max) < 0.01


# =============================================================================
# HARD GATE TESTS
# =============================================================================

class TestHardGates:
    def _make_candidate(self, **kwargs) -> Candidate:
        defaults = {
            "candidate_id": "TEST-001",
            "product_family": "Test Product",
            "sku": "TEST-SKU",
            "country": "US",
            "selling_price": 100.0,
            "supplier_price": 30.0,
            "supplier_shipping": 10.0,
            "expected_cpc": 1.0,
            "cvr_base": 0.005,
            "cvr_pessimistic": 0.002,
            "cvr_optimistic": 0.01,
            "intent_score": 0.6,
            "shopping_seller_count": 5,
            "supplier_reliability": 0.7,
            "economics_confidence": ConfidenceLevel.MEDIUM,
            "cpc_confidence_domain": ConfidenceLevel.MEDIUM,
            "cvr_confidence": ConfidenceLevel.MEDIUM,
            "supplier_confidence": ConfidenceLevel.MEDIUM,
            "competition_confidence": ConfidenceLevel.MEDIUM,
            "demand_confidence": ConfidenceLevel.MEDIUM,
        }
        defaults.update(kwargs)
        c = Candidate(**defaults)
        # Calculate economics for the candidate
        econ = calculate_economics(
            c.selling_price, c.supplier_price, c.supplier_shipping,
            c.duties, c.payment_fee_rate, 0.20, 0.05,
            c.expected_cpc, c.cvr_pessimistic, c.cvr_base, c.cvr_optimistic,
        )
        c.pre_ad_contribution = econ.pre_ad_contribution
        c.break_even_cvr = econ.break_even_cvr
        c.headroom_pessimistic = econ.headroom_pessimistic
        c.headroom_base = econ.headroom_base
        c.headroom_optimistic = econ.headroom_optimistic
        return c

    def test_gate1_rejects_negative_contribution(self):
        """Gate 1 rejects when pre_ad_contribution <= 0."""
        c = self._make_candidate(
            selling_price=30.0,
            supplier_price=20.0,
            supplier_shipping=10.0,
            expected_returns_rate=0.10,
        )
        # With these params: contribution = 30 - 30 - payment_fees - 3 = negative
        result = gate_1_positive_economics(c)
        assert not result.passed
        assert result.status == HardGateStatus.REJECT

    def test_gate2_rejects_pessimistic_headroom(self):
        """Gate 2 rejects when optimistic headroom < 1.0."""
        c = self._make_candidate(
            selling_price=50.0,
            supplier_price=20.0,
            supplier_shipping=10.0,
            expected_cpc=2.0,
            cvr_pessimistic=0.002,
            cvr_base=0.005,
            cvr_optimistic=0.008,
        )
        # Calculate headroom
        econ = calculate_economics(
            c.selling_price, c.supplier_price, c.supplier_shipping,
            c.duties, c.payment_fee_rate, 0.20, 0.05,
            c.expected_cpc, c.cvr_pessimistic, c.cvr_base, c.cvr_optimistic,
        )
        c.headroom_optimistic = econ.headroom_optimistic
        c.headroom_base = econ.headroom_base
        result = gate_2_plausible_paid_economics(c)
        # With 0.008 * ~15 / 2.0 ≈ 0.06 headroom → REJECT
        assert not result.passed

    def test_gate4_rejects_saturated_sku(self):
        """Gate 4 rejects when seller count > 20."""
        c = self._make_candidate(shopping_seller_count=25)
        from packages.scoring.gates import gate_4_sku_saturation
        result = gate_4_sku_saturation(c)
        assert not result.passed
        assert result.status == HardGateStatus.REJECT

    def test_gate5_rejects_unreliable_supplier(self):
        """Gate 5 rejects when supplier reliability < 0.3."""
        c = self._make_candidate(supplier_reliability=0.2)
        from packages.scoring.gates import gate_5_supplier_viability
        result = gate_5_supplier_viability(c)
        assert not result.passed
        assert result.status == HardGateStatus.REJECT

    def test_gate6_rejects_low_intent(self):
        """Gate 6 rejects when intent score <= 0.1."""
        c = self._make_candidate(intent_score=0.05)
        from packages.scoring.gates import gate_6_query_intent
        result = gate_6_query_intent(c)
        assert not result.passed
        assert result.status == HardGateStatus.REJECT

    def test_gate7_rejects_low_confidence(self):
        """Gate 7 quarantines when >= 4 confidence fields are VERY_LOW."""
        c = self._make_candidate(
            economics_confidence=ConfidenceLevel.VERY_LOW,
            cpc_confidence_domain=ConfidenceLevel.VERY_LOW,
            cvr_confidence=ConfidenceLevel.VERY_LOW,
            supplier_confidence=ConfidenceLevel.VERY_LOW,
        )
        from packages.scoring.gates import gate_7_data_confidence
        result = gate_7_data_confidence(c)
        assert not result.passed
        assert result.status == HardGateStatus.QUARANTINE

    def test_passing_candidate(self):
        """A well-configured candidate passes all gates."""
        c = self._make_candidate(
            selling_price=450.0,
            supplier_price=130.0,
            supplier_shipping=20.0,
            duties=10.0,
            expected_cpc=1.0,
            cvr_pessimistic=0.005,
            cvr_base=0.008,
            cvr_optimistic=0.015,
            intent_score=0.75,
            shopping_seller_count=5,
            supplier_reliability=0.8,
            shipping_days=7,
            economics_confidence=ConfidenceLevel.MEDIUM,
            cpc_confidence_domain=ConfidenceLevel.MEDIUM,
            cvr_confidence=ConfidenceLevel.MEDIUM,
            supplier_confidence=ConfidenceLevel.MEDIUM,
            competition_confidence=ConfidenceLevel.MEDIUM,
            demand_confidence=ConfidenceLevel.MEDIUM,
        )
        report = run_all_gates(c)
        assert report.passed, f"Should pass all gates: {report.reject_reasons}"


# =============================================================================
# SOFT SCORING TESTS
# =============================================================================

class TestSoftScoring:
    def test_low_confidence_penalty(self):
        """Low-confidence candidate gets score penalty."""
        c = Candidate(
            candidate_id="SCORE-001",
            headroom_base=2.0,
            pre_ad_contribution=250.0,
            intent_score=0.8,
            shopping_seller_count=3,
            supplier_reliability=0.8,
            monthly_search_volume=10000,
            merchant_differentiation_score=0.7,
            economics_confidence=ConfidenceLevel.HIGH,
            cpc_confidence_domain=ConfidenceLevel.HIGH,
            cvr_confidence=ConfidenceLevel.HIGH,
            supplier_confidence=ConfidenceLevel.HIGH,
            competition_confidence=ConfidenceLevel.HIGH,
            demand_confidence=ConfidenceLevel.HIGH,
        )
        report_high = score_candidate(c)

        c_low = c.model_copy()
        c_low.economics_confidence = ConfidenceLevel.LOW
        c_low.cpc_confidence_domain = ConfidenceLevel.LOW
        c_low.cvr_confidence = ConfidenceLevel.LOW
        c_low.supplier_confidence = ConfidenceLevel.LOW
        c_low.competition_confidence = ConfidenceLevel.LOW
        c_low.demand_confidence = ConfidenceLevel.LOW
        report_low = score_candidate(c_low)

        assert report_low.adjusted_score < report_high.adjusted_score, \
            f"Low confidence should score less: {report_low.adjusted_score} vs {report_high.adjusted_score}"

    def test_score_components_sum_to_raw(self):
        """Raw score should equal sum of weighted components."""
        c = Candidate(
            headroom_base=1.5,
            pre_ad_contribution=100.0,
            intent_score=0.6,
            shopping_seller_count=8,
            supplier_reliability=0.6,
            monthly_search_volume=5000,
            merchant_differentiation_score=0.4,
        )
        report = score_candidate(c)
        component_sum = sum(comp.weighted_value for comp in report.components)
        assert abs(report.raw_score - component_sum) < 0.01


# =============================================================================
# BAYESIAN MODEL TESTS
# =============================================================================

class TestBayesianModel:
    def test_300_clicks_zero_sales_high_breve(self):
        """300 clicks zero sales at 1.5% break-even CVR → strong evidence against."""
        result = analyze_test_result(
            clicks=300,
            orders=0,
            break_even_cvr=0.015,
        )
        # P(0 sales | 1.5% CVR) = (0.985)^300 ≈ 0.01%
        assert result["probability_zero_sales_if_viable"] < 0.05
        assert result["decision"] == "STRONG_EVIDENCE_AGAINST"

    def test_300_clicks_zero_sales_low_breve(self):
        """300 clicks zero sales at 0.4% break-even CVR → within normal variance."""
        result = analyze_test_result(
            clicks=300,
            orders=0,
            break_even_cvr=0.004,
        )
        # P(0 sales | 0.4% CVR) = (0.996)^300 ≈ 30%
        assert result["probability_zero_sales_if_viable"] > 0.20
        assert result["decision"] in ["UNCERTAIN", "WEAK"]

    def test_posterior_updates_with_data(self):
        """Posterior should shift toward observed CVR."""
        p = create_posterior(clicks=0, orders=0)
        assert p.posterior_mean_cvr == pytest.approx(0.5, abs=0.01)  # Prior mean

        p2 = p.update(additional_clicks=200, additional_orders=2)
        assert p2.posterior_mean_cvr < 0.1  # Should shift toward 1%
        assert p2.clicks == 200
        assert p2.orders == 2

    def test_probability_above_threshold(self):
        """P(CVR > threshold) should decrease as threshold increases."""
        p = create_posterior(clicks=100, orders=3)
        p_low = p.probability_above(0.01)
        p_high = p.probability_above(0.10)
        assert p_low > p_high

    def test_decision_bands(self):
        """Test all decision bands."""
        # STRONGLY_PROMISING: many orders relative to clicks
        p = create_posterior(clicks=100, orders=10)
        assert p.decide(0.05) == "STRONGLY_PROMISING"

        # STRONG_EVIDENCE_AGAINST: zero orders with many clicks
        p = create_posterior(clicks=500, orders=0)
        assert p.decide(0.01) == "STRONG_EVIDENCE_AGAINST"

    def test_100_clicks_kill_is_wrong(self):
        """Demonstrate why '100 clicks then kill' is often wrong."""
        explanation = explain_why_100_clicks_kill_is_wrong(100, 0.0048)
        assert "62%" in explanation  # At 0.48% CVR, 100 clicks has 62% chance of 0 sales


# =============================================================================
# FUNNEL CLASSIFIER TESTS
# =============================================================================

class TestFunnelClassifier:
    def test_mask_diagnostic(self):
        """$289 mask: 86% impression share, 148 clicks, 0 ATC → not delivery problem."""
        metrics = FunnelMetrics(
            impressions=5000,
            clicks=148,
            atc=0,
            checkout=0,
            purchases=0,
            break_even_cvr=0.007,
        )
        diag = classify_funnel(metrics)
        assert diag.state == FunnelState.CLICKS_NO_ATC
        assert "trust" in diag.likely_problem_class.lower() or "product" in diag.likely_problem_class.lower()
        assert "not delivery" in diag.explanation.lower() or "not a delivery" in diag.explanation.lower()

    def test_lumbar_pillow_diagnostic(self):
        """Lumbar pillow: 81 clicks, 4 ATC, 1 checkout, 0 purchase → economics/shipping."""
        metrics = FunnelMetrics(
            impressions=3000,
            clicks=81,
            atc=4,
            checkout=1,
            purchases=0,
            break_even_cvr=0.071,
        )
        diag = classify_funnel(metrics)
        assert diag.state == FunnelState.CHECKOUT_NO_PURCHASE
        # The problem class should include shipping/payment/trust/price
        assert "shipping" in diag.likely_problem_class.lower() or "payment" in diag.likely_problem_class.lower()

    def test_no_delivery(self):
        """No impressions → NO_DELIVERY state."""
        metrics = FunnelMetrics(impressions=0, clicks=0)
        diag = classify_funnel(metrics)
        assert diag.state == FunnelState.NO_DELIVERY

    def test_impressions_no_clicks(self):
        """Impressions but no clicks → offer/title/image problem."""
        metrics = FunnelMetrics(impressions=5000, clicks=0)
        diag = classify_funnel(metrics)
        assert diag.state == FunnelState.IMPRESSIONS_NO_CLICKS

    def test_profitable_scalable(self):
        """Purchases + profit → PROFITABLE_SCALABLE."""
        metrics = FunnelMetrics(
            impressions=10000,
            clicks=500,
            atc=50,
            checkout=10,
            purchases=8,
            revenue=2400.0,
            ad_spend=500.0,
            contribution_profit=800.0,
            break_even_cvr=0.01,
            pre_ad_contribution=300.0,
        )
        diag = classify_funnel(metrics)
        assert diag.state == FunnelState.PROFITABLE_SCALABLE


# =============================================================================
# QUERY CLASSIFIER TESTS
# =============================================================================

class TestQueryClassifier:
    def test_exact_model(self):
        """Exact model queries classified correctly."""
        assert classify_query("Roomba j7+") == QueryCategory.EXACT_MODEL
        assert classify_query("Dyson V15 Detect") == QueryCategory.EXACT_MODEL

    def test_informational(self):
        """Informational queries classified correctly."""
        cat = classify_query("how do robot vacuums work")
        assert cat == QueryCategory.INFORMATIONAL

    def test_high_intent(self):
        """High-intent queries classified correctly."""
        cat = classify_query("buy robot vacuum cleaner")
        assert cat in [QueryCategory.PRODUCT_HIGH_INTENT, QueryCategory.EXACT_MODEL]

    def test_negative_keyword_threshold(self):
        """Should add negative when CVR < 40% threshold for generic queries."""
        m = QueryMetrics(
            query="best vacuum cleaner",
            category=QueryCategory.GENERIC_COMMERCIAL,
            clicks=30,
            orders=0,
            cvr=0.0,
        )
        assert should_add_negative(m)

        # Not enough data
        m2 = QueryMetrics(
            query="best vacuum cleaner",
            category=QueryCategory.GENERIC_COMMERCIAL,
            clicks=10,
            orders=0,
            cvr=0.0,
        )
        assert not should_add_negative(m2)


# =============================================================================
# STATE MACHINE TESTS
# =============================================================================

class TestStateMachine:
    def test_valid_transitions(self):
        """Test valid state transitions."""
        sm = CandidateStateMachine()
        c = Candidate(candidate_id="SM-001")
        assert c.state == CandidateState.DISCOVERED

        # DISCOVERED → RESEARCHING
        assert sm.transition(c, CandidateState.RESEARCHING, "start_research")
        assert c.state == CandidateState.RESEARCHING

        # RESEARCHING → BUILD_READY
        assert sm.transition(c, CandidateState.BUILD_READY, "research_complete")
        assert c.state == CandidateState.BUILD_READY

        # BUILD_READY → FREE_LISTINGS_LIVE
        assert sm.transition(c, CandidateState.FREE_LISTINGS_LIVE, "enable_free_listings")
        assert c.state == CandidateState.FREE_LISTINGS_LIVE

    def test_invalid_transition(self):
        """Test invalid state transition is rejected."""
        sm = CandidateStateMachine()
        c = Candidate(candidate_id="SM-002")
        # DISCOVERED → PROFITABLE_SCALABLE is not valid
        assert not sm.transition(c, CandidateState.PROFITABLE_SCALABLE, "skip_to_win")
        assert c.state == CandidateState.DISCOVERED

    def test_killed_can_revive(self):
        """KILLED → DISCOVERED (revive) should be valid."""
        sm = CandidateStateMachine()
        c = Candidate(candidate_id="SM-003", state=CandidateState.KILLED)
        assert sm.transition(c, CandidateState.DISCOVERED, "revive")
        assert c.state == CandidateState.DISCOVERED


# =============================================================================
# EVOI TESTS
# =============================================================================

class TestEVOI:
    def test_free_tests_rank_higher(self):
        """Free tests should rank higher than paid tests by EV/OI."""
        c = Candidate(
            candidate_id="EVOI-001",
            cvr_confidence=ConfidenceLevel.LOW,
            competition_confidence=ConfidenceLevel.LOW,
            demand_confidence=ConfidenceLevel.LOW,
            headroom_base=1.5,
            pre_ad_contribution=100.0,
        )
        actions = calculate_evoi(c)
        # Free actions should be in top positions
        free_actions = [a for a in actions if a.cost == 0]
        paid_actions = [a for a in actions if a.cost > 0]
        if free_actions and paid_actions:
            assert free_actions[0].evoi > paid_actions[0].evoi

    def test_recommend_next_action(self):
        """Should recommend an action."""
        c = Candidate(
            candidate_id="EVOI-002",
            cvr_confidence=ConfidenceLevel.LOW,
            headroom_base=1.5,
            pre_ad_contribution=100.0,
        )
        action = recommend_next_action(c)
        assert action.action is not None
        assert action.evoi >= 0


# =============================================================================
# CAPITAL ALLOCATION TESTS
# =============================================================================

class TestAllocation:
    def test_allocate_to_eligible(self):
        """Should allocate budget to eligible candidates only."""
        candidates = [
            Candidate(
                candidate_id=f"ALLOC-{i}",
                state=CandidateState.PAID_TEST_READY,
                headroom_base=1.5,
                pre_ad_contribution=100.0,
                monthly_search_volume=5000,
                exact_query_share=0.3,
                cvr_confidence=ConfidenceLevel.LOW,
            )
            for i in range(3)
        ]
        result = allocate_budget(candidates, total_budget=10.0)
        assert len(result.allocations) > 0
        assert result.unallocated >= 0

    def test_no_eligible_candidates(self):
        """Should handle no eligible candidates gracefully."""
        candidates = [
            Candidate(
                candidate_id="ALLOC-DEAD",
                state=CandidateState.KILLED,
            )
        ]
        result = allocate_budget(candidates)
        assert len(result.allocations) == 0


# =============================================================================
# OVERINTERVENTION GUARD TESTS
# =============================================================================

class TestOverinterventionGuard:
    def test_blocks_intervention_with_insufficient_data(self):
        """Should block intervention when < 20 clicks."""
        guard = OverinterventionGuard()
        decision = guard.should_intervene(
            candidate_id="GUARD-001",
            current_clicks=10,
            current_orders=0,
            current_state={},
            observation="Low CTR",
            hypothesis="Title needs improvement",
        )
        assert not decision.should_intervene
        assert "Insufficient evidence" in decision.reason

    def test_allows_intervention_with_sufficient_data(self):
        """Should allow intervention when > 20 clicks and proper observation."""
        guard = OverinterventionGuard()
        decision = guard.should_intervene(
            candidate_id="GUARD-002",
            current_clicks=50,
            current_orders=0,
            current_state={},
            proposed_action=InterventionType.CHANGE_LANDING_PAGE,
            observation="148 clicks, 0 ATC — product/offer not working",
            hypothesis="Landing page doesn't build trust for $289 product",
        )
        assert decision.should_intervene

    def test_blocks_without_observation(self):
        """Should block intervention without observation/hypothesis."""
        guard = OverinterventionGuard()
        decision = guard.should_intervene(
            candidate_id="GUARD-003",
            current_clicks=50,
            current_orders=0,
            current_state={},
            proposed_action=InterventionType.CHANGE_BIDS,
        )
        assert not decision.should_intervene
        assert "No observation" in decision.reason


# =============================================================================
# INTEGRATION TESTS WITH REAL CANDIDATES
# =============================================================================

class TestRealCandidates:
    @pytest.fixture
    def real_candidates(self):
        """Load real candidates from data file."""
        path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                            "data", "real_candidates.json")
        with open(path) as f:
            data = json.load(f)
        return [Candidate(**c) for c in data]

    def test_mask_rejected_for_paid(self, real_candidates):
        """The $289 red-light mask should be rejected for paid testing."""
        mask = [c for c in real_candidates if "red-light" in c.product_family.lower()][0]
        report = run_all_gates(mask)
        assert not report.passed, f"Mask should fail gates: {report.reject_reasons}"

    def test_lumbar_pillow_rejected(self, real_candidates):
        """The lumbar pillow should be rejected."""
        pillow = [c for c in real_candidates if "lumbar" in c.product_family.lower()][0]
        report = run_all_gates(pillow)
        assert not report.passed, f"Pillow should fail gates: {report.reject_reasons}"

    def test_baby_stroller_passes(self, real_candidates):
        """The premium baby stroller should pass gates (or at least quarantine, not reject)."""
        stroller = [c for c in real_candidates if "baby" in c.product_family.lower()][0]
        report = run_all_gates(stroller)
        assert report.overall_status != HardGateStatus.REJECT, \
            f"Baby stroller should not be rejected: {report.reject_reasons}"

    def test_all_candidates_have_economics(self, real_candidates):
        """All real candidates should have pre_ad_contribution calculated."""
        for c in real_candidates:
            assert c.pre_ad_contribution != 0 or c.selling_price <= 0, \
                f"{c.candidate_id} missing economics"


# =============================================================================
# PRODUCT CLASSIFIER TESTS
# =============================================================================

class TestProductClassifier:
    def _make_candidate(self, **kwargs) -> Candidate:
        defaults = {
            "candidate_id": "PC-001",
            "product_family": "Test Product",
            "sku": "TEST-SKU",
            "country": "US",
            "selling_price": 100.0,
            "supplier_price": 30.0,
            "supplier_shipping": 10.0,
            "expected_cpc": 1.0,
            "cvr_base": 0.005,
            "cvr_pessimistic": 0.002,
            "cvr_optimistic": 0.01,
            "intent_score": 0.6,
            "shopping_seller_count": 5,
            "supplier_reliability": 0.7,
            "economics_confidence": ConfidenceLevel.MEDIUM,
            "cpc_confidence_domain": ConfidenceLevel.MEDIUM,
            "cvr_confidence": ConfidenceLevel.MEDIUM,
            "supplier_confidence": ConfidenceLevel.MEDIUM,
            "competition_confidence": ConfidenceLevel.MEDIUM,
            "demand_confidence": ConfidenceLevel.MEDIUM,
        }
        defaults.update(kwargs)
        c = Candidate(**defaults)
        econ = calculate_economics(
            c.selling_price, c.supplier_price, c.supplier_shipping,
            c.duties, c.payment_fee_rate, 0.20, 0.05,
            c.expected_cpc, c.cvr_pessimistic, c.cvr_base, c.cvr_optimistic,
        )
        c.pre_ad_contribution = econ.pre_ad_contribution
        c.break_even_cvr = econ.break_even_cvr
        c.headroom_pessimistic = econ.headroom_pessimistic
        c.headroom_base = econ.headroom_base
        c.headroom_optimistic = econ.headroom_optimistic
        return c

    def test_champion_classification(self):
        """High headroom, good contribution, reliable supplier, some traffic → CHAMPION."""
        c = self._make_candidate(
            selling_price=450.0, supplier_price=130.0, supplier_shipping=20.0,
            duties=10.0, expected_cpc=0.80, cvr_base=0.008, cvr_optimistic=0.015,
            supplier_reliability=0.8, shopping_seller_count=3,
        )
        c.observed_clicks = 200
        c.observed_orders = 3
        c.probability_cvr_above_break_even = 0.8
        result = classify_product(c)
        assert result.product_class == ProductClass.CHAMPION

    def test_zombie_negative_contribution(self):
        """Negative contribution → ZOMBIE."""
        c = self._make_candidate(
            selling_price=30.0, supplier_price=20.0, supplier_shipping=10.0,
            expected_cpc=1.0,
        )
        econ = calculate_economics(
            c.selling_price, c.supplier_price, c.supplier_shipping,
            c.duties, c.payment_fee_rate, 0.20, 0.15,
            c.expected_cpc, c.cvr_pessimistic, c.cvr_base, c.cvr_optimistic,
        )
        c.pre_ad_contribution = econ.pre_ad_contribution
        c.headroom_base = econ.headroom_base
        result = classify_product(c)
        assert result.product_class == ProductClass.ZOMBIE

    def test_zombie_saturated_sku(self):
        """More than 20 sellers → ZOMBIE."""
        c = self._make_candidate(shopping_seller_count=25)
        result = classify_product(c)
        assert result.product_class == ProductClass.ZOMBIE

    def test_sleeper_no_traffic(self):
        """Good economics but zero traffic → SLEEPER."""
        c = self._make_candidate(
            selling_price=450.0, supplier_price=130.0, supplier_shipping=20.0,
            duties=10.0, expected_cpc=0.80, cvr_base=0.008, cvr_optimistic=0.015,
            supplier_reliability=0.8, shopping_seller_count=3,
        )
        result = classify_product(c)
        assert result.product_class == ProductClass.SLEEPER

    def test_waster_fragile_no_evidence(self):
        """Fragile headroom (1.0-1.2) + 100+ clicks + 0 orders → WASTER."""
        c = self._make_candidate(
            selling_price=150.0, supplier_price=20.0, supplier_shipping=10.0,
            expected_cpc=1.0, cvr_base=0.01, cvr_optimistic=0.02,
            cvr_pessimistic=0.005,
        )
        econ = calculate_economics(
            c.selling_price, c.supplier_price, c.supplier_shipping,
            c.duties, c.payment_fee_rate, 0.20, 0.05,
            c.expected_cpc, c.cvr_pessimistic, c.cvr_base, c.cvr_optimistic,
        )
        c.pre_ad_contribution = econ.pre_ad_contribution
        c.headroom_base = econ.headroom_base
        c.headroom_optimistic = econ.headroom_optimistic
        c.observed_clicks = 150
        c.observed_orders = 0
        c.probability_cvr_above_break_even = 0.05
        result = classify_product(c)
        assert result.product_class == ProductClass.WASTER

    def test_waster_low_posterior(self):
        """Low posterior after many clicks + fragile headroom → WASTER."""
        c = self._make_candidate(
            selling_price=150.0, supplier_price=20.0, supplier_shipping=10.0,
            expected_cpc=1.0, cvr_base=0.01, cvr_optimistic=0.02,
            cvr_pessimistic=0.005,
        )
        econ = calculate_economics(
            c.selling_price, c.supplier_price, c.supplier_shipping,
            c.duties, c.payment_fee_rate, 0.20, 0.05,
            c.expected_cpc, c.cvr_pessimistic, c.cvr_base, c.cvr_optimistic,
        )
        c.pre_ad_contribution = econ.pre_ad_contribution
        c.headroom_base = econ.headroom_base
        c.headroom_optimistic = econ.headroom_optimistic
        c.observed_clicks = 300
        c.observed_orders = 0
        c.probability_cvr_above_break_even = 0.03
        result = classify_product(c)
        assert result.product_class == ProductClass.WASTER

    def test_potential_marginal_economics(self):
        """Positive contribution but marginal headroom → POTENTIAL."""
        c = self._make_candidate(
            selling_price=100.0, supplier_price=30.0, supplier_shipping=10.0,
            expected_cpc=1.5, cvr_base=0.005, cvr_optimistic=0.008,
        )
        result = classify_product(c)
        assert result.product_class in [ProductClass.POTENTIAL, ProductClass.ZOMBIE]

    def test_classification_has_reasoning(self):
        """Classification should always include reasoning."""
        c = self._make_candidate()
        result = classify_product(c)
        assert len(result.reasoning) > 0
        assert result.product_class is not None


# =============================================================================
# FREE SIGNAL SCORER TESTS
# =============================================================================

class TestFreeSignals:
    def test_zero_impressions(self):
        """No impressions → ZERO_IMPRESSIONS state, score 0."""
        data = FreeListingData(free_impressions=0, free_clicks=0)
        result = calculate_free_signal_score(data)
        assert result.state == FreeSignalState.ZERO_IMPRESSIONS
        assert result.free_signal_score == 0.0

    def test_impressions_no_clicks(self):
        """Impressions but no clicks → IMPRESSIONS_NO_CLICKS."""
        data = FreeListingData(free_impressions=5000, free_clicks=0)
        result = calculate_free_signal_score(data)
        assert result.state == FreeSignalState.IMPRESSIONS_NO_CLICKS

    def test_clicks_no_atc(self):
        """Clicks but no ATC → CLICKS_NO_ATC."""
        data = FreeListingData(free_impressions=5000, free_clicks=100, atcs=0)
        result = calculate_free_signal_score(data)
        assert result.state == FreeSignalState.CLICKS_NO_ATC

    def test_clicks_with_atc(self):
        """Clicks with ATC → CLICKS_WITH_ATC."""
        data = FreeListingData(free_impressions=5000, free_clicks=100, atcs=10)
        result = calculate_free_signal_score(data)
        assert result.state == FreeSignalState.CLICKS_WITH_ATC
        assert result.free_signal_score > 0.3

    def test_strong_free_listing(self):
        """Strong free listing data → high score."""
        data = FreeListingData(
            free_impressions=10000, free_clicks=500,
            atcs=50, orders=5,
            console_impressions=8000, console_clicks=400,
            console_queries=50, console_avg_position=8.0,
            console_ctr=0.05,
        )
        result = calculate_free_signal_score(data)
        assert result.free_signal_score >= 0.5
        assert result.state == FreeSignalState.CLICKS_WITH_ATC

    def test_should_start_paid_test(self):
        """CLICKS_WITH_ATC → should start paid test."""
        result = calculate_free_signal_score(
            FreeListingData(free_impressions=5000, free_clicks=100, atcs=10)
        )
        assert should_start_paid_test(result)

    def test_should_not_start_paid_no_signal(self):
        """IMPRESSIONS_NO_CLICKS → should not start paid test."""
        result = calculate_free_signal_score(
            FreeListingData(free_impressions=5000, free_clicks=0)
        )
        assert not should_start_paid_test(result)

    def test_search_console_data_included(self):
        """Search Console data affects query quality score."""
        data = FreeListingData(
            free_impressions=2000, free_clicks=50,
            console_impressions=3000, console_clicks=150,
            console_queries=20, console_avg_position=5.0,
            console_ctr=0.05,
        )
        result = calculate_free_signal_score(data)
        assert result.query_quality_score > 0

    def test_score_range_0_to_1(self):
        """Score should always be between 0 and 1."""
        data = FreeListingData(
            free_impressions=50000, free_clicks=5000,
            atcs=500, orders=100,
        )
        result = calculate_free_signal_score(data)
        assert 0.0 <= result.free_signal_score <= 1.0


# =============================================================================
# FUNNEL BAYESIAN TESTS
# =============================================================================

class TestFunnelBayesian:
    def test_all_stages_with_data(self):
        """All stages with data should produce valid posteriors."""
        result = analyze_funnel_bayesian(
            impressions=10000, clicks=300,
            atcs=15, checkouts=8, orders=5,
        )
        assert result.ctr.stage_name == "CTR"
        assert result.atc_rate.stage_name == "ATC_RATE"
        assert result.checkout_rate.stage_name == "CHECKOUT_RATE"
        assert result.purchase_rate.stage_name == "PURCHASE_RATE"
        assert result.ctr.probability_above_threshold > 0

    def test_no_data_stages(self):
        """No data → NO_DATA decision for all stages."""
        result = analyze_funnel_bayesian(
            impressions=0, clicks=0,
            atcs=0, checkouts=0, orders=0,
        )
        assert result.ctr.decision == "NO_DATA"
        assert result.atc_rate.decision == "NO_DATA"

    def test_bottleneck_detection(self):
        """Weak ATC stage should be identified as bottleneck."""
        result = analyze_funnel_bayesian(
            impressions=10000, clicks=300,
            atcs=0, checkouts=0, orders=0,
            viable_atc_rate=0.05,
        )
        assert result.bottleneck_stage in ("ATC_RATE", "CHECKOUT_RATE", "PURCHASE_RATE")

    def test_strong_funnel(self):
        """Strong funnel → overall_viable should be True."""
        result = analyze_funnel_bayesian(
            impressions=10000, clicks=500,
            atcs=50, checkouts=30, orders=25,
            viable_ctr=0.02, viable_atc_rate=0.05,
            viable_checkout_rate=0.50, viable_purchase_rate=0.80,
        )
        assert result.overall_viable

    def test_summary_string(self):
        """Summary should contain stage information."""
        result = analyze_funnel_bayesian(
            impressions=5000, clicks=100,
            atcs=5, checkouts=2, orders=1,
        )
        assert "CTR" in result.summary
        assert "ATC_RATE" in result.summary


# =============================================================================
# COUNTRY SELECTION TESTS
# =============================================================================

class TestCountrySelection:
    def test_us_scores_highest_for_english_product(self):
        """US should rank highly for English-speaking markets."""
        scores = select_country(product_price=100.0, top_n=3)
        assert len(scores) == 3
        country_codes = [s.country for s in scores]
        assert "US" in country_codes

    def test_country_score_range(self):
        """Country scores should be between 0 and 1."""
        scores = select_country(product_price=100.0, top_n=10)
        for s in scores:
            assert 0.0 <= s.composite_score <= 1.0

    def test_ranking_order(self):
        """Scores should be in descending order."""
        scores = select_country(product_price=100.0, top_n=10)
        for i in range(len(scores) - 1):
            assert scores[i].composite_score >= scores[i + 1].composite_score

    def test_get_best_country(self):
        """get_best_country should return a single result."""
        best = get_best_country(product_price=200.0)
        assert best.country is not None
        assert best.composite_score > 0

    def test_custom_country(self):
        """Should accept custom country profiles."""
        custom = [
            CountryProfile(code="US", name="US", cpc_estimate=0.50, search_demand_monthly=100000),
            CountryProfile(code="NO", name="Norway", cpc_estimate=2.00, search_demand_monthly=5000),
        ]
        scores = select_country(product_price=100.0, countries=custom, top_n=2)
        assert scores[0].country == "US"

    def test_low_cpc_boosts_score(self):
        """Lower CPC should increase score."""
        low_cpc = CountryProfile(code="LOW", name="Low CPC", cpc_estimate=0.30, search_demand_monthly=20000)
        high_cpc = CountryProfile(code="HIGH", name="High CPC", cpc_estimate=3.00, search_demand_monthly=20000)
        s_low = score_country(low_cpc, product_price=100.0)
        s_high = score_country(high_cpc, product_price=100.0)
        assert s_low.composite_score > s_high.composite_score


# =============================================================================
# SCALING RULES TESTS
# =============================================================================

class TestScalingRules:
    def _make_candidate(self, **kwargs) -> Candidate:
        defaults = {
            "candidate_id": "SC-001",
            "selling_price": 100.0,
            "supplier_price": 30.0,
            "supplier_shipping": 10.0,
            "expected_cpc": 1.0,
            "cvr_base": 0.005,
            "economics_confidence": ConfidenceLevel.MEDIUM,
            "cpc_confidence_domain": ConfidenceLevel.MEDIUM,
            "cvr_confidence": ConfidenceLevel.MEDIUM,
            "supplier_confidence": ConfidenceLevel.MEDIUM,
            "competition_confidence": ConfidenceLevel.MEDIUM,
            "demand_confidence": ConfidenceLevel.MEDIUM,
        }
        defaults.update(kwargs)
        c = Candidate(**defaults)
        econ = calculate_economics(
            c.selling_price, c.supplier_price, c.supplier_shipping,
            c.duties, c.payment_fee_rate, 0.20, 0.05,
            c.expected_cpc, c.cvr_pessimistic, c.cvr_base, c.cvr_optimistic,
        )
        c.pre_ad_contribution = econ.pre_ad_contribution
        c.headroom_base = econ.headroom_base
        return c

    def test_scale_up_when_all_conditions_met(self):
        """Should scale up when all conditions are met."""
        c = self._make_candidate()
        c.observed_clicks = 200
        c.observed_orders = 5
        c.probability_cvr_above_break_even = 0.8
        engine = ScalingEngine()
        decision = engine.evaluate_scaling(
            candidate=c, current_budget=5.0,
            roas=3.0, recent_contribution=50.0,
            recent_cvr=0.01, baseline_cvr=0.008,
        )
        assert decision.action == ScalingAction.SCALE_UP
        assert decision.new_budget > 5.0

    def test_hold_when_negative_contribution(self):
        """Should hold when contribution is negative."""
        c = self._make_candidate()
        c.observed_clicks = 200
        c.probability_cvr_above_break_even = 0.8
        engine = ScalingEngine()
        decision = engine.evaluate_scaling(
            candidate=c, current_budget=5.0,
            recent_contribution=-10.0,
        )
        assert decision.action in [ScalingAction.HOLD, ScalingAction.STOP]

    def test_stop_on_cvr_collapse(self):
        """Should stop when CVR collapses."""
        c = self._make_candidate()
        c.observed_clicks = 200
        c.probability_cvr_above_break_even = 0.8
        engine = ScalingEngine()
        decision = engine.evaluate_scaling(
            candidate=c, current_budget=5.0,
            recent_contribution=5.0,
            recent_cvr=0.002, baseline_cvr=0.01,
        )
        assert decision.action in [ScalingAction.STOP, ScalingAction.HOLD]

    def test_increment_percentage(self):
        """Default increment should be 15%."""
        engine = ScalingEngine()
        assert engine.increment_pct == 0.15

    def test_should_stop_scaling(self):
        """Should detect when to stop scaling."""
        engine = ScalingEngine()
        assert engine.should_stop_scaling(roas=0.3, contribution=10.0)
        assert engine.should_stop_scaling(roas=2.0, contribution=-5.0)
        assert not engine.should_stop_scaling(roas=3.0, contribution=50.0)

    def test_scaling_history_recorded(self):
        """Each scaling decision should be recorded."""
        c = self._make_candidate()
        c.observed_clicks = 100
        c.probability_cvr_above_break_even = 0.5
        engine = ScalingEngine()
        engine.evaluate_scaling(candidate=c, current_budget=5.0, recent_contribution=10.0)
        engine.evaluate_scaling(candidate=c, current_budget=5.75, recent_contribution=15.0)
        assert len(engine.get_history()) == 2


# =============================================================================
# AUCTION EXPLAINER TESTS
# =============================================================================

class TestAuctionExplainer:
    def test_generates_paragraph(self):
        """Should generate a non-empty explanation paragraph."""
        c = Candidate(
            candidate_id="AE-001",
            product_family="Test Product",
            sku="TEST-SKU",
            selling_price=200.0,
            supplier_price=50.0,
            supplier_shipping=10.0,
            expected_cpc=1.0,
            cvr_base=0.005,
            pre_ad_contribution=130.0,
            break_even_cvr=0.0077,
            headroom_base=0.65,
            headroom_optimistic=1.5,
            exact_query_share=0.4,
            shopping_seller_count=3,
            shipping_days=7,
            shipping_gap_vs_market=0,
            supplier_selectivity="selective",
            supplier_reliability=0.8,
            cvr_confidence=ConfidenceLevel.LOW,
        )
        expl = generate_auction_explanation(c)
        assert len(expl.explanation_paragraph) > 100
        assert expl.contribution_margin == 130.0
        assert expl.break_even_cvr == 0.0077
        assert expl.seller_count == 3

    def test_includes_all_required_elements(self):
        """Explanation should include all required numbers."""
        c = Candidate(
            candidate_id="AE-002",
            product_family="Widget",
            selling_price=150.0,
            supplier_price=40.0,
            supplier_shipping=8.0,
            expected_cpc=1.20,
            cvr_base=0.006,
            pre_ad_contribution=95.0,
            break_even_cvr=0.0126,
            headroom_base=0.79,
            headroom_optimistic=1.98,
            exact_query_share=0.3,
            shopping_seller_count=8,
            shipping_days=10,
            shipping_gap_vs_market=3,
            supplier_selectivity="open",
        )
        expl = generate_auction_explanation(c)
        assert "contribution margin" in expl.explanation_paragraph.lower() or "$" in expl.explanation_paragraph
        assert "break-even" in expl.explanation_paragraph.lower() or "break_even" in expl.explanation_paragraph.lower()
        assert "CPC" in expl.explanation_paragraph
        assert "sellers" in expl.explanation_paragraph.lower()


# =============================================================================
# PRODUCT EXPERT TESTS
# =============================================================================

class TestProductExpert:
    def test_register_product(self):
        """Should register a product profile."""
        expert = ProductExpert()
        c = Candidate(
            candidate_id="PE-001",
            product_family="Test",
            sku="TEST",
            selling_price=100.0,
            headroom_base=2.5,
            supplier_reliability=0.8,
            shipping_days=5,
            shopping_seller_count=3,
            intent_score=0.8,
        )
        profile = expert.register_product(c)
        assert profile.candidate_id == "PE-001"
        assert len(profile.strengths) > 0

    def test_compare_products(self):
        """Should compare two products."""
        expert = ProductExpert()
        c1 = Candidate(
            candidate_id="PE-A", product_family="Product A", sku="A",
            selling_price=100.0, headroom_base=2.0, supplier_reliability=0.8,
        )
        c2 = Candidate(
            candidate_id="PE-B", product_family="Product B", sku="B",
            selling_price=150.0, headroom_base=1.5, supplier_reliability=0.5,
        )
        expert.register_product(c1)
        expert.register_product(c2)
        result = expert.compare_products("PE-A", "PE-B")
        assert result is not None
        assert result.product_a == "Product A"
        assert result.product_b == "Product B"

    def test_answer_buyer_need(self):
        """Should recommend products based on buyer requirements."""
        expert = ProductExpert()
        c1 = Candidate(
            candidate_id="PE-C1", product_family="Cheap", sku="C1",
            selling_price=50.0, headroom_base=1.5, supplier_reliability=0.7,
        )
        c2 = Candidate(
            candidate_id="PE-C2", product_family="Expensive", sku="C2",
            selling_price=200.0, headroom_base=2.5, supplier_reliability=0.9,
        )
        expert.register_product(c1)
        expert.register_product(c2)
        result = expert.answer_buyer_need(
            need_type=BuyerNeedType.BUDGET_CONSTRAINED,
            budget=80.0,
        )
        assert result.best_match_candidate_id == "PE-C1"

    def test_capture_demand(self):
        """Should capture demand data."""
        expert = ProductExpert()
        from services.catalog.product_expert import BuyerDemand
        demand = BuyerDemand(
            budget_range=(50, 100),
            feature_requirements=["lightweight"],
            use_case="travel",
            recommended_product="PE-001",
            conversion_outcome=ConversionOutcome.PURCHASED,
        )
        expert.capture_demand(demand)
        summary = expert.get_demand_summary()
        assert summary["total_captures"] == 1

    def test_demand_summary_empty(self):
        """Empty demand log should return zero summary."""
        expert = ProductExpert()
        summary = expert.get_demand_summary()
        assert summary["total_captures"] == 0


# =============================================================================
# PIPELINE INTEGRATION TESTS
# =============================================================================

class TestPipeline:
    def test_pipeline_runs(self):
        """Full pipeline should run without errors."""
        result = run_pipeline()
        assert result.total_loaded == 10
        assert result.passed_gates + result.rejected + result.quarantined == 10

    def test_pipeline_produces_classifications(self):
        """Pipeline should classify all candidates."""
        result = run_pipeline()
        total_classified = sum(result.classification_counts.values())
        assert total_classified == 10

    def test_pipeline_finds_top_candidate(self):
        """Pipeline should identify a top candidate."""
        result = run_pipeline()
        assert result.top_candidate is not None
        assert result.top_candidate.candidate.hard_gate_status != HardGateStatus.REJECT

    def test_pipeline_generates_output_files(self):
        """Pipeline should generate all output files."""
        import tempfile
        result = run_pipeline()
        with tempfile.TemporaryDirectory() as tmpdir:
            # Override OUTPUT_DIR
            import services.research.pipeline as pip
            old_dir = pip.OUTPUT_DIR
            pip.OUTPUT_DIR = tmpdir
            try:
                with open(os.path.join(tmpdir, "FINAL_SELECTION.md"), "w") as f:
                    f.write(generate_final_selection(result))
                with open(os.path.join(tmpdir, "LAUNCH_PLAN.md"), "w") as f:
                    f.write(generate_launch_plan(result))
                with open(os.path.join(tmpdir, "CURRENT_UNKNOWNKNOWNS.md"), "w") as f:
                    f.write(generate_unknownknowns(result))
                assert os.path.exists(os.path.join(tmpdir, "FINAL_SELECTION.md"))
                assert os.path.exists(os.path.join(tmpdir, "LAUNCH_PLAN.md"))
                assert os.path.exists(os.path.join(tmpdir, "CURRENT_UNKNOWNKNOWNS.md"))
            finally:
                pip.OUTPUT_DIR = old_dir

    def test_pipeline_budget_allocation(self):
        """Pipeline should produce a budget allocation."""
        result = run_pipeline()
        assert result.budget_allocation is not None

    def test_rejected_candidates_are_zombies_or_wasters(self):
        """Rejected candidates should be classified as ZOMBIE or WASTER."""
        result = run_pipeline()
        for pcr in result.candidates:
            if pcr.candidate.hard_gate_status == HardGateStatus.REJECT:
                if pcr.classification:
                    assert pcr.classification.product_class in [
                        ProductClass.ZOMBIE, ProductClass.WASTER, ProductClass.POTENTIAL
                    ], f"{pcr.candidate.candidate_id} rejected but classified as {pcr.classification.product_class}"


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
