# Canonique versus dérivé

Entrée canonique de build 3.2.2 : `canon/domain/kristal-virology.canonical-payload.json`. Les sources métier historiques restent sous `knowledge-base/sources`. Le fichier `.kristal/v9` historique n’est pas réécrit.

`materializations/v9/factorized/` est une représentation physique réversible avec dictionnaire des clés et valeurs communes. `knowledge-base/corpus`, `build/v9`, `runtime` et les indices hérités sont des read models et/ou matérialisations, pas de nouvelles autorités.

Logical Commitment attendu : `sha256:3cc5eb9afa33f4380ceb97f731367f7fcafe86cd181198f7a747c8f5880f5725`. Changer compression ou emplacement ne doit pas le modifier.
