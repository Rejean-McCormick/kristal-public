# Canon et dérivés — Kristal-Accounting

- `canon/state.index.json` engage exactement les membres du snapshot v9 historique.
- `canon/domain/*.payload.json` contient les payloads canoniques de ces membres, recalculés selon JCS-SHA256.
- `canon/epistemic/legacy-build-input-*.payload.json` préserve les payloads logiques de source utilisés pour le build, **hors membres State**.
- Les vrais composants métier de référence (notamment l'état v6 sous `knowledge-base/corpus/` et les sources métier) restent conservés en place. On **ne classe pas tout `knowledge-base/corpus` comme dérivé**.
- `.kristal/v8`, les index et les documents de lecture sont des couches de compatibilité ; `.kristal/v9` est un paquet historique conservé.
- `build/v9` est une reconstruction, jamais une nouvelle autorité.

Les manifests de matérialisation v9 historiques sont réimportés tels quels après vérification des digests de leurs segments. Un manifest natif ne constitue pas une preuve de factorisation.
