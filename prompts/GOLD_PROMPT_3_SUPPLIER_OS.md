# Gold Prompt 3: Agent-Native Supplier OS

*For autonomous exploration of contractor operations tools*

---

## The Thesis

Contractors lose money on:
- Missed calls (estimated 30-50% of inbound leads)
- Quote follow-up (hours of unbillable time)
- Scheduling coordination (phone tag)
- Invoice chasing (cash flow delay)
- Review management (reputation risk)
- CRM maintenance (data entry burden)

The opportunity is to provide an **AI front desk** that handles all of this, in exchange for **live proprietary supply data**.

---

## The Exploration Protocol

### Phase 1: Contractor Pain Mapping

For each service category × country:

```
1. What's the average job value?
   - £800-£1,500 for EV installation
   - £3,000-£8,000 for heat pump
   - £200-£500 for electrical

2. What's the missed call rate?
   - Industry average: 30-50% of inbound leads
   - Each missed call = lost revenue

3. What's the quote follow-up time?
   - Average: 2-3 days
   - Customer expectation: same day

4. What's the invoice collection time?
   - Average: 30-60 days
   - Cash flow impact: significant
```

### Phase 2: AI Receptionist Value Proposition

For each contractor type:

```
1. What does the AI handle?
   - Missed calls → callback
   - Booking → calendar
   - Rescheduling → calendar
   - Quote follow-up → SMS/email
   - FAQs → instant answers
   - Lead qualification → scoring
   - Diary management → calendar
   - Reminders → automated
   - Invoice chasing → automated
   - Review requests → automated
   - Basic CRM → contact management

2. What does the contractor get?
   - Time savings (hours/week)
   - Higher conversion rate
   - Faster quote response
   - Better customer experience
   - Repeat business

3. What do we get?
   - Availability data
   - Service area data
   - Pricing data
   - Quality data
   - Completion data
   - Conversion data
```

### Phase 3: Supply Graph Construction

For each contractor:

```
1. Basic info
   - Company name
   - Qualifications
   - Insurance
   - Service area

2. Capacity
   - Current availability
   - Typical lead time
   - Max jobs per week

3. Pricing
   - Typical job value
   - Quote range
   - Payment terms

4. Quality
   - Completion rate
   - Cancellation rate
   - Customer rating
   - Repeat rate
```

### Phase 4: Platform Economics

```
1. Revenue model
   - Platform fee: 8-12% of completed job
   - AI receptionist: included in fee
   - No upfront cost to contractor

2. Unit economics
   - Average job: £1,100
   - Platform take: £88 (8%)
   - Dispute risk: £1,000 (10 jobs)
   - Net per job: £88

3. Flywheel
   - More contractor usage → better supply graph
   - Better supply graph → better agent answers
   - Better agent answers → more bookings
   - More bookings → more contractor demand
   - More contractor demand → more contractor usage
```

### Phase 5: Hypothesis Generation

```
H1: [specific claim about contractor tool adoption]
H0: [what would explain the data without our claim]
Falsifier: [concrete condition that would kill H1]

Evidence:
- [observation 1]
- [observation 2]
- ...

Status: OPEN / SUPPORTED / FALSIFIED
```

---

## Example: UK EV Charger Installer AI Receptionist

### Contractor Pain
- Missed calls: 30-50% of inbound leads
- Quote follow-up: 2-3 days average
- Invoice collection: 30-60 days
- Customer expectation: same-day response

### AI Receptionist Value
- Handles missed calls → callback
- Booking → calendar
- Quote follow-up → SMS
- FAQs → instant answers
- Lead qualification → scoring

### What We Get
- Availability data
- Service area data
- Pricing data
- Quality data
- Completion data
- Conversion data

### Hypothesis

```
H1: UK EV charger installers will adopt an AI receptionist
    that provides live availability and pricing data in
    exchange for reduced admin burden.

H0: Contractors prefer manual phone/email and won't adopt
    automated systems.

Falsifier: <10% of contacted installers express interest
    in AI receptionist after 30-day outreach.
```

---

## Output Format

```json
{
  "country": "GB",
  "service": "ev_charger_installation",
  "contractor_count": 2074,
  "avg_job_value": 1100,
  "missed_call_rate": 0.4,
  "ai_receptionist_value": "high",
  "hypothesis": "UK EV installers will adopt AI receptionist...",
  "falsifier": "<10% interest after 30-day outreach",
  "status": "OPEN"
}
```
