# Modèle natif — Kristal-Botany

**Kind local** : `land_plant_architecture_function_graph`.

**Géométrie conservée** : architecture des Embryophyta : organes, tissus, fonctions, croissance, reproduction, taxonomie et réponses à l’environnement.

**Invariant essentiel** : les relations d’organes, cycles et fonctions végétales ne remplacent pas la taxonomie ou les interactions écologiques.

Le contrat engagé par le v9 historique reste `kristal.compat.v6-state-logical/1.0`. Ce contrat utilise le payload d'origine engagé dans v9 (corpus sémantique natif pour Catho ; `kristal_state` v6 pour les autres), avec les informations de provenance existantes. Cette migration ne convertit pas ce graphe en ontologie uniforme, en table ou en pipeline artificiel.

La vue authoring `canon/domain/legacy-v6-state.payload.json` est une photographie canonique du payload existant. Les fichiers du domaine dans `knowledge-base` restent inchangés. Le maintien en synchronisation future de ces deux sources exige une procédure éditoriale explicite.
