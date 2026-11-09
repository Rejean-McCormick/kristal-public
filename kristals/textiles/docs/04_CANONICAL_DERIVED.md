# Canonique versus dérivé

Entrée canonique de build 3.2.2 : `canon/domain/kristal-textiles.canonical-payload.json`. Les sources métier historiques restent sous `knowledge-base/sources`. Le fichier `.kristal/v9` historique n’est pas réécrit.

`materializations/v9/factorized/` est une représentation physique réversible avec dictionnaire des clés et valeurs communes. `knowledge-base/corpus`, `build/v9`, `runtime` et les indices hérités sont des read models et/ou matérialisations, pas de nouvelles autorités.

Logical Commitment attendu : `sha256:e9934a06bcd24c36e1dc5c6457e5a5e543875aa2c8fee8707d0bdd91eba184a6`. Changer compression ou emplacement ne doit pas le modifier.
