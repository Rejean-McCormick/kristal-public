# 2026-10-27 — C1/C2 signed offline evidence verifier (read-only)

- Added `tools/c123_offline.py` to verify independent externally issued Ed25519 C1/C2 receipts against exact clean Git/C3 bytes, issuer roles, local revocation list, validity windows and exact path scope.
- Added 14 synthetic adversarial signature tests; fixtures never authorize real publication.
- `c3-regression-tests.yml` now installs the verifier dependency and runs all tests (not a release gate).
- Added `docs/C123_SIGNED_GATE.md` and `docs/IMMUTABLE_RELEASE_PLAN.md`; Bootstrap-managed workflows and node configuration remain byte-identical.
- **No real C1/C2 signer, real Zoology reader surface/index, remote immutability attestation, public push or activation.**

# Changelog

## 2026-10-12 — Offline C3 hardening, English documentation

- Added `tools/repository_audit.py`, a **read-only** JSON readiness report covering node/root identity, C3 collection integrity and Bootstrap-managed file drift. Its output never claims C1 or C2 verification.
- Added adversarial structural-validation tests: duplicate JSON keys, duplicate member IDs, member commitment profiles, malformed policy data, unlisted root files, inconsistent snapshot/manifest and AI state references.
- Strengthened `tools/c3_collection.py` error handling and path checks while retaining existing surface, sync-manifest and collection-index formats and their digest conventions.
- Added `.github/workflows/c3-regression-tests.yml` for unit-test fixtures, separated from the existing fail-closed hosted collection checks.
- Rewrote `README.md` and added `docs/STAGING_INTAKE.md`, `docs/FRAMEWORK_PIN_REVIEW.md` and `docs/RELEASE_GATES.md` in English.
- **Not changed:** v9 root and Zoology snapshots and commitments, node ID, GitHub binding, capability declarations, `.kristal/bootstrap-state.json`, and both Bootstrap-managed GitHub workflows.
- **Not performed:** public GitHub write, trust-store change, managed-file adoption, actual Manager sync, C1 qualification, C2 grant, release or activation.

This is a repository-source update, not a semantic-state migration. Actual GitHub HEAD, branch protection, secret configuration and publication readiness require an authorized owner audit.
- Disabled the historical `GitSink.bat` script's unconditional `git add --all` / `git push`. In a public collection, a push is public exposure and cannot proceed without scope-limited authorization. The entrypoint now exits `BLOCKED` without writing anything.
- Excluded the original `SMARTDUMP_INDEX.txt` from the distributed source update because it describes the **old ZIP extraction**, not the updated repository; the input snapshot remains available as the external audit reference.
