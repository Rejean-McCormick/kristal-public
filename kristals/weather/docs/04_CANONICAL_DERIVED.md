# Canonique versus dérivé

Entrée canonique de build 3.2.2 : `canon/domain/kristal-weather.canonical-payload.json`. Les sources métier historiques restent sous `knowledge-base/sources`. Le fichier `.kristal/v9` historique n’est pas réécrit.

`materializations/v9/factorized/` est une représentation physique réversible avec dictionnaire des clés et valeurs communes. `knowledge-base/corpus`, `build/v9`, `runtime` et les indices hérités sont des read models et/ou matérialisations, pas de nouvelles autorités.

Logical Commitment attendu : `sha256:3046a3a957605cc866a19bbd2e59756f782a2ddc3559a572c6a8f3f2204f0012`. Changer compression ou emplacement ne doit pas le modifier.
