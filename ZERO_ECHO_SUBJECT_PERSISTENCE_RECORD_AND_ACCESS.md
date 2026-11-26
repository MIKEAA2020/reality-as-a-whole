# Subject persistence, records and access on the coherent echo

**Next dependency:** [the physical report and ownership-symmetry test](ZERO_OWNERSHIP_REPORT_SYMMETRY_AND_INCIDENCE.md) implements the saved/current comparison, repairs the saved-record type-symmetry break, tests explicit ownership bridges and evaluates their conditional incidence census.

## Result and scope

This continues the [joint quality–incidence construction](ZERO_JOINT_INCIDENCE_QUALITY_OPPOSITE_PAIR_ROOT.md) at the next dependency: **what would make successive occurrences belong to the same subject, and what can the existing physical carrier actually tell us?**

A new conditional record protocol compares the old J sign before and after the actual coherent echo. It gives a real, reversible physical test of continuity of a *record*, but it does not select continuity of an *experiencer*. On the original quantum vectors:

1. A ready auxiliary bit coherently records the pre-echo sign `z`. At tick 10 its joint distribution with the current sign `j` is `(z,j)=(+,+):1/2, (+,−):1/4, (−,+):1/4, (−,−):0`. Their product determines the conserved B sign exactly.
2. The saved `z` and the gauge-constrained pair's anchor sign `K` satisfy `K=s z` in the same recorded branches. The clock-dressed sign counterpart reverses K while preserving the saved J record, as checked on actual complex histories.
3. The physical record is **not free or passive**: retaining it changes the reduced coherent state. Tracing it out gives fidelity `5/8` with the unrecorded pure tick-10 state in the specified sign slice. Undoing the actual inverse echo and then the recording gate returns the original coherent state and the ready bit; trying to reset at tick 10 instead leaves the bit non-ready with weight `1/2`.
4. Subject persistence and pair-factor ownership remain undetermined by these data. Explicit one-subject, two-subject and momentary-subject assignments have the same physical state, record statistics and opposite-pair operator identities. They are formal **conditional interpretations**, not demonstrated conscious possible worlds or evidence that subjecthood cannot be physically constituted.

The [implementation](verification/zero_echo_subject_persistence.py) and [tests](verification/zero_echo_subject_persistence_test.py) use the existing original angular/echo quantum vectors, including the physical pair encoding. The added memory, its preparation, and its recording interactions are stipulated. No experience is inferred from a quantum outcome.

## 1. Three different identity questions

At clock ticks 7, 10 and 13, distinguish:

* **Physical carrier transport:** the specified gates unitarily carry the old system, echo record and angular register through T–Q–T and its inverse. This is established on the physical model.
* **Occurrence identity:** if there are experiences at different clock readings, they can be *distinct successive occurrences* even if a subject persists. A before and an after are not automatically one instantaneous occurrence because their carrier returns.
* **Subject ownership:** a relation that assigns those occurrences to subjects. It is not a tested projector or an established first-person report in this model.

For one conditional history, the implementation offers three nonidentical equivalence relations over the three clock-indexed occurrence **slots**:

```text
persistent:  (A,A,A)    fresh: (A,B,C)    returning: (A,B,A)
                  ticks 7,10,13
```

These are simple controls, not an exhaustive theory of identity. All have the same actual physical vectors and the same physical predictions, because the ownership relation is an additional interpretive input and is not used in the gate equations. Returning is included to expose the assumption that causal continuity must also be experiential continuity; it is **not** claimed that a real subject could disappear and recur.

For the two transported constrained-pair factors at those three ticks, likewise consider six structural slots. One composite owner, two persistent factor owners, and six momentary owners yield 1, 2 and 6 subjects respectively under their stipulated partitions. Pair signs `K,−K`, physical coherence and record results are identical. The pair extension is an isometric encoding, not two freely prepared copies of the old quantum state; the six slots are labels for proposed ownership of pair-factor observables, not six established subjects. More general overlapping or nested subjects are not captured by these simple partitions; the [Miller audit](MILLER_SUBJECT_PARTHOOD_AND_DECOMBINATION_AUDIT.md) cautions against treating physical overlap as proof of shared experiential tokens.

There are also two explicit **physical-history-based rule candidates**, rather than just three arbitrary partitions. On the existing reduced 20-tick ledger, write `U_t` for the actual cyclic prefix, let `x` be the state at t, and let `a∈{1,2}` be a stipulated transported pair-factor label. Define

```text
worldline owner(t,x,a) = (U_t⁻¹ x,a),
momentary owner(t,x,a) = (t,U_t⁻¹ x,a).
```

Along a single transported branch these give respectively one and twenty owners per factor over the cycle. Both are covariant under the actual one-tick shift including the 19→0 closure: worldline labels stay fixed, while momentary owner labels rotate with the clock. Both also preserve the equality relation under the existing *reduced* transported type flip and sign flip; exhaustive tests cover all 320 reduced clock/state slots, both factor labels, and cross-tick pairs along each seed. Thus even demanding cyclic time covariance plus these symmetries does not select persistence. The rules are functions of the specified reduced clock and carrier, but they are candidate **bridges to ownership**, not physical proof of a subject. The original complex-history sign counterpart additionally requires its clock phase, checked separately below; a proof of full quantum experiential equivariance would require a defined subject bridge.

There is a substantive caveat: the worldline rule singles out an initial-clock label and distinguishes different seeds. Its covariance under the specified transport does not show that a confined observer can access that seed, or that the rule is fundamental, preparation-independent, or invariant under every possible unitary change of description. The momentary rule likewise uses a clock tick as an identity input. Since the clock is cyclic, its twenty IDs recur on the next mathematical cycle; distinguishing repeated laps would require an extra winding record not present here. Neither rule is asserted as the necessary constitution of reality.

A separate fair binary tag illustrates the refinement issue. If physically coupled and recorded, it gives two **distinct physical outcomes**, each with weight `1/16` inside a previous `1/8` cell; their sum remains `1/8`. For either ownership rule one may assign both refined outcomes the same owner, or include the tag in the owner ID and assign two owners. Both are explicit extensions of the bookkeeping; neither follows from physical weight additivity. This is not a claim that genuinely different outcomes are aliases, nor that adding a coin is operationally free. The verifier tests the ownership extensions and exact weights as an abstract product refinement; it does not implement a second quantum recording circuit.

**Limited no-selection result:** the displayed physical state, its echo, the pair constraint and the specified record probabilities do not *by themselves supply an ownership rule*. This is not a theorem that no other physical principle can select one; it says what a proposed constitution must add or derive. A complete physical–experiential theory could identify ownership through a specific further physical structure, but it must specify it rather than infer it from the bare availability of a clock, a memory, or opposite signs.

## 2. A concrete before/after instrument

On each supported branch before the echo, the old signs are `B=b`, `J=z`, echo memory `R=+`, and sign pointer `M=s`. The actual T–Q–T map takes these to

```text
J=j=b z,        R=b,        Q_now=s b z,        Q_echo=s z.
```

Add a separate two-state memory L, initially ready in `|+⟩`, and apply the J-controlled reversible gate

```text
C_J = P_(J=+)⊗I_L + P_(J=−)⊗X_L,
C_J (|ψ⟩|+⟩) = P_+|ψ⟩|+⟩ + P_-|ψ⟩|−⟩.
```

The gate is unitary because `P_+` and `P_-` are complementary orthogonal projections. This is a coherent record, not a measurement or a claim that its value is already experienced. Apply the original echo pulses, then compare L with J. On the specified N=4 physical history their exact physical joint Born table, summed over angular and pointer labels, is

| saved `z` | current `j` | weight | `b=zj` |
|:---:|:---:|---:|:---:|
| + | + | 1/2 | + |
| + | − | 1/4 | − |
| − | + | 1/4 | − |
| − | − | 0 | + |

The result is checked directly on the old complex source vectors for labels 0, 7 and 15 and both pointer signs, using `j_project` and the original `pulse` operations. Earlier tests establish the underlying echo relations on all 16 original source labels. No independent preparation of a classical hidden trajectory is assumed; the joint table is obtained by the explicitly coupled record and a final commuting effect.

At anchor tick 10, the physical constrained pair is `Z₁=K=s r j`, `Z₂=−K`. Since `r=b` and `j=bz`, the actual record gives

```text
Z₁=K=s z,      Z₂=−s z,
(Q_now,Q_echo) = (r Z₁,Z₁).
```

The tests encode the actual recorded branches in the existing constrained pair and check both signs. The extra memory can also be carried through the echo separately from the pair; extending the pair encoding and transported gates requires the same physical-sector/dressing care as before. This calculation is not a newly demonstrated independent subject on either pair factor.

## 3. A record has coherent cost and can be undone

The pre-echo weights of `z=+` and `z=−` are `3/4` and `1/4`. They are coherent components of each specified normalized sign slice. Retaining L entangles it with the old carrier. If L is ignored, the old system is dephased between the two J sectors. Its fidelity with the original **pure, unrecorded sign-slice state** at tick 10 is

```text
F = (3/4)² + (1/4)² = 5/8.
```

This is a comparison of the normalized old/angular/echo state in the fixed sign slice with the reduced state after tracing L; it is not a universal fidelity for an arbitrary input. It demonstrates why the time-comparison protocol cannot be presented as a costless observation of an untouched original history.

The same T–Q–T in reverse returns the carrier to tick 7's state at tick 13. Applying `C_J` again then disentangles and resets L to `|+⟩`, preserving the whole old complex state, including relative phases. The tests also use a deliberately complex relative phase across the J sectors. The memory does **not** remain available as a lasting record after this coherent uncomputation.

By contrast, applying the same reset gate immediately at tick 10 compares against the *current* J, which differs from saved z when `b=−`; the final L is non-ready with physical weight `1/2`. Resetting an unknown independently retained record or exporting a permanent copy requires additional assumptions and may incur costs. No thermodynamic dissipation claim follows from this reversible circuit alone.

The added register has not been derived from zero, and its gates have not been shown to satisfy a chosen physical energy, locality, or realm-access restriction. The clock must be supplied with the extra operations: a cyclic history can be constructed by inserting the J-controlled write at the echo entrance and its inverse after the actual inverse echo, but it is a **modified clock cycle**, not the original one with an invisible memory. The existing purified apparatus remains unchanged across ticks 7–13 in each B block; nevertheless no new detailed energy-conservation theorem for this write has been proved.

## 4. Counterpart, clock and pair are not discarded

The earlier physical counterpart is the old-system exchange `S` together with sign flip `s→−s`. Since S commutes with J on the valid sector, it also commutes with the J-controlled memory write. The necessary `(-1)^n_Q(t)` clock phase is still required across Q pulses. On representative original vectors, both sign slices and both saved-z memory slices, the tests directly verify the dressed relation at every tick 7–13. It reverses both candidate quality signs while leaving the physical saved-J label unchanged; a nonzero opposite sign remains a distinct modeled value.

The opposite-pair identity is exact in the pair's valid sector and is transported by the already specified history dressing. The new record can be coherently uncomputed as above; the test checks its compatibility with the actual pair at the anchor. It does **not** show that either pair sign is a feeling, that a sign counterpart maps actual subjects, or that actual incidence weights are invariant. In particular, zero physical pair sum does not force zero weighted subject sum under unequal incidence multiplicities.

## 5. What a confined readout can and cannot tell

The following are *optimal deterministic guesses from the specifically listed commuting sign outcomes*, under the physical table and equal sign-pointer weights. They are not bounds for arbitrary joint quantum measurements or for a different prepared state.

| available signs | target | optimal success |
|---|---|---:|
| current J only | `Q_now` | 1/2 |
| current J and saved L=z | `Q_now` | 1/2 |
| current J and M=s | `Q_now` | 1 |
| current J and M=s | `Q_echo` | 3/4 |
| current J, M=s and R | `Q_echo` | 1 |
| current J only | B | 3/4 |
| current J and L=z | B | 1 |

For example, `J=+` mixes B=+ with B=− in weights `1/2` and `1/4`, while `J=−` has B=− in weight `1/4`. Knowing s and j gives `Q_now`; the best `Q_echo` guess additionally uses the majority R value conditional on j. A j-only inhabitant has no access to M merely because a global description contains M. The extra L coupling is likewise not automatically available within a confined realm.

A **physical report bit** could discriminate ownership hypotheses only after specifying a truthful or noisy bridge from an occurrence's owner to that bit and implementing an allowed readout. For example, a stipulated 90%-accurate answer to “same owner at 7 and 10?” would statistically discriminate the persistent and fresh hypotheses; but neither that accuracy nor even the availability of the question follows from this circuit. If the competing ownership assignments retain exactly the same physical state and report law, no measurement of that unchanged physical report can distinguish them. If an added bridge gives different report distributions, it is an extra falsifiable constitutive commitment, not a consequence of silently naming the J record “subject.”

## 6. Next dependency and epistemic status

The constructive advance is a real coherence-aware before/after instrument connected to the same echo, sign counterpart and pair, plus concrete information-access limits and ownership countermodels. It separates four notions often conflated: a reversible record, an occurrence at a time, a subject continuing across times, and a report about ownership.

The next feasible task is to strengthen or discriminate the two explicit **ownership/subject-constitution rule candidates** against actual accessible algebras and histories. A promising constraint is that a proposed rule must treat reversible memory, independently accessible records and plural/overlapping subjects consistently, without collapsing counterpart signs into gauge or manufacturing new subjects from arbitrary refinements. Neither the explicit rules nor the fixed partitions here are a derived experiential law. Seek a concrete first-person/report bridge or a necessary inconsistency, not an assumed selection by time covariance.

After an ownership bridge is specified, revisit the incidence measure and its symmetry, then physical locality, energy and the zero/necessity origin. This investigation has not solved those upstream assumptions or all roadmap items, and the 90% illustration is not an experimental result.

Reproduce:

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. python -m unittest \
  verification.zero_echo_subject_persistence_test \
  verification.zero_joint_quality_incidence_root_test -v
```
