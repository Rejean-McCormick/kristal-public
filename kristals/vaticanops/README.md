# Bundle Kristal + annexes normalisées (24 octobre 2026)

**Entrée recommandée :** `OUVRIR_VATICANOPS.html` (double-cliquer, fonctionne hors ligne).

Cette distribution fusionne la dernière version `VaticanOps-PROGRESSION-NORMATIVE-2026-10-24.zip` et le bundle `VaticanOps-ANNEXES-NORMALISEES-v1-2026-10-24.zip`. Elle préserve les identifiants et artefacts canoniques préexistants. Le dossier `annexes/` conserve 517 originaux octet pour octet, les index normalisés et 78 notices **non acquises**.

Pour les références, consulter `derived/annex-reference-bindings.json`, `derived/procedure-annex-links.json` ou `annexes/00_INDEX/INDEX.html`. Vérifier l'intégrité avec `python tools/verifier_bundle.py`.

**Portée :** la présence d'une copie n'atteste ni de sa version en vigueur ni de son applicabilité. 57 graphes éditoriaux, non certifiés juridiquement. Il ne s'agit pas d'une exhaustive compilation de tous les documents publics et internes du Vatican.

---

# VaticanOps — édition approfondie de recherche (24 octobre 2026)

**Kristal indépendant** : ARK-04 (procédure/protocole) + ARK-01 (référentiel et preuves). **Statut `building`, non publié, non activé.** Aucun aval du Saint-Siège, aucune qualification juridique, aucun moteur d'exécution ou de décision religieuse/judiciaire.

## Extension supplémentaire — sources officielles vérifiées (24 octobre 2026)

**Nouveau :** `VaticanOps_Normes_Verifiees.html` — 8 références officielles contrôlées, 57 paraphrases d’articles et 12 parcours de recherche non exécutables. Les textes nouveaux ne sont pas téléchargés; les 57 graphes locaux originaux restent inchangés. Voir `NOUVEAUTES_2026-10-24.md`.

## Ouvrir

- `VaticanOps_Corpus_Total.html` — portail hors ligne, recherche plein texte, 57 graphes, 78 notices complémentaires. Cliquer sur « Voir les étapes et leurs passages sources » pour lire l'ancrage précis.
- `VaticanOps_Atlas.html` — notices officielles, autorités et risques de versions.
- `VaticanOps_Dashboard.html` — exploration alternative des 57 graphes et du corpus.
- `VaticanOps.pyw` — application Windows avec Python.
- `VaticanOps_Synchroniser.pyw` — téléchargements des textes publics référencés vers une couche **non révisée**.
- `VaticanOps_Collecte_Publique.pyw` — découverte des pages de collections publiques, limites et contrôle SHA-256.

## Couverture réellement contenue dans cette archive

| Mesure contrôlée | Nombre |
|---|---:|
| Œuvres primaires originales présentes avec leurs copies locales | **6** |
| Fichiers sources intacts avec SHA-256 | **517** |
| Unités textuelles reconstituées, intégrales et SHA-256 vérifiées | **2 678** |
| Graphes procéduraux éditoriaux (16 originaux + 41 nouveaux) | **57** |
| Nœuds / transitions | **232 / 180** |
| Passages source effectivement reliés à au moins un graphe | **193** |
| Passages non encore rattachés à un graphe | **2 485** |
| Assertions épistémiques locales | **412** |
| Graphe sémantique v11 : entités / assertions | **278 / 457** |
| Notices publiques externes **sans copies locales** | **78** |
| Dossiers nouveaux téléchargés depuis ces 78 notices | **0** |

Les **1 668 candidats** trouvés par expressions régulières restent des suggestions de lecture sans statut de procédure vérifiée. Les 57 graphes sont des **séquences d'étude documentaire**; ils n'attestent ni la complétude des conditions, ni leur validité temporelle, ni la compétence de l'autorité dans un cas concret.

**Les 78 notices ne sont pas 78 documents acquis.** Certaines pointent des répertoires; une seule collection peut contenir des centaines de textes. La collecte directe de ces URLs n'était pas disponible dans l'environnement de construction. Aucune copie complémentaire n'a été présentée comme intégrée.

## Nouveautés vérifiables

1. **41 graphes supplémentaires** avec 131 nouvelles références textuelles uniques, couvrant administration, CIC latin, biens et justice, DDF, vacance, conclave et liturgie.
2. **193 références distinctes ancrées à un fichier source**; 517 empreintes SHA-256 d'origine inchangées.
3. **Matrice article par article** `validation/MATRICE_2678_DISPOSITIONS.csv` : chaque unité, son livre/catégorie, ses mots-clés, la présence ou non d'un graphe, le statut de révision et sa source exacte.
4. **Index SQLite plein texte** `derived/VaticanOps_recherche.sqlite`, basé sur la totalité des fragments intégralement vérifiés.
5. **Graphe sémantique v11** enrichi en conservant les identités existantes. Toutes les créations restent dans le domaine éditorial indépendant.
6. **7 nouvelles pistes officielles** : confidentialité des données de l'État, lignes directrices IA, textes d'application sur les marchés publics, droits de secrétariat, règles judiciaires et législation du gouvernement de l'État. Ce sont des **références**, pas des copies.

## Sources manquantes prioritaires

CCEO et modifications de 2026; loi fondamentale du Vatican de 2026; règlement du personnel de 2025; VELM 2023; normes DDF 2021; tribunaux et `Lex propria` 2024; réforme des procès matrimoniaux de 2015 (textes canoniques manquants au dossier d'origine); textes des finances, marchés publics, Gouvernorat et protection des données; causes des saints; textes et livres liturgiques spécialisés; documents des dicastères et Acta Apostolicae Sedis. Des `Ordo servandus` et manuels internes peuvent ne pas être publics.

**Important :** le Code canonique de départ ne dispose pas des canons reformulés sur les procès de nullité matrimoniale : VaticanOps n'invente pas un graphe de ces procédures. Une étape de collecte et de consolidation avec les textes de 2015 est obligatoire.

## Auditer et reconstruire

```powershell
python tools/vaticanops.py audit
python tools/validate_vaticanops.py
python tools/validate_expansion.py
python tools/validate_exhaustive.py
python tools/build_clause_audit.py
python tools/kristal.py check .
python tools/kristal.py check-v11 .
python tools/kristal.py check-ai .
python -m unittest discover -s tests -v
```

Après une acquisition sur un ordinateur connecté, exécuter `python tools/rebuild_all.py` pour mettre à jour les index; les nouvelles captures **ne sont pas automatiquement promues** en sources canoniques validées. Les commandes `tools/expand_local_procedures.py`, `tools/align_epistemic_assertions.py` et `tools/extend_v11_semantic_graph.py` sont idempotentes pour reproduire l'extension documentaire.

Le texte numérisé n'est pas une version consolidée du droit. Une compétence, une règle en vigueur, une procédure correctement applicable et une copie téléchargée sont quatre assertions différentes. Toute utilisation décisionnelle exige le texte normatif actuel, ses amendements et une analyse spécialisée.
