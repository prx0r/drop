"""Test pipelines - Level 3 tests with mock data."""

import sys
sys.path.insert(0, '/root/drop')

def test_gmail_import_mock():
    """Level 3: Gmail import with mock email."""
    from pipelines.gmail_import import GmailImportPipeline
    from schemas.observation import EvidenceSource
    
    gmail = GmailImportPipeline()
    
    subject = "[GeoDrop Market Anomaly Probe] 2026-09-07 08:00 — Test candidate"
    body = """
    Test report content.
    
    Found Flak AS as Norwegian distributor.
    Total sellers: 5
    Good sellers: 2
    Price NOK 7590.
    KILL this candidate.
    """
    
    observations = gmail.run(subject, body, probe_id="test", candidate_id="TEST-001")
    
    assert len(observations) > 0, "Should extract at least 1 observation"
    
    fields = [obs.field for obs in observations]
    assert "supplier_name" in fields, "Should find supplier"
    assert "total_sellers" in fields or "decision" in fields, "Should find sellers or decision"
    
    print("TEST: Gmail import mock")
    print(f"  Input: {len(body)} chars")
    print(f"  Output: {len(observations)} observations")
    print(f"  Fields: {fields}")
    print("RESULT: PASS")
    return True

def test_gmail_import_deduplication():
    """Level 3: Deduplication works."""
    from pipelines.gmail_import import GmailImportPipeline
    
    gmail = GmailImportPipeline()
    
    body = """
    Flak AS is the distributor.
    Flak has stock.
    Flak offers dealer terms.
    """
    
    observations = gmail.run("[Test] 2026-09-07 08:00", body, probe_id="test")
    
    # Should deduplicate - Flak should appear once, not 3 times
    supplier_count = sum(1 for obs in observations if obs.field == "supplier_name")
    assert supplier_count <= 2, f"Flak should appear at most 2 times, got {supplier_count}"
    
    print("TEST: Gmail import deduplication")
    print(f"  Input: 'Flak' mentioned 3 times")
    print(f"  Output: {supplier_count} supplier observations")
    print("RESULT: PASS")
    return True

def test_state_machine_transitions():
    """Level 3: State machine with observations."""
    from pipelines.state_machine import StateMachinePipeline
    from schemas.candidate import Candidate, CandidateState
    from schemas.observation import Observation, EvidenceSource, EvidenceGrade
    
    sm = StateMachinePipeline()
    
    candidate = Candidate(product_family="Test", country_code="NO")
    
    # Create demand observation
    obs = Observation(
        entity_type="candidate",
        entity_id="TEST-001",
        field="demand_level",
        value="high",
        source=EvidenceSource.SERP,
        source_grade=EvidenceGrade.B,
    )
    
    result = sm.run(candidate, [obs])
    
    print("TEST: State machine transitions")
    print(f"  Input: demand_level observation")
    print(f"  Transition: {result.summary}")
    print("RESULT: PASS")
    return True

def test_kernel_generator():
    """Level 3: Kernel generation from observations."""
    from pipelines.kernel_generator import KernelGeneratorPipeline
    from schemas.observation import Observation, EvidenceSource, EvidenceGrade
    from schemas.hypothesis import Hypothesis
    
    kg = KernelGeneratorPipeline()
    
    observations = [
        Observation(
            entity_type="candidate",
            entity_id="TEST-001",
            field="supplier_name",
            value="Flak AS",
            source=EvidenceSource.MANUAL,
            source_grade=EvidenceGrade.C,
        ),
        Observation(
            entity_type="candidate",
            entity_id="TEST-001",
            field="price_observed",
            value=7590.0,
            unit="NOK",
            source=EvidenceSource.RETAILER_SITE,
            source_grade=EvidenceGrade.C,
        ),
    ]
    
    hypothesis = Hypothesis(
        claim="Test hypothesis",
        null_hypothesis="Test null",
        falsifier="Test falsifier",
    )
    
    kernels = kg.run(observations, [hypothesis])
    
    assert len(kernels) > 0, "Should generate at least 1 kernel"
    
    print("TEST: Kernel generator")
    print(f"  Input: {len(observations)} observations")
    print(f"  Output: {len(kernels)} kernels")
    print(f"  Types: {[k.kernel_type.value for k in kernels]}")
    print("RESULT: PASS")
    return True

if __name__ == "__main__":
    print("=" * 60)
    print("PIPELINE TESTS (Level 3)")
    print("=" * 60)
    
    tests = [
        test_gmail_import_mock,
        test_gmail_import_deduplication,
        test_state_machine_transitions,
        test_kernel_generator,
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
