# AI Context — Literature

This is a deterministic, derived orientation document for offline AI reading. It is not the canon.

- State ref: `urn:kristal:state:literature`
- State Logical Commitment: `sha256:49f22ae05a0fc779b2fd6d35b3ec44701ad251f08e0c0d24fb58a721d95c14cb`
- Workspace profile: `layered`
- Native model: `typed_bibliographic_interpretive_graph`
- Canonical artifacts: `12`
- Sources: `9`
- External pinned references: `0`
- Materialization manifests: `0`
- Workspace-local materialization blobs: `0`

## Reading rule

Treat `canon/` and the exact `state/state-snapshot.json` as the semantic basis. Treat `ai/` as derived navigation. Use `sources/` for provenance. Materialization manifests describe physical representations and may point to local or external bytes without changing semantic identity. Do not require GitHub or any executable tool to read this package.

---

## Included orientation from `docs/00_INTENT_AND_SCOPE.md`

# Intention et portée — Kristal-Literature

Ce Kristal est un corpus de référence statique sur : **Œuvre, texte, forme, thème, contexte et réception littéraire**. La mise à niveau 3.2.2 est additive et préserve la connaissance canonique engagée et le format portable v6 historique.

L'ancienne couche v9, le corpus de connaissance et les read models v8 restent intacts. Cette mise à jour crée un espace de travail 3.2.2 pour vérifier et reconstruire l'engagement logique v9 sans retoucher l'identité.

L'index de collection est produit séparément et n'appartient pas aux commitments des enfants.

---

## Included orientation from `docs/01_SEMANTIC_BOUNDARY.md`

# Frontière sémantique — Kristal-Literature

## Subject

Œuvre, texte, forme, thème, contexte et réception littéraire

## Possession locale

Le domaine des assertions du Logical Artifact `urn:kristal:literature:artifact:canonical-knowledge` ; ses distinctions, son applicabilité, ses références et leurs contextes.

## Ne possède pas

N’embarque pas de textes littéraires complets et ne transforme pas l’interprétation en fait intrinsèque. Ne possède pas les référentiels externes ni leur cycle de publication.

## Invariant et scope

work ≠ expression ≠ manifestation ≠ item ; œuvre ≠ témoin ; auteur ≠ narrateur ≠ locuteur ; réception ≠ qualité intrinsèque.

`state_ref`: `urn:kristal:state:literature`. Scope v9 repris tel quel pour préserver le State Commitment : `{"domain": "literature", "subdomain": "work_text_form_theme_context_reception", "language": "fr"}`.

---

## Included orientation from `docs/02_NATIVE_MODEL.md`

# Forme native — Kristal-Literature

**Type de forme découvert :** `typed_bibliographic_interpretive_graph`. Cette désignation est descriptive dans l'enveloppe d'authoring, elle ne remplace pas le contrat de l'artefact historique.

**Axes utiles :** œuvre, texte, forme et genre, thème, contexte, réception.

**Invariant :** work ≠ expression ≠ manifestation ≠ item ; œuvre ≠ témoin ; auteur ≠ narrateur ≠ locuteur ; réception ≠ qualité intrinsèque.

Le payload logique historique est un **état portable v6** avec assertions atomiques, provenance, applicabilité et extensions de domaine. Il est engagé en v9 sous le contrat `kristal.compat/v6-portable-state-logical-projection/1.0`.

Les schémas métier sous `knowledge-base/` sont conservés ; aucun schéma graphique universel n'est imposé par la normalisation.

---

## Included orientation from `docs/03_EPISTEMIC_MODEL.md`

# Épistémologie et autorité — Kristal-Literature

Le Kristal conserve les `source_refs`, la provenance et les statuts épistémiques exactement comme dans le corpus d'origine. Une référence source n'est pas automatiquement une preuve ni une autorité unique.

Les divergences de sources doivent rester explicites et ne pas être remplacées silencieusement par un résumé. Les sorties IA ne sont pas promues en faits par défaut.

Le catalogue normalisé `sources/source-catalog.json` comprend 9 références, dont 0 notices avec identifiant seul. Ces notices incomplètes ne constituent pas une vérification externe des sources.

work ≠ expression ≠ manifestation ≠ item ; œuvre ≠ témoin ; auteur ≠ narrateur ≠ locuteur ; réception ≠ qualité intrinsèque.

---

## Included orientation from `docs/04_CANONICAL_DERIVED.md`

# Canonique, projections et matérialisations — Kristal-Literature

## Représentation authoring v9

Le fichier `canon/domain/legacy-v6-logical-payload.json` est la représentation JSON du payload logique engagé par `.kristal/v9/artifact.json` ; `canon/state.index.json` enregistre son `compute-json-jcs`. Le corpus v6 et les sources historiques restent des témoins canoniques hérités, préservés octet pour octet. Une nouvelle édition doit synchroniser la provenance et le canon plutôt que créer deux autorités contradictoires.

## Représentations physiques

La matérialisation existante `.kristal/v9/materialization.json` utilise le profil `kristal.materialization/kristal-state-v6/1`, avec 1 segment(s), aucune factorisation ou segmentation supplémentaire déclarée. Ses blobs pointent dans `knowledge-base/corpus/`.

Le kit produit sa matérialisation `inline-json/1` pendant `build-v9`, puis `tools/register_legacy_materialization.py` vérifie et enregistre la représentation v6 existante dans le build et ajuste les capabilities aux profils réellement présents.

Ni réplication des assertions en dimensions artificielles, ni faux `factorization=true`. Une compression/changement de layout peut être introduit plus tard uniquement avec reconstruction logique vérifiée.
