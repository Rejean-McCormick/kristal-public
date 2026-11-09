# Kristal — kOA / Koali Sales Pitch

**Local workspace :** `kristal.local-workspace/3.2.0` (Authoring Kit 3.2.2)  
**Semantic State :** `kristal.state/9.0`  
**Domaine :** `koa-sales-pitch`  
**Lifecycle local :** `building`

## Commandes Local 3.2.2

```bash
python tools/kristal.py check .
python tools/kristal.py build-v9 .
```

Le canon Local 3.2.2 est déclaré dans `canon/state.index.json`. Les couches historiques `.kristal/v8` et `.kristal/v9` sont conservées comme compatibilité/dérivés ; elles ne sont pas la surface d'authoring courante. Aucune publication ni activation réseau n'est implicite.

---

## Description fonctionnelle héritée

Version **v0.6.0** — base de connaissance et copilote de rencontre.

## Ce que cette version améliore

1. **Sécurité par séparation** : l’architecture est maintenant décrite comme une isolation stratégique des responsabilités, autorités et données, reliées par des **points d’articulation explicites**.
2. **Trois niveaux de sécurité** : contrôles techniques + pratiques humaines/organisationnelles + isolation architecturale.
3. **Identité locale** : les workflows peuvent travailler avec des rôles stables pendant que la correspondance rôle→personne reste dans une couche locale.
4. **Réponse incubateur plus concrète** : “c’est sécuritaire ?” répond d’abord au mécanisme architectural, puis à la frontière de preuve (audit/déploiement).
5. **Discipline de preuve** : modularité ≠ garantie de confinement; aucun pentest, certification ou protocole précis n’est inventé.

## À lire avant une rencontre

1. `views/meeting-fast-path.md`
2. `views/top-25.md`
3. `views/security-and-modularity.md`
4. `views/scale-continuum.md`
5. `views/language-and-semantics.md`
6. `views/pre-meeting-gates.md`
7. `views/chatgpt-live-prompt.md`

## Règle centrale

**Répondre au besoin avant l’architecture; pour la sécurité, expliquer la séparation stratégique avant les contrôles génériques.**

`question → réponse simple → preuve/limite → bridge seulement si utile`

## E2E

La preuve E2E annoncée comme prochaine étape reste **non vérifiée dans ce Kristal** tant qu’un artefact réel n’est pas attaché et enregistré dans `meeting-state.json`.

## Validation locale

```bash
python knowledge-base/tools/validate.py
python knowledge-base/tools/query.py "c'est sécuritaire" --profile incubator
python knowledge-base/tools/query.py "points d'articulation" --profile incubator
```


## Structure normalisée

- `.kristal/` — couche v8 dérivée et métadonnées de normalisation;
- `external-source-library/` — extraits de sources conservés séparément;
- `knowledge-base/corpus/` — état canonique et index;
- `knowledge-base/sources/` — sources éditoriales internes;
- `knowledge-base/profiles/` — profils de lecture;
- `knowledge-base/schemas/` — schémas;
- `knowledge-base/documentation/` — documentation;
- `knowledge-base/tools/` — outils;
- `views/` — projections de lecture pour les rencontres;
- `validation/` — rapports de validation.

Les chemins internes ont été alignés sur cette structure; les extraits de sources externes ne sont pas réécrits.


## Kristal v9

Ce repo est migré vers **Kristal 9.0.0-draft.1 — Semantic State Architecture** sans supprimer les surfaces v6/v8 existantes.

- canon v9 : l’état v6 canonique `knowledge-base/corpus/sales-pitch.kristal-state.json`;
- snapshot logique immuable : `.kristal/v9/state-snapshot.json`;
- matérialisations : `.kristal/v9/materialization.*.json`;
- projection portable v6 : conservée sous `.kristal/v8/portable-state.kristal-state.json` et explicitement dérivée;
- profils de rencontre, vues Markdown et index/query v8 : restent dérivés/read-side;
- identité logique v9 : séparée des digests physiques des fichiers.

Voir `.kristal/v9/README.md` et `V9_MIGRATION.md`.
