# Build Notes — 2026-09-07

*Session: Voiceagent integration + infrastructure planning*

---

## What We Discovered

### voiceagent is the runtime, not a separate project

The voiceagent repo already has:
- Graph-grounded chat
- Business YAML configuration
- Voice adapter (edge TTS)
- API endpoints (/chat, /graph/search, /health)
- Norwegian language handling
- Product nodes with compatibility info
- Policy nodes, service nodes, FAQ nodes
- Escalation rules
- Tool registry
- Session management

**The voiceagent IS the Drop Resolver Runtime.**

Voice is one channel. Web chat is another. Product finder is another. Shopify PDP is another. Google is another. ChatGPT/Shopify Catalog is another.

### The graph needs expansion

Current implementation: lexical token matching + neighbor expansion.

Missing:
- Typed entities (OEM, ASSET, MODEL, GENERATION, COMPONENT, PART, SKU, SUPPLIER)
- Typed edges (FITS, DOES_NOT_FIT, SUPERSEDES, REPLACED_BY, REQUIRES_PART, REQUIRES_ADAPTER)
- Evidence binding (every edge needs source URL + verification status)
- Photo similarity → candidate retrieval only (not compatibility assertion)

### The architecture is becoming clear

```
               DROP GRAPH
                   │
        ┌──────────┼────────────┐
        ↓          ↓            ↓
      HUMAN      GOOGLE       SHOPIFY
      PDP        AI MODE      CATALOG/UCP
        │          │            │
        └──────────┼────────────┘
                   ↓
              CUSTOMER AGENT
                   ↑
                   │
             VOICEAGENT
```

### Shopify alignment

- Shopify Catalog auto-syndicates to agentic storefronts
- Storefront MCP available at /api/ucp/mcp
- /agents.md auto-generated
- Knowledge Base app for FAQs
- Google Merchant Center supplemental data for compatibility

### The compiler is the main product

```
drop compile NO-BALCONY-HARDWARE-001
```

should emit:

```
dist/
├── graph.json
├── voiceagent.yaml
├── shopify-products.jsonl
├── shopify-metafields.jsonl
├── google-primary-supplement.jsonl
├── google-conversational.jsonl
├── schemaorg.jsonl
├── resolver-cases.json
└── build-manifest.json
```

One input. Every representation synchronized.

---

## Next Steps

1. Demote 25 current ACTIVE campaigns to truthful states
2. Restore Allaway + AKVA/BioCycle into canonical campaign registry
3. Define subgraph.schema.v1
4. Turn balcony-door YAML into first evidence-backed real subgraph
5. Modify voiceagent to load compiled Drop graphs
6. Build Shopify Admin/metafield compiler
7. Stand up one Shopify test store
8. Enable Shopify Catalog + Google & YouTube
9. Add Merchant Center supplemental conversational data
10. Test live Shopify /api/ucp/mcp endpoint against 50 compatibility questions
