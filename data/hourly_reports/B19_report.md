# GoldProbe B19 — Great Britain MOT Defect → Repair / Retest

**Date:** 2026-09-07  
**Method:** GoldProbe 2.1 research-native  
**Score:** disabled

## Executive result

**A portable standardized report is not enough. Colocation can overwhelm it.**

DVSA recorded **35,229,047 initial MOT tests in 2024–25**.

Of these:
- **1,924,120** passed after rectification of minor defects at the MOT station
- **7,903,963** remained failed
- initial fail rate: **27.90%**
- final fail rate: **22.44%**.

Source:
https://www.gov.uk/csv-preview/68e682df8c1db6022d0ca269/dvsa-mot-01-mot-test-results-by-class-of-vehicle.csv

DVSA explicitly explains that the initial fail rate is the vehicle as presented, while the final fail rate excludes vehicles fixed for minor defects at the time of the test.

That means:

**9,828,083 initial failure/rectification events**

and **1,924,120 (19.58%)** were rectified at the test station immediately.

This is not the total same-garage repair rate. It is a hard lower/specific signal that colocation captures meaningful work before the customer ever shops elsewhere.

## 1. The network is huge

2024–25:
- **23,097 private MOT test stations**
- 219 other stations
- **66,423 nominated testers**.

Source:
https://www.gov.uk/csv-preview/68e64032dadf7616351e4f3a/dvsa-mot-06-mot-test-stations-and-testers.csv

So this is a mature distributed inspection market, not a scarce-compliance-service opportunity.

## 2. The report itself is exceptionally standardized

MOT defects use:
- Dangerous
- Major
- Minor
- Advisory.

Dangerous = direct/immediate road-safety or serious environmental risk; **fail and do not drive until repaired**.

Major = fail, repair immediately.

Minor = pass but repair ASAP.

Advisory = pass; monitor/repair if necessary.

Source:
https://www.gov.uk/government/news/mot-changes-20-may-2018

The DVSA bulk history API goes further. Each vehicle can carry:
- make/model
- dates
- mileage
- full MOT history
- defect text
- defect type including DANGEROUS, MAJOR, MINOR, ADVISORY and PRS.

Source:
https://documentation.history.mot.api.gov.uk/mot-history-api/download-vehicle-mot-history-data/bulk-file-formats/

This is one of the richest machine-readable maintenance datasets GoldProbe has encountered.

## 3. Repair scope is therefore portable in principle

A driver can take a failed MOT report to another garage.

The categories and exact defect text persist in the public/authorized data graph.

So `STANDARDIZED_DEFECT_CODES_ENABLE_PORTABLE_REMEDIATION` survives technically.

But that does not answer who gets the job.

## 4. The government directly rewards same-site repair

If the driver **leaves the vehicle at the test centre for repair** and it is partially retested within 10 working days:

**partial retest fee = £0**.

If the driver takes it away and returns later:
- certain next-working-day items can still be free;
- within 10 working days a partial retest fee may apply;
- outside those cases, full retest/full fee can apply.

Source:
https://www.gov.uk/getting-an-mot/retests

Maximum car MOT fee is **£54.85**.

Source:
https://www.gov.uk/getting-an-mot/mot-test-fees

So the system itself creates a switching-cost gradient.

## 5. Dangerous defects can physically trap the customer

GOV.UK says a failed vehicle can be taken away only if:
- its existing MOT is still valid
- **and it has no dangerous defect**.

Otherwise it needs repair before normal driving.

Driving a vehicle that failed for a dangerous problem can mean:
- up to **£2,500 fine**
- 3 penalty points
- possible driving ban.

Source:
https://www.gov.uk/getting-an-mot/after-the-test

So theoretical supplier choice remains open, but the car may require a tow/recovery to exercise it.

### `SAFETY_CLASSIFICATION_CREATES_PHYSICAL_CHANNEL_LOCKIN`

This is a new transaction-right dimension.

## 6. Which defects dominate?

For Class 3/4 vehicles in 2024–25, DVSA reports defects present on:

- lamps/reflectors/electrical equipment: **10.89% of tests**
- suspension: **8.73%**
- brakes: **6.63%**
- tyres: **6.39%**
- visibility: **4.54%**.

Dangerous:
- tyres: **4.74% of tests**
- brakes: **2.58%**.

Average defect count per initial failed test: **2.44**.

Source:
https://www.gov.uk/csv-preview/68e682f5750fcf90fa6fff65/dvsa-mot-03-mot-class-3-and-4-vehicles-initial-failures-by-defect-category.csv

This is useful because different defect classes have radically different switching friction.

A bulb can be fixed instantly.

Dangerous tyre/brake failure can immobilize the car.

## 7. Generic neutral routing is already hyper-mature

FixMyCar currently says:
- **3.6m+ drivers**
- **15,000+ garages/mobile mechanics/dealerships** in its network
- dedicated MOT comparison
- repair quote comparison
- combined MOT + service.

Its MOT-specific current page lists **1,672 garages**, with average quoted MOT around £47.

Sources:
https://www.whocanfixmycar.com/
https://www.whocanfixmycar.com/lp/services/mot

So even if colocation did not exist, generic `compare garages` is not a fresh GoldProbe wedge.

## 8. New mechanism: COLOCATED_DIAGNOSIS_REMEDIATION_CAPTURE

The sequence is:

```text
customer brings physical asset to diagnoser
                ↓
standardized defect report
                ↓
diagnoser already has asset + technician + bay
                ↓
same-site repair removes transport/rebooking friction
                ↓
same-site retest receives regulatory price advantage
                ↓
repair captured before marketplace search
```

The crucial point:

**report portability does not imply economic portability.**

## 9. This changes the schema

GoldProbe needs:

### `switching_friction_after_diagnosis`
- asset physically at diagnoser?
- can it move safely/legal?
- towing required?
- repeat visit?
- same-supplier retest discount?
- customer time cost?

and:

### `diagnosis_remediation_colocation`
- can diagnoser repair?
- immediate rectification rate?
- same-site retest advantage?

These may be more predictive than report standardization.

## 10. The real gold here may be the dataset, not the middleman business

DVSA gives:
- weekly bulk snapshot
- daily delta files
- asset-level historical defects
- model/make
- mileage
- test dates
- defect semantics.

This enables:

`make × model × age × mileage × geography × defect category -> next-MOT risk`

Potential products:
- fleet predictive maintenance
- pre-MOT recommendations
- used-car risk
- garage inventory/parts forecasting
- insurer/warranty analytics.

That's much more novel than another failed-MOT garage marketplace.

## 11. B19 falsification review

### Supported
- standardized report
- portable defect data
- huge repeat compliance volume.

### Strongly supported
- same-site repair has explicit economic advantage
- immediate station rectification is material
- dangerous failure creates physical switching friction.

### Falsified
- portable report alone creates neutral marketplace whitespace.
- enormous regulated failure volume implies easy leadgen.
- physical supplier choice equals practical transaction choice.

## 12. Autonomous next probe — B20 Ireland NCT

This is the cleanest possible A/B.

Great Britain:
**MOT testing commonly sits inside repair garages.**

Ireland:
**NCT inspection is institutionally centralized/separated from repair.**

So B20 asks:

> **If the diagnosing institution cannot sell the repair, does standardized failure demand become materially more open and valuable to a repair-routing intermediary?**

That directly tests whether colocation is causal rather than merely correlated with B19's marketplace maturity.
