# Validation

1. `python tools/kristal.py check .`
2. `python tools/kristal.py build-v9 .`
3. `python tools/verify_factorized_v9.py` (nécessite `zstd`).

Le nouveau State Commitment doit correspondre à `sha256:7699cd9fdf994b3fc9c6af922060bb9221d0454e6f1d8401f13fa0607e582efb`. Vérifier en plus les digests des blobs historiques. Ce protocole confirme la fidélité de migration et les intégrités cryptographiques, pas la vérité substantielle des données du domaine.
