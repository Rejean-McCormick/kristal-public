# Canon et dérivés — Kristal-Pouvoirs-France

**Canon authoring** : `canon/state.index.json` et `canon/domain/jurisdictional-power.payload.json`. Le payload du membre v9 est copié exactement et ses engagements sont recalculés par JCS-SHA256.

**Canon juridique historique conservé** : `knowledge-base/corpus/*.kristal-state.json` et `knowledge-base/sources/`. Ces fichiers ont un statut de source native, pas de simple cache.

**Représentation historique** : `.kristal/v9/` est gardé intact. La matérialisation de profil `kristal.materialization/kristal-state-v6/1` référence son blob existant sous `.kristal/v8/`.

**Dérivés** : `.kristal/v8/index`, autres read models v8, `build/v9`, runtime, projections produites, release. Une nouvelle matérialisation ne doit pas changer le Logical Commitment.
