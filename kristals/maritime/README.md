# Kristal-Maritime

Kristal-Maritime 1.0.0 is a static, source-backed Kristal v6 corpus centered on:

**vessel × marine environment × navigation × cargo/operation**

The multiplication sign denotes interaction, not a universal numeric product. The graph is intentionally sparse: a relation is included only when it is meaningful for the maritime model.

The corpus represents vessel types and characteristics, the marine environment, navigation information and systems, cargo classes, operations, safety concepts and their interfaces. IMO, IHO, IALA and NOAA references are used as provenance anchors; the package is not a live navigation service or an exhaustive legal corpus.

Canonical state: `knowledge-base/corpus/maritime.kristal-state.json`

Run `python knowledge-base/tools/validate.py` from the package root to validate schema, references, hashes, evidence coverage and manifest integrity.
