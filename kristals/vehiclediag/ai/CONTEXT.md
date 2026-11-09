# AI Context — VehiculeDiag

This is a deterministic, derived orientation document for offline AI reading. It is not the canon.

- State ref: `urn:vehiclediag:state:reference`
- State Logical Commitment: `sha256:1d35e4a939ea4ab9eb6d28cdef1cff1cf1a8a22cd9299a9417524ee28160190b`
- Workspace profile: `executable`
- Native model: `multiplex_causal_diagnostic_model`
- Canonical artifacts: `2`
- Sources: `18`
- External pinned references: `0`
- Materialization manifests: `3`
- Workspace-local materialization blobs: `3`

## Reading rule

Treat `canon/` and the exact `state/state-snapshot.json` as the semantic basis. Treat `ai/` as derived navigation. Use `sources/` for provenance. Materialization manifests describe physical representations and may point to local or external bytes without changing semantic identity. Do not require GitHub or any executable tool to read this package.

---

## Included orientation from `docs/00_INTENT_AND_SCOPE.md`

# Intention et scope

## Pourquoi ce Kristal existe

Kristal-VehiculeDiag formalise un diagnostic automobile causal, probabiliste et testable. Le véhicule est modélisé comme un réseau multiplexe de chemins fonctionnels observables plutôt que comme une table `symptôme → pièce`.

## Corpus / problème de départ

Le corpus actuel est un jeu éditorial illustratif : neuf circuits démonstrateurs, des composants et ports, des connexions, chemins fonctionnels, états opératoires, points de test, modes de panne, archétypes, symptômes, DTC génériques et règles de sécurité. Il ne contient pas de données OEM réelles.

## Résultats attendus

Le Kristal doit permettre la reconstruction déterministe du modèle de référence, des projections diagnostiques et de l’overlay épistémique, tout en conservant la distinction entre canon, projections et runtime.

---

## Included orientation from `docs/01_SEMANTIC_BOUNDARY.md`

# Frontière sémantique

## Subject / territoire

Le Subject est un modèle de référence générique de diagnostic automobile causal multiplexe : composants, ports, connexions, couches physiques/logiques, chemins fonctionnels, états opératoires, tests et perturbations de panne.

## Possède

Le Kristal possède son modèle éditorial générique, ses démonstrateurs, son modèle de panne, son modèle de mesure, ses règles de sécurité génériques et l’overlay épistémique qui décrit leur provenance/applicabilité dans l’écosystème Kristal.

## Ne possède pas

Il ne possède pas les faits OEM d’un véhicule réel, les mesures terrain non ingérées, les décisions de réparation, ni les résultats calculés comme rankings/postérieurs/plans/priors appris.

## Relations avec d’autres Kristals

Aucune référence externe pinée n’est requise dans l’état actuel. Toute future dépendance inter-Kristal devra être enregistrée avec son Logical Commitment.

## State identity v9

`state_ref = urn:vehiclediag:state:reference`. La normalisation 3.2.2 conserve ce State identity et vise à reproduire le Logical Commitment v9 déjà validé.

---

## Included orientation from `docs/02_NATIVE_MODEL.md`

# Modèle natif

## Primitives du domaine

Composants, ports/bornes, connexions, couches, chemins fonctionnels, états opératoires, dependency sets, points de test, mesures, symptômes, DTC, modes de panne et archétypes.

## Relations / transformations

Les connexions relient des ports; les chemins ordonnent des segments fonctionnels; les états opératoires activent ou désactivent des comportements; les modes de panne perturbent le graphe; les tests produisent des observations permettant de mettre à jour les hypothèses diagnostiques.

## Dimensions internes

Le modèle couvre notamment les couches électrique, masse, signal, contrôle, réseau, fluide, hydraulique, air, mécanique, thermique et fonctionnelle.

## Forme native retenue

`multiplex_causal_diagnostic_model` — graphe causal multiplexe exécutable à granularité composant/port/arête.

## Logical Contracts v9

- `vehiclediag.reference-model/3.0` : modèle métier natif normalisé.
- `kristal_state.hash_target/6.0` : overlay épistémique portable v6, dépendant du modèle de référence.

## Pourquoi cette forme ne perd pas d'information essentielle

Une réduction à une table symptôme/cause ou à une liste générique d’assertions perdrait la topologie, la granularité des ports, l’ordre des chemins, les états opératoires, les dépendances et la distinction entre couches.

## Alternatives rejetées

Le portable v6 et les indexes v8 restent des projections d’interopérabilité/lecture; ils ne remplacent pas le modèle natif.

---

## Included orientation from `docs/03_EPISTEMIC_MODEL.md`

# Modèle épistémique

## Régimes d'information

Le Kristal distingue documentation/configuration spécifique, schéma ou procédure OEM, bulletin technique, mesure réelle, cas terrain documenté, fiche fabricant, connaissance générique éditoriale et hypothèse diagnostique calculée.

## Provenance épistémique

Les données spécifiques doivent conserver applicabilité et provenance. Une mesure conserve son contexte, état opératoire, instrument, unité et date.

## Autorité

Les données livrées ici sont éditoriales et illustratives; elles ne sont pas autoritaires pour un véhicule réel. Une source réelle doit déclarer son autorité et sa portée de configuration.

## Incertitude / conflits / inconnus

Une observation ne doit pas être confondue avec la vérité cachée. Un DTC ou un symptôme ne constitue pas un diagnostic. Les cas terrain peuvent informer des priors après agrégation contrôlée mais ne réécrivent pas automatiquement la topologie de référence.

## Provenance de build

Les records de compilation et les manifests décrivent la dérivation informatique. Ils restent séparés de la provenance épistémique portée par l’overlay.

## Politique des sorties IA

Les sorties IA sont des propositions jusqu’à validation explicite et ne constituent pas une autorité diagnostique ou de sécurité.

---

## Included orientation from `docs/04_CANONICAL_DERIVED.md`

# Canonique et dérivé

## Source(s) de vérité

La couche éditoriale autoritaire est `knowledge-base/sources/**`. Le build métier normalise ces sources en un modèle logique v9.

## Logical Artifacts canoniques

Le workspace 3.2.2 enregistre deux payloads state-bearing :

- `canon/domain/reference-model.json` → `vehiclediag.reference-model/3.0`;
- `canon/epistemic/epistemic-overlay.json` → `kristal_state.hash_target/6.0`.

Ces payloads ont été extraits du build v9 métier validé et doivent rester reproductibles depuis `knowledge-base/sources/**`.

## Artefacts dérivés / Runtime

`knowledge-base/corpus/**`, `.kristal/v8/**`, `.kristal/v9/**`, `build/**`, `runtime/**`, `derived/**` et les projections matérialisées sont reconstructibles.

## Materializations

Les graphes runtime, indexes, diagnostics de cas, portable v6 et anciens wrappers v9 sont des représentations physiques ou surfaces de lecture; leur existence ne change pas le Logical Commitment.

## Recettes de reconstruction

Depuis `knowledge-base/` : `python tools/build.py`, `python tools/build_v9.py`, `python tools/validate_v9.py`. Ensuite, depuis le kit 3.2.2 : `python tools/kristal.py check <workspace>` puis `python tools/kristal.py build-v9 <workspace>`.
