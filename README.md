# kristal-public

**Kristal v10 GitHub collection host — public, read-only structural controls, publication sealed.**

This repository holds node metadata, state snapshots, and *eligible* derived read surfaces for explicitly approved Kristals. It is **not** the semantic owner of the hosted states, not the Authoring Kit, not a fact-validation service, and not an automatic publication authority.

> **Current supplied snapshot status (2026-11-09): `BLOCKED` for hosted collection qualification.**
> `kristals/index.json` **is present** in the supplied ZIP, but `tools/c3_collection.py --repo . validate-index` fails because the Aerospace read-surface manifest refers to `canon/domain/v11/updates/wikidata-2026-10-27-v11-1/normalized-KA-KS-candidates.jsonl.gz`, which is absent. The offline audit also detects Bootstrap-managed file-hash drift. C1 independent qualification and C2 public authorization remain `NOT_VERIFIED`. Do not create a substitute file or index to force C3 PASS. The root genesis state is not Zoology.

## Quick local checks

Python 3.10+; no network, token, credential, or third-party dependency required for these commands:

```bash
python -m unittest discover -s tests -v
python tools/repository_audit.py --repo .
python tools/repository_audit.py --repo . --strict
python tools/c3_collection.py --repo . scan
```

`repository_audit.py` prints a machine-readable, read-only local report: observed node/root identities, discovered slugs, collection integrity, C1/C2 verification status, and managed-file SHA drift. Without `--strict` it returns 0 to allow inspection even of an incomplete repository; with `--strict` it exits nonzero for integrity failures or detected Bootstrap drift.

`validate-index` is **blocked on the supplied snapshot** due to unresolved referenced bytes, even though the index exists. A green regression-test job does **not** mean the collection is publishable.

## C1/C2 signed evidence preflight (new — still sealed)

A separate offline tool, `tools/c123_offline.py`, can now verify **real Ed25519 signatures** for externally issued C1 qualification and C2 approval receipts against an independently protected trust policy **outside this repository**, while requiring a clean exact Git commit and a structurally valid C3 collection. It checks exact digest/scope binding, expiration, revocation lists and independent signing keys. **It never authorizes a public write or creates a release**; proof of issuer legitimacy, fresh revocation state, genuine approvals and immutable remote release remain external obligations.

See [Signed C1/C2 Gate](docs/C123_SIGNED_GATE.md) and [Immutable Release Plan](docs/IMMUTABLE_RELEASE_PLAN.md). The collection remains **BLOCKED** pending complete C3 evidence, resolution of the missing Aerospace bytes and separate owner C1/C2 approvals. The local signed-gate tests do not grant those approvals. Unit tests use ephemeral synthetic signers and do not constitute real approval.

## Repository map

| Path | Purpose |
| --- | --- |
| `.kristal/node.json` | v10 collection node identity and roles |
| `.kristal/bindings/github.json` | Replaceable host locator and declared GitHub visibility |
| `.kristal/capabilities.json` | Declared compatibility and capabilities; not independent proof |
| `.kristal/bootstrap-state.json` | Historical Bootstrap-managed file fingerprints; **do not rewrite automatically** |
| `state/state-snapshot.json` | Collection root/genesis state, with no members |
| `kristals/zoology/state/state-snapshot.json` | Independently identified Zoology v9 snapshot |
| `kristals/<slug>/.kristal/sync-manifest.json` | Manager-generated exact read-surface manifest, when genuinely available |
| `kristals/index.json` | Derived collection discovery index, **present but collection-wide C3 validation BLOCKED** |
| `tools/c3_collection.py` | Local C3 structural index/surface validator and optional candidate index generator |
| `tools/repository_audit.py` | Local status, identity and Bootstrap-drift diagnostics; never authorizes publication |
| `tools/c123_offline.py` | Detached external C1/C2 Ed25519 receipt verification (read-only, no publication permission) |
| `requirements-security.txt` | Optional cryptographic verifier dependency for locally executed C1/C2 checks |
| `.github/workflows/kristal-qualify.yml` | Bootstrap-managed C3 integrity check; fails closed on incomplete collection |
| `.github/workflows/kristal-publish.yml` | Bootstrap-managed **sealed**, read-only candidate check; always blocks publication |
| `.github/workflows/c3-regression-tests.yml` | Independent, read-only Python regression suite for C3 tooling |

## Controlled future ingestion (not performed here)

A **legitimate repaired surface** must originate from an authorized domain workspace and the actual Kit/Manager owners, with identity, provenance, file list, bytes, readiness and digest verified. In an isolated staging copy, reconcile missing/extra member paths and rebuild the exact read-surface and collection index under the applicable owner contract. Only then may `python tools/c3_collection.py --repo . validate-index` return a **structural** PASS. Never fabricate missing source bytes or quietly rewrite a manifest to fit an incomplete snapshot.

Even a structural PASS does **not** establish independent C1 qualification, authorized C2 public exposure, a verified immutable publication, or activation. A push to a **public** repository already exposes bytes — authorization must precede any public synchronization, PR, upload, or release.

For the detailed sequence, see [Staging Intake](docs/STAGING_INTAKE.md), [C3 Handoff](docs/C3_HANDOFF.md), [Framework Pin Review](docs/FRAMEWORK_PIN_REVIEW.md), and [Release Gate Checklist](docs/RELEASE_GATES.md).

## Boundaries

- Preserve canonical v9 identity and Logical/State Commitments; Git SHA and read-surface digest do not replace them.
- Keep node identity separate from hosted member states. The memberless root genesis **must not** be substituted for Zoology.
- Manager owns read-surface synchronization/index generation; Bootstrap owns node configuration and managed workflow reconciliation; C1 qualifies independently; C2 grants exact authorization; C3 checks hosting integrity.
- Konstellation and Konstellation Light consume approved, policy-checked reader projections; they do not confer knowledge authority.
- The repository's two existing managed GitHub workflows remain deliberately sealed/read-only until owners jointly approve a trusted C1/C2/C3 gate. Changing tracked workflow files would require Bootstrap reconciliation.

**No public publication, activation, remote push, or semantic-state migration was performed in this offline update.**

> **Final-system Branch 03 alignment (2026-11-09):** See [the release/distribution/exploration integration note](docs/FINAL_SYSTEM_BRANCH03.md). The seven-owner pipeline is a target with independently gated qualification, permission, packaging and readers. This source snapshot does not authorize public publication or deployment.
