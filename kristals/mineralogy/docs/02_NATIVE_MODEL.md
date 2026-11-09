# Modèle natif — Kristal-Mineralogy

**Kind local** : `composition_structure_property_occurrence_graph`.

**Géométrie conservée** : composition chimique + structure cristalline → identité minérale → propriétés → occurrences.

**Invariant essentiel** : la composition et la structure ne doivent pas être confondues ; les contextes d’occurrence sont distincts de l’identité.

Le contrat engagé par le v9 historique reste `kristal_state.hash_target/6.0`. Ce contrat est un `kristal_state` v6 matérialisé en assertions atomiques avec informations de provenance. Cette migration ne convertit pas ce graphe en ontologie uniforme, en table ou en pipeline artificiel.

La vue authoring `canon/domain/legacy-v6-state.payload.json` est une photographie canonique du payload existant. Les fichiers du domaine dans `knowledge-base` restent inchangés. Le maintien en synchronisation future de ces deux sources exige une procédure éditoriale explicite.
