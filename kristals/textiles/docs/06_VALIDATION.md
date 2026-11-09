# Validation

1. `python tools/kristal.py check .`
2. `python tools/kristal.py build-v9 .`
3. `python tools/verify_factorized_v9.py` (nécessite `zstd`).

Le nouveau State Commitment doit correspondre à `sha256:749bfc75fb9e33a1001a6bf21f05c55e8bef0f1ae9378397b6c6f88ba0dd80d6`. Vérifier en plus les digests des blobs historiques. Ce protocole confirme la fidélité de migration et les intégrités cryptographiques, pas la vérité substantielle des données du domaine.
