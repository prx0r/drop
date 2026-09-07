"""Campaign compiler pipeline.

Transforms research state into deployment configuration.
Input: CampaignHypothesis + CountrySnapshot + CandidateSnapshot
Output: LaunchSpec
"""

from __future__ import annotations

from typing import Optional

from schemas.campaign import (
    CampaignHypothesis,
    LaunchSpec,
    ActivationGate,
    CountryProfile,
    CountryExecutionPolicy,
)
from schemas.candidate import Candidate
from schemas.observation import Observation


class CampaignCompiler:
    """Compiles research state into a LaunchSpec.

    This is a pure transform. No I/O.
    """

    def compile(
        self,
        hypothesis: CampaignHypothesis,
        country_profile: CountryProfile,
        execution_policy: CountryExecutionPolicy,
        candidate: Candidate,
        observations: list[Observation],
    ) -> LaunchSpec:
        """Compile a LaunchSpec from research state."""

        # Build store configuration
        store = self._build_store_config(hypothesis, country_profile, execution_policy)

        # Build decision engine
        decision_engine = self._build_decision_engine(hypothesis, candidate)

        # Build merchant config
        merchant = self._build_merchant_config(hypothesis, observations)

        # Build ads config
        ads = self._build_ads_config(hypothesis, country_profile, observations)

        # Build measurement config
        measurement = self._build_measurement_config(country_profile)

        # Calculate economics
        economics = self._calculate_economics(hypothesis, observations)

        # Build activation gates
        activation_gates = self._build_activation_gates(hypothesis, observations)

        return LaunchSpec(
            campaign_hypothesis_id=hypothesis.hypothesis_id,
            store=store,
            decision_engine=decision_engine,
            merchant=merchant,
            ads=ads,
            measurement=measurement,
            economics=economics,
            activation_gates=[gate.model_dump() for gate in activation_gates],
        )

    def _build_store_config(
        self,
        hypothesis: CampaignHypothesis,
        country_profile: CountryProfile,
        execution_policy: CountryExecutionPolicy,
    ) -> dict:
        """Build store configuration from country + hypothesis."""
        return {
            "market": hypothesis.country_code,
            "language": execution_policy.required_language,
            "currency": country_profile.currency,
            "brand": f"Drop {hypothesis.ecosystem.replace('_', ' ').title()}",
            "navigation": [
                {"path": "/", "label": "Home"},
                {"path": "/velg", "label": "Choose System"},
                {"path": "/kompatibilitet", "label": "Compatibility"},
                {"path": "/produkter", "label": "Products"},
                {"path": "/kontakt", "label": "Contact"},
            ],
            "payments": execution_policy.required_payment_methods,
            "shipping": execution_policy.shipping_constraints,
            "returns": f"{country_profile.consumer_protection_days} days",
            "legal": execution_policy.required_disclosures,
        }

    def _build_decision_engine(
        self,
        hypothesis: CampaignHypothesis,
        candidate: Candidate,
    ) -> dict:
        """Build the AI decision engine configuration."""
        return {
            "questions": [
                {
                    "id": "existing_owner",
                    "text": "Har du allerede Davis-utstyr?",
                    "type": "boolean",
                    "required": True,
                },
                {
                    "id": "current_equipment",
                    "text": "Hva slags Davis-utstyr har du?",
                    "type": "select",
                    "options": ["Vantage Vue", "Vantage Pro2", "WeatherLink", "Annet"],
                    "depends_on": "existing_owner",
                    "depends_value": True,
                },
                {
                    "id": "goal",
                    "text": "Hva ønsker du å oppnå?",
                    "type": "select",
                    "options": [
                        "Erstatte gammel konsoll",
                        "Legge til fjernovervåking",
                        "Oppgradere til Pro2",
                        "Bygge komplett stasjon",
                    ],
                },
            ],
            "compatibility_rules": [
                {"condition": "model == 'Vantage Vue'", "compatible": ["6313EU", "WeatherLink Live"]},
                {"condition": "model == 'Vantage Pro2'", "compatible": ["6313EU", "WeatherLink Live"]},
                {"condition": "goal == 'fjernovervåking'", "requires": ["WeatherLink Live"]},
            ],
            "recommendations": "dynamic",  # AI generates based on answers
        }

    def _build_merchant_config(
        self,
        hypothesis: CampaignHypothesis,
        observations: list[Observation],
    ) -> dict:
        """Build merchant/product configuration."""
        # Extract products from observations
        products = []
        for obs in observations:
            if obs.field == "product_name" and isinstance(obs.value, str):
                products.append({
                    "name": obs.value,
                    "source": "observation",
                })

        return {
            "products": products if products else [{"name": "Davis 6313EU", "source": "hypothesis"}],
            "gtins": [],
            "prices": {},
            "stock": "unknown",
            "shipping": "standard",
            "returns": "30_days",
        }

    def _build_ads_config(
        self,
        hypothesis: CampaignHypothesis,
        country_profile: CountryProfile,
        observations: list[Observation],
    ) -> dict:
        """Build Google Ads configuration."""
        return {
            "channel": "google_search",
            "geo": hypothesis.country_code,
            "language": country_profile.languages[0] if country_profile.languages else "no",
            "keywords": [
                "davis værstasjon",
                "davis vantage vue norge",
                "davis vantage pro2",
                "davis konsoll",
                "davis erstatning",
                "værstasjon kompatibilitet",
            ],
            "negatives": ["gratis", "brukt", "billig", "tilbud"],
            "ads": [
                {
                    "headline": "Davis Værstasjon - Norsk Spesialist",
                    "description": "Kompatibilitetsveiledning for Davis-eiere. Finn riktig utstyr.",
                    "path": "davis.no/kompatibilitet",
                }
            ],
            "bidding": "maximize_clicks",
            "budget_daily": 0,  # BLOCKED until activation
        }

    def _build_measurement_config(
        self,
        country_profile: CountryProfile,
    ) -> dict:
        """Build measurement/tracking configuration."""
        return {
            "events": [
                "page_view",
                "chooser_start",
                "chooser_complete",
                "product_view",
                "add_to_cart",
                "begin_checkout",
                "purchase",
            ],
            "conversions": ["purchase"],
            "attribution": "last_click",
            "consent": "eea_gdpr" if country_profile.country_code in ["NO", "FI", "SE", "DK", "DE", "NL", "IE", "GB"] else "none",
        }

    def _calculate_economics(
        self,
        hypothesis: CampaignHypothesis,
        observations: list[Observation],
    ) -> dict:
        """Calculate economic projections."""
        # Extract price data from observations
        prices = [obs.value for obs in observations if obs.field == "price_observed" and isinstance(obs.value, (int, float))]
        
        avg_price = sum(prices) / len(prices) if prices else 0
        
        return {
            "avg_price": avg_price,
            "estimated_cogs": avg_price * 0.4,  # Estimate
            "estimated_shipping": 100,  # NOK estimate
            "estimated_margin": avg_price * 0.6 - 100,
            "break_even_cac": avg_price * 0.3,  # 30% of margin
            "break_even_cpc": 0,  # BLOCKED - needs real CPC data
            "cm0": 0,  # BLOCKED - needs real supplier cost
            "cm1": 0,  # BLOCKED - needs real ad cost
            "cm2": 0,  # BLOCKED - needs real AI/API cost
        }

    def _build_activation_gates(
        self,
        hypothesis: CampaignHypothesis,
        observations: list[Observation],
    ) -> list[ActivationGate]:
        """Build activation gates from hypothesis requirements."""
        gates = []

        # Check if we have supplier data
        has_supplier = any(obs.field == "supplier_name" for obs in observations)
        gates.append(ActivationGate(
            gate_id="supplier_authorized",
            name="Supplier Authorized",
            description="Must have authorized supplier or dealer relationship",
            required=True,
            evidence_source="supplier_email",
            status="PASS" if has_supplier else "BLOCKED",
            blocked_reason=None if has_supplier else "No supplier authorization confirmed",
        ))

        # Check if we have price data
        has_price = any(obs.field == "price_observed" for obs in observations)
        gates.append(ActivationGate(
            gate_id="exact_supplier_cost",
            name="Exact Supplier Cost",
            description="Must have verified dealer net price",
            required=True,
            evidence_source="supplier_quote",
            status="PASS" if has_price else "BLOCKED",
            blocked_reason=None if has_price else "No supplier price confirmed",
        ))

        # Economic gates (always blocked until real data)
        gates.append(ActivationGate(
            gate_id="positive_cm2",
            name="Positive CM2",
            description="CM2 must be positive at test assumptions",
            required=True,
            evidence_source="economics_calculation",
            status="BLOCKED",
            blocked_reason="Requires supplier cost + CPC data",
        ))

        gates.append(ActivationGate(
            gate_id="keyword_data_authenticated",
            name="Keyword Data Authenticated",
            description="Must have real Keyword Planner data",
            required=True,
            evidence_source="google_ads_api",
            status="BLOCKED",
            blocked_reason="Google Ads Standard access pending",
        ))

        return gates
