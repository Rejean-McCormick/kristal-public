# AGENTS — Kristal-ScolQc

Ce dépôt est un Local Kristal 3.2.2 qui conserve sans réécriture sémantique la release domaine **1.4.0** et son état v9 existant.

## Règles de modification

1. Préserver la forme native : graphe éducatif temporel et juridictionnel, règles, transitions, curriculum, admission, provenance et gouvernance des sources.
2. Ne jamais confondre `authority`, `document`, `edition`, `representation` et snapshot local.
3. Ne jamais interpréter une transition comme une admission garantie, ni un curriculum comme une règle d'admission.
4. La couverture du Kristal n'est pas la vérité institutionnelle. Une absence de couverture ne vaut pas `false`.
5. `external-source-library/` et `source-manager/` sont opérationnels. Leurs octets, captures et états locaux ne font pas partie du canon logique du Kristal.
6. Les quatre fichiers sous `canon/artifacts/` sont les Logical Artifacts v9 promus, byte-identiques à la couche v9 historique au moment de la normalisation. Si les ressources de domaine changent, ils doivent être régénérés/requalifiés avant release.
7. Les sorties de `.kristal/v8/`, `.kristal/v9/`, `build/`, `release/`, `runtime/`, `derived/`, `state/` et `validation/` sont dérivées ou opérationnelles.
8. Ne pas publier ou activer automatiquement. Build, qualification, publication et activation sont des étapes séparées.

## Validation minimale avant toute release

Depuis `knowledge-base/` :

```bash
python tools/build.py
python tools/validate.py
```

Puis avec le Kristal Authoring Kit 3.2.2 :

```bash
python tools/kristal.py check <Kristal-ScolQc>
python tools/kristal.py build-v9 <Kristal-ScolQc>
```

Le build 3.2.2 doit préserver les quatre commitments membres historiques. Toute divergence doit être expliquée et qualifiée comme changement sémantique ou changement de segmentation avant publication.
