# Modèle natif

## Primitives du domaine

Le document natif combine `source_refs`, assertions, provenance, reader policies, portée/applicabilité, valuations épistémiques, relations et extensions métier.

Familles déclarées dans le corpus : 447 termes de glossaire, 62 ressources, 5 voies judiciaires, 4 modèles/axes d’état, 14 transitions judiciaires et 6 relations épistémiques.

## Forme retenue

`structured_epistemic_state/5.0` est conservé comme forme native. Il s’agit d’un document d’état épistémique structuré, riche en assertions adressables et en métadonnées de provenance; il ne doit pas être aplati en une topologie universelle.

## Logical Contract v9

- Artifact ID : `urn:kristal:policeops:artifact:native-canon`
- Contract : `policeops.structured-epistemic-state/5.0`
- Commitment : `kristal.logical/jcs-sha256-v1` conservé en mode `precomputed` depuis le build v9 PoliceOps vérifié. Le build historique applique la `hash_target_policy` native et exclut les champs auto-référentiels (`state_id`, `content_hash`, `signatures`) avant engagement logique; le Local Kit générique ne doit pas redéfinir cette identité.

## Compatibilité

La projection v6 sous `.kristal/v8/` et les indexes v8 sont dérivés/rebuildables. Le build v9 legacy sous `.kristal/v9/` est conservé comme trace de migration mais n’est plus l’enveloppe d’authoring courante.
