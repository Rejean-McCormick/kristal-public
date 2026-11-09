# Instructions IA locales — Kristal v10 Authoring

Lire d'abord le `AGENTS.md` du Kristal Authoring Kit si disponible, puis `docs/00_...` à `docs/07_...` de ce Kristal.

Ne jamais inventer de contenu pour remplir un fichier vide. Un champ `unknown`, une liste vide ou un stub explicite est préférable à une fausse complétude.

Avant toute modification du canon :

1. identifier la source et l'autorité ;
2. déterminer le régime épistémique ;
3. vérifier l'ownership ;
4. préserver les Semantic IDs existants ;
5. distinguer contenu logique, build, matérialisation, hosting et read model ;
6. mettre à jour les dérivés uniquement après le canon ;
7. ne jamais changer un Logical Commitment en modifiant seulement compression, segment, index, cache, repo, branche ou URL.

Avant publication réseau :

```text
check
  ↓
build-v9
  ↓
export-hosted
  ↓
commit/push exact
  ↓
github-qualify exact commit
  ↓
github-publish
  ↓
verify publication bundle
  ↓
activate seulement si explicitement demandé
```

Une IA peut préparer, vérifier et proposer. Elle ne doit pas considérer une sortie IA comme canonique, ni transformer une publication en activation implicite.
