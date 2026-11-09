# Canonique et dérivé — Kristal-Cybersecurity

## Canon 3.2.2

`canon/domain/legacy-v6-state.payload.json` est un adaptateur lossless du payload du Logical Artifact historique `urn:kristal:cybersecurity:canonical-state`.

`canon/state.index.json` lie le contenu à son contrat, son scope, son authority_ref et au calcul `compute-json-jcs`.

## Legacy / matérialisation

Les répertoires `knowledge-base/` originaux ne sont ni écrasés ni désactivés. Le manifest d’origine `.kristal/v9/materialization-manifest.json` enregistre `kristal.materialization/native-blob/1` et les blobs immuables référencés. La couche 3.2.2 génère en plus `inline-json/1`; elle **ne remplace pas** le manifest d’origine, ni ne réclame une factorisation non construite.

Les projections historiques sous `knowledge-base/corpus/` et les index `.kristal/v8/` restent disponibles.
