# Noncanonical craft procedure candidates (v1)

## Scope

The native `typed_craft_process_graph` and historical v6/v9/v11 source data are **unchanged**. This new authoring layer expresses workshop guidance as a *candidate*: material inputs, tools, gestures, operations, intended product states, prerequisities, risks, quality gates and contextually attributed variants. An instruction record is not a record of an executed process and confers **no authority to execute**.

## Data contract

Each procedure candidate uses `contracts/craft-procedure.schema.json` (JSON Schema Draft 2020-12). Every semantic `urn:craft:*` reference must exist in the historical `knowledge-base/corpus/craft.referent-registry.json` and carry the matching semantic family: material, tool, gesture, operation or object. Local step IDs are **only** candidate process nodes; they are never minted KQ/KP identities.

A step records distinct material, tool, gesture and operation identities; prerequisite steps form an acyclic graph. Each hazard has severity, warning, necessary competence and mitigating controls; a high-severity hazard requires explicit review. All procedure candidates carry `execution_authorization = not_granted`, including any candidate marked documentary-reviewed. A quality check names its criterion and associated numerical tolerance; `planned_unmeasured` is neither acceptance nor failure, and the object outcome remains expected until independently measured and recorded. A defect is not automatically a nonconformity.

## Source and epistemic policy

Use catalogued source IDs but do not treat the six local source cards as independently verified. Each evidence record is either `catalogued_unverified` or `verified`, with verification date, locator, passage and source version required for `verified`. A source citation is not a general operational approval. Synthetic examples require `example_status: synthetic` and must not be presented as historical or normative recipes.

Workshop/tradition variants are distinct contextual alternatives, never a universal procedure. Attribution and its verification status are required. No procedural claims are promoted to canon by validation; provenance and substantive safety still need domain-expert review.

## Validation and next steps

Run the Python domain validator and local Kit check on a working copy. Proposed human decisions: verify each source passage; approve domain-specific workshop terminology and measurement methods; obtain expert safety review for any real application; decide separately whether any versioned native procedural content merits canonical admission. Any future v11 opt-in needs registration, reviewed identities and Framework/Integration qualification, not merely existing `.kristal/v11/` files.
