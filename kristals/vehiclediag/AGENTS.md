# AGENTS — Kristal-VehiculeDiag

## Règles de maintenance

1. Préserver le modèle causal multiplexe natif; ne pas le réduire à une table `symptôme → pièce` ni à une liste universelle d’assertions.
2. `knowledge-base/sources/**` est la couche éditoriale autoritaire. Les fichiers `knowledge-base/corpus/**`, `.kristal/v8/**`, `.kristal/v9/**`, `build/**`, `runtime/**` et `projections/materialized/**` sont reconstructibles.
3. Les payloads `canon/domain/reference-model.json` et `canon/epistemic/epistemic-overlay.json` sont les formes logiques state-bearing utilisées par le workspace 3.2.2. Ils doivent rester reproductibles depuis les sources par les outils métier.
4. Toute donnée spécifique à un véhicule réel doit porter applicabilité et provenance. Les données de démonstration ne doivent jamais être présentées comme OEM.
5. Les postérieurs, rankings, plans de tests, scores de fermeture et priors appris restent des projections; ils ne deviennent pas canoniques sans décision explicite de modèle.
6. Séparer provenance épistémique et provenance de build.
7. Les sorties IA restent des propositions jusqu’à validation explicite.
8. Avant toute publication : exécuter le build métier, les tests métier, `kristal.py check`, puis `kristal.py build-v9`; qualifier indépendamment avant publication.
9. Ne pas publier ni activer automatiquement un état lors d’une simple normalisation locale.
