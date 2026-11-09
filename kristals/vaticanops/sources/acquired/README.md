# Public document source captures

No additional official sources are bundled here at packaging time because live
outbound downloads are blocked in the file-building environment.

On an Internet-connected computer run `VaticanOps_Synchroniser.pyw` or
`python tools/sync_official.py sync --all`. Each acquired item is stored
under its ID with the original bytes, text extraction if HTML, SHA-256 digest,
and a mutable acquisition manifest. This layer is **derived, not canonical**:
acquisition alone is not legal review, consolidation, or authorization.

Use `python tools/discover_official.py` after collecting indexes to enumerate
possible additional document links for later human curatorial selection.
