# AI Context — Pouvoirs-Australie

This is a deterministic, derived orientation document for offline AI reading. It is not the canon.

- State ref: `urn:kristal:state:pouvoirs-australie`
- State Logical Commitment: `sha256:fa3e5f53d784509e2c146ad2c823e6faab750b8ea6e16a019ac4454ae5fd84e5`
- Workspace profile: `layered`
- Native model: `jurisdictional_legal_power_relational_graph`
- Canonical artifacts: `1`
- Sources: `23`
- External pinned references: `0`
- Materialization manifests: `0`
- Workspace-local materialization blobs: `0`

## Reading rule

Treat `canon/` and the exact `state/state-snapshot.json` as the semantic basis. Treat `ai/` as derived navigation. Use `sources/` for provenance. Materialization manifests describe physical representations and may point to local or external bytes without changing semantic identity. Do not require GitHub or any executable tool to read this package.

---

## Included orientation from `docs/00_INTENT_AND_SCOPE.md`

# Intentions et périmètre — Kristal-Pouvoirs-Australie

Le Kristal traite **qui décide quoi**, la compétence juridique, les limites, les délégations, la responsabilité et les contrôles dans l’ordre interne de **Commonwealth of Australia**.

Le périmètre original et ses exclusions sont dans `README.md`. La migration 3.2.2 n'étend ni n’actualise le contenu juridique. Date indiquée dans le catalogue de source : **2026-10-02** (n'est pas une validation juridique au 7 octobre 2026).

Identité v9 historique : `urn:kristal:state:pouvoirs-australie`.

---

## Included orientation from `docs/01_SEMANTIC_BOUNDARY.md`

# Frontière sémantique — Kristal-Pouvoirs-Australie

**Domaine / juridiction** : `mécanismes légaux de pouvoir` / `Commonwealth of Australia`.

Le corpus distingue les institutions/charges, leurs habilitations, la validité des actes, les limitations et les contrôles. Il ne résume pas une compétence de droit à une simple influence politique.

**Interface extérieure** : le droit international substantiel et le droit matériel de l’Union européenne sont exclus, sauf les mécanismes juridiques internes de réception/ratification/préparation lorsque le corpus original les traite.

**Limites propres à cette juridiction** : voir `knowledge-base/documentation/INVARIANTS.md`, `knowledge-base/documentation/DOMAIN_MODEL.md` et `README.md`, qui conservent leurs formulations originales.

---

## Included orientation from `docs/02_NATIVE_MODEL.md`

# Modèle natif — Kristal-Pouvoirs-Australie

Type déclaratif : `jurisdictional_legal_power_relational_graph`.

Le modèle encode des **assertions sourcées** portant sur les institutions, fonctions, instruments, compétences et mécanismes de contrôle. Les coordonnées de juridiction, domaine d'application, date et provenance demeurent distinctes des identités.

Logical Contract conservé : `kristal.compat.v6-state-logical/1.0`.

Source du membre logique : `canon/domain/jurisdictional-power.payload.json` ; original inchangé : `.kristal/v9/logical-artifact.json`.

Les ontologies et distinctions détaillées sont **celles du modèle natif** documenté dans `knowledge-base/documentation/DOMAIN_MODEL.md` et non une nouvelle ontologie globale inventée par l'enveloppe 3.2.2.

---

## Included orientation from `docs/03_EPISTEMIC_MODEL.md`

# Provenance et autorité — Kristal-Pouvoirs-Australie

Les **23 entrées** du catalogue original sont conservées sous `knowledge-base/sources/source_catalog.json`. `sources/source-catalog.json` donne une vue structurée 3.2.2, sans trancher le degré d'autorité des pièces.

Une source officielle fournit une provenance ou une preuve, mais une compétence juridique est toujours soumise à l'interprétation du texte applicable, à l'ordre juridique et à sa date. Ne jamais présenter une réponse générée ou une source hors contexte comme autorité automatiquement validée.

Le statut temporel de référence est celui des données ; la migration ne revérifie pas les sources sur le Web.

---

## Included orientation from `docs/04_CANONICAL_DERIVED.md`

# Canon et dérivés — Kristal-Pouvoirs-Australie

**Canon authoring** : `canon/state.index.json` et `canon/domain/jurisdictional-power.payload.json`. Le payload du membre v9 est copié exactement et ses engagements sont recalculés par JCS-SHA256.

**Canon juridique historique conservé** : `knowledge-base/corpus/*.kristal-state.json` et `knowledge-base/sources/`. Ces fichiers ont un statut de source native, pas de simple cache.

**Représentation historique** : `.kristal/v9/` est gardé intact. La matérialisation de profil `kristal.materialization/kristal-state-v6/1` référence son blob existant sous `.kristal/v8/`.

**Dérivés** : `.kristal/v8/index`, autres read models v8, `build/v9`, runtime, projections produites, release. Une nouvelle matérialisation ne doit pas changer le Logical Commitment.
