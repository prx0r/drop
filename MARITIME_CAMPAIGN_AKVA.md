# Campaign: AKVA Feed System Resolver

*Generated: 2026-09-07*
*Status: HUMAN_ACTION_REQUIRED (B2B variant needed)*

---

## Binary Gate Result

| # | Statement | Verdict |
|---|-----------|---------|
| B1 | Installed base exists | YES |
| B2 | Lifecycle trigger exists | YES |
| B3 | Compatibility problem exists | YES |
| B4 | Local supply exists | YES |
| B5 | Buyer can self-identify | YES (engineer) |
| B6 | Shippable without technician | NO (B2B) |
| B7 | No single specialist owns decision | YES |
| B8 | Supplier will sell to us | UNKNOWN |
| B9 | Compatibility can be proven | YES (116-page catalogue) |
| B10 | Legal responsibility explicit | YES (B2B) |

**Result: B6 NO + B8 UNKNOWN → HUMAN_ACTION_REQUIRED**

---

## Campaign JSON

```json
{
  "campaign_id": "MAR-NOR-AKVA-FEED-001",
  "track": "b2b_resolution_graph",

  "country": "NO",
  "language": "en",
  "oem": "AKVA group",
  "asset_family": "aquaculture_feed_system",
  "installed_asset": "feed system components",
  "generation": "multi-generation",
  "trigger": "equipment_failure_or_maintenance",
  "component_family": "selector_valves, doser_valves, blowers, sensors, controllers",

  "status": "HUMAN_ACTION_REQUIRED",

  "hard_gates": {
    "supplier_exists": true,
    "stock_fresh": "UNKNOWN",
    "compatibility_proven": true,
    "legal_explicit": true,
    "b2b_buyer": true,
    "technician_install_required": "PARTIAL"
  },

  "installed_base": {
    "description": "AKVA aquaculture feed systems installed globally",
    "source": "https://www.akvagroup.no/getfile.php/1312187-1664461726/Dokumenter/01.%20LOGIN%20-%20DOKUMENTER/Spare%20parts/Engelsk/Spare%20Part%20Catalouge%20Feed%20System_low.pdf",
    "confidence": "HIGH"
  },

  "identity": {
    "identification_method": "photo/nameplate + equipment family selection",
    "resolver_inputs": ["site/barge", "photo/nameplate", "equipment family", "fault description"],
    "resolver_outputs": ["exact AKVA part number", "BOM", "stock/lead time", "approved alternative"]
  },

  "compatibility_graph": {
    "source": "AKVA 116-page spare-parts catalogue",
    "source_url": "https://www.akvagroup.no/getfile.php/1312187-1664461726/Dokumenter/01.%20LOGIN%20-%20DOKUMENTER/Spare%20parts/Engelsk/Spare%20Part%20Catalouge%20Feed%20System_low.pdf",
    "example_edges": [
      {"from": "Selector Valve CF32 L60 CCS #0101561", "to": "Cabinet #0103246", "relation": "INSTALLED_IN"},
      {"from": "Selector Valve CF32 L60 CCS #0101561", "to": "CCS Selector Vari Module #0101081", "relation": "REQUIRES"},
      {"from": "Selector Valve CF32 L60 CCS #0101561", "to": "inductive sensor #10051", "relation": "REQUIRES"}
    ]
  },

  "supplier": {
    "identified": true,
    "primary": "AKVA group",
    "secondary": "UQP/KET Marine",
    "net_prices_verified": false,
    "stock_feed_verified": false,
    "direct_ship_verified": false,
    "rma_verified": false,
    "supplier_type": "B2BRepresentation"
  },

  "economics": {
    "model": "RFQ/PO routing",
    "revenue_type": "supplier_referral_or_procurement_saaS",
    "aov": "UNKNOWN",
    "margin": "UNKNOWN"
  },

  "distribution": {
    "channel": "B2B resolution → RFQ → PO",
    "not_applicable": ["merchant_center", "shopify_catalog"]
  },

  "experiment": {
    "phase": "graph_extraction",
    "action": "Extract 116-page catalogue into structured graph",
    "benchmark": "100 technician queries vs Google/ChatGPT/AKVA site",
    "success_rule": ["Drop resolves fuzzy request into exact SKU/BOM faster than alternatives"],
    "kill_rule": ["AKVA site search already resolves adequately"]
  },

  "evidence": [
    {
      "type": "catalogue",
      "source": "https://www.akvagroup.no/getfile.php/1312187-1664461726/Dokumenter/01.%20LOGIN%20-%20DOKUMENTER/Spare%20parts/Engelsk/Spare%20Part%20Catalouge%20Feed%20System_low.pdf",
      "date": "2026-09-07",
      "confidence": "HIGH"
    },
    {
      "type": "supplier_analog",
      "source": "https://www.akvagroup.com/service-support/land-based/need-for-spareparts-manuals",
      "date": "2026-09-07",
      "confidence": "HIGH"
    }
  ],

  "kill_reasons": [],
  "lessons": ["B2B campaigns need different binary gate (B6 shippable not applicable)"],

  "state": "SUPPLIER_VALIDATION"
}
```

---

## What the Schema Misses for B2B

### 1. Buyer type field

```json
"buyer_type": "B2B" or "B2C" or "B2B2C"
```

B2B campaigns have different gates (technician install not required, professional buyer self-identifies).

### 2. Procurement workflow

```json
"procurement_workflow": {
  "requisition_source": "engineer/technician",
  "approval_required": true,
  "rfq_method": "email/shipServ/procureShip",
  "po_method": "direct/supplier_portal"
}
```

### 3. Downtime cost

```json
"downtime_cost": {
  "per_hour": "UNKNOWN",
  "source": "IMPA blog"
}
```

For B2B maritime, downtime cost drives urgency and willingness to pay.

### 4. Multi-site/multi-vessel

```json
"deployment_scope": "single_vessel" or "fleet" or "global",
"vessel_registry": "Fiskeridirektoratet dataset"
```

### 5. Compliance/certification

```json
"compliance": {
  "classification_society": "DNV/Lloyd's/BV",
  "oem_approval_required": true,
  "warranty_implications": "non-original may void warranty"
}
```

### 6. Partner/referral model

```json
"partner_model": {
  "type": "supplier_referral" or "procurement_saaS" or "ai_frontend_fee",
  "partner": "UQP/KET",
  "commission": "UNKNOWN"
}
```

---

## Updated Schema for B2B Campaigns

```json
{
  "campaign_id": "string",
  "track": "b2b_resolution_graph",
  "buyer_type": "B2B",

  "procurement_workflow": {
    "requisition_source": "engineer/technician",
    "approval_required": boolean,
    "rfq_method": "string",
    "po_method": "string"
  },

  "downtime_cost": {
    "per_hour": "number or UNKNOWN",
    "source": "string"
  },

  "deployment_scope": "single_vessel/fleet/global",

  "compliance": {
    "classification_society": "string",
    "oem_approval_required": boolean,
    "warranty_implications": "string"
  },

  "partner_model": {
    "type": "string",
    "partner": "string",
    "commission": "number or UNKNOWN"
  }
}
```

---

## Score (if B8 verified)

| # | Statement | Score |
|---|-----------|-------|
| S1 | Photo + nameplate required | +10 |
| S2 | Wrong part = equipment downtime | +10 |
| S3 | Multi-generation BOM graph | +10 |
| S4 | Large installed base | +10 |
| S5 | Regular maintenance cycles | +10 |
| S6 | AKVA + UQP/KET suppliers | +10 |
| S7 | No stock feed yet | 0 |
| S8 | Direct ship unknown | -10 |
| S9 | Not small parcel (B2B) | 0 |
| S10 | Photo identifiable | +10 |
| S11 | High AOV (B2B requisition) | +10 |
| S12 | Margin unknown | 0 |
| S13 | Wrong-part cost high (downtime) | +10 |
| S14 | AKVA has catalogue but not resolver | +10 |
| S15 | AKVA is OEM, not competing | +10 |
| S16 | Maritime procurement fragmented | +10 |
| S17 | Norwegian aquaculture niche | +10 |
| S18 | Technical terminology non-trivial | +10 |
| S19 | B2B (not GMC) | 0 |
| S20 | B2B (not Shopify) | 0 |

**Total: 140/200 → VERIFY (needs supplier verification)**
