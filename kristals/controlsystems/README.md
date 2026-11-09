# Kristal-ControlSystems v1.0.0

Corpus statique de référence sur les **systèmes de commande et de régulation**.

## Noyau conceptuel

```text
Consigne / référence r
        ↓
   comparaison ← mesure y_m ← capteur ← sortie y
        ↓ erreur e                     ↑
   contrôleur → commande u → actionneur → système / procédé
```

Chaîne conceptuelle : **consigne → système → mesure → erreur → correction**.

## Principe de conception

Le Kristal distingue strictement le système physique, son modèle, la mesure, l’erreur, la perturbation et la loi de commande. Une rétroaction n’est jamais supposée stabilisante par définition. Les propriétés de stabilité, performance et robustesse portent toujours un contexte de modèle et d’architecture.

## Portée v1

- boucle ouverte et boucle fermée;
- rétroaction négative/positive, feedforward, cascade, retour d’état;
- capteur, chaîne de mesure, contrôleur, actionneur, procédé, observateur;
- signaux canoniques `r, e, u, y, y_m, d, n, x, x_hat`;
- familles P/I/D, PI/PD/PID, compensateurs lead/lag, retour d’état, LQR, MPC, adaptatif et robuste au niveau conceptuel;
- modèles continu/discret, linéaire/non linéaire, LTI, SISO/MIMO, fonction de transfert, espace d’état;
- stabilité, suivi, erreur permanente, réponse transitoire, marges, robustesse, sensibilité, effort de commande;
- perturbations, bruit, incertitudes, saturation, retards, quantification et échantillonnage.

## Frontière volontaire

Ce Kristal n’est **pas** un manuel de réglage. Il ne contient pas de gains prêts à appliquer, de paramètres de commande pour une machine réelle, ni de limites de sécurité spécifiques à un procédé. Les méthodes de synthèse sont décrites comme concepts conditionnels.

## Reproductibilité

```bash
python knowledge-base/tools/build.py
python knowledge-base/tools/validate.py
python knowledge-base/tools/query.py --concept pid
```

Les sources distantes sont cataloguées par métadonnées; le corpus canonique est autonome, statique et hashé.
