# HistoryTech — paquet consolidé

Structure stable, explicite et sans numéro de version dans les noms de dossiers :

```text
HistoryTech/
├── knowledge-base/
├── source-manager/
└── external-source-library/
    ├── indexes/
    ├── snapshots/
    └── source-store.json
```

Le corpus canonique contenu dans `knowledge-base/` est conservé byte pour byte afin de préserver son manifeste SHA-256. Les changements concernent uniquement l'organisation extérieure, le gestionnaire et la bibliothèque de sources.

Les archives ZIP imbriquées, le template sidecar séparé, les caches Python et les copies PDF publiées en double ont été retirés.
