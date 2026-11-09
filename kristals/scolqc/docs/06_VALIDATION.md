# Validation

La qualification combine les contrôles natifs du domaine et les contrôles du Local Kristal 3.2.2.

## Domaine

Depuis `knowledge-base/` :

```bash
python tools/build.py
python tools/validate.py
```

Le validateur natif couvre notamment le schéma du structured epistemic state, les hashes d'assertions, les références source/autorité/document/édition/représentation, les règles et transitions, le curriculum, l'admission collégiale et FP, l'acquisition des sources et la cohérence de release.

## Workspace 3.2.2

```bash
python <Authoring-Kit>/tools/kristal.py check <Kristal-ScolQc>
python <Authoring-Kit>/tools/kristal.py build-v9 <Kristal-ScolQc>
```

Le `check` prouve la cohérence structurelle du workspace; il ne prouve pas la vérité sémantique.

Pour cette migration additive, un contrôle supplémentaire est requis : le snapshot construit doit conserver les quatre commitments membres historiques et, tant que ni les ressources ni leur segmentation ne changent, le State Logical Commitment historique `sha256:76020a229f3db812d3b10c3f51ebc56818281966bd0dd93c562003e0541a71b9`.
