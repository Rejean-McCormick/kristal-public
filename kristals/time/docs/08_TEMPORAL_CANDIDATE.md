# Noncanonical temporal candidate — Kristal-Time

**Status:** proposed; domain-owner review required. This is an **additive** extension for `temporal_entity_recurrence_graph`. None of its examples, validations or derived previews amend the domain canon, the preserved v9 commitments, the v11 graph, or the legacy source catalog.

## Scope and boundaries

The existing corpus and canon remain the source of the Kristal's historical content. This candidate adds an explicit tagged vocabulary with JSON Schema and executable rejection cases for:

| Tagged record | Meaning | Forbidden conflation |
| --- | --- | --- |
| `instant` | Offset-qualified civil timestamp mapped to a UTC-oriented Python datetime | Local wall-clock time or calendar day cannot be treated as a unique instant |
| `local_time` | Wall-clock value and an explicit named IANA zone | UTC offset/abbreviation is not an IANA region; fold and gap need a policy |
| `civil_date` | Gregorian date without clock/offset | No implicit instant is inferred |
| `interval` | Two offset-qualified instants, half-open `[start,end)` | Interval is not a duration; end must follow start |
| `fixed_duration` | Nonnegative elapsed seconds | Fixed elapsed time is not a civil period |
| `civil_period` | Gregorian years, canonical months (0–11) and days | A month has no context-free length in seconds |
| `recurrence` | Bounded, calendar-based **preview** | A rule is not an accepted or authoritative occurrence ledger |
| `interval_relation` | Checked Allen-style relationship for two nonempty intervals | Ordering alone does not imply causality |
| `instant_interval_relation` | Checked relationship of an instant with half-open interval | Interval and instant are distinct types; at-end is outside |

### DST resolution

`local_time` without a zone is rejected by the schema. `America/Toronto` is supported **only if runtime IANA data for it are available**. Candidate resolution roundtrips both PEP 495 folds through UTC:

* A nonexistent local wall time (spring DST gap) **fails**; it is never normalized without disclosure.
* An ambiguous time (autumn DST fold) **fails** unless `resolution` selects `earlier` or `later`.
* An unambiguous time resolves without needing a choice. An explicit `resolution` field remains part of the contract.
* Unknown `-00:00` offsets, invalid offsets and leap-second `:60` timestamps fail rather than being silently treated as ordinary instants.

This is Python `datetime`/`zoneinfo` time arithmetic and **not** certified leap-second-correct TAI/UTC/UT1 metrology. The underlying tzdata version actually used by the system `ZoneInfo` loader is **not pinned** by the candidate. The legacy source catalog references IANA tzdb **2026e**, but that reference does **not** establish which tzdb edition runs in an arbitrary deployment. Verify/pin deploy-time tzdata separately for reproducible civil time mapping.

### Recurrence subset (not full RFC 5545)

Only `FREQ=DAILY|WEEKLY|MONTHLY|YEARLY`, `INTERVAL` (optional), and mandatory `COUNT` (1–100) are supported. Every unsupported RRULE component, including `BYDAY`, `BYMONTHDAY`, `RDATE`, `EXDATE`, `UNTIL`, and `TZID` inline extensions, is rejected. Recurrence previews preserve the local clock and use the explicit IANA zone; dates absent in a month or year and local times nonexistent due to DST are **skipped** (not shifted). Ambiguous occurrences fail without `earlier`/`later` policy. Maximum iteration count is bounded. These previews are deliberately narrower than iCalendar's complete rules and are **not an RFC 5545 conformance claim**. No schedule is registered or executed.

### Source and epistemic gates

Documents use `record_role=synthetic_test` or `candidate_proposal`; neither constitutes canonical admission. All records must cite at least one ID already present in `sources/source-catalog.json`; this verifies local **reference existence**, not the substantive truth of the cited statement. `observed` or `sourced_claim` cases must additionally contain `evidence_ref` and `authority_ref`; the validator checks nonemptiness, not the external authority's credentials or the document's contents. `illustrative` test records are explicitly marked synthetic. Wikidata may be used as an externally reviewed identity crosswalk but never as a foundational operational source.

No new KQ/KP or v11 identities are created. The legacy `.kristal/v11/semantic-graph.json` is preserved byte for byte; this repository's workspace does not declare the current Kit's explicit v11 authoring opt-in, so `check-v11` was **not** invoked.

### Sources available in the existing Kristal catalog

- `src:w3c:owl-time-2022` — W3C *Time Ontology in OWL*, Candidate Recommendation Draft, 15 November 2022, <https://www.w3.org/TR/owl-time/>.
- `src:rfc:3339` — IETF RFC 3339, *Date and Time on the Internet: Timestamps*, July 2002, <https://www.rfc-editor.org/info/rfc3339/>.
- `src:rfc:5545` — IETF RFC 5545, *Internet Calendaring and Scheduling Core Object Specification*, September 2009, <https://www.rfc-editor.org/info/rfc5545/>.
- `src:iana:tzdb-2026e` — existing source-catalog reference to IANA tzdb 2026e. General tzdb maintenance description: <https://data.iana.org/time-zones/tz-link.html>. **Do not infer that the runtime uses the catalog's version**.

The W3C/IETF/IANA public URLs were opened for this upgrade. Their source type/version descriptions have been checked where explicitly stated. Access to paid ISO standards and complete scientific verification were **not** performed.

## Run

```bash
# Inside Kristal-Time
python tools/validate_temporal_contract.py examples/SYNTHETIC_temporal_scenarios.json
python -m unittest discover -s tests -p 'test_temporal_contract.py' -v
# From the extracted parent folder, using Kit v4.0.0-draft.3:
python Kristal-Authoring-Kit/tools/kristal.py check Kristal-Time
(cd Kristal-Time && python knowledge-base/tools/validate.py)
```

**Dependencies:** Python 3.10+; `jsonschema>=4` for JSON Schema Draft 2020-12; OS zoneinfo database or Python `tzdata` with the zones used in tests. Dependencies are not included or fetched by this ZIP. These are local validations only; they do not confer canonical admission, independent qualification, certification, synchronization, or publication.

### Historic-byte preservation verification

`standardisation/no-wikidata-v1/original-sha256.json` stores the original 116 file digests from the provided archive. Re-run `python tools/verify_original_integrity.py` to verify that every historical file remains byte-identical. This is a local audit, not a cryptographic signature by an external authority.
