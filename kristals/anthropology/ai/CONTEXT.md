# AI Context — Anthropology

This is a deterministic, derived orientation document for offline AI reading. It is not the canon.

- State ref: `urn:kristal:anthropology:state`
- State Logical Commitment: `sha256:295dda54df336245779cf88a8649f048a3bfd3e3756bca08ce7821d47d21c9f6`
- Workspace profile: `layered`
- Native model: `situated_comparative_cultural_graph`
- Canonical artifacts: `9`
- Sources: `14`
- External pinned references: `0`
- Materialization manifests: `2`
- Workspace-local materialization blobs: `0`

## Reading rule

Treat `canon/` and the exact `state/state-snapshot.json` as the semantic basis. Treat `ai/` as derived navigation. Use `sources/` for provenance. Materialization manifests describe physical representations and may point to local or external bytes without changing semantic identity. Do not require GitHub or any executable tool to read this package.

---

## Included orientation from `docs/00_INTENT_AND_SCOPE.md`

# Intentions et périmètre — Kristal-Anthropology

Le domaine et les exclusions sont définis par `README.md`, `knowledge-base/documentation/` et les sources historiques conservées octet par octet.

**Orientation historique** : Systèmes culturels, éléments, relations, contextes et axes de comparaison.

La mise à jour est structurelle : l'enveloppe Local 3.2.2 s'ajoute au State v9 établi, sans réécrire ses identités ou son modèle métier.

**State ref** : `urn:kristal:anthropology:state`.

---

## Included orientation from `docs/01_SEMANTIC_BOUNDARY.md`

# Frontière sémantique — Kristal-Anthropology

Domaine déclaré : `anthropology`.

Distinction fondatrice à préserver : **population ≠ culture ; description ≠ essence ; cooccurrence ≠ causalité**.

La connaissance, les limites et les non-équivalences documentées dans `README.md` et `knowledge-base/documentation/` restent les références pour les futures éditions. Les sources externes demeurent externes, et les projections ne transfèrent pas la propriété sémantique.

---

## Included orientation from `docs/02_NATIVE_MODEL.md`

# Modèle natif — Kristal-Anthropology

Type : `situated_comparative_cultural_graph`.

Orientation / structure : **Systèmes culturels, éléments, relations, contextes et axes de comparaison**.

Il faut respecter la structure historisée : ne pas transformer une trajectoire, un graphe multiplexe, un ledger ou une série de mesures contextualisées en une table générique non typée.

Le builder 3.2.2 travaille avec les payloads existants sous `canon/domain/` et conserve les Logical Contracts existants des membres State v9 :

- `anthropology.canonical-knowledge-state/1.0` — `urn:kristal:anthropology:artifact:canonical-state`

---

## Included orientation from `docs/03_EPISTEMIC_MODEL.md`

# Provenance et épistémologie — Kristal-Anthropology

Le catalogue source normalisé `sources/source-catalog.json` est un **index de lecture non arbitral** de `knowledge-base/sources/source-catalog.json`; les entrées originelles sont conservées sous `native_metadata`. Les autorités et les niveaux de preuve restent définis par les documents métier hérités.

Aucune sortie IA ou nouvelle inférence ne devient automatiquement autorité. Conserver les absences, les conflits et les nuances de provenance, sans prendre une projection comme source primaire.

Le `build_input` historique `1 artefact(s)` reste distinct des `1 membres` engagés dans le State Snapshot.

---

## Included orientation from `docs/04_CANONICAL_DERIVED.md`

# Canon et dérivés — Kristal-Anthropology

- `canon/state.index.json` engage exactement les membres du snapshot v9 historique.
- `canon/domain/*.payload.json` contient les payloads canoniques de ces membres, recalculés selon JCS-SHA256.
- `canon/epistemic/legacy-build-input-*.payload.json` préserve les payloads logiques de source utilisés pour le build, **hors membres State**.
- Les vrais composants métier de référence (notamment l'état v6 sous `knowledge-base/corpus/` et les sources métier) restent conservés en place. On **ne classe pas tout `knowledge-base/corpus` comme dérivé**.
- `.kristal/v8`, les index et les documents de lecture sont des couches de compatibilité ; `.kristal/v9` est un paquet historique conservé.
- `build/v9` est une reconstruction, jamais une nouvelle autorité.

Les manifests de matérialisation v9 historiques sont réimportés tels quels après vérification des digests de leurs segments. Un manifest natif ne constitue pas une preuve de factorisation.
