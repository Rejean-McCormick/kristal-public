# Canonique versus dérivé

Entrée canonique de build 3.2.2 : `canon/domain/kristal-telecommunications.canonical-payload.json`. Les sources métier historiques restent sous `knowledge-base/sources`. Le fichier `.kristal/v9` historique n’est pas réécrit.

`materializations/v9/factorized/` est une représentation physique réversible avec dictionnaire des clés et valeurs communes. `knowledge-base/corpus`, `build/v9`, `runtime` et les indices hérités sont des read models et/ou matérialisations, pas de nouvelles autorités.

Logical Commitment attendu : `sha256:e604ccc4bf67bed4f08d047def200fc85a25a781701b0f7e7fc3e2501731e5f5`. Changer compression ou emplacement ne doit pas le modifier.
