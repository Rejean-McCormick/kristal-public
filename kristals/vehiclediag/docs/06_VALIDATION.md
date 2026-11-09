# Validation du domaine et lifecycle v10

## Invariants structurels

Le graphe doit conserver l’identité des composants, ports et connexions; une connexion peut être une cible de panne; les chemins ordonnés restent ordonnés; les états opératoires et dépendances doivent rester cohérents.

## Invariants épistémiques

`DTC != diagnostic`, `symptôme != cause`, `mesure != vérité cachée`, `réparation réussie != preuve suffisante de cause racine`, `absence de DTC != absence de panne`, et une connaissance générique ne devient pas automatiquement un fait spécifique.

## Tests de reconstruction

Le corpus fournit un self-check, une validation métier, une validation v9 et une suite de tests unitaires. La normalisation 3.2.2 doit en plus passer `kristal.py check` et `kristal.py build-v9`.

## Logical Commitments

Le Reference Model et l’Epistemic Overlay utilisent `kristal.logical/jcs-sha256-v1`; le State Snapshot utilise `kristal.state-commitment/jcs-sha256-v1`. La migration doit conserver les commitments historiques lorsque le contenu logique ne change pas.

## Critères de publication

Publication interdite si le build métier, les tests, le check 3.2.2 ou la qualification indépendante échouent. `build`, `publish` et `activate` restent des étapes séparées. La présente normalisation ne publie ni n’active rien.
