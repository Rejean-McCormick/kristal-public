# Canonique et dérivé

## Source(s) de vérité

Pour l'authoring Local 3.2.2, `canon/state.index.json` est le registre des Logical Artifacts canoniques. Les fichiers sous `canon/artifacts/` sont des copies **byte-identiques** des neuf artefacts précédemment canoniques sous `.kristal/v9/artifacts/`. Leur déplacement physique ne change donc ni contrat ni engagement logique.

## Logical Artifacts canoniques

Les neuf artefacts sont déclarés dans `canon/state.index.json` en mode `precomputed` avec leurs engagements `kristal.logical/jcs-sha256-v1` existants.

## Artefacts dérivés / Runtime

`.kristal/v8/` reste un read model/query/index legacy. `.kristal/v9/` est conservé comme surface v9 historique de matérialisation, échange, activation locale et compatibilité. `knowledge-base/media_coverage_report.json`, les index et les sorties `build/` ne sont pas le canon.

## Materializations

Les materialization manifests historiques sous `.kristal/v9/materializations/` décrivent la représentation physique des Logical Artifacts. Ils ne remplacent pas l'identité logique.

## Recettes de reconstruction

- validation historique de domaine : `python knowledge-base/tools/validate.py` ;
- rebuild historique v9 : `python knowledge-base/tools/build_v9.py` ;
- validation Local 3.2.2 : `python tools/kristal.py check .` ;
- build Local 3.2.2 : `python tools/kristal.py build-v9 .`.
