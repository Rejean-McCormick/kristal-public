# Modèle natif — Kristal-ControlSystems

**Kind local** : `feedback_control_loop_signal_architecture_graph`.

**Géométrie conservée** : consigne → système → mesure → erreur → correction, incluant contrôleur, actionneur, observateur et rétroaction.

**Invariant essentiel** : rétroaction ≠ stabilisation garantie ; système physique ≠ modèle ≠ mesure ≠ perturbation ≠ loi de commande.

Le contrat engagé par le v9 historique reste `kristal.compat.v6-state-logical/1.0`. Ce contrat utilise le payload d'origine engagé dans v9 (corpus sémantique natif pour Catho ; `kristal_state` v6 pour les autres), avec les informations de provenance existantes. Cette migration ne convertit pas ce graphe en ontologie uniforme, en table ou en pipeline artificiel.

La vue authoring `canon/domain/legacy-v6-state.payload.json` est une photographie canonique du payload existant. Les fichiers du domaine dans `knowledge-base` restent inchangés. Le maintien en synchronisation future de ces deux sources exige une procédure éditoriale explicite.
