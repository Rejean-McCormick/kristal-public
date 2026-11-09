# Hébergement, publication et lecture — Kristal Catho

## Architecture et statut

Ce dépôt demeure un **Kristal local**, avec six Logical Artifacts et un State Snapshot au contrat **`kristal.state/9.0`**. C'est normal dans le Framework **v10 (`10.0.0-draft.3.2`)** : la v10 ajoute l'architecture de réseau hébergé et conserve le modèle sémantique v9 et ses engagements.

La publication v10 nécessite un hôte, un binding concret, une révision Git exacte, une qualification indépendante (C1) et les autorisations de publication requises (C2/C3 selon la chaîne). Aucun de ces éléments n'est supposé, inventé ou créé par cette mise à jour locale. **Aucune synchronisation GitHub, publication immuable ou activation n'a eu lieu.** Le workspace demeure `building`.

Les éléments historiques `.kristal/v9/` (ancien snapshot, Exchange, Activation) sont conservés tels quels ; ils ne sont pas des preuves de publication de la présente version à six artefacts.

## Métadonnées de lecture

- `build/v9/` : artefacts logiques et snapshot **candidats** reconstruits de manière déterministe ; aucun engagement canonique n'est modifié.
- `kristal.discovery.json` et `derived/reader-{inventory,profile}.json` : inventaire et conseils de lecture **non canoniques**, générés par l'Authoring Kit 3.3.1.
- `ai/` et `AI_MANIFEST.json` : projection déterministe **non canonique** liée à l'état local ; sa présence ne signifie pas qu'une IA doit être exécutée. `portable_ai.enabled` demeure `false`.
- `derived/catho-graph/` : graphe exploratoire hors canon ; les rapprochements candidats ne sont pas des équivalences établies.

Les lecteurs (dont Konstellation) doivent vérifier les octets effectivement lus, le format physique, les tailles et les empreintes. Les métadonnées Discovery ne sont ni une preuve de validité doctrinale, ni une autorisation d'accès, ni un droit de publication.

## Vérification locale (aucun envoi réseau)

Depuis le dossier du Kristal :

```bash
python tools/kristal.py check .
python tools/kristal.py audit-discovery . --require-fresh
python tools/kristal.py read-surface . --require-ready
```

Le dernier test porte sur la préparation technique d'une projection, **pas** sur une autorisation de synchronisation. Après chaque modification des sources enregistrées ou de la projection de lecture, reconstruire les sorties dérivées concernées et relancer ces contrôles. Le rapport propre à cette mise à jour est `validation/MAJ_LOCALE_V10_2026-10-16.md`.
