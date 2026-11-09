# Instructions IA locales — Kristal Local 3.2

Ce fichier concerne les agents qui **modifient** un Local Kristal. La couche `AI_START_HERE.md` n'existe que si un read model IA optionnel a été construit.

Ne jamais inventer de contenu pour remplir un fichier vide. Un champ `unknown`, une liste vide ou un stub explicite est préférable à une fausse complétude.

Avant toute modification du canon :

1. identifier la source et l'autorité ;
2. déterminer le régime épistémique ;
3. vérifier l'ownership ;
4. préserver les Semantic IDs existants ;
5. distinguer contenu logique, build, matérialisation, hosting et read model ;
6. mettre à jour les dérivés uniquement après le canon ;
7. ne jamais changer un Logical Commitment en modifiant seulement compression, segment, index, cache, repo, branche, URL ou couche `ai/`.

Après une modification canonique :

```text
check
  ↓
build-v9
  ↓
portable AI read layer regenerated automatically
  ↓
check-ai
```

Pour une publication réseau optionnelle :

```text
export-hosted
  ↓
commit/push exact
  ↓
Kristal GitHub Setup: qualify exact commit
  ↓
Kristal GitHub Setup: publish / activate
  ↓
verify publication bundle
  ↓
activate seulement si explicitement demandé
```

Une IA peut préparer, vérifier et proposer. Elle ne doit pas considérer une sortie IA comme canonique, ni transformer une publication en activation implicite.

## Règles propres au Kristal « Qui décide quoi ? »

- Conserver la distinction **fonction / titulaire**, **autorité juridique / responsabilité politique**, **décision / contrôle** et le régime de chaque ordre juridique sans imposer un modèle identique aux autres pays.
- Un fait juridique est cadré par la juridiction, l'applicabilité et la date de référence ; aucun changement de droit récent n'est affirmé par la migration.
- Le droit international et le droit substantiel de l'UE appartiennent au Kristal supranational distinct, sauf interfaces internes explicitement engagées.
- Préserver le contenu de `knowledge-base/corpus/` et la bibliothèque de sources native ; ces composants métier sont canoniques historiques, pas des caches éliminables.
- Ne pas modifier `.kristal/v9/` : son State Commitment historique est l'étalon de la normalisation.
- Préférer `python tools/build-preserving-v9.py` au build standard seul pour réimporter la matérialisation v6 native et vérifier sa reconstruction.
- Ne pas confondre passage de `check` et validation de l'exactitude juridique, ni un fichier d'activation historique et une nouvelle activation.
