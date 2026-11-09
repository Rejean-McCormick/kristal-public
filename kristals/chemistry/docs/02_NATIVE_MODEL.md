# Modèle natif — Kristal-Chemistry

**Kind local** : `multiscale_epistemic_entity_state_process_graph`.

**Géométrie conservée** : ENTITY ↔ STATE ↔ PROCESS, sous conditions thermodynamiques, cinétiques et observations ; processus de réaction potentiellement cycliques.

**Invariant essentiel** : identité ≠ classification ; réaction chimique ≠ transition de phase ; propriété ≠ observation et les réactions n’imposent pas un DAG.

Le contrat engagé par le v9 historique reste `kristal.compat.v6-state-logical/1.0`. Ce contrat utilise le payload d'origine engagé dans v9 (corpus sémantique natif pour Catho ; `kristal_state` v6 pour les autres), avec les informations de provenance existantes. Cette migration ne convertit pas ce graphe en ontologie uniforme, en table ou en pipeline artificiel.

La vue authoring `canon/domain/legacy-v6-state.payload.json` est une photographie canonique du payload existant. Les fichiers du domaine dans `knowledge-base` restent inchangés. Le maintien en synchronisation future de ces deux sources exige une procédure éditoriale explicite.
