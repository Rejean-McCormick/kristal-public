# Kristal-Theatre v1.0.0

Corpus statique et validé décrivant la grammaire **texte/performance → personnage → scène → mise en scène → représentation**.

## Noyau conceptuel

- **Texte / œuvre** : œuvre théâtrale, texte dramatique, version, adaptation, acte, scène textuelle, didascalie et action dramaturgique.
- **Personnage / rôle** : personnage fictionnel, rôle performatif, attribution à un interprète, objectifs, relations et parcours.
- **Scène / espace** : plateau, espace de jeu, public, coulisses, blocking, lignes de vue, entrées/sorties et transitions.
- **Mise en scène** : concept directeur, interprétation, répétition, casting, dramaturgie, régie, changements et exploitation.
- **Conception** : scénographie, accessoires, costumes, lumière, son, projection, automation et documentation technique.
- **Représentation** : événement daté, jeu, voix, geste, mouvement, rythme, improvisation, variations et réception du public.

## Invariant central

Le théâtre n’est pas réductible à son texte. Le Kristal sépare explicitement **œuvre**, **texte/version**, **production/mise en scène** et **représentation datée**. Une même œuvre peut donner lieu à plusieurs productions; une production à plusieurs représentations; chaque représentation peut varier sans devenir automatiquement une nouvelle production.

## Garde-fous majeurs

- scène textuelle ≠ scène physique ;
- personnage ≠ rôle ≠ interprète ;
- texte dramatique ≠ production ;
- didascalie ≠ action effectivement réalisée ;
- mise en scène ≠ simple blocking ;
- production ≠ représentation ;
- représentation ≠ captation ;
- répétition ≠ représentation publique ;
- décor ≠ plateau ;
- cue ≠ état technique ;
- prompt book ≠ script ;
- réception du public ≠ critique publiée ;
- applaudissements ≠ mesure objective de qualité ;
- reprise d’une œuvre ≠ reprise de la même mise en scène ;
- théâtre ≠ cinéma, danse, opéra ou rituel par simple similarité de forme.

## Taille

- Référents : **254**
- Assertions atomiques : **1015**
- Sources : **8**

## Organisation

Le fichier canonique est `knowledge-base/corpus/theatre.kristal-state.json`. Cinq modèles spécialisés décrivent la relation œuvre-réalisation, personnage-rôle-interprète, scène-espace, mise en scène-production et représentation comme événement.

## Statut

Référence statique v1.0.0. Le corpus ne contient ni catalogue exhaustif de pièces, ni histoire mondiale du théâtre, ni données dynamiques de billetterie, ni textes dramatiques protégés reproduits.
