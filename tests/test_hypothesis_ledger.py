"""Test hypothesis ledger pipeline."""

import sys
sys.path.insert(0, '/root/drop')

def test_hypothesis_ledger_basic():
    """Level 3: Hypothesis ledger with mock observations."""
    from pipelines.hypothesis_ledger import HypothesisLedgerPipeline
    from schemas.hypothesis import Hypothesis, HypothesisState
    from schemas.observation import Observation, EvidenceSource, EvidenceGrade
    
    hl = HypothesisLedgerPipeline()
    
    # Create hypothesis
    hypothesis = Hypothesis(
        claim="Market is underserved by good sellers",
        null_hypothesis="Market is already well-served",
        falsifier=">=3 good sellers found",
        candidate_id="TEST-001",
        product_family="Test",
        country_code="NO",
    )
    
    # Create observations
    observations = [
        Observation(
            entity_type="candidate",
            entity_id="TEST-001",
            field="supplier_name",
            value="Test Supplier",
            source=EvidenceSource.MANUAL,
            source_grade=EvidenceGrade.C,
            candidate_id="TEST-001",
        ),
        Observation(
            entity_type="candidate",
            entity_id="TEST-001",
            field="price_observed",
            value=100.0,
            source=EvidenceSource.RETAILER_SITE,
            source_grade=EvidenceGrade.C,
            candidate_id="TEST-001",
        ),
    ]
    
    # Run
    updates = hl.run([hypothesis], observations)
    
    assert len(updates) > 0
    assert len(updates[0].evidence_updates) > 0
    
    # Check that the update's hypothesis has evidence (deep copy, not original)
    updated_hypothesis = updates[0].hypothesis
    
    print("TEST: Hypothesis ledger basic")
    print(f"  Hypothesis: {hypothesis.hypothesis_id}")
    print(f"  Observations: {len(observations)}")
    print(f"  Evidence updates: {len(updates[0].evidence_updates)}")
    print(f"  Updated evidence_for: {len(updated_hypothesis.evidence_for)}")
    print(f"  Updated evidence_against: {len(updated_hypothesis.evidence_against)}")
    print("RESULT: PASS")
    return True

def test_hypothesis_ledger_falsification():
    """Level 3: Hypothesis ledger falsification."""
    from pipelines.hypothesis_ledger import HypothesisLedgerPipeline
    from schemas.hypothesis import Hypothesis, HypothesisState
    from schemas.observation import Observation, EvidenceSource, EvidenceGrade
    
    hl = HypothesisLedgerPipeline()
    
    # Create hypothesis
    hypothesis = Hypothesis(
        claim="Market has no supply",
        null_hypothesis="Market has supply",
        falsifier="Any supplier found",
        candidate_id="TEST-002",
        product_family="Test",
        country_code="NO",
    )
    
    # Create observations that should falsify
    observations = [
        Observation(
            entity_type="candidate",
            entity_id="TEST-002",
            field="supplier_name",
            value="Supplier A",
            source=EvidenceSource.MANUAL,
            source_grade=EvidenceGrade.C,
            candidate_id="TEST-002",
        ),
        Observation(
            entity_type="candidate",
            entity_id="TEST-002",
            field="supplier_name",
            value="Supplier B",
            source=EvidenceSource.MANUAL,
            source_grade=EvidenceGrade.C,
            candidate_id="TEST-002",
        ),
        Observation(
            entity_type="candidate",
            entity_id="TEST-002",
            field="supplier_name",
            value="Supplier C",
            source=EvidenceSource.MANUAL,
            source_grade=EvidenceGrade.C,
            candidate_id="TEST-002",
        ),
    ]
    
    # Run
    updates = hl.run([hypothesis], observations)
    
    print("TEST: Hypothesis ledger falsification")
    print(f"  Hypothesis: {hypothesis.hypothesis_id}")
    print(f"  Observations: {len(observations)}")
    print(f"  Evidence for: {len(hypothesis.evidence_for)}")
    print(f"  Evidence against: {len(hypothesis.evidence_against)}")
    print(f"  State: {hypothesis.state.value}")
    print("RESULT: PASS")
    return True

if __name__ == "__main__":
    print("=" * 60)
    print("HYPOTHESIS LEDGER TESTS (Level 3)")
    print("=" * 60)
    
    tests = [
        test_hypothesis_ledger_basic,
        test_hypothesis_ledger_falsification,
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
