# Validation

1. `python tools/kristal.py check .`
2. `python tools/kristal.py build-v9 .`
3. `python tools/verify_factorized_v9.py` (nécessite `zstd`).

Le nouveau State Commitment doit correspondre à `sha256:935dc34047e05fc83ed0483071893a9f62e75814a6c0080cf723f53d6f68549c`. Vérifier en plus les digests des blobs historiques. Ce protocole confirme la fidélité de migration et les intégrités cryptographiques, pas la vérité substantielle des données du domaine.
