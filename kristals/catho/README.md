> **Mise à jour v11 (migration structurelle)** : [lire `README_V11.md`](README_V11.md). Nouveaux KQ/KP/KA/KS, dictionnaires multilingues, correspondances Wikidata sous revue. Les versions v8/v9 sont conservées et non réécrites.

# Kristal Catho — paquet organisé

Ce paquet regroupe le corpus canonique et les documents de stratégie dans une structure unique, sans numéro de version dans les noms de dossiers.

## Structure

- `knowledge-base/` — corpus canonique, source éditoriale, documentation, schémas et outils de validation.
- `project-strategy/` — stratégie interne, conception produit, matériel de diffusion et documents de livraison.
- `CLEANUP-REPORT.md` — résumé des opérations de consolidation et de validation.

Les numéros d’édition ou de format utiles à la compatibilité sont conservés uniquement dans les fichiers de métadonnées et le contenu documentaire.


## Extension figures catholiques (13 octobre 2026)

Le second artefact canonique `canon/domain/personnes-reconnaissances.json` fournit les 38 docteurs de l'Église, les 267 lignes de pontificats du Vatican (265 personnes uniques), ainsi que les répertoires de la Commission théologique internationale, de l'Académie pontificale de Saint-Thomas-d'Aquin et des prix Ratzinger. Les catégories sont explicites et **cumulables** ; chacune est accompagnée de sa source et éventuellement de son année/mandat/section. La religion ne se déduit pas du fait d'avoir été distingué par le Vatican. L'ancienne base doctrinale reste inchangée.

- [Guide d'utilisation et réserves](knowledge-base/exports/README-personnes.md)
- [CSV des personnes et tags](knowledge-base/exports/personnes-tags.csv)
- [Requête CLI](knowledge-base/tools/query_personnes.py)
- [Validation spécialisée](knowledge-base/tools/validate_people.py)

Cette édition est au stade `building` du framework : vérifications mécaniques effectuées, qualification indépendante non revendiquée.


## Semantic Links and offline graph reader (2026-10-15)

Six v9 Logical Artifacts are now registered. See [Semantic Links architecture and validation](docs/CATHO_SEMANTIC_LINKS_MEGA.md) for attributed Wikidata P50 claim pointers, 99 historic themes, institutional source connections, and explicitly unresolved identity research. The standalone offline explorer is `derived/catho-graph/explorer.html`. Skope itself is unchanged; this reader is derived and noncanonical.


## Compatibilité locale Kristal v10 — 16 octobre 2026

La v10 du Framework ajoute l'hébergement et le réseau ; le contenu sémantique de Catho reste un **état v9 à six artefacts**, sans changement d'identité ni des engagements. Cette archive restaure le dossier candidat `build/v9/`, met à jour l'outil local vers l'Authoring Kit 3.3.1 et régénère les métadonnées Discovery et la surface de lecture dérivée.

Pour le contrôle local : `python tools/kristal.py audit-discovery . --require-fresh`. Pour les étapes v10 qui nécessitent une autorisation humaine et une qualification indépendante, voir [Hébergement et publication](docs/07_HOSTING_AND_PUBLICATION.md). Aucun hébergement, publication ni activation v10 n'est revendiqué.
