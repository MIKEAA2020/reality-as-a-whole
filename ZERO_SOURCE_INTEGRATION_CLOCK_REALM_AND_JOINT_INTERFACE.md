# Source integration, fourth pass: clocks, realm access and a joint echo constraint

## A constructive question across the existing sources

**Coherent continuation:** [one angular–reservoir quantum history](ZERO_COHERENT_ANGULAR_RESERVOIR_CLOCK_ACCESS.md) composes the original quantum echo and full purified reservoir, checks the same reference-conditioned predictions and coherent clock entries, and supplies a stationary randomized-anchor POVM. Bare reference projectors are not themselves stationary; access remains explicitly conditional.

The user has emphasized that a confined surface/game inhabitant does not automatically access the traveler/player's richer realm, and that time is relational rather than a preferred external clock. Earlier work already joined Page–Wootters to the sphere and constructed two differently correlated internal reference clocks using [TIME/DATA's clock-map question](ZERO_STRUCTURAL_TIME_TWO_CLOCK_STATIONARY_BRIDGE.md). [Kent's supplied paper](KENT_LORENTZIAN_QUANTUM_REALITY_FULL_PAPER_AUDIT.md) supplies a related but different idea: which boundary records are admissible varies by spacetime location. This pass adapts the **need for explicitly scoped access**, not Kent's specific future-boundary prescription or single-history ontology.

The implementation joins the earlier typed B-claim correctness and the `sj`/`sjr` candidate-quality contrast **in the same clock-conditioned physical event**. The exact tests use the existing 20-tick sphere ledger under both clean and thermal auxiliary preparations, and the two previously defined q=1 and q=2 reference-clock relations. The clocks and their preparation are additional model inputs; they are not derived from zero.

## 1. Audit and plan

- **TIME/DATA:** its identity/difference/compatibility/reconfiguration grammar points toward tracking what a reference actually distinguishes; its proposed clock map was not derived by the source. Retain the question, not its unproved field or cosmological conjectures.
- **Page–Wootters:** stationary joint correlations can represent internal change, but an abstract global observable is not automatically available to a confined subject. Keep the joint effect and explicitly specify the access needed to condition on it.
- **Kent:** its point-dependent selection of spacelike final records is not a general theorem that all global or later records are locally accessible. Kent assumes background Lorentzian geometry and a selected final configuration, so neither is imported as an emergent-spacetime derivation. We use his insight as an **access-design constraint**, not an implementation of his cone rule.
- **The user's surface/game analogy:** keep the subject, its accessible records and the richer observer distinct. No j-only subject is granted the B, M, echo or reference registers without a specified coupling and accessible algebra.

**Plan:** on the current model's fixed normal claim `c=r` and independently specified B target, pair the physical correctness event with the difference between the two already proposed candidate signs. Then condition their joint distribution on each existing reference clock's reading 2. This makes the access and the actual joint prediction explicit rather than putting the physical and experiential questions into unrelated models.

## 2. The joint event yields a sharper constraint

Define

```text
C := (r=b)                      normal physical claim is correct
D := (s j ≠ s j r) = (r=−1)    two candidate quality signs differ.
```

On the old ready-state physical support, an exact all-tick result is

```text
P(C=false and D=true | tick t) = 0   for every t=0,…,19.
```

The reason is specific to this history: the B-positive branch has pre-echo `z=+` only, and its record stays `r=+` throughout; hence any `r=−` has B-negative and the `c=r` claim is correct. On B-negative branches the reverse inference need not hold. The test checks the complete joint table against the original sphere/reservoir ensemble for **every tick** and for both auxiliary preparations. It does not assert that the signs are felt or that the model's B is a humanly meaningful target.

This joined result is useful in designing a real discriminator: **within this model**, observing normal physical claim errors is not a way of sampling cases where the two quality rules disagree. Conversely, a record that correctly predicts B need not discriminate the two candidate qualities. To compare the latter requires their independently justified phenomenal/report interface and actual access to the relevant M, j and E records. The fact that a global model can form the conjunction is not evidence that a confined subject can form or report it.

## 3. The two internal clocks yield different joint tables

Use the already specified extra four-state reference R with `R=q t mod 4`, q=1 or 2, conditioned on `R=2`. These are **different correlated physical clock preparations**, not merely different coordinate names. Denote by `D` the physical predicate above, not an independently experienced observation. Exact conditional Born weights are:

| Clock | `P(C,D | R=2)` | `P(C,¬D | R=2)` | `P(¬C,D | R=2)` | `P(¬C,¬D | R=2)` |
|---|---:|---:|---:|---:|
| q=1 | 1/10 | 1/2 | 0 | 2/5 |
| q=2 | 1/20 | 1/2 | 0 | 9/20 |

Thus the already known echo-claim correctness rates are `3/5` and `11/20`, while the candidate-sign disagreement rates are `1/10` and `1/20`. The new point is their **joint** relation: all disagreement lies in the correct-claim cell, and the additional clock changes its incidence in the selected physical subensemble. A selected `R=2` cell has probability `1/4` for q=1 and `1/2` for q=2; under q=2, readings 1 and 3 have zero weight, so conditioning on them is undefined. Tick 20 is the same clock label as tick 0.

As in the prior two-clock construction, correlating the new reference dephases some off-diagonal clock-history coherences if it is traced out. The table follows from the specified joint clock preparation and diagonal effects; it is not a claim that adding the reference leaves the complete unconditioned state identical. Different ticks here describe alternatives in a specified joint protocol, not simultaneous invasive readouts. The quality-disagreement predicate is model structure, not a first-person incidence measure.

## 4. Access and next constitutional job

For this calculation an analyst uses B, r, j, s and R in the stated modeled joint interface. A proposed subject restricted to j or to a surface/game realm is **not** thereby granted those degrees of freedom. An actual subject-level implementation must explicitly provide the relevant interactions, detector states, operational scope and report-error model. Nor does the clock/reference comparison entail a background Lorentz cone, a detector inside it or an operational signal between realms. Kent's spacelike rule would need a separate geometry, final-data instrument and limit proof before it could be implemented here.

The implementation is [verification/zero_stationary_clock_claim_quality.py](verification/zero_stationary_clock_claim_quality.py), with [three tests](verification/zero_stationary_clock_claim_quality_test.py). It carries TIME/DATA's clock-comparison problem and the access lesson from Kent into the same sphere battery candidate, rather than treating them as solved rival theories. What remains is to derive a physical geometry and access law, the actual experiencer and quality map, and the physical–experiential incidence measure from the proposed constitution; finite model compatibility does not by itself accomplish those goals.

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. python -m unittest \
 verification.zero_stationary_clock_claim_quality_test \
 verification.zero_stationary_battery_bridge_test \
 verification.zero_structural_time_stationary_two_clock_test -v
```
