# Kristal-Urbanism v1.0.0

**Domaine :** urbanisme — parcelle → quartier → ville → réseau; usage, densité, mobilité  
**Statut :** `working`  
**Snapshot éditorial :** 2026-10-02  
**Langue principale :** français

## Axe canonique

`parcelle → quartier → ville → réseau`

Axes transversaux : `usage + densité + mobilité`.

Le passage d’échelle n’est **pas une causalité**. Les réseaux traversent les parcelles, quartiers et villes; ils peuvent aussi relier plusieurs villes. Le corpus modélise donc la progression d’échelle avec des axes auxiliaires de **forme urbaine**, **réseau**, **périmètre**, **indicateur** et **condition urbaine**.

## Garde-fous

- `densité ≠ surpeuplement`
- `mobilité ≠ accessibilité`
- `limite municipale ≠ zone bâtie ≠ centre urbain statistique ≠ zone urbaine fonctionnelle`
- `distance euclidienne ≠ distance parcourable sur réseau`
- `usage conceptuel ≠ permission réglementaire locale ≠ activité observée`
- `connectivité ≠ capacité ≠ sécurité ≠ fiabilité ≠ équité`

Les relations forme–usage–densité–mobilité sont encodées comme **relations contextuelles**, non comme lois causales universelles.

## Contenu

Voir `knowledge-base/corpus/index.json` pour les comptes calculés, `corpus/urbanism.kristal-state.json` pour l’état Kristal v6 et `sources/source_catalog.json` pour les références.

## Validation

```bash
cd knowledge-base
python tools/build.py
python tools/validate.py
python -m unittest tests/test_model.py
```

Le corpus est reconstruit de façon déterministe à partir de `sources/*.json`.
