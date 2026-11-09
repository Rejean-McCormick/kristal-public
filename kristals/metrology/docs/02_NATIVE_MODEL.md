# Modèle natif — Kristal-Metrology

**Kind local** : `metrological_traceability_relation_graph`.

**Géométrie conservée** : grandeur → unité → instrument ou système → mesure → incertitude → traçabilité.

**Invariant essentiel** : valeur mesurée ≠ valeur vraie ; erreur ≠ incertitude ; étalonnage ≠ ajustage.

Le contrat engagé par le v9 historique reste `kristal_state.hash_target/6.0`. Ce contrat est un `kristal_state` v6 matérialisé en assertions atomiques avec informations de provenance. Cette migration ne convertit pas ce graphe en ontologie uniforme, en table ou en pipeline artificiel.

La vue authoring `canon/domain/legacy-v6-state.payload.json` est une photographie canonique du payload existant. Les fichiers du domaine dans `knowledge-base` restent inchangés. Le maintien en synchronisation future de ces deux sources exige une procédure éditoriale explicite.
