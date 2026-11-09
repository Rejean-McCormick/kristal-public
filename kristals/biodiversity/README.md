# Kristal-Biodiversity v0.1.0

Corpus statique validé sur **taxons × espace × temps** : présence, absence contextualisée, abondance, diversité et menace.

## Principe

Le Kristal prend comme unité minimale :

`taxon concept + spatial support + temporal support + evidence/provenance`

Puis il distingue quatre familles d'objets :

`occurrence → abundance → diversity/community → threat assessment`

Une non-détection n'est pas automatiquement une absence. Une occurrence n'est pas une aire de répartition. Une abondance sans unité/protocole n'est pas directement comparable. Une catégorie de menace est une **évaluation datée et scoped**, pas une propriété intemporelle d'un nom d'espèce.

## Seed v0.1.0

- 6 concepts taxonomiques / scopes
- 7 unités ou supports spatiaux
- 6 supports temporels
- 5 événements/protocoles d'échantillonnage
- 4 patrons/occurrences de présence-absence
- 5 objets d'abondance
- 5 objets de diversité/composition
- 9 catégories IUCN
- 2 patrons/évaluations de menace
- 4 objets de menace
- 12 relations explicites
- 287 assertions Kristal v6
- 12 sources/standards institutionnels

Le seed s'aligne sur Darwin Core/TDWG pour l'occurrence, GBIF pour les données d'occurrence et d'événement d'échantillonnage, GEO BON pour distribution/abondance/diversité, et IUCN pour les évaluations de risque d'extinction.

## État canonique

`knowledge-base/corpus/biodiversity.kristal-state.json`

## Limites

Le corpus ne constitue pas un atlas mondial et n'ingère aucun flux vivant. Les exemples normatifs sont explicitement marqués comme tels. L'exemple *Panthera tigris* est conservé comme **fiche IUCN archivée**, donc comme état historique de source et non comme prétention sur le statut le plus récent.

## Validation

```bash
python knowledge-base/tools/validate.py
```
