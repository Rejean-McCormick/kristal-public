# Canonique et dérivé

## Source de vérité v9

Le Logical Artifact autoritatif est le `structured_epistemic_state/5.0` situé historiquement à `knowledge-base/corpus/power-topology.structured-epistemic-state.json`. Son emplacement historique est conservé pour éviter une relocalisation ou duplication sémantiquement inutile.

## Logical Artifact canonique

`canon/state.index.json` enregistre l'Artifact ID `urn:kristal:power:canonical-state`, son contrat logique, son scope et son autorité. Le commitment est calculé par JCS + SHA-256 selon `kristal.logical/jcs-sha256-v1`.

## Inputs d'authoring et reconstruction

Les couches sous `knowledge-base/sources/`, les schémas et les règles de build constituent les entrées de reconstruction du corpus. Le validateur du domaine vérifie notamment résolution référentielle, provenance, intégrité du manifeste et rebuild déterministe.

## Artefacts dérivés / runtime

Sont dérivés ou opérationnels : `.kristal/v8`, `.kristal/v9`, `build/`, `state/`, `runtime/`, `projections/materialized/`, `local-corpus-index`, `knowledge-base/corpus/index.json` et `knowledge-base/corpus/evidence-links.json`.

`corpus-indexer/` est un outil/sidecar et non une seconde autorité sémantique.

## Materializations

Le paquet `.kristal/v9` préexistant matérialise le même membre logique et lie le blob canonique historique. La nouvelle sortie `build/v9` sert de candidat reproductible Local Kristal 3.2.2 ; elle ne devient publiée ou active que par des étapes distinctes.
