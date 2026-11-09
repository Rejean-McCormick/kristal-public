# Import Skope/Wikidata — Kristal-Governance

Cette copie inclut le résultat du run `6e7fb0ae5434f629` dans `sources/wikidata-skope/runs/6e7fb0ae5434f629/`.

- **Sources intégrées** : entités Wikidata complètes dans `raw/full-evidence/`, propositions complètes dans `raw/enrichment-proposals.jsonl`, rapports, sélection QID et résolution d'identité d'origine.
- **Index de travail** : `crosswalk-candidates.jsonl` et `priority-relations.jsonl` (propositions **non validées** et **non publiables**).
- **État** : merge **au niveau des preuves externes**, sans promotion des assertions en KAs, ni génération de KS, ni acceptation d'identité KQ↔QID ou KP↔PID.
- **Protection** : `canon/`, `.kristal/`, le catalogue `sources/source-catalog.json` et les commitments v9 restent inchangés.

La source est Wikidata, via Skope, avec les paramètres et la provenance figurant dans `raw/run-report.json` et `raw/source-profiles/maxwd-local.json`.
Les statuts `lexical_only_unverified` et `publication_authorized=false` restent applicables, même si les fichiers ont été fusionnés dans le paquet Kristal.

## Lecture rapide

1. `source-index.json` : synthèse et chemins intégrés.
2. `crosswalk-candidates.jsonl` : identités candidates de lecture (ne pas copier dans `.kristal/v11/external-crosswalk.json`).
3. `priority-relations.jsonl` : P31/P279/P361/P527, à convertir en KA seulement après mapping sémantique fiable.
4. `raw/full-evidence/` et `raw/enrichment-proposals.jsonl` : matériaux bruts, avec références et rangs Wikidata.

## Pour une intégration canonique ultérieure

Une opération distincte doit réconcilier les identités KQ/QID, définir la sémantique de KP/PID et faire accepter les assertions via diK/Authoring Kit. Les fichiers du présent import ne sont ni un crosswalk accepté ni un canon v11.
