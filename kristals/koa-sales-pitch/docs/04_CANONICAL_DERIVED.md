# Canonique et dérivé

## Source de vérité

Le canon Local 3.2.2 est `canon/domain/sales-pitch.kristal-state.json`. Il est une copie byte-identique de l'ancien état compilé v6 afin de préserver la continuité sémantique.

`knowledge-base/corpus/sales-pitch.kristal-state.json` est conservé comme **miroir de compatibilité legacy** pour les outils v6/v8 et doit rester byte-identique au canon tant que ces outils existent.

## Logical Artifacts canoniques

`canon/state.index.json` enregistre `urn:kristal:koa-sales-pitch:canonical` sous le contrat `kristal.v6-state-reference/1.0`. Le commitment précomputed préserve l'identité logique v9 déjà établie.

## Artefacts dérivés / Runtime

Sont dérivés : `.kristal/v8`, `.kristal/v9` historique, `views/`, `knowledge-base/profiles/`, `knowledge-base/corpus/` comme miroir legacy, `derived/`, `runtime/`, `state/` et `build/`.

Les fichiers sous `knowledge-base/sources/` restent des entrées éditoriales/support ; ils ne sont pas promus individuellement comme Logical Artifacts canoniques dans cette migration.

## Materializations

La copie sous `canon/domain` est la matérialisation locale autoritative utilisée par le workspace 3.2.2. L'ancienne matérialisation v9 sous `.kristal/v9` demeure un artefact historique de compatibilité.

## Recettes de reconstruction

Le package conserve ses outils natifs `knowledge-base/tools/validate.py` et `query.py`. Le lifecycle Local 3.2.2 utilise `tools/kristal.py check .` puis `tools/kristal.py build-v9 .`.
