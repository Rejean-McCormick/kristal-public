# Modèle natif — Kristal-Biodiversity

**Kind local** : `taxon_space_time_evidence_observation_graph`.

**Géométrie conservée** : taxon concept × spatial support × temporal support × evidence/provenance → occurrence, abondance, diversité, évaluation de menace.

**Invariant essentiel** : non-détection ≠ absence ; occurrence ≠ aire de répartition ; une catégorie de menace est contextualisée et datée.

Le contrat engagé par le v9 historique reste `kristal.compat.v6-state-logical/1.0`. Ce contrat utilise le payload d'origine engagé dans v9 (corpus sémantique natif pour Catho ; `kristal_state` v6 pour les autres), avec les informations de provenance existantes. Cette migration ne convertit pas ce graphe en ontologie uniforme, en table ou en pipeline artificiel.

La vue authoring `canon/domain/legacy-v6-state.payload.json` est une photographie canonique du payload existant. Les fichiers du domaine dans `knowledge-base` restent inchangés. Le maintien en synchronisation future de ces deux sources exige une procédure éditoriale explicite.
