"""Test end-to-end - Level 6-7 tests with real Gmail → BigQuery."""

import sys
sys.path.insert(0, '/root/drop')

def get_credentials():
    """Get all credentials from agent-vault."""
    import subprocess
    from google.oauth2.credentials import Credentials
    from google.auth.transport.requests import Request
    
    def get_cred(key):
        result = subprocess.run(
            ['agent-vault', 'vault', 'credential', 'get', key, '--vault', 'oracle'],
            capture_output=True, text=True
        )
        return result.stdout.strip()
    
    gmail_creds = Credentials(
        token=None,
        refresh_token=get_cred('GMAIL_REFRESH_TOKEN'),
        token_uri='https://oauth2.googleapis.com/token',
        client_id=get_cred('GMAIL_CLIENT_ID'),
        client_secret=get_cred('GMAIL_CLIENT_SECRET'),
    )
    gmail_creds.refresh(Request())
    
    cloud_creds = Credentials(
        token=None,
        refresh_token=get_cred('GOOGLE_REFRESH_TOKEN'),
        token_uri='https://oauth2.googleapis.com/token',
        client_id=get_cred('GOOGLE_CLIENT_ID'),
        client_secret=get_cred('GOOGLE_CLIENT_SECRET'),
    )
    cloud_creds.refresh(Request())
    
    return gmail_creds, cloud_creds, get_cred('GOOGLE_CLOUD_PROJECT')

def test_gmail_fetch():
    """Level 6: Fetch real email from Gmail."""
    import urllib.request, urllib.parse, json
    
    gmail_creds, _, _ = get_credentials()
    
    headers = {"Authorization": f"Bearer {gmail_creds.token}"}
    query = urllib.parse.quote("to:tradesprior@gmail.com subject:GeoDrop")
    url = f"https://gmail.googleapis.com/gmail/v1/users/me/messages?q={query}&maxResults=1"
    
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    data = json.loads(response.read())
    messages = data.get("messages", [])
    
    assert len(messages) > 0, "Should find at least 1 email"
    
    print("TEST: Gmail fetch")
    print(f"  Found {len(messages)} emails")
    print(f"  Message ID: {messages[0]['id']}")
    print("RESULT: PASS")
    return True

def test_full_pipeline():
    """Level 7: Full pipeline Gmail → BigQuery."""
    import urllib.request, urllib.parse, json, base64
    from pipelines.gmail_import import GmailImportPipeline
    from pipelines.state_machine import StateMachinePipeline
    from pipelines.kernel_generator import KernelGeneratorPipeline
    from schemas.candidate import Candidate
    from schemas.hypothesis import Hypothesis
    from storage.bigquery import BigQueryStorage
    from google.cloud import bigquery
    
    gmail_creds, cloud_creds, project_id = get_credentials()
    
    # Step 1: Fetch email
    headers = {"Authorization": f"Bearer {gmail_creds.token}"}
    query = urllib.parse.quote("to:tradesprior@gmail.com subject:GeoDrop")
    url = f"https://gmail.googleapis.com/gmail/v1/users/me/messages?q={query}&maxResults=1"
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    data = json.loads(response.read())
    msg_id = data["messages"][0]["id"]
    
    url = f"https://gmail.googleapis.com/gmail/v1/users/me/messages/{msg_id}?format=full"
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    msg_data = json.loads(response.read())
    
    payload = msg_data.get("payload", {})
    subject = ""
    for h in payload.get("headers", []):
        if h["name"] == "Subject":
            subject = h["value"]
    
    def find_text(part):
        if part.get("mimeType") == "text/plain":
            d = part.get("body", {}).get("data", "")
            if d:
                return base64.urlsafe_b64decode(d).decode("utf-8", errors="replace")
        for subpart in part.get("parts", []):
            result = find_text(subpart)
            if result:
                return result
        return None
    
    body = find_text(payload)
    assert body, "Should extract email body"
    
    # Step 2: Parse
    gmail_pipe = GmailImportPipeline()
    observations = gmail_pipe.run(subject, body, probe_id="E2E-TEST", candidate_id="E2E-TEST-001")
    assert len(observations) > 0, "Should extract observations"
    
    # Step 3: Create candidate
    candidate = Candidate(product_family="E2E Test", country_code="NO")
    
    # Step 4: State machine
    sm = StateMachinePipeline()
    sm_result = sm.run(candidate, observations)
    
    # Step 5: Kernel generator
    kg = KernelGeneratorPipeline()
    kernels = kg.run(observations, [])
    
    # Step 6: Write to BigQuery
    storage = BigQueryStorage(project_id=project_id)
    storage._client = bigquery.Client(project=project_id, credentials=cloud_creds)
    
    written = 0
    for obs in observations:
        try:
            storage.write_observation(obs)
            written += 1
        except:
            pass
    
    # Step 7: Verify
    result = storage.client.query(
        "SELECT COUNT(*) as cnt FROM drop.fact_market_observation WHERE candidate_id = 'E2E-TEST-001'"
    ).result()
    
    for row in result:
        assert row.cnt > 0, "Should have observations in BigQuery"
    
    # Clean up
    storage.client.query("DELETE FROM drop.fact_market_observation WHERE candidate_id = 'E2E-TEST-001'").result()
    
    print("TEST: Full pipeline Gmail → BigQuery")
    print(f"  1. Fetched email: {len(body)} chars")
    print(f"  2. Parsed: {len(observations)} observations")
    print(f"  3. Candidate: {candidate.candidate_id}")
    print(f"  4. State: {sm_result.summary}")
    print(f"  5. Kernels: {len(kernels)}")
    print(f"  6. Written: {written}/{len(observations)}")
    print(f"  7. Verified in BigQuery")
    print("RESULT: PASS")
    return True

if __name__ == "__main__":
    print("=" * 60)
    print("END-TO-END TESTS (Level 6-7)")
    print("=" * 60)
    
    tests = [
        test_gmail_fetch,
        test_full_pipeline,
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
