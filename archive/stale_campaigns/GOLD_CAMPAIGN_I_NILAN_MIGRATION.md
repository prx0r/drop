# Gold Campaign I — Denmark Nilan Ventilation Control Migration

*Generated: 2026-09-07*
*Score: 83/100*
*Status: ATTACK*

---

## The Pitch

**Nilan says it can supply parts for old units, but private customers are directed to partners. CTS602 migration to HMI touch panel requires latest software and installer. Commerce/services convergence.**

---

## Why This Is #9

| Factor | Data | Score |
|--------|------|-------|
| **Installed base** | Large Danish ventilation installed base | 8/10 |
| **Replacement frequency** | Controllers fail, owners upgrade | 7/10 |
| **Identity difficulty** | "Which Nilan controller do I have?" | 9/10 |
| **Compatibility complexity** | CTS602 → HMI, software requirement | 9/10 |
| **Wrong part cost** | Wrong upgrade = doesn't work | 8/10 |
| **Purchase urgency** | Medium (ventilation, not emergency) | 7/10 |
| **Self-service resolution** | Consumer can photograph controller | 8/10 |
| **Pre-SKU uncertainty** | High — consumer doesn't know version | 9/10 |
| **Digital merchant gap** | Private customers directed to partners | 8/10 |
| **Language fragmentation** | Danish documentation | 8/10 |
| **Visual identifiability** | Photos of controller, unit | 8/10 |
| **Gross margin** | 20-30% on kits | 7/10 |
| **Shipping suitability** | Small parcel, lightweight | 9/10 |
| **Supplier accessibility** | Nilan partners | 7/10 |

**Score: 112/140**

---

## The Evidence

### 1. Nilan directs private customers to partners

Parts for old units available through partners.

### 2. CTS602 migration requires installer

HMI touch panel upgrade requires latest software and should be done by installer.

### 3. Commerce/services convergence

Kit margin + installer referral + later servicing.

---

## What We Build

### "Nilan Migration Resolver"

```
Input: photo of old Nilan controller/unit
Output: exact upgrade bundle + local installer
Graph: unit → controller generation → software requirement → HMI upgrade → extension cable → accessories → installer-required edges
```

---

## Unit Economics

| Metric | Value |
|--------|-------|
| Average order value | EUR 300-800 |
| Gross margin | 20-30% |
| Net per order | EUR 60-240 |
| Break-even orders/month | 10 |

---

## 30-Day Experiment

1. Map CTS602 migration paths
2. Find 3 willing installers
3. Find 1 parts supplier
4. Test migration resolver
5. Launch with installer referral

**Success:** 30 verified migration paths, 3 installers, 1 supplier.

**Falsifier:** Nilan partners already resolve migration adequately.
