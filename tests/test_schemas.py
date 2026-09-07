"""Test schemas - Level 1-2 tests."""

import sys
sys.path.insert(0, '/root/drop')

def test_observation_import():
    """Level 1: Observation imports."""
    from schemas.observation import Observation, EvidenceGrade, EvidenceSource, UnknownField
    print("TEST: Observation import")
    print("RESULT: PASS")
    return True

def test_observation_instantiate():
    """Level 2: Observation can be created."""
    from schemas.observation import Observation, EvidenceGrade, EvidenceSource
    
    obs = Observation(
        entity_type="candidate",
        entity_id="NO-TEST-001",
        field="dealer_price",
        value=5200.0,
        unit="NOK",
        source=EvidenceSource.RETAILER_SITE,
        source_grade=EvidenceGrade.C,
        source_name="Test Supplier",
        candidate_id="NO-TEST-001",
        tags=["test"],
    )
    
    assert obs.entity_id == "NO-TEST-001"
    assert obs.field == "dealer_price"
    assert obs.value == 5200.0
    assert obs.source_grade == EvidenceGrade.C
    
    print("TEST: Observation instantiation")
    print(f"  Created: {obs.observation_id}")
    print(f"  Entity: {obs.entity_id}")
    print(f"  Field: {obs.field} = {obs.value}")
    print("RESULT: PASS")
    return True

def test_candidate_import():
    """Level 1: Candidate imports."""
    from schemas.candidate import Candidate, CandidateState
    print("TEST: Candidate import")
    print("RESULT: PASS")
    return True

def test_candidate_instantiate():
    """Level 2: Candidate can be created."""
    from schemas.candidate import Candidate, CandidateState
    
    candidate = Candidate(
        product_family="Test Product",
        country_code="NO",
        category="Test Category",
    )
    
    assert candidate.state == CandidateState.DISCOVERED
    assert candidate.product_family == "Test Product"
    
    print("TEST: Candidate instantiation")
    print(f"  Created: {candidate.candidate_id}")
    print(f"  State: {candidate.state.value}")
    print("RESULT: PASS")
    return True

def test_candidate_state_machine():
    """Level 2: Candidate state transitions work."""
    from schemas.candidate import Candidate, CandidateState
    
    candidate = Candidate(
        product_family="Test",
        country_code="NO",
    )
    
    # Valid transition
    result = candidate.transition(CandidateState.DEMAND_VERIFIED, "test")
    assert result == True
    assert candidate.state == CandidateState.DEMAND_VERIFIED
    
    # Invalid transition (skip states)
    result = candidate.transition(CandidateState.LAUNCHABLE, "skip")
    assert result == False
    assert candidate.state == CandidateState.DEMAND_VERIFIED
    
    print("TEST: Candidate state machine")
    print(f"  Valid transition: DISCOVERED → DEMAND_VERIFIED")
    print(f"  Invalid transition rejected: DEMAND_VERIFIED → LAUNCHABLE")
    print("RESULT: PASS")
    return True

def test_hypothesis_import():
    """Level 1: Hypothesis imports."""
    from schemas.hypothesis import Hypothesis, HypothesisState
    print("TEST: Hypothesis import")
    print("RESULT: PASS")
    return True

def test_hypothesis_instantiate():
    """Level 2: Hypothesis can be created."""
    from schemas.hypothesis import Hypothesis, HypothesisState
    
    hypothesis = Hypothesis(
        claim="Test claim",
        null_hypothesis="Test null",
        falsifier="Test falsifier",
    )
    
    assert hypothesis.state == HypothesisState.OPEN
    assert hypothesis.claim == "Test claim"
    
    print("TEST: Hypothesis instantiation")
    print(f"  Created: {hypothesis.hypothesis_id}")
    print(f"  State: {hypothesis.state.value}")
    print("RESULT: PASS")
    return True

def test_kernel_import():
    """Level 1: Kernel imports."""
    from schemas.kernel import Kernel, KernelType, BeliefDelta
    print("TEST: Kernel import")
    print("RESULT: PASS")
    return True

def test_kernel_instantiate():
    """Level 2: Kernel can be created."""
    from schemas.kernel import Kernel, KernelType, BeliefDelta
    
    kernel = Kernel(
        hypothesis="Test hypothesis",
        new_observation={"fact": "test"},
        belief_delta=BeliefDelta.MODERATELY_FOR,
        kernel_type=KernelType.DEMAND_DISCOVERY,
    )
    
    assert kernel.kernel_type == KernelType.DEMAND_DISCOVERY
    assert kernel.belief_delta == BeliefDelta.MODERATELY_FOR
    
    print("TEST: Kernel instantiation")
    print(f"  Created: {kernel.kernel_id}")
    print(f"  Type: {kernel.kernel_type.value}")
    print("RESULT: PASS")
    return True

def test_economics_import():
    """Level 1: Economics imports."""
    from schemas.economics import CostLedger, DecisionEvent, FeatureSnapshot
    print("TEST: Economics import")
    print("RESULT: PASS")
    return True

def test_economics_instantiate():
    """Level 2: Economics objects can be created."""
    from schemas.economics import CostLedger
    
    ledger = CostLedger(
        gross_revenue=100.0,
        cogs=30.0,
        paid_acquisition=10.0,
        ai_tokens=5.0,
    )
    ledger.calculate()
    
    assert ledger.cm0 == 70.0
    assert ledger.cm2 == 55.0
    
    print("TEST: Economics instantiation")
    print(f"  CM0: {ledger.cm0}")
    print(f"  CM2: {ledger.cm2}")
    print("RESULT: PASS")
    return True

if __name__ == "__main__":
    print("=" * 60)
    print("SCHEMA TESTS (Level 1-2)")
    print("=" * 60)
    
    tests = [
        test_observation_import,
        test_observation_instantiate,
        test_candidate_import,
        test_candidate_instantiate,
        test_candidate_state_machine,
        test_hypothesis_import,
        test_hypothesis_instantiate,
        test_kernel_import,
        test_kernel_instantiate,
        test_economics_import,
        test_economics_instantiate,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            if test():
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"TEST: {test.__name__}")
            print(f"ERROR: {e}")
            print("RESULT: FAIL")
            failed += 1
    
    print(f"\n{'=' * 60}")
    print(f"RESULTS: {passed} passed, {failed} failed")
    print("=" * 60)
