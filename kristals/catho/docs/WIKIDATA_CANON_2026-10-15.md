# Import canonique v9 — Catho / Wikidata — 15 octobre 2026

Cette migration éditoriale ajoute deux Logical Artifacts à `canon/state.index.json` sans changer les deux payloads canoniques antérieurs et sans réécrire les états historiques `.kristal/v9`.

## Données et propriété

- `canon/domain/wikidata-import.json` : 1 692 enregistrements Wikidata **intégraux** extraits du dump `wikidata-20260922-all.json.bz2`, avec déclarations `claims`, qualificatifs, références, rangs, libellés, alias et sitelinks. L'ensemble est une sélection bornée; l'absence d'un élément ne prouve pas sa non-existence dans Wikidata.
- `canon/domain/wikidata-alignments.json` : 406 personnes de la campagne sélectionnée, dont 245 rapprochements de l'index exact P31=Q5 non réévalués indépendamment et 161 dossiers en recherche. 21 dossiers possèdent des **propositions de recherche documentaire** et 3 autres des **suggestions algorithmiques** ; aucune de ces 24 correspondances n'est acceptée automatiquement. Contient les 339 assertions d'enquête Skope, 24 URL enregistrées sans récupération indépendante, et les candidats détaillés.
- 1 455 relations P50 dans la rubrique `author_work_index_observations` proviennent de l'index agrégé Wikidata, non d'une assertion `P50` directe individuellement recoupée. Les items complets contiennent leurs déclarations propres.
- `canon/domain/personnes-reconnaissances.json` (668 personnes) et `canon/domain/legacy-logical-artifact.payload.json` sont **strictement inchangés**. Les identifiants Catho existants sont réutilisés sans création de doublons.

## Provenance et engagements

L'instantané conserve son manifeste de campagne et les condensats SHA-256 des deux segments compressés. Les fichiers d'entrée conservés sous `knowledge-base/imports/...` restent disponibles pour audit. La sérialisation canonique des deux nouveaux artefacts est JSON stable, engageable via `compute-json-jcs` du Kit.

**Les sources documentaires ne sont pas vérifiées ici sur le Web.** Une URL présente dans le dossier est une référence, pas une attestation de son contenu. `candidate` et `unknown` ne signifient ni `accepted` ni `false`. Une appartenance à une institution catholique n'est pas une approbation doctrinale.

## Construction locale / publication

```powershell
$k = "C:\mycode\Kristal\locals\A-Kristal-Catho"
$py = "C:\Users\rejea\AppData\Local\Programs\Python\Python312\python.exe"
& $py "$k\tools\validate_catho_wikidata.py" $k
& $py "$k\tools\kristal.py" check $k
& $py "$k\tools\kristal.py" build-v9 $k
& $py "$k\tools\kristal.py" check $k
```

`build-v9` construit un état **candidat local**, pas une qualification factuelle ni une publication/activation. Skope ne lit pas automatiquement le graphe canonique v9 sous forme de visualisation ; sa consultation relève d'un lecteur compatible et ne modifie pas cet import.
