# Architecture VaticanOps v2

## Séparation des responsabilités

**Capture** → fichiers officiels sous `sources/` avec SHA-256 → index d'unités `derived/source-units.json` → registre canonique d'identifiants textuels `canon/domain/vaticanops.text-unit-registry.json`.

**Interprétation** → 16 graphes ARK-04 + 167 assertions éditoriales à réviser. Les références pointent vers les documents physiques : emplacement, identité textuelle, SHA de fichier et de passage.

**Normativité** → registre des versions et des organes, mais la vigueur reste `undetermined_requires_specialist_review`. Une date, une copie et une autorité citée n'autorisent pas à déterminer automatiquement la portée d'un texte.

**Conditions** → chaque transition possède une garde explicitement typée et un identifiant stable. La logique est à trois valeurs : `unknown` n'est ni `false` ni `true` ; toute décision pratique est hors périmètre.

**Identités** → KQ/KP/KA/KS profil v11 opt-in (namespace local), avec lexique français et aucune correspondance Wikidata présumée. Il décrit la provenance des graphes, pas une ontologie juridique complète.

**Build et lecture** → état v9 et engagements canoniques calculés par le kit ; vue HTML autonome et Tkinter ; AI portable dérivée, non canonique. Aucune publication, activation, mise à jour en direct ou commande institutionnelle.

## Politique d'exception et de délais

Les délais présents dans les textes restent des citations/paraphrases non calculables. On évite d'automatiser les calendriers de recours sans définition de jour utile, champ d'application, version et confirmation par autorité compétente. Toute exception n'est ajoutée que si une référence exacte est disponible. L'absence de règle encodée n'implique pas qu'aucune règle existe.

## Extension sûre

Lors de l'ajout de procédures, conserver les identités KQ/KA existantes ; inscrire les nouveaux passages avec l'empreinte exacte ; ajouter sources et assertions, puis réviser les gardes et relancer `check-v11`, `validate_vaticanops.py`, `audit` et le builder v9. Les fichiers `VaticanOps_Dashboard.html` et `derived/` doivent être régénérés après extension.
