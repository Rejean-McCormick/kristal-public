# AI Context — Cybersecurity

This is a deterministic, derived orientation document for offline AI reading. It is not the canon.

- State ref: `urn:kristal:state:cybersecurity`
- State Logical Commitment: `sha256:ce349a4ad4d44b2f71f5d91294ae3f55e1a3a677941c3ec6cb57560a2e60292d`
- Workspace profile: `layered`
- Native model: `typed_risk_scenario_graph`
- Canonical artifacts: `1`
- Sources: `11`
- External pinned references: `0`
- Materialization manifests: `0`
- Workspace-local materialization blobs: `0`

## Reading rule

Treat `canon/` and the exact `state/state-snapshot.json` as the semantic basis. Treat `ai/` as derived navigation. Use `sources/` for provenance. Materialization manifests describe physical representations and may point to local or external bytes without changing semantic identity. Do not require GitHub or any executable tool to read this package.

---

## Included orientation from `docs/00_INTENT_AND_SCOPE.md`

# Intention et scope — Kristal-Cybersecurity

## Intention originale (extrait README)

# Kristal-Cybersecurity v1.0.0

Corpus statique de référence en cybersécurité, centré sur le modèle :

**actif × menace × vulnérabilité × contrôle × impact**

Le noyau ajoute exposition, scénario, vraisemblance, preuve, état/efficacité des contrôles et risque inhérent/résiduel.

## Normalisation 3.2.2

Enveloppe de construction locale sans modification des assertions v6 ni des snapshots v9 historiques. Statut local `validated`, sans nouvelle publication ni activation.

---

## Included orientation from `docs/01_SEMANTIC_BOUNDARY.md`

# Frontière sémantique — Kristal-Cybersecurity

## Objet

actif × menace × vulnérabilité × contrôle × impact.

## Invariant

Taxonomie, scénario, preuve, état de contrôle et jugement de risque restent séparés.

## Ownership

Le Kristal engage sa connaissance locale existante. Les références externes ont leur propre autorité et le Kristal ne possède ni les sources amont ni leur maintenance.

## Identité stable

`state_ref`: `urn:kristal:state:cybersecurity` ; `authority_ref`: `urn:kristal:authority:cybersecurity`.

---

## Included orientation from `docs/02_NATIVE_MODEL.md`

# Modèle natif — Kristal-Cybersecurity

Type conservé : `typed_risk_scenario_graph`.

Orientation documentée : **actif × menace × vulnérabilité × contrôle × impact**.

Taxonomie, scénario, preuve, état de contrôle et jugement de risque restent séparés.

Les assertions typées, identités, provenances et contraintes restent dans le payload v6 historique. Le contrat logique est `kristal_state/6.0`. Le contenu original des modèles est conservé sous `knowledge-base/` sans conversion sémantique.

## Référence historique

`knowledge-base/documentation/ARCHITECTURE.md`.

---

## Included orientation from `docs/03_EPISTEMIC_MODEL.md`

# Modèle épistémique — Kristal-Cybersecurity

Les assertions historiques sont conservées avec leurs données de provenance. Le catalogue original est `external-source-library/source-store.json`. La version normalisée est un index d’accès ; elle ne promeut pas un enregistrement externe en vérité universelle.

Un conflit ne se résout pas par écrasement silencieux ; une absence de valeur n’équivaut pas à `false`. Les résultats d’une IA future ne sont pas des assertions canoniques sans décision explicite.

---

## Included orientation from `docs/04_CANONICAL_DERIVED.md`

# Canonique et dérivé — Kristal-Cybersecurity

## Canon 3.2.2

`canon/domain/legacy-v6-state.payload.json` est un adaptateur lossless du payload du Logical Artifact historique `urn:kristal:cybersecurity:canonical-state`.

`canon/state.index.json` lie le contenu à son contrat, son scope, son authority_ref et au calcul `compute-json-jcs`.

## Legacy / matérialisation

Les répertoires `knowledge-base/` originaux ne sont ni écrasés ni désactivés. Le manifest d’origine `.kristal/v9/materialization-manifest.json` enregistre `kristal.materialization/native-blob/1` et les blobs immuables référencés. La couche 3.2.2 génère en plus `inline-json/1`; elle **ne remplace pas** le manifest d’origine, ni ne réclame une factorisation non construite.

Les projections historiques sous `knowledge-base/corpus/` et les index `.kristal/v8/` restent disponibles.
