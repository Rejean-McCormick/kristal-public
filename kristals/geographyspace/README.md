# Kristal GeographySpace 1.0.0

Kristal GeographySpace est un corpus statique de **sémantique spatiale géographique**. Il répond aux questions structurantes : *où ? dans quoi ? à quelle échelle ? par rapport à quoi ? séparé par quoi ? distribué comment ? circulant entre quoi ?*

## Périmètre

Sept axes canoniques : **localisation, territoire, échelle, voisinage, frontière, distribution, flux**.

Ce Kristal ne cherche pas à devenir un atlas, une base de pays, un moteur SIG ni un corpus de géopolitique. Il fournit la grammaire spatiale que ces domaines pourront réutiliser.

## État

- Kristal Standard **v6** (`kristal_state`)
- corpus **1.0.0**
- 154 référents
- 258 assertions atomiques
- 6 sources de référence / synthèse
- données de test synthétiques séparées des connaissances du monde réel
- validation JSON Schema + audit de graphe + manifeste SHA-256

## Fichiers principaux

- `knowledge-base/corpus/geographyspace.kristal-state.json` — état canonique v6
- `knowledge-base/corpus/geographyspace.referent-registry.json` — identités stables
- `knowledge-base/corpus/relation-algebra.json` — propriétés des relations spatiales
- `knowledge-base/corpus/scale-model.json` — séparation stricte des sens d’« échelle »
- `knowledge-base/corpus/domain-coverage.json` — couverture et exclusions
- `knowledge-base/sources/source-catalog.json` — provenance documentaire
- `knowledge-base/tools/validate.py` — validation complète
- `knowledge-base/tools/query.py` — requête locale simple

## Invariants critiques

1. **Référent ≠ géométrie.** Une géométrie représente une entité; elle n’en constitue pas l’identité.
2. **Coordonnées ≠ localisation sans CRS.**
3. **Territoire ≠ autorité.** Aucune souveraineté, propriété ou compétence n’est déduite d’une géométrie.
4. **Étendue ≠ résolution ≠ grain ≠ échelle cartographique.**
5. **Proximité ≠ adjacence ≠ connectivité réseau.**
6. **Distribution observée ≠ processus causal.**
7. **Flux ≠ trajectoire.** Un OD peut être connu sans chemin observé.

## Validation

```bash
cd knowledge-base
python tools/validate.py
python tools/audit_graph.py
python tools/query.py --topic flux
```

## Kristal v9

Ce repo est migré vers **Kristal 9.0.0-draft.1 — Semantic State Architecture** sans supprimer les surfaces v6/v8 existantes.

- canon v9 : le state v6 canonique `knowledge-base/corpus/geographyspace.kristal-state.json`;
- snapshot logique immuable : `.kristal/v9/state-snapshot.json`;
- matérialisation(s) : `.kristal/v9/materialization.*.json`;
- projection portable v6 : conservée sous `.kristal/v8/portable-state.kristal-state.json` et explicitement dérivée;
- indexes/read models v8 : restent dérivés et reconstruisibles;
- identité logique v9 : séparée des digests physiques des fichiers.

Voir `.kristal/v9/README.md` et `V9-MIGRATION.md`.
