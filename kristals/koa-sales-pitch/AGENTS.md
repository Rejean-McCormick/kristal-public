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


## Garde-fous propres à Sales Pitch

- Ne jamais présenter les 120 scénarios historiques et les 36 archétypes V2 comme 156 validations indépendantes.
- Ne jamais promouvoir une illustration utilisateur, un stress test d'actualité ou une synthèse interne au rang de validation de marché.
- Ne jamais annoncer une preuve E2E comme vérifiée tant qu'un artefact reproductible n'est pas attaché et enregistré.
- Pour la sécurité, distinguer principe architectural, contrôles techniques, pratiques humaines et preuve de déploiement.
- Préserver la distinction kOA / Digital Ecosystem / Koali / Kristal / Konnaxion / Orgo.
- Le miroir `knowledge-base/corpus/sales-pitch.kristal-state.json` doit rester byte-identique à `canon/domain/sales-pitch.kristal-state.json` tant que les outils legacy sont conservés.
