# Millions Mining — Findings

## Session: 2026-09-06

### Files Reviewed
1. `docs/millions.md` — 762 lines, failure cases + winning cases
2. `docs/millions2.md` — 1203 lines, deep analysis of $10k/day case
3. `docs/millions3transcript.md` — 365 lines, video transcript
4. `docs/millions4.md` — 1374 lines, $20M revenue blueprint

---

## Key Alpha Found

### 1. The Failure Cases Are More Valuable Than Wins

**$289 Red-Light Mask (July 2026)**
- 10 days, $315 spend, 148 clicks, $2.10 CPC
- 86% impression share, 0 ATC, 0 sales
- **Lesson:** High impression share + clicks + zero ATC = NOT an ads problem. Product-market fit issue.

**Lumbar Pillow (Apr 2026)**
- 2 weeks, $173 spend, 81 clicks, 4 ATCs, 1 checkout, 0 sales
- **Lesson:** Upper funnel working but conversion broken. Trust/offer issue.

### 2. The $10k/day Case Has Hidden Math

- 0.48% CVR, not 4-5%
- $389 AOV
- 7,500 sessions for 36 orders
- **Low-CVR ecommerce is naturally streaky** — 100-200 visits can look dead at 0.48% CVR

### 3. Theo's $10/day → First Sale

- $0.65 CPC
- ~200 clicks needed at 0.5% CVR
- ~$130 spend
- First sale in ~2 weeks is arithmetic, not magic

### 4. Fashion Has Highest Search Demand

- Clothing dominates Google Trends
- Higher returns but higher volume
- Google Shopping scales better than Meta

### 5. $20M Revenue Blueprint (millions4.md)

- 20 Google stores live
- 200k+ orders
- $20M+ revenue
- ~20% net profit after refunds
- Chinese New Year = preparation time for Q2/Q3/Q4

---

## Missed Case Studies

| Source | Data | Why Important |
|--------|------|---------------|
| Helena (Alidropship) | $2,360 in 2 months, <$1k budget | True beginner success |
| Pitiful_Gene795 | $14k in 7 days, 0.48% CVR | Longitudinal data |
| Day 26 diary | $2,184/day revenue | Feed/title changes documented |
| $30/day PMax | 4-5 conversions/day | PMax validation |

---

## Links to Browse

| URL | Content |
|-----|---------|
| forum.alidropship.com/threads/14144 | Helena's case study |
| reddit.com/r/dropshipping/comments/1sbobsp | Day 26 diary |
| reddit.com/r/dropshipping/comments/1sl3sn7 | 0 to 10k |
| github.com/google-marketing-solutions/feedgen | Feed optimization |
| github.com/google-marketing-solutions/merch-intel | Merchant Intelligence |

---

## TODOs

1. [ ] Import Helena's full case study from Alidropship
2. [ ] Import Day 26 diary from Reddit
3. [ ] Clone feedgen and test with sample data
4. [ ] Create economic calculator from MODEL.md
5. [ ] Build opportunity scorer with real data
6. [ ] Create product catalog with 50+ candidates
7. [ ] Score all candidates
8. [ ] Find top 5 opportunities
9. [ ] Create launch plan for #1 opportunity
10. [ ] Set up PostgreSQL schema for tracking
