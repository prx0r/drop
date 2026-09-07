#!/usr/bin/env python3
"""
Expand all campaigns with full detail
"""

import os
import re

CAMPAIGN_TEMPLATE = """# {title}

## Campaign: {campaign_id}
## Status: ACTIVE
## Last Updated: 2026-09-07

---

## 1. MARKET OVERVIEW

### Installed Base
{installed_base}

### Lifecycle Trigger
{lifecycle_trigger}

### Buyer Journey
```
Customer identifies problem
    ↓
IDENTIFICATION: photo/type plate
    ↓
COMPATIBILITY: model/generation check
    ↓
REPLACEMENT: exact part or successor
    ↓
PURCHASE: shippable, small parcel
```

---

## 2. COMPETITOR ANALYSIS

{competitor_analysis}

---

## 3. PRODUCT CATALOG (Initial 75 SKUs)

### Component Families
{component_families}

### Compatibility Dimensions
{compatibility_dimensions}

---

## 4. PRICING

| Product | Public Price | Our Margin | Notes |
|---------|--------------|------------|-------|
{pricing_rows}

### Unit Economics
- Average order value: {aov}
- Gross margin: {margin}
- Shipping: {shipping}
- Net per order: {net_per_order}
- Break-even: {breakeven}

---

## 5. SUPPLIER STRATEGY

### Primary Suppliers
{suppliers}

### Action Items
{supplier_actions}

---

## 6. AD STRATEGY

### Google Search
```
Budget: {search_budget}
Keywords: {keywords}
Match type: exact/phrase
Negative: installation, service
```

### Google Shopping
```
Budget: {shopping_budget}
Campaign: standard_shopping
Products: only verified SKUs
```

### Free Listings
```
Budget: 0
Merchant Center: enabled
```

---

## 7. MERCHANT CENTER FEED

### Products (75 SKUs)
- Brand + MPN
- Compatibility details
- Q&A for common questions
- Related products

---

## 8. LANDING PAGE STRUCTURE

### Hero Section
- Product image
- Compatibility statement
- Price and availability
- Buy button

### Identification Section
- How to identify your model
- Photo examples
- Measurement guide

### Compatibility Table
- Model × fits/doesn't fit matrix

### FAQ
- Common questions answered

---

## 9. SUCCESS METRICS

| Metric | Target | Timeline |
|--------|--------|----------|
| SKUs live | 75 | Week 1 |
| First paid order | 1 | Week 4 |
| Orders/month | {orders_target} | Month 3 |
| Revenue/month | {revenue_target} | Month 3 |

---

## 10. NEXT STEPS

{next_steps}
"""

def get_campaign_details(campaign_id):
    """Get details for each campaign."""
    details = {
        "heatpump-electronics": {
            "title": "Heat Pump Electronics — Finland",
            "installed_base": "1.8 million heat pumps in Finland. 33% of sales are replacements.",
            "lifecycle_trigger": "Controller boards, sensors, Wi-Fi modules fail every 5-15 years.",
            "competitor_analysis": """| Name | Type | Stock | Gap |
|------|------|-------|-----|
| Finnish distributors | Trade | Parts available | Trade-oriented |
| Pihabotti | Retailer | Heat pump parts | Limited electronics |
| Finnparttia | Retailer | Heat pump parts | Limited electronics |
| Staypro | Retailer | Heat pump parts | Limited electronics |

### Digital Merchant Gap: 9/10
Controller boards, sensors, Wi-Fi modules wide open. 1.8M installed heat pumps.""",
            "component_families": """| Family | Components | Price Range |
|--------|------------|-------------|
| Controller boards | Generation-specific | EUR 200-500 |
| Temperature sensors | NTC/PTC | EUR 20-50 |
| Wi-Fi modules | Model-specific | EUR 50-150 |
| Display assemblies | Generation-specific | EUR 100-300 |
| Fan control modules | Voltage-dependent | EUR 50-150 |""",
            "compatibility_dimensions": """Model/generation specific
Voltage (24V/230V)
Connector type
Firmware version""",
            "pricing_rows": """| Controller board | EUR 200-500 | 30% | Generation-dependent |
| Temperature sensor | EUR 20-50 | 40% | Simple, high-volume |
| Wi-Fi module | EUR 50-150 | 30% | Model-specific |""",
            "aov": "EUR 100-300",
            "margin": "25-35%",
            "shipping": "EUR 10-20",
            "net_per_order": "EUR 25-100",
            "breakeven": "20 orders/month",
            "suppliers": """| Supplier | Type | Contact | Terms |
|----------|------|---------|-------|
| Finnish distributors | Trade | TBD | Unknown |
| Heat pump specialists | Retailer | TBD | Unknown |""",
            "supplier_actions": """1. Contact 3 Finnish heat pump distributors
2. Verify stock of controller boards and sensors
3. Request net pricing and direct-ship capability""",
            "search_budget": "EUR 50/day",
            "keywords": '"heat pump controller replacement", "lämpöpumppu ohjauspaneeli"',
            "shopping_budget": "EUR 25/day",
            "orders_target": "20",
            "revenue_target": "EUR 3,000",
            "next_steps": """1. Contact Finnish heat pump distributors
2. Identify 50 common controller/sensor models
3. Build compatibility graph
4. Create Merchant Center feed
5. Set up Shopify store
6. Launch Google Ads test"""
        },
        "hottub-control-panels": {
            "title": "Hot-Tub Control Panels — Nordic",
            "installed_base": "Large Nordic hot-tub installed base. Consumer brand ≠ component manufacturer.",
            "lifecycle_trigger": "Controllers fail, screens die, upgrade desired.",
            "competitor_analysis": """| Name | Type | Stock | Gap |
|------|------|-------|-----|
| Viskan Spa | Norwegian retailer | Nordic panels | Dealer-only, serial-range specific |
| AuraSpa.fi | Finnish retailer | Balboa/Gecko | Good compatibility info |
| Folkpool.se | Swedish retailer | Nordic panels | Serial-number ranges, dealer-only |
| Vikingbad | Manufacturer | Own systems | Limited compatibility data |
| Balboa | OEM | Global | No consumer resolver |
| Gecko | OEM | Global | No consumer resolver |

### Digital Merchant Gap: 9/10
No cross-brand compatibility resolver. Consumer must know internal control system.""",
            "component_families": """| Family | Components | Price Range |
|--------|------------|-------------|
| Balboa VL-series | Control panels | EUR 200-400 |
| Balboa TP-series | Control panels | EUR 300-500 |
| Gecko IN.K-series | Control panels | EUR 400-700 |
| Controller boxes | PCBs | EUR 500-1,500 |""",
            "compatibility_dimensions": """Hot-tub brand
Control system (Balboa/Gecko/Spanet)
Serial-number range
Pump count
Heater type""",
            "pricing_rows": """| Balboa VL260 | EUR 200 | 30% | |
| Gecko IN.K500 | EUR 425 | 30% | |
| Controller box | EUR 500-1,500 | 25% | Complex ID |""",
            "aov": "EUR 300-700",
            "margin": "25-35%",
            "shipping": "EUR 15-25",
            "net_per_order": "EUR 75-245",
            "breakeven": "15 orders/month",
            "suppliers": """| Supplier | Type | Contact | Terms |
|----------|------|---------|-------|
| AuraSpa.fi | Finnish retailer | auraspa.fi | Unknown |
| Viskan Spa | Norwegian retailer | viskanspa.no | Dealer-only |
| Folkpool.se | Swedish retailer | folkpool.se | Unknown |""",
            "supplier_actions": """1. Contact AuraSpa.fi — verify stock and pricing
2. Contact Viskan Spa — verify dealer terms
3. Identify Balboa/Gecko distributors""",
            "search_budget": "EUR 50/day",
            "keywords": '"hot tub control panel", "spabad kontrollpanel", "Balboa replacement"',
            "shopping_budget": "EUR 25/day",
            "orders_target": "15",
            "revenue_target": "EUR 5,000",
            "next_steps": """1. Contact AuraSpa.fi — verify stock
2. Contact Viskan Spa — verify dealer terms
3. Map Balboa/Gecko compatibility
4. Build 75 SKU catalog
5. Create Merchant Center feed
6. Launch Google Ads test"""
        },
        "marine-electronics-retrofit": {
            "title": "Marine Electronics Retrofit Adapters — Nordic",
            "installed_base": "Millions of recreational boats. Marine electronics generations change connectors.",
            "lifecycle_trigger": "Electronics upgrade cycles. Old transducers remain useful.",
            "competitor_analysis": """| Name | Type | Stock | Gap |
|------|------|-------|-----|
| Garmin | OEM | Adapters EUR 75 | No cross-brand resolver |
| Marine Shop Norway | Retailer | NMEA 2000 adapters | Limited selection |
| PartWake | Intelligence | Marine part ID | Research only, no fulfillment |

### Digital Merchant Gap: 8/10
No cross-brand adapter resolver. Consumer must know pin configurations.""",
            "component_families": """| Family | Components | Price Range |
|--------|------------|-------------|
| Garmin adapters | 6→8→12 pin | EUR 75-200 |
| NMEA 2000 adapters | Protocol converters | EUR 100-500 |
| Analogue→digital | Legacy converters | EUR 200-1,000 |""",
            "compatibility_dimensions": """Old device brand/model
New device brand/model
Connector type (4/6/8/12-pin)
Protocol (NMEA 0183/2000)
Voltage""",
            "pricing_rows": """| Garmin 6→8 pin adapter | EUR 75 | 25% | |
| NMEA 2000 adapter | EUR 100-500 | 30% | |
| Analogue converter | EUR 200-1,000 | 25% | Complex ID |""",
            "aov": "EUR 100-500",
            "margin": "25-30%",
            "shipping": "EUR 15-25",
            "net_per_order": "EUR 25-150",
            "breakeven": "20 orders/month",
            "suppliers": """| Supplier | Type | Contact | Terms |
|----------|------|---------|-------|
| Marine Shop Norway | Retailer | marineshop.no | Unknown |
| Garmin | OEM | garmin.com | Adapters only |""",
            "supplier_actions": """1. Contact Marine Shop Norway — verify adapter stock
2. Contact Garmin — verify adapter availability
3. Identify NMEA 2000 adapter suppliers""",
            "search_budget": "EUR 50/day",
            "keywords": '"marine adapter", "NMEA 2000 adapter", "Garmin transducer adapter"',
            "shopping_budget": "EUR 25/day",
            "orders_target": "20",
            "revenue_target": "EUR 5,000",
            "next_steps": """1. Contact Marine Shop Norway
2. Map Garmin pin transitions
3. Build adapter compatibility graph
4. Create Merchant Center feed
5. Launch Google Ads test"""
        }
    }
    
    # Default template for campaigns without specific details
    default = {
        "title": campaign_id.replace("-", " ").title(),
        "installed_base": "See original campaign file for details.",
        "lifecycle_trigger": "Equipment failure, obsolescence, or migration required.",
        "competitor_analysis": "See original campaign file for competitor details.",
        "component_families": "See original campaign file for component details.",
        "compatibility_dimensions": "Model/generation specific, voltage/connector dependent.",
        "pricing_rows": "| Primary component | See market data | 25-30% | Generation-dependent |",
        "aov": "See market data",
        "margin": "25-35%",
        "shipping": "Small parcel rates",
        "net_per_order": "See calculation",
        "breakeven": "15-20 orders/month",
        "suppliers": "See original campaign file for supplier details.",
        "supplier_actions": "1. Contact suppliers\n2. Verify stock and pricing\n3. Request net pricing",
        "search_budget": "See market data",
        "keywords": "brand + model + delar/erstatning",
        "shopping_budget": "See market data",
        "orders_target": "15-20",
        "revenue_target": "See calculation",
        "next_steps": "1. Contact suppliers\n2. Build product catalog\n3. Create Merchant Center feed\n4. Set up Shopify store\n5. Launch Google Ads test"
    }
    
    return details.get(campaign_id, default)

def main():
    campaigns_dir = "/root/drop/campaigns/active"
    
    for filename in os.listdir(campaigns_dir):
        if filename.endswith(".md"):
            campaign_id = filename.replace(".md", "")
            filepath = os.path.join(campaigns_dir, filename)
            
            # Check if already expanded
            with open(filepath, 'r') as f:
                content = f.read()
            
            if "MARKET OVERVIEW" in content:
                print(f"Skipping {campaign_id} (already expanded)")
                continue
            
            # Get details
            details = get_campaign_details(campaign_id)
            
            # Generate expanded content
            expanded = CAMPAIGN_TEMPLATE.format(**details)
            
            # Write expanded content
            with open(filepath, 'w') as f:
                f.write(expanded)
            
            print(f"Expanded: {campaign_id}")

if __name__ == "__main__":
    main()
