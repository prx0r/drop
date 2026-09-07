"""Anti-cheat verification for agent peer review.

Provides evidence gates, behavioral analysis, and cross-reference checking.
Agents cannot claim work is done without verifiable proof.
"""

import hashlib
import json
import subprocess
from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, Field


class EvidenceGate(BaseModel):
    """An evidence gate that must pass before work is claimed complete."""
    
    gate_id: str
    description: str
    claim: str  # What the agent claims
    verification_method: str  # How to verify
    expected_result: str  # What should be true
    actual_result: Optional[str] = None
    passed: Optional[bool] = None
    verified_at: Optional[datetime] = None
    proof_hash: Optional[str] = None  # Content hash of proof


class BehavioralAnomaly(BaseModel):
    """Detected anomaly in agent behavior."""
    
    anomaly_id: str
    anomaly_type: str  # "claim_reality_mismatch", "missing_evidence", "temporal_inconsistency"
    severity: str  # "HIGH", "MEDIUM", "LOW"
    description: str
    claim: str  # What agent claimed
    reality: str  # What was actually found
    detected_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class AntiCheatVerifier:
    """Verifies agent claims against reality."""
    
    def __init__(self):
        self.gates: list[EvidenceGate] = []
        self.anomalies: list[BehavioralAnomaly] = []
    
    def add_gate(self, gate_id: str, description: str, claim: str, verification_method: str, expected_result: str) -> EvidenceGate:
        """Add an evidence gate."""
        gate = EvidenceGate(
            gate_id=gate_id,
            description=description,
            claim=claim,
            verification_method=verification_method,
            expected_result=expected_result,
        )
        self.gates.append(gate)
        return gate
    
    def verify_test_output(self, test_name: str, expected_passes: int, actual_output: str) -> bool:
        """Verify test output matches claim."""
        # Check if output contains "PASS"
        if "RESULT: PASS" not in actual_output and "passed" not in actual_output.lower():
            self.anomalies.append(BehavioralAnomaly(
                anomaly_id=f"ANOM-{datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S')}",
                anomaly_type="claim_reality_mismatch",
                severity="HIGH",
                description=f"Agent claimed {test_name} passed, but output shows failure",
                claim=f"{test_name} passed",
                reality=actual_output[:200],
            ))
            return False
        
        # Check pass count
        if f"{expected_passes} passed" in actual_output or f"RESULTS: {expected_passes} passed" in actual_output:
            return True
        
        # Extract actual pass count
        import re
        match = re.search(r"(\d+) passed", actual_output)
        if match:
            actual_passes = int(match.group(1))
            if actual_passes < expected_passes:
                self.anomalies.append(BehavioralAnomaly(
                    anomaly_id=f"ANOM-{datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S')}",
                    anomaly_type="claim_reality_mismatch",
                    severity="MEDIUM",
                    description=f"Agent claimed {expected_passes} tests passed, but {actual_passes} actually passed",
                    claim=f"{expected_passes} tests passed",
                    reality=f"{actual_passes} tests passed",
                ))
                return False
        
        return True
    
    def verify_bigquery_write(self, candidate_id: str, expected_count: int) -> bool:
        """Verify data was actually written to BigQuery."""
        try:
            import subprocess
            
            def get_cred(key):
                result = subprocess.run(
                    ['agent-vault', 'vault', 'credential', 'get', key, '--vault', 'oracle'],
                    capture_output=True, text=True
                )
                return result.stdout.strip()
            
            from google.oauth2.credentials import Credentials
            from google.auth.transport.requests import Request
            from google.cloud import bigquery
            
            creds = Credentials(
                token=None,
                refresh_token=get_cred('GOOGLE_REFRESH_TOKEN'),
                token_uri='https://oauth2.googleapis.com/token',
                client_id=get_cred('GOOGLE_CLIENT_ID'),
                client_secret=get_cred('GOOGLE_CLIENT_SECRET'),
            )
            creds.refresh(Request())
            
            client = bigquery.Client(project=get_cred('GOOGLE_CLOUD_PROJECT'), credentials=creds)
            
            result = client.query(
                f"SELECT COUNT(*) as cnt FROM drop.fact_market_observation WHERE candidate_id = '{candidate_id}'"
            ).result()
            
            for row in result:
                if row.cnt < expected_count:
                    self.anomalies.append(BehavioralAnomaly(
                        anomaly_id=f"ANOM-{datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S')}",
                        anomaly_type="claim_reality_mismatch",
                        severity="HIGH",
                        description=f"Agent claimed {expected_count} observations written, but BigQuery has {row.cnt}",
                        claim=f"{expected_count} observations in BigQuery",
                        reality=f"{row.cnt} observations in BigQuery",
                    ))
                    return False
            
            return True
        except Exception as e:
            self.anomalies.append(BehavioralAnomaly(
                anomaly_id=f"ANOM-{datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S')}",
                anomaly_type="verification_failure",
                severity="HIGH",
                description=f"Could not verify BigQuery write: {e}",
                claim="BigQuery write verified",
                reality=f"Verification failed: {e}",
            ))
            return False
    
    def verify_bigquery_read(self, candidate_id: str, expected_fields: list[str]) -> bool:
        """Verify data can be read from BigQuery with correct fields."""
        try:
            import subprocess
            
            def get_cred(key):
                result = subprocess.run(
                    ['agent-vault', 'vault', 'credential', 'get', key, '--vault', 'oracle'],
                    capture_output=True, text=True
                )
                return result.stdout.strip()
            
            from google.oauth2.credentials import Credentials
            from google.auth.transport.requests import Request
            from google.cloud import bigquery
            
            creds = Credentials(
                token=None,
                refresh_token=get_cred('GOOGLE_REFRESH_TOKEN'),
                token_uri='https://oauth2.googleapis.com/token',
                client_id=get_cred('GOOGLE_CLIENT_ID'),
                client_secret=get_cred('GOOGLE_CLIENT_SECRET'),
            )
            creds.refresh(Request())
            
            client = bigquery.Client(project=get_cred('GOOGLE_CLOUD_PROJECT'), credentials=creds)
            
            result = client.query(
                f"SELECT * FROM drop.fact_market_observation WHERE candidate_id = '{candidate_id}' LIMIT 1"
            ).result()
            
            rows = list(result)
            if not rows:
                self.anomalies.append(BehavioralAnomaly(
                    anomaly_id=f"ANOM-{datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S')}",
                    anomaly_type="claim_reality_mismatch",
                    severity="HIGH",
                    description=f"Agent claimed data readable from BigQuery, but no rows found for {candidate_id}",
                    claim=f"Data readable for {candidate_id}",
                    reality="No rows found",
                ))
                return False
            
            # Check fields exist
            row_dict = dict(rows[0])
            for field in expected_fields:
                if field not in row_dict:
                    self.anomalies.append(BehavioralAnomaly(
                        anomaly_id=f"ANOM-{datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S')}",
                        anomaly_type="claim_reality_mismatch",
                        severity="MEDIUM",
                        description=f"Agent claimed field '{field}' exists, but it's missing",
                        claim=f"Field '{field}' exists",
                        reality=f"Fields: {list(row_dict.keys())}",
                    ))
                    return False
            
            return True
        except Exception as e:
            self.anomalies.append(BehavioralAnomaly(
                anomaly_id=f"ANOM-{datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S')}",
                anomaly_type="verification_failure",
                severity="HIGH",
                description=f"Could not verify BigQuery read: {e}",
                claim="BigQuery read verified",
                reality=f"Verification failed: {e}",
            ))
            return False
    
    def generate_proof_hash(self, data: str) -> str:
        """Generate content hash for proof."""
        return hashlib.sha256(data.encode()).hexdigest()[:16]
    
    def generate_report(self) -> dict:
        """Generate verification report."""
        gates_passed = sum(1 for g in self.gates if g.passed)
        gates_total = len(self.gates)
        
        return {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "gates": {
                "total": gates_total,
                "passed": gates_passed,
                "failed": gates_total - gates_passed,
            },
            "anomalies": {
                "total": len(self.anomalies),
                "high": sum(1 for a in self.anomalies if a.severity == "HIGH"),
                "medium": sum(1 for a in self.anomalies if a.severity == "MEDIUM"),
                "low": sum(1 for a in self.anomalies if a.severity == "LOW"),
            },
            "verdict": "PASS" if gates_passed == gates_total and len([a for a in self.anomalies if a.severity == "HIGH"]) == 0 else "FAIL",
            "anomaly_details": [a.model_dump() for a in self.anomalies],
        }
