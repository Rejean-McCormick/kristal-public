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

## Exigences particulières à Kristal-Software

- Invariant : Intention ≠ exigence ≠ spécification ≠ code ≠ exécution ; défaut ≠ état erroné ≠ défaillance.
- Forme native : `typed_software_lifecycle_graph`.
- Préserver toutes les distinctions, provenances et qualifications métier figurant dans le canon historique.
- `.kristal/v9` contient une matérialisation existante contrôlée, distincte de celle générée par le kit.
- Ne pas déclarer factorization/segmentation sans matérialisation construite et preuve de reconstruction.
- Toute modification de Logical Commitment doit être traitée comme une révision de connaissance et non une simple migration.
