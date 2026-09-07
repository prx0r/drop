"""Pipeline 1: Gmail Import

Converts raw email text into structured Observations.

Input: Raw email text (from probe reports)
Output: List[Observation]

This pipeline:
1. Parses email headers (subject, date, probe name)
2. Extracts structured facts from the email body
3. Maps facts to Observation objects
4. Tags each observation with probe_id, candidate_id, hypothesis_id

Side effects: NONE. This is a pure transform.
I/O happens in the storage layer.
"""

from __future__ import annotations

import re
from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, Field

from schemas.observation import Observation, EvidenceGrade, EvidenceSource


class EmailMetadata(BaseModel):
    """Parsed email metadata."""

    subject: str
    date: Optional[datetime] = None
    probe_name: Optional[str] = None
    hour: Optional[int] = None
    candidate_mentioned: Optional[str] = None


class GmailImportPipeline:
    """Converts raw email text into structured Observations.

    This is a pure transform. No I/O.
    """

    # Probe name patterns
    PROBE_PATTERNS = {
        "Commerce Trace Radar": "commerce-trace-radar",
        "Product-Market Opportunity Radar": "product-market-radar",
        "Free-Traffic Query Radar": "free-traffic-query-radar",
        "Supplier Margin Radar": "supplier-margin-radar",
        "Store Launch Blueprint Engine": "store-launch-blueprint",
    }

    # Candidate ID patterns
    CANDIDATE_PATTERN = re.compile(
        r"(?:candidate|product|product_family)[=:]\s*([A-Z]{2}-[A-Z]+-\d{3,})"
    )

    # Evidence grade mapping
    EVIDENCE_GRADE_MAP = {
        "official": EvidenceGrade.A,
        "authorized": EvidenceGrade.A,
        "major retailer": EvidenceGrade.B,
        "multiple sellers": EvidenceGrade.B,
        "single seller": EvidenceGrade.C,
        "forum": EvidenceGrade.D,
        "reddit": EvidenceGrade.D,
        "social media": EvidenceGrade.D,
    }

    def parse_email_metadata(self, subject: str, body: str) -> EmailMetadata:
        """Parse email subject and body into metadata."""
        probe_name = None
        for pattern, probe_id in self.PROBE_PATTERNS.items():
            if pattern.lower() in subject.lower():
                probe_name = probe_id
                break

        # Extract date from subject (format: YYYY-MM-DD HH:00)
        date_match = re.search(r"(\d{4}-\d{2}-\d{2})\s+(\d{2}):00", subject)
        date = None
        hour = None
        if date_match:
            try:
                date = datetime.strptime(
                    f"{date_match.group(1)} {date_match.group(2)}:00:00",
                    "%Y-%m-%d %H:%M:%S",
                ).replace(tzinfo=timezone.utc)
                hour = int(date_match.group(2))
            except ValueError:
                pass

        # Extract candidate mention
        candidate_match = self.CANDIDATE_PATTERN.search(body)
        candidate_mentioned = candidate_match.group(1) if candidate_match else None

        return EmailMetadata(
            subject=subject,
            date=date,
            probe_name=probe_name,
            hour=hour,
            candidate_mentioned=candidate_mentioned,
        )

    def extract_observations(
        self,
        body: str,
        metadata: EmailMetadata,
        probe_id: Optional[str] = None,
        candidate_id: Optional[str] = None,
    ) -> list[Observation]:
        """Extract structured observations from email body.

        This is the core transform. It converts free-text email body
        into typed Observation objects.
        """
        observations = []

        # Extract supplier mentions
        supplier_observations = self._extract_supplier_observations(
            body, metadata, probe_id, candidate_id
        )
        observations.extend(supplier_observations)

        # Extract price observations
        price_observations = self._extract_price_observations(
            body, metadata, probe_id, candidate_id
        )
        observations.extend(price_observations)

        # Extract demand observations
        demand_observations = self._extract_demand_observations(
            body, metadata, probe_id, candidate_id
        )
        observations.extend(demand_observations)

        # Extract merchant observations
        merchant_observations = self._extract_merchant_observations(
            body, metadata, probe_id, candidate_id
        )
        observations.extend(merchant_observations)

        # Extract decision observations (KILL, ADVANCE, etc.)
        decision_observations = self._extract_decision_observations(
            body, metadata, probe_id, candidate_id
        )
        observations.extend(decision_observations)

        return observations

    def _extract_supplier_observations(
        self,
        body: str,
        metadata: EmailMetadata,
        probe_id: Optional[str],
        candidate_id: Optional[str],
    ) -> list[Observation]:
        """Extract supplier-related observations."""
        observations = []

        # Look for supplier names
        supplier_patterns = [
            r"(?:supplier|distributor|wholesaler|retailer)[:\s]+([A-Z][a-zA-Z\s]+)",
            r"(?:contacted?|emailed?|quoted?)[:\s]+([A-Z][a-zA-Z\s]+)",
            r"(?:Max Sievert|Flak|Onninen|RIDGID|Testo|Hikmicro|Hunter)",
        ]

        for pattern in supplier_patterns:
            matches = re.finditer(pattern, body)
            for match in matches:
                supplier_name = match.group(1) if match.lastindex else match.group(0)
                observations.append(
                    Observation(
                        entity_type="supplier",
                        entity_id=f"{metadata.candidate_mentioned or candidate_id or 'UNKNOWN'}-SUPPLIER",
                        field="supplier_name",
                        value=supplier_name.strip(),
                        source=EvidenceSource.MANUAL,
                        source_grade=EvidenceGrade.C,
                        probe_id=probe_id,
                        candidate_id=candidate_id,
                        tags=["supplier", "discovery"],
                    )
                )

        return observations

    def _extract_price_observations(
        self,
        body: str,
        metadata: EmailMetadata,
        probe_id: Optional[str],
        candidate_id: Optional[str],
    ) -> list[Observation]:
        """Extract price observations."""
        observations = []

        # Look for price patterns
        price_patterns = [
            r"(?:NOK|EUR|USD|GBP|SEK|DKK)\s*[\d,]+\.?\d*",
            r"[\d,]+\.?\d*\s*(?:NOK|EUR|USD|GBP|SEK|DKK)",
            r"(?:price|cost|margin)[:\s]+[\d,]+\.?\d*",
        ]

        for pattern in price_patterns:
            matches = re.finditer(pattern, body, re.IGNORECASE)
            for match in matches:
                price_text = match.group(0)
                # Try to extract numeric value
                numeric_match = re.search(r"[\d,]+\.?\d*", price_text)
                if numeric_match:
                    try:
                        value = float(numeric_match.group(0).replace(",", ""))
                        # Determine currency
                        currency = "UNKNOWN"
                        for c in ["NOK", "EUR", "USD", "GBP", "SEK", "DKK"]:
                            if c in price_text.upper():
                                currency = c
                                break

                        observations.append(
                            Observation(
                                entity_type="candidate",
                                entity_id=candidate_id or metadata.candidate_mentioned or "UNKNOWN",
                                field="price_observed",
                                value=value,
                                unit=currency,
                                source=EvidenceSource.RETAILER_SITE,
                                source_grade=EvidenceGrade.C,
                                probe_id=probe_id,
                                candidate_id=candidate_id,
                                tags=["price", "market_data"],
                            )
                        )
                    except ValueError:
                        pass

        return observations

    def _extract_demand_observations(
        self,
        body: str,
        metadata: EmailMetadata,
        probe_id: Optional[str],
        candidate_id: Optional[str],
    ) -> list[Observation]:
        """Extract demand-related observations."""
        observations = []

        # Look for demand signals
        demand_patterns = [
            (r"(?:search volume|queries|impressions)[:\s]+[\d,]+", "search_volume"),
            (r"(?:demand|popularity|interest)[:\s]+(high|medium|low|strong|weak)", "demand_level"),
            (r"(?:trend|growth|increasing|decreasing)[:\s]+([+\-]?\d+%)", "demand_trend"),
        ]

        for pattern, field_name in demand_patterns:
            matches = re.finditer(pattern, body, re.IGNORECASE)
            for match in matches:
                value_text = match.group(1) if match.lastindex else match.group(0)
                # Try to extract numeric
                numeric_match = re.search(r"[\d,]+", value_text)
                if numeric_match:
                    try:
                        value = float(numeric_match.group(0).replace(",", ""))
                        observations.append(
                            Observation(
                                entity_type="candidate",
                                entity_id=candidate_id or metadata.candidate_mentioned or "UNKNOWN",
                                field=field_name,
                                value=value,
                                source=EvidenceSource.SERP,
                                source_grade=EvidenceGrade.C,
                                probe_id=probe_id,
                                candidate_id=candidate_id,
                                tags=["demand", "market_data"],
                            )
                        )
                    except ValueError:
                        pass

        return observations

    def _extract_merchant_observations(
        self,
        body: str,
        metadata: EmailMetadata,
        probe_id: Optional[str],
        candidate_id: Optional[str],
    ) -> list[Observation]:
        """Extract merchant/competition observations."""
        observations = []

        # Look for seller counts
        seller_patterns = [
            (r"(?:total sellers?|seller count|retailer count)[:\s]+(\d+)", "total_sellers"),
            (r"(?:good sellers?|competent sellers?|quality sellers?)[:\s]+(\d+)", "good_sellers"),
            (r"(?:merchant count|shop count)[:\s]+(\d+)", "total_sellers"),
        ]

        for pattern, field_name in seller_patterns:
            matches = re.finditer(pattern, body, re.IGNORECASE)
            for match in matches:
                try:
                    value = int(match.group(1))
                    observations.append(
                        Observation(
                            entity_type="candidate",
                            entity_id=candidate_id or metadata.candidate_mentioned or "UNKNOWN",
                            field=field_name,
                            value=value,
                            source=EvidenceSource.SERP,
                            source_grade=EvidenceGrade.C,
                            probe_id=probe_id,
                            candidate_id=candidate_id,
                            tags=["competition", "merchant_count"],
                        )
                    )
                except ValueError:
                    pass

        return observations

    def _extract_decision_observations(
        self,
        body: str,
        metadata: EmailMetadata,
        probe_id: Optional[str],
        candidate_id: Optional[str],
    ) -> list[Observation]:
        """Extract decision observations (KILL, ADVANCE, etc.)."""
        observations = []

        # Look for decision keywords
        decision_patterns = [
            (r"\bKILL\b", "KILLED", "Hypothesis falsified"),
            (r"\bADVANCE\b", "ADVANCED", "Candidate advanced"),
            (r"\bHOLD\b", "HELD", "Candidate on hold"),
            (r"\bLAUNCH\b", "LAUNCH_READY", "Candidate ready to launch"),
            (r"\bFROZEN\b", "FROZEN", "Candidate frozen pending external action"),
            (r"\bHUMAN_ACTION_REQUIRED\b", "HUMAN_ACTION_REQUIRED", "External action needed"),
        ]

        for pattern, decision, reason in decision_patterns:
            if re.search(pattern, body, re.IGNORECASE):
                observations.append(
                    Observation(
                        entity_type="candidate",
                        entity_id=candidate_id or metadata.candidate_mentioned or "UNKNOWN",
                        field="decision",
                        value=decision,
                        source=EvidenceSource.MANUAL,
                        source_grade=EvidenceGrade.A,
                        probe_id=probe_id,
                        candidate_id=candidate_id,
                        tags=["decision", decision.lower()],
                        raw_snapshot=reason,
                    )
                )

        return observations

    def run(
        self,
        email_subject: str,
        email_body: str,
        probe_id: Optional[str] = None,
        candidate_id: Optional[str] = None,
    ) -> list[Observation]:
        """Run the Gmail import pipeline.

        Input: Raw email subject and body
        Output: List of typed Observations
        """
        # Parse metadata
        metadata = self.parse_email_metadata(email_subject, email_body)

        # Use probe_name from metadata if not provided
        if probe_id is None and metadata.probe_name:
            probe_id = metadata.probe_name

        # Use candidate_id from metadata if not provided
        if candidate_id is None and metadata.candidate_mentioned:
            candidate_id = metadata.candidate_mentioned

        # Extract observations
        observations = self.extract_observations(
            body=email_body,
            metadata=metadata,
            probe_id=probe_id,
            candidate_id=candidate_id,
        )

        return observations
