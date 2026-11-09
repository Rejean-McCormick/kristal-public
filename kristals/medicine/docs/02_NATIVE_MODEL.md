# Forme native — Kristal-Medicine

**Type de forme découvert :** `clinical_state_evidence_reference_graph`. Cette désignation est descriptive dans l'enveloppe d'authoring, elle ne remplace pas le contrat de l'artefact historique.

**Axes utiles :** référence, anomalie, syndrome, diagnostic, intervention, suivi, résultat.

**Invariant :** Anomalie ≠ diagnostic ; résultat de test ≠ certitude ; intervention ≠ résultat garanti ; la chaîne est navigation, non protocole obligatoire.

Le payload logique historique est un **état portable v6** avec assertions atomiques, provenance, applicabilité et extensions de domaine. Il est engagé en v9 sous le contrat `kristal.compat/v6-portable-state-logical-projection/1.0`.

Les schémas métier sous `knowledge-base/` sont conservés ; aucun schéma graphique universel n'est imposé par la normalisation.
