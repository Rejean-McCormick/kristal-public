# Canonique versus dérivé

Entrée canonique de build 3.2.2 : `canon/domain/kristal-theatre.canonical-payload.json`. Les sources métier historiques restent sous `knowledge-base/sources`. Le fichier `.kristal/v9` historique n’est pas réécrit.

`materializations/v9/factorized/` est une représentation physique réversible avec dictionnaire des clés et valeurs communes. `knowledge-base/corpus`, `build/v9`, `runtime` et les indices hérités sont des read models et/ou matérialisations, pas de nouvelles autorités.

Logical Commitment attendu : `sha256:a6fa33edc0da8707e468a304f288e7b51d38a8a887ffd44a174ab755aca20843`. Changer compression ou emplacement ne doit pas le modifier.
