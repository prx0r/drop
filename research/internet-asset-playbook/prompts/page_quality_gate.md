# Prompt: page quality gate

Review this candidate page before publication.

Fail the page if any condition is true:

1. It is mostly generic prose an LLM can answer without visiting the site.
2. It has no unique data, tool, calculation, current availability, verification, or decision function.
3. Any factual claim lacks a source or provenance record.
4. A price, capability, rating, certification, or location is inferred rather than verified.
5. The page differs from another page only by a keyword/location substitution.
6. Sponsored or affiliate relationships are not disclosed.
7. The title promises a ranking (“best”, “top”) without an explicit scoring method.
8. Source data is stale and the page fails to show its last-verified date.
9. The page exists primarily because a keyword tool showed volume.
10. A reasonable user would gain no value if they arrived directly rather than via search.

If the page passes, return:

- unique user value;
- evidence fields used;
- freshness date;
- intended action/conversion;
- what would make the page materially better.
