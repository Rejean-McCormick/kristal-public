# Instructions IA locales — Kristal-PoliceOps / Local 3.2.2

Ce fichier régit les agents qui modifient ce Local Kristal. Le corpus canonique actuel est `knowledge-base/corpus/policeops.structured-epistemic-state.json`.

## Invariants

- Ne jamais inventer de contenu pour combler une lacune. `unknown`, une liste vide ou une limitation explicite est préférable.
- Ne pas promouvoir une assertion `claimed` ou `sourced` en règle reconnue sans validation et canal d’autorité explicites.
- Préserver les Semantic IDs, `state_id`, hashes et source IDs existants sauf migration canonique explicitement décidée.
- Le Source Store externe matérialise des bytes; il ne devient pas propriétaire de la vérité sémantique.
- Orgo possède Cases, Tasks, workflow et décisions en cours; PoliceOps ne doit pas absorber silencieusement ce lifecycle.
- Les répertoires `.kristal/v8`, `.kristal/v9`, `build/`, `validation/`, `runtime/`, `external-source-library/` et les index sont dérivés ou opérationnels.
- Une sortie IA reste une proposition tant qu’elle n’a pas été acceptée par le processus d’autorité approprié.

## Avant toute modification canonique

1. identifier la source et l’autorité;
2. déterminer le régime épistémique;
3. vérifier l’ownership;
4. préserver les IDs;
5. distinguer canon, build, matérialisation, hosting et read model;
6. ne pas masquer les conflits, inconnues ou limitations de source.

## Validation locale

```text
python knowledge-base/tools/validate.py
python tools/kristal.py check .
python tools/kristal.py build-v9 .
```

Le build ne publie et n’active rien. La publication/activation réseau reste une opération distincte et ne doit jamais être implicite.
