# Modèle natif

- **Kind** : `spatial_relation_and_scale_graph`
- **Description** : Entités spatiales, lieux, géométries, régions, relations, distributions, réseaux et échelles.
- **Axes et coordonnées** : CRS, relations spatiales, territoire, échelle, résolution, distribution et flux.
- **Invariant** : La géométrie ne détermine pas l’identité; un tracé ne décide ni souveraineté ni légitimité.

## Canal canonique de migration

Le Logical Artifact `urn:kristal:geographyspace:canonical` possède le contrat `kristal.v6-state-reference/1.0`. Son payload authoring se trouve dans `canon/domain/geographyspace.logical-payload.json` et est recalculé sans commitment `precomputed`.

Les modèles métier historiques sont dans `knowledge-base/` : leur forme native demeure autoritaire pour l'interprétation ; la seule enveloppe 3.2.2 ne redéfinit pas les sémantiques.
