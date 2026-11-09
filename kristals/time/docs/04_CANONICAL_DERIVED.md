# Canonique versus dérivé

Entrée canonique de build 3.2.2 : `canon/domain/kristal-time.canonical-payload.json`. Les sources métier historiques restent sous `knowledge-base/sources`. Le fichier `.kristal/v9` historique n’est pas réécrit.

`materializations/v9/factorized/` est une représentation physique réversible avec dictionnaire des clés et valeurs communes. `knowledge-base/corpus`, `build/v9`, `runtime` et les indices hérités sont des read models et/ou matérialisations, pas de nouvelles autorités.

Logical Commitment attendu : `sha256:47cf73e1fcc2b6b9368583aca08056a1319383abc7c10ea1ec250937747b3f29`. Changer compression ou emplacement ne doit pas le modifier.
