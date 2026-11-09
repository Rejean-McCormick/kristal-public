# Modèle natif

- **Kind** : `stratigraphic_process_event_temporal_graph`
- **Description** : Matière, processus, structure, enregistrement stratigraphique et événement géologique.
- **Axes et coordonnées** : Matière, processus, structure, stratigraphie, temps et événements.
- **Invariant** : Processus ≠ événement; temps géologique ≠ unité rocheuse; discordance ≠ couche déposée.

## Canal canonique de migration

Le Logical Artifact `urn:kristal:geology:canonical` possède le contrat `kristal.v6-state-reference/1.0`. Son payload authoring se trouve dans `canon/domain/geology.logical-payload.json` et est recalculé sans commitment `precomputed`.

Les modèles métier historiques sont dans `knowledge-base/` : leur forme native demeure autoritaire pour l'interprétation ; la seule enveloppe 3.2.2 ne redéfinit pas les sémantiques.
