# AI Context — Medicine

This is a deterministic, derived orientation document for offline AI reading. It is not the canon.

- State ref: `urn:kristal:state:medicine`
- State Logical Commitment: `sha256:3672a6d0df71b739fe81ef871439e0eb4fb39009be53521e359bf5620bd15e49`
- Workspace profile: `layered`
- Native model: `clinical_state_evidence_reference_graph`
- Canonical artifacts: `13`
- Sources: `19`
- External pinned references: `0`
- Materialization manifests: `0`
- Workspace-local materialization blobs: `0`

## Reading rule

Treat `canon/` and the exact `state/state-snapshot.json` as the semantic basis. Treat `ai/` as derived navigation. Use `sources/` for provenance. Materialization manifests describe physical representations and may point to local or external bytes without changing semantic identity. Do not require GitHub or any executable tool to read this package.

---

## Included orientation from `docs/00_INTENT_AND_SCOPE.md`

# Intention et portée — Kristal-Medicine

Ce Kristal est un corpus de référence statique sur : **Référence, anomalie, syndrome, diagnostic, intervention, résultat et incertitude clinique**. La mise à niveau 3.2.2 est additive et préserve la connaissance canonique engagée et le format portable v6 historique.

L'ancienne couche v9, le corpus de connaissance et les read models v8 restent intacts. Cette mise à jour crée un espace de travail 3.2.2 pour vérifier et reconstruire l'engagement logique v9 sans retoucher l'identité.

L'index de collection est produit séparément et n'appartient pas aux commitments des enfants.

---

## Included orientation from `docs/01_SEMANTIC_BOUNDARY.md`

# Frontière sémantique — Kristal-Medicine

## Subject

Référence, anomalie, syndrome, diagnostic, intervention, résultat et incertitude clinique

## Possession locale

Le domaine des assertions du Logical Artifact `urn:kristal:medicine:artifact:canonical-knowledge` ; ses distinctions, son applicabilité, ses références et leurs contextes.

## Ne possède pas

N’est ni un système de décision clinique, ni un catalogue de prescriptions, ni un outil de triage, ni un conseil médical individualisé. Ne possède pas les référentiels externes ni leur cycle de publication.

## Invariant et scope

Anomalie ≠ diagnostic ; résultat de test ≠ certitude ; intervention ≠ résultat garanti ; la chaîne est navigation, non protocole obligatoire.

`state_ref`: `urn:kristal:state:medicine`. Scope v9 repris tel quel pour préserver le State Commitment : `{"domain": "medicine", "subdomain": "clinical-state-model", "language": "fr"}`.

---

## Included orientation from `docs/02_NATIVE_MODEL.md`

# Forme native — Kristal-Medicine

**Type de forme découvert :** `clinical_state_evidence_reference_graph`. Cette désignation est descriptive dans l'enveloppe d'authoring, elle ne remplace pas le contrat de l'artefact historique.

**Axes utiles :** référence, anomalie, syndrome, diagnostic, intervention, suivi, résultat.

**Invariant :** Anomalie ≠ diagnostic ; résultat de test ≠ certitude ; intervention ≠ résultat garanti ; la chaîne est navigation, non protocole obligatoire.

Le payload logique historique est un **état portable v6** avec assertions atomiques, provenance, applicabilité et extensions de domaine. Il est engagé en v9 sous le contrat `kristal.compat/v6-portable-state-logical-projection/1.0`.

Les schémas métier sous `knowledge-base/` sont conservés ; aucun schéma graphique universel n'est imposé par la normalisation.

---

## Included orientation from `docs/03_EPISTEMIC_MODEL.md`

# Épistémologie et autorité — Kristal-Medicine

Le Kristal conserve les `source_refs`, la provenance et les statuts épistémiques exactement comme dans le corpus d'origine. Une référence source n'est pas automatiquement une preuve ni une autorité unique.

Les divergences de sources doivent rester explicites et ne pas être remplacées silencieusement par un résumé. Les sorties IA ne sont pas promues en faits par défaut.

Le catalogue normalisé `sources/source-catalog.json` comprend 19 références, dont 0 notices avec identifiant seul. Ces notices incomplètes ne constituent pas une vérification externe des sources.

Anomalie ≠ diagnostic ; résultat de test ≠ certitude ; intervention ≠ résultat garanti ; la chaîne est navigation, non protocole obligatoire.

---

## Included orientation from `docs/04_CANONICAL_DERIVED.md`

# Canonique, projections et matérialisations — Kristal-Medicine

## Représentation authoring v9

Le fichier `canon/domain/legacy-v6-logical-payload.json` est la représentation JSON du payload logique engagé par `.kristal/v9/artifact.json` ; `canon/state.index.json` enregistre son `compute-json-jcs`. Le corpus v6 et les sources historiques restent des témoins canoniques hérités, préservés octet pour octet. Une nouvelle édition doit synchroniser la provenance et le canon plutôt que créer deux autorités contradictoires.

## Représentations physiques

La matérialisation existante `.kristal/v9/materialization.json` utilise le profil `kristal.materialization/kristal-state-v6/1`, avec 1 segment(s), aucune factorisation ou segmentation supplémentaire déclarée. Ses blobs pointent dans `knowledge-base/corpus/`.

Le kit produit sa matérialisation `inline-json/1` pendant `build-v9`, puis `tools/register_legacy_materialization.py` vérifie et enregistre la représentation v6 existante dans le build et ajuste les capabilities aux profils réellement présents.

Ni réplication des assertions en dimensions artificielles, ni faux `factorization=true`. Une compression/changement de layout peut être introduit plus tard uniquement avec reconstruction logique vérifiée.
