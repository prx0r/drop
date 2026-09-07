# Gold Prompt 1: Agent-Native Commerce

*For autonomous exploration of specialist product markets*

---

## The Thesis

There exists a class of products where:
- High purchase intent exists (search demand)
- Technical complexity creates decision friction
- Existing merchants inadequately resolve the decision
- Localized specialist positioning creates margin
- AI can provide the decision engine that merchants cannot

These are **compatibility-heavy, specification-driven products** where the buyer needs help choosing, not just browsing.

---

## The Exploration Protocol

### Phase 1: Installed Base Discovery

For each country × ecosystem combination:

```
1. What large physical systems exist?
   - Heat pumps
   - EV chargers
   - Solar panels
   - Weather stations
   - Security systems
   - Smart home devices

2. What lifecycle events do they generate?
   - Replacement (age/failure)
   - Maintenance (filters, cleaning)
   - Upgrade (new features)
   - Compatibility (new components)
   - Repair (breakdown)

3. What's the installed base size?
   - Official statistics (SSB, StatFin, ONS)
   - Industry reports
   - Sales data
```

### Phase 2: Merchant Gap Detection

For each ecosystem × country:

```
1. Count total sellers
   - Google Shopping
   - Price comparison sites
   - Marketplace listings

2. Count good sellers (quality > 70)
   - Specialist positioning
   - Technical content
   - Local language
   - Real reviews

3. Calculate merchant gap
   gap = (demand - good_sellers) / demand

4. Flag if gap > 0.5
```

### Phase 3: Search Demand Validation

For each ecosystem × country:

```
1. Generate native-language queries
   - Product names
   - Compatibility queries
   - Problem/solution queries
   - Comparison queries

2. Check search volume
   - Google Keyword Planner
   - Google Trends
   - Comparison sites

3. Check commercial intent
   - Transactional queries
   - Shopping results
   - Price comparison presence
```

### Phase 4: Economics Check

For each product × country:

```
1. Get retail price from observations
2. Get supplier cost (if known)
3. Calculate margin
4. Check if margin > break-even
5. Flag if margin < 0
```

### Phase 5: Hypothesis Generation

For each promising opportunity:

```
H1: [specific claim about market]
H0: [what would explain the data without our claim]
Falsifier: [concrete condition that would kill H1]

Evidence:
- [observation 1]
- [observation 2]
- ...

Status: OPEN / SUPPORTED / FALSIFIED
```

---

## Example: Finland Heat Pump Controllers

### Installed Base
- 1.8M heat pumps installed
- 112,000 sold in 2025 (+63% YoY)
- 33% are replacements
- 8-year avg age → replacement wave starting

### Merchant Gap
- 3 known merchants (Pihabotti, Finnparttia, Staypro)
- Specialist positioning unclear
- Gap likely exists

### Search Demand
- "lämpöpumppu ohjain" (heat pump controller)
- "varmepumppu kauko-ohjaus" (heat pump remote)
- "lämpöpumppu suodatin" (heat pump filter)

### Economics
- Retail: €250
- Supplier: €80 (assumed)
- Shipping: €15
- Margin: €88.25 (44.1%)
- Break-even CAC: €88.25

### Hypothesis

```
H1: Finnish heat pump owners will convert through a
    compatibility/remote-control decision service at
    an acquisition cost below €88.25.

H0: Existing merchants already solve the compatibility
    problem adequately.

Falsifier: >=3 good online sellers found for heat pump
    controllers in Finland.
```

---

## The Query Forest

For each ecosystem, generate native-language queries:

```
heat_pump:
  FI: "lämpöpumppu ohjain", "varmepumppu kauko-ohjaus", "daikin lämpöpumppu"
  NO: "varmepumpe kontroller", "varmepumpe kjerne", "daikin varmepumpe"
  DE: "wärmepumpe controller", "wärmepumpe fernbedienung", "daikin wärmepumpe"
  DK: "varmepumpe controller", "varmepumpe fjernbetjening", "daikin varmepumpe"
```

---

## The Merchant Gap Detection

For each ecosystem × country:

```
1. Count total sellers (Google Shopping, comparison sites)
2. Count good sellers (quality > 70)
3. Calculate merchant gap = (demand - good_sellers) / demand
4. Flag if gap > 0.5
```

---

## The Economics Check

For each product × country:

```
1. Get retail price from observations
2. Get supplier cost (if known)
3. Calculate margin
4. Check if margin > break-even
5. Flag if margin < 0
```

---

## Output Format

```json
{
  "country": "FI",
  "ecosystem": "heat_pump",
  "installed_base": 1800000,
  "merchant_gap": 0.65,
  "search_volume": 5000,
  "retail_price": 250,
  "supplier_cost": 80,
  "margin": 88.25,
  "break_even_cac": 88.25,
  "hypothesis": "Finnish heat pump owners will convert...",
  "falsifier": ">=3 good sellers found",
  "status": "OPEN"
}
```
