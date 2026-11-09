# Mechanical Study Candidate Contract (noncanonical)

## Purpose and boundary

This additive contract describes one bounded mechanical study without rewriting the historical `typed_mechanism_effort_motion_graph`. It is **not** an approval to size, manufacture, operate, repair, inspect or certify real machinery. `schemas/mechanical-study.schema.json` specifies structure; `tools/validate_mechanical_study.py` enforces selected physical and epistemic invariants using only the standard library.

## Semantic layers

- **Geometry/material:** actual dimensions, properties, measurement provenance and units; descriptive model input, not an accepted design fact.
- **Loading and boundary:** explicit load identity, magnitude, operational bounds, supports, temperature and assumptions. Undeclared limits block numerical acceptance.
- **Model/calculation:** supported equations are deliberately enumerated. Force (`N`), torque (`N m`), stress (`Pa`), strain (`1`), speed (`m/s`, `rad/s`) and power (`W`) have distinct quantity types. Even when torque and energy share an SI dimension, their semantic roles are incompatible.
- **Test/evidence:** an observation is a measurement with date, conditions, uncertainty and catalogued provenance, not validation of the entire system.
- **Failure:** observed symptoms, failure mode and *alternative causal hypotheses* remain distinct; no automatic root-cause confirmation, intervention permission or safety certification.

## Supported equations (SI inputs)

| equation | inputs | output | applicability |
| --- | --- | --- | --- |
| axial_stress | force N; area m2 | stress Pa | nominal average axial stress only |
| axial_strain | stress Pa; modulus Pa | strain 1 | linear elastic, homogeneous assumption |
| rotational_power | torque N m; angular_speed rad/s | power W | instantaneous mechanical shaft power |
| linear_power | force N; linear_speed m/s | power W | collinear force and velocity |
| delivered_power | input_power W; efficiency 1 | power W | efficiency must have evidence and a modeled-loss declaration |

All inputs require declared ranges; numeric values must lie inside them, and reported results must be consistent within a narrow computational tolerance. The validator does **not** prove the selected formula applies, the underlying material is correct, fatigue life, stress concentration, instability, tribological behavior or measurement accuracy. It does not perform finite-element analysis.

## Provenance and standards

Only IDs existing in the checked-out `sources/source-catalog.json` may be referenced. Their stored title, locator and retrieval metadata remain historical. NIST SP 330 section 2 (https://www.nist.gov/pml/special-publication-330/sp-330-section-2) supports SI dimensional distinctions and specifically distinguishes torque from energy. Its online material was consulted on 2026-10-24. It is **not** a design code or test certification. Other catalog entries are not independently re-verified here. Every *new* record states edition, date, applicability and epistemic status.

Synthetic material numbers are tagged `property_basis: synthetic_only`; the NIST catalog reference is a reference for SI unit semantics, **not** for the sample elastic-modulus value. Real material data would require separate documented property evidence and human review. An experimental record must cite `epistemic_status: observation` and must not cite a published unit standard as if it were a laboratory report.

## Execution

From this Kristal's root:

```sh
python tools/validate_mechanical_study.py examples/mechanical-study-valid.json
python -m unittest discover -s tests -p 'test_mechanical_study.py' -v
python knowledge-base/tools/validate.py
```

Use the pinned Local Kit separately for `check`; `build-v9` only on an isolated copy. Do not run `publish-v9`, `activate-v9`, v11 enrollment, diK changes or remote sync. Qualification requires independent authority.
