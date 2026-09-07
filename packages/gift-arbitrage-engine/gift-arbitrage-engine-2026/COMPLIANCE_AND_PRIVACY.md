# Compliance, IP, Privacy and Quality Checklist

This is a commercialization checklist, not legal advice.

## Etsy

Current Etsy rules relevant to this model:

- seller-prompted AI creations are permitted, but AI use must be disclosed;
- original seller designs may be fulfilled by a disclosed production partner;
- buyer-personalized products may be produced by a production partner;
- generic reselling outside Etsy’s allowed categories is not permitted;
- AI prompt bundles are specifically listed as not qualifying as seller-designed items;
- accurate production/shipping-origin information is required.

Sources:
- https://www.etsy.com/legal/creativity/
- https://www.etsy.com/legal/sellers/

## Copyright/IP

Never assume that “personalized” removes IP risk.

Avoid:
- Disney/Marvel/Pokémon/etc. characters without licenses;
- “in the style of” marketed around living artists or recognizable protected franchises;
- copying Monopoly, UNO, Guess Who or other protected game branding/trade dress;
- copyrighted song audio/lyrics in QR gifts without rights;
- using marketplace competitor art as model input/assets.

Build original templates and product systems.

## Customer-uploaded media

Require the buyer to confirm they have permission to use uploaded photos/audio/text.

For group gifts, clearly tell the organizer that contributions will be shared in the final artifact.

## Children

Use minimum necessary data. For a Santa letter or children’s book, avoid requesting sensitive facts. Do not infer behavior, health, school performance, ethnicity, religion or other sensitive traits from photos/data. Parent-provided facts should be optional and reviewable.

## Birth data / astrology

Exact date, time and location can be sensitive personal data. Collect only if necessary, secure it, allow deletion, and avoid retaining it by default unless the user explicitly opts into annual reminders.

Astrology/numerology should be framed as interpretive/entertainment/self-reflection material. Do not present medical, financial or legal outcomes as facts.

## Voice recordings

- private object storage;
- signed/expiring generation links;
- stable but access-controlled playback URLs;
- deletion control;
- no voice cloning unless explicitly requested and appropriate;
- do not fabricate messages from deceased people.

## Hallucination controls

The product must never surprise the buyer with invented memories.

Use:
1. source-grounded structured facts;
2. generated draft;
3. automatic fact/name/date consistency check;
4. customer preview/approval for high-sensitivity products;
5. immutable print manifest.

## Quality gates by product

### Books/newspapers
- spelling and chronology;
- image resolution;
- crop/bleed;
- page count;
- no duplicate photos;
- print proof on at least one representative SKU.

### Recipe products
- buyer confirms transcription;
- do not modify quantities/temperatures without explicit request.

### Crosswords/games
- solver validates every puzzle;
- no duplicate/ambiguous answers;
- safe/appropriate content filter.

### QR products
- QR survives print size/material;
- link is tested after production;
- hosting retention policy is clear.

### Astrology
- actual chart engine/calculation source;
- deterministic data snapshot saved with the order;
- LLM cannot invent planetary positions/aspects.
