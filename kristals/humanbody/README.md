# Kristal HumanBody — paquet consolidé

Structure stable, explicite et sans numéro de version dans les noms de dossiers :

```text
Kristal-HumanBody/
├── knowledge-base/
│   ├── corpus/
│   ├── documentation/
│   ├── edition/
│   ├── examples/
│   ├── integration/
│   ├── profiles/
│   ├── schemas/
│   ├── sources/
│   └── tools/
└── external-source-library/
    ├── indexes/
    ├── snapshots/
    ├── source-store.json
    └── manifest.sha256.json
```

La version du corpus reste enregistrée dans `knowledge-base/VERSION`, les métadonnées et le changelog, mais elle ne fait plus partie des noms de dossiers.

Le ZIP imbriqué de la base et le ZIP redondant du seed ne sont pas conservés.
