# User Message — Building Hardware Opportunities + 10 Gold Campaigns

*Sent: 2026-09-07*
*Status: SAVED WORD-FOR-WORD*

---

Yes. After filtering for **actual launchability**, not just attractive macro data, these are the subgraphs I would investigate first.

The best new opportunity is not heat pumps. It is **old Scandinavian building hardware**.

## 1. Norway: old balcony/terrace-door mechanisms

This is extremely close to the ideal GeoDrop object.

Norway has 2.76 million dwellings, including 1.31 million detached houses. ([SSB][1]) A Norwegian locksmith currently advertises exactly the pain we want: old/out-of-production terrace-door locks and mechanisms from **GU, ASSA, TrioVing, Grorud, Fix**, including hardware from the 1970s–2000s, and essentially says "contact us, maybe we have the weird thing you need." ([SystemLaaS][2])

An actual old GU lock used in Uldal balcony doors from **1993–2004** sells for NOK 1,246 ex VAT. ([Ellefsen Sikkerhet][3]) Another old Norwegian door-handle design was historically selling **300k–360k pairs per year** and replacement reproductions now sell around NOK 1,125. ([moloas.com][4])

This is the query:

> "This mechanism in my 1998 balcony door broke. What replaces it?"

Perfect.

The graph:

```
DOOR MANUFACTURER
  Uldal / NorDan / Gilje / Strømmen / etc.
          ↓
YEAR / GENERATION
          ↓
LOCK FAMILY
 GU / ASSA / FIX / Grorud
          ↓
MEASUREMENTS
 backset
 centres
 strip length
 spindle
 handing
          ↓
ORIGINAL PART
          ↓
CURRENT REPLACEMENT
```

Customer supplies **photo + 3 measurements**.

We resolve the product.

### Why I like it

Current commerce is fragmented between:

- window manufacturers;
- locksmiths;
- hardware wholesalers;
- legacy-hardware shops;
- PDFs/order forms.

ASSA ABLOY says it is the Scandinavian market leader for espagnolette/window hardware, but its site is predominantly an **OEM information surface**, not a magical consumer resolver. ([ASSA ABLOY][5])

NorDan has some direct spare parts, but even its catalog is date/generation-specific—for example hinges suitable for windows produced after week 26 of 2012. ([NorDan Norge][6])

That is exactly the structured graph we can normalize.

**Score: 9.4/10.**

This may be better than cabins.

---

# 2. Norway: Wallas legacy cabin-heater parts

This one is highly concrete.

Depending on SSB methodology, Norway has around **452k–484k recreational buildings**, with roughly 48% geographically scattered rather than in dense cabin developments. ([SSB][7])

Wallas has decades of heater generations installed in cabins and boats.

One control panel, **361062**, fits:

```
22Dt
22GB
26CC
26CC Winter
30Dt
30GB
40CC
40CC Winter
40Dt
```

([Wallas][8])

Other lovely SKUs include:

| Part | Compatibility | Norway retail |
| --- | --- | ---: |
| Wallas control panel | multiple 22/26/30/40 models | ~NOK 2,999 |
| FC2 pump | M2600/M4000/M26/M40/26CC/40CC | NOK 2,999 |
| Glow-plug kit | huge legacy model range | NOK 979 |
| Tank connector | M26/M40/M2600/M4000/26CC/40CC | NOK 795 |
| Control cable | multiple generations | NOK 799 |

([Sunwind][9])

And Sunwind explicitly has **dealer-only spare parts** and openly accepts dealer applications. ([Sunwind][10])

That's unusually actionable.

### Store concept

Not:

> hytte reservedeler.

Instead:

> **Wallas replacement resolver for Norwegian cabins.**

User uploads:

```
photo of heater
photo of panel
photo of model plate
```

We return:

```
You have Wallas 26CC.

Your old controller:
361061

Current compatible control:
361062

Also compatible with:
...

NOK X
Ships tomorrow.
```

### Weakness

Wallas itself has a pretty good parts database and Sunwind sells many products directly. ([Wallas][11])

So we only win if dealer economics are good and we make **identification materially easier**.

**Score: 9.1/10.**

---

# 3. Finland/Norway: old hot-tub control panels

This was the surprise winner.

It fits your model beautifully:

> consumer has an expensive physical asset, one little controller dies, replacement identity is confusing, but the component itself is often plug-and-play.

Finnish sellers currently sell:

- Balboa VL260 ~€199
- TP800 ~€349
- Gecko IN.K500 ~€425
- Gecko IN.K800 ~€545
- IN.K1001 ~€690

and explicitly warn that the control panel must match the underlying control system. ([AuraSpa][12])

Norwegian panels commonly run **NOK 2,000–8,800**, while controller boxes/PCBs can reach NOK 5k–15k. ([Viskan Spa -][13])

Here's why it's particularly interesting:

The consumer-facing hot-tub brand often isn't the component manufacturer.

```
HOT TUB BRAND
Vikingbad / Nordic / Sundance / random dead manufacturer
       ↓
INTERNAL CONTROL SYSTEM
Balboa / Gecko / Spanet
       ↓
CONTROL BOX
       ↓
COMPATIBLE TOPSIDE PANELS
```

So a customer says:

> "My 2013 Vikingbad screen died."

The actual purchasing problem is:

> determine underlying Balboa controller → determine compatible topside → possibly current superseding panel.

### Evidence of real pain

Recent hot-tub owners repeatedly describe obsolete control panels, unknown manufacturers and the difficulty of figuring out which modern system is compatible. ([Reddit][14])

Swedish retailers show the weirdness explicitly: some Nordic panels only fit given **serial-number ranges** and some are dealer-only despite being in stock. ([Folkpool][15])

That is a gorgeous agentic graph.

### Launch subset

Only customer-safe topside components initially:

```
Balboa VL-series
Balboa TP-series
Gecko IN.K-series
selected Nordic/Folkpool mappings
```

Don't sell mains-voltage control packs as DIY unless appropriate.

**Score: 9.0/10.**

---

# 4. Nordic marine: legacy electronics retrofit adapters

This is another real one.

The Nordics contain **millions of recreational boats**. More importantly, marine electronics generations change connectors and networking standards while expensive installed transducers/sensors remain useful.

Garmin itself documents the transition:

```
legacy 6-pin
 → 4-pin
 → 8-pin
 → 12-pin
```

and explicitly tells owners they can sometimes reuse old transducers using adapters. ([Garmin Support][16])

A simple 6→8-pin adapter currently costs around €75. ([Garmin][17])

More sophisticated analogue→NMEA 2000 adapters sell for around **NOK 2,569**. ([Marine Shop][18])

The query is fantastic:

> "I have this old Garmin transducer. I bought this new chartplotter. What cable do I need?"

Or:

> "Can I connect this old Raymarine sensor into my NMEA 2000 network?"

### Graph

```
OLD DEVICE
 ↓
port / protocol / generation
 ↓
NEW DEVICE
 ↓
direct compatible?
 ├─ yes
 └─ no
     ↓
adapter chain
     ↓
correct SKU
```

This is potentially **cross-brand**, which makes the knowledge graph valuable beyond any one merchant.

### Weakness

Specialist marine retailers are technically competent.

So I'd start this as:

> **migration resolver + affiliate/direct-sale router**

before forcing a full dropship operation.

**Score: 8.8/10.**

---

# 5. Scandinavia: old window/balcony-door hardware more broadly

I separate this from opportunity #1 because there is potentially a much larger second-stage graph.

Sweden alone has nearly **5.3 million dwellings**, 41% in one/two-dwelling buildings. ([Statistikmyndigheten SCB][19]) Finland has over one million households in one- or two-dwelling houses. ([PX Data][20])

Hardware categories include:

```
espagnolette mechanisms
window brakes
hinges
handles
gearboxes
locking strips
keeps
sliding-door locks
balcony-door brakes
```

A current Swedish homeowner asking how to find an old Habo espagnolette was told it effectively needs to be ordered through an ASSA reseller via an order form. ([Byggahus.se][21])

That's archaic enough to be interesting.

### Killer interface

```
1. Photograph whole door/window.
2. Photograph mechanism.
3. Photograph stamped markings.
4. Measure A / B / C.
5. AI resolves hardware family.
6. Show verified replacement.
```

There is contemporary industry guidance saying identification often comes down to photos, marks, dimensions and mounting geometry. ([Window Hardware Direct][22])

This is almost tailor-made for multimodal models.

**Score: 8.8/10.**

Main unknown: wholesale/dropship access and margins.

---

# 6. Nordic powered-recliner controls

This is the weird little wildcard.

Current Norwegian/Finnish/Swedish results are overwhelmingly generic marketplace listings for **OKIN/Limoss** 2-button/4-button/5-pin controls.

Examples are roughly:

- NOK 139–329;
- €29–45;
- SEK 160–450.

([Shopit.se][23])

The products are used by many furniture brands because the underlying motors come from common suppliers such as Okin/Limoss. Specialist US stores already exist specifically around Okin replacement power supplies, which validates the subgraph. ([Okin Power Supply][24])

But Nordic search results are largely:

> generic Chinese seller + vague "5 pin" compatibility + 1–3 week delivery.

That is exactly the type of digital supply weakness we wanted.

### Customer journey

```
photo under chair
       ↓
motor manufacturer
OKIN / Limoss
       ↓
connector
5-pin / 2-pin etc.
       ↓
function count
2 / 4 / 6 button
       ↓
compatible handset
```

Extremely easy to photograph.

Extremely easy to ship.

No technician.

### Weakness

AOV is low and I don't have a reliable Nordic installed-base statistic.

Therefore this is an **excellent £100 experiment**, not something I'd build a thesis around yet.

**Score: 8.2/10.**

---

# What I would now reject

This research has killed quite a few seductive ideas.

**Generic Mitsubishi remotes:** real demand, but Finnish merchants already have good generation/model guidance.

**Generic garage remotes:** Norwegian specialists already have old-remote image selectors and replacement systems. ([portspesialisten.com][25])

**Thetford toilets:** incredibly nice lifecycle graph—models from 1987–2006 with parts explicitly split at dates such as June 15, 2000—but Nordic retailers already have excellent SKU coverage. ([Thetford][26])

**Dometic Heki rooflight parts:** similarly good lifecycle mechanics but Swedish/Norwegian sellers have dozens of indexed exact-model parts. ([campingvaruhuset.se][27])

**Robot mower components:** Husqvarna already provides strong exact-model compatibility. ([Husqvarna][28])

Those are excellent **benchmarks for our resolver**, not great first markets.

---

# My actual top three now

If the goal is **something you can plausibly own**, I would run these three Snowball probes all the way to supplier economics:

### A — `old Norwegian balcony-door hardware`

Initial graph:

```
GU
ASSA/FIX
Grorud
NorDan
Uldal
Strømmen

1970–2010
```

Find the ~100 common legacy mechanisms/components.

This has massive structural installed-base logic and relatively primitive discovery.

### B — `Norwegian Wallas cabin heater lifecycle`

Initial graph:

```
M2600
M4000
M26
M40
26CC
40CC
22Dt
30Dt
40Dt
22GB
30GB
```

Then only 50–100 high-value, consumer-addressable components.

We already have an explicit potential dealer path via Sunwind. ([Sunwind][29])

### C — `Nordic hot-tub control resolver`

Initial graph:

```
consumer spa brand
        ↓
year / serial
        ↓
Balboa / Gecko system
        ↓
compatible control panel
        ↓
current replacement
```

This might be the **purest Agentic Shopify experiment**, because the photos are distinctive, parts cost hundreds, compatibility is difficult, and the actual component is frequently user-swappable.

---

# Which one I'd launch first

I would currently pick **Norwegian old balcony-door/window mechanisms** for the next deep probe.

Not because we know it makes the most money—we do not yet.

Because it has the strongest combination of:

```
enormous installed base
+
decades of legacy generations
+
consumer-visible failure
+
photo/measurement identification
+
no regulated diagnosis
+
small shippable product
+
£50–£150+ replacement value
+
fragmented specialist supply
+
absurdly poor consumer discovery
+
Norwegian-language moat
```

And the search evidence contains the sentence we keep trying to find economically:

> **"We stock old/discontinued/unusual locks… maybe we have exactly what you need."** ([SystemLaaS][2])

That is a supplier practically advertising:

> **"Our inventory needs an AI frontend."**

The next step isn't another broad market report. It is to take **Norwegian balcony-door hardware**, enumerate the 50–100 common legacy products/generations, find every current seller and actual buy price, identify which wholesalers can supply us, and test the native Norwegian query/photo flow through Google and ChatGPT. That will tell us whether we have an actual first Agentic GeoDrop store rather than another attractive thesis.

[1]: https://www.ssb.no/en/bygg-bolig-og-eiendom/bolig-og-boforhold/statistikk/boliger
[2]: https://www.systemlaas.no/terrassedorer/
[3]: https://www.ellefsensikkerhet.no/detaljer/107330/MPL322%EA%9C%9935_Esp%E1%B6%A7_L%C3%A5skasse%E1%B6%A7_GU_gammel
[4]: https://www.moloas.com/Produkter/Dorvridere/Moderne_dorvridere_1950-1970/1738_Dorvrider_1960_talls_krom
[5]: https://www.assaabloy.com/se/sv/solutions/products/beslag-till-fonsterindustrin/spanjolettsystem
[6]: https://www.nordan.no/produktkategori/shop/vindusbeslag/hengsler-til-vindu/
[7]: https://www.ssb.no/bygg-bolig-og-eiendom/faktaside/hytter-og-ferieboliger
[8]: https://wallas.fi/partsearch/tuote.php?k=&t=361062
[9]: https://www.sunwind.no/alle-produkter/reservedeler/reservedeler-varme/kontrollpanel-kabel-%2826-40cc%29
[10]: https://www.sunwind.no/alle-produkter/reservedeler/reservedeler-vann
[11]: https://www.wallas.fi/kauppa/index.php?action=unit&l=67
[12]: https://auraspa.fi/ulkoporealtaan-varaosat/ohjauspaneelit
[13]: https://www.viskanspa.no/spabad/kategori/reservdelar/kontrollpaneler/
[14]: https://www.reddit.com/r/hottub/comments/1uuu819/replacing_a_control_pack/
[15]: https://www.folkpool.se/produkter/spa/reservdelar/kontroller/kontroller-nordic-hot-tub/kontrollpanel-gecko-2pump-nordic-aldre.html
[16]: https://support.garmin.com/en-AU/?faq=FYzNJ06VUF11E3PL2oto99
[17]: https://www.garmin.com/el-GR/p/85643/pn/010-11613-00/
[18]: https://www.marineshop.no/garmin/102823/2839-garmin-gra-10-rorvinkel-adapter
[19]: https://www.scb.se/en/finding-statistics/statistics-by-subject-area/housing-construction-and-building/housing-and-accommodation/dwelling-stock/
[20]: https://pxdata.stat.fi/PxWeb/pxweb/en/StatFin/StatFin__asku/15fh.px/table/tableViewLayout1/
[21]: https://www.byggahus.se/forum/threads/hur-ska-jag-hitta-ratt-spanjolett.563803/
[22]: https://windowhardwaredirect.com/blogs/news/how-to-identify-window-hardware-without-a-brand-name
[23]: https://shopit.se/rekliner-massagefatoljfjarrkontroller/5-stifts-4-knapps-fjarrkontroll-for-eldriven-recliner-ersattning-p109387824051083
[24]: https://okinpowersupply.com/
[25]: https://www.portspesialisten.com/merker/hormann
[26]: https://www.thetford.com/int/thetford-service-and-support/c2-c3-c4-series/
[27]: https://www.campingvaruhuset.se/sv/husvagn-husbil/kaross/takluckor/reservdelar
[28]: https://www.husqvarna.com/uk/maintenance-and-spare-parts/power-supply-unit/
[29]: https://www.sunwind.no/ofte-stilte-sporsmal/generelt/%C3%B8nsker-%C3%A5-bli-forhandler-hvordan-g%C3%A5r-jeg-frem

ok this is more on the rihgt lines.. create 10 gold campaigns more aligned with this thesis your otehr ones likely need someone to install them

---

*Source: User message*
