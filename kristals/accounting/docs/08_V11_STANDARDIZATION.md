# Kristal-Accounting — standardisation Authoring Kit v4 draft.2 / préparation v11

**Statut : enveloppe standardisée + v11 readiness, PAS un Kristal converti en v11.**

## Références utilisées

- Snapshot local du Kristal-Accounting v1.0.0 (corpus v6, v8, v9, local workspace 3.2.2).
- Snapshot de Kristal-Authoring-Kit v4.0.0-draft.2 du 17 octobre 2026, notamment `docs/26_V11_SEMANTIC_AUTHORING.md`, `docs/27_DIK_INTEGRATION.md` et `docs/28_V11_FRAMEWORK_QUALIFICATION.md`.
- La **norme du Framework v11 draft.3**, telle qu'épinglée par `contracts/v11-framework-pin.json`, reste une autorité externe distincte. Le snapshot du Kit n'autorise pas seul à déclarer une conversion v11 conforme.

## Ce qui a été fait

1. Mise à niveau de `tools/kristal.py` et de `tools/kristal_v11_core.py` à partir du Kit joint. **Adaptation locale documentée** dans `_discover_materialization_manifests` : l'ancienne matérialisation éditoriale `source-bundle` reste une entrée historique, hors des deux membres du State v9. Le script `tools/build-preserving-v9.py` vérifie **séparément** les 3 manifestes historiques et les blobs/segments associés.
2. Aucun payload historique ou paquet `.kristal/v8/`, `.kristal/v9/` n'a été réécrit. Les fichiers de l'archive historique sont conservés avec leurs SHA-256 enregistrés dans `validation/baseline-canonical-hashes.json`.
3. Le commit logique v9 est **inchangé** : `sha256:5453336ee188d670da638c0afd1c86a6e7ea7b36df75fe58322bcfacfa4f2a3a`.
4. Le nouvel outil fournit `build-discovery` / `audit-discovery` pour reconstruire les métadonnées de lecture. Ces caches dérivés ne sont **pas embarqués** : leur empreinte deviendrait périmée lors du packaging. Exécuter `python tools/kristal.py build-discovery .` localement au besoin.
5. Inventaire de conversion v11 et libellés **non canoniques** sous `derived/v11/`. Le registre v11, le graphe v11, le crosswalk et le dictionnaire v11 ne sont **pas** créés à partir de suppositions.

## Situation v11 réelle

- `289` référents historiques : `216` candidats **famille KQ**, `73` candidats **famille KP**, **zéro ID KQ/KP alloué**.
- `581` assertions historiques : conversion KA **non autorisée** tant que l'adaptateur complet et les preuves sont absents.
- `10` sources distinctes : KS à concevoir et approuver, non attribués ici.
- Le corpus originel contient des prédicats `urn:accounting:predicate:*` et des libellés dans ses objets v6. Ces URN et labels **ne sont pas** des IDs canoniques KQ/KP v11.
- `KQ != Wikidata Q`, `KP != Wikidata P`, `label != identity` et `migration proposal != migration approved`.
- Les types natifs de comptabilité, l'applicabilité, les pièces probantes, les dimensions et les extensions ne doivent pas être aplatis en triples naïfs.

## Commandes locales de vérification

```bash
python knowledge-base/tools/validate.py
python tools/kristal.py check .
python tools/build-preserving-v9.py
python tools/prepare-v11-readiness.py --check
python tools/validate-standardization.py
```

Le build écrit **uniquement** sous `build/` et d'autres sorties dérivées. Il ne publie ni n'active un nouvel état.

## Étapes de migration à faire approuver

1. Choisir et valider le namespace, chaque cible KQ/KP et l'alignement entre anciens URN et nouveaux identifiants. Ne pas attribuer par simple ordre de ligne ou similarité de mot.
2. Renseigner les preuves KS, le statut de révision et les correspondances `exactMatch` externes éventuelles, indépendamment des dictionnaires.
3. Écrire un **adaptateur accounting v6→v11 explicite** préservant les 581 assertions, les objets item/literal, régimes épistémiques, applicabilités et extensions natives. La commande `apply-v11-plan` du Kit est **limitée aux graphes déjà structurés en v11** ; elle ne couvre pas ce corpus hétérogène automatiquement.
4. Créer des artefacts v11 candidats distincts, les qualifier avec **les schémas réels du Framework draft.3 et le Kit `qualify-v11`**, puis enregistrer leurs contrats comme Logical Artifacts. Construire un nouveau v9 commitment uniquement après approbation.
5. Ne pas confondre `build`, `qualification`, `publication` et `activation`. Ces dernières nécessitent une autorisation explicite.

## Limites

La conformité indépendante v11 n'est pas revendiquée : aucun graphe KQ/KP complet n'a été créé. La qualification technique v9 et les tests métier locaux ne certifient pas les règles IFRS ni les pratiques d'une juridiction.
