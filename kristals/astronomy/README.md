# Kristal-Astronomy

**Version:** 1.0.0  
**Édition:** 2026-10-02  
**Format canonique:** Kristal Standard 6.0 (`kristal_state`)

Kristal-Astronomy est un corpus statique, traçable et orienté IA sur les **objets célestes et leur observation**.

## Axe conceptuel

Le noyau suit huit axes :

`type → masse → distance → mouvement → rayonnement → formation → évolution → observation`

L’ajout de `observation` est intentionnel : en astronomie, de nombreuses propriétés sont inférées à partir d’un signal, d’un modèle, d’un référentiel et d’une époque. Le corpus refuse donc les « nombres nus » lorsque le contexte affecte le sens.

## Contenu de cette édition

- taxonomie large : étoiles, rémanents, trous noirs, corps planétaires, petits corps, objets diffus, amas, galaxies;
- snapshot de référence du Système solaire : Soleil, 8 planètes, Lune, Pluton;
- modèle de mesure : unité, méthode, incertitude/limite, époque, référentiel, bande passante;
- observation : astrométrie, parallaxe, mouvement propre, vitesse radiale, photométrie, spectroscopie, transit, imagerie directe, occultation, interférométrie, radio, X/gamma, ondes gravitationnelles, neutrinos;
- formation et évolution : graphe stellaire conditionnel et mécanismes galactiques de haut niveau;
- sources externes : NASA, ESA/Gaia, IAU, CDS/SIMBAD, NASA Exoplanet Archive.

## Frontière

Cette édition ne cherche pas à recopier des catalogues vivants. Gaia, SIMBAD et l’Exoplanet Archive sont des **sources externes versionnables**. Une future ingestion doit produire un snapshot explicite avec date/version/provenance.

Elle ne remplace pas non plus :
- un moteur d’éphémérides;
- un catalogue de transitoires en temps réel;
- un modèle cosmologique;
- Kristal-Physics pour les lois fondamentales;
- Kristal-Chemistry pour la microphysique/composition détaillée.

## Fichiers centraux

- `knowledge-base/corpus/astronomy.kristal-state.json` — état canonique v6;
- `knowledge-base/corpus/astronomy.referent-registry.json` — identités stables;
- `knowledge-base/corpus/domain-coverage.json` — couverture et limites;
- `knowledge-base/sources/measurement_model.json` — sémantique des mesures;
- `knowledge-base/sources/observation_methods.json` — méthodes d’observation;
- `external-source-library/source-store.json` — catalogue de provenance;
- `validation/astronomy-validation-report.json` — validation technique et éditoriale.

## Statut de validation

`reference` signifie ici : schéma valide, références internes cohérentes, mesures sélectionnées traçables à des sources déclarées et règles de représentation vérifiées. Cela **ne constitue pas une reconnaissance officielle** par la NASA, l’ESA, l’IAU, le CDS ou une autre institution.
