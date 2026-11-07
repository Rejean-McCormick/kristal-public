# AI Context — Accounting

This is a deterministic, derived orientation document for offline AI reading. It is not the canon.

- State ref: `urn:kristal:accounting:state`
- State Logical Commitment: `sha256:5453336ee188d670da638c0afd1c86a6e7ea7b36df75fe58322bcfacfa4f2a3a`
- Workspace profile: `layered`
- Native model: `accounting_event_ledger_graph`
- Canonical artifacts: `2`
- Sources: `10`
- External pinned references: `0`
- Materialization manifests: `3`
- Workspace-local materialization blobs: `0`

## Reading rule

Treat `canon/` and the exact `state/state-snapshot.json` as the semantic basis. Treat `ai/` as derived navigation. Use `sources/` for provenance. Materialization manifests describe physical representations and may point to local or external bytes without changing semantic identity. Do not require GitHub or any executable tool to read this package.

---

## Included orientation from `docs/00_INTENT_AND_SCOPE.md`

# Intentions et périmètre — Kristal-Accounting

Le domaine et les exclusions sont définis par `README.md`, `knowledge-base/documentation/` et les sources historiques conservées octet par octet.

**Orientation historique** : Événement économique → reconnaissance/mesure → écriture → compte/livre → période → état financier.

La mise à jour est structurelle : l'enveloppe Local 3.2.2 s'ajoute au State v9 établi, sans réécrire ses identités ou son modèle métier.

**State ref** : `urn:kristal:accounting:state`.

---

## Included orientation from `docs/01_SEMANTIC_BOUNDARY.md`

# Frontière sémantique — Kristal-Accounting

Domaine déclaré : `accounting`.

Distinction fondatrice à préserver : **événement économique, pièce justificative, écriture, compte, période et preuve demeurent distincts**.

La connaissance, les limites et les non-équivalences documentées dans `README.md` et `knowledge-base/documentation/` restent les références pour les futures éditions. Les sources externes demeurent externes, et les projections ne transfèrent pas la propriété sémantique.

---

## Included orientation from `docs/02_NATIVE_MODEL.md`

# Modèle natif — Kristal-Accounting

Type : `accounting_event_ledger_graph`.

Orientation / structure : **Événement économique → reconnaissance/mesure → écriture → compte/livre → période → état financier**.

Il faut respecter la structure historisée : ne pas transformer une trajectoire, un graphe multiplexe, un ledger ou une série de mesures contextualisées en une table générique non typée.

Le builder 3.2.2 travaille avec les payloads existants sous `canon/domain/` et conserve les Logical Contracts existants des membres State v9 :

- `accounting.canonical-knowledge-state/1.0` — `urn:kristal:accounting:artifact:canonical-state`
- `accounting.identity-registry/1.0` — `urn:kristal:accounting:artifact:identity-registry`

---

## Included orientation from `docs/03_EPISTEMIC_MODEL.md`

# Provenance et épistémologie — Kristal-Accounting

Le catalogue source normalisé `sources/source-catalog.json` est un **index de lecture non arbitral** de `external-source-library/source-store.json`; les entrées originelles sont conservées sous `native_metadata`. Les autorités et les niveaux de preuve restent définis par les documents métier hérités.

Aucune sortie IA ou nouvelle inférence ne devient automatiquement autorité. Conserver les absences, les conflits et les nuances de provenance, sans prendre une projection comme source primaire.

Le `build_input` historique `1 artefact(s)` reste distinct des `2 membres` engagés dans le State Snapshot.

---

## Included orientation from `docs/04_CANONICAL_DERIVED.md`

# Canon et dérivés — Kristal-Accounting

- `canon/state.index.json` engage exactement les membres du snapshot v9 historique.
- `canon/domain/*.payload.json` contient les payloads canoniques de ces membres, recalculés selon JCS-SHA256.
- `canon/epistemic/legacy-build-input-*.payload.json` préserve les payloads logiques de source utilisés pour le build, **hors membres State**.
- Les vrais composants métier de référence (notamment l'état v6 sous `knowledge-base/corpus/` et les sources métier) restent conservés en place. On **ne classe pas tout `knowledge-base/corpus` comme dérivé**.
- `.kristal/v8`, les index et les documents de lecture sont des couches de compatibilité ; `.kristal/v9` est un paquet historique conservé.
- `build/v9` est une reconstruction, jamais une nouvelle autorité.

Les manifests de matérialisation v9 historiques sont réimportés tels quels après vérification des digests de leurs segments. Un manifest natif ne constitue pas une preuve de factorisation.
