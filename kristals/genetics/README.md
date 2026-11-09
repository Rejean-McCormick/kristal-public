# Kristal-Genetics v0.1.0

Corpus statique validé sur l'information héréditaire : **locus, variante, génotype, expression, phénotype et transmission**.

## Principe

Le Kristal encode des niveaux distincts au lieu de réduire la génétique à « un gène = un trait » :

`locus → variante → génotype → expression / produit → phénotype`, avec la **transmission** comme graphe séparé.

Une association n'est jamais promue en causalité sans source explicite. La présence d'un variant n'est pas un phénotype. L'expression dépend du contexte cellulaire et biologique.

## Seed v0.1.0

- 6 loci / systèmes génomiques
- 7 variants ou classes alléliques
- 9 états génotypiques
- 6 enregistrements d'expression / produit
- 7 phénotypes de référence
- 6 modèles de transmission
- 48 relations explicites
- 189 assertions Kristal v6
- 18 sources institutionnelles

Exemples mécanistiquement distincts : HBB/HbS, CFTR/F508del, ABO, F8, HTT et ADN mitochondrial.

## État canonique

`knowledge-base/corpus/genetics.kristal-state.json`

Les autres JSON sont des vues/registries lisibles du même domaine.

## Usage et limites

Corpus de référence, pas un outil de diagnostic ni d'interprétation de résultats individuels. Les classifications ClinVar sont conservées avec leur contexte de condition et de source. Les fréquences de population, scores polygéniques et inférences d'ascendance sont volontairement hors seed.

## Validation

```bash
python knowledge-base/tools/validate.py
```

## Kristal v9

Ce repo est migré vers **Kristal 9.0.0-draft.1 — Semantic State Architecture** sans supprimer les surfaces v6/v8 existantes.

- canon v9 : le state v6 canonique `knowledge-base/corpus/genetics.kristal-state.json`;
- snapshot logique immuable : `.kristal/v9/state-snapshot.json`;
- matérialisation(s) : `.kristal/v9/materialization.*.json`;
- projection portable v6 : conservée sous `.kristal/v8/portable-state.kristal-state.json` et explicitement dérivée;
- indexes/read models v8 : restent dérivés et reconstruisibles;
- identité logique v9 : séparée des digests physiques des fichiers.

Voir `.kristal/v9/README.md` et `V9-MIGRATION.md`.
