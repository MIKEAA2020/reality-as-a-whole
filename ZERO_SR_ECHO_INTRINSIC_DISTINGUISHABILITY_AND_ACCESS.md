# Intrinsic distinguishability and access in the SR-inspired echo

## Result

The [preceding analysis](ZERO_SR_ECHO_COORDINATE_EQUIVALENCE_AND_CONTENT.md) showed that nonzero rescalings of the candidate quality coordinates can be mere changes of description. This pass asks what the same echo fixes **without choosing a coordinate scale** and what an explicit physical access mechanism would do to it.

On the selected two-branch echo sector, quantum trace distance gives an exact, basis-independent measure of physical state distinguishability. It exposes a distinction missed by the earlier `(S,T)` outcome table: two coherent states can have exactly the same S and T outcome probabilities and still be perfectly distinguishable by a phase-sensitive effect.

A new, explicitly constructed **clock-invariant unsharp pointer write** also shows a continuous tradeoff for one specified state and instrument. With pointer-state overlap `r=3/5`, the best pointer-only guess of the two T branches succeeds with probability `9/10`; the retained record coherence has visibility `3/5`; and the unconditioned record-history fidelity is `4/5`. The pointer has a distinct ready state and the construction preserves the reduced stationary clock constraint.

These are mathematical results for a stipulated physical model—not an identified qualitative metric, an actual subject or evidence that the pointer is subjectively accessible. No phenomenological identity is assumed to follow automatically from distinguishability. Code and tests: [intrinsic-access checks](verification/zero_sr_echo_intrinsic_access_test.py).

## 1. The same echo, selected before an additional saved record

At the established post-echo anchor, select the `M=+`, `R=−` sector. The two supported angular/J branches have equal conditional weight `1/2`, common `G=3/16`, and `T=+1` or `T=−1`. The earlier [complex-vector analysis](ZERO_ECHO_CONSTITUTIVE_MODES_AND_COHERENCE.md) verifies their orthogonality and support in the original echo, for the specified tested sources. Let their normalized branch vectors be `|e₊⟩,|e₋⟩`, with any existing relative phases absorbed into the basis.

This section uses the original selected coherent echo, **not** an additional saved-J memory silently assumed absent from its state. If that memory is included and entangled with the branches, the reduced old carrier can have different coherence; a joint measurement including the memory is a different interface. Likewise, postselection and the following phase-sensitive effect are not shown to be locally available to a subject.

Within the two-dimensional isometric branch representation, every density matrix has the form

```text
ρ(p,c) = [[p, c], [c*, 1−p]],
0≤p≤1,    |c|²≤p(1−p).
```

Here the basis labels refer to the physical T record. They are not established phenomenal labels. In particular, a superposition need not possess one definite Q value from a table of eigenvalue outcomes.

## 2. A physical metric derived from distinguishability

For two such states `ρ=ρ(p,c)` and `σ=ρ(q,d)`, define trace distance

```text
D(ρ,σ) = ½ ||ρ−σ||₁ = √[(p−q)²+|c−d|²].
```

The final equality follows by diagonalizing the traceless Hermitian `2×2` difference. This is invariant under a simultaneous unitary change of basis. More operationally, if the two preparations have equal prior probabilities and one may perform **any** effect on this two-branch carrier, the optimal correct-guess probability is `(1+D)/2`. The optimizing effect is the projector on the positive eigenspace of `ρ−σ`. The verifier checks these statements for real and complex coherences.

The metric is intrinsic to the declared quantum state space and its full effect algebra in a precise mathematical and operational sense. It is not automatically intrinsic to the experience of a subject: the allowed effect may be global, a subject may access only a restricted algebra, and phenomenal similarity need not equal operational distinguishability. The quantum description and Born rule are themselves premises, not derived from the self-sufficient whole by this calculation.

Restricted access gives different discrimination:

- **S only:** both states are entirely in `S=0`, so the outcome statistics are identical.
- **T only:** the total variation distance of the two binary outcome laws is `|p−q|`.
- **All effects on the two-branch carrier:** the optimal distance is `√[(p−q)²+|c−d|²]`.

For example, for diagonal states with `p=.8` and `q=.2`, T alone gives distance `.6` and optimal success `.8`. The T-only distance can be smaller than the full physical distance; an access restriction is therefore substantive, not a change in the underlying state.

## 3. A distinction hidden by both mode statistics

Consider the actual selected balanced state and a second state obtained by an **additional stipulated phase flip** on one branch:

```text
|ψ₊⟩=(|e₊⟩+|e₋⟩)/√2,     |ψ₋⟩=(|e₊⟩−|e₋⟩)/√2.
```

Both give `S=0` with certainty and `T=±1` with probability `1/2`. Their candidate mode-outcome distributions, including all invertible κ relabelings, are identical. Nevertheless `⟨ψ₊|ψ₋⟩=0` and `D=1`, so an ideal phase-sensitive effect can distinguish them perfectly. T dephasing makes their reduced states identical, reducing the physical distance to zero for that channel.

This does **not** prove that the two phases feel different. It does establish that a candidate identifying experience solely with the definite `(S,T)` *outcome label* leaves out a physical distinction in coherent states. A more complete constitution must say whether and how coherent phase is relevant, how it is accessed, or why it is not part of the relevant experience. It cannot infer a definite outcome pair for an unmeasured superposition merely from the PVM.

The `Qκ=G(S,κT)` relabelings also leave the same physical T projectors intact for κ≠0. The fact that `Q₀` merges their outcome labels does not remove the underlying distinguishability or prove that it is felt. This respects the earlier distinction between passive coordinate change and a non-invertible coarse description.

## 4. An explicit stationary unsharp access instrument

Use the existing [reduced 20-step clock](ZERO_ECHO_MODE_INSTRUMENTS_CLOCK_TRANSPORT.md), with shift W and the twirled, orthogonal anchor-mode projectors `Π₊`, `Π₋` for `(S,T)=(0,+1),(0,−1)`. They commute with W. Let `Πrest=I−Π₊−Π₋`.

Add a three-state pointer with a distinct `|ready⟩` and two orthogonal output basis states `|0⟩,|1⟩`. For `0≤r≤1`, choose pointer unitaries `V₊,V₋` satisfying

```text
V₊|ready⟩ = |0⟩,
V₋|ready⟩ = r|0⟩ + √(1−r²)|1⟩.
```

Both written pointer states are orthogonal to ready, so a write is distinguishable from no write even when they overlap one another. Define

```text
U = Π₊⊗V₊ + Π₋⊗V₋ + Πrest⊗I.
```

Orthogonality and completeness of the Πs make U unitary; their commutation with W gives `[U,W⊗I]=0`. The implementation constructs the full `480×480` reduced-history/pointer unitary and checks unitarity and commutation. The two normalized stationary branch histories `|E₊⟩,|E₋⟩` are prepared by transporting the anchor record basis states through the existing cycle. They are an isometric representation of the two selected record branches, **not** the full old carrier, angular apparatus and environment.

On the balanced stationary input `(|E₊⟩+|E₋⟩)/√2`, tracing out the pointer produces off-diagonal branch element `r/2`. Consequently, for this state and real overlap:

```text
visibility V = 2|⟨E₊|ρhistory|E₋⟩| = r,
F = ⟨ψ|ρhistory|ψ⟩ = (1+r)/2.
```

For equally likely definite input branches, the conditional pointer states have trace distance `Dpointer=√(1−r²)`. An optimal pointer-only measurement therefore has

```text
Pcorrect=(1+√(1−r²))/2,
Dpointer²+V²=1.
```

At `r=3/5`, the exact values are `Dpointer=4/5`, `Pcorrect=9/10`, `V=3/5`, `F=4/5`. At r=0, the pointer records the branch perfectly but removes this coherence; at r=1 the two written pointer states agree, carry no branch information, and leave this coherence unchanged. The tests verify the conditional pointer states, the reduced density matrix, and preservation of the W=1 constraint.

This tradeoff is **not a universal law for every instrument or state**. It is an identity for the declared pure balanced input and this particular controlled unitary, with the specified pointer optimum. It also does not establish that the globally clock-conditioned U has a local laboratory implementation, costs no energy, or is read by an experiencer. If the pointer is read or reset, those further operations and any losses must be included. Its physical backaction is a feature of the modeled *intervention*; it does not introduce an external agent to make an algebraic identity true.

## 5. What this says about subject and qualitative identity

The physical pointer measures a mode record. A subject-access proposal must additionally specify **which physical entity, if any, is a subject**, whether it can access the relevant pointer or interference effect, what is experienced, and how the reporter and time windows are aligned. The first-person evidence of actual experiencers should be taken seriously; the model's ordinary pointer bit is not itself such evidence.

The previous persistent-ledger and momentary-ledger hypotheses may assign different owner labels to the same recorded trajectory while leaving the defined state, U and pointer statistics unchanged. Our code's ownership control reflects exactly this restricted construction: owner labels do not enter its physical circuit. It does not prove that two complete physically identical worlds with different subject facts are possible, nor that a richer physical/experiential constitution could not settle identity. A real ownership-sensitive channel would be another specified interaction, requiring appropriate independent calibration and backaction accounting.

A useful next hypothesis could identify an experience with a suitable *whole state and accessible algebra*, rather than a single eigenvalue vector. But this is not forced by trace distance. Even if its state-space metric is operationally derived, we still need reasons to map that metric—or some other relational structure—to actual felt similarity, ownership and incidence. A subjective metric may be non-Euclidean, context-dependent, or not exist in the simple form proposed. Agreement with reportability alone is not equivalent to establishing phenomenal quality.

## 6. Why this advances the SR analogy—and where it stops

1. **Internal determination:** state, effect and pointer relations give the distances, success probability and coherence tradeoff without an outside force supplying the resulting values.
2. **Coordinate independence:** the quantum trace distance is basis invariant, and nonzero rescaling of the proposed Q labels does not change the T projectors. The physical effect set, not the units in which Q is written, determines the operational result.
3. **Same carrier, different access:** S-only, T-only and phase-sensitive effects reveal different distinctions. This illustrates why an apparent zero can be a coarse description, not a disappearance of structure.
4. **Not yet experiential necessity:** none of these facts identifies a subject or proves that physical distinguishability is a lived distinction. Nor does the reduced clock derive the actual full carrier, occurrence measure or self-sufficient whole. A genuinely constitutive identity, if justified, would not need an external causal bridge; the missing work is to establish *which* identity and its subject/quality/incidence consequences.

The most direct next step is to define an experimentally or independently supported qualitative relation and compare its predictions with both T-only and phase-sensitive physical access, including an actual candidate subject and the cost of its matched interface. A negative or ambiguous result should be allowed to challenge the candidate, rather than being absorbed into an unfalsifiable identification.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. python -m unittest \
 verification.zero_sr_echo_intrinsic_access_test \
 verification.zero_sr_echo_coordinate_equivalence_test \
 verification.zero_echo_constitutive_modes_test \
 verification.zero_echo_mode_clock_transport_test -v
```

These checks cover the finite quantum model, specified effects, conditional pointer and reduced clock. They do not establish consciousness, phenomenological calibration, locality or actual subject incidence.
