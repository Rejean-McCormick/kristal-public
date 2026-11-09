# Kristal-Veterinary

Kristal-Veterinary 1.0.0 is a static, source-backed Kristal v6 corpus centered on:

**species × physiological system × pathology × intervention**

The matrix is intentionally sparse rather than Cartesian: a relation is encoded only where clinically or biologically meaningful. The corpus is comparative and cross-species, spanning companion animals, equids, livestock, poultry, selected exotic animals, aquatic animals and wildlife.

Interventions are represented as domains of care, not as prescriptions. No dosing tables or autonomous treatment protocols are included.

Canonical state: `knowledge-base/corpus/veterinary.kristal-state.json`

Run `python knowledge-base/tools/validate.py` from the package root to validate schema, references, hashes, evidence coverage and manifest integrity.
