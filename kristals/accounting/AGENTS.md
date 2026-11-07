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

## Contraintes propres à Kristal-Accounting

- **Forme native** : accounting_event_ledger_graph; Événement économique → reconnaissance/mesure → écriture → compte/livre → période → état financier.
- **Invariant** : événement économique, pièce justificative, écriture, compte, période et preuve demeurent distincts.
- Ne pas ajouter le `build_input` historique comme membre State v9.
- Ne pas modifier silencieusement le contenu de `.kristal/v9/` ou le corpus de référence historique.
- Le build à privilégier est `python tools/build-preserving-v9.py` afin de réimporter et revalider les matérialisations v9 natives.
- Ne jamais prétendre avoir factorisé une représentation si seuls des blobs natifs sont présents.

## Couche de standardisation 2026-10-17 — Authoring Kit v4 draft.2

- Le domaine historique v6/v8/v9 est **figé** : ses deux membres canoniques et ses trois matérialisations historiques restent inchangés ; les sources éditoriales sont un `build_input`, pas un troisième membre canonique.
- `tools/kristal.py` est adapté localement pour ignorer **uniquement** la matérialisation `source-bundle` référencée comme `historical_build_inputs` au moment du build canonique. `tools/build-preserving-v9.py` en vérifie toujours les blobs et le SHA. Ne jamais transformer ce contournement en admission canonique.
- La migration v11 est **candidate**, inventoriée sous `derived/v11/` seulement. Les 216 familles KQ et 73 familles KP ne sont PAS des IDs alloués, et les 581 assertions ne sont PAS des KA déjà migrées.
- Ne jamais remplacer un URN historique par un KQ inventé, ou lui attribuer un Q Wikidata par similarité de libellé. La validation des rôles, des preuves et des dictionnaires appartient aux outils et approbations v11/diK.
- Lire `docs/08_V11_STANDARDIZATION.md` et exécuter `python tools/validate-standardization.py` avant toute édition sémantique.
