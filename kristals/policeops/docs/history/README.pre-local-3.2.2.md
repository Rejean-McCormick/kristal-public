# PoliceOps Kristal — paquet organisé

Ce paquet regroupe les éléments du snapshot SmartSnap dans une structure stable et explicite, sans numéro de version dans les noms de dossiers.

```text
PoliceOps-Kristal/
├── knowledge-base/
│   ├── corpus/
│   ├── documentation/
│   ├── edition/
│   ├── integration/
│   ├── profiles/
│   ├── runtime/
│   ├── schemas/
│   ├── sources/
│   └── tools/
├── source-manager/
├── external-source-library/
└── SmartSnap.pyw
```

## Principes appliqués

- la base `knowledge-base/` est conservée byte-for-byte afin de préserver son `state_id` et ses hashes ;
- les trois fichiers JSON dupliqués à la racine du snapshot original ne sont conservés qu'à leur emplacement canonique sous `knowledge-base/sources/` ;
- le schéma Source Store identique n'est conservé qu'une fois, sous `knowledge-base/schemas/` ;
- le sidecar versionné devient `external-source-library/` ;
- le gestionnaire utilise automatiquement ces nouveaux noms ;
- `SmartSnapK.pyw` devient `SmartSnap.pyw` et reste à la racine afin de continuer à capturer tout le paquet.

## Limite du snapshot reçu

SmartSnap n'a pas inclus les représentations stockées sous `objects/` (PDF/HTML/MHTML, etc.). Le manifeste de la bibliothèque externe référence donc des fichiers qui ne sont pas présents dans ce ZIP. Les métadonnées et la baseline restent utiles, mais une vérification physique complète du Source Store exige le store original ou une nouvelle synchronisation.
