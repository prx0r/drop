# Gold Prompt 2: Agent-Native Services

*For autonomous exploration of local service markets*

---

## The Thesis

There exists a class of services where:
- High ticket value (£500-£5,000)
- Fragmented supplier base (many small operators)
- Phone-tag friction (customers call, operators miss calls)
- Predictable service area (geographic constraint)
- Structured qualification (OZEV, MCS, certifications)
- Measurable provider quality (ratings, completion rates)

The opportunity is to be the **provider the agent can transact with cleanly**, rather than hoping it chooses a random contractor.

---

## The Exploration Protocol

### Phase 1: Service Category Discovery

For each country:

```
1. What high-ticket services exist?
   - EV charger installation
   - Heat pump installation
   - Solar panel installation
   - Boiler replacement
   - Electrical upgrades
   - Garage doors
   - Roofing
   - Drainage

2. What's the ticket size?
   - £500-£5,000 range
   - Enough to fund acquisition
   - Not so high that disputes are catastrophic

3. What's the supplier fragmentation?
   - Many small operators
   - No dominant national player
   - Local service areas
```

### Phase 2: Qualification Mapping

For each service × country:

```
1. What certifications exist?
   - OZEV-approved installers
   - MCS-certified installers
   - Electrical qualifications
   - Gas safety certificates

2. Where is the data?
   - Government directories
   - Trade associations
   - Manufacturer lists
   - Company registries

3. Can it be structured?
   - Postcode-searchable
   - Certification-verified
   - Availability-checkable
```

### Phase 3: Economics Check

For each service × location:

```
1. What's the typical job value?
   - £800-£1,500 for EV installation
   - £3,000-£8,000 for heat pump
   - £200-£500 for electrical

2. What's the platform take?
   - 8-12% of completed job
   - £80-£120 per EV install
   - £300-£800 per heat pump

3. What's the dispute risk?
   - Single £1,000 loss = 10 successful jobs
   - Need installation evidence
   - Need clear scope/change-order rules
```

### Phase 4: Supply Graph Construction

For each service × location:

```
1. Find providers
   - Government directories (OZEV, MCS)
   - Company registries
   - Google Business
   - Trade associations

2. Verify qualifications
   - Certification status
   - Insurance
   - Reviews
   - Response time

3. Build service graph
   - Provider → service area
   - Provider → qualifications
   - Provider → availability
   - Provider → pricing
   - Provider → quality score
```

### Phase 5: Hypothesis Generation

```
H1: [specific claim about service market]
H0: [what would explain the data without our claim]
Falsifier: [concrete condition that would kill H1]

Evidence:
- [observation 1]
- [observation 2]
- ...

Status: OPEN / SUPPORTED / FALSIFIED
```

---

## Example: UK EV Charger Installation

### Service Category
- Ticket: £800-£1,500
- Fragmentation: ~2,074 OZEV-approved installers
- Qualification: OZEV-approved, BS 7671 compliant
- Service area: Postcode-based

### Supplier Graph
```
OZEV Directory → 2,074 installers
    ↓
Postcode coverage
    ↓
Charger compatibility
    ↓
Quote bands
    ↓
Availability
    ↓
Quality score
```

### Economics
- Job value: £1,100
- Platform take: £88 (8%)
- Dispute risk: £1,000 (10 jobs)
- Net per job: £88

### Hypothesis

```
H1: UK homeowners will use an AI agent to find, compare and book
    OZEV-approved EV charger installers at an acquisition cost
    below £88 per completed job.

H0: Rightcharge and similar services already solve this adequately.

Falsifier: >=3 OZEV-approved installers with <48h availability
    found in any single postcode area.
```

---

## The Service Graph

```
Postcode: NG7 (Nottingham)
 └─ EV charger installation
      ├─ Installer A
      │   ├─ OZEV approved
      │   ├─ service radius: 15km
      │   ├─ next availability: Thursday
      │   ├─ accepted chargers: Zappi, Ohme, Hypervolt
      │   ├─ installation types: tethered, untethered
      │   ├─ typical price: £900-£1,100
      │   ├─ acceptance rate: 85%
      │   ├─ cancellation rate: 5%
      │   └─ rating: 4.8/5
      │
      ├─ Installer B
      └─ Installer C
```

---

## The Contractor OS

Offer: **"We'll give you an AI front desk."**

It handles:
- Missed calls
- Booking
- Rescheduling
- Quote follow-up
- SMS
- FAQs
- Lead qualification
- Diary
- Reminders
- Invoice chasing
- Review requests
- Basic CRM

In exchange you obtain:
- Availability
- Service area
- Jobs accepted/rejected
- Pricing ranges
- Skills
- Equipment supported
- Response time
- Completion data
- Conversion rate

---

## Output Format

```json
{
  "country": "GB",
  "service": "ev_charger_installation",
  "ticket_value": 1100,
  "platform_take": 88,
  "provider_count": 2074,
  "provider_density": "high",
  "qualification": "OZEV-approved",
  "hypothesis": "UK homeowners will use AI agent...",
  "falsifier": ">=3 installers with <48h availability",
  "status": "OPEN"
}
```
