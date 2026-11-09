# Canonique, projections et matérialisations — Kristal-Materials

## Représentation authoring v9

Le fichier `canon/domain/legacy-v6-logical-payload.json` est la représentation JSON du payload logique engagé par `.kristal/v9/artifact.json` ; `canon/state.index.json` enregistre son `compute-json-jcs`. Le corpus v6 et les sources historiques restent des témoins canoniques hérités, préservés octet pour octet. Une nouvelle édition doit synchroniser la provenance et le canon plutôt que créer deux autorités contradictoires.

## Représentations physiques

La matérialisation existante `.kristal/v9/materialization.json` utilise le profil `kristal.materialization/kristal-state-v6/1`, avec 1 segment(s), aucune factorisation ou segmentation supplémentaire déclarée. Ses blobs pointent dans `knowledge-base/corpus/`.

Le kit produit sa matérialisation `inline-json/1` pendant `build-v9`, puis `tools/register_legacy_materialization.py` vérifie et enregistre la représentation v6 existante dans le build et ajuste les capabilities aux profils réellement présents.

Ni réplication des assertions en dimensions artificielles, ni faux `factorization=true`. Une compression/changement de layout peut être introduit plus tard uniquement avec reconstruction logique vérifiée.
