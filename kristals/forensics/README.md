# Kristal-Forensics v1.0.0

**Trace → acquisition → analyse → comparaison → interprétation → conclusion limitée.**

Kristal-Forensics décrit la chaîne épistémique générale de la science forensique. Il représente les traces, leur acquisition et intégrité, la performance des méthodes, la comparaison, l'interprétation sous propositions explicites, puis la communication de conclusions dont la portée reste bornée par les données et les limitations.

## Noyau conceptuel

```text
trace
  ↓
acquisition ──> identité / provenance / chaîne de possession
  ↓
analyse ──────> observation / mesure / performance / incertitude
  ↓
comparaison ──> ressemblances + différences + variabilité
  ↓
interprétation ──> propositions + modèle + données de référence
  ↓
conclusion limitée ──> portée + incertitude + limitations
```

## Distinctions obligatoires

- observation ≠ interprétation;
- résultat analytique ≠ conclusion probante;
- similarité ≠ source commune;
- chaîne de possession ≠ preuve de vérité ou d'origine;
- validation d'une méthode ≠ garantie de justesse pour chaque cas;
- taux d'erreur de validation ≠ probabilité que cette conclusion particulière soit erronée;
- rapport de vraisemblance ≠ probabilité a posteriori d'une proposition;
- identification ≠ absence d'incertitude;
- accréditation ≠ infaillibilité;
- opinion experte ≠ décision factuelle ultime.

## Portée v1

Le corpus est transversal aux disciplines. Il couvre acquisition, préservation, chaîne de possession, contamination, échantillonnage, validation, performances, incertitude, caractéristiques comparées, populations de référence, propositions source/activité, rapports de vraisemblance, facteurs humains, communication des limitations et conclusions bornées. Les disciplines spécialisées sont des interfaces, pas des procédures opérationnelles détaillées.

## Frontière volontaire

Cette version ne contient ni protocoles de laboratoire pas-à-pas, ni recettes d'acquisition opérationnelle, ni procédures permettant de contourner une investigation, ni règles juridiques propres à une juridiction, ni seuils universels d'identification. Les méthodes spécifiques appartiennent à des Kristals disciplinaires ou à des référentiels professionnels versionnés.

## Reproductibilité

```bash
python knowledge-base/tools/build.py
python knowledge-base/tools/validate.py
python knowledge-base/tools/query.py --concept "conclusion limitée"
```

Les artefacts canoniques sont statiques, hashés et reconstruits déterministiquement.

## Kristal v9

Ce repo est migré vers **Kristal 9.0.0-draft.1 — Semantic State Architecture** sans supprimer les surfaces v6/v8 existantes.

- canon v9 : le state v6 canonique `knowledge-base/corpus/forensics.kristal-state.json`;
- snapshot logique immuable : `.kristal/v9/state-snapshot.json`;
- matérialisation(s) : `.kristal/v9/materialization.*.json`;
- projection portable v6 : conservée sous `.kristal/v8/portable-state.kristal-state.json` et explicitement dérivée;
- indexes/read models v8 : restent dérivés et reconstruisibles;
- identité logique v9 : séparée des digests physiques des fichiers.

Voir `.kristal/v9/README.md` et `V9-MIGRATION.md`.
