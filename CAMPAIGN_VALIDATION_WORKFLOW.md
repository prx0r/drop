# Campaign Validation Workflow

*Generated: 2026-09-07*
*Status: STANDARD — How to validate any campaign*

---

## The Flow

```
1. TAKE OWNERSHIP
   Load campaign JSON
   Parse all fields

2. ASSESS OBJECTIVELY
   Run binary gate (10 statements)
   Run score rubric (20 statements)
   Identify all UNKNOWN fields

3. SEARCH TO VALIDATE
   For each UNKNOWN:
     - What source would answer it?
     - Search web / BigQuery / Gmail
     - Find evidence
     - Update field with evidence

4. UPDATE STATUS
   Re-run binary gate
   Re-run score rubric
   Determine new status
   Log mutation

5. DECIDE NEXT ACTION
   ATTACK → proceed to supplier contact
   VERIFY → continue validation
   WATCH → keep monitoring
   REJECT → kill and log lesson
```

---

## Example: Helios ELS

### Step 1: Take Ownership

Loaded campaign JSON. Status: WATCH.

### Step 2: Assess Objectively

Binary Gate:
- B5: UNKNOWN (consumer can self-identify)
- B6: UNKNOWN (shippable without technician)
- B8: UNKNOWN (supplier will sell)
- B10: UNKNOWN (legal responsibility)

Score: 150/200 → VERIFY

### Step 3: Search to Validate

**B5 search:** "Helios ELS NFC technician configuration"
- Found: NFC models require authorised technician
- Found: Older non-NFC models may be simpler
- Updated: B5 = PARTIAL

**B6 search:** "Helios ELS fan insert replacement DIY"
- Found: Fan insert is modular, slides into housing
- Found: Haustechnik Binder sells directly to consumers
- Updated: B6 = PARTIAL

**B8 search:** "Haustechnik Binder Helios ELS"
- Found: EUR 218.90, Trusted Shops 4.87/5, accepts PayPal
- Updated: B8 = YES

**B10 search:** "Germany electrical installation regulations fan replacement"
- Found: Replacing fan insert is maintenance, not installation
- Found: Electrical connection requires specialist
- Updated: B10 = PARTIAL

### Step 4: Update Status

Re-run binary gate: B5/B6/B10 = PARTIAL, B8 = YES
Re-run score: 170/200 → ATTACK (with caveats)

### Step 5: Decide Next Action

ATTACK with caveats:
- Only target older non-NFC models
- Exclude NFC models
- Include electrical disclaimer
- Verify supplier terms

---

## The Rule

**Agents may create unlimited candidates. They may not create a Gold Campaign until every required hard gate is PASS.**

This eliminates persuasive-but-economically-useless research.
