# User Message — Thesis Refinement + Installed Base Corrections

*Sent: 2026-09-07*
*Status: SAVED WORD-FOR-WORD*

---

Yes. The market research supports the thesis strongly—but it also tells us **where not to compete**.

The broad ideas are already being built. The opportunity is to go much narrower and own the ugly data layer that the broad platforms cannot economically maintain.

The single strongest ecommerce datapoint I found is from Shopify's **Q2 2026 commerce data**: in research/specification-heavy categories, AI-referred shoppers converted at roughly **2× the rate of organic-search shoppers**. Shopify also found that traffic originating from structured Shopify Catalog data converted about **2× better than traffic from scraped/third-party product data**. ([Shopify][1])

Even more directly supportive of GeoDrop: Shopify says **71% of AI-attributed orders in 2025 came from long-tail categories**, and categories outside its top 100 now account for almost 55% of Shopify sales. Shopify's own framing is essentially that AI is unusually good at matching a specific buyer to a specialist product. ([Shopify][2])

So the core economic premise is real:

> **AI is disproportionately useful when the purchase requires reasoning about specifications, compatibility, context or suitability.**

That is exactly where we should operate.

---

# Market map

| Opportunity | Demand evidence | Existing competitors | Gap remaining | My score |
| --- | --- | --- | --- | ---: |
| **Agentic Job Broker** | Very strong | Checkatrade, Bark, Rated People, Taskrabbit, Thumbtack, Rightcharge | **Accepted-job routing + agent-native + vertical UK supply** | **9.5/10** |
| **Free Front Desk → Supplier Graph** | Extremely strong | Probook, Avoca, ServiceTitan-class products | **Free/WhatsApp-first for small UK trades as data acquisition** | **9/10 as wedge** |
| **Agentic Replacement Broker / GeoDrop 2.0** | Extremely strong | FixPart, Partium, PartsNow | **Cross-supplier fitment + local-language + geographical routing** | **9.5/10** |
| **Visual Compatibility Graph** | Proven | Partium, PartsNow, Shopify image search | **Exact compatibility + negative fitment + supersessions** | **9/10 moat** |
| **Photo → PO for trades** | Proven | MRO Command, SpareFinder, Buyer24, Corivo | **Small trades + local wholesalers instead of industrial enterprise** | **8/10** |
| **Supplier Normalization Layer** | Huge established market | Akeneo, Pimcore, Plytix, Salsify | **Tiny analogue suppliers → machine API automatically** | **8.5/10 infra** |
| **Compatibility/Fitment API** | Proven category | ACES/PIES, Parts Resolve | **Non-automotive vertical fitment** | **9/10 asset** |
| **Agentic Aftersales-as-a-Service** | Strong | Partful, Partium, Akeneo | Smaller OEM/distributor long tail | **8/10** |
| **Nordic Installed-Base Microverticals** | Excellent structural demand | Vertical incumbents vary | **Hyper-specific language + legacy + supersession niches** | **9/10 research target** |
| **Supplier Trust Graph** | Clearly valuable | Checkatrade/Thumbtack ratings | Outcome-derived machine trust | **8.5/10 moat** |

---

# 1. Agentic Job Broker — validated, but move fast

Google now does almost exactly the demand-side behavior we predicted.

A user can ask Google to check local service pricing and availability. Google calls multiple businesses, collects the answers and sends the customer a comparison. Google AI Mode now also handles categories including electricians and other home services. ([Google Help][3])

But Google's standard "check pricing" flow explicitly says **it does not create the final booking**; the user receives the information and then contacts the business. ([Google Help][3])

That's our opening:

```
GOOGLE
"What does it cost and who's available?"

OUR BROKER
"Three can do it.
Jim: £925 Thursday
Sarah: £980 Friday
ABC: £895 Monday

Choose one."

→ Jim accepts
→ Jim pays lead unlock
→ contact details released
→ done
```

Taskrabbit gives even stronger validation. Its new Home Services API uses essentially:

```
Estimate
   ↓
Availability
   ↓
Bid
   ↓
Book
   ↓
Project status
```

It exposes real-time service eligibility, pricing and appointment windows programmatically. ([Taskrabbit Developer Hub][4])

That is almost precisely our proposed service schema.

### But the competition is real

Thumbtack is already moving **photo/voice → problem diagnosis → appropriate professional**. In early testing, it says 87% of customers found the photo/voice input valuable. Thumbtack has roughly **300,000 local service businesses** in its network. ([Thumbtack][5])

And there is now an even more direct competitor: **GeraHome** claims to expose provider search, availability, insurance status, pricing and booking through REST + MCP, including UK coverage. ([GeraHome][6])

I would not panic about GeraHome yet. Its own pages give inconsistent geographic figures—20 countries on one comparison page, 50+ elsewhere and 60+ on its facts page—so I would treat it as **evidence that people see the opportunity**, not yet evidence that somebody has built an impregnable network. ([GeraHome][7])

### The UK incumbents leave a clear opening

Checkatrade's current model starts at £59/month and lets trades choose postcode areas and desired lead volume. Its consumer EV page sends a job to up to three installers who then independently contact the customer. ([Join Checkatrade][8])

Rated People says it receives around **1 million job posts annually** and traditionally charges membership plus lead access; Bark currently prices its lead currency at £1.80/credit, with lead cost depending on service and job scope. ([Bark Help Center][9])

There is obvious contractor frustration with shared/stale/unresponsive leads in recent UK Reddit discussions. That's anecdotal rather than market-wide proof, but the recurring complaint is exactly what our model fixes: people resent paying to chase someone who never answers. ([Reddit][10])

Our innovation should therefore be:

> **Don't charge Jim to contact an unqualified stranger. Charge Jim only after we've collected enough job information, Jim has seen the anonymized job, and Jim explicitly says "yes, I want this."**

That's qualitatively different.

---

# 2. Free receptionist → Supplier Graph

This part is overwhelmingly validated.

Probook's current product claims:

- 58,000+ customer interactions daily;
- 82% handled end-to-end;
- lead capture via voice/web;
- equipment and job-history cleaning;
- historical-data-based real-time dispatching;
- ETA and revenue forecasting. ([Probook][15])

Avoca similarly has inbound/outbound AI, speed-to-lead, scheduling, web chat and deep integrations into field-service systems across hundreds of home-service businesses. One of its customers says Avoca handles about 70% of call volume. ([Avoca AI][16])

So:

### Generic AI receptionist = red ocean.

### Free receptionist as supply-data acquisition = excellent.

Our product is not:

> "Buy an AI receptionist from us."

It is:

> "We'll handle your missed calls for free because it lets us understand what work you want."

Then:

```
conversation
→ job taxonomy
→ availability
→ price behavior
→ accepted/rejected work
→ geography
→ supplier score
```

That's materially different from competing head-on with Avoca/Probook.

---

# 3. Agentic Replacement Broker — strongest product opportunity

This has unusually strong support.

Shopify's most recent data says the strongest AI advantage occurs in **spec-led categories**, precisely where consumers compare compatibility, specifications and trade-offs. AI-referred shoppers there convert around **2× organic**. ([Shopify][1])

That's almost a direct empirical validation of:

> Bosch pump / HVAC board / heat-pump remote / obscure cottage component > fashionable commodity product.

Shopify also reports that **71% of AI-attributed orders came from long-tail categories** in 2025. ([Shopify][2])

### But don't begin with generic appliance spares

I found a formidable incumbent.

**FixPart** operates localized sites across Norway, Finland, Sweden, Denmark, the UK and most of Europe, claims 15M+ spare parts, and already has model-based fitment and a "guaranteed fit" feature. If you're uncertain, you can send them a photo of the model plate and requested component and they manually return the correct product link. ([FixPart][17])

That tells us two things simultaneously:

**Demand is extremely real.**

**"Generic appliance replacement parts for Norway" is not our niche.**

Go narrower/weirder.

---

# 4. Photo → part identification is definitely real

There are multiple strong competitors.

**PartsNow** launched Photo Match in July 2026 for heavy-duty truck parts: photo → component classification → catalog matches → vehicle fitment → OEM cross-reference → live pricing. ([partsnow.ai][18])

**Partium** does image, OCR, semantic text, barcode and BoM-based parts search. Deutsche Bahn reportedly uses it across 95 maintenance plants and 12,200 users, with Partium claiming 46,800 person-days saved annually. ([Partium][19])

Partium's technical documentation explains that its engine can compare:

```
image → image
image → text
text → image
text → text
```

and combine multiple modalities to rank candidate parts. ([Partium Docs][20])

And Shopify's Catalog API itself now supports **image search plus multimodal text+image search across Catalog**. ([Shopify][21])

Therefore:

> **Do NOT make "we identify parts from photos" the moat.**

That is becoming commodity infrastructure.

Make:

> **photo → exact asset → exact component → compatible/superseding part → evidence → local commercial availability.**

---

# 5. Compatibility is the moat — there's decades of evidence

Automotive gives us an extremely useful precedent.

The automotive aftermarket built an entire industry data standard called **ACES** specifically for communicating **fitment** between products and vehicle configurations. It is backed by multiple relational reference databases and machine-readable APIs. ([Auto Care][22])

Walmart's marketplace literally requires manufacturer brand + exact MPN to associate listings with compatibility/fitment records. ([Walmart Developer][23])

That is the closest analogue to our thesis:

> **Someone will eventually need ACES for everything else.**

Heat pumps, boilers, commercial kitchen equipment, cabin water systems, robot mowers, coffee machines, garage-door motors etc. don't have a universally clean equivalent.

There is already a small startup called **Parts Resolve** building evidence-backed supersession, cross-reference and fitment APIs for automotive parts. ([Parts Resolve][24])

Again: validation.

The opportunity is **non-automotive ACES**.

---

# 6. Supersession data is especially valuable

This pain is everywhere.

A recent parts-industry article describes the three critical mappings aftermarket catalogs need as:

```
OEM → aftermarket
competitor → equivalent
old SKU → superseding SKU
```

and notes that bad mappings directly cause wrong-part orders. ([Uncap][25])

Recent Reddit examples illustrate how ugly the problem gets in the wild. One LG owner found **five different apparently compatible gasket part numbers** from official LG pages/support channels for a single washing-machine model. Another HVAC owner had a technician who couldn't source an old circuit board and resorted to posting photographs online. ([Reddit][26])

That's exactly our product.

Not:

> "here are visually similar pumps."

But:

> "OEM number X was replaced by Y in 2017; Y fits revisions A–C, but not revision D; here is the source evidence."

That data is worth money.

---

# 7. Photo → PO is also real, and industrial players are racing toward it

This one surprised me by how thoroughly it is being validated.

**MRO Command** already does:

```
photo/text/email
→ AI identifies part
→ constructs RFQ
→ sends to vendors
→ normalizes quotes
→ compares price/lead time/freight
→ generates PO
```

It claims a network of 5,000+ MRO suppliers. ([MRO Command][27])

**Buyer24** similarly performs urgent multi-supplier RFQs, cross-reference matching and automated supplier follow-ups. ([Buyer24.ai][28])

**Corivo** connects the needed component to asset history, previous suppliers, price, lead time and purchase history before recommending the next purchasing action. ([Corivo][29])

**Andustry**, a YC company, is using AI to source obscure industrial parts globally and then manually verifies suppliers. ([Andustry][30])

So generic industrial procurement is getting crowded.

But I don't see these companies concentrating on:

> **one-man electrician → WhatsApp photo → nearby CEF/Edmundson/Screwfix/etc → correct part waiting tomorrow morning.**

That's a much cheaper, lighter product.

And it feeds our local parts graph.

---

# 8. Supplier normalization is a massive established category

Akeneo essentially confirms the problem verbatim.

Its current product markets an AI Supplier Data Manager that extracts, maps and normalizes product information from arbitrary supplier formats—spreadsheets, documents, etc.—before feeding it into a governed PIM/catalog. It also now markets explicit AI/agentic-commerce syndication. ([Akeneo][31])

Shopify itself says ecommerce catalogs commonly begin as **supplier spreadsheets, model numbers and sparse fields** and specifically lists compatibility information as an important enrichment field. ([Shopify][32])

So don't compete with Akeneo selling enterprise PIM.

Our tiny-business version is much more interesting:

```
SUPPLIER INPUT

PDF
Excel
bad website
WhatsApp
phone
email

        ↓

OUR NORMALIZER

canonical SKU
attributes
compatibility
inventory
price
service capability

        ↓

OUR API
```

This is the exact infrastructure both of our wedges need.

---

# 9. Nordic GeoDrop remains excellent—but broad categories are not enough

### Finland heat pumps is legitimately exceptional

SULPU says Finland had almost **2 million installed heat pumps** by mid-2026. Deliveries in H1 2026 rose **63% year-over-year**, including +71% in air-to-air heat pumps. More importantly for us, SULPU explicitly says replacement demand from the installed base is now a **significant and continuous demand source**. ([SULPU][33])

Its January report says more than **one-third of current air-to-air heat-pump sales are already replacements**; Sweden's corresponding replacement share is about 50%. ([SULPU][34])

That is almost the perfect GeoDrop lifecycle signal.

But generic heat-pump components aren't empty. Norwegian retailers like Quickpart already sell original/universal remotes and explicitly offer human help choosing the compatible model; FixPart has a huge localized parts catalog. ([FixPart][35])

Therefore attack the **broken compatibility edge**, not "heat pump accessories."

Examples:

```
2011 Mitsubishi remote → current replacement
obsolete control board → supersession
Wi-Fi module → model compatibility
sensor → exact unit/revision
old compressor/controller → repair/replace economics
```

That's much better.

### Norway cabins is also structurally real

Norway has **452,150 cabins and other recreational buildings in 2026**. ([SSB][36])

There is substantial installed equipment sitting across those properties:

- pumps;
- 12V/230V water systems;
- heaters;
- gas-water systems;
- solar;
- batteries;
- controllers;
- plumbing fittings.

Existing retailers such as Sparelys, Sunwind, Hyttetorget and others carry large catalogs, but their organization is traditional browse/search ecommerce rather than "photograph the thing installed in your cabin and resolve its exact successor." ([Sparelys][37])

I particularly like cabin equipment because:

> **old equipment + remote location + high inconvenience of ordering wrong part = high value of certainty.**

But we still need SKU-level market scans before choosing the actual subsystem.

---

# 10. Right-to-repair is a huge macro tailwind

This may be underappreciated.

EU Right-to-Repair rules began applying on **July 31, 2026**. Manufacturers must make repair information and spare parts more accessible for covered products, and the European Commission expects the rules to generate about **€4.8 billion in growth and investment**. An EU-wide online repair platform is due in 2027. ([European Commission][38])

Separate ecodesign rules also increasingly mandate years of spare-part availability and public repair information for product categories. ([EUR-Lex][39])

That's fantastic for us.

More structured OEM parts information becomes legally available.

We can normalize it.

---

# 11. Agentic Aftersales is already a business category

**Partful** is another very strong validation.

Its whole proposition is that OEM parts catalogs are broken. It converts CAD+BOM data into interactive parts catalogs so users identify the correct component and purchase from the OEM rather than going elsewhere. ([Partful][40])

Its commissioned OEM research claims:

- only 15% of consumers could find needed parts directly from the manufacturer;
- 52% of professionals have difficulty identifying required parts;
- 67% of parts revenue leaks to third parties.

Those numbers are Partful's own research/marketing, so I wouldn't treat them like government statistics, but the fact that Partful has raised multiple millions to solve exactly this problem is meaningful market validation. ([Partful][40])

Our twist is:

> Partful helps the OEM retain the sale.

We can be the **neutral resolver across OEMs + distributors + marketplaces + technicians**.

That's a different position.

---

# 12. Important warning: marketplaces are going to be brutal competitors

Similarweb's latest data is the strongest challenge to the pure "small agent-native store wins" idea.

Its September 2026 analysis says marketplaces receive around **46.8 million monthly AI referral visits**, up 237% YoY, with the monthly level climbing from 33.2M in June 2025 to 89.9M in May 2026. Amazon/Temu-like marketplaces are disproportionately attractive destinations because of breadth, structured data and transactional trust. ([Similarweb][41])

This is exactly why I now prefer:

> **resolver → route transaction**

over:

> **every answer must buy from our store.**

Sometimes:

```
Our stock → margin £19
```

wins.

Sometimes:

```
Amazon affiliate → £4
```

wins.

Sometimes:

```
supplier direct → £12 referral
```

wins.

Don't fight where Amazon is clearly better.

Own the **decision**.

---

# The strategic conclusion

The research changes the stack from:

```
STORE
 ↓
AI SEO
 ↓
SALE
```

to:

```
             PROBLEM
                │
                ▼
          RESOLUTION GRAPH
                │
       ┌────────┴─────────┐
       ▼                  ▼
    PRODUCT             SERVICE
       │                  │
       ▼                  ▼
 compatibility       qualification
       │                  │
       ▼                  ▼
 SUPPLIER ROUTER       BID ROUTER
       │                  │
       ▼                  ▼
best valid seller   accepted contractor
       │                  │
       └────────┬─────────┘
                ▼
              SOLVED
```

## What I would actually pursue

1. **Agentic Job Broker — Nottingham EV**: build the structured job intake → anonymized broadcast → contractor price/availability response → customer selects → contractor pays lead unlock → details revealed. Test £20/£35/£50 lead-unlock pricing rather than a percentage fee.

2. **GeoDrop Replacement Probe — one Nordic installed-base subsystem**: not generic appliances. Probe Finnish heat-pump remotes/controllers/legacy electronics, Norwegian cabin pump/water-system components, robot-mower lifecycle components and similar extremely specific installed-base categories. Score 500–2,000 candidate SKUs for price dispersion, seller quality, image coverage, compatibility complexity and supersession complexity.

3. **One shared graph underneath both**: `asset`, `part`, `compatibility`, `supplier`, `service`, `location`, `availability`, `price`, `credential`, `outcome`. The front desk continuously fills the service half; the replacement resolver continuously fills the product half.

The biggest validation from this research is that **nearly every individual primitive now has a competitor**: image identification, voice agents, lead marketplaces, supplier normalization, fitment databases, local-service booking, parts procurement.

What I **do not** see as an established winner is the specific combination:

> **consumer problem/photo → exact machine-readable resolution → geographically optimal physical part or verified local human → transaction, with proprietary compatibility and fulfillment data accumulating underneath.**

That is the opportunity I would now concentrate the `drop` architecture around.

[1]: https://www.shopify.com/au/enterprise/blog/ai-search-category-behavior
[2]: https://www.shopify.com/news/entrepreneurs-outselling-mainstream
[3]: https://support.google.com/websearch/answer/16421135
[4]: https://developer.taskrabbit.com/docs/overview-taskrabbit-home-services-api
[5]: https://www.thumbtack.com/guide/content/a-first-look-at-our-new-ai-powered-experience
[6]: https://gerahome.com/
[7]: https://gerahome.com/facts
[8]: https://join.checkatrade.com/pricing/
[9]: https://help.bark.com/hc/en-gb/articles/13346288068892
[10]: https://www.reddit.com/r/DIYUK/comments/1sut02s/
[15]: https://www.probook.ai/platform
[16]: https://www.avocaai.org/
[17]: https://fixpart.co.uk/customer-service
[18]: https://partsnow.ai/news/photo-match-identify-parts-from-picture
[19]: https://www.partium.io/find
[20]: https://docs.partium.io/partium-find/partium-search-engine/how-partium-image-part-search-works/
[21]: https://www.shopify.com/news/spring-26-edition-dev
[22]: https://www.autocare.org/aces
[23]: https://developer.walmart.com/global-marketplace/docs/automotive-fitment
[24]: https://www.partsresolve.com/oem-suppliers
[25]: https://www.uncap.com/post/parts-cross-reference-data
[26]: https://www.reddit.com/r/hvacadvice/comments/1ueg1xz/
[27]: https://www.mrocommand.com/
[28]: https://buyer24.ai/use-cases/mro-industrial
[29]: https://www.getcorivo.com/
[30]: https://sell.andustry.com/
[31]: https://www.akeneo.com/
[32]: https://www.shopify.com/enterprise/blog/product-data-enrichment-ecommerce
[33]: https://www.sulpu.fi/5132-2/
[34]: https://www.sulpu.fi/lampopumppujen-myynti-palasi-kasvu-uralle-kasvua-10-suomeen-myyty-lampopumppuja-jo-10-miljardilla/
[35]: https://fixpart.no/inneklima-reservedeler/pumpe
[36]: https://www.ssb.no/kultur-og-fritid/faktaside/ferie-og-fritid
[37]: https://www.sparelys.no/butikk/vann/ror-og-koplinger
[38]: https://commission.europa.eu/news-and-media/news/right-repair-new-consumer-rights-easy-and-attractive-repairs-2026-07-31_en
[39]: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32023R1670
[40]: https://partful.io/
[41]: https://aisearch.similarweb.com/blog/ai-referral-traffic-by-industry/

---

*Source: User message*
