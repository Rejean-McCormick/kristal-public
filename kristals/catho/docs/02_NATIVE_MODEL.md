# Modèle natif — Kristal-Catho

**Kind local** : `doctrinal_semantic_corpus_with_provenance`.

**Géométrie conservée** : corpus sémantique chrétien / catholique et documentation des positions, références, dossiers et registres de preuve.

**Invariant essentiel** : les positions et attestations dépendent de leur tradition, source et degré de reconnaissance ; ne pas assimiler stratégie de diffusion et canon doctrinal.

Le contrat engagé par le v9 historique reste `kristal.catho.semantic-corpus/1.0`. Ce contrat utilise le payload d'origine engagé dans v9 (corpus sémantique natif pour Catho ; `kristal_state` v6 pour les autres), avec les informations de provenance existantes. Cette migration ne convertit pas ce graphe en ontologie uniforme, en table ou en pipeline artificiel.

La vue authoring `canon/domain/legacy-logical-artifact.payload.json` est une photographie canonique du payload existant. Les fichiers du domaine dans `knowledge-base` restent inchangés. Le maintien en synchronisation future de ces deux sources exige une procédure éditoriale explicite.



## Contrat complémentaire — personnes et reconnaissances

Un second Logical Artifact enregistré sous `urn:kristal:catho:artifact:personnes-reconnaissances` implémente `kristal.catho.personnes-reconnaissances/1.0`. Son modèle est **relationnel à catégories multiples** (`personne` ← `reconnaissance` → `source`) : une personne peut être pape, docteur, membre de la CTI, académicien et lauréat du prix. Chaque lien de reconnaissance conserve sa provenance et, si disponible, son mandat, année, section et numéro de pontificat. Il n'altère pas le payload historique.
