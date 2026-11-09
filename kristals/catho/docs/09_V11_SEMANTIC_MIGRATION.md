# Migration Catho v11 : décisions et garanties

## Périmètre

La migration inclut l'ensemble des 4 520 nœuds, des 8 691 relations du graphe de consultation, des 1 076 assertions du corpus éditorial, des 3 203 qualificatifs d'assertion ainsi que les types de nœuds et les métadonnées de preuve et de provenance présentes dans les sources.

Chaque ancienne référence URI ou `wikidata:Q...` dispose d'une identité locale KQ indépendante. Les propriétés de relations et les qualificatifs sont normalisés en KP. Les catégories de nœuds sont représentées par des KQ de catégorie, reliés avec un KP de classification. Les assertions possèdent des KA ; leurs preuves et leurs sources ont des KS. Les textes narratifs de positions et d'arguments ont été matérialisés comme littéraux français, avec les références KQ/KP séparées.

Les **preuves structurées** et les objets JSON d'origine sont conservés intégralement dans les fichiers historiques et dans `canon/v11/provenance/evidence-by-assertion.jsonl`, associés à chaque KA. Des faits attribués à Wikidata ou à une source institutionnelle restent des faits **attribués**, non des prises de position de Kristal-Catho.

## Alignement Wikidata

- `accepted` + `audited_rule` : uniquement les références à des identifiants Wikidata présents en tant que tels dans le snapshot importé et les propriétés P explicitement présentes. Cela ne certifie pas leur signification ou leur vérité.
- `candidate` : tout rapprochement externe qui ne dispose pas de la preuve suffisante, en particulier les rapprochements de personnes Catho qui n'ont pas été indépendamment revalidés, et les Q externes absents du snapshot local.
- `research-candidate:Q...` : identité **locale de proposition de recherche**, distincte de l'entité `wikidata:Q...` et de toute personne historique.
- Aucune correspondance `closeMatch` ou `relatedMatch` n'est prise pour un `exactMatch`.

La liste entière des cas à examiner se trouve dans `canon/v11/review/pending-wikidata-alignments.json`.

## Dictionnaires

Les libellés FR préexistants sont portés dans une couche appelée `legacy-fr.json`, avec le réviseur marqué explicitement `automated-legacy-label-preservation-not-human-approval` : il s'agit d'une **transcription**, pas d'une approbation linguistique humaine.

Les données lexicales Wikidata proviennent du snapshot borné daté du 22 septembre 2026. Elles sont conservées dans des couches séparées par langue, avec priorité inférieure aux labels hérités de Catho pour l'affichage français. Les équivalences KQ ↔ Q pour ces couches sont structurellement vérifiées. `fr-CA` fait repli sur `fr`, sans inventer de traduction canadienne.

Les vrais taux de couverture (directe, par repli, manquante) figurent dans `.kristal/v11/reports/coverage-all.json` et `.csv`. La traduction des concepts spécifiques à Catho manque encore dans beaucoup de langues ; ces lacunes ne sont pas masquées.

## Limites et publication

Le Framework v11.0.0-draft.3 reste une **version de contrat draft**. L'Authoring Kit v4 doit encore qualifier/publier l'état complet avant d'en faire un artefact v11 pleinement engagé. Aucun artefact historique v9 n'a été réécrit ni réengagé.

La migration ne signifie pas que toutes les affirmations historiques sont vérifiées ; la validation théologique, les identités humaines incertaines et la complétion de 300 langues sont des chantiers de revue distincts.

## Tests

La commande `python tools/validate_v11_semantic.py` contrôle les 167 sources verrouillées, tous les anciens nœuds, arêtes, assertions éditoriales et qualificatifs, les appartenances de références, les correspondances acceptées, les candidatures, l'intégrité des couches lexicales et les preuves associées aux KA.

Le test `tools/make_v11_smoke.py` produit un petit projet diK réel depuis les mêmes artefacts ; l'export, la vérification et la restauration diK ont été testés sur ce projet. Les vues Markdown humaines ne sont **pas** des artefacts réversibles.
