"""Test storage - Level 4-5 tests with real BigQuery."""

import sys
sys.path.insert(0, '/root/drop')

def get_bigquery_client():
    """Get BigQuery client with credentials from agent-vault."""
    import subprocess
    from google.oauth2.credentials import Credentials
    from google.auth.transport.requests import Request
    from google.cloud import bigquery
    
    def get_cred(key):
        result = subprocess.run(
            ['agent-vault', 'vault', 'credential', 'get', key, '--vault', 'oracle'],
            capture_output=True, text=True
        )
        return result.stdout.strip()
    
    creds = Credentials(
        token=None,
        refresh_token=get_cred('GOOGLE_REFRESH_TOKEN'),
        token_uri='https://oauth2.googleapis.com/token',
        client_id=get_cred('GOOGLE_CLIENT_ID'),
        client_secret=get_cred('GOOGLE_CLIENT_SECRET'),
    )
    creds.refresh(Request())
    
    return bigquery.Client(project=get_cred('GOOGLE_CLOUD_PROJECT'), credentials=creds)

def test_bigquery_connection():
    """Level 4: BigQuery connection works."""
    client = get_bigquery_client()
    tables = list(client.list_tables('drop'))
    
    assert len(tables) > 0, "Should have tables in drop dataset"
    
    print("TEST: BigQuery connection")
    print(f"  Tables in drop: {len(tables)}")
    print("RESULT: PASS")
    return True

def test_observation_write():
    """Level 4: Observation write to BigQuery."""
    from storage.bigquery import BigQueryStorage
    from schemas.observation import Observation, EvidenceSource, EvidenceGrade
    from google.cloud import bigquery
    import subprocess
    
    def get_cred(key):
        result = subprocess.run(
            ['agent-vault', 'vault', 'credential', 'get', key, '--vault', 'oracle'],
            capture_output=True, text=True
        )
        return result.stdout.strip()
    
    from google.oauth2.credentials import Credentials
    from google.auth.transport.requests import Request
    
    creds = Credentials(
        token=None,
        refresh_token=get_cred('GOOGLE_REFRESH_TOKEN'),
        token_uri='https://oauth2.googleapis.com/token',
        client_id=get_cred('GOOGLE_CLIENT_ID'),
        client_secret=get_cred('GOOGLE_CLIENT_SECRET'),
    )
    creds.refresh(Request())
    
    storage = BigQueryStorage(project_id=get_cred('GOOGLE_CLOUD_PROJECT'))
    storage._client = bigquery.Client(project=get_cred('GOOGLE_CLOUD_PROJECT'), credentials=creds)
    
    obs = Observation(
        entity_type="candidate",
        entity_id="TEST-WRITE-001",
        field="test_field",
        value=123.45,
        source=EvidenceSource.MANUAL,
        source_grade=EvidenceGrade.C,
        candidate_id="TEST-WRITE-001",
    )
    
    storage.write_observation(obs)
    
    # Verify
    result = storage.client.query(
        f"SELECT COUNT(*) as cnt FROM drop.fact_market_observation WHERE candidate_id = 'TEST-WRITE-001'"
    ).result()
    
    for row in result:
        assert row.cnt > 0, "Should have at least 1 row"
    
    # Clean up
    storage.client.query("DELETE FROM drop.fact_market_observation WHERE candidate_id = 'TEST-WRITE-001'").result()
    
    print("TEST: Observation write to BigQuery")
    print(f"  Wrote observation: {obs.observation_id}")
    print(f"  Verified in BigQuery")
    print("RESULT: PASS")
    return True

def test_observation_read():
    """Level 5: Observation read from BigQuery."""
    from storage.bigquery import BigQueryStorage
    from schemas.observation import Observation, EvidenceSource, EvidenceGrade
    from google.cloud import bigquery
    import subprocess
    
    def get_cred(key):
        result = subprocess.run(
            ['agent-vault', 'vault', 'credential', 'get', key, '--vault', 'oracle'],
            capture_output=True, text=True
        )
        return result.stdout.strip()
    
    from google.oauth2.credentials import Credentials
    from google.auth.transport.requests import Request
    
    creds = Credentials(
        token=None,
        refresh_token=get_cred('GOOGLE_REFRESH_TOKEN'),
        token_uri='https://oauth2.googleapis.com/token',
        client_id=get_cred('GOOGLE_CLIENT_ID'),
        client_secret=get_cred('GOOGLE_CLIENT_SECRET'),
    )
    creds.refresh(Request())
    
    storage = BigQueryStorage(project_id=get_cred('GOOGLE_CLOUD_PROJECT'))
    storage._client = bigquery.Client(project=get_cred('GOOGLE_CLOUD_PROJECT'), credentials=creds)
    
    # Write test data
    obs = Observation(
        entity_type="candidate",
        entity_id="TEST-READ-001",
        field="read_test",
        value=456.78,
        source=EvidenceSource.MANUAL,
        source_grade=EvidenceGrade.C,
        candidate_id="TEST-READ-001",
    )
    storage.write_observation(obs)
    
    # Read it back
    results = storage.read_observations(candidate_id="TEST-READ-001")
    
    assert len(results) > 0, "Should read at least 1 observation"
    assert results[0]["field_name"] == "read_test", "Field name should match"
    
    # Clean up
    storage.client.query("DELETE FROM drop.fact_market_observation WHERE candidate_id = 'TEST-READ-001'").result()
    
    print("TEST: Observation read from BigQuery")
    print(f"  Wrote: {obs.observation_id}")
    print(f"  Read back: {len(results)} observations")
    print(f"  Field matches: {results[0]['field_name'] == 'read_test'}")
    print("RESULT: PASS")
    return True

if __name__ == "__main__":
    print("=" * 60)
    print("STORAGE TESTS (Level 4-5)")
    print("=" * 60)
    
    tests = [
        test_bigquery_connection,
        test_observation_write,
        test_observation_read,
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
