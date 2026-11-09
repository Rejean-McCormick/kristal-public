# Collecte publique extensible — VaticanOps

Le programme `VaticanOps_Collecte_Publique.pyw` est une interface Windows pour explorer **des collections officielles publiques** ; il ne contourne aucune authentification, contrôle d'accès ou restriction des sites et ne collecte aucun dossier privé.

Il utilise la bibliothèque standard Python et n'a besoin que de Python 3.10+ (Tkinter inclus avec Python Windows).

## Démarrage

1. Décompresser le dossier VaticanOps complet.
2. Ouvrir `VaticanOps_Corpus_Total.html` pour la consultation immédiate hors ligne.
3. Lancer `VaticanOps_Synchroniser.pyw` pour les documents **déjà identifiés par URL précise**.
4. Lancer `VaticanOps_Collecte_Publique.pyw` pour parcourir les **index officiels**, avec un budget raisonnable (250 fichiers, profondeur 2 proposés).
5. Ouvrir de nouveau `VaticanOps_Corpus_Total.html`, reconstruit à la fin du téléchargement, pour parcourir les nouveaux passages non révisés.

## Console

```powershell
python tools/sync_official.py list
python tools/sync_official.py sync
python tools/sync_official.py sync --all
python tools/harvest_collections.py seeds
python tools/harvest_collections.py run --max 250 --depth 2 --delay 1
python tools/harvest_collections.py status
python tools/rebuild_all.py
python tools/recherche.py "recours" --max 20
python tools/validate_exhaustive.py
```

Le collecteur consulte les fichiers robots.txt et applique la politique `strict` par défaut. Si l'URL robots.txt est indisponible, le site est ignoré. Un utilisateur autorisé peut lancer en console avec `--robots-policy allow-on-error` pour gérer ce cas, mais les règles explicites d'interdiction restent respectées. Aucune requête plus fréquente qu'une par 0,2 seconde n'est autorisée, et la valeur par défaut est d'une seconde.

Les fichiers et leur empreinte SHA-256 sont enregistrés dans `sources/harvested/manifest.json` ; la file d'URLs découvertes est enregistrée dans `sources/harvested/frontier.json` pour reprise. Les textes HTML sont extraits dans `derived/harvested-units.json` ; les PDF sont conservés sous forme de copies binaires mais leur contenu n'est pas analysé sans outil PDF supplémentaire.

La collecte ne constitue **pas** une certification de l'applicabilité juridique, de la complétude des archives ou de l'authenticité normative finale. L'intégration dans le canon v9/v11 doit rester une opération séparée de revue spécialisée.

## Limites

- Les pages rendues uniquement en JavaScript, les liens non découvrables et certaines pièces jointes peuvent être manqués.
- Un index officiel peut pointer vers des publications antérieures, abrogées, amendées ou non normatives.
- Une collection comme les *Acta Apostolicae Sedis* est beaucoup plus vaste que le budget de collecte recommandé; répéter la découverte au besoin.
- Les protocoles confidentiels ou non publiés ne sont pas acquis.
- Le système traite uniquement les ressources publiques sur une liste fermée de domaines officiels et n'affirme pas être un outil institutionnel du Saint-Siège.
