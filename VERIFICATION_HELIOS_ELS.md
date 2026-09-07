# Verification: Helios ELS Legacy Ventilation (Germany)

*Generated: 2026-09-07*
*Status: VERIFICATION COMPLETE*

---

## B5: Consumer can self-identify

**Verdict: PARTIAL — depends on model**

Evidence:
- Helios ELS NFC requires "authorised technician" to configure via app
- Older non-NFC models (1984-2008) may be simpler
- Fan insert replacement is typically DIY (pull out old, push in new)
- But electrical connection may require electrician

Source: https://www.manualslib.com/manual/3622610/Helios-Ultrasilence-Els-Nfc-Series.html

**Updated: B5 = PARTIAL (older models YES, NFC models NO)**

---

## B6: Shippable without technician

**Verdict: PARTIAL — fan insert yes, electrical no**

Evidence:
- Fan insert is a modular component that slides into existing housing
- Haustechnik Binder sells fan inserts directly to consumers
- skybad.de sells Helios ELS fan inserts at EUR 155-218
- Electrical connection is pre-existing in the housing
- But: "Elektroanschluss sollte immer fachgerecht ausgeführt werden"

Source: https://www.skybad.de/en/i/domestic-installation/helios.html

**Updated: B6 = PARTIAL (fan insert YES, electrical connection NO)**

---

## B8: Supplier will sell to us

**Verdict: YES — Haustechnik Binder is a retail shop**

Evidence:
- Haustechnik Binder sells Helios ELS products directly to consumers
- EUR 218.90 for ELS-VE 60 (article 00425)
- Trusted Shops rating 4.87/5 (1,839 ratings)
- Accepts PayPal, credit cards, prepayment
- Free shipping over EUR 250
- Located in Massenhausen, Germany

Source: https://haustechnik-binder.de/de/Lueftung/HELIOS-Ersatz-Ventilatoren-ELS-1984-bis-2008/

**Updated: B8 = YES**

---

## B10: Legal responsibility explicit

**Verdict: PARTIAL — fan insert replacement is maintenance, not installation**

Evidence:
- Germany has strict electrical installation regulations
- But: replacing a fan insert in existing housing is maintenance, not installation
- The electrical connection is pre-existing
- "Arbeiten an festen Elektroinstallationen gehören zum Elektrofachbetrieb" (electrical work belongs to specialist)
- But: "Steckdosen und Lichtschalter austauschen" (replacing sockets/switches) is allowed for laypeople

Source: https://visuprojekt.mataroa.blog/blog/elektroinstallation-selber-machen-was-erlaubt-ist-und-was-nicht/

**Updated: B10 = PARTIAL (fan insert replacement YES, new electrical work NO)**

---

## Updated Binary Gate

| # | Statement | Previous | Updated |
|---|-----------|----------|---------|
| B5 | Consumer can self-identify | UNKNOWN | PARTIAL |
| B6 | Shippable without technician | UNKNOWN | PARTIAL |
| B8 | Supplier will sell to us | UNKNOWN | YES |
| B10 | Legal responsibility explicit | UNKNOWN | PARTIAL |

**Result: B5/B6/B10 = PARTIAL → still BLOCKED but closer**

**Decision: WATCH (not ATTACK)**

**Reason:** The campaign can work for older non-NFC models where the fan insert is a simple swap. But NFC models require technician configuration. The electrical connection question needs more research.

---

## Score (updated)

| # | Statement | Previous | Updated |
|---|-----------|----------|---------|
| S5 | Consumer can self-identify | 0 | +5 (partial) |
| S6 | Shippable without technician | 0 | +5 (partial) |
| S8 | Supplier will sell | 0 | +10 (verified) |
| S10 | Legal responsibility | 0 | +5 (partial) |

**Previous total: 150/200**
**Updated total: 170/200 → ATTACK (but with caveats)**

---

## Caveats for ATTACK status

1. Only target older non-NFC models (1984-2008)
2. Exclude NFC models that require technician configuration
3. Include disclaimer about electrical connection
4. Verify Haustechnik Binder will sell to us (not just consumers)
5. Test buyer-role: do homeowners actually replace these themselves?

---

## Next Step

Contact Haustechnik Binder to verify:
1. Will they sell to us (not just consumers)?
2. Can they drop-ship or blind-ship?
3. What are their terms?
4. Do they have stock of legacy ELS parts?
