# Kristal-Catho · Semantic Links (2026-10-15)

## Scope and status

This release adds **two canonically registered Logical Artifacts** to the four already present, without changing the contents of the original four domain payloads or the 145-entry source catalogue:

- `canon/domain/catho-semantic-links.json` — explicit, typed cross-artifact relationships and original Wikidata statement pointers;
- `canon/domain/catho-topics.json` — original historic corpus topics and separately attributed Wikidata P921 subjects, with no automatic equivalence.

One `kristal.state/9.0` State Snapshot commits six Logical Artifacts. The self-contained visual graph in `derived/catho-graph/` is **not canonical** and can be regenerated.

**Important:** a canonical artifact may record an *attributed external claim* or an *open hypothesis*. Its admission as a record does not endorse the factual truth of the claim. Attribution, identity resolution, authority, certainty and admission are separate.

## Facts bound to the provided snapshots

| Material | Count | Interpretation |
| --- | ---: | --- |
| Full Wikidata items | 1,692 | Previously imported, no re-query |
| Wikidata statements with imported QID endpoints | 2,495 | 2,493 distinct source/property/target triples; source GUIDs remain available |
| Author–work relationships in campaign | 1,455 | **All traced** to source `P50` statement GUID(s) in the imported full item records |
| Historic author ↔ Catho person explicit roster refs | 21 | Explicit links in preexisting canonical person registry, **not** new independent identity proof |
| Unconfirmed Skope research claims | 339 | Research-only edges, never identity confirmation; 24 candidate QIDs and 24 source URLs remain unverified |
| Historic corpus assertions | 1,076 | Original content unchanged, source/evidence/qualifiers read in derived graph |
| Distinct historic themes | 99 | Original `corpus:theme` qualifiers |
| Distinct Wikidata P921 subject QIDs | 280 | From 772 Wikidata claims; 273 subject items not present as full records in this selected snapshot |
| Institutional attribution records | 750 | Read as recorded in original Catho roster; not theological endorsement |
| Historical source records linked by corpus | 138 | Existing historical source IDs and evidence pointers |
| Identity dossiers open | 161 | None automatically confirmed; 21 proposals remain proposals |
| Historical author referents without roster link | 36 | May represent persons, institutions or documents: **not** automatically matched |
| Derived reader graph | 4,520 nodes / 8,691 edges | Includes assertions, sources, works, persons, topics and authored source links |

## Files and roles

- `canon/domain/wikidata-import.json`: immutable attributed external source snapshot. Retains qualifiers, rank, references, IDs, and the source dump identity.
- `canon/domain/wikidata-alignments.json`: pre-existing campaign results and non-accepted AI research.
- `canon/domain/catho-semantic-links.json`: **canonical pointers** to the existing statements (not duplicates), explicit roster references, institutional attributions, historical source support.
- `canon/domain/catho-topics.json`: independent topic namespaces; the absence of a QID's full record is *partial coverage*, not negation.
- `derived/catho-graph/edges.json`, `nodes.json`, `by-*.json`: loss-aware, rebuildable read indexes.
- `derived/catho-graph/research-queue.json`: explicitly unresolved identities, historic authors and P921 subject records to acquire.
- `derived/catho-graph/explorer.html`: offline, self-contained English reader; open in a browser without a server. Its visible nodes and edges do not turn source assertions into domain facts.
- `tools/build_catho_semantic_links.py`: deterministic `build` (explicit canonical change), `project` (read-model only), and `check` (read-only).

## Local validation

Run from PowerShell 7, in the **Kristal-Catho** directory:

```powershell
$py = 'C:\Users\rejea\AppData\Local\Programs\Python\Python312\python.exe'
& $py tools\build_catho_semantic_links.py . check
& $py tools\validate_catho_wikidata.py .
& $py -m unittest discover -s tests -p test_catho_semantic_links.py -v
& $py tools\kristal.py check .
```

Rebuild the view only (no semantic state mutation):

```powershell
& $py tools\build_catho_semantic_links.py . project
```

To build a new state after future **intentional** canonical changes:

```powershell
& $py tools\build_catho_semantic_links.py . build
& $py tools\kristal.py build-v9 .
& $py tools\kristal.py check .
```

`build-v9` does not publish or activate. `check` establishes technical consistency, not independent theological truth or identity verification. Do not mistake Wikidata preferred rank, editorial subject similarity or an AI score for high certainty.

## Next data acquisition boundaries

The research queue makes the next targeted harvest practical: 273 referenced P921 topics outside the bounded snapshot, 36 historic source-author referents with no explicit Catho roster link, and 161 unresolved identities. These are **three distinct shortfalls**, not 470 asserted missing people or facts. New evidence and user-approved identity decisions should be recorded separately, then recompiled through the authoring workflow.

## Skope and readers

Skope and EncyKlopedia are unchanged. Selecting this Kristal in Skope does not guarantee its current UI consumes `derived/catho-graph/` or new v9 logical artifacts. The standalone explorer is usable independently. A future generic reader adapter may consume the JSON indexes using explicit provenance/coverage checks, without modifying Catho canon.
