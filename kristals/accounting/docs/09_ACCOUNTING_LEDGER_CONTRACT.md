# Candidate accounting ledger contract — noncanonical (v1.0)

This is a **noncanonical, read-only exchange-validation contract** layered onto the
existing `accounting_event_ledger_graph` native model. It is not an accounting
software posting engine, compliance certification, canonical schema migration,
or proof of the authenticity of accounting evidence.

## Native layers and independent identities

| Domain layer | Candidate JSON location | Why separate |
| --- | --- | --- |
| Economic event | `economic_events[]` | An observed event is not recognition, an entry or a causal proof |
| Source document and evidence | `source_documents[]` | The original evidence has its own document identity, locator and source |
| Recognition / accounting basis | `accounting_basis` | Declared version and source; not a presumption that IFRS or local rules apply |
| Journal entries and debit/credit lines | `journal_entries[]` | Posting date, evidence refs, side, account and currency are explicit |
| Account and ledger | `accounts[]`, derived `general_ledger` | Account ≠ financial statement line; ledger derived from journal by account |
| Fiscal year, period and close | `fiscal_year`, `periods[]` | Interval, status and closure evidence independent of entry |
| Trial balance | derived `trial_balance` | Deterministic account/currency/period aggregation, not a separate recorded event |
| Forecast / projection | `projections[]` | Never included in journal, ledger or trial balance totals |
| Source provenance | `sources[]` | Declared publisher, version, date, locator, jurisdiction and epistemic status |

`reports` are computed on demand and carry the marker `DERIVED_NONCANONICAL_NOT_POSTED`.
They must not be mistaken for accepted balances, published accounts, an activated
read-surface, or a validated State Commitment.

## Invariants tested

- JSON Schema 2020-12 and real calendar dates. Amounts are decimal **strings**;
  floating point values, negative and zero entry lines are rejected. Arithmetic
  uses Python `decimal.Decimal` and does not silently round.
- Stable typed references and global unique IDs across entity classes; journal
  line IDs unique within each entry. Evidence references resolve, and each
  journal document references the **same event** as its entry.
- Fiscal periods must belong to the specified exercise, fall within it, and not
  overlap. Entry posting date must be in the referenced period and within the
  accounting basis validity. Closed and locked periods require a document ref.
  **This does not authenticate a closure or authorize future postings.**
- Every journal entry balances debits/credits in **one currency**; no implicit
  exchange-rate conversion or cross-currency compensation is allowed. Debits and
  credits are also checked per period/currency. Currency codes are 3-letter
  uppercase candidates; ISO-4217 status is **not** independently checked.
- Ledger and trial balance are produced only from valid posted-example lines;
  projections remain forecast evidence, excluded from actuals. A journal is
  event history, not proof of underlying causality or current state.
- Source metadata and basis refs are mandatory. Source authenticity, effective
  legal scope, standards compliance, completeness of real transactions and
  approval by competent accountants require separate authority.

## Example commands from the Kristal root

```bash
python tools/validate-accounting-ledger.py examples/synthetic-accounting/valid_balanced.json --report /tmp/accounting-derived-report.json
python tools/validate-accounting-ledger.py examples/synthetic-accounting/reject_unbalanced.json
python -m unittest discover -s tests -v
python tools/validate-standardization.py
python tools/kristal.py check .
```

The first command is expected to exit zero. Negative examples intentionally exit
nonzero. The validator changes no files unless `--report` explicitly specifies an
output location. The output is a **derived local report**, not a journal posting.

`tools/kristal.py check .` is the *historically adapted Accounting-local Kit tool*.
The **unmodified external Kit v4.0.0-draft.3** can reject the original historical
`source-bundle` materialization: it is a documented build input, not a third
canonical v9 member. Do not erase or admit it to canon as a shortcut. The only
historical build protocol allowed here is the adapted
`tools/build-preserving-v9.py` on an isolated copy after prerequisite checks.

## Limits and future decisions

No real organizational accounts, source documents, balances, exchange rates,
regulatory jurisdiction, accounting-period authorization or authenticated
responsible person are included. The sample source is explicitly **SYNTHETIC**.
The corpus's existing IFRS references are historical source **metadata**, not
freshly verified compliance opinions; references must be checked by domain
reviewers before use. The candidate contract is not a claim that it maps all 581
legacy v6 assertions, or that v11/KQ/KP/KA/KS identities have been allocated.

Framework v11 remains opted out. Future activation, if desired, requires reviewed
namespace-qualified identity registry, evidence mappings, diK handling when
appropriate, independent Framework v11 qualification, and explicit authority.
Do not use Wikidata as a foundation for operational accounting claims.
