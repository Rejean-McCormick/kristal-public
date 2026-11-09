# Kristal-Literature v1.0.0

Corpus statique de référence en littérature, centré sur le modèle :

**œuvre → texte → forme → thème → contexte → réception**

Le noyau ajoute identité bibliographique, structure textuelle, rôles narratifs, interprétation, provenance et temporalité.

## Taille
- 907 assertions Kristal v6
- 458 référents
- 8 sources externes + 1 modèle éditorial local
- 47 formes / genres
- 30 unités textuelles
- 30 traits textuels / narratifs / poétiques / dramatiques
- 40 thèmes de vocabulaire
- 25 dimensions de contexte
- 26 types de réception
- 17 types de preuve

## Principe de lecture

Le Kristal distingue l’identité abstraite d’une œuvre de ses expressions, éditions, exemplaires et témoins textuels. Les thèmes et interprétations sont représentés comme des lectures étayées plutôt que comme des propriétés intrinsèques. La réception est située dans un public, une période, un lieu et des sources.

Distinctions obligatoires :

1. `work != expression != manifestation != item`;
2. `work != text != text_witness`;
3. `author != narrator != speaker != character`;
4. `form/genre != theme/topic`;
5. `reception != intrinsic_quality`;
6. `context != demonstrated_cause_or_authorial_intention`.

## Référentiels

IFLA LRM structure l’identité bibliographique; TEI P5 structure les textes et leurs divisions; LCGFT sert d’ancrage au vocabulaire genre/forme; CIDOC CRM apporte le modèle événementiel pour contexte et réception.

## Validation
```bash
python knowledge-base/tools/validate.py
```

## Frontières

La v1 n’embarque pas de textes littéraires complets, n’attribue pas automatiquement des thèmes aux œuvres et ne produit aucun score esthétique. Elle fournit le cadre stable permettant d’ajouter ensuite des œuvres, éditions, passages, lectures critiques et événements de réception avec provenance.
