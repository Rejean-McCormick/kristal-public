# Kristal-ScolQc — paquet consolidé

Kristal-ScolQc est un **Local Kristal 3.2.2** représentant des connaissances structurées sur le parcours scolaire et les règles éducatives du Québec. La release domaine reste **1.4.0**; la normalisation locale est additive et ne réécrit pas les assertions éducatives.

```text
Kristal-ScolQc/
├── kristal.workspace.json       # enveloppe Local Kristal 3.2.2
├── canon/                       # index + quatre Logical Artifacts v9 qualifiés
├── docs/                        # contrat de forme, frontières et validation 3.2.2
├── sources/                     # index de sources 3.2.2 vers le catalogue domaine
├── knowledge-base/              # données scolaires Québec, contrats, schémas, outils
├── source-manager/              # application opérationnelle de capture et résolution
├── external-source-library/     # Source Store opérationnel; hors canon logique
└── .kristal/                    # couches historiques v8/v9 conservées pour compatibilité
```

Les noms de dossiers historiques restent stables. Les versions historiques et techniques restent dans les fichiers de métadonnées où elles sont nécessaires.

La bibliothèque externe est initialisée depuis le corpus courant et contient les **122 sources officielles déclarées**, mais aucun document téléchargé tant que `sync` n'est pas lancé.

## Validation

Validation domaine :

```bash
cd knowledge-base
python tools/build.py
python tools/validate.py
```

Validation Local Kristal 3.2.2 :

```bash
python <Authoring-Kit>/tools/kristal.py check <Kristal-ScolQc>
python <Authoring-Kit>/tools/kristal.py build-v9 <Kristal-ScolQc>
```

La publication et l'activation sont volontairement séparées du build et ne sont pas effectuées par la normalisation.
