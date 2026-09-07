# Maritime Norway — Deep Intelligence Report

*Generated: 2026-09-07*
*Status: HIGH-SIGNAL — AKVA feed systems + KET separator obsolescence*

---

## The Opportunity

> **Build the compatibility/obsolescence layer between a vessel engineer's photo/nameplate/requisition and the existing maritime RFQ/procurement networks.**

This avoids the heat-pump problem where the consumer owns the asset but the installer actually chooses and buys the component. On commercial vessels, crew/engineers commonly create the requisition themselves.

---

## Market Size

- 1.067 million recreational boats
- 4,989 registered fishing vessels (89% active)
- Major commercial/offshore fleet
- 990 seawater salmon/trout sites

---

## Top 12 Maritime Subgraphs

| Rank | Subgraph | Score | Model |
|------|----------|-------|-------|
| 1 | AKVA aquaculture feed-system spares | 96 | B2B resolution → RFQ/PO |
| 2 | GEA/Alfa Laval obsolete separator controls | 95 | migration/repair graph |
| 3 | AKVA cameras/sensors/winches | 91 | B2B exact-part resolver |
| 4 | Plate heat-exchanger plates/gaskets | 90 | exact-fit procurement |
| 5 | Marine refrigeration/HVAC obsolete components | 89 | replacement/supersession |
| 6 | Starting-air compressor service kits | 88 | scheduled recurring parts |
| 7 | Marine sewage/vacuum toilet systems | 86 | installed-system graph |
| 8 | Commercial pump/compressor service kits | 85 | photo/nameplate → PO |
| 9 | AERON legacy HVAC equipment | 84 | vessel/project history graph |
| 10 | Commercial engine auxiliary/electrical parts | 79 | professional resolver |
| 11 | Ballast-water sensors/controls/consumables | 74 | compliance lifecycle |
| 12 | Legacy thruster/windlass | 63 | benchmark / selective |

---

## #1: AKVA Feed System Resolver

AKVA has 116-page spare-parts catalogue with machine-readable BOM-like relationships.

Example:
```
Selector Valve CF32 L60 CCS
    #0101561
→ Cabinet #0103246
→ CCS Selector Vari Module #0101081
→ S-Pipe Assembly #0101554
→ motor/gear #10083
→ sensor plate #0101557
→ inductive sensor #10051
→ seals, cables, fittings
```

AKVA says users needing spare parts should contact them and can call for urgent requests. Long lead times on PLC modules, VSDs, circuit boards.

### Business Model

Not ecommerce. RFQ/PO routing:
```
customer → Drop resolver → verified AKVA part/BOM → RFQ to AKVA/authorized source → PO
```

Charge: supplier referral / transaction % or buyer procurement SaaS.

---

## #2: GEA/Alfa Laval Separator Obsolescence

KET Marine holds ~30,000 separator spare parts. UQP has represented marine suppliers since 1946.

### Westfalia C7/D10 → Siemens I/O-4 conversion

Old controls on OSC/OSD/OSE separators. GEA stopped supplying. KET offers conversion kit.

### Alfa Laval EPC-50

Fitted on S/P separators 1999-2010. Alfa Laval stopped supplying spares 2023. KET can provide new/reconditioned boards.

---

## #3-12: Additional Maritime Subgraphs

See full report for details on AKVA cameras, plate heat exchangers, marine refrigeration, Sperre compressors, sewage systems, pumps, AERON HVAC, engine parts, ballast water, thrusters.

---

## Supplier Types

### Type A — Perfect Partners
UQP / MPCC / KET (30k parts, live stock, engineering capability)

### Type B — Internally Strong, Externally Analog
AERON (47 years of project history), Maritim Motor (Yanmar parts)

### Type C — Very Analog but Generic
Maritime Supply (hydraulics, pneumatics, spares)

### Type D — Digital Competitors
ASIL (thousands of referenced part numbers), VesselCore (structured intake)

---

## The Maritime Drop Architecture

```
VESSEL
IMO 1234567
        │
        ├── Yanmar 6EY18ALW
        │       ├── turbo, pump, service kits
        │
        ├── Alfa Laval S separator
        │       ├── EPC50 board/repair/obsolete/successor
        │       └── service kit
        │
        ├── Sperre compressor
        │       ├── serial, operating hours, next kit
        │
        ├── AERON HVAC
        │       └── installed project BOM
        │
        └── Wärtsilä sewage plant
                ├── pumps, valves, controls

                        ↓

             CURRENT SUPPLY GRAPH

UQP/KET       €X     2 days
MPCC          €Y     stock
OEM           €Z     14 days
repairer      €A     exchange
alternative   €B     verified compatible
```

---

## Two Experiments

### Experiment A — AKVA Feed Systems
Extract 116-page catalogue into structured graph. Generate 100 technician queries. Benchmark vs Google/ChatGPT/AKVA site.

### Experiment B — UQP/KET Separator Lifecycle
Start with Westfalia C7/D10 + Alfa Laval EPC-50. Build migration graph. Contact UQP.

---

## Sources

1. AKVA group — 116-page spare-parts catalogue
2. UQP/KET — 30,000 separator spare parts
3. IMPA — procurement of spare parts
4. Sperre — 30 years spare-parts availability
5. MPCC — Wärtsilä/Hamworthy parts
6. AERON — 47 years of project history
7. Framo — 8,000 unique spare components (avoid)
