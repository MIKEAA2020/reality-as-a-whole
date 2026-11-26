# Ownership, a physical report and the symmetry it must carry

**Calibration follow-up:** [the ownership-report root-cause diagnosis](ZERO_ECHO_OWNERSHIP_REPORT_CALIBRATION_ROOT_CAUSE.md) gives exact conditional discrimination thresholds and an error-correlation control; physical B accuracy is not itself identity calibration.

**Next dependency:** [causal access and refinement on the echo](ZERO_ECHO_CAUSAL_ACCESS_AND_SUBJECT_REFINEMENT.md) tests a local support criterion against actual gate timing, logical encoding, record-access sets and overlap accounting; it does not infer subjects from the resulting graph.

## Main result

The preceding [persistence and record construction](ZERO_ECHO_SUBJECT_PERSISTENCE_RECORD_AND_ACCESS.md) left an actionable question: can a real report distinguish two explicit subject-ownership rules on the existing echo, rather than simply assume that it does? This pass builds the comparison into the same quantum history, checks its symmetry and asks what an incidence census would mean.

The strongest results are conditional but concrete:

1. A reversible report qubit can record the product of saved pre-echo J and current J. On the supported echo this product equals B and the original echo record R. Thus it is an exact **physical B report**, not yet a report of personal identity.
2. The saved J record **breaks the previously established bare type-swap symmetry**. The repair must also flip the saved memory on the R-negative sector. This dressed operation preserves the recorded quantum state and comparison report in the tested histories, while the constrained opposite-pair signs transform as required.
3. Two explicit, oppositely B-dependent ownership rules have identical physical report distributions and respect the reduced clock, type and sign symmetries. A report can discriminate them only with an independently justified bridge connecting its physical bit to an experiential identity truth.
4. A different active, state-family-adapted sector exchange changes B while preserving the tested recorded state. If it is required to preserve subject identity, both B-dependent rules fail. But this exchange also changes accessible physical observables; it is not automatically a gauge redundancy or a symmetry of the full physical–experiential laws.
5. Under a clearly stated, hypothetical equal-subject census, the two rules produce very different self-location fractions, although both have the same physical B probability. Physical weights can be maintained by a different stipulated weighting. Neither census nor weighting is derived merely from zero.

Implementation: [verification/zero_ownership_report_bridge.py](verification/zero_ownership_report_bridge.py); checks: [verification/zero_ownership_report_bridge_test.py](verification/zero_ownership_report_bridge_test.py). The subject rules, extra memory and any interpretation of a bit as a first-person answer remain model inputs. These results do not show that finite registers experience anything.

## 1. Build a report without pretending it reads a subject

Before the existing T–Q–T echo write `J=z` coherently to the additional saved memory L. At the tick-10 anchor the supported relations are

```text
j=bz,       r=b,       z j=b=r.
```

Adjoin a report bit H initially `+`, then reversibly flip H first if `z=−` and again if `j=−`. The result is

```text
H=z j=b=r.
```

The control operations are coherent controlled-NOTs: no classical hidden-path or intermediate measurement is needed. Direct checks use the original complex old-system/angular/echo states for source labels 0, 7 and 15 and both sign slices. The report `H=±` has physical weights `1/2,1/2`, and agrees branchwise with both B and R on the specified support. Since R is already available globally at tick 10, a hypothetical observer with direct access to R could infer the same B value without the additional L comparison. A j-only observer has no such right: L, R and the report bit require their own access and coupling.

This construction makes a useful trap explicit: an observer may read a reliable, reversible **physical correlation**, but its value cannot be called “same subject” unless a separate constitution connects that correlation to ownership. On this model, even a perfect B-report is consistent with opposite ownership assignments below.

The prepared L and H bits and the recording operations are additional resources, not obtained from zero. Their physical locality, energy budget and confinement are not established. The comparison instrument can be added to a modified cycle; it is not an observation invisibly inserted into the original history.

## 2. The record breaks the bare type symmetry—and how to repair it

At the anchor, the prior actual type operation D exchanges the two quality coordinates. On the supported sign sector it sends

```text
j → r j,       r → r,       b → b,
```

and reflects the two negative angular bins. Prior to adding L, D fixes the prepared angular/old-record quantum state. With the saved pre-echo J sign left untouched, however,

```text
z j  →  z r j.
```

Because initially `zj=b=r`, the transformed comparison value is `+` on **every** supported branch. Indeed, the tests find that the bare-swapped report is + with probability 1 rather than 1/2. This is an actual change in the correlation with the new physical memory, not a notational issue or a harmless global phase.

Dress D by a controlled flip of L on `r=−`:

```text
D_L:    j → r j,       z → r z,       r → r.
```

Then `(r z)(r j)=zj`: H is preserved. The code applies the actual quantum angular type swap to each saved-memory slice and flips L on its negative-R slice. On the tested original complex histories, the **entire recorded state**, not just the diagonal report law, is restored within numerical precision. The bare operation fails; the dressed one succeeds. This is a state/sector result for the specified anchor, not a claim that the dressing has been derived from the ultimate constitution or proven local.

The constrained pair is not ignored. Its anchor values are `Z₁=K=s r j=s z`, `Z₂=−K`. Under the paired physical type transformation,

```text
Z₁ → r Z₁,     Z₂ → r Z₂,
z → r z,       H → H,
```

and the reflected bin maps to the actual target bin. The tests apply the original pair encoding to complex recorded branch vectors before and after the transformation and check target signs and masses. Pair balance is retained, but opposite signs are not identified as gauge-equivalent.

The sign counterpart is a **different** operation: its clock-phase dressing and commutation with saved J were checked in the previous pass. The extra H gates depend only on J and L, so the same valid-sector commutation extends to this physical comparison; this algebraic inference is conditional on the stated controlled gates. Neither symmetry proves an invariant actual-incidence measure.

## 3. Retaining a report changes the state

Run the actual inverse echo, undo the L write, and keep H. The saved L resets while H remains correlated with B. On the specified normalized pure sign slice, the old carrier with H traced out has fidelity

```text
F = P(B=+)² + P(B=−)² = 1/2.
```

This contrasts with `5/8` for retaining only the previous saved-J memory. It is a conditional, state-specific fidelity, not a universal measurement-disturbance constant. Applying B-controlled NOT to H after the cycle coherently uncomputes the retained report, recovers the original full complex state and resets H. The tests verify the norm and the full-vector restoration for three original source labels and both signs. After uncomputation the answer is no longer a durable record; no thermodynamic cost or free permanent record is claimed.

For a noisy **physical** readout, the explicitly complete channel with Kraus operators

```text
√η I,       √(1−η) X
```

reports B correctly with probability η. It may be implemented by a prepared environment bit followed by a controlled flip and tracing that environment. At `η=9/10` the physical-bit accuracy is 90%; that is a stipulated channel parameter, not measured accuracy of any first-person identity report.

## 4. Two explicit rival ownership bridges

Use the previous reduced cyclic ledger, with initial seed `ξ=U_t⁻¹x` and a fixed proposed pair-factor label a. For successive slots on one transported seed, compare:

```text
Bridge A: B=+  → one persisting owner;   B=− → a distinct owner at each tick.
Bridge B: B=−  → one persisting owner;   B=+ → a distinct owner at each tick.
```

These are explicit candidate **constitutive rules**, not established experiences. On the 20-tick cycle the tick-indexed owner labels repeat after the cycle; no extra winding register has been postulated. Each candidate respects the specified reduced clock shift, including its closing edge. The reduced transported type flip and sign flip keep B unchanged, so each respects those maps too. Exhaustive checks cover all reduced clock/state/factor labels. The full quantum sign counterpart and the record-dressed type symmetry have their separately stated scopes above.

The candidates disagree on whether the slots at ticks 7 and 10 have the same owner in every supported B sector. Yet they use precisely the **same physical state and report law**: `P(H=+)=P(H=−)=1/2` for either rule. In a physical description that contains no subject bridge, every allowed physical measurement has the same distribution under these two interpretive extensions. This is an indistinguishability result for the specified competing descriptions, not a proof that no physical theory could ever define or report ownership.

If the report is *separately* assumed to answer the ownership question, then its conditional empirical meaning changes. With the physical bit-flip accuracy η relative to B,

| Extra assumption about ownership | Probability H agrees with that stipulated identity truth |
|---|---:|
| Bridge A | η |
| Bridge B | `1−η` |

At `η=9/10`, those values are `9/10` and `1/10`. At `η=1/2`, even the hypothetical joint truth/report tables coincide. The tests verify the exact rational tables and the quantum channel. But calibrating H against B does **not** calibrate H against first-person identity. To use the table to choose a bridge, one needs an independent, justified access to identity truth or a principled and testable theory of how truthful reports are produced. Without it, merely announcing that H means “same owner” builds the conclusion into the input. This issue is especially important in a confined realm: global B or L may not be available to the putative experiencer.

## 5. A stronger active-symmetry test rejects both bridges—conditionally

The prior [record-dressed rotation construction](ZERO_RECORD_DRESSED_SPHERE_ROTATION_SYMMETRY.md) supplies common source-span frames. Using those actual numerical frames, construct an **active** unitary that exchanges finite angular bins 0 and 2, transporting their old/echo vectors with the existing sector maps and flipping L on those bins. On three source labels and both sign slices, the operation fixes the full recorded anchor state to numerical precision. It exchanges a B-negative supported sector with a B-positive sector.

Bridge A says the 7-to-10 ownership relation is different on those sectors; bridge B says the reverse. Therefore neither preserves that equality relation under this exchange. In particular:

> If this active sector exchange is an admissible symmetry of the complete subject-identity constitution, and subject equality must be preserved under it, both B-dependent bridges are ruled out.

The condition is substantive. This is a finite state-family-adapted swap, **not a demonstrated frame-gauge transformation, a literal spatial rotation, an established local operation, or a symmetry of the complete clock/pair/energy/experiential law**. It changes B, the comparison-report observable, and individual angular magnitudes: for the prior type-compatible `g₂`, the swapped bin values are `3/16` and `5/16`. On an already written H record its action would also have to transport H; a fixed meaning assigned to the H output need not be invariant. The earlier [quotient correction](ZERO_RELATIONAL_GEOMETRY_KINETIC_MEASURE_SELECTION.md) also warns against treating all larger-carrier active actions as frame-gauge actions. Thus this is a discriminating *symmetry obligation*, not a proof that the two bridges are false in reality.

Conversely, requiring invariance under an active transformation simply because it fixes one state would be unjustified: a state can have symmetries that are not symmetries of the complete laws or accessible observables. This is exactly why the type-swap repair and this sector-swap control are reported separately.

## 6. What changes when owners are counted?

The two bridges have the same physical B marginal, `P(B=+)=1/2`, but different proposed owner multiplicities. For a sharply specified counterfactual census, assume **all six supported reduced seeds** are jointly actual, count factor 1 only, and give one unit to each distinct subject ID over the twenty cyclic clock labels. The two B-positive seeds are the two sign slices with `z=+`; the four B-negative seeds have both z and s signs.

| Hypothetical census | B+ owner IDs | B− owner IDs | naive B+ fraction |
|---|---:|---:|---:|
| Bridge A: B+ persists | 2 | 80 | `1/41` |
| Bridge B: B− persists | 40 | 4 | `10/11` |

These numbers are **not** Born probabilities and do not establish that all supported quantum alternatives are simultaneous actual subjects. They show that identifying a subject and assigning its measure are separate jobs. If, as an alternative bookkeeping hypothesis, each seed's given physical weight is split equally across the owner IDs assigned to that seed, the coarse B weights are `1/2,1/2` for either bridge. This restores the physical marginal by construction; it does not establish the correct self-location measure or that such owners exist.

Nor does replacing physical weights by this census automatically break sign balance here: both proposals treat the two s signs symmetrically. A real experiential cancellation requires the actual signed values and their actual incidence measure to obey the appropriate counterpart relation; neither follows from this count or from an operator zero alone.

## 7. Next dependency

The next viable step is to test whether a candidate subject bridge can be **derived from a physical-access/causal criterion** that is stable under admissible refinements and independent distant additions, while respecting the specifically justified symmetries rather than every state stabilizer. It must handle overlapping subjects and clock persistence without assuming that a report is truthful. If such a bridge is supplied, its induced incidence measure and actual signed balance can then be checked; locality, physical energy and the originating zero constitution remain further unresolved dependencies.

Reproduce:

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. python -m unittest \
  verification.zero_ownership_report_bridge_test \
  verification.zero_echo_subject_persistence_test -v
```
