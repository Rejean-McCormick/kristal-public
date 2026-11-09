# Validation

1. `python tools/kristal.py check .`
2. `python tools/kristal.py build-v9 .`
3. `python tools/verify_factorized_v9.py` (nécessite `zstd`).

Le nouveau State Commitment doit correspondre à `sha256:cccab018f9e58f24b6f00c85187bc6580e31014d8ebde280c6603c1af59b8008`. Vérifier en plus les digests des blobs historiques. Ce protocole confirme la fidélité de migration et les intégrités cryptographiques, pas la vérité substantielle des données du domaine.
