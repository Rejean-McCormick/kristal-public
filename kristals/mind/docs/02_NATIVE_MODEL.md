# Modèle natif — Kristal-Mind

**Kind local** : `recurrent_cognitive_process_graph`.

**Géométrie conservée** : perception → représentation → mémoire → décision → action, avec boucles de rétroaction.

**Invariant essentiel** : cette flèche décrit la navigation et non un traitement cérébral strictement sériel ; attention et contrôle sont transversaux.

Le contrat engagé par le v9 historique reste `kristal_state.hash_target/6.0`. Ce contrat est un `kristal_state` v6 matérialisé en assertions atomiques avec informations de provenance. Cette migration ne convertit pas ce graphe en ontologie uniforme, en table ou en pipeline artificiel.

La vue authoring `canon/domain/legacy-v6-state.payload.json` est une photographie canonique du payload existant. Les fichiers du domaine dans `knowledge-base` restent inchangés. Le maintien en synchronisation future de ces deux sources exige une procédure éditoriale explicite.
