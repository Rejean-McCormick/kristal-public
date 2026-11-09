# Canonique versus dérivé

Entrée canonique de build 3.2.2 : `canon/domain/kristal-transportation.canonical-payload.json`. Les sources métier historiques restent sous `knowledge-base/sources`. Le fichier `.kristal/v9` historique n’est pas réécrit.

`materializations/v9/factorized/` est une représentation physique réversible avec dictionnaire des clés et valeurs communes. `knowledge-base/corpus`, `build/v9`, `runtime` et les indices hérités sont des read models et/ou matérialisations, pas de nouvelles autorités.

Logical Commitment attendu : `sha256:46b4f599100e71769115eb49ea8c62e4cb4ee885afcfa31112297d51bb5036c6`. Changer compression ou emplacement ne doit pas le modifier.
