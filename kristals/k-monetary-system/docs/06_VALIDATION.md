# 06 — Validation

Workspace validation uses `python tools/kristal.py check .` and v9 build commitments.

Domain validation additionally requires:

1. All statechart transition targets exist.
2. Ordinary settlement preserves K_M accounting conservation.
3. K_M and K_C remain semantically distinct.
4. Founder override remains false in the constitutional contract.
5. Smart Vote is referenced as external rather than duplicated.
6. Every debt-reduction channel identifies a creditor-side/accounting counterpart.
7. Model outputs remain explicitly non-authoritative.
8. Failure states and counterarguments remain representable.

Empirical validation is currently incomplete and is separately tracked in the epistemic validation state.
