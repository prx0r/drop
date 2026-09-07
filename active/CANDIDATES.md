# CANDIDATES

*Current pipeline state. Updated 2026-09-07.*

---

## Pipeline Summary

| State | Count | Candidates |
|-------|-------|------------|
| DISCOVERED | 5 | Robot Vacuums FI, Air Purifiers FI, EV Chargers FI, Air Conditioners FI, Sleeping Bags NO |
| DEMAND_VERIFIED | 1 | Hunter Hydrawise FI |
| SUPPLY_PATH_VERIFIED | 1 | RIDGID SeeSnake FI |
| HOLD_VALIDATE | 1 | Davis Weather NO |
| KILLED | 5 | Bosch, HIKMICRO, Airthings, Hunter (as store), Robot Mowers FI |

---

## Active Pipeline

### Tier 1: Finland — Highest Potential

| Lead | Products | Shops | Good Sellers | Supplier | Status | Action |
|------|----------|-------|--------------|----------|--------|--------|
| **Robot Vacuums** | 341 | 22 | 5 | DistriHUB (dropship) | EMAIL_SENT | Waiting for response |
| **EV Chargers** | 435 | 21 | 3 | BESEN (China) | EMAIL_SENT | Waiting for response |
| **Air Purifiers** | 625 | 24 | 4 | TBD | DISCOVERED | Research supplier |
| **Air Conditioners** | 60 | 17 | 2 | TBD | DISCOVERED | Research supplier |

### Tier 2: Norway

| Lead | AOV NOK | Supplier | Status | Action |
|------|---------|----------|--------|--------|
| **Davis Weather** | 15,400-39,400 | Flak/Hovdan | ACKNOWLEDGED | Waiting for human response |
| **Sleeping Bags** | 2,000-8,000 | TBD | DISCOVERED | Research supplier |
| **Wood Stoves** | 15,000-50,000 | TBD | DISCOVERED | Research supplier |

---

## What's Live on moltwork.com

| URL | Content | Language | Worker |
|-----|---------|----------|--------|
| /davis | Davis weather stations landing | Norwegian | moltwork-davis |
| /davis/vantage-vue-vs-pro2 | Vue vs Pro2 comparison | Norwegian | moltwork-davis |
| /davis/hytte | Davis for cabin monitoring | Norwegian | moltwork-davis |
| /davis/vinter-drift | Winter operation guide | Norwegian | moltwork-davis |
| /davis/home-assistant | Davis + Home Assistant | Norwegian | moltwork-davis |
| /robotvacuum | Robot vacuum comparison | Finnish | moltwork-fi |
| /ev-charger | EV charger comparison | Finnish | moltwork-fi |
| /saastopuhdistin | Air purifier comparison | Finnish | moltwork-more |
| /talvikit | Winter car accessories | Finnish | moltwork-more |

---

## Emails Sent (12 total)

| # | To | Purpose | Status |
|---|-----|---------|--------|
| 1 | Flak@flak.no | Davis dealer application | ACKNOWLEDGED |
| 2 | Post@hovdan.no | Davis backup supplier | SENT |
| 3 | yritysmyyntipalvelu@onninen.com | RIDGID 70808 price | SENT |
| 4 | ridgid.scandinavia@emerson.com | RIDGID authorization | ACKNOWLEDGED |
| 5 | hello@distrihub.eu | Robot vacuums Dreame/Roborock | SENT |
| 6 | info@elkogroup.com | Dreame Nordic distributor | SENT |
| 7 | info@besen-group.com | EV chargers Chinese | SENT |
| 8 | sales@garden.roborock.com | Roborock online reseller | SENT |

---

## State Machine Rules

Each run must: ADVANCE, KILL, or RESOLVE a field.
If none → run produced no useful information.
