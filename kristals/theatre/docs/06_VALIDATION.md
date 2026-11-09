# Validation

1. `python tools/kristal.py check .`
2. `python tools/kristal.py build-v9 .`
3. `python tools/verify_factorized_v9.py` (nécessite `zstd`).

Le nouveau State Commitment doit correspondre à `sha256:2a364ab27898c42f0a37772d9b5a8124af70c6c4331de5c9669e83ad88eaeb70`. Vérifier en plus les digests des blobs historiques. Ce protocole confirme la fidélité de migration et les intégrités cryptographiques, pas la vérité substantielle des données du domaine.
